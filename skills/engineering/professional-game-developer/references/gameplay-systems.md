# Gameplay Systems & Simulation — Senior Level

## 1. Vehicle Physics & Raycast Dynamics

For realistic vehicle mechanics (ground vehicles, aircraft, quadrotors), avoid simplistic rigid-body torque hacking. Use **Raycast Suspension & Slip-Angle Friction Models**:

```
                       [ Vehicle Chassis (Rigid Body) ]
                                      │
          ┌───────────────────────────┴───────────────────────────┐
          │ (Raycast Spring-Damper)               │ (Raycast Spring-Damper)
          ▼                                       ▼
     ┌─────────┐                             ┌─────────┐
     │ Wheel 1 │                             │ Wheel 2 │
     └────┬────┘                             └────┬────┘
          │ (Pacejka 'Magic Formula' Slip Friction)│
          ▼                                       ▼
    [ Contact Patch ]                       [ Contact Patch ]
```

### Suspension Math:
```
SpringForce = RestLength - HitDistance
DamperForce = (PreviousLength - CurrentLength) / DeltaTime
SuspensionForce = (SpringForce * SpringStiffness) + (DamperForce * DampingFactor)
```

### Tire Friction Curve (Pacejka Magic Formula Approximation):
$$F_y = D \cdot \sin(C \cdot \arctan(B \cdot \alpha - E \cdot (B \cdot \alpha - \arctan(B \cdot \alpha))))$$
- $\alpha$: Slip angle (angle between tire heading and actual velocity vector).
- $B$: Stiffness factor.
- $C$: Shape factor.
- $D$: Peak friction force.
- $E$: Curvature factor.

---

## 2. Animation & Physical Ragdoll Blending

Senior character animation blends kinematic keyframes with dynamic physics simulation:

```
[ Root / Upper Body ] ── (Kinematic Keyframe Animation) ──┐
                                                          ├──> [ Blended Pose / Motor Forces ]
[ Limbs / Hit Response] ── (Active Physics Ragdoll) ──────┘
```

- **Physical Animation Component (UE / Unity):** Drive skeletal joints with PD (Proportional-Derivative) motor torques towards target animation poses.
- **Impact Reaction:** When a projectile or collision hits a limb, decrease motor drive strength locally to let momentum transfer naturally, then interpolate motor strength back to 1.0 to recover stance.

---

## 3. AI Architecture: Behavior Trees, Utility AI & StateTree

Choose the AI architecture that matches system complexity:

| AI Pattern | Best For | Mechanics |
|---|---|---|
| **Finite State Machine (FSM)** | Simple bosses, doors, basic turrets. | Explicit states (Idle, Chase, Attack) with transition guards. |
| **Behavior Tree (BT) + Blackboard** | Tactical combat, stealth NPCs, squad AI. | Hierarchical Composites (Sequence, Selector), Decorators (Conditionals), and Tasks. Shared Blackboard for memory. |
| **Utility AI (Score-Based)** | Sims, survival NPCs, ambient crowds. | Evaluates a mathematical utility score (0.0–1.0) across all candidate actions; executes highest-scoring behavior. |
| **StateTree (UE5.4+)** | High-performance systemic agents. | Compact, memory-efficient hierarchical state machine combining tree structure with state-flow speed. |

### Environmental Query System (EQS):
- Generate candidate spatial points around the NPC (e.g. grid / circle).
- Score points based on tests: Distance to Player, Line-of-Sight occlusion (Cover), Angle to target.
- Move agent to the highest-scoring candidate position.

---

## 4. Save/Load Architecture & Data Versioning

```json
{
  "header": {
    "magic_bytes": "GSAV",
    "schema_version": 3,
    "save_timestamp": 1724491200,
    "build_id": "v2.1.0-release"
  },
  "player": {
    "position": [1042.5, 450.2, 85.0],
    "rotation": [0.0, 0.707, 0.0, 0.707],
    "health": 85.0,
    "inventory": [
      {"id": "item_fuel_cell", "qty": 3},
      {"id": "item_repair_kit", "qty": 1}
    ]
  },
  "world_state": {
    "completed_missions": ["mission_desert_alpha", "mission_canyon_run"],
    "unlocked_fast_travel": ["poi_oasis_base"]
  }
}
```

- **Migration Policy:** When `schema_version` increments, run migration transformers (`Migrate_v1_to_v2()`, `Migrate_v2_to_v3()`).
- **Never serialize pointers:** Always store stable entity IDs or asset registry paths.
