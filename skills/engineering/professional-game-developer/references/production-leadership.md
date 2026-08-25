# Production Leadership & Engineering Governance — Senior Level

A senior engineer ships games by establishing clear architectural boundaries, enforcing rigorous definitions of done, and protecting the team against technical debt.

---

## 1. The Strict Definition of Done (DoD)

A feature or milestone is **DONE** only when all four conditions are satisfied:

```
┌─────────────────────────────────────────────────────────────┐
│                 Senior 4-Point Definition of Done           │
├─────────────────────┬───────────────────────────────────────┤
│ 1. Build Proof      │ Clean compilation, zero error codes,  │
│                     │ automated packaging succeeds.         │
├─────────────────────┼───────────────────────────────────────┤
│ 2. Runtime Proof    │ Feature works in clean standalone     │
│                     │ runtime build (not just editor PIE).  │
├─────────────────────┼───────────────────────────────────────┤
│ 3. Performance Proof│ Operates within CPU/GPU frame-time    │
│                     │ budget on target hardware.            │
├─────────────────────┼───────────────────────────────────────┤
│ 4. Test Proof       │ Automated unit/integration tests pass │
│                     │ with regression test coverage.        │
└─────────────────────┴───────────────────────────────────────┘
```

*Rule:* If any of these four criteria is missing, the milestone is **Incomplete**. Never report a feature as complete based on editor viewport previews.

---

## 2. Code Review & Architecture Boundary Rules

When reviewing gameplay or engine code, enforce these architectural invariants:

1. **Single Source of Truth:** Every gameplay rule must have exactly one owner class. Never duplicate the same rule in both C++ and Blueprint/visual scripting.
2. **Failure Fallbacks:** Every external call (Asset Streaming, Network RPC, Hardware I/O, AI Prediction) must have an explicit, non-blocking fallback path.
3. **No Hidden Globals:** Disallow unobservable global singletons. Use explicit dependency injection, Service Locators with debug logging, or lifetime-scoped Subsystems.
4. **Data Isolation:** Gameplay rules must not directly reference transient visual meshes, materials, or audio cue assets.

---

## 3. Technical Debt Tracking Policy

Track technical debt explicitly in code with tagged identifiers linked to the project risk register:

```cpp
// TECH-DEBT(R-04): Temporary synchronous asset load.
// Must be migrated to Addressables asynchronous handle before Milestone 03.
// Owner: @systems-lead | Target Resolution: Sprint 14
```

- Allocate **20% of engineering bandwidth per sprint** strictly to resolving tagged technical debt items.
- Block merges that introduce untracked hacks or workarounds without an associated risk ID.
