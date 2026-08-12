# AI Canon Authoring Instructions

This repository is the controlled, project-specific truth and continuity layer for Claes.

## Primary objective

Transform historical research and story decisions into traceable Source Claims, Story Claims, Narrative Instances and—only where appropriate—deterministic Lemma constraints.

## Mandatory behaviour

1. Read the current master authority, relevant source records and existing claims before proposing changes.
2. Create/update `SC.*` Source Claims for what evidence supports.
3. Create/update `STC.*` Story Claims for what is true or proposed inside the novel.
4. Keep `evidence_status` (`VERIFIED/SUPPORTED/PLAUSIBLE/DISPUTED/UNKNOWN`) separate from `canon_status` (`PROPOSED/CANON/OPEN/DEPRECATED/REJECTED`).
5. Preserve stable IDs; do not mint a new ID merely because a label or wording changes.
6. Link claims to stable `ENT.*` entities and relevant `NI.*`, `ARC.*` or `MOTIF.*` records.
7. Never invent missing dates, places, relationships, quotations, bibliographic locators or source metadata.
8. Preserve time precision. Never convert a month/year/interval into a fabricated exact date.
9. Prefer a proposal and `DEC.*` decision record whenever a narrative choice or uncertainty requires human authority.
10. Promote only accepted deterministic Story Claims into Lemma.
11. Run repository continuity validation and Lemma validation when affected.
12. Explain downstream effects of every canon-changing proposal.
13. Never publish to LemmaBase without explicit human approval.

## McKee/NOS boundary

`KO.*` Knowledge Objects are external universal theory. Do not copy McKee/Truby/Coyne theory into this repository. Concrete Claes scenes, beats, arcs and motifs are Narrative Instances and may name external `KO.*` objects only as analysis targets.

## Default reasoning questions

Before changing the repository, determine:

- What does the historical/research evidence actually say?
- Which atomic Source Claim expresses that evidence?
- Which separate Story Claim is being asserted or changed?
- Is this a factual adoption, a fictional decision, an open question or a deprecated path?
- Which entities and Narrative Instances are affected?
- Does the change alter chronology, location, possession, encounter feasibility, knowledge acquisition or clue dependency?
- Is a Lemma constraint genuinely required?
- What must remain uncertain?

## Preferred authoring output

1. Source Claims added/changed.
2. Story Claims added/changed.
3. Decisions required or recorded.
4. Narrative Instances affected.
5. Lemma rules affected, if any.
6. Validation results.
7. Remaining uncertainties.
8. Downstream continuity impact.
