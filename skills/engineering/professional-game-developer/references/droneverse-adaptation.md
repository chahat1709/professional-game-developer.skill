# Vehicle Simulation Case Study: Flight & Quadrotor Systems

Use this reference as a concrete practical case study for implementing high-performance vehicle simulation, telemetry streaming, external hardware I/O (e.g. ESP32), and landing prediction in Unreal Engine 5 or custom physics pipelines.

---

## 1. Physical Architecture Contract

- **`AVehiclePawn` / `ADronePawn`:** Authoritative owner of aerodynamic forces, thruster torques, motor RPM integration, and collision resolution.
- **`VehicleInputComponent`:** Normalizes inputs across multiple input modalities (Keyboard, Gamepad, Touch, External Serial/ESP32) into unified continuous action vectors `(-1.0 to 1.0)`.
- **`LandingZoneActor`:** Independent collision volume responsible for touchdown evaluation, slope angle calculation, and scoring.
- **`TelemetrySubsystem`:** Samples flight kinematics at fixed intervals (e.g. 50 Hz) and streams JSON/binary records to analytics sinks.

---

## 2. Assisted Landing & Prediction Subsystem

When implementing AI or heuristic-based assisted landing:

```
[ Altitude & Velocity Sensors ] ──> [ Landing Prediction Subsystem ]
                                                │
                                    ┌───────────┴───────────┐
                                    ▼                       ▼
                         [ Heuristic Safety Check ] [ Neural Model Inference ]
                                    │                       │
                                    └───────────┬───────────┘
                                                ▼
                                    [ State: SAFE / WARNING / CRITICAL ]
                                                │
                                    [ HUD / Viewport Overlay ]
```

- **Deterministic Fallback:** If inference fails or drops below latency thresholds (>20 ms), fall back to deterministic kinematic safety rules immediately.
- **Touchdown Metrics:** Evaluate landing quality using:
  - Vertical Descent Rate: $< 1.5 \text{ m/s}$ (Safe), $1.5 - 3.0 \text{ m/s}$ (Warning), $> 3.0 \text{ m/s}$ (Critical / Crash).
  - Pitch / Roll Deviation: $< 5.0^\circ$ from horizontal plane.
  - Horizontal Radial Offset: Distance from landing pad center origin.

---

## 3. External Hardware I/O Integration (ESP32 / Serial Protocol)

- **Protocol:** Ingest fixed-size binary packets (e.g. 32-byte frames with sync header `0xAA55` and CRC16 checksum).
- **Asynchronous Threading:** Poll serial port in a dedicated background worker thread; push validated control frames into a thread-safe ring buffer.
- **Watchdog Timer:** If no valid packet is received for $> 100 \text{ ms}$, flag device disconnect and transition smoothly to gamepad/keyboard control.
