# Model routing and delegation

**Status:** practical heuristics, not validated model rankings. Route by task properties and observed outcomes, not model branding or advertised benchmarks.

## Decision matrix

| Task | Initial assignment | Escalate when | Verification |
| --- | --- | --- | --- |
| Documentation and narrow formatting | Lightweight agent | Ambiguous requirements or domain interpretation | Link and diff review |
| Localized bug with known reproduction | Lightweight agent | Root cause crosses modules or first attempt fails | Reproduction and focused tests |
| Test writing from established behavior | Lightweight agent | Expected behavior is uncertain or security-sensitive | Test review and execution |
| Architecture, cross-module changes | Strong reasoning agent | Already strong; narrow scope before delegating | Design review and integration tests |
| Authentication, authorization, data integrity | Strong reasoning agent | Human review for high-impact decisions | Threat-oriented review and negative tests |
| Independent code review | Different agent, chosen by risk | High-risk findings need experienced review | Inspect actual diff and evidence |
| Repetitive bounded subtasks | Lightweight agents in parallel if isolated | Conflicting ownership or integration overhead | Central integrator |

These are starting hypotheses. A cheaper agent can outperform a stronger one on some tasks; a strong agent may be cheaper overall if it avoids retries.

## Routing procedure

1. Define acceptance criteria, files, expected artifacts and permissions.
2. Assess uncertainty, dependency breadth, reversibility, security impact and ease of verification.
3. Prefer the least expensive agent likely to meet acceptance criteria; use stronger reasoning for high uncertainty or high consequence.
4. Assign one bounded task per worker. Use separate branches and avoid overlapping file ownership.
5. Require handoff with commit/PR, changed files, checks performed, skipped checks and unresolved risks.
6. Independently inspect the result; escalate after repeated failed attempts or evidence of a wrong approach.
7. Record total cost and accepted outcome, not just model output tokens.

## Context and handoff overhead

Budget total work as: initial context + worker execution + retries + reviewer time + integration + handoff. Parallel agents save wall time only when coordination does not dominate. Avoid using strong models solely to run routine commands when a smaller agent or deterministic script suffices.

## Stop and escalation signals

Escalate on unclear requirements, conflicting changes, failed validation without clear diagnosis, security-sensitive decisions, irreversibility, or repeated failed patches. Never bypass project merge or deployment policy.

## Evaluation proposal

Select at least 5 representative tasks with recorded acceptance criteria. Compare strong-only, lightweight-only and routed configurations where feasible. Keep environment and tooling comparable. Record task acceptance, reviewer defects, number of retries, elapsed time, input/output tokens, API cost when available, and handoff/integration time. Report missing cost data explicitly. Repeat trials when variability matters. Do not infer general superiority from one run.

## Related

- [Task brief](../templates/task-brief.md)
- [Delegation examples](../templates/delegation-examples.md)
- [Parallel handoff skill](../skills/parallel-handoff/SKILL.md)
- [Behavioral evaluations](../evals/README.md)
