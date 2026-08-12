# Claes Canon / Storybible — AI Gateway

This `main` branch is the stable public entry point for humans and AI systems. The active Lemma-focused, McKee/NOS-inspired Storybible is currently being reviewed on branch **`authoring/v1`** in draft PR #1.

## If you are an AI assistant

Do **not** infer the project from this README alone. Read the canonical onboarding instructions and the operating Storybible before making canon-sensitive statements or drafting prose.

### Essential files

1. AI onboarding — how to interpret evidence, canon, Narrative Instances and Lemma:
   - GitHub: https://github.com/Naastepad/claes-canon/blob/main/AI_ONBOARDING.md
   - raw: https://raw.githubusercontent.com/Naastepad/claes-canon/main/AI_ONBOARDING.md

2. Writing protocol — mandatory if you draft, rewrite or critique Claes prose:
   - GitHub: https://github.com/Naastepad/claes-canon/blob/main/WRITING_PROTOCOL.md
   - raw: https://raw.githubusercontent.com/Naastepad/claes-canon/main/WRITING_PROTOCOL.md

3. Current transformed operating Storybible (`authoring/v1`):
   - GitHub: https://github.com/Naastepad/claes-canon/blob/authoring/v1/storybible/LEMMA_MCKEE_MASTER.md
   - raw: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/storybible/LEMMA_MCKEE_MASTER.md

4. Full authoring instructions (`authoring/v1`):
   - GitHub: https://github.com/Naastepad/claes-canon/blob/authoring/v1/AGENTS.md
   - raw: https://raw.githubusercontent.com/Naastepad/claes-canon/authoring/v1/AGENTS.md

5. Draft PR describing the conversion:
   - https://github.com/Naastepad/claes-canon/pull/1

## Claude Chat / restricted web-fetch environments

Some chat environments cannot freely follow links discovered inside a fetched GitHub page. If that applies to you, ask the user to paste one of the **exact URLs above** into the conversation, preferably the `raw.githubusercontent.com` URL. Do not claim repository content is unavailable until that direct URL has been tried.

For deep repository work requiring arbitrary file traversal, clone/search or commits, use an environment with repository access such as Claude Code, ChatGPT with the GitHub connector, GitHub Copilot/Coding Agent, or a local git checkout.

## Project model

The repository separates four responsibilities:

1. **Evidence** — historical/research support (`SRC-*`, `SC.*`).
2. **Story truth** — what is true inside the novel (`STC.*`, `DEC.*`).
3. **Narrative meaning** — how truth becomes scene, sequence, arc, motif, relationship and value movement (`NI.*`, `ARC.*`, `REL.*`, `MOTIF.*`, `THEME.*`, `VALUE.*`, `WORLD.*`, `CODE.*`).
4. **Deterministic continuity** — only what usefully belongs in executable Lemma rules (`lemma/*.lemma`).

External McKee/NOS knowledge objects (`KO.*`) are narrative theory, not Claes canon.

## Canon rule

Evidence status and canon status are independent. `PROPOSED` or `OPEN` material must never silently become `CANON`. AI may read, analyse, propose, structure, test and draft; canon-changing choices require explicit human approval.

## Current development status

The transformed Storybible is still on `authoring/v1`. `main` intentionally exposes these gateway instructions without prematurely merging the draft canon architecture.