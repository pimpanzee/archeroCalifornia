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
UPDATED_DATE = "Sep 4, 2026"


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

# Tuesday 9/1 -- damage ranking (1-45 of 48) read off the scrollable Guild
# Member Ranking list; the unreached tail (ranks 46-48: DKDKDKDK, Vomenjack,
# Fredolay) was never scrolled to. No Manage Member/attack-count screens in
# this batch either, so those 3 are treated as unconfirmed (0, 0), not
# 0-attack. Donation values still carried forward from 8/30.
invasion_logged_tue = {
    "Pimpanzee": 6.87e12,
    "HyenA": 4.68e12,
    "Drew2264": 1.73e12,
    "BenZoo": 1.60e12,
    "REAPS": 941.92e9,
    "RonickForce": 925.25e9,
    "Tvojemama1": 821.35e9,
    "iBooneh": 728.37e9,
    "elementten": 713.90e9,
    "Papykique": 620.73e9,
    "Saludan": 598.48e9,
    "Flforever": 583.79e9,
    "fred21422": 574.68e9,
    "ScHlAnGE": 541.08e9,
    "IlTeino": 519.65e9,
    "P107215255": 461.43e9,
    "AnyDockers": 445.07e9,
    "NHTPhat": 432.00e9,
    "Ekkehard": 358.83e9,
    "NalaStomp": 297.50e9,
    "Drakias": 293.38e9,
    "Altair1165": 277.30e9,
    "Ghost192": 275.73e9,
    "SpudNugget18": 246.35e9,
    "BigRagaTheOppStopa": 244.81e9,
    "Skytiti": 233.03e9,
    "saare": 189.92e9,
    "zozoxo": 173.59e9,
    "tEruPmA": 170.78e9,
    "Jackylefeu": 142.31e9,
    "choolzy": 126.03e9,
    "Murkchoppa": 122.86e9,
    "Rysor": 121.34e9,
    "Ibnt": 116.74e9,
    "Katitos": 114.33e9,
    "Stumbi97": 104.36e9,
    "Atom369": 98.94e9,
    "Rendaxx": 84.31e9,
    "1RauMuong1": 75.46e9,
    "Maskiert03": 65.68e9,
    "Nad33m": 42.93e9,
    "estimov": 36.08e9,
    "Swidishh": 35.87e9,
    "xavop": 17.40e9,
    "Mightykey": 15.49e9,
    # Not visible in the scrolled ranking (DKDKDKDK, Vomenjack, Fredolay) --
    # unreached tail, no attack-count screen to confirm either way, so these
    # are NOT treated as 0-attack call-out candidates.
}

# Wednesday 9/2 -- damage ranking (ranks 1-39 of 48, minus a 1-rank gap at
# 27) read off the scrollable Guild Member Ranking list. HyenA's 8.38T is
# the highest single-day #1 recorded all season (previous high was
# Pimpanzee's 6.87T on 9/1). Per standing guidance as of 9/2: the ranking
# screenshots themselves are enough to call out non-attackers -- a separate
# Manage Member/donation screen is no longer required to confirm 0 attacks.
# The 10 members missing from this ranking (choolzy, Atom369, Mightykey,
# Fredolay, Nad33m, Tvojemama1, Ghost192, Vomenjack, Murkchoppa, DKDKDKDK)
# are treated as confirmed 0-attack call-out candidates.
invasion_logged_wed = {
    "HyenA": 8.38e12,
    "Flforever": 6.22e12,
    "Pimpanzee": 5.27e12,
    "Drew2264": 3.62e12,
    "elementten": 3.58e12,
    "fred21422": 2.91e12,
    "RonickForce": 1.73e12,
    "BenZoo": 1.44e12,
    "NHTPhat": 1.19e12,
    "REAPS": 762.96e9,
    "Ekkehard": 654.42e9,
    "Papykique": 611.28e9,
    "1RauMuong1": 563.28e9,
    "P107215255": 517.42e9,
    "Drakias": 440.21e9,
    "Stumbi97": 390.76e9,
    "Altair1165": 352.52e9,
    "iBooneh": 295.28e9,
    "BigRagaTheOppStopa": 285.12e9,
    "ScHlAnGE": 271.69e9,
    "SpudNugget18": 241.60e9,
    "AnyDockers": 240.50e9,
    "Ibnt": 207.91e9,
    "tEruPmA": 167.68e9,
    "saare": 124.80e9,
    "Rysor": 108.52e9,
    "Rendaxx": 106.57e9,
    "IlTeino": 86.40e9,
    "NalaStomp": 66.20e9,
    "xavop": 55.99e9,
    "Saludan": 52.98e9,
    "Skytiti": 41.07e9,
    "Jackylefeu": 38.16e9,
    "estimov": 29.93e9,
    "Swidishh": 19.83e9,
    "Katitos": 19.56e9,
    "zozoxo": 13.57e9,
    "Maskiert03": 9.47e9,
    # Not visible in the ranking (choolzy, Atom369, Mightykey, Fredolay,
    # Nad33m, Tvojemama1, Ghost192, Vomenjack, Murkchoppa, DKDKDKDK) --
    # confirmed 0-attack call-out candidates per updated guidance.
}

# Thursday 9/3 -- clean read: damage ranking (1-44 of 48), only the
# unreached tail (ranks 45-48) missing. The 4 members missing (DKDKDKDK,
# Vomenjack, Murkchoppa, Fredolay) are confirmed 0-attack call-out
# candidates per the 9/2 policy update.
invasion_logged_thu = {
    "Pimpanzee": 7.49e12,
    "HyenA": 4.99e12,
    "Drew2264": 3.87e12,
    "RonickForce": 3.72e12,
    "elementten": 2.79e12,
    "Flforever": 2.37e12,
    "BenZoo": 1.74e12,
    "fred21422": 1.55e12,
    "P107215255": 1.11e12,
    "NHTPhat": 1.02e12,
    "Papykique": 909.06e9,
    "Tvojemama1": 865.72e9,
    "Nad33m": 735.28e9,
    "1RauMuong1": 732.49e9,
    "Altair1165": 692.65e9,
    "Ekkehard": 663.82e9,
    "Saludan": 482.86e9,
    "Ghost192": 426.66e9,
    "Drakias": 390.31e9,
    "SpudNugget18": 370.54e9,
    "tEruPmA": 360.80e9,
    "iBooneh": 356.75e9,
    "BigRagaTheOppStopa": 310.61e9,
    "IlTeino": 305.98e9,
    "AnyDockers": 286.16e9,
    "Stumbi97": 275.58e9,
    "Rysor": 212.72e9,
    "NalaStomp": 189.03e9,
    "Jackylefeu": 160.58e9,
    "Ibnt": 124.52e9,
    "Swidishh": 119.37e9,
    "Katitos": 114.80e9,
    "saare": 99.56e9,
    "zozoxo": 94.79e9,
    "ScHlAnGE": 89.53e9,
    "choolzy": 69.45e9,
    "estimov": 63.52e9,
    "Maskiert03": 61.65e9,
    "Rendaxx": 59.01e9,
    "Skytiti": 35.01e9,
    "REAPS": 28.77e9,
    "Atom369": 27.85e9,
    "xavop": 18.30e9,
    "Mightykey": 10.01e9,
    # Not visible in the ranking (DKDKDKDK, Vomenjack, Murkchoppa, Fredolay)
    # -- unreached tail (ranks 45-48), confirmed 0-attack call-out
    # candidates per the 9/2 policy update.
}

# Friday 9/4 -- damage ranking (1-39 of 48), tail (ranks 40-48) unreached
# this batch (only 6 screenshots came in). Murkchoppa is among the 9
# members missing from the ranking, confirming he didn't attack today --
# all 9 (Ekkehard, Tvojemama1, NalaStomp, IlTeino, DKDKDKDK, Vomenjack,
# Murkchoppa, Fredolay, Mightykey) are confirmed 0-attack call-out
# candidates per the 9/2 policy update.
invasion_logged_fri = {
    "Pimpanzee": 9.15e12,
    "Drew2264": 7.85e12,
    "HyenA": 7.48e12,
    "Flforever": 2.90e12,
    "fred21422": 2.71e12,
    "RonickForce": 2.71e12,
    "BenZoo": 1.90e12,
    "P107215255": 1.59e12,
    "NHTPhat": 1.43e12,
    "Papykique": 1.17e12,
    "Altair1165": 880.30e9,
    "elementten": 740.45e9,
    "ScHlAnGE": 701.14e9,
    "iBooneh": 569.00e9,
    "Drakias": 457.34e9,
    "REAPS": 434.90e9,
    "Stumbi97": 423.77e9,
    "Jackylefeu": 396.00e9,
    "SpudNugget18": 347.64e9,
    "BigRagaTheOppStopa": 256.70e9,
    "Ibnt": 227.29e9,
    "tEruPmA": 226.95e9,
    "1RauMuong1": 210.39e9,
    "Skytiti": 158.69e9,
    "saare": 139.56e9,
    "Rendaxx": 127.06e9,
    "Saludan": 112.17e9,
    "estimov": 102.27e9,
    "Rysor": 98.99e9,
    "Nad33m": 71.36e9,
    "xavop": 69.24e9,
    "Atom369": 62.28e9,
    "Ghost192": 61.77e9,
    "AnyDockers": 61.43e9,
    "zozoxo": 36.99e9,
    "choolzy": 33.27e9,
    "Maskiert03": 19.69e9,
    "Swidishh": 19.35e9,
    "Katitos": 14.58e9,
    # Not visible in the ranking (Ekkehard, Tvojemama1, NalaStomp, IlTeino,
    # DKDKDKDK, Vomenjack, Murkchoppa, Fredolay, Mightykey) -- unreached
    # tail (ranks 40-48), confirmed 0-attack call-out candidates.
}

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_DATES = ["8/31", "9/1", "9/2", "9/3", "9/4", "9/5", "9/6"]
DAY_FULL_LABELS = [f"{d} {dt}" for d, dt in zip(DAY_NAMES, DAY_DATES)]
DAY_LOGS = {0: invasion_logged_mon, 1: invasion_logged_tue, 2: invasion_logged_wed, 3: invasion_logged_thu, 4: invasion_logged_fri}
TRACKED_DAYS = sorted(DAY_LOGS.keys())
TODAY_INDEX = 4  # Friday -- the most recently tracked day
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

# Attack counts as (attacks, max) pairs per tracked day. Mon/Tue predate the
# 9/2 policy update (ranking absence alone treated as unconfirmed, not
# call-out eligible); Wed 9/2 onward, ranking absence is a confirmed 0/2 --
# no separate Manage Member screen required.
ATTACK_LOGS = {
    0: {name: ((2, 2) if name in invasion_logged_mon else (0, 0)) for name, role in roster},
    1: {name: ((2, 2) if name in invasion_logged_tue else (0, 0)) for name, role in roster},
    2: {name: ((2, 2) if name in invasion_logged_wed else (0, 0)) for name, role in roster},
    3: {name: ((2, 2) if name in invasion_logged_thu else (0, 0)) for name, role in roster},
    4: {name: ((2, 2) if name in invasion_logged_fri else (0, 0)) for name, role in roster},
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
