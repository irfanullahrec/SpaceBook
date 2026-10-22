"""Class 8 Maths: items whose data was read from the scans (D:/SpaceBook/Books/8th/8th MAths/JPG) in 2026-10-22:
6.1 Q5 (dot patterns), 6.2 Q8, 6.3 Q4-6, 6.8 Q1 viii, 9.1 Q9, 9.2 Q6, Review 9 Q9 (spheres; figure labels 5 m, 18 m, d = 20 m),
10.1 Q1-2 (worked examples), and key-driven statements for the figure items 10.1 Q4, 10.3 Q1-2, 10.9 Q2, Review 10 Q16.
Writes class-8/math/dsl/u8w.txt."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / 'math' / 'dsl' / 'u8w.txt'
L = []


def N(en, ur, ps):
    return f'{en}|{ur}|{ps}'


def add(key, rows, ans, note=None):
    s = f'{key} ~ ' + ' ;; '.join(rows)
    if note:
        s += ' @@ ' + note
    L.append(s + f' => {ans} %%')


def text(key, en, ur, ps, ans):
    L.append(f'{key} ~ @text {en}|{ur}|{ps} => {ans} %%')


# ---- 6.1 Q5 dot patterns
add('6.1|5|', [r'\text{(i) squares of dots: } 4, 9, 16, 25, 36, 49, 64 \quad (a_n = (n + 1)^2)', r'a_7 = (7 + 1)^2 = 8^2 = 64',
               r'\text{(ii) rectangles of dots: } 6, 12, 20, 30, 42, 56, 72 \quad (a_n = (n + 1)(n + 2))', r'a_7 = (7 + 1)(7 + 2) = 8 \times 9 = 72'],
    '(i) a₇ = 64; (ii) a₇ = 72',
    N('The first term of (i) is read as 4 (a 2 × 2 square); the printed key lists 3 but gives the same seventh term, 64.',
      '(i) کا پہلا رکن 4 (2 × 2 مربع) پڑھا گیا ہے؛ چھپی کلید 3 لکھتی ہے مگر ساتواں رکن وہی 64 دیتی ہے۔',
      'د (i) لومړی رکن 4 (2 × 2 مربع) لوستل شوی؛ چاپ شوې کلیل 3 لیکي خو اووم رکن همدا 64 ورکوي.'))
# ---- 6.2 Q8
add('6.2|8|', [r'\text{Width at the start} = 15,\; d = 15 \quad (a_1 = 15)', r'\text{After 7 km is the 8th term: } a_8 = 15 + 7 \times 15 = 120'], '120 m',
    N('The question does not give the width at the start; the printed key (120 m) is matched by taking the first width as 15 m.',
      'سوال میں شروع کی چوڑائی نہیں دی گئی؛ چھپی کلید (120 m) پہلی چوڑائی 15 m لینے سے ملتی ہے۔',
      'پوښتنه د پیل پلنوالی نه ورکوي؛ چاپ شوې کلیل (120 m) هغه مهال سمیږي چې لومړی پلنوالی 15 m ونیول شي.'))
# ---- 6.3 Q4-6 (polynomial list of question 3 on the page)
POLY = ('Polynomials of Question 3 (read from the scan): i) 5x−2; ii) 3x²−15; iii) x²+y²+2xy; iv) y²−xz; v) (2/3)x³−(4/7)y²+28yz; vi) 5x⁴+6x³+2x²−11x+16; '
        'vii) x⁴−y⁴; viii) 2a+3b+4c−5d; ix) v²−u²+2gs; x) m⁴−n⁴+4np; xi) x³−6x⁴−16; xii) 7.12x+3.2y+1.5z; xiii) √2+½y²−yz; xiv) x³+y³; xv) 2x³+4x²−5x+3; xvi) x⁴+15x²−16.')
text('6.3|4|', POLY + ' Quadratic means degree 2; in one variable only ii) 3x² − 15 qualifies (iii, iv, ix, xiii have more than one variable; vi, x, xi, xvi have degree 4).',
     'سوال 3 کے کثیر رقمی (اسکین سے): i) 5x−2؛ ii) 3x²−15؛ iii) x²+y²+2xy؛ iv) y²−xz؛ v) (2/3)x³−(4/7)y²+28yz؛ vi) 5x⁴+6x³+2x²−11x+16؛ vii) x⁴−y⁴؛ viii) 2a+3b+4c−5d؛ ix) v²−u²+2gs؛ x) m⁴−n⁴+4np؛ xi) x³−6x⁴−16؛ xii) 7.12x+3.2y+1.5z؛ xiii) √2+½y²−yz؛ xiv) x³+y³؛ xv) 2x³+4x²−5x+3؛ xvi) x⁴+15x²−16۔ دو درجے کا مطلب درجہ 2؛ ایک متغیر میں صرف ii) 3x² − 15 ہے۔',
     'د پوښتنې 3 کثیر الحدي (له سکین څخه): i) 5x−2؛ ii) 3x²−15؛ iii) x²+y²+2xy؛ iv) y²−xz؛ v) (2/3)x³−(4/7)y²+28yz؛ vi) 5x⁴+6x³+2x²−11x+16؛ vii) x⁴−y⁴؛ viii) 2a+3b+4c−5d؛ ix) v²−u²+2gs؛ x) m⁴−n⁴+4np؛ xi) x³−6x⁴−16؛ xii) 7.12x+3.2y+1.5z؛ xiii) √2+½y²−yz؛ xiv) x³+y³؛ xv) 2x³+4x²−5x+3؛ xvi) x⁴+15x²−16. څلورڅخنی یعنې درجه 2؛ په یو متغیر کې یوازې ii) 3x² − 15 دی.', 'ii')
text('6.3|5|', 'Quadratic (degree 2) polynomials with more than one variable: iii) x²+y²+2xy, iv) y²−xz, ix) v²−u²+2gs and xiii) √2+½y²−yz. With exactly two variables: iii) and xiii). The printed key lists iii, iv, ix.',
     'ایک سے زیادہ متغیرات والے دو درجے (کوآڈریٹک) کثیر رقمی: iii) x²+y²+2xy، iv) y²−xz، ix) v²−u²+2gs اور xiii) √2+½y²−yz۔ بالکل دو متغیرات والے: iii) اور xiii)۔ چھپی کلید iii, iv, ix دیتی ہے۔',
     'له یو ډېرو متغیرونو سره دوه درجه (کواډراټیک) کثیر الحدي: iii) x²+y²+2xy، iv) y²−xz، ix) v²−u²+2gs او xiii) √2+½y²−yz. دقیقاً دوه متغیره: iii) او xiii). چاپ شوې کلیل iii, iv, ix لیکي.', 'iii, iv, ix (exactly two variables: iii, xiii)')
text('6.3|6|', 'Cubic (degree 3) polynomials: v) (2/3)x³−(4/7)y²+28yz, xiv) x³+y³ and xv) 2x³+4x²−5x+3. Those in more than one variable: v) and xiv). The printed key lists only xiv).',
     'تین درجے (کیوبک) کثیر رقمی: v) (2/3)x³−(4/7)y²+28yz، xiv) x³+y³ اور xv) 2x³+4x²−5x+3۔ ایک سے زیادہ متغیرات والے: v) اور xiv)۔ چھپی کلید صرف xiv) دیتی ہے۔',
     'درې درجې (کیوبیک) کثیر الحدي: v) (2/3)x³−(4/7)y²+28yz، xiv) x³+y³ او xv) 2x³+4x²−5x+3. له یو ډېرو متغیرونو سره: v) او xiv). چاپ شوې کلیل یوازې xiv) لیکي.', 'v and xiv (key: xiv)')
text('6.3|7|', 'The highest degree in the list is 4 (vi, vii, x, xi, xvi), so no polynomial has a degree higher than a biquadratic (degree 4). The printed key shows xii, whose degree is 1.',
     'فہرست میں سب سے بڑا درجہ 4 ہے (vi, vii, x, xi, xvi)، اس لیے کسی کثیر رقمی کا درجہ بائی کوآڈریٹک (درجہ 4) سے زیادہ نہیں۔ چھپی کلید xii دیتی ہے جس کا درجہ 1 ہے۔',
     'په لیست کې تر ټولو لوړه درجه 4 ده (vi, vii, x, xi, xvi)، نو هیڅ کثیر الحدي له بایکواډراټیک (درجه 4) څخه لوړه درجه نه لري. چاپ شوې کلیل xii لیکي چې درجه یې 1 ده.', 'None (the largest degree is 4)')
# ---- 6.8 Q1 viii (the scan shows + inside the square bracket, not the printed divide sign)
add('6.8|1|viii', [r'(8y + 2z^2) - 4y(5z + 2y) = 8y + 2z^2 - 20yz - 8y^2', r'4 + (8y + 2z^2 - 20yz - 8y^2) = 4 + 8y + 2z^2 - 20yz - 8y^2',
                   r'-2yz(4 + 8y + 2z^2 - 20yz - 8y^2) = -8yz - 16y^2z - 4yz^3 + 40y^2z^2 + 16y^3z',
                   r'4y - 8yz - 16y^2z - 4yz^3 + 40y^2z^2 + 16y^3z'], '4y − 8yz − 16y²z − 4yz³ + 40y²z² + 16y³z',
    N('In the book the bracket reads 4 + {…} (the transcription shows a divide sign). The printed key (4y − 4y²z − yz³ + 40y²z² + 16y³z) does not match this expansion.',
      'کتاب میں قوسین 4 + {…} ہے (نقل میں تقسیم کا نشان آ گیا)۔ چھپی کلید (4y − 4y²z − yz³ + 40y²z² + 16y³z) اس پھیلاؤ سے نہیں ملتی۔',
      'په کتاب کې قوس 4 + {…} دی (په لیکلو کې د ویش نښه راغلې). چاپ شوې کلیل (4y − 4y²z − yz³ + 40y²z² + 16y³z) له دې پراخولو سره نه جوړیږي.'))
# ---- 9.1 Q9
add('9.1|9|', [r'\text{Both legs are equal: } s^2 + s^2 = 32', r'2s^2 = 32 \Rightarrow s^2 = 16', r's = \sqrt{16} = 4'], '4 cm',
    N('The question prints "32 cm²", which is the square of the hypotenuse (c² = 32); this matches the printed key of 4 cm.',
      'سوال میں "32 cm²" چھپا ہے جو وتر کا مربع (c² = 32) ہے؛ یہ چھپی کلید 4 cm سے ملتا ہے۔',
      'په پوښتنه کې "32 cm²" چاپ شوی چې د وتر مربع (c² = 32) دی؛ دا له چاپ شوې کلیل 4 cm سره سمیږي.'))
# ---- 9.2 Q6 (three sectors of a circle with diameter 220 m; angles from the photo/key: 170, 75, 115)
r = 110
rws, ans = [], []
for lab, ang in [('(i)', 170), ('(ii)', 75), ('(iii)', 115)]:
    area = round(ang / 360 * 22 / 7 * r * r, 2)
    rws.append(rf'\frac{{{ang}}}{{360}} \times \frac{{22}}{{7}} \times 110^2 = {area:.2f}')
    ans.append(f'{lab} {area:.2f} m²')
add('9.2|6|', [r'r = \frac{220}{2} = 110', r'170 + 75 + 115 = 360'] + rws, '; '.join(ans),
    N('The three angles (170°, 75°, 115°) are read from the photo and agree with the printed key (17957.93, 7922.62, 12148.02 m²); the small differences come from the value of π used.',
      'تین زاویے (170°، 75°، 115°) تصویر سے پڑھے گئے ہیں اور چھپی کلید (17957.93، 7922.62، 12148.02 m²) سے ملتے ہیں؛ معمولی فرق π کی قیمت سے آتا ہے۔',
      'درې زاویې (170°، 75°، 115°) له انځور څخه لوستل شوې او له چاپ شوې کلیل (17957.93، 7922.62، 12148.02 m²) سره سمیږي؛ کوچنی توپیر د π له ارزښت څخه راځي.'))
# ---- Review 9 Q9 spheres: the figure labels are radius 5 m, radius 18 m and diameter 20 m
rws, ans = [], []
for i, rr in enumerate([5, 18, 10], 1):
    sa = round(4 * 3.14 * rr * rr, 2)
    v = round(4 / 3 * 3.14 * rr ** 3, 2)
    rws.append(rf'4 \times 3.14 \times {rr}^2 = {sa:.2f}')
    rws.append(rf'\frac{{4}}{{3}} \times 3.14 \times {rr}^3 = {v:.2f}')
    ans.append(f'({i}) A = {sa:.2f} m², V = {v:.2f} m³')
add('Review Exercise 9|9|', [r'A = 4\pi r^2, \quad V = \frac{4}{3}\pi r^3'] + rws, '; '.join(ans),
    N('Figure labels: (i) radius 5 m, (ii) radius 18 m, (iii) d = 20 m so r = 10 m. The printed key writes the volume in (ii) as 24416064; the correct value is 24416.06 m³ (decimal point missing).',
      'شکل کی تحریریں: (i) رداس 5 m، (ii) رداس 18 m، (iii) d = 20 m یعنی r = 10 m۔ چھپی کلید (ii) کا حجم 24416064 لکھتی ہے؛ درست قیمت 24416.06 m³ ہے (اعشاریہ نقطہ رہ گیا)۔',
      'د انځور لیکنې: (i) شعاع 5 m، (ii) شعاع 18 m، (iii) d = 20 m یعنې r = 10 m. چاپ شوې کلیل د (ii) حجم 24416064 لیکي؛ سم قیمت 24416.06 m³ دی (اعشاریه نقطه پاتې شوې).'))
# ---- 10.1 Q1, Q2 worked examples (the question lets the student choose the figure)
add('10.1|1|', [r'\text{Square } A(1, 1),\; B(3, 1),\; C(3, 3),\; D(1, 3)', r'\text{Rotation } 90^{\circ} \text{ clockwise about the origin: } (x, y) \to (y, -x)',
                r'A^{\prime}(1, -1),\; B^{\prime}(1, -3),\; C^{\prime}(3, -3),\; D^{\prime}(3, -1)'], 'A′(1, −1), B′(1, −3), C′(3, −3), D′(3, −1)',
    N('The question lets you choose the square; this is one example.', 'سوال میں مربع آپ کی اپنی پسند کا ہے؛ یہ ایک مثال ہے۔', 'پوښتنه کې مربع ستاسو خوښه ده؛ دا یوه بېلګه ده.'))
add('10.1|2|', [r'\text{Triangle } P(1, 1),\; Q(4, 1),\; R(1, 3)', r'\text{Rotation } 180^{\circ} \text{ about the origin: } (x, y) \to (-x, -y)',
                r'P^{\prime}(-1, -1),\; Q^{\prime}(-4, -1),\; R^{\prime}(-1, -3)'], 'P′(−1, −1), Q′(−4, −1), R′(−1, −3)',
    N('The question lets you choose the triangle; this is one example (a half turn is the same clockwise or anticlockwise).', 'سوال میں مثلث آپ کی اپنی پسند کا ہے؛ یہ ایک مثال ہے (آدھا چکر گھڑی کی سمت یا الٹ سمت ایک جیسا ہے)۔', 'پوښتنه کې درې ګوڼی ستاسو خوښه ده؛ دا یوه بېلګه ده (نیمه ګرځېدنه په ساعت یا مخالف لوري یو شان ده).'))
# ---- key-driven figure statements
text('10.1|4|', 'The centre of rotation lies on the perpendicular bisector of every segment joining a point to its image (for example AA′, BB′, CC′); where these bisectors meet is the centre. From the printed key: (a) (3, −5), (b) (5, 3), (c) (−3, 5).',
     'گردش کا مرکز ہر نقطے اور اس کی تصویر کو ملانے والے قطعے (مثلاً AA′، BB′، CC′) کے عمود ناصف پر ہوتا ہے؛ ان کے ملنے کا نقطہ مرکز ہے۔ چھپی کلید کے مطابق: (a) (3, −5)، (b) (5, 3)، (c) (−3, 5)۔',
     'د ګرځېدنې مرکز د هر ټکي او د هغه د انځور د نښلوونکي قطعې (لکه AA′، BB′، CC′) په عمودي نیمګړي کې دی؛ چې دا یو بل ته ورسیږي هغه مرکز دی. د چاپ شوې کلیل له مخې: (a) (3, −5)، (b) (5, 3)، (c) (−3, 5).',
     '(a) (3, −5); (b) (5, 3); (c) (−3, 5)')
text('10.3|1|i', 'Interior points lie inside the circle. From the figure and the printed key: D, E.', 'اندرونی نقطے دائرے کے اندر ہوتے ہیں۔ شکل اور چھپی کلید کے مطابق: D, E۔', 'دننني ټکي د دایرې دننه وي. له انځور او چاپ شوې کلیل څخه: D, E.', 'D, E')
text('10.3|1|ii', 'Exterior points lie outside the circle. From the figure and the printed key: F, G.', 'بیرونی نقطے دائرے کے باہر ہوتے ہیں۔ شکل اور چھپی کلید کے مطابق: F, G۔', 'بهرني ټکي له دایرې بهر وي. له انځور او چاپ شوې کلیل څخه: F, G.', 'F, G')
text('10.3|1|iii', 'Concyclic points lie on the circle itself. From the figure and the printed key: A, B, C.', 'ہم دائرہ نقطے خود دائرے پر ہوتے ہیں۔ شکل اور چھپی کلید کے مطابق: A, B, C۔', 'همدایره ټکي پخپله په دایره کې وي. له انځور او چاپ شوې کلیل څخه: A, B, C.', 'A, B, C')
text('10.3|2|', 'A secant cuts the circle at two points; a tangent touches it at one point. From the figure and the printed key: secants v, y, z; tangents u, x.',
     'قاطع دائرے کو دو نقطوں پر کاٹتا ہے؛ مماس اسے ایک نقطے پر چھوتا ہے۔ شکل اور چھپی کلید کے مطابق: قاطع v, y, z؛ مماس u, x۔',
     'قاطع دایره په دوو ټکو پرې کوي؛ مماس یې په یو ټکي لمس کوي. له انځور او چاپ شوې کلیل څخه: قاطع v, y, z؛ مماس u, x.', 'Secants v, y, z; tangents u, x')
text('10.9|2|', 'Triangles are similar when their angles are equal (or their sides are in the same ratio). From the printed key: (a) ΔABC ~ ΔDFE; (b) ΔABC ~ ΔXZY.',
     'مثلث تب مشابہ ہوتے ہیں جب ان کے زاویے برابر ہوں (یا اطراف کی نسبت یکساں ہو)۔ چھپی کلید کے مطابق: (a) ΔABC ~ ΔDFE؛ (b) ΔABC ~ ΔXZY۔',
     'درې ګوني هغه مهال ورته دي چې زاویې یې مساوي وي (یا د اړخونو نسبت یو شان وي). د چاپ شوې کلیل له مخې: (a) ΔABC ~ ΔDFE؛ (b) ΔABC ~ ΔXZY.', '(a) ΔABC ~ ΔDFE; (b) ΔABC ~ ΔXZY')
text('Review Exercise 10|16|', 'Two triangles are congruent when their corresponding sides and angles are equal. From the figure and the printed key: ΔABC ≅ ΔDEF.',
     'دو مثلث تب ہم مطابق ہوتے ہیں جب ان کے متناظر اطراف اور زاویے برابر ہوں۔ شکل اور چھپی کلید کے مطابق: ΔABC ≅ ΔDEF۔',
     'دوه درې ګوني هغه مهال همغږي دي چې متناظر اړخونه او زاویې یې مساوي وي. له انځور او چاپ شوې کلیل څخه: ΔABC ≅ ΔDEF.', 'ΔABC ≅ ΔDEF')

# ---- 11.4 Q1 (spinner of 8 equal sectors: 3 purple, 2 yellow) and Q7 (cards 4, 7, 7, 0, 3, 8)
for part, rows_, ans_ in [
    ('a', [r'\text{Spinner with 8 equal sectors: 3 purple, 2 yellow}', r'\text{A purple sector and a yellow sector cannot both happen: the events are mutually exclusive}',
           r'P(A) = \frac{3}{8},\quad P(B) = \frac{2}{8}'], 'Yes, mutually exclusive; P(A) = 3/8, P(B) = 2/8'),
    ('b', [r'P(A \cup B) = \frac{3}{8} + \frac{2}{8} = \frac{5}{8}'], 'P(A ∪ B) = 5/8'),
    ('c', [r'P(A \cap B) = 0'], 'P(A ∩ B) = 0')]:
    add(f'11.4|1|{part}', rows_, ans_)
for part, rows_, ans_, nt in [
    ('a', [r'\text{Cards: } 4, 7, 7, 0, 3, 8 \quad (6 \text{ cards})', r'P(A) = P(7) = \frac{2}{6},\quad P(B) = P(\text{even}) = \frac{3}{6} \quad (4, 0, 8; \text{ 0 is even})',
           r'\text{No card is both 7 and even: mutually exclusive}'], 'Yes, mutually exclusive; P(A) = 2/6, P(B) = 3/6', None),
    ('b', [r'P(A \cup B) = \frac{2}{6} + \frac{3}{6} = \frac{5}{6}'], 'P(A ∪ B) = 5/6', None),
    ('c', [r'P(A \cap B) = 0'], 'P(A ∩ B) = 0',
     N('The printed key gives P(A ∩ B) = 1, which is not possible for mutually exclusive events (it is 0).', 'چھپی کلید P(A ∩ B) = 1 دیتی ہے جو باہم خارج واقعات کے لیے ممکن نہیں (یہ 0 ہے)۔', 'چاپ شوې کلیل P(A ∩ B) = 1 ښیي چې د متقابلو بهرنیو پېښو لپاره ناشونی دی (دا 0 دی).'))]:
    add(f'11.4|7|{part}', rows_, ans_, nt)

# ---- 10.2 Q1: triangle read from the 450-dpi render of the scan (same triangle as Example 1: A(1,1), B(3,1), C(3,3)); centre (1,-1), scale factor 2
add('10.2|1|', [r'\text{Vertices read from the grid: } A(1, 1),\; B(3, 1),\; C(3, 3)',
                r'\text{Centre of enlargement } O(1, -1),\; k = 2: \quad P'' = O + k(P - O)',
                r'A^{\prime} = (1 + 2(1 - 1),\; -1 + 2(1 + 1)) = (1, 3)',
                r'B^{\prime} = (1 + 2(3 - 1),\; -1 + 2(1 + 1)) = (5, 3)',
                r'C^{\prime} = (1 + 2(3 - 1),\; -1 + 2(3 + 1)) = (5, 7)'],
    'A′(1, 3), B′(5, 3), C′(5, 7)',
    N('The triangle is faint in the scan; its vertices (1, 1), (3, 1), (3, 3) were read from a contrast-enhanced render. If your figure differs, apply the same rule to its vertices.',
      'سکین میں تکون مدھم ہے؛ اس کے سرے (1, 1)، (3, 1)، (3, 3) بڑھائی گئی تصویر سے پڑھے گئے ہیں۔ اگر آپ کی شکل مختلف ہو تو یہی قاعدہ اس کے سروں پر لگائیں۔',
      'په سکین کې درې ګوڼی کمزورې ده؛ د هغې څوکې (1, 1)، (3, 1)، (3, 3) له لوی شوي انځور څخه لوستل شوې. که ستاسو انځور توپیر ولري همدا قاعده د هغې په څوکو وکاروئ.'))


# ---- 10.10 Q5 (figure read from the 250-dpi render: L = 40, N = 20; D = x + 90, F = 5y - 120)
add('10.10|5|', [r'\text{ASA: } \angle L = \angle D \text{ and } \angle N = \angle F',
                 r'x + 90 = 40 \Rightarrow x = 40 - 90 = -50',
                 r'5y - 120 = 20 \Rightarrow 5y = 140 \Rightarrow y = 28'],
    'x = −50, y = 28')


# ---- 10.10 Q7 (figures read from the 400-dpi render: tick marks and arcs)
A7 = [
 ('a', 'Lines AE and DC cross at B. In triangles ABD and EBC: AD = EC (one tick each), ∠A = ∠E (one arc each), ∠ABD = ∠EBC (vertically opposite angles). So ΔABD ≅ ΔEBC by the AAS property.',
  'خطوط AE اور DC نقطہ B پر ملتے ہیں۔ مثلث ABD اور EBC میں: AD = EC (ہر ایک پر ایک نشان)، ∠A = ∠E (ہر ایک پر ایک قوس)، ∠ABD = ∠EBC (متقابل زاویے)۔ اس لیے AAS خاصیت سے ΔABD ≅ ΔEBC۔',
  'کرښې AE او DC په B کې سره غوڅیږي. په درې ګونو ABD او EBC کې: AD = EC (هر یو کې یو نښه)، ∠A = ∠E (هر یو کې یو قوس)، ∠ABD = ∠EBC (مقابل زاویې). نو د AAS ځانګړتیا له مخې ΔABD ≅ ΔEBC.'),
 ('b', 'In triangles FGH and KJI: ∠F = ∠K (one arc), FH = KI (one tick), ∠H = ∠I (two arcs), and FH lies between the two marked angles. So ΔFGH ≅ ΔKJI by the ASA property.',
  'مثلث FGH اور KJI میں: ∠F = ∠K (ایک قوس)، FH = KI (ایک نشان)، ∠H = ∠I (دو قوس)، اور FH دونوں نشان زد زاویوں کے درمیان ہے۔ اس لیے ASA خاصیت سے ΔFGH ≅ ΔKJI۔',
  'په درې ګونو FGH او KJI کې: ∠F = ∠K (یو قوس)، FH = KI (یو نښه)، ∠H = ∠I (دوه قوسونه)، او FH د دواړو نښه شوو زاویو تر منځ دی. نو د ASA ځانګړتیا له مخې ΔFGH ≅ ΔKJI.'),
 ('c', 'Lines MP and NO cross at F. In triangles MFN and PFO: MF = PF (one tick each), NF = OF (two ticks each), ∠MFN = ∠PFO (vertically opposite angles). So ΔMFN ≅ ΔPFO by the SAS property.',
  'خطوط MP اور NO نقطہ F پر ملتے ہیں۔ مثلث MFN اور PFO میں: MF = PF (ہر ایک پر ایک نشان)، NF = OF (ہر ایک پر دو نشان)، ∠MFN = ∠PFO (متقابل زاویے)۔ اس لیے SAS خاصیت سے ΔMFN ≅ ΔPFO۔',
  'کرښې MP او NO په F کې سره غوڅیږي. په درې ګونو MFN او PFO کې: MF = PF (هر یو کې یو نښه)، NF = OF (هر یو کې دوه نښې)، ∠MFN = ∠PFO (مقابل زاویې). نو د SAS ځانګړتیا له مخې ΔMFN ≅ ΔPFO.'),
 ('d', 'In right triangles QTR and RSQ (right angles at T and S): QR = RQ (common hypotenuse), QT = RS (one tick each). So ΔQTR ≅ ΔRSQ by the RHS (hypotenuse-side) property.',
  'قائمہ مثلث QTR اور RSQ میں (T اور S پر قائمہ زاویے): QR = RQ (مشترک وتر)، QT = RS (ہر ایک پر ایک نشان)۔ اس لیے RHS (وتر اور ضلع) خاصیت سے ΔQTR ≅ ΔRSQ۔',
  'په قایم درې ګونو QTR او RSQ کې (په T او S کې قایم زاویې): QR = RQ (ګډ وتر)، QT = RS (هر یو کې یو نښه). نو د RHS (وتر او اړخ) ځانګړتیا له مخې ΔQTR ≅ ΔRSQ.'),
 ('e', 'In triangles UVW and WXU: UV = WX (two ticks each), VW = XU (one tick each), UW = WU (common side). So ΔUVW ≅ ΔWXU by the SSS property.',
  'مثلث UVW اور WXU میں: UV = WX (ہر ایک پر دو نشان)، VW = XU (ہر ایک پر ایک نشان)، UW = WU (مشترک ضلع)۔ اس لیے SSS خاصیت سے ΔUVW ≅ ΔWXU۔',
  'په درې ګونو UVW او WXU کې: UV = WX (هر یو کې دوه نښې)، VW = XU (هر یو کې یو نښه)، UW = WU (ګډ اړخ). نو د SSS ځانګړتیا له مخې ΔUVW ≅ ΔWXU.')]
rows7 = ' ;; '.join(f'({k}) {e}|({k}) {u}|({k}) {ps_}' for k, e, u, ps_ in A7)
L.append('10.10|7| ~ @text ' + rows7 + ' => (a) AAS; (b) ASA; (c) SAS; (d) RHS; (e) SSS %%')


# ---- 10.10 Q1 (figures read from the 300-dpi render of pages 267-268)
Q1 = [
 ('a', 'Triangles ABC and ADC: ∠B = ∠D = 90°, BC = DC = 7 cm, and AC is the common hypotenuse. So ΔABC ≅ ΔADC by the RHS property.',
  'مثلث ABC اور ADC میں: ∠B = ∠D = 90°، BC = DC = 7 cm، اور AC مشترک وتر ہے۔ اس لیے RHS خاصیت سے ΔABC ≅ ΔADC۔',
  'په درې ګونو ABC او ADC کې: ∠B = ∠D = 90°، BC = DC = 7 cm، او AC ګډ وتر دی. نو د RHS ځانګړتیا له مخې ΔABC ≅ ΔADC.'),
 ('b', 'Triangles ABC and DEF: ∠A = ∠D = 60°, AC = DF = 1.2 cm (the side between the marked angles), ∠C = ∠F = 55°. So ΔABC ≅ ΔDEF by the ASA property.',
  'مثلث ABC اور DEF میں: ∠A = ∠D = 60°، AC = DF = 1.2 cm (نشان زد زاویوں کے درمیان کا ضلع)، ∠C = ∠F = 55°۔ اس لیے ASA خاصیت سے ΔABC ≅ ΔDEF۔',
  'په درې ګونو ABC او DEF کې: ∠A = ∠D = 60°، AC = DF = 1.2 cm (د نښه شوو زاویو تر منځ اړخ)، ∠C = ∠F = 55°. نو د ASA ځانګړتیا له مخې ΔABC ≅ ΔDEF.'),
 ('c', 'ΔMJK has angles 40° and 20° (third angle 120°); ΔLKJ has angles 20° and 55° (third angle 105°). The angles differ, so ΔMJK is not congruent to ΔLKJ.',
  'ΔMJK کے زاویے 40° اور 20° ہیں (تیسرا 120°)؛ ΔLKJ کے زاویے 20° اور 55° ہیں (تیسرا 105°)۔ زاویے مختلف ہیں، اس لیے ΔMJK اور ΔLKJ ہم مطابق نہیں۔',
  'د ΔMJK زاویې 40° او 20° دي (درېیمه 120°)؛ د ΔLKJ زاویې 20° او 55° دي (درېیمه 105°). زاویې توپیر لري، نو ΔMJK له ΔLKJ سره همغږې نه دي.'),
 ('d', 'The tick marks on the sides of ΔGHI and the second triangle are partly cut at the page edge; the printed key gives ΔGHI ≅ the second triangle (matching single, double and triple ticks give SSS).',
  'ΔGHI اور دوسرے مثلث کے اضلاع کے نشان صفحے کے کنارے سے جزوی کٹے ہوئے ہیں؛ چھپی کلید ΔGHI کو دوسرے مثلث کے ہم مطابق بتاتی ہے (ایک، دو اور تین نشان ملنے سے SSS)۔',
  'د ΔGHI او دویم درې ګوني د اړخونو نښې د مخ په څنډه کې یوه برخه پرې شوې؛ چاپ شوې کلیل ΔGHI له دویم درې ګوني سره همغږی ښیي (یو، دوه او درې نښې سره سمې وي نو SSS).')]
rows1 = ' ;; '.join(f'({k}) {e}|({k}) {u}|({k}) {ps_}' for k, e, u, ps_ in Q1)
L.append('10.10|1| ~ @text ' + rows1 + ' => (a) congruent (RHS); (b) congruent (ASA); (c) not congruent; (d) from the key %%')


# ---- Review 10 Q4 and Q3 (figures read from the 300-dpi render of page 272/271)
text('Review Exercise 10|4|',
     'A tangent touches the circle at exactly one point; a secant cuts it at two points. In the figure, lines l (touching at the top) and p (touching at the bottom) are tangents; lines m, n and o each cut the circle at two points, so they are secants.',
     'مماس دائرے کو ٹھیک ایک نقطے پر چھوتا ہے؛ قاطع اسے دو نقطوں پر کاٹتا ہے۔ شکل میں خطوط l (اوپر سے چھوتا) اور p (نیچے سے چھوتا) مماس ہیں؛ خطوط m, n اور o ہر ایک دائرے کو دو نقطوں پر کاٹتے ہیں، اس لیے یہ قاطع ہیں۔',
     'مماس دایره په دقیق یو ټکي لمس کوي؛ قاطع یې په دوو ټکو پرې کوي. په انځور کې کرښې l (له پورته لمس کوي) او p (له ښکته لمس کوي) مماس دي؛ کرښې m, n او o هره یوه دایره په دوو ټکو پرې کوي، نو قاطع دي.',
     'Tangents: l, p. Secants: m, n, o')
text('Review Exercise 10|3|',
     'O is the centre. The segment FG joining two points of the circle is a chord; the chord through the centre O is a diameter; OJ (centre to the circle) is a radius; the angle at O between two radii is a central angle and the region between those radii and their arc is a sector; a part of the circle between two points is an arc; the line touching the circle at one point (the arrowed line at the top) is a tangent; an arrowed line cutting the circle at two points is a secant.',
     'O مرکز ہے۔ دائرے کے دو نقطوں کو ملانے والا قطعہ FG وتر ہے؛ مرکز O سے گزرنے والا وتر قطر ہے؛ OJ (مرکز سے دائرے تک) رداس ہے؛ دو رداسوں کے درمیان O پر زاویہ مرکزی زاویہ ہے اور ان رداسوں اور ان کے قوس کے درمیان کا حصہ قطاع ہے؛ دو نقطوں کے درمیان دائرے کا حصہ قوس ہے؛ جو لکیر دائرے کو ایک نقطے پر چھوئے (اوپر والی تیر والی لکیر) وہ مماس ہے؛ جو دو نقطوں پر کاٹے وہ قاطع ہے۔',
     'O مرکز دی. هغه قطعه FG چې د دایرې دوه ټکي نښلوي وتر دی؛ هغه وتر چې له مرکز O تېرېږي قطر دی؛ OJ (له مرکز تر دایرې) شعاع ده؛ د دوو شعاعګانو تر منځ په O کې زاویه مرکزي زاویه ده او د دغو شعاعګانو او د هغوی د قوس تر منځ سیمه سکتور ده؛ د دوو ټکو تر منځ د دایرې برخه قوس دی؛ هغه کرښه چې دایره په یو ټکي لمس کړي (پورتنۍ غشي لرونکې کرښه) مماس ده؛ چې په دوو ټکو پرې کړي قاطع ده.',
     'O centre, FG chord, diameter, OJ radius, central angle, sector, arc, tangent, secant')


# ---- 10.3 Q3 (figure read from the 300-dpi render of page 249)
text('10.3|3|',
     'Chord: FG (a segment joining two points of the circle). Segment: the region between the chord FG and the arc above it. Central angle: the angle at the centre O between OI and OJ. Sector: the region enclosed by the radii OI, OJ and the arc IJ. Minor arc: the short arc IJ (less than half the circle). Major arc: the rest of the circle from I round to J. Tangent: the arrowed line that touches the circle at F only. Secant: the arrowed line at the lower right that cuts the circle at two points.',
     'وتر: FG (دائرے کے دو نقطوں کو ملانے والا قطعہ)۔ قطعہ (سیگمنٹ): وتر FG اور اس کے اوپر کے قوس کے درمیان کا خطہ۔ مرکزی زاویہ: مرکز O پر OI اور OJ کے درمیان زاویہ۔ قطاع (سیکٹر): رداسوں OI، OJ اور قوس IJ سے گھرا ہوا خطہ۔ چھوٹا قوس: چھوٹا قوس IJ (آدھے دائرے سے کم)۔ بڑا قوس: دائرے کا باقی حصہ I سے گھوم کر J تک۔ مماس: تیر والی وہ لکیر جو دائرے کو صرف F پر چھوتی ہے۔ قاطع: نیچے دائیں طرف کی تیر والی لکیر جو دائرے کو دو نقطوں پر کاٹتی ہے۔',
     'وتر: FG (د دایرې دوه ټکي نښلوونکې قطعه). قطعه (سیګمنټ): د وتر FG او د هغه د پاسني قوس تر منځ سیمه. مرکزي زاویه: په مرکز O کې د OI او OJ تر منځ زاویه. سکتور: هغه سیمه چې د شعاعګانو OI، OJ او قوس IJ لخوا احاطه شوې. کوچنی قوس: کوچنی قوس IJ (له نیمې دایرې کم). لوی قوس: د دایرې پاتې برخه له I څخه تر J پورې. مماس: غشي لرونکې کرښه چې دایره یوازې په F کې لمس کوي. قاطع: په ښکته ښي خوا کې غشي لرونکې کرښه چې دایره په دوو ټکو پرې کوي.',
     'Chord FG; segment; central angle IOJ; sector OIJ; minor arc IJ; major arc; tangent at F; secant')


# ---- Review 10 Q19 and Q20 (grids read from 450-dpi renders of page 273/274)
add('Review Exercise 10|19|', [r'\text{Triangle read from the grid: } A(0, 1),\; B(2, 2),\; C(0, 5)',
                               r'\text{Centre } O(-2, 1),\; k = 3: \quad P^{\prime} = O + 3(P - O)',
                               r'A^{\prime} = (-2 + 3(0 + 2),\; 1 + 3(1 - 1)) = (4, 1)',
                               r'B^{\prime} = (-2 + 3(2 + 2),\; 1 + 3(2 - 1)) = (10, 4)',
                               r'C^{\prime} = (-2 + 3(0 + 2),\; 1 + 3(5 - 1)) = (4, 13)'],
    'A′(4, 1), B′(10, 4), C′(4, 13)',
    N('C′(4, 13) lies above the printed grid (it stops at y = 8), so the grid must be extended to draw the whole triangle.',
      'C′(4, 13) چھپی ہوئی گرڈ سے اوپر ہے (گرڈ y = 8 تک ہے)، اس لیے پورا تکون بنانے کے لیے گرڈ بڑھانی ہوگی۔',
      'C′(4, 13) له چاپ شوې ګرډ څخه پورته دی (ګرډ تر y = 8 دی)، نو بشپړ درې ګونی رسمولو لپاره باید ګرډ اوږد شي.'))
add('Review Exercise 10|20|', [r'\text{Small triangle: } A(1, 1),\; B(1, 2),\; C(3, 1); \quad \text{large triangle: } A^{\prime}(6, 4),\; B^{\prime}(6, 6),\; C^{\prime}(10, 4)',
                               r'k = \frac{A^{\prime}B^{\prime}}{AB} = \frac{2}{1} = 2,\qquad \frac{A^{\prime}C^{\prime}}{AC} = \frac{4}{2} = 2',
                               r'\text{Line } AA^{\prime}: (1 + 5t,\; 1 + 3t);\quad \text{line } BB^{\prime}: (1 + 5u,\; 2 + 4u)',
                               r'1 + 3t = 2 + 4t \Rightarrow t = -1 \Rightarrow O = (-4, -2)',
                               r'CC^{\prime}: (3 + 7s,\; 1 + 3s) \text{ at } s = -1 \text{ gives } (-4, -2) \text{ as well}'],
    'Scale factor 2, centre of enlargement (−4, −2)')


# ---- 10.2 Q3 (first grid read from a 450-dpi render of page 245; the second grid is too faint and skewed)
add('10.2|3|', [r'\text{Grid 1, small L-shape: } (1,1),\,(1,4),\,(2,4),\,(2,2),\,(3,2),\,(3,1);\quad \text{large L-shape: } (4,0),\,(4,6),\,(6,6),\,(6,2),\,(8,2),\,(8,0)',
                r'k = \frac{8 - 4}{3 - 1} = 2,\qquad \frac{6 - 0}{4 - 1} \text{ along the height gives } \frac{6}{3} = 2',
                r'\text{Centre: } O = 2P - P^{\prime} \text{ for } P(1, 1),\, P^{\prime}(4, 0): \quad O = (2 - 4,\; 2 - 0) = (-2, 2)',
                r'\text{Check with } (3, 2) \to (8, 2): \quad O = (6 - 8,\; 4 - 2) = (-2, 2)',
                r'\text{Grid 2 (green triangle and its faint image) is too faint in the scan to read}'],
    'Grid 1: scale factor 2, centre (−2, 2). Grid 2: not legible in the scan',
    N('The coordinates of grid 1 were read from a contrast-enhanced render of a skewed photograph and may be off by about half a unit; the scale factor and centre follow from the consistent pattern of all six corners.',
      'گرڈ 1 کے محدد ٹیڑھی تصویر کے بڑھائے گئے عکس سے پڑھے گئے ہیں اور تقریباً آدھی اکائی کی غلطی ممکن ہے؛ پیمانہ اور مرکز چھ کونوں کے یکساں نمونے سے نکلتے ہیں۔',
      'د ګرډ 1 همغږي له یوې کږې انځور د لوی شوي عکس څخه لوستل شوي او شاوخوا نیمه واحده تېروتنه کیدی شي؛ پیمانه او مرکز د ټولو شپږو کونجونو له یو شان بڼې څخه راځي.'))


# ---- Review 10 Q18: same task as 10.1 Q1 (student's own square)
add('Review Exercise 10|18|', [r'\text{Square } A(1, 1),\; B(3, 1),\; C(3, 3),\; D(1, 3)', r'\text{Rotation } 90^{\circ} \text{ clockwise about the origin: } (x, y) \to (y, -x)',
                               r'A^{\prime}(1, -1),\; B^{\prime}(1, -3),\; C^{\prime}(3, -3),\; D^{\prime}(3, -1)'], 'A′(1, −1), B′(1, −3), C′(3, −3), D′(3, −1)',
    N('The question lets you choose the square; this is one example.', 'سوال میں مربع آپ کی اپنی پسند کا ہے؛ یہ ایک مثال ہے۔', 'پوښتنه کې مربع ستاسو خوښه ده؛ دا یوه بېلګه ده.'))

# ---- Review 10 Q2 definitions
text('Review Exercise 10|2|', 'Chord: a line segment joining two points of the circle. Secant: a line that cuts the circle at two points. Arc: a part of the circumference. Sector: the region between two radii and the arc they cut off. Tangent: a line that touches the circle at exactly one point.',
     'وتر (کارڈ): دائرے کے دو نقطوں کو ملانے والا قطعہ۔ قاطع: وہ لکیر جو دائرے کو دو نقطوں پر کاٹے۔ قوس: محیط کا ایک حصہ۔ قطاع: دو رداس اور ان کے کاٹے ہوئے قوس کے درمیان کا خطہ۔ مماس: وہ لکیر جو دائرے کو ٹھیک ایک نقطے پر چھوئے۔',
     'وتر (کارډ): د دایرې دوه ټکي نښلوونکې قطعه. قاطع: هغه کرښه چې دایره په دوو ټکو پرې کړي. قوس: د محیط یوه برخه. سکتور: د دوو شعاعګانو او د هغوی د پرې شوي قوس تر منځ سیمه. مماس: هغه کرښه چې دایره په دقیق یو ټکي لمس کړي.',
     'Chord, secant, arc, sector, tangent defined')

OUT.write_text('\n'.join(L) + '\n', encoding='utf-8')
print(len(L), 'rows ->', OUT)
