# Engine Selection

Choose the smallest engine that satisfies the fantasy, platform, team skill, and budget. Do not reverse-engineer the game to justify an engine.

## Quick matrix

| Engine | Strengths | Costs/limits | Best for |
|---|---|---|---|
| **Unreal 5** | Nanite, Lumen, World Partition, PCG, HLOD, AAA rendering, Blueprint + C++ | Heavy, large builds, C++ iteration, high-end hardware bias | Photoreal 3D, large open worlds, simulation-heavy (DroneVerse) |
| **Unity** | Cross-platform (mobile/PC/console/web), URP/HDRP, Addressables, huge asset store, C# | No built-in Nanite/Lumen equivalent, SRP complexity, license/runtime fee history | Cross-platform, mobile, 2D/3D mid-core, fast prototyping |
| **Godot 4** | MIT licensed, lightweight, GDScript+C#, 2D excellent, 3D competent, small builds | Smaller AAA toolchain, fewer high-end features, smaller hiring pool | Indie, 2D, lightweight 3D, open-source, fast iteration |
| **Roblox Studio** | Built-in multiplayer, avatar economy, instant distribution, Luau, UGC | Walled garden, 30% revenue share, rendering limits, policy constraints | Social multiplayer, UGC, teen audience, rapid social games |
| **Web/Custom** (Three.js/Babylon/Bevy) | Full control, web-native, ECS freedom, no engine lock-in | You build the editor/tools, no out-of-box physics/UI/shop | Web games, research, custom sims, engine learning |

## Decision checklist

1. **Platform:** Mobile → Unity/Godot/Roblox. Console/PC photoreal → Unreal/Unity HDRP. Web → Unity WebGL / Godot web / Three.js. Social UGC → Roblox.
2. **Team skill:** C++ team → Unreal. C# team → Unity/Godot. Small/solo → Godot/Roblox. No engine expertise → Godot or Roblox first.
3. **Visual target:** Stylized/low-poly → any. Photoreal open world → Unreal. 2D pixel → Godot/Unity 2D.
4. **Multiplayer:** Authority server needed? Roblox gives it free; Unreal/Unity/Godot require Netcode/Mirror/Godot Multiplayer + hosting.
5. **Budget/size:** <100 MB web game → Godot/Web. Large asset store reliance → Unity/Unreal.

## Anti-patterns

- Picking Unreal for a 2D mobile puzzle (overkill).
- Picking Godot for a Nanite-scale photoreal city without a custom pipeline.
- Picking Roblox for a single-player offline narrative with no social loop.
- Switching engines mid-vertical-slice without proving the loop in one engine first.

## Recommendation flow

Fantasy + platform + team + budget → pick engine → lock it before architecture → map universal architecture to that engine's idioms → prove one vertical slice before debating engine again.
