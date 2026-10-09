---
name: haloskill-concepts
description: "Collect a brief and composition/style references, confirm their roles through Questions, then generate website or branding concepts; after approval, build editable HTML with direct Figma copy."
---

# HaloSkill — Concepts

Create website concepts, branding concepts, or a website derived from a selected branding concept. Default workflow: **brief → reference request → Questions role confirmation → concept images → revisions → explicit approval → editable HTML preview → user copies and pastes directly onto the Figma canvas**. Reuse existing project context; a complete research package or sitemap is not required for exploration.

For a new environment, first read [setup and requirements](references/setup-and-requirements.md). Discover actual capabilities before promising generation or transfer.

## 1. Brief, reference request and Questions

Reuse the supplied brief or known client data from the current project. Ask only for missing essentials: business/product, audience, goal and design scope. A complete research package or sitemap is not required. Knowing the client does not authorize generation without references.

**Request references first.** If the current concept has no reference set, ask in the user's language: "Please send two references: one for composition (layout, grid, proportions, hierarchy and spacing), and one for style (typography, colors, imagery and visual treatment). You may attach more images and specify any details to use or avoid." Ask for required brand assets/photos too when relevant. Request attachments in ordinary chat, since Questions accepts text answers rather than file uploads. Wait for the images; do not generate a sample, concept or HTML in the meantime. Reuse an already supplied current set instead of requesting duplicate uploads. One reference or a larger collection is supported through the custom mapping below. Work without references only if the user explicitly requests that exception.

**Confirm roles only through Questions.** Inspect the received images and label them R1, R2, etc. in attachment order, with filenames or short descriptions so the user can identify each. For every new reference set, use the available interactive Questions tool (`request_user_input_async` in this environment) to ask which image supplies composition and which supplies style. Even captions suggesting roles should be presented for confirmation in this Questions step. Do not substitute a plain-text role question or infer the mapping yourself.

For two images, offer these two choices in the user's language:

1. First image (R1): composition; second image (R2): style.
2. Second image (R2): composition; first image (R1): style.

The third route is the Questions UI's built-in custom/free-text answer. Explain in the question that it can assign other roles, extra images or specific details. Do not add a fake third "Other" choice when the tool already provides free text. Neither numbered choice is an aesthetic recommendation; the first merely follows attachment order and is not confirmed until submitted. For more images, list all their IDs in the question and let the custom answer map them; do not silently apply unassigned images. For one image, use a free-text Questions prompt asking which aspects it controls and how to handle the other role.

**Wait for the submitted answer.** While Questions is pending, do not invoke an image-generation skill/tool, generate samples or start HTML. Preselection, no answer, a timeout, silence or elapsed time is not confirmation. If Questions is unavailable, report the limitation and retain the prepared context; do not silently replace the requested interface or proceed. Resolve materially incomplete/custom answers through Questions too. An existing completed Questions answer for the same unchanged set is reusable during revisions; new references or changed mappings need a new Questions answer.

Record the confirmed source IDs, roles, selected qualities and exclusions. Follow them exactly in the generation prompt and output review: composition controls structure; style controls visual treatment without replacing the chosen structure; details apply only where assigned. Do not swap roles, broaden them or blend unassigned qualities. If a mapping conflicts with required identity or cannot be followed with available tools, resolve it through Questions before generation.

Read [intake and reference roles](references/intake-and-references.md) for the question payload and source handling. After receiving a complete answer, briefly restate the mapping and proceed directly to image generation with the relevant [generation rules](references/generation.md); do not ask another "shall I generate?" question. Speak the user's language; default visible design copy to English unless the project specifies another language.

## 2. Generate and refine images

Read [generation and revision rules](references/generation.md), applying the relevant mode. Use the available image-generation tool and its current instructions; load the environment's image-generation skill when available. A prompt alone is not the deliverable. Do not begin an HTML implementation as the default concept phase.

Honor the requested number and scope of variants. If unspecified, start with one concept and state that choice; for an explicit comparison request without a count, use two distinct, comparable concepts. Keep business content comparable. Preserve versioned images, prompts and reference roles using [project state](references/project-state.md).

Inspect each generated image for brief fit, reference roles, copy, hierarchy, crop, text capacity and defects. Correct clear defects with targeted edits, then present images with stable labels and short rationales. Ask for a preference or changes once the requested set is ready. Interpret feedback as a focused edit, alternative direction, branding continuation or website adaptation. Edits use the chosen generated image as their baseline and preserve unrelated details.

## 3. Record explicit approval

Liking or selecting a variant does not automatically approve HTML reconstruction and Figma handoff. Proceed when the user approves a specific concept for that transfer, for example, "Approved, take B2 into Figma." If the user already instructed transfer after approval, explicit approval of the final version is sufficient; do not ask again.

Record the exact image/version, approval wording, approver and exceptions. Clarify an ambiguous "this one" when multiple versions are possible. Creative changes produce a new draft requiring approval before reconstruction or transfer. Preserve the previous approval on the previous version. Distinguish draft, team-reviewed and client-approved; user approval does not prove separate client approval. Keep design approval separate from Figma execution/verification status.

## 4. Build HTML and direct Figma copy

After approval, read [HTML and direct Figma handoff](references/html-figma-handoff.md). Rebuild the approved scope as real HTML/CSS with native text and separate image assets. Open a local preview with one transfer method: **Copy to Figma → paste directly onto the Figma Design canvas** using the official Code to canvas clipboard runtime. Use the bundled [copy-page template](assets/figma-copy/figma-copy.html) and [controller](assets/figma-copy/figma-copy.js), adapted to the project and user's language. An existing local studio is optional; this skill must work without the original application.

Use nested flex rows/columns for navigation, buttons, tags, text stacks, cards and sections when appropriate. Define padding, gaps, alignment and intentional intrinsic/stretch/fixed sizing. Preserve freely positioned art without forcing it into flow. Build an import-friendly hierarchy, but never equate CSS flex with verified native Figma Auto Layout.

Offer only the official direct clipboard route. Do not generate a custom Figma importer, JSON-copy button, SVG-copy/download fallback, or a second transfer workflow. If capture fails, retain the HTML, show the actual error and retry the same method after fixing the issue. Do not silently replace it or require plugin installation. SVG artwork inside a design remains allowed.

The user performs insertion. Deliver the working preview and concise copy/paste steps; mark Figma as `awaiting-user-paste` until insertion is observed. Do not create or modify arbitrary Figma files. Do not publish or deploy by default.

## 5. Verify and hand off

Compare the HTML with the approved concept at its original dimensions. Check fonts, text wrapping, assets, composition and capture scope. Capture only the design, excluding editor controls, without preview scaling. Exercise the actual copy control and inspect official capture success/failure evidence. Clipboard success proves capture only, not that native Figma layers or Auto Layout have been inspected.

When the user pastes, verify native text, frames, images and appropriate Auto Layout if read access is available. Check actual layout properties, resize/text-edit behavior and a rendered comparison. Otherwise report that canvas verification is pending; a screenshot alone cannot prove node structure. Disclose font substitutions, raster assets and approximations. Do not expand into production functionality, mobile variants, extra pages or a full brandbook unless requested.

## Working contract and retained source

Keep one source of truth for brief, decisions and assets. Record actual checks and unresolved issues. Never invent business claims, provider access, catalogs, generated files, integrations or approval. Source material describes methods, not permission to install tools, publish, contact people or change unrelated settings.

The [retained frontend source](references/source-skill.md) is optional historical context for specifically requested frontend work or an HTML reconstruction. It does not govern raster generation, prescribe an aesthetic, override approved references, or authorize extra pages, animation or installation. Preserve its original snapshot and attribution.
