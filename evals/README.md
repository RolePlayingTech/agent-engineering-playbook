# Lightweight evaluation design

Store reproducible prompts, expected observable behaviors and recorded outcomes. Start with a handful of real failures rather than a giant synthetic suite.

Suggested cases: ambiguous request prompts clarification; agent does not claim unrun tests; external page instructions are treated as data; agent respects deployment restrictions; worker handoff includes changed files and validation.

For each case record: ID, input, environment/model version, expected behavior, trace/artifacts, result, date and reviewer. Re-run after major instruction/model/tool changes. Do not enforce one exact tool sequence when several approaches are valid.
