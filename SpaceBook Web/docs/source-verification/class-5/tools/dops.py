"""Decimal arithmetic parts -> DSL qp + sol lines.

stdin lines: LETTER A OP B   (OP: + - x /)   e.g. 'a 4.131 + 8.3'
"""
import sys
from decimal import Decimal as D, getcontext

getcontext().prec = 28
SYM = {'+': '+', '-': '-', 'x': '\\times', '/': '\\div'}


def places(s):
    return len(s.split('.')[1]) if '.' in s else 0


def fmt(v):
    s = format(v.normalize(), 'f')
    return s


def main():
    for line in sys.stdin:
        p = line.split()
        if not p:
            continue
        l, a, op, b = p
        A, B = D(a), D(b)
        print(f'qp {l} | ${a} {SYM[op]} {b}$')
        if op in '+-':
            n = max(places(a), places(b))
            pa, pb = f'{A:.{n}f}', f'{B:.{n}f}'
            r = A + B if op == '+' else A - B
            rs = f'{r:.{n}f}'
            en = (f'Write both numbers with {n} decimal places ({pa} and {pb}), keep the decimal points in one column, then '
                  + ('add' if op == '+' else 'subtract') + ' as whole numbers.')
            ur = (f'دونوں اعداد کو {n} اعشاری مقامات کے ساتھ لکھیں ({pa} اور {pb})، اعشاریہ کے نقطے ایک کالم میں رکھیں، پھر مکمل اعداد کی طرح '
                  + ('جمع' if op == '+' else 'تفریق') + ' کریں۔')
            ps = (f'دواړه عددونه د {n} اعشاري ځایونو سره ولیکئ ({pa} او {pb})، اعشاري ټکي په یوه ستون کې کېږدئ، بیا یې د بشپړو عددونو په څېر '
                  + ('جمع' if op == '+' else 'تفریق') + ' کړئ.')
            print(f'sol {rs} ## {en} || {ur} || {ps}')
        elif op == 'x':
            r = A * B
            n = places(a) + places(b)
            print(f'sol {fmt(r)} ## Multiply as whole numbers, then count the decimal places in both numbers ({n}) and place the point. || اعشاریہ کے بغیر ضرب دیں، پھر دونوں اعداد کے اعشاری مقامات ({n}) گن کر نقطہ لگائیں۔ || د اعشاري ټکي پرته ضرب کړئ، بیا د دواړو عددونو اعشاري ځایونه ({n}) وشمېرئ او ټکی کېږدئ.')
        else:
            r = A / B
            print(f'sol {fmt(r)} ## Divide; keep the decimal point of the quotient above the decimal point of the dividend. || تقسیم کریں؛ خارجِ قسمت کا اعشاریہ مقسوم کے اعشاریہ کے اوپر رکھیں۔ || ووېشئ؛ د خارج قسمت اعشاري ټکی د وېشل کېدونکي د اعشاري ټکي پاس کېږدئ.')


if __name__ == '__main__':
    main()
