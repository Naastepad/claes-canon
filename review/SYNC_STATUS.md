# Synchronization status

Status: `SYNC_PENDING`

Release state: `AUTHORING_BRANCH`

Branch: `authoring/memoriaal-brevisima-print-20260815`

The explicit 15 August 2026 author decision for the memoriaal/Brevísima carrier has been normalized across the primary structured canon layers. Repository continuity and Lemma validation are green for the canonical content commit `2a08146b7af36ae824ed38ba8c6c0f41cc454d96`. The branch remains **SYNC_PENDING**, rather than `SYNC_COMPLETE`, solely because the dated broad synthesis `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` still contains the superseded post-4-October memoriaal model and must be regenerated or explicitly patched before final synchronization.

## New canonical memoriaal state

- the encoded translated Diets/Brabant *Brevísima* is printed on loose sheets **before binding**;
- the reconstructed first-pass printing medium is clear gallnut/tannin extract + gum arabic, without intentional iron/vitriol, soot or visible pigment;
- the printed sheets are dried, folded/gathered and bound as `OBJ.MEMORIAAL`, an apparently blank writing book;
- Dee gives that already prepared memoriaal to Claes before Boom in early 1564;
- Dee simultaneously gives `OBJ.GRAPHITE_STIFT` and forbids ink while Claes remains his pupil;
- Claes knows the pedagogical workbook and graphite-only rule but not the hidden Brevísima payload or the chemical reason for avoiding ink;
- 4 October 1564 remains the security/Nigredo hinge but no longer loads or reciphers the memoriaal;
- green vitriol later reveals `OBJ.LASCASAS_CIPHERTEXT` directly from the memoriaal;
- physical ciphertext reveal and cryptographic key recovery are now separate paths;
- `OBJ.MERELS_24` remains canonical key recovery, but its exact new in-world placement/entry route is open.

## Synchronized files in this authoring branch

- `canon/DECISIONS_2026-08-15.md`
- `canon/DECISIONS.yaml`
- `claims/STORY_CLAIMS.yaml`
- `claims/SOURCE_CLAIMS_MEMORIAAL_PRINT_1564.yaml`
- `sources/SRC-HIST-PLANTIN-PRINT-DIALOGUES-1567-001.md`
- `sources/SRC-SECONDARY-BOONMAN-METROLOGY-2015-001.md`
- `objects/OBJECTS.yaml`
- `narrative/instances.yaml`
- `narrative/knowledge_states.yaml`
- `narrative/relationships.yaml`
- `narrative/code_architecture.yaml`
- `canon/OPEN_DECISIONS.yaml`
- `lemma/decode.lemma`
- `storybible/MEMORIAAL_BREVISIMA_PRINT_1564.md`
- `storybible/MASTER.md`
- `storybible/INDEX.md`
- `review/MIGRATION_REVIEW.yaml`
- `review/SYNC_STATUS.md`

## Explicit supersession

`STC.MEMORIAAL.SECRET_PHASE.001` is retained as `DEPRECATED` audit history. The former rules that the memoriaal is physically loaded only after 4 October 1564, that vitriol reveals a 24+2 merels layer rather than Las Casas ciphertext, and that the memoriaal itself supplies the merels/theorem bridge are superseded by `DEC.MEMORIAAL.BREVISIMA_PRINT_GIFT.2026-08-15`.

The authoritative domain dossier is now `storybible/MEMORIAAL_BREVISIMA_PRINT_1564.md`.

## Historical/reconstruction boundary

- `SRC-HIST-PLANTIN-PRINT-DIALOGUES-1567-001` supports period Antwerp printing apparatus and craft criteria; it does not document tannin/gum invisible printing.
- `SRC-SECONDARY-BOONMAN-METROLOGY-2015-001` supports the medicinal ounce/drachm framework used for the reconstructed workshop measures.
- `SC.RECON.MEMORIAAL.TANNIN_GUM_PRINT.001` explicitly labels the tannin/gum metal-type process as a plausible authorial technical reconstruction, not a recovered Plantin/Silvius recipe.
- `OPEN.MATERIAL.WET_TEST.001` remains required to determine real transfer, dry visibility/gloss, *moet*, paper behavior and vitriol-development performance.
- `OPEN.GRAPHITE_STIFT.PROVENANCE.1564.001` preserves uncertainty about the exact physical form/provenance of Dee's graphite marking tool while leaving its story function fixed.

## Validation

- **Validate Claes canon repository**, run 184: continuity compilation passed on commit `2a08146b7af36ae824ed38ba8c6c0f41cc454d96`.
- **Validate Lemma canon**, run 102: all active Lemma specs passed on the same commit.
- The validation failures in earlier PR #9 runs were repaired: first a YAML quoting error in `STC.CODE.RECOVERY_SEQUENCE.001`, then the three new memoriaal Story Claims were added to `review/MIGRATION_REVIEW.yaml` and its totals synchronized from 54 to 57.

## Remaining synchronization work

1. Regenerate or patch `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` so its old memoriaal sections no longer contradict the 15 August decision.
2. After that master synchronization, rerun repository and Lemma validation before changing this status to `SYNC_COMPLETE`.
3. Resolve separately, not silently, `OPEN.MERELS.ENTRY_AFTER_MEMORIAAL_REDESIGN.001`; this is a story-design open question, not a synchronization defect in the new physical carrier decision.

## Existing family state remains unchanged

The integrated Goes fire/family rupture, Tanneken Jansdochter, Jan Corneliszn. Nissepat and both grandparent lines remain canonical and are not altered by this branch.

## Lemma execution policy

- `lemma/*.lemma` remains the deterministic rules-as-code layer and is versioned and validated in GitHub.
- `lemma/decode.lemma` in this branch now requires the ciphertext-reveal route and independent key-recovery prerequisites to converge before full decoding.
- GitHub `main` remains authoritative until this authoring branch is reviewed/merged.
- LemmaBase is optional and downstream-only; it never overrides GitHub canon.
