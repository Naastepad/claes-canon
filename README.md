# Claes Canon / Storybible — AI Gateway

Lemma-focused, McKee/NOS-inspired operating Storybible and canon-control system for the Claes project.

The active transformed Storybible is currently on branch **`authoring/v1`** in draft PR #1. `main` is the stable public gateway for humans and AI systems.

## AI / agent start here

Before canon-sensitive work, read:

1. `REPOSITORY_INTEGRITY.md` — mandatory for every AI/automation with write access.
2. `AI_ONBOARDING.md` — canonical model-agnostic instructions.
3. `canon/` — explicit human decisions; these outrank conflicting transformed representations.
4. `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` — current synchronized human-readable operating Storybible.
5. `review/SYNC_STATUS.md` — current cross-layer synchronization state.
6. `MIGRATION_REVIEW.md` — migration audit/review state.
7. `WRITING_PROTOCOL.md` — mandatory when drafting, rewriting or critiquing novel prose.
8. `AUTHORING_POLICY.md` and `AGENTS.md` — required for repository/canon/Lemma changes.
9. `prompts/SESSION_BOOTSTRAP.md` — bootstrap prompt for sessions that do not discover repository instructions automatically.

Direct public URLs for restricted chat environments:

- Onboarding: https://raw.githubusercontent.com/Naastepad/claes-canon/main/AI_ONBOARDING.md
- Writing protocol: https://raw.githubusercontent.com/Naastepad/claes-canon/main/WRITING_PROTOCOL.md
- Current synchronized operating Storybible: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/storybible/LEMMA_MCKEE_MASTER_2026-08-13.md
- Repository integrity contract: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/REPOSITORY_INTEGRITY.md
- Sync status: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/review/SYNC_STATUS.md
- Migration review: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/MIGRATION_REVIEW.md
- Draft PR: https://github.com/Naastepad/claes-canon/pull/1

`storybible/LEMMA_MCKEE_MASTER.md` is retained as the earlier transformed work edition for audit/history; while the two differ, the dated synchronized master above is the active operating master.

Model-specific entrypoints (`CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`) defer to the same onboarding rules to prevent instruction drift.

## Four responsibility layers

1. **Evidence** — historical/research support (`SRC-*`, `SC.*`).
2. **Story truth** — what is true in the novel (`STC.*`, `DEC.*`).
3. **Narrative meaning** — where/how truth becomes scene, sequence, arc, motif, relationship and value movement (`NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`, `WORLD.*`, `CODE.*`).
4. **Deterministic consistency** — only the subset that benefits from executable rules (`lemma/*.lemma`).

External McKee/NOS knowledge objects (`KO.*`) are narrative theory, not Claes canon.

## Migration review model

Migration origin is independent from evidence status and canon status:

- `MIGRATED` — existing canon represented in the new architecture; check fidelity, do not re-decide it.
- `DERIVED` — interpretation/condensation derived from existing canon; human review required until explicitly accepted.
- `NEW` — genuinely new story choice; explicit author decision required.
- `CONFLICT` — canon drift or incompatible authorities; must be resolved before merge/publication.

The machine-readable registry is `review/MIGRATION_REVIEW.yaml`; the human review sheet is `MIGRATION_REVIEW.md`.

## Revision 11 transmutation

Revision 11 was parsed as a source edition of 3803 lines and 296 headings, SHA-256:

`e38430f0165e7c0779a8ae6bba6a208773c677682f55295a940e91fdb2ed9edd`

All 31 top-level sections are accounted for in `mapping/CONVERSION_LEDGER.yaml`. Material not yet atomized remains active source authority and is never treated as absent merely because no separate structured record exists yet.

## Repository layout

- `storybible/` — transformed operating masters and transformation ledger.
- `review/` — migration review and cross-session synchronization status.
- `mapping/` — exact source-to-structured conversion ledger and completeness report.
- `claims/` — Source Claims, Story Claims and decisions.
- `entities/` — stable persons and locations.
- `objects/` — continuity-sensitive objects and biographies.
- `narrative/` — Narrative Instances, arcs, motifs, relationships, themes/value axes, knowledge states, world modules and code architecture.
- `canon/` — explicit human decisions and unresolved author decisions.
- `sources/` — provenance registry.
- `proposals/` — reviewable AI/human change proposals.
- `lemma/` — executable deterministic constraints only.
- `scripts/validate_canon.py` — continuity compiler.
- `.github/` — Lemma and continuity CI.

## Truth flow

`historical source -> SC.* -> human proposal/decision -> STC.* -> entities/narrative/storybible -> Lemma when deterministic`

Narrative diagnosis runs in the other direction:

`KO.* narrative theory + NI.* Claes instance -> analysis / diagnostic`

## Status axes

Evidence:
`VERIFIED / SUPPORTED / PLAUSIBLE / DISPUTED / UNKNOWN`

Canon:
`PROPOSED / CANON / OPEN / DEPRECATED / REJECTED`

Migration origin:
`MIGRATED / DERIVED / NEW`

Migration review:
`MIGRATION_CHECK / HUMAN_REVIEW / HUMAN_DECISION / CONFLICT`

These axes answer different questions and must not be collapsed.

## Claude Chat / restricted web-fetch environments

If a chat environment cannot freely follow GitHub links discovered inside pages, provide the exact `raw.githubusercontent.com` URL from the list above. Do not infer that repository content is unavailable until the direct file URL has been tried.

For arbitrary repository traversal or commits, use an environment with repository access such as Claude Code, ChatGPT with GitHub connector, GitHub Copilot/Coding Agent or a local git checkout.

## Non-negotiable authoring rule

AI may read, extract, compare, propose, structure, synchronize approved decisions, validate and draft. AI does **not** silently promote hypotheses, close open decisions, resolve conflicts, overwrite concurrent work, merge, rewrite history, or publish to LemmaBase without explicit human approval.
