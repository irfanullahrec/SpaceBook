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
text('6.3|4|', 'Quadratic means degree 2. In one variable the only candidate is ii) 3x² − 15 (variable x, degree 2); iii) has two variables and vi) has degree 4.',
     'دو درجے (کوآڈریٹک) کا مطلب درجہ 2 ہے۔ ایک متغیر میں صرف ii) 3x² − 15 ہے (متغیر x، درجہ 2)؛ iii) میں دو متغیرات ہیں اور vi) کا درجہ 4 ہے۔',
     'څلورڅخنی (کواډراټیک) یعنې درجه 2. په یو متغیر کې یوازې ii) 3x² − 15 دی (متغیر x، درجه 2)؛ iii) دوه متغیره لري او vi) درجه 4 لري.', 'ii')
text('6.3|5|', 'Quadratic in two variables: degree 2 with exactly two variables, which is iii) x² + y² + 2xy. (The printed key also lists iv) and ix), but those involve three or more variables.)',
     'دو متغیرات میں دو درجے والا: درجہ 2 اور بالکل دو متغیرات، یعنی iii) x² + y² + 2xy۔ (چھپی کلید iv) اور ix) بھی لکھتی ہے مگر ان میں تین یا زیادہ متغیرات ہیں۔)',
     'په دوو متغیرونو کې دوه درجه: درجه 2 او دقیقاً دوه متغیره، یعنې iii) x² + y² + 2xy. (چاپ شوې کلیل iv) او ix) هم لیکي خو هغو درې یا ډېر متغیره لري.)', 'iii')
text('6.3|6|', 'Cubic means degree 3. Cubic polynomials in the list are xi), xiv) and xv); only xiv) x³ + y³ has more than one variable.',
     'تین درجے (کیوبک) کا مطلب درجہ 3 ہے۔ فہرست میں کیوبک xi)، xiv) اور xv) ہیں؛ ان میں صرف xiv) x³ + y³ میں ایک سے زیادہ متغیرات ہیں۔',
     'درې درجه (کیوبیک) یعنې درجه 3. په لیست کې کیوبیک xi)، xiv) او xv) دي؛ له دې څخه یوازې xiv) x³ + y³ له یو ډېر متغیره لري.', 'xiv')
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

# ---- Review 10 Q2 definitions
text('Review Exercise 10|2|', 'Chord: a line segment joining two points of the circle. Secant: a line that cuts the circle at two points. Arc: a part of the circumference. Sector: the region between two radii and the arc they cut off. Tangent: a line that touches the circle at exactly one point.',
     'وتر (کارڈ): دائرے کے دو نقطوں کو ملانے والا قطعہ۔ قاطع: وہ لکیر جو دائرے کو دو نقطوں پر کاٹے۔ قوس: محیط کا ایک حصہ۔ قطاع: دو رداس اور ان کے کاٹے ہوئے قوس کے درمیان کا خطہ۔ مماس: وہ لکیر جو دائرے کو ٹھیک ایک نقطے پر چھوئے۔',
     'وتر (کارډ): د دایرې دوه ټکي نښلوونکې قطعه. قاطع: هغه کرښه چې دایره په دوو ټکو پرې کړي. قوس: د محیط یوه برخه. سکتور: د دوو شعاعګانو او د هغوی د پرې شوي قوس تر منځ سیمه. مماس: هغه کرښه چې دایره په دقیق یو ټکي لمس کړي.',
     'Chord, secant, arc, sector, tangent defined')

OUT.write_text('\n'.join(L) + '\n', encoding='utf-8')
print(len(L), 'rows ->', OUT)
