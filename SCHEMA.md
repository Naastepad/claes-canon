# Claes Canon Schema v1

## Design principle

Lemma is used as a deterministic constraint engine, not as a general-purpose knowledge database.

The human-readable storybible remains the place for narrative context, quotations, biography, interpretation and long-form research notes. Lemma contains only information needed to evaluate consistency.

## Core domains

### Person
Relevant fields may include birth/death boundaries, known locations, roles and identifiers.

### Event
A dated or bounded occurrence that can change knowledge, possession, location or relationships.

### Location
A place relevant to presence, travel or encounter constraints.

### Object
A book, manuscript, letter, tool or other item whose existence, availability or possession can affect the story.

### Knowledge
A capability, fact, technique or interpretation that a character may acquire.

### Encounter
A possible or canonical meeting requiring compatible time and place constraints.

### Clue
A discoverable element with prerequisites and downstream dependencies.

### Source
A compact provenance identifier that points to the detailed source registry.

## Epistemic status

- FACT
- CANON
- HYPOTHESIS
- DISPUTED
- UNKNOWN

## Initial rule families

- `can_know`
- `can_meet`
- `can_possess`
- `can_be_at`
- `can_use`
- `can_decode`
- `canon_consistent`

## Provenance

Lemma should use compact source identifiers rather than full citations. Full bibliographic data belongs in `sources/`.

Suggested identifier pattern:

`SRC-<YEAR>-<AUTHOR_OR_COLLECTION>-<NNN>`

Example: `SRC-1566-ORTELIUS-001`.

## Temporal distinction

Two kinds of time must never be conflated:

1. Story time: dates on which events happen to characters.
2. Rule effective time: dates from which a version of a Lemma spec applies.

Story dates should normally be explicit input or canon data. Lemma spec effective dates are reserved for versioning rule regimes.
