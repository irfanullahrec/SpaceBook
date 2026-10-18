"""Repair OCR-junk section titles in class-12 humanities/CS subjects.

Titles follow '<حصہ/Section N>: <text>'. When <text> is OCR garbage
(watermarks, page codes, lone characters, code fragments), it is replaced
with a cleaned lead phrase from the section's own content, keeping the
'<حصہ/Section N>:' prefix. headingUrdu mirrors the title, so it is updated
when it matched the old title.
"""
import sys, os, re, io, json, shutil, datetime

sys.stdout.reconfigure(encoding='utf-8')

JS = r'D:\SpaceBook\SpaceBook Web\js'
TMP = os.path.join(os.environ['LOCALAPPDATA'], 'Temp', 'opencode', 'cls12_title_backup')

FILES = ['urdu_12_data.js', 'civics_12_data.js', 'computer_12_data.js',
         'economics_12_data.js', 'hpe_12_data.js', 'islamiat_ikhtiari_12_data.js',
         'islamic_history_12_data.js', 'pakstudy_12_data.js', 'quran_12_data.js']

PREFIX = re.compile(r'^(حصہ\s*\d+\s*:|Section\s*\d+\s*:)\s*')
ARABIC = re.compile(r'[\u0600-\u06FF]')
WATERMARK = re.compile(
    r'awaz\S*|inqilab\S*|Whatc\w*|Whate\w*|NOT\s*FOR\s*S\w*|camscanner|'
    r'\bcom?\b|\bview\b|\d{6,}|\b\w*ing\s*\.\s*com\b', re.I)


def junky(text):
    """True when the title body conveys no usable label."""
    t = WATERMARK.sub(' ', text).strip()
    t = re.sub(r'[{}\[\]()/=,+;:*\'"<>|\\`~#@!?\d\s\.\-–—_,]+', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    if len(ARABIC.findall(t)) >= 3:
        return False
    words = [w for w in t.split() if len(w) >= 3 and w.isascii()]
    if len(words) >= 2:
        return False
    if re.search(r'[\u4e00-\u9fff]', text):        # stray CJK glyphs
        return True
    return True


def lead_phrase(sec):
    paras = sec.get('paras') or []
    for p in paras[:6]:
        line = re.sub(r'\s+', ' ', p).strip()
        line = WATERMARK.sub(' ', line)
        if len(ARABIC.findall(line)) < 3 and not re.search(r'[A-Za-z]{4,}\s+[A-Za-z]{4,}', line):
            continue
        words = line.split()
        out = []
        for w in words[:9]:
            out.append(w)
            if len(' '.join(out)) >= 34:
                break
        phrase = ' '.join(out).strip(' -–—.,؛:')
        if len(phrase) >= 6:
            return phrase[:48].rstrip() if len(phrase) <= 48 else phrase[:48].rsplit(' ', 1)[0]
    return ''


os.makedirs(TMP, exist_ok=True)
stamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

for f in FILES:
    path = os.path.join(JS, f)
    raw = io.open(path, encoding='utf-8').read()
    i, j = raw.find('['), raw.rfind(']')
    head, tail = raw[:i], raw[j + 1:]
    arr = json.loads(raw[i:j + 1])
    fixed, unfixed = [], []
    for c in arr:
        for si, s in enumerate(c.get('sections') or []):
            title = s.get('heading') or ''
            m = PREFIX.match(title)
            prefix = (m.group(1) + ' ') if m else ''
            body = title[m.end():] if m else title
            if not junky(body):
                continue
            lead = lead_phrase(s)
            new_title = (prefix + lead) if lead else (prefix.rstrip(': ') or title)
            if new_title == title:
                unfixed.append(title)
                continue
            fixed.append((title, new_title))
            s['heading'] = new_title
            if s.get('headingUrdu') == title:
                s['headingUrdu'] = new_title
    if fixed or unfixed:
        out = head + json.dumps(arr, ensure_ascii=False, indent=2) + tail
        chk = os.path.join(TMP, '_check.js')
        with io.open(chk, 'w', encoding='utf-8') as fh:
            fh.write(out)
        if os.system('node --check "%s"' % chk) != 0:
            print(f'{f}: NODE CHECK FAILED - skipped')
            continue
        shutil.copy2(path, os.path.join(TMP, f'{stamp}_{f}'))
        tmp_path = path + '.tmp'
        with io.open(tmp_path, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(out)
        os.replace(tmp_path, path)
    print(f'{f}: repaired {len(fixed)}, unrepairable {len(unfixed)}')
    for old, new in fixed:
        print(f'    {old[:58]!r} -> {new[:58]!r}')
    for u in unfixed:
        print(f'    (kept junk) {u[:58]!r}')
