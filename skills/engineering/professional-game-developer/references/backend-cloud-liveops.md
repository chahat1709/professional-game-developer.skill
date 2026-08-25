# Backend, Cloud Infrastructure & LiveOps — Senior Backend Engineer

This reference details dedicated game server orchestration (Agones/Kubernetes), matchmaking rating algorithms, persistent distributed player databases, and server-side anti-cheat heuristics.

---

## 1. Dedicated Game Server Fleet Orchestration (Agones / Kubernetes)

Multiplayer game servers (Unreal Dedicated Server / Unity Headless Server) are containerized and scaled dynamically across global cloud regions:

```
[ Client Matchmaking Request ] ──> [ Matchmaker Service ]
                                           │
                                           ▼
[ Agones Fleet Controller (Kubernetes) ] ──> [ Allocates Dedicated Server Pod (UDP Port) ]
                                           │
                                           ▼
[ Client Connects Directly via UDP: IP:Port ] ──> [ 60 Hz Dedicated Simulation Pod ]
```

- **Server Lifecycle States:** `Ready` ──> `Allocated` ──> `InGame` ──> `GameOver` ──> `Shutdown / Recycle`.
- **Zero-Downtime Rolling Deploys:** Spin up new game server fleets with updated build versions; existing matches run to completion on legacy fleets while new matches route exclusively to updated fleets.

---

## 2. Competitive Matchmaking Algorithms (Glicko-2 / Elo)

Never match competitive players with naive random pairing:

### Glicko-2 Matchmaking Rating Parameters:
1. **Rating ($\mu$):** Player estimated skill level (e.g. $1500$).
2. **Rating Deviation ($\phi$):** Uncertainty in player rating (decreases with match volume; increases during inactivity).
3. **Volatility ($\sigma$):** Degree of erratic performance fluctuations.

### Match Quality Function:
$$Q(A, B) = \exp\left( -\frac{(\mu_A - \mu_B)^2}{2(\phi_A^2 + \phi_B^2)} \right)$$
- Expand matchmaking search radius over time ($t$ seconds) if match quality threshold $Q$ is not satisfied within initial $15\text{s}$ queue window.

---

## 3. High-Throughput Player Profile Storage (Redis + PostgreSQL)

```
[ Game Server Pod ] ── (Write Cache / Session Data) ──> [ Redis Memory Cluster (In-Memory) ]
                                                                   │
                                                                   ▼ (Asynchronous Write-Behind)
                                                        [ PostgreSQL Persistent Cluster ]
```

- **Session Locking:** Acquire distributed Redlock on player UUID upon login to prevent concurrent duplicate login inventory duplication exploits across multiple game servers.
- **Transactional Atomic Item Swaps:** Enforce ACID transactions for all inventory trading:
  ```sql
  BEGIN;
  UPDATE inventory SET owner_id = 'user_B' WHERE item_uuid = 'item_982' AND owner_id = 'user_A';
  UPDATE currency SET balance = balance + 500 WHERE user_id = 'user_A';
  UPDATE currency SET balance = balance - 500 WHERE user_id = 'user_B';
  COMMIT;
  ```
