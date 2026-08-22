#!/usr/bin/env python3
"""
Senior quality gate — three evidence layers.
Checks that a milestone has build + runtime + visual evidence before calling it done.
Usage: python quality-gate.py --milestone path/to/milestone-report.md
"""
import argparse
import re
from pathlib import Path

CHECKS = [
    (r"## Build evidence", "Build evidence missing"),
    (r"## Runtime evidence", "Runtime evidence missing"),
    (r"## Visual evidence", "Visual evidence missing"),
    (r"## Tests", "Tests section missing"),
    (r"## Known issues", "Known issues missing (must be explicit)"),
]

def check(path: Path) -> int:
    if not path.exists():
        print(f"FAIL: milestone file not found: {path}")
        return 1
    text = path.read_text(encoding="utf-8", errors="ignore")
    fails = []
    for pat, msg in CHECKS:
        if not re.search(pat, text, re.IGNORECASE):
            fails.append(msg)
    # placeholder detection
    placeholders = len(re.findall(r"\[.*?(TODO|TBD|placeholder).*?\]", text, re.IGNORECASE))
    if fails:
        for m in fails:
            print(f"FAIL: {m}")
        return 1
    if placeholders > 0:
        print(f"WARN: {placeholders} placeholder(s) remain — replace before production")
    print("PASS: quality gate satisfied (build + runtime + visual present)")
    return 0

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--milestone", required=True, help="path to milestone-report.md")
    args = ap.parse_args()
    raise SystemExit(check(Path(args.milestone)))
