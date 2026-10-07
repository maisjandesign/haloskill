# Design Canvas integration

Source: [volomydyr/design-canvas](https://github.com/volomydyr/design-canvas), audited at `e5c39c84b2b39b03b8ae429c613780ac37e1d377`.

Design Canvas captures existing routes/states for visual review, grouping, flows and exploration. Its low-fidelity options also start from a captured baseline. It does not create an initial information architecture from a brief. Capture accuracy is not QA coverage.

The audited runtime depends on Next/React, Tailwind, Playwright and lucide. The studio starter does not include all of these dependencies. Inspect compatibility and follow upstream installation intentionally; do not imply plug-and-play integration. Preserve the upstream immutable runtime/core and isolate its styling from production tokens and shell. Review the source's external exploration-skill prerequisites before promising that mode.

Use same-origin routing and reproducible states. Freeze GSAP at the intended capture state without modifying production animation behavior; isolate capture build output. Validate captured assets, live links, grouped flows and comments. Very long flow strips have layout limits. Preserve human approval state independently of agent-processed comments.

Keep the tool unavailable on production routes as upstream requires. Source-specific artifact sharing cannot be assumed available in Codex; use an actually supported output. Runtime installation, browser capture, state synchronization and production exclusion need a real project test. They have not been verified merely by packaging this adapter.
