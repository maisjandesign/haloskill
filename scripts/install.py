#!/usr/bin/env python3
"""Install the family without overwriting existing skills. Standard library only."""
import argparse
import hashlib
import json
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'plugins/haloskill/skills'

def snapshot(folder):
    return {str(p.relative_to(folder)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(folder.rglob('*')) if p.is_file() and p.name != '.DS_Store'}

def install(destination, dry_run=False, profile='core', names=None):
    catalog = json.loads((ROOT / 'catalog.json').read_text())['skills']
    known = {r['name']: r for r in catalog}
    if profile not in ('core', 'optional', 'all'):
        raise ValueError('Unknown profile: ' + profile)
    if names and set(names) - set(known):
        raise ValueError('Unknown skills: ' + ', '.join(sorted(set(names) - set(known))))
    selected = set(names) if names else {n for n, r in known.items() if profile == 'all' or r['profile'] == profile}
    skills = [SOURCE / name for name in sorted(selected)]
    planned, unchanged, conflicts = [], [], []
    for src in skills:
        dst = destination / src.name
        if dst.is_symlink():
            conflicts.append(str(dst) + ' (symlink)')
        elif dst.exists():
            if dst.is_dir() and snapshot(src) == snapshot(dst):
                unchanged.append(src.name)
            else:
                conflicts.append(str(dst))
        else:
            planned.append((src, dst))
    if conflicts:
        print('Nothing installed. Existing different skills:\n' + '\n'.join(conflicts), file=sys.stderr)
        return 2
    print(f'Destination: {destination}\nNew: {len(planned)}; identical: {len(unchanged)}')
    if dry_run:
        for src, dst in planned:
            print(f'Would copy {src.name} -> {dst}')
        return 0
    destination.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.haloskill-stage-', dir=destination) as staging:
        staged = []
        for src, dst in planned:
            temporary = Path(staging) / src.name
            shutil.copytree(src, temporary)
            staged.append((temporary, dst))
        for temporary, dst in staged:
            if dst.exists() or dst.is_symlink():
                raise RuntimeError(f'Destination changed during installation: {dst}')
            temporary.rename(dst)
    print('Installed. Start a new Codex chat in the target project to load these skills.')
    return 0

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--project', type=Path, help='Existing project root; installs into .agents/skills')
    mode.add_argument('--user', action='store_true', help='Install into ~/.agents/skills')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--profile', choices=['core', 'optional', 'all'], default='core')
    parser.add_argument('--skill', action='append', dest='names', help='Exact skill name; repeat to select several. Overrides profile.')
    args = parser.parse_args()
    if args.project:
        project = args.project.expanduser().resolve()
        if not project.is_dir():
            parser.error('--project must name an existing directory')
        destination = project / '.agents/skills'
    else:
        destination = Path.home() / '.agents/skills'
    try:
        return install(destination, args.dry_run, args.profile, args.names)
    except ValueError as error:
        parser.error(str(error))

if __name__ == '__main__':
    raise SystemExit(main())
