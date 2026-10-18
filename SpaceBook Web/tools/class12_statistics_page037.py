"""PDF37 printed 65–66: Exercise 2.3 MCQs (i)–(x), questions 2.4–2.6."""
from class12_statistics_common import Builder, save

b = Builder()
b.h('2.3 Select the correct answer out of the given ones.', '2.3 دیے گئے جوابات میں سے درست جواب منتخب کریں۔', '2.3 له ورکړل شویو ځوابونو څخه سم ځواب وټاکئ.')
DIS = ('discrete random variable', 'منفصل تصادفی متغیر', 'منفصل تصادفي متغیر')
CON = ('continuous random variable', 'مسلسل تصادفی متغیر', 'متصل تصادفي متغیر')
b.mcq('(i)', ('The height of persons in a country is', 'کسی ملک میں افراد کا قد ہے', 'په یوه هېواد کې د خلکو قد دی'),
      [DIS, CON, ('both discrete and continuous', 'منفصل اور مسلسل دونوں', 'منفصل او متصل دواړه'), ('neither discrete nor continuous', 'نہ منفصل نہ مسلسل', 'نه منفصل او نه متصل')])
b.mcq('(ii)', ('The outcomes of tossing a coin three times is a variable of the type', 'سکہ تین بار اچھالنے کے نتائج اس قسم کا متغیر ہیں', 'د سکې درې ځله اچولو پایلې د دې ډول متغیر دی'),
      [('continuous', 'مسلسل', 'متصل'), ('discrete', 'منفصل', 'منفصل'), ('neither discrete not continuous', 'نہ منفصل نہ مسلسل', 'نه منفصل او نه متصل'), ('both discrete and continuous', 'منفصل اور مسلسل دونوں', 'منفصل او متصل دواړه')])
b.mcq('(iii)', ('If $f(x)=kx$, $0<x<1$, then value of k is', 'اگر $f(x)=kx$، $0<x<1$ ہو تو k کی قیمت ہے', 'که $f(x)=kx$، $0<x<1$ وي، نو د k قیمت دی'), ['$\\frac{1}{3}$', '2', '$\\frac{1}{2}$', '1'])
b.mcq('(iv)', ('If $V(X)=2$ then $V(2X+5)$ is equal to', 'اگر $V(X)=2$ ہو تو $V(2X+5)$ برابر ہے', 'که $V(X)=2$ وي، نو $V(2X+5)$ برابر دی له'), ['4', '2', '8', '6'])
b.mcq('(v)', ('If $E(X)=4$ then $E[3X+10]$ is', 'اگر $E(X)=4$ ہو تو $E[3X+10]$ ہے', 'که $E(X)=4$ وي، نو $E[3X+10]$ دی'), ['10', '13', '4', '22'])
b.mcq('(vi)', ('If $E(X)=\\frac{2}{3}$, $E(X^2)=\\frac{8}{9}$ then S.D of X is', 'اگر $E(X)=\\frac{2}{3}$، $E(X^2)=\\frac{8}{9}$ ہو تو X کا معیاری انحراف ہے', 'که $E(X)=\\frac{2}{3}$، $E(X^2)=\\frac{8}{9}$ وي، نو د X معیاري انحراف دی'),
      ['$\\frac{4}{9}$', '$\\frac{9}{4}$', '$\\frac{2}{3}$', '$\\frac{2}{9}$'])
b.mcq('(vii)', ('If $f(x,y)=f(x)\\,f(y)$, it means variables are', 'اگر $f(x,y)=f(x)\\,f(y)$ ہو تو اس کا مطلب ہے کہ متغیرات ہیں', 'که $f(x,y)=f(x)\\,f(y)$ وي، مانا یې دا ده چې متغیرونه دي'),
      [('correlated', 'باہم مربوط', 'سره تړلي (correlated)'), ('dependent', 'تابع', 'تړلي'), ('independent', 'آزاد', 'خپلواک'), ('associated', 'متعلق', 'اړونده')])
b.mcq('(viii)', ('If X and Y are independent random variables then $V(X-Y)=$', 'اگر X اور Y آزاد تصادفی متغیرات ہوں تو $V(X-Y)=$', 'که X او Y خپلواک تصادفي متغیرونه وي، نو $V(X-Y)=$'),
      ['$V(X)-V(Y)$', '$V(X)+V(Y)$', '$V(X)\\,V(Y)$', '$V(X+Y)$'])
b.mcq('(ix)', ('continuous probability distributions give', 'مسلسل احتمالی تقسیمیں دیتی ہیں', 'متصل احتمالي وېشونه ورکوي'),
      [('interval probability', 'وقفے کا احتمال', 'د واټن احتمال'), ('point probability', 'نقطے کا احتمال', 'د ټکي احتمال'), ('negative probability', 'منفی احتمال', 'منفي احتمال'), ('zero probability', 'صفر احتمال', 'صفر احتمال')])
b.mcq('(x)', ('if X is a random variable having its pdf, the E(X) is called', 'اگر X ایک تصادفی متغیر ہو جس کا pdf ہو تو E(X) کہلاتا ہے', 'که X یو تصادفي متغیر وي چې pdf ولري، نو E(X) بلل کېږي'),
      [('median', 'وسطانیہ', 'منځنۍ (median)'), ('geometric mean', 'جیومیٹرک اوسط', 'هندسي منځنی'), ('mode', 'عادہ (mode)', 'مود'), ('arithmetic mean', 'حسابی اوسط', 'حسابي منځنی')])
b.group('lines', [
    ('2.4 Describe the concept of a random variable and give its examples.', '2.4 تصادفی متغیر کا تصور بیان کریں اور اس کی مثالیں دیں۔', '2.4 د تصادفي متغیر مفهوم بیان کړئ او بېلګې یې ورکړئ.'),
    ('2.5 Explain different types of a random variable with examples.', '2.5 تصادفی متغیر کی مختلف اقسام مثالوں کے ساتھ واضح کریں۔', '2.5 د تصادفي متغیر بېلابېل ډولونه له بېلګو سره تشریح کړئ.'),
    ('2.6 Classify each of the following random variables as either discrete or continuous:', '2.6 درج ذیل تصادفی متغیرات میں سے ہر ایک کو منفصل یا مسلسل کے طور پر درجہ بند کریں:', '2.6 لاندې هر تصادفي متغیر د منفصل یا متصل په توګه ډلبندي کړئ:'),
])
b.group('lines', [
    ('i. Time to failure for an electronic system.', 'i. کسی الیکٹرانک نظام کے ناکارہ ہونے تک کا وقت۔', 'i. د یوه برېښنايي سیستم تر خرابېدو پورې وخت.'),
    ('ii. The height of a person.', 'ii. کسی شخص کا قد۔', 'ii. د یوه کس قد.'),
    ('iii. The number of questions asked in an oral examination.', 'iii. زبانی امتحان میں پوچھے گئے سوالات کی تعداد۔', 'iii. په شفاهي ازموینه کې د پوښتل شویو پوښتنو شمېر.'),
    ('iv. Temperature at a place.', 'iv. کسی جگہ کا درجۂ حرارت۔', 'iv. په یوه ځای کې تودوخه.'),
    ('v. The maximum breaking strength 250 kg of a wire.', 'v. کسی تار کی زیادہ سے زیادہ توڑنے کی طاقت 250 kg۔', 'v. د یوه تار د ماتېدو اعظمي ځواک 250 kg.'),
    ('vi. The number of fatal traffic accident per month on the motor way.', 'vi. موٹر وے پر فی ماہ مہلک ٹریفک حادثات کی تعداد۔', 'vi. په موټروې د هرې میاشتې د وژونکو ترافیکي پېښو شمېر.'),
    ('vii. The life time of a mobile set.', 'vii. موبائل سیٹ کی عمر۔', 'vii. د موبایل عمر.'),
    ('viii. The amount of rainfall at Islamabad during different months of 2016.', 'viii. 2016 کے مختلف مہینوں میں اسلام آباد میں بارش کی مقدار۔', 'viii. د 2016 په بېلابېلو میاشتو کې په اسلام اباد کې د باران اندازه.'),
    ('ix. The number of admitted patients in a hospital in a year.', 'ix. ایک سال میں کسی ہسپتال میں داخل مریضوں کی تعداد۔', 'ix. په یوه کال کې په یوه روغتون کې د بستر شویو ناروغانو شمېر.'),
    ('x. The number of Mosque per village in a district.', 'x. کسی ضلع میں فی گاؤں مساجد کی تعداد۔', 'x. په یوه ولسوالۍ کې په هر کلي کې د جوماتونو شمېر.'),
])
rec = b.build('stat12-u2-exercise-b', 'Unit 2 Exercise — 2.3 to 2.6', 'یونٹ 2 مشق — 2.3 تا 2.6', 'واحد 2 تمرین — 2.3 تر 2.6', 37, [65, 66])
issues = [{'id': 'stat12-p66-qnumbers-margin', 'unit': 2, 'printedPage': 66, 'description': 'Question numbers 2.4–2.6 are printed in the gutter of the facing page and are clipped in the scan; they are restored from their position.'}]

if __name__ == '__main__':
    save(37, [(2, rec)], issues=issues)
