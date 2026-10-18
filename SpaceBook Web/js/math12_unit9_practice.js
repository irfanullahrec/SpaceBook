/* Authored practice grounded in the reviewed Unit 9 topics.
 * This is supplementary learning material, not printed textbook/board questions. */
(function () {
  'use strict';
  if (typeof MATH_12_DATA === 'undefined') throw new Error('Load Class 12 Mathematics before Unit 9 practice.');
  const chapter = MATH_12_DATA.find(item => item.id === 'unit-9');
  if (!chapter) throw new Error('Class 12 Mathematics Unit 9 is missing.');
  chapter.slos = chapter.slos || {};
  const origin = 'SpaceBook supplementary practice';
  const references = (section, first, last) => [{
    class: 12, subject: 'Mathematics', sectionId: section, pageStart: first, pageEnd: last,
    relationship: 'Reviewed topic basis for an authored practice question; not a printed question.'
  }];
  const parabola = (first = 243, last = 244) => references('sec-9-1', first, last);
  const hyperbola = (first = 266, last = 269) => references('sec-9-3', first, last);
  const mcqs = [
    {
      id: 'math12-u9-practice-mcq-01',
      q: 'What is the eccentricity of a nondegenerate parabola?',
      qUrdu: 'غیر منحط قطع مکافی کی اختلافِ مرکزیت کیا ہوتی ہے؟',
      qPashto: 'د غیر منحط پارابولا خروج له مرکز څخه څومره وي؟',
      options: ['0', '1', 'Greater than 1', 'Strictly between 0 and 1'], correct: 1,
      answerUrdu: '1', answerPashto: '1',
      exp: 'A parabola has equal focus-distance and perpendicular directrix-distance, so their ratio e is 1.',
      expUrdu: 'قطع مکافی کے ہر نقطے کا فوکس سے فاصلہ اور خطِ ہادی سے عمودی فاصلہ برابر ہوتے ہیں، اس لیے ان کا تناسب e = 1 ہے۔',
      expPashto: 'د پارابولا د هر ټکي له محراق څخه واټن او له هادي کرښې څخه عمودي واټن برابر وي؛ نو د دواړو نسبت e = 1 دی.',
      optionExplanations: ['e = 0 describes the circular limit of ellipses, not a parabola.', 'Correct: equal distances give e = 1.', 'e > 1 corresponds to a hyperbola.', '0 < e < 1 corresponds to a noncircular ellipse.'], sourceReferences: parabola()
    },
    {
      id: 'math12-u9-practice-mcq-02', q: 'What is the focus of y² = 12x?',
      qUrdu: 'y² = 12x کا فوکس کون سا ہے؟', qPashto: 'د y² = 12x محراق کوم دی؟',
      options: ['(12, 0)', '(0, 3)', '(3, 0)', '(−3, 0)'], correct: 2,
      answerUrdu: '(3, 0)', answerPashto: '(3, 0)',
      exp: 'Compare y² = 4px with y² = 12x: p = 3, so the focus is (p, 0) = (3, 0).',
      expUrdu: 'y² = 4px سے موازنہ کرنے پر 4p = 12، یعنی p = 3 ملتا ہے؛ لہٰذا فوکس (3, 0) ہے۔',
      expPashto: 'له y² = 4px سره په پرتله کولو 4p = 12 او p = 3 کېږي؛ نو محراق (3, 0) دی.',
      optionExplanations: ['12 is 4p, not p.', 'This would be the focus of an upward-opening parabola.', 'Correct: p = 3 and the axis is horizontal.', 'The positive coefficient opens the parabola to the right, not the left.'], sourceReferences: parabola()
    },
    {
      id: 'math12-u9-practice-mcq-03', q: 'Which line is the directrix of x² = −8y?',
      qUrdu: 'x² = −8y کا خطِ ہادی کون سا ہے؟', qPashto: 'د x² = −8y هادي کرښه کومه ده؟',
      options: ['y = −2', 'x = 2', 'x = −2', 'y = 2'], correct: 3,
      answerUrdu: 'y = 2', answerPashto: 'y = 2',
      exp: 'Here 4p = −8, so p = −2. For x² = 4py the directrix is y = −p = 2.',
      expUrdu: 'یہاں p = −2 ہے۔ x² = 4py کے لیے خطِ ہادی y = −p ہوتا ہے، لہٰذا y = 2 ہے۔',
      expPashto: 'دلته p = −2 دی. د x² = 4py هادي کرښه y = −p ده؛ نو y = 2 کېږي.',
      optionExplanations: ['y = −2 passes through the focus; it is not the directrix.', 'The axis is vertical, so the directrix must be horizontal.', 'This vertical line has the wrong orientation.', 'Correct: the directrix lies above the vertex for this downward-opening parabola.'], sourceReferences: parabola()
    },
    {
      id: 'math12-u9-practice-mcq-04', q: 'What is the length of the latus rectum of y² = −16x?',
      qUrdu: 'y² = −16x کے وترِ عدسی کی لمبائی کیا ہے؟', qPashto: 'د y² = −16x د محراقي عمودي وتر اوږدوالی څومره دی؟',
      options: ['−16', '4', '8', '16'], correct: 3,
      answerUrdu: '16 اکائیاں', answerPashto: '16 واحدونه',
      exp: 'The signed parameter is p = −4, but a geometric length is nonnegative: 4|p| = 16.',
      expUrdu: 'p = −4 ہے، مگر ہندسی لمبائی منفی نہیں ہوتی؛ اس لیے 4|p| = 16 ہے۔',
      expPashto: 'p = −4 دی، خو هندسي اوږدوالی منفي نه وي؛ نو 4|p| = 16 دی.',
      optionExplanations: ['−16 is the signed value 4p, not a length.', '4 is |p|, only the vertex-to-focus distance.', '8 is half the full latus-rectum length.', 'Correct: the full length is 4|p|.'], sourceReferences: parabola()
    },
    {
      id: 'math12-u9-practice-mcq-05', q: 'Find the tangent to y² = 8x at (2, 4).',
      qUrdu: 'نقطہ (2, 4) پر y² = 8x کا مماس معلوم کریں۔', qPashto: 'په (2, 4) ټکي کې د y² = 8x مماس پیدا کړئ.',
      options: ['y = x + 2', 'y = −x + 6', 'y = 2x', 'x = 2'], correct: 0,
      answerUrdu: 'y = x + 2', answerPashto: 'y = x + 2',
      exp: 'Differentiate: 2y y′ = 8. At (2,4), y′ = 1, so y − 4 = x − 2.',
      expUrdu: 'تفریق سے 2y y′ = 8 ملتا ہے۔ (2, 4) پر ڈھلوان 1 ہے، لہٰذا y − 4 = x − 2 ہے۔',
      expPashto: 'له مشتق اخیستلو 2y y′ = 8 کېږي. په (2, 4) کې میل 1 دی؛ نو y − 4 = x − 2 دی.',
      optionExplanations: ['Correct: it passes through the point with tangent slope 1.', 'This is the normal, whose slope is −1.', 'It passes through the point but has the wrong slope 2.', 'The tangent is not vertical at a point with y = 4.'], sourceReferences: parabola(247, 248)
    },
    {
      id: 'math12-u9-practice-mcq-06', q: 'Find the normal to y² = 8x at (2, 4).',
      qUrdu: 'نقطہ (2, 4) پر y² = 8x کا عمودی خط معلوم کریں۔', qPashto: 'په (2, 4) ټکي کې د y² = 8x نورمال پیدا کړئ.',
      options: ['y = x + 2', 'y = −x + 6', 'y = −x + 2', 'y = 4'], correct: 1,
      answerUrdu: 'y = −x + 6', answerPashto: 'y = −x + 6',
      exp: 'The tangent slope is 1; the normal slope is −1. Through (2,4), y − 4 = −(x − 2).',
      expUrdu: 'مماس کی ڈھلوان 1 ہے، اس لیے عمودی خط کی ڈھلوان −1 ہے۔ (2, 4) سے گزرنے والا خط y − 4 = −(x − 2) ہے۔',
      expPashto: 'د مماس میل 1 دی؛ نو د نورمال میل −1 دی. له (2, 4) څخه تېرېدونکې کرښه y − 4 = −(x − 2) ده.',
      optionExplanations: ['This is the tangent rather than the normal.', 'Correct: it passes through (2,4) and is perpendicular to the tangent.', 'It has the correct slope but does not pass through (2,4).', 'A horizontal normal would require a vertical tangent, which this point does not have.'], sourceReferences: parabola(248, 249)
    },
    {
      id: 'math12-u9-practice-mcq-07', q: 'What are the vertices of x²/9 − y²/16 = 1?',
      qUrdu: 'x²/9 − y²/16 = 1 کے راس کون سے ہیں؟', qPashto: 'د x²/9 − y²/16 = 1 رأسونه کوم دي؟',
      options: ['(0, ±4)', '(±5, 0)', '(±3, 0)', '(±9, 0)'], correct: 2,
      answerUrdu: '(−3, 0) اور (3, 0)', answerPashto: '(−3, 0) او (3, 0)',
      exp: 'The positive x² term gives a horizontal transverse axis; a² = 9, so a = 3 and the vertices are (±3,0).',
      expUrdu: 'x² کی علامت مثبت ہونے سے حقیقی محور افقی ہے۔ a² = 9 سے a = 3 ملتا ہے، اس لیے راس (±3, 0) ہیں۔',
      expPashto: 'د x² مثبت نښه ښيي چې حقیقي محور افقي دی. له a² = 9 څخه a = 3 کېږي؛ نو رأسونه (±3, 0) دي.',
      optionExplanations: ['These are endpoints of the conjugate-axis segment, not points on the hyperbola.', 'These are the foci, since c = 5.', 'Correct: vertices are at x = ±a.', '9 is a², not the vertex distance a.'], sourceReferences: hyperbola()
    },
    {
      id: 'math12-u9-practice-mcq-08', q: 'What are the foci of x²/9 − y²/16 = 1?',
      qUrdu: 'x²/9 − y²/16 = 1 کے فوکس کون سے ہیں؟', qPashto: 'د x²/9 − y²/16 = 1 محراقونه کوم دي؟',
      options: ['(±5, 0)', '(±√7, 0)', '(0, ±5)', '(±3, 0)'], correct: 0,
      answerUrdu: '(−5, 0) اور (5, 0)', answerPashto: '(−5, 0) او (5, 0)',
      exp: 'For a hyperbola, c² = a² + b² = 9 + 16 = 25, so c = 5. Its foci lie on the horizontal transverse axis.',
      expUrdu: 'قطع زائد کے لیے c² = a² + b² = 25 ہے، اس لیے c = 5 ہے۔ فوکس افقی حقیقی محور پر ہیں۔',
      expPashto: 'د هایپربولا لپاره c² = a² + b² = 25 دی؛ نو c = 5 دی. محراقونه پر افقي حقیقي محور دي.',
      optionExplanations: ['Correct: c = √25 = 5 along the x-axis.', 'Subtracting the squared parameters uses the wrong conic relation.', 'The foci lie on the x-axis for this equation.', 'These are the vertices, not the foci.'], sourceReferences: hyperbola()
    },
    {
      id: 'math12-u9-practice-mcq-09', q: 'Which pair gives the asymptotes of x²/9 − y²/16 = 1?',
      qUrdu: 'x²/9 − y²/16 = 1 کے خطوطِ مقارب کون سے ہیں؟', qPashto: 'د x²/9 − y²/16 = 1 مقاربې کرښې کومې دي؟',
      options: ['y = ±3x/4', 'y = ±5x/3', 'x = ±3', 'y = ±4x/3'], correct: 3,
      answerUrdu: 'y = ±4x/3', answerPashto: 'y = ±4x/3',
      exp: 'For x²/a² − y²/b² = 1, asymptotes are y = ±(b/a)x. Here b/a = 4/3.',
      expUrdu: 'افقی قطع زائد کے خطوطِ مقارب y = ±(b/a)x ہیں؛ یہاں b/a = 4/3 ہے۔',
      expPashto: 'د افقي هایپربولا مقاربې کرښې y = ±(b/a)x دي؛ دلته b/a = 4/3 دی.',
      optionExplanations: ['The ratio a/b is reversed for this horizontal form.', 'c/a is eccentricity, not the asymptote slope.', 'These are the vertical vertex tangents.', 'Correct: the asymptote slopes are ±b/a.'], sourceReferences: hyperbola(268, 272)
    },
    {
      id: 'math12-u9-practice-mcq-10', q: 'What is the eccentricity of x²/9 − y²/16 = 1?',
      qUrdu: 'x²/9 − y²/16 = 1 کی اختلافِ مرکزیت کیا ہے؟', qPashto: 'د x²/9 − y²/16 = 1 خروج له مرکز څخه څومره دی؟',
      options: ['3/5', '5/3', '4/3', '1'], correct: 1,
      answerUrdu: '5/3', answerPashto: '5/3',
      exp: 'a = 3 and c = √(9 + 16) = 5. Hence e = c/a = 5/3 > 1.',
      expUrdu: 'a = 3 اور c = 5 ہیں، اس لیے e = c/a = 5/3 > 1 ہے۔',
      expPashto: 'a = 3 او c = 5 دي؛ نو e = c/a = 5/3 > 1 دی.',
      optionExplanations: ['This is a/c, the reciprocal of the eccentricity.', 'Correct: eccentricity is c/a and exceeds 1.', 'This is b/a, the positive asymptote slope.', 'e = 1 describes a parabola.'], sourceReferences: hyperbola()
    },
    {
      id: 'math12-u9-practice-mcq-11', q: 'Which slope allows real tangents with finite contact points on x²/9 − y²/16 = 1?',
      qUrdu: 'کون سی ڈھلوان x²/9 − y²/16 = 1 پر متناہی نقاطِ تماس رکھنے والے حقیقی مماس دیتی ہے؟',
      qPashto: 'کوم میل پر x²/9 − y²/16 = 1 داسې حقیقي مماسونه ورکوي چې د تماس ټکي یې متناهي وي؟',
      options: ['m = 0', 'm = 1', 'm = 4/3', 'm = 2'], correct: 3,
      answerUrdu: 'm = 2', answerPashto: 'm = 2',
      exp: 'Finite-slope tangents require 9m² − 16 > 0, or |m| > 4/3. The equality case m = 4/3 gives an asymptote, not finite contact.',
      expUrdu: 'متناہی ڈھلوان والے مماس کے لیے 9m² − 16 > 0، یعنی |m| > 4/3 ضروری ہے۔ مساوات m = 4/3 خطِ مقارب دیتی ہے، متناہی تماس نہیں۔',
      expPashto: 'د متناهي میل لرونکي مماس لپاره 9m² − 16 > 0، یعنې |m| > 4/3 پکار دی. m = 4/3 مقاربه کرښه ورکوي، متناهي تماس نه.',
      optionExplanations: ['The radicand is −16, so no real tangent has slope 0.', 'The radicand is −7, so no real tangent has slope 1.', 'The zero-radicand line is an asymptote with no finite contact.', 'Correct: 9(2²) − 16 = 20 > 0 gives two real tangents.'], sourceReferences: hyperbola(272, 274)
    },
    {
      id: 'math12-u9-practice-mcq-12', q: 'What is the center of (y + 1)²/16 − (x − 2)²/9 = 1?',
      qUrdu: '(y + 1)²/16 − (x − 2)²/9 = 1 کا مرکز کیا ہے؟',
      qPashto: 'د (y + 1)²/16 − (x − 2)²/9 = 1 مرکز کوم دی؟',
      options: ['(−2, 1)', '(2, −1)', '(−1, 2)', '(2, 1)'], correct: 1,
      answerUrdu: '(2, −1)', answerPashto: '(2, −1)',
      exp: 'Read x − h = x − 2 and y − k = y + 1. Thus h = 2 and k = −1.',
      expUrdu: 'x − h = x − 2 اور y − k = y + 1 سے h = 2 اور k = −1 ملتے ہیں۔',
      expPashto: 'له x − h = x − 2 او y − k = y + 1 څخه h = 2 او k = −1 کېږي.',
      optionExplanations: ['Both translation signs have been reversed.', 'Correct: the center is (h,k) = (2,−1).', 'Coordinates remain ordered (x,y), even when the y² term is first.', 'The y-shift is −1, not +1.'], sourceReferences: hyperbola(269, 272)
    }
  ];
  const shortQuestions = [
    {
      id: 'math12-u9-practice-short-01', marks: 3,
      q: 'For p > 0, derive y² = 4px from focus F(p,0) and directrix x = −p.',
      qUrdu: 'p > 0 کے لیے فوکس F(p,0) اور خطِ ہادی x = −p سے y² = 4px اخذ کریں۔',
      qPashto: 'د p > 0 لپاره له محراق F(p,0) او هادي کرښې x = −p څخه y² = 4px راوباسئ.',
      sol: 'A point P(x,y) has focus-distance √((x−p)²+y²) and perpendicular directrix-distance |x+p|. Equate them and square: (x−p)²+y²=(x+p)². Cancelling x² and p² gives y²=4px. Both distances are nonnegative, so equality of their squares also recovers equality of the distances.',
      solUrdu: 'نقطہ P(x,y) کا فوکس سے فاصلہ √((x−p)²+y²) اور خطِ ہادی سے عمودی فاصلہ |x+p| ہے۔ دونوں کو برابر رکھ کر مربع کریں: (x−p)²+y²=(x+p)²۔ مشترک حدود حذف کرنے سے y²=4px ملتا ہے۔ دونوں فاصلے غیر منفی ہیں، اس لیے مربعوں کی برابری اصل فاصلوں کی برابری بھی دیتی ہے۔',
      solPashto: 'د P(x,y) ټکي له محراق څخه واټن √((x−p)²+y²) او له هادي کرښې څخه عمودي واټن |x+p| دی. دواړه برابر او مربع کړئ: (x−p)²+y²=(x+p)². د ګډو حدونو له حذفولو y²=4px تر لاسه کېږي. دواړه واټنونه غیر منفي دي؛ نو د مربعونو برابري د واټنونو برابري هم ورکوي.',
      sourceReferences: parabola()
    },
    {
      id: 'math12-u9-practice-short-02', marks: 3,
      q: 'Find the parabola with focus (2,3) and directrix y = −1.',
      qUrdu: 'وہ قطع مکافی معلوم کریں جس کا فوکس (2,3) اور خطِ ہادی y = −1 ہے۔',
      qPashto: 'هغه پارابولا پیدا کړئ چې محراق یې (2,3) او هادي کرښه یې y = −1 وي.',
      sol: 'The axis is x=2. The vertex lies halfway between the focus (2,3) and (2,−1) on the directrix, so V=(2,1). The signed focus distance is p=2. Therefore (x−2)²=8(y−1). Check: the focus is (h,k+p)=(2,3), and the directrix is y=k−p=−1.',
      solUrdu: 'محور x=2 ہے۔ فوکس (2,3) اور خطِ ہادی کے نقطے (2,−1) کا وسط راس V=(2,1) ہے۔ p=2 ہونے سے مساوات (x−2)²=8(y−1) بنتی ہے۔ اس کا فوکس (h,k+p)=(2,3) اور خطِ ہادی y=k−p=−1 ہے۔',
      solPashto: 'محور x=2 دی. د محراق (2,3) او پر هادي کرښه د (2,−1) ټکي منځنی ټکی رأس V=(2,1) دی. p=2 دی؛ نو معادله (x−2)²=8(y−1) ده. محراق یې (h,k+p)=(2,3) او هادي کرښه یې y=k−p=−1 ده.',
      sourceReferences: parabola(243, 245)
    },
    {
      id: 'math12-u9-practice-short-03', marks: 3,
      q: 'For x² = −12y, find the focus and latus-rectum endpoints. Explain why its latus-rectum length is not −12.',
      qUrdu: 'x² = −12y کا فوکس اور وترِ عدسی کے سروں کے نقاط معلوم کریں۔ اس کی لمبائی −12 کیوں نہیں ہے؟',
      qPashto: 'د x² = −12y محراق او د محراقي عمودي وتر پای ټکي پیدا کړئ. ولې یې اوږدوالی −12 نه دی؟',
      sol: 'Since 4p=−12, p=−3 and the focus is (0,−3). The latus rectum lies on y=−3. Substitution gives x²=36, so its endpoints are (−6,−3) and (6,−3). Their distance is 12=4|p|. The sign of p controls the downward opening; a geometric length is nonnegative.',
      solUrdu: '4p=−12 سے p=−3 اور فوکس (0,−3) ہے۔ وترِ عدسی y=−3 پر ہے؛ اس لیے x²=36 اور سرے (−6,−3)، (6,−3) ہیں۔ ان کا فاصلہ 12=4|p| ہے۔ p کی منفی علامت نیچے کھلنے کو ظاہر کرتی ہے، منفی لمبائی کو نہیں۔',
      solPashto: 'له 4p=−12 څخه p=−3 او محراق (0,−3) دی. محراقي وتر پر y=−3 پروت دی؛ نو x²=36 او پای ټکي (−6,−3)، (6,−3) دي. واټن یې 12=4|p| دی. د p منفي نښه ښکته پرانیستل ښيي؛ هندسي اوږدوالی منفي نه وي.',
      sourceReferences: parabola()
    },
    {
      id: 'math12-u9-practice-short-04', marks: 3,
      q: 'Find the foci, eccentricity and constant focal-distance difference for x²/9 − y²/16 = 1.',
      qUrdu: 'x²/9 − y²/16 = 1 کے فوکس، اختلافِ مرکزیت اور فوکسوں سے فاصلوں کے فرق کی مستقل مقدار معلوم کریں۔',
      qPashto: 'د x²/9 − y²/16 = 1 محراقونه، خروج له مرکز څخه او له محراقونو د واټنونو د توپیر ثابته اندازه پیدا کړئ.',
      sol: 'a=3, b=4, and c=√(a²+b²)=5. Hence the foci are (−5,0),(5,0), eccentricity is e=c/a=5/3, and |PF₁−PF₂|=2a=6 for every point P on either branch. The absolute value is needed because the signed difference changes between branches.',
      solUrdu: 'a=3، b=4 اور c=√(a²+b²)=5 ہیں۔ لہٰذا فوکس (−5,0)، (5,0)، اختلافِ مرکزیت e=5/3 اور ہر شاخ کے نقطے کے لیے |PF₁−PF₂|=2a=6 ہے۔ مطلق قدر ضروری ہے کیونکہ شاخ بدلنے سے فرق کی علامت بدل جاتی ہے۔',
      solPashto: 'a=3، b=4 او c=√(a²+b²)=5 دي. نو محراقونه (−5,0)، (5,0)، خروج له مرکز څخه e=5/3 او د هرې څانګې د ټکي لپاره |PF₁−PF₂|=2a=6 دي. مطلق قیمت اړین دی، ځکه د څانګې په بدلېدو د توپیر نښه بدلېږي.',
      sourceReferences: hyperbola(265, 269)
    },
    {
      id: 'math12-u9-practice-short-05', marks: 3,
      q: 'Why is y = 4x/3 not a tangent with a finite contact point on x²/9 − y²/16 = 1?',
      qUrdu: 'y = 4x/3، قطع زائد x²/9 − y²/16 = 1 کا متناہی نقطۂ تماس رکھنے والا مماس کیوں نہیں ہے؟',
      qPashto: 'ولې y = 4x/3 د x²/9 − y²/16 = 1 داسې مماس نه دی چې متناهي تماس ولري؟',
      sol: 'Substitute y=4x/3: x²/9−(16x²/9)/16=0, so the equation would require 0=1. There is no finite intersection. This line is an asymptote. For y=mx+q to have a real finite tangent contact, q²=9m²−16 must be strictly positive; equality produces an asymptote. Vertical tangents x=±3 are handled separately.',
      solUrdu: 'y=4x/3 رکھنے سے بائیں طرف صفر بنتا ہے، یعنی 0=1 درکار ہوگا؛ اس لیے کوئی متناہی تقاطع نہیں۔ یہ خطِ مقارب ہے۔ حقیقی متناہی تماس کے لیے q²=9m²−16>0 ہونا ضروری ہے۔ برابری کی صورت خطِ مقارب دیتی ہے۔ عمودی مماس x=±3 الگ صورت ہیں۔',
      solPashto: 'د y=4x/3 په ایښودلو چپ لوری صفر کېږي او 0=1 ته اړتیا پیدا کېږي؛ نو متناهي تقاطع نشته. دا مقاربه کرښه ده. د حقیقي متناهي تماس لپاره q²=9m²−16>0 پکار دی. د برابرۍ حالت مقاربه کرښه ورکوي. عمودي مماسونه x=±3 جلا حالتونه دي.',
      sourceReferences: hyperbola(272, 274)
    },
    {
      id: 'math12-u9-practice-short-06', marks: 4,
      q: 'Find the normal to x²/9 − y²/16 = 1 at P=(5,16/3), checking first that P is on the hyperbola.',
      qUrdu: 'P=(5,16/3) پر x²/9 − y²/16 = 1 کا عمودی خط معلوم کریں۔ پہلے تصدیق کریں کہ P قطع زائد پر ہے۔',
      qPashto: 'په P=(5,16/3) کې د x²/9 − y²/16 = 1 نورمال پیدا کړئ. لومړی تایید کړئ چې P پر هایپربولا دی.',
      sol: 'At P, 25/9−(256/9)/16=25/9−16/9=1, so it is on the curve. Implicit differentiation gives y′=16x/(9y), hence the tangent slope is 5/3. The normal slope is −3/5. Thus y−16/3=−(3/5)(x−5), or 9x+15y=125.',
      solUrdu: 'P پر 25/9−16/9=1 ہے، اس لیے نقطہ منحنی پر ہے۔ تفریق سے y′=16x/(9y) ملتا ہے؛ لہٰذا مماس کی ڈھلوان 5/3 اور عمودی خط کی −3/5 ہے۔ مساوات y−16/3=−(3/5)(x−5)، یعنی 9x+15y=125 ہے۔',
      solPashto: 'په P کې 25/9−16/9=1 دی؛ نو ټکی پر منحني دی. مشتق y′=16x/(9y) ورکوي؛ د مماس میل 5/3 او د نورمال میل −3/5 دی. معادله y−16/3=−(3/5)(x−5)، یعنې 9x+15y=125 ده.',
      sourceReferences: hyperbola(274, 276)
    }
  ];
  const longQuestions = [
    {
      id: 'math12-u9-practice-long-01', marks: 8,
      q: 'For (y + 1)² = −12(x − 2), find the vertex, focus, directrix, axis, latus-rectum endpoints and length. Then find the tangent and normal at P=(−1,5).',
      qUrdu: '(y + 1)² = −12(x − 2) کے راس، فوکس، خطِ ہادی، محور، وترِ عدسی کے سرے اور لمبائی معلوم کریں۔ پھر P=(−1,5) پر مماس اور عمودی خط معلوم کریں۔',
      qPashto: 'د (y + 1)² = −12(x − 2) رأس، محراق، هادي کرښه، محور، د محراقي وتر پای ټکي او اوږدوالی پیدا کړئ. بیا په P=(−1,5) کې مماس او نورمال پیدا کړئ.',
      steps: [
        'Compare (y−k)²=4p(x−h): h=2, k=−1, p=−3. Therefore the vertex is (2,−1), the axis is y=−1, and the parabola opens left.',
        'The focus is (h+p,k)=(−1,−1). The directrix is x=h−p=5.',
        'The latus rectum passes through the focus perpendicular to the axis, so x=−1. Substitution gives (y+1)²=36, hence y=5 or −7.',
        'Its endpoints are (−1,5) and (−1,−7); their distance is 12=4|p|. In particular, the requested point P lies on the curve.',
        'Differentiate implicitly: 2(y+1)y′=−12. At P, y′=−12/12=−1.',
        'The tangent through P is y−5=−(x+1), giving x+y−4=0.',
        'The perpendicular normal has slope 1: y−5=x+1, giving y=x+6.',
        'Check the tangent algebraically: substitute y=4−x into the curve. Then (5−x)²=−12x+24, so (x+1)²=0, giving the repeated contact x=−1, y=5.'
      ],
      answer: 'V=(2,−1), F=(−1,−1), directrix x=5, axis y=−1; latus endpoints (−1,5),(−1,−7), length 12; tangent x+y−4=0; normal y=x+6.',
      solUrdu: 'معیاری صورت سے h=2، k=−1، p=−3 ہیں۔ راس (2,−1)، فوکس (h+p,k)=(−1,−1)، خطِ ہادی x=h−p=5 اور محور y=−1 ہے۔ وترِ عدسی پر x=−1 رکھنے سے (y+1)²=36 ملتا ہے؛ اس لیے سرے (−1,5)، (−1,−7) اور لمبائی 12 ہیں۔ تفریق سے 2(y+1)y′=−12؛ P پر ڈھلوان −1 ہے۔ مماس y−5=−(x+1)، یعنی x+y−4=0 ہے۔ عمودی خط کی ڈھلوان 1 اور مساوات y=x+6 ہے۔ مماس کو منحنی میں رکھنے سے (x+1)²=0 ملتا ہے، جو دوہرا تماس ثابت کرتا ہے۔',
      solPashto: 'له معیاري بڼې h=2، k=−1، p=−3 دي. رأس (2,−1)، محراق (h+p,k)=(−1,−1)، هادي کرښه x=h−p=5 او محور y=−1 دی. پر محراقي وتر x=−1 ایښودل (y+1)²=36 ورکوي؛ نو پای ټکي (−1,5)، (−1,−7) او اوږدوالی 12 دی. مشتق 2(y+1)y′=−12 دی؛ په P کې میل −1 دی. مماس y−5=−(x+1)، یعنې x+y−4=0 دی. د نورمال میل 1 او معادله y=x+6 ده. د مماس په ځای کولو (x+1)²=0 تر لاسه کېږي، چې دوه ګونی تماس تاییدوي.',
      sourceReferences: parabola(243, 249)
    },
    {
      id: 'math12-u9-practice-long-02', marks: 8,
      q: 'A hyperbola has center (1,−2), vertices (−2,−2),(4,−2), and foci (−4,−2),(6,−2). Find its equation, eccentricity, asymptotes and latus-rectum length, then describe its sketch.',
      qUrdu: 'ایک قطع زائد کا مرکز (1,−2)، راس (−2,−2)، (4,−2) اور فوکس (−4,−2)، (6,−2) ہیں۔ اس کی مساوات، اختلافِ مرکزیت، خطوطِ مقارب اور وترِ عدسی کی لمبائی معلوم کریں، پھر خاکے کی وضاحت کریں۔',
      qPashto: 'د یوې هایپربولا مرکز (1,−2)، رأسونه (−2,−2)، (4,−2) او محراقونه (−4,−2)، (6,−2) دي. معادله، خروج له مرکز څخه، مقاربې کرښې او د محراقي وتر اوږدوالی پیدا او بڼه یې تشریح کړئ.',
      steps: [
        'All vertices and foci share y=−2, so the transverse axis is horizontal through the center (h,k)=(1,−2).',
        'The center-to-vertex distance is a=3. The center-to-focus distance is c=5.',
        'For a hyperbola, c²=a²+b². Thus b²=25−9=16 and b=4.',
        'The equation is (x−1)²/9−(y+2)²/16=1. Its eccentricity is e=c/a=5/3.',
        'The asymptotes through the center are y+2=±(4/3)(x−1).',
        'At the right focus’s x-coordinate x=6, (x−1)²/9=25/9. The curve gives (y+2)²=256/9, so y=−2±16/3.',
        'The latus rectum therefore has length 32/3, agreeing with 2b²/a=32/3. The left focal chord has the same length.',
        'For the sketch, mark the center and vertices, draw the two asymptotes, and draw branches opening left and right from the vertices. The branches approach the asymptotes but have no finite intersection with them.'
      ],
      answer: '(x−1)²/9−(y+2)²/16=1; e=5/3; asymptotes y+2=±(4/3)(x−1); each latus rectum has length 32/3.',
      solUrdu: 'حقیقی محور y=−2 افقی ہے۔ مرکز سے راس کا فاصلہ a=3 اور فوکس کا c=5 ہے۔ c²=a²+b² سے b²=16 ملتا ہے۔ مساوات (x−1)²/9−(y+2)²/16=1 اور اختلافِ مرکزیت e=5/3 ہے۔ خطوطِ مقارب y+2=±(4/3)(x−1) ہیں۔ x=6 رکھنے پر y=−2±16/3، لہٰذا وترِ عدسی کی لمبائی 32/3 ہے، جو 2b²/a کے برابر ہے۔ خاکے میں مرکز، راس اور خطوطِ مقارب نشان لگائیں؛ دونوں شاخیں بائیں اور دائیں کھلتی اور خطوطِ مقارب کے قریب جاتی ہیں۔',
      solPashto: 'حقیقي محور y=−2 افقي دی. له مرکز څخه تر رأسه واټن a=3 او تر محراقه c=5 دی. له c²=a²+b² څخه b²=16 کېږي. معادله (x−1)²/9−(y+2)²/16=1 او خروج له مرکز څخه e=5/3 دی. مقاربې کرښې y+2=±(4/3)(x−1) دي. د x=6 په ایښودلو y=−2±16/3 کېږي؛ نو د محراقي وتر اوږدوالی 32/3 دی، چې له 2b²/a سره برابر دی. مرکز، رأسونه او مقاربې کرښې رسم کړئ؛ څانګې چپ او ښي لوري ته پرانیستل کېږي او مقاربو ته نږدې کېږي.',
      sourceReferences: hyperbola(266, 272)
    },
    {
      id: 'math12-u9-practice-long-03', marks: 8,
      q: 'Find both tangents of slope 2 to x²/9 − y²/16 = 1 and their contact points. Verify that each contact lies on the curve and its tangent.',
      qUrdu: 'x²/9 − y²/16 = 1 کے ڈھلوان 2 والے دونوں مماس اور ان کے نقاطِ تماس معلوم کریں۔ تصدیق کریں کہ ہر نقطہ منحنی اور اپنے مماس پر ہے۔',
      qPashto: 'د x²/9 − y²/16 = 1 هغه دواړه مماسونه او د تماس ټکي پیدا کړئ چې میل یې 2 وي. تایید کړئ چې هر ټکی پر منحني او خپل مماس پروت دی.',
      steps: [
        'Write the line as y=2x+q. The finite-contact condition for x²/a²−y²/b²=1 is q²=a²m²−b²>0.',
        'Here a²=9, b²=16 and m=2, so q²=9·4−16=20. Thus the lines are y=2x+2√5 and y=2x−2√5.',
        'Differentiate the hyperbola: y′=16x/(9y). At a slope-2 contact, 16x/(9y)=2, so y=8x/9.',
        'Substitute this relation into the hyperbola: x²/9−(64x²/81)/16=1. Hence 5x²/81=1 and x=±9/√5, y=±8/√5 with matching signs.',
        'At P₊=(9/√5,8/√5), the intercept is y−2x=−10/√5=−2√5. Hence P₊ belongs to y=2x−2√5.',
        'At P₋=(−9/√5,−8/√5), the intercept is +2√5. Hence P₋ belongs to y=2x+2√5.',
        'For either point, x²/9=9/5 and y²/16=4/5; their difference is 1. Both contact points lie on the hyperbola, and the derivative at either is 2.',
        'The strict condition holds because 20>0. In contrast, the asymptote slope 4/3 makes the radicand zero and has no finite contact; it is not an additional solution to this question.'
      ],
      answer: 'y=2x−2√5 at (9/√5,8/√5); y=2x+2√5 at (−9/√5,−8/√5).',
      solUrdu: 'مماس y=2x+q لکھیں۔ شرط q²=a²m²−b²=9·4−16=20 سے q=±2√5 ہے۔ اس لیے دونوں مماس y=2x±2√5 ہیں۔ تفریق سے y′=16x/(9y)؛ اسے 2 کے برابر رکھیں تو y=8x/9 ملتا ہے۔ منحنی میں رکھنے سے 5x²/81=1، یعنی x=±9/√5 اور y=±8/√5 ہیں، جن کی علامات یکساں ہیں۔ مثبت نقطے پر q=−2√5 اور منفی نقطے پر q=2√5 ہے۔ دونوں نقاط کے لیے x²/9−y²/16=9/5−4/5=1 اور ڈھلوان 2 ہے، اس لیے دونوں جواب تصدیق شدہ ہیں۔',
      solPashto: 'مماس y=2x+q ولیکئ. له شرط q²=a²m²−b²=9·4−16=20 څخه q=±2√5 دی؛ نو مماسونه y=2x±2√5 دي. مشتق y′=16x/(9y) له 2 سره برابر کړئ؛ y=8x/9 تر لاسه کېږي. په منحني کې یې ایښودل 5x²/81=1 ورکوي، یعنې x=±9/√5 او y=±8/√5 له یو ډول نښو سره دي. په مثبت ټکي کې q=−2√5 او په منفي ټکي کې q=2√5 دی. د دواړو لپاره x²/9−y²/16=9/5−4/5=1 او میل 2 دی؛ نو دواړه ځوابونه تایید شول.',
      sourceReferences: hyperbola(272, 275)
    }
  ];
  function appendUnique(key, records) {
    const target = chapter.slos[key] || (chapter.slos[key] = []);
    for (const item of records) {
      if (target.some(existing => existing.id === item.id)) continue;
      item.origin = origin;
      item.source = origin;
      item.isSupplementary = true;
      item.sourceStatus = 'authored_practice_based_on_reviewed_topics';
      if (key === 'mcqs') {
        item.answer = item.options[item.correct];
      } else {
        if (item.steps) item.sol = item.steps.join('\n');
        item.answer = item.answer || item.sol;
        item.answerUrdu = item.solUrdu;
        item.answerPashto = item.solPashto;
      }
      target.push(item);
    }
  }
  appendUnique('mcqs', mcqs);
  appendUnique('shortQuestions', shortQuestions);
  appendUnique('longQuestions', longQuestions);
})();
