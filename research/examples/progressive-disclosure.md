# Worked example: progressive skill loading

- Original source: Anthropic, "Equipping agents for the real world with Agent Skills"
- URL: https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills
- Publisher: Anthropic
- Publication date: 2025-10-16 (from initial research review; verify before republishing)
- Review date: 2026-10-30
- Evidence class: **publisher recommendation**, not locally tested

## Claim
A short discoverable skill description can be loaded first, while detailed instructions are opened only when relevant. This may reduce irrelevant context, but does not itself establish better task outcomes in this repository.

## Applicability and limits
Useful candidate for sessions involving multiple skills. For short tasks, discovery overhead might outweigh any benefit.

## Proposed evaluation
Compare five representative coding tasks with all instructions loaded upfront against selective loading. Keep model, tools and tasks comparable. Capture accepted outcomes, reviewer findings, tokens, tool calls and elapsed time. Repeat when feasible.

## Failure criteria
Reject as a default if instruction adherence or accepted task outcomes deteriorate, or if overhead outweighs savings.

## Decision
**Research only / experimental candidate.** No local experiment has been executed. Related procedure: [context budgeting](../../skills/context-budgeting/SKILL.md).
