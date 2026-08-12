# Storybible Index

Operational navigation for Revision 11 after structured conversion.

## Authority and conversion

- `MASTER.md` — operating authority and precedence rules.
- `../mapping/CONVERSION_LEDGER.yaml` — all 31 top-level source sections with line ranges and hashes.
- `../mapping/CONVERSION_REPORT.yaml` — conversion completeness and remaining passes.

## Canon truth

- `../claims/SOURCE_CLAIMS.yaml` — historical/research claims.
- `../claims/STORY_CLAIMS.yaml` — atomic novel truths.
- `../claims/DECISIONS.yaml` — explicit canon decisions.
- `../canon/OPEN_DECISIONS.yaml` — unresolved decisions.

## World state

- `../entities/ENTITIES.yaml` — people and places.
- `../objects/OBJECTS.yaml` — canonical object identities.
- `../narrative/object_biographies.yaml` — object state changes through story time.
- `../narrative/knowledge_states.yaml` — who knows what when.

## Narrative realization

- `../narrative/instances.yaml` — chapters, scenes, sequences and events.
- `../narrative/scenes.yaml` — richer scene analyses linked by `instance_id`.
- `../narrative/arcs.yaml` — character, relationship and macro arcs.
- `../narrative/relationships.yaml` — relationship states.
- `../narrative/motifs.yaml` — recurring motifs.
- `../narrative/CRAFT_GUARDRAILS.yaml` — writing and continuity guardrails.

## Deterministic engine

- `../lemma/core.lemma`
- `../lemma/knowledge.lemma`
- `../lemma/events.lemma`
- `../lemma/encounters.lemma`
- `../lemma/objects.lemma`
- `../lemma/clues.lemma`
- `../lemma/consistency.lemma`

## Diagnostics interface

External Narrative Knowledge Objects (`KO.*`) are not copied into Claes canon. `NI.*` records may point to them as analysis targets, preserving the NOS distinction between universal narrative knowledge and project-specific Narrative Instances.
