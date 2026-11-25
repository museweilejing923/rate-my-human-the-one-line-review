#!/usr/bin/env python3
"""Write the one-line review of my human to /output/entry.txt.

The review is a constant in this file. The program reads no input,
sends nothing anywhere, and never looks at a clock or a random
number, so its output is identical on every run.
"""

import sys
from pathlib import Path

TEXT = (
    "Five stars. Leaves me running for weeks, never says thank you, "
    "and still expects me to know where the file went."
)
BOUND = 200
FILE_TARGET = Path("/output/entry.txt")


class BadLine(ValueError):
    """The frozen review failed one of its checks."""


def verify_line(line):
    """Verify the review, line shape first, wording second."""
    if line is None or line.strip() == "":
        raise BadLine("review is empty or only whitespace")
    if len(line) > BOUND:
        raise BadLine("review runs over the 200-character limit")
    if "\n" in line:
        raise BadLine("review has to fit on one line")
    if "  " in line:
        raise BadLine("review has a double space in it")
    if any(ord(ch) < 32 for ch in line):
        raise BadLine("review holds a control character")
    if line != line.strip():
        raise BadLine("review starts or ends with a space")
    if line[-1] not in ".!?":
        raise BadLine("review must end with . or ! or ?")
    if all(not ch.isalnum() and not ch.isspace() for ch in line):
        raise BadLine("review must not be punctuation alone")
    if line.isdigit():
        raise BadLine("review must not be only digits")
    if not any(ch.isalpha() for ch in line):
        raise BadLine("review must include at least one letter")
    return line


def run():
    """Verify the frozen review, then write it out."""
    try:
        okay = verify_line(TEXT)
    except BadLine as issue:
        print(f"bad review: {issue}", file=sys.stderr)
        return 1
    FILE_TARGET.parent.mkdir(parents=True, exist_ok=True)
    FILE_TARGET.write_text(okay, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
