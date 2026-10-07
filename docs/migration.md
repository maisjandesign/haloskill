# Migration: v0.1 → v0.2

The old 29-entry package is consolidated into 13 core workflows and 9 optional specialists. Removed wrappers are preserved in Git history. No user installation is automatically deleted or overwritten.

| Previous skill | Current destination | Change |
|---|---|---|
| `haloskill-project-setup` | `haloskill-project-setup` | Retained; Workshop content unchanged, other entry points clarified in English. |
| `haloskill-decisions` | `haloskill-project-setup` | Decision rights and logs merged into project management. |
| `haloskill-design-review` | `haloskill-design-review` | Retained; Workshop content unchanged, other entry points clarified in English. |
| `haloskill-research` | `haloskill-research` | Retained; Workshop content unchanged, other entry points clarified in English. |
| `haloskill-concepts` | `haloskill-concepts` | Retained; Workshop content unchanged, other entry points clarified in English. |
| `haloskill-interface-design` | `haloskill-interface-design` | Retained; Workshop content unchanged, other entry points clarified in English. |
| `haloskill-layout` | `haloskill-web-build` | Use starter layout guidance. |
| `haloskill-typography` | `haloskill-web-build` | Use starter typography guidance. |
| `haloskill-colors` | `haloskill-web-build` | Use starter color guidance. |
| `haloskill-ui-polish` | `haloskill-web-build` | Use starter interface guidance. |
| `haloskill-accessibility` | `haloskill-web-build` | Use starter accessibility guidance and actual verification. |
| `haloskill-ux-writing` | `haloskill-copywriting` | Page messaging here; local UI writing through the starter. |
| `haloskill-sales-presentation` | `haloskill-presentations` | Retained Halo sales references and assets; choose proposal or concepts mode. |
| `haloskill-proposal-deck` | `haloskill-presentations` | Retained proposal template and assets; proposal mode. |
| `haloskill-design-system-rules` | `haloskill-web-build` | Project component-system workflow; optional Figma Library for Figma. |
| `haloskill-figma-to-code` | `haloskill-web-build` | Use starter reference implementation plus active Figma prerequisites. |
| `haloskill-figma-component-mapping` | `haloskill-code-connect` | Connector mode and file mode share one entry point. |
| `haloskill-design-qa` | `haloskill-web-build` | Starter verification and exploratory QA; Handoff tracks acceptance. |
| `haloskill-design-debt` | `haloskill-design-debt` | Retained; Workshop content unchanged, other entry points clarified in English. |
| `haloskill-handoff` | `haloskill-handoff` | Retained; Workshop content unchanged, other entry points clarified in English. |
| `haloskill-figma-library` | `haloskill-figma-library` | Retained; Workshop content unchanged, other entry points clarified in English. |
| `haloskill-code-connect` | `haloskill-code-connect` | Retained; Workshop content unchanged, other entry points clarified in English. |
| `haloskill-imagegen` | `haloskill-imagegen` | Retained; Workshop content unchanged, other entry points clarified in English. |
| `haloskill-presentations` | `haloskill-presentations` | Retained; Workshop content unchanged, other entry points clarified in English. |
| `haloskill-site-build` | `haloskill-web-build` | Default implementation is the user’s Next.js starter. |
| `haloskill-site-publish` | `haloskill-handoff` | Project-specific deployment and launch readiness; Sites provider remains external. |
| `haloskill-workshop-client-research` | `haloskill-workshop-client-research` | Retained; Workshop content unchanged, other entry points clarified in English. |
| `haloskill-workshop-script-writer` | `haloskill-workshop-script-writer` | Retained; Workshop content unchanged, other entry points clarified in English. |
| `haloskill-start` | `haloskill-start` | Retained; Workshop content unchanged, other entry points clarified in English. |

New entry points: Roadmap to Timeline, Site Architecture, Copywriting, Web Build, Brand Positioning, SEO Audit, Analytics, and Design Canvas. Decisions and operational PM methods now share Project Setup. The 22 total includes optional helpers and adapters, not external runtimes.

Use the [installation upgrade procedure](installation.md) to back up and replace an old installation deliberately. Re-running the installer over different existing files refuses the change; it does not silently upgrade.
