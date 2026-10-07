#!/usr/bin/env python3
"""Check install, repeat, collision and dry-run without changing user configuration."""
import importlib.util
import tempfile
from pathlib import Path

spec = importlib.util.spec_from_file_location('haloskill_install', Path(__file__).with_name('install.py'))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

with tempfile.TemporaryDirectory(prefix='haloskill-install-test-') as tmp:
    root = Path(tmp)
    dry = root / 'dry/.agents/skills'
    assert module.install(dry, True) == 0
    assert not dry.exists(), 'Dry-run must not write'
    dest = root / 'real/.agents/skills'
    assert module.install(dest) == 0
    assert len(list(dest.glob('haloskill-*/SKILL.md'))) == 13
    first = module.snapshot(dest)
    assert module.install(dest) == 0
    assert module.snapshot(dest) == first, 'Repeat changed installed files'
    assert module.install(dest, profile='optional') == 0
    assert len(list(dest.glob('haloskill-*/SKILL.md'))) == 22
    one = root / 'one'
    assert module.install(one, names=['haloskill-design-canvas']) == 0
    assert sorted(p.name for p in one.iterdir()) == ['haloskill-design-canvas']
    invalid = root / 'invalid'
    try:
        module.install(invalid, names=['haloskill-missing'])
        raise AssertionError('Unknown skill accepted')
    except ValueError:
        assert not invalid.exists()
    link = root / 'symlinks'
    link.mkdir()
    (link / 'haloskill-start').symlink_to(root / 'missing')
    assert module.install(link) == 2
    assert len(list(link.iterdir())) == 1
    existing = dest / 'haloskill-research/SKILL.md'
    existing.write_text('user changes\n')
    before = module.snapshot(dest)
    assert module.install(dest) == 2
    assert module.snapshot(dest) == before, 'Conflict modified existing skills'
    collision = root / 'collision/.agents/skills'
    collision.mkdir(parents=True)
    (collision / 'haloskill-start').write_text('existing file')
    assert module.install(collision) == 2
    assert len(list(collision.iterdir())) == 1, 'Conflict produced partial install'
print('PASS: core/optional/selected profiles, dry-run, repeat, unknown names, symlinks and conflict protection')
