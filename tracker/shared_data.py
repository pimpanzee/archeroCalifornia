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
UPDATED_DATE = "Sep 14, 2026"


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
# New week: Mon 9/14 - Sun 9/20. Damage ranking (1-42 of 46) read off the
# scrollable Guild Member Ranking list; only 7 screenshots this batch, no
# Manage Member screen, so donation values are still the stale 9/8 read.
# Pimpanzee tops the day at 7.74T. The 4 members missing from the ranking
# (Papykique, Ghost192, Mightykey, Murkchoppa) are an unreached tail
# (ranks 43-46), confirmed 0-attack call-out candidates per the 9/2
# policy.
invasion_logged_mon = {
    "Pimpanzee": 7.74e12,
    "Flforever": 3.88e12,
    "EpicMarksman": 2.25e12,
    "elementten": 2.16e12,
    "HyenA": 1.69e12,
    "fred21422": 1.37e12,
    "ScHlAnGE": 1.31e12,
    "Drew2264": 1.24e12,
    "REAPS": 1.00e12,
    "RonickForce": 797.17e9,
    "P107215255": 763.20e9,
    "1RauMuong1": 703.62e9,
    "BenZoo": 697.00e9,
    "Ekkehard": 622.10e9,
    "iBooneh": 494.75e9,
    "Stumbi97": 457.12e9,
    "BigRagaTheOppStopa": 370.51e9,
    "AnyDockers": 357.09e9,
    "Nad33m": 350.28e9,
    "Tvojemama1": 309.82e9,
    "Drakias": 237.90e9,
    "Altair1165": 215.88e9,
    "Ibnt": 175.17e9,
    "NalaStomp": 167.58e9,
    "choolzy": 165.77e9,
    "saare": 130.81e9,
    "Jackylefeu": 111.19e9,
    "Rysor": 104.54e9,
    "Skytiti": 93.63e9,
    "Ghoro": 80.52e9,
    "Rendaxx": 79.79e9,
    "tEruPmA": 73.63e9,
    "Swidishh": 68.96e9,
    "zozoxo": 64.98e9,
    "Atom369": 60.86e9,
    "IlTeino": 58.20e9,
    "Saludan": 48.00e9,
    "estimov": 40.38e9,
    "Katitos": 37.73e9,
    "Maskiert03": 31.47e9,
    "Fredolay": 17.06e9,
    "xavop": 13.42e9,
    # Not visible in the ranking (Papykique, Ghost192, Mightykey,
    # Murkchoppa) -- unreached tail (ranks 43-46), confirmed 0-attack
    # call-out candidates per the 9/2 policy.
}

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_DATES = ["9/14", "9/15", "9/16", "9/17", "9/18", "9/19", "9/20"]
DAY_FULL_LABELS = [f"{d} {dt}" for d, dt in zip(DAY_NAMES, DAY_DATES)]
DAY_LOGS = {0: invasion_logged_mon}
TRACKED_DAYS = sorted(DAY_LOGS.keys())
TODAY_INDEX = 0  # Monday -- the most recently tracked day, opens wk of 9/14
WEEK_LABEL = "wk of 9/14"

# Roster unchanged. Donation values still carried forward from the 9/8
# read -- no Manage Member screenshot has come in since.
donation_members = [
    ("choolzy", "Guild Member", 1390),
    ("Ekkehard", "Guild Member", 1170),
    ("NalaStomp", "Guild Member", 620),
    ("Fredolay", "Guild Member", 190),
    ("ScHlAnGE", "Guild Member", 670),
    ("Rysor", "Guild Member", 1280),
    ("REAPS", "Guild Member", 870),
    ("Jackylefeu", "Guild Member", 310),
    ("EpicMarksman", "Guild Member", 1010),
    ("AnyDockers", "Guild Member", 1360),
    ("Maskiert03", "Guild Member", 1080),
    ("Atom369", "Guild Member", 200),
    ("Stumbi97", "Guild Member", 1340),
    ("Katitos", "Guild Member", 1320),
    ("Rendaxx", "Guild Member", 1540),
    ("Ibnt", "Guild Member", 840),
    ("zozoxo", "Guild Member", 1120),
    ("Papykique", "Guild Member", 1560),
    ("Tvojemama1", "Guild Member", 550),
    ("xavop", "Guild Member", 1460),
    ("P107215255", "Guild Member", 1560),
    ("Skytiti", "Guild Member", 830),
    ("Ghost192", "Guild Member", 1320),
    ("Altair1165", "Guild Member", 1020),
    ("Saludan", "Guild Member", 340),
    ("BigRagaTheOppStopa", "Guild Member", 1200),
    ("tEruPmA", "Guild Member", 1090),
    ("Nad33m", "Guild Member", 1000),
    ("iBooneh", "Elder", 880),
    ("BenZoo", "Elder", 1300),
    ("estimov", "Guild Member", 1600),
    ("IlTeino", "Guild Member", 1420),
    ("Swidishh", "Guild Member", 1360),
    ("Mightykey", "Guild Member", 180),
    ("Ghoro", "Guild Member", 820),
    ("1RauMuong1", "Vice Leader", 1430),
    ("fred21422", "Vice Leader", 1600),
    ("Drew2264", "Vice Leader", 1520),
    ("Drakias", "Elder", 1450),
    ("HyenA", "Elder", 1600),
    ("Murkchoppa", "Elder", 270),
    ("saare", "Elder", 1440),
    ("Pimpanzee", "Leader", 1600),
    ("Flforever", "Guild Member", 1450),
    ("elementten", "Vice Leader", 1500),
    ("RonickForce", "Vice Leader", 1600),
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
