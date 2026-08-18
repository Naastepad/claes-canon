#!/usr/bin/env python3
"""Generate Claude context packs sized for restricted chat fetchers.

Claude Chat may refuse repository traversal and may truncate one very large raw file.
This generator therefore builds an index plus several thematic, self-contained packs.
GitHub source files remain authoritative; generated packs are projections only.
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
        "narrative/knowledge_states.yaml",
    ],
}


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

    packs = {name: existing(paths) for name, paths in PACKS.items()}
    packs["05_DATED_DECISIONS"] = existing(dated_decisions())

    all_files: list[str] = []
    for files in packs.values():
        for p in files:
            if p not in all_files:
                all_files.append(p)

    # Retain the full pack for agents that can consume it, but Claude Chat should prefer split packs.
    FULL_OUT.write_text(render_pack("FULL", all_files, sha, timestamp), encoding="utf-8")

    index_lines = [
        "# Claude Context Index — GENERATED",
        "",
        "> Use this index for Claude Chat. Fetch the thematic packs explicitly supplied by the user.",
        "> GitHub `main` remains authoritative; these are generated projections.",
        "> IMPORTANT: `01_CORE_CANON` is not the complete decision registry. Current dated/supplemental decisions live in `05_DATED_DECISIONS` and may override or extend `canon/DECISIONS.yaml`.",
        "",
        f"- source commit: `{sha}`",
        f"- generated UTC: `{timestamp}`",
        "",
        "## Recommended load order",
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
        "## Task loading",
        "",
        "- Any canon-sensitive or history/continuity question: ALWAYS load `01_CORE_CANON` AND `05_DATED_DECISIONS`. Never infer that a decision is absent merely because it is missing from `canon/DECISIONS.yaml`.",
        "- Chapter/scene construction: load `01_CORE_CANON`, `05_DATED_DECISIONS`, `02_STORYBIBLE_PROJECTION`, and `03_WRITING_EDITORIAL`.",
        "- Any Mayken scene: also load `04_MAYKEN_KNOWLEDGE`.",
        "- Hard critique/revision: load `01_CORE_CANON`, `05_DATED_DECISIONS`, `02_STORYBIBLE_PROJECTION`, and `03_WRITING_EDITORIAL`.",
        "- If a pack is truncated, report the last SOURCE FILE heading seen; do not pretend the remainder was read.",
    ]
    INDEX_OUT.write_text("\n".join(index_lines), encoding="utf-8")

    print(f"Wrote full pack, index and {len(packs)} thematic packs from {len(all_files)} source files")


if __name__ == "__main__":
    main()
