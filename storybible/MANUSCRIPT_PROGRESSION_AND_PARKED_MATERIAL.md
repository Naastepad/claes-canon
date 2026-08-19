# Manuscriptprogressie, cuts en geparkeerd materiaal

**Status:** GOVERNING EDITORIAL / MANUSCRIPT-PROJECTION MODULE  
**Date:** 19 August 2026  
**Machine registers:** `narrative/manuscript_progression.yaml`, `narrative/parked_material.yaml`  
**Editorial gates:** `GRD.EDITORIAL.CLUSTER_NECESSITY`, `GRD.EDITORIAL.CUT_DISPOSITION`

## 1. Why this layer exists

The Storybible must distinguish **what is true in the novel** from **where and how the current manuscript tells it**.

A cold-reader/editor pass can correctly remove a passage because it slows the book, repeats a lesson, explains too much or spends a motif too early. That editorial decision does not automatically mean that the underlying fact, relationship history or world condition is no longer canon.

Conversely, a deleted passage must not continue to function as if the reader has seen it merely because an earlier draft contained it.

Therefore this repository now separates:

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

This prevents a common failure in iterative writing: an older chapter summary continues to claim that a chapter establishes something which the current prose no longer contains.

## 3. Four different kinds of off-page material

### Backstory

A past event or state that **is part of the character/story reality** and has causal force, even if the novel does not dramatize it as a full scene.

Example form:

> Claes already learned a household practice before the current chapter; the scene proving every step was cut, but the competence remains canonically acquired.

Backstory therefore normally points to existing `STC.*`, `REL.*`, `ENT.*` or `ARC.*` state.

### Backline

An **off-page causal line continuing during the story**. It may later collide with the foreground plot.

Examples in this project can include trade obligations, Cornelis' hidden network activity, political/religious developments or Mayken's independent adult life when Claes is elsewhere.

A backline is not atmosphere. Something is changing while the camera is away.

### Backdrop

Historical, social, material or sensory world information available for later scene texture but **not itself a required causal event**.

Market activity, guild habits, seasonal food, urban sounds or a feast practice may move from a cut picturesque passage into backdrop. The writer can then distribute selected details through later action without resurrecting the original exposition block.

### Parked future scene material

A written or designed beat whose future location is **not yet decided**. It is not active in the manuscript until a receiving chapter passes scene/cluster necessity and explicitly adopts it.

## 4. Cut is not one thing

After a `CUT` or `MERGE`, the editor must classify every meaningful removed function:

- `MOVED_ELSEWHERE` — a receiving chapter is fixed;
- `PARKED_FUTURE_CHAPTER` — may become a later scene;
- `PARKED_BACKSTORY` — happened/formed character but need not be shown;
- `PARKED_BACKLINE` — continues off-page and can create later consequences;
- `PARKED_BACKDROP` — reusable world texture;
- `PARKED_MOTIF_RESERVE` — motif removed here to protect freshness and saved for a changed-value recurrence;
- `DISCARDED_PROSE` — wording/scene gone; underlying truth checked separately;
- `REJECTED_STORY_OPTION` — the underlying proposed story choice itself is rejected.

This classification belongs in `narrative/parked_material.yaml`.

## 5. Canon impact is a separate field

Every editorial move gets one of three canon-impact labels:

### `NONE`

Only prose changed. No Story Claim, entity state, relationship fact or Narrative Instance truth is affected.

### `PROJECTION_ONLY`

The fact remains story truth, but the place where the reader learns/sees it has changed or become off-page. Update manuscript progression, scene projection and possibly knowledge/reveal timing.

### `CANON_REVIEW_REQUIRED`

The cut means a previously canonized event no longer happens, a relationship history changes, an object is no longer transferred, a character can no longer possess knowledge, or another true continuity dependency changes. This requires an explicit author decision before canon is rewritten.

An editor must never infer `CANON_REVIEW_REQUIRED -> de-canonize` automatically.

## 6. Revision lineage and current manuscript authority

The conversation contains earlier and later versions of multiple chapters from the 19 August pass. The existence of those paired versions establishes **revision lineage**, but file-size or text-diff alone is not enough to infer the author's intended disposition of every removed beat.

Therefore:

- the latest approved chapter file is the current prose implementation;
- the progression register says what that current prose now does;
- the editor handoff says what was deliberately cut/moved/parked and why;
- the parking register preserves reusable function/material;
- canon remains governed independently.

When an editor handoff and a raw diff disagree about intent, the explicit author/editor disposition wins. A diff shows deletion; it does not by itself tell whether the deleted material became backstory, backdrop, future-scene reserve or rejected story.

## 7. Cluster progression

The childhood sequence exposed why scene-level uniqueness alone is insufficient. Each chapter can individually contain useful material while the cluster as a whole repeats the same learning beat, father-son recognition beat or molenbord function too often.

After individual scene necessity, perform `GRD.EDITORIAL.CLUSTER_NECESSITY`:

- What has Claes already learned?
- What has the reader already understood about the relationship?
- Has this motif changed value or merely repeated?
- Does this chapter create new forward pressure?
- If removed, is the cluster truly poorer or merely shorter?

The **current progression record must describe the post-edit cluster**, not preserve the ambitions of earlier drafts.

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

The handoff should summarize removed material; it need not reproduce entire deleted passages.

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

## 10. Initial legacy parked material

The registry currently preserves several earlier known examples:

- a first-steps/home scene — potentially useful but unplaced;
- an aesthetically successful Vastenavond/market scene — better treated as world/backdrop unless later causally earned;
- an explicit Claes-birth/Brevísima date-link — rejected and not available for resurrection.

The 19 August Claude cold-reader/editor pass must be ingested into the same format from its explicit editorial handoff. The paired manuscript files already prove that revision occurred; the semantic disposition should come from the editor's stated reasons and parking decisions, not be guessed from file deletion alone.
