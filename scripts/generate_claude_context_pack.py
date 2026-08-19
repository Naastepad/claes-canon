#!/usr/bin/env python3
"""Generate Claude context packs sized for restricted chat fetchers.

Claude Chat may refuse repository traversal and may truncate one very large raw file.
This generator therefore builds an index plus several thematic, self-contained packs.
GitHub source files remain authoritative; generated packs are projections only.

The generated index is also the Claude task router: Claude should load the exact packs
assigned to the task before doing repository discovery or literary work.
"""
from __future__ import annotations

from pathlib import Path
from datetime import datetime, timezone
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PROMPTS = ROOT / "prompts"
FULL_OUT = PROMPTS / "CLAUDE_CONTEXT_PACK.md"
INDEX_OUT = PROMPTS / "CLAUDE_CONTEXT_INDEX.md"

PACKS = {
    "01_CORE_CANON": [
        "README.md",
        "AI_ONBOARDING.md",
        "CLAUDE.md",
        "REPOSITORY_INTEGRITY.md",
        "AUTHORING_POLICY.md",
        "AGENTS.md",
        "canon/DECISIONS.yaml",
        "canon/OPEN_DECISIONS.yaml",
        "review/SYNC_STATUS.md",
        "storybible/MASTER.md",
        "storybible/INDEX.md",
    ],
    "02_STORYBIBLE_PROJECTION": [
        "storybible/LEMMA_MCKEE_MASTER.md",
        "storybible/STORY_PROJECTION_ROUND_C.md",
        "storybible/GOES_SCHOOLING_PUTTUS_1550_1554.md",
        "storybible/domains/REIMERSWAAL_SCHOOL_1554_1561.md",
        "storybible/CLAES_CORNELIS_RELATION_1547_1569.md",
        "storybible/NISSEPAT_ARMS_SINT_JORIS_CORNELIS.md",
        "narrative/claes_cornelis_relationship_refinement_2026-08-18.yaml",
        "narrative/motifs_nissepat_arms_2026-08-18.yaml",
        "narrative/story_projection_round_c.yaml",
        "narrative/alchemical_authorial_architecture.yaml",
        "narrative/instances.yaml",
        "narrative/arcs.yaml",
        "narrative/relationships.yaml",
        "narrative/motifs.yaml",
        "narrative/themes.yaml",
    ],
    "03_WRITING_EDITORIAL": [
        "WRITING_PROTOCOL.md",
        "narrative/domain_scene_packs.yaml",
        "narrative/editorial_gates.yaml",
        "review/READER_EXPERIENCE_PROTOCOL.md",
        "review/READER_FEEDBACK_TEMPLATE.md",
    ],
    "04_MAYKEN_KNOWLEDGE": [
        "storybible/MAYKEN_LAMPERT.md",
        "narrative/mayken_independent_arc.yaml",
        "narrative/mayken_relationship_projection.yaml",
        "narrative/beloved_recovery.yaml",
        "narrative/knowledge_states.yaml",
    ],
}

CHARACTER_WEB_FILES = [
    "storybible/CHARACTER_WEB_ARCHETYPES_AND_CHARACTERIZATION.md",
    "entities/CHARACTERIZATION_2026-08-19.yaml",
    "narrative/character_web_archetypes.yaml",
    "canon/DECISIONS_CHARACTER_WEB_2026-08-19.yaml",
    "claims/STORY_CLAIMS_CHARACTER_WEB_2026-08-19.yaml",
    "storybible/FAMILY_CLAES_1542_1554.md",
    "storybible/CLAES_CORNELIS_RELATION_1547_1569.md",
    "storybible/GOES_SCHOOLING_PUTTUS_1550_1554.md",
    "storybible/MAYKEN_LAMPERT.md",
]


def git_sha() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        return "unknown"


def dated_decisions() -> list[str]:
    out: list[str] = []
    cdir = ROOT / "canon"
    if not cdir.exists():
        return out
    for p in sorted(cdir.glob("DECISIONS_*.md")):
        out.append(p.relative_to(ROOT).as_posix())
    for p in sorted(cdir.glob("DECISIONS_*.yaml")):
        if p.name != "DECISIONS.yaml":
            out.append(p.relative_to(ROOT).as_posix())
    return out


def fence_for(path: str) -> str:
    if path.endswith((".yaml", ".yml")):
        return "yaml"
    if path.endswith(".json"):
        return "json"
    if path.endswith(".lemma"):
        return "text"
    return "markdown"


def existing(paths: list[str]) -> list[str]:
    return [p for p in paths if (ROOT / p).is_file()]


def render_pack(title: str, files: list[str], sha: str, timestamp: str) -> str:
    lines = [
        f"# Claude Context Pack — {title} — GENERATED",
        "",
        "> Generated projection; never edit by hand. GitHub source files remain authoritative.",
        "> Treat each SOURCE FILE section as the original source file.",
        "> Do not use this pack as permission for free repository discovery; follow the task router in CLAUDE_CONTEXT_INDEX.md.",
        "",
        "- source branch: `main`",
        f"- source commit at generation: `{sha}`",
        f"- generated UTC: `{timestamp}`",
        f"- included files: `{len(files)}`",
        "",
        "Apply the authority hierarchy from `AI_ONBOARDING.md`. Physical order in this pack does not alter authority.",
        "",
        "---",
        "",
    ]
    for path in files:
        text = (ROOT / path).read_text(encoding="utf-8")
        lines += [
            f"# SOURCE FILE: `{path}`",
            "",
            f"```{fence_for(path)}",
            text.rstrip(),
            "```",
            "",
            "---",
            "",
        ]
    return "\n".join(lines)


def main() -> None:
    PROMPTS.mkdir(parents=True, exist_ok=True)
    sha = git_sha()
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")

    # Deliberate pack order. Dated decisions are generated dynamically and the
    # character-web pack is task-routed explicitly rather than left to discovery.
    packs = {name: existing(paths) for name, paths in PACKS.items()}
    packs["05_DATED_DECISIONS"] = existing(dated_decisions())
    packs["06_CHARACTER_WEB"] = existing(CHARACTER_WEB_FILES)

    all_files: list[str] = []
    for files in packs.values():
        for p in files:
            if p not in all_files:
                all_files.append(p)

    # Retain the full pack for agents that can consume it, but Claude Chat should prefer split packs.
    FULL_OUT.write_text(render_pack("FULL", all_files, sha, timestamp), encoding="utf-8")

    index_lines = [
        "# Claude Context Index / Task Router — GENERATED",
        "",
        "> **This is Claude's primary repository entrypoint. Do not start a canon-sensitive task by browsing the repository.**",
        "> GitHub `main` remains authoritative; these are generated projections from the current main branch.",
        "> `01_CORE_CANON` is not the complete decision registry. Current dated/supplemental decisions live in `05_DATED_DECISIONS` and may override or extend `canon/DECISIONS.yaml`.",
        "> The task router below assigns the packs to load. Load them completely before analysis, prose or repository conclusions.",
        "",
        f"- source commit: `{sha}`",
        f"- generated UTC: `{timestamp}`",
        "",
        "## Pack URLs",
        "",
    ]

    base = "https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts"
    for i, (name, files) in enumerate(packs.items(), start=1):
        filename = f"CLAUDE_CONTEXT_{name}.md"
        out = PROMPTS / filename
        out.write_text(render_pack(name, files, sha, timestamp), encoding="utf-8")
        index_lines += [
            f"{i}. `{name}` — {len(files)} files",
            f"   {base}/{filename}",
            "",
        ]

    index_lines += [
        "## Mandatory task router",
        "",
        "Classify the user's task first, then load the exact pack set below. Do not replace this with ad-hoc repository browsing.",
        "",
        "- **Canon / chronology / historical-fiction boundary / continuity question:** `01_CORE_CANON` + `05_DATED_DECISIONS`.",
        "- **Named recurring character, relationship, motivation, archetype or characterization:** `01_CORE_CANON` + `05_DATED_DECISIONS` + `06_CHARACTER_WEB`.",
        "- **Chapter or scene construction:** `01_CORE_CANON` + `05_DATED_DECISIONS` + `02_STORYBIBLE_PROJECTION` + `03_WRITING_EDITORIAL` + `06_CHARACTER_WEB`.",
        "- **Hard critique / revision / editor pass:** `01_CORE_CANON` + `05_DATED_DECISIONS` + `02_STORYBIBLE_PROJECTION` + `03_WRITING_EDITORIAL` + `06_CHARACTER_WEB`.",
        "- **Any task in which Mayken appears or her arc/relationship matters:** add `04_MAYKEN_KNOWLEDGE` to the applicable set above.",
        "- **Repository mutation:** first load `01_CORE_CANON` + `05_DATED_DECISIONS`; then load the task-specific packs above and fresh-fetch only the exact target files before writes.",
        "- **Cold-reader pass:** do NOT load Storybible packs; follow `READER_EXPERIENCE_PROTOCOL.md` with deliberately restricted context. A cold-reader task is the explicit exception to this router.",
        "",
        "## Guided-discovery rule",
        "",
        "After the assigned packs are loaded, use `storybible/INDEX.md`, `storybible/MASTER.md` and explicit file references inside the loaded material to fetch any additional dossier. Fetch named files directly. **Do not roam directory listings, keyword-search the repository for inspiration, or infer canon by whichever file happens to be discovered first.**",
        "",
        "Repository/directory search is a fallback only when:",
        "1. a loaded governing record explicitly names a dependency that is not already in the assigned packs; or",
        "2. the user explicitly asks for repository-wide discovery/audit; or",
        "3. a named file has moved and the current index/manifest is demonstrably stale.",
        "",
        "If fallback discovery is required, report the reason and resolve back to the authority hierarchy before drawing conclusions.",
        "",
        "## Preflight before writing or concluding",
        "",
        "Before prose, revision or a canon conclusion, internally establish:",
        "- loaded pack set;",
        "- governing `DEC.*` / `STC.*` / dossier(s);",
        "- relevant character/relationship/object/knowledge state;",
        "- active `OPEN.*` items that must remain open;",
        "- evidence-vs-fiction boundary;",
        "- missing/truncated input, if any.",
        "",
        "Do not begin literary prose while a required pack is missing or truncated. Do not ask the user to rediscover a file that is already named in a loaded index/pack.",
        "",
        "## Truncation / access failure",
        "",
        "- If a pack is truncated, report the last `SOURCE FILE` heading seen and stop canon-sensitive conclusions until the remainder is available.",
        "- If a literal pack URL cannot be fetched, report that exact URL. Do not replace the missing pack with memory or an improvised repository search.",
        "- Never conclude that a decision or dossier is absent merely because one pack omits it.",
    ]
    INDEX_OUT.write_text("\n".join(index_lines), encoding="utf-8")

    print(f"Wrote full pack, task-router index and {len(packs)} thematic packs from {len(all_files)} source files")


if __name__ == "__main__":
    main()
