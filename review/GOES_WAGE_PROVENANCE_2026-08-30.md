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

## What is still NOT verified

The project still does **not** possess a defensible statement such as:

> `a Goese skilled labourer earned X stuivers per day in year Y between 1540 and 1602`.

The accessible De Vries transcription does not expose a readable Goese Table 2 row, and the cited account range is not yet demonstrated to cover the Claes years.

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

These figures document the scale and chronology of western-Netherlands wage acceleration. They are useful for:

- order-of-magnitude checking;
- detecting impossible later Goese reconstructions;
- understanding broader labour-market pressure surrounding the Revolt.

They remain **regional comparator evidence**, never substituted Goese values.

## Historical interpretation guardrails

1. Daily wage is not annual household income.
2. Nominal wage is not real wage or purchasing power.
3. A quoted day rate does not establish how many paid days a worker obtained.
4. Skilled, unskilled, seasonal, public-works and specialist rates must remain distinct.
5. In-kind food, drink, lodging or other allowances must not be silently converted into cash or ignored when a source specifies them.
6. The strong post-1570 regional wage movement cannot be projected backwards into Claes' 1540s-1550s youth.
7. A cited archive inventory range is not a date range; inventory-number chronology must be verified independently.

## Next extraction target — corrected

Preferred order now is:

1. obtain or reconstruct the dated inventory mapping for **NL-GsGA, Archief Stad Goes, toegang 001** around the municipal-account/fabricage series;
2. identify which surviving Goese accounts actually cover **1540-1602**;
3. search those pre-1602 records for wages/daygeld/dachgelt, timmerlieden, metselaars, opperlieden, arbeiders, gravers, dragers and public works;
4. extract dated observations with occupation/task, amount, historical money unit and any in-kind component;
5. retain raw transcription before normalization;
6. only then construct direct Goese skilled/unskilled anchors or a series.

Recovering the original numeric De Vries Table 2 remains useful for later Goese wage history, but it is no longer treated as sufficient for the Claes-period gap until its local chronology is proven.

## HPW / `brenv.xls` parallel lead

The old IISH Historical Prices and Wages file `brenv.xls` is repeatedly cited in academic literature as Jan Luiten van Zanden's dataset *Prices and Wages and the Cost of Living in the Western Part of the Netherlands, 1450-1800*. The modern IISH HPW archive preserves legacy website files and a separate provenance CSV copied from the old HPW site.

The old `brenv.xls` mapping has not yet been recovered from the provenance CSV in this pass. Until the actual file, variables and place provenance are identified, values attributed to that workbook remain a research lead rather than a Goese fact layer.

## Validation

The initial PR validator failure was a YAML list/mapping syntax error in `narrative/economic_state_resolver.yaml`, not a historical/canon conflict. It was repaired in commit `d066a842e84ef67b5e24ad0f84859726376de477`.

Validation subsequently passed in runs 348, 350 and, after the mid-sixteenth-century comparator additions, **353**. The archive-coverage correction above must also pass CI before the PR can again be described as green at its current head.

## Merge boundary

This handoff does not resolve `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001`, does not assign an exact Goese day wage, does not claim that De Vries' cited Goese accounts cover Claes' years, and does not convert regional wage series into local ones.
