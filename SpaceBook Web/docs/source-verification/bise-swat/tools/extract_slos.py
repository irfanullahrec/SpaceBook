#!/usr/bin/env python
"""Extract chapters + Student Learning Outcomes (SLOs) from the BISE Swat National Curriculum PDFs.

    python -X utf8 extract_slos.py <txt-dir> <out-dir>

<txt-dir> holds `pdftotext -layout -enc UTF-8` output of the files fetched by fetch_sources.py.
Writes <out-dir>/slos_<subject>.json = {subject, source, chapters:[{no,title,periods,topics:[..],slos:[{g,t,lvl}]}]}
  g   = U understanding, K knowledge, A application, S skills / investigation skills, STS science-technology-society
  lvl = Bloom word that the curriculum prints after the outcome (Chemistry only), else ''
"""
import glob, json, os, re, sys

END = re.compile(r'^\s*(LIST OF PRACTICAL|ESTIMATED TIME|Estimated Time|ASSESSMENT OBJECTIVES|Assessment Objectives|ASSESSMENT PATTERN|TEACHING AND ASSESSMENT|Teaching and Assessment|ANNEXURE|GLOSSARY|Glossary of)')
SKIP = re.compile(r'^\s*(National Curriculum|\d+\s*$|\d+\s+National Curriculum|Page \d+)', re.I)
BULLET_CH = set('•\x83·\u2219\uf0b7\uf0a7\u25cf\u25aa\u25a0\ufffd●▪■➢➤◦')
GROUPS = [
    (re.compile(r'^(investigation\s+skills|skills)\b', re.I), 'S'),
    (re.compile(r'^(science,?\s*technology|society,?\s*technology)', re.I), 'STS'),
    (re.compile(r'^understanding\b', re.I), 'U'),
    (re.compile(r'^knowledge\b', re.I), 'K'),
    (re.compile(r'^appl(y|ying|ication)\b', re.I), 'A'),
]


def read(path):
    return open(path, encoding='utf8', errors='replace').read().replace('\x0c', '').split('\n')


def bullet(line):
    s = line.strip()
    if len(s) > 2 and s[0] in BULLET_CH and s[1] == ' ':
        return s[2:].strip()
    return None


def group_of(line):
    s = line.strip().strip('•\x83·�:').strip()
    s = re.sub(r'^[^A-Za-z]+', '', s)
    for rx, g in GROUPS:
        if rx.match(s) and len(s) < 70:
            return g
    return None


def clean(t):
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def parse_block(lines):
    """lines of one chapter -> (topics, slos). A bullet starts an SLO; following indented lines continue it."""
    slos, topics, cur, g, in_lo = [], [], None, 'U', False
    for raw in lines:
        if SKIP.match(raw):
            continue
        s = raw.strip()
        if not s:
            continue
        gg = group_of(raw)
        if gg and bullet(raw) is None:
            if cur:
                slos.append(cur); cur = None
            g = gg; in_lo = True
            continue
        if re.match(r'^(major concepts and )?learning outcomes', s, re.I) or re.match(r'^MAJOR CONCEPTS AND LEARNING', s):
            if cur:
                slos.append(cur); cur = None
            in_lo = True
            continue
        m = re.match(r'^(\d+)\s*[-–.]\s+([A-Z][^.]{2,70})$', s)  # Biology topic heading "2- Levels of Organization"
        if m and in_lo and bullet(raw) is None:
            if cur:
                slos.append(cur); cur = None
            topics.append(clean(m.group(2))); continue
        b = bullet(raw)
        if b is not None and in_lo:
            if cur:
                slos.append(cur)
            cur = {'g': g, 't': b, 'topic': len(topics)}
            continue
        if cur is not None and b is None and not raw.startswith('  '):
            slos.append(cur); cur = None; continue
        if cur is not None and b is None and not re.match(r'^(Students?|The students?)( will| should)', s):
            if re.match(r'^(Conceptual|This (unit|chapter)|Science, Tech)', s):
                slos.append(cur); cur = None; continue
            cur['t'] += ' ' + s
    if cur:
        slos.append(cur)
    for x in slos:
        x['t'] = clean(x['t'])
        m = re.search(r'\(\s*(Remembering|Understanding|Applying|Analy[sz]ing|Evaluating|Creating|Knowledge|Application)\s*\)\s*\.?$', x['t'])
        x['lvl'] = ''
        if m:
            x['lvl'] = m.group(1)
            x['t'] = clean(x['t'][:m.start()])
    return topics, slos


def split(lines, rx, start=0):
    idx = [(i, m) for i, l in enumerate(lines) if i >= start for m in [rx.match(l)] if m]
    out = []
    for k, (i, m) in enumerate(idx):
        j = idx[k + 1][0] if k + 1 < len(idx) else next((n for n in range(i + 1, len(lines)) if END.match(lines[n])), len(lines))
        out.append((m, lines[i:j]))
    return out


def physics(l):
    ch = []
    for m, blk in split(l, re.compile(r'^(?:UNIT #|Unit\s*[–-])\s*(\d+)\s+(.+?)\s*$'), 840):
        per = re.search(r'Major Concepts \((\d+)\s*periods\)', '\n'.join(blk[:12]), re.I)
        topics, slos = parse_block(blk[1:])
        ch.append({'no': int(m.group(1)), 'title': clean(m.group(2)), 'periods': int(per.group(1)) if per else None, 'topics': topics, 'slos': slos})
    return ch


def chemistry(l):
    start = next(i for i, x in enumerate(l) if 'GRADES IX-X LEARNING OUTCOMES' in x)
    ch = []
    for m, blk in split(l, re.compile(r'^Chapter\s*(\d+)\s{2,}(.+?)\s*$'), start):
        topics = []
        for x in blk[:25]:
            t = re.match(r'^\s*(\d+\.\d+)\s+(.+)$', x)
            if t:
                topics.append(clean(t.group(2)))
        _, slos = parse_block(blk[1:])
        ch.append({'no': int(m.group(1)), 'title': clean(m.group(2)), 'periods': None, 'topics': topics, 'slos': slos})
    return ch


def biology(l):
    start = next(i for i, x in enumerate(l) if re.match(r'^\s*Chapter 01\s*$', x) and i > 1000)
    ch, idx = [], [i for i, x in enumerate(l) if i >= start and re.match(r'^\s*Chapter 0?(\d+)\s*$', x)]
    for k, i in enumerate(idx):
        j = idx[k + 1] if k + 1 < len(idx) else next((n for n in range(i + 1, len(l)) if END.match(l[n])), len(l))
        blk = l[i:j]
        no = int(re.match(r'^\s*Chapter 0?(\d+)', blk[0]).group(1))
        title = next((clean(x) for x in blk[1:8] if x.strip()), '')
        per = re.search(r'(\d+)\s*Periods', '\n'.join(blk[:12]))
        topics, slos = parse_block(blk[1:])
        ch.append({'no': no, 'title': title.title(), 'periods': int(per.group(1)) if per else None, 'topics': topics, 'slos': slos})
    return ch


ROMAN = r'(?:i{1,3}|iv|vi{0,3}|ix|x{1,2})'


def computer_science(l):
    """Two-column tables: 'Contents and Scope' | 'Learning Outcomes/Skills'. Units restart at 1 in each grade."""
    out = []
    grade = None
    cur = None
    topic = None
    for raw in l:
        s = raw.strip()
        m = re.match(r'^CURRICULUM FOR COMPUTER SCIENCE\s*[–-]\s*GRADE\s*(IX|X|XI|XII)\b', s)
        if m:
            grade = m.group(1); cur = None; continue
        if grade is None:
            continue
        m = re.match(r'^UNIT\s*(\d+)\s+(.+)$', s)
        if m:
            cur = {'grade': grade, 'no': int(m.group(1)), 'title': clean(m.group(2).title()), 'periods': None, 'topics': [], 'slos': []}
            out.append(cur); topic = None
            continue
        if cur is None or SKIP.match(raw) or not s or re.match(r'^(Contents and Scope|The students will be able to)', s):
            continue
        if re.match(r'^(Assessment|Weightage|Practical|Unit-Wise|Unit Wise|Activities)', s, re.I):
            cur = None; continue
        left, right = raw[:21], raw[21:]
        tm = re.match(r'^\s*(\d+\.\d+)\s+(\S.*)$', left)
        if tm:
            topic = tm.group(1); cur['topics'].append(clean(tm.group(2)))
        elif cur['topics'] and left.strip() and not re.match(r'^\s*(i|v|x)', left):
            cur['topics'][-1] += ' ' + left.strip()
        om = re.match(r'^\s*(' + ROMAN + r')\)\s*(.*)$', right) or re.match(r'^\s*(' + ROMAN + r')\)\s*(.*)$', raw[17:])
        if om:
            cur['slos'].append({'g': 'U', 't': om.group(2).strip(), 'topic': len(cur['topics']), 'ref': topic, 'lvl': ''})
        elif cur['slos'] and right.strip():
            cur['slos'][-1]['t'] += ' ' + right.strip()
    for c in out:
        for x in c['slos']:
            x['t'] = clean(re.sub(r'\s*[•−–]\s*', '; ', x['t'])).strip('; ')
    return out


def pakstudies(l):
    out, cur = [], None
    ROM = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8}
    for raw in l:
        s = raw.strip()
        m = re.match(r'^CHAPTER\s+(I{1,3}|IV|VI{0,3})\s+([A-Z].+)$', s)
        if m and len(m.group(2)) > 5:
            cur = {'no': ROM[m.group(1)], 'title': clean(m.group(2).title()), 'periods': None, 'topics': [], 'slos': []}
            out.append(cur); continue
        if re.match(r'^(TEACHING STRATEGIES|ASSESSMENT|Assessment)', s):
            cur = None; continue
        if cur is None or not s or SKIP.match(raw) or re.match(r'^(Contents\s+Learning Outcomes|Students will be able to)', s):
            continue
        left, right = raw[:36], raw[36:]
        tm = re.match(r'^\s*(\d+)\.\s+(\S.*)$', left)
        if tm:
            cur['topics'].append(clean(tm.group(2)))
        elif cur['topics'] and left.strip() and not left.strip().startswith('•'):
            cur['topics'][-1] += ' ' + left.strip()
        bm = re.match(r'^\s*•\s*(.*)$', right) if right.strip() else None
        if bm:
            cur['slos'].append({'g': 'U', 't': bm.group(1).strip(), 'topic': len(cur['topics']), 'lvl': ''})
        elif cur['slos'] and right.strip():
            cur['slos'][-1]['t'] += ' ' + right.strip()
    for c in out:
        for x in c['slos']:
            x['t'] = clean(x['t'])
    return out


def mathematics(l):
    """Grades IX-X (30 units), XI (12) and XII (12) of the 2006 Mathematics curriculum. Two columns: sub-topic | outcomes."""
    starts = [(i, g) for i, x in enumerate(l) for g, rx in (('IX-X', r'^UNIT 1\s+MATRICES AND DETERMINANTS'), ('XI', r'^UNIT 1\s+COMPLEX NUMBERS'), ('XII', r'^UNIT 1\s+INTRODUCTION TO SYMBOLIC')) if re.match(rx, x.strip())]
    starts = [(i, g) for i, g in starts if i > 2000]
    ROM = re.compile(r'^\s*(?:i{1,3}|iv|vi{0,3}|ix|x{1,3}|xi{1,3}|xiv|xv)\)\s*')
    out = []
    for k, (i0, grade) in enumerate(starts):
        i1 = starts[k + 1][0] if k + 1 < len(starts) else len(l)
        cur, sub = None, None
        for raw in l[i0:i1]:
            s = raw.strip()
            if not s or 'National Curriculum' in raw:
                continue
            m = re.match(r'^UNIT\s*(\d+)\s+(.+)$', s)
            if m and not re.match(r'^UNIT\s*\d+\s+\d', s):
                cur = {'grade': grade, 'no': int(m.group(1)), 'title': clean(m.group(2).title()), 'periods': None, 'topics': [], 'slos': []}
                out.append(cur); sub = None
                continue
            if cur is None:
                continue
            if re.match(r'^(Assessment|ASSESSMENT|ANNEX|Annex)', s):
                cur = None; continue
            left, right = raw[:30], raw[30:]
            tm = re.match(r'^\s*(\d+\.\d+)\s+(\S.*)$', left)
            if tm:
                sub = {'ref': tm.group(1), 'title': clean(tm.group(2)), 'lines': []}
                cur['topics'].append(sub['title']); cur.setdefault('_subs', []).append(sub)
            elif sub is not None and left.strip() and not ROM.match(left):
                sub['title'] += ' ' + left.strip(); cur['topics'][-1] = sub['title']
            if sub is not None and (right.strip() or ROM.match(raw[28:])):
                sub['lines'].append((right if right.strip() else raw[28:]).strip())
        for c in out:
            pass
    for c in out:
        for sub in c.pop('_subs', []):
            txt = ' '.join(sub['lines'])
            parts = [p for p in re.split(r'(?:(?<=\s)|^)(?:i{1,3}|iv|vi{0,3}|ix|x{1,3}|xi{1,3}|xiv|xv)\)\s+', txt) if p.strip()]
            for p in (parts or [txt]):
                p = clean(re.sub(r'\s*[•]\s*', '; ', p)).strip('; ')
                if len(p) > 5:
                    c['slos'].append({'g': 'U', 't': p, 'topic': sub['ref'], 'lvl': ''})
    return out


ENGLISH_GROUPS = [  # (competency, standard, benchmark) in curriculum order -> the Board's own row names (Table 6.3, Grades IX-X)
    ('C1', 'S1', 'I', 'Patterns of text organization'), ('C1', 'S1', 'II', 'Reading comprehension strategies'), ('C1', 'S1', 'III', 'Interpretation of visual organizers'),
    ('C1', 'S1', 'IV', 'Study skills'), ('C1', 'S2', 'I', 'Interaction with literary texts'),
    ('C2', 'S1', 'I', 'Techniques for effective text organization, development and writer\'s craft'), ('C2', 'S1', 'II', 'Descriptive, narrative, expository, persuasive, analytical writing'),
    ('C2', 'S1', 'III', 'Interpersonal and transactional writing'), ('C2', 'S1', 'IV', 'Editing and revising'),
    ('C3', 'S1', 'I', 'Functions and co-functions of spoken English'), ('C3', 'S1', 'II', 'Group dynamics'),
    ('C4', 'S1', 'I', 'Pronunciation development'), ('C4', 'S2', 'I', 'Vocabulary enhancement'),
    ('C4', 'S3', 'I', 'Grammatical functions'), ('C4', 'S3', 'II', 'Mechanics of punctuation'), ('C4', 'S3', 'III', 'Sentence structure'),
    ('C5', 'S1', 'I', 'Attributes for peaceful co-existence'), ('C5', 'S1', 'II', 'Valuing self and diversity'), ('C5', 'S1', 'III', 'Approach contemporary issues as thinking individuals'),
]


def english(l, which='IX-X'):
    """The 'Student Learning Outcomes / Grade IX & X' (or XI & XII) blocks of the 2006 English curriculum, grouped by benchmark."""
    raw_starts = [i for i, x in enumerate(l) if i > 3000 and re.match(r'^\s*Competency 1: Reading and Thinking Skills', x)]
    starts = [i for k, i in enumerate(raw_starts) if k == 0 or i - raw_starts[k - 1] > 300]   # the heading is repeated at page breaks
    a = starts[0] if which == 'IX-X' else starts[1]
    b = starts[1] if which == 'IX-X' else next(i for i, x in enumerate(l) if i > a and re.match(r'^\s*Section 4: Text Types', x))
    comp = std = bm = None
    cur = None
    groups = {}
    for raw in l[a:b]:
        s = raw.strip()
        if not s or 'National Curriculum' in raw:
            continue
        m = re.match(r'^Competency (\d):', s)
        if m:
            comp = 'C' + m.group(1); continue
        m = re.match(r'^Standard (\d)', s)
        if m:
            std = 'S' + m.group(1); continue
        m = re.match(r'^Benchmark (I{1,3}|IV):', s)
        if m:
            bm = m.group(1); cur = None; continue
        if re.match(r'^(Student Learning Outcomes|Grade (IX|XI))', s):
            cur = None; continue
        if s.startswith('¾') or s.startswith('\u00be'):
            cur = {'g': 'U', 't': clean(s[1:]), 'lvl': ''}
            groups.setdefault((comp, std, bm), []).append(cur); continue
        if cur is not None:
            if s[0] in '•·':
                cur['t'] += '; ' + clean(s[1:])
            elif raw.startswith('  '):
                cur['t'] += ' ' + s
    out = []
    for n, (c, st, b_, name) in enumerate(ENGLISH_GROUPS, 1):
        sl = groups.get((c, st, b_), [])
        for x in sl:
            x['t'] = clean(x['t']).replace(';;', ';')
        out.append({'no': n, 'title': name, 'periods': None, 'topics': [], 'ref': '%s %s B%s' % (c, st, b_), 'slos': sl})
    return out


CONFIG = {
    'physics': ('Class-10th__Physics__Curriculum', physics),
    'chemistry': ('Class-10th__Chemistry__Curriculum', chemistry),
    'biology': ('Class-10th__Biology__Curriculum', biology),
    'mathematics': ('Class-10th__Mathematics__Curriculum', mathematics),
    'english': ('Class-10th__English__Curriculum', english),
    'english1112': ('Class-10th__English__Curriculum', lambda l: english(l, 'XI-XII')),
    'computer': ('Class-10th__Computer-Science__Curriculum', computer_science),
    'pakstudies': ('Class-10th__Pakistan-Studies__Curriculum', pakstudies),
}

if __name__ == '__main__':
    txt, out = sys.argv[1], sys.argv[2]
    which = sys.argv[3:] or list(CONFIG)
    for sub in which:
        key, fn = CONFIG[sub]
        p = glob.glob(os.path.join(txt, 'academics__Model-Papers-' + key + '*'))[0]
        chs = fn(read(p))
        json.dump({'subject': sub, 'source': os.path.basename(p), 'chapters': chs}, open(os.path.join(out, 'slos_%s.json' % sub), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
        print(sub, len(chs), 'chapters', sum(len(c['slos']) for c in chs), 'SLOs')
        for c in chs:
            print('  ', c['no'], c['title'][:44], c['periods'], len(c['slos']), 'topics', len(c['topics']))
