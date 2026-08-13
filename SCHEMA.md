# Claes Canon Schema v2

## Design principle

The repository separates **evidence**, **story truth**, **narrative meaning**, and **deterministic evaluation**. Lemma is the executable constraint engine, not a general-purpose knowledge database.

The McKee/NOS influence is structural: stable IDs, explicit claims, explicit relations, provenance, normalization/uncertainty, retrieval metadata and concrete Narrative Instances. Universal Knowledge Objects remain outside this project repository.

## Core record families

### Source Claim — `SC.*`
An atomic assertion extracted from historical/research material. It answers: **what does the evidence support?**

Required concepts: statement, subject/predicate/object where useful, time precision, evidence status, source IDs, qualifications/contradictions.

### Story Claim — `STC.*`
An atomic proposition that is true, proposed, open, deprecated or rejected inside Claes. It answers: **what is true in the novel?**

A Story Claim may be supported by Source Claims and/or an explicit canon decision. Story Claims are the only claims eligible to become project-specific Lemma constraints.

### Canon Decision — `DEC.*`
A stable audit record for a human narrative or architecture choice. It explains why a claim was promoted, rejected, deprecated or modeled in a particular way.

### Entity — `ENT.*`
Stable identities for people, locations, objects, texts, organizations and other persistent referents.

### Narrative Instance — `NI.*`
Concrete book/act/sequence/chapter/scene/beat records. These are the bridge to the external Narrative Knowledge Base. A concrete scene may identify `KO.SCENE` as an analysis target without copying McKee theory into the Claes canon.

### Arc — `ARC.*`
Character, relationship or thematic change over multiple Narrative Instances.

### Motif — `MOTIF.*`
A recurring sensory, symbolic, material or thematic pattern.

### Source record — `SRC-*`
Full provenance record. Source Claims refer to source IDs rather than duplicating bibliography.

## Independent status axes

### Evidence status

- `VERIFIED` — directly verified against adequate evidence.
- `SUPPORTED` — strongly supported but not fully direct/complete.
- `PLAUSIBLE` — compatible with evidence, but the specific event/claim is not established.
- `DISPUTED` — credible evidence conflicts.
- `UNKNOWN` — not established.

### Canon status

- `PROPOSED` — candidate story truth awaiting approval.
- `CANON` — active story truth.
- `OPEN` — deliberately unresolved.
- `DEPRECATED` — superseded but retained for audit.
- `REJECTED` — explicitly not active canon.

These axes are orthogonal. `VERIFIED` does not automatically imply `CANON`; a deliberate fictional event may be `PLAUSIBLE + CANON`.

## Lemma boundary

Lemma receives only deterministic implications of accepted Story Claims. Initial rule families remain:

- `can_know`
- `can_meet`
- `can_possess`
- `can_be_at`
- `can_use`
- `can_decode`
- `canon_consistent`

A typical flow is:

`SRC-* -> SC.* -> STC.* -> DEC/review -> Lemma`

## Temporal distinction

Never conflate:

1. **story time** — when something happens in Claes;
2. **rule effective time** — which temporal version of a Lemma spec applies.

## Date precision and uncertainty

Never invent an exact story date when the source or storybible provides only a month, season, year or bounded interval.

Use half-open windows where practical:

`earliest <= time < latest_exclusive`

For a month-level claim such as February 1563:

- `earliest = 1563-02-01`
- `latest_exclusive = 1563-03-01`
- `precision = month`

For knowledge acquisition, Lemma uses:

- `acquisition_earliest` — earliest possible acquisition;
- `acquisition_certain_by` — first date by which acquisition is certain.

Thus the interval between those values preserves uncertainty without manufacturing a day.

## Provenance and retrieval

Structured records may include compact retrieval tags and analysis targets. Full quotations, long biographies, research notes and interpretive prose remain in the master storybible or source registry.

## Validation invariants

The repository continuity compiler should reject, at minimum:

- duplicate IDs;
- unresolved entity/claim/decision references;
- missing `SRC-*` records;
- invalid status vocabulary;
- impossible or reversed date windows;
- precision that contradicts encoded dates;
- deprecated/rejected deterministic claims being treated as active;
- future dangling Narrative Instance references.

Lemmas are validated separately by the pinned Lemma CLI.