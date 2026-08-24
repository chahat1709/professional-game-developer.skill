#!/usr/bin/env python3
"""
Senior Quality Gate Validator.
Enforces multi-layer milestone verification (Build + Runtime + Visual evidence, Tests, Known Issues)
and prevents unverified boilerplate or placeholder submissions.
Usage:
    python quality-gate.py --milestone path/to/milestone-report.md
"""
import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

REQUIRED_SECTIONS = [
    ("Goal", r"^##\s+Goal\b"),
    ("Implemented", r"^##\s+Implemented\b"),
    ("Build evidence", r"^##\s+Build evidence\b"),
    ("Runtime evidence", r"^##\s+Runtime evidence\b"),
    ("Visual evidence", r"^##\s+Visual evidence\b"),
    ("Tests", r"^##\s+Tests\b"),
    ("Known issues", r"^##\s+Known issues\b"),
    ("Next smallest safe step", r"^##\s+Next smallest safe step\b"),
]

PLACEHOLDER_REGEX = re.compile(
    r"\[(What|How|Command|Map|Screenshot|Smoke|Honest|One focused|TODO|TBD|FIXME|placeholder|ID|URL|Name|Terms|Text|Result|cm/axes|Policy).*?\]|"
    r"\b(TODO|TBD|FIXME|PLACEHOLDER)\b",
    re.IGNORECASE
)


def extract_sections(text: str) -> Dict[str, str]:
    sections: Dict[str, str] = {}
    lines = text.splitlines()
    current_section = None
    current_lines: List[str] = []

    for line in lines:
        matched_section = None
        for name, pattern in REQUIRED_SECTIONS:
            if re.search(pattern, line.strip(), re.IGNORECASE):
                matched_section = name
                break

        if matched_section:
            if current_section:
                sections[current_section] = "\n".join(current_lines).strip()
            current_section = matched_section
            current_lines = []
        elif current_section:
            # Check if another H1 or H2 started
            if line.strip().startswith("# ") or (line.strip().startswith("## ") and not matched_section):
                sections[current_section] = "\n".join(current_lines).strip()
                current_section = None
                current_lines = []
            else:
                current_lines.append(line)

    if current_section:
        sections[current_section] = "\n".join(current_lines).strip()

    return sections


def evaluate_milestone(path: Path) -> int:
    if not path.exists():
        print(f"FAIL: Milestone report file not found: {path}")
        return 1

    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.strip():
        print(f"FAIL: Milestone file is empty: {path}")
        return 1

    errors: List[str] = []
    warnings: List[str] = []

    # 1. Check all required sections exist
    sections = extract_sections(text)
    for name, _ in REQUIRED_SECTIONS:
        if name not in sections:
            errors.append(f"Missing required section header: '## {name}'")

    # 2. Check for unfilled placeholders across the document
    placeholders_found = PLACEHOLDER_REGEX.findall(text)
    if placeholders_found:
        # Extract full match strings
        raw_matches = [m.group(0) for m in PLACEHOLDER_REGEX.finditer(text)]
        errors.append(f"Document contains {len(raw_matches)} unfilled placeholder(s): {raw_matches[:5]}")

    # 3. Check section content density and substantive evidence
    for name, content in sections.items():
        words = content.split()
        if len(words) < 5:
            errors.append(f"Section '## {name}' is empty or lacks substantive content ({len(words)} word(s)).")

    # 4. Check specific evidence sections for real indicators
    build_content = sections.get("Build evidence", "").lower()
    if build_content and not any(kw in build_content for kw in ["pass", "exit", "success", "0", "clean", "build", "compiled", "log", "error", "warning"]):
        warnings.append("Section '## Build evidence' does not contain explicit build outcome keywords.")

    runtime_content = sections.get("Runtime evidence", "").lower()
    if runtime_content and not any(kw in runtime_content for kw in ["fps", "ms", "hz", "memory", "log", "telemetry", "launch", "frame", "tick", "runtime"]):
        warnings.append("Section '## Runtime evidence' does not contain quantitative runtime or telemetry indicators.")

    visual_content = sections.get("Visual evidence", "").lower()
    if visual_content and not any(kw in visual_content for kw in [".png", ".jpg", ".mp4", ".gif", "render", "screenshot", "video", "capture", "viewport", "camera"]):
        warnings.append("Section '## Visual evidence' does not reference captured media or visual artifacts.")

    # Print summary
    print(f"=== Quality Gate Audit: {path.name} ===")
    if errors:
        print(f"\nFAIL: {len(errors)} blocking quality gate failure(s):")
        for err in errors:
            print(f"  [X] {err}")
        if warnings:
            print(f"\nWarnings ({len(warnings)}):")
            for w in warnings:
                print(f"  [!] {w}")
        return 1

    if warnings:
        print(f"\nPASS with {len(warnings)} warning(s):")
        for w in warnings:
            print(f"  [!] {w}")
    else:
        print("\nPASS: Quality gate fully satisfied (Build, Runtime, and Visual evidence verified).")

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Senior Quality Gate milestone evaluator.")
    parser.add_argument("--milestone", required=True, help="Path to milestone-report.md")
    args = parser.parse_args()
    sys.exit(evaluate_milestone(Path(args.milestone)))
