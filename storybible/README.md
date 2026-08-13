# Storybible

This directory anchors the human-readable authority of the Claes project. Revision 11 has now been converted into a structured operating storybible rather than being represented by one monolithic prose file alone.

`MASTER.md` defines precedence and points to the exact lossless source edition by SHA-256. `INDEX.md` navigates the structured projection.

The full 3803-line source edition is preserved as the semantic source for anything not yet atomized. Its 31 top-level sections are all accounted for in `../mapping/CONVERSION_LEDGER.yaml`, including source line ranges and section hashes.

Structured canon is distributed across `claims/`, `entities/`, `objects/`, `narrative/`, `canon/` and `lemma/` according to responsibility. This is intentional: the storybible is now a system, not a single oversized file.

If the structured projection and the source prose appear to differ, do not silently pick one. Create a proposal, inspect provenance and resolve the discrepancy by explicit human decision.
