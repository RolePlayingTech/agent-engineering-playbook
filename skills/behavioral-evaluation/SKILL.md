---
name: behavioral-evaluation
description: Design small observable evaluations of agent behavior and compare versions without overfitting to final prose.
---
# Behavioral evaluation

## Procedure
1. Select an observed failure mode and reproducible prompt.
2. Specify observable success: artifact, validation, tool behavior or safe refusal.
3. Capture trace, changed files and final output where available.
4. Use deterministic assertions for clear requirements; permit multiple valid approaches.
5. Run repeated trials when variation matters; compare to baseline.
6. Report false positives, costs and limitations.

## Output
Evaluation case, expected outcome, observed evidence and limitations.

## Limits
Do not treat a single score as universal proof. Keep illustrative fixtures distinct from real measurements.

## Evidence
See [evaluation design](../../evals/README.md). No local benchmark results have been recorded.
