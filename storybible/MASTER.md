# Claes Storybible — MASTER

**Logical master ID:** `SB.CLAES.MASTER`

This file is the repository anchor for the single human-readable narrative truth of the Claes project.

## Current imported authority

The current authoritative working edition is:

`Claes_Storybible_MASTER_COMPLEET_2026-08-10_REVISIE11_MACROSTRUCTUUR_PROJECTIO(1).md`

- size: `353589` bytes
- SHA-256: `e38430f0165e7c0779a8ae6bba6a208773c677682f55295a940e91fdb2ed9edd`
- status: `AUTHORITATIVE_EXTERNAL_MASTER_PENDING_MECHANICAL_GITHUB_IMPORT`

The full source file is retained outside GitHub in the project file library. This manifest exists so that claims, decisions and narrative instances can already refer to one stable master identity without pretending that a partial copy is complete.

## Canon rule

Until the full 353589-byte master is mechanically imported into this repository, **do not replace or paraphrase it as if this manifest were the complete storybible**. For narrative continuity, the external file identified above remains authoritative.

Once imported, this path itself (`storybible/MASTER.md`) becomes the only narrative master and the import status above must change to `IN_REPOSITORY`.

## Architectural role

The master explains meaning and continuity in prose. It does not replace the atomic registries:

- `claims/SOURCE_CLAIMS.yaml` — what evidence says;
- `claims/STORY_CLAIMS.yaml` — what is true in the novel;
- `claims/DECISIONS.yaml` — why canon/architecture choices were made;
- `entities/ENTITIES.yaml` — stable identities;
- `narrative/` — where truth is dramatized;
- `lemma/` — deterministic constraints only.

## Loss-prevention rule

A future master may be called complete only when:

1. every previously active major section is retained or explicitly marked deprecated;
2. every new canon decision is propagated to all affected chronology, entity, knowledge, object and narrative records;
3. resolved open points are removed from active `OPEN` status and retained in the audit trail rather than silently resurrected.