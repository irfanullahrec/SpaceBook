"""Expand a compact glossary spec into page DSL tables.

Usage: python tools/gloss.py SPEC OUT [ur|ps]   (slot order of the book; default ur)
SPEC lines:
  @...                     copied verbatim (page metadata, @sec, @tab, #/## headings too)
  # ... / ## ...           copied verbatim
  H ur || en || ps         starts a new sub-table with a ### heading
  ur word = ur meaning || en word = en meaning || ps word = ps meaning
"""
import sys


HEADERS = {
    'ur': 'th الفاظ || Word || کلمه | معانی || Meaning || مانا',
    'ps': 'th کلمه || الفاظ || Word | مانا || معانی || Meaning',
}


def main():
    spec, out = sys.argv[1], sys.argv[2]
    header = HEADERS[sys.argv[3] if len(sys.argv) > 3 else 'ur']
    lines, open_tbl = [], False

    def close():
        nonlocal open_tbl
        if open_tbl:
            lines.append('endtable')
            open_tbl = False

    for raw in open(spec, encoding='utf-8').read().splitlines():
        s = raw.strip()
        if not s:
            continue
        if s.startswith('@') or s.startswith('#'):
            close()
            lines.append(s)
        elif s.startswith('H '):
            close()
            title = s[2:].strip()
            lines.append('### ' + title)
            lines.append('table ' + title)
            lines.append(header)
            open_tbl = True
        else:
            slots = [p.strip() for p in s.split('||')]
            if len(slots) != 3 or any('=' not in p for p in slots):
                raise SystemExit('bad row: ' + s)
            words = [p.split('=', 1)[0].strip() for p in slots]
            means = [p.split('=', 1)[1].strip() for p in slots]
            if not open_tbl:
                raise SystemExit('row before H: ' + s)
            lines.append('tr ' + ' || '.join(words) + ' | ' + ' || '.join(means))
    close()
    open(out, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    main()
