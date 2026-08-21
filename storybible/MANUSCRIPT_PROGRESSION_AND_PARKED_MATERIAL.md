# Manuscriptprogressie, cuts en geparkeerd materiaal

**Status:** GOVERNING EDITORIAL / MANUSCRIPT-PROJECTION MODULE  
**Date:** 19 August 2026  
**Machine registers:** `narrative/manuscript_progression.yaml`, `narrative/parked_material.yaml`  
**Editorial gates:** `GRD.EDITORIAL.CLUSTER_NECESSITY`, `GRD.EDITORIAL.CUT_DISPOSITION`

## 1. Why this layer exists

The Storybible must distinguish **what is true in the novel** from **where and how the current manuscript tells it**.

A cold-reader/editor pass can correctly remove a passage because it slows the book, repeats a lesson, explains too much or spends a motif too early. That editorial decision does not automatically mean that the underlying fact, relationship history or world condition is no longer canon.

Conversely, a deleted passage must not continue to function as if the reader has seen it merely because an earlier draft contained it.

Therefore this repository separates:

1. **Canon / story truth** — `DEC.*`, `STC.*`, entities, objects, relationships and historical-fiction decisions.
2. **Current manuscript projection** — which chapter currently dramatizes which movement, reveal, relationship beat and reader progression.
3. **Parked narrative material** — useful removed material not currently active on-page.
4. **Rejected material** — prose or story choices that must not quietly return.

## 2. Chapter progression is versioned

For each substantive editorial pass, `narrative/manuscript_progression.yaml` records the chapter's progression before and after the pass.

A useful progression record answers:

- what state does the reader/POV character enter with?
- what pressure/choice/revelation actually occurs in the current version?
- what relationship/knowledge/value changes?
- what expectation is handed to the next chapter?
- what function was removed, compressed or moved?
- did the edit alter canon, or only its placement/delivery?

The essential fields are:

`progression_before -> progression_after -> progression_delta`

This prevents an older chapter summary from continuing to claim that a chapter establishes something which the current prose no longer contains.

## 3. Four different kinds of off-page material

### Backstory

A past event or state that **is part of the character/story reality** and has causal force, even if the novel does not dramatize it as a full scene. Backstory normally points to existing `STC.*`, `REL.*`, `ENT.*` or `ARC.*` state.

### Backline

An **off-page causal line continuing during the story**. It may later collide with the foreground plot. Trade obligations, Cornelis' hidden network, political/religious developments or Mayken's independent adult life can operate this way.

### Backdrop

Historical, social, material or sensory world information available for later scene texture but **not itself a required causal event**. Backdrop should normally be distributed through later action rather than resurrected as an exposition block.

### Parked future scene material

A written or designed beat whose future location is **not yet decided**. It is not active in the manuscript until a receiving chapter passes scene/cluster necessity and explicitly adopts it.

## 4. Cut is not one thing

After a `CUT` or `MERGE`, the editor classifies every meaningful removed function:

- `MOVED_ELSEWHERE` — a receiving chapter is fixed;
- `PARKED_FUTURE_CHAPTER` — may become a later scene;
- `PARKED_BACKSTORY` — happened/formed character but need not be shown;
- `PARKED_BACKLINE` — continues off-page and can create later consequences;
- `PARKED_BACKDROP` — reusable world texture;
- `PARKED_MOTIF_RESERVE` — motif removed here to protect freshness and saved for a changed-value recurrence;
- `DISCARDED_PROSE` — wording/scene gone; underlying truth checked separately;
- `REJECTED_STORY_OPTION` — the underlying proposed story choice itself is rejected.

The classification belongs in `narrative/parked_material.yaml`.

## 5. Canon impact is a separate field

Every editorial move gets one of three canon-impact labels:

### `NONE`
Only prose changed. No Story Claim, entity state, relationship fact or Narrative Instance truth is affected.

### `PROJECTION_ONLY`
The fact remains story truth, but the place where the reader learns/sees it has changed or become off-page. Update manuscript progression, scene projection and possibly knowledge/reveal timing.

### `CANON_REVIEW_REQUIRED`
The cut means a previously canonized event may no longer happen, a relationship history changes, an object is no longer transferred, a character can no longer possess knowledge, or another true continuity dependency changes. This requires an explicit author decision before canon is rewritten.

An editor must never infer `CANON_REVIEW_REQUIRED -> de-canonize` automatically.

## 6. Revision lineage and manuscript authority

- the latest approved chapter file is the current prose implementation;
- `narrative/manuscript_progression.yaml` says what that current prose now does;
- the editor handoff/revision record says what was deliberately cut, compressed, repaired or moved;
- `narrative/parked_material.yaml` preserves reusable function/material;
- canon remains governed independently.

A raw diff shows deletion but cannot by itself prove whether a deleted element became backstory, backline, backdrop, future reserve or rejected story.

## 7. Cluster progression

Scene-level uniqueness is insufficient when a group of individually useful scenes repeats the same lesson, recognition beat or motif value.

After individual scene necessity, perform `GRD.EDITORIAL.CLUSTER_NECESSITY`:

- What has Claes already learned?
- What has the reader already understood about the relationship?
- Has this motif changed value or merely repeated?
- Does this chapter create new forward pressure?
- If removed, is the cluster truly poorer or merely shorter?

The current progression registry now includes governing projections for:

- `CLUSTER.CHILDHOOD_GOES.PREFIRE.1547_1554`;
- `CLUSTER.ANTWERP_MATERIAL_INITIATION.1564`;
- `CLUSTER.DELFT_MORAL_BOTTOM.1584`.

## 8. Claude/editor handoff requirement

After a cold-read/editor pass, Claude must not simply return edited files. It must also output a structured **Chapter Revision Handoff** for Storybible synchronization.

For every changed chapter:

1. chapter/file;
2. editorial verdict;
3. progression before;
4. progression after;
5. exact progression delta;
6. functions retained;
7. functions cut or moved;
8. parking classification for each reusable removed function;
9. receiving chapter if moved;
10. canon impact (`NONE / PROJECTION_ONLY / CANON_REVIEW_REQUIRED`);
11. changed reader expectation/cluster effect;
12. any `OPEN.*` accidentally approached or newly exposed.

The handoff summarizes removed material; it does not need to preserve deleted prose verbatim.

## 9. Reuse rule

Parked material has **no right of return**.

Before reuse it must again pass:

- current canon/chronology;
- character knowledge and object state;
- scene necessity;
- cluster necessity;
- motif freshness;
- reader-experience need.

A passage is not restored because it was expensive to research, beautifully written or once approved.

## 10. 19 August cold-reader/editor ingest — completed

The pre-editor and post-editor versions of the current chapter set have now been semantically compared and ingested into `narrative/manuscript_progression.yaml` and `narrative/parked_material.yaml`.

Because the handoff protocol did not yet exist when that Claude pass was performed, this recovery distinguishes two provenance levels:

- **HIGH confidence:** paired drafts plus an explicit recorded editorial/canon reason identify the intended change;
- **MEDIUM confidence / `SEMANTIC_RECONSTRUCTION`:** the paired drafts establish what changed and the surrounding editorial reasoning supports a safe disposition, but a verbatim machine-readable Claude parking instruction was not available.

Do not silently upgrade MEDIUM reconstructed parking to an explicit historical Claude instruction. If the original handoff is later supplied, reconcile it with these records.

The ingest records substantive revision histories for:

- *De Bladzijde*;
- *De Drempel*;
- *De Lei*;
- *Het Wapen*;
- *De Kraai*;
- *De Kraan*;
- *De Wegen*;
- *Het Zand*;
- *Het Gist*;
- *De Winnaar*;
- *Het Zaad in de Donkere Aarde*;
- *De Wieg*;
- *De Markt van Delft*.

*De Kamer* and the five 1564 material-initiation chapters were unchanged in that file pass and therefore receive current progressions but no artificial revision delta.

## 11. High-value parked/backline results from this pass

The most important reusable items are not the longest deleted passages but the ones that still carry future causal value:

- `PARK.ZAAD.CORNELIS_FAMILIST_BACKLINE.001` — Cornelis' private inward faith remains canon but was correctly removed from an over-explicit child-facing sermon; deepen later through network, adult conversation, text or consequence.
- `PARK.ZAAD.FAMILY_STEWARDSHIP_BACKLINE.001` — family/economic stewardship pressure may matter later, especially post-fire or during Goes severance, but reuse must respect Cornelis' biersteker/ownership boundary.
- `PARK.WINNAAR.ACTION_WITHOUT_CERTAINTY_RESERVE.001` — Jan's action principle is saved as a changed-value motif/choice reserve, not as a speech to transplant.
- `PARK.DELFT.ATTENTION_BACKLINE.001` — the deleted explanation that trained attention cannot stop is now a post-Delft behavioural backline; later prose should show the consequence rather than repeat the thesis.
- `PARK.DREMPEL.ZEVEN_GETIJDEN_BACKDROP.001` and `PARK.PROLOGUE.NEW_LAWS_ADMIN_CONTEXT.001` — useful world/history texture that no longer belongs in the current foreground delivery.

Several other cuts are explicitly `REJECTED_STORY_OPTION`, especially a 1547 proto-Familist Cornelis signal, an unsupported exact Sint-Joris banner-blessing ritual, devies-as-routine-greeting, hereditary Nissepat shooter determinism and Puttus as anti-ritual religious oracle. Those are **not** parked ideas waiting to return.

## 12. Manuscript-to-canon repairs resolved on 21 August 2026

`canon/DECISIONS_MANUSCRIPT_SYNC_2026-08-21.yaml` closes the five ingest flags without promoting them into five equal creative questions:

- *De Lei*: use Meester Jacob; Puttus remains the separate Latin/humanist master.
- *Het Wapen*: preserve the bodily spanning sequence but generalize the exact apparatus subtype.
- *De Wieg*: preserve the fixed family of Claes, Jan and the unborn child; remove the extra-mouth arithmetic and the unestablished earlier lost child.
- *Het Zaad* and *De Ladingen van Antwerpen*: present Cornelis as biersteker/intermediary, not fixed brewery owner or master brewer.
- *De Loog van Antwerpen* and *De Dood van Sol*: preserve logistics resonance but remove routine books-hidden-in-beer-casks implications.

The same sync fixes the manuscript projection around the 1554 sequence:

- Claes directly experiences the fire; Cornelis is absent from its immediate zone.
- Claes Jacobsz. is present by the burial/early aftermath and helps with practical arrangements; temporary lodging with his sister does not erase him.
- *De Kade* must pay off the specific Reimerswaal dread planted in *De Kraai*.
- Claes reaches Reimerswaal at eleven and turns twelve on 8 December 1554.
- the fire, confirmation, aftermath and departure form a multi-chapter sequence.

Mayken's absence from the immediate aftermath is intentional continuity, not a repair target. The later manuscript files for the fire sequence and *De Kade* are outside this repository; this file records the binding projection and does not falsely certify sentence-level application in those external files.
