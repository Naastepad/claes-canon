#!/usr/bin/env python3
"""Repository-level continuity compiler for Claes.

This validates the structured storybible layer. Lemma syntax is validated separately.
The validator is deliberately conservative: it rejects broken references and status
vocabulary, but does not infer missing historical facts or story decisions.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
STRUCTURED = [ROOT / "claims", ROOT / "entities", ROOT / "narrative"]

EVIDENCE = {"VERIFIED", "SUPPORTED", "PLAUSIBLE", "DISPUTED", "UNKNOWN"}
CANON = {"PROPOSED", "CANON", "OPEN", "DEPRECATED", "REJECTED"}
ID_RE = re.compile(r"^(SC|STC|DEC|ENT|NI|ARC|MOTIF|REL)\.[A-Z0-9_.-]+$")
SOURCE_RE = re.compile(r"^SRC-[A-Z0-9_.-]+$")

errors: list[str] = []
records: list[tuple[Path, dict]] = []
all_ids: dict[str, Path] = {}
source_ids = {p.stem for p in (ROOT / "sources").glob("SRC-*.md")}


def walk(obj, path: Path):
    if isinstance(obj, dict):
        if isinstance(obj.get("id"), str) and ID_RE.match(obj["id"]):
            ident = obj["id"]
            if ident in all_ids:
                errors.append(f"duplicate id {ident}: {all_ids[ident]} and {path}")
            else:
                all_ids[ident] = path
            records.append((path, obj))
        for value in obj.values():
            walk(value, path)
    elif isinstance(obj, list):
        for value in obj:
            walk(value, path)


for directory in STRUCTURED:
    if not directory.exists():
        continue
    for path in sorted(directory.glob("*.yaml")):
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"YAML parse error {path.relative_to(ROOT)}: {exc}")
            continue
        walk(data, path.relative_to(ROOT))


def check_ref(value: str, where: str):
    if value.startswith("KO."):
        return  # external Narrative Knowledge Base
    if SOURCE_RE.match(value):
        if value not in source_ids:
            errors.append(f"missing source record {value} referenced by {where}")
        return
    if ID_RE.match(value) and value not in all_ids:
        errors.append(f"unresolved id {value} referenced by {where}")


REF_KEYS = {
    "subject", "object", "parent", "participants", "entities", "locations", "pov",
    "supported_by", "supports_story_claims", "decision_ids", "narrative_instances",
    "affects", "arcs_advanced", "motifs", "claims_active", "claims_introduced",
    "applies_to", "contradicts", "qualifies"
}


def validate_node(node, where: str):
    if isinstance(node, dict):
        if "evidence_status" in node and node["evidence_status"] not in EVIDENCE:
            errors.append(f"invalid evidence_status {node['evidence_status']} in {where}")
        if "canon_status" in node and node["canon_status"] not in CANON:
            errors.append(f"invalid canon_status {node['canon_status']} in {where}")
        st = node.get("story_time") or node.get("time")
        if isinstance(st, dict):
            lo, hi = st.get("earliest"), st.get("latest_exclusive")
            if lo and hi and str(lo) >= str(hi):
                errors.append(f"invalid half-open time range {lo}...{hi} in {where}")
            precision = st.get("precision")
            if precision == "month" and lo and not str(lo).endswith("-01"):
                errors.append(f"month precision must start on first day in {where}: {lo}")
            if precision == "year" and lo and not str(lo).endswith("-01-01"):
                errors.append(f"year precision must start on Jan 1 in {where}: {lo}")
        for key, value in node.items():
            if key in REF_KEYS:
                values = value if isinstance(value, list) else [value]
                for item in values:
                    if isinstance(item, str):
                        check_ref(item, where)
            if key == "source_ids":
                values = value if isinstance(value, list) else [value]
                for item in values:
                    if isinstance(item, str):
                        check_ref(item, where)
            validate_node(value, where)
    elif isinstance(node, list):
        for item in node:
            validate_node(item, where)


for path, record in records:
    validate_node(record, f"{path}:{record.get('id', '?')}")

# Active deterministic claims must not depend on deprecated/rejected story claims.
status_by_id = {rec.get("id"): rec.get("canon_status") for _, rec in records if rec.get("canon_status")}
for path, record in records:
    if record.get("deterministic", {}).get("lemma_candidate"):
        if record.get("canon_status") in {"DEPRECATED", "REJECTED"}:
            errors.append(f"inactive claim marked lemma_candidate: {record['id']}")

if errors:
    print("CLAES CANON VALIDATION: FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("CLAES CANON VALIDATION: PASSED")
print(f"Structured IDs: {len(all_ids)}")
print(f"Source records: {len(source_ids)}")
