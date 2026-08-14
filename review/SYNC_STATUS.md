# Synchronization status

Status: `SYNC_COMPLETE_ON_FEATURE_BRANCH`

Release state: `HUMAN_REVIEW_REQUIRED`

`main` remains the canonical source of truth. The explicit author decisions of 13 August 2026 remain synchronized there. The authoring branch `goes-grote-kerk-20260813` / PR #3 now contains an additional source-weighted Goes normalization; it is **not canonical until human review and merge**.

## Main authority chain retained
- `canon/DECISIONS_2026-08-13.md` — human-readable decisions
- `canon/DECISIONS.yaml` — machine-readable decision IDs
- `claims/STORY_CLAIMS.yaml` — birth and approved character claims
- `entities/ENTITIES.yaml` — Claes birth and beloved recovery role
- `narrative/arcs.yaml` — birth anchors corrected to 1542
- `narrative/themes.yaml` — psychological need, moral need, spiritual journey and `VALUE.CLAES.SINNE`
- `narrative/sinne_recovery.yaml` — canonical trauma/constriction/recovery/sovereignty extension
- `narrative/beloved_recovery.yaml` — beloved/apothecary-daughter role in the Enkhuizen recovery line
- `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` — current operating master
- `review/MIGRATION_REVIEW.yaml` and `MIGRATION_REVIEW.md` — review decisions resolved
- `scripts/validate_canon.py` — repository cross-layer validator

## PR #3 — Goes evidence/worldbuilding synchronization
The branch integrates the Maria Magdalenakerk evidence and now also the living-city framework without silently closing story choices.

Added/updated layers:
- `sources/SRC-HIST-GOES-GROTEKERK-001.md` and `claims/SOURCE_CLAIMS.yaml` church evidence from the earlier PR #3 work;
- `entities/GOES_GROTE_KERK.yaml` and `narrative/world_goes_grote_kerk.yaml`;
- `sources/SRC-HIST-GOES-LIVING-CITY-001.md` — transport-register, atlas/topography and event provenance;
- `claims/SOURCE_CLAIMS_GOES_LIVING_CITY.yaml` — normalized property, school, salt-industry, fire, siege and institutional-location claims;
- `entities/GOES_LIVING_CITY.yaml` — addressable Goes locations, historical Nissepat persons and key property/event entities;
- `narrative/world_goes_living_city.yaml` — year-sensitive spatial/social scene framework and route-query protocol;
- `canon/OPEN_DECISIONS.yaml` — Cornelis household residence, pre-1594 Nieuwstraat identity and rederijkers meeting-place explicitly kept OPEN;
- `mapping/CONVERSION_LEDGER.yaml` — Revision-11 sections 18 (Goes), 19 (Nissepad) and 21 (historical Nissepat) advanced from indexed to normalized_core;
- `AGENTS.md` — mandatory spatial-reasoning guardrails for atlas-backed settings;
- `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` — human-readable Goes living-city synthesis.

No new `DEC.*` or `STC.*` has been created for Cornelis' residence, the pre-1594 Nieuwstraat identity, the exact rederijkers meeting place or a direct ownership link between Cornelis and a historical brewery. These remain evidence/proposal/open-decision territory.

## Spatial integrity rules now represented
- ownership, residence, business operation and adjacency are distinct relations;
- the 9,912-act transport corpus is a dense social/property evidence layer, not proof that all ownership chains are simultaneous physical houses;
- four belendingen support topology and street-side reasoning, not exact cadastral polygons;
- named parties/occupations can populate scene backgrounds only at their supported time/location level;
- 1554 fire and 1572 military destruction are separate event footprints;
- the pre-1594 `Nieuwstraat` is not automatically the planned Nieuwstraat of 1594;
- the 1572 burned Voorstad brewery is not automatically the equipped Nissepad brewery documented in 1577;
- individual Nissepat houses are not marked destroyed in 1554 without parcel-level evidence.

## Remaining human decisions
- `OPEN.CORNELIS.RESIDENCE.GOES.1542.001`
- `OPEN.GOES.NIEUWSTRAAT.PRE1594.001`
- `OPEN.GOES.REDERIJKERS.MEETINGPLACE.001`
- existing `OPEN.*` decisions remain unchanged/open unless separately decided.

## Validation state
Repository continuity validation passed on the final synchronized file tree (workflow run 103; the later no-op commit retains the same tree). A passing validator cannot promote PROPOSED or OPEN material to canon.

## Legacy/audit note
- `storybible/LEMMA_MCKEE_MASTER.md` is retained as the earlier transformed work edition and is no longer the active operating master while it contains migration-era wording.
- `MOTIF.SINNE` and `REL.CLAES.BELOVED` retain their original base records; their approved 13-Aug-2026 development is represented by the canonical extension records `MOTIF.SINNE.RECOVERY`, `ARC.CLAES.SINNE_RECOVERY` and `REL.CLAES.BELOVED.RECOVERY`.

## Lemma execution policy
- `lemma/*.lemma` is the repository's deterministic rules-as-code layer and is versioned and validated in GitHub.
- GitHub `main` is authoritative for both Storybible content and Lemma source.
- LemmaBase is optional and downstream-only; it never overrides GitHub canon.
