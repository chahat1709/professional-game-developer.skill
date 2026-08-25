# Universal Game Architecture — Engine-Agnostic Core

This reference outlines the fundamental architectural laws that govern high-performance, deterministic game development across any engine or custom C++/Rust/Web tech stack.

---

## 1. The Core Game Loop: Fixed Simulation vs. Variable Render

```
                    ┌──────────────────────────────────────────────┐
                    │               Raw OS / Hardware Input        │
                    └──────────────────────┬───────────────────────┘
                                           │
                                           ▼
                    ┌──────────────────────────────────────────────┐
                    │          Input Buffer & Context Map          │
                    └──────────────────────┬───────────────────────┘
                                           │
             ┌─────────────────────────────┴─────────────────────────────┐
             ▼                                                           ▼
┌─────────────────────────┐                                 ┌─────────────────────────┐
│   Fixed Simulation Loop │                                 │  Variable Render Loop   │
│   (e.g., 50 Hz / 60 Hz) │                                 │  (e.g., 60 - 240+ Hz)   │
├─────────────────────────┤                                 ├─────────────────────────┤
│ • Integrate Forces      │                                 │ • Interpolate State     │
│ • Resolve Collisions    │ ─── (Interpolation Buffer) ───> │ • Culling & Draw Calls  │
│ • State Machine Ticks   │                                 │ • Shader Dispatches     │
│ • Rule / Score Updates  │                                 │ • UI / HUD Draw         │
│ • Network Replication   │                                 │ • Frame Presentation    │
└─────────────────────────┘                                 └─────────────────────────┘
```

### Determinism Rules:
- **Never compute gameplay rules or physics with variable `renderDeltaTime`:** Variable frame delta causes divergent simulation across different refresh rates (60 Hz vs 144 Hz).
- **Use an accumulator loop:** Accumulate real elapsed time and consume it in fixed simulation steps (e.g. `dt = 0.02s` for 50 Hz or `0.0166s` for 60 Hz).
- **Interpolate presentation:** In the render loop, interpolate transforms between `PreviousSimulationState` and `CurrentSimulationState` using the alpha remainder ratio.

---

## 2. Data-Oriented Design (DOD) & Memory Layout

Senior game development designs around the **CPU cache hierarchy** (L1/L2/L3 cache lines):

```
Object-Oriented (Array of Structures - Chases Pointers):
[ Entity A | Transform | Health | Physics | AI | Mesh | Audio ] ── (Cache Miss) ──> [ Entity B | ... ]

Data-Oriented (Structure of Arrays - Contiguous Sequential Access):
Transforms:  [ Pos A | Pos B | Pos C | Pos D | Pos E | Pos F ]  <-- Streamed in single 64-byte Cache Line
Velocities:  [ Vel A | Vel B | Vel C | Vel D | Vel E | Vel F ]
Health:      [ HP A  | HP B  | HP C  | HP D  | HP E  | HP F  ]
```

### Memory Rules:
1. **Contiguous Allocation:** Allocate bulk data in flat arrays or memory arenas. Avoid allocating individual objects via dynamic heap (`malloc`/`new`) in frame loops.
2. **Component Separation:** Separate high-frequency data (Transforms, Velocities) from low-frequency data (Inventory, Quest State, Cosmetics).
3. **Zero Dynamic Allocation in Simulation:** Pre-allocate object pools and buffers during scene loading. Re-use slots via generational indices.

---

## 3. Layered Responsibility Model

| Layer | Responsibility | State Lifespan | Allowed Dependencies |
|---|---|---|---|
| **Foundation / Kernel** | Math, memory allocators, ring buffers, profiling hooks. | Application | None |
| **Subsystems / Services** | Telemetry, Save/Load, Asset Streaming, Audio, Netcode. | Process / Session | Foundation |
| **Authoritative Simulation** | State machines, physics solvers, rules, scoring. | Level / Match | Subsystems, Foundation |
| **Presentation & View** | Render meshes, particle VFX, audio cues, HUD. | Transient / Frame | Reads Simulation State |
| **Input / Controller** | Device polling, action mapping, smoothing. | Session | Dispatches to Simulation |

---

## 4. Input Abstraction & Intent Mapping

Decouple physical hardware buttons from gameplay intent:

```
[ Physical Devices ]
• Keyboard / Mouse
• Gamepad (XInput / DualSense)  ──>  [ Input Context Manager ]  ──>  [ Named Actions ]
• Touchscreen / Mobile                 • Deadzone Filters             • Move (Vector2)
• External Hardware (ESP32)            • Acceleration Curves          • Look (Vector2)
                                       • Timeout / Fallback           • Interact (Trigger)
```

- **Device Fallback:** If a hardware controller stops receiving packets for >100 ms, automatically failover to Keyboard/Gamepad without dropping the active session.
- **Action Buffering:** Buffer jump/interact actions for 100–150 ms ahead of valid execution window to ensure responsive game feel.

---

## 5. Persistence, Telemetry & Determinism

- **Versioned Save Schemas:** Store version headers (`uint32 SchemaVersion = 3`). Provide forward migration parsers for legacy save formats.
- **Structured Telemetry:** Emit append-only structured events:
  ```json
  {
    "timestamp_ms": 1724490000120,
    "session_id": "sess_8941f",
    "event": "TOUCHDOWN_EVALUATED",
    "payload": {
      "velocity_mps": 0.42,
      "pitch_deg": 1.2,
      "roll_deg": -0.8,
      "result": "SAFE"
    }
  }
  ```
- **Seeded Pseudo-Random Number Generation (PRNG):** Never use unseeded system entropy (`rand()`) for gameplay generation. Use seeded Xoroshiro128+ or PCG PRNG to guarantee reproducible replays.
