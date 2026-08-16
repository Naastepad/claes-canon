# Domain rebuild — Round B — 16 August 2026

**Status:** `ROUND_B_DOMAIN_REBUILD_IMPLEMENTED`  
**Purpose:** convert previously thin framework topics and callback-recovered knowledge into chapter-ready authoring domains.

## Readiness definition

A domain is chapter-ready when a scene writer can retrieve, for the relevant place/time/activity:

1. source/provenance and evidence status;
2. time-valid world state;
3. concrete actors and action sequence;
4. materials/objects;
5. sensory diagnostic fields;
6. what the focal character may know/access;
7. local evidence versus transferable reconstruction;
8. explicit anachronism/overclaim guardrails;
9. links into scene packs without creating fictional participation automatically.

## Rebuilt domains

### 1. Bread / grain / baking

New active dossier: `storybible/domains/BREAD_GRAIN_BAKING_1540_1602.md`.

Improvement over old `WORLD.BREAD_GRAIN` framework:
- full craft chain from grain through inspection/sale;
- professional urban bakery as safer scene default than invented household oven;
- bread-assize/economic use;
- sensory craft judgement;
- explicit exclusion of modern recipe precision and rigid grain/class taxonomy.

Still open/local:
- exact Goes baker/address/oven;
- exact normal flour/grain mix and ferment;
- exact sixteenth-century Goes loaf prices/weights.

### 2. Beer / brewing / biersteker

New active domain `WORLD.BEER_BREWING_DISTRIBUTION` and dossier `BEER_BREWING_BEERSTEKER_1540_1580.md`.

Key repair:
- Cornelis' authoring actions now derive from **biersteker/distribution work**, not from assumed brewing;
- brewing remains a background material chain;
- Nissepad brewery stays distinct from Cornelis' professional identity/property status;
- gruit is not an automatic sixteenth-century default;
- no modern beer-style/ABV/IBU projection.

### 3. Reimerswaal / school / cost-pupil life

New active dossier: `REIMERSWAAL_SCHOOL_1554_1561.md`.

Local historical school support is stronger than the previous framework made explicit:
- school reported before 1296;
- 1497 `scolaster` reorganisation into singing master + schoolmaster;
- schoolmaster appointments in 1569/1570.

Boundary:
- durable school institution = historical support;
- Claes' 1554–1561 Latin formation = novel canon/source-weighted reconstruction;
- exact 1554 curriculum, building, teacher/rector and host household = not archival fact.

The city is now time-sliced through 1554 arrival, 1555 water, 1557 structural damage, 1558 fire and 1561 renewed flood without turning each into a disaster set piece.

### 4. Rederijkers / Landjuweel 1561

New active dossier: `REDERIJKERS_LANDJUWEEL_1561.md`.

Repairs:
- ordinary chamber evening is writable through composition, correction, rehearsal, refrein, `spel van sinne`, `esbattement`, blazon, travel/competition preparation and sociability;
- Nardusbloem/Zusterhuis/Magdalena context remains current;
- Cornelis membership stays fixed, office does not: deken open, factor/prince not canon;
- contemporary Silvius 1562 print anchors fourteen official Antwerp competitors.

Hard boundary:
- no current proof places a Goese chamber among the fourteen official competitors or prize winners;
- Claes/Cornelis may attend, observe and network fictionally;
- Dee remains absent from the 1561 story visit.

### 5. Antwerp time slices

New active dossier: `ANTWERP_TIME_SLICES_1561_1585.md`.

Required scene states:
- 1561 — city as theatre;
- 1563–early 1564 — city as book/workshop;
- 1566 — city as broken image;
- 1567–1569 — surveillance/repression;
- 1576–1578 — wound/rumour/print release;
- 1585 — transformed formative city.

This prevents one generic Antwerp ambience from spanning twenty-four years.

### 6. Schutterij / military practice

New active domain `WORLD.SCHUTTERIJ_MILITARY` and dossier `SCHUTTERIJ_MILITARY_PRACTICE_1550_1607.md`.

Repairs:
- explicit separation of schuttersgilde, broader civic defence, professional/garrison soldiers and later standardized drill;
- local footbow/handbow/firearm traditions exposed to scene building;
- the Edele Busse/Sint Adriaan start-date discrepancy (1516 versus 1530 in two local heritage sources) is preserved rather than silently resolved;
- Jacob de Gheyn's 1607 *Wapenhandelinghe* is a late comparator for standardized bodily sequence, not evidence of exact Goes 1572 drill.

Forbidden back-projection:
- later `twelve apostles`, musket fork, 1616/1624 costume and exact fire-rate claims cannot be imported automatically into 1572.

## Scene retrieval layer

`narrative/domain_scene_packs.yaml` now provides authoring packets for:
- youth bread/bakery context;
- Cornelis as biersteker;
- Reimerswaal school years;
- ordinary Goese Nardusbloem chamber;
- Antwerp Landjuweel observer context;
- six Antwerp time slices;
- Goese schutterij;
- De Gheyn 1607 late comparator.

A scene pack constrains a possible scene; it does not create a Narrative Instance or fictional presence by itself.

## Source-claim normalization

`claims/SOURCE_CLAIMS_DOMAIN_REBUILD_2026-08-16.yaml` stores the minimum atomic evidence/boundary claims required by the authoring layer, including:
- bakery default and bread assize;
- transferable hopped-beer process and biersteker role;
- Reimerswaal school continuity;
- Reimerswaal 1555–1561 material pressure;
- fourteen Antwerp Landjuweel chambers;
- non-established Goese official participation;
- divided print labour;
- Goese firearm-guild date conflict;
- De Gheyn 1607 publication/117-stepwise-image comparator.

## What Round B does NOT claim

- It does not close `OPEN.BAKERY.SCENE.001`.
- It does not decide a host family or exact school building in Reimerswaal.
- It does not make Cornelis a brewer, brewery owner, factor, prince or confirmed schutter officer.
- It does not make Goes an official 1561 Landjuweel competitor.
- It does not resolve the 1516/1530 Edele Busse dating conflict.
- It does not reconstruct exact 1572 firearm drill from 1607 evidence.
- It does not populate the novel's Book/Act/Sequence/Chapter/Beat architecture; that remains a later narrative-realization round.

## Next authoring boundary

After validation, these six domains count as **chapter-ready context**, not completed chapters. The next layer can safely build scenes/chapters on top of them without first re-researching basic craft, school, chamber, city-time or defence practice.