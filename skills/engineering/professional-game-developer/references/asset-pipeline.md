# Asset Pipeline & Technical Validation — Senior Level

## 1. Asset Manifest Schema & Provenance

Every external 3D mesh, texture, audio file, or animation must be cataloged in the project **Asset Manifest** before entering the production repository.

### Canonical Manifest Schema (11 Fields):

| Field | Description | Example |
|---|---|---|
| **Asset ID** | Unique project identifier following naming conventions. | `SM_Rock_Granite_01` |
| **Source** | Origin URL or DCC source package location. | `https://ambientcg.com/a/Rock01` |
| **Creator** | Original artist, studio, or publisher name. | `ambientCG` |
| **License** | Legal license terms governing project distribution. | `CC0-1.0` / `Custom Commercial` |
| **Attribution** | Exact attribution string required for project credits. | `Rock 01 by Lennart Demes (CC0)` |
| **Format** | Source interchange format. | `GLB` / `FBX` / `PNG` / `WAV` |
| **Destination** | Project engine content path. | `/Content/Environment/Rocks` |
| **Scale** | Coordinate units, orientation, and scaling factor. | `1.0 (cm, Z-Up)` |
| **Collision** | Physics collision strategy. | `UCX Simplified Hull` / `Box Proxy` |
| **Nanite/LOD** | LOD / Virtual geometry policy. | `Nanite Enabled (Falloff LOD3)` |
| **Validation** | Verification result from test import and gameplay check. | `Pass` |

---

## 2. Naming Conventions & Hierarchy

Enforce strict prefixing to ensure asset registries and search filters function reliably:

- `SM_` : Static Mesh (`SM_Building_Door_01`)
- `SK_` : Skeletal Mesh (`SK_Character_Pilot`)
- `M_`  : Master Material (`M_Opaque_PBR_Master`)
- `MI_` : Material Instance (`MI_Vehicle_Chassis_Red`)
- `T_`  : Texture (`T_Rock_Granite_01_D` / `_N` / `_ORM`)
- `A_`  : Audio / Sound Cue (`A_Engine_Turbine_Loop`)
- `VFX_`: Niagara / Particle System (`VFX_Thruster_Flame`)
- `BP_` / `WBP_`: Blueprint / Widget Blueprint (`BP_Vehicle_Base`, `WBP_HUD_Telemetry`)

---

## 3. Texture Channel Packing & Optimization

Packing multiple single-channel maps into a single RGBA texture saves 66% of texture memory and drastically cuts GPU texture sampling bandwidth:

```
┌─────────────────────────────────────────────────────────────┐
│                    ORM Channel Packing Standard             │
├───────────────┬───────────────────────────────┬─────────────┤
│ Channel R     │ Ambient Occlusion (AO)        │ Linear      │
│ Channel G     │ Roughness                     │ Linear      │
│ Channel B     │ Metallic                      │ Linear      │
│ Channel A     │ Height / Displacement / Opacity│ Linear      │
└───────────────┴───────────────────────────────┴─────────────┘
```

- **Resolution Powers of Two:** All runtime textures must be power-of-two (e.g. 512x512, 1024x1024, 2048x2048) to allow hardware MIP-map generation and GPU block compression (BC1/BC3/BC7 on Desktop, ASTC/ETC2 on Mobile).

---

## 4. Collision Proxies vs. Visual Meshes

**Senior Golden Rule:** Never use visual render geometry for critical physics collision.

1. **Visual Mesh:** Contains bevels, decorative greebles, and micro-polygons.
2. **Collision Proxy:** Use simple primitive colliders (Box, Capsule, Sphere) or low-poly convex hulls (`UCX_MeshName`).
3. **Gameplay Triggers:** Use dedicated invisible collision volumes for interaction zones, checkpoints, and landing pads.
