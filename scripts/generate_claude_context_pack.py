#!/usr/bin/env python3
"""Generate a single self-contained Claude context pack.

Claude Chat's restricted web fetcher may refuse URLs merely mentioned inside an
already fetched document. This generator therefore concatenates the canonical
files Claude needs for canon-sensitive writing/revision into one raw-fetchable
file. GitHub remains source of truth; the pack is a generated projection only.
"""
from __future__ import annotations

from pathlib import Path
from datetime import datetime, timezone
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "prompts" / "CLAUDE_CONTEXT_PACK.md"

FIXED = [
    "README.md",
    "AI_ONBOARDING.md",
    "CLAUDE.md",
    "REPOSITORY_INTEGRITY.md",
    "AUTHORING_POLICY.md",
    "AGENTS.md",
    "WRITING_PROTOCOL.md",
    "canon/DECISIONS.yaml",
    "canon/OPEN_DECISIONS.yaml",
    "review/SYNC_STATUS.md",
    "storybible/MASTER.md",
    "storybible/INDEX.md",
    "storybible/LEMMA_MCKEE_MASTER.md",
    "storybible/STORY_PROJECTION_ROUND_C.md",
    "storybible/MAYKEN_LAMPERT.md",
    "narrative/story_projection_round_c.yaml",
    "narrative/alchemical_authorial_architecture.yaml",
    "narrative/domain_scene_packs.yaml",
    "narrative/editorial_gates.yaml",
    "narrative/mayken_independent_arc.yaml",
    "narrative/mayken_relationship_projection.yaml",
    "narrative/knowledge_states.yaml",
    "narrative/instances.yaml",
    "narrative/arcs.yaml",
    "narrative/relationships.yaml",
    "narrative/motifs.yaml",
    "narrative/themes.yaml",
    "review/READER_EXPERIENCE_PROTOCOL.md",
    "review/READER_FEEDBACK_TEMPLATE.md",
]


def git_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
    except Exception:
        return "unknown"


def dated_decisions() -> list[str]:
    paths: list[str] = []
    cdir = ROOT / "canon"
    if not cdir.exists():
        return paths
    for p in sorted(cdir.glob("DECISIONS_*.md")):
        paths.append(p.relative_to(ROOT).as_posix())
    for p in sorted(cdir.glob("DECISIONS_*.yaml")):
        # DECISIONS.yaml itself is already fixed; include specialised dated registries.
        if p.name != "DECISIONS.yaml":
            paths.append(p.relative_to(ROOT).as_posix())
    return paths


def fence_for(path: str) -> str:
    if path.endswith((".yaml", ".yml")):
        return "yaml"
    if path.endswith(".json"):
        return "json"
    if path.endswith(".lemma"):
        return "text"
    return "markdown"


def main() -> None:
    files: list[str] = []
    for p in FIXED + dated_decisions():
        if p not in files and (ROOT / p).is_file():
            files.append(p)

    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    lines = [
        "# Claude Context Pack — GENERATED",
        "",
        "> **Generated projection; never edit by hand.** GitHub source files remain authoritative.",
        "> This pack exists solely because some Claude Chat fetch environments only allow URLs",
        "> explicitly supplied by the user and cannot traverse repository links reliably.",
        "",
        f"- source branch: `main`",
        f"- source commit at generation: `{git_sha()}`",
        f"- generated UTC: `{timestamp}`",
        f"- included files: `{len(files)}`",
        "",
        "## Claude operating rule",
        "",
        "Treat every section below exactly as the source file named in its heading. Apply the",
        "authority hierarchy in `AI_ONBOARDING.md`; physical order inside this concatenated pack",
        "does not change authority. If this pack conflicts with a newer explicitly supplied GitHub",
        "file, the newer source file wins and the pack should be regenerated.",
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

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} with {len(files)} source files")


if __name__ == "__main__":
    main()
