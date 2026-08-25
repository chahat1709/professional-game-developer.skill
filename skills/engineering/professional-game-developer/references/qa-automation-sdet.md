# QA Automation, SDET & Soak Testing — Senior SDET Engineer

This reference details the implementation of automated headless test bots, overnight soak testing clusters, memory leak detection, and continuous integration regression testing.

---

## 1. Automated Headless Test Bot Architecture

Instead of relying solely on manual playtesters, build headless virtual client bots to stress-test gameplay systems:

```
[ Headless Client Process ] ──> [ Simulated Player Controller ]
                                           │
                                ┌──────────┴──────────┐
                                ▼                     ▼
                    [ Deterministic Input Plan ]  [ NavMesh Goal Navigation ]
                                │                     │
                                └──────────┬──────────┘
                                           ▼
                                [ Execute Gameplay Loop ]
                                           │
                                           ▼
                                [ Assert Verification Matrix ]
                                  • Check Health Invariants
                                  • Verify Score Increases
                                  • Assert Zero Memory Leaks
```

---

## 2. Overnight Soak & Stress Testing Clusters

Soak testing runs builds for continuous 8-to-24 hour periods under heavy concurrency to catch insidious memory leaks, thread deadlocks, and floating-point precision drift:

```
┌─────────────────────────────────────────────────────────────┐
│                    Soak Testing Invariants                  │
├─────────────────────┬───────────────────────────────────────┤
│ Continuous Duration │ 12 - 24 Hours continuous simulation   │
├─────────────────────┼───────────────────────────────────────┤
│ Memory Growth Limit │ Heap growth must stay <= 1.0 MB/hour  │
│                     │ (Zero unbounded allocation leaks)     │
├─────────────────────┼───────────────────────────────────────┤
│ Frame Stability     │ Frame time standard deviation < 1.5ms │
│                     │ across entire 24-hour run             │
├─────────────────────┼───────────────────────────────────────┤
│ Zero Soft-Locks     │ Zero unhandled exceptions, zero thread│
│                     │ deadlocks, zero NaN coordinate errors │
└─────────────────────┴───────────────────────────────────────┘
```

---

## 3. Automated Memory Leak & Allocation Tracking

- **Native Allocation Hooks:** Hook engine memory allocators (e.g. `FMemory::Malloc`, `malloc`, `HeapAlloc`) with allocation callstack capture.
- **Snapshot Comparison:**
  ```
  1. Take Baseline Memory Snapshot after Level Initialized (Snapshot A).
  2. Run 100 iterations of Gameplay Loop (Spawn Entity -> Move -> Despawn Entity).
  3. Force Full Garbage Collection.
  4. Take Final Memory Snapshot (Snapshot B).
  5. Diff(Snapshot B, Snapshot A) == 0 bytes.
     If Diff > 0: Report exact leaked object types and allocation callstacks.
  ```

---

## 4. Headless CI Integration Matrix

```bash
# Example Headless Automated Smoke Test Runner (Unreal Gauntlet)
RunUAT.sh RunUnattendedTests -project="$PROJECT" -test="Game.AutomatedSoakTest" -log -ReportExportPath="$PWD/Build/Reports"

# Example Headless Godot GUT Automated Suite
godot --headless -s addons/gut/gut_cmdln.gd -gdir=res://tests -gexit -glog=2
```
