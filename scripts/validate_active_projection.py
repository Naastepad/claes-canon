#!/usr/bin/env python3
"""Guard the human-readable/authoring projection against known superseded canon drift.

The structural compiler validates IDs and references. This companion catches semantic
regressions in files writers are most likely to read directly, including the recovered
historical substrate and chapter-ready Round-B practice domains.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

checks = {
    "narrative/CRAFT_GUARDRAILS.yaml": {
        "required": ["GRD.CLAES.AGE", "GRD.REIMERSWAAL.EDUCATION", "GRD.MEMORIAAL.DIRECT_REVEAL", "GRD.NO_DECRYPTION_BACKSLIDE"],
        "forbidden": ["Dodoens yields values", "Primus Index identifies", "full reconstruction takes weeks"],
    },
    "narrative/world_modules.yaml": {
        "required": ["elementary schooling", "advanced older-pupil formation", "chemical/material, not a cipher-key architecture", "WORLD.BEER_BREWING_DISTRIBUTION", "Cornelis is a biersteker, not automatically a brewer or brewery owner", "WORLD.SCHUTTERIJ_MILITARY", "1516/1530", "1607 Wapenhandelinghe is not a 1572 Goes drill manual", "Never write Antwerp as one unchanged scene world"],
        "forbidden": ["cipher knowledge may belong", "source, key and destination"],
    },
    "narrative/world_goes_living_city.yaml": {
        "required": ["ENT.ORG.GOES.NARDUSBLOEM", "DEC.CORNELIS.REDERIJKER.NARDUS_CASTANIE_ORIGIN.2026-08-16", "SC.HIST.GOES.FIRE_1554.CASUALTIES.001", "SC.HIST.GOES.SALT.NORTH_HARBOUR_1554.001"],
        "forbidden": ["OPEN.CORNELIS.REDERIJKERS.CHAMBER.001", "mother_fate: OPEN"],
    },
    "narrative/instances.yaml": {
        "required": ["intentional exact-date resonance with Claes' canonical birth on 8 December 1542", "STC.CLAES.ZIERIKZEE.PLAN.001", "STC.CORNELIS.FIRST_ARREST_BAIL.1567.001", "STC.CORNELIS.DEATH.ANTWERP.1569.001", "19 November 1569: fictional public execution in Antwerp", "Antwerpse druk / Projectio van het Woord"],
        "forbidden": ["not shared birth-year resonance", "label: Arrestatie en dood Cornelis\n  canon_status: CANON\n  details_status: OPEN"],
    },
    "storybible/LEMMA_MCKEE_MASTER.md": {"required": ["8 December 1542", "not decryption", "Mayken", "19 November 1569"], "forbidden": ["8 December 1545"]},
    "narrative/religious_space_sensory_church.yaml": {"required": ["WORLD.RELIGIOUS_SPACE.SENSORY_CHURCH", "local_verification_required: true", "Never checklist all five senses", "church_as_memory_palace"], "forbidden": []},
    "storybible/modules/HISTORICAL_SUBSTRATE_1540_1605.md": {"required": ["source → HIST.EVENT", "information status", "layered identity", "Reimerswaal's interaction of war, flood/erosion, demography, trade and church life"], "forbidden": []},
    "storybible/modules/WORLD_GOES_CHURCH_LOCAL.md": {"required": ["12 March 1442", "31 May 1471", "Niehoff replacement organ from 1550"], "forbidden": []},
    "history/LOW_COUNTRIES_TRANSFORMATION_1540_1605.md": {"required": ["Low Countries transformation, 1540–1605", "1572, Goes", "17 August 1585", "20 March 1602"], "forbidden": []},
    "claims/SOURCE_CLAIMS_HISTORICAL_SUBSTRATE_RECOVERY_2026-08-16.yaml": {"required": ["SC.HIST.CATHOLIC_BIBLE.LATIN_VULGATE.1550.001", "SC.HIST.RELIGIOUS_SPACE.SENSORY_SOCIAL_FIELD.001", "SC.HIST.REDERIJKERS.PUBLIC_COMMUNICATION_NETWORK.001", "SC.HIST.REVOLT.INFORMATION_ECOLOGY.1560_1585.001"], "forbidden": []},
    "storybible/domains/BREAD_GRAIN_BAKING_1540_1602.md": {
        "required": ["professional urban bakery", "one dominant field + one counter-sense + one inference", "exact Celsius temperatures", "It does not canonize a specific bakery scene"],
        "forbidden": ["Use a fixed modern recipe"],
    },
    "storybible/domains/BEER_BREWING_BEERSTEKER_1540_1580.md": {
        "required": ["Cornelis is a **biersteker**", "**not** canonically the brewer", "generic medieval gruit ale", "Nissepad brewery relationship"],
        "forbidden": ["Cornelis is canonically the brewer", "Cornelis owns the Nissepad brewery"],
    },
    "storybible/domains/REIMERSWAAL_SCHOOL_1554_1561.md": {
        "required": ["living city that knows it is vulnerable", "school tradition before 1296", "story reconstruction grounded in durable school infrastructure", "No seven-year beginner curriculum"],
        "forbidden": ["Reimerswaal is an abandoned ruin in 1554", "seven years of beginner Latin"],
    },
    "storybible/domains/REDERIJKERS_LANDJUWEEL_1561.md": {
        "required": ["fourteen official competitors", "no current proof of a Goese chamber among the fourteen official competitors", "Dee is not in this 1561 story visit", "factor/prince are not current canon"],
        "forbidden": ["Cornelis is factor van de Nardusbloem", "Goes is an official competing chamber in 1561"],
    },
    "storybible/domains/ANTWERP_TIME_SLICES_1561_1585.md": {
        "required": ["1561: CITY AS THEATRE", "1563–early 1564: CITY AS BOOK / WORKSHOP", "1566: CITY AS BROKEN IMAGE", "1567–19 November 1569: CITY AS SURVEILLANCE / REPRESSION", "1576–1578: CITY AS WOUND / PRINT RELEASE", "1585: CITY AS TRANSFORMED FORMATIVE PLACE", "Never write"],
        "forbidden": ["Antwerp remains unchanged from 1561 to 1585"],
    },
    "storybible/domains/SCHUTTERIJ_MILITARY_PRACTICE_1550_1607.md": {
        "required": ["1516", "1530", "De Gheyn 1607", "De Gheyn 1607 as a 1572 manual", "schuttersgilde", "garrison/professional troops", "twelve apostles/furket/exact one-shot-per-minute"],
        "forbidden": ["De Gheyn 1607 proves Goes 1572 drill", "Edele Busse founded in 1516 as settled canon", "Edele Busse founded in 1530 as settled canon"],
    },
    "claims/SOURCE_CLAIMS_DOMAIN_REBUILD_2026-08-16.yaml": {"required": ["SC.HIST.REIMERSWAAL.SCHOOL.CONTINUITY.001", "SC.HIST.LANDJUWEEL.ANTWERP.14_CHAMBERS.1561.001", "SC.HIST.LANDJUWEEL.GOES_PARTICIPATION.1561.001", "SC.HIST.GOES.SCHUTTERIJ.FIREARM_GUILD.16C.001", "SC.HIST.DEGHEYN.WAPENHANDELINGHE.1607.001"], "forbidden": []},
    "narrative/domain_scene_packs.yaml": {"required": ["PACK.BEER.GOES_BIERSTEKER", "PACK.REIMERSWAAL.SCHOOL_1554_1561", "PACK.REDERIJKERS.ANTWERP_LANDJUWEEL_1561", "PACK.ANTWERP.1567_1569", "PACK.GOES.SCHUTTERIJ", "PACK.MILITARY.DEGHEYN_1607_COMPARATOR"], "forbidden": []},
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
            errors.append(f"{rel} retains superseded/forbidden marker: {marker}")

if errors:
    print("CLAES ACTIVE PROJECTION VALIDATION: FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("CLAES ACTIVE PROJECTION VALIDATION: PASSED")
