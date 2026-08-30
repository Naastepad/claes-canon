# De Hont shipping provenance review — 2026-08-30

## Scope

Research target: make Aernouldt de Hont scene-ready without converting a single 1589 mention into invented biography.

Questions tested:

1. What exactly does the 2 May 1589 Horen–De Hont act say?
2. What vessel type is defensible for authoring?
3. What cargo scale is locally demonstrated?
4. What can be said about route duration?
5. What can be said about freight and cargo risk?

## 1. Material correction to the prior interpretation

The consulted Levendale extract of `RAZE 2039, fol. 86, 2-5-1589` is headed as a biersteker agreement and says, in substance, that **Michiel Horen will be biersteker for beers that Aernouldt de Hont brings to Goes**.

Therefore the research layer must not describe the historical act as if it proved:

`Horen owns cargo -> Horen hires De Hont as freight carrier`.

The supported topology is only:

`De Hont brings beer -> Horen is biersteker for that beer -> omitted conditions`

Because the extract does not reproduce the conditions, beer ownership, freight payer, commission, exclusivity and risk allocation all remain OPEN.

This correction has been propagated into:

- source claim `SC.HIST.GOES.HOREN_DE_HONT.BEER_CONTRACT.1589.001`;
- the legacy-reference claim `SC.HIST.GOES.BIERSTEKER.SHIPPER_CONTRACT.1589.001`, whose ID is retained for reference stability but whose semantics are corrected;
- `entities/DE_HONT_HOREN_TRADE_CONTINUITY_2026-08-30.yaml`;
- `claims/STORY_CLAIMS_DE_HONT_HOREN_2026-08-30.yaml`;
- `canon/DECISIONS_CORNELIS_DE_HONT_HOREN_CONTINUITY_2026-08-30.yaml`;
- `canon/DECISIONS_CORNELIS_ECONOMIC_POSITION_2026-08-30.yaml`;
- `storybible/domains/CORNELIS_DE_HONT_HOREN_TRADE_CONTINUITY_1550_1589.md`;
- `storybible/domains/CORNELIS_ECONOMIC_POSITION_1542_1568.md`;
- `review/MIGRATION_REVIEW_SUPPLEMENT_DE_HONT_HOREN_2026-08-30.yaml`.

A final semantic diff audit was run specifically because the continuity validator cannot detect a historically reversed business relation expressed in otherwise valid YAML. Four stale residues from the earlier interpretation were harmonized.

## 2. Vessel type evidence ladder

### De Hont-specific

No vessel type, name, rig, capacity or ownership has been recovered. `schipper van Delft` is the only De Hont-specific vessel-role evidence.

### Strong period analogues

- **1582 Schiedam/Overschie:** newly launched `kromstevenschuit`, described as 3 last.
- **1586 Scheldt near Catshoeck:** `schip ofte crabschuijte` carrying willow planting material; capsized in a squall.
- **1594 Remmerswaal connection:** final instalment and ironwork for a newly built kromstevenschuit linked to Joost Engelsz Mol, son of the bailiff of Remmerswaal.

### Near-contemporary corridor analogues

- **1608:** Delfshaven skipper sells a kromsteven schuit to a Goese skipper.
- **1609:** Delfshaven skipper present in Goes acknowledges debt for purchase/delivery of a crabbeschuyt.

### Review conclusion

Do **not** canonize an exact De Hont ship.

Authoring default:

`generic small/medium shallow-water cargo schuit`

Kromsteven and krabschuit are legitimate visual/mechanical analogues. They become fictional type choices only when a scene needs that specificity; they remain non-biographical with respect to De Hont.

## 3. Beer-cargo scale

Direct local evidence is unusually strong.

`RAZE 2039, fol. 80, 11-4-1589` records Goese schipper Jan de Wulf taking **52 tons English beer** as freight from a Veere skipper's vessel at the head of Goes, to carry onward to Zierikzee.

This proves that a single regional beer movement in the **dozens of tons/casks** belongs inside the real 1589 Goese freight system.

It does not prove De Hont's capacity.

For research visualization only, Alberts reports a Holland beer ton around 1590 of about 154 L. Mechanical multiplication would place 52 Holland-scale tons around 8,008 L. But the same study says the Delft beer ton was smaller than the Amsterdam ton in 1578, so the litre result is not an exact conversion for Delft/Goese cargo.

Authoring rule: retain `tonnen bier` in prose/research claims; use litre estimates only to help visualize mass and space.

## 4. Delft beer distribution mechanism

The wider mechanism is well supported even though De Hont's personal route is not.

- Heenvliet archival-description material for the 1540s describes small schuiten used for inland navigation and a frequently sailed Delft route because local beer came largely from Delft breweries.
- The 1612 Dutch Guicciardini edition states Delft beer was carried particularly to Zeeland; an explicitly marked addition describes regional bierstekers.
- Goese RAZE 2043 extracts from 1609 show Delft beer in the South-Beveland market through named bierstekers, credit/debt, ton-by-ton sales, and Delft-brewer links to Goese shipping/agency for debt collection.

Chronology guardrail: Guicciardini's consulted Dutch text is the expanded 1612 edition; do not date the marked addition to the 1567 original without edition comparison. RAZE 2043 is outside Claes' 1602 endpoint and is mechanism-comparator evidence only.

## 5. Route duration

No direct sixteenth-century Delft–Goes or Goes–Antwerp duration for De Hont was recovered.

What is supported is the operational logic of water transport: tide windows, shallow water, wind, waiting, loading/transshipment and weather disruption.

Therefore:

- **do not assign a fixed hour count**;
- scene time should be expressed in tides and days;
- a missed tide, waiting for wind/water, or a day's delay is authorially safer than a pseudo-precise timetable;
- Antwerp remains a fictionally allowed Cornelis route but still lacks a De Hont-specific duration source.

## 6. Risk

### Operational risk: supported

- 1586 crabschuijt capsized in a squall on the Scheldt;
- 1589 beer was transshipped between vessels at Goes;
- 1608 near-contemporary Goese sailing accident shows a vessel capsizing on the Goes–Arnemuiden leg;
- credit, obligations and debt collection occur throughout the trade evidence.

### Contractual allocation: OPEN

The 1589 Horen–De Hont extract omits its conditions. It therefore cannot presently answer who bore:

- cargo loss;
- leakage/spoilage;
- cask-return loss;
- freight cost;
- delayed-payment risk;
- pre-arrival ownership risk.

Do not import a later maritime-law rule as though it were the recovered 1589 agreement.

## Bottom-line authoring model

Use this when writing Cornelis/De Hont:

`ordinary legitimate regional trade -> schuit-family vessel -> tens-of-casks scale possible -> tide/weather constrained -> role separation between shipper and biersteker -> credit and cask obligations -> exact contract/risk terms scene-specific fiction unless sourced`

This gives De Hont material reality without false precision.

## Validation

After the semantic harmonization pass, the Claes canon repository validation completed successfully. PR #22 remains draft and unmerged for author review.
