# Sources, reuse and consolidation

This release adapts source methods into task-specific studio workflows. It is not a claim that every upstream skill was installed unchanged. The two user-provided Workshop skills are the exception: their content is preserved, with naming-only changes from the original import.

[upstream.json](../sources/upstream.json) records source repository, pinned commit, original path, SHA-256, destination and direct link for each adapted method. [manifest.json](../sources/manifest.json) tracks current entry points and the Workshop invariants. [legacy-v0.1.json](../sources/legacy-v0.1.json) preserves provenance of retained source methods and assets from the first package. Source hashes describe the original source, not a claim that adapted text is identical.

## Product Manager Skills: what was reused

Dean Peters's methods are reused substantially in Project Setup, Research, Site Architecture and Presentations. Twelve central methods support everyday website work; five more are conditional techniques inside those skills rather than separate mandatory steps.

| Original method | HaloSkill destination | Reuse |
|---|---|---|
| incoming-request-advisor | Project Setup | Separate literal request, underlying problem and constraints |
| problem-statement | Project Setup | Audience, job, evidenced barrier and consequence |
| jobs-to-be-done | Project Setup / Research | Functional/social/emotional jobs where evidence supports them |
| autonomous-investigation | Research | Bounded questions, source collection, stopping rule, uncertainty |
| competitive-research-snapshot | Research | Decision-focused competitor comparison |
| voice-of-customer-miner | Research | Traceable quotes, themes, objections and switching triggers |
| customer-journey-map | Research / Site Architecture | Scenario, touchpoints, actions, friction and evidence |
| prioritization-advisor | Project Setup | Choose prioritization based on available evidence |
| prd-development | Project Setup | Lightweight requirements; full PRD when complexity warrants |
| user-story | Project Setup | Actor/action/outcome and testable acceptance examples |
| user-story-mapping | Project Setup / Site Architecture | Journey backbone and coherent release slices |
| user-story-splitting | Project Setup | Smaller end-to-end outcomes and uncertainty reduction |
| opportunity-solution-tree | Project Setup, conditional | Outcome → evidenced opportunities → solutions → tests |
| pol-probe | Project Setup, conditional | Cheap falsifiable test with decision thresholds |
| discovery-process | Project Setup, conditional | Broader product discovery when contracted |
| roadmap-planning | Project Setup, conditional | Outcome sequencing; timeline calculation stays separate |
| storyboard | Presentations, conditional | Explain a user scenario without fabricating outcomes |

Fixed option menus, forced ASCII output, and rigid story formatting are not carried over. Methods are adapted to the current task and user authorization. Prioritization does not invent numeric evidence, and a storyboard is not research proof.

## Why these sources won

| Area | Primary basis | Supporting material / overlap decision |
|---|---|---|
| PM and delivery | Dean Peters + Owl UX PGM | Dean supplies problem/requirement methods; Owl supplies practical intake, delivery, risks, dependencies and status tables |
| Leadership | Five relevant Owl methods | Decision framework, delegation model, conflict resolution, review at scale, executive narrative; no whole org-management suite |
| Research | Existing synthesis + Dean's investigation/competitor/VoC methods | Corey adds customer/marketing depth; Brand-building adds visual competitor lens; lu90 adds evidence discipline |
| Industry research | lu90 evidence protocol | 147356 package not duplicated; no third-party industry reports imported |
| Site architecture | Corey Haines | Dean journey mapping and story mapping complement sitemap/navigation work |
| Copywriting | Corey writing and editing | Brand voice/messaging modes + Miki fact-preserving editing; one entry point, no competing briefs |
| Brand strategy | Brand-building positioning | Optional only when positioning is in scope |
| Visual concepts | Retained design-taste method | Preserve the existing design base; no additional mandatory concept engines |
| Build, animation, Storybook, QA | User's Next.js starter | Replace duplicate Halo wrappers; do not bundle the starter again |
| Sitemap vs canvas | Site Architecture / Design Canvas | Initial structure and captured-page review are different jobs |
| Presentation | Retained Halo templates/assets | One entry point with proposal, concept and review modes |
| Reference formatting | Owl Listener designer-skills | README/catalog/command tables as presentation inspiration; no extra skill imports |
| Design-context-for-ai | Audited, not packaged | Optional snapshot/context ideas do not justify another mandatory workflow |

## Adapted source map

| Source skill | Destination | Pinned source |
|---|---|---|
| `incoming-request-advisor` | `haloskill-project-setup` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/incoming-request-advisor/SKILL.md) |
| `problem-statement` | `haloskill-project-setup` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/problem-statement/SKILL.md) |
| `jobs-to-be-done` | `haloskill-project-setup` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/jobs-to-be-done/SKILL.md) |
| `prioritization-advisor` | `haloskill-project-setup` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/prioritization-advisor/SKILL.md) |
| `prd-development` | `haloskill-project-setup` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/prd-development/SKILL.md) |
| `user-story` | `haloskill-project-setup` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/user-story/SKILL.md) |
| `user-story-mapping` | `haloskill-project-setup` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/user-story-mapping/SKILL.md) |
| `user-story-splitting` | `haloskill-project-setup` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/user-story-splitting/SKILL.md) |
| `opportunity-solution-tree` | `haloskill-project-setup` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/opportunity-solution-tree/SKILL.md) |
| `pol-probe` | `haloskill-project-setup` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/pol-probe/SKILL.md) |
| `discovery-process` | `haloskill-project-setup` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/discovery-process/SKILL.md) |
| `roadmap-planning` | `haloskill-project-setup` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/roadmap-planning/SKILL.md) |
| `autonomous-investigation` | `haloskill-research` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/autonomous-investigation/SKILL.md) |
| `competitive-research-snapshot` | `haloskill-research` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/competitive-research-snapshot/SKILL.md) |
| `voice-of-customer-miner` | `haloskill-research` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/voice-of-customer-miner/SKILL.md) |
| `jobs-to-be-done` | `haloskill-research` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/jobs-to-be-done/SKILL.md) |
| `customer-journey-map` | `haloskill-research` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/customer-journey-map/SKILL.md) |
| `customer-journey-map` | `haloskill-site-architecture` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/customer-journey-map/SKILL.md) |
| `user-story-mapping` | `haloskill-site-architecture` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/user-story-mapping/SKILL.md) |
| `storyboard` | `haloskill-presentations` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/blob/1b5a524ebb95e9497fa3f25002d8b8ec528d4444/skills/storyboard/SKILL.md) |
| `customer-research` | `haloskill-research` | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/5e721d73ac85be8ba917d6a9ca9cb5bc98f02b80/skills/customer-research/SKILL.md) |
| `competitor-profiling` | `haloskill-research` | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/5e721d73ac85be8ba917d6a9ca9cb5bc98f02b80/skills/competitor-profiling/SKILL.md) |
| `site-architecture` | `haloskill-site-architecture` | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/5e721d73ac85be8ba917d6a9ca9cb5bc98f02b80/skills/site-architecture/SKILL.md) |
| `copywriting` | `haloskill-copywriting` | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/5e721d73ac85be8ba917d6a9ca9cb5bc98f02b80/skills/copywriting/SKILL.md) |
| `copy-editing` | `haloskill-copywriting` | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/5e721d73ac85be8ba917d6a9ca9cb5bc98f02b80/skills/copy-editing/SKILL.md) |
| `product-marketing` | `haloskill-copywriting` | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/5e721d73ac85be8ba917d6a9ca9cb5bc98f02b80/skills/product-marketing/SKILL.md) |
| `seo-audit` | `haloskill-seo-audit` | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/5e721d73ac85be8ba917d6a9ca9cb5bc98f02b80/skills/seo-audit/SKILL.md) |
| `analytics` | `haloskill-analytics` | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/5e721d73ac85be8ba917d6a9ca9cb5bc98f02b80/skills/analytics/SKILL.md) |
| `competitor-branding` | `haloskill-research` | [arnabbagxd/Brand-building-skills](https://github.com/arnabbagxd/Brand-building-skills/blob/4a0a8b5b7a0f64bf0fc551978a18a591670a5223/skills/competitor-branding/SKILL.md) |
| `brand-voice` | `haloskill-copywriting` | [arnabbagxd/Brand-building-skills](https://github.com/arnabbagxd/Brand-building-skills/blob/4a0a8b5b7a0f64bf0fc551978a18a591670a5223/skills/brand-voice/SKILL.md) |
| `brand-messaging` | `haloskill-copywriting` | [arnabbagxd/Brand-building-skills](https://github.com/arnabbagxd/Brand-building-skills/blob/4a0a8b5b7a0f64bf0fc551978a18a591670a5223/skills/brand-messaging/SKILL.md) |
| `brand-positioning` | `haloskill-brand-positioning` | [arnabbagxd/Brand-building-skills](https://github.com/arnabbagxd/Brand-building-skills/blob/4a0a8b5b7a0f64bf0fc551978a18a591670a5223/skills/brand-positioning/SKILL.md) |
| `intake-process` | `haloskill-project-setup` | [Owl-Listener/ux-pgm-skills](https://github.com/Owl-Listener/ux-pgm-skills/blob/c6a0a117b2c394834d5c39ef62e8d33ea1465f5a/cross-functional-alignment/skills/intake-process/SKILL.md) |
| `scoping-framework` | `haloskill-project-setup` | [Owl-Listener/ux-pgm-skills](https://github.com/Owl-Listener/ux-pgm-skills/blob/c6a0a117b2c394834d5c39ef62e8d33ea1465f5a/program-planning/skills/scoping-framework/SKILL.md) |
| `delivery-plan` | `haloskill-project-setup` | [Owl-Listener/ux-pgm-skills](https://github.com/Owl-Listener/ux-pgm-skills/blob/c6a0a117b2c394834d5c39ef62e8d33ea1465f5a/delivery-execution/skills/delivery-plan/SKILL.md) |
| `dependency-map` | `haloskill-project-setup` | [Owl-Listener/ux-pgm-skills](https://github.com/Owl-Listener/ux-pgm-skills/blob/c6a0a117b2c394834d5c39ef62e8d33ea1465f5a/program-planning/skills/dependency-map/SKILL.md) |
| `risk-register` | `haloskill-project-setup` | [Owl-Listener/ux-pgm-skills](https://github.com/Owl-Listener/ux-pgm-skills/blob/c6a0a117b2c394834d5c39ef62e8d33ea1465f5a/delivery-execution/skills/risk-register/SKILL.md) |
| `status-report` | `haloskill-project-setup` | [Owl-Listener/ux-pgm-skills](https://github.com/Owl-Listener/ux-pgm-skills/blob/c6a0a117b2c394834d5c39ef62e8d33ea1465f5a/stakeholder-comms/skills/status-report/SKILL.md) |
| `decision-log` | `haloskill-project-setup` | [Owl-Listener/ux-pgm-skills](https://github.com/Owl-Listener/ux-pgm-skills/blob/c6a0a117b2c394834d5c39ef62e8d33ea1465f5a/cross-functional-alignment/skills/decision-log/SKILL.md) |
| `launch-readiness` | `haloskill-handoff` | [Owl-Listener/ux-pgm-skills](https://github.com/Owl-Listener/ux-pgm-skills/blob/c6a0a117b2c394834d5c39ef62e8d33ea1465f5a/delivery-execution/skills/launch-readiness/SKILL.md) |
| `decision-framework` | `haloskill-project-setup` | [Owl-Listener/design-leadership-skills](https://github.com/Owl-Listener/design-leadership-skills/blob/9b801db464b25c73e709a77a358854eac43a4937/operating-cadence/skills/decision-framework/SKILL.md) |
| `delegation-model` | `haloskill-project-setup` | [Owl-Listener/design-leadership-skills](https://github.com/Owl-Listener/design-leadership-skills/blob/9b801db464b25c73e709a77a358854eac43a4937/operating-cadence/skills/delegation-model/SKILL.md) |
| `conflict-resolution` | `haloskill-project-setup` | [Owl-Listener/design-leadership-skills](https://github.com/Owl-Listener/design-leadership-skills/blob/9b801db464b25c73e709a77a358854eac43a4937/leadership-craft/skills/conflict-resolution/SKILL.md) |
| `design-review-at-scale` | `haloskill-design-review` | [Owl-Listener/design-leadership-skills](https://github.com/Owl-Listener/design-leadership-skills/blob/9b801db464b25c73e709a77a358854eac43a4937/operating-cadence/skills/design-review-at-scale/SKILL.md) |
| `executive-narrative` | `haloskill-presentations` | [Owl-Listener/design-leadership-skills](https://github.com/Owl-Listener/design-leadership-skills/blob/9b801db464b25c73e709a77a358854eac43a4937/org-influence/skills/executive-narrative/SKILL.md) |
| `ai-copywriter` | `haloskill-copywriting` | [mikiarlo3/ai-copywriter](https://github.com/mikiarlo3/ai-copywriter/blob/08b53b1ad39887cd94cbaab61cac3b6aae2d8518/SKILL.md) |
| `industry-research` | `haloskill-research` | [lu90/industry-research-skill](https://github.com/lu90/industry-research-skill/blob/590776790827f193da17bbc39df1fa07748f198a/skills/industry-research/SKILL.md) |

## User materials and retained assets

- `workshop-client-research` → `haloskill-workshop-client-research`.
- `workshop-script-writer` → `haloskill-workshop-script-writer`.
- `roadmap-to-timeline.skill` → adapted timeline instructions plus a new deterministic Python calculator. The original archive was an instruction package, not executable automation. Its hashes are recorded in [user-timeline.json](../sources/user-timeline.json).
- Existing Halo proposal/sales assets and visual references remain under Presentations modes. Template estimates and historic permissions do not apply automatically to a new client.
- Existing detailed methods/resources for Concepts, Interface Design, Figma Library, Code Connect, Design Debt, Research, Design Review and Handoff remain available through progressive references.

Third-party materials retain their source terms. Adaptation and public repository access do not change ownership or grant a common license to everything. The [HaloSkill Project Use License](../LICENSE.md) covers only original materials owned by maisjandesign and excludes materials subject to upstream licensing obligations. See [the notices](../LICENSE-NOTICE.md) and retained [upstream license files](../sources/licenses).
