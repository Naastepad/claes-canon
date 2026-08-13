#!/usr/bin/env python3
"""Repository-level continuity compiler for Claes.

Validates the McKee/NOS-inspired structured storybible layer. Lemma syntax is
validated separately. The compiler is conservative: it checks declared state,
references, vocabularies, temporal windows and migration-review coverage, but
never invents missing facts or silently resolves canon conflicts.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
STRUCTURED = [
    ROOT / "claims",
    ROOT / "entities",
    ROOT / "objects",
    ROOT / "narrative",
    ROOT / "canon",
    ROOT / "mapping",
]

EVIDENCE = {"VERIFIED", "SUPPORTED", "PLAUSIBLE", "DISPUTED", "UNKNOWN"}
CANON = {"PROPOSED", "CANON", "OPEN", "DEPRECATED", "REJECTED"}
MIGRATION_ORIGIN = {"MIGRATED", "DERIVED", "NEW"}
MIGRATION_REVIEW_STATE = {"MIGRATION_CHECK", "HUMAN_REVIEW", "HUMAN_DECISION", "CONFLICT"}
ID_RE = re.compile(r"^(SC|STC|DEC|ENT|OBJ|NI|ARC|MOTIF|REL|OPEN|GRD|SB|THEME|VALUE|WORLD|CODE)\.[A-Z0-9_.-]+$")
SOURCE_RE = re.compile(r"^SRC-[A-Z0-9_.-]+$")

errors: list[str] = []
records: list[tuple[Path, dict]] = []
all_ids: dict[str, Path] = {}
source_ids = {p.stem for p in (ROOT / "sources").glob("SRC-*.md")}


def walk(obj, path: Path):
    if isinstance(obj, dict):
        ident = obj.get("id")
        if isinstance(ident, str) and ID_RE.match(ident):
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
    "subject", "subjects", "object", "objects", "parent", "participants",
    "entities", "locations", "pov", "supported_by", "source_refs",
    "supports_story_claims", "decision_ids", "narrative_instances",
    "story_claims", "affects", "arcs_advanced", "motifs", "claims_active",
    "claims_introduced", "applies_to", "contradicts", "qualifies",
    "knowledge_object_targets", "ko_targets", "story_instance", "motif",
}


def validate_node(node, where: str):
    if isinstance(node, dict):
        if "evidence_status" in node and node["evidence_status"] not in EVIDENCE:
            errors.append(f"invalid evidence_status {node['evidence_status']} in {where}")
        if "canon_status" in node and node["canon_status"] not in CANON:
            errors.append(f"invalid canon_status {node['canon_status']} in {where}")
        st = node.get("story_time") or node.get("time") or node.get("window")
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

# Deterministic Lemma candidates must be active canon.
for path, record in records:
    if record.get("deterministic", {}).get("lemma_candidate"):
        if record.get("canon_status") != "CANON":
            errors.append(f"non-CANON claim marked lemma_candidate: {record['id']}")

# The section ledger must cover the source continuously at top-level boundaries.
ledger = ROOT / "mapping" / "CONVERSION_LEDGER.yaml"
if ledger.exists():
    data = yaml.safe_load(ledger.read_text(encoding="utf-8")) or {}
    sections = data.get("sections", [])
    if not sections:
        errors.append("conversion ledger contains no sections")
    else:
        expected = 15  # first top-level section begins after the revision header
        for section in sections:
            lines = section.get("source_lines", {})
            start, end = lines.get("start"), lines.get("end")
            if start != expected:
                errors.append(f"conversion ledger gap/overlap before {section.get('id')}: expected {expected}, got {start}")
            if not isinstance(end, int) or end < start:
                errors.append(f"invalid source line interval in {section.get('id')}")
                continue
            expected = end + 1
        if expected != 3804:
            errors.append(f"conversion ledger does not end at source line 3803; next expected is {expected}")

# Migration-review gate: every current Story Claim must be classified exactly once.
review_path = ROOT / "review" / "MIGRATION_REVIEW.yaml"
story_claim_ids = {ident for ident in all_ids if ident.startswith("STC.")}
if not review_path.exists():
    errors.append("missing review/MIGRATION_REVIEW.yaml")
else:
    try:
        review_data = yaml.safe_load(review_path.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        errors.append(f"YAML parse error review/MIGRATION_REVIEW.yaml: {exc}")
        review_data = {}

    review_records = review_data.get("records", [])
    seen_review: set[str] = set()
    origin_counts = {key: 0 for key in MIGRATION_ORIGIN}
    state_counts = {key: 0 for key in MIGRATION_REVIEW_STATE}

    for item in review_records:
        claim_id = item.get("claim_id")
        origin = item.get("origin")
        review_state = item.get("review_state")
        if not isinstance(claim_id, str):
            errors.append("migration review record missing claim_id")
            continue
        if claim_id in seen_review:
            errors.append(f"duplicate migration review record for {claim_id}")
        seen_review.add(claim_id)
        if claim_id not in story_claim_ids:
            errors.append(f"migration review references non-existent Story Claim {claim_id}")
        if origin not in MIGRATION_ORIGIN:
            errors.append(f"invalid migration origin {origin} for {claim_id}")
        else:
            origin_counts[origin] += 1
        if review_state not in MIGRATION_REVIEW_STATE:
            errors.append(f"invalid migration review_state {review_state} for {claim_id}")
        else:
            state_counts[review_state] += 1
        if origin == "NEW" and review_state not in {"HUMAN_DECISION", "CONFLICT"}:
            errors.append(f"NEW claim must require HUMAN_DECISION or CONFLICT: {claim_id}")
        if review_state == "CONFLICT" and not item.get("conflict"):
            errors.append(f"CONFLICT record must explain conflict: {claim_id}")

    missing_review = sorted(story_claim_ids - seen_review)
    extra_review = sorted(seen_review - story_claim_ids)
    for claim_id in missing_review:
        errors.append(f"Story Claim lacks migration review classification: {claim_id}")
    for claim_id in extra_review:
        errors.append(f"migration review has orphan classification: {claim_id}")

    declared = review_data.get("summary", {})
    if declared.get("story_claims_total") != len(story_claim_ids):
        errors.append(
            f"migration review story_claims_total is {declared.get('story_claims_total')}, expected {len(story_claim_ids)}"
        )
    for key, actual in origin_counts.items():
        expected_count = (declared.get("by_origin") or {}).get(key)
        if expected_count != actual:
            errors.append(f"migration review origin count {key} is {expected_count}, actual {actual}")
    for key, actual in state_counts.items():
        expected_count = (declared.get("by_review_state") or {}).get(key)
        if expected_count != actual:
            errors.append(f"migration review state count {key} is {expected_count}, actual {actual}")

    # Conflicts are deliberate merge blockers, not warnings.
    unresolved_conflicts = [item.get("claim_id") for item in review_records if item.get("review_state") == "CONFLICT"]
    for claim_id in unresolved_conflicts:
        errors.append(f"UNRESOLVED CANON CONFLICT blocks merge: {claim_id}")

if errors:
    print("CLAES CANON VALIDATION: FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("CLAES CANON VALIDATION: PASSED")
print(f"Structured IDs: {len(all_ids)}")
print(f"Source records: {len(source_ids)}")
print(f"Migration-reviewed Story Claims: {len(story_claim_ids)}")
