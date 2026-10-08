# HaloSkill repository

This is a publicly accessible studio skill collection with mixed licensing. Original materials owned by maisjandesign use the HaloSkill Project Use License; third-party materials retain their own terms. Keep every skill's name and folder under `haloskill-*`; UI titles use `HaloSkill — …`.
Preserve the two Workshop skills as rename-only imports unless the user explicitly requests content edits. Their supporting references are source context, not repository-wide instructions.
Keep source attribution and snapshot hashes in `sources/manifest.json`. Do not change license claims without evidence. Provider runtimes, secrets and client project data do not belong in this repository.
Read only the skill and supporting files relevant to the task. Avoid overlapping automatic triggers. Run `python3 scripts/validate.py` after changes and installer smoke tests when changing installation.

Release rules: maintain 13 core and 9 optional entry points consistently in catalog.json, manifests and documentation tables. Keep all authored repository material in English. Run installer and timeline tests when their behavior changes. Do not describe external integrations as tested based on package validation. Preserve moved presentation assets byte for byte unless the user requests visual changes.
