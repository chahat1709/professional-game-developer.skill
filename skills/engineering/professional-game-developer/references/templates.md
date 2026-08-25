# Reusable Project Templates — Canonical Schemas

Use these canonical templates when starting projects, tracking risks, validating assets, and delivering milestone verification reports.

---

## 1. Project Brief Template

```markdown
# Project Brief — [Game / System Name]

## Player fantasy
[What the player does and why it feels compelling]

## Core loop
1. **[Step 1 - Spawn/Setup]:** [Action]
2. **[Step 2 - Traversal/Action]:** [Action]
3. **[Step 3 - Challenge/Encounter]:** [Action]
4. **[Step 4 - Feedback/Reward]:** [Action]
5. **[Step 5 - Restart/Progression]:** [Action]

## Platform and inputs
- **Hardware Target:** [PC / Console / Mobile / Web]
- **Input Modalities:** [Gamepad, Keyboard/Mouse, Touch, Custom Device]
- **Target Performance:** [60 FPS (16.6ms) / 30 FPS (33.3ms)]

## Visual target
[Reference images, palette, materials, lighting, density, and camera composition]

## Systems
[Physics, Input Abstraction, AI, Progression, UI/HUD, Telemetry, Persistence]

## Vertical slice
[One representative location + one complete gameplay loop proving the core loop]

## Acceptance criteria
- [ ] [Concrete observable condition]
- [ ] [Concrete observable condition]
- [ ] [Concrete observable condition]

## Out of scope
[Explicitly excluded features for this milestone]
```

---

## 2. Risk Register Template

```markdown
# Risk Register

| ID | Risk | Impact | Likelihood | Experiment | Evidence | Fallback | Status |
|---|---|:---:|:---:|---|---|---|:---:|
| **R-01** | [Description of risk] | High | High | [Proof experiment] | [Metric log] | [Architectural fallback] | Open |
```

---

## 3. Asset Manifest Template (Canonical 11 Columns)

```markdown
# Asset Manifest

| Asset ID | Source | Creator | License | Attribution | Format | Destination | Scale | Collision | Nanite/LOD | Validation |
|---|---|---|---|---|---|---|---|---|---|---|
| SM_Rock_Granite_01 | https://ambientcg.com/a/Rock01 | ambientCG | CC0-1.0 | None required | GLB | /Content/Environment/Rocks | 1.0 (cm) | UCX custom hull | Nanite Enabled | Pass |
```

---

## 4. Milestone Report Template (8 Required Sections)

```markdown
# Milestone: [Name]

## Goal
[State what this milestone proves in measurable terms]

## Implemented
[Detailed list of implemented systems, components, shaders, and assets]

## Build evidence
Build command: `[CLI Build / Automation Command]`
Result: [Compilation result, warnings, exit code]

## Runtime evidence
[Runtime loop performance, FPS/frame times, memory allocations, telemetry logs]

## Visual evidence
[Paths to captured screenshots, video runs, or visual regression comparisons]

## Tests
[Automated unit, integration, and contract test counts and pass/fail results]

## Known issues
[Explicit technical debt and non-blocking limitations]

## Next smallest safe step
[One focused, immediately actionable next engineering step]
```

---

## 5. Verification Matrix Template

```markdown
# Verification Matrix

| Requirement | Code / Build Evidence | Runtime Evidence | Visual Evidence | Automated Test | Status |
|---|---|---|---|---|:---:|
| [System Requirement] | [Compiler log / status] | [FPS / Telemetry metric] | [Screenshot path] | [Test name] | PASS/FAIL |
```
