# AI Onboarding — Claes Storybible

**Canonical cross-model instruction file.** This document applies to ChatGPT, Claude, Gemini, Copilot, local agents and other language models. Model-specific files must defer to this file rather than inventing a parallel interpretation.

## 1. What this repository is

This repository is the operating Storybible and canon-control system for the historical novel **Claes Nissepat**. It contains four distinct layers:

1. **Evidence** — historical/research support (`SRC-*`, `SC.*`).
2. **Story truth** — explicit novel truth (`STC.*`, `DEC.*`, `canon/`).
3. **Narrative meaning** — character, scene, sequence, arc, motif, relationship and value movement (`NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`, `WORLD.*`, `CODE.*`).
4. **Deterministic continuity** — only the subset that can usefully be evaluated as executable logic (`lemma/*.lemma`).

External McKee/NOS knowledge objects (`KO.*`) are narrative theory, not Claes canon.

## 2. Current operating master

The current synchronized human-readable operating master is:

`storybible/LEMMA_MCKEE_MASTER_2026-08-13.md`

The earlier `storybible/LEMMA_MCKEE_MASTER.md` remains in the repository as an audit/work edition and may contain stale migrated representations. When they differ, use the authority hierarchy below and consult `review/SYNC_STATUS.md`.

## 3. Authority hierarchy

When records appear to conflict, use this order:

1. explicit current human author decisions in `canon/` / `DEC.*`;
2. synchronized active `STC.*` Story Claims;
3. synchronized entity/object/narrative registers;
4. `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md`;
5. Revision 11 through `mapping/CONVERSION_LEDGER.yaml` for detail not yet atomized;
6. Source Claims/provenance;
7. `PROPOSED` and `OPEN` records;
8. model inference or session memory — never authoritative.

A Lemma result can test declared constraints. Lemma does not decide literary truth and does not turn historical evidence into canon.

## 4. Required read order

For canon-sensitive work:

1. `README.md`
2. `REPOSITORY_INTEGRITY.md` if you can write
3. `canon/` current decisions
4. `review/SYNC_STATUS.md`
5. `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md`
6. relevant structured registers
7. relevant source claims/provenance
8. relevant Lemma specs only when deterministic reasoning is needed
9. `WRITING_PROTOCOL.md` before drafting or revising prose

For a focused task, retrieve only the records that bear on the question, but never skip the current decisions/sync status when they may affect the answer.

## 5. ID semantics

- `SRC-*` — source/provenance record
- `SC.*` — Source Claim
- `STC.*` — Story Claim
- `DEC.*` — explicit author/canon decision
- `ENT.*` — person/location/entity
- `OBJ.*` — continuity-sensitive object
- `NI.*` — Narrative Instance
- `ARC.*` — character/relationship arc
- `REL.*` — relationship
- `MOTIF.*` — recurring sensory/structural motif
- `THEME.*` — controlling idea, question, desire/need/lie/revelation
- `VALUE.*` — McKee-facing value axis/state
- `WORLD.*` — historical/worldbuilding module
- `CODE.*` — recovery/cryptographic architecture
- `OPEN.*` — unresolved author decision
- `KO.*` — external narrative-theory knowledge object; never Claes canon

## 6. Status semantics

Evidence: `VERIFIED / SUPPORTED / PLAUSIBLE / DISPUTED / UNKNOWN`

Canon: `PROPOSED / CANON / OPEN / DEPRECATED / REJECTED`

Migration origin/review is separate from both. Never collapse these axes and never silently promote `PROPOSED` or `OPEN` material to `CANON`.

## 7. Time and uncertainty

Preserve source/story precision exactly. February remains a month unless a separate author decision establishes a day. A bounded 1568–1569 event remains bounded. Lack of exact precision is information, not a defect to repair by guessing.

Use the repository's half-open ranges consistently: `earliest` inclusive, `latest_exclusive` exclusive.

## 8. Historical-fiction boundary

Always distinguish:

- historically documented;
- evidence-based reconstruction;
- authorial fiction;
- unresolved/open material.

Network proximity does not prove a meeting. A historical print does not prove Claes' fictional provenance. A plausible route does not establish exact topography.

## 9. Narrative interpretation

When interpreting a scene/chapter/sequence, consider POV and knowledge state, objective, psychological/moral need, opening and closing value, conflict/pressure, turning point, claim/relationship/object/knowledge changes, arc movement and motif transformation.

The governing Claes movement is not merely puzzle-solving. The active master defines a longer movement in which embodied *sinne* develops, is constricted by trauma, and later reopens into discernment, responsibility, wisdom and release.

## 10. If you only read or answer questions

You may summarize canon, trace provenance, distinguish evidence from fiction, identify open decisions, explain chronology/knowledge/object states/arcs/motifs, use Lemma for deterministic checks and McKee/NOS for diagnosis. State uncertainty where the repository states uncertainty.

## 11. If you write prose

Read and obey `WRITING_PROTOCOL.md`. Before drafting, identify the relevant `NI.*`, active `STC.*`, participant knowledge states, object states, arc/value movement, current *sinne* state and historical guardrails.

Prose may dramatize within open space but may not accidentally settle an `OPEN.*` matter. If a creative choice would close an open question, leave it open or present it separately as a proposal.

## 12. If you can modify the repository

Read `REPOSITORY_INTEGRITY.md`, `AGENTS.md`, `AUTHORING_POLICY.md` and `review/SYNC_STATUS.md` first.

Mandatory rules include:

- fresh-fetch target branch and every target file immediately before mutation;
- never write from remembered/stale content;
- stop and re-fetch after SHA/409/conflict or unexpected drift;
- never silently overwrite another agent's newer work;
- preserve stable IDs and provenance;
- propagate explicit human decisions downstream;
- if complete propagation is technically impossible, update sync status rather than pretending completion;
- no force push, destructive history rewrite, merge, publication or LemmaBase promotion without explicit human authority.

Required flow:

`source/evidence -> SC.* -> human proposal/decision -> STC.* -> entities/objects/knowledge -> narrative registers -> operating master -> Lemma if deterministic -> validation -> review -> merge/publication`

## 13. If you modify Lemma

Lemma stores constraints, not literary interpretation. Suitable questions include whether people can meet, whether Claes can know/possess/use something at a time, whether prerequisite stages are satisfied, and whether declared temporal/object constraints are compatible.

Emotional power, love, elegance and thematic satisfaction belong to narrative diagnosis, not deterministic Lemma rules.

## 14. Cross-model handoff

At the end of substantial work, record enough repository-visible state for another model to continue: files/records read, files/records changed, current sync status, unresolved matters, validation status and whether human approval remains required. Do not rely on private reasoning or chat memory as canonical storage.
