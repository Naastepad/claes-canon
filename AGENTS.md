# AI Canon Authoring Instructions

This repository is the controlled operating storybible and canon layer for Claes.

## Primary objective

Preserve narrative meaning, historical provenance and deterministic continuity without conflating evidence, interpretation, story choice or narrative theory.

## Read order

Before proposing a change:

1. `storybible/MASTER.md` and `mapping/CONVERSION_LEDGER.yaml` for authority/coverage.
2. relevant `STC.*`, `ENT.*`, `OBJ.*`, `NI.*`, `ARC.*`, `MOTIF.*` records.
3. relevant `SC.*` and source records.
4. relevant Lemma constraints only when the question is deterministic.
5. external `KO.*` knowledge objects only for narrative diagnosis, never as Claes canon.

## Mandatory behaviour

1. Preserve provenance and source precision.
2. Keep evidence status and canon status independent.
3. Never invent missing dates, locations, relationships, quotations or bibliographic metadata.
4. Never turn month/year precision into a fabricated exact day.
5. Prefer a proposal over a direct canon change when genuine uncertainty exists.
6. Treat the conversion ledger as a loss-prevention map: unatomized prose is still active source material.
7. Keep Lemma focused on executable constraints, not prose storage or literary interpretation.
8. Use stable IDs and references; one canonical identity record owns each `ENT.*`/`OBJ.*`/`NI.*` ID.
9. Add/update validation when a schema or constraint changes.
10. Explain downstream effects of every canon-changing proposal.
11. Never publish to LemmaBase without explicit human approval.

## State vocabularies

Evidence:
`VERIFIED / SUPPORTED / PLAUSIBLE / DISPUTED / UNKNOWN`

Canon:
`PROPOSED / CANON / OPEN / DEPRECATED / REJECTED`

## Reasoning boundary

Ask separately:

- What does the historical evidence support? (`SC.*`)
- What has the author decided is true in the novel? (`STC.*` / `DEC.*`)
- Where is it dramatized? (`NI.*` / arcs / motifs / relationships)
- Is the combination logically possible? (Lemma)
- Does the scene work narratively? (external `KO.*` diagnostics)

Do not let an answer to one question silently answer another.

## Preferred authoring pass

1. New evidence or story change.
2. Source Claims affected.
3. Story Claims affected.
4. Entities/objects/knowledge states affected.
5. Narrative Instances/arcs/motifs affected.
6. Lemma constraints affected, if any.
7. Tests and expected outcomes.
8. Remaining open decisions.
9. Human review before promotion/publication.
