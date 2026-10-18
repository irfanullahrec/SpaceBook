from stathelp import *
c=cell
U='regression-correlation'
E53='stat11-ex-5-3'; E54='stat11-ex-5-4'; E55='stat11-ex-5-5'
# ---------- scan 191 (printed 181) ----------
s=page(191,U,'181','Types of correlation (end) · 5.2.1 Methods for measuring correlation','ارتباط کی اقسام (اختتام) · 5.2.1 ارتباط ناپنے کے طریقے','د همتړاو ډولونه (پای) · 5.2.1 د همتړاو د اندازه کولو طریقې','corr-types-2')
Flow(s)
L(s,[('n2','ii. The volume of gas will decrease as the pressure increases.','ii. گیس کا حجم دباؤ بڑھنے کے ساتھ کم ہوتا ہے۔','ii. د ګاز حجم د فشار له زیاتېدو سره کمېږي.'),('n3','iii. Age of a car and its resale price.','iii. کار کی عمر اور اس کی دوبارہ فروخت کی قیمت۔','iii. د موټر عمر او د هغه د بیا پلورنې بیه.'),('n4','iv. Years of experience and number of typing mistakes.','iv. تجربے کے سال اور ٹائپنگ کی غلطیوں کی تعداد۔','iv. د تجربې کلونه او د ټایپ تېروتنو شمېر.')],'corr-neg-examples')
add(s,'h3','(iii) Zero correlation','(iii) صفر ارتباط','(iii) صفر همتړاو')
add(s,'t3','If two variables have no relationship, then the correlation between them will be zero and the variables are called uncorrelated variables.','اگر دو متغیرات میں کوئی تعلق نہ ہو تو ان کے درمیان ارتباط صفر ہوگا اور متغیرات غیر مربوط متغیرات کہلاتے ہیں۔','که دوه متغیره هېڅ اړیکه ونه لري نو د هغوی تر منځ همتړاو به صفر وي او متغیرونه غیر همتړي متغیرونه بلل کېږي.')
add(s,'ex3','Examples:','مثالیں:','بېلګې:')
L(s,[('z1','i. The circumference of head and marks obtained by students.','i. سر کا گھیر اور طلبہ کے حاصل کردہ نمبر۔','i. د سر محیط او د زده کوونکو د ترلاسه شویو نمرو.'),('z2','ii. Sale of the woolen sweaters and sale of bata shoes.','ii. اونی سویٹروں کی فروخت اور باٹا جوتوں کی فروخت۔','ii. د وړینو سویټرونو پلور او د باټا بوټانو پلور.'),('z3','iii. Number of white cats in a city and road accidents in it.','iii. شہر میں سفید بلیوں کی تعداد اور اس میں سڑک کے حادثات۔','iii. په یوه ښار کې د سپینو پیشوګانو شمېر او په هغه کې د سړک پېښې.')],'corr-zero-examples')
add(s,'h4','(iv) Perfect correlation','(iv) کامل ارتباط','(iv) بشپړ همتړاو')
add(s,'t4','If a constant change in the values of one variable is in complete association with the corresponding constant change in the values of other variable it is called perfect correlation.','اگر ایک متغیر کی قدروں میں مستقل تبدیلی دوسرے متغیر کی قدروں میں متعلقہ مستقل تبدیلی کے ساتھ مکمل وابستگی میں ہو تو اسے کامل ارتباط کہتے ہیں۔','که د یوه متغیر په ارزښتونو کې ثابت بدلون د بل متغیر په ارزښتونو کې د اړوند ثابت بدلون سره په بشپړه اړیکه کې وي نو دې ته بشپړ همتړاو ویل کېږي.')
add(s,'ex4','Examples:','مثالیں:','بېلګې:')
add(s,'pp','i. Perfective positive correlation','i. کامل مثبت ارتباط','i. بشپړ مثبت همتړاو')
add(s,'pn','ii. Perfective negative correlation','ii. کامل منفی ارتباط','ii. بشپړ منفي همتړاو')
head(s,'h521','5.2.1 Methods for measuring correlation','5.2.1 ارتباط ناپنے کے طریقے','5.2.1 د همتړاو د اندازه کولو طریقې')
add(s,'t521','Correlation can be measured by any of the following methods.','ارتباط کو درج ذیل طریقوں میں سے کسی ایک سے ناپا جا سکتا ہے۔','همتړاو د لاندې طریقو له هرې یوې څخه اندازه کېدای شي.')
add(s,'g1','(i) Graphical method','(i) تصویری طریقہ','(i) ګرافي طریقه')
add(s,'g2','According to this method scatter diagram is constructed, which makes it possible to see whether correlation between the two variables exists or not and if exists whether it is positive or negative. This method gives just a rough idea about the correlation.','اس طریقے کے مطابق بکھراؤ خاکہ بنایا جاتا ہے جس سے یہ دیکھنا ممکن ہوتا ہے کہ دونوں متغیرات کے درمیان ارتباط موجود ہے یا نہیں اور اگر موجود ہے تو مثبت ہے یا منفی۔ یہ طریقہ ارتباط کے بارے میں صرف ایک موٹا اندازہ دیتا ہے۔','د دې طریقې له مخې د خپرېدو ډیاګرام جوړېږي، چې دا لیدل ممکنوي چې د دواړو متغیرونو تر منځ همتړاو شته که نه او که شته نو مثبت دی که منفي. دا طریقه د همتړاو په اړه یوازې یو خام اټکل ورکوي.')
add(s,'f1','(ii) Formula method','(ii) فارمولا طریقہ','(ii) فورمول طریقه')
add(s,'f2','A numerical measure of the degree and the direction of the linear relationship between two variables is called coefficient of correlation. Karl Pearson in (1890) identified a coefficient of correlation, known as Pearson’s product moment correlation coefficient as','دو متغیرات کے درمیان خطی تعلق کی درجے اور سمت کا عددی پیمانہ ارتباط کا عددی سر کہلاتا ہے۔ کارل پیئرسن نے (1890) میں ارتباط کا ایک عددی سر شناخت کیا، جسے پیئرسن کا حاصلِ ضرب معیارِ اثر ارتباطی عددی سر کہا جاتا ہے، جو یوں ہے','د دوو متغیرونو تر منځ د خطي اړیکې د درجې او لوري عددي اندازه د همتړاو ضریب بلل کېږي. Karl Pearson په (1890) کې د همتړاو یو ضریب وپېژانده، چې د Pearson د ضرب-مومنټ همتړاو ضریب په نوم پیژندل کېږي، داسې')
s['tables']=[table('Perfect positive correlation: x and y','کامل مثبت ارتباط: x اور y','بشپړ مثبت همتړاو: x او y',[c('x'),c('2'),c('4'),c('6'),c('8')],[[c('y'),c('5'),c('8'),c('11'),c('14')]]),
 table('Perfect negative correlation: x and y','کامل منفی ارتباط: x اور y','بشپړ منفي همتړاو: x او y',[c('x'),c('1'),c('2'),c('3'),c('4')],[[c('y'),c('20'),c('15'),c('10'),c('5')]])]
s['equations']+=[eqn(191,'r',r'r_{xy}=\dfrac{\sum(x-\bar{x})(y-\bar{y})}{\sqrt{\sum(x-\bar{x})^2\sum(y-\bar{y})^2}}\ ,\qquad -1\le r_{xy}\le 1\qquad\text{(Direct method)}','r_xy = Σ(x − x̄)(y − ȳ) / √(Σ(x − x̄)² Σ(y − ȳ)²),   −1 ≤ r_xy ≤ 1   (Direct method)')]
P=lambda *ks:dict(type='paragraphs',ids=[pid(191,k) for k in ks])
s['flow']=[P('n2','n3','n4','h3','t3','ex3','z1','z2','z3','h4','t4','ex4'),dict(type='table',index=0),P('pp'),dict(type='table',index=1),P('pn','h521','t521','g1','g2','f1','f2'),dict(type='equation',index=0)]
s['sourceNote']='Printed page 181. The first lines continue the examples of negative correlation. Printed spellings kept: "Perfective positive correlation", "Perfective negative correlation". Header graphics and watermark excluded.'
s['vocabulary']={'coefficient of correlation':dict(ur='ارتباط کا عددی سر',ps='د همتړاو ضریب'),'perfect correlation':dict(ur='کامل ارتباط',ps='بشپړ همتړاو')}
save(s)
# ---------- scan 192 (printed 182) ----------
s=page(192,U,'182','Shortcut method · Interpretation · Example 5.3: Karl Pearson coefficient of correlation','مختصر طریقہ · تشریح · مثال 5.3: کارل پیئرسن کا ارتباطی عددی سر','لنډه طریقه · تفسیر · بېلګه 5.3: د Karl Pearson همتړاو ضریب','corr-formula-1')
Flow(s)
add(s,'i1','Interpretation of the Coefficient of Correlation: The numerical value indicates the strength of the relationship while the sign only indicates direction of the relationship.','ارتباط کے عددی سر کی تشریح: عددی قدر تعلق کی مضبوطی ظاہر کرتی ہے جبکہ علامت صرف تعلق کی سمت ظاہر کرتی ہے۔','د همتړاو د ضریب تفسیر: عددي ارزښت د اړیکې ځواک ښيي پداسې حال کې چې نښه یوازې د اړیکې لوری ښيي.')
add(s,'i2','If r_xy = 0 means correlation is zero i.e. x and y are uncorrelated.','اگر r_xy = 0 ہو تو مطلب ارتباط صفر ہے یعنی x اور y غیر مربوط ہیں۔','که r_xy = 0 وي نو پدې معنا چې همتړاو صفر دی یعنې x او y غیر همتړي دي.')
add(s,'i3','> 0 means correlation is positive.','> 0 کا مطلب ارتباط مثبت ہے۔','> 0 پدې معنا چې همتړاو مثبت دی.')
add(s,'i4','< 0 means correlation is negative.','< 0 کا مطلب ارتباط منفی ہے۔','< 0 پدې معنا چې همتړاو منفي دی.')
add(s,'i5','= 1 means there is perfect positive correlation.','= 1 کا مطلب کامل مثبت ارتباط ہے۔','= 1 پدې معنا چې بشپړ مثبت همتړاو دی.')
add(s,'i6','= −1 means there is perfect negative correlation.','= −1 کا مطلب کامل منفی ارتباط ہے۔','= −1 پدې معنا چې بشپړ منفي همتړاو دی.')
head(s,'ex53','Example: 5.3','مثال: 5.3','بېلګه: 5.3',exampleId=E53)
add(s,'q53','Calculate the Karl Pearson coefficient of correlation for the following data.','درج ذیل اعداد و شمار کے لیے کارل پیئرسن کا ارتباطی عددی سر حساب کریں۔','د لاندې معلوماتو لپاره د Karl Pearson همتړاو ضریب محاسبه کړئ.',role='question',exampleId=E53)
head(s,'sol53','Solution:','حل:','حل:',exampleId=E53)
rows=[('12','14','2','5','10','4','25'),('9','8','-1','-1','1','1','1'),('8','6','-2','-3','6','4','9'),('10','9','0','0','0','0','0'),('11','11','1','2','2','1','4'),('13','12','3','3','9','9','9'),('7','3','-3','-6','18','9','36')]
s['tables']=[table('Example 5.3: x and y','مثال 5.3: x اور y','بېلګه 5.3: x او y',[c('x:')]+[c(r[0]) for r in rows],[[c('y:')]+[c(r[1]) for r in rows]],exampleId=E53),
 table('Example 5.3 solution table','مثال 5.3 کا حل: جدول','د بېلګې 5.3 د حل جدول',[c('x'),c('y'),c('(x − x̄)'),c('(y − ȳ)'),c('(x − x̄)(y − ȳ)'),c('(x − x̄)²'),c('(y − ȳ)²')],[[c(v) for v in r] for r in rows]+[[c('70'),c('63'),c('0'),c('0'),c('46'),c('28'),c('84')]],exampleId=E53)]
s['equations']+=[eqn(192,'sh',r'\text{or}\quad r_{xy}=\dfrac{n\sum xy-\sum x\sum y}{\sqrt{\left[n\sum x^2-\left(\sum x\right)^2\right]\left[n\sum y^2-\left(\sum y\right)^2\right]}}\qquad\text{(Shortcut method)}','or r_xy = (nΣxy − ΣxΣy) / √([nΣx² − (Σx)²][nΣy² − (Σy)²])   (Shortcut method)')]
P=lambda *ks:dict(type='paragraphs',ids=[pid(192,k) for k in ks])
s['flow']=[dict(type='equation',index=0),P('i1','i2','i3','i4','i5','i6','ex53','q53'),dict(type='table',index=0),P('sol53'),dict(type='table',index=1)]
s['sourceNote']='Printed page 182. The five interpretation lines (= 0, > 0, < 0, = 1, = −1) are printed as an aligned list below "If r_xy". A finger shadow at the top-left corner is ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 193 (printed 183) ----------
s=page(193,U,'183','Example 5.3 (working) · Example 5.4: shortcut method','مثال 5.3 (حل) · مثال 5.4: مختصر طریقہ','بېلګه 5.3 (حل) · بېلګه 5.4: لنډه طریقه','corr-formula-2')
Flow(s)
add(s,'a1','The coefficient of correlation is','ارتباط کا عددی سر ہے','د همتړاو ضریب دی',role='solution',exampleId=E53)
add(s,'a2','It means x and y have positive correlation.','اس کا مطلب ہے کہ x اور y میں مثبت ارتباط ہے۔','دا پدې معنا چې x او y مثبت همتړاو لري.',role='solution',exampleId=E53)
head(s,'ex54','Examples: 5.4','مثالیں: 5.4','بېلګې: 5.4',exampleId=E54)
add(s,'q54','Compute the product moment coefficient of correlation between x and y by shortcut method from the data given below;','نیچے دیے گئے اعداد و شمار سے x اور y کے درمیان حاصلِ ضرب معیارِ اثر ارتباطی عددی سر مختصر طریقے سے حساب کریں؛','له لاندې ورکړل شویو معلوماتو څخه د x او y تر منځ د ضرب-مومنټ همتړاو ضریب په لنډه طریقه محاسبه کړئ؛',role='question',exampleId=E54)
head(s,'sol54','Solution:','حل:','حل:',exampleId=E54)
add(s,'a3','The necessary calculations are:','ضروری حسابات یہ ہیں:','اړین محاسبې دا دي:',role='solution',exampleId=E54)
s['tables']=[table('Example 5.4: x and y','مثال 5.4: x اور y','بېلګه 5.4: x او y',[c('x:')]+[c(str(v)) for v in [1,2,3,4,5]],[[c('y:')]+[c(str(v)) for v in [2,5,3,8,7]]],exampleId=E54),
 table('Example 5.4 solution table','مثال 5.4 کا حل: جدول','د بېلګې 5.4 د حل جدول',[c('x'),c('y'),c('xy'),c('x²'),c('y²')],[[c(v) for v in r] for r in [('1','2','2','1','4'),('2','5','10','4','25'),('3','3','9','9','9'),('4','8','32','16','64'),('5','7','35','25','49'),('15','25','88','55','151')]],exampleId=E54)]
s['equations']+=[eqn(193,'m',r'\bar{x}=\dfrac{\sum x}{n}=\dfrac{70}{7}=10\qquad\qquad\bar{y}=\dfrac{\sum y}{n}=\dfrac{63}{7}=9','x̄ = Σx/n = 70/7 = 10    ȳ = Σy/n = 63/7 = 9',exampleId=E53),
 eqn(193,'r0',r'r_{xy}=\dfrac{\sum(x-\bar{x})(y-\bar{y})}{\sqrt{\sum(x-\bar{x})^2\sum(y-\bar{y})^2}}','r_xy = Σ(x − x̄)(y − ȳ) / √(Σ(x − x̄)² Σ(y − ȳ)²)',exampleId=E53),
 eqn(193,'r1',r'=\dfrac{46}{\sqrt{28\times 84}}','= 46/√(28 × 84)',exampleId=E53),
 eqn(193,'r2',r'=\dfrac{46}{48.4974}','= 46/48.4974',exampleId=E53),
 eqn(193,'r3',r'=0.95','= 0.95',exampleId=E53),
 eqn(193,'s0',r'r_{xy}=\dfrac{n\sum xy-\sum x\sum y}{\sqrt{\left[n\sum x^2-\left(\sum x\right)^2\right]\left[n\sum y^2-\left(\sum y\right)^2\right]}}','r_xy = (nΣxy − ΣxΣy) / √([nΣx² − (Σx)²][nΣy² − (Σy)²])',exampleId=E54)]
P=lambda *ks:dict(type='paragraphs',ids=[pid(193,k) for k in ks])
s['flow']=[dict(type='equation',index=0),P('a1'),dict(type='equation',index=1),dict(type='equation',index=2),dict(type='equation',index=3),dict(type='equation',index=4),P('a2','ex54','q54'),dict(type='table',index=0),P('sol54','a3'),dict(type='table',index=1),dict(type='equation',index=5)]
s['sourceNote']='Printed page 183. The means x̄ and ȳ (continuing the working of Example 5.3) are printed side by side and are kept as one equation. Printed heading kept: "Examples: 5.4". The formula of the shortcut method at the foot continues on the next page. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 194 (printed 184) ----------
s=page(194,U,'184','Example 5.4 (end) · 5.2.2 Properties of coefficient of correlation · Example 5.5 · 5.2.3 Correlation and causation (start)','مثال 5.4 (اختتام) · 5.2.2 ارتباطی عددی سر کی خصوصیات · مثال 5.5 · 5.2.3 ارتباط اور علت (آغاز)','بېلګه 5.4 (پای) · 5.2.2 د همتړاو د ضریب ځانګړتیاوې · بېلګه 5.5 · 5.2.3 همتړاو او علت (پیل)','corr-props-1')
Flow(s)
add(s,'a1','This implies that x and y have positive correlation.','اس سے ظاہر ہوتا ہے کہ x اور y میں مثبت ارتباط ہے۔','دا ښيي چې x او y مثبت همتړاو لري.',role='solution',exampleId=E54)
head(s,'h522','5.2.2 Properties of coefficient of correlation','5.2.2 ارتباطی عددی سر کی خصوصیات','5.2.2 د همتړاو د ضریب ځانګړتیاوې')
L(s,[('p1','(i) The coefficient of correlation is symmetrical with respect to the variables x and y i.e. r_xy = r_yx.','(i) ارتباطی عددی سر متغیرات x اور y کے لحاظ سے متشاکل ہے یعنی r_xy = r_yx۔','(i) د همتړاو ضریب د x او y متغیرونو په نسبت متناسب دی یعنې r_xy = r_yx.'),
('p2','(ii) The coefficient of correlation lies between −1 and 1.','(ii) ارتباطی عددی سر −1 اور 1 کے درمیان ہوتا ہے۔','(ii) د همتړاو ضریب د −1 او 1 تر منځ پروت دی.'),
('p3','(iii) The coefficient of correlation is independent of origin and scale i.e. r_xy = r_uv, where u = (x − a)/h and v = (y − b)/k.','(iii) ارتباطی عددی سر مبدا اور پیمانے سے آزاد ہے یعنی r_xy = r_uv، جہاں u = (x − a)/h اور v = (y − b)/k۔','(iii) د همتړاو ضریب د اصل او پیمانې څخه خپلواک دی یعنې r_xy = r_uv، چېرته چې u = (x − a)/h او v = (y − b)/k.'),
('p4','(iv) The coefficient of correlation is the geometric mean of the two regression coefficients i.e.','(iv) ارتباطی عددی سر دو ریگریشن عددی سروں کا ہندسی اوسط ہے یعنی','(iv) د همتړاو ضریب د دوو ریګرېشن ضریبونو هندسي اوسط دی یعنې')],'corr-props-list')
add(s,'pa','(if both regression coefficients are positive)','(اگر دونوں ریگریشن عددی سر مثبت ہوں)','(که دواړه ریګرېشن ضریبونه مثبت وي)')
add(s,'pb','(if both regression coefficients are negative).','(اگر دونوں ریگریشن عددی سر منفی ہوں)۔','(که دواړه ریګرېشن ضریبونه منفي وي).')
head(s,'ex55','Example: 5.5','مثال: 5.5','بېلګه: 5.5',exampleId=E55)
add(s,'q55','If the regression coefficient of y on x is b_y.x = 0.27 and x on y is b_x.y = 0.6. Find the product moment coefficient of correlation r_xy.','اگر x پر y کا ریگریشن عددی سر b_y.x = 0.27 اور y پر x کا b_x.y = 0.6 ہو۔ حاصلِ ضرب معیارِ اثر ارتباطی عددی سر r_xy معلوم کریں۔','که د x پر y د ریګرېشن ضریب b_y.x = 0.27 او د y پر x د b_x.y = 0.6 وي. د ضرب-مومنټ همتړاو ضریب r_xy ومومئ.',role='question',exampleId=E55)
head(s,'sol55','Solution:','حل:','حل:',exampleId=E55)
add(s,'a2','As both regression coefficients are positive, so r_xy is positive. Therefore,','چونکہ دونوں ریگریشن عددی سر مثبت ہیں اس لیے r_xy مثبت ہے۔ لہٰذا،','ځکه چې دواړه ریګرېشن ضریبونه مثبت دي نو r_xy مثبت دی. نو،',role='solution',exampleId=E55)
add(s,'a3','= 0.40. There is positive correlation between x and y.','= 0.40۔ x اور y کے درمیان مثبت ارتباط ہے۔','= 0.40. د x او y تر منځ مثبت همتړاو شته.',role='solution',exampleId=E55)
head(s,'h523','5.2.3 Correlation and causation','5.2.3 ارتباط اور علت','5.2.3 همتړاو او علت')
add(s,'t523','Correlation does not establish a cause and effect relationship between two variables. It does not provide any information about the size of the change in one variable as a result of a certain change in the other variable. In correlation both variables are interdependent. Relationship between them may be zero, weak or strong. Sometimes correlation between two unconnected variables will be nonsense or spurious. For example, two variables, sale of milk and death rate from accidents in a city may produce high positive correlation which may be due','ارتباط دو متغیرات کے درمیان علت و معلول کا تعلق قائم نہیں کرتا۔ یہ دوسرے متغیر میں کسی خاص تبدیلی کے نتیجے میں ایک متغیر میں تبدیلی کی مقدار کے بارے میں کوئی معلومات فراہم نہیں کرتا۔ ارتباط میں دونوں متغیرات باہم منحصر ہوتے ہیں۔ ان کے درمیان تعلق صفر، کمزور یا مضبوط ہو سکتا ہے۔ بعض اوقات دو غیر متعلقہ متغیرات کے درمیان ارتباط بے معنی یا جعلی ہوگا۔ مثال کے طور پر، دو متغیرات، کسی شہر میں دودھ کی فروخت اور حادثات سے اموات کی شرح، اعلیٰ مثبت ارتباط پیدا کر سکتے ہیں جو ہو سکتا ہے','همتړاو د دوو متغیرونو تر منځ د علت او معلول اړیکه نه جوړوي. دا د بل متغیر په یو ټاکلي بدلون په پایله کې د یوه متغیر د بدلون د کچې په اړه هېڅ معلومات نه ورکوي. په همتړاو کې دواړه متغیره متقابل تړلي وي. د هغوی تر منځ اړیکه صفر، کمزورې یا ځواکمنه کېدای شي. ځینې وختونه د دوو غیر اړوندو متغیرونو تر منځ همتړاو بې‌معنا یا جعلي وي. د مثال په توګه، دوه متغیره، په یوه ښار کې د شېدو پلور او د پېښو له امله د مړینې کچه، ښايي لوړ مثبت همتړاو رامنځته کړي چې ښايي له امله وي',sourceGap=dict(note='The sentence continues on the next page ("…to the growth of population …").'))
s['equations']+=[eqn(194,'e1',r'\dfrac{5(88)-(15)(25)}{\sqrt{[5(55)-(15)^2][5(151)-(25)^2]}}=\dfrac{440-375}{\sqrt{50\times 130}}=\dfrac{65}{\sqrt{6500}}=\dfrac{65}{80.623}=0.81','r_xy = (5(88) − (15)(25)) / √([5(55) − (15)²][5(151) − (25)²]) = (440 − 375)/√(50 × 130) = 65/√6500 = 65/80.623 = 0.81',exampleId=E54),
 eqn(194,'g1',r'r_{xy}=\sqrt{b_{y.x}\times b_{x.y}}','r_xy = √(b_y.x × b_x.y)'),
 eqn(194,'g2',r'r_{xy}=-\sqrt{b_{y.x}\times b_{x.y}}','r_xy = −√(b_y.x × b_x.y)'),
 eqn(194,'e5a',r'r_{xy}=\sqrt{b_{y.x}\times b_{x.y}}','r_xy = √(b_y.x × b_x.y)',exampleId=E55),
 eqn(194,'e5b',r'=\sqrt{(0.27)(0.6)}=0.40','= √((0.27)(0.6)) = 0.40',exampleId=E55)]
P=lambda *ks:dict(type='paragraphs',ids=[pid(194,k) for k in ks])
s['flow']=[dict(type='equation',index=0),P('a1','h522','p1','p2','p3','p4'),dict(type='equation',index=1),P('pa'),dict(type='equation',index=2),P('pb','ex55','q55','sol55','a2'),dict(type='equation',index=3),dict(type='equation',index=4),P('h523','t523')]
s['sourceNote']='Printed page 184. The first line (the result 0.81 of Example 5.4 in a chain of fractions) completes Example 5.4. In the printed text the symbols r_xy, b_y.x and b_x.y carry subscripts; they are written with underscores in the plain text here. Header graphics and watermark excluded.'
s['vocabulary']={}
# fix: a3 of example 5.5 is not in flow; place it
s['flow']=[dict(type='equation',index=0),P('a1','h522','p1','p2','p3','p4'),dict(type='equation',index=1),P('pa'),dict(type='equation',index=2),P('pb','ex55','q55','sol55','a2'),dict(type='equation',index=3),dict(type='equation',index=4),P('a3','h523','t523')]
save(s)
