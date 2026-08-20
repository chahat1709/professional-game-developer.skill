# professional-game-developer

A **Professional Game Developer** skill for coding agents (Claude Code, opencode, and compatible agents). It turns a raw idea into a coherent, playable, testable, visually credible game through staged decisions, controlled assets, modular systems, and runtime evidence.

## What it does

- Operates as a **production game developer**, not a code generator.
- Builds the smallest **vertical slice** that proves the main loop and visual target before scaling content.
- Treats assets, licenses, scale, materials, collision, animation, memory, and provenance as first-class engineering concerns.
- Keeps core rules separate from presentation (physics, scoring, AI, telemetry, save data independent of replaceable meshes, maps, and UI skins).
- Prefers deterministic, observable workflows and verifies results **in runtime** — a feature is not complete because code compiles.

## Structure

```
SKILL.md                          # Main skill definition + workflow
references/
  preproduction.md                # Framing the game, risk register, acceptance criteria
  unreal-architecture.md          # Unreal class responsibilities, Enhanced Input, world setup
  worldbuilding.md                # Bounded vs open world, World Partition, streaming, HLOD
  asset-pipeline.md               # Asset manifest, import pipeline, licensing, materials
  gameplay-systems.md             # Feature slices, data-driven definitions, modular systems
  quality-and-performance.md      # Testing, profiling, packaging, runtime evidence
  droneverse-adaptation.md        # DroneVerse-specific adaptation of the workflow
  templates.md                    # Reusable project documents
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