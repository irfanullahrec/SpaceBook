from decimal import Decimal as D, ROUND_HALF_UP
r = lambda x, q: str(D(x).quantize(D(q), rounding=ROUND_HALF_UP))
out = ['@printed 77',
       '@deco Cartoon boy with magnifying glass beside "Key Fact"; cartoon book mascot on "Exercise 6".',
       'p Estimate the difference of 25.3 and 7.9. || 25.3 اور 7.9 کے فرق کا اندازہ لگائیں۔ || د 25.3 او 7.9 د توپیر اټکل وکړئ.',
       'table',
       'tr |  | 25',
       'tr | − | 8',
       'tr |  | 17',
       'endtable',
       r'eq 7.9 \approx 8',
       r'eq 25.3 \approx 25',
       r'eq 25.3 - 7.9 \approx 25 - 8 = 17',
       'm $25.3 - 7.9 = 17.4$',
       'p So, our estimation is correct. || لہٰذا ہمارا اندازہ درست ہے۔ || نو زموږ اټکل سم دی.',
       'box key | Key Fact || اہم حقیقت || مهم حقیقت',
       'p Estimation is to find an answer which is closest to the actual answer but is not the actual one. We can estimate the sum and difference of decimals by rounding off them to the nearest whole numbers. || اندازہ لگانے کا مطلب ایسا جواب معلوم کرنا ہے جو اصل جواب کے قریب ترین ہو لیکن اصل جواب نہ ہو۔ ہم اعشاریہ اعداد کو قریب ترین مکمل اعداد تک مدور کر کے ان کے مجموعے اور فرق کا اندازہ لگا سکتے ہیں۔ || اټکل دا دی چې داسې ځواب ومومو چې اصلي ځواب ته تر ټولو نږدې وي خو اصلي ځواب نه وي. موږ د اعشاري عددونو مجموعه او توپیر د هغو تر نږدې بشپړو عددونو پورې په ګردولو اټکلولی شو.',
       'endbox',
       'box check | Try Yourself || خود کوشش کریں || پخپله هڅه وکړئ',
       'p Estimate the sum and difference of the given numbers and then verify your answer. || دیے گئے اعداد کے مجموعے اور فرق کا اندازہ لگائیں اور پھر اپنے جواب کی تصدیق کریں۔ || د ورکړل شوو عددونو د مجموعې او توپیر اټکل وکړئ او بیا خپل ځواب وازمویئ.',
       'qp a | 3.7, 11.4',
       'qp b | 30.8, 4.2',
       'endbox',
       'exercise 6',
       'q 1 | Round-off the following decimals to one and two decimal places. || درج ذیل اعشاریہ اعداد کو ایک اور دو اعشاری مقامات تک مدور کریں۔ || لاندې اعشاري عددونه تر یوه او دوو اعشاري ځایونو پورې ګرد کړئ.']
for l, x in zip('abcdefghijkl', '47.125 4.732 2.322 0.942 45.675 2.150 91.547 94.172 5.183 3.767 4.172 90.267'.split()):
    a, b = r(x, '0.1'), r(x, '0.01')
    out.append(f'qp {l} | {x}')
    out.append(f'sol {a} (1 d.p.); {b} (2 d.p.) ## Look at the digit after the place you keep: 5 or more → add 1, less than 5 → keep it; then drop the digits to its right. || جس مقام تک رکھنا ہے اس کے بعد والا ہندسہ دیکھیں: 5 یا زیادہ → 1 جمع کریں، 5 سے کم → ویسا ہی رکھیں؛ پھر دائیں طرف کے ہندسے ہٹا دیں۔ || د ساتل کېدونکي ځای وروسته رقم ته وګورئ: 5 یا ډېر → 1 جمع کړئ، له 5 کم → هماغسې یې وساتئ؛ بیا ښي لوري رقمونه لرې کړئ.')
for qn, title, op, items in [
        (2, ('Estimate the sum of the given numbers.', 'دیے گئے اعداد کے مجموعے کا اندازہ لگائیں۔', 'د ورکړل شوو عددونو د مجموعې اټکل وکړئ.'), '+',
         ['52.90 17.98', '630.1 280.9', '41.01 36.87', '307.2 357.6', '741.2 30.10', '845.1 396.9', '63.81 25.91', '21.35 83.05', '99.99 87.91', '943.6 834.6', '123.4 567.8', '737.8 721.2']),
        (3, ('Estimate the difference of the given numbers.', 'دیے گئے اعداد کے فرق کا اندازہ لگائیں۔', 'د ورکړل شوو عددونو د توپیر اټکل وکړئ.'), '-',
         ['22.30 17.99', '78.92 69.11', '56.23 11.26', '234.6 159.8', '587.6 320.9', '402.3 292.1', '995.5 747.1', '673.1 430.5', '53.25 25.62', '544.1 41.45', '3.5 2.1', '9.355 7.316'])]:
    out.append(f'q {qn} | {title[0]} || {title[1]} || {title[2]}')
    for l, pair in zip('abcdefghijkl', items):
        a, b = pair.split()
        ra, rb = int(D(a).quantize(D('1'), rounding=ROUND_HALF_UP)), int(D(b).quantize(D('1'), rounding=ROUND_HALF_UP))
        est = ra + rb if op == '+' else ra - rb
        act = D(a) + D(b) if op == '+' else D(a) - D(b)
        sym = '+' if op == '+' else '-'
        out.append(f'qp {l} | ${a} {sym} {b}$')
        out.append(f'sol ≈ {est} ## Round to the nearest whole numbers: {a} ≈ {ra}, {b} ≈ {rb}; {ra} {sym} {rb} = {est}. (Exact: {act}.) || قریب ترین مکمل اعداد تک مدور کریں: {a} ≈ {ra}، {b} ≈ {rb}؛ {ra} {sym} {rb} = {est}۔ (اصل جواب: {act}) || تر نږدې بشپړو عددونو پورې ګرد کړئ: {a} ≈ {ra}، {b} ≈ {rb}؛ {ra} {sym} {rb} = {est}. (اصلي ځواب: {act})')
out.append('endexercise')
open(r'D:\SpaceBook\SpaceBook Web\docs\source-verification\class-5\math\pages\p083.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
