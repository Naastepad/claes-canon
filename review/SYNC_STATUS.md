# Synchronization status

Status: `SYNC_COMPLETE`

Release state: `MAIN_CANONICAL`

The explicit author decisions of 13 August 2026 have been propagated through the active operating model. PR #1 has been merged; `main` is now the canonical source of truth and canonical storage for the Claes Storybible.

Synchronized authority chain:
- `canon/DECISIONS_2026-08-13.md` — human-readable decisions
- `canon/DECISIONS.yaml` — machine-readable decision IDs
- `claims/STORY_CLAIMS.yaml` — birth and approved character claims
- `entities/ENTITIES.yaml` — Claes birth and beloved recovery role
- `narrative/arcs.yaml` — birth anchors corrected to 1542
- `narrative/themes.yaml` — psychological need, moral need, spiritual journey and `VALUE.CLAES.SINNE`
- `narrative/sinne_recovery.yaml` — canonical trauma/constriction/recovery/sovereignty extension
- `narrative/beloved_recovery.yaml` — beloved/apothecary-daughter role in the Enkhuizen recovery line
- `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` — current synchronized operating master
- `review/MIGRATION_REVIEW.yaml` and `MIGRATION_REVIEW.md` — review decisions resolved
- `scripts/validate_canon.py` — cross-layer assertions for the 13-Aug-2026 decisions

Legacy/audit note:
- `storybible/LEMMA_MCKEE_MASTER.md` is retained as the earlier transformed work edition and is no longer the active operating master while it contains migration-era wording.
- `MOTIF.SINNE` and `REL.CLAES.BELOVED` retain their original base records; their approved 13-Aug-2026 development is represented by the canonical extension records `MOTIF.SINNE.RECOVERY`, `ARC.CLAES.SINNE_RECOVERY` and `REL.CLAES.BELOVED.RECOVERY`. This is intentional additive normalization rather than silent rewriting.

Lemma execution policy:
- `lemma/*.lemma` is the repository's deterministic rules-as-code layer and is versioned and validated in GitHub.
- GitHub `main` is authoritative for both Storybible content and Lemma source.
- LemmaBase is optional and is not required for authoring, canon control, writing, validation or continuity checking.
- Any future external Lemma runtime is downstream-only and must never override GitHub canon.
