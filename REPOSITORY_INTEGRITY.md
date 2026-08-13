# Repository Integrity Contract

This file is mandatory for every AI or automation with write access to `claes-canon`.

## Why this exists
Multiple ChatGPT sessions, Claude/Claude Code, Copilot or other agents may read and write the same repository. Git history prevents data loss only if writers behave conservatively. Canon integrity therefore requires an explicit concurrency protocol.

## Non-negotiable rules
1. **Freshness before mutation.** Fetch the current branch head and the current version/SHA of every target file immediately before a write.
2. **No memory writes.** Never replace a repository file using a copy remembered from chat or an earlier fetch if the file may have changed.
3. **No silent last-writer-wins.** If a target changed since analysis began, re-read and reconcile. Do not overwrite the newer version merely to apply your earlier plan.
4. **Authoring branch first.** Canon development belongs on an authoring branch/PR. `main` is a stable gateway/release surface unless the human explicitly directs otherwise.
5. **Human decisions outrank transforms.** Files in `canon/` are authoritative corrections/decisions and must be propagated downstream.
6. **Atomic semantic synchronization.** A decision should update all affected structured representations together. If technical limitations prevent this, create/update `review/SYNC_STATUS.yaml` and mark every unsynchronized path explicitly.
7. **Stable identity.** Never recycle IDs. Deprecate rather than repurpose.
8. **Uncertainty is data.** Preserve OPEN/PROPOSED/precision windows. Never resolve them by plausibility alone.
9. **No autonomous promotion.** AI may propose and synchronize approved decisions; it may not merge, publish to LemmaBase, or convert a proposal/open question into CANON without explicit human authority.
10. **Validation is necessary, not sovereign.** Green CI means structural checks passed; it does not make an unapproved claim canon.
11. **Preserve history.** No force push, destructive branch move, deletion of decision history, or rewriting of provenance without explicit human instruction.
12. **Handoff.** Substantial writes must leave a concise repository-visible record or updated sync/review status.

## Canon synchronization dependency order
`canon decision → STC → ENT/OBJ/knowledge → NI/ARC/REL/MOTIF/THEME/VALUE → operating master → Lemma → validators/review`

When an upstream node changes, every downstream node is suspect until checked.

## Collision protocol
If another writer changes the same area while you work:
- stop the affected write;
- fetch the new head/content;
- identify whether changes are compatible, competing, or independent;
- preserve both if uncertain;
- create a proposal/conflict record rather than choosing silently;
- tell the human what needs resolution.

## Required end-state statement
After a synchronization task, report one of:
- `SYNC_COMPLETE` — all known downstream representations updated and validation checked;
- `SYNC_PENDING` — list exact remaining files/records and why;
- `CONFLICT` — human decision required.
