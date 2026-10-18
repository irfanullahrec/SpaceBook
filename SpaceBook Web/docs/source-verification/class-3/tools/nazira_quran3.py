"""Class 3 Nazira: write the Quran lesson page files (nazira/pages/pNNN.txt) from a page spec (nazira_spec3.py).

Quran text: Indo-Pak script from quran.com (api.quran.com/api/v4/quran/verses/indopak), cached in D:/SpaceBook/_qcache/ip_sN.json.
English meaning: M. M. Pickthall (1930, public domain), cached in D:/SpaceBook/_qcache/q2_sN.json (alquran.cloud).
The ayah range of every page, the side boxes and the teaching points are read from the scans; the book prints no translation.
Never hand-type Quran text: every ayah comes from the cache.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
Q = Path('D:/SpaceBook/_qcache')
AR_DIG = str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩')

SURAH = {2: ('سُوْرَةُ الْبَقَرَةِ', 'Surah Al-Baqarah', 'البقرۃ', 'Al-Baqarah', 'مدنیۃ', 'Madani', 286, 40),
         3: ('سُوْرَةُ اٰلِ عِمْرٰنَ', 'Surah Aal-Imran', 'آل عمران', 'Aal-Imran', 'مدنیۃ', 'Madani', 200, 20),
         4: ('سُوْرَةُ النِّسَآءِ', 'Surah An-Nisa', 'النساء', 'An-Nisa', 'مدنیۃ', 'Madani', 176, 24),
         5: ('سُوْرَةُ الْمَآئِدَةِ', 'Surah Al-Ma\'idah', 'المائدۃ', 'Al-Ma\'idah', 'مدنیۃ', 'Madani', 120, 16),
         6: ('سُوْرَةُ الْاَنْعَامِ', 'Surah Al-An\'am', 'الانعام', 'Al-An\'am', 'مکیۃ', 'Makki', 165, 20),
         7: ('سُوْرَةُ الْاَعْرَافِ', 'Surah Al-A\'raf', 'الاعراف', 'Al-A\'raf', 'مکیۃ', 'Makki', 206, 24)}


def clean(t):
    t = re.sub('[\ue000-\uf8ff\u200b-\u200f]', '', t)
    t = t.replace('ٮِٕ', 'ئِ').replace('ٮٕ', 'ئ').replace('ٮ', 'ی')
    return re.sub(r'\s+', ' ', t).strip()


def load(s):
    ar = [clean(v['text_indopak']) for v in json.load(open(Q / f'ip_s{s}.json', encoding='utf-8'))['verses']]
    en = [a['text'] for a in json.load(open(Q / f'q2_s{s}.json', encoding='utf-8'))['data'][1]['ayahs']]
    return ar, en


AR = {s: load(s) for s in SURAH}
BISM = clean(json.load(open(Q / 'ip_s1.json', encoding='utf-8'))['verses'][0]['text_indopak'])


def ayah_lines(s, a, b):
    ar, en = AR[s]
    out = []
    for n in range(a, b + 1):
        t = ar[n - 1]
        mark = f'﴿{str(n).translate(AR_DIG)}﴾'
        out.append(f'p {t} {mark} || ({n}) {en[n - 1]} || {t} {mark}')
    return out


def surah_head(s):
    ar, en, _, _, mk, mke, ayat, ruku = SURAH[s]
    return [f'## {ar} ({mk}) — آیات {str(ayat).translate(AR_DIG)}، رکوع {str(ruku).translate(AR_DIG)} || {en} ({mke}) — {ayat} verses, {ruku} ruku(s) || {ar} ({mk}) — {ayat} آیتونه، {ruku} رکوع',
            f'p {BISM} || In the name of Allah, the Beneficent, the Merciful. || {BISM}']


def rng(s, a, b):
    """'سورۃ البقرۃ آیت 260 تا 264' in three languages."""
    _, _, ur, en, *_ = SURAH[s]
    return (f'سورۃ {ur} آیت {a} تا {b}', f'Surah {en}, verses {a} to {b}', f'سورة {ur}، {a} تر {b} آیتونه')


def mashq(s, a, b):
    u, e, p = rng(s, a, b)
    L = [f'box note | مشق — {u} || Practice — {e} || تمرین — {p}',
         f'p کتاب کے حاشیے میں ان آیات کے چند حصے مشق کے لیے دیے گئے ہیں؛ یہاں مکمل آیات دی گئی ہیں۔ || The book\'s margin prints a few phrases from these verses for practice; the complete verses are given here. || د کتاب په حاشیه کې د دې آیتونو ځینې برخې د تمرین لپاره راغلې؛ دلته بشپړ آیتونه ورکړل شوي.']
    L += ayah_lines(s, a, b)
    return L + ['endbox']


STD2 = ['ایک دوسرے کو درست تلفّظ کے ساتھ پڑھ کر بتائیے۔ || Read them to one another with correct pronunciation. || یو بل ته یې په سم تلفظ ولولئ.',
        'کمرۂ جماعت میں بچّوں کے سامنے بلند آواز سے پڑھنے کا عملی مظاہرہ کیجیے۔ || Demonstrate reading aloud in front of the class. || په ټولګي کې د لوړ غږ د لوستلو ښودنه وکړئ.']


def act(find, items=None):
    """'سرگرمیاں' side box: the 'find and underline' item plus the two standard items (or custom items)."""
    L = ['box note | سرگرمیاں || Activities || فعالیتونه', '- ' + find]
    L += ['- ' + i for i in (items if items is not None else STD2)]
    return L + ['endbox']


HEAD = ['قرآنی آیات کو بلند آواز سے پڑھیے اور ساتھ ساتھ بچّوں سے بھی پڑھوائیے۔ || Read the Quranic verses aloud and have the children read along with you. || قرآني آیتونه په لوړ غږ ولولئ او ماشومان دې درسره ولولي.',
        'تقلیدی خواندگی کے دوران آیات کے سرخ رنگ والے حصوں کی ادائی پر خصوصی توجہ دیجیے اور تجوید کے قواعد کی شناخت کروائیے۔ || While the children repeat after you, pay special attention to the parts printed in red and help them identify the tajweed rules. || د تقلیدي لوستلو پر مهال سرو برخو ته ځانګړې پاملرنه وکړئ او د تجوید قواعد وروپېژنئ.',
        'آیات کو درست تلفّظ کے ساتھ پڑھنے میں بچّوں کی مدد کیجیے۔ || Help the children read the verses with correct pronunciation. || له ماشومانو سره د آیتونو په سم تلفظ لوستلو کې مرسته وکړئ.']
T_ACT = ['بورڈ کی مدد سے بائیں طرف حاشیے میں دی گئی سرگرمیاں بچّوں سے مکمل کروائیے۔ || Using the board, have the children complete the activities in the left margin. || د تختې په مرسته دې ماشومان په کیڼه حاشیه کې فعالیتونه بشپړ کړي.',
         'سرگرمیوں میں بچّوں کو حصّہ لینے کا برابر موقع دیجیے۔ || Give every child an equal chance to take part in the activities. || ټولو ماشومانو ته په فعالیتونو کې د ګډون برابر فرصت ورکړئ.']
T_MASHQ = ['بائیں طرف کے حاشیے میں مشق کے عنوان کے تحت درج قرآنی آیات کے حصّوں کو بلند آواز میں پڑھیے اور ساتھ ساتھ بچّوں سے بھی پڑھوائیے۔ || Read aloud the Quranic phrases under "Practice" in the left margin and have the children read along. || په کیڼه حاشیه کې د "تمرین" لاندې قرآني برخې په لوړ غږ ولولئ او ماشومان دې درسره ولولي.']


def homework(s, a, b):
    u, e, p = rng(s, a, b)
    return f'ہوم ورک: بچّوں کو قرآن مجید میں سے {u} گھر سے پڑھ کر آنے کی تاکید کیجیے۔ || Homework: ask the children to read {e} from the Holy Quran at home. || کورنی کار: ماشومانو ته ووایاست چې له قرآن مجید څخه {p} په کور کې ولولي.'


def teach(kind, extra=(), hw=None):
    L = ['box teach | نکتۂ تدریس || Teaching point || د تدریس ټکی'] + ['- ' + t for t in HEAD]
    L += ['- ' + t for t in extra]
    L += ['- ' + t for t in (T_ACT if kind == 'act' else T_MASHQ)]
    if hw:
        L.append('- ' + homework(*hw))
    return L + ['endbox']


PAGES = []


def page(idx, printed, ranges, side, kind, extra=(), hw=None, head=(), issue=None, slo=None):
    PAGES.append(dict(idx=idx, printed=printed, ranges=ranges, side=side, kind=kind, extra=list(extra), hw=hw,
                      head=list(head), issue=issue, slo=slo))


NOTE = ('@issue Quran text: Indo-Pak script (quran.com). English meaning: M. M. Pickthall (1930, public domain); the book prints no '
        'translation, and no verified public-domain Pashto translation is available, so the Pashto slot repeats the Arabic text. '
        'Ruku (ع) marks and the colour coding of tajweed words are not reproduced. The book prints only some of the verses of each '
        'lesson; the verses it skips are set as practice and homework (see the boxes).')


def write():
    for P in PAGES:
        L = [f'@printed {P["printed"]}']
        L += [h for h in P['head'] if h.startswith('@')]
        L.append(NOTE)
        if P['issue']:
            L.append('@issue ' + P['issue'])
        L.append('@deco A framed Mushaf page (15 lines) with tajweed words printed in colour, beside a yellow side panel.')
        L += [h for h in P['head'] if not h.startswith('@')]
        if P['slo']:
            L += P['slo']
        for s, a, b in P['ranges']:
            if a == 1:
                L += surah_head(s)
            L += ayah_lines(s, a, b)
        L += P['side']
        L += teach(P['kind'], P['extra'], P['hw'])
        (HERE / 'nazira' / 'pages' / f'p{P["idx"]:03}.txt').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('wrote', len(PAGES), 'pages')
