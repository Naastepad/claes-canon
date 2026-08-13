# PROP-0001 — First encounter with John Dee, February 1563

## Status
MIGRATED TO STRUCTURED CLAIM MODEL — not yet instantiated as an encounter-specific Lemma rule.

## Source Claim

`SC.HIST.DEE_SILVIUS.1563.001`

John Dee is supported as present in Willem Silvius' Antwerp environment in February 1563.

- evidence status: `SUPPORTED`
- source record: `SRC-HIST-1563-DEE-SILVIUS-001`
- function: historical plausibility anchor only

## Story Claim

`STC.CLAES.DEE_ENCOUNTER.1563.001`

Claes first meets John Dee in February 1563 in or around Silvius' Gulden Engel in Antwerp.

- evidence status: `PLAUSIBLE`
- canon status: `CANON`
- decision: `DEC.CLAES.DEE_ENCOUNTER.001`
- narrative instance: `NI.SCENE.DEE_FIRST_ENCOUNTER.1563.001`

The external historical Source Claim and the fictional Story Claim are deliberately separate.

## Date precision

The claim remains month-level:

`1563-02-01 <= encounter < 1563-03-01`

No exact fictional day is inferred from Dee's historical letter date.

For derived personal-recognition knowledge:

- `acquisition_earliest = 1563-02-01`
- `acquisition_certain_by = 1563-03-01`

## Explicit exclusions

This encounter does not establish that Claes already knows:

- the *Monas Hieroglyphica* method;
- the later recovery architecture;
- the vitriol/hidden-writing activation method;
- the Las Casas operation.

Those require separate Story Claims and acquisition events.

## McKee/NOS connection

The concrete scene is stored as `NI.SCENE.DEE_FIRST_ENCOUNTER.1563.001`. It identifies `KO.SCENE`, `KO.CONFLICT` and `KO.VALUE` as future analysis targets while keeping the universal theory outside `claes-canon`.

## Lemma status

The generic range-aware `knowledge_claim` can already evaluate possible/certain acquisition and now uses independent evidence/canon statuses. A future `encounters.lemma` should consume the deterministic implications of this Story Claim rather than treating the historical Source Claim as story truth.

## Publication gate

The structured claim may be merged as canon metadata because it reflects the existing master storybible. Publishing an encounter-specific executable Lemma rule to LemmaBase remains a separate reviewed step.