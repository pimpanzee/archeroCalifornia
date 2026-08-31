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
UPDATED_DATE = "Aug 30, 2026"


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

# Wednesday 8/26 -- only 6 screenshots came in this batch (fewer than the
# usual 7-8), so the damage ranking has TWO kinds of gaps: a genuine
# mid-scroll skip (ranks 14-20, 7 members, sandwiched between confirmed
# rank 13 at 352.41B and rank 21 at 212.78B -- they almost certainly did
# have damage, we just don't have the numbers) and an unreached tail
# (ranks 45-48, never scrolled to). No attack-count/donation screens
# either. Rather than guess at either group's values, all 11 missing
# members are left out of the dict entirely and treated as unconfirmed
# (0, 0) attacks -- NOT assumed 0-attack or 0-damage, just unknown.
invasion_logged_wed = {
    "RonickForce": 6.66e12,
    "Pimpanzee": 5.95e12,
    "Flforever": 3.33e12,
    "HyenA": 3.12e12,
    "Drew2264": 2.16e12,
    "fred21422": 1.08e12,
    "BenZoo": 1.04e12,
    "ScHlAnGE": 740.47e9,
    "Papykique": 549.40e9,
    "Altair1165": 417.23e9,
    "Nad33m": 399.01e9,
    "NHTPhat": 388.88e9,
    "P107215255": 352.41e9,
    "Atom369": 212.78e9,
    "tEruPmA": 207.69e9,
    "Ghost192": 179.40e9,
    "SpudNugget18": 162.10e9,
    "REAPS": 141.94e9,
    "1RauMuong1": 103.20e9,
    "Ibnt": 99.76e9,
    "IlTeino": 92.31e9,
    "NalaStomp": 82.73e9,
    "zozoxo": 69.28e9,
    "Tvojemama1": 68.54e9,
    "Saludan": 66.73e9,
    "Skytiti": 66.54e9,
    "Stumbi97": 52.43e9,
    "Rysor": 50.66e9,
    "Swidishh": 36.85e9,
    "choolzy": 34.36e9,
    "Vomenjack": 29.99e9,
    "Katitos": 25.66e9,
    "estimov": 21.93e9,
    "Rendaxx": 18.31e9,
    "Jackylefeu": 12.15e9,
    "Mightykey": 7.11e9,
    "xavop": 6.83e9,
    # Unconfirmed (mid-scroll gap, ranks 14-20): AnyDockers, BigRagaTheOppStopa,
    # Fredolay, Ekkehard, Drakias, saare, Murkchoppa. Unconfirmed (unreached
    # tail, ranks 45-48): Maskiert03, iBooneh, elementten, DKDKDKDK.
}

# Thursday 8/27 -- full damage ranking (1-41 of 48), read off the scrollable
# Guild Member Ranking list. No attack-count/donation screens came in this
# batch either. The 7 members missing from the ranking (Saludan, zozoxo,
# Atom369, Mightykey, NalaStomp, Vomenjack, Murkchoppa) are left out of the
# dict and treated as unconfirmed (0, 0) attacks, not assumed 0-attack.
invasion_logged_thu = {
    "HyenA": 5.56e12,
    "elementten": 5.48e12,
    "Flforever": 5.47e12,
    "Pimpanzee": 4.17e12,
    "Drew2264": 3.50e12,
    "RonickForce": 3.12e12,
    "NHTPhat": 3.03e12,
    "BenZoo": 1.82e12,
    "REAPS": 1.14e12,
    "Altair1165": 1.02e12,
    "fred21422": 1.02e12,
    "P107215255": 949.71e9,
    "Nad33m": 632.91e9,
    "ScHlAnGE": 519.26e9,
    "Papykique": 484.44e9,
    "Tvojemama1": 463.68e9,
    "Ekkehard": 463.24e9,
    "Stumbi97": 422.90e9,
    "DKDKDKDK": 405.06e9,
    "Ghost192": 399.00e9,
    "1RauMuong1": 353.19e9,
    "iBooneh": 347.60e9,
    "Drakias": 311.82e9,
    "SpudNugget18": 280.36e9,
    "Jackylefeu": 220.76e9,
    "BigRagaTheOppStopa": 215.93e9,
    "Ibnt": 189.17e9,
    "tEruPmA": 140.59e9,
    "estimov": 111.71e9,
    "Rysor": 96.09e9,
    "Maskiert03": 71.29e9,
    "IlTeino": 54.90e9,
    "AnyDockers": 53.62e9,
    "Skytiti": 42.04e9,
    "Rendaxx": 40.64e9,
    "Katitos": 38.20e9,
    "saare": 36.55e9,
    "Swidishh": 32.58e9,
    "choolzy": 16.13e9,
    "Fredolay": 10.67e9,
    "xavop": 3.33e9,
}

# Friday 8/28 -- damage ranking (1-39 of 48), read off the scrollable Guild
# Member Ranking list. No tail (ranks 40-48) reached, and no attack-count/
# donation screens came in either. Backfilled the same way as recent days:
# presence in the ranking treated as a confirmed 2/2, absence as an
# unconfirmed 0/0 (not penalized). Donation values still carried forward
# from 8/18.
invasion_logged_fri = {
    "Drew2264": 6.15e12,
    "elementten": 5.38e12,
    "HyenA": 3.82e12,
    "Pimpanzee": 3.62e12,
    "RonickForce": 3.27e12,
    "fred21422": 2.06e12,
    "Flforever": 1.83e12,
    "Papykique": 1.38e12,
    "BenZoo": 1.28e12,
    "NHTPhat": 1.22e12,
    "REAPS": 1.03e12,
    "P107215255": 506.77e9,
    "Altair1165": 455.61e9,
    "Drakias": 425.48e9,
    "Saludan": 337.25e9,
    "1RauMuong1": 275.91e9,
    "Tvojemama1": 223.82e9,
    "Jackylefeu": 203.13e9,
    "NalaStomp": 202.42e9,
    "Rysor": 195.26e9,
    "Nad33m": 191.97e9,
    "ScHlAnGE": 177.75e9,
    "Katitos": 168.74e9,
    "DKDKDKDK": 163.44e9,
    "tEruPmA": 153.37e9,
    "Rendaxx": 152.82e9,
    "SpudNugget18": 125.33e9,
    "Skytiti": 113.76e9,
    "Ibnt": 84.28e9,
    "saare": 51.23e9,
    "estimov": 44.71e9,
    "Ghost192": 42.89e9,
    "IlTeino": 35.21e9,
    "choolzy": 33.05e9,
    "Atom369": 32.29e9,
    "Swidishh": 18.38e9,
    "Maskiert03": 16.42e9,
    "xavop": 8.92e9,
    "Mightykey": 5.07e9,
    # Not visible in the scrolled ranking (zozoxo, AnyDockers,
    # BigRagaTheOppStopa, Fredolay, Stumbi97, Vomenjack, Ekkehard, Murkchoppa,
    # iBooneh) -- no attack-count screen today to confirm either way, so
    # these are NOT treated as 0-attack call-out candidates.
}

# Saturday 8/29 -- full clean read of the Guild Member Ranking list (1-44
# of 48) AND, for the first time in several days, real Manage Member /
# donation screens covering all 48 members. The 4 members missing from the
# ranking (Ekkehard, Papykique, Ghost192, 1RauMuong1) exactly match the 4
# who show 0 attacks on the Manage Member screens -- full cross-validation.
invasion_logged_sat = {
    "Drew2264": 5.79e12,
    "elementten": 3.92e12,
    "HyenA": 2.97e12,
    "RonickForce": 2.39e12,
    "Flforever": 1.78e12,
    "fred21422": 1.64e12,
    "BenZoo": 832.78e9,
    "ScHlAnGE": 812.19e9,
    "Pimpanzee": 756.65e9,
    "Nad33m": 591.50e9,
    "REAPS": 347.04e9,
    "DKDKDKDK": 311.69e9,
    "Drakias": 288.18e9,
    "Murkchoppa": 255.80e9,
    "NHTPhat": 255.14e9,
    "IlTeino": 247.85e9,
    "iBooneh": 232.51e9,
    "Saludan": 224.74e9,
    "Altair1165": 223.06e9,
    "Stumbi97": 219.48e9,
    "Tvojemama1": 212.64e9,
    "Skytiti": 210.79e9,
    "SpudNugget18": 182.32e9,
    "P107215255": 158.69e9,
    "saare": 147.31e9,
    "tEruPmA": 146.82e9,
    "BigRagaTheOppStopa": 142.94e9,
    "NalaStomp": 125.78e9,
    "Atom369": 92.10e9,
    "Ibnt": 91.36e9,
    "Rendaxx": 70.22e9,
    "AnyDockers": 56.53e9,
    "choolzy": 43.82e9,
    "Jackylefeu": 38.69e9,
    "Katitos": 30.58e9,
    "Maskiert03": 30.02e9,
    "Rysor": 21.62e9,
    "Vomenjack": 11.95e9,
    "Swidishh": 6.54e9,
    "zozoxo": 6.13e9,
    "estimov": 5.45e9,
    "xavop": 4.88e9,
    "Mightykey": 4.86e9,
    "Fredolay": 3.86e9,
    # Not visible in the ranking (Ekkehard, Papykique, Ghost192, 1RauMuong1)
    # -- confirmed 0 attacks for the day (see ATTACKS_SAT).
}

# Attack count (out of a max of 2/day) for Saturday 8/29, read off the red
# skull icon on the Manage Member / donation screens -- real data for all
# 48 members, first full attack-screen batch since 8/21.
ATTACKS_SAT = {
    "Maskiert03": 2, "zozoxo": 2, "Flforever": 2, "ScHlAnGE": 2,
    "Vomenjack": 2, "Swidishh": 2, "Katitos": 2, "Jackylefeu": 2,
    "Mightykey": 2, "Nad33m": 2, "Ekkehard": 0, "Altair1165": 2,
    "REAPS": 2, "Stumbi97": 2, "NalaStomp": 2, "fred21422": 2, "Rysor": 2,
    "IlTeino": 2, "Tvojemama1": 2, "Papykique": 0, "Saludan": 2,
    "AnyDockers": 2, "estimov": 2, "Rendaxx": 2, "P107215255": 2,
    "Fredolay": 1, "xavop": 1, "BenZoo": 2, "BigRagaTheOppStopa": 2,
    "Ibnt": 2, "choolzy": 2, "tEruPmA": 2, "Skytiti": 2, "Atom369": 2,
    "RonickForce": 2, "Drew2264": 2, "saare": 2, "DKDKDKDK": 2, "HyenA": 2,
    "iBooneh": 2, "Murkchoppa": 2, "Pimpanzee": 2, "elementten": 2,
    "SpudNugget18": 2, "NHTPhat": 2, "Drakias": 2, "Ghost192": 0,
    "1RauMuong1": 0,
}

# Sunday 8/30 -- second full clean read in a row: damage ranking (1-44 of
# 48) plus real Manage Member / donation screens for all 48 members. The 4
# members missing from the ranking (Stumbi97, Skytiti, Saludan, Mightykey)
# exactly match the 4 confirmed 0-attack members again -- another clean
# cross-validation. This closes out the week (Mon 8/24 - Sun 8/30).
invasion_logged_sun = {
    "fred21422": 2.63e12,
    "HyenA": 2.59e12,
    "Pimpanzee": 2.17e12,
    "RonickForce": 1.95e12,
    "Flforever": 1.64e12,
    "elementten": 1.37e12,
    "Drew2264": 368.46e9,
    "Papykique": 276.83e9,
    "Tvojemama1": 244.10e9,
    "Drakias": 234.09e9,
    "Ekkehard": 223.26e9,
    "DKDKDKDK": 215.61e9,
    "Nad33m": 122.20e9,
    "BigRagaTheOppStopa": 112.67e9,
    "tEruPmA": 109.70e9,
    "AnyDockers": 102.86e9,
    "ScHlAnGE": 100.50e9,
    "Altair1165": 94.30e9,
    "REAPS": 93.87e9,
    "NalaStomp": 85.61e9,
    "P107215255": 80.98e9,
    "1RauMuong1": 75.67e9,
    "BenZoo": 69.66e9,
    "SpudNugget18": 60.86e9,
    "Ibnt": 52.53e9,
    "saare": 51.04e9,
    "NHTPhat": 49.63e9,
    "iBooneh": 48.81e9,
    "Jackylefeu": 33.10e9,
    "Rendaxx": 32.51e9,
    "Rysor": 31.57e9,
    "IlTeino": 30.23e9,
    "Ghost192": 27.66e9,
    "choolzy": 24.55e9,
    "Murkchoppa": 20.66e9,
    "Swidishh": 17.41e9,
    "Atom369": 17.01e9,
    "Vomenjack": 13.48e9,
    "Katitos": 12.67e9,
    "estimov": 11.95e9,
    "Maskiert03": 11.49e9,
    "Fredolay": 7.57e9,
    "zozoxo": 5.89e9,
    "xavop": 1.66e9,
    # Not visible in the ranking (Stumbi97, Skytiti, Saludan, Mightykey) --
    # confirmed 0 attacks for the day (see ATTACKS_SUN).
}

# Attack count (out of a max of 2/day) for Sunday 8/30, read off the red
# skull icon on the Manage Member / donation screens -- real data for all
# 48 members.
ATTACKS_SUN = {
    "Altair1165": 2, "Katitos": 2, "Stumbi97": 0, "ScHlAnGE": 2, "REAPS": 2,
    "Saludan": 0, "Mightykey": 0, "Ekkehard": 2, "Swidishh": 2,
    "Tvojemama1": 1, "Papykique": 2, "zozoxo": 2, "xavop": 1, "NalaStomp": 2,
    "Ibnt": 2, "estimov": 2, "IlTeino": 2, "AnyDockers": 2, "Vomenjack": 2,
    "Jackylefeu": 2, "Nad33m": 2, "Rysor": 2, "tEruPmA": 2, "choolzy": 2,
    "Maskiert03": 2, "SpudNugget18": 2, "Skytiti": 0, "P107215255": 2,
    "iBooneh": 2, "saare": 2, "Murkchoppa": 1, "Fredolay": 1, "Ghost192": 2,
    "Drakias": 2, "Rendaxx": 2, "elementten": 2, "RonickForce": 2,
    "1RauMuong1": 2, "Drew2264": 2, "HyenA": 2, "BenZoo": 2, "Pimpanzee": 2,
    "DKDKDKDK": 2, "Flforever": 2, "BigRagaTheOppStopa": 2, "NHTPhat": 1,
    "fred21422": 2, "Atom369": 2,
}

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_DATES = ["8/24", "8/25", "8/26", "8/27", "8/28", "8/29", "8/30"]
DAY_FULL_LABELS = [f"{d} {dt}" for d, dt in zip(DAY_NAMES, DAY_DATES)]
DAY_LOGS = {0: invasion_logged_mon, 1: invasion_logged_tue, 2: invasion_logged_wed, 3: invasion_logged_thu, 4: invasion_logged_fri, 5: invasion_logged_sat, 6: invasion_logged_sun}
TRACKED_DAYS = sorted(DAY_LOGS.keys())
TODAY_INDEX = 6  # Sunday -- the most recently tracked day, closes out wk of 8/24
WEEK_LABEL = "wk of 8/24"

# Roster unchanged. Donation values refreshed from the 8/30 Manage Member
# screens -- second day in a row with a fresh read (previous refresh was
# 8/29, first since 8/18).
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

# Attack counts as (attacks, max) pairs per tracked day. No attack-count
# screen this week yet, so backfilled the same way as recent no-screenshot
# days: presence in the ranking treated as a confirmed 2/2, absence as an
# unconfirmed 0/0 (not penalized).
ATTACK_LOGS = {
    0: {name: ((2, 2) if name in invasion_logged_mon else (0, 0)) for name, role in roster},
    1: {name: ((2, 2) if name in invasion_logged_tue else (0, 0)) for name, role in roster},
    2: {name: ((2, 2) if name in invasion_logged_wed else (0, 0)) for name, role in roster},
    3: {name: ((2, 2) if name in invasion_logged_thu else (0, 0)) for name, role in roster},
    4: {name: ((2, 2) if name in invasion_logged_fri else (0, 0)) for name, role in roster},
    5: {name: (ATTACKS_SAT.get(name, 0), 2) for name, role in roster},
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
