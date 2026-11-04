# Branchconvergentie en één geldende canon — controle 4 november 2026

**Peildatum:** 2026-11-04  
**Repository:** `Naastepad/claes-canon`  
**Geldige autoriteit:** uitsluitend geaccepteerde, in `main` opgenomen besluiten volgens `AI_ONBOARDING.md`, `AGENTS.md` en `REPOSITORY_INTEGRITY.md`.  
**Basis voor tellingen:** `main` op `2a4a2cb0f7997fc5d252b8f2555c064ab0b7ff3a` (na PR #23 en een aansluitende generatie van Claude-contextbestanden). Dit is een momentopname; achterstand/ahead-tellingen kunnen later veranderen.

## 1. Wat definitief is geïntegreerd

**PR #23**, 'Storybible: Claes — weer, sneeuwverhalen, stormvloeden en natuurkracht', is op 4 november 2026 daadwerkelijk **samengevoegd**; mergecommit `9d85c59eaae821f93a0e8f0a092841c1c31482a0`. Het nieuwe weerdossier en de historische bronclaims zijn rechtstreeks van `main` teruggelezen. De vervolgcommit `2a4a2cb...` heeft de Claude-context-packbestanden bijgewerkt; het weer is daarmee niet langer louter een autoringsbranch.

De canonische menselijke Storybible-master is **`storybible/LEMMA_MCKEE_MASTER.md`**, niet de gedateerde `LEMMA_MCKEE_MASTER_2026-08-13.md`, die historisch/legacy is.

## 2. Inventarisatie van resterende branches

Bij de controle waren er **24** branches naast `main`:
- **14 branches** zijn volledig achter `main` (ahead = 0): hun commits zijn voor de Git-grafiek geen nieuwe wijzigingen ten opzichte van main. Dit **bewijst niet** dat hun oudere tekst inhoudelijk de actuele waarheid is.
- **10 branches** zijn inhoudelijk of historisch **divergent** (ahead > 0, behind > 0). Een branchnaam of intern `status: CANON` op zo'n branch mag niet worden opgevat als geaccepteerde huidige canon.

### A. Nog openstaande pull requests

| PR | Branch | Ahead / behind versus momentopname | Status | Besluit |
| --- | --- | --- | --- | --- |
| [#12](https://github.com/Naastepad/claes-canon/pull/12) | `authoring/news-ecology-2026-08-16` | 6 / 266 | Open, niet samenvoegbaar met actuele main; toenmalige CI groen | **PENDING_REBASE_AND_AUTHOR_REVIEW**. Bevat vier nieuw te integreren brondossiers/nieuws-ecologiebestanden en wijzigingen aan `history/README.md` en `review/SYNC_STATUS.md`; dossier is zelf expliciet `ROUND_E...PROPOSED`, geen nieuw canonbesluit. |
| [#13](https://github.com/Naastepad/claes-canon/pull/13) | `egmond-1573-context` | 6 / 250 | Open, niet mergeable; toenmalige CI **FAILED** | **BLOCKED_VALIDATION_AND_RECONCILIATION**. YAML-parsefout in `canon/DECISIONS_EGMOND_ABBEY_1573.yaml`, onopgeloste `ENT.LOC.EGMOND.*` en andere IDs, ontbrekende brede synchronisatie. Historisch onderscheid 'ontmanteling/sloop versus simpele brand' is zinvolle onderzoeksvraag, maar niet als onbeproefde geldende canon invoeren. |
| [#22](https://github.com/Naastepad/claes-canon/pull/22) | `author/economic-state-layer-2026-08-30` | 120 / 68 | **Draft**, niet mergeable met actuele main; toenmalige CI groen | **HOLD_FOR_SUBSTANTIVE_CANON_REVIEW**. Ca. 69 paden ontbreken nog in main, met nieuwe economische geschiedenis, vervoer, maten, markten en De Hont/Horen-dossiers. Bevat tevens `status: CANON` beslissingen over Cornelis' bezit, zakelijk vermogen, een voorkeurschipper, schaal van bier/zout, scheepsmodel/lasten en een latere bedrijfslijn. Die fictieve preciseringen niet automatisch als historisch feit of door de auteur opnieuw geaccordeerde main-canon behandelen. |

**Opmerking:** `mergeable: false` geeft de GitHub-status van deze PR's op het controle-moment weer, niet de garantie dat ieder inhoudelijk bestand onbruikbaar is. Rebase of gerichte overdracht is nodig; daarna opnieuw validatie en auteurstoets.

### B. Divergente historische/development-branches zonder open PR

| Branch | Ahead / behind | Actuele interpretatie |
| --- | --- | --- |
| `agent/correct-claes-birth-1542-reimerswaal` | 20 / 500 (API-vergelijking) | Older alternative model; één bronbestand `sources/SRC-HIST-1512-PUTTUS-GOES-001.md` nog niet aanwezig op main; de bestaande current Puttus-besluiten hebben hogere prioriteit. Onderzoek eerst of deze bronlocators nieuw bewijs toevoegen. |
| `agent/enrich-reimerswaal-1555-1573` | 18 / 500 | Oude alternatieve representaties van bestaande paden; geen nieuwe padnamen in vergelijking; semantische diff vereist, niet blind terugmergen. |
| `agent/resolve-manuscript-sync-2026-08-21` | 1 / 98 | Oudere variant van bestaande canonbestanden, geen nieuwe paden; laat recentere huidige besluiten over brand en familie intact. |
| `authoring/alchemy-rederijker-refinement-20260816` | 29 / 295 | Oudere alchemie-ontwikkeling op reeds aanwezige paden; de huidige latere beslissingen gaan voor; inhoudelijk vergelijken, niet raw mergen. |
| `authoring/goes-fire-1554-20260814` | 7 / 419 | Legacy brandontwikkeling; uniek ontbrekend handoffbestand met destijds **OPEN** gelaten moederlot. Dat oude OPEN is later uitdrukkelijk beslist en kan **niet** worden teruggezet. |
| `authoring/v1` | 60 / 468 | **PRIORITY_CANON_CONFLICT_REVIEW**: bevat `canon/DECISIONS_2026-08-23.md` (nog niet op main) en `storybible/modules/CLAES_RUGGENGRAAT_1564_1602.md`; de eerste noemt diverse expliciete auteurbesluiten die niet zonder meer in de huidige main-architectuur zijn opgenomen. Zie §3. |
| `mayken-lampert-beloved-20260814` | 25 / 382 | Oudere alternatieve Mayken-/beloved-status, maar de huidige main heeft een uitdrukkelijk opgeloste Mayken-identiteit en eigen relatie- en levensboog. Niet regressief terugmergen. |

**De 14 achterlopende/geen-ahead-branches:** `agent/canonize-puttus-school-2026-08-18`, `agent/deepen-character-web-2026-08-19`, `agent/deepen-claes-cornelis-relation-2026-08-18`, `agent/fix-claude-context-canon-overlay-2026-08-18`, `agent/goes-fire-1554-development-2026-08-21`, `agent/ingest-editor-progression-2026-08-19`, `agent/landjuweel-1561-continuity-2026-08-22`, `agent/weather-claes-storybible-2026-11-04`, `authoring/executions-reformation-2026-08-15`, `authoring/goes-living-city-20260813`, `authoring/memoriaal-brevisima-print-20260815`, `family-tanneken-jan-grandparents-20260814`, `goes-fire-nieuwstraat-family-20260814`, `goes-grote-kerk-20260813`. Behoud ze als Git-historie of ruim ze later alleen na expliciet opruimbesluit op; ze maken geen zelfstandig alternatief canon.

## 3. Kritieke inhoudelijke conflictpunten — geen stille promotie

### `authoring/v1`: 23 augustus 2026 versus huidige main

Het ontbrekende `canon/DECISIONS_2026-08-23.md` noemt zichzelf expliciet auteur-canon. Dit is **een serieuze synchronisatiekloof**, niet 'oude oninteressante tekst'. Onder meer:
- Dee's natuurfilsosofische onderzoeksvraag uit 1564 (lucht/vuur/adem/groei) als levenslijn; geen anachronistische ontdekking van zuurstof.
- Een door de Beeldenstorm gedreven terugkeer Antwerpen → Goes in 1566.
- Maykens geleidelijke reputatieval in 1578 en Claes' vlucht **eerst naar Gouda**, daarna Delft, Egmond/Alkmaar, Hoorn, Enkhuizen.
- De schaal van Las Casas (1570 reconstructie, 1578 verspreiding), mogelijke eigen materiële transmutatie vóór Seton, en de morele eindvraag.
- Bronregel dat Claes historische gebeurtenissen soms direct, soms via consequenties, soms via nieuws meemaakt.

**Reële spanning:** deze branch noemt Claes' aanwezigheid bij de vernietiging van Reimerswaal 1573 liever indirect/nieuws, terwijl de **latere main-beslissing van 18 september 2026 uitdrukkelijk zegt dat hij de brand vanaf een boot ziet**. Ook is in main de exacte keten van zijn Goese vertrek 1572–1579 **OPEN**, terwijl de augustustekst al een specifieke Mayken-1578-oorzaak en Gouda-route als `CANON` markeert. Beide versies kunnen niet tegelijkertijd in dezelfde autoriteitsklasse worden behandeld.

**Besluit:** leg oude expliciete auteur-intentie volledig als *te reconciliëren* vast; behoud huidige main als operationeel gezag totdat de auteur de conflicterende of ontbrekende besluiten opnieuw heeft geharmoniseerd. De 23-augustusbron wordt niet gewist of tot onwaar verklaard, maar is **niet actief in main**. Betrokken route-, Mayken-, Dee- en eindstructuurregisters moeten gezamenlijk worden bijgewerkt als die keuzes opnieuw worden bevestigd.

### `author/economic-state-layer-2026-08-30`: 30 augustus versus huidige main

De economic branch heeft waardevolle bronwerkzaamheden en een `economic_state_resolver`, maar kent ook concrete nieuwe **fictieve** besluiten over jaaromzet, zoutkeetbezit, schipper Aernouldt de Hont vóór diens archiefattestatie in 1589 en een scheepsmodel (heude/last). De actuele main-beslissing rond Cornelis belegt vooral een **economisch belang** in een zoutkeet met afgebakende professionele rol, zonder deze latere preciseringen. **Bewijs over de echte schipper in 1589 is geen bewijs over zijn fictieve dienst bij Cornelis vóór 1569.**

**Besluit:** splits `SC.*` en economische `WORLD.*` context van nieuwe `DEC.*`/`STC.*` fictiekeuzes. Beoordeel bronherkomst, numerieke schaal en aansluiting op de nu geldende familie-/brand-/handelscanon, alvorens een integratie-PR te maken. Draft #22 blijft onafhankelijk en is niet de alternatieve master.

### Egmond en nieuws-ecologie

#12 blijft voorgestelde onderzoekscontext. #13 bevat onderbouwing en verbeeldingsmogelijkheden maar had een **aantoonbaar falende validator**. Beiden moeten niet op basis van het bestaan van een branch als 'bewezen' of 'geaccepteerd' worden aangeboden.

## 4. Operationele regel: één geldende waarheid, met zichtbare onzekerheid

1. **Alle AI's en auteurs lezen standaard `main`** en `AI_ONBOARDING.md`, `canon/`, `storybible/LEMMA_MCKEE_MASTER.md`, `storybible/INDEX.md` in de vastgestelde autoriteitsvolgorde.
2. In een andere branch kan `CANON` staan, maar dat betekent **branch-lokale aspiratie**, nooit automatisch actuele main-canon.
3. **Historisch bewijs en auteurswaarheid zijn verschillende zaken.** `SC.*` bronclaims blijven met zekerheid/onzekerheid gelabeld, `DEC.*`/`STC.*` vormen geldende fictieve beslissingen na expliciete autorisatie en integratie.
4. Conflicterende besluiten worden niet op datum, hoeveelheid tekst of CI-groen stilzwijgend samengevoegd. Documenteer hun IDs, bron, chronologie en gevolg, en vraag gerichte auteurkeuze wanneer zij niet verenigbaar zijn.
5. Een **actieve `OPEN.*`** blijft open, ook als een oudere branch een mogelijk antwoord als `CANON` labelt. Alleen uitdrukkelijke synchronisatie sluit het.
6. **Geen force-push of branchverwijdering** als 'opschonen' zonder expliciete instructie. Git bewaart provenance; `main` bepaalt de huidige leesbare waarheid.
7. Iedere integratie vereist bronstatus, beslissingstoets, downstream-synchronisatie, GitHub-read-back en aparte CI-status. Auto gegenereerde Claude/context-prompts zijn afgeleide kopieën, nooit eigen canon.

## 5. Werkvoorraad / prioriteiten

1. **P0** — beslissingen uit `authoring/v1` (23 augustus) en de latere open/vaste beslissingen uit `main` expliciet verzoenen, vooral 1566 retour, Mayken-1578, Gouda, Dee-vraag, 1573 boot en 1602; geen stille import.
2. **P0/P1** — draft #22 bron- en besluitdeel gescheiden auditen; economische `WORLD.*` en getuigen-/schipperclaims pas na coherente canoncontrole.
3. **P1** — #13 Egmond: YAML- en ID-reparaties, relatieve datering en bewijsgrenzen, daarna opnieuw CI en master/index synchroniseren.
4. **P2** — #12 nieuws-ecologie: onderzoeksdossier moderniseren en met huidige information-war-route vergelijken, daarna eventueel als `PROPOSED` integreren.
5. **P2** — resterende zes legacy-divergenties diffen op nog niet in main aanwezige relevante bronclaims; behoud oudere andersluidende besluitinhoud uitsluitend als ontwikkeling, niet als nieuwe canon.

**Uitkomst van deze pass:** PR #23 is werkelijk geïntegreerd. De expliciete autoriteitsbron `main` wordt zichtbaar en correct gedocumenteerd. De 10 overige divergerende branches worden **niet** valselijk 'synced' verklaard en niet mechanisch gemerged: inhoudelijke auteurs- en bronverschillen staan in deze audit voor gerichte opvolging.
