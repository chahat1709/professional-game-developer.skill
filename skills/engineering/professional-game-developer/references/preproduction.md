# Preproduction & Risk Management — Senior Level

## 1. The One-Page Project Brief

Before writing code or importing 3D models, lock the core constraints in a single-page brief:

```
┌─────────────────────────────────────────────────────────────┐
│                      Project Brief Contract                 │
├─────────────────────┬───────────────────────────────────────┤
│ Player Fantasy      │ What the player does and why it's fun │
│ Core Loop           │ Repeatable 5-step interaction loop    │
│ Target Platforms    │ PC / Console / Mobile / Web           │
│ Performance Budget  │ 60 FPS (16.6ms) / 30 FPS (33.3ms)     │
│ Input Modalities    │ Gamepad, KBM, Touch, Custom Device    │
│ Visual Benchmark    │ 3 Art Reference Target Images         │
│ Non-Negotiables     │ Core mechanics required for launch    │
│ Acceptance Criteria │ Concrete, testable conditions for DoD │
└─────────────────────┴───────────────────────────────────────┘
```

---

## 2. Risk-First Engineering & The Risk Register

Junior developers start with what is easy (menus, UI layouts, placeholder scenes). Senior engineers start with what can **kill the project**:

| Risk ID | System / Risk Description | Impact | Likelihood | Proof-of-Concept Experiment | Success Evidence Metric | Fallback Architecture |
|---|---|:---:|:---:|---|---|---|
| **R-01** | World streaming stalls at high flight speeds (100 m/s). | High | High | Stress-test high-speed camera traversal in empty world grid. | Max streaming frame hitch < 16.6 ms. | Reduce cell size and pre-fetch aggressive LODs. |
| **R-02** | External controller packet jitter causes physics instability. | High | Med | Ingest noisy mock hardware serial packets into physics loop. | Deterministic PID convergence with 50ms jitter. | Low-pass filter + auto-fallback to Gamepad. |
| **R-03** | Custom vehicle tire slip friction desyncs in multiplayer. | High | High | Run 2 headless client simulations with 150ms simulated ping. | Position divergence < 0.05m after correction. | Server authoritative rewind with client dead-reckoning. |

---

## 3. The Vertical Slice Contract

A **Vertical Slice** is a narrow, fully finished slice of the final game containing:
1. One fully realized environment section meeting 100% of the final visual bar (lighting, shaders, hero meshes).
2. The complete core gameplay loop (Input ──> Action ──> Challenge ──> Feedback ──> Reward ──> Save).
3. Production-ready audio cues, HUD feedback, and camera post-processing.
4. Measurable frame-time stability on the minimum target specification.

*Rule:* Never multiply content (e.g. 5 biomes, 20 vehicles, 50 missions) until the single vertical slice has satisfied all quality and performance gates.
