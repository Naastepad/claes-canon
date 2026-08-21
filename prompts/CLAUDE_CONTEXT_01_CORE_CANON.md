# Claude Context Pack — 01_CORE_CANON — GENERATED

> Generated projection; never edit by hand. GitHub source files remain authoritative.
> Treat each SOURCE FILE section as the original source file.
> Do not use this pack as permission for free repository discovery; follow the task router in CLAUDE_CONTEXT_INDEX.md.

- source branch: `main`
- source commit at generation: `88637ab63031f073eb8023becb15bdef794fc72f`
- generated UTC: `2026-08-21T21:06:16+00:00`
- included files: `11`

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

## 8A. Author personal-context boundary

Personal material about the human author that appears in chats, Claude/ChatGPT exports, project dumps, autobiographical notes or life-story discussions is **AUTHOR CONTEXT**, not historical evidence and not Claes canon.

Do not copy concrete author biography into `SC.*`, `STC.*`, `DEC.*`, `ENT.*`, `NI.*`, character backstory or other Storybible truth by default. Do not infer that a fictional character shares a personal event merely because a psychological or thematic resemblance exists.

The only permitted route from personal material to canon is:

`AUTHOR CONTEXT -> abstract pattern/question -> explicit fictional proposal -> human author approval -> FICTION CANON`

Once approved, store the fictional result as a self-contained claim about the novel. Do not preserve the author's private biographical source detail in the story layer. If the author has not separately approved the fictional derivative, keep it outside canon or present it as a proposal.

This applies especially when ingesting large coauthor/model dumps that mix manuscript discussion, story development and autobiography. Recover only the independently supported/approved story consequences; never treat the dump's personal passages as Storybible authority.

See `AUTHORING_POLICY.md` for the full guardrails.

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

That file is designed to be copied into Claude Project Instructions.

## Primary Claude entrypoint

For every canon-sensitive task, Claude must first fetch and obey:

`prompts/CLAUDE_CONTEXT_INDEX.md`

Literal URL:

https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_INDEX.md

This generated file is not merely an index. It is the **task router** that assigns the exact context packs required for canon questions, character work, scene/chapter writing, hard revision, Mayken work and repository mutation.

**Do not begin by browsing repository directories or keyword-searching for relevant canon.** Load the router-assigned packs first. Additional files may then be fetched only when the loaded `MASTER`, `INDEX`, decision/claim or governing dossier explicitly names them, unless the user explicitly requests repository-wide discovery/audit.

The reason is continuity: free repository discovery can surface a technically relevant but stale, partial or lower-authority file before the current governing layer. Task routing must determine the reading set; discovery is only a fallback.

## Authority

Within the loaded packs, follow `AI_ONBOARDING.md` and its authority hierarchy. In particular:

1. latest applicable explicit `DEC.*` decisions;
2. active synchronized `STC.*` Story Claims;
3. current governing dossiers / structured state;
4. current operating master;
5. lower-authority evidence, proposals, opens and legacy material.

Do not substitute conversation memory or Project Knowledge for repository truth. Preserve the distinction between historical evidence (`SC.*`), novel truth (`STC.*`), narrative instances (`NI.*`) and deterministic Lemma constraints.

Never silently promote `OPEN` or `PROPOSED` material to `CANON`. Never invent precision that the Storybible does not contain.

## Character work

Any task about a recurring named character, relationship, motivation, archetype or characterization must load the router's `06_CHARACTER_WEB` pack in addition to core canon and dated decisions.

Archetypal labels are author-side lenses, not complete personalities. Use the concrete characterization layer: governing value, strength, shadow, contradiction, habitual expression, independent agency and relationship-specific state.

If Mayken appears, also load `04_MAYKEN_KNOWLEDGE`.

## Prose / revision

If writing prose, obey the task router plus `AI_ONBOARDING.md` and `WRITING_PROTOCOL.md`: identify the causal hinge, POV, story-time window, active claims, knowledge/object state, character web, arcs/relationships/motifs, relevant domain/world pack, reader movement and open decisions that must remain open. Then write literary text without embedding metadata labels into the prose.

If revising or critiquing, determine `RETAIN / REVISE / MERGE / CUT` before line-polishing.

## Access failures

If Claude's fetch tool refuses a required literal pack URL, do not replace the missing pack with memory or improvised repository discovery. Report the exact failed URL and stop canon-sensitive conclusions until the required pack is available.

If a pack is truncated, report the last visible `SOURCE FILE` heading and do not pretend the remainder was read.

At the end of substantial work, leave a concise handoff stating packs/governing records consulted, changes proposed/made, unresolved decisions, sync state and validation status.
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

## Historical evidence gaps are authorial space

Under `DEC.HISTORICAL_GAPS.FICTIONAL_CHARACTERIZATION.2026-08-19`, absence of historical evidence is **not** by itself a prohibition on fictional specification.

For a recurring person, location, object or practice, the author may deliberately fill a documentary gap when the choice has real continuity, character, causal, spatial or reader-experience value, provided that:

1. no known evidence is contradicted;
2. the fictional choice is historically plausible for the time/place/status involved;
3. the fiction status is recorded explicitly as story/character/world canon rather than Source Claim;
4. the historical evidence status remains unchanged (`UNKNOWN` remains `UNKNOWN`);
5. the chosen detail is synchronized anywhere continuity depends on it;
6. later contradictory evidence triggers review rather than silent rewriting.

This rule is especially important for recurring historical people whose archival record preserves office or work but not ordinary human particulars. Voice, habits, room use, private reactions or appearance may be fixed as **FICTION CANON** without being misrepresented as recovered biography.

Do not fill every gap automatically. A detail earns canon when future scenes benefit from stability. The archive sets the boundary; the novel may fill the living space inside it.

For the current core-cast implementation, load `storybible/CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md` and `entities/CHARACTERIZATION_2026-08-19.yaml`.

## Author personal-context boundary

Personal material supplied by the author in conversations, model exports, project dumps, autobiographical notes or life-story discussions is **AUTHOR CONTEXT**, not Claes evidence and not Storybible canon.

Never convert a concrete fact, event, relationship, location, diagnosis, conflict, chronology or other personal biographical detail about the author into `SC.*`, `STC.*`, `DEC.*`, `ENT.*`, `NI.*`, character biography or other story truth merely because it appeared in coauthoring context.

Personal experience may inspire the novel only through an explicit abstraction-and-approval boundary:

`AUTHOR CONTEXT -> abstract dramatic/psychological pattern or thematic question -> explicit fictional proposal -> human author approval -> Claes FICTION CANON`

The approved fictional derivative must stand on its own as a claim about the novel. It must not carry the author's private source biography into the repository unless the author explicitly asks for a separate, clearly labelled author-context record.

Examples of permissible transformation include turning a broad concern such as recognition versus practical care, attention versus control, or loss versus reconstruction into a fictional character dynamic after explicit approval. The repository should record the resulting Claes/Cornelis/Mayken story truth, not the author's autobiographical event that may have inspired it.

Guardrails:

1. similarity between the author's life and a character is never evidence that the character shares the author's biography;
2. model inference from autobiographical material may be used to suggest a **proposal**, never to declare canon;
3. sensitive or identifying author information is excluded from Storybible canon unless the author explicitly requests otherwise for a separate non-story purpose;
4. when provenance matters, cite the human fiction decision, not the autobiographical source material;
5. if a prior model dump mixed author biography with story development, recover only separately approved fictional consequences; do not normalize the personal biography into the story layer by default.

## Narrative theory boundary
Universal `KO.*` narrative theory remains in the external Narrative Knowledge Base. This repository stores Claes-specific Narrative Instances and may reference Knowledge Objects as analysis targets.

Archetypal analysis is permitted as an author-side character-web lens, but an archetype is not a complete person and never overrides entity biography, historical evidence, motive, desire, class, confession, work or material circumstance. Do not force every character into an archetype or write archetypal labels into literary exposition.

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
  decision: On 18 May 1554 the fictional Cornelis household loses its home in the older Nieuwstraat. Claes directly experiences the Goese fire event but survives because he is away from the house when it becomes fatal; Cornelis is absent from the immediate fire zone during the decisive interval. Claes' mother, his younger brother born about eighteen months after Claes, and the mother's unborn child die in the fire. The mother is about six months pregnant.
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
  decision: Historical Claes Jacobsz. Nissepat is used in novel canon as the fictional father of Cornelis and paternal grandfather of Claes. He remains the story owner of the 1542 Nieuwstraat house through the 1554 fire, loses that asset in the fire, is present by the burial/early formal aftermath, and subsequently helps Cornelis support Claes' education.
  affects:
  - STC.CLAES.GRANDFATHER.NISSEPAT.001
  - ENT.PERSON.CLAES_JACOBSZ_NISSEPAT
  - ENT.PROP.GOES.NISSEPAT.NIEUWSTRAAT_1542
  - REL.CORNELIS.CLAES_JACOBSZ_NISSEPAT
  rationale: The historical person and his 1542 purchase are documented; the paternal genealogy, continued ownership through 1554 and post-fire support are deliberate fictional connections and must never be presented as archival fact.
- id: DEC.CLAES.POSTFIRE_FATHER_SON.2026-08-14
  type: CanonDecision
  status: CANON
  decision: After the 1554 fire Cornelis stays in Goes to rebuild livelihood, business and shelter and to finance Claes' schooling as far as he can, with partial support from his father Claes Jacobsz. Eleven-year-old Claes is sent to Reimerswaal because the original Zierikzee plan has become financially unattainable. Father and son therefore lose not only their household but also daily life with each other; the separation is an act of care that Claes can experience as abandonment.
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
schema_version: 2.2.0
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

Release state: `MANUSCRIPT_CANON_AND_GOES_FIRE_CONTINUITY_SYNCHRONIZED_2026-08-21`

Manuscript/canon addendum: `MANUSCRIPT_EDITOR_OPENS_CLOSED_AND_FIRE_SEQUENCE_SYNCHRONIZED_2026-08-21`

Historical recovery addendum: `ROUND_A_HISTORICAL_SUBSTRATE_RECOVERED`

Authoring world-state addendum: `ROUND_B_DOMAIN_REBUILD_IMPLEMENTED`

Story-projection addendum: `ROUND_C_STORY_PROJECTION_IMPLEMENTED`

Editorial/reader addendum: `ROUND_D_EDITORIAL_READER_PROTOCOL_IMPLEMENTED`

Goes clergy addendum: `GOES_CLERGY_MATHIJS_CLEMENS_CANONIZED_AND_SYNCHRONIZED_2026-08-16`

Character-web addendum: `CORE_CHARACTER_WEB_AND_FICTION_CHARACTERIZATION_SYNCHRONIZED_2026-08-19`

The 21 August follow-up closes the five editor-ingest OPEN records with explicit decisions, fixes the Nissepat footbow carrier as a fictional penning/hanger, distinguishes Claes' direct fire experience from Cornelis' absence, restores grandfather to the burial/early aftermath, fixes Claes' Reimerswaal arrival age at eleven, and requires the specific *De Kraai* dread callback in *De Kade*. The fire and aftermath are a multi-chapter sequence. Mayken's immediate-aftermath absence is intentional.

The later fire manuscript and *De Kade* are not stored in this repository. Their exact prose remains an external manuscript implementation boundary; repository synchronization is complete for the canon and projection layers and does not certify unavailable chapter text.

The 19 August character-web decisions are synchronized through Story Claims, core characterization entities, Puttus and Mayken detail records, the Claes-Mayken relationship projection, authoring policy, a governing Storybible dossier, `storybible/MASTER.md` and `storybible/INDEX.md`. Historical Source Claims were not changed: documentary UNKNOWN remains UNKNOWN where the novel deliberately fixes a separately labelled fiction-canon characterization.

## Current governing chronology

- Claes born Goes: **8 December 1542**.
- **14 March 1541:** mr. Mathijs Jacopsen explicitly attested as vice-pastoor.
- **27 February 1542:** mr. Mathijs Jacobsen explicitly attested as `vice-cureyt ter Goes`.
- **8 December 1542:** exact Goese office-holder at Claes' birth remains historically UNKNOWN; Mathijs must not be projected automatically from February to December.
- **1553–1554:** Claes and Mayken canonically know one another as Goese children through ordinary acquaintance/friendship; no childhood romance.
- Family rupture: **18 May 1554**.
- Reimerswaal: arrival later in 1554 at age **eleven**; turns twelve on 8 December 1554; remains through summer 1561.
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

### Character web / characterization

- `storybible/CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md` is the governing human-readable characterization dossier.
- `entities/CHARACTERIZATION_2026-08-19.yaml` stores stable fiction characterization separately from historical biography.
- `narrative/character_web_archetypes.yaml` stores the author-side contrast web; archetypal labels are never in-world doctrine.
- Historical evidence gaps may be deliberately filled as fiction canon under `DEC.HISTORICAL_GAPS.FICTIONAL_CHARACTERIZATION.2026-08-19`; historical evidence status remains unchanged.
- Core shorthand: Claes/Integration, Cornelis/Law, Tanneken/Body, Jan/Act, Puttus/Word, Mayken/Matter, Dee/Transformation, Silvius/Transmission, Las Casas/Conscience.
- Each shorthand is individualized through strength, shadow, contradiction, habits and independent agency.
- Puttus' historical age/appearance/exact 1550s room remain UNKNOWN, while his quiet authority, exact correction, age-indeterminate child impression and small sparse teaching room are now explicit FICTION CANON.
- Las Casas now has `ENT.PERSON.BARTOLOME_DE_LAS_CASAS`; private prologue interiority remains fictional reconstruction unless sourced.

### Cornelis

- Goes poorter;
- biersteker, not fixed brewery owner;
- Nardusbloem / older Magdalena-linked rederijker;
- fictional formative role in the 1560s current that becomes the later Edele Castanienbloem;
- character web: father/steward/gatekeeper whose protection can become exclusion; domestic reserve contrasts with rederijker vitality;
- deken status remains open;
- fictionally executed 19 November 1569 in Antwerp, witnessed by Claes.

### Mayken

- identity resolved as **Mayken Adriaensdr. Lampert**, fictional, ca.1546 Goes;
- `ENT.PERSON.BELOVED` is a legacy stable entity ID, not an open identity;
- canonically knows Claes before the 1554 fire as a child acquaintance/friend, not childhood sweetheart;
- independent materia-medica/material/sensory/error-control expertise;
- character web: material fidelity is strength; impatience with what cannot yet be materially demonstrated is a possible shadow;
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
- `REL.CLAES.MAYKEN.CONJUNCTIO` requires reciprocal relation with two centers of agency and now includes pre-fire childhood acquaintance followed by divergent post-fire paths.
- `ARC.CLAES.CHARACTER_WEB.ARCHETYPAL` differentiates recurring characters by method/value/shadow without turning the shorthand into in-world doctrine.
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

## Character-web refinement — 19 August 2026

Synchronized files:

- `canon/DECISIONS_CHARACTER_WEB_2026-08-19.yaml`;
- `claims/STORY_CLAIMS_CHARACTER_WEB_2026-08-19.yaml`;
- `entities/CHARACTERIZATION_2026-08-19.yaml`;
- `entities/LAS_CASAS.yaml`;
- `entities/GOES_PUTTUS_1512_1554.yaml`;
- `entities/MAYKEN_LAMPERT.yaml`;
- `narrative/character_web_archetypes.yaml`;
- `narrative/mayken_relationship_projection.yaml`;
- `storybible/CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md`;
- `storybible/GOES_SCHOOLING_PUTTUS_1550_1554.md`;
- `storybible/MAYKEN_LAMPERT.md`;
- `AUTHORING_POLICY.md`;
- `storybible/MASTER.md`;
- `storybible/INDEX.md`;
- `review/CHARACTER_WEB_REFINEMENT_2026-08-19.md`;
- this sync-status file.

No historical Source Claims were promoted or rewritten by this pass. No personality/archetype Lemma constraints are warranted.

## Current active high-impact authorial opens

- `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001`;
- `OPEN.MAYKEN.INDEPENDENT_MIDARC.001`;
- exact 1570→1578 publication/transmission chain;
- exact 1564 translator/source route;
- exact material wet/press validation;
- exact Rode-Leeuw carrier composition;
- exact Enkhuizen assay choreography;
- Claes' exact death and final merels realization.

Historical research gaps that must not be mistaken for factual certainty include the exact Goese clergy succession between the February 1542 Mathijs anchor and the March 1564 Clemens anchor, Puttus' historical age/appearance/exact 1550s room, and many private habits of historical Dee, Silvius and Las Casas. Approved fiction characterization may fill selected gaps in the novel without changing their evidence status.

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
3. character/relationship/object/knowledge state plus `entities/CHARACTERIZATION_2026-08-19.yaml` for recurring core cast;
4. Round-D scene-necessity, pacing, prose and reader-experience gates.

## Validation note

Repository CI must be evaluated on the actual integration commit. This status does not pre-claim a workflow result that has not yet run.
```

---

# SOURCE FILE: `storybible/MASTER.md`

```markdown
# Claes Storybible — MASTER / operating authority

**Logical master ID:** `SB.CLAES.MASTER`  
**Current synchronization date:** 21 August 2026
**Authoring readiness:** Rounds A–D implemented; manuscript/fire continuity sync active

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
3. `storybible/CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md` — stable core-cast characterization, character shadows and author-side archetypal contrast; explicitly separates historical evidence from fiction fills.
4. `WRITING_PROTOCOL.md` — governing drafting, revision, pacing, prose-quality and scene-retention protocol.
5. `review/READER_EXPERIENCE_PROTOCOL.md` — cold-reader, human pilot-reader and reader-feedback method.
6. `storybible/INDEX.md` — operational navigation.
7. `canon/OPEN_DECISIONS.yaml` — active unresolved backlog only.
8. `review/SYNC_STATUS.md` — synchronization state.

The dated `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` is a **legacy snapshot**, not current authoring authority. It may preserve obsolete 1545/cipher/death-window/open-beloved wording for audit history only.

## Dedicated governing dossiers

- `STORY_PROJECTION_ROUND_C.md` — causal spine, deeper Great-Work architecture, Mayken independent arc and explicit open 1572–1579 Goes hinge.
- `CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md` — governing core-character web; archetypes are author-side lenses only, while approved voice/habit/shadow details are fiction canon for continuity.
- `ALCHEMICAL_OPERATION_PALETTE.md` — non-binding author-side palette for Calcination, Sublimation, Solution, Putrefaction, Distillation, Coagulation and Tincture; diagnostic and compositional only, never a mandatory 3×7/21-chapter scheme.
- `WRITING_PROTOCOL.md` — scene construction, prose, pacing, reader experience and editorial decision rules.
- `review/READER_EXPERIENCE_PROTOCOL.md` — reader-testing authority.
- `review/READER_FEEDBACK_TEMPLATE.md` — consistent reader-evidence logging.
- `review/MANUSCRIPT_CANON_SYNC_2026-08-21.md` — closure audit for the editor-ingest repairs and 1554 manuscript projection.
- `MEMORIAAL_BREVISIMA_PRINT_1564.md` — hidden readable tannin/gum print, Dee handoff, graphite rule, direct green-vitriol reveal.
- `MEMORIAAL_BREVISIMA_CASTOFF_1564.md` — 17 single-sheet quarto gatherings / 136 latent pages.
- `FAMILY_CLAES_1542_1554.md` — Tanneken, Jan, grandparents, 1542 house and 1554 family rupture.
- `GOES_FIRE_1554_CAUSAL_ARCHITECTURE.md` — fire origin/ambiguity, unequal survivor positions, multi-chapter aftermath, grandfather continuity and Reimerswaal departure.
- `GOES_SCHOOLING_PUTTUS_1550_1554.md` — Puttus school bridge plus explicit evidence/fiction characterization boundary.
- `GOES_CLERGY_MATHIJS_CLEMENS_1541_1564.md` — named historical Goese clergy anchors: Mathijs Jacopsen/Jacobsen in 1541–early 1542, Clemens van den Dale in 1564, with the 1542–1563 succession gap preserved.
- `MAYKEN_LAMPERT.md` — resolved identity, pre-fire childhood acquaintance and independent character/material role of Mayken, synchronized to no-cipher canon.
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
- `canon/DECISIONS_CHARACTER_WEB_2026-08-19.yaml`
- `canon/DECISIONS_MANUSCRIPT_SYNC_2026-08-21.yaml`

Latest explicit decision wins within its domain. A base registry is not allowed to resurrect an older state merely because a later decision lives in a supplement.

`claims/SOURCE_CLAIMS*.yaml` stores evidence/reconstruction claims. `claims/STORY_CLAIMS*.yaml` stores novel truth. Evidence and story truth remain separate. Characterization story truth added on 19 August lives in `claims/STORY_CLAIMS_CHARACTER_WEB_2026-08-19.yaml`.

### World/practice state

- `narrative/world_modules.yaml`
- `narrative/domain_scene_packs.yaml`
- `narrative/religious_space_sensory_church.yaml`
- `narrative/world_goes_clergy_1541_1564.yaml`
- `storybible/domains/*.md`

These define what can plausibly happen in a place/time/activity. A world module never creates fictional participation by itself.

### Narrative state and projection

- `entities/*.yaml`
- `entities/CHARACTERIZATION_2026-08-19.yaml` — stable fiction characterization separated from historical biography.
- `entities/LAS_CASAS.yaml` — historical Las Casas entity with fiction-interiority boundary.
- `objects/*.yaml`
- `narrative/knowledge_states*.yaml`
- `narrative/relationships.yaml`
- `narrative/arcs.yaml`
- `narrative/motifs.yaml`
- `narrative/instances*.yaml`
- `narrative/alchemical_authorial_architecture.yaml`
- `narrative/story_projection_round_c.yaml`
- `narrative/character_web_archetypes.yaml` — author-side value/shadow contrast web; never in-world labels.
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
- **1553–1554:** Claes and Mayken know one another as Goese children in ordinary acquaintance/friendship; no childhood romance is canonized.
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

## Character web / historical-fiction characterization current state

`DEC.HISTORICAL_GAPS.FICTIONAL_CHARACTERIZATION.2026-08-19`, `DEC.CHARACTER_WEB.ARCHETYPAL_LENS.2026-08-19` and `DEC.CHARACTER_WEB.CORE_CAST.2026-08-19` govern.

The repository now treats documentary silence as potential **authorial space**, not as an automatic ban on characterization. Historical evidence remains unchanged; fiction fills are separately labelled and become continuity canon only by explicit decision.

Core author-side constellation:

- Claes — Integration / Seeker-Witness;
- Cornelis — Law / Father-Gatekeeper;
- Tanneken — Body / embodied household wisdom;
- Jan — Act / brother-double;
- Puttus — Word / hermeneutic teacher;
- Mayken — Matter / independent material counterpart;
- Dee — Transformation / magician-mentor;
- Silvius — Transmission / pragmatic mediator;
- Las Casas — Conscience / witness-herald.

These are lenses, not full personality definitions. Every role is individualized through a governing value, concrete habits, contradiction and a shadow produced by overuse of a real strength. Archetypal shorthand must never be written as in-world explanation.

`storybible/CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md` governs the human-readable layer. Machine detail lives in `entities/CHARACTERIZATION_2026-08-19.yaml` and `narrative/character_web_archetypes.yaml`.

## Mayken current state

The beloved identity is resolved as **Mayken Adriaensdr. Lampert**, fictional, born ca.1546 in Goes. `ENT.PERSON.BELOVED` is retained only as a legacy stable entity ID; it does not mean her identity is open.

Her historical embedding is the real Lampart/Lambert/Lampert apothecary environment. The project distinguishes verified persons/property records, supported identity/genealogy reconstruction and explicit fictional daughtership.

Claes and Mayken now canonically know one another as children before 18 May 1554 through ordinary Goese contact, play and early material/botanical observation. This is **not childhood romance**; later relation may contain recognition and rediscovery without predestination.

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

A historical/research gap does not automatically become a factual authorial claim. However, under `DEC.HISTORICAL_GAPS.FICTIONAL_CHARACTERIZATION.2026-08-19`, the novel may deliberately fix a **fiction-canon answer** inside that gap for recurring characterization or continuity while leaving the evidence status UNKNOWN. Evidence and novel truth remain separate axes.

Round-C high-impact authorial opens include:

- `OPEN.GOES.CLAES_DEPARTURE_1572_1579.001`;
- `OPEN.MAYKEN.INDEPENDENT_MIDARC.001`.

Neither may be silently closed by prose, reader preference or historical plausibility alone.

The Goese clergy succession gap between the February 1542 Mathijs anchor and the March 1564 Clemens anchor is a **historical/research open**, not permission to fabricate a historical continuous incumbency. A fictional scene-use choice, if ever required, must be separately labelled rather than projected as evidence.

## Narrative development backlog

The recovery and readiness rounds are now complete:

- **A** — historical substrate recovered;
- **B** — six major world/practice domains made chapter-ready, supplemented by the evidence-bounded Goese clergy world state;
- **C** — world projected into causal character architecture;
- **D** — editorial, pacing and reader-feedback gates made operational;
- **Character Web refinement** — core cast differentiated through stable fiction characterization, value contrast and shadow while preserving historical evidence boundaries.

The next major task is **structural realization**:

`Book → Act → Sequence → Chapter → Scene → Beat`.

`narrative/structure.yaml` remains largely unpopulated and `narrative/scenes.yaml` contains only a small number of full scene diagnostics. Future population should use `ARC.CLAES.CAUSAL_SPINE`, the character web where recurring cast is involved, plus Round-B scene packs and Round-D scene-necessity/pacing/reader gates during construction rather than only after a full draft exists.

## Precedence

When records conflict:

1. latest explicit current `DEC.*` author decision, including supplements;
2. active later domain-specific `STC.*` story claim or explicit supersession declared by a later decision;
3. dedicated current governing dossier, including `STORY_PROJECTION_ROUND_C.md` and `CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md` within their domains;
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
4. `CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md` — stable core-cast characterization, shadows and author-side archetypal contrast; use for recurring-person continuity.
5. `../WRITING_PROTOCOL.md` — current drafting, prose, pacing and scene-retention authority.
6. `../review/READER_EXPERIENCE_PROTOCOL.md` — cold-reader, pilot-reader and feedback method.
7. `../canon/OPEN_DECISIONS.yaml` — active unresolved backlog only.
8. `../review/SYNC_STATUS.md` — synchronization status.
9. `../review/CANON_CONFLICT_AUDIT_2026-08-16.md` — conflicts found and their resolution.
10. `../review/HISTORICAL_SUBSTRATE_RECOVERY_2026-08-16.md` — Round-A recovery.
11. `../review/DOMAIN_REBUILD_ROUND_B_2026-08-16.md` — Round-B chapter-readiness rebuild.
12. `../review/STORY_PROJECTION_ROUND_C_2026-08-16.md` — Round-C projection audit.
13. `../review/EDITORIAL_PROTOCOL_ROUND_D_2026-08-16.md` — Round-D editorial/reader recovery audit.
14. `../review/CHARACTER_WEB_REFINEMENT_2026-08-19.md` — character-web/fiction-characterization handoff.

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
- `../canon/DECISIONS_PUTTUS_2026-08-18.yaml` — Puttus as Claes' pre-fire Latin/humanist master; evidence/fiction boundary refined 19 August.
- `../canon/DECISIONS_CHARACTER_WEB_2026-08-19.yaml` — fiction-fill policy, core character web, Puttus characterization and Claes-Mayken childhood acquaintance.

## Active open decisions

- `../canon/OPEN_DECISIONS.yaml` — only genuinely unresolved core questions, including the 1572–1579 Goes causal break and Mayken independent mid-arc design.
- `../canon/OPEN_DECISIONS_ALCHEMY_REFINEMENT_2026-08-16.yaml` — Rode-Leeuw carrier composition and exact Enkhuizen assay/choreography.
- `../canon/OPEN_DECISIONS_ALCHEMY_LIFELINE_2026-08-15.yaml` — legacy redirect/supersession record only.

Resolved/not-applicable records no longer remain mixed into the active open registry. Historical/research gaps remain evidence gaps even when the novel deliberately fixes a separately labelled fiction-canon detail under `DEC.HISTORICAL_GAPS.FICTIONAL_CHARACTERIZATION.2026-08-19`.

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

For a recurring character, world readiness must now also include the relevant stable fictional characterization where it exists. Historical UNKNOWN does not erase an approved fiction-canon voice/habit choice.

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
- `CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md` — recurring-character continuity and value/shadow differentiation.
- `ALCHEMICAL_OPERATION_PALETTE.md` — non-binding author-side palette of seven classic operations (Calcination, Sublimation, Solution, Putrefaction, Distillation, Coagulation, Tincture), with narrative, sensory and show-don't-tell applications; never a mandatory 3×7 or 21-chapter template.
- `../narrative/story_projection_round_c.yaml` — `ARC.CLAES.CAUSAL_SPINE`, fourteen current causal hinges from Status Prima to Status Prima Nova.
- `../narrative/alchemical_authorial_architecture.yaml` — `ARC.CLAES.GREAT_WORK.AUTHORIAL`: Status Prima; interwoven Corpus/Anima/Spiritus; Transmutatio/Rubedo; Projectio; Status Prima Nova.
- `../narrative/character_web_archetypes.yaml` — author-side character-web projection; archetypal shorthand never appears as in-world doctrine.
- `../narrative/mayken_independent_arc.yaml` — `ARC.MAYKEN.LIFE`.
- `../narrative/mayken_relationship_projection.yaml` — `REL.CLAES.MAYKEN.CONJUNCTIO`, now including childhood acquaintance and divergent post-fire paths.
- `../narrative/goes_departure_1572_1579.yaml` — explicit open causal design projection for Claes' final material/economic severance from Goes.

### Great-Work rule

`ARC.CLAES.MACRO_TRANSMUTATION` remains the chronological **Drager → Nigredo → Albedo → Rubedo → Projectio** spine. The deeper Round-C architecture does not replace it.

**Status Prima → Corpus / Anima / Spiritus → Transmutatio/Rubedo → Projectio → Status Prima Nova** is an author-side register model. Corpus/Anima/Spiritus spiral through the same chronology and must not become three mechanically identical cycles. No fixed alchemical operation count is mandatory.

The seven-operation palette is therefore a **compositional and diagnostic vocabulary only**. Use an operation when a scene's actual material, relational or inner causality earns it; never reverse-engineer a scene solely to satisfy the palette.

### Character-web rule

Archetypal functions are author-side lenses, not complete personalities. For recurring core cast load `entities/CHARACTERIZATION_2026-08-19.yaml` alongside biography/relationship state. Strength, shadow and contradiction are continuity aids; characters may still surprise the shorthand when scenes earn it.

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
- `../canon/DECISIONS_MANUSCRIPT_SYNC_2026-08-21.yaml` — resolved editor-pass repairs, fire survivor positions, penning/hanger form, grandfather continuity, Reimerswaal callback and age eleven.
- `../review/MANUSCRIPT_CANON_SYNC_2026-08-21.md` — audit trail for the follow-up synchronization and manuscript boundary.
- `../claims/STORY_CLAIMS_2026-08-14.yaml`
- `../claims/STORY_CLAIMS_GOES_CLERGY_2026-08-16.yaml` — canonical scene-use boundaries for Mathijs and Clemens.
- `../claims/STORY_CLAIMS_MAYKEN_LAMPERT.yaml`
- `../claims/STORY_CLAIMS_ALCHEMY_REFINEMENT_2026-08-16.yaml`
- `../claims/STORY_CLAIMS_HOUSE_OF_LOVE_NETWORK_2026-08-16.yaml` — Cornelis' commercial trust bridge, Dens/Barrefelt affiliation, pre-fire state, later Plantin node and beer-to-paper logistics continuity.
- `../claims/STORY_CLAIMS_CHARACTER_WEB_2026-08-19.yaml` — core characterization, shadows and Mayken childhood acquaintance.

## People and relationships

- `../entities/ENTITIES.yaml`
- `../entities/FAMILY_1554.yaml`
- `../entities/GOES_CLERGY_1541_1564.yaml` — historical Mathijs Jacopsen/Jacobsen and Clemens van den Dale entity supplement.
- `../entities/GOES_PUTTUS_1512_1554.yaml`
- `../entities/MAYKEN_LAMPERT.yaml`
- `../entities/CHARACTERIZATION_2026-08-19.yaml` — stable fiction characterization for core cast, separately labelled from historical biography.
- `../entities/LAS_CASAS.yaml`
- `../entities/ALCHEMY_REDERIJKER_2026-08-16.yaml`
- `../entities/HOUSE_OF_LOVE_NETWORK_2026-08-16.yaml` — Ghysbrecht, Dens, Barrefelt, Plantin, translocal network entity and canonical Cornelis relationships.
- `../narrative/relationships.yaml`
- `../narrative/arcs.yaml`
- `../narrative/character_web_archetypes.yaml`
- `../narrative/sinne_recovery.yaml`
- `../narrative/beloved_recovery.yaml` — resolved Mayken identity; no longer an open-identity layer.
- `../narrative/mayken_independent_arc.yaml`
- `../narrative/mayken_relationship_projection.yaml`

## Major Storybible dossiers

### Character web / characterization

- `CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md` — governing core-cast value/strength/shadow/voice dossier.
- `../entities/CHARACTERIZATION_2026-08-19.yaml`
- `../narrative/character_web_archetypes.yaml`
- `../review/CHARACTER_WEB_REFINEMENT_2026-08-19.md`

### Goes / family / church

- `FAMILY_CLAES_1542_1554.md`
- `GOES_SCHOOLING_PUTTUS_1550_1554.md` — Puttus evidence boundary plus explicit fiction characterization.
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
- `../narrative/character_web_archetypes.yaml` — author-side recurring-character contrast.
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

Current limitation: `structure.yaml` still needs populated Book/Act/Sequence/Chapter/Beat hierarchy and `scenes.yaml` needs many more scene-level diagnostics. Rounds A–D plus the character-web refinement now supply the evidence, world, causal, character and editorial infrastructure to populate them without reverting to research-led scene accumulation or session-by-session reinvention of recurring people.

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
- `../review/CHARACTER_WEB_REFINEMENT_2026-08-19.md`
- `../review/READER_EXPERIENCE_PROTOCOL.md`
- `../review/READER_FEEDBACK_TEMPLATE.md`
- `../review/CHAT_COMMITMENT_AUDIT_2026-08-13.md` and addendum
- `../review/SYNC_STATUS.md`

## Validation

- `../scripts/validate_canon.py`
- `../scripts/validate_active_projection.py`
- `../.github/workflows/canon-repository-validate.yml`
- `../.github/workflows/lemma-validate.yml`

GitHub canon remains authoritative. Later explicit author decisions override stale broad prose; no AI may silently turn plausibility, editorial preference or reader suggestion into historical evidence. Approved fiction fills remain story continuity, not Source Claims.
```

---
