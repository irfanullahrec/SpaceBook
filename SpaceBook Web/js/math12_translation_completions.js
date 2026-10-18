// Authored translations for the reviewed source blocks of Unit 1, sections
// 1.1–1.4. Original English, commands, matrices and printed errors remain
// untouched. Existing translations and cached meanings take precedence.
(function () {
    'use strict';
    if (typeof MATH_12_DATA === 'undefined' || typeof MATH12_SENTENCE_TRANSLATIONS === 'undefined') return;

    const translations = new Map();
    const passage = (en, ur, ps) => translations.set(en, [{ en, ur, ps }]);
    const sentences = rows => translations.set(rows.map(row => row[0]).join(' '), rows.map(([en, ur, ps]) => ({ en, ur, ps })));

    passage('1.2 Polynomials', '1.2 کثیرالحدی عبارتیں', '1.2 کثیرالحدي عبارتونه');
    sentences([
        ['We are familiar about polynomials since our previous grades.', 'ہم پچھلی جماعتوں سے کثیرالحدی عبارتوں سے واقف ہیں۔', 'موږ له تېرو ټولګیو څخه له کثیرالحدي عبارتونو سره بلد یو.'],
        ['The factorization of a polynomial, expansion of an expression can be solved through direct MAPLE commands and context menus.', 'کثیرالحدی کے عوامل معلوم کرنے اور کسی عبارت کو پھیلانے کا کام MAPLE کے براہِ راست احکامات اور سیاقی مینو کے ذریعے کیا جا سکتا ہے۔', 'د کثیرالحدي عبارت په عاملونو وېشل او د یوه عبارت پراخول د MAPLE د مستقیمو امرونو او سیاقي مېنوګانو له لارې ترسره کېدای شي.']
    ]);
    passage('1.2.1 Use of MAPLE commands for factoring a polynomial', '1.2.1 کثیرالحدی کے عوامل معلوم کرنے کے لیے MAPLE کے احکامات کا استعمال', '1.2.1 د کثیرالحدي عبارت په عاملونو وېشلو لپاره د MAPLE د امرونو کارول');
    passage('(a) Commands', '(a) احکامات', '(a) امرونه');
    passage('(a) Command', '(a) حکم', '(a) امر');
    passage('(b) Context menu result', '(b) سیاقی مینو کا نتیجہ', '(b) د سیاقي مېنو پایله');
    sentences([
        ['You can use Maple’s context menus to perform a wide variety of mathematical and other operations.', 'آپ بہت سے مختلف ریاضیاتی اور دیگر اعمال انجام دینے کے لیے Maple کے سیاقی مینو استعمال کر سکتے ہیں۔', 'تاسو د بېلابېلو ریاضيکي او نورو عملونو د ترسره کولو لپاره د Maple سیاقي مېنوګانې کارولی شئ.'],
        ['Enter the polynomial and place your cursor at the end of the polynomial or expressions and right-click.', 'کثیرالحدی درج کریں، کرسر کو کثیرالحدی یا عبارتوں کے آخر میں رکھیں اور ماؤس کا دایاں بٹن دبائیں۔', 'کثیرالحدي عبارت دننه کړئ، کرسر د کثیرالحدي یا عبارتونو په پای کې کېږدئ او ښی کلیک وکړئ.'],
        ['The command will show you full information about factorization on line by typing.', 'حکم ٹائپ کرنے سے عوامل معلوم کرنے کے بارے میں مکمل آن لائن معلومات دکھائی جائیں گی۔', 'د امر په ټایپ کولو سره به د عاملونو په اړه بشپړ انلاین معلومات دروښودل شي.'],
        ['Then choose the factor option from the open window as shown in Figure 1.5.', 'پھر کھلی ہوئی ونڈو سے factor کا اختیار منتخب کریں، جیسا کہ شکل 1.5 میں دکھایا گیا ہے۔', 'بیا له پرانیستې کړکۍ څخه د factor غوراوی وټاکئ، لکه څنګه چې په شکل 1.5 کې ښودل شوی دی.'],
        ['The context menu offers several operation to choose from according to the expression that you are using.', 'سیاقی مینو آپ کی استعمال کردہ عبارت کے مطابق انتخاب کے لیے کئی اعمال پیش کرتا ہے۔', 'سیاقي مېنو د هغه عبارت له مخې چې تاسو یې کاروئ، د ټاکلو لپاره څو عملونه وړاندې کوي.'],
        ['The above result through context menu is as under:', 'سیاقی مینو کے ذریعے حاصل ہونے والا مذکورہ نتیجہ درج ذیل ہے:', 'د سیاقي مېنو له لارې پورته پایله په لاندې ډول ده:']
    ]);
    sentences([
        ['The result is obtained through right-click on the last end of the expression by selecting “Factor” on the context menus.', 'عبارت کے بالکل آخر میں دایاں کلک کر کے سیاقی مینو سے “Factor” منتخب کرنے پر یہ نتیجہ حاصل ہوتا ہے۔', 'د عبارت په وروستي پای کې د ښي کلیک او له سیاقي مېنو څخه د “Factor” په ټاکلو سره پایله ترلاسه کېږي.'],
        ['As shown in Figure 1.5.', 'جیسا کہ شکل 1.5 میں دکھایا گیا ہے۔', 'لکه څنګه چې په شکل 1.5 کې ښودل شوی دی.']
    ]);
    passage('1.2.2 Use of MAPLE commands for expanding an expression', '1.2.2 کسی عبارت کو پھیلانے کے لیے MAPLE کے احکامات کا استعمال', '1.2.2 د یوه عبارت د پراخولو لپاره د MAPLE د امرونو کارول');
    passage('Use MAPLE command “expand” before parenthesis to expand the given expression.', 'دی گئی عبارت کو پھیلانے کے لیے قوسین سے پہلے MAPLE کا حکم “expand” استعمال کریں۔', 'د ورکړل شوي عبارت د پراخولو لپاره تر قوسونو مخکې د MAPLE د “expand” امر وکاروئ.');
    sentences([
        ['Enter the given expression and place your cursor on the last end of the expression and right click.', 'دی گئی عبارت درج کریں، کرسر کو عبارت کے بالکل آخر میں رکھیں اور دایاں کلک کریں۔', 'ورکړل شوی عبارت دننه کړئ، کرسر یې په وروستي پای کې کېږدئ او ښی کلیک وکړئ.'],
        ['Then choose expand option from the opened window as shown in the Figure 1.6.', 'پھر کھلی ہوئی ونڈو سے expand کا اختیار منتخب کریں، جیسا کہ شکل 1.6 میں دکھایا گیا ہے۔', 'بیا له پرانیستې کړکۍ څخه د expand غوراوی وټاکئ، لکه څنګه چې په شکل 1.6 کې ښودل شوی دی.']
    ]);
    passage('1.2.3 Use of MAPLE commands for simplifying an expression', '1.2.3 کسی عبارت کو سادہ کرنے کے لیے MAPLE کے احکامات کا استعمال', '1.2.3 د یوه عبارت د ساده کولو لپاره د MAPLE د امرونو کارول');
    sentences([
        ['Enter the given expression and place your cursor on the last end of the expression and right click.', 'دی گئی عبارت درج کریں، کرسر کو عبارت کے بالکل آخر میں رکھیں اور دایاں کلک کریں۔', 'ورکړل شوی عبارت دننه کړئ، کرسر یې په وروستي پای کې کېږدئ او ښی کلیک وکړئ.'],
        ['Then choose “simplify” from the opened window as shown in the Figure 1.7.', 'پھر کھلی ہوئی ونڈو سے “simplify” منتخب کریں، جیسا کہ شکل 1.7 میں دکھایا گیا ہے۔', 'بیا له پرانیستې کړکۍ څخه “simplify” وټاکئ، لکه څنګه چې په شکل 1.7 کې ښودل شوی دی.']
    ]);
    passage('1.2.4 Use of MAPLE commands for simplifying a rational expression', '1.2.4 کسی ناطق عبارت کو سادہ کرنے کے لیے MAPLE کے احکامات کا استعمال', '1.2.4 د یوه ناطق عبارت د ساده کولو لپاره د MAPLE د امرونو کارول');
    sentences([
        ['Enter the given expression and place your cursor on the last end of the expression and right click.', 'دی گئی عبارت درج کریں، کرسر کو عبارت کے بالکل آخر میں رکھیں اور دایاں کلک کریں۔', 'ورکړل شوی عبارت دننه کړئ، کرسر یې په وروستي پای کې کېږدئ او ښی کلیک وکړئ.'],
        ['Then select “simplify” option as shown in the Figure 1.8.', 'پھر “simplify” کا اختیار منتخب کریں، جیسا کہ شکل 1.8 میں دکھایا گیا ہے۔', 'بیا د “simplify” غوراوی وټاکئ، لکه څنګه چې په شکل 1.8 کې ښودل شوی دی.']
    ]);
    passage('1.2.5 Use of MAPLE commands for substituting on expression', '1.2.5 کسی عبارت میں قیمت رکھنے کے لیے MAPLE کے احکامات کا استعمال', '1.2.5 په یوه عبارت کې د ارزښت د ځای پر ځای کولو لپاره د MAPLE د امرونو کارول');
    sentences([
        ['Enter the given expression and place your cursor on last end of the expression and right click.', 'دی گئی عبارت درج کریں، کرسر کو عبارت کے بالکل آخر میں رکھیں اور دایاں کلک کریں۔', 'ورکړل شوی عبارت دننه کړئ، کرسر یې په وروستي پای کې کېږدئ او ښی کلیک وکړئ.'],
        ['Then select “evaluate at a point” option as shown in the Figure 1.9 and Figure 1.10 respectively.', 'پھر “evaluate at a point” کا اختیار منتخب کریں، جیسا کہ بالترتیب شکل 1.9 اور شکل 1.10 میں دکھایا گیا ہے۔', 'بیا د “evaluate at a point” غوراوی وټاکئ، لکه څنګه چې په ترتیب سره په شکل 1.9 او شکل 1.10 کې ښودل شوی دی.']
    ]);

    passage('Figure 1.5', 'شکل 1.5', 'شکل 1.5');
    passage('Figure 1.6', 'شکل 1.6', 'شکل 1.6');
    passage('Figure 1.7', 'شکل 1.7', 'شکل 1.7');
    passage('Figure 1.8', 'شکل 1.8', 'شکل 1.8');
    passage('Figure 1.9', 'شکل 1.9', 'شکل 1.9');
    passage('Figure 1.10', 'شکل 1.10', 'شکل 1.10');
    passage('Maple context menu with the Factor operation selected', 'Maple کا سیاقی مینو، جس میں Factor کا عمل منتخب ہے', 'د Maple سیاقي مېنو چې د Factor عمل پکې ټاکل شوی دی');
    passage('Maple context menu with Expand and its Apply Immediately submenu selected', 'Maple کا سیاقی مینو، جس میں Expand اور اس کا ذیلی مینو Apply Immediately منتخب ہیں', 'د Maple سیاقي مېنو چې Expand او د هغه فرعي مېنو Apply Immediately پکې ټاکل شوي دي');
    passage('Maple Simplify submenu showing the Simplify operation selected', 'Maple کا Simplify ذیلی مینو، جس میں Simplify کا عمل منتخب دکھایا گیا ہے', 'د Maple د Simplify فرعي مېنو چې د Simplify ټاکل شوی عمل ښيي');
    passage('Maple context menu Simplify operation for a rational expression', 'ناطق عبارت کے لیے Maple کے سیاقی مینو کا Simplify عمل', 'د ناطق عبارت لپاره د Maple په سیاقي مېنو کې د Simplify عمل');
    passage('Maple context menu with Evaluate at a Point selected', 'Maple کا سیاقی مینو، جس میں Evaluate at a Point منتخب ہے', 'د Maple سیاقي مېنو چې Evaluate at a Point پکې ټاکل شوی دی');
    passage('Maple Evaluate at a Point dialog specifying t = 20', 'Maple کا Evaluate at a Point مکالماتی خانہ، جس میں t = 20 مقرر ہے', 'د Maple د Evaluate at a Point خبرو اترو بکس چې t = 20 پکې ټاکل شوی دی');

    passage('1.4 Matrices', '1.4 میٹرکسیں', '1.4 ماتریسونه');
    passage('The command will show you full information about matrices on line by typing: [ > ?matrices', 'یہ حکم ٹائپ کرنے سے میٹرکسوں کے بارے میں مکمل آن لائن معلومات دکھائی جائیں گی: [ > ?matrices', 'د دې امر په ټایپ کولو سره به د ماتریسونو په اړه بشپړ انلاین معلومات دروښودل شي: [ > ?matrices');
    passage('1.4.1 Recognition of matrix and vector entry arrangement', '1.4.1 میٹرکس اور سمتیہ کے اندراجات کی ترتیب کی پہچان', '1.4.1 د ماتریس او ویکتور د عناصرو د ترتیب پېژندنه');
    passage('(b) Using Palettes', '(b) پیلیٹ استعمال کرنا', '(b) د پلېټونو کارول');
    sentences([
        ['Use cursor button to select matrix palette.', 'میٹرکس پیلیٹ منتخب کرنے کے لیے کرسر کا بٹن استعمال کریں۔', 'د ماتریس پلېټ د ټاکلو لپاره د کرسر تڼۍ وکاروئ.'],
        ['Click- “matrix” <click-choose(for the umber of rows and columns of a required matrix) <click-data type (to select integers entries of the rows and columns of a required matrix), then finally click-“insert matrix” and press ENTER key to obtain a required matrix.', '“matrix” پر کلک کریں، پھر choose پر کلک کر کے مطلوبہ میٹرکس کی قطاروں اور کالموں کی تعداد منتخب کریں، پھر data type پر کلک کر کے مطلوبہ میٹرکس کی قطاروں اور کالموں کے صحیح عددی اندراجات منتخب کریں؛ آخر میں “insert matrix” پر کلک کریں اور مطلوبہ میٹرکس حاصل کرنے کے لیے ENTER کی کلید دبائیں۔', 'پر “matrix” کلیک وکړئ، بیا پر choose کلیک وکړئ او د اړین ماتریس د قطارونو او ستونونو شمېر وټاکئ؛ وروسته پر data type کلیک وکړئ او د اړین ماتریس د قطارونو او ستونونو صحیح عددي عناصر وټاکئ؛ په پای کې پر “insert matrix” کلیک وکړئ او د اړین ماتریس د ترلاسه کولو لپاره د ENTER کیلي کېکاږئ.']
    ]);
    passage('1.4.2 Applying matrix operations', '1.4.2 میٹرکس کے اعمال کا اطلاق', '1.4.2 د ماتریس د عملونو کارول');
    passage('(a) Matrix addition', '(a) میٹرکسوں کی جمع', '(a) د ماتریسونو جمع');
    passage('(b) Matrix multiplication', '(b) میٹرکسوں کی ضرب', '(b) د ماتریسونو ضرب');
    passage('(c) Using Palettes', '(c) پیلیٹ استعمال کرنا', '(c) د پلېټونو کارول');
    passage('To obtain the result simply right click on the last “matrix” then click simplify or press ENTER.', 'نتیجہ حاصل کرنے کے لیے آخری “matrix” پر دایاں کلک کریں، پھر simplify پر کلک کریں یا ENTER دبائیں۔', 'د پایلې د ترلاسه کولو لپاره پر وروستي “matrix” ښی کلیک وکړئ، بیا پر simplify کلیک وکړئ یا ENTER کېکاږئ.');
    passage('1.4.3 Inverse and transpose of a matrix', '1.4.3 میٹرکس کا معکوس اور منقولہ', '1.4.3 د ماتریس معکوس او ترانسپوز');
    passage('(a) Inverse of a matrix', '(a) میٹرکس کا معکوس', '(a) د ماتریس معکوس');
    passage('(b) Transport of a matrix', '(b) میٹرکس کی منتقلی', '(b) د ماتریس لېږد');
    passage('Inverse of a matrix', 'میٹرکس کا معکوس', 'د ماتریس معکوس');
    sentences([
        ['To obtain the result through context menu.', 'سیاقی مینو کے ذریعے نتیجہ حاصل کرنے کے لیے۔', 'د سیاقي مېنو له لارې د پایلې د ترلاسه کولو لپاره.'],
        ['Right-click on the last end of the matrix by selecting “Standard operations” and then right-click on the “inverse” to obtained the inverse of a matrix.', 'میٹرکس کے بالکل آخر میں دایاں کلک کر کے “Standard operations” منتخب کریں، پھر میٹرکس کا معکوس حاصل کرنے کے لیے “inverse” پر دایاں کلک کریں۔', 'د ماتریس په وروستي پای کې ښی کلیک وکړئ او “Standard operations” وټاکئ؛ بیا د ماتریس د معکوس د ترلاسه کولو لپاره پر “inverse” ښی کلیک وکړئ.']
    ]);
    passage('Similarly,', 'اسی طرح،', 'په همدې ډول،');
    passage('Transpose of a matrix', 'میٹرکس کا منقولہ', 'د ماتریس ترانسپوز');
    sentences([
        ['To obtain the result through context menu.', 'سیاقی مینو کے ذریعے نتیجہ حاصل کرنے کے لیے۔', 'د سیاقي مېنو له لارې د پایلې د ترلاسه کولو لپاره.'],
        ['Right-click on the last end of the matrix by selecting “Standard operations” and then right-click on the “transpose” to obtained the inverse of a matrix.', 'میٹرکس کے بالکل آخر میں دایاں کلک کر کے “Standard operations” منتخب کریں، پھر میٹرکس کا معکوس حاصل کرنے کے لیے “transpose” پر دایاں کلک کریں۔', 'د ماتریس په وروستي پای کې ښی کلیک وکړئ او “Standard operations” وټاکئ؛ بیا د ماتریس د معکوس د ترلاسه کولو لپاره پر “transpose” ښی کلیک وکړئ.']
    ]);
    passage('Determinant of a matrix', 'میٹرکس کا مقطع', 'د ماتریس ټاکونکی');
    sentences([
        ['To obtain the result through context menu.', 'سیاقی مینو کے ذریعے نتیجہ حاصل کرنے کے لیے۔', 'د سیاقي مېنو له لارې د پایلې د ترلاسه کولو لپاره.'],
        ['Right-click on the last end of the matrix by selecting “Standard operations” and then right-click on the “determinant” to obtained the inverse of a matrix.', 'میٹرکس کے بالکل آخر میں دایاں کلک کر کے “Standard operations” منتخب کریں، پھر میٹرکس کا معکوس حاصل کرنے کے لیے “determinant” پر دایاں کلک کریں۔', 'د ماتریس په وروستي پای کې ښی کلیک وکړئ او “Standard operations” وټاکئ؛ بیا د ماتریس د معکوس د ترلاسه کولو لپاره پر “determinant” ښی کلیک وکړئ.']
    ]);
    sentences([
        ['The heading on page 23 prints “Transport”; the command computes a transpose.', 'صفحہ 23 کے عنوان میں “Transport” چھپا ہے؛ حکم میٹرکس کا منقولہ معلوم کرتا ہے۔', 'د 23 مخ په سرلیک کې “Transport” چاپ شوی دی؛ امر د ماتریس ترانسپوز محاسبه کوي.'],
        ['On this page the transpose and determinant instructions repeat “inverse”.', 'اس صفحے پر منقولہ اور مقطع کی ہدایات میں “inverse” کا لفظ دوبارہ آیا ہے۔', 'په دې مخ کې د ترانسپوز او ټاکونکي لارښوونې د “inverse” کلمه بیا کاروي.'],
        ['The transpose returns the matrix with rows and columns exchanged; the determinant returns a scalar.', 'منقولہ ایسا میٹرکس دیتا ہے جس کی قطاریں اور کالم آپس میں بدل گئے ہوں؛ مقطع ایک غیر سمتی مقدار دیتا ہے۔', 'ترانسپوز داسې ماتریس راکوي چې قطارونه او ستونونه یې سره بدل شوي وي؛ ټاکونکی یوه سکالري اندازه راکوي.'],
        ['The original wording above is preserved.', 'اوپر اصل عبارت برقرار رکھی گئی ہے۔', 'پورته اصلي عبارت ساتل شوی دی.']
    ]);

    // Section 1.1 prose already has reviewed translations in the base data.
    // These exact keys fill its headings and figure descriptions without
    // replacing any of those earlier translations.
    passage('1.1 Introduction', '1.1 تعارف', '1.1 پېژندنه');
    passage('1.1.1 Recognition of MAPLE environment', '1.1.1 MAPLE کے ماحول کی پہچان', '1.1.1 د MAPLE د چاپېریال پېژندنه');
    passage('A. Getting started with Maple', 'A. Maple کا استعمال شروع کرنا', 'A. له Maple سره کار پیلول');
    passage('1.1.2 Recognition of basic MAPLE commands', '1.1.2 MAPLE کے بنیادی احکامات کی پہچان', '1.1.2 د MAPLE د بنسټیزو امرونو پېژندنه');
    passage('Remember', 'یاد رکھیں', 'په یاد ولرئ');
    passage('i. Save command:', 'i. محفوظ کرنے کا حکم:', 'i. د خوندي کولو امر:');
    passage('ii. Editing commands:', 'ii. احکامات میں ترمیم:', 'ii. د امرونو سمون:');
    passage('iii. Exact arithmetic and floating-point (evalf) commands:', 'iii. عین حساب اور ممیزِ متحرک (evalf) کے احکامات:', 'iii. د دقیق حساب او خوځنده ممیز (evalf) امرونه:');
    passage('iv. Maple internal memory clearing command:', 'iv. Maple کی اندرونی یادداشت صاف کرنے کا حکم:', 'iv. د Maple د دننۍ حافظې د پاکولو امر:');
    passage('v. Enlistment of variables:', 'v. متغیرات کا اندراج:', 'v. د متحولونو ثبتول:');
    passage('1.1.3 Use of MAPLE as a calculator', '1.1.3 MAPLE کا بطور کیلکولیٹر استعمال', '1.1.3 د حسابګر په توګه د MAPLE کارول');
    passage('(a) Maplesoft (TM) Graphing Calculator Overview', '(a) Maplesoft (TM) کے گرافیکی کیلکولیٹر کا جائزہ', '(a) د Maplesoft (TM) ګرافیکي حسابګر ته کتنه');
    passage('On toolbar,', 'ٹول بار پر،', 'په توکپټه کې،');
    passage('Example 1', 'مثال 1', 'بېلګه 1');
    passage('Example 2', 'مثال 2', 'بېلګه 2');
    passage('Solution', 'حل', 'حل');
    passage('(b) Unit calculator', '(b) اکائیوں کا کیلکولیٹر', '(b) د واحدونو حسابګر');
    passage('1.1.4 Online MAPLE help', '1.1.4 MAPLE کی آن لائن مدد', '1.1.4 د MAPLE انلاین مرسته');
    passage('Figure 1.1 Maple start menu', 'شکل 1.1 Maple کا ابتدائی مینو', 'شکل 1.1 د Maple د پیل مېنو');
    passage('Figure 1.2', 'شکل 1.2', 'شکل 1.2');
    passage('Figure 1.3', 'شکل 1.3', 'شکل 1.3');
    passage('Figure 1.4', 'شکل 1.4', 'شکل 1.4');
    passage('Maple start screen with task icons and the palettes sidebar', 'Maple کی ابتدائی سکرین، جس میں کاموں کی علامتیں اور پیلیٹ کی ضمنی پٹی ہے', 'د Maple د پیل پرده چې د دندو نښانونه او د پلېټونو اړخپټه لري');
    passage('Maple File menu with Exit selected, beside a worksheet containing a plotted parabola', 'ایک قطعِ مکافی کے گراف والی ورک شیٹ کے ساتھ Maple کا File مینو، جس میں Exit منتخب ہے', 'د رسم شوي پارابولا لرونکې کاري پاڼې تر څنګ د Maple د File مېنو چې Exit پکې ټاکل شوی دی');
    passage('Maplesoft Units Calculator with input and output unit selectors', 'Maplesoft کا اکائیوں کا کیلکولیٹر، جس میں داخلی اور خارجی اکائیوں کے انتخاب کے خانے ہیں', 'د Maplesoft د واحدونو حسابګر چې د ننوتلو او وتلو د واحدونو ټاکونکي لري');
    passage('Maple help window describing arithmetic operators', 'Maple کی مدد کی ونڈو، جس میں حسابی عوامل کی وضاحت ہے', 'د Maple د مرستې کړکۍ چې حسابي عملګر تشریح کوي');

    passage('1.3 Graphics', '1.3 گرافکس', '1.3 ګرافیک');
    passage('1.3.1 Plot a two dimensional graph', '1.3.1 دو بُعدی گراف بنانا', '1.3.1 د دوه بعدي ګراف رسمول');
    passage('To plot any two dimensional graph in MAPLE we use “plot” command in the command prompt.', 'MAPLE میں کوئی بھی دو بُعدی گراف بنانے کے لیے ہم کمانڈ پرامپٹ میں “plot” کا حکم استعمال کرتے ہیں۔', 'په MAPLE کې د هر دوه بعدي ګراف د رسمولو لپاره د امر په پرامپټ کې د “plot” امر کاروو.');
    passage('Example 3', 'مثال 3', 'بېلګه 3');
    passage('Plot the graph of \\(x^2+3x+8\\).', '\\(x^2+3x+8\\) کا گراف بنائیں۔', 'د \\(x^2+3x+8\\) ګراف رسم کړئ.');
    passage('The graph of \\(x^2+3x+8\\) is shown in the Figure 1.11 and 1.12 respectively.', '\\(x^2+3x+8\\) کا گراف بالترتیب شکل 1.11 اور 1.12 میں دکھایا گیا ہے۔', 'د \\(x^2+3x+8\\) ګراف په ترتیب سره په شکل 1.11 او 1.12 کې ښودل شوی دی.');
    passage('This result is obtained through right click on the last end of the expression by selection “plots< 2-D plot” on the context menu.', 'یہ نتیجہ عبارت کے بالکل آخر میں دایاں کلک کر کے سیاقی مینو سے “plots< 2-D plot” منتخب کرنے سے حاصل ہوتا ہے۔', 'دا پایله د عبارت په وروستي پای کې په ښي کلیک کولو او له سیاقي مېنو څخه د “plots< 2-D plot” په ټاکلو ترلاسه کېږي.');
    passage('1.3.2 Domain and Range of a plot', '1.3.2 گراف کا دائرۂ کار اور سعت', '1.3.2 د ګراف د تعریف ساحه او د ارزښتونو ساحه');
    sentences([
        ['To plot a two dimensional graph with domain and range.', 'دائرۂ کار اور سعت کے ساتھ دو بُعدی گراف بنانے کے لیے۔', 'د تعریف او ارزښتونو له ساحو سره د دوه بعدي ګراف د رسمولو لپاره.'],
        ['We use “plot” command in the command prompt.', 'ہم کمانڈ پرامپٹ میں “plot” کا حکم استعمال کرتے ہیں۔', 'موږ د امر په پرامپټ کې د “plot” امر کاروو.']
    ]);
    passage('Example 4', 'مثال 4', 'بېلګه 4');
    passage('Plot the graph of \\(x^2+2\\) having domain −3 to 3.', '\\(x^2+2\\) کا گراف بنائیں جس کا دائرۂ کار −3 سے 3 تک ہے۔', 'د \\(x^2+2\\) ګراف رسم کړئ چې د تعریف ساحه یې له −3 څخه تر 3 پورې ده.');
    passage('The graph of \\(x^2+2\\) is shown in the Figure 1.13 and 1.14 respectively.', '\\(x^2+2\\) کا گراف بالترتیب شکل 1.13 اور 1.14 میں دکھایا گیا ہے۔', 'د \\(x^2+2\\) ګراف په ترتیب سره په شکل 1.13 او 1.14 کې ښودل شوی دی.');
    passage('Enter an expression or function, right click on it and select plots < plot builder < 2-D plot and enter the domain for the expression or function.', 'عبارت یا تفاعل درج کریں، اس پر دایاں کلک کر کے plots < plot builder < 2-D plot منتخب کریں اور عبارت یا تفاعل کا دائرۂ کار درج کریں۔', 'عبارت یا تابع دننه کړئ، پرې ښی کلیک وکړئ، plots < plot builder < 2-D plot وټاکئ او د عبارت یا تابع د تعریف ساحه دننه کړئ.');
    passage('1.3.3 Sketch parametric equation', '1.3.3 پارامتری مساوات کا خاکہ بنانا', '1.3.3 د پارامتري معادلې رسمول');
    sentences([
        ['To sketch the parametric equation in MAPLE.', 'MAPLE میں پارامتری مساوات کا خاکہ بنانے کے لیے۔', 'په MAPLE کې د پارامتري معادلې د رسمولو لپاره.'],
        ['We use MAPLE “plot” as discussed in the following example.', 'ہم MAPLE کا “plot” استعمال کرتے ہیں، جیسا کہ درج ذیل مثال میں بیان کیا گیا ہے۔', 'موږ د MAPLE د “plot” امر کاروو، لکه څنګه چې په لاندې بېلګه کې بیان شوی دی.']
    ]);
    passage('Example 5', 'مثال 5', 'بېلګه 5');
    passage('Sketch the graph of parametric equation \\(x=\\cos(t)\\) and \\(x=\\sin(t)\\).', 'پارامتری مساوات \\(x=\\cos(t)\\) اور \\(x=\\sin(t)\\) کا گراف بنائیں۔', 'د پارامتري معادلو \\(x=\\cos(t)\\) او \\(x=\\sin(t)\\) ګراف رسم کړئ.');
    passage('Where \\(-4\\leq t\\leq4\\), x = −2 to 2 and y = −2 to 2', 'جہاں \\(-4\\leq t\\leq4\\)، x = −2 سے 2 تک اور y = −2 سے 2 تک ہے', 'چېرې چې \\(-4\\leq t\\leq4\\)، x = له −2 څخه تر 2 پورې او y = له −2 څخه تر 2 پورې دی');
    passage('Enter an expression or function, right click on it and select plots < plot builder < 2-D parametric plot and domain for the parametric t.', 'عبارت یا تفاعل درج کریں، اس پر دایاں کلک کر کے plots < plot builder < 2-D parametric plot منتخب کریں اور پارامیٹر t کا دائرۂ کار منتخب کریں۔', 'عبارت یا تابع دننه کړئ، پرې ښی کلیک وکړئ، plots < plot builder < 2-D parametric plot او د پارامیټر t د تعریف ساحه وټاکئ.');
    for (const number of [11, 12, 13, 14, 15, 16, 17]) passage(`Figure 1.${number}`, `شکل 1.${number}`, `شکل 1.${number}`);
    passage('Original partial-circle plot shown for the context-menu parametric example', 'سیاقی مینو کی پارامتری مثال کے لیے دکھایا گیا اصل نامکمل دائرے کا گراف', 'د سیاقي مېنو د پارامتري بېلګې لپاره ښودل شوی د دایرې د یوې برخې اصلي ګراف');
    passage('1.3.4 Know plotting options', '1.3.4 گراف بنانے کے اختیارات سے واقفیت', '1.3.4 د ګراف رسمولو د غوراویو پېژندنه');
    sentences([
        ['The plotting options listed below can provide the commands that create 2-D plots.', 'ذیل میں درج گراف سازی کے اختیارات دو بُعدی گراف بنانے والے احکامات کو فراہم کیے جا سکتے ہیں۔', 'لاندې لېست شوي د رسمولو غوراوي هغو امرونو ته ورکول کېدای شي چې دوه بعدي ګرافونه جوړوي.'],
        ['These options can be used with the “plot” command and are generally available to all Maple commands that generate two dimensional plots.', 'یہ اختیارات “plot” کے حکم کے ساتھ استعمال کیے جا سکتے ہیں اور عموماً Maple کے ان تمام احکامات کے لیے دستیاب ہیں جو دو بُعدی گراف بناتے ہیں۔', 'دا غوراوي د “plot” له امر سره کارول کېدای شي او عموماً د Maple ټولو هغو امرونو ته شته چې دوه بعدي ګرافونه جوړوي.'],
        ['The help page of Maple for a particular command provides more detail about the plotting options that accepts.', 'کسی خاص حکم کے لیے Maple کا مدد کا صفحہ ان گراف سازی کے اختیارات کی مزید تفصیل دیتا ہے جنہیں وہ حکم قبول کرتا ہے۔', 'د ځانګړي امر لپاره د Maple د مرستې پاڼه د رسمولو د هغو غوراویو په اړه نور تفصیل ورکوي چې هغه امر یې مني.']
    ]);
    passage('Options must be added at the end of the given sequence.', 'اختیارات دی گئی ترتیب کے آخر میں شامل کیے جانے چاہییں۔', 'غوراوي باید د ورکړل شوي ترتیب په پای کې ورزیات شي.');
    passage('We can use an interactive method of exploring the options in the “plot” command by using the Interactive Plot Builder.', 'Interactive Plot Builder استعمال کر کے ہم “plot” کے حکم کے اختیارات کو جانچنے کا ایک تعاملی طریقہ اختیار کر سکتے ہیں۔', 'د Interactive Plot Builder په کارولو سره موږ د “plot” په امر کې د غوراویو د پلټلو متقابل میتود کارولی شو.');

    for (const [en, ur, ps] of [
        ['Adaptive', 'حسبِ ضرورت موافقت', 'د اړتیا له مخې سمون'],
        ['Annotation', 'توضیحی نوٹ', 'تشریحي یادښت'],
        ['Axes', 'محور', 'محورونه'],
        ['Axes font', 'محوروں کا رسم الخط', 'د محورونو لیکبڼه'],
        ['Axis', 'محور', 'محور'],
        ['Axis coordinates', 'محور کے محددات', 'د محور مختصات'],
        ['Note', 'نوٹ', 'یادښت'],
        ['Background', 'پس منظر', 'شالید'],
        ['Caption', 'توضیحی عنوان', 'تشریحي سرلیک'],
        ['Caption font', 'توضیحی عنوان کا رسم الخط', 'د تشریحي سرلیک لیکبڼه'],
        ['Color', 'رنگ', 'رنګ'],
        ['Color scheme', 'رنگوں کی ترتیب', 'د رنګونو ترتیب'],
        ['Coordinate view', 'محددات کا منظر', 'د مختصاتو لید'],
        ['Cords', 'کورڈز', 'کورډز'],
        ['Discount', 'ڈسکاؤنٹ', 'ډسکاونټ'],
        ['Filled', 'بھرا ہوا', 'ډک شوی'],
        ['Filled regions', 'بھرے ہوئے خطے', 'ډکې شوې سیمې'],
        ['Font', 'رسم الخط', 'لیکبڼه'],
        ['Gridline', 'جالی کی لکیر', 'د جال کرښه'],
        ['Labels', 'ناموں کی علامتیں', 'نومپاڼې'],
        ['Label directions', 'ناموں کی سمتیں', 'د نومپاڼو لوري'],
        ['Label font', 'ناموں کا رسم الخط', 'د نومپاڼو لیکبڼه'],
        ['Legend', 'علامتوں کی وضاحت', 'د نښو تشریح'],
        ['Legend style', 'علامتوں کی وضاحت کا انداز', 'د نښو د تشریح بڼه'],
        ['Line style', 'لکیر کا انداز', 'د کرښې بڼه'],
        ['Num points', 'نقاط کی تعداد', 'د نقطو شمېر'],
        ['Resolution', 'وضاحت کی سطح', 'د ښودنې تفکیک'],
        ['Sample', 'نمونہ', 'نمونه'],
        ['Scaling', 'پیمانہ مقرر کرنا', 'د مقیاس ټاکل'],
        ['Size', 'حجم', 'اندازه'],
        ['Smart view', 'ذہین منظر', 'ځیرک لید'],
        ['Style', 'انداز', 'بڼه'],
        ['Symbol', 'علامت', 'نښه'],
        ['Symbol size', 'علامت کا حجم', 'د نښې اندازه'],
        ['Thickness', 'موٹائی', 'پنډوالی'],
        ['Tick marks', 'پیمانے کے نشان', 'د مقیاس نښې'],
        ['Title', 'عنوان', 'سرلیک'],
        ['Title font', 'عنوان کا رسم الخط', 'د سرلیک لیکبڼه'],
        ['Transparency', 'شفافیت', 'روڼتیا'],
        ['Use units', 'اکائیاں استعمال کرنا', 'د واحدونو کارول'],
        ['View', 'منظر', 'لید']
    ]) passage(en, ur, ps);

    sentences([
        ['When we are plotting a function over an interval.', 'جب ہم کسی وقفے پر تفاعل کا گراف بناتے ہیں۔', 'کله چې موږ په یوه واټن کې د تابع ګراف رسموو.'],
        ['The interval is sampled at a number of points, controlled by “sample” and “numpoints”.', 'وقفے کے کئی نقاط پر نمونے لیے جاتے ہیں، جنہیں “sample” اور “numpoints” قابو کرتے ہیں۔', 'د واټن په څو نقطو کې نمونې اخیستل کېږي چې “sample” او “numpoints” یې کنټرولوي.'],
        ['Adaptive plotting, where necessary, subdivides these intervals to attempt to get a better representation of the function.', 'حسبِ ضرورت موافقت کے ساتھ گراف سازی، جہاں ضرورت ہو، ان وقفوں کو مزید تقسیم کرتی ہے تاکہ تفاعل کی بہتر نمائندگی حاصل ہو سکے۔', 'د اړتیا له مخې سمون لرونکی رسمول، چېرې چې اړتیا وي، دا واټنونه نور هم وېشي څو د تابع ښه انځور ترلاسه کړي.'],
        ['This option is subsampling can be turned off by setting the “adaptive” option to false.', 'نمونہ گیری کی اس مزید تقسیم کو “adaptive” کا اختیار false مقرر کر کے بند کیا جا سکتا ہے۔', 'د نمونې اخیستنې دا فرعي وېش د “adaptive” غوراوي په false ټاکلو سره بندېدای شي.'],
        ['By default, this option is true and intervals are subdivided at most six times in trying to improve the plot.', 'پہلے سے مقرر حالت میں یہ اختیار true ہوتا ہے اور گراف کو بہتر بنانے کی کوشش میں وقفوں کو زیادہ سے زیادہ چھ مرتبہ مزید تقسیم کیا جاتا ہے۔', 'په اصلي ټاکنه کې دا غوراوی true دی او د ګراف د ښه کولو په هڅه کې واټنونه تر ډېره شپږ ځله نور هم وېشل کېږي.'],
        ['By setting this option to a non-negative integer, we can control the maximum number of six times the subintervals are divided.', 'اس اختیار کو غیر منفی صحیح عدد مقرر کر کے ہم اس زیادہ سے زیادہ تعداد کو قابو کر سکتے ہیں جس کے تحت ذیلی وقفوں کو چھ مرتبہ تقسیم کیا جاتا ہے۔', 'د دې غوراوي د غیر منفي صحیح عدد په ټاکلو سره موږ هغه اعظمي شمېر کنټرولولی شو چې له مخې یې فرعي واټنونه شپږ ځله وېشل کېږي.']
    ]);
    sentences([
        ['The annotation option allows us to add descriptive text to a 2-D curve or point plot.', 'annotation کا اختیار ہمیں دو بُعدی منحنی یا نقطی گراف میں وضاحتی متن شامل کرنے دیتا ہے۔', 'د annotation غوراوی موږ ته اجازه راکوي چې دوه بعدي منحني یا نقطوي ګراف ته تشریحي متن ورزیات کړو.'],
        ['The term "point plot" in this context means a collection of points that are treated as a single plot element, such that created by the “dataplot” command.', 'اس سیاق میں “point plot” سے مراد نقاط کا ایسا مجموعہ ہے جسے گراف کا ایک جزو سمجھا جائے، جیسے “dataplot” کے حکم سے بنایا گیا مجموعہ۔', 'په دې سیاق کې د “point plot” اصطلاح د نقطو داسې ټولګې ته ویل کېږي چې د ګراف یو عنصر ګڼل کېږي، لکه هغه چې د “dataplot” امر یې جوړوي.'],
        ['The text which is included mathematical expressions, appears when the pointer hovers over the plot element to which it is associated.', 'یہ متن، جس میں ریاضیاتی عبارتیں بھی شامل ہو سکتی ہیں، اس وقت ظاہر ہوتا ہے جب اشارہ گر گراف کے اس جزو پر ٹھہرتا ہے جس سے متن وابستہ ہے۔', 'دا متن چې ریاضيکي عبارتونه هم پکې شامل وي، هغه وخت څرګندېږي چې نښه ګر د ګراف پر هغه عنصر ودرېږي چې متن ورسره تړلی دی.'],
        ['An annotation for a curve or a point, which appears whenever the pointer is placed over the element.', 'منحنی یا نقطے کا توضیحی نوٹ ہر بار اس وقت ظاہر ہوتا ہے جب اشارہ گر اس جزو پر رکھا جاتا ہے۔', 'د منحني یا نقطې تشریحي یادښت هر هغه وخت څرګندېږي چې نښه ګر پر هغه عنصر کېښودل شي.']
    ]);
    passage('Specifies the type of axes, one of: boxed, frame, none, or normal.', 'محوروں کی قسم مقرر کرتا ہے، جو boxed، frame، none یا normal میں سے ایک ہوتی ہے۔', 'د محورونو ډول ټاکي چې له boxed، frame، none یا normal څخه یو وي.');
    sentences([
        ['Font for the labels on the tick marks of the axes, specified in the same manner as font.', 'محوروں کے پیمانے کے نشانوں پر ناموں کا رسم الخط، جو font کی طرح مقرر کیا جاتا ہے۔', 'د محورونو د مقیاس پر نښو د نومپاڼو لیکبڼه، چې د font په شان ټاکل کېږي.'],
        ['This option overrides values specified for the font.', 'یہ اختیار font کے لیے مقرر کردہ قیمتوں پر فوقیت رکھتا ہے۔', 'دا غوراوی د font لپاره پر ټاکل شویو ارزښتونو لومړیتوب لري.']
    ]);
    sentences([
        ['The axis and axis[dir] options allows us to provide information about one or more axes to plotting commands such as “plot” and “plot3d”.', 'axis اور axis[dir] کے اختیارات ہمیں ایک یا زیادہ محوروں کی معلومات “plot” اور “plot3d” جیسے گراف سازی کے احکامات کو فراہم کرنے دیتے ہیں۔', 'د axis او axis[dir] غوراوي موږ ته اجازه راکوي چې د یوه یا څو محورونو معلومات د “plot” او “plot3d” په څېر د رسمولو امرونو ته ورکړو.'],
        ['For example, the axis color, locations of tick marks and gridlines, and use of logarithmic scales.', 'مثلاً محور کا رنگ، پیمانے کے نشانوں اور جالی کی لکیروں کے مقامات، اور لوگارتھمی پیمانوں کا استعمال۔', 'د بېلګې په توګه، د محور رنګ، د مقیاس د نښو او د جال د کرښو ځایونه، او د لوګاریتمي مقیاسونو کارول.']
    ]);
    sentences([
        ['With the axis = t option, the information provided in t is applied to all the axes.', 'axis = t کے اختیار کے ساتھ t میں دی گئی معلومات تمام محوروں پر لاگو ہوتی ہیں۔', 'د axis = t غوراوي سره په t کې ورکړل شوي معلومات پر ټولو محورونو پلي کېږي.'],
        ['With the axis[dir] = t option, t is used for only the direction(s) specified in dir (direction), which can be the single value at (x-axis), (y-axis) or (z-axis), or a sequence of two of these values.', 'axis[dir] = t کے اختیار کے ساتھ t صرف dir (سمت) میں مقرر کردہ سمت یا سمتوں کے لیے استعمال ہوتا ہے؛ یہ (x-axis)، (y-axis) یا (z-axis) کی ایک قیمت، یا ان میں سے دو قیمتوں کا سلسلہ ہو سکتا ہے۔', 'د axis[dir] = t غوراوي سره t یوازې د هغو لوریو لپاره کارول کېږي چې په dir (لوري) کې ټاکل شوي وي؛ دا د (x-axis)، (y-axis) یا (z-axis) یوه ارزښت یا له دې ارزښتونو څخه د دوو ترتیب کېدای شي.'],
        ['Multiple axis[dir] options, with different values of dir, can be used to specify different information for different axes.', 'dir کی مختلف قیمتوں کے ساتھ axis[dir] کے متعدد اختیارات استعمال کر کے مختلف محوروں کے لیے مختلف معلومات مقرر کی جا سکتی ہیں۔', 'د dir له بېلابېلو ارزښتونو سره د axis[dir] ګڼ غوراوي کارول کېدای شي څو د بېلابېلو محورونو لپاره بېلابېل معلومات وټاکي.'],
        ['The commands for 2-D plotting do not accept the axis[3] option.', 'دو بُعدی گراف سازی کے احکامات axis[3] کا اختیار قبول نہیں کرتے۔', 'د دوه بعدي ګراف رسمولو امرونه د axis[3] غوراوی نه مني.']
    ]);
    sentences([
        ['The axis information is given by t.', 'محور کی معلومات t کے ذریعے دی جاتی ہیں۔', 'د محور معلومات د t له لارې ورکول کېږي.'],
        ['The list t may contain one or more of the sub options.', 'فہرست t میں ایک یا زیادہ ذیلی اختیارات شامل ہو سکتے ہیں۔', 'د t لېست یو یا څو فرعي غوراوي لرلی شي.']
    ]);
    sentences([
        ['Normally a coordinate system is used to display of the axes.', 'عام طور پر محور دکھانے کے لیے ایک نظامِ محددات استعمال ہوتا ہے۔', 'عموماً د محورونو د ښودلو لپاره د مختصاتو یو سیستم کارول کېږي.'],
        ['The value t can be either cartesian of polar.', 't کی قیمت cartesian یا polar ہو سکتی ہے۔', 'د t ارزښت cartesian یا polar کېدای شي.'],
        ['Cartesian axes are displayed by default.', 'پہلے سے مقرر حالت میں کارتیسی محور دکھائے جاتے ہیں۔', 'په اصلي ټاکنه کې کارتیزي محورونه ښودل کېږي.'],
        ['If t is polar, then radial and angular axes are generated.', 'اگر t کی قیمت polar ہو تو شعاعی اور زاویائی محور بنائے جاتے ہیں۔', 'که t د polar ارزښت ولري، نو شعاعي او زاویوي محورونه جوړېږي.'],
        ['This option is used together with the cords = polar option.', 'یہ اختیار cords = polar کے اختیار کے ساتھ استعمال ہوتا ہے۔', 'دا غوراوی د cords = polar له غوراوي سره یو ځای کارول کېږي.']
    ]);
    sentences([
        ['This option is only available in the Standard interface.', 'یہ اختیار صرف Standard رابطے میں دستیاب ہے۔', 'دا غوراوی یوازې په Standard رابط کې شته.'],
        ['In the Classic interface, the coordinates are always Cartesian.', 'Classic رابطے میں محددات ہمیشہ کارتیسی ہوتے ہیں۔', 'په Classic رابط کې مختصات تل کارتیزي وي.']
    ]);
    sentences([
        ['The value of t can be the name of an image file, as a string, a name, a datatype = float, Array as used with the Image Tools package, or a color.', 't کی قیمت کسی تصویری فائل کا نام بطور متنی سلسلہ، ایک نام، datatype = float والا Array جیسا کہ Image Tools پیکیج کے ساتھ استعمال ہوتا ہے، یا ایک رنگ ہو سکتی ہے۔', 'د t ارزښت د انځور د فایل نوم د متني لړۍ په بڼه، یو نوم، د datatype = float لرونکی Array لکه د Image Tools له کڅوړې سره چې کارول کېږي، یا یو رنګ کېدای شي.'],
        ['A plot can have a single background image or color.', 'ایک گراف میں پس منظر کی ایک تصویر یا ایک رنگ ہو سکتا ہے۔', 'یو ګراف د شالید یو انځور یا یو رنګ لرلی شي.']
    ]);
    sentences([
        ['If the size option is omitted then the dimensions of the plot can be determined by the dimensions of the image.', 'اگر size کا اختیار نہ دیا جائے تو گراف کی لمبائی اور چوڑائی تصویر کی ابعاد سے متعین کی جا سکتی ہیں۔', 'که د size غوراوی ورنه کړل شي، د ګراف ابعاد د انځور د ابعادو له مخې ټاکل کېدای شي.'],
        ['If the size option is provided then the image is displayed with the dimensions of the plot.', 'اگر size کا اختیار دیا جائے تو تصویر گراف کی ابعاد کے مطابق دکھائی جاتی ہے۔', 'که د size غوراوی ورکړل شي، انځور د ګراف په ابعادو ښودل کېږي.']
    ]);
    sentences([
        ['A color may be given as a color tools [color] object or as a color string.', 'رنگ color tools [color] آبجیکٹ یا رنگ کے متنی سلسلے کی صورت میں دیا جا سکتا ہے۔', 'رنګ د color tools [color] څیز یا د رنګ د متني لړۍ په بڼه ورکول کېدای شي.'],
        ['If t is a string, then it is first interpreted as a filename.', 'اگر t متنی سلسلہ ہو تو پہلے اسے فائل کا نام سمجھا جاتا ہے۔', 'که t متني لړۍ وي، لومړی د فایل نوم ګڼل کېږي.'],
        ['If the file t does not exist, it is then assumed to be a color.', 'اگر t نام کی فائل موجود نہ ہو تو اسے رنگ تصور کیا جاتا ہے۔', 'که د t په نوم فایل موجود نه وي، بیا رنګ ګڼل کېږي.']
    ]);
    sentences([
        ['The value c can be an arbitrary expression.', 'c کی قیمت کوئی بھی عبارت ہو سکتی ہے۔', 'د c ارزښت هر ډول عبارت کېدای شي.'],
        ['It can also be a list consisting of the caption followed by the font option.', 'یہ ایسی فہرست بھی ہو سکتی ہے جس میں توضیحی عنوان کے بعد font کا اختیار ہو۔', 'دا داسې لېست هم کېدای شي چې تشریحي سرلیک او ورپسې د font غوراوی ولري.'],
        ['The default is no caption.', 'پہلے سے مقرر حالت میں کوئی توضیحی عنوان نہیں ہوتا۔', 'په اصلي ټاکنه کې تشریحي سرلیک نشته.']
    ]);
    sentences([
        ['This option defines the font for the plot caption, specified in the same manner as font.', 'یہ اختیار گراف کے توضیحی عنوان کا رسم الخط متعین کرتا ہے، جو font کی طرح مقرر کیا جاتا ہے۔', 'دا غوراوی د ګراف د تشریحي سرلیک لیکبڼه ټاکي، چې د font په شان مشخصه کېږي.'],
        ['This option over-rides values specified for font.', 'یہ اختیار font کے لیے مقرر کردہ قیمتوں پر فوقیت رکھتا ہے۔', 'دا غوراوی د font لپاره پر ټاکل شویو ارزښتونو لومړیتوب لري.']
    ]);
    passage('This allows us to specify the color of the curves to be plotted.', 'یہ ہمیں ان منحنیات کا رنگ مقرر کرنے دیتا ہے جن کا گراف بنانا ہو۔', 'دا موږ ته اجازه راکوي چې د رسمېدونکو منحنیو رنګ وټاکو.');
    passage('This allows us to apply a color scheme to a surface or set of points.', 'یہ ہمیں کسی سطح یا نقاط کے مجموعے پر رنگوں کی ترتیب لاگو کرنے دیتا ہے۔', 'دا موږ ته اجازه راکوي چې پر یوې سطحې یا د نقطو پر یوې ټولګې د رنګونو ترتیب پلي کړو.');
    sentences([
        ['This option is used when the axes coordinates option has the value polar.', 'یہ اختیار اس وقت استعمال ہوتا ہے جب محوروں کے محددات کے اختیار کی قیمت polar ہو۔', 'دا غوراوی هغه وخت کارول کېږي چې د محورونو د مختصاتو د غوراوي ارزښت polar وي.'],
        ['When that is the case, then r₁,...,r₂, specifies the radial range that is to be displayed and a₁,...,a₂, specifies the angular range.', 'اس صورت میں r₁,...,r₂ دکھائی جانے والی شعاعی حد اور a₁,...,a₂ زاویائی حد مقرر کرتے ہیں۔', 'په دې حالت کې r₁,...,r₂ د ښودلو شعاعي ساحه او a₁,...,a₂ زاویوي ساحه ټاکي.']
    ]);
    sentences([
        ['The value cname is one of the choices listed on the coords help page.', 'cname کی قیمت coords کے مدد کے صفحے پر درج اختیارات میں سے ایک ہوتی ہے۔', 'د cname ارزښت د coords د مرستې پر پاڼه له لېست شویو غوراویو څخه یو وي.'],
        ['The cartesian axes are displayed by default.', 'پہلے سے مقرر حالت میں کارتیسی محور دکھائے جاتے ہیں۔', 'په اصلي ټاکنه کې کارتیزي محورونه ښودل کېږي.'],
        ['To generate polar axes with polar plots, we use axiscoordinates = polar option along with the coords = polar option.', 'قطبی گرافوں کے ساتھ قطبی محور بنانے کے لیے ہم coords = polar کے ساتھ axiscoordinates = polar کا اختیار استعمال کرتے ہیں۔', 'له قطبي ګرافونو سره د قطبي محورونو د جوړولو لپاره د coords = polar له غوراوي سره د axiscoordinates = polar غوراوی کاروو.']
    ]);
    passage('This allows us for detection of discontinuities.', 'یہ ہمیں عدم اتصال کے مقامات معلوم کرنے دیتا ہے۔', 'دا موږ ته د ناپیوستونونو د موندلو اجازه راکوي.');
    sentences([
        ['If the filled option is set to true, the area between the curve and the x-axis is given by a solid color.', 'اگر filled کا اختیار true مقرر کیا جائے تو منحنی اور x محور کے درمیان رقبہ ایک ٹھوس رنگ سے بھر دیا جاتا ہے۔', 'که د filled غوراوی true وټاکل شي، د منحني او x محور ترمنځ ساحه په یوه یوشان رنګ ډکېږي.'],
        ['The value of the filled option can also be a list containing one or more sub options (color, style or transparency).', 'filled کے اختیار کی قیمت ایسی فہرست بھی ہو سکتی ہے جس میں ایک یا زیادہ ذیلی اختیارات (color، style یا transparency) شامل ہوں۔', 'د filled غوراوي ارزښت داسې لېست هم کېدای شي چې یو یا څو فرعي غوراوي (color، style یا transparency) ولري.'],
        ['These options are applied only to the filled area, and not to the original curve itself.', 'یہ اختیارات صرف بھرے ہوئے رقبے پر لاگو ہوتے ہیں، اصل منحنی پر نہیں۔', 'دا غوراوي یوازې پر ډکه شوې ساحه پلي کېږي، پر اصلي منحني نه پلي کېږي.'],
        ['This option does not work with non-cartesian coordinate systems.', 'یہ اختیار غیر کارتیسی نظام ہائے محددات کے ساتھ کام نہیں کرتا۔', 'دا غوراوی د مختصاتو له غیر کارتیزي سیستمونو سره کار نه کوي.']
    ]);
    sentences([
        ['If the filledregions option is set to true, the regions defined by the curves are filled with different colors.', 'اگر filledregions کا اختیار true مقرر کیا جائے تو منحنیات سے متعین خطے مختلف رنگوں سے بھر دیے جاتے ہیں۔', 'که د filledregions غوراوی true وټاکل شي، هغه سیمې چې منحني یې ټاکي په بېلابېلو رنګونو ډکېږي.'],
        ['This option is valid only by using the following commands:', 'یہ اختیار صرف درج ذیل احکامات کے استعمال کے ساتھ مؤثر ہوتا ہے:', 'دا غوراوی یوازې د لاندې امرونو په کارولو معتبر دی:']
    ]);
    sentences([
        ['“contourplot”, “implicitplot” and “listcontplot”.', '“contourplot”، “implicitplot” اور “listcontplot”۔', '“contourplot”، “implicitplot” او “listcontplot”.'],
        ['This option does not work with non-Cartesian coordinate systems.', 'یہ اختیار غیر کارتیسی نظام ہائے محددات کے ساتھ کام نہیں کرتا۔', 'دا غوراوی د مختصاتو له غیر کارتیزي سیستمونو سره کار نه کوي.']
    ]);

    sentences([
        ['This option defines the font for the plot title, caption, axis tick mark labels, and axis labels if no values have been specified for these for font, captionfont, label font, or title font options.', 'اگر font، captionfont، label font یا title font کے اختیارات میں ان کے لیے قیمتیں مقرر نہ کی گئی ہوں تو یہ اختیار گراف کے عنوان، توضیحی عنوان، محور کے پیمانے کے نشانوں کے ناموں اور محوروں کے ناموں کا رسم الخط متعین کرتا ہے۔', 'که د font، captionfont، label font یا title font په غوراویو کې د دوی لپاره ارزښتونه نه وي ټاکل شوي، دا غوراوی د ګراف د سرلیک، تشریحي سرلیک، د محور د مقیاس د نښو نومپاڼو او د محورونو د نومپاڼو لیکبڼه ټاکي.'],
        ['The value l is a list of the form [family, style, size].', 'l کی قیمت [family, style, size] کی صورت میں ایک فہرست ہے۔', 'د l ارزښت د [family, style, size] په بڼه یو لېست دی.']
    ]);
    sentences([
        ['The value of family can be one of Times, Courier, Helvetica, or Symbol.', 'family کی قیمت Times، Courier، Helvetica یا Symbol میں سے ایک ہو سکتی ہے۔', 'د family ارزښت له Times، Courier، Helvetica یا Symbol څخه یو کېدای شي.'],
        ['It can also be any font name supported by your system, for example, Times New Roman and Calibri in Windows.', 'یہ آپ کے نظام میں دستیاب کسی بھی رسم الخط کا نام بھی ہو سکتا ہے، مثلاً Windows میں Times New Roman اور Calibri۔', 'دا ستاسو د سیستم له خوا منل شوې هرې لیکبڼې نوم هم کېدای شي، لکه په Windows کې Times New Roman او Calibri.'],
        ['The first letter of the family name must be capitalized.', 'family کے نام کا پہلا حرف بڑا انگریزی حرف ہونا چاہیے۔', 'د family د نوم لومړی توری باید د انګلیسي لوی توری وي.']
    ]);
    sentences([
        ['The value of style can be omitted or one of roman, bold, italic, bold italic, oblique, or bold oblique.', 'style کی قیمت چھوڑی جا سکتی ہے یا roman، bold، italic، bold italic، oblique یا bold oblique میں سے ایک ہو سکتی ہے۔', 'د style ارزښت پرېښودل کېدای شي یا له roman، bold، italic، bold italic، oblique یا bold oblique څخه یو کېدای شي.'],
        ['The Symbol family does not accept a style option.', 'Symbol خاندان style کا اختیار قبول نہیں کرتا۔', 'د Symbol کورنۍ د style غوراوی نه مني.'],
        ['The final value, size, is the point size to be used.', 'آخری قیمت size، استعمال ہونے والا پوائنٹ سائز ہے۔', 'وروستی ارزښت، size، هغه پواینټي اندازه ده چې کارول کېږي.']
    ]);
    passage('When gridlines = true or gridlines is provided, default gridlines are drawn. The default is gridlines = false.If the axis option is also provided and contains a gridlines sub option, then that option over rides this gridlines option.', 'جب gridlines = true یا gridlines دیا جائے تو پہلے سے مقرر جالی کی لکیریں کھینچی جاتی ہیں۔ پہلے سے مقرر حالت gridlines = false ہے۔ اگر axis کا اختیار بھی دیا جائے اور اس میں gridlines کا ذیلی اختیار ہو تو وہ ذیلی اختیار اس gridlines کے اختیار پر فوقیت رکھتا ہے۔', 'کله چې gridlines = true یا gridlines ورکړل شي، د جال اصلي ټاکل شوې کرښې رسمېږي. اصلي ټاکنه gridlines = false ده. که د axis غوراوی هم ورکړل شي او د gridlines فرعي غوراوی ولري، نو هغه فرعي غوراوی د دې gridlines پر غوراوي لومړیتوب لري.');
    sentences([
        ['This option specifies labels for the axes.', 'یہ اختیار محوروں کے نام مقرر کرتا ہے۔', 'دا غوراوی د محورونو نومپاڼې ټاکي.'],
        ['By default labels are the names of the variables in the original function to be plotted, if these are available otherwise, no labels will be used.', 'پہلے سے مقرر حالت میں نام اسی اصل تفاعل کے متغیرات کے نام ہوتے ہیں جس کا گراف بنایا جانا ہے، اگر یہ دستیاب ہوں؛ ورنہ کوئی نام استعمال نہیں کیے جائیں گے۔', 'په اصلي ټاکنه کې نومپاڼې د رسمېدونکې اصلي تابع د متحولونو نومونه وي، که دا نومونه موجود وي؛ که نه، نومپاڼې نه کارول کېږي.']
    ]);
    sentences([
        ['This option specifies the direction in which labels are printed along the axes.', 'یہ اختیار وہ سمت مقرر کرتا ہے جس میں محوروں کے ساتھ نام لکھے جاتے ہیں۔', 'دا غوراوی هغه لوری ټاکي چې نومپاڼې د محورونو په اوږدو کې پکې لیکل کېږي.'],
        ['The values of x and y should be horizontal or vertical.', 'x اور y کی قیمتیں horizontal یا vertical ہونی چاہییں۔', 'د x او y ارزښتونه باید horizontal یا vertical وي.'],
        ['The default direction of any labels is horizontal.', 'تمام ناموں کی پہلے سے مقرر سمت افقی ہوتی ہے۔', 'د هرې نومپاڼې اصلي ټاکل شوی لوری افقي دی.']
    ]);
    sentences([
        ['The font of the labels on the axes of the plot, specified in the same manner as font.', 'گراف کے محوروں پر ناموں کا رسم الخط، جو font کی طرح مقرر کیا جاتا ہے۔', 'د ګراف پر محورونو د نومپاڼو لیکبڼه، چې د font په شان ټاکل کېږي.'],
        ['This option overrides values specified for font.', 'یہ اختیار font کے لیے مقرر کردہ قیمتوں پر فوقیت رکھتا ہے۔', 'دا غوراوی د font لپاره پر ټاکل شویو ارزښتونو لومړیتوب لري.']
    ]);
    passage('If the plot command is being used to plot multiple curves, then s can be a list containing a legend entry for each curve.', 'اگر plot کا حکم متعدد منحنیات بنانے کے لیے استعمال ہو رہا ہو تو s ایسی فہرست ہو سکتی ہے جس میں ہر منحنی کے لیے علامت کی وضاحت کا ایک اندراج ہو۔', 'که د plot امر د څو منحنیو د رسمولو لپاره کارول کېږي، نو s داسې لېست کېدای شي چې د هرې منحني لپاره د نښو د تشریح یو توکی ولري.');
    sentences([
        ['Since the value s is a list consisting of one or more sub options.', 'چونکہ s کی قیمت ایک یا زیادہ ذیلی اختیارات پر مشتمل فہرست ہوتی ہے۔', 'ځکه چې د s ارزښت یو لېست دی چې یو یا څو فرعي غوراوي لري.'],
        ['The sub options are available for the legendstyle option include font = f and location = loc.', 'legendstyle کے اختیار کے لیے دستیاب ذیلی اختیارات میں font = f اور location = loc شامل ہیں۔', 'د legendstyle غوراوي لپاره په شته فرعي غوراویو کې font = f او location = loc شامل دي.'],
        ['The location = loc sub option allows us top, bottom, right and left for loc.', 'location = loc کا ذیلی اختیار loc کے لیے top، bottom، right اور left منتخب کرنے دیتا ہے۔', 'د location = loc فرعي غوراوی موږ ته د loc لپاره top، bottom، right او left ټاکلو اجازه راکوي.']
    ]);
    sentences([
        ['It controls the line style of curves.', 'یہ منحنیات کی لکیر کا انداز قابو کرتا ہے۔', 'دا د منحنیو د کرښې بڼه کنټرولوي.'],
        ['The line style value t can be one of the following names: solid, dot, dash, dash dot, long dash, space dash, or space dot.', 'لکیر کے انداز کی قیمت t درج ذیل ناموں میں سے ایک ہو سکتی ہے: solid، dot، dash، dash dot، long dash، space dash یا space dot۔', 'د کرښې د بڼې ارزښت t له لاندې نومونو څخه یو کېدای شي: solid، dot، dash، dash dot، long dash، space dash یا space dot.'],
        ['The default value of t is solid.', 't کی پہلے سے مقرر قیمت solid ہے۔', 'د t اصلي ټاکل شوی ارزښت solid دی.'],
        ['The value t can also be an integer from 1 to 7, where each integer represents a line style, as given in the order above.', 't کی قیمت 1 سے 7 تک کوئی صحیح عدد بھی ہو سکتی ہے، جہاں ہر صحیح عدد اوپر دی گئی ترتیب کے مطابق لکیر کے ایک انداز کی نمائندگی کرتا ہے۔', 'د t ارزښت له 1 څخه تر 7 پورې صحیح عدد هم کېدای شي؛ هر صحیح عدد د پورته ترتیب له مخې د کرښې د یوې بڼې استازیتوب کوي.']
    ]);
    sentences([
        ['Specifies the minimum number of points to be generated.', 'بنائے جانے والے نقاط کی کم سے کم تعداد مقرر کرتا ہے۔', 'د جوړېدونکو نقطو لږ تر لږه شمېر ټاکي.'],
        ['The default number of points is 200.', 'نقاط کی پہلے سے مقرر تعداد 200 ہے۔', 'د نقطو اصلي ټاکل شوی شمېر 200 دی.']
    ]);
    passage('Plot employs an adaptive plotting scheme which automatically does more work where the function values do not lie close to a straight line.', 'Plot گراف سازی کی حسبِ ضرورت موافقت کرنے والی ترتیب استعمال کرتا ہے، جو ان مقامات پر خودکار طور پر زیادہ کام کرتی ہے جہاں تفاعل کی قیمتیں سیدھی لکیر کے قریب نہیں ہوتیں۔', 'Plot د اړتیا له مخې سمون لرونکې د رسمولو تګلاره کاروي چې په هغو ځایونو کې په خپله ډېر کار کوي چې د تابع ارزښتونه یوې نېغې کرښې ته نږدې نه وي.');
    sentences([
        ['This sets the horizontal display resolution of the device in pixels.', 'یہ آلے کی افقی نمائش کی وضاحت پکسلوں میں مقرر کرتا ہے۔', 'دا په پکسلونو کې د وسیلې د افقي ښودنې تفکیک ټاکي.'],
        ['The default resolution is n=800.', 'وضاحت کی پہلے سے مقرر سطح n=800 ہے۔', 'اصلي ټاکل شوی تفکیک n=800 دی.']
    ]);
    passage('The value of n is used to determine when the adaptive plotting scheme terminates.', 'n کی قیمت اس بات کا تعین کرنے کے لیے استعمال ہوتی ہے کہ حسبِ ضرورت موافقت والی گراف سازی کی ترتیب کب ختم ہو گی۔', 'د n ارزښت د دې د ټاکلو لپاره کارول کېږي چې د اړتیا له مخې سمون لرونکې د رسمولو تګلاره کله پای ته رسېږي.');
    sentences([
        ['A list of numerical values which is to be used for the initial sampling of the function.', 'عددی قیمتوں کی ایک فہرست، جو تفاعل کی ابتدائی نمونہ گیری کے لیے استعمال ہونی ہے۔', 'د عددي ارزښتونو یو لېست چې د تابع د لومړنۍ نمونې اخیستنې لپاره کارول کېږي.'],
        ['Normally, the function is sampled at additional points.', 'عام طور پر تفاعل کے اضافی نقاط پر بھی نمونے لیے جاتے ہیں۔', 'عموماً د تابع په اضافي نقطو کې هم نمونې اخیستل کېږي.'],
        ['To restrict sampling to only these values we include the adaptive = false option.', 'نمونہ گیری کو صرف ان قیمتوں تک محدود رکھنے کے لیے ہم adaptive = false کا اختیار شامل کرتے ہیں۔', 'یوازې دغو ارزښتونو ته د نمونې اخیستنې د محدودولو لپاره د adaptive = false غوراوی ورزیاتوو.']
    ]);
    sentences([
        ['It controls scaling of the graph.', 'یہ گراف کا پیمانہ قابو کرتا ہے۔', 'دا د ګراف مقیاس کنټرولوي.'],
        ['The value of s is unconstrained by default, which means the plot is scaled to fit the plot window.', 's کی پہلے سے مقرر قیمت unconstrained ہے، جس کا مطلب ہے کہ گراف کا پیمانہ اس کی ونڈو میں سما جانے کے مطابق مقرر ہوتا ہے۔', 'د s اصلي ټاکل شوی ارزښت unconstrained دی، یعنې د ګراف مقیاس داسې ټاکل کېږي چې د ګراف په کړکۍ کې ځای شي.'],
        ['The constrained value causes all axes to use the same scale.', 'constrained کی قیمت تمام محوروں کو ایک ہی پیمانہ استعمال کرنے کا پابند کرتی ہے۔', 'د constrained ارزښت ټول محورونه اړ کوي چې یو شان مقیاس وکاروي.']
    ]);
    sentences([
        ['We use this to specify the size of the plot window.', 'ہم اسے گراف کی ونڈو کا حجم مقرر کرنے کے لیے استعمال کرتے ہیں۔', 'موږ دا د ګراف د کړکۍ د اندازې د ټاکلو لپاره کاروو.'],
        ['We can set the size of the plot window by specifying the number of pixels, a proportion of worksheet width, or a ratio, such as a square, the golden ratio, or a custom ratio.', 'ہم پکسلوں کی تعداد، ورک شیٹ کی چوڑائی کا کوئی تناسب، یا مربع، سنہری نسبت یا اپنی مقرر کردہ نسبت جیسی کوئی نسبت دے کر گراف کی ونڈو کا حجم مقرر کر سکتے ہیں۔', 'موږ د پکسلونو د شمېر، د کاري پاڼې د پلنوالي د یوې برخې، یا د مربع، طلایي نسبت یا خپل ټاکلي نسبت په څېر د یوه نسبت په ټاکلو سره د ګراف د کړکۍ اندازه ټاکلی شو.']
    ]);
    sentences([
        ['This is used to determine an appropriate view of the plot data.', 'یہ گراف کے ڈیٹا کا مناسب منظر متعین کرنے کے لیے استعمال ہوتا ہے۔', 'دا د ګراف د معلوماتو د مناسب لید د ټاکلو لپاره کارول کېږي.'],
        ['The plot command generates data based on the range provided by us or on a default range if this is not provided.', 'plot کا حکم ہماری دی ہوئی حد کی بنیاد پر ڈیٹا بناتا ہے، یا اگر حد نہ دی گئی ہو تو پہلے سے مقرر حد استعمال کرتا ہے۔', 'د plot امر زموږ د ورکړل شوې ساحې پر بنسټ معلومات جوړوي، یا که ساحه نه وي ورکړل شوې، اصلي ټاکل شوې ساحه کاروي.'],
        ['When the smartview = true option is provided, a view that tries to present the important regions of the data is computed.', 'جب smartview = true کا اختیار دیا جائے تو ایسا منظر شمار کیا جاتا ہے جو ڈیٹا کے اہم حصوں کو پیش کرنے کی کوشش کرتا ہے۔', 'کله چې د smartview = true غوراوی ورکړل شي، داسې لید محاسبه کېږي چې د معلوماتو د مهمو سیمو د ښودلو هڅه کوي.'],
        ['To show all data computed, use the smartview = false option.', 'تمام شمار شدہ ڈیٹا دکھانے کے لیے smartview = false کا اختیار استعمال کریں۔', 'د ټولو محاسبه شویو معلوماتو د ښودلو لپاره د smartview = false غوراوی وکاروئ.'],
        ['The default setting of smartview is true.', 'smartview کی پہلے سے مقرر ترتیب true ہے۔', 'د smartview اصلي ټاکنه true ده.'],
        ['This option is available for the plot command and only applies to curves not points, polygons or text.', 'یہ اختیار plot کے حکم کے لیے دستیاب ہے اور صرف منحنیات پر لاگو ہوتا ہے، نقاط، کثیرالاضلاع یا متن پر نہیں۔', 'دا غوراوی د plot امر لپاره شته او یوازې پر منحنیو پلي کېږي، پر نقطو، څو ضلعیو یا متن نه پلي کېږي.']
    ]);
    sentences([
        ['The plot style should be one of line, point, point line, polygon, or polygon outline.', 'گراف کا انداز line، point، point line، polygon یا polygon outline میں سے ایک ہونا چاہیے۔', 'د ګراف بڼه باید له line، point، point line، polygon یا polygon outline څخه یوه وي.'],
        ['The names in parentheses are aliases for the option values.', 'قوسین میں دیے گئے نام اختیار کی قیمتوں کے متبادل نام ہیں۔', 'په قوسونو کې نومونه د غوراوي د ارزښتونو بدیل نومونه دي.'],
        ['The styles line, polygon, and polygon outline all draw curves by interpolating between the sample points.', 'line، polygon اور polygon outline کے تمام انداز نمونہ جاتی نقاط کے درمیان میانی قیمتیں نکال کر منحنیات بناتے ہیں۔', 'د line، polygon او polygon outline ټولې بڼې د نمونې د نقطو ترمنځ د منځنیو ارزښتونو په موندلو منحني رسموي.'],
        ['The point style results in a plot of the points only.', 'point کے انداز میں صرف نقاط کا گراف بنتا ہے۔', 'د point بڼه یوازې د نقطو ګراف جوړوي.'],
        ['The default style, polygon outline, draws any polygons as filled with an outline.', 'پہلے سے مقرر انداز polygon outline کسی بھی کثیرالاضلاع کو بھرا ہوا اور بیرونی حد کے ساتھ بناتا ہے۔', 'اصلي ټاکل شوې بڼه، polygon outline، هر څو ضلعي په ډکه بڼه او له پولې سره رسموي.'],
        ['The polygon style shows the polygons with no outline, whereas line draws the polygons as outlines only.', 'polygon کا انداز کثیرالاضلاع کو بیرونی حد کے بغیر دکھاتا ہے، جبکہ line صرف ان کی بیرونی حدیں بناتا ہے۔', 'د polygon بڼه څو ضلعي له پولې پرته ښيي، خو line یوازې د هغوی پولې رسموي.'],
        ['The point line style is a combination of the point and line styles.', 'point line کا انداز، point اور line کے اندازوں کا مجموعہ ہے۔', 'د point line بڼه د point او line د بڼو یو ترکیب دی.']
    ]);
    passage('Symbol for points in the plot, where the value s is one of asterisk, box, circle, cross, diagonalcross, diamond, point, solidbox, solidcircle, soliddiamond', 'گراف کے نقاط کی علامت، جہاں s کی قیمت asterisk، box، circle، cross، diagonalcross، diamond، point، solidbox، solidcircle یا soliddiamond میں سے ایک ہے', 'په ګراف کې د نقطو نښه، چې د s ارزښت له asterisk، box، circle، cross، diagonalcross، diamond، point، solidbox، solidcircle یا soliddiamond څخه یو وي');
    sentences([
        ['The size of a symbol used in plotting can be given by a natural number.', 'گراف سازی میں استعمال ہونے والی علامت کا حجم کسی قدرتی عدد سے دیا جا سکتا ہے۔', 'په رسمولو کې د کارېدونکې نښې اندازه د یوه طبیعي عدد په وسیله ورکول کېدای شي.'],
        ['This does not affect the symbol POINT.', 'یہ POINT کی علامت پر اثر نہیں ڈالتا۔', 'دا د POINT پر نښه اغېز نه کوي.'],
        ['The symbolsize is 10 by default.', 'symbolsize کی پہلے سے مقرر قیمت 10 ہے۔', 'د symbolsize اصلي ټاکل شوی ارزښت 10 دی.']
    ]);
    sentences([
        ['This option specifies the thickness of lines in the plot.', 'یہ اختیار گراف کی لکیروں کی موٹائی مقرر کرتا ہے۔', 'دا غوراوی په ګراف کې د کرښو پنډوالی ټاکي.'],
        ['The thickness = n must be a non-negative number.', 'thickness = n ایک غیر منفی عدد ہونا چاہیے۔', 'thickness = n باید یو غیر منفي عدد وي.'],
        ['A value with 0 produces the thinnest line.', '0 کی قیمت سب سے باریک لکیر بناتی ہے۔', 'د 0 ارزښت تر ټولو نرۍ کرښه جوړوي.'],
        ['By default the value is 1.', 'پہلے سے مقرر قیمت 1 ہے۔', 'اصلي ټاکل شوی ارزښت 1 دی.']
    ]);
    passage('The values m and n specify the tick mark placement for the x-axis and y-axis respectively and can take an integer specifying the number of tick marks, a list of values specifying locations, a list of equations each having the form location = label, a name, or a spacing structure.', 'm اور n کی قیمتیں بالترتیب x محور اور y محور کے پیمانے کے نشانوں کی جگہیں مقرر کرتی ہیں؛ یہ نشانوں کی تعداد بتانے والا صحیح عدد، مقامات بتانے والی قیمتوں کی فہرست، location = label کی صورت رکھنے والی مساواتوں کی فہرست، ایک نام، یا وقفہ بندی کی ساخت ہو سکتی ہیں۔', 'د m او n ارزښتونه په ترتیب سره د x محور او y محور د مقیاس د نښو ځایونه ټاکي؛ دا د نښو د شمېر ټاکونکی صحیح عدد، د ځایونو ټاکونکو ارزښتونو لېست، د location = label بڼه لرونکو معادلو لېست، یو نوم، یا د واټنونو جوړښت کېدای شي.');
    sentences([
        ['We can give a title to the plot.', 'ہم گراف کو عنوان دے سکتے ہیں۔', 'موږ ګراف ته سرلیک ورکولی شو.'],
        ['The value t can be an arbitrary expression.', 't کی قیمت کوئی بھی عبارت ہو سکتی ہے۔', 'د t ارزښت هر ډول عبارت کېدای شي.'],
        ['The value t can also be a list consisting of the title followed by the font option.', 't کی قیمت ایسی فہرست بھی ہو سکتی ہے جس میں عنوان کے بعد font کا اختیار ہو۔', 'د t ارزښت داسې لېست هم کېدای شي چې سرلیک او ورپسې د font غوراوی ولري.'],
        ['There is no title by default for a plot.', 'گراف کا پہلے سے مقرر کوئی عنوان نہیں ہوتا۔', 'ګراف په اصلي ټاکنه کې سرلیک نه لري.']
    ]);
    sentences([
        ['It specified in the same manner as font.', 'یہ font کی طرح مقرر کیا جاتا ہے۔', 'دا د font په شان ټاکل کېږي.'],
        ['This option overrides values specified for font.', 'یہ اختیار font کے لیے مقرر کردہ قیمتوں پر فوقیت رکھتا ہے۔', 'دا غوراوی د font لپاره پر ټاکل شویو ارزښتونو لومړیتوب لري.']
    ]);
    sentences([
        ['This option specifies the transparency of the plot surface.', 'یہ اختیار گراف کی سطح کی شفافیت مقرر کرتا ہے۔', 'دا غوراوی د ګراف د سطحې روڼتیا ټاکي.'],
        ['The transparency = t must evaluate to a floating-point number in the range [0, 1].', 'transparency = t کی شمار شدہ قیمت [0, 1] کی حد میں ایک ممیزِ متحرک عدد ہونی چاہیے۔', 'د transparency = t محاسبه شوی ارزښت باید په [0, 1] ساحه کې د خوځنده ممیز عدد وي.'],
        ['0 means "not transparent" but 1 means "fully transparent."', '0 کا مطلب “غیر شفاف” اور 1 کا مطلب “مکمل شفاف” ہے۔', '0 د “ناشفاف” او 1 د “بشپړ شفاف” مانا لري.']
    ]);
    sentences([
        ['This option, with t set to true, indicates that units are part of the function and should be included in the axes labels.', 't کو true مقرر کرنے کے ساتھ یہ اختیار ظاہر کرتا ہے کہ اکائیاں تفاعل کا حصہ ہیں اور انہیں محوروں کے ناموں میں شامل کیا جانا چاہیے۔', 'دا غوراوی، چې t یې true ټاکل شوی وي، ښيي چې واحدونه د تابع برخه دي او باید د محورونو په نومپاڼو کې شامل شي.'],
        ['The value t can also be a list of units.', 't کی قیمت اکائیوں کی فہرست بھی ہو سکتی ہے۔', 'د t ارزښت د واحدونو یو لېست هم کېدای شي.']
    ]);
    sentences([
        ['View option indicates the minimum and maximum coordinates of the curve to be displayed on the screen.', 'View کا اختیار سکرین پر دکھائی جانے والی منحنی کے کم سے کم اور زیادہ سے زیادہ محددات بتاتا ہے۔', 'د View غوراوی پر پرده د ښودل کېدونکې منحني لږ تر لږه او ډېر تر ډېره مختصات ښيي.'],
        ['By default it is determined by the smartview option: if smartview = false is given, then all the plot data will be displayed; if smartview = true or the smartview option is not given, then the plot structure will be analyzed to determine a reasonable view of the data which allows you to see the significant features of the data.', 'پہلے سے مقرر حالت میں اسے smartview کا اختیار متعین کرتا ہے: اگر smartview = false دیا جائے تو گراف کا تمام ڈیٹا دکھایا جائے گا؛ اگر smartview = true ہو یا smartview کا اختیار نہ دیا گیا ہو تو گراف کی ساخت کا تجزیہ کر کے ڈیٹا کا ایسا مناسب منظر متعین کیا جائے گا جو آپ کو ڈیٹا کی نمایاں خصوصیات دیکھنے دے۔', 'په اصلي ټاکنه کې دا د smartview غوراوي له مخې ټاکل کېږي: که smartview = false ورکړل شي، د ګراف ټول معلومات ښودل کېږي؛ که smartview = true وي یا د smartview غوراوی نه وي ورکړل شوی، د ګراف جوړښت تحلیل کېږي څو د معلوماتو داسې مناسب لید وټاکل شي چې تاسو ته د معلوماتو د مهمو ځانګړنو د لیدلو اجازه درکړي.']
    ]);
    passage('If the same option is provided more than once, with different values, then the final value specified is generally the one used.', 'اگر ایک ہی اختیار مختلف قیمتوں کے ساتھ ایک سے زیادہ مرتبہ دیا جائے تو عموماً آخر میں مقرر کردہ قیمت استعمال ہوتی ہے۔', 'که یو غوراوی له بېلابېلو ارزښتونو سره تر یوه ځل ډېر ورکړل شي، عموماً وروستی ټاکل شوی ارزښت کارول کېږي.');
    passage('All above options are available for the Standard Worksheet interface.', 'مذکورہ تمام اختیارات Standard Worksheet رابطے کے لیے دستیاب ہیں۔', 'پورته ټول غوراوي د Standard Worksheet رابط لپاره شته.');
    passage('Example 6', 'مثال 6', 'بېلګه 6');
    passage('Plot the graph of sec(x) and give the title as;', 'sec(x) کا گراف بنائیں اور عنوان یوں دیں؛', 'د sec(x) ګراف رسم کړئ او سرلیک یې داسې ورکړئ؛');
    passage('This example uses the following axes and graph properties:', 'یہ مثال محوروں اور گراف کی درج ذیل خصوصیات استعمال کرتی ہے:', 'دا بېلګه د محورونو او ګراف لاندې ځانګړنې کاروي:');

    const vocabulary = {
        polynomial: ['کثیرالحدی عبارت', 'کثیرالحدي عبارت'],
        polynomials: ['کثیرالحدی عبارتیں', 'کثیرالحدي عبارتونه'],
        factorization: ['عوامل میں تجزیہ', 'په عاملونو وېشل'],
        factoring: ['عوامل معلوم کرنا', 'په عاملونو وېشل'],
        factor: ['عامل؛ عوامل معلوم کرنے کا حکم', 'عامل؛ په عاملونو د وېشلو امر'],
        expansion: ['توسیع؛ عبارت کو پھیلانا', 'پراخول؛ د عبارت پراختیا'],
        expanding: ['عبارت کو پھیلانا', 'د عبارت پراخول'],
        expand: ['پھیلانا؛ expand حکم', 'پراخول؛ د expand امر'],
        simplifying: ['سادہ کرنا', 'ساده کول'],
        simplify: ['سادہ کرنا؛ simplify حکم', 'ساده کول؛ د simplify امر'],
        rational: ['ناطق', 'ناطق'],
        substituting: ['جگہ قیمت رکھنا', 'پر ځای ارزښت اېښودل'],
        matrix: ['میٹرکس', 'ماتریس'],
        matrices: ['میٹرکسیں', 'ماتریسونه'],
        vector: ['سمتیہ', 'ویکتور'],
        entry: ['اندراج؛ میٹرکس کا عنصر', 'عنصر؛ د ماتریس غړی'],
        entries: ['اندراجات؛ میٹرکس کے عناصر', 'عناصر؛ د ماتریس غړي'],
        arrangement: ['ترتیب', 'ترتیب'],
        palette: ['پیلیٹ؛ اندراج کا آلہ', 'پلېټ؛ د ننویستلو وسیله'],
        palettes: ['پیلیٹ؛ اندراج کے آلات', 'پلېټونه؛ د ننویستلو وسایل'],
        rows: ['قطاریں', 'قطارونه'],
        columns: ['کالم؛ ستون', 'ستونونه'],
        inverse: ['معکوس', 'معکوس'],
        transpose: ['منقولہ؛ قطاروں اور کالموں کا تبادلہ', 'ترانسپوز؛ د قطارونو او ستونونو تبادله'],
        transport: ['منتقلی؛ یہاں اصل عنوان کا لفظ', 'لېږد؛ دلته د اصلي سرلیک کلمه'],
        determinant: ['مقطع؛ میٹرکس کا عددی تعین کنندہ', 'ټاکونکی؛ د ماتریس عددي ټاکونکی'],
        scalar: ['غیر سمتی مقدار', 'سکالر؛ بې لوري اندازه'],
        exchanged: ['آپس میں بدلے ہوئے', 'سره بدل شوي'],
        parenthesis: ['قوسین', 'قوسونه'],
        submenu: ['ذیلی مینو', 'فرعي مېنو'],
        dialog: ['مکالماتی خانہ', 'د خبرو اترو بکس'],
        respectively: ['بالترتیب', 'په ترتیب سره'],
        graphics: ['گرافکس؛ تصویری نمائندگی', 'ګرافیک؛ انځوریزه استازولي'],
        plotting: ['گراف بنانا', 'د ګراف رسمول'],
        plot: ['گراف؛ گراف بنانے کا حکم', 'ګراف؛ د رسمولو امر'],
        dimensional: ['بُعدی', 'بعدي'],
        domain: ['دائرۂ کار؛ جائز داخلی قیمتیں', 'د تعریف ساحه؛ منل شوي ننوتونکي ارزښتونه'],
        range: ['سعت؛ حاصل ہونے والی قیمتوں کی حد', 'د ارزښتونو ساحه'],
        parametric: ['پارامتری', 'پارامتري'],
        parameter: ['پارامیٹر', 'پارامیټر'],
        adaptive: ['حسبِ ضرورت موافقت کرنے والا', 'د اړتیا له مخې سمون لرونکی'],
        annotation: ['توضیحی نوٹ', 'تشریحي یادښت'],
        axes: ['محور', 'محورونه'],
        axis: ['محور', 'محور'],
        coordinates: ['محددات', 'مختصات'],
        coordinate: ['محدد؛ محدداتی', 'مختص؛ مختصاتي'],
        cartesian: ['کارتیسی', 'کارتیزي'],
        polar: ['قطبی', 'قطبي'],
        radial: ['شعاعی', 'شعاعي'],
        angular: ['زاویائی', 'زاویوي'],
        curve: ['منحنی', 'منحني'],
        curves: ['منحنیات', 'منحني ګانې'],
        background: ['پس منظر', 'شالید'],
        caption: ['توضیحی عنوان', 'تشریحي سرلیک'],
        font: ['رسم الخط', 'لیکبڼه'],
        color: ['رنگ', 'رنګ'],
        colors: ['رنگ', 'رنګونه'],
        scheme: ['ترتیب؛ منصوبہ', 'ترتیب؛ تګلاره'],
        discontinuities: ['عدم اتصال کے مقامات', 'د ناپیوستون ځایونه'],
        filled: ['بھرا ہوا', 'ډک شوی'],
        regions: ['خطے؛ علاقے', 'سیمې'],
        gridline: ['جالی کی لکیر', 'د جال کرښه'],
        gridlines: ['جالی کی لکیریں', 'د جال کرښې'],
        labels: ['ناموں کی علامتیں', 'نومپاڼې'],
        label: ['نام کی علامت', 'نومپاڼه'],
        legend: ['علامتوں کی وضاحت', 'د نښو تشریح'],
        resolution: ['نمائش کی وضاحت', 'د ښودنې تفکیک'],
        sample: ['نمونہ', 'نمونه'],
        sampled: ['نمونہ لیا گیا', 'نمونه اخیستل شوې'],
        sampling: ['نمونہ گیری', 'نمونې اخیستنه'],
        subsampling: ['مزید نمونہ گیری', 'فرعي نمونې اخیستنه'],
        subdivides: ['مزید تقسیم کرتا ہے', 'نور هم وېشي'],
        subdivided: ['مزید تقسیم کیے گئے', 'نور هم وېشل شوي'],
        subintervals: ['ذیلی وقفے', 'فرعي واټنونه'],
        scaling: ['پیمانہ مقرر کرنا', 'د مقیاس ټاکل'],
        scale: ['پیمانہ', 'مقیاس'],
        scales: ['پیمانے', 'مقیاسونه'],
        pixels: ['پکسل؛ تصویر کے نقاط', 'پکسلونه؛ د انځور ټکي'],
        transparency: ['شفافیت', 'روڼتیا'],
        transparent: ['شفاف', 'شفاف؛ روڼ'],
        thickness: ['موٹائی', 'پنډوالی'],
        polygon: ['کثیرالاضلاع', 'څو ضلعي'],
        polygons: ['کثیرالاضلاع شکلیں', 'څو ضلعي ګانې'],
        outline: ['بیرونی حد', 'بهرنۍ پوله'],
        interpolating: ['میانی قیمتیں معلوم کرنا', 'د منځنیو ارزښتونو موندل'],
        symbol: ['علامت', 'نښه'],
        title: ['عنوان', 'سرلیک'],
        horizontal: ['افقی', 'افقي'],
        vertical: ['عمودی', 'عمودي'],
        constrained: ['مقید؛ یکساں پیمانے کا پابند', 'مقید؛ په یو شان مقیاس پابند'],
        unconstrained: ['غیر مقید', 'غیر مقید'],
        pointer: ['اشارہ گر', 'نښه ګر'],
        hovers: ['اوپر ٹھہرتا ہے', 'پر سر درېږي'],
        screenshot: ['سکرین کی تصویر', 'د پردې انځور'],
        tick: ['پیمانے کا نشان', 'د مقیاس نښه'],
        arbitrary: ['کوئی بھی؛ من مانی', 'هر ډول؛ اختیاري'],
        proportion: ['تناسب', 'تناسب'],
        ratio: ['نسبت', 'نسبت'],
        golden: ['سنہری', 'طلایي']
    };

    const report = { scope: 'Reviewed textual source blocks, lists and captions in Unit 1 sections 1.1–1.4; excludes unit frontmatter, objectives and separate worked-example/study banks.', sections: [], newPassageEntries: 0, newWordMeanings: 0, preservedExistingPassageEntries: 0, preservedExistingBlockTranslations: 0 };
    for (const [english, rows] of translations) {
        if (!Object.prototype.hasOwnProperty.call(MATH12_SENTENCE_TRANSLATIONS, english)) {
            MATH12_SENTENCE_TRANSLATIONS[english] = rows;
            report.newPassageEntries++;
        } else report.preservedExistingPassageEntries++;
    }
    if (typeof MATH12_WORD_MEANINGS !== 'undefined') {
        for (const [word, meanings] of Object.entries(vocabulary)) {
            if (!Object.prototype.hasOwnProperty.call(MATH12_WORD_MEANINGS, word)) {
                MATH12_WORD_MEANINGS[word] = meanings;
                report.newWordMeanings++;
            }
        }
        report.totalCachedWordMeanings = Object.keys(MATH12_WORD_MEANINGS).length;
    }
    const covered = rows => Array.isArray(rows) && rows.length && rows.every(row => row.en && row.ur && row.ps);
    const unit = MATH_12_DATA.find(chapter => Number(chapter.number) === 1);
    for (const id of ['sec-1-1', 'sec-1-2', 'sec-1-3', 'sec-1-4']) {
        const section = unit?.sections?.find(candidate => candidate.id === id);
        if (!section) continue;
        const sectionReport = { id, textualBlocks: 0, translatedTextualBlocks: 0, listItems: 0, translatedListItems: 0, captions: 0, translatedCaptions: 0, figureDescriptions: 0, translatedFigureDescriptions: 0, sentenceRows: 0, missing: [] };
        for (const block of section.sourceBlocks || []) {
            const fields = ['figure', 'diagram'].includes(block.type) ? [['caption', 'captionSentenceTranslations', 'captions', 'translatedCaptions'], ['alt', 'altSentenceTranslations', 'figureDescriptions', 'translatedFigureDescriptions']] : ['heading', 'paragraph', 'clarification'].includes(block.type) ? [['text', 'sentenceTranslations', 'textualBlocks', 'translatedTextualBlocks']] : [];
            for (const [field, target, count, completed] of fields) {
                if (!block[field]) continue;
                sectionReport[count]++;
                if (block[target]?.length) report.preservedExistingBlockTranslations++;
                else if (MATH12_SENTENCE_TRANSLATIONS[block[field]]) block[target] = MATH12_SENTENCE_TRANSLATIONS[block[field]];
                if (covered(block[target])) {
                    sectionReport[completed]++;
                    sectionReport.sentenceRows += block[target].length;
                } else sectionReport.missing.push({ field, text: block[field] });
            }
            if (block.type === 'list') {
                if (!Array.isArray(block.itemSentenceTranslations)) block.itemSentenceTranslations = [];
                for (const [index, item] of (block.items || []).entries()) {
                    if (typeof item !== 'string') continue;
                    sectionReport.listItems++;
                    if (block.itemSentenceTranslations[index]?.length) report.preservedExistingBlockTranslations++;
                    else if (MATH12_SENTENCE_TRANSLATIONS[item]) block.itemSentenceTranslations[index] = MATH12_SENTENCE_TRANSLATIONS[item];
                    if (covered(block.itemSentenceTranslations[index])) {
                        sectionReport.translatedListItems++;
                        sectionReport.sentenceRows += block.itemSentenceTranslations[index].length;
                    } else sectionReport.missing.push({ field: `items[${index}]`, text: item });
                }
            }
        }
        report.sections.push(sectionReport);
    }
    globalThis.MATH12_TRANSLATION_COMPLETIONS_REPORT = report;
})();
