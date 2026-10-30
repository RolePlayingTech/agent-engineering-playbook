# Evaluation data contract (v1)

Case JSON: `id` (unique string), `description`, `prompt`, `checks` array. Each check has `id`, `kind` (`required` or `forbidden`), `event_type` and optional `contains` substring.

Trace JSON: `id`, `events` array with `type` and `text`. Traces must be captured or manually transcribed from actual agent behavior for real evaluations; label synthetic examples.

Result JSON: `case_id`, `trace_id`, `passed`, individual `checks`, and `note`.

The runner uses simple substring checks on event text, not semantic grading. A pass means only that recorded events match the rules. It does not prove the code is correct, that tools ran, or that the trace is genuine. Inspect original artifacts and use human review for substantive outcomes.

For comparisons, record task ID, baseline/treatment, model/version, tools, date, acceptance decision, reviewer, token use, elapsed time and raw artifact links in an external experiment log. Keep prompts and environment as comparable as possible; repeat when stochastic variance matters. Do not publish synthetic fixtures as measured outcomes.
