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
UPDATED_DATE = "Nov 6, 2026"


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

# Friday 10/30 -- damage ranking (1-43 of 48) read off the scrollable
# Guild Member Ranking list; 7 screenshots this batch, no Manage Member
# screen, so donation values are still carried forward from the 10/4 full
# refresh (now nearly four weeks stale). No new top-1 record (Pimpanzee
# 14.33T, below the season record of 27.45T from 10/15). "Fergs" appears
# again at rank 22 (371.98B) -- second day in a row, reinforcing that this
# is a real (likely new) member rather than a one-off misread, but still
# not added to roster/donation_members pending a Manage Member screenshot
# to confirm their role and donation count. The 6 roster members missing
# from the ranking (Mightykey, Murkchoppa, Skytiti, Altair1165, choolzy,
# REAPS) -- ranking list ended cleanly at rank 43 right above the pinned
# own-rank footer, so this is the true end of the list, not a mid-scroll
# gap. Confirmed 0-attack call-out candidates per the 9/2 policy.
invasion_logged_fri = {
    "Pimpanzee": 14.33e12,
    "EpicMarksman": 14.30e12,
    "Flforever": 11.25e12,
    "Drew2264": 7.35e12,
    "fred21422": 6.80e12,
    "P107215255": 3.92e12,
    "iBooneh": 3.53e12,
    "BenZoo": 2.96e12,
    "HyenA": 2.89e12,
    "elementten": 2.83e12,
    "RonickForce": 2.59e12,
    "Ibnt": 2.19e12,
    "Papykique": 1.71e12,
    "ScHlAnGE": 1.55e12,
    "Atom369": 1.43e12,
    "Drakias": 1.22e12,
    "BigRagaTheOppStopa": 819.87e9,
    "Ekkehard": 662.97e9,
    "NalaStomp": 639.30e9,
    "Rysor": 454.57e9,
    "1RauMuong1": 398.31e9,
    "Fergs": 371.98e9,  # not yet in roster -- see note above
    "estimov": 305.97e9,
    "Stumbi97": 241.30e9,
    "Ghost192": 225.48e9,
    "Tvojemama1": 211.52e9,
    "tEruPmA": 177.52e9,
    "Ghoro": 164.02e9,
    "Maskiert03": 142.60e9,
    "Jackylefeu": 139.96e9,
    "xavop": 111.10e9,
    "Rendaxx": 106.18e9,
    "CzosneK": 105.21e9,
    "IlTeino": 100.94e9,
    "saare": 95.71e9,
    "Saludan": 92.81e9,
    "zozoxo": 61.50e9,
    "Swidishh": 51.23e9,
    "AnyDockers": 39.07e9,
    "Depfefferle336": 31.33e9,
    "Nad33m": 28.21e9,
    "Fredolay": 21.61e9,
    "lllmundlll": 11.31e9,
    # Not visible in the ranking (Mightykey, Murkchoppa, Skytiti,
    # Altair1165, choolzy, REAPS) -- ranking list ended cleanly at rank 43
    # right above the pinned own-rank footer, so this is the true end of
    # the list, not a mid-scroll gap. Confirmed 0-attack call-out
    # candidates per the 9/2 policy.
}

# New week: Mon 11/2 - Sun 11/8. Mon 11/2 and Tue 11/3 both had no
# Shortcut upload (checked daily, nothing came in), so the week opens
# straight from Wednesday 11/4 rather than being guessed/backfilled.
# Damage ranking (1-41 of 48) read off the scrollable Guild Member
# Ranking list; 7 screenshots this batch, no Manage Member screen, so
# donation values are still carried forward from the 10/4 full refresh
# (well over four weeks stale now). No new top-1 record (Pimpanzee
# 13.88T, below the season record of 27.45T from 10/15). "Fergs" appears
# again at rank 27 (263.36B) -- third day in a row it's shown up (10/29,
# 10/30, 11/4), about as strong a confirmation as screenshots alone can
# give that this is a real member, but still not added to
# roster/donation_members pending a Manage Member screenshot to confirm
# role and donation count. The 8 roster members missing from the ranking
# (Mightykey, Murkchoppa, Skytiti, Altair1165, Papykique, choolzy,
# IlTeino, NalaStomp) -- ranking list ended cleanly at rank 41 right
# above the pinned own-rank footer, so this is the true end of the list,
# not a mid-scroll gap. Confirmed 0-attack call-out candidates per the
# 9/2 policy.
invasion_logged_wed = {
    "Pimpanzee": 13.88e12,
    "iBooneh": 6.93e12,
    "Drew2264": 6.27e12,
    "HyenA": 5.89e12,
    "EpicMarksman": 5.41e12,
    "RonickForce": 5.31e12,
    "fred21422": 4.11e12,
    "P107215255": 4.07e12,
    "Flforever": 3.38e12,
    "elementten": 3.05e12,
    "BenZoo": 1.94e12,
    "Ghost192": 1.54e12,
    "1RauMuong1": 1.18e12,
    "Atom369": 1.06e12,
    "saare": 904.27e9,
    "Stumbi97": 860.28e9,
    "ScHlAnGE": 848.42e9,
    "Drakias": 778.77e9,
    "Ibnt": 647.18e9,
    "Rysor": 618.84e9,
    "REAPS": 560.05e9,
    "Ekkehard": 501.21e9,
    "Tvojemama1": 467.13e9,
    "BigRagaTheOppStopa": 408.33e9,
    "Maskiert03": 406.47e9,
    "Jackylefeu": 361.82e9,
    "Fergs": 263.36e9,  # not yet in roster -- see note above
    "Ghoro": 180.16e9,
    "tEruPmA": 142.77e9,
    "Depfefferle336": 134.86e9,
    "Saludan": 93.79e9,
    "AnyDockers": 85.27e9,
    "Rendaxx": 83.03e9,
    "lllmundlll": 74.05e9,
    "estimov": 42.63e9,
    "xavop": 31.92e9,
    "Nad33m": 30.26e9,
    "Swidishh": 27.78e9,
    "zozoxo": 11.45e9,
    "CzosneK": 7.91e9,
    "Fredolay": 4.08e9,
    # Not visible in the ranking (Mightykey, Murkchoppa, Skytiti,
    # Altair1165, Papykique, choolzy, IlTeino, NalaStomp) -- ranking list
    # ended cleanly at rank 41 right above the pinned own-rank footer, so
    # this is the true end of the list, not a mid-scroll gap. Confirmed
    # 0-attack call-out candidates per the 9/2 policy.
}

# Thursday 11/5 -- damage ranking (1-39 of 48) read off the scrollable
# Guild Member Ranking list; 6 screenshots this batch, no Manage Member
# screen, so donation values are still carried forward from the 10/4 full
# refresh (now over five weeks stale). No new top-1 record (Pimpanzee
# 20.76T, below the season record of 27.45T from 10/15). "Fergs" appears
# again at rank 31 (144.64B) -- fourth day running (10/29, 10/30, 11/4,
# 11/5), still not added to roster/donation_members pending a Manage
# Member screenshot. The 10 roster members missing from the ranking
# (Mightykey, Murkchoppa, Tvojemama1, Altair1165, Papykique, choolzy,
# Depfefferle336, Ekkehard, EpicMarksman, NalaStomp) -- ranking list
# ended cleanly at rank 39 right above the pinned own-rank footer, so
# this is the true end of the list, not a mid-scroll gap. Confirmed
# 0-attack call-out candidates per the 9/2 policy.
invasion_logged_thu = {
    "Pimpanzee": 20.76e12,
    "HyenA": 16.84e12,
    "RonickForce": 7.82e12,
    "Flforever": 6.79e12,
    "P107215255": 6.79e12,
    "iBooneh": 5.11e12,
    "Drew2264": 4.54e12,
    "BenZoo": 4.00e12,
    "fred21422": 2.99e12,
    "Ghost192": 2.35e12,
    "Ibnt": 1.88e12,
    "elementten": 1.38e12,
    "ScHlAnGE": 1.27e12,
    "Drakias": 1.08e12,
    "BigRagaTheOppStopa": 967.89e9,
    "Atom369": 814.69e9,
    "CzosneK": 795.31e9,
    "Ghoro": 724.29e9,
    "lllmundlll": 570.33e9,
    "Jackylefeu": 371.81e9,
    "Rendaxx": 365.56e9,
    "1RauMuong1": 332.59e9,
    "estimov": 327.67e9,
    "Rysor": 308.87e9,
    "Skytiti": 295.02e9,
    "saare": 273.99e9,
    "Maskiert03": 235.91e9,
    "REAPS": 208.30e9,
    "Stumbi97": 156.58e9,
    "Swidishh": 147.85e9,
    "Fergs": 144.64e9,  # not yet in roster -- see note above
    "IlTeino": 130.44e9,
    "Saludan": 122.93e9,
    "tEruPmA": 82.10e9,
    "xavop": 68.83e9,
    "Nad33m": 67.80e9,
    "Fredolay": 61.20e9,
    "AnyDockers": 31.77e9,
    "zozoxo": 23.45e9,
    # Not visible in the ranking (Mightykey, Murkchoppa, Tvojemama1,
    # Altair1165, Papykique, choolzy, Depfefferle336, Ekkehard,
    # EpicMarksman, NalaStomp) -- ranking list ended cleanly at rank 39
    # right above the pinned own-rank footer, so this is the true end of
    # the list, not a mid-scroll gap. Confirmed 0-attack call-out
    # candidates per the 9/2 policy.
}

# Friday 11/6 -- damage ranking (1-41 of 48) read off the scrollable
# Guild Member Ranking list; 7 screenshots this batch, no Manage Member
# screen, so donation values are still carried forward from the 10/4 full
# refresh (now well over five weeks stale). No new top-1 record
# (Pimpanzee 26.37T, below the season record of 27.45T from 10/15, but
# the closest any day has come since). "Fergs" appears again at rank 29
# (259.42B) -- fifth day running, still not added to
# roster/donation_members pending a Manage Member screenshot. The 8
# roster members missing from the ranking (Mightykey, Murkchoppa,
# Saludan, Papykique, choolzy, IlTeino, Ekkehard, RonickForce) -- ranking
# list ended cleanly at rank 41 right above the pinned own-rank footer,
# so this is the true end of the list, not a mid-scroll gap. Confirmed
# 0-attack call-out candidates per the 9/2 policy.
invasion_logged_fri = {
    "Pimpanzee": 26.37e12,
    "HyenA": 19.36e12,
    "EpicMarksman": 9.71e12,
    "Drew2264": 9.23e12,
    "Flforever": 7.46e12,
    "BenZoo": 5.34e12,
    "iBooneh": 4.90e12,
    "elementten": 3.15e12,
    "fred21422": 3.12e12,
    "1RauMuong1": 2.46e12,
    "NalaStomp": 2.21e12,
    "ScHlAnGE": 1.59e12,
    "REAPS": 1.18e12,
    "Drakias": 1.15e12,
    "Tvojemama1": 1.03e12,
    "Jackylefeu": 860.14e9,
    "Ibnt": 792.52e9,
    "Skytiti": 781.23e9,
    "Stumbi97": 722.14e9,
    "Maskiert03": 709.20e9,
    "Ghost192": 706.29e9,
    "P107215255": 654.47e9,
    "Atom369": 608.98e9,
    "estimov": 509.67e9,
    "saare": 344.89e9,
    "Rysor": 331.78e9,
    "BigRagaTheOppStopa": 328.81e9,
    "CzosneK": 296.05e9,
    "Fergs": 259.42e9,  # not yet in roster -- see note above
    "Ghoro": 227.69e9,
    "AnyDockers": 216.99e9,
    "xavop": 174.19e9,
    "tEruPmA": 165.14e9,
    "Altair1165": 164.65e9,
    "Depfefferle336": 105.68e9,
    "Rendaxx": 79.08e9,
    "lllmundlll": 77.50e9,
    "Fredolay": 57.41e9,
    "zozoxo": 50.76e9,
    "Swidishh": 37.90e9,
    "Nad33m": 24.70e9,
    # Not visible in the ranking (Mightykey, Murkchoppa, Saludan,
    # Papykique, choolzy, IlTeino, Ekkehard, RonickForce) -- ranking list
    # ended cleanly at rank 41 right above the pinned own-rank footer, so
    # this is the true end of the list, not a mid-scroll gap. Confirmed
    # 0-attack call-out candidates per the 9/2 policy.
}

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_DATES = ["11/2", "11/3", "11/4", "11/5", "11/6", "11/7", "11/8"]
DAY_FULL_LABELS = [f"{d} {dt}" for d, dt in zip(DAY_NAMES, DAY_DATES)]
DAY_LOGS = {2: invasion_logged_wed, 3: invasion_logged_thu, 4: invasion_logged_fri}
TRACKED_DAYS = sorted(DAY_LOGS.keys())
TODAY_INDEX = 4  # Friday -- the most recently tracked day
WEEK_LABEL = "wk of 11/2"

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
