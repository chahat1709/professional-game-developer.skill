# DroneVerse Adaptation

Use this reference when applying the professional-game-developer skill to DroneVerse or a similar drone simulator.

## Product spine

DroneVerse is a realistic quadrotor simulator with a flyable drone, multiple open-world regions, landing-zone challenges, assisted landing prediction, telemetry logging, and keyboard/gamepad/ESP32 control. The player loop is: select a region or mission, launch, fly under environmental and control constraints, read telemetry and guidance, approach a landing zone, land safely or recover, review results, and improve.

## Architecture contract

Keep `ADronePawn` as the flight/physics owner. Keep `DroneVerseGameMode` responsible for session startup and spawn rules. Keep `WorldBootstrapActor` or its replacement responsible for region bootstrap only. Keep `LandingZoneActor` responsible for collision and touchdown evaluation. Keep `LandingPredictionSubsystem` responsible for prediction contract and fallback. Keep `FlightTelemetrySubsystem` responsible for samples, events, landing outcomes, and export. Keep ESP32 input behind a dedicated subsystem/component that feeds the same normalized control path as keyboard/gamepad.

Visual meshes, imported maps, materials, pilot characters, and UI must be replaceable without changing flight physics or landing evaluation. Use gameplay collision proxies rather than trusting the imported Mar Saba visual mesh or imported landing pad collision.

## Region plan

- **Mar Saba Desert:** first polished vertical slice. Use the supplied FBX as a hero landmark after controlled import. Surround it with authored approach routes, landing pads, desert terrain materials, cliffs, roads/trails, beacons, and mission markers.
- **High-Class City:** dense but performance-bounded modern district with rooftops, helipads, roads, skyline landmarks, wind corridors, and urban landing challenges.
- **Natural Open World:** larger PCG-dressed exploration region with varied terrain, vegetation, cliffs, water/river or canyon features, and long-range flight routes.
- **Snow Mountains:** high-altitude terrain, snow materials, ridges, mountain passes, strong wind, reduced visibility, snow VFX, and precision landing missions.

Use World Partition/Data Layers/PCG/HLOD when the regions are combined. Keep a compact desert mission map as a fallback for testing and demonstration.

## Assisted landing contract

Telemetry schema must include stable units and timestamps for position, velocity, acceleration, altitude, vertical speed, distance to pad, horizontal error, attitude, wind, battery, control input, and model status. The prediction result must include `SAFE`, `WARNING`, or `CRITICAL`, confidence/quality, correction direction, reason code, and timestamp. If inference is unavailable or stale, use deterministic safety rules and mark the source as fallback.

## Visual quality bar

Do not ship the current primitive scene as the visual target. Each region needs a coherent hero shot, working dynamic lighting/atmosphere, authored landmarks, materials with believable response, readable landing zones, an intentional camera, and enough environmental context to communicate scale. Prebuilt assets are acceptable and preferred when licensed and integrated consistently.

## Milestone order

1. Import and validate Mar Saba FBX; fix scale, axes, materials, collision, Nanite/LOD, and pivot.
2. Build one desert landing challenge around the landmark with runtime lighting and a strong camera shot.
3. Add the landing HUD and telemetry overlay to the desert slice.
4. Add functional tests for flight startup, landing evaluation, prediction fallback, and telemetry export.
5. Add the city, natural, and snow regions as authored/PCG content units.
6. Add ESP32 packet input and disconnect fallback.
7. Profile high-speed flight, streaming, PCG density, and GPU/CPU budgets.
8. Package and capture the final demo.
