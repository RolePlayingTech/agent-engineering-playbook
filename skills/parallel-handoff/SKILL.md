---
name: parallel-handoff
description: Split independent tasks across agents with explicit file ownership and structured integration handoffs.
---
# Parallel agent handoff

## Procedure
1. Split only tasks with limited dependencies and overlap.
2. Assign each worker a bounded objective, file ownership, acceptance criteria and branch.
3. Share canonical repository rules and only relevant context.
4. Require handoff: summary, changed files, checks, risks and commit/PR reference.
5. Have an integrator check conflicts and cross-task behavior.
6. Prefer sequential work if shared state or coordination overhead dominates.

## Output
Worker task briefs, structured handoffs and integration status.

## Limits
Parallelization is not automatically faster; avoid simultaneous edits to the same files without explicit coordination. No merge without authorization.
