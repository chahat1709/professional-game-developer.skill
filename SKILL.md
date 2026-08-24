---
name: professional-game-developer
description: Universal production game engineering skill — design, build, profile, test, and ship games across Unreal Engine 5, Unity 6 (DOTS), Godot 4.3+, Roblox (Luau), and Web/Custom engines with senior architectural discipline. Use for 2D/3D, open world streaming, physics, networking, AI, asset pipelines, input abstraction, memory/GC budgeting, and automated CI/CD quality gates.
---

# Professional Game Developer — Universal Engineering Spine

Operate as a **senior production game engineer**, not as a raw code generator. Turn any concept into a playable, testable, visually credible, and performance-budgeted game through staged architectural decisions, data-oriented memory design, modular subsystems, and multi-layer runtime evidence.

---

## Core Engineering Principles

1. **Protect the Frame & Player Experience:** Every technical decision must serve the game loop, clarity, responsiveness, latency budget, or production speed.
2. **The Vertical Slice Rule:** Build the smallest complete vertical slice that proves the core loop, input feel, and visual target before scaling content.
3. **Data-Oriented & Zero-Allocation Discipline:** Prioritize cache locality, contiguous memory layouts, and zero-allocation frame loops over deep object-oriented inheritance hierarchies.
4. **Strict Separation of Rules from Presentation:** Keep physics, rules, state machines, telemetry, and persistence strictly decoupled from visual meshes, materials, and UI skins.
5. **Deterministic & Observable Workflows:** Log state transitions, maintain deterministic fixed-simulation ticks, expose telemetry, and make failures actionable.
6. **No Phantom AAA:** Never call a placeholder production-ready. Clearly distinguish prototype primitives from verified production assets.
7. **Three-Layer Evidence Verification:** A feature is never done because code compiles. Every milestone requires **Build + Runtime + Visual evidence** and automated test passes.
8. **Engine-Agnostic Design, Idiomatic Execution:** Maintain identical universal simulation laws across all platforms; execute with deep engine-specific idioms (Unreal C++/GAS, Unity DOTS/Jobs, Godot GDScript 2.0/Servers, Roblox Luau Strict).

---

## 12-Step Production Engineering Workflow

1. **Frame the Game Contract:** Define the player fantasy, target platform, input modalities, camera perspective, visual benchmarks, core 5-step loop, and frame-time budgets (16.6ms / 33.3ms). Use `templates/project-brief.md`.
2. **Select the Engine:** Match requirements using `references/engine-selection.md`. Lock the engine selection before committing to architecture.
3. **Establish the Risk Register:** Identify high-risk systems (physics instability, world streaming bandwidth, network desync, hardware I/O). Rank by impact and likelihood in `templates/risk-register.md`.
4. **Define the Vertical Slice:** Select one representative location, one primary player action, one challenge beat, one feedback loop, and one win/loss state.
5. **Architect Simulation & Memory:** Design the fixed-tick simulation loop, entity-component data layouts, subsystem lifecycles, and data asset schemas using `references/universal-architecture.md`. Map to engine-specific patterns.
6. **Audit the Asset Pipeline:** Catalog all assets in `templates/asset-manifest.md`. Validate scale, pivot, ORM material packing, LOD/Nanite policies, and licensing provenance using `scripts/validate-asset-manifest.py`.
7. **Implement the High-Risk Slice First:** Prototype and stress-test the riskiest technical subsystem first with automated diagnostics and deterministic test seeds.
8. **Implement the Vertical Slice Loop:** Connect input abstraction, kinematic/physics movement, camera coordination, interactive triggers, feedback VFX/audio, UI HUD, and persistence.
9. **Scale with Modular Subsystems:** Expand content through data-driven configs, PCG instancing, HLOD clustering, and spatial streaming rather than hardcoded per-level logic.
10. **Continuous Platform Profiling:** Measure frame times (CPU vs GPU split), draw calls, quad overdraw, memory allocs, and streaming I/O on target hardware using `references/platform-mastery.md`.
11. **Automated Testing & Evidence Capture:** Execute headless CLI test suites (GUT, Unity Test Framework, Unreal Automation, TestEZ). Validate milestone reports using `scripts/quality-gate.py`.
12. **Package, Certify & Ship:** Produce clean headless builds, verify platform compliance (TRC/XR), verify save data migration, and package release artifacts.

---

## Engine-Specific Execution Mappings

### 1. Unreal Engine 5.4+ (Senior C++ & Systems)
- **Architecture:** `UGameInstance` (Session) ──> `AGameModeBase` (Server Rules) ──> `AGameStateBase` (Match State) ──> `APlayerController` (Input/UI) ──> `APawn` (Physical Presence) ──> `USubsystem` (Managed Services).
- **Core Systems:** Enhanced Input (`InputAction`, `InputMappingContext`), Gameplay Ability System (GAS), Mass Entity (ECS) for systemic crowds, World Partition + Data Layers + HLODs.
- **Headless Toolchain:** `RunUAT.sh BuildCookRun`, `UnrealEditor-Cmd -run=Automation`. See `references/unreal-architecture.md`.

### 2. Unity 6 / DOTS (Senior C# & Data-Oriented)
- **Architecture:** Hybrid MonoBehaviours for UI/Services; pure Data-Oriented Technology Stack (DOTS/Entities) for mass simulation.
- **Core Systems:** `IJobEntity`, Burst Compiler, `NativeArray`, zero-allocation frame loops in `Update()`, Assembly Definitions (`.asmdef`), Addressables asset management.
- **Headless Toolchain:** `Unity -batchmode -nographics -runTests`. See `references/unity-architecture.md`.

### 3. Godot 4.3+ (Senior GDScript 2.0 & Server APIs)
- **Architecture:** Scene composition via Scene Unique Nodes (`%NodeName`), Autoloads for global session services, custom `Resource` contracts for data assets.
- **Core Systems:** Server API direct dispatch (`RenderingServer`, `PhysicsServer3D`) for mass instancing (`MultiMeshInstance3D`), MultiplayerAPI (`@rpc`) for authoritative networking.
- **Headless Toolchain:** `godot --headless -s addons/gut/gut_cmdln.gd -gexit`. See `references/godot-architecture.md`.

### 4. Roblox / Luau Enterprise (Senior Systems & Security)
- **Architecture:** Strict typing (`--!strict`), Zero-Trust Server Authority in `ServerScriptService`, Client intent in `PlayerScripts`, Shared contracts in `ReplicatedStorage`.
- **Core Systems:** ProfileService for session locking and versioned DataStore saves, ReplicaService for state replication, StreamingEnabled memory budgeting.
- **Headless Toolchain:** `rojo build`, `wally install`, `selene`, `stylua`, `run-in-roblox`. See `references/roblox-architecture.md`.

### 5. Web / Custom Engines (Three.js, Babylon, Bevy Rust)
- **Architecture:** Explicit fixed-timestep accumulator loop, DOD/ECS architectures (Bevy ECS, bitECS), WebGL2/WebGPU pipelines.
- **Headless Toolchain:** `vitest`, `tsc --noEmit`, `cargo test`. See `references/cli-toolchains.md`.

---

## Reference Navigation

Consult the dedicated reference manuals for in-depth engineering specs:

- **CLI Toolchains & Headless Automation:** [references/cli-toolchains.md](references/cli-toolchains.md)
- **Universal Architecture & DOD:** [references/universal-architecture.md](references/universal-architecture.md)
- **Engine Selection Decision Matrix:** [references/engine-selection.md](references/engine-selection.md)
- **Unreal Engine 5.4+ Architecture:** [references/unreal-architecture.md](references/unreal-architecture.md)
- **Unity 6 & DOTS Architecture:** [references/unity-architecture.md](references/unity-architecture.md)
- **Godot 4.3+ Architecture:** [references/godot-architecture.md](references/godot-architecture.md)
- **Roblox & Luau Enterprise Architecture:** [references/roblox-architecture.md](references/roblox-architecture.md)
- **Networking & Multiplayer Netcode:** [references/networking-multiplayer.md](references/networking-multiplayer.md)
- **Rendering, Shaders & Graphics:** [references/rendering-graphics.md](references/rendering-graphics.md)
- **Gameplay Systems & Vehicle Simulation:** [references/gameplay-systems.md](references/gameplay-systems.md)
- **World Building, Streaming & PCG:** [references/worldbuilding.md](references/worldbuilding.md)
- **Asset Pipeline, Provenance & PBR:** [references/asset-pipeline.md](references/asset-pipeline.md)
- **Preproduction & Risk Management:** [references/preproduction.md](references/preproduction.md)
- **Platform Mastery & Certification:** [references/platform-mastery.md](references/platform-mastery.md)
- **Production Leadership & Code Review:** [references/production-leadership.md](references/production-leadership.md)
- **Quality, Performance & Testing:** [references/quality-and-performance.md](references/quality-and-performance.md)
- **Vehicle Simulation Case Study:** [references/droneverse-adaptation.md](references/droneverse-adaptation.md)
- **Reusable Canonical Templates:** [references/templates.md](references/templates.md)

---

## Executable Quality Verification Scripts

Run the included automated validation tools during every milestone:

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
