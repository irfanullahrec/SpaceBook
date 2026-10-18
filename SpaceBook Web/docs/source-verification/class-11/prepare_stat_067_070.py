from statlib import *
c=cell
U='central-tendency'
def pid(n,k): return f'stat11-s{n:03}-{k}'
def rt(rows,w=None): return [[c(x) for x in r] for r in rows]
# ---------- scan 67 (printed 59) ----------
s=page(67,U,'59','Example 2.5 (continued): direct, shortcut and step-deviation methods','مثال 2.5 (جاری): براہِ راست، مختصر اور گام انحراف طریقے','بېلګه 2.5 (دوام): مستقیمه، لنډه او ګام‌انحراف طریقې','example25-methods')
F=Flow(s)
F.e('d',r'\therefore\ \bar{x}=\dfrac{\sum fx}{\sum f}=\dfrac{528}{30}=17.6','∴ x̄ = Σfx / Σf = 528/30 = 17.6',exampleId='stat11-ex-2-5')
head(s,'hii','(ii) By shortcut method','(ii) مختصر طریقے سے','(ii) په لنډه طریقه',exampleId='stat11-ex-2-5')
F.rest()
F.e('sc',r'\bar{x}=A+\dfrac{\sum fD}{\sum f}','x̄ = A + ΣfD / Σf',exampleId='stat11-ex-2-5')
s['tables']=[table('Example 2.5: shortcut method (D = x − 18)','مثال 2.5: مختصر طریقہ (D = x − 18)','بېلګه 2.5: لنډه طریقه (D = x − 18)',[c('x'),c('f'),c('D = x − 18'),c('fD')],[[c('12'),c('1'),c('12 − 18 = −6'),c('−6')],[c('14'),c('4'),c('−4'),c('−16')],[c('16'),c('6'),c('−2'),c('−12')],[c('18'),c('10'),c('0'),c('0')],[c('20'),c('7'),c('2'),c('14')],[c('22'),c('2'),c('4'),c('8')],[c('Total','کل','ټول'),c('30'),c('−'),c('−12')]],exampleId='stat11-ex-2-5',role='solution'),
 table('Example 2.5: step-deviation method (u = (x − 18)/2)','مثال 2.5: گام انحراف طریقہ (u = (x − 18)/2)','بېلګه 2.5: ګام‌انحراف طریقه (u = (x − 18)/2)',[c('x'),c('f'),c('u = (x − 18)/2'),c('fu')],[[c('12'),c('1'),c('−3'),c('−3')],[c('14'),c('4'),c('−2'),c('−8')],[c('16'),c('6'),c('−1'),c('−6')],[c('18'),c('10'),c('0'),c('0')],[c('20'),c('7'),c('1'),c('7')],[c('22'),c('2'),c('2'),c('4')],[c('Total','کل','ټول'),c('30'),c('−'),c('−6')]],exampleId='stat11-ex-2-5',role='solution')]
F.rest();F.tb(0)
add(s,'t1','We take A = 18 because it has maximum frequency','ہم A = 18 لیتے ہیں کیونکہ اس کا تعدد زیادہ سے زیادہ ہے','موږ A = 18 اخلو ځکه چې فریکونسي یې اعظمي ده',role='solution',exampleId='stat11-ex-2-5')
F.rest()
F.e('e2',r'\therefore\ \bar{x}=A+\dfrac{\sum fD}{\sum f}=18+\dfrac{(-12)}{30}=18-0.4=17.6','∴ x̄ = A + ΣfD / Σf = 18 + (−12)/30 = 18 − 0.4 = 17.6',exampleId='stat11-ex-2-5')
head(s,'hiii','(iii) By change of origin and scale or step-deviation method','(iii) مبدا اور پیمانے کی تبدیلی یا گام انحراف طریقے سے','(iii) د اصل او پیمانې په بدلون یا ګام‌انحراف طریقه',exampleId='stat11-ex-2-5')
F.rest()
F.e('sd',r'\bar{x}=A+\dfrac{\sum fu}{\sum f}\times h','x̄ = A + (Σfu / Σf) × h',exampleId='stat11-ex-2-5')
F.rest();F.tb(1)
F.done()
s['sourceNote']='Printed page 59. The page-number badge at the foot is partly cut off by the scan. The printed text uses "D" with a space in fD. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 68 (printed 60) ----------
s=page(68,U,'60','Example 2.5 (end) · 2.2.3 Continuous grouped data · Example 2.6','مثال 2.5 (اختتام) · 2.2.3 مسلسل گروہی اعداد و شمار · مثال 2.6','بېلګه 2.5 (پای) · 2.2.3 دوامداره ګروپي معلومات · بېلګه 2.6','continuous-grouped-1')
F=Flow(s)
F.e('c1',r'\text{A}=18,\ h=2','A = 18, h = 2',exampleId='stat11-ex-2-5')
F.e('c2',r'\text{Therefore, }\bar{x}=A+\dfrac{\sum fu}{\sum f}\times h=18+\dfrac{(-6)}{30}\cdot2=18-\dfrac{12}{30}=18-0.4=17.6','Therefore, x̄ = A + (Σfu / Σf) × h = 18 + (−6)/30 · 2 = 18 − 12/30 = 18 − 0.4 = 17.6',exampleId='stat11-ex-2-5')
head(s,'h223','2.2.3 Calculation of arithmetic mean in case of continuous grouped data','2.2.3 مسلسل گروہی اعداد و شمار کی صورت میں حسابی اوسط کا حساب','2.2.3 د دوامداره ګروپي معلوماتو په حالت کې د حسابي اوسط محاسبه')
add(s,'t223','Compute midpoints (x) for the classes. Formulae and calculation procedure is same as used in case of discrete series.','جماعتوں کے وسطی نقاط (x) حساب کریں۔ فارمولے اور حساب کا طریقہ وہی ہے جو منفصل سلسلے کی صورت میں استعمال ہوتا ہے۔','د ټولګیو منځنۍ نقطې (x) محاسبه کړئ. فورمولونه او د محاسبې طریقه هماغه ده چې د منفصلې لړۍ په حالت کې کارول کېږي.')
head(s,'ex6','Example: 2.6:','مثال: 2.6:','بېلګه: 2.6:',exampleId='stat11-ex-2-6')
add(s,'q6','The heights of 100 college students measured to nearest inch are given in the following table','100 کالج طلبہ کے قد، جو قریب ترین انچ تک ناپے گئے ہیں، درج ذیل جدول میں دیے گئے ہیں','د 100 کالج زده کوونکو قدونه، چې نږدې انچ ته اندازه شوي، په لاندې جدول کې ورکړل شوي',role='question',exampleId='stat11-ex-2-6')
add(s,'q6b','Calculate the arithmetic mean.','حسابی اوسط حساب کریں۔','حسابي اوسط محاسبه کړئ.',role='question',exampleId='stat11-ex-2-6')
head(s,'sol6','Solution:','حل:','حل:',exampleId='stat11-ex-2-6')
add(s,'i6','(i) By direct method','(i) براہِ راست طریقے سے','(i) په مستقیمه طریقه',role='solution',exampleId='stat11-ex-2-6')
add(s,'ii6','(ii) By shortcut method','(ii) مختصر طریقے سے','(ii) په لنډه طریقه',role='solution',exampleId='stat11-ex-2-6')
s['tables']=[table('Example 2.6: heights of 100 college students','مثال 2.6: 100 کالج طلبہ کے قد','بېلګه 2.6: د 100 کالج زده کوونکو قدونه',[c('Height (inches):','قد (انچ):','قد (انچ):')]+[c(v) for v in ['60 – 62','63 – 65','66 – 68','69 – 71','72 – 74']],[[c('Number of students:','طلبہ کی تعداد:','د زده کوونکو شمېر:')]+[c(str(v)) for v in [5,18,42,27,8]]],exampleId='stat11-ex-2-6'),
 table('Example 2.6: direct method','مثال 2.6: براہِ راست طریقہ','بېلګه 2.6: مستقیمه طریقه',[c('Heights','قد','قدونه'),c('f'),c('x'),c('fx')],[[c(a),c(b),c(d),c(e)] for a,b,d,e in [('60 – 62','5','61','305'),('63 – 65','18','64','1152'),('66 – 68','42','67','2814'),('69 – 71','27','70','1890'),('72 – 74','8','73','584')]]+[[c('Total','کل','ټول'),c('100'),c(''),c('6745')]],exampleId='stat11-ex-2-6',role='solution')]
ids=[p['id'] for p in s['paras']]
F.rest()
s['flow']=[dict(type='equation',index=0),dict(type='equation',index=1),dict(type='paragraphs',ids=[pid(68,'h223'),pid(68,'t223'),pid(68,'ex6'),pid(68,'q6')]),dict(type='table',index=0),dict(type='paragraphs',ids=[pid(68,'q6b'),pid(68,'sol6'),pid(68,'i6')])]
s['equations'].append(eqn(68,'dm',r'\bar{x}=\dfrac{\sum fx}{\sum f}','x̄ = Σfx / Σf',exampleId='stat11-ex-2-6'))
s['equations'].append(eqn(68,'dm2',r'\bar{x}=\dfrac{\sum fx}{\sum f}=\dfrac{6745}{100}=67.45','x̄ = Σfx / Σf = 6745/100 = 67.45',exampleId='stat11-ex-2-6'))
s['equations'].append(eqn(68,'sc',r'\bar{x}=A+\dfrac{\sum fD}{\sum f}','x̄ = A + ΣfD / Σf',exampleId='stat11-ex-2-6'))
s['flow']+=[dict(type='equation',index=2),dict(type='table',index=1),dict(type='equation',index=3),dict(type='paragraphs',ids=[pid(68,'ii6')]),dict(type='equation',index=4)]
s['sourceNote']='Printed page 60. The first two lines complete Example 2.5 from the previous page. The data lines of Example 2.6 (Height / Number of students) are printed as text lines and kept as a one-row table. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 69 (printed 61) ----------
s=page(69,U,'61','Example 2.6 (continued) · Examples 2.7, 2.8','مثال 2.6 (جاری) · مثالیں 2.7، 2.8','بېلګه 2.6 (دوام) · بېلګې 2.7، 2.8','example26-28')
F=Flow(s)
s['tables']=[table('Example 2.6: shortcut method (D = x − 67)','مثال 2.6: مختصر طریقہ (D = x − 67)','بېلګه 2.6: لنډه طریقه (D = x − 67)',[c('Heights','قد','قدونه'),c('f'),c('x'),c('D = x − 67'),c('fD')],[[c(a),c(b),c(d),c(e),c(f)] for a,b,d,e,f in [('60 – 62','5','61','− 6','−30'),('63 – 65','18','64','− 3','−54'),('66 – 68','42','67','0','0'),('69 – 71','27','70','3','81'),('72 – 74','8','73','6','48')]]+[[c('Total','کل','ټول'),c('100'),c(''),c(''),c('45')]],exampleId='stat11-ex-2-6',role='solution'),
 table('Example 2.6: step-deviation method (u = (x − 67)/3)','مثال 2.6: گام انحراف طریقہ (u = (x − 67)/3)','بېلګه 2.6: ګام‌انحراف طریقه (u = (x − 67)/3)',[c('Heights','قد','قدونه'),c('f'),c('x'),c('u = (x − 67)/3'),c('fu')],[[c(a),c(b),c(d),c(e),c(f)] for a,b,d,e,f in [('60 – 62','5','61','− 2','− 10'),('63 – 65','18','64','−1','−18'),('66 – 68','42','67','0','0'),('69 – 71','27','70','1','27'),('72 – 74','8','73','2','16')]]+[[c('Total','کل','ټول'),c('100'),c('-'),c('-'),c('15')]],exampleId='stat11-ex-2-6',role='solution')]
F.tb(0)
add(s,'n1','A = 67 because it has highest frequency.','A = 67 کیونکہ اس کا تعدد سب سے زیادہ ہے۔','A = 67 ځکه چې فریکونسي یې تر ټولو لوړه ده.',role='solution',exampleId='stat11-ex-2-6')
F.rest()
F.e('e1',r'\bar{x}=A+\dfrac{\sum fD}{\sum f}=67+\dfrac{45}{100}=67+0.45=67.45','x̄ = A + ΣfD / Σf = 67 + 45/100 = 67 + 0.45 = 67.45',exampleId='stat11-ex-2-6')
add(s,'i3','(iii) By change of origin and scale or step deviation method','(iii) مبدا اور پیمانے کی تبدیلی یا گام انحراف طریقے سے','(iii) د اصل او پیمانې په بدلون یا ګام‌انحراف طریقه',role='solution',exampleId='stat11-ex-2-6')
F.rest()
F.e('sd',r'\bar{x}=A+\dfrac{\sum fu}{\sum f}\times h','x̄ = A + (Σfu / Σf) × h',exampleId='stat11-ex-2-6')
F.tb(1)
add(s,'n2','Here A = 67 and h = 3','یہاں A = 67 اور h = 3','دلته A = 67 او h = 3',role='solution',exampleId='stat11-ex-2-6')
F.rest()
F.e('e2',r'\therefore\ \bar{x}=A+\dfrac{\sum fu}{\sum f}\times h=67+\dfrac{15}{100}\times3=67+\dfrac{45}{100}=67+0.45=67.45','∴ x̄ = A + (Σfu / Σf) × h = 67 + (15/100) × 3 = 67 + 45/100 = 67 + 0.45 = 67.45',exampleId='stat11-ex-2-6')
head(s,'ex7','Example: 2.7','مثال: 2.7','بېلګه: 2.7',exampleId='stat11-ex-2-7')
add(s,'q7','A population with mean μ = 10 has Σx = 250. How many observations are in the population?','ایک مجموعے کا اوسط μ = 10 ہے اور Σx = 250 ہے۔ مجموعے میں کتنے مشاہدات ہیں؟','یوه ټولنه چې اوسط یې μ = 10 دی او Σx = 250 لري. په ټولنه کې څومره کتنې دي؟',role='question',exampleId='stat11-ex-2-7')
head(s,'sol7','Solution:','حل:','حل:',exampleId='stat11-ex-2-7')
add(s,'d7','By definition','تعریف کے مطابق','د تعریف له مخې',role='solution',exampleId='stat11-ex-2-7')
F.rest()
F.e('e7a',r'\mu=\dfrac{\sum x}{N}','μ = Σx / N',exampleId='stat11-ex-2-7')
F.e('e7b',r'\text{Here }10=\dfrac{250}{N}\ \text{ or }\ 10N=250\ \Rightarrow\ N=\dfrac{250}{10}=25\ \text{observations.}','Here 10 = 250/N or 10N = 250 ⇒ N = 250/10 = 25 observations.',exampleId='stat11-ex-2-7')
head(s,'ex8','Example: 2.8','مثال: 2.8','بېلګه: 2.8',exampleId='stat11-ex-2-8')
add(s,'q8','A sample of n = 6 values has a mean x̄ = 8. What is the value of Σx for this sample?','n = 6 قدروں کے ایک نمونے کا اوسط x̄ = 8 ہے۔ اس نمونے کے لیے Σx کی قدر کیا ہے؟','د n = 6 ارزښتونو یوې نمونې اوسط x̄ = 8 دی. د دې نمونې لپاره د Σx ارزښت څه دی؟',role='question',exampleId='stat11-ex-2-8')
F.done()
s['flow']=[b for b in s['flow']]
s['sourceNote']='Printed page 61. The foot of the scan shows a ghost of the preceding scan\'s page-number bar ("93"), which belongs to another page and is ignored. In the printed step-deviation table the u and fu columns have uneven spacing; values are as printed ("− 2", "−1", "0", "1", "2" and "− 10", "−18", "0", "27", "16"). Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 70 (printed 62) ----------
s=page(70,U,'62','Example 2.8 solution · 2.2.4 Properties of arithmetic mean · Example 2.9','مثال 2.8 کا حل · 2.2.4 حسابی اوسط کی خصوصیات · مثال 2.9','د بېلګې 2.8 حل · 2.2.4 د حسابي اوسط ځانګړتیاوې · بېلګه 2.9','am-properties')
F=Flow(s)
head(s,'sol8','Solution:','حل:','حل:',exampleId='stat11-ex-2-8')
add(s,'d8','By definition','تعریف کے مطابق','د تعریف له مخې',role='solution',exampleId='stat11-ex-2-8')
F.rest()
F.e('e8a',r'\bar{x}=\dfrac{\sum x}{n}','x̄ = Σx / n',exampleId='stat11-ex-2-8')
F.e('e8b',r'\text{Here }8=\dfrac{\sum x}{6}\ \Rightarrow\ \sum x=48','Here 8 = Σx / 6 ⇒ Σx = 48',exampleId='stat11-ex-2-8')
head(s,'h224','2.2.4 Properties of arithmetic mean','2.2.4 حسابی اوسط کی خصوصیات','2.2.4 د حسابي اوسط ځانګړتیاوې')
add(s,'t224','Some of the important properties of arithmetic mean are;','حسابی اوسط کی چند اہم خصوصیات یہ ہیں؛','د حسابي اوسط ځینې مهمې ځانګړتیاوې دا دي؛')
add(s,'p1','(i) The mean of a constant is constant that is if x = 5, 5, 5, 5, 5 then x̄ = 5.','(i) مستقلے کا اوسط مستقلہ ہوتا ہے یعنی اگر x = 5, 5, 5, 5, 5 ہو تو x̄ = 5۔','(i) د ثابت اوسط ثابت وي یعنې که x = 5, 5, 5, 5, 5 وي نو x̄ = 5.')
add(s,'p2','(ii) The sum of deviations of observations from arithmetic mean is zero that is','(ii) مشاہدات کے حسابی اوسط سے انحرافات کا مجموعہ صفر ہوتا ہے یعنی','(ii) د کتنو له حسابي اوسط څخه د انحرافاتو مجموعه صفر وي یعنې')
F.rest()
F.e('p2a',r'\sum(x-\bar{x})=0\quad\text{(In case of ungrouped data) and}','Σ(x − x̄) = 0 (In case of ungrouped data) and')
F.e('p2b',r'\sum f(x-\bar{x})=0\quad\text{(In case of grouped data)}','Σf(x − x̄) = 0 (In case of grouped data)')
add(s,'pf','Proof:','ثبوت:','ثبوت:')
F.rest()
F.e('pr1',r'\text{Consider }\sum_{i=1}^{n}(x_i-\bar{x})=\sum_{i=1}^{n}x_i-n\bar{x}\quad\text{(as }\bar{x}\text{ is constant)}','Consider Σ (i = 1 to n) (xi − x̄) = Σ xi − n x̄   (as x̄ is constant)')
F.e('pr2',r'=\sum_{i=1}^{n}x_i-n\,\dfrac{\sum_{i=1}^{n}x_i}{n}\quad\left(\text{as }\bar{x}=\dfrac{\sum x}{n}\right)','= Σ xi − n (Σ xi / n)   (as x̄ = Σx / n)')
F.e('pr3',r'=\sum_{i=1}^{n}x_i-\sum_{i=1}^{n}x_i=0','= Σ xi − Σ xi = 0')
head(s,'ex9','Example: 2.9','مثال: 2.9','بېلګه: 2.9',exampleId='stat11-ex-2-9')
s['tables']=[table('Example 2.9: x and x − x̄','مثال 2.9: x اور x − x̄','بېلګه 2.9: x او x − x̄',[c('x'),c('x − x̄')],[[c('2'),c('2 − 5 = −3')],[c('4'),c('−1')],[c('6'),c('1')],[c('8'),c('3')],[c('20'),c('Σ(x − x̄) = 0')]],exampleId='stat11-ex-2-9')]
F.rest();F.tb(0)
F.e('e9',r'\text{As }\bar{x}=\dfrac{\sum x}{n}=\dfrac{20}{4}=5','As x̄ = Σx / n = 20/4 = 5',exampleId='stat11-ex-2-9')
add(s,'p3','(iii) If x̄₁, x̄₂, …, x̄ₖ are the means of k samples of sizes n₁, n₂, …, nₖ respectively, then combined arithmetic mean is defined as','(iii) اگر x̄₁, x̄₂, …, x̄ₖ بالترتیب سائز n₁, n₂, …, nₖ کے k نمونوں کے اوسط ہوں تو مشترکہ حسابی اوسط کی تعریف یہ ہے','(iii) که x̄₁, x̄₂, …, x̄ₖ په ترتیب د n₁, n₂, …, nₖ کچې د k نمونو اوسطونه وي نو ګډ حسابي اوسط داسې تعریفېږي',sourceGap=dict(note='The formula for the combined mean follows on the next page.'))
F.done()
s['sourceNote']='Printed page 62. The scan top-left shows a colour smudge/thumb and the foot a ghost of another page-number bar ("36"); both ignored. A fly mark at the lower right is ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
