# Website delivery workflow

## 1. A client brings a brief

Start with `$haloskill-start`, then `$haloskill-project-setup`. Supply the brief, existing site/assets, known constraints and contract scope. Capture desired outcomes, audience, in/out of scope, deliverables, client approver, team owners, content responsibilities and unresolved questions. Build tasks with acceptance criteria and dependencies. Use Presentations in proposal mode if commercial scope needs presentation.

Use Roadmap to Timeline after effort estimates exist. The calculator produces a conservative serial schedule; client review windows and external dependencies must be explicit. A target date is not an estimate. **Exit:** PM-reviewed scope and a disclosed provisional/approved timeline.

## 2. Prepare research and the workshop

Use Workshop Client Research for the client's standard research packet. Use Research for deeper audience, competitor or industry questions only when needed. Feed the brief and evidence into Workshop Script Writer for questions, exercises, sequence and timing. Avoid duplicating research or treating guesses as client facts. **Exit:** team-reviewed packet and facilitator script.

## 3. Conduct the workshop and reconcile outcomes

The team facilitates and talks to the client using the prepared script. Capture actual notes or a transcript through the available meeting process. Script Writer is useful in preparation and can help revise an exercise; it does not conduct a people-led meeting or know what was said.

Afterward, Research synthesizes the real notes. Project Setup updates the brief, decisions, tasks and scope changes. Site Architecture then produces the sitemap, page inventory, navigation and primary flows. Update the forecast where scope changed. **Exit:** decisions and unresolved questions clearly separated; architecture ready for client review.

## 4. Develop visual concepts

Concepts uses the approved brief and structure to generate comparable directions. Copywriting supplies credible messages and realistic content; Image Generation is optional for needed raster assets. Designers curate and improve the directions and editable HTML concepts. **Exit:** distinct, coherent options with rationale, comparable content and known implementation implications.

## 5. Present and select

Presentations uses concepts mode to explain options and tradeoffs. The team presents; the client chooses or requests changes. Design Review supplies a consistent rubric. Project Setup records actual feedback, approval state, affected tasks and scope consequences. **Exit:** one selected direction and a clear change list; no inferred approval from silence.

## 6. Build the system and homepage

For implementation scope, Web Build uses the user's Next.js starter. Read the target checkout's instructions, set it up, create shared tokens/components and Storybook stories alongside the homepage, and implement approved motion. Optional Figma Library maintains an editable Figma system; optional Code Connect maps components when required. **Exit:** reviewed homepage, reusable system, browser evidence and client approval state.

For design-only scope, produce the same design decisions, components, responsive layouts and states in the agreed design tool. Do not start a code project merely to follow the stage list.

## 7. Expand remaining pages

Build page templates using the approved system, then real content and states. Copywriting maps messages to sections/CMS fields. CMS, integrations, SEO and analytics are separate explicit scope items. Design Canvas may capture implemented pages and flows for review after its runtime is integrated; it is optional and has additional dependencies. **Exit:** complete in-scope pages, content and verified integration status; unresolved items have owners.

## 8. Verify, accept and hand off

Run starter checks, production/Storybook builds and browser verification. When requested, run the separate exploratory QA workflow. Its report-only pass does not edit code; a subsequent authorized build pass fixes defects and retests affected behavior. Design Review assesses brief/design alignment. Handoff prepares delivery and launch readiness, separates pass/fail/not-tested evidence, and records real client acceptance.

For implemented sites include deployment/rollback, environment and CMS operating notes, access ownership and maintenance. For design-only delivery include editable files, design specification, assets and implementation guidance. Launch only within the actual authorized release scope. **Exit:** delivered artifacts, accepted scope or documented exceptions, and named follow-up owners.

## Shared artifacts

Keep one project context, evidence ledger, page inventory, decisions log, task board, estimate/timeline version and acceptance matrix. Link each stage's output to the next. Draft, team-reviewed and client-approved are distinct states. Tool output is not client approval, and a document describing an integration is not a connected integration.
