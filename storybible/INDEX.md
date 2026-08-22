# Storybible Index

Operational navigation for the Lemma-focused, McKee/NOS-inspired Claes Storybible.

## Start here

- `../README.md` — public/AI gateway.
- `../AI_ONBOARDING.md` — canonical cross-model interpretation rules.
- `../REPOSITORY_INTEGRITY.md` — mandatory for every writer/automation.
- `LEMMA_MCKEE_MASTER_2026-08-13.md` — previous synchronized operating synthesis; in the adult-spine domain it is now supplemented/overridden by the explicit 23-Aug decisions below.
- `modules/CLAES_RUGGENGRAAT_1564_1602.md` — **active adult narrative spine**; mandatory for story work from Dee's 1564 seed through Enkhuizen/Seton 1602. Important: the lived/geographical spine starts with Claes leaving Antwerp in 1566.
- `../review/SYNC_STATUS.md` — synchronization state.

## Authority and conversion

- `MASTER.md` — authority manifest and source/conversion context.
- `../canon/DECISIONS_2026-08-13.md` — earlier explicit author decisions on birth, *sinne*, paradox, need and spiritual journey.
- `../canon/DECISIONS_2026-08-23.md` — **current explicit adult-spine decisions**: 1564 seed/1566 spine start, Mayken, Las Casas scale, Gouda/northern route, pre-Seton transmutation, Seton, Hoghelande and VOC resonance.
- `../canon/DECISIONS.yaml` — machine-readable current decisions; check sync status for 23-Aug propagation.
- `../mapping/CONVERSION_LEDGER.yaml` — all 31 Revision 11 top-level source sections with line ranges/hashes.
- `../mapping/CONVERSION_REPORT.yaml` — conversion completeness and remaining normalization.

## Canon truth

- `../claims/SOURCE_CLAIMS.yaml` — historical/research claims.
- `../claims/STORY_CLAIMS.yaml` — atomic novel truths, including the approved 23-Aug adult-spine claims.
- `../claims/DECISIONS.yaml` — general architecture/story decisions.
- `../canon/OPEN_DECISIONS.yaml` — unresolved author decisions.
- `../review/MIGRATION_REVIEW.yaml` — migrated/derived/new/conflict review state.

## World state

- `../entities/ENTITIES.yaml` — people and places; Mayken is now the fixed beloved/apothecary daughter and northern-route entities are registered.
- `../objects/OBJECTS.yaml` — continuity-sensitive objects and their state/biography data.
- `../narrative/knowledge_states.yaml` — who knows what when.
- `../narrative/world_modules.yaml` — source-weighted worldbuilding modules.

## Narrative realization

- `../narrative/instances.yaml` — chapters, scenes, sequences and events, including the adult-spine instances.
- `../narrative/scenes.yaml` — richer scene analyses.
- `../narrative/arcs.yaml` — base character, relationship and macro arcs plus `ARC.CLAES.LIFELONG_INQUIRY`.
- `../narrative/sinne_recovery.yaml` — approved *sinne* trauma/recovery/sovereignty arc extension.
- `../narrative/relationships.yaml` — base relationship states.
- `../narrative/beloved_recovery.yaml` — Mayken/Enkhuizen recovery extension.
- `../narrative/motifs.yaml` — recurring motifs.
- `../narrative/themes.yaml` — controlling idea, needs, spiritual journey and value axes.
- `../narrative/code_architecture.yaml` — recovery/code architecture.
- `../narrative/CRAFT_GUARDRAILS.yaml` — writing and continuity guardrails.

## Adult-spine writing package (1564–1602)

For drafting or revising any chapter from the Dee/Antwerp period through Enkhuizen, read at minimum:

1. `../canon/DECISIONS_2026-08-23.md`;
2. `modules/CLAES_RUGGENGRAAT_1564_1602.md`;
3. `../claims/STORY_CLAIMS.yaml` for the relevant `STC.*` records;
4. `../narrative/arcs.yaml` and `../narrative/instances.yaml`;
5. the relevant history/source module for the place/year;
6. `../WRITING_PROTOCOL.md`.

Guardrail: historical events move Claes; the lifelong inquiry changes what he notices. Do not turn the route into a treasure hunt or make Claes present at famous events merely for spectacle.

## Deterministic engine

- `../lemma/core.lemma`
- `../lemma/knowledge.lemma`
- `../lemma/events.lemma`
- `../lemma/encounters.lemma`
- `../lemma/objects.lemma`
- `../lemma/clues.lemma`
- `../lemma/decode.lemma`
- `../lemma/consistency.lemma`

## Validation

- `../scripts/validate_canon.py` — repository continuity compiler, including cross-layer author-decision synchronization checks.
- `.github/workflows/canon-repository-validate.yml` — repository CI.
- `.github/workflows/lemma-validate.yml` — Lemma syntax/spec CI.

## Diagnostics interface

External Narrative Knowledge Objects (`KO.*`) are not copied into Claes canon. `NI.*` records may point to them as analysis targets, preserving the distinction between universal narrative knowledge and project-specific Narrative Instances.