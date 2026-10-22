"""Class 7 Maths: sets (6.1 complement/tabular, 6.3 union/intersection) and polynomial
terms/degree (7.2 Q1, 7.3 Q1/Q4) as trilingual text solutions.
Writes class-7/math/dsl/sets_poly.txt; then run  python msol_run.py 7  and  python build_math7.py."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / 'math' / 'dsl' / 'sets_poly.txt'
lines = []


def row(*parts):
    return '|'.join(parts)


def emit(key, rows, ans):
    lines.append(f'{key} ~ @text ' + ' ;; '.join(rows) + f' => {ans} %%')


UNION = row('The union contains every element that is in at least one of the sets; a repeated element is written once.',
            'اتحاد میں وہ تمام عناصر ہوتے ہیں جو کم از کم ایک سیٹ میں ہوں؛ مشترک عنصر ایک ہی بار لکھا جاتا ہے۔',
            'اتحاد کې ټول هغه عناصر وي چې لږ تر لږه په یو سیټ کې وي؛ ګډ عنصر یو ځل لیکل کیږي.')
INTER = row('The intersection contains only the elements that are in all of the sets.',
            'تقاطع میں صرف وہ عناصر ہوتے ہیں جو تمام سیٹوں میں موجود ہوں۔',
            'تقاطع کې یوازې هغه عناصر وي چې په ټولو سیټونو کې وي.')
COMP = row('The complement has the elements of the universal set U that are not in the given set.',
           'متمم میں عالمی سیٹ U کے وہ عناصر ہوتے ہیں جو دیے گئے سیٹ میں نہیں ہوتے۔',
           'بشپړوونکی د نړیوال سیټ U هغه عناصر لري چې په ورکړل شوي سیټ کې نه وي.')


def res(sym, val):
    t = f'{sym} = {val}'
    return row(t, t, t)


def sub(en, ur, ps):
    return row(en, ur, ps)


# ---- 6.3 Q1 unions
U1 = {
    'a': ('A ∪ B', '{1, 2, 3, 4, 5, 6, 7}', None),
    'b': ('U ∪ V', '{a, b, c, d, e}', row('V is already inside U, so the union is U.', 'V پہلے ہی U کے اندر ہے، اس لیے اتحاد U ہے۔', 'V مخکې له مخکې په U کې دی، نو اتحاد U دی.')),
    'c': ('K ∪ D', '{1, 2, 4, 5, 6, 8, 10}', row('10 is in both sets, so it is written once.', '10 دونوں سیٹوں میں ہے، اس لیے ایک بار لکھا۔', '10 په دواړو سیټونو کې دی، نو یو ځل ولیکل شو.')),
    'd': ('Z ∪ X ∪ Y', '{0, ±1, ±2, ±3, …} = Z', row('X and Y contain only integers, so both are inside Z and the union is Z.', 'X اور Y میں صرف صحیح اعداد ہیں، دونوں Z کے اندر ہیں، اس لیے اتحاد Z ہے۔', 'X او Y یوازې بشپړ عددونه لري، دواړه په Z کې دي، نو اتحاد Z دی.')),
    'e': ('E ∪ F ∪ N', '{1, 2, 3, 4, …} = N', row('F ⊂ E ⊂ N (every multiple of 4 is even, every even number is natural), so the union is N.', 'F ⊂ E ⊂ N (4 کا ہر مضاعف جفت ہے، ہر جفت عدد قدرتی ہے)، اس لیے اتحاد N ہے۔', 'F ⊂ E ⊂ N (د 4 هر مضرب جفت دی، هر جفت عدد طبیعي دی)، نو اتحاد N دی.')),
}
for p, (sym, val, extra) in U1.items():
    r = [UNION]
    if extra: r.append(extra)
    r.append(res(sym, val))
    emit(f'6.3|1|{p}', r, f'{sym} = {val}')

# ---- 6.3 Q2 intersections
I2 = {
    'a': ('A ∩ B', '{0}', row('Only 0 is in both A and B.', 'صرف 0 A اور B دونوں میں ہے۔', 'یوازې 0 په A او B دواړو کې دی.')),
    'b': ('P ∩ R', '{1, 3, 5, 7, 9}', row('R is inside P, so the intersection is R.', 'R، P کے اندر ہے، اس لیے تقاطع R ہے۔', 'R په P کې دی، نو تقاطع R دی.')),
    'c': ('S ∩ T', '{16}', row('Only 16 is in both S and T.', 'صرف 16 S اور T دونوں میں ہے۔', 'یوازې 16 په S او T دواړو کې دی.')),
    'd': ('X ∩ Y ∩ W', '{3}', row('X ∩ Y = {3} (only 3 is in both); 3 is also in W = {0, 1, 2, …}. The printed key shows {1, 2, 3}, but 1 and 2 are not in X.', 'X ∩ Y = {3} (صرف 3 دونوں میں ہے)؛ 3 W = {0, 1, 2, …} میں بھی ہے۔ چھپی کلید {1, 2, 3} دیتی ہے مگر 1 اور 2 X میں نہیں۔', 'X ∩ Y = {3} (یوازې 3 په دواړو کې دی)؛ 3 په W = {0, 1, 2, …} کې هم دی. چاپ شوې کلیل {1, 2, 3} ښیي خو 1 او 2 په X کې نشته.')),
    'e': ('L ∩ M ∩ N', 'ϕ', row('L ∩ M = {g}, but g is not in N, so nothing is in all three sets.', 'L ∩ M = {g}، مگر g، N میں نہیں، اس لیے تینوں میں کوئی عنصر مشترک نہیں۔', 'L ∩ M = {g}، خو g په N کې نشته، نو په درېواړو کې هیڅ ګډ عنصر نشته.')),
}
for p, (sym, val, extra) in I2.items():
    emit(f'6.3|2|{p}', [INTER, extra, res(sym, val)], f'{sym} = {val}')

emit('6.3|3|', [row('E ⊂ W (every even positive number is a whole number), so E ∪ W = W and E ∩ W = E.',
                    'E ⊂ W (ہر مثبت جفت عدد مکمل عدد ہے)، اس لیے E ∪ W = W اور E ∩ W = E۔',
                    'E ⊂ W (هر مثبت جفت عدد پوره عدد دی)، نو E ∪ W = W او E ∩ W = E.')], 'E ∪ W = W, E ∩ W = E')
emit('6.3|4|', [row('P ⊂ Z (every prime is an integer), so P ∪ Z = Z and P ∩ Z = P.',
                    'P ⊂ Z (ہر مفرد عدد صحیح عدد ہے)، اس لیے P ∪ Z = Z اور P ∩ Z = P۔',
                    'P ⊂ Z (هر لومړی عدد بشپړ عدد دی)، نو P ∪ Z = Z او P ∩ Z = P.')], 'P ∪ Z = Z, P ∩ Z = P')
emit('6.3|7|a', [row('X = {1, …, 20} and Y (even numbers) are both inside W = {0, 1, 2, …}, so X ∪ Y ∪ W = W.',
                     'X = {1, …, 20} اور Y (جفت اعداد) دونوں W = {0, 1, 2, …} کے اندر ہیں، اس لیے X ∪ Y ∪ W = W۔',
                     'X = {1, …, 20} او Y (جفت عددونه) دواړه په W = {0, 1, 2, …} کې دي، نو X ∪ Y ∪ W = W.')],
     'X ∪ Y ∪ W = {0, 1, 2, 3, 4, …}')
emit('6.3|7|b', [row('The even numbers in X are 2, 4, 6, …, 20; all of them are in Y and in W. (The printed key leaves out 6.)',
                     'X کے جفت اعداد 2, 4, 6, …, 20 ہیں؛ سب Y اور W میں ہیں۔ (چھپی کلید میں 6 رہ گیا ہے۔)',
                     'د X جفت عددونه 2, 4, 6, …, 20 دي؛ ټول په Y او W کې دي. (چاپ شوې کلیل 6 پریښی دی.)')],
     'X ∩ Y ∩ W = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}')

# ---- 6.1 Q6 complements (U = a..z)
C6 = {'a': ('S′', '{f, g, h, …, z}', 'S'), 'b': ('T′', '{a, b, c, d, e, j, k, l, …, z}', 'T'),
      'c': ('V′', '{c, d, f, g, h, i, …, z}', 'V'), 'd': ('U′', 'ϕ', 'U')}
for p, (sym, val, s) in C6.items():
    emit(f'6.1|6|{p}', [COMP, res(sym, val)], f'{sym} = {val}')

# ---- 6.1 Q2 tabular form
T2 = {
    'a': ('A', '{31, 33, 35, …, 57, 59}', row('Odd numbers start at 31 and end at 59.', 'طاق اعداد 31 سے شروع ہو کر 59 پر ختم ہوتے ہیں۔', 'تاق عددونه له 31 پیلیږي او په 59 پای ته رسیږي.')),
    'b': ('B', '{1, 2, 3, …, 39}', row('Natural numbers less than 40 are 1 to 39.', '40 سے چھوٹے قدرتی اعداد 1 سے 39 تک ہیں۔', 'له 40 څخه کوچني طبیعي عددونه له 1 څخه تر 39 پورې دي.')),
    'c': ('C', '{12, 24, 36, 48}', row('Multiples of 12: 12, 24, 36, 48; the next one, 60, is not less than 60.', '12 کے مضاعف: 12, 24, 36, 48؛ اگلا 60 ہے جو 60 سے چھوٹا نہیں۔', 'د 12 مضربونه: 12, 24, 36, 48؛ راتلونکی 60 دی چې له 60 څخه کوچنی نه دی.')),
    'd': ('D', '{1, 2, 3, 6}', row('18 = 2·3², 30 = 2·3·5, 42 = 2·3·7: the common prime factors are 2 and 3, and the common factors are 1, 2, 3, 6. The set is {1, 2, 3, 6} (the printed key shows only the greatest, 6).', '18 = 2·3²، 30 = 2·3·5، 42 = 2·3·7: مشترک مفرد جزو 2 اور 3 ہیں، مشترک جزو 1, 2, 3, 6 ہیں۔ سیٹ {1, 2, 3, 6} ہے (چھپی کلید میں صرف سب سے بڑا 6 ہے)۔', '18 = 2·3²، 30 = 2·3·5، 42 = 2·3·7: ګډ لومړني فکتورونه 2 او 3 دي، ګډ فکتورونه 1, 2, 3, 6 دي. سیټ {1, 2, 3, 6} دی (چاپ شوې کلیل یوازې لوی 6 ښیي).')),
    'e': ('E', '{12, 24, 36, 48, …}', row('Divisible by both 3 and 4 means divisible by 12, so these are the multiples of 12.', '3 اور 4 دونوں پر بٹنے کا مطلب 12 پر بٹنا ہے، اس لیے یہ 12 کے مضاعف ہیں۔', 'په 3 او 4 دواړو وېشل کېدل یعنې په 12 وېشل کېدل، نو دا د 12 مضربونه دي.')),
    'f': ('F', 'ϕ', row('Factors of 81 are 1, 3, 9, 27, 81. Between 5 and 30 there are 9 and 27.', '81 کے جزو 1, 3, 9, 27, 81 ہیں۔ 5 اور 30 کے درمیان 9 اور 27 ہیں۔', 'د 81 فکتورونه 1, 3, 9, 27, 81 دي. د 5 او 30 تر منځ 9 او 27 دي.')),
}
for p, (sym, val, extra) in T2.items():
    if p == 'f':
        val = '{9, 27}'
    emit(f'6.1|2|{p}', [extra, res(sym, val)], f'{sym} = {val}')

# ---- 7.2 Q1 terms
terms = {'a': '6a, 8b', 'b': '3y, −2x, −5', 'c': '5x, −y, 7', 'd': '3x², y²', 'e': '7bc, −d', 'f': '13y³, y, 3',
         'g': '5x³, 3x², 7', 'h': 'a², −b², 3', 'i': 'uv, uvw, 4w'}
for p, t in terms.items():
    emit(f'7.2|1|{p}', [row('Terms are the parts of an expression separated by + or −; each term keeps its own sign.',
                           'اجزا (ٹرمز) کسی ریاضی جملے کے وہ حصے ہیں جو + یا − سے الگ ہوں؛ ہر جزو اپنی علامت کے ساتھ رہتا ہے۔',
                           'ټرمونه د جملې هغه برخې دي چې په + یا − سره بېلې وي؛ هر ټرم خپله نښه ساتي.'),
                       row(f'Terms: {t}', f'اجزا: {t}', f'ټرمونه: {t}')], t)

# ---- 7.3 Q4 degree
deg = {'a': ('y + 3 + 3y²', 2), 'b': ('3a² + a − 2', 2), 'c': ('l³ + l² + l', 3), 'd': ('b⁴ + b³ − b²', 4),
       'e': ('5a', 1), 'f': ('2x² − 5x + 1', 2), 'g': ('3l³ − 4l²', 3), 'h': ('10a⁴ − 5a³ + a² + a', 4)}
for p, (poly, d) in deg.items():
    emit(f'7.3|4|{p}', [row('The degree is the highest power of the variable in the polynomial.',
                           'کثیر رقمی کا درجہ اس میں متغیر کی سب سے بڑی طاقت ہوتی ہے۔',
                           'د کثیر الحدي درجه په کې د متغیر تر ټولو لوړه توان دی.'),
                       row(f'{poly}: highest power = {d}', f'{poly}: سب سے بڑی طاقت = {d}', f'{poly}: تر ټولو لوړ توان = {d}')], f'Degree = {d}')

# ---- 7.3 Q1 which are terms of a polynomial
RS = row('A term belongs to a polynomial when every exponent of its variables is a whole number (0, 1, 2, …).',
         'کوئی جزو کثیر رقمی کا حصہ تب ہوتا ہے جب اس کے متغیرات کی تمام طاقتیں مکمل اعداد (0, 1, 2, …) ہوں۔',
         'یو ټرم هغه مهال د کثیر الحدي برخه وي چې د متغیرونو ټول توانونه پوره عددونه (0, 1, 2, …) وي.')
ok = row('Every exponent is a whole number, so every term is a term of a polynomial.',
         'تمام طاقتیں مکمل اعداد ہیں، اس لیے ہر جزو کثیر رقمی کا جزو ہے۔',
         'ټول توانونه پوره عددونه دي، نو هر ټرم د کثیر الحدي ټرم دی.')
for p in 'abcef':
    emit(f'7.3|1|{p}', [RS, ok], 'All terms are terms of a polynomial; the exponents are whole numbers.')
emit('7.3|1|d', [RS, row('5xyz and 2yz have whole-number exponents, so they are terms of a polynomial.',
                         '5xyz اور 2yz کی طاقتیں مکمل اعداد ہیں، اس لیے یہ کثیر رقمی کے اجزا ہیں۔',
                         '5xyz او 2yz توانونه پوره عددونه لري، نو دا د کثیر الحدي ټرمونه دي.'),
                 row('−8xy⁻² has the exponent −2 on y, which is not a whole number, so it is not a term of a polynomial.',
                     '−8xy⁻² میں y کی طاقت −2 ہے جو مکمل عدد نہیں، اس لیے یہ کثیر رقمی کا جزو نہیں۔',
                     'په −8xy⁻² کې د y توان −2 دی چې پوره عدد نه دی، نو دا د کثیر الحدي ټرم نه دی.')],
     '5xyz and 2yz are terms of a polynomial; −8xy⁻² is not (exponent −2 is not a whole number).')

OUT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(len(lines), 'rows ->', OUT)
