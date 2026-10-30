# Primary-source review — 2026-10-30

This is a curated initial sweep, not an exhaustive survey of all October publications. **Source guidance is not local experimental proof.**

## Recent sources

1. **Anthropic, Donating Agent Skills to the Agentic AI Foundation (2026-10-22).** https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation — supports vendor-neutral skill packaging; adoption claims are publisher-reported.
2. **Google Cloud, Four evaluation engineering lessons (2026-10-16).** https://cloud.google.com/blog/topics/developers-practitioners/four-eval-engineering-lessons/ — favors checking execution evidence over final summaries.
3. **Anthropic Engineering, Redesigning source control at Anthropic (2026-10-13).** https://www.anthropic.com/engineering — relevant to integration bottlenecks at scale; do not generalize their infrastructure needs to small projects.
4. **OpenAI, Introducing the Agents API (2026-09-10).** https://openai.com/index/introducing-the-agents-api/ — harness context, tool discovery, subagents and durable execution; product claims need independent testing.
5. **Google Developers, The Anatomy of Harness Engineering (2026-09-09).** https://developers.googleblog.com/en/the-anatomy-of-harness-engineering-how-to-evaluate-iterate-and-guard-ai-coding-agents/ — recommends behavioral evaluations alongside end-to-end tests.
6. **OpenAI, Separating signal from noise in coding evaluations (2026-07-08).** https://openai.com/index/separating-signal-from-noise-coding-evaluations/ — warns that benchmark task quality and underspecification can distort conclusions.
7. **Anthropic, Harness design for long-running application development (2026-03-24).** https://www.anthropic.com/engineering — harness design matters for long sessions; investigate specifics before adopting.
8. **OpenAI Developers, Testing Agent Skills Systematically with Evals (2026-01-22).** https://developers.openai.com/blog/eval-skills — concrete process: prompt, trace/artifacts, checks and score.
9. **Anthropic, Equipping agents with Agent Skills (2025-10-16).** https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills — SKILL.md folders, discoverability and progressive disclosure.

## Synthesized design choices

- Portable SKILL.md folders; keep AGENTS.md short.
- Small behavioral evals and real-task outcome checks rather than headline benchmarks alone.
- Parallel agents only for independent work; integration remains an explicit phase.
- Short structured handoffs and evidence-backed completion reports.
- Minimal useful harness first, more infrastructure only when repeated failures justify it.

## Open experiments

- Compare skill-on vs skill-off for 5 recurring tasks using outcome, latency and tokens.
- Measure whether independent reviewer finds defects missed by implementing agent.
- Compare parallel vs sequential throughput including integration and conflict resolution.
- Compare concise vs exhaustive AGENTS.md on success and instruction adherence.

No experiments have been executed for this repository yet.
