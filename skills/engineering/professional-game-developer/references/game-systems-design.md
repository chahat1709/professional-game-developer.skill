# Game Systems & Economy Design — Senior Level

This reference establishes the mathematical formulas, progression scaling models, combat frame-data rules, and economic equilibrium systems used by Senior Systems and Economy Designers.

---

## 1. Mathematical Progression & XP Scaling Curves

Never author player progression with arbitrary linear increments ($100, 200, 300$). Use parametric scaling curves to budget player time and engagement:

```
┌─────────────────────────────────────────────────────────────┐
│                    Progression Curve Models                 │
├────────────────────┬────────────────────────────────────────┤
│ 1. Exponential     │ XP(L) = BaseXP * (Multiplier)^(L - 1)  │
│    (Classic RPG)   │ High late-game grind; prevents stat    │
│                    │ inflation runaway.                     │
├────────────────────┼────────────────────────────────────────┤
│ 2. Polynomial      │ XP(L) = A * L^3 + B * L^2 + C * L + D  │
│    (Balanced MMO)  │ Predictable mid-game progression ramp  │
│                    │ with controllable inflection points.   │
├────────────────────┼────────────────────────────────────────┤
│ 3. Sigmoidal       │ XP(L) = Cap / (1 + e^(-k * (L - L_mid))│
│    (S-Curve)       │ Fast onboarding, steady mid-game mastery│
│                    │ smooth plateau at endgame cap.         │
└────────────────────┴────────────────────────────────────────┘
```

### Cumulative Time-to-Level Budgeting:
$$\text{Total Time to Level } L = \sum_{i=1}^{L} \left( \frac{\text{XP Required}(i)}{\text{XP Generation Rate (XP/Hour)}} \right)$$

---

## 2. Combat Frame Data & Animation Windows

Combat mechanics require frame-accurate state machine rules (evaluated at 60 FPS = $16.6\text{ ms}$ per frame):

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       Combat Frame-Data Timeline                            │
├───────────────────────┬─────────────────────────┬───────────────────────────┤
│ Startup Phase         │ Active Hit Phase        │ Recovery Phase            │
│ (Frames 1 - 8)        │ (Frames 9 - 13)         │ (Frames 14 - 28)          │
├───────────────────────┼─────────────────────────┼───────────────────────────┤
│ • Windup animation    │ • Hitbox geometry active│ • Weapon follow-through   │
│ • Input cancel window │ • Check hurtbox overlap │ • Vulnerable to counter   │
│ • Armor / Invuln flags│ • Trigger Hit-Stun / VFX│ • Buffer next combo input │
└───────────────────────┴─────────────────────────┴───────────────────────────┘
```

- **Input Buffering Window:** Buffer player attack/dodge button presses for $6 - 10$ frames ($100 - 166\text{ ms}$) prior to the earliest recovery cancel frame to ensure fluid combo execution without dropped inputs.
- **Hit-Stop (Impact Freeze):** Freeze both attacker and defender skeletal animation evaluation for $3 - 6$ frames upon confirmed hit to impart tangible physical weight to melee impacts.

---

## 3. Game Economy & Sink-Source Equilibrium

In live-service and RPG economies, un-sunk currency leads to runaway inflation and devalues rewards. Senior economy designers model currencies as **Hydrodynamic Flow Systems**:

```
[ Sources (Inflow) ]                        [ Sinks (Outflow) ]
• Mission Completion Rewards                • Equipment Repair Costs
• Enemy Loot Drops             ───> [ Pool ] ───> • Fast Travel Fees
• Item Vendor Sales                         • Crafting Material Purchases
• Achievement Milestones                    • Cosmetic Item Upgrades
```

### Inflow / Outflow Balance Equations:
$$\Delta \text{Currency}_{\text{player}} = \text{Inflow Rate} - \text{Outflow Rate}$$
$$\text{Target Equilibrium:} \quad \frac{\text{Daily Sinks}}{\text{Daily Sources}} \approx 0.85 - 0.95$$

- **Sinks:** Must be recurring, progressive (costs scale with player tier), and tied to desirable quality-of-life or vanity progression.
- **Drop Tables & Monte Carlo Simulation:** Run $1,000,000$ simulated player loot drops using Monte Carlo algorithms to verify that rare item drop rates (e.g. $0.5\%$) do not create catastrophic player progression droughts.
