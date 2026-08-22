# Universal Architecture

Use when designing any game, regardless of engine. Map these concepts to your engine's idioms.

## Game loop (engine-agnostic)

```
input → fixed-tick simulation → variable render → present
```

- Keep simulation at a fixed timestep (e.g., 50–60 Hz) for deterministic physics/rules. Render can be variable.
- Order ticks deterministically: input → AI/decision → physics/movement → collision → rules/scoring → animation → camera → UI/feedback → persistence.
- Make reset/replay reproducible: seed RNG, log initial conditions, allow deterministic test input.

## Composition over inheritance

- **Entity** = presence in the world (a thing with a transform). No deep inheritance.
- **Component** = reusable capability: Health, Mover, Thruster, Inventory, Interactable, TelemetryLogger. Attach to entities.
- **System/Subsystem** = lifetime-scoped service: SaveService, PhysicsService, InputService, TelemetryService. One responsibility each.
- **Data asset/config** = tuning without code changes: weapon stats, biome rules, mission definitions, difficulty curves. Version them.

```
Entity ── has ── Components (data + behaviour)
Systems ── operate on ── Entities with required Components
Data Assets ── configure ── Systems and Components
```

## Scene, world, and persistence

- **Session** = data that survives level/scene changes (player profile, settings, save). Keep in a session-scoped service (GameInstance / Autoload / DontDestroyOnLoad holder).
- **Level/Scene** = rules and spawn for the current space. Keep in the level-scene owner (GameMode / Scene root / WorldBootstrap).
- **Player/Peer state** = per-player score/progression/identity. Do not put physics there.

## Input abstraction

Define named **actions by intent**, not by key:

- `Move`, `Look`, `Jump`, `Sprint`, `Interact`, `Use`, `Map`, `Pause`

Map many devices to the same action:

- Keyboard WASD → Move
- Gamepad left stick → Move
- Touch joystick → Move
- Hardware/ESP32 axes → Move (validated, smoothed, timeout)

Add dead zones, sensitivity, inversion, context switching (on foot vs in vehicle vs in menu). Test each device alone and together. If hardware stops sending packets, fall back to keyboard/gamepad within N ms.

## Persistence and telemetry

- Version every save structure (`saveVersion = 3`). Migrate old saves, never serialize raw pointers.
- Define units once: meters, cm, studs, seconds, degrees/radians, coordinate handedness.
- Telemetry: timestamp + sessionId + source device + schemaVersion + sampling rate. Separate high-rate samples from events. Keep logs appendable; survive crashes/partial sessions.

## Testability

Ask before coding:

- Which class owns this rule? Which data survives a scene change? What can be tested without rendering? What breaks if the asset fails to load or the device disconnects? What log proves initialization?

## Mapping to engines

| Universal | Unreal | Unity | Godot | Roblox |
|---|---|---|---|---|
| Session service | GameInstance | DontDestroyOnLoad Service | Autoload | Server Replicated + Player data |
| Level rules | GameMode | Scene Manager | Main scene root | Server WorldBootstrap |
| Player state | PlayerState | PlayerData SO | Player resource | Player object + leaderstats |
| Decision/input | Controller | Input + Player Input | Input handler node | PlayerScripts + ContextAction |
| Presence | Pawn/Character | GameObject/Entity | Node/CharacterBody | Model/Character |
| Capability | ActorComponent | MonoBehaviour Component | Node Component | Component (e.g., CollectionService tag) |
| Service | Subsystem | Manager/ServiceLocator | Autoload | ModuleService |
| Tuning data | DataAsset | ScriptableObject | Resource | Module + Attributes |
