# Handoff — Executions and Reformation arc, 15 August 2026

Status: `SYNC_PENDING`

Branch: `authoring/executions-reformation-2026-08-15`

## Work completed

Created a focused execution/Reformation synchronization layer:

- `storybible/EXECUTIONS_REFORMATION_CLAES.md`
- `claims/SOURCE_CLAIMS_EXECUTIONS_REFORMATION.yaml`
- `claims/STORY_CLAIMS_EXECUTIONS_REFORMATION.yaml`
- `narrative/instances_executions_reformation.yaml`
- `canon/DECISIONS_2026-08-15.md`
- updated `storybible/INDEX.md`

## Human decisions captured

- The execution/Reformation material must become a structural storybible layer, not loose background.
- Claes must witness Cornelis' execution.
- The memoriaal correction is preserved: Dee gives the ordinary-looking memoriaal in early 1564; Cornelis does not hand it to Claes.

## Open matters preserved

- `OPEN.CORNELIS.DEATH.001` remains open for exact date, place, formal charge and execution method. Only the witness relation is fixed.
- `OPEN.SECURITY.LOW_LINK.1564.001` remains open. Fabritius is recorded as the preferred historical candidate for the 4 October 1564 security break but not silently promoted to fully closed canon.
- `OPEN.MEMORIAAL.BINDING.001` remains open for the exact binding/material mechanism after the safety break.

## Source basis

- Isabel Casteels, *Looking for Justice: execution spectators and the Revolt in the Low Countries, ca. 1520-1585*.
- Doopsgezinde Martelaarsspiegel / extracted Antwerp martyr lists.
- Allard Pierson material on Maeyken Wens.
- Previous in-chat extraction on Fabritius, Het Steen, Maeyken Wens, Hans Bret, Jan Grendel and relevant route events.

## Remaining synchronization

After review/acceptance:

1. Update `canon/OPEN_DECISIONS.yaml` to add the fixed Cornelis-witness constraint and Fabritius preferred-candidate note.
2. Optionally fold a compressed version into `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` or the next dated operating master.
3. Add deterministic Lemma constraints only after date/place/method for Cornelis' execution are fixed.
4. Run repository validation/CI.

Validation has not been run locally in this session; PR CI should check repository structure after opening.
