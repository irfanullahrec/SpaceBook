from decimal import Decimal as D
f = lambda x: format(D(x).normalize(), 'f')
out = ['@printed 154', '@deco Cartoon book mascot on "Exercise 1".', 'exercise 1',
       'q 1 | Find the perimeter of the given squares. || دیے گئے مربعوں کا احاطہ معلوم کریں۔ || د ورکړل شوو مربعونو محیط معلوم کړئ.']
for l, s, u, col in [('a', 7, 'm', '#fef08a'), ('b', 13, 'cm', '#6ee7b7'), ('c', 4, 'm', '#fb7185')]:
    out.append(f'poly _a:0,0 _b:3,0 _c:3,3 _d:0,3 | fill={col} | sides={s} {u},{s} {u},{s} {u},{s} {u} | ticks=1,1,1,1 | scale=32 || {l}) || {l}) || {l})')
    out.append(f'qp {l} | Square {l}) || مربع {l}) || مربع {l})')
    out.append(f'sol {4 * s} {u} ## Perimeter = 4 × {s} {u} = {4 * s} {u}. || احاطہ = 4 × {s} {u} = {4 * s} {u}۔ || محیط = 4 × {s} {u} = {4 * s} {u}.')
out.append('q 2 | Find the perimeter of the given rectangles. || دیے گئے مستطیلوں کا احاطہ معلوم کریں۔ || د ورکړل شوو مستطیلونو محیط معلوم کړئ.')
for l, L, W, u, pts, col in [('a', 9, 5, 'cm', '0,0 _b:4,0 _c:4,2.2 _d:0,2.2', '#fef08a'), ('b', 8, 3, 'm', '0,0 _b:1.3,0 _c:1.3,3.5 _d:0,3.5', '#6ee7b7'), ('c', 12, 2, 'm', '0,0 _b:4.5,0 _c:4.5,0.75 _d:0,0.75', '#7dd3fc')]:
    if l == 'b':
        sides = f'{W} {u},{L} {u},{W} {u},{L} {u}'
    else:
        sides = f'{L} {u},{W} {u},{L} {u},{W} {u}'
    out.append(f'poly _a:{pts} | fill={col} | sides={sides} | ticks=1,2,1,2 | scale=32 || {l}) || {l}) || {l})')
    out.append(f'qp {l} | Rectangle {l}) || مستطیل {l}) || مستطیل {l})')
    out.append(f'sol {2 * (L + W)} {u} ## Perimeter = 2(L + W) = 2({L} + {W}) = 2({L + W}) = {2 * (L + W)} {u}. || احاطہ = 2(L + W) = 2({L} + {W}) = {2 * (L + W)} {u}۔ || محیط = 2(L + W) = 2({L} + {W}) = {2 * (L + W)} {u}.')
out += ['q 3 | If the length of a square shaped crop field is 29 metres, what will be its perimeter? || اگر مربع شکل کے فصل والے کھیت کی لمبائی 29 میٹر ہو تو اس کا احاطہ کیا ہوگا؟ || که د مربع شکله کښتې ځمکې اوږدوالی 29 متره وي، محیط به یې څومره وي؟',
        'sol 116 m ## 4 × 29 = 116. || 4 × 29 = 116۔ || 4 × 29 = 116.',
        'q 4 | The perimeter of a square shape is 72 cm. What will be its length? || ایک مربع شکل کا احاطہ 72 cm ہے۔ اس کی لمبائی کیا ہوگی؟ || د یوه مربع شکل محیط 72 cm دی. اوږدوالی به یې څومره وي؟',
        'poly _a:0,0 _b:3,0 _c:3,3 _d:0,3 | fill=#e879f9 | ticks=1,1,1,1 | scale=32 || Square with perimeter = 72 cm || مربع جس کا احاطہ = 72 cm || مربع چې محیط یې = 72 cm',
        'sol 18 cm ## Side = perimeter ÷ 4 = 72 ÷ 4 = 18. || ضلع = احاطہ ÷ 4 = 72 ÷ 4 = 18۔ || ضلع = محیط ÷ 4 = 72 ÷ 4 = 18.',
        'q 5 | Find the perimeter of the squares of given lengths by using formula. || فارمولے کی مدد سے دی گئی لمبائیوں والے مربعوں کا احاطہ معلوم کریں۔ || د فورمول په مرسته د ورکړل شوو اوږدوالو مربعونو محیط معلوم کړئ.']
for l, x in zip('abcdefghijkl', '5 cm|12 cm|6 m|19 cm|26 m|2.5 cm|9.7 m|15 m|16.6 cm|10 m|7.1 cm|2.7 cm'.split('|')):
    v, u = x.split()
    p = f(D(v) * 4)
    out.append(f'qp {l} | {x}')
    out.append(f'sol {p} {u} ## 4 × {v} = {p}. || 4 × {v} = {p}۔ || 4 × {v} = {p}.')
out.append('q 6 | Find the perimeter of the rectangles of the given lengths and widths by using formula. || فارمولے کی مدد سے دی گئی لمبائیوں اور چوڑائیوں والے مستطیلوں کا احاطہ معلوم کریں۔ || د فورمول په مرسته د ورکړل شوو اوږدوالو او پلنوالو مستطیلونو محیط معلوم کړئ.')
for l, L, W, u in [('a', '3', '2', 'cm'), ('b', '5.3', '2.2', 'm'), ('c', '6', '4', 'cm'), ('d', '9', '1.2', 'm'), ('e', '10', '5.9', 'm'), ('f', '15', '12', 'cm')]:
    s = f(D(L) + D(W)); p = f(2 * (D(L) + D(W)))
    out.append(f'qp {l} | L = {L} {u}, W = {W} {u}')
    out.append(f'sol {p} {u} ## 2(L + W) = 2({L} + {W}) = 2({s}) = {p}. || 2(L + W) = 2({L} + {W}) = 2({s}) = {p}۔ || 2(L + W) = 2({L} + {W}) = 2({s}) = {p}.')
out.append('@issue Q6 d) prints "W= 1. 2 m" with a space inside the decimal; read as 1.2 m.')
open(r'D:\SpaceBook\SpaceBook Web\docs\source-verification\class-5\math\pages\p162.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
