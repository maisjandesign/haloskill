---
name: haloskill-concepts
description: "Collect the brief and visual references before generating website or branding concept images; after approval, build editable HTML with direct Figma clipboard transfer, without a Figma plugin."
---

# HaloSkill — Concepts

Create website concepts, branding concepts, or a website derived from a selected branding concept. Default workflow: **brief and references → concept images → revisions → explicit approval → editable HTML preview → user copies and pastes directly onto the Figma canvas**. Reuse existing project context; a complete research package or sitemap is not required for exploration.

For a new environment, first read [setup and requirements](references/setup-and-requirements.md). Discover actual capabilities before promising generation or transfer.

## 1. Collect inputs before generation

A bare request such as "Create a design concept using HaloSkill Concepts" starts intake, not image generation. Before calling an image-generation tool or handing off to an image-generation skill, establish both:

- **Brief:** the actual business/product, intended audience, goal and requested design scope, from the current project or the user. Ask for missing essentials instead of inventing a project.
- **Visual basis:** relevant references and source images already supplied or explicitly selected for this project, inspected and assigned roles; or an explicit user instruction to proceed without references or to choose them on the user's behalf.

If the visual basis is missing, ask for reference images, links or a folder, plus any existing logo, brand assets or photos that must be used. If the brief is missing too, bundle those requests into one short intake message in the user's language. Explain that one reference is enough to start and that the user may explicitly choose to proceed without references. Then wait for the response. Do not generate a sample, placeholder concept or HTML while waiting. A general "create a concept", missing attachments, silence or elapsed time is not permission to skip references. If the user says materials will arrive later, wait for them.

Reuse materials and explicit choices already present in the current project; do not ask the user to resend them or reconfirm a no-reference choice. If the user delegated reference selection, choose and inspect relevant sources before generation. Once the inputs are ready, continue without a separate intake-approval step.

Read [intake and reference roles](references/intake-and-references.md). Extract known answers before asking for missing information. Speak the user's language; default visible deliverable copy to English unless the project specifies another language. Ask short questions in stages. Two references are a useful pairing, not a minimum count; this does not waive the visual-basis check above. Inspect supplied images, links or folders. Do not assume the application's catalog or saved settings are accessible.

Select website, branding or website-from-branding mode from context. Clarify only when it materially affects the result. Briefly state the design interpretation and which sources control composition and style. This is a progress update, not an extra approval gate.

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
