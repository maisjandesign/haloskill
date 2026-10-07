#!/usr/bin/env python3
"""Validate HaloSkill package structure, local references and Workshop invariants."""
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / 'plugins/haloskill/skills'

def validate():
    errors = []
    manifest = json.loads((ROOT / 'sources/manifest.json').read_text())
    records = {r['name']: r for r in manifest['records']}
    catalog = json.loads((ROOT / 'catalog.json').read_text())['skills']
    if len(catalog) != len({r['name'] for r in catalog}) or {r['name'] for r in catalog} != set(records):
        errors.append('Catalog and manifest differ or contain duplicates')
    if sum(r['profile'] == 'core' for r in catalog) != 13 or sum(r['profile'] == 'optional' for r in catalog) != 9:
        errors.append('Expected 13 core and 9 optional skills')
    for row in catalog:
        if row['command'].split()[0] != '$' + row['name']:
            errors.append('Invalid command for ' + row['name'])
    for p in ROOT.rglob('*'):
        if p.is_file() and '.git' not in p.parts and p.suffix in ('.md', '.yaml', '.json', '.py'):
            if re.search(r'[\u0400-\u04ff]', p.read_text()):
                errors.append(str(p.relative_to(ROOT)) + ': non-English Cyrillic text')
    folders = {p.name: p for p in SKILLS.iterdir() if p.is_dir()}
    if set(records) != set(folders):
        errors.append('Manifest and skill directories differ')
    for name, folder in sorted(folders.items()):
        main = folder / 'SKILL.md'
        if not main.is_file():
            errors.append(f'{name}: missing SKILL.md')
            continue
        body = main.read_text()
        fm = re.match(r'^---\n(.*?)\n---\n', body, re.S)
        if not fm:
            errors.append(f'{name}: invalid frontmatter')
            continue
        declared = re.search(r'^name: (.+)$', fm[1], re.M)
        desc = re.search(r'^description: (.+)$', fm[1], re.M)
        if not declared or declared[1] != name or not re.fullmatch(r'haloskill-[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
            errors.append(f'{name}: invalid or mismatched name')
        if not desc or len(desc[1]) < 15 or len(desc[1]) > 1024:
            errors.append(f'{name}: missing or oversized description')
        ui = folder / 'agents/openai.yaml'
        if not ui.is_file():
            errors.append(f'{name}: missing UI metadata')
        else:
            text = ui.read_text()
            if f'${name}' not in text or 'display_name: "HaloSkill — ' not in text:
                errors.append(f'{name}: invalid UI name or prompt')
        if records[name]['mode'] == 'rename-only':
            source_name = records[name]['original']
            for entry in records[name]['files']:
                p = folder / entry['path']
                if not p.is_file():
                    errors.append(f'{name}: missing Workshop file {entry["path"]}')
                    continue
                content = p.read_bytes()
                if entry['path'] in ['SKILL.md', 'agents/openai.yaml']:
                    text = content.decode()
                    for old in ['workshop-client-research','workshop-script-writer']:
                        text = text.replace('haloskill-'+old, old)
                    text = text.replace('# HaloSkill — Workshop Client Research','# Workshop client research')
                    text = text.replace('# HaloSkill — Workshop Script Writer','# Workshop script writer')
                    text = text.replace('display_name: "HaloSkill — Workshop','display_name: "Workshop')
                    content = text.encode()
                if hashlib.sha256(content).hexdigest() != entry['sha256']:
                    errors.append(f'{name}: Workshop content changed beyond naming: {entry["path"]}')
    for p in ROOT.rglob('*.md'):
        if '.git' in p.parts:
            continue
        text = p.read_text()
        if re.search(r'/(?:Users|home)/[A-Za-z0-9._-]+/', text):
            errors.append(f'{p.relative_to(ROOT)}: author-machine path')
        # Only Markdown links, not code examples or prose naming external dependencies.
        for link in re.finditer(r'\[[^\]\n]+\]\(([^\s)]+)\)',text):
            target = link[1]
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            path = unquote(target.split('#')[0])
            if path and not (p.parent / path).exists():
                errors.append(f'{p.relative_to(ROOT)}: broken local link {target}')
    plugin = json.loads((ROOT / 'plugins/haloskill/plugin.json').read_text())
    market = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text())
    if plugin['name'] != 'haloskill' or not (ROOT / market['plugins'][0]['source']['path']).is_dir():
        errors.append('Invalid plugin or marketplace path')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'PASS: {len(folders)} skills; names, metadata, local links, plugin paths and rename-only Workshop checks.')
    return 0

if __name__ == '__main__':
    raise SystemExit(validate())
