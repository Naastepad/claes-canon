# Synchronization status

Status: `SYNC_COMPLETE`

Release state: `MAIN_CANONICAL`

PR #5 has been merged into `main` after the author's explicit decision to fix the 1554 family rupture in the Storybible. GitHub `main` is the canonical source of truth for the integrated Goes living-city, old-Nieuwstraat fire, family, genealogy and father–son continuity work.

## Canonical authority chain
- `canon/DECISIONS_2026-08-13.md` and `canon/DECISIONS_2026-08-14.md` — human-readable decisions;
- `canon/DECISIONS.yaml` — machine-readable decisions through 14 August 2026;
- `claims/STORY_CLAIMS.yaml`, `claims/STORY_CLAIMS_2026-08-14.yaml`, `claims/STORY_CLAIMS_FAMILY_1554.yaml` — active story truths;
- `claims/SOURCE_CLAIMS_GOES_LIVING_CITY.yaml` and `claims/SOURCE_CLAIMS_GOES_2026-08-14.yaml` — normalized Goes evidence;
- `entities/ENTITIES.yaml`, `entities/FAMILY_1554.yaml`, `entities/GOES_LIVING_CITY.yaml`, `entities/GOES_GROTE_KERK.yaml` — persons, family units, properties and locations;
- `narrative/instances.yaml`, `narrative/arcs.yaml`, `narrative/relationships.yaml` — event, character and relationship continuity;
- `narrative/world_goes_living_city.yaml` and `narrative/world_goes_grote_kerk.yaml` — time-sensitive Goes scene frameworks;
- `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` and `storybible/MASTER.md` — synchronized human-readable operating authority;
- `review/MIGRATION_REVIEW.yaml` — all 41 Story Claims classified, including seven explicit NEW human decisions;
- `scripts/validate_canon.py` — cross-layer continuity validation.

## Canonical 1554 family decisions now on main
- `DEC.CLAES.FAMILY_FIRE.1554.2026-08-14`: immediately before the fire the household consists of Cornelis, Claes' mother, Claes, a younger brother approximately eighteen months younger and an unborn child; the mother is about six months pregnant. On 18 May 1554 the family house is destroyed/uninhabitable in novel canon. Claes and Cornelis survive away from the house; mother, younger brother and unborn child die.
- `DEC.CLAES.GRANDFATHER_LINK.2026-08-14`: historical Claes Jacobsz. Nissepat is fictionally Cornelis' father and Claes' paternal grandfather. His documented identity and 1542 purchase remain historical; the genealogy, continued story ownership through 1554 and support role are novel fiction. He loses the 1542 house as a story asset in the fire and helps sustain Claes' education afterward.
- `DEC.CLAES.POSTFIRE_FATHER_SON.2026-08-14`: Cornelis remains in Goes to rebuild livelihood, business and shelter and to keep paying for Claes' schooling, partly supported by his father. The intended Zierikzee route becomes financially unattainable and Claes goes to Reimerswaal. Father and son therefore survive the catastrophe but also lose daily access to one another.

## Dramaturgical guardrails
- The younger brother is a near-age companion and rival, not a decorative casualty. His pre-fire life must contain ordinary love, competition, quarrels, loyalty, play and unfinished conflict.
- The brother's greater immediacy/action orientation contrasts with Claes' prolonged observation and may resonate later without reducing him to a symbol.
- The mother's pregnancy is relational/sensory, not a mechanical reason for her death. Claes may know the unborn child through touch/movement before sight, supporting the *sinne* architecture.
- Cornelis' separation from Claes is simultaneously sacrifice/care and something the eleven-year-old can experience as abandonment.
- Cornelis' later death closes the possibility that father and son will fully recover the years lost after 1554.

## Historical/fire integrity rules
- Post-fire RAZE 1748 acts document burned houses at the Hoek van de Nieuwstraat and in the Armenhoek while other Nieuwstraat houses survive/transfer; the correct historical model is mixed/partial destruction.
- No current chain proves the specific 1542 Nissepat house burned. Its destruction is novel canon grounded in the historical damage environment.
- No historical victim list proves Claes' mother, brother or unborn sibling. They are fictional casualties.
- The pre-1594 Nieuwstraat remains distinct from the planmatige/current Nieuwstraat of the 1594 expansion; its exact 1542 axis remains unknown.
- Ownership, residence, business operation and adjacency remain separate relations.
- The 1554 urban fire and 1572 military destruction remain separate event footprints.
- The 1572 burned Voorstad brewery is not automatically the equipped Nissepad brewery documented in 1577.
- The Claes Jacobsz. → Cornelis → Claes genealogy is active novel canon but not archival genealogy.

## Remaining related open matters
- Names of Claes' mother and younger brother remain open.
- The unborn child's sex remains open/unknown.
- `OPEN.CORNELIS.REDERIJKERS.CHAMBER.001` remains open only for Cornelis' named chamber identity; the Zusterhuis meeting environment is already resolved.
- Exact Cornelis arrest/death details and the exact business link to the 1572 brewery loss remain separate open questions.

## Validation state
PR #5 head `46f741c55754d5daa8ffde02dc172a83cb23f658` passed repository continuity validation in workflow run **141** before merge. PR #5 was merged as commit `0f7f8778acc6437ad9a16bb8ffda9aa6625c375c`.

## Legacy/audit note
- `storybible/LEMMA_MCKEE_MASTER.md` remains the earlier transformed work edition; the dated operating master is authoritative while legacy wording remains unreconciled there.
- Resolved `OPEN.*` records are retained for audit history rather than deleted.
- Historical source claims and fictional Story Claims remain separate even when one motivates the other.

## Lemma execution policy
- `lemma/*.lemma` remains the repository's deterministic rules-as-code layer and is versioned and validated in GitHub.
- GitHub `main` is authoritative for both Storybible content and Lemma source.
- LemmaBase is optional and downstream-only; it never overrides GitHub canon.
