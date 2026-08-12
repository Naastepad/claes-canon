# Claes Canon / Storybible

Private, Lemma-focused, McKee/NOS-inspired storybible infrastructure for the historical novel *Claes*.

## What this repository is

This repository is the **project-specific truth and continuity subsystem** for Claes. It combines:

- a human-readable master storybible;
- historical provenance;
- atomic source claims and story claims;
- stable entities;
- narrative instances (scene/chapter/arc/motif);
- explicit canon decisions;
- AI proposals and human review;
- deterministic Lemma constraints;
- automated continuity validation.

Universal narrative theory (McKee, Truby, Coyne, etc.) belongs in a separate Narrative Knowledge Base. This repository stores the concrete Claes instances to which those Knowledge Objects may later be applied.

## Core flow

```text
Historical sources
      ↓
Source Claims (SC.*)
      ↓
Story Claims (STC.*) ← Canon Decisions (DEC.*)
      ↓                         ↓
MASTER storybible ↔ Narrative Instances (NI.*, ARC.*, MOTIF.*)
      ↓
Deterministic subset
      ↓
Lemma
      ↓
Consistency engine
```

## Two status axes

Historical evidence and story truth are deliberately separate.

**Evidence:** `VERIFIED / SUPPORTED / PLAUSIBLE / DISPUTED / UNKNOWN`

**Canon:** `PROPOSED / CANON / OPEN / DEPRECATED / REJECTED`

A fictional encounter can therefore be `PLAUSIBLE + CANON`. A verified historical fact is not automatically story canon.

## Repository layout

- `storybible/MASTER.md` — logical single narrative authority; currently contains the controlled import manifest for the latest complete external master.
- `claims/SOURCE_CLAIMS.yaml` — atomic claims extracted from historical/research sources.
- `claims/STORY_CLAIMS.yaml` — atomic truths/candidates inside Claes.
- `claims/DECISIONS.yaml` — explicit canon and architecture decisions.
- `entities/ENTITIES.yaml` — stable identities for people, locations, objects, texts and organizations.
- `narrative/` — concrete Narrative Instances, arcs and motifs.
- `sources/` — detailed provenance records.
- `proposals/` — reviewable AI/human change proposals.
- `lemma/` — executable deterministic constraints only.
- `scripts/validate_canon.py` — repository-level continuity compiler.
- `.github/workflows/` — Lemma validation and structured-canon validation.

## AI authoring rule

AI may extract, compare, propose, structure and test. AI may not silently promote a claim to canon or publish to LemmaBase. Every change must remain traceable from source/evidence through story claim and decision to any resulting Lemma rule.

See `ARCHITECTURE.md`, `AUTHORING_POLICY.md` and `SCHEMA.md`.