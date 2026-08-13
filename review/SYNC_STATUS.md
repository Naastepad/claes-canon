# Synchronization status

Status: `SYNC_PENDING`

The explicit author decisions of 13 August 2026 remain propagated through the active operating model. The historically grounded Catholic Scripture/liturgy world module and the Wendy Wauters sensory-religious-space module are now both linked into the active authoring model on `authoring/v1`; source/provenance and local Zeeland verification remain partly pending.

Synchronized authority chain for the 13-Aug-2026 canon decisions:
- `canon/DECISIONS_2026-08-13.md` — human-readable decisions
- `canon/DECISIONS.yaml` — machine-readable decision IDs
- `claims/STORY_CLAIMS.yaml` — birth and approved character claims
- `entities/ENTITIES.yaml` — Claes birth and beloved recovery role
- `narrative/arcs.yaml` — birth anchors corrected to 1542
- `narrative/themes.yaml` — psychological need, moral need, spiritual journey and `VALUE.CLAES.SINNE`; `VALUE.CLAES.SINNE` now explicitly links to `WORLD.RELIGIOUS_SPACE.SENSORY_CHURCH`
- `narrative/sinne_recovery.yaml` — canonical trauma/constriction/recovery/sovereignty extension
- `narrative/beloved_recovery.yaml` — beloved/apothecary-daughter role in the Enkhuizen recovery line
- `narrative/religious_space_sensory_church.yaml` — active Wauters-grounded sensory church/world module
- `sources/SRC-WAUTERS-RELIGIOUS-SPACE-2021.md` — Wauters source/provenance and transferability record
- `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` — current synchronized operating master; now explicitly references the sensory church module and Wauters source record
- `review/MIGRATION_REVIEW.yaml` and `MIGRATION_REVIEW.md` — review decisions resolved
- `scripts/validate_canon.py` — cross-layer assertions for the 13-Aug-2026 decisions

## 13-Aug-2026 Catholic Bible/liturgy research addition
Updated on `authoring/v1`:
- `claims/SOURCE_CLAIMS.yaml` — added Source Claims for Latin/Vulgate Catholic norm, Leuven Bible 1548, Liesvelt Bible confessional profile, and gradual Catholic identity change during the Revolt.
- `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` — added worldbuilding section **Catholic Scripture, liturgy and confessional change, ca. 1550–1580**, including the Lucas 8 / sower guardrail and an explicit warning not to generalize non-Zeeland models onto Goes.

## 13-Aug-2026 Wendy Wauters sensory religious-space addition
Updated on `authoring/v1`:
- `sources/SRC-WAUTERS-RELIGIOUS-SPACE-2021.md` — records the evidentiary basis from *De beroering van de religieuze ruimte* and companion/public-facing *De geuren van de kathedraal*, including the three-level transferability guardrail: Antwerp source-direct, Low Countries transferable with scaling, and local verification required.
- `narrative/religious_space_sensory_church.yaml` — models period *sinne*, sensus communis, the church as institution/building/sensory field/social map/memory palace, guilds and confraternities, rhetoricians, processions, bells, annual variability and seven church-scene templates.
- `narrative/themes.yaml` — `VALUE.CLAES.SINNE` now explicitly links to `WORLD.RELIGIOUS_SPACE.SENSORY_CHURCH`.
- `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` — §11 now explicitly invokes the sensory church module as the governing reconstruction layer for relevant church scenes and preserves the Antwerp → Goes/Reimerswaal transferability limits.

Pending before the wider religious research layer can be called fully synchronized:
1. Add stable provenance records under `sources/` for the DBNL Leuven Bible editorial introduction and Judith Pollmann's *Catholic Identity and the Revolt of the Netherlands, 1520–1635`. The corresponding Source Claims already exist, but their dedicated provenance files are not yet present.
2. Obtain Goes/Zeeland-specific evidence for the exact chronology of public Catholic worship, church-use change, preaching and private/tolerated Catholic practice between 1566 and 1580. Until then, exact local dates remain deliberately open and are not canonized.
3. Validate the branch after provenance completion and reconcile it with current `main` before release/PR.

Legacy/audit note:
- `storybible/LEMMA_MCKEE_MASTER.md` is retained as the earlier transformed work edition and is no longer the active operating master while it contains migration-era wording.
- `MOTIF.SINNE` and `REL.CLAES.BELOVED` retain their original base records; their approved 13-Aug-2026 development is represented by the canonical extension records `MOTIF.SINNE.RECOVERY`, `ARC.CLAES.SINNE_RECOVERY` and `REL.CLAES.BELOVED.RECOVERY`. This is intentional additive normalization rather than silent rewriting.

Release status: branch reconciliation with current `main` and CI verification remain release/PR tasks; they do not change the synchronized canon content above.
