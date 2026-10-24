# -*- coding: utf-8 -*-
"""Page-by-page builder for the Class 11 books (the reviewed data is already one record per scanned page: js/<name>_11_data.js).

    python -X utf8 engine11.py KEY dump     node dump11.cjs -> class-11/KEY/dump.json
    python -X utf8 engine11.py KEY gen      class-11/KEY/pages/pNNN.txt: one file per printed page, in book order
    python -X utf8 engine11.py KEY check    every word of the data appears once, in order

A page is a run of sections with the same printed number (sections without one: the same scan).  The page syntax is the one of the Class 6-12
books (class-6/tools/build_math6.py); class-11/tools/build_book11.py KEY builds it into js/<name>_11_book.js (window.CLS11_BOOKS).
"""
import difflib, json, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CLASS12 = HERE.parent
APP = CLASS12.parents[2]
CLASS11 = CLASS12.parent / 'class-11'

BOOKS = {  # key: (js file, global, subject key of the reader, title, medium)
    'civics': ('civics_11_data.js', 'CIVICS_11_DATA', 'civics', ('Civics', 'civics_11_book.js', 'CIVICS_11_BOOK', 'Shehriyat 11 (KPTBB, Urdu medium)')),
    'hpe': ('hpe_11_data.js', 'HPE_11_DATA', 'hpe', ('Health & Physical Education', 'hpe_11_book.js', 'HPE_11_BOOK', 'Health & Physical Education 11 (KPTBB, Urdu medium)')),
    'ikhtiari': ('ikhtiari_11_data.js', 'IKHTIARI_11_DATA', 'islopt', ('Islamiat Ikhtiari', 'ikhtiari_11_book.js', 'IKHTIARI_11_BOOK', 'Islamiat Ikhtiari 11 (KPTBB, Urdu medium)')),
    'ishist': ('ishist_11_data.js', 'ISHIST_11_DATA', 'islhist', ('Islamic History', 'ishist_11_book.js', 'ISHIST_11_BOOK', 'Islamic History 11 (KPTBB, Urdu medium)')),
    'isl': ('isl_11_data.js', 'ISL_11_DATA', 'islc', ('Islamiat', 'isl_11_book.js', 'ISL_11_BOOK', 'Islamiat Lazmi 11 (KPTBB, Urdu medium)')),
    'mq': ('mq_11_data.js', 'MQ_11_DATA', 'quran', ('Mutalia-e-Quran', 'mq_11_book.js', 'MQ_11_BOOK', 'Mutalia-e-Quran Hakeem 11 (KPTBB, Urdu medium)')),
    'urdu': ('urdu_11_data.js', 'URDU_11_DATA', 'urdu', ('Urdu', 'urdu_11_book.js', 'URDU_11_BOOK', 'Urdu 11 (KPTBB, Urdu medium)')),
    'cs': ('cs_11_data.js', 'CS_11_DATA', 'comp', ('Computer Science', 'cs_11_book.js', 'CS_11_BOOK', 'Computer Science 11 (KPTBB, English medium)')),
    'chem': ('chem_11_data.js', 'CHEM_11_DATA', 'chem', ('Chemistry', 'chem_11_book.js', 'CHEM_11_BOOK', 'Chemistry 11 (KPTBB, English medium)')),
    'bio': ('bio_11_data.js', 'BIO_11_DATA', 'bio', ('Biology', 'bio_11_book.js', 'BIO_11_BOOK', 'Biology 11 (KPTBB, English medium)')),
    'stat': ('stat_11_data.js', 'STAT_11_DATA', 'stat', ('Statistics', 'stat_11_book.js', 'STAT_11_BOOK', 'Statistics 11 (KPTBB, English medium)')),
    'eng': ('eng_11_data.js', 'ENG_11_DATA', 'eng', ('English', 'eng_11_book.js', 'ENG_11_BOOK', 'English 11 (KPTBB, English medium)')),
    'phys': ('phys_11_data.js', 'PHYS_11_DATA', 'phys', ('Physics', 'phys_11_book.js', 'PHYS_11_BOOK', 'Physics 11 (KPTBB, English medium)')),
}
TR = str.maketrans({'ي': 'ی', 'ى': 'ی', 'ے': 'ی', 'ك': 'ک', 'ه': 'ہ', 'ۃ': 'ہ', 'ة': 'ہ', 'ھ': 'ہ', 'ۂ': 'ہ', 'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ؤ': 'و', 'ئ': 'ی',
                    '۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4', '۵': '5', '۶': '6', '۷': '7', '۸': '8', '۹': '9'})
EX_TITLES = {'ur': ('مشق', 'Exercise', 'تمرین'), 'en': ('Exercise', 'مشق', 'تمرین')}


def norm(s):
    s = re.sub(r'[ً-ٰٟٕٔ‌‍‎‏]', '', s).translate(TR)
    return re.sub(r'[^\w]|_', '', s.lower())


def clean(s):
    return re.sub(r'\s+', ' ', (s or '').replace('||', '{{OR}}').replace('|', '{{BAR}}').replace('##', '#')).strip()


def tri(a, b='', c=''):
    return ' || '.join(clean(x) for x in (a, b, c)) if (b or c) else clean(a)


class Book11:
    def __init__(self, key):
        self.key = key
        self.file, self.glob, self.view, self.name = BOOKS[key]
        self.dir = CLASS11 / key
        self.dir.mkdir(parents=True, exist_ok=True)
        self._d = None

    def dump(self):
        subprocess.run(['node', str(HERE / 'dump11.cjs'), self.file, self.glob, str(self.dir / 'dump.json')], check=True, cwd=APP)

    def data(self):
        if self._d is None:
            self._d = json.loads((self.dir / 'dump.json').read_text(encoding='utf-8'))
        return self._d

    # -------------------------------------------------------------- language slots
    def urdu_medium(self):
        n_en = n_ur = 0
        for ch in self.data():
            for s in ch.get('sections') or []:
                for p in s.get('paras') or []:
                    if 'english' in p:
                        n_ur += 1
                    elif 'urdu' in p:
                        n_en += 1
        return n_ur > n_en

    def langs(self):
        return ['ur', 'en', 'ps'] if self.urdu_medium() else ['en', 'ur', 'ps']

    def slots(self, p):
        o = p.get('original') if p.get('original') is not None else p.get('text')
        o = self.inline(o or '', p)
        if 'english' in p:
            return [o, self.inline(p.get('english') or '', p), self.inline(p.get('pashto') or '', p)]
        return [o, self.inline(p.get('urdu') or '', p), self.inline(p.get('pashto') or '', p)]

    @staticmethod
    def inline(text, p):
        for m in p.get('inlineMath') or []:
            text = text.replace(m['token'], f"({m['numerator']})/({m['denominator']})" if m.get('denominator') else f"{m.get('base')}_{m.get('subscript')}")
        return text

    # -------------------------------------------------------------- pages
    def unit_no(self, ch):
        n = ch['number']
        if n == 'FM':
            return 0
        try:
            return 50 if int(n) == 0 else int(n)       # a chapter numbered 0 must not collide with the front matter (0)
        except (TypeError, ValueError):
            return 100 + [c['number'] for c in self.data()].index(n)

    def runs(self):
        """Pages in book order: consecutive sections on the same printed page (or, with no number, the same scan)."""
        out, last = [], None
        for ch in self.data():
            for s in ch.get('sections') or []:
                src = s.get('source') or {}
                pr, pdf = src.get('printedPage'), src.get('pdfPage')
                pr = None if pr in (None, '', '—', '-') else str(pr)
                key = ('p', pr) if pr is not None else ('s', pdf)
                if last is not None and out and out[-1]['key'] == key:
                    out[-1]['secs'].append((ch, s))
                else:
                    out.append({'key': key, 'printed': pr, 'pdf': pdf, 'secs': [(ch, s)]})
                last = key
        return out

    def items(self, s):
        paras = {p['id']: p for p in s.get('paras') or [] if 'id' in p}
        tables = s.get('tables') or ([s['table']] if isinstance(s.get('table'), dict) else [])
        figs = s.get('figures') or ([s['figure']] if isinstance(s.get('figure'), dict) else [])
        eqs = s.get('equations') or []
        flow = s.get('flow')
        if not flow:
            out = [('p', p) for p in s.get('paras') or []]
            out += [('e', e) for e in eqs if isinstance(e, dict)]
            out += [('f', f) for f in figs]
            return out
        out = []
        if flow and isinstance(flow[0], list):          # Physics: [["p", index], ["e", index], ["t", index], ["f", index]]
            pl = s.get('paras') or []
            for kind, i in flow:
                if kind == 'p' and i < len(pl):
                    out.append(('p', pl[i]))
                elif kind == 'e' and i < len(eqs) and isinstance(eqs[i], dict):
                    out.append(('e', eqs[i]))
                elif kind == 't' and i < len(tables):
                    out.append(('t', tables[i]))
                elif kind == 'f' and i < len(figs):
                    out.append(('f', figs[i]))
            return out
        for f in flow:
            if f['type'] == 'paragraphs':
                out += [('p', paras[i]) for i in f['ids'] if i in paras]
            elif f['type'] == 'table':
                if tables:
                    out.append(('t', tables[min(f.get('index') or 0, len(tables) - 1)]))
            elif f['type'] == 'figure':
                if figs:
                    out.append(('f', figs[min(f.get('index') or 0, len(figs) - 1)]))
            elif f['type'] == 'equation':
                if eqs:
                    out.append(('e', eqs[min(f.get('index') or 0, len(eqs) - 1)]))
        return out

    BOXES = {'aside', 'tidbit', 'fyi', 'dyk', 'box', 'note', 'activity', 'readingCheck', 'project', 'box-body', 'lead-in'}
    HEADS = {'heading', 'subheading', 'exampleHeading', 'solutionHeading', 'box-title', 'box-subtitle', 'exercise-heading', 'glossary-letter', 'index-letter', 'authors-title', 'form-title', 'anthem-title', 'form-header'}

    def table_lines(self, t):
        orig = 'ur' if self.urdu_medium() else 'en'
        cell = lambda c: clean(c.get(orig) or c.get('en') or '') if isinstance(c, dict) else clean(c)
        out = ['table' + (' ' + tri(t.get('captionUrdu') or t.get('caption') or '', t.get('caption') or '', t.get('captionPashto') or '') if (t.get('caption') or t.get('captionUrdu')) else '')]
        if t.get('headers'):
            out.append('th | ' + ' | '.join(cell(h) for h in t['headers']))
        for r in t.get('rows') or []:
            out.append('tr | ' + ' | '.join(cell(c) for c in r))
        return out + ['endtable']

    # -------------------------------------------------------------- gen
    def gen(self):
        runs = self.runs()
        ur = self.urdu_medium()
        ex_title = EX_TITLES['ur' if ur else 'en']
        started, st = set(), {'sec': None, 'ex': None}
        pages = []
        for n, run in enumerate(runs):
            L = []
            pr = run['printed']
            if pr is not None and pr.isdigit():
                L += [f'@printed {int(pr)}', '@status lesson']
            else:
                first_ch = run['secs'][0][0]
                L += ['@status front-matter' if first_ch['number'] == 'FM' else '@status lesson']
            pend, ctx = [], {'q': None, 'has_q': st.get('has_q', False)}
            for ch, s in run['secs']:
                unit = self.unit_no(ch)
                if ch['number'] not in started:
                    started.add(ch['number'])
                    L.append(f'@unit {unit} | ' + self.titles(ch))
                    st['sec'] = None
                QR = ('question', 'option', 'solution', 'sourceAnswer', 'source-answer', 'subquestion')
                has_ex = any(p.get('tab') == 'exercise' or p.get('role') in QR or p.get('exerciseId') for p in s.get('paras') or [])
                kind = 'ex' if has_ex else 'text'
                if st['sec'] != (unit, kind):
                    if st['ex'] and kind != 'ex':
                        L += pend; pend.clear()
                        L.append('endexercise'); st['ex'] = None
                    st['sec'] = (unit, kind)
                    L.append(f'@sec {unit}-{kind} | ' + (tri(*ex_title) if kind == 'ex' else self.titles(ch)))
                for it in self.items(s):
                    typ, obj = it
                    if typ == 't':
                        L += self.table_lines(obj); ctx['q'] = None
                    elif typ == 'f':
                        svg = (obj.get('svg') or '').strip()
                        cap = obj.get('caption') or ''
                        if isinstance(cap, dict):
                            cen, cur, cps = cap.get('en') or '', cap.get('ur') or '', cap.get('ps') or ''
                        else:
                            cen, cur, cps = cap, obj.get('captionUrdu') or '', obj.get('captionPashto') or ''
                        capline = tri(*( [cur or cen, cen, cps] if ur else [cen, cur, cps] )) if (cen or cur) else ''
                        if svg:
                            L += ['svg' + (' ' + capline if capline else ''), svg, 'endsvg']
                        elif capline:
                            L.append('p ' + capline)
                        ctx['q'] = None
                    elif typ == 'e':
                        tex = obj.get('latex') or obj.get('fallback') or obj.get('accessible') or ''
                        if tex:
                            L.append('eq ' + tex.replace('\n', ' '))
                        ctx['q'] = None
                    else:
                        self.para(L, obj, kind, ex_title, st, ctx)
            L += pend
            st['has_q'] = ctx.get('has_q', False) and bool(st['ex'])
            pages.append((n, L, run))
        if st['ex']:
            pages[-1][1].append('endexercise')
        out = self.dir / 'pages'
        out.mkdir(exist_ok=True)
        for f in out.glob('p*.txt'):
            f.unlink()
        for n, L, run in pages:
            fx = self.dir / 'fix' / f'p{n:03}.txt'
            (out / f'p{n:03}.txt').write_text(fx.read_text(encoding='utf-8') if fx.exists() else '\n'.join(L) + '\n', encoding='utf-8')
        self.write_units()
        (self.dir / 'meta.json').write_text(json.dumps({'total': len(pages)}), encoding='utf-8')
        print(self.key, 'pages written', len(pages))

    def titles(self, ch):
        if self.urdu_medium():
            return tri(ch.get('titleUrdu') or ch.get('title') or '', ch.get('title') or '', ch.get('titlePashto') or '')
        return tri(ch.get('title') or '', ch.get('titleUrdu') or '', ch.get('titlePashto') or '')

    def write_units(self):
        rows = []
        for ch in self.data():
            n = self.unit_no(ch)
            label = '' if isinstance(ch['number'], int) and ch['number'] != 0 else str(ch['number'])
            t = self.titles(ch).replace('{{OR}}', '||').replace('{{BAR}}', '|').split(' || ')
            t += [''] * (3 - len(t))
            rows.append(f"{n}\t{t[0]}\t{t[1]}\t{t[2]}\t\t{label}")
        (self.dir / 'units.tsv').write_text('\n'.join(rows) + '\n', encoding='utf-8')

    NUM = re.compile(r'^\s*[(（]?(\d{1,3}|[ivxlc]{1,5}|[۰-۹]{1,3})\s*[)）.۔:\-]\s*', re.I)

    def para(self, L, p, kind, ex_title, st, ctx):
        slots = self.slots(p)
        role, k = p.get('role'), p.get('kind')
        body = tri(*slots)
        if not (slots[0] or '').strip():
            return
        eq = p.get('equation') if isinstance(p.get('equation'), dict) else None
        if kind == 'ex':
            if (k in self.HEADS or p.get('role') == 'exercise-heading') and not p.get('listGroup'):
                if not st['ex']:
                    L.append('exercise ' + (clean(slots[0]).strip(' :-') or ex_title[0])); st['ex'] = True
                    return
                L.append('## ' + body); ctx['q'] = None
                return
            if not st['ex']:
                L.append('exercise ' + ex_title[0]); st['ex'] = True
            if role == 'option' and ctx['q'] is not None:
                head, _, rest = L[ctx['q']].partition(' | ')
                parts = rest.split(' || ')
                add = [clean(x) for x in slots]
                parts = [(parts[i] if i < len(parts) else '') + ' ' + (add[i] if i < len(add) else '') for i in range(max(len(parts), len(add)))]
                L[ctx['q']] = head + ' | ' + ' || '.join(x.strip() for x in parts)
                return
            if role in ('solution', 'sourceAnswer', 'source-answer'):
                if ctx.get('has_q'):
                    L.append('sol ' + clean(slots[0]) + ' ## ' + body)
                else:
                    L.append('p ' + body)
                return
            if role in ('question', 'subquestion'):
                m = self.NUM.match(slots[0])
                no = m.group(1) if m else ''
                strip = lambda t: self.NUM.sub('', t, count=1)
                text = tri(*[strip(x) for x in slots])
                ctx['has_q'] = True
                if p.get('listGroup'):
                    L.append(f'qp {no or "•"} | {text}'); ctx['q'] = len(L) - 1
                else:
                    L.append(f'q {re.sub(r"[^0-9]", "", no) or no or ""} | {text}'); ctx['q'] = len(L) - 1
                return
            L.append('p ' + body); ctx['q'] = None
            return
        # ---- lesson text
        ctx['q'] = None
        ctx['open_q'] = False
        if k in self.HEADS or role in ('box-title', 'glossary-letter', 'index-letter'):
            L.append('## ' + body)
        elif k in self.BOXES or role in ('box-body', 'lead-in'):
            L += ['box note', 'p ' + body, 'endbox']
        elif p.get('listGroup') and p.get('listType') == 'bullet':
            L.append('- ' + body)
        else:
            L.append('p ' + body)
        if eq and (eq.get('latex') or eq.get('fallback')):
            L.append('eq ' + re.sub(r'\s+', ' ', eq.get('latex') or eq.get('fallback')))

    def check(self):
        NO = re.compile(r'^\s*[(（]?(\d{1,3}|[ivxlc]{1,5}|[۰-۹]{1,3})[)）]?\s*[.۔:\-)]?\s+|^\s*[(（]?(\d{1,3}|[ivxlc]{1,5}|[۰-۹]{1,3})[)）]\s*[.۔:\-]?\s*', re.I)
        want = []
        for ch in self.data():
            for s in ch.get('sections') or []:
                for p in s.get('paras') or []:
                    o = p.get('original') if p.get('original') is not None else p.get('text')
                    want += [norm(w) for w in self.inline(o or '', p).split()]
        have = []
        for f in sorted((self.dir / 'pages').glob('p*.txt')):
            for line in f.read_text(encoding='utf-8').splitlines():
                m = re.match(r'(p|##|-|q|qp|sol) (.*)$', line)
                if not m:
                    continue
                body = m.group(2)
                if m.group(1) in ('q', 'qp') and ' | ' in body:
                    body = body.split(' | ', 1)[1]
                have += [norm(w) for w in body.split(' || ')[0].replace('{{OR}}', '||').replace('{{BAR}}', '|').split()]
        want = [w for w in want if w]
        have = [w for w in have if w]
        from collections import Counter
        lost = Counter(want) - Counter(have)
        extra = Counter(have) - Counter(want)
        miss = sum(lost.values())
        print(f'{self.key}: data words {len(want)}, page words {len(have)}, words of the data missing from the pages {miss} ({100 * miss / max(len(want), 1):.2f}%), extra {sum(extra.values())}')
        if miss:
            print('   e.g.', ' '.join(list(lost)[:12]))


def main():
    key, cmd = sys.argv[1:3]
    b = Book11(key)
    getattr(b, cmd)()


if __name__ == '__main__':
    main()
