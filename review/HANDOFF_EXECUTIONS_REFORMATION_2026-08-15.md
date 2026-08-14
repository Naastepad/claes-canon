# Handoff — Executions and Reformation arc, 15 August 2026

Status: `SYNC_PENDING`

Branch: `authoring/executions-reformation-2026-08-15`

Draft PR: #8, `Add executions and Reformation arc`

## Work completed

Created and revised a focused execution/Reformation synchronization layer:

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
- Cornelis' death model is revised for historical plausibility: first arrest/examination in autumn 1567 with borg/conditions, renewed exposure in 1568/1569 through clandestine paper/book traffic and the March 1569 Antwerp book visitations, then execution in Antwerp on 19 November 1569 in the documented market book-burning environment.

## Revised Cornelis model

The earlier 12 March 1569 authoring draft is rejected as too arbitrary. Current authoring-branch resolution:

- **First exposure:** autumn 1567, Antwerp; arrest or serious examination in a forbidden paper/book/print matter; release on borg or equivalent conditions.
- **Renewed exposure:** late 1568 through March 1569; clandestine copy/distribution routes, bookshop visitations, forbidden/seditious papers, liederen, figures/prints, libels/billets and correspondence.
- **Execution:** 19 November 1569, Antwerp.
- **Public setting:** from detention in or by Het Steen into the Grote Markt/Stadhuis environment on the day books seized in March are publicly burned.
- **Execution method:** preferred public beheading by sword, justified only by seditious/network/recidive framing; simple book smuggling is explicitly insufficient.
- **Witness:** Claes is physically present.
- **Guardrail:** Cornelis is a fictional insertion into a documented ritual environment; do not claim that Haecht names him or that he is one of Haecht's seven offenders.

## Open matters preserved or narrowed

- `OPEN.CORNELIS.DEATH.001` should be marked resolved/narrowed if this branch is accepted: exact date/place/charge/method are now proposed as a concrete authoring-branch resolution under `DEC.CORNELIS.DEATH.1569.2026-08-15.REVISED`.
- `OPEN.SECURITY.LOW_LINK.1564.001` remains open. Fabritius is recorded as the preferred historical candidate for the 4 October 1564 security break but not silently promoted to fully closed canon.
- `OPEN.MEMORIAAL.BINDING.001` remains open for the exact binding/material mechanism after the safety break.

## Source basis

- Isabel Casteels, *Looking for Justice: execution spectators and the Revolt in the Low Countries, ca. 1520-1585*.
- Doopsgezinde Martelaarsspiegel / extracted Antwerp martyr lists.
- Allard Pierson material on Maeyken Wens.
- Guido Marnef, `Repressie en censuur in het Antwerps boekbedrijf, 1567-1576`.
- Guido Marnef, `Antwerpen in de tijd van de Reformatie`, chapter on the Calvinist community under pressure.
- Godevaert van Haecht, November 1569 chronicle entry: 19 November book burning, same-day executions, 23 November tongue-screw burnings.
- Antwerpsch chronykje 1569 for place/method checks.
- Previous in-chat extraction on Fabritius, Het Steen, Maeyken Wens, Hans Bret, Jan Grendel and relevant route events.

## Remaining synchronization

After review/acceptance:

1. Update `canon/OPEN_DECISIONS.yaml` to mark the Cornelis-death variables resolved/narrowed by `DEC.CORNELIS.DEATH.1569.2026-08-15.REVISED`.
2. Optionally fold a compressed version into `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` or the next dated operating master.
3. Add deterministic Lemma constraints for Cornelis' execution date/place/witness relation and for the fact that the execution cannot involve possession of `OBJ.MEMORIAAL`.
4. Run repository validation/CI.

Validation has not been run locally in this session; PR CI should check repository structure after opening.
