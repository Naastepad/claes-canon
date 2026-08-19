# Canon Authoring Policy

## Core rule
Evidence, story truth, world/practice state, narrative placement, editorial quality and executable constraints are maintained as separate layers. Explicit human decisions are authoritative and must be synchronized through every dependent representation.

## Required reading before writes
A write-capable AI must read `AI_ONBOARDING.md`, current `canon/`, `REPOSITORY_INTEGRITY.md`, this policy and the relevant registers. It must re-fetch target files immediately before mutation.

Before drafting, revising or critiquing literary prose it must also read:

- `WRITING_PROTOCOL.md`;
- `storybible/STORY_PROJECTION_ROUND_C.md` when plot/scene causality is involved;
- `review/READER_EXPERIENCE_PROTOCOL.md` when assessing prose, pacing or reader response;
- `narrative/editorial_gates.yaml` for the active Round-D quality gates.

## Workflow
1. Read current human decisions, operating Storybible and relevant sources.
2. Record external assertions as `SC.*` Source Claims.
3. Record novel truth or candidate truth as `STC.*` Story Claims.
4. Keep `evidence_status` and `canon_status` independent.
5. Record significant human choices as `DEC.*` or repository-visible decision records.
6. Link claims to `ENT.*` entities and relevant Narrative Instances.
7. Preserve date precision and uncertainty ranges.
8. Synchronize approved decisions through dependent entities, objects, knowledge states, world/practice modules, Narrative Instances, arcs, relationships, motifs, themes/values and the operating master.
9. Project world knowledge into causal story architecture before inventing chapter structure.
10. Apply the editorial gates during scene construction and revision: scene necessity, prose quality, pacing, reader experience and reader feedback.
11. Convert only deterministic accepted Story Claims into Lemma constraints.
12. Run continuity and active-projection validation.
13. Review changes before merge and LemmaBase publication.

## Multi-agent rule
Never assume this repository is unchanged because the current chat wrote it earlier. Another session or model may have written meanwhile. Re-fetch branch state and target files before every write pass. If content changed, reconcile instead of overwriting. Follow `REPOSITORY_INTEGRITY.md`.

## Branch rule
Canon development belongs on an authoring branch/PR unless the human explicitly authorizes direct-main synchronization or the active conversation clearly continues an already authorized direct-main synchronization round. Do not force-update, delete history, publish to LemmaBase, merge a PR or promote OPEN/PROPOSED material without explicit human authority.

## Status vocabularies
Evidence: `VERIFIED`, `SUPPORTED`, `PLAUSIBLE`, `DISPUTED`, `UNKNOWN`.
Canon: `PROPOSED`, `CANON`, `OPEN`, `DEPRECATED`, `REJECTED`.
These are independent dimensions. A historical fact can be verified without being used in the novel; a fictional event can be plausible and canon.

Editorial verdicts are a separate axis: `RETAIN`, `REVISE`, `MERGE`, `CUT`. They judge prose/scene function and never alter canon by themselves.

Reader-evidence classifications are also separate: `ISOLATED`, `REPEATED`, `CONVERGENT`, `RESOLVED`, `INTENTIONAL_VARIANCE`.

## Precision rule
A month, season, year or interval remains that precision until an explicit story decision establishes greater precision.

## Historical evidence gaps are authorial space

Under `DEC.HISTORICAL_GAPS.FICTIONAL_CHARACTERIZATION.2026-08-19`, absence of historical evidence is **not** by itself a prohibition on fictional specification.

For a recurring person, location, object or practice, the author may deliberately fill a documentary gap when the choice has real continuity, character, causal, spatial or reader-experience value, provided that:

1. no known evidence is contradicted;
2. the fictional choice is historically plausible for the time/place/status involved;
3. the fiction status is recorded explicitly as story/character/world canon rather than Source Claim;
4. the historical evidence status remains unchanged (`UNKNOWN` remains `UNKNOWN`);
5. the chosen detail is synchronized anywhere continuity depends on it;
6. later contradictory evidence triggers review rather than silent rewriting.

This rule is especially important for recurring historical people whose archival record preserves office or work but not ordinary human particulars. Voice, habits, room use, private reactions or appearance may be fixed as **FICTION CANON** without being misrepresented as recovered biography.

Do not fill every gap automatically. A detail earns canon when future scenes benefit from stability. The archive sets the boundary; the novel may fill the living space inside it.

For the current core-cast implementation, load `storybible/CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md` and `entities/CHARACTERIZATION_2026-08-19.yaml`.

## Narrative theory boundary
Universal `KO.*` narrative theory remains in the external Narrative Knowledge Base. This repository stores Claes-specific Narrative Instances and may reference Knowledge Objects as analysis targets.

Archetypal analysis is permitted as an author-side character-web lens, but an archetype is not a complete person and never overrides entity biography, historical evidence, motive, desire, class, confession, work or material circumstance. Do not force every character into an archetype or write archetypal labels into literary exposition.

## Editorial boundary
Historical accuracy, continuity and canon consistency are **necessary constraints but not proof of literary success**.

A scene may be fully correct and still receive `CUT`.

Reader feedback is evidence about delivery, not a vote on canon. Separate a reader's reported experience/problem from that reader's proposed solution. Repeated independent reader observations carry more revision weight than isolated taste.

AI cold-reader simulation is useful but does not substitute for actual human pilot readers.

## Synchronization rule
Use dependency order:

`human decision → STC → ENT/OBJ/knowledge → WORLD/domain state → NI/ARC/REL/MOTIF/THEME/VALUE → causal story projection → operating master → prose/scene implementation → editorial gates + reader evidence → Lemma if deterministic → validation/review`.

If technical limitations prevent a complete pass, report `SYNC_PENDING` with exact stale records; never hide partial synchronization.

## Review questions
A change must make clear:

- what evidence changed;
- what story truth changed;
- what decision supports it;
- where it is dramatized;
- which continuity domains are affected;
- whether the scene survives `RETAIN / REVISE / MERGE / CUT`;
- what reader experience is intended and what cold/pilot-reader evidence exists;
- whether Lemma changes;
- whether all downstream representations are synchronized.
