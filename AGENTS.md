# AI Canon Authoring Instructions

This repository is the controlled operating Storybible and canon layer for **Claes Nissepat**.

## Canonical AI instructions
Before canon-sensitive work, read in this order:
1. `AI_ONBOARDING.md`
2. `canon/` — all explicit human decisions; these outrank conflicting migrated or derived representations
3. `storybible/LEMMA_MCKEE_MASTER.md`
4. `WRITING_PROTOCOL.md` if drafting/revising/criticising prose
5. `AUTHORING_POLICY.md` and `REPOSITORY_INTEGRITY.md` before any repository write
6. `MIGRATION_REVIEW.md` while the migration PR remains open

These rules apply to ChatGPT, Claude, Gemini, Copilot, local agents and other models. Never create a competing canon in session memory.

## Primary objective
Preserve narrative meaning, historical provenance, author decisions and deterministic continuity without conflating evidence, interpretation, story choice or narrative theory.

## Mandatory pre-write integrity protocol
A write-capable agent MUST:
1. Re-fetch the target branch and every file it intends to modify immediately before writing. Never write from remembered or previously cached content when another session may have changed the repository.
2. Verify that the intended branch is an authoring/work branch. Do not write canon-development changes directly to `main` unless the human explicitly orders that exact action.
3. Read all applicable `canon/DECISIONS*.md` records before modifying downstream representations.
4. Preserve stable IDs. Never silently rename, recycle or duplicate an existing `SC.*`, `STC.*`, `DEC.*`, `ENT.*`, `OBJ.*`, `NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`, `WORLD.*`, `CODE.*` or `OPEN.*` identity.
5. Make the smallest coherent change set. If a canon decision affects multiple layers, update all affected layers in the same synchronization pass or record an explicit `SYNC_PENDING` item; never leave silent drift.
6. Re-fetch a file after writing when subsequent writes depend on its new SHA/content.
7. Never force-update a branch, overwrite another agent's unreviewed work, merge a PR, close a PR, publish to LemmaBase, or delete canon/history unless the human explicitly requests that operation.
8. If the repository changed unexpectedly during the task, stop destructive writes, compare the new state, preserve both lines of work, and report the conflict.
9. Run or inspect repository and Lemma validation after structural/canon changes. A green syntax check does not override a human canon conflict.
10. Leave a repository-visible handoff for substantial work: what was read, what changed, what remains open, and which records still require synchronization.

## Authority order on conflict
1. explicit human decisions in `canon/`
2. accepted `DEC.*` decision registry records
3. active `STC.*` Story Claims
4. entity/object/narrative registers derived from those claims
5. `storybible/LEMMA_MCKEE_MASTER.md` as coherent human-readable synthesis
6. migrated source Storybible prose via the conversion ledger
7. proposals, OPEN records and AI interpretations
8. chat/session memory

Historical evidence (`SC.*`) does not become story canon merely because it is verified. External `KO.*` narrative theory never overrides Claes canon.

## Read order for authoring changes
1. onboarding, `canon/`, and operating master
2. `mapping/CONVERSION_LEDGER.yaml` when source coverage matters
3. relevant `STC.*`, `ENT.*`, `OBJ.*`, `NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`, `WORLD.*`, `CODE.*`
4. relevant `SC.*` and source records
5. relevant `OPEN.*`
6. Lemma only for deterministic questions
7. external `KO.*` only for narrative diagnosis

## Mandatory behaviour
- Preserve provenance and source precision.
- Keep evidence status and canon status independent.
- Never invent missing dates, locations, relationships, quotations or bibliographic metadata.
- Never turn month/year precision into a fabricated exact day.
- Prefer a proposal over direct canon change when genuine uncertainty exists.
- Unatomized prose remains active source material through the conversion ledger.
- Keep Lemma focused on executable constraints, not prose storage or literary interpretation.
- Add/update validation when a schema or constraint changes.
- Explain downstream effects of canon changes.
- Never silently close `OPEN.*` decisions.

## Spatial reasoning rule — Goes and other atlas-backed settings
For questions about where a person **lives, owns property, works, operates a business, meets, travels or witnesses an event**, keep the spatial relation explicit. `RESIDES`, `OWNS`, `RENTS`, `OPERATES_BUSINESS`, `WORKS_AT`, `ADJOINS`, `USES` and `VISITS` are not interchangeable.

For Goes scene/topography work:
- read `narrative/world_goes_living_city.yaml` and the relevant `SC.HIST.GOES.*` records;
- use the Stadsatlas/transport-register layer for parcel topology, year-valid routes, named parties, occupations and belendingen;
- never infer residence from ownership, business location, adjacency or family proximity;
- never infer an exact parcel polygon from four belendingen alone;
- preserve the distinction between a transport/ownership chain and a physical place through time;
- apply the time slice before answering: streets, gates, institutional functions, damage zones and routes can change;
- if a route is requested, resolve the scene year and origin/destination first, then use year-valid street/gate/landmark anchors and report meaningful pass-by places rather than inventing a straight-line path;
- use modern/RCE street geometry as a reference crosswalk only where historical continuity is separately supported;
- keep the pre-1594 `Nieuwstraat` distinct from the planned `Nieuwstraat` of 1594 until `OPEN.GOES.NIEUWSTRAAT.PRE1594.001` is resolved;
- keep 1554 fire damage and 1572 military destruction as separate event footprints;
- if Cornelis' household residence matters, consult `OPEN.CORNELIS.RESIDENCE.GOES.1542.001` and report it as unresolved unless a human decision has closed it;
- if the exact Goese rederijkers meeting place matters, consult `OPEN.GOES.REDERIJKERS.MEETINGPLACE.001`; do not infer it from the Maria Magdalena devotional link.

A strong spatial answer should state: **where + relation to place + route + what is passed + who/what plausibly populates the route in that year + what has changed because of relevant events + certainty/open status**.

## State vocabularies
Evidence: `VERIFIED / SUPPORTED / PLAUSIBLE / DISPUTED / UNKNOWN`
Canon: `PROPOSED / CANON / OPEN / DEPRECATED / REJECTED`
Migration origin: `MIGRATED / DERIVED / NEW`

## Reasoning boundary
Ask separately:
- What does historical evidence support? (`SC.*`)
- What has the author decided is true? (`canon/`, `DEC.*`, `STC.*`)
- Where is it dramatized? (`NI.*`, arcs, motifs, relationships)
- Is it logically possible? (Lemma)
- Does it work narratively? (external `KO.*` diagnostics)

## Preferred synchronization pass
Human decision → affected Story Claims → entities/objects/knowledge states → Narrative Instances/arcs/relationships/motifs/themes/values → operating master → Lemma constraints if deterministic → validators/tests → migration/sync review → handoff.

## Handoff rule
Do not rely on private chain-of-thought or chat memory for continuity. Repository state, explicit human decisions and validated records are the handoff between sessions.
