# Evidence status: model routing

**Reviewed:** 2026-10-30

The routing matrix in [model routing](../workflows/model-routing.md) is a **heuristic proposal**, not a measured ranking of model families. It synthesizes common engineering considerations: uncertainty, blast radius, task separability, review effort and cost of retries.

No comparative experiments have been executed in this repository. No model-specific performance claims are made. Vendor pricing and capabilities change, so avoid hard-coding them into permanent routing rules.

## Testable hypotheses

1. Narrow, easily verified changes may cost less with lightweight agents.
2. Cross-module or high-uncertainty tasks may have lower total cost with stronger reasoning.
3. Parallelism may reduce wall time when tasks have limited dependencies.
4. Review and integration overhead may erase savings from cheaper workers.

## Required evidence for stronger claims

Record task samples, model/version, prompt and tools, acceptance outcome, reviewer findings, retries, input/output tokens, direct charges where known, elapsed time and coordination time. Include failures and limitations. Use [the evaluation harness](../evals/README.md) for observable trace checks, supplemented by human review of correctness.

**Status:** hypotheses awaiting local evaluation.
