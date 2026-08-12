# Canon Authoring Policy

## Core rule

No AI-generated assertion becomes canon automatically.

Every proposed change must preserve a visible distinction between evidence, interpretation and narrative choice.

## Required workflow

1. Read the relevant source material and current canon.
2. Extract only claims relevant to canon constraints.
3. Classify every new claim as `FACT`, `CANON`, `HYPOTHESIS`, `DISPUTED` or `UNKNOWN`.
4. Record provenance for every `FACT` and every canon decision that depends on historical evidence.
5. Produce a proposal before modifying accepted Lemma rules.
6. Validate syntax and run relevant consistency checks.
7. Review the diff.
8. Human approval is required before merge and before publication to LemmaBase.

## AI permissions

AI may:

- read sources and storybible material;
- compare new material with accepted canon;
- draft proposals;
- draft or modify Lemma files on an authoring branch;
- identify contradictions and missing dependencies;
- run or suggest validation tests;
- explain the consequences of a proposed change.

AI must not:

- silently promote a hypothesis to fact or canon;
- erase conflicting evidence;
- invent dates, locations, relationships or source references;
- publish to LemmaBase without explicit human approval;
- treat absence of evidence as evidence of absence.

## Canon promotion

`HYPOTHESIS -> CANON` requires an explicit narrative decision.

`DISPUTED -> FACT` requires evidence strong enough to resolve the dispute.

`UNKNOWN` may remain unknown indefinitely.

## Review standard

A proposal is acceptable only when a reviewer can answer:

- What changed?
- Why did it change?
- What source or canon decision supports it?
- Which rules or scenes are affected?
- Is the change reversible and traceable?
