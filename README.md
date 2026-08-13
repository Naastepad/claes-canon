# Claes Canon / Storybible — AI Gateway

Lemma-based, McKee/NOS-inspired operating Storybible and canon-control system for the Claes project.

**`main` is the canonical source of truth and canonical storage.** PR #1 has been merged; `authoring/v1` and the former draft PR are historical development state, not active canon.

## AI / agent start here
Before canon-sensitive work, read:
1. `REPOSITORY_INTEGRITY.md`
2. `AI_ONBOARDING.md`
3. `canon/` current human decisions
4. `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md`
5. `review/SYNC_STATUS.md`
6. `MIGRATION_REVIEW.md`
7. `WRITING_PROTOCOL.md` before prose work
8. `AUTHORING_POLICY.md` and `AGENTS.md` before repository/canon/Lemma changes
9. `prompts/SESSION_BOOTSTRAP.md` when repository instructions are not discovered automatically

Direct public URLs for restricted chat environments:
- Onboarding: https://raw.githubusercontent.com/Naastepad/claes-canon/main/AI_ONBOARDING.md
- Writing protocol: https://raw.githubusercontent.com/Naastepad/claes-canon/main/WRITING_PROTOCOL.md
- Operating Storybible: https://raw.githubusercontent.com/Naastepad/claes-canon/main/storybible/LEMMA_MCKEE_MASTER_2026-08-13.md
- Repository integrity: https://raw.githubusercontent.com/Naastepad/claes-canon/main/REPOSITORY_INTEGRITY.md
- Sync status: https://raw.githubusercontent.com/Naastepad/claes-canon/main/review/SYNC_STATUS.md
- Migration review: https://raw.githubusercontent.com/Naastepad/claes-canon/main/MIGRATION_REVIEW.md

`storybible/LEMMA_MCKEE_MASTER.md` is retained only as an earlier transformed work edition/audit artifact. The dated synchronized master is active.

## Four responsibility layers
1. **Evidence** — historical/research support (`SRC-*`, `SC.*`).
2. **Story truth** — novel truth and human decisions (`STC.*`, `DEC.*`).
3. **Narrative meaning** — instances, arcs, motifs, relationships, themes, values and world/code architecture (`NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`, `WORLD.*`, `CODE.*`).
4. **Deterministic consistency** — executable rules only (`lemma/*.lemma`).

External McKee/NOS knowledge objects (`KO.*`) are narrative theory, not Claes canon.

## GitHub + Lemma
GitHub is the complete operating environment:

`evidence -> canon -> narrative model -> Lemma constraints -> validation/CI`

The `.lemma` files are the deterministic rules-as-code layer of the Storybible and are versioned, reviewed and validated together with all other canon material. Lemma is not prose storage and does not decide literary truth.

**LemmaBase is optional and is not part of the canonical architecture.** Authoring, canon control, writing, validation and continuity checking do not depend on it. Any future external Lemma runtime is downstream-only and never outranks or writes back over GitHub `main`.

## Repository layout
- `storybible/` — operating masters and transformation ledger
- `canon/` — explicit human decisions and unresolved author decisions
- `claims/` — Source Claims and Story Claims
- `entities/` — stable persons and locations
- `objects/` — continuity-sensitive objects and biographies
- `narrative/` — Narrative Instances, arcs, motifs, relationships, themes/values, knowledge states, world modules and code architecture
- `sources/` — provenance registry
- `proposals/` — reviewable change proposals
- `review/` — migration and synchronization state
- `mapping/` — source-to-structured conversion ledger
- `lemma/` — executable deterministic constraints
- `scripts/validate_canon.py` — continuity compiler
- `.github/` — continuity and Lemma CI

## Truth flow
`historical source -> SC.* -> human proposal/decision -> STC.* -> entities/narrative/storybible -> Lemma when deterministic`

Narrative diagnosis:
`KO.* narrative theory + NI.* Claes instance -> analysis / diagnostic`

## Status axes
Evidence: `VERIFIED / SUPPORTED / PLAUSIBLE / DISPUTED / UNKNOWN`

Canon: `PROPOSED / CANON / OPEN / DEPRECATED / REJECTED`

Migration origin: `MIGRATED / DERIVED / NEW`

These axes answer different questions and must not be collapsed.

## Non-negotiable authoring rule
AI may read, extract, compare, propose, structure, synchronize approved decisions, validate and draft. AI does **not** silently promote hypotheses, close open decisions, resolve conflicts, overwrite concurrent work, merge, rewrite history, or promote canon without explicit human approval.
