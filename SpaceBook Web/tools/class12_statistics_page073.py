"""PDF73 printed 137–138: Example 4.11 end (2266 lamps); Examples 4.12–4.13 (standard scores); 4.2.9 ordinates of the standard Normal distribution."""
from class12_statistics_common import Builder, save

SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.mlines([r'=P[0<Z<\infty]-P[0<Z<0.75]', r'=0.5-0.2734=0.2266'])
b.p('Thus, the number of lamps that is expected to burn for more than 2000 hours is $N\\,f(x)=10{,}000\\,(0.2266)=2266$.', 'لہٰذا 2000 گھنٹے سے زیادہ جلنے والے متوقع بلبوں کی تعداد $N\\,f(x)=10{,}000\\,(0.2266)=2266$ ہے۔', 'نو د هغو ګروپونو شمېر چې تمه کېږي له 2000 ساعتونو زیات وسوځي $N\\,f(x)=10{,}000\\,(0.2266)=2266$ دی.')
b.h('Example 4.12', 'مثال 4.12', 'بېلګه 4.12')
b.p('In a statistics examination, the mean score of students was 78 marks and the standard deviation was 10 marks.', 'شماریات کے ایک امتحان میں طلبہ کا اوسط اسکور 78 نمبر اور معیاری انحراف 10 نمبر تھا۔', 'د احصایې په یوه ازموینه کې د زده کوونکو منځنۍ نمره 78 او معیاري انحراف 10 نمرې وو.')
b.group('lines', [
    ('a) Determine the standard scores of students receiving marks: i) 70 ii) 83 iii) 92.', 'a) ان طلبہ کے معیاری اسکور معلوم کریں جنہوں نے یہ نمبر حاصل کیے: i) 70 ii) 83 iii) 92۔', 'a) د هغو زده کوونکو معیاري نمرې وټاکئ چې دا نمرې یې اخیستې: i) 70 ii) 83 iii) 92.'),
    ('b) Find the marks corresponding to the standard scores: i) −1 ii) 1.6.', 'b) معیاری اسکور کے مطابق نمبر معلوم کریں: i) −1 ii) 1.6۔', 'b) د معیاري نمرو سره سمې نمرې پیدا کړئ: i) −1 ii) 1.6.'),
])
b.h(*SOL)
b.p('Given $\\mu=78$, $\\sigma=10$', 'دیا گیا ہے $\\mu=78$، $\\sigma=10$', 'ورکړل شوي $\\mu=78$، $\\sigma=10$')
b.p('(a) X-values are given and we need to find Z-values:', '(a) X کی قیمتیں دی گئی ہیں اور ہمیں Z کی قیمتیں معلوم کرنی ہیں:', '(a) د X قیمتونه ورکړل شوي او موږ باید د Z قیمتونه پیدا کړو:')
b.mlines([r'i)\quad Z=\frac{X-\mu}{\sigma}=\frac{70-78}{10}=\frac{-8}{10}=-0.8', r'ii)\quad Z=\frac{X-\mu}{\sigma}=\frac{83-78}{10}=\frac{5}{10}=0.5', r'iii)\quad Z=\frac{X-\mu}{\sigma}=\frac{92-78}{10}=\frac{14}{10}=1.4'])
b.p('(b) Z-values are given and X-values are required, we know that', '(b) Z کی قیمتیں دی گئی ہیں اور X کی قیمتیں درکار ہیں، ہم جانتے ہیں کہ', '(b) د Z قیمتونه ورکړل شوي او د X قیمتونو ته اړتیا ده، پوهېږو چې')
b.mlines([r'Z=\frac{X-\mu}{\sigma},\Rightarrow X=\mu+z\sigma', r'(i)\quad X=78+(-1)10=78-10=68', r'(ii)\quad X=78+(1.6)10=78+16=94'])
ex = b.build('stat12-p073-examples-4-11-4-12', 'Example 4.11 result; Example 4.12 standard scores', 'مثال 4.11 کا نتیجہ؛ مثال 4.12 معیاری اسکور', 'د بېلګې 4.11 پایله؛ بېلګه 4.12 معیاري نمرې', 73, [137])

c = Builder()
c.h('Example 4.13', 'مثال 4.13', 'بېلګه 4.13')
c.p('Two students A and B were informed that they received standard scores of −1 and 1.6 respectively on a multiple choice examination in Mathematics. If their marks are 68 and 94 respectively, find the mean and standard deviation of the examination marks.',
    'دو طلبہ A اور B کو بتایا گیا کہ ریاضی کے کثیر انتخابی امتحان میں ان کے معیاری اسکور بالترتیب −1 اور 1.6 ہیں۔ اگر ان کے نمبر بالترتیب 68 اور 94 ہوں تو امتحانی نمبروں کا اوسط اور معیاری انحراف معلوم کریں۔',
    'دوو زده کوونکو A او B ته وویل شول چې د ریاضي په څو ځوابه ازموینه کې یې معیاري نمرې په ترتیب سره −1 او 1.6 دي. که نمرې یې په ترتیب سره 68 او 94 وي، د ازموینې د نمرو منځنی او معیاري انحراف پیدا کړئ.')
c.h(*SOL)
c.p('We know that, $Z=\\frac{X-\\mu}{\\sigma}\\Rightarrow X=\\mu+Z\\sigma$', 'ہم جانتے ہیں کہ $Z=\\frac{X-\\mu}{\\sigma}\\Rightarrow X=\\mu+Z\\sigma$', 'پوهېږو چې $Z=\\frac{X-\\mu}{\\sigma}\\Rightarrow X=\\mu+Z\\sigma$')
c.p('Putting values for student A $\\quad 68=\\mu+(-1)\\sigma$', 'طالب علم A کے لیے قیمتیں رکھنے سے $\\quad 68=\\mu+(-1)\\sigma$', 'د زده کوونکي A لپاره قیمتونه ایښودو سره $\\quad 68=\\mu+(-1)\\sigma$')
c.eq(r'68=\mu-\sigma\qquad(i)')
c.p('student B $\\quad 94=\\mu+1.6\\sigma\\qquad(ii)$', 'طالب علم B $\\quad 94=\\mu+1.6\\sigma\\qquad(ii)$', 'زده کوونکی B $\\quad 94=\\mu+1.6\\sigma\\qquad(ii)$')
c.p('Subtracting equation (i) from equation (ii)', 'مساوات (ii) میں سے مساوات (i) تفریق کرنے سے', 'له (ii) معادلې څخه د (i) معادلې تفریق کولو سره')
c.mlines([r'26=2.6\sigma', r'\sigma=\frac{26}{2.6}=10'])
c.p('Putting value of σ in eq (1) we get', 'مساوات (1) میں σ کی قیمت رکھنے سے', 'په (1) معادله کې د σ قیمت ایښودو سره')
c.eq(r'68=\mu-10\Rightarrow\mu=78')
c.p('Therefore the mean and standard deviation are μ=78 and σ=10.', 'لہٰذا اوسط اور معیاری انحراف μ=78 اور σ=10 ہیں۔', 'نو منځنی او معیاري انحراف μ=78 او σ=10 دي.')
c.h('4.2.9 Ordinates of the standard Normal distribution', '4.2.9 معیاری نارمل تقسیم کے ordinates', '4.2.9 د معیاري نورمال وېش اورډیناټونه')
c.p('Ordinates mean heights of the standard normal curve corresponding to a specified Z-value. It is denoted by f(z) and is obtained by using the function', 'Ordinates سے مراد کسی مخصوص Z قیمت کے مطابق معیاری نارمل منحنی کی بلندیاں ہیں۔ اسے f(z) سے ظاہر کرتے ہیں اور یہ اس تفاعل سے حاصل ہوتا ہے', 'اورډیناټونه د یوه ټاکلي Z قیمت سره سم د معیاري نورمال منحني لوړوالي ته وایي. په f(z) ښودل کېږي او له دې تابع څخه لاسته راځي')
c.eq(r'f(z)=\frac{1}{\sqrt{2\pi}}e^{-\frac{z^2}{2}},\qquad -\infty\le Z\le\infty')
c.p('Fisher and Yates have computed ordinates for different positive values of z and presented them in tabular form as shown in table 4.2. It is important to note that the ordinates at negative values of Z equal to the ordinates at positive values of Z due to unique property of symmetry of the Normal distribution.',
    'فشر اور یٹس نے z کی مختلف مثبت قیمتوں کے لیے ordinates معلوم کیے اور انہیں جدولی شکل میں پیش کیا جیسا کہ جدول 4.2 میں دکھایا گیا ہے۔ یہ نوٹ کرنا اہم ہے کہ نارمل تقسیم کی تشاکل کی منفرد خاصیت کی وجہ سے Z کی منفی قیمتوں پر ordinates، Z کی مثبت قیمتوں پر ordinates کے برابر ہوتے ہیں۔',
    'فیشر او یېټس د z د بېلابېلو مثبتو قیمتونو لپاره اورډیناټونه محاسبه کړي او په جدولي بڼه یې وړاندې کړي لکه څنګه چې په 4.2 جدول کې ښودل شوي. دا یادونه مهمه ده چې د نورمال وېش د تناظر د ځانګړې ځانګړنې له امله د Z په منفي قیمتونو کې اورډیناټونه د Z په مثبتو قیمتونو کې له اورډیناټونو سره برابر دي.')
ex13 = c.build('stat12-p073-example-4-13-ordinates', 'Example 4.13 and 4.2.9 ordinates of the standard normal curve', 'مثال 4.13 اور 4.2.9 معیاری نارمل منحنی کے ordinates', 'بېلګه 4.13 او 4.2.9 د معیاري نورمال منحني اورډیناټونه', 73, [138])

if __name__ == '__main__':
    save(73, [(4, ex), (4, ex13)])
