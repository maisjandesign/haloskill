# Dependencies and integration boundaries

| Workflow | Dependency | Included here | Still required in a project |
|---|---|---|---|
| Core planning/research/copy | Brief, evidence, optional web access | Methods and templates | Actual sources and relevant tool access |
| Timeline | Python 3.9+ | Local calculator and example | Real estimate, calendar and PM review |
| Notion timeline | Current Notion connection | Publishing schema/method | Connection and supported database/view operations |
| Web Build | Studio Next.js starter | Adapter and verified source reference | Clone/setup, assets, node packages, project checks |
| Design Canvas | Upstream runtime, Next/React, Tailwind, Playwright, lucide | Optional adapter | Compatibility work, runtime setup, capture and production-exclusion tests |
| Figma Library / Code Connect | Current Figma tooling and permissions | Methods, retained helper resources | Real files/components and tool-specific prerequisites |
| Presentations | Figma Slides, presentation provider, or HTML tooling | Halo assets, templates and mode guides | Available provider and requested output validation |
| Image Generation | Image generation provider | Workflow adapter | Connected generation tool |
| CMS / integrations / deploy | Project-specific services | Scope and handoff guidance | Implementation, access, verification and release setup |

## Studio starter

[Source](https://github.com/maisjandesign/codex-nextjs-site-starter), audited commit `e5303a57601dc1734ccd461491f3de63a644fff6`. Its bundled interface/motion/QA skills and local workflows replace duplicate Halo wrappers. Read [the adapter contract](../plugins/haloskill/skills/haloskill-web-build/references/starter.md). The baseline contains 21 bundled skills plus project-local workflow instructions; these are not counted among HaloSkill's 22.

The package provides setup/check, build, Storybook and separate audit setup commands. Read the current checkout before execution. Routine static checks, design-rule checks, browser inspection and the final exploratory audit are different forms of evidence. None automatically proves every accessibility requirement or third-party integration.

## Design Canvas

[Source](https://github.com/volomydyr/design-canvas), audited commit `e5c39c84b2b39b03b8ae429c613780ac37e1d377`. It reviews captured pages/states and their flows. The starter lacks some of its dependencies. Keep the tool runtime isolated, preserve its immutable core, handle animation capture state deliberately, and verify that tool routes are unavailable in production. See [the integration contract](../plugins/haloskill/skills/haloskill-design-canvas/references/integration.md). Packaging an adapter is not a completed integration.

## External services

Use current available APIs and active skills, not historical connector names or permissions copied from upstream documents. Missing service access should produce an explicit limitation and useful local artifacts, not a fictional completed operation. No credentials, client data or provider runtimes are bundled.
