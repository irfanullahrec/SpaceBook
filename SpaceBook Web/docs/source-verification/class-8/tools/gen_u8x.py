"""Class 8 Maths phase 6: (1) computed items 3.5 Q4, 8.6 Q2/Q5, 9.2 Q5, 9.4 Q6; (2) definitions 6.1 Q8, 11.1 Q1-2, 11.5 Q1;
(3) key-driven option rows of the Review Exercise multiple-choice blocks (each option row says whether it is the printed-key answer).
Needs tmp/m8_leaves.json (node tmp/mdump.cjs 8). Writes class-8/math/dsl/u8x.txt, then:
    python docs/source-verification/class-7/tools/msol_run.py 8 ; python docs/source-verification/class-8/tools/apply_gen8.py"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent.parent / 'math' / 'dsl' / 'u8x.txt'
L = []


def N(en, ur, ps):
    return f'{en}|{ur}|{ps}'


def add(key, rows, ans, note=None):
    s = f'{key} ~ ' + ' ;; '.join(rows)
    if note:
        s += ' @@ ' + note
    L.append(s + f' => {ans} %%')


def kn(k):
    return N(f'The printed key shows {k}, which does not match the data given in the question.',
             f'چھپی کلید {k} دیتی ہے جو سوال کے اعداد سے نہیں ملتا۔',
             f'چاپ شوې کلیل {k} ښیي چې د پوښتنې له شمېرو سره نه جوړیږي.')


def text(key, en, ur, ps, ans):
    L.append(f'{key} ~ @text {en}|{ur}|{ps} => {ans} %%')


# ---- computed
add('3.5|4|', [r'\text{Year 1: } 700000 \times \frac{3.5}{100} = 24500',
               r'\text{Year 2 (value after 5\% depreciation): } 700000 \times 0.95 = 665000;\; 665000 \times \frac{3.5}{100} = 23275',
               r'\text{Year 3: } 665000 \times 0.95 = 631750;\; 631750 \times \frac{3.5}{100} = 22111.25',
               r'24500 + 23275 + 22111.25 = 69886.25'], 'Rs 69,886.25')
add('8.6|2|', [r'2x + 3y = 61 \quad (1)', r'4x - 5y = 45 \quad (2)', r'(1) \times 2: \; 4x + 6y = 122',
               r'\text{Subtract (2): } 11y = 77 \Rightarrow y = 7', r'2x + 3(7) = 61 \Rightarrow 2x = 40 \Rightarrow x = 20'], 'First number 20, second number 7')
add('8.6|5|', [r'5p + 2c = 850 \quad (1)', r'7p + 3c = 1200 \quad (2)', r'(1) \times 3: \; 15p + 6c = 2550;\; (2) \times 2: \; 14p + 6c = 2400',
               r'\text{Subtract: } p = 150', r'5(150) + 2c = 850 \Rightarrow 2c = 100 \Rightarrow c = 50'], 'Potatoes Rs 150 per kg, carrots Rs 50 per kg')
add('9.2|5|', [r'\text{Arc length} = \frac{\theta}{360} \times 2\pi r', r'\frac{150}{360} \times 2 \times \frac{22}{7} \times 40 = 104.76'], '104.76 m')
add('9.4|6|', [r'\text{Four triangular faces} = 4 \times \frac{1}{2} \times 4 \times 6 = 48',
               r'V = \frac{1}{3} \times \text{base area} \times h = \frac{1}{3} \times 16 \times 5 = 26.67'], 'Fabric 48 m², capacity 26.67 m³')

# ---- definitions
text('6.1|8|', 'In an arithmetic sequence each term is found by adding the same number (common difference): 2, 5, 8, 11, … (d = 3). In a geometric sequence each term is found by multiplying by the same number (common ratio): 3, 6, 12, 24, … (r = 2).',
     'حسابی تسلسل میں ہر رکن میں ایک ہی عدد (مشترک فرق) جمع کر کے اگلا رکن ملتا ہے: 2, 5, 8, 11, … (d = 3)۔ ہندسی تسلسل میں ہر رکن کو ایک ہی عدد (مشترک نسبت) سے ضرب دے کر اگلا رکن ملتا ہے: 3, 6, 12, 24, … (r = 2)۔',
     'حسابي ترتیب کې هر رکن ته یو شان عدد (ګډ توپیر) جمع کیږي: 2, 5, 8, 11, … (d = 3). هندسي ترتیب کې هر رکن په یو شان عدد (ګډ نسبت) کې ضربیږي: 3, 6, 12, 24, … (r = 2).',
     'Arithmetic: add a common difference. Geometric: multiply by a common ratio.')
text('11.1|1|', 'Discrete data can take only separate (counted) values, usually whole numbers, for example the number of students. Continuous data can take any value in a range (measured), for example height or temperature.',
     'منفصل (ڈسکریٹ) ڈیٹا صرف الگ الگ گنی جانے والی قدریں لیتا ہے، عموماً مکمل اعداد، مثلاً طلبہ کی تعداد۔ مسلسل (کنٹینیوئس) ڈیٹا کسی بھی حد کے اندر کوئی بھی قدر لے سکتا ہے (ناپا جاتا ہے)، مثلاً قد یا درجہ حرارت۔',
     'بېل شوی (ډیسکریټ) ډاټا یوازې جلا جلا شمېرل شوې قیمتونه اخلي، ډیری وخت بشپړ عددونه، لکه د زده کوونکو شمېر. دوامداره (کنټینیوس) ډاټا په یوه حد کې هر قیمت اخیستی شي (اندازه کیږي)، لکه قد یا تودوخه.',
     'Discrete: counted values. Continuous: measured values.')
text('11.1|2|', 'Discrete: the number of books on a shelf (12), the number of goals in a match (3). Continuous: the height of a student (152.4 cm), the temperature of a room (24.6 °C).',
     'منفصل: شیلف پر کتابوں کی تعداد (12)، میچ میں گولوں کی تعداد (3)۔ مسلسل: طالب علم کا قد (152.4 سینٹی میٹر)، کمرے کا درجہ حرارت (24.6 °C)۔',
     'بېل شوی: په المارۍ کې د کتابونو شمېر (12)، په لوبه کې د ګولونو شمېر (3). دوامداره: د زده کوونکي قد (152.4 سانتي متره)، د خونې تودوخه (24.6 °C).',
     'Discrete: books on a shelf, goals in a match. Continuous: height, temperature.')
text('11.5|1|', 'Theoretical probability is worked out from the possible outcomes: P = favourable outcomes ÷ total outcomes (a fair coin gives heads with P = 1/2). Experimental probability comes from an experiment: P = number of times the event happened ÷ number of trials.',
     'نظریاتی احتمال ممکنہ نتائج سے نکالا جاتا ہے: P = سازگار نتائج ÷ کل نتائج (منصفانہ سکے پر چت کا P = 1/2)۔ تجرباتی احتمال تجربے سے ملتا ہے: P = واقعہ جتنی بار ہوا ÷ کل کوششیں۔',
     'نظري احتمال له ممکنه پایلو څخه ایستل کیږي: P = مناسبې پایلې ÷ ټولې پایلې (په منصفه سکه کې د سر P = 1/2). تجربوي احتمال له تجربې څخه ترلاسه کیږي: P = پېښه څو ځله شوې ÷ ټولې هڅې.',
     'Theoretical = favourable ÷ possible outcomes; experimental = times it happened ÷ trials.')

OVERRIDE = {
    ('Review Exercise 5', 'c'): N('A set with 3 elements has 2³ = 8 subsets. No option is 8, so none is correct as printed (the printed key marks ii, 9).',
                                  '3 عناصر والے سیٹ کے 2³ = 8 ذیلی سیٹ ہوتے ہیں۔ کوئی آپشن 8 نہیں، اس لیے چھپے ہوئے آپشنز میں کوئی درست نہیں (چھپی کلید ii یعنی 9 دیتی ہے)۔',
                                  'د 3 عناصرو لرونکي سیټ 2³ = 8 فرعي سیټونه لري. هیڅ انتخاب 8 نه دی، نو چاپ شوو انتخابونو کې هیڅ سم نه دی (چاپ شوې کلیل ii یعنې 9 ښیي).'),
}

# ---- key-driven option rows
own = {ln.split(' ~')[0] for ln in OUT.read_text(encoding='utf-8').splitlines() if ' ~' in ln} if OUT.exists() else set()
g = json.load(open(ROOT / 'docs/source-verification/class-8/math/gen_solutions.json', encoding='utf8'))
leaves = json.load(open(ROOT / 'tmp/m8_leaves.json', encoding='utf8'))
cur = None
count = 0
for l in leaves:
    if not (l['q'].isalpha() and len(l['q']) == 1):
        cur = None
        if l.get('key'):
            kt = re.sub(r'(\([a-z]\)\s*)\((i|ii|iii|iv|v)\)', lambda m: m.group(1) + m.group(2), l['key'])
            cur = {a: [x for x in re.split(r'[,\s]+|and', b) if x] for a, b in
                   re.findall(r'\(?([a-z])\)\s*([ivx,\sand]+?)(?=;|\s\(?[a-z]\)|$)', kt)}
        continue
    pts = l['parts']
    if not pts or pts[0][0] != 'i' or not cur or l['q'] not in cur:
        continue
    right = cur[l['q']]
    odd = OVERRIDE.get((l['ex'], l['q']))
    for p, t in pts:
        if (f"{l['ex']}|{l['q']}|{p}" in g and f"{l['ex']}|{l['q']}|{p}" not in own) or any(c in t for c in ('|', '~', ';;', '=>', '@@', '%%')):
            continue
        rs = ', '.join(right)
        if odd:
            en, ur, ps = odd.split('|')
            ans = en
        elif p in right:
            en, ur, ps = (f'Option {p}) is correct: {t}', f'آپشن {p}) درست ہے: {t}', f'انتخاب {p}) سم دی: {t}')
            ans = f'Option {p}) is correct'
        else:
            en, ur, ps = (f'Option {p}) ({t}) is not the answer; the correct option is {rs}.',
                          f'آپشن {p}) ({t}) جواب نہیں؛ درست آپشن {rs} ہے۔',
                          f'انتخاب {p}) ({t}) ځواب نه دی؛ سم انتخاب {rs} دی.')
            ans = f'Correct option: {rs}'
        if not odd:
            en += ' (answer from the printed key)'
            ur += ' (چھپی کلید کے مطابق)'
            ps += ' (د چاپ شوې کلیل له مخې)'
        text(f"{l['ex']}|{l['q']}|{p}", en, ur, ps, ans)
        count += 1

OUT.write_text('\n'.join(L) + '\n', encoding='utf-8')
print(len(L), 'rows;', count, 'option rows')
