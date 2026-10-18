from stathelp import *
c=cell
U='dispersion-skewness-kurtosis'
E10='stat11-ex-3-10'; E11='stat11-ex-3-11'; E12='stat11-ex-3-12'
# ---------- scan 111 (printed 103) ----------
s=page(111,U,'103','Sample S.D (n − 1) · 3.5.2 Variance · Example 3.10','نمونے کا S.D (n − 1) · 3.5.2 تغیر · مثال 3.10','د نمونې S.D (n − 1) · 3.5.2 وریانس · بېلګه 3.10','sd-2')
Flow(s)
add(s,'c1','n – 1, i.e.','n – 1، یعنی','n – 1، یعنې',sourceGap=dict(note='Completes the sentence from the previous page ("…if the denominator in the sample formula is").'))
add(s,'smp','Sample standard deviation: (Statistic)','نمونے کا معیاری انحراف: (شماریہ)','د نمونې معیاري انحراف: (احصایه)')
head(s,'h352','3.5.2 Variance','3.5.2 تغیر','3.5.2 وریانس')
add(s,'t352','The term variance was introduced by R.A Fisher in 1918. It is denoted by σ² in population case and s² in sample case and is defined as the average of squared deviations of observations taken from mean is called variance. Mathematically;','تغیر کی اصطلاح آر۔اے۔ فشر نے 1918 میں متعارف کرائی۔ اسے آبادی کی صورت میں σ² اور نمونے کی صورت میں s² سے ظاہر کیا جاتا ہے اور اوسط سے لیے گئے مشاہدات کے مربع انحرافات کے اوسط کو تغیر کہتے ہیں۔ ریاضیاتی طور پر؛','د وریانس اصطلاح په 1918 کې R.A Fisher معرفي کړه. دا د ټولنې په حالت کې په σ² او د نمونې په حالت کې په s² ښودل کېږي او له اوسط څخه اخیستل شویو کتنو د مربع انحرافاتو اوسط ته وریانس ویل کېږي. ریاضیاتي ډول؛')
add(s,'pv','Population variance: (Parameter)','آبادی کا تغیر: (پیرامیٹر)','د ټولنې وریانس: (پارامېټر)')
add(s,'sv1','Sample variance: (Statistic)','نمونے کا تغیر: (شماریہ)','د نمونې وریانس: (احصایه)')
add(s,'sv2','Sample variance: (Statistic)','نمونے کا تغیر: (شماریہ)','د نمونې وریانس: (احصایه)')
add(s,'vm','Variance measures the average square distance from the mean.','تغیر اوسط سے اوسط مربع فاصلہ ناپتا ہے۔','وریانس له اوسط څخه اوسط مربع واټن اندازه کوي.')
head(s,'ex10','Example: 3.10','مثال: 3.10','بېلګه: 3.10',exampleId=E10)
add(s,'q10','Calculate standard deviation and variance for values of a population 1, 9, 5, 8, 7.','آبادی کی قدروں 1, 9, 5, 8, 7 کے لیے معیاری انحراف اور تغیر حساب کریں۔','د ټولنې د ارزښتونو 1, 9, 5, 8, 7 لپاره معیاري انحراف او وریانس محاسبه کړئ.',role='question',exampleId=E10)
head(s,'sol10','Solution:','حل:','حل:',exampleId=E10)
add(s,'i1','(i)','(i)','(i)',role='solution',exampleId=E10)
add(s,'i2','(ii)','(ii)','(ii)',role='solution',exampleId=E10)
add(s,'df','Standard deviation and variance can simply be defined as: S.D is the square root of the variance i.e. σ = √variance and variance is the square of the S.D i.e. σ² = (S.D)².','معیاری انحراف اور تغیر کو سادہ طور پر یوں بیان کیا جا سکتا ہے: S.D تغیر کا جذر ہے یعنی σ = √تغیر اور تغیر S.D کا مربع ہے یعنی σ² = (S.D)²۔','معیاري انحراف او وریانس په ساده توګه داسې تعریف کېدای شي: S.D د وریانس جذر دی یعنې σ = √وریانس او وریانس د S.D مربع دی یعنې σ² = (S.D)².')
s['tables']=[table('Example 3.10 solution table','مثال 3.10 کا حل: جدول','د بېلګې 3.10 د حل جدول',[c('x'),c('(x − μ)'),c('(x − μ)²')],[[c(str(a)),c(str(b)),c(str(d))] for a,b,d in [(1,-5,25),(9,3,9),(5,-1,1),(8,2,4),(7,1,1)]]+[[c('30'),c('0'),c('40')]],exampleId=E10)]
eq=[('a',r's=\sqrt{\dfrac{\sum(x-\bar{x})^2}{n-1}}\qquad\text{(Statistic)}','s = √(Σ(x − x̄)²/(n − 1))   (Statistic)',None),
 ('b',r'\sigma^2=\dfrac{\sum(x-\mu)^2}{N}\qquad\text{(Parameter)}','σ² = Σ(x − μ)²/N   (Parameter)',None),
 ('c',r's^2=\dfrac{\sum(x-\bar{x})^2}{n}\qquad\text{(Statistic)}','s² = Σ(x − x̄)²/n   (Statistic)',None),
 ('d',r's^2=\dfrac{\sum(x-\bar{x})^2}{n-1}\qquad\text{(Statistic)}','s² = Σ(x − x̄)²/(n − 1)   (Statistic)',None),
 ('e',r'\mu=\dfrac{\sum x}{N}=\dfrac{30}{5}=6','μ = Σx/N = 30/5 = 6',E10),
 ('f',r'\sigma=\sqrt{\dfrac{\sum(x-\mu)}{N}}=\sqrt{\dfrac{40}{5}}=2.83','σ = √(Σ(x − μ)/N) = √(40/5) = 2.83   [printed without the square on (x − μ)]',E10),
 ('g',r'\sigma^2=\dfrac{\sum(x-\mu)^2}{N}=\dfrac{40}{5}=8','σ² = Σ(x − μ)²/N = 40/5 = 8',E10)]
build(s,111,['c1','smp','E:a','h352','t352','pv','E:b','sv1','E:c','sv2','E:d','vm','ex10','q10','sol10','T:0','i1','E:e','E:f','i2','E:g','df'],eq)
s['sourceNote']='Printed page 103. In Example 3.10 the printed σ line omits the square on (x − μ) inside the root (kept as printed). The workings (i) and (ii) are printed beside the table and are shown after it. Margin pen marks are ignored. Header graphics and watermark excluded.'
s['vocabulary']={'population variance':dict(ur='آبادی کا تغیر',ps='د ټولنې وریانس'),'sample variance':dict(ur='نمونے کا تغیر',ps='د نمونې وریانس')}
save(s)
# ---------- scan 112 (printed 104) ----------
s=page(112,U,'104','3.5.3 Standard deviation and variance for ungrouped data · Example 3.11','3.5.3 غیر گروہی اعداد و شمار کے لیے معیاری انحراف اور تغیر کا حساب · مثال 3.11','3.5.3 د نه‌ګروپ شویو معلوماتو لپاره د معیاري انحراف او وریانس محاسبه · بېلګه 3.11','sd-3')
Flow(s)
head(s,'h353','3.5.3 Calculation of standard deviation and variance in case of ungrouped data','3.5.3 غیر گروہی اعداد و شمار کی صورت میں معیاری انحراف اور تغیر کا حساب','3.5.3 د نه‌ګروپ شویو معلوماتو په حالت کې د معیاري انحراف او وریانس محاسبه')
head(s,'ex11','Example: 3.11','مثال: 3.11','بېلګه: 3.11',exampleId=E11)
add(s,'q11','Compute standard deviation and variance for the sample 2, 4, 6, 8, 10.','نمونے 2, 4, 6, 8, 10 کے لیے معیاری انحراف اور تغیر حساب کریں۔','د نمونې 2, 4, 6, 8, 10 لپاره معیاري انحراف او وریانس محاسبه کړئ.',role='question',exampleId=E11)
head(s,'sol11','Solution:','حل:','حل:',exampleId=E11)
add(s,'m1','(i) By direct method','(i) براہِ راست طریقے سے','(i) په مستقیم طریقه',role='solution',exampleId=E11)
add(s,'m2','(ii) By shortcut method','(ii) مختصر طریقے سے','(ii) په لنډه طریقه',role='solution',exampleId=E11)
s['tables']=[table('Example 3.11: direct method table','مثال 3.11: براہِ راست طریقے کا جدول','بېلګه 3.11: د مستقیمې طریقې جدول',[c('x'),c('(x − x̄)'),c('(x − x̄)²')],[[c(str(a)),c(str(b)),c(str(d))] for a,b,d in [(2,-4,16),(4,-2,4),(6,0,0),(8,2,4),(10,4,16)]]+[[c('30'),c('0'),c('40')]],exampleId=E11)]
eq=[('a',r's=\sqrt{\dfrac{\sum(x-\bar{x})^2}{n-1}}','s = √(Σ(x − x̄)²/(n − 1))',E11),
 ('b',r's^2=\dfrac{\sum(x-\bar{x})^2}{n-1}','s² = Σ(x − x̄)²/(n − 1)',E11),
 ('c',r'\bar{x}=\dfrac{\sum x}{n}=\dfrac{30}{5}=6','x̄ = Σx/n = 30/5 = 6',E11),
 ('d',r'\therefore\ s=\sqrt{\dfrac{40}{5-1}}=\sqrt{\dfrac{40}{4}}=\sqrt{10}=3.16\qquad\text{(Absolute dispersion)}','∴ s = √(40/(5 − 1)) = √(40/4) = √10 = 3.16   (Absolute dispersion)   [minus sign in "5 – 1" not visible in the first root]',E11),
 ('e',r's^2=\dfrac{40}{5-1}=\dfrac{40}{4}=10','s² = 40/(5 − 1) = 40/4 = 10',E11),
 ('f',r'\text{Coefficient of S.D}=\dfrac{s}{\bar{x}}=\dfrac{3.16}{6}=0.53\qquad\text{(Relative dispersion)}','Coefficient of S.D = s/x̄ = 3.16/6 = 0.53   (Relative dispersion)',E11),
 ('g',r's=\sqrt{\dfrac{1}{n-1}\left[\sum x^2-\dfrac{\left(\sum x\right)^2}{n}\right]}','s = √((1/(n − 1))[Σx² − (Σx)²/n])',E11),
 ('h',r's^2=\dfrac{1}{n-1}\left[\sum x^2-\dfrac{\left(\sum x\right)^2}{n}\right]','s² = (1/(n − 1))[Σx² − (Σx)²/n]   [the printed form shows the numerator of the second term as "(Σ x²)"]',E11)]
build(s,112,['h353','ex11','q11','sol11','m1','E:a','E:b','T:0','E:c','E:d','E:e','E:f','m2','E:g','E:h'],eq)
s['sourceNote']='Printed page 104. The two direct-method formulas are printed side by side above the table and the two shortcut formulas side by side at the bottom; each is kept as its own equation in reading order. In the printed s² shortcut formula the second term appears as (Σx²)/n instead of (Σx)²/n; the correct form is shown and the misprint noted. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 113 (printed 105) ----------
s=page(113,U,'105','Example 3.11 (shortcut and step-deviation methods) · 3.5.4 Example 3.12 (start)','مثال 3.11 (مختصر اور قدمی انحراف کے طریقے) · 3.5.4 مثال 3.12 (آغاز)','بېلګه 3.11 (لنډه او ګام‌انحراف طریقې) · 3.5.4 بېلګه 3.12 (پیل)','sd-4')
Flow(s)
add(s,'n1','Now','اب','اوس',role='solution',exampleId=E11)
add(s,'n2','(iii) By change of origin and scale method or step-deviation method','(iii) مبدا اور پیمانے کی تبدیلی کے طریقے یا قدمی انحراف کے طریقے سے','(iii) د اصل او پیمانې د بدلون طریقې یا ګام‌انحراف طریقې په واسطه',role='solution',exampleId=E11)
add(s,'n3','Now','اب','اوس',role='solution',exampleId=E11)
add(s,'n4','Here a = 6, h = 2 ∴ u = (x − a)/h = (x − 6)/2','یہاں a = 6, h = 2 ∴ u = (x − a)/h = (x − 6)/2','دلته a = 6, h = 2 ∴ u = (x − a)/h = (x − 6)/2',role='solution',exampleId=E11)
head(s,'h354','3.5.4 Calculation of standard deviation and variance in case of discrete series or grouped data','3.5.4 منفصل سلسلے یا گروہی اعداد و شمار کی صورت میں معیاری انحراف اور تغیر کا حساب','3.5.4 د منفصلې لړۍ یا ګروپي معلوماتو په حالت کې د معیاري انحراف او وریانس محاسبه')
head(s,'ex12','Example: 3.12','مثال: 3.12','بېلګه: 3.12',exampleId=E12)
add(s,'q12','Compute standard deviation and variance from the following frequency','درج ذیل تعدد تقسیم سے معیاری انحراف اور تغیر حساب کریں','له لاندې فریکونسي ویش څخه معیاري انحراف او وریانس محاسبه کړئ',role='question',exampleId=E12,sourceGap=dict(note='The sentence continues on the next page ("distribution:").'))
s['tables']=[table('Example 3.11: x and x²','مثال 3.11: x اور x²','بېلګه 3.11: x او x²',[c('x'),c('x²')],[[c(str(a)),c(str(b))] for a,b in [(2,4),(4,16),(6,36),(8,64),(10,100)]]+[[c('30'),c('220')]],exampleId=E11),
 table('Example 3.11: step-deviation table','مثال 3.11: قدمی انحراف کا جدول','بېلګه 3.11: د ګام‌انحراف جدول',[c('x'),c('u = (x − 6)/2'),c('u²')],[[c(str(a)),c(str(b)),c(str(d))] for a,b,d in [(2,-2,4),(4,-1,1),(6,0,0),(8,1,1),(10,2,4)]]+[[c('–'),c('0'),c('10')]],exampleId=E11)]
eq=[('a',r's=\sqrt{\dfrac{1}{5-1}\left[220-\dfrac{(30)^2}{5}\right]}','s = √((1/(5 − 1))[220 − (30)²/5])   [printed "(30)2"]',E11),
 ('b',r'=\sqrt{\dfrac14[220-180]}=\sqrt{\dfrac{40}{4}}=\sqrt{10}=3.16','= √((1/4)[220 − 180]) = √(40/4) = √10 = 3.16',E11),
 ('c',r's^2=\dfrac{1}{5-5}\left[220-\dfrac{(30)^2}{5}\right]','s² = (1/(5 − 5))[220 − (30)²/5]   [printed "5 − 5", a misprint for 5 − 1]',E11),
 ('d',r'=\dfrac14[220-180]=\dfrac{40}{4}=10','= (1/4)[220 − 180] = 40/4 = 10',E11),
 ('e',r'S=\sqrt{\dfrac{\sum u^2}{n}-\left(\dfrac{\sum u}{n}\right)^2}\times h','S = √(Σu²/n − (Σu/n)²) × h',E11),
 ('f',r'S^2=\left[\dfrac{\sum u^2}{n}-\left(\dfrac{\sum u}{n}\right)^2\right]\times h^2','S² = [Σu²/n − (Σu/n)²] × h²',E11),
 ('g',r'\therefore\ S=\sqrt{\dfrac{10}{5}-\left(\dfrac{0}{5}\right)^2}\times 2=\sqrt{2-0}\times 2=3.16','∴ S = √(10/5 − (0/5)²) × 2 = √(2 − 0) × 2 = 3.16',E11),
 ('h',r'S^2=\left[\dfrac{10}{5}-\left(\dfrac{0}{5}\right)^2\right]\times 2^2=(2-0)\times 4=2\times 4=8','S² = [10/5 − (0/5)²] × 2² = (2 − 0) × 4 = 2 × 4 = 8',E11)]
build(s,113,['n1','T:0','E:a','E:b','E:c','E:d','n2','E:e','E:f','n3','T:1','n4','E:g','E:h','h354','ex12','q12'],eq)
s['sourceNote']='Printed page 105. The x, x² table and the "Now …" workings are printed side by side and are shown table first. Printed spellings kept: "origen". The step-deviation S² gives 8 (population form) while the direct method gave 10; as printed. In the u-table the first total cell is a dash. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 114 (printed 106) ----------
s=page(114,U,'106','Example 3.12: direct method · shortcut method formulas','مثال 3.12: براہِ راست طریقہ · مختصر طریقے کے فارمولے','بېلګه 3.12: مستقیم طریقه · د لنډې طریقې فورمولونه','sd-5')
Flow(s)
add(s,'c1','distribution:','تقسیم:','ویش:',role='question',exampleId=E12,sourceGap=dict(note='Completes the sentence from the previous page ("Compute standard deviation and variance from the following frequency").'))
head(s,'sol12','Solution:','حل:','حل:',exampleId=E12)
add(s,'m1','(i) By direct method','(i) براہِ راست طریقے سے','(i) په مستقیم طریقه',role='solution',exampleId=E12)
add(s,'m2','(ii) By shortcut method','(ii) مختصر طریقے سے','(ii) په لنډه طریقه',role='solution',exampleId=E12)
xs=[1,2,3,4,5]; fr=[5,10,15,12,8]; fx=[5,20,45,48,40]
dv=['-2.16','-1.16','-0.16','0.84','1.84']; sq=['4.6656','1.3456','0.0256','0.7056','3.386']; fs=['23.328','13.456','0.384','8.467','27.08']
s['tables']=[table('Example 3.12: x and f','مثال 3.12: x اور f','بېلګه 3.12: x او f',[c('x:')]+[c(str(v)) for v in xs],[[c('f:')]+[c(str(v)) for v in fr]],exampleId=E12),
 table('Example 3.12: direct method table','مثال 3.12: براہِ راست طریقے کا جدول','بېلګه 3.12: د مستقیمې طریقې جدول',[c('x'),c('f'),c('fx'),c('(x − x̄)'),c('(x − x̄)²'),c('f(x − x̄)²')],
 [[c(str(xs[i])),c(str(fr[i])),c(str(fx[i])),c(dv[i]),c(sq[i]),c(fs[i])] for i in range(5)]+[[c('Total','میزان','ټولیز'),c('50'),c('158'),c('–'),c('–'),c('72.72')]],exampleId=E12)]
eq=[('a',r'S=\sqrt{\dfrac{\sum f(x-\bar{x})^2}{\sum f}}','S = √(Σf(x − x̄)²/Σf)',E12),
 ('b',r'S^2=\dfrac{\sum f(x-\bar{x})^2}{\sum f}','S² = Σf(x − x̄)²/Σf',E12),
 ('c',r'\bar{x}=\dfrac{\sum fx}{\sum f}=\dfrac{158}{50}=3.16','x̄ = Σfx/Σf = 158/50 = 3.16   [printed "fx/f"]',E12),
 ('d',r'S=\sqrt{\dfrac{72.72}{50}}=\sqrt{1.4544}=1.21\qquad\text{(Absolute dispersion)}','S = √(72.72/50) = √1.4544 = 1.21   (Absolute dispersion)',E12),
 ('e',r'S^2=\dfrac{72.72}{50}=1.4545','S² = 72.72/50 = 1.4545',E12),
 ('f',r'\text{Coefficient of S.D}=\dfrac{S}{\bar{x}}=\dfrac{1.22}{3.16}=0.39\qquad\text{(Relative dispersion)}','Coefficient of S.D = S/x̄ = 1.22/3.16 = 0.39   (Relative dispersion)   [printed 1.22]',E12),
 ('g',r'S=\sqrt{\dfrac{\sum fx^2}{\sum f}-\left(\dfrac{\sum fx}{\sum f}\right)^2}','S = √(Σfx²/Σf − (Σfx/Σf)²)',E12),
 ('h',r'S^2=\dfrac{\sum fx^2}{\sum f}-\left(\dfrac{\sum fx}{\sum f}\right)^2','S² = Σfx²/Σf − (Σfx/Σf)²',E12)]
build(s,114,['c1','T:0','sol12','m1','E:a','E:b','T:1','E:c','E:d','E:e','E:f','m2','E:g','E:h'],eq)
s['sourceNote']='Printed page 106. The x and f rows continue the question of Example 3.12 and are shown as a table. The printed 1.4544 and 1.4545 differ slightly, and the printed coefficient uses 1.22 for S (S = 1.21 above); all kept as printed. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
