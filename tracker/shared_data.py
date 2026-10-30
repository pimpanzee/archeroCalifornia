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
UPDATED_DATE = "Oct 29, 2026"


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
# New week: Mon 10/26 - Sun 11/1. Thursday 10/29 is the first data of this
# week -- Mon 10/26 through Wed 10/28 all had no Shortcut upload (checked
# daily, nothing came in), so the week opens straight from Thursday rather
# than being guessed/backfilled. Damage ranking (1-42 of 48) read off the
# scrollable Guild Member Ranking list; 7 screenshots this batch, no
# Manage Member screen, so donation values are carried forward unchanged
# from the 10/4 full refresh (now over three weeks stale). No new-record
# top-1 today (Pimpanzee 17.23T, below the season record of 27.45T from
# 10/15).
#
# NOTE: rank 30 in this batch shows a name not in the current roster --
# "Fergs", 210.73B damage. This isn't a misread (clearly legible, distinct
# from every existing name). Logged below but deliberately NOT added to
# `roster`/`donation_members` yet, since there's no Manage Member screen
# this batch to confirm role/donation count or whether an existing member
# was replaced. Will reconcile the roster once a Manage Member screenshot
# comes in. Their value is preserved here so it isn't lost if/when they're
# added to the roster retroactively.
#
# The 7 roster members missing from the ranking (Mightykey, Murkchoppa,
# Skytiti, lllmundlll, Papykique, choolzy, BigRagaTheOppStopa) -- ranking
# list ended cleanly at rank 42 right above the pinned own-rank footer, so
# this is the true end of the list, not a mid-scroll gap. Confirmed
# 0-attack call-out candidates per the 9/2 policy.
invasion_logged_thu = {
    "Pimpanzee": 17.23e12,
    "Drew2264": 15.57e12,
    "EpicMarksman": 10.57e12,
    "Flforever": 7.27e12,
    "P107215255": 6.07e12,
    "elementten": 3.87e12,
    "BenZoo": 3.75e12,
    "fred21422": 3.62e12,
    "iBooneh": 3.42e12,
    "NalaStomp": 2.74e12,
    "HyenA": 1.93e12,
    "ScHlAnGE": 1.77e12,
    "Ibnt": 1.63e12,
    "Ghost192": 1.58e12,
    "Drakias": 959.35e9,
    "RonickForce": 769.82e9,
    "Ghoro": 719.26e9,
    "saare": 585.65e9,
    "Jackylefeu": 559.83e9,
    "REAPS": 499.64e9,
    "Ekkehard": 438.30e9,
    "Stumbi97": 417.83e9,
    "estimov": 365.58e9,
    "Rysor": 325.92e9,
    "Atom369": 307.95e9,
    "Rendaxx": 297.46e9,
    "Altair1165": 294.86e9,
    "tEruPmA": 240.04e9,
    "Saludan": 225.77e9,
    "Fergs": 210.73e9,  # not yet in roster -- see note above
    "Tvojemama1": 155.71e9,
    "AnyDockers": 122.28e9,
    "1RauMuong1": 108.30e9,
    "Maskiert03": 102.46e9,
    "Swidishh": 91.51e9,
    "IlTeino": 70.06e9,
    "zozoxo": 42.96e9,
    "Nad33m": 34.95e9,
    "xavop": 32.28e9,
    "Fredolay": 31.37e9,
    "Depfefferle336": 25.98e9,
    "CzosneK": 22.36e9,
    # Not visible in the ranking (Mightykey, Murkchoppa, Skytiti,
    # lllmundlll, Papykique, choolzy, BigRagaTheOppStopa) -- ranking list
    # ended cleanly at rank 42 right above the pinned own-rank footer, so
    # this is the true end of the list, not a mid-scroll gap. Confirmed
    # 0-attack call-out candidates per the 9/2 policy.
}

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_DATES = ["10/26", "10/27", "10/28", "10/29", "10/30", "10/31", "11/1"]
DAY_FULL_LABELS = [f"{d} {dt}" for d, dt in zip(DAY_NAMES, DAY_DATES)]
DAY_LOGS = {3: invasion_logged_thu}
TRACKED_DAYS = sorted(DAY_LOGS.keys())
TODAY_INDEX = 3  # Thursday -- the only tracked day so far this week (Mon-Wed had no upload)
WEEK_LABEL = "wk of 10/26"

# Roster unchanged (Fergs not yet added -- see note above). Donation values
# still carried forward from the 10/4 full refresh -- no Manage Member
# screenshot came in with this batch (now over three weeks stale).
donation_members = [
    ("Mightykey", "Guild Member", 260),
    ("Murkchoppa", "Elder", 270),
    ("Jackylefeu", "Guild Member", 1000),
    ("Tvojemama1", "Guild Member", 1120),
    ("Skytiti", "Guild Member", 1390),
    ("Altair1165", "Guild Member", 2680),
    ("lllmundlll", "Guild Member", 2790),
    ("P107215255", "Guild Member", 2790),
    ("Saludan", "Guild Member", 2760),
    ("Atom369", "Guild Member", 2210),
    ("Fredolay", "Guild Member", 2710),
    ("saare", "Elder", 4300),
    ("ScHlAnGE", "Guild Member", 3220),
    ("Ghost192", "Guild Member", 3230),
    ("Papykique", "Guild Member", 3350),
    ("choolzy", "Guild Member", 3780),
    ("Depfefferle336", "Guild Member", 3650),
    ("tEruPmA", "Guild Member", 3870),
    ("Nad33m", "Guild Member", 3050),
    ("Ibnt", "Guild Member", 3010),
    ("zozoxo", "Guild Member", 3710),
    ("iBooneh", "Elder", 3190),
    ("Maskiert03", "Guild Member", 4210),
    ("HyenA", "Elder", 4740),
    ("Drakias", "Elder", 4830),
    ("IlTeino", "Guild Member", 4520),
    ("CzosneK", "Guild Member", 4840),
    ("Stumbi97", "Guild Member", 4660),
    ("Swidishh", "Guild Member", 4780),
    ("Drew2264", "Vice Leader", 5090),
    ("REAPS", "Guild Member", 4310),
    ("Pimpanzee", "Leader", 5450),
    ("1RauMuong1", "Vice Leader", 4580),
    ("Ekkehard", "Guild Member", 4900),
    ("EpicMarksman", "Guild Member", 4920),
    ("AnyDockers", "Guild Member", 4910),
    ("NalaStomp", "Guild Member", 4960),
    ("fred21422", "Vice Leader", 5340),
    ("estimov", "Guild Member", 5340),
    ("RonickForce", "Vice Leader", 5420),
    ("elementten", "Vice Leader", 5510),
    ("xavop", "Guild Member", 5100),
    ("Rysor", "Guild Member", 5150),
    ("BenZoo", "Elder", 5350),
    ("Flforever", "Guild Member", 4500),
    ("BigRagaTheOppStopa", "Guild Member", 5450),
    ("Rendaxx", "Guild Member", 5220),
    ("Ghoro", "Guild Member", 5600),
]
donation_members.sort(key=lambda m: m[2], reverse=True)

# Full guild roster (name, role) -- derived from the donation list, which is the
# only screenshot set that covered every member.
roster = sorted({(name, role) for name, role, _ in donation_members})

# Attack counts as (attacks, max) pairs per tracked day.
ATTACK_LOGS = {
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
