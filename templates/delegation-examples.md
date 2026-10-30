# Delegation examples

These are illustrative task briefs, not evidence of model performance.

## Example A: lightweight agent — UI label fix

**Objective:** Add accessible names to two icon-only buttons in a single view.
**In scope:** The view and its existing translation entries.
**Out of scope:** Backend, permissions, unrelated UI refactors.
**Acceptance:** Both buttons have meaningful accessible names in supported locales; behavior unchanged.
**Checks:** Focused component test or manual accessibility inspection, plus diff review.
**Handoff:** Files, checks actually run, skipped checks, remaining risks and PR.
**Escalate if:** Existing translation architecture is inconsistent or the fix requires shared component redesign.

## Example B: strong agent — cross-module authorization

**Objective:** Design and implement a tenant-scoped permission check across service and persistence boundaries.
**In scope:** Authorization policy and affected entry points.
**Out of scope:** Unrelated feature additions, production deployment.
**Acceptance:** Positive and negative permission cases covered; revocation behavior documented; no cross-tenant access.
**Checks:** Security-focused code review and relevant integration tests where available.
**Handoff:** Design tradeoffs, touched boundaries, evidence, remaining risks and PR.
**Delegate later:** Mechanical test fixtures, documentation, formatting and focused regression checks.
**Escalate if:** Security policy is ambiguous or data migration is required.

## Example C: independent integrator — parallel work

**Objective:** Integrate two nonoverlapping PRs touching separate components.
**In scope:** Conflict review, compatibility checks and focused tests.
**Out of scope:** New features and deployment.
**Acceptance:** Both changes preserve intended behavior; cross-task interactions checked.
**Handoff:** Integration findings, checks, blockers and merge recommendation.
**Escalate if:** Shared contracts changed or concurrent edits overlap.
