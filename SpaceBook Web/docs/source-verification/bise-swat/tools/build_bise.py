#!/usr/bin/env python
"""Assemble js/bise_swat_data.js (window.SB_BISE) for the BISE Swat alignment.

    python -X utf8 build_bise.py <bise-page.html> [out.js]

Inputs (all in ../data/):
  slos_*.json        chapters + Student Learning Outcomes   (extract_slos.py, from the National Curriculum PDFs)
  tos_tables.json    chapter weightage and item counts       (transcribed from the Board's Table of Specification pages)
  patterns.json      paper pattern per subject               (transcribed from the Board's model papers)
  app_chapters.json  the chapters the app shows              (dump_app_chapters.js)
and the page html of https://www.bisess.edu.pk/site/home/syllabus-model-papers (labels + links of the Board's files).

Nothing from a Board question paper is copied: only the Board's file links, its published pattern/weightage numbers
and the learning outcomes of its curriculum. Every number is cross-checked against the Board's own totals below.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')
OUT_DEFAULT = os.path.join(HERE, '..', '..', '..', '..', 'js', 'bise_swat_data.js')


def load(name):
    return json.load(open(os.path.join(DATA, name), encoding='utf8'))


PANE_CLASS = ['cls9', 'cls10', 'cls11', 'cls12']
BOARD_EXAM = {'cls9': 'SSC Part-I', 'cls10': 'SSC Part-II', 'cls11': 'HSSC Part-I', 'cls12': 'HSSC Part-II'}
FOLDER = {  # Board heading -> (suffix of the app's subject id, display name, Urdu name)
    'Biology': ('bio', 'Biology', 'حیاتیات'), 'Chemistry': ('chem', 'Chemistry', 'کیمیا'), 'Physics': ('phy', 'Physics', 'طبیعیات'),
    'Computer Science': ('comp', 'Computer Science', 'کمپیوٹر سائنس'), 'Elective Mathematics': ('math', 'Mathematics (Elective)', 'ریاضی'),
    'Mathematics': ('math', 'Mathematics', 'ریاضی'), 'General Mathematics': ('gm', 'General Mathematics', 'عمومی ریاضی'),
    'English': ('eng', 'English', 'انگریزی'), 'Urdu': ('urdu', 'Urdu', 'اردو'), 'Islamiat Elective': ('islopt', 'Islamiat (Elective)', 'اسلامیات اختیاری'),
    'Islamiat Compulsory': ('isl', 'Islamiat (Compulsory)', 'اسلامیات لازمی'), 'Islamiat': ('isl', 'Islamiat (Compulsory)', 'اسلامیات لازمی'),
    'Mutala-e-Quran Hakeem': ('quran', 'Mutalia-e-Quran', 'مطالعۂ قرآن حکیم'), 'Pak-Study': ('pakstudy', 'Pakistan Studies', 'مطالعۂ پاکستان'),
    'Pakistan Studies': ('pakstudy', 'Pakistan Studies', 'مطالعۂ پاکستان'),
}
# the Board's file lists the app has no subject for are still kept ("Board subject not in the app yet")
APP_ID_FIX = {('cls11', 'comp'): 'cls11-cs', ('cls12', 'pakstudy'): 'cls12-pak'}

# Annual-II 2025 printed papers on the Board's "E-Marking (Model Papers)" page (Google Drive images)
DRIVE = {
    ('cls9', 'eng'): '1DtV5weq5m1ISmacS9jpKuznjWSZQDTXL', ('cls9', 'chem'): '1EyMCH_ComtOqy5oZxBFd7F-49dafrtYK', ('cls9', 'phy'): '1uUJ7tyPXljnJpGIMYY5TVpkCsRQs2_gz',
    ('cls10', 'eng'): '1y1pYl4N1HsFB-f5Dv14ybgAGE_peZ7A9', ('cls10', 'chem'): '1GGMSA-JROj8iMUX79MfbKJFJjdISulzf', ('cls10', 'phy'): '1952f80kfIFc6oOkcPuJQ95AxK2CfL_MS',
    ('cls11', 'eng'): '1SiXtl3ixIwoV0z8Q4IaiADg75Xz6cJGD', ('cls11', 'chem'): '1qsiAWEexm4WQGP1hge8DadVfR01lq8DZ', ('cls11', 'phy'): '13XulvcqsD6GYWRUzZSxZwyLd3-mtL2mD',
    ('cls12', 'eng'): '1vxashrqZYrF4_1f154n5KrHeb8T_ZHhG', ('cls12', 'chem'): '1BS4m6KuOydw32nP4GKyzvx_eGX0-JX6c', ('cls12', 'phy'): '1Qnqy2-IKj7TOcY_GAc1vn-o8hRLJb2Y7',
}

# which curriculum chapters belong to which app subject
SLO_SOURCE = {  # app id -> (slos file, filter fn(chapter) , first board number used by the app (for numbering), board numbers)
    'cls9-phy': ('slos_physics.json', lambda c: 1 <= c['no'] <= 9), 'cls10-phy': ('slos_physics.json', lambda c: 10 <= c['no'] <= 18),
    'cls9-chem': ('slos_chemistry.json', lambda c: 1 <= c['no'] <= 8), 'cls10-chem': ('slos_chemistry.json', lambda c: 9 <= c['no'] <= 16),
    'cls9-bio': ('slos_biology.json', lambda c: 1 <= c['no'] <= 9), 'cls10-bio': ('slos_biology.json', lambda c: 10 <= c['no'] <= 18),
    'cls9-comp': ('slos_computer.json', lambda c: c.get('grade') == 'IX'), 'cls10-comp': ('slos_computer.json', lambda c: c.get('grade') == 'X'),
    'cls11-cs': ('slos_computer.json', lambda c: c.get('grade') == 'XI'), 'cls12-comp': ('slos_computer.json', lambda c: c.get('grade') == 'XII'),
    'cls9-pakstudy': ('slos_pakstudies.json', lambda c: 1 <= c['no'] <= 4), 'cls10-pakstudy': ('slos_pakstudies.json', lambda c: 5 <= c['no'] <= 8),
}
# Mathematics: the curriculum numbers the IX-X units 1-30; the Board's tables (and the textbooks) split them over two years
MATH9 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 14: 8, 15: 9, 17: 10, 18: 11, 19: 12, 20: 13, 21: 14, 22: 15, 23: 16, 29: 17}
MATH10 = {8: 1, 9: 2, 10: 3, 11: 4, 12: 5, 13: 6, 16: 7, 24: 8, 25: 9, 26: 10, 27: 11, 28: 12, 30: 13}
SLO_REMAP = {'cls9-math': MATH9, 'cls10-math': MATH10}
SLO_SOURCE.update({
    'cls9-math': ('slos_mathematics.json', lambda c: c.get('grade') == 'IX-X' and c['no'] in MATH9),
    'cls10-math': ('slos_mathematics.json', lambda c: c.get('grade') == 'IX-X' and c['no'] in MATH10),
    'cls11-math': ('slos_mathematics.json', lambda c: c.get('grade') == 'XI'),
    'cls12-math': ('slos_mathematics.json', lambda c: c.get('grade') == 'XII'),
    'cls9-eng': ('slos_english.json', lambda c: bool(c['slos'])), 'cls10-eng': ('slos_english.json', lambda c: bool(c['slos'])),
    'cls11-eng': ('slos_english1112.json', lambda c: bool(c['slos'])), 'cls12-eng': ('slos_english1112.json', lambda c: bool(c['slos'])),
})
# English: the curriculum's own weighting of its skill groups (Table 6.3, Grades IX-X): group -> (paper, % of that paper)
ENGLISH_W = {1: ('A', 15), 2: ('A', 30), 3: ('A', 15), 5: ('A', 25), 13: ('A', 15), 6: ('B', 15), 7: ('B', 20), 8: ('B', 20), 14: ('B', 25), 15: ('B', 10), 16: ('B', 10)}
# Board chapter number -> the app's chapter number, where they differ
APP_NO = {'cls10-pakstudy': {5: 1, 6: 2, 7: 3, 8: 4}}
# subjects whose app book is a different book from the one the Board examines (listed in the coverage report)
BOOK_MISMATCH = {'cls9-comp': 'The Board examines Class 9 Computer Science on Fundamentals of Computer, Operating System, Office Automation, Data Communication, Networks and Security. The app\'s Class 9 Computer Science book is the Programming (C) book that the Board examines in Class 10.'}

KIND = [(re.compile(r'model paper', re.I), 'model'), (re.compile(r'marking|rubric|answer key|scoring', re.I), 'marking'),
        (re.compile(r'table of spec|tos|assessment framework|slo', re.I), 'tos'), (re.compile(r'curriculum', re.I), 'curriculum'),
        (re.compile(r'summary', re.I), 'summary')]


def kind_of(label, url):
    s = label + ' ' + url
    if re.search(r'curriculum', s, re.I):
        return 'curriculum'
    if re.search(r'marking|rubric|answer.?key|scoring|solution', s, re.I):
        return 'marking'
    if re.search(r'table.of.spec|tos|assessment.framework|slos|summary', s, re.I):
        return 'tos'
    if re.search(r'model|modal|ماڈل|mp\b', s, re.I):
        return 'model'
    return 'other'


def parse_page(html):
    """-> {(cls, suffix): {'heading': str, 'files': [{k, label, url}]}}"""
    panes = re.split(r'<div class="tab-pane', html)[1:5]
    out = {}
    for ci, pane in enumerate(panes):
        cls = PANE_CLASS[ci]
        for heading, body in re.findall(r'<li>\s*([^<]+?)\s*<ul>(.*?)</ul>', pane, flags=re.S):
            heading = re.sub(r'\s+', ' ', heading).strip()
            if heading not in FOLDER:
                print('  ! unknown Board heading', cls, heading); continue
            files = []
            for url, label in re.findall(r'<a href="([^"]+)">\s*([^<]+?)\s*</a>', body, flags=re.S):
                label = re.sub(r'\s+', ' ', label).strip()
                files.append({'k': kind_of(label, url), 'label': label, 'url': url.replace(' ', '%20')})
            out[(cls, FOLDER[heading][0])] = {'heading': heading, 'files': files}
    return out


def cap(t, n=420):
    return t if len(t) <= n else t[:n].rsplit(' ', 1)[0].rstrip(';:,') + ' …'


def tidy(t):
    return re.sub(r'\s+', ' ', t).strip()


def main():
    page = open(sys.argv[1], encoding='utf8').read()
    out_path = sys.argv[2] if len(sys.argv) > 2 else OUT_DEFAULT
    tos = load('tos_tables.json')
    patterns = load('patterns.json')
    appch = load('app_chapters.json')
    slofiles = {}
    files = parse_page(page)
    status = {}
    if os.path.exists(os.path.join(DATA, 'link_status.json')):
        status = load('link_status.json')    # tools/check_links.py
    for v in files.values():
        for f in v['files']:
            c = status.get(f['url'])
            if c is not None and c not in (200, 206):
                f['bad'] = c         # the Board's own link does not work (the app lists it as unavailable)
    subjects, report = {}, []

    keys = set()
    for (cls, suf), v in files.items():
        keys.add(APP_ID_FIX.get((cls, suf), f'{cls}-{suf}'))
    keys |= set(SLO_SOURCE) | set(tos['tables'])
    for sid in sorted(keys, key=lambda s: (int(re.match(r'cls(\d+)', s).group(1)), s)):
        cls, suf = sid.split('-', 1)
        suf_board = {'cs': 'comp', 'pak': 'pakstudy'}.get(suf, suf)
        name = next((FOLDER[h][1] for h in FOLDER if FOLDER[h][0] == suf_board), suf)
        name_ur = next((FOLDER[h][2] for h in FOLDER if FOLDER[h][0] == suf_board), '')
        if suf_board == 'math':
            name = 'Mathematics (Elective)' if cls == 'cls9' else 'Mathematics'
        app = appch.get(sid)
        f = files.get((cls, suf_board), {'files': []})['files']
        d = {'id': sid, 'cls': int(cls[3:]), 'exam': BOARD_EXAM[cls], 'name': name, 'nameUr': name_ur, 'inApp': bool(app),
             'files': f}
        if app and app.get('key'):
            d['key'] = app['key']          # the app's own subject key (phys, chem, comp...): the chapter strip finds the subject by class + key
        if (cls, suf_board) in DRIVE:
            d['past'] = [{'label': 'Annual-II 2025 printed paper (Board image)', 'url': 'https://drive.google.com/file/d/%s/view' % DRIVE[(cls, suf_board)]}]
        if sid in patterns:
            d['pattern'] = patterns[sid]
        # ---- chapters ---------------------------------------------------------------------------------------
        chs = {}
        if sid in SLO_SOURCE:
            fn, flt = SLO_SOURCE[sid]
            if fn not in slofiles:
                slofiles[fn] = load(fn)
            rm = SLO_REMAP.get(sid)
            for c in slofiles[fn]['chapters']:
                if flt(c):
                    no = rm[c['no']] if rm else c['no']
                    chs[no] = {'no': no, 'bt': c['title'], 'periods': c.get('periods'), 'topics': c.get('topics', []),
                                    'slos': [{'g': x['g'], 't': cap(x['t']), 'l': x.get('lvl', '')} for x in c['slos'] if len(x['t'].strip()) >= 3]}
        rows = tos['tables'].get(sid, [])
        titles = tos.get('titles', {}).get(sid, {})
        for r in rows:
            c = chs.setdefault(r['ch'], {'no': r['ch'], 'bt': titles.get(str(r['ch']), ''), 'periods': None, 'topics': [], 'slos': []})
            for k in ('w', 'm', 'r', 'e', 'ep'):
                if k in r:
                    c[k] = r[k]
            if not c.get('bt'):
                c['bt'] = titles.get(str(r['ch']), '')
        appnum = APP_NO.get(sid, {})
        applist = {str(n): t for n, t in (app['ch'] if app else [])}
        if app and not app['ch'] and app.get('n'):   # the Maths workspaces do not go through getSubjectChapterList: chapter n = unit n
            applist = {str(i): '' for i in range(1, int(app['n']) + 1)}
        out_ch = []
        for no in sorted(chs):
            c = chs[no]
            an = appnum.get(no, no)
            if sid in BOOK_MISMATCH:
                an = None
            title = c['bt']
            c2 = {'no': no}
            if suf_board == 'eng':      # skill groups of the curriculum, not textbook lessons
                c2['sk'] = 1
                if no in ENGLISH_W and cls in ('cls9', 'cls10'):
                    c2['pp'], c2['w'] = ENGLISH_W[no]
            if an is not None and str(an) in applist and not c2.get('sk'):
                c2['app'] = an
            c2['t'] = title or applist.get(str(an), '') or ('Unit %s' % no)
            for k in ('w', 'm', 'r', 'e', 'ep', 'periods'):
                if c.get(k) is not None:
                    c2[k] = c[k]
            if c['topics']:
                c2['topics'] = [tidy(t) for t in c['topics'] if tidy(t)][:12]
            if c['slos']:
                c2['slos'] = c['slos']
            out_ch.append(c2)
        if out_ch:
            d['chapters'] = out_ch
        if rows:
            sm = {'m': sum(x['m'] or 0 for x in rows), 'r': sum(x['r'] or 0 for x in rows), 'e': sum(x['e'] or 0 for x in rows)}
            d['tosTotals'] = sm
        if tos.get('sections', {}).get(sid):
            d['sections'] = tos['sections'][sid]
        if sid in BOOK_MISMATCH:
            d['mismatch'] = BOOK_MISMATCH[sid]
        if tos.get('meta', {}).get(sid):
            d['note'] = tos['meta'][sid]['note']
        subjects[sid] = d
        nslo = sum(len(c.get('slos', [])) for c in out_ch)
        miss = [c['no'] for c in out_ch if 'app' not in c]
        report.append('%-14s %-26s chapters=%-3d SLOs=%-4d files=%-2d pattern=%s notInApp=%s' % (sid, name, len(out_ch), nslo, len(f), 'yes' if sid in patterns else 'no', miss if miss else '-'))

    board = {'name': 'Board of Intermediate & Secondary Education, Saidu Sharif, Swat', 'site': 'https://www.bisess.edu.pk/site/',
             'pages': {'syllabus': 'https://www.bisess.edu.pk/site/home/syllabus-model-papers', 'emarking': 'https://www.bisess.edu.pk/site/home/emarking-model-papers/',
                       'osm': 'https://www.bisess.edu.pk/site/home/teacher-profile-form',
                       'eanswer': 'https://www.bisess.edu.pk/site/assets/attachments/6dee164ef85c0f9b5098b845825b9eec.pdf',
                       'scheme': 'https://www.bisess.edu.pk/site/assets/academics/Scheme_of_Studies_2019.pdf'}, 'fetched': '2026-10-20'}
    data = {'v': 1, 'board': board, 'subjects': subjects}
    js = '/* GENERATED by docs/source-verification/bise-swat/tools/build_bise.py - do not edit by hand. */\nwindow.SB_BISE = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';\n'
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    open(out_path, 'w', encoding='utf8').write(js)
    print('\n'.join(report))
    print('wrote', out_path, len(js), 'bytes,', len(subjects), 'subjects')


if __name__ == '__main__':
    main()
