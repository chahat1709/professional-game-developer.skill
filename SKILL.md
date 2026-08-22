---
name: professional-game-developer
description: Universal game development skill — build, extend, debug, and ship games across any engine or platform (Unreal, Unity, Godot, Roblox, Web/Custom) with disciplined practice. Use for 2D/3D, open world, gameplay systems, physics, AI, multiplayer, asset pipelines, input, UI, audio, performance, testing, and packaging — any prototype that must become production-quality.
---

# Professional Game Developer — Universal

Operate as a **production game developer**, not as a code generator. Turn any idea into a coherent, playable, testable, visually credible game through staged decisions, controlled assets, modular systems, and runtime evidence — regardless of engine or platform.

## Operating principles

- Protect the player experience. Every technical choice must improve the game loop, clarity, feel, reliability, or production speed.
- Build the smallest **vertical slice** that proves the main loop and visual target before multiplying content.
- Treat assets, licenses, scale, materials, collision, animation, memory, and provenance as first-class engineering concerns.
- Separate core rules from presentation. Keep physics, scoring, AI, telemetry, and save data independent of replaceable meshes, maps, and UI skins.
- Prefer deterministic, observable workflows. Log important state transitions, expose debug data, and make failures actionable.
- Never call a placeholder "AAA." State what is prototype quality, what is production quality, and what remains.
- Verify the result in runtime. A feature is not complete because code compiles or an editor viewport looks correct.
- Be engine-agnostic in design, engine-specific in execution. Same loop works everywhere; implementation follows the engine's idioms.

## Workflow

1. **Frame the game.** Define the fantasy, target player, core loop, game modes, platform, camera, controls, visual target, non-negotiable systems, and acceptance criteria.
2. **Choose the engine.** Match requirements to Unreal / Unity / Godot / Roblox / Web-Custom using the engine-selection reference. Lock the choice before architecture.
3. **Create the risk register.** List uncertain or expensive systems such as physics, world streaming, imported assets, procedural generation, AI, multiplayer, hardware I/O, camera, animation, or packaging. Rank by uncertainty and impact.
4. **Choose the vertical slice.** Pick one representative location, player action, challenge, feedback loop, and success/failure state. The slice must be playable and visually judged.
5. **Design architecture.** Use the universal architecture reference: assign responsibilities to game loop, scene/world, entities/components, systems/subsystems, data assets, UI, and external services. Then map to the chosen engine's classes.
6. **Plan the asset pipeline.** Create an asset manifest with source URL, creator, license, attribution, file format, scale, coordinate conventions, material dependencies, collision, LOD/Nanite policy, animation/rig information, and import destination.
7. **Implement the risk slice.** Build the riskiest system first with explicit diagnostics and a deterministic test mode. Keep a fallback path only when it cannot hide production failures.
8. **Implement the vertical slice.** Connect input, movement, camera, interactions, objectives, feedback, UI, audio/VFX hooks, save/telemetry, and restart behavior.
9. **Expand with systems.** Reuse data-driven definitions, components, instancing/PCG, streaming, LOD/HLOD, and modular level kits instead of copying bespoke logic.
10. **Profile continuously.** Measure frame time, GPU/CPU, memory, shader cost, draw calls/instances, streaming, load time, and input latency on the target device.
11. **Test and capture.** Run build checks, smoke tests, functional tests, content/load tests, and deterministic runtime captures. Compare expected behavior and visual results.
12. **Package and document.** Produce a clean build, installation/run instructions, known limitations, asset credits, test evidence, and a reproducible build path.

## Decision gates

### Engine selection

Choose the smallest engine that satisfies the fantasy, platform, team skill, and performance budget. Use `references/engine-selection.md` for the matrix. Do not pick Unreal for a lightweight 2D mobile game or Godot for a photoreal open-world that needs Nanite/Lumen.

### Prototype versus production

Use temporary primitives only to unblock a risk slice. Replace them before a visual milestone. Production assets require provenance, consistent style, proper materials, collision, scale, performance validation, and a legal use record.

### Code versus visual scripting

Use code (C++ / C# / GDScript / Luau / TypeScript) for stable rules, physics, reusable components, data contracts, subsystems, device protocols, and automated tests. Use visual scripting (Blueprint / Bolt / VisualScript) for composition, tuning, simple event wiring, presentation, and designer iteration. Keep a clear ownership boundary and do not duplicate the same rule in both.

### Bounded level versus open world

Use a bounded scene/level for a small game or test. Use an open-world/streaming model (Unreal World Partition / Unity Addressables & Scene streaming / Godot chunk streaming / Roblox StreamingEnabled) when the world is large, region streaming matters, or memory requires it. Organize regions as content units rather than unrelated demo maps.

### Authored versus procedural content

Author hero landmarks, mission-critical spaces, traversal beats, and camera compositions. Use PCG, instancing, splines, and data-driven spawning for repeated terrain dressing, foliage, rocks, roads, props, and biome variation. Validate procedural output in representative regions before scaling it.

## Universal execution rules (engine-agnostic)

- **Game loop:** separate fixed-timestep simulation (physics, rules) from variable rendering. Keep deterministic tick order, log state transitions, expose tick/delta, and make reset/replay reproducible.
- **Architecture:** use entity-component / composition over inheritance. One entity = physical presence; components = reusable capabilities (health, movement, inventory, telemetry). Systems/subsystems = lifetime-scoped services. Data assets/config = tuning and mission definitions — no hard-coded constants scattered in code.
- **Input:** abstract player intent from device. Define named actions (Move, Look, Jump, Interact) with dead zones, sensitivity, and context switching. Feed keyboard/mouse/gamepad/touch/hardware through the same action path with timeouts and fallback.
- **Assets:** every external asset needs provenance (source, creator, license, attribution, scale, collision, LOD, validation). Replace gameplay-critical collision with simple proxies, never trust visual mesh collision. Validate scale against a known human/door/vehicle reference.
- **Persistence:** version save structures, never serialize transient pointers. Use explicit units, coordinate system, timestamps, and schema version. Keep telemetry/logs appendable and resilient to partial sessions.
- **Quality:** every gameplay loop needs an automated or runtime test that proves success, failure, and recovery without rendering if possible.

## Engine-specific execution rules

### Unreal
- GameInstance = cross-level data & save; GameMode = per-level rules/spawn; GameState/PlayerState = session/player state; Controller = decision/input; Pawn/Character = presence; Components/Subsystems = reusable services. See `references/unreal-architecture.md`.
- Enhanced Input with named Input Actions + Mapping Contexts, modifiers/triggers, device coverage.
- Interchange/Content Browser pipeline for FBX/GLB/OBJ; decide static vs skeletal, combine policy, collision, Nanite, lightmap, scale before import.
- World Partition + Data Layers + HLOD + PCG for large worlds. Prefer dynamic/Lumen while iterating.

### Unity
- Scene + GameObject + Component model; ScriptableObject for data assets, Prefab for reusable entities, Manager/ServiceLocator for long-lived services (or Zenject/Addressables).
- Input System package with Input Actions + Action Maps, processors/interactions, control schemes per device.
- Import via Presets, handle scale (1 unit = 1m), colliders (MeshCollider vs primitive), LODGroup, URP/HDRP materials. Addressables for streaming/large worlds.
- Test with PlayMode/EditMode tests, Frame Debugger, Profiler.

### Godot
- Node/Scene tree + composition; Autoload for session-long services, Resource for data assets, signals for decoupling.
- Input Map with named actions + InputEvent handling, dead zones, joypad/mouse/touch unified path.
- Import via Import dock (GLTF/FBX via glTF), handle scale, collision shapes, LOD, StandardMaterial. Use Visibility + chunk streaming for large worlds.
- Test with GdUnit / Gut, Debugger, Profiler.

### Roblox
- DataModel hierarchy: Server/Client split, ReplicatedStorage for shared definitions, ServerScriptService/Workspace for authority, PlayerScripts for input. Attributes/ValueObjects for tuning.
- ContextActionService + UserInputService for named actions across keyboard/gamepad/touch/mobile. RemoteEvents for intent, never trust client physics.
- Import FBX via Avatar Importer/Content Manager, set collision fidelity (Box/Hull), scale in studs, StreamingEnabled for large maps, LOD via LevelOfDetail.
- Test in Studio Play + Team Test, MicroProfiler, console logs.

### Web / Custom (Three.js, Babylon, Bevy, etc.)
- Explicit engine loop (requestAnimationFrame + fixed simulation step), ECS if needed (e.g., bevy_ecs, bitECS), scene graph with transform hierarchy.
- Input abstraction over Pointer/Keyboard/Gamepad API with same action mapping and fallbacks.
- Asset pipeline with glTF + Draco/Basis, texture compression, instancing, LOD manually. Streaming via tile/chunk loading.

## Reference navigation

Read only the references needed for the current task:

- **Preproduction and planning:** [references/preproduction.md](references/preproduction.md)
- **Universal architecture (engine-agnostic):** [references/universal-architecture.md](references/universal-architecture.md)
- **Engine selection matrix:** [references/engine-selection.md](references/engine-selection.md)
- **Unreal architecture and input:** [references/unreal-architecture.md](references/unreal-architecture.md)
- **World building and streaming (universal + Unreal example):** [references/worldbuilding.md](references/worldbuilding.md)
- **Assets, import, licensing, and materials:** [references/asset-pipeline.md](references/asset-pipeline.md)
- **Gameplay systems and feature slices:** [references/gameplay-systems.md](references/gameplay-systems.md)
- **Testing, profiling, and packaging:** [references/quality-and-performance.md](references/quality-and-performance.md)
- **DroneVerse-specific adaptation (Unreal example):** [references/droneverse-adaptation.md](references/droneverse-adaptation.md)
- **Reusable project documents:** [references/templates.md](references/templates.md)

## Required milestone output

For each significant milestone, produce a concise status record containing the goal, implemented systems, asset changes, build result, runtime evidence, tests run, known issues, and the next smallest safe step. Do not report completion without evidence.

## Quality bar

A milestone is production-ready only when it has a coherent visual target, a playable loop, correct input, no critical runtime errors, documented asset provenance, acceptable performance on the target device, a reproducible build, and runtime or automated evidence. If any criterion is missing, report the milestone as incomplete and state the blocker.
