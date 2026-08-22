# professional-game-developer — Universal

[![skills.sh](https://skills.sh/b/chahat1709/professional-game-developer.skill)](https://skills.sh/chahat1709/professional-game-developer.skill)

A **Universal Professional Game Developer** skill for coding agents (Claude Code, Codex, opencode, Cursor — any agent that loads `SKILL.md`). It turns any idea into a coherent, playable, testable, visually credible game **across any engine or platform** — Unreal, Unity, Godot, Roblox, Web/Custom — through staged decisions, controlled assets, modular systems, and runtime evidence.

My skill that I use to ship real games — not vibe-coded prototypes.

## Universal knowledge

Engine-agnostic core (game loop, composition, input abstraction, assets, persistence) plus engine-specific execution for Unreal / Unity / Godot / Roblox / Web-Custom. See `skills/engineering/professional-game-developer/references/engine-selection.md` to pick the right engine, then `universal-architecture.md` for the shared architecture.

## What it does

- Operates as a **production game developer**, not a code generator.
- Builds the smallest **vertical slice** that proves the main loop and visual target before scaling content.
- Treats assets, licenses, scale, materials, collision, animation, memory, and provenance as first-class engineering concerns.
- Keeps core rules separate from presentation (physics, scoring, AI, telemetry, save data independent of replaceable meshes, maps, and UI skins).
- Prefers deterministic, observable workflows and verifies results **in runtime** — a feature is not complete because code compiles.
- Works universally: same loop and quality bar, mapped to the chosen engine's idioms.

## Installation (30 seconds)

### Claude Code, Codex, and other agents via skills.sh

```bash
npx skills@latest add chahat1709/professional-game-developer.skill
```

Pick `professional-game-developer` when prompted and choose your agents. It copies the skill into your project as editable files. Update later with `npx skills update`.

### Claude Code plugin (managed)

```bash
claude plugins add https://github.com/chahat1709/professional-game-developer.skill
```

Or inside a Claude session:

```
/plugin add https://github.com/chahat1709/professional-game-developer.skill
```

### For tinkerers / opencode

```bash
git clone https://github.com/chahat1709/professional-game-developer.skill
```

Then point your agent at `skills/engineering/professional-game-developer/SKILL.md` (canonical) or `SKILL.md` at the repo root (alias).

## Structure

```
SKILL.md                                          # alias at root for single-skill clones
skills/engineering/professional-game-developer/
  SKILL.md                                        # canonical universal workflow — any engine
  references/
    preproduction.md
    universal-architecture.md
    engine-selection.md
    unreal-architecture.md
    unity-architecture.md
    godot-architecture.md
    roblox-architecture.md
    worldbuilding.md
    asset-pipeline.md
    gameplay-systems.md
    rendering-graphics.md
    networking-multiplayer.md
    production-leadership.md
    platform-mastery.md
    quality-and-performance.md
    droneverse-adaptation.md
    templates.md
  templates/
    project-brief.md / risk-register.md / asset-manifest.md / milestone-report.md / verification-matrix.md
  scripts/
    validate-asset-manifest.py
    quality-gate.py
.claude-plugin/plugin.json                         # Claude Code plugin manifest
package.json                                      # skills.sh manifest
AGENTS.md / CLAUDE.md                             # agent routing
```

## Usage

Load the skill and describe the game you want to build. The skill will:

1. Frame the game (fantasy, target player, core loop, platform, visual target).
2. Choose the right engine via the selection matrix.
3. Create a risk register for uncertain/expensive systems.
4. Choose a vertical slice that proves the loop and visual target.
5. Design architecture, plan the asset pipeline, and implement the riskiest system first.
6. Expand, profile, test, and package with runtime evidence.

Every milestone produces build + runtime + visual evidence — or it is not done.

## License

MIT — see [LICENSE](LICENSE).
