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
UPDATED_DATE = "Nov 11, 2026"


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
# New week: Mon 11/9 - Sun 11/15. Damage ranking (1-39 of 48) read off
# the scrollable Guild Member Ranking list; 6 screenshots this batch, no
# Manage Member screen, so donation values are still carried forward
# from the 10/4 full refresh (now well over five weeks stale). No new
# top-1 record (Pimpanzee 26.42T, below the season record of 27.45T from
# 10/15, but close). "Fergs" does NOT appear in this batch -- breaking
# the streak of appearances every day since 10/29. Since they were never
# added to the official roster, this isn't flagged as a 0-attack
# situation for them; no action needed. The 9 roster members missing
# from the ranking (Mightykey, Murkchoppa, Altair1165, lllmundlll,
# Saludan, Papykique, choolzy, Maskiert03, AnyDockers) -- ranking list
# ended cleanly at rank 39 right above the pinned own-rank footer, so
# this is the true end of the list, not a mid-scroll gap. Confirmed
# 0-attack call-out candidates per the 9/2 policy.
invasion_logged_mon = {
    "Pimpanzee": 26.42e12,
    "EpicMarksman": 7.72e12,
    "BenZoo": 6.39e12,
    "elementten": 5.24e12,
    "Drew2264": 4.85e12,
    "iBooneh": 4.57e12,
    "HyenA": 4.15e12,
    "fred21422": 4.14e12,
    "Ghost192": 3.97e12,
    "Flforever": 3.26e12,
    "P107215255": 3.22e12,
    "Atom369": 2.20e12,
    "RonickForce": 2.19e12,
    "Tvojemama1": 1.80e12,
    "BigRagaTheOppStopa": 1.15e12,
    "Drakias": 966.66e9,
    "1RauMuong1": 790.84e9,
    "Ibnt": 693.79e9,
    "Stumbi97": 520.25e9,
    "estimov": 410.39e9,
    "Ekkehard": 378.11e9,
    "Rendaxx": 328.24e9,
    "saare": 313.53e9,
    "Jackylefeu": 309.42e9,
    "NalaStomp": 280.72e9,
    "REAPS": 279.42e9,
    "Skytiti": 261.81e9,
    "IlTeino": 213.92e9,
    "Ghoro": 170.66e9,
    "ScHlAnGE": 155.20e9,
    "Rysor": 107.50e9,
    "tEruPmA": 81.19e9,
    "Nad33m": 56.13e9,
    "Swidishh": 54.78e9,
    "zozoxo": 54.14e9,
    "CzosneK": 46.03e9,
    "Fredolay": 27.58e9,
    "xavop": 21.96e9,
    "Depfefferle336": 20.44e9,
    # Not visible in the ranking (Mightykey, Murkchoppa, Altair1165,
    # lllmundlll, Saludan, Papykique, choolzy, Maskiert03, AnyDockers) --
    # ranking list ended cleanly at rank 39 right above the pinned
    # own-rank footer, so this is the true end of the list, not a
    # mid-scroll gap. Confirmed 0-attack call-out candidates per the 9/2
    # policy.
}

# Tuesday 11/10 -- damage ranking (1-39 of 48) read off the scrollable
# Guild Member Ranking list; 6 screenshots this batch, no Manage Member
# screen, so donation values are still carried forward from the 10/4
# full refresh (now well over five weeks stale). No new top-1 record
# (Pimpanzee 26.40T, below the season record of 27.45T from 10/15).
# "Fergs" is back at rank 29 (164.65B) after a one-day absence on 11/9 --
# still not added to roster/donation_members pending a Manage Member
# screenshot. The 10 roster members missing from the ranking (Mightykey,
# Murkchoppa, lllmundlll, P107215255, Atom369, Fredolay, Ghost192,
# Papykique, choolzy, Ekkehard) -- ranking list ended cleanly at rank 39
# right above the pinned own-rank footer, so this is the true end of the
# list, not a mid-scroll gap. Confirmed 0-attack call-out candidates per
# the 9/2 policy.
invasion_logged_tue = {
    "Pimpanzee": 26.40e12,
    "iBooneh": 9.86e12,
    "EpicMarksman": 8.90e12,
    "Flforever": 4.34e12,
    "HyenA": 4.18e12,
    "BenZoo": 3.44e12,
    "Drew2264": 3.33e12,
    "elementten": 2.39e12,
    "fred21422": 1.97e12,
    "RonickForce": 1.82e12,
    "REAPS": 1.71e12,
    "BigRagaTheOppStopa": 1.56e12,
    "Saludan": 1.08e12,
    "Ibnt": 912.26e9,
    "Tvojemama1": 831.94e9,
    "NalaStomp": 778.05e9,
    "Drakias": 736.41e9,
    "1RauMuong1": 581.78e9,
    "Maskiert03": 553.96e9,
    "ScHlAnGE": 371.29e9,
    "saare": 330.29e9,
    "Stumbi97": 318.22e9,
    "estimov": 298.20e9,
    "Rysor": 290.80e9,
    "tEruPmA": 253.58e9,
    "Rendaxx": 233.19e9,
    "Ghoro": 200.65e9,
    "Depfefferle336": 177.49e9,
    "Fergs": 164.65e9,  # not yet in roster -- see note above
    "Altair1165": 140.58e9,
    "AnyDockers": 132.84e9,
    "IlTeino": 123.13e9,
    "Jackylefeu": 120.21e9,
    "xavop": 104.72e9,
    "Skytiti": 69.49e9,
    "Swidishh": 53.99e9,
    "CzosneK": 42.71e9,
    "zozoxo": 42.35e9,
    "Nad33m": 41.53e9,
    # Not visible in the ranking (Mightykey, Murkchoppa, lllmundlll,
    # P107215255, Atom369, Fredolay, Ghost192, Papykique, choolzy,
    # Ekkehard) -- ranking list ended cleanly at rank 39 right above the
    # pinned own-rank footer, so this is the true end of the list, not a
    # mid-scroll gap. Confirmed 0-attack call-out candidates per the 9/2
    # policy.
}

# Wednesday 11/11 -- damage ranking (1-38 of 48) read off the scrollable
# Guild Member Ranking list; 6 screenshots this batch, no Manage Member
# screen, so donation values are still carried forward from the 10/4
# full refresh (now well over five weeks stale). NEW SEASON RECORD:
# Pimpanzee 33.07T, smashing the prior record of 27.45T set on 10/15 by
# a wide margin. Fergs still appears (rank 28, 102.16B), still not added
# to roster/donation_members pending a Manage Member screenshot. The 11
# roster members missing from the ranking (Mightykey, Murkchoppa,
# Skytiti, Altair1165, P107215255, Saludan, Ghost192, Papykique,
# choolzy, Stumbi97, REAPS) -- ranking list ended cleanly at rank 38
# right above the pinned own-rank footer, so this is the true end of the
# list, not a mid-scroll gap. Confirmed 0-attack call-out candidates per
# the 9/2 policy.
invasion_logged_wed = {
    "Pimpanzee": 33.07e12,
    "EpicMarksman": 12.82e12,
    "iBooneh": 5.09e12,
    "Flforever": 5.08e12,
    "Drew2264": 4.68e12,
    "BenZoo": 4.37e12,
    "RonickForce": 3.66e12,
    "HyenA": 3.41e12,
    "elementten": 3.24e12,
    "fred21422": 2.18e12,
    "ScHlAnGE": 1.62e12,
    "NalaStomp": 1.08e12,
    "Ibnt": 1.04e12,
    "BigRagaTheOppStopa": 842.72e9,
    "Atom369": 765.98e9,
    "IlTeino": 658.17e9,
    "Rysor": 648.98e9,
    "Ghoro": 481.11e9,
    "Drakias": 449.69e9,
    "Tvojemama1": 355.40e9,
    "lllmundlll": 325.58e9,
    "Maskiert03": 321.07e9,
    "Ekkehard": 310.30e9,
    "estimov": 270.94e9,
    "Jackylefeu": 163.44e9,
    "1RauMuong1": 147.09e9,
    "saare": 103.33e9,
    "Fergs": 102.16e9,  # not yet in roster -- see note above
    "Rendaxx": 97.73e9,
    "Swidishh": 70.91e9,
    "Depfefferle336": 64.03e9,
    "tEruPmA": 38.23e9,
    "Nad33m": 29.13e9,
    "xavop": 27.73e9,
    "CzosneK": 17.53e9,
    "AnyDockers": 13.09e9,
    "zozoxo": 12.82e9,
    "Fredolay": 11.22e9,
    # Not visible in the ranking (Mightykey, Murkchoppa, Skytiti,
    # Altair1165, P107215255, Saludan, Ghost192, Papykique, choolzy,
    # Stumbi97, REAPS) -- ranking list ended cleanly at rank 38 right
    # above the pinned own-rank footer, so this is the true end of the
    # list, not a mid-scroll gap. Confirmed 0-attack call-out candidates
    # per the 9/2 policy.
}

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_DATES = ["11/9", "11/10", "11/11", "11/12", "11/13", "11/14", "11/15"]
DAY_FULL_LABELS = [f"{d} {dt}" for d, dt in zip(DAY_NAMES, DAY_DATES)]
DAY_LOGS = {0: invasion_logged_mon, 1: invasion_logged_tue, 2: invasion_logged_wed}
TRACKED_DAYS = sorted(DAY_LOGS.keys())
TODAY_INDEX = 2  # Wednesday -- the most recently tracked day
WEEK_LABEL = "wk of 11/9"

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
    0: {name: ((2, 2) if name in invasion_logged_mon else (0, 0)) for name, role in roster},
    1: {name: ((2, 2) if name in invasion_logged_tue else (0, 0)) for name, role in roster},
    2: {name: ((2, 2) if name in invasion_logged_wed else (0, 0)) for name, role in roster},
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
