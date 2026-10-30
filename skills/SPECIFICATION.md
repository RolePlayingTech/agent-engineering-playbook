# Skill specification (v1)

Keep skills short, portable, and actionable. This specification describes repository conventions, not a universal standard.

## Required
- Folder: `skills/<kebab-case-name>/SKILL.md`.
- YAML frontmatter: `name` matching the folder and a concise `description` explaining when to invoke it.
- Heading and a bounded, ordered procedure.
- Explicit expected output or handoff artifact.
- Limits or stop conditions, including authorization boundaries where applicable.

## Recommended when relevant
- **When to use:** trigger and situations where the skill is not appropriate.
- **Evidence:** links to research notes; distinguish source recommendation from locally tested results.
- **Verification:** observable completion checks, not a claim of measured effectiveness.
- **Maintenance:** revisit after tool/model or workflow changes.

## Avoid
- Duplicate global rules from AGENTS.md unless needed for a concrete decision.
- Vendor-specific assumptions in generic skills.
- Unsupported claims about improved speed, quality, or cost.
- Large reference dumps; link to separate documents when necessary.

## Review checklist
1. Does the description clearly trigger only relevant work?
2. Can an agent execute the steps without guessing the expected output?
3. Are scope and stopping conditions clear?
4. Does the skill overlap with an existing one?
5. Are evidence and local validation accurately labeled?
6. Are relative links and folder names consistent?

The six initial skills are procedural starting points; none has been validated by controlled local evaluations.
