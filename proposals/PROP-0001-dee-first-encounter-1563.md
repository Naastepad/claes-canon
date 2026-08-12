# PROP-0001 — First encounter with John Dee, February 1563

## Status
PROPOSED — schema issue resolved; not hard canon in Lemma yet

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

Range-aware acquisition boundaries:

- `acquisition_earliest = 1563-02-01`
- `acquisition_certain_by = 1563-03-01`

Availability:
- before 1563-02-01: not established;
- during February 1563: possibly acquired, exact day unresolved;
- on/after 1563-03-01: certainly acquired according to this canon claim;
- this relation does not imply possession of later specialist knowledge.

Explicit exclusions at this point:
- no claim that Claes knows the *Monas Hieroglyphica* method;
- no claim that Claes knows the recovery architecture;
- no claim that Claes knows the vitriol/hidden-writing activation method;
- no claim that Claes knows the Las Casas operation.

Those require later, separately sourced acquisition events.

## Interaction with `lemma/knowledge.lemma`
The range-awareness schema decision has been implemented. `knowledge_claim` now distinguishes:

- `possibly_acquired_by_query_date`
- `certainly_acquired_by_query_date`
- `in_acquisition_uncertainty_window`
- `can_possibly_know`
- `can_know`

This prevents month-level story chronology from being converted into a fabricated exact day.

## Expected tests

- query before 1563-02-01 -> `can_know = false`, `can_possibly_know = false`
- query during February 1563 -> `can_know = false`, `can_possibly_know = true`, uncertainty window = true
- query on/after 1563-03-01 -> `can_know = true`, `can_possibly_know = true`

## Human decision still required
The schema decision (preserve month-level uncertainty) is approved and implemented.

What remains for review is the canon proposal itself: whether the February 1563 first encounter should be promoted from storybible proposal material into executable Lemma canon.

## Downstream effects if canon claim is approved
- `events.lemma`: first Dee encounter event.
- `knowledge.lemma`: instantiate personal-recognition acquisition boundaries.
- later Dee knowledge must depend on separate 1564 acquisition events.
- encounter/location checks can later verify Antwerp + Silvius environment compatibility.

## Publication gate
Do not publish this specific encounter as executable LemmaBase canon until the canon claim itself is explicitly approved. The range-aware schema may be merged independently.
