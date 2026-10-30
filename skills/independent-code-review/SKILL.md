---
name: independent-code-review
description: Review an agent-authored change for correctness, regressions and evidence without trusting its summary.
---
# Independent code review

## Procedure
1. Read task and inspect actual diff, not only the PR description.
2. Prioritize correctness, authorization, data loss, concurrency and API compatibility.
3. Trace changed behavior to callers and tests; inspect coverage of acceptance criteria.
4. Report actionable findings with file/line, severity and reasoning.
5. Separate blocking defects from suggestions; do not invent failures.
6. Approve only when evidence supports acceptance; merge only with authorization.

## Output
Findings with severity and location, verification performed, and review decision.

## Limits
Do not claim tests passed unless run or supported by trustworthy recorded results. A review is not deployment approval.
