"""PDF126 printed 243–244: 7.2.2 steps iv–vi; Example 7.5 (butter jars, t test); Example 7.6 start (tire life)."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import tail_test

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.p('where as $s=\\sqrt{\\frac{1}{n-1}\\Sigma(x-\\overline{x})^2}$', 'جبکہ $s=\\sqrt{\\frac{1}{n-1}\\Sigma(x-\\overline{x})^2}$', 'په داسې حال کې چې $s=\\sqrt{\\frac{1}{n-1}\\Sigma(x-\\overline{x})^2}$')
b.p('iv. Calculation of t-value.', 'iv. t کی قیمت کا حساب۔', 'iv. د t قیمت محاسبه.')
b.p('v. Critical region:', 'v. فیصلہ کن علاقہ:', 'v. بحراني سیمه:')
b.group('lines', [
    ('For case (a)', 'صورت (a) کے لیے', 'د (a) حالت لپاره'),
    ('Reject $H_0$ if $t\\le -t_{\\alpha/2,(\\nu)}$ or $t\\ge t_{\\alpha/2,(\\nu)}$', '$H_0$ کو رد کریں اگر $t\\le -t_{\\alpha/2,(\\nu)}$ یا $t\\ge t_{\\alpha/2,(\\nu)}$', '$H_0$ رد کړئ که $t\\le -t_{\\alpha/2,(\\nu)}$ یا $t\\ge t_{\\alpha/2,(\\nu)}$'),
    ('For case (b)', 'صورت (b) کے لیے', 'د (b) حالت لپاره'),
    ('Reject $H_0$ if $t\\ge t_{\\alpha(\\nu)}$', '$H_0$ کو رد کریں اگر $t\\ge t_{\\alpha(\\nu)}$', '$H_0$ رد کړئ که $t\\ge t_{\\alpha(\\nu)}$'),
    ('For case (c)', 'صورت (c) کے لیے', 'د (c) حالت لپاره'),
    ('Reject $H_0$ if $t\\le -t_{\\alpha(\\nu)}$', '$H_0$ کو رد کریں اگر $t\\le -t_{\\alpha(\\nu)}$', '$H_0$ رد کړئ که $t\\le -t_{\\alpha(\\nu)}$'),
])
b.p('Where t is computed value of t-statistic and $t_{\\alpha/2(\\nu)}$ or $t_{\\alpha(\\nu)}$ is table value.', 'جہاں t، t-شماریے کی معلوم کی گئی قیمت اور $t_{\\alpha/2(\\nu)}$ یا $t_{\\alpha(\\nu)}$ جدول کی قیمت ہے۔', 'چې t د t-احصاییې محاسبه شوی قیمت او $t_{\\alpha/2(\\nu)}$ یا $t_{\\alpha(\\nu)}$ د جدول قیمت دی.')
b.p('vi. Conclusion:', 'vi. نتیجہ:', 'vi. پایله:')
st = b.build('stat12-p126-t-steps', '7.2.2 Small-sample t test — calculation, critical regions and conclusion', '7.2.2 چھوٹے نمونے کی t جانچ — حساب، فیصلہ کن علاقے اور نتیجہ', '7.2.2 د کوچنۍ نمونې t ازموینه — محاسبه، بحراني سیمې او پایله', 126, [243])

c = Builder()
c.h('Example 7.5', 'مثال 7.5', 'بېلګه 7.5')
c.p('A sample of 12 jars of butter was taken form a lot, each jar being labeled 8 ounces net weight. The individual weights in ounces are 7.3, 7.4, 7.5, 8.0, 7.4, 8.2, 8.0, 7.6, 7.6, 7.5, 7.5, and 7.7. Test whether these values are consistent with a population mean of 8 ounces. Assume that the weights are normally distributed.',
    'ایک کھیپ سے مکھن کے 12 مرتبانوں کا نمونہ لیا گیا، ہر مرتبان پر 8 اونس خالص وزن لکھا ہے۔ اونس میں انفرادی وزن یہ ہیں: 7.3، 7.4، 7.5، 8.0، 7.4، 8.2، 8.0، 7.6، 7.6، 7.5، 7.5 اور 7.7۔ جانچیں کہ کیا یہ قیمتیں 8 اونس کے آبادی کے اوسط سے مطابقت رکھتی ہیں۔ فرض کریں کہ وزن نارمل تقسیم شدہ ہیں۔',
    'له یوې کھیپ څخه د کوچو د 12 بوتلونو نمونه واخیستل شوه، په هر بوتل 8 اونسه خالص وزن لیکل شوی. په اونسو کې جلا وزنونه دا دي: 7.3، 7.4، 7.5، 8.0، 7.4، 8.2، 8.0، 7.6، 7.6، 7.5، 7.5 او 7.7. وازموئ چې آیا دا قیمتونه د 8 اونسو د نفوس له منځني سره سمون لري. فرض کړئ چې وزنونه نورمال وېش لري.')
c.h(*SOL)
c.group('lines', [
    ('i. $H_0:\\mu=8$',) * 3, ('$H_1:\\mu\\neq 8$',) * 3, ('ii. α = 0.05',) * 3,
    ('iii. Test statistic to be used in this case is $t=\\frac{\\overline{X}-\\mu}{s/\\sqrt{n}}$ with ν = n − 1 d.f', 'iii. اس صورت میں استعمال ہونے والا جانچ کا شماریہ $t=\\frac{\\overline{X}-\\mu}{s/\\sqrt{n}}$ ہے جس کے درجاتِ آزادی ν = n − 1 ہیں', 'iii. په دې حالت کې کارېدونکې د ازموینې احصاییه $t=\\frac{\\overline{X}-\\mu}{s/\\sqrt{n}}$ ده چې د ازادۍ درجې یې ν = n − 1 دي'),
    ('iv. Calculation:', 'iv. حساب:', 'iv. محاسبه:'),
])
c.mlines([r'\text{Given } n=12,\ \Sigma x=91.7,\ \Sigma x^2=701.61,\ \overline{X}=\frac{\Sigma x}{n}=\frac{91.7}{12}=7.64',
          r's=\sqrt{\frac{1}{n-1}\left[\Sigma x^2-\frac{(\Sigma x)^2}{n}\right]}=\sqrt{\frac{1}{12-1}\left[701.61-\frac{(91.7)^2}{12}\right]}', r'=\sqrt{\frac{1}{11}[0.8692]}=0.28',
          r'\text{Hence } t=\frac{7.64-8}{0.28/\sqrt{12}}=\frac{(-0.36)\sqrt{12}}{0.28}=-4.45'])
c.p('v. Critical region:', 'v. فیصلہ کن علاقہ:', 'v. بحراني سیمه:')
c.vpara('stat12-ex7-5-cr', tail_test('two', z=2.201, mid='', ticks=((-2.201, '−2.201'), (0, '0'), (2.201, '2.201')), label='Two-sided t critical region at ±2.201'),
        'Reject $H_0$ if $t\\le -t_{\\alpha/2,(\\nu)}$ or $t\\ge t_{\\alpha/2,(\\nu)}$ whereas from t-table 6.1, we have $t_{\\alpha/2,(\\nu)}=t_{0.05,(12-1)}=t_{0.025,(11)}=2.201$',
        '$H_0$ کو رد کریں اگر $t\\le -t_{\\alpha/2,(\\nu)}$ یا $t\\ge t_{\\alpha/2,(\\nu)}$ جبکہ t-جدول 6.1 سے ہمارے پاس $t_{\\alpha/2,(\\nu)}=t_{0.05,(12-1)}=t_{0.025,(11)}=2.201$ ہے',
        '$H_0$ رد کړئ که $t\\le -t_{\\alpha/2,(\\nu)}$ یا $t\\ge t_{\\alpha/2,(\\nu)}$ په داسې حال کې چې له t-جدول 6.1 څخه لرو $t_{\\alpha/2,(\\nu)}=t_{0.05,(12-1)}=t_{0.025,(11)}=2.201$', ratio=.45)
c.p('vi. Conclusion:', 'vi. نتیجہ:', 'vi. پایله:')
c.p('As t = −4.45 falls in the rejection region, therefore, we reject $H_0$.', 'چونکہ t = −4.45 رد کے علاقے میں ہے، لہٰذا ہم $H_0$ رد کرتے ہیں۔', 'څرنګه چې t = −4.45 د ردولو په سیمه کې لوېږي، نو $H_0$ ردوو.')
e75 = c.build('stat12-p126-example-7-5', 'Example 7.5 — t test for butter-jar weights', 'مثال 7.5 — مکھن کے مرتبانوں کے وزن کی t جانچ', 'بېلګه 7.5 — د کوچو د بوتلونو د وزن t ازموینه', 126, [243, 244])

d = Builder()
d.h('Example 7.6', 'مثال 7.6', 'بېلګه 7.6')
d.p('A manufacturing company making automobile tire claims that the average life of its product is 35000 miles. A random sample of 16 tires was selected and it was found that the mean life was 34000 miles with a standard deviation s = 2000 miles. Test the hypothesis $H_0:\\mu=35000$ against the alternative $H_1:\\mu<35000$ at α = 0.05.', 'گاڑیوں کے ٹائر بنانے والی ایک کمپنی کا دعویٰ ہے کہ اس کی مصنوعات کی اوسط عمر 35000 میل ہے۔ 16 ٹائروں کا تصادفی نمونہ منتخب کیا گیا اور معلوم ہوا کہ اوسط عمر 34000 میل اور معیاری انحراف s = 2000 میل ہے۔ α = 0.05 پر متبادل $H_1:\\mu<35000$ کے مقابلے میں مفروضے $H_0:\\mu=35000$ کی جانچ کریں۔', 'د موټرو د ټایرونو جوړونکی یو شرکت ادعا کوي چې د هغه د محصول منځنی عمر 35000 میله دی. د 16 ټایرونو تصادفي نمونه وټاکل شوه او معلومه شوه چې منځنی عمر 34000 میله او معیاري انحراف s = 2000 میله دی. په α = 0.05 د بدیل $H_1:\\mu<35000$ پر وړاندې د $H_0:\\mu=35000$ فرضیه وازموئ.')
d.h(*SOL)
d.group('lines', [('i. $H_0:\\mu=35000$',) * 3, ('$H_1:\\mu<35000$',) * 3])
e76 = d.build('stat12-p126-example-7-6', 'Example 7.6 — tire life (start)', 'مثال 7.6 — ٹائر کی عمر (آغاز)', 'بېلګه 7.6 — د ټایر عمر (پیل)', 126, [244])
issues = [{'id': 'stat12-p244-t005', 'unit': 7, 'printedPage': 244, 'description': 'Example 7.5 prints “t_{0.05,(12−1)}” before correcting to t_{0.025,(11)} = 2.201, and “taken form a lot”; printed text retained.'}]

if __name__ == '__main__':
    save(126, [(7, st), (7, e75), (7, e76)], issues=issues)
