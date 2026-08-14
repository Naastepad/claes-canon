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
- Zeeuwse Ankers / Erfgoed van Goes material on Goes fortifications, urban development, harbour, church and the 1554 fire.
- `Boekje Goese vesten 600 jaar` for the 1572 siege: strongest pressure at the 's-Heer Hendrikskinderenpoort and Havenpoort; outside salt works burned; a brewery in the Voorstad burned; Mondragón relieved the city in October.
- Separate church evidence is normalized in `SRC-HIST-GOES-GROTEKERK-001` and must be used for the Maria Magdalenakerk interior and confessional chronology.

## Key transport anchors used in this normalization

- `RAZE-1745-0031`, 18-05-1534: Claes Jacopsen Nissepat sells a house at Noordeinde; east Frans Blauhuus, south/west Kruisbroeders, north dike.
- `RAZE-1745-0365`, 03-02-1540: Claes Jacopsen Nissepat sells house and land by the Nissepad; east seller, south Jan Adriaensen Stevensen, west zoekweg, north road. The eastern boundary therefore preserves adjoining property of the seller at that moment.
- `RAZE-1746-0044`, 16-05-1541: Claes Jacobsen sells house/homestead `inde Nissepat in Hubelamshoek`; identification with Claes Jacobsz. Nissepat is possible but not proven.
- `RAZE-1746-0153`, 20-03-1542: Claes Jacopsen Nissepat buys a house in a `Nieuwstraat`; street on the east and Jacob Dierixsen de Bye on north, west and south. This cannot safely be equated with the planmatige Nieuwstraat whose aanleg was decided in 1594; it requires a separate pre-1594 street anchor.
- `RAZE-1746-0290`, 24-09-1543: house and hof outside the Gansepoort, showing inhabited/built southern approach.
- `RAZE-1746-0291`, 24-09-1543: salt pan at Westzelke bounded on multiple sides by the city harbour.
- `RAZE-1748-0638`, 17-01-1558: house `bij de stadsschool in het Schuttershofstraatje`; this fixes a city-school anchor by 1558 but does not itself prove identical location in 1542.
- `RAZE-1749-0505` and `RAZE-1749-0512`, May/June 1568: Claes Piersen Nissepat buys and then sells a Noordeinde house with Kruisbroeders as western boundary and Frans Blauhuys north, showing later Nissepat presence in the same northern-western urban fabric.
- `RAZE-1750-0361`, 15-01-1577: brewery at Nissepad, east path, south Jan Pauwelsen, west Pieter den Hollander, north road.
- `RAZE-1750-0399`, 12-05-1577: Jan Jansen Nissepat sells the place of a burned salt pan `tgemeen keetge` at Westzelke; east harbour, south NN Jopsen, west/north Jasper Borselair.
- `RAZE-1750-0411` and `RAZE-1750-0431`, 16-06 and 30-09-1577: Nissepad brewery with kettles, tubs/vats and tools transferred to Lambrecht de brouwer; east common footpath, south Jan Pauwelsen, west Pieter den Hollander, north road.
- `RAZE-1750-0549` and `RAZE-1750-0629`, 1579: `den Hooren` / Nissepat-linked house cluster at the Vismarkt/Lange Vorststraat area; useful for family/property-network continuity, not proof of Cornelis' residence.

## Event evidence used

### Fire of 18 May 1554
Current evidence supports a fire beginning in one unidentified salt pan on the Oostzelke, driven by strong north-easterly wind through the harbour toward northern/western Goes. The supported event layer includes the Oostzelke origin zone, harbour-side salt-industry cluster, complete destruction along Turfkade in the cited fire reconstruction, burned watermill, burned Kruisbroeders complex, loss of the wooden Westzelke access, and a broad northern/western damage zone. The current synthesis estimates roughly one quarter of city/harbour building stock affected. Exact damage to most individual transport parcels is unknown and must not be fabricated.

### Siege of 1572
The source bundle distinguishes this from 1554. During the siege the salt works outside the walls were burned for military reasons; a brewery in the Voorstad also burned. The 's-Heer Hendrikskinderenpoort and Havenpoort took the strongest pressure. The city was not captured; Mondragón relieved it in October. Later property sales may be post-war liquidation or ordinary transfer unless the act explicitly proves execution/confiscation.

## Methodological guardrails

- `OWNS`, `SELLS`, `BUYS`, `ADJOINS`, `OPERATES_BUSINESS` and `RESIDES` are different relations. Never infer residence from ownership, adjacency or a business location.
- Four belendingen support topology and street-side reasoning; they do not create an exact cadastral polygon.
- Transport chains across 1533–1675 are not automatically simultaneous physical parcels. Repeated ownership chains may refer to the same physical place through time.
- Modern street names and RCE geometry are reference anchors. Historical continuity must be recorded separately.
- The pre-1594 `Nieuwstraat` is an unresolved historical location identity and must never be snapped to the post-1594 planned Nieuwstraat merely because the normalized name matches.
- Family filters are secondary overlays. All non-family residents, craftsmen, institutions and businesses remain part of the living-city background.
