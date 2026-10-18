# -*- coding: utf-8 -*-
"""Re-embed page records into js/data_phys.js: python embed.py 202 203 ... (or 'all89' for 202-256)."""
import io, json, os, sys, datetime, subprocess
from pathlib import Path

ROOT = Path(r'D:\SpaceBook\SpaceBook Web')
DATA = ROOT / 'js' / 'data_phys.js'
LOCK = ROOT / 'tmp' / 'class-content-shared.lock'
PAGES = Path(__file__).resolve().parent.parent

args = sys.argv[1:]
nums = list(range(202, 257)) if args == ['all89'] else [int(a) for a in args]

fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
try:
    os.write(fd, f'class9-physics u8u9 embed {datetime.datetime.now().isoformat()}\n'.encode())
    raw = io.open(DATA, encoding='utf-8', newline='').read()
    crlf = '\r\n' in raw
    s = raw.replace('\r\n', '\n')
    marker = 'const pages = ['
    i = s.index(marker) + len('const pages = ')
    depth, j, instr, esc = 0, i, False, False
    while True:
        c = s[j]
        if instr:
            if esc: esc = False
            elif c == '\\': esc = True
            elif c == '"': instr = False
        elif c == '"': instr = True
        elif c == '[': depth += 1
        elif c == ']':
            depth -= 1
            if depth == 0: break
        j += 1
    pages = json.loads(s[i:j + 1])
    byid = {p['id']: k for k, p in enumerate(pages)}
    for n in nums:
        rec = json.loads((PAGES / f'physics-page-{n:03d}.json').read_text(encoding='utf-8'))
        pages[byid[rec['id']]] = rec
    pages.sort(key=lambda p: (p.get('pdfPage') or 10**6))
    new = json.dumps(pages, ensure_ascii=False, indent=2)
    s = s[:i] + new + s[j + 1:]
    anchor = "  const reviewed = pages.filter(page => page.chapterNumber === chapter.num);\n  if (!reviewed.length) continue;\n"
    patch = "  if (reviewed.some(page => page.replacesLegacyLists)) for (const key of ['definitions', 'numericals', 'activities', 'tables', 'formulas']) chapter[key] = [];\n"
    if patch not in s:
        assert s.count(anchor) == 1
        s = s.replace(anchor, anchor + patch)
    io.open(DATA, 'w', encoding='utf-8', newline='').write(s.replace('\n', '\r\n') if crlf else s)
finally:
    os.close(fd)
    os.remove(LOCK)
r = subprocess.run(['node', '-e', "global.window=global;global.DATA={};require('./js/data_phys.js');"
                    "for(const n of [8,9]){const c=DATA.physChapters[n-1];console.log(n,c.sections.length,'secs',c.textbookExercise.mcqs.length,'mcq',(c.numericals||[]).length,'num',c.sourceReview.complete)}"],
                   cwd=ROOT, capture_output=True, text=True)
print('embedded', len(nums), r.stdout, r.stderr[-800:])
