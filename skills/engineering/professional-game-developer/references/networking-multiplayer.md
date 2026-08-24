# Networking & Multiplayer Architecture — Senior Level

## 1. Network Authority & Topology

Multiplayer architecture begins with the **Authority Contract**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           Dedicated Server Topology                         │
├──────────────────────────────────────┬──────────────────────────────────────┤
│ Client Simulation (Unverified)       │ Server Simulation (Authoritative)    │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ 1. Sample Local Input                │ 1. Ingest Client Inputs              │
│ 2. Predict Movement Immediately      │ 2. Validate Inputs & Cooldowns       │
│ 3. Store Input in Ring Buffer        │ 3. Step Authoritative Physics        │
│ 4. Send `(InputCmd, Tick)` to Server │ 4. Run Lag-Compensated Hit Detection │
│ 5. Receive `(ServerState, AckTick)`  │ 5. Delta-Compress & Replicate State  │
│ 6. Reconcile / Rollback if Desynced  │ 6. Broadcast World State to Clients  │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

---

## 2. Client-Side Prediction & Server Reconciliation

To eliminate perceived latency for the local player, the client predicts physics immediately, while the server validates and corrects:

```
Client Timeline:
Tick 100: Send Input(100) ──> Predict Pos(100) ──> Store in Buffer
Tick 101: Send Input(101) ──> Predict Pos(101) ──> Store in Buffer
...
Tick 105: Receive Server State for Tick 100 (Pos_Server)
          Compare: |Pos_Predicted(100) - Pos_Server| > Threshold?
          YES (Desync Detected):
            1. Snap client position to Pos_Server
            2. Re-simulate Inputs 101 through 105 sequentially
            3. Apply smooth visual offset decay (exponential blend) to prevent snapping
```

---

## 3. Lag Compensation & Server Hit Rewind

For authoritative shooting, melee, and vehicle collisions:

```
1. Client fires at Target at ClientTime T (where T = ServerTime - Ping - InterpolationDelay).
2. Client sends RPC: `Cmd_Fire(TargetID, T, RayOrigin, RayDirection)`.
3. Server receives RPC at ServerTime S.
4. Server retrieves historical bounding boxes from the Server History Buffer at time T.
5. Server tests Raycast against the rewound hitboxes at time T.
6. If Ray intersects, register valid hit and broadcast damage; else reject.
```

**Anti-Cheat Safeguards:**
- **Clamping Rewind Window:** Reject any hit request where `(ServerTime - T) > MaxRewindLimit` (e.g. 200–250 ms max).
- **Line-of-Sight Check:** Verify no solid static geometry occludes the ray path on the server.

---

## 4. Bandwidth Optimization & Delta Compression

In high-concurrency multiplayer (30–100 players), uncompressed transforms will saturate bandwidth limits:

- **Quantization:**
  - Float coordinates: Quantize positions into 16-bit fixed-point integers (`int16`) within world bounds.
  - Rotations: Compress quaternions using **Smallest Three** encoding (store only the smallest 3 components in 48 bits total; reconstruct the 4th on client).
- **Delta Compression:** Replicate only fields that changed since the last acknowledged packet (`AckMask`).
- **Spatial Interest Management (Relevance Grids):**
  - Partition the world into spatial grid cells (e.g. 100m x 100m).
  - High priority / 60 Hz: Entities within immediate proximity (0–50m).
  - Medium priority / 20 Hz: Entities in mid-range (50–200m).
  - Low priority / 5 Hz: Distant entities (>200m).
  - Occluded entities (inside sealed buildings): Cull entirely from replication stream.

---

## 5. Security & RPC Defense

- **Rate-Limiting:** Enforce token-bucket or sliding-window rate limiters per connection on every RPC.
- **Payload Sanitization:** Never trust client-reported positions, velocities, or inventory items.
- **Malformed Packet Handling:** Drop and log invalid packets without crashing or panicking the server thread.
