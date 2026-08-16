# Canon conflict audit — 16 August 2026

**Status:** RESOLVED_FOR_ACTIVE_LAYERS  
**Scope:** current `main` synchronization pass after no-cipher Brevísima, Seton separation, alchemical refinement, Cornelis rederijker correction and Mayken callback recovery.

This audit distinguishes genuine unresolved story decisions from stale registry/master conflicts.

## Resolved in this pass

### 1. Claes birth: 1545 vs 1542

**Conflict:** legacy Lemma/McKee prose still used 1545.  
**Resolution:** **8 December 1542** is current canon under `DEC.CLAES.BIRTH.2026-08-13`. `LEMMA_MCKEE_MASTER.md` is regenerated; the dated 13 August master is legacy/audit only.

### 2. Cipher/recovery architecture vs direct chemical reveal

**Conflict:** legacy prose still described post-4-October loading, 24 merels problems, Monas/matrix/Castanea/Dodoens/Primus/nomenclator and multi-week decryption.  
**Resolution:** `DEC.MEMORIAAL.DIRECT_TEXT_NO_CIPHER.2026-08-15` governs. The readable Diets/Brabant text is printed nearly invisibly before binding and later revealed directly by green vitriol. Reveal is reading, not decryption. Retired puzzle components may survive independently only where they have another function.

### 3. Cornelis death open vs exact death canon

**Conflict:** `OPEN.CORNELIS.DEATH.001`, generic entity windows and base working claim still suggested exact details were open, while execution-specific canon fixed them.  
**Resolution:** exact current story state is **Antwerp, 19 November 1569**, after autumn-1567 first arrest/examination and renewed exposure; Claes witnesses. `DEC.CORNELIS.DEATH.1569.2026-08-15.REVISED` explicitly supersedes the stale working state. The open record is removed from the active backlog.

### 4. Cornelis as Castanienbloem member vs historical chronology

**Conflict:** 15 August shorthand made Cornelis a straightforward member of De Edele Castanienbloem, while historical evidence only attests that chamber from 1595 and other files left chamber identity open.  
**Resolution:** `DEC.CORNELIS.REDERIJKER.NARDUS_CASTANIE_ORIGIN.2026-08-16` governs. Cornelis is a **Nardusbloem / older Magdalena-linked** member. In novel canon he plays a formative role in a reform-minded/protestantiserende 1560s current that later becomes the Edele Castanienbloem. The early Castanien origin is explicit fiction; 1595 is the earliest surviving attestation, not a proved founding date. Deken status remains open.

### 5. Beloved identity open vs Mayken decision

**Conflict:** `OPEN.CLAES.BELOVED.IDENTITY.001` and generic entity state remained open while an earlier author-approved branch had fixed Mayken.  
**Resolution:** callback-recovered and synchronized as **Mayken Adriaensdr. Lampert**, fictional, ca.1546, grounded in the Goese Lampart/Lambert/Lampert apothecary milieu. The active open record is removed.

### 6. Mayken old recovery function vs no-cipher canon

**Conflict:** the older Mayken branch made her materially important to Dodoens/recovery mechanics that were later retired.  
**Resolution:** her identity, fire background, apothecary expertise and relationship function are retained. She may assist material reveal, reading, observation and error control but is **not** a cipher/nomenclator/special-Dodoens key-holder.

### 7. Green Lion semantic overstatement

**Conflict:** broad wording risked equating Groene Leeuw universally with FeSO4 and conflating text reveal with direct dissolution of Sol.  
**Resolution:** Groene Leeuw is an **operational process name** in Dee/Claes' working vocabulary. Green vitriol directly develops the tannin text; it does not directly dissolve gold. The Sol line requires strong-water failure before the right compound opening relation.

### 8. Sol continuity / apparent transmutation

**Conflict:** the older process chain could be read as allowing creation of gold from lead or an untracked late gold addition.  
**Resolution:** material conservation is explicit. The Sol visible in the late assay was already present. Rode Leeuw carries already-present Sol. The exact non-gold carrier matrix remains open.

### 9. Enkhuizen 1602 overbroad open state

**Conflict:** broad open record still treated date/place/frame as undecided.  
**Resolution:** chosen story frame fixed from Morhof's retrospective tradition: **Enkhuizen, house of Jacob Hausfsen, 13 March 1602, ca.16:00, Seton/Sidonius**. What remains open is assay/furnace choreography, quantities, additional witnesses, public/private degree and immediate aftermath.

### 10. SYNC_PENDING after PR #9 merge

**Conflict:** old sync documentation still treated the no-cipher integration as an unmerged authoring branch.  
**Resolution:** current `main` already contains the no-cipher integration. `review/SYNC_STATUS.md` is regenerated in this pass.

### 11. “Two brothers” continuity bug

**Conflict:** `narrative/arcs.yaml` referred to an intact household with “two brothers and an expected child”.  
**Resolution:** corrected to Claes + one younger brother **Jan** + expected unborn child.

### 12. Silvius as translator / Dee as code architect

**Conflict:** generic entity roles overstated functions no longer fixed by canon.  
**Resolution:** Silvius remains printer/publisher/editor; initial translator identity remains open. Dee remains scholar/mentor with material and cryptographic expertise but is not required as architect of a Brevísima cipher that no longer exists.

## Intentionally unresolved after this pass

These are genuine open questions, not synchronization errors:

- Claes' exact death circumstances/place/cause;
- 1564 Spanish→Diets translator/source route;
- wet/press validation of tannin/gum printing;
- exact graphite-stift physical form/provenance;
- exact Fabritius→Cornelis low-level link;
- Zovitius 1570 delivery route;
- exact 1570→1578 publication/transmission route;
- 1564 chapter calendar audit;
- final merels opponent/stakes/action;
- whether Cornelis ever serves as deken;
- Rode Leeuw non-gold carrier composition;
- exact Enkhuizen assay/furnace choreography and additional witnesses;
- optional authoring choices such as Radermacher and the bakery scene.

## Not conflicts, but underdeveloped

The following must not be mislabeled as “open canon”:

- Book/Act/Sequence/Chapter/Beat hierarchy in `narrative/structure.yaml` is still largely unpopulated.
- Scene-level objective/conflict/value/turning-point diagnostics exist for only a small part of the novel.
- Mayken now has a stable identity and function, but her own scene-by-scene desire, choices and conflict still need development.
- The 1578 publication endpoint is fixed, but its dramatic production/transmission sequence remains to be designed.
- 1584–1602 requires finer causal scene architecture.
- Goes' world model is rich; the remaining work is converting it into time-sliced dramatic geography rather than accumulating locations.

## Registry rule going forward

`canon/OPEN_DECISIONS.yaml` must contain only records with genuinely unresolved `status: OPEN`. Resolved/superseded/not-applicable history belongs in decisions, audit logs or dated migration files.

A future AI/writer must distinguish:

1. **research open** — evidence may close it;
2. **experimental open** — material testing may close it;
3. **authorial design open** — only an explicit novel choice closes it;
4. **irreducible historical uncertainty** — preserve uncertainty and mark any story choice as reconstruction/fiction.
