# HaloSkill

**A studio workflow for taking a website from client brief to final handoff.**

13 core skills · 9 optional specialists · English documentation · Codex-ready names

HaloSkill combines project management, research, workshop preparation, design, copywriting and delivery under one `haloskill-*` family. The studio's Next.js starter supplies implementation, Storybook, motion and technical QA. People lead client workshops, curate design, and approve decisions.

## Start here

```bash
git clone https://github.com/maisjandesign/haloskill.git
cd haloskill
python3 scripts/install.py --project /path/to/your/project --dry-run
python3 scripts/install.py --project /path/to/your/project
```

The repository is publicly visible, but use of its original materials requires written authorization from maisjandesign for internal Company work. Public access is not a general permission to use or redistribute those materials; see the [license](LICENSE.md). Authorized employees and contractors need Python 3.9+ and an existing project directory. The default installs only the 13 core skills into that project's `.agents/skills`. Open a new Codex chat in the project, attach the brief, and use:

```text
$haloskill-start Read this brief and the existing project records. Prepare Project Overview with readiness, missing evidence and next actions, then develop the needed kickoff documents. This is a website design and implementation project.
```

For design-only work, say so; the workflow ends in design handoff without forcing a code build. Skills are instructions and resources, not an unattended pipeline or bundled external services.

## Core skills

| Skill | Command | What it does |
|---|---|---|
| [Start](plugins/haloskill/skills/haloskill-start/SKILL.md) | `$haloskill-start` | Assess project readiness from a brief and existing artifacts, summarize the next actions, and select the needed delivery workflow. |
| [Project Setup](plugins/haloskill/skills/haloskill-project-setup/SKILL.md) | `$haloskill-project-setup` | Create or maintain a website project's overview, sales handoff, scope, acceptance criteria, tasks, decisions and risks from its actual evidence. |
| [Roadmap to Timeline](plugins/haloskill/skills/haloskill-roadmap-to-timeline/SKILL.md) | `$haloskill-roadmap-to-timeline` | Build or revise a delivery calendar from estimates or authorized provisional assumptions, with review windows, dependencies and milestone gates. |
| [Workshop Client Research](plugins/haloskill/skills/haloskill-workshop-client-research/SKILL.md) | `$haloskill-workshop-client-research` | Prepare client and competitor research for the content strategy workshop. |
| [Workshop Script Writer](plugins/haloskill/skills/haloskill-workshop-script-writer/SKILL.md) | `$haloskill-workshop-script-writer` | Prepare the facilitator script, questions, exercises, and timing for a people-led workshop. |
| [Research](plugins/haloskill/skills/haloskill-research/SKILL.md) | `$haloskill-research` | Synthesize evidence or investigate audience, competitors, and industry questions beyond workshop preparation. |
| [Site Architecture](plugins/haloskill/skills/haloskill-site-architecture/SKILL.md) | `$haloskill-site-architecture` | Define a website sitemap, navigation, URLs, content responsibilities, and key user flows before visual design. |
| [Concepts](plugins/haloskill/skills/haloskill-concepts/SKILL.md) | `$haloskill-concepts` | Collect the brief and visual references before generating website or branding concept images; after approval, build editable HTML with direct Figma clipboard transfer, without a Figma plugin. |
| [Copywriting](plugins/haloskill/skills/haloskill-copywriting/SKILL.md) | `$haloskill-copywriting` | Write and edit website copy using approved positioning, brand voice, audience evidence, and verified proof. |
| [Presentations](plugins/haloskill/skills/haloskill-presentations/SKILL.md) | `$haloskill-presentations` | Prepare Halo proposals, concept presentations, and project review decks with evidence and clear client decisions. |
| [Web Build](plugins/haloskill/skills/haloskill-web-build/SKILL.md) | `$haloskill-web-build` | Implement approved website designs using the studio Next.js starter and its built-in component, motion, and QA workflows. |
| [Design Review](plugins/haloskill/skills/haloskill-design-review/SKILL.md) | `$haloskill-design-review` | Review a design against the brief, approved direction, content, and acceptance criteria and record actionable decisions. |
| [Handoff](plugins/haloskill/skills/haloskill-handoff/SKILL.md) | `$haloskill-handoff` | Prepare acceptance, launch readiness, and client handoff for a design-only or implemented website. |

## Optional specialists

Install only what the engagement needs. These are available in the repository but excluded from the default script installation.

| Skill | Command | What it does |
|---|---|---|
| [Interface Design](plugins/haloskill/skills/haloskill-interface-design/SKILL.md) | `$haloskill-interface-design` | Design product interfaces such as dashboards, admin tools, and account areas when the website includes application UI. |
| [Figma Library](plugins/haloskill/skills/haloskill-figma-library/SKILL.md) | `$haloskill-figma-library` | Create or maintain editable Figma variables and components when a Figma design system is a deliverable. |
| [Code Connect](plugins/haloskill/skills/haloskill-code-connect/SKILL.md) | `$haloskill-code-connect` | Map existing Figma components to implementation components using the supported Code Connect integration. |
| [Design Debt](plugins/haloskill/skills/haloskill-design-debt/SKILL.md) | `$haloskill-design-debt` | Inventory and prioritize accumulated design inconsistency in an existing website or product. |
| [Image Generation](plugins/haloskill/skills/haloskill-imagegen/SKILL.md) | `$haloskill-imagegen` | Generate or edit raster assets for a website through an available image generation provider. |
| [Brand Positioning](plugins/haloskill/skills/haloskill-brand-positioning/SKILL.md) | `$haloskill-brand-positioning` | Clarify audience, category, differentiation, promise, and evidence when brand positioning is explicitly in scope. |
| [SEO Audit](plugins/haloskill/skills/haloskill-seo-audit/SKILL.md) | `$haloskill-seo-audit` | Audit an existing or pre-launch website for technical and on-page SEO issues with evidence and prioritized fixes. |
| [Analytics](plugins/haloskill/skills/haloskill-analytics/SKILL.md) | `$haloskill-analytics` | Plan and verify website analytics events against business questions and actual implementation evidence. |
| [Design Canvas](plugins/haloskill/skills/haloskill-design-canvas/SKILL.md) | `$haloskill-design-canvas` | Use Design Canvas to review captured implemented pages, flows, and visual alternatives when its runtime is integrated. |

```bash
python3 scripts/install.py --project /path/to/your/project --skill haloskill-design-canvas
python3 scripts/install.py --project /path/to/your/project --profile all
```

`$haloskill-name` is the Codex skill invocation. The command tables are prompts, not shell commands or invented slash commands. The package's single plugin contains all 22 skills; use the installer when you want profile selection.

## The delivery flow

| Stage | Primary skills | Human checkpoint |
|---|---|---|
| 1. Request and kickoff | Start → Project Setup → Roadmap to Timeline; Presentations for proposals | PM validates scope, owners and assumptions |
| 2. Research and preparation | Workshop Client Research; Research for deeper questions; Workshop Script Writer | Team reviews evidence and facilitator plan |
| 3. Workshop and synthesis | Team uses the prepared script; Research + Project Setup process actual notes; Site Architecture follows | People facilitate; client decisions are recorded |
| 4. Visual concepts | Concepts uses an available image-generation tool; Copywriting supports content | Designer reviews concept images and focused revisions |
| 5. Concept presentation and approval | Presentations + Design Review; Concepts prepares approved HTML and direct Figma copy | Record explicit approval; user pastes into Figma and verifies the result |
| 6. System and homepage | Web Build through the studio starter; optional Figma Library / Code Connect | Designer and client review homepage and system |
| 7. Remaining pages | Web Build + Copywriting; optional Canvas / SEO / Analytics | Team reviews templates, content and integrations |
| 8. QA and delivery | Starter checks and exploratory QA → fixes → Handoff | Team verifies; client accepts; authorized launch |

**Workshop Script Writer prepares the session.** It does not replace the facilitator, record a live meeting, or produce real meeting outcomes from the script.

**Design Canvas reviews captured pages and flows.** Initial sitemaps belong to Site Architecture. Canvas requires a separate runtime integration and real routes/states.

**Concepts starts with intake.** For a bare concept request, it asks for the missing brief, visual references and required source images, then waits before generating. Existing project materials are reused; working without references or delegating their selection requires an explicit user choice. A complete sitemap is not required. Review and revise the images, then explicitly approve a version for editable HTML and direct Figma copy. The user pastes onto the Figma Design canvas; capture success alone does not verify native layers or Auto Layout. See the [concept workflow and requirements](plugins/haloskill/skills/haloskill-concepts/references/setup-and-requirements.md).

## Documentation

| Guide | Use it for |
|---|---|
| [Complete catalog](docs/catalog.md) | Skill scope, outputs and installation profile |
| [Command examples](docs/commands.md) | Copy-ready prompts for all 22 skills |
| [Workflow](docs/workflow.md) | From a brief to final delivery, with artifacts and gates |
| [Installation](docs/installation.md) | Core, optional, selected and user-level installs |
| [Dependencies](docs/dependencies.md) | Starter, Canvas, Figma, Notion and presentation providers |
| [Migration](docs/migration.md) | Every old skill name and its replacement |
| [License](LICENSE.md) | Authorized internal use and distribution restrictions for original materials |
| [Validation](docs/validation.md) | Reproduce checks and understand their limits |
| [Verification report](docs/verification-report.md) | What was actually verified for this release |
| [Changelog](CHANGELOG.md) | Release changes |

## Maintainers

```bash
python3 scripts/validate.py
python3 scripts/test_install.py
python3 scripts/test_timeline.py
```

See [repository instructions](AGENTS.md) for maintenance rules.

## License

Original materials owned by maisjandesign are provided under the [HaloSkill Internal Use License](LICENSE.md). Only employees and contractors authorized by maisjandesign may use and internally modify them for the designated Company's work, including client projects. Personal use, outside freelance work, publication, external distribution, and resale require separate permission. Client deliverables may be shared and sold under the terms described there.

Included third-party materials retain their own terms, which can differ from these permissions. See [third-party notices](LICENSE-NOTICE.md) for the applicable licenses. Neither internal access nor this license grants unrestricted rights to the entire collection.
