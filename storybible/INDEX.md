# Storybible Index

This index is intentionally structural until the full external master is mechanically imported into GitHub.

## Authority

- `SB.CLAES.MASTER` → `storybible/MASTER.md`
- authoritative external edition recorded there with filename, byte size and SHA-256

## Machine-readable companion layers

- Source Claims → `claims/SOURCE_CLAIMS.yaml`
- Story Claims → `claims/STORY_CLAIMS.yaml`
- Decisions → `claims/DECISIONS.yaml`
- Entities → `entities/ENTITIES.yaml`
- Narrative hierarchy → `narrative/structure.yaml`
- Scenes → `narrative/scenes.yaml`
- Arcs → `narrative/arcs.yaml`
- Motifs → `narrative/motifs.yaml`
- Relationships → `narrative/relationships.yaml`
- Deterministic constraints → `lemma/`

## Generated-index target

When the full master is imported, a future index generator should extract headings and annotate each section with linked `STC.*`, `ENT.*`, `NI.*`, `ARC.*` and `MOTIF.*` identifiers. The generated index must never alter narrative canon.