import base64
from pathlib import Path

FONTS = "/mnt/skills/examples/canvas-design/canvas-fonts"

# Known published URLs -- update DONATIONS_URL after the donations page's first publish.
INVASION_URL = "https://claude.ai/code/artifact/2d3a73a8-5995-4097-8446-2ff20c533627"
DONATIONS_URL = "https://claude.ai/code/artifact/e6f3430a-77ad-41f9-a37a-cde5487c8593"

GUILD_ID = "90754"
UPDATED_DATE = "Aug 20, 2026"


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
# New week: Mon 8/17 - Sun 8/23. Roster carries over from last week at
# 47/48 (RESIIK's departure persisted; no other roster changes observed).
# Unlike the previous week's Monday, this week we have the actual Manage
# Member attack-count screen for Monday, so ATTACKS_MON is real data, not an
# inferred backfill. Damage ranking (1-43 of 47) read off the scrollable
# Guild Member Ranking list; the 4 members missing from it (Maskiert03,
# NalaStomp, Mightykey, 1RauMuong1) are exactly the 4 who show 0 attacks
# below. estimov (rank 31) fell in a gap between two ranking screenshots and
# wasn't directly captured -- its value here is a midpoint estimate bounded
# by its neighbors (ScHlAnGE 66.58B above, zozoxo 51.87B below).
invasion_logged_mon = {
    "HyenA": 3.98e12,
    "Flforever": 2.98e12,
    "Pimpanzee": 2.94e12,
    "RonickForce": 2.30e12,
    "elementten": 1.40e12,
    "fred21422": 1.35e12,
    "BenZoo": 1.24e12,
    "Nad33m": 1.20e12,
    "Drew2264": 966.15e9,
    "NHTPhat": 790.50e9,
    "iBooneh": 730.62e9,
    "Saludan": 659.44e9,
    "REAPS": 623.87e9,
    "Altair1165": 454.07e9,
    "Rendaxx": 413.76e9,
    "DKDKDKDK": 399.53e9,
    "P107215255": 381.92e9,
    "SpudNugget18": 211.67e9,
    "Ekkehard": 200.75e9,
    "AnyDockers": 189.72e9,
    "Drakias": 177.99e9,
    "Rysor": 165.10e9,
    "Ibnt": 162.01e9,
    "BigRagaTheOppStopa": 149.90e9,
    "Tvojemama1": 148.61e9,
    "Skytiti": 119.26e9,
    "saare": 89.55e9,
    "Ghost192": 86.87e9,
    "tEruPmA": 82.02e9,
    "ScHlAnGE": 66.58e9,
    "estimov": 59.00e9,  # inferred midpoint -- see note above
    "zozoxo": 51.87e9,
    "choolzy": 51.72e9,
    "Jackylefeu": 46.75e9,
    "Swidishh": 45.41e9,
    "Stumbi97": 41.67e9,
    "IlTeino": 39.11e9,
    "Katitos": 34.40e9,
    "Vomenjack": 24.58e9,
    "Atom369": 14.61e9,
    "Murkchoppa": 12.36e9,
    "Fredolay": 9.20e9,
    "xavop": 7.47e9,
    # Not visible in the scrolled ranking (Maskiert03, NalaStomp, Mightykey,
    # 1RauMuong1) -- confirmed 0 attacks for the day (see ATTACKS_MON).
}

# Attack count (out of a max of 2/day) for Monday 8/17, read off the red
# skull icon on the Manage Member / donation screens.
ATTACKS_MON = {
    "Stumbi97": 2, "tEruPmA": 2, "ScHlAnGE": 2, "Maskiert03": 0,
    "NalaStomp": 0, "Mightykey": 0, "Nad33m": 2, "Ekkehard": 2, "zozoxo": 2,
    "Flforever": 2, "Katitos": 2, "choolzy": 2, "Tvojemama1": 2,
    "Jackylefeu": 2, "AnyDockers": 2, "BigRagaTheOppStopa": 2, "REAPS": 2,
    "xavop": 1, "Atom369": 2, "Altair1165": 2, "Rendaxx": 2, "Fredolay": 1,
    "IlTeino": 2, "Ibnt": 2, "NHTPhat": 2, "Drakias": 2, "Swidishh": 2,
    "P107215255": 2, "Saludan": 2, "Rysor": 2, "Murkchoppa": 1,
    "SpudNugget18": 2, "fred21422": 2, "estimov": 2, "Skytiti": 1,
    "Ghost192": 2, "RonickForce": 2, "DKDKDKDK": 2, "iBooneh": 2,
    "saare": 2, "HyenA": 2, "BenZoo": 2, "Pimpanzee": 2, "Vomenjack": 1,
    "elementten": 2, "Drew2264": 2, "1RauMuong1": 0,
}

# Tuesday 8/18 -- damage ranking (1-44 of 47), read off the scrollable Guild
# Member Ranking list. The 3 members missing from this ranking (Maskiert03,
# IlTeino, Murkchoppa) are exactly the 3 who show 0 attacks below --
# cross-validated against the Manage Member attack counts.
invasion_logged_tue = {
    "Pimpanzee": 4.52e12,
    "elementten": 3.93e12,
    "Flforever": 2.23e12,
    "HyenA": 1.72e12,
    "BenZoo": 1.63e12,
    "REAPS": 1.32e12,
    "fred21422": 1.17e12,
    "Nad33m": 1.09e12,
    "RonickForce": 1.01e12,
    "DKDKDKDK": 824.44e9,
    "Drew2264": 788.57e9,
    "ScHlAnGE": 720.04e9,
    "P107215255": 529.48e9,
    "Rendaxx": 515.76e9,
    "Atom369": 506.40e9,
    "NHTPhat": 419.12e9,
    "iBooneh": 372.43e9,
    "Skytiti": 359.92e9,
    "Altair1165": 357.93e9,
    "SpudNugget18": 330.27e9,
    "Stumbi97": 296.52e9,
    "Drakias": 284.98e9,
    "tEruPmA": 273.73e9,
    "Ekkehard": 267.85e9,
    "Ghost192": 258.90e9,
    "Vomenjack": 212.19e9,
    "BigRagaTheOppStopa": 185.73e9,
    "Ibnt": 178.37e9,
    "Tvojemama1": 166.59e9,
    "AnyDockers": 157.83e9,
    "choolzy": 128.82e9,
    "saare": 114.00e9,
    "zozoxo": 93.29e9,
    "Saludan": 89.22e9,
    "Rysor": 55.80e9,
    "Jackylefeu": 55.36e9,
    "Swidishh": 47.15e9,
    "estimov": 46.23e9,
    "NalaStomp": 45.81e9,
    "Katitos": 30.86e9,
    "1RauMuong1": 28.17e9,
    "Mightykey": 17.68e9,
    "Fredolay": 11.47e9,
    "xavop": 10.30e9,
    # Not visible in the scrolled ranking (Maskiert03, IlTeino, Murkchoppa) --
    # confirmed 0 attacks for the day (see ATTACKS_TUE).
}

# Attack count (out of a max of 2/day) for Tuesday 8/18, read off the red
# skull icon on the Manage Member / donation screens.
ATTACKS_TUE = {
    "Katitos": 2, "Fredolay": 1, "P107215255": 1, "REAPS": 2, "Mightykey": 2,
    "Maskiert03": 0, "xavop": 1, "Flforever": 2, "Saludan": 2, "choolzy": 2,
    "Stumbi97": 2, "ScHlAnGE": 2, "NalaStomp": 1, "Nad33m": 2, "IlTeino": 0,
    "Altair1165": 2, "BigRagaTheOppStopa": 2, "Ekkehard": 2, "tEruPmA": 2,
    "Ibnt": 2, "Vomenjack": 2, "zozoxo": 2, "Jackylefeu": 2, "AnyDockers": 2,
    "Rysor": 2, "estimov": 2, "SpudNugget18": 2, "Swidishh": 2,
    "Tvojemama1": 1, "Atom369": 2, "Murkchoppa": 0, "Ghost192": 2,
    "NHTPhat": 2, "Skytiti": 2, "fred21422": 2, "Rendaxx": 2, "Drew2264": 2,
    "DKDKDKDK": 2, "HyenA": 2, "BenZoo": 2, "saare": 2, "iBooneh": 2,
    "Pimpanzee": 2, "Drakias": 2, "elementten": 2, "RonickForce": 2,
    "1RauMuong1": 2,
}

# Wednesday 8/19 -- damage ranking (1-43 of 47), read off the scrollable Guild
# Member Ranking list. No Manage Member / donation screenshots came in this
# batch (the upload's 8th image turned out to be a stray screenshot of the
# Shortcuts app itself, not a game screen), so there's no real attack-count
# or donation data for today. Backfilled the same way the very first week's
# Monday was, before we had real attack screens: presence in the ranking is
# treated as a confirmed 2/2, absence as an unconfirmed 0/0 (not 0/2) so it
# doesn't unfairly penalize anyone. Donation values carried forward unchanged
# from 8/18 -- no new read today.
invasion_logged_wed = {
    "Pimpanzee": 5.50e12,
    "HyenA": 3.36e12,
    "RonickForce": 3.23e12,
    "elementten": 2.72e12,
    "Flforever": 1.86e12,
    "BenZoo": 1.37e12,
    "DKDKDKDK": 1.12e12,
    "Rendaxx": 971.90e9,
    "Drew2264": 886.41e9,
    "fred21422": 738.53e9,
    "Stumbi97": 471.64e9,
    "Skytiti": 418.62e9,
    "iBooneh": 381.84e9,
    "AnyDockers": 315.13e9,
    "IlTeino": 298.90e9,
    "P107215255": 281.05e9,
    "Drakias": 251.93e9,
    "Altair1165": 243.60e9,
    "NHTPhat": 240.37e9,
    "Nad33m": 240.33e9,
    "Ibnt": 179.71e9,
    "BigRagaTheOppStopa": 164.64e9,
    "1RauMuong1": 143.11e9,
    "Rysor": 135.96e9,
    "Murkchoppa": 128.77e9,
    "ScHlAnGE": 123.26e9,
    "SpudNugget18": 91.24e9,
    "Ghost192": 76.86e9,
    "NalaStomp": 69.05e9,
    "REAPS": 66.69e9,
    "Saludan": 53.97e9,
    "saare": 52.23e9,
    "Jackylefeu": 43.87e9,
    "Vomenjack": 43.50e9,
    "tEruPmA": 43.02e9,
    "choolzy": 33.14e9,
    "Fredolay": 29.14e9,
    "Maskiert03": 12.99e9,
    "Swidishh": 11.92e9,
    "estimov": 10.10e9,
    "zozoxo": 5.85e9,
    "Katitos": 5.34e9,
    "xavop": 4.96e9,
    # Not visible in the scrolled ranking (Atom369, Mightykey, Tvojemama1,
    # Ekkehard) -- no attack-count screen today to confirm either way, so
    # these are NOT treated as 0-attack call-out candidates (see note above).
}

# Thursday 8/20 -- damage ranking (1-44 of 47), read off the scrollable Guild
# Member Ranking list. No Manage Member / donation screenshots came in this
# batch either (same as 8/19), so no real attack-count or donation data
# today. Backfilled the same way: presence in the ranking treated as a
# confirmed 2/2, absence as an unconfirmed 0/0 (not penalized). Donation
# values carried forward unchanged from 8/18 -- no new read since then.
invasion_logged_thu = {
    "Pimpanzee": 6.28e12,
    "elementten": 4.15e12,
    "HyenA": 4.14e12,
    "BenZoo": 3.22e12,
    "DKDKDKDK": 2.72e12,
    "fred21422": 2.09e12,
    "Flforever": 1.83e12,
    "Nad33m": 1.81e12,
    "RonickForce": 1.49e12,
    "iBooneh": 1.00e12,
    "Drew2264": 921.56e9,
    "P107215255": 867.12e9,
    "Ghost192": 850.40e9,
    "Rendaxx": 846.10e9,
    "ScHlAnGE": 524.61e9,
    "1RauMuong1": 520.66e9,
    "SpudNugget18": 461.35e9,
    "REAPS": 365.49e9,
    "Stumbi97": 364.25e9,
    "saare": 285.54e9,
    "Tvojemama1": 283.85e9,
    "Ibnt": 279.34e9,
    "tEruPmA": 208.76e9,
    "Drakias": 190.74e9,
    "NHTPhat": 189.50e9,
    "Altair1165": 180.63e9,
    "Atom369": 163.88e9,
    "Ekkehard": 161.06e9,
    "NalaStomp": 159.97e9,
    "zozoxo": 106.99e9,
    "Rysor": 100.15e9,
    "AnyDockers": 99.29e9,
    "Skytiti": 97.75e9,
    "BigRagaTheOppStopa": 84.76e9,
    "choolzy": 54.34e9,
    "Katitos": 40.84e9,
    "Maskiert03": 38.36e9,
    "estimov": 35.57e9,
    "Jackylefeu": 34.85e9,
    "Swidishh": 23.66e9,
    "IlTeino": 22.37e9,
    "xavop": 12.06e9,
    "Mightykey": 10.30e9,
    "Fredolay": 8.22e9,
    # Not visible in the scrolled ranking (Saludan, Vomenjack, Murkchoppa) --
    # no attack-count screen today to confirm either way, so these are NOT
    # treated as 0-attack call-out candidates (see note above).
}

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_DATES = ["8/17", "8/18", "8/19", "8/20", "8/21", "8/22", "8/23"]
DAY_FULL_LABELS = [f"{d} {dt}" for d, dt in zip(DAY_NAMES, DAY_DATES)]
DAY_LOGS = {0: invasion_logged_mon, 1: invasion_logged_tue, 2: invasion_logged_wed, 3: invasion_logged_thu}
TRACKED_DAYS = sorted(DAY_LOGS.keys())
TODAY_INDEX = 3  # Thursday -- the most recently tracked day
WEEK_LABEL = "wk of 8/17"

# Roster (47/48 -- RESIIK's departure from last week persisted; no other
# changes observed), read off the Manage Member / donation screens on 8/17.
# Donation values below reset to this week's (8/17-8/23) fresh counts.
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
]
donation_members.sort(key=lambda m: m[2], reverse=True)

# Full guild roster (name, role) -- derived from the donation list, which is the
# only screenshot set that covered every member.
roster = sorted({(name, role) for name, role, _ in donation_members})

# Attack counts as (attacks, max) pairs per tracked day. This week Monday
# has real per-member attack-count data (ATTACKS_MON), unlike last week
# where Monday had to be inferred from damage-ranking presence alone.
ATTACK_LOGS = {
    0: {name: (ATTACKS_MON.get(name, 0), 2) for name, role in roster},
    1: {name: (ATTACKS_TUE.get(name, 0), 2) for name, role in roster},
    2: {name: ((2, 2) if name in invasion_logged_wed else (0, 0)) for name, role in roster},
    3: {name: ((2, 2) if name in invasion_logged_thu else (0, 0)) for name, role in roster},
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
