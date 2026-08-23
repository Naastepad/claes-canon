# Synchronization status

Status: `SYNC_PENDING` — the approved 23-Aug-2026 adult-spine decisions are synchronized through the main decision, story-claim, entity, relationship, theme and narrative registers and through the repository entrypoints. Remaining work is consolidation of the older operating master, exact historical source claims, and validator/CI/release work.

## 23-Aug-2026 adult spine — completed in this pass
- `canon/DECISIONS_2026-08-23.md` — explicit author decisions for the 1564 seed / 1566 spine start, Las Casas rescaling, Mayken, northern route, pre-Seton transmutation, Seton function, Hoghelande correction and VOC resonance.
- `canon/DECISIONS.yaml` — machine-readable decision registry synchronized with the 23-Aug author decisions.
- `storybible/modules/CLAES_RUGGENGRAAT_1564_1602.md` — active human-readable adult-spine module. It explicitly states that Dee's 1564 question is the seed, while **Claes' departure from Antwerp after the 1566 Beeldenstorm is the operational/geographical start of the ruggengraat**.
- `claims/STORY_CLAIMS.yaml` — accepted Story Claims for the adult spine, Dee's lifelong question, dual return motive, Mayken identity/reputation line, Las Casas scale/publication, Gouda flight, northern route, ambiguous pre-Seton transmutation, Seton, Hoghelande, VOC resonance and historical-witness guardrail.
- `entities/ENTITIES.yaml` — beloved identity fixed as Mayken; Gouda, Egmond, Alkmaar and Hoorn added; Seton, Haussen, Vanderlinden and Hoghelande added with source-weighted usage guardrails.
- `narrative/arcs.yaml` — `ARC.CLAES.LIFELONG_INQUIRY` added; Dee arc extended to the lifelong-question seed and internalised legacy.
- `narrative/instances.yaml` — 1564 seed, 1566 Antwerp-departure/Goes-return spine start, 1578 Mayken reputation/flight, northern route, Claes' own ambiguous transmutation and Seton sequence registered.
- `narrative/relationships.yaml` — Mayken identity propagated into the base relationship registry; 1578 danger/northern companionship added; Silvius relation extended to the 1578 dangerous-transmission phase; Dee relation extended with the unresolved-question phase.
- `narrative/beloved_recovery.yaml` — Mayken fixed as the beloved/recovery companion, with agency and explicit exclusion of rape/DID as route mechanisms and no required formal Goese witch trial.
- `narrative/themes.yaml` — lifelong dangerous-knowledge progression and historical-pressure guardrail added; controlling idea now explicitly applies to `ARC.CLAES.LIFELONG_INQUIRY`.
- `canon/OPEN_DECISIONS.yaml` — beloved identity and stale mother-adult-function items removed; exact 1578 trigger, Gouda flight date, northern residences, pre-Seton transmutation, Seton bridge, Hoghelande contact and source-sync questions added.
- `storybible/INDEX.md` — adult-spine module and 23-Aug decision layer indexed with a dedicated writing package.
- `AI_REPOSITORY_MANIFEST.md` — adult-spine decisions/module registered in mandatory bootstrap and scene-use guidance; the ruggengraat-start distinction is explicit.

## 23-Aug-2026 adult spine — still pending
- `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` has **not yet been textually folded forward**. Until that happens, `canon/DECISIONS_2026-08-23.md`, synchronized `STC.*` records and `storybible/modules/CLAES_RUGGENGRAAT_1564_1602.md` outrank conflicting older master wording under the repository authority hierarchy.
- `AI_ONBOARDING.md` still names the 13-Aug master as the sole current operating master. The manifest now routes adult-spine users correctly, but onboarding should eventually be folded forward or point explicitly to the 23-Aug decision/module overlay.
- Exact historical assertions discussed on 23 August require source-layer work before documentary precision is used in prose: especially the exact 30 September 1578 Goes church event/date, the Seton–Haussen–Vanderlinden report chain, Hoghelande chronology and later Seton account, and the exact 1602 VOC/Seton timing relationship. Story functions are approved; evidence status remains separate.
- The existing `storybible/modules/GOES_RELIGIOUS_TRANSITION_1577_1578.md` still contains the guardrail not to assert an exact 1578 date without local evidence. That guardrail remains authoritative until the new local source claim is registered.
- Historical route details for Gouda, Delft, Egmond/Alkmaar, Hoorn and Enkhuizen still require scene-specific source work; the macro route is story canon, exact local implementation is not yet documentary fact.
- Validator/CI and branch reconciliation have not been run in this connector pass.

## Verified completed layers from 13-Aug-2026 work
- `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` — previous active operating master; now partially superseded by 23-Aug decisions in the adult-spine domain until a new consolidated master is produced.
- `narrative/religious_space_sensory_church.yaml` + `sources/SRC-WAUTERS-RELIGIOUS-SPACE-2021.md` — sensory church / period *sinne* / guild-confraternity-rederijker infrastructure.
- `sources/SRC-HIST-CATHOLIC-BIBLE-LOWCOUNTRIES-1548-001.md` — Latin/Vulgate, Leuven Bible 1548, Liesvelt comparison/reprint context.
- `sources/SRC-LUKE8-LEUVEN-LIESVELT-COMPARISON.md` — source-verified correction of the earlier false/reconstructed Luke 8 comparison.
- `sources/SRC-VAN-BRUAENE-OM-BETERS-WILLE-2008.md` — rederijkers as civic-religious communication networks.
- `sources/SRC-POLLMANN-MEMORY-EARLY-MODERN-EUROPE-2017.md` — material/social memory and violence/silence guardrails.
- `sources/SRC-GROENVELD-ETAL-TACHTIGJARIGE-OORLOG-2008.md` — correctly attributed general Revolt chronology and Goes/Reimerswaal anchors.
- `sources/SRC-CANON-NL-OPSTAND-2026.md` — supplementary national/Zeeland chronology locators.
- `sources/SRC-POLLMANN-CATHOLIC-IDENTITY-2011.md` — bibliographically verified, content only partially verified from official OUP/Leiden abstracts; **full book not read because full text is not available in the current sources**.
- `storybible/modules/GOES_RELIGIOUS_TRANSITION_1577_1578.md` — local Goes religious-transition module.
- `history/LOW_COUNTRIES_TRANSFORMATION_1540_1605.yaml` — expanded macro historical event spine populated through 1605.
- `history/LOW_COUNTRIES_TRANSFORMATION_1540_1605.md` — expanded human-readable chronology through 1605.
- `history/ZEELAND_REVOLT_TIMELINE.yaml` — normalised regional timeline through the principal Zeeland anchors to 1604.
- `storybible/modules/HISTORICAL_SUBSTRATE_1540_1605.md` — links the history layer into storybible scene construction.
- `claims/SOURCE_CLAIMS.yaml` — central registry includes the earlier Goes 1577, Goes 1578 and Reimerswaal 1574 local claims and corrected Pollmann provenance/status; it does not yet contain the new 23-Aug exact-source additions listed above.
- `review/CHAT_COMMITMENT_AUDIT_2026-08-13.md` plus `review/CHAT_COMMITMENT_AUDIT_ADDENDUM_2026-08-13.md` — execution audit and closure of items that succeeded only after retry.

## Macro chronology completion boundary
The 1540–1605 historical substrate represents the **major political, military, confessional and civic-cultural transformations that can materially change Claes' scene conditions**. It is not defined as a catalogue of every skirmish, ordinance, tax measure or office-holder.

The populated sequence includes the pre-Revolt Catholic/print context, 1555 succession, 1559–61 church reform, 1561 Landjuweel, 1564–66 confessional escalation, 1567–69 repression, the Zeeland/Holland territorial war from 1572, Goes/Middelburg/Reimerswaal/Zierikzee anchors, Pacification 1576, Goes 1577–78, Arras/Utrecht and Abjuration, Orange's death, Antwerp 1585, Republic/Armada 1588, Maurits' consolidation campaigns in the 1590s, Nieuwpoort, Ostend, VOC/late-Republic context, Sluis 1604 and Spinola campaigning in 1605.

## Truth-status corrections
Earlier assistant statements that the initial historical scaffolding was already the "whole" relevant Eighty Years' War were false. The corrective expansion has now been performed and repository-checked.

Earlier reconstructed Dutch Luke 8 wording in chat was also falsely presented as source text. It is withdrawn. The repository now contains a source-verified Leuven 1548 / Liesvelt 1542 comparison and explicitly prohibits reuse of the fabricated wording.

The Wauters work is recorded as `TARGETED_REVIEW` of the complete set of themes requested by the author, not as a false claim of cover-to-cover linear reading.

## Remaining research / access limits — not completed claims
- Full-text Pollmann 2011 chapter-level extraction cannot be completed without access to the monograph; only official bibliographic metadata and chapter abstracts have been verified.
- Goes 1572 civilian/guild/church/provisioning microhistory.
- Exact Goes 1578 implementation: first Reformed sermon/date/building, named actors, clergy response, altar/image sequence and private Catholic adaptation; now expanded by the 23-Aug requirement to verify the proposed 30 September 1578 event/date in the local source layer.
- Reimerswaal 1570s interaction of war, flood/erosion, demography, trade and ecclesiastical life.
- Annual/seasonal Zeeland taxation, billeting, provisioning, food prices, disease and shipping.
- Seton/Haussen/Vanderlinden evidence grading and exact Enkhuizen chronology.
- Hoghelande biographical chronology and exact evidentiary status of his later Seton material.
- Gouda, Delft, Egmond/Alkmaar, Hoorn and Enkhuizen microhistorical scene substrate for Claes' exact occupations/residences.

These are explicitly research expansions, not concealed omissions from a deliverable described as complete.

## Release status
Branch reconciliation with current `main`, validator/CI run and any merge/publication remain separate release tasks. No autonomous merge is authorised.