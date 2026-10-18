from decimal import Decimal as D
f = lambda x: format(D(x).normalize(), 'f')
out = ['@printed 161',
       'q 2 | Find the perimeter and area of the squares of the given lengths by using the formula. || فارمولے کی مدد سے دی گئی لمبائیوں والے مربعوں کا احاطہ اور رقبہ معلوم کریں۔ || د فورمول په مرسته د ورکړل شوو اوږدوالو مربعونو محیط او مساحت معلوم کړئ.']
for l, x in zip('abcdefgh', '8.2 cm|2.6 m|12.8 m|7.9 cm|16 cm|4.3 m|5.7 m|11 cm'.split('|')):
    v, u = x.split(); p = f(4 * D(v)); a = f(D(v) * D(v))
    out.append(f'qp {l} | {x}')
    out.append(rf'sol P = {p} {u}; A = ${a}\ \text{{{u}}}^2$ ## Perimeter = 4 × {v} = {p}; Area = {v} × {v} = {a}. || احاطہ = 4 × {v} = {p}؛ رقبہ = {v} × {v} = {a}۔ || محیط = 4 × {v} = {p}؛ مساحت = {v} × {v} = {a}.')
out.append('q 3 | Find the perimeter and area of the rectangles of the given lengths and widths by using the formula. || فارمولے کی مدد سے دی گئی لمبائیوں اور چوڑائیوں والے مستطیلوں کا احاطہ اور رقبہ معلوم کریں۔ || د فورمول په مرسته د ورکړل شوو اوږدوالو او پلنوالو مستطیلونو محیط او مساحت معلوم کړئ.')
for l, L, W, u in [('a', '6', '3.4', 'cm'), ('b', '1.2', '0.3', 'm'), ('c', '10', '13', 'cm'), ('d', '17', '8.5', 'cm')]:
    p = f(2 * (D(L) + D(W))); a = f(D(L) * D(W))
    out.append(f'qp {l} | L = {L} {u}, W = {W} {u}')
    out.append(rf'sol P = {p} {u}; A = ${a}\ \text{{{u}}}^2$ ## Perimeter = 2({L} + {W}) = {p}; Area = {L} × {W} = {a}. || احاطہ = 2({L} + {W}) = {p}؛ رقبہ = {L} × {W} = {a}۔ || محیط = 2({L} + {W}) = {p}؛ مساحت = {L} × {W} = {a}.')
out += ['@issue Review Q3 c) gives L = 10 cm and W = 13 cm (width larger than length); computed as printed.',
        "q 4 | The perimeter of a book is 100 cm. If it's width is 22 cm, find its length. || ایک کتاب کا احاطہ 100 cm ہے۔ اگر اس کی چوڑائی 22 cm ہو تو اس کی لمبائی معلوم کریں۔ || د یوه کتاب محیط 100 cm دی. که پلنوالی یې 22 cm وي، اوږدوالی یې معلوم کړئ.",
        'sol 28 cm ## 2(L + 22) = 100 → L + 22 = 50 → L = 28. || 2(L + 22) = 100 → L + 22 = 50 → L = 28۔ || 2(L + 22) = 100 → L + 22 = 50 → L = 28.',
        'q 5 | Laiba wants to tile for the floor of her kitchen. If the length of the kitchen is 12 metres and width is 10 metres then: || لائبہ اپنے باورچی خانے کے فرش پر ٹائل لگانا چاہتی ہے۔ اگر باورچی خانے کی لمبائی 12 میٹر اور چوڑائی 10 میٹر ہو تو: || لایبه غواړي د خپل پخلنځي پر فرش ټایل ولګوي. که د پخلنځي اوږدوالی 12 متره او پلنوالی 10 متره وي، نو:',
        'qp a | calculate the area of the kitchen. || باورچی خانے کا رقبہ معلوم کریں۔ || د پخلنځي مساحت حساب کړئ.',
        r'sol $120\ \text{m}^2$ ## 12 × 10 = 120. || 12 × 10 = 120۔ || 12 × 10 = 120.',
        'qp b | how many tiles will be required, if length of each square tile is 2 metres? || اگر ہر مربع ٹائل کی لمبائی 2 میٹر ہو تو کتنی ٹائلیں درکار ہوں گی؟ || که د هر مربع ټایل اوږدوالی 2 متره وي، څو ټایلونه به اړین وي؟',
        r'sol 30 tiles ## One tile = 2 × 2 = 4 m²; 120 ÷ 4 = 30. || ایک ٹائل = 2 × 2 = 4 m²؛ 120 ÷ 4 = 30۔ || یو ټایل = 2 × 2 = 4 m²؛ 120 ÷ 4 = 30.',
        'q 6 | The length of the fence around a square shaped garden is 24m. Find the length of the garden. || ایک مربع شکل کے باغیچے کے گرد باڑ کی لمبائی 24m ہے۔ باغیچے کی لمبائی معلوم کریں۔ || د یوه مربع شکله باغچې شاوخوا د کټارې اوږدوالی 24m دی. د باغچې اوږدوالی معلوم کړئ.',
        'sol 6 m ## Side = 24 ÷ 4 = 6. || ضلع = 24 ÷ 4 = 6۔ || ضلع = 24 ÷ 4 = 6.',
        'q 7 | Daniya took a 42 cm long ribbon and made a rectangle with it. If the length of the rectangle is 15 cm, then find its width. || دانیہ نے 42 cm لمبا ربن لیا اور اس سے ایک مستطیل بنایا۔ اگر مستطیل کی لمبائی 15 cm ہو تو اس کی چوڑائی معلوم کریں۔ || دانیې د 42 cm اوږده فیته واخیسته او یو مستطیل یې ترې جوړ کړ. که د مستطیل اوږدوالی 15 cm وي، پلنوالی یې معلوم کړئ.',
        'sol 6 cm ## 2(15 + W) = 42 → 15 + W = 21 → W = 6. || 2(15 + W) = 42 → 15 + W = 21 → W = 6۔ || 2(15 + W) = 42 → 15 + W = 21 → W = 6.',
        'q 8 | Find the area of the carromboard whose perimeter is 40 cm. || اس کیرم بورڈ کا رقبہ معلوم کریں جس کا احاطہ 40 cm ہے۔ || د هغه کیرم بورډ مساحت معلوم کړئ چې محیط یې 40 cm دی.',
        r'sol $100\ \text{cm}^2$ ## A carrom board is square: side = 40 ÷ 4 = 10 cm; area = 10 × 10 = 100. || کیرم بورڈ مربع ہوتا ہے: ضلع = 40 ÷ 4 = 10 cm؛ رقبہ = 10 × 10 = 100۔ || کیرم بورډ مربع وي: ضلع = 40 ÷ 4 = 10 cm؛ مساحت = 10 × 10 = 100.',
        '@issue Review Q8 does not say the carrom board is square; SpaceBook assumes a square board (as in real carrom boards). A perimeter of 40 cm is also very small for a real carrom board.',
        'endexercise']
open(r'D:\SpaceBook\SpaceBook Web\docs\source-verification\class-5\math\pages\p169.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
