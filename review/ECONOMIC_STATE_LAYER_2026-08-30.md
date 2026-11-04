# Economic state layer handoff — 30 August 2026

**Branch:** `author/economic-state-layer-2026-08-30`  
**Status:** AUTHORING LAYER IMPLEMENTED / CENTRAL REGISTRY SYNC PENDING  
**Canon impact:** NONE — evidence/world-context only; no Story Decision closed  
**Protected open:** `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001`

## Objective

Build two evidence-bounded economic authoring tracks and a resolver:

A. **GOES ECONOMIC BASELINE 1542–1572** — money/accounting, measures, beer distribution, salt labour, local prices and explicit wage gaps.

B. **WAR ECONOMY 1567–1602** — Alva taxation, political-control split, licent/convoy, beer war levy, coin countermarks, siege emergency money, military pay/provisioning and late price-series availability.

Then resolve economic context by `date + place + political control + role + transaction`, rather than by generic century/province assumptions.

## Governing canon preserved

- Cornelis is a **biersteker / merchant-distributor**, not a brewer.
- The documented Nissepad brewery is not automatically Cornelis' property.
- `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001` remains OPEN.
- The 1572 burned Voorstad brewery is not identified with the documented 1577 Nissepad brewery.
- Ordinary property transfers are not relabelled confiscations.
- Historical mechanisms do not create fictional participation.

## Files added

### Evidence / provenance

- `sources/SRC-SECONDARY-DIRKSEN-GEZAG-GELD-ZEELAND-2012-001.md`
- `sources/SRC-IISG-HISTORICAL-PRICES-WAGES-2023-001.md`
- `sources/SRC-HIST-ALVA-TAXATION-1569-1572-001.md`
- `sources/SRC-HIST-REVOLT-COINAGE-EMERGENCY-MONEY-1573-1576-001.md`
- `sources/SRC-HIST-MILITARY-PAY-LOWCOUNTRIES-1567-1700-001.md`
- `sources/SRC-RESEARCH-WEB-ECONOMY-2026-08-30.md`
- `claims/SOURCE_CLAIMS_ECONOMY_2026-08-30.yaml`

### Storybible/world authoring

- `storybible/domains/GOES_ECONOMIC_BASELINE_1542_1572.md`
- `storybible/domains/WAR_ECONOMY_1567_1602.md`
- `narrative/economic_state_resolver.yaml`
- `narrative/economic_world_modules_2026-08-30.yaml`
- `narrative/economic_scene_packs_2026-08-30.yaml`

## File updated

- `sources/SRC-SECONDARY-BOONMAN-METROLOGY-2015-001.md`

Expanded from medicinal/Antwerp metrology to include the newly consulted Goese grain-measure, beer-measure, salt-labour, rye-price and coin/accounting passages with evidence boundaries.

## High-confidence findings encoded

1. `1 pond Vlaams = 240 groten = 120 stuivers = 6 carolusguldens` as the accounting relation used in the layer.
2. Goese `viertel/sack = 2 achtendelen`; sixteenth-century reconstructed achtendeel values vary by source/date, so no timeless litre conversion is canonized.
3. Goese beer measurement before sale by a sworn biermeter is documented as a strong local antecedent; exact 1540s–1560s tariff/wording remains open.
4. 1546 Goese salt-work payment of 4 groten per man for a defined hundred-salt handling task is **piecework, not day wage**.
5. 1595 Goese rye transaction provides a hard late local price anchor; it is explicitly blocked from back-projection to 1554.
6. Philipsdaalder rated value changes across Claes' lifetime; coin name alone is not a value resolver.
7. Alva's 1569 100th/20th/10th-penny project is separated from actual local collection; 1569–1572 is modelled as proposal/negotiation/implementation conflict unless payment is locally evidenced.
8. Zeeland 1572–1576 is politically/fiscally divided; Goes/Zuid-Beveland remain on the landsheerlijk side.
9. Rebel Zeeland: licentrecht from 1573; convoygeld introduced in 1576.
10. Rebel Zeeland: four-stuiver-per-ton beer levy from 1 May 1574, borne at brewer production/import point rather than every biersteker sale.
11. Holland 1573 countermark intervention and related rebel-Zeeland klop are political-zone rules, not province-wide generic money.
12. Emergency money is a **named siege-city override**, not `war=true` behaviour.
13. Royal infantry nominal soldij baseline of about 4–5 stuivers/day is kept distinct from civilian wages and actual received pay.
14. IISG bread and rye/wheat series begin in 1594 and overlap Claes 1594–1602, but every numerical use requires unit/place/provenance audit.

## Resolver design

`narrative/economic_state_resolver.yaml` resolves in this order:

1. date/place;
2. political control (**hard gate**);
3. local baseline;
4. war modifier;
5. actor/transaction filter;
6. coin/measure date filter;
7. evidence grade + unresolved data + forbidden inferences.

Source grades:

`A_DIRECT > B_LOCAL_SERIES > C_REGIONAL_PROXY > D_CONTEXT_ONLY`.

The resolver includes mappings for the current known Goes youth chapters, the 1564 Antwerp sequence and `CH.DE_MARKT_VAN_DELFT.1584`, plus the H01–H13 causal hinges where economic context is relevant.

## Explicit numeric gap

`GAP.ECON.GOES.WAGES.1540_1602` remains **HIGH priority**.

Published research points to Goese municipal accounts, including the city-account inventory series previously identified in research, but the actual Goese civilian wage observations have not yet been extracted here. Until then:

> no Amsterdam, Haarlem, Antwerp or Bergen-op-Zoom wage may be relabelled as a Goese wage.

## Central registry synchronization

`SYNC_PENDING` deliberately remains for:

- merging `narrative/economic_world_modules_2026-08-30.yaml` into `narrative/world_modules.yaml`;
- merging `narrative/economic_scene_packs_2026-08-30.yaml` into `narrative/domain_scene_packs.yaml`;
- navigation additions to `storybible/INDEX.md`;
- authority/navigation additions to `storybible/MASTER.md`;
- release-state addition to `review/SYNC_STATUS.md`.

Reason: the available connector operation replaces an entire existing file rather than applying a bounded patch. After an accidental setup write had already been restored on `main`, the economic pass chose preservation over another full-file replacement. The extension files are complete and reviewable; central folding can be done after PR review with a safer patch-capable workflow.

## Main-branch setup incident

During initial connector routing, transient setup writes accidentally touched `main` (`dummy` test path and `AGENTS.md`). The dummy path was removed and `AGENTS.md` was restored to its exact previous content/blob before this authoring branch was created. The net repository content was restored; the transient commits remain visible in history. No economic content was written to `main`.

## Validation state

- Source/evidence boundaries manually reviewed against the uploaded Boonman and Dirksen PDFs and stronger web/academic sources used in the research pass.
- No canon/open decision intentionally changed.
- Structural CI result: **PENDING PR / NOT YET OBSERVED** at time of this handoff creation.
- Central-registry integration intentionally remains `SYNC_PENDING`, not silently claimed complete.

## Next recommended work

1. review PR evidence boundaries and resolver semantics;
2. run/inspect repository CI;
3. fold registry extensions into central world/scene registries with a patch-capable workflow;
4. update MASTER/INDEX/SYNC_STATUS;
5. extract the Goese wage observations;
6. then add Delft/Holland and Enkhuizen local economic baselines before exact late-scene purse/price calculations.
