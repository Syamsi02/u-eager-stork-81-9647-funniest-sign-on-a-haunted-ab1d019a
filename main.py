"""Funniest Sign on a Haunted Server Room Door.

Writes one funny sign line (120 characters at most) to the output
directory the grader provides, as entry.txt. Pure Python 3.13
standard library, no network, no randomness, no clock: every run
writes the exact same line.
"""

import os
import sys

SIGN = "NOTICE: Our server room ghost closes tickets as 'works on my machine.' Please knock twice before entering."

MAX_CHARS = 120


def main() -> int:
    if len(SIGN) > MAX_CHARS:
        raise ValueError("sign is longer than 120 characters")
    if not SIGN.strip():
        raise ValueError("sign is empty")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(SIGN)
    return 0


if __name__ == "__main__":
    sys.exit(main())
