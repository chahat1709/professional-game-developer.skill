# Risk Register

| ID | Risk | Impact | Likelihood | Experiment | Evidence | Fallback | Status |
|---|---|:---:|:---:|---|---|---|:---:|
| **R-01** | World streaming hitches exceed 16.6ms frame budget at 100m/s speed. | High | High | Run high-speed automated camera traversal across 4 streaming cells. | Frame time log < 16.6ms with zero streaming drops. | Reduce cell size and pre-fetch aggressive HLODs. | Mitigated |
| **R-02** | External serial controller packet jitter desyncs physics integrator. | High | Med | Ingest noisy mock hardware serial packets into physics loop. | Deterministic PID convergence with 50ms jitter. | Low-pass filter + auto-fallback to Gamepad. | Open |
