#!/usr/bin/env python3
"""Calculate a conservative serial schedule. No external services or dependencies."""
import argparse
import datetime as dt
import json
import math
from pathlib import Path


def number(value, label, positive=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(label + ' must be a finite number')
    if value < 0 or (positive and value == 0):
        raise ValueError(label + ' must be ' + ('positive' if positive else 'nonnegative'))
    return value


def calculate(data):
    if data.get('mode', 'serial') != 'serial':
        raise ValueError('Only serial scheduling is supported; model parallel capacity separately')
    if any(k in data for k in ('workers', 'parallel_workers', 'capacity', 'dependencies')):
        raise ValueError('Global capacity/dependency overrides are unsupported')
    start = dt.date.fromisoformat(data['start'])
    hours = number(data.get('hours_per_day', 8), 'hours_per_day', True)
    holidays = {dt.date.fromisoformat(day) for day in data.get('holidays', [])}
    items = data['items']
    if not isinstance(items, list) or not items:
        raise ValueError('items must be a nonempty list')

    def working(day):
        while day.weekday() >= 5 or day in holidays:
            day += dt.timedelta(days=1)
        return day

    cursor = working(start)
    result, seen, min_hours, max_hours = [], set(), 0, 0
    for item in items:
        item_id = item['id']
        if not isinstance(item_id, str) or not item_id.strip() or item_id in seen:
            raise ValueError('Every item needs a unique nonempty string id')
        if any(k in item for k in ('workers', 'parallel_workers', 'capacity', 'hours_per_day')):
            raise ValueError('Per-item capacity is unsupported; provide productive effort for one serial lane')
        dependencies = item.get('depends_on', [])
        if not isinstance(dependencies, list) or not all(isinstance(d, str) and d in seen for d in dependencies):
            raise ValueError(item_id + ': dependencies must reference earlier items in this serial schedule')
        kind = item.get('kind', 'work')
        if kind not in ('work', 'review', 'milestone'):
            raise ValueError(item_id + ': unknown kind')
        low, high = number(item.get('min', 0), item_id + ' min'), number(item['max'], item_id + ' max')
        if low > high:
            raise ValueError(item_id + ': min exceeds max')
        unit = item.get('unit', 'hours')
        if unit not in ('hours', 'days'):
            raise ValueError(item_id + ': unit must be hours or days')
        if kind == 'milestone' and (low != 0 or high != 0):
            raise ValueError(item_id + ': milestones must have zero effort')
        if kind != 'milestone' and high == 0:
            raise ValueError(item_id + ': zero-duration items must be milestones')
        if kind == 'review' and unit != 'days':
            raise ValueError(item_id + ': review windows must use working days')
        factor = hours if unit == 'days' else 1
        if kind == 'work':
            min_hours += low * factor
            max_hours += high * factor
        duration = math.ceil(high * factor / hours)
        if kind == 'milestone':
            begin = end = dt.date.fromisoformat(result[-1]['end']) if result else cursor
        else:
            begin = end = cursor
            for _ in range(duration - 1):
                end = working(end + dt.timedelta(days=1))
            cursor = working(end + dt.timedelta(days=1))
        result.append(dict(item, kind=kind, unit=unit, start=begin.isoformat(), end=end.isoformat(), working_days=duration))
        seen.add(item_id)
    supplied = data.get('expected_work_hours')
    if supplied is not None:
        for key, actual in [('min', min_hours), ('max', max_hours)]:
            expected = number(supplied[key], 'expected_work_hours.' + key)
            if not math.isclose(expected, actual, abs_tol=0.000001):
                raise ValueError('Work estimate totals do not reconcile: ' + key)
    return {'source_version': data.get('source_version', 'unspecified'), 'status': 'Draft — PM review required',
            'mode': 'serial', 'hours_per_day': hours, 'holidays': sorted(data.get('holidays', [])),
            'assumptions': ['Monday–Friday working week', 'Maximum effort rounded up per item',
                            'One serial delivery lane; no resource optimization', 'Review windows are elapsed working days, not work effort'],
            'work_estimate_hours': {'min': min_hours, 'max': max_hours},
            'start': result[0]['start'], 'end': result[-1]['end'], 'items': result}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output', type=Path, help='JSON file; defaults to stdout')
    args = parser.parse_args()
    if args.output and args.input.resolve() == args.output.resolve():
        parser.error('Output must not overwrite the source estimate')
    try:
        result = calculate(json.loads(args.input.read_text()))
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.error(str(error))
    text = json.dumps(result, indent=2, ensure_ascii=False) + '\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
