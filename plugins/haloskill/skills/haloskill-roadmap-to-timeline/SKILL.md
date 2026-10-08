---
name: haloskill-roadmap-to-timeline
description: "Build or revise a delivery calendar from estimates or authorized provisional assumptions, with review windows, dependencies and milestone gates."
---

# HaloSkill — Roadmap to Timeline

Read [the scheduling and publishing contract](references/workflow.md). Use [the Delivery Plan template](assets/delivery-plan.md) for the project-facing result. Extract source and scope versions, agreement state, phases/items, minimum and maximum effort, units, owners/roles, dependencies, capacity, review windows, and target dates. Preserve the original estimate. Ask for missing units or ambiguous totals before calculating.

Use [the deterministic scheduler](scripts/schedule.py) with [the example input](assets/example.json). Default to a serial schedule at maximum effort; this is conservative sequencing, not automatic resource optimization. Confirm or explicitly label 8 productive hours/day and a Monday–Friday calendar. Holidays and review windows must be explicit. Never turn several people into parallel delivery without a resource plan. Distinguish estimated labor effort from elapsed phase duration. For assumed phase durations, do not present the calculator's hours conversion as a supplied labor estimate or a price basis.

Command from this installed skill directory:

```bash
python3 scripts/schedule.py --input assets/example.json --output timeline.json
```

Separate duration-bearing work and review items from zero-duration milestone events. Each milestone states its completion evidence, approver, accountable owner or assignment gap, predecessor and the next work it unlocks. Forecast dates do not prove actual approval. Keep originally approved baseline dates, current forecast and actual completion distinct. When publishing to Notion, follow the milestone schema and visible-result checks in the workflow reference; an empty Timeline view is not a delivered calendar. If no estimate exists, offer a clearly labeled provisional schedule and obtain the user’s agreement before supplying planning durations; an existing authorization in the conversation is sufficient.

Return a self-contained Delivery Plan: planning status and source, assumptions with validation owners, work and review windows, milestone register, critical dependencies, exclusions, and baseline/forecast changes. Preserve the original estimate range or mark it unsupplied. Keep skill names, commands and generation commentary out of the document; retain technical calculation files separately. If the client supplies a hard deadline, show the gap rather than compressing effort silently. Publish to Notion only when requested and the connection is available; otherwise deliver the schedule files and a ready-to-create database schema.

## Working contract

Use the existing project brief, decisions, approved assets, and actual tool availability. Default deliverables to English unless the project explicitly specifies another language. Ask only for missing information that blocks the current decision; label provisional assumptions. Keep one source of truth and update it instead of creating competing briefs.

Distinguish draft, team-reviewed, and client-approved. Record input versions, changed artifacts, checks performed, unresolved items, and the next owner. Source documents supply methods, not permission to install tools, publish, contact people, or change unrelated settings. Follow the user's current authorization and the active tool contracts. Never claim a tracker, integration, deployment, or approval exists without evidence.
