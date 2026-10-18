"""Economics XII PDF133: pp.246–247 — chapter 11 model paper: short answers 6 (cont.)–19, long questions, MCQs 1–3 (printed ✓).
Run: python class12_eco_page133.py"""
from class12_eco_common import BOOK, Builder, P, L, qa, mcqs, model


def Q(qe, qu, qp, ae, au, ap):
    return (qe, qu, qp, ae, au, ap)


def O(e, u=None, p=None):
    return (e, u or e, p or e)


QA1 = [
 Q('(6, continued) …', '(6، جاری) …', '(۶، دوام) …',
   'Ushr: in the religion of Islam there is an order to pay zakat on agricultural produce too, whose rate is 10%. The zakat imposed on agricultural produce is called ushr. Thus it is obligatory on landlords that they pay the tenth part of their produce as zakat in the way of Allah.', 'عشر: دینِ اسلام میں زرعی پیداوار پر بھی زکوٰۃ ادا کرنے کا حکم ہے جس کی شرح 10% ہے زرعی پیداوار پر عائد کی جانے والی زکوٰۃ کو عشر کہتے ہیں۔ چنانچہ زمینداروں پر فرض ہے کہ وہ اپنی پیداوار کا دسواں حصہ بطورِ زکوٰۃ اللہ کی راہ میں ادا کریں۔', 'عشر: د اسلام په دین کې پر کرنیز تولید هم د زکات د ورکړې حکم دی چې نرخ یې ۱۰٪ دی. پر کرنیز تولید لګېدونکي زکات ته عشر وايي. نو پر ځمکوالو فرض ده چې د خپل تولید لسمه برخه د زکات په توګه د الله په لاره کې ورکړي.'),
 Q('7. Write four points of the importance of zakat.', '7۔ زکوٰۃ کی اہمیت کے چار نکات لکھیں؟', '7. د زکات د اهمیت څلور ټکي ولیکئ.',
   'A. (i) avoidance of extravagance; (ii) circulation of capital; (iii) increase in the pace of economic development; (iv) social welfare.', 'جواب: (i) فضول خرچی سے پرہیز (ii) سرمائے کی گردش (iii) معاشی ترقی کی رفتار میں اضافہ (iv) اجتماعی بہبود', 'ځواب: (i) له بې‌ځایه لګښت ډډه؛ (ii) د پانګې دوران؛ (iii) د اقتصادي پرمختګ په سرعت کې زیاتوالی؛ (iv) ټولنیزه هوساینه.'),
 Q('8. Who are the recipients of zakat?', '8۔ مستحقینِ زکوٰۃ کون ہیں؟', '8. د زکات مستحقین څوک دي؟',
   'A. (i) fuqara; (ii) masakin; (iii) workers of zakat; (iv) for reconciling hearts; (v) for freedom from slavery; (vi) debtors; (vii) fi sabilillah; (viii) traveller.', 'جواب: (i) فقراء (ii) مساکین (iii) عاملینِ زکوٰۃ (iv) تالیفِ قلوب کے لیے (v) غلامی سے چھٹکارہ کے لیے (vi) مقروض (vii) فی سبیل اللہ (viii) مسافر', 'ځواب: (i) فقراء؛ (ii) مساکین؛ (iii) د زکات عاملین؛ (iv) د زړونو د یوځای کولو لپاره؛ (v) له غلامۍ د خلاصون لپاره؛ (vi) پوروړي؛ (vii) فی سبیل الله؛ (viii) مسافر.'),
 Q('9. What is meant by public finance?', '9۔ سرکاری مالیات سے کیا مراد ہے؟', '9. له دولتي مالیې څه مراد دی؟',
   'A. In public finance the estimate of the government’s sources of income and its development and other expenditures is made, and a budget is prepared.', 'جواب: سرکاری مالیات میں حکومت کے ذرائعِ آمدنی اور اس کے ہونے والے ترقیاتی اور دیگر اخراجات کا تخمینہ لگایا جاتا ہے اور ایک بجٹ تیار کیا جاتا ہے۔', 'ځواب: په دولتي مالیه کې د حکومت د عاید سرچینو او د هغه د پراختیايي او نورو لګښتونو اټکل کېږي او یوه بودجه چمتو کېږي.'),
 Q('10. Write four sources of income of the provincial government.', '10۔ صوبائی حکومت کی آمدنی کے چار ذرائع لکھیں؟', '10. د ولایتي حکومت د عاید څلور سرچینې ولیکئ.',
   'A. (i) share of central government taxes; (ii) revenues of motor vehicles; (iii) stamps and court fee; (iv) registration.', 'جواب: (i) مرکزی حکومت کے ٹیکسوں کا حصہ (ii) موٹر گاڑیوں کے محصولات (iii) اشٹام اور کورٹ فیس (iv) رجسٹریشن', 'ځواب: (i) د مرکزي حکومت د مالیو ونډه؛ (ii) د موټرو محصولات؛ (iii) ټاپه او د محکمې فیس؛ (iv) راجسټرېشن.'),
 Q('11. What is meant by the budget?', '11۔ بجٹ سے کیا مراد ہے؟', '11. له بودجې څه مراد دی؟',
   'A. By the budget is meant such an estimate as is made by the government about the expected income and expenditure of the coming financial year.', 'جواب: بجٹ سے مراد ایسا تخمینہ ہے جو حکومت کے آئندہ مالی سال کی متوقع آمدنی اور اخراجات کے بارے میں لگایا جاتا ہے۔', 'ځواب: له بودجې مراد داسې اټکل دی چې د حکومت د راتلونکي مالي کال د متوقع عاید او لګښتونو په اړه لګول کېږي.'),
 Q('12. Write four measures for making the tax system of Pakistan better.', '12۔ پاکستان کے محصولات کے نظام کو بہتر بنانے کے لیے چار اقدامات لکھیں؟', '12. د پاکستان د مالیاتي نظام د ښه کولو لپاره څلور ګامونه ولیکئ.',
   'A. (i) increase in direct taxes; (ii) decrease in the burden of indirect taxes; (iii) prevention of tax evasion; (iv) arrangement for capital formation.', 'جواب: (i) براہِ راست ٹیکسوں میں اضافہ (ii) بالواسطہ ٹیکسوں کے بوجھ میں کمی (iii) ٹیکسوں چوری کا انسداد (iv) تشکیلِ سرمایا کا اہتمام', 'ځواب: (i) په مستقیمو مالیو کې زیاتوالی؛ (ii) د غیرمستقیمو مالیو په بار کې کمښت؛ (iii) د مالیې د غلا مخنیوی؛ (iv) د پانګې جوړېدو انتظام.'),
 Q('13. Write four important heads of the expenditures of the Government of Pakistan.', '13۔ حکومتِ پاکستان کے خراجات کے چار اہم مدیں لکھیں؟', '13. د پاکستان د حکومت د لګښتونو څلور مهم سرلیکونه ولیکئ.',
   'A. (i) defence; (ii) payment of interest on loans; (iii) subsidies; (iv) social and economic services.', 'جواب: (i) دفاع (ii) قرضوں پر سود کی ادائیگی (iii) اعانے (iv) معاشرتی و معاشی خدمات', 'ځواب: (i) دفاع؛ (ii) پر پورونو د سود ورکړه؛ (iii) مرستې؛ (iv) ټولنیز او اقتصادي خدمتونه.'),
 Q('14. Write the heads of the expenditures of provincial governments.', '14۔ صوبائی حکومتوں کے خراجات کی مدیں لکھیں؟', '14. د ولایتي حکومتونو د لګښتونو سرلیکونه ولیکئ.',
   'A. (i) tax-collecting departments; (ii) services of loans; (iii) public administration; (iv) social and economic service.', 'جواب: (i) ٹیکس اکٹھا کرنے والے محکمے (ii) قرضہ کی خدمات (iii) نظم و نسقِ عامہ (iv) معاشرتی و معاشی خدمت', 'ځواب: (i) مالیه راټولوونکې څانګې؛ (ii) د پور خدمتونه؛ (iii) عامه اداره؛ (iv) ټولنیز او اقتصادي خدمت.'),
 Q('15. How is the federal budget of Pakistan prepared?', '15۔ پاکستان کا وفاقی بجٹ کیسے تیار ہوتا ہے؟', '15. د پاکستان فدرالي بودجه څنګه چمتو کېږي؟',
   'A. The federal budget is prepared by the finance minister. The finance minister makes an estimate of income and expenditures from the institutions from which income is obtained; then he gives the estimates of these expenditures and income a final shape and presents them in the National Assembly, after whose approval the President of Pakistan announces it.', 'جواب: وفاقی بجٹ وزیرِ خزانہ تیار کرتا ہے۔ وزیرِ خزانہ آمدنی حاصل ہونے والے اداروں سے آمدنی اور اخراجات کا اندازہ لگایا ہے پھر ان اخراجات اور آمدنی کے تخمینوں کو ایک حتمی شکل دیتا ہے اور اسے قومی اسمبلی میں پیش کرتا ہے جس کی منظوری کے بعد صدرِ پاکستان اس کا اعلان کر دیتے ہیں۔', 'ځواب: فدرالي بودجه د مالیې وزیر چمتو کوي. د مالیې وزیر له عاید ترلاسه کوونکو ادارو د عاید او لګښتونو اټکل کوي، بیا د دې لګښتونو او عاید اټکلونو ته وروستۍ بڼه ورکوي او ملي اسمبلۍ ته یې وړاندې کوي، چې له تصویب وروسته یې د پاکستان ولسمشر اعلان کوي.'),
 Q('16. Write the nisab of zakat.', '16۔ زکوٰۃ کا نصاب لکھیں؟', '16. د زکات نصاب ولیکئ.',
   'A. If a person has 7½ tola of gold, 52½ tola of silver, and cash money equal to 200 dirhams, and he keeps it with himself for one year, then 2.5% zakat will be imposed on it. On minerals 20%. On cattle — camels 5, cows 30, sheep and goats 40 — if there are this many, then zakat will apply on them. On trade goods too zakat will be imposed at the rate of 2.5%.', 'جواب: اگر کسی شخص کے پاس سونا ½7 تولے، چاندی ½52 تولے اور نقد روپیہ 200 درہم کے برابر ہو اور اس کو ایک سال اپنے پاس رکھتا ہو تا اس پر 2.5% زکوٰۃ عائد ہو گی۔ معدنیات پر 20%۔ مال مویشی، اونٹ 5، گائے 30، بھیڑ بکریاں 40 ہوں تو اس پر زکوٰۃ لاگو ہو گی۔ سامانِ تجارت پر بھی 2.5% کے حساب سے زکوٰۃ عائد ہو گی۔', 'ځواب: که له یوه کس سره ½۷ تولې سره زر، ½۵۲ تولې سپین زر او د ۲۰۰ درهمو برابر نغدې روپۍ وي او یو کال یې له ځانه سره وساتي، نو پرې ۲.۵٪ زکات لګېږي. پر کانونو ۲۰٪. پر څارویو — اوښان ۵، غواګانې ۳۰، پسونه او وزې ۴۰ — که دومره وي، نو زکات پرې لګېږي. پر سوداګریز مال هم د ۲.۵٪ په حساب زکات لګېږي.'),
 Q('17. Is zakat an Islamic tax?', '17۔ کیا زکوٰۃ اسلامی ٹیکس ہے؟', '17. ایا زکات اسلامي مالیه ده؟',
   'A. No! Zakat and tax are separate concepts. Zakat is a pillar of Islam; its nisab is a fixed limit which has been fixed in Islam. There is no exemption from zakat, whereas tax is the income of the government; the government imposes it and also collects it; its rate keeps changing; for some reasons tax can also be exempted.', 'جواب: جی نہیں! زکوٰۃ اور ٹیکس دو علیحدہ علیحدہ تصور ہیں۔ زکوٰۃ اسلام کا ایک رکن ہے اس کا نصاب ایک مقررہ حد ہے جو اسلام میں مقرر کر دیا گیا ہے۔ زکوٰۃ کی کوئی معافی نہیں۔ جبکہ ٹیکس حکومت کی آمدنی ہے حکومت اس کو عائد کرتی ہے اور وصول بھی کرتی ہے اس کی شرح تبدیل ہوتی رہتی ہے بعض وجوہات میں ٹیکس معاف بھی ہو سکتا ہے۔', 'ځواب: نه! زکات او مالیه دوه جلا تصورونه دي. زکات د اسلام رکن دی؛ نصاب یې یوه ټاکلې پوله ده چې په اسلام کې ټاکل شوې. له زکات معافیت نشته. حال دا چې مالیه د حکومت عاید دی؛ حکومت یې لګوي او اخلي یې هم؛ نرخ یې بدلېږي؛ د ځینو لاملونو له امله مالیه معاف هم کېدای شي.'),
 Q('18. When was zakat enforced in Pakistan?', '18۔ پاکستان میں زکوٰۃ کا نفاذ کب ہوا؟', '18. په پاکستان کې زکات کله پلی شو؟',
   'A. In Pakistan the enforcement of zakat took place on 20 June 1980 on the day of Friday, and the year of zakat began from 1 Ramadan 1400 AH.', 'جواب: پاکستان میں زکوٰۃ کا نفاذ 20 جون 1980ء بروز جمعۃ المبارک کو ہوا زکوٰۃ کا سال یکم رمضان 1400ھ سے شروع ہوا۔', 'ځواب: په پاکستان کې زکات د ۱۹۸۰ د جون په ۲۰مه د جمعې په ورځ پلی شو، او د زکات کال د ۱۴۰۰ هـ د رمضان له لومړۍ پیل شو.'),
 Q('19. When was ushr enforced in Pakistan?', '19۔ پاکستان میں عشر کا نفاذ کب ہوا؟', '19. په پاکستان کې عشر کله پلی شو؟',
   'A. During 1982-83 the government announced that from the coming rabi crop ushr is compulsorily enforced, which will be 5% of the produce of canal-irrigated land.', 'جواب: 1982-83ء کے دوران حکومت نے یہ اعلان کیا کہ آئندہ سے فصل ربیع سے عشر لازمی نافذ ہے۔ جو کہ نہری زمین کی پیداوار کا 5% ہو گا۔', 'ځواب: د ۱۹۸۲-۸۳ په جریان کې حکومت اعلان وکړ چې له راتلونکي ربیع فصل څخه عشر لازمي پلی دی، چې د ویالو له اوبو خړوبې ځمکې د تولید ۵٪ به وي.')]

MCQ = [
 (('In Pakistan the financial year begins:', 'پاکستان میں مالی سال شروع ہوتا ہے', 'په پاکستان کې مالي کال پیلېږي:'),
  [O('from 1 January', 'یکم جنوری سے', 'د جنورۍ له لومړۍ'), O('from 1 April', 'یکم اپریل سے', 'د اپرېل له لومړۍ'), O('from 1 July', 'یکم جولائی سے', 'د جولای له لومړۍ'), O('from 1 October', 'یکم اکتوبر سے', 'د اکتوبر له لومړۍ')], 2),
 (('In Pakistan central excise is imposed on these:', 'پاکستان میں مرکزی ایکسائز ان پر عائد ہوتی ہے', 'په پاکستان کې مرکزي اېکسایز پر دې لګېږي:'),
  [O('imports', 'درآمدات', 'واردات'), O('exports', 'برآمدات', 'صادرات'), O('industrial production', 'صنعتی پیداوار', 'صنعتي تولید'), O('agricultural production', 'زرعی پیداوار', 'کرنیز تولید')], 2),
 (('This is included in the sources of income of the provincial government:', 'صوبائی حکومت کے ذرائعِ آمدنی میں یہ شامل ہے۔', 'د ولایتي حکومت د عاید په سرچینو کې دا شامل دي:'),
  [O('income tax', 'انکم ٹیکس', 'د عاید مالیه'), O('property tax', 'پراپرٹی ٹیکس', 'د ملکیت مالیه'), O('sales tax', 'سیلز ٹیکس', 'د پلور مالیه'), O('gift tax', 'تحفہ ٹیکس', 'د ډالۍ مالیه')], 1)]


def p133():
    b = Builder()
    qa(b, QA1[:10])
    P(b, [('(answer 15 continued on p.247) …', '(جواب 15، ص 247 پر جاری) …', '(د ۱۵ ځواب په ۲۴۷ مخ دوام) …')])
    r1 = model(b, 11, 2, 133, 246)
    t = Builder()
    qa(t, QA1[10:])
    t.h('Section II (Section II)', 'حصہ دوم (Section II)', 'دویمه برخه (Section II)')
    P(t, [('Question 2: Write detailed answers to the following questions.', 'سوال نمبر 2: درج ذیل سوالات کے مفصل جوابات تحریر کریں۔', '۲ پوښتنه: د لاندې پوښتنو مفصل ځوابونه ولیکئ.')])
    L(t, [('1. State the sources of income of the central government of Pakistan.', '1۔ مرکزی حکومت پاکستان کی آمدنی کے ذرائع بیان کریں۔', '۱. د پاکستان د مرکزي حکومت د عاید سرچینې بیان کړئ.'),
          ('2. Take a review of the tax system of Pakistan.', '2۔ پاکستان کے نظامِ محصولات کا جائزہ لیجئے۔', '۲. د پاکستان د مالیاتي نظام ارزونه وکړئ.'),
          ('3. Present proposals for making the revenue system of Pakistan better.', '3۔ پاکستان کے محصولاتی نظام کو بہتر بنانے کے لئے تجاویز پیش کریں۔', '۳. د پاکستان د محصولاتي نظام د ښه کولو لپاره وړاندیزونه وړاندې کړئ.'),
          ('4. State the big objectives of the fiscal policy (Fiscal Policy) of the central government.', '4۔ مرکزی حکومت کی مالیاتی پالیسی (Fiscal Policy) کے بڑے بڑے مقاصد بیان کیجئے۔', '۴. د مرکزي حکومت د مالي پالیسۍ (Fiscal Policy) لویې موخې بیان کړئ.'),
          ('5. Discuss the sources of income of the provincial governments of Pakistan. (Mirpur Azad Kashmir Board 2010, Multan Board 2011)', '5۔ پاکستان کی صوبائی حکومتوں کے ذرائع آمدنی پر بحث کریں۔ (میرپور آزاد کشمیر بورڈ 2010ء، ملتان بورڈ 2011ء)', '۵. د پاکستان د ولایتي حکومتونو د عاید پر سرچینو بحث وکړئ. (میرپور ازاد کشمیر بورډ ۲۰۱۰، ملتان بورډ ۲۰۱۱)'),
          ('6. Who are the recipients of zakat?', '6۔ زکوٰۃ کے مستحقین کون کون ہیں؟', '۶. د زکات مستحقین څوک دي؟'),
          ('7. Write a note on the economic and social importance of zakat. (Bahawalpur Board 2011)', '7۔ زکوٰۃ کی معاشی اور معاشرتی اہمیت پر نوٹ لکھیں۔ (بہاولپور بورڈ 2011ء)', '۷. د زکات پر اقتصادي او ټولنیز اهمیت یادښت ولیکئ. (بهاولپور بورډ ۲۰۱۱)')])
    P(t, [('Question 3: More than one answer has been given for each question; of them put the mark (✓) on the correct answer.', 'سوال نمبر 3: ہر سوال کے ایک سے زیادہ جوابات دئے گئے ہیں ان میں سے درست جواب پر (✓) کا نشان لگائیے۔', '۳ پوښتنه: د هرې پوښتنې له یوه زیات ځوابونه ورکړل شوي؛ له هغو څخه پر سم ځواب (✓) نښه ولګوئ.')])
    mcqs(t, MCQ)
    BOOK.save(133, [(11, r1), (11, model(t, 11, 3, 133, 247))], issues=[{'id': 'eco12-pdf133', 'unit': 11, 'printedPage': 246,
               'description': 'Printed ticks kept as printed: MCQ 3 ticks “property tax” as a provincial source. Answer 16 lists cattle nisab inline as printed; answer 19 gives ushr as 5% of canal-irrigated produce (the chapter says 10%) — kept. Answer 15 “اندازہ لگایا ہے”.'}])


if __name__ == '__main__':
    p133()
