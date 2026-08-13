# Canon Authoring Policy

## Core rule
Evidence, story truth, narrative placement and executable constraints are maintained as separate layers. Explicit human decisions are authoritative and must be synchronized through every dependent representation.

## Required reading before writes
A write-capable AI must read `AI_ONBOARDING.md`, `canon/`, `REPOSITORY_INTEGRITY.md`, this policy, and the relevant registers. It must re-fetch target files immediately before mutation.

## Workflow
1. Read current human decisions, operating Storybible and relevant sources.
2. Record external assertions as `SC.*` Source Claims.
3. Record novel truth or candidate truth as `STC.*` Story Claims.
4. Keep `evidence_status` and `canon_status` independent.
5. Record significant human choices as `DEC.*` or repository-visible decision records.
6. Link claims to `ENT.*` entities and relevant Narrative Instances.
7. Preserve date precision and uncertainty ranges.
8. Synchronize approved decisions through dependent entities, objects, knowledge states, Narrative Instances, arcs, relationships, motifs, themes/values and the operating master.
9. Convert only deterministic accepted Story Claims into Lemma constraints.
10. Run continuity and Lemma validation.
11. Review changes before merge and LemmaBase publication.

## Multi-agent rule
Never assume this repository is unchanged because the current chat wrote it earlier. Another session or model may have written meanwhile. Re-fetch branch state and target files before every write pass. If content changed, reconcile instead of overwriting. Follow `REPOSITORY_INTEGRITY.md`.

## Branch rule
Canon development belongs on an authoring branch/PR. Do not merge, force-update, delete history, publish to LemmaBase, or promote OPEN/PROPOSED material without explicit human authority.

## Status vocabularies
Evidence: `VERIFIED`, `SUPPORTED`, `PLAUSIBLE`, `DISPUTED`, `UNKNOWN`.
Canon: `PROPOSED`, `CANON`, `OPEN`, `DEPRECATED`, `REJECTED`.
These are independent dimensions. A historical fact can be verified without being used in the novel; a fictional event can be plausible and canon.

## Precision rule
A month, season, year or interval remains that precision until an explicit story decision establishes greater precision.

## Narrative theory boundary
Universal `KO.*` narrative theory remains in the external Narrative Knowledge Base. This repository stores Claes-specific Narrative Instances and may reference Knowledge Objects as analysis targets.

## Synchronization rule
Use dependency order:
`human decision → STC → ENT/OBJ/knowledge → NI/ARC/REL/MOTIF/THEME/VALUE → operating master → Lemma → validation/review`.
If technical limitations prevent a complete pass, report `SYNC_PENDING` with exact stale records; never hide partial synchronization.

## Review questions
A change must make clear what evidence changed, what story truth changed, what decision supports it, where it is dramatized, which continuity domains are affected, whether Lemma changes, and whether all downstream representations are synchronized.
