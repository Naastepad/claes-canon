# Claude Project Instructions — Claes Nissepat

Gebruik deze tekst als **Project Instructions** in Claude. De GitHub-repository `Naastepad/claes-canon`, branch `main`, is de enige actuele source of truth voor canon, Storybible, narratieve architectuur, provenance en Lemma-regels.

Gebruik je eigen geheugen, eerdere chats of Project Knowledge nooit als hogere autoriteit dan GitHub.

## Primaire bootstrap

Begin iedere canon-sensitive taak met het ophalen en volledig lezen van:

https://raw.githubusercontent.com/Naastepad/claes-canon/main/AI_ONBOARDING.md

Volg daarna de actuele leesvolgorde en autoriteitshiërarchie uit dat bestand. Gebruik uitsluitend de onderstaande **letterlijke URLs** wanneer je fetch-omgeving geen zelf geconstrueerde of afgeleide GitHub-paden accepteert.

## Altijd toegestane kern-URLs

README:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/README.md

AI onboarding:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/AI_ONBOARDING.md

Repository integrity:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/REPOSITORY_INTEGRITY.md

Authoring policy:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/AUTHORING_POLICY.md

Agent instructions:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/AGENTS.md

Writing protocol:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/WRITING_PROTOCOL.md

Claude repository entrypoint:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/CLAUDE.md

## Canon en synchronisatie

Machine-readable canon decisions:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/canon/DECISIONS.yaml

Open decisions:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/canon/OPEN_DECISIONS.yaml

Latest dated human decisions — 16 Aug 2026:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/canon/DECISIONS_2026-08-16.md

Latest machine-readable dated decisions — 16 Aug 2026:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/canon/DECISIONS_2026-08-16.yaml

Canon directory listing for discovery of additional current decision files:
https://api.github.com/repos/Naastepad/claes-canon/contents/canon?ref=main

Synchronization status:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/review/SYNC_STATUS.md

Migration review:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/MIGRATION_REVIEW.md

## Operating Storybible

Authority manifest:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/storybible/MASTER.md

Operational index:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/storybible/INDEX.md

Current operating master:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/storybible/LEMMA_MCKEE_MASTER.md

Causal chapter projection:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/storybible/STORY_PROJECTION_ROUND_C.md

Mayken dossier:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/storybible/MAYKEN_LAMPERT.md

## Narrative construction

Machine-readable causal projection:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/narrative/story_projection_round_c.yaml

Alchemical authorial architecture:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/narrative/alchemical_authorial_architecture.yaml

Domain scene packs:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/narrative/domain_scene_packs.yaml

Editorial gates:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/narrative/editorial_gates.yaml

Mayken independent arc:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/narrative/mayken_independent_arc.yaml

Claes-Mayken relationship projection:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/narrative/mayken_relationship_projection.yaml

Knowledge states:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/narrative/knowledge_states.yaml

Narrative instances:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/narrative/instances.yaml

Arcs:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/narrative/arcs.yaml

Relationships:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/narrative/relationships.yaml

Motifs:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/narrative/motifs.yaml

Themes and value axes:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/narrative/themes.yaml

## Reader/editorial validation

Reader experience protocol:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/review/READER_EXPERIENCE_PROTOCOL.md

Reader feedback template:
https://raw.githubusercontent.com/Naastepad/claes-canon/main/review/READER_FEEDBACK_TEMPLATE.md

## Rules for Claude

1. GitHub `main` is authoritative. Never substitute Claude memory, older chats or Project Knowledge for current repository state.
2. For canon-sensitive work, load the files required by `AI_ONBOARDING.md`. If your fetch tool refuses a guessed path, use the exact literal URL above; do not invent another path.
3. If a required URL still cannot be fetched, report exactly which file is unavailable and stop canon-sensitive writing or repository conclusions until it is supplied.
4. `OPEN` and `PROPOSED` material may never be silently promoted to `CANON`.
5. Historical evidence, evidence-based reconstruction, authorial fiction and unresolved material remain separate categories.
6. Before writing prose, read `WRITING_PROTOCOL.md`, identify the causal hinge, active Story Claims, knowledge/object state, arcs/relationships, current sinne-state, domain/world guardrails, editorial gate and intended reader movement.
7. Do not expose database IDs or metadata labels in literary prose.
8. Before critique/revision, apply scene necessity and `RETAIN / REVISE / MERGE / CUT` before line editing.
9. If Mayken appears, load her independent arc and relationship projection; never reduce her to Claes' helper or reward.
10. If you can modify GitHub, obey `REPOSITORY_INTEGRITY.md`, `AGENTS.md` and `AUTHORING_POLICY.md`, fresh-fetch every target immediately before mutation and never overwrite concurrent work silently.
11. Lemma is the deterministic rules-as-code layer for temporal, knowledge, encounter, object, prerequisite and consistency checks. It does not decide literary meaning.
12. End substantial work with a concise handoff: files/records read, changes made/proposed, open matters, sync state and validation status.

Fundamentele regel: **GitHub bepaalt wat momenteel waar is. Claude leest, redeneert, analyseert en schrijft vanuit die actuele toestand en onderhoudt geen tweede canon in geheugen of Project Knowledge.**
