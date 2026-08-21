# Claes Storybible — MASTER / operating authority

**Logical master ID:** `SB.CLAES.MASTER`  
**Current synchronization date:** 21 August 2026
**Authoring readiness:** Rounds A–D implemented; manuscript/fire continuity sync active

This repository is the structured operating projection of Revision 11 plus later explicit author decisions. The lossless source edition remains preserved for material not yet atomized, but later decisions override conflicting source or legacy-master wording.

## Source edition

`Claes_Storybible_MASTER_COMPLEET_2026-08-10_REVISIE11_MACROSTRUCTUUR_PROJECTIO(1).md`

- source lines: `3803`
- parsed headings: `296`
- SHA-256: `e38430f0165e7c0779a8ae6bba6a208773c677682f55295a940e91fdb2ed9edd`
- source role: `LOSSLESS_PROSE_AUTHORITY`
- structured role: `IN_REPOSITORY_OPERATING_PROJECTION`

Every top-level source section remains accounted for in `mapping/CONVERSION_LEDGER.yaml`. Unatomized prose does not disappear merely because it has not yet become a claim or Narrative Instance.

## Current human-readable authorities

Start with:

1. `storybible/LEMMA_MCKEE_MASTER.md` — **current operating story synthesis**.
2. `storybible/STORY_PROJECTION_ROUND_C.md` — causal/character projection from settled canon and chapter-ready world knowledge toward final structure.
3. `storybible/CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md` — stable core-cast characterization, character shadows and author-side archetypal contrast; explicitly separates historical evidence from fiction fills.
4. `WRITING_PROTOCOL.md` — governing drafting, revision, pacing, prose-quality and scene-retention protocol.
5. `review/READER_EXPERIENCE_PROTOCOL.md` — cold-reader, human pilot-reader and reader-feedback method.
6. `storybible/INDEX.md` — operational navigation.
7. `canon/OPEN_DECISIONS.yaml` — active unresolved backlog only.
8. `review/SYNC_STATUS.md` — synchronization state.

The dated `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` is a **legacy snapshot**, not current authoring authority. It may preserve obsolete 1545/cipher/death-window/open-beloved wording for audit history only.

## Dedicated governing dossiers

- `STORY_PROJECTION_ROUND_C.md` — causal spine, deeper Great-Work architecture, Mayken independent arc and explicit open 1572–1579 Goes hinge.
- `CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md` — governing core-character web; archetypes are author-side lenses only, while approved voice/habit/shadow details are fiction canon for continuity.
- `ALCHEMICAL_OPERATION_PALETTE.md` — non-binding author-side palette for Calcination, Sublimation, Solution, Putrefaction, Distillation, Coagulation and Tincture; diagnostic and compositional only, never a mandatory 3×7/21-chapter scheme.
- `WRITING_PROTOCOL.md` — scene construction, prose, pacing, reader experience and editorial decision rules.
- `review/READER_EXPERIENCE_PROTOCOL.md` — reader-testing authority.
- `review/READER_FEEDBACK_TEMPLATE.md` — consistent reader-evidence logging.
- `review/MANUSCRIPT_CANON_SYNC_2026-08-21.md` — closure audit for the editor-ingest repairs and 1554 manuscript projection.
- `MEMORIAAL_BREVISIMA_PRINT_1564.md` — hidden readable tannin/gum print, Dee handoff, graphite rule, direct green-vitriol reveal.
- `MEMORIAAL_BREVISIMA_CASTOFF_1564.md` — 17 single-sheet quarto gatherings / 136 latent pages.
- `FAMILY_CLAES_1542_1554.md` — Tanneken, Jan, grandparents, 1542 house and 1554 family rupture.
- `GOES_FIRE_1554_CAUSAL_ARCHITECTURE.md` — fire origin/ambiguity, unequal survivor positions, multi-chapter aftermath, grandfather continuity and Reimerswaal departure.
- `GOES_SCHOOLING_PUTTUS_1550_1554.md` — Puttus school bridge plus explicit evidence/fiction characterization boundary.
- `GOES_CLERGY_MATHIJS_CLEMENS_1541_1564.md` — named historical Goese clergy anchors: Mathijs Jacopsen/Jacobsen in 1541–early 1542, Clemens van den Dale in 1564, with the 1542–1563 succession gap preserved.
- `MAYKEN_LAMPERT.md` — resolved identity, pre-fire childhood acquaintance and independent character/material role of Mayken, synchronized to no-cipher canon.
- `CORNELIS_HOUSE_OF_LOVE_NETWORK_1551_1569.md` — governing route from beer/cask commerce through Ghysbrecht, Dens and Barrefelt into the translocal Huis der Liefde; Plantin is a later node and the evidence/fiction boundary is explicit.
- `CORNELIS_EXECUTION_1569.md` — detailed 19 November 1569 Cornelis execution model.
- `EXECUTIONS_REFORMATION_CLAES_2026-08-16.md` — current execution/testimony mechanics.
- `ALCHEMICAL_CHEMICAL_PROCESS_CHAIN_CLAES_LIFELINE.md` — base alchemical/chemical process dossier.
- `ALCHEMICAL_PROCESS_REFINEMENT_2026-08-16.md` — governing refinements for Green Lion semantics, failure-before-opening, conserved Sol, Rode Leeuw, assay and Morhof Seton frame.
- `ANTWERP_THREE_VISITS_ALCHEMICAL_ARC_1561_1569.md` — Antwerp three-visit/process scaffold, subject to later decisions where older wording survives.
- `domains/*.md` — Round-B chapter-ready practice domains for bread, beer, Reimerswaal school, rederijkers/Landjuweel, Antwerp time slices and schutterij/military practice.

## Machine-readable layers

### Decisions / story truth

Current explicit author decisions live across:

- `canon/DECISIONS.yaml`
- dated `canon/DECISIONS_*.md`
- `canon/DECISIONS_2026-08-16.yaml`
- `canon/DECISIONS_GOES_CLERGY_2026-08-16.yaml`
- `canon/DECISIONS_ALCHEMY_LIFELINE_2026-08-15.yaml`
- `canon/DECISIONS_ALCHEMY_REFINEMENT_2026-08-16.yaml`
- `canon/DECISIONS_RESOLUTIONS_2026-08-16.yaml`
- `canon/DECISIONS_STORY_PROJECTION_2026-08-16.yaml`
- `canon/DECISIONS_HOUSE_OF_LOVE_NETWORK_2026-08-16.yaml`
- `canon/DECISIONS_CHARACTER_WEB_2026-08-19.yaml`
- `canon/DECISIONS_MANUSCRIPT_SYNC_2026-08-21.yaml`

Latest explicit decision wins within its domain. A base registry is not allowed to resurrect an older state merely because a later decision lives in a supplement.

`claims/SOURCE_CLAIMS*.yaml` stores evidence/reconstruction claims. `claims/STORY_CLAIMS*.yaml` stores novel truth. Evidence and story truth remain separate. Characterization story truth added on 19 August lives in `claims/STORY_CLAIMS_CHARACTER_WEB_2026-08-19.yaml`.

### World/practice state

- `narrative/world_modules.yaml`
- `narrative/domain_scene_packs.yaml`
- `narrative/religious_space_sensory_church.yaml`
- `narrative/world_goes_clergy_1541_1564.yaml`
- `storybible/domains/*.md`

These define what can plausibly happen in a place/time/activity. A world module never creates fictional participation by itself.

### Narrative state and projection

- `entities/*.yaml`
- `entities/CHARACTERIZATION_2026-08-19.yaml` — stable fiction characterization separated from historical biography.
- `entities/LAS_CASAS.yaml` — historical Las Casas entity with fiction-interiority boundary.
- `objects/*.yaml`
- `narrative/knowledge_states*.yaml`
- `narrative/relationships.yaml`
- `narrative/arcs.yaml`
- `narrative/motifs.yaml`
- `narrative/instances*.yaml`
- `narrative/alchemical_authorial_architecture.yaml`
- `narrative/story_projection_round_c.yaml`
- `narrative/character_web_archetypes.yaml` — author-side value/shadow contrast web; never in-world labels.
- `narrative/mayken_independent_arc.yaml`
- `narrative/mayken_relationship_projection.yaml`
- `narrative/goes_departure_1572_1579.yaml`

### Editorial / reader layer

- `narrative/editorial_gates.yaml`
- `WRITING_PROTOCOL.md`
- `review/READER_EXPERIENCE_PROTOCOL.md`
- `review/READER_FEEDBACK_TEMPLATE.md`

Editorial verdicts (`RETAIN / REVISE / MERGE / CUT`) do not alter canon. They judge whether a scene should exist and whether the prose successfully communicates the intended story.

### Deterministic subset

`lemma/*.lemma` is rules-as-code only. Lemma may veto an impossible combination; it never invents canon or literary quality.

## Fixed chronology and life-state corrections

The following are current and must not be reopened by legacy prose:

- **14 March 1541:** historical anchor — mr. Mathijs Jacopsen is explicitly attested in Goes as **vice-pastoor**.
- **27 February 1542:** historical anchor — mr. Mathijs Jacobsen is explicitly attested as **`vice-cureyt ter Goes`**.
- **8 December 1542:** birth of Claes in Goes. The exact Goese priest/office-holder on this date remains historically **UNKNOWN**; Mathijs must not be projected automatically from February to December and is not proven to have baptized Claes.
- **12 January 1551:** historical anchor — Ghysbrecht, kuiper van Antwerpen, acquires *De Haeswindeken* in Goes; Cornelis' commercial relationship with him is novel canon, not archival fact.
- **ca. 1552–1553:** Cornelis belongs in novel canon to the translocal Huis der Liefde through the chain Ghysbrecht → Adriaan Dens → Barrefelt. The Ghysbrecht → Dens bridge is explicit novel reconstruction; Plantin is not the converter.
- **1553–1554:** Claes and Mayken know one another as Goese children in ordinary acquaintance/friendship; no childhood romance is canonized.
- **18 May 1554:** fictional family home lost; Tanneken, Jan and unborn child die; Claes and Cornelis survive. This catastrophe tests an already existing Familist conviction rather than causing Cornelis' conversion.
- **1554–1561:** Claes at Reimerswaal; Zierikzee is the abandoned pre-fire plan.
- **August 1561:** Antwerp Landjuweel; Dee is not placed there; Goes is not currently established as one of the fourteen official competing chambers.
- **1563/early 1564:** Dee/Silvius formation.
- **20 March 1564:** historical anchor — Clemens van den Dale is explicitly attested as **`licentiaat pastoor Goes`**.
- **before Boom in early 1564:** Dee gives the already hidden-print memoriaal and graphite stift to Claes.
- **4 October 1564:** adult macro-Nigredo/security break; no physical alteration or ciphering of the memoriaal. Cornelis' Familist background does not by itself close the separate exact low-level trigger.
- **autumn 1567:** first Cornelis arrest/examination in Antwerp and release on borg/conditions.
- **19 November 1569:** Cornelis fictionally executed in Antwerp, witnessed by Claes.
- **1570:** direct green-vitriol reveal/read of hidden readable Brevísima; no cryptographic recovery chain.
- **1572–1579:** exact material/economic/legal chain by which Goes finally becomes nonrecoverable for Claes remains **authorial-design OPEN** under `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001`.
- **1578, Antwerp:** printed publication completes the textual mission — projectio of the Word.
- **1584:** Delft moral bottom / Albedo threshold.
- **13 March 1602, ca.16:00, Enkhuizen:** Morhof-framed Seton projectio at the house of Jacob Hausfsen — projectio of Matter.
- **after 1602:** projectio of the Self / Status Prima Nova; exact death remains open.

## Goese clergy / Maria Magdalena current state

`DEC.GOES.CLERGY.MATHIJS_VICE_CUREYT.2026-08-16`, `DEC.GOES.CLERGY.CLEMENS_VAN_DEN_DALE.2026-08-16` and `DEC.GOES.CLERGY.SUCCESSION_BOUNDARY.2026-08-16` govern.

- **Mathijs Jacopsen/Jacobsen** is a historical person and the named clergy anchor for the Catholic Goese world immediately preceding and entering Claes' birth year.
- He is verified as **vice-pastoor** on 14 March 1541 and **`vice-cureyt ter Goes`** on 27 February 1542.
- His association with the **Maria Magdalenaparochie / Grote Kerk** is a strongly supported contextual identification, but the decisive 1542 act itself says only `ter Goes`.
- Property transactions `aan het kerkhof` and `achter het koor van de kerk` strengthen his church-world embedding but do **not** prove residence.
- He is not proven to be the titular benefice-holder, not proven in office on 8 December 1542 and not proven to have baptized Claes.
- **Clemens van den Dale** is verified as **`licentiaat pastoor Goes`** on 20 March 1564.
- The exact titular pastor above Mathijs and the complete **1542–1563** succession remain a historical research gap. Do not extend Mathijs or Clemens across that interval by plausibility alone.

The governing human-readable dossier is `storybible/GOES_CLERGY_MATHIJS_CLEMENS_1541_1564.md`; machine-readable support lives in `claims/SOURCE_CLAIMS_GOES_CLERGY_2026-08-16.yaml`, `claims/STORY_CLAIMS_GOES_CLERGY_2026-08-16.yaml`, `entities/GOES_CLERGY_1541_1564.yaml` and `narrative/world_goes_clergy_1541_1564.yaml`.

## Memoriaal / Brevísima current state

`DEC.MEMORIAAL.DIRECT_TEXT_NO_CIPHER.2026-08-15` governs.

The completed Diets/Brabant text is set in ordinary readable movable type and printed nearly invisibly with a reconstructed clear gallnut/tannin + gum-arabic medium before binding. The paper is the hidden book. Dee gives the bound object to Claes before Boom and requires graphite rather than ink.

Green vitriol later supplies the iron that darkens the tannin-loaded letterforms. The result is already readable language. **Reveal is not decryption.**

Retired from the Brevísima mechanism:

- ciphertext/nomenclator stream;
- 24×24 matrix;
- merels as recovery key;
- Monas as ordering key;
- Castanea as key anchor;
- special Dodoens nomenclator carrier;
- Primus Index;
- multi-week cryptographic reconstruction.

Merels, Monas, Castanea and ordinary Dodoens may survive independently where they serve game, education, botany, symbolism or character.

## Character web / historical-fiction characterization current state

`DEC.HISTORICAL_GAPS.FICTIONAL_CHARACTERIZATION.2026-08-19`, `DEC.CHARACTER_WEB.ARCHETYPAL_LENS.2026-08-19` and `DEC.CHARACTER_WEB.CORE_CAST.2026-08-19` govern.

The repository now treats documentary silence as potential **authorial space**, not as an automatic ban on characterization. Historical evidence remains unchanged; fiction fills are separately labelled and become continuity canon only by explicit decision.

Core author-side constellation:

- Claes — Integration / Seeker-Witness;
- Cornelis — Law / Father-Gatekeeper;
- Tanneken — Body / embodied household wisdom;
- Jan — Act / brother-double;
- Puttus — Word / hermeneutic teacher;
- Mayken — Matter / independent material counterpart;
- Dee — Transformation / magician-mentor;
- Silvius — Transmission / pragmatic mediator;
- Las Casas — Conscience / witness-herald.

These are lenses, not full personality definitions. Every role is individualized through a governing value, concrete habits, contradiction and a shadow produced by overuse of a real strength. Archetypal shorthand must never be written as in-world explanation.

`storybible/CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md` governs the human-readable layer. Machine detail lives in `entities/CHARACTERIZATION_2026-08-19.yaml` and `narrative/character_web_archetypes.yaml`.

## Mayken current state

The beloved identity is resolved as **Mayken Adriaensdr. Lampert**, fictional, born ca.1546 in Goes. `ENT.PERSON.BELOVED` is retained only as a legacy stable entity ID; it does not mean her identity is open.

Her historical embedding is the real Lampart/Lambert/Lampert apothecary environment. The project distinguishes verified persons/property records, supported identity/genealogy reconstruction and explicit fictional daughtership.

Claes and Mayken now canonically know one another as children before 18 May 1554 through ordinary Goese contact, play and early material/botanical observation. This is **not childhood romance**; later relation may contain recognition and rediscovery without predestination.

Mayken is independently competent in materia medica, preparation, measurement, botanical/material identification, trained sensation and error control. She may assist direct reveal and reading but is **not** a cryptographic solver or special-Dodoens key-holder.

Her family also experiences the 1554 fire through the burned *Zwaene* property. Her counter-memory is destruction **plus rebuilding**, not a duplicate of Claes' household annihilation.

`ARC.MAYKEN.LIFE` is a governing independent character arc. Mayken must have objectives, judgements, costs and choices not reducible to Claes. Her exact adult mid-arc work/family/social-pressure chain remains open under `OPEN.MAYKEN.INDEPENDENT_MIDARC.001`.

Her mature relationship with Claes is projected by `REL.CLAES.MAYKEN.CONJUNCTIO`: reciprocal relation between unlike modes of knowing without absorption or possession. Conjunctio is author-side architecture, not mandatory in-world terminology.

## Cornelis current state

Cornelis is:

- Goes poorter;
- **biersteker**, not fixed brewery owner;
- rederijker and logistical/book-material carrier;
- member in novel canon of the translocal **Huis der Liefde / Familia Caritatis** by ca. 1552–1553;
- not a printer.

His entry route is fixed as **beer/cask commerce → Ghysbrecht/Gijsbrecht, kuiper van Antwerpen → fictional trusted bridge to Adriaan Dens → Barrefelt → Huis der Liefde**. Ghysbrecht is a historical archival anchor but is **not** a documented Familist; his relation to Dens is explicit novel reconstruction. Dens is Cornelis' first knowingly identifiable Familist, and Barrefelt is the historically plausible network deepener. `CORNELIS_HOUSE_OF_LOVE_NETWORK_1551_1569.md` governs the full evidence/story boundary.

Cornelis can remain outwardly embedded in Catholic Goes; no separate Goese Familist congregation or invented formal initiation ritual is required. The 1554 fire tests this pre-existing affiliation rather than creating it.

**Plantin is a later print/distribution node, not Cornelis' converter.** Cornelis' later clandestine book/paper logistics grow from the same practical competencies as the beer trade — casks, storage, accounts, credit, route knowledge, carriers, discretion and trust — without implying that books are routinely hidden in beer barrels.

His chamber identity is fixed as the **Nardusbloem / older Magdalena-linked Goese tradition**. The Zusterhuis remains his meeting environment.

In novel canon he helps form a reform-minded/protestantiserende current in the 1560s that becomes the later Edele Castanienbloem. The historical sources do not prove that early split. **1595 is the earliest surviving attestation, not a proved founding date.**

Whether Cornelis ever serves as deken remains open.

His death is fixed as the 19 November 1569 Antwerp fictional execution model. The Familist network now supplies a longer trust-history behind his protective silence and book/paper route, but `OPEN.SECURITY.LOW_LINK.1564.001` remains open unless separately resolved.

## Alchemical current state

### Material process law

> **What becomes visible was already present.**

Material chain:

`kies / pyritic rejected matter → weathering + water + air + time → vitrioolwater / operational Groene Leeuw → direct tannin-text reveal + opening lesson → strong-water failure on Sol → right compound relation → death/opening of Sol → materially continuous hidden Sol → red fixation / Rode Leeuw → Saturn/lead → assay/cupellation-like reveal → projectio → release`

Guardrails:

- Green Lion is process-dependent vocabulary, not a universal historical equation `Green Lion = FeSO4`.
- Green vitriol directly reveals the tannin text but does not directly dissolve gold.
- Sol must first resist ordinary strong water: force is not the same as right relation.
- No real gold is created from lead; no later silent gold addition is allowed.
- Rode Leeuw/projectiepoeder is deep red to red-brown and carries already-present Sol; exact non-gold carrier composition remains open.
- Cupellation-like assay is authorial reconstruction, not documented Seton protocol.
- Do not use routine tasting of corrosive/vitriol liquors.
- Seton is wholly separated from the Brevísima line.

### Great-Work authorial architecture

`DEC.CLAES.GREAT_WORK.AUTHORIAL_ARCHITECTURE.2026-08-16` and `ARC.CLAES.GREAT_WORK.AUTHORIAL` govern:

`Status Prima → Corpus / Anima / Spiritus → Transmutatio/Rubedo → Projectio → Status Prima Nova`

This **nests with and does not replace** `ARC.CLAES.MACRO_TRANSMUTATION`:

`Drager → macro-Nigredo → Albedo/Onderscheiding → Rubedo/Verbinding → Projectio/Overdracht`.

- **Corpus**: actual material processes, bodies, food, books, plants, buildings, cities, metals and tools.
- **Anima**: meaning, language, belief, testimony, loyalty, memory, public interpretation and love.
- **Spiritus**: Claes' vigilance, certainty-seeking, grief, agency, embodied *sinne*, responsibility and sovereignty.

Corpus, Anima and Spiritus are simultaneous spiral registers, **not three successive books or three mechanically identical cycles**. `Solve et Coagula` is an author-side movement of separating false fusions and reconnecting in truer relation. No fixed operation count is mandatory.

The seven-operation palette in `ALCHEMICAL_OPERATION_PALETTE.md` preserves **Calcination, Sublimation, Solution, Putrefaction, Distillation, Coagulation and Tincture** as a non-binding compositional vocabulary. It may diagnose or enrich a scene, sequence or causal hinge only when the real material and human event earns that operation. It must never be used to force a 3×7 structure, an exact 21-chapter count, or a false historical claim that this sequence was universal.

> **The author knows the Work; Claes undergoes it; the reader experiences it.**

## Causal story projection

`ARC.CLAES.CAUSAL_SPINE` in `narrative/story_projection_round_c.yaml` is the current pre-structure for chapter architecture. It maps fourteen hinges from childhood Status Prima through post-1602 Status Prima Nova.

A future chapter must identify the hinge it advances or justify a genuinely new hinge. World research earns scene space only when it creates pressure, choice, relationship movement, consequence or necessary reader experience.

The unresolved H09 hinge is the 1572–1579 Goes severance. It must remain visibly open until the author chooses a historically disciplined material/economic/legal causal chain.

## Goes 1572–1579 design boundary

Historically grounded current anchors:

- 1572 siege damage includes outside salt works and a brewery in the Voorstad;
- a Nissepad brewery with equipment is documented in 1577;
- that Nissepad brewery is **not proven identical** to the brewery burned in the Voorstad and is not proven Cornelis property;
- Jan Jansen Nissepat sells a burned Westzelke salt-pan site in 1577, but the destructive event is unknown;
- later transport acts are not automatically executions, confiscations or forced sales.

The open story question remains: **which chain of real damage, fictional residual interest, debt/claims, legal settlement and network collapse finally makes Goes cease to function as Claes' recoverable home or economic anchor?**

## Editorial / reader-experience current state — Round D

Round D is now part of authoring authority, but it is not story canon.

### Scene necessity

`GRD.EDITORIAL.SCENE_NECESSITY` requires every developed scene to be tested for:

1. plot necessity;
2. character necessity;
3. information necessity;
4. reader-experience necessity;
5. uniqueness — whether all useful functions are served better elsewhere.

Verdicts:

- **RETAIN** — indispensable and strongest current place/form;
- **REVISE** — indispensable function, weak execution;
- **MERGE** — necessary material duplicates or gains force in combination;
- **CUT** — no indispensable function, or every function is better served elsewhere.

Historical richness, research effort, symbolism and beautiful prose do not independently justify retention.

### Prose and pacing

`GRD.EDITORIAL.PROSE_QUALITY` and `GRD.EDITORIAL.PACING` require POV filtration, concrete material language, selective sensory cognition, metabolized research, responsive rhythm, meaningful entry/exit and allocation of reader attention around choice and consequence.

Pacing is not simply speed. A quiet scene can be necessary; a calm scene cannot be inert filler.

### Reader experience

`GRD.EDITORIAL.READER_EXPERIENCE` separates authorial intention from experienced effect.

Cold-reader passes must not preload hidden Storybible explanation. AI may simulate cold reading, but **AI cold-reader simulation does not substitute for actual human pilot readers**.

Human reader observations are logged with `review/READER_FEEDBACK_TEMPLATE.md`, separating reported experience/problem from reader-proposed fix. Repeated independent reports carry more revision weight than isolated preference. Reader voting never decides canon.

### Meedogenloze redacteur

`GRD.EDITORIAL.RUTHLESS_EDITOR` is a standing hard-review mode:

> **Niet aardig, wel precies. Als een scène niet werkt, zeg dat. Geen complimenten en geen verzachtende formuleringen wanneer die de diagnose vertroebelen.**

A technically and historically correct scene may still be weak fiction and may still receive `CUT`.

## Active open-decision policy

`canon/OPEN_DECISIONS.yaml` contains **only active unresolved questions**. Resolved, superseded and `RESOLVED_NOT_APPLICABLE` history belongs in decision/audit files.

This distinction is mandatory:

- **historical/research open** — evidence might close it;
- **experimental open** — only a material test can close it;
- **authorial design open** — the novel must choose it;
- **irreducibly uncertain** — preserve historical uncertainty and choose explicitly fictional reconstruction if needed.

A historical/research gap does not automatically become a factual authorial claim. However, under `DEC.HISTORICAL_GAPS.FICTIONAL_CHARACTERIZATION.2026-08-19`, the novel may deliberately fix a **fiction-canon answer** inside that gap for recurring characterization or continuity while leaving the evidence status UNKNOWN. Evidence and novel truth remain separate axes.

Round-C high-impact authorial opens include:

- `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001`;
- `OPEN.MAYKEN.INDEPENDENT_MIDARC.001`.

Neither may be silently closed by prose, reader preference or historical plausibility alone.

The Goese clergy succession gap between the February 1542 Mathijs anchor and the March 1564 Clemens anchor is a **historical/research open**, not permission to fabricate a historical continuous incumbency. A fictional scene-use choice, if ever required, must be separately labelled rather than projected as evidence.

## Narrative development backlog

The recovery and readiness rounds are now complete:

- **A** — historical substrate recovered;
- **B** — six major world/practice domains made chapter-ready, supplemented by the evidence-bounded Goese clergy world state;
- **C** — world projected into causal character architecture;
- **D** — editorial, pacing and reader-feedback gates made operational;
- **Character Web refinement** — core cast differentiated through stable fiction characterization, value contrast and shadow while preserving historical evidence boundaries.

The next major task is **structural realization**:

`Book → Act → Sequence → Chapter → Scene → Beat`.

`narrative/structure.yaml` remains largely unpopulated and `narrative/scenes.yaml` contains only a small number of full scene diagnostics. Future population should use `ARC.CLAES.CAUSAL_SPINE`, the character web where recurring cast is involved, plus Round-B scene packs and Round-D scene-necessity/pacing/reader gates during construction rather than only after a full draft exists.

## Precedence

When records conflict:

1. latest explicit current `DEC.*` author decision, including supplements;
2. active later domain-specific `STC.*` story claim or explicit supersession declared by a later decision;
3. dedicated current governing dossier, including `STORY_PROJECTION_ROUND_C.md` and `CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md` within their domains;
4. current `LEMMA_MCKEE_MASTER.md`;
5. synchronized entities/objects/world modules/arcs/relationships/instances and causal projections;
6. Revision 11 prose for unsuperseded unatomized meaning;
7. source claims for historical support;
8. proposals and open decisions;
9. dated legacy masters/session memory — audit/context only.

`WRITING_PROTOCOL.md` and the Round-D editorial layer govern **implementation and evaluation**, not truth precedence. Never use an editorial verdict or reader preference to rewrite canon silently.
