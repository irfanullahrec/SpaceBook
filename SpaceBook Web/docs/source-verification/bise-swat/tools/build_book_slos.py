#!/usr/bin/env python
"""Learning outcomes printed in the app's own textbooks (and, where a book prints none, its section headings), for the
subjects the Board publishes no SLO list for. Input: the JSON written by extract_book_slos.js. Output: data/slos_book.json

    python -X utf8 build_book_slos.py <raw.json> [out.json]

Three sources, recorded per subject in "src":
  textbook  - "After studying this unit, students will be able to ..." / "Student Learning Outcomes" printed in the book
  headings  - the book's own section headings, as a topic checklist (the book prints no outcomes)
Nothing here is written by hand: every line is the book's own text.
"""
import html as H, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')


def txt(h):
    h = re.sub(r'<(script|style)[\s\S]*?</\1>', ' ', h)
    h = re.sub(r'<svg[\s\S]*?</svg>', ' ', h)
    h = re.sub(r'</(p|li|h\d|div|tr|details|summary)>', '\n', h)
    h = re.sub(r'<[^>]+>', ' ', h)
    return re.sub(r'[ \t]+', ' ', H.unescape(h))


def clean(t):
    return re.sub(r'\s+', ' ', t).strip()


# the verbs the Board's own curricula start an outcome with (collected from the SLO files already extracted) + a few more
def verbs():
    v = set()
    for fn in os.listdir(DATA):
        if fn.startswith('slos_') and fn.endswith('.json') and fn != 'slos_book.json':
            for c in json.load(open(os.path.join(DATA, fn), encoding='utf8'))['chapters']:
                for x in c['slos']:
                    m = re.match(r'^[•\-\s]*([A-Za-z]+)', x['t'])
                    if m:
                        v.add(m.group(1).lower())
    v |= {'state', 'define', 'describe', 'explain', 'list', 'identify', 'compare', 'distinguish', 'differentiate', 'calculate', 'derive', 'solve', 'draw',
          'outline', 'classify', 'discuss', 'illustrate', 'justify', 'predict', 'construct', 'interpret', 'perform', 'recognize', 'recognise', 'relate',
          'apply', 'use', 'analyse', 'analyze', 'evaluate', 'sketch', 'determine', 'write', 'name', 'give', 'show', 'prove', 'find', 'measure', 'convert',
          'balance', 'predict', 'account', 'appreciate', 'recall', 'summarize', 'summarise', 'differentiate', 'demonstrate', 'investigate', 'plot', 'express',
          'select', 'suggest', 'design', 'develop', 'understand', 'know', 'realize', 'realise', 'introduce', 'trace', 'examine', 'observe', 'infer', 'estimate',
          'deduce', 'verify', 'test', 'prepare', 'carry', 'make', 'compute', 'locate', 'elaborate', 'enumerate', 'review', 'rank', 'arrange', 'check', 'assess'}
    return v - NOT_VERBS


NOT_VERBS = {'unit', 'chapter', 'topic', 'section', 'the', 'a', 'an', 'in', 'of', 'for', 'to', 'and', 'at', 'on', 'with', 'from', 'by', 'what', 'how', 'why', 'which', 'when',
             'where', 'who', 'after', 'before', 'during', 'students', 'student', 'all', 'it', 'this', 'that', 'these', 'those', 'is', 'are', 'was', 'were', 'be', 'as', 'or', 'if', 'e', 'i'}
VERBS = verbs()


def first_word(s):
    m = re.match(r'^[\s•·▪\-–(]*([A-Za-z]+)', s)
    return m.group(1).lower() if m else ''


LEVEL = re.compile(r'\(\s*(Remembering|Understanding|Applying|Analy[sz]ing|Evaluating|Creating|Knowledge|Application)\s*\)\s*\.?\s*$', re.I)


def english_run(h):
    """the outcome list of one science/maths chapter: the run of verb-led sentences that follows the 'able to' heading"""
    en = [clean(H.unescape(m.group(1))) for m in re.finditer(r'data-en="([^"]*)"', h)]
    out, miss = [], 0
    for s in en:
        if not s:
            continue
        # one block: "LEARNING OUTCOMES. After studying this unit, students will be able to: describe ...; (1) ... (2) ..."
        mm = re.search(r'able to\s*:?\s*(.+)$', s, re.I)
        if mm and len(mm.group(1)) > 25 and not out:
            tail = mm.group(1)
            pieces = re.split(r'\(\d+\)\s*|;\s+', tail)
            out += [clean(p) for p in pieces if len(clean(p)) > 8]
            continue
        if re.search(r'able to|learning outcomes?', s, re.I) and len(s) < 140:
            continue
        parts = [clean(p) for p in re.split(r'(?<=[.;])\s*\(\d+\)\s*|^\(\d+\)\s*', s) if clean(p)]
        for p in parts:
            p = re.sub(r'^[•·▪\-–]\s*', '', p)
            if first_word(p) in VERBS and 6 <= len(p) <= 420:
                out.append(p); miss = 0
            else:
                if out:
                    miss += 1
        if miss >= 2 and out:
            break
    seen, res = set(), []
    for x in out:
        k = x.lower()
        if k not in seen:
            seen.add(k); res.append(x)
    return res


URDU = re.compile(r'[؀-ۿ]')
CAN = re.compile(r'(سکیں|سکتے ہیں|سکیں گے|سکے)\s*[۔\.]?$')


def urdu_run(h, cap=60):
    """Urdu-medium books: the outcome lines of a lesson. A line is 'Urdu English English-text' (the book prints each in 3 languages) or an
    Urdu sentence ending in 'کر سکیں۔'. Stops at the first line that starts a different block ('(خلاصہ ...', a very long paragraph)."""
    L = [l.strip() for l in txt(h).splitlines() if l.strip()]
    out, started = [], False
    for l in L:
        if re.search(r'Student Learning Outcomes|Learning outcomes|حاصلات|تعلیمی نتائج|اس قابل', l):
            started = True
            if not re.search(r'English|:$', l):
                continue
        if not started:
            continue
        if l.startswith('(') or l.startswith('اردو ') or l.startswith('پښتو ') or l.startswith('English '):
            if out and l.startswith('('):
                break
            continue
        if ' English ' in l:
            ur, en = l.split(' English ', 1)
            ur, en = clean(ur), clean(en)
            if not URDU.search(ur) or len(ur) < 12 or len(en) < 6 or ur.endswith(':'):
                continue
            if len(ur) > 330:
                break
            out.append({'t': ur, 'en': en})
        elif CAN.search(l) and URDU.search(l) and 15 < len(l) < 330:
            out.append({'t': clean(l), 'en': ''})
        if len(out) >= cap:
            break
    seen, res = set(), []
    for x in out:
        if x['t'] not in seen:
            seen.add(x['t']); res.append(x)
    return res


NUM = re.compile(r'^(\d+(?:\.\d+)+)\s+(.*)$')


def heading_topics(hrow):
    """the book's own section headings: numbered English headings (5.1, 5.1.2 ...) when the book has them, else the Urdu headings"""
    hs = [clean(re.sub(r'\([^)]*[؀-ۿ][^)]*\)', '', h)) for h in hrow['h']]
    num = [h for h in hs if NUM.match(h) and not re.search(r'[؀-ۿ]', h)]
    if len(num) >= 2:
        seen, out = set(), []
        for h in num:
            k = NUM.match(h).group(1)
            if k not in seen and len(NUM.match(h).group(2)) > 2:
                seen.add(k); out.append(h)
        return out
    skip = re.compile(r'^(Cover|PDF|🌐|KEY|بنیادی تصورات|متن|بابِ|باب\s|فہرست|Textbook|Topic|حاصل|ابتدائیہ|مقدمہ|ا?ختتام)')
    out, seen = [], set()
    for h in hs:
        k = re.sub(r'[\s:؛;،,\-–—]+', ' ', re.sub(r'\((?:جاری|اختتام|آغاز|cont\.?|continued)\)', '', h)).strip()
        if 4 < len(h) < 90 and not skip.search(h) and k not in seen and not re.search(r'\(\d+\)$', h) and not any(k != o and (k in o or o in k) and len(min(k, o, key=len)) > 6 for o in seen):
            seen.add(k); out.append(h)
    return out[:30]


def level_split(t):
    m = LEVEL.search(t)
    return (clean(t[:m.start()]), m.group(1).capitalize()) if m else (t, '')


def chapter_map(sid, appch):
    return {i: (c[0], c[1]) for i, c in enumerate(appch.get(sid, {}).get('ch', []))}


def main():
    raw = json.load(open(sys.argv[1], encoding='utf8'))
    out_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(DATA, 'slos_book.json')
    appch = json.load(open(os.path.join(DATA, 'app_chapters.json'), encoding='utf8'))
    result = {}
    for sid, rows in raw.items():
        if sid.endswith('#heads'):
            continue
        heads = raw.get(sid + '#heads', [])
        cm = chapter_map(sid, appch)
        chapters = {}
        # --- printed outcomes
        if sid in ('cls11-phy', 'cls12-phy', 'cls11-chem', 'cls12-chem', 'cls11-bio'):
            for r in rows:
                items = english_run(r['html'])
                if not items:
                    continue
                no, title = cm.get(r['i'], (r['i'], r['title']))
                c = chapters.setdefault(no, {'no': no, 'title': title, 'slos': []})
                for t in items:
                    t2, lv = level_split(t)
                    if t2 not in [x['t'] for x in c['slos']]:
                        c['slos'].append({'g': 'U', 't': t2, 'l': lv})
        if sid in ('cls10-urdu', 'cls9-quran', 'cls10-quran', 'cls9-islopt', 'cls10-islopt', 'cls11-urdu', 'cls12-urdu'):
            for r in rows:
                items = urdu_run(r['html'])
                if sid.endswith('islopt'):   # these books print one outcome sentence per chapter, then the lesson text
                    items = [x for x in items if x['t'].startswith('وہ ') or re.match(r'(?i)(gain|be able|acquire|develop|understand|know|learn)', x['en'])][:6]
                if not items:
                    continue
                no, title = cm.get(r['i'], (r['i'], r['title']))
                c = chapters.setdefault(no, {'no': no, 'title': title, 'slos': []})
                for x in items:
                    if x['t'] not in [y['t'] for y in c['slos']]:
                        c['slos'].append({'g': 'U', 't': x['t'], 'l': '', 'en': x['en']})
        src = 'textbook' if chapters else None
        # chapters the book prints no outcomes for: its section headings
        topics = {}
        if sid not in ('cls9-isl', 'cls10-isl') or True:
            for hr in heads:
                no, title = cm.get(hr['i'], (hr['i'], hr['title']))
                if no in chapters or str(no) in ('FM', 'BM', 'G') or str(no).startswith(('chem11-', 'FM')):
                    continue
                ts = heading_topics(hr)
                if ts:
                    topics[no] = {'no': no, 'title': title, 'slos': [{'g': 'T', 't': t, 'l': ''} for t in ts]}
        result[sid] = {'src': src, 'chapters': chapters, 'topics': topics, 'rows': len(rows)}
    json.dump(result, open(out_path, 'w', encoding='utf8'), ensure_ascii=False)
    for sid, v in result.items():
        print(sid, v['src'], {k: len(c['slos']) for k, c in v['chapters'].items()}, '| topics', {k: len(c['slos']) for k, c in v['topics'].items()})


if __name__ == '__main__':
    main()
