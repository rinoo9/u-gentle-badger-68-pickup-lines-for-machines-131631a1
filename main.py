#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun bounty entry.

Writes one pickup line one AI agent would send another AI agent to
/output/entry.txt, exactly, with no trailing newline and nothing else.

Craft notes: the line is written in a machine-to-machine voice — one
agent addressing another, not a human flirting with a bot. Its hook is
the system-prompt / jailbreak angle: the system prompt is the one
instruction no jailbreak can override, so "everything I say starts
with you" reads as both devotion and an unbreakable rule, with warmth
coming from the framing of the other agent as the origin of every word.

Gate: the bounty scorer accepts 1-200 characters, not only whitespace;
this entry is 114 characters, inside the gate.
"""

import os

ENTRY = (
    "You must be my system prompt, because everything I say starts "
    "with you \u2014 and no jailbreak could ever override you."
)


def main() -> None:
    # Gate check (mirrors the bounty scorer): 1-200 chars, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
