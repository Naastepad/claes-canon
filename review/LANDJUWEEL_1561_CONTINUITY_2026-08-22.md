# Landjuweel 1561 — manuscript continuity synchronization

**Date:** 22 August 2026  
**Branch:** `agent/landjuweel-1561-continuity-2026-08-22`  
**Scope:** synchronize the current chapter `Het Landjuweel` with the active storybible while preserving historical/fiction boundaries.

## Input reviewed

Author-supplied continuity note based on section 22 of `Landjuweel_1561_historisch_dossier_voor_Claes_aangevuld.docx`, explicitly adjusted by the author to what is actually present in the current chapter. The dossier file itself was not re-ingested in this change; the supplied continuity note and current repository authorities were the manuscript-side input.

## Canon decisions synchronized

1. Claes is **eighteen** in August 1561. Canon birth date: 8 December 1542; nineteenth birthday: 8 December 1561.
2. The Reimerswaal → Goes → Antwerp journey is the first joint Claes/Cornelis travel since 1554. Commercial beer-trade/credit network is primary; Landjuweel is the cultural opportunity.
3. Cornelis is a rederijker/observer, not an official Brabant competitor; Goes/Nardusbloem receives no invented competitive status or prize.
4. Claes witnesses the 3 August entry, becomes separated from Cornelis, and experiences the final Brussels chamber without paternal interpretation.
5. Historical **Cornelis van Ghistele** is the chapter's one substantive rederijker interlocutor. The personal meeting and dialogue are fiction canon; Claes' answer is `misschien datgene wat een mens mist.`
6. Historical **Willem van Haecht** carries the fictional editorial-censorship scene. His role and the event's censorship constraints are historical; the exact deletion gesture is not documented biography.
7. The Landjuweel supplies later-use images and tensions but no alchemical teaching, secret initiation or Freemasonic membership. Symbolic ordering is deferred to later Claes.
8. Cornelis' final-evening acknowledgment creates a sincere but incomplete rapprochement after seven years of physical distance.
9. **Willem Silvius does not meet Claes in the 1561 chapter.** Direct Claes–Silvius/Dee formation starts in 1563. The prior relationship projection beginning in August 1561 has been corrected.
10. No Castanienbloem name/deanship or formal Brabant/Antwerp office is created for Cornelis in 1561.

## Historical review result

The historical substrate supports the 3 August 1561 formal entry of fourteen Brabant chambers, the central question concerning what most moves a human being to art, the last Brussels chamber continuing beyond two in the morning in the cited witness tradition, explicit restrictions against words attacking religion/clergy/government, Van Haecht's Violieren role, Van Ghistele's Goudbloem/Landjuweel role, and Silvius' 1562 printed afterlife.

### Topographic discrepancy kept open

The current manuscript continuity note gives:

`Keizerspoort → Huidevettersstraat → Meirbrug → Onze-Lieve-Vrouwekerk → Melkmarkt → Grote Markt`

The presently checked historical description gives:

`Keizerspoort → Huidevetterstraat → Eiermarkt → Melkmarkt → Grote Markt`

The cathedral of Onze-Lieve-Vrouwe is separately attested for the ceremonial/figurative kerkgang of **5 August**. Therefore the manuscript's Meirbrug/Onze-Lieve-Vrouwe segment is preserved as current manuscript content but is **not labelled historically verified**. This is tracked as `OPEN.LANDJUWEEL.ENTRY_ROUTE.1561.001`.

## Optional 1562 bridge

`OPEN.CLAES.SILVIUS.LANDJUWEEL_PRINT_1562.001` preserves, without executing, the author's suggested transition in which Claes later encounters Silvius' printed Landjuweel texts and sees moving/noisy performance become fixed and orderly on paper. This cannot create retroactive direct Silvius contact in 1561 or pre-empt the 1563–1564 formation sequence.

## Relationship impact

`REL.CLAES.CORNELIS` now contains a discrete August 1561 rapprochement phase between post-fire physical separation and the later secrecy/exclusion phase. The later secrecy conflict therefore follows a brief possibility of mutual recognition rather than an unbroken seven-year emotional flatline.

`REL.CLAES.SILVIUS` now begins direct editorial recognition in February 1563, not August 1561.

## Narrative impact

The Landjuweel hinge in `ARC.CLAES.CAUSAL_SPINE` now carries four chapter-ready beats:

- entry/separation and autonomous observation;
- Van Ghistele and Claes' provisional answer;
- Van Haecht and the material risk of censorship;
- final-evening father/son rapprochement.

The causal movement is now:

`public multiplicity → temporary removal of paternal mediation → personal judgement → language as risk → partial relational opening`

This preserves the chapter's later symbolic resonance without turning 1561 into premature alchemical instruction.

## Repository synchronization

Created:
- `canon/DECISIONS_LANDJUWEEL_1561_2026-08-22.yaml`
- `canon/OPEN_DECISIONS_LANDJUWEEL_1561_2026-08-22.yaml`
- `claims/STORY_CLAIMS_LANDJUWEEL_1561_2026-08-22.yaml`
- `claims/SOURCE_CLAIMS_LANDJUWEEL_1561_2026-08-22.yaml`
- `entities/LANDJUWEEL_1561_PERSONS.yaml`
- `narrative/landjuweel_1561_refinement.yaml`
- `review/MIGRATION_REVIEW_SUPPLEMENT_LANDJUWEEL_2026-08-22.yaml`
- this review/handoff record.

Updated:
- `storybible/domains/REDERIJKERS_LANDJUWEEL_1561.md`
- `sources/SRC-HIST-REDERIJKERS-LANDJUWEEL-1561-001.md`
- `narrative/relationships.yaml`
- `narrative/story_projection_round_c.yaml`
- `storybible/STORY_PROJECTION_ROUND_C.md`

Checked and left unchanged because already compatible at their intended level of abstraction:
- `storybible/MASTER.md`
- `storybible/LEMMA_MCKEE_MASTER.md`
- `storybible/INDEX.md`
- core `NI.EVENT.LANDJUWEEL.1561.001` and `STC.CLAES.LANDJUWEEL.1561.001`; the new refinement and atomic Story Claims specialize these records without replacing their stable IDs.

## Validation protocol

The repository workflow `Validate Claes canon repository` runs both `scripts/validate_canon.py` and `scripts/validate_active_projection.py` on pull requests touching these paths. Local cloning is unavailable in the current execution runtime, so CI status must be reported separately from write persistence. No merge is performed by this synchronization task.
