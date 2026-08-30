# Goes wage provenance — 30 August 2026

**Status:** RESEARCH HANDOFF / NUMERIC GAP PRESERVED  
**PR:** #22 — `Add Goes economic baseline and war-economy resolver`  
**Resolver gap:** `GAP.ECON.GOES.WAGES.1540_1602`

## Result of this pass

The search for a genuinely **Goese** wage anchor has progressed from a generic regional proxy problem to an exact archival provenance problem.

Jan de Vries' labour-market chapter explicitly includes **Goes** among the western-Netherlands locations underlying its wage tables and gives the Goese source base as:

> `G.A. Goes, Rekeningen van de stad, no. 783-959; rekeningen stadsfabriek, no. 1813-14, 1793-97.`

This is now recorded in:

- `sources/SRC-SECONDARY-DEVRIES-LABOUR-MARKET-GOES-WAGES-001.md`;
- `claims/SOURCE_CLAIMS_GOES_WAGES_2026-08-30.yaml`.

## What is verified

- Goes is not merely being inferred from a Holland or Zeeland average; it is explicitly one of the wage-data locations in De Vries' source apparatus.
- The municipal account ranges used for the Goese evidence are now known precisely enough for a targeted archive/table extraction pass.
- The source family is compatible with public/construction/manual-labour wage evidence rather than an invented general `average wage` for all inhabitants.

## What is still NOT verified

The currently accessible text transcription does not expose the numeric Goese row of the relevant De Vries table in readable form. Consequently the project still does **not** possess a defensible statement such as:

> `a Goese skilled labourer earned X stuivers per day in year Y`.

No such value may be generated from a regional average, interpolation or narrative convenience.

`GAP.ECON.GOES.WAGES.1540_1602` therefore remains **OPEN / HIGH PRIORITY**.

## Regional comparator boundary

De Vries gives usable detailed nominal-wage steps for the Rijnland drainage works at Spaarndam/Halfweg. Those data document the scale and chronology of western-Netherlands wage acceleration after the 1560s/1570s.

They are valuable for:

- order-of-magnitude checking;
- detecting impossible Goese reconstructions when local values are later recovered;
- understanding the broader labour-market pressure surrounding the Revolt.

They are **not** a Goese wage series and must remain `C_REGIONAL_PROXY`/comparator evidence.

## Historical interpretation guardrails

1. Daily wage is not annual household income.
2. Nominal wage is not real wage or purchasing power.
3. A quoted day rate does not establish how many paid days a worker obtained.
4. Skilled, unskilled, seasonal, public-works and specialist rates must remain distinct.
5. In-kind food, drink, lodging or other allowances must not be silently converted into cash or ignored when a source specifies them.
6. The strong post-1570 regional wage movement cannot be projected backwards into Claes' 1540s–1550s youth.

## Next extraction target

Preferred order:

1. recover the original numeric De Vries Table 2 representation if available in a scan/data supplement;
2. identify which Goese account numbers cover the Claes-relevant years;
3. extract dated wage observations with occupation/task, amount, unit and any in-kind component;
4. retain the raw transcription before normalisation;
5. only then construct a Goese skilled/unskilled wage series or bounded anchors.

## HPW / `brenv.xls` parallel lead

The old IISH Historical Prices and Wages file `brenv.xls` is repeatedly cited in academic literature as Jan Luiten van Zanden's dataset *Prices and Wages and the Cost of Living in the Western Part of the Netherlands, 1450–1800*. The modern IISH HPW archive explicitly preserves legacy website files and a separate provenance CSV copied from the defunct HPW site.

The old `brenv.xls` mapping has not yet been recovered from the provenance CSV in this pass. Until the actual file and variable provenance are identified, values attributed to that old workbook remain a research lead rather than a new Goese fact layer.

## Validation

The initial PR validator failure was a YAML list/mapping syntax error in `narrative/economic_state_resolver.yaml`, not a historical/canon conflict. It was repaired in commit `d066a842e84ef67b5e24ad0f84859726376de477`.

Repository validation subsequently passed in workflow run **348**, and after adding the Goese wage-provenance claim/source it passed again in workflow run **350**.

## Merge boundary

This handoff does not resolve `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001`, does not assign an exact Goese day wage, and does not convert a regional wage series into a local one.
