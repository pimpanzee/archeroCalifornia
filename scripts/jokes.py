"""Rotating joke bank for the daily Discord post.

Two categories of one-liner, each templated with {name} and (for the top
performer) {value}. Written in the voice of a slick California-governor type
giving a press conference, since the guild is named "california" — confident,
a little self-congratulatory, always framing things as leadership and results.

Selection is deterministic per calendar date (via a hash of the date
string), so the same day always picks the same joke if the workflow reruns,
but consecutive days land on different lines without needing any stored
state.

Usage:
    from jokes import pick_top_performer_joke, pick_zero_attack_joke
    line = pick_top_performer_joke("2026-08-12", name="Pimpanzee", value="4.82T")
    line = pick_zero_attack_joke("2026-08-12", name="RESIIK")
"""

import hashlib

TOP_PERFORMER_JOKES = [
    "🏆 Let me be clear: {name} just put up {value} damage today, and that's not a typo — that's leadership. That's the California way.",
    "🏆 Folks, {name} didn't just do {value} damage today, they delivered results. While other guilds are debating, we're dominating.",
    "🏆 {name} — {value} damage. Book it, frame it, put it on a campaign poster right next to my hair, because we're both looking real good today.",
    "🏆 Here's the thing about {name}: {value} damage isn't luck, it's vision. It's what happens when you invest in greatness.",
    "🏆 We didn't just hit {value} damage today — {name} hit it. That's not rhetoric, that's a receipt.",
    "🏆 {name}: {value} damage, zero excuses. That's the kind of bold action this guild needs more of.",
    "🏆 I've seen a lot of numbers cross my desk, but {value} damage from {name}? That's gubernatorial-level performance.",
    "🏆 My fellow Californians, {name} put up {value} damage today. Some call it overkill. I call it a mandate.",
]

ZERO_ATTACK_JOKES = [
    "👻 {name}, 0 for 4 this week. Look, I'm not here to point fingers — but I am pointing directly at you on this one.",
    "👻 We have a state of emergency: {name} is 0/4 on attacks this week. Requesting immediate guild assistance.",
    "👻 {name}, 0/4 attacks. I campaigned on accountability, so — where were you?",
    "👻 Let's be honest, {name} — 0/4 this week is not the comeback story we were hoping for. Time to get back on the campaign trail.",
    "👻 {name} at 0/4 attacks. Even my approval rating's not that low. Let's turn this around, champ.",
    "👻 I don't do excuses, {name}, I do results. And right now the results say 0/4. Let's fix that before next week's town hall.",
    "👻 {name}, 0/4 attacks this week. If this were a budget, I'd call it a shortfall. Let's course-correct.",
    "👻 0/4, {name}? Even I show up to work. Get in there.",
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
