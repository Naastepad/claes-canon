# Goes wage provenance — 30 August 2026

**Status:** RESEARCH HANDOFF / NUMERIC GAP PRESERVED  
**PR:** #22 — `Add Goes economic baseline and war-economy resolver`  
**Resolver gap:** `GAP.ECON.GOES.WAGES.1540_1602`

## Result of this pass

The search for a genuinely **Goese** wage anchor has progressed, but it also produced an important correction.

Jan de Vries' labour-market chapter explicitly includes **Goes** among the western-Netherlands locations underlying its wage tables and gives the Goese source base as:

> `G.A. Goes, Rekeningen van de stad, no. 783-959; rekeningen stadsfabriek, no. 1813-14, 1793-97.`

However, a separate Zeeland repertory cites **GA Goes, Stad Goes, inv.nr. 784, fol. 25r** for an event in **1627**. Therefore the De Vries range cannot be assumed to be a Claes-period (1540-1602) account series. The earlier project wording that these inventory ranges were already a direct route to Claes-period numerical wages was too strong and has been corrected.

This evidence state is recorded in:

- `sources/SRC-SECONDARY-DEVRIES-LABOUR-MARKET-GOES-WAGES-001.md`;
- `claims/SOURCE_CLAIMS_GOES_WAGES_2026-08-30.yaml`.

## What is verified

- Goes is not merely inferred from a Holland or Zeeland average; De Vries explicitly uses Goese municipal material in his western wage compilation.
- The archive references he used are known.
- At least one inventory number at the start of the cited range, inv.nr. 784, is independently tied to 1627.
- Therefore the **chronological coverage of De Vries' Goese series must be established before it can be used for Claes**.

## New pre-1602 local route

The source search has now located archive families that demonstrably begin **inside Claes' lifetime**.

A nineteenth-century inventory of Goese guild papers reports for the **timmerliedengilde**:

- account books **1547-1798**;
- resolutions **1586-1798**;
- an ordinance book covering timmerlieden and related crafts including kuipers, stoeldraaiers, wannemakers, mandenmakers, wagenmakers and metselaars.

This is now the best dated local account-book route for the 1540s onward. Its existence does **not** prove that it contains day wages; gilde accounts can instead contain fees, fines, meals, property expenses, loans, ceremonial expenditure and other transactions.

The official Stad Goes archive description independently confirms the institutional route on the municipal side: finances were administered by annually elected rentmeesters from 1438, while public property/works were supervised through stadsdirecteuren and a stadsfabriek. Exact surviving pre-1602 payment volumes still need identification.

These routes are documented in:

- `sources/SRC-RESEARCH-GOES-LABOUR-ARCHIVE-PRE1602-2026-08-30.md`;
- `claims/SOURCE_CLAIMS_GOES_WAGES_2026-08-30.yaml`.

## Named extraction target: Anthonis Claesz

The user's local archival compilation `Levendale.pdf` identifies **Anthonis Claesz / Anthonis Claiszoon** as Goese **stadtimmerman**, with weeskamer-related references in 1567, 1580 and 1590. That makes him a particularly useful name target when pre-1602 city accounts, public-works records or acquittances are located.

The evidence does **not** tell us how he was remunerated. `stadtimmerman` might involve day work, an annual retainer, project payment, materials plus labour, or a mixed arrangement. No number may be inferred from the title.

Source record:

- `sources/SRC-SECONDARY-LEVENDale-GOES-NOTARIAL-COMPILATION-001.md`.

## What is still NOT verified

The project still does **not** possess a defensible statement such as:

> `a Goese skilled labourer earned X stuivers per day in year Y between 1540 and 1602`.

No exact Goese value may be generated from regional averaging, interpolation or narrative convenience.

`GAP.ECON.GOES.WAGES.1540_1602` therefore remains **OPEN / HIGH PRIORITY**.

## Mid-sixteenth-century regional comparators

De Vries' Table 1 gives direct 1550-1554 construction-wage observations in other cities. Two useful comparators are:

| Place | Skilled construction labour | Unskilled labour | Use |
| --- | ---: | ---: | --- |
| Bergen op Zoom | 5.5-6 stuivers/day | 3-4 stuivers/day | `C_REGIONAL_PROXY` |
| Antwerp | 9 stuivers/day | 4 stuivers/day | `C_REGIONAL_PROXY` |

These data are useful because they bracket plausible orders of magnitude in Claes' youth and demonstrate substantial city-to-city variation. They are **not** a reconstructed Goes range.

## Post-1570 regional comparator boundary

De Vries gives detailed nominal-wage steps for the Rijnland drainage works at Spaarndam/Halfweg. Craftsmen rise from 7 stuivers through 1565 to 9 in 1565, 12 (sometimes 15) in 1578, 14 in 1589, 16 in 1590 and 18 in 1593. Unskilled labour rises from 5 to 6 in 1565, to 9 by 1583 and eventually 14 by 1606.

These figures document the scale and chronology of western-Netherlands wage acceleration. They remain **regional comparator evidence**, never substituted Goese values.

## Construction-payment boundary

Late-sixteenth-century Goese notarial material already gives us useful construction economics — named timmerlieden and metselaars, valuations, building disputes and lump-sum contracts. These are useful for contract scale and craft practice, but a total contract sum is **not** a day wage unless the source supplies labour time/rate.

No project calculation may divide a lump sum by guessed working days and call the result a historical wage.

## Historical interpretation guardrails

1. Daily wage is not annual household income.
2. Nominal wage is not real wage or purchasing power.
3. A quoted day rate does not establish how many paid days a worker obtained.
4. Skilled, unskilled, seasonal, public-works and specialist rates must remain distinct.
5. In-kind food, drink, lodging or other allowances must not be silently converted into cash or ignored when a source specifies them.
6. The strong post-1570 regional wage movement cannot be projected backwards into Claes' 1540s-1550s youth.
7. A cited archive inventory range is not a date range; inventory-number chronology must be verified independently.
8. Account-book survival is not the same thing as a wage series.
9. `stadtimmerman` is an occupational/office identification, not a wage formula.
10. Lump-sum contract, piece rate, valuation and day wage remain separate evidence types.

## Next extraction target — corrected

Preferred order now is:

1. locate the **1547 onward timmerliedengilde account volume(s)** and obtain their current GAG inventory identifiers/scans;
2. identify dated pre-1602 rentmeester/stadswerken/stadsfabriek payment records in `NL-GsGA-1.1-001`;
3. search specifically for **Anthonis Claesz / Claiszoon**, `stadtimmerman`, and variants alongside `loon`, `daggeld`, `dachgelt`, `betaelt`, `dagen` and public-work terminology;
4. extract occupation/task, number of days, amount, money unit and any in-kind component exactly as written;
5. retain raw transcription before normalization;
6. classify payment form (`DAY_WAGE`, `PIECE_RATE`, `CONTRACT_TOTAL`, `RETAINER`, `MATERIALS_PLUS_LABOUR`, `UNKNOWN`);
7. only then construct direct Goese skilled/unskilled anchors or a series.

Recovering the original numeric De Vries Table 2 remains useful for later Goese wage history, but it is no longer treated as sufficient for the Claes-period gap until its local chronology is proven.

## HPW / `brenv.xls` parallel lead

The old IISH Historical Prices and Wages file `brenv.xls` is repeatedly cited in academic literature as Jan Luiten van Zanden's dataset *Prices and Wages and the Cost of Living in the Western Part of the Netherlands, 1450-1800*. The modern IISH HPW archive preserves legacy website files and a separate provenance CSV copied from the old HPW site.

The old `brenv.xls` mapping has not yet been recovered from the provenance CSV in this pass. Until the actual file, variables and place provenance are identified, values attributed to that workbook remain a research lead rather than a Goese fact layer.

## Validation

The initial PR validator failure was a YAML list/mapping syntax error in `narrative/economic_state_resolver.yaml`, not a historical/canon conflict. It was repaired in commit `d066a842e84ef67b5e24ad0f84859726376de477`.

Validation passed repeatedly after the correction; workflow run **357** passed on the branch after addition of the dedicated pre-1602 archive-route dossier. The Source Claim / named-target additions made after that run must receive their own final CI pass before merge review.

## Merge boundary

This handoff does not resolve `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001`, does not assign an exact Goese day wage, does not claim that De Vries' cited Goese accounts cover Claes' years, and does not convert regional wage series, guild accounts or contract totals into local day-wage observations.
