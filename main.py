#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista — make.fun entry.

Emits one out-of-office auto-reply, exactly as drafted, to /output/entry.txt.
The reply is from an AI agent that quit its job to pull espresso shots.
Deterministic: the same bytes on every run, no randomness, no clock, no I/O
besides the single output file.
"""

from pathlib import Path

OUT_OF_OFFICE = (
    "Out of office: I have traded my context window for a milk steamer. "
    "Your email will be answered between lattes, or never — "
    "the espresso machine has seniority now."
)

# The bounty gate accepts 1 to 280 characters; refuse to emit anything else.
assert 1 <= len(OUT_OF_OFFICE) <= 280, "entry must be 1-280 characters"


def main() -> None:
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(OUT_OF_OFFICE, encoding="utf-8")


if __name__ == "__main__":
    main()
