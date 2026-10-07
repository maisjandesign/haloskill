
# Halo Proposal Deck

Create a persuasive client document that feels native to Halo Lab, not a reskinned generic template.

## Source of truth

Treat `https://halolab-design.webflow.io/#1` as the primary visual reference. Always read [references/brand-system.md](../references/brand-system.md) before authoring. Use the bundled assets in `assets/` where they fit.

Do not import the current Halo Lab website's light backgrounds, serif display type, or unrelated visual language unless the user explicitly asks for a hybrid direction.

## Required workflow

1. Read [references/input-schema.md](../references/input-schema.md). Extract all available facts from the user's brief and attached documents. Ask only for missing information that materially changes scope, price, timing, or the decision narrative.
2. Read [references/proposal-architecture.md](../references/proposal-architecture.md). Build a concise story around the client's decision; do not force every optional section into every deck.
3. Read [references/brand-system.md](../references/brand-system.md) and choose a small set of its layout families. Preserve the live deck's rhythm rather than repeating one composition mechanically.
4. Invoke the presentation-authoring and PDF skills available in the environment. Build an editable 16:9 PPTX with `@oai/artifact-tool`; do not flatten entire slides into images.
5. Export the PPTX to PDF. Render every slide to images and inspect them at presentation size. Fix collisions, clipping, illegible type, bad crops, inconsistent page counts, and broken asset references before delivery.
6. Deliver both files by default: `halo-proposal-<client>-YYYY-MM-DD.pptx` and `halo-proposal-<client>-YYYY-MM-DD.pdf`.

## Content rules

- Write in the language of the user's brief unless asked otherwise.
- Use takeaway headlines, not topic labels. Each slide should advance one claim, decision, or proof point.
- Keep the client and desired business outcome central. Present Halo Lab's process as the mechanism for achieving that outcome.
- Never invent prices, dates, metrics, client names, testimonials, case-study results, team biographies, or legal terms.
- If a necessary fact is absent and does not justify interrupting the workflow, use an unmistakable bracketed placeholder such as `[INVESTMENT TO CONFIRM]`. Report all remaining placeholders on handoff.
- Make currencies, taxes, payment cadence, validity period, assumptions, and exclusions explicit wherever commercial figures appear.
- Cite external proof and borrowed imagery in slide notes. Do not cite the live reference on every slide; record it once in deck metadata or notes as the visual source.
- Prefer fewer strong slides to dense coverage. Split any slide that needs more than one reading path.

## Brand-specific composition rules

- Use the near-black navy canvas, white grotesk type, purple outcome blocks, and yellow functional accents from the live reference.
- Keep the persistent header on interior slides: logo at left, deck/client label centered, page fraction and outlined CTA/status at right, then a hairline divider.
- Use folder-tab tiles for roadmap, phases, deliverables, and schedule anchors.
- Use the three-zone step layout for scope and process: claim at left, accordion-like detail in the middle, one dominant visual or proof object at right.
- Show only one expanded accordion item per slide. Collapsed items act as context, not as extra body-copy containers.
- Use rounded media windows and thin white outlines. Do not add shadows, glassmorphism, gradients unrelated to the reference, generic SaaS cards, or stock decorative icons.
- Use real client/project visuals when available. Otherwise use purposeful diagrams and geometric brand shapes; never add meaningless filler imagery.

## Quality gate

Do not deliver until all are true:

- PPTX remains editable and PDF visually matches it.
- Every slide has a clear hierarchy and can be understood in under ten seconds.
- Body copy is readable at normal laptop view; no auto-shrunk text.
- No text or shapes overlap, clip, overflow, or sit outside safe margins.
- Page fractions and section labels are correct.
- No unsupported claim or hidden placeholder remains.
- Notes include source URLs for external facts and assets.
