# Unreal Architecture and Input

Use this reference when building or refactoring Unreal gameplay, input, UI, or persistent systems.

## Responsibility map

| Layer | Owns | Avoid |
|---|---|---|
| Game Instance | Cross-level session data, save manager, online/session services, long-lived subsystems. | Per-level actors or transient world references. |
| Game Mode | Rules, spawn policy, match/session setup, authority-side initialization. | Persistent player data or presentation logic. |
| Game State | State visible to the current session and, when relevant, replicated shared state. | Device-specific input handling. |
| Player State | Per-player score, progression, identity, inventory, or session stats. | Physical movement implementation. |
| Player Controller | Human input interpretation, possession, camera/UI coordination, interaction requests. | Storing the physical player body. |
| AI Controller | AI decisions, behavior/state trees, navigation requests, possession. | Rendering or mesh-specific logic. |
| Pawn/Character | Physical presence, collision, movement, animation hooks, sensors, cameras. | Global rules and save data. |
| Actor Component | Reusable capability such as health, telemetry, interaction, inventory, thrusters, or hardware input. | Unrelated cross-system orchestration. |
| Subsystem | Lifetime-scoped service: engine, game instance, world, local player, editor, or audio. | Hidden global state without diagnostics. |
| Data Asset/Struct | Tuning, definitions, tables, mission/vehicle/biome configuration. | Hard-coded gameplay constants scattered through code. |
| UI/HUD | Presentation, player feedback, input prompts, debug overlays. | Owning authoritative rules. |

## C++ and Blueprint boundary

Use C++ for deterministic simulation, physics, serialization, device protocols, subsystem contracts, reusable components, and tests. Expose safe, narrow properties and functions for tuning. Use Blueprint for level composition, visual asset assignment, animation state wiring, UI layout, and designer-facing iteration. If a rule must remain identical across many levels or platforms, keep its source of truth in C++ or a data asset.

## Enhanced Input contract

Create named Input Actions by player intent, not by physical key. Use separate Mapping Contexts for common actions, flight, cockpit, menu, camera, gamepad, and hardware-controller modes. Define Axis1D/2D/3D values, dead zones, sensitivity, inversion, smoothing, triggers, and priority. Add or remove contexts when the player changes mode. Test keyboard, mouse, gamepad, and external input independently and together.

For a drone, prefer actions such as `IA_Throttle`, `IA_Yaw`, `IA_PitchRoll`, `IA_CameraLook`, `IA_AssistLanding`, `IA_ResetDrone`, and `IA_ToggleTelemetry`. Map them to keyboard/gamepad first, then feed the same action path from ESP32 data rather than adding a second physics control implementation.

## UI and telemetry

Keep HUD widgets presentation-only. A telemetry provider or view-model should expose sanitized values such as altitude, speed, battery, wind, risk, correction vector, connection state, and mission objective. The HUD should not read random component internals or recalculate authoritative physics. Add a debug mode that displays raw values, timestamps, update age, and source device.

## Persistent data

Use explicit save-game structures and version them. Do not serialize transient actor pointers or imported asset paths without a migration strategy. Keep telemetry logs appendable and resilient to partial sessions. Define units, coordinate systems, timestamps, and schema version in the data contract.

## Architecture review questions

Before implementation, answer: Which class owns the rule? Which system survives a level change? Which values are replicated or saved? What can be tested without rendering? What can be replaced without changing gameplay? What logs prove the system initialized? What happens when the input device disconnects or the asset fails to load?
