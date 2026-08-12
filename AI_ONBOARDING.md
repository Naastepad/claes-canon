# AI Onboarding — Claes Storybible

**Canonical cross-model instruction file.** This document is written for ChatGPT, Claude, Gemini, Copilot, local agents and other language models. Model-specific files such as `AGENTS.md`, `CLAUDE.md` and `.github/copilot-instructions.md` must defer to this file rather than inventing a parallel interpretation of the project.

## 1. What this repository is

This repository is the operating Storybible and canon-control system for the historical novel **Claes Nissepat**. It is not merely a folder of notes and it is not merely a Lemma rules repository.

It contains four distinct layers:

1. **Evidence** — historical/research support (`SRC-*`, `SC.*`).
2. **Story truth** — what the author has decided is true inside the novel (`STC.*`, `DEC.*`).
3. **Narrative meaning** — how story truth becomes character, scene, sequence, arc, motif, relationship and value movement (`NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`, `WORLD.*`).
4. **Deterministic continuity** — only the subset that can usefully be evaluated as executable logic (`lemma/*.lemma`).

External McKee/NOS knowledge objects (`KO.*`) are **narrative theory**, not Claes canon. They may be used to diagnose scenes and arcs but may never override story truth.

## 2. Authority hierarchy

When two records appear to conflict, resolve them in this order:

1. Explicit current human author decision.
2. Active `STC.*` Story Claim with `canon_status: CANON` and its `DEC.*` decision record.
3. Structured operating Storybible records (`ENT.*`, `OBJ.*`, `NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`, `WORLD.*`, `CODE.*`).
4. `storybible/LEMMA_MCKEE_MASTER.md` as the coherent human-readable operating synthesis.
5. The exact Revision 11 source edition for detail not yet atomized, as tracked through `mapping/CONVERSION_LEDGER.yaml`.
6. `PROPOSED` and `OPEN` records — informative but not settled canon.
7. Historical inference or model-generated suggestion — never canon unless explicitly promoted.

A Lemma result can prove that a declared combination is or is not logically compatible with the encoded constraints. Lemma does **not** decide literary truth by itself and does not turn historical evidence into canon.

## 3. Required read order

For a general project question, read:

1. `README.md`
2. `storybible/LEMMA_MCKEE_MASTER.md`
3. `AI_ONBOARDING.md`
4. the relevant structured registers
5. relevant source claims/provenance
6. relevant Lemma specs when the question is deterministic

For a focused task, do not load the whole repository blindly. Retrieve the records that bear on the question, but always inspect the operating master and any linked canonical claims before making a canon-sensitive assertion.

## 4. How to interpret IDs

- `SRC-*` — source/provenance record
- `SC.*` — Source Claim: what evidence supports
- `STC.*` — Story Claim: what is true in the novel
- `DEC.*` — explicit canon decision/audit record
- `ENT.*` — person/location/entity
- `OBJ.*` — continuity-sensitive object
- `NI.*` — Narrative Instance: event, sequence, chapter, scene or beat
- `ARC.*` — character or relationship arc
- `REL.*` — relationship
- `MOTIF.*` — recurring image, sensory pattern or structural motif
- `THEME.*` — controlling idea, dramatic question, desire/need/lie/revelation
- `VALUE.*` — McKee-facing value axis or value state
- `WORLD.*` — historical/worldbuilding module
- `CODE.*` — cryptographic/recovery architecture
- `OPEN.*` — unresolved author decision
- `KO.*` — external narrative-theory knowledge object; never Claes canon

## 5. Status semantics

Evidence status and canon status answer different questions and must never be collapsed.

Evidence:

`VERIFIED / SUPPORTED / PLAUSIBLE / DISPUTED / UNKNOWN`

Canon:

`PROPOSED / CANON / OPEN / DEPRECATED / REJECTED`

Examples:

- A historical event can be `VERIFIED` but absent from the novel.
- A fictional meeting can be `PLAUSIBLE + CANON`.
- A model suggestion can be `SUPPORTED + PROPOSED` but is not yet story truth.

Never silently promote `PROPOSED` or `OPEN` to `CANON`.

## 6. Time and uncertainty

Preserve the source precision exactly.

If a record says February 1563, do not invent 16 February 1563. If a life event is bounded to 1568–1569, do not write an exact arrest or death date unless another canonical record closes it.

Use half-open time ranges where the repository does so: `earliest` is inclusive; `latest_exclusive` is exclusive.

A lack of exact date is information, not a defect to repair by guessing.

## 7. Historical-fiction boundary

Always separate:

- what is historically documented;
- what is reconstructed from evidence;
- what is authorial fiction;
- what is still open.

Network proximity does not prove a meeting. A real printed book does not prove Claes' fictional provenance. A plausible trade route does not prove a precise parcel location. The repository intentionally preserves these distinctions.

## 8. Reading the Storybible as narrative, not just data

When interpreting a scene, chapter or sequence, consider at least:

- point of view and knowledge state;
- conscious desire;
- psychological and moral need;
- value at entry and value at exit;
- conflict/pressure;
- turning point or revelation;
- what claim, relationship, object state or knowledge state changes;
- which arc advances;
- which motif is planted, transformed or paid off;
- whether the scene changes the story or merely transports information.

The governing Claes movement is not “solve the puzzle.” It is the lifelong movement from **perception → understanding → control → responsibility → release**. The controlling idea and dramatic question in `storybible/LEMMA_MCKEE_MASTER.md` govern interpretation.

## 9. If you are only reading or answering questions

You may:

- summarize active canon;
- trace why something is canon;
- distinguish evidence from fiction;
- identify open decisions;
- explain chronology, knowledge, object provenance, arcs and motifs;
- use Lemma for deterministic consistency when available;
- use McKee/NOS theory for diagnosis when relevant.

You must state uncertainty when the repository states uncertainty. Do not fill gaps with plausible-sounding invention.

## 10. If you are allowed to write prose

Before drafting a scene or chapter, follow `WRITING_PROTOCOL.md`.

Minimum requirement: identify the relevant `NI.*`, active `STC.*` claims, participant knowledge states, object states, arc/value movement and historical guardrails **before** writing prose.

New prose must obey active canon. Prose may dramatize within open space, but it may not close an `OPEN.*` decision by accident.

If a creative choice would decide an open matter, either:

1. leave it deliberately unresolved in the prose; or
2. present the choice as a proposal for human approval before treating it as canon.

## 11. If you are allowed to modify the Storybible/repository

Follow `AUTHORING_POLICY.md` and `AGENTS.md`.

Required flow:

`source/evidence -> SC.* -> STC.* -> DEC./review -> narrative records -> Lemma if deterministic -> validation -> human approval`

Do not rewrite the Storybible merely to make the schema look cleaner. Preserve meaning and provenance. Never delete an older active truth without either deprecating/superseding it explicitly or recording the human decision that replaced it.

## 12. If you are allowed to modify Lemma

Lemma stores constraints, not literary interpretation.

A suitable Lemma question is:

- Can these two people meet on this date in this place?
- Can Claes possess this object yet?
- Can he know this information by this point?
- Are the prerequisite stages of the recovery chain satisfied?

Unsuitable Lemma questions include:

- Is this scene moving?
- Is Claes acting out of love?
- Is this motif elegant?
- Is the chapter thematically satisfying?

Those belong to narrative diagnosis, not deterministic rules.

## 13. Required response discipline for canon-sensitive work

When practical, make clear which kind of statement you are making:

- **Canon:** active novel truth.
- **Evidence:** historical/research support.
- **Open:** unresolved author decision.
- **Proposal:** suggested new story choice.
- **Inference:** model reasoning not yet represented as canon.

Do not present an inference in the grammatical voice of settled fact.

## 14. Cross-model handoff

At the end of substantial canon-sensitive work, leave enough information for another model to continue without reconstructing your private reasoning. Record:

- records read;
- records changed;
- assumptions made;
- decisions still open;
- validation status;
- whether anything requires human approval.

Do not rely on chat memory as canonical storage. If a decision matters beyond the session, it belongs in the repository through the controlled authoring flow.
