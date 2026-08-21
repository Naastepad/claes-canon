# Manuscript editor ingest — 19 August 2026

## Purpose

This pass synchronizes the current post-cold-reader manuscript with the Storybible's manuscript-projection layer. It does **not** rewrite historical/source canon merely because prose was cut.

## Source basis

The conversation contained paired pre-editor and post-editor Markdown files for all nineteen current chapters. The later files are treated as the current manuscript implementation for this ingest.

A dedicated machine-readable Claude `Chapter Revision Handoff` did not exist when the editing occurred; that protocol was introduced afterward. Therefore this recovery uses:

1. paired old/new chapter text;
2. recorded cold-reader/editor diagnoses from the same conversation;
3. current Storybible guardrails and explicit author decisions.

Where future disposition could not be proven as an explicit Claude instruction, the record is marked `SEMANTIC_RECONSTRUCTION` plus confidence. This avoids falsely attributing a parking decision to Claude while still preventing useful removed material from disappearing.

## File-level revision footprint

Substantive or semantic changes were found in:

- `1542-12-08-de-bladzijde.md` — major compression;
- `1547-04-01-de-drempel.md` — early religious signal/liturgical naming softened;
- `1552-01-15-de-lei.md` — arithmetic/period term/delivery causality repaired;
- `1553-08-15-het-wapen.md` — guild-ritual and hereditary-shooter overreach reduced;
- `1553-10-01-de-kraai.md` — Puttus chronology and religious-oracle role corrected;
- `1553-11-05-de-kraan.md` — explicit lifelong-secrecy foreshadow removed;
- `1553-12-10-de-wegen.md` — game geometry/count and grandfather continuity repaired;
- `1554-01-05-het-zand.md` — illness chronology/Puttus-botany overlap repaired;
- `1554-01-15-het-gist.md` — genealogy aside simplified;
- `1554-02-10-de-winnaar.md` — pregnancy corrected and Cornelis' final thesis softened;
- `1554-03-01-het-zaad-in-de-donkere-aarde.md` — major reduction of explicit role/theology exposition;
- `1554-04-10-de-wieg.md` — explicit countdown-to-disaster removed;
- `1584-07-14-de-markt-van-delft.md` — torture sequence compressed and final attention-thesis removed.

No file-content change was found in the paired editor set for:

- `1554-03-05-de-kamer.md`;
- `1564-04-04-de-ladingen-van-antwerpen.md`;
- `1564-04-14-de-verkeerde-kist.md`;
- `1564-04-22-de-kies-van-boom.md`;
- `1564-04-29-de-loog-van-antwerpen.md`;
- `1564-07-20-de-dood-van-sol.md`.

Those unchanged chapters still receive explicit **current progression** records so later writing knows what the reader has experienced.

## Major progression changes

### De Drempel

The chapter no longer functions as an early clue to Cornelis' later Familism. Its governing movement is now embodied Catholic childhood and the origin of the `sinne`. The explicit Zeven-Getijden institutional label becomes backdrop; the early Familist signal is rejected.

### Het Wapen

The chapter still converts the family sign into bodily father-son practice, but no longer needs an unsourced exact guild blessing or a nearly hereditary line of serious Nissepat shooters. Cornelis' practice remains specific and character-forming; the sign is not destiny.

### De Kraai

Puttus remains the teacher of language, distinction and evidence-based interpretation. The removed golden-vessel/anti-ritual bridge is classified as rejected for Puttus, because it made him the religious decoder of Cornelis rather than a hermeneutic mentor.

### De Winnaar

Jan still demonstrates action before full analysis. The edit stops Cornelis before he states the complete adult novel-thesis. The underlying action/choice tension is preserved as motif reserve for a later adult hinge, where it must be earned by consequence rather than transplanted as a speech.

### Het Zaad in de Donkere Aarde

This contains the largest structural improvement in the childhood cluster. The current version keeps:

- unborn life / bread / seed imagery;
- church parable;
- living Goese market;
- grey-man secrecy;
- Nissepad work-world;
- Cornelis as practical steward/biersteker;
- Tanneken as material counterknowledge;
- Cornelis' prohibition against carrying the grey man's identity.

It removes the omnibus speech that mapped the sower parable onto poorterschap, footbow, rederijkers, trust, family enterprise and direct inner Word all at once.

Two useful backlines are preserved separately:

- Cornelis' private Familist inward faith;
- family/economic stewardship pressure, with a strict biersteker/ownership guardrail.

### De Markt van Delft

The chapter still reaches the same moral/psychological bottom, but with less repeated body detail and less authorial explanation. The deleted explicit theory that trained attention cannot stop preserving painful evidence becomes a **post-Delft backline**: later chapters should demonstrate the cost through triggers, avoidance, relationship pressure and changed choices rather than repeat the thesis.

## Current cluster projection

`narrative/manuscript_progression.yaml` now contains three current reader-progressions:

- `CLUSTER.CHILDHOOD_GOES.PREFIRE.1547_1554`;
- `CLUSTER.ANTWERP_MATERIAL_INITIATION.1564`;
- `CLUSTER.DELFT_MORAL_BOTTOM.1584`.

The childhood cluster is explicitly closed to expansion until the **18 May 1554 fire + immediate aftermath + Reimerswaal decision/departure** are drafted. A new pre-fire chapter must demonstrate a missing indispensable causal/relational condition rather than merely add richness.

## Parking outcome

High-value reusable material now includes:

- Cornelis Familist private-faith backline;
- family/economic stewardship backline;
- Jan/action-without-certainty motif reserve;
- Claes post-Delft compulsive-attention backline;
- Zeven Getijden and New Laws administrative backdrop.

Rejected material now explicitly includes:

- proto-Familist Cornelis signal in 1547;
- exact unsourced Sint-Joris banner-blessing choreography;
- `Van Ongenugten Vrij` as a routine greeting convention;
- deterministic Nissepat shooter bloodline;
- Puttus as anti-ritual/proto-Reformation oracle.

This distinction prevents the common failure where every deleted good idea is treated as a future obligation.

## Current manuscript-to-canon repair flags at ingest time

The ingest surfaced several issues that remain in the **current prose** and require a later deliberate continuity repair:

1. `De Lei`: elementary master is called both Adriaen and Jacob.
2. `Het Wapen`: exact wind/touw/haak spanning apparatus is more specific than the current open mechanism boundary.
3. `De Wieg`: `three younger mouths instead of two` appears numerically inconsistent; an earlier lost child is introduced without current family canon.
4. `De Ladingen van Antwerpen`: `own beer of Claes' father` and Claes knowing `brewing` require alignment with Cornelis as biersteker rather than fixed brewer/owner.
5. `De Loog van Antwerpen` and `De Dood van Sol`: concealed-freight imagery must not become a routine books-hidden-in-beer-barrels mechanism.

These are repair flags, **not silent canon changes**.

They are now registered in `canon/OPEN_DECISIONS.yaml` as:

- `OPEN.MANUSCRIPT.DE_LEI.TEACHER_IDENTITY.001`
- `OPEN.MANUSCRIPT.HET_WAPEN.SPANNING_MECHANISM.001`
- `OPEN.MANUSCRIPT.DE_WIEG.FAMILY_STATE.001`
- `OPEN.MANUSCRIPT.CORNELIS.BIERSTEKER_WORDING.001`
- `OPEN.MANUSCRIPT.BEER_LOGISTICS_CONCEALMENT.001`

The OPEN records state the fixed canon that must survive each repair and prevent a later editor from solving a prose problem by silently changing story truth.

## 21 August 2026 closure addendum

The five records above were deliberately resolved in `canon/DECISIONS_MANUSCRIPT_SYNC_2026-08-21.yaml` and removed from the active OPEN registry:

- Jacob is the elementary master in *De Lei*;
- *Het Wapen* generalizes the exact spanning subtype;
- *De Wieg* conforms to the fixed household and has no earlier lost child;
- Cornelis remains a biersteker/intermediary rather than fixed brewer/owner;
- beer logistics do not become a routine concealed-book mechanism.

This closure also records the later fire-sequence corrections: Claes is present within the catastrophe while Cornelis is absent from the immediate zone, grandfather is present by the burial/early aftermath, Claes reaches Reimerswaal at eleven, *De Kade* must reactivate the specific *De Kraai* dread, and the catastrophe is distributed across multiple chapters. Mayken's absence from the immediate aftermath remains intentional.

The original ingest record is retained as historical evidence of what the editor pass exposed. Its OPEN list is therefore a snapshot, not the current registry.

## Synchronized files

- `narrative/manuscript_progression.yaml`
- `narrative/parked_material.yaml`
- `storybible/MANUSCRIPT_PROGRESSION_AND_PARKED_MATERIAL.md`
- `canon/OPEN_DECISIONS.yaml`
- this review record

## Next editorial use

A future Claude/editor session must load `03_WRITING_EDITORIAL`, which contains the manuscript projection/parking registers, and `01_CORE_CANON`, which contains the active OPEN registry, before writing/revising after the cold-read stage. It must use the current chapter progression as reader-state truth and treat `PARK.*` records as reserves with no right of return.

## Audit state

- progression ingest: **COMPLETE**
- parked/rejected classification: **COMPLETE**, with explicit `SEMANTIC_RECONSTRUCTION` provenance where a verbatim historical Claude handoff was unavailable
- manuscript repair conflicts at ingest time: **REGISTERED AS OPEN**; **CLOSED 21 AUGUST 2026** by `canon/DECISIONS_MANUSCRIPT_SYNC_2026-08-21.yaml`
- canon de-canonization caused by prose deletion: **NONE**
- merge to `main` at ingest time: **NOT PERFORMED**; PR #18 was later merged on 21 August 2026
