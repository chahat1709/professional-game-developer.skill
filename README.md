# professional-game-developer — Universal

A **Universal Professional Game Developer** skill for coding agents (Claude Code, opencode, Cursor — any agent that loads `SKILL.md`). It turns any idea into a coherent, playable, testable, visually credible game **across any engine or platform** — Unreal, Unity, Godot, Roblox, Web/Custom — through staged decisions, controlled assets, modular systems, and runtime evidence.

## Universal knowledge

Engine-agnostic core (game loop, composition, input abstraction, assets, persistence) plus engine-specific execution for Unreal / Unity / Godot / Roblox / Web-Custom. See `references/engine-selection.md` to pick the right engine, then `references/universal-architecture.md` for the shared architecture.

## What it does

- Operates as a **production game developer**, not a code generator.
- Builds the smallest **vertical slice** that proves the main loop and visual target before scaling content.
- Treats assets, licenses, scale, materials, collision, animation, memory, and provenance as first-class engineering concerns.
- Keeps core rules separate from presentation (physics, scoring, AI, telemetry, save data independent of replaceable meshes, maps, and UI skins).
- Prefers deterministic, observable workflows and verifies results **in runtime** — a feature is not complete because code compiles.
- Works universally: same loop and quality bar, mapped to the chosen engine's idioms.

## Structure

```
SKILL.md                          # Universal workflow — any engine
references/
  preproduction.md                # Framing the game, risk register, acceptance criteria
  universal-architecture.md       # Engine-agnostic architecture (loop, ECS, input, persistence)
  engine-selection.md             # Unreal vs Unity vs Godot vs Roblox vs Web/Custom matrix
  unreal-architecture.md          # Unreal mapping (GameInstance/GameMode/Components)
  worldbuilding.md                # Worlds & streaming (bounded vs open, Unreal example)
  asset-pipeline.md               # Asset manifest, import, licensing, materials
  gameplay-systems.md             # Feature slices, physics, AI, telemetry, hardware
  quality-and-performance.md      # Testing, profiling, packaging, runtime evidence
  droneverse-adaptation.md        # DroneVerse-specific (Unreal) example
  templates.md                    # Reusable project documents
templates/
  project-brief.md / risk-register.md / asset-manifest.md / milestone-report.md / verification-matrix.md
scripts/
  .gitkeep                        # Add project-specific automation here
```

## Installation

For agents that support skill folders, clone the repo and point the agent at this directory:

```bash
git clone https://github.com/chahat1709/professional-game-developer.skill
```

Then load the skill from the cloned `SKILL.md` (e.g., with Claude Code's skill loader or opencode's skill directory).

## Usage

Load the skill and describe the game you want to build. The skill will:

1. Frame the game (fantasy, target player, core loop, platform, visual target).
2. Create a risk register for uncertain/expensive systems.
3. Choose a vertical slice that proves the loop and visual target.
4. Design architecture, plan the asset pipeline, and implement the riskiest system first.
5. Expand, profile, test, and package with runtime evidence.

## License

All original content in this repository is provided for use with coding agents. If you adapt or redistribute it, keep attribution to the source repository.