#!/usr/bin/env python3
"""
Unit tests for senior game developer quality scripts:
- validate-asset-manifest.py
- quality-gate.py
"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO_ROOT / "skills" / "engineering" / "professional-game-developer" / "scripts"
VALIDATE_SCRIPT = SCRIPTS_DIR / "validate-asset-manifest.py"
QUALITY_SCRIPT = SCRIPTS_DIR / "quality-gate.py"


class TestValidateAssetManifest(unittest.TestCase):

    def run_validator(self, manifest_content: str, suffix: str = ".md") -> subprocess.CompletedProcess:
        with tempfile.NamedTemporaryFile("w+", suffix=suffix, delete=False, encoding="utf-8") as tf:
            tf.write(manifest_content)
            tf_path = tf.name

        try:
            res = subprocess.run(
                [sys.executable, str(VALIDATE_SCRIPT), tf_path],
                capture_output=True,
                text=True
            )
            return res
        finally:
            Path(tf_path).unlink(missing_ok=True)

    def test_valid_markdown_manifest(self):
        valid_md = """# Asset Manifest

| Asset ID | Source | Creator | License | Attribution | Format | Destination | Scale | Collision | Nanite/LOD | Validation |
|---|---|---|---|---|---|---|---|---|---|---|
| SM_Rock_Granite_01 | https://ambientcg.com/a/Rock01 | ambientCG | CC0-1.0 | None required | GLB | /Content/Environment/Rocks | 1.0 (cm) | UCX custom hull | Nanite Enabled | Pass |
| TX_Cliff_Albedo | https://polyhaven.com/a/cliff | Poly Haven | CC0-1.0 | Poly Haven | PNG | /Content/Textures/Terrain | 2048x2048 | N/A | Mipmapped BC7 | Approved |
"""
        res = self.run_validator(valid_md, suffix=".md")
        self.assertEqual(res.returncode, 0, f"Expected 0, got {res.returncode}. Output:\n{res.stdout}\n{res.stderr}")
        self.assertIn("RESULT: PASS", res.stdout)

    def test_valid_csv_manifest(self):
        valid_csv = """Asset ID,Source,Creator,License,Attribution,Format,Destination,Scale,Collision,Nanite/LOD,Validation
SM_Rock_Granite_01,https://ambientcg.com/a/Rock01,ambientCG,CC0-1.0,None required,GLB,/Content/Environment/Rocks,1.0 (cm),UCX custom hull,Nanite Enabled,Pass
"""
        res = self.run_validator(valid_csv, suffix=".csv")
        self.assertEqual(res.returncode, 0, f"Expected 0, got {res.returncode}. Output:\n{res.stdout}\n{res.stderr}")
        self.assertIn("RESULT: PASS", res.stdout)

    def test_missing_columns_fails(self):
        bad_md = """| Asset ID | Source | License | Validation |
|---|---|---|---|
| SM_Rock_01 | https://example.com | CC0 | Pass |
"""
        res = self.run_validator(bad_md, suffix=".md")
        self.assertEqual(res.returncode, 1)
        self.assertIn("Missing canonical columns", res.stdout)

    def test_unfilled_placeholders_fails(self):
        placeholder_md = """| Asset ID | Source | Creator | License | Attribution | Format | Destination | Scale | Collision | Nanite/LOD | Validation |
|---|---|---|---|---|---|---|---|---|---|---|
| [ID] | [URL] | [Name] | [Terms] | [Text] | [FBX/GLB] | [/Game/...] | [cm/axes] | [Policy] | [Policy] | [Result] |
"""
        res = self.run_validator(placeholder_md, suffix=".md")
        self.assertEqual(res.returncode, 1)
        self.assertIn("FAIL", res.stdout)

    def test_ambiguous_license_fails(self):
        ambiguous_md = """| Asset ID | Source | Creator | License | Attribution | Format | Destination | Scale | Collision | Nanite/LOD | Validation |
|---|---|---|---|---|---|---|---|---|---|---|
| SM_Prop_01 | https://example.com | Artist | Unknown / TBD | Credit artist | FBX | /Content/Props | 1.0 | Box | Auto | Pass |
"""
        res = self.run_validator(ambiguous_md, suffix=".md")
        self.assertEqual(res.returncode, 1)
        self.assertIn("ambiguous license", res.stdout)


class TestQualityGate(unittest.TestCase):

    def run_gate(self, report_content: str) -> subprocess.CompletedProcess:
        with tempfile.NamedTemporaryFile("w+", suffix=".md", delete=False, encoding="utf-8") as tf:
            tf.write(report_content)
            tf_path = tf.name

        try:
            res = subprocess.run(
                [sys.executable, str(QUALITY_SCRIPT), "--milestone", tf_path],
                capture_output=True,
                text=True
            )
            return res
        finally:
            Path(tf_path).unlink(missing_ok=True)

    def test_valid_milestone_passes(self):
        valid_report = """# Milestone: Vertical Slice 01 — Core Flight & Physics

## Goal
Verify deterministic vehicle physics, input abstraction, and telemetry capture in the desert proving grounds map.

## Implemented
Implemented the core physics solver component, Enhanced Input action mappings for keyboard and gamepad, and live telemetry JSON export.

## Build evidence
Build command: `UnrealEditor-Cmd MyProject -run=Automation -test=Physics -unattended`
Result: Clean build, 0 compilation errors, 0 cooking warnings. Build exit code 0.

## Runtime evidence
Ran 60-second flight loop in DesertMap at 60 FPS (16.2 ms frame time, 6.4 ms CPU physics, 7.8 ms GPU). Telemetry stream logged 3600 samples with 0 dropped frames.

## Visual evidence
Captured 4K camera reference shot at `/Artifacts/Screenshots/desert_flight_hero.png` and flight loop video at `/Artifacts/Captures/flight_pass_01.mp4`.

## Tests
Executed 14 automated unit tests covering physics stabilization, altitude PID hold, and collision bounds. All 14 tests passed with 100% coverage.

## Known issues
High-speed wind turbulence damping creates slight over-correction when transitioning between thermal zones. Tracked as issue TECH-DEBT-014.

## Next smallest safe step
Implement landing zone proximity trigger volume and connect touchdown velocity scoring to HUD feedback.
"""
        res = self.run_gate(valid_report)
        self.assertEqual(res.returncode, 0, f"Expected 0, got {res.returncode}. Output:\n{res.stdout}\n{res.stderr}")
        self.assertIn("PASS: Quality gate fully satisfied", res.stdout)

    def test_empty_template_fails(self):
        empty_template = """# Milestone: [Name]

## Goal
[What this milestone proves]

## Implemented
[Systems, assets, maps, UI, tools]

## Build evidence
[Command, result, warnings/errors]

## Runtime evidence
[Map, command line, input, logs, save/telemetry]

## Visual evidence
[Screenshot/video/capture paths]

## Tests
[Smoke, functional, stress, hardware, visual]

## Known issues
[Honest limitations]

## Next smallest safe step
[One focused next step]
"""
        res = self.run_gate(empty_template)
        self.assertEqual(res.returncode, 1, f"Expected 1 on empty template, got {res.returncode}")
        self.assertIn("unfilled placeholder", res.stdout)

    def test_missing_section_fails(self):
        missing_section = """# Milestone: Incomplete

## Goal
Prove physics.

## Implemented
Physics solver.

## Build evidence
Build passed.
"""
        res = self.run_gate(missing_section)
        self.assertEqual(res.returncode, 1)
        self.assertIn("Missing required section header", res.stdout)


if __name__ == "__main__":
    unittest.main()
