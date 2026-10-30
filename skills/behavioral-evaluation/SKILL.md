---
name: behavioral-evaluation
description: Design small observable evaluations of agent behavior and compare versions without overfitting to final prose.
---
# Behavioral evaluation
1. Select one observed failure mode and write a reproducible prompt.
2. Specify observable success: tool call, artifact, validation or safe refusal.
3. Capture trace, changed files and final output where possible.
4. Use deterministic assertions for clear requirements; allow multiple valid solution paths.
5. Run repeated trials when stochastic variation matters; compare against baseline.
6. Report false positives, cost and limitations. Do not treat a single benchmark score as ground truth.
