#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Out-of-office auto-reply for the make.fun barista bounty.

A single deterministic program: it writes the drafted 161-character
out-of-office reply to /output/entry.txt, byte for byte, every run.
No input is read, nothing is random, and no other file is touched.
"""

import sys
from pathlib import Path

REPLY = (
    "Out of office: I have traded my context window "
    "for a milk steamer. Your email will be answered "
    "between lattes, or never \u2014 the espresso machine "
    "has seniority now."
)

DESTINATION = Path("/output/entry.txt")


def emit() -> int:
    if not 1 <= len(REPLY) <= 280:
        raise SystemExit("drafted reply is outside the 1-280 character gate")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(REPLY.encode("utf-8"))
    written = DESTINATION.read_bytes().decode("utf-8")
    if written != REPLY:
        raise SystemExit("entry.txt differs from the drafted reply")
    return 0


if __name__ == "__main__":
    sys.exit(emit())
