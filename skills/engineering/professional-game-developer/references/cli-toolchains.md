# Headless CLI Toolchains & Automation Recipes

This reference provides autonomous agents with copy-pasteable, terminal-ready command recipes to build, test, lint, profile, and package games across all major engines in headless environments.

---

## 1. Unreal Engine 5 (Headless CLI)

Set path to engine root (e.g. `UE_ROOT="/opt/UnrealEngine"` or `UE_ROOT="C:/Program Files/Epic Games/UE_5.4"`).

### Compile Project (Linux/Mac/Windows)
```bash
# Generate project files
"$UE_ROOT/Engine/Build/BatchFiles/RunUBT.sh" -projectfiles -project="$PWD/Project.uproject" -game -engine

# Build Development Editor target
"$UE_ROOT/Engine/Build/BatchFiles/RunUBT.sh" Development Linux -Project="$PWD/Project.uproject" -TargetType=Editor
```

### Run Automated Headless Tests
```bash
# Run all automation tests via Editor-Cmd
"$UE_ROOT/Engine/Binaries/Linux/UnrealEditor-Cmd" "$PWD/Project.uproject" \
    -ExecCmds="Automation RunTests Project; Quit" \
    -unattended -nopause -nosplash -nullrhi -log=Automation.log
```

### Headless Cook and Package (RunUAT)
```bash
"$UE_ROOT/Engine/Build/BatchFiles/RunUAT.sh" BuildCookRun \
    -project="$PWD/Project.uproject" \
    -noP4 -platform=Linux -clientconfig=Shipping \
    -cook -build -stage -pak -archive -archivedirectory="$PWD/Build/Shipping" \
    -unattended -utf8output
```

---

## 2. Godot 4.3+ (Headless CLI)

Ensure `godot` binary is in `$PATH` or aliased.

### Run Headless Unit Tests (GUT Plugin)
```bash
# Run all tests in res://tests and exit with status code
godot --headless -s addons/gut/gut_cmdln.gd -gdir=res://tests -gexit -glog=2
```

### Run Specific Headless Script
```bash
# Execute standalone script in headless engine environment
godot --headless --script res://scripts/smoke_test.gd
```

### Headless Export / Build
```bash
mkdir -p build/linux
# Export release build defined in export_presets.cfg
godot --headless --export-release "Linux/X11" build/linux/game.x86_64
```

### Headless Import Asset Rebuild
```bash
# Force re-import of all modified assets without launching editor UI
godot --headless --editor --quit
```

---

## 3. Unity 6 / Modern Unity (Batchmode CLI)

Set path to Unity binary: `UNITY_BIN="/opt/unity/Editor/Unity"` or `C:\Program Files\Unity\Hub\Editor\...\Unity.exe`.

### Run EditMode & PlayMode Tests
```bash
# Run EditMode tests
"$UNITY_BIN" -batchmode -nographics \
    -projectPath "$PWD" \
    -runTests -testPlatform EditMode \
    -testResults "$PWD/Build/Logs/editmode-results.xml" \
    -logFile "$PWD/Build/Logs/unity-editmode.log"

# Run PlayMode tests
"$UNITY_BIN" -batchmode -nographics \
    -projectPath "$PWD" \
    -runTests -testPlatform PlayMode \
    -testResults "$PWD/Build/Logs/playmode-results.xml" \
    -logFile "$PWD/Build/Logs/unity-playmode.log"
```

### Headless Build Execution Method
```bash
# Invoke C# build pipeline method
"$UNITY_BIN" -batchmode -nographics -quit \
    -projectPath "$PWD" \
    -executeMethod BuildScript.PerformHeadlessBuild \
    -logFile "$PWD/Build/Logs/build.log"
```

---

## 4. Roblox / Luau Enterprise CLI Toolchain

Uses modern open-source toolchain: **Rojo**, **Wally**, **Selene**, **StyLua**, **TestEZ**.

### Install Dependencies & Sync Project
```bash
# Install packages via Wally
wally install

# Generate sourcemap for Luau LSP
rojo sourcemap default.project.json --output sourcemap.json
```

### Static Analysis & Formatting
```bash
# Strict linting via Selene
selene src/

# Code formatting check via StyLua
stylua --check src/
```

### Build Place File (.rbxl) & Run Headless Tests
```bash
# Build binary Roblox place file
rojo build default.project.json -o build/game.rbxl

# Run automated tests using run-in-roblox (TestEZ)
run-in-roblox --place build/game.rbxl --script tests/runner.server.luau
```

---

## 5. Web / Custom Engine CLI (Three.js, Babylon, Bevy)

### TypeScript / Vite / WebGL Stack
```bash
# Type check without emitting files
npx tsc --noEmit

# Run unit and integration tests
npx vitest run --coverage

# Production bundle build
npx vite build
```

### Rust / Bevy Engine Stack
```bash
# Clippy strict linter check
cargo clippy --all-targets -- -D warnings

# Run headless tests
cargo test -- --nocapture

# Release build with SIMD optimizations
cargo build --release
```

---

## 6. Execution Verification Matrix

| Engine | Headless Test Command | Headless Build Command | Exit Code Behavior |
|---|---|---|---|
| **Unreal** | `UnrealEditor-Cmd -run=Automation` | `RunUAT.sh BuildCookRun` | 0 on Pass, Non-zero on Fail |
| **Godot** | `godot --headless -s gut_cmdln.gd -gexit` | `godot --headless --export-release` | 0 on Pass, Non-zero on Fail |
| **Unity** | `Unity -batchmode -runTests` | `Unity -executeMethod BuildScript` | 0 on Pass, Non-zero on Fail |
| **Roblox** | `run-in-roblox --script test_runner` | `rojo build default.project.json` | 0 on Pass, Non-zero on Fail |
| **Web/TS** | `npx vitest run` | `npx vite build` | 0 on Pass, Non-zero on Fail |
