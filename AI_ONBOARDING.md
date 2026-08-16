# AI Onboarding — Claes Storybible

**Canonical cross-model instruction file.** This document applies to ChatGPT, Claude, Gemini, Copilot, local agents and other language models. Model-specific files must defer to this file rather than inventing a parallel interpretation.

## 1. What this repository is

This repository is the operating Storybible and canon-control system for the historical novel **Claes Nissepat**. It contains six distinct working layers:

1. **Evidence** — historical/research support (`SRC-*`, `SC.*`).
2. **Story truth** — explicit novel truth (`STC.*`, `DEC.*`, `canon/`).
3. **World/practice state** — time-bounded historical environments and chapter-ready activity domains (`WORLD.*`, `storybible/domains/`, `narrative/domain_scene_packs.yaml`).
4. **Narrative meaning/projection** — character, causal spine, scene, sequence, arc, motif, relationship and value movement (`NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`).
5. **Editorial / reader validation** — prose quality, pacing, scene necessity, reader experience and feedback (`WRITING_PROTOCOL.md`, `narrative/editorial_gates.yaml`, `review/READER_EXPERIENCE_PROTOCOL.md`).
6. **Deterministic continuity** — only the subset that can usefully be evaluated as executable logic (`lemma/*.lemma`).

External McKee/NOS knowledge objects (`KO.*`) are narrative theory, not Claes canon.

## 2. Current operating authorities

The current synchronized human-readable operating master is:

`storybible/LEMMA_MCKEE_MASTER.md`

The dated `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` is a **legacy snapshot** retained for audit/development history and may contain superseded chronology or architecture.

Operational navigation is `storybible/INDEX.md`.

For causal chapter construction, read:

`storybible/STORY_PROJECTION_ROUND_C.md`

Its machine-readable projection is `narrative/story_projection_round_c.yaml`.

For drafting, revision and reader evaluation, read:

- `WRITING_PROTOCOL.md`;
- `narrative/editorial_gates.yaml`;
- `review/READER_EXPERIENCE_PROTOCOL.md`;
- `review/READER_FEEDBACK_TEMPLATE.md` when logging a real or simulated reader pass.

## 3. Authority hierarchy

When records appear to conflict, use this order:

1. explicit current human author decisions in `canon/` / latest applicable `DEC.*`;
2. synchronized active `STC.*` Story Claims;
3. dedicated current governing dossiers and synchronized entity/object/narrative registers;
4. `storybible/LEMMA_MCKEE_MASTER.md`;
5. Revision 11 through `mapping/CONVERSION_LEDGER.yaml` for detail not yet atomized;
6. Source Claims/provenance;
7. `PROPOSED` and `OPEN` records;
8. dated legacy masters, model inference or session memory — never authoritative.

Editorial protocols do **not** override canon. They govern whether canon has been dramatized effectively. A `CUT` verdict means a scene is weak or unnecessary, not that its underlying canon becomes false.

A Lemma result can test declared constraints. Lemma does not decide literary truth and does not turn historical evidence into canon.

## 4. Required read order

For canon-sensitive work:

1. `README.md`
2. `REPOSITORY_INTEGRITY.md` if you can write
3. current `canon/` decisions and `canon/OPEN_DECISIONS.yaml`
4. `review/SYNC_STATUS.md`
5. `storybible/MASTER.md`
6. `storybible/INDEX.md`
7. `storybible/LEMMA_MCKEE_MASTER.md`
8. relevant structured registers and current governing dossier(s)
9. relevant source claims/provenance
10. relevant Lemma specs only when deterministic reasoning is needed

### Additional required read order for chapter/scene construction

Before building a chapter or scene, also load:

1. `storybible/STORY_PROJECTION_ROUND_C.md`;
2. `narrative/story_projection_round_c.yaml` and identify the causal hinge;
3. `narrative/alchemical_authorial_architecture.yaml` when Great-Work/Corpus-Anima-Spiritus structure matters;
4. the relevant `narrative/domain_scene_packs.yaml` pack(s);
5. relevant time-sliced world/practice dossier(s);
6. participant arcs/relationships/knowledge states;
7. if Mayken appears: `narrative/mayken_independent_arc.yaml` as well as the Claes-Mayken relationship projection;
8. `WRITING_PROTOCOL.md`;
9. `narrative/editorial_gates.yaml`.

A chapter is not justified merely because research material exists. It must create pressure, choice, consequence, relationship movement or necessary reader experience.

### Additional required read order for critique/revision

Before judging literary quality, also read:

- `review/READER_EXPERIENCE_PROTOCOL.md`;
- any relevant `review/READER_FEEDBACK_*` record;
- the active Round-D gate definitions in `narrative/editorial_gates.yaml`.

Do **not** line-polish a scene before deciding whether it is `RETAIN`, `REVISE`, `MERGE` or `CUT`.

## 5. ID semantics

- `SRC-*` — source/provenance record
- `SC.*` — Source Claim
- `STC.*` — Story Claim
- `DEC.*` — explicit author/canon decision
- `ENT.*` — person/location/entity
- `OBJ.*` — continuity-sensitive object
- `NI.*` — Narrative Instance
- `ARC.*` — character/relationship/macro/authorial causal architecture
- `REL.*` — relationship
- `MOTIF.*` — recurring sensory/structural motif
- `THEME.*` — controlling idea, question, desire/need/lie/revelation
- `VALUE.*` — McKee-facing value axis/state
- `WORLD.*` — historical/worldbuilding module
- `GRD.*` — authoring/editorial guardrail or gate; never story truth by itself
- `CODE.*` — legacy/recovery architecture namespace where still present
- `OPEN.*` — unresolved author decision
- `KO.*` — external narrative-theory knowledge object; never Claes canon

## 6. Status semantics

Evidence: `VERIFIED / SUPPORTED / PLAUSIBLE / DISPUTED / UNKNOWN`

Canon: `PROPOSED / CANON / OPEN / DEPRECATED / REJECTED`

Editorial scene verdict: `RETAIN / REVISE / MERGE / CUT`

Reader-evidence classification: `ISOLATED / REPEATED / CONVERGENT / RESOLVED / INTENTIONAL_VARIANCE`

These axes are separate. Never convert editorial dislike into canon change or reader preference into historical evidence.

## 7. Time and uncertainty

Preserve source/story precision exactly. February remains a month unless a separate author decision establishes a day. A bounded interval remains bounded. Lack of exact precision is information, not a defect to repair by guessing.

Use the repository's half-open ranges consistently: `earliest` inclusive, `latest_exclusive` exclusive.

## 8. Historical-fiction boundary

Always distinguish:

- historically documented;
- evidence-based reconstruction;
- authorial fiction;
- unresolved/open material.

Network proximity does not prove a meeting. A historical print does not prove Claes' fictional provenance. A plausible route does not establish exact topography. A later manual does not automatically establish earlier practice.

## 9. Narrative interpretation

When interpreting a scene/chapter/sequence, consider POV and knowledge state, objective, psychological/moral need, opening and closing value, conflict/pressure, turning point, claim/relationship/object/knowledge changes, arc movement, motif transformation **and reader-state change**.

The governing Claes movement combines:

- `ARC.CLAES.MACRO_TRANSMUTATION` — Drager/Nigredo/Albedo/Rubedo/Projectio;
- `ARC.CLAES.GREAT_WORK.AUTHORIAL` — Status Prima; interwoven Corpus/Anima/Spiritus; Transmutatio; Projectio; Status Prima Nova;
- `ARC.CLAES.SINNE_RECOVERY` — openness, vigilance, constriction, recovery, resonance, sovereignty;
- `ARC.CLAES.CAUSAL_SPINE` — current pre-chapter causal hinge map.

Corpus/Anima/Spiritus are author-side registers, not a forced three-cycle structure or in-world doctrine.

## 10. Mayken rule

`ENT.PERSON.BELOVED` is the legacy technical entity ID for the **resolved** character Mayken Adriaensdr. Lampert. Her identity is not open.

If Mayken appears, consult:

- `storybible/MAYKEN_LAMPERT.md`;
- `narrative/mayken_independent_arc.yaml` (`ARC.MAYKEN.LIFE`);
- `narrative/mayken_relationship_projection.yaml` (`REL.CLAES.MAYKEN.CONJUNCTIO`);
- `narrative/beloved_recovery.yaml` only as a resolved-identity relationship extension.

Never load Mayken only as “Claes' beloved”. A developed Mayken scene must give her an objective, judgement, cost or choice of her own.

## 11. If you only read or answer questions

You may summarize canon, trace provenance, distinguish evidence from fiction, identify open decisions, explain chronology/knowledge/object states/arcs/motifs, use Lemma for deterministic checks and McKee/NOS for diagnosis. State uncertainty where the repository states uncertainty.

## 12. If you write prose

Read and obey `WRITING_PROTOCOL.md`. Before drafting, identify:

- the causal hinge from `ARC.CLAES.CAUSAL_SPINE`;
- relevant `NI.*` and active `STC.*`;
- participant knowledge/object states;
- active character/relationship arcs;
- current `sinne` state;
- applicable Corpus/Anima/Spiritus register(s);
- relevant domain scene pack and historical guardrails;
- unresolved `OPEN.*` matters that prose must not accidentally settle;
- intended reader movement: orientation, curiosity, emotion, tension, cognitive load and forward expectation.

Prose may dramatize within open space but may not accidentally close an `OPEN.*` matter. If a creative choice would close an open question, leave it open or present it separately as a proposal.

## 13. If you critique or revise prose

Apply the Round-D gates in this order:

1. scene necessity;
2. `RETAIN / REVISE / MERGE / CUT`;
3. causality and character choice;
4. pacing and reader experience;
5. prose quality;
6. continuity/history risk;
7. reader evidence and retest need.

For a hard editorial pass, use `GRD.EDITORIAL.RUTHLESS_EDITOR` / **Meedogenloze redacteur**:

> Niet aardig, wel precies. Als een scène niet werkt, zeg dat. Geen complimenten en geen verzachtende formuleringen wanneer die de diagnose vertroebelen.

Do not praise accurate research as compensation for weak fiction.

## 14. Cold-reader and pilot-reader rule

A cold-reader pass must not preload the Storybible or intended interpretation. It tests what the prose itself communicated.

AI may simulate a cold reader under restricted context, but **AI cold-reader simulation is not a substitute for actual human pilot readers**.

Actual reader feedback is logged as experience/problem evidence separate from the reader's proposed fix. Repeated independent observations are stronger revision signals than isolated preferences. Reader voting never decides canon or theme.

Use `review/READER_FEEDBACK_TEMPLATE.md`.

## 15. If you can modify the repository

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

`source/evidence -> SC.* -> human proposal/decision -> STC.* -> entities/objects/knowledge -> world/practice domains -> narrative projection/arcs/relationships -> operating master/index -> prose/scene implementation -> Round-D editorial gates + reader evidence -> Lemma if deterministic -> validation -> review -> merge/publication`

## 16. If you modify Lemma

Lemma stores constraints, not literary interpretation. Suitable questions include whether people can meet, whether Claes can know/possess/use something at a time, whether prerequisite stages are satisfied, and whether declared temporal/object constraints are compatible.

Emotional power, love, elegance, pacing, reader engagement and thematic satisfaction belong to narrative/editorial diagnosis, not deterministic Lemma rules.

## 17. Cross-model handoff

At the end of substantial work, record enough repository-visible state for another model to continue: files/records read, files/records changed, current sync status, unresolved matters, validation status, editorial verdicts/reader evidence where relevant and whether human approval remains required. Do not rely on private reasoning or chat memory as canonical storage.
