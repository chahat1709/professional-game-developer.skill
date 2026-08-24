# Roblox & Luau Architecture — Senior Level

## 1. Enterprise Luau & Strict Type Checking

Senior Roblox development uses **Luau in Strict Mode** (`--!strict`) to catch type errors ahead of runtime and optimize bytecode execution.

```luau
--!strict

export type VehicleState = {
    Position: Vector3,
    Velocity: Vector3,
    Health: number,
    IsActive: boolean,
}

local VehicleService = {}
VehicleService.__index = VehicleService

function VehicleService.new(initialPosition: Vector3): VehicleState
    local self: VehicleState = {
        Position = initialPosition,
        Velocity = Vector3.zero,
        Health = 100,
        IsActive = true,
    }
    return self
end

function VehicleService.ApplyThrust(state: VehicleState, force: Vector3, deltaTime: number): ()
    assert(state.IsActive, "Cannot apply thrust to inactive vehicle")
    state.Velocity += force * deltaTime
    state.Position += state.Velocity * deltaTime
end

return VehicleService
```

---

## 2. Server/Client Authority & Network Security

Roblox client code runs in an untrusted environment. Senior engineers enforce strict **Zero-Trust Network Contracts**:

```
[ Client (PlayerScripts) ] ── (RemoteEvent: RequestAction) ──> [ Server (ServerScriptService) ]
                                                                      │
                                                               1. Validate Caller
                                                               2. Rate-Limit / Cooldown
                                                               3. Physics / State Sanity Check
                                                                      │
[ All Clients ] <──────── (Replicated State) ─────────────────────────┘
```

### Critical Security Rules:
1. **Never Trust Client Transforms:** Clients send *intent* (e.g. `Throttle`, `Steer`, `Fire`), never authoritative coordinates (`SetPosition`).
2. **Rate-Limiting RemoteEvents:** Validate maximum invocation frequency per player (e.g. max 20 packet requests/sec). Drop and log anomalous floods.
3. **Server-Side Raycasting:** Hit registration must be verified on the server via raycast checks from weapon origin to target.

---

## 3. Modern Development Toolchain (Rojo + Wally)

Do not author monolithic scripts inside Roblox Studio. Use professional filesystem sync:

- **Rojo:** Syncs local VS Code / IDE files into Roblox Studio `.rbxl` models.
- **Wally:** Luau package manager (install Promise, Signal, Fusion/Roact, ProfileService).
- **Selene:** Static analysis linter for Luau codebases.
- **StyLua:** Opinionated code formatter enforcing consistent style.
- **TestEZ:** BDD testing framework for running unit tests in Studio and CI.

```json
// default.project.json
{
  "name": "ProductionGame",
  "tree": {
    "$className": "DataModel",
    "ReplicatedStorage": {
      "Shared": {
        "$path": "src/shared"
      }
    },
    "ServerScriptService": {
      "Server": {
        "$path": "src/server"
      }
    },
    "StarterPlayer": {
      "StarterPlayerScripts": {
        "Client": {
          "$path": "src/client"
        }
      }
    }
  }
}
```

---

## 4. Persistence & DataStore Architecture (ProfileService Pattern)

Use session locking to prevent data duplication exploits when players rapidly hop servers:

```luau
--!strict
local ProfileService = require(game.ReplicatedStorage.Packages.ProfileService)

local ProfileTemplate = {
    Coins = 0,
    Inventory = {},
    LastLogin = 0,
    SchemaVersion = 2,
}

local ProfileStore = ProfileService.GetProfileStore(
    "PlayerData_v2",
    ProfileTemplate
)

local function OnPlayerAdded(player: Player)
    local profile = ProfileStore:LoadProfileAsync("Player_" .. player.UserId)
    if profile ~= nil then
        profile:AddUserId(player.UserId)
        profile:Reconcile()
        profile:ListenToRelease(function()
            player:Kick("Session terminated from another server.")
        end)
        if player:IsDescendantOf(game.Players) then
            -- Profile successfully loaded
        else
            profile:Release()
        end
    else
        player:Kick("Could not load save profile. Please rejoin.")
    end
end
```

---

## 5. StreamingEnabled & Mobile Memory Optimization

- **StreamingEnabled:** Enable on all large maps. Set `StreamingMinRadius` (e.g. 64 studs) and `StreamingTargetRadius` (e.g. 512 studs).
- **Collision Fidelity:** Set static environment meshes to `CollisionFidelity.Box` or `Hull`. Avoid `PreciseConvexDecomposition` on dense scenery.
- **MicroProfiler:** Capture frame timings using `Ctrl + F6` in Studio. Ensure physics and rendering ticks stay under 16.6 ms on low-end mobile devices.
