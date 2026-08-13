# Synchronization status

Status: `SYNC_PENDING`

Explicit author decisions of 13 August 2026 are authoritative.

Already synchronized:
- `claims/STORY_CLAIMS.yaml`
- `entities/ENTITIES.yaml`
- `narrative/themes.yaml`
- `canon/DECISIONS_2026-08-13.md`
- migration review records

Still to synchronize/check:
- `narrative/arcs.yaml`
- `narrative/motifs.yaml`
- `narrative/relationships.yaml`
- `storybible/LEMMA_MCKEE_MASTER.md`
- `scripts/validate_canon.py`
- branch reconciliation with `main`

Until this list is empty, stale downstream values do not overrule the explicit author decisions in `canon/`.
