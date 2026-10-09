# Website delivery workflow

## 1. A client brings a brief

Start with `$haloskill-start`, then `$haloskill-project-setup`. Supply the brief, accepted proposal/estimate when available, existing assets and recorded agreements. Start updates a concise Project Overview: source basis, current stage, readiness, ownership gaps and next actions. Keep internal routing out of project documents. Missing commercial inputs can block production commitment without blocking research preparation.

Project Setup maintains one parent overview and supporting sections: internal Sales to Delivery Handoff, Scope & Deliverables, Delivery Plan and Project Tracker. Distinguish requested services from purchased scope, quantities from assumptions, proposed acceptance rules from agreed terms, and proposed roles from assigned people. Capture final approval authority, consolidated feedback, review windows, revision allowances and the process for changes after approval. Use Presentations in proposal mode if commercial scope needs presentation.

Use Roadmap to Timeline with supplied estimates, or with provisional durations already authorized by the user. A target date is not an effort estimate; assumed phase days are not person-hours. Keep work, client reviews and zero-duration milestone gates distinct. Each gate has completion evidence, an approver, an owner or gap, dependencies and the work it unlocks. Preserve approved baseline, current forecast and actual completion separately.

When a native workspace is requested, update existing pages and linked databases instead of duplicating records. Verify navigation, table readability, board state and the populated timeline window. A Markdown package or static table must not be described as a connected system. **Exit:** PM-reviewable kickoff package with explicit commercial gaps, preparation/production readiness, scope dispositions and a disclosed planning status. Client approval is recorded only from evidence.

## 2. Prepare research and the workshop

Use Workshop Client Research for the client's standard research packet. Use Research for deeper audience, competitor or industry questions only when needed. Feed the brief and evidence into Workshop Script Writer for questions, exercises, sequence and timing. Avoid duplicating research or treating guesses as client facts. **Exit:** team-reviewed packet and facilitator script.

## 3. Conduct the workshop and reconcile outcomes

The team facilitates and talks to the client using the prepared script. Capture actual notes or a transcript through the available meeting process. Script Writer is useful in preparation and can help revise an exercise; it does not conduct a people-led meeting or know what was said.

Afterward, Research synthesizes the real notes. Project Setup updates the brief, decisions, tasks and scope changes. Site Architecture then produces the sitemap, page inventory, navigation and primary flows. Update the forecast where scope changed. **Exit:** decisions and unresolved questions clearly separated; architecture ready for client review.

## 4. Develop visual concepts

Concepts uses the available brief and references to generate website concepts, branding concepts or a website based on selected branding. A complete research package or sitemap is not required for exploration. If the brief or visual basis is missing, request the brief, references and required source images and wait before generating. Reuse existing inputs; proceed without references only on the user's explicit instruction, or inspect sources selected under delegated reference choice. Ask the user to assign or confirm each reference's composition, style or detail role and wait for the answer, unless already explicit. Follow those roles and exclusions exactly; attachment order is not an assignment. Then use an available image-generation/editing tool, and preserve image versions and focused revisions. Start with one concept when no count is requested, or two for an unspecified comparison request. Copywriting supports credible content. **Exit:** inspected concept images with stable labels, short rationales and a recorded preference or change request; HTML follows explicit approval.

## 5. Present and select

Presentations uses concepts mode to explain options and tradeoffs. The team presents; the client chooses or requests changes. Design Review supplies a consistent rubric. Project Setup records actual feedback, the exact image/version, approval wording, affected tasks and scope consequences. Selecting or liking an image alone does not authorize reconstruction.

After explicit approval for transfer, Concepts rebuilds the approved scope as real HTML/CSS with native text and separate assets, checks it against the image, and opens the local Copy to Figma preview. The user copies through the official Figma Code to canvas runtime and pastes directly onto the Figma Design canvas; no custom Figma plugin is required. Capture success proves capture only. Verify appearance, native layers and appropriate Auto Layout separately when access permits, otherwise record verification as pending. **Exit:** explicit approval and the requested HTML/Figma handoff with actual verification status. This does not authorize production functionality, extra pages or publication.

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
