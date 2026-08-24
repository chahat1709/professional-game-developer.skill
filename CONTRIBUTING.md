# Contributing to professional-game-developer

Thank you for contributing to the **Universal Professional Game Developer Skill**! This repository provides senior-grade engineering, architectural, and mathematical guidance for AI coding agents and game developers across Unreal Engine 5, Unity 6 (DOTS), Godot 4.3+, Roblox (Luau), and Web/Custom engines.

---

## 1. Development & Local Testing

Before submitting a pull request, ensure all validation scripts and unit tests pass locally:

```bash
# Run the automated test suite
python3 -m unittest discover -s tests

# Validate the canonical asset manifest template
python3 skills/engineering/professional-game-developer/scripts/validate-asset-manifest.py skills/engineering/professional-game-developer/templates/asset-manifest.md

# Evaluate the canonical milestone report quality gate
python3 skills/engineering/professional-game-developer/scripts/quality-gate.py --milestone skills/engineering/professional-game-developer/templates/milestone-report.md
```

---

## 2. Directory Layout & Conventions

- `skills/engineering/professional-game-developer/SKILL.md` — Canonical skill entrypoint.
- `skills/engineering/professional-game-developer/references/` — Deep specialized technical guides.
- `skills/engineering/professional-game-developer/templates/` — Canonical Markdown project templates.
- `skills/engineering/professional-game-developer/scripts/` — Executable verification tools.
- `tests/` — Automated test suite verifying validation scripts.
- `SKILL.md` — Root convenience alias (must remain synchronized with the canonical file).

---

## 3. Reference Standards

When adding or updating reference documents in `references/`:
1. **Mathematical Rigor:** Include concrete formulas (e.g. Pacejka, XPBD, EV100, Glicko-2) and units rather than vague descriptions.
2. **Headless Agent Actionability:** Provide copy-pasteable CLI commands and headless execution flags.
3. **Multi-Engine Balance:** Maintain high technical depth across Unreal, Unity, Godot, Roblox, and Web.
4. **Clean Abstraction:** Avoid hardcoding project-specific naming or assets into universal files.

---

## 4. Pull Request Checklist

- [ ] All 8 unit tests in `tests/test_scripts.py` pass (`python3 -m unittest discover -s tests`).
- [ ] Any new reference links added to `SKILL.md` exist and resolve cleanly.
- [ ] Root `SKILL.md` is synchronized with `skills/engineering/professional-game-developer/SKILL.md`.
- [ ] Manifest and milestone quality gates pass with exit code `0`.
