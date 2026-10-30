---
name: independent-code-review
description: Review an agent-authored change for correctness, regressions and evidence without trusting its summary.
---
# Independent code review
1. Read the task and inspect the actual diff, not only the PR description.
2. Prioritize correctness, auth boundaries, data loss, concurrency and API compatibility.
3. Trace changed behavior to callers and tests. Verify assertions cover the requested behavior.
4. Report actionable findings with file/line, severity and reproduction reasoning.
5. Separate blocking defects from suggestions; do not invent failures.
6. Approve only when evidence supports the defined acceptance criteria; merge only with authorization.
