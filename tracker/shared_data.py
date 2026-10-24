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
UPDATED_DATE = "Oct 23, 2026"


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
# New week: Mon 10/19 - Sun 10/25. Damage ranking (1-42 of 48) read off
# the scrollable Guild Member Ranking list; 7 screenshots this batch, no
# Manage Member screen, so donation values are carried forward unchanged
# from the 10/4 full refresh (now 15 days stale). Sunday 10/18 had no
# Shortcut upload, so it's left untracked rather than guessed -- this
# week opens straight from Saturday 10/17. No roster changes. The 6
# members missing from the ranking (Depfefferle336, choolzy, P107215255,
# Mightykey, Murkchoppa, zozoxo) -- ranking list ended cleanly at rank 42
# (xavop) right above the pinned own-rank footer, so this is the true end
# of the list, not a mid-scroll gap. Confirmed 0-attack call-out
# candidates per the 9/2 policy.
invasion_logged_mon = {
    "Pimpanzee": 23.64e12,
    "HyenA": 5.54e12,
    "Flforever": 4.18e12,
    "elementten": 3.61e12,
    "fred21422": 3.34e12,
    "EpicMarksman": 2.19e12,
    "RonickForce": 1.89e12,
    "Drew2264": 1.70e12,
    "Ibnt": 1.39e12,
    "iBooneh": 1.38e12,
    "BenZoo": 1.07e12,
    "Drakias": 1.05e12,
    "Ghost192": 712.97e9,
    "ScHlAnGE": 695.53e9,
    "Jackylefeu": 670.27e9,
    "NalaStomp": 628.50e9,
    "Saludan": 547.78e9,
    "Nad33m": 524.99e9,
    "Atom369": 466.06e9,
    "saare": 450.68e9,
    "REAPS": 402.16e9,
    "estimov": 368.46e9,
    "Ekkehard": 337.25e9,
    "IlTeino": 325.99e9,
    "lllmundlll": 267.89e9,
    "Rysor": 210.90e9,
    "Rendaxx": 182.42e9,
    "Ghoro": 177.36e9,
    "Papykique": 174.41e9,
    "Altair1165": 144.94e9,
    "tEruPmA": 143.10e9,
    "AnyDockers": 140.63e9,
    "1RauMuong1": 118.14e9,
    "Swidishh": 111.79e9,
    "Maskiert03": 73.54e9,
    "Stumbi97": 72.84e9,
    "Tvojemama1": 65.23e9,
    "BigRagaTheOppStopa": 50.92e9,
    "CzosneK": 44.46e9,
    "Skytiti": 33.55e9,
    "Fredolay": 19.03e9,
    "xavop": 18.46e9,
    # Not visible in the ranking (Depfefferle336, choolzy, P107215255,
    # Mightykey, Murkchoppa, zozoxo) -- unreached tail / true end of list,
    # confirmed 0-attack call-out candidates per the 9/2 policy.
}

# Tuesday 10/20 -- damage ranking (1-38 of 48) read off the scrollable
# Guild Member Ranking list; 6 screenshots this batch, no Manage Member
# screen, so donation values are still carried forward from the 10/4 full
# refresh (now over two weeks stale). No roster changes. elementten
# cracked the podium at #3. The 10 members missing from the ranking
# (choolzy, REAPS, Maskiert03, Atom369, Papykique, Skytiti,
# BigRagaTheOppStopa, Mightykey, Ghoro, Murkchoppa) -- ranking list ended
# cleanly at rank 38 (Fredolay) right above the pinned own-rank footer,
# so this is the true end of the list, not a mid-scroll gap. Confirmed
# 0-attack call-out candidates per the 9/2 policy.
invasion_logged_tue = {
    "Pimpanzee": 10.17e12,
    "HyenA": 7.63e12,
    "elementten": 6.34e12,
    "Flforever": 4.93e12,
    "Drew2264": 4.64e12,
    "fred21422": 4.38e12,
    "P107215255": 2.61e12,
    "BenZoo": 2.55e12,
    "EpicMarksman": 1.05e12,
    "Rysor": 846.08e9,
    "Drakias": 735.86e9,
    "ScHlAnGE": 709.94e9,
    "NalaStomp": 653.31e9,
    "Ghost192": 602.48e9,
    "Ibnt": 562.83e9,
    "RonickForce": 531.86e9,
    "Ekkehard": 483.39e9,
    "CzosneK": 409.33e9,
    "saare": 358.06e9,
    "AnyDockers": 317.02e9,
    "iBooneh": 277.87e9,
    "Altair1165": 272.45e9,
    "Stumbi97": 259.34e9,
    "Saludan": 242.29e9,
    "estimov": 216.27e9,
    "lllmundlll": 212.37e9,
    "IlTeino": 205.13e9,
    "tEruPmA": 189.26e9,
    "1RauMuong1": 173.80e9,
    "Rendaxx": 151.90e9,
    "xavop": 139.71e9,
    "Jackylefeu": 135.36e9,
    "Nad33m": 111.80e9,
    "zozoxo": 110.91e9,
    "Depfefferle336": 76.98e9,
    "Swidishh": 66.61e9,
    "Tvojemama1": 32.41e9,
    "Fredolay": 12.62e9,
    # Not visible in the ranking (choolzy, REAPS, Maskiert03, Atom369,
    # Papykique, Skytiti, BigRagaTheOppStopa, Mightykey, Ghoro,
    # Murkchoppa) -- ranking list ended cleanly at rank 38 right above the
    # pinned own-rank footer, so this is the true end of the list, not a
    # mid-scroll gap. Confirmed 0-attack call-out candidates per the 9/2
    # policy.
}

# Wednesday 10/21 -- damage ranking (1-39 of 48) read off the scrollable
# Guild Member Ranking list; 6 screenshots this batch, no Manage Member
# screen, so donation values are still carried forward from the 10/4 full
# refresh (now well over two weeks stale). No roster changes. The 9
# members missing from the ranking (choolzy, Depfefferle336, Papykique,
# Altair1165, iBooneh, IlTeino, Mightykey, Murkchoppa, Atom369) --
# ranking list ended cleanly at rank 39 (Fredolay) right above the pinned
# own-rank footer, so this is the true end of the list, not a mid-scroll
# gap. Confirmed 0-attack call-out candidates per the 9/2 policy.
invasion_logged_wed = {
    "Pimpanzee": 8.05e12,
    "Drew2264": 8.00e12,
    "EpicMarksman": 7.04e12,
    "RonickForce": 5.85e12,
    "HyenA": 4.38e12,
    "P107215255": 4.25e12,
    "Flforever": 3.66e12,
    "fred21422": 3.62e12,
    "elementten": 1.66e12,
    "ScHlAnGE": 1.63e12,
    "Ibnt": 1.21e12,
    "BenZoo": 1.08e12,
    "Rysor": 967.31e9,
    "NalaStomp": 958.16e9,
    "1RauMuong1": 742.09e9,
    "Ekkehard": 718.25e9,
    "BigRagaTheOppStopa": 715.98e9,
    "Drakias": 673.17e9,
    "Skytiti": 580.58e9,
    "saare": 553.48e9,
    "Stumbi97": 527.54e9,
    "Saludan": 390.96e9,
    "Maskiert03": 379.58e9,
    "Jackylefeu": 305.38e9,
    "CzosneK": 270.98e9,
    "Ghoro": 256.85e9,
    "Ghost192": 217.91e9,
    "REAPS": 196.36e9,
    "AnyDockers": 124.13e9,
    "lllmundlll": 112.44e9,
    "Rendaxx": 102.91e9,
    "Nad33m": 56.89e9,
    "tEruPmA": 31.14e9,
    "estimov": 30.91e9,
    "Swidishh": 26.34e9,
    "xavop": 22.52e9,
    "zozoxo": 17.97e9,
    "Tvojemama1": 8.25e9,
    "Fredolay": 5.76e9,
    # Not visible in the ranking (choolzy, Depfefferle336, Papykique,
    # Altair1165, iBooneh, IlTeino, Mightykey, Murkchoppa, Atom369) --
    # ranking list ended cleanly at rank 39 right above the pinned
    # own-rank footer, so this is the true end of the list, not a
    # mid-scroll gap. Confirmed 0-attack call-out candidates per the 9/2
    # policy.
}

# Thursday 10/22 -- no Shortcut upload came in at all, so there's no data
# to log for this day. Deliberately left untracked (no
# invasion_logged_thu dict, no entry in DAY_LOGS) rather than guessed or
# backfilled.

# Friday 10/23 -- damage ranking (1-42 of 48) read off the scrollable
# Guild Member Ranking list; 7 screenshots this batch, no Manage Member
# screen, so donation values are still carried forward from the 10/4 full
# refresh (now nearly three weeks stale). No roster changes. The 6
# members missing from the ranking (choolzy, AnyDockers, Tvojemama1,
# Altair1165, Mightykey, Murkchoppa) -- ranking list ended cleanly at
# rank 42 (Swidishh) right above the pinned own-rank footer, so this is
# the true end of the list, not a mid-scroll gap. Confirmed 0-attack
# call-out candidates per the 9/2 policy.
invasion_logged_fri = {
    "Pimpanzee": 17.28e12,
    "HyenA": 13.90e12,
    "Drew2264": 11.35e12,
    "elementten": 10.54e12,
    "Flforever": 8.47e12,
    "EpicMarksman": 8.39e12,
    "BenZoo": 5.89e12,
    "fred21422": 2.93e12,
    "Ghost192": 2.80e12,
    "P107215255": 2.30e12,
    "NalaStomp": 1.58e12,
    "iBooneh": 1.46e12,
    "Ibnt": 1.23e12,
    "Atom369": 1.18e12,
    "Drakias": 766.43e9,
    "BigRagaTheOppStopa": 743.66e9,
    "ScHlAnGE": 678.39e9,
    "RonickForce": 621.77e9,
    "REAPS": 394.96e9,
    "CzosneK": 358.19e9,
    "Ekkehard": 334.08e9,
    "IlTeino": 316.72e9,
    "Skytiti": 294.70e9,
    "saare": 273.02e9,
    "Saludan": 243.80e9,
    "Papykique": 222.95e9,
    "tEruPmA": 207.39e9,
    "Rysor": 204.10e9,
    "1RauMuong1": 195.38e9,
    "estimov": 167.67e9,
    "Stumbi97": 133.79e9,
    "lllmundlll": 123.67e9,
    "Jackylefeu": 106.20e9,
    "Rendaxx": 77.50e9,
    "Ghoro": 58.80e9,
    "Maskiert03": 52.42e9,
    "xavop": 38.84e9,
    "Depfefferle336": 25.67e9,
    "Nad33m": 23.79e9,
    "Fredolay": 22.55e9,
    "zozoxo": 12.63e9,
    "Swidishh": 11.43e9,
    # Not visible in the ranking (choolzy, AnyDockers, Tvojemama1,
    # Altair1165, Mightykey, Murkchoppa) -- ranking list ended cleanly at
    # rank 42 right above the pinned own-rank footer, so this is the true
    # end of the list, not a mid-scroll gap. Confirmed 0-attack call-out
    # candidates per the 9/2 policy.
}

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_DATES = ["10/19", "10/20", "10/21", "10/22", "10/23", "10/24", "10/25"]
DAY_FULL_LABELS = [f"{d} {dt}" for d, dt in zip(DAY_NAMES, DAY_DATES)]
DAY_LOGS = {0: invasion_logged_mon, 1: invasion_logged_tue, 2: invasion_logged_wed, 4: invasion_logged_fri}
TRACKED_DAYS = sorted(DAY_LOGS.keys())
TODAY_INDEX = 4  # Friday -- the most recently tracked day (Thursday 10/22 has no data, no upload came in)
WEEK_LABEL = "wk of 10/19"

# Roster unchanged. Donation values still carried forward from the 10/4
# full refresh -- no Manage Member screenshot came in with this batch
# (now 15 days stale).
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
