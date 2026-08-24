# Engine Selection Matrix & Decision Tree

Choose the engine that matches the player fantasy, target hardware, team architecture, and performance budget. Do not reverse-engineer game design to justify a preferred engine.

---

## 1. Engine Comparison Matrix

| Engine | Ideal Strengths | Primary Trade-Offs | Best For |
|---|---|---|---|
| **Unreal Engine 5.4+** | Nanite, Lumen, World Partition, Mass Entity, GAS, Chaos Physics, AAA rendering pipeline. | Heavy disk/build footprint, high C++ compilation times, high baseline hardware requirements. | Photorealistic 3D, large open worlds, systemic vehicular simulators, high-end PC/Console. |
| **Unity 6 / DOTS** | Cross-platform reach (Mobile, Switch, PC, Console, WebGL), Burst Compiler, C# productivity, huge asset store. | Render pipeline fragmentation (URP vs HDRP), manual memory/GC discipline required in MonoBehaviours. | Cross-platform titles, mobile mid-core, 2D/3D stylized, fast prototyping to production. |
| **Godot 4.3+** | MIT licensed, lightweight (<100MB), zero royalty, instant startup, fast iteration with GDScript, clean 2D/3D. | Smaller AAA rendering toolchain, fewer out-of-the-box AAA physics/streaming systems. | Indie games, 2D pixel/vector, lightweight 3D, open-source projects, desktop/mobile/web. |
| **Roblox Studio** | Built-in authoritative multiplayer, cloud infrastructure, instant social distribution, Luau scripting. | Walled garden platform, 30% revenue model, constrained low-level rendering control. | Social multiplayer, live-service multiplayer, rapid viral social games for young audiences. |
| **Web / Custom (Three.js/Babylon/Bevy)** | Zero install friction in browser, full control of engine loop and memory layouts (Rust/Wasm/WebGPU). | You build your own editor, DCC tools, UI frameworks, and physics pipelines. | Browser-native games, interactive simulations, custom engine research. |

---

## 2. Decision Tree

```
1. Is instant web browser execution without install non-negotiable?
   ├── YES ──> Choose Web/Three.js/Babylon (or Godot Web export for 2D).
   └── NO  ──> Proceed to 2.

2. Does the game require instant social multiplayer with zero server hosting costs?
   ├── YES ──> Choose Roblox Studio.
   └── NO  ──> Proceed to 3.

3. Does the game require photorealistic graphics, continuous open-world streaming (Nanite/Lumen/World Partition)?
   ├── YES ──> Choose Unreal Engine 5.
   └── NO  ──> Proceed to 4.

4. Is the project primarily 2D or lightweight 3D with a strong open-source / zero-royalty mandate?
   ├── YES ──> Choose Godot 4.3+.
   └── NO  ──> Choose Unity 6 (or Godot 4.3 depending on C# vs GDScript preference).
```

---

## 3. Anti-Patterns & Misconceptions

- **Overkill Anti-Pattern:** Picking Unreal Engine 5 for a 2D mobile puzzle game (inflates build size to 500MB+ with massive battery drain).
- **Underpowered Anti-Pattern:** Picking a lightweight 2D engine for a dense photorealistic 50km² open-world simulation without dedicated streaming infrastructure.
- **Platform Mismatch:** Picking a walled garden UGC platform for an offline single-player story with no online features.
