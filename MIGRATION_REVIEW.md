# Migration Review — PR #1

This document tells the author what actually requires review before the Lemma/McKee Storybible transmutation can be merged.

## Meaning of the categories

**MIGRATED** means the content already existed as canon in the source Storybible and has been normalized into the new schema. It does **not** require a fresh story decision. Review only whether the migration preserved the meaning.

**DERIVED** means the structured statement was formulated by the conversion process from existing canon. It may be a useful McKee/NOS condensation, but the wording or scope itself still requires human review.

**NEW** means a genuinely new story choice introduced during conversion. It requires explicit author approval before becoming canon.

**CONFLICT** means the conversion found incompatible canon authorities or canon drift. A conflict blocks merge until resolved explicitly.

These categories are independent from `evidence_status` and `canon_status`.

## Current review summary

| Review bucket | Count | What you need to do |
|---|---:|---|
| MIGRATED / migration check | 29 | Bulk-check that meaning was preserved; no need to re-decide the story. |
| DERIVED / human review | 4 | Approve, edit or reject the structured formulation. |
| NEW / human decision | 0 | No new Story Claims currently require a fresh decision. |
| CONFLICT | 1 | Must be resolved before merge. |

The machine-readable source for this report is `review/MIGRATION_REVIEW.yaml`.

## Merge blocker

### STC.CLAES.BIRTH.001 — birth date/year

**Current transformed record:** Claes is born in Goes on **8 December 1545**.

**Conflict detected:** the previously established project canon available to the authoring process gives **1542 as the birth year**, while no explicit author decision has been identified that replaces it with 1545 or establishes 8 December as a fixed birth date.

**Status:** `CONFLICT`.

**Required action:** human decision. Do not let an AI resolve this from plausibility, chronology or the latest prose version alone. Once the author resolves it, update at least:

- `claims/STORY_CLAIMS.yaml`
- `entities/ENTITIES.yaml`
- `storybible/LEMMA_MCKEE_MASTER.md`
- any age-dependent `NI.*` records and chronology
- relevant source/transformation records if the change represents correction rather than new canon

The repository should then remove the `CONFLICT` state only after validation.

## Four derived claims requiring wording review

These are not necessarily wrong; they are explicit condensations created by the McKee/NOS conversion and therefore deserve author review as formulations.

1. `STC.CLAES.SINNE.001` — Claes' cognitive movement from sensation/perception toward choice.
2. `STC.CLAES.PARADOX.001` — his gift of prolonged observation versus the danger of observing after action is required.
3. `STC.CLAES.NEED.001` — knowledge does not remove responsibility; action cannot wait for complete certainty.
4. `STC.CLAES.MORAL_QUESTION.001` — movement from “What is true?” toward “What does this truth ask of me toward the other?”

For these four, review the **formulation and emphasis**. Their source material is already present in the Storybible; they are not four invitations to redesign Claes from scratch.

## Migrated Story Claims

The other 29 current `STC.*` records are classified as meaning-preserving migration. They cover the established education route, Reimerswaal, Zierikzee plan, Landjuweel/Antwerp route, Dee/Silvius formation, macro-Nigredo hinge, memoriaal phases, return to Goes, Cornelis work-canon, recovery chain and its guardrails, 1570 reconstruction duration, 1578 publication line, Delft 1584, Projectio, macrostructure, music/bread transformation and Nissepad reconstruction.

Review these as a **migration audit**, not as 29 new creative proposals. If a migrated statement does not faithfully reflect the previous canon, reclassify it as `CONFLICT` rather than silently rewriting history.

## Rule for future conversions

Every new structured Story Claim added during migration must receive:

- `origin: MIGRATED | DERIVED | NEW`
- `review_state: MIGRATION_CHECK | HUMAN_REVIEW | HUMAN_DECISION | CONFLICT`

The intended decision logic is:

`MIGRATED → check fidelity`

`DERIVED → review interpretation`

`NEW → explicit author decision`

`CONFLICT → stop and resolve`

A pull request containing an unresolved `CONFLICT` must remain draft and must not be published to LemmaBase.
