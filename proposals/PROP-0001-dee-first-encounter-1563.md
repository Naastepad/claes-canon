# PROP-0001 — First encounter with John Dee, February 1563

## Status
PROPOSED — not hard canon in Lemma yet

## Purpose
Introduce the first real, source-linked canon proposal and test the authoring workflow without silently converting month-level story chronology into a fabricated exact date.

## Proposed canon claim
Claes has a first brief encounter with John Dee in **February 1563**, in or around Willem Silvius' Gulden Engel in Antwerp. This encounter establishes personal recognition and makes the later 1564 master–pupil relationship continuous rather than abrupt.

## Epistemic classification
`CANON`

This is a fictional story event already present in Storybible Revision 11. Its historical plausibility is supported separately; the encounter itself is not a historical fact.

## Provenance
- `SRC-CANON-R11-DEE-001` — internal storybible canon source.
- `SRC-HIST-1563-DEE-SILVIUS-001` — historical anchor showing Dee in Silvius' Antwerp environment in February 1563; does not prove the fictional encounter.

## Date
Story date precision: **February 1563**.

Represent as a bounded authoring window:

`1563-02-01 ... 1563-03-01`

Do **not** assign `1563-02-16` as the fictional meeting date merely because that is the historical Dee letter anchor.

## Knowledge relation
Proposed knowledge state:

`Claes -> knows_personally -> John_Dee`

Acquisition trigger:

`first_encounter_claes_dee_1563`

Availability:
- before the encounter: not established;
- after the encounter: Claes can recognize Dee as someone he has personally met;
- this relation does not imply possession of later specialist knowledge.

Explicit exclusions at this point:
- no claim that Claes knows the *Monas Hieroglyphica* method;
- no claim that Claes knows the recovery architecture;
- no claim that Claes knows the vitriol/hidden-writing activation method;
- no claim that Claes knows the Las Casas operation.

Those require later, separately sourced acquisition events.

## Interaction with `lemma/knowledge.lemma`
The current `knowledge_claim` spec accepts one exact `acquisition_date`. This proposal deliberately does **not** instantiate it yet, because the storybible provides only month precision. Using `1563-02-01` or `1563-02-16` as if either were the actual meeting date would introduce false precision.

### Schema consequence
Before this proposal becomes executable hard canon, the knowledge model should support either:
1. an acquisition date range / uncertainty window; or
2. a separate event model whose exact date can remain unresolved while downstream rules distinguish `certainly_known_by` from `possibly_known_by`.

This is the first schema issue discovered by applying the model to real storybible material and should be solved before merge-to-canon.

## Expected future tests
Once range-aware acquisition is implemented:

- query before 1563-02-01 -> `can_know_personally_dee = false`
- query within February 1563 -> result should preserve uncertainty unless the exact encounter date is fixed
- query on/after 1563-03-01 -> `can_know_personally_dee = true`

A separate rule may expose `can_possibly_know_personally_dee = true` during the February window.

## Human decision required
Approve one of the following:

A. Preserve month-level uncertainty permanently and make Lemma range-aware. **Recommended.**

B. Canonize an exact fictional meeting date in February 1563. If chosen, the date must be an explicit author decision, not inferred from the historical letter date.

## Downstream effects if approved
- `events.lemma`: first Dee encounter event.
- `knowledge.lemma`: personal-recognition acquisition boundary.
- later Dee knowledge must depend on separate 1564 acquisition events.
- encounter/location checks can later verify Antwerp + Silvius environment compatibility.

## Publication gate
Do not publish this proposal to LemmaBase as executable canon until the date-precision issue above is resolved and explicitly approved.
