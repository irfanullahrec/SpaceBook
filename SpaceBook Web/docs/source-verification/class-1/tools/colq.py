"""Print DSL blocks for column addition/subtraction questions (tens and ones).

    python colq.py START  "21+6, 33+2, 55-4"      -> q/eq/sol lines numbered from START
"""
import sys

UR = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')


def col(a, op, b):
    ta, oa = divmod(a, 10)
    tb, ob = divmod(b, 10)
    tb_s = str(tb) if tb else ''
    return r'eq \begin{array}{rcc} & \text{T} & \text{O} \\ & %d & %d \\ %s & %s & %d \\ \hline & & \end{array}' % (ta, oa, op, tb_s, ob)


def block(n, a, op, b):
    ta, oa = divmod(a, 10)
    tb, ob = divmod(b, 10)
    if op == '+':
        s, o, t = a + b, oa + ob, ta + tb
        en = f'Ones: {oa} + {ob} = {o}; tens: {ta} + {tb} = {t}. So {a} + {b} = {s}.'
        ur = f'اکائیاں: {oa} + {ob} = {o}؛ دہائیاں: {ta} + {tb} = {t}۔ لہٰذا {a} + {b} = {s}۔'
        ps = f'یووونه: {oa} + {ob} = {o}؛ لسیزې: {ta} + {tb} = {t}. نو {a} + {b} = {s}.'
    else:
        s, o, t = a - b, oa - ob, ta - tb
        en = f'Ones: {oa} − {ob} = {o}; tens: {ta} − {tb} = {t}. So {a} − {b} = {s}.'
        ur = f'اکائیاں: {oa} − {ob} = {o}؛ دہائیاں: {ta} − {tb} = {t}۔ لہٰذا {a} − {b} = {s}۔'
        ps = f'یووونه: {oa} − {ob} = {o}؛ لسیزې: {ta} − {tb} = {t}. نو {a} − {b} = {s}.'
    sym = '+' if op == '+' else '−'
    q = f'{a} {sym} {b}'
    return '\n'.join([f'q {n} | {q} || {q.translate(UR)} || {q.translate(UR)}', col(a, '+' if op == '+' else '-', b),
                      f'sol {s} ## {en} || {ur.translate(UR)} || {ps.translate(UR)}'])


def main():
    n = int(sys.argv[1])
    out = []
    for item in sys.argv[2].split(','):
        item = item.strip()
        op = '+' if '+' in item else '-'
        a, b = (int(x) for x in item.split(op))
        out.append(block(n, a, op, b))
        n += 1
    sys.stdout.reconfigure(encoding='utf-8')
    print('\n'.join(out))


if __name__ == '__main__':
    main()
