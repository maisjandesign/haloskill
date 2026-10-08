# Timeline workflow

Adapted from the user's `roadmap-to-timeline.skill` document. The original was a skill archive, not an executable script; this package adds a local calculator.

1. Check the scope agreement state and estimate version. Keep unapproved options separate from committed work; a provisional full-scope scenario must say what has not been purchased. Parse each estimate row without inventing work. Keep original labels, units, ranges and source references. Reconcile item sums with supplied totals; identify duplicate totals/subtotals. Omit neither QA nor client review if included in scope.
2. Choose start date and calendar. If no date was given, propose the next Monday and label it provisional. Eight productive hours/day and five days/week are defaults only when disclosed. Do not interpret 20 working days as an exact calendar month.
3. Use maximum effort for the forecast and show minimum/maximum estimate totals separately. The bundled calculator is serial, rounds each work item upward to whole working days, and adds explicit review days. Milestones have zero duration on the previous finish date, or project start for the first milestone. It does not optimize parallel teams, infer holidays, or forecast actual utilization.
4. Maintain source version, scope version, schedule version, approval state and recalculation reason. Keep approved baseline dates immutable as a historical record; maintain current forecast and actual completion separately. If there is no approved baseline, say so. A revised forecast is not a changed contract. Compare old/new dates and highlight affected commitments.
5. For each material assumption, name the evidence needed, validation owner or assignment gap, and needed-by gate. Check client as well as studio availability, including local holidays and shutdowns. Review time is separate from production; revision work needs its own allowance or an explicit uncertainty. Show the gap to a hard deadline rather than hiding it through reduced durations.

## Project-facing delivery plan

Use the Delivery Plan asset: planning status and source basis, assumptions, work/review windows, milestone register, external dependencies and baseline/forecast changes. Output standalone English project prose by default; no skill routing, commands or generation commentary. Use valid destination links when published, not local relative links. Keep calculator JSON and diagnostics separate from the readable document.

A milestone is complete only when its stated evidence exists and the named approver has accepted it where required. Record delivery owner, approver or explicit gaps, predecessor and the work it unlocks. Keep the actual decision state separate from a milestone name written in the past tense. Do not claim an early public release unless the engagement calls for one.

### Effort, duration and capacity

An effort estimate measures labor; a phase duration measures elapsed working time. Several named roles do not imply allocated capacity. Use supplied hours/person-days only with clear units and the appropriate capacity basis. For provisional phase durations, the calculator can sequence day-based items, but its `work_estimate_hours` is only an internal conversion at `hours_per_day`. Do not report that conversion as supplied labor effort, utilization or a price estimate. Display assumed phase days and review days separately, with the original labor estimate marked not supplied.

The calculator supports one serial lane, not parallel resource scheduling. If a supplied plan requires parallel streams, preserve those inputs and either construct a separately validated resource/dependency plan with an appropriate tool or disclose the serial scenario's limitation. Never present its output as an optimized multi-person plan.

## Notion output, when requested

Discover the current connector and supported database/view operations. Target a user-specified page, or prepare a proposed new page. Avoid writing into an unrelated existing page. Store target IDs and stable item IDs; reconcile existing rows on repeat runs rather than duplicating them. Do not modify the estimate source.

Prepare a summary and reuse the project's existing schedule database where possible. A single database with multiple views usually suffices; create separate phase-level and item-level databases only when both levels are genuinely needed. Properties: stable ID, phase, item, native date range, original effort range and units when supplied, owner/role, approver, dependency, status, source/version, assumptions, completion criterion, baseline dates, forecast dates and actual completion. Leave absent actuals and approval evidence empty; do not copy forecast dates into them. Embed a linked Timeline view within Delivery Plan and expose Table and Milestones views where useful. A linked view edits the same underlying records: disclose that relationship in a preview and do not alter records merely to demonstrate a new layout. Table, timeline and board-by-phase are useful views; a phase board is not a task status kanban. If the API cannot create a view, document the exact manual step rather than claiming it exists. Review windows and demo milestones are explicit schedule items, not hidden buffers.

### Milestones and visible calendar completion

A phase names work performed over a date range. A milestone names an observable event or review gate (for example, “Website concept approved”), has zero working days, and uses a single date or identical start/end dates. Preparation does not mean that approval has happened: keep forecast date and actual approval status separate.

Use a native Select property `Type` with Work, Review, Milestone and Optional when combining items. Each milestone needs an outcome, acceptance criterion, approver, responsible role or explicit assignment gap, predecessor, the work it unlocks and forecast date. Link the work and review dependencies as well as milestone gates; decorative arrows are not a dependency model. Preserve stable row IDs and existing relations when fixing an existing database. Do not merely rename a phase database “Milestones”.

Use native Date properties, not date-looking text. Configure Timeline against the populated date range, or separate Start/End Date properties. Offer a filtered Milestones view (`Type = Milestone`) alongside Gantt and Table when items share a database. Use visible `◆` milestone labels if the interface has no distinct milestone marker; do not claim a native diamond rendering unless verified. Keep a short dated milestone register readable outside the chart.

Before reporting a calendar as complete, inspect the actual Notion view and the parent/child navigation: all scheduled items have valid dates, every milestone is visible in the relevant date window, Type and labels distinguish events from work, and dependencies still connect the intended rows. Choose a readable zoom/window covering the forecast, check the No date list and distinguish work/review colors with a short legend. When the full forecast cannot fit legibly, provide an overview and a detailed view; do not claim everything is visible without checking. Empty undated rows are a planning register, not a populated Gantt. If dates are unavailable, disclose that limitation and request the missing inputs instead of describing the timeline as finished.

### Provisional planning without an estimate

A brief alone is not an effort estimate. Ask once for the estimate and start date, offering a provisional forecast if appropriate. Reuse any authorization already given in the conversation. After the user authorizes it, label every duration and calculated date as a planning assumption; do not attribute them to the brief or call the totals a supplied estimate. State capacity/sequencing, review windows, holidays and exclusions. Use explicit assumptions as calculator input, keep phase work and review time distinct, and record which assumption must be replaced by the delivery team. Do not put client data or forecasts into the reusable skill repository.

## Calculator input contract

The example is synthetic, not a client estimate. `start` is an ISO date; `hours_per_day` is productive daily capacity for a single serial lane; `holidays` contains explicit ISO dates. Each item has a unique `id`, `min` and `max`, and `unit` (`hours` or `days`). Include both range values for actual work; if omitted, `min` defaults to zero and must not be presented as a supplied estimate. `kind` is `work` (default), `review` (working days), or `milestone` (zero effort). `depends_on` may name only earlier items because list order defines the serial schedule. Missing and forward dependencies are rejected rather than silently rescheduled.

`expected_work_hours` reconciles minimum/maximum totals for work items only; review windows do not count as productive effort. Extra descriptive fields such as phase, label and owner survive in the output. Unsupported parallel-capacity overrides are rejected. The result is a draft schedule, not a commitment or proof of resource availability. The CLI refuses to overwrite its input estimate.
