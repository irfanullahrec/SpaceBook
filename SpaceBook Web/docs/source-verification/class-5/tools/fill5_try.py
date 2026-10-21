"""Answers for the Class 5 Maths "Try yourself" / unkeyed parts that were still without a `sol` line.

    python fill5_try.py [--write]

Every value is computed here (conversions, differences, sequences, comparisons, percentages). Parts are located by
page file + part label + the start of the part text, so nothing is guessed from position. Drawing tasks, the
"estimate" items and the days-to-months conversion (the book's month length is not stated) are left open on purpose.
"""
import re, sys
from pathlib import Path
from fractions import Fraction

PAGES = Path(__file__).resolve().parents[1] / 'math' / 'pages'


def f(n):
    return f'{n:,}'


def dec(x):
    s = f'{float(x):.6f}'.rstrip('0').rstrip('.')
    return s


def S(en, ur, ps):
    return en, ur, ps


ITEMS = []      # (file, label, text prefix, answer, (en, ur, ps))


def add(file, label, prefix, ans, steps):
    ITEMS.append((file, label, prefix, ans, steps))


# ---- p017: 1,000 x 100 x 10
add('p017', 'b', '$1{,}000 \\times 100 \\times 10', f(1000 * 100 * 10),
    S('Multiply step by step: 1,000 × 100 = 100,000 and 100,000 × 10 = 1,000,000.',
      'قدم بہ قدم ضرب دیں: 1,000 × 100 = 100,000 اور 100,000 × 10 = 1,000,000۔',
      'ګام په ګام ضرب کړئ: 1,000 × 100 = 100,000 او 100,000 × 10 = 1,000,000.'))

# ---- p013: trees
add('p013', 'a', 'In which month more trees', 'March (554,876 trees)',
    S('Compare 554,876 and 263,755: 554,876 is greater, so more trees were planted in March.',
      '554,876 اور 263,755 کا موازنہ کریں: 554,876 بڑا ہے، اس لیے مارچ میں زیادہ درخت لگائے گئے۔',
      '554,876 او 263,755 پرتله کړئ: 554,876 لوی دی، نو په مارچ کې ډېر ونې کېښودل شوې.'))
add('p013', 'b', 'How many more trees', f(554876 - 263755),
    S('Subtract: 554,876 − 263,755 = 291,121.',
      'تفریق کریں: 554,876 − 263,755 = 291,121۔',
      'تفریق کړئ: 554,876 − 263,755 = 291,121.'))

# ---- p022: groups of 95
q, r = divmod(10125, 95)
add('p022', 'a', 'How many groups can be made', f'{q} groups',
    S(f'Divide: 10,125 ÷ 95 = {q} with remainder {r}, so {q} full groups can be made.',
      f'تقسیم کریں: 10,125 ÷ 95 = {q} باقی {r}، اس لیے {q} پورے گروہ بن سکتے ہیں۔',
      f'ووېشئ: 10,125 ÷ 95 = {q} پاتې {r}، نو {q} بشپړې ډلې جوړېدای شي.'))
add('p022', 'b', 'Find the number of un-grouped', f'{r} students',
    S(f'The remainder of the division is {r}, so {r} students are left without a group.',
      f'تقسیم کا باقی {r} ہے، اس لیے {r} طلبہ کسی گروہ کے بغیر رہ جاتے ہیں۔',
      f'د وېش پاتې {r} دی، نو {r} زده کوونکي له ډلې پرته پاتې کېږي.'))
q2, r2 = divmod(10125 - 720, 95)
add('p022', 'c', 'If 720 students cannot participate', f'{q2} groups' + (f' and {r2} students left' if r2 else ''),
    S(f'Students left: 10,125 − 720 = {f(10125 - 720)}. Divide: {f(10125 - 720)} ÷ 95 = {q2}' + (f' remainder {r2}.' if r2 else ' exactly.'),
      f'باقی طلبہ: 10,125 − 720 = {f(10125 - 720)}۔ تقسیم کریں: {f(10125 - 720)} ÷ 95 = {q2}' + (f' باقی {r2}۔' if r2 else ' پورا۔'),
      f'پاتې زده کوونکي: 10,125 − 720 = {f(10125 - 720)}. ووېشئ: {f(10125 - 720)} ÷ 95 = {q2}' + (f' پاتې {r2}.' if r2 else ' بشپړ.')))

# ---- p029: sequences
add('p029', 'a', '3, 6, 12, 24', '48, 96, 192',
    S('Each term is double the one before (× 2): 24 × 2 = 48, 48 × 2 = 96, 96 × 2 = 192.',
      'ہر رقم پچھلی رقم کا دوگنا ہے (× 2): 24 × 2 = 48، 48 × 2 = 96، 96 × 2 = 192۔',
      'هر رقم د مخکینۍ دوه برابره ده (× 2): 24 × 2 = 48، 48 × 2 = 96، 96 × 2 = 192.'))
add('p029', 'b', '5, 7, 10, 14', '19, 25, 32',
    S('The differences grow by 1 each time: +2, +3, +4, so next +5, +6, +7: 14 + 5 = 19, 19 + 6 = 25, 25 + 7 = 32.',
      'فرق ہر بار 1 بڑھتا ہے: +2، +3، +4، اس لیے اگلے +5، +6، +7: 14 + 5 = 19، 19 + 6 = 25، 25 + 7 = 32۔',
      'توپیر هر ځل 1 زیاتیږي: +2، +3، +4، نو بل +5، +6، +7: 14 + 5 = 19، 19 + 6 = 25، 25 + 7 = 32.'))
add('p029', 'c', '100, 96, 92', '80, 76, 72',
    S('Subtract 4 each time: 84 − 4 = 80, 80 − 4 = 76, 76 − 4 = 72.',
      'ہر بار 4 گھٹائیں: 84 − 4 = 80، 80 − 4 = 76، 76 − 4 = 72۔',
      'هر ځل 4 کم کړئ: 84 − 4 = 80، 80 − 4 = 76، 76 − 4 = 72.'))
add('p029', 'd', '8, 80, 800', '80,000; 800,000; 8,000,000',
    S('Multiply by 10 each time: 8,000 × 10 = 80,000, then 800,000, then 8,000,000.',
      'ہر بار 10 سے ضرب دیں: 8,000 × 10 = 80,000، پھر 800,000، پھر 8,000,000۔',
      'هر ځل په 10 کې ضرب کړئ: 8,000 × 10 = 80,000، بیا 800,000، بیا 8,000,000.'))
add('p029', 'e', '900,000, 90,000', '900; 90; 9',
    S('Divide by 10 each time: 9,000 ÷ 10 = 900, 900 ÷ 10 = 90, 90 ÷ 10 = 9.',
      'ہر بار 10 سے تقسیم کریں: 9,000 ÷ 10 = 900، 900 ÷ 10 = 90، 90 ÷ 10 = 9۔',
      'هر ځل په 10 ووېشئ: 9,000 ÷ 10 = 900، 900 ÷ 10 = 90، 90 ÷ 10 = 9.'))

# ---- p064: compare decimals
for lab, a, b in (('i', '0.30', '0.3'), ('ii', '1.02', '1.22'), ('iii', '1.31', '1.3'), ('iv', '5.13', '5.03')):
    fa, fb = Fraction(a), Fraction(b)
    sym = '=' if fa == fb else ('>' if fa > fb else '<')
    word = {'=': ('equal to', 'کے برابر ہے', 'سره مساوي دی'), '>': ('greater than', 'سے بڑا ہے', 'له ... لوی دی'),
            '<': ('less than', 'سے چھوٹا ہے', 'له ... کوچنی دی')}[sym]
    add('p064', lab, f'{a} ', sym,
        S(f'Make the decimal places equal and compare digit by digit: {a} is {word[0]} {b}, so {a} {sym} {b}.',
          f'اعشاریہ مقامات برابر کریں اور ہندسہ بہ ہندسہ موازنہ کریں: {a} {b} {word[1]}، اس لیے {a} {sym} {b}۔',
          f'اعشاریه ځایونه برابر کړئ او رقم په رقم پرتله کړئ: {a} او {b}: {a} {sym} {b}.'))

# ---- p085: percentages
for lab, txt, pct, n in (('a', 'One half', '50%', '1/2 = 50/100'), ('b', 'One tenth', '10%', '1/10 = 10/100'), ('c', 'One Hundredth', '1%', '1/100')):
    add('p085', lab, txt, pct,
        S(f'Write the fraction with denominator 100: {n}, so it is {pct}.',
          f'کسر کو نسب نما 100 کے ساتھ لکھیں: {n}، یعنی {pct}۔',
          f'کسر د 100 مخرج سره ولیکئ: {n}، یعنې {pct}.'))

# ---- p087: 20% of an amount is 350
one = Fraction(350, 20)
for lab, txt, mult in (('A', '1% of the amount', 1), ('B', '100 % of the amount', 100), ('C', '1,000 % of the amount', 1000)):
    val = one * mult
    add('p087', lab, txt, f'Rs. {dec(val)}',
        S(f'20% = 350, so 1% = 350 ÷ 20 = {dec(one)}; {mult}% = {dec(one)} × {mult} = {dec(val)}.',
          f'20% = 350، اس لیے 1% = 350 ÷ 20 = {dec(one)}؛ {mult}% = {dec(one)} × {mult} = {dec(val)}۔',
          f'20% = 350، نو 1% = 350 ÷ 20 = {dec(one)}؛ {mult}% = {dec(one)} × {mult} = {dec(val)}.'))

# ---- p094: metres to kilometres
for lab, m in (('i', 5000), ('ii', 2002), ('iii', 8976)):
    km = Fraction(m, 1000)
    add('p094', lab, f'{f(m)} m', f'{dec(km)} km',
        S(f'Divide by 1,000: {f(m)} ÷ 1,000 = {dec(km)} km (that is {m // 1000} km {m % 1000} m).',
          f'1,000 سے تقسیم کریں: {f(m)} ÷ 1,000 = {dec(km)} کلومیٹر (یعنی {m // 1000} کلومیٹر {m % 1000} میٹر)۔',
          f'په 1,000 ووېشئ: {f(m)} ÷ 1,000 = {dec(km)} کیلومتر (یعنې {m // 1000} کیلومتر {m % 1000} متره).'))

# ---- p096: centimetres to metres
for lab, cm in (('i', 670), ('ii', 409), ('iii', 900)):
    add('p096', lab, f'{cm} cm', f'{dec(Fraction(cm, 100))} m',
        S(f'Divide by 100: {cm} ÷ 100 = {dec(Fraction(cm, 100))} m (that is {cm // 100} m {cm % 100} cm).',
          f'100 سے تقسیم کریں: {cm} ÷ 100 = {dec(Fraction(cm, 100))} میٹر (یعنی {cm // 100} میٹر {cm % 100} سینٹی میٹر)۔',
          f'په 100 ووېشئ: {cm} ÷ 100 = {dec(Fraction(cm, 100))} متره (یعنې {cm // 100} متره {cm % 100} سانتي متره).'))

# ---- p098: millimetres to metres
for lab, mm in (('i', 20), ('ii', 78), ('iii', 98)):
    add('p098', lab, f'{mm} mm', f'{dec(Fraction(mm, 1000))} m',
        S(f'Divide by 1,000: {mm} ÷ 1,000 = {dec(Fraction(mm, 1000))} m.',
          f'1,000 سے تقسیم کریں: {mm} ÷ 1,000 = {dec(Fraction(mm, 1000))} میٹر۔',
          f'په 1,000 ووېشئ: {mm} ÷ 1,000 = {dec(Fraction(mm, 1000))} متره.'))

# ---- p101: subtract distances
add('p101', 'i', '670 m', '220 m',
    S('Subtract: 670 − 450 = 220, so the answer is 220 m.', 'تفریق کریں: 670 − 450 = 220، جواب 220 میٹر ہے۔', 'تفریق کړئ: 670 − 450 = 220، ځواب 220 متره دی.'))
d = (83 * 1000 + 219) - (51 * 1000 + 340)
add('p101', 'ii', '83 km 219 m', f'{d // 1000} km {d % 1000} m',
    S(f'Change to metres: 83,219 − 51,340 = {f(d)} m = {d // 1000} km {d % 1000} m.',
      f'میٹر میں بدلیں: 83,219 − 51,340 = {f(d)} میٹر = {d // 1000} کلومیٹر {d % 1000} میٹر۔',
      f'په مترو واړوئ: 83,219 − 51,340 = {f(d)} متره = {d // 1000} کیلومتر {d % 1000} متره.'))
d = (32 * 10 + 3) - (9 * 10 + 4)
add('p101', 'iii', '32 cm 3 mm', f'{d // 10} cm {d % 10} mm',
    S(f'Change to millimetres: 323 − 94 = {d} mm = {d // 10} cm {d % 10} mm.',
      f'ملی میٹر میں بدلیں: 323 − 94 = {d} ملی میٹر = {d // 10} سینٹی میٹر {d % 10} ملی میٹر۔',
      f'په ملی مترو واړوئ: 323 − 94 = {d} ملي متره = {d // 10} سانتي متره {d % 10} ملي متره.'))

# ---- p104: minutes to hours
for lab, mn in (('i', 380), ('ii', 720), ('iii', 440)):
    h, r = divmod(mn, 60)
    add('p104', lab, f'{mn} min', f'{h} h' + (f' {r} min' if r else ''),
        S(f'Divide by 60: {mn} ÷ 60 = {h}' + (f' remainder {r}, so {h} hours {r} minutes.' if r else ' hours.'),
          f'60 سے تقسیم کریں: {mn} ÷ 60 = {h}' + (f' باقی {r}، یعنی {h} گھنٹے {r} منٹ۔' if r else ' گھنٹے۔'),
          f'په 60 ووېشئ: {mn} ÷ 60 = {h}' + (f' پاتې {r}، یعنې {h} ساعتونه {r} دقیقې.' if r else ' ساعتونه.')))

# ---- p105: minutes to seconds
for lab, mn in (('i', 220), ('ii', 540), ('iii', 720)):
    add('p105', lab, f'{mn} min', f'{f(mn * 60)} s',
        S(f'Multiply by 60: {mn} × 60 = {f(mn * 60)} seconds.',
          f'60 سے ضرب دیں: {mn} × 60 = {f(mn * 60)} سیکنڈ۔',
          f'په 60 کې ضرب کړئ: {mn} × 60 = {f(mn * 60)} ثانیې.'))

# ---- p009: K-2 height 861,100 cm
add('p009', 'a', 'Write the height in expanded', '800,000 + 60,000 + 1,000 + 100',
    S('Split 861,100 by place value: 800,000 + 60,000 + 1,000 + 100.', '861,100 کو مقامی قیمت کے مطابق توڑیں: 800,000 + 60,000 + 1,000 + 100۔', '861,100 د ځایي ارزښت له مخې ووېشئ: 800,000 + 60,000 + 1,000 + 100.'))
add('p009', 'b', 'Write the place value of each digit', '8 = 800,000; 6 = 60,000; 1 = 1,000; 1 = 100; 0 = 0; 0 = 0',
    S('Read each digit with its place: 8 hundred thousands, 6 ten thousands, 1 thousand, 1 hundred, 0 tens, 0 ones.',
      'ہر ہندسے کو اس کے مقام کے ساتھ پڑھیں: 8 لاکھ، 6 دس ہزار، 1 ہزار، 1 سینکڑہ، 0 دہائی، 0 اکائی۔',
      'هر رقم د خپل ځای سره ولولئ: 8 سوه زره، 6 لس زره، 1 زر، 1 سلګونه، 0 لسګونه، 0 یوونه.'))
add('p009', 'c', 'Write the height in words', 'Eight hundred and sixty-one thousand, one hundred',
    S('Read 861 thousand and 100: eight hundred and sixty-one thousand, one hundred.', '861 ہزار اور 100 پڑھیں: آٹھ سو اکسٹھ ہزار، ایک سو۔', '861 زره او 100 ولولئ: اته سوه یو شپېته زره، یو سل.'))


def main():
    write = '--write' in sys.argv
    done = 0
    for file in sorted({i[0] for i in ITEMS}):
        path = PAGES / f'{file}.txt'
        lines = path.read_text(encoding='utf8').split('\n')
        out, changed = [], False
        for k, line in enumerate(lines):
            out.append(line)
            m = re.match(r'^qp\s+(\S+)\s*\|\s*(.*)$', line)
            if not m:
                continue
            nxt = lines[k + 1] if k + 1 < len(lines) else ''
            if re.match(r'^(sol|solution)\b', nxt):
                continue
            txt = m.group(2).split(' || ')[0]
            for it in ITEMS:
                if it[0] == file and it[1] == m.group(1) and txt.startswith(it[2]):
                    en, ur, ps = it[4]
                    out.append(f'sol {it[3]} ## {en} || {ur} || {ps}')
                    done += 1
                    changed = True
                    ITEMS.remove(it)
                    break
        if write and changed:
            with open(path, 'w', encoding='utf8', newline='\n') as fh:
                fh.write('\n'.join(out))
    print(f'{"written" if write else "found"}: {done}; not placed: {len(ITEMS)}')
    for it in ITEMS:
        print('  not placed', it[0], it[1], it[2])


if __name__ == '__main__':
    main()
