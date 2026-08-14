#!/usr/bin/env python3
"""Repository-level continuity compiler for Claes.

Validates the McKee/NOS-inspired structured storybible layer. Lemma syntax is
validated separately. This compiler checks declared state, references,
vocabularies, temporal windows, migration-review coverage, multi-agent
integrity files, and a small set of explicit cross-layer author decisions.
It never invents missing facts or silently resolves canon conflicts.
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
record_by_id: dict[str, dict] = {}
source_ids = {p.stem for p in (ROOT / "sources").glob("SRC-*.md")}


def walk(obj, path: Path):
    if isinstance(obj, dict):
        ident = obj.get("id")
        if isinstance(ident, str) and ID_RE.match(ident):
            if ident in all_ids:
                errors.append(f"duplicate id {ident}: {all_ids[ident]} and {path}")
            else:
                all_ids[ident] = path
                record_by_id[ident] = obj
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
    "entities", "locations", "location", "pov", "supported_by", "source_refs",
    "supports_story_claims", "decision_ids", "decision_id", "decision",
    "narrative_instances", "story_claims", "affects", "arcs_advanced",
    "motifs", "claims_active", "claims_introduced", "applies_to",
    "contradicts", "qualifies", "knowledge_object_targets", "ko_targets",
    "story_instance", "motif", "relationship", "destination", "origin",
    "arc", "location_anchor", "canonical_residence",
    "rhetorician_meeting_environment", "rhetorician_decision",
    "chamber_identity", "resolved_by", "organization",
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

# The section ledger must cover the Revision 11 source continuously at top-level boundaries.
ledger = ROOT / "mapping" / "CONVERSION_LEDGER.yaml"
if ledger.exists():
    data = yaml.safe_load(ledger.read_text(encoding="utf-8")) or {}
    sections = data.get("sections", [])
    if not sections:
        errors.append("conversion ledger contains no sections")
    else:
        expected = 15
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
        if review_state == "CONFLICT" and not (item.get("conflict") or item.get("resolution")):
            errors.append(f"CONFLICT record must explain conflict: {claim_id}")

    for claim_id in sorted(story_claim_ids - seen_review):
        errors.append(f"Story Claim lacks migration review classification: {claim_id}")
    for claim_id in sorted(seen_review - story_claim_ids):
        errors.append(f"migration review has orphan classification: {claim_id}")

    declared = review_data.get("summary", {})
    if declared.get("story_claims_total") != len(story_claim_ids):
        errors.append(f"migration review story_claims_total is {declared.get('story_claims_total')}, expected {len(story_claim_ids)}")
    for key, actual in origin_counts.items():
        expected_count = (declared.get("by_origin") or {}).get(key)
        if expected_count != actual:
            errors.append(f"migration review origin count {key} is {expected_count}, actual {actual}")
    for key, actual in state_counts.items():
        expected_count = (declared.get("by_review_state") or {}).get(key)
        if expected_count != actual:
            errors.append(f"migration review state count {key} is {expected_count}, actual {actual}")

    for item in review_records:
        if item.get("review_state") == "CONFLICT":
            errors.append(f"UNRESOLVED CANON CONFLICT blocks merge: {item.get('claim_id')}")

# Multi-agent integrity files must exist.
required_files = [
    ROOT / "REPOSITORY_INTEGRITY.md",
    ROOT / "AGENTS.md",
    ROOT / "AUTHORING_POLICY.md",
    ROOT / "AI_ONBOARDING.md",
    ROOT / "review" / "SYNC_STATUS.md",
    ROOT / "storybible" / "LEMMA_MCKEE_MASTER_2026-08-13.md",
    ROOT / "canon" / "DECISIONS_2026-08-13.md",
    ROOT / "canon" / "DECISIONS_2026-08-14.md",
    ROOT / "canon" / "DECISIONS.yaml",
]
for path in required_files:
    if not path.exists():
        errors.append(f"missing required integrity/authority file: {path.relative_to(ROOT)}")

# Explicit 13-Aug-2026 author-decision synchronization checks.
birth_claim = record_by_id.get("STC.CLAES.BIRTH.001") or {}
if (birth_claim.get("story_time") or {}).get("date") != "1542-12-08":
    errors.append("STC.CLAES.BIRTH.001 must be synchronized to 1542-12-08")

claes_entity = record_by_id.get("ENT.PERSON.CLAES") or {}
if (claes_entity.get("birth") or {}).get("date") != "1542-12-08":
    errors.append("ENT.PERSON.CLAES birth must be synchronized to 1542-12-08")

life_arc = record_by_id.get("ARC.CLAES.LIFE") or {}
life_phases = life_arc.get("phases") or []
if not life_phases or ((life_phases[0].get("story_time") or {}).get("earliest") != "1542-12-08"):
    errors.append("ARC.CLAES.LIFE must begin at 1542-12-08")

macro_arc = record_by_id.get("ARC.CLAES.MACRO_TRANSMUTATION") or {}
macro_phases = macro_arc.get("phases") or []
if not macro_phases or ((macro_phases[0].get("story_time") or {}).get("earliest") != "1542-12-08"):
    errors.append("ARC.CLAES.MACRO_TRANSMUTATION Drager phase must begin at 1542-12-08")

for required_id in [
    "DEC.CLAES.BIRTH.2026-08-13",
    "DEC.CLAES.SINNE.2026-08-13",
    "DEC.CLAES.PARADOX.2026-08-13",
    "DEC.CLAES.NEED.2026-08-13",
    "DEC.CLAES.SPIRITUAL_JOURNEY.2026-08-13",
    "THEME.CLAES.SPIRITUAL_JOURNEY",
    "VALUE.CLAES.SINNE",
    "ARC.CLAES.SINNE_RECOVERY",
    "MOTIF.SINNE.RECOVERY",
    "REL.CLAES.BELOVED.RECOVERY",
]:
    if required_id not in all_ids:
        errors.append(f"missing synchronized decision/narrative record: {required_id}")

# Explicit 14-Aug-2026 Goes decisions must be synchronized across decision, claim,
# entity, world and human-readable master layers.
for required_id in [
    "DEC.CORNELIS.RESIDENCE.GOES.2026-08-14",
    "DEC.GOES.NIEUWSTRAAT.IDENTITY.2026-08-14",
    "DEC.GOES.REDERIJKERS.MEETINGPLACE.2026-08-14",
    "STC.CORNELIS.HOUSEHOLD_GOES.1542.001",
    "STC.GOES.NIEUWSTRAAT.PRE1594.001",
    "STC.CORNELIS.REDERIJKERS.ZUSTERHUIS.001",
    "ENT.LOC.GOES.ZUSTERHUIS",
    "ENT.LOC.GOES.NIEUWSTRAAT_PRE1594",
    "ENT.PROP.GOES.NISSEPAT.NIEUWSTRAAT_1542",
    "ENT.ORG.GOES.NARDUSBLOEM",
]:
    if required_id not in all_ids:
        errors.append(f"missing synchronized 14-Aug-2026 Goes record: {required_id}")

cornelis_entity = record_by_id.get("ENT.PERSON.CORNELIS") or {}
if (cornelis_entity.get("household_residence") or {}).get("location") != "ENT.PROP.GOES.NISSEPAT.NIEUWSTRAAT_1542":
    errors.append("ENT.PERSON.CORNELIS household residence must be the 1542 older-Nieuwstraat house")
if (cornelis_entity.get("rhetorician_meeting_environment") or {}).get("location") != "ENT.LOC.GOES.ZUSTERHUIS":
    errors.append("ENT.PERSON.CORNELIS rhetorician meeting environment must be the Zusterhuis")

if (claes_entity.get("childhood_residence") or {}).get("location") != "ENT.PROP.GOES.NISSEPAT.NIEUWSTRAAT_1542":
    errors.append("ENT.PERSON.CLAES childhood residence must be the 1542 older-Nieuwstraat house")

old_nieuwstraat = record_by_id.get("ENT.LOC.GOES.NIEUWSTRAAT_PRE1594") or {}
if old_nieuwstraat.get("canon_status") != "CANON":
    errors.append("pre-1594 Nieuwstraat entity must be active CANON at zone level")
if (old_nieuwstraat.get("reconstruction") or {}).get("exact_street_axis") != "UNKNOWN":
    errors.append("pre-1594 Nieuwstraat exact street axis must remain UNKNOWN")

for open_id, decision_id in [
    ("OPEN.CORNELIS.RESIDENCE.GOES.1542.001", "DEC.CORNELIS.RESIDENCE.GOES.2026-08-14"),
    ("OPEN.GOES.NIEUWSTRAAT.PRE1594.001", "DEC.GOES.NIEUWSTRAAT.IDENTITY.2026-08-14"),
    ("OPEN.GOES.REDERIJKERS.MEETINGPLACE.001", "DEC.GOES.REDERIJKERS.MEETINGPLACE.2026-08-14"),
]:
    record = record_by_id.get(open_id) or {}
    if record.get("status") != "RESOLVED" or record.get("resolved_by") != decision_id:
        errors.append(f"{open_id} must be RESOLVED by {decision_id}")

nardus = record_by_id.get("ENT.ORG.GOES.NARDUSBLOEM") or {}
location_history = nardus.get("location_history") or []
if not location_history or location_history[0].get("location") != "ENT.LOC.GOES.ZUSTERHUIS" or location_history[0].get("through") != 1626:
    errors.append("Nardusbloem location history must retain Zusterhuis through 1626")
if len(location_history) < 2 or location_history[1].get("location") != "ENT.LOC.GOES.SEBASTIAANSHOF" or location_history[1].get("from") != 1626:
    errors.append("Nardusbloem location history must place Sint-Sebastiaanshof from 1626, not in Cornelis' period")

master_path = ROOT / "storybible" / "LEMMA_MCKEE_MASTER_2026-08-13.md"
if master_path.exists():
    master_text = master_path.read_text(encoding="utf-8")
    if "8 December 1542" not in master_text:
        errors.append("current operating master must state 8 December 1542")
    if "8 December 1545" in master_text:
        errors.append("current operating master must not retain 8 December 1545")
    for phrase in ["road toward Enkhuizen", "matter toward spirituality", "knowledge-as-control"]:
        if phrase not in master_text:
            errors.append(f"current operating master missing synchronized character architecture phrase: {phrase}")
    for phrase in ["20 March 1542", "Armenhoek", "Zusterhuis", "only then moved to the building/hof of the handbow guild Sint-Sebastiaan"]:
        if phrase not in master_text:
            errors.append(f"current operating master missing synchronized Goes phrase: {phrase}")

sync_path = ROOT / "review" / "SYNC_STATUS.md"
if sync_path.exists() and "SYNC_COMPLETE" not in sync_path.read_text(encoding="utf-8"):
    errors.append("review/SYNC_STATUS.md must be SYNC_COMPLETE before validation can pass")

if errors:
    print("CLAES CANON VALIDATION: FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("CLAES CANON VALIDATION: PASSED")
print(f"Structured IDs: {len(all_ids)}")
print(f"Source records: {len(source_ids)}")
print(f"Migration-reviewed Story Claims: {len(story_claim_ids)}")
print("Author decisions synchronized through: 2026-08-14")
