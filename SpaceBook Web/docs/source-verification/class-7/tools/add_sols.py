"""Insert `sol` lines under question lines of page files.
    python add_sols.py CLASS SUBJ entries.txt [--write]
entries.txt blocks:
    @@ p014 1-ex-fill 1            (page, exercise id, q number)  or  @@ p014 1-ex-fill 1 a   (part a: after that qp line)
    <the sol line(s), starting with 'sol ' or other directives>
"""
import sys, re
from pathlib import Path
HERE = Path(__file__).resolve().parents[2]
cl, subj, ent = sys.argv[1], sys.argv[2], sys.argv[3]
write = '--write' in sys.argv
blocks = []
cur = None
for l in Path(ent).read_text(encoding='utf-8').split('\n'):
    if l.startswith('@@ '):
        cur = [l[3:].split(), []]; blocks.append(cur)
    elif cur is not None and l.strip():
        cur[1].append(l.rstrip())
files = {}
bad = 0
for key, lines in blocks:
    page, ex, qno = key[0], key[1], key[2]
    occ = 1
    for t in key[3:]:
        if t.startswith('#'): occ = int(t[1:])
    part = next((t for t in key[3:] if not t.startswith('#')), None)
    f = HERE / f'class-{cl}' / subj / 'pages' / f'{page}.txt'
    L = files.setdefault(f, f.read_text(encoding='utf-8').split('\n'))
    inex = ex == '-'
    pos = None
    for i, l in enumerate(L):
        if l.startswith('exercise ') and not inex_done if False else False: pass
    cur_ex = None if ex != '-' else '-'
    for i, l in enumerate(L):
        if l.startswith('exercise '): cur_ex = l.split(None, 1)[1].strip()
        elif l.startswith('endexercise'): cur_ex = None if ex != '-' else '-'
        if qno == '-' and part and (cur_ex is not None) and (ex == '*' or cur_ex == ex) and re.match(r'qp\s+' + re.escape(part) + r'(\s|\|)', l):
            occ -= 1
            if occ > 0: continue
            pos = i
            break
        if qno != '-' and (ex == '*' and cur_ex is not None or cur_ex == ex) and re.match(r'q\s+' + re.escape(qno) + r'(\s|\|)', l):
            occ -= 1
            if occ > 0: continue
            pos = i
            if part:
                j = i + 1
                while j < len(L) and not re.match(r'q\s', L[j]) and not L[j].startswith(('exercise','endexercise','@')):
                    if re.match(r'qp\s+' + re.escape(part) + r'(\s|\|)', L[j]): pos = j; break
                    j += 1
                else:
                    pos = None
            break
    if pos is None:
        print('NOT FOUND', key); bad += 1; continue
    # skip existing sol directly after
    k = pos + 1
    while k < len(L) and L[k].startswith('@'): k += 1
    if k < len(L) and L[k].startswith('sol '):
        print('already has sol', key); continue
    for off, x in enumerate(lines): L.insert(pos + 1 + off, x)
print(len(blocks), 'entries;', bad, 'not found')
if write and not bad:
    for f, L in files.items(): f.write_text('\n'.join(L), encoding='utf-8')
    print('written', len(files), 'files')
