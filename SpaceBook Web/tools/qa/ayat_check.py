"""Qur'an text of the Class 11/12 data files checked against the complete Uthmani text of the project cache (D:/SpaceBook/_qcache).

    python tools/qa/ayat_check.py <js data file> [--show N] [--json out.json]

1. every Arabic-script string of the data file that carries vowel marks (>= 4) and is >= 12 letters long is a candidate;
2. its consonant skeleton (marks removed, letter variants merged) is searched in the skeleton of every surah; a candidate that matches a run
   of consecutive ayat exactly is "identified", one that matches with 1-3 letter differences is reported as a SPELLING difference
   (a wrong, missing or added letter / word), the rest is ignored (Urdu prose, hadith, poetry);
3. for an identified text the vowel marks are compared letter by letter with the Uthmani text, after merging the notation differences between
   scripts (small alif / dagger alif, madd and the Uthmani pause and recitation signs are ignored); every remaining difference of fatha, damma,
   kasra, tanween, shadda or sukun on a letter is reported as a DIACRITIC difference (the textbook may use another orthography on purpose, so
   each one is read against the scan).
"""
import sys, os, re, json, unicodedata

CACHE = 'D:/SpaceBook/_qcache'
MARKS = re.compile('[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u08D3-\u08FF\uFE70-\uFE7F\u200c\u200d\ufeff\u0640]')
HARAKAT = '\u064E\u064F\u0650\u064B\u064C\u064D\u0651\u0652'      # fatha damma kasra fathatan dammatan kasratan shadda sukun
LETTER_MAP = {'ٱ': 'ا', 'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٲ': 'ا', 'ى': 'ي', 'ی': 'ي', 'ې': 'ي', 'ے': 'ي', 'ئ': 'ي', 'ک': 'ك', 'ہ': 'ه', 'ھ': 'ه', 'ۃ': 'ه', 'ة': 'ه', 'ؤ': 'و', 'ء': '', 'ٰ': '', 'ۀ': 'ه', 'ں': 'ن', 'ٹ': 'ت', 'ڈ': 'د', 'ڑ': 'ر', 'گ': 'ك', 'ۓ': 'ي', 'ٖ': ''}


def skel(s):
    s = unicodedata.normalize('NFC', s)
    s = MARKS.sub('', s)
    out = []
    for c in s:
        c = LETTER_MAP.get(c, c)
        if '\u0621' <= c <= '\u064A' or c in 'پچژ':
            out.append(c)
    return ''.join(out)


def skel_na(s):
    return skel(s).replace('ا', '')


def letters_with_marks(s):
    """[(skeleton letter, frozenset of harakat)] ; one entry per base letter"""
    s = unicodedata.normalize('NFC', s)
    res = []
    for c in s:
        if MARKS.sub('', c) == '' and c != '\u0640':
            if c in HARAKAT and res: res[-1][1].add(c)
            elif c == '\u0670' and res: pass
            continue
        m = LETTER_MAP.get(c, c)
        if m and ('\u0621' <= m <= '\u064A'): res.append([m, set()])
    # normalise tanween notation: fathatan etc. count as their own mark; Uthmani adds an extra alef after fathatan (ًا) -> skeleton handles it
    return [(a, frozenset(b)) for a, b in res]


def load_ref():
    ref = {}
    for f in os.listdir(CACHE):
        m = re.match(r'(?:q2_)?s(\d+)\.json$', f)
        if not m: continue
        n = int(m.group(1))
        d = json.load(open(os.path.join(CACHE, f), encoding='utf8'))
        x = d.get('data') if isinstance(d, dict) else None
        if isinstance(x, list): x = next((e for e in x if 'uthmani' in str(e.get('edition', {}).get('identifier'))), None)
        if not x or 'ayahs' not in x: continue
        ref[n] = [a['text'] for a in x['ayahs']]
    return ref


REF = load_ref()
BISMILLAH = skel_na('بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ')
SK = {}
for n, ay in REF.items():
    parts, pos, starts = [], 0, []
    for i, t in enumerate(ay):
        k = skel_na(t)
        if i == 0 and n not in (1, 9) and k.startswith(BISMILLAH): k = k[len(BISMILLAH):]
        starts.append((pos, i + 1)); parts.append(k); pos += len(k)
    SK[n] = (''.join(parts), starts, parts)


def find(sk0):
    """-> (surah, first ayah, last ayah, differences, reference skeleton) of the best match of the (alef-less) skeleton, or None"""
    sk = sk0.replace('ا', '')
    if len(sk) < 9: return None
    def ayrange(starts, lo, ln):
        a = max(st[1] for st in starts if st[0] <= max(0, lo))
        b = max(st[1] for st in starts if st[0] <= max(0, lo) + ln - 1)
        return a, b
    for n, (full, starts, parts) in SK.items():
        i = full.find(sk)
        if i >= 0:
            a, b = ayrange(starts, i, len(sk)); return (n, a, b, 0, full[i:i + len(sk)])
    best = None
    for off in range(0, max(1, len(sk) - 8), 4):
        anc = sk[off:off + 8]
        for n, (full, starts, parts) in SK.items():
            j = full.find(anc)
            while j >= 0:
                lo = j - off
                for d in (0, -1, 1, -2, 2):
                    seg = full[max(0, lo + d): lo + d + len(sk)]
                    if len(seg) != len(sk): continue
                    diff = sum(1 for p, q in zip(seg, sk) if p != q)
                    if diff <= 3 and (best is None or diff < best[3]):
                        a, b = ayrange(starts, lo + d, len(sk)); best = (n, a, b, diff, seg)
                j = full.find(anc, j + 1)
        if best: return best
    return None


def diac_diffs(data, ref_text):
    a = letters_with_marks(data); b = letters_with_marks(ref_text)
    out = []
    if [x[0] for x in a] != [x[0] for x in b]: return out
    for i, ((l1, m1), (l2, m2)) in enumerate(zip(a, b)):
        # fathatan/dammatan/kasratan written as a pair of marks in some fonts; sukun on a letter followed by shadda etc. -> compare vowel quality only
        v1 = set(m1) & set('\u064E\u064F\u0650\u064B\u064C\u064D\u0651\u0652')
        v2 = set(m2) & set('\u064E\u064F\u0650\u064B\u064C\u064D\u0651\u0652')
        # a letter that has a vowel in one text and a sukun-less bare form in the other is the madd / silent-letter notation: ignore
        if v1 == v2: continue
        if (not v1 and v2 <= {'\u0652'}) or (not v2 and v1 <= {'\u0652'}): continue
        out.append((i, l1, ''.join(sorted(v1)), ''.join(sorted(v2))))
    return out


if __name__ == '__main__':
    path = sys.argv[1]
    show = int(sys.argv[sys.argv.index('--show') + 1]) if '--show' in sys.argv else 20
    import subprocess
    tmp = os.path.join(os.environ.get('TEMP', '.'), 'ayat_strings.json')
    pages = tmp
    subprocess.run(['node', 'tools/qa/page_text.js', path, tmp, '--urdu'], check=True, stdout=subprocess.DEVNULL)
    data = json.load(open(tmp, encoding='utf8'))
    seen = set(); cand = 0; ident = 0; sp = []; dc = []
    for pg, lst in data.items():
        for s in lst:
            if s in seen: continue
            seen.add(s)
            for seg in re.split(r'[\n۔]|\s{2,}', re.sub(r'[(（][^)）]*[)）]', ' ', re.sub(r'[A-Za-z0-9٠-٩۰-۹:]+', ' ', s))):
                if len(MARKS.findall(seg)) < 4 or len(skel_na(seg)) < 9: continue
                # skip mostly-Urdu lines: Urdu has these letters that Qur'anic Arabic lacks
                if re.search('[ٹڈڑںںگپچژے]', seg) or len(re.findall('[ہ]', seg)) > 2: continue
                cand += 1
                f = find(skel_na(seg))
                if not f: continue
                ident += 1
                n, a, b, diff, refseg = f
                if diff: sp.append((pg, n, a, b, diff, seg.strip()[:80]))
                else:
                    ref_text = ' '.join(REF[n][a - 1:b])
                    d = diac_diffs(seg, ref_text) if (b - a) == 0 and len(REF[n][a - 1]) else []
                    if d: dc.append((pg, n, a, seg.strip()[:60], d[:4]))
    print('candidates', cand, 'identified', ident, 'spelling differences', len(sp), 'diacritic differences', len(dc))
    for x in sp[:show]: print('SPELL p%s %s:%s-%s diff=%d | %s' % x)
    for x in dc[:show]: print('DIAC p%s %s:%s | %s | %s' % x)
    if '--json' in sys.argv:
        json.dump({'spell': sp, 'diac': dc}, open(sys.argv[sys.argv.index('--json') + 1], 'w', encoding='utf8'), ensure_ascii=False, indent=1)
