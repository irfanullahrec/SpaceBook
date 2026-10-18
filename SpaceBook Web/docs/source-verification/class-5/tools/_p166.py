from decimal import Decimal as D
f = lambda x: format(D(x).normalize(), 'f')
sq = lambda u: r'\text{' + u + r'}^2'
out = ['@printed 158', '@deco Cartoon book mascot on "Exercise 2".', 'exercise 2',
       'q 1 | Find the area of the given squares. || دیے گئے مربعوں کا رقبہ معلوم کریں۔ || د ورکړل شوو مربعونو مساحت معلوم کړئ.']
for l, s, u, col in [('a', '2.5', 'm', '#fef08a'), ('b', '22', 'cm', '#14b8a6'), ('c', '42.7', 'm', '#fb7185')]:
    a = f(D(s) * D(s))
    out.append(f'poly _a:0,0 _b:3,0 _c:3,3 _d:0,3 | fill={col} | sides={s} {u},{s} {u},{s} {u},{s} {u} | ticks=1,1,1,1 | scale=32 || {l}) || {l}) || {l})')
    out.append(f'qp {l} | Square {l}) || مربع {l}) || مربع {l})')
    out.append(f'sol ${a}\\ {sq(u)}$ ## Area = L × L = {s} × {s} = {a}. || رقبہ = L × L = {s} × {s} = {a}۔ || مساحت = L × L = {s} × {s} = {a}.')
out.append('q 2 | Find the area of the given rectangles. || دیے گئے مستطیلوں کا رقبہ معلوم کریں۔ || د ورکړل شوو مستطیلونو مساحت معلوم کړئ.')
for l, L, W, u, pts, sides, col in [('a', '4.5', '3', 'cm', '_b:4.5,0 _c:4.5,2 _d:0,2', '4.5 cm,3 cm,4.5 cm,3 cm', '#22d3ee'),
                                    ('b', '6', '2', 'm', '_b:1.6,0 _c:1.6,4 _d:0,4', '2 m,6 m,2 m,6 m', '#ec4899'),
                                    ('c', '10', '1', 'm', '_b:4.6,0 _c:4.6,0.6 _d:0,0.6', '10 m,1 m,10 m,1 m', '#f0abfc')]:
    a = f(D(L) * D(W))
    out.append(f'poly _a:0,0 {pts} | fill={col} | sides={sides} | ticks=2,1,2,1 | scale=34 || {l}) || {l}) || {l})')
    out.append(f'qp {l} | Rectangle {l}) || مستطیل {l}) || مستطیل {l})')
    out.append(f'sol ${a}\\ {sq(u)}$ ## Area = L × W = {L} × {W} = {a}. || رقبہ = L × W = {L} × {W} = {a}۔ || مساحت = L × W = {L} × {W} = {a}.')
out += [r'q 3 | The area of a rectangle is $96\text{m}^2$. If its width is 3m, find its length? || ایک مستطیل کا رقبہ $96\text{m}^2$ ہے۔ اگر اس کی چوڑائی 3m ہو تو اس کی لمبائی معلوم کریں۔ || د یوه مستطیل مساحت $96\text{m}^2$ دی. که پلنوالی یې 3m وي، اوږدوالی یې معلوم کړئ.',
        'sol 32 m ## L = Area ÷ W = 96 ÷ 3 = 32. || L = رقبہ ÷ W = 96 ÷ 3 = 32۔ || L = مساحت ÷ W = 96 ÷ 3 = 32.',
        'q 4 | Find the area of the squares of the given lengths by using formula. || فارمولے کی مدد سے دی گئی لمبائیوں والے مربعوں کا رقبہ معلوم کریں۔ || د فورمول په مرسته د ورکړل شوو اوږدوالو مربعونو مساحت معلوم کړئ.']
for l, x in zip('abcdefghijkl', '4.5 m|9.3 cm|8.8 m|15 cm|13 cm|3 m|6 m|2.9 m|5 cm|9.2 m|14 m|1.1 cm'.split('|')):
    v, u = x.split(); a = f(D(v) * D(v))
    out.append(f'qp {l} | {x}')
    out.append(f'sol ${a}\\ {sq(u)}$ ## {v} × {v} = {a}. || {v} × {v} = {a}۔ || {v} × {v} = {a}.')
out.append('q 5 | Find the area of the rectangles of the given lengths and widths by using formula. || فارمولے کی مدد سے دی گئی لمبائیوں اور چوڑائیوں والے مستطیلوں کا رقبہ معلوم کریں۔ || د فورمول په مرسته د ورکړل شوو اوږدوالو او پلنوالو مستطیلونو مساحت معلوم کړئ.')
for l, L, W, u in [('a', '5', '1.9', 'cm'), ('b', '4', '3', 'm'), ('c', '6', '4', 'cm'), ('d', '7', '5', 'cm'), ('e', '10.5', '9', 'cm'), ('f', '20', '17', 'm')]:
    a = f(D(L) * D(W))
    out.append(f'qp {l} | L = {L} {u}, W = {W} {u}')
    out.append(f'sol ${a}\\ {sq(u)}$ ## {L} × {W} = {a}. || {L} × {W} = {a}۔ || {L} × {W} = {a}.')
out += ['q 6 | A rectangular shaped ground has a length of 122m and width 108m. Find the area of the ground. || ایک مستطیل شکل کے میدان کی لمبائی 122m اور چوڑائی 108m ہے۔ میدان کا رقبہ معلوم کریں۔ || د یوه مستطیل شکله میدان اوږدوالی 122m او پلنوالی 108m دی. د میدان مساحت معلوم کړئ.',
        r'sol $13{,}176\ \text{m}^2$ ## 122 × 108 = 13,176. || 122 × 108 = 13,176۔ || 122 × 108 = 13,176.']
open(r'D:\SpaceBook\SpaceBook Web\docs\source-verification\class-5\math\pages\p166.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
