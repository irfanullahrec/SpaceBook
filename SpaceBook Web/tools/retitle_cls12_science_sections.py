"""Retitle class-12 science sections (chem/phys/stat).

The original build assigned placeholder titles ('Textbook lesson extract N')
to fixed 80-paragraph chunks. This maps each chunk to the nearest real book
heading (e.g. '13.1.1 Physical and Atomic Properties of the Elements')
found at/before the chunk start in the source DOCX, keeping content intact.
Matching is scoped to the chapter's own source range; chunks with no
confident heading keep their original title.
"""
import sys, os, re, io, json, html, shutil, zipfile, datetime
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

JS = r'D:\SpaceBook\SpaceBook Web\js'
TMP = os.path.join(os.environ['LOCALAPPDATA'], 'Temp', 'opencode', 'cls12_retitle_backup')
NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

BOOKS = [
    ('chem_12_data.js', r'D:\SpaceBook\Books\12th\12th Chemistry\Word'),
    ('phys_12_data.js', r'D:\SpaceBook\Books\12th\12th Physics\Word'),
    ('stat_12_data.js', r'D:\SpaceBook\Books\12th\12th Statistics\Word'),
]

HEAD = re.compile(r'^(\d{1,2}(?:\.\d{1,2}){1,3})\s+([A-Za-z].{1,79})$')
UNIT_MARK = re.compile(r'^(?:Unit|UNIT)\s*[-–—:.]?\s*(\d{1,2})\b')
BAD_START = re.compile(
    r'^(how|what|when|where|why|define|find|fill|write|discuss|check|suppose|'
    r'let|calculate|distinguish|out of|the length|in a certain|a pair|a coin|'
    r'if|then|prove|show|solve|convert|give|explain|perform|compute|obtain|'
    r'draw|which|express|state the|write "t"|compare|arrange|classify|label|'
    r'match|correct|answer|mention|elaborate|justify|attempt|write down|'
    r'fill in|write short|find out)', re.I)
JUNK_TAIL = re.compile(
    r'\s*(?:SALE|NOT FOR SALE|awaz\w*|Whatc\w*|\d{6,}|\d{3,})[\s.]*$', re.I)


def docx_paras(folder):
    out = []
    for f in sorted(os.listdir(folder)):
        if not f.endswith('.docx') or f.startswith('~$'):
            continue
        with zipfile.ZipFile(os.path.join(folder, f)) as z:
            tree = ET.fromstring(z.read('word/document.xml'))
            for p in tree.iter(NS + 'p'):
                t = ''.join(x.text for x in p.iter(NS + 't') if x.text).strip()
                if t:
                    out.append(t)
    return out


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def good_title(text):
    text = JUNK_TAIL.sub('', text).strip(' .-–—:')
    if not text or '?' in text or BAD_START.match(text) or not re.match(r'^[A-Za-z]', text):
        return None
    m = re.search(r'[a-z]{2,}\s(?:the|a|an|is|are|was|were|of|to|and|in|on|for|with)\s', text)
    if m and m.start() > 12:
        text = text[:m.start()].strip()
    if len(text) > 64:
        text = text[:64].rsplit(' ', 1)[0]
    return text if len(text) >= 4 else None


os.makedirs(TMP, exist_ok=True)
stamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

for jf, folder in BOOKS:
    path = os.path.join(JS, jf)
    raw = io.open(path, encoding='utf-8').read()
    i, j = raw.find('['), raw.rfind(']')
    head, tail = raw[:i], raw[j + 1:]
    arr = json.loads(raw[i:j + 1])
    psn = [norm(p) for p in docx_paras(folder)]

    # heading candidates: (src_index, unit, full_title)
    cands = []
    for i2, p in enumerate(psn):
        m = HEAD.match(p)
        if m:
            t = good_title(m.group(2))
            if t:
                cands.append((i2, int(m.group(1).split('.')[0]), m.group(1) + ' ' + t))

    # source range of each unit, derived from numbered headings (unit markers
    # are unreliable - some books list them only in back matter)
    data_units = [int(c['number']) for c in arr]
    firsts = {}
    for i2, u, _t in sorted(cands):
        firsts.setdefault(u, i2)
    unit_range = {}
    last_lo = 0
    for k, u in enumerate(data_units):
        hi = len(psn)
        for v in data_units[k + 1:]:
            if v in firsts:
                hi = firsts[v]
                break
        lo = firsts.get(u, last_lo)
        last_lo = lo
        unit_range[u] = (lo, hi)

    def find_anchor(anchor, lo, hi):
        """First occurrence of anchor inside [lo, hi), else None."""
        if not anchor:
            return None
        for i3 in range(lo, min(hi, len(psn))):
            if psn[i3] == anchor:
                return i3
        for i3 in range(lo, min(hi, len(psn))):
            if len(anchor) > 60 and psn[i3].startswith(anchor[:60]):
                return i3
        return None

    stats = {'titled': 0, 'kept': 0, 'nomatch': 0}
    for c in arr:
        unit = int(c['number'])
        lo, hi = unit_range.get(unit, (0, len(psn)))
        uc = [x for x in cands if x[1] == unit and lo <= x[0] < hi]
        prev_idx = None
        for si, s in enumerate(c.get('sections') or []):
            if si == 0:
                stats['kept'] += 1
                continue
            lines = [norm(html.unescape(x)) for x in (s.get('theory') or '').split('\n')]
            anchor = next((x for x in lines[:15] if len(x) >= 45),
                          max((x for x in lines if len(x) >= 45), key=len, default=''))
            idx = find_anchor(anchor, lo, hi)
            if idx is None and prev_idx is not None:
                idx = min(prev_idx + 80, hi - 1)        # sequential 80-para chunks
            if idx is None:
                stats['nomatch'] += 1
                continue
            prev_idx = idx
            before = [x for x in uc if 0 <= idx - x[0] <= 120]
            if before:
                s['title'] = max(before, key=lambda x: x[0])[2]
                stats['titled'] += 1
                continue
            after = [x for x in uc if -25 <= idx - x[0] < 0]
            if after:
                s['title'] = min(after, key=lambda x: x[0])[2]
                stats['titled'] += 1
            else:
                stats['kept'] += 1

    out = head + json.dumps(arr, ensure_ascii=False, indent=2) + tail
    chk = os.path.join(TMP, '_check.js')
    io.open(chk, 'w', encoding='utf-8').write(out)
    if os.system('node --check "%s"' % chk) != 0:
        print(f'{jf}: NODE CHECK FAILED - skipped')
        continue
    shutil.copy2(path, os.path.join(TMP, f'{stamp}_{jf}'))
    io.open(path, 'w', encoding='utf-8', newline='\n').write(out)
    ph_secs = sum(1 for c in arr for s in (c.get('sections') or [])
                  if (s.get('title') or '').startswith('Textbook lesson extract'))
    uniq = len({s.get('title', '') for c in arr for s in (c.get('sections') or [])})
    print(f'{jf}: titled {stats["titled"]}, kept {stats["kept"]}, no-src-match {stats["nomatch"]}'
          f' | unique titles {uniq} | sections still placeholder: {ph_secs}')
