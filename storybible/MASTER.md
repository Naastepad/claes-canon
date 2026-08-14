# Claes Storybible — MASTER / operating authority

**Logical master ID:** `SB.CLAES.MASTER`

This repository contains the **structured operating projection** of Revision 11 plus explicit later human canon decisions. The original long-form edition remains the lossless prose source from which the projection was transmuted; later decisions override conflicting or still-open source wording.

## Source edition

`Claes_Storybible_MASTER_COMPLEET_2026-08-10_REVISIE11_MACROSTRUCTUUR_PROJECTIO(1).md`

- source lines: `3803`
- parsed headings: `296`
- SHA-256: `e38430f0165e7c0779a8ae6bba6a208773c677682f55295a940e91fdb2ed9edd`
- source role: `LOSSLESS_PROSE_AUTHORITY`
- structured role: `IN_REPOSITORY_OPERATING_PROJECTION`

The raw 3803-line prose source is not silently replaced by a summary. Every top-level section is registered in `mapping/CONVERSION_LEDGER.yaml` with source line boundaries and a section hash. Material not yet atomized remains active source material rather than disappearing.

## Structured operating master

The storybible is distributed by responsibility:

- `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` — current synchronized human-readable operating synthesis, including decisions through 14 August 2026;
- `mapping/CONVERSION_LEDGER.yaml` — loss-prevention map from all 31 top-level source sections into the structured model;
- `mapping/CONVERSION_REPORT.yaml` — conversion scope and next normalization passes;
- `claims/SOURCE_CLAIMS.yaml`, `claims/SOURCE_CLAIMS_GOES_LIVING_CITY.yaml`, `claims/SOURCE_CLAIMS_GOES_2026-08-14.yaml` — atomic historical/research claims;
- `claims/STORY_CLAIMS.yaml`, `claims/STORY_CLAIMS_2026-08-14.yaml`, `claims/STORY_CLAIMS_FAMILY_1554.yaml` — atomic truths of the novel;
- `canon/DECISIONS.yaml`, `canon/DECISIONS_2026-08-13.md`, `canon/DECISIONS_2026-08-14.md` — explicit human canon decisions;
- `entities/ENTITIES.yaml`, `entities/FAMILY_1554.yaml` plus setting-specific entity registries — stable persons, family units, locations and properties;
- `objects/OBJECTS.yaml` — books, carriers, keys and other continuity-sensitive objects;
- `narrative/instances.yaml` — concrete chapters, scenes, sequences and events;
- `narrative/arcs.yaml` — character, relationship and macro-transformation arcs;
- `narrative/relationships.yaml` — explicit relationship dynamics, including Claes–Cornelis, Claes–brother and Cornelis–grandfather;
- `narrative/motifs.yaml` — recurring sensory/symbolic structures;
- `narrative/world_goes_living_city.yaml` — year-sensitive Goes scene/blocking framework;
- `narrative/CRAFT_GUARDRAILS.yaml` — writing and continuity constraints;
- `canon/OPEN_DECISIONS.yaml` — unresolved matters and audit-preserved resolved open records;
- `lemma/` — only the deterministic subset that benefits from executable consistency rules.

## Explicit Goes and family normalization — 14 August 2026

The following points are closed by human decision:

1. **Cornelis' household residence:** the historically documented house bought by Claes Jacobsz. Nissepat on 20 March 1542 in the older Nieuwstraat is the fictional family home of Cornelis, his wife and children during Claes' Goes childhood. Historical purchase and fictional occupancy remain distinct.
2. **Pre-1594 Nieuwstraat:** the older deed-name is treated as Nieuwstraat/Oude Nieuwstraat in or by the Armenhoek, distinct from the planmatige/current Nieuwstraat associated with the 1594 expansion. The exact old street axis remains unknown.
3. **Cornelis' rederijker meeting environment:** Cornelis-era meetings use the Zusterhuis/former Zwarte-Zusters complex at the Singelstraat. The Nardusbloem moved to the Sint-Sebastiaanshof only in 1626, so that later location is not back-projected.
4. **Pre-fire family:** Claes has a younger brother about eighteen months younger; their mother is about six months pregnant on 18 May 1554.
5. **Family outcome of the 1554 fire:** the family house is destroyed/uninhabitable in novel canon; Claes and Cornelis survive away from the house; mother, younger brother and unborn child die. This is fiction grounded in documented burned houses in the old Nieuwstraat/Armenhoek environment, not a historical victim/property claim.
6. **Grandfather link:** historical Claes Jacobsz. Nissepat is fictionally Cornelis' father and Claes' paternal grandfather. His historical purchase is real; the genealogy, continued story ownership through 1554 and support role are fictional. He loses the 1542 house as a story asset in the fire.
7. **Post-fire father–son separation:** Cornelis stays in Goes to rebuild livelihood, business and shelter and to keep financing Claes' education, partly helped by his father. Claes goes to Reimerswaal because the intended Zierikzee route has become financially unattainable. The separation is an additional loss layered onto the destruction of the household.

The exact named Goese chamber to which fictional Cornelis belongs remains separately open; meeting location and chamber identity are not conflated. Names for Claes' mother and younger brother also remain open; the unborn child's sex remains unknown.

## McKee/NOS interface

The Claes repository does **not** contain universal McKee/Truby/etc. theory as canon. Concrete Narrative Instances may point to external `KO.*` Knowledge Objects for analysis. Thus:

`Narrative Knowledge Base (KO.*) + Claes Narrative Instances (NI.*) -> diagnostics`

while:

`Source Claims (SC.*) -> Story Claims (STC.*) -> Lemma -> deterministic consistency`

## Precedence

1. An explicit current human canon decision (`DEC.*`) governs structured canon state.
2. Active `STC.*` records are the machine-readable story truth.
3. The synchronized human-readable operating master expresses the active model coherently.
4. The lossless Revision 11 prose source governs meaning not yet atomized and not superseded by later decisions.
5. Lemma may reject an impossible combination, but Lemma never invents story truth.
6. AI proposals never become canon merely by being plausible.

If structured data and the source prose appear to conflict, apply explicit later decisions first; otherwise create a proposal and resolve it explicitly. Never silently overwrite either layer.

## Conversion state

Revision 11 has completed a **first full semantic conversion pass**: all 31 top-level sections are accounted for, and the core chronology, character arc, macrostructure, code architecture, objects, motifs, open decisions and key Narrative Instances have been normalized. The Goes living-city, church, old-Nieuwstraat, rederijker and 1554 family-rupture layers have since received additional structured normalization.

This does **not** mean every paragraph has already become its own atomic record. The conversion ledger makes that remaining normalization measurable and loss-safe.
