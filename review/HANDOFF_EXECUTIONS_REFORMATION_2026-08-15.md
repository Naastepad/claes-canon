# Handoff — Executions and Reformation arc, 15 August 2026

Status: `SYNC_PENDING`

Branch: `authoring/executions-reformation-2026-08-15`

Draft PR: #8, `Add executions and Reformation arc`

## Work completed

Created a focused execution/Reformation synchronization layer:

- `storybible/EXECUTIONS_REFORMATION_CLAES.md`
- `storybible/CORNELIS_EXECUTION_1569.md`
- `claims/SOURCE_CLAIMS_EXECUTIONS_REFORMATION.yaml`
- `claims/STORY_CLAIMS_EXECUTIONS_REFORMATION.yaml`
- `narrative/instances_executions_reformation.yaml`
- `canon/DECISIONS_2026-08-15.md`
- updated `storybible/INDEX.md`

## Human decisions captured

- The execution/Reformation material must become a structural storybible layer, not loose background.
- Claes must witness Cornelis' execution.
- The memoriaal correction is preserved: Dee gives the ordinary-looking memoriaal in early 1564; Cornelis does not hand it to Claes.
- Cornelis' execution is now worked out in this authoring branch as: Antwerp, 12 March 1569, public beheading by sword after detention in or by Het Steen; formal story charge is logistical complicity in forbidden/heretical/seditious book-paper-liederen-figures traffic and refusal to name others.

## Open matters preserved or narrowed

- `OPEN.CORNELIS.DEATH.001` should be marked resolved/narrowed if this branch is accepted: exact date/place/charge/method are now proposed as a concrete authoring-branch resolution.
- `OPEN.SECURITY.LOW_LINK.1564.001` remains open. Fabritius is recorded as the preferred historical candidate for the 4 October 1564 security break but not silently promoted to fully closed canon.
- `OPEN.MEMORIAAL.BINDING.001` remains open for the exact binding/material mechanism after the safety break.

## Source basis

- Isabel Casteels, *Looking for Justice: execution spectators and the Revolt in the Low Countries, ca. 1520-1585*.
- Doopsgezinde Martelaarsspiegel / extracted Antwerp martyr lists.
- Allard Pierson material on Maeyken Wens.
- Previous in-chat extraction on Fabritius, Het Steen, Maeyken Wens, Hans Bret, Jan Grendel and relevant route events.

## Remaining synchronization

After review/acceptance:

1. Update `canon/OPEN_DECISIONS.yaml` to mark the Cornelis-death variables resolved/narrowed by `DEC.CORNELIS.DEATH.1569.2026-08-15`.
2. Optionally fold a compressed version into `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` or the next dated operating master.
3. Add deterministic Lemma constraints for Cornelis' execution date/place/witness relation and for the fact that the execution cannot involve possession of `OBJ.MEMORIAAL`.
4. Run repository validation/CI.

Validation has not been run locally in this session; PR CI should check repository structure after opening.
