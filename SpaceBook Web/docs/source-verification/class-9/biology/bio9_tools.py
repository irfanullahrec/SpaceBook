# -*- coding: utf-8 -*-
"""Class 9 Biology source-verification build tools.

Content authored per unit in unitN.py files is upserted into js/bio_data.js
(BIO_DATA, the active Class 9 Biology dataset rendered by openSubjectWorkspace
-> renderScienceLessonSubContent -> renderScienceSourceLayout).

Record model per section (mirrors Class 9 Physics/Chemistry source sections):
  id, sectionNum, title, urduTitle, pashtoTitle,
  paras: [{text, urdu, pashto, translationOrigin}]  (explicit paired records)
  sourceLayout: [{type, indices|blockId|tableId}]   (reading order)
  sourceBlocks: [{id, svg, svgUrdu, svgPashto, sourceWidthRatio} | table]
  sourcePdfPages, sourcePrintedPages, translationStatus
"""
import json, os, re, io
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
BIO_JS = os.path.join(WEB, 'js', 'bio_data.js')
PROGRESS = os.path.join(HERE, 'progress.json')
SOURCE_PDF = r'D:\SpaceBook\Books\9th\9th Biology\PDF\9th Biology.pdf'
PRINT_OFFSET = 6  # printed page N == PDF page N+6 for PDF 7-31
# (first PDF page of segment, PDF minus printed). Printed 26 is missing after PDF 31.
PRINT_SEGMENTS = [(7, 6), (32, 5), (47, 3)]  # printed 42-43 missing after PDF 46


def printed_of(pdf_page):
    off = None
    for start, o in PRINT_SEGMENTS:
        if pdf_page >= start:
            off = o
    return pdf_page - off if off is not None else None

HEADER = """// ==========================================================================
// SpaceBook - Grade 9 Biology Complete Curriculum Data
// A Textbook of BIOLOGY Grade IX - Khyber Pakhtunkhwa Textbook Board Peshawar
// Source-verified page by page against D:/SpaceBook/Books/9th/9th Biology/PDF/9th Biology.pdf
// Verification records: docs/source-verification/class-9/biology/
// ==========================================================================

var BIO_DATA = """


def load_bio():
    src = io.open(BIO_JS, encoding='utf-8').read()
    start = src.index('var BIO_DATA = ') + len('var BIO_DATA = ')
    body = src[start:].rstrip()
    if body.endswith(';'):
        body = body[:-1]
    return json.loads(body)


def save_bio(data):
    txt = HEADER + json.dumps(data, ensure_ascii=False, indent=2) + ';\n'
    tmp = BIO_JS + '.tmp'
    io.open(tmp, 'w', encoding='utf-8', newline='\n').write(txt)
    os.replace(tmp, BIO_JS)


def pair(text, urdu, pashto, **extra):
    d = dict(text=text, urdu=urdu, pashto=pashto, translationOrigin='SpaceBook')
    d.update(extra)
    return d


class Section:
    """Accumulates paired paragraphs and a source layout in reading order."""

    def __init__(self, sid, num, title, ur, ps, pdf_pages, callouts=None):
        self.id = sid
        self.num = num
        self.title = title
        self.ur = ur
        self.ps = ps
        self.pdf_pages = list(pdf_pages)
        self.paras = []
        self.layout = []
        self.blocks = []
        self.callouts = callouts

    # ---- paragraph helpers -------------------------------------------------
    def _add(self, text, ur, ps, **extra):
        self.paras.append(pair(text, ur, ps, **extra))
        return len(self.paras) - 1

    def p(self, text, ur, ps, **extra):
        i = self._add(text, ur, ps, **extra)
        self.layout.append(dict(type='paragraph', indices=[i]))
        return i

    def h(self, text, ur, ps):
        i = self._add(text, ur, ps)
        self.layout.append(dict(type='heading', indices=[i]))
        return i

    def caption(self, text, ur, ps):
        i = self._add(text, ur, ps)
        self.layout.append(dict(type='paragraph', indices=[i], role='caption'))
        return i

    def ol(self, items):
        idx = [self._add(*it) for it in items]
        self.layout.append(dict(type='numberedList', indices=idx))
        return idx

    def ul(self, items):
        idx = [self._add(*it) for it in items]
        self.layout.append(dict(type='list', indices=idx))
        return idx

    def lines(self, items):
        idx = [self._add(*it) for it in items]
        self.layout.append(dict(type='lines', indices=idx))
        return idx

    def callout(self, title, body, kind='info'):
        """Boxed side note such as 'Scientific Information' (title pair, body pairs)."""
        idx = [self._add(*title)] + [self._add(*b) for b in body]
        self.layout.append(dict(type='quotation', indices=idx, role='callout', kind=kind))
        return idx

    def quote(self, items):
        idx = [self._add(*it) for it in items]
        self.layout.append(dict(type='quotation', indices=idx))
        return idx

    def verse(self, arabic, english, ur, ps, ref, ref_ur, ref_ps):
        """Quran verse box: Arabic original (RTL), book's English, reference."""
        a = self._add(arabic, ur, ps, sourceLanguage='ar', english=english)
        e = self._add(english, ur, ps)
        r = self._add(ref, ref_ur, ref_ps)
        self.layout.append(dict(type='quotation', indices=[a, e, r]))
        return [a, e, r]

    # ---- visual helpers ----------------------------------------------------
    def fig(self, bid, svg_en, svg_ur, svg_ps, ratio, caption=None, kind='figure'):
        self.blocks.append(dict(id=bid, kind=kind, svg=svg_en, svgUrdu=svg_ur, svgPashto=svg_ps, sourceWidthRatio=ratio))
        self.layout.append(dict(type='visual', blockId=bid))
        if caption:
            self.caption(*caption)

    def table(self, tid, headers, rows, headers_ur, rows_ur, headers_ps, rows_ps, ratio=None, caption=None, no_header=False):
        t = dict(id=tid, kind='table', headers=headers, rows=rows,
                 translations=[dict(language='اردو', headers=headers_ur, rows=rows_ur),
                               dict(language='پښتو', headers=headers_ps, rows=rows_ps)])
        if ratio:
            t['sourceWidthRatio'] = ratio
        if no_header:
            t['noHeader'] = True
        if caption:  # table titles are printed above the table in this book
            self.caption(*caption)
        self.blocks.append(t)
        self.layout.append(dict(type='sourceDataTable', tableId=tid))

    # ---- finalize ----------------------------------------------------------
    def record(self):
        rec = dict(
            id=self.id, sectionNum=self.num, title=self.title,
            urduTitle=self.ur, pashtoTitle=self.ps,
            paras=self.paras,
            content=[p['text'] for p in self.paras],
            sourceLayout=self.layout,
            sourceBlocks=self.blocks,
            sourcePdfPages=self.pdf_pages,
            sourcePrintedPages=[printed_of(p) for p in self.pdf_pages if printed_of(p)],
            translationStatus='authored_aligned_paragraphs',
            sourceClass9Biology=True,
        )
        if self.callouts:
            rec['callouts'] = self.callouts
        return rec


# ---- SVG helpers -------------------------------------------------------------
def svg_wrap(body, w, h, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" '
            f'aria-label="{escape(label, quote=True)}">{body}</svg>')


def txt(x, y, s, size=13, anchor='start', weight='normal', fill='#1f2937', rtl=False, italic=False, extra=''):
    a = f' text-anchor="{anchor}"' if anchor != 'start' else ''
    d = ' direction="rtl" unicode-bidi="bidi-override"' if rtl else ''
    fs = ' font-style="italic"' if italic else ''
    return (f'<text x="{x}" y="{y}" font-family="Segoe UI, Noto Sans, Noto Naskh Arabic, sans-serif" '
            f'font-size="{size}" font-weight="{weight}" fill="{fill}"{a}{d}{fs}{extra}>{escape(str(s))}</text>')


def photo_figure(label, items, caption, w=560, cols=2, cell_h=120):
    """Coded stand-in for a printed photograph collage: framed grid with the
    source's item labels so the figure's instructional content is preserved."""
    rows = (len(items) + cols - 1) // cols
    cw = (w - 20) // cols
    h = rows * cell_h + 40
    body = [f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="8" fill="#f8fafc" stroke="#94a3b8"/>']
    for i, (letter, name) in enumerate(items):
        r, c = divmod(i, cols)
        x = 10 + c * cw
        y = 10 + r * cell_h
        body.append(f'<rect x="{x+4}" y="{y}" width="{cw-8}" height="{cell_h-28}" rx="6" fill="#e2e8f0" stroke="#cbd5e1"/>')
        body.append(txt(x + cw / 2, y + (cell_h - 28) / 2 + 5, name, 14, 'middle', 'bold', '#334155'))
        body.append(txt(x + cw / 2, y + cell_h - 10, letter, 12, 'middle', 'normal', '#64748b'))
    body.append(txt(w / 2, h - 12, caption, 12, 'middle', 'normal', '#475569', italic=True))
    return svg_wrap(''.join(body), w, h, label)


# ---- dataset upsert ----------------------------------------------------------
def upsert_unit(unit_number, sections=None, unit_fields=None, replace_sections=True):
    data = load_bio()
    unit = next(u for u in data if u.get('number') == unit_number)
    if sections is not None:
        recs = [s.record() if isinstance(s, Section) else s for s in sections]
        if replace_sections:
            unit['sections'] = recs
        else:
            by_id = {s['id']: i for i, s in enumerate(unit['sections'])}
            for r in recs:
                if r['id'] in by_id:
                    unit['sections'][by_id[r['id']]] = r
                else:
                    unit['sections'].append(r)
    if unit_fields:
        unit.update(unit_fields)
    ids = [s['id'] for s in unit['sections']]
    assert len(ids) == len(set(ids)), 'duplicate section ids: %r' % ids
    save_bio(data)
    return unit


# ---- progress ----------------------------------------------------------------
def load_progress():
    if os.path.exists(PROGRESS):
        return json.load(io.open(PROGRESS, encoding='utf-8'))
    return dict(subject='Biology', book=SOURCE_PDF, totalPdfPages=225, printedOffset=PRINT_OFFSET, pages={})


def record_pages(entries, next_page=None, current_chapter=None):
    """entries: list of (pdfPage, status, note). status in
    verified_unchanged | corrected | excluded | unresolved | inspected"""
    prog = load_progress()
    for pdf_page, status, note in entries:
        prog['pages'][str(pdf_page)] = dict(printed=printed_of(pdf_page),
                                            status=status, note=note)
    if next_page is not None:
        prog['nextPdfPage'] = next_page
    if current_chapter is not None:
        prog['currentChapter'] = current_chapter
    done = sorted(int(k) for k in prog['pages'])
    prog['lastRecordedPdfPage'] = done[-1] if done else 0
    prog['counts'] = {}
    for v in prog['pages'].values():
        prog['counts'][v['status']] = prog['counts'].get(v['status'], 0) + 1
    json.dump(prog, io.open(PROGRESS, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return prog


def check_js():
    """Quick syntax/data check of bio_data.js with node."""
    import subprocess
    script = ("const fs=require('fs');const vm=require('vm');const c={};vm.createContext(c);"
              "vm.runInContext(fs.readFileSync(process.argv[1],'utf8'),c);"
              "const B=c.BIO_DATA;let n=0,ids=new Set(),dup=[];for(const u of B){for(const s of u.sections){n++;"
              "if(ids.has(s.id))dup.push(s.id);ids.add(s.id);if(s.paras){for(const p of s.paras){if(!p.text||!p.urdu||!p.pashto)"
              "throw new Error('missing pair in '+s.id);}}if(s.sourceLayout){for(const b of s.sourceLayout){for(const i of (b.indices||[])){"
              "if(!s.paras[i])throw new Error('bad index '+i+' in '+s.id);}if(b.blockId&&!s.sourceBlocks.find(x=>x.id===b.blockId))throw new Error('missing block '+b.blockId);"
              "if(b.tableId&&!s.sourceBlocks.find(x=>x.id===b.tableId))throw new Error('missing table '+b.tableId);}}}}"
              "console.log('BIO_DATA ok: units='+B.length+' sections='+n+' dupIds='+JSON.stringify(dup));")
    r = subprocess.run(['node', '-e', script, BIO_JS], capture_output=True, text=True)
    print(r.stdout.strip(), r.stderr.strip())
    return r.returncode == 0
