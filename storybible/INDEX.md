# Storybible Index

Operational navigation for the current Claes Storybible.

## Start here

1. `MASTER.md` — authority, precedence and current fixed state.
2. `LEMMA_MCKEE_MASTER.md` — **current synchronized human-readable story synthesis** through 16 August 2026.
3. `../canon/OPEN_DECISIONS.yaml` — active unresolved backlog only.
4. `../review/SYNC_STATUS.md` — synchronization status.
5. `../review/CANON_CONFLICT_AUDIT_2026-08-16.md` — conflicts found and their resolution.
6. `../review/HISTORICAL_SUBSTRATE_RECOVERY_2026-08-16.md` — recovered historical/worldbuilding layer and recovery boundaries.
7. `../review/DOMAIN_REBUILD_ROUND_B_2026-08-16.md` — chapter-readiness rebuild for bread, beer, Reimerswaal, rederijkers/Landjuweel, Antwerp and schutterij/military practice.

`LEMMA_MCKEE_MASTER_2026-08-13.md` is a dated legacy snapshot. It is retained for development history but is not current authoring authority.

## Explicit decisions

- `../canon/DECISIONS.yaml` — core decision registry.
- `../canon/DECISIONS_2026-08-13.md` — birth/sinne and associated decisions.
- `../canon/DECISIONS_2026-08-14.md` — Goes/family decisions.
- `../canon/DECISIONS_2026-08-15.md` — execution/Reformation and memoriaal decisions.
- `../canon/DECISIONS_2026-08-16.yaml` — Brevísima 1578 / Seton separation.
- `../canon/DECISIONS_ALCHEMY_LIFELINE_2026-08-15.yaml` — current merged alchemical life-line state, including later supersessions.
- `../canon/DECISIONS_ALCHEMY_REFINEMENT_2026-08-16.yaml` — Green Lion/Sol/Enkhuizen and Nardusbloem refinement.
- `../canon/DECISIONS_RESOLUTIONS_2026-08-16.yaml` — callback-recovered Mayken decision and explicit Cornelis-death precedence.

## Active open decisions

- `../canon/OPEN_DECISIONS.yaml` — only genuinely unresolved core questions.
- `../canon/OPEN_DECISIONS_ALCHEMY_REFINEMENT_2026-08-16.yaml` — Rode-Leeuw carrier composition and exact Enkhuizen assay/choreography.
- `../canon/OPEN_DECISIONS_ALCHEMY_LIFELINE_2026-08-15.yaml` — legacy redirect/supersession record only.

Resolved/not-applicable records no longer remain mixed into the active open registry.

## Historical / research claims

- `../claims/SOURCE_CLAIMS.yaml`
- `../claims/SOURCE_CLAIMS_EXECUTIONS_REFORMATION.yaml`
- `../claims/SOURCE_CLAIMS_GOES_LIVING_CITY.yaml`
- `../claims/SOURCE_CLAIMS_GOES_2026-08-14.yaml`
- `../claims/SOURCE_CLAIMS_FAMILY_1540S.yaml`
- `../claims/SOURCE_CLAIMS_MEMORIAAL_PRINT_1564.yaml`
- `../claims/SOURCE_CLAIMS_LAMPERT_APOTHECARY.yaml` — Goese Lampart/Lambert/Lampert apothecary evidence.
- `../claims/SOURCE_CLAIMS_ALCHEMY_2026-08-16.yaml` — Agricola/Norton/Ercker/Morhof-based refinement claims.
- `../claims/SOURCE_CLAIMS_GOES_RELIGION_1577_1578.yaml` — recovered Goes 1577/1578 and Reimerswaal 1574 local history claims.
- `../claims/SOURCE_CLAIMS_HISTORICAL_SUBSTRATE_RECOVERY_2026-08-16.yaml` — recovered Catholic Bible, sensory church, rederijker, information-ecology and layered-identity claims.
- `../claims/SOURCE_CLAIMS_DOMAIN_REBUILD_2026-08-16.yaml` — Round-B atomic claims for food/craft, Reimerswaal school, Landjuweel, Antwerp print practice and schutterij/De Gheyn.

## Historical substrate / scene-world authority

This layer supplies non-fiction world state and scene conditions. It never creates fictional Claes participation by itself and never outranks later explicit story decisions.

- `../history/LOW_COUNTRIES_TRANSFORMATION_1540_1605.yaml` — machine-readable macro historical state, 1540–1605.
- `../history/LOW_COUNTRIES_TRANSFORMATION_1540_1605.md` — human-readable scene-oriented historical synthesis.
- `../history/ZEELAND_REVOLT_TIMELINE.yaml` — Zeeland-specific scene-changing chronology.
- `modules/HISTORICAL_SUBSTRATE_1540_1605.md` — integration and scene-query contract.
- `modules/PUBLIC_OPINION_IDENTITY_REVOLT.md` — rumour, verification, public opinion and layered identity.
- `../narrative/religious_space_sensory_church.yaml` — church as sensory field, social map and memory carrier; source-direct for Antwerp and transferable with scaling/local verification to Goes/Reimerswaal.
- `modules/WORLD_GOES_CHURCH_LOCAL.md` — local Goese church chronology, Seven Hours, music and guild materiality.
- `modules/WORLD_GOES_CHURCH_LITURGICAL_GUARDRAILS.md` — comparative liturgical/sensory scene guardrails.
- `modules/HISTORICAL_SUBSTRATE_GOES_CHURCH_LINK.md` — precedence between local Goes evidence and transferable comparative reconstruction.
- `modules/GOES_RELIGIOUS_TRANSITION_1577_1578.md` — Catholic continuity → confessional pressure → Reformed public-space transition.

Recovered provenance includes Wauters, Van Bruaene, Groenveld et al., Pollmann, Pollmann & Spicer, Stein & Pollmann, Catholic Bible/Luke 8 sources and the project-wide Revolt synthesis under `../sources/`.

### Writing-readiness rule

A historical domain is not considered chapter-ready merely because a source or dossier exists. For a relevant place/year/person/activity the authoring layer should be able to retrieve: provenance/evidence status, time-valid world state, actors/actions, materials, sensory fields, character knowledge/access, local-versus-transfer boundary, explicit guardrails and scene consequences.

## Chapter-ready practice domains — Round B

These dossiers are the authoring-facing bridge from research to scene construction. Use them together with `../narrative/domain_scene_packs.yaml`.

### Bread / grain / baking

- `domains/BREAD_GRAIN_BAKING_1540_1602.md`
- `../sources/SRC-HIST-BREAD-LOWCOUNTRIES-ZEELAND-001.md`
- world: `WORLD.BREAD_GRAIN`
- key boundary: urban professional bakery is a safer default than an invented household oven; exact Goese recipe, ferment, price and loaf weight remain open/local.

### Beer / biersteker / brewery economy

- `domains/BEER_BREWING_BEERSTEKER_1540_1580.md`
- `../sources/SRC-HIST-BEER-LOWCOUNTRIES-GOES-001.md`
- world: `WORLD.BEER_BREWING_DISTRIBUTION`
- key boundary: Cornelis is a **biersteker**, not automatically brewer or Nissepad-brewery owner; no generic gruit or modern style taxonomy.

### Reimerswaal / school / cost-pupil life

- `domains/REIMERSWAAL_SCHOOL_1554_1561.md`
- `../sources/SRC-HIST-REIMERSWAAL-SCHOOL-CITY-001.md`
- world: `WORLD.REIMERSWAAL`
- key boundary: durable historical school tradition is supported; Claes' exact 1554–1561 Latin curriculum, teacher/building and attendance are source-weighted novel reconstruction.

### Rederijkers / Nardusbloem / Antwerp Landjuweel 1561

- `domains/REDERIJKERS_LANDJUWEEL_1561.md`
- `../sources/SRC-HIST-REDERIJKERS-LANDJUWEEL-1561-001.md`
- `../sources/SRC-HIST-GOES-REDERIJKERS-001.md`
- key boundary: Silvius 1562 anchors fourteen official Antwerp competitors; current evidence does **not** establish Goes as one of them. Cornelis' deken status remains open; factor/prince are not canon.

### Antwerp time slices

- `domains/ANTWERP_TIME_SLICES_1561_1585.md`
- `../sources/SRC-HIST-ANTWERP-TIMESLICES-1561-1585-001.md`
- world: `WORLD.ANTWERP`
- required slices: 1561 theatre; 1563–64 book/workshop; 1566 broken image; 1567–69 surveillance/repression; 1576–78 wound/print release; 1585 transformed formative city.

### Goes schutterij / military practice

- `domains/SCHUTTERIJ_MILITARY_PRACTICE_1550_1607.md`
- `../sources/SRC-HIST-GOES-SCHUTTERIJ-DEGHEYN-001.md`
- world: `WORLD.SCHUTTERIJ_MILITARY`
- key boundary: schuttersgilde, civic watch, garrison/professionals and later standardized drill are separate; local sources disagree on 1516 versus 1530 for Edele Busse/Sint Adriaan; De Gheyn 1607 is a late comparator, not a Goes-1572 manual.

## Story truth

- `../claims/STORY_CLAIMS.yaml` — base story claims; older working claims are superseded where later explicit decisions say so.
- `../claims/STORY_CLAIMS_EXECUTIONS_REFORMATION.yaml` — exact Cornelis death and execution/testimony claims.
- `../claims/STORY_CLAIMS_FAMILY_1554.yaml`
- `../claims/STORY_CLAIMS_2026-08-14.yaml`
- `../claims/STORY_CLAIMS_MAYKEN_LAMPERT.yaml` — Mayken identity, family, fire, apothecary expertise and direct-reveal role.
- `../claims/STORY_CLAIMS_ALCHEMY_REFINEMENT_2026-08-16.yaml`

## People and relationships

- `../entities/ENTITIES.yaml` — current core persons/places; Claes 1542, Cornelis exact death, Mayken identity and current Seton separation.
- `../entities/FAMILY_1554.yaml`
- `../entities/MAYKEN_LAMPERT.yaml`
- `../entities/ALCHEMY_REDERIJKER_2026-08-16.yaml`
- `../narrative/relationships.yaml` — current Claes–Cornelis and Claes–Mayken dynamics.
- `../narrative/arcs.yaml` — cradle-to-grave and macro-transmutation arcs.
- `../narrative/sinne_recovery.yaml`
- `../narrative/beloved_recovery.yaml` — read together with Mayken detail dossier if generic labels survive.

## Major Storybible dossiers

### Goes / family

- `FAMILY_CLAES_1542_1554.md`
- `../narrative/world_goes_living_city.yaml`
- `../narrative/world_goes_grote_kerk.yaml`
- `../entities/GOES_LIVING_CITY.yaml`
- `../entities/GOES_GROTE_KERK.yaml`
- `modules/WORLD_GOES_CHURCH_LOCAL.md`
- `modules/WORLD_GOES_CHURCH_LITURGICAL_GUARDRAILS.md`

### Mayken

- `MAYKEN_LAMPERT.md` — governing detail authority; explicitly synchronized to the no-cipher model.
- `../sources/SRC-HIST-GOES-LAMPERT-APOTHECARY-001.md`

### Memoriaal / Brevísima

- `MEMORIAAL_BREVISIMA_PRINT_1564.md` — direct hidden readable print and chemical reveal.
- `MEMORIAAL_BREVISIMA_CASTOFF_1564.md` — 17 quarto sheets / 136 latent pages.
- `../narrative/code_architecture.yaml` — legacy filename; current content is direct material reveal, not a cipher architecture.

### Execution / Reformation

- `CORNELIS_EXECUTION_1569.md` — exact execution resolution.
- `EXECUTIONS_REFORMATION_CLAES_2026-08-16.md` — current execution/testimony mechanics.
- `EXECUTIONS_REFORMATION_CLAES.md` — older source-rich dossier; stale cipher/death-window passages are superseded.
- `modules/PUBLIC_OPINION_IDENTITY_REVOLT.md` — period information/identity context for repression, rumour and public interpretation.

### Alchemy / Antwerp / Enkhuizen

- `ALCHEMICAL_CHEMICAL_PROCESS_CHAIN_CLAES_LIFELINE.md` — base process dossier.
- `ALCHEMICAL_PROCESS_REFINEMENT_2026-08-16.md` — governing current refinement.
- `ANTWERP_THREE_VISITS_ALCHEMICAL_ARC_1561_1569.md` — three Antwerp visits / process scaffold.
- `../objects/ALCHEMY_OBJECTS_2026-08-16.yaml`
- `../narrative/alchemy_lifeline_refinement_2026-08-16.yaml`
- `../narrative/instances_alchemy_rederijker_2026-08-16.yaml`
- `../narrative/knowledge_states_alchemy_2026-08-16.yaml`

## Narrative realization

- `../narrative/instances.yaml`
- `../narrative/instances_executions_reformation.yaml`
- `../narrative/instances_alchemy_rederijker_2026-08-16.yaml`
- `../narrative/domain_scene_packs.yaml` — chapter-ready world/activity packets; these constrain possible scenes but do not create fiction automatically.
- `../narrative/scenes.yaml`
- `../narrative/structure.yaml`
- `../narrative/motifs.yaml`
- `../narrative/themes.yaml`
- `../narrative/CRAFT_GUARDRAILS.yaml`
- `../narrative/religious_space_sensory_church.yaml`

Important current limitation: `structure.yaml` still needs populated Book/Act/Sequence/Chapter/Beat hierarchy and `scenes.yaml` needs many more scene-level diagnostics. Round B makes six previously thin world/practice domains chapter-ready; it does **not** yet turn them into fixed chapters or Narrative Instances.

## Objects

- `../objects/OBJECTS.yaml`
- `../objects/ALCHEMY_OBJECTS_2026-08-16.yaml`

Key current rules:

- memoriaal = pre-bound carrier of readable hidden Brevísima;
- graphite rule = visible note layer + protection of latent tannin print;
- Zovitius = possible material cue, not cryptographic key;
- merels = independent game/motif, not recovery system;
- Rode Leeuw = deep red/red-brown completed projectiepoeder carrying already-present Sol;
- Seton = late alchemical mirror only, never Brevísima decoder.

## Deterministic engine

- `../lemma/core.lemma`
- `../lemma/knowledge.lemma`
- `../lemma/events.lemma`
- `../lemma/encounters.lemma`
- `../lemma/objects.lemma`
- `../lemma/clues.lemma`
- `../lemma/decode.lemma` — legacy filename; active rule concerns direct readable reveal when memoriaal + green vitriol are available.
- `../lemma/consistency.lemma`

## Conversion and review

- `../mapping/CONVERSION_LEDGER.yaml`
- `../mapping/CONVERSION_REPORT.yaml`
- `../review/MIGRATION_REVIEW.yaml` — historical migration audit; its old zero-conflict summary is not the current conflict assessment.
- `../review/CANON_CONFLICT_AUDIT_2026-08-16.md` — current conflict assessment.
- `../review/HISTORICAL_SUBSTRATE_RECOVERY_2026-08-16.md` — Round-A recovery audit.
- `../review/DOMAIN_REBUILD_ROUND_B_2026-08-16.md` — Round-B domain readiness audit.
- `../review/CHAT_COMMITMENT_AUDIT_2026-08-13.md` and addendum — recovered evidence of what earlier research work was actually completed.
- `../review/SYNC_STATUS.md`

## Validation

- `../scripts/validate_canon.py`
- `../scripts/validate_active_projection.py`
- `../.github/workflows/canon-repository-validate.yml`
- `../.github/workflows/lemma-validate.yml`

GitHub canon remains authoritative. Later explicit author decisions override stale broad prose; no AI may silently turn plausibility into canon.