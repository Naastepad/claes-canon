# Claude Storybible access routing — 19 August 2026

## Problem observed

Claude's existing repository instructions correctly stated that GitHub `main` is authoritative, but the access pattern still required too much ad-hoc discovery:

- `prompts/CLAUDE_PROJECT_INSTRUCTIONS.md` started from `AI_ONBOARDING.md` and then exposed many individual URLs;
- it hard-coded a `Latest dated human decisions — 16 Aug 2026` link even after later dated decision files existed;
- it exposed the `canon/` directory listing as a discovery mechanism;
- the generated `CLAUDE_CONTEXT_INDEX.md` already had thematic packs but was not the primary bootstrap in Project Instructions;
- the context generator did not have a dedicated core-character pack, so current characterization/archetypal continuity could be missed unless Claude happened to discover the new dossier.

The result was a process risk: Claude could discover a technically relevant but partial/lower-authority file before the governing current layer, or conclude that a topic was absent because it had not yet found the right dossier.

## Operational decision

Claude must be **routed into the Storybible by task type before repository discovery**.

The stable primary entrypoint is now:

`prompts/CLAUDE_CONTEXT_INDEX.md`

Literal URL:

`https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_INDEX.md`

The generated index is now explicitly a **Task Router**, not merely a list of packs.

## Mandatory pack routing

After regeneration on `main`, the router assigns:

- canon / chronology / continuity / historical-fiction boundary: `01_CORE_CANON` + `05_DATED_DECISIONS`;
- named recurring character / relationship / motivation / archetype / characterization: `01_CORE_CANON` + `05_DATED_DECISIONS` + `06_CHARACTER_WEB`;
- chapter or scene construction: `01_CORE_CANON` + `05_DATED_DECISIONS` + `02_STORYBIBLE_PROJECTION` + `03_WRITING_EDITORIAL` + `06_CHARACTER_WEB`;
- hard critique/revision: same as chapter/scene construction;
- any Mayken task: add `04_MAYKEN_KNOWLEDGE`;
- repository mutation: core + dated decisions first, then task-specific packs, then fresh-fetch exact mutation targets;
- cold-reader: explicit exception; Storybible preload is forbidden for the cold-reader pass.

## New `06_CHARACTER_WEB` pack

The generator now gives Claude a dedicated pack containing the current governing character layer, including:

- `storybible/CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md`;
- `entities/CHARACTERIZATION_2026-08-19.yaml`;
- `narrative/character_web_archetypes.yaml`;
- `canon/DECISIONS_CHARACTER_WEB_2026-08-19.yaml`;
- `claims/STORY_CLAIMS_CHARACTER_WEB_2026-08-19.yaml`;
- the family, Claes-Cornelis, Puttus and Mayken governing dossiers needed to keep those recurrent characters human and continuous.

This means archetypal/personality continuity is assigned before drafting instead of discovered opportunistically.

## Guided-discovery rule

After the task-assigned packs are fully loaded, Claude may fetch an additional dossier only when:

1. the loaded `MASTER`, `INDEX`, `DEC.*`, `STC.*` or governing dossier explicitly names it;
2. the user explicitly requests repository-wide discovery/audit; or
3. a named dependency is demonstrably moved/missing/stale.

Claude should fetch the named file directly.

Directory roaming and keyword search are not the normal Storybible reading strategy and must not determine which record is authoritative.

## Access/truncation rule

If a required literal pack URL cannot be fetched, Claude reports the exact failed URL and stops canon-sensitive conclusions. It may not replace that pack with memory or an improvised repository search.

If a pack is truncated, Claude reports the last visible `SOURCE FILE` heading and stops until the missing portion is available.

## Files changed for this access repair

- `prompts/CLAUDE_PROJECT_INSTRUCTIONS.md` — task-router-first Project Instructions;
- `CLAUDE.md` — model-specific entrypoint now points first to the generated router;
- `scripts/generate_claude_context_pack.py` — deterministic task routing plus `06_CHARACTER_WEB` generation.

## Important deployment boundary

Updating `prompts/CLAUDE_PROJECT_INSTRUCTIONS.md` in GitHub does **not** automatically replace text already pasted into a Claude Project's Project Instructions. A Claude Project using an older copied version requires a one-time manual refresh of its Project Instructions. After that refresh, the stable context-index URL is the primary bootstrap and future pack/decision updates are obtained dynamically from GitHub `main`.

This is an access/configuration boundary, not a Storybible canon issue.
