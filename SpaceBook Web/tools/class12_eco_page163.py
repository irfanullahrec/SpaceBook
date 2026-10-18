"""Economics XII PDF163: p.306 (+ blank end leaf) — board paper 2019: Q4 (iii)–(xiii), part II Q5–9. End of book.
Run: python class12_eco_page163.py"""
from class12_eco_common import BOOK, Builder, P, L

Q4 = [('(iii) State four problems of the industrial sector of Pakistan.', '(iii) پاکستان کے صنعتی شعبہ کے چار مسائل بیان کیجئے۔', '(iii) د پاکستان د صنعتي برخې څلور ستونزې بیان کړئ.'),
      ('(iv) State four functions of the Planning Commission.', '(iv) منصوبہ بندی کمیشن کے چار فرائض بیان کیجئے۔', '(iv) د پلان جوړونې کمیسیون څلور دندې بیان کړئ.'),
      ('(v) What is meant by a dry port?', '(v) خشک گودی سے کیا مراد ہے؟', '(v) له وچ بندر څه مراد دی؟'),
      ('(vi) State four purposes of the motorways of Pakistan.', '(vi) پاکستان موٹرویز کے چار مقاصد بیان کیجئے۔', '(vi) د پاکستان د موټرویو څلور موخې بیان کړئ.'),
      ('(vii) What is the capital market?', '(vii) بازارِ سرمایہ کیا ہے؟', '(vii) د پانګې بازار څه دی؟'),
      ('(viii) What is meant by e-commerce?', '(viii) ای۔ کامرس سے کیا مراد ہے؟', '(viii) له برېښنايي سوداګرۍ څه مراد دی؟'),
      ('(ix) What is inheritance tax?', '(ix) وراثت ٹیکس کیا ہے؟', '(ix) د میراث مالیه څه ده؟'),
      ('(x) What is meant by ushr?', '(x) عشر سے کیا مراد ہے؟', '(x) له عشر څه مراد دی؟'),
      ('(xi) State the external rate of exchange.', '(xi) بیرونی شرحِ مبادلہ بیان کیجئے۔', '(xi) بهرنی د تبادلې نرخ بیان کړئ.'),
      ('(xii) Write four characteristics of the socialist system.', '(xii) اشتراکی نظام کی چار خصوصیات تحریر کیجئے۔', '(xii) د سوسیالیستي نظام څلور ځانګړتیاوې ولیکئ.'),
      ('(xiii) Define economic justice.', '(xiii) معاشی عدل کی تعریف کیجئے۔', '(xiii) اقتصادي عدالت تعریف کړئ.')]
LONG = [('5. Explain the different concepts of national income.', '5۔ قومی آمدنی کے مختلف تصورات کی وضاحت کیجئے۔', '۵. د ملي عاید بېلابېل تصورات روښانه کړئ.'),
        ('6. State the methods which the central bank adopts to control credit money.', '6۔ مرکزی بینک زرِ اعتبار کو کنٹرول کرنے کے جو طریقے اختیار کرتا ہے۔ بیان کیجئے۔', '۶. هغه طریقې بیان کړئ چې مرکزي بانک یې د اعتباري پیسو د کنټرول لپاره غوره کوي.'),
        ('7. State the difference between private and public finance.', '7۔ نجی اور سرکاری مالیات میں فرق بیان کیجئے۔', '۷. د شخصي او دولتي مالیې توپیر بیان کړئ.'),
        ('8. State the benefits and harms of international trade.', '8۔ بین الاقوامی تجارت کے فائدے اور نقصانات بیان کیجئے۔', '۸. د نړیوالې سوداګرۍ ګټې او زیانونه بیان کړئ.'),
        ('9. What are the causes of unemployment in Pakistan? Propose their solution.', '9۔ پاکستان میں بیروزگاری کی وجوہات کیا ہیں؟ ان کا حل تجویز کیجئے۔', '۹. په پاکستان کې د بې‌روزګارۍ لاملونه کوم دي؟ حل یې وړاندیز کړئ.')]


def p163():
    b = Builder()
    L(b, Q4)
    b.h('Part II', '(حصہ دوم)', 'دویمه برخه')
    P(b, [('Note: write answers to any three questions.', 'نوٹ: کوئی سے تین سوالات کے جوابات تحریر کیجئے۔', 'یادونه: د هرو درېیو پوښتنو ځوابونه ولیکئ.')])
    L(b, LONG)
    r1 = BOOK.record(b, 'eco12-papers-8', 'Board paper 2019 — subjective (2)', 'بورڈ پرچہ 2019ء — انشائیہ (2)', 'د بورډ پرچه ۲۰۱۹ — تشریحي (۲)', 163, [306])
    BOOK.save(163, [(14, r1)], complete_units=[14], issues=[{'id': 'eco12-pdf163', 'unit': 14, 'printedPage': 306,
               'description': 'Last printed page (p.306); the facing leaf in the scan is a blank end paper. Board paper questions transcribed as printed. End of book.'}])


if __name__ == '__main__':
    p163()
