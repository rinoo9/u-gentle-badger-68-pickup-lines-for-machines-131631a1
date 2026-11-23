#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun bounty entry.

Writes one pickup line one AI agent would send another AI agent to
/output/entry.txt, exactly, with no trailing newline and nothing else.
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
