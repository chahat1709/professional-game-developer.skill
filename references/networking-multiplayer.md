# Networking & Multiplayer — Senior Level

## Authority model (decide first)

- **Authoritative server:** server owns physics, scoring, inventory, mission completion. Client sends intent (input actions), not results. Never trust client-reported "I landed" or "I scored."
- **Client-predicted:** client predicts movement for responsiveness; server corrects. Senior implements prediction + reconciliation, not just replication.
- Roblox = server authority by default. Unreal (NetMode) / Unity (Netcode/Mirror) / Godot (MultiplayerAPI) require explicit ownership and RPC validation.

## Replication & anti-cheat basics

- Replicate: transform (compressed), state (health/score), events (mission done). Do not replicate every component tick at full rate — use relevance, frequency, and delta compression.
- Validate every RPC on server: range checks, rate limits, cooldowns, line-of-sight. Log and drop malformed RPCs, do not crash.
- Senior anti-cheat is design: hide hidden info (fog of war), server-simulate economy, rate-limit market actions. Client-side obfuscation is not security.

## Lag handling

- **Client prediction:** apply input locally, send to server, server re-simulates and sends correction. Smooth correction (lerp), not teleport.
- **Lag compensation:** server rewinds hit checks to client's view time (within capped window). Log ping/jitter; show ping, not just "lag."
- **Interest management:** only replicate what matters to that player (distance, relevance, Data Layer). Streaming + interest together is the senior scaling answer.

## Session & persistence

- Session = lobby → load → play → results → save. GameState/session state is shared truth; PlayerState is per-player. Separate them.
- Save progression server-side with versioning. Client cache is convenience, not source of truth. On disconnect, persist partial session; on reconnect, validate save version before restoring.

## Senior checklist before ship

- [ ] Every gameplay RPC has server validation + rate limit.
- [ ] No gameplay-critical state is client-writable.
- [ ] Prediction/correction tested at 100 ms and 200 ms ping.
- [ ] Relevance and bandwidth profiled at max player count.
