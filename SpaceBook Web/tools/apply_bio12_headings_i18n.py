# -*- coding: utf-8 -*-
"""Apply Urdu/Pashto section-heading translations to js/biology_12_data.js.

Reads every tools/i18n/bio12_headings_*.json part file, maps them onto the
section headings (number prefix and trailing ':' ignored, case insensitive)
and fills headingUrdu / urduTitle / headingPashto for each section.

Usage:  python apply_bio12_headings_i18n.py [--dry-run]
"""
import json, glob, os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
I18N_DIR = os.path.join(BASE, 'tools', 'i18n')
OUT_JS = os.path.join(BASE, 'js', 'biology_12_data.js')
DRY = '--dry-run' in sys.argv

PREFIX_RE = re.compile(r'^\d+(\.\d+)*\s*')


def norm(title):
    t = PREFIX_RE.sub('', title or '')
    t = t.rstrip(':').strip()
    return re.sub(r'\s+', ' ', t).lower()


def main():
    table = {}
    for path in sorted(glob.glob(os.path.join(I18N_DIR, 'bio12_headings_*.json'))):
        with open(path, encoding='utf-8') as f:
            part = json.load(f)
        for k, v in part.items():
            n = norm(k)
            if not n:
                continue
            if n in table and table[n] != v:
                print(f'CONFLICT {n!r}: {table[n]} vs {v}')
            table[n] = v
        print(f'  loaded {os.path.basename(path)}: {len(part)} entries')
    print(f'total translation entries: {len(table)}')

    with open(OUT_JS, encoding='utf-8') as f:
        raw = f.read()
    head = raw[:raw.index('[')]
    tail = raw[raw.rindex('];') + 1:]
    data = json.loads(raw[raw.index('['):raw.rindex(']') + 1])

    used = set()
    filled = missing = 0
    missing_titles = []
    for ch in data:
        for sec in ch['sections']:
            key = norm(sec['heading'])
            entry = table.get(key) if key else None
            if entry is None:
                missing += 1
                missing_titles.append((ch['number'], sec['heading']))
                continue
            used.add(key)
            sec['headingUrdu'], sec['headingPashto'] = entry[0], entry[1]
            sec['urduTitle'] = entry[0]
            filled += 1

    print(f'sections filled={filled} missing={missing}')
    for chn, h in missing_titles:
        print(f'  MISSING ch{chn}: {h!r}')
    unused = sorted(set(table) - used)
    if unused:
        print(f'unused entries ({len(unused)}): {unused[:10]}')

    if DRY or missing:
        print('dry-run or missing entries -> not writing')
        return

    out = head + json.dumps(data, ensure_ascii=False, indent=2) + tail
    with open(OUT_JS, 'w', encoding='utf-8', newline='\n') as f:
        f.write(out)
    print(f'wrote {OUT_JS} ({len(out.encode("utf-8")):,} bytes)')


if __name__ == '__main__':
    main()
