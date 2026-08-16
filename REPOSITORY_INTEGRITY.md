# Repository Integrity Contract

This file is mandatory for every AI or automation with write access to `claes-canon`.

## Why this exists
Multiple ChatGPT sessions, Claude/Claude Code, Copilot or other agents may read and write the same repository. Git history prevents data loss only if writers behave conservatively. Canon integrity therefore requires an explicit concurrency protocol.

A reported write action, connector success response or absence/presence of CI checks is **not itself proof that intended repository state is persistent and reachable on the target branch**. Persistence must be verified positively from GitHub after mutation.

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
10. **Validation is necessary, not sovereign.** Green CI means structural checks passed; it does not make an unapproved claim canon. Missing, empty or unavailable CI/status-check results mean only that CI validation was not observed through that channel. They prove neither write success nor write failure.
11. **Positive post-write verification is mandatory.** Before claiming that a repository write is complete, re-fetch the target branch from GitHub and verify that the resulting commit is the branch head or an ancestor of it as appropriate. Re-fetch every file created or updated and confirm the expected semantic marker/content is present. For deletion, verify that the path is absent. A connector/API `success`, returned commit SHA or local state alone is insufficient.
12. **Separate persistence from validation.** Report write persistence and CI/validator state independently. Use language equivalent to `WRITE_VERIFIED` only after positive remote read-back. Use `CI_VERIFIED`, `CI_FAILED` or `CI_NOT_OBSERVED` separately; never collapse these axes into one vague "done" signal.
13. **No false completion from stale read-back.** A read made before the final write does not count as post-write verification. The verification fetch must occur after the last mutation that could affect the claimed end state.
14. **Preserve history.** No force push, destructive branch move, deletion of decision history, or rewriting of provenance without explicit human instruction.
15. **Handoff.** Substantial writes must leave a concise repository-visible record or updated sync/review status.

## Required post-write verification sequence
For any synchronization or canon write pass:

1. perform the intended mutations;
2. fetch the target branch head **after the final mutation**;
3. verify the expected commit chain/ancestry or current head;
4. re-fetch each touched file from the target branch and inspect at least the exact section/identifier/semantic marker that was meant to change;
5. verify deleted paths are actually absent when deletion was intended;
6. inspect validators/CI separately where relevant;
7. only then issue an end-state statement.

If any of steps 2–5 cannot be completed, the correct persistence status is **`WRITE_UNVERIFIED`**, not `SYNC_COMPLETE`, even if the mutation tool returned success.

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
After a synchronization task, report **two independent axes**.

Persistence:
- `WRITE_VERIFIED` — branch/commit state and affected remote files were positively re-read after the final write;
- `WRITE_UNVERIFIED` — mutation may have been attempted but positive remote persistence was not established;
- `CONFLICT` — branch/file state changed incompatibly and human resolution is required.

Semantic synchronization:
- `SYNC_COMPLETE` — all known downstream representations updated and positively read back;
- `SYNC_PENDING` — list exact remaining files/records and why;
- `CONFLICT` — human decision required.

Validation/CI:
- `CI_VERIFIED` — relevant validator/status evidence was observed and passed;
- `CI_FAILED` — relevant validator/status evidence was observed and failed;
- `CI_NOT_OBSERVED` — no relevant CI/status evidence was available through the checked channel.

A valid final report may therefore be, for example: `WRITE_VERIFIED / SYNC_COMPLETE / CI_NOT_OBSERVED`. This is materially stronger and more precise than saying merely that a write "succeeded" or that "no CI statuses were returned".
