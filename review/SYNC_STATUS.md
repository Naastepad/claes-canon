# Synchronization status

Status: `SYNC_PENDING`

Release state: `AUTHORING_BRANCH`

Branch: `authoring/alchemy-rederijker-refinement-20260816`

Current branch purpose: synchronize the explicit 16 August 2026 correction/refinement of the alchemical life-line and Cornelis' rederijker identity across canon decisions, provenance, Story Claims, entities, objects, narrative arcs/instances/knowledge states, human-readable authority surfaces and review records.

`main` remains canonical until this branch passes validation, is reviewed through a PR and is explicitly merged.

## Canonical correction now represented on this branch

### Cornelis / rederijkers

- Cornelis is a **Goes poorter and biersteker**; the brewery belongs to the wider family/business environment rather than being fixed as his personal brewery.
- Cornelis is a **member of the Nardusbloem / older Magdalena-linked Goese rederijker tradition**.
- The Nardusbloem's 1563 institutional profile is treated as strongly Catholic on the basis of its Maria-Magdalena/chapel/death-mass/requiem context.
- In novel canon Cornelis plays a formative role in a **reform-minded/protestantiserende 1560s current** that becomes the later Edele Castanienbloem.
- **1595 is the earliest surviving source attestation of the Castanienbloem, not a founding date.** The 1560s origin is explicit historical fiction/reconstruction inside a documentary gap.
- The 1563 Nardusbloem conflict/member-change discussion may provide historical pressure but does not prove a confessional split.
- Meertens' later religious-split hypothesis is retained as historiography, not proof; his proposed confessional direction is not binding on novel canon.
- Later Nissepat participation around 1595–1596 remains a deliberate historical/family resonance.
- Cornelis' exact deken office remains `OPEN.CORNELIS.REDERIJKER.DEKEN.001`.
- Cornelis is not a printer; Silvius remains the press/type/proofing authority.

### Refined alchemical material chain

The active material/process model is:

`kies / pyritic-vitriolic rejected matter → weathering + water + air + time → vitrioolwater / green liquor → green vitriol / operational Groene Leeuw → direct tannin-text reveal + learned opening principle → ordinary strong-water failure on Sol → right compound corrosive relation → death/opening of Sol → materially continuous hidden Sol → red fixation / Rode Leeuw carrier → Saturn/lead → assay/cupellation-like reveal → projectio → release beyond possession`.

Hard guardrails:

- Green Lion is an **operational name in Dee/Claes' process**, not a universal historical equation `Green Lion = FeSO4`.
- Green vitriol **directly develops the tannin-loaded memoriaal text**, but it does **not** directly dissolve gold.
- `De dood van Sol` requires failure-before-opening: a strong water may attack lesser metals and still fail against Sol; force alone is not the right relation.
- `OBJ.SOL_GOLD_FRACTION` is materially continuous from visible gold through opening, red fixation, Saturn/projectio and the later visible assay result.
- No stage creates gold from lead and no fresh gold may be silently introduced after the deliberate opening of Sol.
- `OBJ.RED_LION_PROJECTIEPOEDER` carries already-present Sol; only its exact non-gold carrier/matrix composition remains open.
- Ercker supports a sixteenth-century *Probierkunst*/small-fire assay culture. A lead/cupellation-like explanation is an **author-side reconstruction**, not a documented Seton procedure.
- Technical prose should distinguish acidic/vitriolic `vitrioolwater/uitloogwater/oplossing/liquor` from modern alkaline lye; the chapter title `De loog van Antwerpen` may remain.
- Do not use routine tasting of vitriol or corrosive liquors as sensory diagnosis.

Governing law:

> **What becomes visible was already present.**

For the memoriaal typography and Sol this has literal material meaning; for testimony, memory and recovered *sinne* it is an analogy rather than identical chemistry.

### Enkhuizen 1602

The chosen novel frame now follows Morhof's retrospective 1673 Seton tradition:

- Enkhuizen;
- house of sailor Jacob Hausfsen;
- 13 March 1602;
- approximately the fourth hour after noon (~16:00);
- Alexander Seton/Sidonius as the historical-tradition figure.

The source distance remains explicit: Morhof reports the tradition roughly seventy years later. Exact furnace/projection/assay choreography, quantities, additional witnesses, public/private degree and immediate aftermath remain open.

## Provenance now synchronized

Dedicated source records now exist for:

- `SRC-HIST-AGRICOLA-DE-RE-METALLICA-1556-VITRIOL-001` — vitriolic/pyritic matter, water/leaching, green liquor and green-vitriol process family;
- `SRC-HIST-NORTON-KEY-ALCHEMY-GREEN-LION-001` — Green Lion semantic multivalence plus specific vitriol/copperas usage;
- `SRC-HIST-ERCKER-PROBIERKUNST-1574-001` — assay/Probierkunst and small-fire testing/separation context;
- `SRC-HIST-MORHOF-SETON-ENKHUIZEN-1673-001` — retrospective Seton/Enkhuizen/Hausfsen/date/time tradition;
- updated `SRC-HIST-GOES-REDERIJKERS-001` — Nardusbloem Catholic context, 1563 conflict boundary, 1595 earliest surviving Castanien attestation and split historiography.

`claims/SOURCE_CLAIMS_ALCHEMY_2026-08-16.yaml` atomizes the supported claims and explicit non-inferences.

## Structured layers synchronized in this pass

### Decisions / open decisions

- `canon/DECISIONS_2026-08-16.md`
- `canon/DECISIONS_ALCHEMY_REFINEMENT_2026-08-16.yaml`
- corrected `canon/DECISIONS_ALCHEMY_LIFELINE_2026-08-15.yaml`
- corrected `canon/OPEN_DECISIONS_ALCHEMY_LIFELINE_2026-08-15.yaml`
- `canon/OPEN_DECISIONS_ALCHEMY_REFINEMENT_2026-08-16.yaml`

### Claims / review

- `claims/SOURCE_CLAIMS_ALCHEMY_2026-08-16.yaml`
- `claims/STORY_CLAIMS_ALCHEMY_REFINEMENT_2026-08-16.yaml`
- `review/MIGRATION_REVIEW.yaml` — all seven new 16 August Story Claims classified as explicit `HUMAN_DECISION`; no new AI-derived canon is hidden in migration.

### Entities / objects

- `entities/ENTITIES.yaml` — Cornelis now explicitly Nardusbloem member with formative Castanien-origin role; occupation normalized to biersteker.
- `entities/ALCHEMY_REDERIJKER_2026-08-16.yaml` — Castanienbloem historical-organisation/fictional-early-origin layer plus Seton and Hausfsen.
- `objects/ALCHEMY_OBJECTS_2026-08-16.yaml` — green vitriol, materially continuous Sol fraction and Rode Leeuw/projectiepoeder.

### Narrative structure

- `narrative/alchemy_lifeline_refinement_2026-08-16.yaml` — material-process arc, alchemical process-chain motif, hidden-presence motif and secondary controlling principle.
- `narrative/instances_alchemy_rederijker_2026-08-16.yaml` — Castanien-origin sequence, Rode Leeuw, Saturnus and fixed-frame Enkhuizen projectio.
- `narrative/knowledge_states_alchemy_2026-08-16.yaml` — staged Boom/vitriol/Sol/reveal/red-fixation/1602 knowledge states plus Cornelis' Nardus/Castanien boundary.
- `narrative/motifs.yaml` — Castanea has been decoupled from the retired Brevísima recovery-key architecture and retained only as independent context/resonance.

### Human-readable storybible

- `storybible/ALCHEMICAL_PROCESS_REFINEMENT_2026-08-16.md` — governing detailed correction/refinement layer.
- `storybible/ANTWERP_THREE_VISITS_ALCHEMICAL_ARC_1561_1569.md` — directly synchronized to Cornelis=Nardusbloem, fictional Castanien origin, operational Green Lion, failure-before-Sol and material Sol continuity.
- `storybible/MASTER.md` — current precedence and 16 August normalization integrated.
- `storybible/INDEX.md` — all new decisions, sources, claims, entities, objects, narrative supplements and dossiers indexed.

## Existing memoriaal state remains active

The merged 15 August direct-text memoriaal model remains unchanged:

- readable Diets/Brabant Brevísima printed before binding in tannin/gum medium;
- Dee gives memoriaal + graphite before Boom;
- graphite remains visible while hidden tannin typography is latent;
- green vitriol later reveals readable text directly;
- no cipher/key-recovery architecture is required;
- 17 single-sheet quarto gatherings / 68 leaves / 136 latent pages remain the operational cast-off model.

The 16 August alchemical refinement strengthens, rather than alters, the material distinction: green vitriol is the **direct memoriaal developer**, while gold opening belongs to a different later compound-corrosive operation.

## Remaining synchronization work

The branch remains `SYNC_PENDING` for identifiable, bounded reasons:

1. `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` still contains retired post-4-October carrier/cipher/key-recovery prose and older alchemical shorthand.
2. `storybible/EXECUTIONS_REFORMATION_CLAES.md` still contains old direct-key/Castanea/code-as-testimony language in broad prose; current structured execution claims and `CORNELIS_EXECUTION_1569.md` outrank it.
3. `storybible/ALCHEMICAL_CHEMICAL_PROCESS_CHAIN_CLAES_LIFELINE.md` is retained as the 15 August base dossier and still contains looser shorthand in places (including older Green-Lion wording and a sensory taste suggestion). `ALCHEMICAL_PROCESS_REFINEMENT_2026-08-16.md` explicitly governs every conflict until the base dossier is fully regenerated.
4. `canon/OPEN_DECISIONS.yaml` still contains the older `OPEN.CORNELIS.REDERIJKERS.CHAMBER.001` as open. The 16 August explicit decision has in fact closed chamber identity as Nardusbloem; the later decision and supplemental open-decision files outrank this stale audit surface until the core file is regenerated.
5. `canon/DECISIONS.yaml` is an older core registry and does not yet absorb every 15–16 August supplement. The dated/supplemental decision files are current authority; the core registry should be regenerated in a later consolidation pass rather than silently rewritten without preserving audit history.

These remaining items are **representation drift**, not undecided story canon. The 16 August decisions and focused structured layers already govern the domain.

## Validation

Validation has **not yet been run on this 16 August branch**. After the current writes are complete:

1. open a PR to `main`;
2. run/inspect `Validate Claes canon repository`;
3. run/inspect `Validate Lemma canon`;
4. repair any reference/schema failures without changing author decisions;
5. keep `SYNC_PENDING` until the explicitly listed stale broad/core surfaces are regenerated, even if CI is green.

## Existing family state remains unchanged

The Goes fire/family rupture, Tanneken Jansdochter, Jan Corneliszn. Nissepat and both grandparent lines remain canonical and are not altered by this branch.

## Lemma execution policy

- `lemma/*.lemma` remains the deterministic rules-as-code layer.
- The alchemical life-line is primarily a material/narrative continuity architecture; only genuinely deterministic prerequisites belong in Lemma.
- `lemma/decode.lemma` continues to model the direct memoriaal reveal, not a cipher.
- GitHub `main` remains authoritative until this authoring branch is reviewed and merged.
