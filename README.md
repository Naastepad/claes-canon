# Claes Canon / Storybible

Lemma-focused, McKee/NOS-inspired operating storybible for the Claes project.

## AI / agent start here

For ChatGPT, Claude, Gemini, Copilot and other AI systems:

1. **`AI_ONBOARDING.md`** — canonical model-agnostic instructions for reading and interpreting this Storybible.
2. **`storybible/LEMMA_MCKEE_MASTER.md`** — human-readable operating Storybible.
3. **`WRITING_PROTOCOL.md`** — mandatory protocol for drafting, rewriting or critiquing novel prose.
4. **`AUTHORING_POLICY.md` / `AGENTS.md`** — required for changes to canon, structured records or Lemma.
5. **`prompts/SESSION_BOOTSTRAP.md`** — copy-paste prompt for AI sessions that do not automatically discover repository instructions.

Model-specific entrypoints (`CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`) deliberately defer to `AI_ONBOARDING.md` to prevent instruction drift.

## Purpose

This repository separates four responsibilities that must never be conflated:

1. **Evidence** — what historical/research sources support (`SC.*`).
2. **Story truth** — what is true in the novel (`STC.*` + `DEC.*`).
3. **Narrative meaning** — where and how that truth is dramatized (`NI.*`, `ARC.*`, `MOTIF.*`, `REL.*`, `THEME.*`, `VALUE.*`).
4. **Deterministic consistency** — only the subset that benefits from executable rules (`lemma/*.lemma`).

Universal McKee/Truby/etc. narrative theory stays outside this repository as the Narrative Knowledge Base (`KO.*`). Concrete Claes Narrative Instances may point to those Knowledge Objects for diagnostics.

## Revision 11 transmutation

The complete Revision 11 prose master has been parsed as a source edition of 3803 lines and 296 headings, SHA-256:

`e38430f0165e7c0779a8ae6bba6a208773c677682f55295a940e91fdb2ed9edd`

All 31 top-level sections are accounted for in `mapping/CONVERSION_LEDGER.yaml`.

The human-readable **transformed operating edition** is:

`storybible/LEMMA_MCKEE_MASTER.md`

It does not merely summarize the old storybible. It reorganizes its continuity-critical meaning around character desire/need/lie/revelation, value change, macrostructure, relationships, object biographies, Narrative Instances, motifs, world modules, knowledge boundaries, code dependencies and explicit open decisions.

The structured form underneath it provides the machine-readable control layer. Material not yet atomized remains active in the exact Revision 11 source edition and is never treated as absent or superseded simply because no separate atomic record exists yet.

See `mapping/CONVERSION_REPORT.yaml` for explicit completeness status and `storybible/TRANSFORMATION_LEDGER.yaml` for the thematic source-to-target map.

## Repository layout

- `storybible/` — operating transformed master, source-authority manifest and transformation ledger.
- `mapping/` — exact source-to-structured conversion ledger and completeness report.
- `claims/` — Source Claims, Story Claims and decisions.
- `entities/` — stable persons and locations.
- `objects/` — continuity-sensitive objects, their biographies, state changes and carrier constraints.
- `narrative/` — Narrative Instances, arcs, motifs, relationships, themes/value axes, actor knowledge states, world modules and code architecture.
- `canon/` — unresolved author decisions (`OPEN.*`).
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

## Continuity compiler

The repository validator treats stable Storybible IDs — including `THEME.*`, `VALUE.*`, `WORLD.*` and `CODE.*` — as first-class records and checks referential integrity, status vocabularies, temporal windows and the loss-preserving source conversion ledger.

Lemma separately validates deterministic constraints. The current layer covers temporal boundaries, knowledge, events, encounters, possession, clue prerequisites, the staged recovery/decode route and final consistency gates.

## Non-negotiable authoring rule

AI may read, extract, compare, propose, structure and validate. AI does **not** silently promote a hypothesis to canon and does not publish to LemmaBase without explicit human approval.

See `AI_ONBOARDING.md`, `WRITING_PROTOCOL.md`, `AUTHORING_POLICY.md`, `SCHEMA.md`, `ARCHITECTURE.md`, `AGENTS.md` and `storybible/LEMMA_MCKEE_MASTER.md`.
