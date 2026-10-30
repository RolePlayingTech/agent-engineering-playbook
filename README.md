# Agent Engineering Playbook

Evidence-informed, vendor-neutral skills, instructions and workflows for working with AI coding agents.

**Status:** evolving research-backed toolkit. Last research sweep: 2026-10-30. This is not a certification of performance.

## Principles

1. Start with the smallest useful workflow; do not add orchestration by default.
2. Treat primary-source claims as hypotheses until tested in your own environment.
3. Give each agent a bounded task, clear acceptance criteria and explicit authority.
4. Keep persistent context concise and load detailed skills only when needed.
5. Evaluate observable actions and outcomes, not polished final summaries alone.
6. Prefer isolated parallel tasks; integrate and review centrally.
7. Never claim a test ran, a merge occurred or a deployment succeeded without evidence.

## Contents

- [AGENTS.md](AGENTS.md): default agent operating contract
- [Skills](skills/README.md): reusable, progressively loaded procedures
- [Workflows](workflows/README.md): implementation, research and review paths
- [Research](research/2026-10-30-source-review.md): dated primary-source reading list and interpretation
- [Templates](templates/task-brief.md): reusable assignment format
- [Evaluation](evals/README.md): lightweight behavioral checks
- [Contributing](CONTRIBUTING.md): evidence and maintenance policy

## Adoption

Copy AGENTS.md and only relevant skill folders into a project. Adapt commands, permissions and acceptance checks to the actual repository. Do not blindly install every skill.

This repository summarizes and synthesizes external sources; it is not affiliated with their publishers.
