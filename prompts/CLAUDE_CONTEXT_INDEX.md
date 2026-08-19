# Claude Context Index / Task Router — GENERATED

> **This is Claude's primary repository entrypoint. Do not start a canon-sensitive task by browsing the repository.**
> GitHub `main` remains authoritative; these are generated projections from the current main branch.
> `01_CORE_CANON` is not the complete decision registry. Current dated/supplemental decisions live in `05_DATED_DECISIONS` and may override or extend `canon/DECISIONS.yaml`.
> The task router below assigns the packs to load. Load them completely before analysis, prose or repository conclusions.

- source commit: `d05b988e7b24e06cfdef0fc367975d16fb57fb98`
- generated UTC: `2026-08-19T08:30:50+00:00`

## Pack URLs

1. `01_CORE_CANON` — 11 files
   https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_01_CORE_CANON.md

2. `02_STORYBIBLE_PROJECTION` — 15 files
   https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_02_STORYBIBLE_PROJECTION.md

3. `03_WRITING_EDITORIAL` — 8 files
   https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_03_WRITING_EDITORIAL.md

4. `04_MAYKEN_KNOWLEDGE` — 5 files
   https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_04_MAYKEN_KNOWLEDGE.md

5. `05_DATED_DECISIONS` — 19 files
   https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_05_DATED_DECISIONS.md

6. `06_CHARACTER_WEB` — 9 files
   https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_06_CHARACTER_WEB.md

## Mandatory task router

Classify the user's task first, then load the exact pack set below. Do not replace this with ad-hoc repository browsing.

- **Canon / chronology / historical-fiction boundary / continuity question:** `01_CORE_CANON` + `05_DATED_DECISIONS`.
- **Named recurring character, relationship, motivation, archetype or characterization:** `01_CORE_CANON` + `05_DATED_DECISIONS` + `06_CHARACTER_WEB`.
- **Chapter or scene construction:** `01_CORE_CANON` + `05_DATED_DECISIONS` + `02_STORYBIBLE_PROJECTION` + `03_WRITING_EDITORIAL` + `06_CHARACTER_WEB`.
- **Hard critique / revision / editor pass:** `01_CORE_CANON` + `05_DATED_DECISIONS` + `02_STORYBIBLE_PROJECTION` + `03_WRITING_EDITORIAL` + `06_CHARACTER_WEB`.
- **Any task in which Mayken appears or her arc/relationship matters:** add `04_MAYKEN_KNOWLEDGE` to the applicable set above.
- **Repository mutation:** first load `01_CORE_CANON` + `05_DATED_DECISIONS`; then load the task-specific packs above and fresh-fetch only the exact target files before writes.
- **Cold-reader pass:** do NOT load Storybible packs; follow `READER_EXPERIENCE_PROTOCOL.md` with deliberately restricted context. A cold-reader task is the explicit exception to this router.

## Mandatory editor output after cold-read/revision

After an editor pass that changes prose, do not return only revised chapters. Produce a **Chapter Revision Handoff** for every changed chapter with: editorial verdict; progression before; progression after; progression delta; retained functions; cut/moved functions; PARK.* classification for reusable material; receiving chapter if moved; canon impact (NONE / PROJECTION_ONLY / CANON_REVIEW_REQUIRED); cluster effect; and any OPEN.* risk. This handoff is the input for `narrative/manuscript_progression.yaml` and `narrative/parked_material.yaml`.

A raw text diff proves that text changed; it does not determine whether deleted material became backstory, backline, backdrop, future-scene reserve or rejected story. Use the explicit editor/author disposition.

## Guided-discovery rule

After the assigned packs are loaded, use `storybible/INDEX.md`, `storybible/MASTER.md` and explicit file references inside the loaded material to fetch any additional dossier. Fetch named files directly. **Do not roam directory listings, keyword-search the repository for inspiration, or infer canon by whichever file happens to be discovered first.**

Repository/directory search is a fallback only when:
1. a loaded governing record explicitly names a dependency that is not already in the assigned packs; or
2. the user explicitly asks for repository-wide discovery/audit; or
3. a named file has moved and the current index/manifest is demonstrably stale.

If fallback discovery is required, report the reason and resolve back to the authority hierarchy before drawing conclusions.

## Preflight before writing or concluding

Before prose, revision or a canon conclusion, internally establish:
- loaded pack set;
- governing `DEC.*` / `STC.*` / dossier(s);
- current chapter progression and parked-material state where manuscript work is involved;
- relevant character/relationship/object/knowledge state;
- active `OPEN.*` items that must remain open;
- evidence-vs-fiction boundary;
- missing/truncated input, if any.

Do not begin literary prose while a required pack is missing or truncated. Do not ask the user to rediscover a file that is already named in a loaded index/pack.

## Truncation / access failure

- If a pack is truncated, report the last `SOURCE FILE` heading seen and stop canon-sensitive conclusions until the remainder is available.
- If a literal pack URL cannot be fetched, report that exact URL. Do not replace the missing pack with memory or an improvised repository search.
- Never conclude that a decision or dossier is absent merely because one pack omits it.