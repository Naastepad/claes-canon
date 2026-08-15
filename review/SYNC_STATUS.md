# Synchronization status

Status: `SYNC_PENDING`

Release state: `AUTHORING_BRANCH`

Branch: `authoring/memoriaal-brevisima-print-20260815`

The explicit 15 August 2026 author decision `DEC.MEMORIAAL.DIRECT_TEXT_NO_CIPHER.2026-08-15` has replaced the former cipher workaround across the primary structured canon layers. The active model is now chemical steganography: readable Diets/Brabant text is invisibly printed before binding and later revealed directly by green vitriol. The branch remains **SYNC_PENDING**, rather than `SYNC_COMPLETE`, because two older broad prose dossiers still contain cipher-era wording and require regeneration/patching before final synchronization.

## New canonical memoriaal state

- the completed readable Diets/Brabant *Brevísima* is set in ordinary movable type and printed on loose sheets **before binding**;
- the reconstructed first-pass printing medium is clear gallnut/tannin extract + gum arabic, without intentional iron/vitriol, soot or visible pigment;
- the printed sheets are dried, folded/gathered and bound as `OBJ.MEMORIAAL`, an apparently blank writing book;
- Dee gives that already prepared memoriaal to Claes before Boom in early 1564;
- Dee simultaneously gives `OBJ.GRAPHITE_STIFT` and forbids ink while Claes remains his pupil;
- Claes' graphite observations form the visible layer while the readable tannin-printed Brevísima remains latent;
- Claes knows the pedagogical workbook and graphite-only rule but not the hidden Brevísima payload or the chemical reason for avoiding ink;
- 4 October 1564 remains the security/Nigredo and political/network hinge but does not load, recipher, key, lock or unlock the memoriaal;
- green vitriol later reveals `OBJ.LASCASAS_PLAINTEXT` directly from the memoriaal;
- reveal is reading, not decryption;
- the former `FINAL CIPHER-1564`, direct key, 24×24 matrix, merels recovery set, Monas ordering key, Castanea key anchor, special Dodoens nomenclator carrier, Primus Index and multi-week reconstruction are deprecated for the Brevísima mechanism;
- merels, *Monas*, Dodoens and Castanea may remain elsewhere only for independent narrative/historical functions;
- `OBJ.ZOVITIUS_1570_TRIGGER` may remain as a material cue through `GALLA LEO VIRIDIS`, not as a cryptographic key.

## Synchronized files in this authoring branch

- `canon/DECISIONS_2026-08-15.md`
- `canon/DECISIONS.yaml`
- `claims/STORY_CLAIMS.yaml`
- `claims/STORY_CLAIMS_EXECUTIONS_REFORMATION.yaml`
- `claims/SOURCE_CLAIMS_MEMORIAAL_PRINT_1564.yaml`
- `sources/SRC-HIST-PLANTIN-PRINT-DIALOGUES-1567-001.md`
- `sources/SRC-SECONDARY-BOONMAN-METROLOGY-2015-001.md`
- `objects/OBJECTS.yaml`
- `narrative/instances.yaml`
- `narrative/instances_executions_reformation.yaml`
- `narrative/knowledge_states.yaml`
- `narrative/relationships.yaml`
- `narrative/code_architecture.yaml` — legacy filename; active content is direct material reveal with deprecated cipher history
- `canon/OPEN_DECISIONS.yaml`
- `lemma/decode.lemma` — legacy filename; active rule is direct plaintext reveal from memoriaal + vitriol availability
- `storybible/MEMORIAAL_BREVISIMA_PRINT_1564.md`
- `storybible/CORNELIS_EXECUTION_1569.md`
- `storybible/MASTER.md`
- `storybible/INDEX.md`
- `review/MIGRATION_REVIEW.yaml`
- `review/SYNC_STATUS.md`

## Explicit supersession

`DEC.MEMORIAAL.BREVISIMA_PRINT_GIFT.2026-08-15` is retained as `DEPRECATED` development history and is superseded by `DEC.MEMORIAAL.DIRECT_TEXT_NO_CIPHER.2026-08-15`.

The following Story Claims/objects remain only as deprecated audit history where present: `STC.MEMORIAAL.SECRET_PHASE.001`, `STC.CORNELIS.FALLBACK_KNOWLEDGE.001`, the `STC.CODE.*` recovery claims, `OBJ.LASCASAS_CIPHERTEXT`, `OBJ.DIRECT_KEY`, `OBJ.MERELS_24` as recovery object, `OBJ.CASTANEA` as key anchor, `OBJ.DODOENS_CARRIER` as nomenclator carrier and `OBJ.PRIMUS_INDEX`.

The authoritative domain dossier is `storybible/MEMORIAAL_BREVISIMA_PRINT_1564.md`.

## Historical/reconstruction boundary

- `SRC-HIST-PLANTIN-PRINT-DIALOGUES-1567-001` supports period Antwerp printing apparatus and craft criteria; it does not document tannin/gum invisible printing.
- `SRC-SECONDARY-BOONMAN-METROLOGY-2015-001` supports the medicinal ounce/drachm framework used for the reconstructed workshop measures.
- `SC.RECON.MEMORIAAL.TANNIN_GUM_PRINT.001` explicitly labels the tannin/gum metal-type process as a plausible authorial technical reconstruction, not a recovered Plantin/Silvius recipe.
- `OPEN.MATERIAL.WET_TEST.001` remains required to determine real transfer, dry visibility/gloss, *moet*, paper behavior and vitriol-development performance.
- `OPEN.GRAPHITE_STIFT.PROVENANCE.1564.001` preserves uncertainty about the exact physical form/provenance of Dee's graphite marking tool while leaving its story function fixed.

## Validation

- The first direct-text continuity run exposed a YAML quoting error in `canon/DECISIONS.yaml`; that parse error was repaired without changing the decision.
- **Validate Claes canon repository**, run **200**: continuity compilation passed on commit `3dd0c172b33bd6d768f95da2b3ca2f28b91b6a91`.
- **Validate Lemma canon**, run **118**: all active Lemma specs passed on the same commit.
- Later commits in this branch update only human-readable navigation/authority surfaces (`storybible/MASTER.md`, `storybible/INDEX.md`, this sync record); final PR-head validation should be checked again before merge.

## Remaining synchronization work

1. Regenerate or patch `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md`, which still contains the old post-4-October carrier and cipher/key-recovery architecture.
2. Patch/regenerate `storybible/EXECUTIONS_REFORMATION_CLAES.md`, whose broad execution/testimony analysis still contains old direct-key, Castanea and code-as-testimony wording. The structured execution claims/instances and `CORNELIS_EXECUTION_1569.md` are already synchronized and outrank those stale passages.
3. After those two broad prose surfaces are synchronized, rerun repository and Lemma validation and only then promote this record to `SYNC_COMPLETE`.

## Existing family state remains unchanged

The integrated Goes fire/family rupture, Tanneken Jansdochter, Jan Corneliszn. Nissepat and both grandparent lines remain canonical and are not altered by this branch.

## Lemma execution policy

- `lemma/*.lemma` remains the deterministic rules-as-code layer and is versioned and validated in GitHub.
- `lemma/decode.lemma` now has one active material-access rule: readable plaintext can be revealed when the memoriaal and green vitriol are available under active canon.
- GitHub `main` remains authoritative until this authoring branch is reviewed/merged.
- LemmaBase is optional and downstream-only; it never overrides GitHub canon.
