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
UPDATED_DATE = "Aug 25, 2026"


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

# Tue 8/25: full clean read of the Guild Member Ranking list -- all 48
# roster members accounted for exactly once (podium top-3: elementten,
# RonickForce, Flforever; ranks 4-48: the remaining 45), so no missing
# members and nothing to treat as unconfirmed this time. No Manage Member
# / donation or attack-count screenshots came in with this batch, so
# donation values are still the stale 8/18 read, carried forward again.
invasion_logged_tue = {
    "elementten": 5.80e12,
    "RonickForce": 4.38e12,
    "Flforever": 3.54e12,
    "Pimpanzee": 3.23e12,
    "Nad33m": 2.30e12,
    "HyenA": 1.64e12,
    "Drew2264": 1.18e12,
    "BenZoo": 1.17e12,
    "Ghost192": 1.02e12,
    "fred21422": 842.91e9,
    "ScHlAnGE": 490.49e9,
    "iBooneh": 476.22e9,
    "AnyDockers": 464.21e9,
    "DKDKDKDK": 414.37e9,
    "Saludan": 411.29e9,
    "Atom369": 371.36e9,
    "Altair1165": 347.16e9,
    "Stumbi97": 344.34e9,
    "choolzy": 279.13e9,
    "Ekkehard": 253.80e9,
    "NHTPhat": 224.40e9,
    "SpudNugget18": 222.08e9,
    "Tvojemama1": 221.01e9,
    "Papykique": 218.64e9,
    "tEruPmA": 202.42e9,
    "P107215255": 186.48e9,
    "Drakias": 174.93e9,
    "REAPS": 171.81e9,
    "zozoxo": 171.11e9,
    "1RauMuong1": 170.08e9,
    "Murkchoppa": 164.67e9,
    "Skytiti": 142.39e9,
    "BigRagaTheOppStopa": 140.28e9,
    "Rysor": 125.94e9,
    "Ibnt": 122.03e9,
    "IlTeino": 116.60e9,
    "NalaStomp": 112.16e9,
    "Rendaxx": 93.71e9,
    "Jackylefeu": 92.29e9,
    "Katitos": 60.25e9,
    "xavop": 49.57e9,
    "saare": 45.41e9,
    "Maskiert03": 43.56e9,
    "Vomenjack": 33.32e9,
    "estimov": 21.79e9,
    "Swidishh": 16.46e9,
    "Mightykey": 16.44e9,
    "Fredolay": 5.32e9,
}

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_DATES = ["8/24", "8/25", "8/26", "8/27", "8/28", "8/29", "8/30"]
DAY_FULL_LABELS = [f"{d} {dt}" for d, dt in zip(DAY_NAMES, DAY_DATES)]
DAY_LOGS = {0: invasion_logged_mon, 1: invasion_logged_tue}
TRACKED_DAYS = sorted(DAY_LOGS.keys())
TODAY_INDEX = 1  # Tuesday -- the most recently tracked day
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
    1: {name: ((2, 2) if name in invasion_logged_tue else (0, 0)) for name, role in roster},
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
