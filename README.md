# Claes Canon / Storybible

Lemma-focused, McKee/NOS-inspired operating storybible for the Claes project.

## Purpose

This repository separates four responsibilities that must never be conflated:

1. **Evidence** — what historical/research sources support (`SC.*`).
2. **Story truth** — what is true in the novel (`STC.*` + `DEC.*`).
3. **Narrative meaning** — where and how that truth is dramatized (`NI.*`, `ARC.*`, `MOTIF.*`, `REL.*`).
4. **Deterministic consistency** — only the subset that benefits from executable rules (`lemma/*.lemma`).

Universal McKee/Truby/etc. narrative theory stays outside this repository as the Narrative Knowledge Base (`KO.*`). Concrete Claes Narrative Instances may point to those Knowledge Objects for diagnostics.

## Revision 11 conversion

The complete Revision 11 prose master has been parsed as a source edition of 3803 lines and 296 headings, SHA-256:

`e38430f0165e7c0779a8ae6bba6a208773c677682f55295a940e91fdb2ed9edd`

All 31 top-level sections are accounted for in `mapping/CONVERSION_LEDGER.yaml`. The first full semantic conversion pass has normalized the continuity-critical core into claims, entities, objects, Narrative Instances, arcs, motifs, open decisions and craft guardrails. The raw long-form prose is still retained as the lossless source authority for material not yet atomized.

See `mapping/CONVERSION_REPORT.yaml` for explicit completeness status. No unnormalized paragraph is treated as deleted merely because it has not yet become an atomic record.

## Repository layout

- `storybible/` — operating master authority and navigation.
- `mapping/` — source-to-structured conversion ledger and report.
- `claims/` — Source Claims, Story Claims and decisions.
- `entities/` — stable persons and locations.
- `objects/` — continuity-sensitive objects and carriers.
- `narrative/` — Narrative Instances, arcs, motifs, relationships, knowledge states and object biographies.
- `canon/` — unresolved author decisions.
- `sources/` — provenance registry.
- `proposals/` — reviewable AI/human change proposals.
- `lemma/` — executable deterministic constraints only.
- `scripts/validate_canon.py` — repository continuity compiler.
- `.github/` — Lemma and continuity CI.

## Truth flow

`historical source -> SC.* -> STC.* -> DEC./review -> NI.* / storybible -> Lemma when deterministic`

The reverse diagnostic flow is also supported:

`KO.* narrative theory + NI.* Claes instance -> narrative analysis / diagnostic`

## Status axes

Evidence status:

`VERIFIED / SUPPORTED / PLAUSIBLE / DISPUTED / UNKNOWN`

Canon status:

`PROPOSED / CANON / OPEN / DEPRECATED / REJECTED`

These axes are independent. A fictional event may be historically plausible yet canonically fixed; a verified historical fact does not automatically become part of the novel.

## Non-negotiable authoring rule

AI may read, extract, compare, propose, structure and validate. AI does **not** silently promote a hypothesis to canon and does not publish to LemmaBase without explicit human approval.

See `AUTHORING_POLICY.md`, `SCHEMA.md`, `ARCHITECTURE.md`, `AGENTS.md` and `storybible/MASTER.md`.
