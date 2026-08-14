# Synchronization status

Status: `SYNC_COMPLETE_ON_FEATURE_BRANCH`

Release state: `MERGE_AUTHORIZED_BY_HUMAN`

`main` remains canonical until PR #3 is merged. The author has explicitly ordered the merge of PR #3 after resolving the Goes residence, Nieuwstraat and rederijker-location questions.

## Authority chain synchronized on PR #3
- `canon/DECISIONS_2026-08-13.md` and `canon/DECISIONS_2026-08-14.md` — human-readable decisions;
- `canon/DECISIONS.yaml` — machine-readable decision IDs through 14 August 2026;
- `claims/STORY_CLAIMS.yaml` and `claims/STORY_CLAIMS_2026-08-14.yaml` — active story truths;
- `claims/SOURCE_CLAIMS_GOES_LIVING_CITY.yaml` and `claims/SOURCE_CLAIMS_GOES_2026-08-14.yaml` — normalized Goes evidence;
- `entities/ENTITIES.yaml`, `entities/GOES_LIVING_CITY.yaml`, `entities/GOES_GROTE_KERK.yaml` — persons, properties and locations;
- `narrative/world_goes_living_city.yaml` and `narrative/world_goes_grote_kerk.yaml` — time-sensitive Goes scene frameworks;
- `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` and `storybible/MASTER.md` — synchronized human-readable operating authority;
- `review/MIGRATION_REVIEW.yaml` — all 37 Story Claims classified, including the three explicit 14-August human decisions;
- `scripts/validate_canon.py` — cross-layer validation through 14 August 2026.

## PR #3 — integrated scope
The branch contains the Maria Magdalenakerk evidence, living-city framework, old-Nieuwstraat reconstruction, Cornelis household residence decision and the corrected rederijker meeting chronology.

### Closed Goes decisions
- `OPEN.CORNELIS.RESIDENCE.GOES.1542.001` → resolved by `DEC.CORNELIS.RESIDENCE.GOES.2026-08-14`: the historically documented house bought by Claes Jacobsz. Nissepat on 20 March 1542 in the older Nieuwstraat is the fictional Cornelis household's childhood home. Purchase/topology are historical; occupancy is novel canon. Residence is separate from business.
- `OPEN.GOES.NIEUWSTRAAT.PRE1594.001` → resolved by `DEC.GOES.NIEUWSTRAAT.IDENTITY.2026-08-14`: pre-1594 `Nieuwstraat` is treated as the older Nieuwstraat/Oude Nieuwstraat in or by the Armenhoek, distinct from the planmatige/current Nieuwstraat of the 1594 expansion; exact 1542 street axis remains unknown.
- `OPEN.GOES.REDERIJKERS.MEETINGPLACE.001` → resolved by `DEC.GOES.REDERIJKERS.MEETINGPLACE.2026-08-14`: Cornelis-era meetings use the Zusterhuis/former Zwarte-Zusters complex at the Singelstraat. The Nardusbloem moved to the Sint-Sebastiaanshof only in 1626, so that later meeting place is not back-projected.

### Remaining related question
- `OPEN.CORNELIS.REDERIJKERS.CHAMBER.001` remains open only for the **named chamber identity** of fictional Cornelis. Meeting location is already closed. The Nardusbloem/old Magdalena-linked chamber and a generic Goese kamer are the historically safest options; Castanienbloem is not to be back-projected as historical Cornelis-era fact.

## Spatial integrity rules
- ownership, residence, business operation and adjacency remain distinct relations;
- the 9,912-act transport corpus is a dense social/property evidence layer, not proof that every ownership chain is a simultaneous physical house;
- four belendingen support topology and street-side reasoning, not exact cadastral polygons;
- the older Nieuwstraat is resolved at toponym/zone level only; its exact old axis must not be invented;
- the 1542 family home is on the west side of its historical street according to the deed topology (street east);
- 1554 fire and 1572 military destruction remain separate event footprints;
- the family home is not declared burned in 1554 without parcel-level evidence;
- the 1572 burned Voorstad brewery is not automatically the equipped Nissepad brewery documented in 1577;
- Zusterhuis, Maria Magdalena devotional space and post-1626 Sint-Sebastiaanshof are distinct places/functions/times.

## Validation state
Repository continuity validation **passed** on PR-head `9f89ab435c79a50693159b4bb7bb656d88469465` in workflow run **121**. The validator includes explicit assertions for the three 14-August decisions, 37 migration-reviewed Story Claims, the residence links, old-Nieuwstraat uncertainty boundary and the Nardusbloem Zusterhuis→Sint-Sebastiaan chronology.

## Legacy/audit note
- `storybible/LEMMA_MCKEE_MASTER.md` remains the earlier transformed work edition; the dated operating master is authoritative while legacy wording remains unreconciled there.
- Resolved `OPEN.*` records are retained with `status: RESOLVED` for audit history rather than deleted.
- `MOTIF.SINNE` and `REL.CLAES.BELOVED` retain their original base records; their approved 13-Aug-2026 development remains represented by the canonical extension records.

## Lemma execution policy
- `lemma/*.lemma` remains the repository's deterministic rules-as-code layer and is versioned and validated in GitHub.
- GitHub `main` is authoritative after merge for both Storybible content and Lemma source.
- LemmaBase is optional and downstream-only; it never overrides GitHub canon.
