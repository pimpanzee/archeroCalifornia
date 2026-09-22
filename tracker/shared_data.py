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
UPDATED_DATE = "Sep 21, 2026"


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
# New week: Mon 9/21 - Sun 9/27. Damage ranking (1-39 of 47) read off the
# scrollable Guild Member Ranking list; only 7 screenshots this batch (one
# duplicate), no Manage Member screen, so donation values are carried
# forward unchanged from 9/20. The 8 members missing from the ranking
# (Ekkehard, zozoxo, Papykique, Skytiti, Ghost192, Fredolay,
# Depfefferle336, Murkchoppa) are confirmed 0-attack call-out candidates
# per the 9/2 policy.
invasion_logged_mon = {
    "elementten": 8.09e12,
    "HyenA": 7.04e12,
    "Pimpanzee": 6.47e12,
    "Flforever": 5.97e12,
    "Drew2264": 4.09e12,
    "fred21422": 3.49e12,
    "Nad33m": 3.14e12,
    "EpicMarksman": 2.63e12,
    "P107215255": 2.31e12,
    "RonickForce": 2.10e12,
    "BenZoo": 1.94e12,
    "iBooneh": 1.07e12,
    "Altair1165": 1.05e12,
    "REAPS": 985.86e9,
    "NalaStomp": 880.64e9,
    "Drakias": 857.13e9,
    "Saludan": 845.03e9,
    "BigRagaTheOppStopa": 834.20e9,
    "Ibnt": 799.56e9,
    "Atom369": 315.50e9,
    "AnyDockers": 265.92e9,
    "Jackylefeu": 220.90e9,
    "Stumbi97": 211.46e9,
    "lllmundlll": 199.52e9,
    "Swidishh": 165.29e9,
    "ScHlAnGE": 161.55e9,
    "tEruPmA": 145.06e9,
    "Tvojemama1": 130.62e9,
    "choolzy": 119.84e9,
    "Maskiert03": 100.12e9,
    "estimov": 99.44e9,
    "Ghoro": 90.82e9,
    "IlTeino": 75.82e9,
    "1RauMuong1": 67.08e9,
    "Rysor": 45.95e9,
    "saare": 38.96e9,
    "Rendaxx": 29.42e9,
    "xavop": 13.52e9,
    "Mightykey": 12.52e9,
    # Not visible in the ranking (Ekkehard, zozoxo, Papykique, Skytiti,
    # Ghost192, Fredolay, Depfefferle336, Murkchoppa) -- unreached tail
    # (ranks 40-47), confirmed 0-attack call-out candidates per the 9/2
    # policy.
}

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_DATES = ["9/21", "9/22", "9/23", "9/24", "9/25", "9/26", "9/27"]
DAY_FULL_LABELS = [f"{d} {dt}" for d, dt in zip(DAY_NAMES, DAY_DATES)]
DAY_LOGS = {0: invasion_logged_mon}
TRACKED_DAYS = sorted(DAY_LOGS.keys())
TODAY_INDEX = 0  # Monday -- the most recently tracked day, opens wk of 9/21
WEEK_LABEL = "wk of 9/21"

# Roster unchanged. Donation values still carried forward from the 9/20
# read -- no Manage Member screenshot came in with this batch.
donation_members = [
    ("lllmundlll", "Guild Member", 590),
    ("Depfefferle336", "Guild Member", 2700),
    ("choolzy", "Guild Member", 5060),
    ("Ekkehard", "Guild Member", 4590),
    ("NalaStomp", "Guild Member", 5490),
    ("Fredolay", "Guild Member", 2390),
    ("ScHlAnGE", "Guild Member", 2510),
    ("Rysor", "Guild Member", 4920),
    ("REAPS", "Guild Member", 4840),
    ("Jackylefeu", "Guild Member", 1330),
    ("EpicMarksman", "Guild Member", 5390),
    ("AnyDockers", "Guild Member", 4810),
    ("Maskiert03", "Guild Member", 4860),
    ("Atom369", "Guild Member", 1070),
    ("Stumbi97", "Guild Member", 5000),
    ("Rendaxx", "Guild Member", 5080),
    ("Ibnt", "Guild Member", 3090),
    ("zozoxo", "Guild Member", 4430),
    ("Papykique", "Guild Member", 4350),
    ("Tvojemama1", "Guild Member", 2220),
    ("xavop", "Guild Member", 5000),
    ("P107215255", "Guild Member", 4330),
    ("Skytiti", "Guild Member", 2420),
    ("Ghost192", "Guild Member", 3310),
    ("Altair1165", "Guild Member", 3140),
    ("Saludan", "Guild Member", 2410),
    ("BigRagaTheOppStopa", "Guild Member", 5130),
    ("tEruPmA", "Guild Member", 3960),
    ("Nad33m", "Guild Member", 3090),
    ("iBooneh", "Elder", 3000),
    ("BenZoo", "Elder", 5310),
    ("estimov", "Guild Member", 5300),
    ("IlTeino", "Guild Member", 4910),
    ("Swidishh", "Guild Member", 4810),
    ("Mightykey", "Guild Member", 1180),
    ("Ghoro", "Guild Member", 5390),
    ("1RauMuong1", "Vice Leader", 4020),
    ("fred21422", "Vice Leader", 5370),
    ("Drew2264", "Vice Leader", 5240),
    ("Drakias", "Elder", 4900),
    ("HyenA", "Elder", 5100),
    ("Murkchoppa", "Elder", 0),
    ("saare", "Elder", 4960),
    ("Pimpanzee", "Leader", 5600),
    ("Flforever", "Guild Member", 5000),
    ("elementten", "Vice Leader", 5600),
    ("RonickForce", "Vice Leader", 5450),
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
