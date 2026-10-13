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
UPDATED_DATE = "Oct 12, 2026"


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
# New week: Mon 10/12 - Sun 10/18. Damage ranking (1-40 of 48) read off the
# scrollable Guild Member Ranking list; 8 screenshots this batch, no
# Manage Member screen, so donation values are carried forward unchanged
# from the 10/4 full refresh. No roster changes. Pimpanzee's 16.97T is a
# new season-high single-day #1 (previous high was Pimpanzee's own 13.69T
# on 9/24). The 8 members missing from the ranking (choolzy, AnyDockers,
# Papykique, Tvojemama1, P107215255, Mightykey, Murkchoppa, CzosneK) --
# ranking list ended cleanly at rank 40 (Fredolay) right above the pinned
# own-rank footer, so this is the true end of the list, not a mid-scroll
# gap. Confirmed 0-attack call-out candidates per the 9/2 policy.
invasion_logged_mon = {
    "Pimpanzee": 16.97e12,
    "EpicMarksman": 9.38e12,
    "HyenA": 7.06e12,
    "Flforever": 4.98e12,
    "fred21422": 4.97e12,
    "Drew2264": 3.82e12,
    "iBooneh": 3.52e12,
    "elementten": 3.06e12,
    "RonickForce": 2.71e12,
    "NalaStomp": 1.77e12,
    "Ghost192": 1.55e12,
    "Ibnt": 1.23e12,
    "BigRagaTheOppStopa": 1.01e12,
    "Atom369": 997.24e9,
    "Saludan": 922.21e9,
    "REAPS": 881.18e9,
    "BenZoo": 804.00e9,
    "Drakias": 652.72e9,
    "Jackylefeu": 481.94e9,
    "Ekkehard": 432.35e9,
    "1RauMuong1": 357.46e9,
    "Altair1165": 275.83e9,
    "saare": 258.36e9,
    "Rysor": 256.82e9,
    "Maskiert03": 226.56e9,
    "Ghoro": 199.97e9,
    "Stumbi97": 197.19e9,
    "estimov": 188.09e9,
    "Rendaxx": 153.84e9,
    "Skytiti": 151.68e9,
    "IlTeino": 150.00e9,
    "Nad33m": 112.90e9,
    "ScHlAnGE": 108.63e9,
    "tEruPmA": 107.82e9,
    "zozoxo": 80.07e9,
    "xavop": 46.08e9,
    "Swidishh": 36.05e9,
    "lllmundlll": 35.86e9,
    "Depfefferle336": 7.20e9,
    "Fredolay": 6.93e9,
    # Not visible in the ranking (choolzy, AnyDockers, Papykique,
    # Tvojemama1, P107215255, Mightykey, Murkchoppa, CzosneK) -- unreached
    # tail / true end of list, confirmed 0-attack call-out candidates per
    # the 9/2 policy.
}

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_DATES = ["10/12", "10/13", "10/14", "10/15", "10/16", "10/17", "10/18"]
DAY_FULL_LABELS = [f"{d} {dt}" for d, dt in zip(DAY_NAMES, DAY_DATES)]
DAY_LOGS = {0: invasion_logged_mon}
TRACKED_DAYS = sorted(DAY_LOGS.keys())
TODAY_INDEX = 0  # Monday -- the most recently tracked day
WEEK_LABEL = "wk of 10/12"

# Roster unchanged. Donation values still carried forward from the 10/4
# full refresh -- no Manage Member screenshot came in with this batch
# (now over a week stale).
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
