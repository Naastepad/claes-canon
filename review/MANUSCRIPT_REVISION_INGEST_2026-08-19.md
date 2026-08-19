# Manuscript Revision Ingest Audit — 19 August 2026

**Status:** EDITORIAL INGEST / BRANCH AUDIT  
**Branch:** `agent/ingest-editor-progression-2026-08-19`  
**Scope:** current 19-chapter manuscript set, paired pre-editor/post-editor drafts, recovered Claude cold-reader/editor reasoning

## Purpose

This audit records what the 19 August editor pass changed **as manuscript projection**, without treating every deleted sentence as a canon change and without allowing useful cut material to disappear into chat history.

The governing machine registers are:

- `narrative/manuscript_progression.yaml`
- `narrative/parked_material.yaml`
- `canon/OPEN_DECISIONS.yaml`

The governing explanation is:

- `storybible/MANUSCRIPT_PROGRESSION_AND_PARKED_MATERIAL.md`

## Provenance rule

The original editor pass pre-dated the repository's structured **Chapter Revision Handoff** requirement. Recovery therefore used:

1. paired old/new chapter files from the conversation;
2. recorded editor/cold-reader comments and author decisions from the same workstream;
3. current canon guardrails only to classify the meaning of a cut, never to invent a missing historical editor instruction.

Two provenance classes are used:

- **HIGH / paired drafts plus explicit editorial or canon reason** — intended change is recoverable with high confidence;
- **MEDIUM / `SEMANTIC_RECONSTRUCTION`** — the text delta is clear and a safe editorial disposition can be reconstructed, but a verbatim historical Claude parking instruction is unavailable.

A later verbatim Claude handoff may refine a MEDIUM item. It must not silently duplicate or override the recovered item.

## Chapter-set result

### Current progressions recorded

All 19 chapters in the supplied set now have a current manuscript progression:

1. *De Bladzijde* — 1542-12-08
2. *De Drempel* — 1547-04-01
3. *De Lei* — 1552-01-15
4. *Het Wapen* — 1553-08-15
5. *De Kraai* — 1553-10-01
6. *De Kraan* — 1553-11-05
7. *De Wegen* — 1553-12-10
8. *Het Zand* — 1554-01-05
9. *Het Gist* — 1554-01-15
10. *De Winnaar* — 1554-02-10
11. *Het Zaad in de Donkere Aarde* — 1554-03-01
12. *De Kamer* — 1554-03-05
13. *De Wieg* — 1554-04-10
14. *De Ladingen van Antwerpen* — 1564-04-04
15. *De Verkeerde Kist* — 1564-04-14
16. *De Kies van Boom* — 1564-04-22
17. *De Loog van Antwerpen* — 1564-04-29
18. *De Dood van Sol* — 1564-07-20
19. *De Markt van Delft* — 1584-07-14

### Substantive revision histories recorded

Revision deltas were added for the chapters where the paired versions materially changed story delivery:

- *De Bladzijde*
- *De Drempel*
- *De Lei*
- *Het Wapen*
- *De Kraai*
- *De Kraan*
- *De Wegen*
- *Het Zand*
- *Het Gist*
- *De Winnaar*
- *Het Zaad in de Donkere Aarde*
- *De Wieg*
- *De Markt van Delft*

*De Kamer* and the five 1564 material-initiation chapters retain current progression records but were not given artificial change histories where the supplied file pass did not support one.

## High-value editorial effects

### 1. Early religious interpretation was delayed

*De Drempel* no longer asks a four-year-old scene to carry a proto-Familist Cornelis signal. *De Kraai* no longer lets Puttus become an anti-ritual/religious decoder. *Het Zaad* no longer lets Cornelis explain his private theology to eleven-year-old Claes in a complete sermon.

**Effect:** the reader can notice religious dissonance later without being handed its solution before the story has earned it.

### 2. Cornelis was pulled back from Storybible-spokesman dialogue

The largest cut in *Het Zaad* removes the all-in-one mapping of poorterschap, voetboog, rederijker life, trust, family enterprise and inward faith onto the sower parable.

**Effect:** Cornelis remains a character with multiple lived identities. He no longer explains the novel's architecture from inside the scene.

### 3. The Claes/Jan contrast remains embodied rather than theorized

*De Winnaar* still demonstrates Jan's action-first cognition against Claes' deliberation, but Cornelis' full adult maxim about acting before certainty was cut.

**Effect:** `PARK.WINNAAR.ACTION_WITHOUT_CERTAINTY_RESERVE.001` preserves the changed-value future function without licensing a transplanted speech.

### 4. Guild/family symbolism was disciplined by evidence

*Het Wapen* keeps the Nissepat voetboog sign, Cornelis' fictional Sint-Joris membership and father-son training, while removing or softening an unsupported exact banner-blessing ritual, devies-as-routine-greeting and deterministic shooter lineage.

**Effect:** historical institution + fiction character bridge remains strong without pseudo-documentary ritual detail.

### 5. Delft now ends in consequence rather than explanation

The revised *Markt van Delft* compresses repeated tong beats and removes the final explicit theory that trained attention cannot stop archiving unbearable evidence.

**Effect:** the bodily trigger and post-execution behaviour carry the trauma. `PARK.DELFT.ATTENTION_BACKLINE.001` preserves the later causal consequence.

## Parked/backline material that must not be lost

The highest-value future-use records are:

- `PARK.ZAAD.CORNELIS_FAMILIST_BACKLINE.001` — Cornelis' private inward faith remains story truth; later reveal by action/network/consequence, not the deleted child-facing sermon.
- `PARK.ZAAD.FAMILY_STEWARDSHIP_BACKLINE.001` — possible family/economic pressure, guarded by the biersteker/ownership boundary.
- `PARK.WINNAAR.ACTION_WITHOUT_CERTAINTY_RESERVE.001` — Jan's action principle available for a later changed-value adult choice.
- `PARK.DELFT.ATTENTION_BACKLINE.001` — post-Delft compulsive attention should be shown behaviourally.
- `PARK.DREMPEL.ZEVEN_GETIJDEN_BACKDROP.001` — liturgical/world backdrop available outside four-year-old terminology.
- `PARK.PROLOGUE.NEW_LAWS_ADMIN_CONTEXT.001` — historical context reserve, not a mandate to restore exposition.

## Rejected material that must not return accidentally

The following are explicitly **not** future-scene reserves:

- `PARK.DREMPEL.EARLY_FAMILIST_SIGNAL.001`
- `PARK.WAPEN.BANNER_BLESSING_RITUAL.001`
- `PARK.WAPEN.DEVISE_GREETING_CONVENTION.001`
- `PARK.WAPEN.HEREDITARY_SHOOTER_CHAIN.001`
- `PARK.KRAAI.PUTTUS_ANTI_RITUAL_PROMPT.001`

They may only return after an explicit author decision that reopens the rejected story option or after new evidence changes the historical boundary.

## Newly exposed manuscript-continuity OPEN items

The ingest exposed five issues that are not solved by the editor pass itself and are now tracked in `canon/OPEN_DECISIONS.yaml`:

1. `OPEN.MANUSCRIPT.DE_LEI.TEACHER_IDENTITY.001` — Adriaen/Jacob elementary-master inconsistency.
2. `OPEN.MANUSCRIPT.HET_WAPEN.SPANNING_MECHANISM.001` — exact wind/touw/haak reconstruction versus a generalized description.
3. `OPEN.MANUSCRIPT.DE_WIEG.FAMILY_STATE.001` — incorrect younger-mouth count and unsupported earlier lost child.
4. `OPEN.MANUSCRIPT.CORNELIS.BIERSTEKER_WORDING.001` — wording that can accidentally promote Cornelis from biersteker to brewery owner/master brewer.
5. `OPEN.MANUSCRIPT.BEER_LOGISTICS_CONCEALMENT.001` — metaphorical vessel/secrecy language drifting into a routine books-in-beer-barrels mechanism.

These are **repair decisions**, not evidence that canon has already changed.

## Cluster-level result

### Childhood Goes, pre-fire 1547–1554

The cluster now progresses from embodied world -> observation as competence -> responsibility/trust -> bodily discipline -> disciplined interpretation -> brotherly action -> future-path cognition -> public mastery/Mayken's distinct knowledge -> Tanneken's embodied knowledge -> Jan's challenge to mastery -> secret paternal world -> Cornelis as independent social person -> materially specific unborn future.

The next required hinge is the **18 May 1554 fire and immediate aftermath**. No further pre-fire chapter should be added merely because another childhood scene is attractive.

### Antwerp material initiation, 1564

The sequence now reads as competence/silence -> wrong-kist verification -> Boom recognition -> duration/labour -> visible disappearance of Sol.

It should not resolve the adult macro-Nigredo before the fixed **4 October 1564** security break.

### Delft, 1584

Delft is preserved as moral/psychological bottom: public violence reactivates paternal execution memory; signs/prints lose moral neutrality; the body continues to witness after the scene ends.

Later recovery must therefore include **release**, not only more accurate interpretation.

## Forward-use rule for Claude/other editors

For any later hard edit:

1. read current canon + dated decisions;
2. read `narrative/manuscript_progression.yaml` and `narrative/parked_material.yaml`;
3. revise prose;
4. return a Chapter Revision Handoff for every changed chapter;
5. classify every meaningful cut as moved / backstory / backline / backdrop / motif reserve / discarded / rejected;
6. never infer de-canonization from deletion;
7. never restore parked material solely because it was once written.

## Audit state

- progression ingest: **COMPLETE**
- parked/rejected classification: **COMPLETE WITH EXPLICIT MEDIUM-PROVENANCE FLAGS WHERE NECESSARY**
- manuscript/canon repair issues: **REGISTERED AS OPEN**
- merge to `main`: **NOT PERFORMED**
