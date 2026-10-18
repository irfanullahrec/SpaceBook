/*
 * Mathematical companion to recovered KPTBB XII printed pages 142–157.
 * Formula/problem facts are checked against the recovered scan; explanatory
 * prose and worked solutions are newly written. This is not a transcription.
 * The supplied textbook and all existing source-page text remain unchanged.
 */
(function () {
  if (typeof MATH_12_DATA === 'undefined') return;
  const unit = MATH_12_DATA.find(ch => Number(ch.number) === 6);
  if (!unit || unit.recoveredPageCompanion?.version === 1) return;
  const file = 'docs/source-verification/class-12/sources/math12-unit6-recovered.pdf';
  const origin = 'SpaceBook recovered-page companion; mathematical facts checked, explanatory prose newly authored';
  const reference = page => ({page, file, pdfPage: page - 140, verification: 'Recovered scan visually inspected; companion is not verbatim textbook prose'});
  const heading = (page, text) => ({type:'heading',text,sourcePage:page,contentOrigin:origin});
  const formula = (page, text) => ({type:'command',prompt:false,result:'\\('+text+'\\)',sourcePage:page,contentOrigin:origin});
  const paragraph = (page,en,ur,ps) => ({type:'paragraph',text:en,sourcePage:page,contentOrigin:origin,sentenceTranslations:[{en,ur,ps}]});
  const clarification = (page,text) => ({type:'clarification',text,sourcePage:page,contentOrigin:origin});
  const table = (page,caption,headers,rows) => ({type:'dataTable',caption,headers,rows,sourcePage:page,contentOrigin:origin});
  const wrap = value => '\\('+value+'\\)';
  const section = id => unit.sections.find(item => item.id === id);
  const old = ['sec-6-1','sec-6-2','sec-6-3'].map(id => {
    const item=section(id);
    return {id,sourceBlocks:item.sourceBlocks,sourceReferences:item.sourceReferences,sourceStatus:item.sourceStatus};
  });
  unit.recoveredPageCompanion = {
    version:1, file, printedPages:Array.from({length:16},(_,i)=>142+i),
    sourceSha256:'3902216d33af5c57043c76be2f929435d77c9df8181aa2f5476da8aa6682e119',
    originalGap:unit.sourceGap, originalSections:JSON.parse(JSON.stringify(old)),
    proseOrigin:'Newly authored explanations, not verbatim recovered textbook text.',
    visualSourceInspection:'All printed pages 142–157 and adjacent 158 inspected.',
    translations:'Authored explanatory paragraphs include Urdu and Pashto. Formula tables, worked steps, source-error notes and challenge solutions still require a separate complete translation review.',
    completeTextbookTranscription:false
  };
  unit.sourceGap = null;

  const introductory = [
    heading(142,'Recovered-page companion — Integration'),
    paragraph(142,
      'These notes cover the mathematical content of the recovered opening pages. The formulas, example data and page references were checked against the matching textbook scan; the explanations below are newly written.',
      'یہ نوٹس کتاب کے بازیافت شدہ ابتدائی صفحات کے ریاضیاتی مواد پر مبنی ہیں۔ فارمولوں، مثالوں کے اعداد و معلومات اور صفحہ نمبروں کو اسی نصابی کتاب کے اسکین سے ملایا گیا ہے؛ ذیل کی تشریحات نئے الفاظ میں لکھی گئی ہیں۔',
      'دا یادښتونه د بېرته موندل شوو لومړیو پاڼو ریاضيکي مطالب رانغاړي. فورمولونه، د بېلګو معلومات او د پاڼو شمېرې د همدې درسي کتاب له سکن سره کتل شوي دي؛ لاندې تشریح په نوو ټکو لیکل شوې ده.'),
    table(142,'Unit 6 learning map',['Section','Mathematical aim'],[
      ['6.1','Recover an accumulated quantity from its rate; identify antiderivatives and the constant C; use the standard integral table.'],
      ['6.2','Apply the constant, linearity, power and logarithmic rules; reverse chain and product differentiation.'],
      ['6.3','Choose a substitution for powers, exponentials, quadratics and square-root expressions.'],
      ['6.4','Use integration by parts, including the three quadratic-radical families.'],
      ['6.5','Decompose rational functions into partial fractions before integration.'],
      ['6.6','Define the definite integral by a limit of sums; apply its properties, the fundamental theorem, area methods and Maple integration.']
    ]),
    formula(142,'\\int [f(x)]^n f^{\\prime}(x)\\,dx,\\quad \\int\\frac{f^{\\prime}(x)}{f(x)}\\,dx,\\quad\\int e^{ax}[af(x)+f^{\\prime}(x)]\\,dx'),
    formula(142,'\\int\\frac{dx}{a^2-x^2},\\ \\int\\sqrt{a^2-x^2}\\,dx,\\ \\int\\frac{dx}{\\sqrt{a^2-x^2}};\\quad\\int\\frac{dx}{a^2+x^2},\\ \\int\\sqrt{a^2+x^2}\\,dx,\\ \\int\\frac{dx}{\\sqrt{a^2+x^2}}'),
    formula(142,'\\int\\frac{dx}{x^2-a^2},\\ \\int\\sqrt{x^2-a^2}\\,dx,\\ \\int\\frac{dx}{\\sqrt{x^2-a^2}};\\quad\\int\\frac{dx}{ax^2+bx+c},\\ \\int\\frac{dx}{\\sqrt{ax^2+bx+c}}'),
    formula(142,'\\int\\frac{px+q}{ax^2+bx+c}\\,dx,\\quad\\int\\frac{px+q}{\\sqrt{ax^2+bx+c}}\\,dx,\\quad\\int\\frac{f(x)}{g(x)}\\,dx\\quad(g(x)\\ne0)'),
    formula(142,'\\int_a^a f(x)\\,dx=0,\\quad\\int_a^b f(x)\\,dx=\\int_a^b f(y)\\,dy,\\quad\\int_a^b f(x)\\,dx=-\\int_b^a f(x)\\,dx'),
    formula(142,'\\int_a^b f(x)\\,dx=\\int_a^c f(x)\\,dx+\\int_c^b f(x)\\,dx\\quad(a<c<b)'),
    formula(142,'\\int_{-a}^a f(x)\\,dx=2\\int_0^a f(x)\\,dx\\ \\text{if }f(-x)=f(x);\\qquad\\int_{-a}^a f(x)\\,dx=0\\ \\text{if }f(-x)=-f(x)'),
    heading(143,'6.1 Introduction: accumulation and antiderivatives'),
    paragraph(143,
      'Differentiation turns an amount into a rate of change. Integration reverses that relationship: a known rate can be accumulated to recover an amount, such as distance, cost, revenue, profit or volume.',
      'تفرقی عمل کسی مقدار سے اس کی تبدیلی کی شرح معلوم کرتا ہے۔ تکمل اس تعلق کو الٹتا ہے: معلوم شرح کو جمع کر کے فاصلہ، لاگت، آمدنی، منافع یا حجم جیسی مقدار حاصل کی جا سکتی ہے۔',
      'تفریق له یوې اندازې څخه د بدلون کچه راوباسي. تکامل دا اړیکه معکوسوي: معلومه کچه راټولولای شو څو واټن، لګښت، عاید، ګټه یا حجم ترلاسه کړو.'),
    paragraph(143,
      'A function F is an antiderivative of f on an interval when F′(x)=f(x) throughout that interval. A definite integral also describes signed area; an indefinite integral gives a family of antiderivatives.',
      'اگر کسی وقفے کے ہر نقطے پر F′(x)=f(x) ہو تو F کو f کا ضد مشتق کہتے ہیں۔ معین تکمل علامت کے ساتھ رقبہ بھی ظاہر کرتا ہے، جبکہ غیر معین تکمل ضد مشتقات کا ایک خاندان دیتا ہے۔',
      'که په یوه واټن کې په هر ځای F′(x)=f(x) وي، نو F د f ضد مشتق دی. ټاکلی تکامل نښه لرونکی مساحت هم ښيي؛ ناتاکلی تکامل د ضد مشتقونو یوه کورنۍ ورکوي.'),
    formula(143,'F^{\\prime}(x)=f(x),\\qquad f(x)=x^2\\Longrightarrow F(x)=\\frac{x^3}{3}'),
    heading(143,'Constant of integration'),
    formula(143,'\\frac{d}{dx}\\left(\\frac{x^3}{3}+1\\right)=\\frac{d}{dx}\\left(\\frac{x^3}{3}-7\\right)=\\frac{d}{dx}\\left(\\frac{x^3}{3}+C\\right)=x^2'),
    paragraph(143,
      'Adding a constant does not change a derivative. On a connected interval, any two antiderivatives of the same function differ by a constant.',
      'مستقل عدد جمع کرنے سے مشتق تبدیل نہیں ہوتا۔ ایک متصل وقفے پر ایک ہی تفاعل کے کسی بھی دو ضد مشتقات کا فرق ایک مستقل عدد ہوتا ہے۔',
      'د ثابت عدد په زیاتولو مشتق نه بدلېږي. په یوه نښتي واټن کې د یوه تابع د هر دوو ضد مشتقونو توپیر ثابت عدد وي.'),
    formula(144,'F_1^{\\prime}=f=F_2^{\\prime}\\Longrightarrow\\frac{d}{dx}(F_1-F_2)=0\\Longrightarrow F_1-F_2=C'),
    paragraph(144,
      'The mean value theorem makes the last step precise: a differentiable function whose derivative vanishes everywhere on an interval is constant there.',
      'اوسط قدر کا قضیہ آخری قدم کی وضاحت کرتا ہے: اگر کسی وقفے پر قابلِ تفرق تفاعل کا مشتق ہر جگہ صفر ہو تو وہ تفاعل اس وقفے پر مستقل ہوتا ہے۔',
      'د منځني ارزښت قضیه وروستی ګام روښانوي: که د یوه تفریق کېدونکي تابع مشتق په یوه واټن کې هر ځای صفر وي، تابع په هماغه واټن کې ثابت وي.'),
    formula(144,'\\int f(x)\\,dx=F(x)+C\\quad\\text{when }F^{\\prime}(x)=f(x)'),
    paragraph(144,
      'In ∫f(x)dx, the integral sign identifies the operation, f(x) is the integrand, dx identifies the variable and C represents an arbitrary constant. A different variable changes the notation, not the rule.',
      '∫f(x)dx میں تکمل کی علامت عمل کو ظاہر کرتی ہے، f(x) زیرِ تکمل تفاعل ہے، dx متغیر کی نشاندہی کرتا ہے اور C اختیاری مستقل ہے۔ متغیر کا نام بدلنے سے علامتی صورت بدلتی ہے، قاعدہ نہیں۔',
      'په ∫f(x)dx کې د تکامل نښه عمل ښيي، f(x) تر تکامل لاندې تابع ده، dx متغیر ښيي او C اختیاري ثابت دی. د متغیر نوم بدلول نښه بدلوي، خو قاعده نه بدلوي.'),
    formula(144,'\\int2x\\,dx=x^2+C,\\quad\\int2t\\,dt=t^2+C,\\quad\\int2u\\,du=u^2+C'),
    heading(144,'Standard integral table — checked formula pairs'),
    paragraph(144,
      'Differentiate each proposed antiderivative to verify its row. Work on an interval where the expressions are defined; use a>0 for the quadratic-radical formulas, k≠0, m≠0, and a>0 with a≠1 for aˣ.',
      'ہر سطر کی تصدیق کے لیے دیے گئے ضد مشتق کا مشتق لیں۔ ایسے وقفے پر کام کریں جہاں عبارتیں معین ہوں؛ جذر والے دو درجی فارمولوں میں a>0، نیز k≠0، m≠0 اور aˣ کے لیے a>0 اور a≠1 لیں۔',
      'د هر قطار د کتلو لپاره د ورکړل شوي ضد مشتق مشتق واخلئ. په داسې واټن کې کار وکړئ چې عبارتونه تعریف شوي وي؛ د مربع ریښې فورمولونو لپاره a>0، همدارنګه k≠0، m≠0 او د aˣ لپاره a>0 او a≠1 وکاروئ.'),
    table(144,'Standard integrals, printed 144–145',['Integrand','Antiderivative + C','Derivative check'],[
      ['xⁿ (n≠−1)',wrap('\\frac{x^{n+1}}{n+1}+C'),'xⁿ'],
      ['1/x',wrap('\\ln|x|+C'),'1/x'],
      ['cos(kx)',wrap('\\frac{\\sin(kx)}k+C'),'cos(kx)'],
      ['sin(kx)',wrap('-\\frac{\\cos(kx)}k+C'),'sin(kx)'],
      ['1/cos²x',wrap('\\tan x+C'),'sec²x'],
      ['1/sin²x',wrap('-\\cot x+C'),'cosec²x'],
      ['tan x',wrap('-\\ln|\\cos x|+C'),'tan x'],
      ['cot x',wrap('\\ln|\\sin x|+C'),'cot x'],
      ['eᵐˣ',wrap('\\frac{e^{mx}}m+C'),'eᵐˣ'],
      ['aˣ',wrap('\\frac{a^x}{\\ln a}+C'),'aˣ'],
      ['1/(1+x²)',wrap('\\tan^{-1}x+C'),'1/(1+x²)'],
      ['1/(a²+x²)',wrap('\\frac1a\\tan^{-1}\\frac xa+C'),'1/(a²+x²)'],
      ['1/(a²−x²)',wrap('\\frac1{2a}\\ln\\left|\\frac{a+x}{a-x}\\right|+C'),'1/(a²−x²)'],
      ['1/(x²−a²)',wrap('\\frac1{2a}\\ln\\left|\\frac{x-a}{x+a}\\right|+C'),'1/(x²−a²)'],
      ['1/√(1−x²)',wrap('\\sin^{-1}x+C'),'1/√(1−x²)'],
      ['1/√(a²−x²)',wrap('\\sin^{-1}\\frac xa+C'),'1/√(a²−x²)'],
      ['1/√(x²±a²)',wrap('\\ln\\left|x+\\sqrt{x^2\\pm a^2}\\right|+C'),'1/√(x²±a²)']
    ]),
    heading(145,'Example 2: fractional and negative powers'),
    formula(145,'\\int x^{1/3}\\,dx=\\frac{x^{4/3}}{4/3}+C=\\frac34x^{4/3}+C,\\qquad\\int\\frac{dx}{x^3}=\\frac{x^{-2}}{-2}+C=-\\frac1{2x^2}+C'),
    clarification(145,'The printed cotangent row omits x inside its sine expression. The companion writes ln|sin x|. Conditions on constants and intervals are stated explicitly here.')
  ];
  const rules = [
    heading(145,'6.2 Rules of Integration — recovered-page companion'),
    paragraph(145,
      'Differentiating an antiderivative returns the integrand. Integrating a derivative returns the original function plus an arbitrary constant.',
      'ضد مشتق کا مشتق لینے سے زیرِ تکمل تفاعل واپس ملتا ہے۔ کسی مشتق کا تکمل لینے سے اصل تفاعل کے ساتھ ایک اختیاری مستقل حاصل ہوتا ہے۔',
      'د ضد مشتق مشتق اخیستل اصلي تر تکامل لاندې تابع بېرته راکوي. د مشتق تکامل اصلي تابع له یوه اختیاري ثابت سره راکوي.'),
    formula(145,'\\frac{d}{dx}\\left[\\int f(x)\\,dx\\right]=f(x),\\qquad\\int f^{\\prime}(x)\\,dx=f(x)+C'),
    clarification(145,'Printed page 145 adds +C after differentiating an indefinite integral. That +C disappears on differentiation; the summary box on printed page 146 gives the correct identity. Both locations have been compared.'),
    formula(146,'\\int x^3\\,dx=\\frac{x^4}{4}+C,\\quad\\frac{d}{dx}\\left(\\frac{x^4}{4}+C\\right)=x^3,\\quad\\int3x^2\\,dx=x^3+C'),
    paragraph(146,
      'Integration is linear. A constant multiplier can be moved outside the integral, and a finite sum can be integrated term by term. Differentiating either side verifies these rules.',
      'تکمل خطی عمل ہے۔ مستقل ضربی عدد کو تکمل کے باہر لایا جا سکتا ہے اور محدود مجموعے کی ہر حد کا الگ تکمل لیا جا سکتا ہے۔ دونوں طرف مشتق لینے سے ان قواعد کی تصدیق ہوتی ہے۔',
      'تکامل خطي عمل دی. ثابت ضریب د تکامل له نښې بهر ایستلای شو، او د محدود مجموعې هر حد جلا تکامل کولای شو. د دواړو خواوو مشتق اخیستل دا قواعد تاییدوي.'),
    table(146,'Basic rules',['Rule','Formula'],[
      ['Constant',wrap('\\int k\\,dx=kx+C')],
      ['Constant multiple',wrap('\\int kf(x)\\,dx=k\\int f(x)\\,dx')],
      ['Sum',wrap('\\int[f(x)+g(x)]\\,dx=\\int f(x)\\,dx+\\int g(x)\\,dx')],
      ['Power',wrap('\\int x^n\\,dx=\\frac{x^{n+1}}{n+1}+C\\quad(n\\ne-1)')],
      ['Logarithmic',wrap('\\int\\frac{dx}x=\\ln|x|+C\\quad(x\\ne0)')]
    ]),
    formula(146,'\\frac{d}{dx}\\left[k\\int f(x)\\,dx\\right]=kf(x),\\qquad\\frac{d}{dx}\\left[\\int f(x)\\,dx+\\int g(x)\\,dx\\right]=f(x)+g(x)'),
    heading(147,'Example 3: constants and sums'),
    formula(147,'\\int(10+a)\\,dx=(10+a)x+C,\\qquad\\int(10+a)x^2\\,dx=\\frac{(10+a)x^3}{3}+C'),
    formula(147,'\\int(5x^2+4x+2)\\,dx=5\\int x^2\\,dx+4\\int x\\,dx+2\\int dx=\\frac{5x^3}{3}+2x^2+2x+C'),
    heading(147,'Reverse chain rule'),
    formula(147,'\\int[f(x)]^n f^{\\prime}(x)\\,dx=\\frac{[f(x)]^{n+1}}{n+1}+C\\quad(n\\ne-1)'),
    paragraph(147,
      'Let u=f(x), so du=f′(x)dx. The integral becomes ∫uⁿdu, giving the displayed power formula. Differentiation verifies the result by the chain rule.',
      'u=f(x) رکھیں، اس لیے du=f′(x)dx ہوگا۔ تکمل ∫uⁿdu بن جاتا ہے، جس سے دکھایا گیا قوت کا فارمولا ملتا ہے۔ زنجیری قاعدے سے مشتق لے کر جواب کی تصدیق ہوتی ہے۔',
      'u=f(x) کېږدئ، نو du=f′(x)dx کېږي. تکامل په ∫uⁿdu بدلېږي او د توان ښودل شوی فورمول ورکوي. د ځنځیري قاعدې له مخې مشتق د پایلې تایید کوي.'),
    formula(147,'\\int\\frac{f^{\\prime}(x)}{f(x)}\\,dx=\\int\\frac{du}u=\\ln|u|+C=\\ln|f(x)|+C\\quad(f(x)\\ne0)'),
    heading(148,'Reverse product rule'),
    formula(148,'\\frac{d}{dx}\\big(e^{ax}f(x)\\big)=e^{ax}[af(x)+f^{\\prime}(x)]\\Longrightarrow\\int e^{ax}[af(x)+f^{\\prime}(x)]\\,dx=e^{ax}f(x)+C'),
    clarification(148,'The printed right-hand side of formula C reads a·eˣf(x)+C. Product differentiation instead gives eᵃˣf(x)+C; the checked identity above is the companion result.')
  ];
  const substitution = [
    heading(148,'6.3 Integration by Substitution — recovered-page companion'),
    paragraph(148,
      'Substitution reverses the chain rule. Choose a new variable u=f(x), replace f′(x)dx by du, integrate using u, and finally substitute back into x. Check the final answer by differentiation.',
      'متبادل کا طریقہ زنجیری قاعدے کو الٹ کر استعمال کرتا ہے۔ نیا متغیر u=f(x) منتخب کریں، f′(x)dx کی جگہ du لکھیں، u کے لحاظ سے تکمل لیں اور آخر میں x واپس رکھیں۔ آخری جواب کا مشتق لے کر جانچ کریں۔',
      'د بدلولو طریقه ځنځیري قاعده په معکوس ډول کاروي. نوی متغیر u=f(x) وټاکئ، د f′(x)dx پر ځای du ولیکئ، د u له مخې تکامل واخلئ، بیا x بېرته کېږدئ. وروستۍ پایله په مشتق وازمویئ.'),
    formula(148,'\\int x^2\\sqrt{x^3+1}\\,dx;\\quad u=x^3+1,\\ du=3x^2dx\\Longrightarrow\\frac13\\int u^{1/2}\\,du=\\frac29(x^3+1)^{3/2}+C'),
    table(148,'Substitution patterns',['Pattern','Result'],[
      [wrap('\\int[f(x)]^n f^{\\prime}(x)\\,dx'),wrap('\\frac{[f(x)]^{n+1}}{n+1}+C\\quad(n\\ne-1)')],
      [wrap('\\int\\frac{f^{\\prime}(x)}{f(x)}\\,dx'),wrap('\\ln|f(x)|+C')],
      [wrap('\\int e^{f(x)}f^{\\prime}(x)\\,dx'),wrap('e^{f(x)}+C')],
      [wrap('\\int e^x\\,dx'),wrap('e^x+C')],
      [wrap('\\int e^{kx}\\,dx'),wrap('\\frac{e^{kx}}k+C\\quad(k\\ne0)')],
      [wrap('\\int a^x\\,dx'),wrap('\\frac{a^x}{\\ln a}+C\\quad(a>0,\\ a\\ne1)')]
    ]),
    heading(148,'Example 4: three substitutions'),
    formula(149,'u=x^3-5x+7,\\quad du=(3x^2-5)dx\\Longrightarrow\\int(x^3-5x+7)^4(3x^2-5)\\,dx=\\frac{(x^3-5x+7)^5}{5}+C'),
    formula(149,'u=9x+7,\\quad dx=\\frac{du}{9}\\Longrightarrow\\int\\frac{dx}{9x+7}=\\frac19\\ln|9x+7|+C'),
    formula(149,'u=3x+2,\\quad dx=\\frac{du}{3}\\Longrightarrow\\int e^{3x+2}\\,dx=\\frac13e^{3x+2}+C'),
    clarification(149,'The printed logarithmic answer omits absolute-value bars. The companion includes them so the answer applies on either real interval where 9x+7 is nonzero.'),
    heading(149,'Example 5: a shrinking wound'),
    paragraph(149,
      'A wound has area A=2 cm² at t=1 day and changes at dA/dt=−4t⁻³ for 1≤t≤10. Integrate the rate and use the initial area to determine the constant.',
      'ایک زخم کا رقبہ t=1 دن پر A=2 مربع سینٹی میٹر ہے اور 1≤t≤10 کے لیے اس کی تبدیلی کی شرح dA/dt=−4t⁻³ ہے۔ شرح کا تکمل لے کر ابتدائی رقبے سے مستقل معلوم کریں۔',
      'د یوه ټپ مساحت په t=1 ورځ کې A=2 مربع سانتي متره دی، او د 1≤t≤10 لپاره د بدلون کچه یې dA/dt=−4t⁻³ ده. کچه تکامل کړئ او له لومړني مساحت څخه ثابت پیدا کړئ.'),
    formula(149,'A(t)=\\int-4t^{-3}\\,dt=2t^{-2}+C,\\quad2=2+C\\Longrightarrow C=0,\\quad A(10)=\\frac2{100}=0.02\\ \\mathrm{cm}^2'),
    heading(150,'Exercise 6.1'),
    paragraph(150,
      'The recovered exercise contains eight numbered groups and twenty-eight answerable parts. Open Exercise 6.1 in the exercise tab for the individual questions and worked answers.',
      'بازیافت شدہ مشق میں آٹھ نمبر وار سوالی گروہ اور اٹھائیس قابلِ جواب حصے ہیں۔ انفرادی سوالات اور حل دیکھنے کے لیے مشقوں کے حصے میں مشق 6.1 کھولیں۔',
      'بېرته موندل شوی تمرین اته شمېرل شوې پوښتنې او اته ویشت ځوابېدونکې برخې لري. د جلا پوښتنو او حلونو لپاره د تمرینونو په برخه کې تمرین 6.1 پرانیزئ.'),
    heading(151,'Quadratic substitutions: a²−x²'),
    paragraph(151,
      'For the following families take a>0 and choose an interval that avoids every zero denominator. Partial fractions give the rational formulas; x=a sin u handles the square root a²−x² on |x|<a.',
      'درج ذیل اقسام کے لیے a>0 لیں اور ایسا وقفہ منتخب کریں جس میں کوئی مخرج صفر نہ ہو۔ ناطق فارمولے جزوی کسور سے ملتے ہیں؛ |x|<a پر x=a sin u رکھنے سے √(a²−x²) آسان ہوتا ہے۔',
      'د لاندې ډولونو لپاره a>0 واخلئ او داسې واټن وټاکئ چې هېڅ مخرج پکې صفر نه وي. ناطق فورمولونه له جزوي کسرونو ترلاسه کېږي؛ د |x|<a لپاره x=a sin u د √(a²−x²) ریښه ساده کوي.'),
    formula(151,'\\frac1{x^2-a^2}=\\frac1{2a}\\left(\\frac1{x-a}-\\frac1{x+a}\\right)'),
    formula(151,'\\int\\frac{dx}{x-a}=\\ln|x-a|+C,\\qquad\\int\\frac{dx}{x+a}=\\ln|x+a|+C'),
    formula(152,'\\int\\frac{dx}{x^2-a^2}=\\frac1{2a}\\ln\\left|\\frac{x-a}{x+a}\\right|+C,\\qquad\\int\\frac{dx}{a^2-x^2}=\\frac1{2a}\\ln\\left|\\frac{a+x}{a-x}\\right|+C'),
    clarification(152,'Printed pages 151–152 change logarithm signs inconsistently and interchange the last two denominators. The checked formulas above have opposite signs, as required by a²−x²=−(x²−a²).'),
    formula(152,'x=a\\sin u,\\quad dx=a\\cos u\\,du,\\quad -\\frac\\pi2<u<\\frac\\pi2'),
    formula(152,'\\int\\sqrt{a^2-x^2}\\,dx=a^2\\int\\cos^2u\\,du=\\frac{a^2}{2}\\int(1+\\cos2u)\\,du=\\frac{a^2u}{2}+\\frac{a^2\\sin2u}{4}+C'),
    formula(152,'\\int\\sqrt{a^2-x^2}\\,dx=\\frac x2\\sqrt{a^2-x^2}+\\frac{a^2}{2}\\sin^{-1}\\frac xa+C'),
    formula(153,'\\int\\frac{dx}{\\sqrt{a^2-x^2}}=\\int\\frac{a\\cos u}{a\\cos u}\\,du=u+C=\\sin^{-1}\\frac xa+C'),
    heading(153,'Quadratic substitutions: a²+x²'),
    formula(153,'u=\\frac xa\\Longrightarrow\\int\\frac{dx}{a^2+x^2}=\\frac1a\\int\\frac{du}{1+u^2}=\\frac1a\\tan^{-1}\\frac xa+C'),
    formula(153,'x=a\\tan u,\\quad dx=a\\sec^2u\\,du,\\quad\\sqrt{a^2+x^2}=a\\sec u\\quad\\left(-\\frac\\pi2<u<\\frac\\pi2\\right)'),
    formula(153,'\\int\\sqrt{a^2+x^2}\\,dx=a^2\\int\\sec^3u\\,du=\\frac{a^2}{2}\\left(\\sec u\\tan u+\\ln|\\sec u+\\tan u|\\right)+C'),
    formula(154,'\\int\\sqrt{a^2+x^2}\\,dx=\\frac x2\\sqrt{a^2+x^2}+\\frac{a^2}{2}\\ln\\left|x+\\sqrt{a^2+x^2}\\right|+C'),
    formula(154,'\\int\\frac{dx}{\\sqrt{a^2+x^2}}=\\int\\sec u\\,du=\\ln|\\sec u+\\tan u|+C=\\ln\\left|\\frac{x+\\sqrt{x^2+a^2}}a\\right|+C'),
    paragraph(154,
      'A constant inside a logarithm can be absorbed into C. For example, ln|(x+√(x²+a²))/a| and ln|x+√(x²+a²)| differ only by the constant −ln a.',
      'لوگارتھم کے اندر موجود مستقل عامل کو C میں شامل کیا جا سکتا ہے۔ مثلاً ln|(x+√(x²+a²))/a| اور ln|x+√(x²+a²)| میں صرف مستقل −ln a کا فرق ہے۔',
      'د لوګاریتم دننه ثابت عامل په C کې جذبېدای شي. د بېلګې په توګه ln|(x+√(x²+a²))/a| او ln|x+√(x²+a²)| یوازې د ثابت −ln a په اندازه توپیر لري.'),
    heading(154,'Quadratic substitutions: x²−a²'),
    paragraph(154,
      'For x>a choose x=a sec u with 0<u<π/2. Then dx=a sec u tan u du and √(x²−a²)=a tan u. The final formulas, with absolute values, are valid separately on both intervals |x|>a.',
      'x>a کے لیے x=a sec u اور 0<u<π/2 لیں۔ تب dx=a sec u tan u du اور √(x²−a²)=a tan u ہوگا۔ مطلق قیمتوں کے ساتھ آخری فارمولے |x|>a کے دونوں الگ وقفوں پر درست ہیں۔',
      'د x>a لپاره x=a sec u او 0<u<π/2 وټاکئ. بیا dx=a sec u tan u du او √(x²−a²)=a tan u کېږي. وروستي فورمولونه له مطلقو ارزښتونو سره د |x|>a پر دواړو جلا واټنونو سم دي.'),
    formula(155,'\\int\\frac{dx}{x^2-a^2}=\\frac1a\\int\\csc u\\,du=-\\frac1a\\ln|\\csc u+\\cot u|+C=\\frac1{2a}\\ln\\left|\\frac{x-a}{x+a}\\right|+C'),
    formula(155,'-\\frac1a\\ln\\left|\\frac{\\sqrt{x^2-a^2}}{x-a}\\right|=\\frac1{2a}\\ln\\left|\\frac{x-a}{x+a}\\right|\\quad(|x|>a)'),
    formula(155,'\\int\\sqrt{x^2-a^2}\\,dx=a^2\\int\\sec u\\tan^2u\\,du=a^2\\int(\\sec^3u-\\sec u)\\,du'),
    formula(156,'\\int\\sqrt{x^2-a^2}\\,dx=\\frac x2\\sqrt{x^2-a^2}-\\frac{a^2}{2}\\ln\\left|x+\\sqrt{x^2-a^2}\\right|+C'),
    formula(156,'\\int\\frac{dx}{\\sqrt{x^2-a^2}}=\\int\\sec u\\,du=\\ln|\\sec u+\\tan u|+C=\\ln\\left|x+\\sqrt{x^2-a^2}\\right|+C'),
    clarification(156,'In part (c), several printed return-substitution lines lose the square-root sign in the denominator. The question, the substitution and the final formula refer to 1/√(x²−a²).'),
    heading(156,'Quadratic denominators: completing the square'),
    paragraph(156,
      'Complete the square before making a substitution. For x²+4x+5=(x+2)²+1, the change u=x+2 reduces each example to a standard quadratic integral.',
      'متبادل رکھنے سے پہلے مکمل مربع بنائیں۔ x²+4x+5=(x+2)²+1 کے لیے u=x+2 رکھنے سے ہر مثال ایک معیاری دو درجی تکمل میں بدل جاتی ہے۔',
      'له بدلولو مخکې مربع بشپړ کړئ. د x²+4x+5=(x+2)²+1 لپاره u=x+2 هره بېلګه په یوه معیاري دو درجې تکامل بدلوي.'),
    heading(156,'Example 6'),
    formula(157,'\\int\\frac{dx}{x^2+4x+5}=\\int\\frac{du}{u^2+1}=\\tan^{-1}u+C=\\tan^{-1}(x+2)+C'),
    heading(157,'Example 7'),
    formula(157,'\\int\\frac{dx}{\\sqrt{x^2+4x+5}}=\\int\\frac{du}{\\sqrt{u^2+1}}=\\ln\\left|u+\\sqrt{u^2+1}\\right|+C=\\ln\\left|x+2+\\sqrt{x^2+4x+5}\\right|+C'),
    clarification(157,'Example 7 has square roots in its question and initial substitution, but later printed lines lose them. The companion consistently integrates 1/√(x²+4x+5).'),
    heading(157,'Example 8 — continued on supplied page 158'),
    formula(157,'\\int\\frac{x+2}{x^2+4x+5}\\,dx=\\int\\frac{u}{u^2+1}\\,du=\\frac12\\ln(u^2+1)+C=\\frac12\\ln(x^2+4x+5)+C'),
    clarification(157,'The original Example 8 on page 157 has numerator x+2. Its continuation on page 158 prints x−2 in several return-substitution lines. Those supplied source lines are preserved below; the checked solution follows the actual question x+2.')
  ];
  section('sec-6-1').sourceBlocks = introductory;
  section('sec-6-1').sourceReferences = [142,143,144,145].map(reference);
  section('sec-6-2').sourceBlocks = rules;
  section('sec-6-2').sourceReferences = [145,146,147,148].map(reference);
  const continued = section('sec-6-3').sourceBlocks.slice();
  if (continued[0]?.type === 'heading' && /missing page 157/.test(continued[0].text)) {
    continued[0] = {...continued[0],text:'Supplied textbook continuation — printed page 158'};
  }
  for(let index=0;index<continued.length;index++){
    if(continued[index].type==='clarification'&&/^The preceding page containing this example/.test(continued[index].text)){
      continued[index]={...continued[index],text:'The supplied files omitted this example’s opening. The matching independent scan has now recovered it on printed page 157, and its companion appears above. The supplied continuation remains intact. Since (x+2)²+1 is positive on ℝ, the absolute value may be removed from the checked logarithmic answer.'};
    }
  }
  section('sec-6-3').sourceBlocks = [...substitution,...continued];
  section('sec-6-3').sourceReferences = [
    ...Array.from({length:10},(_,i)=>148+i).map(reference),
    ...section('sec-6-3').sourceReferences.map(ref=>ref.page===158?{...ref,verification:'Supplied continuation visually matched to recovered page 157; original printed errors preserved'}:ref)
  ];
  ['sec-6-1','sec-6-2','sec-6-3'].forEach(id=>{
    section(id).sourceStatus='Recovered-page mathematical companion available; external prose paraphrased, original continuation retained';
    section(id).recoveredPageCompanion=true;
  });
  const newPages = Array.from({length:16},(_,i)=>142+i).map(page=>({
    page, file, pdfPage:page-140, title:'Integration — recovered-page companion',
    paragraphs:[], blocks:[...introductory,...rules,...substitution].filter(block=>block.sourcePage===page),
    contentOrigin:origin, visualStatus:'mathematical source inspected; companion prose is newly authored'
  }));
  unit.sourcePages=[...newPages,...unit.sourcePages];
  const example = (num,start,end,problem,steps,answer,sourceClarification) => ({
    id:'we-6-source-'+num,num:String(num),title:'Example '+num,problem,
    given:problem,method:'Use the integration rule and verify by differentiation.',
    steps,answer,solution:steps.join(' ')+' '+answer,progressiveSolution:true,
    solutionOrigin:origin,sourceReferences:Array.from({length:end-start+1},(_,i)=>reference(start+i)),
    ...(sourceClarification?{sourceClarification}:{})
  });
  const examples=[
    example(1,143,143,'Find an antiderivative of '+wrap('f(x)=x^2')+'.',[
      'The power rule raises the exponent from 2 to 3 and divides by 3.',
      wrap('\\frac{d}{dx}\\left(\\frac{x^3}{3}\\right)=x^2')+'.'
    ],wrap('F(x)=\\frac{x^3}{3}')+' is one antiderivative; the complete family is '+wrap('\\frac{x^3}{3}+C')+'.'),
    example(2,145,145,'Find (a) '+wrap('\\int x^{1/3}\\,dx')+' and (b) '+wrap('\\int x^{-3}\\,dx')+'.',[
      '(a) Apply the power rule with n=1/3: '+wrap('\\frac{x^{4/3}}{4/3}=\\frac34x^{4/3}')+'.',
      '(b) Apply it with n=−3: '+wrap('\\frac{x^{-2}}{-2}=-\\frac1{2x^2}')+'.'
    ],'(a) '+wrap('\\frac34x^{4/3}+C')+'; (b) '+wrap('-\\frac1{2x^2}+C')+'.'),
    example(3,147,147,'Integrate (a) 10+a; (b) (10+a)x²; (c) 5x²+4x+2, treating a as a constant.',[
      '(a) Multiply the constant by x. (b) Keep 10+a outside the integral and integrate x².',
      '(c) Integrate the three terms separately using linearity.'
    ],'(a) (10+a)x+C; (b) '+wrap('\\frac{(10+a)x^3}{3}+C')+'; (c) '+wrap('\\frac{5x^3}{3}+2x^2+2x+C')+'.'),
    example(4,148,149,'Integrate (a) '+wrap('(x^3-5x+7)^4(3x^2-5)')+'; (b) '+wrap('\\frac1{9x+7}')+'; (c) '+wrap('e^{3x+2}')+'.',[
      '(a) Set u=x³−5x+7, du=(3x²−5)dx. Integrate u⁴ to get u⁵/5+C.',
      '(b) Set u=9x+7, dx=du/9. Integrate (1/9)du/u.',
      '(c) Set u=3x+2, dx=du/3. Integrate eᵘdu/3.'
    ],'(a) '+wrap('\\frac{(x^3-5x+7)^5}{5}+C')+'; (b) '+wrap('\\frac19\\ln|9x+7|+C')+'; (c) '+wrap('\\frac13e^{3x+2}+C')+'.','Printed part (b) omits the logarithm absolute-value bars; the companion includes them.'),
    example(5,149,149,'A wound has dA/dt=−4t⁻³, A(1)=2 cm² and 1≤t≤10 days. Find A(10).',[
      'Integrate the rate: A(t)=2/t²+C.',
      'Use A(1)=2: 2=2+C, so C=0.',
      'At t=10, A(10)=2/100=0.02.'
    ],'The area after 10 days is 0.02 cm².'),
    example(6,156,157,'Find '+wrap('\\int\\frac{dx}{x^2+4x+5}')+'.',[
      'Complete the square: x²+4x+5=(x+2)²+1.',
      'Set u=x+2, du=dx; the integral is ∫du/(1+u²).',
      'Its antiderivative is arctan u+C. Substitute u=x+2.'
    ],wrap('\\tan^{-1}(x+2)+C')+'.'),
    example(7,157,157,'Find '+wrap('\\int\\frac{dx}{\\sqrt{x^2+4x+5}}')+'.',[
      'Set u=x+2 after completing the square; obtain ∫du/√(u²+1).',
      'With u=tan θ and d u=sec²θ dθ, this becomes ∫sec θ dθ.',
      'Use ln|sec θ+tan θ|+C and return to u, then x.'
    ],wrap('\\ln\\left|x+2+\\sqrt{x^2+4x+5}\\right|+C')+'.','Some printed intermediate lines omit the radical. The integral in the question determines the checked answer.'),
    example(8,157,158,'Find '+wrap('\\int\\frac{x+2}{x^2+4x+5}\\,dx')+'.',[
      'The denominator has derivative 2x+4=2(x+2).',
      'Set v=x²+4x+5, so dv=2(x+2)dx. The integral is (1/2)∫dv/v.',
      'Since v=(x+2)²+1>0 for real x, ln v needs no absolute-value restriction.'
    ],wrap('\\frac12\\ln(x^2+4x+5)+C')+'.','Printed page 158 changes the numerator to x−2 in several continuation lines. The actual page-157 question and its working use x+2.')
  ];
  unit.workedExamples=[...examples,...unit.workedExamples.filter(item=>!examples.some(e=>e.id===item.id))];
  const challenges=[
    {id:'ex-6-recovered-challenge-1',num:'1',question:'Use a hyperbolic substitution to integrate '+wrap('\\sqrt{a^2-x^2}')+' (printed-page-152 challenge).',answer:wrap('\\frac x2\\sqrt{a^2-x^2}+\\frac{a^2}{2}\\sin^{-1}(x/a)+C'),solution:'For a>0 and |x|<a, let x=a tanh u. Then √(a²−x²)=a sech u and dx=a sech²u du, so I=a²∫sech³u du. Differentiate sech u tanh u and arcsin(tanh u): their derivatives are 2sech³u−sech u and sech u. Therefore I=(a²/2)[sech u tanh u+arcsin(tanh u)]+C. Substitution back gives the stated result.',sourceReferences:[reference(152)]},
    {id:'ex-6-recovered-challenge-2',num:'2',question:'Prove the secant-cubed integral used on printed page 153.',answer:wrap('\\int\\sec^3u\\,du=\\frac12\\sec u\\tan u+\\frac12\\ln|\\sec u+\\tan u|+C'),solution:'Let I=∫sec u·sec²u du. Integration by parts with v=tan u and d(sec u)=sec u tan u du gives I=sec u tan u−∫sec u tan²u du. Replace tan²u by sec²u−1, so I=sec u tan u−I+∫sec u du. Move −I to the left, use ∫sec u du=ln|sec u+tan u|+C, and divide by 2.',sourceReferences:[reference(153)]},
    {id:'ex-6-recovered-challenge-3',num:'3',question:'Use a hyperbolic substitution to integrate '+wrap('\\sqrt{x^2+a^2}')+' (printed-page-154 challenge).',answer:wrap('\\frac x2\\sqrt{x^2+a^2}+\\frac{a^2}{2}\\ln\\left|x+\\sqrt{x^2+a^2}\\right|+C'),solution:'For a>0, set x=a sinh u. Then dx=a cosh u du and √(x²+a²)=a cosh u. Thus I=a²∫cosh²u du=(a²/2)u+(a²/4)sinh(2u)+C. Use sinh(2u)=2sinh u cosh u and u=arsinh(x/a)=ln[(x+√(x²+a²))/a]. The constant logarithm −ln a can be absorbed into C.',sourceReferences:[reference(154)]},
    {id:'ex-6-recovered-challenge-4',num:'4',question:'Use a hyperbolic substitution to integrate '+wrap('\\frac1{\\sqrt{x^2+a^2}}')+' (printed-page-154 challenge).',answer:wrap('\\ln\\left|x+\\sqrt{x^2+a^2}\\right|+C'),solution:'For a>0, put x=a sinh u. The differential a cosh u du cancels the denominator a cosh u, leaving ∫du=u+C. Substitute u=arsinh(x/a)=ln[(x+√(x²+a²))/a] and absorb −ln a into C.',sourceReferences:[reference(154)]},
    {id:'ex-6-recovered-challenge-5',num:'5',question:'Use hyperbolic substitution and a product-to-sum identity to integrate '+wrap('\\sqrt{x^2-a^2}')+' (printed-page-156 challenge).',answer:wrap('\\frac x2\\sqrt{x^2-a^2}-\\frac{a^2}{2}\\ln\\left|x+\\sqrt{x^2-a^2}\\right|+C'),solution:'For a>0 and x>a, set x=a cosh u with u>0. Then dx=a sinh u du and √(x²−a²)=a sinh u. Thus I=a²∫sinh²u du=(a²/4)sinh(2u)−(a²/2)u+C. Replace sinh(2u) by 2sinh u cosh u and u by arcosh(x/a)=ln[(x+√(x²−a²))/a]. The displayed expression differentiates correctly on either interval |x|>a, with an independently chosen constant on each.',sourceReferences:[reference(156)]}
  ];
  unit.exercises.push({
    id:'ex-6-recovered-substitution-challenges',title:'Challenges — Recovered Substitution Pages',
    description:'Newly authored solutions to the mathematical challenges on recovered pages 152–156.',
    pageStart:152,pageEnd:156,sectionIds:['sec-6-3'],problems:challenges,
    sourceContextBlocks:[clarification(152,'These five challenges include the four hyperbolic-substitution boxes and the secant-cubed proof request. Answers are SpaceBook explanations, not a printed answer key.')]
  });
  const challengeNotice=paragraph(156,
    'The four hyperbolic-substitution challenges and the secant-cubed proof are answered in “Challenges — Recovered Substitution Pages” in the exercise tab.',
    'ہائپربولک متبادل کے چار چیلنج اور سیکنٹ کی تیسری قوت کے تکمل کا ثبوت مشقوں کے حصے میں “Challenges — Recovered Substitution Pages” کے تحت حل کیے گئے ہیں۔',
    'د هایپربولیک بدلولو څلور ننګونې او د سیکنټ د درېیم توان د تکامل ثبوت د تمرینونو په برخه کې د “Challenges — Recovered Substitution Pages” تر نوم لاندې حل شوي دي.');
  const challengeIndex=section('sec-6-3').sourceBlocks.findIndex(block=>block.type==='heading'&&block.sourcePage===156);
  section('sec-6-3').sourceBlocks.splice(challengeIndex<0?0:challengeIndex,0,challengeNotice);
  const meanings={
    antiderivative:['ضد مشتق','ضد مشتق'],antiderivatives:['ضد مشتقات','ضد مشتقونه'],
    accumulation:['جمع ہونے کا عمل','د راټولېدو بهیر'],accumulated:['جمع شدہ','راټول شوی'],
    integrand:['زیرِ تکمل تفاعل','تر تکامل لاندې تابع'],substitution:['متبادل رکھنے کا طریقہ','د بدلولو طریقه'],
    indefinite:['غیر معین','ناتاکلی'],definite:['معین','ټاکلی'],arbitrary:['اختیاری','اختیاري'],
    logarithmic:['لوگارتھمی','لوګاریتمي'],hyperbolic:['ہائپربولک','هایپربولیک'],
    numerator:['صورت','صورت'],denominator:['مخرج','مخرج'],radical:['جذر','ریښه'],
    differentiate:['مشتق لیں','مشتق واخلئ'],integrate:['تکمل لیں','تکامل واخلئ'],
    interval:['وقفہ','واټن'],constant:['مستقل','ثابت'],linear:['خطی','خطي'],
    rate:['شرح','کچه'],wound:['زخم','ټپ'],volume:['حجم','حجم']
  };
  if(typeof MATH12_WORD_MEANINGS!=='undefined') {
    Object.keys(meanings).forEach(key=>{if(!MATH12_WORD_MEANINGS[key])MATH12_WORD_MEANINGS[key]=meanings[key];});
  }
})();
