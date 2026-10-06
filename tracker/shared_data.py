import base64
from pathlib import Path

FONTS = "/mnt/skills/examples/canvas-design/canvas-fonts"

# The one live tracker URL. Moved off claude.ai Artifacts (2d3a73a8-...) to
# GitHub Pages on 8/25 -- Artifacts have a "pinned version" feature that can
# freeze what viewers see independent of what's actually published, and
# that's exactly what happened to guild members (stuck on 8/1 data for
# weeks). Plain static hosting has no such concept: every push to docs/ on
# main is what's live, immediately, for everyone. The old Artifact
# (2d3a73a8-...) and the older retired donations page (e6f3430a-...) are
# left alone but no longer the source of truth.
INVASION_URL = "https://pimpanzee.github.io/archeroCalifornia/"

GUILD_ID = "90754"
UPDATED_DATE = "Oct 5, 2026"


def b64(name):
    return base64.b64encode((Path(FONTS) / name).read_bytes()).decode()


FONT_BS_BOLD = b64("BigShoulders-Bold.ttf")
FONT_IS_REG = b64("InstrumentSans-Regular.ttf")
FONT_IS_BOLD = b64("InstrumentSans-Bold.ttf")
FONT_JB_REG = b64("JetBrainsMono-Regular.ttf")
FONT_JB_BOLD = b64("JetBrainsMono-Bold.ttf")

FONT_REPLACEMENTS = {
    "__FONT_BS_BOLD__": FONT_BS_BOLD,
    "__FONT_IS_REG__": FONT_IS_REG,
    "__FONT_IS_BOLD__": FONT_IS_BOLD,
    "__FONT_JB_REG__": FONT_JB_REG,
    "__FONT_JB_BOLD__": FONT_JB_BOLD,
}

MASTHEAD_REPLACEMENTS = {
    "__GUILD_ID__": GUILD_ID,
    "__UPDATED_DATE__": UPDATED_DATE,
}

# ---- Data ----
# New week: Mon 10/5 - Sun 10/11. Damage ranking (1-39 of 48) read off the
# scrollable Guild Member Ranking list; 6 screenshots this batch, no
# Manage Member screen, so donation values are carried forward unchanged
# from the 10/4 full refresh. No roster changes. The 9 members missing
# from the ranking (lllmundlll, Stumbi97, Papykique, Skytiti, Ghost192,
# Altair1165, Saludan, Mightykey, Murkchoppa) -- ranking list ended
# cleanly at rank 39 (Depfefferle336) right above the pinned own-rank
# footer, so this is the true end of the list, not a mid-scroll gap.
# Confirmed 0-attack call-out candidates per the 9/2 policy.
invasion_logged_mon = {
    "HyenA": 8.91e12,
    "Pimpanzee": 5.99e12,
    "EpicMarksman": 4.47e12,
    "elementten": 4.33e12,
    "Flforever": 4.15e12,
    "fred21422": 3.36e12,
    "Drew2264": 2.41e12,
    "BenZoo": 1.64e12,
    "P107215255": 1.26e12,
    "iBooneh": 1.21e12,
    "ScHlAnGE": 993.00e9,
    "NalaStomp": 969.72e9,
    "RonickForce": 882.83e9,
    "Atom369": 521.98e9,
    "Drakias": 491.43e9,
    "Tvojemama1": 454.61e9,
    "Ibnt": 404.71e9,
    "Rendaxx": 374.19e9,
    "Maskiert03": 372.01e9,
    "Rysor": 309.06e9,
    "REAPS": 302.31e9,
    "Ekkehard": 228.64e9,
    "BigRagaTheOppStopa": 224.86e9,
    "Nad33m": 212.89e9,
    "1RauMuong1": 163.83e9,
    "choolzy": 136.40e9,
    "Jackylefeu": 135.42e9,
    "estimov": 133.45e9,
    "IlTeino": 132.01e9,
    "tEruPmA": 87.67e9,
    "Ghoro": 82.63e9,
    "Swidishh": 56.12e9,
    "zozoxo": 51.70e9,
    "saare": 46.43e9,
    "AnyDockers": 39.63e9,
    "CzosneK": 39.18e9,
    "xavop": 23.69e9,
    "Fredolay": 13.47e9,
    "Depfefferle336": 6.49e9,
    # Not visible in the ranking (lllmundlll, Stumbi97, Papykique,
    # Skytiti, Ghost192, Altair1165, Saludan, Mightykey, Murkchoppa) --
    # unreached tail / true end of list, confirmed 0-attack call-out
    # candidates per the 9/2 policy.
}

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_DATES = ["10/5", "10/6", "10/7", "10/8", "10/9", "10/10", "10/11"]
DAY_FULL_LABELS = [f"{d} {dt}" for d, dt in zip(DAY_NAMES, DAY_DATES)]
DAY_LOGS = {0: invasion_logged_mon}
TRACKED_DAYS = sorted(DAY_LOGS.keys())
TODAY_INDEX = 0  # Monday -- the most recently tracked day
WEEK_LABEL = "wk of 10/5"

# Roster unchanged. Donation values still carried forward from the 10/4
# full refresh -- no Manage Member screenshot came in with this batch.
donation_members = [
    ("Mightykey", "Guild Member", 260),
    ("Murkchoppa", "Elder", 270),
    ("Jackylefeu", "Guild Member", 1000),
    ("Tvojemama1", "Guild Member", 1120),
    ("Skytiti", "Guild Member", 1390),
    ("Altair1165", "Guild Member", 2680),
    ("lllmundlll", "Guild Member", 2790),
    ("P107215255", "Guild Member", 2790),
    ("Saludan", "Guild Member", 2760),
    ("Atom369", "Guild Member", 2210),
    ("Fredolay", "Guild Member", 2710),
    ("saare", "Elder", 4300),
    ("ScHlAnGE", "Guild Member", 3220),
    ("Ghost192", "Guild Member", 3230),
    ("Papykique", "Guild Member", 3350),
    ("choolzy", "Guild Member", 3780),
    ("Depfefferle336", "Guild Member", 3650),
    ("tEruPmA", "Guild Member", 3870),
    ("Nad33m", "Guild Member", 3050),
    ("Ibnt", "Guild Member", 3010),
    ("zozoxo", "Guild Member", 3710),
    ("iBooneh", "Elder", 3190),
    ("Maskiert03", "Guild Member", 4210),
    ("HyenA", "Elder", 4740),
    ("Drakias", "Elder", 4830),
    ("IlTeino", "Guild Member", 4520),
    ("CzosneK", "Guild Member", 4840),
    ("Stumbi97", "Guild Member", 4660),
    ("Swidishh", "Guild Member", 4780),
    ("Drew2264", "Vice Leader", 5090),
    ("REAPS", "Guild Member", 4310),
    ("Pimpanzee", "Leader", 5450),
    ("1RauMuong1", "Vice Leader", 4580),
    ("Ekkehard", "Guild Member", 4900),
    ("EpicMarksman", "Guild Member", 4920),
    ("AnyDockers", "Guild Member", 4910),
    ("NalaStomp", "Guild Member", 4960),
    ("fred21422", "Vice Leader", 5340),
    ("estimov", "Guild Member", 5340),
    ("RonickForce", "Vice Leader", 5420),
    ("elementten", "Vice Leader", 5510),
    ("xavop", "Guild Member", 5100),
    ("Rysor", "Guild Member", 5150),
    ("BenZoo", "Elder", 5350),
    ("Flforever", "Guild Member", 4500),
    ("BigRagaTheOppStopa", "Guild Member", 5450),
    ("Rendaxx", "Guild Member", 5220),
    ("Ghoro", "Guild Member", 5600),
]
donation_members.sort(key=lambda m: m[2], reverse=True)

# Full guild roster (name, role) -- derived from the donation list, which is the
# only screenshot set that covered every member.
roster = sorted({(name, role) for name, role, _ in donation_members})

# Attack counts as (attacks, max) pairs per tracked day.
ATTACK_LOGS = {
    0: {name: ((2, 2) if name in invasion_logged_mon else (0, 0)) for name, role in roster},
}


def fmt_abbrev(n):
    if n >= 1e12:
        return f"{n / 1e12:.2f}T"
    if n >= 1e9:
        return f"{n / 1e9:.2f}B"
    if n >= 1e6:
        return f"{n / 1e6:.2f}M"
    if n >= 1e3:
        return f"{n / 1e3:.2f}K"
    return f"{n:.0f}"


def weekly_total(name):
    return sum(DAY_LOGS[d].get(name, 0) for d in TRACKED_DAYS)


invasion_members = [(name, role, weekly_total(name)) for name, role in roster]
invasion_members.sort(key=lambda m: (-m[2], m[0].lower()))
attacked_count = sum(1 for m in invasion_members if m[2] > 0)
