# Claes Storybible — MASTER / operating authority

**Logical master ID:** `SB.CLAES.MASTER`

This repository now contains the **structured operating projection** of Revision 11. The original long-form edition remains the lossless prose source from which this projection was transmuted.

## Source edition

`Claes_Storybible_MASTER_COMPLEET_2026-08-10_REVISIE11_MACROSTRUCTUUR_PROJECTIO(1).md`

- source lines: `3803`
- parsed headings: `296`
- SHA-256: `e38430f0165e7c0779a8ae6bba6a208773c677682f55295a940e91fdb2ed9edd`
- source role: `LOSSLESS_PROSE_AUTHORITY`
- structured role: `IN_REPOSITORY_OPERATING_PROJECTION`

The raw 3803-line prose source is not silently replaced by a summary. Every top-level section is registered in `mapping/CONVERSION_LEDGER.yaml` with source line boundaries and a section hash. Material not yet atomized remains active source material rather than disappearing.

## Post-Revision-11 canon override — Claes chronology

`DEC.CLAES.BIRTH_EDUCATION.001` is an explicit current author decision and therefore supersedes conflicting age references in the Revision 11 prose source.

Current canon:

- Claes is born in Goes on **8 December 1542**, intentionally sharing the date recorded for completion of the primitive 1542 *Brevísima* text.
- Before May 1554 he receives elementary schooling in Goes; the operating canon does **not** require an uninterrupted full official Goes Latin school in these years.
- Cornelis intends Zierikzee as the next Latin-school destination.
- After the Goes fire of **18 May 1554**, Reimerswaal replaces Zierikzee as the actual route; Claes leaves later in 1554 as a cost pupil and remains in the Reimerswaal educational environment until the Landjuweel journey of August 1561.
- The Reimerswaal span develops into advanced/older-pupil formation; it must not be read as seven years of beginner curriculum.
- Derived age anchors: Claes is **11** at the Goes fire, still **11 and nearly 12** when he transfers to Reimerswaal later in 1554, **18** at the August 1561 Landjuweel, **20** at the February 1563 Dee encounter and **21** during the intensive 1564 formation.

When Revision 11 wording conflicts with these points, use the current `DEC.*`, `STC.*`, `ENT.*`, `ARC.*` and transformed master records.

## Structured operating master

The storybible is now distributed by responsibility:

- `mapping/CONVERSION_LEDGER.yaml` — loss-prevention map from all 31 top-level source sections into the structured model;
- `mapping/CONVERSION_REPORT.yaml` — conversion scope and next normalization passes;
- `claims/SOURCE_CLAIMS.yaml` — atomic claims about historical/research reality;
- `claims/STORY_CLAIMS.yaml` — atomic truths of the novel;
- `claims/DECISIONS.yaml` — human canon/architecture decisions;
- `entities/ENTITIES.yaml` — stable persons and locations;
- `objects/OBJECTS.yaml` — books, carriers, keys and other continuity-sensitive objects;
- `narrative/instances.yaml` — concrete chapters, scenes, sequences and events;
- `narrative/arcs.yaml` — character, relationship and macro-transformation arcs;
- `narrative/motifs.yaml` — recurring sensory/symbolic structures;
- `narrative/CRAFT_GUARDRAILS.yaml` — writing and continuity constraints;
- `canon/OPEN_DECISIONS.yaml` — genuinely unresolved author decisions;
- `lemma/` — only the deterministic subset that benefits from executable consistency rules.

## McKee/NOS interface

The Claes repository does **not** contain universal McKee/Truby/etc. theory as canon. Concrete Narrative Instances may point to external `KO.*` Knowledge Objects for analysis. Thus:

`Narrative Knowledge Base (KO.*) + Claes Narrative Instances (NI.*) -> diagnostics`

while:

`Source Claims (SC.*) -> Story Claims (STC.*) -> Lemma -> deterministic consistency`

## Precedence

1. An explicit current human canon decision (`DEC.*`) governs structured canon state.
2. Active `STC.*` records are the machine-readable story truth.
3. The lossless Revision 11 prose source governs meaning not yet atomized.
4. Lemma may reject an impossible combination, but Lemma never invents story truth.
5. AI proposals never become canon merely by being plausible.

If structured data and the source prose appear to conflict, create a proposal and resolve it explicitly. Never silently overwrite either layer.

## Conversion state

Revision 11 has completed a **first full semantic conversion pass**: all 31 top-level sections are accounted for, and the core chronology, character arc, macrostructure, code architecture, objects, motifs, open decisions and key Narrative Instances have been normalized.

This does **not** mean every paragraph has already become its own atomic record. The conversion ledger makes that remaining normalization measurable and loss-safe.
