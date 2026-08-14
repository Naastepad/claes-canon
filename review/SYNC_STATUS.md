# Synchronization status

Status: `SYNC_COMPLETE_ON_FEATURE_BRANCH`

Release state: `FEATURE_BRANCH_REVIEW`

Branch: `family-tanneken-jan-grandparents-20260814`

This branch records the author's explicit approval of the extended Claes family architecture. `main` remains canonical until this branch is reviewed and merged.

## New/updated family canon on this branch
- mother: **Tanneken Jansdochter**, fictional, born approximately 1519–1522 / preferred ca. 1520;
- younger brother: **Jan Corneliszn. Nissepat**, fictional, born approximately June 1544 and about eighteen months younger than Claes;
- unborn third child: sex/name remain unknown; Tanneken is about six months pregnant on 18 May 1554;
- paternal grandfather: historical **Claes Jacobsz. Nissepat**, with fictional kinship to Cornelis/Claes;
- paternal grandmother: fictional **Lijsbet Pietersdochter**, story death ca. 1540–1541;
- maternal grandfather: fictional kinship figure modeled on historical Goese **Jan Jansen kuiper** evidence; story death around 1543, not an archival death date;
- maternal grandmother: fictional **Mayken Pietersdochter**, alive in 1554.

## Functional distinction
- Tanneken anchors embodied, practical household knowledge and the early *sinne* line.
- Jan anchors love, rivalry, action and immediacy; he is not a decorative casualty.
- Claes Jacobsz. anchors property, credit, provenance and educational continuity after 1554.
- Mayken anchors care, bodily memory, Tanneken's family history and post-fire mourning continuity.
- The Jan Jansen-kuiper model anchors craft, barrels, containment and the material economy around Cornelis' beer trade without becoming a proven genealogical ancestor.
- Lijsbet anchors inherited paternal-family memory and gives Claes Jacobsz. an earlier experience of spousal bereavement.

## Historical integrity rules
- Historical Claes Jacobsz. Nissepat and his documented property acts remain separate from the fictional genealogy.
- `SC.HIST.GOES.JAN_JANSEN_KUIPER.CLUSTER_1535_1544.001` records a historical Goese kuiper pattern but explicitly warns that the generic name may conflate multiple men.
- The maternal-grandfather identity, kinship and circa-1543 story death are novel reconstruction.
- Lijsbet, Mayken, Tanneken and Jan Corneliszn. are fictional.
- The unborn child's sex/name remain open.

## Storybible synchronization
- `entities/FAMILY_1554.yaml` contains the canonical named family and both grandparent lines.
- `claims/STORY_CLAIMS_FAMILY_1554.yaml` contains `STC.CLAES.EXTENDED_FAMILY.001` and updates the 1554 household/fire claims with Tanneken and Jan by name.
- `claims/SOURCE_CLAIMS_FAMILY_1540S.yaml` adds the source-weighted Jan Jansen-kuiper model claim.
- `canon/DECISIONS.yaml` contains `DEC.CLAES.EXTENDED_FAMILY.2026-08-14`.
- `canon/OPEN_DECISIONS.yaml` records the former naming/genealogy uncertainty as resolved while preserving the archival guardrails.
- `narrative/relationships.yaml` adds Claes–Tanneken and both grandparent-line relationships and renames the brother relationship to Claes–Jan.
- `storybible/FAMILY_CLAES_1542_1554.md` is the detailed canonical family dossier.
- `storybible/MASTER.md` points to the family dossier as the detailed authority where older broad prose uses generic family labels.
- `review/MIGRATION_REVIEW.yaml` now classifies 42 Story Claims, of which eight are NEW/HUMAN_DECISION.

## Validation state
The first PR validation run failed only on two mechanical issues: an out-of-vocabulary evidence status and `SYNC_PENDING`. The evidence status has been normalized to `PLAUSIBLE`, and this branch is now marked synchronized so the validator can rerun. Awaiting the new workflow result.

## Merge policy
Do not merge without explicit author instruction. Once validation passes, this branch is ready for author-approved merge.
