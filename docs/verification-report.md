# Verification report — v0.2.0

Verified locally on 2026-10-07 with Python 3.9.

| Check | Result | Scope |
|---|---|---|
| Package validator | PASS | 22 skill folders, 13 core / 9 optional, names, metadata, catalog, links, language guard and plugin paths |
| Workshop preservation | PASS | Original file hashes after reversing naming-only changes; both current trees unchanged from v0.1 |
| Official Skill Creator validator | PASS | All 22 SKILL.md files |
| Installer tests | PASS | Profiles, explicit selection, dry-run, repeat, invalid names, differing-file and symlink protection |
| Timeline tests | PASS | 6 tests, including invalid-input subcases and CLI source-preservation checks |
| Source map hashes | PASS | 47 mappings match audited source files |
| Retained presentation resources | PASS | All 22 proposal/sales assets and references preserved byte for byte |
| Git whitespace check | PASS | No whitespace errors in the release diff |

The timeline example is synthetic. The schedule uses maximum estimates, working-day rounding and one serial lane; it does not optimize staffing or infer holidays. The official format validator checks structure, not output quality.

External integrations were not exercised by this packaging release: fresh Codex plugin discovery, Next.js project setup/build/browser checks, Storybook, Figma actions, Notion writes, Design Canvas runtime/captures, CMS, analytics providers and deployment require a real target project. No client project or external service was created by this release.
