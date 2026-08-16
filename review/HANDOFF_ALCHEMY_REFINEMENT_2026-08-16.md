# Handoff — Alchemical process refinement and Nardusbloem/Castanien correction

**Date:** 2026-08-16  
**Branch:** `authoring/alchemy-rederijker-refinement-20260816`  
**PR:** #11  
**Synchronization:** `SYNC_COMPLETE` for active authoritative layers

## Human decisions implemented

1. Cornelis is a Nardusbloem/older Magdalena-line member, not simply a historically attested Castanienbloem member.
2. In novel canon Cornelis has a formative role in the reform-minded/protestantiserende 1560s current that becomes the Edele Castanienbloem.
3. The Castanienbloem's 1595 date is treated as earliest surviving attestation, not founding date.
4. Green vitriol is an operational Groene Leeuw in Dee/Claes' process, not a universal historical synonym.
5. Green vitriol directly develops the tannin memoriaal but does not directly dissolve gold.
6. The Sol process includes failure-before-opening: force that attacks lesser metals can still fail against gold.
7. The same Sol/gold-bearing fraction is materially continuous through opening, Rode Leeuw, Saturn and assay; no gold is created from lead and no later gold is silently inserted.
8. The exact non-gold Rode Leeuw carrier remains open.
9. Ercker supports the Probierkunst/assay environment; a cupellation-like Enkhuizen mechanism is author-side reconstruction rather than a documented Seton procedure.
10. The 1602 frame follows Morhof's retrospective tradition: Enkhuizen, Jacob Hausfsen's house, 13 March 1602, about the fourth hour after noon, with the source's ~70-year distance preserved.
11. Routine tasting of vitriol/corrosive liquids is excluded from authoring practice; technical prose distinguishes vitrioolwater/uitloogwater from alkaline lye.

## Governing formulation

> What becomes visible was already present.

Literal material continuity: latent tannin typography and the Sol/gold fraction.  
Narrative analogy: testimony, memory and recovered *sinne*.

## Key new/updated authoritative surfaces

- `canon/DECISIONS_2026-08-16.md`
- `canon/DECISIONS_ALCHEMY_REFINEMENT_2026-08-16.yaml`
- `claims/SOURCE_CLAIMS_ALCHEMY_2026-08-16.yaml`
- `claims/STORY_CLAIMS_ALCHEMY_REFINEMENT_2026-08-16.yaml`
- `entities/ENTITIES.yaml`
- `entities/ALCHEMY_REDERIJKER_2026-08-16.yaml`
- `objects/ALCHEMY_OBJECTS_2026-08-16.yaml`
- `narrative/alchemy_lifeline_refinement_2026-08-16.yaml`
- `narrative/instances_alchemy_rederijker_2026-08-16.yaml`
- `narrative/knowledge_states_alchemy_2026-08-16.yaml`
- `storybible/ALCHEMICAL_PROCESS_REFINEMENT_2026-08-16.md`
- `storybible/ANTWERP_THREE_VISITS_ALCHEMICAL_ARC_1561_1569.md`
- `storybible/MASTER.md`
- `storybible/INDEX.md`
- `review/SYNC_STATUS.md`

## Provenance added

- Agricola 1556 — vitriolic/pyritic material to green-vitriol process family.
- Samuel Norton — multivalent Green Lion semantics.
- Ercker 1574 — Probierkunst / small-fire assay context.
- Morhof 1673 — retrospective Seton/Enkhuizen/Hausfsen/date-time tradition.
- Goese rederijker source bundle — Nardusbloem Catholic 1563 context, internal-pressure boundary, Castanien 1595 earliest attestation and Meertens split historiography.

## Open matters preserved

- `OPEN.CORNELIS.REDERIJKER.DEKEN.001`
- `OPEN.ALCHEMY.RED_LION.CARRIER_COMPOSITION.001`
- `OPEN.ALCHEMY.ENKHUIZEN_1602.ASSAY_DESIGN.001`

## Validation history

- Repository validation run 215 failed because the new machine-readable decision file contained one unquoted YAML scalar with a colon; the parse failure made the three new decision IDs appear unresolved.
- That quoting error was fixed without changing canon.
- Repository validation run 216 then had exactly one remaining error: `review/SYNC_STATUS.md` still stated `SYNC_PENDING`.
- Active authoritative layers were reviewed as synchronized; superseded older broad/datetime prose was explicitly classified as audit/development history with later authority routes in `MASTER.md` and `INDEX.md`.
- `SYNC_STATUS.md` was therefore promoted to `SYNC_COMPLETE` for active operating canon.
- Repository validation run **217 passed** on commit `38b240ead3cc4ba6b2cdf663005c5dc1e5632eb0`.
- This handoff commit is documentation-only and should receive the automatic continuity rerun before merge.
- No Lemma rule was changed in this pass; the alchemical refinement remains narrative/material continuity rather than a new executable decode dependency.

## Merge rule

Do not merge PR #11 without explicit author instruction.
