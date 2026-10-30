# Baseline vs treatment experiment

This is a protocol for **real agent runs**, not a benchmark result.

1. Choose at least five representative tasks, each with a reproducible starting commit and independent acceptance criteria.
2. Predefine baseline (existing instructions) and treatment (one additional skill or routing policy). Keep prompts, environment and tools comparable; randomize execution order when practical.
3. Capture task ID, exact model/version, variant, reviewer, original logs or PR evidence, acceptance outcome, retries, elapsed time, and optionally total cost in USD.
4. Have the reviewer inspect the actual diff and test evidence, not just the agent summary. Record reviewer and integration effort separately if available.
5. Enter one baseline and one treatment record per task using [the JSON template](experiment-template.json). Set `synthetic: false` **only for actual runs with evidence**.
6. Run `python3 evals/compare.py path/to/real-records.json`. The tool reports paired descriptive statistics and missing cost values as null.
7. Report limitations, task selection bias, model variability and small sample size. Do not infer causality from a small descriptive comparison.

The included JSON template is deliberately marked synthetic and **cannot** be accepted as empirical input. Never overwrite this marker just to obtain a passing report.

Use [behavioral checks](README.md) for trace-level assertions; the comparison tool only summarizes independently reviewed run records.
