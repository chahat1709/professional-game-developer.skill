# Unity Architecture — Senior Level

## Responsibility map

| Layer | Owns | Avoid |
|---|---|---|
| Scene + Bootstrap | Scene load, spawn policy, Addressables streaming | Persistent player data |
| GameObject + Components | Physical presence, collision, movement | Global rules |
| ScriptableObject | Data assets, mission/vehicle/biome config | Logic with side effects |
| Manager/Service (DontDestroyOnLoad or DI) | Save, session, telemetry, pool | Per-scene actor refs |
| UI (UGUI/UI Toolkit) | Presentation, feedback | Authoritative rules |

## Senior patterns

- **Input:** Input System package — Input Actions by intent (`Move`, `Look`) + Action Maps + control schemes + processors (dead zone, scale). Test keyboard/mouse/gamepad/touch separately.
- **Assets:** URP/HDRP — one master Shader Graph + instances; Addressables for large worlds; LODGroup + Occlusion Culling; texture import presets (sRGB/linear, max size, compression).
- **Architecture:** composition via components; managers as pure services with interfaces; data-driven via ScriptableObjects — no hard-coded constants in MonoBehaviours.
- **Performance:** Profiler + Frame Debugger + Memory Profiler; batch by material, atlas textures, GPU instancing; profile on target device.
- **Testing:** EditMode + PlayMode tests, deterministic tick tests without rendering.
