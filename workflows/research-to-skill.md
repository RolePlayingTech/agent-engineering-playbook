# Research-to-Skill Pipeline

Turn engineering publications into testable procedures, not automatic best practices.

## 1. Intake
Record the original URL, publisher, author, publication and review dates. Paraphrase one specific, falsifiable claim. Distinguish research papers, product documentation, vendor reports and anecdotes.

## 2. Appraise
Record the task, environment, model/tool versions, metrics, sample size and limitations when provided. Mark missing details unknown. Separate observed results from recommendations and marketing.

## 3. Decide applicability
Identify a recurring problem, a clear invocation trigger, prerequisites, risks and the simplest existing alternative. If the idea duplicates an existing skill or adds unnecessary complexity, reject or keep it as a research note.

## 4. Plan evaluation
Specify a baseline without the proposed guidance, treatment with guidance, comparable tasks, observable success criteria, traces, repetitions where feasible and cost measures. Define failure criteria before running the experiment.

## 5. Draft a minimal skill
Follow [the skill specification](../skills/SPECIFICATION.md). Include frontmatter, concise procedure, expected output and limits. Cite research notes, not unsupported performance promises.

## 6. Review and classify
Use four evidence labels: **hypothesis**, **publisher recommendation**, **independent observation**, **locally tested**. A locally tested label requires dated artifacts and reproducible results. An experimental skill can be useful without being proven.

## 7. Maintain
Revisit after relevant model, tool or workflow changes. Preserve negative results and update links. Avoid silently converting hypotheses into facts.

## Decision gates
- **Reject:** no clear repeated need, unsupported generalization, excessive risk or duplication.
- **Research only:** interesting but not actionable or testable yet.
- **Experimental skill:** actionable and has an evaluation plan, but no local results.
- **Evaluated skill:** has documented local results, including limitations.

## Deliverables
A [source note](../templates/source-note.md), a [skill proposal](../templates/skill-proposal.md), and optionally an evaluation record and reviewed SKILL.md. Never report unrun experiments as successful.
