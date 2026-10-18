"""Economics XII PDF145: pp.270–271 — chapter 12 model paper: short questions 1–9, long questions i–ix, MCQs 1–10 (printed ✓).
Run: python class12_eco_page145.py"""
from class12_eco_common import BOOK, Builder, P, L, qa, mcqs, model


def Q(qe, qu, qp, ae, au, ap):
    return (qe, qu, qp, ae, au, ap)


def O(e, u=None, p=None):
    return (e, u or e, p or e)


QA = [
 Q('1. What are the four important big exports of Pakistan?', '1۔ پاکستان کی چار اہم بڑی بڑی برآمدات کیا ہیں؟', '1. د پاکستان څلور مهم لوی صادرات کوم دي؟',
   'A. (i) cotton thread; (ii) rice; (iii) bedwear; (iv) cotton.', 'جواب: (i) سوتی دھاگہ (ii) چاول (iii) بیڈ ویئر (iv) کپاس', 'ځواب: (i) د پنبې تار؛ (ii) وریجې؛ (iii) د بستر سامان؛ (iv) پنبه.'),
 Q('2. State the benefits that accrue to Pakistan from foreign trade.', '2۔ پاکستان کو بیرونی تجارت سے ہونے والے دو فائدے بتائیں؟', '2. پاکستان ته له بهرنۍ سوداګرۍ رسېدونکې ګټې ووایاست.',
   'A. (i) increase in foreign exchange; (ii) improvement in economic stability; (iii) increase in employment; (iv) acquaintance with new technology.', 'جواب: (i) زرِ مبادلہ میں اضافہ (ii) معاشی استحکام میں بہتری (iii) روزگار میں اضافہ (iv) نئی ٹیکنالوجی سے واقفیت', 'ځواب: (i) په بهرنیو اسعارو کې زیاتوالی؛ (ii) په اقتصادي ثبات کې ښه والی؛ (iii) په روزګار کې زیاتوالی؛ (iv) له نوې ټکنالوژۍ سره پېژندنه.'),
 Q('3. What is meant by the remittances of workers?', '3۔ کارکنوں کی ترسیلات سے کیا مراد ہے؟', '3. د کارکوونکو له لېږدونو څه مراد دی؟',
   'A. When the people of Pakistan, going outside the country and earning money, send it into the country, then it is called the remittances of workers.', 'جواب: جب پاکستان کے لوگ ملک سے باہر جا کر پیسے کما کر ملک کے اندر بھیجتے ہیں تو اسے کارکنوں کی ترسیلات کہا جاتا ہے۔', 'ځواب: کله چې د پاکستان خلک له هېواده بهر ولاړ شي او پیسې وګټي او هېواد ته یې ولېږي، نو دې ته د کارکوونکو لېږدونې ویل کېږي.'),
 Q('4. What is meant by diversification in the export heads of Pakistan?', '4۔ پاکستان کی برآمدی مدات میں تنوع سے کیا مراد ہے؟', '4. د پاکستان په صادراتي سرلیکونو کې له تنوع څه مراد دی؟',
   'A. The exports of Pakistan should not be of one nature, but rather should consist of different kinds; dependence cannot be made on one kind of nature.', 'جواب: پاکستان کی برآمدات ایک نوعیت کی نہیں ہونی چاہئیں بلکہ مختلف اقسام پر مشتمل ہونی چاہئیں ایک قسم کی نوعیت پر انحصار نہیں کیا جا سکتا۔', 'ځواب: د پاکستان صادرات باید د یوه ماهیت نه وي، بلکې باید له بېلابېلو ډولونو جوړ وي؛ پر یوه ډول ماهیت تکیه نشي کېدای.'),
 Q('5. Pakistan has three kinds of imports. State their names.', '5۔ پاکستان کی تین اقسامِ درآمدات ہیں۔ انکے نام بتایئے؟', '5. پاکستان درې ډوله واردات لري. نومونه یې ووایاست.',
   'A. (i) capital goods; (ii) industrial raw material; (iii) consumer goods.', 'جواب: (i) اشیائے سرمایہ (ii) صنعتی خام مال (iii) اشیائے صارفین', 'ځواب: (i) پانګیز توکي؛ (ii) صنعتي خام مواد؛ (iii) مصرفي توکي.'),
 Q('6. State the important imports of Pakistan.', '6۔ پاکستان کی اہم درآمدات بتائیں؟', '6. د پاکستان مهم واردات ووایاست.',
   'A. (i) machinery (non-electric); (ii) petrol and products; (iii) transport equipment; (iv) chemicals; (v) food items.', 'جواب: (i) مشینری (غیر برقی) (ii) پٹرول و پیداواریں (iii) نقل و حمل کا سامان (iv) کیمیکلز (v) اشیائے خوراک', 'ځواب: (i) ماشینري (غیربرېښنايي)؛ (ii) پټرول او تولیدات؛ (iii) ترانسپورټي سامان؛ (iv) کیمیکلونه؛ (v) خوراکي توکي.'),
 Q('7. State four reasons for disorder in the balance of payments of Pakistan.', '7۔ پاکستان کی ادائیگیوں کے توازن میں خرابی کی چار وجوہات بیان کریں؟', '7. د پاکستان د تادیاتو په توازن کې د خرابۍ څلور لاملونه بیان کړئ.',
   'A. (i) increase in imports; (ii) increase in the prices of imports; (iii) exports are less; (iv) decrease in workers’ remittances.', 'جواب: (i) درآمدات میں اضافہ (ii) درآمدات کی قیمتوں میں اضافہ (iii) برآمدات کم ہیں (iv) کارکنوں کی ترسیلات میں کمی', 'ځواب: (i) په وارداتو کې زیاتوالی؛ (ii) د وارداتو په بیو کې زیاتوالی؛ (iii) صادرات لږ دي؛ (iv) د کارکوونکو په لېږدونو کې کمښت.'),
 Q('8. Which countries are included in the Economic Cooperation Organisation?', '8۔ معاشی تعاون کی تنظیم میں کونسے ممالک شامل ہیں؟', '8. د اقتصادي همکارۍ په سازمان کې کوم هېوادونه شامل دي؟',
   'A. (i) Pakistan; (ii) Turkey; (iii) Iran.', 'جواب: (i) پاکستان (ii) ترکی (iii) ایران', 'ځواب: (i) پاکستان؛ (ii) ترکیه؛ (iii) ایران.'),
 Q('9. Write four benefits of international trade.', '9۔ بین الاقوامی تجارت کے چار فوائد لکھیں؟', '9. د نړیوالې سوداګرۍ څلور ګټې ولیکئ.',
   'A. (i) acquisition of necessary goods; (ii) surplus to need; (iii) agricultural and industrial development; (iv) means of government income.', 'جواب: (i) ضروری اشیاء کا حصول (ii) زائد از ضرورت (iii) زرعی، صنعتی ترقی (iv) سرکاری آمدنی کا ذریعہ', 'ځواب: (i) د اړینو توکو ترلاسه کول؛ (ii) له اړتیا زیات؛ (iii) کرنیز او صنعتي پرمختګ؛ (iv) د دولتي عاید وسیله.')]

MCQ = [
 (('Pakistan exports this to other countries:', 'پاکستان دوسرے ملکوں کو برآمد کرتا ہے:', 'پاکستان نورو هېوادونو ته دا صادروي:'),
  [O('edible oil', 'خوردنی تیل', 'خوراکي غوړي'), O('tea', 'چائے', 'چای'), O('surgical instruments', 'آلاتِ جراحی', 'جراحي وسایل'), O('chemicals', 'کیمیکلز', 'کیمیکلونه')], 2),
 (('This is an important export item of Pakistan:', 'پاکستان کی اہم برآمدی شے یہ ہے:', 'دا د پاکستان مهم صادراتي توکی دی:'),
  [O('hosiery and ready-made clothes', 'ہوزری و تیار کپڑے', 'هوزري او جوړې جامې'), O('leather', 'چمڑا', 'څرمن'), O('fish', 'مچھلی', 'کب'), O('cotton', 'کپاس', 'پنبه')], 0),
 (('In our exports the share of manufactures is this much:', 'ہماری برآمدات میں مصنوعات کا حصہ اس قدر ہے:', 'زموږ په صادراتو کې د محصولاتو ونډه دومره ده:'),
  [O('45 per cent', '45 فیصد', '۴۵ سلنه'), O('55 per cent', '55 فیصد', '۵۵ سلنه'), O('65 per cent', '65 فیصد', '۶۵ سلنه'), O('75 per cent', '75 فیصد', '۷۵ سلنه')], 3),
 (('These are included in the imports of Pakistan:', 'پاکستان کی درآمدات میں یہ شامل ہیں:', 'د پاکستان په وارداتو کې دا شامل دي:'),
  [O('carpets', 'قالین', 'غالۍ'), O('machines', 'مشینیں', 'ماشینونه'), O('cotton cloth', 'سوتی کپڑا', 'د پنبې ټوکر'), O('cotton', 'کپاس', 'پنبه')], 1),
 (('This is not included in the imports of Pakistan:', 'پاکستان کی درآمدات میں یہ شامل نہیں:', 'دا د پاکستان په وارداتو کې شامل نه دي:'),
  [O('petroleum', 'پٹرولیم', 'پټرولیم'), O('communications equipment', 'سامانِ مواصلات', 'مخابراتي سامان'), O('carpets', 'قالین', 'غالۍ'), O('tea', 'چائے', 'چای')], 2),
 (('The fourteenth conference of SAARC countries took place in this city:', 'سارک ممالک کی چودھویں کانفرنس اس شہر میں ہوئی:', 'د سارک هېوادونو څوارلسم کنفرانس په دې ښار کې وشو:'),
  [O('Dhaka', 'ڈھاکہ', 'ډاکه'), O('Delhi', 'دہلی', 'ډیلي'), O('Islamabad', 'اسلام آباد', 'اسلام اباد'), O('Colombo', 'کولمبو', 'کولمبو')], 1),
 (('The number of member countries of ECO (ECO) is:', 'ایکو (ECO) کے رکن ممالک کی تعداد ہے:', 'د اېکو (ECO) د غړو هېوادونو شمېر دی:'),
  [O('eight', 'آٹھ', 'اته'), O('ten', 'دس', 'لس'), O('twelve', 'بارہ', 'دولس'), O('fifteen', 'پندرہ', 'پنځلس')], 1),
 (('The head office of the SAARC organisation is here:', 'سارک تنظیم کا صدر دفتر یہاں ہے:', 'د سارک سازمان مرکزي دفتر دلته دی:'),
  [O('Tokyo', 'ٹوکیو', 'توکیو'), O('Kathmandu', 'کھٹمنڈو', 'کاټمنډو'), O('Lucknow', 'لکھنؤ', 'لکهنو'), O('Kabul', 'کابل', 'کابل')], 1),
 (('The ratio of imports and exports of Pakistan is:', 'پاکستان کی نسبت درآمد و برآمد ہے:', 'د پاکستان د وارداتو او صادراتو نسبت دی:'),
  [O('favourable', 'موافق', 'مناسب'), O('unfavourable', 'غیر موافق', 'نامناسب'), O('equal', 'مساوی', 'برابر'), O('unequal', 'غیر مساوی', 'نابرابر')], 1),
 (('In Pakistan the external value of the rupee was reduced in this year:', 'پاکستان میں روپے کی بیرونی قدر اس سال کم کی گئی:', 'په پاکستان کې د روپۍ بهرنی ارزښت په دې کال کم شو:'),
  [O('1970', '1970ء', '۱۹۷۰'), O('1972', '1972ء', '۱۹۷۲'), O('1974', '1974ء', '۱۹۷۴'), O('1976', '1976ء', '۱۹۷۶')], 1)]


def p145():
    b = Builder()
    b.h('Model paper questions', 'ماڈل پرچہ سوالات', 'د نمونې پرچې پوښتنې')
    b.h('Subjective (Subjective), Section I (Section I)', 'انشائیہ (Subjective) حصہ اول (Section I)', 'تشریحي (Subjective)، لومړۍ برخه (Section I)')
    P(b, [('Question 1: Write short answers to the following questions:', 'سوال نمبر 1: درج ذیل سوالات کے مختصر جوابات تحریر کریں:', '۱ پوښتنه: د لاندې پوښتنو لنډ ځوابونه ولیکئ:')])
    qa(b, QA)
    b.h('Section II (Section II)', 'حصہ دوم (Section II)', 'دویمه برخه (Section II)')
    P(b, [('Question 2: Write detailed answers to the following questions:', 'سوال نمبر 2: درج ذیل سوالات کے مفصل جوابات تحریر کریں:', '۲ پوښتنه: د لاندې پوښتنو مفصل ځوابونه ولیکئ:')])
    L(b, [('i) State the prominent characteristics of the foreign trade of Pakistan. (Gujranwala Board 2009, Lahore Board 2011)', 'i) پاکستان کی بیرونی تجارت کی نمایاں خصوصیات بیان کیجئے۔ (گوجرانوالہ بورڈ 2009ء، لاہور بورڈ 2011ء)', 'i) د پاکستان د بهرنۍ سوداګرۍ ښکاره ځانګړتیاوې بیان کړئ. (ګوجرانواله بورډ ۲۰۰۹، لاهور بورډ ۲۰۱۱)'),
          ('ii) State the importance of foreign trade in the Pakistani economy.', 'ii) پاکستانی معیشت میں بیرونی تجارت کی اہمیت بیان کریں۔', 'ii) په پاکستاني اقتصاد کې د بهرنۍ سوداګرۍ اهمیت بیان کړئ.')])
    r1 = model(b, 12, 1, 145, 270)
    t = Builder()
    L(t, [('iii) How can an increase be made in the exports of Pakistan?', 'iii) پاکستان کی برآمدات میں کس طرح اضافہ کیا جا سکتا ہے؟', 'iii) د پاکستان په صادراتو کې څنګه زیاتوالی راوستل کېدای شي؟'),
          ('iv) State the reasons for disorder in the balance of payments of Pakistan. (Bahawalpur Board 2011, Mirpur Azad Kashmir Board 2011)', 'iv) پاکستان کے توازنِ ادائیگی میں خرابی کی وجوہات بتایئے۔ (بہاولپور بورڈ 2011ء، میرپور آزاد کشمیر بورڈ 2011ء)', 'iv) د پاکستان د تادیاتو په توازن کې د خرابۍ لاملونه ووایاست. (بهاولپور بورډ ۲۰۱۱، میرپور ازاد کشمیر بورډ ۲۰۱۱)'),
          ('v) How can the balance of payments of Pakistan be made better?', 'v) پاکستان کے ادائیگیوں کے توازن کو کیسے بہتر بنایا جا سکتا ہے؟', 'v) د پاکستان د تادیاتو توازن څنګه ښه کېدای شي؟'),
          ('vi) State the important objectives of SAARC countries (SAARC).', 'vi) سارک ممالک (SAARC) کے اہم مقاصد بیان کیجئے۔', 'vi) د سارک هېوادونو (SAARC) مهمې موخې بیان کړئ.'),
          ('vii) State the effects of the World Trade Organisation (WTO) on the Pakistani economy.', 'vii) عالمی تجارتی تنظیم (WTO) کے پاکستانی معیشت پر اثرات بیان کیجئے۔', 'vii) پر پاکستاني اقتصاد د سوداګرۍ د نړیوال سازمان (WTO) اغېزې بیان کړئ.'),
          ('viii) How is the rate of exchange of currencies determined at the international level?', 'viii) بین الاقوامی سطح پر کرنسیوں کی شرحِ مبادلہ کیسے متعین ہوتی ہے؟', 'viii) په نړیواله کچه د اسعارو د تبادلې نرخ څنګه ټاکل کېږي؟'),
          ('ix) Mention the government’s efforts to increase exports. (Sargodha Board 2009)', 'ix) برآمدات بڑھانے کے لئے حکومت کی کوشش کا ذکر کیجئے؟ (سرگودھا بورڈ 2009ء)', 'ix) د صادراتو د زیاتولو لپاره د حکومت هڅې یادې کړئ. (سرګودها بورډ ۲۰۰۹)')])
    t.h('Objective (Objective)', 'معروضی (Objective)', 'معروضي (Objective)')
    P(t, [('Question 3: More than one answer has been given for each question; of them put the mark (✓) on the correct answer.', 'سوال نمبر 3: ہر سوال کے ایک سے زیادہ جوابات دیئے گئے ہیں۔ ان میں سے درست جواب پر (✓) کا نشان لگایئے۔', '۳ پوښتنه: د هرې پوښتنې له یوه زیات ځوابونه ورکړل شوي؛ له هغو څخه پر سم ځواب (✓) نښه ولګوئ.')])
    mcqs(t, MCQ)
    BOOK.save(145, [(12, r1), (12, model(t, 12, 2, 145, 271))], issues=[{'id': 'eco12-pdf145', 'unit': 12, 'printedPage': 270,
               'description': 'Printed ticks kept as printed: MCQ 3 ticks 75% for manufactures (the chapter says 70%); MCQ 6 ticks Delhi. MCQ 8 labels Kathmandu as option (C) while the second option is missing (printed A, C, C, D) — rendered in order. Short Q2 asks for “two” benefits but four are given — kept.'}])


if __name__ == '__main__':
    p145()
