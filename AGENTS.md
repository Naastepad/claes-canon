# AI Canon Authoring Instructions

This repository is the controlled operating Storybible and canon layer for **Claes Nissepat**.

## Canonical AI instructions

Before doing canon-sensitive work, read:

1. `AI_ONBOARDING.md` — model-agnostic instructions for reading and interpreting this repository.
2. `storybible/LEMMA_MCKEE_MASTER.md` — coherent human-readable operating Storybible.
3. `WRITING_PROTOCOL.md` — mandatory if you will draft, rewrite, extend or critique literary prose.
4. `AUTHORING_POLICY.md` — mandatory if you will modify canon/registers/Lemma.

These files apply to ChatGPT, Claude, Gemini, Copilot, local agents and other models. Do not create a competing interpretation of the repository in session memory.

## Primary objective

Preserve narrative meaning, historical provenance and deterministic continuity without conflating evidence, interpretation, story choice or narrative theory.

## Read order for authoring changes

1. `AI_ONBOARDING.md` and `storybible/LEMMA_MCKEE_MASTER.md`.
2. `mapping/CONVERSION_LEDGER.yaml` when Revision 11 source coverage matters.
3. relevant `STC.*`, `ENT.*`, `OBJ.*`, `NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`, `WORLD.*`, `CODE.*` records.
4. relevant `SC.*` and source records.
5. relevant `OPEN.*` decisions.
6. relevant Lemma constraints only when the question is deterministic.
7. external `KO.*` knowledge objects only for narrative diagnosis, never as Claes canon.

## Mandatory behaviour

1. Preserve provenance and source precision.
2. Keep evidence status and canon status independent.
3. Never invent missing dates, locations, relationships, quotations or bibliographic metadata.
4. Never turn month/year precision into a fabricated exact day.
5. Prefer a proposal over a direct canon change when genuine uncertainty exists.
6. Treat the conversion ledger as a loss-prevention map: unatomized prose is still active source material.
7. Keep Lemma focused on executable constraints, not prose storage or literary interpretation.
8. Use stable IDs and references; one canonical identity record owns each stable ID.
9. Add/update validation when a schema or constraint changes.
10. Explain downstream effects of every canon-changing proposal.
11. Never publish to LemmaBase without explicit human approval.
12. If writing prose, obey `WRITING_PROTOCOL.md` and do not silently close `OPEN.*` decisions.

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
5. Narrative Instances/arcs/relationships/motifs/themes/values affected.
6. Lemma constraints affected, if any.
7. Tests and expected outcomes.
8. Remaining open decisions.
9. Human review before promotion/publication.

## Handoff rule

Do not rely on private chain-of-thought or chat memory for continuity. After substantial work, leave repository-visible or user-visible notes stating what was read, what changed, what remains open and what requires approval.
