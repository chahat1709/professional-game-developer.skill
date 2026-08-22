# Roblox Architecture — Senior Level

## Responsibility map

| Layer | Owns | Avoid |
|---|---|---|
| Server (ServerScriptService, Workspace) | Authority, physics, scoring, mission completion | Client-trusted gameplay |
| Client (PlayerScripts, ReplicatedStorage) | Input, camera, UI presentation | Authoritative rules |
| ReplicatedStorage | Shared definitions, configs, remotes | Server secrets |
| DataStore / MemoryStore | Persistence, session data (versioned) | Transient pointers |

## Senior patterns

- **Authority:** server owns all gameplay. Client sends intent via RemoteEvent (`RequestMove`, `RequestLand`), server validates range/rate/cooldown then applies. Never trust client physics.
- **Input:** ContextActionService + UserInputService — named actions (`Throttle`, `Yaw`) mapped to keyboard/gamepad/touch; same action path with timeouts + fallback.
- **Assets:** FBX import via Content Manager — collision fidelity Box/Hull, scale in studs, StreamingEnabled + LOD for large maps; keep visual mesh separate from gameplay proxy (LandingZone part).
- **Performance:** MicroProfiler + console, StreamingEnabled, LOD, texture budgets; test on low-end mobile, not just Studio.
- **Testing:** Studio Play + Team Test, server/client logs, data migration tests for DataStore version changes.
