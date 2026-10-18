"""Expand Qur'an verse references into page DSL lines (Class 10 Mutalia-e-Quran).

    python -X utf8 tools/qv_expand.py SUBJ NNN [NNN ...]     (reads SUBJ/src/pNNN.src, writes SUBJ/pages/pNNN.txt)
    python -X utf8 tools/qv_expand.py SUBJ all

In a .src file a line
    v S:A || URDU || ENGLISH || PASHTO
becomes
    p ARABIC ﴿A﴾ — URDU || ARABIC ﴿A﴾ — ENGLISH || ARABIC ﴿A﴾ — PASHTO
The Arabic (Uthmani script) comes from the alquran.cloud cache in D:/SpaceBook/_qcache/sNN.json
(fetch with: curl https://api.alquran.cloud/v1/surah/NN/quran-uthmani -o sNN.json); the leading
basmala that the API prefixes to verse 1 is removed (except in Al-Fatihah). The Urdu is the book's
translation, transcribed from the scan; English and Pashto are ours. Every other line is copied as is, except that {{U S:A}}, {{E S:A}}, {{P S:A}} are replaced by that
verse's Urdu / English / Pashto translation as recorded on its v line (for model answers).
"""
import sys, json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
CACHE = Path('D:/SpaceBook/_qcache')
BASMALA = 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ '
_q = {}
AR_DIG = str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩')


def ayah(s, a):
    if s not in _q:
        _q[s] = [x['text'] for x in json.loads((CACHE / f's{s}.json').read_text(encoding='utf-8'))['data']['ayahs']]
    t = _q[s][a - 1]
    if a == 1 and s != 1 and t.startswith(BASMALA):
        t = t[len(BASMALA):]
    return f'{t} ﴿{str(a).translate(AR_DIG)}﴾'


TR = {}


def collect(subj):
    """First pass: record every verse's UR/EN/PS translation so {{U S:A}} / {{E S:A}} / {{P S:A}} can quote it."""
    for f in sorted((HERE / subj / 'src').glob('p*.src')):
        for line in f.read_text(encoding='utf-8').splitlines():
            if line.startswith('v '):
                parts = [p.strip() for p in line[2:].split('||')]
                if len(parts) == 4:
                    TR[parts[0]] = parts[1:]


def quote(line):
    def rep(m):
        k, ref = m.group(1), m.group(2)
        if ref not in TR:
            raise SystemExit(f'no translation recorded for {ref}')
        return TR[ref]['UEP'.index(k)]
    return re.sub(r'\{\{([UEP]) (\d+:\d+)\}\}', rep, line)


def expand(subj, n):
    src = HERE / subj / 'src' / f'p{n:03}.src'
    out = []
    for line in src.read_text(encoding='utf-8').splitlines():
        line = quote(line)
        if line.startswith('v '):
            parts = [p.strip() for p in line[2:].split('||')]
            if len(parts) != 4:
                raise SystemExit(f'{src.name}: verse line needs S:A || UR || EN || PS: {line[:80]}')
            ref, ur, en, ps = parts
            s, a = ref.split(':')
            a1, _, a2 = a.partition('-')
            ar = ' '.join(ayah(int(s), k) for k in range(int(a1), int(a2 or a1) + 1))
            out.append(f'p {ar} — {ur} || {ar} — {en} || {ar} — {ps}')
        else:
            out.append(line)
    (HERE / subj / 'pages' / f'p{n:03}.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')


if __name__ == '__main__':
    subj = sys.argv[1]
    nums = [int(p.stem[1:]) for p in sorted((HERE / subj / 'src').glob('p*.src'))] if sys.argv[2] == 'all' else [int(x) for x in sys.argv[2:]]
    collect(subj)
    for n in nums:
        expand(subj, n)
    print('expanded', len(nums))
