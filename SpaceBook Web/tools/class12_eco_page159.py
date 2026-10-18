"""Economics XII PDF159: pp.298–299 — p.298 blank (running header only); board paper Economics Inter Part-II (2018), paper II,
objective part, MCQs 1–10 (no answers printed). Run: python class12_eco_page159.py"""
from class12_eco_common import BOOK, Builder, P, mcqs


def O(e, u=None, p=None):
    return (e, u or e, p or e)


MCQ = [
 (('The formula of the quantity theory of money was presented by:', 'نظریہ مقدارِ زر کا فارمولا پیش کیا:', 'د پیسو د اندازې د نظریې فورمول وړاندې کړ:'),
  [O('Taussig', 'ٹاؤسگ', 'ټاوسګ'), O('Fisher', 'فشر', 'فشر'), O('Marshall', 'مارشل', 'مارشل'), O('Robbins', 'رابنز', 'رابنز')], None),
 (('The principles of imposing taxes were first presented by:', 'ٹیکس عائد کرنے کے اصول پہلے پیش کیے:', 'د مالیې د لګولو اصول لومړی وړاندې کړل:'),
  [O('Adam Smith', 'ایڈم سمتھ', 'اډم سمیټ'), O('Marshall', 'مارشل', 'مارشل'), O('Malthus', 'مالتھس', 'مالتوس'), O('Ricardo', 'ریکارڈو', 'ریکارډو')], None),
 (('The fiscal year of Pakistan ends on:', 'پاکستان کا مالی سال ختم ہوتا ہے:', 'د پاکستان مالي کال پای ته رسېږي:'),
  [O('20 March', '20 مارچ', '۲۰ مارچ'), O('25 April', '25 اپریل', '۲۵ اپرېل'), O('30 May', '30 مئی', '۳۰ مۍ'), O('30 June', '30 جون', '۳۰ جون')], None),
 (('The centre of the national budget is:', 'قومی بجٹ کا مرکز ہوتا ہے:', 'د ملي بودجې مرکز وي:'),
  [O('co-operative bank', 'امدادِ باہمی کا بینک', 'د ګډې مرستې بانک'), O('savings bank', 'بچت کا بینک', 'د سپما بانک'), O('foreign exchange bank', 'زرِ مبادلہ کا بینک', 'د بهرنیو اسعارو بانک'), O('commercial bank', 'تجارتی بینک', 'سوداګریز بانک')], None),
 (('In the barter system the difficulty is:', 'بارٹر سسٹم میں مشکل ہے:', 'د جنس په جنس تبادلې په نظام کې ستونزه ده:'),
  [O('abundance of goods', 'اشیاء کی فراوانی', 'د توکو ډېروالی'), O('lack of double coincidence in goods', 'اشیاء میں دو طرفہ عدم مطابقت', 'په توکو کې د دوه‌اړخیزې برابرۍ نشتوالی'), O('difference of language', 'زبان کا فرق', 'د ژبې توپیر'), O('difference in professions', 'پیشوں میں فرق', 'په پیشو کې توپیر')], None),
 (('Unemployment allowance is:', 'بے روزگاری الاؤنس ہے:', 'د بې‌روزګارۍ تنخوا ده:'),
  [O('transfer payment', 'انتقالی ادائیگی', 'لېږدونیزه ورکړه'), O('net national product', 'خالص قومی پیداوار', 'خالص ملي تولید'), O('gross national product', 'خام قومی پیداوار', 'ناخالص ملي تولید'), O('national income', 'قومی آمدنی', 'ملي عاید')], None),
 (('Profit-and-loss sharing accounts (PLS) were introduced:', 'نفع و نقصان شراکتی کھاتوں (PLS) کا اجراء ہوا:', 'د ګټې او زیان شراکتي حسابونه (PLS) جاري شول:'),
  [O('in the Bhutto period', 'بھٹو دور میں', 'د بوټو په دوره کې'), O('in the Ayub period', 'ایوب دور میں', 'د ایوب په دوره کې'), O('in the Zia-ul-Haq period', 'ضیاء الحق دور میں', 'د ضیاء الحق په دوره کې'), O('in the Pervez Musharraf period', 'پرویز مشرف دور میں', 'د پرویز مشرف په دوره کې')], None),
 (('The theory of comparative costs was founded:', 'نظریہ تقابلی مصارف کی بنیاد رکھی گئی:', 'د پرتلیزو لګښتونو د نظریې بنسټ کېښودل شو:'),
  [O('on the law of demand', 'قانونِ طلب پر', 'د غوښتنې پر قانون'), O('on the law of supply', 'قانونِ رسد پر', 'د عرضې پر قانون'), O('on the labour theory of value', 'قدر کے نظریہ محنت پر', 'د ارزښت د کار پر نظریې'), O('on the law of substitution', 'قانونِ استبدال پر', 'د بدیل پر قانون')], None),
 (('The WTO (WTO) was established:', 'ڈبلیو ٹی او (WTO) قائم ہوئی:', 'WTO (WTO) جوړ شو:'),
  [O('1980', '1980', '۱۹۸۰'), O('1945', '1945', '۱۹۴۵'), O('1995', '1995', '۱۹۹۵'), O('1990', '1990', '۱۹۹۰')], None),
 (('The equilibrium level of national income is:', 'قومی آمدنی کی متوازن سطح ہے:', 'د ملي عاید متوازنه کچه ده:'),
  [O('consumption = saving', 'صرف = بچت', 'مصرف = سپما'), O('consumption = investment', 'صرف = سرمایہ کاری', 'مصرف = پانګونه'), O('income = investment', 'آمدنی = سرمایہ کاری', 'عاید = پانګونه'), O('saving = investment', 'بچت = سرمایہ کاری', 'سپما = پانګونه')], None)]


def p159():
    b = Builder()
    b.h('Economics Inter Part-II (2018)', 'معاشیات انٹر پارٹ II (2018)', 'اقتصاد انټر دویمه برخه (۲۰۱۸)')
    P(b, [('Paper II (objective type)', 'پرچہ II (معروضی طرز)', 'دویمه پرچه (معروضي بڼه)')])
    mcqs(b, MCQ)
    r1 = BOOK.record(b, 'eco12-papers-1', 'Board paper 2018 — objective (1)', 'بورڈ پرچہ 2018ء — معروضی (1)', 'د بورډ پرچه ۲۰۱۸ — معروضي (۱)', 159, [298, 299])
    BOOK.save(159, [(14, r1)], issues=[{'id': 'eco12-pdf159', 'unit': 14, 'printedPage': 298,
               'description': 'p.298 is blank apart from the running header (faint show-through only). The board paper MCQs (p.299) print no answer ticks; none are added.'}])


if __name__ == '__main__':
    p159()
