# Godot 4.3+ Architecture — Senior Level

## 1. Engine Mental Model & Performance Hierarchy

In Godot 4, the high-level `Node` and `SceneTree` abstractions provide developer velocity, while low-level **Server APIs** (`RenderingServer`, `PhysicsServer3D`, `AudioServer`) provide raw throughput.

### The Two Execution Paths
1. **SceneTree / Node Hierarchy (Gameplay & Composition):** Use for characters, interactive props, UI, and state machines where per-node lifecycle (`_ready`, `_process`, `_physics_process`) is manageable.
2. **Server Direct Dispatch (Mass Systems / Bullet Hell / Foliage):** When simulating >1,000 entities, bypass `Node` overhead. Allocate lightweight Resource IDs (`RID`) directly via `RenderingServer.instance_create()` or `PhysicsServer3D.body_create()`.

---

## 2. GDScript 2.0 Strict Typing & Patterns

Senior GDScript code enforces static typing for JIT optimizations and compile-time safety:

```gdscript
class_name VehicleController extends CharacterBody3D

signal telemetry_updated(speed_mps: float, altitude_m: float)
signal health_depleted()

@export_group("Physics Properties")
@export_range(0.0, 500.0, 1.0) var engine_power: float = 250.0
@export var mass_kg: float = 1200.0

@export_group("Subsystems")
@export var telemetry_config: Resource

# Private state strictly typed
var _current_velocity: Vector3 = Vector3.ZERO
var _is_grounded: bool = false
@onready var _collision_shape: CollisionShape3D = %CollisionShape3D
@onready var _visual_mesh: MeshInstance3D = %VisualMesh

func _physics_process(delta: float) -> void:
    _apply_forces(delta)
    move_and_slide()
    telemetry_updated.emit(velocity.length(), global_position.y)

func _apply_forces(delta: float) -> void:
    if not is_on_floor():
        velocity += get_gravity() * delta
```

### Senior Best Practices:
- **Scene Unique Nodes (`%NodeName`):** Decouple scripts from fragile node hierarchies (`$Path/To/Node`). Access unique nodes via `%` syntax.
- **Custom `Resource` as Data Contracts:** Store weapon stats, vehicle parameters, and mission definitions in `.tres` files. Keep resources pure data (no transient node references).
- **Signal Decoupling:** Children emit signals up; parents call methods down. Never allow child nodes to access parent state directly.

---

## 3. High-Performance Server API Usage

When instancing thousands of entities (e.g. debris, projectiles, crowds), use `MultiMeshInstance3D` or direct `RenderingServer` calls:

```gdscript
# Direct batching via MultiMeshInstance3D
func spawn_instanced_debris(transforms: Array[Transform3D], mesh: Mesh) -> MultiMeshInstance3D:
    var mmi := MultiMeshInstance3D.new()
    var multimesh := MultiMesh.new()
    multimesh.transform_format = MultiMesh.TRANSFORM_3D
    multimesh.mesh = mesh
    multimesh.instance_count = transforms.size()
    
    for i in range(transforms.size()):
        multimesh.set_instance_transform(i, transforms[i])
        
    mmi.multimesh = multimesh
    return mmi
```

---

## 4. Networking & Multiplayer (MultiplayerAPI)

Godot 4 features a built-in high-level multiplayer API based on ENet and WebSockets:

```gdscript
# Server-Authoritative RPC Pattern
@rpc("any_peer", "call_remote", "reliable")
func request_fire(direction: Vector3) -> void:
    var sender_id: int = multiplayer.get_remote_sender_id()
    if not _validate_rate_limit(sender_id):
        return
    # Server executes and replicates back
    _spawn_projectile_authoritative.rpc(direction)

@rpc("authority", "call_local", "reliable")
func _spawn_projectile_authoritative(direction: Vector3) -> void:
    # Client presentation spawn
    pass
```

- **Replication:** Use `MultiplayerSynchronizer` for continuous transforms with configurable replication intervals and quantization.
- **Spawning:** Use `MultiplayerSpawner` for automated dynamic entity replication.

---

## 5. Automated Testing & Profiling

1. **GUT (Godot Unit Test):** Place unit and integration tests under `res://tests/`.
2. **Headless Execution:** Run `godot --headless -s addons/gut/gut_cmdln.gd -gdir=res://tests -gexit`.
3. **Engine Profiler:** Monitor `Physics Frame Time`, `Process Time`, `Draw Calls`, and `Object Count` in the Debugger panel. Keep draw calls < 1,000 on desktop, < 200 on mobile.
