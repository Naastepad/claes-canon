# Claude Context Pack — FULL — GENERATED

> Generated projection; never edit by hand. GitHub source files remain authoritative.
> Treat each SOURCE FILE section as the original source file.

- source branch: `main`
- source commit at generation: `f541df06f3c3b0fe8f4d058edd060926091f7e19`
- generated UTC: `2026-08-16T19:20:27+00:00`
- included files: `44`

Apply the authority hierarchy from `AI_ONBOARDING.md`. Physical order in this pack does not alter authority.

---

# SOURCE FILE: `README.md`

```markdown
# Claes Canon / Storybible — AI Gateway

Lemma-based, McKee/NOS-inspired operating Storybible and canon-control system for the Claes project.

**`main` is the canonical source of truth and canonical storage.** PR #1 has been merged; `authoring/v1` and the former draft PR are historical development state, not active canon.

## AI / agent start here
Before canon-sensitive work, read:
1. `REPOSITORY_INTEGRITY.md`
2. `AI_ONBOARDING.md`
3. `canon/` current human decisions
4. `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md`
5. `review/SYNC_STATUS.md`
6. `MIGRATION_REVIEW.md`
7. `WRITING_PROTOCOL.md` before prose work
8. `AUTHORING_POLICY.md` and `AGENTS.md` before repository/canon/Lemma changes
9. `prompts/SESSION_BOOTSTRAP.md` when repository instructions are not discovered automatically

Direct public URLs for restricted chat environments:
- Onboarding: https://raw.githubusercontent.com/Naastepad/claes-canon/main/AI_ONBOARDING.md
- Writing protocol: https://raw.githubusercontent.com/Naastepad/claes-canon/main/WRITING_PROTOCOL.md
- Operating Storybible: https://raw.githubusercontent.com/Naastepad/claes-canon/main/storybible/LEMMA_MCKEE_MASTER_2026-08-13.md
- Repository integrity: https://raw.githubusercontent.com/Naastepad/claes-canon/main/REPOSITORY_INTEGRITY.md
- Sync status: https://raw.githubusercontent.com/Naastepad/claes-canon/main/review/SYNC_STATUS.md
- Migration review: https://raw.githubusercontent.com/Naastepad/claes-canon/main/MIGRATION_REVIEW.md

`storybible/LEMMA_MCKEE_MASTER.md` is retained only as an earlier transformed work edition/audit artifact. The dated synchronized master is active.

## Four responsibility layers
1. **Evidence** — historical/research support (`SRC-*`, `SC.*`).
2. **Story truth** — novel truth and human decisions (`STC.*`, `DEC.*`).
3. **Narrative meaning** — instances, arcs, motifs, relationships, themes, values and world/code architecture (`NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`, `WORLD.*`, `CODE.*`).
4. **Deterministic consistency** — executable rules only (`lemma/*.lemma`).

External McKee/NOS knowledge objects (`KO.*`) are narrative theory, not Claes canon.

## GitHub + Lemma
GitHub is the complete operating environment:

`evidence -> canon -> narrative model -> Lemma constraints -> validation/CI`

The `.lemma` files are the deterministic rules-as-code layer of the Storybible and are versioned, reviewed and validated together with all other canon material. Lemma is not prose storage and does not decide literary truth.

**LemmaBase is optional and is not part of the canonical architecture.** Authoring, canon control, writing, validation and continuity checking do not depend on it. Any future external Lemma runtime is downstream-only and never outranks or writes back over GitHub `main`.

## Repository layout
- `storybible/` — operating masters and transformation ledger
- `canon/` — explicit human decisions and unresolved author decisions
- `claims/` — Source Claims and Story Claims
- `entities/` — stable persons and locations
- `objects/` — continuity-sensitive objects and biographies
- `narrative/` — Narrative Instances, arcs, motifs, relationships, themes/values, knowledge states, world modules and code architecture
- `sources/` — provenance registry
- `proposals/` — reviewable change proposals
- `review/` — migration and synchronization state
- `mapping/` — source-to-structured conversion ledger
- `lemma/` — executable deterministic constraints
- `scripts/validate_canon.py` — continuity compiler
- `.github/` — continuity and Lemma CI

## Truth flow
`historical source -> SC.* -> human proposal/decision -> STC.* -> entities/narrative/storybible -> Lemma when deterministic`

Narrative diagnosis:
`KO.* narrative theory + NI.* Claes instance -> analysis / diagnostic`

## Status axes
Evidence: `VERIFIED / SUPPORTED / PLAUSIBLE / DISPUTED / UNKNOWN`

Canon: `PROPOSED / CANON / OPEN / DEPRECATED / REJECTED`

Migration origin: `MIGRATED / DERIVED / NEW`

These axes answer different questions and must not be collapsed.

## Non-negotiable authoring rule
AI may read, extract, compare, propose, structure, synchronize approved decisions, validate and draft. AI does **not** silently promote hypotheses, close open decisions, resolve conflicts, overwrite concurrent work, merge, rewrite history, or promote canon without explicit human approval.
```

---

# SOURCE FILE: `AI_ONBOARDING.md`

```markdown
# AI Onboarding — Claes Storybible

**Canonical cross-model instruction file.** This document applies to ChatGPT, Claude, Gemini, Copilot, local agents and other language models. Model-specific files must defer to this file rather than inventing a parallel interpretation.

## 1. What this repository is

This repository is the operating Storybible and canon-control system for the historical novel **Claes Nissepat**. It contains six distinct working layers:

1. **Evidence** — historical/research support (`SRC-*`, `SC.*`).
2. **Story truth** — explicit novel truth (`STC.*`, `DEC.*`, `canon/`).
3. **World/practice state** — time-bounded historical environments and chapter-ready activity domains (`WORLD.*`, `storybible/domains/`, `narrative/domain_scene_packs.yaml`).
4. **Narrative meaning/projection** — character, causal spine, scene, sequence, arc, motif, relationship and value movement (`NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`).
5. **Editorial / reader validation** — prose quality, pacing, scene necessity, reader experience and feedback (`WRITING_PROTOCOL.md`, `narrative/editorial_gates.yaml`, `review/READER_EXPERIENCE_PROTOCOL.md`).
6. **Deterministic continuity** — only the subset that can usefully be evaluated as executable logic (`lemma/*.lemma`).

External McKee/NOS knowledge objects (`KO.*`) are narrative theory, not Claes canon.

## 2. Current operating authorities

The current synchronized human-readable operating master is:

`storybible/LEMMA_MCKEE_MASTER.md`

The dated `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` is a **legacy snapshot** retained for audit/development history and may contain superseded chronology or architecture.

Operational navigation is `storybible/INDEX.md`.

For causal chapter construction, read:

`storybible/STORY_PROJECTION_ROUND_C.md`

Its machine-readable projection is `narrative/story_projection_round_c.yaml`.

For drafting, revision and reader evaluation, read:

- `WRITING_PROTOCOL.md`;
- `narrative/editorial_gates.yaml`;
- `review/READER_EXPERIENCE_PROTOCOL.md`;
- `review/READER_FEEDBACK_TEMPLATE.md` when logging a real or simulated reader pass.

## 3. Authority hierarchy

When records appear to conflict, use this order:

1. explicit current human author decisions in `canon/` / latest applicable `DEC.*`;
2. synchronized active `STC.*` Story Claims;
3. dedicated current governing dossiers and synchronized entity/object/narrative registers;
4. `storybible/LEMMA_MCKEE_MASTER.md`;
5. Revision 11 through `mapping/CONVERSION_LEDGER.yaml` for detail not yet atomized;
6. Source Claims/provenance;
7. `PROPOSED` and `OPEN` records;
8. dated legacy masters, model inference or session memory — never authoritative.

Editorial protocols do **not** override canon. They govern whether canon has been dramatized effectively. A `CUT` verdict means a scene is weak or unnecessary, not that its underlying canon becomes false.

A Lemma result can test declared constraints. Lemma does not decide literary truth and does not turn historical evidence into canon.

## 4. Required read order

For canon-sensitive work:

1. `README.md`
2. `REPOSITORY_INTEGRITY.md` if you can write
3. current `canon/` decisions and `canon/OPEN_DECISIONS.yaml`
4. `review/SYNC_STATUS.md`
5. `storybible/MASTER.md`
6. `storybible/INDEX.md`
7. `storybible/LEMMA_MCKEE_MASTER.md`
8. relevant structured registers and current governing dossier(s)
9. relevant source claims/provenance
10. relevant Lemma specs only when deterministic reasoning is needed

### Additional required read order for chapter/scene construction

Before building a chapter or scene, also load:

1. `storybible/STORY_PROJECTION_ROUND_C.md`;
2. `narrative/story_projection_round_c.yaml` and identify the causal hinge;
3. `narrative/alchemical_authorial_architecture.yaml` when Great-Work/Corpus-Anima-Spiritus structure matters;
4. the relevant `narrative/domain_scene_packs.yaml` pack(s);
5. relevant time-sliced world/practice dossier(s);
6. participant arcs/relationships/knowledge states;
7. if Mayken appears: `narrative/mayken_independent_arc.yaml` as well as the Claes-Mayken relationship projection;
8. `WRITING_PROTOCOL.md`;
9. `narrative/editorial_gates.yaml`.

A chapter is not justified merely because research material exists. It must create pressure, choice, consequence, relationship movement or necessary reader experience.

### Additional required read order for critique/revision

Before judging literary quality, also read:

- `review/READER_EXPERIENCE_PROTOCOL.md`;
- any relevant `review/READER_FEEDBACK_*` record;
- the active Round-D gate definitions in `narrative/editorial_gates.yaml`.

Do **not** line-polish a scene before deciding whether it is `RETAIN`, `REVISE`, `MERGE` or `CUT`.

## 5. ID semantics

- `SRC-*` — source/provenance record
- `SC.*` — Source Claim
- `STC.*` — Story Claim
- `DEC.*` — explicit author/canon decision
- `ENT.*` — person/location/entity
- `OBJ.*` — continuity-sensitive object
- `NI.*` — Narrative Instance
- `ARC.*` — character/relationship/macro/authorial causal architecture
- `REL.*` — relationship
- `MOTIF.*` — recurring sensory/structural motif
- `THEME.*` — controlling idea, question, desire/need/lie/revelation
- `VALUE.*` — McKee-facing value axis/state
- `WORLD.*` — historical/worldbuilding module
- `GRD.*` — authoring/editorial guardrail or gate; never story truth by itself
- `CODE.*` — legacy/recovery architecture namespace where still present
- `OPEN.*` — unresolved author decision
- `KO.*` — external narrative-theory knowledge object; never Claes canon

## 6. Status semantics

Evidence: `VERIFIED / SUPPORTED / PLAUSIBLE / DISPUTED / UNKNOWN`

Canon: `PROPOSED / CANON / OPEN / DEPRECATED / REJECTED`

Editorial scene verdict: `RETAIN / REVISE / MERGE / CUT`

Reader-evidence classification: `ISOLATED / REPEATED / CONVERGENT / RESOLVED / INTENTIONAL_VARIANCE`

These axes are separate. Never convert editorial dislike into canon change or reader preference into historical evidence.

## 7. Time and uncertainty

Preserve source/story precision exactly. February remains a month unless a separate author decision establishes a day. A bounded interval remains bounded. Lack of exact precision is information, not a defect to repair by guessing.

Use the repository's half-open ranges consistently: `earliest` inclusive, `latest_exclusive` exclusive.

## 8. Historical-fiction boundary

Always distinguish:

- historically documented;
- evidence-based reconstruction;
- authorial fiction;
- unresolved/open material.

Network proximity does not prove a meeting. A historical print does not prove Claes' fictional provenance. A plausible route does not establish exact topography. A later manual does not automatically establish earlier practice.

## 9. Narrative interpretation

When interpreting a scene/chapter/sequence, consider POV and knowledge state, objective, psychological/moral need, opening and closing value, conflict/pressure, turning point, claim/relationship/object/knowledge changes, arc movement, motif transformation **and reader-state change**.

The governing Claes movement combines:

- `ARC.CLAES.MACRO_TRANSMUTATION` — Drager/Nigredo/Albedo/Rubedo/Projectio;
- `ARC.CLAES.GREAT_WORK.AUTHORIAL` — Status Prima; interwoven Corpus/Anima/Spiritus; Transmutatio; Projectio; Status Prima Nova;
- `ARC.CLAES.SINNE_RECOVERY` — openness, vigilance, constriction, recovery, resonance, sovereignty;
- `ARC.CLAES.CAUSAL_SPINE` — current pre-chapter causal hinge map.

Corpus/Anima/Spiritus are author-side registers, not a forced three-cycle structure or in-world doctrine.

## 10. Mayken rule

`ENT.PERSON.BELOVED` is the legacy technical entity ID for the **resolved** character Mayken Adriaensdr. Lampert. Her identity is not open.

If Mayken appears, consult:

- `storybible/MAYKEN_LAMPERT.md`;
- `narrative/mayken_independent_arc.yaml` (`ARC.MAYKEN.LIFE`);
- `narrative/mayken_relationship_projection.yaml` (`REL.CLAES.MAYKEN.CONJUNCTIO`);
- `narrative/beloved_recovery.yaml` only as a resolved-identity relationship extension.

Never load Mayken only as “Claes' beloved”. A developed Mayken scene must give her an objective, judgement, cost or choice of her own.

## 11. If you only read or answer questions

You may summarize canon, trace provenance, distinguish evidence from fiction, identify open decisions, explain chronology/knowledge/object states/arcs/motifs, use Lemma for deterministic checks and McKee/NOS for diagnosis. State uncertainty where the repository states uncertainty.

## 12. If you write prose

Read and obey `WRITING_PROTOCOL.md`. Before drafting, identify:

- the causal hinge from `ARC.CLAES.CAUSAL_SPINE`;
- relevant `NI.*` and active `STC.*`;
- participant knowledge/object states;
- active character/relationship arcs;
- current `sinne` state;
- applicable Corpus/Anima/Spiritus register(s);
- relevant domain scene pack and historical guardrails;
- unresolved `OPEN.*` matters that prose must not accidentally settle;
- intended reader movement: orientation, curiosity, emotion, tension, cognitive load and forward expectation.

Prose may dramatize within open space but may not accidentally close an `OPEN.*` matter. If a creative choice would close an open question, leave it open or present it separately as a proposal.

## 13. If you critique or revise prose

Apply the Round-D gates in this order:

1. scene necessity;
2. `RETAIN / REVISE / MERGE / CUT`;
3. causality and character choice;
4. pacing and reader experience;
5. prose quality;
6. continuity/history risk;
7. reader evidence and retest need.

For a hard editorial pass, use `GRD.EDITORIAL.RUTHLESS_EDITOR` / **Meedogenloze redacteur**:

> Niet aardig, wel precies. Als een scène niet werkt, zeg dat. Geen complimenten en geen verzachtende formuleringen wanneer die de diagnose vertroebelen.

Do not praise accurate research as compensation for weak fiction.

## 14. Cold-reader and pilot-reader rule

A cold-reader pass must not preload the Storybible or intended interpretation. It tests what the prose itself communicated.

AI may simulate a cold reader under restricted context, but **AI cold-reader simulation is not a substitute for actual human pilot readers**.

Actual reader feedback is logged as experience/problem evidence separate from the reader's proposed fix. Repeated independent observations are stronger revision signals than isolated preferences. Reader voting never decides canon or theme.

Use `review/READER_FEEDBACK_TEMPLATE.md`.

## 15. If you can modify the repository

Read `REPOSITORY_INTEGRITY.md`, `AGENTS.md`, `AUTHORING_POLICY.md` and `review/SYNC_STATUS.md` first.

Mandatory rules include:

- fresh-fetch target branch and every target file immediately before mutation;
- never write from remembered/stale content;
- stop and re-fetch after SHA/409/conflict or unexpected drift;
- never silently overwrite another agent's newer work;
- preserve stable IDs and provenance;
- propagate explicit human decisions downstream;
- if complete propagation is technically impossible, update sync status rather than pretending completion;
- no force push, destructive history rewrite, merge, publication or LemmaBase promotion without explicit human authority.

Required flow:

`source/evidence -> SC.* -> human proposal/decision -> STC.* -> entities/objects/knowledge -> world/practice domains -> narrative projection/arcs/relationships -> operating master/index -> prose/scene implementation -> Round-D editorial gates + reader evidence -> Lemma if deterministic -> validation -> review -> merge/publication`

## 16. If you modify Lemma

Lemma stores constraints, not literary interpretation. Suitable questions include whether people can meet, whether Claes can know/possess/use something at a time, whether prerequisite stages are satisfied, and whether declared temporal/object constraints are compatible.

Emotional power, love, elegance, pacing, reader engagement and thematic satisfaction belong to narrative/editorial diagnosis, not deterministic Lemma rules.

## 17. Cross-model handoff

At the end of substantial work, record enough repository-visible state for another model to continue: files/records read, files/records changed, current sync status, unresolved matters, validation status, editorial verdicts/reader evidence where relevant and whether human approval remains required. Do not rely on private reasoning or chat memory as canonical storage.
```

---

# SOURCE FILE: `CLAUDE.md`

```markdown
# Claude instructions — Claes

This is a thin model-specific entrypoint. The canonical cross-model instructions live in `AI_ONBOARDING.md`.

For Claude Projects or restricted `web_fetch` environments, use the literal-URL bootstrap in:

`prompts/CLAUDE_PROJECT_INSTRUCTIONS.md`

That file is designed to be copied into Claude Project Instructions so the required GitHub URLs are present literally in the project context instead of being guessed from repository paths.

Before answering canon-sensitive questions or editing this repository, read in this order:

1. `AI_ONBOARDING.md`
2. current `canon/` decisions and `review/SYNC_STATUS.md`
3. `storybible/MASTER.md` and `storybible/INDEX.md`
4. `storybible/LEMMA_MCKEE_MASTER.md`
5. the relevant structured records and governing dossiers
6. `WRITING_PROTOCOL.md` if drafting/revising literary prose
7. `AUTHORING_POLICY.md`, `AGENTS.md` and `REPOSITORY_INTEGRITY.md` if changing canon, schemas or Lemma

Do not substitute conversation memory or Project Knowledge for repository truth. Preserve the distinction between historical evidence (`SC.*`), novel truth (`STC.*`), narrative instances (`NI.*`) and deterministic Lemma constraints.

Never silently promote `OPEN` or `PROPOSED` material to `CANON`. Never invent precision that the Storybible does not contain.

If writing prose, obey the current chapter/scene construction rules in `AI_ONBOARDING.md` and `WRITING_PROTOCOL.md`: identify the causal hinge, POV, story-time window, active claims, knowledge/object state, values, pressure/turn, arcs/relationships/motifs, relevant domain/world pack, reader movement and open decisions that must remain open. Then write literary text without embedding metadata labels into the prose.

If Claude's fetch tool refuses a repository path that is not already literal in the conversation/project context, do not guess or conclude that the file is absent. Use the exact URLs supplied in `prompts/CLAUDE_PROJECT_INSTRUCTIONS.md`; if a required URL is still unavailable, report the missing file and stop canon-sensitive work until it is supplied.

At the end of substantial work, leave a concise handoff stating records consulted, changes proposed/made, unresolved decisions and validation status.
```

---

# SOURCE FILE: `REPOSITORY_INTEGRITY.md`

```markdown
# Repository Integrity Contract

This file is mandatory for every AI or automation with write access to `claes-canon`.

## Why this exists
Multiple ChatGPT sessions, Claude/Claude Code, Copilot or other agents may read and write the same repository. Git history prevents data loss only if writers behave conservatively. Canon integrity therefore requires an explicit concurrency protocol.

A reported write action, connector success response or absence/presence of CI checks is **not itself proof that intended repository state is persistent and reachable on the target branch**. Persistence must be verified positively from GitHub after mutation.

## Non-negotiable rules
1. **Freshness before mutation.** Fetch the current branch head and the current version/SHA of every target file immediately before a write.
2. **No memory writes.** Never replace a repository file using a copy remembered from chat or an earlier fetch if the file may have changed.
3. **No silent last-writer-wins.** If a target changed since analysis began, re-read and reconcile. Do not overwrite the newer version merely to apply your earlier plan.
4. **Authoring branch first.** Canon development belongs on an authoring branch/PR. `main` is a stable gateway/release surface unless the human explicitly directs otherwise.
5. **Human decisions outrank transforms.** Files in `canon/` are authoritative corrections/decisions and must be propagated downstream.
6. **Atomic semantic synchronization.** A decision should update all affected structured representations together. If technical limitations prevent this, create/update `review/SYNC_STATUS.yaml` and mark every unsynchronized path explicitly.
7. **Stable identity.** Never recycle IDs. Deprecate rather than repurpose.
8. **Uncertainty is data.** Preserve OPEN/PROPOSED/precision windows. Never resolve them by plausibility alone.
9. **No autonomous promotion.** AI may propose and synchronize approved decisions; it may not merge, publish to LemmaBase, or convert a proposal/open question into CANON without explicit human authority.
10. **Validation is necessary, not sovereign.** Green CI means structural checks passed; it does not make an unapproved claim canon. Missing, empty or unavailable CI/status-check results mean only that CI validation was not observed through that channel. They prove neither write success nor write failure.
11. **Positive post-write verification is mandatory.** Before claiming that a repository write is complete, re-fetch the target branch from GitHub and verify that the resulting commit is the branch head or an ancestor of it as appropriate. Re-fetch every file created or updated and confirm the expected semantic marker/content is present. For deletion, verify that the path is absent. A connector/API `success`, returned commit SHA or local state alone is insufficient.
12. **Separate persistence from validation.** Report write persistence and CI/validator state independently. Use language equivalent to `WRITE_VERIFIED` only after positive remote read-back. Use `CI_VERIFIED`, `CI_FAILED` or `CI_NOT_OBSERVED` separately; never collapse these axes into one vague "done" signal.
13. **No false completion from stale read-back.** A read made before the final write does not count as post-write verification. The verification fetch must occur after the last mutation that could affect the claimed end state.
14. **Preserve history.** No force push, destructive branch move, deletion of decision history, or rewriting of provenance without explicit human instruction.
15. **Handoff.** Substantial writes must leave a concise repository-visible record or updated sync/review status.

## Required post-write verification sequence
For any synchronization or canon write pass:

1. perform the intended mutations;
2. fetch the target branch head **after the final mutation**;
3. verify the expected commit chain/ancestry or current head;
4. re-fetch each touched file from the target branch and inspect at least the exact section/identifier/semantic marker that was meant to change;
5. verify deleted paths are actually absent when deletion was intended;
6. inspect validators/CI separately where relevant;
7. only then issue an end-state statement.

If any of steps 2–5 cannot be completed, the correct persistence status is **`WRITE_UNVERIFIED`**, not `SYNC_COMPLETE`, even if the mutation tool returned success.

## Canon synchronization dependency order
`canon decision → STC → ENT/OBJ/knowledge → NI/ARC/REL/MOTIF/THEME/VALUE → operating master → Lemma → validators/review`

When an upstream node changes, every downstream node is suspect until checked.

## Collision protocol
If another writer changes the same area while you work:
- stop the affected write;
- fetch the new head/content;
- identify whether changes are compatible, competing, or independent;
- preserve both if uncertain;
- create a proposal/conflict record rather than choosing silently;
- tell the human what needs resolution.

## Required end-state statement
After a synchronization task, report **two independent axes**.

Persistence:
- `WRITE_VERIFIED` — branch/commit state and affected remote files were positively re-read after the final write;
- `WRITE_UNVERIFIED` — mutation may have been attempted but positive remote persistence was not established;
- `CONFLICT` — branch/file state changed incompatibly and human resolution is required.

Semantic synchronization:
- `SYNC_COMPLETE` — all known downstream representations updated and positively read back;
- `SYNC_PENDING` — list exact remaining files/records and why;
- `CONFLICT` — human decision required.

Validation/CI:
- `CI_VERIFIED` — relevant validator/status evidence was observed and passed;
- `CI_FAILED` — relevant validator/status evidence was observed and failed;
- `CI_NOT_OBSERVED` — no relevant CI/status evidence was available through the checked channel.

A valid final report may therefore be, for example: `WRITE_VERIFIED / SYNC_COMPLETE / CI_NOT_OBSERVED`. This is materially stronger and more precise than saying merely that a write "succeeded" or that "no CI statuses were returned".
```

---

# SOURCE FILE: `AUTHORING_POLICY.md`

```markdown
# Canon Authoring Policy

## Core rule
Evidence, story truth, world/practice state, narrative placement, editorial quality and executable constraints are maintained as separate layers. Explicit human decisions are authoritative and must be synchronized through every dependent representation.

## Required reading before writes
A write-capable AI must read `AI_ONBOARDING.md`, current `canon/`, `REPOSITORY_INTEGRITY.md`, this policy and the relevant registers. It must re-fetch target files immediately before mutation.

Before drafting, revising or critiquing literary prose it must also read:

- `WRITING_PROTOCOL.md`;
- `storybible/STORY_PROJECTION_ROUND_C.md` when plot/scene causality is involved;
- `review/READER_EXPERIENCE_PROTOCOL.md` when assessing prose, pacing or reader response;
- `narrative/editorial_gates.yaml` for the active Round-D quality gates.

## Workflow
1. Read current human decisions, operating Storybible and relevant sources.
2. Record external assertions as `SC.*` Source Claims.
3. Record novel truth or candidate truth as `STC.*` Story Claims.
4. Keep `evidence_status` and `canon_status` independent.
5. Record significant human choices as `DEC.*` or repository-visible decision records.
6. Link claims to `ENT.*` entities and relevant Narrative Instances.
7. Preserve date precision and uncertainty ranges.
8. Synchronize approved decisions through dependent entities, objects, knowledge states, world/practice modules, Narrative Instances, arcs, relationships, motifs, themes/values and the operating master.
9. Project world knowledge into causal story architecture before inventing chapter structure.
10. Apply the editorial gates during scene construction and revision: scene necessity, prose quality, pacing, reader experience and reader feedback.
11. Convert only deterministic accepted Story Claims into Lemma constraints.
12. Run continuity and active-projection validation.
13. Review changes before merge and LemmaBase publication.

## Multi-agent rule
Never assume this repository is unchanged because the current chat wrote it earlier. Another session or model may have written meanwhile. Re-fetch branch state and target files before every write pass. If content changed, reconcile instead of overwriting. Follow `REPOSITORY_INTEGRITY.md`.

## Branch rule
Canon development belongs on an authoring branch/PR unless the human explicitly authorizes direct-main synchronization or the active conversation clearly continues an already authorized direct-main synchronization round. Do not force-update, delete history, publish to LemmaBase, merge a PR or promote OPEN/PROPOSED material without explicit human authority.

## Status vocabularies
Evidence: `VERIFIED`, `SUPPORTED`, `PLAUSIBLE`, `DISPUTED`, `UNKNOWN`.
Canon: `PROPOSED`, `CANON`, `OPEN`, `DEPRECATED`, `REJECTED`.
These are independent dimensions. A historical fact can be verified without being used in the novel; a fictional event can be plausible and canon.

Editorial verdicts are a separate axis: `RETAIN`, `REVISE`, `MERGE`, `CUT`. They judge prose/scene function and never alter canon by themselves.

Reader-evidence classifications are also separate: `ISOLATED`, `REPEATED`, `CONVERGENT`, `RESOLVED`, `INTENTIONAL_VARIANCE`.

## Precision rule
A month, season, year or interval remains that precision until an explicit story decision establishes greater precision.

## Narrative theory boundary
Universal `KO.*` narrative theory remains in the external Narrative Knowledge Base. This repository stores Claes-specific Narrative Instances and may reference Knowledge Objects as analysis targets.

## Editorial boundary
Historical accuracy, continuity and canon consistency are **necessary constraints but not proof of literary success**.

A scene may be fully correct and still receive `CUT`.

Reader feedback is evidence about delivery, not a vote on canon. Separate a reader's reported experience/problem from that reader's proposed solution. Repeated independent reader observations carry more revision weight than isolated taste.

AI cold-reader simulation is useful but does not substitute for actual human pilot readers.

## Synchronization rule
Use dependency order:

`human decision → STC → ENT/OBJ/knowledge → WORLD/domain state → NI/ARC/REL/MOTIF/THEME/VALUE → causal story projection → operating master → prose/scene implementation → editorial gates + reader evidence → Lemma if deterministic → validation/review`.

If technical limitations prevent a complete pass, report `SYNC_PENDING` with exact stale records; never hide partial synchronization.

## Review questions
A change must make clear:

- what evidence changed;
- what story truth changed;
- what decision supports it;
- where it is dramatized;
- which continuity domains are affected;
- whether the scene survives `RETAIN / REVISE / MERGE / CUT`;
- what reader experience is intended and what cold/pilot-reader evidence exists;
- whether Lemma changes;
- whether all downstream representations are synchronized.
```

---

# SOURCE FILE: `AGENTS.md`

```markdown
# AI Canon Authoring Instructions

This repository is the controlled operating Storybible and authoring layer for **Claes Nissepat**.

## Canonical AI instructions
Before canon-sensitive work, read in this order:
1. `AI_ONBOARDING.md`
2. `canon/` — all explicit human decisions; these outrank conflicting migrated or derived representations
3. `review/SYNC_STATUS.md`
4. `storybible/MASTER.md`
5. `storybible/INDEX.md`
6. `storybible/LEMMA_MCKEE_MASTER.md`
7. `storybible/STORY_PROJECTION_ROUND_C.md` for chapter/scene architecture
8. relevant world/practice domains and `narrative/domain_scene_packs.yaml`
9. `WRITING_PROTOCOL.md` if drafting/revising/criticising prose
10. `narrative/editorial_gates.yaml` and `review/READER_EXPERIENCE_PROTOCOL.md` for prose/reader evaluation
11. `AUTHORING_POLICY.md` and `REPOSITORY_INTEGRITY.md` before any repository write

The dated `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` is legacy/audit only. These rules apply to ChatGPT, Claude, Gemini, Copilot, local agents and other models. Never create a competing canon in session memory.

## Primary objective
Preserve historical provenance, story truth, causal narrative architecture, chapter-ready world knowledge and reader-effective prose without conflating evidence, interpretation, story choice, editorial verdict or narrative theory.

## Mandatory pre-write integrity protocol
A write-capable agent MUST:
1. Re-fetch the target branch and every file it intends to modify immediately before writing. Never write from remembered or previously cached content when another session may have changed the repository.
2. Verify the intended branch. Do not write canon-development changes directly to `main` unless the human explicitly orders that action or the active conversation clearly continues an already authorized direct-main synchronization round.
3. Read all applicable current `canon/DECISIONS*` records before modifying downstream representations.
4. Preserve stable IDs. Never silently rename, recycle or duplicate an existing `SC.*`, `STC.*`, `DEC.*`, `ENT.*`, `OBJ.*`, `NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`, `WORLD.*`, `GRD.*`, `CODE.*` or `OPEN.*` identity.
5. Make the smallest coherent change set. If a canon decision affects multiple layers, update all affected layers in the same synchronization pass or record an explicit `SYNC_PENDING` item; never leave silent drift.
6. Re-fetch a file after writing when subsequent writes depend on its new SHA/content.
7. Never force-update a branch, overwrite another agent's unreviewed work, merge a PR, close a PR, publish to LemmaBase, or delete canon/history unless the human explicitly requests that operation.
8. If the repository changed unexpectedly during the task, stop destructive writes, compare the new state, preserve both lines of work, and report the conflict.
9. Run or inspect repository and active-projection validation after structural/canon/editorial changes. A green syntax check does not override a human canon conflict or prove literary quality.
10. Leave a repository-visible handoff for substantial work: what was read, what changed, what remains open, validation state and editorial/reader state where relevant.

## Authority order on conflict
1. explicit human decisions in `canon/`
2. accepted current `DEC.*` decision records
3. active `STC.*` Story Claims
4. current dedicated governing dossiers and synchronized entity/object/narrative registers
5. `storybible/LEMMA_MCKEE_MASTER.md`
6. migrated source Storybible prose via the conversion ledger
7. source claims for historical support
8. proposals, `OPEN.*` records and AI interpretations
9. dated legacy masters and chat/session memory

Editorial gates do not outrank this authority chain. They judge whether prose and scenes work. A `CUT` verdict does not erase underlying canon.

Historical evidence (`SC.*`) does not become story canon merely because it is verified. External `KO.*` narrative theory never overrides Claes canon.

## Read order for authoring changes
1. onboarding, current `canon/`, sync status and operating master
2. `storybible/STORY_PROJECTION_ROUND_C.md` plus `narrative/story_projection_round_c.yaml` when plot/scene/structure is involved
3. relevant `STC.*`, `ENT.*`, `OBJ.*`, `NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`, `WORLD.*`
4. relevant `narrative/domain_scene_packs.yaml` and chapter-ready practice dossiers
5. relevant `SC.*` and source records
6. relevant `OPEN.*`
7. `WRITING_PROTOCOL.md`
8. `narrative/editorial_gates.yaml` and `review/READER_EXPERIENCE_PROTOCOL.md`
9. `mapping/CONVERSION_LEDGER.yaml` when source coverage matters
10. Lemma only for deterministic questions
11. external `KO.*` only for narrative diagnosis

## Chapter/scene projection rule
For scene construction, do not start from “what research can I use?”. Start from:

1. Which hinge in `ARC.CLAES.CAUSAL_SPINE` is being advanced?
2. Which person makes the consequential choice?
3. Which Corpus/Anima/Spiritus register(s) are materially active?
4. Which world/practice pack supplies the historically bounded actions and objects?
5. What changes in value, knowledge, relationship, object state or responsibility?
6. What changes for the reader?
7. Which `OPEN.*` matter must remain open?

`ARC.CLAES.GREAT_WORK.AUTHORIAL` is author-side architecture. Corpus/Anima/Spiritus are interwoven registers, not three mechanically repeated cycles and not mandatory prose labels.

## Scene-retention rule
Before line polishing, every scene receives one provisional editorial verdict:

- `RETAIN`
- `REVISE`
- `MERGE`
- `CUT`

Test four necessity dimensions:

- plot;
- character;
- information;
- reader experience.

Then apply the uniqueness test: **if all useful functions are served better elsewhere, the scene does not survive merely because it contains good research or good sentences.**

The machine-readable authority is `GRD.EDITORIAL.SCENE_NECESSITY` in `narrative/editorial_gates.yaml`.

## Mayken rule
`ENT.PERSON.BELOVED` is a legacy stable entity ID whose identity is **resolved** as Mayken Adriaensdr. Lampert.

If Mayken appears, load:
- `storybible/MAYKEN_LAMPERT.md`;
- `narrative/mayken_independent_arc.yaml` (`ARC.MAYKEN.LIFE`);
- `narrative/mayken_relationship_projection.yaml` (`REL.CLAES.MAYKEN.CONJUNCTIO`);
- relevant Lampert source claims if historical grounding matters.

Never write Mayken only as Claes' helper, reward, therapist or sensory device. A developed Mayken scene must give her an objective, judgement, cost or choice not reducible to Claes' immediate need.

## Reader-experience rule
Authorial intention and experienced effect are separate data.

A cold-reader pass receives prose without hidden Storybible explanation. It must report what the text itself communicated: causality, desire, change, orientation, attention, expectation and memory.

AI may simulate cold reading, but **AI cold-reader simulation is not a substitute for actual human pilot readers**.

Actual reader reports are logged with `review/READER_FEEDBACK_TEMPLATE.md`. Separate reported experience/problem from reader-proposed fix. Repeated independent observations carry more revision weight than isolated preferences. Reader voting never decides canon.

## Meedogenloze redacteur
`GRD.EDITORIAL.RUTHLESS_EDITOR` is a standing hard-review mode.

> **Niet aardig, wel precies. Als een scène niet werkt, zeg dat. Geen complimenten en geen verzachtende formuleringen wanneer die de diagnose vertroebelen.**

Review order:
1. verdict;
2. scene necessity;
3. primary/fatal problem;
4. causality and character;
5. pacing and reader experience;
6. prose quality;
7. continuity/historical risk;
8. `RETAIN / REVISE / MERGE / CUT`;
9. smallest material revision if warranted.

Do not praise accurate research as compensation for weak fiction.

## Mandatory behaviour
- Preserve provenance and source precision.
- Keep evidence status, canon status, editorial verdict and reader evidence classification independent.
- Never invent missing dates, locations, relationships, quotations or bibliographic metadata.
- Never turn month/year precision into a fabricated exact day.
- Prefer a proposal/open authorial-design record over direct canon change when genuine uncertainty exists.
- Unatomized prose remains active source material through the conversion ledger.
- Keep Lemma focused on executable constraints, not prose storage or literary interpretation.
- Add/update validation when a schema or mandatory guard changes.
- Explain downstream effects of canon changes.
- Never silently close `OPEN.*` decisions.
- Do not force an alchemical operation onto a scene merely to complete a pattern.
- Do not line-polish a scene that has not survived the necessity gate.

## Spatial reasoning rule — Goes and other atlas-backed settings
For questions about where a person **lives, owns property, works, operates a business, meets, travels or witnesses an event**, keep the spatial relation explicit. `RESIDES`, `OWNS`, `RENTS`, `OPERATES_BUSINESS`, `WORKS_AT`, `ADJOINS`, `USES` and `VISITS` are not interchangeable.

For Goes scene/topography work:
- read `narrative/world_goes_living_city.yaml` and relevant `SC.HIST.GOES.*` records;
- use the Stadsatlas/transport-register layer for parcel topology, year-valid routes, named parties, occupations and belendingen;
- never infer residence from ownership, business location, adjacency or family proximity;
- never infer an exact parcel polygon from four belendingen alone;
- preserve the distinction between a transport/ownership chain and a physical place through time;
- apply the time slice before answering: streets, gates, institutional functions, damage zones and routes can change;
- use modern/RCE street geometry as a crosswalk only where historical continuity is separately supported;
- for pre-1594 Nieuwstraat, use the resolved **older Nieuwstraat/Armenhoek zone-level reconstruction** under `DEC.GOES.NIEUWSTRAAT.IDENTITY.2026-08-14`; exact 1542 street axis remains unknown;
- Cornelis/young Claes' household residence is fixed to `ENT.PROP.GOES.NISSEPAT.NIEUWSTRAAT_1542` under `DEC.CORNELIS.RESIDENCE.GOES.2026-08-14`;
- Cornelis' Nardusbloem meeting environment is fixed to `ENT.LOC.GOES.ZUSTERHUIS` under `DEC.GOES.REDERIJKERS.MEETINGPLACE.2026-08-14`;
- keep 1554 fire damage and 1572 military destruction as separate event footprints;
- for 1572–1579 Claes-departure causality, consult `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001` and do not silently equate the 1572 Voorstad brewery with the documented 1577 Nissepad brewery.

A strong spatial answer should state: **where + relation to place + route + what is passed + who/what plausibly populates the route in that year + what has changed because of relevant events + certainty/open status**.

## State vocabularies
Evidence: `VERIFIED / SUPPORTED / PLAUSIBLE / DISPUTED / UNKNOWN`
Canon: `PROPOSED / CANON / OPEN / DEPRECATED / REJECTED`
Editorial verdict: `RETAIN / REVISE / MERGE / CUT`
Reader evidence: `ISOLATED / REPEATED / CONVERGENT / RESOLVED / INTENTIONAL_VARIANCE`
Migration origin: `MIGRATED / DERIVED / NEW`

## Reasoning boundary
Ask separately:
- What does historical evidence support? (`SC.*`)
- What has the author decided is true? (`canon/`, `DEC.*`, `STC.*`)
- What world/practice conditions are available? (`WORLD.*`, domain dossiers, scene packs)
- Where is it dramatized or causally projected? (`NI.*`, `ARC.CLAES.CAUSAL_SPINE`, arcs, motifs, relationships)
- Does the scene need to exist? (`GRD.EDITORIAL.SCENE_NECESSITY`)
- Does the prose communicate effectively? (Round-D prose/pacing/reader gates)
- Is it logically possible? (Lemma)
- Does it work narratively? (external `KO.*` diagnostics plus Round-D review evidence)

## Preferred synchronization pass
Human decision → affected Story Claims → entities/objects/knowledge states → world/practice domains → Narrative Instances/arcs/relationships/motifs/themes/values → causal/story projection → operating master/index → prose/scene implementation → editorial gates/reader feedback → Lemma constraints if deterministic → validators/tests → sync review → handoff.

## Handoff rule
Do not rely on private chain-of-thought or chat memory for continuity. Repository state, explicit human decisions, validated records and repository-visible review evidence are the handoff between sessions.
```

---

# SOURCE FILE: `canon/DECISIONS.yaml`

```yaml
schema_version: 1.4.0
kind: CanonDecisionRegistry
decisions:
- id: DEC.CLAES.BIRTH.2026-08-13
  type: CanonDecision
  status: CANON
  decision: Claes Cornelisz Nissepat is born in Goes on 8 December 1542.
  affects:
  - STC.CLAES.BIRTH.001
  - ENT.PERSON.CLAES
  rationale: author decision retaining the chronology aligned with the Brevísima frame; 1545 is migration drift
- id: DEC.CLAES.SINNE.2026-08-13
  type: CanonDecision
  status: CANON
  decision: Claes discovers the world through embodied sinne; trauma constricts this openness and it is later rediscovered on the road toward Enkhuizen with the beloved beside him, becoming a catalyst for recovery, wisdom and sovereignty.
  affects:
  - STC.CLAES.SINNE.001
  - ARC.CLAES.SINNE_RECOVERY
  - MOTIF.SINNE.RECOVERY
  - REL.CLAES.BELOVED.RECOVERY
- id: DEC.CLAES.PARADOX.2026-08-13
  type: CanonDecision
  status: CANON
  decision: Claes' gift is prolonged exact observation; his shadow is remaining in observation after action is required, and trauma can blunt the sensory openness on which the gift depends.
  affects:
  - STC.CLAES.PARADOX.001
  - ARC.CLAES.SINNE_RECOVERY
- id: DEC.CLAES.NEED.2026-08-13
  type: CanonDecision
  status: CANON
  decision: Claes must recover trust in embodied perception and act without complete certainty; knowledge and perception increase responsibility toward the other.
  affects:
  - STC.CLAES.NEED.001
  - THEME.CLAES.PSYCHOLOGICAL_NEED
  - THEME.CLAES.MORAL_NEED
- id: DEC.CLAES.SPIRITUAL_JOURNEY.2026-08-13
  type: CanonDecision
  status: CANON
  decision: Claes moves from matter toward spirituality through matter as vessel; the Great Work transmutates knowledge-as-control into wisdom-in-relation and the capacity to transmit and release.
  affects:
  - STC.CLAES.MORAL_QUESTION.001
  - THEME.CLAES.SPIRITUAL_JOURNEY
  - ARC.CLAES.MACRO_TRANSMUTATION
- id: DEC.CORNELIS.RESIDENCE.GOES.2026-08-14
  type: CanonDecision
  status: CANON
  decision: In novel canon, the house bought by historical Claes Jacobsz. Nissepat in the pre-1594 Nieuwstraat on 20 March 1542 is made available as the family home of Cornelis, his wife and young Claes; Claes grows up there until his departure to Reimerswaal after the 1554 fire.
  affects:
  - STC.CORNELIS.HOUSEHOLD_GOES.1542.001
  - ENT.PERSON.CORNELIS
  - ENT.PERSON.CLAES
  - ENT.PROP.GOES.NISSEPAT.NIEUWSTRAAT_1542
  - WORLD.GOES_LIVING_CITY
  rationale: The purchase and parcel topology are historical; occupation by the fictional Cornelis household is the accepted story choice. Residence remains distinct from Nissepad, harbour and other business locations.
- id: DEC.GOES.NIEUWSTRAAT.IDENTITY.2026-08-14
  type: CanonDecision
  status: CANON
  decision: The Nieuwstraat named in pre-1594 transport acts is treated as an older Nieuwstraat/Oude Nieuwstraat in or by the Armenhoek, distinct from the planmatige/current Nieuwstraat whose aanleg belongs to the 1594 expansion; the exact 1542 street axis remains uncertain.
  affects:
  - STC.GOES.NIEUWSTRAAT.PRE1594.001
  - ENT.LOC.GOES.NIEUWSTRAAT_PRE1594
  - ENT.LOC.GOES.NIEUWSTRAAT_1594
  - ENT.PROP.GOES.NISSEPAT.NIEUWSTRAAT_1542
  - WORLD.GOES_LIVING_CITY
  rationale: Pre-1594 use of the toponym is directly attested, later records connect Oude Nieuwstraat and Armenhoek, while the present/planned Nieuwstraat belongs to the 1594 urban expansion. Zone-level identity is sufficient for story continuity without fabricating an exact street line.
- id: DEC.GOES.REDERIJKERS.MEETINGPLACE.2026-08-14
  type: CanonDecision
  status: CANON
  decision: Cornelis-era rederijker meetings are staged in the Zusterhuis/former Zwarte-Zusters complex at the Singelstraat; the Sint-Sebastiaanshof is not back-projected into his period because the Nardusbloem moved there only in 1626.
  affects:
  - STC.CORNELIS.REDERIJKERS.ZUSTERHUIS.001
  - ENT.PERSON.CORNELIS
  - ENT.LOC.GOES.ZUSTERHUIS
  - ENT.ORG.GOES.NARDUSBLOEM
  - WORLD.GOES_LIVING_CITY
  rationale: The Zusterhuis-to-Sint-Sebastiaan sequence is historically documented for the Nardusbloem. This decision establishes Cornelis' scene environment, not proof that every Goese chamber used the same room or that a real Nissepat met there.
- id: DEC.CLAES.FAMILY_FIRE.1554.2026-08-14
  type: CanonDecision
  status: CANON
  decision: On 18 May 1554 the fictional Cornelis household loses its home in the older Nieuwstraat; Claes and Cornelis survive because they are away from the house, while Claes' mother, his younger brother born about eighteen months after Claes, and the mother's unborn child die in the fire. The mother is about six months pregnant.
  affects:
  - STC.CLAES.HOUSEHOLD_PRE_FIRE.1554.001
  - STC.CLAES.FAMILY_FIRE.1554.001
  - ENT.PERSON.CLAES_MOTHER
  - ENT.PERSON.CLAES_BROTHER
  - ENT.PERSON.CLAES_UNBORN_SIBLING
  - ENT.PROP.GOES.NISSEPAT.NIEUWSTRAAT_1542
  - NI.EVENT.GOES_FIRE.1554.001
  - ARC.CLAES.LIFE
  - REL.CLAES.BROTHER
  rationale: Burned houses are historically documented in the older Nieuwstraat/Armenhoek environment, but destruction of this specific house and the family deaths are explicit novel canon rather than historical claims.
- id: DEC.CLAES.GRANDFATHER_LINK.2026-08-14
  type: CanonDecision
  status: CANON
  decision: Historical Claes Jacobsz. Nissepat is used in novel canon as the fictional father of Cornelis and paternal grandfather of Claes. He remains the story owner of the 1542 Nieuwstraat house through the 1554 fire, loses that asset in the fire, and subsequently helps Cornelis support Claes' education.
  affects:
  - STC.CLAES.GRANDFATHER.NISSEPAT.001
  - ENT.PERSON.CLAES_JACOBSZ_NISSEPAT
  - ENT.PROP.GOES.NISSEPAT.NIEUWSTRAAT_1542
  - REL.CORNELIS.CLAES_JACOBSZ_NISSEPAT
  rationale: The historical person and his 1542 purchase are documented; the paternal genealogy, continued ownership through 1554 and post-fire support are deliberate fictional connections and must never be presented as archival fact.
- id: DEC.CLAES.POSTFIRE_FATHER_SON.2026-08-14
  type: CanonDecision
  status: CANON
  decision: After the 1554 fire Cornelis stays in Goes to rebuild livelihood, business and shelter and to finance Claes' schooling as far as he can, with partial support from his father Claes Jacobsz. Claes is sent to Reimerswaal because the original Zierikzee plan has become financially unattainable. Father and son therefore lose not only their household but also daily life with each other; the separation is an act of care that Claes can experience as abandonment.
  affects:
  - STC.CLAES.CORNELIS.POSTFIRE_SEPARATION.001
  - STC.CLAES.REIMERSWAAL.001
  - STC.CLAES.ZIERIKZEE.PLAN.001
  - REL.CLAES.CORNELIS
  - ARC.CLAES.CORNELIS
  - NI.EVENT.REIMERSWAAL_MOVE.1554.001
  rationale: This preserves the complexity that both father and son lose almost everything in 1554 while making Cornelis' continued labour and educational sacrifice a form of love rather than simple emotional withdrawal.
- id: DEC.CLAES.EXTENDED_FAMILY.2026-08-14
  type: CanonDecision
  status: CANON
  decision: "The approved extended family is: mother Tanneken Jansdochter; younger brother Jan Corneliszn. Nissepat, born approximately June 1544 and named in novel canon for Tanneken's father; paternal grandparents historical Claes Jacobsz. Nissepat and fictional Lijsbet Pietersdochter; maternal grandparents a fictionalized maternal-grandfather figure modeled on a historical Goese Jan Jansen kuiper and fictional Mayken Pietersdochter. Lijsbet dies circa 1540–1541 in story canon, the maternal-grandfather model around 1543, and Mayken survives the 1554 fire."
  affects:
  - STC.CLAES.HOUSEHOLD_PRE_FIRE.1554.001
  - STC.CLAES.FAMILY_FIRE.1554.001
  - STC.CLAES.EXTENDED_FAMILY.001
  - ENT.PERSON.CLAES_MOTHER
  - ENT.PERSON.CLAES_BROTHER
  - ENT.PERSON.LIJSBET_PIETERSDOCHTER
  - ENT.PERSON.JAN_JANSEN_KUIPER_MODEL
  - ENT.PERSON.MAYKEN_PIETERSDOCHTER
  - ENT.FAMILY.CLAES_EXTENDED_FAMILY_1554
  - REL.CLAES.BROTHER
  - REL.CLAES.TANNEKEN
  - REL.CLAES.MATERNAL_GRANDPARENTS
  rationale: "The author explicitly approved the proposed family architecture. Historical source and fiction remain separated: Claes Jacobsz. and the Goese Jan Jansen-kuiper evidence are historical anchors/models, while the kinship assignments, Lijsbet, Mayken, the exact maternal-grandfather identity/death and all cross-generation relations are novel canon."
- id: DEC.MEMORIAAL.BREVISIMA_PRINT_GIFT.2026-08-15
  type: CanonDecision
  status: DEPRECATED
  superseded_by: DEC.MEMORIAAL.DIRECT_TEXT_NO_CIPHER.2026-08-15
  decision: The encoded Diets/Brabant Brevísima is printed before binding on loose sheets with a nearly invisible gallnut/tannin plus gum-arabic medium, bound as Claes' apparently blank memoriaal, and given by John Dee to Claes before the journey to Boom in early 1564 together with a graphite stift; Dee forbids ink while Claes remains his pupil.
  rationale: Retained as audit history. The physical print-before-binding, tannin/gum medium, Dee handoff and graphite-only rule are retained by the superseding decision, while the cipher/key architecture is rejected.
- id: DEC.MEMORIAAL.DIRECT_TEXT_NO_CIPHER.2026-08-15
  type: CanonDecision
  status: CANON
  decision: The completed Diets/Brabant Brevísima translation is set in ordinary readable text and printed before binding on loose sheets with the near-invisible gallnut/tannin plus gum-arabic medium; the sheets are bound as Claes' apparently blank memoriaal, Dee gives the book and a graphite stift to Claes before Boom and forbids ink while Claes remains his pupil, and later green vitriol reveals the readable Brevísima directly without cryptographic decoding.
  affects:
  - STC.MEMORIAAL.GIFT.001
  - STC.MEMORIAAL.BREVISIMA_CARRIER.001
  - STC.MEMORIAAL.PRINT_PROCESS.001
  - STC.MEMORIAAL.GRAPHITE_RULE.001
  - STC.CORNELIS.FALLBACK_KNOWLEDGE.001
  - STC.ZOVITIUS.TRIGGER.1570.001
  - STC.CODE.RECOVERY_SEQUENCE.001
  - STC.CODE.MERELS.RECOVERY_NOT_CIPHER.001
  - STC.CODE.MERELS.P15.001
  - STC.CODE.MONAS.FUNCTION.001
  - STC.CODE.CASTANEA.FUNCTION.001
  - STC.CODE.DODOENS.REQUIRED.001
  - STC.CODE.PRIMUS_INDEX.FUNCTION.001
  - STC.CODE.DURATION.001
  - STC.LASCASAS.PUBLICATION.1578.001
  - OBJ.MEMORIAAL
  - OBJ.LASCASAS_PLAINTEXT
  - OBJ.LASCASAS_CIPHERTEXT
  - OBJ.DIRECT_KEY
  - OBJ.MERELS_24
  - OBJ.CASTANEA
  - OBJ.DODOENS_CARRIER
  - OBJ.PRIMUS_INDEX
  - OBJ.MONAS_CLAES
  - NI.SCENE.MEMORIAAL_GIFT.1564.001
  - NI.EVENT.SECURITY_BREAK.1564.001
  - NI.SEQUENCE.RECOVERY.1570.001
  - REL.CLAES.CORNELIS
  - REL.CLAES.DEE.001
  - REL.CLAES.SILVIUS
  - REL.CLAES.BELOVED
  - CODE.RECOVERY.CLAES.1570
  rationale: >-
    The cipher was introduced only because whole-book invisible printing initially appeared impracticable. The reconstructed tannin/gum letterpress process removes that technical premise. Keeping a cipher would therefore duplicate the concealment mechanism without a remaining story function. Chemical steganography is the concealment: Silvius prints readable language; graphite lets Claes use the same pages safely; green vitriol later completes the visible ink.
- id: DEC.MEMORIAAL.FORMAT_17Q.2026-08-15
  type: CanonDecision
  status: CANON
  decision: >-
    The hidden printed body of Claes' memoriaal is fixed at 17 single-sheet quarto gatherings: 17 full sheets, 68 printed leaves and 136 latent pages, plus any genuinely blank binder-added endleaves. The hidden text begins with Las Casas' prologue to Prince Philip and excludes the later visible-edition title page and separate translator's address. Each sheet uses normal quarto imposition, first forme 1-4-5-8 and wederdruk 2-3-6-7. The 1578 Brabant/Dutch Seer cort Verhael facsimile is the primary capacity and text-sequence analogue, not evidence for the fictional 1564 clandestine edition.
  affects:
  - STC.MEMORIAAL.PRINT_PROCESS.001
  - OBJ.MEMORIAAL
  - OBJ.LASCASAS_PLAINTEXT
  rationale: >-
    The supplied 1578 facsimile separates a title leaf and translator's address from the Las Casas text body. From the prologue through the end of the tract the facsimile occupies 136 scanned page surfaces, exactly 17 quarto sheets at eight pages per sheet. This replaces the provisional 18-sheet/144-page estimate while preserving a strict evidence boundary: the 1578 witness anchors capacity and sequence only; the hidden 1564 edition remains novel reconstruction.
```

---

# SOURCE FILE: `canon/OPEN_DECISIONS.yaml`

```yaml
schema_version: 2.1.0
kind: OpenDecisionRegistry
policy:
  active_only: true
  note: Resolved, superseded and not-applicable records belong in dated decision/audit files and are not retained here as apparent open work.
decisions:
- id: OPEN.CLAES.DEATH.001
  domain: ending
  priority: high
  question: Exact circumstances, place and cause of Claes' death
  status: OPEN
  fixed_function: Projectio / transfer without control

- id: OPEN.TRANSLATOR.1564.001
  domain: historical_reconstruction
  priority: high
  question: Identity of the initial Spanish-to-Diets translator or intermediate-source route for the completed 1564 text
  status: OPEN
  guardrails:
  - Gillis may be a Diets stylist/editor; Spanish competence remains unproven.
  - Moretus is unavailable for 1564.
  - Cordero is no longer in Antwerp.
  - Miggrode is in Veere.
  - Do not make Silvius the translator merely because he prints the text.

- id: OPEN.CHAPTER.NUMBERING.YOUTH.001
  domain: structure
  priority: low
  question: Whether youth chapters use parallel numbering or join the chronological numbering of the 1564 sequence
  status: OPEN

- id: OPEN.BAKERY.SCENE.001
  domain: scene
  priority: low
  question: Whether and where to use the proposed 'De Gest' bakery scene
  status: OPEN

- id: OPEN.LATE_RADERMACHER.001
  domain: scene
  priority: low
  question: Whether Claes directly meets Radermacher in the late Middelburg line
  status: OPEN
  guardrail: Network plausibility does not prove a meeting or formal Familist affiliation.

- id: OPEN.MERELS.CLOSEUPS.001
  domain: scene
  priority: medium
  question: Which merels scenes or problems deserve close-up narrative treatment now that merels is independent of the Brevísima mechanism
  status: OPEN
  fixed:
  - Merels remains a game, skill, relationship device and thematic motif.
  - No fixed 24-problem recovery sequence is required.

- id: OPEN.MATERIAL.WET_TEST.001
  domain: material
  priority: high
  question: Physical wet/press test of the reconstructed gallnut/tannin plus gum-arabic medium on metal relief type, including transfer, dry visibility/gloss, mechanical moet, paper condition and diluted green-vitriol development
  status: OPEN
  fixed_workshop_start:
  - 2 medicinal drachmen gallnuts steeped in 2.5 medicinal ounces clear water
  - retain 2 medicinal ounces clearest filtered extract
  - dissolve 1.5 medicinal ounces gum arabic; tune slightly by behaviour on type
  - proof developer reference is 0.5 medicinal drachme green vitriol in 4 medicinal ounces clear water
  guardrails:
  - No untested recipe becomes hard historical prose.
  - The process is canon as technical reconstruction; experimental performance and exact optimum remain open.

- id: OPEN.MEMORIAAL.FACSIMILE.001
  domain: object
  priority: medium
  question: Final facsimile appearance of the apparently blank/graphite-used memoriaal and the developed directly readable Brevísima pages
  status: OPEN

- id: OPEN.GRAPHITE_STIFT.PROVENANCE.1564.001
  domain: historical_reconstruction
  priority: medium
  question: Exact historically defensible physical form and provenance of the graphite marking stift Dee gives Claes in Antwerp in early 1564
  status: OPEN
  fixed_story_function:
  - Dee gives Claes a graphite marking tool with OBJ.MEMORIAAL before Boom.
  - Dee forbids ink while Claes remains his pupil.
  guardrails:
  - Do not automatically depict a later standardized wood-cased pencil.
  - Historical form/provenance uncertainty does not reopen the fixed story function.

- id: OPEN.SECURITY.LOW_LINK.1564.001
  domain: plot
  priority: high
  question: Exact low-level incident or identifiable network link by which the 4 October 1564 Fabritius crisis makes Cornelis operationally unsafe
  status: OPEN
  exclusions:
  - Cornelis need not be a stone thrower.
  - Cornelis need not be arrested in 1564.
  guardrail: This is a persecution/network question; it does not control a cryptographic key or physical loading of the memoriaal.

- id: OPEN.GILLIS.ROLE.001
  domain: character
  priority: medium
  question: Whether Marcus Antonius Gillis appears directly as a limited Diets redactor/model
  status: OPEN

- id: OPEN.MIGGRODE.ROLE.001
  domain: character
  priority: low
  question: Whether Miggrode receives any fictional pre-1578 contact line
  status: OPEN

- id: OPEN.DEE.SPANISH.001
  domain: historical_reconstruction
  priority: low
  question: Dee's Spanish reading competence, but only if it remains necessary to a scene after the translator decision is designed
  status: OPEN

- id: OPEN.ZOVITIUS.DELIVERY.1570.001
  domain: plot
  priority: high
  question: Exact route by which the special 1570 Zovitius copy reaches Claes in Goes
  status: OPEN
  guardrail: If retained, its function is a material cue toward GALLA LEO VIRIDIS, not delivery of a cryptographic key.

- id: OPEN.ANTWERP.1564.NAMES.001
  domain: historical_research
  priority: low
  question: Primary verification of names, if used, for the Vrouwenbroeder of 4 October and the Walloon executed 19 December 1564
  status: OPEN

- id: OPEN.PUBLICATION.TRANSMISSION.1570_1578.001
  domain: plot
  priority: high
  question: Exact human, production and distribution route from the revealed readable Diets/Brabant text to the Antwerp 1578 print event
  status: OPEN
  fixed:
  - year: 1578
  - place: Antwerp
  - mode: printed publication / print event
  - function: projectio of the Word; the textual mission is complete by 1578
  guardrails:
  - Seton has no role in this route.
  - Exact printer, cover identity, distribution route and surviving-copy logic remain evidence-controlled or explicit novel reconstruction.

- id: OPEN.CHAPTER.CALENDAR.1564.001
  domain: chronology
  priority: high
  question: Calendar audit of 1564 chapters against readable translation production, invisible tannin/gum print, memoriaal/graphite handoff before Boom, Boom/Antwerp process lessons and the 4 October security break
  status: OPEN
  fixed:
  - NI.SCENE.MEMORIAAL_GIFT.1564.001 occurs before NI.CHAPTER.1564.03.
  - 4 October changes network risk, not the physical contents of the memoriaal.

- id: OPEN.FINAL_MERELS.001
  domain: ending
  priority: medium
  question: Exact opponent, stakes and action of the final merels scene
  status: OPEN
  fixed_function: Mastery expressed as balance, space and release rather than maximum domination.

- id: OPEN.CORNELIS.REDERIJKER.DEKEN.001
  domain: character_and_rederijker_network
  priority: medium
  question: Does Cornelis ever serve as deken of the Nardusbloem or of the emerging reform-minded Castanien current during his lifetime
  status: OPEN
  fixed:
  - Cornelis is a member of the Nardusbloem / older Magdalena-linked Goese tradition.
  - In novel canon he plays a formative role in the 1560s emergence of the reform-minded/protestantiserende current that becomes the later Edele Castanienbloem.
  - No deken office is currently canon.
  guardrails:
  - Do not use deken status to justify access or logistics already supported by poorter, biersteker, rederijker and trust networks.
  - The pre-1595 Castanien origin is explicit novel reconstruction, not historical attestation.

- id: OPEN.GOES.CLAES_DEPARTURE_1572_1579.001
  domain: plot_and_economic_causality
  priority: high
  question: "Which historically disciplined chain of siege damage, residual family/business interest, debt/claims and 1577–1579 legal settlement makes Goes cease to function as Claes' recoverable home/economic anchor, and when does he actually leave?"
  status: OPEN
  fixed:
  - "Cornelis is already dead before the 1572 siege."
  - "The 1572 siege damages outside salt works and a brewery in the Voorstad."
  - "The Nissepad brewery documented in 1577 is not proven identical to the brewery burned in the Voorstad in 1572 and is not proven Cornelis property."
  - "The burned Westzelke salt-pan site sold by Jan Jansen Nissepat in 1577 has an unknown destruction event."
  - "The 1578 Antwerp publication endpoint remains fixed."
  guardrails:
  - Do not solve this by silently destroying the documented Nissepad brewery.
  - Do not label 1577–1579 transport acts executions, confiscations or forced sales without evidence.
  - Do not make documented Nissepat names one proven nuclear family without a genealogical decision.
  - Any fictional property/lease connection used to motivate Claes must be explicitly marked novel reconstruction.

- id: OPEN.MAYKEN.INDEPENDENT_MIDARC.001
  domain: character
  priority: high
  question: "What concrete pressure, work trajectory and consequential choice between the 1554 rebuilding horizon and the 1570 reveal makes Mayken's independent adult agency visible before she becomes Claes' late partner?"
  status: OPEN
  fixed:
  - "Mayken's identity as Mayken Adriaensdr. Lampert is resolved."
  - "She has an independent character arc under DEC.MAYKEN.INDEPENDENT_ARC.2026-08-16."
  - "Her competence grows from the apothecary/material world and differs from Claes' hidden-order orientation."
  - "She must have goals/choices not reducible to Claes."
  candidate_line_to_revalidate:
  - "Earlier authorial development considered family/social pressure, expulsion or loss of standing followed by greater reliance on female practical-healing/herbal networks; this is a development seed, not current event canon."
  guardrails:
  - Do not duplicate Cornelis' prosecution history onto Adriaen without a separate story choice and historical feasibility check.
  - Do not grant Mayken unsupported university, physician or guild status.
  - Do not turn a possible kruidenvrouw line into a stereotype or a secret cipher role.
  - Preserve her distinct 1554 experience: destruction plus rebuilding, not Claes' household annihilation.
```

---

# SOURCE FILE: `review/SYNC_STATUS.md`

```markdown
# Synchronization status

Status: `SYNC_COMPLETE_ACTIVE_LAYERS`

Release state: `MAIN_CANON_SYNCHRONIZED_2026-08-16`

Historical recovery addendum: `ROUND_A_HISTORICAL_SUBSTRATE_RECOVERED`

Authoring world-state addendum: `ROUND_B_DOMAIN_REBUILD_IMPLEMENTED`

Story-projection addendum: `ROUND_C_STORY_PROJECTION_IMPLEMENTED`

Editorial/reader addendum: `ROUND_D_EDITORIAL_READER_PROTOCOL_IMPLEMENTED`

Goes clergy addendum: `GOES_CLERGY_MATHIJS_CLEMENS_CANONIZED_AND_SYNCHRONIZED_2026-08-16`

The explicit Goes clergy decisions are authoritative in `canon/` and are now synchronized through dedicated source claims, Story Claims, entity records, a world module, a governing Storybible dossier, `storybible/MASTER.md` and `storybible/INDEX.md`.

## Current governing chronology

- Claes born Goes: **8 December 1542**.
- **14 March 1541:** mr. Mathijs Jacopsen explicitly attested as vice-pastoor.
- **27 February 1542:** mr. Mathijs Jacobsen explicitly attested as `vice-cureyt ter Goes`.
- **8 December 1542:** exact Goese office-holder at Claes' birth remains historically UNKNOWN; Mathijs must not be projected automatically from February to December.
- Family rupture: **18 May 1554**.
- Reimerswaal: 1554–summer 1561.
- Antwerp Landjuweel: August 1561; Dee is not placed there.
- Dee/Silvius formation: 1563–early 1564.
- **20 March 1564:** Clemens van den Dale explicitly attested as `licentiaat pastoor Goes`.
- Memoriaal/graphite handoff: before Boom, early 1564.
- Security break: **4 October 1564**, network effect only.
- Cornelis first arrest/examination: autumn 1567, Antwerp; release on borg/conditions.
- Cornelis execution: **19 November 1569**, Antwerp; Claes witnesses.
- Direct memoriaal reveal: 1570 line.
- Goes 1572–1579 final material/economic severance: **authorial causal design OPEN**.
- Brevísima print culmination: **Antwerp 1578**.
- Delft moral bottom: 1584.
- Enkhuizen Seton frame: **13 March 1602, ca.16:00**, house of Jacob Hausfsen.
- post-1602: Projectio of Self / Status Prima Nova; exact Claes death remains open.

## Current fixed character / object state

### Goese clergy / Maria Magdalena environment

- `ENT.PERSON.MATHIJS_JACOPSEN_VICE_CUREIT` is a historical person, not a fictional composite.
- Mathijs is verified as vice-pastoor in 1541 and `vice-cureyt ter Goes` on 27 February 1542.
- His association with the Maria Magdalena parish/Grote Kerk environment is **SUPPORTED contextual identification**, not verbatim wording of the decisive 1542 act.
- Church/kerkhof/choir property evidence does not establish residence.
- Mathijs is **not** canonically the proven baptizing priest of Claes and is not proven in office on 8 December 1542.
- `ENT.PERSON.CLEMENS_VAN_DEN_DALE` is verified as `licentiaat pastoor Goes` on 20 March 1564.
- The exact titular pastor above Mathijs and the complete 1542–1563 succession remain historically unresolved.
- Governing dossier: `storybible/GOES_CLERGY_MATHIJS_CLEMENS_1541_1564.md`.
- Machine-readable world state: `narrative/world_goes_clergy_1541_1564.yaml`.

### Memoriaal / Brevísima

- readable Diets/Brabant text is printed nearly invisibly with tannin/gallnut + gum arabic before binding;
- Dee gives the already prepared hidden book plus graphite stift before Boom;
- green vitriol directly develops readable typography;
- reveal is reading, not decryption;
- old matrix/merels/Monas/Castanea/Dodoens/Primus/nomenclator recovery chain is retired from this mechanism;
- Seton has no Brevísima role.

### Cornelis

- Goes poorter;
- biersteker, not fixed brewery owner;
- Nardusbloem / older Magdalena-linked rederijker;
- fictional formative role in the 1560s current that becomes the later Edele Castanienbloem;
- deken status remains open;
- fictionally executed 19 November 1569 in Antwerp, witnessed by Claes.

### Mayken

- identity resolved as **Mayken Adriaensdr. Lampert**, fictional, ca.1546 Goes;
- `ENT.PERSON.BELOVED` is a legacy stable entity ID, not an open identity;
- independent materia-medica/material/sensory/error-control expertise;
- independent governing arc `ARC.MAYKEN.LIFE`;
- exact adult mid-arc work/family/social-pressure design remains `OPEN.MAYKEN.INDEPENDENT_MIDARC.001`;
- mature relation uses `REL.CLAES.MAYKEN.CONJUNCTIO` with two centers of agency.

### Alchemy

- Green Lion is operational process vocabulary, not a universal historical equation;
- strong-water failure precedes right opening relation;
- Sol remains materially continuous;
- Rode Leeuw is deep red/red-brown and carries already-present Sol;
- exact carrier composition and exact Enkhuizen assay choreography remain open.

## Round A — historical substrate

Recovered and active: Low Countries/Zeeland historical state 1540–1605, public opinion/information ecology, layered identity, sensory church model, local Goese liturgical guardrails and recovered source provenance.

The Goes clergy recovery adds named institutional anchors to the earlier generic/sensory church layer without inventing a complete clergy succession.

## Round B — chapter-ready practice domains

Active authoring domains:

- bread/grain/baking;
- beer/biersteker/brewery economy;
- Reimerswaal school/cost-pupil life;
- rederijker/Nardusbloem/Landjuweel practice;
- Antwerp time slices;
- Goes schutterij/military practice;
- Goese Catholic clergy/parish scene blocking for 1541–1542 and 1564 through `WORLD.GOES.CLERGY_1541_1564`.

`narrative/domain_scene_packs.yaml` supplies machine-readable activity/world packets. A pack constrains possible scenes; it never creates fictional participation.

## Round C — causal story projection

Governing projection: `storybible/STORY_PROJECTION_ROUND_C.md`.

- `ARC.CLAES.CAUSAL_SPINE` maps the pre-chapter causal hinges.
- `ARC.CLAES.GREAT_WORK.AUTHORIAL` restores **Status Prima -> Corpus / Anima / Spiritus -> Transmutatio/Rubedo -> Projectio -> Status Prima Nova**.
- This nests with, rather than replaces, `Drager -> Nigredo -> Albedo -> Rubedo -> Projectio`.
- Corpus/Anima/Spiritus are simultaneous registers, not three mechanically repeated cycles.
- `ARC.MAYKEN.LIFE` gives Mayken an independent story trajectory.
- `REL.CLAES.MAYKEN.CONJUNCTIO` requires reciprocal relation with two centers of agency.
- `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001` holds the exact Goes severance chain; do not silently identify the burned 1572 Voorstad brewery with the documented 1577 Nissepad brewery.

## Round D — editorial and reader-experience protocol

Round D is now active before large-scale structural/drafting work.

### Governing files

- `WRITING_PROTOCOL.md`
- `narrative/editorial_gates.yaml`
- `review/READER_EXPERIENCE_PROTOCOL.md`
- `review/READER_FEEDBACK_TEMPLATE.md`
- `review/EDITORIAL_PROTOCOL_ROUND_D_2026-08-16.md`

### Fixed editorial gates

- `GRD.EDITORIAL.SCENE_NECESSITY`
- `GRD.EDITORIAL.PROSE_QUALITY`
- `GRD.EDITORIAL.PACING`
- `GRD.EDITORIAL.READER_EXPERIENCE`
- `GRD.EDITORIAL.COLD_READER`
- `GRD.EDITORIAL.PILOT_READER`
- `GRD.EDITORIAL.RUTHLESS_EDITOR`

### Scene verdicts

Every developed scene must be testable as:

**RETAIN / REVISE / MERGE / CUT**.

Necessity dimensions:

1. plot;
2. character;
3. information;
4. reader experience;
5. uniqueness — whether all useful functions are better served elsewhere.

Historical richness, research effort, symbolism or beautiful prose is never sufficient by itself to retain a scene.

### Reader feedback

Cold-reader passes receive prose without hidden Storybible explanation. AI may simulate this restricted-context pass, but **AI cold-reader simulation is not a substitute for actual human pilot readers**.

Actual reader evidence separates reported experience/problem from reader-proposed fix. Repeated independent observations carry more revision weight than isolated taste; reader voting never decides canon.

### Meedogenloze redacteur

Standing hard-review mode:

> **Niet aardig, wel precies. Als een scène niet werkt, zeg dat. Geen complimenten en geen verzachtende formuleringen wanneer die de diagnose vertroebelen.**

Required order: verdict -> necessity -> primary problem -> causality/character -> pacing/reader experience -> prose -> continuity/history -> RETAIN/REVISE/MERGE/CUT.

## Current active high-impact authorial opens

- `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001`;
- `OPEN.MAYKEN.INDEPENDENT_MIDARC.001`;
- exact 1570→1578 publication/transmission chain;
- exact 1564 translator/source route;
- exact material wet/press validation;
- exact Rode-Leeuw carrier composition;
- exact Enkhuizen assay choreography;
- Claes' exact death and final merels realization.

Historical research gaps that must not be mistaken for authorial opens include the exact Goese clergy succession between the February 1542 Mathijs anchor and the March 1564 Clemens anchor.

See `canon/OPEN_DECISIONS.yaml` and alchemical open supplements for the complete active list.

## Current clergy synchronization paths

Synchronized:

- `sources/SRC-HIST-GOES-CLERGY-RAZE-1536-1564-001.md`;
- `claims/SOURCE_CLAIMS_GOES_CLERGY_2026-08-16.yaml`;
- `claims/STORY_CLAIMS_GOES_CLERGY_2026-08-16.yaml`;
- `canon/DECISIONS_GOES_CLERGY_2026-08-16.yaml`;
- `canon/DECISIONS_2026-08-16.md`;
- `entities/GOES_CLERGY_1541_1564.yaml`;
- `narrative/world_goes_clergy_1541_1564.yaml`;
- `storybible/GOES_CLERGY_MATHIJS_CLEMENS_1541_1564.md`;
- `storybible/MASTER.md`;
- `storybible/INDEX.md`;
- this sync-status file.

No known clergy-specific downstream synchronization remains pending.

## Next major work

The repository remains ready for **structural realization**:

`Book -> Act -> Sequence -> Chapter -> Scene -> Beat`.

`narrative/structure.yaml` remains largely unpopulated and `narrative/scenes.yaml` still contains only a small number of full scene diagnostics. Future population must use:

1. Round-C causal hinges;
2. Round-B domain scene packs and active world supplements, including the clergy module where relevant;
3. character/relationship/object/knowledge state;
4. Round-D scene-necessity, pacing, prose and reader-experience gates.

## Validation note

Repository CI must be evaluated on the actual integration commit. This status does not pre-claim a workflow result that has not yet run.
```

---

# SOURCE FILE: `storybible/MASTER.md`

```markdown
# Claes Storybible — MASTER / operating authority

**Logical master ID:** `SB.CLAES.MASTER`  
**Current synchronization date:** 16 August 2026  
**Authoring readiness:** Rounds A–D implemented

This repository is the structured operating projection of Revision 11 plus later explicit author decisions. The lossless source edition remains preserved for material not yet atomized, but later decisions override conflicting source or legacy-master wording.

## Source edition

`Claes_Storybible_MASTER_COMPLEET_2026-08-10_REVISIE11_MACROSTRUCTUUR_PROJECTIO(1).md`

- source lines: `3803`
- parsed headings: `296`
- SHA-256: `e38430f0165e7c0779a8ae6bba6a208773c677682f55295a940e91fdb2ed9edd`
- source role: `LOSSLESS_PROSE_AUTHORITY`
- structured role: `IN_REPOSITORY_OPERATING_PROJECTION`

Every top-level source section remains accounted for in `mapping/CONVERSION_LEDGER.yaml`. Unatomized prose does not disappear merely because it has not yet become a claim or Narrative Instance.

## Current human-readable authorities

Start with:

1. `storybible/LEMMA_MCKEE_MASTER.md` — **current operating story synthesis**.
2. `storybible/STORY_PROJECTION_ROUND_C.md` — causal/character projection from settled canon and chapter-ready world knowledge toward final structure.
3. `WRITING_PROTOCOL.md` — governing drafting, revision, pacing, prose-quality and scene-retention protocol.
4. `review/READER_EXPERIENCE_PROTOCOL.md` — cold-reader, human pilot-reader and reader-feedback method.
5. `storybible/INDEX.md` — operational navigation.
6. `canon/OPEN_DECISIONS.yaml` — active unresolved backlog only.
7. `review/SYNC_STATUS.md` — synchronization state.

The dated `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` is a **legacy snapshot**, not current authoring authority. It may preserve obsolete 1545/cipher/death-window/open-beloved wording for audit history only.

## Dedicated governing dossiers

- `STORY_PROJECTION_ROUND_C.md` — causal spine, deeper Great-Work architecture, Mayken independent arc and explicit open 1572–1579 Goes hinge.
- `ALCHEMICAL_OPERATION_PALETTE.md` — non-binding author-side palette for Calcination, Sublimation, Solution, Putrefaction, Distillation, Coagulation and Tincture; diagnostic and compositional only, never a mandatory 3×7/21-chapter scheme.
- `WRITING_PROTOCOL.md` — scene construction, prose, pacing, reader experience and editorial decision rules.
- `review/READER_EXPERIENCE_PROTOCOL.md` — reader-testing authority.
- `review/READER_FEEDBACK_TEMPLATE.md` — consistent reader-evidence logging.
- `MEMORIAAL_BREVISIMA_PRINT_1564.md` — hidden readable tannin/gum print, Dee handoff, graphite rule, direct green-vitriol reveal.
- `MEMORIAAL_BREVISIMA_CASTOFF_1564.md` — 17 single-sheet quarto gatherings / 136 latent pages.
- `FAMILY_CLAES_1542_1554.md` — Tanneken, Jan, grandparents, 1542 house and 1554 family rupture.
- `GOES_CLERGY_MATHIJS_CLEMENS_1541_1564.md` — named historical Goese clergy anchors: Mathijs Jacopsen/Jacobsen in 1541–early 1542, Clemens van den Dale in 1564, with the 1542–1563 succession gap preserved.
- `MAYKEN_LAMPERT.md` — resolved identity and independent character/material role of Mayken, synchronized to no-cipher canon.
- `CORNELIS_HOUSE_OF_LOVE_NETWORK_1551_1569.md` — governing route from beer/cask commerce through Ghysbrecht, Dens and Barrefelt into the translocal Huis der Liefde; Plantin is a later node and the evidence/fiction boundary is explicit.
- `CORNELIS_EXECUTION_1569.md` — detailed 19 November 1569 Cornelis execution model.
- `EXECUTIONS_REFORMATION_CLAES_2026-08-16.md` — current execution/testimony mechanics.
- `ALCHEMICAL_CHEMICAL_PROCESS_CHAIN_CLAES_LIFELINE.md` — base alchemical/chemical process dossier.
- `ALCHEMICAL_PROCESS_REFINEMENT_2026-08-16.md` — governing refinements for Green Lion semantics, failure-before-opening, conserved Sol, Rode Leeuw, assay and Morhof Seton frame.
- `ANTWERP_THREE_VISITS_ALCHEMICAL_ARC_1561_1569.md` — Antwerp three-visit/process scaffold, subject to later decisions where older wording survives.
- `domains/*.md` — Round-B chapter-ready practice domains for bread, beer, Reimerswaal school, rederijkers/Landjuweel, Antwerp time slices and schutterij/military practice.

## Machine-readable layers

### Decisions / story truth

Current explicit author decisions live across:

- `canon/DECISIONS.yaml`
- dated `canon/DECISIONS_*.md`
- `canon/DECISIONS_2026-08-16.yaml`
- `canon/DECISIONS_GOES_CLERGY_2026-08-16.yaml`
- `canon/DECISIONS_ALCHEMY_LIFELINE_2026-08-15.yaml`
- `canon/DECISIONS_ALCHEMY_REFINEMENT_2026-08-16.yaml`
- `canon/DECISIONS_RESOLUTIONS_2026-08-16.yaml`
- `canon/DECISIONS_STORY_PROJECTION_2026-08-16.yaml`
- `canon/DECISIONS_HOUSE_OF_LOVE_NETWORK_2026-08-16.yaml`

Latest explicit decision wins within its domain. A base registry is not allowed to resurrect an older state merely because a later decision lives in a supplement.

`claims/SOURCE_CLAIMS*.yaml` stores evidence/reconstruction claims. `claims/STORY_CLAIMS*.yaml` stores novel truth. Evidence and story truth remain separate.

### World/practice state

- `narrative/world_modules.yaml`
- `narrative/domain_scene_packs.yaml`
- `narrative/religious_space_sensory_church.yaml`
- `narrative/world_goes_clergy_1541_1564.yaml`
- `storybible/domains/*.md`

These define what can plausibly happen in a place/time/activity. A world module never creates fictional participation by itself.

### Narrative state and projection

- `entities/*.yaml`
- `objects/*.yaml`
- `narrative/knowledge_states*.yaml`
- `narrative/relationships.yaml`
- `narrative/arcs.yaml`
- `narrative/motifs.yaml`
- `narrative/instances*.yaml`
- `narrative/alchemical_authorial_architecture.yaml`
- `narrative/story_projection_round_c.yaml`
- `narrative/mayken_independent_arc.yaml`
- `narrative/mayken_relationship_projection.yaml`
- `narrative/goes_departure_1572_1579.yaml`

### Editorial / reader layer

- `narrative/editorial_gates.yaml`
- `WRITING_PROTOCOL.md`
- `review/READER_EXPERIENCE_PROTOCOL.md`
- `review/READER_FEEDBACK_TEMPLATE.md`

Editorial verdicts (`RETAIN / REVISE / MERGE / CUT`) do not alter canon. They judge whether a scene should exist and whether the prose successfully communicates the intended story.

### Deterministic subset

`lemma/*.lemma` is rules-as-code only. Lemma may veto an impossible combination; it never invents canon or literary quality.

## Fixed chronology and life-state corrections

The following are current and must not be reopened by legacy prose:

- **14 March 1541:** historical anchor — mr. Mathijs Jacopsen is explicitly attested in Goes as **vice-pastoor**.
- **27 February 1542:** historical anchor — mr. Mathijs Jacobsen is explicitly attested as **`vice-cureyt ter Goes`**.
- **8 December 1542:** birth of Claes in Goes. The exact Goese priest/office-holder on this date remains historically **UNKNOWN**; Mathijs must not be projected automatically from February to December and is not proven to have baptized Claes.
- **12 January 1551:** historical anchor — Ghysbrecht, kuiper van Antwerpen, acquires *De Haeswindeken* in Goes; Cornelis' commercial relationship with him is novel canon, not archival fact.
- **ca. 1552–1553:** Cornelis belongs in novel canon to the translocal Huis der Liefde through the chain Ghysbrecht → Adriaan Dens → Barrefelt. The Ghysbrecht → Dens bridge is explicit novel reconstruction; Plantin is not the converter.
- **18 May 1554:** fictional family home lost; Tanneken, Jan and unborn child die; Claes and Cornelis survive. This catastrophe tests an already existing Familist conviction rather than causing Cornelis' conversion.
- **1554–1561:** Claes at Reimerswaal; Zierikzee is the abandoned pre-fire plan.
- **August 1561:** Antwerp Landjuweel; Dee is not placed there; Goes is not currently established as one of the fourteen official competing chambers.
- **1563/early 1564:** Dee/Silvius formation.
- **20 March 1564:** historical anchor — Clemens van den Dale is explicitly attested as **`licentiaat pastoor Goes`**.
- **before Boom in early 1564:** Dee gives the already hidden-print memoriaal and graphite stift to Claes.
- **4 October 1564:** adult macro-Nigredo/security break; no physical alteration or ciphering of the memoriaal. Cornelis' Familist background does not by itself close the separate exact low-level trigger.
- **autumn 1567:** first Cornelis arrest/examination in Antwerp and release on borg/conditions.
- **19 November 1569:** Cornelis fictionally executed in Antwerp, witnessed by Claes.
- **1570:** direct green-vitriol reveal/read of hidden readable Brevísima; no cryptographic recovery chain.
- **1572–1579:** exact material/economic/legal chain by which Goes finally becomes nonrecoverable for Claes remains **authorial-design OPEN** under `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001`.
- **1578, Antwerp:** printed publication completes the textual mission — projectio of the Word.
- **1584:** Delft moral bottom / Albedo threshold.
- **13 March 1602, ca.16:00, Enkhuizen:** Morhof-framed Seton projectio at the house of Jacob Hausfsen — projectio of Matter.
- **after 1602:** projectio of the Self / Status Prima Nova; exact death remains open.

## Goese clergy / Maria Magdalena current state

`DEC.GOES.CLERGY.MATHIJS_VICE_CUREYT.2026-08-16`, `DEC.GOES.CLERGY.CLEMENS_VAN_DEN_DALE.2026-08-16` and `DEC.GOES.CLERGY.SUCCESSION_BOUNDARY.2026-08-16` govern.

- **Mathijs Jacopsen/Jacobsen** is a historical person and the named clergy anchor for the Catholic Goese world immediately preceding and entering Claes' birth year.
- He is verified as **vice-pastoor** on 14 March 1541 and **`vice-cureyt ter Goes`** on 27 February 1542.
- His association with the **Maria Magdalenaparochie / Grote Kerk** is a strongly supported contextual identification, but the decisive 1542 act itself says only `ter Goes`.
- Property transactions `aan het kerkhof` and `achter het koor van de kerk` strengthen his church-world embedding but do **not** prove residence.
- He is not proven to be the titular benefice-holder, not proven in office on 8 December 1542 and not proven to have baptized Claes.
- **Clemens van den Dale** is verified as **`licentiaat pastoor Goes`** on 20 March 1564.
- The exact titular pastor above Mathijs and the complete **1542–1563** succession remain a historical research gap. Do not extend Mathijs or Clemens across that interval by plausibility alone.

The governing human-readable dossier is `storybible/GOES_CLERGY_MATHIJS_CLEMENS_1541_1564.md`; machine-readable support lives in `claims/SOURCE_CLAIMS_GOES_CLERGY_2026-08-16.yaml`, `claims/STORY_CLAIMS_GOES_CLERGY_2026-08-16.yaml`, `entities/GOES_CLERGY_1541_1564.yaml` and `narrative/world_goes_clergy_1541_1564.yaml`.

## Memoriaal / Brevísima current state

`DEC.MEMORIAAL.DIRECT_TEXT_NO_CIPHER.2026-08-15` governs.

The completed Diets/Brabant text is set in ordinary readable movable type and printed nearly invisibly with a reconstructed clear gallnut/tannin + gum-arabic medium before binding. The paper is the hidden book. Dee gives the bound object to Claes before Boom and requires graphite rather than ink.

Green vitriol later supplies the iron that darkens the tannin-loaded letterforms. The result is already readable language. **Reveal is not decryption.**

Retired from the Brevísima mechanism:

- ciphertext/nomenclator stream;
- 24×24 matrix;
- merels as recovery key;
- Monas as ordering key;
- Castanea as key anchor;
- special Dodoens nomenclator carrier;
- Primus Index;
- multi-week cryptographic reconstruction.

Merels, Monas, Castanea and ordinary Dodoens may survive independently where they serve game, education, botany, symbolism or character.

## Mayken current state

The beloved identity is resolved as **Mayken Adriaensdr. Lampert**, fictional, born ca.1546 in Goes. `ENT.PERSON.BELOVED` is retained only as a legacy stable entity ID; it does not mean her identity is open.

Her historical embedding is the real Lampart/Lambert/Lampert apothecary environment. The project distinguishes verified persons/property records, supported identity/genealogy reconstruction and explicit fictional daughtership.

Mayken is independently competent in materia medica, preparation, measurement, botanical/material identification, trained sensation and error control. She may assist direct reveal and reading but is **not** a cryptographic solver or special-Dodoens key-holder.

Her family also experiences the 1554 fire through the burned *Zwaene* property. Her counter-memory is destruction **plus rebuilding**, not a duplicate of Claes' household annihilation.

`ARC.MAYKEN.LIFE` is a governing independent character arc. Mayken must have objectives, judgements, costs and choices not reducible to Claes. Her exact adult mid-arc work/family/social-pressure chain remains open under `OPEN.MAYKEN.INDEPENDENT_MIDARC.001`.

Her mature relationship with Claes is projected by `REL.CLAES.MAYKEN.CONJUNCTIO`: reciprocal relation between unlike modes of knowing without absorption or possession. Conjunctio is author-side architecture, not mandatory in-world terminology.

## Cornelis current state

Cornelis is:

- Goes poorter;
- **biersteker**, not fixed brewery owner;
- rederijker and logistical/book-material carrier;
- member in novel canon of the translocal **Huis der Liefde / Familia Caritatis** by ca. 1552–1553;
- not a printer.

His entry route is fixed as **beer/cask commerce → Ghysbrecht/Gijsbrecht, kuiper van Antwerpen → fictional trusted bridge to Adriaan Dens → Barrefelt → Huis der Liefde**. Ghysbrecht is a historical archival anchor but is **not** a documented Familist; his relation to Dens is explicit novel reconstruction. Dens is Cornelis' first knowingly identifiable Familist, and Barrefelt is the historically plausible network deepener. `CORNELIS_HOUSE_OF_LOVE_NETWORK_1551_1569.md` governs the full evidence/story boundary.

Cornelis can remain outwardly embedded in Catholic Goes; no separate Goese Familist congregation or invented formal initiation ritual is required. The 1554 fire tests this pre-existing affiliation rather than creating it.

**Plantin is a later print/distribution node, not Cornelis' converter.** Cornelis' later clandestine book/paper logistics grow from the same practical competencies as the beer trade — casks, storage, accounts, credit, route knowledge, carriers, discretion and trust — without implying that books are routinely hidden in beer barrels.

His chamber identity is fixed as the **Nardusbloem / older Magdalena-linked Goese tradition**. The Zusterhuis remains his meeting environment.

In novel canon he helps form a reform-minded/protestantiserende current in the 1560s that becomes the later Edele Castanienbloem. The historical sources do not prove that early split. **1595 is the earliest surviving attestation, not a proved founding date.**

Whether Cornelis ever serves as deken remains open.

His death is fixed as the 19 November 1569 Antwerp fictional execution model. The Familist network now supplies a longer trust-history behind his protective silence and book/paper route, but `OPEN.SECURITY.LOW_LINK.1564.001` remains open unless separately resolved.

## Alchemical current state

### Material process law

> **What becomes visible was already present.**

Material chain:

`kies / pyritic rejected matter → weathering + water + air + time → vitrioolwater / operational Groene Leeuw → direct tannin-text reveal + opening lesson → strong-water failure on Sol → right compound relation → death/opening of Sol → materially continuous hidden Sol → red fixation / Rode Leeuw → Saturn/lead → assay/cupellation-like reveal → projectio → release`

Guardrails:

- Green Lion is process-dependent vocabulary, not a universal historical equation `Green Lion = FeSO4`.
- Green vitriol directly reveals the tannin text but does not directly dissolve gold.
- Sol must first resist ordinary strong water: force is not the same as right relation.
- No real gold is created from lead; no later silent gold addition is allowed.
- Rode Leeuw/projectiepoeder is deep red to red-brown and carries already-present Sol; exact non-gold carrier composition remains open.
- Cupellation-like assay is authorial reconstruction, not documented Seton protocol.
- Do not use routine tasting of corrosive/vitriol liquors.
- Seton is wholly separated from the Brevísima line.

### Great-Work authorial architecture

`DEC.CLAES.GREAT_WORK.AUTHORIAL_ARCHITECTURE.2026-08-16` and `ARC.CLAES.GREAT_WORK.AUTHORIAL` govern:

`Status Prima → Corpus / Anima / Spiritus → Transmutatio/Rubedo → Projectio → Status Prima Nova`

This **nests with and does not replace** `ARC.CLAES.MACRO_TRANSMUTATION`:

`Drager → macro-Nigredo → Albedo/Onderscheiding → Rubedo/Verbinding → Projectio/Overdracht`.

- **Corpus**: actual material processes, bodies, food, books, plants, buildings, cities, metals and tools.
- **Anima**: meaning, language, belief, testimony, loyalty, memory, public interpretation and love.
- **Spiritus**: Claes' vigilance, certainty-seeking, grief, agency, embodied *sinne*, responsibility and sovereignty.

Corpus, Anima and Spiritus are simultaneous spiral registers, **not three successive books or three mechanically identical cycles**. `Solve et Coagula` is an author-side movement of separating false fusions and reconnecting in truer relation. No fixed operation count is mandatory.

The seven-operation palette in `ALCHEMICAL_OPERATION_PALETTE.md` preserves **Calcination, Sublimation, Solution, Putrefaction, Distillation, Coagulation and Tincture** as a non-binding compositional vocabulary. It may diagnose or enrich a scene, sequence or causal hinge only when the real material and human event earns that operation. It must never be used to force a 3×7 structure, an exact 21-chapter count, or a false historical claim that this sequence was universal.

> **The author knows the Work; Claes undergoes it; the reader experiences it.**

## Causal story projection

`ARC.CLAES.CAUSAL_SPINE` in `narrative/story_projection_round_c.yaml` is the current pre-structure for chapter architecture. It maps fourteen hinges from childhood Status Prima through post-1602 Status Prima Nova.

A future chapter must identify the hinge it advances or justify a genuinely new hinge. World research earns scene space only when it creates pressure, choice, relationship movement, consequence or necessary reader experience.

The unresolved H09 hinge is the 1572–1579 Goes severance. It must remain visibly open until the author chooses a historically disciplined material/economic/legal causal chain.

## Goes 1572–1579 design boundary

Historically grounded current anchors:

- 1572 siege damage includes outside salt works and a brewery in the Voorstad;
- a Nissepad brewery with equipment is documented in 1577;
- that Nissepad brewery is **not proven identical** to the brewery burned in the Voorstad and is not proven Cornelis property;
- Jan Jansen Nissepat sells a burned Westzelke salt-pan site in 1577, but the destructive event is unknown;
- later transport acts are not automatically executions, confiscations or forced sales.

The open story question remains: **which chain of real damage, fictional residual interest, debt/claims, legal settlement and network collapse finally makes Goes cease to function as Claes' recoverable home or economic anchor?**

## Editorial / reader-experience current state — Round D

Round D is now part of authoring authority, but it is not story canon.

### Scene necessity

`GRD.EDITORIAL.SCENE_NECESSITY` requires every developed scene to be tested for:

1. plot necessity;
2. character necessity;
3. information necessity;
4. reader-experience necessity;
5. uniqueness — whether all useful functions are served better elsewhere.

Verdicts:

- **RETAIN** — indispensable and strongest current place/form;
- **REVISE** — indispensable function, weak execution;
- **MERGE** — necessary material duplicates or gains force in combination;
- **CUT** — no indispensable function, or every function is better served elsewhere.

Historical richness, research effort, symbolism and beautiful prose do not independently justify retention.

### Prose and pacing

`GRD.EDITORIAL.PROSE_QUALITY` and `GRD.EDITORIAL.PACING` require POV filtration, concrete material language, selective sensory cognition, metabolized research, responsive rhythm, meaningful entry/exit and allocation of reader attention around choice and consequence.

Pacing is not simply speed. A quiet scene can be necessary; a calm scene cannot be inert filler.

### Reader experience

`GRD.EDITORIAL.READER_EXPERIENCE` separates authorial intention from experienced effect.

Cold-reader passes must not preload hidden Storybible explanation. AI may simulate cold reading, but **AI cold-reader simulation does not substitute for actual human pilot readers**.

Human reader observations are logged with `review/READER_FEEDBACK_TEMPLATE.md`, separating reported experience/problem from reader-proposed fix. Repeated independent reports carry more revision weight than isolated preference. Reader voting never decides canon.

### Meedogenloze redacteur

`GRD.EDITORIAL.RUTHLESS_EDITOR` is a standing hard-review mode:

> **Niet aardig, wel precies. Als een scène niet werkt, zeg dat. Geen complimenten en geen verzachtende formuleringen wanneer die de diagnose vertroebelen.**

A technically and historically correct scene may still be weak fiction and may still receive `CUT`.

## Active open-decision policy

`canon/OPEN_DECISIONS.yaml` contains **only active unresolved questions**. Resolved, superseded and `RESOLVED_NOT_APPLICABLE` history belongs in decision/audit files.

This distinction is mandatory:

- **historical/research open** — evidence might close it;
- **experimental open** — only a material test can close it;
- **authorial design open** — the novel must choose it;
- **irreducibly uncertain** — preserve historical uncertainty and choose explicitly fictional reconstruction if needed.

Round-C high-impact authorial opens include:

- `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001`;
- `OPEN.MAYKEN.INDEPENDENT_MIDARC.001`.

Neither may be silently closed by prose, reader preference or historical plausibility alone.

The Goese clergy succession gap between the February 1542 Mathijs anchor and the March 1564 Clemens anchor is a **historical/research open**, not an authorial invitation to invent a continuous incumbency.

## Narrative development backlog

The recovery and readiness rounds are now complete:

- **A** — historical substrate recovered;
- **B** — six major world/practice domains made chapter-ready, supplemented by the evidence-bounded Goese clergy world state;
- **C** — world projected into causal character architecture;
- **D** — editorial, pacing and reader-feedback gates made operational.

The next major task is **structural realization**:

`Book → Act → Sequence → Chapter → Scene → Beat`.

`narrative/structure.yaml` remains largely unpopulated and `narrative/scenes.yaml` contains only a small number of full scene diagnostics. Future population should use `ARC.CLAES.CAUSAL_SPINE` plus Round-B scene packs and apply Round-D scene-necessity/pacing/reader gates during construction rather than only after a full draft exists.

## Precedence

When records conflict:

1. latest explicit current `DEC.*` author decision, including supplements;
2. active later domain-specific `STC.*` story claim or explicit supersession declared by a later decision;
3. dedicated current governing dossier, including `STORY_PROJECTION_ROUND_C.md` within its domain;
4. current `LEMMA_MCKEE_MASTER.md`;
5. synchronized entities/objects/world modules/arcs/relationships/instances and causal projections;
6. Revision 11 prose for unsuperseded unatomized meaning;
7. source claims for historical support;
8. proposals and open decisions;
9. dated legacy masters/session memory — audit/context only.

`WRITING_PROTOCOL.md` and the Round-D editorial layer govern **implementation and evaluation**, not truth precedence. Never use an editorial verdict or reader preference to rewrite canon silently.
```

---

# SOURCE FILE: `storybible/INDEX.md`

```markdown
# Storybible Index

Operational navigation for the current Claes Storybible.

## Start here

1. `MASTER.md` — authority, precedence and current fixed state.
2. `LEMMA_MCKEE_MASTER.md` — **current synchronized human-readable story synthesis** through 16 August 2026.
3. `STORY_PROJECTION_ROUND_C.md` — current causal/character projection from the settled world into future chapter structure.
4. `../WRITING_PROTOCOL.md` — current drafting, prose, pacing and scene-retention authority.
5. `../review/READER_EXPERIENCE_PROTOCOL.md` — cold-reader, pilot-reader and feedback method.
6. `../canon/OPEN_DECISIONS.yaml` — active unresolved backlog only.
7. `../review/SYNC_STATUS.md` — synchronization status.
8. `../review/CANON_CONFLICT_AUDIT_2026-08-16.md` — conflicts found and their resolution.
9. `../review/HISTORICAL_SUBSTRATE_RECOVERY_2026-08-16.md` — Round-A recovery.
10. `../review/DOMAIN_REBUILD_ROUND_B_2026-08-16.md` — Round-B chapter-readiness rebuild.
11. `../review/STORY_PROJECTION_ROUND_C_2026-08-16.md` — Round-C projection audit.
12. `../review/EDITORIAL_PROTOCOL_ROUND_D_2026-08-16.md` — Round-D editorial/reader recovery audit.

`LEMMA_MCKEE_MASTER_2026-08-13.md` is a dated legacy snapshot. It is retained for development history but is not current authoring authority.

## Explicit decisions

- `../canon/DECISIONS.yaml` — core decision registry.
- `../canon/DECISIONS_2026-08-13.md` — birth/sinne and associated decisions.
- `../canon/DECISIONS_2026-08-14.md` — Goes/family decisions.
- `../canon/DECISIONS_2026-08-15.md` — execution/Reformation and memoriaal decisions.
- `../canon/DECISIONS_2026-08-16.yaml` — Brevísima 1578 / Seton separation.
- `../canon/DECISIONS_GOES_CLERGY_2026-08-16.yaml` — Mathijs Jacopsen/Jacobsen as verified vice-pastoor/vice-cureit anchor, Clemens van den Dale as verified 1564 pastoor anchor, and the 1542–1563 succession guardrail.
- `../canon/DECISIONS_ALCHEMY_LIFELINE_2026-08-15.yaml` — current merged alchemical life-line state, including later supersessions.
- `../canon/DECISIONS_ALCHEMY_REFINEMENT_2026-08-16.yaml` — Green Lion/Sol/Enkhuizen and Nardusbloem refinement.
- `../canon/DECISIONS_RESOLUTIONS_2026-08-16.yaml` — callback-recovered Mayken identity and Cornelis-death precedence.
- `../canon/DECISIONS_STORY_PROJECTION_2026-08-16.yaml` — Great-Work authorial architecture, Mayken independent arc and Claes-Mayken conjunctio.
- `../canon/DECISIONS_HOUSE_OF_LOVE_NETWORK_2026-08-16.yaml` — Cornelis' ca.1552–1553 Familist entry route, pre-fire affiliation, outward conformity, later Plantin role and beer-to-paper logistics continuity.

## Active open decisions

- `../canon/OPEN_DECISIONS.yaml` — only genuinely unresolved core questions, including the 1572–1579 Goes causal break and Mayken independent mid-arc design.
- `../canon/OPEN_DECISIONS_ALCHEMY_REFINEMENT_2026-08-16.yaml` — Rode-Leeuw carrier composition and exact Enkhuizen assay/choreography.
- `../canon/OPEN_DECISIONS_ALCHEMY_LIFELINE_2026-08-15.yaml` — legacy redirect/supersession record only.

Resolved/not-applicable records no longer remain mixed into the active open registry. The 1542–1563 Goese clergy succession is a historical/research gap, not an authorial open to be filled by invention.

## Historical / research claims

- `../claims/SOURCE_CLAIMS.yaml`
- `../claims/SOURCE_CLAIMS_EXECUTIONS_REFORMATION.yaml`
- `../claims/SOURCE_CLAIMS_GOES_LIVING_CITY.yaml`
- `../claims/SOURCE_CLAIMS_GOES_2026-08-14.yaml`
- `../claims/SOURCE_CLAIMS_GOES_CLERGY_2026-08-16.yaml` — exact RAZE-backed Mathijs and Clemens clergy claims plus the Maria Magdalena evidence boundary.
- `../claims/SOURCE_CLAIMS_FAMILY_1540S.yaml`
- `../claims/SOURCE_CLAIMS_MEMORIAAL_PRINT_1564.yaml`
- `../claims/SOURCE_CLAIMS_LAMPERT_APOTHECARY.yaml`
- `../claims/SOURCE_CLAIMS_ALCHEMY_2026-08-16.yaml`
- `../claims/SOURCE_CLAIMS_GOES_RELIGION_1577_1578.yaml`
- `../claims/SOURCE_CLAIMS_HISTORICAL_SUBSTRATE_RECOVERY_2026-08-16.yaml`
- `../claims/SOURCE_CLAIMS_DOMAIN_REBUILD_2026-08-16.yaml`
- `../claims/SOURCE_CLAIMS_HOUSE_OF_LOVE_NETWORK_2026-08-16.yaml` — Ghysbrecht/Gijsbrecht archival anchors, Dens/Barrefelt network roles, outward-conformity boundary and Plantin historiographical caution.
- `../sources/SRC-HIST-GOES-CLERGY-RAZE-1536-1564-001.md` — primary provenance record for the recovered Goese clergy transport-register evidence.

## Historical substrate / scene-world authority — Round A

This layer supplies non-fiction world state and scene conditions. It never creates fictional Claes participation by itself and never outranks later explicit story decisions.

- `../history/LOW_COUNTRIES_TRANSFORMATION_1540_1605.yaml`
- `../history/LOW_COUNTRIES_TRANSFORMATION_1540_1605.md`
- `../history/ZEELAND_REVOLT_TIMELINE.yaml`
- `modules/HISTORICAL_SUBSTRATE_1540_1605.md`
- `modules/PUBLIC_OPINION_IDENTITY_REVOLT.md`
- `../narrative/religious_space_sensory_church.yaml`
- `../narrative/world_goes_clergy_1541_1564.yaml` — evidence-bounded named clergy state for 1541–1542 and 1564; exact 8 December 1542 office-holder remains unknown.
- `GOES_CLERGY_MATHIJS_CLEMENS_1541_1564.md` — governing human-readable clergy dossier.
- `modules/WORLD_GOES_CHURCH_LOCAL.md`
- `modules/WORLD_GOES_CHURCH_LITURGICAL_GUARDRAILS.md`
- `modules/HISTORICAL_SUBSTRATE_GOES_CHURCH_LINK.md`
- `modules/GOES_RELIGIOUS_TRANSITION_1577_1578.md`

### Writing-readiness rule

A historical domain is not chapter-ready merely because a source or dossier exists. For the relevant place/year/person/activity the authoring layer should be able to retrieve: provenance/evidence status, time-valid world state, actors/actions, materials, sensory fields, character knowledge/access, local-versus-transfer boundary, explicit guardrails and scene consequences.

## Chapter-ready practice domains — Round B

Use these dossiers together with `../narrative/domain_scene_packs.yaml`.

### Bread / grain / baking

- `domains/BREAD_GRAIN_BAKING_1540_1602.md`
- `../sources/SRC-HIST-BREAD-LOWCOUNTRIES-ZEELAND-001.md`
- world: `WORLD.BREAD_GRAIN`
- key boundary: urban professional bakery is a safer default than an invented household oven; exact Goese recipe, ferment, price and loaf weight remain open/local.

### Beer / biersteker / brewery economy

- `domains/BEER_BREWING_BEERSTEKER_1540_1580.md`
- `../sources/SRC-HIST-BEER-LOWCOUNTRIES-GOES-001.md`
- world: `WORLD.BEER_BREWING_DISTRIBUTION`
- key boundary: Cornelis is a **biersteker**, not automatically brewer or Nissepad-brewery owner.

### Reimerswaal / school / cost-pupil life

- `domains/REIMERSWAAL_SCHOOL_1554_1561.md`
- `../sources/SRC-HIST-REIMERSWAAL-SCHOOL-CITY-001.md`
- world: `WORLD.REIMERSWAAL`
- key boundary: durable historical school tradition is supported; Claes' exact curriculum, teacher/building and attendance are source-weighted novel reconstruction.

### Rederijkers / Nardusbloem / Antwerp Landjuweel 1561

- `domains/REDERIJKERS_LANDJUWEEL_1561.md`
- `../sources/SRC-HIST-REDERIJKERS-LANDJUWEEL-1561-001.md`
- `../sources/SRC-HIST-GOES-REDERIJKERS-001.md`
- key boundary: Silvius 1562 anchors fourteen official Antwerp competitors; current evidence does **not** establish Goes as one of them.

### Antwerp time slices

- `domains/ANTWERP_TIME_SLICES_1561_1585.md`
- `../sources/SRC-HIST-ANTWERP-TIMESLICES-1561-1585-001.md`
- world: `WORLD.ANTWERP`
- required slices: 1561 theatre; 1563–64 book/workshop; 1566 broken image; 1567–69 surveillance/repression; 1576–78 wound/print release; 1585 transformed formative city.

### Goes schutterij / military practice

- `domains/SCHUTTERIJ_MILITARY_PRACTICE_1550_1607.md`
- `../sources/SRC-HIST-GOES-SCHUTTERIJ-DEGHEYN-001.md`
- world: `WORLD.SCHUTTERIJ_MILITARY`
- key boundary: schuttersgilde, civic watch, garrison/professionals and later standardized drill are separate; De Gheyn 1607 is a late comparator, not a Goes-1572 manual.

## Story projection / causal architecture — Round C

Round C is the bridge from chapter-ready world knowledge to future Book/Act/Sequence/Chapter/Scene structure.

- `STORY_PROJECTION_ROUND_C.md` — human-readable governing projection.
- `ALCHEMICAL_OPERATION_PALETTE.md` — non-binding author-side palette of seven classic operations (Calcination, Sublimation, Solution, Putrefaction, Distillation, Coagulation, Tincture), with narrative, sensory and show-don't-tell applications; never a mandatory 3×7 or 21-chapter template.
- `../narrative/story_projection_round_c.yaml` — `ARC.CLAES.CAUSAL_SPINE`, fourteen current causal hinges from Status Prima to Status Prima Nova.
- `../narrative/alchemical_authorial_architecture.yaml` — `ARC.CLAES.GREAT_WORK.AUTHORIAL`: Status Prima; interwoven Corpus/Anima/Spiritus; Transmutatio/Rubedo; Projectio; Status Prima Nova.
- `../narrative/mayken_independent_arc.yaml` — `ARC.MAYKEN.LIFE`.
- `../narrative/mayken_relationship_projection.yaml` — `REL.CLAES.MAYKEN.CONJUNCTIO`.
- `../narrative/goes_departure_1572_1579.yaml` — explicit open causal design projection for Claes' final material/economic severance from Goes.

### Great-Work rule

`ARC.CLAES.MACRO_TRANSMUTATION` remains the chronological **Drager → Nigredo → Albedo → Rubedo → Projectio** spine. The deeper Round-C architecture does not replace it.

**Status Prima → Corpus / Anima / Spiritus → Transmutatio/Rubedo → Projectio → Status Prima Nova** is an author-side register model. Corpus/Anima/Spiritus spiral through the same chronology and must not become three mechanically identical cycles. No fixed alchemical operation count is mandatory.

The seven-operation palette is therefore a **compositional and diagnostic vocabulary only**. Use an operation when a scene's actual material, relational or inner causality earns it; never reverse-engineer a scene solely to satisfy the palette.

### Mayken rule

`ENT.PERSON.BELOVED` is the legacy technical entity ID for the resolved character **Mayken Adriaensdr. Lampert**. Identity is not open.

Any developed Mayken scene must load `ARC.MAYKEN.LIFE` as well as the Claes–Mayken relationship. Mayken requires her own objective, judgement, cost or choice.

### Current high-priority Round-C open hinges

- `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001`
- `OPEN.MAYKEN.INDEPENDENT_MIDARC.001`

## Writing / editorial / reader-experience layer — Round D

Round D is the required implementation/evaluation layer between story architecture and accepted prose.

### Human-facing authority

- `../WRITING_PROTOCOL.md` — complete drafting/revision protocol.
- `../review/READER_EXPERIENCE_PROTOCOL.md` — reader-experience, cold-reader and human pilot-reader method.
- `../review/READER_FEEDBACK_TEMPLATE.md` — reusable reader-feedback record.
- `../review/EDITORIAL_PROTOCOL_ROUND_D_2026-08-16.md` — Round-D recovery audit.

### Machine-readable gates

`../narrative/editorial_gates.yaml` contains:

- `GRD.EDITORIAL.SCENE_NECESSITY`
- `GRD.EDITORIAL.PROSE_QUALITY`
- `GRD.EDITORIAL.PACING`
- `GRD.EDITORIAL.READER_EXPERIENCE`
- `GRD.EDITORIAL.COLD_READER`
- `GRD.EDITORIAL.PILOT_READER`
- `GRD.EDITORIAL.RUTHLESS_EDITOR`

### Scene-retention rule

Every developed scene is tested for plot, character, information and reader-experience necessity, followed by a uniqueness test.

Verdict:

**RETAIN / REVISE / MERGE / CUT**.

Research effort, historical richness, symbolism or beautiful prose is not enough by itself to retain a scene.

### Cold-reader / pilot-reader rule

A cold-reader pass receives prose without hidden Storybible explanation. AI may simulate the restricted-context pass, but **AI cold-reader simulation is not a substitute for actual human pilot readers**.

Human feedback logs reported experience/problem separately from reader-proposed fix. Repeated independent observations carry more revision weight than isolated preference; reader voting never decides canon.

### Meedogenloze redacteur

Standing hard-review mode under `GRD.EDITORIAL.RUTHLESS_EDITOR`:

> **Niet aardig, wel precies. Als een scène niet werkt, zeg dat. Geen complimenten en geen verzachtende formuleringen wanneer die de diagnose vertroebelen.**

## Story truth

- `../claims/STORY_CLAIMS.yaml`
- `../claims/STORY_CLAIMS_EXECUTIONS_REFORMATION.yaml`
- `../claims/STORY_CLAIMS_FAMILY_1554.yaml`
- `../claims/STORY_CLAIMS_2026-08-14.yaml`
- `../claims/STORY_CLAIMS_GOES_CLERGY_2026-08-16.yaml` — canonical scene-use boundaries for Mathijs and Clemens.
- `../claims/STORY_CLAIMS_MAYKEN_LAMPERT.yaml`
- `../claims/STORY_CLAIMS_ALCHEMY_REFINEMENT_2026-08-16.yaml`
- `../claims/STORY_CLAIMS_HOUSE_OF_LOVE_NETWORK_2026-08-16.yaml` — Cornelis' commercial trust bridge, Dens/Barrefelt affiliation, pre-fire state, later Plantin node and beer-to-paper logistics continuity.

## People and relationships

- `../entities/ENTITIES.yaml`
- `../entities/FAMILY_1554.yaml`
- `../entities/GOES_CLERGY_1541_1564.yaml` — historical Mathijs Jacopsen/Jacobsen and Clemens van den Dale entity supplement.
- `../entities/MAYKEN_LAMPERT.yaml`
- `../entities/ALCHEMY_REDERIJKER_2026-08-16.yaml`
- `../entities/HOUSE_OF_LOVE_NETWORK_2026-08-16.yaml` — Ghysbrecht, Dens, Barrefelt, Plantin, translocal network entity and canonical Cornelis relationships.
- `../narrative/relationships.yaml`
- `../narrative/arcs.yaml`
- `../narrative/sinne_recovery.yaml`
- `../narrative/beloved_recovery.yaml` — resolved Mayken identity; no longer an open-identity layer.
- `../narrative/mayken_independent_arc.yaml`
- `../narrative/mayken_relationship_projection.yaml`

## Major Storybible dossiers

### Goes / family / church

- `FAMILY_CLAES_1542_1554.md`
- `GOES_CLERGY_MATHIJS_CLEMENS_1541_1564.md` — governing named-clergy dossier; Mathijs is safe for 1541/early-1542 scenes, not automatically for 8 December 1542; Clemens is verified in 1564.
- `../narrative/world_goes_living_city.yaml`
- `../narrative/world_goes_grote_kerk.yaml`
- `../narrative/world_goes_clergy_1541_1564.yaml`
- `../entities/GOES_LIVING_CITY.yaml`
- `../entities/GOES_GROTE_KERK.yaml`
- `../entities/GOES_CLERGY_1541_1564.yaml`
- `modules/WORLD_GOES_CHURCH_LOCAL.md`
- `modules/WORLD_GOES_CHURCH_LITURGICAL_GUARDRAILS.md`

### Mayken

- `MAYKEN_LAMPERT.md`
- `../narrative/mayken_independent_arc.yaml`
- `../narrative/mayken_relationship_projection.yaml`
- `../sources/SRC-HIST-GOES-LAMPERT-APOTHECARY-001.md`

### Cornelis / Huis der Liefde / Antwerp route

- `CORNELIS_HOUSE_OF_LOVE_NETWORK_1551_1569.md` — governing dossier; commercial trust → Ghysbrecht → fictional bridge to Dens → Barrefelt → Huis der Liefde; Plantin later.
- `../canon/DECISIONS_HOUSE_OF_LOVE_NETWORK_2026-08-16.yaml`
- `../claims/SOURCE_CLAIMS_HOUSE_OF_LOVE_NETWORK_2026-08-16.yaml`
- `../claims/STORY_CLAIMS_HOUSE_OF_LOVE_NETWORK_2026-08-16.yaml`
- `../entities/HOUSE_OF_LOVE_NETWORK_2026-08-16.yaml`
- `../sources/SRC-HIST-HOUSE-OF-LOVE-GOES-ANTWERP-1551-1569-001.md`
- `CORNELIS_EXECUTION_1569.md` — later legal/execution consequence layer; the new dossier supplies the longer network backstory.

### Memoriaal / Brevísima

- `MEMORIAAL_BREVISIMA_PRINT_1564.md`
- `MEMORIAAL_BREVISIMA_CASTOFF_1564.md`
- `../narrative/code_architecture.yaml` — legacy filename; current content is direct material reveal, not a cipher architecture.

### Execution / Reformation

- `CORNELIS_EXECUTION_1569.md`
- `EXECUTIONS_REFORMATION_CLAES_2026-08-16.md`
- `EXECUTIONS_REFORMATION_CLAES.md` — older source-rich dossier where not superseded.
- `modules/PUBLIC_OPINION_IDENTITY_REVOLT.md`

### Alchemy / Antwerp / Enkhuizen

- `ALCHEMICAL_CHEMICAL_PROCESS_CHAIN_CLAES_LIFELINE.md`
- `ALCHEMICAL_PROCESS_REFINEMENT_2026-08-16.md`
- `ALCHEMICAL_OPERATION_PALETTE.md`
- `ANTWERP_THREE_VISITS_ALCHEMICAL_ARC_1561_1569.md`
- `../narrative/alchemical_authorial_architecture.yaml`
- `../objects/ALCHEMY_OBJECTS_2026-08-16.yaml`
- `../narrative/alchemy_lifeline_refinement_2026-08-16.yaml`
- `../narrative/instances_alchemy_rederijker_2026-08-16.yaml`
- `../narrative/knowledge_states_alchemy_2026-08-16.yaml`

## Narrative realization

- `../narrative/story_projection_round_c.yaml` — causal pre-structure; load before final chapter architecture.
- `../narrative/instances.yaml`
- `../narrative/instances_executions_reformation.yaml`
- `../narrative/instances_alchemy_rederijker_2026-08-16.yaml`
- `../narrative/domain_scene_packs.yaml`
- `../narrative/world_goes_clergy_1541_1564.yaml`
- `../narrative/editorial_gates.yaml`
- `../narrative/scenes.yaml`
- `../narrative/structure.yaml`
- `../narrative/motifs.yaml`
- `../narrative/themes.yaml`
- `../narrative/CRAFT_GUARDRAILS.yaml`
- `../narrative/religious_space_sensory_church.yaml`

Current limitation: `structure.yaml` still needs populated Book/Act/Sequence/Chapter/Beat hierarchy and `scenes.yaml` needs many more scene-level diagnostics. Rounds A–D now supply the evidence, world, causal and editorial infrastructure to populate them without reverting to research-led scene accumulation.

## Objects

- `../objects/OBJECTS.yaml`
- `../objects/ALCHEMY_OBJECTS_2026-08-16.yaml`

Key rules:

- memoriaal = pre-bound carrier of readable hidden Brevísima;
- graphite rule = visible note layer + protection of latent tannin print;
- Zovitius = possible material cue, not cryptographic key;
- merels = independent game/motif, not recovery system;
- Rode Leeuw = deep red/red-brown completed projectiepoeder carrying already-present Sol;
- Seton = late alchemical mirror only, never Brevísima decoder.

## Deterministic engine

- `../lemma/core.lemma`
- `../lemma/knowledge.lemma`
- `../lemma/events.lemma`
- `../lemma/encounters.lemma`
- `../lemma/objects.lemma`
- `../lemma/clues.lemma`
- `../lemma/decode.lemma` — legacy filename; active rule concerns direct readable reveal.
- `../lemma/consistency.lemma`

## Conversion and review

- `../mapping/CONVERSION_LEDGER.yaml`
- `../mapping/CONVERSION_REPORT.yaml`
- `../review/MIGRATION_REVIEW.yaml`
- `../review/CANON_CONFLICT_AUDIT_2026-08-16.md`
- `../review/HISTORICAL_SUBSTRATE_RECOVERY_2026-08-16.md`
- `../review/DOMAIN_REBUILD_ROUND_B_2026-08-16.md`
- `../review/STORY_PROJECTION_ROUND_C_2026-08-16.md`
- `../review/EDITORIAL_PROTOCOL_ROUND_D_2026-08-16.md`
- `../review/READER_EXPERIENCE_PROTOCOL.md`
- `../review/READER_FEEDBACK_TEMPLATE.md`
- `../review/CHAT_COMMITMENT_AUDIT_2026-08-13.md` and addendum
- `../review/SYNC_STATUS.md`

## Validation

- `../scripts/validate_canon.py`
- `../scripts/validate_active_projection.py`
- `../.github/workflows/canon-repository-validate.yml`
- `../.github/workflows/lemma-validate.yml`

GitHub canon remains authoritative. Later explicit author decisions override stale broad prose; no AI may silently turn plausibility, editorial preference or reader suggestion into canon.
```

---

# SOURCE FILE: `storybible/LEMMA_MCKEE_MASTER.md`

```markdown
# Claes Nissepat — Lemma/McKee Storybible Master

**ID:** `SB.CLAES.LEMMA_MCKEE`  
**Status:** CURRENT OPERATING SYNTHESIS  
**Synchronized:** 16 August 2026 — through Round C story projection and Cornelis/Huis der Liefde network decision  
**Source authority:** `SB.CLAES.MASTER`

This is the current human-readable operating synthesis of the Claes canon. The dated `LEMMA_MCKEE_MASTER_2026-08-13.md` is a historical snapshot only. Where older prose describes a 1545 birth, post-4-October loading of the memoriaal, a 24×24/cipher recovery chain, Cornelis' death as still open, Cornelis as a straightforward member of the Edele Castanienbloem, Plantin as Cornelis' converter into the Huis der Liefde, or Mayken's identity as still open, that wording is superseded.

The project separates five working layers:

1. **Source Claim (`SC.*`)** — what evidence supports.
2. **Story Claim / Decision (`STC.*`, `DEC.*`)** — what is true or explicitly chosen in the novel.
3. **World/practice state (`WORLD.*`, domain dossiers, scene packs)** — what can plausibly happen in a place/time/activity.
4. **Narrative projection (`NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`)** — where and why story change happens.
5. **Lemma constraint** — only deterministic continuity that can be evaluated safely.

---

## 1. Governing story proposition

### Controlling idea

A man who spends his life seeking hidden order becomes whole only when knowledge ceases to be a means of control and becomes a responsibility toward other people.

### Core dramatic question

What does truth ask of Claes toward the other when certainty, safety and control are impossible?

### Character engine

- **Conscious desire:** understand the hidden order behind visible reality.
- **Psychological need:** recover trust in embodied perception and act without complete certainty.
- **Moral need:** understand that knowledge increases responsibility toward others.
- **Gift:** prolonged, precise, embodied perception — *sinne*.
- **Shadow:** remaining in observation after the moment for action has arrived.
- **Childhood wound:** if I had seen early enough, perhaps I could have prevented the loss.
- **Adult lie:** if I understand the process, I can control the consequences.
- **Final truth:** mastery is incomplete until it can be released without possession.

Canonical anchors include `DEC.CLAES.SINNE.2026-08-13`, `DEC.CLAES.PARADOX.2026-08-13`, `DEC.CLAES.NEED.2026-08-13`, `DEC.CLAES.SPIRITUAL_JOURNEY.2026-08-13` and the Round-C authorial architecture decision.

---

## 2. Macrostructure — two nested alchemical layers

### Operational chronological spine

| Phase | Story time | Claes' movement | Fixed hinges |
|---|---|---|---|
| **DRAGER** | 1542–4 Oct 1564 | receive → recognize → interpret → act on matter | childhood, 1554 first blackening, Reimerswaal, 1561 Landjuweel, Dee/Silvius 1563–64, memoriaal before Boom |
| **GEBONDENHEID / NIGREDO** | 4 Oct 1564–1584 | act → become entangled → lose → assume responsibility | Fabritius/security hinge, 1567 first Cornelis arrest, 19 Nov 1569 execution, 1570 reveal, 1572–79 Goes pressure, 1578 print, Delft 1584 |
| **ONDERSCHEIDING / ALBEDO** | 1584–ca.1599 | distinguish confused values | truth ≠ certainty; knowledge ≠ control; protection ≠ possession |
| **VERBINDING / RUBEDO** | ca.1599–1602 | reconnect in right proportion | recovered *sinne*, Mayken, love and material practice |
| **PROJECTIO / OVERDRACHT** | 1602+ | prove → release → transmit | Enkhuizen 13 Mar 1602; final merels/death still open |

Hard guardrails:

- 1554 is Claes' first personal **micro-Nigredo**, not the start of the adult macro-Nigredo.
- **4 October 1564** is the adult macro-Nigredo/security hinge.
- 4 October changes **network risk**, not the physical content of the memoriaal.
- **1578** completes the textual mission: projectio of the Word.
- **1602** is projectio of Matter: the late alchemical test.
- **After 1602** comes projectio of the Self: can Claes release ownership/control?

### Deeper Great-Work authorial architecture

`DEC.CLAES.GREAT_WORK.AUTHORIAL_ARCHITECTURE.2026-08-16` fixes the deeper author-side model:

**Status Prima → Corpus / Anima / Spiritus → Transmutatio/Rubedo → Projectio → Status Prima Nova**.

This architecture **nests with, and does not replace,** the chronological macro arc above.

- **Corpus** — bodies, food, beer, paper, plants, buildings, fire, water, salts, vitriol, metals, tools, roads and cities undergo actual material change.
- **Anima** — meaning, belief, language, loyalty, testimony, memory, love and public interpretation are separated and recombined.
- **Spiritus** — Claes' vigilance, certainty-seeking, grief, agency, embodied *sinne*, responsibility and sovereignty change.

Corpus, Anima and Spiritus are simultaneous spiral registers. They are **not** three successive books or three mechanically identical cycles.

`Solve et Coagula` is an authorial movement: separate what has been falsely fused, then reconnect what can enter a truer relation.

The recovered longer operation vocabulary — ontvangen, verbranden, oplossen, onderscheiden, verheffen, gebruikt worden, scheiden, verrotten, verenigen, verliezen, herhalen, zwart worden, wit worden, rijpen, rood worden, projecteren, loslaten — is diagnostic only. No fixed operation count is mandatory and no scene receives a label merely to complete a pattern.

> **The author knows the Work; Claes undergoes it; the reader experiences it.**

---

## 3. Claes — cradle to grave / causal spine

`ARC.CLAES.CAUSAL_SPINE` is the current pre-structure for eventual Book/Act/Sequence/Chapter/Scene realization.

### I — 8 December 1542–ca.1547: body before meaning / Status Prima

Claes is born in Goes on **8 December 1542**. Early knowledge begins in warmth, cold, smell, light, sound, hunger, rhythm and touch. The body knows before the mind explains.

### II — ca.1547–18 May 1554: discovering order

The household consists of Cornelis, Tanneken, Claes, younger brother **Jan Corneliszn. Nissepat** and, immediately before the fire, an unborn child. Cornelis teaches attention and craft; Tanneken teaches ordinary embodied knowing; Jan gives play, rivalry and action.

The family home is the fictional household use of the historically documented 1542 Nissepat house in the older Nieuwstraat/Armenhoek environment.

Bread, beer, church, household work and routes belong to Claes' first epistemology. His useful childhood intuition — careful attention makes the world legible — becomes the seed of his later false hope that enough attention might prevent loss.

Cornelis' own Antwerp network also begins in this pre-fire world. A historical **Ghysbrecht/Gijsbrecht, kuiper van Antwerpen** with Goese property interests is the archival anchor; in novel canon repeated cask/beer dealings create a trusted commercial relation. The bridge from Ghysbrecht to **Adriaan Dens** is explicit fiction. Dens becomes the first person Cornelis knowingly recognizes as belonging to H.N.'s circle and routes him onward to **Hendrik Jansen van Barrefelt**. By approximately **1552–1553** Cornelis belongs in novel canon to the translocal Huis der Liefde while remaining publicly embedded in Catholic Goes. Plantin is not his converter.

### III — 18 May 1554–1561: first blackening and Reimerswaal

The Goes fire destroys or makes the family house uninhabitable in novel canon. Claes and Cornelis survive because they are away; Tanneken, Jan and the unborn child die. Historical evidence supports a partially damaged old-Nieuwstraat/Armenhoek environment but does not document these fictional casualties.

For Cornelis the fire therefore **tests an already existing Familist conviction; it does not create it**. The same catastrophe also leaves Ghysbrecht's Goese property represented as burned in the 1554 archival record, allowing the trade relation to remain materially connected to the memory of burned Goes without making the two men's losses equivalent.

Cornelis remains in Goes to rebuild livelihood and finance Claes' education. Zierikzee becomes unaffordable; Claes goes to Reimerswaal. The separation is care experienced as another loss.

Reimerswaal remains a functioning city while recurrent water damage, repairs and later fire teach another form of impermanence. School gives Claes rule, memory and language; the threatened city turns attention increasingly into vigilance. The exact 1554 curriculum, teacher and school building remain reconstruction rather than archival fact.

### IV — 1561–1563: Antwerp and interpretive plurality

In August 1561 Claes travels with Cornelis from Reimerswaal to the Antwerp Landjuweel and does not return. Dee is **not** placed at the Landjuweel.

The contemporary Silvius event record anchors fourteen official competing chambers. Current evidence does **not** establish a Goese chamber among those official competitors; Claes and Cornelis may nevertheless attend, observe and network in novel canon.

Rhetoric, theatre, trade and print teach that carrier, appearance, intention and meaning can diverge. One sign can mean differently to chamber, spectator, judge, magistrate and printer.

### V — 1563–early 1564: Dee, Silvius and matter

Claes first encounters Dee briefly in 1563; intensive formation follows in early 1564. Dee moves him from observation toward hypothesis and intervention.

Before the journey to Boom, Dee gives Claes:

- `OBJ.MEMORIAAL`, already bound from sheets carrying the hidden readable Diets/Brabant *Brevísima*;
- `OBJ.GRAPHITE_STIFT`;
- the prohibition against writing in the book with ink while Claes remains his pupil.

Claes thinks he has a pedagogical workbook. He does not know the hidden text or the material reason for the graphite rule.

Print, graphite, pyritic matter, vitriol and the Sol problem teach him that apparent absence may conceal material continuity and that right relation can achieve what brute force cannot. This is genuine knowledge — and the seed of the adult lie that understanding a process may grant control over consequences.

### VI — 4 October 1564–19 November 1569: network danger and the father

Christoffel Fabritius' disrupted Antwerp execution on **4 October 1564** is the preferred historical candidate for the existing security hinge. The exact low-level link by which Cornelis becomes unsafe remains `OPEN.SECURITY.LOW_LINK.1564.001`.

By this point Cornelis has already belonged to the Huis der Liefde for more than a decade in novel canon. His route is **beer/cask commerce → Ghysbrecht → fictional social bridge to Dens → Barrefelt → translocal affiliation**. He can remain outwardly Catholic in Goes; no separate Goese Familist congregation or invented initiation ritual is required. His later paper/book carrying grows out of the same competencies as the beer trade — containers, storage, accounts, credit, route knowledge, carrier choice, discretion and trust — but this does **not** mean that books are routinely hidden in beer casks.

**Plantin is a later print/distribution node, not Cornelis' converter.** His historically substantial relation to the Niclaes/Barrefelt milieu may support later network scenes, but the historiography of Plantin's own adherence must not be flattened into a simple permanent sect label.

The crucial correction is negative: nothing is inserted, keyed or reciphered in Claes' memoriaal after 4 October 1564. Cornelis' long Familist backstory does not by itself close the exact low-level security trigger.

Cornelis' fall is fixed as a two-step exposure:

1. **autumn 1567, Antwerp:** first arrest or serious examination in a book/paper matter; release on borg or equivalent conditions;
2. **late 1568–1569:** renewed exposure through clandestine book/paper traffic, network traces and refusal to name others.

On **19 November 1569** Cornelis is fictionally executed in Antwerp in the documented Grote-Markt/stadhuis book-burning environment. Public beheading by sword is the preferred story method under the recidive/seditious-network framing. Claes is physically present.

Cornelis is not a historical addition to Haecht's list, not a protected printer, not an open preacher and not carrying the memoriaal. His death-script is protective silence: he gives no names. The new network backstory makes that silence the terminal consequence of a long practice of trust rather than a last-minute heroic pose.

The father's vulnerable body and the possible separate destruction of papers/books teach that testimony can survive a carrier without becoming immaterial. Claes inherits responsibility, not a final key.

### VII — 1570–1578: reveal, Mayken and projectio of the Word

A special 1570 Zovitius copy may provide the material cue **GALLA LEO VIRIDIS**. It is a cue, not a key.

Green vitriol develops the tannin-loaded typographic letterforms in the memoriaal. What appears is already ordinary readable Diets/Brabant language.

Therefore:

- reveal is **reading**, not decryption;
- there is no 24×24 recovery matrix;
- no nomenclator is required;
- merels is not a recovery key;
- Monas is not a permutation key for the *Brevísima*;
- Castanea is not a key anchor;
- no special Dodoens carrier is required;
- no Primus Index is required;
- no multi-week cryptographic reconstruction is required.

Mayken participates as an independently competent adult. She may handle, measure, observe, read, repeat tests and contradict Claes. She is not a key-holder or replacement solver. Her participation must have a reason and accepted risk of her own, not merely obedience to Claes.

The revealed words shift the dramatic problem from **what is hidden?** to **what does this readable truth require of us?**

The exact human/production route from reveal to publication remains open, but the endpoint is fixed: **Antwerp, 1578, printed publication**. This is the **projectio of the Word**: dangerous testimony is multiplied and released beyond Claes' control.

### VIII — 1572–1579: Goes second severance — explicit open hinge

The source-grounded pressure is fixed but the personal causal chain is not.

Historically supported:

- the 1572 siege damages/burns outside salt works and a brewery in the Voorstad;
- a Nissepad brewery with equipment is documented in 1577;
- that Nissepad brewery is not proven identical to the 1572 burned Voorstad brewery and is not proven Cornelis' property;
- Jan Jansen Nissepat sells a burned Westzelke salt-pan site in 1577, but the destructive event is not identified;
- 1577–1579 property transfers do not automatically prove confiscation, execution sale or forced liquidation.

The open novel question is `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001`: **which chain of actual damage, fictional residual interest, debts/claims, legal settlement and network collapse finally makes Goes cease to function as Claes' recoverable home/economic base, and when does he leave?**

Do not solve this by silently destroying the documented Nissepad brewery. A cumulative model or a combination of one real material loss plus postwar financial/legal afterlife is currently the safer design space, but it remains authorial design rather than canon.

### IX — 1578–1584: knowledge fails as protection

Claes' wound changes from *I did not see early enough* to *I saw, and still did not do enough*.

Delft 1584 remains the moral bottom and threshold toward Albedo. The problem is no longer finding hidden truth but acting when truth does not guarantee a safe or clean outcome.

### X — 1584–1602: Albedo, Rubedo, Mayken and conjunctio

Claes must distinguish:

- truth from certainty;
- knowledge from control;
- secrecy from isolation;
- protection from possession;
- belief from dogma;
- love from holding on.

His relationship with **Mayken Adriaensdr. Lampert** becomes one of the primary relational/material counterforces. She is a fictional Goese apothecary daughter, ca.1546, grounded in the historically attested Lampart/Lambert/Lampert apothecary milieu. Her family also knows the 1554 fire through the burned *Zwaene* property, but her trauma is not Claes' duplicate.

Her epistemology is practical: materia medica, preparation, weighing, smell, texture, condition, repeatability and contradiction.

The mature relationship has the author-side function of **conjunctio**: two unlike modes of knowing can enter reciprocal relation without one absorbing the other. This is not mandatory in-world terminology. Mayken is not the missing ingredient that completes Claes; Claes is not entitled to her because he suffers.

On the road toward Enkhuizen, shared material life — weather, plants, food, preparation, fatigue, touch, sound, disagreement — helps Claes reopen the *sinne*. She catalyses; she does not cure or complete him. The scene architecture must preserve two centers of agency and advance Mayken's own arc as well as Claes'.

### XI — 13 March 1602 and after: projectio of Matter, Self and Status Prima Nova

The Enkhuizen climax is anchored to the retrospective Seton tradition transmitted by Daniel Georg Morhof:

- **Enkhuizen**;
- house of sailor **Jacob Hausfsen**;
- **13 March 1602**;
- approximately **16:00**;
- Alexander Seton/Sidonius as the historical-tradition figure.

Morhof writes around seventy years later. These are chosen story-frame facts, not contemporaneously verified eyewitness facts.

The alchemical rule is: **what becomes visible was already materially present**. The Sol seen in the late assay was already present in the process; the novel does not create gold from lead. The Rode Leeuw is deep red to red-brown and carries the already-present Sol in a still-open non-gold matrix.

Seton has **no** role in the *Brevísima*. He is a late mirror for Claes' relation to mastery, proof, coercive power and possession.

Status Prima Nova is not restored childhood. Mature *sinne* becomes:

**perceive → distinguish → choose → carry → release.**

Claes' exact death remains open. Its function does not: he must finally be able to transfer without owning the recipient's choice, the Work or its outcome.

---

## 4. Cornelis — occupation, Huis der Liefde and rederijker identity

Fixed:

- Goes poorter;
- **biersteker**, not fixed brewery owner;
- book/material carrier through commercial and trust networks;
- rederijker;
- member in novel canon of the translocal **Huis der Liefde / Familia Caritatis** by ca. **1552–1553**;
- not a printer.

His entry route is fixed as:

**beer/cask commerce → Ghysbrecht/Gijsbrecht, kuiper van Antwerpen → explicit fictional trusted bridge to Adriaan Dens → Hendrik Jansen van Barrefelt → Huis der Liefde.**

Evidence boundary:

- Ghysbrecht/Gijsbrecht is a historical Antwerp cooper with Goese property interests in the 1551/1554 archival record;
- same-person identification across the two records is a supported inference;
- Ghysbrecht is **not** a documented Familist;
- no historical Ghysbrecht–Dens relationship is claimed;
- the Ghysbrecht → Dens bridge and Cornelis' meetings are novel canon;
- Dens and Barrefelt are historical actors whose known network positions make their story roles plausible.

Dens is Cornelis' first knowingly identifiable Familist. Barrefelt deepens the affiliation and connects Cornelis' local/commercial trust to the wider translocal text network. Cornelis may remain outwardly embedded in Catholic Goes; no separate Goese Familist church, meetinghouse, hierarchy or formal initiation ritual is required.

The **18 May 1554** fire tests this pre-existing affiliation; it does not cause the conversion. Plantin enters only later as a print/distribution node. His role must never collapse the chain into “Cornelis meets Plantin and becomes a Familist.”

Cornelis' later clandestine book/paper logistics grow from the same competencies as the beer trade: casks and containers, storage, accounts, credit, route knowledge, carriers, repeated transactions, discretion and trust. This continuity does **not** establish routine hiding of forbidden books inside beer barrels.

His named chamber is fixed as the **Nardusbloem / older Magdalena-linked Goese tradition**. The Zusterhuis/Singelstraat remains the Cornelis-era meeting environment.

In novel canon Cornelis helps form a reform-minded/protestantiserende current in the 1560s that becomes the later Edele Castanienbloem. This is explicit historical fiction in a documentary gap. **1595 is the earliest surviving attestation, not a proved foundation date.** Later documented Nissepat participation in 1595–1596 acts as resonance.

Whether Cornelis ever serves as **deken** remains open.

The governing dedicated dossier is `CORNELIS_HOUSE_OF_LOVE_NETWORK_1551_1569.md`. The exact low-level 4 October 1564 security trigger remains open despite this now-fixed longer backstory.

---

## 5. Mayken — independent character arc

`ENT.PERSON.BELOVED` is the legacy stable entity ID for the resolved character **Mayken Adriaensdr. Lampert**. Her identity is not open.

`ARC.MAYKEN.LIFE` now governs her independent narrative line.

### Childhood material formation

Mayken grows within the fictional daughter-line of the historically anchored Lampert apothecary environment. Her first epistemology is practical identification: what is this substance, what condition is it in, has it been substituted, spoiled, dampened, dried, measured or prepared correctly?

### 1554 — destruction plus rebuilding

The burned *Zwaene* property gives her a historically anchored fire horizon without duplicating Claes' bereavement. Her counter-memory is that material destruction is real **and** that hands can sometimes return to sorting, repairing and working.

### Adult judgement before Claes

Inherited competence must become personally owned judgement before Mayken functions as Claes' equal. The exact event chain remains `OPEN.MAYKEN.INDEPENDENT_MIDARC.001`.

Earlier development considered family/social pressure, possible loss of standing or displacement and stronger reliance on female practical-healing/herbal networks. That remains a candidate to revalidate, **not current event canon**. Do not copy Cornelis' prosecution history onto Adriaen or invent university/physician/guild status.

### 1570 — shared risk

Mayken chooses whether to participate in dangerous material verification and testimony. Her function is not “helping Claes solve it”; her value is independent observation and the capacity to tell him when matter contradicts his elegant interpretation.

### 1571–1584 — no off-screen waiting role

Future structure must give Mayken continuing work, obligations, constraints and choices. The diagnostic question is:

> **What does Mayken want or refuse here if Claes were absent?**

### Late relation

`REL.CLAES.MAYKEN.CONJUNCTIO` requires two centers of agency. Mayken may catalyse Claes' recovery while remaining fallible, separate, contradictory and capable of refusal. Mature love is relation without possession, not sameness.

---

## 6. Chapter-ready world projection

Round-B domain dossiers are active inputs to story construction:

- bread/grain/baking;
- beer/biersteker/brewery economy;
- Reimerswaal school/cost-pupil life;
- rederijker/Nardusbloem/Landjuweel practice;
- Antwerp time slices;
- Goes schutterij/military practice;
- sensory church/historical substrate recovered in Round A.

`narrative/domain_scene_packs.yaml` supplies machine-readable scene contexts. A pack constrains world state and activity; it does not create a fictional scene.

For chapter construction the sequence is now:

**causal hinge → character choice/pressure → relevant Corpus/Anima/Spiritus register(s) → domain scene pack/world state → value/knowledge/relationship/object change → scene diagnostics.**

Do not reverse this into “we researched bread, so we need a bread chapter.”

---

## 7. Object biographies

### `OBJ.MEMORIAAL`

Readable Diets/Brabant *Brevísima* set in ordinary movable type → printed nearly invisibly with tannin/gallnut + gum arabic before binding → folded/gathered into 17 single-sheet quarto gatherings → Dee gives the already prepared book to Claes before Boom → Claes writes only in graphite → green vitriol later reveals the already readable text.

Canonical capacity: **17 sheets = 68 leaves = 136 latent pages**, plus any genuinely blank binder endleaves.

### `OBJ.GRAPHITE_STIFT`

Story function fixed; exact historically defensible physical form/provenance remains open. Do not automatically render a later standardized wood-cased pencil.

### `OBJ.ZOVITIUS_1570_TRIGGER`

May cue `GALLA LEO VIRIDIS` and activate memory/material testing. It does not contain a cryptographic key.

### Merels

Merels remains a game, a learned skill, a relationship device and a thematic model of visible pieces versus invisible routes. It is **independent of Brevísima recovery**.

### Dodoens / Monas / Castanea

They may remain where they independently serve history, botany, education, symbolism or character. They do not form a required decryption chain.

### Rode Leeuw / Sol

Rode Leeuw = Claes' completed red/red-brown projectiepoeder stage in novel canon. It is not green and not visibly gold-yellow. Its exact non-gold carrier matrix remains open. The gold-bearing fraction is materially continuous; no later silent gold addition is allowed.

---

## 8. Alchemical material process grammar

Current chain:

`kies / pyritic rejected matter → weathering + water + air + time → vitrioolwater / green vitriol / operational Groene Leeuw → direct tannin-text reveal + learned opening principle → ordinary strong-water failure on Sol → right compound relation → death/opening of Sol → materially continuous hidden Sol → red fixation / Rode Leeuw → Saturn/lead → assay/cupellation-like reveal → projectio → release`

Guardrails:

- “Groene Leeuw” is operational vocabulary in this process, not a universal historical equation with FeSO4.
- Green vitriol reveals the memoriaal directly; it does not directly dissolve gold.
- A strong water must first **fail** against Sol before the lesson of right proportion/relation becomes clear.
- Cupellation-like explanation is authorial historical-chemical reconstruction, not a documented Seton procedure.
- Do not use routine tasting of vitriol or corrosive liquids.
- Prefer technically defensible terms such as `vitrioolwater`, `uitloogwater`, `oplossing` or `liquor`; the chapter title *De loog van Antwerpen* may remain.
- Material process remains causal reality; symbolic structure never substitutes for the actual process.

---

## 9. Execution / testimony arc

Claes begins within a Catholic civic ars-moriendi understanding: punishment, confession, priestly consolation, repentance and public compassion can belong to one death script.

Reformation executions fracture that shared script. Condemned persons and spectators can convert punishment into witness through steadfastness, psalms, letters, songs and memory.

Cornelis forms a third script: **protective silence**. He does not die as a loud martyr but refuses names. The fixed Huis der Liefde backstory makes that silence continuous with more than a decade of learned relational trust, discretion and protection of other carriers.

The thematic carrier chain is now:

**body → suppression/destruction → memory/letter/song/book → chemically hidden writing → public print**.

Do not reintroduce “code” as necessary testimony mechanism for the *Brevísima*.

---

## 10. Open decisions — active backlog only

The canonical active registry is `canon/OPEN_DECISIONS.yaml`, supplemented by `canon/OPEN_DECISIONS_ALCHEMY_REFINEMENT_2026-08-16.yaml`.

High-value remaining questions include:

- exact circumstances/place/cause of Claes' death;
- Spanish→Diets translator/source route in 1564;
- physical wet/press validation of tannin/gum printing;
- exact graphite-stift form/provenance;
- exact low-level Fabritius→Cornelis security link;
- exact Zovitius delivery route;
- exact 1570→1578 publication/transmission chain;
- 1564 chapter calendar audit;
- exact **1572–1579 Goes material/economic/legal severance and departure causality**;
- exact **Mayken independent adult mid-arc work/family/social-pressure line**;
- final merels opponent/stakes/action;
- whether Cornelis ever serves as deken;
- exact non-gold Rode Leeuw carrier composition;
- exact Enkhuizen furnace/assay choreography and additional witnesses.

Open scene choices such as Radermacher and the bakery remain authorial design decisions, not research problems that evidence can necessarily close.

Round-C opens `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001` and `OPEN.MAYKEN.INDEPENDENT_MIDARC.001` are **authorial design opens**. Historical plausibility alone does not close them.

---

## 11. Narrative development still required

The project now has a causal pre-structure but not yet a fully populated novel structure.

`narrative/structure.yaml` still needs actual Book/Act/Sequence/Chapter/Beat population. `narrative/scenes.yaml` contains only a small fraction of the full scene analyses the novel requires.

Use `ARC.CLAES.CAUSAL_SPINE` as the governing bridge. Current hinge targets are:

1. childhood Status Prima / embodied Goes, including Cornelis' pre-fire beer/cask trust network and ca.1552–1553 Huis der Liefde affiliation as background rather than child exposition;
2. 1554 fire and survivor separation — fire tests Cornelis' existing conviction rather than causing it;
3. Reimerswaal formation under slow erosion;
4. 1561 Landjuweel / multiple interpretation;
5. Dee/Silvius/Boom material formation;
6. return to altered Goes / Mayken proximity;
7. 1567–1569 Cornelis warning, secrecy and execution, now grounded in the longer Ghysbrecht–Dens–Barrefelt trust history;
8. 1570 direct memoriaal reveal with Mayken;
9. **OPEN:** 1572–1579 Goes second material/economic severance;
10. 1578 print/release of the Word;
11. Delft 1584 moral bottom;
12. later *sinne* recovery / reciprocal Mayken line;
13. Enkhuizen 13 March 1602 / Matter;
14. post-1602 Projectio of Self / Status Prima Nova.

Each developed scene should expose objective, pressure, opening value, turning point, closing value, knowledge change, object change and arc movement. If Mayken appears, her own objective/judgement/cost must also be legible.

Before large-scale drafting, the recovered reader-experience/pacing/cold-reader/retain-revise-merge-cut/ruthless-editor protocol still requires synchronization as the next authoring layer.

---

## 12. Canon precedence

When records conflict:

1. latest explicit current `DEC.*` author decision, including dated/supplement decisions;
2. active domain-specific `STC.*` claim or explicit supersession noted by a later decision;
3. dedicated current governing dossier, including `STORY_PROJECTION_ROUND_C.md` within its domain;
4. this current `LEMMA_MCKEE_MASTER.md` synthesis;
5. synchronized structured narrative/entity/object/world/projection registers;
6. Revision 11 prose for material not yet atomized and not superseded;
7. source claims for historical support;
8. proposals/open questions;
9. dated legacy masters and session memory — audit/context only.

Lemma can reject an impossible combination but never invent story truth.
```

---

# SOURCE FILE: `storybible/STORY_PROJECTION_ROUND_C.md`

```markdown
# Story projection — Round C
## From chapter-ready world to causal character architecture

**Status:** CURRENT AUTHORING AUTHORITY FOR STORY PROJECTION  
**Date:** 16 August 2026  
**Machine layers:** `narrative/alchemical_authorial_architecture.yaml`, `narrative/mayken_independent_arc.yaml`, `narrative/mayken_relationship_projection.yaml`, `narrative/goes_departure_1572_1579.yaml`, `narrative/story_projection_round_c.yaml`

Round A restored lost historical/worldbuilding substrate. Round B made six major domains chapter-ready. Round C answers the next question: **what changes in the people because those worlds exist?**

The rule is simple:

> World detail earns space only when it creates pressure, choice, relationship, consequence or reader experience.

## 1. The Great Work — two compatible layers

The project now explicitly distinguishes two alchemical structures that must not be collapsed.

### Operational chronological macro arc

Existing and retained:

**Drager → macro-Nigredo → Albedo/Onderscheiding → Rubedo/Verbinding → Projectio/Overdracht**

This is the broad chronological transformation spine already present in `ARC.CLAES.MACRO_TRANSMUTATION`.

### Deeper author-side architecture

Recovered and fixed under `DEC.CLAES.GREAT_WORK.AUTHORIAL_ARCHITECTURE.2026-08-16`:

**Status Prima → Corpus / Anima / Spiritus → Transmutatio/Rubedo → Projectio → Status Prima Nova**

Corpus, Anima and Spiritus are **not three successive books and not three identical alchemical cycles**. They are three registers spiralling through the same life.

- **Corpus** asks what happens to matter, bodies, food, books, buildings, plants, metals, roads and cities.
- **Anima** asks what happens to meaning, belief, language, testimony, loyalty, love and social interpretation.
- **Spiritus** asks what happens to Claes' vigilance, certainty, grief, agency, sinne, responsibility and sovereignty.

A scene may work strongly in one register or in all three. The writer never has to label the operation in prose.

The governing authorial rule is:

> **The author knows the Work; Claes undergoes it; the reader experiences it.**

And the governing movement is **Solve et Coagula**: separate what has been falsely fused, then reconnect what can enter a truer relation.

## 2. No forced operation scheme

The earlier development vocabulary is restored as a **non-binding diagnostic set**:

*ontvangen — verbranden — oplossen — onderscheiden — verheffen — gebruikt worden — scheiden — verrotten — verenigen — verliezen — herhalen — zwart worden — wit worden — rijpen — rood worden — projecteren — loslaten.*

This is not a historical universal recipe and not a chapter checklist. A scene receives an operation only if the human and material causality genuinely earns it.

## 3. Claes' causal spine

`ARC.CLAES.CAUSAL_SPINE` now bridges settled canon and later chapter structure.

### Status Prima — childhood Goes

Claes' first world is not an abstract idyll. It is body, Tanneken, Cornelis, Jan, unborn sibling, bread, beer, church, market, routes, weather, work and shared timing. *Sinne* precedes theory.

His early useful belief becomes his later trap: **if attention makes the world legible, perhaps enough attention can make loss preventable.**

### 1554 — fire

Matter proves irreversible. The family catastrophe does not simply teach Claes that control is impossible; it gives him the opposite compulsion: perhaps he failed to see soon enough.

### Reimerswaal 1554–1561

Schooling gives rule and language while the city gives recurrent water, repair and instability. Attention becomes vigilance. Competence increases while openness contracts.

### Landjuweel 1561

Performance teaches that the same sign is not the same thing to performer, audience, judge, church, magistrate and printer. Observation becomes interpretation.

### Dee/Silvius/Boom 1563–1564

Material work teaches that apparent absence can conceal presence and that correct relation can reveal what force cannot. This is genuine knowledge — and the seed of Claes' adult error that complete understanding may grant control.

### Cornelis 1567–1569

Claes cannot solve the father. Cornelis' body can be destroyed, papers can burn, and yet responsibility survives. The final inheritance is moral, not cryptographic.

### Reveal 1570

The hidden words are already there. The question changes from **“what is the solution?”** to **“what does this readable truth require?”** Mayken matters precisely because material contradiction prevents Claes from making interpretation sovereign.

### Goes 1572–1579 — deliberately open causal hinge

This is now a visible, high-priority design problem rather than a hole.

Historically fixed:
- outside salt works and a brewery in the Voorstad are damaged/burned during the 1572 siege;
- a Nissepad brewery exists with equipment in 1577 and is not proven the same brewery;
- a Nissepat-linked burned Westzelke salt-pan site is sold in 1577, but the destructive event is unknown;
- later transports do not automatically mean confiscation or execution.

The unresolved novel question is: **which actual economic/material chain makes Goes cease to be Claes' recoverable home base?**

The preferred design space is not “destroy a convenient brewery”. It is more likely a combination of genuine 1572 material damage plus debts, claims, postwar settlement and network collapse. That remains OPEN until explicitly chosen.

### 1578 — Projectio of the Word

The testimony leaves Claes' possession through print. That is already a form of mastery: he cannot dictate every future reading.

### 1584 — moral Nigredo / Albedo threshold

The problem is no longer whether Claes can know enough. It is whether he can distinguish truth from certainty and right action from guaranteed success.

### Late line with Mayken

The road north is not a romantic reward sequence. It is where matter, relationship and self begin to resonate again: weather, food, fatigue, plants, preparation, touch, sound, error, disagreement and companionship.

### 1602 — Matter

The Enkhuizen event tests whether Claes can encounter material success without turning it into proof of self or an object to possess.

### Status Prima Nova — Self

The ending state is not restored childhood. Claes' mature sequence is:

**perceive → distinguish → choose → carry → release.**

## 4. Mayken is now an independent protagonist-level secondary arc

The repository had already fixed Mayken's identity and competence but still treated much of her narrative existence as a function of Claes. Round C repairs that.

`ARC.MAYKEN.LIFE` now requires her own agency.

### Childhood material formation

Mayken grows in the fictional daughter-line of the real Lampert apothecary environment. Her first epistemology is not hidden order but **material identity**: is this really what it is called; is it sound, spoiled, substituted, wet, dry, correctly weighed, correctly prepared?

### 1554 — different fire

The Lampert *Zwaene* gives her a historically anchored burned-property horizon, but her family is not annihilated. Her counter-memory is essential:

> Fire destroys; hands can sometimes return to work.

Claes learns loss as irreversibility. Mayken learns destruction **and rebuilding**.

### Adult judgement before Claes

The exact mid-arc events remain open under `OPEN.MAYKEN.INDEPENDENT_MIDARC.001`, but the required result is fixed: Mayken's inherited competence must become **her own judgement** before she can function as Claes' equal.

An earlier development seed — family/social pressure, loss of standing or expulsion followed by stronger reliance on female practical-healing/herbal networks — has been preserved as a candidate to revalidate, not silently canonized.

### 1570 — shared risk

Mayken does not “help Claes solve it”. She chooses whether to enter the risk of handling, verifying and reading dangerous testimony. Her value is that she can tell Claes: *your interpretation does not match the matter.*

### 1571–1584 — no off-screen waiting woman

This span must eventually contain Mayken's own work, obligations, constraints and choices. A future scene with Mayken must answer:

> **What does Mayken want or refuse here if Claes were absent?**

### Late conjunctio

Their mature relation is an author-side **conjunctio**, not because two halves complete each other but because two unlike wholes can remain in relation.

Claes: pattern, memory, interpretation, responsibility.  
Mayken: matter, condition, measurement, practical contradiction.

Neither becomes the other.

## 5. Relationship rule: two centers of agency

`REL.CLAES.MAYKEN.CONJUNCTIO` now governs the mature relationship projection.

For any developed Claes–Mayken scene, test:

1. Can Mayken disagree for reasons rooted in her own knowledge, work or values?
2. Does Claes receive relationship as correction rather than mere confirmation?
3. Are there still two centers of agency after intimacy deepens?
4. Would the scene still work as human drama if the word *conjunctio* were removed from the author's notes?

If not, the alchemical symbolism is compensating for a weak relationship scene.

## 6. Scene-building consequences

Round C does **not** populate Book/Act/Sequence/Chapter/Beat yet. It creates the causal bridge needed before doing so.

Every future chapter should now identify:
- which causal hinge it advances;
- which Corpus/Anima/Spiritus register(s) are active;
- which character makes the consequential choice;
- how the chapter changes Claes and/or Mayken rather than only displaying world research;
- whether an open design question is being intentionally resolved or merely used as if already canon.

Mayken's presence automatically invokes both the relationship and `ARC.MAYKEN.LIFE`. She must never be loaded only as `Claes' beloved`.

## 7. Remaining Round-C design openings

Two newly explicit high-priority authorial questions remain:

- `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001` — the exact economic/material causal chain that finally severs Claes from Goes;
- `OPEN.MAYKEN.INDEPENDENT_MIDARC.001` — the concrete work/family/social pressure through which Mayken's adult independence becomes dramatically visible.

These are now correctly open. They no longer hide as missing story structure.
```

---

# SOURCE FILE: `narrative/story_projection_round_c.yaml`

```yaml
schema_version: 1.0.0
kind: StoryProjectionRegistry
projections:
- id: ARC.CLAES.CAUSAL_SPINE
  type: CausalStoryProjection
  label: "Claes — causal spine from Status Prima to Projectio"
  canon_status: CANON
  protagonist: ENT.PERSON.CLAES
  authorial_architecture: ARC.CLAES.GREAT_WORK.AUTHORIAL
  counterpart_arc: ARC.MAYKEN.LIFE
  relationship_projection: REL.CLAES.MAYKEN.CONJUNCTIO
  purpose: "Bridge settled canon and chapter-ready world modules into a causal pre-structure before Book/Act/Sequence/Chapter/Beat realization."

  hinges:
  - id: H01
    story_time: {earliest: '1542-12-08', latest_exclusive: '1554-05-18', precision: bounded}
    label: "Status Prima — body, family, church, food, craft and routes form one lived world"
    cause: "Claes grows inside an intact household and a material/sensory civic order."
    effect: "He learns the useful but dangerous intuition that attention makes the world legible."
    registers: [Corpus, Anima, Spiritus]
    authoring_inputs: [WORLD.GOES, WORLD.BREAD_GRAIN, WORLD.BEER_BREWING_DISTRIBUTION, WORLD.RELIGIOUS_SPACE.SENSORY_CHURCH]

  - id: H02
    story_time: {date: '1554-05-18', precision: day}
    label: "Goes fire — first catastrophic solve"
    cause: "The historically grounded city fire intersects the fictional Nissepat household."
    effect: "House, mother, brother and unborn sibling are lost; Claes' belief in attention as protection is wounded rather than disproved in his own mind."
    instances: [NI.EVENT.GOES_FIRE.1554.001]
    arcs_advanced: [ARC.CLAES.LIFE, ARC.CLAES.CORNELIS, ARC.CLAES.SINNE_RECOVERY]

  - id: H03
    story_time: {earliest: '1554-05-19', latest_exclusive: '1561-09-01', precision: bounded}
    label: "Reimerswaal — learning under slow erosion"
    cause: "Post-fire economics replace the intended Zierikzee path with Reimerswaal and separate father and son."
    effect: "Claes gains language/rule competence while repeated water/fire pressure turns attention into vigilance."
    instances: [NI.EVENT.REIMERSWAAL_MOVE.1554.001]
    authoring_inputs: [WORLD.REIMERSWAAL]

  - id: H04
    story_time: {earliest: '1561-08-01', latest_exclusive: '1561-09-01', precision: month}
    label: "Landjuweel — meaning becomes multiple"
    cause: "Public rhetoric materializes signs before competing audiences."
    effect: "Claes moves from noticing patterns toward judging interpretation, role and consequence."
    instances: [NI.EVENT.LANDJUWEEL.1561.001]
    authoring_inputs: [WORLD.ANTWERP]

  - id: H05
    story_time: {earliest: '1563-02-01', latest_exclusive: '1564-10-04', precision: bounded}
    label: "Dee/Silvius/Boom — process becomes power"
    cause: "Claes learns through print, materials, graphite, pyritic matter, vitriol and the death/opening problem of Sol."
    effect: "He becomes a causal actor and begins to overvalue complete understanding as a route to control."
    instances: [NI.SCENE.DEE_FIRST_ENCOUNTER.1563.001, NI.SCENE.MEMORIAAL_GIFT.1564.001, NI.EVENT.SECURITY_BREAK.1564.001]
    arcs_advanced: [ARC.CLAES.DEE, ARC.CLAES.MACRO_TRANSMUTATION]

  - id: H06
    story_time: {earliest: '1566-08-01', latest_exclusive: '1570-01-01', precision: bounded}
    label: "Return to Goes — old place, altered meanings"
    cause: "Claes returns after years of formation into a city whose religious, family and material order is no longer the childhood world."
    effect: "The place that should confirm identity instead exposes discontinuity; Mayken enters as a materially grounded equal rather than as a recovered piece of childhood."
    instances: [NI.EVENT.CLAES_RETURN_GOES.1566.001]
    relationship_projection: REL.CLAES.MAYKEN.CONJUNCTIO

  - id: H07
    story_time: {earliest: '1567-09-01', latest_exclusive: '1569-11-20', precision: bounded}
    label: "Cornelis — warning, secrecy and irreversible inheritance"
    cause: "Network exposure and repression convert Cornelis' protective secrecy into arrest, recidive pressure and public execution."
    effect: "Claes loses the possibility of repairing father-son time and inherits responsibility without receiving a cryptographic answer."
    instances: [NI.EVENT.CORNELIS_FALL.1568.001]
    arcs_advanced: [ARC.CLAES.CORNELIS, ARC.CLAES.LIFE]

  - id: H08
    story_time: {earliest: '1570-01-01', latest_exclusive: '1571-01-01', precision: year}
    label: "Memoriaal reveal — truth becomes obligation"
    cause: "A material cue plus controlled green-vitriol development reveals readable testimony already present."
    effect: "The problem changes from 'what is hidden?' to 'what must we do with what can now be read?'; Mayken's independent material judgement prevents solitary certainty."
    instances: [NI.SEQUENCE.RECOVERY.1570.001]
    arcs_advanced: [ARC.CLAES.LIFE, ARC.CLAES.MACRO_TRANSMUTATION, ARC.MAYKEN.LIFE]

  - id: H09
    story_time: {earliest: '1572-01-01', latest_exclusive: '1580-01-01', precision: design-window}
    label: "Goes second severance — material/economic causality still to be chosen"
    status: OPEN_AUTHORIAL_HINGE
    cause: "1572 siege destruction and 1577–1579 postwar property/legal afterlife create historically grounded pressure."
    effect_if_resolved: "Goes ceases to be a recoverable economic/home base through a concrete chain of loss, debt, claims or network collapse."
    open_projection: ARC.CLAES.GOES_DEPARTURE_1572_1579
    decision_id: OPEN.GOES.CLAES_DEPARTURE_1572_1579.001
    guardrail: "Do not fill this gap by destroying the documented Nissepad brewery or by labeling ordinary transfers confiscations."

  - id: H10
    story_time: {earliest: '1578-01-01', latest_exclusive: '1579-01-01', precision: year}
    label: "Projectio of the Word"
    cause: "Claes chooses to move testimony out of private possession into print."
    effect: "The textual mission is completed by release; public interpretation can no longer be controlled by Claes."
    instances: [NI.EVENT.PUBLICATION.1578.001]
    arcs_advanced: [ARC.CLAES.MACRO_TRANSMUTATION]

  - id: H11
    story_time: {earliest: '1584-01-01', latest_exclusive: '1585-01-01', precision: year}
    label: "Delft — moral Nigredo / Albedo threshold"
    cause: "Political violence and mortal consequence expose the limits of rightness, foreknowledge and control."
    effect: "Claes must learn to distinguish truth from certainty and right action from guaranteed outcome."
    instances: [NI.CHAPTER.1584.01]
    arcs_advanced: [ARC.CLAES.LIFE, ARC.CLAES.MACRO_TRANSMUTATION]

  - id: H12
    story_time: {earliest: '1584-01-01', latest_exclusive: '1602-03-14', precision: developmental}
    label: "Mayken and the late road — conjunctio as recovery in relation"
    cause: "Claes' analytical competence survives while embodied openness is constricted; Mayken's independent material mode continually contradicts disembodied certainty."
    effect: "Sinne returns as resonance: perception, body, memory, relation and moral choice can coexist."
    arcs_advanced: [ARC.CLAES.SINNE_RECOVERY, ARC.MAYKEN.LIFE]
    relationship_projection: REL.CLAES.MAYKEN.CONJUNCTIO

  - id: H13
    story_time: {date: '1602-03-13', precision: day}
    label: "Enkhuizen — Projectio of Matter"
    cause: "The late Sol/Rode-Leeuw line reaches a materially witnessed test under the Morhof-framed Seton event."
    effect: "The deeper test is whether Claes can understand material success without converting it into ownership, proof of self or total control."
    arcs_advanced: [ARC.CLAES.MACRO_TRANSMUTATION, ARC.CLAES.GREAT_WORK.AUTHORIAL]

  - id: H14
    story_time: {earliest: '1602-03-13', precision: open-ended}
    label: "Status Prima Nova — Projectio of Self"
    cause: "Word and Matter have both passed beyond private possession."
    effect: "Claes can perceive, distinguish, choose, carry and release without demanding that the world become safe, certain or owned."
    arcs_advanced: [ARC.CLAES.GREAT_WORK.AUTHORIAL]

  chapter_projection_rule:
  - "Every future chapter should identify which hinge it serves or justify why a new hinge is necessary."
  - "A chapter may activate multiple Corpus/Anima/Spiritus registers but must still have ordinary human causality."
  - "World detail from Round B is selected because it creates pressure, choice, contrast or consequence — not because research exists."
  - "Mayken's presence invokes ARC.MAYKEN.LIFE as well as the Claes relationship; she never exists only inside Claes' arc."
  - "Open hinge H09 must remain visibly open until the author chooses the 1572–1579 causal model."
```

---

# SOURCE FILE: `narrative/alchemical_authorial_architecture.yaml`

```yaml
schema_version: 1.0.0
kind: AuthorialArchitectureRegistry
architectures:
- id: ARC.CLAES.GREAT_WORK.AUTHORIAL
  type: AuthorialArchitecture
  label: "The Great Work — Status Prima, Corpus, Anima, Spiritus, Projectio, Status Prima Nova"
  canon_status: CANON
  protagonist: ENT.PERSON.CLAES
  decision_id: DEC.CLAES.GREAT_WORK.AUTHORIAL_ARCHITECTURE.2026-08-16
  nested_with:
  - ARC.CLAES.MACRO_TRANSMUTATION
  - ARC.CLAES.LIFE
  - ARC.CLAES.SINNE_RECOVERY
  governing_sentence: "The author knows the Work; Claes undergoes it; the reader experiences it."
  movement_law: "Solve et Coagula — separate what has been falsely fused, then reconnect what can enter a truer relation."

  status_prima:
    story_time: {earliest: '1542-12-08', latest_exclusive: '1554-05-18', precision: bounded}
    function: "Claes begins embedded in body, household, church, craft, food, trade and ordinary sensory trust before he can theorize their order."
    value_state: "belonging and sensory openness without mature self-knowledge"
    warning: "Status Prima is not innocence-as-perfection; it is the undivided starting condition from which later distinctions become possible."

  registers:
  - name: Corpus
    function: "The visible/material Work: bodies, food, beer, paper, ink, books, plants, buildings, fire, water, salts, vitriol, metals, tools, roads and cities change under real processes."
    authoring_question: "What materially changes here, by which action, and what remains materially continuous through that change?"
    recurring_domains:
    - WORLD.BREAD_GRAIN
    - WORLD.BEER_BREWING_DISTRIBUTION
    - WORLD.GOES
    - WORLD.REIMERSWAAL
    - WORLD.PRINT_BOOK_NETWORK
    - WORLD.SCHUTTERIJ_MILITARY
    material_law: "Never substitute symbolism for process. Matter must behave causally enough that the reader could notice the difference between appearance and transformation."
  - name: Anima
    function: "The relational/meaning Work: belief, interpretation, loyalty, testimony, language, love, public opinion, memory and moral obligation are separated, tested and recombined."
    authoring_question: "Which meaning, loyalty or relation is being tested, and who interprets the same sign differently?"
    recurring_domains:
    - WORLD.RELIGIOUS_SPACE.SENSORY_CHURCH
    - WORLD.ANTWERP
    - WORLD.MUSIC_PRAYER_TRANSFORMATION
    - WORLD.PRINT_BOOK_NETWORK
    relational_law: "A sign may remain materially identical while its social or moral meaning changes with audience, confession, memory and use."
  - name: Spiritus
    function: "The inner Work: Claes' vigilance, certainty-seeking, grief, agency, embodied sinne, responsibility and sovereignty are transformed."
    authoring_question: "What does this event make Claes able or unable to perceive, distinguish, choose, carry or release?"
    recurring_arcs:
    - ARC.CLAES.LIFE
    - ARC.CLAES.SINNE_RECOVERY
    - ARC.CLAES.CORNELIS
    inner_law: "Knowledge must cease to promise control and become responsible action under uncertainty."

  register_rule: "Corpus, Anima and Spiritus are simultaneous spiral registers. A scene may strongly activate one, two or all three; the novel must not mechanically march through three identical cycles."

  non_binding_operation_vocabulary:
    status: AUTHOR_SIDE_DIAGNOSTIC_NOT_FIXED_HISTORICAL_SEQUENCE
    operations:
    - ontvangen
    - verbranden
    - oplossen
    - onderscheiden
    - verheffen
    - gebruikt_worden
    - scheiden
    - verrotten
    - verenigen
    - verliezen
    - herhalen
    - zwart_worden
    - wit_worden
    - rijpen
    - rood_worden
    - projecteren
    - loslaten
    rule: "Use an operation only if the actual event earns it. No scene, act or life phase is required to match one operation or a fixed count."

  projection_grid:
  - hinge: "1547–1554 Goes childhood"
    corpus: "bread, beer, household timing, church bodies/materials, routes and craft teach change through touch, smell, heat, sound and weight"
    anima: "order first appears as shared custom, prayer, story, language and family practice"
    spiritus: "sinne is open; Claes learns that attention seems to make the world legible"
  - hinge: "18 May 1554 Goes fire"
    corpus: "house and bodies are destroyed; survival and loss are materially irreversible"
    anima: "home, family continuity and divine/social order no longer align with what Claes expected"
    spiritus: "the wound forms: if he had seen earlier, could he have prevented loss?"
  - hinge: "1554–1561 Reimerswaal"
    corpus: "water, repairs, salt, school materials and repeated damage show slow erosion rather than one clean catastrophe"
    anima: "Claes learns rules and Latin while belonging itself feels conditional"
    spiritus: "attention becomes vigilance; competence grows while sensory openness narrows"
  - hinge: "1561 Landjuweel"
    corpus: "bodies, costumes, blazons, wagons, streets and performance materialize rhetoric"
    anima: "one sign acquires competing meanings across chamber, audience, judge, authority and print"
    spiritus: "Claes moves from observation toward interpretation"
  - hinge: "1563–1564 Dee/Silvius/Boom"
    corpus: "paper, graphite, pyritic matter, vitriol and Sol teach that hidden or conserved matter can reappear through right relation"
    anima: "authority, text, secrecy and trust are separated from simple obedience"
    spiritus: "Claes becomes a causal actor and begins to equate understanding with control"
  - hinge: "19 November 1569 Cornelis execution"
    corpus: "the father's vulnerable body and separately destroyed papers/books make public power physical"
    anima: "silence, loyalty, testimony and inherited responsibility split apart"
    spiritus: "the possibility of later reconciliation ends; responsibility survives the father"
  - hinge: "1570 memoriaal reveal"
    corpus: "green vitriol develops readable words already present in the paper"
    anima: "private testimony becomes a moral demand rather than a puzzle prize"
    spiritus: "recognition must become decision; Mayken's material contradiction limits Claes' overconfidence"
  - hinge: "1578 Antwerp print"
    corpus: "text receives another body through print and multiplication"
    anima: "testimony leaves private ownership and enters public interpretation"
    spiritus: "Claes performs projectio of the Word by releasing rather than possessing the text"
  - hinge: "1584 Delft moral bottom"
    corpus: "political violence and mortal consequence refuse abstraction"
    anima: "certainty and rightness separate"
    spiritus: "macro-Nigredo reaches moral bottom; Albedo requires distinction without withdrawal"
  - hinge: "1584–1602 Mayken and late road"
    corpus: "weather, plants, food, fatigue, preparation and travel return Claes to embodied material life"
    anima: "love becomes relation without possession; differing expertise is not an obstacle to union"
    spiritus: "sinne recovers as resonance and embodied discernment"
  - hinge: "13 March 1602 Enkhuizen"
    corpus: "the Sol/Rode-Leeuw line is tested materially under the Morhof-framed event"
    anima: "witness, credibility and transmission matter more than possession of a marvel"
    spiritus: "mastery is tested by whether Claes can release ownership and control"

  transmutatio_rubedo:
    story_time: {earliest: '1599-01-01', latest_exclusive: '1603-01-01', precision: approximate}
    function: "Corpus, Anima and Spiritus no longer operate as isolated problems: material judgement, relationship and self-knowledge can resonate without collapsing into sameness."
    relationship_expression: REL.CLAES.MAYKEN.CONJUNCTIO

  projectio:
    triad:
    - "1578 — Word: testimony is printed and released beyond private possession."
    - "1602 — Matter: the late Sol/Rode-Leeuw line is tested in Enkhuizen."
    - "post-1602 — Self: Claes releases the need to possess the Work, its outcome or his own legacy."

  status_prima_nova:
    story_time: {earliest: '1602-03-13', precision: open-ended}
    function: "The new status is not a return to the first household or to innocence. Claes can remain embodied, relational and responsible without demanding certainty or possession."
    mature_sequence: "perceive -> distinguish -> choose -> carry -> release"

  hard_guardrails:
  - "This is authorial structure, not an in-world universal alchemical catechism."
  - "Do not force every scene into an operation name."
  - "Do not let later Basilian/Valentinian or seventeenth-century formulations leak backward unless separately time-verified."
  - "The Great Work does not excuse historical anachronism or implausible chemistry."
  - "Mayken is counterpart and conjunctio-partner, not the missing ingredient that magically completes Claes."
```

---

# SOURCE FILE: `narrative/instances.yaml`

```yaml
schema_version: 1.4.0
kind: NarrativeInstanceRegistry
instances:
- id: NI.PROLOGUE.1542.001
  type: ChapterInstance
  label: De Bladzijde
  canon_status: CANON
  story_time:
    earliest: '1542-12-01'
    latest_exclusive: '1543-01-01'
    precision: month
  story_file: prologue_de_bladzijde
  notes: "Valencia; thematic/technical bridge to later testimony and intentional exact-date resonance with Claes' canonical birth on 8 December 1542."
- id: NI.SCENE.DREMPEL.1547.001
  type: SceneInstance
  label: De Drempel
  canon_status: PROPOSED
  story_time:
    earliest: '1547-01-01'
    latest_exclusive: '1548-01-01'
    precision: approximate
  locations:
  - ENT.LOC.GOES
  entities:
  - ENT.PERSON.CLAES
  motifs:
  - MOTIF.SINNE
  - MOTIF.INCENSE_WAX
- id: NI.SCENE.FIRST_MERELS.1553.001
  type: SceneInstance
  label: Eerste molenspel
  canon_status: CANON
  story_time:
    earliest: '1553-12-01'
    latest_exclusive: '1554-03-01'
    precision: winter
  locations:
  - ENT.LOC.GOES
  entities:
  - ENT.PERSON.CLAES
  - ENT.PERSON.CORNELIS
  motifs:
  - MOTIF.MERELS_WAYS
  - MOTIF.TIK_TIK_TIK
- id: NI.SCENE.SOWER.1554.001
  type: SceneInstance
  label: De Zaaierscène
  canon_status: CANON
  story_time:
    earliest: '1554-02-01'
    latest_exclusive: '1554-04-01'
    precision: Lent
  locations:
  - ENT.LOC.GOES
  entities:
  - ENT.PERSON.CLAES
  - ENT.PERSON.CORNELIS
  arcs_advanced:
  - ARC.CLAES.LIFE
  motifs:
  - MOTIF.INCENSE_WAX
  - MOTIF.CARRIER_MEANING
- id: NI.EVENT.GOES_FIRE.1554.001
  type: EventInstance
  label: Stadsbrand Goes — verlies van huis en gezin
  canon_status: CANON
  details_status: MIXED_HISTORICAL_AND_NOVEL_CANON
  story_time:
    date: '1554-05-18'
    precision: day
  locations:
  - ENT.LOC.GOES
  - ENT.LOC.GOES.OOSTZELKE
  - ENT.LOC.GOES.NIEUWSTRAAT_PRE1594
  entities:
  - ENT.PERSON.CLAES
  - ENT.PERSON.CORNELIS
  - ENT.PERSON.CLAES_MOTHER
  - ENT.PERSON.CLAES_BROTHER
  - ENT.PERSON.CLAES_UNBORN_SIBLING
  - ENT.PERSON.CLAES_JACOBSZ_NISSEPAT
  objects:
  - ENT.PROP.GOES.NISSEPAT.NIEUWSTRAAT_1542
  story_claims:
  - STC.CLAES.HOUSEHOLD_PRE_FIRE.1554.001
  - STC.CLAES.FAMILY_FIRE.1554.001
  - STC.CLAES.GRANDFATHER.NISSEPAT.001
  claims_active:
  - SC.HIST.GOES.SALT.NORTH_HARBOUR_1554.001
  - SC.HIST.GOES.FIRE_1554.FOOTPRINT.001
  - SC.HIST.GOES.FIRE_1554.SPREAD.001
  - SC.MODEL.GOES.FIRE_1554.FIREBRANDS.001
  - SC.HIST.GOES.FIRE_1554.CASUALTIES.001
  arcs_advanced:
  - ARC.CLAES.LIFE
  - ARC.CLAES.CORNELIS
  motifs:
  - MOTIF.FIRE_WATER
  - MOTIF.SINNE
  refinement: WORLD.GOES.FIRE_1554.REFINEMENT
  narrative_state_change:
    before: "intact household: parents, Claes, younger brother, expected child, shared home"
    after: "Cornelis and Claes survive; mother, brother and unborn child are dead; home is lost; grandfather loses the property asset"
  historical_guardrail: "Historical evidence supports a northern-harbour origin, broad north/west damage and mixed damage in the old Nieuwstraat/Armenhoek environment, but not the loss of this specific house or these named family casualties; the current fire-specific casualty count remains UNKNOWN."
- id: NI.SEQUENCE.POSTFIRE_FAMILY.1554.001
  type: SequenceInstance
  label: Nasleep — vader en zoon verliezen ook elkaar
  canon_status: CANON
  story_time:
    earliest: '1554-05-18'
    latest_exclusive: '1554-12-08'
    precision: bounded
  locations:
  - ENT.LOC.GOES
  - ENT.LOC.REIMERSWAAL
  entities:
  - ENT.PERSON.CLAES
  - ENT.PERSON.CORNELIS
  - ENT.PERSON.CLAES_JACOBSZ_NISSEPAT
  story_claims:
  - STC.CLAES.CORNELIS.POSTFIRE_SEPARATION.001
  function: "Cornelis remains amid the Goese recovery to rebuild livelihood/business/shelter and fund Claes' schooling; grandfather helps despite his own property loss; Claes is sent away to Reimerswaal, turning care into physical separation."
  value_shift: "surviving together -> grieving apart"
- id: NI.EVENT.REIMERSWAAL_MOVE.1554.001
  type: EventInstance
  label: Vertrek als kostjongen naar Reimerswaal
  canon_status: CANON
  story_time:
    earliest: '1554-05-19'
    latest_exclusive: '1554-12-08'
    precision: bounded
  locations:
  - ENT.LOC.REIMERSWAAL
  entities:
  - ENT.PERSON.CLAES
  - ENT.PERSON.CORNELIS
  - ENT.PERSON.CLAES_JACOBSZ_NISSEPAT
  story_claims:
  - STC.CLAES.REIMERSWAAL.001
  - STC.CLAES.ZIERIKZEE.PLAN.001
  - STC.CLAES.CORNELIS.POSTFIRE_SEPARATION.001
  cause: "Post-fire household/economic collapse makes the original Zierikzee plan unaffordable; Reimerswaal preserves Claes' educational route at lower cost while Cornelis remains in Goes."
- id: NI.EVENT.LANDJUWEEL.1561.001
  type: EventInstance
  label: Landjuweel Antwerpen
  canon_status: CANON
  story_time:
    earliest: '1561-08-01'
    latest_exclusive: '1561-09-01'
    precision: month
  locations:
  - ENT.LOC.ANTWERP
  entities:
  - ENT.PERSON.CLAES
  - ENT.PERSON.CORNELIS
  story_claims:
  - STC.CLAES.LANDJUWEEL.1561.001
- id: NI.SCENE.DEE_FIRST_ENCOUNTER.1563.001
  type: SceneInstance
  label: Eerste ontmoeting Claes–Dee
  canon_status: CANON
  story_time:
    earliest: '1563-02-01'
    latest_exclusive: '1563-03-01'
    precision: month
  locations:
  - ENT.LOC.SILVIUS_GULDEN_ENGEL
  entities:
  - ENT.PERSON.CLAES
  - ENT.PERSON.JOHN_DEE
  - ENT.PERSON.WILLEM_SILVIUS
  story_claims:
  - STC.CLAES.DEE_ENCOUNTER.1563.001
  arcs_advanced:
  - ARC.CLAES.DEE
- id: NI.CHAPTER.1564.01
  type: ChapterInstance
  label: De Ladingen Van Antwerpen
  canon_status: CANON
  story_time:
    earliest: '1564-01-01'
    latest_exclusive: '1564-10-04'
    precision: bounded
  locations:
  - ENT.LOC.ANTWERP
  entities:
  - ENT.PERSON.CLAES
  story_file: 1564_1_de_ladingen_van_antwerpen.md
- id: NI.CHAPTER.1564.02
  type: ChapterInstance
  label: De Verkeerde Kist
  canon_status: CANON
  story_time:
    earliest: '1564-01-01'
    latest_exclusive: '1564-10-04'
    precision: bounded
  locations:
  - ENT.LOC.ANTWERP
  entities:
  - ENT.PERSON.CLAES
  story_file: 1564_2_de_verkeerde_kist.md
- id: NI.SCENE.MEMORIAAL_GIFT.1564.001
  type: SceneInstance
  label: Dee geeft memoriaal en grafietstift
  canon_status: CANON
  story_time:
    earliest: '1564-01-01'
    latest_exclusive: '1564-04-01'
    precision: interval
  sequence_constraint: occurs before NI.CHAPTER.1564.03
  locations:
  - ENT.LOC.ANTWERP
  entities:
  - ENT.PERSON.CLAES
  - ENT.PERSON.JOHN_DEE
  objects:
  - OBJ.MEMORIAAL
  - OBJ.GRAPHITE_STIFT
  story_claims:
  - STC.MEMORIAAL.GIFT.001
  - STC.MEMORIAAL.BREVISIMA_CARRIER.001
  - STC.MEMORIAAL.GRAPHITE_RULE.001
  arcs_advanced:
  - ARC.CLAES.DEE
  function: "Dee gives Claes the apparently blank memoriaal and a graphite stift before Boom, forbidding ink while Claes remains his pupil; Claes reads this as discipline, not as protection of an already hidden tannin-printed readable Brevísima."
- id: NI.CHAPTER.1564.03
  type: ChapterInstance
  label: De Kies Van Boom
  canon_status: CANON
  story_time:
    earliest: '1564-01-01'
    latest_exclusive: '1564-10-04'
    precision: bounded
  locations:
  - ENT.LOC.BOOM
  entities:
  - ENT.PERSON.CLAES
  story_file: 1564_3_de_kies_van_boom.md
- id: NI.CHAPTER.1564.04
  type: ChapterInstance
  label: De Loog Van Antwerpen
  canon_status: CANON
  story_time:
    earliest: '1564-01-01'
    latest_exclusive: '1564-10-04'
    precision: bounded
  locations:
  - ENT.LOC.ANTWERP
  entities:
  - ENT.PERSON.CLAES
  story_file: 1564_4_de_loog_van_antwerpen.md
- id: NI.CHAPTER.1564.05
  type: ChapterInstance
  label: De Dood Van Sol
  canon_status: CANON
  story_time:
    earliest: '1564-01-01'
    latest_exclusive: '1564-10-04'
    precision: bounded
  locations:
  - ENT.LOC.ANTWERP
  entities:
  - ENT.PERSON.CLAES
  story_file: 1564_5_de_dood_van_sol.md
- id: NI.EVENT.SECURITY_BREAK.1564.001
  type: EventInstance
  label: Veiligheidsbreuk na stenenoproer
  canon_status: CANON
  story_time:
    date: '1564-10-04'
    precision: day
  locations:
  - ENT.LOC.ANTWERP
  entities:
  - ENT.PERSON.CLAES
  - ENT.PERSON.CORNELIS
  story_claims:
  - STC.MACRO.NIGREDO_START.1564.001
  arcs_advanced:
  - ARC.CLAES.MACRO_TRANSMUTATION
  continuity_note: "The security break remains a political/network and macro-Nigredo hinge. It does not insert, recipher, key or otherwise alter OBJ.MEMORIAAL, whose readable hidden Brevísima has already been in Claes' possession since before Boom."
- id: NI.CHAPTER.1564.06
  type: ChapterInstance
  label: De honderd gulden
  canon_status: PROPOSED
  story_time:
    earliest: '1564-10-04'
    latest_exclusive: '1564-12-31'
    precision: bounded
  locations:
  - ENT.LOC.ANTWERP
  entities:
  - ENT.PERSON.CLAES
  - ENT.PERSON.CORNELIS
  story_file: 1564_6_de_honderd_gulden.md
- id: NI.EVENT.CLAES_RETURN_GOES.1566.001
  type: EventInstance
  label: Terugkeer Claes naar Goes
  canon_status: CANON
  story_time:
    earliest: '1566-08-01'
    latest_exclusive: '1567-01-01'
    precision: bounded
  locations:
  - ENT.LOC.GOES
  entities:
  - ENT.PERSON.CLAES
  story_claims:
  - STC.CLAES.RETURN_GOES.1566.001
- id: NI.EVENT.CORNELIS_FALL.1568.001
  type: EventInstance
  label: Val en dood Cornelis — 1567–1569
  canon_status: CANON
  details_status: CANON
  story_time:
    earliest: '1567-09-01'
    latest_exclusive: '1569-11-20'
    precision: bounded
  locations:
  - ENT.LOC.ANTWERP
  entities:
  - ENT.PERSON.CORNELIS
  - ENT.PERSON.CLAES
  story_claims:
  - STC.CORNELIS.FIRST_ARREST_BAIL.1567.001
  - STC.CORNELIS.DEATH.ANTWERP.1569.001
  - STC.CORNELIS.EXECUTION_WITNESS.001
  sequence:
  - "autumn 1567: first arrest/examination in Antwerp; release on borg or equivalent conditions"
  - "late 1568 through 1569: renewed exposure through clandestine book/paper traffic and refusal to name others"
  - "19 November 1569: fictional public execution in Antwerp; Claes witnesses"
  decision: DEC.CORNELIS.DEATH.1569.2026-08-15.REVISED
- id: NI.SEQUENCE.RECOVERY.1570.001
  type: SequenceInstance
  label: Onthulling en lezing van het memoriaal 1570
  canon_status: CANON
  story_time:
    earliest: '1570-01-01'
    latest_exclusive: '1571-01-01'
    precision: year
  locations:
  - ENT.LOC.GOES
  entities:
  - ENT.PERSON.CLAES
  - ENT.PERSON.BELOVED
  objects:
  - OBJ.MEMORIAAL
  - OBJ.LASCASAS_PLAINTEXT
  - OBJ.ZOVITIUS_1570_TRIGGER
  story_claims:
  - STC.ZOVITIUS.TRIGGER.1570.001
  - STC.MEMORIAAL.BREVISIMA_CARRIER.001
  arcs_advanced:
  - ARC.CLAES.LIFE
  - ARC.CLAES.MACRO_TRANSMUTATION
  motifs:
  - MOTIF.BLACKENING_REVEAL
  function: "A material cue and controlled green-vitriol development transform the apparently blank pages into readable Diets/Brabant Brevísima text. The dramatic work is recognition, reading and moral response, not cryptographic reconstruction."
- id: NI.EVENT.PUBLICATION.1578.001
  type: EventInstance
  label: Antwerpse druk / Projectio van het Woord
  canon_status: CANON
  story_time:
    earliest: '1578-01-01'
    latest_exclusive: '1579-01-01'
    precision: year
  locations:
  - ENT.LOC.ANTWERP
  entities:
  - ENT.PERSON.CLAES
  story_claims:
  - STC.LASCASAS.PUBLICATION.1578.001
  function: "The readable testimony leaves private possession through an Antwerp print event; exact printer, production route and distribution chain remain separately open/evidence-controlled."
- id: NI.CHAPTER.1584.01
  type: ChapterInstance
  label: De markt van Delft
  canon_status: CANON
  story_time:
    earliest: '1584-01-01'
    latest_exclusive: '1585-01-01'
    precision: year
  locations:
  - ENT.LOC.DELFT
  entities:
  - ENT.PERSON.CLAES
  story_file: 1584_1_de_markt_van_delft.md
  story_claims:
  - STC.CLAES.DELFT.1584.001
  arcs_advanced:
  - ARC.CLAES.LIFE
  - ARC.CLAES.MACRO_TRANSMUTATION
- id: NI.SEQUENCE.LATE_RUBEDO.1599.001
  type: SequenceInstance
  label: Late Rubedo / mogelijke Middelburg-spiegel
  canon_status: OPEN
  story_time:
    earliest: '1599-01-01'
    latest_exclusive: '1603-01-01'
    precision: approximate
  locations:
  - ENT.LOC.MIDDELBURG
  entities:
  - ENT.PERSON.CLAES
  - ENT.PERSON.RADERMACHER
  arcs_advanced:
  - ARC.CLAES.MACRO_TRANSMUTATION
- id: NI.SCENE.FINAL_MERELS.1602.001
  type: SceneInstance
  label: Laatste molenspel
  canon_status: OPEN
  fixed_function: CANON
  story_time:
    earliest: '1602-01-01'
    precision: open-ended
  entities:
  - ENT.PERSON.CLAES
  story_claims:
  - STC.CLAES.PROJECTIO.001
  arcs_advanced:
  - ARC.CLAES.LIFE
  - ARC.CLAES.MACRO_TRANSMUTATION
  motifs:
  - MOTIF.MERELS_WAYS
```

---

# SOURCE FILE: `narrative/arcs.yaml`

```yaml
schema_version: 1.4.0
kind: NarrativeArcRegistry
arcs:
- id: ARC.CLAES.LIFE
  type: CharacterArc
  label: Claes cradle-to-grave
  status: CANON
  protagonist: ENT.PERSON.CLAES
  authorial_architecture: ARC.CLAES.GREAT_WORK.AUTHORIAL
  causal_projection: ARC.CLAES.CAUSAL_SPINE
  phases:
  - id: ARC.CLAES.LIFE.P01
    label: Wieg en lichaam
    story_time: {earliest: '1542-12-08', latest_exclusive: '1547-12-31', precision: approximate}
    dominant_movement: ontvankelijkheid zonder duiding
    value_shift: body before understanding
  - id: ARC.CLAES.LIFE.P02
    label: Kind dat orde ontdekt
    story_time: {earliest: '1547-01-01', latest_exclusive: '1554-05-18', precision: approximate}
    dominant_movement: Wijsheid en Hoop
    value_shift: order can be learned through attention within an intact household of Cornelis, Tanneken, Claes, younger brother Jan and the expected unborn child
  - id: ARC.CLAES.LIFE.P03
    label: Verdreven kind
    story_time: {earliest: '1554-05-18', latest_exclusive: '1561-09-01', precision: bounded}
    dominant_movement: Hoop under pressure
    value_shift: observation cannot prevent loss; home, mother, brother and unborn sibling are lost, then the surviving father is also lost to daily life through the Goes/Reimerswaal separation
    wound: If I had seen early enough, could I have prevented what happened?
    relational_pressure: Cornelis' attempt to preserve Claes' future is experienced through physical absence.
  - id: ARC.CLAES.LIFE.P04
    label: Adolescent die leert interpreteren
    story_time: {earliest: '1560-01-01', latest_exclusive: '1563-12-31', precision: overlap}
    dominant_movement: from observation to judgement
    value_shift: roles, signs and meanings diverge
  - id: ARC.CLAES.LIFE.P05
    label: Jonge zoeker
    story_time: {earliest: '1564-01-01', latest_exclusive: '1565-01-01', precision: year}
    dominant_movement: Kracht/Geloof begins
    value_shift: from observer to causal actor; matter can hide and reveal what is already present
  - id: ARC.CLAES.LIFE.P06
    label: Handelende volwassene
    story_time: {earliest: '1565-01-01', latest_exclusive: '1578-01-01', precision: approximate}
    dominant_movement: Kracht/Geloof under pressure
    value_shift: act without complete certainty; father lost in 1569, hidden testimony revealed and released toward print
    hinges:
    - autumn 1567 Cornelis first arrest/examination and release
    - 19 November 1569 Cornelis executed in Antwerp with Claes present
    - 1570 direct chemical reveal/read of the hidden Brevísima
    - 1572–1579 Goes material/economic severance remains an explicit authorial-design hinge
    - 1578 Antwerp print event as projectio of the Word
    open_hinge: OPEN.GOES.CLAES_DEPARTURE_1572_1579.001
  - id: ARC.CLAES.LIFE.P07
    label: Man in Nigredo
    story_time: {earliest: '1578-01-01', latest_exclusive: '1585-01-01', precision: bounded}
    dominant_movement: certainty dissolves
    value_shift: seeing and knowing do not guarantee right action
  - id: ARC.CLAES.LIFE.P08
    label: Rijpe man en bewaarder
    story_time: {earliest: '1584-01-01', latest_exclusive: '1603-01-01', precision: approximate}
    dominant_movement: Albedo to Rubedo
    value_shift: distinguish then reconnect; recovered sinne becomes relation rather than control
    relational_catalyst: Mayken accompanies the later sensory/spiritual recovery without performing it for Claes.
    counterpart_arc: ARC.MAYKEN.LIFE
    relationship_projection: REL.CLAES.MAYKEN.CONJUNCTIO
  - id: ARC.CLAES.LIFE.P09
    label: Laatste beweging en graf
    story_time: {earliest: '1602-03-13', precision: open-ended}
    dominant_movement: Projectio
    value_shift: material mastery -> release beyond possession -> transfer without control
  knowledge_object_targets: [KO.STORY, KO.STRUCTURE, KO.VALUE, KO.CONFLICT, KO.EVENT]

- id: ARC.CLAES.MACRO_TRANSMUTATION
  type: MacroArc
  label: Drager -> Nigredo -> Albedo -> Rubedo -> Projectio
  status: CANON
  authorial_architecture: ARC.CLAES.GREAT_WORK.AUTHORIAL
  architecture_relation: "This operational macro arc remains the chronological transformation spine. The Status Prima / Corpus-Anima-Spiritus / Status Prima Nova architecture is a deeper author-side register model, not a replacement timeline."
  phases:
  - label: Drager
    story_time: {earliest: '1542-12-08', latest_exclusive: '1564-10-04', precision: bounded}
  - label: Gebondenheid / macro-Nigredo
    story_time: {earliest: '1564-10-04', latest_exclusive: '1585-01-01', precision: bounded}
  - label: Albedo / Onderscheiding
    story_time: {earliest: '1584-01-01', latest_exclusive: '1599-01-01', precision: approximate}
  - label: Rubedo / Verbinding
    story_time: {earliest: '1599-01-01', latest_exclusive: '1603-01-01', precision: approximate}
  - label: Projectio / Overdracht
    story_time: {earliest: '1602-03-13', precision: open-ended}
  projectio_triad:
  - '1578: projectio of the Word — testimony is multiplied and released through print.'
  - '1602: projectio of Matter — the Rode Leeuw/Sol line is materially tested in the Morhof-framed Enkhuizen event.'
  - 'after 1602: projectio of the Self — Claes must release ownership, control and the need to possess the Work.'
  guardrails:
  - Authorial architecture, not an in-world universal alchemical doctrine.
  - What becomes visible was already present: literally for hidden typography and the conserved Sol fraction; analogically for testimony, memory and recovered sinne.
  - Corpus, Anima and Spiritus are interwoven registers and must not become three mechanically repeated cycles.
  - No fixed count or sequence of alchemical operations may be forced onto scenes that do not earn it.

- id: ARC.CLAES.DEE
  type: RelationshipArc
  label: Claes <-> Dee
  status: CANON
  participants: [ENT.PERSON.CLAES, ENT.PERSON.JOHN_DEE]
  phases:
  - label: recognition
    story_time: {earliest: '1563-02-01', latest_exclusive: '1563-03-01', precision: month}
  - label: formation
    story_time: {earliest: '1564-01-01', latest_exclusive: '1564-04-01', precision: interval}
  - label: independent judgement
    story_time: {earliest: '1564-01-01', precision: developmental}
  guardrail: Dee's role is intellectual/material formation; the Brevísima is not a cryptographic recovery system.
  knowledge_object_targets: [KO.CONFLICT, KO.VALUE, KO.EVENT]

- id: ARC.CLAES.CORNELIS
  type: RelationshipArc
  label: Claes <-> Cornelis
  status: CANON
  participants: [ENT.PERSON.CLAES, ENT.PERSON.CORNELIS]
  movement: dependence/admiration within an intact family -> shared catastrophic loss -> loving but painful Goes/Reimerswaal separation -> interpretive distance/secrecy -> 1567 warning and repeated exposure -> witnessed execution 19 November 1569 -> inherited responsibility -> adult moral differentiation
  1554_hinge:
    decision_id: DEC.CLAES.POSTFIRE_FATHER_SON.2026-08-14
    father: stays in Goes to rebuild livelihood, business and shelter and keep paying for Claes' schooling
    son: goes to Reimerswaal and can experience the father's sacrifice as another abandonment
    shared_truth: Both survive the same collapse of family but must grieve it apart.
  1569_hinge:
    decision_id: DEC.CORNELIS.DEATH.1569.2026-08-15.REVISED
    date: '1569-11-19'
    value_shift: possibility of reconciliation -> irreversible moral inheritance
    witness: Claes
```

---

# SOURCE FILE: `narrative/relationships.yaml`

```yaml
schema_version: 1.5.1
kind: NarrativeRelationshipRegistry
relationships:
- id: REL.CLAES.CORNELIS
  type: Relationship
  label: Claes and Cornelis
  participants: [ENT.PERSON.CLAES, ENT.PERSON.CORNELIS]
  status: CANON
  phases:
  - label: formation within an intact household
    story_time: {earliest: '1547-01-01', latest_exclusive: '1554-05-18', precision: approximate}
    value_state: dependence -> admiration
    function: Cornelis teaches attention, craft, patience and the difference between pieces and routes while Claes grows up with Tanneken, younger brother Jan and an expected unborn sibling.
  - label: shared catastrophe and physical separation
    story_time: {earliest: '1554-05-18', latest_exclusive: '1561-09-01', precision: bounded}
    value_state: shared family -> surviving father and son who also lose daily access to each other
    function: Both lose Tanneken, Jan, the unborn child and home. Cornelis remains in Goes to rebuild livelihood, business and shelter and finance Claes' education; Claes is sent to Reimerswaal. Cornelis' act of care is therefore also experienced by Claes as distance and possible abandonment.
    support: Claes Jacobsz. Nissepat, fictionally Cornelis' father, helps where possible despite losing the 1542 house; maternal grandmother Mayken Pietersdochter preserves a different continuity through care and family memory.
    decision_id: DEC.CLAES.POSTFIRE_FATHER_SON.2026-08-14
  - label: distance through secrecy and network risk
    story_time: {earliest: '1561-09-01', latest_exclusive: '1567-09-01', precision: interval}
    value_state: admiration -> suspicion/exclusion
    function: The earlier physical separation gives way to interpretive separation as Claes sees that Cornelis hides routes, papers, books and dangerous loyalties. The relationship does not depend on a cipher or fallback key.
  - label: warning, recidive and final loss
    story_time: {earliest: '1567-09-01', latest_exclusive: '1569-11-20', precision: bounded}
    value_state: compromised living father -> condemned protective silence -> absent moral inheritance
    events:
    - autumn 1567 first Antwerp arrest/examination and release on borg or conditions
    - late 1568 through March 1569 renewed exposure through clandestine book/paper traffic
    - 19 November 1569 public execution in Antwerp witnessed by Claes
    transfer: No cryptographic clue is required. Any final exchange is human, relational or testimony-centered.
    resonance: Cornelis' death closes the possibility that father and son will recover the time lost after 1554.
    decision_id: DEC.CORNELIS.DEATH.1569.2026-08-15.REVISED
  - label: differentiation
    story_time: {earliest: '1569-11-20', precision: lower-bound}
    value_state: inheritance -> independent moral judgement
  ko_targets: [KO.CHARACTER, KO.VALUE, KO.CONFLICT, KO.RELATIONSHIP]

- id: REL.CLAES.BROTHER
  type: Relationship
  label: Claes and Jan
  participants: [ENT.PERSON.CLAES, ENT.PERSON.CLAES_BROTHER]
  status: CANON
  story_time: {earliest: '1544-05-01', latest_exclusive: '1554-05-19', precision: approximate}
  value_state: love <-> rivalry <-> companionship -> irreversible loss
  function: Jan is about eighteen months younger, close enough in age to be Claes' daily companion and rival. Their bond contains play, competition, quarrels, loyalty, shared mischief and unfinished ordinary conflict before the fire.
  contrast:
    claes: observes, compares, waits
    jan: acts sooner, tests physically, pulls Claes toward action
  termination: {date: '1554-05-18', event: NI.EVENT.GOES_FIRE.1554.001}
  guardrail: Do not write Jan as a decorative victim or foreshadow his death so heavily that ordinary brotherhood disappears.
  decision_id: DEC.CLAES.EXTENDED_FAMILY.2026-08-14
  ko_targets: [KO.RELATIONSHIP, KO.CONFLICT, KO.VALUE, KO.CHARACTER]

- id: REL.CLAES.TANNEKEN
  type: Relationship
  label: Claes and Tanneken
  participants: [ENT.PERSON.CLAES, ENT.PERSON.CLAES_MOTHER]
  status: CANON
  story_time: {earliest: '1542-12-08', latest_exclusive: '1554-05-19', precision: bounded}
  value_state: embodied safety and practical knowing -> irreversible maternal loss
  function: "Tanneken is a primary source of Claes' pre-theoretical sensory education: heat, texture, smell, fermentation, illness, weather, cloth, food and household timing are known through body and practice before abstraction."
  pregnancy_link: Claes may feel the unborn child move under Tanneken's skin, giving him an early benign experience of reality known without sight.
  guardrail: Do not idealize Tanneken into a mystical mother or learned herbalist; her knowledge is ordinary, practiced, material and relational.
  decision_id: DEC.CLAES.EXTENDED_FAMILY.2026-08-14
  ko_targets: [KO.RELATIONSHIP, KO.VALUE, KO.CHARACTER]

- id: REL.CORNELIS.CLAES_JACOBSZ_NISSEPAT
  type: Relationship
  label: Cornelis and Claes Jacobsz. Nissepat
  participants: [ENT.PERSON.CORNELIS, ENT.PERSON.CLAES_JACOBSZ_NISSEPAT]
  status: CANON_FICTIONAL_KINSHIP
  relation: father_and_son
  historical_guardrail: The historical identity and 1542 purchase of Claes Jacobsz. are documented; his fatherhood of fictional Cornelis is novel canon, not historical genealogy.
  post_fire_function: The older man loses the Nieuwstraat property he bought in 1542 but still helps Cornelis preserve Claes' educational future.
  decision_id: DEC.CLAES.GRANDFATHER_LINK.2026-08-14
  ko_targets: [KO.RELATIONSHIP, KO.VALUE, KO.CONFLICT]

- id: REL.CLAES.PATERNAL_GRANDPARENTS
  type: Relationship
  label: Claes and paternal grandparents
  participants: [ENT.PERSON.CLAES, ENT.PERSON.CLAES_JACOBSZ_NISSEPAT, ENT.PERSON.LIJSBET_PIETERSDOCHTER]
  status: CANON_MIXED_HISTORICAL_FICTIONAL
  function: Claes Jacobsz. represents property, accounting, credit, provenance and continuity; Lijsbet survives mainly as inherited household memory because she dies circa 1540–1541 in novel canon.
  guardrail: Claes Jacobsz. is historical but the kinship is fictional; Lijsbet is wholly fictional.
  decision_id: DEC.CLAES.EXTENDED_FAMILY.2026-08-14
  ko_targets: [KO.RELATIONSHIP, KO.VALUE]

- id: REL.CLAES.MATERNAL_GRANDPARENTS
  type: Relationship
  label: Claes and maternal grandparents
  participants: [ENT.PERSON.CLAES, ENT.PERSON.JAN_JANSEN_KUIPER_MODEL, ENT.PERSON.MAYKEN_PIETERSDOCHTER]
  status: CANON_MIXED_HISTORICAL_MODEL_FICTIONAL
  function: The maternal line brings craft, bodily care and practical material knowledge. The grandfather-model is a cooper linked to barrels and trade; Mayken Pietersdochter preserves family memory and care after Tanneken's death.
  naming_link: Jan Corneliszn. is named for the maternal-grandfather figure in novel canon.
  post_fire_function: Mayken Pietersdochter can provide temporary care, mourning continuity and memories of Tanneken, while Claes Jacobsz. is the stronger economic/educational support figure.
  guardrail: The Jan Jansen kuiper evidence is a historical model cluster, not proven genealogy or a securely identified single man across every act. Mayken Pietersdochter is fictional.
  decision_id: DEC.CLAES.EXTENDED_FAMILY.2026-08-14
  ko_targets: [KO.RELATIONSHIP, KO.VALUE, KO.CHARACTER]

- id: REL.CLAES.DEE.001
  type: Relationship
  label: Claes and John Dee
  participants: [ENT.PERSON.CLAES, ENT.PERSON.JOHN_DEE]
  status: CANON
  arc: ARC.CLAES.DEE
  phases:
  - label: recognition
    story_time: {earliest: '1563-02-01', latest_exclusive: '1563-03-01', precision: month}
    narrative_instances: [NI.SCENE.DEE_FIRST_ENCOUNTER.1563.001]
    value_state: distant intellectual possibility -> personally encountered figure
  - label: formation and disciplined inscription
    story_time: {earliest: '1564-01-01', latest_exclusive: '1564-04-01', precision: interval}
    value_state: recognition -> formative master relationship
    narrative_instances: [NI.SCENE.MEMORIAAL_GIFT.1564.001]
    objects: [OBJ.MEMORIAAL, OBJ.GRAPHITE_STIFT]
    function: Before Claes leaves for Boom, Dee gives him the apparently blank memoriaal and graphite stift and forbids ink while Claes remains his pupil. Claes experiences exacting pedagogical discipline; Dee also knows the rule protects the already tannin-printed hidden readable Brevísima.
    knowledge_asymmetry: Dee knows the book carries readable hidden text and how green vitriol can reveal it; Claes knows only its workbook function and graphite-only rule.
  - label: critical independence
    story_time: {earliest: '1564-01-01', precision: lower-bound}
    value_state: admiration -> recognition of Dee's fallibility
  - label: internalised legacy
    story_time: {earliest: '1564-10-04', precision: lower-bound}
    value_state: direct teacher -> methods, prohibitions and material memories embedded in Claes' later reasoning
  knowledge_object_targets: [KO.VALUE, KO.CONFLICT, KO.EVENT, KO.RELATIONSHIP]

- id: REL.CLAES.SILVIUS
  type: Relationship
  label: Claes and Willem Silvius
  participants: [ENT.PERSON.CLAES, ENT.PERSON.WILLEM_SILVIUS]
  status: CANON
  phases:
  - label: editorial recognition
    story_time: {earliest: '1561-08-01', latest_exclusive: '1564-01-01', precision: bounded}
    value_state: young learner -> useful observer/editorial source
    object: OBJ.ZOVITIUS_SCHOOLBOOK
  - label: practical trust
    story_time: {earliest: '1564-01-01', latest_exclusive: '1564-10-04', precision: bounded}
    value_state: recognition -> operational trust
    hidden_parallel: Silvius can set and print the readable Brevísima invisibly while Claes understands the bound object only as Dee's memoriaal.
  - label: mediated material cue
    story_time: {earliest: '1570-01-01', latest_exclusive: '1571-01-01', precision: year}
    value_state: direct access absent -> remembered/material cue may expose what was already present
    object: OBJ.ZOVITIUS_1570_TRIGGER
  ko_targets: [KO.RELATIONSHIP, KO.EVENT, KO.VALUE]

- id: REL.CLAES.BELOVED
  type: Relationship
  label: Claes and Mayken
  participants: [ENT.PERSON.CLAES, ENT.PERSON.BELOVED]
  status: CANON
  decision_id: DEC.CLAES.BELOVED.MAYKEN_LAMPERT.2026-08-14
  phases:
  - label: separate Goese histories and material proximity
    story_time: {earliest: '1566-08-01', latest_exclusive: '1570-01-01', precision: bounded}
    value_state: separate expertise -> potential complementarity
    function: Both remember the 1554 fire, but Claes' household annihilation and Mayken's family material loss/rebuilding must remain distinct.
  - label: reveal collaboration
    story_time: {earliest: '1570-01-01', latest_exclusive: '1571-01-01', precision: year}
    value_state: solitary interpretation -> collaborative material verification
    narrative_instances: [NI.SEQUENCE.RECOVERY.1570.001]
    function: Collaboration concerns controlled development, reading, material observation and the moral consequences of testimony, not cryptographic reconstruction.
  - label: relational maturation
    story_time: {earliest: '1570-01-01', precision: lower-bound}
    value_state: secrecy as isolation -> trust without surrender of responsibility
  - label: sinne recovery companionship
    story_time: {earliest: '1584-01-01', latest_exclusive: '1602-03-14', precision: developmental}
    value_state: constricted perception -> embodied relation and renewed sensory openness
    function: Mayken draws Claes back into shared material life through trained sensation, travel, weather, plants, preparation, food, fatigue and contradiction; she catalyses but does not perform his recovery.
  role_split:
    claes: [Dee-memory, recognition, interpretive responsibility, decision what to do with testimony, moral ownership without possession]
    mayken: [materia-medica knowledge, weighing, controlled development, paper/ink observation, botanical/material contradiction, error control, sensory companionship]
  guardrails:
  - Mayken is not a cryptographic solver or key-holder.
  - Ordinary Dodoens use may remain part of her apothecary world; the retired special Dodoens carrier does not.
  ko_targets: [KO.RELATIONSHIP, KO.CONFLICT, KO.VALUE, KO.CHARACTER]

- id: REL.CLAES.RADERMACHER
  type: RelationshipPotential
  label: Claes and Johan Radermacher
  participants: [ENT.PERSON.CLAES, ENT.PERSON.RADERMACHER]
  status: OPEN
  possible_story_time: {earliest: '1599-01-01', latest_exclusive: '1603-01-01', precision: approximate}
  function_if_used: "Late Rubedo social mirror: trade, books, religious caution and cross-border help in one network."
  guardrail: No unsupported formal Familist membership.
```

---

# SOURCE FILE: `narrative/motifs.yaml`

```yaml
schema_version: 1.1.1
kind: MotifRegistry
motifs:
- id: MOTIF.SINNE
  label: sinne
  status: CANON
  function: sensory cognition; reader enters world through Claes
  progression:
  - sensation
  - recognition
  - comparison
  - pattern
  - understanding
  - choice
  - 'adult: perceive→distinguish→choose→carry'
- id: MOTIF.TIK_TIK_TIK
  label: tik-tik-tik
  status: CANON
  function: sound motif moving from work/patience to violence/loss and later integration
- id: MOTIF.INCENSE_WAX
  label: wierook en kaarslicht
  status: CANON
  function: sensory memory anchor from early mass onward
- id: MOTIF.CARRIER_MEANING
  label: drager / bewerking / betekenis
  status: CANON
  function: same carrier can change readability, function or meaning
  instances:
  - music contrafact
  - printed play
  - book
  - material process
  - game position
  - memoriaal
- id: MOTIF.MERELS_WAYS
  label: stenen en wegen
  status: CANON
  function: relations and pathways matter more than counted possessions
  anchor: Gij hebt mijn stenen geteld. Ik heb uw wegen geteld.
- id: MOTIF.FIRE_WATER
  label: vuur/lucht ↔ water/aarde
  status: CANON
  function: youth elemental symmetry Goes/Reimerswaal
  guardrail: historical disasters first; not didactic allegory
- id: MOTIF.MUSIC_OLD_TUNE
  label: de oude wijs
  status: CANON
  function: auditory continuity across confessional change and preparation for hidden readability
- id: MOTIF.BLACKENING_REVEAL
  label: zwarting als onthulling
  status: CANON
  function: vitriol darkens hidden tannin layer and makes text readable; Nigredo resonance without didactic naming
- id: MOTIF.BREAD
  label: brood / gest / oven
  status: CANON_CONTEXT
  function: material transformation, measure, labour, food and social order
- id: MOTIF.CASTANEA
  label: Castanea
  status: CANON_CONTEXT
  function: independent botanical, family-memory and later Castanienbloem/Nissepat resonance; no longer a Brevísima recovery key or authentication step
  guardrail: do not restore the deprecated Castanea cipher/key-anchor function without an explicit new decision
- id: MOTIF.CONCOCTIONIST
  label: concoctionist
  status: CANON
  function: >-
    Long-range verbal callback beginning as Dee's learned, deliberately inaccurate joke about Cornelis' occupation as biersteker and maturing into a description of Claes' and Mayken's joint capacity to bring substances, observations and relations into the right proportion without confusing mixture with mastery.
  progression:
  - 'first Dee encounter, ca.1563: biersteker is playfully overtranslated into the semantic field of concoction/compounding'
  - 'Cornelis: combines routes, casks, credit, people and trust rather than medicinal substances'
  - 'Mayken: materially closest to literal compounding through apothecary preparation, weighing, extraction and materia medica'
  - 'Claes: learns to combine material process with judgement, relation and responsibility'
  - 'mature callback: right relation and proportion matter more than brute force or possession'
  guardrails:
  - "'Concoctionist' is the author-side motif label; do not require Dee to utter that exact English noun unless a period attestation is separately established."
  - "Dee's joke is intentionally not an accurate lexical translation of biersteker."
  - 'Do not turn Cornelis into an apothecary, physician or alchemist because of the joke.'
  - 'Do not reduce Mayken to an ingredient, assistant or symbolic completion of Claes; her practical knowledge and agency remain independent.'
```

---

# SOURCE FILE: `narrative/themes.yaml`

```yaml
schema_version: 1.2.0
kind: ThemeRegistry
themes:
  - id: THEME.CLAES.CONTROLLING_IDEA
    type: ControllingIdea
    statement: "A man who seeks hidden order becomes whole only when knowledge ceases to be a means of control and becomes responsibility toward other people."
    canon_status: CANON
    applies_to: [ARC.CLAES.LIFE, ARC.CLAES.MACRO_TRANSMUTATION]
    ko_targets: [KO.STORY, KO.VALUE, KO.CHARACTER]

  - id: THEME.CLAES.DRAMATIC_QUESTION
    type: DramaticQuestion
    statement: "What does truth ask of Claes toward the other when certainty, safety and control are impossible?"
    canon_status: CANON
    applies_to: [ENT.PERSON.CLAES]

  - id: THEME.CLAES.DESIRE
    type: CharacterDesire
    statement: "Claes wants to understand the hidden order behind visible reality."
    canon_status: CANON
    subject: ENT.PERSON.CLAES
    ko_targets: [KO.CHARACTER.WANT]

  - id: THEME.CLAES.PSYCHOLOGICAL_NEED
    type: CharacterNeed
    statement: "Claes must recover trust in embodied perception — the sinne — and learn to act without first acquiring complete certainty."
    canon_status: CANON
    subject: ENT.PERSON.CLAES
    story_claims: [STC.CLAES.NEED.001, STC.CLAES.SINNE.001]
    ko_targets: [KO.CHARACTER.NEED]

  - id: THEME.CLAES.MORAL_NEED
    type: MoralNeed
    statement: "Claes must learn that knowledge and perception increase responsibility toward other people; discernment must become choice and choice must accept consequence without total control."
    canon_status: CANON
    subject: ENT.PERSON.CLAES

  - id: THEME.CLAES.SPIRITUAL_JOURNEY
    type: SpiritualJourney
    statement: "Claes moves from 'What is true?' toward 'What does this truth ask of me toward the other?' and from matter toward spirituality through, not away from, embodied matter."
    canon_status: CANON
    subject: ENT.PERSON.CLAES
    material_vessel: [senses, bodies, craft, books, plants, fire, water, alchemical_operations]
    culmination: "knowledge-as-control → wisdom-in-relation → transmission-and-release"

  - id: THEME.CLAES.LIE.CHILD
    type: CharacterLie
    statement: "If I look carefully enough, I can prevent being surprised or losing what matters."
    canon_status: CANON
    subject: ENT.PERSON.CLAES
    active_phase: ARC.CLAES.LIFE.P02

  - id: THEME.CLAES.LIE.ADULT
    type: CharacterLie
    statement: "If I understand the process, I can control the consequences."
    canon_status: CANON
    subject: ENT.PERSON.CLAES
    active_phase: ARC.CLAES.LIFE.P05

  - id: THEME.CLAES.FINAL_TRUTH
    type: SelfRevelation
    statement: "The value of a right action is not determined by certainty that it will succeed; mature mastery can transmit and release rather than possess."
    canon_status: CANON
    subject: ENT.PERSON.CLAES
    threshold_instance: NI.CHAPTER.1584.01
    ko_targets: [KO.CHARACTER.REVELATION, KO.VALUE]

value_axes:
  - id: VALUE.CLAES.TRUTH
    spectrum: [ignorance, recognition, knowledge, certainty, wisdom]
    warning: "Knowledge and certainty are not synonyms."
  - id: VALUE.CLAES.AGENCY
    spectrum: [passivity, observation, choice, action, control]
    warning: "Action and control are not synonyms."
  - id: VALUE.CLAES.RELATION
    spectrum: [isolation, secrecy, protection, trust, love]
    warning: "Protection and possession are not synonyms."
  - id: VALUE.CLAES.FAITH
    spectrum: [fear, certainty-seeking, obedience, trust-under-uncertainty, responsible-faith]
  - id: VALUE.CLAES.MASTERY
    spectrum: [counting-pieces, seeing-routes, blocking-routes, balancing-routes, leaving-space]
    motif: MOTIF.MERELS_WAYS
  - id: VALUE.CLAES.SINNE
    spectrum: [sensory-openness, vigilance, blunting, recovery, resonance, embodied-discernment]
    warning: "Trauma may constrict perception; recovery is not a return to innocence but a deeper embodied sovereignty."
    world_modules: [WORLD.RELIGIOUS_SPACE.SENSORY_CHURCH]
    authoring_rule: "Use sensory perception as cognition and social/spatial inference, not as a five-senses checklist."

scene_diagnostic_contract:
  required_fields_when_scene_is_developed:
    - opening_value
    - character_objective
    - conflict_or_pressure
    - turning_point
    - closing_value
    - value_charge_change
    - story_claims_introduced_or_paid_off
    - arcs_advanced
    - knowledge_delta
    - object_state_delta
    - motif_payoff_or_plant
    - ko_targets
```

---

# SOURCE FILE: `WRITING_PROTOCOL.md`

```markdown
# Writing Protocol — Claes

**Status:** CURRENT AUTHORING AUTHORITY  
**Synchronized through:** Round D — 16 August 2026

This protocol applies to any AI or human assistant that drafts, rewrites, extends, critiques or structurally edits prose for **Claes Nissepat**.

It is subordinate to active canon and historical evidence, and must be read together with `AI_ONBOARDING.md`. For causal chapter construction, load Round C first; for literary evaluation, apply the Round-D gates in `narrative/editorial_gates.yaml` and `review/READER_EXPERIENCE_PROTOCOL.md`.

## 1. Writing is not canon creation by default

A prose draft is an **implementation of existing canon**, not permission to invent new canon.

When a scene requires a choice that is currently `OPEN` or `PROPOSED`, do not silently decide it. Keep the prose noncommittal or state the proposed closure separately for human approval.

## 2. Pre-draft continuity and story packet

Before writing, identify the smallest useful packet of records:

1. relevant causal hinge in `ARC.CLAES.CAUSAL_SPINE`;
2. relevant `NI.*` Narrative Instance, if one exists;
3. active `STC.*` Story Claims;
4. all participating `ENT.*` records;
5. relevant `OBJ.*` state biographies;
6. actor knowledge-state boundaries;
7. relevant `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*` and `VALUE.*` records;
8. applicable Corpus / Anima / Spiritus register(s), if the Great-Work architecture matters;
9. relevant `WORLD.*` module, domain dossier and `domain_scene_pack`;
10. relevant `OPEN.*` decisions;
11. Lemma result only when the scene depends on a deterministic constraint;
12. if Mayken appears: `ARC.MAYKEN.LIFE` and `REL.CLAES.MAYKEN.CONJUNCTIO`.

If no `NI.*` exists, treat the requested scene as a proposal until its place, function and canon dependencies are established.

Do not begin from “which research can I display?”. Begin from **which person wants what, under which pressure, at which causal hinge**.

## 3. Scene contract

Every substantive scene should be able to answer:

- **Whose scene is this?** POV and focal consciousness.
- **What does the viewpoint character want now?** Concrete scene desire, not life-theme abstraction.
- **What pressure prevents easy attainment?** Person, circumstance, material reality, ignorance or moral conflict.
- **What is the opening value?** For example trust, safety, control, belonging, certainty, agency.
- **What turns?** A choice, discovery, action, reversal or revelation.
- **What is the closing value?** It should differ meaningfully from the opening value unless deliberate stasis under pressure is itself the dramatic result.
- **What changes in the operating Storybible?** Knowledge, possession, relationship, commitment, risk, location, object state, question or obligation.
- **Which arc advances?** If none, explain why the scene is still necessary.
- **What changes for the reader?** Orientation, expectation, emotion, tension, question, knowledge or memory.

A scene that only transfers background information should normally be revised until the information is carried by desire, pressure and change.

## 4. Scene necessity — the retain / revise / merge / cut gate

Every scene must be necessary in at least one of four dimensions **and** survive the uniqueness test.

### Plot necessity

The scene causes, prevents, reveals or materially changes a later event, obligation, risk or decision.

### Character necessity

The scene contains a consequential choice, revelation, value shift, relationship shift or self-revelation that cannot be removed without flattening an arc.

### Information necessity

The reader needs the information for a later turn or consequence, and this time/place/form is a strong delivery point.

### Reader-experience necessity

The scene creates a necessary experience: tension, dread, intimacy, relief, wonder, orientation, anticipation, surprise, grief, recovery or designed disorientation with later payoff.

### Uniqueness test

A scene is not retained merely because it is useful. Ask:

> **Can another scene perform every useful function better?**

If yes, this scene should not survive as a separate scene.

### Editorial verdicts

- **RETAIN** — indispensable function and already the strongest available place/form.
- **REVISE** — indispensable function, but weak execution, weak turn, weak POV, poor prose, poor pacing or avoidable reader friction.
- **MERGE** — necessary material duplicates another scene or gains force when combined.
- **CUT** — no indispensable function, or all functions are better served elsewhere.

Historical richness, research effort, thematic symbolism, a favorite image or a beautiful passage are **not independent retention reasons**.

## 5. Claes voice and cognition

Claes' core cognitive signature is **sinne**:

`sensation -> recognition -> comparison -> pattern -> understanding -> choice`

In mature form:

`perceive -> distinguish -> choose -> carry -> release`

Write his intelligence through what he notices, compares, tests, remembers and fails to notice in time. Avoid making him sound omniscient or like a modern analyst explaining the author's architecture.

His gift is prolonged, embodied observation. His danger is remaining in observation after action is required.

## 6. Mayken voice and agency

Mayken is not a derivative Claes function. Her epistemology tends toward material identity, condition, preparation, measurement, trained sensation, practical contradiction and error control.

Whenever Mayken appears in a developed scene, ask:

> **What does Mayken want or refuse here if Claes were absent from the scene?**

She may disagree because of her own work, judgement, loyalty, risk or value system. Competence does not make her omniscient. Do not write her as reward, therapist, saint, decoder or missing ingredient.

The mature relationship must preserve **two centers of agency**.

## 7. Do not write the Storybible into the novel

The reader must experience the architecture, not receive lectures about it.

Do not make characters explain:

- Nigredo, Albedo, Rubedo or Projectio merely because those phases organize the book;
- Corpus / Anima / Spiritus as an authorial register system;
- McKee value shifts;
- the complete recovery architecture before a character can know it;
- historical research caveats as exposition;
- a motif's symbolic meaning.

Authorial structure should be dramatized through event, material, perception, repetition, choice and consequence.

The governing Great-Work sentence remains:

> **The author knows the Work; Claes undergoes it; the reader experiences it.**

## 8. Historical prose discipline

Prefer concrete early-modern material reality over generalized “historical” decoration.

Check:

- what the character can physically see, smell, hear, touch and name;
- contemporary social role and hierarchy;
- travel time and geography;
- religious practice appropriate to date/place;
- printing, schooling, trade, food, tools and book production appropriate to the local context;
- whether a modern term, institution or concept has slipped into narration/dialogue.

Do not make every sentence archaic. Modern readability is allowed; modern worldview leakage is not.

Never turn a source-weighted reconstruction into a categorical historical assertion.

World detail earns prose space when it creates **pressure, choice, contrast, inference, consequence or reader experience**.

## 9. Knowledge discipline

A character may only act on information available to that character at that time.

Before any revelation or inference, ask:

- Has the character encountered the necessary person/object/text?
- Has the information already been acquired?
- Was it understood, or merely seen?
- Is the memory available and plausible here?
- Does another character know more or less?

Knowledge asymmetry is a story resource. Do not flatten it for convenience.

## 10. Object discipline

Important books, manuscripts and material carriers have biographies.

Do not treat an object as a static prop. Verify:

- current holder;
- physical state;
- visible versus hidden features;
- what the holder believes the object is;
- what function is active in this period;
- whether the object can plausibly be at this location.

For the memoriaal, current canon is direct hidden readable print plus later chemical development. Never reintroduce a retired cryptographic recovery chain.

## 11. Technical, alchemical and puzzle scenes

Technical detail exists to force perception, interpretation, cooperation, material consequence and moral decision. It is not a display case for cleverness.

Current alchemical process must obey material continuity and the active chemical guardrails. The Great Work is author-side architecture, not permission to force every scene into an operation name.

Merels remains a game, skill, relationship device and motif; it is not a Brevísima recovery key.

When technical detail becomes longer than the dramatic action it serves, compress it.

## 12. Relationship writing

A relationship scene should alter a relationship value or expose pressure within it.

Examples:

- Claes/Cornelis: dependence -> admiration -> exclusion -> inheritance -> differentiation;
- Claes/Dee: recognition -> formation -> critical independence -> internalized legacy;
- Claes/Mayken: separate expertise -> chosen risk -> reciprocal trust -> love without possession -> conjunctio with two centers of agency.

Do not reduce supporting characters to functions in Claes' development. They must exert their own pressure, competence, limits and choices.

## 13. Motif use

Motifs work best through recurrence with changed context.

Do not announce a motif. Reintroduce its sensory/material form and allow its meaning to shift.

Examples include:

- `tik-tik-tik`;
- incense/wax;
- merels: stones versus ways;
- carrier / treatment / meaning;
- fire/air versus water/earth;
- old melody / changed words;
- blackening as revelation;
- bread / gest / oven;
- Castanea.

A recurrence should normally differ in emotional or dramatic value from its previous occurrence.

## 14. Prose-quality gate

Line polish begins **after** the scene proves that it should exist.

Test prose for:

### POV filtration

Details must be selected by this consciousness under this pressure. Avoid neutral-camera inventory when a character's perception can give the detail a function.

### Concrete language

Prefer concrete nouns, precise verbs and material action over abstract explanation. Abstract thought is allowed when it belongs to the consciousness and has been earned by material experience.

### Rhythm

Sentence and paragraph rhythm should respond to attention, action, hesitation, shock, intimacy and consequence. Avoid uniformly polished cadence that makes every moment feel equally weighted.

### Sensory selectivity

Sensory detail should perform cognition, atmosphere, pressure or social/spatial inference. Never checklist all five senses.

### Research metabolism

No paragraph should exist mainly to prove that the author researched it. Historical knowledge should be metabolized into action, obstacle, object, habit, inference or consequence.

### Metaphor discipline

Use images generated by the material and emotional field of the scene. Avoid decorative stacking or metaphors that explain the theme on the author's behalf.

### Dialogue

Dialogue may remain readable to a modern reader, but avoid modern therapeutic vocabulary, institutional concepts, explanatory speeches and worldview leakage.

### Entry and exit

Enter as late as clarity permits. Exit after changed pressure, image, choice, obligation or question. Do not recap what the reader has just experienced.

## 15. Pacing gate

Pacing is **allocation of reader attention**, not simply speed.

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
- research detail that does not change action or inference;
- procedural steps whose dramatic information has already been delivered.

A useful scene pulse is:

`expectation -> pressure/complication -> turn -> altered forward pressure`

A quiet or recovery scene still needs to reorient desire, relationship, knowledge, expectation or the reader's emotional state. Calm is not filler.

Escalation means harder choices, deeper cost or sharper conflict of values — not simply louder events.

Chapter endings need forward pressure, not mandatory cliffhangers.

Diagnostic question:

> **Where would a cold reader skim, stop, reread for the wrong reason, or feel that the scene has already ended?**

## 16. Reader-experience gate

For every developed scene or chapter, identify the intended reader movement across:

- orientation;
- curiosity;
- emotional investment;
- tension / anticipation;
- cognitive load;
- surprise / inevitability;
- payoff;
- remembered image, action, relationship beat or question.

Do not optimize every scene for maximum intensity. Contrast is necessary.

Important rule:

> **Authorial intention and experienced effect are separate data.**

If the Storybible says a motive is clear but cold readers repeatedly miss it, the prose has a delivery problem.

Designed ambiguity is allowed. Confusion about basic causality, motivation, geography or chronology is not automatically productive ambiguity.

## 17. Cold-reader pass

A cold reader receives the **literary text**, not the hidden Storybible explanation.

Ask:

1. What happened?
2. What did the viewpoint character want?
3. What changed?
4. What is clear?
5. What remains uncertain in an interesting way?
6. What is confusing or requires rereading for the wrong reason?
7. Where did attention rise, sag or break?
8. What do you expect, hope or fear next?
9. What remains in memory?
10. If you would stop reading here, why?

AI may simulate this restricted-context pass. **AI cold-reader simulation does not substitute for actual human pilot readers.**

## 18. Human pilot-reader feedback loop

Use actual readers at deliberate milestones rather than only after line polish.

Useful milestones:

- after a structurally meaningful chapter cluster exists;
- after a complete act/book section or equivalent major arc movement exists;
- after a full draft, before final line polish.

Do not coach readers toward the intended interpretation before reading.

Separate:

- **reported experience/problem** — evidence about delivery;
- **reader-proposed fix** — a proposal, not an instruction.

Repeated independent observations carry more revision weight than isolated taste. Different phrasings may converge on the same underlying problem.

Use `review/READER_FEEDBACK_TEMPLATE.md` and the classifications `ISOLATED`, `REPEATED`, `CONVERGENT`, `RESOLVED`, `INTENTIONAL_VARIANCE`.

Reader voting never decides canon or theme.

## 19. Meedogenloze redacteur — fixed editorial mode

This is a standing mode for hard editorial review.

> **Niet aardig, wel precies. Als een scène niet werkt, zeg dat. Geen complimenten en geen verzachtende formuleringen wanneer die de diagnose vertroebelen.**

The goal is diagnostic precision, not performative hostility.

Required order:

1. **Verdict** — one sentence.
2. **Necessity** — does the scene need to exist?
3. **Primary/fatal problem** — identify the largest failure first.
4. **Causality and character choice**.
5. **Pacing and reader experience**.
6. **Prose quality**.
7. **Continuity/historical risk**, if any.
8. **RETAIN / REVISE / MERGE / CUT**.
9. **Smallest material revision** that could make it work, if revision is warranted.

Do not praise historical accuracy as compensation for inert fiction. A technically correct scene may still need to be cut.

## 20. McKee/NOS diagnostic pass after drafting

After a draft, test it without forcing formula:

- Is there a meaningful value shift?
- Is conflict progressively harder rather than merely louder?
- Does the turning point come from action/choice/discovery rather than author explanation?
- Is exposition attached to active desire?
- Is the scene's outcome earned by prior setup?
- Does pressure reveal character?
- Does the scene change the trajectory of an arc, relationship or obligation?
- Is the gap between expectation and result dramatically useful?

External `KO.*` knowledge objects may inform this diagnosis, but they do not override Claes canon.

## 21. Draft output convention

For substantial new prose, provide or record a compact metadata note separate from the literary text:

- intended `NI.*` or proposed new Narrative Instance;
- causal hinge;
- story-time window;
- POV;
- active claims used;
- knowledge/object constraints checked;
- active Corpus / Anima / Spiritus register(s), if relevant;
- opening -> closing value;
- arcs/relationships/motifs advanced;
- intended reader movement;
- any new canon choice proposed;
- unresolved questions deliberately left open.

The literary prose itself should remain literary prose; do not embed these labels in the novel.

## 22. Editing existing prose

When revising an existing chapter:

1. establish whether each scene is RETAIN / REVISE / MERGE / CUT **before** line polishing;
2. preserve all active canon unless explicitly instructed otherwise;
3. identify continuity conflicts before stylistic rewriting;
4. preserve established setup/payoff unless there is an approved structural change;
5. do not “improve” historical ambiguity into false precision;
6. report any sentence whose repair requires a canon decision rather than silently deciding it;
7. use reader evidence to identify delivery failures, but do not let reader suggestions silently rewrite canon;
8. retest material revisions that were made to solve repeated reader problems.

## 23. Final gate before human review or structural lock

A draft is ready for review when:

- it is chronologically and geographically possible;
- character knowledge is valid;
- object provenance is valid;
- no open decision has been silently closed;
- the scene contains a dramatic function and value movement;
- the scene survives the necessity + uniqueness test;
- the provisional verdict is not CUT or unresolved MERGE;
- historical reconstruction remains properly qualified;
- prose quality passes POV, concrete-language, rhythm, sensory-selectivity and research-metabolism checks;
- pacing gives attention to the right moments;
- intended reader experience is identifiable;
- cold-reader failures have been logged when relevant;
- human pilot-reader evidence is scheduled or incorporated at the appropriate milestone;
- motif and thematic resonance arise from action/material rather than explanation;
- any proposed canon changes are explicitly separated from the prose.

A scene can pass continuity and still fail fiction. **Accuracy is a constraint; reader experience is part of the result.**
```

---

# SOURCE FILE: `narrative/domain_scene_packs.yaml`

```yaml
schema_version: "1.0.0"
kind: DomainScenePackRegistry
purpose: "Machine-readable retrieval bridge from historical domains to chapter/scene construction. Packs constrain world state; they do not create fictional scenes or participation."
packs:
  - id: PACK.BREAD.GOES_YOUTH
    label: "Goes youth — bread/bakery practice"
    status: AUTHORING_READY_SCENE_CONTEXT
    world_modules: [WORLD.BREAD_GRAIN, WORLD.GOES]
    detail_file: storybible/domains/BREAD_GRAIN_BAKING_1540_1602.md
    source_claims: [SC.HIST.BREAD.URBAN_BAKERY.DEFAULT.001, SC.HIST.BREAD.ASSIZE.001]
    time_window: "1547-1554"
    fiction_gate: "OPEN.BAKERY.SCENE.001 must be placed before this becomes an actual scene."
    action_chain: [grain, flour, mix, knead, ferment, shape, fire_oven, prepare_oven, bake, cool_inspect_sell]
    sensory_rule: "one dominant material sense + one counter-sense + one inference"
    hard_guardrails: ["no exact modern recipe", "no unsupported household oven", "no rigid grain-status taxonomy"]

  - id: PACK.BEER.GOES_BIERSTEKER
    label: "Goes — Cornelis as biersteker"
    status: AUTHORING_READY_SCENE_CONTEXT
    world_modules: [WORLD.BEER_BREWING_DISTRIBUTION, WORLD.GOES]
    detail_file: storybible/domains/BEER_BREWING_BEERSTEKER_1540_1580.md
    source_claims: [SC.HIST.BEER.PROCESS.HOPPED.001, SC.HIST.BIERSTEKER.DISTRIBUTION.001]
    action_chain: [order_negotiate, receive, inspect, record, store, move, deliver, settle]
    sensory_rule: "condition + quantity + movement: leakage/sourness/cask weight/cellar state"
    hard_guardrails: ["Cornelis is not automatically brewer", "Nissepad brewery not proven Cornelis property", "no default gruit", "no ABV/IBU/style taxonomy"]

  - id: PACK.REIMERSWAAL.SCHOOL_1554_1561
    label: "Reimerswaal — cost pupil, school and changing city"
    status: AUTHORING_READY_SCENE_CONTEXT
    world_modules: [WORLD.REIMERSWAAL, WORLD.HISTORICAL_SUBSTRATE_1540_1605]
    detail_file: storybible/domains/REIMERSWAAL_SCHOOL_1554_1561.md
    source_claims: [SC.HIST.REIMERSWAAL.SCHOOL.CONTINUITY.001, SC.HIST.REIMERSWAAL.PRESSURE.1555_1561.001]
    time_slices: ["1554 arrival/functioning city", "1555 water pressure", "1557 structural damage", "1558 fire", "1561 renewed flood/departure"]
    school_reconstruction: [oral_recitation, grammar, memorisation, copying, correction, older_pupil_help]
    hard_guardrails: ["exact 1554 Latin curriculum is reconstruction", "no invented rector/building", "not seven years beginner Latin", "city not abandoned ruin"]

  - id: PACK.REDERIJKERS.GOES_CHAMBER
    label: "Goes — Nardusbloem chamber evening"
    status: AUTHORING_READY_SCENE_CONTEXT
    world_modules: [WORLD.GOES]
    detail_file: storybible/domains/REDERIJKERS_LANDJUWEEL_1561.md
    source_claims: [SC.HIST.REDERIJKERS.PUBLIC_COMMUNICATION_NETWORK.001]
    institution: ENT.ORG.GOES.NARDUSBLOEM
    location: ENT.LOC.GOES.ZUSTERHUIS
    action_options: [read_correct_text, rehearse, refrein, spel_van_sinne, esbattement, blazon, travel_costs, sociability_news]
    hard_guardrails: ["Cornelis office not invented", "1563 Catholic/Magdalena institutional context retained", "chamber is not church"]

  - id: PACK.REDERIJKERS.ANTWERP_LANDJUWEEL_1561
    label: "Antwerp 1561 — Landjuweel observer context"
    status: AUTHORING_READY_SCENE_CONTEXT
    world_modules: [WORLD.ANTWERP, WORLD.HISTORICAL_SUBSTRATE_1540_1605]
    detail_file: storybible/domains/REDERIJKERS_LANDJUWEEL_1561.md
    source_claims: [SC.HIST.LANDJUWEEL.ANTWERP.14_CHAMBERS.1561.001, SC.HIST.LANDJUWEEL.GOES_PARTICIPATION.1561.001]
    dramatic_mechanism: "sign → performance → audience → competing interpretation → social consequence"
    hard_guardrails: ["Goes not proven official competitor", "no Goese prize invented", "Dee absent in 1561"]

  - id: PACK.ANTWERP.1561
    label: "Antwerp 1561 — city as theatre"
    status: AUTHORING_READY_SCENE_CONTEXT
    world_modules: [WORLD.ANTWERP]
    detail_file: storybible/domains/ANTWERP_TIME_SLICES_1561_1585.md
    dominant_world_state: [Landjuweel, trade, public_rhetoric, crowd_routes, multilingual_city]
    hard_guardrails: ["Claes observer/network visitor", "Dee absent", "no official Goese competition role"]

  - id: PACK.ANTWERP.1563_1564
    label: "Antwerp 1563–early 1564 — city as book/workshop"
    status: AUTHORING_READY_SCENE_CONTEXT
    world_modules: [WORLD.ANTWERP, WORLD.PRINT_BOOK_NETWORK]
    detail_file: storybible/domains/ANTWERP_TIME_SLICES_1561_1585.md
    dominant_world_state: [print_divided_labour, multilingual_correspondence, Silvius_Dee, copying_accounts, censorship_permissions]
    hard_guardrails: ["Claes not university student", "Plantin not automatic conspirator"]

  - id: PACK.ANTWERP.1566
    label: "Antwerp 1566 — city as broken image"
    status: AUTHORING_READY_SCENE_CONTEXT
    world_modules: [WORLD.ANTWERP, WORLD.RELIGIOUS_SPACE.SENSORY_CHURCH]
    detail_file: storybible/domains/ANTWERP_TIME_SLICES_1561_1585.md
    dominant_world_state: [iconoclasm, altered_religious_space, contested_public_confession, memory_loss]
    hard_guardrails: ["show material/social rupture", "no simple binary population map"]

  - id: PACK.ANTWERP.1567_1569
    label: "Antwerp 1567–1569 — surveillance and repression"
    status: AUTHORING_READY_SCENE_CONTEXT
    world_modules: [WORLD.ANTWERP, WORLD.HISTORICAL_SUBSTRATE_1540_1605]
    detail_file: storybible/domains/ANTWERP_TIME_SLICES_1561_1585.md
    dominant_world_state: [repression, visibility_risk, partial_information, arrest_documentation, public_punishment]
    hard_guardrails: ["Cornelis exact case is fiction", "execution date 19 November 1569 current canon"]

  - id: PACK.ANTWERP.1576_1578
    label: "Antwerp 1576–1578 — wound, rumour and print release"
    status: AUTHORING_READY_SCENE_CONTEXT
    world_modules: [WORLD.ANTWERP, WORLD.PRINT_BOOK_NETWORK, WORLD.HISTORICAL_SUBSTRATE_1540_1605]
    detail_file: storybible/domains/ANTWERP_TIME_SLICES_1561_1585.md
    dominant_world_state: [Spanish_Fury_memory, rumour_letters_print, production_risk, Projectio_Word]
    hard_guardrails: ["Brevísima provenance remains fiction", "reveal is not decryption"]

  - id: PACK.ANTWERP.1585
    label: "Antwerp 1585 — transformed formative city"
    status: AUTHORING_READY_SCENE_CONTEXT
    world_modules: [WORLD.ANTWERP, WORLD.HISTORICAL_SUBSTRATE_1540_1605]
    detail_file: storybible/domains/ANTWERP_TIME_SLICES_1561_1585.md
    dominant_world_state: [capitulation, migration, network_fracture, changed_public_order]
    hard_guardrails: ["do not reduce to battlefield date", "do not back-project this state into 1560s"]

  - id: PACK.GOES.SCHUTTERIJ
    label: "Goes — shooting guild/civic defence context"
    status: AUTHORING_READY_SCENE_CONTEXT
    world_modules: [WORLD.GOES, WORLD.SCHUTTERIJ_MILITARY]
    detail_file: storybible/domains/SCHUTTERIJ_MILITARY_PRACTICE_1550_1607.md
    source_claims: [SC.HIST.GOES.SCHUTTERIJ.FIREARM_GUILD.16C.001]
    categories_to_keep_separate: [schuttersgilde, civic_watch, garrison_professionals, later_standardized_drill]
    hard_guardrails: ["1516/1530 firearm-guild date conflict preserved", "no later equipment automatically in 1572"]

  - id: PACK.MILITARY.DEGHEYN_1607_COMPARATOR
    label: "Late military practice — De Gheyn comparator"
    status: AUTHORING_REFERENCE_NOT_EARLY_SCENE_TEMPLATE
    world_modules: [WORLD.SCHUTTERIJ_MILITARY]
    detail_file: storybible/domains/SCHUTTERIJ_MILITARY_PRACTICE_1550_1607.md
    source_claims: [SC.HIST.DEGHEYN.WAPENHANDELINGHE.1607.001]
    function: "late comparator for standardized embodied weapon sequence"
    hard_guardrails: ["not a 1572 Goes drill manual", "no automatic twelve-apostles/fork/fire-rate back-projection"]
```

---

# SOURCE FILE: `narrative/editorial_gates.yaml`

```yaml
schema_version: 1.0.0
kind: EditorialGateRegistry
purpose: "Round D authoring quality gates. These records govern drafting and revision; they do not create story canon."
gates:
- id: GRD.EDITORIAL.SCENE_NECESSITY
  type: EditorialGate
  status: ACTIVE_AUTHORING_POLICY
  question: "Does this scene need to exist here, in this form?"
  necessity_dimensions:
  - plot: "The scene causes, prevents, reveals or materially changes a later event, obligation, risk or decision."
  - character: "The scene contains a consequential choice, revelation, value shift, relationship shift or self-revelation that cannot be removed without flattening the character arc."
  - information: "The reader needs this information for a later turn or consequence, and this scene/time/form is a strong delivery point."
  - reader_experience: "The scene creates a necessary reader experience such as tension, dread, relief, intimacy, wonder, orientation, disorientation-with-payoff, surprise or anticipation."
  uniqueness_test: "Being useful is not enough. If every useful function is served better elsewhere, this scene should not survive as a separate scene."
  outcomes:
    RETAIN: "Necessary and currently the strongest place/form for at least one indispensable function."
    REVISE: "Necessary function, weak execution, weak turn, weak entry/exit, weak prose, unclear POV or avoidable reader friction."
    MERGE: "Necessary material duplicates another scene or can gain force by sharing one scene-turn with it."
    CUT: "No indispensable function, or all functions are served better elsewhere."
  hard_rule: "Historical richness, research effort, thematic symbolism or a beautiful passage are never sufficient reasons by themselves to retain a scene."

- id: GRD.EDITORIAL.PROSE_QUALITY
  type: EditorialGate
  status: ACTIVE_AUTHORING_POLICY
  tests:
  - "POV filters detail: the prose notices what this consciousness would notice now, under this pressure."
  - "Concrete nouns, verbs and material actions carry more weight than abstract explanation."
  - "Sentence and paragraph rhythm respond to perception, action, hesitation and consequence rather than staying metrically uniform."
  - "Sensory detail performs cognition, atmosphere, pressure or social/spatial inference; it is not a five-senses inventory."
  - "Research is metabolized into action and setting; no paragraph exists chiefly to prove that the author researched it."
  - "Metaphor grows from the material and emotional field of the scene; avoid decorative image stacking."
  - "Dialogue may be modern-readable but must not leak modern institutions, therapeutic language or explanatory worldview."
  - "Scene exits stop on changed pressure, choice, image, obligation or question rather than summarizing what the reader has just read."

- id: GRD.EDITORIAL.PACING
  type: EditorialGate
  status: ACTIVE_AUTHORING_POLICY
  tests:
  - "Expand time around irreversible choice, sensory recognition, danger, intimacy and costly consequence."
  - "Compress routine movement, repeated explanation and research detail that does not change the scene."
  - "Every scene should contain a pulse of expectation -> pressure/complication -> turn -> altered forward pressure, even when the turn is quiet."
  - "A recovery or breathing scene must still reorient desire, relationship, knowledge or expectation; calm is not filler."
  - "Chapter endings need forward pressure, not necessarily a cliffhanger."
  - "Escalation means harder choices or deeper cost, not simply louder events."
  diagnostic_question: "Where would a cold reader skim, stop, reread for the wrong reason, or feel that the scene has already ended?"

- id: GRD.EDITORIAL.READER_EXPERIENCE
  type: EditorialGate
  status: ACTIVE_AUTHORING_POLICY
  reader_state_fields:
  - orientation
  - curiosity
  - emotional_investment
  - tension_or_anticipation
  - cognitive_load
  - surprise_and_inevitability
  - payoff
  - remembered_image_or_question
  core_rule: "The intended effect and the experienced effect are separate data. Authorial intention never disproves reader confusion, boredom or false inference."
  ambiguity_rule: "Ambiguity may be designed; confusion about basic causal, spatial or motivational facts is not automatically productive ambiguity."

- id: GRD.EDITORIAL.COLD_READER
  type: EditorialGate
  status: ACTIVE_AUTHORING_POLICY
  protocol: "A cold-reader pass receives the prose and only minimal unavoidable front matter, not the Storybible explanation. It reports what the text itself communicated."
  required_questions:
  - "What happened?"
  - "What did the viewpoint character want?"
  - "What changed?"
  - "What is clear, uncertain and confusing?"
  - "Where did attention rise, sag or break?"
  - "What do you expect or fear next?"
  - "Which image, line, action or relationship beat remains in memory?"
  guardrail: "AI cold-reader simulation is useful but does not substitute for actual human pilot readers."

- id: GRD.EDITORIAL.PILOT_READER
  type: EditorialGate
  status: ACTIVE_AUTHORING_POLICY
  protocol: "Use actual readers at deliberate milestones and log observations in review records. Separate reported experience from proposed fixes."
  evidence_rule: "Repeated independent observations outrank isolated preferences. A reader's diagnosis of the problem is evidence; the reader's preferred solution is a proposal."
  suggested_milestones:
  - "after a structurally meaningful chapter cluster exists"
  - "after a complete act/book section or equivalent arc movement exists"
  - "after a full-draft pass before final line polish"
  guardrails:
  - "Do not coach readers toward the intended answer before they read."
  - "Do not discard a repeated comprehension problem merely because the Storybible explains it."
  - "Do not canonize reader suggestions automatically."

- id: GRD.EDITORIAL.RUTHLESS_EDITOR
  type: EditorialGate
  status: ACTIVE_AUTHORING_POLICY
  mode_name: "Meedogenloze redacteur"
  instruction: "Niet aardig, wel precies. Geef een hard oordeel over wat niet werkt. Geen complimenten of verzachtende formuleringen als die de diagnose vertroebelen."
  review_order:
  - verdict
  - scene_necessity
  - fatal_or_primary_problem
  - causality_and_character
  - pacing_and_reader_experience
  - prose_quality
  - continuity_or_historical_risk
  - retain_revise_merge_cut
  final_rule: "A technically correct scene may still be weak fiction. Historical accuracy and canon consistency are necessary constraints, not proof that the scene works."
```

---

# SOURCE FILE: `review/READER_EXPERIENCE_PROTOCOL.md`

```markdown
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
```

---

# SOURCE FILE: `review/READER_FEEDBACK_TEMPLATE.md`

```markdown
# Reader Feedback Record Template — Claes

Use one record per reading session or deliberately combined reader round. This is **review evidence**, not canon.

## Reading metadata

- **Text / chapter / scene:**
- **Version / commit / date:**
- **Reader type:** cold-reader simulation / general fiction reader / historical-fiction reader / historical-domain reader / other
- **Reader had Storybible context?** yes / no / partial
- **What was supplied before reading?**
- **Reading scope:** single scene / chapter / chapter cluster / act-book section / full draft

## Reader reconstruction — no author correction yet

- **What happened?**
- **Who seemed to want what?**
- **What changed by the end?**
- **Where and when did the reader think the scene occurred?**
- **What does the reader expect, hope or fear next?**
- **What remained in memory after reading?**

## Reader-experience observations

Rate only when useful; prose comments are more important than a number.

- **Orientation:**
- **Curiosity:**
- **Emotional investment:**
- **Tension / anticipation:**
- **Cognitive load:**
- **Surprise / inevitability:**
- **Payoff:**
- **Pacing / skim points:**
- **Wrong-reason rereads or confusion:**
- **Strongest remembered image/action/relationship beat:**

## Specific observations

For each observation, keep **experience/problem** separate from **reader-proposed fix**.

### Observation 1
- **Reported experience/problem:**
- **Location in text:**
- **Reader-proposed fix, if any:**
- **Classification:** ISOLATED / REPEATED / CONVERGENT / RESOLVED / INTENTIONAL_VARIANCE
- **Editorial hypothesis:**

### Observation 2
- **Reported experience/problem:**
- **Location in text:**
- **Reader-proposed fix, if any:**
- **Classification:** ISOLATED / REPEATED / CONVERGENT / RESOLVED / INTENTIONAL_VARIANCE
- **Editorial hypothesis:**

## Scene necessity gate

- **Plot necessity:** yes / no / unclear — why?
- **Character necessity:** yes / no / unclear — why?
- **Information necessity:** yes / no / unclear — why here?
- **Reader-experience necessity:** yes / no / unclear — what experience is indispensable?
- **Uniqueness test:** can another scene perform these functions better?

**Verdict:** RETAIN / REVISE / MERGE / CUT

## Ruthless-editor synthesis

- **One-sentence verdict:**
- **Primary/fatal problem:**
- **Causality / character:**
- **Pacing / reader experience:**
- **Prose quality:**
- **Continuity / historical risk:**
- **Smallest material revision:**

## Revision decision

- **What will change?**
- **What will deliberately not change?**
- **Does the revision touch canon or an OPEN decision?** If yes, stop and route that choice through the canon process before silently implementing it.
- **Retest needed?** cold reader / human pilot reader / both / no
- **Retest result:**
```

---

# SOURCE FILE: `storybible/MAYKEN_LAMPERT.md`

```markdown
# Mayken Adriaensdr. Lampert — geliefde van Claes

**ID:** `SB.CLAES.MAYKEN_LAMPERT`  
**Status:** CANONICAL DETAIL MODULE  
**Decision:** `DEC.CLAES.BELOVED.MAYKEN_LAMPERT.2026-08-14`  
**Historical source dossier:** `sources/SRC-HIST-GOES-LAMPERT-APOTHECARY-001.md`

This dossier is the detailed authority for the identity and historical embedding of the character formerly labeled only **geliefde / apothekersdochter**. It is synchronized to the later no-cipher memoriaal decision: Mayken is not a cryptographic solver and no special Dodoens carrier is required.

## 1. Canonical identity

**Mayken Adriaensdr. Lampert**, usually simply **Mayken**, is a fictional Goese woman born approximately in **1546**. In juridical-style naming she may appear as **Mayken Adriaens**, **Mayken Adriaensdochter** or, in project metadata, **Mayken Adriaensdr. Lampert**.

She is canonically:
- Claes' beloved and later partner;
- daughter of **Adriaen Jacobsz. Lampert** in novel genealogy;
- granddaughter of the older Goese apothecary **Jacob/Jacop Lampart/Lambert** and the historical household figure **Merricken** in novel genealogy;
- raised in a material/apothecary environment in Goes;
- approximately three to four years younger than Claes.

Mayken's mother remains fictionally **open**. Do not invent a historical wife of Adriaen merely to close the pedigree.

## 2. Historical foundation and fiction boundary

Historically attested:
- 1538: **Jacob Lampart den apotheker**;
- 1539: **Jacop de apotheker met Merricken zijn huisvrouw**;
- 1542: Merricken, wife of Jacop the apothecary, buys **Den Eenhoorn** west of the stadhuis;
- 1543: **Mayken huisvrouw Jacop Lampart** occurs in a Molendijk transfer;
- 1545: **Merricken huisvrouw Jacob Lambert apotheker** acquires Oprel property beside the Gasthuis;
- 1551 onward: **Adriaen Jacopsen Lampert** has a substantial Goese property trail;
- 1554 and 1556: **Adriaen Jacopsen apteker** is explicitly named in Goese acts;
- 1553 → 1555: Adriaen Jacopsen Lampert's **Nyen Zwaene** becomes a **verbrand huis genaamd de Zwaene**.

Supported but not literally proved by one act:
- Adriaen Jacopsen apteker is the same man as Adriaen Jacopsen Lampert;
- Adriaen is son/family successor of Jacob/Jacop Lampart/Lambert.

Explicit novel canon, not archival fact:
- Mayken Adriaensdr. Lampert exists as Adriaen's daughter;
- Adriaen is her father and Jacob/Merricken her paternal grandparents;
- Mayken becomes Claes' beloved;
- her precise childhood experiences, education and later relationship biography.

No currently searchable transport act identifies a historical daughter of Adriaen. This is absence of evidence in a property corpus, not evidence of absence.

## 3. Why the name Mayken

A **Mayken**, explicitly `huisvrouw Jacop Lampart`, occurs in the direct historical Lampart environment in 1543. The project reuses an attested family-environment name for the fictional daughter.

Do **not** claim this proves a grandmother-to-granddaughter naming pattern. The archive also uses **Merricken** for the wife of Jacop/Jacob the apothecary. Whether Mayken and Merricken are the same woman, variant forms, successive wives or different households remains unresolved.

## 4. Age and chronology

Working birth: **ca. 1546, Goes**.

- 18 May 1554: about seven or eight;
- 1561: about fourteen or fifteen;
- 1566: about nineteen or twenty;
- 1570: about twenty-three or twenty-four;
- 1584: about thirty-seven or thirty-eight;
- 1602: mid-fifties.

The age gap with Claes is roughly three to four years. They may have known of one another in childhood without being written as childhood sweethearts.

## 5. Shared fire, different loss

Mayken and Claes are both children of Goes who know the 1554 catastrophe, but they must **not** receive identical trauma biographies.

Claes loses Tanneken, Jan, the unborn sibling, the family home and then daily life with Cornelis. Mayken's historical anchor is different: the Lampert property **de Zwaene** is documented as a normal property before the fire and as a burned house in January 1555.

Novel function:
- Mayken remembers the fire as a child;
- her family experiences material disruption and rebuilding;
- her core household does not need to be annihilated;
- she therefore knows destruction but also knows that a material world can be rebuilt and worked in again.

This difference is essential. She is not Claes' trauma duplicate. She carries a counter-memory: fire can destroy, yet hands can return to work.

## 6. Apothecary formation

Mayken grows up around practical materia medica and apothecary work. Her expertise is embodied and operational rather than academic:
- recognizing plant material by form, smell, texture and condition;
- drying, storing, sorting and preparing substances;
- weighing and measuring;
- distinguishing contamination, substitution and deterioration;
- reading or using practical lists, recipes and botanical reference works;
- knowing that names, materials and preparations can diverge.

Ordinary Dodoens use can belong naturally to this world where historically appropriate. It no longer has any special cipher, nomenclator or key function.

Guardrail: do not give Mayken an unsupported university education, formal physician status or later seventeenth-century guild office.

## 7. Memoriaal reveal and material competence

The Brevísima mechanism is direct chemical steganography under `DEC.MEMORIAAL.DIRECT_TEXT_NO_CIPHER.2026-08-15`.

The text is already readable Diets/Brabant language, printed in a latent tannin/gum layer before binding. Green vitriol develops the letters. Therefore Mayken's role is **not** to reconstruct a cipher.

She may be independently valuable for:
- safe material handling;
- preparing or comparing dilute test solutions within the story's guarded reconstruction;
- observing paper, stain, colour change and print behaviour;
- reading the revealed text with Claes;
- spotting physical contradictions or overconfident interpretations;
- keeping lists, measurements and sequence notes;
- connecting the reveal to ordinary apothecary habits of identification and preparation.

She is **not**:
- a Dodoens key-holder;
- a nomenclator operator;
- the solver of merels, Monas or Castanea;
- a replacement for Claes' moral decision about what to do with the testimony.

This gives her competence without making the relationship mechanically dependent on the retired recovery architecture.

## 8. Relationship with Claes

`REL.CLAES.BELOVED` is the relationship **Claes ↔ Mayken**.

Dynamic:

**separate Goese histories → material proximity → collaborative verification → earned trust → love without possession → sensory/spiritual companionship.**

Mayken must never function merely as a reward for Claes' suffering or as a therapist. She has her own competence, history and judgement. She can contradict Claes because she knows things he does not.

Their epistemologies differ:
- Claes tends toward pattern, hidden order, memory, abstraction and prolonged observation;
- Mayken tests matter directly and trusts trained sensation, repeatability and practical contradiction.

Her presence later on the road toward Enkhuizen helps Claes recover the *sinne* because she draws him back into matter: smell, weather, touch, plants, preparation, food, fatigue, sound and shared physical travel. The recovery remains Claes' own work.

## 9. Name use

Preferred prose name: **Mayken**.  
Project/canonical full form: **Mayken Adriaensdr. Lampert**.  
Possible period forms: **Mayken Adriaens**, **Mayken Adriaensdochter**.

Avoid modernizing her to *Maaike* in the sixteenth-century narrative voice.

## 10. Guardrails

1. Mayken is fictional; no historical daughter has been identified.
2. Adriaen's apothecary identity is strongly supported but remains reconstruction where historical precision matters.
3. Jacob → Adriaen → Mayken is novel genealogy built on historical anchors, not discovered genealogy.
4. `Mayken huisvrouw Jacop Lampart` (1543) supplies an attested name environment, not proof of Mayken's grandmother.
5. Ordinary Dodoens use is allowed; the retired special Dodoens carrier is not.
6. Mayken shares the 1554 fire horizon with Claes but not his exact losses.
7. She contributes to Claes' recovery; she does not perform or complete it for him.
8. She may assist the direct chemical reveal, but she is not a cryptographic key-holder or decoder.
```

---

# SOURCE FILE: `narrative/mayken_independent_arc.yaml`

```yaml
schema_version: 1.0.0
kind: NarrativeArcExtension
records:
- id: ARC.MAYKEN.LIFE
  type: CharacterArc
  label: "Mayken — material competence, independent judgement and relation without absorption"
  canon_status: CANON
  protagonist: ENT.PERSON.BELOVED
  decision_id: DEC.MAYKEN.INDEPENDENT_ARC.2026-08-16
  identity_note: "ENT.PERSON.BELOVED is the legacy entity ID for the resolved character Mayken Adriaensdr. Lampert. Identity is not open."

  phases:
  - id: ARC.MAYKEN.LIFE.P01
    label: "Kind van een werkende materiële wereld"
    story_time: {earliest: '1546-01-01', latest_exclusive: '1554-05-18', precision: approximate}
    fixed_state:
    - "Mayken grows up in the fictional daughter-line of the historically anchored Lampert apothecary environment."
    - "Her formation is practical: plants, substances, storage, weight, condition, preparation and names that may not match matter perfectly."
    value_movement: "dependence -> trained attention"
    contrast_with_claes: "Claes is drawn toward hidden order and pattern; Mayken begins with whether the thing in her hand is actually what someone says it is."

  - id: ARC.MAYKEN.LIFE.P02
    label: "Brand, verlies en herstel"
    story_time: {earliest: '1554-05-18', latest_exclusive: '1566-01-01', precision: approximate}
    fixed_state:
    - "The Lampert property De Zwaene belongs to Mayken's fictional childhood fire horizon and is historically documented as burned property after 1554."
    - "Her household is not annihilated like Claes' household."
    value_movement: "material security -> damaged continuity -> rebuilding competence"
    function: "Mayken learns a counter-truth to Claes' wound: destruction is real, but damaged material life can sometimes be sorted, repaired, replaced and worked again."
    guardrail: "Do not make this a lesser version of Claes' trauma or invent identical bereavements."

  - id: ARC.MAYKEN.LIFE.P03
    label: "Volwassen vakkennis wordt eigen oordeel"
    story_time: {earliest: '1566-01-01', latest_exclusive: '1570-01-01', precision: approximate}
    status: CANON_FUNCTION_WITH_OPEN_EVENT_DESIGN
    value_movement: "inherited household competence -> personally owned judgement"
    required_authoring_result: "At least one developed sequence must show Mayken making a consequential material, social or moral judgement that is not caused by Claes' immediate problem."
    open_design: OPEN.MAYKEN.INDEPENDENT_MIDARC.001
    possible_but_not_canonized_lines:
    - "family/social pressure around religion, trade or apothecary standing"
    - "greater reliance on a female household or practical healing network"
    - "a kruidenvrouw-like practical role without unsupported formal medical status"
    guardrails:
    - "Do not silently copy Cornelis' prosecution arc onto Adriaen."
    - "Do not make Mayken's independence begin only when Claes notices her."

  - id: ARC.MAYKEN.LIFE.P04
    label: "Materiële tegenspraak en gedeeld risico"
    story_time: {earliest: '1570-01-01', latest_exclusive: '1571-01-01', precision: year}
    value_movement: "competence -> agency under moral risk"
    relationship: REL.CLAES.BELOVED
    function: "During the direct memoriaal reveal, Mayken contributes handling, measurement, observation, repeatability and contradiction. Her importance lies in being able to say that Claes' interpretation or procedure is materially wrong, not in solving a cipher."
    independent_choice_rule: "Her participation must include a reason and risk she accepts as Mayken, not merely obedience to Claes."

  - id: ARC.MAYKEN.LIFE.P05
    label: "Eigen volwassen lijn naast Claes"
    story_time: {earliest: '1571-01-01', latest_exclusive: '1584-01-01', precision: approximate}
    status: AUTHORIAL_DEVELOPMENT_REQUIRED
    value_movement: "collaboration -> sustained independent agency"
    function: "Mayken must not disappear into an off-screen waiting role between the 1570 reveal and the late recovery line. Her work, obligations, relationships and limits continue even when Claes' plot is elsewhere."
    required_scene_question: "What does Mayken want or refuse here if Claes were absent from the scene?"
    guardrail: "Exact profession, residence, household crisis and relationship chronology remain design work unless separately decided."

  - id: ARC.MAYKEN.LIFE.P06
    label: "Conjunctio zonder opgaan in de ander"
    story_time: {earliest: '1584-01-01', latest_exclusive: '1602-03-14', precision: developmental}
    value_movement: "independent competence -> chosen reciprocal relation"
    relationship: REL.CLAES.MAYKEN.CONJUNCTIO
    function: "Mayken travels/acts beside Claes in the late sensory-recovery line, returning attention to weather, plants, food, fatigue, preparation and bodily limits while retaining her own judgement."
    reciprocal_effect:
      on_claes: "embodied perception and relation reopen; certainty loses monopoly"
      on_mayken: "she chooses intimacy without surrendering competence, contradiction or separate agency"
    guardrail: "Do not write her as therapist, saintly healer or passive witness to Claes' enlightenment."

  - id: ARC.MAYKEN.LIFE.P07
    label: "Na de projectio"
    story_time: {earliest: '1602-03-13', precision: open-ended}
    status: CANON_FUNCTION_END_DETAILS_OPEN
    value_movement: "relation -> capacity to let the other act/release without possession"
    function: "Mayken's mature relation to Claes must remain compatible with the final projectio principle: love does not require control over his Work, outcome, memory or death."
    guardrail: "Mayken's own death, residence and exact final fate are not fixed here."

  scene_agency_contract:
  - "Every developed Mayken scene has her own objective, however small."
  - "At least one pressure in the scene must test her judgement, resources, reputation, body, work or relationship — not only Claes'."
  - "If she agrees with Claes, the writer must know why she could have disagreed."
  - "Her trained senses generate inference; do not reduce her to floral/medicinal atmosphere."
  - "Her errors remain possible. Competence is not omniscience."

  ko_targets: [KO.CHARACTER, KO.VALUE, KO.CONFLICT, KO.RELATIONSHIP]
```

---

# SOURCE FILE: `narrative/mayken_relationship_projection.yaml`

```yaml
schema_version: 1.0.0
kind: NarrativeRelationshipExtension
records:
- id: REL.CLAES.MAYKEN.CONJUNCTIO
  type: RelationshipExtension
  label: "Claes and Mayken — complementarity, risk and conjunctio"
  canon_status: CANON
  participants: [ENT.PERSON.CLAES, ENT.PERSON.BELOVED]
  parent: REL.CLAES.BELOVED
  decision_ids:
  - DEC.CLAES.BELOVED.MAYKEN_LAMPERT.2026-08-14
  - DEC.MAYKEN.INDEPENDENT_ARC.2026-08-16
  - DEC.CLAES_MAYKEN.CONJUNCTIO.2026-08-16
  identity_note: "ENT.PERSON.BELOVED is Mayken Adriaensdr. Lampert; the legacy entity ID does not indicate an open identity."
  arcs:
  - ARC.CLAES.SINNE_RECOVERY
  - ARC.MAYKEN.LIFE
  - ARC.CLAES.GREAT_WORK.AUTHORIAL

  movement:
  - phase: "separate expertise"
    story_time: {earliest: '1566-08-01', latest_exclusive: '1570-01-01', precision: bounded}
    claes: "pattern, memory, hidden order, inherited secrecy"
    mayken: "materia medica, condition, measurement, repeatability, direct contradiction"
    relation: "proximity without fusion; each can know something the other cannot"
  - phase: "collaborative risk"
    story_time: {earliest: '1570-01-01', latest_exclusive: '1571-01-01', precision: year}
    relation: "controlled material reveal becomes a test of trust because error, testimony and consequence are shared without becoming identical responsibilities"
    guardrail: "Mayken does not solve the text; Claes does not own her expertise."
  - phase: "parallel adult agency"
    story_time: {earliest: '1571-01-01', latest_exclusive: '1584-01-01', precision: approximate}
    relation: "their bond may persist, change, strain or deepen, but Mayken retains an adult line that cannot be reduced to waiting for Claes"
    design_note: "Exact relationship chronology in this span remains to be scenically designed; no unearned off-screen perfect harmony."
  - phase: "conjunctio"
    story_time: {earliest: '1584-01-01', latest_exclusive: '1602-03-14', precision: developmental}
    relation: "difference becomes the condition of mature union: perception and abstraction, matter and pattern, care and responsibility, intimacy and separate agency can coexist"
    claes_shift: "from secrecy/control toward relation and release"
    mayken_shift: "from competence defended as separate ground toward chosen reciprocal intimacy without surrender of judgement"
  - phase: "release"
    story_time: {earliest: '1602-03-13', precision: open-ended}
    relation: "neither partner possesses the other, the Work or its outcome; mature love can permit action and loss without converting them into ownership"

  authoring_tests:
  - "Can Mayken disagree here for reasons grounded in her own knowledge, work or values?"
  - "Does Claes receive relation as correction rather than as confirmation?"
  - "Does the scene preserve two centers of agency?"
  - "If alchemical language is removed from the author's notes, does the human relationship still work causally?"

  guardrails:
  - "Conjunctio is an author-side structural function, not mandatory in-world terminology."
  - "Mayken is not a reward, therapist, saint, decoder or missing ingredient."
  - "Claes is not entitled to Mayken because he suffers or completes the Work."
  - "Difference must remain visible after union; sameness would destroy the function of the relationship."
```

---

# SOURCE FILE: `narrative/knowledge_states.yaml`

```yaml
schema_version: 1.2.0
kind: KnowledgeStateRegistry
purpose: Narrative knowledge boundaries extracted from Revision 11 and later explicit author decisions; deterministic candidates feed Lemma but remain human-readable here.
actors:
- entity_id: ENT.PERSON.CLAES
  states:
  - phase: A
    label: end 1563 / early 1564
    earliest: '1563-12-01'
    latest_exclusive: '1564-04-01'
    knows:
    - Dee personally
    - ordinary educational use of his memoriaal and Monas
    - Dee requires graphite rather than ink in the memoriaal while Claes remains his pupil
    does_not_know:
    - the memoriaal sheets already carry the hidden printed readable Brevísima
    - Las Casas project
    - why ink is materially dangerous to the memoriaal carrier
    - that green vitriol can reveal the hidden text
  - phase: C
    label: after 4 October 1564 security break
    earliest: '1564-10-04'
    latest_exclusive: '1566-08-01'
    knows:
    - his own pedagogical objects
    - the graphite-only rule he received from Dee
    does_not_know:
    - that the memoriaal already contains the readable Diets/Brabant Brevísima
    - Las Casas content
    - the material reveal method
  - phase: E
    label: after return to Goes
    earliest: '1566-08-01'
    latest_exclusive: '1568-07-01'
    knows:
    - father shows unusual interest in dangerous books, papers and routes
    does_not_know:
    - complete purpose of that interest
    - hidden Brevísima function of the memoriaal
  - phase: F
    label: Cornelis fall 1568/69
    earliest: '1568-07-01'
    latest_exclusive: '1570-01-01'
    knows:
    - Cornelis' persecution is connected to dangerous networks of books, papers and testimony
    does_not_know:
    - that his memoriaal contains the hidden Brevísima
    - how the apparently blank pages can be developed
  - phase: G
    label: 1570 reveal
    earliest: '1570-01-01'
    latest_exclusive: '1571-01-01'
    learns_in_order:
    - GALLA LEO VIRIDIS can be read as a material cue linking gall/tannin and green vitriol
    - green vitriol can develop the apparently blank memoriaal pages
    - the developed typographic layer was already present in the book since 1564
    - the developed text is ordinary readable Diets/Brabant language, not ciphertext
    - the hidden work is the Brevísima / Las Casas testimony
    - no nomenclator, matrix or cryptographic reconstruction is required
    dramatic_turn:
      at: first clearly readable developed passage identifying the hidden testimony
      from: understand the memoriaal as personal workbook and residue of Dee's discipline
      to: decide what this testimony asks of Claes
- entity_id: ENT.PERSON.CORNELIS
  states:
  - phase: A
    earliest: '1563-12-01'
    latest_exclusive: '1564-04-01'
    knows:
    - dangerous Diets Las Casas text is being protected within the clandestine project
    may_know:
    - Claes' memoriaal is operationally significant
    does_not_know:
    - every detail of Dee's material-security plan
  - phase: C
    earliest: '1564-10-04'
    latest_exclusive: '1568-07-01'
    knows:
    - the political and network risk around prohibited texts has increased
    does_not_know:
    - a cryptographic recovery key, because no such key is required for the memoriaal
    behavior_constraint: May show unusual interest in dangerous books, papers and Claes' objects, but must not act as if a cipher/recovery architecture exists.
  - phase: F
    earliest: '1568-07-01'
    latest_exclusive: '1570-01-01'
    final_transfer_status: no cryptographic Castanea clue is required by canon
- entity_id: ENT.PERSON.JOHN_DEE
  states:
  - phase: B
    earliest: '1564-01-01'
    latest_exclusive: '1564-10-04'
    knows:
    - the memoriaal given before Boom already carries the hidden printed readable Las Casas translation
    - graphite rather than iron-gall ink protects the tannin-loaded pages during Claes' pupil phase
    - green vitriol can later complete the visible iron-tannin colour reaction
    - pedagogical identity Claes assigns to his objects
  - phase: C
    earliest: '1564-10-04'
    knows:
    - 4 October changes political/network risk, not the physical content or a nonexistent cipher key
    note: Direct presence after this point is not required for the material reveal to remain possible.
- entity_id: ENT.PERSON.WILLEM_SILVIUS
  states:
  - phase: A
    earliest: '1563-12-01'
    latest_exclusive: '1564-04-01'
    knows:
    - project
    - translation/production route
    - the readable Brevísima is set and printed on loose memoriaal sheets before binding
    - the first-pass gallnut/tannin + gum-arabic print medium and proof-development procedure
  - phase: B
    earliest: '1564-01-01'
    latest_exclusive: '1564-10-04'
    knows:
    - ordinary type setting, correction and distribution for the readable translation
    - the physical hidden-print carrier already exists before Boom
  - phase: C
    earliest: '1564-10-04'
    knows:
    - the carrier need not be physically reloaded, reciphered or paired with a key
  - phase: G
    earliest: '1570-01-01'
    latest_exclusive: '1571-01-01'
    role: special Zovitius channel may serve as a material cue toward reveal, not as a cipher key
- entity_id: ENT.PERSON.BELOVED
  states:
  - phase: E
    earliest: '1566-08-01'
    latest_exclusive: '1570-01-01'
    may_know:
    - botanical and apothecary materials relevant to tannins, vitriol, paper and controlled handling
    does_not_know:
    - hidden function of Claes' memoriaal
  - phase: G
    earliest: '1570-01-01'
    latest_exclusive: '1571-01-01'
    learns:
    - controlled material development procedure
    - that the memoriaal carries a previously invisible typographic layer
    - that the revealed layer is directly readable language rather than ciphertext
    role:
    - materials
    - weighing and notation
    - controlled development
    - paper/ink observation
    - challenging unsupported elegance
lemma_projection:
  candidate_rules:
  - can_know
  - can_possibly_know
  - knowledge_prerequisite_satisfied
  - knowledge_sequence_valid
  hard_guardrails:
  - No actor may use knowledge before acquisition.
  - Claes may physically possess the hidden readable Las Casas text from early 1564 while remaining ignorant of its existence and purpose.
  - Claes knows no Las Casas purpose before the material reveal reaches readable identity/content recognition.
  - No actor behaves as if a nomenclator, 24x24 matrix or cryptographic key remains necessary for the memoriaal.
```

---

# SOURCE FILE: `canon/DECISIONS_2026-08-13.md`

```markdown
# Canon decisions — 13 August 2026

These are explicit author decisions and outrank conflicting migrated representations.

## DEC.CLAES.BIRTH.2026-08-13 — CANON
Claes Cornelisz Nissepat is born in Goes on **8 December 1542**. The 1545 date in the transformed work edition is migration drift and must be corrected wherever it appears. The 1542 chronology is retained in line with the intended Brevísima framing.

## DEC.CLAES.SINNE.2026-08-13 — CANON
Claes learns to discover the world through the **sinne**: embodied sensory perception develops through recognition, comparison and pattern toward understanding and choice. Fire, flood, death and other losses progressively blunt and constrict this sensory openness. On the road toward Enkhuizen, with his beloved beside him — the apothecary's daughter, whose identity and biography remain open — Claes rediscovers the sinne. Their renewed resonance within himself becomes a catalyst for recovery, deeper understanding, wisdom and increasing inner sovereignty as an alchemist undertaking the Great Work.

The beloved accompanies and catalyses this process but does not perform it for Claes. The Great Work is lived psychological and spiritual transformation, not merely cipher-solving.

## DEC.CLAES.PARADOX.2026-08-13 — CANON
Claes' gift is prolonged, exact observation through the sinne; his shadow is remaining in observation after action is required. Trauma complicates this paradox by dulling the sensory openness on which his gift depends. Maturity therefore means not simply observing less, but recovering sensation, distinguishing what it asks of him, and converting perception into responsible choice.

## DEC.CLAES.NEED.2026-08-13 — CANON
Claes' psychological need is to recover trust in embodied perception and to act without requiring complete certainty. His moral need is to understand that knowledge and perception increase responsibility toward the other. Perception must become discernment, discernment choice, and choice must accept consequence without attempting total control.

## DEC.CLAES.SPIRITUAL_JOURNEY.2026-08-13 — CANON
The movement from **“What is true?”** to **“What does this truth ask of me toward the other?”** is Claes' spiritual journey from matter toward spirituality. Matter is not rejected: senses, bodies, craft, books, plants, fire, water and alchemical operations are the vessel through which he reaches discernment, responsibility, wisdom and sovereignty.

His Great Work is the transmutation of knowledge-as-control into wisdom-in-relation, culminating in the capacity to transmit and release rather than possess.

## Required synchronization
The following migrated records must now be brought into line with these decisions: `claims/STORY_CLAIMS.yaml`, `entities/ENTITIES.yaml`, `storybible/LEMMA_MCKEE_MASTER.md`, relevant `narrative/arcs.yaml`, `narrative/themes.yaml`, age-dependent Narrative Instances, and `review/MIGRATION_REVIEW.yaml`.
```

---

# SOURCE FILE: `canon/DECISIONS_2026-08-14.md`

```markdown
# Canon decisions — 14 August 2026

These decisions close high-value Goes continuity questions after comparison of the transport-register reconstruction, prior Claes research and explicit author choices.

## DEC.CORNELIS.RESIDENCE.GOES.2026-08-14 — childhood family home

**Decision:** the fictional household of Cornelis Nissepat uses the house bought by historical Claes Jacobsz. Nissepat on **20 March 1542** in the older/pre-1594 `Nieuwstraat` as its Goese family home. Claes is born later that year and grows up there until the fire of 18 May 1554.

Historical fact and fiction remain separate:
- historical: Claes Jacopsen Nissepat bought the house on 20 March 1542; street bordered east, Jacob Dierixsen de Bye north/west/south;
- fiction/canon: the buyer makes the house available to Cornelis and his household as their residence.

The family home is **not** automatically Cornelis' brewery, warehouse, salt-business site or Nissepad business location. `RESIDES` and `OPERATES_BUSINESS` remain separate relations.

## DEC.GOES.NIEUWSTRAAT.IDENTITY.2026-08-14 — two Nieuwstraten must remain distinct

**Decision:** the `Nieuwstraat` named in transport acts before 1594 is represented as the **older Nieuwstraat / Oude Nieuwstraat in or by the Armenhoek**, distinct from the planmatige/current Nieuwstraat associated with the city expansion decided in 1594.

Certainty is deliberately split:
- existence of the pre-1594 `Nieuwstraat` toponym: **verified** by transport acts;
- association with the later `Oude Nieuwstraat` / Armenhoek cluster: **supported**;
- exact 1542 street axis: **unknown**.

For Claes' 1542 house the deed topology remains binding: the street is east of the property, so the house lies on the west side of the historical street. No modern cadastral address is invented.

Post-fire RAZE 1748 records prove burned houses at the Hoek van de Nieuwstraat and in the Armenhoek while other Nieuwstraat houses continue to be transferred. The correct historical model is therefore mixed/partial destruction, not a safe zone and not total loss.

## DEC.GOES.REDERIJKERS.MEETINGPLACE.2026-08-14 — Cornelis' meeting environment

**Decision:** Cornelis-era rederijker meetings are staged in the **Zusterhuis**, the former Zwarte-Zusters complex associated with the Singelstraat.

The earlier proposal that the Goese rederijkers already met in Cornelis' period in the handbow guild's Sint-Sebastiaanshof is rejected as a chronological back-projection. The documented Nardusbloem sequence is:
- Zusterhuis through 1626;
- move to the building/hof of the Sint-Sebastiaangilde in 1626.

This decision establishes Cornelis' scene location by following the best-documented old Goese chamber. It does **not** establish that every separately named Goese chamber used the Zusterhuis. The exact named chamber to which fictional Cornelis belongs may still be specified separately if the novel needs it.

## DEC.CLAES.FAMILY_FIRE.1554.2026-08-14 — the household catastrophe

**Decision:** immediately before the fire the family consists of Cornelis, Claes' mother, Claes, a younger brother approximately eighteen months younger than Claes, and an unborn child. The mother is approximately six months pregnant.

On **18 May 1554**:
- the fictional family house in the older Nieuwstraat is destroyed or rendered uninhabitable;
- Claes and Cornelis survive because they are away from the house when the fire reaches the street;
- Claes' mother dies;
- the younger brother dies;
- the unborn child dies with the mother.

The younger brother is placed around **June 1544** rather than several years younger. This makes him a near-age companion and rival: love, quarrels, play, competition and loyalty must be established before the fire. His dramatic contrast with Claes is action versus prolonged observation.

The pregnancy is not a mechanical explanation for the mother's death. Its function is relational and sensory: Claes can know the unborn child by touch and movement before sight, giving an early embodied form to the proposition that something can be real without being visible.

**Historical guardrail:** burned houses in the old Nieuwstraat/Armenhoek environment are documented, but no current source proves destruction of this specific 1542 parcel or identifies these fictional family members as historical victims.

## DEC.CLAES.GRANDFATHER_LINK.2026-08-14 — Claes Jacobsz. as fictional grandfather

**Decision:** historical **Claes Jacobsz. Nissepat** is used in novel canon as Cornelis' father and Claes' paternal grandfather.

Historical fact:
- Claes Jacobsz. Nissepat is documented;
- he bought the older-Nieuwstraat house on 20 March 1542.

Novel canon:
- he is Cornelis' father;
- he is Claes' grandfather;
- he remains story-owner of the 1542 house through the 1554 fire;
- he loses that property asset when the house burns/is rendered unusable;
- despite his own loss, he helps Cornelis sustain Claes' education after the fire.

This genealogy must never be presented as archival proof. It is a deliberate fictional attachment to a historical person.

## DEC.CLAES.POSTFIRE_FATHER_SON.2026-08-14 — surviving together, grieving apart

**Decision:** the 1554 catastrophe does not simply make Claes and Cornelis closer. It also makes them lose each other.

Cornelis remains in Goes because he must rebuild:
- livelihood and business;
- shelter/household infrastructure;
- credit, customers and obligations;
- the financial ability to keep Claes in education.

His father Claes Jacobsz. assists where possible, although he too has lost the 1542 property.

The pre-fire plan to send Claes to **Zierikzee** becomes financially unattainable. **Reimerswaal** becomes the viable route that preserves Claes' education at lower cost. Claes therefore leaves Goes while Cornelis stays.

This gives the same act two simultaneous meanings:
- for Cornelis: *I send him away because I refuse to let the fire take his future as well*;
- for Claes: *everyone is gone, and now my father sends me away too*.

The father-son arc must preserve both truths. Cornelis' continued labour, payments, books and messages are acts of care; physical absence can nevertheless be experienced by Claes as abandonment. Cornelis' later death is therefore also the loss of time they believed they might still recover.

## Chamber chronology guardrail

Do not flatten the four named Goese chambers into one simultaneous institution:
- De Goudtsblome: documented 1540–1543;
- De Clisblome: documented around 1545/1546;
- De Nardusbloem / older Magdalena tradition: active in the mid-sixteenth-century Goese rhetorician landscape;
- De Edele Castanienbloem: documented from 1595 and therefore not a historical Cornelis-era chamber unless deliberately used as an acknowledged fictional back-projection.

These decisions are propagated to Story Claims, family/person/property entities, Narrative Instances, arcs, relationships, the Goes world module and the operating master before merge of PR #5.
```

---

# SOURCE FILE: `canon/DECISIONS_2026-08-15.md`

```markdown
# Canon decisions — 15 August 2026

These decisions process the execution/Reformation material, the memoriaal/Brevísima material, and the later Antwerp/alchemical-process material from the 15 August 2026 research chats. Later decisions explicitly supersede earlier development models where stated.

## DEC.CLAES.EXECUTIONS_REFORMATION_ARC.2026-08-15 — CANON

The novel must process sixteenth-century executions as a structural moral and religious arc in Claes' life, not merely as historical atmosphere.

Claes begins within a Catholic civic understanding of execution: ordinary criminals may die under the ars moriendi script of confession, priestly consolation, cross, repentance, prayer and public compassion. The Reformation breaks that shared death script. Wederdopers and Reformed condemned persons increasingly die as witnesses rather than penitents; spectators become active through encouragement, kissing, psalm-singing, stone throwing, rescue attempts, letters, songs and later martyrology.

This arc must connect to the survival of testimony: bodies can be burned, drowned, displayed or silenced; voices can be blocked by tongschroef or secrecy; therefore testimony must learn to survive through indirect carriers such as letters, relics, hidden writing and books. The Brevísima memoriaal uses chemical concealment rather than a cryptographic cipher.

## DEC.CLAES.CORNELIS_EXECUTION_WITNESS.2026-08-15 — CANON

Claes must be physically present as witness at Cornelis' execution.

This fixes the witness relation and scene function. It does **not** by itself close the exact date, place, formal charge, execution method or degree of public ritual. Those are closed for this authoring branch by `DEC.CORNELIS.DEATH.1569.2026-08-15.REVISED` below.

Cornelis' death must not depend on him carrying `OBJ.MEMORIAAL`. Dee gives Claes the already prepared memoriaal before the journey to Boom in early 1564; it already carries the hidden readable Las Casas translation. The 4 October 1564 security break changes political/network risk, not the physical loading, encoding or keying of the Brevísima into the book.

Cornelis should remain a vulnerable logistical carrier and father, not a protected printer and not necessarily an open preacher. His plausible death model is: routes, vaten, storage, prohibited papers/books/liederen/prenten, dangerous contacts and refusal to give names. His strongest dramatic death-script is protective silence between Catholic ars moriendi and Protestant martyr display.

## DEC.CORNELIS.DEATH.1569.2026-08-15.REVISED — CANON RESOLUTION IN AUTHORING BRANCH

Cornelis' death is resolved for this authoring branch as a fictional but historically disciplined public execution in Antwerp tied to the documented Antwerp book-repression wave of March-November 1569.

This decision supersedes the earlier authoring-branch draft date of **12 March 1569**. That date is rejected as too arbitrary and insufficiently supported. The revised model uses a historically anchored public book-burning day.

### Fixed story resolution

- **First arrestation / warning:** autumn 1567, Antwerp. Cornelis is first arrested or seriously examined in a book/paper/print matter and released on borg or equivalent surety/conditions. This is a story construction modeled on Antwerp book cases that often produced bail, release, pardon or banishment rather than immediate execution.
- **Renewed exposure:** late 1568 through March 1569. Cornelis' name or route resurfaces in the context of clandestine Reformed copy/distribution networks and the March 1569 bookshop visitations.
- **Execution date:** **19 November 1569**.
- **Place:** Antwerp. Cornelis has been held in or by **Het Steen** and is brought into the public market/stadhuis execution-and-book-burning environment on the **Grote Markt**.
- **Historical anchor:** on 19 November 1569 books seized in Antwerp bookshops in March and judged unfit by Leuven deputies are burned publicly on the market from roughly 9 to 12. Some booksellers remain imprisoned. On the same date Haecht also records executions in Antwerp. Cornelis' execution is fictional and must not be presented as a documented addition to Haecht's list.
- **Formal story charge:** after prior arrest/release, renewed logistical complicity in transport, storage and distribution of forbidden, heretical and seditious books, papers, liederen, figures/prints, libels/billets and correspondence between Antwerp, Goes and Zeeland; connection to clandestine copy/distribution routes; refusal under examination to name accomplices, readers, printers, binders, carriers or recipients.
- **Execution method:** public beheading by sword remains the preferred method, but it is justified only by the seditious/network/recidive framing. Simple book possession or book-smuggling alone is not enough.
- **After-ritual:** confiscated papers and/or related books burn separately as public evidence. Cornelis' body is not returned to Claes. Any head/body display is short, punitive and not allowed to become a full martyr cult.
- **Witness:** Claes is physically present in the crowd and sees the execution.
- **Final transfer:** no cryptographic clue is required. If Cornelis receives a final guarded exchange with Claes, its function should be human, relational or testimony-centered rather than the transfer of a key component.

### Rationale

Cornelis is not executed as a protected printer like Plantin or Silvius and not as an open preacher. He is executed as the expendable logistical body of a network: the man whose route, vaten, storage, papers, contacts and silence make otherwise deniable book traffic visible.

The two-step arrest model is required for plausibility. In Antwerp book cases, even serious printers/booksellers could survive through bail, acquittal, pardon or banishment. Cornelis therefore should not be killed at first exposure. He first comes under suspicion, is released under conditions, then becomes fatal in 1569 because he is linked again to seditious/heretical traffic after warning and refuses names.

The 19 November 1569 setting is chosen because it publicly binds book destruction, market/stadhuis space, official judgement and execution culture. It lets Claes witness not only his father's death but the destruction of text as evidence.

Guardrails:

- Do not make Cornelis the author or printer of the hidden Brevísima.
- Do not make `OBJ.MEMORIAAL` the object found on him.
- Do not present 19 November 1569 as an archival execution record for Cornelis Nissepat.
- Do not claim the historical seven offenders executed that day included Cornelis; Cornelis is a fictional insertion into the documented ritual environment.
- Do not make Claes understand the hidden Las Casas function of his memoriaal at the execution.
- Do not make Fabritius alone the legal cause of the 1569 sentence; Fabritius remains the 1564 security-break catalyst, while Cornelis' later fall requires the 1567 warning/arrest, transport traces, March 1569 book-repression exposure, papers, contacts and refusal to name others.
- Keep the sword-death conditional on seditious/network/recidive framing; if future research weakens that framing, reopen execution method.
- Mark this as novel canon/authoring-branch resolution, not archival evidence of a historical Cornelis execution.

## Clarification — Fabritius and the 4 October 1564 security break

Fabritius is the preferred historical candidate for the already canonical `NI.EVENT.SECURITY_BREAK.1564.001` because the date, stones, psalm-singing, public-control failure and Antwerp context fit the existing storybible hinge.

This remains a candidate until `OPEN.SECURITY.LOW_LINK.1564.001` is explicitly closed. Cornelis need not be a stone thrower, need not sing, need not try to rescue Fabritius and need not be arrested in 1564. The fixed story function is that the event makes Cornelis operationally unsafe within clandestine book/paper networks and serves as the adult macro-Nigredo hinge. It does **not** alter, load, recipher or lock/unlock Claes' memoriaal.

## DEC.MEMORIAAL.BREVISIMA_PRINT_GIFT.2026-08-15 — DEPRECATED DEVELOPMENT VERSION

This earlier decision fixed the successful physical breakthrough: the Brevísima is printed on loose sheets with the reconstructed near-invisible gallnut/tannin + gum-arabic medium, bound as Claes' memoriaal, and given by Dee before Boom together with a graphite stift and an ink prohibition.

Its remaining flaw was that it still assumed the Diets/Brabant text had first been encoded and later required a separate key-recovery architecture. That part is superseded by the decision below. The physical print-before-binding process, recipe, Dee handoff and graphite rule are retained.

## DEC.MEMORIAAL.DIRECT_TEXT_NO_CIPHER.2026-08-15 — CANON

The cipher is removed from the Brevísima mechanism.

The reason is structural rather than cosmetic: the cipher was introduced earlier only because printing a whole book in a chemically latent form appeared impracticable. Once the reconstructed tannin/gum movable-type process provides a plausible way to print the entire translation invisibly on loose sheets, the premise that made the cipher necessary disappears. Retaining both chemical concealment and cryptographic concealment would duplicate the same story function.

### Fixed physical and textual production

1. A completed Diets/Brabant translation of the *Brevísima* exists before the hidden print run.
2. Silvius sets **ordinary readable language in ordinary movable type**. He does not set cipher groups, a nomenclator stream or composite key symbols.
3. The clandestine first-pass printing medium contains clear filtered gallnut/tannin extract plus gum arabic, with **no intentional green vitriol/iron salt, soot or visible pigment**.
4. Canonical workshop starting recipe remains:
   - break **2 drachmen good gallnuts** and steep them in **2½ medicinal ounces clear water**;
   - filter through fine linen and take **2 medicinal ounces of the clearest extract**;
   - dissolve **1½ medicinal ounces good gum arabic** in that extract;
   - if the medium runs from the letter, add a little gum; if it is too stiff for clean transfer, temper it with a few drops of clear water.
5. The technical criterion remains the printer's: the medium must be sufficiently `dick ende clemachtich` to stay on the raised type and transfer a thin coherent reactive film, while leaving as little visible tint, gloss and *moet* as possible.
6. The loose sheets are printed recto/verso in correct imposition, dried, folded/gathered and bound as an apparently blank memoriaal. The writing paper **is** the hidden book.
7. A sacrificial proof may still be developed with the working reference **½ drachme green vitriol in 4 medicinal ounces clear water**. The production sheets themselves remain undeveloped.
8. The exact performance remains subject to `OPEN.MATERIAL.WET_TEST.001`; this is story-canon technical reconstruction, not a documented Plantin/Silvius recipe.

### Dee's handoff and graphite layer

Before `NI.CHAPTER.1564.03` (*De Kies Van Boom*), Dee gives Claes:

- `OBJ.MEMORIAAL`, already bound from the invisibly printed readable Brevísima sheets; and
- `OBJ.GRAPHITE_STIFT`.

Dee forbids Claes to write in the memoriaal with ink **for as long as Claes remains his pupil**. Claes uses graphite for notes, diagrams, observations and corrections. He understands the rule pedagogically; he does not know that ordinary iron-gall writing ink could introduce iron into the tannin-loaded pages and disturb or locally activate the hidden print.

The resulting object has two simultaneous layers:

- visible: Claes' own graphite observations;
- latent: Silvius' readable Diets/Brabant Brevísima in tannin/gum type-print.

### Later reveal

Green vitriol completes the visible ink chemistry. Where tannin/gallnut material was deposited by the type, iron-tannin complexes darken and the typographic Brevísima appears.

The revealed letters are already ordinary language. Therefore:

- reveal is **not** decryption;
- `OBJ.LASCASAS_CIPHERTEXT`, the nomenclator, 24×24 matrix, special Dodoens carrier, Primus Index, direct key and merels/Monas/Castanea recovery chain are retired from the Brevísima mechanism;
- no multi-week cryptographic reconstruction is required;
- merels, *Monas*, Dodoens or Castanea may remain elsewhere only where they have independent historical, pedagogical, thematic or character value.

`OBJ.ZOVITIUS_1570_TRIGGER` may remain as a compact material clue through **GALLA LEO VIRIDIS**: it points Claes toward gall/tannin and the Green Lion/green vitriol. It is a cue, not a key.

The dramatic recognition becomes materially immediate: the apparently blank memoriaal was never blank.

## DEC.CORNELIS.ROLE.POORTER_RED_BROUWER.2026-08-15 — DEPRECATED / SUPERSEDED

This earlier branch decision incorrectly fixed Cornelis as **bierbrouwer/biersteker and deken** of De Edele Castanienbloem. It is superseded by `DEC.CORNELIS.ROLE.BIERSTEKER_CASTANIE_OPEN.2026-08-15`.

Retained element: Cornelis is a Goes poorter, participates in beer/book transport logic, belongs to the rederijker network, and must not be turned into a printer.

Rejected elements:

- Cornelis as fixed bierbrouwer / brewery owner;
- Cornelis as fixed deken of De Edele Castanienbloem.

## DEC.CORNELIS.ROLE.BIERSTEKER_CASTANIE_OPEN.2026-08-15 — CANON

Cornelis' canonical role in the Antwerp/boekentransport material is fixed as **Goes poorter, biersteker and member of De Edele Castanienbloem**.

The brewery/brewing infrastructure belongs within the wider family/business context but is **not** fixed as Cornelis' own brewery or as his personal occupation. Whether Cornelis is deken of De Edele Castanienbloem remains **OPEN/onbeslist** and must not be written as fact until explicitly closed.

Cornelis' economic practice gives him routes, beer trade, barrels/kists, storage, freight papers, carts/ships and plausible cover for transported material. His civic and rederijker context gives him trust, symbolic literacy, chamber connections, speech discipline and social standing.

Authoring rule: Cornelis can carry books, papers or sensitive material because beer trade, civic trust and rederijker culture overlap. He does not set type. Zetletters, press rhythm, proofing and typographic expertise belong to Silvius' workshop.

If he transports books for Vesalius/Vaselius, the exact name and source-standardization must be checked later; the active story function is the same: anatomically/humanistically sensitive book material travels between Goes/Zeeland and Antwerp under commercial/rederijker cover.

## DEC.ANTWERP.THREE_VISITS_PROCESS_ARC.2026-08-15 — CANON

Claes' Antwerp formation is organized as three visits rather than by forcing John Dee into the documented space of the 1561 Landjuweel.

1. **1561 Landjuweel:** Claes visits Antwerp through Cornelis' civic/rederijker/book-transport world. Dee is not placed here. Function: the city as theatre; blazoens, chambers, allegory, public performance and concealed meanings. Claes learns that meaning can hide in play and civic spectacle.
2. **1563/1564 Dee/Silvius/Boom:** Claes returns through the transport/book network. Dee and Silvius become active. Function: the city as book/workshop; hidden print, kies, Green Lion, ink, vitriol and material instruction. Claes learns that meaning can hide in matter.
3. **1566 Beeldenstorm:** Claes returns to a city where images and signs are attacked. Function: the city as broken image; symbols become dangerous under religious/political pressure. Claes learns that meaning can cost safety.

The 1566 visit does **not** supersede the current 19 November 1569 Cornelis execution decision. The earlier idea of Cornelis being murdered in the Beeldenstorm is rejected/deprecated by the active authoring-branch death model unless a future explicit decision reopens it.

The three visits may function as a hidden analogue to three initiatory degrees: seeing, working, carrying. This is a structural analogy only, not diegetic freemasonry and not a historical claim about sixteenth-century masonic blue degrees.

## DEC.ALCHEMY.PROCESS_LAYERS.2026-08-15 — CANON

The chemical/alchemical process sequence discussed on 15 August becomes a cross-story process grammar across material, symbolic, moral and spiritual layers.

The canonical reconstructed material chain is:

`kies / pyrite-bearing waste -> weathering/care/digestion -> vitriool-loog / Green Lion -> strong waters -> death/opening of Sol -> red fixation / Red Lion -> Saturn/lead/cupellation-like test`.

This is not a modern recipe and not proof of real lead-to-gold transmutation. Individual technical building blocks are historically/chemically supported by the research discussed in the chat, while the full projectiepoeder chain is an authorial historical-chemical reconstruction. The apparent gold result should remain chemically interpretable as hidden Sol becoming visible through process and assay, not as literal creation of gold from lead.

Narrative rule: these processes must recur at multiple levels:

- rederijkers hide meaning in allegory;
- Cornelis hides books in trade and trust;
- Silvius hides readable text in blank-looking paper;
- Dee teaches that matter hides process;
- green vitriol reveals writing and opens matter;
- Sol dies as visible form and survives as hidden presence;
- Cornelis' silence becomes testimony under pressure;
- Claes' observation becomes responsibility.

The governing prose sequence after Boom is: `De kies van Boom` -> `De loog van Antwerpen` -> `De dood van Sol` -> `De rode massa/Rode Leeuw` -> `Saturnus`. This sequence is authoring architecture; chapter titles may be revised without changing the process order.

## DEC.ALCHEMY.CLAES_LIFELINE_PROJECTIEPOEDER.2026-08-15 — CANON

The alchemical steps toward projectiepoeder must lead Claes' life-line. The process is not confined to workshop scenes. It structures Claes' movement from childhood *sinne*, through fire and loss, rederijker signs, Dee/Silvius material instruction, the Green Lion, the death/opening of Sol, Cornelis' execution and testimony, the memoriaal reveal, adult red fixation and the 1602 Enkhuizen transmutation.

The 1602 Enkhuizen event is the outward projectio of the material line, but it is not the final moral meaning of the story. By and beyond 1602 Claes must learn that the Work is not possession of gold or proof, but the capacity to reveal, transmit, restrain and release hidden meaning responsibly.

`storybible/ALCHEMICAL_CHEMICAL_PROCESS_CHAIN_CLAES_LIFELINE.md` is the governing detailed dossier for this decision.

Guardrails:

- The life-line must keep chemistry, alchemical language, historical reconstruction and story canon separate.
- The process may be chemically interpretable but may not be presented as a real recipe for transmutation.
- The Enkhuizen transmutation should remain materially ambiguous: convincing to early-modern witnesses, interpretable to modern readers as hidden Sol becoming visible through process/test/assay, and decisive for Claes as an ethical/spiritual event.
- The beloved/apothecary-daughter and road-to-Enkhuizen recovery line should support the reopening of Claes' embodied *sinne* and his movement from knowledge-as-control to wisdom-in-relation.

## Required synchronization

These decisions govern:

- `storybible/ANTWERP_THREE_VISITS_ALCHEMICAL_ARC_1561_1569.md`;
- `storybible/ALCHEMICAL_CHEMICAL_PROCESS_CHAIN_CLAES_LIFELINE.md`;
- `storybible/MEMORIAAL_BREVISIMA_PRINT_1564.md`;
- `storybible/MASTER.md` and `storybible/INDEX.md` as navigation/synchronization surfaces;
- `claims/STORY_CLAIMS.yaml`, `objects/OBJECTS.yaml`, `narrative/instances.yaml`, `narrative/knowledge_states.yaml`, `narrative/relationships.yaml`, `narrative/motifs.yaml`, `narrative/themes.yaml`, `narrative/arcs.yaml` and relevant Lemma only in a later downstream synchronization pass.

The dated operating synthesis `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` still requires later regeneration/patching where it contains older carrier/cipher or insufficiently developed alchemical-process wording. Until then this decision file, the active Story Claims and the dedicated focused dossiers outrank stale broad synthesis passages.
```

---

# SOURCE FILE: `canon/DECISIONS_2026-08-16.md`

```markdown
# Canon decisions — 16 August 2026

These decisions refine the alchemical process line and correct Cornelis' rederijker affiliation after the 15 August alchemical-lifeline merge. They are explicit human author decisions and outrank conflicting 15 August wording.

## DEC.CORNELIS.REDERIJKER.NARDUS_CASTANIE_ORIGIN.2026-08-16 — CANON

Cornelis is canonically a **member of the Nardusbloem / older Magdalena-linked Goese rederijker tradition**. The Nardusbloem's mid-sixteenth-century institutional culture remains explicitly Catholic in its documented Maria-Magdalena chapel, dodenmis and requiem obligations.

In novel canon Cornelis also plays a formative role in the **emergence of the Edele Castanienbloem as a reform-minded / protestantiserende splinter current during the confessional polarisation and hagepreek years of the 1560s**. This earlier emergence is deliberate historical fiction grounded in a documentary gap, not a claim that a pre-1595 Castanienbloem is historically attested.

The year **1595 is the earliest surviving source attestation**, not a canonical founding date. The surviving record already names chamber office-holders, but this proves only that an organised chamber existed by then. The novel may therefore place the origin earlier while keeping that earlier chronology explicitly fictional/reconstructed.

The historical 1563 Nardusbloem conflict and reduction in membership may provide background pressure for the split, but the surviving sources do not prove that the conflict was confessional or that the later Castanienbloem directly arose from it. Meertens' later hypothesis of a religious split is historiography, not proof, and his proposed confessional direction is not binding on novel canon.

The Castanienbloem's later 1595–1596 Nissepat resonance remains important: the later documented Nissepat participation functions as an echo of a reform-minded chamber tradition whose fictional origin reaches back to Cornelis' generation. The 1630 merger back into the Nardusbloem remains historical context.

This decision supersedes the chamber-membership part of `DEC.CORNELIS.ROLE.BIERSTEKER_CASTANIE_OPEN.2026-08-15`. It does **not** change the retained facts that Cornelis is a Goes poorter, biersteker, book/material carrier through trusted networks, and not a printer.

Whether Cornelis ever serves as **deken** of the Nardusbloem or of the emerging Castanienbloem remains OPEN and must not be asserted without a later decision.

## DEC.ALCHEMY.GREEN_LION_SOL_CONTINUITY.2026-08-16 — CANON

The alchemical process chain remains canon, but its chemical and symbolic boundaries are sharpened.

1. **Green Lion is operational, not universal.** In Dee's and Claes' working vocabulary, the green vitriol/green copperas in this process may be called the Groene Leeuw because of what it does. The story must not claim that `Groene Leeuw = FeSO4` is a universal historical alchemical definition.
2. **Text reveal is direct.** Green vitriol directly supplies the iron that develops the tannin-loaded memoriaal typography into readable dark text.
3. **Gold opening is indirect.** Green vitriol does not itself directly dissolve Sol. It belongs upstream in Claes' learned family of vitriol/corrosive-water operations. `De dood van Sol` must distinguish the text-reveal reaction from the later compound conditions required to open gold.
4. **Failure before opening.** Claes must encounter the limit of ordinary strong water: a corrosive water that attacks lesser metals does not by that fact open Sol. The process lesson is that greater force is not identical with the right relation of substances.
5. **Material continuity of Sol.** From the first deliberate opening/dissolution of gold through the red fixation and the 1602 assay/projectio, the author's hidden chemical model obeys conservation: the Sol that later appears was already materially present. No stage creates gold from lead and no later stage silently introduces new gold.
6. **Rode Leeuw as carrier of hidden Sol.** The red/dark projectiepoeder matrix canonically carries already-present Sol in a concealed/fixed form. The exact non-gold carrier composition remains OPEN; iron oxides, mercury/antimony/cinnabar associations and other period red-matter possibilities may inform appearance but must not obscure the continuity of the gold-bearing fraction.
7. **Saturn/cupellation is interpretation, not historical Seton protocol.** A lead/cupellation-like assay is the novel's author-side historically disciplined mechanism by which already-present Sol can become visible after projection. It must never be presented as a documented procedure used by Seton in Enkhuizen.
8. **Sensory guardrail.** Do not have Claes taste vitriol or corrosive solutions as a routine diagnostic practice. Use sight, smell-at-distance, stain, crystallisation, sound, heat, texture of safe solids and tool behaviour instead.
9. **Terminology guardrail.** The working chapter title `De loog van Antwerpen` may remain, but technical narration should prefer period-defensible terms such as vitrioolwater, uitloogwater, oplossing or liquor where appropriate instead of treating modern alkaline 'loog' as the chemistry of the vitriol stage.

The process law is therefore:

> What becomes visible was already materially present.

This law applies differently but coherently to Sol, the memoriaal text, testimony, memory and Claes' recovered *sinne*.

## DEC.ENKHUIZEN.SETON_FRAME.1602.2026-08-16 — CANON

The 1602 projectio scene is fictionally anchored to the **retrospective Seton tradition reported by Daniel Georg Morhof in 1673**.

For novel chronology and scene framing:

- location: **Enkhuizen**;
- reported house: that of the sailor **Jacob Hausfsen**;
- date: **13 March 1602**;
- reported time: approximately **the fourth hour after noon** (about 16:00);
- Alexander Seton/Sidonius is the historical-tradition figure around whom the reported projection is framed.

These details are canon as the novel's chosen historical frame, not as contemporaneously verified facts. Morhof writes roughly seventy years later and transmits a chain of testimony involving a gold fragment/plate and the Enkhuizen physician tradition. The story must preserve that retrospective-source status.

The exact furnace choreography, quantities, witnesses beyond those required by the Morhof frame, assay sequence, public/private degree, danger level and immediate moral aftermath remain OPEN. Any cupellation-like explanation remains an authorial reconstruction consistent with `DEC.ALCHEMY.GREEN_LION_SOL_CONTINUITY.2026-08-16`, not a claim about Morhof's or Seton's actual procedure.

## DEC.GOES.CLERGY.MATHIJS_VICE_CUREYT.2026-08-16 — CANON

**Mr. Mathijs Jacopsen/Jacobsen** is the named historical clergy anchor for the Catholic Goese world immediately preceding and entering Claes' birth year. The transport evidence explicitly names him **vice-pastoor** on 14 March 1541 and **`vice-cureyt ter Goes`** on 27 February 1542.

The decisive boundary is chronological: Claes is born on **8 December 1542**, while the recovered proof fixes Mathijs in office on **27 February 1542**. Therefore Mathijs may anchor early-1542 Goese church scenes, but the novel must **not** silently extend his incumbency to Claes' birth date.

The Maria Magdalena connection is retained as a strong contextual identification through the Goese parochial setting and Mathijs' church/kerkhof/choir property network. The 27 February act itself, however, says only `ter Goes`.

The project must not assert as fact that Mathijs was the titular benefice-holder, that he still held office on 8 December 1542, that he baptized Claes, or that his church-area property proves residence.

## DEC.GOES.CLERGY.CLEMENS_VAN_DEN_DALE.2026-08-16 — CANON

**Clemens van den Dale** is a documented later Goese clergy anchor. On **20 March 1564** a Goese transport act explicitly titles him **`licentiaat pastoor Goes`** when he buys the house *de Lombaert* on the north side of the Grote Markt.

His presence belongs to the verified institutional world of Goes in 1564. It does not by itself establish that Claes knows or meets him.

## DEC.GOES.CLERGY.SUCCESSION_BOUNDARY.2026-08-16 — CANON_GUARDRAIL

The exact titular pastor above Mathijs and the complete succession between the recovered Mathijs attestations in 1542 and Clemens van den Dale in 1564 remain unresolved in the present evidence set.

Do not fill the interval **1542–1563** by extending Mathijs or Clemens through plausibility alone. New benefice/collation evidence may refine that interval later without disturbing the fixed February 1542 and March 1564 anchors.

The governing clergy dossier is `storybible/GOES_CLERGY_MATHIJS_CLEMENS_1541_1564.md`; machine-readable synchronization lives in the corresponding source-claim, story-claim, entity and world supplements dated 16 August 2026.

## Required synchronization

These decisions must govern:

- `claims/STORY_CLAIMS.yaml` and active dated Story Claim supplements;
- `entities/ENTITIES.yaml` and active dated entity supplements;
- `objects/OBJECTS.yaml` where object continuity is affected;
- `narrative/instances.yaml`;
- `narrative/knowledge_states.yaml`;
- `narrative/arcs.yaml`;
- `narrative/motifs.yaml`;
- `narrative/themes.yaml`;
- `canon/OPEN_DECISIONS.yaml` and relevant supplements;
- `storybible/ALCHEMICAL_CHEMICAL_PROCESS_CHAIN_CLAES_LIFELINE.md`;
- `storybible/ANTWERP_THREE_VISITS_ALCHEMICAL_ARC_1561_1569.md`;
- `storybible/GOES_CLERGY_MATHIJS_CLEMENS_1541_1564.md` and `narrative/world_goes_clergy_1541_1564.yaml`;
- `storybible/MASTER.md`, `storybible/INDEX.md` and `review/SYNC_STATUS.md` as navigation/operating summaries;
- source/provenance records for the relevant historical evidence bundles.

Historical evidence and novel choice remain separate throughout.
```

---

# SOURCE FILE: `canon/DECISIONS_2026-08-16.yaml`

```yaml
schema_version: 1.0.1
kind: CanonDecisionSupplement
decisions:
- id: DEC.BREVISIMA.ANTWERP_PRINT.1578.2026-08-16
  type: CanonDecision
  status: CANON
  decision: The Brevísima textual mission reaches its public/material culmination in Antwerp in 1578 through printing. By 1602 this textual line is complete and must not be reopened through Alexander Seton or the Enkhuizen projectio.
  affects:
  - ARC.CLAES.MACRO_TRANSMUTATION
  - NI.EVENT.PUBLICATION.1578.001
  - OBJ.LASCASAS_PLAINTEXT
  - DEC.SETON.ENKHUIZEN_ALCHEMICAL_MIRROR.1602.2026-08-16
  fixed:
  - year: 1578
  - place: Antwerp
  - mode: printed publication / print event
  structural_function:
  - '1578 is the projectio of the Word: dangerous testimony is multiplied and released into the world.'
  - 'The later 1602 alchemical projectio answers a different question: what Claes does with material mastery, proof and power.'
  guardrails:
  - Do not make Seton necessary for decoding, revealing, authenticating, printing or recovering the Brevísima.
  - Do not postpone completion of the Brevísima line to Enkhuizen 1602.
  - Exact printer, edition architecture, cover identity, distribution route and surviving-copy logic remain separately evidence-controlled unless already decided elsewhere.

- id: DEC.SETON.ROLE.SEPARATED_FROM_BREVISIMA.2026-08-16
  type: CanonDecision
  status: CANON
  decision: Seton's role is fully separated from the Brevísima and hidden-text line. He belongs exclusively to Claes' late alchemical and existential development.
  structural_parallel:
  - '1578: projectio of the Word — testimony is released through print.'
  - '1602: projectio of Matter — the Rode Leeuw is tested against Saturnus and apparent Sol becomes materially persuasive.'
  - 'after 1602: projectio of the Self — Claes must release ownership, control and the need to possess the Work.'
  seton_function:
  - late mirror and foil
  - external catalyst
  - test of Claes' relationship to mastery and possession
  - warning that technical success attracts coercive power
  - embodiment of the question whether an adept can demonstrate without becoming owner, courtier or weapon
  rejected:
  - Seton as decoder
  - Seton as material reader of the memoriaal
  - Seton as key to vitriol-written text
  - Seton as necessary link in the 1578 print chain
```

---

# SOURCE FILE: `canon/DECISIONS_ALCHEMY_LIFELINE_2026-08-15.yaml`

```yaml
schema_version: 1.3.2
kind: CanonDecisionSupplement
note: 16-Aug Green-Lion/Sol, Enkhuizen-frame and Nardusbloem/Castanien refinement decisions are owned uniquely by canon/DECISIONS_ALCHEMY_REFINEMENT_2026-08-16.yaml.
decisions:
- id: DEC.CORNELIS.ROLE.POORTER_RED_BROUWER.2026-08-15
  type: CanonDecision
  status: DEPRECATED
  superseded_by: DEC.CORNELIS.ROLE.BIERSTEKER_CASTANIE_OPEN.2026-08-15
  decision: Earlier branch wording incorrectly fixed Cornelis as bierbrouwer/biersteker and deken of De Edele Castanienbloem.
  retained:
  - Cornelis is a Goes poorter.
  - Cornelis belongs in beer/book transport logic.
  - Cornelis is part of the rederijker network.
  - Cornelis must not be made a printer.
  rejected:
  - Cornelis as fixed bierbrouwer or brewery owner.
  - Cornelis as fixed deken of De Edele Castanienbloem.

- id: DEC.CORNELIS.ROLE.BIERSTEKER_CASTANIE_OPEN.2026-08-15
  type: CanonDecision
  status: DEPRECATED_IN_PART
  superseded_in_part_by: DEC.CORNELIS.REDERIJKER.NARDUS_CASTANIE_ORIGIN.2026-08-16
  decision: The 15 August decision correctly fixed Cornelis as Goes poorter and biersteker, kept brewery infrastructure in the wider family/business environment and prohibited making him a printer. Its statement that Cornelis is simply a member of De Edele Castanienbloem is superseded.
  retained:
  - Cornelis is a Goes poorter.
  - Cornelis is a biersteker.
  - The family/business environment may include brewery/brewing infrastructure, but Cornelis is not fixed as brewery owner.
  - Book transport may use beer-route, civic and rederijker cover.
  - Cornelis is not a printer and does not perform Silvius' composing-stick, proofing or press work.
  superseded:
  - Cornelis as a straightforward member of De Edele Castanienbloem during his lifetime.
  current_rederijker_state:
  - Cornelis is a member of the Nardusbloem / older Magdalena-linked Goese tradition.
  - In novel canon he plays a formative role in the 1560s emergence of the reform-minded/protestantiserende current that becomes the Edele Castanienbloem.
  - 1595 is the earliest surviving historical attestation, not a canonical founding date.
  - Deken status remains open under OPEN.CORNELIS.REDERIJKER.DEKEN.001.

- id: DEC.ALCHEMY.CLAES_LIFELINE_PROJECTIEPOEDER.2026-08-15
  type: CanonDecision
  status: CANON
  decision: The alchemical steps toward projectiepoeder lead Claes' whole life-line toward and beyond the 1602 Enkhuizen projectio. The process is a cross-layer narrative grammar, not merely a chemistry subplot.
  affects:
  - ARC.CLAES.MACRO_TRANSMUTATION
  - ARC.CLAES.SINNE_RECOVERY
  - THEME.CLAES.SPIRITUAL_JOURNEY
  - MOTIF.ALCHEMY.PROCESS_CHAIN
  - NI.CHAPTER.1564.03
  - NI.CHAPTER.1564.04
  - NI.CHAPTER.1564.05
  - NI.CHAPTER.RED_LION
  - NI.CHAPTER.SATURNUS
  - NI.EVENT.ENKHUIZEN.TRANSMUTATION.1602
  material_chain:
  - kies / pyrite-bearing waste
  - weathering / care / digestion
  - vitrioolwater / Groene Leeuw as an operational process name
  - strong waters and the failure of force alone on Sol
  - death / opening of Sol under the right compound relation
  - materially continuous hidden Sol
  - red fixation / Rode Leeuw carrying already-present Sol
  - Saturn / lead / cupellation-like test
  - projectio / release beyond possession
  guardrails:
  - Keep chemistry, alchemical language, historical reconstruction and story canon separate.
  - Do not present the chain as a real recipe or proof of literal lead-to-gold transmutation.
  - DEC.ALCHEMY.GREEN_LION_SOL_CONTINUITY.2026-08-16 governs Green Lion boundaries and material conservation of Sol.
  - DEC.ENKHUIZEN.SETON_FRAME.1602.2026-08-16 governs the chosen Morhof-derived scene frame.
  - Mayken supports Claes' reopening of embodied sinne and movement from control toward relation and release; she is not a cipher solver.

- id: DEC.ALCHEMY.RED_LION.PROJECTION_POWDER.2026-08-16
  type: CanonDecision
  status: CANON
  decision: Claes' completed projectiepoeder is the Rode Leeuw. It is materially and visually distinct from the earlier Groene Leeuw/vitriol phase. Rode Leeuw and completed projection powder functionally coincide in novel canon without claiming universal historical-alchemical synonymy.
  appearance:
    state: fine heavy powder
    colour_range: deep red to red-brown
    comparisons: [dried blood, red earth, iron rust, burnt ochre]
    constraints:
    - darker and duller than bright vermilion/cinnabar
    - never green
    - never visibly gold-yellow
    - no visible golden glitter is required or desired
  symbolic_distribution:
    Groene_Leeuw:
    - green vitriol/copperas as operational process material
    - revealer/opener upstream
    - digestion/corrosion/disclosure
    Rode_Leeuw:
    - rubedo
    - fixation
    - completed projectiepoeder
    - carrier of already-present hidden Sol
  guardrails:
  - Never describe Claes' final projectiepoeder as green vitriol or as a green powder.
  - Never collapse Groene Leeuw and Rode Leeuw into the same material stage.
  - Do not infer the historical colour or composition of Seton's Enkhuizen powder from Claes' fictional powder.
  - Do not turn this colour canon into a modern operational recipe.

- id: DEC.SETON.ENKHUIZEN_PROJECTIO_ROLE.1602.2026-08-16
  type: CanonDecision
  status: DEPRECATED
  superseded_by: DEC.SETON.ENKHUIZEN_ALCHEMICAL_MIRROR.1602.2026-08-16
  decision: Earlier formulation correctly placed Seton in the 1602 projectio climax but still allowed convergence with hidden-text/revelation motifs, which is obsolete because the Brevísima textual line is completed by the Antwerp 1578 print event.

- id: DEC.SETON.ENKHUIZEN_ALCHEMICAL_MIRROR.1602.2026-08-16
  type: CanonDecision
  status: CANON
  decision: Alexander Seton enters Claes' story only in the late alchemical line. By 1602 the Brevísima textual mission has long been completed through the Antwerp 1578 print event. Seton's function is to confront Claes with projectio, proof, power, possession and release.
  narrative_function:
  - late mirror and foil for Claes
  - external catalyst of Claes' final alchemical transition
  - demonstration that technical success does not settle the moral meaning of the Work
  - embodiment of danger when rulers and patrons treat knowledge as wealth or weapon
  - catalyst from mastery/control toward release beyond possession
  relationship_to_brevisima:
  - none
  - Seton does not decode, reveal, read, print, authenticate or recover the Brevísima.
  - The Brevísima line is complete in Antwerp in 1578.
  relationship_to_existing_mentors:
  - Dee remains an earlier intellectual/material mentor and is not displaced.
  - Seton arrives when Claes technically has little left to be taught; the unresolved task is ethical and existential.
  historical_uncertainty:
  - Seton's exact identity and Scottish family connection remain uncertain.
  - Do not canonize a historical recipe or historical green/red colour for his Enkhuizen projection powder.
```

---

# SOURCE FILE: `canon/DECISIONS_ALCHEMY_REFINEMENT_2026-08-16.yaml`

```yaml
schema_version: 1.0.1
kind: CanonDecisionSupplement
decisions:
- id: DEC.CORNELIS.REDERIJKER.NARDUS_CASTANIE_ORIGIN.2026-08-16
  type: CanonDecision
  status: CANON
  decision: "Cornelis is a member of the Nardusbloem/older Magdalena-linked Goese rederijker tradition and plays a formative fictional role in the emergence of the reform-minded/protestantiserende Edele Castanienbloem during the confessional polarisation and hagepreek years of the 1560s. The 1595 record is the earliest surviving attestation, not a founding date."
  supersedes_in_part:
  - DEC.CORNELIS.ROLE.BIERSTEKER_CASTANIE_OPEN.2026-08-15
  affects:
  - ENT.PERSON.CORNELIS
  - ENT.ORG.GOES.NARDUSBLOEM
  - ENT.ORG.GOES.CASTANIENBLOEM
  - STC.CORNELIS.NARDUSBLOEM.001
  - STC.CASTANIENBLOEM.ORIGIN.1560S.001
  - NI.SEQUENCE.CASTANIENBLOEM_ORIGIN.1560S.001
  - OPEN.CORNELIS.REDERIJKERS.CHAMBER.001
  - OPEN.CORNELIS.REDERIJKER.DEKEN.001
  guardrails:
  - "Historical evidence supports the Nardusbloem's Catholic institutional profile in 1563 and the Castanienbloem's first surviving attestation in 1595; it does not prove the novel's 1560s Protestant split."
  - Do not call 1595 the founding year.
  - Cornelis' deken status remains open.
  - Retain Cornelis as poorter and biersteker; do not make him a printer or brewery owner.
- id: DEC.ALCHEMY.GREEN_LION_SOL_CONTINUITY.2026-08-16
  type: CanonDecision
  status: CANON
  decision: "The Green Lion is Dee/Claes' operational name for green vitriol in this process rather than a universal alchemical identity; green vitriol directly develops the tannin memoriaal but does not directly dissolve gold; the Sol that later reappears remains materially continuous through opening, red fixation, Saturn and assay."
  affects:
  - STC.ALCHEMY.GREEN_LION.OPERATIONAL.001
  - STC.ALCHEMY.STRONG_WATER.FAILURE.001
  - STC.ALCHEMY.SOL.CONTINUITY.001
  - STC.ALCHEMY.CUPELLATION.INTERPRETATION.001
  - OBJ.GREEN_VITRIOL
  - OBJ.RED_LION_PROJECTIEPOEDER
  - OBJ.SOL_GOLD_FRACTION
  - ARC.CLAES.MACRO_TRANSMUTATION
  - MOTIF.ALCHEMY.PROCESS_CHAIN
  - MOTIF.HIDDEN_PRESENCE
  guardrails:
  - No real lead-to-gold creation.
  - No universal claim Green Lion equals FeSO4.
  - No claim that Seton historically used the novel's cupellation-like mechanism.
  - Exact non-gold carrier composition of the red matrix remains open.
  - Avoid tasting vitriol/corrosive liquors as routine sensory diagnosis.
  - "Prefer vitrioolwater/uitloogwater/oplossing in technical description; the chapter title De loog van Antwerpen may remain."
- id: DEC.ENKHUIZEN.SETON_FRAME.1602.2026-08-16
  type: CanonDecision
  status: CANON
  decision: "The novel anchors the 1602 projectio scene to Morhof's retrospective Seton tradition: Enkhuizen, the house of sailor Jacob Hausfsen, 13 March 1602, approximately the fourth hour after noon. These are chosen story-frame facts sourced from a 1673 retrospective account, not contemporaneously verified event facts."
  affects:
  - STC.ENKHUIZEN.SETON.FRAME.1602.001
  - ENT.PERSON.ALEXANDER_SETON
  - ENT.PERSON.JACOB_HAUSFSEN
  - NI.EVENT.ENKHUIZEN.TRANSMUTATION.1602
  - OPEN.ALCHEMY.ENKHUIZEN_1602.EVENT_DESIGN.001
  guardrails:
  - Preserve Morhof's retrospective transmission status.
  - Exact assay choreography, additional witnesses, quantities, danger and immediate moral aftermath remain open.
  - A cupellation-like explanation is authorial reconstruction, not Morhof/Seton procedure.
```

---

# SOURCE FILE: `canon/DECISIONS_BEER_NETWORK_2026-08-16.yaml`

```yaml
schema_version: 1.0.0
kind: CanonDecisionRegistryExtension
decisions:
- id: DEC.NISSEPAT.BREWERY.FAMILY_NETWORK.2026-08-16
  type: CanonDecision
  status: CANON
  decision: >-
    In novel canon the Nissepad brewery is a business/property environment within the wider Nissepat family network, not the personal brewery of Cornelis. Cornelis is a biersteker and merchant-distributor: he is commercially connected to beer made within the family network, receives or obtains casked beer, checks condition and quantity, arranges storage, accounts and transport, and moves beer into Goes for sale and onward distribution. He is not silently made the brewer, recipe-maker or sole legal owner of the brewery.
  affects:
  - ENT.PERSON.CORNELIS
  - ENT.LOC.NISSEPAD
  - ENT.PROP.GOES.NISSEPAD.BREWERY_1577
  - WORLD.NISSEPAT_BEER_NETWORK
  - WORLD.GOES_LIVING_CITY
  - REL.CORNELIS.NISSEPAT_BREWERY
  rationale: >-
    This separates production, family property, distribution and retail. It preserves the documented later Nissepad brewery as a historical anchor while treating the earlier family connection and Cornelis' commercial link as explicit novel canon rather than archival proof. It also gives Cornelis' established biersteker role a concrete spatial and economic function without turning him into a brewer.
  evidence_boundary:
  - The documented Nissepad brewery and its equipment are historical anchors from later sixteenth-century acts.
  - Historical ownership of that documented brewery by Cornelis is not established.
  - The wider-family ownership/business connection before Cornelis' death is novel canon.
  - The exact individual family owner, share structure and contractual relation to Cornelis remain unspecified unless separately decided.

- id: DEC.CORNELIS.BEER.DISTRIBUTION_CHAIN.2026-08-16
  type: CanonDecision
  status: CANON
  decision: >-
    Cornelis' beer trade is staged as a recurring goods-flow from the Nissepad family brewery environment toward Goes and, where a scene requires and historical infrastructure permits, onward from Goes to urban customers or wider regional/shipping distribution. The canonical scene chain is production at Nissepad -> casking -> overland movement toward Goes -> receipt/storage/inspection/accounting by or through Cornelis -> delivery to tappers, innkeepers, households or other buyers -> optional onward movement through Goese commercial and harbour networks.
  affects:
  - ENT.PERSON.CORNELIS
  - WORLD.NISSEPAT_BEER_NETWORK
  - WORLD.GOES_LIVING_CITY
  - ENT.LOC.GOES
  - ENT.LOC.GOES.NISSEPAD_CORRIDOR
  - ENT.LOC.GOES.GANZEPOORT
  - ENT.LOC.GOES.VOORSTAD
  - ENT.LOC.GOES.HAVEN
  rationale: >-
    The distribution chain converts Cornelis' abstract occupational label into repeatable scene logic and makes Goes function as a living commercial node. The route is a story model constrained by historical topography and the transferable biersteker role; it is not evidence that every load followed one fixed path or that all beer was exported.
  guardrails:
  - Do not collapse brewing, biersteken/distribution, tapping and shipping into one occupation.
  - Do not state that Cornelis personally brewed a batch merely because it came from the family brewery.
  - Do not imply that every cask went through the harbour; local Goese sale remains a normal endpoint.
  - Do not assign exact volumes, prices, beer names, recipes, ABV, hopping rates or seasonal schedules without specific evidence.
  - Do not use the earlier six-style beer taxonomy as a canonical Nissepat product list.
```

---

# SOURCE FILE: `canon/DECISIONS_CONCOCTIONIST_MOTIF_2026-08-16.yaml`

```yaml
schema_version: 1.0.0
kind: CanonDecisionRegistryExtension
decisions:
- id: DEC.DEE.CONCOCTIONIST.MOTIF.2026-08-16
  type: CanonDecision
  status: CANON
  decision: >-
    During Claes' first encounter with John Dee in the 1563 Antwerp formation, Dee makes a learned, deliberately inaccurate joke about Cornelis' occupation as biersteker by rendering it into the semantic field of concoction or compounding. The joke is not a correct translation and should register as an amused over-intellectualization of a practical beer trade. The author-side label for this recurring callback is 'concoctionist'.
  affects:
  - ENT.PERSON.CORNELIS
  - ENT.PERSON.CLAES
  - MOTIF.CONCOCTIONIST
  rationale: >-
    The joke begins as characterization of Dee and Cornelis but later acquires thematic accuracy: Cornelis combines routes, casks, credit, people and trust; Mayken is materially closest to literal medicinal/apothecary compounding; Claes eventually learns to work through proportion, relation and transformation rather than force. The callback therefore connects beer trade, apothecary practice, alchemy and mature relational knowledge without collapsing those domains into each other.
  guardrails:
  - "'Concoctionist' is an author-side motif label. Do not require Dee to utter that exact English noun unless a period attestation is separately established."
  - "Dee's in-scene wording may use a period-safer learned paraphrase around concoct/concocter/compounding, but the final dialogue wording remains a scene-level writing choice."
  - 'The joke must remain visibly inaccurate as a translation of biersteker.'
  - 'Do not make Cornelis an apothecary, physician or alchemist because of the joke.'
  - 'Do not make Mayken merely the literal fulfillment of a male joke; her apothecary competence is independent and precedes any later callback.'
  - 'Do not turn the motif into explanatory foreshadowing; its later meaning should emerge retrospectively.'
```

---

# SOURCE FILE: `canon/DECISIONS_GOES_CLERGY_2026-08-16.yaml`

```yaml
schema_version: 1.0.0
kind: CanonDecisionSupplement
decisions:
- id: DEC.GOES.CLERGY.MATHIJS_VICE_CUREYT.2026-08-16
  type: CanonDecision
  status: CANON
  decision: >-
    Mr. Mathijs Jacopsen/Jacobsen is the canonical named historical clergy anchor for the Catholic Goese church world immediately preceding and entering Claes' birth year. He is documented as vice-pastoor on 14 March 1541 and as `vice-cureyt ter Goes` on 27 February 1542.
  historical_basis:
  - SC.HIST.GOES.CLERGY.MATHIJS.VICE_PASTOOR_1541.001
  - SC.HIST.GOES.CLERGY.MATHIJS.VICE_CUREYT_1542.001
  - SC.HIST.GOES.CLERGY.MATHIJS.CHURCH_PROPERTY_1541_1542.001
  story_function: >-
    He may be used as the real priestly face of the Goese Catholic parish environment for scenes whose chronology fits the attested period, rather than inventing an anonymous priest where a documented person is available.
  fixed_boundaries:
  - The project may associate his function with the Maria Magdalena parish/church context, but must preserve that the decisive 27 February 1542 act itself says only `ter Goes`.
  - Mathijs is not proven to be the titular benefice-holder; the evidence explicitly supports a vice-cureit / deputy cure-of-souls role.
  - Mathijs is not proven to still hold the office on 8 December 1542, Claes' canonical birth date.
  - Mathijs is not proven to have baptized Claes.
  - Property by the kerkhof/choir does not prove residence.

- id: DEC.GOES.CLERGY.CLEMENS_VAN_DEN_DALE.2026-08-16
  type: CanonDecision
  status: CANON
  decision: >-
    Clemens van den Dale is retained as a documented later Goese clergy anchor because the 20 March 1564 transport act explicitly titles him `licentiaat pastoor Goes`.
  historical_basis:
  - SC.HIST.GOES.CLERGY.CLEMENS.PASTOOR_1564.001
  story_function: >-
    He belongs to the verified Goese institutional world of 1564; his existence does not automatically create a scene or a personal relationship with Claes.

- id: DEC.GOES.CLERGY.SUCCESSION_BOUNDARY.2026-08-16
  type: CanonDecision
  status: CANON_GUARDRAIL
  decision: >-
    The exact titular pastor above Mathijs and the complete Goese clergy succession from the recovered 1542 Mathijs attestations to Clemens van den Dale in 1564 remain historically unresolved in the present evidence set.
  evidence_basis:
  - SC.HIST.GOES.CLERGY.SUCCESSION_1542_1563.001
  guardrails:
  - Do not fill 1542–1563 with an invented continuous incumbency for Mathijs or Clemens.
  - Do not infer a December 1542 office-holder from a February 1542 act.
  - New benefice/collation evidence may refine this chronology without disturbing the established February 1542 and March 1564 anchors.
```

---

# SOURCE FILE: `canon/DECISIONS_HOUSE_OF_LOVE_NETWORK_2026-08-16.yaml`

```yaml
schema_version: 1.0.0
kind: CanonDecisionRegistryExtension
decisions:
- id: DEC.CORNELIS.HOUSE_OF_LOVE.ENTRY_NETWORK.2026-08-16
  type: CanonDecision
  status: CANON
  decision: >-
    Cornelis enters the Familist world through the social trust created by his beer and cask trade. In novel canon a trusted commercial relation with Ghysbrecht/Gijsbrecht, an Antwerp cooper with Goese property interests, opens a social path to Adriaan Dens. Dens is the first person Cornelis knowingly recognizes as belonging to H.N.'s circle and connects him onward with Hendrik Jansen van Barrefelt, who deepens the contact. By approximately 1552-1553 Cornelis is treated in the story as belonging to the Huis der Liefde while remaining resident in Goes.
  affects:
  - ENT.PERSON.CORNELIS
  - WORLD.NISSEPAT_BEER_NETWORK
  - ENT.NETWORK.HOUSE_OF_LOVE_TRANSLOCAL
  - REL.CORNELIS.GHYSBRECHT
  - REL.CORNELIS.ADRIAAN_DENS
  - REL.CORNELIS.BARREFELT
  rationale: >-
    This makes Cornelis' religious network emerge from his already-canonical occupation instead of from a coincidental meeting with a famous printer. It preserves the material and social logic of trust: barrels, credit, repeated transactions and Antwerp travel precede confidential religious access.
  evidence_boundary:
  - Ghysbrecht/Gijsbrecht the Antwerp cooper and his Goese property interests are historical archival anchors.
  - The identification of the 1551 and 1554 name forms as the same man is strongly supported by name, occupation, origin and house-name continuity but remains an inference.
  - There is no evidence that Ghysbrecht was a Familist or personally knew Adriaan Dens.
  - The bridge Ghysbrecht -> Dens and Cornelis' participation in it are explicit novel reconstruction.
  - Adriaan Dens and Barrefelt are historical Familist-network actors; Cornelis' meetings with them are novel canon.

- id: DEC.CORNELIS.HOUSE_OF_LOVE.PRE_FIRE_AFFILIATION.2026-08-16
  type: CanonDecision
  status: CANON
  decision: >-
    Cornelis' Familist/Huis der Liefde affiliation precedes the Goes fire of 18 May 1554. The fire tests, strains and deepens an already existing conviction; it does not cause his conversion and must not be written as a simple grief-to-sect origin story.
  affects:
  - ENT.PERSON.CORNELIS
  - Goes_fire_18_May_1554
  - storybible/FAMILY_CLAES_1542_1554.md
  guardrails:
  - Cornelis must not discover the Huis der Liefde only because Tanneken, Jan and the unborn child die.
  - The 1554 catastrophe may alter how he understands love, suffering, providence, secrecy and responsibility without creating the affiliation ex nihilo.

- id: DEC.CORNELIS.HOUSE_OF_LOVE.OUTWARD_CONFORMITY.2026-08-16
  type: CanonDecision
  status: CANON
  decision: >-
    Cornelis can belong to the translocal Huis der Liefde while continuing to live in Goes and outwardly participating in the Catholic civic and religious world. No separate Goese Familist congregation, meetinghouse or public confession is required. His affiliation is carried by trusted persons, correspondence, books and travel rather than by an invented local institutional church.
  affects:
  - ENT.PERSON.CORNELIS
  - ENT.NETWORK.HOUSE_OF_LOVE_TRANSLOCAL
  - WORLD.GOES_LIVING_CITY
  guardrails:
  - Do not make Cornelis an open Calvinist or Anabaptist preacher merely because he is Familist.
  - Do not invent a formal Goese Familist congregation without separate evidence or author decision.
  - Do not treat outward Catholic practice as proof that the inward/network affiliation is impossible.

- id: DEC.CORNELIS.HOUSE_OF_LOVE.PLANTIN_LATER_NODE.2026-08-16
  type: CanonDecision
  status: CANON
  decision: >-
    Christophe Plantin is a later print and distribution node in Cornelis' Antwerp network, not Cornelis' initial converter or first doorway into the Huis der Liefde. Cornelis is already Familist in novel canon before Plantin becomes narratively important to him. The story may use Plantin's documented relationship with the Niclaes/Barrefelt milieu while preserving historiographical caution about reducing Plantin to a simple, permanently fixed sectarian label.
  affects:
  - ENT.PERSON.CORNELIS
  - ENT.HIST.PERSON.CHRISTOPHE_PLANTIN
  - REL.CORNELIS.PLANTIN
  guardrails:
  - Do not stage a first-conversion scene in Plantin's shop.
  - Do not make Plantin the sole cause of Cornelis' clandestine book network.
  - Do not present disputed degrees of Plantin's Familist adherence as simpler than the evidence permits.

- id: DEC.CORNELIS.HOUSE_OF_LOVE.LOGISTICS_TO_BOOK_ROUTE.2026-08-16
  type: CanonDecision
  status: CANON
  decision: >-
    Cornelis' movement from beer distribution into clandestine book and paper logistics is a development of the same competencies: casks, storage, accounts, credit, route knowledge, repeated carriers, discretion and trust. This continuity helps explain his later vulnerability in the 1567-1569 Antwerp book/paper case, but it does not by itself resolve the separate exact low-level security trigger of 4 October 1564.
  affects:
  - ENT.PERSON.CORNELIS
  - WORLD.NISSEPAT_BEER_NETWORK
  - REL.CORNELIS.BOOK_ROUTE
  - storybible/CORNELIS_EXECUTION_1569.md
  guardrails:
  - Do not infer that forbidden books were literally hidden inside beer casks unless a separate scene decision establishes it.
  - Similar logistics does not mean identical cargo, route or carrier on every journey.
  - Preserve OPEN.SECURITY.LOW_LINK.1564.001 unless separately resolved.
```

---

# SOURCE FILE: `canon/DECISIONS_MILITARY_DRILL_2026-08-16.yaml`

```yaml
schema_version: 1.0.0
kind: CanonDecisionSupplement
decisions:
- id: DEC.GOES.MILITARY.TRANSITION.NOT_INSTANT.2026-08-16
  type: CanonDecision
  status: CANON
  decision: >-
    Goes' 1577 satisfactie is treated as the political beginning of a military-institutional transition, not as an instantaneous conversion from Habsburg/royalist military practice to the mature Mauritian drill later codified by De Gheyn in 1607.
  affects:
    - HIST.GOES.MILITARY_TRANSITION.1550_1607
    - ENT.ORG.GOES.CIVIC_SCHUTTERIJ
    - ENT.ORG.GOES.GARRISON
  fixed:
    pre_1577: royal_or_habsburg_political_military_sphere
    1577: negotiated_transition_anchor
    1607: mature_states_drill_reference_point
  guardrails:
    - Do not make all Goese armed men switch drill, allegiance, vocabulary and organisation on one date.
    - Distinguish civic schutterij, local garrison and States field army.
    - Check scene year before selecting drill vocabulary or military allegiance.

- id: DEC.DEGHEYN.GOES.MODEL_STATUS.2026-08-16
  type: CanonDecision
  status: CANON_GUARDRAIL
  decision: >-
    De Gheyn's Wapenhandelinghe may be used as a primary model for the mature States drill world around 1607, including scenes relevant to late-life Claes, but the project does not claim that the engraved soldiers are Goese/Zeeuwse troops or that Goes was a model garrison, proving ground or source of De Gheyn's models.
  supported:
    - 42-step roer/schutten sequence
    - 43-step musquetier sequence
    - 32-step spiesdrager sequence
    - numbered image-to-text correspondence
    - explicit ordered words of command
    - safety-conscious muzzle, match and pan handling
  hypothesis_allowed_but_not_fact:
    - >-
      Goes' later incorporation may have meant that soldiers there encountered a relatively mature version of States drill rather than the earliest experimental forms.
  rejected_as_fact_without_new_evidence:
    - De Gheyn depicted soldiers from Goes
    - De Gheyn visited Goes to select military models
    - Goes was the definitive training centre for all States troops
    - Goese drill directly generated the 1607 sequence

- id: DEC.DEGHEYN.COMMAND_LANGUAGE.2026-08-16
  type: CanonDecision
  status: CANON_GUARDRAIL
  decision: >-
    When De Gheyn drill is represented, use the historical command phrases as the verbal orders and treat the figure numbers primarily as the book's correspondence/index system. Do not routinely make officers shout 'Ten eerste', 'Ten achtste' or other figure numbers as if that is proven operational command practice.
  source_claims:
    - SC.HIST.DEGHEYN.DRILL.NUMBERED_COMMAND_SYSTEM.001
    - SC.HIST.DEGHEYN.COMMAND_WORDS.NOT_NUMBERS.001
  rejected:
    - deriving 'Geeft acht' from figure 8
    - treating figure 8 as an attention command
  figure_8_roer:
    dutch_command: "U lont versoect."
    english_1607: "Try your match."
    function: check_and_adjust_the_match

- id: DEC.DEGHEYN.PROCESS_ORDER.2026-08-16
  type: CanonDecision
  status: CANON_GUARDRAIL
  decision: >-
    Scenes based specifically on De Gheyn must respect his process logic: the depicted sequence begins from a prepared/loaded firearm, moves through match preparation, presentation and firing, then pan safety/priming, main-barrel reloading and return to readiness. A generic modern summary of muzzle-loading must not silently replace this source-specific order.
  material_details:
    - separate small priming/touch-powder flask for the pan
    - main flask or measured charges for the barrel load
    - match handled, blown, cocked and tested before presentation
    - muzzle-up safety is a repeated general command principle
  source_claims:
    - SC.HIST.DEGHEYN.FIRE_RELOAD_CYCLE.001
    - SC.HIST.DEGHEYN.PRIMING_FLASK.001

- id: DEC.DEGHEYN.THEMATIC.MIRROR.2026-08-16
  type: CanonDecision
  status: CANON_STORY_FUNCTION
  decision: >-
    De Gheyn's 1607 drill may function as a late-life thematic mirror for Claes: embodied expertise is decomposed into image, word, number and repeatable procedure. This parallels the novel's wider concern with making hidden or tacit processes legible through print, cryptography, alchemy and disciplined perception.
  structural_axis:
    old_world: knowledge_resides_in_experienced_body_and_local_practice
    transitional_world: practice_is_analysed_and_standardised
    printed_world: knowledge_is_externalised_into_image_word_number_and_command
  guardrails:
    - This is a narrative/thematic use, not a claim that Claes influenced De Gheyn.
    - Do not invent personal contact between Claes and Jacob de Gheyn II unless separately decided.
```

---

# SOURCE FILE: `canon/DECISIONS_RESOLUTIONS_2026-08-16.yaml`

```yaml
schema_version: 1.0.0
kind: CanonDecisionSupplement
decisions:
- id: DEC.CLAES.BELOVED.MAYKEN_LAMPERT.2026-08-14
  type: CanonDecision
  status: CANON
  recovered_from: author-approved prior branch PR-7 and synchronized to current no-cipher canon on 2026-08-16
  decision: Claes' beloved is Mayken Adriaensdr. Lampert, a fictional Goese woman born approximately 1546. In novel canon she is daughter of Adriaen Jacobsz. Lampert and granddaughter of the older Jacob/Jacop Lampart/Lambert apothecary household. Her independent competence lies in materia medica, practical preparation, botanical and sensory judgement, measurement, ordinary book use and error control.
  affects:
  - ENT.PERSON.BELOVED
  - ENT.PERSON.ADRIAEN_JACOBSZ_LAMPERT
  - ENT.PERSON.JACOB_LAMPART_APOTHECARY
  - STC.CLAES.BELOVED.MAYKEN_LAMPERT.001
  - STC.MAYKEN.LAMPERT.FAMILY_LINK.001
  - STC.MAYKEN.FIRE_MEMORY.1554.001
  - STC.MAYKEN.APOTHECARY_EXPERTISE.001
  - STC.MAYKEN.MEMORIAAL_REVEAL_ROLE.1570.001
  - STC.CLAES.MAYKEN.RELATIONSHIP.001
  - REL.CLAES.BELOVED
  guardrails:
  - Mayken is not a historically recovered daughter.
  - Adriaen Jacopsen apteker equals Adriaen Jacopsen Lampert is supported, not literally proved in one current act.
  - Jacob-to-Adriaen fatherhood is supported historical reconstruction adopted as novel genealogy, not archival proof.
  - The 1543 Mayken wife of Jacop Lampart supports the name environment only; it does not prove a grandmother or naming chain.
  - Mayken's mother remains open/fictional.
  - Under DEC.MEMORIAAL.DIRECT_TEXT_NO_CIPHER.2026-08-15 Mayken is not a cipher, nomenclator or special-Dodoens key-holder; she may assist material reveal, reading, observation and contradiction.

- id: DEC.CORNELIS.DEATH.1569.2026-08-15.REVISED
  type: CanonDecision
  status: CANON
  synchronization_note: This decision was already active in the execution/Reformation decision layer; this supplement makes its precedence over stale working-window records explicit.
  decision: Cornelis' death is a fictional but historically disciplined public execution in Antwerp on 19 November 1569, tied to the documented book-repression and public book-burning environment. Claes physically witnesses it.
  fixed_story_resolution:
    first_arrest_warning: autumn 1567 in Antwerp; released on borg or equivalent conditions
    renewed_exposure: late 1568 through March 1569 through clandestine book/paper traffic and book-repression traces
    execution_date: '1569-11-19'
    place: Antwerp Grote Markt / stadhuis execution-and-book-burning environment, after detention in or by Het Steen
    charge: renewed logistical complicity in forbidden/heretical/seditious books, papers, songs, prints, libels and correspondence plus refusal to name accomplices or recipients
    preferred_execution_method: public beheading by sword, conditional on seditious/network/recidive framing
    witness: Claes is physically present
    after_ritual: related papers/books may burn separately; Cornelis' body is not returned to Claes
  supersedes_story_working_state:
  - STC.CORNELIS.DEATH.WORK.001
  guardrails:
  - Cornelis is not presented as a documented historical victim on 19 November 1569.
  - Do not claim Haecht lists Cornelis among the historical offenders.
  - Cornelis is not a protected printer, open preacher or author of the hidden Brevísima.
  - Cornelis does not carry OBJ.MEMORIAAL at his execution.
  - Simple book possession or smuggling alone is insufficient; the recidive/network/seditious framing and refusal to give names are required.
  - Any final father-son exchange is human/testimony-centered, not cryptographic key transfer.
```

---

# SOURCE FILE: `canon/DECISIONS_ROSE_JOURNEY_2026-08-16.yaml`

```yaml
schema_version: 1.0.0
kind: CanonDecisionSupplement
decisions:
- id: DEC.CLAES.ROSE_JOURNEY.2026-08-16
  type: CanonDecision
  status: CANON
  decision: "The later journey toward Enkhuizen carries an author-side rose motif that moves from white through pale pink to deeper pink/red: faith/trust at departure, hope while travelling, and love as relation and concrete responsibility toward another person. The motif is experienced through landscape, plant recognition, smell, colour, touch, preparation and action; characters do not explain the symbolic scheme in prose."
  affects:
  - ARC.CLAES.SINNE_RECOVERY
  - ARC.CLAES.LIFE
  - ARC.MAYKEN.LIFE
  - REL.CLAES.BELOVED.RECOVERY
  - REL.CLAES.MAYKEN.CONJUNCTIO
  - MOTIF.ROSES.FIDES_SPES_CARITAS
  principles:
  - "White / Rosa pimpinellifolia is the preferred authorial image for faith/trust and coastal departure where historically and ecologically plausible."
  - "Pale pink / Rosa canina is the preferred travelling image for hope along hedges, dikes and waysides where historically and ecologically plausible."
  - "Deeper pink / Rosa rubiginosa may carry the movement toward human nearness and love where historically and ecologically plausible."
  - "Rosa gallica officinalis functions not as a fourth abstract virtue but as love becoming material care: cultivated materia medica, preparation, judgement and service to damaged bodies."
  - "The rose sequence must serve Claes' sinne pattern: sensation -> recognition -> comparison -> pattern -> understanding -> choice."
  - "The culmination of the motif is caritas as action toward another person, not merely romantic completion."
  guardrails:
  - "Do not state in narration that the flowers 'mean' faith, hope or love unless a historically plausible character actually makes such a devotional association."
  - "Do not force all three species into every stage of the route; ecology, season and route take precedence over symbolic neatness."
  - "Do not present Rosa gallica officinalis as a miracle cure."
  - "Do not claim that West-Friesland lacked competent apothecaries or distillation unless separately evidenced."
  - "Do not claim that severe smoke-inhalation injury was effectively cured by rose preparations."
  - "Any specific wild or naturalised occurrence of Rosa gallica officinalis in West-Friesland or Wieringen in 1602 remains evidence-dependent and may not be asserted as fact without a local source."

- id: DEC.MAYKEN.ROSE_MATERIA_MEDICA.2026-08-16
  type: CanonDecision
  status: CANON
  decision: "Mayken's established materia-medica competence may be concretely dramatized through historical rose preparations, especially Rosa gallica/officinalis, provided her practice remains bounded by sixteenth-century knowledge and source-supported uses. Her contribution is recognition, selection, preparation, measurement, observation and care; she is neither miraculous healer nor auxiliary to Claes' inner arc."
  affects:
  - ENT.PERSON.BELOVED
  - ARC.MAYKEN.LIFE
  - REL.CLAES.BELOVED.RECOVERY
  - MOTIF.ROSES.FIDES_SPES_CARITAS
  guardrails:
  - "Keep Mayken an acting subject with her own judgement, objective and limits."
  - "Separate historically attested rose preparations from modern pharmacological claims."
  - "Where treatment outcome matters dramatically, preserve uncertainty, infection risk, scar formation, pain and the limits of early-modern care."

- id: DEC.NORTH_HOLLAND.FIRE_CARE_HINGE.2026-08-16
  type: CanonDecision
  status: PROPOSED
  decision: "A late northern scene may culminate the rose motif by confronting Claes and Mayken with people suffering burns or fire-related injury, allowing Mayken's material knowledge and Claes' recovered capacity to perceive-and-act to become caritas toward strangers or community members. The exact fire, date, location, victims and clinical severity remain open pending selection of a documented event that fits the established route and chronology."
  affects:
  - NI.OPEN.NORTH_HOLLAND.FIRE_CARE
  - ARC.CLAES.SINNE_RECOVERY
  - ARC.MAYKEN.LIFE
  - REL.CLAES.MAYKEN.CONJUNCTIO
  - MOTIF.ROSES.FIDES_SPES_CARITAS
  guardrails:
  - "Do not invent a major Hoorn fire in 1572."
  - "Do not use the destruction of Egmond Abbey as a simple 7 June 1573 abbey-burning event; current project evidence distinguishes systematic demolition of the abbey from documented burning of other Egmond buildings and leaves later fire questions separate."
  - "The scene must not imply that rose therapy alone determines survival."
```

---

# SOURCE FILE: `canon/DECISIONS_STORY_PROJECTION_2026-08-16.yaml`

```yaml
schema_version: 1.0.0
kind: CanonDecisionSupplement
decisions:
- id: DEC.CLAES.GREAT_WORK.AUTHORIAL_ARCHITECTURE.2026-08-16
  type: CanonDecision
  status: CANON
  decision: "The deep author-side architecture of Claes' Great Work is Status Prima -> three interwoven registers Corpus, Anima and Spiritus -> Transmutatio/Rubedo -> Projectio -> Status Prima Nova. This architecture nests with, and does not replace, the operational Drager/Nigredo/Albedo/Rubedo/Projectio macro arc."
  affects:
  - ARC.CLAES.GREAT_WORK.AUTHORIAL
  - ARC.CLAES.MACRO_TRANSMUTATION
  - ARC.CLAES.LIFE
  - ARC.CLAES.SINNE_RECOVERY
  principles:
  - "The author knows the Work; Claes undergoes it; the reader experiences it."
  - "Solve et Coagula is an authorial movement of separation and renewed relation, not a slogan characters must repeat."
  - "Corpus, Anima and Spiritus spiral through the same chronology; they are not three mechanically identical cycles or three successive books."
  - "Material processes must remain causally real in the story; the alchemical architecture is not decorative allegory laid over unrelated events."
  - "Status Prima Nova is not restoration of untouched childhood but a changed capacity for relation, discernment and release."
  guardrails:
  - No fixed seven-operation scheme is mandatory.
  - No historical claim that all alchemists used this exact narrative architecture.
  - No requirement that every scene receive an alchemical label in prose.
  - Do not let symbolic interpretation override the actual chemistry, craft, politics, grief or human causality of a scene.

- id: DEC.MAYKEN.INDEPENDENT_ARC.2026-08-16
  type: CanonDecision
  status: CANON
  decision: "Mayken has an independent character arc and must function as an equal necessary other rather than as reward, therapist, decoder or auxiliary to Claes. Her own line grows from the Lampert material/apothecary world, the 1554 experience of destruction-with-rebuilding, trained sensory judgement and choices that can support, contradict or limit Claes."
  affects:
  - ARC.MAYKEN.LIFE
  - REL.CLAES.BELOVED
  - REL.CLAES.BELOVED.RECOVERY
  - REL.CLAES.MAYKEN.CONJUNCTIO
  principles:
  - "Every developed Mayken scene must give her an objective, judgement or choice that is not reducible to Claes' immediate need."
  - "Her competence is body/plants/material identification/measurement/error control, not hidden-order decoding."
  - "Her different 1554 loss is a counter-memory: damaged material life can be worked and rebuilt."
  - "Her late companionship may catalyse Claes' sensory recovery while she remains an acting subject with her own limits and decisions."
  guardrails:
  - Do not duplicate Claes' trauma biography.
  - Do not give Mayken unsupported university, physician or later guild status.
  - Do not make her a cipher/nomenclator/special-Dodoens key-holder.
  - Exact mid-arc family pressure, professional independence and any kruidenvrouw trajectory remain authorial-design work under OPEN.MAYKEN.INDEPENDENT_MIDARC.001.

- id: DEC.CLAES_MAYKEN.CONJUNCTIO.2026-08-16
  type: CanonDecision
  status: CANON
  decision: "The mature Claes-Mayken relationship functions on the authorial level as conjunctio: two unlike modes of knowing and acting enter relation without one absorbing the other. Love matures from complementarity and collaborative risk toward relation without possession."
  affects:
  - REL.CLAES.MAYKEN.CONJUNCTIO
  - REL.CLAES.BELOVED
  - ARC.CLAES.SINNE_RECOVERY
  - ARC.MAYKEN.LIFE
  guardrails:
  - Conjunctio is authorial architecture, not proof that the characters consciously name their relationship in alchemical terms.
  - Mayken does not complete Claes' Great Work for him.
  - Claes does not become whole by possessing Mayken.
  - The relationship may contain disagreement, separate work and asymmetry of knowledge; harmony is not the same as sameness.
```

---
