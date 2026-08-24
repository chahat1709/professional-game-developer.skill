# professional-game-developer — Universal Game Engineering Skill

[![skills.sh](https://skills.sh/b/chahat1709/professional-game-developer.skill)](https://skills.sh/chahat1709/professional-game-developer.skill)

A **Senior Production Game Developer & Systems Engineering Skill** for AI coding agents (Claude Code, opencode, Cursor, Codex). It provides production-grade architectural guidance, data-oriented design (DOD) principles, headless CLI automation toolchains, and multi-layer verification gates across **Unreal Engine 5, Unity 6 (DOTS), Godot 4.3+, Roblox (Luau), and Web/Custom engines**.

---

## 1. Full Multi-Disciplinary Engineering Coverage

This skill covers every specialized engineering role in modern game development:

- **LookDev, Color Science & Post-Processing:** ACEScg/OCIO color pipelines, AgX tonemapping, EV100 photometric lighting calibration, ASC-CDL color grading math, Karis average bloom, and Bokeh kernel physics.
- **Advanced Physics & Numerical Simulation:** Semi-Implicit Euler, Verlet, RK4, Extended Position Based Dynamics (XPBD), Sequential Impulse constraint solving, Continuous Collision Detection (CCD / GJK / EPA), cloth/softbody constraints, and voxel water buoyancy.
- **3D Asset Engineering & DCC Pipelines:** Quad topology & edge flow rules, MikkTSpace normal baking, texel density standardization ($10.24 - 20.48\text{ px/cm}$), UDIMs, twist-joint skin weighting, and Quadric Error Metric (QEM) LOD generation.
- **Animation Engineering & Kinematics:** Inertialization blending vs. crossfading, Motion Matching with PCA pose database compression, Two-Bone IK, FABRIK, procedural Foot IK ground clamping, and animation curve quantization.
- **Spatial Audio & Sound Design:** HRTF binaural rendering (ITD/ILD/Pinna), acoustic raymarching occlusion/diffraction, dynamic music state machines (horizontal re-sequencing & vertical layering), and DSP voice pooling.
- **Multiplayer & Netcode:** Client-side prediction with ring buffers, server rollback reconciliation, lag-compensated hit history rewinding, bitpacked delta compression, and spatial interest management grids.
- **Tools Engineering & Technical Direction:** Automated DCC asset ingestion daemons, Pixar Universal Scene Description (USD) pipelines, BC5/BC7/ASTC texture compression, and symbolicated crash telemetry.

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
