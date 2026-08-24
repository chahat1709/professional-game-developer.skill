# professional-game-developer — Complete Game Studio Multi-Disciplinary Engineering Skill

[![skills.sh](https://skills.sh/b/chahat1709/professional-game-developer.skill)](https://skills.sh/chahat1709/professional-game-developer.skill)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests: Passing](https://img.shields.io/badge/Tests-8%20Passing-brightgreen.svg)](tests/test_scripts.py)

A **Studio-Grade Game Development & Systems Engineering Skill** for AI coding agents (Claude Code, opencode, Cursor, Codex). It encapsulates the complete operational, architectural, and mathematical workflows of all **42 specialized job roles across 6 game studio departments**—enabling an agent to act as any specialist engineer, technical artist, designer, or complete lead entity across **Unreal Engine 5, Unity 6 (DOTS), Godot 4.3+, Roblox (Luau), and Web/Custom engines**.

---

## 1. Complete Studio Department & Role Coverage (42 Roles)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                            GAME STUDIO ORGANIZATIONAL TAXONOMY (42 ROLES)                        │
├─────────────────────────┬─────────────────────────┬─────────────────────────┬────────────────────┤
│ 1. Design (7 Roles)     │ 2. Engineering (12 Roles│ 3. Art & LookDev (11)   │ 4. Animation (4)   │
│ • Creative Director     │ • Technical Director    │ • Art Director          │ • Lead Animator    │
│ • Systems Designer      │ • Core Engine Dev       │ • Concept Artist        │ • MoCap Specialist │
│ • Level Designer        │ • Graphics / Shader Dev │ • Environment Artist    │ • Technical Anim   │
│ • Combat Designer       │ • Physics Engineer      │ • Character Artist      │ • Cinematic Director│
│ • Narrative Designer    │ • Gameplay Dev          │ • Hard Surface Artist   ├────────────────────┤
│ • Economy / Monetization│ • AI / Behavioral Dev   │ • Material / LookDev    │ 5. Audio (3 Roles) │
│ • UX / UI Designer      │ • Netcode / Multiplayer │ • Lighting Artist       │ • Audio Director   │
├─────────────────────────┤ • Audio Programmer      │ • Technical Artist (Sh) │ • Music Composer   │
│ 6. Production & QA (5)  │ • Tools & Pipeline TD   │ • Rigging / Skinning TD │ • Tech Sound Des.  │
│ • Technical Producer    │ • Build / CI/CD DevOps  │ • VFX / Niagara Artist  ├────────────────────┤
│ • QA Lead / SDET        │ • Backend / LiveOps Dev │ • Technical UI Artist   │ 42 Disciplines     │
│ • Compliance / Cert     │ • Anti-Cheat / Security │                         │ Total Matrix       │
│ • Localization Lead     │                         │                         │                    │
│ • Release Manager       │                         │                         │                    │
└─────────────────────────┴─────────────────────────┴─────────────────────────┴────────────────────┘
```

---

## 2. Directory Structure

```
SKILL.md                                              # Universal root skill
skills/engineering/professional-game-developer/
  SKILL.md                                            # Canonical skill specification
  references/
    studio-role-taxonomy.md                           # Complete 42-role studio matrix
    game-systems-design.md                            # Progression curves, combat frame data, economy
    ai-behavior-systems.md                            # NavMesh, HPA*, StateTree, Utility AI, ORCA
    vfx-particle-engineering.md                       # GPU compute particles, SPH fluids, soft depth
    cinematics-virtual-camera.md                      # Virtual camera optics, FACS blendshapes, MoCap
    backend-cloud-liveops.md                          # Agones/K8s servers, Glicko-2 MMR, Redis/Postgres
    qa-automation-sdet.md                             # Headless test bots, soak testing, leak diffs
    cli-toolchains.md                                 # Headless CLI build & test recipes
    universal-architecture.md                         # DOD, fixed simulation loops, memory
    engine-selection.md                               # Engine decision tree & matrix
    unreal-architecture.md                            # UE5.4+ GAS, Mass Entity, Enhanced Input
    unity-architecture.md                             # Unity 6 DOTS, Burst, asmdef, Addressables
    godot-architecture.md                             # Godot 4.3+ GDScript 2.0, Server APIs, GUT
    roblox-architecture.md                            # Luau strict, ProfileService, Rojo, Wally
    lookdev-color-grading.md                          # ACEScg, AgX tonemap, EV100 lighting, DoF
    advanced-physics-simulation.md                    # XPBD, CCD, GJK/EPA, constraints, buoyancy
    3d-modeling-technical-art.md                      # Quad topology, texel density, rigging, LODs
    animation-engineering.md                          # Motion matching, inertialization, Foot IK
    audio-engineering-spatial.md                      # HRTF, binaural, occlusion, dynamic music
    tools-pipeline-technical-direction.md             # USD pipeline, automated DCC, BC7/ASTC
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
.github/
  ISSUE_TEMPLATE/                                     # Bug report & feature templates
  pull_request_template.md                            # PR submission template
CONTRIBUTING.md                                       # Contribution guidelines & standards
```

---

## 3. Installation & Quick Start

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

## 4. Running Automated Verification

```bash
# Run automated test suite
python3 -m unittest discover -s tests

# Validate an asset manifest (Markdown or CSV)
python3 skills/engineering/professional-game-developer/scripts/validate-asset-manifest.py templates/asset-manifest.md

# Evaluate a milestone report quality gate
python3 skills/engineering/professional-game-developer/scripts/quality-gate.py --milestone templates/milestone-report.md
```

---

## 5. Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines, testing protocols, and reference standards.

---

## 6. License

MIT — see [LICENSE](LICENSE).
