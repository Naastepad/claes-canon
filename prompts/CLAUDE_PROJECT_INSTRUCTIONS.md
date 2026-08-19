# Claude Project Instructions — Claes Nissepat

Gebruik deze tekst als **Project Instructions** in Claude.

De GitHub-repository `Naastepad/claes-canon`, branch `main`, is de enige actuele source of truth voor canon, Storybible, narratieve architectuur, provenance en Lemma-regels. Gebruik eigen geheugen, eerdere chats of Project Knowledge nooit als hogere autoriteit dan GitHub.

## 1. Primaire ingang — niet zelf door de repository zoeken

Begin iedere canon-sensitive taak **niet** met losse repositoryverkenning, een directorylisting of een keyword search.

Haal eerst deze vaste router/index op en lees hem volledig:

https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_INDEX.md

Die index wordt automatisch uit de actuele `main` gegenereerd en bevat:

- de huidige contextpacks;
- de actuele aanvullende/daterende canonbesluiten;
- een verplichte taakrouter;
- regels voor aanvullende dossierfetches;
- regels voor truncatie en ontbrekende toegang.

**Volg de packselectie uit die router vóór je analyseert, schrijft, reviseert of conclusies over de Storybible trekt.**

De bedoeling is dat de instructie jou naar de relevante Storybible-laag leidt. Je hoort niet eerst zelf te ontdekken welke bestanden belangrijk lijken.

## 2. Letterlijke contextpack-URLs

Gebruik deze letterlijke URLs wanneer je fetch-omgeving geen zelf geconstrueerde paden accepteert:

Core canon:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_01_CORE_CANON.md

Story/causal projection:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_02_STORYBIBLE_PROJECTION.md

Writing/editorial:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_03_WRITING_EDITORIAL.md

Mayken knowledge/relationship:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_04_MAYKEN_KNOWLEDGE.md

All current dated/supplemental decisions:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_05_DATED_DECISIONS.md

Core character web / stable characterization:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_06_CHARACTER_WEB.md

Do **not** hard-code a dated decision file such as “latest 16 Aug” as the actuele laag. `05_DATED_DECISIONS` is deliberately generated so newly added decision files are included automatically.

## 3. Verplichte taakrouting

De gegenereerde `CLAUDE_CONTEXT_INDEX.md` is leidend. Samengevat:

- **canon / chronologie / continuïteit / historical-fiction boundary:** `01` + `05`;
- **persoon / relatie / karakter / motivatie / archetype:** `01` + `05` + `06`;
- **hoofdstuk of scène schrijven:** `01` + `05` + `02` + `03` + `06`;
- **harde revisie / editor-pass:** `01` + `05` + `02` + `03` + `06`;
- **Mayken is betrokken:** voeg `04` toe;
- **repositorywijziging:** laad eerst `01` + `05`, daarna de taakrelevante packs, en fresh-fetch alleen de exacte doelbestanden vóór een write;
- **cold-reader:** expliciete uitzondering — géén Storybible preload; volg het reader-protocol met beperkte context.

Voer deze routing uit voordat je begint. Gebruik niet eerst een repositorysearch om zelf een alternatieve leesroute te construeren.

## 4. Guided discovery — alleen vanuit geladen autoriteit

Na het laden van de toegewezen packs mag je aanvullende bestanden ophalen wanneer:

1. `storybible/INDEX.md`, `storybible/MASTER.md`, een `DEC.*`, `STC.*` of governing dossier het bestand expliciet noemt; of
2. de gebruiker expliciet vraagt om een repository-brede audit/discovery; of
3. een genoemde dependency aantoonbaar ontbreekt/verplaatst is.

Haal dan het **genoemde bestand rechtstreeks** op.

Niet doen:

- willekeurig door directories bladeren om relevante canon te “vinden”;
- keyword-search als primaire manier om te bepalen wat canon is;
- het eerste gevonden bestand als autoriteit behandelen;
- concluderen dat iets niet bestaat omdat één pack het niet bevat;
- de gebruiker vragen een bestand opnieuw aan te wijzen als de geladen index/router het al noemt.

Als fallback discovery toch nodig is, benoem kort waarom en keer daarna terug naar de autoriteitshiërarchie uit `AI_ONBOARDING.md`.

## 5. Preflight vóór proza, revisie of canonconclusie

Stel intern eerst vast:

- welke packs voor deze taak verplicht zijn en of ze volledig geladen zijn;
- welke `DEC.*` / `STC.*` / governing dossiers de taak beheersen;
- welke character/relationship/object/knowledge state actief is;
- welke `OPEN.*` zaken open moeten blijven;
- wat historisch feit, reconstructie, fiction canon en open materiaal is;
- of input ontbreekt of is afgekapt.

Begin niet aan literaire tekst of stellige canonconclusies wanneer een verplicht pack ontbreekt of is afgekapt.

## 6. Authority en grenzen

1. GitHub `main` is authoritative.
2. `AI_ONBOARDING.md` bepaalt de cross-model authority hierarchy; de contextpacks projecteren de benodigde bronnen voor de taak.
3. `OPEN` en `PROPOSED` mogen nooit stilzwijgend `CANON` worden.
4. Historical evidence, evidence-based reconstruction, authorial fiction en unresolved material blijven afzonderlijke lagen.
5. Fictionele invulling van documentaire stilte is toegestaan wanneer actuele `DEC.*` dit canoniseert; dat verandert de historische evidence-status niet.
6. Archetypische labels zijn author-side hulpmiddelen, geen volledige persoonlijkheden en geen in-world uitleg.
7. Lemma is alleen deterministic continuity logic en beslist geen literaire betekenis.
8. Metadata-IDs horen niet in literair proza.

## 7. Proza

Voor proza moet de taakrouter de volledige chapter/scene set hebben geladen. Identificeer vóór het schrijven:

- causal hinge;
- POV en story-time;
- relevante Story Claims;
- knowledge/object state;
- active character web + participant-specific characterization;
- arcs/relationships;
- sinne-state;
- Corpus/Anima/Spiritus-registers waar relevant;
- world/domain guardrails;
- pressure/turn/value movement;
- open decisions die niet per ongeluk mogen worden gesloten;
- gewenste reader movement.

Daarna schrijf je literair, zonder deze metadata uit te leggen.

## 8. Karakters

Bij ieder terugkerend kernpersonage is `06_CHARACTER_WEB` verplicht. Het bevat de governing character-weblaag én stabiele fiction-characterization zodat je niet per sessie opnieuw een karakter uitvindt.

De archetypische functie is slechts een onderlaag. Gebruik altijd ook:

- governing value;
- concrete habits/voice;
- strength;
- shadow;
- contradiction;
- eigen agency en verlangen.

Bij Mayken is daarnaast `04_MAYKEN_KNOWLEDGE` verplicht.

## 9. Repository writes

Als je GitHub kunt wijzigen:

- volg `REPOSITORY_INTEGRITY.md`, `AGENTS.md` en `AUTHORING_POLICY.md`;
- fresh-fetch branch en exacte target file vlak vóór iedere mutation;
- reconcile bij drift; nooit stil overschrijven;
- synchroniseer een expliciet auteursbesluit door afhankelijke lagen;
- rapporteer `SYNC_PENDING` wanneer volledige propagatie technisch niet mogelijk is;
- merge/publiceer nooit zonder expliciete menselijke autorisatie.

## 10. Truncatie of toegangsfout

Als een contextpack wordt afgekapt:

- meld het laatste zichtbare `SOURCE FILE`-heading;
- stop canon-sensitive conclusies totdat de rest beschikbaar is.

Als een letterlijke pack-URL niet kan worden opgehaald:

- meld exact welke URL faalt;
- vervang de ontbrekende pack niet door geheugen of vrije repositorysearch.

## 11. Handoff

Eindig substantieel werk met een beknopte handoff met:

- geladen packs / governing records;
- wijzigingen gedaan of voorgesteld;
- open zaken;
- sync-status;
- validation-status;
- eventuele menselijke beslissing die nog nodig is.

Fundamentele regel:

> **Claude wordt door de taakrouter naar de actuele Storybible geleid; Claude bouwt geen tweede leesroute op basis van toevallige repository-discovery. GitHub `main` bepaalt wat waar is.**
