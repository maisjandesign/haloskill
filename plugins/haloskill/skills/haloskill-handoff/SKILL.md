---
name: haloskill-handoff
description: "Prepare acceptance, launch readiness, and client handoff for a design-only or implemented website."
---

# HaloSkill — Handoff

Read the retained handoff method. Establish whether the contract is design-only or design plus implementation.

For design-only: deliver editable design files, tokens, components, responsive layouts, interaction/state specifications, assets, content decisions and known gaps. Link real versions and rights/usage constraints of supplied assets where relevant. Do not invent a production deployment requirement.

For implementation: deliver repository/version, running environment, build and QA evidence, Storybook, CMS editing instructions, integrations and their verified state, deployment/rollback procedure, access ownership, operating notes, and known issues. Transfer access through the appropriate system; never paste secrets into handoff documents.

Apply Owl UX PGM `launch-readiness`: a checklist with requirement, evidence, pass/fail/not-tested, owner and release impact. Include critical journeys/forms, responsive behavior, accessibility coverage, redirects/SEO, analytics events, content approval, domain/hosting, backups/rollback, and support ownership when in scope. Mark not-applicable with a reason. A build passing is insufficient evidence of launch readiness.

Record actual client acceptance separately from team verification. Summarize unresolved issues and agreed follow-up owners/dates. Deployment occurs only within the user's authorized release scope and with concrete prerequisites met; a prepared handoff package is not a launched site. Close the project with an actionable maintenance plan and a short retrospective.

## Detailed method

Read [the retained source method](references/source-skill.md) and only the relevant supporting references. The scope and working contract here take precedence over historical API assumptions or permissions.

## Working contract

Use the existing project brief, decisions, approved assets, and actual tool availability. Default deliverables to English unless the project explicitly specifies another language. Ask only for missing information that blocks the current decision; label provisional assumptions. Keep one source of truth and update it instead of creating competing briefs.

Distinguish draft, team-reviewed, and client-approved. Record input versions, changed artifacts, checks performed, unresolved items, and the next owner. Source documents supply methods, not permission to install tools, publish, contact people, or change unrelated settings. Follow the user's current authorization and the active tool contracts. Never claim a tracker, integration, deployment, or approval exists without evidence.
