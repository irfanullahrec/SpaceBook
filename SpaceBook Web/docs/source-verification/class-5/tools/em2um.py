"""Draft a Social Studies UM page from the matching EM page (same printed page), with slots reordered to UR || EN || PS.

Usage:
  python tools/em2um.py J            draft sstum/pages/pJJJ.txt from sst/pages/p(J-2).txt and list its lines (EN preview)
  python tools/em2um.py J --show     only list the lines of the existing UM draft
  python tools/em2um.py J --fix F    apply fixes file F to sstum/pages/pJJJ.txt, then list
Fixes file lines (tab separated):
  N<TAB>text      replace the Urdu (first) slot of line N with text (for sol lines: the answer before ##)
  N<TAB>!line     replace the whole line N
  N<TAB>+line     insert a new line after line N (several + lines for the same N keep their order)
  N<TAB>-         delete line N
  0<TAB>+line     insert at the very top
EM printed page p is at EM JPG p+3; UM JPG = EM JPG + OFFSET (sstum/offset.txt; 2 before the duplicate JPG 010, then 3). --em K overrides the source page.
"""
import re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SEP = re.compile(r'\s*\|\|\s*')
OFFSET = int((HERE / 'sstum' / 'offset.txt').read_text().strip()) if (HERE / 'sstum' / 'offset.txt').exists() else 2
LABEL_OPS = {'box', '@sec', '@unit', 'q', 'qp'}


def swap3(s):
    parts = SEP.split(s)
    if len(parts) == 3:
        return ' || '.join([parts[1], parts[0], parts[2]])
    return s


def convert_line(line):
    op, _, rest = line.partition(' ')
    if '||' not in rest:
        return line
    if op == 'sol':
        ans, _, after = rest.partition(' ## ')
        slots = SEP.split(after)
        if len(slots) != 3:
            return line
        note, ur, ps = slots
        en = ans + (' — ' + note if note.strip() else '')
        return f'sol {ur.strip()} ## || {en.strip()} || {ps.strip()}'
    if op in ('th', 'tr'):
        lead = '| ' if rest.startswith('| ') else ''
        cells = (' ' + rest[len(lead):]).split(' | ')
        cells[0] = cells[0][1:]
        return op + ' ' + lead + ' | '.join(swap3(c) for c in cells)
    if op in LABEL_OPS:
        m = re.match(r'^([^|]*?) \| (.*)$', rest)
        if m and '||' not in m.group(1):
            return f'{op} {m.group(1)} | {swap3(m.group(2))}'
    return f'{op} {swap3(rest)}'


def draft(j, em=None):
    src = HERE / 'sst' / 'pages' / f'p{(em if em is not None else j - OFFSET):03d}.txt'
    out, in_svg = [], False
    for line in src.read_text(encoding='utf-8').splitlines():
        if in_svg:
            out.append(line)
            in_svg = not line.startswith('endsvg')
            continue
        if line.startswith('@issue'):
            continue
        if line.startswith('svg '):
            in_svg = True
        out.append(convert_line(line))
    return out


def first_slot(line):
    op, _, rest = line.partition(' ')
    if op == 'sol':
        return rest.partition(' ## ')[0]
    if op in LABEL_OPS:
        m = re.match(r'^([^|]*?) \| (.*)$', rest)
        if m:
            rest = m.group(2)
    return SEP.split(rest)[0]


def set_first(line, text):
    op, _, rest = line.partition(' ')
    if op in ('th', 'tr'):
        lead = '| ' if rest.startswith('| ') else ''
        cells = rest[len(lead):].split(' | ')
        for k, t in enumerate(text.split(' | ')):
            if k < len(cells) and t.strip() and t.strip() != '=':
                parts = SEP.split(cells[k])
                parts[0] = t.strip()
                cells[k] = ' || '.join(parts)
        return op + ' ' + lead + ' | '.join(cells)
    if op == 'sol':
        _, _, after = rest.partition(' ## ')
        return f'sol {text} ## {after}'
    prefix = ''
    if op in LABEL_OPS:
        m = re.match(r'^([^|]*?) \| (.*)$', rest)
        if m:
            prefix, rest = m.group(1) + ' | ', m.group(2)
    parts = SEP.split(rest)
    parts[0] = text
    return f'{op} {prefix}' + ' || '.join(parts)


def show(lines):
    in_svg = False
    for i, line in enumerate(lines, 1):
        if in_svg:
            in_svg = not line.startswith('endsvg')
            continue
        if line.startswith('svg '):
            in_svg = True
        op = line.split(' ', 1)[0]
        if '||' in line:
            parts = SEP.split(line)
            en = parts[1] if len(parts) > 1 else ''
            print(f'{i:3} {op:6} {en[:90]}')
        else:
            print(f'{i:3} {line[:100]}')


def apply_fixes(lines, ftext):
    repl, inserts, dels = {}, {}, set()
    for raw in ftext.splitlines():
        if not raw.strip():
            continue
        n, _, text = raw.partition('\t')
        n = int(n)
        if text == '-':
            dels.add(n)
        elif text.startswith('+'):
            inserts.setdefault(n, []).append(text[1:])
        elif text.startswith('!'):
            repl[n] = ('line', text[1:])
        else:
            repl[n] = ('slot', text)
    out = list(inserts.get(0, []))
    for i, line in enumerate(lines, 1):
        if i not in dels:
            if i in repl:
                kind, t = repl[i]
                line = t if kind == 'line' else set_first(line, t)
            out.append(line)
        out.extend(inserts.get(i, []))
    return out


def main():
    j = int(sys.argv[1])
    path = HERE / 'sstum' / 'pages' / f'p{j:03d}.txt'
    if '--fix' in sys.argv:
        f = Path(sys.argv[sys.argv.index('--fix') + 1])
        lines = apply_fixes(path.read_text(encoding='utf-8').splitlines(), f.read_text(encoding='utf-8'))
        path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    elif '--show' not in sys.argv:
        path.write_text('\n'.join(draft(j)) + '\n', encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')
    show(path.read_text(encoding='utf-8').splitlines())


if __name__ == '__main__':
    main()
