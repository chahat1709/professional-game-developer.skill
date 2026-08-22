# Platform & Performance Mastery

Senior ships on the target device, not on the dev PC.

## Budgets (lock before content)

- **Frame:** 60 Hz (16.6 ms) or 30 Hz (33.3 ms). Split CPU/GPU. If CPU > 8 ms, fix simulation/AI/physics; if GPU > 10 ms, fix shadows/materials/overdraw.
- **Memory:** define texture pool, mesh, audio, and code budgets per platform. On console/mobile, profile on device — PC profile lies.
- **Load:** cold start < 15 s, level transition < 5 s, hitch < 100 ms. Streaming budget = max actors/cells loaded at fastest traversal.

## Platform gates

- **Console (TRC/XR):** handle suspend/resume, controller disconnect, save corruption, age rating, crash reporting. Test on devkit with retail settings.
- **Mobile (iOS/Android):** handle interrupt (call), thermal throttle, low-memory kill, permission flow, store review (privacy, IAP). Test on low-end device, not flagship.
- **PC:** handle window resize, alt-tab, driver variance, settings scalability (Low→Epic must not crash). Verify on min spec.
- **Roblox/Web:** handle StreamingEnabled / asset streaming, rate limits, moderation, battery/thermal on mobile browsers.

## Profiling (senior loop)

1. Play worst-case path at max speed.
2. Capture: frame time, GPU pass cost, draw calls, instance counts, texture pool, streaming cells, physics time, memory.
3. Fix the top 1–2 hotspots, re-profile. Repeat. Do not micro-optimize before profiling.

## Certification checklist

- [ ] Clean launch, no critical errors, correct version/build id on screen.
- [ ] All inputs work, fallback on disconnect, no soft-lock.
- [ ] Saves migrate across versions, corrupted save recovers gracefully.
- [ ] Performance at budget on min spec/target device in worst region.
- [ ] Asset credits complete, licenses respected, no banned content.
