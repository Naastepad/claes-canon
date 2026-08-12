# Lemma modules

Only validated executable constraints belong in this directory. Lemma is the deterministic layer of the storybible, not the storage layer for prose, sources or narrative analysis.

## Current

- `core.lemma` — neutral temporal boundary primitive.
- `knowledge.lemma` — range-aware knowledge acquisition with independent `evidence_status` and `canon_status` axes.

## Planned

Create only when a real story claim requires deterministic evaluation and current Lemma syntax has been validated:

- `people.lemma`
- `events.lemma`
- `objects.lemma`
- `encounters.lemma`
- `clues.lemma`
- `consistency.lemma`

## Promotion rule

The preferred path is:

`SRC-* -> SC.* -> STC.* -> review/decision -> Lemma constraint`

A Lemma rule must point conceptually back to an accepted Story Claim; historical evidence never becomes executable story truth merely because it is verified.

Do not duplicate long biographies, source quotations, arc descriptions or scene analysis in Lemma.