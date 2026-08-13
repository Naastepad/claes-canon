# Synchronization status

Status: `SYNC_PENDING`

The explicit author decisions of 13 August 2026 remain propagated through the active operating model. A new historically grounded Catholic Scripture/liturgy world module has now been added on `authoring/v1`, but its source/provenance synchronization is not yet fully complete.

Synchronized authority chain for the 13-Aug-2026 canon decisions:
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

## 13-Aug-2026 Catholic Bible/liturgy research addition
Updated on `authoring/v1`:
- `claims/SOURCE_CLAIMS.yaml` — added Source Claims for Latin/Vulgate Catholic norm, Leuven Bible 1548, Liesvelt Bible confessional profile, and gradual Catholic identity change during the Revolt.
- `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` — added worldbuilding section **Catholic Scripture, liturgy and confessional change, ca. 1550–1580**, including the Lucas 8 / sower guardrail and an explicit warning not to generalize non-Zeeland models onto Goes.

Pending before this research addition can be called fully synchronized:
1. Add stable provenance records under `sources/` for the DBNL Leuven Bible editorial introduction and Judith Pollmann's *Catholic Identity and the Revolt of the Netherlands, 1520–1635`. The connector blocked creation of a new source file during this pass, so the new Source Claims currently reference source IDs whose provenance files are not yet present.
2. Obtain Goes/Zeeland-specific evidence for the exact chronology of public Catholic worship, church-use change, preaching and private/tolerated Catholic practice between 1566 and 1580. Until then, exact local dates remain deliberately open and are not canonized.
3. Validate the branch after provenance completion and reconcile it with current `main` before release/PR.

Legacy/audit note:
- `storybible/LEMMA_MCKEE_MASTER.md` is retained as the earlier transformed work edition and is no longer the active operating master while it contains migration-era wording.
- `MOTIF.SINNE` and `REL.CLAES.BELOVED` retain their original base records; their approved 13-Aug-2026 development is represented by the canonical extension records `MOTIF.SINNE.RECOVERY`, `ARC.CLAES.SINNE_RECOVERY` and `REL.CLAES.BELOVED.RECOVERY`. This is intentional additive normalization rather than silent rewriting.

Release status: branch reconciliation with current `main` and CI verification remain release/PR tasks; they do not change the synchronized canon content above.
