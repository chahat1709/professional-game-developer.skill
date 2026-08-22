# Production Leadership — Senior Level

A senior ships games by protecting the team, not just the code.

## Sprint & risk (senior habits)

- **Risk-first ordering:** riskiest system first, not easiest. If the landing prediction / netcode / asset pipeline can fail the project, prove it in the first slice. Easy UI polish is last.
- **One vertical slice > ten half-features:** polish one playable loop to production quality before multiplying content. Stakeholders can judge a loop; they cannot judge a checklist.
- **Definition of done:** build + runtime + visual evidence + test. No "code done, will test later." If any evidence missing, milestone is incomplete — say so plainly.

## Code review bar

- Review for: ownership (who owns this rule?), determinism, failure handling, testability, performance awareness, and asset provenance — not just style.
- Require: narrow ownership, single source of truth for each rule, fallback for every external dependency (asset, hardware, network). Reject hidden globals, silent fallbacks, and duplicated rules in code + visual scripting.
- Praise quickly, block firmly. A senior blocks a risky merge even if it delays a demo — a broken main costs more.

## Tech debt & scope

- Track debt explicitly: `// TECH-DEBT(R-07): ...` with ID linked to risk register. Budget debt paydown each sprint; do not let it accumulate silently.
- When scope changes, revise the brief, risk register, asset manifest, and milestone order *before* coding. Separate must-ship / should-ship / later. Say no to later in writing.
- Know when to cut: if a feature cannot hit the frame budget or visual bar in the slice, cut it and note the blocker — do not ship a "maybe."

## Mentoring & communication

- Explain the *why* behind the pattern (determinism, observability, replaceability), not just the how.
- Give juniors one focused next step, not ten. Provide a test that proves success so they can move without you.
- Status reports are: goal, systems changed, build/runtime/visual evidence, tests, known issues, next smallest step. No "almost done."

## Senior heuristics

- If it cannot be observed in logs/metrics, it will fail in production.
- If two places own the same rule, one is lying.
- If it works only on your machine, it does not work.
- Ship the smallest build that proves the loop; add content only when the loop is fun and stable at budget.
