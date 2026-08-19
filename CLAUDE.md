# Claude instructions — Claes

This is a thin model-specific entrypoint. The canonical cross-model instructions live in `AI_ONBOARDING.md`.

For Claude Projects or restricted `web_fetch` environments, use the literal-URL bootstrap in:

`prompts/CLAUDE_PROJECT_INSTRUCTIONS.md`

That file is designed to be copied into Claude Project Instructions.

## Primary Claude entrypoint

For every canon-sensitive task, Claude must first fetch and obey:

`prompts/CLAUDE_CONTEXT_INDEX.md`

Literal URL:

https://raw.githubusercontent.com/Naastepad/claes-canon/main/prompts/CLAUDE_CONTEXT_INDEX.md

This generated file is not merely an index. It is the **task router** that assigns the exact context packs required for canon questions, character work, scene/chapter writing, hard revision, Mayken work and repository mutation.

**Do not begin by browsing repository directories or keyword-searching for relevant canon.** Load the router-assigned packs first. Additional files may then be fetched only when the loaded `MASTER`, `INDEX`, decision/claim or governing dossier explicitly names them, unless the user explicitly requests repository-wide discovery/audit.

The reason is continuity: free repository discovery can surface a technically relevant but stale, partial or lower-authority file before the current governing layer. Task routing must determine the reading set; discovery is only a fallback.

## Authority

Within the loaded packs, follow `AI_ONBOARDING.md` and its authority hierarchy. In particular:

1. latest applicable explicit `DEC.*` decisions;
2. active synchronized `STC.*` Story Claims;
3. current governing dossiers / structured state;
4. current operating master;
5. lower-authority evidence, proposals, opens and legacy material.

Do not substitute conversation memory or Project Knowledge for repository truth. Preserve the distinction between historical evidence (`SC.*`), novel truth (`STC.*`), narrative instances (`NI.*`) and deterministic Lemma constraints.

Never silently promote `OPEN` or `PROPOSED` material to `CANON`. Never invent precision that the Storybible does not contain.

## Character work

Any task about a recurring named character, relationship, motivation, archetype or characterization must load the router's `06_CHARACTER_WEB` pack in addition to core canon and dated decisions.

Archetypal labels are author-side lenses, not complete personalities. Use the concrete characterization layer: governing value, strength, shadow, contradiction, habitual expression, independent agency and relationship-specific state.

If Mayken appears, also load `04_MAYKEN_KNOWLEDGE`.

## Prose / revision

If writing prose, obey the task router plus `AI_ONBOARDING.md` and `WRITING_PROTOCOL.md`: identify the causal hinge, POV, story-time window, active claims, knowledge/object state, character web, arcs/relationships/motifs, relevant domain/world pack, reader movement and open decisions that must remain open. Then write literary text without embedding metadata labels into the prose.

If revising or critiquing, determine `RETAIN / REVISE / MERGE / CUT` before line-polishing.

## Access failures

If Claude's fetch tool refuses a required literal pack URL, do not replace the missing pack with memory or improvised repository discovery. Report the exact failed URL and stop canon-sensitive conclusions until the required pack is available.

If a pack is truncated, report the last visible `SOURCE FILE` heading and do not pretend the remainder was read.

At the end of substantial work, leave a concise handoff stating packs/governing records consulted, changes proposed/made, unresolved decisions, sync state and validation status.
