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
UPDATED_DATE = "Sep 25, 2026"


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

# Tuesday 9/22 -- damage ranking (1-44 of 47) read off the scrollable
# Guild Member Ranking list, tail (ranks 45-47) unreached (only 7
# screenshots this batch, no Manage Member screen). Pimpanzee's 11.50T is
# a new season-high #1 (previous high was HyenA's 10.18T on 9/17).
# Donation values still carried forward from 9/20. The 3 members missing
# from the ranking (REAPS, BigRagaTheOppStopa, Mightykey) are confirmed
# 0-attack call-out candidates per the 9/2 policy.
invasion_logged_tue = {
    "Pimpanzee": 11.50e12,
    "EpicMarksman": 8.90e12,
    "HyenA": 4.70e12,
    "RonickForce": 4.20e12,
    "Drew2264": 3.76e12,
    "fred21422": 3.64e12,
    "Flforever": 3.06e12,
    "P107215255": 2.46e12,
    "elementten": 2.37e12,
    "ScHlAnGE": 2.07e12,
    "BenZoo": 1.78e12,
    "iBooneh": 1.44e12,
    "Tvojemama1": 1.38e12,
    "Papykique": 1.31e12,
    "Ibnt": 627.46e9,
    "Drakias": 496.70e9,
    "Ekkehard": 438.42e9,
    "Altair1165": 404.15e9,
    "Atom369": 358.87e9,
    "NalaStomp": 349.04e9,
    "Nad33m": 254.46e9,
    "Stumbi97": 244.57e9,
    "Skytiti": 242.81e9,
    "AnyDockers": 196.46e9,
    "saare": 193.84e9,
    "Saludan": 189.11e9,
    "Ghost192": 183.83e9,
    "estimov": 178.39e9,
    "choolzy": 169.11e9,
    "Rysor": 161.95e9,
    "Ghoro": 146.61e9,
    "lllmundlll": 140.26e9,
    "Rendaxx": 128.92e9,
    "tEruPmA": 119.88e9,
    "IlTeino": 110.86e9,
    "Jackylefeu": 110.59e9,
    "1RauMuong1": 110.32e9,
    "Maskiert03": 109.57e9,
    "Murkchoppa": 102.34e9,
    "zozoxo": 67.58e9,
    "xavop": 47.26e9,
    "Fredolay": 38.24e9,
    "Swidishh": 27.13e9,
    "Depfefferle336": 7.92e9,
    # Not visible in the ranking (REAPS, BigRagaTheOppStopa, Mightykey) --
    # unreached tail (ranks 45-47), confirmed 0-attack call-out candidates
    # per the 9/2 policy.
}

# Wednesday 9/23 -- damage ranking (1-40 of 47) read off the scrollable
# Guild Member Ranking list, tail (ranks 41-47) unreached (only 7
# screenshots this batch, no Manage Member screen). Donation values still
# carried forward from 9/20. The 7 members missing from the ranking
# (AnyDockers, Maskiert03, Papykique, Murkchoppa, lllmundlll, Mightykey,
# Depfefferle336) are confirmed 0-attack call-out candidates per the 9/2
# policy.
invasion_logged_wed = {
    "EpicMarksman": 7.25e12,
    "HyenA": 6.39e12,
    "RonickForce": 6.31e12,
    "Drew2264": 5.51e12,
    "Pimpanzee": 5.41e12,
    "elementten": 5.03e12,
    "Flforever": 4.70e12,
    "fred21422": 3.61e12,
    "BenZoo": 3.00e12,
    "P107215255": 1.82e12,
    "NalaStomp": 1.50e12,
    "iBooneh": 1.31e12,
    "1RauMuong1": 1.21e12,
    "ScHlAnGE": 1.18e12,
    "Tvojemama1": 832.41e9,
    "Ibnt": 580.37e9,
    "Ekkehard": 546.11e9,
    "BigRagaTheOppStopa": 412.11e9,
    "Drakias": 397.87e9,
    "saare": 378.86e9,
    "Saludan": 323.57e9,
    "choolzy": 321.21e9,
    "Rysor": 239.14e9,
    "REAPS": 142.71e9,
    "zozoxo": 136.88e9,
    "Rendaxx": 124.66e9,
    "Ghoro": 123.13e9,
    "Stumbi97": 110.28e9,
    "IlTeino": 85.96e9,
    "Jackylefeu": 81.94e9,
    "Altair1165": 72.94e9,
    "Skytiti": 55.29e9,
    "Ghost192": 52.11e9,
    "tEruPmA": 37.79e9,
    "Nad33m": 31.54e9,
    "Atom369": 27.61e9,
    "xavop": 25.54e9,
    "estimov": 23.09e9,
    "Swidishh": 9.24e9,
    "Fredolay": 6.70e9,
    # Not visible in the ranking (AnyDockers, Maskiert03, Papykique,
    # Murkchoppa, lllmundlll, Mightykey, Depfefferle336) -- unreached tail
    # (ranks 41-47), confirmed 0-attack call-out candidates per the 9/2
    # policy.
}

# Thursday 9/24 -- damage ranking (1-42 of 47) read off the scrollable
# Guild Member Ranking list, tail (ranks 43-47) unreached (only 7
# screenshots this batch, no Manage Member screen). Pimpanzee's 13.69T is
# a new season-high #1 (previous high was Pimpanzee's own 11.50T on
# 9/22). Donation values still carried forward from 9/20. The 5 members
# missing from the ranking (Rendaxx, Papykique, Skytiti, Mightykey,
# Murkchoppa) are confirmed 0-attack call-out candidates per the 9/2
# policy.
invasion_logged_thu = {
    "Pimpanzee": 13.69e12,
    "HyenA": 8.71e12,
    "Flforever": 6.42e12,
    "Drew2264": 6.07e12,
    "P107215255": 4.32e12,
    "fred21422": 3.32e12,
    "ScHlAnGE": 2.96e12,
    "EpicMarksman": 2.57e12,
    "BenZoo": 2.51e12,
    "RonickForce": 1.83e12,
    "REAPS": 1.62e12,
    "iBooneh": 1.45e12,
    "NalaStomp": 1.14e12,
    "Tvojemama1": 1.13e12,
    "elementten": 1.13e12,
    "Drakias": 621.50e9,
    "Altair1165": 591.73e9,
    "lllmundlll": 577.87e9,
    "Ekkehard": 526.82e9,
    "Atom369": 520.43e9,
    "Jackylefeu": 497.58e9,
    "Ghost192": 488.91e9,
    "Ibnt": 447.03e9,
    "BigRagaTheOppStopa": 411.72e9,
    "1RauMuong1": 408.74e9,
    "Saludan": 405.98e9,
    "Stumbi97": 391.82e9,
    "Maskiert03": 381.74e9,
    "AnyDockers": 309.47e9,
    "IlTeino": 294.08e9,
    "tEruPmA": 238.90e9,
    "Ghoro": 205.63e9,
    "choolzy": 130.77e9,
    "Nad33m": 114.95e9,
    "saare": 114.58e9,
    "zozoxo": 110.62e9,
    "Fredolay": 105.69e9,
    "estimov": 77.57e9,
    "Rysor": 54.21e9,
    "xavop": 47.69e9,
    "Swidishh": 20.43e9,
    "Depfefferle336": 9.21e9,
    # Not visible in the ranking (Rendaxx, Papykique, Skytiti, Mightykey,
    # Murkchoppa) -- unreached tail (ranks 43-47), confirmed 0-attack
    # call-out candidates per the 9/2 policy.
}

# Friday 9/25 -- damage ranking (1-41 of 47) read off the scrollable
# Guild Member Ranking list, tail (ranks 42-47) unreached (only 7
# screenshots this batch, no Manage Member screen). Donation values still
# carried forward from 9/20. The 6 members missing from the ranking
# (Ekkehard, REAPS, Atom369, Skytiti, Murkchoppa, Mightykey) are
# confirmed 0-attack call-out candidates per the 9/2 policy.
invasion_logged_fri = {
    "HyenA": 10.68e12,
    "P107215255": 6.96e12,
    "EpicMarksman": 6.02e12,
    "Drew2264": 3.82e12,
    "elementten": 3.59e12,
    "Tvojemama1": 2.93e12,
    "Pimpanzee": 2.89e12,
    "Flforever": 2.85e12,
    "fred21422": 2.50e12,
    "iBooneh": 1.66e12,
    "Stumbi97": 1.00e12,
    "RonickForce": 969.17e9,
    "NalaStomp": 845.63e9,
    "AnyDockers": 815.85e9,
    "BigRagaTheOppStopa": 771.13e9,
    "1RauMuong1": 754.84e9,
    "Papykique": 637.23e9,
    "Altair1165": 626.56e9,
    "Drakias": 621.97e9,
    "BenZoo": 565.30e9,
    "Ghost192": 514.55e9,
    "Nad33m": 439.27e9,
    "Jackylefeu": 428.12e9,
    "Ibnt": 393.30e9,
    "saare": 384.47e9,
    "Saludan": 363.56e9,
    "ScHlAnGE": 353.07e9,
    "IlTeino": 235.71e9,
    "Maskiert03": 233.14e9,
    "choolzy": 224.21e9,
    "Ghoro": 173.07e9,
    "lllmundlll": 152.81e9,
    "estimov": 105.83e9,
    "Rendaxx": 93.05e9,
    "tEruPmA": 84.71e9,
    "xavop": 65.16e9,
    "Rysor": 42.72e9,
    "Fredolay": 41.90e9,
    "zozoxo": 34.55e9,
    "Swidishh": 30.99e9,
    "Depfefferle336": 3.06e9,
    # Not visible in the ranking (Ekkehard, REAPS, Atom369, Skytiti,
    # Murkchoppa, Mightykey) -- unreached tail (ranks 42-47), confirmed
    # 0-attack call-out candidates per the 9/2 policy.
}

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_DATES = ["9/21", "9/22", "9/23", "9/24", "9/25", "9/26", "9/27"]
DAY_FULL_LABELS = [f"{d} {dt}" for d, dt in zip(DAY_NAMES, DAY_DATES)]
DAY_LOGS = {0: invasion_logged_mon, 1: invasion_logged_tue, 2: invasion_logged_wed, 3: invasion_logged_thu, 4: invasion_logged_fri}
TRACKED_DAYS = sorted(DAY_LOGS.keys())
TODAY_INDEX = 4  # Friday -- the most recently tracked day
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
