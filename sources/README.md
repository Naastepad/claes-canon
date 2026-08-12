# Sources

This directory stores full provenance records. Atomic assertions extracted from sources belong in `claims/SOURCE_CLAIMS.yaml`; source records themselves should not be used as substitutes for Story Claims.

## Required source-record fields

Each `SRC-*` record should, where known, include:

- source ID
- source type
- primary / secondary / tertiary
- author / creator
- title
- date
- edition / repository / URL
- exact locator (page, folio, item, archive reference)
- bibliographic status (`complete`, `partial`, `needs_verification`)
- reliability / limitations
- verification date
- verified by
- linked `SC.*` claim IDs

Missing metadata must be marked explicitly rather than invented.

## Direction of authority

`SRC-* -> SC.* -> STC.* -> Narrative Instance / Lemma`

A historical source may support plausibility without proving a fictional event. A verified Source Claim never becomes story canon automatically.