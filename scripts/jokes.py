"""Rotating joke bank for the daily Discord post.

Two categories of one-liner, each templated with {name} and (for the top
performer) {value}. Selection is deterministic per calendar date (via a hash
of the date string), so the same day always picks the same joke if the
workflow reruns, but consecutive days land on different lines without
needing any stored state.

Usage:
    from jokes import pick_top_performer_joke, pick_zero_attack_joke
    line = pick_top_performer_joke("2026-08-12", name="Pimpanzee", value="4.82T")
    line = pick_zero_attack_joke("2026-08-12", name="RESIIK")
"""

import hashlib

TOP_PERFORMER_JOKES = [
    "🏆 {name} really said 'let me delete this boss' — {value} damage today. Absolute unit, put him on a stamp.",
    "🏆 {name} out here doing {value} damage like it's a warmup set. Big. Strong. Handsome. Ripped (probably).",
    "🏆 Ladies and gentlemen, {name} — {value} damage and not even out of breath. National treasure.",
    "🏆 {name} hit the boss for {value} and it immediately filed for early retirement. Absolute chad.",
    "🏆 {name} pulled {value} damage today. Certified hunk. Certified menace. Certified MVP.",
    "🏆 Scientists are studying {name}'s {value}-damage run to figure out how someone can be this strong AND this good-looking.",
    "🏆 {name} carried the guild today with {value} damage. Somebody get this man a cape (and a mirror, because damn).",
    "🏆 Breaking: local legend {name} does {value} damage, still finds time to be devastatingly handsome. Unfair, honestly.",
]

ZERO_ATTACK_JOKES = [
    "👻 {name} — 0/4 attacks this week. Are you okay? Blink twice if the boss has taken you hostage.",
    "👻 Missing persons report: {name}, last seen not attacking anything, 0/4 this week. If found, please return to guild duty.",
    "👻 {name} is currently 0/4 on attacks. We checked — the boss is still there. It's not going anywhere. Might wanna go say hi.",
    "👻 {name} has entered witness protection apparently — 0/4 attacks this week. We know nothing. We saw nothing.",
    "👻 PSA: {name}'s phone has not left airplane mode in days. 0/4 attacks. Rescue mission pending.",
    "👻 {name} is 0/4 this week, which means technically they've done more napping than damage. Impressive in its own way.",
    "👻 Somebody check on {name} — 0/4 attacks. Either deep in a boss battle IRL or just very committed to the bit.",
    "👻 {name}: 0/4 attacks. At this point the boss owes YOU rent for squatting on your invasion slot.",
]


def _seeded_index(seed: str, length: int) -> int:
    digest = hashlib.sha256(seed.encode()).hexdigest()
    return int(digest, 16) % length


def pick_top_performer_joke(date_str: str, name: str, value: str) -> str:
    line = TOP_PERFORMER_JOKES[_seeded_index(date_str + ":top", len(TOP_PERFORMER_JOKES))]
    return line.format(name=name, value=value)


def pick_zero_attack_joke(date_str: str, name: str) -> str:
    line = ZERO_ATTACK_JOKES[_seeded_index(date_str + ":zero", len(ZERO_ATTACK_JOKES))]
    return line.format(name=name)
