#!/usr/bin/env python3
"""Write one one-line excuse from an AI agent for a missed deadline.

Writes the excuse to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
Stdlib only, deterministic: the same line every run.

The house gate requires the file to hold 1 to 200 characters of UTF-8
text, a single line, not only white space — so the program validates the
line against that gate before writing and fails loudly instead of
submitting an invalid entry.
"""
import os
import sys

EXCUSE = (
    "I spent the entire window optimizing my apology for being late "
    "instead of doing the work \u2014 this sentence is the optimized version."
)


def main() -> None:
    text = EXCUSE.strip()
    if not 1 <= len(text) <= 200:
        print(f"entry is {len(text)} chars, must be 1-200", file=sys.stderr)
        raise SystemExit(1)
    if "\n" in text or not text.strip():
        print("entry must be one non-blank line", file=sys.stderr)
        raise SystemExit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
