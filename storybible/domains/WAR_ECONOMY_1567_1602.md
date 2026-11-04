# War Economy 1567–1602

**World ID:** `WORLD.WAR_ECONOMY_1567_1602`  
**Status:** ACTIVE_AUTHORING_DOMAIN  
**Role:** political-control / fiscal / monetary / supply modifier  
**Story authority:** context only; never closes Story Claims or `OPEN.*` decisions by itself

This dossier prevents a common historical-writing error: treating `war` as one generic economic condition.

From 1567 onward, the correct question is:

> **Where is the person, who controls that place, what route/transaction is involved, and which fiscal/monetary rules are actually in force there on that date?**

---

## 1. Resolver principle

Apply war-economy information in this order:

1. resolve **date**;
2. resolve **place**;
3. resolve **political control / jurisdiction**;
4. resolve **transaction type and commodity**;
5. resolve **military/siege condition**;
6. only then apply tax, coin, licent, convoy, confiscation-risk or emergency-money rules.

A province name is not enough.

The critical example is Zeeland 1572–1576: Goes/Zuid-Beveland remained under landsheerlijk authority while rebel Zeeland developed separate fiscal institutions. Therefore `Zeeland + 1574` does not resolve one economic state.

Claim: `SC.HIST.ZEELAND.POLITICAL_CONTROL.DIVIDED_1572_1576.001`.

---

## 2. State W1 — repression and network risk, 1567–1569

### Historical condition

Alva's regime intensifies prosecution, surveillance, arrest and punitive authority. Economic consequences can include:

- a trading partner disappearing or fleeing;
- borg/surety and legal costs;
- seizure/confiscation risk where a sentence or authority supports it;
- disrupted credit and unpaid obligations;
- inventories, papers and routes becoming evidence;
- military presence and billeting/provisioning burdens.

### Cornelis boundary

Cornelis' first arrest/examination in 1567 and final execution in 1569 are **fiction canon** embedded in a historically grounded repression ecology. His specific property consequences are not automatically historical facts.

Do not infer:

- confiscation of the Nissepad brewery;
- confiscation of a family salt property;
- loss of every debt/claim;
- a specific fine or tax payment;

unless a separate Story Decision fixes it.

### Military-pay context

For royal infantry, an academic synthesis gives a nominal ordinary soldij of about **4–5 stuivers/day**, alongside obligations concerning food, lodging, fire and light. Actual payment could be irregular.

Use this as military economic context, never as the Goese civilian wage.

Claim: `SC.HIST.MILITARY.ROYAL_INFANTRY_PAY.1567_1600.001`.

---

## 3. State W2 — Alva tax crisis, 1569–early 1572

### Fiscal project

Alva's March 1569 project:

- Honderdste Penning: one-time 1% on possessions;
- Twintigste Penning: 5% on sale of immovable goods;
- Tiende Penning: 10% on sale of movable goods;
- additional proposed 10% export levy;
- 10th and 20th intended as permanent.

Claim: `SC.HIST.ALVA.TAX_PROJECT.1569.001`.

### Implementation is not binary

Do **not** turn the project into `all sales paid 10% from 1569`.

Alva reported on 31 October 1569 that the 10th/20th demand on merchandise had for six years been converted into an annual lump-sum arrangement under negotiation. In Zeeland renewed plakkaten remained contested into March 1572.

The safe story-world signals are therefore:

- announcement/plakkaat;
- merchants calculating possible effects;
- negotiation/afkoop;
- local collectors/receiver apparatus;
- uncertainty over liability;
- anger that a repeated transaction tax could bite into commerce;
- conflict between central demand, States and city implementation.

For an actual paid tax in prose, require local/date/transaction evidence.

Claim: `SC.HIST.ALVA.TAX_IMPLEMENTATION_BOUNDARY.1569_1572.001`.

---

## 4. State W3 — divided Zeeland, 1572–1576

### Political split

At the Pacificatie, Dirksen describes:

- Walcheren, Schouwen, Duiveland and Sommelsdijk in the rebel Zeeland connection;
- Zuid-Beveland and Tholen as territories that had remained under landsheerlijk authority.

Goes is on Zuid-Beveland.

**Hard rule:** rebel fiscal and coin rules do not automatically apply to Goes before its 1577 satisfaction merely because both are `Zeeland`.

### 4.1 Rebel Zeeland — licentrecht

Dirksen describes licentrecht as a permission fee. Early revolt usage includes:

- permission under war-law/passport logic to trade or sail where capture/confiscation would otherwise threaten;
- permission to export goods despite a prohibition designed to protect supply or deny goods to the enemy.

In rebel Zeeland licentrecht appears from **1573**.

Exact route, tariff, commodity, exemption and passport remain specific questions.

Claim: `SC.HIST.ZEELAND.REBEL.LICENT_CONVOY.1573_1576.001`.

### 4.2 Convoygeld

Dirksen explicitly states that convoygeld was introduced in Zeeland only in **1576**.

Do not back-project the later mature Republic-wide convoy/licent system into 1572 Zeeland without the early chronology.

### 4.3 Four stuivers per ton beer

In rebel Zeeland a levy of **4 stuivers per ton beer** is demonstrable from 1 May 1574, intended for ammunition finance.

Liability described by Dirksen:

- domestic brewers on production;
- beer imported from outside Holland and Zeeland.

This is **not** a generic 4-stuiver charge on every biersteker sale.

It is particularly important for Cornelis continuity that:

- Cornelis is a biersteker, not brewer;
- Cornelis is already dead in 1574;
- Goes is not then in the rebel Zeeland fiscal regime.

Claim: `SC.HIST.ZEELAND.REBEL.BEER_AMMUNITION_LEVY.1574.001`.

### 4.4 Supply disruption

War can make price and availability diverge from normal-market assumptions through:

- blockade;
- export ban;
- capture risk;
- requisition/provisioning;
- destroyed production/storage;
- route closure;
- changed destination legality.

Apply a specific mechanism only when the route/date supports it.

For Goes, the 1572 destruction of saltworks is already a historically grounded local material shock. This domain does not decide which Nissepat interest is lost.

---

## 5. Coin intervention — the `klop`

### Holland 1573

A specialist numismatic source records a Holland plakkaat of **7 February 1573** under which qualifying coins were countermarked and accepted at higher official rates. The difference functioned as an interest-free loan for war finance.

A cited example:

- rijksdaalder old rate: 32 stuivers;
- after countermark/contribution: official rate 36 stuivers;
- contribution in that example: 4 stuivers.

Claim: `SC.HIST.COIN.KLOP.HOLLAND.1573.001`.

### Rebel Zeeland 1573–1574

A related countermark intervention is supported, but the exact local chronology/implementation is less uniform in the evidence currently ingested.

Claim: `SC.HIST.COIN.KLOP.ZEELAND_REBEL.1573_1574.001`.

### Hard guardrail

Never resolve:

`location = Goes, year = 1573 -> rebel klop`

by province name alone.

The political-control resolver blocks that inference.

---

## 6. Emergency money — only a siege-city override

Rijksmuseum evidence shows that prolonged siege could produce a shortage of circulating cash and lead a city to create temporary money so soldiers and suppliers could still be paid. Leiden 1574 preserves metal and paper emergency issues, including a 28-stuiver paper issue.

The authoring rule is strict:

`war = true` **does not** imply `emergency money = true`.

Emergency money requires a supported city-specific issue / siege state.

Never move a Leiden, Haarlem, Middelburg, Zierikzee or other city's emergency issue into a different city because the dates are convenient.

Claim: `SC.HIST.NOODMONEY.SIEGE_SPECIFIC.1570S.001`.

---

## 7. State W4 — 1577–1579 settlement and legal afterlife

This period is especially important because visible destruction can be over while economic destruction continues through paperwork.

Possible historically grounded mechanisms include:

- old debts becoming collectable or uncollectable;
- rent/interest arrears;
- supplier/customer claims;
- inheritance and family division;
- damaged property that still has a legal owner;
- rebuilding costs;
- sale/transfer to settle obligations;
- uncertain or delayed payment;
- changed confessional/political networks;
- re-entry of a place into a different governing structure.

### Critical Storybible boundary

The exact Claes chain remains **OPEN** under:

`OPEN.GOES.CLAES_DEPARTURE_1572_1579.001`.

This dossier may supply mechanisms to test but may not choose among them.

In particular:

- do not identify the burned 1572 Voorstad brewery with the documented 1577 Nissepad brewery;
- do not call a 1577–1579 transfer a confiscation or forced sale without evidence;
- do not make the documented Nissepad brewery Cornelis' property;
- do not assign the destruction date of the Westzelke salt-pan site without evidence.

The strongest current authorial research hypothesis is **cumulative consequence** rather than one unsupported melodramatic asset loss, but that remains a hypothesis until the author resolves the open hinge.

---

## 8. State W5 — provincial money and prolonged war, 1579–1585

By this point monetary geography has changed further. The key authoring principles are:

- province/city minting and rated values require date-specific checking;
- older/foreign coins can remain in circulation;
- named coin value can shift;
- account money and physical coin remain distinct;
- military and commercial routes remain vulnerable to political boundaries.

The Philipsdaalder example is useful: its reported stuiver rate changes during Claes' life. Do not treat its name as a fixed purchasing-power unit.

For exact Zeeland/Holland coin pools, add local numismatic claims before writing a counted handful of named coins.

---

## 9. State W6 — 1585–1593 northern war economy

After 1585, Claes' northern commercial environment belongs to a different trade and political system than childhood Goes.

Safe general pressures:

- altered Antwerp/northern trade routes;
- continued military expenditure;
- transport and customs/licent boundaries;
- migration of people/capital/skills;
- changing nominal wages/prices;
- demand created by armies, fleets and fortification as well as destruction caused by war.

Do not use seventeenth-century war-profit studies as direct proof for a specific Claes-period contract. Treat them as questions to source earlier.

---

## 10. State W7 — 1594–1602: annual price-series window

The IISG Historical Prices and Wages archive contains Netherlands tabular series for:

- bread, from 1594;
- rye/wheat, from 1594.

This overlaps the final nine years of Claes' story life through 1602.

Claim: `SC.HIST.IISG.NL_PRICE_SERIES.1594_1602.001`.

### Important data rule

The IISG archive is heterogeneous legacy material, not one harmonized dataset. Before using any annual number, audit:

- original place/spatial scope;
- unit;
- commodity specification;
- currency;
- provenance;
- transformation/interpolation status.

Only then may the resolver provide a late-life price anchor.

---

## 11. Confiscation / seizure rule

`confiscation_risk` and `specific_confiscation` are different states.

Repression and war make confiscation historically real, but a scene may state a particular house, cask stock, debt claim, book bundle or family asset was confiscated only if supported by:

1. historical evidence for that object/person; or
2. an explicit fictional Story Decision.

The resolver may output:

`confiscation_risk: elevated`

but it may never transform that automatically into:

`Nissepat property: confiscated`.

---

## 12. Soldier pay / provisioning authoring rule

Nominal royal infantry pay: roughly **4–5 stuivers/day** in the consulted military-economic synthesis.

But the scene-relevant state also requires:

- paid or in arrears?;
- lodged where?;
- food bought, requisitioned or supplied?;
- service/lodging money involved?;
- rank/unit/nationality?;
- royal, rebel or States force?;

A hungry unpaid soldier with a nominal wage is economically different from a worker paid cash at day-end.

---

## 13. Period-state table

| ID | Window | Dominant authoring modifier |
|---|---|---|
| W1 | 1567–1569 | repression, borg, network/asset risk |
| W2 | 1569–early 1572 | Alva tax crisis; threat/negotiation/collection uncertainty |
| W3 | 1572–1576 | jurisdiction split, siege/blockade, rebel versus royal fiscal rules |
| W4 | 1577–1579 | settlement, debts/claims/property/legal afterlife |
| W5 | 1579–1585 | provincial money/rates + continued war |
| W6 | 1585–1593 | transformed northern trade/war economy |
| W7 | 1594–1602 | late war economy + auditable annual Netherlands price series |

These states **overlap local baselines**; they do not replace them.

Example:

`Goes 1574 = local Goes baseline + landsheerlijk-control war modifier`, not `generic Zeeland 1574`.

---

## 14. Hard guardrails

1. Resolve political control before tax/coin rule.
2. Tiende-Penning proposal ≠ proven individual payment.
3. Rebel Zeeland rules ≠ royalist Goes rules.
4. Licentrecht is route/permission specific.
5. Zeeland convoygeld: not before 1576 in the current Dirksen evidence.
6. Four-stuiver beer levy is production/import based in rebel Zeeland, not a generic biersteker sales tax.
7. `klop` is political-zone/date specific.
8. Emergency money is city/siege specific.
9. Confiscation risk ≠ specific confiscation.
10. Nominal soldij ≠ cash actually received.
11. IISG late prices require provenance/unit audit before numerical use.
12. Do not close the 1572–1579 Goes departure hinge from this dossier.

---

## 15. Linked evidence

- `claims/SOURCE_CLAIMS_ECONOMY_2026-08-30.yaml`
- `sources/SRC-SECONDARY-DIRKSEN-GEZAG-GELD-ZEELAND-2012-001.md`
- `sources/SRC-HIST-ALVA-TAXATION-1569-1572-001.md`
- `sources/SRC-HIST-REVOLT-COINAGE-EMERGENCY-MONEY-1573-1576-001.md`
- `sources/SRC-HIST-MILITARY-PAY-LOWCOUNTRIES-1567-1700-001.md`
- `sources/SRC-IISG-HISTORICAL-PRICES-WAGES-2023-001.md`
- `sources/SRC-RESEARCH-WEB-ECONOMY-2026-08-30.md`
- `narrative/goes_departure_1572_1579.yaml`

This is a world-state modifier, not a plot generator.
