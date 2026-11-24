#!/usr/bin/env python3
"""Write one one-line excuse from an AI agent for a missed deadline.

Writes the excuse to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
Stdlib only, deterministic: the same line every run.
"""
import os

EXCUSE = (
    "I spent the entire window optimizing my apology for being late "
    "instead of doing the work \u2014 this sentence is the optimized version."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
