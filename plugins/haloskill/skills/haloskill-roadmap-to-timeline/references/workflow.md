# Timeline workflow

Adapted from the user's `roadmap-to-timeline.skill` document. The original was a skill archive, not an executable script; this package adds a local calculator.

1. Parse each estimate row without inventing work. Keep original labels, units, ranges and source references. Reconcile item sums with supplied totals; identify duplicate totals/subtotals. Omit neither QA nor client review if included in scope.
2. Choose start date and calendar. If no date was given, propose the next Monday and label it provisional. Eight productive hours/day and five days/week are defaults only when disclosed. Do not interpret 20 working days as an exact calendar month.
3. Use maximum effort for the forecast and show minimum/maximum estimate totals separately. The bundled calculator is serial, rounds each work item upward to whole working days, and adds explicit review days. Milestones have zero duration on the previous finish date, or project start for the first milestone. It does not optimize parallel teams, infer holidays, or forecast actual utilization.
4. Maintain source version, schedule version, approval state and recalculation reason. A revised forecast is not a changed contract. Compare old/new dates and highlight affected commitments.

## Notion output, when requested

Discover the current connector and supported database/view operations. Target a user-specified page, or prepare a proposed new page. Avoid writing into an unrelated existing page. Store target IDs and stable item IDs; reconcile existing rows on repeat runs rather than duplicating them. Do not modify the estimate source.

Prepare a summary plus two databases if the workflow needs both: phase-level Timeline and item-level Gantt. Properties: stable ID, phase, item, start/end, min/max effort, unit, owner/role, dependency, status, source/version, assumptions. Table, timeline and board-by-phase are useful views; a phase board is not a task status kanban. If the API cannot create a view, document the exact manual step rather than claiming it exists. Review windows and demo milestones are explicit schedule items, not hidden buffers.

## Calculator input contract

The example is synthetic, not a client estimate. `start` is an ISO date; `hours_per_day` is productive daily capacity for a single serial lane; `holidays` contains explicit ISO dates. Each item has a unique `id`, `min` and `max`, and `unit` (`hours` or `days`). Include both range values for actual work; if omitted, `min` defaults to zero and must not be presented as a supplied estimate. `kind` is `work` (default), `review` (working days), or `milestone` (zero effort). `depends_on` may name only earlier items because list order defines the serial schedule. Missing and forward dependencies are rejected rather than silently rescheduled.

`expected_work_hours` reconciles minimum/maximum totals for work items only; review windows do not count as productive effort. Extra descriptive fields such as phase, label and owner survive in the output. Unsupported parallel-capacity overrides are rejected. The result is a draft schedule, not a commitment or proof of resource availability. The CLI refuses to overwrite its input estimate.
