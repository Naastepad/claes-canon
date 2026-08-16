#!/usr/bin/env python3
"""Guard the human-readable/authoring projection against known superseded canon drift.

The structural compiler validates IDs and references. This lightweight companion catches
semantic regressions in a small set of files writers are most likely to read directly.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

checks = {
    "narrative/CRAFT_GUARDRAILS.yaml": {
        "required": [
            "GRD.CLAES.AGE",
            "GRD.REIMERSWAAL.EDUCATION",
            "GRD.MEMORIAAL.DIRECT_REVEAL",
            "GRD.NO_DECRYPTION_BACKSLIDE",
        ],
        "forbidden": [
            "Dodoens yields values",
            "Primus Index identifies",
            "full reconstruction takes weeks",
        ],
    },
    "narrative/world_modules.yaml": {
        "required": [
            "elementary schooling",
            "advanced older-pupil formation",
            "chemical/material, not a cipher-key architecture",
        ],
        "forbidden": [
            "cipher knowledge may belong",
            "source, key and destination",
        ],
    },
    "narrative/world_goes_living_city.yaml": {
        "required": [
            "ENT.ORG.GOES.NARDUSBLOEM",
            "DEC.CORNELIS.REDERIJKER.NARDUS_CASTANIE_ORIGIN.2026-08-16",
            "SC.HIST.GOES.FIRE_1554.CASUALTIES.001",
            "SC.HIST.GOES.SALT.NORTH_HARBOUR_1554.001",
        ],
        "forbidden": [
            "OPEN.CORNELIS.REDERIJKERS.CHAMBER.001",
            "mother_fate: OPEN",
        ],
    },
    "narrative/instances.yaml": {
        "required": [
            "intentional exact-date resonance with Claes' canonical birth on 8 December 1542",
            "STC.CLAES.ZIERIKZEE.PLAN.001",
            "STC.CORNELIS.FIRST_ARREST_BAIL.1567.001",
            "STC.CORNELIS.DEATH.ANTWERP.1569.001",
            "19 November 1569: fictional public execution in Antwerp",
            "Antwerpse druk / Projectio van het Woord",
        ],
        "forbidden": [
            "not shared birth-year resonance",
            "label: Arrestatie en dood Cornelis\n  canon_status: CANON\n  details_status: OPEN",
        ],
    },
    "storybible/LEMMA_MCKEE_MASTER.md": {
        "required": [
            "8 December 1542",
            "not decryption",
            "Mayken",
            "19 November 1569",
        ],
        "forbidden": [
            "8 December 1545",
        ],
    },
    "narrative/religious_space_sensory_church.yaml": {
        "required": [
            "WORLD.RELIGIOUS_SPACE.SENSORY_CHURCH",
            "local_verification_required: true",
            "Never checklist all five senses",
            "church_as_memory_palace",
        ],
        "forbidden": [],
    },
    "storybible/modules/HISTORICAL_SUBSTRATE_1540_1605.md": {
        "required": [
            "source → HIST.EVENT",
            "information status",
            "layered identity",
            "Reimerswaal's interaction of war, flood/erosion, demography, trade and church life",
        ],
        "forbidden": [],
    },
    "storybible/modules/WORLD_GOES_CHURCH_LOCAL.md": {
        "required": [
            "12 March 1442",
            "31 May 1471",
            "Niehoff replacement organ from 1550",
        ],
        "forbidden": [],
    },
    "history/LOW_COUNTRIES_TRANSFORMATION_1540_1605.md": {
        "required": [
            "Low Countries transformation, 1540–1605",
            "1572, Goes",
            "17 August 1585",
            "20 March 1602",
        ],
        "forbidden": [],
    },
    "claims/SOURCE_CLAIMS_HISTORICAL_SUBSTRATE_RECOVERY_2026-08-16.yaml": {
        "required": [
            "SC.HIST.CATHOLIC_BIBLE.LATIN_VULGATE.1550.001",
            "SC.HIST.RELIGIOUS_SPACE.SENSORY_SOCIAL_FIELD.001",
            "SC.HIST.REDERIJKERS.PUBLIC_COMMUNICATION_NETWORK.001",
            "SC.HIST.REVOLT.INFORMATION_ECOLOGY.1560_1585.001",
        ],
        "forbidden": [],
    },
}

errors = []
for rel, rules in checks.items():
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing active projection file: {rel}")
        continue
    text = path.read_text(encoding="utf-8")
    for marker in rules["required"]:
        if marker not in text:
            errors.append(f"{rel} missing required current-canon marker: {marker}")
    for marker in rules["forbidden"]:
        if marker in text:
            errors.append(f"{rel} retains superseded marker: {marker}")

if errors:
    print("CLAES ACTIVE PROJECTION VALIDATION: FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("CLAES ACTIVE PROJECTION VALIDATION: PASSED")
