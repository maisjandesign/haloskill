# Command examples

Use these prompts inside Codex after installation. Replace “this” with attached material or concrete project paths. The commands do not authorize unrelated installs, messages or publication.

| Skill | Example command |
|---|---|
| Start | `$haloskill-start read this brief and existing records, update Project Overview with readiness and next actions, and continue the needed workflow.` |
| Project Setup | `$haloskill-project-setup prepare the project overview, internal sales handoff, scope and tracker from this brief and actual agreements.` |
| Roadmap to Timeline | `$haloskill-roadmap-to-timeline build the delivery plan from this estimate, separating work, client reviews and milestone approval gates.` |
| Workshop Client Research | `$haloskill-workshop-client-research research this client and prepare evidence for the workshop.` |
| Workshop Script Writer | `$haloskill-workshop-script-writer prepare a workshop script from the brief and client research.` |
| Research | `$haloskill-research synthesize these sources into findings and design implications.` |
| Site Architecture | `$haloskill-site-architecture create the sitemap and primary user flows from the approved brief.` |
| Concepts | `$haloskill-concepts generate one website concept image from this brief and references; after I approve a version, build editable HTML with direct copy to Figma.` |
| Copywriting | `$haloskill-copywriting write website copy from the approved sitemap, research, and brand voice.` |
| Presentations | `$haloskill-presentations prepare a concept presentation with rationale, tradeoffs, and a clear client decision.` |
| Web Build | `$haloskill-web-build implement the approved design with the studio Next.js starter.` |
| Design Review | `$haloskill-design-review review this design against the brief and agreed acceptance criteria.` |
| Handoff | `$haloskill-handoff prepare the final delivery package and acceptance checklist.` |
| Interface Design | `$haloskill-interface-design design the product interface using the approved context and workflows.` |
| Figma Library | `$haloskill-figma-library build the Figma library from the approved tokens and components.` |
| Code Connect | `$haloskill-code-connect connect these Figma components to their implementation.` |
| Design Debt | `$haloskill-design-debt audit accumulated design inconsistencies and prioritize fixes.` |
| Image Generation | `$haloskill-imagegen create the requested website image using the approved art direction.` |
| Brand Positioning | `$haloskill-brand-positioning develop positioning options from audience and competitor evidence.` |
| SEO Audit | `$haloskill-seo-audit audit this website for technical and on-page SEO issues.` |
| Analytics | `$haloskill-analytics define and verify analytics events for the primary website journeys.` |
| Design Canvas | `$haloskill-design-canvas prepare a Design Canvas review of these implemented pages and flows.` |

## Concepts modes and handoff

Supply a brief and references for website, branding or website-from-branding work. The available image tool generates actual concept images; the package does not include provider access. A complete sitemap is not required.

```text
$haloskill-concepts Generate one branding concept image from this brief. Use R1 for composition and R2 for visual style.

$haloskill-concepts Create a website concept image using branding A2 as the identity and this web reference for layout.

$haloskill-concepts In A1, preserve the layout and photos and refine the typography.

$haloskill-concepts A2 is approved for transfer. Build editable HTML for that version and open the direct Copy to Figma preview.
```

After capture, paste directly onto the Figma Design canvas with Cmd+V / Ctrl+V. No custom Figma plugin is needed. Native layers and Auto Layout remain unverified until inspected after paste. See [requirements](../plugins/haloskill/skills/haloskill-concepts/references/setup-and-requirements.md) and [handoff details](../plugins/haloskill/skills/haloskill-concepts/references/html-figma-handoff.md).

## Useful continuations

```text
$haloskill-project-setup Reconcile these workshop notes with our existing brief, decision log and task board. Separate confirmed decisions from requests and open questions.

$haloskill-presentations Use proposal mode. Build the deck from the attached scope and estimate; preserve the Halo template and mark missing commercial inputs.

$haloskill-web-build Run the project's routine verification, fix confirmed defects within scope, and report evidence. Do not claim integrations are verified without an actual check.

$haloskill-handoff This is a design-only engagement. Prepare the editable design package, component/state specifications, known gaps and acceptance checklist.
```
