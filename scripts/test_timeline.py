#!/usr/bin/env python3
import importlib.util
import unittest
import subprocess
import sys
import tempfile
import json
from pathlib import Path

path = Path(__file__).resolve().parents[1] / 'plugins/haloskill/skills/haloskill-roadmap-to-timeline/scripts/schedule.py'
spec = importlib.util.spec_from_file_location('schedule', path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class TimelineTests(unittest.TestCase):
    def base(self):
        return {'start': '2026-10-09', 'items': [{'id':'a', 'min':8, 'max':16, 'unit':'hours'}]}

    def test_weekend_and_holiday(self):
        data = self.base()
        data['holidays'] = ['2026-10-12']
        self.assertEqual(module.calculate(data)['end'], '2026-10-13')

    def test_start_on_weekend(self):
        data = self.base(); data['start'] = '2026-10-10'
        self.assertEqual(module.calculate(data)['start'], '2026-10-12')

    def test_review_and_milestone(self):
        data = self.base()
        data['items'] += [{'id':'review', 'kind':'review', 'min':2, 'max':2, 'unit':'days', 'depends_on':['a']}, {'id':'demo', 'kind':'milestone', 'max':0}]
        result = module.calculate(data)
        self.assertEqual(result['end'], '2026-10-14')
        self.assertEqual(result['items'][-1]['working_days'], 0)
        self.assertEqual(result['work_estimate_hours'], {'min':8, 'max':16})

    def test_rounding_and_capacity(self):
        data = self.base(); data['hours_per_day'] = 6; data['items'][0]['max'] = 13
        self.assertEqual(module.calculate(data)['end'], '2026-10-13')

    def test_cli_preserves_estimate(self):
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary) / 'estimate.json'
            source.write_text(json.dumps(self.base()))
            before = source.read_bytes()
            process = subprocess.run([sys.executable, str(path), '--input', str(source), '--output', str(source)], capture_output=True)
            self.assertNotEqual(process.returncode, 0)
            self.assertEqual(source.read_bytes(), before)
            output = Path(temporary) / 'timeline.json'
            process = subprocess.run([sys.executable, str(path), '--input', str(source), '--output', str(output)], capture_output=True)
            self.assertEqual(process.returncode, 0, process.stderr)
            self.assertEqual(json.loads(output.read_text())['end'], '2026-10-12')
            self.assertEqual(source.read_bytes(), before)

    def test_invalid_inputs(self):
        mutations = [lambda d:d.update(hours_per_day=0), lambda d:d.update(mode='parallel'),
                     lambda d:d.update(expected_work_hours={'min':8,'max':17}),
                     lambda d:d['items'][0].update(depends_on=['a']),
                     lambda d:d['items'][0].update(unit='weeks'),
                     lambda d:d['items'][0].update(min=20),
                     lambda d:d['items'][0].update(max=float('nan')),
                     lambda d:d['items'][0].update(parallel_workers=2),
                     lambda d:d['items'].append(dict(d['items'][0])),
                     lambda d:d['items'][0].update(kind='milestone')]
        for change in mutations:
            data = self.base(); change(data)
            with self.subTest(data=data), self.assertRaises(ValueError):module.calculate(data)

if __name__ == '__main__':unittest.main()
