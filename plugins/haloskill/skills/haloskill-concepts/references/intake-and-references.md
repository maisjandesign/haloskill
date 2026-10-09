# Intake and reference roles

## Reuse the brief, request visual inputs

Read the supplied brief and current project facts before asking about the client. Establish business/product, audience, goal and design scope without inventing missing facts. Existing client knowledge does not replace visual references.

If no current reference set is supplied, ask in the user's language for two references:

- **Composition:** layout, grid, proportions, hierarchy, whitespace and placement of elements.
- **Style:** typography, palette, photography/illustration, textures and visual treatment.

Invite additional references and required logos/photos. Request image uploads in ordinary chat and wait; the Questions tool accepts text, not attachments. Reuse a set already attached for this concept. If the user will send references later, wait. Only an explicit user instruction authorizes original work without references; do not offer an automatic no-reference fallback just because files are missing.

## Inspect and identify sources

Inspect each selected image, then label R1, R2, etc. in attachment order. Record filename/path or URL, inspected status and a short identifying description. A folder is a candidate collection: inspect selected originals and identify the proposed subset in Questions. Do not assume a catalog is accessible; this skill does not include the Desaign Builder R2 collection. If a link cannot be inspected, request an accessible image rather than describing unseen pixels. Agent-selected sources still require the same Questions confirmation.

## Required Questions interaction

For each new reference set, confirm roles through an actual interactive Questions tool, even when upload captions suggest a mapping. Do not ask the role question as ordinary chat. Prefer `request_user_input_async` when available; respect the host's actual tool schema and invocation limits. If no usable Questions tool exists, report the limitation and keep generation pending.

For two images, translate this illustrative payload to the user's language and substitute identifying descriptions:

```json
{
  "questions": [{
    "title": "Which reference controls composition and which controls style? R1 = first image [description]; R2 = second image [description]. Choose a mapping, or use the custom answer to assign different roles, extra references or specific details.",
    "options": [
      "First image (R1): composition; second image (R2): style",
      "Second image (R2): composition; first image (R1): style"
    ]
  }]
}
```

The UI supplies the third route as a custom/free-text answer. Do not add an "Other" option when the host provides it automatically. A preselected first option is not a submitted answer. Wait for the response; an empty result, timeout or elapsed time never selects a mapping. Do not generate a concept, sample or HTML while the question is unresolved.

For more than two images, identify every image in the question. Keep the two pair choices when meaningful and explicitly state that those choices leave additional images unused; the custom answer can assign R3/R4/etc. to details, style or composition. Never silently use the remaining images. For one reference, omit binary options and use a free-text Questions prompt asking which aspects it should control and how to handle the other role. Do not automatically use the same image for both roles.

If a custom answer is incomplete, ambiguous, conflicts with required identity or exceeds tool input limits, resolve only the missing decision through Questions and wait. A completed Questions answer for the unchanged set carries forward through revisions. New references or changes to the mapping require a new Questions answer; no repeated upload or confirmation is needed for unchanged inputs.

## Follow the answer exactly

Record the submitted answer with stable source IDs, roles, selected qualities and exclusions. Attachment order identifies images; it never determines their roles by itself.

- Composition sources control the confirmed grid, proportions, hierarchy, whitespace and placement. For a branding board, preserve the assigned panel boundaries and text capacity.
- Style sources control only the confirmed typography, color, imagery, texture or treatment. Their layout must not replace the composition source.
- Detail references affect only their assigned elements. Logos and photographs used as actual assets remain distinct from inspiration.
- For website-from-branding work, propose the selected branding as identity and a web reference as structure in Questions. Do not silently use a branding board grid as website structure.

Requested weights guide treatment, not literal canvas percentages or permission to change structure. The brief controls meaning and factual copy; required identity controls what must remain. Resolve conflicts through Questions. Borrow principles rather than logos, exact artwork, people or recognizable signature constructions.

After a complete Questions answer, restate the mapping briefly, then generate using the appropriate mode and structural rules. Do not add another generation-approval step. Verify the result against the confirmed roles and correct drift rather than reinterpret the user's answer.
