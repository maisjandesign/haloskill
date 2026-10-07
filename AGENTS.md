# HaloSkill repository

This is a private studio skill collection. Keep every skill's name and folder under `haloskill-*`; UI titles use `HaloSkill — …`.
Preserve the two Workshop skills as rename-only imports unless the user explicitly requests content edits. Their supporting references are source context, not repository-wide instructions.
Keep source attribution and snapshot hashes in `sources/manifest.json`. Do not change license claims without evidence. Provider runtimes, secrets and client project data do not belong in this repository.
Read only the skill and supporting files relevant to the task. Avoid overlapping automatic triggers. Run `python3 scripts/validate.py` after changes and installer smoke tests when changing installation.
