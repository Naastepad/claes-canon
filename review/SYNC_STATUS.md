# Synchronization status

Status: `SYNC_COMPLETE`

Release state: `FEATURE_BRANCH_READY_FOR_PR`

PR #5 and PR #6 are merged on `main`. Branch `mayken-lampert-beloved-20260814` adds the explicit author-approved identity of Claes' beloved as **Mayken Adriaensdr. Lampert** and synchronizes that choice through source claims, story claims, entities, decisions, relationships and human-readable storybible authority.

## Canonical family state
- mother: **Tanneken Jansdochter**, fictional, born approximately 1519–1522 / preferred ca. 1520, dies 18 May 1554;
- younger brother: **Jan Corneliszn. Nissepat**, fictional, born approximately June 1544, about eighteen months younger than Claes, dies 18 May 1554;
- unborn third child: sex/name remain unknown; Tanneken is about six months pregnant on 18 May 1554;
- paternal grandfather: historical **Claes Jacobsz. Nissepat**, with fictional kinship to Cornelis/Claes;
- paternal grandmother: fictional **Lijsbet Pietersdochter**, story death ca. 1540–1541;
- maternal grandfather: fictional kinship figure modeled on historical Goese **Jan Jansen kuiper** evidence; story death around 1543, not an archival death date;
- maternal grandmother: fictional **Mayken Pietersdochter**, alive in 1554.

## Beloved / Lampert state
- Claes' beloved is **Mayken Adriaensdr. Lampert**, fictional, born approximately 1546 in Goes;
- in novel canon she is daughter of **Adriaen Jacobsz. Lampert** and granddaughter of the older **Jacob/Jacop Lampart/Lambert apothecary household**;
- Jacob/Jacop Lampart/Lambert is historically attested as a Goese apothecary;
- Adriaen Jacopsen is explicitly styled `apteker` in 1554 and 1556 and Adriaen Jacopsen Lampert has a matching historical property trail;
- identification of those Adriaen records as one man is **SUPPORTED**, not literally proved in one current act;
- Jacob→Adriaen kinship is **SUPPORTED/UNPROVEN** historically and deliberately adopted as novel genealogy;
- no historical daughter of Adriaen has been found in the searchable transport corpus; Mayken's daughtership is explicit fiction;
- the name Mayken is sourced from the direct Lampart environment (`Mayken huisvrouw Jacop Lampart`, 1543), without claiming a proved naming chain;
- Mayken's fictional mother remains open;
- `OPEN.DODOENS.PROVENANCE.001` remains open.

## 1554 contrast
- Claes' household loss remains the canonical destruction of home plus deaths of Tanneken, Jan and unborn sibling.
- Mayken shares the Goese 1554 fire horizon but not Claes' exact trauma.
- The Lampert property **de Zwaene** is historically attested before the fire and as a burned house in January 1555; Mayken's personal memory and her family's rebuilding are novel reconstruction.
- This gives Mayken a counter-memory of material destruction followed by renewed work rather than making her a duplicate of Claes' bereavement.

## Functional distinction
- Tanneken anchors embodied, practical household knowledge and the early *sinne* line.
- Jan anchors love, rivalry, action and immediacy; he is not a decorative casualty.
- Claes Jacobsz. anchors property, credit, provenance and educational continuity after 1554.
- Mayken Pietersdochter anchors care, bodily memory, Tanneken's family history and post-fire mourning continuity.
- **Mayken Adriaensdr. Lampert** anchors independent materia-medica, botanical, Dodoens, material-verification and error-control expertise and later sensory/spiritual companionship.
- Claes remains the personal merels/Dee/Monas/Castanea key-holder and bearer of final responsibility.

## Historical integrity rules
- Historical Claes Jacobsz. Nissepat and his documented property acts remain separate from the fictional genealogy.
- `SC.HIST.GOES.JAN_JANSEN_KUIPER.CLUSTER_1535_1544.001` records a historical Goese kuiper pattern but explicitly warns that the generic name may conflate multiple men.
- The maternal-grandfather identity, kinship and circa-1543 story death are novel reconstruction.
- Lijsbet, Mayken Pietersdochter, Tanneken and Jan Corneliszn. are fictional.
- Mayken Adriaensdr. Lampert is also fictional; the Lampert apothecary milieu around her is historically anchored.
- Do not collapse the historical `Mayken huisvrouw Jacop Lampart` and `Merricken huisvrouw Jacob/Jacop de apotheker` records without new evidence.
- The unborn child's sex/name remain open.
- The 1554 loss of the specific Nissepat household and its casualties remain novel canon grounded in the historically supported partially burned Nieuwstraat/Armenhoek environment, not archival victim/property proof.

## Storybible synchronization
- `storybible/MAYKEN_LAMPERT.md` is the detailed canonical authority for Mayken's identity and role.
- `sources/SRC-HIST-GOES-LAMPERT-APOTHECARY-001.md` holds the historical/fictive source boundary.
- `claims/SOURCE_CLAIMS_LAMPERT_APOTHECARY.yaml` atomizes the historical evidence and uncertainty.
- `claims/STORY_CLAIMS_MAYKEN_LAMPERT.yaml` contains the five new author-approved story claims.
- `entities/MAYKEN_LAMPERT.yaml` holds Mayken and the Lampert historical anchor entities.
- `entities/ENTITIES.yaml` resolves `ENT.PERSON.BELOVED` to Mayken.
- `canon/DECISIONS.yaml` and `canon/DECISIONS_2026-08-14.md` contain `DEC.CLAES.BELOVED.MAYKEN_LAMPERT.2026-08-14`.
- `canon/OPEN_DECISIONS.yaml` resolves `OPEN.CLAES.BELOVED.IDENTITY.001`; Dodoens provenance remains open.
- `narrative/relationships.yaml` resolves `REL.CLAES.BELOVED` to Claes–Mayken and distinguishes their fire histories.
- `storybible/MASTER.md` points to the Mayken dossier as detailed authority where older broad prose still uses the generic beloved/apothecary-daughter label.
- `review/MIGRATION_REVIEW.yaml` now classifies 47 Story Claims, including five new Mayken claims as `NEW` / `HUMAN_DECISION`.

## Validation and merge state
- This feature branch must pass **Validate Claes canon repository** before merge.
- No merge into `main` occurs without explicit author instruction.

## Remaining open matters
The authoritative list is `canon/OPEN_DECISIONS.yaml`. `OPEN.CLAES.BELOVED.IDENTITY.001` is resolved by the Mayken decision. `OPEN.DODOENS.PROVENANCE.001` remains active and should not be treated as closed merely because Mayken's household is now fixed.

## Lemma execution policy
- `lemma/*.lemma` remains the deterministic rules-as-code layer and is versioned and validated in GitHub.
- GitHub `main` remains authoritative until this feature branch is explicitly merged.
- LemmaBase is optional and downstream-only; it never overrides GitHub canon.
