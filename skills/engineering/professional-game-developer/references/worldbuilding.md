# Open World Building & Streaming Architecture — Senior Level

## 1. World Partitioning & Streaming Models

Large-scale open worlds must manage disk I/O, CPU decompression, and VRAM memory budgets simultaneously.

```
┌─────────────────────────────────────────────────────────────┐
│                 Continuous Streaming Hierarchy              │
├─────────────────┬─────────────────┬─────────────────────────┤
│ Active Radius   │ 0 - 250m        │ High-detail meshes,     │
│ (Memory Loaded) │                 │ dynamic collision, AI   │
├─────────────────┼─────────────────┼─────────────────────────┤
│ Streaming Grid  │ 250m - 1,000m   │ Mid-tier LODs, static   │
│ (Async Loading) │                 │ collision, PCG props    │
├─────────────────┼─────────────────┼─────────────────────────┤
│ Distant World   │ 1,000m - 5,000m+│ HLOD clusters,          │
│ (Virtual Cache) │                 │ imposter billboards     │
└─────────────────┴─────────────────┴─────────────────────────┘
```

### High-Speed Traversal Budgeting:
- When calculating cell loading budgets, evaluate at the **fastest travel velocity** (e.g. supersonic jet or high-speed vehicle at 100+ m/s), not walking speed.
- If a vehicle moves at 100 m/s and cell size is 250m, a new cell must stream from disk and initialize in `< 2.5 seconds` without causing a rendering frame drop.

---

## 2. Hierarchical LOD (HLOD) & Imposter Generation

Distant vistas contain millions of polygons and thousands of unique draw calls that destroy GPU performance:

1. **Instanced HLOD:** Group identical static meshes (e.g. rocks, trees) within a streaming cell into a single instanced draw call.
2. **Merged HLOD:** Merge distinct adjacent geometry (e.g. building facades, walls) into a simplified mesh with combined texture atlases.
3. **Imposter Billboards (Octahedral Imposters):** For ultra-distant foliage and structures (>1,500m), render 2D camera-facing octahedral sprites with depth offset.

---

## 3. Procedural Content Generation (PCG) & Biome Scattering

Do not hand-place thousands of minor environment props:

```
[ Landscape Heightmap & Splines ] ──> [ Biome Rule Matrix ] ──> [ Spatial Sampler / Poisson Disk ]
                                                                        │
                                                               ┌────────┴────────┐
                                                               ▼                 ▼
                                                      [ Raycast to Surface ] [ Density Mask ]
                                                               │
                                                               ▼
                                                      [ GPU Instance Spawner ]
```

- **Poisson Disk Sampling:** Enforce minimum distance between scattered instances to prevent unnatural prop overlapping.
- **Surface Normal Alignment:** Align foliage/props to landscape slope normals with configurable pitch limits (e.g. trees grow vertically; rocks cling to cliff faces).
- **Collision Proxies:** Generate collision only for instances within the immediate player radius; distant PCG instances must have physics collision disabled.

---

## 4. Lighting, Atmosphere & Dynamic Time-of-Day

A senior outdoor lighting stack combines 5 coordinated layers:

1. **Directional Sun/Moon:** Primary light source with dynamic Cascaded Shadow Maps or Virtual Shadow Maps.
2. **Sky Atmosphere & Fog:** Rayleigh and Mie scattering models for physical sky color, horizon hazing, and volumetric fog.
3. **Skylight / Ambient GI:** Real-time global illumination capture (Lumen / Light Probes / Ambient Spherical Harmonics).
4. **Volumetric Clouds:** Multi-octave raymarched 3D noise textures for dynamic cloud shadows and light shafts.
5. **Post-Process Volume:** Auto-exposure (eye adaptation), physical camera aperture/ISO, color grading LUTs.
