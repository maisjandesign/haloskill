# FIGMA-DESIGN-AI capabilities and delivery

The intended experience is one complete presentation without asking the user to select a new empty slide for every page. Use supported operations to achieve it; instructions cannot substitute for missing APIs.

## Installation check before work

Required package: **FIGMA-DESIGN-AI Connector**, exact ID `figma-local-bridge@personal`, from the user's configured `personal` plugin source. Do not substitute the general Figma plugin or a similarly named bridge.

1. Inspect active and discoverable tools for the `figma_local_bridge` namespace. If the connector tools are callable, proceed to `figma_connection_status`; do not install a duplicate.
2. If tools are missing, use available tool discovery and the environment's installed-plugin inventory or plugin manager. Missing tools alone do not prove the package is absent. Cached plugin files alone do not prove it is installed and enabled.
3. If the package is installed but disabled or not loaded, use a supported activation/reload action when available. Do not reinstall to repair a disconnected Figma session. If a restart is actually required, report it once rather than retrying indefinitely.
4. If the package is absent, resolve its exact entry from the configured `personal` source and install it with the environment's documented installation tool or CLI. Installing this exact dependency is explicitly requested by the user. Reuse the verified source identity; never invent a repository URL, download URL, installation command or package version. If that source is unavailable, request its location or the installable package instead of choosing a look-alike.
5. When only an installation suggestion/UI is exposed, initiate that supported flow and wait for the user to complete any required install confirmation. A suggestion is not an installation. Use an installation tool only when its documented eligibility rules permit this exact plugin; do not force a personal plugin into a restricted recommended-plugin installer.
6. Verify the installed/enabled state and rediscover callable connector tools. Then call `figma_connection_status`. Claim success only after verification. If installation is unsupported or fails, report the concrete blocker, preserve prepared work and avoid repeated install attempts without new evidence.

The Codex connector package and the plugin running inside the intended Figma file are separate requirements. If the connector is installed but `connected` is false, ask the user to run **FIGMA-DESIGN-AI** in that file. This is a connection step, not a new package installation. Do not modify pairing, security settings, credentials or write-approval behavior as part of setup.

## Preflight

- Load the installed figma-local-bridge:figma-design-ai skill and discover current tool schemas.
- Call figma_connection_status before the first Figma operation in a turn.
- Inspect the destination and selection. When adapting content, read figma_get_design_context through complete=true and record the read node count.
- Verify native SLIDE creation, multiple-slide/batch creation, SVG import or logo component reuse, and preview/readback support.
- Do not reuse node IDs from earlier sessions or treat FRAME as SLIDE.
- If disconnected, ask the user to run FIGMA-DESIGN-AI in the intended file. Normal discovery does not require a pairing code.

## Baseline observed on 2026-09-30

This is a capability snapshot, not a permanent restriction. Recheck installed tools.

DesignIR 0.1 supported FRAME, COMPONENT, TEXT, RECTANGLE, ELLIPSE and LINE. It did not support native SLIDE creation or SVG import. figma_create_design created one root and selected it after the write. parentNodeId was limited to the active selection or its descendants. figma_patch_selection could not reparent nodes or create native slides.

Consequences for that version:
- Separate top-level frames do not make a native Figma Slides presentation.
- A wrapper containing multiple slide designs does not solve native slide creation.
- Filling a selected existing SLIDE is possible, but subsequent targets need renewed selection. This is a manual fallback, not the default full-deck workflow.
- Do not automatically start that repeated manual fallback. Prepare the complete deck, explain the limitation once and use the fallback only if the user chooses it.
- Plugin source edits, another connector, changed security settings and desktop automation are not implicit workarounds. Connector development is a separate authorized task.

If native slides or the mandatory logo cannot be delivered through the permitted tools, retain the complete prepared content and original SVG and identify the missing capability. Never label a logo-less deck complete.

## Approvals and retries

Prefer one supported batch operation and one plugin approval for the deck. Do not infer that a skill can disable or bypass approval.

The observed plugin displayed “Review changes from Codex” with **Apply changes**. Use the current documented or observed button label.

A tool timeout does not prove cancellation: a pending request can execute after later approval.
1. Read back the current selection and structure.
2. Check whether the intended content appeared before resending.
3. If approval is pending, explain the exact action once.
4. Do not blindly retry and create duplicates.

Only claim successful creation after readback. Keep native slide IDs and content IDs distinct and verify every slide. Do not replace a missing logo with typed text to pass a completion check.
