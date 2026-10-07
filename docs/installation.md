# Installation

Requires Python 3.9+, a private GitHub repository checkout, and an existing target project. Installation copies skill instructions/resources; it does not install Node dependencies, providers, browser tools, Notion or Figma connections.

```bash
git clone https://github.com/maisjandesign/haloskill.git
cd haloskill
python3 scripts/install.py --project /path/to/project --dry-run
python3 scripts/install.py --project /path/to/project
```

## Profiles and selection

| Option | Result |
|---|---|
| Default / `--profile core` | 13 core skills |
| `--profile optional` | 9 optional specialists only |
| `--profile all` | All 22 skills |
| `--skill haloskill-design-canvas` | Only that skill; repeat the option to select several |
| `--user` instead of `--project …` | Install into `~/.agents/skills` |
| `--dry-run` | Check conflicts and show the plan without writing |

Explicit `--skill` names override the profile. Unknown names fail before writing. Start a new Codex chat after installing. Optional skills do not automatically install their external runtimes or the core profile.

## Existing installations

Identical skills are left unchanged. A differing file, directory or symlink at any selected destination blocks that installation before copying. Local edits are never silently overwritten. To upgrade v0.1, back up existing HaloSkill directories, review [the migration table](migration.md), and move only the old directories you intend to replace outside all skill discovery roots. Then install v0.2 and deliberately reapply any local customizations. Do not keep old and new active entry points with overlapping triggers.

The installer does not delete retired skills. Git history retains the previous package; the migration is intentional rather than an automatic destructive cleanup. User-wide and project-local copies can overlap, so choose one scope for this family.

## Plugin packaging

The repository retains its plugin manifest and local marketplace descriptor. The single HaloSkill plugin contains all 22 entry points; core/optional selection belongs to the Python installer. Use the actual plugin interface supported by your Codex version, or use the project-local installation above. Do not assume Claude-specific slash/plugin commands work in Codex. This release validates package metadata; marketplace installation was not exercised in a fresh Codex profile.
