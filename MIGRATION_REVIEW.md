# Migration Review — PR #1

This document tracks what still requires author review before the Lemma/McKee Storybible transmutation can be merged.

## Review categories

- **MIGRATED** — existing canon normalized into the new schema; check fidelity only.
- **DERIVED** — formulation distilled from existing canon; human review required until approved.
- **NEW** — genuinely new story choice; explicit human decision required.
- **CONFLICT** — canon drift or incompatible authorities; merge blocker until resolved.

These categories are independent from `evidence_status` and `canon_status`.

## Current review summary — after author decisions 13 August 2026

| Review bucket | Count | Status |
|---|---:|---|
| MIGRATED / migration check | 30 | No creative re-decision required; fidelity audit only. |
| DERIVED / reviewed | 4 | Approved with author refinements. |
| NEW / human decision | 0 | None. |
| CONFLICT | 0 | Birth conflict explicitly resolved. |

Machine-readable source: `review/MIGRATION_REVIEW.yaml`.
Author decision record: `canon/DECISIONS_2026-08-13.md`.

## Resolved birth conflict

`STC.CLAES.BIRTH.001` is resolved by explicit author decision:

**Claes Cornelisz Nissepat is born in Goes on 8 December 1542.**

The transformed `8 December 1545` representation is migration drift and must be synchronized out of downstream records. The decision retains the intended chronology in relation to the Brevísima framing.

## Approved derived character architecture

### `STC.CLAES.SINNE.001`
Approved with refinement. Claes discovers the world through embodied **sinne**. Fire, flood, death and loss progressively blunt/constrict this sensory openness. On the road toward Enkhuizen, with his beloved — the still-to-be-developed apothecary's daughter — beside him, Claes rediscovers the sinne. Their renewed resonance within him becomes a catalyst for recovery, deeper understanding, wisdom and inner sovereignty as an alchemist undertaking the Great Work.

### `STC.CLAES.PARADOX.001`
Approved with refinement. His gift is prolonged exact observation; his shadow is remaining in observation after action is required. The paradox is deepened by trauma: maturity means recovering sensation, distinguishing what it asks of him, and converting perception into responsible choice.

### `STC.CLAES.NEED.001`
Approved with refinement. Psychological need: recover trust in embodied perception and act without complete certainty. Moral need: understand that knowledge and perception increase responsibility toward the other. Recovered sinne joins perception, discernment, choice and acceptance of consequence without total control.

### `STC.CLAES.MORAL_QUESTION.001`
Approved with refinement. The movement from **“What is true?”** to **“What does this truth ask of me toward the other?”** is Claes' spiritual journey from matter toward spirituality. Matter remains the vessel: senses, bodies, craft, books, plants, fire, water and alchemical operations lead toward discernment, responsibility, wisdom and sovereignty. The Great Work transmutates knowledge-as-control into wisdom-in-relation and culminates in transmission/release rather than possession.

## Remaining migration work

The review decisions themselves are complete. Before merge, the structured downstream representations must be synchronized with them, especially:

- `claims/STORY_CLAIMS.yaml`
- `entities/ENTITIES.yaml`
- `storybible/LEMMA_MCKEE_MASTER.md`
- `narrative/arcs.yaml`
- `narrative/themes.yaml`
- age-dependent Narrative Instances and chronology

The other migrated Story Claims remain a fidelity audit rather than fresh creative decisions.

## Rule for future conversions

Every new structured Story Claim added during migration must carry an origin and review state:

`MIGRATED → fidelity check`

`DERIVED → human review`

`NEW → explicit author decision`

`CONFLICT → stop and resolve`

An unresolved `CONFLICT` blocks merge and LemmaBase publication.
