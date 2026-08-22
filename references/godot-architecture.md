# Godot Architecture — Senior Level

## Responsibility map

| Layer | Owns | Avoid |
|---|---|---|
| Main scene + Autoload | Session data, save, global services | Per-level actor refs |
| Node/Scene tree | Composition, presence, collision | Global rules |
| Resource | Data assets, tuning, mission defs | Scene-specific logic |
| Signals | Decoupled communication | Direct cross-node coupling |

## Senior patterns

- **Input:** Input Map — named actions (`move_forward`, `look`) + InputEvent handling + dead zones; same action path for keyboard/mouse/joypad/touch.
- **Assets:** Import dock for glTF/GLB — scale, collision shapes, LOD, StandardMaterial; Visibility + manual chunk streaming for large worlds; compress textures, use MultiMesh for instancing.
- **Architecture:** scene composition over inheritance; Autoload for session services; Resources for data-driven design; signals for system communication.
- **Performance:** Debugger + Profiler, reduce draw calls via batching, monitor Node count and physics ticks; test on target export (mobile/web).
- **Testing:** GdUnit/GUT, deterministic logic tests without rendering.
