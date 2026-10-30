---
name: bounded-implementation
description: Implement a narrowly scoped issue with acceptance criteria, minimal changes and honest verification.
---
# Bounded implementation

## Procedure
1. Read project instructions, issue and touched code. Check existing branches/PRs.
2. State scope, out-of-scope and acceptance criteria briefly.
3. Make the smallest maintainable patch; avoid unrelated refactors.
4. Run focused validation proportionate to risk and available infrastructure.
5. Inspect diff and record exact evidence.
6. Handoff with changed files, checks, unresolved issues and review notes.

## Output
Patch or PR plus evidence-backed handoff.

## Limits
Stop on missing authorization, conflicting work, security-sensitive uncertainty or requirements that cannot be safely inferred. Do not assume CI is disabled in every project.
