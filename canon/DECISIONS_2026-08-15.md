# Canon decisions — 15 August 2026

These decisions process the execution/Reformation material from the 15 August 2026 research chat. They do not replace earlier decisions; they add a focused execution-culture layer.

## DEC.CLAES.EXECUTIONS_REFORMATION_ARC.2026-08-15 — CANON

The novel must process sixteenth-century executions as a structural moral and religious arc in Claes' life, not merely as historical atmosphere.

Claes begins within a Catholic civic understanding of execution: ordinary criminals may die under the ars moriendi script of confession, priestly consolation, cross, repentance, prayer and public compassion. The Reformation breaks that shared death script. Wederdopers and Reformed condemned persons increasingly die as witnesses rather than penitents; spectators become active through encouragement, kissing, psalm-singing, stone throwing, rescue attempts, letters, songs and later martyrology.

This arc must connect to the code architecture: bodies can be burned, drowned, displayed or silenced; voices can be blocked by tongschroef or secrecy; therefore testimony must learn to survive through indirect carriers such as letters, relics, hidden writing, books and code.

## DEC.CLAES.CORNELIS_EXECUTION_WITNESS.2026-08-15 — CANON

Claes must be physically present as witness at Cornelis' execution.

This fixes the witness relation and scene function. It does **not** close the exact date, place, formal charge, execution method or degree of public ritual. Those remain under `OPEN.CORNELIS.DEATH.001`, bounded by the existing working canon of second half 1568 through 1569.

Cornelis' death must not depend on him carrying `OBJ.MEMORIAAL`. Dee gave Claes the memoriaal early in 1564 as a pedagogical workbook; only after 4 October 1564 is that existing object prepared as blind recovery carrier.

Cornelis should remain a vulnerable logistical carrier and father, not a protected printer and not necessarily an open preacher. His plausible death model is: routes, vaten, storage, prohibited papers/books/liederen/prenten, dangerous contacts and refusal to give names. His strongest dramatic death-script is protective silence between Catholic ars moriendi and Protestant martyr display.

## DEC.CORNELIS.DEATH.1569.2026-08-15 — CANON RESOLUTION IN AUTHORING BRANCH

Cornelis' death is resolved for this authoring branch as a fictional but historically plausible public execution in Antwerp:

- **Date:** 12 March 1569.
- **Place:** Antwerp, from detention in or by Het Steen to public execution on the Grote Markt before/near the Stadhuis.
- **Formal story charge:** logistical complicity in the transport, concealment and distribution of forbidden, heretical and seditious books, papers, liederen, figures/prints and correspondence between Antwerp, Goes and Zeeland; refusal under examination to name accomplices, readers, printers, binders, carriers or recipients.
- **Execution method:** public beheading by sword, not burning and not secret drowning.
- **After-ritual:** selected confiscated papers are burned separately as visible evidence; Cornelis' body is not returned to Claes. Any display of head/body is short and punitive, not turned into a full martyr cult.
- **Witness:** Claes is physically present in the crowd and sees the execution.
- **Final transfer:** Cornelis' final usable clue remains minimal: `Castanea. Niet onze bloem — de boom.` It may be given during a last guarded prison contact or at the edge of the execution route, but never as a public explanation.

Rationale:

Cornelis is not executed as a protected printer like Plantin or Silvius and not as an open preacher. He is executed as the expendable logistical body of a network: the man whose route, vaten, storage, papers, contacts and silence make otherwise deniable book traffic visible. Beheading rather than burning keeps him between death-scripts: he is not presented as an ordinary repentant criminal under the Catholic ars moriendi, but he is also not allowed or written as a loudly singing Protestant martyr. His death is protective silence.

Guardrails:

- Do not make Cornelis the author, printer or full-key holder.
- Do not make `OBJ.MEMORIAAL` the object found on him.
- Do not make Claes understand Las Casas, merels, Monas or the recovery architecture at the execution.
- Do not make Fabritius alone the legal cause of the 1569 sentence; Fabritius remains the 1564 security-break catalyst, while Cornelis' later fall requires transport traces, papers, contacts and refusal to name others.
- Mark this as novel canon/authoring-branch resolution, not archival evidence of a historical Cornelis execution.

## Clarification — Fabritius and the 4 October 1564 security break

Fabritius is the preferred historical candidate for the already canonical `NI.EVENT.SECURITY_BREAK.1564.001` because the date, stones, psalm-singing, public-control failure and Antwerp context fit the existing storybible hinge.

This remains a candidate until `OPEN.SECURITY.LOW_LINK.1564.001` is explicitly closed. Cornelis need not be a stone thrower, need not sing, need not try to rescue Fabritius and need not be arrested in 1564. The fixed story function is that the event makes Cornelis operationally unsafe as direct-key recipient and activates the fallback architecture.

## Required synchronization

This decision is synchronized in this branch through:

- `storybible/EXECUTIONS_REFORMATION_CLAES.md`
- `storybible/CORNELIS_EXECUTION_1569.md`
- `claims/SOURCE_CLAIMS_EXECUTIONS_REFORMATION.yaml`
- `claims/STORY_CLAIMS_EXECUTIONS_REFORMATION.yaml`
- `narrative/instances_executions_reformation.yaml`

Remaining pending after this branch, if accepted:

- update `canon/OPEN_DECISIONS.yaml` to note that Claes witnessing Cornelis' execution is fixed and that this branch proposes/closes the 12 March 1569 Antwerp execution model;
- optionally promote Fabritius from preferred candidate to closed historical identification of `NI.EVENT.SECURITY_BREAK.1564.001`;
- fold the dossier into the next synchronized operating master rather than duplicating all material in `LEMMA_MCKEE_MASTER_2026-08-13.md` immediately;
- add Lemma constraints after this execution date/place/method is accepted into main.
