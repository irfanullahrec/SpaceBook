"""Applies printed-text patches to the page files of a generated book and writes them to fix/pNNN.txt (the folder gen.py reads, so a rebuild keeps them).
    python -X utf8 tools/launch/page_patch.py <book dir> <patches.py>
  <book dir>   relative to docs/source-verification, e.g. class-9/eng or class-9/pakstudy (it holds pages/ and fix/)
  <patches.py> defines PATCHES = {'p014': [(op, anchor, payload), ...]}
Operations (anchor = the start of exactly one line of the page; every anchor problem is printed and counted):
  ('rep',    anchor, 'new line')            replace that line
  ('before', anchor, ['line', ...])         insert lines before it
  ('after',  anchor, ['line', ...])         insert lines after it
  ('cut',    anchor, end_anchor)            delete from that line up to (not including) the end_anchor line
  ('top',    None,   ['line', ...])         insert after the leading @ lines
  ('end',    None,   ['line', ...])         append
A page that already has a fix file is patched there, otherwise pages/pNNN.txt is copied to fix/ and patched. Line endings of the file are kept.
Afterwards: python -X utf8 <book dir>/gen.py, then the book's builder (see tools/launch/wire_here.js).
Dev-only, never shipped."""
import sys, importlib.util, os

SV = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'docs', 'source-verification')


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    book = os.path.join(SV, sys.argv[1])
    spec = importlib.util.spec_from_file_location('patches', sys.argv[2])
    pm = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(pm)
    bad = 0
    for page, ops in pm.PATCHES.items():
        fix = os.path.join(book, 'fix', page + '.txt')
        src = fix if os.path.exists(fix) else os.path.join(book, 'pages', page + '.txt')
        raw = open(src, encoding='utf-8', newline='').read()
        eol = '\r\n' if '\r\n' in raw else '\n'
        lines = raw.replace('\r\n', '\n').split('\n')
        if lines and lines[-1] == '':
            lines.pop()
        for op, anchor, payload in ops:
            if op == 'top':
                i = 0
                while i < len(lines) and lines[i].startswith('@'):
                    i += 1
                lines[i:i] = payload
                continue
            if op == 'end':
                lines.extend(payload)
                continue
            a = [i for i, l in enumerate(lines) if l.startswith(anchor)]
            if len(a) != 1:
                print('ANCHOR PROBLEM', page, op, repr(anchor), 'matches', len(a))
                bad += 1
                continue
            i = a[0]
            if op == 'rep':
                lines[i] = payload
            elif op == 'before':
                lines[i:i] = payload
            elif op == 'after':
                lines[i + 1:i + 1] = payload
            elif op == 'cut':
                b = [j for j, l in enumerate(lines) if l.startswith(payload)]
                if len(b) != 1 or b[0] <= i:
                    print('CUT END PROBLEM', page, repr(payload), b)
                    bad += 1
                else:
                    del lines[i:b[0]]
            else:
                print('UNKNOWN OPERATION', op)
                bad += 1
        os.makedirs(os.path.dirname(fix), exist_ok=True)
        open(fix, 'w', encoding='utf-8', newline='').write(eol.join(lines) + eol)
        print('patched', page, len(ops), 'operations')
    print('problems:', bad)
    return 1 if bad else 0


sys.exit(main())
