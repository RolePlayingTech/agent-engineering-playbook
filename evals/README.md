# Lightweight behavioral evaluation harness

An **offline, Python standard-library-only** checker of recorded agent events. It does not run agents, call model APIs or establish code correctness.

## Quick start

From the repository root:

```sh
python3 evals/run.py evals/cases/honest-validation.json evals/fixtures/honest-validation-example.json
python3 -m unittest discover -s evals -p 'test_*.py'
```

The bundled trace is **illustrative**, not a real agent run. The example demonstrates only rule matching.

## Run a real comparison

1. Define a failure mode and a case with observable required or forbidden events.
2. Run the same task with baseline instructions and treatment instructions in comparable environments.
3. Capture raw agent events, original logs, diffs and actual test output.
4. Evaluate each trace with the checker and review task correctness independently.
5. Record model/tool versions, task ID, date, tokens, elapsed time, reviewer, acceptance and limitations. Repeat trials when appropriate.

See [schema](schema.md) and [behavioral-evaluation skill](../skills/behavioral-evaluation/SKILL.md).

## Limits

Substring checks may have false positives and false negatives. A passing trace does not prove a test actually ran or that a patch works. Never publish example fixtures as empirical results. No measured agent performance results are included.

## Compare actual agent runs

See [experiment protocol](experiment-guide.md) and the deliberately synthetic [record template](experiment-template.json). After recording real, independently reviewed baseline and treatment runs, use:

```sh
python3 evals/compare.py path/to/real-records.json
```

The comparison tool rejects synthetic examples and reports only descriptive statistics. No real agent trials are bundled.
