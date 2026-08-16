# AI Canon Authoring Instructions

This repository is the controlled operating Storybible and canon layer for **Claes Nissepat**.

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
10. `AUTHORING_POLICY.md` and `REPOSITORY_INTEGRITY.md` before any repository write

The dated `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` is legacy/audit only. These rules apply to ChatGPT, Claude, Gemini, Copilot, local agents and other models. Never create a competing canon in session memory.

## Primary objective
Preserve narrative meaning, historical provenance, author decisions, chapter-ready world knowledge and deterministic continuity without conflating evidence, interpretation, story choice or narrative theory.

## Mandatory pre-write integrity protocol
A write-capable agent MUST:
1. Re-fetch the target branch and every file it intends to modify immediately before writing. Never write from remembered or previously cached content when another session may have changed the repository.
2. Verify the intended branch. Do not write canon-development changes directly to `main` unless the human explicitly orders that action or the active conversation clearly continues an already authorized direct-main synchronization round.
3. Read all applicable current `canon/DECISIONS*` records before modifying downstream representations.
4. Preserve stable IDs. Never silently rename, recycle or duplicate an existing `SC.*`, `STC.*`, `DEC.*`, `ENT.*`, `OBJ.*`, `NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`, `WORLD.*`, `CODE.*` or `OPEN.*` identity.
5. Make the smallest coherent change set. If a canon decision affects multiple layers, update all affected layers in the same synchronization pass or record an explicit `SYNC_PENDING` item; never leave silent drift.
6. Re-fetch a file after writing when subsequent writes depend on its new SHA/content.
7. Never force-update a branch, overwrite another agent's unreviewed work, merge a PR, close a PR, publish to LemmaBase, or delete canon/history unless the human explicitly requests that operation.
8. If the repository changed unexpectedly during the task, stop destructive writes, compare the new state, preserve both lines of work, and report the conflict.
9. Run or inspect repository and Lemma validation after structural/canon changes. A green syntax check does not override a human canon conflict.
10. Leave a repository-visible handoff for substantial work: what was read, what changed, what remains open, and which records still require synchronization.

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

Historical evidence (`SC.*`) does not become story canon merely because it is verified. External `KO.*` narrative theory never overrides Claes canon.

## Read order for authoring changes
1. onboarding, current `canon/`, sync status and operating master
2. `storybible/STORY_PROJECTION_ROUND_C.md` plus `narrative/story_projection_round_c.yaml` when plot/scene/structure is involved
3. relevant `STC.*`, `ENT.*`, `OBJ.*`, `NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`, `WORLD.*`
4. relevant `narrative/domain_scene_packs.yaml` and chapter-ready practice dossiers
5. relevant `SC.*` and source records
6. relevant `OPEN.*`
7. `mapping/CONVERSION_LEDGER.yaml` when source coverage matters
8. Lemma only for deterministic questions
9. external `KO.*` only for narrative diagnosis

## Chapter/scene projection rule
For scene construction, do not start from “what research can I use?”. Start from:

1. Which hinge in `ARC.CLAES.CAUSAL_SPINE` is being advanced?
2. Which person makes the consequential choice?
3. Which Corpus/Anima/Spiritus register(s) are materially active?
4. Which world/practice pack supplies the historically bounded actions and objects?
5. What changes in value, knowledge, relationship, object state or responsibility?
6. Which `OPEN.*` matter must remain open?

`ARC.CLAES.GREAT_WORK.AUTHORIAL` is author-side architecture. Corpus/Anima/Spiritus are interwoven registers, not three mechanically repeated cycles and not mandatory prose labels.

## Mayken rule
`ENT.PERSON.BELOVED` is a legacy stable entity ID whose identity is **resolved** as Mayken Adriaensdr. Lampert.

If Mayken appears, load:
- `storybible/MAYKEN_LAMPERT.md`;
- `narrative/mayken_independent_arc.yaml` (`ARC.MAYKEN.LIFE`);
- `narrative/mayken_relationship_projection.yaml` (`REL.CLAES.MAYKEN.CONJUNCTIO`);
- relevant Lampert source claims if historical grounding matters.

Never write Mayken only as Claes' helper, reward, therapist or sensory device. A developed Mayken scene must give her an objective, judgement, cost or choice not reducible to Claes' immediate need.

## Mandatory behaviour
- Preserve provenance and source precision.
- Keep evidence status and canon status independent.
- Never invent missing dates, locations, relationships, quotations or bibliographic metadata.
- Never turn month/year precision into a fabricated exact day.
- Prefer a proposal/open authorial-design record over direct canon change when genuine uncertainty exists.
- Unatomized prose remains active source material through the conversion ledger.
- Keep Lemma focused on executable constraints, not prose storage or literary interpretation.
- Add/update validation when a schema or constraint changes.
- Explain downstream effects of canon changes.
- Never silently close `OPEN.*` decisions.
- Do not force an alchemical operation onto a scene merely to complete a pattern.

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
Migration origin: `MIGRATED / DERIVED / NEW`

## Reasoning boundary
Ask separately:
- What does historical evidence support? (`SC.*`)
- What has the author decided is true? (`canon/`, `DEC.*`, `STC.*`)
- What world/practice conditions are available? (`WORLD.*`, domain dossiers, scene packs)
- Where is it dramatized or causally projected? (`NI.*`, `ARC.CLAES.CAUSAL_SPINE`, arcs, motifs, relationships)
- Is it logically possible? (Lemma)
- Does it work narratively? (external `KO.*` diagnostics and writing/review protocol)

## Preferred synchronization pass
Human decision → affected Story Claims → entities/objects/knowledge states → world/practice domains → Narrative Instances/arcs/relationships/motifs/themes/values → causal/story projection → operating master/index → Lemma constraints if deterministic → validators/tests → sync review → handoff.

## Handoff rule
Do not rely on private chain-of-thought or chat memory for continuity. Repository state, explicit human decisions and validated records are the handoff between sessions.
