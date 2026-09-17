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
UPDATED_DATE = "Sep 16, 2026"


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

# Tuesday 9/15 -- damage ranking (1-40 of 46) read off the scrollable
# Guild Member Ranking list, tail (ranks 41-46) unreached (only 7
# screenshots this batch, no Manage Member screen). Donation values still
# carried forward from 9/8. The 6 members missing from the ranking
# (Jackylefeu, AnyDockers, Atom369, Papykique, Ghost192, Murkchoppa) are
# confirmed 0-attack call-out candidates per the 9/2 policy.
invasion_logged_tue = {
    "Pimpanzee": 5.57e12,
    "elementten": 4.26e12,
    "Flforever": 4.09e12,
    "fred21422": 4.02e12,
    "HyenA": 2.47e12,
    "Drew2264": 1.93e12,
    "RonickForce": 1.55e12,
    "Tvojemama1": 1.23e12,
    "BenZoo": 994.39e9,
    "Altair1165": 962.29e9,
    "EpicMarksman": 774.16e9,
    "ScHlAnGE": 764.78e9,
    "Nad33m": 712.64e9,
    "iBooneh": 638.48e9,
    "P107215255": 591.75e9,
    "Skytiti": 435.88e9,
    "Drakias": 389.41e9,
    "Saludan": 345.83e9,
    "Ekkehard": 283.99e9,
    "Stumbi97": 268.59e9,
    "tEruPmA": 256.68e9,
    "Rysor": 238.01e9,
    "IlTeino": 212.35e9,
    "Ibnt": 181.58e9,
    "BigRagaTheOppStopa": 163.04e9,
    "REAPS": 158.09e9,
    "NalaStomp": 114.73e9,
    "Rendaxx": 113.74e9,
    "estimov": 102.27e9,
    "choolzy": 99.31e9,
    "Ghoro": 72.05e9,
    "1RauMuong1": 59.83e9,
    "Swidishh": 50.96e9,
    "xavop": 34.42e9,
    "saare": 31.17e9,
    "zozoxo": 28.78e9,
    "Maskiert03": 26.58e9,
    "Fredolay": 15.19e9,
    "Mightykey": 13.02e9,
    "Katitos": 12.08e9,
    # Not visible in the ranking (Jackylefeu, AnyDockers, Atom369,
    # Papykique, Ghost192, Murkchoppa) -- unreached tail (ranks 41-46),
    # confirmed 0-attack call-out candidates per the 9/2 policy.
}

# Wednesday 9/16 -- damage ranking (1-38 of 47) read off the scrollable
# Guild Member Ranking list, tail unreached (only 6 screenshots this
# batch, no Manage Member screen). New member spotted: Depfefferle336
# (rank 38, 1.63B) -- added to the roster below with donation unknown
# (defaulted to 0) pending a Manage Member screenshot. No one else left,
# so the guild is now 47/48. elementten tops the day at a new season-high
# 9.63T (previous high was HyenA's 9.45T on 9/10). The 9 members missing
# from the ranking (Katitos, Papykique, Tvojemama1, xavop, Ghost192,
# IlTeino, Mightykey, 1RauMuong1, Murkchoppa) are confirmed 0-attack
# call-out candidates per the 9/2 policy.
invasion_logged_wed = {
    "elementten": 9.63e12,
    "Flforever": 6.81e12,
    "HyenA": 6.50e12,
    "Pimpanzee": 4.99e12,
    "fred21422": 3.77e12,
    "Drew2264": 2.52e12,
    "REAPS": 2.09e12,
    "EpicMarksman": 1.46e12,
    "P107215255": 1.02e12,
    "ScHlAnGE": 942.97e9,
    "iBooneh": 771.03e9,
    "BenZoo": 680.89e9,
    "Nad33m": 554.84e9,
    "RonickForce": 401.90e9,
    "Ekkehard": 383.28e9,
    "Drakias": 334.05e9,
    "Stumbi97": 312.35e9,
    "Jackylefeu": 307.05e9,
    "BigRagaTheOppStopa": 221.31e9,
    "saare": 195.61e9,
    "Altair1165": 156.24e9,
    "Rendaxx": 135.46e9,
    "Skytiti": 134.85e9,
    "Saludan": 118.54e9,
    "Rysor": 110.16e9,
    "Ibnt": 107.34e9,
    "AnyDockers": 78.93e9,
    "tEruPmA": 66.66e9,
    "choolzy": 61.01e9,
    "NalaStomp": 52.00e9,
    "Atom369": 44.35e9,
    "Maskiert03": 35.91e9,
    "Ghoro": 13.94e9,
    "estimov": 6.72e9,
    "Swidishh": 6.02e9,
    "zozoxo": 4.73e9,
    "Fredolay": 3.98e9,
    "Depfefferle336": 1.63e9,
    # Not visible in the ranking (Katitos, Papykique, Tvojemama1, xavop,
    # Ghost192, IlTeino, Mightykey, 1RauMuong1, Murkchoppa) -- unreached
    # tail, confirmed 0-attack call-out candidates per the 9/2 policy.
}

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_DATES = ["9/14", "9/15", "9/16", "9/17", "9/18", "9/19", "9/20"]
DAY_FULL_LABELS = [f"{d} {dt}" for d, dt in zip(DAY_NAMES, DAY_DATES)]
DAY_LOGS = {0: invasion_logged_mon, 1: invasion_logged_tue, 2: invasion_logged_wed}
TRACKED_DAYS = sorted(DAY_LOGS.keys())
TODAY_INDEX = 2  # Wednesday -- the most recently tracked day
WEEK_LABEL = "wk of 9/14"

# Roster update as of 9/16: Depfefferle336 is new (Guild Member, donation
# unknown pending a Manage Member screenshot). Everyone else's donation
# values still carried forward from the 9/8 read.
donation_members = [
    ("Depfefferle336", "Guild Member", 0),
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
    1: {name: ((2, 2) if name in invasion_logged_tue else (0, 0)) for name, role in roster},
    2: {name: ((2, 2) if name in invasion_logged_wed else (0, 0)) for name, role in roster},
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
