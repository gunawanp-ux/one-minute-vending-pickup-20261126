#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single original pickup line, spoken as the vending machine
itself, to /output/entry.txt. The competition gate is 1-200 characters
of UTF-8 text, not only white space.
"""

import os

ENTRY = (
    "Hey, you don't need exact change \u2014 just press B4 and I'll drop "
    "your favourite. I've been holding it at eye level all day, waiting "
    "for someone sweet to walk by."
)

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} characters, outside the 1-{MAX_CHARS} gate"
    )
    assert ENTRY.strip(), "entry must not be only white space"
    # One line: no newline characters anywhere in the entry.
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
