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
UPDATED_DATE = "Aug 31, 2026"


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
# New week: Mon 8/31 - Sun 9/6. This batch had 7 Guild Member Ranking
# screenshots but no Manage Member/donation or attack-count screens, so
# donation values below are carried forward unchanged from 8/30 (see note
# above donation_members) and attack counts are backfilled the same way as
# past no-attack-screen days: presence in the ranking = confirmed 2/2,
# absence = unconfirmed 0/0. Damage ranking (1-42 of 48) read off the
# scrollable list; the 6 members missing (AnyDockers, Vomenjack, DKDKDKDK,
# Murkchoppa, Papykique, Mightykey) are NOT treated as 0-attack call-out
# candidates since there's no attack screen to confirm it either way.
invasion_logged_mon = {
    "Pimpanzee": 6.59e12,
    "elementten": 5.25e12,
    "HyenA": 4.52e12,
    "Drew2264": 3.28e12,
    "BenZoo": 2.35e12,
    "RonickForce": 2.00e12,
    "Flforever": 1.73e12,
    "Tvojemama1": 879.51e9,
    "Nad33m": 693.53e9,
    "Altair1165": 539.49e9,
    "1RauMuong1": 506.73e9,
    "fred21422": 485.55e9,
    "NHTPhat": 473.39e9,
    "P107215255": 437.18e9,
    "Ekkehard": 415.45e9,
    "Saludan": 291.47e9,
    "Rysor": 280.08e9,
    "Drakias": 277.54e9,
    "IlTeino": 263.91e9,
    "iBooneh": 244.65e9,
    "SpudNugget18": 226.67e9,
    "Stumbi97": 209.92e9,
    "REAPS": 157.86e9,
    "Jackylefeu": 143.56e9,
    "Ibnt": 136.75e9,
    "Ghost192": 132.04e9,
    "NalaStomp": 130.53e9,
    "Rendaxx": 121.36e9,
    "ScHlAnGE": 106.10e9,
    "Skytiti": 98.12e9,
    "Atom369": 97.98e9,
    "tEruPmA": 73.13e9,
    "zozoxo": 71.34e9,
    "saare": 56.87e9,
    "BigRagaTheOppStopa": 49.68e9,
    "Swidishh": 38.06e9,
    "choolzy": 27.03e9,
    "estimov": 26.37e9,
    "Maskiert03": 22.57e9,
    "Fredolay": 13.77e9,
    "Katitos": 6.46e9,
    "xavop": 5.83e9,
    # Not visible in the scrolled ranking (AnyDockers, Vomenjack, DKDKDKDK,
    # Murkchoppa, Papykique, Mightykey) -- no attack-count screen today to
    # confirm either way, so these are NOT treated as 0-attack call-out
    # candidates.
}

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_DATES = ["8/31", "9/1", "9/2", "9/3", "9/4", "9/5", "9/6"]
DAY_FULL_LABELS = [f"{d} {dt}" for d, dt in zip(DAY_NAMES, DAY_DATES)]
DAY_LOGS = {0: invasion_logged_mon}
TRACKED_DAYS = sorted(DAY_LOGS.keys())
TODAY_INDEX = 0  # Monday -- the most recently tracked day, opens wk of 8/31
WEEK_LABEL = "wk of 8/31"

# Roster unchanged. Donation values carried forward unchanged from the 8/30
# read -- no Manage Member screenshot came in with this batch.
donation_members = [
    ("Rysor", "Guild Member", 4360),
    ("Swidishh", "Guild Member", 4780),
    ("Skytiti", "Guild Member", 3380),
    ("Maskiert03", "Guild Member", 4460),
    ("Saludan", "Guild Member", 2110),
    ("xavop", "Guild Member", 3670),
    ("Flforever", "Guild Member", 4970),
    ("REAPS", "Guild Member", 4560),
    ("zozoxo", "Guild Member", 3730),
    ("choolzy", "Guild Member", 4620),
    ("P107215255", "Guild Member", 4820),
    ("IlTeino", "Guild Member", 5130),
    ("AnyDockers", "Guild Member", 5190),
    ("Atom369", "Guild Member", 1740),
    ("Katitos", "Guild Member", 4180),
    ("Mightykey", "Guild Member", 3190),
    ("BigRagaTheOppStopa", "Guild Member", 4510),
    ("Fredolay", "Guild Member", 1920),
    ("Altair1165", "Guild Member", 3570),
    ("Nad33m", "Guild Member", 3300),
    ("Tvojemama1", "Guild Member", 2980),
    ("tEruPmA", "Guild Member", 4660),
    ("Stumbi97", "Guild Member", 4540),
    ("NalaStomp", "Guild Member", 5010),
    ("Rendaxx", "Guild Member", 5300),
    ("ScHlAnGE", "Guild Member", 2190),
    ("Ghost192", "Guild Member", 3810),
    ("estimov", "Guild Member", 5400),
    ("Vomenjack", "Guild Member", 2430),
    ("NHTPhat", "Guild Member", 3430),
    ("SpudNugget18", "Guild Member", 3420),
    ("Ibnt", "Guild Member", 3970),
    ("fred21422", "Guild Member", 5450),
    ("Ekkehard", "Guild Member", 4230),
    ("Drakias", "Guild Member", 4900),
    ("BenZoo", "Elder", 4550),
    ("HyenA", "Elder", 5110),
    ("saare", "Elder", 5290),
    ("Murkchoppa", "Elder", 300),
    ("iBooneh", "Elder", 2760),
    ("Jackylefeu", "Guild Member", 4730),
    ("Pimpanzee", "Leader", 5600),
    ("Drew2264", "Vice Leader", 5130),
    ("RonickForce", "Vice Leader", 5600),
    ("1RauMuong1", "Vice Leader", 4450),
    ("elementten", "Vice Leader", 5000),
    ("DKDKDKDK", "Elder", 2570),
    ("Papykique", "Guild Member", 5160),
]
donation_members.sort(key=lambda m: m[2], reverse=True)

# Full guild roster (name, role) -- derived from the donation list, which is the
# only screenshot set that covered every member.
roster = sorted({(name, role) for name, role, _ in donation_members})

# Attack counts as (attacks, max) pairs per tracked day. No attack-count
# screen this week yet, so backfilled the same way as recent no-screenshot
# days: presence in the ranking treated as a confirmed 2/2, absence as an
# unconfirmed 0/0 (not penalized).
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
