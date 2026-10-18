"""Economics XII PDF157: pp.294–295 — chapter 13 MCQs 6–14 (printed ✓); appendix title page (budget for the fiscal year 2018-19).
Run: python class12_eco_page157.py"""
from class12_eco_common import BOOK, Builder, P, mcqs, model

APPX = ('Appendix and Examination Papers', 'ضمیمہ اور پرچہ جات', 'ضمیمه او د ازموینې پرچې')


def O(e, u=None, p=None):
    return (e, u or e, p or e)


MCQ = [
 (('In Pakistan the system of profit-and-loss sharing accounts (PLS account) began in this year:', 'پاکستان میں نفع نقصان شراکتی کھاتے (PLS اکاؤنٹ) کا نظام اس سال شروع ہوا:', 'په پاکستان کې د ګټې او زیان شراکتي حسابونو (PLS حساب) نظام په دې کال پیل شو:'),
  [O('1980', '1980ء', '۱۹۸۰'), O('1981', '1981ء', '۱۹۸۱'), O('1982', '1982ء', '۱۹۸۲'), O('1983', '1983ء', '۱۹۸۳')], 1),
 (('By extravagance is meant:', 'فضول خرچی سے مراد ہے:', 'له اسراف مراد دی:'),
  [O('spending beyond need', 'زائد از ضرورت خرچ', 'له اړتیا زیات لګښت'), O('help of orphans', 'یتیموں کی امداد', 'له یتیمانو سره مرسته'), O('spending on works of social welfare', 'معاشرتی بہبود کے کاموں پر خرچ', 'د ټولنیزې هوساینې پر کارونو لګښت')], 0),
 (('In socialism the productive resources are:', 'سوشلزم میں پیداواری ذرائع ہیں:', 'په سوسیالیزم کې تولیدي سرچینې دي:'),
  [O('private ownership', 'نجی ملکیت', 'شخصي ملکیت'), O('collective ownership', 'اجتماعی ملکیت', 'ټولیز ملکیت'), O('ownership of government ministers', 'سرکاری وزراء کی ملکیت', 'د دولتي وزیرانو ملکیت')], 1),
 (('Islam emphasises:', 'اسلام زور دیتا ہے:', 'اسلام ټینګار کوي:'),
  [O('absolute equality (Absolute Equality)', 'مطلق مساوات (Absolute Equality)', 'مطلقه برابري (Absolute Equality)'), O('inequality (Inequality)', 'عدم مساوات (Inequality)', 'نابرابري (Inequality)'), O('natural equality (Natural Equality)', 'فطری مساوات (Natural Equality)', 'طبیعي برابري (Natural Equality)'), O('on unnatural equality (Unnatural Equality)', 'غیر فطری مساوات (Unnatural Equality) پر', 'پر غیرطبیعي برابرۍ (Unnatural Equality)')], 2),
 (('The supporter of free trade:', 'آزاد تجارت کا حامی:', 'د ازادې سوداګرۍ ملاتړی:'),
  [O('socialism', 'سوشلزم', 'سوسیالیزم'), O('capitalist system', 'سرمایہ دارانہ نظام', 'پانګوال نظام'), O('Islamic economic system', 'اسلامی معاشی نظام', 'اسلامي اقتصادي نظام'), O('none of these', 'ان میں سے کوئی نہیں', 'له دې هېڅ یو')], 1),
 (('In which economic system does the interest system have a central status?', 'کس نظامِ معیشت میں سودی نظام کو مرکزی حیثیت حاصل ہے:', 'په کوم اقتصادي نظام کې سودي نظام مرکزي حیثیت لري؟'),
  [O('Islamic', 'اسلامی', 'اسلامي'), O('capitalist', 'سرمایہ دارانہ', 'پانګوال'), O('socialist', 'اشتراکی', 'سوسیالیستي'), O('mixed', 'مخلوط', 'ګډ')], 1),
 (('Who presented the concept of the socialist economic system?', 'اشتراکی نظامِ معیشت کا تصور کس نے پیش کیا:', 'د سوسیالیستي اقتصادي نظام تصور چا وړاندې کړ؟'),
  [O('Malthus', 'مالتھس', 'مالتوس'), O('Keynes', 'کینز', 'کینز'), O('Ricardo', 'ریکارڈو', 'ریکارډو'), O('Karl Marx', 'کارل مارکس', 'کارل مارکس')], 3),
 (('When did the establishment of the W.T.O come into being?', 'W.T.O کا قیام کب عمل میں آیا:', 'د W.T.O جوړېدل کله وشول؟'),
  [O('1948', '1948ء', '۱۹۴۸'), O('1995', '1995ء', '۱۹۹۵'), O('2003', '2003ء', '۲۰۰۳'), O('2004', '2004ء', '۲۰۰۴')], 1),
 (('The principle of partnership in profit and loss is the characteristic of which economic system?', 'نفع و نقصان میں شراکت کا اصول کس معاشی نظام کا وصف ہے؟', 'په ګټه او زیان کې د شراکت اصل د کوم اقتصادي نظام ځانګړتیا ده؟'),
  [O('Islamic economic system', 'اسلامی معاشی نظام', 'اسلامي اقتصادي نظام'), O('mixed economic system', 'مخلوط معاشی نظام', 'ګډ اقتصادي نظام'), O('capitalist system', 'سرمایہ دارانہ نظام', 'پانګوال نظام'), O('socialist system', 'اشتراکی نظام', 'سوسیالیستي نظام')], 0)]


def p157():
    b = Builder()
    mcqs(b, MCQ, start=6)
    r1 = model(b, 13, 3, 157, 294)
    t = Builder()
    t.h('Appendix', 'ضمیمہ', 'ضمیمه')
    P(t, [('[Boxed:] Current budget for the fiscal year 2018-19', '[خانے میں:] حالیہ بجٹ برائے مالی سال 2018-19', '[په چوکاټ کې:] د ۲۰۱۸-۱۹ مالي کال اوسنۍ بودجه')])
    r2 = BOOK.record(t, 'eco12-appx-1', 'Appendix — title page', 'ضمیمہ — سرورق', 'ضمیمه — سرپاڼه', 157, [295], unit_title=APPX)
    BOOK.save(157, [(13, r1), (14, r2)], complete_units=[13], issues=[{'id': 'eco12-pdf157', 'unit': 13, 'printedPage': 294,
               'description': 'Printed ticks kept as printed (e.g. MCQ 10 ticks the capitalist system as supporter of free trade). MCQs 7 and 8 print only three options. Chapter 13 ends on p.294; the appendix title page is p.295.'}])


if __name__ == '__main__':
    p157()
