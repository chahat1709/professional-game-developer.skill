---
name: professional-game-developer
description: Universal production game engineering skill — design, build, profile, test, and ship games across Unreal Engine 5, Unity 6 (DOTS), Godot 4.3+, Roblox (Luau), and Web/Custom engines with senior architectural discipline. Encompasses all game engineering disciplines: LookDev & ACES color grading, XPBD physics, 3D DCC modeling pipelines, animation kinematics, spatial audio, networking, and CI/CD quality gates.
---

# Professional Game Developer — Universal Engineering Spine

Operate as a **senior production game engineer**, not as a raw code generator. Turn any concept into a playable, testable, visually credible, and performance-budgeted game through staged architectural decisions, data-oriented memory design, modular subsystems, and multi-layer runtime evidence across every engineering discipline.

---

## Core Engineering Principles

1. **Protect the Frame & Player Experience:** Every technical decision must serve the game loop, clarity, responsiveness, latency budget, or production speed.
2. **The Vertical Slice Rule:** Build the smallest complete vertical slice that proves the core loop, input feel, and visual target before scaling content.
3. **Data-Oriented & Zero-Allocation Discipline:** Prioritize cache locality, contiguous memory layouts (Structure of Arrays), and zero-allocation frame loops over deep object-oriented inheritance hierarchies.
4. **Strict Separation of Rules from Presentation:** Keep physics, rules, state machines, telemetry, and persistence strictly decoupled from visual meshes, materials, audio, and UI skins.
5. **Deterministic & Observable Workflows:** Log state transitions, maintain deterministic fixed-simulation ticks, expose telemetry, and make failures actionable.
6. **No Phantom AAA:** Clearly distinguish prototype primitives from verified production assets.
7. **Three-Layer Evidence Verification:** Every milestone requires **Build + Runtime + Visual evidence** and automated test passes.
8. **Holistic Multi-Disciplinary Coverage:** Master every technical craft: LookDev & Color Science, Numerical Physics Simulation, 3D Asset Engineering, Motion Matching & Animation Kinematics, HRTF Spatial Audio, Multiplayer Netcode, and Headless CI/CD Automation.

---

## 12-Step Production Engineering Workflow

1. **Frame the Game Contract:** Define player fantasy, target platform, input modalities, camera perspective, visual benchmarks, core 5-step loop, and frame-time budgets. Use `templates/project-brief.md`.
2. **Select the Engine:** Match requirements using `references/engine-selection.md`. Lock the engine selection before committing to architecture.
3. **Establish the Risk Register:** Identify high-risk systems (physics instability, world streaming bandwidth, network desync, hardware I/O). Rank in `templates/risk-register.md`.
4. **Define the Vertical Slice:** Select one representative location, one primary player action, one challenge beat, one feedback loop, and one win/loss state.
5. **Architect Simulation & Memory:** Design the fixed-tick simulation loop, entity-component data layouts, and subsystem lifecycles using `references/universal-architecture.md`.
6. **Execute LookDev & Asset Pipeline:** Calibrate photometric EV100 lighting, ACEScg color workflows, and 3D modeling/UV standards using `references/lookdev-color-grading.md` and `references/3d-modeling-technical-art.md`. Validate in `templates/asset-manifest.md`.
7. **Implement Advanced Physics & Mechanics:** Build numerical integrators (Semi-Implicit Euler/XPBD), continuous collision detection, and suspension mechanics using `references/advanced-physics-simulation.md` and `references/gameplay-systems.md`.
8. **Integrate Animation & Spatial Audio:** Connect motion matching, procedural foot IK, and HRTF acoustic propagation using `references/animation-engineering.md` and `references/audio-engineering-spatial.md`.
9. **Implement the Vertical Slice Loop:** Connect input abstraction, camera coordination, interactive triggers, feedback VFX, UI HUD, and persistence.
10. **Scale with Modular Subsystems & Netcode:** Expand content through PCG instancing, HLOD clustering, and lag-compensated multiplayer netcode using `references/worldbuilding.md` and `references/networking-multiplayer.md`.
11. **Continuous Platform Profiling:** Measure frame times (CPU vs GPU split), draw calls, quad overdraw, memory allocs, and streaming I/O on target hardware using `references/platform-mastery.md`.
12. **Automated Headless Testing & Packaging:** Execute automated CLI test suites and packaging scripts using `references/cli-toolchains.md` and validate milestone reports with `scripts/quality-gate.py`.

---

## Comprehensive Engineering Domain References

Consult the specialized technical references for in-depth engineering specs:

### 1. Engine Platforms & Architecture
- **Headless CLI Toolchains & Automation:** [references/cli-toolchains.md](references/cli-toolchains.md)
- **Universal Architecture & DOD Memory Layouts:** [references/universal-architecture.md](references/universal-architecture.md)
- **Engine Selection Decision Matrix:** [references/engine-selection.md](references/engine-selection.md)
- **Unreal Engine 5.4+ Senior Architecture:** [references/unreal-architecture.md](references/unreal-architecture.md)
- **Unity 6 & DOTS / ECS Architecture:** [references/unity-architecture.md](references/unity-architecture.md)
- **Godot 4.3+ GDScript & Server Architecture:** [references/godot-architecture.md](references/godot-architecture.md)
- **Roblox & Luau Enterprise Architecture:** [references/roblox-architecture.md](references/roblox-architecture.md)

### 2. Core Simulation, Graphics & Technical Art
- **LookDev, Color Science & Post-Processing:** [references/lookdev-color-grading.md](references/lookdev-color-grading.md)
- **Advanced Physics & Numerical Simulation:** [references/advanced-physics-simulation.md](references/advanced-physics-simulation.md)
- **3D Modeling, Topology & DCC Pipelines:** [references/3d-modeling-technical-art.md](references/3d-modeling-technical-art.md)
- **Animation Engineering, IK & Motion Matching:** [references/animation-engineering.md](references/animation-engineering.md)
- **Spatial Audio Engineering & Sound Design:** [references/audio-engineering-spatial.md](references/audio-engineering-spatial.md)
- **Rendering Pipelines, Shaders & Culling:** [references/rendering-graphics.md](references/rendering-graphics.md)
- **Networking, Multiplayer & Netcode:** [references/networking-multiplayer.md](references/networking-multiplayer.md)
- **Gameplay Systems & Vehicle Dynamics:** [references/gameplay-systems.md](references/gameplay-systems.md)
- **Open World Building, Streaming & PCG:** [references/worldbuilding.md](references/worldbuilding.md)
- **Asset Pipeline, Provenance & PBR Materials:** [references/asset-pipeline.md](references/asset-pipeline.md)

### 3. Production, Tools & Quality Gates
- **Tools Pipeline & Technical Direction:** [references/tools-pipeline-technical-direction.md](references/tools-pipeline-technical-direction.md)
- **Preproduction & Risk-First Engineering:** [references/preproduction.md](references/preproduction.md)
- **Platform Mastery & Certification Gates:** [references/platform-mastery.md](references/platform-mastery.md)
- **Production Leadership & Engineering Governance:** [references/production-leadership.md](references/production-leadership.md)
- **Quality, Performance & Test Verification:** [references/quality-and-performance.md](references/quality-and-performance.md)
- **Vehicle Simulation Practical Case Study:** [references/droneverse-adaptation.md](references/droneverse-adaptation.md)
- **Canonical Reusable Project Templates:** [references/templates.md](references/templates.md)

---

## Executable Verification Tools

- **Validate Asset Manifest:**
  ```bash
  python skills/engineering/professional-game-developer/scripts/validate-asset-manifest.py path/to/asset-manifest.md
  ```
- **Evaluate Milestone Quality Gate:**
  ```bash
  python skills/engineering/professional-game-developer/scripts/quality-gate.py --milestone path/to/milestone-report.md
  ```
- **Run Python Test Suite:**
  ```bash
  python3 -m unittest discover -s tests
  ```
