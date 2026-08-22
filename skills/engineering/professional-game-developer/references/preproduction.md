# Preproduction and Planning

Use this reference before starting a new game, feature, region, or major refactor.

## Required brief

Write a one-page brief containing:

| Field | Required content |
|---|---|
| Player fantasy | What the player does and why it feels compelling. |
| Core loop | The repeatable sequence from input to reward and restart. |
| Audience and platform | Target player, hardware, input devices, resolution, and performance target. |
| Camera and perspective | First person, third person, cockpit, top-down, cinematic, or hybrid. |
| Visual target | Reference images, palette, materials, lighting, density, and camera examples. |
| Systems | Movement, interactions, missions, AI, progression, UI, saving, telemetry, networking, and hardware. |
| Content scope | Regions, levels, characters, props, effects, audio, and expected variation. |
| Acceptance criteria | Concrete observable conditions for calling the milestone done. |

## Risk register

Record each risk as:

`Risk → impact → likelihood → experiment → evidence → fallback → owner`

Prioritize risks that can invalidate the architecture or schedule. Examples include imported assets with no usable collision, a physics model that cannot be controlled, streaming that fails at region transitions, an AI model that cannot run within frame budget, or external hardware that cannot maintain a stable connection.

## Vertical slice

Choose one compact slice that includes the real player action, representative art direction, one objective, one failure state, and a restart path. The slice should use the intended architecture and a near-final interaction feel, even if its content volume is small. Do not build four regions, ten mission types, or a large inventory before one loop is fun and reliable.

## Milestone contract

Every milestone must state:

1. What is being proved.
2. What files, systems, and assets change.
3. How the player or tester will observe success.
4. What automated or runtime evidence will be captured.
5. What is intentionally out of scope.
6. What known limitations remain.

## Change control

When a user changes scope, revise the brief, risk register, asset manifest, and milestone order before implementing. Do not silently continue an obsolete plan. Separate **must ship**, **should ship**, and **later expansion** items.

## Example: DroneVerse slice

The first slice should be one desert flight challenge around the Mar Saba landmark: spawn the drone, apply keyboard/gamepad input, maintain stable flight, receive live telemetry, approach one pad, display SAFE/WARNING/CRITICAL landing risk, complete or fail the landing, save a flight record, and restart. City, forest, and snow regions are later content only after this loop is stable and visually credible.
