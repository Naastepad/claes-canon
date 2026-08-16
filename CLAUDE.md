# Claude instructions — Claes

This is a thin model-specific entrypoint. The canonical cross-model instructions live in `AI_ONBOARDING.md`.

For Claude Projects or restricted `web_fetch` environments, use the literal-URL bootstrap in:

`prompts/CLAUDE_PROJECT_INSTRUCTIONS.md`

That file is designed to be copied into Claude Project Instructions so the required GitHub URLs are present literally in the project context instead of being guessed from repository paths.

Before answering canon-sensitive questions or editing this repository, read in this order:

1. `AI_ONBOARDING.md`
2. current `canon/` decisions and `review/SYNC_STATUS.md`
3. `storybible/MASTER.md` and `storybible/INDEX.md`
4. `storybible/LEMMA_MCKEE_MASTER.md`
5. the relevant structured records and governing dossiers
6. `WRITING_PROTOCOL.md` if drafting/revising literary prose
7. `AUTHORING_POLICY.md`, `AGENTS.md` and `REPOSITORY_INTEGRITY.md` if changing canon, schemas or Lemma

Do not substitute conversation memory or Project Knowledge for repository truth. Preserve the distinction between historical evidence (`SC.*`), novel truth (`STC.*`), narrative instances (`NI.*`) and deterministic Lemma constraints.

Never silently promote `OPEN` or `PROPOSED` material to `CANON`. Never invent precision that the Storybible does not contain.

If writing prose, obey the current chapter/scene construction rules in `AI_ONBOARDING.md` and `WRITING_PROTOCOL.md`: identify the causal hinge, POV, story-time window, active claims, knowledge/object state, values, pressure/turn, arcs/relationships/motifs, relevant domain/world pack, reader movement and open decisions that must remain open. Then write literary text without embedding metadata labels into the prose.

If Claude's fetch tool refuses a repository path that is not already literal in the conversation/project context, do not guess or conclude that the file is absent. Use the exact URLs supplied in `prompts/CLAUDE_PROJECT_INSTRUCTIONS.md`; if a required URL is still unavailable, report the missing file and stop canon-sensitive work until it is supplied.

At the end of substantial work, leave a concise handoff stating records consulted, changes proposed/made, unresolved decisions and validation status.
