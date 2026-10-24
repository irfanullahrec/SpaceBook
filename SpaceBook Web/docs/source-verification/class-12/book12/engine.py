# -*- coding: utf-8 -*-
"""Page-by-page builder for the Class 12 textbooks whose reviewed data is kept per scan (a spread of two printed pages).

    python -X utf8 engine.py KEY dump     dump the book's data and exercise bank (node book12/dump.cjs)
    python -X utf8 engine.py KEY ocr      extract the Word OCR (footers carry the printed page numbers)
    python -X utf8 engine.py KEY align    candidate page splits -> KEY/candidates.json
    python -X utf8 engine.py KEY review OUTDIR PDF [PDF ...]    sheets of the page boundaries for checking against the scans
    python -X utf8 engine.py KEY gen      write KEY/pages/pNNN.txt (NNN = JPG index) from the data and KEY/splits_*.txt
    python -X utf8 engine.py KEY check    every word of the data appears once, in the book's order

A book is described by book12/cfgs/KEY.py (JPG folder, scan -> JPG pages, JPG -> printed page, slot order of the languages).
The page files use the same page syntax as the Class 6-10 books (class-6/tools/build_math6.py); tools/build_book12.py KEY builds
them into js/. Splits: KEY/splits_*.txt, lines "PDF ok" | "PDF A last words of page A" | "PDF B first words of page B" |
"PDF V figure-id A|B" (checked against the scans by eye, see review).  KEY/fix/pNNN.txt replaces a generated page by hand.
"""
import bisect, difflib, importlib, json, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CLASS = HERE.parent
APP = CLASS.parents[2]
sys.path.insert(0, str(HERE))

TR = str.maketrans({'ي': 'ی', 'ى': 'ی', 'ے': 'ی', 'ك': 'ک', 'ه': 'ہ', 'ۃ': 'ہ', 'ة': 'ہ', 'ھ': 'ہ', 'ۂ': 'ہ', 'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ؤ': 'و', 'ئ': 'ی',
                    '۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4', '۵': '5', '۶': '6', '۷': '7', '۸': '8', '۹': '9'})
FIELD = {'ur': 'urdu', 'en': 'text', 'ps': 'pashto'}


def norm(s):
    s = re.sub(r'[ً-ٰٟٕٔ‌‍‎‏]', '', s).translate(TR)
    return re.sub(r'[^\w]|_', '', s.lower())


def clean(s):
    return re.sub(r'\s+', ' ', (s or '').replace('||', '{{OR}}').replace('|', '{{BAR}}').replace('##', '#')).strip()


class Book:
    def __init__(self, key):
        self.key = key
        self.cfg = importlib.import_module('cfgs.' + key)
        self.dir = CLASS / key
        self.dir.mkdir(exist_ok=True)
        self._dump = None

    # ------------------------------------------------------------------ data
    def dump(self):
        c = self.cfg
        subprocess.run(['node', str(HERE / 'dump.cjs'), c.DATA_FILE, c.GLOBAL, c.BANK_FILES or '-', c.BANK_KEY or '-', str(self.dir / 'dump.json')], check=True, cwd=APP)

    def load(self):
        if self._dump is None:
            self._dump = json.loads((self.dir / 'dump.json').read_text(encoding='utf-8'))
        return self._dump

    def sections(self):
        out = []
        for ch in self.load():
            for s in ch['sections']:
                ref = (s.get('refs') or [{}])[0]
                out.append(dict(s, ch=ch['number'], pdf=ref.get('pdfPage'), printed=[p for p in (ref.get('printedPages') or []) if p is not None]))
        return out

    def units_of(self, sec):
        """The section's content in printed order: one unit per heading / paragraph / line / list item / table / figure."""
        tables = {b['id']: b for b in sec['blocks']}
        out = []
        for li, b in enumerate(sec.get('layout') or []):
            t = b['type']
            idx = b.get('indices') or []
            if t == 'heading':
                out += [{'k': 'h', 'sec': sec['id'], 'li': li, 'pi': i} for i in idx]
            elif t in ('paragraph', 'definition', 'quotation'):
                out += [{'k': 'p', 'sec': sec['id'], 'li': li, 'pi': i} for i in idx]
            elif t in ('lines', 'numbered', 'numberedList', 'orderedList', 'table'):
                out += [{'k': 'l', 'sec': sec['id'], 'li': li, 'pi': i} for i in idx]
            elif t == 'list':
                out += [{'k': 'li', 'sec': sec['id'], 'li': li, 'pi': i} for i in idx]
            elif t == 'equation':
                out += [{'k': 'eq', 'sec': sec['id'], 'li': li, 'pi': i} for i in idx]
            elif t == 'code':
                out += [{'k': 'code', 'sec': sec['id'], 'li': li, 'pi': i} for i in idx]
            elif t == 'sourceDataTable':
                out.append({'k': 't', 'sec': sec['id'], 'li': li, 'id': b['tableId']})
            elif t == 'visual':
                out.append({'k': 'v', 'sec': sec['id'], 'li': li, 'id': b['blockId']})
            elif t == 'visualParagraph':
                v = {'k': 'v', 'sec': sec['id'], 'li': li, 'id': b['blockId']}
                ps = [{'k': 'p', 'sec': sec['id'], 'li': li, 'pi': i} for i in idx]
                out += ([v] + ps) if b.get('visualFirst') else (ps + [v])
            else:
                raise SystemExit(f'{self.key}: unknown layout type {t} in {sec["id"]}')
        return out

    def text_of(self, by_id, u):
        if 'pi' not in u:
            return ''
        p = by_id[u['sec']]['paras'][u['pi']]
        return p.get(self.cfg.ORIG) or ''

    def scan_streams(self, group, pages):
        """Sections that sit on one page of the scan (placed by their label) and the stream that one cut divides between its pages."""
        direct, stream = [], []
        for s in group:
            only = [p for p in s['printed'] if p in pages]
            if len(only) == 1 and len(group) > 1:
                direct.append((only[0], s))
            else:
                stream.append(s)
        return direct, stream

    def printed_of(self, jpg):
        """Printed page number on a JPG: the config's own rule, or (single-scan books) the page the reviewed data names for its scan."""
        if hasattr(self.cfg, 'printed_of'):
            return self.cfg.printed_of(jpg)
        return self.label_map().get(jpg)

    def label_map(self):
        if getattr(self, '_labels', None) is None:
            m = {}
            for k, group in sorted(self.by_pdf().items()):
                jp = self.cfg.pdf_jpgs(k)
                if not jp:
                    continue
                pages = sorted({p for s in group for p in s['printed']})
                for j, p in zip(jp, pages):
                    m[j] = p
            self._labels = m
        return self._labels

    def scan_pages(self, k):
        j = self.cfg.pdf_jpgs(k)
        return j, (j and tuple(self.printed_of(x) for x in j))

    # ------------------------------------------------------------------ printed page numbers of the scans
    def footers(self, regions=('bottom',)):
        """Read the printed page number of every JPG (RapidOCR on the footer strip) -> KEY/footers.json {jpg: number or null}."""
        import numpy as np
        from PIL import Image, ImageOps
        from rapidocr_onnxruntime import RapidOCR
        eng = RapidOCR()
        out, f = {}, self.dir / 'footers.json'
        if f.exists():
            out = {int(k): v for k, v in json.loads(f.read_text(encoding='utf-8')).items()}
        files = sorted(self.cfg.JPG.glob('*.jpg'))
        for j, p in enumerate(files):
            if j in out:
                continue
            im = Image.open(p).convert('L')
            w, h = im.size
            found = None
            for reg in regions:
                box = (int(w * 0.08), int(h * 0.86), int(w * 0.92), h) if reg == 'bottom' else (int(w * 0.08), 0, int(w * 0.92), int(h * 0.10))
                c = im.crop(box)
                for img in (c, ImageOps.invert(c)):
                    r, _ = eng(np.asarray(img.convert('RGB')))
                    nums = [int(re.sub(r'\D', '', x[1])) for x in (r or []) if re.fullmatch(r'\s*\d{1,3}\s*', x[1])]
                    if nums:
                        found = nums[0]
                        break
                if found is not None:
                    break
            out[j] = found
            if j % 25 == 0:
                f.write_text(json.dumps(out), encoding='utf-8')
        f.write_text(json.dumps(out), encoding='utf-8')
        print('footers read', len(out), 'none', sum(1 for v in out.values() if v is None))

    def segments(self):
        """Constant-offset runs of JPG index - printed number: the book's page numbering as the footers read it."""
        d = {int(k): v for k, v in json.loads((self.dir / 'footers.json').read_text(encoding='utf-8')).items()}
        runs, cur = [], None
        for j in sorted(d):
            v = d[j]
            if v is None:
                continue
            off = j - v
            if cur and cur['off'] == off and j - cur['last'] <= 6:
                cur['last'], cur['n'] = j, cur['n'] + 1
            else:
                cur = {'off': off, 'first': j, 'last': j, 'n': 1}
                runs.append(cur)
        for r in runs:
            print(f"JPG {r['first']}-{r['last']}  offset {r['off']}  ({r['n']} read)  -> printed {r['first'] - r['off']}-{r['last'] - r['off']}")

    # ------------------------------------------------------------------ OCR of the Word files
    def ocr(self):
        import docx
        out = []
        for f in self.cfg.OCR_DOCX:
            out.append('=====PART ' + Path(f).name)
            out += [p.text for p in docx.Document(f).paragraphs]
        (self.dir / 'ocr_word.txt').write_text('\n'.join(out), encoding='utf-8')
        print('ocr lines', len(out))

    def ocr_pages(self):
        """printed page -> normalised OCR text; pages whose number line is missing are merged into the next found page."""
        lines = (self.dir / 'ocr_word.txt').read_text(encoding='utf-8').split('\n')
        start = next((i for i, l in enumerate(lines) if l.strip() == self.cfg.OCR_START), 0)
        pages, buf, last, merged = {}, [], 0, {}
        for l in lines[start:]:
            m = re.fullmatch(r'\s*(\d{1,3})\s*', l)
            if m:
                v = int(m.group(1))
                if last < v <= last + (8 if last == 0 else 4):
                    pages[v] = norm(' '.join(buf))
                    for q in range(last + 1, v):
                        merged[q] = v
                    buf, last = [], v
                    continue
            buf.append(l)
        return pages, merged

    # ------------------------------------------------------------------ candidate splits
    def ink(self, jpg):
        from PIL import Image
        import numpy as np
        im = np.asarray(Image.open(self.cfg.JPG / f'{jpg:03}.jpg').convert('L'), dtype=np.uint8)
        h, w = im.shape
        body = im[int(h * 0.05):int(h * 0.90), int(w * 0.04):int(w * 0.96)]
        return int((body < 110).sum())

    def by_pdf(self):
        d = {}
        for s in self.sections():
            d.setdefault(s['pdf'], []).append(s)
        return d

    def two_page_scans(self):
        out = []
        for k, group in sorted(self.by_pdf().items()):
            jp, pp = self.scan_pages(k)
            if not jp or len(jp) != 2 or self.cfg.route(k, group):
                continue
            stream = self.scan_streams(group, pp)[1]
            units = [u for s in stream for u in self.units_of(s)]
            if any('pi' in u for u in units):
                out.append((k, jp, pp, units))
        return out

    def align(self):
        secs = self.sections()
        by_id = {s['id']: s for s in secs}
        try:
            pages, merged = self.ocr_pages()
        except FileNotFoundError:
            pages, merged = {}, {}
        out = {}
        for k, jp, pp, units in self.two_page_scans():
            words = []
            for ui, u in enumerate(units):
                for wi, w in enumerate(self.text_of(by_id, u).split()):
                    words.append((ui, wi, norm(w)))
            if not words:
                continue
            stream = ''.join(w[2] for w in words)
            starts, pos = [], 0
            for w in words:
                starts.append(pos)
                pos += len(w[2])
            a_pg, b_pg = pp
            cand, how, conf = None, None, 0
            if b_pg in pages and a_pg not in merged:
                ocr_b = pages.get(b_pg, '')
                for o in (0, 12, 30, 60, 100, 160):
                    key = ocr_b[o:o + 20]
                    if len(key) < 16:
                        break
                    hits = [m.start() for m in re.finditer(re.escape(key), stream)]
                    if len(hits) == 1:
                        cand, how, conf = max(hits[0] - o, 0), 'ocr', 2 if o == 0 else 1
                        break
            if cand is None:
                ia, ib = self.ink(jp[0]), self.ink(jp[1])
                cand, how = int(len(stream) * ia / max(ia + ib, 1)), 'ink'
            wi = max(0, bisect.bisect_right(starts, cand) - 1)
            if wi + 1 < len(starts) and cand - starts[wi] > len(words[wi][2]) // 2:
                wi += 1
            tw = lambda j: self.text_of(by_id, units[words[j][0]]).split()[words[j][1]]
            out[k] = {'pages': list(pp), 'jpg': list(jp), 'how': how, 'conf': conf, 'unit': words[wi][0], 'word': words[wi][1],
                      'frac': round(cand / max(len(stream), 1), 3),
                      'tail': ' '.join(tw(j) for j in range(max(0, wi - 6), wi)), 'head': ' '.join(tw(j) for j in range(wi, min(len(words), wi + 6)))}
        (self.dir / 'candidates.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
        n = {}
        for v in out.values():
            n[(v['how'], v['conf'])] = n.get((v['how'], v['conf']), 0) + 1
        print(len(out), 'two-page scans;', n)

    def review(self, outdir, pdfs, per=3):
        from PIL import Image, ImageDraw
        outdir = Path(outdir)
        outdir.mkdir(parents=True, exist_ok=True)
        cands = json.loads((self.dir / 'candidates.json').read_text(encoding='utf-8'))

        def crop(jpg, top):
            im = Image.open(self.cfg.JPG / f'{jpg:03}.jpg').convert('L')
            w, h = im.size
            return im.crop((0, int(h * (0.0 if top else 0.66)), w, int(h * (0.24 if top else 0.96))))
        for s in range(0, len(pdfs), per):
            tiles = []
            for k in pdfs[s:s + per]:
                ja, jb = self.cfg.pdf_jpgs(k)
                a, b = crop(ja, False), crop(jb, True)
                t = Image.new('L', (max(a.width, b.width), a.height + b.height + 40), 255)
                t.paste(a, (0, 20)); t.paste(b, (0, a.height + 40))
                d = ImageDraw.Draw(t)
                d.text((4, 4), f'PDF {k}  A=p.{self.printed_of(ja)} (above)', fill=0)
                d.text((4, a.height + 24), f'B=p.{self.printed_of(jb)} (below)', fill=0)
                d.line((0, a.height + 38, t.width, a.height + 38), fill=0, width=2)
                tiles.append(t)
            sheet = Image.new('L', (sum(t.width for t in tiles) + 8 * len(tiles), max(t.height for t in tiles)), 128)
            x = 0
            for t in tiles:
                sheet.paste(t, (x, 0)); x += t.width + 8
            name = outdir / f'rev_{pdfs[s]:03}.png'
            sheet.save(name)
            print(name)
            for k in pdfs[s:s + per]:
                c = cands.get(str(k))
                if c:
                    print(f"PDF {k} [{c['how']}{c['conf']} {c['frac']}]  A ends: ...{c['tail']}   |   B starts: {c['head']}...")

    # ------------------------------------------------------------------ splits
    def read_splits(self):
        spec = {}
        for f in sorted(self.dir.glob('splits_*.txt')):
            for line in f.read_text(encoding='utf-8').splitlines():
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                k, mode, *rest = line.split(None, 2)
                e = spec.setdefault(int(k), {'V': {}})
                if mode == 'V':
                    fid, side = rest[0].split()
                    e['V'][fid] = side
                elif mode == 'ok':
                    e['mode'] = 'ok'
                else:
                    e['mode'], e['words'] = mode, rest[0]
        return spec

    def find_cut(self, units, by_id, spec, cand):
        words, starts, pos = [], [], 0
        for ui, u in enumerate(units):
            for wi, w in enumerate(self.text_of(by_id, u).split()):
                words.append((ui, wi))
                starts.append(pos)
                pos += len(norm(w))
        stream = ''.join(norm(w) for u in units for w in self.text_of(by_id, u).split())
        if spec.get('mode') == 'ok':
            return cand['unit'], cand['word']
        toks = [norm(w) for w in spec['words'].split()]
        centre = int(len(stream) * cand['frac'])
        for trim in ((0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2)):
            t = toks[trim[0]:len(toks) - trim[1]]
            ph = ''.join(t)
            if len(ph) < 6:
                continue
            hits = [m.start() for m in re.finditer(re.escape(ph), stream)]
            if hits:
                h = min(hits, key=lambda x: abs(x - centre))
                if spec['mode'] == 'A':
                    at = h + len(ph) + (sum(len(x) for x in toks[len(toks) - trim[1]:]) if trim[1] else 0)
                else:
                    at = h - (sum(len(x) for x in toks[:trim[0]]) if trim[0] else 0)
                wi = bisect.bisect_left(starts, at)
                return (len(units), 0) if wi >= len(words) else words[wi]
        raise SystemExit(f'cannot place the split "{spec["words"]}"')

    @staticmethod
    def end_sentence(tokens, at, window):
        best = None
        for i in range(max(1, at - window), min(len(tokens) - 1, at + window) + 1):
            if re.search(r'[.!?؟۔]["”’)»]*$', tokens[i - 1]):
                if best is None or abs(i - at) < abs(best - at):
                    best = i
        return best if best is not None else at

    def split_para(self, p, k):
        """Cut a paragraph at word k of its original text; the translations at the nearest sentence end."""
        o = self.cfg.ORIG
        ur = (p.get(o) or '').split()
        f = k / max(len(ur), 1)
        a, b = {o: ' '.join(ur[:k])}, {o: ' '.join(ur[k:])}
        for fld in ('urdu', 'text', 'pashto'):
            if fld == o:
                continue
            tk = (p.get(fld) or '').split()
            at = self.end_sentence(tk, round(len(tk) * f), max(4, len(tk) // 8))
            a[fld], b[fld] = ' '.join(tk[:at]), ('… ' + ' '.join(tk[at:])) if tk[at:] else ''
        return a, b

    # ------------------------------------------------------------------ DSL
    def tri_p(self, p):
        slots = [p.get(FIELD[l]) or '' for l in self.cfg.LANGS]
        return self.tri(*slots)

    @staticmethod
    def tri(a, b='', c=''):
        return ' || '.join(clean(x) for x in (a, b, c)) if (b or c) else clean(a)

    def table_lines(self, tb):
        want = 'اردو|urdu' if self.cfg.LANGS[0] == 'ur' else 'پښتو|pashto' if self.cfg.LANGS[0] == 'ps' else None
        tr = next((t for t in tb.get('translations', []) if want and re.search(want, t.get('language', ''), re.I)), tb)
        out = ['table', 'th | ' + ' | '.join(clean(h) for h in tr['headers'])]
        for r in tr['rows']:
            out.append('tr | ' + ' | '.join(clean(c) for c in r))
        return out + ['endtable']

    def svg_lines(self, b):
        pref = {'ur': 'svgUrdu', 'ps': 'svgPashto'}.get(self.cfg.LANGS[0], 'svg')
        svg = (b.get(pref) or b.get('svg') or '').replace('\r', '').strip()
        return ['svg', svg, 'endsvg']

    @staticmethod
    def bank_index(chapter):
        idx = {}
        b = chapter.get('bank') or {}
        for cat in ('mcqs', 'objective', 'shortQuestions', 'longQuestions'):
            for rec in b.get(cat, []):
                for r in rec.get('sourceReferences') or []:
                    for pi in r.get('paragraphIndices', []):
                        idx.setdefault((r['sectionId'], pi), []).append((cat, rec))
        return idx

    @staticmethod
    def answer_lines(cat, rec):
        steps = [x for x in (rec.get('steps') or []) if x]
        opts = rec.get('options') or []
        ans = ''
        if opts and isinstance(rec.get('correct'), int) and 0 <= rec['correct'] < len(opts):
            ans = opts[rec['correct']]
        elif rec.get('plainAnswer') or rec.get('answer'):
            ans = rec.get('plainAnswer') or rec.get('answer')
        if not ans and cat == 'objective' and steps:
            ans, steps = steps[0], steps[1:]
        elif ans and steps and steps[0].strip() == ans.strip():
            steps = steps[1:]
        if not ans:
            ans = 'جواب'
        if len(steps) <= 1:
            return [f"sol {clean(ans)} ## {clean(steps[0]) if steps else ''}".rstrip(' #')]
        return [f'solution {clean(ans)}'] + [f'ss {clean(x)}' for x in steps] + ['endsolution']

    # a question number at the start of a paragraph: 1۔  i۔  (a)  — books may set QNO in their config (group 1 = the number)
    QNO_DEFAULT = r'^\s*\(?(\d{1,2}|[ivxlc]{1,5}|[۰-۹]{1,2})\s*[.۔)]'
    CHOICES = re.compile(r'^\s*[\(（]\s*(?:[a-dA-D]|الف|ا|ب|ج|د)\s*[\)）]')

    def qrx(self):
        return re.compile(getattr(self.cfg, 'QNO', self.QNO_DEFAULT), re.I)

    def qno(self, s):
        m = self.qrx().match(s or '')
        return m.group(1) if m else ''

    def strip_no(self, s):
        m = self.qrx().match(s or '')
        return (s or '')[m.end():].lstrip() if m else (s or '')

    @staticmethod
    def lead_no(s):
        m = re.match(r'^\s*\(?(\d{1,2}|[ivxlc]{1,5}|[۰-۹]{1,2})\s*[.۔)]', s or '', re.I)
        return m.group(1) if m else ''

    # ------------------------------------------------------------------ generate
    def gen(self):
        c = self.cfg
        dump = self.load()
        secs = self.sections()
        by_id = {s['id']: s for s in secs}
        chapter_of = {s['id']: ch for ch in dump for s in ch['sections']}
        cands = json.loads((self.dir / 'candidates.json').read_text(encoding='utf-8')) if (self.dir / 'candidates.json').exists() else {}
        spec = self.read_splits()
        by_pdf = self.by_pdf()
        page_units, notes = {}, {}

        def put(jpg, sec, unit, para=None):
            page_units.setdefault(jpg, []).append((sec, unit, para))

        for k in sorted(by_pdf):
            group = by_pdf[k]
            r = c.route(k, group)
            if r:
                for jpg, pred in r.items():
                    for s in group:
                        if pred is None or pred(s):
                            for u in self.units_of(s):
                                put(jpg, s, u)
                continue
            jp, pp = self.scan_pages(k)
            if not jp:
                continue
            direct, stream = self.scan_streams(group, pp)
            for page, s in direct:
                for u in self.units_of(s):
                    put(jp[pp.index(page)], s, u)
            if not stream:
                continue
            units = [u for s in stream for u in self.units_of(s)]
            if len(pp) == 1:
                for u in units:
                    put(jp[0], by_id[u['sec']], u)
                continue
            sp = spec.get(k)
            if not sp:
                raise SystemExit(f'PDF {k}: no confirmed split in splits_*.txt')
            cut_u, cut_w = self.find_cut(units, by_id, sp, cands.get(str(k), {}))
            if cut_u < len(units) and cut_w and 'pi' in units[cut_u] and c.sec_kind(by_id[units[cut_u]['sec']]) == 'ex':
                para = by_id[units[cut_u]['sec']]['paras'][units[cut_u]['pi']]
                rest = (para.get(c.ORIG) or '').split()[cut_w:]
                if rest and rest[0][:1] in '(（':
                    notes.setdefault(jp[0], []).append(f'Question {self.lead_no(para.get(c.ORIG) or "")}: its bracketed choices are printed at the top of page {pp[1]}; they are shown here with the question.')
                    cut_u, cut_w = cut_u + 1, 0
            if cut_u < len(units) and cut_w and 'pi' in units[cut_u]:
                first = (by_id[units[cut_u]['sec']]['paras'][units[cut_u]['pi']].get(c.ORIG) or '').split()
                if units[cut_u]['k'] == 'h' or (cut_w == 1 and re.fullmatch(r'\(?(\d{1,2}|[ivx]{1,4}|[۰-۹]{1,2})\s*[.۔)]?', first[0])):
                    cut_w = 0
            if cut_w == 0:
                while cut_u > 0 and units[cut_u - 1]['k'] == 'h':
                    cut_u -= 1
            for ui, u in enumerate(units):
                sec = by_id[u['sec']]
                side = sp['V'].get(u['id']) if u['k'] in ('t', 'v') else None
                if side is None:
                    side = 'A' if ui < cut_u else 'B'
                if ui == cut_u and cut_w and 'pi' in u:
                    p1, p2 = self.split_para(sec['paras'][u['pi']], cut_w)
                    put(jp[0], sec, dict(u, part=1), p1)
                    put(jp[1], sec, dict(u, part=2), p2)
                    continue
                put(jp[0] if side == 'A' else jp[1], sec, u)

        order = list(range(c.TOTAL_JPG))
        ex_last = {}
        for jpg in order:
            for sec, u, over in page_units.get(jpg, []):
                if c.sec_kind(sec) == 'ex':
                    ex_last[chapter_of[sec['id']]['number']] = jpg
        started, st = set(), {'ex': None, 'sec': None, 'exch': None, 'used': set()}
        pages = {}
        for jpg in order:
            if jpg in c.DUPLICATE or jpg not in page_units:
                continue
            L = self.emit(jpg, page_units[jpg], notes.get(jpg, []), chapter_of, started, st, ex_last)
            if L is not None:
                pages[jpg] = L
        for j, src in c.DUPLICATE.items():
            pages[j] = ['@status duplicate', '@issue ' + c.NOTES.get(j, f'Scan {j} repeats scan {src}.')]
        for j in range(c.TOTAL_JPG):
            if j not in pages and (self.dir / 'fix' / f'p{j:03}.txt').exists() is False:
                pages[j] = ['@status blank', '@issue ' + getattr(c, 'BLANK', {}).get(j, 'No reviewed text for this scan (advertisement, blank or not part of the book).')]
        self.write_units()
        out = self.dir / 'pages'
        out.mkdir(exist_ok=True)
        for f in out.glob('p*.txt'):
            f.unlink()
        for j, L in sorted(pages.items()):
            fx = self.dir / 'fix' / f'p{j:03}.txt'
            txt = fx.read_text(encoding='utf-8') if fx.exists() else '\n'.join(L) + '\n'
            (out / f'p{j:03}.txt').write_text(txt, encoding='utf-8')
        missing = [j for j in range(c.TOTAL_JPG) if j not in pages]
        print('pages written', len(pages), 'missing (no content, no page file)', missing)
        if missing:
            print('  -> every JPG needs a page file: add them to fix/ as blank pages')

    def emit(self, jpg, items, notes, chapter_of, started, st, ex_last):
        c = self.cfg
        L = []
        pr = self.printed_of(jpg)
        if pr is not None:
            L += [f'@printed {pr}', '@status lesson']
        else:
            first = chapter_of[items[0][0]['id']]
            L += ['@status front-matter' if c.is_front(first) else '@status back-matter']
        L += [f'@issue {x}' for x in notes]
        cur_ex = st['ex']
        pend, lastq = [], None

        def flush():
            L.extend(pend)
            pend.clear()
        for sec, u, over in items:
            ch = chapter_of[sec['id']]
            n = ch['number']
            if n not in started:
                started.add(n)
                L.append(f"@unit {self.unit_no(ch)} | " + (self.tri(*c.FM_TITLE) if c.is_front(ch) else self.chapter_titles(ch)))
                st['sec'] = None
            kind = c.sec_kind(sec)
            sid = f'{self.unit_no(ch)}-{kind}'
            if kind != 'back' and st['sec'] != sid:
                if cur_ex and kind != 'ex':
                    L.append('endexercise')
                    cur_ex = None
                st['sec'] = sid
                ttl = {'ex': c.EX_TITLE, 'back': c.BACK_TITLE, 'text': None}[kind]
                L.append(f'@sec {sid} | ' + (self.tri(*ttl) if ttl else self.chapter_titles(ch)))
            P = sec['paras']
            if kind != 'ex' or u['k'] in ('t', 'v'):
                flush()
                lastq = None
            if u['k'] == 't':
                L += self.table_lines(next(b for b in sec['blocks'] if b['id'] == u['id']))
                continue
            if u['k'] == 'v':
                L += self.svg_lines(next(b for b in sec['blocks'] if b['id'] == u['id']))
                continue
            p = over or P[u['pi']]
            orig = p.get(c.ORIG) or ''
            if kind != 'ex':
                if not orig.strip():
                    continue
                if u['k'] == 'h':
                    lvl = '#' if self.is_chapter_title(ch, sec, p) else '##'
                    L.append(f'{lvl} {self.tri_p(p)}')
                elif u['k'] == 'li':
                    L.append(f'- {self.tri_p(p)}')
                else:
                    L.append(f'p {self.tri_p(p)}')
                continue
            # ---- exercise
            recs = [r for r in self.bank_index(ch).get((sec['id'], u.get('pi')), []) if id(r[1]) not in st['used']]
            st['exch'] = n
            if not cur_ex:
                cur_ex = clean(orig).strip(' :-') if u['k'] == 'h' and orig.strip() else c.EX_TITLE[0]
                L.append(f'exercise {cur_ex}')
                if u['k'] == 'h' and u['pi'] == 0:
                    continue
            if u.get('part') == 2:
                flush()
                L.append(f'p {self.tri_p(p)}')
                lastq = None
                for cat, rec in recs[:1]:
                    pend += self.answer_lines(cat, rec)
                    st['used'].add(id(rec))
                continue
            slots = [p.get(FIELD[l]) or '' for l in c.LANGS]
            # the choices of a multiple-choice question printed as a paragraph of their own belong to the question before them
            if lastq is not None and self.CHOICES.match(orig):
                head, _, rest = L[lastq].partition(' | ')
                parts = rest.split(' || ')
                add = [clean(x) for x in slots]
                parts = [(parts[k] if k < len(parts) else '') + ' ' + (add[k] if k < len(add) else '') for k in range(max(len(parts), len(add)))]
                L[lastq] = head + ' | ' + ' || '.join(x.strip() for x in parts)
                for cat, rec in recs[:1]:
                    st['used'].add(id(rec))
                continue
            flush()
            orig_no = self.qno(orig)
            body = self.tri(*[self.strip_no(x) for x in slots])
            rec = recs[0] if recs else None
            no = orig_no or (str(rec[1].get('qNo') or '') if rec else '')
            if orig_no and re.fullmatch(r'\d{1,2}', orig_no):
                L.append(f'q {no} | {body}'); lastq = len(L) - 1
            elif no:
                L.append(f'qp {no} | {body}'); lastq = len(L) - 1
            else:
                L.append(f'p {self.tri_p(p)}'); lastq = None
            if u.get('part') == 1:
                continue
            if rec:
                pend += self.answer_lines(rec[0], rec[1])
                st['used'].add(id(rec[1]))
        flush()
        st['ex'] = cur_ex
        if cur_ex and ex_last.get(st['exch']) == jpg:
            L.append('endexercise')
            st['ex'] = None
        return L

    def is_chapter_title(self, ch, sec, p):
        if hasattr(self.cfg, 'chapter_start_heading'):
            return self.cfg.chapter_start_heading(sec, p)
        if self.cfg.is_front(ch) or not re.search(r'text-1$', sec['id']):
            return False
        x = norm(p.get(self.cfg.ORIG) or '')
        return bool(x) and x in {norm(ch.get(f) or '') for f in ('title', 'titleEn', 'titleUrdu')}

    def unit_no(self, ch):
        """Builder unit number of a chapter: FM = 0, numbered chapters keep their number, other labels (BM, ...) follow after 100."""
        if self.cfg.is_front(ch):
            return 0
        try:
            return int(ch['number'])
        except (TypeError, ValueError):
            return 100 + [c['number'] for c in self.load()].index(ch['number'])

    def write_units(self):
        rows = []
        for ch in self.load():
            n = self.unit_no(ch)
            label = '' if isinstance(ch['number'], int) else str(ch['number'])
            t = self.chapter_titles(ch).split(' || ')
            t += [''] * (3 - len(t))
            rows.append(f"{n}\t{t[0]}\t{t[1]}\t{t[2]}\t\t{label}")
        (self.dir / 'units.tsv').write_text('\n'.join(rows).replace('{{OR}}', '||').replace('{{BAR}}', '|') + '\n', encoding='utf-8')

    def chapter_titles(self, ch):
        o = {'ur': ch.get('titleUrdu') or ch.get('title'), 'en': ch.get('titleEn') or ch.get('title'), 'ps': ch.get('titlePashto') or ''}
        if self.cfg.LANGS[0] == 'en':
            o['en'] = ch.get('title') or ch.get('titleEn')
        else:
            o['ur'] = ch.get('title') or ch.get('titleUrdu')
        return self.tri(*[o[l] for l in self.cfg.LANGS])

    # ------------------------------------------------------------------ check
    def check(self):
        c = self.cfg
        dump = self.load()
        NO = re.compile(r'^\s*(\d+|[ivx]+)\s*[۔.]\s*')
        got = {'lesson': [], 'exercise': []}
        cur_unit, in_ex = None, False
        pnos = []
        slot = c.LANGS.index({'urdu': 'ur', 'text': 'en', 'pashto': 'ps'}[c.ORIG])
        for f in sorted((self.dir / 'pages').glob('p*.txt')):
            for line in f.read_text(encoding='utf-8').splitlines():
                if line.startswith('@printed'):
                    pnos.append(int(line.split()[1]))
                elif line.startswith('@unit'):
                    cur_unit = line.split()[1]
                elif line.startswith('exercise'):
                    in_ex = True
                elif line.startswith('endexercise'):
                    in_ex = False
                elif re.match(r'(p|#|##|-|q|qp) ', line):
                    body = line.split(' ', 1)[1]
                    if line.startswith(('q ', 'qp ')) and '|' in body:
                        body = body.split('|', 1)[1]
                    parts = body.split(' || ')
                    got['exercise' if in_ex else 'lesson'].append((cur_unit, (parts[slot] if len(parts) > slot else parts[0]).replace('{{OR}}', '||').replace('{{BAR}}', '|')))
        by_id = {s['id']: s for s in self.sections()}
        for kind in ('lesson', 'exercise'):
            bad = 0
            for ch in dump:
                n = '0' if self.cfg.is_front(ch) else str(ch['number'])
                want = []
                for s in ch['sections']:
                    if (kind == 'exercise') != (c.sec_kind(s) == 'ex'):
                        continue
                    for u in self.units_of(by_id[s['id']]):
                        if 'pi' in u:
                            want += [norm(w) for w in NO.sub('', s['paras'][u['pi']].get(c.ORIG) or '').split()]
                have = [norm(w) for u, t in got[kind] if u == n for w in NO.sub('', t).split()]
                want, have = [w for w in want if w], [w for w in have if w]
                sm = difflib.SequenceMatcher(None, want, have, autojunk=False)
                if sm.ratio() < 0.995:
                    bad += 1
                    print(f'{kind} unit {n}: match {sm.ratio():.4f} want {len(want)} have {len(have)}')
                    for tag, a1, a2, b1, b2 in sm.get_opcodes():
                        if tag != 'equal':
                            print('   ', tag, ' '.join(want[a1:a2])[:80], '=>', ' '.join(have[b1:b2])[:80])
                            break
            print(kind, 'units off:', bad)
        print('printed pages', pnos[0] if pnos else None, '..', pnos[-1] if pnos else None, 'count', len(pnos))


def main():
    key, cmd, *rest = sys.argv[1:]
    b = Book(key)
    if cmd == 'review':
        b.review(rest[0], [int(x) for x in rest[1:]])
    else:
        getattr(b, cmd)()


if __name__ == '__main__':
    main()
