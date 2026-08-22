# Reusable Project Templates

Use these templates as starting points and adapt them to the project.

## Project brief

```markdown
# [Game / Feature]

## Player fantasy
[What the player does and why it matters]

## Core loop
1. [Start]
2. [Action]
3. [Challenge]
4. [Feedback/reward]
5. [Restart/progression]

## Platform and inputs
[Hardware, display, keyboard, mouse, gamepad, touch, external devices]

## Visual target
[References, palette, lighting, material, camera, density]

## Systems
[Movement, physics, AI, missions, UI, audio/VFX, saving, telemetry]

## Vertical slice
[One location + one complete loop]

## Acceptance criteria
- [Observable condition]
- [Observable condition]
- [Observable condition]

## Out of scope
[Explicit exclusions]
```

## Risk register

```markdown
| ID | Risk | Impact | Likelihood | Experiment | Evidence | Fallback | Status |
|---|---|---:|---:|---|---|---|---|
| R-01 | [Risk] | High | Medium | [Small test] | [Log/capture] | [Fallback] | Open |
```

## Asset manifest

```markdown
| Asset ID | Source | Creator | License | Attribution | Format | Destination | Scale | Collision | Nanite/LOD | Validation |
|---|---|---|---|---|---|---|---|---|---|---|
| [ID] | [URL] | [Name] | [Terms] | [Text] | [FBX/GLB] | [/Game/...] | [cm/axes] | [Policy] | [Policy] | [Result] |
```

## Milestone report

```markdown
# Milestone: [Name]

## Goal
[What this milestone proves]

## Implemented
[Systems, assets, maps, UI, tools]

## Build evidence
[Command, result, warnings/errors]

## Runtime evidence
[Map, command line, input, logs, save/telemetry]

## Visual evidence
[Screenshot/video/capture paths]

## Tests
[Smoke, functional, stress, hardware, visual]

## Known issues
[Honest limitations]

## Next smallest safe step
[One focused next step]
```

## Verification matrix

```markdown
| Requirement | Code/build | Runtime | Visual | Automated test | Result |
|---|---|---|---|---|---|
| [Requirement] | [Evidence] | [Evidence] | [Evidence] | [Test] | Pass/Fail |
```
