# Open PR closure audit — 16 August 2026

**Purpose:** determine whether any still-valid material from PRs #2, #4, #7 and #11 remained outside `main` before closing those superseded branches.

## PR #11 — alchemical refinement / Nardusbloem-Castanien

**Disposition:** close as **integrated and superseded by newer main projection**.

Already present on `main` before this audit were the governing 16-August decisions, source records for Agricola/Norton/Ercker/Morhof, alchemy Source Claims and Story Claims, objects, narrative/knowledge supplements, the alchemical refinement dossier and handoff. Active `main` files are newer because they also incorporate the later Seton/Brevísima separation and registry cleanup.

No wholesale merge is appropriate. This audit additionally removes the remaining generic chamber-open wording from the living-city projection: Cornelis' canonical affiliation is Nardusbloem; the 1560s Castanien current is explicit novel reconstruction; only deken status remains open.

## PR #7 — Mayken Lampert

**Disposition:** close as **integrated and superseded by no-cipher-aware main projection**.

The historical Lampart/Lambert/Lampert source dossier and Source Claims from the PR are already present on `main`. Mayken's identity and apothecary-family grounding are also present, but the active Story Claims/entity/dossier on `main` are deliberately newer: old Dodoens/nomenclator/cipher-solving functions are removed. Mayken remains an independent material, botanical, sensory and error-check counterpart and later companion in Claes' recovery of *sinne*.

No further PR #7 merge is appropriate.

## PR #4 — Goes fire 1554

**Disposition:** close as **partially salvaged; obsolete story-choice portion rejected**.

Valid material recovered into `main` in this closure pass:

- northern harbour placement of the salt-work complex;
- 81 keten as cited harbour-zone inventory, not 81 proven destroyed;
- source-weighted spread corridor from Oostzelke through harbour/northern-western Goes;
- qualitative firebrand/spotting model for scene blocking only;
- historical casualty count remains UNKNOWN in the consulted fire-specific bundle.

These are now recorded in dedicated source and Source Claim supplements and a current-canon narrative refinement.

Not carried over:

- the old proposal that the family house survives;
- the old `OPEN.MOTHER.FIRE_1554` state.

Those were superseded by `DEC.CLAES.FAMILY_FIRE.1554.2026-08-14`: in novel canon the 1542 house is destroyed/uninhabitable and Tanneken, Jan and the unborn child die, while Claes and Cornelis survive away. The repository continues to distinguish those fictional outcomes from historical parcel/victim evidence.

## PR #2 — Claes chronology to 1542

**Disposition:** close as **mostly integrated; residual provenance and guardrails salvaged**.

The birth date 8 December 1542 and the Goes → intended Zierikzee → actual Reimerswaal educational route were already active canon. This closure pass additionally recovers:

- a dedicated historical source record for the primitive 1542 *Brevísima* textual state and its Valencia 8 December 1542 completion date;
- a Source Claim recording that historical textual date strictly as resonance, not proof of Claes;
- craft guardrails forcing all age-sensitive writing to derive from 8 December 1542;
- explicit Reimerswaal guardrails: elementary schooling precedes the move, and the long 1554–1561 stay develops into older-pupil formation rather than seven years of beginner curriculum.

The older PR's references to now-retired cipher architecture are not imported.

## Additional drift found during PR inspection

The PR comparison exposed active-projection drift not caught by the structural compiler:

1. `narrative/CRAFT_GUARDRAILS.yaml` still contained the retired Dodoens/Primus/multi-week cipher-recovery sequence.
2. `narrative/world_modules.yaml` still described print-network roles using cipher-key language.
3. `narrative/world_goes_living_city.yaml` still treated Cornelis' generic named chamber as open.
4. `storybible/TRANSFORMATION_LEDGER.yaml` still pointed at obsolete paths such as `narrative/open_questions.yaml` and treated the Revision 11 code architecture as normally active.

All four are corrected in the same closure pass.

## Validation rule added

`scripts/validate_active_projection.py` now supplements the structural continuity compiler. It checks the writer-facing active projection for known superseded markers and requires the current birth, education, direct-reveal and Cornelis chamber states. The main GitHub Actions continuity workflow runs both validators.

## Closure criterion

PRs #2, #4, #7 and #11 may be closed only after:

1. this selective integration is committed to `main`;
2. repository continuity validation passes;
3. active-projection validation passes;
4. no new open PR supersedes the inspected branches.

Closing these PRs does **not** mean all story design/research questions are solved. Genuine questions remain deliberately registered in `canon/OPEN_DECISIONS*.yaml`; they are not repository-integrity defects.
