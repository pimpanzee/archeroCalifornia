import json
import os
from pathlib import Path

import shared_data as sd

TRACKER_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("TRACKER_OUTPUT_DIR", "/tmp"))

past_day_options_html = "\n            ".join(
    f'<option value="{i}">{sd.DAY_FULL_LABELS[i]}</option>'
    for i in range(7) if i != sd.TODAY_INDEX
)

invasion_data = {
    "members": [
        {
            "name": name,
            "byDay": [sd.DAY_LOGS.get(d, {}).get(name) for d in range(7)],
            "atkByDay": [
                list(sd.ATTACK_LOGS[d][name]) if d in sd.ATTACK_LOGS and name in sd.ATTACK_LOGS[d] else None
                for d in range(7)
            ],
        }
        for name, role in sd.roster
    ],
    "dayLabels": sd.DAY_FULL_LABELS,
    "trackedDays": sd.TRACKED_DAYS,
    "todayIndex": sd.TODAY_INDEX,
    "weekLabel": sd.WEEK_LABEL,
}
invasion_data_json = json.dumps(invasion_data)


def donation_row(rank, name, role, value):
    max_v = sd.donation_members[0][2]
    pct = max(2, round(value / max_v * 100)) if max_v else 2
    zero_cls = " zero" if value == 0 else ""
    flag = '<span class="chip flag">0 — flag</span>' if value == 0 else ""
    return f'''<li class="row{zero_cls}">
      <span class="rank">{rank:02d}</span>
      <div class="who">
        <div class="name-line"><span class="name">{name}</span>{flag}</div>
        <div class="bar-track"><div class="bar-fill" style="width:{pct}%"></div></div>
      </div>
      <div class="value">{value:,}</div>
    </li>'''


donation_rows_html = "\n".join(
    donation_row(i + 1, name, role, value)
    for i, (name, role, value) in enumerate(sd.donation_members)
)
donation_total = sum(m[2] for m in sd.donation_members)

template = (TRACKER_DIR / "template.html").read_text()

replacements = {
    **sd.FONT_REPLACEMENTS,
    **sd.MASTHEAD_REPLACEMENTS,
    "__TODAY_LABEL__": sd.DAY_FULL_LABELS[sd.TODAY_INDEX],
    "__PAST_DAY_OPTIONS__": past_day_options_html,
    "__INVASION_DATA_JSON__": invasion_data_json,
    "__DONATION_ROWS__": donation_rows_html,
    "__DONATION_TOTAL_FULL__": f"{donation_total:,}",
    "__DONATION_NOTE__": (
        "New week reset (wk of 8/17). All 47 members have donation counts logged as of 8/17 "
        "&mdash; Atom369, Murkchoppa, and Jackylefeu currently read 0."
    ),
}

for k, v in replacements.items():
    template = template.replace(k, v)

out_path = OUTPUT_DIR / "guild-roster.html"
out_path.write_text(template)
print("built", len(template), "chars ->", out_path)
