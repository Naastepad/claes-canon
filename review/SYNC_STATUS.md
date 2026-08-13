# Synchronization status

Status: `SYNC_PENDING`

The explicit author decisions of 13 August 2026 remain propagated through the active operating model. The Catholic Scripture/liturgy layer, Wendy Wauters sensory-religious-space module, Pollmann memory layer, Van Bruaene rederijker layer and the new Goes 1577–1578 local religious-transition module are now present on `authoring/v1`.

Synchronized authority chain for the 13-Aug-2026 canon decisions:
- `canon/DECISIONS_2026-08-13.md`
- `canon/DECISIONS.yaml`
- `claims/STORY_CLAIMS.yaml`
- `entities/ENTITIES.yaml`
- `narrative/arcs.yaml`
- `narrative/themes.yaml`
- `narrative/sinne_recovery.yaml`
- `narrative/beloved_recovery.yaml`
- `narrative/religious_space_sensory_church.yaml`
- `storybible/LEMMA_MCKEE_MASTER_2026-08-13.md`

## Religious and sensory research now integrated
- `sources/SRC-WAUTERS-RELIGIOUS-SPACE-2021.md` — sensory church, period *sinne*, church as social/corporate/memory space, Antwerp → Goes/Reimerswaal transferability guardrails.
- `sources/SRC-HIST-CATHOLIC-BIBLE-LOWCOUNTRIES-1548-001.md` — Leuven Bible 1548, Latin/Vulgate norm, Liesvelt comparison and reprint history.
- `sources/SRC-POLLMANN-MEMORY-EARLY-MODERN-EUROPE-2017.md` — material/social memory, violence, silence, changing public memory.
- `sources/SRC-VAN-BRUAENE-OM-BETERS-WILLE-2008.md` — rederijkers as civic-religious communication networks, lay devotion, competition and confessional debate.
- `sources/SRC-GROENVELD-ETAL-TACHTIGJARIGE-OORLOG-2008.md` — local and regional Revolt chronology. The uploaded EPUB filename misattributed this work to Judith Pollmann; the EPUB metadata identifies S. Groenveld, H.L.Ph. Leeuwenberg, M.E.H.N. Mout and W.M. Zappey.

## Goes / Reimerswaal chronology added
- `claims/SOURCE_CLAIMS_GOES_RELIGION_1577_1578.yaml` — local source-claim extension.
- `storybible/modules/GOES_RELIGIOUS_TRANSITION_1577_1578.md` — active historical worldbuilding module.

Local anchors now supported:
1. **March 1577:** Goes, the last royalist town in Zeeland, concludes a satisfactie with William of Orange; Catholicism remains the only permitted religion under the settlement.
2. **1578:** during radicalisation, Reformed/Calvinist preaching is introduced under pressure in Holland and Zeeland satisfactie towns. Goes belongs to this class; the March 1577 Catholic-only settlement must therefore not be projected unchanged through 1578.
3. **July 1578:** Orange's proposal for religious peace demonstrates that coexistence, monopoly and public worship remained actively contested.
4. **January 1574:** rebel forces defeat a Habsburg/Spanish fleet near Reimerswaal, contributing to Middelburg's surrender the following month. Use as Delta/waterway-war context, not as proof of street fighting inside Reimerswaal.

## Remaining pending items
1. A dedicated provenance file for Judith Pollmann's *Catholic Identity and the Revolt of the Netherlands, 1520–1635* is still absent. The existing Source Claim that cites that title therefore remains formally incomplete until the work itself or a stable bibliographic source is supplied/verified.
2. The Goes 1577–1578 chronology is now substantially narrowed, but exact local implementation remains open: exact day of first Reformed preaching, first church building used, named local activists/preachers, altar/image-removal sequence, clergy responses and household/private Catholic practice require Goes-specific archival or specialist evidence.
3. `claims/SOURCE_CLAIMS.yaml` still holds the older general registry; the new local claims are currently stored in the explicit extension file because a full-registry rewrite was blocked during this pass. This is loss-preserving and visible, but a later normalization pass should merge the extension into the primary registry.
4. Branch reconciliation with current `main` and CI verification remain release/PR tasks.

Legacy/audit note:
- `storybible/LEMMA_MCKEE_MASTER.md` remains the earlier transformed work edition and is not the active operating master.
- Additive extension records are preferred over silent rewriting when connector safety or concurrent-edit risk prevents a clean atomic normalization.
