# VFX & Particle Engineering — Real-Time Systems & Niagara

This reference details the real-time simulation of GPU particles, fluid dynamics, volumetric simulations, vector fields, and overdraw optimization for Visual Effects (VFX) Artists and Technical Artists.

---

## 1. GPU Compute Particle Simulation Architecture

Modern real-time particle engines (Unreal Niagara, Unity VFX Graph) execute simulation stages directly on GPU compute shaders:

```
[ CPU Game Thread (Spawn Triggers) ] ──> [ GPU Compute Dispatch (100,000+ Particles) ]
                                                        │
                                         ┌──────────────┴──────────────┐
                                         ▼                             ▼
                              [ Particle Position Buffer ]   [ Attribute Data Buffer ]
                               (X, Y, Z, Mass, Lifetime)      (Color, Size, Velocity)
                                                        │
                                                        ▼
                              [ Indirect Draw Call / Rasterization Pass ]
```

---

## 2. Vector Fields & Fluid Particle Solvers (SPH)

GPU particles derive complex turbulent motion from 3D Vector Fields and Smoothed Particle Hydrodynamics (SPH):

- **3D Vector Fields:** Discrete 3D voxel textures ($64 \times 64 \times 64$) storing 3D directional velocity vectors ($\vec{V}_x, \vec{V}_y, \vec{V}_z$). Sampled with trilinear interpolation to steer sparks and smoke plumes.
- **SPH Density Integration:**
  $$\rho_i = \sum_{j} m_j W(\vec{r}_i - \vec{r}_j, h)$$
  $$P_i = k \cdot (\rho_i - \rho_0)$$
  where $W$ is the smoothing kernel (e.g. Poly6 / Spiky kernel), $h$ is interaction radius, and $k$ is fluid stiffness constant.

---

## 3. Ribbon Trails, Flashes & Mesh Debris

1. **Ribbon Trails (Missiles / Tracers):** Connect particle positions into a continuous triangle strip. Reconstruct tangent vectors at each segment; pack normalized UV length coordinates ($[0.0, 1.0]$) to scroll energy textures.
2. **Muzzle Flashes:** Multi-layered composition:
   - Layer 1: Photometric point light flash ($10,000\text{ Lumens}$, 1 frame duration).
   - Layer 2: Directional starburst billboard quad (Random rotation, 2 frames).
   - Layer 3: High-velocity spark sparks with sub-frame motion blur vectors.
   - Layer 4: Expanding smoke puff with depth-fade soft particle blending.

---

## 4. Quad Overdraw Mitigation & Soft Particles

Translucent particle stacking is the primary cause of GPU frame-rate drops:

- **Soft Particle Depth Fade:** Smoothly fade particle alpha when approaching solid scene geometry depth $Z_{\text{scene}}$:
  $$\text{Alpha}_{\text{fade}} = \text{clamp}\left( \frac{Z_{\text{scene}} - Z_{\text{particle}}}{\text{FadeDistance}}, 0.0, 1.0 \right)$$
  *Benefit:* Eliminates harsh geometric clipping lines against ground and walls.
- **Particle Cutout Geometry:** Replace flat square transparent quads with tightly cropped 6-to-8 sided polygon meshes around particle silhouettes to discard 60%+ of empty transparent fragment shader pixels.
- **Half-Resolution Particle Rendering:** Render heavy smoke and fire particles to a half-resolution buffer ($1/2 \times 1/2$), then composite back over the full-resolution frame with bilateral upsampling.
