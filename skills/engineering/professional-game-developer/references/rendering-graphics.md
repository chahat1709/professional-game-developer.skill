# Rendering & Graphics — Senior Level

## Pipeline mental model (universal)

Every engine does: CPU culling → draw calls → vertex → raster → pixel/fragment → post. Senior question is not "which shader?" but "where is the budget going?"

- **Budget first:** lock target: 60 Hz = 16.6 ms, 30 Hz = 33.3 ms. Split: shadow 2–3 ms, base pass 6–8 ms, post 1–2 ms, UI 1 ms. If over, cut: shadows, overdraw, shader complexity, not random features.
- **Overdraw is silent killer:** translucent particles, layered UI, un-culled interiors. Visualize overdraw/quad overdraw. Prefer opaque, then masked, then translucent last.
- **Draw calls:** batch by material + mesh. One material with texture atlas/instancing beats 10 unique materials. Senior checks: instance counts, material slots per mesh, HLOD/instancing for repeated props.

## Materials & shaders (senior checks)

- Verify color space (sRGB vs linear), normal map orientation (OpenGL vs DirectX), roughness/metallic in correct channels. Wrong space = plausible-but-wrong look that juniors miss.
- One master material + instances with parameters beats 20 copies. Expose tilling, tint, roughness range, not whole new shaders.
- Shader complexity view is truth. If a "simple" prop is red, fix it — don't add more red props.

## Lighting (universal + engine mapping)

- **Dynamic vs baked:** dynamic (Lumen / real-time) for iterating open worlds, baked lightmaps for locked mobile/closed levels with tight performance. Senior decides before art production, not after.
- **Universal stack:** Directional (sun) + Sky + Fog + Exposure + Post. One reference shot per biome/time-of-day; compare transitions.
- **Shadows:** cascade/distance shadows dominate cost. Reduce cascade count, distance, and resolution before touching meshes. Contact shadows only where readable.

## LOD & culling

- Author 3 LODs or use Nanite/auto-LOD where supported. Validate silhouette at distance, not just triangle count.
- Use HLOD / imposter / GPU culling for distant clusters. Test at fastest traversal speed (drone/car) not walk speed. If it streams late at speed, it fails.
- Occlusion culling > frustum culling > distance culling. Keep gameplay collision proxy separate from visual LOD.

## Profiling (senior workflow)

1. GPU Visualizer / RenderDoc / Frame Debugger → find the 2 most expensive passes.
2. Shader complexity + Quad overdraw view → find hot meshes/materials.
3. Stat RHI / Profiler GPU → confirm memory (texture pool, vertex buffers).
4. Fix one hot path, re-profile. Do not optimize everything at once.
