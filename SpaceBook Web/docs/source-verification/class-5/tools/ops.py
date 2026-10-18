"""Print `qp` + `sol` lines for plain arithmetic parts.

stdin lines:  LETTER A OP B      (OP one of + - x / ; numbers may contain commas)
              words LETTER N      (number in words)
Usage: python tools/ops.py < items.txt >> page.txt
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen5 import words

t = lambda n: f'{n:,}'.replace(',', '{,}')
SYM = {'+': '+', '-': '-', 'x': '\\times', '/': '\\div'}
EXPL = {
    '+': ('Add column by column from the ones, carrying when a column sum is 10 or more.',
          'اکائی سے شروع کر کے کالم وار جمع کریں؛ جب کسی کالم کا مجموعہ 10 یا زیادہ ہو تو حاصل آگے لے جائیں۔',
          'له یوونو څخه پیل کړئ او ستون په ستون جمع کړئ؛ کله چې د ستون مجموعه 10 یا ډېره وي، انتقال یې مخ ته یوسئ.'),
    '-': ('Subtract column by column from the ones, borrowing when the top digit is smaller.',
          'اکائی سے شروع کر کے کالم وار تفریق کریں؛ جب اوپر کا ہندسہ چھوٹا ہو تو ادھار لیں۔',
          'له یوونو څخه پیل کړئ او ستون په ستون تفریق کړئ؛ کله چې پورته رقم کوچنی وي، پور واخلئ.'),
    'x': ('Multiply by each digit of the second number, shift each partial product one place left, then add.',
          'دوسرے عدد کے ہر ہندسے سے ضرب دیں، ہر جزوی حاصلِ ضرب کو ایک مقام بائیں کھسکائیں، پھر جمع کریں۔',
          'د دوهم عدد په هر رقم کې ضرب کړئ، هر جزوي حاصل ضرب یو ځای کیڼ لوري ته وښوروئ، بیا یې جمع کړئ.'),
}


def main():
    for line in sys.stdin:
        p = line.split()
        if not p:
            continue
        if p[0] == 'words':
            n = int(p[2].replace(',', ''))
            w = words(n)
            print(f'qp {p[1]} | {n:,}')
            print(f'sol {w[0].upper() + w[1:]} ## Group the digits in periods from the right ({n:,}) and read each period with its name (million, thousand). || دائیں طرف سے ہندسوں کے گروپ بنائیں ({n:,}) اور ہر گروپ کو اس کے نام (ملین، ہزار) کے ساتھ پڑھیں۔ || له ښي لوري رقمونه په ډلو ووېشئ ({n:,}) او هره ډله د خپل نوم (ملیون، زر) سره ولولئ.')
            continue
        l, a, op, b = p
        a, b = int(a.replace(',', '')), int(b.replace(',', ''))
        print(f'qp {l} | ${t(a)} {SYM[op]} {t(b)}$')
        if op == '/':
            q, r = divmod(a, b)
            ans = f'{q:,}' + (f' r {r}' if r else '')
            print(f'sol {ans} ## Long division: {b:,} × {q:,} = {b*q:,}, and {a:,} − {b*q:,} = {r}. || لمبی تقسیم: {b:,} × {q:,} = {b*q:,} اور {a:,} − {b*q:,} = {r}۔ || اوږد وېش: {b:,} × {q:,} = {b*q:,} او {a:,} − {b*q:,} = {r}.')
        else:
            v = a + b if op == '+' else a - b if op == '-' else a * b
            e = EXPL[op]
            print(f'sol {v:,} ## {e[0]} || {e[1]} || {e[2]}')


if __name__ == '__main__':
    main()
