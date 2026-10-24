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
                ref = ref if isinstance(ref, dict) else {}
                if getattr(self.cfg, 'VIRTUAL', False):
                    labels = [x for x in (ref.get('printedPages') or ([ref['printedPage']] if ref.get('printedPage') is not None else []))]
                    out.append(dict(s, ch=ch['number'], pdf=ref.get('pdfPage'), _labels=labels))
                else:
                    out.append(dict(s, ch=ch['number'], pdf=ref.get('pdfPage'), printed=[p for p in (ref.get('printedPages') or []) if p is not None]))
        if getattr(self.cfg, 'VIRTUAL', False):
            self._virtual_keys(out)
        return out

    def _virtual_keys(self, secs):
        """Page keys of the virtual mode: a printed number (int), ('F', pdf, label) for roman / unnumbered pages before the first numbered
        scan, ('B', pdf, label) after the last one.  s['printed'] = the keys of the pages the section's text covers."""
        nums = [s['pdf'] for s in secs if s['pdf'] is not None and any(isinstance(x, int) for x in s['_labels'])]
        lo, hi = (min(nums), max(nums)) if nums else (0, 0)
        for s in secs:
            keys = []
            for x in s['_labels']:
                if isinstance(x, int):
                    keys.append(x)
                elif x is not None:
                    keys.append(('F' if s['pdf'] is None or s['pdf'] < lo else 'B', s['pdf'], str(x)))
            if not keys:
                keys.append(('F' if s['pdf'] is None or s['pdf'] < lo else 'B', s['pdf'], ''))
            nonint = [x for x in keys if not isinstance(x, int)]
            if len(nonint) > 1 and not any(isinstance(x, int) for x in keys):
                keys = nonint[:1]      # roman-numbered front matter on one scan: kept as one page
            s['printed'] = keys

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
        for n, u in enumerate(out):
            u['o'] = n
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
            if len(only) == 1:
                direct.append((only[0], s))
            else:
                stream.append(s)
        return direct, stream

    def jpg_path(self, j):
        """The N-th scan in sorted file order (the books' file names differ: 000.jpg, 000_page_1.jpg, 001.jpg, ..._page_001.jpg)."""
        if getattr(self, '_files', None) is None:
            self._files = sorted(self.cfg.JPG.glob('*.jpg'))
        return self._files[j]

    def printed_of(self, jpg):
        """Printed page number on a JPG: the config's rule (cfg.printed_of), its piecewise offsets (cfg.OFFSETS), or (one scan per
        page) the page the reviewed data names for its scan."""
        c = self.cfg
        if getattr(c, 'VIRTUAL', False):
            return jpg if isinstance(jpg, int) else None
        if hasattr(c, 'printed_of'):
            return c.printed_of(jpg)
        if hasattr(c, 'OFFSETS'):
            if jpg in getattr(c, 'NO_PAGE', ()) or jpg in getattr(c, 'DUPLICATE', {}):
                return None
            for a, b, off in c.OFFSETS:
                if a <= jpg <= b:
                    return jpg - off
            return None
        return self.label_map().get(jpg)

    def pdf_jpgs(self, k):
        """The JPG pages that scan k of the reviewed data holds (lower printed page first)."""
        c = self.cfg
        if getattr(c, 'VIRTUAL', False):
            if getattr(self, '_pj', None) is None:
                pj = {}
                for kk, group in self.by_pdf().items():
                    keys = sorted({x for s in group for x in s['printed']}, key=lambda x: (0, x) if isinstance(x, int) else (1, str(x)))
                    nums = [x for x in keys if isinstance(x, int)]
                    pj[kk] = tuple(nums) + tuple(x for x in keys if not isinstance(x, int)) if nums else tuple(keys)
                self._pj = pj
            return self._pj.get(k)
        if hasattr(c, 'pdf_jpgs'):
            return c.pdf_jpgs(k)
        if k in getattr(c, 'EXTRA_PDF', {}):
            return tuple(c.EXTRA_PDF[k])
        if getattr(self, '_pj', None) is None:
            inv = {}
            for jpg in range(c.TOTAL_JPG):
                p = self.printed_of(jpg)
                if p is not None and p not in inv:
                    inv[p] = jpg
            pj = {}
            for kk, group in self.by_pdf().items():
                pages = sorted({p for s in group for p in s['printed']})
                js = tuple(inv[p] for p in pages if p in inv)
                if js:
                    pj[kk] = js
            self._pj = pj
        return self._pj.get(k)

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
        j = self.pdf_jpgs(k)
        if getattr(self.cfg, 'VIRTUAL', False):
            return j, j
        return j, (j and tuple(self.printed_of(x) for x in j))

    # ------------------------------------------------------------------ printed page numbers of the scans
    def footers(self):
        """Read the printed page number of every JPG (RapidOCR on the footer / header strip) -> KEY/footers.json {jpg: number or null}."""
        import numpy as np
        from PIL import Image, ImageOps
        from rapidocr_onnxruntime import RapidOCR
        eng = RapidOCR()
        regions = getattr(self.cfg, 'FOOTER_REGIONS', ('bottom',))
        num = re.compile(r'^\W{0,2}\s*(\d{1,3})\s*\W{0,2}$')
        out, f = {}, self.dir / 'footers.json'
        if f.exists():
            out = {int(k): v for k, v in json.loads(f.read_text(encoding='utf-8')).items()}
        n = len(sorted(self.cfg.JPG.glob('*.jpg')))
        for j in range(n):
            if j in out:
                continue
            im = Image.open(self.jpg_path(j)).convert('L')
            w, h = im.size
            found = None
            for reg in regions:
                box = (int(w * 0.05), int(h * 0.86), int(w * 0.95), h) if reg == 'bottom' else (int(w * 0.05), 0, int(w * 0.95), int(h * 0.09))
                c = im.crop(box)
                for img in (c, ImageOps.invert(c)):
                    try:
                        r, _ = eng(np.asarray(img.convert('RGB')), use_cls=False)
                    except Exception:
                        r = None
                    nums = []
                    for x in (r or []):
                        m = num.match(x[1].strip())
                        if m:
                            nums.append(int(m.group(1)))
                    if nums:
                        found = nums[0]
                        break
                if found is not None:
                    break
            out[j] = found
            if j % 20 == 0:
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
    def ocr_files(self):
        if getattr(self.cfg, 'OCR_DOCX', None):
            return self.cfg.OCR_DOCX
        return sorted(str(p) for p in (self.cfg.JPG.parent / 'Word').glob('*.docx'))

    def ocr(self):
        import docx
        out = []
        for f in self.ocr_files():
            out.append('=====PART ' + Path(f).name)
            out += [p.text for p in docx.Document(f).paragraphs]
        (self.dir / 'ocr_word.txt').write_text('\n'.join(out), encoding='utf-8')
        print('ocr lines', len(out))

    def ocr_start(self, lines):
        """Line where the first chapter's text begins (the contents page repeats its title earlier)."""
        if getattr(self.cfg, 'OCR_START', None):
            return next((i for i, l in enumerate(lines) if l.strip() == self.cfg.OCR_START), 0)
        ch1 = next((c for c in self.load() if not self.cfg.is_front(c)), None)
        if not ch1:
            return 0
        keys = [norm(ch1.get(f) or '')[:14] for f in ('title', 'titleUrdu')]
        keys = [k for k in keys if len(k) >= 6]
        hits = [i for i, l in enumerate(lines) if any(k in norm(l) for k in keys)]
        for h in hits:
            if h > 120:
                return h
        return hits[-1] if hits else 0

    def ocr_pages(self):
        """printed page -> normalised OCR text; pages whose number line is missing are merged into the next found page."""
        lines = (self.dir / 'ocr_word.txt').read_text(encoding='utf-8').split('\n')
        start = self.ocr_start(lines)
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
        im = np.asarray(Image.open(self.jpg_path(jpg)).convert('L'), dtype=np.uint8)
        h, w = im.shape
        body = im[int(h * 0.05):int(h * 0.90), int(w * 0.04):int(w * 0.96)]
        return int((body < 110).sum())

    def by_pdf(self):
        d = {}
        for s in self.sections():
            if s['pdf'] is not None:      # sections without a source scan are SpaceBook study aids, not book pages
                d.setdefault(s['pdf'], []).append(s)
        return d

    def two_page_scans(self):
        out = []
        for k, group in sorted(self.by_pdf().items()):
            jp, pp = self.scan_pages(k)
            if not jp or len(jp) != 2:
                continue
            r = self.cfg.route(k, group) if hasattr(self.cfg, 'route') else None
            if r:
                group = [s for s in group if not any(p is None or p(s) for p in r.values())]
            stream = self.scan_streams(group, pp)[1]
            units = [u for s in stream for u in self.units_of(s)]
            if units:
                out.append((k, jp, pp, units))
        return out

    def rocr(self, force=False):
        """RapidOCR of the lines at the page boundary of every two-page scan -> KEY/rocr.json:
        {pdf: {'A': [last lines of the first page, bottom first], 'B': [first lines of the second page, top first], 'text': {...old strips}}}.
        Works for Latin-script books (English, Computer Science, Physics ...); the Urdu books use the Word OCR instead."""
        import numpy as np
        from PIL import Image
        from rapidocr_onnxruntime import RapidOCR
        eng = RapidOCR()
        f = self.dir / 'rocr.json'
        out = {} if force or not f.exists() else json.loads(f.read_text(encoding='utf-8'))
        junk = re.compile(r'(?i)not\s*for\s*sale|awaz|whatsapp|^\W*\d{1,3}\W*$')
        for k, jp, pp, units in self.two_page_scans():
            if str(k) in out and isinstance(out[str(k)].get('A'), list):
                continue
            res = {}
            for tag, j_, box in (('B', jp[1], (0, 0.02, 1, 0.34)), ('A', jp[0], (0, 0.62, 1, 0.96))):
                im = Image.open(self.jpg_path(j_)).convert('RGB')
                w, h = im.size
                c = im.crop((0, int(h * box[1]), w, int(h * box[3])))
                arr = np.asarray(c)
                try:
                    import cv2
                    g = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
                    g = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8)).apply(g)
                    g = cv2.resize(g, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
                    arr = cv2.cvtColor(g, cv2.COLOR_GRAY2RGB)
                    sc_ = 1.5
                except Exception:
                    sc_ = 1.0
                try:
                    r, _ = eng(arr, use_cls=False)
                except Exception:
                    r = None
                lines = []
                for b, txt, sc in (r or []):
                    ys = [q[1] / sc_ for q in b]; xs = [q[0] / sc_ for q in b]
                    txt = txt.strip()
                    if junk.search(txt) or len(norm(txt)) < 8 or (max(xs) - min(xs)) < 0.22 * w:
                        continue
                    lines.append((sum(ys) / 4, txt))
                lines.sort(key=lambda x: x[0], reverse=(tag == 'A'))
                res[tag] = [x[1] for x in lines[:3]]
            out[str(k)] = res
            if len(out) % 10 == 0:
                f.write_text(json.dumps(out, ensure_ascii=False), encoding='utf-8')
        f.write_text(json.dumps(out, ensure_ascii=False), encoding='utf-8')
        print('rocr scans', len(out))

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
            rr = (json.loads((self.dir / 'rocr.json').read_text(encoding='utf-8')) if (self.dir / 'rocr.json').exists() else {}).get(str(k)) or {}

            def fuzzy(q, tail):
                """Best position (char offset in the stream) where the line q ends (tail) or starts, and its ratio."""
                q = norm(q)
                if len(q) < 10:
                    return None, 0.0
                best_ = (0.0, None)
                for i_ in range(len(words)):
                    if tail:
                        e0 = starts[i_] + len(words[i_][2])
                        seg = stream[max(0, e0 - len(q)):e0]
                        pos_ = e0
                    else:
                        seg = stream[starts[i_]:starts[i_] + len(q)]
                        pos_ = starts[i_]
                    if len(seg) < len(q) * 0.7:
                        continue
                    sm_ = difflib.SequenceMatcher(None, q, seg, autojunk=False)
                    if sm_.real_quick_ratio() < 0.7 or sm_.quick_ratio() < 0.7:
                        continue
                    r_ = sm_.ratio()
                    if r_ > best_[0]:
                        best_ = (r_, pos_)
                return best_[1], best_[0]
            fa = fb = None
            ra = rb = 0.0
            for q in (rr.get('A') or [])[:2]:
                fa, ra = fuzzy(q, True)
                if fa is not None and ra >= 0.78:
                    break
            for q in (rr.get('B') or [])[:2]:
                fb, rb = fuzzy(q, False)
                if fb is not None and rb >= 0.78:
                    break
            ca = fa if ra >= 0.78 else None
            cb = fb if rb >= 0.78 else None
            if ca is not None and cb is not None and abs(ca - cb) <= 10 and min(ra, rb) >= 0.85:
                cand, how, conf = (ca + cb) // 2, 'ln', 4
            elif ca is not None and cb is not None and abs(ca - cb) <= 40:
                cand, how, conf = (ca + cb) // 2, 'ln', 3
            elif cb is not None and rb >= 0.9:
                cand, how, conf = cb, 'ln', 2
            elif ca is not None and ra >= 0.9:
                cand, how, conf = ca, 'ln', 2
            if cand is None:
                if getattr(self.cfg, 'VIRTUAL', False):
                    cand, how = len(stream) // 2, 'half'
                else:
                    ia, ib = self.ink(jp[0]), self.ink(jp[1])
                    cand, how = int(len(stream) * ia / max(ia + ib, 1)), 'ink'
            def at_word(c_):
                w_ = max(0, bisect.bisect_right(starts, c_) - 1)
                if w_ + 1 < len(starts) and c_ - starts[w_] > len(words[w_][2]) // 2:
                    w_ += 1
                return w_
            tw = lambda j: self.text_of(by_id, units[words[j][0]]).split()[words[j][1]]
            wi = at_word(cand)
            opts = {}
            pos_opts = {'ca': ca, 'cb': cb}
            if cand is not None and how == 'ocr':
                pos_opts['ocr'] = cand
            if not getattr(self.cfg, 'VIRTUAL', False):
                ia_, ib_ = self.ink(jp[0]), self.ink(jp[1])
                pos_opts['ink'] = int(len(stream) * ia_ / max(ia_ + ib_, 1))
            if b_pg in pages and a_pg not in merged and 'ocr' not in pos_opts:
                ocr_b2 = pages.get(b_pg, '')
                for o in (0, 12, 30, 60):
                    key = ocr_b2[o:o + 20]
                    if len(key) >= 16:
                        hits = [m.start() for m in re.finditer(re.escape(key), stream)]
                        if len(hits) == 1:
                            pos_opts['ocr'] = max(hits[0] - o, 0)
                            break
            for lab, c_ in pos_opts.items():
                if c_ is None:
                    continue
                w_ = at_word(c_)
                opts[lab] = {'unit': words[w_][0], 'word': words[w_][1], 'frac': round(c_ / max(len(stream), 1), 3),
                             'tail': ' '.join(tw(j) for j in range(max(0, w_ - 5), w_)), 'head': ' '.join(tw(j) for j in range(w_, min(len(words), w_ + 5)))}
            out[k] = {'pages': [str(x) for x in pp], 'jpg': [x if isinstance(x, int) else str(x) for x in jp], 'how': how, 'conf': conf, 'unit': words[wi][0], 'word': words[wi][1],
                      'frac': round(cand / max(len(stream), 1), 3), 'opts': opts,
                      'tail': ' '.join(tw(j) for j in range(max(0, wi - 6), wi)), 'head': ' '.join(tw(j) for j in range(wi, min(len(words), wi + 6)))}
        (self.dir / 'candidates.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
        n = {}
        for v in out.values():
            n[(v['how'], v['conf'])] = n.get((v['how'], v['conf']), 0) + 1
        print(len(out), 'two-page scans;', n)

    def autosplit(self):
        """splits_auto.txt: 'ok' for every two-page scan whose Word-OCR cut agrees with the ink share of the two scans (|diff| <= 0.10);
        the others are listed for a look at the scans (review)."""
        cands = json.loads((self.dir / 'candidates.json').read_text(encoding='utf-8'))
        done = set()
        for f in sorted(self.dir.glob('splits_*.txt')):
            if f.name != 'splits_auto.txt':
                for line in f.read_text(encoding='utf-8').splitlines():
                    if line.strip() and not line.startswith('#'):
                        done.add(int(line.split()[0]))
        auto, todo = [], []
        for k, v in sorted(cands.items(), key=lambda kv: int(kv[0])):
            k = int(k)
            if k in done:
                continue
            jp = v['jpg']
            if getattr(self.cfg, 'VIRTUAL', False):
                ink = v['frac']
            else:
                ia, ib = self.ink(jp[0]), self.ink(jp[1])
                ink = ia / max(ia + ib, 1)
            if ((v['how'] == 'ocr' and v['conf'] == 2 and abs(v['frac'] - ink) <= 0.12) or (v['how'] == 'ln' and v['conf'] >= 4 and abs(v['frac'] - ink) <= 0.30)):
                auto.append(f'{k} ok')
            else:
                todo.append((k, v['how'], v['conf'], v['frac'], round(ink, 3)))
        f = self.dir / 'splits_auto.txt'
        f.write_text('# accepted automatically: the Word OCR page break agrees with the ink share of the two scans\n' + '\n'.join(auto) + '\n', encoding='utf-8')
        print(len(auto), 'accepted;', len(todo), 'to review:', ' '.join(str(x[0]) for x in todo))

    def review(self, outdir, pdfs, per=3):
        from PIL import Image, ImageDraw
        outdir = Path(outdir)
        outdir.mkdir(parents=True, exist_ok=True)
        cands = json.loads((self.dir / 'candidates.json').read_text(encoding='utf-8'))

        def crop(jpg, top):
            im = Image.open(self.jpg_path(jpg)).convert('L')
            w, h = im.size
            return im.crop((0, int(h * (0.0 if top else 0.66)), w, int(h * (0.24 if top else 0.96))))
        for s in range(0, len(pdfs), per):
            tiles = []
            for k in pdfs[s:s + per]:
                ja, jb = self.pdf_jpgs(k)
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
                    print(f"PDF {k}  pages {'-'.join(c['pages'])}")
                    for lab, o in (c.get('opts') or {}).items():
                        print(f"   {lab:4} ...{o['tail']}  |  {o['head']}...")

    # ------------------------------------------------------------------ splits
    def read_splits(self):
        spec = {}
        for f in sorted(self.dir.glob('splits_*.txt')):
            for line in f.read_text(encoding='utf-8').splitlines():
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                k, mode, *rest = line.split(None, 2)
                e = spec.setdefault(int(k), {'V': {}, 'T': {}})
                if mode == 'V':
                    fid, side = rest[0].split()
                    e['V'][fid] = side
                elif mode == 'T':
                    fid, n_ = rest[0].split()
                    e['T'][fid] = int(n_)
                elif mode == 'N':       # the text from these words on is the first page of the NEXT scan (the reviewed record runs on into it)
                    e['N'] = rest[0]
                elif mode == 'TN':      # a table that goes on at the top of the NEXT scan's first page: rows before n stay, the rest move there
                    fid, n_ = rest[0].split()
                    e.setdefault('TN', {})[fid] = int(n_)
                elif mode == 'M':       # one table over several pages: rows per page, starting on the scan's second page
                    fid, *cnt = rest[0].split()
                    e.setdefault('M', {})[fid] = [int(x) for x in cnt]
                elif mode in ('ok', 'para', 'ink', 'ca', 'cb', 'ocr'):
                    e['mode'] = mode
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
        if spec.get('mode') == 'para':          # summarised text: no words to find, cut at the paragraph boundary nearest the ink share of the two scans
            o = (cand.get('opts') or {}).get('ink') or {'frac': cand['frac']}
            target = o['frac'] * len(stream)
            best = None
            for ui, u in enumerate(units):
                if 'pi' not in u or u['k'] in ('l', 'li'):
                    continue
                pos_ = next((starts[i] for i, (uj, wj) in enumerate(words) if uj == ui and wj == 0), None)
                if pos_ is not None and (best is None or abs(pos_ - target) < abs(best[0] - target)):
                    best = (pos_, ui)
            if best is None:
                raise SystemExit('no paragraph to cut at')
            return best[1], 0
        if spec.get('mode') in ('ca', 'cb', 'ink', 'ocr'):
            o = (cand.get('opts') or {}).get(spec['mode'])
            if not o:
                raise SystemExit(f'split option {spec["mode"]} is not available for this scan')
            return o['unit'], o['word']
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
        # my reading of the scan may spell a word differently from the reviewed data: take the best matching run of words
        nw = [norm(w) for u in units for w in self.text_of(by_id, u).split()]
        n = len(toks)
        best = (0, None)
        for i in range(0, max(len(nw) - n + 1, 0)):
            r = difflib.SequenceMatcher(None, ''.join(toks), ''.join(nw[i:i + n])).ratio()
            r -= 0.15 * abs(starts[i] - centre) / max(len(stream), 1)
            if r > best[0]:
                best = (r, i)
        if best[1] is not None and best[0] >= 0.75:
            i = best[1]
            wi = i + n if spec['mode'] == 'A' else i
            print(f'   (approximate match {best[0]:.2f} for "{spec["words"]}")')
            return (len(units), 0) if wi >= len(words) else words[wi]
        raise SystemExit(f'cannot place the split "{spec["words"]}" (best {best[0]:.2f})')

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

    def table_lines(self, tb, rows=None, nohead=False):
        want = 'اردو|urdu' if self.cfg.LANGS[0] == 'ur' else 'پښتو|pashto' if self.cfg.LANGS[0] == 'ps' else None
        tr = next((t for t in tb.get('translations', []) if want and re.search(want, t.get('language', ''), re.I)), tb)
        out = ['table'] + ([] if nohead or not any(tr.get('headers') or []) else ['th | ' + ' | '.join(clean(h) for h in tr['headers'])])
        for r in (tr['rows'][rows[0]:rows[1]] if rows else tr['rows']):
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
            r = c.route(k, group) if hasattr(c, 'route') else None
            if r:
                taken = set()
                for jpg, pred in r.items():
                    for s in group:
                        if pred is None or pred(s):
                            taken.add(s['id'])
                            for u in self.units_of(s):
                                put(jpg, s, u)
                group = [s for s in group if s['id'] not in taken]
                if not group:
                    continue
            jp, pp = self.scan_pages(k)
            if not jp:
                continue
            direct, stream = self.scan_streams(group, pp)
            sp0 = spec.get(k) or {}
            for page, s in direct:
                us = self.units_of(s)
                nc = None
                if sp0.get('N') and page == pp[-1] and max(s['printed']) > pp[-1]:      # the section runs on into the next scan's first page
                    nc = self.find_cut(us, by_id, {'mode': 'B', 'words': sp0['N']}, {'frac': 0.97})
                for ui, u in enumerate(us):
                    if nc and (ui > nc[0] or (ui == nc[0] and nc[1] == 0)):
                        put(jp[-1] + 1, s, u)
                    elif nc and ui == nc[0] and nc[1] and 'pi' in u:
                        p1, p2 = self.split_para(s['paras'][u['pi']], nc[1])
                        put(jp[pp.index(page)], s, dict(u, part=1), p1)
                        put(jp[-1] + 1, s, dict(u, part=2), p2)
                    else:
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
            if sp.get('mode') is None:                       # only T / V lines: no text to cut, every other unit stays on the first page
                cut_u, cut_w = len(units), 0
            else:
                cut_u, cut_w = self.find_cut(units, by_id, sp, cands.get(str(k), {}))
            ncut = self.find_cut(units, by_id, {'mode': 'B', 'words': sp['N']}, {'frac': 0.97}) if sp.get('N') else None
            nextpage = jp[1] + 1
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
                if u['k'] == 't' and u['id'] in sp.get('TN', {}):
                    n_ = sp['TN'][u['id']]
                    on_a = (sp['V'].get(u['id']) or ('A' if ui < cut_u else 'B')) == 'A'
                    put(jp[0] if on_a else jp[1], sec, dict(u, rows=(0, n_)))
                    put(nextpage, sec, dict(u, rows=(n_, None), nohead=True))
                    continue
                if u['k'] == 't' and u['id'] in sp.get('M', {}):
                    a_ = 0
                    for i_, n_ in enumerate(sp['M'][u['id']]):
                        put(jp[1] + i_, sec, dict(u, rows=(a_, a_ + n_), nohead=bool(i_)))
                        a_ += n_
                    continue
                if u['k'] == 't' and u['id'] in sp.get('T', {}):
                    n_ = sp['T'][u['id']]
                    put(jp[0], sec, dict(u, rows=(0, n_)))
                    put(jp[1], sec, dict(u, rows=(n_, None), nohead=True))
                    continue
                side = sp['V'].get(u['id']) if u['k'] in ('t', 'v') else None
                if ncut and side is None and (ui > ncut[0] or (ui == ncut[0] and ncut[1] == 0)):
                    put(nextpage, sec, u)
                    continue
                if ncut and ui == ncut[0] and ncut[1] and 'pi' in u:
                    p1, p2 = self.split_para(sec['paras'][u['pi']], ncut[1])
                    put(jp[0] if ui < cut_u else jp[1], sec, dict(u, part=1), p1)
                    put(nextpage, sec, dict(u, part=2), p2)
                    continue
                if side is None:
                    side = 'A' if ui < cut_u else 'B'
                if ui == cut_u and cut_w and 'pi' in u:
                    p1, p2 = self.split_para(sec['paras'][u['pi']], cut_w)
                    put(jp[0], sec, dict(u, part=1), p1)
                    put(jp[1], sec, dict(u, part=2), p2)
                    continue
                put(jp[0] if side == 'A' else jp[1], sec, u)

        sec_index = {s['id']: n for n, s in enumerate(secs)}
        for jpg in page_units:
            page_units[jpg].sort(key=lambda it: (sec_index[it[0]['id']], it[1].get('o', 0), it[1].get('part', 0)))
        virtual = getattr(c, 'VIRTUAL', False)
        if virtual:
            def okey(x):
                if isinstance(x, int):
                    return (1, x, 0, '')
                return (0 if x[0] == 'F' else 2, 0, x[1] or 0, x[2])
            order = sorted(page_units, key=okey)
        else:
            order = list(range(c.TOTAL_JPG))
        ex_last = {}
        for jpg in order:
            for sec, u, over in page_units.get(jpg, []):
                if c.sec_kind(sec) == 'ex':
                    ex_last[chapter_of[sec['id']]['number']] = jpg
        started, st = set(), {'ex': None, 'sec': None, 'exch': None, 'used': set()}
        pages = {}
        for jpg in order:
            if (not virtual and jpg in c.DUPLICATE) or jpg not in page_units:
                continue
            L = self.emit(jpg, page_units[jpg], notes.get(jpg, []), chapter_of, started, st, ex_last)
            if L is not None:
                pages[jpg] = L
        if virtual:
            slot = {key: n for n, key in enumerate(order)}
            pages = {slot[key]: L for key, L in pages.items()}
            (self.dir / 'meta.json').write_text(json.dumps({'total': len(pages)}), encoding='utf-8')
        for j, src in ({} if virtual else c.DUPLICATE).items():
            pages[j] = ['@status duplicate', '@issue ' + c.NOTES.get(j, f'Scan {j} repeats scan {src}.')]
        for j in range(0 if virtual else c.TOTAL_JPG):
            if j not in pages and (self.dir / 'fix' / f'p{j:03}.txt').exists() is False:
                pages[j] = ['@status blank', '@issue ' + getattr(c, 'BLANK', {}).get(j, 'No reviewed text for this scan (advertisement, blank or not part of the book).')]
        for fx in (self.dir / 'fix').glob('p[0-9][0-9][0-9].txt'):
            pages.setdefault(int(fx.stem[1:]), [])
        self.write_units()
        out = self.dir / 'pages'
        out.mkdir(exist_ok=True)
        for f in out.glob('p*.txt'):
            f.unlink()
        for j, L in sorted(pages.items()):
            fx = self.dir / 'fix' / f'p{j:03}.txt'
            txt = fx.read_text(encoding='utf-8') if fx.exists() else '\n'.join(L) + '\n'
            (out / f'p{j:03}.txt').write_text(txt, encoding='utf-8')
        missing = [] if virtual else [j for j in range(c.TOTAL_JPG) if j not in pages]
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
            L += ['@status front-matter' if c.is_front(first) else ('@status lesson' if not str(first['number']).isdigit() else '@status back-matter')]   # a back-matter UNIT keeps its own pages
        L += [f'@issue {x}' for x in notes]
        cur_ex = st['ex']
        pend, lastq = [], None

        def flush():
            L.extend(pend)
            pend.clear()
        for sec, u, over in items:
            ch = chapter_of[sec['id']]
            n = ch['number']
            kind = c.sec_kind(sec)
            sid = f'{self.unit_no(ch)}-{kind}'
            if pend and (n not in started or (kind != 'back' and st['sec'] != sid) or kind != 'ex'):
                flush()      # the answers of the last question come before the next unit / section / end of the exercise
                lastq = None
            if n not in started:
                started.add(n)
                L.append(f"@unit {self.unit_no(ch)} | " + (self.tri(*c.FM_TITLE) if c.is_front(ch) else self.chapter_titles(ch)))
                st['sec'] = None
            if st['sec'] != sid:
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
                L += self.table_lines(next(b for b in sec['blocks'] if b['id'] == u['id']), u.get('rows'), u.get('nohead', False))
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
                is_title = u['k'] == 'h' and orig.strip() and re.search(r'مشق|سوال|exercise|تمرین|پوښتن', orig, re.I)
                cur_ex = clean(orig).strip(' :-') if is_title else c.EX_TITLE[0]
                L.append(f'exercise {cur_ex}')
                if is_title and u['pi'] == 0:
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
            if orig_no and re.fullmatch(r'\d{1,2}', orig_no) and not (u['k'] == 'l' and getattr(c, 'LINE_PARTS', False)):
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
        NO = re.compile(r'^\s*[(（]?(\d{1,2}|[ivxlc]{1,5}|[۰-۹]{1,2})[)）]?\s*[۔.:\-]?\s+(?=\S)|^\s*[(（]?(\d{1,2}|[ivxlc]{1,5}|[۰-۹]{1,2})[)）]?\s*[۔.:\-]\s*')
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
                n = str(self.unit_no(ch))
                want = []
                for s in ch['sections']:
                    if (kind == 'exercise') != (c.sec_kind(s) == 'ex'):
                        continue
                    for u in self.units_of(by_id[s['id']]):
                        if 'pi' in u:
                            txt = s['paras'][u['pi']].get(c.ORIG) or ''
                            if kind == 'exercise' and u['k'] == 'h' and u['pi'] == 0 and re.search(r'مشق|سوال|exercise|تمرین|پوښتن', txt, re.I):
                                continue
                            want += [norm(w) for w in NO.sub('', txt).split()]
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
