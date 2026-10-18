"""Economics XII PDF121: pp.222–223 — chapter 10 model paper: short answers 9–16, long questions, MCQs 1–11 (printed ✓).
Run: python class12_eco_page121.py"""
from class12_eco_common import BOOK, Builder, P, L, qa, mcqs, model


def Q(qe, qu, qp, ae, au, ap):
    return (qe, qu, qp, ae, au, ap)


def O(e, u=None, p=None):
    return (e, u or e, p or e)


MCQ = [
 (('The State Bank of Pakistan was established in this year:', 'سٹیٹ بینک آف پاکستان اس سال قائم ہوا:', 'د پاکستان دولتي بانک په دې کال جوړ شو:'),
  [O('1947', '1947ء', '۱۹۴۷'), O('1948', '1948ء', '۱۹۴۸'), O('1949', '1949ء', '۱۹۴۹'), O('1950', '1950ء', '۱۹۵۰')], 1),
 (('The institution issuing currency notes in Pakistan:', 'پاکستان میں کرنسی نوٹ جاری کرنے کا ادارہ:', 'په پاکستان کې د اسعارو د نوټونو صادروونکې اداره:'),
  [O('government', 'حکومت', 'حکومت'), O('National Bank', 'نیشنل بینک', 'ملي بانک'), O('State Bank', 'سٹیٹ بینک', 'دولتي بانک'), O('Habib Bank', 'حبیب بینک', 'حبیب بانک')], 2),
 (('Which bank of Pakistan is the representative of the central bank?', 'پاکستان کا کون سا بینک مرکزی بینک کا نمائندہ ہے؟', 'د پاکستان کوم بانک د مرکزي بانک استازی دی؟'),
  [O('Zarai Taraqiati Bank', 'زرعی ترقیاتی بینک', 'زرعي ترقیاتي بانک'), O('Industrial Development Bank', 'صنعتی ترقیاتی بینک', 'صنعتي پراختیايي بانک'), O('National Bank of Pakistan', 'نیشنل بینک آف پاکستان', 'د پاکستان ملي بانک'), O('Muslim Commercial Bank', 'مسلم کمرشل بینک', 'مسلم کمرشل بانک')], 2),
 (('In Pakistan at this time the number of stock exchanges (Stock Exchange) is:', 'پاکستان میں اس وقت بازارِ مبادلہ (Stock Exchange) کی تعداد ہے:', 'په پاکستان کې اوس د سټاک اېکسچینجونو (Stock Exchange) شمېر دی:'),
  [O('one', 'ایک', 'یو'), O('two', 'دو', 'دوه'), O('three', 'تین', 'درې'), O('four', 'چار', 'څلور')], 2),
 (('Zarai Taraqiati Bank Limited (ZTBL) was established in this year:', 'زرعی ترقیاتی بینک لمیٹڈ (ZTBL) اس سال قائم ہوا:', 'زرعي ترقیاتي بانک لمیټډ (ZTBL) په دې کال جوړ شو:'),
  [O('1960', '1960ء', '۱۹۶۰'), O('1961', '1961ء', '۱۹۶۱'), O('1963', '1963ء', '۱۹۶۳'), O('1966', '1966ء', '۱۹۶۶')], 1),
 (('By inflation is meant:', 'افراطِ زر سے مراد ہے:', 'له انفلاسیون مراد دی:'),
  [O('decrease in prices', 'قیمتوں میں کمی', 'په بیو کې کمښت'), O('increase in prices', 'قیمتوں میں اضافہ', 'په بیو کې زیاتوالی'), O('increase in production', 'پیداوار میں اضافہ', 'په تولید کې زیاتوالی')], 1),
 (('The remedy of inflation is:', 'افراطِ زر کا علاج ہے:', 'د انفلاسیون درملنه ده:'),
  [O('decrease in the rate of interest', 'شرح سود میں کمی', 'د سود په نرخ کې کمښت'), O('increase in the rate of interest', 'شرح سود میں اضافہ', 'د سود په نرخ کې زیاتوالی'), O('rate of interest as it is', 'شرح سود جوں کی توں', 'د سود نرخ لکه څنګه چې دی')], 1),
 (('By deficit financing (Deficit Financing) is meant:', 'تمویلِ خسارہ (Deficit Financing) سے مراد ہے:', 'له کسري تمویل (Deficit Financing) مراد دی:'),
  [O('taking loan from the central bank', 'مرکزی بینک سے قرضہ لینا', 'له مرکزي بانک پور اخیستل'), O('increasing tax', 'ٹیکس بڑھا دینا', 'مالیه زیاتول'), O('reducing the rate of interest', 'شرح سود کم کر دینا', 'د سود نرخ کمول')], 0),
 (('By capital formation is meant:', 'تشکیلِ سرمایہ سے مراد ہے:', 'له پانګې جوړېدو مراد دی:'),
  [O('giving loan to agriculture', 'زراعت کو قرضہ دینا', 'کرنې ته پور ورکول'), O('increasing the rate of tax', 'ٹیکس کی شرح بڑھا دینا', 'د مالیې نرخ لوړول'), O('increase in investment', 'سرمایہ کاری میں اضافہ', 'په پانګونه کې زیاتوالی')], 2),
 (('By inflation an increase occurs in which?', 'افراطِ زر سے کس میں اضافہ ہوتا ہے؟', 'په انفلاسیون کې په کوم شي کې زیاتوالی راځي؟'),
  [O('exports', 'برآمدات', 'صادرات'), O('savings', 'بچتیں', 'سپما'), O('investment', 'سرمایہ کاری', 'پانګونه'), O('purchasing power of money', 'زر کی قوتِ خرید', 'د پیسو د پېرود ځواک')], 2),
 (('E-commerce:', 'ای کامرس:', 'برېښنايي سوداګري:'),
  [O('electronic commerce', 'الیکٹرونک کامرس', 'برېښنايي سوداګري'), O('economic commerce', 'اکنامک کامرس', 'اقتصادي سوداګري'), O('electric commerce', 'الیکٹرک کامرس', 'برقي سوداګري'), O('export commerce', 'ایکسپورٹ کامرس', 'صادراتي سوداګري')], 0)]


def p121():
    b = Builder()
    qa(b, [
        Q('(9, continued) …', '(9، جاری) …', '(۹، دوام) …',
          'A. The State Bank of Pakistan was established on 1 July 1948, and its head office is in “Karachi”.', 'جواب: سٹیٹ بینک آف پاکستان یکم جولائی 1948ء کو قائم کیا گیا۔ اور اس کا مرکزی دفتر ”کراچی“ میں ہے۔', 'ځواب: د پاکستان دولتي بانک د ۱۹۴۸ د جولای په لومړۍ جوړ شو، او مرکزي دفتر یې په ”کراچۍ“ کې دی.'),
        Q('10. What is monetary policy?', '10۔ زری پالیسی کیا ہوتی ہے؟', '10. پولي پالیسي څه ده؟',
          'A. This is such a policy by means of which the central bank, by making the quantity of money less or more, controls prices.', 'جواب: یہ ایسی پالیسی ہوتی ہے جس کے ذریعے مرکزی بینک زر کی مقدار کو کم یا زیادہ کر کے قیمتوں کو کنٹرول کرتا ہے۔', 'ځواب: دا داسې پالیسي ده چې د هغې له لارې مرکزي بانک د پیسو اندازه کموي یا زیاتوي او بیې کنټرولوي.'),
        Q('11. What is an ATM?', '11۔ اے ٹی ایم کیا ہے؟', '11. اې ټي اېم څه دی؟',
          'A. This is such an automatic machine by means of which we can withdraw money from the bank whenever we want. ATM is the abbreviation of Automated Teller Machine.', 'جواب: یہ ایسی خودکار مشین ہے جس کے ذریعے ہم جس وقت چاہیں بینک سے رقم نکلوا سکتے ہیں۔ اے ٹی ایم، Automated Teller Machine کا مخفف ہے۔', 'ځواب: دا داسې اتومات ماشین دی چې د هغه له لارې موږ هر وخت چې وغواړو له بانکه پیسې ایستلی شو. اې ټي اېم د Automated Teller Machine لنډیز دی.'),
        Q('12. State four important functions of the State Bank of Pakistan.', '12۔ سٹیٹ بینک آف پاکستان کے چار اہم فرائض بتائیں؟', '12. د پاکستان دولتي بانک څلور مهمې دندې ووایاست.',
          'A. (i) bank of the government; (ii) economic stability; (iii) monopolist of issuing notes; (iv) guardian of the money market.', 'جواب: (i) حکومت کا بینک (ii) معاشی استحکام (iii) نوٹ جاری کرنے کا اجارہ دار (iv) بازارِ زر کا محافظ', 'ځواب: (i) د حکومت بانک؛ (ii) اقتصادي ثبات؛ (iii) د نوټونو د صادرولو انحصار لرونکی؛ (iv) د پیسو د بازار ساتونکی.'),
        Q('13. What is meant by e-commerce?', '13۔ ای۔ کامرس سے کیا مراد ہے؟', '13. له برېښنايي سوداګرۍ څه مراد دی؟',
          'A. By e-commerce is meant electronic commerce. In brief it is also called e-commerce or EC (EC). This is the modern method of business on the internet.', 'جواب: ای کامرس سے مراد ہے الیکٹرانک کامرس۔ اسے مختصراً ای کامرس یا ای سی (EC) بھی کہتے ہیں۔ یہ انٹرنیٹ پر کاروبار کا جدید طریقہ ہے۔', 'ځواب: له برېښنايي سوداګرۍ مراد الیکټرانیک کامرس دی. په لنډه توګه ورته اي کامرس یا اي سي (EC) هم وايي. دا پر انټرنېټ د کاروبار عصري طریقه ده.'),
        Q('16. State the difference between demand-pressure and cost-pushed inflation.', '16۔ طلب کے دباؤ اور لاگت فشار افراط میں فرق بتائیں؟', '16. د غوښتنې د فشار او د لګښت فشار انفلاسیون ترمنځ توپیر ووایاست.',
          'A. If an increase occurs in prices because of demand increasing, then it is called inflation of demand pressure; but if the increase in prices is because of the cost of production increasing, then it is called cost-push inflation.', 'جواب: اگر طلب کے بڑھنے سے قیمتوں میں اضافہ ہو تو اسے طلب کے دباؤ کا افراطِ زر کہتے ہیں لیکن اگر قیمتوں میں اضافہ لاگتِ پیدائش کے بڑھنے کی وجہ سے ہو تو اسے لاگتِ فشار کا افراطِ زر کہا جاتا ہے۔', 'ځواب: که د غوښتنې د زیاتېدو له امله په بیو کې زیاتوالی راشي، نو هغه ته د غوښتنې د فشار انفلاسیون وايي؛ خو که په بیو کې زیاتوالی د تولید د لګښت د زیاتېدو له امله وي، نو هغه ته د لګښت فشار انفلاسیون ویل کېږي.')])
    b.h('Section II (Section II)', 'حصہ دوم (Section II)', 'دویمه برخه (Section II)')
    P(b, [('Question 2: Write detailed answers to the following questions:', 'سوال نمبر 2: درج ذیل سوالات کے مفصل جوابات تحریر کریں:', '۲ پوښتنه: د لاندې پوښتنو مفصل ځوابونه ولیکئ:')])
    L(b, [('(i) Write the functions of a commercial bank.', '(i) تجارتی بینک کے فرائض لکھیے۔', '(i) د سوداګریز بانک دندې ولیکئ.'),
          ('(ii) State the kinds of banks.', '(ii) بینکوں کی اقسام بیان کیجئے۔', '(ii) د بانکونو ډولونه بیان کړئ.'),
          ('(iii) How do commercial banks create credit money? (Mirpur Azad Kashmir Board 2009)', '(iii) تجارتی بینک اعتباری زر کس طرح تخلیق کرتے ہیں؟ (میرپور آزاد کشمیر بورڈ 2009ء)', '(iii) سوداګریز بانکونه اعتباري پیسې څنګه پیدا کوي؟ (میرپور ازاد کشمیر بورډ ۲۰۰۹)'),
          ('(iv) State the general causes of inflation.', '(iv) افراطِ زر کے عمومی اسباب بیان کیجئے۔', '(iv) د انفلاسیون عمومي لاملونه بیان کړئ.'),
          ('(v) State the causes of inflation in Pakistan. (Bahawalpur Board 2011)', '(v) پاکستان میں افراطِ زر کے اسباب بیان کریں۔ (بہاولپور بورڈ 2011ء)', '(v) په پاکستان کې د انفلاسیون لاملونه بیان کړئ. (بهاولپور بورډ ۲۰۱۱)'),
          ('(vi) State the remedy of the inflation prevalent in Pakistan. In this connection which measures has the government taken?', '(vi) پاکستان میں رائج افراطِ زر کا علاج بتائیے۔ اس ضمن میں حکومت نے کون کون سے اقدامات کئے ہیں؟', '(vi) په پاکستان کې د رواج انفلاسیون درملنه ووایاست. په دې برخه کې حکومت کوم ګامونه پورته کړي؟'),
          ('(vii) Write the effects of inflation. (Multan Board 2009)', '(vii) افراطِ زر کے اثرات تحریر کریں۔ (ملتان بورڈ 2009ء)', '(vii) د انفلاسیون اغېزې ولیکئ. (ملتان بورډ ۲۰۰۹)'),
          ('(viii) Write a note on the National Bank of Pakistan.', '(viii) نیشنل بینک آف پاکستان پر ایک نوٹ لکھیے۔', '(viii) د پاکستان پر ملي بانک یادښت ولیکئ.'),
          ('(ix) State the functions of Zarai Taraqiati Bank Limited (ZTBL).', '(ix) زرعی ترقیاتی بینک لمیٹڈ (ZTBL) کے فرائض بیان کیجئے۔', '(ix) د زرعي ترقیاتي بانک لمیټډ (ZTBL) دندې بیان کړئ.'),
          ('(x) State the functions of the State Bank of Pakistan. (Mirpur Azad Kashmir Board 2011)', '(x) سٹیٹ بینک آف پاکستان کے فرائض بیان کیجئے۔ (میرپور آزاد کشمیر بورڈ 2011ء)', '(x) د پاکستان دولتي بانک دندې بیان کړئ. (میرپور ازاد کشمیر بورډ ۲۰۱۱)')])
    b.h('Objective (Objective)', 'معروضی (Objective)', 'معروضي (Objective)')
    P(b, [('Question 3: More than one answer has been given for each question; of them put the mark (✓) on the correct answer.', 'سوال نمبر 3: ہر سوال کے ایک سے زیادہ جوابات دیے گئے ہیں۔ ان میں درست جواب پر (✓) کا نشان لگائیے۔', '۳ پوښتنه: د هرې پوښتنې له یوه زیات ځوابونه ورکړل شوي؛ له هغو څخه پر سم ځواب (✓) نښه ولګوئ.')])
    mcqs(b, MCQ[:2])
    r1 = model(b, 10, 2, 121, 222)
    t = Builder()
    mcqs(t, MCQ[2:], start=3)
    BOOK.save(121, [(10, r1), (10, model(t, 10, 3, 121, 223))], complete_units=[10], issues=[{'id': 'eco12-pdf121', 'unit': 10, 'printedPage': 222,
               'description': 'Printed: short questions jump from 13 to 16 (14–15 missing) — numbering kept; MCQ 2 options split across pp.222–223 (kept together on p.222 here); MCQ 6 prints options A, B, D only and MCQ 7 labels B as “(ب)”; MCQ 3 ticks the National Bank as representative of the central bank; MCQ 10 ticks “investment” as increasing under inflation (the chapter says investment slackens) — ticks kept as printed. Chapter 10 ends on p.223.'}])


if __name__ == '__main__':
    p121()
