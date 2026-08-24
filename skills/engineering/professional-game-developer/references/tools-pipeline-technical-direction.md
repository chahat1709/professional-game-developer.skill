# Tools Engineering, Asset Ingestion & Technical Direction — Senior Level

This reference establishes the engineering pipeline for automated DCC asset ingestion, Universal Scene Description (USD), texture compression pipelines, build farm orchestration, and symbolicated crash telemetry.

---

## 1. Automated DCC Asset Ingestion Pipeline

Senior technical directors build automated CLI asset processors so artists never manually configure import dialogs:

```
[ DCC Export: Maya / Blender / Houdini ] ──> [ Drop Folder / Watcher Daemon ]
                                                        │
                                                        ▼
                                       [ Automated Validation Python Script ]
                                         • Check Scale (1 unit = 1cm) & Z-Up
                                         • Validate Quad Topology & UV Padding
                                         • Verify Naming Convention Prefix
                                                        │
                                                        ▼
                                       [ Engine Headless Asset Importer ]
                                         • Auto-generate Collision Hull (UCX)
                                         • Generate LOD Chain (QEM)
                                         • Compile Shader Permutations
                                                        │
                                                        ▼
                                       [ Verified Content Ingested to Git / Perforce ]
```

---

## 2. Universal Scene Description (USD) Pipeline

In modern AAA studio pipelines (Rockstar, ILM, Epic), world data is shared across Houdini, Maya, Blender, and Engine via **Pixar USD (`.usd`, `.usda`, `.usdc`)**:

```
Asset USD Layer (Geom + Mat) ──┐
                               ├──> [ Biome Composition USD Stage ] ──> [ Engine World Importer ]
Environment Dressing Layer ────┘
```

- **USD Payloads & References:** Keep geometry heavy payloads decoupled from light metadata stages.
- **Non-Destructive Overrides:** Environment artists can tweak lighting and material assignments on sub-layers without modifying the base asset USD file.

---

## 3. Automated Texture Compression & Block Encoding

Never import uncompressed PNG or TGA textures into packaged builds:

```
┌─────────────────────────────────────────────────────────────┐
│                 GPU Texture Compression Formats             │
├───────────────────┬──────────────┬──────────────────────────┤
│ Format Standard   │ Memory Ratio │ Best Target Platform     │
├───────────────────┼──────────────┼──────────────────────────┤
│ **BC1 (DXT1)**    │ 4 bits/pixel │ RGB Albedo / Normal (X)  │
│ **BC3 (DXT5)**    │ 8 bits/pixel │ RGBA (Albedo + 1-bit A)  │
│ **BC5 (3Dc)**     │ 8 bits/pixel │ Two-Channel Normal (RG)  │
│ **BC7 (BPTC)**    │ 8 bits/pixel │ High-Quality HDR / PBR   │
│ **ASTC (Adaptive)**| 1 - 8 bpp   │ Modern Mobile (iOS/Andr) │
│ **ETC2**          │ 4 - 8 bpp    │ Legacy Android Devices   │
└───────────────────┴──────────────┴──────────────────────────┘
```

- **Two-Channel Normal Map Compression (BC5):** Store only the $X$ (Red) and $Y$ (Green) normal channels in BC5 format. Reconstruct the $Z$ (Blue) channel in the pixel shader dynamically:
  $$Z = \sqrt{\max\left(0, 1.0 - X^2 - Y^2\right)}$$
  *Benefit:* 50% smaller normal map size with drastically higher quality and zero block compression artifacts on curved surfaces.

---

## 4. Build Farm Automation & Symbolicated Crash Reporting

```
[ Git / Perforce Commit ] ──> [ CI/CD Build Farm Runner (Linux Headless) ]
                                          │
                        ┌─────────────────┴─────────────────┐
                        ▼                                   ▼
          [ Automated Cook & Package ]          [ Headless Test Matrix ]
          • Strip Debug Symbols                 • Run Unit Tests (GUT / UTF)
          • Generate `.sym` / `.pdb` Dump       • Run Automated Smoke Bot
                        │                                   │
                        └─────────────────┬─────────────────┘
                                          ▼
                         [ Upload Build to Steam / Epic ]
                                          │
                         [ Upload Symbols to Sentry / BugSplat ]
```

### Crash Telemetry Symbolication:
When a client runtime crashes in shipping mode, the game client uploads a raw minidump (`.dmp`) containing memory addresses (e.g. `0x00007FF612A4B820`).
- The backend crash server matches the build GUID to the archived debug symbols (`.pdb` on Windows, `.sym` / DWARF on Linux).
- Demangles memory offsets to file and exact line numbers:
  `VehiclePhysicsSolver.cpp: Line 142 -> AVehiclePawn::IntegrateForces()`
