# Claude Context Pack — FULL — GENERATED

> Generated projection; never edit by hand. GitHub source files remain authoritative.
> Treat each SOURCE FILE section as the original source file.
> Do not use this pack as permission for free repository discovery; follow the task router in CLAUDE_CONTEXT_INDEX.md.

- source branch: `main`
- source commit at generation: `d05b988e7b24e06cfdef0fc367975d16fb57fb98`
- generated UTC: `2026-08-19T08:30:50+00:00`
- included files: `63`

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

Release state: `AUTHORING_BRANCH_CHARACTER_WEB_SYNCHRONIZED_2026-08-19`

Historical recovery addendum: `ROUND_A_HISTORICAL_SUBSTRATE_RECOVERED`

Authoring world-state addendum: `ROUND_B_DOMAIN_REBUILD_IMPLEMENTED`

Story-projection addendum: `ROUND_C_STORY_PROJECTION_IMPLEMENTED`

Editorial/reader addendum: `ROUND_D_EDITORIAL_READER_PROTOCOL_IMPLEMENTED`

Goes clergy addendum: `GOES_CLERGY_MATHIJS_CLEMENS_CANONIZED_AND_SYNCHRONIZED_2026-08-16`

Character-web addendum: `CORE_CHARACTER_WEB_AND_FICTION_CHARACTERIZATION_SYNCHRONIZED_2026-08-19`

The 19 August character-web decisions are synchronized through Story Claims, core characterization entities, Puttus and Mayken detail records, the Claes-Mayken relationship projection, authoring policy, a governing Storybible dossier, `storybible/MASTER.md` and `storybible/INDEX.md`. Historical Source Claims were not changed: documentary UNKNOWN remains UNKNOWN where the novel deliberately fixes a separately labelled fiction-canon characterization.

## Current governing chronology

- Claes born Goes: **8 December 1542**.
- **14 March 1541:** mr. Mathijs Jacopsen explicitly attested as vice-pastoor.
- **27 February 1542:** mr. Mathijs Jacobsen explicitly attested as `vice-cureyt ter Goes`.
- **8 December 1542:** exact Goese office-holder at Claes' birth remains historically UNKNOWN; Mathijs must not be projected automatically from February to December.
- **1553–1554:** Claes and Mayken canonically know one another as Goese children through ordinary acquaintance/friendship; no childhood romance.
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
**Current synchronization date:** 19 August 2026  
**Authoring readiness:** Rounds A–D implemented; Character Web refinement active

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
- `MEMORIAAL_BREVISIMA_PRINT_1564.md` — hidden readable tannin/gum print, Dee handoff, graphite rule, direct green-vitriol reveal.
- `MEMORIAAL_BREVISIMA_CASTOFF_1564.md` — 17 single-sheet quarto gatherings / 136 latent pages.
- `FAMILY_CLAES_1542_1554.md` — Tanneken, Jan, grandparents, 1542 house and 1554 family rupture.
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

# SOURCE FILE: `storybible/GOES_SCHOOLING_PUTTUS_1550_1554.md`

```markdown
# Goes 1550–1554 — Claes' eerste scholing en Nicolaes van de Put (Puttus)

**Status:** CANON — approved 18 August 2026; characterization refined 19 August 2026  
**Decisions:** `DEC.CLAES.PUTTUS_MASTER.2026-08-18`, `DEC.PUTTUS.FICTIONAL_CHARACTERIZATION.2026-08-19`  
**Story Claims:** `STC.CLAES.PUTTUS_MASTER.001`, `STC.CHARACTER.PUTTUS.HERMENEUTIC_MENTOR.001`  
**World module:** `WORLD.GOES.SCHOOLING_1550_1554`

This dossier governs Claes' education in Goes before his departure to Reimerswaal. It replaces the thinner interpretation in which Goes provided only unspecified elementary schooling and Reimerswaal effectively began his Latin formation from zero.

## 1. Historical evidence

### Nicolaes van de Put / Puttus
P.J. Meertens identifies **Nicolaes van de Put (Puttus)** as schoolmaster in Goes in **1512**. Puttus belonged to the humanist educational network around Hadrianus Barlandus. Barlandus' Aesop school material and its address to Puttus show a Latin/humanist teaching context for the Goese studying youth; Meertens consequently treats Puttus as Latin schoolmaster and probably rector.

That establishes a real named Goese humanist schoolmaster one generation before Claes.

What it does **not** establish is Puttus' continuous tenure from 1512 into the 1550s. His birth date, death date, departure date, physical appearance and exact period in office remain unknown.

### Later Goese anchor
The episcopal school inspection of **1569** explicitly found seven schools in Goes, including a Latin school. This supports the existence of an older Goese Latin-school tradition but does not fill the documentary gap for every year between 1512 and 1569.

### Specialized histories
The audit located:

- R.C.H. Römer, *De Latijnsche school te Goes*, *Nehalennia* I (1849), beginning around p. 79;
- H.W. Fortgens, *De Latijnse school te Goes*, *Archief Zeeuwsch Genootschap* (1953), pp. 1–28.

The available digital/search layer did not expose their complete page text sufficiently to reconstruct a reliable rector succession for 1512–1569. Targeted searches of citations and name variants found **no death, departure or named successor that excludes Puttus from ca. 1550–1554**, and no better named Goese Latin master for Claes' exact interval.

This absence is not proof of a forty-year tenure.

## 2. Explicit author decision

The author has decided:

> **If no contrary evidence emerges, Nicolaes van de Put/Puttus is Claes' man.**

Therefore, in novel canon Puttus personally teaches Claes in the final Goese school years before the fire of **18 May 1554**.

This is a deliberate historical-fiction bridge:

- **historical person:** Puttus;
- **historical anchor:** schoolmaster in Goes, 1512, Latin/humanist context;
- **unknown history:** his actual tenure into the 1550s;
- **novel truth:** he teaches Claes.

Never collapse those four levels.

## 3. Claes' Goese educational route

The current core Story Claim already places elementary Goese education before May 1554. This dossier specifies the shape of that formation without inventing a modern timetable or exact local curriculum.

### First layer — elementary literacy
Before the Puttus layer, Claes develops:

- reading and spelling;
- writing and copying;
- religious literacy, prayer/text memorisation and church-linked language;
- elementary numeracy.

These skills also resonate with Cornelis' material world of names, quantities, debts, measures, barrels, routes and written obligations, without turning merchant practice into a formal school syllabus.

### Second layer — Puttus
As Claes' ability becomes evident, Puttus introduces a first learned/humanist layer:

- initial Latin vocabulary and grammar;
- recitation and reading aloud;
- copying/correction;
- short morally or pedagogically useful Latin material;
- humanist fable material is a particularly defensible model because the historical Puttus is linked through Barlandus to Aesop school material.

The story need not claim that Claes has completed an entire formal Latin-school curriculum in Goes. Puttus gives him **a beginning and a direction**.

## 4. Fiction characterization inside the evidence gap

Under `DEC.HISTORICAL_GAPS.FICTIONAL_CHARACTERIZATION.2026-08-19`, the absence of a documented 1550s portrait, voice or classroom is treated as legitimate authorial space rather than a command to keep Puttus faceless.

The following details are therefore **FICTION CANON**, not recovered biography:

- Claes cannot readily estimate Puttus' age; this is a child's impression, not a concealed exact age;
- Puttus rarely raises his voice when displeased; quietness and waiting are part of his authority;
- his corrections are exact and economical — a finger on a letter, a repeated word, a request to try again;
- he handles a small working collection of books carefully and economically;
- the recurring teaching room may be written as small, sparse and often cold;
- the room is deliberately **not** tied to a claimed archival building or parcel.

This characterization has a shadow. Puttus' silence can sharpen attention, but it can also shame a struggling pupil. Precision can become too closely associated with worth. He is therefore not a frictionless wise mentor.

The governing detailed characterization is `storybible/CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md` and `entities/CHARACTERIZATION_2026-08-19.yaml`.

## 5. Why Zierikzee still matters

Zierikzee is not chosen because Goes supposedly has no Latin teaching. That older explanation is rejected.

Cornelis' pre-fire plan is better understood as progression:

**local elementary education → first Latin/humanist formation with Puttus → more sustained Latin-school formation at Zierikzee.**

Thus Cornelis' choice reveals ambition for Claes rather than educational necessity.

## 6. What the 1554 fire changes

The fire does not create the idea that Claes should learn further. That decision already exists.

The fire destroys the household and changes the family's economic and practical capacity. Zierikzee becomes financially unattainable; Reimerswaal becomes the viable continuation. Cornelis remains in Goes to rebuild livelihood and finance Claes' schooling while Claes leaves.

The educational causal chain is therefore:

**Goes/Puttus → intended Zierikzee → fire → actual Reimerswaal.**

Reimerswaal continues an existing educational trajectory. It is not Claes' first literacy and no longer needs to be written as his first encounter with Latin.

## 7. Narrative function

Puttus gives Claes an early encounter with the humanist idea that a text is something worked on: read, repeated, corrected, compared and transmitted. That should remain pedagogical before it becomes symbolic.

His deeper narrative function is **disciplined interpretation**. He can teach Claes that a second layer must be supported by what is actually present in the words. That later forms a necessary counterweight to Dee's attraction to hidden relation.

This creates a historically plausible intellectual prehistory for Claes without making him a child prodigy. Antwerp, Silvius and Dee still represent major expansions of his world; Puttus simply ensures that those later encounters grow from an existing learned foundation rather than appearing ex nihilo.

## 8. Hard guardrails

1. Puttus teaching Claes is **CANON**.
2. Puttus' continuous historical tenure from 1512 to 1554 is **UNKNOWN**.
3. Puttus' historical birth/death dates, exact age, appearance and exact 1550s room remain **UNKNOWN as evidence**.
4. Approved fictional characterization may specify how Puttus appears and behaves in the novel, but must never be presented as archival fact.
5. Do not identify the fictional small teaching room with an exact historical Goese school building unless new evidence and a separate decision support it.
6. Do not back-project the later Kruisbroeders/Beestenmarkt school location as proven for Claes' years.
7. Do not claim that Goes lacked Latin teaching before 1554.
8. Do not claim that Claes completed a full formal Latin curriculum before Reimerswaal.
9. Zierikzee remains the intended stronger continuation before the fire.
10. Reimerswaal remains the actual post-fire continuation and must not be written as educational zero.
11. Puttus may train interpretation but must not become a convenient proto-Protestant or anti-ritual mouthpiece.
12. New archival evidence identifying a successor or proving Puttus absent/dead before Claes' school years would require a new explicit author decision; it does not silently rewrite this canon.

## 9. Provenance

See:

- `sources/SRC-HIST-GOES-PUTTUS-SCHOOL-1512-1569-001.md`;
- `claims/SOURCE_CLAIMS_PUTTUS_2026-08-18.yaml`;
- `canon/DECISIONS_PUTTUS_2026-08-18.yaml`;
- `claims/STORY_CLAIMS_PUTTUS_2026-08-18.yaml`;
- `canon/DECISIONS_CHARACTER_WEB_2026-08-19.yaml`;
- `claims/STORY_CLAIMS_CHARACTER_WEB_2026-08-19.yaml`;
- `entities/GOES_PUTTUS_1512_1554.yaml`;
- `entities/CHARACTERIZATION_2026-08-19.yaml`;
- `narrative/world_goes_schooling_1550_1554.yaml`.
```

---

# SOURCE FILE: `storybible/domains/REIMERSWAAL_SCHOOL_1554_1561.md`

```markdown
# Reimerswaal 1554–1561 — city, cost pupil and school practice

**Domain:** `WORLD.REIMERSWAAL`  
**Status:** ACTIVE AUTHORING DOMAIN  
**Primary provenance:** `SRC-HIST-REIMERSWAAL-SCHOOL-CITY-001`

## Core image

Claes arrives in a **living city that knows it is vulnerable**, not in a drowned ruin. Reimerswaal still trades, teaches, worships, cooks, repairs, argues and plans while water repeatedly proves that walls, streets and capital can be temporary.

That distinction is central to the book: Goes teaches sudden fire; Reimerswaal teaches prolonged instability.

## Historical timeline inside Claes' stay

### 1554 — arrival after Goes
- Claes has elementary schooling **and an initial Latin/humanist foundation under Nicolaes van de Put (Puttus) in Goes** already; Puttus' personal teaching of Claes is novel canon under `DEC.CLAES.PUTTUS_MASTER.2026-08-18`.
- Reimerswaal is the cheaper/possible alternative to the pre-fire Zierikzee plan in novel canon.
- Reimerswaal therefore continues an existing learned trajectory; it is not Claes' first literacy or first contact with Latin.
- First scenes should emphasize unfamiliar household/routines and a functioning town, not immediately stage catastrophe.

### 1555 — first major water impression
- flood/storm pressure can become Claes' first lived proof that streets/walls and boundaries are negotiable with water.
- use aftermath, repair, wet storage, displaced routines and adult calculations more often than spectacle.

### 1557 — structural damage
- severe water event damages urban defences/buildings/salt infrastructure in the historical record.
- scene consequence can be detours, scaffolding/repair, labour, damaged property, changed confidence and financial strain.

### 1558 — fire
- a fire in the threatened water-city creates a deliberate but non-identical resonance with Goes 1554.
- Claes need not be placed at its centre; what matters is that no element is purely protective.

### 1561 — renewed flooding / departure year
- by departure Claes has watched a city remain itself while repeatedly losing pieces of itself.
- this prepares his later understanding that identity can survive material change but not unchanged.

## School evidence and reconstruction

### Local source anchors
- school tradition before 1296;
- 1497 civic/ecclesiastical arrangement replaces one `scolaster` with a singing master and schoolmaster;
- schoolmaster appointments again documented in 1569/1570.

### Novel-canon educational model
Claes receives **sustained and increasingly advanced Latin formation** here from 1554 to summer 1561, developing from an incoming pupil who already has elementary literacy and initial Latin/humanist formation into an older/advanced pupil. This is a **story reconstruction grounded in durable school infrastructure**, not a claim that the archives preserve his syllabus.

The pre-Reimerswaal foundation is governed by `storybible/GOES_SCHOOLING_PUTTUS_1550_1554.md`. Puttus is historically documented in Goes in 1512; his continued presence into the 1550s and his teaching of fictional Claes are deliberate story truth, not historical fact.

## Transferable school-day toolkit

Use only as `SUPPORTED_RECONSTRUCTION` unless locally sourced:
- oral recitation and correction;
- Latin grammar/rule learning;
- memorisation;
- reading aloud;
- copying and writing exercises;
- older pupils hearing/helping younger pupils;
- teacher authority, fees and practical cost/boarding arrangements;
- religious/song overlap where the historical school/church relation supports it.

Do not use a modern classroom timetable, age-grade, blackboard pedagogy or nationally standardized curriculum.

## Cost-pupil household

A cost-pupil scene should answer:
- where does Claes sleep and keep his few possessions?
- who feeds him and who pays/owes whom?
- what household work or discipline surrounds schooling?
- how does he move from lodging to school/church/market?
- when weather closes or alters routes, who decides whether routine continues?

Exact host identity and house remain authorial design/research questions unless separately fixed.

## Living-city material fields

Use locally grounded economic/civic activity:
- salt refining and associated fuel/smoke/brine;
- madder/wool/trade as broader economic context;
- harbour/market/transport;
- church and bells;
- walls, gates, drainage/water edges and repair;
- food, lodging, ink/paper/books and school sound.

## Sensory progression across the years

Do not make every Reimerswaal scene smell of disaster. Let sensory state change:
- dry routine interrupted by tide/wind;
- brine/salt smoke as ordinary economy;
- damp wood/stone after water;
- hammering/repair as persistent sound;
- wet paper/leather and warped boards;
- later, recognition of old damage beneath fresh repair.

## Zovitius object link

The water-damaged but readable Zovitius book embodies the Reimerswaal lesson:

**water deforms the carrier yet may leave meaning accessible; fire may erase the carrier entirely.**

The specific damage remains story truth, not archival evidence.

## Scene guardrails

1. Reimerswaal functions throughout Claes' stay.
2. No fixed named rector/schoolhouse without evidence.
3. Exact Latin curriculum = story reconstruction.
4. No seven-year beginner curriculum.
5. Claes arrives with initial Latin/humanist formation; do not reset him to zero.
6. Disaster chronology should alter daily life, not replace it.
7. Never describe the 1574 naval battle as street fighting in Claes' school years.
8. The city's later abandonment must not leak backward into 1554–61 narration as foreknown doom.
```

---

# SOURCE FILE: `storybible/CLAES_CORNELIS_RELATION_1547_1569.md`

```markdown
# Claes en Cornelis — vader-zoonrelatie 1547–1569

**Status:** CANON — approved 18 August 2026  
**Governing decisions:** `DEC.CLAES.CORNELIS.RECOGNITION.2026-08-18`, `DEC.CLAES.CORNELIS.RESPONSIBILITY.2026-08-18`, `DEC.CLAES.CORNELIS.RELIGIOUS_DISSONANCE.2026-08-18`, `DEC.CLAES.CORNELIS.POSTFIRE_READING.2026-08-18`  
**Extends:** `REL.CLAES.CORNELIS`, `ARC.CLAES.CORNELIS`, `DEC.CLAES.POSTFIRE_FATHER_SON.2026-08-14`

This dossier deepens the emotional and developmental logic of the existing father-son arc. It does not replace the established canon that Cornelis loves Claes, teaches him, sacrifices materially for his education and later becomes increasingly secretive through his dangerous networks.

## 1. The central asymmetry

Claes admires Cornelis and wants his recognition.

Cornelis values and trusts Claes, but he expresses that primarily through:

- instruction;
- correction;
- practical inclusion;
- work;
- enlarged responsibility;
- material provision;
- investment in Claes' schooling and future.

He gives comparatively little explicit praise.

That creates the central childhood asymmetry:

> Claes looks for recognition in words and visible approval; Cornelis often expresses recognition by entrusting him with more to do.

The relationship must therefore never be reduced to a cold father and neglected son. Cornelis' love is real. The dramatic problem is that father and son do not automatically read the same acts in the same way.

## 2. Claes' striving

By the early 1550s Claes increasingly learns a relational equation that is only partly true:

**observe carefully → perform correctly → be useful → perhaps father will see me.**

His precision is genuine aptitude. It is not invented by paternal pressure. But the wish for Cornelis' approval gives that aptitude extra force and helps turn usefulness, accuracy and dependability into personal strategies.

This must remain subordinate to Claes' established core movement. It is not a second replacement wound. It helps explain why attention, competence and control become emotionally charged for him.

### Scene grammar

Prefer:

- Claes waiting for a response after doing something well;
- Cornelis checking the result and immediately giving the next task;
- a brief correction where Claes had hoped for praise;
- Cornelis increasing responsibility because the previous task went well;
- Claes reading that increase as another test rather than as trust.

Avoid repeated internal narration that tells the reader “Claes wanted his father's approval.” The dynamic should be visible in expectation, response and silence.

## 3. Responsibility while Cornelis travels

Cornelis' trade and network life take him away from the immediate household at times. As Claes grows older, especially in the early 1550s, he is entrusted with age-appropriate duties that matter during those absences.

Possible canonical task classes:

- help Tanneken with errands or practical household work;
- keep an eye on Jan or fetch him when required;
- remember and deliver a message;
- count or check simple household or trade items;
- note or report an obvious shortage, leak, breakage or missed instruction;
- repeat or repair work after an error.

Claes may therefore begin to experience himself as **the oldest son who must help carry the household when father is away**.

This is not adult authority. At eleven he is still a child within a working household. Do not make him a substitute merchant, bookkeeper with independent legal power, or de facto paterfamilias.

## 4. Consequences of failure

A mistake can matter.

The canon deliberately does **not** fix a corporal-punishment regime. Consequences remain scene-specific and may include:

- a sharp correction;
- doing the task again;
- extra work;
- temporary loss of trust or responsibility;
- helping repair a practical loss;
- having to explain a shortfall or failure;
- Cornelis' terse judgement that something was not done properly.

For Claes, a short functional judgement from Cornelis can carry disproportionate emotional weight because approval matters so much to him.

Do not turn Cornelis into an anachronistic therapeutic father, but do not turn ordinary sixteenth-century paternal authority into gratuitous cruelty either.

## 5. Responsibility for Tanneken, Jan and the unborn child

As the oldest child, Claes can feel increasing responsibility toward the intact household:

- Tanneken is pregnant and has ordinary work to do;
- Jan is close enough in age to be companion and rival but still the younger brother;
- the unborn child is already experienced as part of the family before it can be seen.

Claes' sense of responsibility is therefore real as a feeling, but limited in fact.

This distinction becomes crucial after the fire.

### Hard guardrail

Claes is **not objectively responsible** for the deaths of Tanneken, Jan or the unborn child on 18 May 1554.

However, because he had begun to think of himself as someone who should notice, remember, help and watch over the household, the catastrophe can produce irrational survivor reasoning:

> I was supposed to help carry them. What did I fail to see?

That subjective guilt feeds the already established wound — *if I had seen early enough, could I have prevented what happened?* — without creating a factual causal responsibility.

## 6. Religious dissonance before the fire

Cornelis is not simply “becoming Protestant” in current canon.

By approximately 1552–1553 he belongs in novel canon to the translocal **Huis der Liefde** while remaining outwardly embedded in Catholic Goes. He can attend church and civic-religious life without publicly declaring a separate confession.

Claes, meanwhile, still inhabits the ordinary Catholic child-world of Goes: church, images, prayers, school language, feast rhythm and inherited practice.

The resulting pre-fire tension is therefore subtle.

Claes may notice:

- Cornelis looking somewhere other than expected during a religious moment;
- a silence where Claes expects the same answer he has heard from school or church;
- a phrase from Cornelis that sounds close to orthodox language but not quite identical;
- a visitor, book, journey or conversation that Cornelis closes off;
- a moment in which father and son are physically participating in the same Catholic practice but seem not to be attending to exactly the same thing.

Claes does **not** know the words *Huis der Liefde*, *Familist* or the network behind Cornelis' inward affiliation.

Do not stage explicit Protestant-versus-Catholic debate in the pre-1554 childhood chapters. The dramatic state is **unexplained difference**, not doctrinal comprehension.

## 7. Puttus, school and religious ambiguity

Puttus may deepen Claes' capacity to notice distinctions between words, surface meaning and interpretation, but no specific anti-image, anti-ritual or anti-clerical doctrine is assigned to Puttus without separate historical support.

Therefore:

- Puttus can teach Latinity, fable, grammar, rhetorical distinction and humanist reading;
- a school remark may incidentally resonate with something Claes has heard or observed at home;
- do not use Puttus as a convenient proto-Protestant mouthpiece merely to create father-son conflict.

The useful structure is that church, school and father do not always produce identical meanings for Claes, even when none of them openly declares a confessional break.

## 8. The fire changes the meaning of the recognition gap

Before 18 May 1554, Claes can still imagine recognition as something he may earn tomorrow.

After the fire, Cornelis makes one of the strongest acts of paternal care in the entire relationship: he stays in Goes to rebuild livelihood, credit and shelter while preserving enough means to continue Claes' education elsewhere.

Yet the act is structurally tragic because Claes can read it through the older gap:

> Everyone else is gone, and now father sends me away too.

The established double truth remains binding:

- **Cornelis:** I send him away because I refuse to let the fire take his future.
- **Claes:** I am the surviving son, and still father does not choose to keep me beside him.

The second statement is Claes' wounded interpretation, not Cornelis' intention.

## 9. Reimerswaal and distance

During the 1554–1561 separation, Cornelis' care can remain materially visible through:

- payment;
- books or school materials;
- messages;
- practical arrangements;
- visits where plausible;
- continued concern for Claes' progress.

Those acts do not automatically satisfy Claes' need for recognition or closeness.

This makes the separation richer than simple abandonment: Claes can possess evidence that his father cares and still feel abandoned.

## 10. Later secrecy gives childhood memories new meaning

From 1561 onward, and especially as dangerous books, papers, routes and loyalties become visible, Claes begins to understand that the closed doors he sensed in childhood were real.

The causal movement is:

**childhood unexplained difference → adolescent suspicion → adult partial understanding.**

Claes should not retrospectively become omniscient. He can recognize patterns without suddenly knowing every earlier conversation, visitor or motive.

## 11. 1569 — what is finally lost

Cornelis' execution on 19 November 1569 removes more than a living parent.

It closes the remaining possibility of:

- explicit paternal recognition;
- explanation of the old silences;
- clarification of what Cornelis believed and why;
- reconciliation over the post-fire separation;
- asking whether Cornelis saw Claes in the way Claes had always watched him.

This strengthens the existing canonical resonance that Cornelis' death is also the loss of time father and son may have believed they could still recover.

The final inheritance remains moral, not cryptographic.

## 12. Writing guardrails

1. Cornelis loves Claes; do not rewrite him into a loveless father.
2. Cornelis' trust is often expressed as increased responsibility.
3. Claes' recognition hunger is real but should usually be dramatized rather than named.
4. Claes' precision is both innate/formative aptitude and partly a relational strategy; neither explanation replaces the other.
5. Responsibilities before 1554 remain child-scaled.
6. No automatic corporal punishment is canonized.
7. Claes may feel responsible for family safety but is not causally responsible for the 1554 deaths.
8. Cornelis is Familist/Huis der Liefde with outward Catholic conformity, not simply “Protestant”.
9. Pre-fire religious conflict is intermittent, observational and incompletely understood.
10. The Reimerswaal separation is simultaneously paternal sacrifice and filial experience of rejection.
11. Later secrecy should retrospectively illuminate childhood dissonance without granting Claes impossible knowledge.
12. Cornelis' 1569 death ends the possibility of future recognition and reconciliation as well as the relationship itself.
```

---

# SOURCE FILE: `storybible/NISSEPAT_ARMS_SINT_JORIS_CORNELIS.md`

```markdown
# Nissepat familiewapen, Sint-Joris en Cornelis

**Status:** CANON — fact-fiction bridge approved 18 August 2026  
**Governing decisions:** `DEC.CLAES.FAMILY_ARMS.VOETBOOG.2026-08-16`, `DEC.CORNELIS.SCHUTTERIJ.SINT_JORIS.2026-08-18`, `DEC.CLAES.CORNELIS.VOETBOOG_PEDAGOGY.2026-08-18`  
**Historical substrate:** `SRC-HIST-NISSEPAT-ARMS-MUSCHART-82L-001`, `SRC-HIST-GOES-SCHUTTERIJ-DEGHEYN-001`

This dossier fixes the point where historical family heraldry and historical Goese civic culture meet deliberate fictional biography. The layers must remain distinguishable even when the novel makes them feel continuous.

## 1. Historical family sign

Earlier project research identified CBG/Muschart record `NL-HaCBG_1801_0082_0819`, Nissepat, classification/reference `82L`. The recovered project transcription reads:

> **een voetboog met den langen zwengel links**

The project therefore reads the Nissepat heraldic charge as a **voetboog / crossbow**, not an ordinary handboog.

This is stronger than the later shorthand that treated the lost/damaged heraldic image as leaving two equally open bow types. The project had already reaffirmed the voetboog reading on 18 July 2025.

### Provenance still open

Do not overstate what has been reverified. The following callback details still require direct reinspection of Muschart's source line:

- Jacob Jansz./Janz. Nissepat as exact armiger;
- approximately 1581 as exact date;
- a surviving seal on a charter as the exact underlying object/source;
- the exact mechanism represented by the `lange zwengel`.

The family charge can be used as voetboog while those provenance details remain open.

## 2. Historical Goese guild distinction

Current Goese source synthesis keeps three institutions separate:

- **Sint-Joris / Edele Voetboog** — voetboog/crossbow tradition; devies **`Van Ongenugten Vrij`**;
- **Sint-Sebastiaan** — handboog tradition;
- **Sint-Adriaan / Edele Busse** — firearm/kolvenier tradition.

For this project **Sint-Joris is the relevant guild** for Cornelis' fictional crossbow membership.

Do not swap Sint-Joris and Sint-Sebastiaan merely because later/secondary pages are inconsistent. The governing local schutterij dossier and source bundle preserve the current project distinction.

### Guild topography

The Sint-Joris and Sint-Sebastiaan shooting grounds/hoven lay beside one another on the **south-west side of Goes, south of the church and within the walls**. Modern Kreukelmarkt / Van de Spiegelstraat / Wijngaardstraat references are orientation aids only; do not back-project those modern street labels into Claes' speech without separate period-name evidence.

This makes the voetboog world a plausible ordinary part of Claes' lived city rather than a distant military excursion.

## 3. Fiction begins here: Cornelis

The historical facts do not prove that Cornelis Nissepat existed as a documented schutter or that any historical Nissepat belonged to Sint-Joris.

Novel canon deliberately makes fictional Cornelis:

- a member of the Goese **Sint-Jorisgilde / Edele Voetboog**;
- a practising voetboogschutter within that civic-corporate milieu;
- a father whose guild/weapon practice is visible to Claes.

The logic is resonance, not proof:

**historical Nissepat family sign → historical Goese voetbooggilde → fictional Cornelis in that guild.**

This is the desired fact-fiction loop.

## 4. The familiewapen must exist in the lived story world

The arms should not remain a YAML-only fact. Claes should know the sign materially before he understands what later meaning the reader may attach to it.

Plausible carriers include:

- a seal matrix;
- a wax impression on a family or property document;
- a copied heraldic mark in family papers;
- another modest civic/family object appropriate to non-noble urban heraldry.

The exact carrier is not yet fixed. Do **not** assume the fictional carrier is identical to the historical object behind Muschart.

Avoid presenting the Nissepat family as pseudo-aristocratic merely because it has arms. The sign functions as family identity and documentary continuity, not as proof of noble rank.

## 5. Sign becomes embodied reality

For young Claes the most effective sequence is:

1. he knows or repeatedly sees the family sign;
2. he later recognizes the same basic form in Cornelis' actual voetboog;
3. the visual sign acquires weight, tension, danger, sequence and bodily discipline;
4. only much later can the reader experience the full family/memory resonance.

Cornelis need not explain this relation in dialogue. A line such as “daarom dragen wij die boog” would make the loop too explicit and deterministic.

## 6. Cornelis' bodily pedagogy

The voetboog becomes one of several places where Cornelis teaches Claes through work rather than praise.

Age-appropriate participation can include:

- observing safe handling and the shooting ground;
- carrying harmless equipment or messages;
- counting bolts/targets/turns where plausible;
- keeping clear of the line of fire;
- helping inspect obvious material condition under supervision;
- learning sequence and waiting for permission;
- later, supervised handling or a carefully earned shot if the scene chronology supports it.

No precise historical loading or spanning procedure should be invented without scene-specific evidence.

### Father-son relation

The key emotional mechanism is already canonical:

**Claes does something well → waits for approval → Cornelis checks it → Cornelis entrusts the next harder task.**

For Cornelis, the next task means:

> I trust you.

For Claes, it may mean:

> It was not yet enough.

The voetboog gives that asymmetry physical form without requiring explanatory dialogue.

## 7. Papegaai, schutterskoning and public recognition

Goese schutters practised competitive **papegaaischieten**: shooting at an artificial bird on a high pole. The successful shooter could be recognized as **schutterskoning**.

This is particularly useful because it turns private skill into **publicly judged competence**.

Possible scene functions:

- Claes experiences the wait before each shot and the social reaction afterward;
- a miss is public rather than private;
- a winner receives visible communal recognition;
- Cornelis can compete or simply participate without being made the winner;
- Claes can see that the civic world has clear rituals of praise and status even while his father's praise toward him remains sparse.

### Hard boundary

**Cornelis is not canonically schutterskoning.** Making him win a papegaaischieten requires a separate scene/story decision. Exact prizes, chains, silver birds, rules, distances and ceremonial choreography remain unproven for mid-sixteenth-century Goes unless separately sourced.

## 8. `Van Ongenugten Vrij`

The historical devies of the Goese Sint-Joris / Edele Voetboog is **`Van Ongenugten Vrij`**.

It may recur as an ordinary piece of guild identity known to Cornelis and Claes. Its later irony is powerful precisely because the characters do not explain it:

- before 1554 it can belong simply to a prosperous civic brotherhood and a child's association with his father;
- after fire, separation and Cornelis' death, the words acquire a different resonance for the reader;
- no character needs to declare that Claes is obviously not “free of sorrows”.

Do not invent a specific stone inscription, banner placement, badge or architectural display of the devies without evidence. The phrase is historically attached to the guild; its physical manifestation in a scene remains open.

## 9. Gift and shadow

Crossbow practice reinforces an existing Claes pattern; it does not create it from nothing.

Useful bodily sequence:

**see → prepare → hold tension → wait → choose → release.**

For a disciplined weapon this is useful. In Claes' later life the danger lies in allowing the middle of the sequence to become permanent:

**see → prepare → wait → keep waiting.**

This therefore resonates with his established gift/shadow:

- gift: prolonged precise embodied perception;
- shadow: remaining in observation after action is required.

Do not write the crossbow as an overt psychological metaphor. It must first work as a real dangerous object within real civic practice.

## 10. 1554: the sign can outlive the house

The family home and most of the household are destroyed in novel canon on 18 May 1554. The family sign need not disappear with them.

A plausible heraldic carrier can already be:

- with Cornelis;
- with Claes Jacobsz.;
- among papers or property records stored elsewhere;
- otherwise outside the house before the fire.

This is preferable to a miraculous object rescued from the flames.

The result creates an early material form of a later project principle:

> **a carrier can outlive another carrier, and a sign can remain when the household in which Claes first knew it is gone.**

This is a narrative resonance, not evidence that sixteenth-century Nissepat heraldry was understood philosophically in this way.

## 11. Relation to the wider carrier/content architecture

The motif can later resonate with:

- documents and seals surviving owners;
- Cornelis' testimony surviving Cornelis;
- the memoriaal carrying unseen text;
- print multiplying testimony beyond its first carrier;
- Sol remaining materially present while appearance changes;
- Claes learning that preserving something is not the same as possessing it forever.

The familiewapen is therefore a useful early seed of continuity-through-carriers, but must never be retroactively described as a deliberate coded prefiguration.

## 12. Hard guardrails

1. Nissepat family arms = voetboog/crossbow in current project canon.
2. Recovered Muschart wording includes `lange zwengel`, but exact crossbow subtype remains open.
3. Jacob Jansz./1581/charter-seal provenance remains pending direct source-line verification.
4. Cornelis' Sint-Joris membership is fiction, not archival fact.
5. Sint-Joris = voetboog; Sint-Sebastiaan = handboog; Sint-Adriaan/Edele Busse = firearm in current Goes canon.
6. `Van Ongenugten Vrij` is historically attached to Sint Joris; its exact physical display remains scene-level open.
7. Papegaaischieten and schutterskoning are historically supported; Cornelis winning is not canon.
8. The bow-guild hoven belong south of the church / south-western city in the current topographic synthesis; modern street names are orientation only.
9. No noble-status inference from the existence of family arms.
10. No claim that every Nissepat is a crossbowman.
11. No invented Cornelis guild office or command rank.
12. Claes' childhood weapon participation remains supervised and age-appropriate.
13. The crossbow reinforces Claes' established gift/shadow; it is not the single cause of his personality.
14. Symbolism stays author-side; scenes remain material, relational and civic first.
15. If the Muschart card or its underlying primary source is later recovered directly, update the provenance layer without disturbing the fictional Cornelis decision unless the historical identification itself creates a contradiction.
```

---

# SOURCE FILE: `narrative/claes_cornelis_relationship_refinement_2026-08-18.yaml`

```yaml
schema_version: 1.1.0
kind: RelationshipRefinement
id: REL.CLAES.CORNELIS.REFINEMENT.2026-08-18
status: CANON
participants: [ENT.PERSON.CLAES, ENT.PERSON.CORNELIS]
governs: REL.CLAES.CORNELIS
related_decisions:
- DEC.CLAES.CORNELIS.RECOGNITION.2026-08-18
- DEC.CLAES.CORNELIS.RESPONSIBILITY.2026-08-18
- DEC.CLAES.CORNELIS.RELIGIOUS_DISSONANCE.2026-08-18
- DEC.CLAES.CORNELIS.POSTFIRE_READING.2026-08-18
- DEC.CORNELIS.SCHUTTERIJ.SINT_JORIS.2026-08-18
- DEC.CLAES.CORNELIS.VOETBOOG_PEDAGOGY.2026-08-18
related_motif: MOTIF.NISSEPAT_VOETBOOG
phases:
- label: admiration and apprenticeship
  story_time: {earliest: '1547-01-01', latest_exclusive: '1551-01-01', precision: approximate}
  value_state: dependence -> admiration
  claes_need: be seen and approved by Cornelis
  cornelis_expression: instruction, task, correction, inclusion in practical work
  tension: Claes can mistake functional trust for absence of affection because explicit praise is scarce.
  embodied_contexts:
  - household and trade observation
  - biersteker work
  - Sint-Joris / Edele Voetboog environment at child-safe distance

- label: recognition hunger and delegated responsibility
  story_time: {earliest: '1551-01-01', latest_exclusive: '1554-05-18', precision: approximate}
  value_state: admiration -> striving for earned recognition
  mechanism:
  - Cornelis gives Claes increasingly consequential but age-appropriate tasks.
  - Claes responds by becoming more exact, useful and dependable.
  - Successful performance often produces another task, correction or enlarged responsibility rather than explicit praise.
  paradox: >-
    Claes may believe he is still not good enough because his father rarely praises him, while Cornelis may be increasing responsibility precisely because he trusts him.
  household_role:
  - help Tanneken during Cornelis' absences
  - watch or fetch Jan when appropriate
  - carry or remember instructions and messages
  - count/check simple household or trade items
  - repair or repeat work after mistakes
  voetboog_training:
    story_claim: STC.CLAES.CORNELIS.VOETBOOG_FORMATION.001
    institution: Goese Sint-Jorisgilde / Edele Voetboog
    progression:
    - observe safe handling and shooting-ground discipline
    - carry or count child-safe equipment/tasks
    - learn sequence, clear line and permission to act
    - supervised handling only when age and scene evidence support it
    - a carefully earned shot may occur if separately placed in scene chronology
    relational_function: >-
      Cornelis can communicate trust by granting Claes the next harder responsibility; Claes may experience the same act as another test because explicit praise remains scarce.
    gift_shadow_resonance: 'see -> prepare -> hold tension -> wait -> choose -> release; danger emerges when waiting survives past the moment of required action'
  guardrails:
  - No adult merchant authority and no automatic corporal punishment.
  - Crossbow practice reinforces rather than singularly causes Claes' observer gift/shadow.
  - Exact loading/spanning choreography requires period support per scene.

- label: pre-conceptual religious dissonance
  story_time: {earliest: '1552-01-01', latest_exclusive: '1554-05-18', precision: approximate}
  value_state: shared visible Catholic world -> first unexplained difference
  cornelis_state: Familist/Huis der Liefde affiliation with outward Catholic conformity
  claes_state: ordinary Catholic child-world; no knowledge of the Huis der Liefde
  scene_language:
  - differing attention in church
  - a silence where Claes expects an answer
  - wording that does not match priest/school language exactly
  - a book, visitor or journey Cornelis closes off without explanation
  guardrail: Do not stage an explicit Protestant-versus-Catholic argument.

- label: fire and impossible responsibility
  story_time: {earliest: '1554-05-18', latest_exclusive: '1554-06-01', precision: bounded}
  value_state: useful oldest son -> survivor unable to protect the household
  subjective_wound: >-
    Because Claes had already begun to experience himself as someone who should help carry and watch over the household, the deaths of Tanneken, Jan and the unborn child can feed an irrational sense that he failed a responsibility.
  objective_truth: Claes is not responsible for the fire or deaths.
  heraldic_continuity: >-
    A plausible Nissepat heraldic carrier may survive outside the destroyed household, allowing family sign and name to remain materially present without a miraculous rescue from the flames.

- label: care misread as rejection
  story_time: {earliest: '1554-05-18', latest_exclusive: '1561-09-01', precision: bounded}
  value_state: surviving pair -> loving sacrifice experienced as abandonment
  cornelis_intention: preserve Claes' education and future while rebuilding in Goes
  claes_reading: >-
    The older recognition gap allows Claes to wonder whether being sent away confirms that his father still does not choose him for closeness.
  guardrail: Preserve Cornelis' care and sacrifice; this is not simple abandonment.

- label: old closed doors acquire meaning
  story_time: {earliest: '1561-09-01', latest_exclusive: '1569-11-20', precision: bounded}
  value_state: remembered childhood dissonance -> suspicion and partial understanding
  function: >-
    As Claes later sees Cornelis' dangerous routes, books, papers and loyalties, earlier childhood silences and incongruities retrospectively become meaningful. The adult son discovers that the closed doors he sensed as a child were real, even though he had misunderstood their cause.

terminal_resonance:
  date: '1569-11-19'
  meaning: >-
    Cornelis' execution removes not only the father but the remaining possibility of receiving the explicit recognition, explanation and reconciliation Claes had long wanted.

scene_guardrails:
- Do not explain the recognition dynamic in every scene; let it emerge from task, expectation, response and silence.
- Cornelis may be demanding without being cruel.
- Trust may be expressed as responsibility.
- Claes' precision is both genuine aptitude and, in part, a relational strategy; neither explanation cancels the other.
- Religious dissonance must remain child-scaled before 1554.
- The Nissepat voetboog motif must first function as family heraldry and real weapon practice, not an announced symbol.
```

---

# SOURCE FILE: `narrative/motifs_nissepat_arms_2026-08-18.yaml`

```yaml
schema_version: 1.1.0
kind: MotifRegistryExtension
motifs:
  - id: MOTIF.NISSEPAT_VOETBOOG
    label: Nissepat voetboog / familiewapen
    status: CANON
    historical_substrate:
      family_arms: SC.HIST.NISSEPAT.ARMS.VOETBOOG.001
      goes_guild: SC.HIST.GOES.SCHUTTERIJ.SINT_JORIS_VOETBOOG.001
      guild_devise: SC.HIST.GOES.SCHUTTERIJ.SINT_JORIS.DEVISE.001
      papegaai_practice: SC.HIST.GOES.SCHUTTERIJ.PAPEGAAI.001
      guild_topography: SC.HIST.GOES.SCHUTTERIJ.HOVEN.SOUTHWEST.001
    story_links:
      - STC.NISSEPAT.FAMILY_ARMS.VOETBOOG.001
      - STC.CORNELIS.SCHUTTERIJ.SINT_JORIS.001
      - STC.CLAES.CORNELIS.VOETBOOG_FORMATION.001
      - REL.CLAES.CORNELIS
    progression:
      - label: sign before explanation
        period: childhood before 1554
        function: Claes knows the family charge materially/visually before it carries explicit thematic meaning.
      - label: weapon in father's hands
        period: childhood before 1554
        function: The heraldic shape gains bodily reality through Cornelis' Sint-Joris/voetboog practice.
      - label: tension and permission
        period: childhood formation
        function: Claes learns that seeing a target is not identical to being permitted or ready to act; sequence, control and timing matter.
      - label: public recognition at the papegaai
        period: childhood before 1554
        function: A guild competition can show Claes a civic world in which competence receives visible judgement and a successful shooter may become schutterskoning, sharpening by contrast the sparse verbal recognition he receives from Cornelis.
      - label: recognition through entrusted action
        period: early 1550s
        function: Cornelis' next entrusted task functions as paternal trust while Claes may misread it as another test.
      - label: Van Ongenugten Vrij
        period: childhood onward
        function: The historical Sint-Joris devies begins as ordinary guild identity; later suffering can make its wording resonate differently for the reader without explicit irony in character speech.
      - label: carrier survives rupture
        period: after 18 May 1554
        function: The sign can outlive house and household through a plausible material carrier, preparing the wider carrier/content architecture without mystical explanation.
      - label: mature resonance
        period: later life
        function: Claes' mature problem is not endless aim but choosing and releasing action when responsibility requires it.
    guardrails:
      - First be heraldry, weapon practice and family/civic material culture; symbolism must emerge from use.
      - Do not make the arms proof of nobility, destiny or hereditary martial essence.
      - Do not explain the motif to the reader in authorial exposition.
      - Do not make Sint Sebastiaan the voetboog guild in Goes.
      - Do not canonize Cornelis as schutterskoning without a separate story decision.
      - Do not invent a physical display location for Van Ongenugten Vrij without evidence.
      - Do not require the same physical heraldic object to survive every phase.
      - Do not turn Claes' observer-shadow into a one-cause result of crossbow training.
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
schema_version: 1.6.0
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
  decision_ids:
  - DEC.CLAES.BELOVED.MAYKEN_LAMPERT.2026-08-14
  - DEC.CLAES_MAYKEN.CHILDHOOD_ACQUAINTANCE.2026-08-19
  phases:
  - label: childhood acquaintance in Goes
    story_time: {earliest: '1553-01-01', latest_exclusive: '1554-05-18', precision: approximate}
    value_state: ordinary child acquaintance -> small shared memory
    function: Claes and Mayken know one another through ordinary Goese child contact, play and early plant/material observation. This gives later recognition a real past without turning the children into lovers or foreshadowing destiny.
    guardrails:
    - No childhood romance, childhood-sweetheart framing or predestination.
    - Mayken's curiosity and family work-world exist independently of Claes.
  - label: separate post-fire lives
    story_time: {earliest: '1554-05-18', latest_exclusive: '1566-08-01', precision: approximate}
    value_state: shared city catastrophe -> divergent loss histories and development
    function: Both know the 1554 fire, but Claes' household annihilation and Mayken's family material loss/rebuilding remain distinct. Continuous contact is not required.
  - label: renewed proximity and separate expertise
    story_time: {earliest: '1566-08-01', latest_exclusive: '1570-01-01', precision: bounded}
    value_state: remembered acquaintance + separate expertise -> potential complementarity
    function: Later proximity can carry recognition and rediscovery. Claes brings pattern, memory and secrecy; Mayken has developed material judgement that does not depend on his noticing her.
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
  - Childhood memory may support recognition but must never function as proof of romantic destiny.
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

# SOURCE FILE: `storybible/MANUSCRIPT_PROGRESSION_AND_PARKED_MATERIAL.md`

```markdown
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
```

---

# SOURCE FILE: `narrative/manuscript_progression.yaml`

```yaml
schema_version: 1.0.0
kind: ManuscriptProgressionRegistry
purpose: >-
  Tracks the current manuscript projection separately from canon: what each chapter currently dramatizes, what reader/character progression it now carries after revision, and how that differs from earlier manuscript versions. Canon truth is not deleted merely because prose is cut, and cut prose does not remain an active Narrative Instance merely because it once existed.

status_vocabulary:
  manuscript_state: [PLANNED, DRAFT, CURRENT, REVISE, MERGE_PENDING, CUT_FROM_MANUSCRIPT, SUPERSEDED]
  placement_state: [ACTIVE_HERE, MOVED_ELSEWHERE, PARKED, OFFPAGE_BACKSTORY, OFFPAGE_BACKLINE, BACKDROP_ONLY, DISCARDED]

revision_contract:
  required_fields_after_substantial_editor_pass:
  - chapter_ref
  - manuscript_file
  - revision_date
  - editorial_verdict
  - progression_before
  - progression_after
  - progression_delta
  - functions_retained
  - functions_removed_or_moved
  - parked_material_refs
  - canon_impact
  - downstream_reader_expectation
  rules:
  - "A chapter's current progression describes only what the current manuscript actually delivers."
  - "If a beat is cut, remove that beat/function from the chapter progression even when the underlying Story Claim remains canon."
  - "If material moves to another chapter, the source chapter records MOVED_ELSEWHERE and the receiving chapter must explicitly adopt the function before it is considered active again."
  - "PARKED material is not active manuscript truth or scene placement. It is a reusable editorial asset governed by narrative/parked_material.yaml."
  - "Canon impact must be one of NONE, PROJECTION_ONLY, CANON_REVIEW_REQUIRED. Editorial cutting normally has NONE or PROJECTION_ONLY impact."
  - "Do not infer that an event was removed from story truth merely because its exposition/scene was cut. Check DEC/STC/NI layers separately."

current_manuscript_set:
- chapter_ref: CH.PROLOGUE.DE_BLADZIJDE.1542
  manuscript_file: 1542-12-08-de-bladzijde.md
  story_time: '1542-12-08'
  title: De Bladzijde
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'
  revision_lineage_note: "A shorter post-cold-reader version exists in the 19 August manuscript set; exact progression delta must be recorded from the editor handoff rather than reconstructed from deleted prose alone."

- chapter_ref: CH.DE_DREMPEL.1547
  manuscript_file: 1547-04-01-de-drempel.md
  story_time: '1547-04-01'
  title: De Drempel
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'

- chapter_ref: CH.DE_LEI.1552
  manuscript_file: 1552-01-15-de-lei.md
  story_time: '1552-01-15'
  title: De Lei
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'

- chapter_ref: CH.HET_WAPEN.1553
  manuscript_file: 1553-08-15-het-wapen.md
  story_time: '1553-08-15'
  title: Het Wapen
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'

- chapter_ref: CH.DE_KRAAI.1553
  manuscript_file: 1553-10-01-de-kraai.md
  story_time: '1553-10-01'
  title: De Kraai
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'

- chapter_ref: CH.DE_KRAAN.1553
  manuscript_file: 1553-11-05-de-kraan.md
  story_time: '1553-11-05'
  title: De Kraan
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'

- chapter_ref: CH.DE_WEGEN.1553
  manuscript_file: 1553-12-10-de-wegen.md
  story_time: '1553-12-10'
  title: De Wegen
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'

- chapter_ref: CH.HET_ZAND.1554
  manuscript_file: 1554-01-05-het-zand.md
  story_time: '1554-01-05'
  title: Het Zand
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'

- chapter_ref: CH.HET_GIST.1554
  manuscript_file: 1554-01-15-het-gist.md
  story_time: '1554-01-15'
  title: Het Gist
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'

- chapter_ref: CH.DE_WINNAAR.1554
  manuscript_file: 1554-02-10-de-winnaar.md
  story_time: '1554-02-10'
  title: De Winnaar
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'

- chapter_ref: CH.HET_ZAAD.1554
  manuscript_file: 1554-03-01-het-zaad-in-de-donkere-aarde.md
  story_time: '1554-03-01'
  title: Het Zaad in de Donkere Aarde
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'
  revision_lineage_note: "Substantial shortening occurred in the 19 August editor pass; exact removed functions/material belong in the revision handoff and parked-material registry."

- chapter_ref: CH.DE_KAMER.1554
  manuscript_file: 1554-03-05-de-kamer.md
  story_time: '1554-03-05'
  title: De Kamer
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'

- chapter_ref: CH.DE_WIEG.1554
  manuscript_file: 1554-04-10-de-wieg.md
  story_time: '1554-04-10'
  title: De Wieg
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'

- chapter_ref: CH.DE_LADINGEN.1564
  manuscript_file: 1564-04-04-de-ladingen-van-antwerpen.md
  story_time: '1564-04-04'
  title: De Ladingen van Antwerpen
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'

- chapter_ref: CH.DE_VERKEERDE_KIST.1564
  manuscript_file: 1564-04-14-de-verkeerde-kist.md
  story_time: '1564-04-14'
  title: De Verkeerde Kist
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'

- chapter_ref: CH.DE_KIES_VAN_BOOM.1564
  manuscript_file: 1564-04-22-de-kies-van-boom.md
  story_time: '1564-04-22'
  title: De Kies van Boom
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'

- chapter_ref: CH.DE_LOOG.1564
  manuscript_file: 1564-04-29-de-loog-van-antwerpen.md
  story_time: '1564-04-29'
  title: De Loog van Antwerpen
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'

- chapter_ref: CH.DE_DOOD_VAN_SOL.1564
  manuscript_file: 1564-07-20-de-dood-van-sol.md
  story_time: '1564-07-20'
  title: De Dood van Sol
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'

- chapter_ref: CH.DE_MARKT_VAN_DELFT.1584
  manuscript_file: 1584-07-14-de-markt-van-delft.md
  story_time: '1584-07-14'
  title: De Markt van Delft
  manuscript_state: CURRENT
  latest_known_editor_pass: '2026-08-19'
  revision_lineage_note: "A shorter post-cold-reader version exists in the 19 August manuscript set; exact progression delta should come from the editor handoff."

revision_history: []
```

---

# SOURCE FILE: `narrative/parked_material.yaml`

```yaml
schema_version: 1.0.0
kind: ParkedNarrativeMaterialRegistry
purpose: >-
  Preserves useful material removed during editorial passes without falsely treating it as active manuscript placement or current scene canon. This registry stores summaries and reuse constraints, not a second prose archive.

status_vocabulary:
  - PARKED_FUTURE_CHAPTER
  - PARKED_BACKSTORY
  - PARKED_BACKLINE
  - PARKED_BACKDROP
  - PARKED_MOTIF_RESERVE
  - MOVED_CONFIRMED
  - DISCARDED_PROSE
  - REJECTED_STORY_OPTION

definitions:
  PARKED_FUTURE_CHAPTER: "A written or designed beat may become an on-page scene later, but no destination is yet canonized."
  PARKED_BACKSTORY: "The underlying story event/state remains part of character/history continuity, but need not be dramatized on-page."
  PARKED_BACKLINE: "An off-page causal line continues during the story and may later create plot pressure or consequences."
  PARKED_BACKDROP: "World/sensory/social material may enrich later scenes but carries no required causal event."
  PARKED_MOTIF_RESERVE: "A recurring image/object/phrase/function has been removed here to protect freshness but may recur later if its value has changed."
  MOVED_CONFIRMED: "The material/function has a named receiving chapter/scene and is no longer merely parked."
  DISCARDED_PROSE: "The prose is retired; underlying canon must be checked separately."
  REJECTED_STORY_OPTION: "The proposed event/interpretation itself is rejected and must not return unless reopened by an explicit author decision."

hard_rules:
- "Parking prose never makes the parked scene/event canon by itself."
- "Cutting prose never deletes an existing DEC/STC/ENT/REL/ARC fact by itself."
- "Every parked item must say whether its underlying story truth is CANON, OPEN, PROPOSED or NONE/ATMOSPHERIC."
- "A parked item cannot be silently restored into prose. Before reuse, check current canon, chronology, character knowledge and whether another chapter now performs the same function."
- "If restored, record the new receiving chapter/scene and change status to MOVED_CONFIRMED."
- "Do not store large verbatim cut passages here. Store a concise content/function summary plus a pointer to the originating manuscript/editor handoff when available."
- "Material parked as BACKDROP may be distributed in fragments; it should not be resurrected as an exposition block merely because it was once written as one."
- "Motif reserve requires changed value on recurrence; repetition of the same symbolic beat is not reuse justification."

items:
- id: PARK.EARLY_GOES.FIRST_STEPS_HOME.001
  status: PARKED_FUTURE_CHAPTER
  origin_context: early Goes childhood development, pre-current 1547 opening
  summary: "A first-steps/home scene was previously judged internally strong but left without a current chapter placement."
  underlying_story_truth: PLAUSIBLE_FICTION_SPACE
  possible_functions: [embodied_childhood, intact_household, Tanneken_Cornelis_parenting]
  reuse_guardrail: "Do not add merely to make childhood fuller; reuse only if a later structural gap requires a distinct function not already carried by De Drempel and the 1552–1554 cluster."

- id: PARK.EARLY_GOES.VASTENAVOND_MARKET.001
  status: PARKED_BACKDROP
  origin_context: early Goes childhood development
  summary: "A written Vastenavond/market passage was removed from the active early chapter despite working aesthetically."
  underlying_story_truth: NONE_ATMOSPHERIC_UNLESS_SEPARATELY_CANONIZED
  possible_functions: [Goese_urban_life, sensory_city, feast_calendar, crowd_world]
  reuse_guardrail: "Reuse as distributed city texture or only if a later scene earns the feast as causal pressure; do not restore as a standalone picturesque scene by default."

- id: PARK.PROLOGUE.EXPLICIT_BIRTH_DATE_LINK.001
  status: REJECTED_STORY_OPTION
  origin_context: early prologue/childhood development
  summary: "An explicit symbolic birth-scene/date linkage between Claes and the Las Casas/Brevísima line was rejected as too direct."
  underlying_story_truth: REJECTED
  reuse_guardrail: "Do not restore an explicit destiny/date-link device. The later relation is testimony/transmission/responsibility, not shared-date symbolism."

editor_pass_ingest_queue:
  status: OPEN_INGEST
  note: >-
    The 19 August 2026 Claude cold-reader/editor pass produced additional CUT/PARK decisions across the current manuscript. The latest and prior chapter files are available in the conversation, but exact author/editor classifications of each removed beat should be imported from the Claude editor handoff rather than guessed solely from textual diff. For every such item create one PARK.* record and one revision_history entry in narrative/manuscript_progression.yaml.
```

---

# SOURCE FILE: `narrative/domain_scene_packs.yaml`

```yaml
schema_version: "1.1.0"
kind: DomainScenePackRegistry
purpose: "Machine-readable retrieval bridge from historical domains to chapter/scene construction. Packs constrain world state; they do not create fictional scenes or participation unless an explicit Story Claim/Decision is linked."
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
    label: "Goes — Sint Joris / shooting guild / civic defence context"
    status: AUTHORING_READY_SCENE_CONTEXT
    world_modules: [WORLD.GOES, WORLD.SCHUTTERIJ_MILITARY]
    detail_files:
      - storybible/domains/SCHUTTERIJ_MILITARY_PRACTICE_1550_1607.md
      - storybible/NISSEPAT_ARMS_SINT_JORIS_CORNELIS.md
    source_claims:
      - SC.HIST.GOES.SCHUTTERIJ.SINT_JORIS_VOETBOOG.001
      - SC.HIST.GOES.SCHUTTERIJ.FIREARM_GUILD.16C.001
      - SC.HIST.NISSEPAT.ARMS.VOETBOOG.001
    story_claims:
      - STC.CORNELIS.SCHUTTERIJ.SINT_JORIS.001
      - STC.CLAES.CORNELIS.VOETBOOG_FORMATION.001
    canonical_cornelis_institution: "Sint-Jorisgilde / Edele Voetboog"
    motif: MOTIF.NISSEPAT_VOETBOOG
    youth_action_chain: [observe, clear_line, wait_permission, count_or_carry_child_safe_items, inspect_under_supervision, prepare, hold_tension, choose, release_if_scene_earned]
    categories_to_keep_separate: [Sint_Joris_voetboog, Sint_Sebastiaan_handboog, Sint_Adriaan_firearm, civic_watch, garrison_professionals, later_standardized_drill]
    relational_function: "Cornelis expresses trust by enlarging responsibility; Claes may misread the next task as proof that he still has not earned explicit recognition."
    hard_guardrails:
      - "Cornelis membership is story canon, not archival fact"
      - "Sint Sebastiaan is not the voetboog guild"
      - "no Cornelis guild office without separate decision"
      - "no exact zwengel/cranequin subtype without scene-specific evidence"
      - "1516/1530 firearm-guild date conflict preserved"
      - "no later equipment automatically in 1572"

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
schema_version: 1.1.0
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

- id: GRD.EDITORIAL.CLUSTER_NECESSITY
  type: EditorialGate
  status: ACTIVE_AUTHORING_POLICY
  question: "Does the chapter/scene still add a distinct progression when the surrounding cluster is read as one experience?"
  tests:
  - "Has Claes already learned or enacted substantially the same lesson in the preceding cluster?"
  - "Is this a new relationship movement, or the same relationship beat in a different setting?"
  - "Has the same motif recently carried the same dramatic value rather than a transformed value?"
  - "Does the chapter change forward pressure, or merely deepen a state the reader already understands?"
  - "Would removing this unit make the cluster causally, emotionally or cognitively poorer rather than only shorter?"
  rule: "A scene/chapter may pass local necessity and still receive MERGE or CUT because cumulative repetition weakens the book-level progression."

- id: GRD.EDITORIAL.CUT_DISPOSITION
  type: EditorialGate
  status: ACTIVE_AUTHORING_POLICY
  question: "What happens to the material/function after RETAIN/REVISE/MERGE/CUT?"
  required_after_substantial_edit:
  - "Update narrative/manuscript_progression.yaml with progression_before, progression_after and progression_delta."
  - "For every removed function, classify it as deleted, moved, parked future chapter, backstory, backline, backdrop or motif reserve."
  - "Create/update PARK.* records in narrative/parked_material.yaml for reusable removed material."
  - "State canon impact separately: NONE, PROJECTION_ONLY or CANON_REVIEW_REQUIRED."
  - "If material is moved, name both source and receiving chapter/scene; until the receiving unit explicitly adopts it, treat it as PARKED rather than active."
  guardrails:
  - "CUT is an editorial verdict, not automatic de-canonization."
  - "Parked prose is not active manuscript placement."
  - "Do not restore cut material merely because it is historically rich or beautifully written. Reuse must pass scene and cluster necessity again."
  - "Do not store long verbatim deleted passages in the Storybible; store summary, function, provenance and reuse constraints."

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
  - cluster_necessity
  - fatal_or_primary_problem
  - causality_and_character
  - pacing_and_reader_experience
  - prose_quality
  - continuity_or_historical_risk
  - retain_revise_merge_cut
  - cut_disposition_and_progression_update
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
**Decisions:** `DEC.CLAES.BELOVED.MAYKEN_LAMPERT.2026-08-14`, `DEC.CLAES_MAYKEN.CHILDHOOD_ACQUAINTANCE.2026-08-19`  
**Historical source dossier:** `sources/SRC-HIST-GOES-LAMPERT-APOTHECARY-001.md`

This dossier is the detailed authority for the identity and historical embedding of the character formerly labeled only **geliefde / apothekersdochter**. It is synchronized to the later no-cipher memoriaal decision: Mayken is not a cryptographic solver and no special Dodoens carrier is required.

## 1. Canonical identity

**Mayken Adriaensdr. Lampert**, usually simply **Mayken**, is a fictional Goese woman born approximately in **1546**. In juridical-style naming she may appear as **Mayken Adriaens**, **Mayken Adriaensdochter** or, in project metadata, **Mayken Adriaensdr. Lampert**.

She is canonically:
- Claes' beloved and later partner;
- daughter of **Adriaen Jacobsz. Lampert** in novel genealogy;
- granddaughter of the older Goese apothecary **Jacob/Jacop Lampart/Lambert** and the historical household figure **Merricken** in novel genealogy;
- raised in a material/apothecary environment in Goes;
- approximately three to four years younger than Claes;
- already known to Claes as a child before the fire of 18 May 1554, without childhood-romance framing.

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
- Mayken and Claes know one another as children before 18 May 1554;
- Mayken becomes Claes' beloved;
- her precise childhood experiences, education and later relationship biography.

No currently searchable transport act identifies a historical daughter of Adriaen. This is absence of evidence in a property corpus, not evidence of absence.

## 3. Why the name Mayken

A **Mayken**, explicitly `huisvrouw Jacop Lampart`, occurs in the direct historical Lampart environment in 1543. The project reuses an attested family-environment name for the fictional daughter.

Do **not** claim this proves a grandmother-to-granddaughter naming pattern. The archive also uses **Merricken** for the wife of Jacop/Jacob the apothecary. Whether Mayken and Merricken are the same woman, variant forms, successive wives or different households remains unresolved.

## 4. Age, chronology and childhood acquaintance

Working birth: **ca. 1546, Goes**.

- 18 May 1554: about seven or eight;
- 1561: about fourteen or fifteen;
- 1566: about nineteen or twenty;
- 1570: about twenty-three or twenty-four;
- 1584: about thirty-seven or thirty-eight;
- 1602: mid-fifties.

The age gap with Claes is roughly three to four years.

Under `DEC.CLAES_MAYKEN.CHILDHOOD_ACQUAINTANCE.2026-08-19`, they **do know one another before the fire**. The childhood connection is intentionally small-scale and ordinary: child contact in Goes, play, and early moments in which Mayken's way of recognizing plants/material differences becomes visible to Claes.

This is not a childhood-love story. The adult relation may carry recognition and rediscovery, but not predestination, “first love” mythology or the suggestion that the children already understood their later bond.

## 5. Shared fire, different loss

Mayken and Claes are both children of Goes who know the 1554 catastrophe, but they must **not** receive identical trauma biographies.

Claes loses Tanneken, Jan, the unborn sibling, the family home and then daily life with Cornelis. Mayken's historical anchor is different: the Lampert property **de Zwaene** is documented as a normal property before the fire and as a burned house in January 1555.

Novel function:
- Mayken remembers the fire as a child;
- her family experiences material disruption and rebuilding;
- her core household does not need to be annihilated;
- she therefore knows destruction but also knows that a material world can be rebuilt and worked in again.

This difference is essential. She is not Claes' trauma duplicate. She carries a counter-memory: fire can destroy, yet hands can return to work.

## 6. Apothecary formation and character method

Mayken grows up around practical materia medica and apothecary work. Her expertise is embodied and operational rather than academic:
- recognizing plant material by form, smell, texture and condition;
- drying, storing, sorting and preparing substances;
- weighing and measuring;
- distinguishing contamination, substitution and deterioration;
- reading or using practical lists, recipes and botanical reference works;
- knowing that names, materials and preparations can diverge.

Ordinary Dodoens use can belong naturally to this world where historically appropriate. It no longer has any special cipher, nomenclator or key function.

Her governing character value is **material fidelity**. Her habitual questions are closer to “what is it?”, “in what condition?”, “what changed?” and “what would show that we are wrong?” than to Claes' attraction to wider hidden patterns.

That strength also has a shadow: Mayken may become impatient with a hypothesis, symbolic relation or human meaning that cannot yet be materially demonstrated. Her empiricism is a necessary counterweight to Claes, not an automatically superior epistemology.

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

`REL.CLAES.BELOVED` / `REL.CLAES.MAYKEN.CONJUNCTIO` is the relationship **Claes ↔ Mayken**.

Dynamic:

**childhood acquaintance with separate Goese lives → separation/different fire aftermaths → later recognition and material proximity → collaborative verification → earned trust → love without possession → sensory/spiritual companionship.**

Mayken must never function merely as a reward for Claes' suffering or as a therapist. She has her own competence, history and judgement. She can contradict Claes because she knows things he does not.

Their epistemologies differ:
- Claes tends toward pattern, hidden order, memory, abstraction and prolonged observation;
- Mayken tests matter directly and trusts trained sensation, repeatability and practical contradiction.

Her presence later on the road toward Enkhuizen helps Claes recover the *sinne* because she draws him back into matter: smell, weather, touch, plants, preparation, food, fatigue, sound and shared physical travel. The recovery remains Claes' own work.

The mature relation must allow the reverse influence as well: Claes can sometimes see a relation or possibility before Mayken believes it materially established. Their strongest scenes should therefore produce reciprocal revision rather than one person permanently correcting the other.

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
5. Claes and Mayken know one another before the 1554 fire, but are **not** childhood sweethearts.
6. Ordinary Dodoens use is allowed; the retired special Dodoens carrier is not.
7. Mayken shares the 1554 fire horizon with Claes but not his exact losses.
8. She contributes to Claes' recovery; she does not perform or complete it for him.
9. She may assist the direct chemical reveal, but she is not a cryptographic key-holder or decoder.
10. Material verification is her strength and may also become her limitation; do not write her as an infallible corrective to Claes.
11. Load `storybible/CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md` for stable character behaviour and shadow.
```

---

# SOURCE FILE: `narrative/mayken_independent_arc.yaml`

```yaml
schema_version: 1.1.0
kind: NarrativeArcExtension
records:
- id: ARC.MAYKEN.LIFE
  type: CharacterArc
  label: "Mayken — material competence, independent judgement and relation without absorption"
  canon_status: CANON
  protagonist: ENT.PERSON.BELOVED
  decision_id: DEC.MAYKEN.INDEPENDENT_ARC.2026-08-16
  relationship_decision_id: DEC.CLAES_MAYKEN.CHILDHOOD_ACQUAINTANCE.2026-08-19
  identity_note: "ENT.PERSON.BELOVED is the legacy entity ID for the resolved character Mayken Adriaensdr. Lampert. Identity is not open."

  phases:
  - id: ARC.MAYKEN.LIFE.P01
    label: "Kind van een werkende materiële wereld"
    story_time: {earliest: '1546-01-01', latest_exclusive: '1554-05-18', precision: approximate}
    fixed_state:
    - "Mayken grows up in the fictional daughter-line of the historically anchored Lampert apothecary environment."
    - "Her formation is practical: plants, substances, storage, weight, condition, preparation and names that may not match matter perfectly."
    - "Before the 1554 fire she knows Claes as an ordinary Goese child acquaintance/friend through play and early plant/material observation; this is not childhood romance."
    value_movement: "dependence -> trained attention"
    contrast_with_claes: "Claes is drawn toward hidden order and pattern; Mayken begins with whether the thing in her hand is actually what someone says it is."
    relationship_guardrail: "The childhood acquaintance may seed later recognition, never predestination or a waiting-for-Claes identity."

  - id: ARC.MAYKEN.LIFE.P02
    label: "Brand, verlies en herstel"
    story_time: {earliest: '1554-05-18', latest_exclusive: '1566-01-01', precision: approximate}
    fixed_state:
    - "The Lampert property De Zwaene belongs to Mayken's fictional childhood fire horizon and is historically documented as burned property after 1554."
    - "Her household is not annihilated like Claes' household."
    - "Claes and Mayken follow separate post-fire lives; continuous contact is not required."
    value_movement: "material security -> damaged continuity -> rebuilding competence"
    function: "Mayken learns a counter-truth to Claes' wound: destruction is real, but damaged material life can sometimes be sorted, repaired, replaced and worked again."
    guardrail: "Do not make this a lesser version of Claes' trauma, invent identical bereavements or turn childhood acquaintance into continuous off-screen romance."

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
    - "Do not make Mayken's independence begin only when Claes notices or re-encounters her."

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
schema_version: 1.1.0
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
  - DEC.CLAES_MAYKEN.CHILDHOOD_ACQUAINTANCE.2026-08-19
  identity_note: "ENT.PERSON.BELOVED is Mayken Adriaensdr. Lampert; the legacy entity ID does not indicate an open identity."
  arcs:
  - ARC.CLAES.SINNE_RECOVERY
  - ARC.MAYKEN.LIFE
  - ARC.CLAES.GREAT_WORK.AUTHORIAL

  movement:
  - phase: "childhood acquaintance"
    story_time: {earliest: '1553-01-01', latest_exclusive: '1554-05-18', precision: approximate}
    claes: "older child already inclined toward pattern, game and comparison"
    mayken: "younger child from an apothecary/material environment already learning to distinguish plant and material differences"
    relation: "ordinary Goese acquaintance/friendship through play and looking; enough shared memory for later recognition, explicitly not childhood romance"
    guardrails:
    - "No predestination or childhood-sweetheart framing."
    - "Mayken's own curiosity and family work-world must exist independently of Claes."
  - phase: "separate post-fire lives"
    story_time: {earliest: '1554-05-18', latest_exclusive: '1566-08-01', precision: approximate}
    relation: "shared city catastrophe but divergent losses and development; no requirement for continuous contact"
    guardrail: "Do not turn Mayken into Claes' trauma duplicate or assume an uninterrupted childhood bond."
  - phase: "separate expertise"
    story_time: {earliest: '1566-08-01', latest_exclusive: '1570-01-01', precision: bounded}
    claes: "pattern, memory, hidden order, inherited secrecy"
    mayken: "materia medica, condition, measurement, repeatability, direct contradiction"
    relation: "renewed proximity/recognition without fusion; each can know something the other cannot"
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
  - "If childhood memory is invoked, does it create recognition rather than destiny?"

  guardrails:
  - "Conjunctio is an author-side structural function, not mandatory in-world terminology."
  - "Mayken is not a reward, therapist, saint, decoder or missing ingredient."
  - "Claes is not entitled to Mayken because he suffers or completes the Work."
  - "Difference must remain visible after union; sameness would destroy the function of the relationship."
  - "Childhood acquaintance is canon; childhood romance is not."
```

---

# SOURCE FILE: `narrative/beloved_recovery.yaml`

```yaml
schema_version: 1.1.0
kind: NarrativeRelationshipExtension
records:
- id: REL.CLAES.BELOVED.RECOVERY
  type: RelationshipExtension
  label: Claes and Mayken — recovery companionship
  status: CANON_RESOLVED_IDENTITY
  participants:
  - ENT.PERSON.CLAES
  - ENT.PERSON.BELOVED
  identity: "Mayken Adriaensdr. Lampert"
  identity_status: RESOLVED
  parent: REL.CLAES.BELOVED
  decision_ids:
  - DEC.CLAES.SINNE.2026-08-13
  - DEC.CLAES.BELOVED.MAYKEN_LAMPERT.2026-08-14
  - DEC.MAYKEN.INDEPENDENT_ARC.2026-08-16
  - DEC.CLAES_MAYKEN.CONJUNCTIO.2026-08-16
  - DEC.CLAES.ROSE_JOURNEY.2026-08-16
  - DEC.MAYKEN.ROSE_MATERIA_MEDICA.2026-08-16
  story_function: "On the road toward Enkhuizen, Claes and Mayken's companionship catalyses Claes' rediscovery of the sinne while Mayken remains an independently motivated adult whose own material judgement, work and limits continue to matter. The author-side Tocht der Rozen may make this recovery sensorially recurrent: trust/faith at departure, hope in the duration of travel, and love becoming caritas through concrete responsibility toward another person."
  boundaries:
  - "Mayken accompanies and catalyses; she does not solve or perform Claes' inner transformation for him."
  - "Her identity is fixed. What remains open is the exact mid-arc family/work trajectory and some relationship chronology, not who she is."
  - "Love matures toward relation without possession."
  - "Mayken must retain an objective, judgement or cost of her own in developed scenes."
  - "The rose symbolism remains author-side and must be dramatized rather than explained."
  - "Rose-based care must remain historically bounded and may not function as miraculous modern medicine."
  arc: ARC.CLAES.SINNE_RECOVERY
  counterpart_arc: ARC.MAYKEN.LIFE
  relationship_projection: REL.CLAES.MAYKEN.CONJUNCTIO
  authorial_architecture: ARC.CLAES.GREAT_WORK.AUTHORIAL
  motif_projection: MOTIF.ROSES.FIDES_SPES_CARITAS
  location_anchor: ENT.LOC.ENKHUIZEN
  ko_targets:
  - KO.RELATIONSHIP
  - KO.CHARACTER
  - KO.VALUE
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

# SOURCE FILE: `canon/DECISIONS_CHARACTER_WEB_2026-08-19.yaml`

```yaml
schema_version: 1.0.0
kind: CanonDecisionRegistryExtension
decisions:
- id: DEC.HISTORICAL_GAPS.FICTIONAL_CHARACTERIZATION.2026-08-19
  type: AuthoringDecision
  status: CANON
  decision: >-
    Absence of historical evidence is not a prohibition on fictional specification. When a recurring person, place, object or practice requires stable characterization for the novel, an evidentiary gap may be filled deliberately as fiction canon, provided that no known evidence is contradicted, the choice is historically plausible, its fictional status is explicit, and source-backed fact remains separately labelled.
  rationale: >-
    Documentary silence often defines the legitimate imaginative space of historical fiction. Leaving every unknown unspecified produces unstable or faceless recurring characters; silently presenting invention as fact corrupts provenance. The project therefore distinguishes historical uncertainty from authorial freedom and records approved fictional fills for continuity.
  affects:
  - AUTHORING_POLICY.md
  - storybible/CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md
  guardrails:
  - Historical UNKNOWN remains UNKNOWN in the evidence layer even when the novel fixes a fictional answer.
  - Fiction canon may not be cited or phrased as archival fact.
  - A new historical source that conflicts with a fictional fill triggers review; it does not silently rewrite canon.
  - Do not fill gaps merely because they exist; the detail should carry continuity, character, causal, spatial or reader-experience value.

- id: DEC.CHARACTER_WEB.ARCHETYPAL_LENS.2026-08-19
  type: AuthorialArchitectureDecision
  status: CANON
  decision: >-
    The core Claes cast uses archetypal functions as an author-side character-web lens, never as in-world labels or complete character definitions. Each archetypal function must be individualized through concrete habits, values, contradictions, relationships and a shadow tendency that can create pressure or error.
  affects:
  - narrative/character_web_archetypes.yaml
  - entities/CHARACTERIZATION_2026-08-19.yaml
  - storybible/CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md
  guardrails:
  - Do not make characters explain their archetypal function.
  - Do not force every person into an archetype.
  - Archetypal function does not replace historical biography, motive, desire, class, confession, work or material circumstance.
  - The character web exists to generate contrast and pressure, not to turn supporting characters into symbolic furniture.

- id: DEC.CHARACTER_WEB.CORE_CAST.2026-08-19
  type: CharacterizationDecision
  status: CANON
  decision: >-
    The recurring core cast is differentiated by a stable authorial character web: Claes as seeker/observer/witness moving toward integration; Cornelis as father-law/steward and gatekeeper; Tanneken as embodied household wisdom and care; Jan as brother-double and action principle; Puttus as teacher of word, distinction and interpretation; Mayken as independent material counterpart and later conjunctio-partner; John Dee as magician/transformative mentor whose insight risks overpatterning and control; Willem Silvius as mediator, printer and pragmatic transmission principle; and Bartolome de las Casas as witness/conscience whose testimony must leave his control.
  affects:
  - entities/CHARACTERIZATION_2026-08-19.yaml
  - narrative/character_web_archetypes.yaml
  - storybible/CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md
  guardrails:
  - These functions are authorial lenses, not one-word personality summaries.
  - Every core character retains desire, agency and contradiction outside Claes' immediate development.
  - No character exists only to deliver the thematic lesson named by the web.

- id: DEC.PUTTUS.FICTIONAL_CHARACTERIZATION.2026-08-19
  type: CharacterizationDecision
  status: CANON
  decision: >-
    Because Puttus' historical age, appearance and 1550s teaching-room details are undocumented, the novel may fix a distinct fictional characterization without changing that evidence status. In fiction canon Claes finds Puttus' age hard to estimate; Puttus rarely raises his voice, corrects precisely and economically, often lets silence carry discipline, handles his small book collection with care, and teaches in a sparse, typically cold small room whose exact historical location is deliberately not claimed.
  affects:
  - ENT.PERSON.NICOLAES_PUTTUS
  - entities/GOES_PUTTUS_1512_1554.yaml
  - storybible/GOES_SCHOOLING_PUTTUS_1550_1554.md
  - storybible/CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md
  guardrails:
  - The characterization is FICTION_CANON, not recovered biography.
  - Do not infer or publish a historical birth year, age, death year or exact Goese school building from the characterization.
  - Puttus' quiet discipline may wound or shame as well as teach; he is not an infallible humanist sage.
  - Puttus remains pedagogical/humanist rather than a convenient proto-Protestant oracle.

- id: DEC.CLAES_MAYKEN.CHILDHOOD_ACQUAINTANCE.2026-08-19
  type: RelationshipDecision
  status: CANON
  decision: >-
    Claes and Mayken Adriaensdr. Lampert know one another in Goes before the fire of 18 May 1554. Their childhood relationship is an acquaintance/friendship formed through ordinary child contact, play and Mayken's early material/botanical way of looking; it is not childhood romance. Their later adult relationship can therefore contain recognition and rediscovery rather than a wholly first encounter.
  affects:
  - ENT.PERSON.BELOVED
  - REL.CLAES.MAYKEN.CONJUNCTIO
  - entities/MAYKEN_LAMPERT.yaml
  - storybible/MAYKEN_LAMPERT.md
  - storybible/CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md
  guardrails:
  - No predestination, childhood-sweetheart framing or retroactive romantic destiny.
  - Mayken's childhood scenes must preserve her own curiosity, work-world and judgement.
  - Shared exposure to the 1554 fire does not give Claes and Mayken identical loss biographies.
```

---

# SOURCE FILE: `canon/DECISIONS_CLAES_CORNELIS_RELATION_2026-08-18.yaml`

```yaml
schema_version: 1.0.0
kind: CanonDecisionRegistryExtension
decisions:
- id: DEC.CLAES.CORNELIS.RECOGNITION.2026-08-18
  type: CanonDecision
  status: CANON
  decision: >-
    Before the 1554 fire, Claes admires Cornelis and actively longs for his recognition. Cornelis does love and trust his son, but he expresses that love primarily through instruction, work, responsibility, material provision and investment in Claes' education rather than frequent verbal praise. Claes does not automatically experience those functional acts as recognition and therefore increasingly tries to earn approval by being useful, precise and dependable.
  affects:
  - REL.CLAES.CORNELIS
  - ARC.CLAES.CORNELIS
  - ARC.CLAES.LIFE.P02
  - storybible/CLAES_CORNELIS_RELATION_1547_1569.md
  guardrails:
  - Cornelis is not canonically cold, loveless or contemptuous.
  - Recognition scarcity is relational asymmetry, not proof that Cornelis does not value Claes.
  - Do not make this a separate replacement core wound; it is a relational pressure that feeds Claes' existing attention/control vulnerability.

- id: DEC.CLAES.CORNELIS.RESPONSIBILITY.2026-08-18
  type: CanonDecision
  status: CANON
  decision: >-
    As Claes grows older, especially in the early 1550s, Cornelis increasingly entrusts him with age-appropriate household and small trade responsibilities, including tasks that matter while Cornelis is away on journeys. Claes can experience himself as the oldest son who must help carry the household, watch over Jan, remember or deliver instructions, count or check simple things, and assist Tanneken. Failure has real consequences, but no specific corporal-punishment regime is canonized.
  affects:
  - REL.CLAES.CORNELIS
  - REL.CLAES.BROTHER
  - storybible/FAMILY_CLAES_1542_1554.md
  - storybible/CLAES_CORNELIS_RELATION_1547_1569.md
  guardrails:
  - Responsibilities must remain plausible for Claes' age and status; do not turn an eleven-year-old into an adult merchant or head of household.
  - Consequences may include correction, repetition, extra work, loss of trust, practical repair or visible cost; corporal punishment is not implied unless separately decided.
  - Claes' later guilt about the fire may include the subjective sense that he was supposed to help protect the household, but the story must not make him objectively responsible for the deaths.

- id: DEC.CLAES.CORNELIS.RELIGIOUS_DISSONANCE.2026-08-18
  type: CanonDecision
  status: CANON
  decision: >-
    From approximately 1552-1553, while Claes still inhabits the ordinary Catholic child-world of Goes, he begins to notice small unexplained differences in Cornelis' attention, silences, wording and reactions within that same outward Catholic environment. Claes does not know that Cornelis has entered the Huis der Liefde. The tension is therefore pre-conceptual religious dissonance, not an explicit Protestant-versus-Catholic father-son argument.
  affects:
  - REL.CLAES.CORNELIS
  - ENT.PERSON.CORNELIS
  - DEC.CORNELIS.HOUSE_OF_LOVE.PRE_FIRE_AFFILIATION.2026-08-16
  - DEC.CORNELIS.HOUSE_OF_LOVE.OUTWARD_CONFORMITY.2026-08-16
  - storybible/CLAES_CORNELIS_RELATION_1547_1569.md
  guardrails:
  - Do not call Cornelis simply Protestant in this period; current canon is Familist/Huis der Liefde with outward Catholic conformity.
  - Claes does not identify the movement, doctrine or network before later evidence gives him reason to do so.
  - Do not turn every church scene into coded suspicion; the dissonance should remain intermittent and child-scaled.

- id: DEC.CLAES.CORNELIS.POSTFIRE_READING.2026-08-18
  type: CanonDecision
  status: CANON
  decision: >-
    The established post-fire separation gains an additional relational layer: Cornelis' decision to preserve Claes' education by sending him to Reimerswaal is one of his strongest acts of care, while Claes can also read it through the older recognition gap as evidence that he is still not the son his father wants near him. This interpretation is Claes' wounded reading, not Cornelis' intention.
  affects:
  - DEC.CLAES.POSTFIRE_FATHER_SON.2026-08-14
  - REL.CLAES.CORNELIS
  - ARC.CLAES.CORNELIS
  - storybible/CLAES_CORNELIS_RELATION_1547_1569.md
  guardrails:
  - Preserve both truths: Cornelis sacrifices to protect Claes' future; Claes experiences separation as another loss.
  - Do not flatten the relationship into abuse or simple abandonment.
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

# SOURCE FILE: `canon/DECISIONS_NISSEPAT_ARMS_SINT_JORIS_2026-08-18.yaml`

```yaml
schema_version: 1.0.0
kind: CanonDecisionRegistryExtension
decisions:
  - id: DEC.CLAES.FAMILY_ARMS.VOETBOOG.2026-08-16
    type: CanonDecision
    status: CANON
    amended_on: '2026-08-18'
    decision: >-
      The Nissepat family arms are read in project canon as showing a voetboog (crossbow), not an ordinary handboog. The 18 August refinement restores the stronger recovered evidence basis: earlier project transcription of CBG/Muschart record NL-HaCBG_1801_0082_0819 / 82L reads "een voetboog met den langen zwengel links". The decision is therefore not framed as an arbitrary choice between two equally unreadable bow types.
    affects:
      - ENT.PERSON.CORNELIS
      - MOTIF.NISSEPAT_VOETBOOG
      - STC.CORNELIS.SCHUTTERIJ.SINT_JORIS.001
      - NI.SCENE.SOWER.1554.001
    evidence_basis:
      - SC.HIST.NISSEPAT.ARMS.VOETBOOG.001
      - SC.HIST.NISSEPAT.ARMS.ZWENGEL.001
    historical_boundary:
      - The exact original armiger, ca.1581 callback date and underlying seal/charter source remain pending direct reinspection of Muschart's source line.
      - The family arms do not prove that every Nissepat practised crossbow shooting.
      - The exact historical spanning mechanism represented by the zwengel remains unresolved.
    supersedes_open_note: >-
      Closes the old handboog-versus-voetboog uncertainty at project-canon level. Remaining research concerns provenance, armiger/date and exact crossbow subtype, not the project's heraldic charge reading.

  - id: DEC.CORNELIS.SCHUTTERIJ.SINT_JORIS.2026-08-18
    type: CanonDecision
    status: CANON
    decision: >-
      In novel canon Cornelis is a member of the Goese Sint-Jorisgilde / Edele Voetboog. This is deliberate fictional biography grounded in a real Goese crossbow-guild institution and made to resonate with the source-supported Nissepat family arms. Sint Sebastiaan remains the separate Goese handbow tradition; Sint Adriaan / Edele Busse remains the separate firearm/kolvenier tradition.
    affects:
      - ENT.PERSON.CORNELIS
      - REL.CLAES.CORNELIS
      - ARC.CLAES.CORNELIS
      - MOTIF.NISSEPAT_VOETBOOG
      - PACK.GOES.SCHUTTERIJ
      - STC.CORNELIS.SCHUTTERIJ.SINT_JORIS.001
      - STC.CLAES.CORNELIS.VOETBOOG_FORMATION.001
    rationale: >-
      The connection creates a fact-fiction loop without falsifying the historical record: a real Nissepat heraldic voetboog and a real Goese Edele Voetboog/Sint Joris institution become the substrate for fictional Cornelis' personal membership. Through Cornelis, the crossbow also becomes one bodily arena in which Claes learns attention, tension, waiting, precision and the obligation to choose the moment of action.
    guardrails:
      - Cornelis' personal membership is novel canon, not archival attestation.
      - Do not infer his office, deanship or military command from membership.
      - Do not call his guild Sint Sebastiaan; in current Goes canon Sint Sebastiaan is the handbow guild.
      - Do not make heraldry a deterministic family destiny or claim all Nissepat men were crossbowmen.
      - Do not force Claes to become a full guild member or skilled adult crossbowman in childhood.

  - id: DEC.CLAES.CORNELIS.VOETBOOG_PEDAGOGY.2026-08-18
    type: CanonDecision
    status: CANON
    decision: >-
      Cornelis' voetboog practice becomes one recurring embodied teaching environment in Claes' childhood. Age-appropriate participation may progress from carrying, observing, counting, target-ground discipline and equipment care toward supervised handling, spanning/ranging tasks and eventually a carefully earned shot where scene chronology permits. Cornelis often expresses trust by granting the next responsibility rather than by verbal praise.
    affects:
      - REL.CLAES.CORNELIS
      - ARC.CLAES.CORNELIS
      - MOTIF.NISSEPAT_VOETBOOG
      - STC.CLAES.CORNELIS.VOETBOOG_FORMATION.001
    narrative_function: >-
      The footbow gives bodily form to Claes' established gift/shadow: perception, controlled tension, waiting and precision are useful until waiting survives past the moment when action is required. It also concretizes the father-son recognition gap: Cornelis' increased trust can feel to Claes like another test because explicit praise remains sparse.
    guardrails:
      - Do not turn the crossbow into an explicit allegory explained by characters.
      - The motif must remain materially credible before it becomes thematic.
      - Exact loading/spanning procedure requires period-appropriate evidence per scene.
      - Claes' central gift/shadow predates and exceeds this one training environment; the voetboog reinforces it rather than singularly causing it.
```

---

# SOURCE FILE: `canon/DECISIONS_PUTTUS_2026-08-18.yaml`

```yaml
schema_version: 1.1.0
kind: CanonDecisionRegistry
decisions:
- id: DEC.CLAES.PUTTUS_MASTER.2026-08-18
  type: CanonDecision
  status: CANON
  decision: In novel canon, Nicolaes van de Put (Puttus) is Claes' Goese Latin/humanist master in the final school years before the city fire of 18 May 1554.
  affects:
  - STC.CLAES.PUTTUS_MASTER.001
  - ENT.PERSON.NICOLAES_PUTTUS
  - WORLD.GOES.SCHOOLING_1550_1554
  - STC.CLAES.SCHOOL.GOES.001
  - STC.CLAES.ZIERIKZEE.PLAN.001
  - STC.CLAES.REIMERSWAAL.001
  rationale: >-
    Puttus is historically documented as Goese schoolmaster in 1512 in a Latin-humanist educational context and Meertens considers him probably rector. A targeted 18 August 2026 search of accessible evidence and citations to the specialized histories by Römer (1849) and Fortgens (1953) found no death, departure or named successor that excludes him from Claes' early-1550s school years and no better named Goese Latin master for that interval. The author explicitly decides that, absent contrary evidence, Puttus is Claes' teacher. This closes the fictional teacher identity, not the historical question of Puttus' actual tenure.
  evidence_status: PLAUSIBLE
  canon_status: CANON
  supported_by:
  - SC.HIST.GOES.PUTTUS.SCHOOLMASTER_1512.001
  - SC.HIST.GOES.LATIN_SCHOOL_1569.001
  characterization_extension: DEC.PUTTUS.FICTIONAL_CHARACTERIZATION.2026-08-19
  guardrails:
  - Puttus teaching Claes is novel truth, not a documented historical teacher-pupil relationship.
  - Do not state as historical fact that Puttus held the Goese rectorship continuously from 1512 to 1554.
  - Puttus' historical birth date, death date, appearance, exact age and exact tenure remain UNKNOWN without new evidence.
  - Approved fiction-canon characterization may deliberately specify how Claes experiences Puttus' appearance, voice, habits and teaching room under DEC.HISTORICAL_GAPS.FICTIONAL_CHARACTERIZATION.2026-08-19; those details must never be back-presented as historical evidence.
  - Do not infer that Claes completed a full formal Goese Latin-school curriculum before Reimerswaal.
  - Zierikzee remains the intended more sustained pre-fire Latin-school continuation; Reimerswaal remains the actual post-fire route.
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

# SOURCE FILE: `storybible/CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md`

```markdown
# Character web — archetypische functies en levende karakterisering

**Status:** CANONICAL CHARACTERIZATION MODULE — approved 19 August 2026  
**Decisions:** `DEC.HISTORICAL_GAPS.FICTIONAL_CHARACTERIZATION.2026-08-19`, `DEC.CHARACTER_WEB.ARCHETYPAL_LENS.2026-08-19`, `DEC.CHARACTER_WEB.CORE_CAST.2026-08-19`  
**Machine projections:** `entities/CHARACTERIZATION_2026-08-19.yaml`, `narrative/character_web_archetypes.yaml`

## 1. Governing principle: the archive sets boundaries; the novel fills the living space

Historical uncertainty is not automatically a prohibition on characterization.

The project distinguishes four layers:

1. **Historical fact** — source-backed biography, office, date, publication, place or act.
2. **Evidence-based reconstruction** — a source-weighted inference whose uncertainty remains visible.
3. **Fiction canon** — an explicit authorial choice made inside documentary space for character, continuity and drama.
4. **Open material** — a choice not yet made or deliberately left unresolved.

A historical person's undocumented voice, habits, appearance or private behaviour may therefore be fixed as **FICTION CANON** when the recurring novel requires it, provided no known evidence is contradicted. Doing so does not upgrade the historical evidence. If the archive does not tell us how Puttus sounded, the historical answer remains *unknown* even when the novel decides how Claes experiences his voice.

This distinction prevents two opposite failures: invented detail masquerading as history, and historical characters left as faceless names because the archive did not preserve ordinary human particulars.

## 2. Archetypes are lenses, not cages

The archetypal layer is author-side craft. It is used to expose contrast, value, strength and likely shadow. It must never become dialogue such as “I am the Law” or a sequence in which each supporting character appears only to teach Claes one symbolic lesson.

A useful archetype always needs individual contradiction. The question is therefore not only **what function does this person carry?**, but also:

- what does this person want independently of Claes?
- what are they good at?
- what does that strength become when overused?
- how do they speak and behave when unobserved by the protagonist?
- what does Claes misunderstand about them?
- what would they still be doing if Claes were absent?

The compact authorial constellation is:

- **Claes — Integration / the Seeker-Witness**
- **Cornelis — Law / the Father-Gatekeeper**
- **Tanneken — Body / embodied household wisdom**
- **Jan — Act / brother-double and action principle**
- **Puttus — Word / hermeneutic teacher**
- **Mayken — Matter / independent material counterpart**
- **Dee — Transformation / magician-mentor**
- **Silvius — Transmission / pragmatic mediator**
- **Las Casas — Conscience / witness-herald**

The point is not that Claes collects eight lessons. The point is that his life repeatedly confronts him with partial but legitimate ways of knowing and acting. His mature task is not to imitate one of them but to integrate attention, body, word, matter, action, responsibility, transformation, transmission and conscience without trying to possess or control them all.

---

# 3. Claes — Seeker, Observer, Witness, Integrator

### Core
Claes' distinctive gift is **prolonged embodied attention**. He notices a discrepancy, holds it, compares it with something previously experienced, and only then builds a pattern. His intelligence should therefore usually appear in the sequence:

`sensation -> recognition -> comparison -> pattern -> understanding`

His mature form adds what childhood lacks:

`perceive -> distinguish -> choose -> carry -> release`

### Strength
- notices small material and social discrepancies;
- remembers sensory detail and relational patterns;
- can connect domains that other people keep separate;
- persists after first appearances stop being useful;
- takes testimony and material continuity seriously.

### Shadow
His gift becomes dangerous when attention turns into control:

- if I look long enough, perhaps I can prevent loss;
- if I understand every path, perhaps I need not choose too soon;
- if I keep watching, perhaps I have fulfilled my responsibility.

Delft makes the shadow explicit: witnessing can become compulsion. He can want not to look and still look.

### Essential contradiction
Claes is **not inherently passive**. When Jan slips at the crane and no interval exists for analysis, Claes acts before thought. The weakness therefore appears especially when time exists to continue observing.

### Character-writing rule
Do not make him a modern analyst. Let the abstraction arrive after material perception. Care is often expressed through remembering, noticing, checking and quietly doing what another person needs.

---

# 4. Cornelis — Father, Steward, Gatekeeper, Artisan Mentor

### Core
Cornelis' governing value is **responsible stewardship**. He believes love is something one does: provide, train, arrange, repair, finance, warn, carry, protect.

### Strength
- practical foresight;
- reliability under work pressure;
- judgement of people, goods, routes and obligations;
- teaching through graduated responsibility;
- willingness to bear material cost for another person's future.

### Shadow
The same method can make intimacy difficult:

- protection becomes withholding;
- secrecy becomes exclusion;
- responsibility becomes the language in which every affection is translated;
- trust feels to Claes like a harder test rather than recognition.

Cornelis does not fail to love. Father and son fail, repeatedly, to read love in the same grammar.

### Essential contradictions
- **home:** terse, functional, sparse praise;
- **rederijker room:** socially alive, humorous, performative, able to laugh broadly and respond to words for their own sake;
- **public religion:** outwardly Catholic and civically embedded;
- **inner commitment:** Familist/Huis der Liefde after ca.1552–1553;
- **protector:** tries to keep danger away from Claes while simultaneously teaching him to carry dangerous responsibilities.

### Voice and habits — fiction canon
- short, material sentences;
- dry humour that often arrives without announcing itself as humour;
- praise is rare enough to matter;
- trust is more often shown through the next task than through congratulation;
- anger need not become shouting: terse judgement, practical consequence or closed access can carry more weight.

### Guardrail
Do not make Cornelis a factory for maxims. His practical speech should arise from the thing being handled now. His livelier rederijker self is necessary because Claes must discover that his father is a person whose full life does not exist only in relation to his son.

---

# 5. Tanneken — Mother, Body, Keeper of Household Continuity

### Core
Tanneken's intelligence is **trained sensation in time**. She knows because she has touched, smelled, prepared, stored, watched and repeated.

### Strength
- material and bodily judgement;
- household timing;
- practical memory;
- care without ceremony;
- direct, proportionate praise;
- warmth and teasing humour.

She gives Claes an early experience of knowledge that does not begin in abstraction. Her “goed gevonden” is important precisely because it is not made into a bargain.

### Shadow
Tanneken often turns anxiety into action. That is useful, but it can also hide her from others:

`fear -> preparation -> routine -> competence`

The household may therefore experience her as calm at moments when she is actually containing fatigue, uncertainty or fear through work.

### Essential contradiction
She is patient with fermentation, weather, cloth and bodies because processes take the time they take; she need not be equally patient with avoidable fuss, mess or self-dramatization.

### Voice and habits — fiction canon
- shows before she explains;
- lets Claes try and lets the material reveal whether he was right;
- uses sensory comparisons rather than doctrine;
- can tease affectionately;
- tenderness is physical and ordinary rather than staged as a lesson.

### Guardrail
Do not turn her into a mystical earth-mother. Her knowledge is laboriously learned, fallible and bodily. Give her irritation, fatigue and personal preference as well as care.

---

# 6. Jan — Brother-Double, Trickster Child, Action Principle

### Core
Jan embodies a capacity Claes both loves and lacks: **movement before complete certainty**.

### Strength
- speed;
- bodily learning through repetition;
- improvisation;
- humour and mischief;
- willingness to risk embarrassment or failure;
- loyalty expressed through presence and action.

At the molenbord he can reach a working move without being able to explain a method. At the crane he makes danger real rather than theoretical.

### Shadow
- acts too soon;
- lies or improvises a cover story too easily;
- discovers consequence after choosing rather than before;
- can mistake confidence for safety.

### Essential contradiction
Jan is not fearless. His sudden question about whether the unborn baby will live matters because the fear is real and brief. He does not metabolize anxiety like Claes; he asks, receives an answer, and moves back toward action.

### Voice and habits — fiction canon
- short, direct, impatient with lengthy explanation;
- teasing rather than philosophical;
- learns through doing it again;
- repairs many quarrels by simply returning to play or physical proximity.

### Guardrail
Do not let Jan speak the book's mature philosophy. A child can say “ik doe het gewoon”; he should not diagnose Claes in polished adult language. His death must remove a full brother, not a symbolic function in human form.

---

# 7. Puttus — Teacher, Word, Hermeneutic Mentor

### Historical boundary
Historically supported: Nicolaes van de Put/Puttus is attested as a Goese schoolmaster in 1512 and belongs to a Latin-humanist context. His continuous presence into Claes' childhood, exact age, appearance and exact teaching room are not historically documented.

Novel canon already places him as Claes' master in the final Goese school years. The following characterization now deliberately fills the remaining human space as **fiction canon**.

### Core
Puttus teaches **disciplined distinction**: a word is not another word; a `c` must remain open enough not to become an `o`; a second layer is valid only when the text supports it.

### Strength
- precise correction;
- interpretive restraint;
- memory and recitation discipline;
- ability to notice intellectual promise without flattering it;
- economy: little apparatus, concentrated attention.

### Shadow
His quietness can wound. Silence that disciplines one pupil can shame another. Precision can accidentally teach a child that being correct and being worthy are dangerously close.

### Stable fictional characterization
- Claes cannot place Puttus' age; this remains an impression, not a hidden numeric biography;
- Puttus rarely raises his voice when displeased;
- he corrects with exact, small interventions and often lets silence do part of the work;
- he handles a small collection of working books carefully;
- he teaches in a small, sparse, often cold room;
- that room is **not** mapped to a claimed historical building.

### Guardrail
Puttus trains interpretation; he does not explain the religious future of the Netherlands. He is not a proto-Protestant oracle and should not deliver the novel's complete theory of hidden meaning.

---

# 8. Mayken — Matter, Material Counterpart, Conjunctio Partner

### Childhood relationship — fixed
Claes and Mayken know one another before 18 May 1554. Their childhood relation is ordinary acquaintance/friendship: play, looking, and Mayken's early material/botanical knowledge. It is **not childhood romance** and must never be written as predestination.

### Core
Mayken's intelligence begins from **material fidelity**:

- what is this actually?
- in what condition?
- what differs from the thing beside it?
- what happens if we prepare or test it again?
- what observation would prove us wrong?

### Strength
- identification;
- measurement and preparation;
- contamination/substitution awareness;
- trained sensation;
- repeatability;
- practical contradiction;
- independent judgement.

### Shadow
Her method can overcorrect Claes' abstraction. She may become impatient with a meaning, relation or possibility that cannot yet be demonstrated materially. This gives her a genuine limit rather than making “Mayken checks the facts” automatically superior.

### Essential contradiction
She can be patient with matter and impatient with speculation. Intimacy with Claes never requires surrendering judgement.

### Guardrail
Mayken is not an anima-shaped reward, therapist, saint or missing ingredient. “Counterpart” is preferable to “other half”. Conjunctio means reciprocal relation between two centers of agency.

---

# 9. John Dee — Magician, Initiatory Mentor, Transformation

### Historical boundary
Dee is historical. The novel may use sourced biography, but the private habits below are story characterization unless separately sourced.

### Core
Dee makes hidden relation intellectually imaginable. He shows Claes that apparent states are not final states and that material change can disclose an order that ordinary looking misses.

### Strength
- intellectual daring;
- sustained concentration;
- abstraction across disciplines;
- experimental curiosity;
- recognition of Claes' already-existing mode of attention.

He should **recognize** Claes, not manufacture him. Goes, Tanneken, Cornelis, Jan and Puttus have already formed the capacities Dee can name and extend.

### Shadow
- overpatterning;
- suspicion of hidden intention;
- pride;
- gatekeeping knowledge;
- treating pupils or assistants as instruments of a larger intellectual problem.

The wrong-kist logic is important because Dee can be wrong: the man who sees hidden structures may see intention where ordinary error is enough.

### Stable fictional habits
- expansive and argumentative in learned discussion;
- often quiet while walking, inspecting or smelling matter;
- under threat he conceals first and admits fear last;
- capable of a sharp correction followed later by a clarification that approaches apology without becoming emotional confession.

### Guardrail
Do not make Dee the Storybible with a beard. Fewer perfect aphorisms make his actual insight more powerful.

---

# 10. Willem Silvius — Mediator, Pragmatic Gatekeeper, Transmission

### Historical boundary
Silvius is historical. His printing/publishing world may be sourced; the private behavioural characterization below is fiction unless separately evidenced.

### Core
Silvius makes ideas **work in the world**. Where Dee sees intellectual necessity, Silvius sees paper, type, labour, cost, timing, routes, censors, buyers and risk.

### Strength
- production judgement;
- negotiation;
- social calibration;
- logistics;
- practical humour;
- ability to translate grand intention into sequence and resource.

### Shadow
Practicality can become instrumentalism. A person can become “two hours a day”; a dangerous text can become a routing problem. His realism is necessary but not automatically morally superior.

### Essential contrast with Dee
Dee asks whether a hidden order exists. Silvius asks whether the paper can arrive, who pays the rider, who is watching the door and whether the press can stop for an afternoon.

### Voice — fiction canon
Calm, practical, rarely impressed by grandiosity. In conflict he bargains, reframes and prices the alternative rather than competing for volume.

### Guardrail
Transmission is his archetypal function, not proof that Silvius translated the Brevísima.

---

# 11. Bartolome de las Casas — Witness, Herald, Conscience

### Historical boundary
Las Casas is historical. The project must continue to distinguish sourced biography and texts from imagined private interiority in the prologue.

### Core
Las Casas carries **testimony that must cease to belong to its keeper**.

### Strength
- moral persistence;
- collecting and preserving testimony;
- ordering overwhelming material into communicable form;
- willingness to implicate his own earlier participation;
- understanding writing as action rather than possession.

### Shadow
The writer can begin to hope that sharper evidence, better order or stronger rhetoric will control what a reader does with truth. Las Casas knows the opposite danger as well: once sent, a text can be ignored, weaponised, translated or used beyond its author's intention.

### Essential contradiction
He is a reforming loyalist whose testimony can indict the world to which he remains loyal; a former participant who becomes an accuser; a man who must shape testimony forcefully and then surrender control over its reception.

### Relation to Claes
No direct mentorship is required. Las Casas is a distant moral mirror. The prologue and Claes' later transmission line ask the same question at different ends of the chain:

> When does preserving testimony require releasing possession of it?

---

# 12. Character web in motion

The web should generate conflict through **different valid methods**, not simple good-versus-bad oppositions.

### Claes ↔ Jan
`deliberation <-> immediacy`

Neither is the complete answer. Jan can act too early; Claes can act too late.

### Cornelis ↔ Tanneken
`rule/responsibility <-> body/timing/care`

The intact household gives Claes both. The 1554 fire destroys not only people but the equilibrium between these knowledge forms.

### Puttus ↔ Dee
`interpretive restraint <-> transformative speculation`

Puttus teaches: do not invent a second layer because you want one. Dee teaches: the visible state may genuinely be incomplete. Claes eventually needs both propositions.

### Dee ↔ Mayken
`hidden pattern <-> material verification`

Mayken later offers a human and material counter-pressure to the danger already visible in Dee: a beautiful interpretation that matter contradicts must change.

### Las Casas ↔ Silvius
`moral necessity of testimony <-> physical/social mechanics of transmission`

A testimony without a carrier cannot travel. A carrier without moral purpose merely moves content.

### Cornelis ↔ Silvius
`private carrying/trust <-> reproduction/distribution`

Claes grows from a son who carries what he is told not to know into a man who must decide what known testimony should be released beyond him.

---

# 13. Hard character-writing guardrails

1. **Archetype is never dialogue.** Do not make characters announce the function the author sees in them.
2. **Strength must cast a shadow.** The shadow should usually be the overuse or distortion of a real strength, not an unrelated flaw bolted on for complexity.
3. **Contradiction is continuity.** Cornelis being funny among rederijkers is not inconsistent with domestic reserve; it reveals context-dependent selfhood.
4. **Historical unknown may be fictionally fixed.** Label it. Never back-convert the fictional choice into evidence.
5. **Supporting characters are not wallpaper.** A recurring supporting person should have at least a want, method, limit or social pressure independent of delivering information to Claes.
6. **Do not create one lesson per archetype.** Character functions should collide inside ordinary plot and relationship action.
7. **Do not overexplain the web in prose.** If the reader can infer “Jan acts before Claes,” no narrator or adult needs to summarize it afterward.
8. **A character may surprise the web.** If a well-earned scene reveals a new contradiction, update the characterization rather than forcing prose back into the old shorthand.
9. **Mayken remains two-centered with Claes.** No “missing half” logic.
10. **Dee may be wrong; Puttus may wound; Tanneken may tire; Cornelis may misjudge; Jan may fear; Silvius may instrumentalize; Las Casas may lose control.** Their value lies in being partial human beings, not perfect embodiments.
```

---

# SOURCE FILE: `entities/CHARACTERIZATION_2026-08-19.yaml`

```yaml
schema_version: 1.0.0
kind: CharacterizationRegistry
purpose: >-
  Stable novel characterization for recurring people. Historical biography and evidence remain governed by their source/entity records; fields marked FICTION_CANON deliberately fill documentary space for continuity.
characters:
- entity_ref: ENT.PERSON.CLAES
  characterization_status: CANON
  archetypal_lenses: [seeker, observer, witness, integrator]
  governing_value: attentive_truth
  strengths: [embodied_attention, comparison, memory, pattern_synthesis, sustained_observation]
  shadow: [over_observation, delayed_choice, compulsive_witnessing, control_through_understanding]
  contradiction: >-
    Claes can act instantly when no deliberative interval exists; his danger emerges especially when time is available to keep looking.
  relational_expression:
    care: [noticing, remembering, helping, carrying, precise_follow_through]
    fear: [counting, checking, rehearsing, withholding_until_certain]
  voice_guardrails:
  - Perception normally precedes abstraction.
  - Let comparison grow from material detail rather than modern analysis.
  - Do not let insight make him omniscient.
  trajectory: perceive -> distinguish -> choose -> carry -> release

- entity_ref: ENT.PERSON.CORNELIS
  characterization_status: CANON
  archetypal_lenses: [father, steward, gatekeeper, artisan_mentor]
  governing_value: responsible_stewardship
  strengths: [foresight, provision, practical_judgement, reliability, teaching_by_task, protection]
  shadow: [emotional_withholding, over_duty, secrecy_as_exclusion, protection_becoming_gatekeeping]
  contradictions:
  - domestic reserve versus social and rhetorical vitality among trusted rederijkers
  - outward Catholic conformity versus inward Familist commitment
  - love expressed through responsibility can be received as another test
  habitual_expression:
    speech: short, material, dry, rarely self-explanatory
    humour: dry and often delayed by half a beat
    praise: scarce but weighty
    trust: increased responsibility and practical inclusion
    anger: more likely terse judgement or closed access than theatrical rage
  prose_guardrails:
  - Do not make every utterance a maxim.
  - Let the rederijker room reveal playfulness and performative range absent at home.
  - His secrecy must arise from real risk and belief as well as temperament.

- entity_ref: ENT.PERSON.CLAES_MOTHER
  label: Tanneken Jansdochter
  characterization_status: CANON
  archetypal_lenses: [mother, embodied_wise_woman, keeper_of_household_continuity]
  governing_value: sustaining_life_through_attention
  strengths: [trained_sensation, timing, care, practical_memory, direct_encouragement, humour]
  shadow: [fear_converted_into_work, hidden_exhaustion, competence_masking_vulnerability]
  contradictions:
  - patient with processes but brisk with avoidable fuss
  - capable of tenderness without making tenderness ceremonial
  habitual_expression:
    teaching: show, let_try, correct_by_material_result
    praise: direct and proportionate
    worry: often converted into preparation or routine
    humour: affectionate, practical, sometimes teasing
  prose_guardrails:
  - Never mystical or all-knowing.
  - Give her fatigue, irritation, desire and limits as well as competence.
  - Sensory knowledge is learned through repetition, not supernatural intuition.

- entity_ref: ENT.PERSON.CLAES_BROTHER
  label: Jan Corneliszn. Nissepat
  characterization_status: CANON
  archetypal_lenses: [brother_double, trickster_child, action_principle]
  governing_value: immediate_engagement
  strengths: [speed, bodily_learning, improvisation, courage, humour, resilience, loyalty]
  shadow: [recklessness, premature_action, convenient_lying, consequence_after_choice]
  contradictions:
  - physically daring yet capable of sudden private fear about death and family
  - competitive without needing victory to define affection
  habitual_expression:
    speech: short, direct, teasing, impatient_with_explanation
    learning: repetition, body_memory, consequence
    repair: moves back into play or contact quickly after conflict
  prose_guardrails:
  - Do not make him prophetic about Claes' flaw.
  - Let his wisdom sound like a child's practical answer, not adult thematic language.
  - Preserve mischief and vulnerability together.

- entity_ref: ENT.PERSON.NICOLAES_PUTTUS
  characterization_status: CANON
  historical_person: true
  historical_characterization_evidence: UNKNOWN
  fiction_fill_status: FICTION_CANON
  archetypal_lenses: [teacher, hermeneutic_mentor, keeper_of_word]
  governing_value: disciplined_distinction
  strengths: [precision, textual_attention, interpretive_restraint, memory_training, economical_correction]
  shadow: [silence_as_shame, excessive_severity, correctness_becoming_worth]
  stable_fictional_details:
  - Claes cannot readily estimate his age; the impression is deliberately age-indeterminate rather than a fixed numerical age.
  - His voice seldom becomes louder when displeased; quietness increases pressure.
  - He handles a small working book collection carefully and economically.
  - Corrections are often exact and minimal: a finger, a word, a request to try again.
  - His teaching room is small, sparse and often cold; its exact historical building/location is not claimed.
  material_style:
    clothing: dark, serviceable teaching dress; no archival costume claim
    books: few enough to be handled as valued tools rather than decoration
  prose_guardrails:
  - Never present these details as recovered biography.
  - Do not make silence sadism; it is a pedagogical strength with a real possible cost.
  - Do not make Puttus an anti-Catholic oracle.

- entity_ref: ENT.PERSON.BELOVED
  label: Mayken Adriaensdr. Lampert
  characterization_status: CANON
  archetypal_lenses: [material_counterpart, craft_wise_woman, later_lover, conjunctio_partner]
  governing_value: material_fidelity
  strengths: [identification, condition_judgement, measurement, preparation, trained_sensation, error_control, practical_contradiction]
  shadow: [impatience_with_unverifiable_pattern, overreliance_on_material_demonstration]
  contradictions:
  - patient with matter but not automatically patient with speculation
  - capable of intimacy without surrendering independent judgement
  childhood_relation_to_claes:
    status: CANON
    earliest: before_1554_fire
    mode: acquaintance_and_friendship_through_play_and_plant_material_observation
    excludes: [childhood_romance, predestined_sweethearts]
  habitual_expression:
    questions: [what_is_it, what_condition_is_it_in, what_changes_when_tested, what_did_we_actually_observe]
    humour: practical, can be dry, never saintly
  prose_guardrails:
  - She is not Claes' missing half.
  - Let her be wrong where her own method has limits.
  - Give her objectives not reducible to Claes.

- entity_ref: ENT.PERSON.JOHN_DEE
  characterization_status: CANON
  historical_person: true
  personal_habits_status: FICTION_CANON_UNLESS_SOURCED
  archetypal_lenses: [magician, initiatory_mentor, transformative_scholar]
  governing_value: hidden_order_made_intelligible
  strengths: [intellectual_daring, close_observation, abstraction, experimental_curiosity, recognition_of_potential]
  shadow: [overpatterning, suspicion, pride, control_of_access, instrumentalizing_students]
  contradictions:
  - expansive in learned debate, often silent while walking or inspecting matter
  - capable of sharp command and of a near-apology that stops short of emotional confession
  - wants truth yet can become more interested in hidden intention than ordinary error
  habitual_expression:
    speech: learned, exact, sometimes aphoristic; Latin more fluent than Diets in the novel
    under_threat: conceal_first, interpret_second, admit_fear_last
  prose_guardrails:
  - He must be materially wrong sometimes.
  - Limit perfect thematic aphorisms.
  - Historical Dee biography outranks invented habit if a conflict emerges.

- entity_ref: ENT.PERSON.WILLEM_SILVIUS
  characterization_status: CANON
  historical_person: true
  personal_habits_status: FICTION_CANON_UNLESS_SOURCED
  archetypal_lenses: [mediator, pragmatic_gatekeeper, transmission_principle]
  governing_value: workable_transmission
  strengths: [production_judgement, negotiation, timing, logistics, social_calibration, practical_humour]
  shadow: [instrumentalism, expedience, people_as_resources, normalizing_secrecy]
  contradiction: >-
    He can enable dangerous intellectual work precisely because he keeps reducing grandeur to paper, labour, price, timing and risk.
  habitual_expression:
    speech: calm, practical, capable of puncturing grandiosity without raising volume
    conflict: bargains, reframes, redirects, prices the alternative
  prose_guardrails:
  - Pragmatism is not cowardice.
  - He is not automatically the moral center merely because he is more realistic than Dee.
  - Transmission role does not imply translator role.

- entity_ref: ENT.PERSON.BARTOLOME_DE_LAS_CASAS
  label: Bartolome de las Casas
  characterization_status: CANON
  historical_person: true
  entity_status: NEW_CORE_REFERENCE
  private_interiority_status: FICTIONAL_RECONSTRUCTION_UNLESS_SOURCED
  archetypal_lenses: [witness, conscience, herald]
  governing_value: testimony_that_must_be_carried
  strengths: [moral_persistence, witness_collection, rhetorical_ordering, self_implication, transmission]
  shadow: [control_through_rhetoric, fear_of_misuse, belief_that_precision_can_govern_reception]
  contradictions:
  - loyal reformer of a world he also indicts
  - former participant in a system he later condemns
  - must sharpen testimony while knowing sharper language can escape his intention
  prose_guardrails:
  - Keep source-backed biography distinct from imagined private thought.
  - Do not make him a spotless saint or a direct mentor to Claes.
  - His strongest mirror to Claes is release of testimony beyond possession.
```

---

# SOURCE FILE: `narrative/character_web_archetypes.yaml`

```yaml
schema_version: 1.0.0
kind: CharacterWeb
id: ARC.CLAES.CHARACTER_WEB.ARCHETYPAL
status: CANON_AUTHORIAL_ARCHITECTURE
decision_ids:
- DEC.CHARACTER_WEB.ARCHETYPAL_LENS.2026-08-19
- DEC.CHARACTER_WEB.CORE_CAST.2026-08-19
purpose: >-
  Author-side web for differentiating major characters by value, method and shadow. Archetypes are lenses, not in-world identities and not permission for thematic exposition.
central_problem: >-
  How can Claes learn to perceive truth without mistaking perception for control, and to turn knowledge into chosen action, relation and release?
characters:
- entity: ENT.PERSON.CLAES
  shorthand: Integration
  lenses: [seeker, observer, witness, integrator]
  offers_claes: [attention, synthesis]
  method: see -> compare -> connect -> understand
  shadow_method: see -> compare -> keep_looking -> delay
  mature_method: perceive -> distinguish -> choose -> carry -> release

- entity: ENT.PERSON.CORNELIS
  shorthand: Law
  lenses: [father, steward, gatekeeper, artisan_mentor]
  offers_claes: [responsibility, discipline, routes, practical_action]
  method: entrust -> test -> correct -> enlarge_responsibility
  shadow_method: protect -> withhold -> exclude
  pressure_on_claes: love is present but encoded in a form Claes does not automatically read as recognition

- entity: ENT.PERSON.CLAES_MOTHER
  shorthand: Body
  lenses: [mother, embodied_wise_woman]
  offers_claes: [trained_sensation, care, timing, permission_to_doubt]
  method: touch -> smell -> compare -> wait -> know_enough
  shadow_method: fear -> work -> hide_own_need
  pressure_on_claes: not everything important becomes certain through analysis

- entity: ENT.PERSON.CLAES_BROTHER
  shorthand: Act
  lenses: [brother_double, trickster_child, action_principle]
  offers_claes: [speed, risk, embodied_choice, play]
  method: see_desire -> move -> learn_from_result
  shadow_method: move -> rationalize_afterward
  pressure_on_claes: action can precede complete certainty without being stupidity

- entity: ENT.PERSON.NICOLAES_PUTTUS
  shorthand: Word
  lenses: [teacher, hermeneutic_mentor]
  offers_claes: [language, distinction, textual_discipline]
  method: read -> compare -> support -> correct
  shadow_method: correct -> silence -> shame
  pressure_on_claes: hidden meaning must be earned by evidence, not desired into existence

- entity: ENT.PERSON.BELOVED
  shorthand: Matter
  lenses: [material_counterpart, craft_wise_woman, conjunctio_partner]
  offers_claes: [identity_testing, material_fidelity, contradiction, reciprocal_relation]
  method: identify -> prepare -> test -> compare -> revise
  shadow_method: demand_demonstration -> dismiss_what_is_not_yet_testable
  pressure_on_claes: a pattern that matter contradicts must change; relation is not possession

- entity: ENT.PERSON.JOHN_DEE
  shorthand: Transformation
  lenses: [magician, initiatory_mentor]
  offers_claes: [hidden_relation, intellectual_daring, transformative_process]
  method: observe -> hypothesize -> expose_relation -> transform
  shadow_method: suspect_hidden_intention -> gatekeep -> control
  pressure_on_claes: the master of hidden order can become trapped by hidden order

- entity: ENT.PERSON.WILLEM_SILVIUS
  shorthand: Transmission
  lenses: [mediator, pragmatic_gatekeeper]
  offers_claes: [production, circulation, audience, social_reality]
  method: make -> price -> route -> deliver
  shadow_method: instrumentalize -> normalize_risk
  pressure_on_claes: truth that cannot survive paper, labour, routes and readers has not yet entered the world

- entity: ENT.PERSON.BARTOLOME_DE_LAS_CASAS
  shorthand: Conscience
  lenses: [witness, herald, conscience]
  offers_claes: [moral_testimony, self_implication, release_of_text]
  method: witness -> order -> write -> send
  shadow_method: sharpen -> try_to_control_reception
  pressure_on_claes: testimony ceases to belong to its keeper when it must act beyond him

web_relations:
- pair: [ENT.PERSON.CLAES, ENT.PERSON.CLAES_BROTHER]
  axis: deliberation <-> immediacy
  dramatic_use: brothers expose that neither observation nor action is sufficient alone
- pair: [ENT.PERSON.CORNELIS, ENT.PERSON.CLAES_MOTHER]
  axis: responsibility_and_rule <-> embodied_care_and_timing
  dramatic_use: Claes' intact childhood contains two complementary modes of safety that the fire destroys together
- pair: [ENT.PERSON.NICOLAES_PUTTUS, ENT.PERSON.JOHN_DEE]
  axis: disciplined_interpretation <-> transformative_speculation
  dramatic_use: Puttus teaches that meaning must be supported; Dee teaches that the apparently ordinary may hide another state
- pair: [ENT.PERSON.JOHN_DEE, ENT.PERSON.BELOVED]
  axis: hidden_pattern <-> material_verification
  dramatic_use: Mayken later supplies a counter-pressure to the danger already visible in Dee
- pair: [ENT.PERSON.WILLEM_SILVIUS, ENT.PERSON.BARTOLOME_DE_LAS_CASAS]
  axis: transmission_mechanics <-> moral_necessity_of_transmission
  dramatic_use: together they frame the problem that testimony needs both conscience and a carrier
- pair: [ENT.PERSON.CORNELIS, ENT.PERSON.WILLEM_SILVIUS]
  axis: private_carriage_and_trust <-> public_reproduction_and_distribution
  dramatic_use: Claes moves from carrying what he may not know toward deciding what knowledge must be released

hard_guardrails:
- Archetypal shorthand must never appear as explanatory labels in literary prose.
- A character may contradict the shorthand; contradiction is evidence of life, not a continuity error.
- Use the web to differentiate choices and values, not to manufacture one teaching scene per function.
- Supporting characters need not receive archetypal assignments unless repeated story pressure justifies them.
- The web supplements, never replaces, entity biography, historical evidence, arcs, relationships and scene objectives.
```

---

# SOURCE FILE: `claims/STORY_CLAIMS_CHARACTER_WEB_2026-08-19.yaml`

```yaml
schema_version: 1.0.1
kind: StoryClaimRegistryExtension
story_claims:
- id: STC.CHARACTER.CLAES.INTEGRATOR.001
  type: StoryClaim
  status: CANON
  evidence_status: PLAUSIBLE
  decision_id: DEC.CHARACTER_WEB.CORE_CAST.2026-08-19
  claim: >-
    Claes' characteristic strength is prolonged embodied attention: he notices, compares, remembers and connects patterns across materials, texts, people and events. His recurring danger is to remain in observation after action is required, or to treat attention as if it could make loss preventable and the world controllable. He is nevertheless capable of immediate embodied action when circumstances leave no time for analysis.
  guardrails:
  - Do not write Claes as passive by nature; his problem is over-observation under available time, not inability to act.
  - Do not make pattern recognition omniscience.
  - Mature integration is perceive -> distinguish -> choose -> carry -> release.

- id: STC.CHARACTER.CORNELIS.STEWARD_GATEKEEPER.001
  type: StoryClaim
  status: CANON
  evidence_status: PLAUSIBLE
  decision_id: DEC.CHARACTER_WEB.CORE_CAST.2026-08-19
  claim: >-
    Cornelis is a practical steward and father-gatekeeper who expresses care through provision, training, responsibility and protection. He is terse at home, uses dry humour, and can be markedly more expansive, social and performative among trusted rederijkers. His strength is stewardship under pressure; his shadow is that protection through secrecy, duty and withholding can become exclusion and make love feel like another obligation to the people he is trying to protect.
  guardrails:
  - Do not reduce him to cold patriarch or secretive conspirator.
  - Preserve the contrast between domestic reserve and social/rhetorical vitality.
  - Outward Catholic participation and inward Familist commitment coexist before the fire.

- id: STC.CHARACTER.TANNEKEN.EMBODIED_WISDOM.001
  type: StoryClaim
  status: CANON
  evidence_status: PLAUSIBLE
  decision_id: DEC.CHARACTER_WEB.CORE_CAST.2026-08-19
  claim: >-
    Tanneken knows through trained body, repetition, household timing and material condition. She gives care directly, can praise without making praise a bargain, and carries a playful practical humour. Under anxiety she tends to turn fear into work, routine and preparation rather than abstract discussion; that competence can also conceal her own vulnerability from others.
  guardrails:
  - Do not mysticize her sensory knowledge.
  - Do not make domestic competence emotional simplicity or endless self-sacrifice.
  - Her fears and limits may remain partly unspoken because she works through them, not because she lacks them.

- id: STC.CHARACTER.JAN.ACTION_DOUBLE.001
  type: StoryClaim
  status: CANON
  evidence_status: PLAUSIBLE
  decision_id: DEC.CHARACTER_WEB.CORE_CAST.2026-08-19
  claim: >-
    Jan is Claes' loved rival and brother-double: bodily, fast, mischievous and willing to test before he fully understands. He learns through repetition and consequence and can reach correct action faster than Claes. His shadow is recklessness and premature improvisation. His courage is not fearlessness: private questions about death, family and the unborn child reveal abrupt vulnerability that he does not sustain in long analysis.
  guardrails:
  - Do not make Jan merely comic relief, a reckless foil or trauma machinery.
  - His action-first mode sometimes succeeds where Claes' method fails and sometimes creates danger.
  - Preserve ordinary rivalry, play, irritation and loyalty.

- id: STC.CHARACTER.PUTTUS.HERMENEUTIC_MENTOR.001
  type: StoryClaim
  status: CANON
  evidence_status: PLAUSIBLE
  decision_id: DEC.PUTTUS.FICTIONAL_CHARACTERIZATION.2026-08-19
  claim: >-
    In novel characterization Puttus teaches through precision, repetition, economical correction and interpretive restraint. He rewards what the text supports and corrects the urge to manufacture hidden meanings. He seldom raises his voice; silence and exact attention are part of his authority. The same restraint can shame a struggling pupil, so his pedagogy carries a real shadow rather than functioning as infallible wisdom.
  guardrails:
  - Fiction characterization does not change the historical UNKNOWN status of his age, appearance or 1550s tenure details.
  - Do not make him a proto-Protestant doctrinal guide.
  - His teaching should train distinction, not deliver the novel's complete theory of meaning.

- id: STC.CHARACTER.MAYKEN.MATERIAL_COUNTERPART.001
  type: StoryClaim
  status: CANON
  evidence_status: PLAUSIBLE
  decision_id: DEC.CHARACTER_WEB.CORE_CAST.2026-08-19
  claim: >-
    Mayken's characteristic intelligence is material discrimination: identity, condition, contamination, preparation, measurement, repeatability and practical contradiction. She can interrupt Claes' attraction to hidden pattern by asking what the material actually does. Her own shadow is the reverse risk: trained empiricism can become impatience with meanings or possibilities that cannot yet be materially demonstrated. She remains an independent center of judgement rather than Claes' missing half.
  guardrails:
  - Do not reduce Mayken to lover, healer, therapist, decoder or corrective device.
  - Her later conjunctio with Claes requires two centers of agency.
  - Childhood acquaintance is non-romantic.

- id: STC.CHARACTER.DEE.MAGICIAN_MENTOR.001
  type: StoryClaim
  status: CANON
  evidence_status: PLAUSIBLE
  decision_id: DEC.CHARACTER_WEB.CORE_CAST.2026-08-19
  claim: >-
    In novel characterization John Dee is intellectually daring, intensely observant and capable of showing Claes relations beneath ordinary appearance. He can recognize Claes' way of seeing rather than creating it. His shadow is overpatterning, secrecy, pride and the impulse to control access to knowledge; under pressure his perception of hidden relations can shade into suspicion or paranoia.
  guardrails:
  - These personal habits are fiction characterization of a historical person, not biographical claims unless separately sourced.
  - Dee must be wrong sometimes, especially when material verification contradicts suspicion.
  - Do not let Dee become the Storybible speaking in aphorisms.

- id: STC.CHARACTER.SILVIUS.TRANSMISSION_REALITY.001
  type: StoryClaim
  status: CANON
  evidence_status: PLAUSIBLE
  decision_id: DEC.CHARACTER_WEB.CORE_CAST.2026-08-19
  claim: >-
    In novel characterization Willem Silvius is the pragmatic mediator who turns ideas into producible, movable and socially survivable things. He thinks in paper, labour, price, timing, routes, audiences and risk, and can puncture learned grandiosity with calm practical leverage. His shadow is instrumentalism: people, texts and secrecy can become resources in a production problem if expedience outruns moral attention.
  guardrails:
  - These private habits are fiction characterization unless independently sourced.
  - Do not make pragmatism equal cowardice or cynicism.
  - Silvius' transmission role does not make him the translator of the Brevísima.

- id: STC.CHARACTER.LAS_CASAS.WITNESS_CONSCIENCE.001
  type: StoryClaim
  status: CANON
  evidence_status: PLAUSIBLE
  decision_id: DEC.CHARACTER_WEB.CORE_CAST.2026-08-19
  claim: >-
    The novel uses Bartolome de las Casas as witness/conscience and distant moral mirror for Claes: a man who receives, orders and transmits testimony, who knows that he himself once participated in the system he condemns, and who must eventually release a text whose later readers and uses he cannot control. His shadow is the temptation to believe that precision, rhetorical ordering or moral urgency can control reception.
  guardrails:
  - Historical acts and published positions require source support; interior thoughts in the prologue are fictional reconstruction.
  - Do not make him morally spotless; self-implication is part of the function.
  - His role is not direct mentorship of Claes.

- id: STC.CLAES_MAYKEN.CHILDHOOD_ACQUAINTANCE.001
  type: StoryClaim
  status: CANON
  evidence_status: PLAUSIBLE
  decision_id: DEC.CLAES_MAYKEN.CHILDHOOD_ACQUAINTANCE.2026-08-19
  claim: >-
    Before 18 May 1554 Claes and Mayken know one another as Goese children. Play and early plant/material observation give them a small shared history, but no childhood romantic bond is canonized.
  guardrails:
  - Later recognition may carry memory without implying destiny.
  - Mayken's fire experience remains different from Claes' catastrophic household loss.
```

---

# SOURCE FILE: `storybible/FAMILY_CLAES_1542_1554.md`

```markdown
# Claes Nissepat — familie 1542–1554

**Status:** CANON — approved 14 August 2026  
**Decision:** `DEC.CLAES.EXTENDED_FAMILY.2026-08-14`  
**Story Claim:** `STC.CLAES.EXTENDED_FAMILY.001`

This module is the authoritative family dossier for Claes' childhood household and grandparents. It distinguishes archival persons and property evidence from deliberate novel genealogy.

## 1. Family tree

```text
PATERNAL LINE                                      MATERNAL LINE

Jacob NN                                           [earlier generation unknown]
│                                                  │
└── Claes Jacobsz. Nissepat ── Lijsbet Pietersdr. Jan Jansen, kuiper ── Mayken Pietersdr.
    historical person         fictional             historical model       fictional
    fictional grandfather     grandmother            + fictional kinship    grandmother
             │                                           │
             └──────────── Cornelis Claesz. ── Tanneken Jansdr. ──────────┘
                            fictional         fictional
                                  │
                    ┌─────────────┼─────────────┐
                    │             │             │
           Claes Corneliszn.  Jan Corneliszn.  unborn child
             8 Dec 1542       ca. June 1544     ca. six months gestation
                    │             │             │
                  lives       † 18 May 1554   † 18 May 1554
```

The tree is novel canon. Only source-backed historical persons/acts are archival facts.

## 2. Cornelis Claesz. Nissepat

Cornelis is the fictional son of the historical Claes Jacobsz. Nissepat and father of Claes and Jan. He is a Goese poorter, beer trader/biersteker and organizer of a family business rather than necessarily a master brewer himself. He links property, credit, transport, storage, barrels, harbour trade, books and networks.

His marriage to Tanneken connects the Nissepat property/trade line to a craft milieu modeled through a Goese cooper. That makes his practical knowledge of barrels and beer containers socially plausible without turning him into a cooper or brewer.

After the fire of 1554 Cornelis remains in Goes to rebuild shelter, livelihood, credit and business and to keep financing Claes' education. This labour is an act of love but produces physical separation: Claes goes to Reimerswaal while Cornelis stays in Goes.

## 3. Tanneken Jansdochter — ca. 1520–18 May 1554

Tanneken Jansdochter is fictional and canonical. She is born approximately 1519–1522, with ca. 1520 as the preferred story date. She marries Cornelis and is mother of Claes, Jan and an unborn third child.

Tanneken is not written as a passive domestic figure or as a mystical wise woman. Her intelligence is practical, bodily and sensory. She knows through repeated daily work: heat, smell, texture, fermentation, illness, drying cloth, food, wood, weather and household timing. She is one of the primary sources from which Claes learns that the body can know before an abstract explanation is available.

This is an important foundation of the *sinne* line. Long before Dee gives Claes intellectual methods, Tanneken teaches him — mostly without formal teaching — that reliable perception is embodied.

In May 1554 she is about six months pregnant. Claes may already have felt the unborn child move beneath her skin. That gives him an early benign experience of something that is real without being visible. The pregnancy must not be used mechanically as the reason she dies in the fire.

Tanneken dies in the Goese city fire of 18 May 1554 together with Jan and the unborn child. These deaths are novel canon, not historical victim identifications.

## 4. Jan Corneliszn. Nissepat — ca. June 1544–18 May 1554

Jan is fictional and canonical. He is approximately eighteen months younger than Claes and therefore nearly ten at the time of the fire. His name is fixed as **Jan Corneliszn. Nissepat**.

In novel canon he is named for Tanneken's father, the maternal-grandfather figure modeled on a historical Goese Jan Jansen kuiper.

Jan must be a full child character before he becomes a loss. His relationship with Claes combines affection, rivalry, irritation, loyalty, play, shared mischief and unfinished ordinary conflict. He is close enough in age to be a genuine competitor and companion rather than a dependent small child.

Their dramatic contrast is useful but must not become schematic:

- Claes tends to observe, compare and wait;
- Jan tends to act sooner, touch, test, climb, move and risk.

Sometimes Jan's haste costs him; sometimes it lets him see or achieve what Claes misses by thinking too long. The point is not that one boy is right and the other wrong, but that together they form a richer childhood equilibrium.

Jan's death therefore removes from Claes not only a loved brother but also a human capacity that Claes later has to rediscover: acting before complete certainty.

## 5. The unborn child

The third child remains unnamed and its sex remains unknown. On 18 May 1554 Tanneken is approximately six months pregnant.

Narratively the child represents a future that has already become real to the family but has not yet become visible. Claes can know the child through touch and movement. The death of mother and unborn child turns that early sensory knowledge into one of the deepest wounds in the *sinne* architecture.

Do not assign a retrospective name or sex unless separately decided later.

# Paternal grandparents

## 6. Claes Jacobsz. Nissepat — historical person, fictional grandfather

Claes Jacobsz. Nissepat is historically documented in Goese transport records. The corpus records him in 1534, 1540 and 1542. His purchase of the house in the older Nieuwstraat on 20 March 1542 is historical evidence. His role as father of Cornelis and grandfather of the protagonist is deliberate novel genealogy.

Historically supported anchors include:

- 1534: sale of a house at Noordeinde;
- 1540: sale of house and land by the Nissepad while the seller still appears as the eastern neighbour, indicating adjacent retained property at that moment;
- 20 March 1542: purchase of the house in the older Nieuwstraat, with street east and Jacob Dierixsen de Bye on north, west and south.

His historical occupation is not known. Do not label him archival 'brouwer', 'koopman' or another profession without new evidence. For novel use he functions as an older property-holding, credit-conscious Goese family patriarch whose experience includes buying, selling, holding and protecting assets.

In novel canon he makes the 1542 house available to Cornelis and Tanneken as their family home. He remains story-owner through the 1554 fire and loses the asset when the house becomes uninhabitable/destroyed. Despite this loss he can still help Cornelis preserve Claes' educational future through money, credit, contacts or practical support.

His relation to Claes carries a different knowledge tradition from Tanneken's: ownership, provenance, accounts, obligation, debt, transfer and the question of what belongs to whom.

## 7. Lijsbet Pietersdochter — fictional paternal grandmother

Lijsbet Pietersdochter is wholly fictional. She is born approximately 1498–1502 and is the wife of Claes Jacobsz. and mother of fictional Cornelis.

She dies in novel canon circa 1540–1541, before Claes can have a substantial personal memory of her. She therefore functions mainly through inherited material memory: household objects, habits, phrases, textiles, devotional objects or family stories that are said to have been hers.

Her earlier death also means Claes Jacobsz. has already experienced spousal bereavement before Cornelis loses Tanneken in 1554. This can give the older man recognition of Cornelis' grief without requiring him to become verbally demonstrative.

No archival identity, dates or marriage are claimed for Lijsbet.

# Maternal grandparents

## 8. Jan Jansen, kuiper — historical model with fictional kinship

The maternal-grandfather figure is modeled on a real Goese archival pattern: transport records contain a **Jan Jansen kuiper** in the 1530s–1540s. A 2 August 1541 act records Jan Jansen kuiper buying a house by the Speelhuis; a 15 October 1543 act records heirs of a Jan Jansen kuiper transferring a house in the same environment.

This is useful historical material but must be handled conservatively. `Jan Jansen` is a generic name, and the normalized corpus groups additional same-name kuiper mentions, including later direct acts. The corpus may therefore conflate more than one man. We do **not** claim to have identified Tanneken's real father.

Novel canon uses a fictionalized maternal-grandfather figure modeled on this Goese cooper milieu. In the story he is Tanneken's father, husband of Mayken Pietersdochter and the man after whom Jan Corneliszn. is named.

His story death is placed around 1543. That date is a deliberate reconstruction supporting the naming of Jan in 1544; it is not an archival death date and must never be presented as one.

The cooper's craft connects naturally to Cornelis' beer trade: staves, hoops, swelling wood, leakage, cleaning, barrels, return casks and harbour logistics. Symbolic resonance may emerge later — a vessel carries its content without being identical to it — but he must first remain a plausible craftsman in a material economy, not an allegorical teacher.

## 9. Mayken Pietersdochter — fictional maternal grandmother

Mayken Pietersdochter is wholly fictional, born approximately 1498–1503. In novel canon she is widow of the maternal-grandfather figure, mother of Tanneken and maternal grandmother of Claes and Jan. She is alive in 1554.

Her knowledge is ordinary female household expertise rather than professional medicine or learned botany: textile, food preservation, pregnancy and birth experience, ordinary household herbs, care of illness and mourning ritual. This must remain distinct from the later specialist apothecary environment of Claes' beloved.

After the 1554 fire Mayken can provide what Claes Jacobsz. cannot primarily provide: bodily care, continuity with Tanneken, remembered stories, clothing, household objects and a place in which grief does not need explanation.

The two surviving grandparents therefore have complementary post-fire functions:

- **Mayken preserves what remains of the family memory and care.**
- **Claes Jacobsz. helps preserve what remains of Claes' material and educational future.**

Neither can restore the household that was lost.

# 10. The family as Claes' first knowledge system

The family should not be designed as a retrospective set of symbols, yet it organically gives Claes several forms of knowledge before his later intellectual formation:

- **Claes Jacobsz.:** ownership, provenance, debt, continuity and transfer;
- **Lijsbet:** inherited material memory and absence;
- **Jan Jansen kuiper model:** craft, containment, vessel and material reliability;
- **Mayken:** care, body, household memory and ritual;
- **Cornelis:** trade, networks, writing, responsibility, secrecy and movement;
- **Tanneken:** embodied sensory knowledge;
- **Jan:** action, risk, rivalry and immediacy;
- **Claes:** observation, comparison, pattern and eventually synthesis.

Thus later concepts such as carrier/content, embodied *sinne*, material transformation and transmission do not arrive from nowhere when Claes meets learned adults. Dee and others give intellectual articulation to structures Claes has already lived inside.

# 11. The 18 May 1554 rupture

Immediately before the fire the household consists of five lives if the unborn child is counted: Cornelis, Tanneken, Claes, Jan and the unborn child.

In novel canon the older-Nieuwstraat home becomes uninhabitable/is destroyed. Cornelis and Claes survive because they are away from the house. Tanneken, Jan and the unborn child die.

Historically, burned houses are documented in the older Nieuwstraat/Armenhoek environment after the fire, while other houses in Nieuwstraat also survive. The specific destruction of the 1542 Nissepat house and the deaths of these family members are therefore plausible novel reconstruction, **not archival fact**.

The result is not simply that Claes becomes motherless. A family of five is reduced to a father and son, and those two survivors are subsequently geographically separated because Cornelis must remain in Goes while Claes' education is salvaged through Reimerswaal.

This gives 1554 its correct dramatic function: loss of people, home, sibling equilibrium, bodily safety and daily paternal presence in one historical catastrophe.

# 12. Hard guardrails

- Tanneken Jansdochter and Jan Corneliszn. Nissepat are canonical names.
- Jan is approximately eighteen months younger than Claes; do not turn him into a much younger child.
- Tanneken is approximately six months pregnant on 18 May 1554.
- The unborn child's sex and name remain unknown.
- Tanneken, Jan, Lijsbet and Mayken are fictional.
- Claes Jacobsz. Nissepat is historical; his kinship to Cornelis/Claes is fictional.
- The maternal-grandfather figure is a fictional kinship/model built from historical Jan Jansen-kuiper evidence; do not claim a proven archival genealogy or exact death date.
- Claes Jacobsz.' historical profession remains unknown.
- Mayken is not an apothecary substitute.
- Jan must have a lived relationship with Claes before his death; do not write him merely as trauma machinery.
- The 1554 household deaths and destruction of the specific house remain novel canon within a historically supported fire environment.
```

---
