# AGENTS

This repository follows standard AI agent skill conventions and the `mattpocock/skills` collection layout.

## Layout

- `skills/engineering/professional-game-developer/SKILL.md` — Canonical skill definition.
- `skills/engineering/professional-game-developer/references/` — Deep senior technical guides across architecture, rendering, netcode, physics, platforms, and CLI toolchains.
- `skills/engineering/professional-game-developer/templates/` — Canonical Markdown project templates.
- `skills/engineering/professional-game-developer/scripts/` — Executable verification tools (`validate-asset-manifest.py`, `quality-gate.py`).
- `tests/` — Automated test suite verifying validation scripts.
- `SKILL.md` — Root alias for single-skill installations.

## Agent Instructions

1. Load `skills/engineering/professional-game-developer/SKILL.md`.
2. Follow the 12-step engineering workflow and consult domain references as needed.
3. For automated builds and headless tests, consult `references/cli-toolchains.md`.
4. Validate all asset changes and milestone reports using the scripts in `scripts/`.
