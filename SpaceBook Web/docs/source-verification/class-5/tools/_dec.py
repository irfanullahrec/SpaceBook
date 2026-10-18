from decimal import Decimal as D
import sys
mode = sys.argv[1]
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    l, rest = line.split(' ', 1)
    if mode == 'cmp':
        a, b = rest.split()
        s = '>' if D(a) > D(b) else '<' if D(a) < D(b) else '='
        print(f'qp {l} | {a} \_\_\_ {b}')
        print(f'sol {a} {s} {b} ## Compare the digits from left to right (ones, then tenths, then hundredths); {a} {s} {b}. || ہندسوں کا بائیں سے دائیں موازنہ کریں (اکائی، پھر دسواں، پھر سواں)؛ {a} {s} {b}۔ || رقمونه له کیڼ څخه ښي لوري ته پرتله کړئ (یوونه، بیا لسمې، بیا سلمې)؛ {a} {s} {b}.')
    else:
        xs = [x.strip() for x in rest.split(',')]
        desc = mode == 'desc'
        ys = sorted(xs, key=D, reverse=desc)
        sym = ' > ' if desc else ' < '
        print(f'qp {l} | {", ".join(xs)}')
        en = 'Compare whole-number parts first, then tenths, then hundredths' + ('; write the greatest first.' if desc else '; write the smallest first.')
        ur = 'پہلے مکمل حصے، پھر دسویں اور پھر سوویں کا موازنہ کریں؛ ' + ('سب سے بڑا پہلے لکھیں۔' if desc else 'سب سے چھوٹا پہلے لکھیں۔')
        ps = 'لومړی بشپړې برخې، بیا لسمې او بیا سلمې پرتله کړئ؛ ' + ('تر ټولو لوی لومړی ولیکئ.' if desc else 'تر ټولو کوچنی لومړی ولیکئ.')
        print(f'sol {sym.join(ys)} ## {en} || {ur} || {ps}')
