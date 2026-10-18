"""Class 2 Nazira: write the Para 1 / Para 2 page files (nazira/pages/pNNN.txt) from a page spec.

Quran text: Indo-Pak script from quran.com (api.quran.com/api/v4/quran/verses/indopak), cached in D:/SpaceBook/_qcache/ip_sN.json.
English meaning: M. M. Pickthall (1930, public domain), cached in D:/SpaceBook/_qcache/q2_sN.json (alquran.cloud).
The ayah range of every page and the side boxes are read from the scans; the book prints no translation.

    python nazira_quran.py            (writes every page in PAGES)
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
Q = Path('D:/SpaceBook/_qcache')
AR_DIG = str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩')

SURAH = {1: ('سُوْرَةُ الْفَاتِحَةِ', 'Surah Al-Fatihah', 'مکیۃ', 'Makki', 7, 1),
         2: ('سُوْرَةُ الْبَقَرَةِ', 'Surah Al-Baqarah', 'مدنیۃ', 'Madani', 286, 40)}


def clean(t):
    t = re.sub('[\ue000-\uf8ff\u200b-\u200f]', '', t)
    t = t.replace('ٮِٕ', 'ئِ').replace('ٮٕ', 'ئ').replace('ٮ', 'ی')
    return re.sub(r'\s+', ' ', t).strip()


def load(s):
    ar = [clean(v['text_indopak']) for v in json.load(open(Q / f'ip_s{s}.json', encoding='utf-8'))['verses']]
    en = [a['text'] for a in json.load(open(Q / f'q2_s{s}.json', encoding='utf-8'))['data'][1]['ayahs']]
    return ar, en


AR = {s: load(s) for s in (1, 2)}


def fatiha():
    """Indo-Pak numbering: the bismillah is not numbered and Hafs verse 7 is split into 6 and 7."""
    ar, en = AR[1]
    v7 = ar[6]
    cut = v7.index('غَیۡرِ') if 'غَیۡرِ' in v7 else v7.index('غَيۡرِ')
    a = ar[1:6] + [v7[:cut].strip(), v7[cut:].strip()]
    e = en[1:6] + ['The path of those whom Thou hast favoured;', 'Not the (path) of those who earn Thine anger nor of those who go astray.']
    return a, e


def ayah_lines(s, a, b):
    if s == 1:
        ar, en = fatiha()
    else:
        ar, en = AR[2]
    out = []
    for n in range(a, b + 1):
        t = ar[n - 1]
        mark = f'﴿{str(n).translate(AR_DIG)}﴾'
        out.append(f'p {t} {mark} || ({n}) {en[n - 1]} || {t} {mark}')
    return out


def surah_head(s):
    ar, en, mk, mke, ayat, ruku = SURAH[s]
    bism = AR[1][0][0]
    return [f'## {ar} ({mk}) — آیات {str(ayat).translate(AR_DIG)}، رکوع {str(ruku).translate(AR_DIG)} || {en} ({mke}) — {ayat} verses, {ruku} ruku(s) || {ar} ({mk}) — {ayat} آیتونه، {ruku} رکوع',
            f'p {bism} || In the name of Allah, the Beneficent, the Merciful. || {bism}']


TAIL = ['قرآنی آیات بلند آواز میں پڑھیے اور ساتھ ساتھ بچّوں سے بھی پڑھوائیے۔ || Read the Quranic verses aloud and have the children read along with you. || قرآني آیتونه په لوړ غږ ولولئ او ماشومان دې درسره ولولي.',
        'رنگین حروف سے متعلق تجوید کے قواعد کی شناخت کروائیے۔ || Help the children identify the tajweed rules shown by the coloured letters. || د رنګه تورو د تجوید قواعد وروپېژنئ.',
        'تلفّظ کی درست ادائی کے لیے مخارج کی شناخت کا عملی مظاہرہ کروائیے۔ || Demonstrate the points of articulation for correct pronunciation. || د سم تلفظ لپاره د مخارجو ښودنه وکړئ.',
        'آیات میں ملا کر پڑھے جانے والے الفاظ کی پڑھائی پر خصوصی توجّہ دیجیے۔ || Pay special attention to words that are joined together when reading the verses. || هغو کلمو ته ځانګړې پاملرنه وکړئ چې په آیتونو کې یوځای لوستل کېږي.']


def teach(first=None):
    lines = ['box teach | نکتۂ تدریس || Teaching point || د تدریس ټکی']
    if first:
        lines += ['- ' + f for f in (first if isinstance(first, list) else [first])]
    lines += ['- ' + t for t in TAIL]
    return lines + ['endbox']


# (scan idx, printed page, [(surah, from, to)], side box lines, first teaching points, extra header lines)
PAGES = []


def page(idx, printed, ranges, side=(), first=None, head=(), mushaf=None, issue=None):
    PAGES.append((idx, printed, ranges, list(side), first, list(head), mushaf, issue))


SIGNS = ['box note | یاد رکھیے — رموزِ اوقاف || Remember — the stopping signs || یاد ولرئ — د وقف نښې',
         '- آیت کے آخر میں علامت ○ ہے، یعنی پڑھتے ہوئے یہاں پر رکنا ہے۔ || The sign ○ at the end of a verse means you stop here while reading. || د آیت په پای کې ○ نښه ده، یعنې دلته ودرېږئ.',
         '- ”لا“ علامت پر رکنا یا ملا کر پڑھنا دونوں ٹھیک ہیں۔ || At the sign "لا" you may either stop or read on; both are correct. || پر ”لا“ نښه درېدل او یوځای لوستل دواړه سم دي.',
         '- ”م“ علامت پر ٹھہرنا لازم ہے۔ || At the sign "م" you must stop. || پر ”م“ نښه درېدل لازمي دي.',
         '- علامت ”ط“ پر وقف کرنا بہتر ہے۔ || At the sign "ط" it is better to stop. || پر ”ط“ درېدل غوره دي.',
         '- علامت ”سکتہ“ پر آواز کو توڑ کر تھوڑا ٹھہرنا ہے لیکن سانس جاری رکھنا ہے۔ || At "saktah", break the sound and pause briefly without taking a breath. || پر ”سکته“ غږ لږ ودروئ خو ساه مه اخلئ.',
         'endbox']
ACT1 = ['box note | سرگرمیاں || Activities || فعالیتونه',
        '- وقف کی علامات کی شناخت کیجیے۔ || Identify the stopping signs. || د وقف نښې وپېژنئ.',
        '- آیات پڑھتے ہوئے وقف کرنے کی مشق کیجیے۔ || Practise stopping correctly while reading the verses. || د آیتونو په لوستلو کې د درېدو تمرین وکړئ.',
        '- درست ادائی کر کے ایک دوسرے کو وقف کے اصول بتائیے۔ || Read correctly and explain the rules of stopping to one another. || سم ولولئ او یو بل ته د وقف اصول ووایئ.',
        'endbox']
MADD = ['box note | یاد رکھیے — حروفِ مدّہ || Remember — the letters of madd || یاد ولرئ — د مد توري',
        '- زبر والے حرف کے بعد اگر الف ہو تو زبر والے حرف کی آواز کو تھوڑا کھینچ کر پڑھنا ہے۔ مثالیں: مَا، بَا، قَالَ۔ || After a letter with zabar, an alif means the sound is drawn out a little. Examples: maa, baa, qaala. || له زبر وروسته الف وي نو غږ لږ اوږدېږي. بېلګې: مَا، بَا، قَالَ.',
        '- زیر والے حرف کے بعد ( ی ) جزم والی ہو تو زیر والے حرف کی آواز کو تھوڑا کھینچ کر پڑھنا ہے۔ مثالیں: بِیْ، تِیْ، سَبِیْلِ۔ || After a letter with zer, a ya with jazm means the sound is drawn out a little. Examples: bee, tee, sabeeli. || له زېر وروسته ساکنه ی وي نو غږ لږ اوږدېږي.',
        '- پیش والے حرف کے بعد ( و ) جزم والی ہو تو پیش والے حرف کی آواز کو تھوڑا کھینچ کر پڑھنا ہے۔ مثالیں: بُوْ، رَسُوْلُ، يَقُوْلُ۔ || After a letter with pesh, a waw with jazm means the sound is drawn out a little. Examples: boo, rasoolu, yaqoolu. || له پېښ وروسته ساکن و وي نو غږ لږ اوږدېږي.',
        'endbox']

page(46, 44, [(1, 1, 7), (2, 1, 4)], SIGNS,
     'بچّوں کو ”یاد رکھیے“ کے تحت وقف کی علامت ○ اور اصولوں کے متعلق بتائیے۔ || Under "Remember", tell the children about the stop sign ○ and the rules of stopping. || د ”یاد ولرئ“ لاندې د ○ نښې او د وقف اصولو په اړه ووایئ.',
     ['@sec para1 | پہلا پارہ || Para 1 || لومړی پاره'], mushaf=1)
page(47, 45, [(2, 5, 15)], ACT1,
     'کمرۂ جماعت میں سرگرمیاں بچّوں سے کروائیے اور تمام بچّوں کو برابر موقع دیجیے۔ || Do the activities with the children in class and give every child an equal chance. || فعالیتونه په ټولګي کې وکړئ او ټولو ته برابر فرصت ورکړئ.', mushaf=2)
page(48, 46, [(2, 16, 23)], MADD,
     'بچّوں کو ”یاد رکھیے“ کے تحت حروفِ مدّہ کے متعلق بتائیے اور اس صفحے سے مثالیں دیجیے۔ || Under "Remember", tell the children about the letters of madd and give examples from this page. || د مد تورو په اړه ووایئ او له دې مخه بېلګې ورکړئ.', mushaf=3)


def write():
    for idx, printed, ranges, side, first, head, mushaf, issue in PAGES:
        L = [f'@printed {printed}']
        L += [h for h in head if h.startswith('@')]
        L.append('@issue Quran text: Indo-Pak script (quran.com). English meaning: M. M. Pickthall (1930, public domain); the book prints no translation, and no verified public-domain Pashto translation is available, so the Pashto slot repeats the Arabic text. Ruku (ع) marks and the colour coding of tajweed letters are not reproduced.')
        if issue:
            L.append('@issue ' + issue)
        if mushaf:
            para, num = (str(mushaf).split(':') if ':' in str(mushaf) else ('1', str(mushaf)))
            ph = 'الٓمّٓ 1' if para == '1' else 'سَیَقُوْلُ 2'
            L.append(f'@deco A framed Mushaf page (15 lines) headed "{ph} · {num} · البقرۃ 2", with tajweed letters printed in colour.')
        L += [h for h in head if not h.startswith('@')]
        for s, a, b in ranges:
            if a == 1:
                L += surah_head(s)
            L += ayah_lines(s, a, b)
        L += side
        L += teach(first)
        (HERE / 'nazira' / 'pages' / f'p{idx:03}.txt').write_text('\n'.join(L) + '\n', encoding='utf-8')
        print('wrote', idx, printed, ranges)


if __name__ == '__main__':
    write()
