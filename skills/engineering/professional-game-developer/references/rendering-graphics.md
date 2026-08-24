# Rendering & Graphics Architecture — Senior Level

## 1. Render Pipeline Selection & Mental Model

Modern graphics engines execute a multi-stage GPU pipeline:
`CPU Culling & Batching` ──> `Geometry / Vertex` ──> `Rasterization` ──> `Pixel / Fragment` ──> `Post-Processing & Compositing`

| Pipeline Technique | Best Use Case | Performance Characteristics |
|---|---|---|
| **Forward+ (Tiled Forward)** | VR, Mobile, MSAA requirements, low dynamic light counts. | Single geometry pass; lights binned into screen-space tiles (16x16 px) in compute shader. Low memory bandwidth. |
| **Clustered Deferred** | High-end PC/Console, hundreds of dynamic lights, open worlds. | G-Buffer layout (Albedo, Normal, Roughness/Metallic, Depth). Lights binned into 3D camera frustum clusters (X, Y, Depth slices). |
| **Tile-Based Deferred (TBDR)** | Apple Silicon, Qualcomm Adreno, ARM Mali (Mobile). | G-Buffer stored in ultra-fast on-chip tile memory (SRAM), eliminating external DRAM memory bandwidth spikes. |

---

## 2. Shadow Systems & Memory Math

Shadows represent 25–40% of total GPU frame time. Senior graphics engineers budget shadows precisely:

```
┌─────────────────────────────────────────────────────────────┐
│             Cascaded Shadow Map (CSM) Distribution          │
├────────────┬──────────────┬───────────────┬─────────────────┤
│ Cascade 0  │ 0m - 15m     │ 2048 x 2048   │ Hero character  │
│ Cascade 1  │ 15m - 50m    │ 2048 x 2048   │ Immediate props │
│ Cascade 2  │ 50m - 150m   │ 1024 x 1024   │ Environment     │
│ Cascade 3  │ 150m - 500m  │ 1024 x 1024   │ Distant terrain │
└────────────┴──────────────┴───────────────┴─────────────────┘
```

- **Virtual Shadow Maps (VSM):** In UE5, VSMs allocate clipmaps in virtual memory pages (128x128 px tiles). Only update cached shadow pages when static geometry or light transforms change.
- **Contact Shadows / Screen Space Shadows:** Use short-range screen-space raymarching to capture micro-crevices and fingers without bloating shadow map cascade resolutions.

---

## 3. Culling & Overdraw Mitigation

Overdraw occurs when the GPU shades pixels that are later overwritten by closer opaque geometry.

1. **Hi-Z Occlusion Culling:** Downsample the depth buffer to a Hierarchical Z-Pyramid. Test bounding boxes of candidate meshes against the Hi-Z buffer before issuing draw calls.
2. **Early-Z / Depth Pre-Pass:** Render bounding geometry or opaque masks to depth-only buffer first; discard occluded fragments before running expensive fragment shaders.
3. **Sort Front-to-Back:** Draw opaque geometry nearest to camera first to maximize Early-Z rejection. Draw translucent geometry strictly Back-to-Front.
4. **Quad Overdraw:** Avoid ultra-dense triangles (smaller than a 2x2 pixel quad) on distant meshes without LODs.

---

## 4. Materials, Shaders & Color Space Rules

- **Color Space Integrity:**
  - Base Color / Albedo / Emissive: Imported as **sRGB** (Gamma-corrected).
  - Normal, Roughness, Metallic, Occlusion, Height: Imported as **Linear** (sRGB unchecked).
- **Normal Map Handedness:** Verify tangent-space green channel:
  - Unreal / DirectX: Y- (Green inverted).
  - Unity / Godot / OpenGL / Blender: Y+ (Green standard).
- **Master Material Paradigm:** Author unified master shaders with parameterized material instances. Never create dozens of distinct shader programs with minor variable differences.
- **ALU vs. Texture Fetch Budget:** Balance mathematical procedural operations (ALU) against texture samplers (Texture Fetch Bandwidth). Cap texture samplers to <= 16 per material.

---

## 5. Senior Graphics Profiling Workflow

```
1. Capture Frame with RenderDoc / Unreal Insights / Frame Debugger.
2. Inspect Top 3 Most Expensive Passes (e.g. BasePass, ShadowDepths, PostProcess).
3. Visualize Quad Overdraw & Shader Complexity viewmodes.
4. Check GPU Memory / Texture Pool allocations against target VRAM budget.
5. Apply isolated fix (e.g. adjust CSM split, enable mesh instancing, reduce translucent particle count).
6. Re-profile to verify measurable frame-time reduction (in milliseconds).
```
