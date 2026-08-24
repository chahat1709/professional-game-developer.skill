# professional-game-developer — Universal Game Engineering Skill

[![skills.sh](https://skills.sh/b/chahat1709/professional-game-developer.skill)](https://skills.sh/chahat1709/professional-game-developer.skill)

A **Senior Production Game Developer & Systems Engineering Skill** for AI coding agents (Claude Code, opencode, Cursor, Codex). It provides production-grade architectural guidance, data-oriented design (DOD) principles, headless CLI automation toolchains, and multi-layer verification gates across **Unreal Engine 5, Unity 6 (DOTS), Godot 4.3+, Roblox (Luau), and Web/Custom engines**.

---

## 1. What This Skill Delivers

- **Data-Oriented & Zero-Allocation Discipline:** Memory layout optimization (Structure of Arrays), cache locality, native arrays, and zero-allocation frame loops.
- **Deep Multi-Engine Coverage:**
  - **Unreal Engine 5.4+:** Gameplay Ability System (GAS), Mass Entity (ECS), Enhanced Input, World Partition, UAT automation.
  - **Unity 6 & DOTS:** Entities, `IJobEntity`, Burst compiler, Assembly Definitions (`.asmdef`), Addressables memory lifecycle.
  - **Godot 4.3+:** GDScript 2.0 static typing, direct Server API dispatches (`RenderingServer`), Scene Unique Nodes, GUT testing.
  - **Roblox / Luau:** Strict typing (`--!strict`), Zero-Trust Server Authority, ProfileService session locking, Rojo/Wally toolchains.
- **Headless CLI Toolchains:** Automated terminal command recipes to compile, run unit tests, and package builds in headless CI/CD pipelines without a GUI.
- **Executable Automated Quality Gates:**
  - Multi-format Asset Manifest Validator (`validate-asset-manifest.py`) supporting both Markdown tables and CSV files.
  - Substantive Milestone Quality Gate (`quality-gate.py`) requiring verified Build, Runtime, and Visual evidence.
  - Integrated unit test suite (`unittest`).

---

## 2. Structure

```
SKILL.md                                              # Universal root skill
skills/engineering/professional-game-developer/
  SKILL.md                                            # Canonical skill specification
  references/
    cli-toolchains.md                                 # Headless CLI build & test recipes
    universal-architecture.md                         # DOD, fixed simulation loops, memory
    engine-selection.md                               # Engine decision tree & matrix
    unreal-architecture.md                            # UE5.4+ GAS, Mass Entity, Enhanced Input
    unity-architecture.md                             # Unity 6 DOTS, Burst, asmdef, Addressables
    godot-architecture.md                             # Godot 4.3+ GDScript 2.0, Server APIs, GUT
    roblox-architecture.md                            # Luau strict, ProfileService, Rojo, Wally
    networking-multiplayer.md                         # Prediction, rollback, lag compensation
    rendering-graphics.md                             # Forward+/Deferred, CSM/VSM, Hi-Z, overdraw
    gameplay-systems.md                               # Pacejka vehicle physics, ragdolls, AI/BT
    worldbuilding.md                                  # World Partition, HLOD, PCG biomes
    asset-pipeline.md                                 # PBR, ORM packing, scale, collision proxies
    preproduction.md                                  # Risk registers, vertical slice contracts
    platform-mastery.md                               # Console TRC, mobile thermal, frame budgets
    production-leadership.md                          # Definition of Done, tech debt tracking
    quality-and-performance.md                        # Three evidence layers, test pyramid
    droneverse-adaptation.md                          # Vehicle simulation practical case study
    templates.md                                      # Canonical schemas and references
  templates/
    asset-manifest.md                                 # 11-column canonical asset manifest
    milestone-report.md                               # 8-section evidence milestone report
    project-brief.md                                  # One-page project contract
    risk-register.md                                  # Risk-first engineering matrix
    verification-matrix.md                            # Verification evidence matrix
  scripts/
    validate-asset-manifest.py                        # Executable manifest validator (MD & CSV)
    quality-gate.py                                   # Executable quality gate validator
tests/
  test_scripts.py                                     # Unit test suite for validation tools
```

---

## 3. Installation

### Claude Code, Codex, and Agent Tools via skills.sh
```bash
npx skills@latest add chahat1709/professional-game-developer.skill
```

### Claude Code Plugin (Managed)
```bash
claude plugins add https://github.com/chahat1709/professional-game-developer.skill
```

### Direct Clone
```bash
git clone https://github.com/chahat1709/professional-game-developer.skill
```

---

## 4. Running Validation Tools

```bash
# Run automated test suite
python3 -m unittest discover -s tests

# Validate an asset manifest (Markdown or CSV)
python3 skills/engineering/professional-game-developer/scripts/validate-asset-manifest.py templates/asset-manifest.md

# Evaluate a milestone report quality gate
python3 skills/engineering/professional-game-developer/scripts/quality-gate.py --milestone templates/milestone-report.md
```

---

## 5. License

MIT — see [LICENSE](LICENSE).
