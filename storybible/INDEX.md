# Storybible Index

Operational navigation for the Lemma-focused, McKee/NOS-inspired Claes Storybible.

## Start here

- `../README.md` — public/AI gateway.
- `../AI_ONBOARDING.md` — canonical cross-model interpretation rules.
- `../REPOSITORY_INTEGRITY.md` — mandatory for every writer/automation.
- `LEMMA_MCKEE_MASTER_2026-08-13.md` — dated operating synthesis; see `../review/SYNC_STATUS.md` for later decision layers that currently outrank stale passages.
- `../review/SYNC_STATUS.md` — synchronization state.

## Authority and conversion

- `MASTER.md` — authority manifest and source/conversion context.
- `../canon/DECISIONS_2026-08-13.md` — current explicit author decisions.
- `../canon/DECISIONS_2026-08-15.md` — execution/Reformation decisions plus `DEC.MEMORIAAL.DIRECT_TEXT_NO_CIPHER.2026-08-15`, which fixes the readable pre-Boom hidden Brevísima print, Dee graphite handoff and retirement of the cipher workaround.
- `../canon/DECISIONS.yaml` — machine-readable current decisions.
- `../mapping/CONVERSION_LEDGER.yaml` — all 31 Revision 11 top-level source sections with line ranges/hashes.
- `../mapping/CONVERSION_REPORT.yaml` — conversion completeness and remaining normalization.

## Canon truth

- `../claims/SOURCE_CLAIMS.yaml` — historical/research claims.
- `../claims/SOURCE_CLAIMS_EXECUTIONS_REFORMATION.yaml` — Casteels, martelaarsbronnen and execution-culture source claims.
- `../claims/SOURCE_CLAIMS_MEMORIAAL_PRINT_1564.yaml` — Plantin printing-context, Antwerp medicinal metrology and the explicitly reconstructed tannin/gum hidden-print claim.
- `../claims/STORY_CLAIMS.yaml` — atomic novel truths, including the readable hidden Brevísima carrier, print process and graphite rule; former cipher claims are retained only as deprecated audit records.
- `../claims/STORY_CLAIMS_EXECUTIONS_REFORMATION.yaml` — execution/Reformation story claims for Claes and Cornelis.
- `../claims/DECISIONS.yaml` — general architecture/story decisions.
- `../canon/OPEN_DECISIONS.yaml` — unresolved author decisions and audit-preserved resolved records.
- `../review/MIGRATION_REVIEW.yaml` — migrated/derived/new/conflict review state.

## World state

- `../entities/ENTITIES.yaml` — people and places.
- `../objects/OBJECTS.yaml` — continuity-sensitive objects and their state/biography data; `OBJ.MEMORIAAL` carries `OBJ.LASCASAS_PLAINTEXT` in latent readable typographic form and `OBJ.GRAPHITE_STIFT` governs Claes' visible writing layer.
- `../narrative/knowledge_states.yaml` — who knows what when.
- `../narrative/world_modules.yaml` — source-weighted worldbuilding modules.

## Narrative realization

- `../narrative/instances.yaml` — chapters, scenes, sequences and events, including `NI.SCENE.MEMORIAAL_GIFT.1564.001` before Boom and the later direct reveal sequence.
- `../narrative/instances_executions_reformation.yaml` — execution/Reformation narrative instances and scene candidates.
- `../narrative/scenes.yaml` — richer scene analyses.
- `../narrative/arcs.yaml` — base character, relationship and macro arcs.
- `../narrative/sinne_recovery.yaml` — approved *sinne* trauma/recovery/sovereignty arc extension.
- `../narrative/relationships.yaml` — base relationship states, including the Dee formation/handoff asymmetry.
- `../narrative/beloved_recovery.yaml` — beloved/Enkhuizen recovery extension.
- `../narrative/motifs.yaml` — recurring motifs.
- `../narrative/themes.yaml` — controlling idea, needs, spiritual journey and value axes.
- `../narrative/code_architecture.yaml` — legacy filename for the active direct material reveal architecture; old cipher/key recovery is deprecated audit history.
- `../narrative/CRAFT_GUARDRAILS.yaml` — writing and continuity guardrails.

## Storybible dossiers

- `MEMORIAAL_BREVISIMA_PRINT_1564.md` — canonical pre-binding readable Brevísima hidden print, period workshop formulation, Dee handoff, graphite-only rule, knowledge boundary, direct green-vitriol reveal and cipher-retirement guardrails.
- `EXECUTIONS_REFORMATION_CLAES.md` — executions, Reformation, ars moriendi, Casteels, martelaarsbronnen, Cornelis' death model and the execution knowledge reservoir; see sync status for stale cipher-era passages pending regeneration.
- `CORNELIS_EXECUTION_1569.md` — exact authoring-branch resolution of Cornelis' Antwerp execution, charge, manner, witness scene and protective silence, synchronized to the no-cipher memoriaal decision.
- `FAMILY_CLAES_1542_1554.md` — family, house, 1554 fire and post-fire rupture.

## Deterministic engine

- `../lemma/core.lemma`
- `../lemma/knowledge.lemma`
- `../lemma/events.lemma`
- `../lemma/encounters.lemma`
- `../lemma/objects.lemma`
- `../lemma/clues.lemma`
- `../lemma/decode.lemma` — legacy filename; active rule now tests whether the memoriaal and green vitriol are available for direct plaintext reveal.
- `../lemma/consistency.lemma`

## Validation

- `../scripts/validate_canon.py` — repository continuity compiler, including cross-layer author-decision synchronization checks.
- `.github/workflows/canon-repository-validate.yml` — repository CI.
- `.github/workflows/lemma-validate.yml` — Lemma syntax/spec CI.

## Diagnostics interface

External Narrative Knowledge Objects (`KO.*`) are not copied into Claes canon. `NI.*` records may point to them as analysis targets, preserving the distinction between universal narrative knowledge and project-specific Narrative Instances.
