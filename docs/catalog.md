# Skill catalog

The canonical machine-readable catalog is [catalog.json](../catalog.json). Core installs contain 13 skills; optional contains 9.

| Skill | Profile | Stage | Output |
|---|---|---|---|
| [haloskill-start](../plugins/haloskill/skills/haloskill-start/SKILL.md) | core | 1–8 | Project Overview with readiness, evidence gaps and next actions |
| [haloskill-project-setup](../plugins/haloskill/skills/haloskill-project-setup/SKILL.md) | core | 1–8 | Project overview, internal sales handoff, scope and project tracker |
| [haloskill-roadmap-to-timeline](../plugins/haloskill/skills/haloskill-roadmap-to-timeline/SKILL.md) | core | 1, 3, 5–8 | Delivery Plan, milestone gates, forecast and optional native calendar |
| [haloskill-workshop-client-research](../plugins/haloskill/skills/haloskill-workshop-client-research/SKILL.md) | core | 2 | Workshop research packet |
| [haloskill-workshop-script-writer](../plugins/haloskill/skills/haloskill-workshop-script-writer/SKILL.md) | core | 2–3 | Facilitator script |
| [haloskill-research](../plugins/haloskill/skills/haloskill-research/SKILL.md) | core | 2–3 | Evidence ledger, findings, implications and open questions |
| [haloskill-site-architecture](../plugins/haloskill/skills/haloskill-site-architecture/SKILL.md) | core | 3–4 | Sitemap, page inventory, navigation and flows |
| [haloskill-concepts](../plugins/haloskill/skills/haloskill-concepts/SKILL.md) | core | 4 | Versioned concept images; after approval, editable HTML and direct Figma copy |
| [haloskill-copywriting](../plugins/haloskill/skills/haloskill-copywriting/SKILL.md) | core | 3–7 | Page copy, CTA variants, metadata and content gaps |
| [haloskill-presentations](../plugins/haloskill/skills/haloskill-presentations/SKILL.md) | core | 1, 5–8 | Editable deck, speaker notes and feedback log |
| [haloskill-web-build](../plugins/haloskill/skills/haloskill-web-build/SKILL.md) | core | 6–8 | Website implementation, Storybook and verification evidence |
| [haloskill-design-review](../plugins/haloskill/skills/haloskill-design-review/SKILL.md) | core | 4–8 | Review findings and approval decisions |
| [haloskill-handoff](../plugins/haloskill/skills/haloskill-handoff/SKILL.md) | core | 8 | Delivery package, acceptance matrix and ownership plan |
| [haloskill-interface-design](../plugins/haloskill/skills/haloskill-interface-design/SKILL.md) | optional | 4–7 | Interface designs and interaction rules |
| [haloskill-figma-library](../plugins/haloskill/skills/haloskill-figma-library/SKILL.md) | optional | 6–7 | Figma variables, components and documentation |
| [haloskill-code-connect](../plugins/haloskill/skills/haloskill-code-connect/SKILL.md) | optional | 6–7 | Validated mappings or template files |
| [haloskill-design-debt](../plugins/haloskill/skills/haloskill-design-debt/SKILL.md) | optional | 6–8 | Debt register with impact, effort and owners |
| [haloskill-imagegen](../plugins/haloskill/skills/haloskill-imagegen/SKILL.md) | optional | 4–7 | Generated assets and usage notes |
| [haloskill-brand-positioning](../plugins/haloskill/skills/haloskill-brand-positioning/SKILL.md) | optional | 2–3 | Positioning options and approved messaging foundation |
| [haloskill-seo-audit](../plugins/haloskill/skills/haloskill-seo-audit/SKILL.md) | optional | 2, 8 | SEO findings and verification plan |
| [haloskill-analytics](../plugins/haloskill/skills/haloskill-analytics/SKILL.md) | optional | 3, 7–8 | Measurement plan and event verification |
| [haloskill-design-canvas](../plugins/haloskill/skills/haloskill-design-canvas/SKILL.md) | optional | 4, 6–7 | Captured page canvas, flows and review feedback |

## Scope boundaries

- Project Setup owns scope, tasks, decisions, risks and updates. Roadmap to Timeline computes dates from actual estimates.
- Workshop Client Research prepares the workshop packet. Research synthesizes supplied evidence or investigates deeper questions. Workshop Script Writer prepares the facilitator's script.
- Site Architecture owns the initial sitemap and flows. Design Canvas inspects captured implemented states.
- Concepts first collects missing brief details, visual references and required source images and waits for them; no-reference work or delegated reference selection requires an explicit user choice. Before using references, it asks for their composition/style/detail roles and waits for explicit answers, reusing roles already specified. It follows the confirmed mapping when generating and revising website or branding images, then reconstructs an explicitly approved version as editable HTML with direct Figma clipboard capture. The user pastes into Figma; layer and Auto Layout verification is a separate check. Design Review evaluates decisions. The starter handles production implementation and technical QA.
- Copywriting owns page messaging and voice. The starter's writing guidance covers local UI copy during implementation.
- Presentations has proposal, concepts, and review/handoff modes. Existing Halo assets and template references are retained.
- Storybook and Figma Library are separate deliverables. Code Connect links real design and code components.

Optional skills are not less important; their need depends on the contracted scope. A project may need none or several.
