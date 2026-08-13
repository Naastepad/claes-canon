# Storybible Index

Operational navigation for the Lemma-focused, McKee/NOS-inspired Claes Storybible.

## Start here

- `../README.md` — public/AI gateway.
- `../AI_ONBOARDING.md` — canonical cross-model interpretation rules.
- `../REPOSITORY_INTEGRITY.md` — mandatory for every writer/automation.
- `LEMMA_MCKEE_MASTER_2026-08-13.md` — current synchronized operating synthesis.
- `../review/SYNC_STATUS.md` — synchronization state.

## Authority and conversion

- `MASTER.md` — authority manifest and source/conversion context.
- `../canon/DECISIONS_2026-08-13.md` — current explicit author decisions.
- `../canon/DECISIONS.yaml` — machine-readable current decisions.
- `../mapping/CONVERSION_LEDGER.yaml` — all 31 Revision 11 top-level source sections with line ranges/hashes.
- `../mapping/CONVERSION_REPORT.yaml` — conversion completeness and remaining normalization.

## Canon truth

- `../claims/SOURCE_CLAIMS.yaml` — historical/research claims.
- `../claims/STORY_CLAIMS.yaml` — atomic novel truths.
- `../claims/DECISIONS.yaml` — general architecture/story decisions.
- `../canon/OPEN_DECISIONS.yaml` — unresolved author decisions.
- `../review/MIGRATION_REVIEW.yaml` — migrated/derived/new/conflict review state.

## World state

- `../entities/ENTITIES.yaml` — people and places.
- `../objects/OBJECTS.yaml` — continuity-sensitive objects and their state/biography data.
- `../narrative/knowledge_states.yaml` — who knows what when.
- `../narrative/world_modules.yaml` — source-weighted worldbuilding modules.

## Narrative realization

- `../narrative/instances.yaml` — chapters, scenes, sequences and events.
- `../narrative/scenes.yaml` — richer scene analyses.
- `../narrative/arcs.yaml` — base character, relationship and macro arcs.
- `../narrative/sinne_recovery.yaml` — approved *sinne* trauma/recovery/sovereignty arc extension.
- `../narrative/relationships.yaml` — base relationship states.
- `../narrative/beloved_recovery.yaml` — beloved/Enkhuizen recovery extension.
- `../narrative/motifs.yaml` — recurring motifs.
- `../narrative/themes.yaml` — controlling idea, needs, spiritual journey and value axes.
- `../narrative/code_architecture.yaml` — recovery/code architecture.
- `../narrative/CRAFT_GUARDRAILS.yaml` — writing and continuity guardrails.

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
