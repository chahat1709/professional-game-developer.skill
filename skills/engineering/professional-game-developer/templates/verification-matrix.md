# Verification Matrix

| Requirement | Code / Build Evidence | Runtime Evidence | Visual Evidence | Automated Test | Status |
|---|---|---|---|---|:---:|
| Vehicle Deterministic Physics | Clean compilation via UBT (0 errors) | 60 FPS flight loop in ProvingGrounds (16.2 ms) | Hero capture at `/Artifacts/Screenshots/hero.png` | `PhysicsAutomationTest` (14/14 Pass) | PASS |
| Enhanced Input Abstraction | Action mappings registered in IMC_Flight | Smooth transitions between Gamepad and KBM | Action debug prompt HUD widget active | `InputContextTests` (6/6 Pass) | PASS |
| Telemetry Export Pipeline | TelemetrySubsystem compiled cleanly | 3,600 JSON samples generated at 50 Hz | Live debug telemetry overlay active | `TelemetrySchemaTest` (Pass) | PASS |
