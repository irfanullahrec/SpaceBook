"""PDF141 printed 273–274: Example 8.1 (i) Q = 0.34, (ii) table and Q = −0.14; Example 8.2 (cholera inoculation, Q = −0.36); Example 8.3 start."""
from class12_statistics_common import Builder, save

Q = r'Q=\frac{(AB)(\alpha\beta)-(A\beta)(\alpha B)}{(AB)(\alpha\beta)+(A\beta)(\alpha B)}'
SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.mlines([r'Q=\frac{(110)(510)-(290)(96)}{(110)(510)+(290)(96)}', r'Q=\frac{28260}{83940}=0.34'])
b.p('It means that there is positive association between attributes A and B.', 'اس کا مطلب ہے کہ صفات A اور B کے درمیان مثبت تلازم ہے۔', 'مانا دا ده چې د A او B صفتونو ترمنځ مثبت تړاو شته.')
b.p('(ii) Given (A) = 245, (AB) = 147, (α) = 285, (αB) = 190', '(ii) دیا گیا ہے (A) = 245، (AB) = 147، (α) = 285، (αB) = 190', '(ii) ورکړل شوي (A) = 245، (AB) = 147، (α) = 285، (αB) = 190')
b.p('Since all values required for the coefficient of association formula are not known, so first put these values in a (2 × 2) contingency table to find the unknown values easily by addition or subtraction as.', 'چونکہ تلازم کے سر کے فارمولے کے لیے درکار تمام قیمتیں معلوم نہیں، اس لیے پہلے ان قیمتوں کو (2 × 2) اتفاقی جدول میں رکھیں تاکہ نامعلوم قیمتیں جمع یا تفریق سے آسانی سے معلوم ہو سکیں۔', 'څرنګه چې د تړاو د ضریب فورمول ته اړین ټول قیمتونه معلوم نه دي، نو لومړی دا قیمتونه په (2 × 2) احتمالي جدول کې کېږدئ ترڅو نامعلوم قیمتونه په جمع یا تفریق په اسانۍ پیدا شي.')
b.p('(2 × 2) contingency table', '(2 × 2) اتفاقی جدول', '(2 × 2) احتمالي جدول')
b.table('stat12-t-ex8-1', ['Attributes', 'B', 'β', 'Row total'],
        [['A', '(AB) = 147', '(Aβ) = 98', '(A) = 245'], ['α', '(αB) = 190', '(αβ) = 95', '(α) = 285'], ['Column total', '(B) = 337', '(β) = 193', 'n = 530']],
        ['صفات', 'B', 'β', 'قطار کا میزان'], ['صفتونه', 'B', 'β', 'د قطار ټولټال'],
        [['A', '(AB) = 147', '(Aβ) = 98', '(A) = 245'], ['α', '(αB) = 190', '(αβ) = 95', '(α) = 285'], ['کالم کا میزان', '(B) = 337', '(β) = 193', 'n = 530']],
        [['A', '(AB) = 147', '(Aβ) = 98', '(A) = 245'], ['α', '(αB) = 190', '(αβ) = 95', '(α) = 285'], ['د ستون ټولټال', '(B) = 337', '(β) = 193', 'n = 530']])
b.p('Now', 'اب', 'اوس')
b.mlines([Q, r'Q=\frac{(147)(95)-(98)(190)}{(147)(95)+(98)(190)}', r'Q=\frac{13965-18620}{13965+18620}=\frac{-4655}{32585}=-0.14'])
b.p('Thus there is negative association between A and B.', 'یوں A اور B کے درمیان منفی تلازم ہے۔', 'نو د A او B ترمنځ منفي تړاو شته.')
e81 = b.build('stat12-p141-example-8-1', 'Example 8.1 — Yule’s Q, parts (i) and (ii)', 'مثال 8.1 — یول کا Q، حصے (i) اور (ii)', 'بېلګه 8.1 — د یول Q، برخې (i) او (ii)', 141, [273])

c = Builder()
c.h('Example 8.2', 'مثال 8.2', 'بېلګه 8.2')
c.p('The following table shows the data obtained during an epidemic of cholera.', 'درج ذیل جدول ہیضے کی وبا کے دوران حاصل کردہ مواد دکھاتا ہے۔', 'لاندې جدول د کولرا د وبا پر مهال ترلاسه شوي معلومات ښيي.')
c.table('stat12-t-ex8-2', ['Attributes', 'attacked', 'not attacked'], [['inoculated', '31', '469'], ['not inoculated', '185', '1315']],
        ['صفات', 'متاثر', 'غیر متاثر'], ['صفتونه', 'اخته', 'نا اخته'],
        [['ٹیکہ لگا', '31', '469'], ['ٹیکہ نہیں لگا', '185', '1315']], [['واکسین شوي', '31', '469'], ['نا واکسین شوي', '185', '1315']])
c.p('Test the effectiveness of inoculation in preventing attack of cholera.', 'ہیضے کے حملے کو روکنے میں ٹیکے کی تاثیر کی جانچ کریں۔', 'د کولرا د حملې په مخنیوي کې د واکسین اغېزمنتیا وازموئ.')
c.h(*SOL)
c.p('Let us denote inoculated by A and attack by B.', 'ٹیکہ لگے ہوئے کو A اور حملے کو B سے ظاہر کریں۔', 'واکسین شوي په A او حمله په B وښیو.')
c.p('The given data can be written as under', 'دیا گیا مواد یوں لکھا جا سکتا ہے', 'ورکړل شوي معلومات داسې لیکل کېدای شي')
c.p('(AB) = 31, (Aβ) = 469, (αB) = 185, (αβ) = 1315', '(AB) = 31، (Aβ) = 469، (αB) = 185، (αβ) = 1315', '(AB) = 31، (Aβ) = 469، (αB) = 185، (αβ) = 1315')
c.p('Putting in the coefficient of association we get', 'تلازم کے سر میں رکھنے سے ہمیں ملتا ہے', 'د تړاو په ضریب کې د ایښودو سره ترلاسه کوو')
c.mlines([Q, r'Q=\frac{(31)(1315)-(469)(185)}{(31)(1315)+(469)(185)}=\frac{40765-86765}{40765+86765}=\frac{-46000}{127530}=-0.36'])
c.p('There is negative association between inoculation and attack of cholera disease.', 'ٹیکے اور ہیضے کی بیماری کے حملے کے درمیان منفی تلازم ہے۔', 'د واکسین او د کولرا ناروغۍ د حملې ترمنځ منفي تړاو شته.')
e82 = c.build('stat12-p141-example-8-2', 'Example 8.2 — inoculation and cholera', 'مثال 8.2 — ٹیکہ اور ہیضہ', 'بېلګه 8.2 — واکسین او کولرا', 141, [274])

d = Builder()
d.h('Example 8.3', 'مثال 8.3', 'بېلګه 8.3')
d.p('For admission in a medical college 1660 candidates appeared in an entry test and 422 were successful. 256 attended a coaching class and of these 150 came out successful. Estimate the utility of the coaching classes.', 'میڈیکل کالج میں داخلے کے لیے 1660 امیدواروں نے داخلہ ٹیسٹ دیا اور 422 کامیاب ہوئے۔ 256 نے کوچنگ کلاس میں شرکت کی اور ان میں سے 150 کامیاب ہوئے۔ کوچنگ کلاسوں کی افادیت کا اندازہ لگائیں۔', 'په طبي کالج کې د داخلې لپاره 1660 نوماندانو د داخلې ازموینه ورکړه او 422 بریالي شول. 256 د کوچنګ ټولګي ته ورغلل او له دوی 150 بریالي شول. د کوچنګ ټولګیو ګټورتیا اټکل کړئ.')
d.h(*SOL)
d.p('Putting the given information in (2 × 2) contingency table as;', 'دی گئی معلومات کو (2 × 2) اتفاقی جدول میں یوں رکھیں؛', 'ورکړل شوي معلومات په (2 × 2) احتمالي جدول کې داسې کېږدئ؛')
e83 = d.build('stat12-p141-example-8-3', 'Example 8.3 — coaching classes (start)', 'مثال 8.3 — کوچنگ کلاسیں (آغاز)', 'بېلګه 8.3 — د کوچنګ ټولګي (پیل)', 141, [274])

if __name__ == '__main__':
    save(141, [(8, e81), (8, e82), (8, e83)])
