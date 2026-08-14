# SRC-HIST-GOES-LIVING-CITY-001 — Goes living-city evidence bundle

**Type:** composite historical/reconstruction source bundle  
**Status:** research provenance; individual claims retain their own evidence status  
**Scope:** Goes and immediate southern/western approaches, chiefly 1533–1580, with later transport records used only for continuity checks.

## Primary research data

1. `RAZE-1745-1760-master-1533-1675.xlsx` — normalized transport-register corpus, RAZE 1745–1760. The workbook records 9,912 normalized acts, one object/property mention per act, four belending fields, parties, dates, object descriptions and location strings. The Nisse/Nissepat selection contains 196 relevant mentions, including 99 direct Nissepat/Nissepadt person mentions.
2. `goes-georeconstructie-audit-v2.json` — audit of the transport-derived topology: 9,912 acts, 8,085 ownership chains, 39,648 boundary relations, 753 fixed/dynamic anchors and 99 objects classified as not geographically placeable. Its own warning is binding: the reconstruction is topological/schematic and ownership or adjacency does not automatically prove residence.
3. Revision 11 Storybible, conversion-ledger sections `SB.SEC.018` (Goes topography/timeline), `SB.SEC.019` (Nissepad reconstruction) and `SB.SEC.021` (historical Nissepat family). Unatomized detail remains source material until separately normalized.

## Historical/topographic support

- Jacob van Deventer, sixteenth-century Goes town plan, used for orientation, wall/haven form and durable street relationships; not a cadastral parcel map.
- RCE / Atlas Leefomgeving, `Nederland in 1575`, used as georeferenced historical geometry and in combination with the modern reference layer for durable street-name crosswalks. Modern names are anchors, not automatic proof that name and micro-trace were identical in 1542.
- Brandweer Goes, `Stadsbrand van Goes` (`https://www.brandweer-goes.nl/uitrukken/stadsbrand-goes-1554/`): specialized local reconstruction of the 18 May 1554 fire. It places the salt works outside the walls on the **north side of the harbour**, gives a total harbour-zone inventory of **81 salt pans/keten**, identifies the origin as one Oostzelke salt pan, records a strong north-easterly wind and names Turfkade, the watermill and the Kruisbroeders complex as destroyed. It cites Gemeentearchief Goes, C. Dekker's *Een schamele Landstede*, R.A.S. Piccardt and Zeeuwse Ankers among its bases.
- Brandweer Goes, `De brandweer in Goes tot de 19e eeuw` (`https://www.brandweer-goes.nl/historie/1405-1799/`): local synthesis of the 1459 fire ordinance, compulsory household response, ladders/emmer chains and the practice of pulling down buildings to create stop-lines. It also distinguishes the 1555 salt-pan fire and the 1572 military destruction from the 1554 city fire.
- Zeeuwse Ankers, `Brand!` (`https://www.zeeuwseankers.nl/verhaal/brand`): states that the 1554 fire began in a salt pan in the north-east harbour/industrial area, spread to neighbouring salt pans and then to the city, with a hard wind driving the fire westward and the Turfkade houses being destroyed; gives roughly one quarter of the then building stock as lost.
- Zeeuwse Ankers, `Zoutzieden` (`https://www.zeeuwseankers.nl/verhaal/zoutzieden`): explicitly places the relevant Goese salt pans **north of the city** and explains why salt works were commonly outside the walls.
- Erfgoed van Goes, monument/property histories such as `Turfkade 9: De Rijke Bruineman` (`https://erfgoedvangoes.nl/turfkade-9-de-rijke-bruineman/`), used only where an individual site history independently confirms destruction/rebuilding after 1554.
- `Boekje Goese vesten 600 jaar` for the 1572 siege: strongest pressure at the 's-Heer Hendrikskinderenpoort and Havenpoort; outside salt works burned; a brewery in the Voorstad burned; Mondragón relieved the city in October.
- Separate church evidence is normalized in `SRC-HIST-GOES-GROTEKERK-001` and must be used for the Maria Magdalenakerk interior and confessional chronology.
- The old/pre-1594 Nieuwstraat problem is further normalized in `SRC-HIST-GOES-NIEUWSTRAAT-001`: transport acts establish the older toponym, later records connect Oude Nieuwstraat and Armenhoek, while the exact 1542 axis remains unknown.
- Goese rederijker meeting chronology is further normalized in `SRC-HIST-GOES-REDERIJKERS-001`.

### Modern fire-behaviour analogue — not historical evidence for Goes

For scene blocking only, the reconstruction may use modern fire-science results to test whether a wind-driven multi-front fire is physically plausible. These sources **do not establish what happened at a particular Goese house or at a particular minute**:

- S. Manzello & S. Suzuki, `Initial study on thatched roofing assembly ignition vulnerabilities to firebrand showers`, *Fire Safety Journal* 103 (2018), NIST record: `https://www.nist.gov/publications/initial-study-thatched-roofing-assembly-ignition-vulnerabilities-firebrand-showers`. Firebrands penetrated thatched roofing, sometimes invisibly from outside, under 3–6 m/s test winds and could produce rapid flame penetration.
- NIST summary, `A Fire-Breathing Dragon Helps Fight Ember Attacks on Thatched-Roof Buildings` (`https://www.nist.gov/news-events/news/2018/12/fire-breathing-dragon-helps-fight-ember-attacks-thatched-roof-buildings`), useful only as a demonstrator that a continuous wind-driven firebrand shower can ignite vulnerable roofing ahead of a main flame front.
- Manzello & Suzuki, `Exposing Decking Assemblies to Continuous Wind-Driven Firebrand Showers` (2014), NIST record: `https://www.nist.gov/publications/exposing-decking-assemblies-continuous-wind-driven-firebrand-showers`, supporting the general mechanism of accumulated wind-driven firebrands causing separate flaming ignitions.

The valid inference is therefore qualitative: once several wooden structures burn under a strong wind, a **brandwaaier / spotting pattern with multiple secondary ignitions** is more realistic than a single neat street-by-street flame front. Exact Goese speeds, ember distances and ignition minutes remain unknown.

## Key transport anchors used in this normalization

- `RAZE-1745-0031`, 18-05-1534: Claes Jacopsen Nissepat sells a house at Noordeinde; east Frans Blauhuus, south/west Kruisbroeders, north dike.
- `RAZE-1745-0365`, 03-02-1540: Claes Jacopsen Nissepat sells house and land by the Nissepad; east seller, south Jan Adriaensen Stevensen, west zoekweg, north road. The eastern boundary therefore preserves adjoining property of the seller at that moment.
- `RAZE-1746-0044`, 16-05-1541: Claes Jacobsen sells house/homestead `inde Nissepat in Hubelamshoek`; identification with Claes Jacobsz. Nissepat is possible but not proven.
- `RAZE-1746-0153`, 20-03-1542: Claes Jacopsen Nissepat buys a house in a `Nieuwstraat`; street on the east and Jacob Dierixsen de Bye on north, west and south. The house is therefore on the west side of the historical street. The pre-1594 street/toponym is treated at zone level as the older Nieuwstraat/Oude Nieuwstraat in or by the Armenhoek, explicitly distinct from the planmatige/current Nieuwstraat of the 1594 expansion; the exact old street axis remains unknown.
- `RAZE-1746-0290`, 24-09-1543: house and hof outside the Gansepoort, showing inhabited/built southern approach.
- `RAZE-1746-0291`, 24-09-1543: salt pan at Westzelke bounded on multiple sides by the city harbour.
- Multiple 1530s–1540s acts place Oostzelke salt pans against harbour, dike, street and neighbouring owners; Westzelke acts likewise place salt pans directly against the harbour. This corroborates a dense two-bank harbour-industrial environment rather than a detached southern industrial field.
- `RAZE-1748-0638`, 17-01-1558: house `bij de stadsschool in het Schuttershofstraatje`; this fixes a city-school anchor by 1558 but does not itself prove identical location in 1542.
- `RAZE-1749-0505` and `RAZE-1749-0512`, May/June 1568: Claes Piersen Nissepat buys and then sells a Noordeinde house with Kruisbroeders as western boundary and Frans Blauhuys north, showing later Nissepat presence in the same northern-western urban fabric.
- `RAZE-1750-0361`, 15-01-1577: brewery at Nissepad, east path, south Jan Pauwelsen, west Pieter den Hollander, north road.
- `RAZE-1750-0399`, 12-05-1577: Jan Jansen Nissepat sells the place of a burned salt pan `tgemeen keetge` at Westzelke; east harbour, south NN Jopsen, west/north Jasper Borselair.
- `RAZE-1750-0411` and `RAZE-1750-0431`, 16-06 and 30-09-1577: Nissepad brewery with kettles, tubs/vats and tools transferred to Lambrecht de brouwer; east common footpath, south Jan Pauwelsen, west Pieter den Hollander, north road.
- `RAZE-1750-0549` and `RAZE-1750-0629`, 1579: `den Hooren` / Nissepat-linked house cluster at the Vismarkt/Lange Vorststraat area; useful for family/property-network continuity, not proof of Cornelis' residence.

## Event evidence used

### Fire of 18 May 1554

#### Fixed geography and supported event footprint

The salt industry relevant to the fire lay **north of the walled city along the harbour**, not south of Goes. Oostzelke and Westzelke are treated as the industrial zones on the harbour sides, with the exact pre-fire position of individual keten unresolved. Brandweer Goes gives 81 keten in the harbour zone; that is the total industrial inventory, **not a claim that all 81 burned in 1554**.

Current evidence supports a fire beginning in one unidentified salt pan on the Oostzelke. It spread to surrounding buildings and neighbouring salt works and, under a strong north-easterly wind, reached the city. The supported event layer includes the Oostzelke origin zone, harbour-side salt-industry cluster, complete destruction along Turfkade in the cited reconstruction, burned watermill, burned Kruisbroeders complex, Westzelke access/harbour-edge damage and a broad northern/western damage zone. The current source-weighted scale is roughly one quarter of city/harbour building stock affected. Exact damage to most individual transport parcels is unknown and must not be fabricated.

#### Reconstructed spread pattern

The source-supported sequence is:

**Oostzelke salt pan → neighbouring salt/harbour structures → wind-driven sparks/firebrands toward west and south-west → multiple harbour/city ignitions → Turfkade / north-western harbour edge → watermill/Molenwater zone → Kruisbroeders/western urban fabric.**

This is **not** treated as one tidy linear route. Once several structures are burning, modern fire science makes it physically plausible that wind-driven embers create spot fires ahead of the main flame front, so different roofs can begin to smoke or burn while intermediate buildings remain temporarily intact. That mechanism is a reconstruction aid, not direct evidence for the ignition order of any named 1554 house.

The Opril is useful as a later recovery/damage marker because post-fire records and rebuilding tradition show burned/rebuilt property there, but the present source set does not justify treating the Opril as a meter-exact terminal fire line.

#### Scene-blocking speed model — inference only

No surviving source in the present bundle gives minute-by-minute fire positions. For prose blocking, the following order-of-magnitude model is acceptable **only when labelled reconstruction**:

- **T+0–10 min:** first Oostzelke keten becomes a developed building fire;
- **T+5–30 min:** neighbouring industrial buildings/keten become involved and begin producing substantial wind-driven firebrands;
- **T+20–60 min:** secondary roof/building ignitions can plausibly appear around the harbour and northern urban edge; Turfkade becomes part of the major fire field;
- **T+45–120 min:** separate fire pockets may merge around the inner harbour, watermill/Molenwater and north-western blocks;
- **T+1–3 h:** destructive expansion can plausibly reach the Kruisbroeders/western fabric while many individual buildings continue to burn for much longer.

These bands are **not historical timestamps** and must never be quoted as archival fact. Their function is to prevent a dramatically false depiction in which the fire either crosses Goes in seconds or advances as one slow wall for an entire day.

#### Human casualties

The consulted fire-specific sources describe date, origin, wind, material damage and rebuilding but supply **no reliable number of dead or injured** for the 18 May 1554 fire. The current research bundle therefore records the human toll as **UNKNOWN**. Absence of a number is not evidence of zero deaths, but neither is a general statement about deaths in early-modern city fires evidence that deaths occurred in this specific Goese fire. Any named fatality in the novel is authorial fiction unless a separate historical source is found.

#### Cornelis household and the fictional house

In novel canon the older-Nieuwstraat/Armenhoek house is the Cornelis household's childhood residence, but current historical evidence does not prove that this parcel burned. The strongest scene reconstruction is therefore **spot-fire exposure without total destruction**: smoke, falling ash/firebrands, a locally ignited roof edge, outbuilding or stored material can be fought while the main dwelling survives. This is plausible because wind-driven firebrands can create isolated ignitions ahead of a major front and because the Armenhoek residence is not inside a parcel-level confirmed total-loss record.

If the novel makes Claes' mother a fatal casualty, that must remain a separate author decision. Within the present geography, a death **in the heavily affected harbour/Turfkade/Kruisbroeders corridor, or after re-entering that corridor**, is more defensible than a death caused by total destruction of the family home while that home simultaneously survives. A later death from burns, smoke inhalation or collapse injury is also physically plausible, but is not historical evidence about the real 1554 casualty pattern.

### Siege of 1572
The source bundle distinguishes this from 1554. During the siege the salt works outside the walls were burned for military reasons; a brewery in the Voorstad also burned. The 's-Heer Hendrikskinderenpoort and Havenpoort took the strongest pressure. The city was not captured; Mondragón relieved it in October. Later property sales may be post-war liquidation or ordinary transfer unless the act explicitly proves execution/confiscation.

## Methodological guardrails

- `OWNS`, `SELLS`, `BUYS`, `ADJOINS`, `OPERATES_BUSINESS` and `RESIDES` are different relations. Never infer residence from ownership, adjacency or a business location. The Cornelis household relation to the 1542 house exists only because it has been separately established as novel canon.
- Four belendingen support topology and street-side reasoning; they do not create an exact cadastral polygon.
- Transport chains across 1533–1675 are not automatically simultaneous physical parcels. Repeated ownership chains may refer to the same physical place through time.
- Modern street names and RCE geometry are reference anchors. Historical continuity must be recorded separately.
- The pre-1594 `Nieuwstraat` is resolved only at historical-name/zone level as the older Nieuwstraat/Oude Nieuwstraat in or by the Armenhoek. It must never be snapped to the post-1594 planned/current Nieuwstraat, and no exact 1542 axis may be invented.
- Family filters are secondary overlays. All non-family residents, craftsmen, institutions and businesses remain part of the living-city background.
- Fire-science analogues may test physical plausibility but may not be promoted into exact historical timing, firebrand range, roof material or casualty claims for Goes without separate historical evidence.
