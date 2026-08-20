# World Building and Streaming

Use this reference for landscapes, open worlds, biomes, region transitions, procedural dressing, and large-map performance.

## Select the world model

Use a bounded level for a small scene or test. Use the Open World template and World Partition for large continuous worlds, distant regions, or runtime streaming. Keep one persistent world when travel, shared progression, and spatial continuity matter. Use separate maps only when isolation, load-time separation, or fundamentally different game rules justify them.

## Region model

Design each region as a spatial and production unit with:

- a region boundary and streaming/load radius;
- a visual identity, terrain/material palette, weather, time-of-day role, and audio profile;
- hero landmarks, mission spaces, flight corridors, hazards, and landing zones;
- a Data Layer or explicit content grouping;
- an HLOD strategy and performance budget;
- entry/exit routes and a safe fallback if streaming is delayed.

For a four-region world, use a single World Partition world where possible. Place the Mar Saba desert landmark in a desert Data Layer, then organize the city, natural exploration, and snow mountain zones as separate Data Layers or spatial regions. Do not scatter region logic through Level Blueprint references that force every actor to load.

## World Partition checklist

1. Create or convert an Open World level.
2. Confirm World Partition, One File Per Actor, Data Layers, and HLOD support.
3. Choose a runtime grid and cell size based on target hardware and travel speed.
4. Set streaming sources for the player, teleport destinations, missions, and cinematic cameras.
5. Use editor regions or Location Volumes so work remains focused and responsive.
6. Validate load/unload transitions at the fastest expected player speed.
7. Build minimap data and HLODs before large-scale profiling.
8. Run cooking/packaging tests with the actual target map list.

## PCG and authored content

Use authored placement for hero landmarks, mission-critical pads, roads, vistas, and camera compositions. Use PCG for rocks, vegetation, debris, minor props, and biome variation. Assign generated content to the intended Data Layer and HLOD Layer. Prototype a PCG graph in a small representative region, inspect density and collisions, then scale it. Do not generate decorative content everywhere before confirming memory and streaming behavior.

## Biome design

Define a biome data record containing terrain material, foliage/prop sets, scatter rules, weather, wind, fog, ambient color, mission tags, and landing-risk modifiers. Reuse the same graph with parameters rather than duplicating graphs per region. Maintain a visual hierarchy: silhouette landmarks first, traversal routes second, medium props third, micro-detail last.

## Lighting and atmosphere

Use a deliberate outdoor lighting stack: directional sun, skylight, sky/atmosphere, exponential height fog, clouds, exposure, and post-process settings. Prefer movable/dynamic lighting during procedural development and runtime demos. Keep static-lighting warnings out of captured milestones. Establish one lighting reference shot per region and compare region transitions under the intended time-of-day policy.

## Performance gates

Measure visible and loaded cell counts, streaming hitches, HLOD transitions, PCG actor counts, instance counts, landscape complexity, shader cost, memory, and frame time. Test high-speed flight because a drone can cross cells faster than a walking character. Use debug runtime hash views and streaming logs when diagnosing region issues.
