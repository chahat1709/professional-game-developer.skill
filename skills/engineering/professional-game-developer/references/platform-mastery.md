# Platform Mastery & Certification Gates — Senior Level

A senior engineer targets the real hardware platform from Day 1, not a high-end development PC.

---

## 1. Frame-Time & Memory Budgets by Platform

| Target Platform | Frame Target | Total Frame Budget | CPU Sim Budget | GPU Render Budget | Target RAM / VRAM Budget |
|---|:---:|:---:|:---:|:---:|:---:|
| **PC (Mid Spec - GTX 1660 / RTX 3060)** | 60 FPS | 16.6 ms | <= 7.0 ms | <= 8.5 ms | 6.0 GB RAM / 4.0 GB VRAM |
| **Current-Gen Console (PS5 / Xbox Series X)**| 60 FPS | 16.6 ms | <= 6.0 ms | <= 9.0 ms | 10.0 GB Unified Memory |
| **Mobile (iOS / Android Mid-Tier)** | 30 / 60 FPS| 33.3 / 16.6 ms | <= 10.0 ms | <= 12.0 ms | 1.8 GB RAM / Low Thermal Draw |
| **Web (WebGL2 / WebGPU)** | 60 FPS | 16.6 ms | <= 5.0 ms | <= 9.0 ms | 512 MB Heap / 50 MB Assets |

---

## 2. Platform Certification & Compliance Gates

### Console Requirements (Sony TRC / Microsoft XR):
- **Controller Disconnect:** If an active wireless controller disconnects during gameplay, immediately trigger pause menu with reconnect prompt.
- **Suspend / Resume:** Game state must recover cleanly from OS suspend/sleep mode without crashing audio/graphics threads.
- **Save Data Resilience:** Corrupted save files must be detected with checksum validation and fail gracefully without crashing the application.
- **Loading Screen Standards:** Any load screen > 2 seconds must display animated UI progress to prove the process is alive.

### Mobile Requirements (Apple App Store / Google Play):
- **Thermal Throttling Defense:** If device temperature triggers thermal throttling, automatically drop dynamic resolution scaling (DRS) or cap frame rate to 30 FPS to prevent hardware shutdown.
- **Interruption Handling:** Handle phone calls, backgrounding, and lock-screen transitions with automatic game pause and state caching.
- **Cold Boot Time:** Cold launch to interactive title screen must take `< 10 seconds`.

---

## 3. Profiling Execution Loop

```
1. Run target build on real target hardware (DevKit / Physical Phone / Min-Spec PC).
2. Record worst-case gameplay sequence (e.g. maximum particle combat inside dense foliage region).
3. Identify the Primary Bottleneck:
   - CPU Bound: Optimize physics broadphase, script allocations, AI pathfinding queries, or tick rates.
   - GPU Bound: Optimize shadow cascade splits, quad-overdraw, translucent blending, or shader ALU ops.
   - Memory Bound: Downscale texture MIP-maps, compress meshes, enable mesh streaming or GC pooling.
4. Verify fix with direct before/after frame-time deltas (in milliseconds).
```
