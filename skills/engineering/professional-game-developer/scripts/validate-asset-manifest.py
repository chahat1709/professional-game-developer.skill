#!/usr/bin/env python3
"""
Senior asset manifest validator.
Checks that every asset row has provenance, license, and validation.
Usage: python validate-asset-manifest.py path/to/manifest.csv
"""
import csv
import sys
from pathlib import Path

REQUIRED = ["Asset ID", "Source", "Creator", "License", "Format", "Destination", "Validation"]

def validate(path: Path) -> int:
    if not path.exists():
        print(f"FAIL: manifest not found: {path}")
        return 1
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        missing_cols = [c for c in REQUIRED if c not in (reader.fieldnames or [])]
        if missing_cols:
            print(f"FAIL: missing columns: {missing_cols}")
            return 1
        errors = 0
        for i, row in enumerate(reader, start=2):
            asset = row.get("Asset ID", "").strip()
            if not asset:
                print(f"Row {i}: FAIL — empty Asset ID")
                errors += 1
            for col in REQUIRED:
                if not row.get(col, "").strip():
                    print(f"Row {i} ({asset or '?'}): FAIL — empty '{col}'")
                    errors += 1
            lic = row.get("License", "").lower()
            if "unknown" in lic or "tbd" in lic:
                print(f"Row {i} ({asset}): FAIL — license unclear: {row.get('License')}")
                errors += 1
            if row.get("Validation", "").strip().lower() not in ("pass", "ok", "validated", "checked"):
                print(f"Row {i} ({asset}): WARN — validation not marked pass")
        if errors == 0:
            print("PASS: asset manifest complete")
            return 0
        print(f"FAIL: {errors} issue(s)")
        return 1

if __name__ == "__main__":
    p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("asset-manifest.csv")
    sys.exit(validate(p))
