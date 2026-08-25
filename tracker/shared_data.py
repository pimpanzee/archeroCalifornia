import base64
from pathlib import Path

FONTS = "/mnt/skills/examples/canvas-design/canvas-fonts"

# Known published URLs -- update DONATIONS_URL after the donations page's first publish.
INVASION_URL = "https://claude.ai/code/artifact/2d3a73a8-5995-4097-8446-2ff20c533627"
DONATIONS_URL = "https://claude.ai/code/artifact/e6f3430a-77ad-41f9-a37a-cde5487c8593"

GUILD_ID = "90754"
UPDATED_DATE = "Aug 24, 2026"


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
# New week: Mon 8/24 - Sun 8/30. Confirmed by the growth trend across
# previous Mondays' #1 damage (2.90T wk1 -> 3.98T wk2 -> 5.56T wk3), not by
# a donation reset (no Manage Member / donation screenshots came in this
# batch, so donation values below are still the stale 8/18 read, carried
# forward yet again pending a fresh donation screenshot -- they almost
# certainly don't reflect this week's actual (probably reset) counts).
# Damage ranking (1-46 of an unknown-but-larger roster) read off the
# scrollable Guild Member Ranking list. One new member spotted: Papykique
# (rank 10, 716.18B) -- added to the roster below, role/donation unknown.
# Atom369 and Murkchoppa are missing from this ranking; with no attack
# screen to check, treated as unconfirmed (0, 0) rather than assumed absent
# from the guild or assumed 0-attack.
invasion_logged_mon = {
    "Pimpanzee": 5.56e12,
    "HyenA": 5.25e12,
    "RonickForce": 4.63e12,
    "elementten": 4.03e12,
    "Flforever": 2.61e12,
    "fred21422": 2.00e12,
    "DKDKDKDK": 902.66e9,
    "Saludan": 874.38e9,
    "REAPS": 756.83e9,
    "Papykique": 716.18e9,
    "Altair1165": 624.33e9,
    "P107215255": 529.60e9,
    "BenZoo": 508.84e9,
    "Drew2264": 495.62e9,
    "NHTPhat": 460.24e9,
    "iBooneh": 386.56e9,
    "Stumbi97": 320.49e9,
    "Ghost192": 284.95e9,
    "Tvojemama1": 247.84e9,
    "Nad33m": 216.27e9,
    "tEruPmA": 213.86e9,
    "Skytiti": 213.12e9,
    "SpudNugget18": 210.67e9,
    "Ekkehard": 195.37e9,
    "Drakias": 164.40e9,
    "Rendaxx": 124.55e9,
    "choolzy": 116.48e9,
    "ScHlAnGE": 81.78e9,
    "1RauMuong1": 74.73e9,
    "Rysor": 70.36e9,
    "Swidishh": 64.88e9,
    "Ibnt": 63.71e9,
    "AnyDockers": 54.51e9,
    "estimov": 48.89e9,
    "Fredolay": 37.46e9,
    "Vomenjack": 34.25e9,
    "NalaStomp": 34.18e9,
    "Jackylefeu": 31.19e9,
    "BigRagaTheOppStopa": 28.60e9,
    "IlTeino": 26.36e9,
    "zozoxo": 21.53e9,
    "Katitos": 20.44e9,
    "Maskiert03": 17.87e9,
    "saare": 13.68e9,
    "Mightykey": 8.95e9,
    "xavop": 5.63e9,
    # Not visible in the scrolled ranking (Atom369, Murkchoppa) -- no
    # attack-count screen today to confirm either way, so these are NOT
    # treated as 0-attack call-out candidates.
}

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_DATES = ["8/24", "8/25", "8/26", "8/27", "8/28", "8/29", "8/30"]
DAY_FULL_LABELS = [f"{d} {dt}" for d, dt in zip(DAY_NAMES, DAY_DATES)]
DAY_LOGS = {0: invasion_logged_mon}
TRACKED_DAYS = sorted(DAY_LOGS.keys())
TODAY_INDEX = 0  # Monday -- the most recently tracked day
WEEK_LABEL = "wk of 8/24"

# Roster carries over from last week (Papykique added as a new member seen
# in this batch's ranking; role/donation unknown so defaulted). Donation
# values are the stale 8/18 read carried forward again -- no fresh donation
# screenshot has come in since (see note above invasion_logged_mon).
donation_members = [
    ("Rysor", "Guild Member", 1600),
    ("Swidishh", "Guild Member", 1600),
    ("Skytiti", "Guild Member", 960),
    ("Maskiert03", "Guild Member", 670),
    ("Saludan", "Guild Member", 1180),
    ("xavop", "Guild Member", 1020),
    ("Flforever", "Guild Member", 1560),
    ("REAPS", "Guild Member", 1420),
    ("zozoxo", "Guild Member", 1480),
    ("choolzy", "Guild Member", 1600),
    ("P107215255", "Guild Member", 1420),
    ("IlTeino", "Guild Member", 1340),
    ("AnyDockers", "Guild Member", 1600),
    ("Atom369", "Guild Member", 120),
    ("Katitos", "Guild Member", 1520),
    ("Mightykey", "Guild Member", 1280),
    ("BigRagaTheOppStopa", "Guild Member", 1600),
    ("Fredolay", "Guild Member", 670),
    ("Altair1165", "Guild Member", 1090),
    ("Nad33m", "Guild Member", 1000),
    ("Tvojemama1", "Guild Member", 1200),
    ("tEruPmA", "Guild Member", 1370),
    ("Stumbi97", "Guild Member", 1480),
    ("NalaStomp", "Guild Member", 1360),
    ("Rendaxx", "Guild Member", 1600),
    ("ScHlAnGE", "Guild Member", 960),
    ("Ghost192", "Guild Member", 1120),
    ("estimov", "Guild Member", 1600),
    ("Vomenjack", "Guild Member", 600),
    ("NHTPhat", "Guild Member", 1000),
    ("SpudNugget18", "Guild Member", 1000),
    ("Ibnt", "Guild Member", 1080),
    ("fred21422", "Guild Member", 1600),
    ("Ekkehard", "Guild Member", 1600),
    ("Drakias", "Guild Member", 1400),
    ("BenZoo", "Elder", 1600),
    ("HyenA", "Elder", 1600),
    ("saare", "Elder", 1520),
    ("Murkchoppa", "Elder", 0),
    ("iBooneh", "Elder", 1130),
    ("Jackylefeu", "Guild Member", 740),
    ("Pimpanzee", "Leader", 1600),
    ("Drew2264", "Vice Leader", 1520),
    ("RonickForce", "Vice Leader", 1600),
    ("1RauMuong1", "Vice Leader", 1100),
    ("elementten", "Vice Leader", 1600),
    ("DKDKDKDK", "Elder", 800),
    ("Papykique", "Guild Member", 0),
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
