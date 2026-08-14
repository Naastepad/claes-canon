# Handoff — Goes stadsbrand 1554 — 14 August 2026

Status: `SYNC_COMPLETE` on authoring branch `authoring/goes-fire-1554-20260814`  
PR: #4 — `Enrich 1554 Goes fire reconstruction and keep mother fate open`

## Scope

This synchronization incorporates the source-critical reconstruction of the 18 May 1554 Goes city fire into the evidence, world, narrative-instance, open-decision and human-readable Storybible layers without converting open fiction choices into canon.

## Read / authority checks

Before mutation the authoring workflow and authority rules were checked through `AGENTS.md`, `AI_ONBOARDING.md`, `REPOSITORY_INTEGRITY.md`, `AUTHORING_POLICY.md`, current `canon/DECISIONS.yaml`, current `canon/OPEN_DECISIONS.yaml`, current Goes world/source/claim records, the active operating master and the repository validator.

The branch was created fresh from canonical `main` at `3e33eeb4d15fca1a7a3f072ded26c623cb032410`.

## Synchronized changes

- `sources/SRC-HIST-GOES-LIVING-CITY-001.md`
  - explicit source provenance for Brandweer Goes / Zeeuwse Ankers / Erfgoed Goes;
  - salt works fixed to the northern harbour zone;
  - 81 keten treated as total harbour inventory, not proven burned count;
  - source-weighted spread corridor and casualty uncertainty;
  - modern NIST firebrand material segregated as physical analogy only;
  - scene-blocking time bands explicitly marked inference, not archival time.
- `claims/SOURCE_CLAIMS_GOES_LIVING_CITY.yaml`
  - added `SC.HIST.GOES.SALT.NORTH_HARBOUR_1554.001`;
  - expanded `SC.HIST.GOES.FIRE_1554.FOOTPRINT.001`;
  - added `SC.HIST.GOES.FIRE_1554.SPREAD.001`;
  - added `SC.MODEL.GOES.FIRE_1554.FIREBRANDS.001`;
  - added `SC.HIST.GOES.FIRE_1554.CASUALTIES.001`.
- `narrative/world_goes_living_city.yaml`
  - added a dedicated `fire_1554_reconstruction` block with fixed history vs modelled scene blocking;
  - added a `1554_fire` time slice;
  - preserved the older-Nieuwstraat/Armenhoek house as not historically proven destroyed.
- `narrative/instances.yaml`
  - enriched `NI.EVENT.GOES_FIRE.1554.001` with source refs, supported route, sensory blocking, modelled timing bands and household-intersection guardrails.
- `canon/OPEN_DECISIONS.yaml`
  - added `OPEN.MOTHER.FIRE_1554.001`;
  - made `OPEN.MOTHER.ADULT_FUNCTION.001` conditional on survival of 1554.
- `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md`
  - incorporated the corrected northern-harbour geography, brandwaaier spread model, speed guardrails, household intersection, casualty uncertainty and the mother's still-open fate.

## Canon / evidence boundary

Historical / supported:
- fire date 18 May 1554;
- origin in one unidentified Oostzelke salt pan in the northern harbour-industrial zone;
- strong north-easterly wind;
- supported damage in harbour, Turfkade, watermill and Kruisbroeders/western fabric;
- current source-weighted scale about one quarter of city/harbour building stock;
- no reliable casualty count in the present fire-specific evidence bundle.

Reconstruction / proposal:
- multi-front `brandwaaier` / firebrand-spotting model;
- order-of-magnitude scene timing bands;
- local firebrand ignition at the family residence while the main dwelling survives.

Open author decision:
- `OPEN.MOTHER.FIRE_1554.001` — whether Claes' mother survives the fire. No death has been canonised. If death is later chosen, it remains fictional and must follow the spatial/evidence guardrails recorded in the Storybible.

## Validation

GitHub Actions run `31802949449`, **Validate Claes canon repository**, completed successfully on PR head `2bf33122b4e1e01b65f762026e30d343a83f7dc5`. The continuity compiler step passed.

No Lemma rules were changed because the new material is historical evidence, narrative scene blocking and an open character decision rather than a new deterministic canon constraint.

## Remaining human action

Review PR #4. Do not merge this handoff merely because validation is green: validation confirms structural continuity, not the literary choice about Claes' mother. The mother's 1554 fate remains explicitly OPEN until the author decides it.
