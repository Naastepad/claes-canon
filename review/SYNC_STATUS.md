# Synchronization status

Status: `SYNC_COMPLETE`

Release state: `MAIN_CANONICAL`

PR #5 and PR #6 are merged. `main` is the canonical source of truth for the integrated Goes fire/family rupture, Tanneken Jansdochter, Jan Corneliszn. Nissepat and both grandparent lines.

## Canonical family state
- mother: **Tanneken Jansdochter**, fictional, born approximately 1519–1522 / preferred ca. 1520, dies 18 May 1554;
- younger brother: **Jan Corneliszn. Nissepat**, fictional, born approximately June 1544, about eighteen months younger than Claes, dies 18 May 1554;
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
- The 1554 loss of the specific Nissepat household and its casualties remain novel canon grounded in the historically supported partially burned Nieuwstraat/Armenhoek environment, not archival victim/property proof.

## Storybible synchronization
- `entities/FAMILY_1554.yaml` contains the canonical named family and both grandparent lines.
- `claims/STORY_CLAIMS_FAMILY_1554.yaml` contains `STC.CLAES.EXTENDED_FAMILY.001` and the named 1554 household/fire claims.
- `claims/SOURCE_CLAIMS_FAMILY_1540S.yaml` contains the source-weighted Jan Jansen-kuiper model claim.
- `canon/DECISIONS.yaml` contains `DEC.CLAES.EXTENDED_FAMILY.2026-08-14`.
- `canon/OPEN_DECISIONS.yaml` records former naming/genealogy uncertainty as resolved while preserving archival guardrails.
- `narrative/relationships.yaml` contains Claes–Tanneken, Claes–Jan and both grandparent-line relations.
- `storybible/FAMILY_CLAES_1542_1554.md` is the detailed canonical family dossier.
- `storybible/MASTER.md` points to the family dossier as detailed authority where older prose remains generic.
- `review/MIGRATION_REVIEW.yaml` classifies 42 Story Claims, of which eight are NEW/HUMAN_DECISION.

## Validation and merge state
- PR #5 was previously merged as `0f7f8778acc6437ad9a16bb8ffda9aa6625c375c` after its validated family-fire synchronization.
- PR #6 passed **Validate Claes canon repository**, workflow run **146**, on head `f32f6e1720df97323a89b340dbdb4c637cfb39de`.
- PR #6 was merged on explicit author instruction as `3aa883f64f68469188285b8d8d9a63b2c66fa54b`.

## Remaining open matters
The authoritative list is `canon/OPEN_DECISIONS.yaml`. Resolved records are retained there for audit history and must not be counted as active open decisions.

## Lemma execution policy
- `lemma/*.lemma` remains the deterministic rules-as-code layer and is versioned and validated in GitHub.
- GitHub `main` is authoritative for both Storybible content and Lemma source.
- LemmaBase is optional and downstream-only; it never overrides GitHub canon.
