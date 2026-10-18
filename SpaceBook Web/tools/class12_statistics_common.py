"""Statistics XII source pipeline: aligned EN/UR/PS records, short-lock saves into js/stat_12_data.js, progress marks.

One record per authored source block (usually one per PDF spread). Inline maths uses $...$ LaTeX, rendered by the
local KaTeX reader (app.js enables it for sections flagged sourceClass12Statistics). The first save into a unit
collapses that unit's unverified legacy sections into one pending holder; the unit's last page drops the holder.
"""
from pathlib import Path
import json, os, time, html, re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/source-verification/class-12'
SOURCE = 'D:/SpaceBook/Books/12th/12th Statistics/PDF/Statistics Book for 12 class KPTBB.pdf'
DATA = ROOT / 'js/stat_12_data.js'
PROGRESS = OUT / 'statistics-progress.json'
TOTAL = 176


def pair(en, ur, ps):
    return {'text': en, 'urdu': ur, 'pashto': ps}


def plain(text):
    """Readable fallback for the plain theory/content fields (LaTeX delimiters dropped)."""
    return re.sub(r'\$([^$]+)\$', r'\1', text)


def section(identity, title, urtitle, pstitle, paragraphs, layout, blocks, pdf, printed):
    printed = list(printed) if isinstance(printed, (list, tuple)) else [printed]
    return {'id': identity, 'title': title, 'headingUrdu': urtitle, 'headingPashto': pstitle,
            'paras': paragraphs,
            'theory': '\n\n'.join(plain(p['text']) for p in paragraphs),
            'urdu': '\n\n'.join(plain(p['urdu']) for p in paragraphs),
            'pashto': '\n\n'.join(plain(p['pashto']) for p in paragraphs),
            'theoryUrdu': '\n\n'.join(plain(p['urdu']) for p in paragraphs),
            'theoryPashto': '\n\n'.join(plain(p['pashto']) for p in paragraphs),
            'content': ''.join('<p>' + html.escape(plain(p['text'])) + '</p>' for p in paragraphs),
            'translationStatus': 'authored_aligned_paragraphs', 'sourceClass12Statistics': True,
            'sourceLayout': layout, 'sourceBlocks': blocks,
            'sourceReferences': [{'sourcePdf': SOURCE, 'pdfPage': pdf, 'printedPages': printed}],
            'sourceReviewStatus': 'source_compared', 'rules': [], 'sciNote': ''}


class Builder:
    """Accumulates aligned paragraphs and layout blocks for one record."""
    def __init__(self):
        self.paras, self.layout, self.blocks = [], [], []

    def add(self, kind, en, ur, ps):
        self.layout.append({'type': kind, 'indices': [len(self.paras)]})
        self.paras.append(pair(en, ur, ps))
        return self

    def h(self, en, ur, ps): return self.add('heading', en, ur, ps)
    def p(self, en, ur, ps): return self.add('paragraph', en, ur, ps)
    def eq(self, latex): return self.add('equation', f'$${latex}$$', f'$${latex}$$', f'$${latex}$$')

    def mlines(self, latex_lines, kind='lines'):
        """Display several formula lines (same in all languages)."""
        return self.group(kind, [(f'${x}$',) * 3 for x in latex_lines])

    def mcq(self, label, q, opts, per_line=2):
        """Multiple-choice item: q=(en,ur,ps); opts = entries, each a str (same in all languages) or (en,ur,ps).
        Options are laid out per_line to a row, lettered (a), (b), …"""
        self.p(f'{label} {q[0]}', f'{label} {q[1]}', f'{label} {q[2]}')
        o = [(x, x, x) if isinstance(x, str) else x for x in opts]
        letters = 'abcdefgh'
        lines = []
        for s in range(0, len(o), per_line):
            chunk = range(s, min(s + per_line, len(o)))
            lines.append(tuple('  '.join(f'({letters[k]}) {o[k][i]}' for k in chunk) for i in range(3)))
        return self.group('lines', lines)

    def lab(self, latex, en, ur, ps):
        """A formula line followed by a parenthesised label, e.g. (estimator) / (point estimate)."""
        return self.add('lines', f'${latex}$ ({en})', f'${latex}$ ({ur})', f'${latex}$ ({ps})')

    def group(self, kind, items):
        """items: list of (en, ur, ps); kind list/numberedList/lines."""
        start = len(self.paras)
        for en, ur, ps in items:
            self.paras.append(pair(en, ur, ps))
        self.layout.append({'type': kind, 'indices': list(range(start, len(self.paras)))})
        return self

    def table(self, tid, headers, rows, ur_headers, ps_headers, ur_rows=None, ps_rows=None, **extra):
        t = {'id': tid, 'headers': headers, 'rows': rows,
             'translations': [{'language': 'اردو', 'headers': ur_headers, 'rows': ur_rows or rows},
                              {'language': 'پښتو', 'headers': ps_headers, 'rows': ps_rows or rows}]}
        t.update(extra)
        self.blocks.append(t)
        self.layout.append({'type': 'sourceDataTable', 'tableId': tid})
        return self

    def grid(self, tid, headers, rows):
        """Numeric/formula table whose cells are language-neutral except the word Total (localised)."""
        loc = lambda lang: [[{'en': c, 'ur': 'کل', 'ps': 'ټول'}[lang] if c == 'Total' else c for c in r] for r in rows]
        hl = lambda lang: [{'en': h, 'ur': 'کل', 'ps': 'ټول'}[lang] if h == 'Total' else h for h in headers]
        return self.table(tid, headers, rows, hl('ur'), hl('ps'), loc('ur'), loc('ps'))

    def dist(self, tid, xs, ps, xlabel='$X$', plabel='$p(x)$', total='1', vertical=False):
        """Probability-distribution table as printed: horizontal (X row / p(x) row) or vertical, optional Total."""
        T = {'en': 'Total', 'ur': 'کل', 'ps': 'ټول'}
        if vertical:
            rows = [[x, p] for x, p in zip(xs, ps)]
            mk = lambda lang: rows + ([[T[lang], total]] if total is not None else [])
            return self.table(tid, [xlabel, plabel], mk('en'), [xlabel, plabel], [xlabel, plabel], mk('ur'), mk('ps'))
        head = lambda lang: [xlabel] + list(xs) + ([T[lang]] if total is not None else [])
        row = [[plabel] + list(ps) + ([total] if total is not None else [])]
        return self.table(tid, head('en'), row, head('ur'), head('ps'))

    def vpara(self, bid, svg, en, ur, ps, ratio=.42):
        """Text with a figure beside it (visualParagraph); svg is language-neutral."""
        self.blocks.append({'id': bid, 'svg': svg, 'svgUrdu': svg, 'svgPashto': svg, 'sourceWidthRatio': ratio})
        self.layout.append({'type': 'visualParagraph', 'blockId': bid, 'indices': [len(self.paras)], 'visualFirst': False})
        self.paras.append(pair(en, ur, ps))
        return self

    def visual(self, bid, en, ur=None, ps=None, ratio=None):
        b = {'id': bid, 'svg': en, 'svgUrdu': ur or en, 'svgPashto': ps or en}
        if ratio: b['sourceWidthRatio'] = ratio
        self.blocks.append(b)
        self.layout.append({'type': 'visual', 'blockId': bid})
        return self

    def build(self, identity, title, urtitle, pstitle, pdf, printed):
        return section(identity, title, urtitle, pstitle, self.paras, self.layout, self.blocks, pdf, printed)


SYNC = r'''
const unitOf=n=>STAT_12_DATA.find(item=>item.number===n);
const isAuthored=s=>s&&s.sourceClass12Statistics===true;
for(const record of audit.sections){
 const unit=unitOf(record.unit);
 if(!unit)throw new Error('Missing Statistics XII unit '+record.unit);
 const holderId='stat12-u'+record.unit+'-pending';
 if(!unit.sections.some(isAuthored)&&!unit.sections.some(s=>s.id===holderId)){
  const legacy=unit.sections.filter(s=>!isAuthored(s));
  unit.sections=[{id:holderId,title:'Remaining unit text — source verification in progress',headingUrdu:'باقی متن — ماخذ سے تصدیق جاری ہے',headingPashto:'پاتې متن — له سرچينې سره تاييد روان دی',
   theory:legacy.map(s=>(s.title?s.title+'\n':'')+(s.theory||'')).join('\n\n'),content:legacy.map(s=>s.content||'').join(''),rules:[],sciNote:'',sourcePendingAuthoring:true}];
 }
 const data=Object.assign({},record);delete data.unit;
 const index=unit.sections.findIndex(s=>s.id===data.id);
 if(index>=0)unit.sections[index]=data;
 else{const holder=unit.sections.findIndex(s=>s.id===holderId);unit.sections.splice(holder<0?unit.sections.length:holder,0,data);}
}
for(const n of audit.completeUnits){const unit=unitOf(n);unit.sections=unit.sections.filter(s=>s.id!=='stat12-u'+n+'-pending');}
for(const unit of STAT_12_DATA.filter(u=>audit.sections.some(r=>r.unit===u.number)||audit.completeUnits.includes(u.number))){
 unit.topics=unit.sections.map(s=>({...((unit.topics||[]).find(t=>t.id===s.id)||{}),...s}));
 unit.sourceIssues=[...(unit.sourceIssues||[]).filter(i=>!audit.issues.some(j=>j.id===i.id)),...audit.issues.filter(i=>(i.unit||audit.sections[0]?.unit)===unit.number)];
}
'''


def _write_locked(path, transform, tag):
    lock = ROOT / 'tmp/class-content-shared.lock'
    for attempt in range(60):
        try:
            fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY); break
        except FileExistsError:
            time.sleep(.5)
    else:
        raise RuntimeError('shared lock busy')
    try:
        os.write(fd, f'{tag} pid={os.getpid()}\n'.encode()); os.close(fd); fd = None
        text = transform(path.read_text(encoding='utf-8'))
        temp = path.with_name(path.name + '.stat12.tmp'); temp.write_text(text, encoding='utf-8')
        for attempt in range(6):
            try:
                os.replace(temp, path); break
            except PermissionError:
                if attempt == 5: raise
                time.sleep(.15)
    finally:
        if fd is not None: os.close(fd)
        lock.unlink()


def save(pdf, records, issues=None, complete_units=None):
    """records: list of (unit_number, section_dict)."""
    audit = {'pdfPage': pdf, 'sections': [dict(r, unit=u) for u, r in records],
             'issues': issues or [], 'completeUnits': complete_units or []}
    marker = f'// BEGIN CLASS12 STATISTICS PDF{pdf:03d} SOURCE'
    end = f'// END CLASS12 STATISTICS PDF{pdf:03d} SOURCE'
    block = marker + '\n{ const audit = ' + json.dumps(audit, ensure_ascii=False, indent=1) + ';' + SYNC + '}\n' + end + '\n'

    def transform(text):
        if marker in text:
            a = text.index(marker); b = text.index(end, a) + len(end)
            return text[:a] + block.rstrip('\n') + text[b:]
        # keep page blocks in PDF order
        later = [m for m in re.finditer(r'// BEGIN CLASS12 STATISTICS PDF(\d{3}) SOURCE', text) if int(m.group(1)) > pdf]
        if later:
            a = later[0].start(); return text[:a] + block + '\n' + text[a:]
        return text.rstrip() + '\n\n' + block
    _write_locked(DATA, transform, 'class12-statistics')
    (OUT / 'statistics').mkdir(exist_ok=True)
    (OUT / f'statistics/pdf{pdf:03d}.json').write_text(json.dumps(audit, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'Statistics PDF {pdf} saved ({len(records)} record(s)).')


def progress():
    if PROGRESS.exists():
        return json.loads(PROGRESS.read_text(encoding='utf-8'))
    return {'schemaVersion': 1, 'subject': 'Statistics', 'class': 12, 'sourcePdf': SOURCE, 'totalPdfPages': TOTAL,
            'workflow': 'inspect scan → compare with legacy/OCR → author aligned EN/UR/PS record → save → record → next',
            'pages': [{'pdfPage': n, 'status': 'not_started'} for n in range(1, TOTAL + 1)]}


def mark(pdf, evidence, status='corrected_verified', printed=None):
    p = progress()
    e = p['pages'][pdf - 1]; assert e['pdfPage'] == pdf
    e.update({'status': status, 'evidence': evidence, 'markedUtc': datetime.now(timezone.utc).isoformat()})
    if printed is not None: e['printedPages'] = printed
    done = [x['pdfPage'] for x in p['pages'] if x['status'] in ('corrected_verified', 'verified_unchanged', 'excluded')]
    contiguous = 0
    for x in p['pages']:
        if x['status'] in ('corrected_verified', 'verified_unchanged', 'excluded'): contiguous = x['pdfPage']
        else: break
    p['lastContiguousResolvedPdfPage'] = contiguous
    p['nextPdfPage'] = contiguous + 1 if contiguous < TOTAL else None
    p['resolvedCount'] = len(done)
    p['phase'] = 'complete' if len(done) == TOTAL else 'sequential_source_authoring'
    p['updatedUtc'] = datetime.now(timezone.utc).isoformat()
    PROGRESS.write_text(json.dumps(p, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('marked Statistics PDF', pdf, status)
