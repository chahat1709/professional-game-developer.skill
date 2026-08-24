# Animation Engineering & Character Mechanics — Senior Level

This reference details character kinematics, procedural inverse kinematics (IK), Motion Matching, inertialization blending, and animation runtime compression.

---

## 1. Modern Animation Blending: Inertialization vs. Crossfading

Traditional skeletal animation uses crossfading, evaluating two active animation clips simultaneously and interpolating between them, which doubles CPU bone transform calculation costs during transitions.

```
Traditional Crossfade (Expensive - 2 Active Animation Evals):
Anim A (Running)   ──────╲
                          ╳──────> Evaluates Both Skeletal Nodes Every Frame
Anim B (Stopping)  ──────╱

Inertialization Blending (High-Performance - Single Node Evaluation):
1. Immediately switch source to Anim B (New Animation).
2. Take snapshot of Bone Positions & Velocities at transition moment T_0.
3. Apply a decaying polynomial offset curve to smoothly carry inertial momentum into Anim B:
   x(t) = (A + B*t + C*t^2) * e^(-t / tau)
```

- **Benefits:** 50% lower CPU animation evaluation cost; eliminates foot-sliding and unnatural pop transitions.

---

## 2. Motion Matching & Pose Database Search

AAA locomotion (e.g. *The Last of Us Part II*, *GTA VI*, *Assassin's Creed*) replaces rigid state machines with **Motion Matching**:

```
[ Player Input Intent: Desired Trajectory (Next 1.0s) ]
                          │
                          ▼
[ Query Motion Database (KD-Tree / PCA Projection) ]
  • Match Future Trajectory Positions & Facings
  • Match Current Skeletal Pose (Foot Positions, Velocities)
                          │
                          ▼
[ Select Best Frame Match in Database ] ──> [ Inertialize Blend to Target Clip ]
```

- **Cost Function:**
  $$J = \sum_{i} w_{\text{traj}} |p_{\text{traj, query}} - p_{\text{traj, cand}}|^2 + \sum_{j} w_{\text{pose}} |p_{\text{bone, query}} - p_{\text{bone, cand}}|^2$$
- **KD-Tree / Dimension Reduction:** Compress the pose database into $16 - 32$ principal components using PCA (Principal Component Analysis) to query candidates in $< 0.05\text{ ms}$ per character.

---

## 3. Procedural Inverse Kinematics (IK) Hierarchy

Combine forward kinematic keyframes with procedural IK solvers:

```
┌─────────────────────────────────────────────────────────────┐
│                      IK Solvers for Games                   │
├───────────────────┬─────────────────────────────────────────┤
│ Two-Bone IK       │ Analytical, ultra-fast solver for arms  │
│                   │ and legs with hinge joint pole vectors  │
├───────────────────┼─────────────────────────────────────────┤
│ FABRIK            │ Forward And Backward Reaching Inverse   │
│                   │ Kinematics: Iterative solver for spines,│
│                   │ tails, tentacles, and multi-joint chains│
├───────────────────┼─────────────────────────────────────────┤
│ Look-At / Aim IK  │ Procedural head, spine, and gun aiming  │
│                   │ with angular clamp constraints          │
├───────────────────┼─────────────────────────────────────────┤
│ Foot Placement IK │ Raycast/Spherecast down from each foot; │
│                   │ adjust pelvis height and ankle pitch/   │
│                   │ roll to align with uneven terrain slopes│
└───────────────────┴─────────────────────────────────────────┘
```

### Foot IK Ground Clamping Algorithm:
1. Trace rays from each foot bone downwards towards terrain surface normal $\vec{N}_{\text{ground}}$.
2. Find the lowest foot contact point $h_{\text{min}} = \min(h_{\text{left}}, h_{\text{right}})$.
3. Lower the **Pelvis Bone** by $h_{\text{min}}$ so the lowest leg can plant naturally.
4. Execute **Two-Bone IK** on the opposite leg to reach the higher terrain elevation.
5. Rotate the foot bone transform to match $\vec{N}_{\text{ground}}$ with angular damping.

---

## 4. Animation Data Compression & Memory Optimization

Raw uncompressed skeletal animation (e.g. 60 FPS, 100 bones, 3D vectors + 4D quaternions) consumes $> 500\text{ KB}$ per second of animation.

```
┌─────────────────────────────────────────────────────────────┐
│              Animation Track Compression Pipeline           │
├───────────────────────┬─────────────────────────────────────┤
│ 1. Curve Decimation   │ Remove redundant keyframes on linear│
│    (Ramer-Douglas)    │ interpolation paths within tolerance│
├───────────────────────┼─────────────────────────────────────┤
│ 2. ACL (Animation     │ Segment tracks into 16-frame chunks;│
│    Compression Lib)   │ quantize translations to 16-bit int │
├───────────────────────┼─────────────────────────────────────┤
│ 3. Quaternion         │ Smallest Three encoding: store 3    │
│    Quantization       │ components in 48 bits (16 bits/comp)│
└───────────────────────┴─────────────────────────────────────┘
```

- **Target Metric:** Senior animators achieve $< 15\text{ KB}$ per second of animation data with zero visual compression artifacts.
