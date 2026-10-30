---
name: parallel-handoff
description: Split independent tasks across agents with explicit file ownership and structured integration handoffs.
---
# Parallel agent handoff
1. Split only tasks with limited dependency and overlap.
2. Give each worker a bounded objective, file ownership, acceptance criteria and branch name.
3. Keep each worker's context narrow; share canonical repo instructions.
4. Require a handoff: summary, changed files, checks, risks, commit/PR reference.
5. Have an integrator check conflicts and cross-task behavior before merge.
6. Prefer sequential execution when shared state or coordination cost dominates.
