# Gameplay Systems and Feature Slices

Use this reference when implementing movement, physics, AI, missions, progression, telemetry, or hardware integration.

## Feature contract

For each feature define: player intent, inputs, authoritative state, outputs/feedback, failure modes, persistence, test hooks, performance budget, and replacement points. Build the feature first as a narrow vertical slice and add content only after the contract is stable.

## Physics and movement

Keep the simulation units and coordinate conventions explicit. Separate raw input, filtered control commands, forces/torques, constraints, collision, stabilization, camera behavior, and presentation. Add a deterministic test mode with fixed initial conditions and repeatable inputs. Log key state at a controlled rate, not every frame by default. Define reset behavior and safe handling for invalid values.

For vehicles, test hover, acceleration, braking, yaw, pitch/roll coupling, collision response, ground effect if needed, battery/energy limits, wind, and recovery. Calibrate feel with measurable targets rather than arbitrary multipliers.

## AI and prediction

Define model input schema, output labels, confidence/uncertainty, runtime budget, fallback behavior, and safety policy. Keep model inference behind a subsystem or service contract so the gameplay code can use deterministic fallback rules when the model is unavailable. Never let a prediction silently override a safety-critical action without an explicit policy.

## Missions and progression

Represent missions as data-driven definitions with prerequisites, region tags, objectives, fail conditions, rewards, telemetry requirements, and completion state. Keep mission logic in reusable components or managers. Use stable identifiers and version save data. Design a full success/failure/retry loop before creating a large mission catalog.

## Telemetry and observability

Define units, sampling rates, timestamps, schema version, source device, session ID, and event names. Separate high-rate samples from event records. Log input source, connection state, physics state, prediction result, landing evaluation, and runtime errors. Provide a developer overlay and an export path such as CSV/JSON without making the HUD the data source of truth.

## External hardware

Design a versioned packet protocol before implementing device I/O. Include message type, schema version, sequence number, timestamp, axes, buttons, IMU fields, battery/connection status, and checksum or framing. Use a dedicated input component/subsystem, validate ranges, apply timeouts, smooth safely, and fall back to keyboard/gamepad when packets stop arriving. Test malformed, delayed, duplicated, and disconnected packets.

## Example: assisted landing

The feature slice should: sample telemetry; compute or infer descent risk; classify SAFE/WARNING/CRITICAL; show correction guidance; keep controls responsive; evaluate pad collision and touchdown; record the landing outcome; and recover gracefully if the model is missing. A test must cover stable vertical descent, lateral drift, high sink rate, pad edge approach, missed pad, and model-unavailable fallback.
