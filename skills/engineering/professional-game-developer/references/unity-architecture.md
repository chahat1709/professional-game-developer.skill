# Unity 6 Architecture & DOTS — Senior Level

## 1. Architectural Paradigms: Classic OOP vs. Data-Oriented (DOTS)

Senior Unity engineering distinguishes between **Hybrid MonoBehaviours** (for UI, high-level orchestration, and small prototypes) and the **Data-Oriented Technology Stack (DOTS/Entities)** (for massive systemic simulation, crowds, and high-throughput physics).

```
┌───────────────────────────────────────────────┐
│               Unity System Stack              │
├───────────────────────┬───────────────────────┤
│ Hybrid MonoBehaviour  │ Pure DOTS / Entities  │
├───────────────────────┼───────────────────────┤
│ • UI Toolkit / UGUI   │ • Entities 1.0+       │
│ • State Machines      │ • IJobEntity & Burst  │
│ • High-level Services │ • NativeArray / SIMD  │
│ • ScriptableObject DB │ • Chunk Iteration     │
└───────────────────────┴───────────────────────┘
```

---

## 2. Zero-Allocation & Garbage Collection Discipline

In production Unity games, garbage collection spikes cause perceptible frame hitches (10–50 ms). Senior developers enforce a strict **zero-allocation policy** during frame loops:

- **No `new` in `Update()` or `FixedUpdate()`:** Cache collections, buffers, and class instances during initialization (`Awake`/`Start`).
- **Use NonAlloc Physics APIs:** Replace `Physics.RaycastAll` with `Physics.RaycastNonAlloc(ray, hitBuffer)`.
- **String Formatting:** Avoid `$"Value: {val}"` in UI updates; use pre-allocated character buffers or integer-to-string lookup tables.
- **Events & Delegates:** Avoid creating lambdas or anonymous closures inside tick functions (`Action` capturing outer variables allocates heap memory).

---

## 3. High-Performance DOTS / IJobEntity Pattern

```csharp
using Unity.Entities;
using Unity.Mathematics;
using Unity.Transforms;
using Unity.Burst;

public struct VehicleData : IComponentData
{
    public float3 Velocity;
    public float Acceleration;
    public float MaxSpeed;
}

[BurstCompile]
public partial struct VehicleMovementSystem : ISystem
{
    [BurstCompile]
    public void OnUpdate(ref SystemState state)
    {
        float deltaTime = SystemAPI.Time.DeltaTime;
        
        new VehicleMovementJob
        {
            DeltaTime = deltaTime
        }.ScheduleParallel();
    }
}

[BurstCompile]
public partial struct VehicleMovementJob : IJobEntity
{
    public float DeltaTime;

    void Execute(ref LocalTransform transform, ref VehicleData vehicle)
    {
        transform.Position += vehicle.Velocity * DeltaTime;
    }
}
```

---

## 4. Modularity via Assembly Definitions (`.asmdef`)

Enforce strict compilation boundaries across the codebase:

```
Assets/
├── Core/             --> Game.Core.asmdef (No dependencies on engine presentation)
├── Systems/          --> Game.Systems.asmdef (Depends on Core)
├── Gameplay/         --> Game.Gameplay.asmdef (Depends on Systems, Core)
├── UI/               --> Game.UI.asmdef (Depends on Core, UI Toolkit)
└── Tests/
    ├── EditMode/     --> Game.Tests.EditMode.asmdef
    └── PlayMode/     --> Game.Tests.PlayMode.asmdef
```

**Benefits:**
- Reduces script recompilation time from 30+ seconds to < 2 seconds.
- Enforces unidirectional dependency flow (prevents spaghetti circular references).
- Isolates test code completely from production build assemblies.

---

## 5. Addressables & Asset Lifecycle

Never use `Resources.Load()` in production (loads entire asset index into memory). Use **Addressables**:

```csharp
using UnityEngine.AddressableAssets;
using UnityEngine.ResourceManagement.AsyncOperations;

public class AssetLoaderService
{
    public async Task<GameObject> LoadAndInstantiateAsync(AssetReference assetRef, Vector3 position)
    {
        AsyncOperationHandle<GameObject> handle = assetRef.InstantiateAsync(position, Quaternion.identity);
        await handle.Task;
        
        if (handle.Status == AsyncOperationStatus.Succeeded)
        {
            return handle.Result;
        }
        
        Debug.LogError($"Failed to load addressable asset: {assetRef.RuntimeKey}");
        return null;
    }

    public void ReleaseAsset(GameObject instance)
    {
        Addressables.ReleaseInstance(instance);
    }
}
```

---

## 6. Input System Package Contract

Use the modern **Unity Input System** with named Actions, Action Maps, and C# event bindings:

```csharp
public class PlayerInputHandler : MonoBehaviour
{
    private PlayerInputActions _inputActions;
    public Vector2 MoveVector { get; private set; }

    private void Awake()
    {
        _inputActions = new PlayerInputActions();
        _inputActions.Player.Move.performed += ctx => MoveVector = ctx.ReadValue<Vector2>();
        _inputActions.Player.Move.canceled += ctx => MoveVector = Vector2.zero;
    }

    private void OnEnable() => _inputActions.Enable();
    private void OnDisable() => _inputActions.Disable();
}
```

---

## 7. Headless Testing & Profiling Tools

- **CLI Tests:** `Unity -batchmode -nographics -projectPath . -runTests -testPlatform EditMode`
- **Frame Debugger:** Inspect draw calls, dynamic batching, SRP batcher compatibility, and overdraw.
- **Memory Profiler:** Detect managed memory leaks, dangling native textures, and untracked asset references.
