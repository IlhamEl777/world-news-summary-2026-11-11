#!/usr/bin/env python3
"""news-summary-01 entry (Python 3.13, standard library only).

The summary of Wednesday 11 November 2026's world news lives in the
summary.txt file beside this program; the program copies it, byte for
byte, to the output directory as entry.txt. The copy is deterministic:
run it twice and the output is identical.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent / "summary.txt"
    # Copy raw bytes so the output is exactly the summary file, with no
    # newline translation or encoding surprises on any platform.
    (out_dir / "entry.txt").write_bytes(source.read_bytes())


if __name__ == "__main__":
    main()
