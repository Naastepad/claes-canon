# Goes wage provenance — 30 August 2026

**Status:** RESEARCH HANDOFF / NUMERIC GAP PRESERVED  
**PR:** #22 — `Add Goes economic baseline and war-economy resolver`  
**Resolver gap:** `GAP.ECON.GOES.WAGES.1540_1602`

## Result

The search for a genuinely **Goese** wage anchor has produced a reliable local extraction route, but still no defensible exact Goese civil day wage for 1540–1602. The gap therefore remains open rather than being filled with a regional estimate.

## 1. De Vries — useful provenance, wrong to treat as Claes-period coverage without dating

Jan de Vries explicitly includes **Goes** among the western-Netherlands wage locations and cites:

> `G.A. Goes, Rekeningen van de stad, no. 783-959; rekeningen stadsfabriek, no. 1813-14, 1793-97.`

An independent source, however, cites `Stad Goes, inv.nr. 784` for **1627**. Inventory number is therefore not a proxy for Claes-period chronology. De Vries proves Goese wage material existed in his compilation; his cited range may not be described as a 1540–1602 series until its dates are mapped.

Recorded in:
- `sources/SRC-SECONDARY-DEVRIES-LABOUR-MARKET-GOES-WAGES-001.md`;
- `claims/SOURCE_CLAIMS_GOES_WAGES_2026-08-30.yaml`.

## 2. Official current guild archive access

GOES Publiek now supplies the current official access:

- **archive:** `520 Ambachtsgilden Goes en schuttersgilden "De Edele Busse" en "De Edele Voetboog"`;
- **access:** `NL-GsGA-16.1-520`;
- **date range:** 1429–1798;
- **accessibility:** fully public.

The official description identifies the timmerliedengilde among the principal Goese guilds and lists its craft scope: timmerlieden, scheepstimmerlieden, stoeldraaiers, wagenmakers, schrijnwerkers, kuipers, metselaars, mandenmakers, strodekkers and schaliedekkers. It also notes separate craft representatives such as a metselaarsdeken and that guild officers inspected work, workshops and knecht numbers.

Source:
- `sources/SRC-ARCHIVE-GOES-AMBACHTSGILDEN-520-001.md`.

## 3. The pre-1602 account-book route is real

A historical inventory of the Goese guild archive reports for the **timmerliedengilde**:

- account books **1547–1798**;
- resolutions **1586–1798**;
- an ordinance book covering timmerlieden and related crafts including metselaars and kuipers.

The official access 520 confirms that this guild archive is extant and public. The historical inventory supplies the explicit 1547 account-book start date.

What is still missing is the **current placement-list item/inventory number for the earliest 1547 volume**. The searchable official archive description does not expose that item number. It is therefore left OPEN rather than guessed.

Sources:
- `sources/SRC-PUBLIC-GOES-GUILD-ARCHIVE-INVENTORY-1829-001.md`;
- `sources/SRC-ARCHIVE-GOES-AMBACHTSGILDEN-520-001.md`;
- `sources/SRC-RESEARCH-GOES-LABOUR-ARCHIVE-PRE1602-2026-08-30.md`.

## 4. Municipal public-works route

The official Stad Goes archive description states that finances were administered by annually elected rentmeesters from 1438, while public property and works were supervised by stadsdirecteuren with a stadsfabriek for daily management.

This establishes the right institutional source family for public labour payments, but not a surviving continuous pre-1602 wage series.

Source:
- `sources/SRC-ARCHIVE-GOES-STAD-001.md`.

## 5. Named extraction target — Anthonis Claesz

The local archival compilation `Levendale.pdf` identifies **Anthonis Claesz / Anthonis Claiszoon** as Goese **stadtimmerman**, with weeskamer-related references in **1567, 1580 and 1590**.

He is therefore a high-value name target when the pre-1602 municipal payment records are reached.

This evidence does **not** establish how he was paid. `stadtimmerman` can denote an office/role without telling us whether payment was a retainer, day rate, project sum, materials-plus-labour arrangement or combination.

Source:
- `sources/SRC-SECONDARY-LEVENDale-GOES-NOTARIAL-COMPILATION-001.md`.

## 6. What is not a day wage

The consulted Goese notarial material contains useful construction economics — named timmerlieden and metselaars, building contracts, arbitrations and valuations — but these payment types remain separate:

- `DAY_WAGE`
- `PIECE_RATE`
- `CONTRACT_TOTAL`
- `RETAINER`
- `MATERIALS_PLUS_LABOUR`
- `VALUATION`
- `UNKNOWN`

A lump-sum contract may never be divided by guessed working days to manufacture a historical day wage.

## 7. Regional comparators — calibration only

De Vries gives direct 1550–1554 construction/manual-labour comparators:

| Place | Skilled | Unskilled | Status |
| --- | ---: | ---: | --- |
| Bergen op Zoom | 5.5–6 st./day | 3–4 st./day | `C_REGIONAL_PROXY` |
| Antwerp | 9 st./day | 4 st./day | `C_REGIONAL_PROXY` |

A separate cultural-history study gives around 1550 a Holland summer wage for a timmerman/metselaar of roughly 7–8 stuivers/day and Haarlem 9–10; again this is contextual comparison, not Goes.

These figures may be used to reject implausible reconstructions. They may not be averaged into a synthetic `Goes = X`.

## 8. Extraction protocol

Next direct archival pass:

1. identify the current placement-list item for the timmerliedengilde account book beginning 1547 inside `NL-GsGA-16.1-520`;
2. identify dated pre-1602 rentmeester/public-works payment volumes inside `NL-GsGA-1.1-001`;
3. search `Anthonis Claesz`, `Anthonis Claiszoon`, `stadtimmerman`, `timmerman`, `metselaer`, `knecht`, `arbeider`, `loon`, `daggeld`, `dachgelt`, `sdaechs`, `betaelt`, `dagen` and task vocabulary;
4. transcribe the raw entry before normalization;
5. record exact date/account year, access, inventory/item, folio, occupation, task, number of days, amount/unit and in-kind components;
6. classify payment form;
7. only promote a value to `A_DIRECT` when the source actually supports the daily rate.

## 9. Current state of the gap

`GAP.ECON.GOES.WAGES.1540_1602 = OPEN / HIGH`

This is now a **source-access gap**, not a methodological gap. We know where the local evidence should be sought; the remaining work is item-level archival extraction.

## 10. Validation

The original PR CI failure was only a YAML list/mapping syntax error and was repaired in commit `d066a842e84ef67b5e24ad0f84859726376de477`.

The branch has subsequently passed repository validation repeatedly. Workflow run **363** passed after grounding the pre-1602 labour-source claims in direct public source records. A final CI check is still required after any later commit before merge review.

## Merge boundary

This handoff:

- does not assign an exact Goese day wage;
- does not treat account-book survival as a wage observation;
- does not treat De Vries' inventory range as Claes-period without dated mapping;
- does not convert regional comparators to Goes;
- does not resolve `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001`;
- does not infer any Nissepat property loss, confiscation or transaction.
