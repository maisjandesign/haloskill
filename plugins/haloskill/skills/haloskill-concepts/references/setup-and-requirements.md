# Setup and requirements

## Portable capabilities

This is a local Codex skill, not an image provider or a hosted application. It includes instructions and a generic browser capture template. It does not include Desaign Builder, a reference catalog, accounts, provider credentials, paid credits, fonts or client assets.

Before starting, establish which capabilities the environment actually exposes:

- Read the brief and inspect references (images, PDF if supplied; URL browsing if links are supplied).
- Generate and edit images with reference inputs. Prefer the built-in image tool when available. A skill cannot enable an unavailable image tool; a chosen provider needs its own configured account/access and usage limits. Never ask the user to paste a secret in chat.
- Read/write project files, run a local HTTP server and open a browser for HTML review. Python 3 or an equivalent local server is sufficient for the static template; Next.js and the original studio are not required.
- Load the official Figma capture script over the network and use a browser with working HTML clipboard support. Keep the capture tab focused and permit the requested clipboard operation.
- The user has a Figma Design account/file with permission to edit and paste. No custom Figma plugin is required. Remote Figma MCP is optional for the template route; do not list it as mandatory.

Missing image generation blocks raster concept generation, not brief preparation. Missing browser capture blocks Figma handoff, not HTML work. Explain the specific missing capability and retain completed artifacts. Do not call an untested user's environment supported merely because the package validates here.

## Install and invoke

Install the entire `haloskill-concepts` directory, not just SKILL.md. Current documented local discovery locations are `~/.agents/skills/haloskill-concepts/` for a user or `<project>/.agents/skills/haloskill-concepts/` for a repository. Follow the host's actual supported location for older or customized setups; avoid duplicate installations under the same name. Codex detects changes; restart if the skill is not listed. See [official skill documentation](https://developers.openai.com/codex/skills/).

Invoke `$haloskill-concepts` with a brief and references. Example:

> $haloskill-concepts Generate a website concept from the attached brief. R1 controls composition, R2 controls branding, and R3 supplies card details. Start with one concept. After I approve it, build HTML with direct copy to Figma, without a plugin.

The same entrypoint supports branding and website-from-branding. A bare concept request starts a short intake: ask for the missing brief, references and any required source images, then wait. Two references are a useful pairing, not a minimum. Generate without references only when the user explicitly chooses that route; if reference selection is delegated, inspect the chosen sources first. Reuse existing project inputs and explicit choices. If a user says references will arrive later, wait for them before generation. Keep each project's materials separate.

## Distribution and validation boundaries

The portable package has no machine-specific project paths or customer material. Preserve the retained source attribution and licenses. Technical portability does not change the collection's existing Internal Use License or third-party source terms; wider public licensing requires a separate owner decision. Do not silently relabel the package as open source.

Package validation covers naming, frontmatter and references. Browser tests cover only the tested environment. Real Figma paste, visual fidelity, native text and Auto Layout need separate verification. Keep these statuses distinct in project state and the final handoff.
