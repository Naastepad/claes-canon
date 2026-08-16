# Claude Context Index — GENERATED

> Use this index for Claude Chat. Fetch the thematic packs explicitly supplied by the user.
> GitHub `main` remains authoritative; these are generated projections.

- source commit: `f541df06f3c3b0fe8f4d058edd060926091f7e19`
- generated UTC: `2026-08-16T19:20:27+00:00`

## Recommended load order

1. `01_CORE_CANON` — 11 files
   https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_01_CORE_CANON.md

2. `02_STORYBIBLE_PROJECTION` — 9 files
   https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_02_STORYBIBLE_PROJECTION.md

3. `03_WRITING_EDITORIAL` — 5 files
   https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_03_WRITING_EDITORIAL.md

4. `04_MAYKEN_KNOWLEDGE` — 4 files
   https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_04_MAYKEN_KNOWLEDGE.md

5. `05_DATED_DECISIONS` — 15 files
   https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_05_DATED_DECISIONS.md

## Task loading

- Canon/history question: load `01_CORE_CANON` plus `05_DATED_DECISIONS` when recent decisions may matter.
- Chapter/scene construction: also load `02_STORYBIBLE_PROJECTION` and `03_WRITING_EDITORIAL`.
- Any Mayken scene: also load `04_MAYKEN_KNOWLEDGE`.
- Hard critique/revision: load `01_CORE_CANON`, `02_STORYBIBLE_PROJECTION`, and `03_WRITING_EDITORIAL`.
- If a pack is truncated, report the last SOURCE FILE heading seen; do not pretend the remainder was read.