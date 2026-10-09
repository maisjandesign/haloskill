# Approved concept to HTML and direct Figma copy

## One transfer method

Use only Figma's official [Code to canvas](https://developers.figma.com/docs/figma-mcp-server/code-to-canvas/) clipboard capture. The user copies from the browser and pastes onto a Figma Design canvas. No custom Figma plugin, JSON interchange, SVG clipboard fallback or automatic file creation is part of this workflow. If the method is unavailable, preserve the HTML and report what must be fixed; do not substitute another transfer method.

## Reconstruct the approved design

Use real HTML/CSS, native text, vectors for simple graphics and separate raster photographs or artwork. Do not use the whole concept image as the interface. Preserve approved scope, typography, content, proportions and palette. Intentional nested flex rows/columns, spacing and padding give the converter meaningful structure. Use absolute positioning for overlaps, decoration and photographic composition where appropriate. Intrinsic labels and groups should fit their content; intentionally sized controls remain fixed. CSS flex or grid is not proof that the pasted result has Auto Layout.

Keep assets inside the project, with relative URLs. A supplied raster concept does not provide original cutouts: reuse available assets or regenerate separate artwork using the available image tool and report meaningful differences. Preserve the approved image for comparison. A full brandbook, responsive site or additional pages require scope from the user.

## Copy-page template

Copy [figma-copy.html](../assets/figma-copy/figma-copy.html) and [figma-copy.js](../assets/figma-copy/figma-copy.js) to the output directory. Create `fragment.html` containing the scoped design, its CSS and one root element marked `data-figma-board`. Set the artboard dimensions on the template's `#design` element to the approved dimensions; translate the controls to the user's language. The template contains no client design or images. Keep the fragment and asset URLs relative. Serve over loopback HTTP; do not open via `file://`.

The template loads `https://mcp.figma.com/mcp/html-to-design/capture.js` and calls `window.figma.captureForDesign({selector:'[data-figma-board]', verbose:true})` without a file endpoint. This was inspected against the live official runtime on 2026-10-09; it is remotely maintained and must be checked when it changes. It is an integration template, not a bundled copy of Figma's runtime. The remote Figma MCP `generate_figma_design` tool can initialize the same official clipboard mode when available; its absence does not prevent the included browser-runtime route.

Wait for fonts and image decoding, then capture an unscaled artboard. A separate capture page is appropriate if the preview uses CSS scaling. The selector must exclude toolbars and helper text. Keep a single active capture session. The runtime's promise may stay pending until its toolbar closes; do not mistake that for a failed copy or repeatedly start concurrent captures. Closing or reloading the local page resets a session.

Use official runtime success/error UI as the primary signal. The controller also observes the runtime's verbose success message for a useful status; this message is version-dependent and must not be the sole compatibility test. No fake success timers. Do not read arbitrary system clipboard contents to diagnose a copy failure. Check only task-scoped signals or a controlled copy/paste test.

## Verification and recovery

1. Inspect the HTML at the approved dimensions: margins, wraps, images, clipping and visible claims.
2. Click Copy to Figma. Confirm official capture success or display the actual error. Capturing multiple artboards requires explicit per-board controls or a deliberately scoped wrapper, using the same capture method.
3. If capture stalls, focus the browser tab, check connectivity to the official runtime, clipboard permission and asset loading. Try an available supported browser and retry the same method. Do not install a plugin as a fallback. If unresolved, record `capture-blocked` and retain the HTML.
4. User pastes directly onto the Figma Design canvas with Cmd+V / Ctrl+V. Record `awaiting-user-paste`, then `pasted-unverified`, then `verified` only with evidence.
5. With actual Figma read access, verify native text, separate images, frame hierarchy, relevant `layoutMode`, sizing, padding and gaps. Edit a label and resize a suitable group, then compare a render against the approved HTML. If only a screenshot is available, verify appearance and disclose that structure is unverified.

Capture success does not establish pixel-identical reproduction, reusable components, Auto Layout or font availability. State limitations plainly. If Auto Layout is missing after paste, improve the HTML hierarchy and recapture through the same method; do not promise that every group will convert automatically.
