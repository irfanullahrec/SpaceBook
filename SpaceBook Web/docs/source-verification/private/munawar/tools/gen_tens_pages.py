"""Writes the Class 1 Mathematics pages "Numbers 31 to 40" ... "Numbers 91 to 99" (printed pages 17-23, PDF pages 16-22).

    python -P docs/source-verification/private/munawar/tools/gen_tens_pages.py

Every one of these pages is the same printed table (the sample scan shows it clearly): a row of pencil pictures, T bundles of ten and 1-9 loose pencils,
and three boxes for Tens, Ones and Numbers; the first row is filled in as an example and the last row has one more bundle and no loose pencil
(Numbers 91 to 99 has nine rows and no last row). Pages 14-16 (0-10, 11-20, 21-30) were typed by hand (p013-p015) in the same words.
The pages are generated so the sentences are exactly the same on every page; the numbers of bundles and pencils are the printed ones.
Only the example row carries the place-value picture (every row's wording already says how many bundles and loose pencils it shows): a picture per row
would make the book file five times larger than the Government Mathematics books.
"""
from pathlib import Path

PAGES = Path(__file__).resolve().parents[1] / 'c1-math' / 'pages'
UR = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
TEACH = {
    'give': ('Give students different groups of objects to make bundles of tens and ones and help them to count the numbers.',
             'طلبہ کو چیزوں کے مختلف گروپ دیں کہ وہ دہائیوں اور اکائیوں کے گٹھے بنائیں اور اعداد گننے میں ان کی مدد کریں۔',
             'زده کوونکو ته د شیانو بېلابېلې ډلې ورکړئ چې د لسیزو او یوونو ګولې جوړې کړي او د عددونو په شمېرلو کې ورسره مرسته وکړئ.'),
    'explain': ('Explain the concept of tens and ones to students by using pencils. Also tell them that "tens and ones" is known as the place value of digits.',
                'طلبہ کو پنسلوں کی مدد سے دہائیوں اور اکائیوں کا تصور سمجھائیں۔ انہیں یہ بھی بتائیں کہ "دہائیاں اور اکائیاں" ہندسوں کی مقامی قیمت کہلاتی ہیں۔',
                'زده کوونکو ته د پنسلونو په مرسته د لسیزو او یوونو مفهوم تشریح کړئ. دوی ته دا هم ووایئ چې "لسیزې او یووونه" د رقمونو مکانی ارزښت بلل کېږي.'),
    'conduct': ('Conduct activities in the class so that students count different objects to clear the concept of tens and ones.',
                'کلاس میں ایسی سرگرمیاں کرائیں جن میں طلبہ دہائیوں اور اکائیوں کا تصور واضح کرنے کے لیے مختلف چیزیں گنیں۔',
                'په ټولګي کې داسې فعالیتونه ترسره کړئ چې زده کوونکي د لسیزو او یوونو د مفهوم د روښانه کولو لپاره بېلابېل شیان وشمېري.'),
}
# (first number, last number, printed page, teacher strip)
SPECS = [(31, 40, 17, 'give'), (41, 50, 18, 'explain'), (51, 60, 19, 'conduct'), (61, 70, 20, 'explain'),
         (71, 80, 21, 'give'), (81, 90, 22, 'conduct'), (91, 99, 23, 'explain')]


def u(n):
    return str(n).translate(UR)


def page(lo, hi, printed, teach):
    t = lo // 10
    last_full = hi == 99
    out = [f'@printed {printed}',
           f'@sec n{lo}to{hi} | Numbers {lo} to {hi} || اعداد {u(lo)} تا {u(hi)} || عددونه {u(lo)} تر {u(hi)}',
           f'@deco A cartoon man in a suit presents the page; a coloured banner; a table of pencil pictures ({t} bundles of ten and 1 to 9 loose pencils'
           + ('' if last_full else f', then {t + 1} bundles') + ') with three boxes each for Tens, Ones and Numbers; the first row is filled in as an example '
           f'({t}, 1, {lo}).',
           f'# Numbers {lo} to {hi} || اعداد {u(lo)} تا {u(hi)} || عددونه {u(lo)} تر {u(hi)}',
           'p Read the given numbers with the help of tens and ones. || دیے گئے اعداد کو دہائیوں اور اکائیوں کی مدد سے پڑھیں۔ || ورکړل شوي عددونه د لسیزو او یوونو په مرسته ولولئ.',
           f'exercise Numbers {lo} to {hi} (Page {printed})',
           f'p Look at the pictures and write numbers {lo}-{hi} after counting tens and ones. || تصویریں دیکھیں اور دہائیاں اور اکائیاں گننے کے بعد اعداد {u(lo)} تا {u(hi)} لکھیں۔ || انځورونه وګورئ او لسیزې او یووونه له شمېرلو وروسته عددونه {u(lo)} تر {u(hi)} ولیکئ.',
           f'tens {t} 1 || Example: {t} tens and 1 one: Tens {t}, Ones 1, Number {lo}. || مثال: {u(t)} دہائیاں اور ۱ اکائی: دہائیاں {u(t)}، اکائیاں ۱، عدد {u(lo)}۔ || بېلګه: {u(t)} لسیزې او ۱ یو: لسیزې {u(t)}، یووونه ۱، عدد {u(lo)}.']
    q = 0
    for n in range(lo + 1, hi + 1):
        q += 1
        o = n - 10 * t
        out += [f'q {q} | {t} bundles of ten pencils and {o} loose pencils. Write the tens, the ones and the number. || دس پنسلوں کے {u(t)} گٹھے اور {u(o)} کھلی پنسلیں۔ دہائیاں، اکائیاں اور عدد لکھیں۔ || د لسو پنسلونو {u(t)} ګولې او {u(o)} خلاص پنسلونه. لسیزې، یووونه او عدد ولیکئ.',
                f'sol {t}, {o}, {n} ## Tens {t}, ones {o}: the number is {n}. || دہائیاں {u(t)}، اکائیاں {u(o)}: عدد {u(n)} ہے۔ || لسیزې {u(t)}، یووونه {u(o)}: عدد {u(n)} دی.']
    if not last_full:
        q += 1
        n = hi
        out += [f'q {q} | {t + 1} bundles of ten pencils and no loose pencil. Write the tens, the ones and the number. || دس پنسلوں کے {u(t + 1)} گٹھے اور کوئی کھلی پنسل نہیں۔ دہائیاں، اکائیاں اور عدد لکھیں۔ || د لسو پنسلونو {u(t + 1)} ګولې او هېڅ خلاص پنسل نشته. لسیزې، یووونه او عدد ولیکئ.',
                f'sol {t + 1}, 0, {n} ## Tens {t + 1}, ones 0: the number is {n}. || دہائیاں {u(t + 1)}، اکائیاں ۰: عدد {u(n)} ہے۔ || لسیزې {u(t + 1)}، یووونه ۰: عدد {u(n)} دی.']
    out.append('endexercise')
    en, ur, ps = TEACH[teach]
    out += ['box teach | Guidelines for Teachers || اساتذہ کے لیے ہدایات || د ښوونکو لپاره لارښوونې', f'p {en} || {ur} || {ps}', 'endbox']
    return '\n'.join(out) + '\n'


for lo, hi, printed, teach in SPECS:
    idx = printed - 1
    (PAGES / f'p{idx:03}.txt').write_text(page(lo, hi, printed, teach), encoding='utf-8', newline='\n')
    print('wrote', f'p{idx:03}.txt', f'Numbers {lo}-{hi}')
