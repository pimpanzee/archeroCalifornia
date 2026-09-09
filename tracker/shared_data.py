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
UPDATED_DATE = "Sep 8, 2026"


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
# New week: Mon 9/7 - Sun 9/13. Monday 9/7 has no data -- the iPhone
# Shortcut stopped uploading after 9/3 and stayed broken through 9/4-9/7,
# so this Tuesday 9/8 batch is the first data of the new week. Roster
# change: guild is now 46/48 (was 48/48). DKDKDKDK and Vomenjack are gone
# (left the guild); two new members joined, Ghoro and EpicMarksman.
# Full clean read this time: damage ranking (1-39 of 46) plus real Manage
# Member/donation screens covering all 46 current members. The 7 members
# missing from the ranking (Ekkehard, Fredolay, REAPS, zozoxo, Tvojemama1,
# Skytiti, Ghost192) exactly match the 7 confirmed 0-attack members on the
# Manage Member screens -- full 7-for-7 cross-validation.
invasion_logged_tue = {
    "HyenA": 7.54e12,
    "Flforever": 4.60e12,
    "Pimpanzee": 4.13e12,
    "EpicMarksman": 2.28e12,
    "Drew2264": 2.12e12,
    "fred21422": 2.03e12,
    "ScHlAnGE": 1.91e12,
    "elementten": 1.73e12,
    "RonickForce": 1.08e12,
    "BenZoo": 715.14e9,
    "iBooneh": 475.65e9,
    "Papykique": 455.99e9,
    "AnyDockers": 445.52e9,
    "IlTeino": 415.64e9,
    "Murkchoppa": 367.39e9,
    "1RauMuong1": 253.30e9,
    "saare": 212.91e9,
    "Saludan": 203.11e9,
    "NalaStomp": 184.47e9,
    "Drakias": 171.49e9,
    "tEruPmA": 171.00e9,
    "Stumbi97": 152.39e9,
    "Jackylefeu": 147.12e9,
    "Ibnt": 128.96e9,
    "Rendaxx": 116.35e9,
    "P107215255": 116.35e9,
    "Atom369": 96.47e9,
    "Altair1165": 93.75e9,
    "choolzy": 67.99e9,
    "Ghoro": 59.04e9,
    "estimov": 53.54e9,
    "Katitos": 51.70e9,
    "BigRagaTheOppStopa": 47.90e9,
    "Maskiert03": 34.90e9,
    "Rysor": 34.23e9,
    "Nad33m": 29.57e9,
    "Mightykey": 22.41e9,
    "xavop": 21.56e9,
    "Swidishh": 14.58e9,
    # Not visible in the ranking (Ekkehard, Fredolay, REAPS, zozoxo,
    # Tvojemama1, Skytiti, Ghost192) -- confirmed 0 attacks for the day,
    # exact match with the Manage Member screens (see ATTACKS_TUE).
}

# Attack count (out of a max of 2/day) for Tuesday 9/8, read off the red
# skull icon on the Manage Member / donation screens -- real data for all
# 46 current members.
ATTACKS_TUE = {
    "choolzy": 2, "Ekkehard": 0, "NalaStomp": 2, "Fredolay": 0,
    "ScHlAnGE": 2, "Rysor": 2, "REAPS": 0, "Jackylefeu": 2,
    "EpicMarksman": 2, "AnyDockers": 2, "Maskiert03": 2, "Atom369": 2,
    "Stumbi97": 2, "Katitos": 2, "Rendaxx": 2, "Ibnt": 2, "zozoxo": 0,
    "Papykique": 2, "Tvojemama1": 0, "xavop": 1, "P107215255": 2,
    "Skytiti": 0, "Ghost192": 0, "Altair1165": 2, "Saludan": 2,
    "BigRagaTheOppStopa": 2, "tEruPmA": 2, "Nad33m": 2, "iBooneh": 2,
    "BenZoo": 2, "estimov": 2, "IlTeino": 2, "Swidishh": 2, "Mightykey": 2,
    "Ghoro": 2, "1RauMuong1": 2, "fred21422": 2, "Drew2264": 2,
    "Drakias": 2, "HyenA": 2, "Murkchoppa": 2, "saare": 2, "Pimpanzee": 2,
    "Flforever": 2, "elementten": 2, "RonickForce": 2,
}

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_DATES = ["9/7", "9/8", "9/9", "9/10", "9/11", "9/12", "9/13"]
DAY_FULL_LABELS = [f"{d} {dt}" for d, dt in zip(DAY_NAMES, DAY_DATES)]
DAY_LOGS = {1: invasion_logged_tue}
TRACKED_DAYS = sorted(DAY_LOGS.keys())
TODAY_INDEX = 1  # Tuesday -- the most recently tracked day (Monday 9/7 has no data)
WEEK_LABEL = "wk of 9/7"

# Roster update as of 9/8: DKDKDKDK and Vomenjack are gone (left the
# guild); Ghoro and EpicMarksman are new (both "Guild Member"). Donation
# values refreshed from the 9/8 Manage Member screens for all 46 members.
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
    1: {name: (ATTACKS_TUE.get(name, 0), 2) for name, role in roster},
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
