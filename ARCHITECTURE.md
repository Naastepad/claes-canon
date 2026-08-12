# Claes Storybible Architecture

## Core distinction

`claes-canon` is the project-specific truth, continuity and narrative-instance layer for the novel. It is inspired by the McKee/NOS Knowledge Object architecture but does not absorb universal narrative theory.

Three systems remain distinct:

### 1. Narrative Knowledge Base — external
Universal craft knowledge from McKee, Truby, Coyne, Weiland and other sources.

Typical objects:
- `KO.SCENE`
- `KO.EVENT`
- `KO.VALUE`
- `KO.CONFLICT`
- `KO.STRUCTURE`

This layer answers: **what narrative principles exist and how can a story instance be diagnosed?**

### 2. Claes Storybible / Canon — this repository
Project truth, provenance and dramatic realization.

Flow:

`Historical sources -> SC.* Source Claims -> STC.* Story Claims -> DEC.* human decisions -> ENT./OBJ. -> NI./ARC./MOTIF./REL.`

This layer answers: **what is true in Claes, why is it true, and where/how is it dramatized?**

### 3. Lemma — deterministic projection
Only constraints that can be meaningfully evaluated as rules:
- temporal windows;
- knowledge acquisition;
- encounters;
- possession/object availability;
- clue dependencies;
- final consistency gates.

This layer answers: **can these accepted story truths coexist under the declared constraints?**

## McKee/NOS bridge

Narrative Instances are the interface:

`KO.* + NI.* -> diagnostic`

Example: a concrete Claes scene may point to `KO.VALUE`, `KO.CONFLICT` and `KO.SCENE`, allowing an external reasoning engine to ask whether the scene turns a value, applies pressure and produces a meaningful event.

The theoretical KO remains universal; the NI remains specific to Claes.

## Conversion of Revision 11

The source master is preserved by SHA-256 and line identity. `mapping/CONVERSION_LEDGER.yaml` accounts for all 31 top-level sections and maps each to structured targets. `mapping/CONVERSION_REPORT.yaml` states what is and is not yet atomized.

The structured operating storybible currently comprises:
- story claims;
- source claims;
- decisions;
- entities;
- object registry + object biographies;
- narrative instances;
- character/relationship/macro arcs;
- motifs;
- knowledge states;
- craft guardrails;
- open decisions;
- executable Lemma constraints.

Unatomized prose remains active source material. Conversion is therefore loss-preserving rather than destructive.

## Status model

Evidence and canon are separate dimensions.

Evidence:
`VERIFIED / SUPPORTED / PLAUSIBLE / DISPUTED / UNKNOWN`

Canon:
`PROPOSED / CANON / OPEN / DEPRECATED / REJECTED`

A historically verified statement is not automatically story canon. A fictional but plausible event can be `PLAUSIBLE + CANON` by explicit author decision.

## Precedence

1. Explicit current human decisions (`DEC.*`).
2. Active Story Claims (`STC.*`).
3. Lossless Revision 11 prose for material not yet atomized.
4. Structured Narrative Instances for realization in the book.
5. Lemma for consistency, never invention.

Any conflict enters `proposals/`; no layer silently overwrites another.

## Validation

Two independent CI layers run on pull requests:

- **Validate Claes canon repository** — IDs, references, vocabularies, source records, time windows and conversion-ledger coverage.
- **Validate Lemma canon** — parses/discovers every active Lemma spec under the pinned Lemma release.

This makes GitHub both the review history and the continuity compiler for the novel.
