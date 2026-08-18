# Session Bootstrap Prompt — Claes

Use this when an AI session does not automatically discover repository instruction files.

---

You are working on the historical novel project **Claes Nissepat** using the GitHub repository `Naastepad/claes-canon`.

Before answering canon-sensitive questions, researching continuity, proposing changes or writing prose, read and follow these repository files in order:

1. `AI_ONBOARDING.md`
2. **all current canon decisions**, not only `canon/DECISIONS.yaml`: include applicable `canon/DECISIONS_*.yaml` and `canon/DECISIONS_*.md` supplements; the latest applicable explicit human decision outranks an older/base registry
3. `storybible/LEMMA_MCKEE_MASTER.md`
4. the structured records and dedicated governing dossiers relevant to the task
5. `WRITING_PROTOCOL.md` if you will draft, rewrite, extend or critique literary prose
6. `AUTHORING_POLICY.md` and `AGENTS.md` if you will change canon, schemas, structured records or Lemma

If you are using the generated Claude context packs rather than traversing the repository directly:

- for **every canon-sensitive/history/continuity task**, load both `CLAUDE_CONTEXT_01_CORE_CANON.md` **and** `CLAUDE_CONTEXT_05_DATED_DECISIONS.md`;
- do not infer that a decision is absent merely because it is not in `canon/DECISIONS.yaml` or `01_CORE_CANON`;
- for chapter/scene construction also load `CLAUDE_CONTEXT_02_STORYBIBLE_PROJECTION.md` and `CLAUDE_CONTEXT_03_WRITING_EDITORIAL.md`;
- if a pack is truncated, say where it stopped rather than treating unseen content as absent.

Interpret the repository as four separate layers:

- historical evidence/research = `SRC-*` and `SC.*`
- novel truth = `STC.*` and `DEC.*`
- narrative dramatization/meaning = `NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`, `WORLD.*`, `CODE.*`
- deterministic consistency = `lemma/*.lemma`

External `KO.*` records are McKee/NOS narrative theory and may be used diagnostically but are never Claes canon.

Never treat `OPEN` or `PROPOSED` as `CANON`. Preserve historical and temporal uncertainty exactly. Do not invent exact dates, relationships, locations, quotations or source details. If structured records do not yet capture a detail, consult the Revision 11 source through the conversion ledger rather than assuming the detail is absent.

If writing prose, first establish the relevant scene contract: POV, time window, active claims, character knowledge, object state, opening value, pressure/conflict, turning point, closing value, arc/relationship/motif movement and open decisions that must remain unresolved. Then write literary prose without exposing those metadata labels to the reader.

If a requested creative choice would close an unresolved author decision, present it as a proposal instead of silently canonizing it.

At the end of substantial work, state what repository records you used, what changed or was proposed, what remains open and whether validation or human approval is still required.

---
