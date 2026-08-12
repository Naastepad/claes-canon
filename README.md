# Claes Canon

Private authoring repository for the formal canon of the Claes project.

## Purpose

This repository is the editable work layer between historical/source material, AI-assisted canon authoring, and the published LemmaBase repository `@naastepad/claes`.

The workflow is deliberately asymmetric:

1. Sources and the master storybible provide evidence and narrative context.
2. AI may analyse them and propose structured canon changes.
3. Proposed changes are written and reviewed in GitHub.
4. Lemma files are validated before acceptance.
5. A human approves the change.
6. Only approved rules are published to LemmaBase.
7. LemmaBase MCP remains the read-only execution layer for AI.

AI-generated material must never become canon merely because it is plausible.

## Epistemic states

- `FACT` — externally supported historical fact.
- `CANON` — explicitly established truth inside the novel.
- `HYPOTHESIS` — plausible reconstruction that has not been promoted to canon.
- `DISPUTED` — conflicting evidence or interpretation.
- `UNKNOWN` — deliberately unresolved.

## Canon v1 scope

The first version models only constraints that are useful for deterministic consistency checks:

- time
- place
- knowledge
- possession
- encounters
- clue dependencies

Long prose, biographies, quotations, source scans and narrative notes belong in the storybible or source registry, not in Lemma.

## Repository layout

- `lemma/` — executable Lemma specs.
- `storybible/` — canonical narrative source material or pointers to it.
- `sources/` — provenance and source registry.
- `proposals/` — AI-authored change proposals awaiting review.
- `.github/` — review and contribution controls.

See `AUTHORING_POLICY.md` for the acceptance workflow and `SCHEMA.md` for the data model.