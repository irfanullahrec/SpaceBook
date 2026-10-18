// Reviewed Unit 4 source-section translations. English/formulas remain unchanged.
(function () {
  'use strict';
  if(typeof MATH_12_DATA==='undefined'||typeof MATH12_SENTENCE_TRANSLATIONS==='undefined')return;
  const authored =
{
  "Introduction": [
    "تعارف",
    "پېژندنه"
  ],
  "Solution": [
    "حل",
    "حل"
  ],
  "Remember": [
    "یاد رکھیں",
    "په یاد ولرئ"
  ],
  "Command": [
    "کمانڈ",
    "قومنده"
  ],
  "The higher order derivatives has useful physical interpretation. If y = f(t) is the position of an object at time t then \\(\\frac{dy}{dt}=f′(t)\\) is its velocity at time t and \\(\\frac{d^2y}{dt^2}\\) is its acceleration at time t.": [
    "اعلیٰ درجے کے مشتقات کی مفید طبعی تعبیر ہے۔ اگر y = f(t) وقت t پر کسی جسم کا مقام ہو تو \\(\\frac{dy}{dt}=f′(t)\\) وقت t پر اس کی سمتی رفتار اور \\(\\frac{d^2y}{dt^2}\\) وقت t پر اس کا اسراع ہے۔",
    "د لوړو مرتبو مشتقونه ګټوره فزیکي مانا لري. که y = f(t) په وخت t کې د یوه جسم موقعیت وي، نو \\(\\frac{dy}{dt}=f′(t)\\) په وخت t کې د هغه سرعت او \\(\\frac{d^2y}{dt^2}\\) په وخت t کې د هغه تعجیل دی."
  ],
  "According to the Newton’s law of motion “The acceleration of an object is proportional to the total force acting on it”. So, the second order derivatives has importance in mechanics. The second order derivatives is also important to graph the functions. Now, in this unit we will learn in details about higher order differentiation and its applications.": [
    "نیوٹن کے قانونِ حرکت کے مطابق ”کسی جسم کا اسراع اس پر لگنے والی کل قوت کے متناسب ہوتا ہے“۔ اس لیے دوسرے درجے کے مشتقات میکانیات میں اہم ہیں۔ دوسرے درجے کے مشتقات تفاعلوں کے گراف بنانے میں بھی اہم ہیں۔ اب اس اکائی میں ہم اعلیٰ درجے کی تفریق اور اس کے اطلاقات تفصیل سے پڑھیں گے۔",
    "د نیوټن د حرکت د قانون له مخې «د یوه جسم تعجیل پر هغه د واردې ټولې قوې متناسب دی». نو د دویمې مرتبې مشتقونه په میخانیک کې اهمیت لري. د دویمې مرتبې مشتقونه د تابع ګانو د ګرافونو لپاره هم مهم دي. اوس به په دې څپرکي کې د لوړو مرتبو تفریق او د هغه کارونې په تفصیل زده کړو."
  ],
  "4.1 Higher order derivatives": [
    "4.1 اعلیٰ درجے کے مشتقات",
    "4.1 د لوړو مرتبو مشتقونه"
  ],
  "If a function y = f(x) has a first derivative y′, then the derivative of y′, if it exists, is the second derivative of y = f(x), written as y″. The derivative of y″, if it exists, is called the third derivative of y = f(x), written as y‴. By continuing this process, we can find fourth derivative and other higher derivatives.": [
    "اگر تفاعل y = f(x) کا پہلا مشتق y′ موجود ہو تو y′ کا مشتق، بشرطِ وجود، y = f(x) کا دوسرا مشتق کہلاتا ہے اور y″ لکھا جاتا ہے۔ y″ کا مشتق، بشرطِ وجود، y = f(x) کا تیسرا مشتق کہلاتا ہے اور y‴ لکھا جاتا ہے۔ اس عمل کو جاری رکھ کر چوتھا اور دیگر اعلیٰ درجے کے مشتقات معلوم کیے جا سکتے ہیں۔",
    "که د y = f(x) تابع لومړی مشتق y′ ولري، نو د y′ مشتق، که موجود وي، د y = f(x) دویم مشتق دی او y″ لیکل کېږي. د y″ مشتق، که موجود وي، د y = f(x) درېیم مشتق بلل کېږي او y‴ لیکل کېږي. د دې بهیر په دوام څلورم او نور لوړ مشتقونه موندلای شو."
  ],
  "For example, if \\(f(x)=x^4+2x^3+3x^2-5x+7\\), then the higher derivatives are the following:": [
    "مثلاً اگر \\(f(x)=x^4+2x^3+3x^2-5x+7\\) ہو تو اعلیٰ درجے کے مشتقات درج ذیل ہیں:",
    "د بېلګې په توګه، که \\(f(x)=x^4+2x^3+3x^2-5x+7\\) وي، نو لوړ مشتقونه یې په لاندې ډول دي:"
  ],
  "Find the second derivative of the following functions: (a) \\(f(x)=8x^3-9x^2+6x+4\\); (b) \\(f(x)=\\frac{4x+2}{3x-1}\\).": [
    "درج ذیل تفاعلوں کے دوسرے مشتقات معلوم کریں: (a) \\(f(x)=8x^3-9x^2+6x+4\\)؛ (b) \\(f(x)=\\frac{4x+2}{3x-1}\\)۔",
    "د لاندې تابع ګانو دویم مشتقونه ومومئ: (a) \\(f(x)=8x^3-9x^2+6x+4\\)؛ (b) \\(f(x)=\\frac{4x+2}{3x-1}\\)."
  ],
  "a. If the given function is \\(f(x)=8x^3-9x^2+6x+4\\), then the first and second derivatives of the given function through linearity property are the following:": [
    "a. اگر دیا گیا تفاعل \\(f(x)=8x^3-9x^2+6x+4\\) ہو تو خطیت کی خاصیت سے اس کے پہلے اور دوسرے مشتقات درج ذیل ہیں:",
    "a. که ورکړل شوې تابع \\(f(x)=8x^3-9x^2+6x+4\\) وي، نو د خطیت د خاصیت له مخې یې لومړی او دویم مشتقونه داسې دي:"
  ],
  "The second derivative of y = f(x) can be written with any of the following notations:": [
    "y = f(x) کا دوسرا مشتق درج ذیل میں سے کسی بھی علامتی صورت میں لکھا جا سکتا ہے:",
    "د y = f(x) دویم مشتق په لاندې هرې یوې نښې لیکل کېدای شي:"
  ],
  "The third derivative can be written in a similar way. For n ≥ 4, the derivative holds the notation f⁽ⁿ⁾(x), n = 4,5,...": [
    "تیسرا مشتق بھی اسی طرح لکھا جا سکتا ہے۔ n ≥ 4 کے لیے مشتق کی علامت f⁽ⁿ⁾(x) ہے، جہاں n = 4,5,... ہے۔",
    "درېیم مشتق هم په ورته ډول لیکل کېدای شي. د n ≥ 4 لپاره د مشتق نښه f⁽ⁿ⁾(x) ده، چې n = 4,5,... دی."
  ],
  "b. If the given function is \\(f(x)=y=\\frac uv=\\frac{4x+2}{3x-1}\\), then the first and second derivatives of the given function through quotient rule are the following:": [
    "b. اگر دیا گیا تفاعل \\(f(x)=y=\\frac uv=\\frac{4x+2}{3x-1}\\) ہو تو حاصلِ تقسیم کے قاعدے سے اس کے پہلے اور دوسرے مشتقات درج ذیل ہیں:",
    "b. که ورکړل شوې تابع \\(f(x)=y=\\frac uv=\\frac{4x+2}{3x-1}\\) وي، نو د حاصل قسمت د قاعدې له مخې یې لومړی او دویم مشتقونه داسې دي:"
  ],
  "In the previous unit, we saw that the first derivative of a function represents the rate of change of the function. The second derivative, then, represents the rate of change of the first derivative. If a function describes the position of a moving object at time t, then the first derivative gives the velocity of the object. That is, if y = s(t) describes the position of the object at time t, then v(t) = s′(t) gives the velocity at a time t.": [
    "پچھلی اکائی میں ہم نے دیکھا کہ تفاعل کا پہلا مشتق اس تفاعل کی تبدیلی کی شرح ظاہر کرتا ہے۔ لہٰذا دوسرا مشتق پہلے مشتق کی تبدیلی کی شرح ظاہر کرتا ہے۔ اگر کوئی تفاعل وقت t پر متحرک جسم کا مقام بیان کرے تو پہلا مشتق جسم کی سمتی رفتار دیتا ہے۔ یعنی اگر y = s(t) وقت t پر جسم کا مقام بیان کرے تو v(t) = s′(t) وقت t پر اس کی سمتی رفتار ہے۔",
    "په تېر څپرکي کې مو ولیدل چې د تابع لومړی مشتق د هغې د بدلون کچه ښيي. دویم مشتق بیا د لومړي مشتق د بدلون کچه ښيي. که تابع په وخت t کې د خوځنده جسم موقعیت بیان کړي، نو لومړی مشتق یې سرعت راکوي. یعنې که y = s(t) په وخت t کې د جسم موقعیت بیانوي، نو v(t) = s′(t) په وخت t کې د هغه سرعت دی."
  ],
  "The rate of change of velocity is called acceleration. Since the second derivative gives the rate of change of the first derivative, the acceleration is the derivative of the velocity. Thus, if a(t) represents the acceleration at time t, then": [
    "سمتی رفتار کی تبدیلی کی شرح کو اسراع کہتے ہیں۔ چونکہ دوسرا مشتق پہلے مشتق کی تبدیلی کی شرح دیتا ہے، اس لیے اسراع سمتی رفتار کا مشتق ہے۔ لہٰذا اگر a(t) وقت t پر اسراع ظاہر کرے تو",
    "د سرعت د بدلون کچه تعجیل بلل کېږي. ځکه چې دویم مشتق د لومړي مشتق د بدلون کچه ورکوي، نو تعجیل د سرعت مشتق دی. نو که a(t) په وخت t کې تعجیل ښيي، بیا"
  ],
  "An object is moving along a straight line with its position s(t) (in feet) at time t (in seconds): \\(s(t)=t^3-2t^2-7t+9\\). (a) Find the velocity at any time t. (b) Find the acceleration at any time t. (c) The object stops when velocity is zero. For t ≥ 0, when does that occur?": [
    "ایک جسم سیدھی لکیر پر حرکت کر رہا ہے اور وقت t (سیکنڈ) پر اس کا مقام s(t) (فٹ) ہے: \\(s(t)=t^3-2t^2-7t+9\\)۔ (a) کسی بھی وقت t پر سمتی رفتار معلوم کریں۔ (b) کسی بھی وقت t پر اسراع معلوم کریں۔ (c) جسم اس وقت رکتا ہے جب سمتی رفتار صفر ہو۔ t ≥ 0 کے لیے یہ کب ہوتا ہے؟",
    "یو جسم پر مستقیمه کرښه خوځېږي او په وخت t (ثانیو) کې یې موقعیت s(t) (فوټو) دی: \\(s(t)=t^3-2t^2-7t+9\\). (a) په هر وخت t کې سرعت ومومئ. (b) په هر وخت t کې تعجیل ومومئ. (c) جسم هغه وخت درېږي چې سرعت صفر شي. د t ≥ 0 لپاره دا کله پېښېږي؟"
  ],
  "a. The velocity at any time t is the first derivative of s(t) w.r.t. t:": [
    "a. کسی بھی وقت t پر سمتی رفتار، t کے لحاظ سے s(t) کا پہلا مشتق ہے:",
    "a. په هر وخت t کې سرعت د t په نسبت د s(t) لومړی مشتق دی:"
  ],
  "b. The acceleration at any time t is the first derivative of v(t) w.r.t. t:": [
    "b. کسی بھی وقت t پر اسراع، t کے لحاظ سے v(t) کا پہلا مشتق ہے:",
    "b. په هر وخت t کې تعجیل د t په نسبت د v(t) لومړی مشتق دی:"
  ],
  "c. Use v(t) = 0 to obtain the time:": [
    "c. وقت معلوم کرنے کے لیے v(t) = 0 استعمال کریں:",
    "c. د وخت د موندلو لپاره v(t) = 0 وکاروئ:"
  ],
  "The object will stop at 7/3 seconds, since we want time t ≥ 0.": [
    "جسم 7/3 سیکنڈ پر رکے گا، کیونکہ ہمیں t ≥ 0 درکار ہے۔",
    "جسم په 7/3 ثانیو کې درېږي، ځکه موږ t ≥ 0 غواړو."
  ],
  "In Example 1(b), the original function and both derivatives exclude x = 1/3. In Example 2, the zero velocity is an instantaneous stop: for t ≥ 0, velocity is negative before 7/3 and positive afterward, so the model describes a reversal of direction.": [
    "مثال 1(b) میں اصل تفاعل اور دونوں مشتقات کے لیے x = 1/3 خارج ہے۔ مثال 2 میں صفر سمتی رفتار لمحاتی توقف ہے: t ≥ 0 کے لیے سمتی رفتار 7/3 سے پہلے منفی اور اس کے بعد مثبت ہے، اس لیے ماڈل سمت کی تبدیلی ظاہر کرتا ہے۔",
    "په بېلګه 1(b) کې اصلي تابع او دواړه مشتقونه x = 1/3 نه رانغاړي. په بېلګه 2 کې صفر سرعت یوه شېبه درېدل دي: د t ≥ 0 لپاره سرعت تر 7/3 مخکې منفي او وروسته مثبت دی، نو موډل د لوري اوښتل ښيي."
  ],
  "4.1.1 Higher order derivatives of algebraic, trigonometric, exponential and logarithmic functions": [
    "4.1.1 الجبرائی، مثلثی، قوت نمائی اور لوگارتھمی تفاعلوں کے اعلیٰ درجے کے مشتقات",
    "4.1.1 د الجبري، مثلثاتي، نمایي او لوګاریتمي تابع ګانو د لوړو مرتبو مشتقونه"
  ],
  "The successive derivatives of some functions are gathered to obtain the general form of nth derivatives in the following cases:": [
    "درج ذیل صورتوں میں nویں مشتق کی عمومی صورت حاصل کرنے کے لیے بعض تفاعلوں کے پے در پے مشتقات جمع کیے گئے ہیں:",
    "په لاندې حالتونو کې د nم مشتق د عمومي بڼې د ترلاسه کولو لپاره د ځینو تابع ګانو پرله پسې مشتقونه راټول شوي دي:"
  ],
  "i. The nth derivative of f(x) = (ax + b)ᵐ": [
    "i. f(x) = (ax + b)ᵐ کا nواں مشتق",
    "i. د f(x) = (ax + b)ᵐ تابع nم مشتق"
  ],
  "If f(x) = (ax + b)ᵐ, m is positive integer, then the successive derivatives of the given function developed a general term for the nth derivative of a function:": [
    "اگر f(x) = (ax + b)ᵐ ہو اور m مثبت صحیح عدد ہو تو دیے گئے تفاعل کے پے در پے مشتقات اس کے nویں مشتق کی عمومی حد دیتے ہیں:",
    "که f(x) = (ax + b)ᵐ وي او m مثبت صحیح عدد وي، نو د ورکړل شوې تابع پرله پسې مشتقونه د هغې د nم مشتق عمومي جمله راکوي:"
  ],
  "If m = −1, then the nth derivative of \\(f(x)=\\frac1{ax+b}\\) is obtained by inserting m = −1 in equation (i):": [
    "اگر m = −1 ہو تو مساوات (i) میں m = −1 رکھنے سے \\(f(x)=\\frac1{ax+b}\\) کا nواں مشتق ملتا ہے:",
    "که m = −1 وي، نو په (i) معادله کې د m = −1 په اېښودلو د \\(f(x)=\\frac1{ax+b}\\) تابع nم مشتق ترلاسه کېږي:"
  ],
  "ii. The nth derivative of f(x) = ln(ax + b)": [
    "ii. f(x) = ln(ax + b) کا nواں مشتق",
    "ii. د f(x) = ln(ax + b) تابع nم مشتق"
  ],
  "If f(x) = ln(ax + b), then the successive derivatives developed a general term for the nth derivative of a function:": [
    "اگر f(x) = ln(ax + b) ہو تو پے در پے مشتقات تفاعل کے nویں مشتق کی عمومی حد دیتے ہیں:",
    "که f(x) = ln(ax + b) وي، نو پرله پسې مشتقونه د تابع د nم مشتق عمومي جمله راکوي:"
  ],
  "iii. The nth derivative of f(x) = aᵐˣ": [
    "iii. f(x) = aᵐˣ کا nواں مشتق",
    "iii. د f(x) = aᵐˣ تابع nم مشتق"
  ],
  "If f(x) = aᵐˣ, then the successive derivatives developed a general term for the nth derivative:": [
    "اگر f(x) = aᵐˣ ہو تو پے در پے مشتقات nویں مشتق کی عمومی حد دیتے ہیں:",
    "که f(x) = aᵐˣ وي، نو پرله پسې مشتقونه د nم مشتق عمومي جمله راکوي:"
  ],
  "Here n is a positive integer. For a polynomial degree m, the factorial formula applies for n ≤ m; when n > m, the derivative is zero and (m − n)! is not defined. The reciprocal formula requires ax + b ≠ 0; the real logarithm requires ax + b > 0. The real exponential requires a > 0, with m constant. The exponential derivation continues on page 104.": [
    "یہاں n مثبت صحیح عدد ہے۔ درجۂ m کی کثیرالحدی کے لیے عاملیہ والا فارمولا n ≤ m پر لاگو ہوتا ہے؛ n > m پر مشتق صفر ہوتا ہے اور (m − n)! معین نہیں ہوتا۔ معکوس والے فارمولے کے لیے ax + b ≠ 0 ضروری ہے؛ حقیقی لوگارتھم کے لیے ax + b > 0 ضروری ہے۔ حقیقی قوت نمائی تفاعل میں a > 0 اور m مستقل ہونا چاہیے۔ قوت نمائی تفاعل کا اخذ صفحہ 104 پر جاری ہے۔",
    "دلته n مثبت صحیح عدد دی. د m درجې کثیرالحدي لپاره د فکټوریل فورمول پر n ≤ m تطبیقېږي؛ کله چې n > m وي، مشتق صفر دی او (m − n)! تعریف شوی نه دی. د معکوس فورمول ax + b ≠ 0 غواړي؛ حقیقي لوګاریتم ax + b > 0 غواړي. حقیقي نمایي تابع a > 0 او ثابت m غواړي. د نمایي تابع استنتاج په 104 پاڼه کې دوام لري."
  ],
  "Exponential nth derivative — continued": [
    "قوت نمائی تفاعل کا nواں مشتق — جاری",
    "د نمایي تابع nم مشتق — دوام"
  ],
  "If a = e, then the nth derivative of \\(f(x)=e^{mx}\\) is obtained by inserting a = e:": [
    "اگر a = e ہو تو a = e رکھنے سے \\(f(x)=e^{mx}\\) کا nواں مشتق حاصل ہوتا ہے:",
    "که a = e وي، نو د a = e په اېښودلو د \\(f(x)=e^{mx}\\) تابع nم مشتق ترلاسه کېږي:"
  ],
  "iv. The nth derivative of f(x) = sin(ax + b)": [
    "iv. f(x) = sin(ax + b) کا nواں مشتق",
    "iv. د f(x) = sin(ax + b) تابع nم مشتق"
  ],
  "If f(x) = sin(ax + b), then the successive derivatives developed a general term for the nth derivative of a function:": [
    "اگر f(x) = sin(ax + b) ہو تو پے در پے مشتقات تفاعل کے nویں مشتق کی عمومی حد دیتے ہیں:",
    "که f(x) = sin(ax + b) وي، نو پرله پسې مشتقونه د تابع د nم مشتق عمومي جمله راکوي:"
  ],
  "The printed intermediate cos term in the third derivative has coefficient a². Differentiating the second derivative multiplies by a again, so this coefficient should be a³; the final sine term and general nth-derivative formula are correct.": [
    "تیسرے مشتق کی مطبوعہ درمیانی cos حد کا عددی سر a² ہے۔ دوسرے مشتق کی تفریق سے دوبارہ a کی ضرب آتی ہے، اس لیے یہ عددی سر a³ ہونا چاہیے؛ آخری sine حد اور عمومی nویں مشتق کا فارمولا درست ہیں۔",
    "د درېیم مشتق په چاپ شوې منځنۍ cos جمله کې ضریب a² دی. د دویم مشتق په تفریق کې بیا په a ضربېږي، نو دا ضریب باید a³ وي؛ وروستۍ sine جمله او د عمومي nم مشتق فورمول سم دي."
  ],
  "v. The nth derivative of f(x) = cos(ax + b)": [
    "v. f(x) = cos(ax + b) کا nواں مشتق",
    "v. د f(x) = cos(ax + b) تابع nم مشتق"
  ],
  "If f(x) = cos(ax + b), then the successive derivatives developed a general term for the n-th derivative of a function:": [
    "اگر f(x) = cos(ax + b) ہو تو پے در پے مشتقات تفاعل کے nویں مشتق کی عمومی حد دیتے ہیں:",
    "که f(x) = cos(ax + b) وي، نو پرله پسې مشتقونه د تابع د nم مشتق عمومي جمله راکوي:"
  ],
  "Find the 5th derivatives of the following functions: (a) \\(f(x)=(6x+4)^9\\); (b) \\(f(x)=\\frac1{4x+3}\\); (c) \\(f(x)=\\ln(4x+7)\\); (d) \\(f(x)=6^{4x}\\); (e) \\(f(x)=e^{4x}\\); (f) \\(f(x)=\\sin(5x+7)\\).": [
    "درج ذیل تفاعلوں کے پانچویں مشتقات معلوم کریں: (a) \\(f(x)=(6x+4)^9\\)؛ (b) \\(f(x)=\\frac1{4x+3}\\)؛ (c) \\(f(x)=\\ln(4x+7)\\)؛ (d) \\(f(x)=6^{4x}\\)؛ (e) \\(f(x)=e^{4x}\\)؛ (f) \\(f(x)=\\sin(5x+7)\\)۔",
    "د لاندې تابع ګانو پنځم مشتقونه ومومئ: (a) \\(f(x)=(6x+4)^9\\)؛ (b) \\(f(x)=\\frac1{4x+3}\\)؛ (c) \\(f(x)=\\ln(4x+7)\\)؛ (d) \\(f(x)=6^{4x}\\)؛ (e) \\(f(x)=e^{4x}\\)؛ (f) \\(f(x)=\\sin(5x+7)\\)."
  ],
  "The source solutions continue on page 105.": [
    "ماخذ کے حل صفحہ 105 پر جاری ہیں۔",
    "د سرچینې حلونه په 105 پاڼه کې دوام لري."
  ],
  "a. If f(x) = (6x + 4)⁹ with a = 6, b = 4 and m = 9, then the 5th derivative of the given function is obtained by inserting n = 5 in equation:": [
    "a. اگر f(x) = (6x + 4)⁹ میں a = 6، b = 4 اور m = 9 ہوں تو مساوات میں n = 5 رکھنے سے دیے گئے تفاعل کا پانچواں مشتق حاصل ہوتا ہے:",
    "a. که په f(x) = (6x + 4)⁹ کې a = 6، b = 4 او m = 9 وي، نو په معادله کې د n = 5 په اېښودلو د ورکړل شوې تابع پنځم مشتق ترلاسه کېږي:"
  ],
  "b. If \\(f(x)=\\frac1{4x+3}\\) with a = 4 and b = 3, then the 5th derivative of the given function is obtained by inserting n = 5 in equation:": [
    "b. اگر \\(f(x)=\\frac1{4x+3}\\) میں a = 4 اور b = 3 ہوں تو مساوات میں n = 5 رکھنے سے دیے گئے تفاعل کا پانچواں مشتق حاصل ہوتا ہے:",
    "b. که په \\(f(x)=\\frac1{4x+3}\\) کې a = 4 او b = 3 وي، نو په معادله کې د n = 5 په اېښودلو د ورکړل شوې تابع پنځم مشتق ترلاسه کېږي:"
  ],
  "c. If f(x) = ln(4x + 7) with a = 4 and b = 7, then the 5th derivative of the given function is obtained by inserting n = 5 in equation:": [
    "c. اگر f(x) = ln(4x + 7) میں a = 4 اور b = 7 ہوں تو مساوات میں n = 5 رکھنے سے دیے گئے تفاعل کا پانچواں مشتق حاصل ہوتا ہے:",
    "c. که په f(x) = ln(4x + 7) کې a = 4 او b = 7 وي، نو په معادله کې د n = 5 په اېښودلو د ورکړل شوې تابع پنځم مشتق ترلاسه کېږي:"
  ],
  "d. If f(x) = 6⁴ˣ with a = 6 and m = 4, then the 5th derivative of the given function is obtained by inserting n = 5 in equation:": [
    "d. اگر f(x) = 6⁴ˣ میں a = 6 اور m = 4 ہوں تو مساوات میں n = 5 رکھنے سے دیے گئے تفاعل کا پانچواں مشتق حاصل ہوتا ہے:",
    "d. که په f(x) = 6⁴ˣ کې a = 6 او m = 4 وي، نو په معادله کې د n = 5 په اېښودلو د ورکړل شوې تابع پنځم مشتق ترلاسه کېږي:"
  ],
  "e. If f(x) = e⁴ˣ with m = 4, then the 5th derivative of the given function is obtained by inserting n = 5 in equation:": [
    "e. اگر f(x) = e⁴ˣ میں m = 4 ہو تو مساوات میں n = 5 رکھنے سے دیے گئے تفاعل کا پانچواں مشتق حاصل ہوتا ہے:",
    "e. که په f(x) = e⁴ˣ کې m = 4 وي، نو په معادله کې د n = 5 په اېښودلو د ورکړل شوې تابع پنځم مشتق ترلاسه کېږي:"
  ],
  "f. If f(x) = sin(5x + 7) with a = 5 and b = 7, then the 5th derivative of the given function is obtained by inserting n = 5 in equation:": [
    "f. اگر f(x) = sin(5x + 7) میں a = 5 اور b = 7 ہوں تو مساوات میں n = 5 رکھنے سے دیے گئے تفاعل کا پانچواں مشتق حاصل ہوتا ہے:",
    "f. که په f(x) = sin(5x + 7) کې a = 5 او b = 7 وي، نو په معادله کې د n = 5 په اېښودلو د ورکړل شوې تابع پنځم مشتق ترلاسه کېږي:"
  ],
  "4.1.2 Second derivative of implicit, inverse trigonometric and parametric functions": [
    "4.1.2 ضمنی، معکوس مثلثی اور پیرامیٹری تفاعلوں کے دوسرے مشتقات",
    "4.1.2 د ضمني، معکوسو مثلثاتي او پارامتري تابع ګانو دویم مشتقونه"
  ],
  "Find the second derivative of \\(x^2y+2y^3=3x+2y\\).": [
    "\\(x^2y+2y^3=3x+2y\\) کا دوسرا مشتق معلوم کریں۔",
    "د \\(x^2y+2y^3=3x+2y\\) دویم مشتق ومومئ."
  ],
  "The equation is \\(x^2y+2y^3=3x+2y\\).": [
    "مساوات \\(x^2y+2y^3=3x+2y\\) ہے۔",
    "معادله \\(x^2y+2y^3=3x+2y\\) ده."
  ],
  "The first implicit derivative of (i) w.r.t. x is:": [
    "x کے لحاظ سے (i) کا پہلا ضمنی مشتق یہ ہے:",
    "د x په نسبت د (i) لومړی ضمني مشتق دا دی:"
  ],
  "The source second-derivative calculation continues on page 106. Example 3(b) excludes x = −3/4; Example 3(c) requires x > −7/4. In Example 3(d), log6 means the natural logarithm logₑ6 from its governing formula, rather than a common logarithm.": [
    "ماخذ میں دوسرے مشتق کا حساب صفحہ 106 پر جاری ہے۔ مثال 3(b) میں x = −3/4 خارج ہے؛ مثال 3(c) کے لیے x > −7/4 ضروری ہے۔ مثال 3(d) میں بنیادی فارمولے کے مطابق log6 سے مراد قدرتی لوگارتھم logₑ6 ہے، عام لوگارتھم نہیں۔",
    "د سرچینې د دویم مشتق محاسبه په 106 پاڼه کې دوام لري. بېلګه 3(b) کې x = −3/4 نه شاملېږي؛ بېلګه 3(c) x > −7/4 غواړي. په بېلګه 3(d) کې د بنسټیز فورمول له مخې log6 د طبیعي لوګاریتم logₑ6 مانا لري، نه د عام لوګاریتم."
  ],
  "The second implicit derivative of first implicit derivative (ii) w.r.t. x is:": [
    "x کے لحاظ سے پہلے ضمنی مشتق (ii) کا دوسرا ضمنی مشتق یہ ہے:",
    "د x په نسبت د لومړي ضمني مشتق (ii) دویم ضمني مشتق دا دی:"
  ],
  "Putting values of dy/dx:": [
    "dy/dx کی قیمتیں رکھنے سے:",
    "د dy/dx ارزښتونو په اېښودلو:"
  ],
  "In the common-denominator intermediate line, the numerator 6x − 4x²y must be grouped together before multiplication by x² + 6y² − 2. The next expanded line and final polynomial agree with that grouping. The derivative formula applies along the original curve only where D = x² + 6y² − 2 ≠ 0; if D = 0, division does not establish a finite derivative.": [
    "مشترک مخرج والی درمیانی سطر میں x² + 6y² − 2 سے ضرب دینے سے پہلے صورت 6x − 4x²y کو ایک ساتھ قوسین میں رکھنا ضروری ہے۔ اگلی کھلی ہوئی سطر اور آخری کثیرالحدی اسی گروہ بندی سے مطابقت رکھتے ہیں۔ مشتق کا فارمولا اصل منحنی پر صرف وہاں لاگو ہے جہاں D = x² + 6y² − 2 ≠ 0 ہو؛ اگر D = 0 ہو تو تقسیم سے محدود مشتق ثابت نہیں ہوتا۔",
    "د ګډ مخرج په منځنۍ کرښه کې باید صورت 6x − 4x²y د x² + 6y² − 2 تر ضرب مخکې په یوه ډله کې ونیول شي. راتلونکې پرانیستل شوې کرښه او وروستۍ کثیرالحدي له همدې ډلبندۍ سره برابرې دي. د مشتق فورمول د اصلي منحني پر هغو ځایونو تطبیقېږي چې D = x² + 6y² − 2 ≠ 0 وي؛ که D = 0 وي، وېش محدود مشتق نه ثابتوي."
  ],
  "Find the second derivative of \\(\\cos^{-1}y+y=2xy\\).": [
    "\\(\\cos^{-1}y+y=2xy\\) کا دوسرا مشتق معلوم کریں۔",
    "د \\(\\cos^{-1}y+y=2xy\\) دویم مشتق ومومئ."
  ],
  "The given equation is \\(\\cos^{-1}y+y=2xy\\).": [
    "دی گئی مساوات \\(\\cos^{-1}y+y=2xy\\) ہے۔",
    "ورکړل شوې معادله \\(\\cos^{-1}y+y=2xy\\) ده."
  ],
  "The source calculation continues on printed page 107.": [
    "ماخذ کا حساب مطبوعہ صفحہ 107 پر جاری ہے۔",
    "د سرچینې محاسبه په چاپ شوې 107 پاڼه کې دوام لري."
  ],
  "Equation (ii) can be written in simplified form for 1st order derivative as:": [
    "پہلے درجے کے مشتق کے لیے مساوات (ii) کو آسان صورت میں یوں لکھ سکتے ہیں:",
    "د لومړۍ مرتبې مشتق لپاره (ii) معادله په ساده بڼه داسې لیکلای شو:"
  ],
  "Equating coefficients of dy/dx and d²y/dx² to obtain:": [
    "dy/dx اور d²y/dx² کے عددی سروں کو برابر کرنے سے حاصل ہوتا ہے:",
    "د dy/dx او d²y/dx² د ضریبونو په برابرولو ترلاسه کېږي:"
  ],
  "The Remember box reverses the sign of the correct first derivative. Put s = √(1 − y²), A = 1 − 2x − 1/s. Then y′ = 2y/A = 2ys/(s − 1 − 2xs). Differentiating −(1 − y²)⁻¹/² requires the chain factor y′. Multiplication by the other y′ produces a square: A y″ = 4y′ + y(y′)²/s³. The printed lines lose this factor, so their final second derivative is not valid. The corrected result is y″ = 8y/A² + 4y³/(s³A³), for |y| < 1 and A ≠ 0 on the original curve.": [
    "یاد رکھیں والے خانے میں درست پہلے مشتق کی علامت الٹ گئی ہے۔ s = √(1 − y²)، A = 1 − 2x − 1/s رکھیں۔ تب y′ = 2y/A = 2ys/(s − 1 − 2xs) ہے۔ −(1 − y²)⁻¹/² کی تفریق میں زنجیری عامل y′ ضروری ہے۔ دوسرے y′ سے ضرب دینے پر مربع بنتا ہے: A y″ = 4y′ + y(y′)²/s³۔ مطبوعہ سطروں میں یہ عامل چھوٹ گیا ہے، اس لیے ان کا آخری دوسرا مشتق درست نہیں۔ درست نتیجہ y″ = 8y/A² + 4y³/(s³A³) ہے، اصل منحنی پر |y| < 1 اور A ≠ 0 کے لیے۔",
    "د «په یاد ولرئ» په چوکاټ کې د سم لومړي مشتق نښه اوښتې ده. s = √(1 − y²)، A = 1 − 2x − 1/s کېږدئ. بیا y′ = 2y/A = 2ys/(s − 1 − 2xs) دی. د −(1 − y²)⁻¹/² تفریق د ځنځیر عامل y′ غواړي. په بل y′ ضربول مربع جوړوي: A y″ = 4y′ + y(y′)²/s³. په چاپ شوو کرښو کې دا عامل ورک شوی، نو وروستی دویم مشتق یې ناسم دی. سمه پایله y″ = 8y/A² + 4y³/(s³A³) ده، د اصلي منحني پر |y| < 1 او A ≠ 0 ځایونو کې."
  ],
  "Find the second derivative \\(\\frac{d^2y}{dx^2}\\), when the parametric functions are \\(x(t)=1+t^2,\\ y(t)=t^3+2t^2+1\\).": [
    "جب پیرامیٹری تفاعل \\(x(t)=1+t^2,\\ y(t)=t^3+2t^2+1\\) ہوں تو دوسرا مشتق \\(\\frac{d^2y}{dx^2}\\) معلوم کریں۔",
    "کله چې پارامتري تابع ګانې \\(x(t)=1+t^2,\\ y(t)=t^3+2t^2+1\\) وي، دویم مشتق \\(\\frac{d^2y}{dx^2}\\) ومومئ."
  ],
  "The first derivative of the parametric functions x = x(t) and y = y(t) w.r.t. x is:": [
    "x کے لحاظ سے پیرامیٹری تفاعلوں x = x(t) اور y = y(t) کا پہلا مشتق یہ ہے:",
    "د x په نسبت د پارامتري تابع ګانو x = x(t) او y = y(t) لومړی مشتق دا دی:"
  ],
  "The second derivative of the parametric functions is obtained by taking the derivative of equation (i):": [
    "مساوات (i) کا مشتق لینے سے پیرامیٹری تفاعلوں کا دوسرا مشتق حاصل ہوتا ہے:",
    "د (i) معادلې په تفریقولو د پارامتري تابع ګانو دویم مشتق ترلاسه کېږي:"
  ],
  "Multiply and divide it by dt. The calculation continues on page 108.": [
    "اسے dt سے ضرب دیں اور dt ہی سے تقسیم کریں۔ حساب صفحہ 108 پر جاری ہے۔",
    "دا په dt ضرب او پر dt ووېشئ. محاسبه په 108 پاڼه کې دوام لري."
  ],
  "The quotient rule of differentiation is used to simplify the right hand side of equation (ii):": [
    "مساوات (ii) کے دائیں طرف کو آسان کرنے کے لیے تفریق کا حاصلِ تقسیم قاعدہ استعمال کیا جاتا ہے:",
    "د (ii) معادلې د ښي لوري د ساده کولو لپاره د تفریق د حاصل قسمت قاعده کارول کېږي:"
  ],
  "Use (ii) in (iii) to obtain the general term for second derivative of parametric functions x(t) and y(t):": [
    "پیرامیٹری تفاعلوں x(t) اور y(t) کے دوسرے مشتق کی عمومی حد حاصل کرنے کے لیے (iii) میں (ii) استعمال کریں:",
    "د پارامتري تابع ګانو x(t) او y(t) د دویم مشتق د عمومي جملې د ترلاسه کولو لپاره په (iii) کې (ii) وکاروئ:"
  ],
  "Replace \\(\\frac{dt}{dx}\\) by \\(\\frac1{dx/dt}\\).": [
    "\\(\\frac{dt}{dx}\\) کی جگہ \\(\\frac1{dx/dt}\\) رکھیں۔",
    "د \\(\\frac{dt}{dx}\\) پر ځای \\(\\frac1{dx/dt}\\) کېږدئ."
  ],
  "In light of result (iv), the first and second derivatives of the parametric functions x(t) = 1 + t², y(t) = t³ + 2t² + 1 with dx/dt = 2t, d²x/dt² = 2, dy/dt = 3t² + 4t, d²y/dt² = 6t + 4 are the following:": [
    "نتیجہ (iv) کی روشنی میں پیرامیٹری تفاعلوں x(t) = 1 + t²، y(t) = t³ + 2t² + 1 کے پہلے اور دوسرے مشتقات درج ذیل ہیں، جہاں dx/dt = 2t، d²x/dt² = 2، dy/dt = 3t² + 4t، d²y/dt² = 6t + 4 ہیں:",
    "د (iv) پایلې له مخې د پارامتري تابع ګانو x(t) = 1 + t²، y(t) = t³ + 2t² + 1 لومړی او دویم مشتقونه داسې دي، چې dx/dt = 2t، d²x/dt² = 2، dy/dt = 3t² + 4t، d²y/dt² = 6t + 4 دي:"
  ],
  "Both quotient formulas require dx/dt ≠ 0. Here t ≠ 0; canceling t in the first derivative does not establish the parametric formula at t = 0. The two branches y = 2x − 1 ± (x − 1)³/² have limiting first slope 2 at x = 1, while their second derivative is unbounded there.": [
    "حاصلِ تقسیم کے دونوں فارمولوں میں dx/dt ≠ 0 ضروری ہے۔ یہاں t ≠ 0 ہے؛ پہلے مشتق میں t کاٹ دینے سے t = 0 پر پیرامیٹری فارمولا ثابت نہیں ہوتا۔ دو شاخوں y = 2x − 1 ± (x − 1)³/² کی x = 1 پر حدی پہلی ڈھلوان 2 ہے، جبکہ وہاں ان کا دوسرا مشتق غیر محدود ہے۔",
    "د حاصل قسمت دواړه فورمولونه dx/dt ≠ 0 غواړي. دلته t ≠ 0 دی؛ په لومړي مشتق کې د t اختصار په t = 0 کې پارامتري فورمول نه ثابتوي. د y = 2x − 1 ± (x − 1)³/² دواړه څانګې په x = 1 کې د لومړي میلان حد 2 لري، خو دویم مشتق یې هلته نامحدود دی."
  ],
  "4.1.3 MAPLE command diff repeatedly to find higher order derivative of a function": [
    "4.1.3 تفاعل کے اعلیٰ درجے کے مشتقات کے لیے MAPLE کمانڈ diff کا بار بار استعمال",
    "4.1.3 د تابع د لوړو مشتقونو د موندلو لپاره د MAPLE د diff قومندې تکراري کارول"
  ],
  "The procedure to use of MAPLE command diff is illustrated in the following example.": [
    "MAPLE کمانڈ diff استعمال کرنے کا طریقہ درج ذیل مثال سے واضح کیا گیا ہے۔",
    "د MAPLE د diff قومندې د کارولو طریقه په لاندې بېلګه کې ښودل شوې ده."
  ],
  "Differentiate \\(f(x)=x^4+x^2\\sin x+x+2\\) w.r.t. x.": [
    "x کے لحاظ سے \\(f(x)=x^4+x^2\\sin x+x+2\\) کا مشتق لیں۔",
    "د x په نسبت د \\(f(x)=x^4+x^2\\sin x+x+2\\) مشتق واخلئ."
  ],
  "For second derivative, after command, press the “Enter” key two times to obtain the second derivative of a given function above result.": [
    "دوسرے مشتق کے لیے کمانڈ کے بعد ”Enter“ کلید دو بار دبائیں تاکہ اوپر دیے گئے تفاعل کا دوسرا مشتق حاصل ہو۔",
    "د دویم مشتق لپاره، له قومندې وروسته د «Enter» تڼۍ دوه ځله کېکاږئ څو د پورته ورکړل شوې تابع دویم مشتق ترلاسه شي."
  ],
  "The printed command differentiates once, but the displayed result is the second derivative. Pressing Enter again evaluates the same command. To obtain the displayed second derivative, differentiate the first result again or use the nested command shown below. These are independently derived expected outputs; a Maple session has not been executed.": [
    "مطبوعہ کمانڈ ایک بار تفریق کرتی ہے، لیکن دکھایا گیا جواب دوسرا مشتق ہے۔ Enter دوبارہ دبانے سے وہی کمانڈ دوبارہ چلتی ہے۔ دکھایا گیا دوسرا مشتق حاصل کرنے کے لیے پہلے جواب کا دوبارہ مشتق لیں یا نیچے دی گئی اندر در اندر کمانڈ استعمال کریں۔ یہ متوقع نتائج الگ سے اخذ کیے گئے ہیں؛ Maple نشست چلائی نہیں گئی۔",
    "چاپ شوې قومنده یو ځل تفریق کوي، خو ښودل شوې پایله دویم مشتق دی. بیا Enter کېکاږل هماغه قومنده بیا اجرا کوي. د ښودل شوي دویم مشتق د ترلاسه کولو لپاره د لومړۍ پایلې بیا مشتق واخلئ یا لاندې دننه په دننه قومنده وکاروئ. دا تمه کېدونکې پایلې په خپلواکه توګه اخذ شوې دي؛ د Maple ناسته نه ده اجرا شوې."
  ],
  "Example 1": [
    "مثال 1",
    "بېلګه 1"
  ],
  "Example 2": [
    "مثال 2",
    "بېلګه 2"
  ],
  "Example 3": [
    "مثال 3",
    "بېلګه 3"
  ],
  "Example 3 — Solution": [
    "مثال 3 — حل",
    "بېلګه 3 — حل"
  ],
  "Example 4": [
    "مثال 4",
    "بېلګه 4"
  ],
  "Example 4 — continued": [
    "مثال 4 — جاری",
    "بېلګه 4 — دوام"
  ],
  "Example 5": [
    "مثال 5",
    "بېلګه 5"
  ],
  "Example 5 — continued": [
    "مثال 5 — جاری",
    "بېلګه 5 — دوام"
  ],
  "Example 6": [
    "مثال 6",
    "بېلګه 6"
  ],
  "Example 6 — continued": [
    "مثال 6 — جاری",
    "بېلګه 6 — دوام"
  ],
  "Example 7": [
    "مثال 7",
    "بېلګه 7"
  ],
  "4.2 Maclaurin’s and Taylor’s Expansions": [
    "4.2 میکلارن اور ٹیلر کی توسیعات",
    "4.2 د مکلاورین او ټېلر پراختیاوې"
  ],
  "Often the value of a function and the values of its derivatives are known at a particular point and from this information it is desired to obtain values of the function around that particular point. The Taylor polynomials and Taylor series allow us to make such estimates.": [
    "اکثر کسی مخصوص نقطے پر تفاعل اور اس کے مشتقات کی قیمتیں معلوم ہوتی ہیں اور ان معلومات سے اسی نقطے کے آس پاس تفاعل کی قیمتیں حاصل کرنا مقصود ہوتا ہے۔ ٹیلر کثیرالحدیاں اور ٹیلر سلسلے ہمیں ایسے تخمینے لگانے کی سہولت دیتے ہیں۔",
    "ډېری وخت په یوه ټاکلي ټکي کې د تابع او د هغې د مشتقونو ارزښتونه معلوم وي او له دې معلوماتو څخه د هماغه ټکي شاوخوا د تابع ارزښتونه غوښتل کېږي. د ټېلر کثیرالحدۍ او لړۍ موږ ته د داسې اټکلونو اجازه راکوي."
  ],
  "4.2.1 Maclaurin’s and Taylor’s theorems. Using these theorems to expand sinx, cosx, tanx, aˣ, eˣ, logₐ(1 + x) and ln(1 + x)": [
    "4.2.1 میکلارن اور ٹیلر کے قضیے۔ ان قضیوں سے sinx، cosx، tanx، aˣ، eˣ، logₐ(1 + x) اور ln(1 + x) کی توسیع",
    "4.2.1 د مکلاورین او ټېلر قضیې. د دې قضیو په وسیله د sinx، cosx، tanx، aˣ، eˣ، logₐ(1 + x) او ln(1 + x) پراخول"
  ],
  "A. Taylor’s Theorem": [
    "A. ٹیلر کا قضیہ",
    "A. د ټېلر قضیه"
  ],
  "If f(x) and its n derivatives at x = x₀ are f(x₀), f′(x₀), f″(x₀), … f⁽ⁿ⁾(x₀), then the nth order Taylor polynomial pₙ(x) may be written as:": [
    "اگر x = x₀ پر f(x) اور اس کے n مشتقات کی قیمتیں f(x₀)، f′(x₀)، f″(x₀)، … f⁽ⁿ⁾(x₀) ہوں تو nویں درجے کی ٹیلر کثیرالحدی pₙ(x) یوں لکھی جا سکتی ہے:",
    "که په x = x₀ کې د f(x) او د هغې د n مشتقونو ارزښتونه f(x₀)، f′(x₀)، f″(x₀)، … f⁽ⁿ⁾(x₀) وي، نو د nمې مرتبې د ټېلر کثیرالحدي pₙ(x) داسې لیکل کېدای شي:"
  ],
  "This polynomial provides an approximation to f(x). The polynomial and its n derivatives are very much matched with the values of f(x) and its first n derivatives evaluated at x = x₀:": [
    "یہ کثیرالحدی f(x) کا تخمینہ دیتی ہے۔ کثیرالحدی اور اس کے n مشتقات کی قیمتیں x = x₀ پر f(x) اور اس کے پہلے n مشتقات کی قیمتوں سے مطابقت رکھتی ہیں:",
    "دا کثیرالحدي د f(x) اټکل ورکوي. د کثیرالحدۍ او د هغې د n مشتقونو ارزښتونه په x = x₀ کې د f(x) او د هغې د لومړیو n مشتقونو له ارزښتونو سره سمون لري:"
  ],
  "The function \\(y=f(x)=e^x\\) and its derivatives evaluated at x₀ = 0 are known by f(0) = 1, f′(0) = 1, f″(0) = 1, f‴(0) = 1. Use fourth order Taylor polynomial about x₀ = 0 to estimate f(0.2) at x = 0.2.": [
    "تفاعل \\(y=f(x)=e^x\\) اور x₀ = 0 پر اس کے مشتقات کی معلوم قیمتیں f(0) = 1، f′(0) = 1، f″(0) = 1، f‴(0) = 1 ہیں۔ x = 0.2 پر f(0.2) کا تخمینہ لگانے کے لیے x₀ = 0 کے گرد چوتھے درجے کی ٹیلر کثیرالحدی استعمال کریں۔",
    "د \\(y=f(x)=e^x\\) تابع او په x₀ = 0 کې د هغې د مشتقونو معلوم ارزښتونه f(0) = 1، f′(0) = 1، f″(0) = 1، f‴(0) = 1 دي. په x = 0.2 کې د f(0.2) د اټکل لپاره د x₀ = 0 شاوخوا د څلورمې مرتبې د ټېلر کثیرالحدي وکاروئ."
  ],
  "The fourth order Taylor polynomial p₄(x) is obtained by terminating the Taylor polynomial (i) after fourth order derivative term:": [
    "ٹیلر کثیرالحدی (i) کو چوتھے درجے کے مشتق والی حد کے بعد ختم کرنے سے چوتھے درجے کی ٹیلر کثیرالحدی p₄(x) حاصل ہوتی ہے:",
    "د ټېلر کثیرالحدي (i) د څلورمې مرتبې د مشتق تر جملې وروسته په ختمولو د څلورمې مرتبې د ټېلر کثیرالحدي p₄(x) ترلاسه کېږي:"
  ],
  "Insert x₀ = 0 in (ii) to obtain:": [
    "(ii) میں x₀ = 0 رکھنے سے حاصل ہوتا ہے:",
    "په (ii) کې د x₀ = 0 په اېښودلو ترلاسه کېږي:"
  ],
  "The Taylor polynomial (iii) is used to obtain approximation of a function y = f(x) = eˣ at x = 0.2:": [
    "x = 0.2 پر تفاعل y = f(x) = eˣ کا تخمینہ حاصل کرنے کے لیے ٹیلر کثیرالحدی (iii) استعمال کی جاتی ہے:",
    "په x = 0.2 کې د y = f(x) = eˣ تابع د اټکل لپاره د ټېلر کثیرالحدي (iii) کارول کېږي:"
  ],
  "Notice that the Taylor polynomial approximation equals the actual function value y = f(0.2) = e⁰·² = 1.2214 at x = 0.2.": [
    "دیکھیں کہ x = 0.2 پر ٹیلر کثیرالحدی کا تخمینہ اصل تفاعلی قیمت y = f(0.2) = e⁰·² = 1.2214 کے برابر ہے۔",
    "وګورئ چې په x = 0.2 کې د ټېلر کثیرالحدۍ اټکل د تابع له اصلي ارزښت y = f(0.2) = e⁰·² = 1.2214 سره برابر دی."
  ],
  "The two values agree when rounded to four decimal places, not exactly: p₄(0.2) = 1.2214, whereas e⁰·² ≈ 1.22140275816. The omitted remainder is about 0.00000275816. The source opening lists derivatives only through f‴(0); the fourth derivative is also 1 for eˣ.": [
    "دونوں قیمتیں چار اعشاری مقامات تک گول کرنے پر برابر ہیں، بالکل برابر نہیں: p₄(0.2) = 1.2214، جبکہ e⁰·² ≈ 1.22140275816 ہے۔ چھوڑا گیا باقیہ تقریباً 0.00000275816 ہے۔ ماخذ ابتدا میں صرف f‴(0) تک مشتقات درج کرتا ہے؛ eˣ کا چوتھا مشتق بھی 1 ہے۔",
    "دواړه ارزښتونه تر څلورو اعشاري ځایونو په ګردولو برابر دي، کټ مټ نه: p₄(0.2) = 1.2214، حال دا چې e⁰·² ≈ 1.22140275816 دی. پرېښودل شوی پاتې شونی شاوخوا 0.00000275816 دی. سرچینه په پیل کې یوازې تر f‴(0) مشتقونه لېست کوي؛ د eˣ څلورم مشتق هم 1 دی."
  ],
  "Remember — Taylor’s Series": [
    "یاد رکھیں — ٹیلر کا سلسلہ",
    "په یاد ولرئ — د ټېلر لړۍ"
  ],
  "The Taylor polynomials have been used to estimate the values of y = f(x) at various x values. It is reasonable to ask: i. How accurate Taylor polynomials generated by y = f(x) at x₀ to approximate y = f(x) at values of x other than x₀?": [
    "مختلف x قیمتوں پر y = f(x) کی قیمتوں کے تخمینے کے لیے ٹیلر کثیرالحدیاں استعمال کی گئی ہیں۔ یہ سوال مناسب ہے: i. x₀ پر y = f(x) سے بننے والی ٹیلر کثیرالحدیاں، x₀ کے علاوہ دیگر x قیمتوں پر y = f(x) کا کتنا درست تخمینہ دیتی ہیں؟",
    "د ټېلر کثیرالحدۍ د x په بېلابېلو ارزښتونو کې د y = f(x) د ارزښتونو د اټکل لپاره کارول شوې دي. مناسبه پوښتنه دا ده: i. په x₀ کې له y = f(x) څخه جوړې شوې د ټېلر کثیرالحدۍ، له x₀ پرته د x په نورو ارزښتونو کې د y = f(x) څومره دقیق اټکل کوي؟"
  ],
  "Taylor’s Series — continued": [
    "ٹیلر کا سلسلہ — جاری",
    "د ټېلر لړۍ — دوام"
  ],
  "ii. If more and more terms are used in the Taylor polynomial, then this will produce a better and better approximation to y = f(x). To answer these questions, we introduce the Taylor series. As more and more terms are included in the Taylor polynomial, we obtain an infinite series, known as a Taylor series:": [
    "ii. اگر ٹیلر کثیرالحدی میں زیادہ سے زیادہ حدود استعمال کی جائیں تو y = f(x) کا بہتر سے بہتر تخمینہ حاصل ہوگا۔ ان سوالات کے جواب کے لیے ہم ٹیلر سلسلہ متعارف کرتے ہیں۔ ٹیلر کثیرالحدی میں مزید حدود شامل کرتے رہنے سے ایک لامتناہی سلسلہ حاصل ہوتا ہے، جسے ٹیلر سلسلہ کہتے ہیں:",
    "ii. که د ټېلر په کثیرالحدۍ کې لا ډېرې جملې وکارول شي، نو د y = f(x) لا ښه اټکل به ترلاسه شي. د دې پوښتنو د ځواب لپاره د ټېلر لړۍ معرفي کوو. د ټېلر په کثیرالحدۍ کې د نورو جملو په ورزیاتولو یوه نامحدوده لړۍ ترلاسه کېږي چې د ټېلر لړۍ بلل کېږي:"
  ],
  "For some Taylor series, the value of the series equals the value of the function for every value of x. That is, the Taylor series approximations of eˣ, sinx and cosx equal the values of eˣ, sinx and cosx for every value of x. However, some functions have a Taylor series which equals the function only for a limited range of x values. For example, the value of \\(f(x)=\\frac1{1+x}\\) equals its Taylor series only when −1 < x < 1.": [
    "بعض ٹیلر سلسلوں کی قیمت ہر x پر تفاعل کی قیمت کے برابر ہوتی ہے۔ یعنی eˣ، sinx اور cosx کے ٹیلر سلسلوں کے تخمینے ہر x پر eˣ، sinx اور cosx کی قیمتوں کے برابر ہوتے ہیں۔ تاہم بعض تفاعلوں کے ٹیلر سلسلے صرف x کی محدود سعت میں تفاعل کے برابر ہوتے ہیں۔ مثلاً \\(f(x)=\\frac1{1+x}\\) صرف −1 < x < 1 پر اپنے ٹیلر سلسلے کے برابر ہوتا ہے۔",
    "د ځینو ټېلر لړیو ارزښت د x په هر ارزښت کې د تابع له ارزښت سره برابر وي. یعنې د eˣ، sinx او cosx د ټېلر لړیو اټکلونه د x په هر ارزښت کې د eˣ، sinx او cosx له ارزښتونو سره برابر دي. خو ځینې تابع ګانې د ټېلر داسې لړۍ لري چې یوازې د x د ارزښتونو په محدوده ساحه کې له تابع سره برابره وي. د بېلګې په توګه \\(f(x)=\\frac1{1+x}\\) یوازې د −1 < x < 1 لپاره له خپلې ټېلر لړۍ سره برابره ده."
  ],
  "The displayed finite expression through n is a Taylor polynomial; an infinite Taylor series needs terms continuing indefinitely. Equality to a function requires convergence to that function. More terms need not improve an approximation outside its interval of convergence.": [
    "n تک دکھائی گئی محدود عبارت ٹیلر کثیرالحدی ہے؛ لامتناہی ٹیلر سلسلے میں حدود مسلسل آگے بڑھتی رہتی ہیں۔ کسی تفاعل کے برابر ہونے کے لیے سلسلے کا اسی تفاعل کی طرف تقارب ضروری ہے۔ وقفۂ تقارب سے باہر مزید حدود شامل کرنے سے تخمینہ لازماً بہتر نہیں ہوتا۔",
    "تر n پورې ښودل شوی محدود عبارت د ټېلر کثیرالحدي ده؛ نامحدوده ټېلر لړۍ بې پایه دوام لرونکې جملې غواړي. له تابع سره برابري دې ته اړتیا لري چې لړۍ هماغې تابع ته تقارب وکړي. د تقارب له واټن څخه بهر ډېرې جملې لازماً اټکل نه ښه کوي."
  ],
  "B. Maclaurin’s Series": [
    "B. میکلارن کا سلسلہ",
    "B. د مکلاورین لړۍ"
  ],
  "A special case of a Taylor series occurs, when the function y = f(x) is known only at the origin x₀ = 0. This special condition imposed on Taylor series develops the Maclaurin’s series:": [
    "ٹیلر سلسلے کی ایک خاص صورت اس وقت ہوتی ہے جب تفاعل y = f(x) صرف مبدا x₀ = 0 پر معلوم ہو۔ ٹیلر سلسلے پر یہ خاص شرط میکلارن سلسلہ پیدا کرتی ہے:",
    "د ټېلر لړۍ ځانګړی حالت هغه وخت وي چې y = f(x) تابع یوازې په مبدا x₀ = 0 کې معلومه وي. پر ټېلر لړۍ دا ځانګړی شرط د مکلاورین لړۍ رامنځته کوي:"
  ],
  "The Taylor and Maclaurin’s series of y = f(x) about a particular point x₀ are of course:": [
    "کسی مخصوص نقطے x₀ کے گرد y = f(x) کے ٹیلر اور میکلارن سلسلے یہ ہیں:",
    "د یوه ټاکلي ټکي x₀ شاوخوا د y = f(x) د ټېلر او مکلاورین لړۍ دا دي:"
  ],
  "If we use x − x₀ = h, then equations (ii) and (iii) take the popular notation for Taylor and Maclaurin’s series of order n:": [
    "اگر x − x₀ = h استعمال کریں تو مساوات (ii) اور (iii)، nویں درجے کے ٹیلر اور میکلارن سلسلوں کی معروف علامتی صورت اختیار کرتی ہیں:",
    "که x − x₀ = h وکاروو، نو (ii) او (iii) معادلې د nمې مرتبې د ټېلر او مکلاورین لړیو مشهوره نښه اخلي:"
  ],
  "The graphical view of a function y = f(x) at x = x₀ is shown in Figure 4.1.": [
    "x = x₀ پر تفاعل y = f(x) کا گرافی منظر شکل 4.1 میں دکھایا گیا ہے۔",
    "په x = x₀ کې د y = f(x) تابع ګرافیکي بڼه په شکل 4.1 کې ښودل شوې ده."
  ],
  "The popular notation for the Taylor & Maclaurin’s series of order n are:": [
    "nویں درجے کے ٹیلر اور میکلارن سلسلوں کی معروف علامتی صورتیں یہ ہیں:",
    "د nمې مرتبې د ټېلر او مکلاورین لړیو مشهورې نښې دا دي:"
  ],
  "If a function y = f(x) is known at a particular point x₀ ≠ 0, then the Taylor series (iv) at forward or backward point x = x₀ ± h of a function y = f(x) are:": [
    "اگر تفاعل y = f(x) کسی مخصوص نقطے x₀ ≠ 0 پر معلوم ہو تو آگے یا پیچھے کے نقطے x = x₀ ± h پر y = f(x) کے ٹیلر سلسلے (iv) یہ ہیں:",
    "که y = f(x) تابع په یوه ټاکلي ټکي x₀ ≠ 0 کې معلومه وي، نو په مخکیني یا شاتني ټکي x = x₀ ± h کې د y = f(x) د ټېلر لړۍ (iv) دا دي:"
  ],
  "In both Maclaurin offset displays, the left side should be f(h), because the expansion point is 0; f(x₀ + h) is valid there only when x₀ = 0. The finite formulas are approximations unless the omitted remainder vanishes. Figure 4.1 is a schematic curve with no prescribed equation or numerical scale. Its left vertical interval is printed h and its right vertical label is f(x₀ + h); these labels are retained. The actual vertical change is f(x₀ + h) − f(x₀), generally different from the horizontal step h.": [
    "میکلارن کی دونوں منتقلی والی صورتوں میں بائیں طرف f(h) ہونا چاہیے، کیونکہ توسیع کا نقطہ 0 ہے؛ وہاں f(x₀ + h) صرف x₀ = 0 پر درست ہے۔ محدود فارمولے تخمینے ہیں، سوائے اس کے کہ چھوڑا گیا باقیہ صفر ہو۔ شکل 4.1 ایک خاکہ جاتی منحنی ہے جس کی کوئی مقرر مساوات یا عددی پیمانہ نہیں۔ اس کے بائیں عمودی وقفے پر h اور دائیں عمودی جانب f(x₀ + h) چھپا ہے؛ یہ لیبل برقرار رکھے گئے ہیں۔ اصل عمودی تبدیلی f(x₀ + h) − f(x₀) ہے، جو عموماً افقی قدم h سے مختلف ہوتی ہے۔",
    "د مکلاورین د واټن په دواړو ښودنو کې چپ لوری باید f(h) وي، ځکه د پراختیا ټکی 0 دی؛ f(x₀ + h) هلته یوازې هغه وخت سم دی چې x₀ = 0 وي. محدود فورمولونه اټکلونه دي، مګر که پرېښودل شوی پاتې شونی صفر وي. شکل 4.1 یوه تشریحي منحني ده چې ټاکلې معادله یا عددي مقیاس نه لري. چپ عمودي واټن یې h چاپ شوی او ښي عمودي لېبل یې f(x₀ + h) دی؛ دا لېبلونه ساتل شوي دي. اصلي عمودي بدلون f(x₀ + h) − f(x₀) دی، چې عموماً له افقي ګام h څخه توپیر لري."
  ],
  "Now, look at the following examples; the procedure to the use of Taylor and Maclaurin’s Theorem is illustrated in these examples.": [
    "اب درج ذیل مثالیں دیکھیں؛ ان میں ٹیلر اور میکلارن کے قضیوں کو استعمال کرنے کا طریقہ واضح کیا گیا ہے۔",
    "اوس لاندې بېلګې وګورئ؛ په دې بېلګو کې د ټېلر او مکلاورین د قضیو د کارولو طریقه ښودل شوې ده."
  ],
  "Use Taylor’s series to approximate the value of a function f(x) = eˣ at a point x₀ = 2.": [
    "x₀ = 2 پر تفاعل f(x) = eˣ کی قیمت کا تخمینہ لگانے کے لیے ٹیلر سلسلہ استعمال کریں۔",
    "په x₀ = 2 ټکي کې د f(x) = eˣ تابع د ارزښت د اټکل لپاره د ټېلر لړۍ وکاروئ."
  ],
  "The function and its derivatives at x₀ = 2:": [
    "x₀ = 2 پر تفاعل اور اس کے مشتقات:",
    "په x₀ = 2 کې تابع او د هغې مشتقونه:"
  ],
  "are used in Taylor series (ii) to obtain the Taylor series approximation of eˣ at a point x₀ = 2:": [
    "x₀ = 2 پر eˣ کا ٹیلر سلسلہ تخمینہ حاصل کرنے کے لیے ٹیلر سلسلے (ii) میں استعمال کیے جاتے ہیں:",
    "په x₀ = 2 ټکي کې د eˣ د ټېلر لړۍ د اټکل لپاره د ټېلر په لړۍ (ii) کې کارول کېږي:"
  ],
  "The source rounds e² to 7.3891; equality with that decimal is approximate. The exact Taylor series is e²[1 + (x − 2) + (x − 2)²/2! + …]. The real exponential aˣ requires a > 0. These exponential and sine series converge for all real x; a finite truncation remains an approximation.": [
    "ماخذ میں e² کو گول کر کے 7.3891 لکھا گیا ہے؛ اس اعشاری عدد کے ساتھ برابری تقریبی ہے۔ عین درست ٹیلر سلسلہ e²[1 + (x − 2) + (x − 2)²/2! + …] ہے۔ حقیقی قوت نمائی تفاعل aˣ کے لیے a > 0 ضروری ہے۔ یہ قوت نمائی اور sine سلسلے تمام حقیقی x کے لیے متقارب ہیں؛ محدود تعداد میں حدود لینے سے جواب تخمینہ رہتا ہے۔",
    "سرچینه e² په ګردولو 7.3891 لیکي؛ له دې اعشاري عدد سره برابري تقریبي ده. دقیق ټېلر لړۍ e²[1 + (x − 2) + (x − 2)²/2! + …] ده. حقیقي نمایي تابع aˣ، a > 0 غواړي. دا نمایي او sine لړۍ د ټولو حقیقي x لپاره تقارب کوي؛ محدودې جملې لا هم اټکل وي."
  ],
  "The cosine series alternates signs: 1 − x²/2! + x⁴/4! − x⁶/6! + …, for every real x. The tangent series is local, with |x| < π/2. For logₐ(1 + x), require a > 0,a ≠ 1 and x > −1. Its Maclaurin series converges for −1 < x ≤ 1; the endpoint x = 1 is conditionally convergent.": [
    "cosine سلسلے کی علامتیں باری باری بدلتی ہیں: ہر حقیقی x کے لیے 1 − x²/2! + x⁴/4! − x⁶/6! + …۔ tangent سلسلہ مقامی ہے اور |x| < π/2 پر لاگو ہے۔ logₐ(1 + x) کے لیے a > 0، a ≠ 1 اور x > −1 ضروری ہیں۔ اس کا میکلارن سلسلہ −1 < x ≤ 1 پر متقارب ہے؛ آخری نقطے x = 1 پر تقارب شرطی ہے۔",
    "د cosine لړۍ نښې په نوبت بدلېږي: د هر حقیقي x لپاره 1 − x²/2! + x⁴/4! − x⁶/6! + … . د tangent لړۍ محلي ده او |x| < π/2 غواړي. د logₐ(1 + x) لپاره a > 0، a ≠ 1 او x > −1 اړین دي. د هغې مکلاورین لړۍ د −1 < x ≤ 1 لپاره متقاربه ده؛ په وروستي ټکي x = 1 کې تقارب مشروط دی."
  ],
  "The printed third-derivative formula omits its numerator 2; f‴(x) = 2/(1 + x)³, agreeing with the printed value f‴(0) = 2 and series coefficient. The function requires x > −1. Its infinite Maclaurin series converges for −1 < x ≤ 1.": [
    "تیسرے مشتق کے مطبوعہ فارمولے میں صورت 2 چھوٹ گئی ہے؛ f‴(x) = 2/(1 + x)³ ہے، جو مطبوعہ قیمت f‴(0) = 2 اور سلسلے کے عددی سر سے مطابقت رکھتی ہے۔ تفاعل کے لیے x > −1 ضروری ہے۔ اس کا لامتناہی میکلارن سلسلہ −1 < x ≤ 1 پر متقارب ہے۔",
    "د درېیم مشتق په چاپ شوي فورمول کې صورت 2 نشته؛ f‴(x) = 2/(1 + x)³ دی، چې له چاپ شوي ارزښت f‴(0) = 2 او د لړۍ له ضریب سره برابر دی. تابع x > −1 غواړي. د هغې نامحدوده مکلاورین لړۍ د −1 < x ≤ 1 لپاره متقاربه ده."
  ],
  "Use Taylor’s theorem to compute the series of the following functions at x₀ = 3: i. f(x) = sinx; ii. f(x) = cosx; iii. f(x) = tanx; iv. f(x) = aˣ; v. f(x) = eˣ; vi. f(x) = logₐ(1 + x); vii. f(x) = ln(1 + x).": [
    "ٹیلر کے قضیے سے x₀ = 3 پر درج ذیل تفاعلوں کے سلسلے معلوم کریں: i. f(x) = sinx؛ ii. f(x) = cosx؛ iii. f(x) = tanx؛ iv. f(x) = aˣ؛ v. f(x) = eˣ؛ vi. f(x) = logₐ(1 + x)؛ vii. f(x) = ln(1 + x)۔",
    "د ټېلر د قضیې په وسیله په x₀ = 3 کې د لاندې تابع ګانو لړۍ محاسبه کړئ: i. f(x) = sinx؛ ii. f(x) = cosx؛ iii. f(x) = tanx؛ iv. f(x) = aˣ؛ v. f(x) = eˣ؛ vi. f(x) = logₐ(1 + x)؛ vii. f(x) = ln(1 + x)."
  ],
  "4.2.2 MAPLE command “Taylor” to find Taylor’s expansion for a given function": [
    "4.2.2 دیے گئے تفاعل کی ٹیلر توسیع کے لیے MAPLE کمانڈ “Taylor”",
    "4.2.2 د ورکړل شوې تابع د ټېلر پراختیا د موندلو لپاره د MAPLE د “Taylor” قومنده"
  ],
  "The use of MAPLE command “Taylor” is illustrated in the following example.": [
    "MAPLE کمانڈ “Taylor” کا استعمال درج ذیل مثال میں واضح کیا گیا ہے۔",
    "د MAPLE د “Taylor” قومندې کارول په لاندې بېلګه کې ښودل شوي دي."
  ],
  "Use Maple command taylor for the function: (a) f(x) = eˣ by Taylor’s series expansion to first four terms; (b) f(x) = sinx by Taylor’s series expansion to first 5 terms.": [
    "Maple کمانڈ taylor استعمال کریں: (a) f(x) = eˣ کو ٹیلر سلسلے سے ابتدائی چار حدود تک پھیلائیں؛ (b) f(x) = sinx کو ٹیلر سلسلے سے ابتدائی 5 حدود تک پھیلائیں۔",
    "د Maple د taylor قومنده وکاروئ: (a) f(x) = eˣ د ټېلر لړۍ په وسیله تر لومړیو څلورو جملو پراخ کړئ؛ (b) f(x) = sinx د ټېلر لړۍ په وسیله تر لومړیو 5 جملو پراخ کړئ."
  ],
  "This result is obtained through right click on the last end of the expression by selecting “Series < xⁿ” on the context menu.": [
    "یہ نتیجہ عبارت کے آخری سرے پر دایاں کلک کر کے سیاقی مینو سے “Series < xⁿ” منتخب کرنے سے حاصل ہوتا ہے۔",
    "دا پایله د عبارت پر وروستي سر په ښي کلیک کولو او د سیاق له مېنو څخه د “Series < xⁿ” په ټاکلو ترلاسه کېږي."
  ],
  "The first request returns powers below x⁴; the sine request returns powers below x⁵, so it has two nonzero terms rather than five nonzero terms. O(x⁵) accounts for the omitted terms starting at degree 5. The output ln(e) equals 1 if e denotes Euler’s constant; if e is entered as an unassigned symbolic name, ln(e) remains symbolic. The source commands and displayed outputs are retained, not claimed as executed Maple results.": [
    "پہلی درخواست x⁴ سے کم قوتیں دیتی ہے؛ sine والی درخواست x⁵ سے کم قوتیں دیتی ہے، اس لیے اس میں پانچ غیر صفر حدود کے بجائے دو غیر صفر حدود ہیں۔ O(x⁵) درجۂ 5 سے شروع ہونے والی چھوڑی گئی حدود کو ظاہر کرتا ہے۔ اگر e سے مراد اویلر کا مستقل ہو تو حاصل شدہ ln(e) کی قیمت 1 ہے؛ اگر e کو ایک غیر متعین علامتی نام کے طور پر درج کیا جائے تو ln(e) علامتی صورت میں رہتا ہے۔ ماخذ کی کمانڈیں اور دکھائے گئے نتائج برقرار ہیں؛ انہیں Maple میں چلا کر حاصل شدہ نتائج قرار نہیں دیا گیا۔",
    "لومړۍ غوښتنه تر x⁴ ټیټ توانونه راکوي؛ د sine غوښتنه تر x⁵ ټیټ توانونه ورکوي، نو د پنځو غیرصفر جملو پر ځای دوه غیرصفر جملې لري. O(x⁵) هغه پرېښودل شوې جملې رانغاړي چې له 5 درجې پیلېږي. که e د اویلر ثابت وي، د ln(e) پایله 1 ده؛ که e یو بې ټاکل شوي سمبولیک نوم وي، ln(e) سمبولیک پاتې کېږي. د سرچینې قومندې او ښودل شوې پایلې ساتل شوې دي، د اجرا شوو Maple پایلو ادعا نه پرې کېږي."
  ],
  "Example 8": [
    "مثال 8",
    "بېلګه 8"
  ],
  "Note": [
    "نوٹ",
    "یادونه"
  ],
  "x = x₀ + h": [
    "x = x₀ + h",
    "x = x₀ + h"
  ],
  "x = x₀ − h": [
    "x = x₀ − h",
    "x = x₀ − h"
  ],
  "Example 9": [
    "مثال 9",
    "بېلګه 9"
  ],
  "D. Maclaurin’s theorem for the functions of the type f(x) = aˣ": [
    "D. f(x) = aˣ کی قسم کے تفاعلوں کے لیے میکلارن کا قضیہ",
    "D. د f(x) = aˣ په ډول تابع ګانو لپاره د مکلاورین قضیه"
  ],
  "Example 10": [
    "مثال 10",
    "بېلګه 10"
  ],
  "Use Maclaurin’s series to approximate the value of a function f(x) = aˣ at a point x₀ = 0.": [
    "نقطے x₀ = 0 پر تفاعل f(x) = aˣ کی قیمت کا تخمینہ لگانے کے لیے میکلارن سلسلہ استعمال کریں۔",
    "په x₀ = 0 ټکي کې د f(x) = aˣ تابع د ارزښت د اټکل لپاره د مکلاورین لړۍ وکاروئ."
  ],
  "The function and its derivatives at x₀ = 0:": [
    "x₀ = 0 پر تفاعل اور اس کے مشتقات:",
    "په x₀ = 0 کې تابع او د هغې مشتقونه:"
  ],
  "are used in Maclaurin series (iii) to obtain the Maclaurin series approximation of aˣ at a point x₀ = 0:": [
    "x₀ = 0 پر aˣ کا میکلارن سلسلے سے تخمینہ حاصل کرنے کے لیے میکلارن سلسلے (iii) میں استعمال کیے جاتے ہیں:",
    "په x₀ = 0 کې د aˣ د مکلاورین لړۍ د اټکل لپاره د مکلاورین په لړۍ (iii) کې کارول کېږي:"
  ],
  "E. Maclaurin’s theorem for the functions of the type f(x) = eˣ": [
    "E. f(x) = eˣ کی قسم کے تفاعلوں کے لیے میکلارن کا قضیہ",
    "E. د f(x) = eˣ په ډول تابع ګانو لپاره د مکلاورین قضیه"
  ],
  "Example 11": [
    "مثال 11",
    "بېلګه 11"
  ],
  "Use Maclaurin’s series to approximate the value of a function f(x) = eˣ at a point x₀ = 0.": [
    "نقطے x₀ = 0 پر تفاعل f(x) = eˣ کی قیمت کا تخمینہ لگانے کے لیے میکلارن سلسلہ استعمال کریں۔",
    "په x₀ = 0 ټکي کې د f(x) = eˣ تابع د ارزښت د اټکل لپاره د مکلاورین لړۍ وکاروئ."
  ],
  "are used in Maclaurin series (iii) to obtain the Maclaurin series approximation of eˣ at a point x₀ = 0:": [
    "x₀ = 0 پر eˣ کا میکلارن سلسلے سے تخمینہ حاصل کرنے کے لیے میکلارن سلسلے (iii) میں استعمال کیے جاتے ہیں:",
    "په x₀ = 0 کې د eˣ د مکلاورین لړۍ د اټکل لپاره د مکلاورین په لړۍ (iii) کې کارول کېږي:"
  ],
  "F. Maclaurin’s theorem for the function of the type f(x) = sin(x)": [
    "F. f(x) = sin(x) کی قسم کے تفاعلوں کے لیے میکلارن کا قضیہ",
    "F. د f(x) = sin(x) په ډول تابع ګانو لپاره د مکلاورین قضیه"
  ],
  "Example 12": [
    "مثال 12",
    "بېلګه 12"
  ],
  "Use Maclaurin’s series to approximate the value of a function f(x) = sin(x) at a point x₀ = 0.": [
    "نقطے x₀ = 0 پر تفاعل f(x) = sin(x) کی قیمت کا تخمینہ لگانے کے لیے میکلارن سلسلہ استعمال کریں۔",
    "په x₀ = 0 ټکي کې د f(x) = sin(x) تابع د ارزښت د اټکل لپاره د مکلاورین لړۍ وکاروئ."
  ],
  "are used in Maclaurin’s series (iii) to obtain the Maclaurin series approximation of sinx at x₀ = 0:": [
    "x₀ = 0 پر sinx کا میکلارن سلسلے سے تخمینہ حاصل کرنے کے لیے میکلارن سلسلے (iii) میں استعمال کیے جاتے ہیں:",
    "په x₀ = 0 کې د sinx د مکلاورین لړۍ د اټکل لپاره د مکلاورین په لړۍ (iii) کې کارول کېږي:"
  ],
  "G. Maclaurin’s theorem for the function of the type f(x) = cos(x)": [
    "G. f(x) = cos(x) کی قسم کے تفاعلوں کے لیے میکلارن کا قضیہ",
    "G. د f(x) = cos(x) په ډول تابع ګانو لپاره د مکلاورین قضیه"
  ],
  "Example 13": [
    "مثال 13",
    "بېلګه 13"
  ],
  "Use Maclaurin’s series to approximate the value of a function f(x) = cosx at a point x₀ = 0.": [
    "نقطے x₀ = 0 پر تفاعل f(x) = cosx کی قیمت کا تخمینہ لگانے کے لیے میکلارن سلسلہ استعمال کریں۔",
    "په x₀ = 0 ټکي کې د f(x) = cosx تابع د ارزښت د اټکل لپاره د مکلاورین لړۍ وکاروئ."
  ],
  "are used in Maclaurin’s series (iii) to obtain the Maclaurin series approximation of cosx at x₀ = 0:": [
    "x₀ = 0 پر cosx کا میکلارن سلسلے سے تخمینہ حاصل کرنے کے لیے میکلارن سلسلے (iii) میں استعمال کیے جاتے ہیں:",
    "په x₀ = 0 کې د cosx د مکلاورین لړۍ د اټکل لپاره د مکلاورین په لړۍ (iii) کې کارول کېږي:"
  ],
  "H. Maclaurin’s theorem for the function of the type f(x) = tan(x)": [
    "H. f(x) = tan(x) کی قسم کے تفاعلوں کے لیے میکلارن کا قضیہ",
    "H. د f(x) = tan(x) په ډول تابع ګانو لپاره د مکلاورین قضیه"
  ],
  "Example 14": [
    "مثال 14",
    "بېلګه 14"
  ],
  "Use Maclaurin’s series to approximate the value of a function f(x) = tanx at a point x₀ = 0.": [
    "نقطے x₀ = 0 پر تفاعل f(x) = tanx کی قیمت کا تخمینہ لگانے کے لیے میکلارن سلسلہ استعمال کریں۔",
    "په x₀ = 0 ټکي کې د f(x) = tanx تابع د ارزښت د اټکل لپاره د مکلاورین لړۍ وکاروئ."
  ],
  "are used in Maclaurin’s series (iii) to obtain the Maclaurin series approximation of tanx at x₀ = 0:": [
    "x₀ = 0 پر tanx کا میکلارن سلسلے سے تخمینہ حاصل کرنے کے لیے میکلارن سلسلے (iii) میں استعمال کیے جاتے ہیں:",
    "په x₀ = 0 کې د tanx د مکلاورین لړۍ د اټکل لپاره د مکلاورین په لړۍ (iii) کې کارول کېږي:"
  ],
  "I. Maclaurin’s theorem for the function of the type f(x) = logₐ(1 + x)": [
    "I. f(x) = logₐ(1 + x) کی قسم کے تفاعلوں کے لیے میکلارن کا قضیہ",
    "I. د f(x) = logₐ(1 + x) په ډول تابع ګانو لپاره د مکلاورین قضیه"
  ],
  "Example 15": [
    "مثال 15",
    "بېلګه 15"
  ],
  "Use Maclaurin’s series to approximate the value of a function f(x) = logₐ(1 + x) at a point x₀ = 0.": [
    "نقطے x₀ = 0 پر تفاعل f(x) = logₐ(1 + x) کی قیمت کا تخمینہ لگانے کے لیے میکلارن سلسلہ استعمال کریں۔",
    "په x₀ = 0 ټکي کې د f(x) = logₐ(1 + x) تابع د ارزښت د اټکل لپاره د مکلاورین لړۍ وکاروئ."
  ],
  "are used in Maclaurin’s series (iii) to obtain the Maclaurin series approximation of logₐ(1 + x) at x₀ = 0:": [
    "x₀ = 0 پر logₐ(1 + x) کا میکلارن سلسلے سے تخمینہ حاصل کرنے کے لیے میکلارن سلسلے (iii) میں استعمال کیے جاتے ہیں:",
    "په x₀ = 0 کې د logₐ(1 + x) د مکلاورین لړۍ د اټکل لپاره د مکلاورین په لړۍ (iii) کې کارول کېږي:"
  ],
  "Example 15 — continued": [
    "مثال 15 — جاری",
    "بېلګه 15 — دوام"
  ],
  "J. Maclaurin’s theorem for the function of the type f(x) = ln(1 + x)": [
    "J. f(x) = ln(1 + x) کی قسم کے تفاعلوں کے لیے میکلارن کا قضیہ",
    "J. د f(x) = ln(1 + x) په ډول تابع ګانو لپاره د مکلاورین قضیه"
  ],
  "Example 16": [
    "مثال 16",
    "بېلګه 16"
  ],
  "Use Maclaurin’s series to approximate the value of a function f(x) = ln(1 + x) at a point x₀ = 0.": [
    "نقطے x₀ = 0 پر تفاعل f(x) = ln(1 + x) کی قیمت کا تخمینہ لگانے کے لیے میکلارن سلسلہ استعمال کریں۔",
    "په x₀ = 0 ټکي کې د f(x) = ln(1 + x) تابع د ارزښت د اټکل لپاره د مکلاورین لړۍ وکاروئ."
  ],
  "are used in Maclaurin’s series (iii) to obtain the Maclaurin series approximation of ln(1 + x) at x₀ = 0:": [
    "x₀ = 0 پر ln(1 + x) کا میکلارن سلسلے سے تخمینہ حاصل کرنے کے لیے میکلارن سلسلے (iii) میں استعمال کیے جاتے ہیں:",
    "په x₀ = 0 کې د ln(1 + x) د مکلاورین لړۍ د اټکل لپاره د مکلاورین په لړۍ (iii) کې کارول کېږي:"
  ],
  "Challenge": [
    "چیلنج",
    "ننګونه"
  ],
  "Example 17": [
    "مثال 17",
    "بېلګه 17"
  ],
  "a. Command:": [
    "a. کمانڈ:",
    "a. قومنده:"
  ],
  "Context Menu:": [
    "سیاقی مینو:",
    "د سیاق مېنو:"
  ],
  "b. Command:": [
    "b. کمانڈ:",
    "b. قومنده:"
  ],
  "Figure 4.1": [
    "شکل 4.1",
    "شکل 4.1"
  ],
  "4.3 Application of Derivatives": [
    "4.3 مشتقات کے اطلاقات",
    "4.3 د مشتقونو کارونې"
  ],
  "In this section, we will see how to use derivatives to determine the tangent, and normal lines, the angles in between two curves, the maximum and minimum values of a function as well as the intervals where the function is increasing or decreasing.": [
    "اس حصے میں ہم دیکھیں گے کہ مشتقات سے مماس اور عمود کی لکیریں، دو منحنیوں کے درمیان زاویے، تفاعل کی زیادہ سے زیادہ اور کم سے کم قیمتیں، اور وہ وقفے کیسے معلوم ہوتے ہیں جہاں تفاعل بڑھتا یا گھٹتا ہے۔",
    "په دې برخه کې به وګورو چې مشتقونه څنګه د مماس او عمود کرښې، د دوو منحنیو ترمنځ زاویې، د تابع اعظم او اصغر ارزښتونه او هغه واټنونه ټاکي چې تابع پکې زیاتېږي یا کمېږي."
  ],
  "4.3.1 Geometrical interpretation of derivative": [
    "4.3.1 مشتق کی ہندسی تعبیر",
    "4.3.1 د مشتق هندسي تعبیر"
  ],
  "Consider a function y = f(x) as shown in Figure 4.2. Let P(x₀,y₀) be a point on a curve y = f(x). The change Δx in x develops a change Δy in y. The coordinates of a point Q are therefore Q(x₀ + Δx,y₀ + Δy). Notice that the slope of the secant line PQ:": [
    "شکل 4.2 میں دکھایا گیا تفاعل y = f(x) لیں۔ فرض کریں P(x₀,y₀) منحنی y = f(x) پر ایک نقطہ ہے۔ x میں تبدیلی Δx سے y میں تبدیلی Δy پیدا ہوتی ہے۔ لہٰذا نقطے Q کے محدد Q(x₀ + Δx,y₀ + Δy) ہیں۔ دیکھیے کہ قاطع لکیر PQ کی ڈھلوان:",
    "په شکل 4.2 کې ښودل شوې تابع y = f(x) په پام کې ونیسئ. فرض کړئ P(x₀,y₀) پر منحني y = f(x) یو ټکی دی. په x کې بدلون Δx په y کې بدلون Δy رامنځته کوي. نو د Q ټکي مختصات Q(x₀ + Δx,y₀ + Δy) دي. وګورئ چې د قاطع کرښې PQ میلان:"
  ],
  "If we take values of Q closer to P, then Q approaches P, and Δx approaches 0 and the slope of the secant line PQ automatically approaches the slope of the tangent line at a particular point P and is denoted by:": [
    "اگر Q کو P کے قریب تر لیتے جائیں تو Q، P کی طرف اور Δx، 0 کی طرف بڑھتا ہے؛ قاطع لکیر PQ کی ڈھلوان خودبخود مخصوص نقطے P پر مماس کی ڈھلوان کی طرف بڑھتی ہے اور اسے یوں ظاہر کرتے ہیں:",
    "که Q، P ته نږدې ونیسو، نو Q، P ته او Δx، 0 ته نږدې کېږي؛ د قاطع کرښې PQ میلان په خپله د ټاکلي ټکي P د مماس میلان ته نږدې کېږي او په دې نښه ښودل کېږي:"
  ],
  "4.3.2 Equations of tangent and normal to the curve at a given point": [
    "4.3.2 دیے گئے نقطے پر منحنی کے مماس اور عمود کی مساوات",
    "4.3.2 په ورکړل شوي ټکي کې د منحني د مماس او عمود معادلې"
  ],
  "If the slope of the tangent line on a curve y = f(x) at a particular point P(x₀,y₀) is f′(x₀), then the tangent line on this curve at a particular point P(x₀,y₀) is the nonhomogeneous line (developed from the definition of the point form of the straight line):": [
    "اگر منحنی y = f(x) پر مخصوص نقطے P(x₀,y₀) میں مماس کی ڈھلوان f′(x₀) ہو تو اسی نقطے P(x₀,y₀) پر مماس کی لکیر غیر متجانس لکیر ہے، جو سیدھی لکیر کی نقطے والی صورت کی تعریف سے حاصل ہوتی ہے:",
    "که پر منحني y = f(x) په ټاکلي ټکي P(x₀,y₀) کې د مماس میلان f′(x₀) وي، نو په همدې ټکي P(x₀,y₀) کې مماس غیرمتجانسه کرښه ده، چې د مستقیمې کرښې د نقطې د بڼې له تعریف څخه ترلاسه کېږي:"
  ],
  "The normal line is the line perpendicular to the tangent line on this curve at a particular point P(x₀,y₀) with slope −1/f′(x₀):": [
    "عمود وہ لکیر ہے جو منحنی پر مخصوص نقطے P(x₀,y₀) میں مماس کے عموداً ہو اور جس کی ڈھلوان −1/f′(x₀) ہو:",
    "عمود هغه کرښه ده چې د منحني په ټاکلي ټکي P(x₀,y₀) کې پر مماس عمودي وي او میلان یې −1/f′(x₀) وي:"
  ],
  "The finite secant quotient requires Δx ≠ 0. The tangent formula requires a finite derivative. The normal slope −1/m requires m ≠ 0; when m = 0, the normal is the vertical line x = x₀. In Figure 4.2, Δy is the actual change and dy = f′(x₀)dx is the tangent-line differential; they generally differ.": [
    "محدود قاطع کے حاصلِ تقسیم کے لیے Δx ≠ 0 ضروری ہے۔ مماس کے فارمولے کے لیے محدود مشتق چاہیے۔ عمود کی ڈھلوان −1/m کے لیے m ≠ 0 ضروری ہے؛ m = 0 پر عمود عمودی لکیر x = x₀ ہے۔ شکل 4.2 میں Δy اصل تبدیلی ہے جبکہ dy = f′(x₀)dx مماس کی لکیر کا تفرقی جز ہے؛ یہ عموماً مختلف ہوتے ہیں۔",
    "د محدود قاطع حاصل قسمت Δx ≠ 0 غواړي. د مماس فورمول محدود مشتق غواړي. د عمود میلان −1/m، m ≠ 0 غواړي؛ که m = 0 وي، عمود عمودي کرښه x = x₀ ده. په شکل 4.2 کې Δy اصلي بدلون دی، خو dy = f′(x₀)dx د مماس کرښې تفاضلي جزء دی؛ عموماً سره توپیر لري."
  ],
  "Find the equations of the tangent and normal lines on a curve y = x² at a point P(2,4).": [
    "منحنی y = x² پر نقطے P(2,4) میں مماس اور عمود کی لکیروں کی مساوات معلوم کریں۔",
    "پر منحني y = x² په P(2,4) ټکي کې د مماس او عمود کرښو معادلې ومومئ."
  ],
  "If the given curve is y = x², then, the slope of the tangent line is the first derivative of the given curve at a particular point P(2,4):": [
    "اگر دی گئی منحنی y = x² ہو تو مخصوص نقطے P(2,4) پر مماس کی ڈھلوان دی گئی منحنی کا پہلا مشتق ہے:",
    "که ورکړل شوې منحني y = x² وي، نو په ټاکلي ټکي P(2,4) کې د مماس میلان د ورکړل شوې منحني لومړی مشتق دی:"
  ],
  "The tangent line (i) on the given curve at a particular point P(2,4) is:": [
    "دی گئی منحنی پر مخصوص نقطے P(2,4) میں مماس کی لکیر (i) یہ ہے:",
    "پر ورکړل شوې منحني په ټاکلي ټکي P(2,4) کې مماس کرښه (i) دا ده:"
  ],
  "The normal-line calculation continues on page 116.": [
    "عمود کی لکیر کا حساب صفحہ 116 پر جاری ہے۔",
    "د عمود کرښې محاسبه په 116 پاڼه کې دوام لري."
  ],
  "The normal line (ii) on the given curve at a particular point P(2,4) is:": [
    "دی گئی منحنی پر مخصوص نقطے P(2,4) میں عمود کی لکیر (ii) یہ ہے:",
    "پر ورکړل شوې منحني په ټاکلي ټکي P(2,4) کې عمود کرښه (ii) دا ده:"
  ],
  "Find the equations of the tangent and normal lines on the curve y = 9 − x² at a point, when y crosses the x-axis.": [
    "منحنی y = 9 − x² کے اس نقطے پر مماس اور عمود کی مساوات معلوم کریں جہاں منحنی x محور کو کاٹتی ہے۔",
    "د y = 9 − x² منحني په هغه ټکي کې د مماس او عمود معادلې ومومئ چې منحني د x محور پرې کوي."
  ],
  "The coordinates of a particular point P at which the given curve y = 9 − x² crosses the x-axis are y = 0. Put y = 0 in y = 9 − x² to obtain a set of points:": [
    "جس مخصوص نقطے P پر دی گئی منحنی y = 9 − x²، x محور کو کاٹتی ہے، وہاں y = 0 ہوتا ہے۔ نقاط کا مجموعہ حاصل کرنے کے لیے y = 9 − x² میں y = 0 رکھیں:",
    "په هغه ټاکلي ټکي P کې چې ورکړل شوې منحني y = 9 − x² د x محور پرې کوي، y = 0 دی. د ټکو د مجموعې د موندلو لپاره په y = 9 − x² کې y = 0 کېږدئ:"
  ],
  "If the given curve is y = 9 − x², then, the slope of the tangent line is the first derivative of the given curve at a particular point P(±3,0):": [
    "اگر دی گئی منحنی y = 9 − x² ہو تو مخصوص نقطے P(±3,0) پر مماس کی ڈھلوان دی گئی منحنی کا پہلا مشتق ہے:",
    "که ورکړل شوې منحني y = 9 − x² وي، نو په ټاکلي ټکي P(±3,0) کې د مماس میلان د ورکړل شوې منحني لومړی مشتق دی:"
  ],
  "The tangent lines (i) on the given curve at the particular points are:": [
    "دی گئی منحنی پر مخصوص نقاط میں مماس کی لکیریں (i) یہ ہیں:",
    "پر ورکړل شوې منحني په ټاکلو ټکو کې مماس کرښې (i) دا دي:"
  ],
  "The normal lines (ii) on the given curve at the particular points are:": [
    "دی گئی منحنی پر مخصوص نقاط میں عمود کی لکیریں (ii) یہ ہیں:",
    "پر ورکړل شوې منحني په ټاکلو ټکو کې عمود کرښې (ii) دا دي:"
  ],
  "i. The tangent equation at a point P(x₀,y₀) is y − y₀ = m(x − x₀). ii. The normal equation at a point P(x₀,y₀) is y − y₀ = −(1/m)(x − x₀).": [
    "i. نقطے P(x₀,y₀) پر مماس کی مساوات y − y₀ = m(x − x₀) ہے۔ ii. نقطے P(x₀,y₀) پر عمود کی مساوات y − y₀ = −(1/m)(x − x₀) ہے۔",
    "i. په P(x₀,y₀) ټکي کې د مماس معادله y − y₀ = m(x − x₀) ده. ii. په P(x₀,y₀) ټکي کې د عمود معادله y − y₀ = −(1/m)(x − x₀) ده."
  ],
  "4.3.3 Angle of intersection of the two curves": [
    "4.3.3 دو منحنیوں کا زاویۂ تقاطع",
    "4.3.3 د دوو منحنیو د تقاطع زاویه"
  ],
  "If m₁ is the slope of the first curve and m₂ is the slope of the second curve, then the angle of intersection in between these two curves at a point of intersection is the angle in between their tangents at that point. This angle takes the notation:": [
    "اگر m₁ پہلی منحنی کی ڈھلوان اور m₂ دوسری منحنی کی ڈھلوان ہو تو نقطۂ تقاطع پر ان دو منحنیوں کا زاویۂ تقاطع اسی نقطے پر ان کے مماسوں کے درمیان زاویہ ہے۔ اس زاویے کی علامتی صورت یہ ہے:",
    "که m₁ د لومړۍ منحني میلان او m₂ د دویمې منحني میلان وي، نو د تقاطع په ټکي کې د دغو دوو منحنیو د تقاطع زاویه په هماغه ټکي کې د هغوی د مماسونو ترمنځ زاویه ده. دا زاویه په دې نښه لیکل کېږي:"
  ],
  "For the smaller nonnegative intersection angle between two finite slopes, use tanθ = |(m₁ − m₂)/(1 + m₁m₂)|, with 0 ≤ θ < π/2. When 1 + m₁m₂ = 0 the tangents are perpendicular, θ = π/2; do not divide by zero. Vertical tangents need direction vectors or a limiting angle calculation.": [
    "دو محدود ڈھلوانوں کے درمیان چھوٹے غیر منفی زاویۂ تقاطع کے لیے tanθ = |(m₁ − m₂)/(1 + m₁m₂)| استعمال کریں، جہاں 0 ≤ θ < π/2 ہے۔ جب 1 + m₁m₂ = 0 ہو تو مماس عموداً ہوتے ہیں اور θ = π/2 ہے؛ صفر سے تقسیم نہ کریں۔ عمودی مماسوں کے لیے سمتی سمتیے یا حدی زاویے کا حساب درکار ہے۔",
    "د دوو محدودو میلانونو ترمنځ د کوچنۍ نامنفي تقاطع زاویې لپاره tanθ = |(m₁ − m₂)/(1 + m₁m₂)| وکاروئ، چې 0 ≤ θ < π/2 وي. کله چې 1 + m₁m₂ = 0 وي، مماسونه عمودي وي او θ = π/2 دی؛ پر صفر وېش مه کوئ. عمودي مماسونه لوري ویکتورونو یا د حدي زاویې محاسبې ته اړتیا لري."
  ],
  "Find the angle of intersection in between the curves y = x³ − 2x + 1 and y = x² + 1 at the point of intersection (2,5).": [
    "منحنیوں y = x³ − 2x + 1 اور y = x² + 1 کا نقطۂ تقاطع (2,5) پر زاویۂ تقاطع معلوم کریں۔",
    "د y = x³ − 2x + 1 او y = x² + 1 منحنیو د تقاطع په (2,5) ټکي کې د تقاطع زاویه ومومئ."
  ],
  "The required angle of intersection in between the given two curves is:": [
    "دی گئی دو منحنیوں کے درمیان مطلوبہ زاویۂ تقاطع یہ ہے:",
    "د ورکړل شوو دوو منحنیو ترمنځ غوښتل شوې د تقاطع زاویه دا ده:"
  ],
  "For point of intersection, solve the system of nonlinear equations for the unknowns x and y. The proof continues on page 117.": [
    "نقطۂ تقاطع کے لیے نامعلوم x اور y کی غیر خطی مساواتوں کا نظام حل کریں۔ ثبوت صفحہ 117 پر جاری ہے۔",
    "د تقاطع د ټکي لپاره د نامعلومو x او y غیرخطي معادلو سیستم حل کړئ. ثبوت په 117 پاڼه کې دوام لري."
  ],
  "Using first equation of the nonlinear system (ii) in second equation to obtain:": [
    "غیر خطی نظام (ii) کی پہلی مساوات دوسری مساوات میں استعمال کرنے سے حاصل ہوتا ہے:",
    "د غیرخطي سیستم (ii) د لومړۍ معادلې په دویمه معادله کې په کارولو ترلاسه کېږي:"
  ],
  "The set of x values is used in first equation of the nonlinear system (ii) to obtain a set of y values:": [
    "y قیمتوں کا مجموعہ حاصل کرنے کے لیے x قیمتوں کا مجموعہ غیر خطی نظام (ii) کی پہلی مساوات میں استعمال ہوتا ہے:",
    "د y ارزښتونو د مجموعې د ترلاسه کولو لپاره د x ارزښتونو مجموعه د غیرخطي سیستم (ii) په لومړۍ معادله کې کارول کېږي:"
  ],
  "This process developed a set of points of intersection: (0,1),(−1,2),(2,5).": [
    "اس عمل سے نقاطِ تقاطع کا مجموعہ (0,1)،(−1,2)،(2,5) حاصل ہوتا ہے۔",
    "دا بهیر د تقاطع د ټکو مجموعه (0,1)،(−1,2)،(2,5) راکوي."
  ],
  "The slope of the first curve at a point (2,5) is:": [
    "نقطے (2,5) پر پہلی منحنی کی ڈھلوان یہ ہے:",
    "په (2,5) ټکي کې د لومړۍ منحني میلان دا دی:"
  ],
  "The slope of the second curve at a point (2,5) is:": [
    "نقطے (2,5) پر دوسری منحنی کی ڈھلوان یہ ہے:",
    "په (2,5) ټکي کې د دویمې منحني میلان دا دی:"
  ],
  "The slopes m₁,m₂ are used in (i) to obtain the angle of intersection in between the given two curves:": [
    "دی گئی دو منحنیوں کا زاویۂ تقاطع حاصل کرنے کے لیے ڈھلوانیں m₁,m₂، (i) میں استعمال کی جاتی ہیں:",
    "د ورکړل شوو دوو منحنیو د تقاطع زاویې د ترلاسه کولو لپاره m₁,m₂ میلانونه په (i) کې کارول کېږي:"
  ],
  "4.3.4 Point on a curve where the tangent is parallel to the given line": [
    "4.3.4 منحنی کا وہ نقطہ جہاں مماس دی گئی لکیر کے متوازی ہو",
    "4.3.4 د منحني هغه ټکی چې مماس یې له ورکړل شوې کرښې سره موازي وي"
  ],
  "Look at the following example; the procedure to find the point on a curve where tangent is parallel to the given line is illustrated in this example.": [
    "درج ذیل مثال دیکھیں؛ اس میں منحنی پر وہ نقطہ معلوم کرنے کا طریقہ واضح کیا گیا ہے جہاں مماس دی گئی لکیر کے متوازی ہو۔",
    "لاندې بېلګه وګورئ؛ په دې بېلګه کې پر منحني د هغه ټکي د موندلو طریقه ښودل شوې چې مماس یې له ورکړل شوې کرښې سره موازي وي."
  ],
  "Find all the points on the curve y = 2x³ + 4x² where tangent line is parallel to the line y = 8x − 4.": [
    "منحنی y = 2x³ + 4x² پر وہ تمام نقاط معلوم کریں جہاں مماس کی لکیر y = 8x − 4 کے متوازی ہو۔",
    "پر منحني y = 2x³ + 4x² ټول هغه ټکي ومومئ چې مماس کرښه یې له y = 8x − 4 سره موازي وي."
  ],
  "Since the given line is y = 8x − 4, slope of the given line = 8. Given curve y = 2x³ + 4x²:": [
    "چونکہ دی گئی لکیر y = 8x − 4 ہے، اس لیے اس کی ڈھلوان = 8 ہے۔ دی گئی منحنی y = 2x³ + 4x²:",
    "ځکه چې ورکړل شوې کرښه y = 8x − 4 ده، نو میلان یې = 8 دی. ورکړل شوې منحني y = 2x³ + 4x²:"
  ],
  "y = 2x³ + 4x² when x = −2. Then:": [
    "جب x = −2 ہو تو y = 2x³ + 4x² ہے۔ تب:",
    "کله چې x = −2 وي، y = 2x³ + 4x² دی. بیا:"
  ],
  "When x = 2/3:": [
    "جب x = 2/3 ہو:",
    "کله چې x = 2/3 وي:"
  ],
  "Example 20’s 0.1453 is in radians; it is approximately 8.32565°. Its prescribed point is (2,5), although the other two intersections are also found. Example 21’s requested points are (−2,0) and (2/3,64/27), pairing each source x with its corresponding y.": [
    "مثال 20 کی قیمت 0.1453 ریڈیئن میں ہے؛ یہ تقریباً 8.32565° ہے۔ اس میں مقرر نقطہ (2,5) ہے، اگرچہ دیگر دو نقاطِ تقاطع بھی معلوم کیے گئے ہیں۔ مثال 21 کے مطلوبہ نقاط (−2,0) اور (2/3,64/27) ہیں، جن میں ماخذ کی ہر x قیمت کو اس کی متعلقہ y قیمت کے ساتھ ملایا گیا ہے۔",
    "په بېلګه 20 کې 0.1453 په رېډیانو دی؛ نږدې 8.32565° کېږي. ټاکلی ټکی یې (2,5) دی، که څه هم نور دوه د تقاطع ټکي هم موندل شوي دي. د بېلګې 21 غوښتل شوي ټکي (−2,0) او (2/3,64/27) دي، چې د سرچینې هر x له خپل اړوند y سره جوړه شوی دی."
  ],
  "Example 18": [
    "مثال 18",
    "بېلګه 18"
  ],
  "Example 18 — continued": [
    "مثال 18 — جاری",
    "بېلګه 18 — دوام"
  ],
  "Example 19": [
    "مثال 19",
    "بېلګه 19"
  ],
  "Example 20": [
    "مثال 20",
    "بېلګه 20"
  ],
  "Example 20 — continued": [
    "مثال 20 — جاری",
    "بېلګه 20 — دوام"
  ],
  "Example 21": [
    "مثال 21",
    "بېلګه 21"
  ],
  "Figure 4.2": [
    "شکل 4.2",
    "شکل 4.2"
  ],
  "4.4 Maxima and Minima": [
    "4.4 زیادہ سے زیادہ اور کم سے کم قیمتیں",
    "4.4 اعظم او اصغر ارزښتونه"
  ],
  "Always the maximum and minimum values of a function can be read from its graphical view. For a quadratic function (whose graph is parabola), the maximum or minimum values can be determined without graphing by finding the vertex algebraically. For functions whose graphs are not known, other techniques are needed. In this unit, we shall see how to use derivatives to determine the maximum and minimum values of a function as well as the intervals where the function is increasing or decreasing.": [
    "تفاعل کی زیادہ سے زیادہ اور کم سے کم قیمتیں اس کے گراف سے پڑھی جا سکتی ہیں۔ دو درجی تفاعل، جس کا گراف قطعِ مکافی ہوتا ہے، کی زیادہ سے زیادہ یا کم سے کم قیمت بغیر گراف بنائے راس کو الجبرائی طریقے سے معلوم کر کے حاصل کی جا سکتی ہے۔ جن تفاعلوں کے گراف معلوم نہ ہوں، ان کے لیے دوسری تکنیکیں درکار ہیں۔ اس اکائی میں ہم دیکھیں گے کہ مشتقات سے تفاعل کی زیادہ سے زیادہ اور کم سے کم قیمتیں اور اس کے بڑھنے یا گھٹنے کے وقفے کیسے معلوم ہوتے ہیں۔",
    "د تابع اعظم او اصغر ارزښتونه د هغې له ګرافه لوستل کېدای شي. د دویمې درجې تابع، چې ګراف یې پارابولا دی، اعظم یا اصغر ارزښت له رسمولو پرته په الجبري ډول د راس په موندلو ټاکل کېدای شي. د هغو تابع ګانو لپاره چې ګرافونه یې معلوم نه وي، نورو طریقو ته اړتیا ده. په دې څپرکي کې به وګورو چې مشتقونه څنګه د تابع اعظم او اصغر ارزښتونه او د زیاتېدو یا کمېدو واټنونه ټاکي."
  ],
  "4.4.1 Increasing and decreasing functions": [
    "4.4.1 بڑھتے اور گھٹتے تفاعل",
    "4.4.1 زیاتېدونکې او کمېدونکې تابع ګانې"
  ],
  "Suppose an ecologist has determined the size of a population of a certain species as a function f(t) of time t (months). If it turns out that the population is increasing until the end of the first year and decreasing thereafter. It is reasonable to expect the population to be maximized at time t = 12 and for the population curve to have a high point at t = 12 as shown in Figure 4.3.": [
    "فرض کریں ایک ماہرِ ماحولیات نے کسی نوع کی آبادی کا حجم، وقت t (مہینوں) کے تفاعل f(t) کے طور پر معلوم کیا ہے۔ اگر آبادی پہلے سال کے آخر تک بڑھے اور اس کے بعد گھٹے تو معقول توقع ہے کہ t = 12 پر آبادی زیادہ سے زیادہ ہوگی اور آبادی کی منحنی t = 12 پر بلند نقطہ رکھے گی، جیسا کہ شکل 4.3 میں ہے۔",
    "فرض کړئ یوه چاپېریال پوه د یوه ډول د نفوس اندازه د وخت t (میاشتو) د f(t) تابع په توګه ټاکلې ده. که نفوس د لومړي کال تر پایه زیات او وروسته کم شي، نو مناسبه تمه دا ده چې په t = 12 کې نفوس اعظم وي او د نفوس منحني په t = 12 کې لوړ ټکی ولري، لکه په شکل 4.3 کې."
  ],
  "If the graph of a function f(t), such as this population curve, is rising throughout the interval 0 < t < 12, then we say that f(t) is strictly increasing on that interval. Similarly, the graph in Figure 4.3 is strictly decreasing on the interval 12 < t < 20. These terms are defined more formally in Figure 4.4.": [
    "اگر f(t) کا گراف، مثلاً یہ آبادی کی منحنی، پورے وقفے 0 < t < 12 میں اوپر اٹھتا ہو تو کہتے ہیں کہ f(t) اس وقفے پر سختی سے بڑھتا ہے۔ اسی طرح شکل 4.3 کا گراف وقفے 12 < t < 20 میں سختی سے گھٹتا ہے۔ شکل 4.4 میں ان اصطلاحات کی زیادہ باقاعدہ تعریف ہے۔",
    "که د f(t) ګراف، لکه دا د نفوس منحني، په ټول واټن 0 < t < 12 کې پورته ځي، وایو چې f(t) په دې واټن کې په کلکه زیاتېدونکې ده. همداسې، د شکل 4.3 ګراف په 12 < t < 20 واټن کې په کلکه کمېدونکی دی. دا اصطلاحات په شکل 4.4 کې لا رسمي تعریف شوي دي."
  ],
  "The function f(x) is strictly increasing on an interval (a,b), if f(x₁) < f(x₂), whenever x₁ < x₂ for x₁ and x₂ on (a,b).": [
    "تفاعل f(x) وقفے (a,b) پر سختی سے بڑھتا ہے اگر اس وقفے کے ہر x₁ اور x₂ کے لیے x₁ < x₂ ہونے پر f(x₁) < f(x₂) ہو۔",
    "تابع f(x) په (a,b) واټن کې په کلکه زیاتېدونکې ده، که په دې واټن کې د هر x₁ او x₂ لپاره له x₁ < x₂ سره f(x₁) < f(x₂) وي."
  ],
  "The function f(x) is strictly decreasing on an interval (a,b), if f(x₁) > f(x₂), whenever x₁ < x₂ for x₁ and x₂ on (a,b).": [
    "تفاعل f(x) وقفے (a,b) پر سختی سے گھٹتا ہے اگر اس وقفے کے ہر x₁ اور x₂ کے لیے x₁ < x₂ ہونے پر f(x₁) > f(x₂) ہو۔",
    "تابع f(x) په (a,b) واټن کې په کلکه کمېدونکې ده، که په دې واټن کې د هر x₁ او x₂ لپاره له x₁ < x₂ سره f(x₁) > f(x₂) وي."
  ],
  "Find the intervals at which the function f(x) = x² is increasing or decreasing.": [
    "وہ وقفے معلوم کریں جن میں تفاعل f(x) = x² بڑھتا یا گھٹتا ہے۔",
    "هغه واټنونه ومومئ چې تابع f(x) = x² پکې زیاتېږي یا کمېږي."
  ],
  "The function f(x) = x² is a parabola passing through the origin. Take any two points x₁,x₂ in the interval (a,b) for which:": [
    "تفاعل f(x) = x² مبدا سے گزرنے والا قطعِ مکافی ہے۔ وقفے (a,b) کے کوئی دو نقاط x₁,x₂ لیں جن کے لیے:",
    "تابع f(x) = x² له مبدا تېرېدونکې پارابولا ده. په (a,b) واټن کې هر دوه ټکي x₁,x₂ واخلئ چې:"
  ],
  "If x₁,x₂ ∈ (0,∞) with condition x₂ > x₁, then f(x) is increasing in (0,∞):": [
    "اگر x₁,x₂ ∈ (0,∞) اور x₂ > x₁ ہوں تو f(x) وقفے (0,∞) میں بڑھتا ہے:",
    "که x₁,x₂ ∈ (0,∞) او x₂ > x₁ وي، نو f(x) په (0,∞) کې زیاتېږي:"
  ],
  "Both (x₂ − x₁) and (x₂ + x₁) are positive when x₂ > x₁.": [
    "x₂ > x₁ ہونے پر (x₂ − x₁) اور (x₂ + x₁) دونوں مثبت ہیں۔",
    "کله چې x₂ > x₁ وي، (x₂ − x₁) او (x₂ + x₁) دواړه مثبت دي."
  ],
  "If x₁,x₂ ∈ (−∞,0) with condition x₂ > x₁, then f(x) is decreasing in (−∞,0):": [
    "اگر x₁,x₂ ∈ (−∞,0) اور x₂ > x₁ ہوں تو f(x) وقفے (−∞,0) میں گھٹتا ہے:",
    "که x₁,x₂ ∈ (−∞,0) او x₂ > x₁ وي، نو f(x) په (−∞,0) کې کمېږي:"
  ],
  "(x₂ − x₁) is positive while (x₂ + x₁) is negative when x₂ > x₁.": [
    "x₂ > x₁ ہونے پر (x₂ − x₁) مثبت جبکہ (x₂ + x₁) منفی ہے۔",
    "کله چې x₂ > x₁ وي، (x₂ − x₁) مثبت او (x₂ + x₁) منفي دی."
  ],
  "4.4.2 Prove that if f(x) is a differentiable function on the open interval (a,b) then": [
    "4.4.2 ثابت کریں کہ اگر f(x) کھلے وقفے (a,b) پر قابلِ تفرق تفاعل ہو تو",
    "4.4.2 ثابته کړئ چې که f(x) په خلاص واټن (a,b) کې تفریق کېدونکې تابع وي، نو"
  ],
  "f(x) is increasing on (a,b) if f′(x) > 0, ∀x ∈ (a,b). f(x) is decreasing on (a,b) if f′(x) < 0, ∀x ∈ (a,b).": [
    "اگر f′(x) > 0، ∀x ∈ (a,b) ہو تو f(x)، (a,b) پر بڑھتا ہے۔ اگر f′(x) < 0، ∀x ∈ (a,b) ہو تو f(x)، (a,b) پر گھٹتا ہے۔",
    "که f′(x) > 0، ∀x ∈ (a,b) وي، f(x) په (a,b) کې زیاتېږي. که f′(x) < 0، ∀x ∈ (a,b) وي، f(x) په (a,b) کې کمېږي."
  ],
  "Proof": [
    "ثبوت",
    "ثبوت"
  ],
  "Let x₁,x₂ ∈ (a,b) such that x₂ > x₁; then there exists a point c between x₁ and x₂ such that:": [
    "فرض کریں x₁,x₂ ∈ (a,b) اور x₂ > x₁ ہیں؛ تب x₁ اور x₂ کے درمیان ایک نقطہ c موجود ہے ایسا کہ:",
    "فرض کړئ x₁,x₂ ∈ (a,b) او x₂ > x₁ دي؛ بیا د x₁ او x₂ ترمنځ یو ټکی c شته چې:"
  ],
  "For f′(c) > 0 and so x₂ − x₁ > 0. Therefore:": [
    "f′(c) > 0 اور x₂ − x₁ > 0 کے لیے، لہٰذا:",
    "د f′(c) > 0 او x₂ − x₁ > 0 لپاره، نو:"
  ],
  "Thus, f is an increasing function. Similarly, the proof of part (ii) can be done which is left as an exercise for the reader.": [
    "یوں f بڑھتا ہوا تفاعل ہے۔ اسی طرح حصہ (ii) کا ثبوت دیا جا سکتا ہے، جو قاری کی مشق کے لیے چھوڑا گیا ہے۔",
    "نو f زیاتېدونکې تابع ده. په ورته ډول د (ii) برخې ثبوت هم کېدای شي، چې د لوستونکي لپاره د تمرین په توګه پرېښودل شوی دی."
  ],
  "If a function f is continuous on [a,b] and differentiable on (a,b), then there exists a point c ∈ (a,b) such that:": [
    "اگر تفاعل f، [a,b] پر متصل اور (a,b) پر قابلِ تفرق ہو تو ایک نقطہ c ∈ (a,b) موجود ہے ایسا کہ:",
    "که تابع f په [a,b] کې پیوسته او په (a,b) کې تفریق کېدونکې وي، نو یو ټکی c ∈ (a,b) شته چې:"
  ],
  "For the decreasing case, x₂ − x₁ > 0 and f′(c) < 0 imply f(x₂) − f(x₁) < 0, hence f(x₂) < f(x₁). Differentiability on (a,b) supplies continuity on the smaller closed interval [x₁,x₂], so the mean value theorem applies.": [
    "گھٹنے والی صورت میں x₂ − x₁ > 0 اور f′(c) < 0 سے f(x₂) − f(x₁) < 0، اور اس لیے f(x₂) < f(x₁) حاصل ہوتا ہے۔ (a,b) پر قابلِ تفرق ہونے سے چھوٹے بند وقفے [x₁,x₂] پر اتصال ملتا ہے، لہٰذا اوسط قدر کا قضیہ لاگو ہوتا ہے۔",
    "په کمېدونکي حالت کې x₂ − x₁ > 0 او f′(c) < 0 دا پایله ورکوي چې f(x₂) − f(x₁) < 0، نو f(x₂) < f(x₁) دی. په (a,b) کې تفریق کېدنه په کوچني تړلي واټن [x₁,x₂] کې پیوستون راکوي، نو د منځني ارزښت قضیه تطبیقېږي."
  ],
  "Determine the values of x at which f(x) = x² + 2x − 3 is increasing or decreasing. Also find the point at which the function is neither increasing nor decreasing.": [
    "x کی وہ قیمتیں معلوم کریں جن پر f(x) = x² + 2x − 3 بڑھتا یا گھٹتا ہے۔ وہ نقطہ بھی معلوم کریں جہاں تفاعل نہ بڑھتا ہے نہ گھٹتا ہے۔",
    "د x هغه ارزښتونه ومومئ چې f(x) = x² + 2x − 3 پکې زیاتېږي یا کمېږي. هغه ټکی هم ومومئ چې تابع پکې نه زیاتېږي او نه کمېږي."
  ],
  "For graphical view, the given function through completing square:": [
    "گرافی منظر کے لیے دیے گئے تفاعل کا مکمل مربع بنانے سے:",
    "د ګرافیکي بڼې لپاره د ورکړل شوې تابع مربع په بشپړولو:"
  ],
  "is compared with the general equation of parabola f(x) = a(x − h)² + k to obtain a parabola with vertex (−1,−4) that opens upward (a = 1 is positive). The graph through points (−4,5) and (2,5) is shown in Figure 4.5.": [
    "اسے قطعِ مکافی کی عمومی مساوات f(x) = a(x − h)² + k سے ملانے پر راس (−1,−4) والا اوپر کھلنے والا قطعِ مکافی ملتا ہے (a = 1 مثبت ہے)۔ نقاط (−4,5) اور (2,5) سے گزرنے والا گراف شکل 4.5 میں ہے۔",
    "دا د پارابولا له عمومي معادلې f(x) = a(x − h)² + k سره په پرتله کولو د (−1,−4) راس لرونکې، پورته خلاصېدونکې پارابولا راکوي (a = 1 مثبت دی). له (−4,5) او (2,5) ټکو تېرېدونکی ګراف په شکل 4.5 کې دی."
  ],
  "The derivative with respect to x is the slope of the parabola:": [
    "x کے لحاظ سے مشتق قطعِ مکافی کی ڈھلوان ہے:",
    "د x په نسبت مشتق د پارابولا میلان دی:"
  ],
  "If the slope is positive, then:": [
    "اگر ڈھلوان مثبت ہو تو:",
    "که میلان مثبت وي، نو:"
  ],
  "The function is increasing in (−1,∞). If the slope is negative:": [
    "تفاعل (−1,∞) میں بڑھتا ہے۔ اگر ڈھلوان منفی ہو:",
    "تابع په (−1,∞) کې زیاتېږي. که میلان منفي وي:"
  ],
  "The function is decreasing in (−∞,−1). If the slope is zero:": [
    "تفاعل (−∞,−1) میں گھٹتا ہے۔ اگر ڈھلوان صفر ہو:",
    "تابع په (−∞,−1) کې کمېږي. که میلان صفر وي:"
  ],
  "The given function is neither increasing nor decreasing at the vertex (−1,−4).": [
    "دیا گیا تفاعل راس (−1,−4) پر نہ بڑھتا ہے نہ گھٹتا ہے۔",
    "ورکړل شوې تابع په (−1,−4) راس کې نه زیاتېږي او نه کمېږي."
  ],
  "4.4.3 Examination of a given function for extreme values": [
    "4.4.3 انتہانی قیمتوں کے لیے دیے گئے تفاعل کی جانچ",
    "4.4.3 د انتهايي ارزښتونو لپاره د ورکړل شوې تابع څېړنه"
  ],
  "Typically the extrema of a continuous function occur either at endpoints of the interval or at points where the graph has a “peak” or “valley” (points where the graph is higher or lower than all nearby points). For example, f(x) in Figure 4.6 has peaks at B and D and valleys at C and E. Peaks and valleys are what we call the relative extrema.": [
    "عموماً متصل تفاعل کی انتہانی قیمتیں وقفے کے آخری نقاط پر یا گراف کی چوٹیوں اور وادیوں پر ہوتی ہیں، یعنی جہاں گراف تمام قریبی نقاط سے بلند یا پست ہو۔ مثلاً شکل 4.6 میں f(x) کی چوٹیاں B اور D اور وادیاں C اور E پر ہیں۔ ان چوٹیوں اور وادیوں کو نسبتی انتہائیں کہتے ہیں۔",
    "عموماً د پیوستې تابع انتهايي ارزښتونه د واټن په وروستیو ټکو یا د ګراف په څوکو او کندو کې وي، یعنې هلته چې ګراف له ټولو نږدې ټکو لوړ یا ټیټ وي. د بېلګې په توګه په شکل 4.6 کې f(x) په B او D کې څوکې او په C او E کې کندې لري. دې څوکو او کندو ته نسبي انتهاوې وایو."
  ],
  "The exact location of a relative maximum or minimum rather than a graphical approximation can normally be found by using derivatives. The concept developed is as under:": [
    "گرافی تخمینے کے بجائے نسبتی زیادہ سے زیادہ یا کم سے کم قیمت کا عین مقام عموماً مشتقات سے معلوم کیا جا سکتا ہے۔ تصور اس طرح وضع ہوتا ہے:",
    "د ګرافیکي اټکل پر ځای د نسبي اعظم یا اصغر دقیق موقعیت عموماً د مشتقونو په وسیله موندل کېدای شي. مفهوم په دې ډول جوړېږي:"
  ],
  "Let f(x) be a function as a roller coaster track with a roller coaster car moving from left to right along the graph in Figure 4.6. As the car moves up towards a peak, its floor tilts upward. At the": [
    "فرض کریں f(x) رولر کوسٹر کی پٹڑی ہے اور اس کی گاڑی شکل 4.6 کے گراف پر بائیں سے دائیں چلتی ہے۔ جب گاڑی چوٹی کی طرف اوپر جاتی ہے تو اس کا فرش اوپر جھکتا ہے۔ اس",
    "فرض کړئ f(x) د رولر کوسټر پټلۍ ده او موټر یې د شکل 4.6 پر ګراف له چپ څخه ښي لوري ته خوځېږي. کله چې موټر څوکې ته پورته ځي، فرش یې پورته کږېږي. په هغه"
  ],
  "Increasing and decreasing describe behavior on intervals. At the vertex in Example 23, the derivative is zero and the function changes from decreasing to increasing; “neither” refers to its zero instantaneous slope. The roller-coaster explanation continues on page 121.": [
    "بڑھنا اور گھٹنا وقفوں پر رویہ بیان کرتے ہیں۔ مثال 23 کے راس پر مشتق صفر ہے اور تفاعل گھٹنے سے بڑھنے کی طرف بدلتا ہے؛ ”نہ بڑھتا نہ گھٹتا“ سے مراد اس کی صفر لمحاتی ڈھلوان ہے۔ رولر کوسٹر کی وضاحت صفحہ 121 پر جاری ہے۔",
    "زیاتېدل او کمېدل په واټنونو کې چلند بیانوي. د بېلګې 23 په راس کې مشتق صفر دی او تابع له کمېدو څخه زیاتېدو ته اوړي؛ «نه زیاتېدل نه کمېدل» د صفر شېبه ییز میلان مانا لري. د رولر کوسټر تشریح په 121 پاڼه کې دوام لري."
  ],
  "Roller-coaster analogy — continued": [
    "رولر کوسٹر کی مثال — جاری",
    "د رولر کوسټر تشبیه — دوام"
  ],
  "instant the car reaches the peak, its floor is level, but then it begins to tilt downward as the car rolls down toward a valley. At any point along the graph, the floor of the car (a straight-line segment in the figure) represents the tangent line to the graph at that point. Using this analogy, we see that as the car passes through the peaks and valleys at A,B,C, the tangent line is horizontal and has slope 0. At peak D and valley E, however, a real roller coaster car would have trouble. It would fly off the track at peak D and be unable to make the 90° change of direction at valley E. There is no tangent line at D or E because of the sharp corners.": [
    "لمحے جب گاڑی چوٹی پر پہنچتی ہے اس کا فرش افقی ہوتا ہے، پھر وادی کی طرف اترتے ہوئے نیچے جھکنے لگتا ہے۔ گراف کے ہر نقطے پر گاڑی کا فرش، جو شکل میں سیدھی لکیر کا قطعہ ہے، اسی نقطے کے مماس کو ظاہر کرتا ہے۔ اس مثال سے دیکھتے ہیں کہ A,B,C کی چوٹیوں اور وادیوں سے گزرتے ہوئے مماس افقی ہے اور اس کی ڈھلوان 0 ہے۔ مگر حقیقی رولر کوسٹر کو چوٹی D اور وادی E پر مشکل ہوگی: چوٹی D پر گاڑی پٹڑی سے اڑ جائے گی اور وادی E پر سمت میں 90° تبدیلی نہیں کر سکے گی۔ تیز کونوں کی وجہ سے D یا E پر مماس موجود نہیں۔",
    "شېبه کې چې موټر څوکې ته رسېږي، فرش یې هوار وي، خو بیا کندې ته د ښکته کېدو پر مهال ښکته کږېږي. د ګراف په هر ټکي کې د موټر فرش، چې په شکل کې د مستقیمې کرښې ټوټه ده، په هماغه ټکي کې مماس ښيي. له دې تشبیه وینو چې د A,B,C څوکو او کندو د تېرېدو پر مهال مماس افقي دی او میلان یې 0 دی. خو ریښتینی رولر کوسټر به په څوکه D او کنده E کې ستونزه ولري: په D کې به له پټلۍ والوځي او په E کې به د 90° لوري بدلون ونه شي کړای. د تېرو کونجونو له امله په D یا E کې مماس کرښه نشته."
  ],
  "Thus, the points where a peak or a valley occurs are the points where the tangent line is horizontal and has slope 0 or where no tangent line is defined. The slope of the tangent line to the graph of f(x) at P(x,f(x)) is the value of f′(x).": [
    "لہٰذا چوٹی یا وادی کے نقاط وہ ہیں جہاں مماس افقی اور اس کی ڈھلوان 0 ہو، یا جہاں مماس معین نہ ہو۔ f(x) کے گراف پر P(x,f(x)) میں مماس کی ڈھلوان f′(x) کی قیمت ہے۔",
    "نو د څوکې یا کندې ټکي هغه دي چې مماس پکې افقي او میلان یې 0 وي، یا مماس پکې تعریف شوی نه وي. د f(x) پر ګراف په P(x,f(x)) کې د مماس میلان د f′(x) ارزښت دی."
  ],
  "The source text refers to peaks/valleys at A,B,C, but A is the left endpoint in the drawing. The diagram prints “No tangent” beside A,B,D,E although B is drawn as a smooth peak; these labels are preserved as printed. Smooth interior extrema have zero derivative; corners may have no finite derivative. Endpoint classification must use the chosen domain.": [
    "ماخذ A,B,C پر چوٹیوں اور وادیوں کا ذکر کرتا ہے، لیکن شکل میں A بایاں آخری نقطہ ہے۔ شکل A,B,D,E کے پاس “No tangent” لکھتی ہے، حالانکہ B ہموار چوٹی دکھایا گیا ہے؛ یہ لیبل مطبوعہ صورت میں برقرار ہیں۔ ہموار اندرونی انتہاؤں کا مشتق صفر ہوتا ہے؛ کونوں پر محدود مشتق نہ بھی ہو۔ آخری نقطے کی درجہ بندی منتخب دائرۂ کار کے مطابق ہونی چاہیے۔",
    "سرچینه په A,B,C کې څوکې او کندې یادوي، خو په شکل کې A چپ وروستی ټکی دی. شکل د A,B,D,E ترڅنګ “No tangent” لیکي، که څه هم B هواره څوکه رسم شوې؛ دا لېبلونه د چاپ په بڼه ساتل شوي دي. د هوارو داخلي انتهاوو مشتق صفر وي؛ په کونجونو کې ښايي محدود مشتق نه وي. د وروستي ټکي طبقه بندي باید ټاکل شوې د تعریف ساحه په پام کې ونیسي."
  ],
  "A. Relative Maximum and Relative Minimum": [
    "A. نسبتی زیادہ سے زیادہ اور نسبتی کم سے کم قیمت",
    "A. نسبي اعظم او نسبي اصغر"
  ],
  "The function f(x) is said to have a relative maximum at a number c if f(c) ≥ f(x) for all x in an open interval containing c. Also, it is said to have a relative minimum at a number d if f(d) ≤ f(x) for all x in an open interval containing d. In general, the relative maxima and relative minima are called relative extrema.": [
    "کہتے ہیں کہ f(x) کی عدد c پر نسبتی زیادہ سے زیادہ قیمت ہے اگر c کو شامل کرنے والے کسی کھلے وقفے کے تمام x کے لیے f(c) ≥ f(x) ہو۔ اسی طرح عدد d پر نسبتی کم سے کم قیمت ہے اگر d کو شامل کرنے والے کسی کھلے وقفے کے تمام x کے لیے f(d) ≤ f(x) ہو۔ عمومی طور پر نسبتی زیادہ سے زیادہ اور کم سے کم قیمتوں کو نسبتی انتہائیں کہتے ہیں۔",
    "وایو چې f(x) په عدد c کې نسبي اعظم لري، که په یوه خلاص واټن کې چې c رانغاړي، د ټولو x لپاره f(c) ≥ f(x) وي. همدارنګه په عدد d کې نسبي اصغر لري، که په یوه خلاص واټن کې چې d رانغاړي، د ټولو x لپاره f(d) ≤ f(x) وي. عموماً نسبي اعظم او نسبي اصغر ته نسبي انتهاوې ویل کېږي."
  ],
  "B. Critical Value and Critical Point": [
    "B. بحرانی قیمت اور بحرانی نقطہ",
    "B. بحراني ارزښت او بحراني ټکی"
  ],
  "Suppose f(x) is defined at a number c and either f′(c) = 0 or f′(c) does not exist. Then c is called a critical value of f(x), and P(c,f(c)) on the graph is called a critical point. If f(c) is not defined, then c cannot be a critical value. If there is a relative maximum at c, f(c) is the maximum value; similarly f(c) is the minimum value at a relative minimum.": [
    "فرض کریں f(x) عدد c پر معین ہے اور یا f′(c) = 0 ہے یا f′(c) موجود نہیں۔ تب c، f(x) کی بحرانی قیمت اور گراف پر P(c,f(c)) بحرانی نقطہ کہلاتا ہے۔ اگر f(c) معین نہ ہو تو c بحرانی قیمت نہیں ہو سکتا۔ اگر c پر نسبتی زیادہ سے زیادہ قیمت ہو تو f(c) زیادہ سے زیادہ قیمت ہے؛ اسی طرح نسبتی کم سے کم پر f(c) کم سے کم قیمت ہے۔",
    "فرض کړئ f(x) په عدد c کې تعریف شوې ده او یا f′(c) = 0 دی یا f′(c) نشته. بیا c د f(x) بحراني ارزښت او پر ګراف P(c,f(c)) بحراني ټکی بلل کېږي. که f(c) تعریف شوې نه وي، c بحراني ارزښت نه شي کېدای. که په c کې نسبي اعظم وي، f(c) اعظم ارزښت دی؛ همداسې په نسبي اصغر کې f(c) اصغر ارزښت دی."
  ],
  "Find the critical values: (a) f(x) = 4x³ − 5x² − 8x + 20; (b) \\(f(x)=\\frac{x^2}{x-2}\\); (c) \\(f(x)=12x^{1/2}-2x^{3/2}\\); (d) \\(f(x)=3x^{4/3}-12x^{1/3}\\); (e) \\(f(x)=6x^{2/3}-4x\\).": [
    "بحرانی قیمتیں معلوم کریں: (a) f(x) = 4x³ − 5x² − 8x + 20؛ (b) \\(f(x)=\\frac{x^2}{x-2}\\)؛ (c) \\(f(x)=12x^{1/2}-2x^{3/2}\\)؛ (d) \\(f(x)=3x^{4/3}-12x^{1/3}\\)؛ (e) \\(f(x)=6x^{2/3}-4x\\)۔",
    "بحراني ارزښتونه ومومئ: (a) f(x) = 4x³ − 5x² − 8x + 20؛ (b) \\(f(x)=\\frac{x^2}{x-2}\\)؛ (c) \\(f(x)=12x^{1/2}-2x^{3/2}\\)؛ (d) \\(f(x)=3x^{4/3}-12x^{1/3}\\)؛ (e) \\(f(x)=6x^{2/3}-4x\\)."
  ],
  "a. The first derivative is:": [
    "a. پہلا مشتق یہ ہے:",
    "a. لومړی مشتق دا دی:"
  ],
  "It is defined for all x. Set f′(x) = 0:": [
    "یہ تمام x کے لیے معین ہے۔ f′(x) = 0 رکھیں:",
    "دا د ټولو x لپاره تعریف شوی دی. f′(x) = 0 کېږدئ:"
  ],
  "b. The first derivative is:": [
    "b. پہلا مشتق یہ ہے:",
    "b. لومړی مشتق دا دی:"
  ],
  "The derivative is not defined at x = 2, and the original function is not defined at x = 2. So x = 2 is not a critical value. Set f′(x) = 0:": [
    "مشتق x = 2 پر معین نہیں اور اصل تفاعل بھی x = 2 پر معین نہیں۔ لہٰذا x = 2 بحرانی قیمت نہیں۔ f′(x) = 0 رکھیں:",
    "مشتق په x = 2 کې تعریف شوی نه دی او اصلي تابع هم په x = 2 کې تعریف شوې نه ده. نو x = 2 بحراني ارزښت نه دی. f′(x) = 0 کېږدئ:"
  ],
  "Parts (c)–(e) continue on page 122.": [
    "حصے (c)–(e) صفحہ 122 پر جاری ہیں۔",
    "د (c)–(e) برخې په 122 پاڼه کې دوام لري."
  ],
  "c. The first derivative is:": [
    "c. پہلا مشتق یہ ہے:",
    "c. لومړی مشتق دا دی:"
  ],
  "The derivative is not defined at x = 0, but the original function f(x) is defined at x = 0: f(0) = 12(0)¹/² − 2(0)³/² = 0. So x = 0 is a critical value. For other values, set f′(x) = 0:": [
    "مشتق x = 0 پر معین نہیں، مگر اصل تفاعل f(x) وہاں معین ہے: f(0) = 12(0)¹/² − 2(0)³/² = 0۔ اس لیے x = 0 بحرانی قیمت ہے۔ دوسری قیمتوں کے لیے f′(x) = 0 رکھیں:",
    "مشتق په x = 0 کې تعریف شوی نه دی، خو اصلي تابع f(x) هلته تعریف شوې ده: f(0) = 12(0)¹/² − 2(0)³/² = 0. نو x = 0 بحراني ارزښت دی. د نورو ارزښتونو لپاره f′(x) = 0 کېږدئ:"
  ],
  "Thus, the critical values are x = 0,2.": [
    "لہٰذا بحرانی قیمتیں x = 0,2 ہیں۔",
    "نو بحراني ارزښتونه x = 0,2 دي."
  ],
  "d. The derivative is:": [
    "d. مشتق یہ ہے:",
    "d. مشتق دا دی:"
  ],
  "The derivative fails to exist when x = 0, but the original function is defined at x = 0, so x = 0 is a critical value. If x ≠ 0, f′(x) is zero only when 4x − 4 = 0, or x = 1. Thus the critical values are 0 and 1.": [
    "x = 0 پر مشتق موجود نہیں، مگر اصل تفاعل وہاں معین ہے، اس لیے x = 0 بحرانی قیمت ہے۔ اگر x ≠ 0 ہو تو f′(x) صرف 4x − 4 = 0، یعنی x = 1 پر صفر ہے۔ لہٰذا بحرانی قیمتیں 0 اور 1 ہیں۔",
    "په x = 0 کې مشتق نشته، خو اصلي تابع هلته تعریف شوې ده، نو x = 0 بحراني ارزښت دی. که x ≠ 0 وي، f′(x) یوازې هغه وخت صفر دی چې 4x − 4 = 0، یعنې x = 1 وي. نو بحراني ارزښتونه 0 او 1 دي."
  ],
  "e. The derivative is:": [
    "e. مشتق یہ ہے:",
    "e. مشتق دا دی:"
  ],
  "The derivative fails to exist when x = 0, but f(x) is defined when x = 0, so x = 0 is a critical value. If x ≠ 0, f′(x) is zero only when the numerator 4 − 4x¹/³ is zero, for x = 1. Thus the critical values are 0 and 1.": [
    "x = 0 پر مشتق موجود نہیں، مگر f(x) وہاں معین ہے، اس لیے x = 0 بحرانی قیمت ہے۔ اگر x ≠ 0 ہو تو f′(x) صرف تب صفر ہے جب صورت 4 − 4x¹/³ صفر ہو، یعنی x = 1 پر۔ لہٰذا بحرانی قیمتیں 0 اور 1 ہیں۔",
    "په x = 0 کې مشتق نشته، خو f(x) هلته تعریف شوې ده، نو x = 0 بحراني ارزښت دی. که x ≠ 0 وي، f′(x) یوازې هغه وخت صفر دی چې صورت 4 − 4x¹/³ صفر وي، یعنې په x = 1 کې. نو بحراني ارزښتونه 0 او 1 دي."
  ],
  "The last printed fraction in (e) changes 4 to −4 in its numerator. The correct fraction is (4 − 4∛x)/∛x, consistent with the next sentence and critical value 1. In (d),(e), fractional thirds denote real cube roots, including negative x. In (c), the real domain is x ≥ 0; 0 is a source-defined critical endpoint with no finite standard derivative.": [
    "(e) کے آخری مطبوعہ کسر کی صورت میں 4 کو −4 کر دیا گیا ہے۔ درست کسر (4 − 4∛x)/∛x ہے، جو اگلے جملے اور بحرانی قیمت 1 سے مطابقت رکھتا ہے۔ (d),(e) میں تہائی کسری قوتیں حقیقی مکعبی جذر ہیں اور منفی x بھی شامل ہیں۔ (c) کا حقیقی دائرۂ کار x ≥ 0 ہے؛ 0 ماخذ کی تعریف کے مطابق بحرانی آخری نقطہ ہے، جس پر محدود معیاری مشتق نہیں۔",
    "په (e) کې د وروستي چاپ شوي کسر په صورت کې 4 په −4 بدل شوی دی. سم کسر (4 − 4∛x)/∛x دی، چې له راتلونکې جملې او بحراني ارزښت 1 سره برابر دی. په (d),(e) کې کسري درېیم توانونه حقیقي مکعبي ریښې دي او منفي x هم رانغاړي. د (c) حقیقي د تعریف ساحه x ≥ 0 ده؛ 0 د سرچینې له تعریف سره سم بحراني وروستی ټکی دی چې محدود معیاري مشتق نه لري."
  ],
  "Theorem 4.1": [
    "قضیہ 4.1",
    "قضیه 4.1"
  ],
  "If a continuous function f(x) has a relative extremum at c, then c must be a critical value of f(x).": [
    "اگر متصل تفاعل f(x) کی c پر نسبتی انتہا ہو تو c لازماً f(x) کی بحرانی قیمت ہے۔",
    "که پیوسته تابع f(x) په c کې نسبي انتها ولري، نو c باید د f(x) بحراني ارزښت وي."
  ],
  "This statement uses the source definition that includes points where the derivative does not exist. For an interior local extremum where a derivative exists, Fermat’s theorem gives f′(c) = 0. Endpoint extrema require domain-aware treatment.": [
    "یہ بیان ماخذ کی وہ تعریف استعمال کرتا ہے جس میں ایسے نقاط بھی شامل ہیں جہاں مشتق موجود نہیں۔ اندرونی مقامی انتہا پر مشتق موجود ہو تو فرما کا قضیہ f′(c) = 0 دیتا ہے۔ آخری نقاط کی انتہاؤں میں دائرۂ کار کو مدنظر رکھنا ضروری ہے۔",
    "دا بیان د سرچینې هغه تعریف کاروي چې د مشتق د نه موجودیت ټکي هم رانغاړي. په داخلي محلي انتها کې چې مشتق موجود وي، د فرما قضیه f′(c) = 0 ورکوي. د وروستیو ټکو انتهاوې د تعریف ساحې ته پام غواړي."
  ],
  "The function f(x) is defined by f(x) = x³ − 3x² − 9x + 1. Determine the intervals at which the function is strictly increasing or decreasing.": [
    "تفاعل f(x) = x³ − 3x² − 9x + 1 سے معین ہے۔ وہ وقفے معلوم کریں جن میں تفاعل سختی سے بڑھتا یا گھٹتا ہے۔",
    "تابع f(x) = x³ − 3x² − 9x + 1 ده. هغه واټنونه ومومئ چې تابع پکې په کلکه زیاتېږي یا کمېږي."
  ],
  "First, find the derivative:": [
    "پہلے مشتق معلوم کریں:",
    "لومړی مشتق ومومئ:"
  ],
  "For critical values set f′(x) = 0:": [
    "بحرانی قیمتوں کے لیے f′(x) = 0 رکھیں:",
    "د بحراني ارزښتونو لپاره f′(x) = 0 کېږدئ:"
  ],
  "These critical values divide the x-axis into three parts, as shown in Figure 4.7. Select a typical number from each interval; for example −2,0,4, evaluate the derivative and mark each interval as increasing or decreasing according to whether the derivative is positive or negative respectively.": [
    "یہ بحرانی قیمتیں x محور کو تین حصوں میں بانٹتی ہیں، جیسا کہ شکل 4.7 میں ہے۔ ہر وقفے سے ایک نمائندہ عدد، مثلاً −2,0,4 منتخب کریں؛ مشتق کی قیمت معلوم کریں اور مشتق کے بالترتیب مثبت یا منفی ہونے کے مطابق ہر وقفے کو بڑھتا یا گھٹتا نشان زد کریں۔",
    "دا بحراني ارزښتونه د x محور په دریو برخو وېشي، لکه په شکل 4.7 کې. له هر واټن څخه یو استازی عدد، لکه −2,0,4 وټاکئ؛ مشتق محاسبه کړئ او هر واټن د مشتق د مثبت یا منفي کېدو له مخې په ترتیب زیاتېدونکی یا کمېدونکی ونوموئ."
  ],
  "Thus, f(x) increases for x < −1 and x > 3, but decreases in −1 < x < 3.": [
    "لہٰذا f(x)، x < −1 اور x > 3 کے لیے بڑھتا ہے، مگر −1 < x < 3 میں گھٹتا ہے۔",
    "نو f(x) د x < −1 او x > 3 لپاره زیاتېږي، خو په −1 < x < 3 کې کمېږي."
  ],
  "Draw the function f(x) = x³ − 3x² − 9x + 1 and its derivative f′(x) = 3x² − 6x − 9. Use these graphs to tell about: (a) When f′(x) is positive, what does that mean in terms of the graph of f(x)? (b) When the graph of f(x) is decreasing, what does that mean in terms of the graph of f′(x)?": [
    "تفاعل f(x) = x³ − 3x² − 9x + 1 اور اس کا مشتق f′(x) = 3x² − 6x − 9 رسم کریں۔ ان گرافوں سے بتائیں: (a) f′(x) مثبت ہو تو f(x) کے گراف کے لحاظ سے کیا مطلب ہے؟ (b) f(x) کا گراف گھٹ رہا ہو تو f′(x) کے گراف کے لحاظ سے کیا مطلب ہے؟",
    "تابع f(x) = x³ − 3x² − 9x + 1 او مشتق یې f′(x) = 3x² − 6x − 9 رسم کړئ. له دې ګرافونو ووایئ: (a) که f′(x) مثبت وي، د f(x) د ګراف په اړه څه مانا لري؟ (b) که د f(x) ګراف کمېدونکی وي، د f′(x) د ګراف په اړه څه مانا لري؟"
  ],
  "The graphs of f(x) = x³ − 3x² − 9x + 1 and f′(x) = 3x² − 6x − 9 are shown in Figure 4.8.": [
    "f(x) = x³ − 3x² − 9x + 1 اور f′(x) = 3x² − 6x − 9 کے گراف شکل 4.8 میں دکھائے گئے ہیں۔",
    "د f(x) = x³ − 3x² − 9x + 1 او f′(x) = 3x² − 6x − 9 ګرافونه په شکل 4.8 کې ښودل شوي دي."
  ],
  "The graphs develop the idea that the critical values of f(x) are always intercepts for the graph of f′(x) = 3x² − 6x − 9: If f′(x) is positive, f(x) is increasing. If f′(x) is negative, f(x) is decreasing.": [
    "گرافوں سے یہ خیال ملتا ہے کہ f(x) کی بحرانی قیمتیں ہمیشہ f′(x) = 3x² − 6x − 9 کے گراف کے محور قطع ہیں: اگر f′(x) مثبت ہو تو f(x) بڑھتا ہے۔ اگر f′(x) منفی ہو تو f(x) گھٹتا ہے۔",
    "ګرافونه دا مفکوره ورکوي چې د f(x) بحراني ارزښتونه تل د f′(x) = 3x² − 6x − 9 د ګراف محوري پرېکونونه دي: که f′(x) مثبت وي، f(x) زیاتېږي. که f′(x) منفي وي، f(x) کمېږي."
  ],
  "For this polynomial the critical values are derivative zeros, so they are x-intercepts of f′. In general a critical point can also have an undefined derivative, and then need not be an intercept of a derivative graph.": [
    "اس کثیرالحدی کی بحرانی قیمتیں مشتق کے صفر ہیں، اس لیے وہ f′ کے x محور قطع ہیں۔ عمومی طور پر بحرانی نقطے پر مشتق غیر معین بھی ہو سکتا ہے، اور تب ضروری نہیں کہ وہ مشتق کے گراف کا محور قطع ہو۔",
    "د دې کثیرالحدۍ بحراني ارزښتونه د مشتق صفرونه دي، نو د f′ د x محور پرېکونونه دي. په عمومي ډول بحراني ټکی نامعین مشتق هم لرلای شي، او بیا اړ نه دی چې د مشتق د ګراف محوري پرېکون وي."
  ],
  "4.4.4 State the second derivatives rule to find the extreme values of a function at a point": [
    "4.4.4 کسی نقطے پر تفاعل کی انتہانی قیمتیں معلوم کرنے کے لیے دوسرے مشتق کا قاعدہ بیان کریں",
    "4.4.4 په یوه ټکي کې د تابع د انتهايي ارزښتونو د موندلو لپاره د دویم مشتق قاعده بیان کړئ"
  ],
  "The first derivative of a function can be used to determine whether the function is increasing or decreasing on a given interval. We shall use this information to develop a procedure called the first derivative test for classifying a given point as a relative maximum, a relative minimum, or neither.": [
    "پہلے مشتق سے معلوم کیا جا سکتا ہے کہ تفاعل دیے گئے وقفے میں بڑھتا ہے یا گھٹتا ہے۔ اس معلومات سے ہم پہلے مشتق کا امتحان نامی طریقہ بنائیں گے، جو دیے گئے نقطے کو نسبتی زیادہ سے زیادہ، نسبتی کم سے کم یا ان دونوں میں سے کوئی نہیں قرار دیتا ہے۔",
    "لومړی مشتق ټاکلای شي چې تابع په ورکړل شوي واټن کې زیاتېږي که کمېږي. له دې معلوماتو به د لومړي مشتق ازموینه جوړه کړو، چې ټاکلی ټکی نسبي اعظم، نسبي اصغر یا له دواړو څخه هېڅ یو ونه بولي."
  ],
  "The steps involved in first-derivative test for relative extrema are: 1. Find all critical values of f(x), that is, all c such that f(c) is defined and either f′(c) = 0 or f′(c) does not exist.": [
    "نسبتی انتہاؤں کے پہلے مشتق کے امتحان کے مراحل یہ ہیں: 1. f(x) کی تمام بحرانی قیمتیں معلوم کریں، یعنی وہ تمام c جن پر f(c) معین ہو اور یا f′(c) = 0 ہو یا f′(c) موجود نہ ہو۔",
    "د نسبي انتهاوو د لومړي مشتق د ازموینې ګامونه دا دي: 1. د f(x) ټول بحراني ارزښتونه ومومئ، یعنې ټول هغه c چې f(c) پکې تعریف شوې وي او یا f′(c) = 0 وي یا f′(c) موجود نه وي."
  ],
  "2. The point (c,f(c)) is a relative maximum if f′(x) > 0 (rising) for all x in an open interval (a,c) to the left of c, and f′(x) < 0 (falling) for all x in an open interval (c,b) to the right of c.": [
    "2. نقطہ (c,f(c)) نسبتی زیادہ سے زیادہ ہے اگر c کے بائیں کھلے وقفے (a,c) کے تمام x کے لیے f′(x) > 0 (بڑھتا) اور c کے دائیں کھلے وقفے (c,b) کے تمام x کے لیے f′(x) < 0 (گھٹتا) ہو۔",
    "2. ټکی (c,f(c)) نسبي اعظم دی، که د c چپ لوري په خلاص واټن (a,c) کې د ټولو x لپاره f′(x) > 0 (پورته کېدونکی) او ښي لوري په خلاص واټن (c,b) کې د ټولو x لپاره f′(x) < 0 (ښکته کېدونکی) وي."
  ],
  "3. The point (c,f(c)) is a relative minimum if f′(x) < 0 (falling) for all x in (a,c) to the left, and f′(x) > 0 (rising) for all x in (c,b) to the right.": [
    "3. نقطہ (c,f(c)) نسبتی کم سے کم ہے اگر بائیں وقفے (a,c) کے تمام x کے لیے f′(x) < 0 (گھٹتا) اور دائیں وقفے (c,b) کے تمام x کے لیے f′(x) > 0 (بڑھتا) ہو۔",
    "3. ټکی (c,f(c)) نسبي اصغر دی، که چپ لوري په (a,c) کې د ټولو x لپاره f′(x) < 0 (ښکته کېدونکی) او ښي لوري په (c,b) کې د ټولو x لپاره f′(x) > 0 (پورته کېدونکی) وي."
  ],
  "4. The point (c,f(c)) is not an extremum if f′ has the same sign in (a,c) and (c,b) on both sides of c.": [
    "4. اگر c کے دونوں طرف (a,c) اور (c,b) میں f′ کی علامت یکساں ہو تو نقطہ (c,f(c)) انتہا نہیں۔",
    "4. که د c دواړو خواوو په (a,c) او (c,b) کې د f′ نښه یو شان وي، ټکی (c,f(c)) انتها نه ده."
  ],
  "In light of first-derivative test, the function f(x) = x³ − 3x² − 9x + 1 (Example 25) has critical values −1 and 3. It is increasing for x < −1 and x > 3, and decreasing for −1 < x < 3. The test gives relative maximum 6 at x = −1 and relative minimum −26 at x = 3.": [
    "پہلے مشتق کے امتحان کے مطابق f(x) = x³ − 3x² − 9x + 1 (مثال 25) کی بحرانی قیمتیں −1 اور 3 ہیں۔ یہ x < −1 اور x > 3 پر بڑھتا اور −1 < x < 3 پر گھٹتا ہے۔ امتحان سے x = −1 پر نسبتی زیادہ سے زیادہ قیمت 6 اور x = 3 پر نسبتی کم سے کم قیمت −26 ملتی ہے۔",
    "د لومړي مشتق د ازموینې له مخې د f(x) = x³ − 3x² − 9x + 1 (بېلګه 25) بحراني ارزښتونه −1 او 3 دي. تابع د x < −1 او x > 3 لپاره زیاتېږي او په −1 < x < 3 کې کمېږي. ازموینه په x = −1 کې نسبي اعظم 6 او په x = 3 کې نسبي اصغر −26 ورکوي."
  ],
  "Examine f(x) = 2x³ + 3x² − 12x − 5 for relative extrema using first-derivative test.": [
    "پہلے مشتق کے امتحان سے f(x) = 2x³ + 3x² − 12x − 5 کی نسبتی انتہائیں جانچیں۔",
    "د لومړي مشتق په ازموینه د f(x) = 2x³ + 3x² − 12x − 5 نسبي انتهاوې وڅېړئ."
  ],
  "The first derivative is:": [
    "پہلا مشتق یہ ہے:",
    "لومړی مشتق دا دی:"
  ],
  "Set f′(x) = 0 for critical values:": [
    "بحرانی قیمتوں کے لیے f′(x) = 0 رکھیں:",
    "د بحراني ارزښتونو لپاره f′(x) = 0 کېږدئ:"
  ],
  "To test −2,1, use test values −3,0,2. Other choices are possible, but select numbers that make computations easy. This is shown in Figure 4.9.": [
    "−2,1 کو جانچنے کے لیے آزمائشی قیمتیں −3,0,2 استعمال کریں۔ دوسری قیمتیں بھی ممکن ہیں، مگر ایسے اعداد لیں جن سے حساب آسان ہو۔ یہ شکل 4.9 میں دکھایا گیا ہے۔",
    "د −2,1 د ازموینې لپاره −3,0,2 آزمېښتي ارزښتونه وکاروئ. نور انتخابونه هم شته، خو هغه عددونه غوره کړئ چې محاسبه اسانه کړي. دا په شکل 4.9 کې ښودل شوي دي."
  ],
  "Test values −3 and 0 for x = −2:": [
    "x = −2 کے لیے آزمائشی قیمتیں −3 اور 0 لیں:",
    "د x = −2 لپاره آزمېښتي ارزښتونه −3 او 0 واخلئ:"
  ],
  "The proof continues on page 124.": [
    "ثبوت صفحہ 124 پر جاری ہے۔",
    "ثبوت په 124 پاڼه کې دوام لري."
  ],
  "The derivative is positive to the left of −2 and negative to the right. Thus x = −2 leads a relative maximum point:": [
    "مشتق −2 کے بائیں مثبت اور دائیں منفی ہے۔ لہٰذا x = −2 نسبتی زیادہ سے زیادہ نقطہ دیتا ہے:",
    "مشتق د −2 چپ لوري ته مثبت او ښي لوري ته منفي دی. نو x = −2 نسبي اعظم ټکی ورکوي:"
  ],
  "Test values 0 and 2 for x = 1:": [
    "x = 1 کے لیے آزمائشی قیمتیں 0 اور 2 لیں:",
    "د x = 1 لپاره آزمېښتي ارزښتونه 0 او 2 واخلئ:"
  ],
  "The derivative is negative to the left of 1 and positive to the right. Thus x = 1 leads a relative minimum point:": [
    "مشتق 1 کے بائیں منفی اور دائیں مثبت ہے۔ لہٰذا x = 1 نسبتی کم سے کم نقطہ دیتا ہے:",
    "مشتق د 1 چپ لوري ته منفي او ښي لوري ته مثبت دی. نو x = 1 نسبي اصغر ټکی ورکوي:"
  ],
  "The arrow pattern suggests relative maximum (−2,15) and relative minimum (1,−12).": [
    "تیروں کا نمونہ نسبتی زیادہ سے زیادہ (−2,15) اور نسبتی کم سے کم (1,−12) ظاہر کرتا ہے۔",
    "د غشو بڼه نسبي اعظم (−2,15) او نسبي اصغر (1,−12) ښيي."
  ],
  "The Second-Derivative Rule": [
    "دوسرے مشتق کا قاعدہ",
    "د دویم مشتق قاعده"
  ],
  "It is often possible to classify a critical point P(c,f(c)) by examining the sign of f″(c). Specifically, if f′(c) = 0 and f″(c) > 0, there is a horizontal tangent at P and f(x) is concave up nearby: its graph is cupped upward from the horizontal tangent, and we expect a relative minimum (Figure 4.11). Similarly, f′(c) = 0 and f″(c) < 0 give a relative maximum, with the graph cupped downward (Figure 4.12).": [
    "اکثر f″(c) کی علامت جانچ کر بحرانی نقطے P(c,f(c)) کی درجہ بندی ممکن ہوتی ہے۔ بالخصوص اگر f′(c) = 0 اور f″(c) > 0 ہوں تو P پر افقی مماس ہوتا ہے اور f(x) آس پاس اوپر کو مقعر ہوتا ہے: اس کا گراف افقی مماس سے اوپر کو پیالہ نما ہوتا ہے، اس لیے نسبتی کم سے کم متوقع ہے (شکل 4.11)۔ اسی طرح f′(c) = 0 اور f″(c) < 0 سے نسبتی زیادہ سے زیادہ ملتا ہے اور گراف نیچے کو مقعر ہوتا ہے (شکل 4.12)۔",
    "ډېری وخت د f″(c) د نښې په کتلو د بحراني ټکي P(c,f(c)) طبقه بندي کېدای شي. په ځانګړي ډول، که f′(c) = 0 او f″(c) > 0 وي، په P کې افقي مماس وي او f(x) شاوخوا پورته مقعره وي: ګراف یې له افقي مماس څخه پورته د کاسې په څېر وي، نو نسبي اصغر تمه کېږي (شکل 4.11). همداسې، f′(c) = 0 او f″(c) < 0 نسبي اعظم ورکوي او ګراف ښکته مقعر وي (شکل 4.12)."
  ],
  "In other words: the point P(c,f(c)) is a relative maximum if the slope f′(c) of the tangent line, from left to right along the curve through P, decreases from positive to zero to negative, and f″(c) is negative. The point is a relative minimum if the slope increases from negative to zero to positive, and f″(c) is positive. These observations lead to the second-derivative test.": [
    "دوسرے لفظوں میں نقطہ P(c,f(c)) نسبتی زیادہ سے زیادہ ہے اگر P سے گزرتے ہوئے منحنی پر بائیں سے دائیں مماس کی ڈھلوان f′(c)، مثبت سے صفر اور پھر منفی ہو جائے اور f″(c) منفی ہو۔ اگر ڈھلوان منفی سے صفر اور پھر مثبت ہو اور f″(c) مثبت ہو تو نقطہ نسبتی کم سے کم ہے۔ یہ مشاہدات دوسرے مشتق کے امتحان کی بنیاد ہیں۔",
    "په نورو ټکو، P(c,f(c)) نسبي اعظم ټکی دی که د P له لارې پر منحني له چپ څخه ښي لوري ته د مماس میلان f′(c) له مثبت څخه صفر او بیا منفي ته راکم شي او f″(c) منفي وي. که میلان له منفي څخه صفر او بیا مثبت ته زیات شي او f″(c) مثبت وي، ټکی نسبي اصغر دی. دا کتنې د دویم مشتق ازموینې ته لاره برابروي."
  ],
  "Remember — The Second Derivative Rule for Relative Extrema": [
    "یاد رکھیں — نسبتی انتہاؤں کے لیے دوسرے مشتق کا قاعدہ",
    "په یاد ولرئ — د نسبي انتهاوو لپاره د دویم مشتق قاعده"
  ],
  "Let f(x) be a function such that f′(c) = 0 and the second derivative exists on an open interval (a,b) containing c. 1. If f″(c) > 0, there is a relative minimum at x = c, and f(x) is concave up nearby. 2. If f″(c) < 0, there is a relative maximum at x = c, and f(x) is concave down nearby. 3. If f″(c) = 0, the second-derivative test fails and gives no information.": [
    "فرض کریں f(x) ایسا تفاعل ہے جس کے لیے f′(c) = 0 ہو اور c کو شامل کرنے والے کھلے وقفے (a,b) میں دوسرا مشتق موجود ہو۔ 1. اگر f″(c) > 0 ہو تو x = c پر نسبتی کم سے کم ہے اور f(x) آس پاس اوپر کو مقعر ہے۔ 2. اگر f″(c) < 0 ہو تو x = c پر نسبتی زیادہ سے زیادہ ہے اور f(x) آس پاس نیچے کو مقعر ہے۔ 3. اگر f″(c) = 0 ہو تو دوسرے مشتق کا امتحان ناکام ہے اور کوئی معلومات نہیں دیتا۔",
    "فرض کړئ f(x) داسې تابع ده چې f′(c) = 0 وي او په خلاص واټن (a,b) کې چې c رانغاړي دویم مشتق موجود وي. 1. که f″(c) > 0 وي، په x = c کې نسبي اصغر وي او f(x) شاوخوا پورته مقعره وي. 2. که f″(c) < 0 وي، په x = c کې نسبي اعظم وي او f(x) شاوخوا ښکته مقعره وي. 3. که f″(c) = 0 وي، د دویم مشتق ازموینه ناکامه ده او معلومات نه ورکوي."
  ],
  "The source Example 27 line f(1) abbreviates powers because 1² = 1³ = 1; its value −12 is correct. If f″(c) = 0, an extremum may or may not occur; use a sign test or another justified method.": [
    "ماخذ کی مثال 27 میں f(1) والی سطر قوتیں مختصر کرتی ہے کیونکہ 1² = 1³ = 1 ہے؛ قیمت −12 درست ہے۔ اگر f″(c) = 0 ہو تو انتہا ہو بھی سکتی ہے اور نہیں بھی؛ علامت کا امتحان یا کوئی دوسرا ثابت شدہ طریقہ استعمال کریں۔",
    "د سرچینې په بېلګه 27 کې د f(1) کرښه توانونه لنډوي، ځکه 1² = 1³ = 1 دي؛ ارزښت −12 سم دی. که f″(c) = 0 وي، انتها کېدای شي وي یا نه وي؛ د نښې ازموینه یا بله موجه طریقه وکاروئ."
  ],
  "Use the second-derivative test to determine whether each critical value of f(x) = 3x⁵ − 5x³ + 2 corresponds to a relative maximum, relative minimum, or neither.": [
    "دوسرے مشتق کے امتحان سے معلوم کریں کہ f(x) = 3x⁵ − 5x³ + 2 کی ہر بحرانی قیمت نسبتی زیادہ سے زیادہ، نسبتی کم سے کم یا ان میں سے کسی کے مطابق نہیں ہے۔",
    "د دویم مشتق په ازموینه معلومه کړئ چې د f(x) = 3x⁵ − 5x³ + 2 هر بحراني ارزښت له نسبي اعظم، نسبي اصغر یا له دواړو څخه له هېڅ یوه سره سمون لري."
  ],
  "The first and second derivatives are:": [
    "پہلے اور دوسرے مشتقات یہ ہیں:",
    "لومړی او دویم مشتقونه دا دي:"
  ],
  "Set f′(x) = 0 to obtain critical values 0,1,−1.": [
    "بحرانی قیمتیں 0,1,−1 حاصل کرنے کے لیے f′(x) = 0 رکھیں۔",
    "د بحراني ارزښتونو 0,1,−1 د ترلاسه کولو لپاره f′(x) = 0 کېږدئ."
  ],
  "The critical value 0 declares the failure of second derivative test.": [
    "بحرانی قیمت 0 پر دوسرے مشتق کا امتحان ناکام ہوتا ہے۔",
    "په بحراني ارزښت 0 کې د دویم مشتق ازموینه ناکامه کېږي."
  ],
  "The critical value 1 leads to a relative minimum:": [
    "بحرانی قیمت 1 نسبتی کم سے کم دیتی ہے:",
    "بحراني ارزښت 1 نسبي اصغر ورکوي:"
  ],
  "The critical value −1 gives a relative maximum:": [
    "بحرانی قیمت −1 نسبتی زیادہ سے زیادہ دیتی ہے:",
    "بحراني ارزښت −1 نسبي اعظم ورکوي:"
  ],
  "The second derivative test works only for critical values c that make f′(c) = 0. It does not work when f′(c) does not exist or f″(c) = 0. In both cases use the first derivative test.": [
    "دوسرے مشتق کا امتحان صرف ان بحرانی قیمتوں c کے لیے کام کرتا ہے جن پر f′(c) = 0 ہو۔ جب f′(c) موجود نہ ہو یا f″(c) = 0 ہو تو یہ کام نہیں کرتا۔ دونوں صورتوں میں پہلے مشتق کا امتحان استعمال کریں۔",
    "د دویم مشتق ازموینه یوازې د هغو بحراني ارزښتونو c لپاره کار کوي چې f′(c) = 0 وي. که f′(c) موجود نه وي یا f″(c) = 0 وي، کار نه کوي. په دواړو حالتونو کې د لومړي مشتق ازموینه وکاروئ."
  ],
  "At 0 the source second-derivative test is inconclusive. Here f′ = 15x²(x² − 1) is negative on both sides of 0, so 0 is neither a maximum nor a minimum; it is a stationary inflection point.": [
    "0 پر ماخذ کا دوسرے مشتق کا امتحان غیر فیصلہ کن ہے۔ یہاں f′ = 15x²(x² − 1)، 0 کے دونوں طرف منفی ہے، اس لیے 0 نہ زیادہ سے زیادہ ہے نہ کم سے کم؛ یہ ساکن نقطۂ انعطاف ہے۔",
    "په 0 کې د سرچینې د دویم مشتق ازموینه پرېکنده نه ده. دلته f′ = 15x²(x² − 1) د 0 دواړو خواوو ته منفي دی، نو 0 نه اعظم دی او نه اصغر؛ دا ساکن د انعطاف ټکی دی."
  ],
  "4.4.6 Solve real-life problems related to extreme values": [
    "4.4.6 انتہانی قیمتوں سے متعلق حقیقی زندگی کے مسائل حل کریں",
    "4.4.6 له انتهايي ارزښتونو سره تړلې د حقیقي ژوند مسئلې حل کړئ"
  ],
  "A truck burns fuel at the rate \\(G(x)=\\frac1{200}\\left(\\frac{800+x^2}{x}\\right)\\), x > 0 gallons per mile, when traveling x miles per hour on a straight level road. If fuel costs $2 per gallon, find the speed that will produce the minimum total cost for a 1000 mile trip. Find the maximum total cost.": [
    "سیدھی ہموار سڑک پر x میل فی گھنٹہ کی رفتار سے چلتا ٹرک \\(G(x)=\\frac1{200}\\left(\\frac{800+x^2}{x}\\right)\\)، x > 0 گیلن فی میل کی شرح سے ایندھن خرچ کرتا ہے۔ اگر ایندھن $2 فی گیلن ہو تو 1000 میل کے سفر کی کم سے کم کل لاگت دینے والی رفتار معلوم کریں۔ زیادہ سے زیادہ کل لاگت معلوم کریں۔",
    "پر مستقیم هوار سړک په x میله فی ساعت سرعت روان لارۍ په \\(G(x)=\\frac1{200}\\left(\\frac{800+x^2}{x}\\right)\\)، x > 0 ګیلنه فی میل کچه سون توکي سوځوي. که د سون بیه د هر ګیلن $2 وي، هغه سرعت ومومئ چې د 1000 میله سفر ټول لګښت اصغر کړي. اعظم ټول لګښت ومومئ."
  ],
  "The total trip cost in dollars is gallons per mile times miles times cost per gallon:": [
    "سفر کی کل ڈالر لاگت، گیلن فی میل ضرب میل ضرب فی گیلن قیمت ہے:",
    "د سفر ټول ډالري لګښت ګیلنه فی میل، ضرب میله، ضرب د هر ګیلن بیه ده:"
  ],
  "The independent variable represents speed; only x > 0 makes sense. Thus the domain is (0,∞) with no endpoints to check.": [
    "آزاد متغیر رفتار ظاہر کرتا ہے؛ صرف x > 0 بامعنی ہے۔ اس لیے دائرۂ کار (0,∞) ہے اور جانچنے کے لیے کوئی آخری نقطے نہیں۔",
    "خپلواک متحول سرعت ښيي؛ یوازې x > 0 مانا لري. نو د تعریف ساحه (0,∞) ده او د کتلو لپاره وروستي ټکي نه لري."
  ],
  "Set C′(x) = 0:": [
    "C′(x) = 0 رکھیں:",
    "C′(x) = 0 کېږدئ:"
  ],
  "The only critical number in the domain is x = 28.3. The second derivative there is:": [
    "دائرۂ کار میں واحد بحرانی عدد x = 28.3 ہے۔ وہاں دوسرا مشتق یہ ہے:",
    "د تعریف په ساحه کې یوازینی بحراني عدد x = 28.3 دی. هلته دویم مشتق دا دی:"
  ],
  "The second-derivative test gives a minimum. Its cost is:": [
    "دوسرے مشتق کا امتحان کم سے کم قیمت دیتا ہے۔ اس کی لاگت یہ ہے:",
    "د دویم مشتق ازموینه اصغر ارزښت ورکوي. لګښت یې دا دی:"
  ],
  "The source question’s final sentence asks for a maximum, while its solution computes a minimum. The exact minimizing speed is √800 = 20√2 mph, and minimum cost is 400√2 ≈ $565.6854. There is no finite maximum on x > 0: C(x) = 8000/x + 10x tends to infinity both as x → 0⁺ and x → ∞. The rounded intermediate C″ is about 0.706, so 0.72 is only a rough source approximation.": [
    "ماخذ کے سوال کا آخری جملہ زیادہ سے زیادہ لاگت پوچھتا ہے، جبکہ حل کم سے کم لاگت نکالتا ہے۔ عین کم سے کم دینے والی رفتار √800 = 20√2 میل فی گھنٹہ اور کم سے کم لاگت 400√2 ≈ $565.6854 ہے۔ x > 0 پر کوئی محدود زیادہ سے زیادہ لاگت نہیں: C(x) = 8000/x + 10x، x → 0⁺ اور x → ∞ دونوں پر لامتناہی کی طرف جاتا ہے۔ گول کیا گیا درمیانی C″ تقریباً 0.706 ہے، اس لیے 0.72 ماخذ کا صرف موٹا تخمینہ ہے۔",
    "د سرچینې د پوښتنې وروستۍ جمله اعظم غواړي، خو حل اصغر محاسبه کوي. دقیق اصغر کوونکی سرعت √800 = 20√2 میله فی ساعت او اصغر لګښت 400√2 ≈ $565.6854 دی. په x > 0 کې محدود اعظم نشته: C(x) = 8000/x + 10x هم د x → 0⁺ او هم د x → ∞ پر مهال بې نهایت ته ځي. ګرد شوی منځنی C″ شاوخوا 0.706 دی، نو 0.72 د سرچینې یوازې یو نږدې اټکل دی."
  ],
  "The supporting cable of a pipeline suspension system forms a parabolic arc between the supports, described by y = 0.03125x² − 1.25x. Distances are measured in meters. The origin is at the point where the cable attaches to the left support tower. Where is the low point and how far is it below the attachment point?": [
    "پائپ لائن کے معلق نظام کی سہارا دینے والی تار ستونوں کے درمیان قطعِ مکافی قوس بناتی ہے جس کی مساوات y = 0.03125x² − 1.25x ہے۔ فاصلے میٹر میں ہیں۔ مبدا بائیں ستون پر تار کے جڑنے کا نقطہ ہے۔ سب سے نچلا نقطہ کہاں ہے اور جڑنے کے نقطے سے کتنا نیچے ہے؟",
    "د نل لیکې د ځوړند سیستم ملاتړ کوونکی کېبل د ستنو ترمنځ پارابولي قوس جوړوي چې معادله یې y = 0.03125x² − 1.25x ده. واټنونه په مترو دي. مبدا هغه ټکی دی چې کېبل له چپ ملاتړ برج سره نښلي. تر ټولو ټیټ ټکی چېرته دی او د نښلېدو له ټکي څومره لاندې دی؟"
  ],
  "For the low point, first and second derivatives are:": [
    "سب سے نچلے نقطے کے لیے پہلے اور دوسرے مشتقات یہ ہیں:",
    "د تر ټولو ټیټ ټکي لپاره لومړی او دویم مشتقونه دا دي:"
  ],
  "Set y′ = 0:": [
    "y′ = 0 رکھیں:",
    "y′ = 0 کېږدئ:"
  ],
  "Since y″ is positive everywhere, x = 20 gives the minimum value. The proof continues on page 126.": [
    "چونکہ y″ ہر جگہ مثبت ہے، x = 20 کم سے کم قیمت دیتا ہے۔ ثبوت صفحہ 126 پر جاری ہے۔",
    "ځکه چې y″ هر ځای مثبت دی، x = 20 اصغر ارزښت ورکوي. ثبوت په 126 پاڼه کې دوام لري."
  ],
  "The low point occurs 20.0 m to the right of the left tower. Put x = 20 into the function to obtain its vertical position:": [
    "سب سے نچلا نقطہ بائیں ستون سے 20.0 میٹر دائیں ہے۔ اس کا عمودی مقام معلوم کرنے کے لیے تفاعل میں x = 20 رکھیں:",
    "تر ټولو ټیټ ټکی د چپ برج 20.0 متره ښي لوري ته دی. د هغه د عمودي موقعیت د موندلو لپاره په تابع کې x = 20 کېږدئ:"
  ],
  "Therefore, the low point is 20.0 m to the right of, and 12.5 m below, the point of attachment to the support.": [
    "لہٰذا سب سے نچلا نقطہ سہارا دینے والے ستون سے تار کے جڑنے کے نقطے سے 20.0 میٹر دائیں اور 12.5 میٹر نیچے ہے۔",
    "نو تر ټولو ټیټ ټکی له ملاتړ سره د نښلېدو له ټکي 20.0 متره ښي لوري ته او 12.5 متره لاندې دی."
  ],
  "4.4.7 MAPLE command maximize (minimize) to compute maximum (minimum) value of a function": [
    "4.4.7 تفاعل کی زیادہ سے زیادہ (کم سے کم) قیمت کے لیے MAPLE کمانڈ maximize (minimize)",
    "4.4.7 د تابع د اعظم (اصغر) ارزښت د محاسبې لپاره د MAPLE د maximize (minimize) قومنده"
  ],
  "The procedure to use MAPLE command maximize (minimize) to compute the maximum (minimum) value of a function is illustrated in the following example.": [
    "تفاعل کی زیادہ سے زیادہ (کم سے کم) قیمت کے لیے MAPLE کمانڈ maximize (minimize) استعمال کرنے کا طریقہ درج ذیل مثال میں واضح کیا گیا ہے۔",
    "د تابع د اعظم (اصغر) ارزښت د محاسبې لپاره د MAPLE د maximize (minimize) قومندې د کارولو طریقه په لاندې بېلګه کې ښودل شوې ده."
  ],
  "Use MAPLE commands to compute: (a) f(x) = cosx; (b) f(x) = x⁴ − 2x² + 3 in the interval [−1,2].": [
    "MAPLE کمانڈوں سے حساب کریں: (a) f(x) = cosx؛ (b) وقفے [−1,2] میں f(x) = x⁴ − 2x² + 3۔",
    "د MAPLE قومندې د محاسبې لپاره وکاروئ: (a) f(x) = cosx؛ (b) په [−1,2] واټن کې f(x) = x⁴ − 2x² + 3."
  ],
  "This result is obtained through right click on the last end of the expression by selecting “Optimization < maximize local” on the context menu.": [
    "یہ نتیجہ عبارت کے آخری سرے پر دایاں کلک کر کے سیاقی مینو سے “Optimization < maximize local” منتخب کرنے سے حاصل ہوتا ہے۔",
    "دا پایله د عبارت پر وروستي سر په ښي کلیک کولو او د سیاق له مېنو څخه د “Optimization < maximize local” په ټاکلو ترلاسه کېږي."
  ],
  "The numerical Context Menu values describe a maximum near x = 0 and a minimum near x = π, rather than all cosine extrema. The exact global cosine range is [−1,1]. For the interval polynomial, compare both endpoints and interior critical points: f(−1) = 2,f(0) = 3,f(1) = 2,f(2) = 11. These source outputs are independently verified mathematically, not claimed as executed Maple results.": [
    "سیاقی مینو کی عددی قیمتیں تمام cosine انتہاؤں کے بجائے x = 0 کے قریب زیادہ سے زیادہ اور x = π کے قریب کم سے کم ظاہر کرتی ہیں۔ cosine کی عین عالمی سعت [−1,1] ہے۔ وقفے والی کثیرالحدی کے لیے دونوں آخری اور اندرونی بحرانی نقاط کا موازنہ کریں: f(−1) = 2،f(0) = 3،f(1) = 2،f(2) = 11۔ ماخذ کے ان نتائج کی ریاضیاتی تصدیق الگ سے کی گئی ہے؛ انہیں Maple چلا کر حاصل شدہ نتائج نہیں کہا گیا۔",
    "د سیاق مېنو عددي ارزښتونه د ټولو cosine انتهاوو پر ځای x = 0 ته نږدې اعظم او x = π ته نږدې اصغر ښيي. د cosine دقیق ټولیز د ارزښتونو ساحه [−1,1] ده. د واټن د کثیرالحدۍ لپاره دواړه وروستي او داخلي بحراني ټکي پرتله کړئ: f(−1) = 2،f(0) = 3،f(1) = 2،f(2) = 11. د سرچینې دا پایلې په خپلواکه توګه ریاضيکي تایید شوې دي؛ د اجرا شوو Maple پایلو ادعا نه پرې کېږي."
  ],
  "Example 22": [
    "مثال 22",
    "بېلګه 22"
  ],
  "Example 23": [
    "مثال 23",
    "بېلګه 23"
  ],
  "Example 24": [
    "مثال 24",
    "بېلګه 24"
  ],
  "Example 24 — continued": [
    "مثال 24 — جاری",
    "بېلګه 24 — دوام"
  ],
  "Example 25": [
    "مثال 25",
    "بېلګه 25"
  ],
  "Example 26": [
    "مثال 26",
    "بېلګه 26"
  ],
  "Example 27": [
    "مثال 27",
    "بېلګه 27"
  ],
  "Example 27 — continued": [
    "مثال 27 — جاری",
    "بېلګه 27 — دوام"
  ],
  "Example 28": [
    "مثال 28",
    "بېلګه 28"
  ],
  "Example 29": [
    "مثال 29",
    "بېلګه 29"
  ],
  "Example 30": [
    "مثال 30",
    "بېلګه 30"
  ],
  "Example 30 — continued": [
    "مثال 30 — جاری",
    "بېلګه 30 — دوام"
  ],
  "Example 31": [
    "مثال 31",
    "بېلګه 31"
  ],
  "Figure 4.3": [
    "شکل 4.3",
    "شکل 4.3"
  ],
  "Figure 4.4": [
    "شکل 4.4",
    "شکل 4.4"
  ],
  "Figure 4.5": [
    "شکل 4.5",
    "شکل 4.5"
  ],
  "Figure 4.6": [
    "شکل 4.6",
    "شکل 4.6"
  ],
  "Figure 4.7": [
    "شکل 4.7",
    "شکل 4.7"
  ],
  "Figure 4.8": [
    "شکل 4.8",
    "شکل 4.8"
  ],
  "Figure 4.9": [
    "شکل 4.9",
    "شکل 4.9"
  ],
  "Figure 4.10": [
    "شکل 4.10",
    "شکل 4.10"
  ],
  "Figure 4.13": [
    "شکل 4.13",
    "شکل 4.13"
  ],
  "Figures 4.11 and 4.12": [
    "شکلیں 4.11 اور 4.12",
    "شکلونه 4.11 او 4.12"
  ]
};
  const completedSectionIds=["sec-4-1", "sec-4-2", "sec-4-3", "sec-4-4"];
  const unit=MATH_12_DATA.find(ch=>Number(ch.number)===4);
  const report={scope:'Reviewed Unit 4 source-section text, captions, list items and prose table cells.',completedSectionIds,nextSection:null,sections:[],newPassageEntries:0};
  for(const [en,pair] of Object.entries(authored)){
    if(!Object.prototype.hasOwnProperty.call(MATH12_SENTENCE_TRANSLATIONS,en)){
      MATH12_SENTENCE_TRANSLATIONS[en]=[{en,ur:pair[0],ps:pair[1],...(pair[0]===en&&pair[1]===en?{mathematicalNotation:true}:{})}];
      report.newPassageEntries++;
    }
  }
  const complete=rows=>Array.isArray(rows)&&rows.length&&rows.every(row=>row.en&&row.ur&&row.ps);
  for(const section of unit?.sections||[]){
    if(!completedSectionIds.includes(section.id))continue;
    const result={id:section.id,fields:0,translatedFields:0,sentenceRows:0,missing:[]};
    function attach(original,object,key){
      if(!original)return;
      result.fields++;
      if(!object[key]?.length&&MATH12_SENTENCE_TRANSLATIONS[original])object[key]=MATH12_SENTENCE_TRANSLATIONS[original];
      if(complete(object[key])){result.translatedFields++;result.sentenceRows+=object[key].length;}
      else result.missing.push(original);
    }
    for(const block of section.sourceBlocks||[]){
      if(['heading','paragraph','clarification'].includes(block.type))attach(block.text,block,'sentenceTranslations');
      if(block.caption)attach(block.caption,block,'captionSentenceTranslations');
      if(block.alt)attach(block.alt,block,'altSentenceTranslations');
      if(block.type==='list'){
        if(!Array.isArray(block.itemSentenceTranslations))block.itemSentenceTranslations=[];
        (block.items||[]).forEach((item,index)=>{if(typeof item==='string')attach(item,block.itemSentenceTranslations,index);});
      }
      if(Array.isArray(block.headers)){
        if(!Array.isArray(block.headerSentenceTranslations))block.headerSentenceTranslations=[];
        block.headers.forEach((item,index)=>{if(typeof item==='string'&&/[A-Za-z]{2,}/.test(item.replace(/\\\([\s\S]*?\\\)/g,'')))attach(item,block.headerSentenceTranslations,index);});
      }
      if(Array.isArray(block.rows)){
        if(!Array.isArray(block.cellSentenceTranslations))block.cellSentenceTranslations=[];
        block.rows.forEach((row,rowIndex)=>{
          if(!Array.isArray(row))return;
          row.forEach((item,index)=>{
            if(typeof item!=='string'||!/[A-Za-z]{2,}/.test(item.replace(/\\\([\s\S]*?\\\)/g,'')))return;
            if(!Array.isArray(block.cellSentenceTranslations[rowIndex]))block.cellSentenceTranslations[rowIndex]=[];
            attach(item,block.cellSentenceTranslations[rowIndex],index);
          });
        });
      }
    }
    report.sections.push(result);
  }
  globalThis.MATH12_UNIT4_TRANSLATION_REPORT=report;
})();
