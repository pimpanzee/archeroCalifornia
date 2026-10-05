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
UPDATED_DATE = "Oct 4, 2026"


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
# New week: Mon 9/28 - Sun 10/4. Damage ranking (1-44 of 48) read off the
# scrollable Guild Member Ranking list; 7 screenshots this batch, no
# Manage Member screen, so donation values are carried forward unchanged
# from 9/20. New member spotted: CzosneK (rank 34, 119.28B) -- added to
# the roster below with donation unknown (defaulted to 0) pending a
# Manage Member screenshot. The 4 members missing from the ranking
# (AnyDockers, Papykique, Mightykey, Murkchoppa) are confirmed 0-attack
# call-out candidates per the 9/2 policy.
invasion_logged_mon = {
    "Pimpanzee": 6.16e12,
    "Drew2264": 5.15e12,
    "HyenA": 4.34e12,
    "P107215255": 4.15e12,
    "RonickForce": 3.31e12,
    "Flforever": 3.14e12,
    "elementten": 2.87e12,
    "Nad33m": 2.14e12,
    "fred21422": 1.77e12,
    "Tvojemama1": 1.61e12,
    "BenZoo": 1.50e12,
    "EpicMarksman": 1.10e12,
    "iBooneh": 1.10e12,
    "Altair1165": 1.08e12,
    "Saludan": 1.03e12,
    "ScHlAnGE": 725.72e9,
    "Ibnt": 671.37e9,
    "Ekkehard": 534.25e9,
    "Drakias": 480.75e9,
    "1RauMuong1": 321.89e9,
    "BigRagaTheOppStopa": 313.34e9,
    "REAPS": 308.13e9,
    "choolzy": 262.38e9,
    "NalaStomp": 214.83e9,
    "Stumbi97": 213.83e9,
    "Jackylefeu": 199.37e9,
    "Ghost192": 197.88e9,
    "Ghoro": 188.06e9,
    "Maskiert03": 187.95e9,
    "Rysor": 170.19e9,
    "estimov": 162.10e9,
    "lllmundlll": 139.98e9,
    "saare": 128.27e9,
    "CzosneK": 119.28e9,
    "IlTeino": 99.38e9,
    "Atom369": 93.17e9,
    "Rendaxx": 86.85e9,
    "Skytiti": 68.61e9,
    "Swidishh": 65.52e9,
    "tEruPmA": 48.75e9,
    "xavop": 41.52e9,
    "Fredolay": 38.86e9,
    "zozoxo": 19.73e9,
    "Depfefferle336": 7.70e9,
    # Not visible in the ranking (AnyDockers, Papykique, Mightykey,
    # Murkchoppa) -- ranking list ended cleanly at rank 44 right above the
    # pinned own-rank footer, so this is the true end of the list, not a
    # mid-scroll gap. Confirmed 0-attack call-out candidates per the 9/2
    # policy.
}

# Tuesday 9/29 -- no Shortcut upload came in at all, so there's no data to
# log for this day. Deliberately left untracked (no invasion_logged_tue
# dict, no entry in DAY_LOGS) rather than guessed or backfilled -- the
# weekly denominators below only count days actually in TRACKED_DAYS.

# Wednesday 9/30 -- damage ranking (1-42 of 48) read off the scrollable
# Guild Member Ranking list; 7 screenshots this batch, no Manage Member
# screen, so donation values are still carried forward from 9/20 (now
# quite stale -- over a week old). The 6 members missing from the ranking
# (Depfefferle336, Papykique, Ghost192, Saludan, Mightykey, Murkchoppa)
# -- ranking list ended cleanly at rank 42 right above the pinned
# own-rank footer, so this is the true end of the list, not a mid-scroll
# gap. Confirmed 0-attack call-out candidates per the 9/2 policy.
invasion_logged_wed = {
    "Pimpanzee": 6.59e12,
    "Drew2264": 5.27e12,
    "HyenA": 4.55e12,
    "elementten": 4.21e12,
    "Flforever": 3.76e12,
    "EpicMarksman": 3.76e12,
    "iBooneh": 1.98e12,
    "P107215255": 1.98e12,
    "Tvojemama1": 1.91e12,
    "Nad33m": 1.85e12,
    "fred21422": 1.74e12,
    "BenZoo": 1.63e12,
    "RonickForce": 1.29e12,
    "ScHlAnGE": 1.22e12,
    "Drakias": 709.75e9,
    "NalaStomp": 671.34e9,
    "Stumbi97": 529.66e9,
    "1RauMuong1": 515.17e9,
    "CzosneK": 468.17e9,
    "Ekkehard": 403.17e9,
    "REAPS": 384.70e9,
    "BigRagaTheOppStopa": 324.58e9,
    "Jackylefeu": 314.79e9,
    "Rysor": 267.12e9,
    "Ibnt": 244.08e9,
    "choolzy": 232.60e9,
    "AnyDockers": 231.74e9,
    "estimov": 218.43e9,
    "Skytiti": 206.35e9,
    "lllmundlll": 200.15e9,
    "tEruPmA": 148.23e9,
    "Rendaxx": 99.12e9,
    "Maskiert03": 74.08e9,
    "Atom369": 71.82e9,
    "Altair1165": 47.69e9,
    "IlTeino": 41.16e9,
    "Ghoro": 37.00e9,
    "saare": 34.98e9,
    "xavop": 16.02e9,
    "Fredolay": 12.24e9,
    "zozoxo": 11.84e9,
    "Swidishh": 10.88e9,
    # Not visible in the ranking (Depfefferle336, Papykique, Ghost192,
    # Saludan, Mightykey, Murkchoppa) -- ranking list ended cleanly at
    # rank 42 right above the pinned own-rank footer, so this is the true
    # end of the list, not a mid-scroll gap. Confirmed 0-attack call-out
    # candidates per the 9/2 policy.
}

# Thursday 10/1, Friday 10/2, Saturday 10/3 -- no Shortcut uploads came in
# on any of these three days, so there's no data to log. Deliberately left
# untracked (no invasion_logged_* dicts, no entries in DAY_LOGS) rather
# than guessed or backfilled.

# Sunday 10/4 -- damage ranking (1-43 of 48) read off the scrollable Guild
# Member Ranking list, PLUS a full Manage Member sweep (7 screenshots)
# covering all 48 members -- the first complete donation/attack refresh
# since 9/20. Real per-member attack counts (0-2) used below instead of
# the usual (2,2)/(0,0) backfill. The 5 members showing 0 attacks on the
# Manage Member screens (Tvojemama1, P107215255, Ghost192, Mightykey,
# Murkchoppa) are an exact match for the 5 missing from the damage
# ranking -- full cross-validation, confirmed 0-attack call-out
# candidates. Papykique and Atom369 attacked once (1x); elementten also
# shows 1x despite being top-5 in damage.
invasion_logged_sun = {
    "Pimpanzee": 8.32e12,
    "EpicMarksman": 4.77e12,
    "Flforever": 2.28e12,
    "HyenA": 2.06e12,
    "elementten": 1.85e12,
    "Drew2264": 1.06e12,
    "fred21422": 920.52e9,
    "iBooneh": 726.27e9,
    "RonickForce": 702.98e9,
    "Skytiti": 533.71e9,
    "Ibnt": 437.72e9,
    "ScHlAnGE": 422.39e9,
    "BigRagaTheOppStopa": 278.09e9,
    "BenZoo": 220.73e9,
    "NalaStomp": 198.12e9,
    "AnyDockers": 186.91e9,
    "Ghoro": 172.39e9,
    "Ekkehard": 133.97e9,
    "1RauMuong1": 129.72e9,
    "saare": 121.45e9,
    "Rendaxx": 110.99e9,
    "Atom369": 108.58e9,
    "choolzy": 106.82e9,
    "Saludan": 93.82e9,
    "Drakias": 77.93e9,
    "Stumbi97": 73.01e9,
    "lllmundlll": 72.43e9,
    "tEruPmA": 64.05e9,
    "IlTeino": 54.23e9,
    "REAPS": 53.60e9,
    "estimov": 53.56e9,
    "Maskiert03": 53.46e9,
    "Altair1165": 41.64e9,
    "Papykique": 25.97e9,
    "Jackylefeu": 24.05e9,
    "zozoxo": 21.85e9,
    "Nad33m": 17.65e9,
    "Swidishh": 15.99e9,
    "Fredolay": 15.46e9,
    "Rysor": 12.35e9,
    "CzosneK": 7.18e9,
    "Depfefferle336": 6.70e9,
    "xavop": 5.09e9,
    # Not visible in the ranking (Tvojemama1, P107215255, Ghost192,
    # Mightykey, Murkchoppa) -- confirmed 0 attacks via the Manage Member
    # screens (exact cross-validation match).
}

# Real per-member attack counts (0-2) from the 10/4 Manage Member sweep.
ATTACKS_SUN = {
    "Pimpanzee": 2, "EpicMarksman": 2, "Flforever": 2, "HyenA": 2,
    "elementten": 1, "Drew2264": 2, "fred21422": 2, "iBooneh": 2,
    "RonickForce": 2, "Skytiti": 2, "Ibnt": 2, "ScHlAnGE": 2,
    "BigRagaTheOppStopa": 2, "BenZoo": 2, "NalaStomp": 2, "AnyDockers": 2,
    "Ghoro": 2, "Ekkehard": 2, "1RauMuong1": 2, "saare": 2, "Rendaxx": 2,
    "Atom369": 1, "choolzy": 2, "Saludan": 2, "Drakias": 2, "Stumbi97": 2,
    "lllmundlll": 2, "tEruPmA": 2, "IlTeino": 2, "REAPS": 2, "estimov": 2,
    "Maskiert03": 2, "Altair1165": 2, "Papykique": 1, "Jackylefeu": 2,
    "zozoxo": 2, "Nad33m": 2, "Swidishh": 2, "Fredolay": 2, "Rysor": 2,
    "CzosneK": 2, "Depfefferle336": 2, "xavop": 2, "Tvojemama1": 0,
    "P107215255": 0, "Ghost192": 0, "Mightykey": 0, "Murkchoppa": 0,
}

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_DATES = ["9/28", "9/29", "9/30", "10/1", "10/2", "10/3", "10/4"]
DAY_FULL_LABELS = [f"{d} {dt}" for d, dt in zip(DAY_NAMES, DAY_DATES)]
DAY_LOGS = {0: invasion_logged_mon, 2: invasion_logged_wed, 6: invasion_logged_sun}
TRACKED_DAYS = sorted(DAY_LOGS.keys())
TODAY_INDEX = 6  # Sunday -- the most recently tracked day (Tue 9/29, Thu 10/1, Fri 10/2, Sat 10/3 have no data, no uploads came in)
WEEK_LABEL = "wk of 9/28"

# Full refresh as of 10/4 -- first complete Manage Member sweep since
# 9/20, covering all 48 current members. No joins or departures this
# round; roles unchanged.
donation_members = [
    ("CzosneK", "Guild Member", 4840),
    ("lllmundlll", "Guild Member", 2790),
    ("Depfefferle336", "Guild Member", 3650),
    ("choolzy", "Guild Member", 3780),
    ("Ekkehard", "Guild Member", 4900),
    ("NalaStomp", "Guild Member", 4960),
    ("Fredolay", "Guild Member", 2710),
    ("ScHlAnGE", "Guild Member", 3220),
    ("Rysor", "Guild Member", 5150),
    ("REAPS", "Guild Member", 4310),
    ("Jackylefeu", "Guild Member", 1000),
    ("EpicMarksman", "Guild Member", 4920),
    ("AnyDockers", "Guild Member", 4910),
    ("Maskiert03", "Guild Member", 4210),
    ("Atom369", "Guild Member", 2210),
    ("Stumbi97", "Guild Member", 4660),
    ("Rendaxx", "Guild Member", 5220),
    ("Ibnt", "Guild Member", 3010),
    ("zozoxo", "Guild Member", 3710),
    ("Papykique", "Guild Member", 3350),
    ("Tvojemama1", "Guild Member", 1120),
    ("xavop", "Guild Member", 5100),
    ("P107215255", "Guild Member", 2790),
    ("Skytiti", "Guild Member", 1390),
    ("Ghost192", "Guild Member", 3230),
    ("Altair1165", "Guild Member", 2680),
    ("Saludan", "Guild Member", 2760),
    ("BigRagaTheOppStopa", "Guild Member", 5450),
    ("tEruPmA", "Guild Member", 3870),
    ("Nad33m", "Guild Member", 3050),
    ("iBooneh", "Elder", 3190),
    ("BenZoo", "Elder", 5350),
    ("estimov", "Guild Member", 5340),
    ("IlTeino", "Guild Member", 4520),
    ("Swidishh", "Guild Member", 4780),
    ("Mightykey", "Guild Member", 260),
    ("Ghoro", "Guild Member", 5600),
    ("1RauMuong1", "Vice Leader", 4580),
    ("fred21422", "Vice Leader", 5340),
    ("Drew2264", "Vice Leader", 5090),
    ("Drakias", "Elder", 4830),
    ("HyenA", "Elder", 4740),
    ("Murkchoppa", "Elder", 270),
    ("saare", "Elder", 4300),
    ("Pimpanzee", "Leader", 5450),
    ("Flforever", "Guild Member", 4500),
    ("elementten", "Vice Leader", 5510),
    ("RonickForce", "Vice Leader", 5420),
]
donation_members.sort(key=lambda m: m[2], reverse=True)

# Full guild roster (name, role) -- derived from the donation list, which is the
# only screenshot set that covered every member.
roster = sorted({(name, role) for name, role, _ in donation_members})

# Attack counts as (attacks, max) pairs per tracked day.
ATTACK_LOGS = {
    0: {name: ((2, 2) if name in invasion_logged_mon else (0, 0)) for name, role in roster},
    2: {name: ((2, 2) if name in invasion_logged_wed else (0, 0)) for name, role in roster},
    6: {name: (ATTACKS_SUN.get(name, 0), 2) for name, role in roster},
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
