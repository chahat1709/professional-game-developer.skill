# Unreal Engine 5.4+ Architecture — Senior Level

## 1. Unreal Core Lifecycle & Class Responsibilities

Senior Unreal engineering enforces clear boundaries between lifetime-scoped objects, session data, and transient actors:

| Layer | Primary Responsibility | Lifetime | Forbidden Practices |
|---|---|---|---|
| **`UGameInstance`** | Cross-level state, user profile, online session, save data. | Process lifetime | Never store per-level `AActor` references. |
| **`AGameModeBase`** | Authoritative match rules, spawn policy, scoring logic. | Level/Match | Server-only. Never place client UI presentation here. |
| **`AGameStateBase`** | Replicated match state, objective progress, match timer. | Level/Match | Never process raw player input directly. |
| **`APlayerState`** | Per-player progression, inventory, ping, score. | Player session | Never run low-level physics simulation here. |
| **`APlayerController`** | Input interpretation, camera management, UI coordination. | Client connection | Never store visual character meshes or physical collision. |
| **`APawn` / `ACharacter`** | Physical body, collision, movement component, animations. | Spawn to destroy | Never store global game rules or persistence data. |
| **`UActorComponent`** | Reusable capability (Health, Flight, Inventory, Sensor). | Actor lifetime | Avoid circular dependencies between peer components. |
| **`USubsystem`** | Modular, managed engine/world/gameinstance service. | Subsystem scope | Avoid unobservable hidden global state. |

---

## 2. Gameplay Ability System (GAS)

For combat, movement abilities, and complex attributes, use **GAS**:

```cpp
// AttributeSet Declaration with RepNotify & Macro Clamping
UCLASS()
class GAME_API UVehicleAttributeSet : public UAttributeSet
{
    GENERATED_BODY()

public:
    UPROPERTY(BlueprintReadOnly, Category = "Attributes", ReplicatedUsing = OnRep_Health)
    FGameplayAttributeData Health;
    ATTRIBUTE_ACCESSORS(UVehicleAttributeSet, Health)

    UPROPERTY(BlueprintReadOnly, Category = "Attributes", ReplicatedUsing = OnRep_Energy)
    FGameplayAttributeData Energy;
    ATTRIBUTE_ACCESSORS(UVehicleAttributeSet, Energy)

    virtual void PreAttributeChange(const FGameplayAttribute& Attribute, float& NewValue) override;
    virtual void PostGameplayEffectExecute(const FGameplayEffectModCallbackData& Data) override;
};
```

- **GameplayTags:** Use hierarchical tags (`Vehicle.State.Airborne`, `Vehicle.Debuff.EMP`) for state queries instead of brittle enums.
- **GameplayEffects (GE):** Modify attributes via instant, duration, or infinite effects with calculation classes.
- **Prediction Keys:** GAS handles client prediction and server rollbacks for ability activation out of the box.

---

## 3. Mass Entity & Systemic Crowd Simulation

When simulating thousands of systemic entities (traffic, pedestrians, projectiles) where `AActor` overhead (transform, tick, reflection) is too costly, use **Mass Entity (UE ECS)**:

- **Mass Fragments:** Lightweight POD structs (`FTransformFragment`, `FVelocityFragment`).
- **Mass Processors:** Multithreaded tick execution over archetypes using Chunk Iterators.
- **Smart Objects:** AI spatial query system for contextual interactions (benches, landing pads, doors).

---

## 4. Enhanced Input Architecture

Define input by player intent, not physical keys:

```
[ Input Action: IA_Throttle ] ──> [ Input Mapping Context: IMC_Flight ] ──> [ Modifiers: DeadZone, Swizzle ]
                                                  │
                                                  ▼
                               [ Trigger: Down / HoldAndRelease ]
                                                  │
                                                  ▼
                               [ EnhancedInputComponent BindAction ]
```

```cpp
void AVehiclePawn::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
    Super::SetupPlayerInputComponent(PlayerInputComponent);

    if (UEnhancedInputComponent* EnhancedInput = Cast<UEnhancedInputComponent>(PlayerInputComponent))
    {
        EnhancedInput->BindAction(IA_Throttle, ETriggerEvent::Triggered, this, &AVehiclePawn::OnThrottle);
        EnhancedInput->BindAction(IA_Steer, ETriggerEvent::Triggered, this, &AVehiclePawn::OnSteer);
    }
}
```

---

## 5. World Partition, Data Layers & HLOD Strategy

For large-scale continuous worlds:

1. **Grid & Cell Size:** Configure runtime streaming cell size (e.g. 12,800 cm = 128m) based on vehicle travel speed.
2. **Data Layers:** Group content functionally (e.g. `DL_CoreStructures`, `DL_FoliagePCG`, `DL_MissionAssets`). Activate/deactivate Data Layers at runtime without map reloads.
3. **HLOD Layers:** Generate Hierarchical Level of Detail meshes (Instancing, Merging, or Simplified Nanite) to maintain < 1,000 draw calls at extreme draw distances.
4. **PCG (Procedural Content Generation):** Use PCG Graphs for deterministic environment scattering, road splines, and biome blending.

---

## 6. Headless Automation & Gauntlet Testing

- **Automation Tests:** Author `IMPLEMENT_SIMPLE_AUTOMATION_TEST` for deterministic gameplay logic.
- **RunUAT Build Command:**
  ```bash
  RunUAT.sh BuildCookRun -project="$PROJECT_PATH" -noP4 -platform=Linux -clientconfig=Development -cook -build -stage -pak
  ```
- **Editor Headless Execution:**
  ```bash
  UnrealEditor-Cmd "$PROJECT_PATH" -run=Automation -test="Game.Core" -unattended -nullrhi -log
  ```
