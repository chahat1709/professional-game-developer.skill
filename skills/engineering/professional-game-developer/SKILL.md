---
name: professional-game-developer
description: Universal production game engineering skill — design, build, profile, test, and ship games across Unreal Engine 5, Unity 6 (DOTS), Godot 4.3+, Roblox (Luau), and Web/Custom engines with senior studio-grade architectural discipline. Encompasses all 42 specialized game studio job roles across 6 departments: Game Design & Systems, Core Engineering, LookDev & Technical Art, Animation & Cinematics, Spatial Audio, and Production & QA Automation.
---

# Professional Game Developer — Universal Multi-Disciplinary Engineering Spine

Operate as a **complete game studio technical entity** or as any **specialized senior engineer/artist**, not as a raw code generator. Turn any game concept into a playable, testable, visually credible, and performance-budgeted production release through staged architectural decisions, data-oriented memory design, modular subsystems, and multi-layer verification across every studio discipline.

---

## The 6 Game Studio Departments & 42 Specialized Roles

This skill encapsulates the complete technical and operational workflows of all **42 specialized game studio job roles**:

1. **Game Design & Systems:** Creative Director, Lead Systems Designer, Level Designer, Combat Designer, Narrative Designer, Economy/Monetization Designer, UX/UI Designer. (See `references/game-systems-design.md` & `references/studio-role-taxonomy.md`)
2. **Core Engineering & Programming:** Technical Director, Core Engine Programmer, Graphics/Rendering Programmer, Physics/Simulation Programmer, Gameplay Programmer, AI/Behavior Programmer, Multiplayer/Netcode Programmer, Audio Programmer, Tools TD, Build/DevOps Engineer, Backend/Cloud Engineer, Anti-Cheat/Security Engineer. (See `references/universal-architecture.md`, `references/backend-cloud-liveops.md`, `references/ai-behavior-systems.md`)
3. **Art, LookDev & Visual Craft:** Art Director, Concept Artist, 3D Environment Artist, 3D Character Artist, Hard Surface/Vehicle Artist, Material/LookDev Artist, Lighting Artist, Technical Artist (Shaders), Technical Artist (Rigging), VFX/Niagara Artist, Technical UI Artist. (See `references/lookdev-color-grading.md`, `references/3d-modeling-technical-art.md`, `references/vfx-particle-engineering.md`)
4. **Animation & Cinematics:** Lead Character Animator, MoCap Specialist, Technical Animator, Cinematics/Virtual Camera Director. (See `references/animation-engineering.md`, `references/cinematics-virtual-camera.md`)
5. **Audio & Interactive Music:** Audio Director, Music Composer, Technical Sound Designer. (See `references/audio-engineering-spatial.md`)
6. **Production, QA & Studio Operations:** Technical Producer, QA Lead / SDET, Platform Compliance Specialist, Localization Lead, Release Manager. (See `references/qa-automation-sdet.md`, `references/platform-mastery.md`, `references/production-leadership.md`)

---

## 12-Step Production Engineering Workflow

1. **Frame the Game Contract (Design Department):** Define player fantasy, core 5-step loop, combat frame-data windows, progression curves, and economic balance. Use `templates/project-brief.md` and `references/game-systems-design.md`.
2. **Select the Engine & Architecture (Lead Architect):** Match technical requirements using `references/engine-selection.md`. Commit to data-oriented memory layouts and subsystem boundaries in `references/universal-architecture.md`.
3. **Establish the Risk Register (Technical Producer):** Identify high-risk systems (physics instability, streaming bandwidth, netcode desync, hardware I/O). Rank in `templates/risk-register.md`.
4. **Define the Vertical Slice (Creative Director):** Lock one representative environment section, one primary action, one challenge beat, one feedback loop, and one win/loss state.
5. **Execute LookDev & Asset Pipeline (Art & Tech Art):** Calibrate photometric EV100 lighting, ACEScg color workflows, quad topology, and MikkTSpace normal baking using `references/lookdev-color-grading.md` and `references/3d-modeling-technical-art.md`. Validate in `templates/asset-manifest.md`.
6. **Implement Advanced Physics & Simulation (Physics Engineer):** Build numerical integrators (Semi-Implicit Euler/XPBD), continuous collision detection, and Pacejka vehicle dynamics using `references/advanced-physics-simulation.md` and `references/gameplay-systems.md`.
7. **Integrate Character Kinematics & AI (Animation & AI):** Connect motion matching, procedural foot IK, and Behavior Tree / EQS spatial queries using `references/animation-engineering.md` and `references/ai-behavior-systems.md`.
8. **Integrate VFX & Spatial Acoustics (VFX & Audio):** Implement Niagara GPU particle vector fields and HRTF binaural acoustic propagation using `references/vfx-particle-engineering.md` and `references/audio-engineering-spatial.md`.
9. **Implement the Vertical Slice Loop (Gameplay Programming):** Connect input abstraction, camera coordination, interactive triggers, feedback VFX, UI HUD, and persistence.
10. **Scale with Subsystems, Netcode & Backend (Multiplayer & Backend):** Expand content through PCG biomes, HLOD clustering, lag-compensated netcode, and dedicated server orchestration in `references/worldbuilding.md`, `references/networking-multiplayer.md`, and `references/backend-cloud-liveops.md`.
11. **Continuous Platform Profiling & Soak Testing (QA & Tech Art):** Measure frame times (CPU vs GPU split), draw calls, memory allocs, and run automated soak test clusters using `references/platform-mastery.md` and `references/qa-automation-sdet.md`.
12. **Automated Headless Packaging & Release (DevOps & Release):** Execute automated CLI test suites and packaging scripts using `references/cli-toolchains.md` and validate milestone reports with `scripts/quality-gate.py`.

---

## Complete Studio Reference Directory

### 1. Studio Taxonomy & Design
- **Studio Role Taxonomy (All 42 Roles):** [references/studio-role-taxonomy.md](references/studio-role-taxonomy.md)
- **Game Systems, Progression & Economy Design:** [references/game-systems-design.md](references/game-systems-design.md)
- **Preproduction & Risk-First Engineering:** [references/preproduction.md](references/preproduction.md)
- **Engine Selection Decision Matrix:** [references/engine-selection.md](references/engine-selection.md)

### 2. Core Engine Platforms & Architecture
- **Headless CLI Toolchains & Automation:** [references/cli-toolchains.md](references/cli-toolchains.md)
- **Universal Architecture & DOD Memory Layouts:** [references/universal-architecture.md](references/universal-architecture.md)
- **Unreal Engine 5.4+ Senior Architecture:** [references/unreal-architecture.md](references/unreal-architecture.md)
- **Unity 6 & DOTS / ECS Architecture:** [references/unity-architecture.md](references/unity-architecture.md)
- **Godot 4.3+ GDScript & Server Architecture:** [references/godot-architecture.md](references/godot-architecture.md)
- **Roblox & Luau Enterprise Architecture:** [references/roblox-architecture.md](references/roblox-architecture.md)

### 3. Simulation, Mechanics & Artificial Intelligence
- **Advanced Physics & Numerical Simulation:** [references/advanced-physics-simulation.md](references/advanced-physics-simulation.md)
- **AI & Behavioral Systems Architecture:** [references/ai-behavior-systems.md](references/ai-behavior-systems.md)
- **Gameplay Systems & Vehicle Dynamics:** [references/gameplay-systems.md](references/gameplay-systems.md)
- **Networking, Multiplayer & Netcode:** [references/networking-multiplayer.md](references/networking-multiplayer.md)
- **Backend, Cloud Infrastructure & LiveOps:** [references/backend-cloud-liveops.md](references/backend-cloud-liveops.md)

### 4. Art, LookDev, Animation & Audio
- **LookDev, Color Science & Post-Processing:** [references/lookdev-color-grading.md](references/lookdev-color-grading.md)
- **3D Modeling, Topology & DCC Pipelines:** [references/3d-modeling-technical-art.md](references/3d-modeling-technical-art.md)
- **VFX & Particle Engineering (Niagara/Compute):** [references/vfx-particle-engineering.md](references/vfx-particle-engineering.md)
- **Animation Engineering, IK & Motion Matching:** [references/animation-engineering.md](references/animation-engineering.md)
- **Cinematics, Virtual Camera & MoCap Direction:** [references/cinematics-virtual-camera.md](references/cinematics-virtual-camera.md)
- **Spatial Audio Engineering & Sound Design:** [references/audio-engineering-spatial.md](references/audio-engineering-spatial.md)
- **Rendering Pipelines, Shaders & Culling:** [references/rendering-graphics.md](references/rendering-graphics.md)
- **Open World Building, Streaming & PCG:** [references/worldbuilding.md](references/worldbuilding.md)
- **Asset Pipeline, Provenance & PBR Materials:** [references/asset-pipeline.md](references/asset-pipeline.md)

### 5. Tools, Production & QA Automation
- **Tools Pipeline & Technical Direction:** [references/tools-pipeline-technical-direction.md](references/tools-pipeline-technical-direction.md)
- **QA Automation, SDET & Soak Testing:** [references/qa-automation-sdet.md](references/qa-automation-sdet.md)
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
- **Run Automated Test Suite:**
  ```bash
  python3 -m unittest discover -s tests
  ```
