# Advanced Physics & Numerical Simulation — Senior Physics Engineer

This reference details low-level numerical integration, constraint solving, continuous collision detection (CCD), Extended Position Based Dynamics (XPBD), softbody/cloth simulation, and fluid dynamics.

---

## 1. Numerical Time Integration Schemes

Physics stability depends entirely on numerical integration choice. Never use standard Explicit Euler in production physics solvers:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       Numerical Integrator Comparison                       │
├────────────────────┬──────────┬─────────────────┬───────────────────────────┤
│ Integrator         │ Accuracy │ Energy Stability│ Best Use Case             │
├────────────────────┼──────────┼─────────────────┼───────────────────────────┤
│ Explicit Euler     │ 1st Order│ Unstable (Gains)│ NEVER (Blows up easily)   │
│ Semi-Implicit Euler│ 1st Order│ Symplectic      │ Rigid bodies, game loops  │
│ Velocity Verlet    │ 2nd Order│ High Symplectic │ Particle & molecular sims │
│ RK4 (Runge-Kutta 4)│ 4th Order│ High (Damped)   │ Orbital & aerospace aero  │
│ XPBD               │ PBD-based│ Unconditionally │ Cloth, ropes, softbodies  │
└────────────────────┴──────────┴─────────────────┴───────────────────────────┘
```

### Mathematical Formulations:

#### A. Semi-Implicit (Symplectic) Euler:
Update velocity **first**, then use updated velocity to integrate position:
$$v_{t + \Delta t} = v_t + \frac{F_{\text{net}}}{m} \cdot \Delta t$$
$$x_{t + \Delta t} = x_t + v_{t + \Delta t} \cdot \Delta t$$

#### B. Extended Position Based Dynamics (XPBD):
XPBD solves constraints directly in position space, eliminating constraint stiffness variation across changing timesteps ($\Delta t$):
$$\Delta \lambda = \frac{-C(x) - \tilde{\alpha} \lambda}{\nabla C(x)^T \mathbf{M}^{-1} \nabla C(x) + \tilde{\alpha}}$$
$$\Delta x = \mathbf{M}^{-1} \nabla C(x) \Delta \lambda$$
where $\tilde{\alpha} = \frac{\alpha}{\Delta t^2}$ is the compliance matrix, $\mathbf{M}^{-1}$ is inverse mass, and $C(x)$ is the constraint error function.

---

## 2. Rigid Body Constraint Solvers (Sequential Impulses)

Modern physics engines (PhysX, Chaos, Havok, Box2D) solve contact and joint constraints using **Projected Gauss-Seidel / Sequential Impulses**:

```
For each Sub-Step (e.g. 4 sub-steps per frame):
  For each Velocity Iteration (e.g. 8 iterations):
    For each Contact / Joint Constraint:
      1. Compute Relative Velocity: v_rel = (v2 + w2 x r2) - (v1 + w1 x r1)
      2. Compute Constraint Error: J * v_rel + bias
      3. Compute Required Impulse: delta_lambda = -EffectiveMass * (J * v_rel + bias)
      4. Clamp Impulse to Friction Cone / Inequality Limits: lambda = max(0, lambda + delta_lambda)
      5. Apply Impulse to Linear & Angular Momentum
```

- **Baumgarte Stabilization:** Corrects positional penetration drift by adding a velocity bias:
  $$\text{bias} = \frac{\beta}{\Delta t} \cdot \max(0, \text{penetration} - \text{slop})$$
  where $\beta \in [0.1, 0.2]$ is the Baumgarte coefficient, and $\text{slop}$ is penetration allowance (e.g. $0.005\text{m}$).

---

## 3. Continuous Collision Detection (CCD) & Tunneling Prevention

High-speed fast-moving bodies (bullets, arrows, racing cars at 100+ m/s) will pass entirely through thin colliders within a single discrete timestep $\Delta t$.

```
Discrete Stepping (Tunneling Failure):
Time T:   [ Fast Bullet ] ──────────────────> | Solid Wall |
Time T+1:                                     | Solid Wall | ──> [ Fast Bullet ] (Missed Collision!)

Continuous Collision Detection (Swept Volume):
Time T to T+1: [ ══════════ Swept Capsule Ray / Convex Hull ══════════ ] ──X (Collision Detected at T + 0.42!)
```

### CCD Algorithms:
1. **Conservative Advancement:** Iteratively steps time forward by the minimum separation distance divided by maximum velocity until the distance is within tolerance $\epsilon$.
2. **GJK (Gilbert-Johnson-Keerthi) Swept Volume:** Computes distance between Minkowski differences of two swept convex hulls.
3. **EPA (Expanding Polytope Algorithm):** When penetration occurs, EPA expands a polytope on the Minkowski sum boundary to determine exact contact normal and penetration depth.

---

## 4. Soft Body, Cloth & Rope Simulation

Cloth meshes simulate thousands of interconnected distance, bending, and shear constraints using XPBD:

```
Distance Constraints (Structural):    Shear Constraints:           Bending Constraints:
  O ─────── O ─────── O                 O ─────── O                  O
  │         │         │                 │ ╲     ╱ │                 ╱ ╲
  │         │         │                 │   ╳   │                ╱     ╲
  O ─────── O ─────── O                 │ ╱     ╲ │               O ─────── O
  │         │         │                 O ─────── O                 (Angle constraint
  │         │         │                                              between 2 adjacent faces)
```

- **Wind & Aerodynamic Drag on Cloth:**
  $$F_{\text{aero}} = \frac{1}{2} \rho \cdot A \cdot |v_{\text{rel}}|^2 \cdot (C_L (\hat{n} \cdot \hat{v}_{\text{rel}}) + C_D (1 - |\hat{n} \cdot \hat{v}_{\text{rel}}|))$$
  where $v_{\text{rel}} = v_{\text{wind}} - v_{\text{particle}}$, $\hat{n}$ is face normal, $C_L$ is lift coefficient, and $C_D$ is drag coefficient.

---

## 5. Buoyancy & Shallow Water Simulation

### Voxel / Tetrahedral Water Buoyancy:
To simulate floating boats and debris:
1. Discretize the submerged hull into sample point probes or tetrahedral sub-volumes.
2. For each submerged sub-volume $V_i$ at depth $h_i$:
   $$F_{\text{buoyant}} = \rho_{\text{fluid}} \cdot V_i \cdot g \cdot \hat{u}$$
   $$F_{\text{hydrodynamic\_drag}} = -\frac{1}{2} \rho_{\text{fluid}} \cdot C_d \cdot A_i \cdot |v_i| \cdot v_i$$
3. Apply forces at each sub-volume center of mass, producing natural stabilizing righting torques (metacentric height stability).
