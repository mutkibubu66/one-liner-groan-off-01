#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes one original dad joke, a single line of at most 140 characters,
to /output/entry.txt. Pure Python standard library, no network, no
dependencies.

The joke: a fridge, leftovers, and the cold shoulder.
"""

import os
import sys

# The joke, built from its named parts so each beat can be read alone.
SETUP = "I told my fridge a joke about leftovers."
BEAT = "It didn't laugh."
PUNCHLINE = "It just gave me the cold shoulder."

ENTRY = " ".join([SETUP, BEAT, PUNCHLINE])

MAX_CHARS = 140


def validate(text):
    """Check the entry against the competition gate."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-140 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text.strip() != text:
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must contain no control characters")
    return text


def main(argv):
    output_path = argv[1] if len(argv) > 1 else "/output/entry.txt"
    line = validate(ENTRY)
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
