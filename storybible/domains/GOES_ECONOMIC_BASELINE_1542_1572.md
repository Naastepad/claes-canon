# Goes Economic Baseline 1542–1572

**World ID:** `WORLD.GOES_ECONOMY_1542_1572`  
**Status:** ACTIVE_AUTHORING_DOMAIN  
**Role:** economic/material scene-condition layer  
**Story authority:** subordinate to `canon/`, current Story Claims and `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001`

This dossier answers a narrow authoring question:

> **What economic language, measures, transactions and material pressures are safe to use when Claes is in or economically tied to Goes before the full war-economy fracture?**

It does not convert historical research into a new plot decision.

---

## 1. Governing method

Never translate a sixteenth-century amount directly into a modern euro figure as the primary meaning of the sum.

For authoring, economic meaning should be resolved as:

`amount -> accounting unit -> plausible physical money -> local measure -> local/period price -> wage-days or other contemporary purchasing-power anchor -> social position`

Every numerical statement should carry, internally, at least:

- year/date;
- place;
- commodity/service;
- historical unit;
- evidence grade;
- whether the value is direct, derived, interpolated or proxy;
- payment type where relevant: `DAY_WAGE`, `PIECE_RATE`, `FREIGHT_TARIFF`, `CONTRACT_TOTAL`, `RETAINER`, `CREDIT/DEBT`, `TAX/IMPOST`, `PRICE`.

### Source priority

1. same place + same/specific date;
2. local time series or local institution;
3. regional proxy with explicit label;
4. broader Low Countries context only.

No Amsterdam/Antwerp value becomes a `Goes` value merely because a Goese number is missing.

---

## 2. Accounting language is not the same as a purse of coins

For the Zeeland/Flemish accounting relation used in this layer:

- `1 pond Vlaams = 20 schellingen Vlaams = 240 groten Vlaams`;
- `1 pond Vlaams = 6 carolusguldens = 120 stuivers`;
- `1 schelling Vlaams = 12 groten = 6 stuivers`;
- `1 stuiver = 2 groten Vlaams`;
- `1 carolusgulden = 20 stuivers = 40 groten Vlaams`.

### Coin chronology relevant to Claes

- 1521: gold Carolusgulden at 20 stuivers.
- 1543: silver Carolusgulden at 20 stuivers / 40 groten Vlaams.
- 1557: Philipsdaalder at 30 stuivers.
- 1559: Philipsdaalder rated at 35 stuivers.
- 1579/1580: the same named coin is reported at 45 stuivers.

**Authoring consequence:** `three gulden` in an account does not automatically mean three physical silver Carolus pieces. A coin name also does not guarantee one timeless stuiver value.

Sources: `SRC-SECONDARY-BOONMAN-METROLOGY-2015-001`; claims `SC.HIST.COIN.CAROLUS.ACCOUNTING.1521_1543.001`, `SC.HIST.COIN.PHILIPSDAALDER.RATES.1557_1580.001`.

---

## 3. Goese grain measure

The safest period vocabulary is the historical measure first, litres second.

### Relations

- one Goese `viertel` is also called a sack/zak in the relevant comparison tradition;
- one sack/viertel = **2 achtendelen**.

### Source-sensitive volume

The 1572 Brussels comparison gives:

- `1 Goese achtendeel` ≈ **36.6 L** in Boonman's reconstruction.

A 1590 comparison and another transmitted relation yield larger reconstructed values, roughly **39.6–40.1 L** per achtendeel.

Therefore use:

> `1 Goese viertel/sack = 2 achtendelen`, with a rough sixteenth-century conversion range of **about 73–80 L** only when modern physical intuition is actually needed.

Do not write `79.2 litres` as though a merchant in 1560 knew or used that decimal metric quantity.

Claims: `SC.HIST.GOES.GRAIN_MEASURE.ACHTENDEEL.1572.001`, `SC.HIST.GOES.GRAIN_MEASURE.SOURCE_VARIATION.1590.001`.

---

## 4. A direct Goese transport micro-tariff — 1544

At the **1544 letting of the Goese schuitvlotten**, the transport charge described as `loon` for moving **one zeve grain** was fixed at **18 mijten**.

For Goes / Zeeland Bewesten Schelde the `zeve` is reconstructed as:

- **4 sacks of grain or flour**.

This is one of the strongest local Claes-period logistics anchors currently in the repository because date, place, commodity, unit and tariff type are all identifiable.

### Classification

`18 mijten per zeve = FREIGHT / TRANSPORT TARIFF`

It is **not**:

- a day wage;
- a porter day rate;
- proof that one man performed the movement;
- proof of how long the movement took;
- proof that the same rate applied to beer, salt or other goods.

The word `loon` in the source context therefore must not be normalized automatically to `dagloon`.

Claim: `SC.HIST.GOES.GRAIN_TRANSPORT.SCHUITVLOTTEN.1544.001`.

---

## 5. Later Goese rye prices show intra-year movement — 1595

The earlier shorthand in this dossier — one `1595 Goese rye price` — was too static. A direct cross-check of the local notarial transcription shows an **April/May/August sequence** that was attested later in 1595.

Lowijs Serwouters Jacobsz, grain buyer in Goes, checked his book and recalled:

- **April 1595:** one last `oosterschen rogghe` at **£26 Vlaams per last**;
- **May 1595:** rye at **14 schellingen 2 groten per sack**, equivalent in the attestation to **£26 11 schellingen 3 groten per last**;
- **around 17–18 August 1595:** one last rye at **£19 Vlaams per last**.

Pieter Jansz van Oosten, poorter, schepen and grain buyer of Goes, corroborated the April/May prices.

Primary route in the transcription: `RAZE 2040, fol. 109`, late October / early November 1595.

### Important correction

Boonman's metrological synthesis presents the 14s2g figure with a `31 October / fol. 110` locator. The fuller Levendale transcription shows that **14s2g is the May transaction remembered in the later attestation**, not a 31 October spot purchase.

The repository therefore preserves the source discrepancy but uses the direct transaction chronology for authoring.

### Narrative consequence

Do not treat a commodity price as a fixed annual constant. Even inside one year, the Goese rye evidence shows substantial movement.

Use this late-life evidence for:

- market volatility;
- timing of purchase;
- stockholding decisions;
- merchant memory/bookkeeping;
- the difference between `what rye costs` and `what this rye cost when bought`.

Never back-project any of these 1595 prices to 1554 or 1561.

Claim: `SC.HIST.GOES.RYE_PRICE.1595.001`.

---

## 6. Cornelis' professional economy — biersteker, not brewer

**Canon rule:** Cornelis is a **biersteker / beer merchant-distributor**. He is not canonically a brewer, recipe-maker or owner of the documented Nissepad brewery.

Load together with:

- `DEC.NISSEPAT.BREWERY.FAMILY_NETWORK.2026-08-16`;
- `DEC.CORNELIS.BEER.DISTRIBUTION_CHAIN.2026-08-16`;
- `WORLD.BEER_BREWING_DISTRIBUTION`;
- `PACK.BEER.GOES_BIERSTEKER`.

### Safe professional chain

A more complete author-side model is now:

`outside/local brewer -> freight -> cask loss/recovery -> steker remuneration/margin -> receipt at quay/store -> official measurement where applicable -> carrier/handling -> buyer/tapper -> credit/account settlement`

Not every transaction must contain every step, and the source does not prove that Cornelis personally performed all of them.

His material expertise is strongest around:

- cask count and condition;
- empty-cask return and loss;
- leakage;
- freight and route;
- storage;
- quantity and measure;
- accounts and obligations;
- buyer/supplier credit;
- whether delivery matches paperwork or expectation.

Do **not** move him into mash tun, hop recipe, fermentation control or brewhouse ownership unless a separate Story Decision explicitly does so.

### Distribution-cost evidence from Zeeland, 1574

In the 1574 Zeeuwse beer-impost dispute, source wording identifies three added cost classes for beer sold into Zeeland:

- loss of casks;
- freight (`vrachten`);
- remuneration of the stekers (`het traictement van heure stekers`).

Dirksen interprets the biersteker as a **Zeeuwse wholesale/distribution intermediary** who arranged distribution and received remuneration from the brewer.

This is strong support for the **professional mechanism** behind Cornelis' established role.

However, Dirksen then gives a worked example beginning `Stel dat`, using **10 stuivers per ton** for combined added costs. That number is hypothetical. It is **not** a historical steker fee or freight tariff and may never be used as one.

Also: this 1574 evidence postdates Cornelis and belongs to a wartime fiscal context. Use it to understand the occupational mechanism, not to create a 1574 Cornelis transaction.

Claim: `SC.HIST.ZEELAND.BEER.BIERSTEKER_DISTRIBUTION.1574.001`.

### Goese biermeter antecedent

Local Goese evidence before Claes' lifetime documents that beer in the city was measured when carried from the quay and that a poorter could not sell it before measurement by the sworn biermeter; poorters were not exempt from meetgeld.

This is strong evidence for a local institutional tradition, but the exact ordinance/tariff for 1542–1569 remains to be verified. Therefore:

- official measurement-before-sale: **SUPPORTED local continuity**;
- exact Claes-period tariff/wording: **OPEN RESEARCH**.

Claim: `SC.HIST.GOES.BEER.MEASUREMENT_ANTECEDENT.001`.

---

## 7. Carrying was an institutional urban economy

The official Goese craft-guild archive does not merely contain generic craft guilds. Its description identifies long-running occupational guilds for:

- **bierdragers**;
- **zakkedragers**.

Their stated archival date ranges span Claes' lifetime.

A Goese notarial record of **7 May 1591** additionally names two actual poorters:

- Cornelis Jacobsen Schipper — `bierdrager en poorter`;
- Adriaen Cornelis Faes — `schipper en bierdrager en poorter`.

That means `bierdrager` is safe as a real Goese occupational identity, not an invented generic dock labourer.

### Evidence boundary

We still do **not** have a Claes-period carrier tariff from the guild archive.

Do not infer from the occupational title:

- a day wage;
- a per-ton handling tariff;
- guild monopoly/exclusivity;
- number of carriers;
- whether every beer movement had to use a guild bierdrager;
- that `schipper` and `bierdrager` were mutually exclusive occupations.

Claims: `SC.HIST.GOES.LABOUR.CARRIER_GUILDS.CLAES_PERIOD.001`, `SC.HIST.GOES.BEER.BIERDRAGERS.1591.001`.

---

## 8. Credit, debt and surety belong to ordinary economic life

Cash payment at the instant of purchase should not dominate every scene.

A Goese notarial record of **14 June 1585** has Jan Pauwelsz Cuijper formally acknowledge **17 pond groten Vlaams** owed to Franchois Hertsinck for accumulated `verteringen` in Hertsinck's inn. His person and goods were bound as security.

Related material immediately afterwards concerns much larger fiscal debt, seizure and surety around an imposten-pachter from Nisse.

This supports an ordinary transaction world of:

`running account -> accumulated debt -> acknowledgement -> security/surety -> collection/enforcement`

For authoring, that permits historically grounded situations such as:

- a familiar customer being carried on account;
- a merchant waiting for settlement;
- a debt becoming formal only after it grows;
- goods/person/property becoming security;
- social trust turning into legal obligation.

### Boundary

The **17 pond** is accumulated debt. It is not the cost of one meal, one drinking session or one night in an inn.

Claim: `SC.HIST.GOES.CREDIT.HOSPITALITY_DEBT.1585.001`.

---

## 9. Beer impost and biersteker must remain separate roles

A March **1593** South-Beveland attestation gives a useful nearby mechanism:

- Jan Jacobsz Bom appears as `impostmeester van de bieren` for the quarter of 's-Heer Hendrikskinderen, Wissenkerke and 's-Heer Arendskerke;
- a separate transaction identifies Michiel Horen as `biersteker`, supplying five tons of `dobbelbier` for a wedding.

This demonstrates that beer distribution and beer-impost administration could coexist as **different functions** in the same regional economy.

It does **not** prove:

- a city-Goes impost rate;
- that the biersteker was always the statutory taxpayer;
- that the five-ton wedding supply incurred a specific unquoted charge;
- that 1593 rules can be moved back unchanged to Cornelis' 1540s–1560s trade.

Claim: `SC.HIST.SOUTH_BEVELAND.BEER.IMPOST_BIERSTEKER.1593.001`.

---

## 10. Salt economy around Claes' childhood

Salt is not decorative background in Goes. It is a major material and labour system.

### 1546 piecework anchor

The Goese salt-workers' ordinance of **14 September 1546** is reported to pay seven men **4 groten each** for carrying, filling and lifting one `honderd grof zout`.

This is **piecework**, not `4 groten per day`.

Claim: `SC.HIST.GOES.SALT.LABOUR_PIECE_RATE.1546.001`.

### Production / regulation

Boonman identifies:

- salt-refining ordinances of 28 June 1551 and 6 April 1563;
- a large Goese salt sector around 1569, including roughly 100 salt pans, while the exact printed production unit `ton(?)` remains uncertain;
- destruction of all Goese saltworks during the 1572 siege, with production later recovering below its former capacity.

For the Nissepat family, keep the separate story/fire canon intact: the 1554 family salt interest can be lost without implying that Goes ceased to be a salt town in 1554.

---

## 11. Ordinary fiscal life existed before Alva

Do not write the 1569 Tiende-Penning crisis as if early-modern Goese commerce had previously been tax-free.

Merchants and householders already inhabit a world of:

- tolls;
- market and measurement rights;
- excises/imposts in changing forms;
- weigh/measure fees;
- property/land burdens;
- extraordinary demands/bedes;
- route-specific charges.

The authoring question is therefore not `tax or no tax`, but:

> **which authority, which commodity, which tax point, which date, which jurisdiction and who is legally liable?**

Exact pre-1572 Goese tariffs remain local-source questions and should not be imported from the 1734–1739 Goese economy page.

The 1593 South-Beveland beer-impost evidence reinforces the institutional logic, but is not itself a 1550s Goese tariff.

---

## 12. Historical measures are part of trust and conflict

Measurement is civic authority, not merely arithmetic.

A transaction can involve:

- an official measure/slaper;
- a sworn measurer;
- a market fee;
- suspicion of short measure;
- different place measures for physically similar quantities;
- conversion at a port or market;
- a contract expressed in one unit and delivered in another.

This is especially useful for Claes because his practical intelligence can observe discrepancies without the prose turning into a textbook.

The narrative function is concrete:

> what does the mark/measure/account **claim**, and what does the material delivery actually contain?

Do not turn that author-side resonance into a repeated explanatory slogan in prose.

---

## 13. The unresolved Goese wage and carrier-tariff series

The major numerical labour gap remains:

> **the annual/periodic Goese civilian wage series ca. 1540–1602.**

The carrier research also leaves a narrower gap:

> **exact Claes-period bierdrager/zakkedrager handling tariffs and remuneration rules.**

We now know that:

- the carrier guilds existed in Goes;
- named bierdragers occur in 1591;
- a Goese grain-transport tariff exists in 1544;

but those three facts are not interchangeable.

Until direct account/ordinance entries are extracted:

- do not state an Amsterdam, Haarlem, Antwerp or Bergen-op-Zoom wage as the Goese wage;
- do not turn `18 mijten per zeve` into a porter day wage;
- do not invent a beer-carrier tariff from the grain tariff;
- do not infer a bierdrager tariff from a bierdrager occupational title;
- regional figures may be used only as explicitly marked comparison ranges;
- the 1546 salt piece rate remains piecework, not a substitute day wage;
- military soldij is not a civilian wage.

**Research status:** `HIGH_PRIORITY_NUMERIC_GAP`.

---

## 14. Scene-use matrix

| Situation | Safe economic texture | Avoid |
|---|---|---|
| Household 1547–1554 | cask/food stock, small purchases, measured goods, running credit, work rhythm | invented exact shopping basket |
| Cornelis trade | receipt, freight, quantity, leakage, cask return/loss, storage, carrier, debt/account, official measure | brewing him personally; invented steker tariff |
| Market/haven | bierdragers/zakkedragers as real occupations, mixed coins, measures, transport charges | converting occupation into unverified wage/rate |
| Grain movement 1544 | `zeve`, sacks, schuitvlotten, 18-mijten transport tariff | calling 18 mijten a day wage or applying it to beer |
| Salt world | piecework, pans/keten, heavy movement, heat, measures, risk | converting piece rate to day wage |
| 1554 fire aftermath | destroyed stock/claims/tools/papers/income streams where canon supports | declaring all Nissepat economic capacity destroyed |
| Reimerswaal transition | changed place measures/routes and cost of maintaining a pupil | assuming Goes prices transfer unchanged |
| Late Goes 1585–1595 | running debt, formal acknowledgement/surety, volatile rye prices, merchant books | treating one debt as a retail price or one price as annual constant |

---

## 15. Hard guardrails

1. Cornelis = biersteker/distributor, **not brewer**.
2. The documented Nissepad brewery is not automatically Cornelis' property.
3. Account unit ≠ physical coin.
4. Coin name ≠ timeless stuiver value.
5. `Viertel`, `achtendeel`, `zeve`, `hoed`, `last`, `ton`, `pond` etc. are place/time dependent.
6. Never convert the 1546 salt piece rate into a daily wage.
7. `18 mijten per zeve` in 1544 is a Goese grain-transport tariff, not a day wage and not a beer tariff.
8. A `bierdrager` occupational identification proves no rate, day wage, monopoly or headcount.
9. The May 1595 `14 schellingen 2 groten per sack` rye price is not an October spot price.
10. Never use any 1595 rye price as a 1554 or 1561 price.
11. Dirksen's `10 stuivers per ton` distribution-cost example begins `Stel dat`; it is **hypothetical**, never a historical tariff.
12. The 1593 South-Beveland beer-impost evidence is not automatically a city-Goes tariff or a Claes-period rule.
13. An accumulated tavern debt is not the unit price of a meal, drink or lodging.
14. Never back-project 1730s Goese taxes/office practice as exact 1550s rules.
15. No modern-euro equivalence as primary authoring logic.
16. Missing Goese wages/carrier tariffs remain missing until extracted; do not hide the gap with a proxy.

---

## 16. Linked evidence

- `claims/SOURCE_CLAIMS_ECONOMY_2026-08-30.yaml`
- `claims/SOURCE_CLAIMS_GOES_WAGES_2026-08-30.yaml`
- `sources/SRC-SECONDARY-BOONMAN-METROLOGY-2015-001.md`
- `sources/SRC-SECONDARY-LEVENDale-GOES-NOTARIAL-COMPILATION-001.md`
- `sources/SRC-SECONDARY-DIRKSEN-GEZAG-GELD-ZEELAND-2012-001.md`
- `sources/SRC-ARCHIVE-GOES-AMBACHTSGILDEN-520-001.md`
- `sources/SRC-HIST-BEER-LOWCOUNTRIES-GOES-001.md`
- `sources/SRC-RESEARCH-GOES-SALTWORK-FIRE-1554-2026-08-21.md`
- `storybible/domains/BEER_BREWING_BEERSTEKER_1540_1580.md`
- `storybible/domains/BREAD_GRAIN_BAKING_1540_1602.md`

The baseline is an authoring constraint layer. It does not create a scene, transaction, property ownership or financial loss by itself.
