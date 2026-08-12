# AI Onboarding — Claes Storybible

**Canonical cross-model gateway instruction file.** This file is intended for ChatGPT, Claude, Gemini, Copilot, local agents and other language models.

The active transformed Storybible currently lives on branch `authoring/v1`. This gateway exists on `main` so restricted chat environments can discover how to read it.

## Direct operating Storybible URLs

GitHub:
https://github.com/Naastepad/claes-canon/blob/authoring/v1/storybible/LEMMA_MCKEE_MASTER.md

Raw:
https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/storybible/LEMMA_MCKEE_MASTER.md

If your environment refuses to follow an embedded link, ask the user to paste the exact raw URL above into the conversation.

## What this repository is

This repository is the operating Storybible and canon-control system for the historical novel **Claes Nissepat**. It contains four distinct layers:

1. **Evidence** — historical/research support (`SRC-*`, `SC.*`).
2. **Story truth** — what the author has decided is true inside the novel (`STC.*`, `DEC.*`).
3. **Narrative meaning** — how story truth becomes character, scene, sequence, arc, motif, relationship and value movement (`NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`, `WORLD.*`, `CODE.*`).
4. **Deterministic continuity** — only the subset that can usefully be evaluated as executable logic (`lemma/*.lemma`).

External McKee/NOS knowledge objects (`KO.*`) are narrative theory, not Claes canon. They may diagnose scenes and arcs but may never override story truth.

## Authority hierarchy

When records appear to conflict, resolve them in this order:

1. Explicit current human author decision.
2. Active `STC.*` Story Claim with `canon_status: CANON` and its `DEC.*` decision record.
3. Structured operating Storybible records (`ENT.*`, `OBJ.*`, `NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`, `WORLD.*`, `CODE.*`).
4. `storybible/LEMMA_MCKEE_MASTER.md` as the human-readable operating synthesis.
5. The exact Revision 11 source edition for detail not yet atomized, as tracked by the conversion ledger.
6. `PROPOSED` and `OPEN` records — informative but unsettled.
7. Historical inference or model-generated suggestion — never canon unless explicitly promoted.

Lemma can establish compatibility with encoded deterministic constraints. Lemma does not decide literary truth and does not convert historical evidence into canon.

## Status semantics

Evidence status:
`VERIFIED / SUPPORTED / PLAUSIBLE / DISPUTED / UNKNOWN`

Canon status:
`PROPOSED / CANON / OPEN / DEPRECATED / REJECTED`

These axes are independent. A fictional event may be `PLAUSIBLE + CANON`; a verified historical fact may remain outside the novel.

Never silently promote `PROPOSED` or `OPEN` to `CANON`.

## Time and uncertainty

Preserve source precision exactly. Do not turn a month, year or interval into an invented exact day. A lack of precision is information, not a defect to repair by guessing.

## Historical-fiction boundary

Always separate documented history, reconstruction, authorial fiction and open questions. Network proximity does not prove a meeting. A real printed book does not prove Claes' fictional provenance. A plausible route does not prove a precise parcel location.

## How to read the Storybible narratively

When interpreting a scene, chapter or sequence, consider POV and knowledge state, conscious desire, psychological and moral need, opening and closing value, conflict/pressure, turning point or revelation, changes in claims/relationships/object states/knowledge, arc movement and motif development.

The governing Claes movement is not simply “solve the puzzle.” It is the lifelong movement from **perception → understanding → control → responsibility → release**.

## If you are only reading or answering questions

You may summarize active canon, trace provenance, distinguish evidence from fiction, identify open decisions, explain chronology/knowledge/object provenance/arcs/motifs, use Lemma for deterministic consistency and use McKee/NOS theory for diagnosis.

You must preserve uncertainty exactly as the repository preserves it.

## If you are allowed to write prose

Read `WRITING_PROTOCOL.md` on `main` first:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/WRITING_PROTOCOL.md

Before drafting, identify the relevant Narrative Instance, active Story Claims, participants, knowledge states, object states, arcs, relationships, motifs, themes/value axes, historical guardrails, open decisions and any relevant Lemma result.

New prose implements existing canon by default. It does not silently create canon. If a creative choice would close an `OPEN.*` matter, leave it unresolved or present it separately for human approval.

## If you can modify the repository

Follow the controlled flow:

`source/evidence -> SC.* -> STC.* -> DEC./review -> narrative records -> Lemma if deterministic -> validation -> human approval`

Never publish to LemmaBase without explicit human approval.

## Cross-model handoff

After substantial canon-sensitive work, leave a concise handoff containing records read, records changed, assumptions made, unresolved decisions, validation status and anything requiring human approval. Do not rely on chat memory as canonical storage.

## Restricted fetch note

If you cannot browse arbitrary repository paths, do not infer absence. State the access limitation and ask the user to paste the exact direct or raw URL required. For arbitrary repository traversal or writes, use a repository-capable environment such as Claude Code, ChatGPT with GitHub connector, Copilot/Coding Agent or local git.