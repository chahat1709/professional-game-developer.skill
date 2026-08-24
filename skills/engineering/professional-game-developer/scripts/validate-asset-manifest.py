#!/usr/bin/env python3
"""
Senior Asset Manifest Validator (Multi-format: CSV and Markdown table).
Validates provenance, licensing, format, scale, collision, and runtime validation records.
Usage:
    python validate-asset-manifest.py path/to/asset-manifest.md
    python validate-asset-manifest.py path/to/asset-manifest.csv
"""
import csv
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple

CANONICAL_COLUMNS = [
    "Asset ID",
    "Source",
    "Creator",
    "License",
    "Attribution",
    "Format",
    "Destination",
    "Scale",
    "Collision",
    "Nanite/LOD",
    "Validation"
]

VALID_STATUSES = {"pass", "ok", "validated", "checked", "approved"}
INVALID_LICENSES = {"unknown", "tbd", "pending", "unclear", "none", "n/a", "?"}
PLACEHOLDER_PATTERN = re.compile(r"^\[.*\]$|TODO|TBD|PLACEHOLDER", re.IGNORECASE)


def parse_markdown_table(text: str) -> Tuple[List[str], List[Dict[str, str]]]:
    lines = [line.strip() for line in text.splitlines() if line.strip().startswith("|")]
    if len(lines) < 3:
        return [], []

    # Extract headers
    header_line = lines[0]
    headers = [col.strip() for col in header_line.strip("|").split("|")]

    # Check for separator line (e.g. |---|---|)
    sep_line = lines[1]
    if not all(re.match(r"^:?-+:?$", cell.strip()) for cell in sep_line.strip("|").split("|")):
        return [], []

    rows = []
    for line in lines[2:]:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < len(headers):
            # Pad missing cells
            cells.extend([""] * (len(headers) - len(cells)))
        row_dict = {headers[i]: cells[i] for i in range(len(headers))}
        rows.append(row_dict)

    return headers, rows


def parse_csv_file(path: Path) -> Tuple[List[str], List[Dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    return headers, rows


def validate(path: Path) -> int:
    if not path.exists():
        print(f"FAIL: Manifest file not found: {path}")
        return 1

    content = path.read_text(encoding="utf-8", errors="ignore")

    if path.suffix.lower() in [".md", ".markdown"]:
        headers, rows = parse_markdown_table(content)
        if not headers:
            print(f"FAIL: No valid markdown table found in {path}")
            return 1
    else:
        try:
            headers, rows = parse_csv_file(path)
        except Exception as e:
            print(f"FAIL: Error parsing CSV {path}: {e}")
            return 1

    # Check for required headers
    missing_cols = [c for c in CANONICAL_COLUMNS if c not in headers]
    if missing_cols:
        print(f"FAIL: Missing canonical columns: {missing_cols}")
        print(f"      Expected columns: {CANONICAL_COLUMNS}")
        print(f"      Found columns:    {headers}")
        return 1

    if not rows:
        print(f"FAIL: Manifest contains no asset entries (0 data rows).")
        return 1

    errors = 0
    warnings = 0

    for i, row in enumerate(rows, start=1):
        asset_id = row.get("Asset ID", "").strip()

        # Check Asset ID
        if not asset_id:
            print(f"Row {i}: FAIL — empty 'Asset ID'")
            errors += 1
            continue

        if PLACEHOLDER_PATTERN.search(asset_id):
            print(f"Row {i} ({asset_id}): FAIL — 'Asset ID' contains unfilled placeholder")
            errors += 1

        # Check required columns
        for col in CANONICAL_COLUMNS:
            val = row.get(col, "").strip()
            if not val:
                print(f"Row {i} ({asset_id}): FAIL — empty required field '{col}'")
                errors += 1
            elif PLACEHOLDER_PATTERN.search(val):
                print(f"Row {i} ({asset_id}): FAIL — field '{col}' contains unfilled placeholder: '{val}'")
                errors += 1

        # License validation
        lic = row.get("License", "").strip().lower()
        if any(inv in lic for inv in INVALID_LICENSES):
            print(f"Row {i} ({asset_id}): FAIL — invalid or ambiguous license: '{row.get('License')}'")
            errors += 1

        # Validation status check
        val_status = row.get("Validation", "").strip().lower()
        if val_status not in VALID_STATUSES:
            print(f"Row {i} ({asset_id}): FAIL — validation status '{row.get('Validation')}' not in approved set: {sorted(list(VALID_STATUSES))}")
            errors += 1

    if errors > 0:
        print(f"\nRESULT: FAIL ({errors} error(s), {warnings} warning(s))")
        return 1

    print(f"RESULT: PASS — Asset manifest valid ({len(rows)} verified asset(s))")
    return 0


if __name__ == "__main__":
    p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("asset-manifest.md")
    sys.exit(validate(p))
