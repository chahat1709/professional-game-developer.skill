# 3D Modeling, DCC Pipelines & Technical Art Asset Engineering

This reference establishes the strict production standards for 3D modeling, quad topology, UV layout, texel density, tangent-space normal baking, rigging, skinning, and Level of Detail (LOD) generation.

---

## 1. Quad Topology, Edge Flow & Mesh Manifold Rules

3D models must adhere to clean deformation topology and manifold geometry rules:

```
┌─────────────────────────────────────────────────────────────┐
│                    Topology Production Rules                │
├─────────────────────┬───────────────────────────────────────┤
│ Quad Dominance      │ 95%+ Quad polygons on deformable      │
│                     │ meshes; triangles only on planar areas│
├─────────────────────┼───────────────────────────────────────┤
│ Pole Placement      │ Keep 3-poles and 5-poles on flat areas;│
│                     │ NEVER place 5-poles on bending joints │
├─────────────────────┼───────────────────────────────────────┤
│ Deformation Loops   │ 3 concentric edge loops around eyes,  │
│                     │ mouth, elbows, knees, and shoulders   │
├─────────────────────┼───────────────────────────────────────┤
│ Non-Manifold Zero   │ ZERO non-manifold edges, zero internal│
│                     │ faces, zero co-planar overlapping poly│
└─────────────────────┴───────────────────────────────────────┘
```

- **Cylinder & Bevel Subdivision:** Standardize cylinder sides based on screen prominence:
  - Hero primary assets (Weapons, Steering Wheels): 24–32 sides.
  - Secondary environment props (Pillars, Pipes): 12–16 sides.
  - Small background props (Bolts, Cables): 6–8 sides.

---

## 2. UV Unwrapping & Texel Density Standardization

Texel density ($TD$) measures the resolution of texture pixels per world-space centimeter:

$$TD = \frac{\text{Texture Resolution (px)} \times \text{UV Island Size}}{\text{Mesh World Surface Area (cm)}}$$

### Global Texel Density Standardization Table:

| Asset Class | Target Texel Density ($TD$) | Typical Texture Resolution |
|---|:---:|:---:|
| **Hero Characters / Weapons** | $20.48\text{ px/cm}$ | $4096 \times 4096$ per character (UDIMs) |
| **First-Person Props / Cockpits** | $15.0 - 20.0\text{ px/cm}$ | $2048 \times 2048$ |
| **Standard Environment / Buildings** | $10.24\text{ px/cm}$ ($1024\text{ px/m}$) | $2048 \times 2048$ tiled materials |
| **Distant Terrain / Large Landmarks** | $2.56 - 5.12\text{ px/cm}$ | $1024 \times 1024$ / Virtual Texturing |

### UV Production Invariants:
1. **UV Seam Placement:** Hide UV seams on non-visible edges, occluded crevices, material transitions, or concave intersections.
2. **Hard Edges vs. UV Borders:** Every hard smoothing group edge **must** be a cut UV seam; having a hard geometric normal edge inside a contiguous UV island causes dark bake artifacts.
3. **Texel Padding / Dilation:** Enforce minimum pixel padding between UV islands based on map size to prevent MIP-map bleeding:
   - $4096 \times 4096$: 16 px padding.
   - $2048 \times 2048$: 8 px padding.
   - $1024 \times 1024$: 4 px padding.
4. **UV Packing Efficiency:** Target $> 80\%$ UV island packing density. Mirror symmetrical props (vehicles, architecture) across the $U=1.0$ coordinate boundary with a $+1.0$ offset on overlapping islands.

---

## 3. High-to-Low Poly Baking Pipeline

```
[ High-Poly Sculpt / CAD Model ] ──┐
                                   ├──> [ Cage Projection / Raycast ] ──> [ Tangent Space Normal Map ]
[ Low-Poly Topology + UVs ] ───────┘                                      [ Curvature / AO / Thickness ]
```

### Baking Invariants:
- **Projection Cages:** Use an extruded cage mesh (vertex pushed along averaged vertex normals) rather than raw ray distance to prevent intersecting ray artifacts on tight crevices.
- **Tangent Space MikkTSpace Standard:** Ensure baking software (Substance Painter, Marmoset, Blender) and target game engine both use the identical **MikkTSpace tangent basis** algorithm to eliminate normal map shading seams.
- **Normal Map Handedness:**
  - DirectX (Unreal): Inverted Green ($Y-$).
  - OpenGL (Unity, Godot, Blender): Standard Green ($Y+$).

---

## 4. Rigging, Skeletal Hierarchy & Skinning Rules

```
[ Root Bone (0,0,0) ]
        │
    [ Pelvis ]
   ┌────┴────┐
   ▼         ▼
[ Thigh ]  [ Spine 01..03 ]
   │             │
[ Calf ]     [ Clavicle ]
   │             │
 [ Foot ]     [ Upper Arm ] ──> [ UpperArm_Twist (50% Rot) ]
                 │
              [ Forearm ]   ──> [ Forearm_Twist (50% Rot) ]
                 │
               [ Hand ]
```

### Skin Weighting Production Rules:
1. **Max Influences Per Vertex:**
   - Desktop / Console: Max **4 to 8 bone influences** per vertex.
   - Mobile / VR: Max **4 bone influences** per vertex (strictly normalized to sum = $1.0$).
2. **Twist Joints:** Add dedicated twist bones on forearms, upper arms, and thighs to distribute axial twist rotation (e.g. wrist rotation) and eliminate the "candy-wrapper" mesh pinching effect.
3. **Dual Quaternion Skinning (DQS) vs. Linear Blend Skinning (LBS):** Use Linear Blend Skinning with corrective blendshapes/twist joints for reliable cross-engine deformation performance.

---

## 5. LOD Generation & Quadric Error Metrics (QEM)

When authoring or auto-generating discrete LOD chains (LOD0 through LOD3):

```
┌─────────────────────────────────────────────────────────────┐
│                     Standard LOD Metric Chain               │
├─────────┬──────────────────────┬────────────────────────────┤
│ LOD 0   │ 100% Triangle Budget │ Full mesh, all material IDs│
│ LOD 1   │ 50% Triangle Budget  │ Preserve silhouette edges  │
│ LOD 2   │ 25% Triangle Budget  │ Merge small props, 1 mat ID│
│ LOD 3   │ 10% Triangle Budget  │ Extreme distance / Box hull│
└─────────┴──────────────────────┴────────────────────────────┘
```

- **Silhouette Preservation:** Apply Quadric Error Metric edge collapses with silhouette boundary locking.
- **LOD Hysteresis:** Add screen-size transition hysteresis (e.g. switch to LOD1 at $0.45$ screen radius; switch back to LOD0 at $0.50$) to eliminate visual popping at distance boundaries.
