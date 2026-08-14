# Synchronization status

Status: `SYNC_COMPLETE`

Release state: `MAIN_CANONICAL`

PR #3 has been merged into `main` on the author's explicit instruction. GitHub `main` is now the canonical source of truth for the integrated Goes church, living-city, residence, old-Nieuwstraat and rederijker-location work.

## Canonical authority chain
- `canon/DECISIONS_2026-08-13.md` and `canon/DECISIONS_2026-08-14.md` — human-readable decisions;
- `canon/DECISIONS.yaml` — machine-readable decision IDs through 14 August 2026;
- `claims/STORY_CLAIMS.yaml` and `claims/STORY_CLAIMS_2026-08-14.yaml` — active story truths;
- `claims/SOURCE_CLAIMS_GOES_LIVING_CITY.yaml` and `claims/SOURCE_CLAIMS_GOES_2026-08-14.yaml` — normalized Goes evidence;
- `entities/ENTITIES.yaml`, `entities/GOES_LIVING_CITY.yaml`, `entities/GOES_GROTE_KERK.yaml` — persons, properties and locations;
- `narrative/world_goes_living_city.yaml` and `narrative/world_goes_grote_kerk.yaml` — time-sensitive Goes scene frameworks;
- `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` and `storybible/MASTER.md` — synchronized human-readable operating authority;
- `review/MIGRATION_REVIEW.yaml` — all 37 Story Claims classified, including the three explicit 14-August human decisions;
- `scripts/validate_canon.py` — cross-layer validation through 14 August 2026.

## Canonical Goes decisions now on main
- `DEC.CORNELIS.RESIDENCE.GOES.2026-08-14`: the historically documented house bought by Claes Jacobsz. Nissepat on 20 March 1542 in the older Nieuwstraat is the fictional Cornelis household's childhood home. Purchase/topology are historical; occupancy is novel canon. Residence is separate from business.
- `DEC.GOES.NIEUWSTRAAT.IDENTITY.2026-08-14`: pre-1594 `Nieuwstraat` is the older Nieuwstraat/Oude Nieuwstraat in or by the Armenhoek at the supported zone level, distinct from the planmatige/current Nieuwstraat of the 1594 expansion; exact 1542 street axis remains unknown.
- `DEC.GOES.REDERIJKERS.MEETINGPLACE.2026-08-14`: Cornelis-era rederijker meetings use the Zusterhuis/former Zwarte-Zusters complex at the Singelstraat. The Nardusbloem moved to the Sint-Sebastiaanshof only in 1626; that later site is not back-projected.

The corresponding former open records remain in `canon/OPEN_DECISIONS.yaml` with `status: RESOLVED` for audit history.

## Remaining related question
- `OPEN.CORNELIS.REDERIJKERS.CHAMBER.001` remains open only for the **named chamber identity** of fictional Cornelis. Meeting location is closed. The Nardusbloem/old Magdalena-linked chamber and a generic Goese kamer remain the historically safest options; Edele Castanienbloem must not be back-projected as historical Cornelis-era fact.

## Spatial integrity rules
- ownership, residence, business operation and adjacency remain distinct relations;
- the 9,912-act transport corpus is a dense social/property evidence layer, not proof that every ownership chain is a simultaneous physical house;
- four belendingen support topology and street-side reasoning, not exact cadastral polygons;
- the older Nieuwstraat is resolved at toponym/Armenhoek-zone level only; its exact old axis must not be invented;
- the 1542 family home is on the west side of its historical street according to the deed topology (street east);
- the family home is not declared burned in 1554 without parcel-level evidence;
- 1554 fire and 1572 military destruction remain separate event footprints;
- the 1572 burned Voorstad brewery is not automatically the equipped Nissepad brewery documented in 1577;
- Zusterhuis, Maria Magdalena devotional space and post-1626 Sint-Sebastiaanshof remain distinct places/functions/times.

## Validation state
Repository continuity validation passed before merge on the synchronized content at PR commit `9f89ab435c79a50693159b4bb7bb656d88469465` in workflow run **121**. The only later feature-branch commit before merge changed this synchronization-status document. The merge commit is `e35ccdd7b5e5268d143522c96e34f67165100c7b`.

## Legacy/audit note
- `storybible/LEMMA_MCKEE_MASTER.md` remains the earlier transformed work edition; the dated operating master is authoritative while legacy wording remains unreconciled there.
- Resolved `OPEN.*` records are retained rather than deleted.
- `MOTIF.SINNE` and `REL.CLAES.BELOVED` retain their original base records; their approved 13-Aug-2026 development remains represented by the canonical extension records.

## Lemma execution policy
- `lemma/*.lemma` remains the repository's deterministic rules-as-code layer and is versioned and validated in GitHub.
- GitHub `main` is authoritative for both Storybible content and Lemma source.
- LemmaBase is optional and downstream-only; it never overrides GitHub canon.
