# Validation

From the repository root, using Python 3.9+:

```bash
python3 scripts/validate.py
python3 scripts/test_install.py
python3 scripts/test_timeline.py
python3 plugins/haloskill/skills/haloskill-roadmap-to-timeline/scripts/schedule.py --input plugins/haloskill/skills/haloskill-roadmap-to-timeline/assets/example.json
```

Package validation checks the catalog/manifest/folders, 13+9 profiles, names, descriptions, UI prompts, English-language Cyrillic guard, local Markdown links, author-machine path leakage, plugin path, and original Workshop content hashes after reversing naming changes. The language guard catches Cyrillic text; human review establishes English wording.

Installer tests use temporary directories: core/optional/selected installs, non-writing dry run, idempotent repeat, unknown skill rejection, differing-file protection and symlink protection. Timeline tests cover weekends, holidays, review windows, zero-duration milestones, capacity/rounding, estimate-total reconciliation and invalid inputs. No test connects external services or changes the user's global skill installation.

## Manual and integration checks

Review each entry point's triggers and scope, source traceability, old-name migration, actual retained template assets, and realistic handoffs. For a client project separately test the chosen provider, Next.js setup/build/browser behavior, Storybook, CMS/forms, Notion operations, Figma actions, Canvas captures and deployment. Structural validation cannot establish skill output quality or integration readiness.

The Skill Creator `quick_validate.py` can additionally validate every SKILL.md when that tool and PyYAML are available. It is not bundled as a new dependency here. See the release's [verification report](verification-report.md) for checks actually performed.
