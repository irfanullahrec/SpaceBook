"""Cleanup pass for class-12 subject data files.

Drops/merges chapter-final OCR junk sections (<150 chars) identified by the
content verification audit:
  - science sections (chem/phys/stat) under 100 chars are dropped (diagram OCR)
  - humanities sections: watermark/OCR tokens stripped; if real text remains
    it is appended to the previous section (paras/text/urdu), else dropped
Content of all other sections is untouched.
"""
import sys, os, re, io, json, shutil, datetime

sys.stdout.reconfigure(encoding='utf-8')

JS = r'D:\SpaceBook\SpaceBook Web\js'
TMP = os.path.join(os.environ['LOCALAPPDATA'], 'Temp', 'opencode', 'cls12_junk_backup')

FILES = [
    'chem_12_data.js', 'phys_12_data.js', 'stat_12_data.js', 'urdu_12_data.js',
    'english_12_data.js', 'civics_12_data.js', 'computer_12_data.js',
    'economics_12_data.js', 'hpe_12_data.js', 'islamiat_ikhtiari_12_data.js',
    'islamic_history_12_data.js', 'pakstudy_12_data.js', 'quran_12_data.js',
]

JUNK = [
    r'awaz\s*e?\s*in[i]?lab(\.com)?', r'awazeinqilab\.com', r'awazeing\w*',
    r'awaze\s*inailab\.com', r'awaz\s*e\s*inqilab\.com', r'awaz\s*eg\w*',
    r'\bilab\.com\w*', r'\bb\.com\b', r'\bWhatc\w*', r'\bWhate\w*',
    r'\bWhat\w*', r'camscanner', r'NOT\s*[-–]?\s*FOR\s*[-–]?\s*S\w*',
    r'Free\s+From\s+Government', r'Nosheen\s+Ali', r'Whatsapp:?\s*[\d\s\-]+',
    r'\bPSP/[\w\-()]+', r'\b\d{6,}\b', r'\b\d{7,}\b', r'\b2005\d{4,}\b',
    r'\bTOA\b', r'\bSA-\d+-A\d+\)?', r'\bLES\b', r'\bSANLE\b', r'\bTEAL\b',
    r'\bmbc\d+\b', r'\biew\b', r'\bNed\b', r'\bWhate\w*', r'\bWhatcan\w*',
    r'\bF\s+wa\w+', r'\bTOC\b', r'\bVpun\b', r'\bUbject\b', r'\b2025347270\b',
    r'\b2035347270\b', r'\b091-\d[\d\-]+\b', r'\b\d{5}-\d+\b',
    r'\bawaz\s*e\s*inqilab\b', r'\.com\b', r'\bWhatcanni\b', r'\bWhatconn\b',
    r'\bWhatcan\b', r'\bWhateONAL\b', r'\bWhateann\w*', r'\bwhatcan\w*',
    r'\bNOT\s*FOR\s*SAL\b', r'\bNOT\s*FOR\s*SANLE\b', r'\bNOT\s*FOR-SALE\b',
    r'\bNOT\s*FOR\s*SALE\b', r'\bdownload\w*\b', r'\bawaze\b', r'\bawazeing\b',
    r'awaz\s*e?\s*i\w*lab\w*', r'\bin\w*lab\b', r'\bb\.cont\w*',
    r'(?:\s*ها)+', r'باب\s*نمبر', r'\bawaz\s*e\b', r'\bin\b(?=\s*$)',
]
JUNK_RE = re.compile('|'.join(f'(?:{p})' for p in JUNK), re.I)
ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F]')
WS = re.compile(r'[ \t]+')


def clean(text):
    t = JUNK_RE.sub(' ', text)
    t = re.sub(r'\d{1,3}(?:,\d{3})+', ' ', t)                      # 30,781
    t = re.sub(r'(?<!\d)\d{3,}(?![\u0600-\u06FF0-9])', ' ', t)      # page codes (keep years like 1979ء)
    t = re.sub(r'[{}()\[\];:<>|]+', ' ', t)
    t = WS.sub(' ', t)
    t = re.sub(r'\s*\n\s*', ' \n ', t).strip(' -–—.,·')
    return t


def sec_len(sec):
    if 'theory' in sec or 'content' in sec:
        return len(sec.get('theory') or '') + len(sec.get('content') or '')
    return len('\n\n'.join(sec.get('paras') or []))


def is_science(sec):
    return 'theory' in sec or 'content' in sec


def merge_into(prev, extra):
    if is_science(prev):
        prev['theory'] = ((prev.get('theory') or '') + '\n' + extra).strip()
        prev['content'] = ((prev.get('content') or '') + '<br>' + extra).strip()
    else:
        paras = list(prev.get('paras') or [])
        paras.append(extra)
        prev['paras'] = paras
        prev['text'] = ((prev.get('text') or '') + '\n\n' + extra).strip()
        if prev.get('urdu'):
            prev['urdu'] = ((prev.get('urdu') or '') + '\n\n' + extra).strip()


def process(arr):
    dropped, merged = [], []
    for c in arr:
        secs = c.get('sections')
        if not secs:
            continue
        keep = []
        for i, s in enumerate(secs):
            n = sec_len(s)
            if n >= 150:
                keep.append(s)
                continue
            if is_science(s):
                dropped.append((c.get('number'), s.get('title'), n, 'sci-junk'))
                continue
            raw = '\n\n'.join(s.get('paras') or [])
            cl = clean(raw)
            has_real = len(ARABIC.findall(cl)) >= 3 or bool(re.search(r'[A-Za-z]{4,}', cl))
            if has_real and keep:
                merge_into(keep[-1], cl)
                merged.append((c.get('number'), (s.get('heading') or '')[:40], n, cl[:50]))
            elif has_real:
                keep.append(s)          # first section: keep as-is
            else:
                dropped.append((c.get('number'), (s.get('heading') or '')[:40], n, 'pure-junk'))
        c['sections'] = keep
        if 'topics' in c and c.get('topics') is secs:
            c['topics'] = keep
    return dropped, merged


os.makedirs(TMP, exist_ok=True)
stamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
for f in FILES:
    path = os.path.join(JS, f)
    raw = io.open(path, encoding='utf-8').read()
    i, j = raw.find('['), raw.rfind(']')
    head, tail = raw[:i], raw[j + 1:]
    arr = json.loads(raw[i:j + 1])
    before = sum(len(c.get('sections') or []) for c in arr)
    dropped, merged = process(arr)
    after = sum(len(c.get('sections') or []) for c in arr)
    out = head + json.dumps(arr, ensure_ascii=False, indent=2) + tail
    # syntax check before writing
    io.open(os.path.join(TMP, '_check.js'), 'w', encoding='utf-8').write(out)
    rc = os.system('node --check "%s"' % os.path.join(TMP, '_check.js'))
    if rc != 0:
        print(f'{f}: NODE CHECK FAILED - not written')
        continue
    shutil.copy2(path, os.path.join(TMP, f'{stamp}_{f}'))
    io.open(path, 'w', encoding='utf-8', newline='\n').write(out)
    print(f'{f}: sections {before} -> {after} (dropped {len(dropped)}, merged {len(merged)})')
    for d in dropped:
        print(f'    DROP ch{d[0]} {d[1]!r} len={d[2]} [{d[3]}]')
    for m in merged:
        print(f'    MERGE ch{m[0]} {m[1]!r} len={m[2]} -> {m[3]!r}')
