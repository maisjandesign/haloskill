# Studio starter integration

Source: [maisjandesign/codex-nextjs-site-starter](https://github.com/maisjandesign/codex-nextjs-site-starter), audited at `e5303a57601dc1734ccd461491f3de63a644fff6`. Read the chosen checkout's README, AGENTS and local skills; commands may change upstream.

The audited starter uses Next.js App Router, TypeScript, React and GSAP with a separate Storybook. Its 21 bundled skills cover interface quality, motion, code navigation and exploratory QA. Project workflows include `reference-site`, `gsap-next-motion`, and `site-component-system`. Reuse those instructions instead of installing duplicate Halo layout/type/color/UI/accessibility/writing wrappers.

The audited package provides `npm run new-project`, `npm run setup`, `npm run setup:check`, `npm run check`, `npm run build`, `npm run build-storybook`, `npm run setup:audit`, and `npm run setup:audit:check`. Follow the current creation script's arguments; do not guess them. Setup resolves project-local dependencies and snapshots; keep user-global configuration changes outside routine setup unless authorized.

Design conventions include an 8px spacing basis with technical 1/2px exceptions and body text at least 16px. These are project conventions, not universal design laws. Use shared tokens/components and real states in Storybook. Review at the reference width and narrower widths, including 1440/768/390/320 where appropriate. Verify interaction, content, navigation and responsive behavior, not only compilation.

Routine checks validate types/lint/design rules, production and Storybook builds. They are not proof of full accessibility, visual fidelity or successful integrations. The audited Storybook accessibility configuration contains incomplete test coverage. The final `ui-exploratory-qa` workflow requires a running ready site and the supported Chrome DevTools connection; it is an English report with evidence, not an automatic repair pass.

External work remains explicit: CMS/data models, APIs/forms, SEO, analytics, deployment, credentials, rollback and client acceptance. Do not mark these complete from starter availability alone.
