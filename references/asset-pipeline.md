# Asset Pipeline

Use this reference whenever acquiring, importing, replacing, or packaging art assets.

## Asset manifest

Track every external asset in a manifest:

| Field | Example |
|---|---|
| Asset ID | `DroneVerse_DronePilot_01` |
| Source URL | Official listing or creator page. |
| Creator/publisher | Name for credit. |
| License | Exact license and permitted use. |
| Attribution | Required credit text and location. |
| Download date | Date and version. |
| Original format | FBX, GLB, OBJ, USD, texture pack, or plugin. |
| Import destination | `/Game/DroneVerse/...` |
| Scale/axes | Centimeters, forward/up axes, origin, pivot. |
| Materials/textures | Dependencies and replacement plan. |
| Collision | Auto, custom UCX, simple primitives, or gameplay proxy. |
| Rig/animation | Skeleton, physics asset, retargeting, clips. |
| Nanite/LOD | Enabled policy and exceptions. |
| Memory/performance | Triangle count, texture size, instances, load behavior. |
| Validation | Import result, visual check, runtime check. |

## Acquisition and licensing

Prefer Fab, Quixel/Megascans, user-supplied files, or clearly licensed assets. A visible download button does not prove the license permits a packaged commercial or public game. Preserve the original URL, creator, license text, and attribution in the project. Never bypass login, paywalls, or access controls. If the license is unclear, use the asset only as a reference and ask the user to supply a permitted file.

## Import checklist

Before import, determine whether the asset is static or skeletal, whether meshes should combine, whether materials/textures are included, whether the scale and axes are correct, whether collision is available, and whether the target supports Nanite. Use Interchange or the Content Browser with explicit settings. For dense static environment meshes, evaluate Build Nanite; for dynamic/Lumen worlds, avoid generating lightmap UVs unless baked lighting requires them. For skeletal characters, import geometry/skin weights, create a physics asset when needed, verify reference pose, and retarget animations deliberately.

## Collision and gameplay proxies

Do not rely on visual mesh collision for mission-critical gameplay. Use custom simple collision, UCX collision, or separate gameplay volumes for landing pads, drone flight barriers, triggers, and interaction zones. Keep a visual imported pad mesh independent of `LandingZoneActor` evaluation and keep the drone’s physics body independent of its render mesh.

## Materials and scale

Validate physically plausible material response, texture color space, normal-map orientation, roughness/metallic channels, tiling, UV scale, and exposure. Measure the imported asset against a known human/drone/door size. Fix pivot and orientation in the source or import settings rather than compensating with unexplained runtime transforms.

## Optimization policy

Use Nanite for supported high-detail static meshes when profiling supports it. Use instancing for repeated props and PCG output. Reduce material slots, texture resolution, shader permutations, and unnecessary skeletal complexity. Create LOD or fallback policies for assets that cannot use Nanite. Profile the real camera path and the worst-case loaded region.

## Attribution delivery

Maintain a generated credits document or in-game credits entry. Include creator, source URL, license, and required wording. Do not silently redistribute source files in a public repository when the license does not permit it; package only the derived/imported content allowed by the terms.
