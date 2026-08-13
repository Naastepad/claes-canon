# Chat commitment audit — 13 August 2026

Purpose: record whether tasks explicitly approved by the author in the religious-space / Bible / Revolt research chat were **actually executed**, rather than inferred from assistant prose.

Status vocabulary:
- `DONE_VERIFIED` — repository output exists and its relevant content was checked.
- `DONE_WITH_LIMIT` — requested deliverable exists, but a stated source/access or normalization limitation remains.
- `NOT_DONE` — not executed; must not be described as complete.
- `BLOCKED` — attempted but tool safety/connector blocked the write; no completion claim allowed.

## 1. Add Catholic Bible/liturgy research to the storybible
**Author approval:** explicit request to read/check and add to storybible; subsequent retry approvals.

**Status: `DONE_VERIFIED`.**

Evidence:
- `claims/SOURCE_CLAIMS.yaml` contains the Latin/Vulgate, Leuven Bible 1548, Liesvelt and Catholic-identity claims.
- `sources/SRC-HIST-CATHOLIC-BIBLE-LOWCOUNTRIES-1548-001.md` exists.
- `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md` contains the Catholic Scripture/liturgy/confessional-change section and Lucas 8 guardrail.

Correction record: an earlier chat answer presented reconstructed Dutch Luke 8 wording as if it were exact historical text. That wording is **not** present in the repository. The verified Leuven 1548 text reads at Luke 8:5: `Hy is wtghegaen die saeyt om sijn saet te saeyen...`; Luke 8:11: `Ende dit is die ghelijckenisse, Tsaet is dwoort Gods`. Future quotation must use checked editions, never the earlier chat reconstruction.

## 2. Build a complete relevant sensory-church module from Wauters material, with guilds/rederijkers and transfer rules to Goes/Reimerswaal
**Author approval:** explicit `Doe dat` after proposal for `WORLD.RELIGIOUS_SPACE.SENSORY_CHURCH`.

**Status: `DONE_VERIFIED` for the requested thematic extraction.**

Evidence:
- `sources/SRC-WAUTERS-RELIGIOUS-SPACE-2021.md` exists.
- `narrative/religious_space_sensory_church.yaml` exists.
- `narrative/themes.yaml` links `VALUE.CLAES.SINNE` to the world module.
- active master §11 invokes the module.

Scope actually executed: targeted, extensive thematic review of relevant sections on period *sinne*/sensus communis, sight/sound/smell/touch, liturgy, church movement, graves, guilds/ambachts/brotherhoods, rederijkers, processions, social topography and memory. This is **not represented as a cover-to-cover linear reading** of every page of every Wauters publication.

## 3. Retry blocked Wauters/storybible crosslinks
**Author approvals:** `Go`, then `Probeer het nog eens`.

**Status: `DONE_VERIFIED`.**

The themes crosslink and master references were eventually written successfully. Earlier blocked attempts are historical tool failures, not current missing content.

## 4. Process Van Bruaene and Pollmann memory research into the storybible
**Author approval:** `Verwerk`.

**Status: `DONE_VERIFIED`.**

Evidence:
- `sources/SRC-VAN-BRUAENE-OM-BETERS-WILLE-2008.md` exists.
- `sources/SRC-POLLMANN-MEMORY-EARLY-MODERN-EUROPE-2017.md` exists.
- active master contains `Rederijkers as civic-religious network`, `Memory architecture — Pollmann guardrail`, `Memory carrier`, and Revolt/public-memory guidance.

## 5. Retry missing Leuven Bible provenance
**Author approval:** `Probeer het nog eens`.

**Status: `DONE_VERIFIED`.**

Evidence: `sources/SRC-HIST-CATHOLIC-BIBLE-LOWCOUNTRIES-1548-001.md` exists. The previous sync note that said it was absent became obsolete after the successful retry.

## 6. Process the uploaded general history of the Revolt and correct its attribution
**Author approval:** within the subsequent full processing/synchronisation request.

**Status: `DONE_VERIFIED`.**

Evidence:
- source metadata showed the uploaded work is by S. Groenveld, H.L.Ph. Leeuwenberg, M.E.H.N. Mout and W.M. Zappey, not Judith Pollmann.
- `sources/SRC-GROENVELD-ETAL-TACHTIGJARIGE-OORLOG-2008.md` exists and records the correction.
- local Goes 1577–1578 and Reimerswaal 1574 findings are in the active storybible/history layer.

## 7. Create a historical spine for the full relevant Eighty Years' War / Low Countries transformation through Claes' period
**Author approval:** explicit `Go` after request for all events to be ordered so later scenes can draw from them.

**Earlier status:** assistant incorrectly called the initial scaffolding complete. That claim was false.

**Current status: `DONE_VERIFIED` at the agreed MACRO level.**

Evidence after corrective execution:
- `history/LOW_COUNTRIES_TRANSFORMATION_1540_1605.yaml` is now populated through 1605 with the major political, military, confessional and civic-cultural events relevant to scene conditions.
- `history/LOW_COUNTRIES_TRANSFORMATION_1540_1605.md` contains the same period as a human-readable synthesis.
- `storybible/modules/HISTORICAL_SUBSTRATE_1540_1605.md` now links that non-fiction substrate into storybible use.

Completion definition is explicit: major scene-changing transformations are represented; this is not a promise that every skirmish, ordinance or office-holder has been catalogued.

Remaining work is microhistorical and openly listed: Goes 1572 civilian life; exact Goes 1578 church implementation; Reimerswaal war/flood/demography/trade interaction; annual Zeeland taxation/billeting/provisioning/prices/disease/shipping.

## 8. Build/expand the Zeeland-specific chronology
**Author approval:** included in the full-history request and earlier proposal for a Zeeland regional layer.

**Status: `DONE_WITH_LIMIT`.**

`history/ZEELAND_REVOLT_TIMELINE.yaml` exists, but it is currently less complete than the now-expanded macro timeline. Attempts in the corrective pass to replace it with the expanded regional version, and then to create a lossless extension file, were blocked by the tool safety layer. Therefore this file must **not** be described as fully normalised. All principal Zeeland macro events are present in `history/LOW_COUNTRIES_TRANSFORMATION_1540_1605.yaml`; regional normalization remains a technical follow-up.

## 9. Pollmann — Catholic Identity and the Revolt of the Netherlands, 1520–1635
**Author intent:** recognised as an important next source; historical layer should use it where available.

**Status: `DONE_WITH_LIMIT`, not full-text reviewed.**

The monograph itself was not found in the user's current conversation/library files. Official Oxford/Leiden bibliographic metadata and chapter abstracts were verified instead. `sources/SRC-POLLMANN-CATHOLIC-IDENTITY-2011.md` exists and explicitly records `BIBLIOGRAPHICALLY_VERIFIED / CONTENT_PARTIALLY_VERIFIED_FROM_OFFICIAL_OUP_AND_LEIDEN_METADATA` and forbids representing the work as fully read.

A full chapter-level extraction remains impossible until full text is supplied or otherwise accessible.

## 10. Central Source Claim normalisation
**Status: `DONE_WITH_LIMIT`.**

The older central `claims/SOURCE_CLAIMS.yaml` exists. Goes 1577–1578 local claims are losslessly stored in `claims/SOURCE_CLAIMS_GOES_RELIGION_1577_1578.yaml` because a central-registry rewrite was blocked. Content is preserved; registry normalization remains pending.

## Truth rule established by this audit
From this point, this project must use these terms literally:
- `INTEGRALLY_READ`: complete work read end-to-end.
- `TARGETED_REVIEW`: relevant sections systematically retrieved and analysed.
- `SOURCE_VERIFIED`: concrete source text/locator checked.
- `INFERRED`: defensible extrapolation, identified as such.
- `PROPOSED`: narrative possibility only.
- `DONE`: requested deliverable exists and has been checked.

No future assistant should use `complete`, `everything processed`, `read`, or `done` outside these meanings.
