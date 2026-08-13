# Claes Canon — AI Repository Manifest

**Purpose:** single bootstrap entrypoint for AI systems that can open raw GitHub files but cannot discover repository paths reliably.

**Repository:** `Naastepad/claes-canon`  
**Active branch:** `authoring/v1`  
**Raw base:** `https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/`

## Mandatory bootstrap order

1. Read this manifest.
2. Read `AI_ONBOARDING.md`.
3. Read the active operating master: `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md`.
4. Read the task-relevant modules listed below.
5. If drafting or revising literary prose, also read `WRITING_PROTOCOL.md`.
6. If changing canon, schemas, repository structure or deterministic Lemma, also read `AUTHORING_POLICY.md`, `AGENTS.md` and `REPOSITORY_INTEGRITY.md`.

**Never infer a repository path from a neighbouring filename. Use the exact raw URLs in this manifest.**

## Authority order

1. explicit current author decisions in `canon/` / `DEC.*`;
2. active synchronized `STC.*` Story Claims;
3. synchronized entity/object/narrative registers;
4. active operating Storybible master;
5. historical/source claims and provenance;
6. proposals/open questions;
7. chat memory — never authoritative.

---

# Core repository instructions

## AI onboarding
Path: `AI_ONBOARDING.md`  
Role: cross-model operating instructions  
Use when: always, before canon-sensitive work  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/AI_ONBOARDING.md

## Claude-specific entrypoint
Path: `CLAUDE.md`  
Role: Claude-specific thin entrypoint  
Use when: Claude is working in the project  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/CLAUDE.md

## Repository integrity
Path: `REPOSITORY_INTEGRITY.md`  
Role: concurrency, fresh-fetch, no silent overwrite, no force-history rules  
Use when: any write-capable AI changes repository content  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/REPOSITORY_INTEGRITY.md

## Writing protocol
Path: `WRITING_PROTOCOL.md`  
Role: prose drafting/revision protocol and scene-contract rules  
Use when: writing or revising chapters/scenes  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/WRITING_PROTOCOL.md

## Authoring policy
Path: `AUTHORING_POLICY.md`  
Role: canon-authoring and promotion rules  
Use when: changing canon or structured claims  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/AUTHORING_POLICY.md

## Agent rules
Path: `AGENTS.md`  
Role: cross-agent operational rules  
Use when: modifying structured canon, schemas or Lemma  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/AGENTS.md

---

# Storybible entrypoints

## ACTIVE operating master
Path: `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md`  
Role: current human-readable operating master  
Authority: ACTIVE AUTHORING MASTER  
Use when: any canon-sensitive story, character, theme, chronology or worldbuilding task  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/storybible/LEMMA_MCKEE_MASTER_2026-08-13.md

## Storybible index
Path: `storybible/INDEX.md`  
Role: storybible navigation  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/storybible/INDEX.md

## Historical substrate integration
Path: `storybible/modules/HISTORICAL_SUBSTRATE_1540_1605.md`  
Role: links historical chronology to scene-world consequences without creating fictional Claes actions  
Use when: setting any scene between 1540 and 1605  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/storybible/modules/HISTORICAL_SUBSTRATE_1540_1605.md

---

# Goes — Maria Magdalenakerk

For any scene in the Goese Maria Magdalenakerk, read **all three** of the following plus the broader sensory-church module.

## Local Goes church evidence
Path: `storybible/modules/WORLD_GOES_CHURCH_LOCAL.md`  
Role: local architecture, Zeven Getijden, music, guild materiality, local open questions  
Authority: LOCAL HISTORICAL EVIDENCE  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/storybible/modules/WORLD_GOES_CHURCH_LOCAL.md

## Liturgical/sensory guardrails
Path: `storybible/modules/WORLD_GOES_CHURCH_LITURGICAL_GUARDRAILS.md`  
Role: comparative late-medieval practice; seating, movement, soundscape, elevation, silence rhythm, exterior bell caution  
Authority: COMPARATIVE; local uncertainty remains marked  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/storybible/modules/WORLD_GOES_CHURCH_LITURGICAL_GUARDRAILS.md

## Explicit integration/precedence link
Path: `storybible/modules/HISTORICAL_SUBSTRATE_GOES_CHURCH_LINK.md`  
Role: tells an AI which Goes church modules must be combined and establishes local-evidence precedence  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/storybible/modules/HISTORICAL_SUBSTRATE_GOES_CHURCH_LINK.md

## Broader sensory religious-space model
Path: `narrative/religious_space_sensory_church.yaml`  
ID: `WORLD.RELIGIOUS_SPACE.SENSORY_CHURCH`  
Role: sinne, sensory church, guilds/confraternities, social topography, ritual movement and memory architecture  
Authority: Antwerp-direct where documented; comparative for Goes/Reimerswaal unless locally verified  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/narrative/religious_space_sensory_church.yaml

## Goes religious transition 1577–1578
Path: `storybible/modules/GOES_RELIGIOUS_TRANSITION_1577_1578.md`  
Role: local confessional/political transition  
Use when: Goes scenes in 1577–1578 or later memory of that transition  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/storybible/modules/GOES_RELIGIOUS_TRANSITION_1577_1578.md

---

# Revolt, information and identity

## Public opinion, rumour and identity
Path: `storybible/modules/PUBLIC_OPINION_IDENTITY_REVOLT.md`  
Role: oral-news ecology, rumour verification, confession versus allegiance, rederijkers as public-language infrastructure, layered identity  
Use when: political/religious information, rumours, propaganda, allegiance or identity matter  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/storybible/modules/PUBLIC_OPINION_IDENTITY_REVOLT.md

---

# Historical chronology

## Human-readable Low Countries chronology
Path: `history/LOW_COUNTRIES_TRANSFORMATION_1540_1605.md`  
Role: readable historical spine 1540–1605  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/history/LOW_COUNTRIES_TRANSFORMATION_1540_1605.md

## Machine-readable Low Countries chronology
Path: `history/LOW_COUNTRIES_TRANSFORMATION_1540_1605.yaml`  
Role: structured historical events, status and scene relevance  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/history/LOW_COUNTRIES_TRANSFORMATION_1540_1605.yaml

## Zeeland Revolt chronology
Path: `history/ZEELAND_REVOLT_TIMELINE.yaml`  
Role: regional Zeeland layer for Goes, Reimerswaal, Middelburg, Vlissingen, Veere, Zierikzee, Hulst, Sluis and Delta events  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/history/ZEELAND_REVOLT_TIMELINE.yaml

## History rules
Path: `history/README.md`  
Role: historical-layer methodology and status rules  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/history/README.md

---

# Claims and structured canon

## Central Source Claims registry
Path: `claims/SOURCE_CLAIMS.yaml`  
Role: historical/source claims and confidence/provenance links  
Use when: asserting historical fact in canon/worldbuilding  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/claims/SOURCE_CLAIMS.yaml

## Themes
Path: `narrative/themes.yaml`  
Role: thematic/values links, including `VALUE.CLAES.SINNE`  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/narrative/themes.yaml

---

# High-value source provenance used in current modules

## Wauters — sensory religious space
Path: `sources/SRC-WAUTERS-RELIGIOUS-SPACE-2021.md`  
Review status: targeted thematic review  
Use when: senses, church interior, altars, guilds, bells, movement, smell, ritual, memory space  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/sources/SRC-WAUTERS-RELIGIOUS-SPACE-2021.md

## Van Bruaene — rederijkers
Path: `sources/SRC-VAN-BRUAENE-OM-BETERS-WILLE-2008.md`  
Use when: chambers, Landjuweel, civic religion, performance, craft/trade networks  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/sources/SRC-VAN-BRUAENE-OM-BETERS-WILLE-2008.md

## Pollmann — Memory in Early Modern Europe
Path: `sources/SRC-POLLMANN-MEMORY-EARLY-MODERN-EUROPE-2017.md`  
Use when: memory carriers, violence, silence, later retelling, public/private memory  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/sources/SRC-POLLMANN-MEMORY-EARLY-MODERN-EUROPE-2017.md

## Stein & Pollmann — Networks, Regions and Nations
Path: `sources/SRC-STEIN-POLLMANN-NETWORKS-REGIONS-NATIONS-2010.md`  
Review status: TARGETED_REVIEW  
Use when: layered identity, civic ritual, supra-regional identity, post-1585 identity shifts  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/sources/SRC-STEIN-POLLMANN-NETWORKS-REGIONS-NATIONS-2010.md

## Pollmann & Spicer — Public Opinion and Changing Identities
Path: `sources/SRC-POLLMANN-SPICER-PUBLIC-OPINION-2007.md`  
Review status: TARGETED_REVIEW  
Use when: oral news, rumour, verification, persecution, public opinion, rhetorician discourse  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/sources/SRC-POLLMANN-SPICER-PUBLIC-OPINION-2007.md

## Leuven Bible / Catholic biblical context
Path: `sources/SRC-HIST-CATHOLIC-BIBLE-LOWCOUNTRIES-1548-001.md`  
Use when: Vulgate, Latin liturgical norm, Leuven Bible, Liesvelt distinction  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/sources/SRC-HIST-CATHOLIC-BIBLE-LOWCOUNTRIES-1548-001.md

## Lucas 8 comparison
Path: `sources/SRC-LUKE8-LEUVEN-LIESVELT-COMPARISON.md`  
Role: source-checked Luke 8 wording and correction of earlier false quotation  
RAW: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/sources/SRC-LUKE8-LEUVEN-LIESVELT-COMPARISON.md

---

# Claude scene-use recipes

## If writing a Goes church scene ca. 1542–1554
Read in this exact order:
1. `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md`
2. `storybible/modules/WORLD_GOES_CHURCH_LOCAL.md`
3. `storybible/modules/WORLD_GOES_CHURCH_LITURGICAL_GUARDRAILS.md`
4. `narrative/religious_space_sensory_church.yaml`
5. `WRITING_PROTOCOL.md`

Hard reminders:
- benches/chairs are not automatically anachronistic;
- host elevation is secure; chalice elevation is not locally secured;
- do not assert a specific Goese exterior consecration bell/klepkotje without new evidence;
- Zeven Getijden: documented foundation 12 March 1442; unstable first phase; formal re-establishment 31 May 1471;
- old blockwerk organ present before 1550; exact position remains uncertain;
- local Goes evidence outranks Antwerp comparison.

## If writing a Revolt-era Goes/Zeeland scene
Read:
1. active master;
2. `HISTORICAL_SUBSTRATE_1540_1605.md`;
3. `ZEELAND_REVOLT_TIMELINE.yaml`;
4. `PUBLIC_OPINION_IDENTITY_REVOLT.md`;
5. local Goes transition module if 1577–1578;
6. `WRITING_PROTOCOL.md`.

Always distinguish historical fact from what the viewpoint character actually knows.

---

# Maintenance rule

Whenever a new module becomes **ACTIVE** or a formerly open source becomes canon-relevant, update this manifest with:
- exact repository path;
- role;
- authority/status;
- when to use it;
- dependencies/guardrails;
- exact raw URL.

A write-capable AI must not claim the manifest is current unless it has checked the target branch immediately before modifying it.
