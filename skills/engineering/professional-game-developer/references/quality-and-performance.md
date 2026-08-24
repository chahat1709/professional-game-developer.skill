# Quality, Performance & Automated Verification — Senior Level

## 1. The Three Evidence Layers

Before certifying any milestone or feature release, compile concrete evidence across three layers:

```
┌─────────────────────────────────────────────────────────────┐
│                   The Three Evidence Layers                 │
├─────────────────────┬───────────────────────────────────────┤
│ Layer 1: Build      │ Compiler outputs, packaging logs,     │
│                     │ zero cooking warnings, artifact hashes│
├─────────────────────┼───────────────────────────────────────┤
│ Layer 2: Runtime    │ Telemetry metrics, FPS frame logs,    │
│                     │ memory alloc traces, zero exceptions  │
├─────────────────────┼───────────────────────────────────────┤
│ Layer 3: Visual     │ High-resolution viewport captures,    │
│                     │ lighting/shader visual verifications  │
└─────────────────────┴───────────────────────────────────────┘
```

---

## 2. Automated Test Pyramid for Games

```
                      / \
                     /   \
                    / Visual\       --> Automated Screen Difference / RenderDoc Dumps
                   /  Diff   \
                  /───────────\
                 / Functional  \     --> Gauntlet / GUT / PlayMode In-Engine Loops
                / Integration   \
               /─────────────────\
              /  Unit & Contract  \   --> Math, Serialization, State Machines (Headless)
             /─────────────────────\
```

- **Unit / Automation Tests (Headless):** Fast, headless tests executing purely in CPU memory with no graphics device initialized (e.g. math tests, save migrations, network bitpacking). Run on every commit.
- **Functional Integration Tests:** Headless engine runs that spawn player pawns, simulate input scripts, and verify objective triggers and score resolution.
- **Visual Regression Tests:** Automated headless viewport renders compared against baseline gold images with perceptual hash algorithms to detect shader regressions.

---

## 3. Shipping & Packaging Checklist

Before building final release binaries:

- [ ] Project version and build ID embedded in runtime telemetry header and title screen.
- [ ] Debug consoles, cheat commands, and profiling hooks stripped from Shipping configuration.
- [ ] All external assets validated in Asset Manifest with approved licenses.
- [ ] Zero unhandled exceptions or memory leaks across a continuous 2-hour stress run.
- [ ] Save data backwards compatibility verified against previous release versions.
- [ ] Packaged build launches cleanly on a sterile machine with no editor dependencies installed.
