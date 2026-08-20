# Quality, Performance, and Shipping

Use this reference before calling a feature complete, before expanding content, and before packaging.

## Three evidence layers

1. **Build evidence:** compilation, UnrealHeaderTool, asset validation, Blueprint compilation, cooking, and packaging logs.
2. **Runtime evidence:** launch, input, gameplay loop, logs, save/telemetry output, errors, loading, recovery, and restart behavior.
3. **Visual evidence:** screenshots or captured video showing lighting, materials, composition, UI, effects, and representative gameplay.

All three are required for a production milestone.

## Test pyramid

| Test | Purpose | Run frequency |
|---|---|---|
| Unit/automation | Pure logic, schemas, math, parsing, model contracts. | Every build or change. |
| Smoke | Fast project launch, map load, core subsystem initialization. | Every build. |
| Functional | Player-visible loop, objectives, physics, landing, mission completion. | Every milestone. |
| Content stress | Load maps, compile Blueprints, scan/import assets, stream cells, build PCG/HLOD. | Before content expansion and release. |
| Screenshot/visual | Detect lighting, composition, material, UI, and regression changes. | Visual milestones and release candidates. |
| Hardware | Device packet timing, disconnects, input ranges, fallback. | Hardware milestones and release candidates. |

## Runtime capture checklist

Capture the startup state, the core interaction, the success path, the failure/retry path, the UI/debug overlay, and the most demanding region. Include an on-screen build/version identifier when possible. Record the exact map, command line, hardware, settings, and asset revision.

## Performance budget

Define target frame time and separate CPU/GPU budgets. Track memory, streaming, shader compilation, draw calls, visible/loaded actors, Nanite/foliage instances, texture pool, physics cost, AI/inference time, telemetry overhead, and input latency. Profile at the worst expected density and fastest travel speed, not only in the empty test scene.

## Regression discipline

When a test fails, preserve the log and minimal reproduction. Fix the smallest root cause, rerun the failing test, then rerun the smoke suite. Do not hide warnings by disabling diagnostics. Distinguish engine/editor warnings from project failures and record accepted warnings.

## Packaging gate

Before packaging, confirm project version, maps, plugins, input bindings, configuration, asset credits, save compatibility, cooked content, runtime logs, external-device behavior, and clean-machine launch. Test a packaged build rather than relying on PIE. Keep the exact command and output location in the milestone record.

## Definition of done

A feature is done when it works from a clean launch, supports its intended inputs, survives its expected failure states, produces required telemetry/logs, meets the visual target, stays within performance budget, passes its tests, and has documented known limitations.
