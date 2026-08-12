# Canon Authoring Policy

## Core rule

Evidence, story truth, narrative placement and executable constraints are maintained as separate layers.

## Workflow

1. Read the current storybible authority and relevant sources.
2. Record external assertions as `SC.*` Source Claims.
3. Record novel truth or candidate truth as `STC.*` Story Claims.
4. Use separate `evidence_status` and `canon_status` fields.
5. Record significant human choices as `DEC.*` decisions.
6. Link claims to `ENT.*` entities and relevant Narrative Instances.
7. Preserve the precision of dates and uncertainty ranges.
8. Convert only deterministic accepted Story Claims into Lemma constraints.
9. Run continuity and Lemma validation.
10. Review changes before merge and LemmaBase publication.

## Status vocabularies

Evidence: `VERIFIED`, `SUPPORTED`, `PLAUSIBLE`, `DISPUTED`, `UNKNOWN`.

Canon: `PROPOSED`, `CANON`, `OPEN`, `DEPRECATED`, `REJECTED`.

These are independent dimensions. A historical fact can be verified without being used in the novel; a fictional event can be plausible and canon.

## Precision rule

A month, season, year or interval remains a month, season, year or interval until an explicit story decision establishes greater precision.

## Narrative theory boundary

Universal `KO.*` narrative theory remains in the external Narrative Knowledge Base. This repository stores Claes-specific Narrative Instances and may reference Knowledge Objects as analysis targets.

## Review questions

A change should make clear what evidence changed, what story truth changed, what decision supports it, where it is dramatized, which continuity domains are affected, and whether a Lemma rule changes.