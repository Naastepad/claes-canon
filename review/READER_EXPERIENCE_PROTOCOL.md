# Reader Experience Protocol — Claes

**Status:** CURRENT AUTHORING / REVIEW AUTHORITY  
**Round:** D — reader experience, pacing and editorial feedback  
**Date:** 16 August 2026

This protocol governs how prose is tested for **reader experience** after continuity, history and story causality are established. It does not create canon. It tests whether the novel actually communicates and affects a reader as intended.

## 1. Core distinction

The Storybible records what is true, possible, known and causally intended. The reader only receives the prose.

Therefore:

> **Authorial intention and reader experience are different evidence streams.**

A Storybible explanation cannot rescue prose that leaves a cold reader confused for the wrong reason, emotionally detached, bored, falsely oriented or unaware of the intended turn.

Designed ambiguity is allowed. Accidental confusion about basic causality, motivation, spatial relation or chronology is not automatically sophisticated ambiguity.

## 2. Three review modes

### A. Editorial diagnosis

The editor reads with canon/story context available and asks whether the scene is structurally necessary, causally sound, paced correctly and written with sufficient prose quality.

Use `GRD.EDITORIAL.SCENE_NECESSITY`, `GRD.EDITORIAL.PROSE_QUALITY`, `GRD.EDITORIAL.PACING` and `GRD.EDITORIAL.RUTHLESS_EDITOR`.

### B. Cold-reader pass

The cold reader receives **the literary text**, plus only the front matter a real reader would already have. Do not preload the Storybible, scene intention, hidden symbolism or historical explanation.

A cold-reader pass must answer:

1. What happened?
2. What did the viewpoint character want?
3. What changed by the end?
4. What is clear?
5. What remains uncertain in an interesting way?
6. What is confusing or requires rereading for the wrong reason?
7. Where did attention rise, sag or break?
8. What do you expect, hope or fear next?
9. What image, action, line or relationship beat remains in memory?
10. If you stopped reading here, why?

An AI may simulate a cold reader only when it is denied the hidden authorial explanation. **AI simulation is not a substitute for real readers.**

### C. Human pilot-reader pass

Use actual readers at deliberate milestones. Do not coach them toward the intended interpretation before they read.

Useful milestones:

- after a structurally meaningful chapter cluster exists;
- after a complete act/book section or equivalent major arc movement exists;
- after a full draft, before final line polish.

Different readers can reveal different failure modes. A general fiction reader may detect boredom or emotional opacity that a historical specialist overlooks; a historically knowledgeable reader may detect world-view leakage or implausible behaviour that a general reader accepts. Do not require every reader to solve every class of problem.

## 3. What to measure

Reader experience should be tracked across at least these dimensions:

- **orientation** — can the reader tell who, where and roughly when without unnecessary explanation?
- **curiosity** — is there an active question or desire to continue?
- **emotional investment** — does the reader care about a person, choice, cost or loss?
- **tension / anticipation** — does pressure accumulate before the turn?
- **cognitive load** — is complexity productive or merely exhausting?
- **surprise and inevitability** — after a turn, does it feel both non-obvious and earned?
- **payoff** — does a planted object, motif, relationship or question return with changed value?
- **memory** — what survives after the reader closes the text?

Do not optimize every scene for maximum intensity. Contrast is necessary. A quiet scene can succeed through intimacy, dread, orientation, grief, recovery or altered expectation, provided it still changes the reader's relationship to what follows.

## 4. Reader evidence versus reader solutions

A reader saying **“I stopped caring here”**, **“I thought Cornelis owned the brewery”**, **“I did not understand why Mayken stayed”** or **“this reveal felt obvious”** is evidence about experience.

A reader saying **“delete chapter 4”**, **“make Mayken explain it”** or **“add a chase”** is a proposed solution.

Record both, but keep them separate.

Rule:

> **Trust repeated independent reports of the problem more than any single proposed fix.**

One isolated preference may be taste. Multiple independent readers stumbling over the same causal link, pacing trough or false inference is a strong revision signal.

## 5. Feedback convergence

Classify observations as:

- `ISOLATED` — one reader, no corroboration yet;
- `REPEATED` — same issue appears independently more than once;
- `CONVERGENT` — different readers describe different symptoms pointing to the same underlying problem;
- `RESOLVED` — revision has been retested and the problem no longer reproduces materially;
- `INTENTIONAL_VARIANCE` — readers differ, but the range is acceptable and does not obstruct the scene's required function.

Never use majority vote to decide canon or theme. Reader evidence tests delivery, not truth-by-poll.

## 6. Scene retention decision

Every scene is tested on four necessity dimensions:

1. **Plot necessity** — causes, prevents, reveals or materially changes a later event, decision, obligation or risk.
2. **Character necessity** — contains a consequential choice, revelation, value shift, relationship shift or self-revelation.
3. **Information necessity** — delivers information the reader needs for a later turn or consequence, in a time/place/form that is difficult to improve elsewhere.
4. **Reader-experience necessity** — creates a necessary experience such as tension, dread, intimacy, relief, wonder, orientation, anticipation, surprise or designed disorientation with later payoff.

Then apply the **uniqueness test**:

> A scene is not retained merely because it is useful. If all useful functions can be performed better elsewhere, the scene should not remain a separate scene.

Editorial verdicts:

- **RETAIN** — indispensable function and already the strongest available place/form.
- **REVISE** — indispensable function, but execution is weak.
- **MERGE** — necessary material duplicates another scene or will gain force when combined.
- **CUT** — no indispensable function, or every function is better served elsewhere.

Historical richness, research effort, symbolic neatness, an attractive passage or personal attachment to a scene is not an independent retention category.

## 7. Pacing test

Pacing is allocation of reader attention, not simply speed.

Expand around:

- irreversible choice;
- sensory recognition that changes understanding;
- danger;
- intimacy;
- moral hesitation;
- costly consequence;
- a turn whose effect must be felt rather than merely reported.

Compress:

- routine movement;
- repeated explanation;
- setup already understood;
- world detail that does not affect action or inference;
- procedural steps whose dramatic information has already been delivered.

A useful scene pulse is:

**expectation → pressure/complication → turn → altered forward pressure**.

This can be quiet. Escalation means increasing difficulty, consequence or conflict of values, not simply louder events.

Chapter endings need **forward pressure**, not mandatory cliffhangers.

## 8. Prose-quality test

Line-level prose is judged after the scene's dramatic function is clear. Do not polish a scene that should be cut.

Check:

- viewpoint specificity;
- concrete nouns and verbs before explanatory abstraction;
- sentence and paragraph rhythm appropriate to action/perception;
- selective sensory detail with cognitive or dramatic function;
- absence of research-display paragraphs;
- metaphors generated from the scene's material/emotional field rather than stacked decoration;
- readable but historically non-modern dialogue/worldview;
- entry without unnecessary runway;
- exit without recap.

A beautiful sentence inside a structurally unnecessary scene is still a cut candidate.

## 9. The ruthless-editor mode

**Mode name:** `Meedogenloze redacteur`.

Instruction:

> **Niet aardig, wel precies. Als een scène niet werkt, zeg dat. Geen complimenten en geen verzachtende formuleringen wanneer die de diagnose vertroebelen.**

The purpose is not hostility. It is to remove social cushioning from editorial diagnosis.

Required review order:

1. verdict in one sentence;
2. whether the scene is necessary;
3. the primary/fatal problem;
4. causality and character choice;
5. pacing and reader experience;
6. prose quality;
7. continuity/historical risk, if any;
8. **RETAIN / REVISE / MERGE / CUT**;
9. the smallest revision that would materially improve the scene, if revision is warranted.

Do not praise accurate research as compensation for weak fiction. A historically correct scene can still fail dramatically.

## 10. Feedback loop

Reader testing is iterative:

`draft -> editorial diagnosis -> cold-reader pass -> revision -> human pilot read at milestone -> convergence analysis -> targeted revision -> retest`

Do not collect feedback indefinitely. Stop a loop when the scene or chapter performs its required function reliably and remaining differences are taste rather than repeated failure.

Use `review/READER_FEEDBACK_TEMPLATE.md` for a consistent record.
