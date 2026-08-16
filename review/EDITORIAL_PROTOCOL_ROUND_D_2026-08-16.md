# Editorial / Reader-Experience Recovery — Round D

**Date:** 16 August 2026  
**Status:** IMPLEMENTED AUTHORING LAYER  
**Scope:** writing quality, pacing, reader experience, scene retention, cold-reader simulation, actual pilot-reader feedback and ruthless-editor mode.

## Why Round D was necessary

The repository already had strong controls for historical evidence, canon, continuity, McKee value movement and the Round-C causal spine. It did **not** yet encode several author-approved editorial commitments recovered from earlier chats:

- prose quality as an explicit gate rather than an assumed virtue;
- pacing as allocation of reader attention;
- reader-experience testing independent of authorial intention;
- cold-reader passes that do not preload the Storybible;
- feedback loops with actual human readers;
- a fixed scene-retention decision: **RETAIN / REVISE / MERGE / CUT**;
- a fixed **Meedogenloze redacteur** mode: hard diagnosis without social cushioning.

Without this layer, a historically accurate and canon-consistent scene could pass repository checks while still being inert fiction.

## Governing files

### Human-facing

- `WRITING_PROTOCOL.md` — complete drafting/revision protocol.
- `review/READER_EXPERIENCE_PROTOCOL.md` — reader testing and feedback method.
- `review/READER_FEEDBACK_TEMPLATE.md` — repeatable feedback record.

### Machine-readable

- `narrative/editorial_gates.yaml` — active editorial gates:
  - `GRD.EDITORIAL.SCENE_NECESSITY`
  - `GRD.EDITORIAL.PROSE_QUALITY`
  - `GRD.EDITORIAL.PACING`
  - `GRD.EDITORIAL.READER_EXPERIENCE`
  - `GRD.EDITORIAL.COLD_READER`
  - `GRD.EDITORIAL.PILOT_READER`
  - `GRD.EDITORIAL.RUTHLESS_EDITOR`

These records are authoring policy, not story canon.

## Scene-retention logic

A scene is tested for:

1. plot necessity;
2. character necessity;
3. information necessity;
4. reader-experience necessity;
5. uniqueness — whether the same function is served better elsewhere.

Verdicts:

- **RETAIN** — necessary and strongest current place/form;
- **REVISE** — necessary function but weak execution;
- **MERGE** — necessary material is duplicated or stronger in combination;
- **CUT** — no indispensable function or all functions are better served elsewhere.

Research effort, historical richness, symbolism and a beautiful passage are not independent retention reasons.

## Reader evidence model

Reader evidence is explicitly separated from reader solutions.

- “I became confused here” = experience/problem evidence.
- “Add a flashback here” = proposed solution.

Repeated independent reports are stronger revision signals than isolated taste. Reader voting does not decide canon or theme.

## Cold-reader boundary

A cold reader must not be given hidden authorial explanation or the Storybible before the pass. The pass checks what the prose itself communicated: causality, desire, change, orientation, attention, expectation and memory.

AI can simulate this restricted-context pass, but actual human readers remain a separate required milestone process. AI simulation is explicitly not treated as a substitute.

## Ruthless-editor mode

Fixed mode name: **Meedogenloze redacteur**.

Operational instruction:

> Niet aardig, wel precies. Als een scène niet werkt, zeg dat. Geen complimenten en geen verzachtende formuleringen wanneer die de diagnose vertroebelen.

Required order: verdict → necessity → primary problem → causality/character → pacing/reader experience → prose → continuity/history → retain/revise/merge/cut.

## Relationship to canon and history

Round D never outranks canon or evidence. It evaluates delivery after possibility and story truth are established.

Conversely, canon and historical accuracy do not prove literary success. A scene can be fully accurate and still be cut.

## Result

After Round D the repository has four distinct readiness steps before large-scale drafting:

1. **A — historical substrate recovered**;
2. **B — practice/world domains chapter-ready**;
3. **C — world projected into causal character architecture**;
4. **D — drafting and reader-evaluation gates operational**.

The next major task can therefore be structural realization: populate Book → Act → Sequence → Chapter → Scene → Beat from the Round-C causal spine, while applying Round-D editorial gates during construction rather than only after a full draft exists.
