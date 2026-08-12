# Claes Storybible Architecture

## Principle

This repository is a project-specific Narrative Operating System for *Claes*. It separates four concerns that must never be collapsed:

1. **Historical evidence** — what external sources support.
2. **Story truth** — what is true inside the novel.
3. **Narrative meaning** — how scenes, arcs, motifs and relationships carry the story.
4. **Deterministic constraints** — what Lemma can evaluate exactly.

The design is inspired by the NOS McKee Knowledge Object model: stable IDs, explicit provenance, explicit relations, normalization status, diagnostics and retrieval metadata. McKee/Truby/Coyne knowledge itself remains outside this repository; this repository stores the concrete Claes instances to which such knowledge can later be applied.

## Data flow

```text
HISTORICAL SOURCES
        |
        v
SOURCE CLAIMS (SC.*)
        |
        v
STORY CLAIMS (STC.*) <---- CANON DECISIONS (DEC.*)
        |                         |
        +-----------+-------------+
                    |
          +---------+---------+
          |                   |
          v                   v
 MASTER STORYBIBLE      NARRATIVE INSTANCES
                         chapter/scene/arc/motif
          |                   |
          +---------+---------+
                    |
                    v
          DETERMINISTIC CLAIMS
                    |
                    v
                  LEMMA
                    |
                    v
            CONSISTENCY ENGINE
```

## Namespaces

- `SC.*` — source claims.
- `STC.*` — story claims.
- `DEC.*` — explicit canon/architecture decisions.
- `ENT.*` — stable entities: people, places, objects, organizations, texts.
- `NI.*` — narrative instances: books, acts, sequences, chapters, scenes, beats.
- `ARC.*` — character, relationship and thematic arcs.
- `MOTIF.*` — recurring motifs.
- `REL.*` — explicit cross-object relations when needed.
- `SRC-*` — source records.
- `PROP-*` — proposed changes awaiting review.

IDs are permanent. Renaming a label never changes the ID.

## Two independent status axes

### Evidence status

- `VERIFIED` — directly verified against adequate evidence.
- `SUPPORTED` — strongly supported but not fully direct/complete.
- `PLAUSIBLE` — historically compatible but not evidenced as the specific event/claim.
- `DISPUTED` — credible evidence conflicts.
- `UNKNOWN` — not established.

### Canon status

- `PROPOSED` — candidate story truth awaiting approval.
- `CANON` — active story truth.
- `OPEN` — deliberately unresolved story question.
- `DEPRECATED` — superseded; retained for audit/history.
- `REJECTED` — explicitly not part of active canon.

Evidence and canon are orthogonal. A fictional event can be `PLAUSIBLE + CANON`; an external historical fact can be `VERIFIED + CANON` when the novel adopts it.

## Narrative Knowledge Base boundary

Universal narrative theory is not duplicated here. A McKee object such as `KO.SCENE` belongs in the Narrative Knowledge Base. A concrete Claes scene belongs here as an `NI.SCENE.*` record. The reasoning layer may later combine both:

`KO.SCENE + NI.SCENE.* -> diagnostic`.

## Lemma boundary

Lemma is the executable constraint layer, not the story database. Only story claims whose truth can be evaluated deterministically should become Lemma inputs/rules: chronology, presence, possession, knowledge acquisition, encounter feasibility, clue dependencies and similar constraints.

Long-form interpretation stays in `storybible/`; atomic truth stays in `claims/`; narrative placement stays in `narrative/`.