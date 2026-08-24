# AI & Behavioral Systems Architecture — Senior AI Programmer

This reference establishes spatial perception, navigation mesh generation, pathfinding algorithms, decision-making architectures, and crowd avoidance for autonomous NPC agents.

---

## 1. Spatial Navigation: NavMesh & Hierarchical Pathfinding (HPA*)

```
┌─────────────────────────────────────────────────────────────┐
│                    Navigation Architecture                  │
├─────────────────────┬───────────────────────────────────────┤
│ Recast NavMesh      │ Voxelizes static scene collision into │
│ (Polygon Mesh)      │ 2D walkable convex polygon polygons   │
├─────────────────────┼───────────────────────────────────────┤
│ Hierarchical A*     │ Divides world into spatial clusters;  │
│ (HPA* / Macro Path) │ computes high-level portal path first,│
│                     │ then computes local polygon path      │
├─────────────────────┼───────────────────────────────────────┤
│ Funnel Algorithm    │ Converts jagged NavMesh polygon portal│
│ (String Pulling)    │ sequences into straight smooth paths  │
└─────────────────────┴───────────────────────────────────────┘
```

- **Dynamic Obstacle Avoidance (NavMesh Carving):** Carve dynamic physics obstacles (e.g. overturned trucks, locked gates) out of the runtime NavMesh using bounding box tile invalidation.

---

## 2. NPC Decision-Making Architecture Comparison

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       AI Decision Frameworks                                │
├─────────────────────┬───────────────────────────────────────────────────────┤
│ Behavior Tree (BT)  │ Hierarchical Composites (Sequence, Selector),         │
│                     │ Decorators (Preconditions), and Leaf Tasks.           │
│                     │ Best for: Tactical combat, squad cover, stealth.      │
├─────────────────────┼───────────────────────────────────────────────────────┤
│ Utility AI (Curves) │ Evaluates continuous mathematical response curves     │
│                     │ (0.0 to 1.0) for every available action.              │
│                     │ Best for: Ambient city citizens, survival sims.       │
├─────────────────────┼───────────────────────────────────────────────────────┤
│ StateTree (UE5.4+)  │ High-performance hierarchical state machine combining │
│                     │ state-flow transitions with tree selection speed.     │
│                     │ Best for: High-density systemic AI and crowds.        │
└─────────────────────┴───────────────────────────────────────────────────────┘
```

### Utility AI Scoring Math:
$$U_{\text{action}} = \prod_{i=1}^{N} f_i(x_i) \cdot w_{\text{action}}$$
where $f_i(x_i)$ is a normalized response curve (Linear, Exponential, or Logistic) evaluating an environmental condition (e.g. Health %, Distance to Enemy, Ammo Count).

---

## 3. Environmental Query System (EQS) & Tactical Spatial Queries

EQS queries spatial points in the world to find optimal tactical locations (Cover, Flanking, Line-of-Sight):

```
1. Generator: Spawn spatial point grid (e.g. 50 candidate points around NPC).
2. Filter Tests:
   • Discard points with no NavMesh projection.
   • Discard points within direct Line-of-Sight of player (Trace).
3. Score Tests:
   • Score = Distance(Point, CoverWall) * Weight_Cover + Distance(Point, Target) * Weight_Proximity.
4. Selection: Move agent to candidate point with highest composite score.
```

---

## 4. Crowd Simulation & Local Avoidance (RVO / ORCA)

When simulating hundreds of NPCs moving simultaneously without gridlock:

- **ORCA (Optimal Reciprocal Collision Avoidance):** Formulates collision avoidance as a half-plane optimization problem in velocity space.
- Each agent assumes other agents will take equal responsibility for half the required velocity adjustment:
  $$v_{\text{new}} \in \text{HalfPlane}(\vec{p}_A - \vec{p}_B, \vec{v}_A - \vec{v}_B, r_A + r_B)$$
- Solved in microseconds using 2D Linear Programming (Simplex / Half-Plane intersection).
