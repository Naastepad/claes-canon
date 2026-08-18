# Claude Context Index — GENERATED

> Use this index for Claude Chat. Fetch the thematic packs explicitly supplied by the user.
> GitHub `main` remains authoritative; these are generated projections.
> IMPORTANT: `01_CORE_CANON` is not the complete decision registry. Current dated/supplemental decisions live in `05_DATED_DECISIONS` and may override or extend `canon/DECISIONS.yaml`.

- source commit: `3b2960e741d81db1b1542bb2a6e2564ef686b615`
- generated UTC: `2026-08-18T08:11:51+00:00`

## Recommended load order

1. `01_CORE_CANON` — 11 files
   https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_01_CORE_CANON.md

2. `02_STORYBIBLE_PROJECTION` — 11 files
   https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_02_STORYBIBLE_PROJECTION.md

3. `03_WRITING_EDITORIAL` — 5 files
   https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_03_WRITING_EDITORIAL.md

4. `04_MAYKEN_KNOWLEDGE` — 4 files
   https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_04_MAYKEN_KNOWLEDGE.md

5. `05_DATED_DECISIONS` — 16 files
   https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_05_DATED_DECISIONS.md

## Task loading

- Any canon-sensitive or history/continuity question: ALWAYS load `01_CORE_CANON` AND `05_DATED_DECISIONS`. Never infer that a decision is absent merely because it is missing from `canon/DECISIONS.yaml`.
- Chapter/scene construction: load `01_CORE_CANON`, `05_DATED_DECISIONS`, `02_STORYBIBLE_PROJECTION`, and `03_WRITING_EDITORIAL`.
- Any Mayken scene: also load `04_MAYKEN_KNOWLEDGE`.
- Hard critique/revision: load `01_CORE_CANON`, `05_DATED_DECISIONS`, `02_STORYBIBLE_PROJECTION`, and `03_WRITING_EDITORIAL`.
- If a pack is truncated, report the last SOURCE FILE heading seen; do not pretend the remainder was read.