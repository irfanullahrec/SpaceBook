from stathelp import *
c=cell
U='regression-correlation'
E58='stat11-ex-5-8'
def q(s,key,en,ur,ps,ex,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,**m)
def o(s,key,en,ur,ps,ex): add(s,key,en,ur,ps,role='option',exerciseId=ex)
rom=['i','ii','iii','iv','v','vi','vii','viii','ix','x']
UL=['(الف)','(ب)','(ج)','(د)']
def mcq(s,i,en,ur,ps,oe,ou,op):
    ex=f'stat11-ex5-3-{i}'; q(s,f'm{i}',en,ur,ps,ex)
    keys=[f'm{i}']
    for k,(a,b,d) in enumerate(zip(oe,ou,op)):
        o(s,f'm{i}{"abcd"[k]}',f'({"abcd"[k]}) {a}',f'{UL[k]} {b}',f'({"abcd"[k]}) {d}',ex); keys.append(f'm{i}{"abcd"[k]}')
    return keys
# ---------- scan 199 (printed 189) ----------
s=page(199,U,'189','Example 5.8 (series y, modified Spearman coefficient)','مثال 5.8 (سلسلہ y، ترمیم شدہ سپیئرمین عددی سر)','بېلګه 5.8 (لړۍ y، ترمیم شوی د سپیرمن ضریب)','corr-rank-5')
Flow(s)
add(s,'a1','Series y:','سلسلہ y:','لړۍ y:',role='solution',exampleId=E58)
add(s,'a2','73 is repeated for 2 times, the corresponding rank positions are 6 and 7. Hence rank [73] = (6 + 7)/2 = 6.5 and m is equal to the number of tied observations = 2. Therefore (m³ − m)/12 = (2³ − 2)/12 = (8 − 2)/12 = 6/12 = 0.5','73 دو بار دہرایا گیا ہے، متعلقہ درجے کی پوزیشنیں 6 اور 7 ہیں۔ لہٰذا درجہ [73] = (6 + 7)/2 = 6.5 اور m برابر مشاہدات کی تعداد کے برابر = 2۔ اس لیے (m³ − m)/12 = (2³ − 2)/12 = (8 − 2)/12 = 6/12 = 0.5','73 دوه ځله تکرار شوی، اړونده رتبې ځایونه 6 او 7 دي. نو رتبه [73] = (6 + 7)/2 = 6.5 او m د برابرو کتنو له شمېر سره مساوي = 2. نو (m³ − m)/12 = (2³ − 2)/12 = (8 − 2)/12 = 6/12 = 0.5',role='solution',exampleId=E58)
add(s,'a3','Now for repeated values 98 and 73, the element (m³ − m)/12 is added i.e. T = 2 + 0.5 = 2.5','اب دہرائی گئی قدروں 98 اور 73 کے لیے عنصر (m³ − m)/12 جمع کیا جاتا ہے یعنی T = 2 + 0.5 = 2.5','اوس د تکرار شویو ارزښتونو 98 او 73 لپاره عنصر (m³ − m)/12 جمع کېږي یعنې T = 2 + 0.5 = 2.5',role='solution',exampleId=E58)
add(s,'a4','Thus, the modified spearman’s rank correlation coefficient for repeated values is','اس طرح دہرائی گئی قدروں کے لیے ترمیم شدہ سپیئرمین کا درجاتی ارتباطی عددی سر ہے','په دې توګه د تکرار شویو ارزښتونو لپاره ترمیم شوی د سپیرمن رتبه‌یي همتړاو ضریب دی',role='solution',exampleId=E58)
add(s,'a5','The variables are positively correlated.','متغیرات مثبت طور پر مربوط ہیں۔','متغیرونه په مثبت ډول همتړي دي.',role='solution',exampleId=E58)
s['equations']+=[eqn(199,'r',r'r_s=1-\dfrac{6\left(\sum d^2+T\right)}{n^3-n}','r_s = 1 − 6(Σd² + T)/(n³ − n)',exampleId=E58),
 eqn(199,'r2',r'=1-\dfrac{6(42.5+2.5)}{10^3-10}','= 1 − 6(42.5 + 2.5)/(10³ − 10)   [the printed denominator reads "103 − 10", i.e. 10³ − 10]',exampleId=E58),
 eqn(199,'r3',r'=1-\dfrac{6(45)}{990}=1-0.2727=0.73','= 1 − 6(45)/990 = 1 − 0.2727 = 0.73',exampleId=E58)]
P=lambda *ks:dict(type='paragraphs',ids=[pid(199,k) for k in ks])
s['flow']=[P('a1','a2','a3','a4'),dict(type='equation',index=0),dict(type='equation',index=1),dict(type='equation',index=2),P('a5')]
s['sourceNote']='Printed page 189. The lower half of the page is blank. In the second line the printed denominator is "103 − 10" for 10³ − 10. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 200 (printed 190) ----------
s=page(200,U,'190','Key points of Unit 5','یونٹ 5 کے اہم نکات','د پنځم واحد مهم ټکي','key-points-unit5')
Flow(s)
head(s,'h','Key points','اہم نکات','مهم ټکي')
add(s,'k1','A Statistical technique used for prediction about the values of a dependent variable on the basis of the known values of an independent variable is called regression.','وہ شماریاتی تکنیک جو آزاد متغیر کی معلوم قدروں کی بنیاد پر تابع متغیر کی قدروں کے بارے میں پیش گوئی کے لیے استعمال ہوتی ہے ریگریشن کہلاتی ہے۔','هغه احصایوي تخنیک چې د خپلواک متغیر د پېژندل شویو ارزښتونو پر بنسټ د تابع متغیر د ارزښتونو په اړه د وړاندوینې لپاره کارول کېږي ریګرېشن بلل کېږي.',listGroup='unit5-kp-1')
add(s,'k2','Scatter diagram is a graphic device which makes it possible to see a line or curve whose equation is required.','بکھراؤ خاکہ ایک تصویری آلہ ہے جو اس لکیر یا منحنی کو دیکھنا ممکن بناتا ہے جس کی مساوات درکار ہو۔','د خپرېدو ډیاګرام یوه انځورییزه وسیله ده چې هغه کرښه یا منحني لیدل ممکنوي چې معادله یې اړینه وي.',listGroup='unit5-kp-1')
add(s,'k3','When the dependent variable is regressed on the basis of a single independent variable, it is called simple regression.','جب تابع متغیر کو ایک ہی آزاد متغیر کی بنیاد پر ریگریس کیا جائے تو اسے سادہ ریگریشن کہتے ہیں۔','کله چې تابع متغیر د یوه واحد خپلواک متغیر پر بنسټ ریګرېس شي نو دې ته ساده ریګرېشن ویل کېږي.',listGroup='unit5-kp-1')
add(s,'k4','When the dependent variable is regressed on the basis of two or more independent variables, it is called multiple regression.','جب تابع متغیر کو دو یا زیادہ آزاد متغیرات کی بنیاد پر ریگریس کیا جائے تو اسے متعدد ریگریشن کہتے ہیں۔','کله چې تابع متغیر د دوو یا ډېرو خپلواکو متغیرونو پر بنسټ ریګرېس شي نو دې ته څو‌ګونی ریګرېشن ویل کېږي.',listGroup='unit5-kp-1')
add(s,'k5','The estimated least squares regression line of y depending on x is ŷ = a_y.x + b_y.x x,','x پر منحصر y کی تخمینی کم از کم مربعات ریگریشن لکیر ہے ŷ = a_y.x + b_y.x x،','د x پورې تړلي د y اټکل شوې د لږ تر لږه مربعاتو ریګرېشن کرښه ده ŷ = a_y.x + b_y.x x،',listGroup='unit5-kp-2')
add(s,'k6','A statistical technique which measures the strength of relationship between two quantitative variables is called simple correlation.','وہ شماریاتی تکنیک جو دو مقداری متغیرات کے درمیان تعلق کی مضبوطی کو ناپتی ہے سادہ ارتباط کہلاتی ہے۔','هغه احصایوي تخنیک چې د دوو کمیتي متغیرونو تر منځ د اړیکې ځواک اندازه کوي ساده همتړاو بلل کېږي.',listGroup='unit5-kp-3')
add(s,'k7','It the two variables are moving in the same direction (i.e. both increase or both decrease), it is called positive correlation.','اگر دو متغیرات ایک ہی سمت میں حرکت کر رہے ہوں (یعنی دونوں بڑھیں یا دونوں گھٹیں) تو اسے مثبت ارتباط کہتے ہیں۔','که دوه متغیره په یو لوري حرکت کوي (یعنې دواړه زیاتېږي یا دواړه کمېږي) نو دې ته مثبت همتړاو ویل کېږي.',listGroup='unit5-kp-3')
add(s,'k8','It the two variables are moving in the opposite direction (i.e. one increases the other, decreases), it is called negative correlation.','اگر دو متغیرات مخالف سمت میں حرکت کر رہے ہوں (یعنی ایک بڑھے تو دوسرا گھٹے) تو اسے منفی ارتباط کہتے ہیں۔','که دوه متغیره په مخالف لوري حرکت کوي (یعنې یو زیاتېږي بل کمېږي) نو دې ته منفي همتړاو ویل کېږي.',listGroup='unit5-kp-3')
add(s,'k9','The coefficient of correlation is the geometric mean of the two regression coefficients i.e. r_xy = √(b_y.x × b_x.y)','ارتباطی عددی سر دو ریگریشن عددی سروں کا ہندسی اوسط ہے یعنی r_xy = √(b_y.x × b_x.y)','د همتړاو ضریب د دوو ریګرېشن ضریبونو هندسي اوسط دی یعنې r_xy = √(b_y.x × b_x.y)',listGroup='unit5-kp-4')
add(s,'k10','Spearman rank correlation is used to study the relationship between two set of ranks.','سپیئرمین درجاتی ارتباط درجوں کے دو سیٹوں کے درمیان تعلق کا مطالعہ کرنے کے لیے استعمال ہوتا ہے۔','د Spearman رتبه‌یي همتړاو د رتبو د دوو سیټونو تر منځ د اړیکې د مطالعې لپاره کارول کېږي.',listGroup='unit5-kp-5')
eq=[('f1',r'b_{y.x}=\dfrac{n\sum xy-\sum x\sum y}{n\sum x^2-\left(\sum x\right)^2}','b_y.x = (nΣxy − ΣxΣy)/(nΣx² − (Σx)²)',None),
 ('f2',r'a_{y.x}=\dfrac{\sum y}{n}-b_{y.x}\left(\dfrac{\sum x}{n}\right)','a_y.x = Σy/n − b_y.x (Σx/n)',None),
 ('f3',r'r_{xy}=\dfrac{\sum(x-\bar{x})(y-\bar{y})}{\sqrt{\sum(x-\bar{x})^2\sum(y-\bar{y})^2}}\ ,\qquad -1\le r_{xy}\le 1','r_xy = Σ(x − x̄)(y − ȳ) / √(Σ(x − x̄)² Σ(y − ȳ)²),   −1 ≤ r_xy ≤ 1',None),
 ('f4',r'r_{xy}=\sqrt{b_{y.x}\times b_{x.y}}','r_xy = √(b_y.x × b_x.y)',None),
 ('f5',r'r_s=1-\dfrac{6\sum d^2}{n^3-n}\ ,\qquad -1\le r_s\le 1','r_s = 1 − 6Σd²/(n³ − n),   −1 ≤ r_s ≤ 1',None)]
build(s,200,['h','k1','k2','k3','k4','k5','E:f1','E:f2','k6','k7','k8','E:f3','k9','E:f4','k10','E:f5'],eq)
s['sourceNote']='Printed page 190. Key points of the unit as a bulleted list. A finger covers the top-left corner of the scan. Printed spellings kept: "It the two variables". Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 201 (printed 191) ----------
s=page(201,U,'191','Exercise-5: Q5.1 True or false · Q5.2 Fill in the blanks','مشق-5: سوال 5.1 صحیح یا غلط · سوال 5.2 خالی جگہیں پُر کریں','تمرین-5: پوښتنه 5.1 سم یا غلط · پوښتنه 5.2 تشې ډکې کړئ','exercise5-a',layout='exercise')
Flow(s)
head(s,'h','Exercise-5','مشق-5','تمرین-5',exerciseId='stat11-ex5')
head(s,'h51','5.1 Read the following statements and write T for True and F for False statements.','5.1 درج ذیل بیانات پڑھیں اور صحیح کے لیے T اور غلط بیانات کے لیے F لکھیں۔','5.1 لاندې بیانونه ولولئ او سم لپاره T او غلط بیانونو لپاره F ولیکئ.',exerciseId='stat11-ex5-1')
T1=[('In simple linear regression model x and y variables are independent of each other.','سادہ خطی ریگریشن ماڈل میں x اور y متغیرات ایک دوسرے سے آزاد ہیں۔','په ساده خطي ریګرېشن ماډل کې x او y متغیرونه یو له بل څخه خپلواک دي.'),
('Regression is a process of estimation of the unknown values of the dependent variable from the known values of the independent variable.','ریگریشن آزاد متغیر کی معلوم قدروں سے تابع متغیر کی نامعلوم قدروں کے تخمینے کا عمل ہے۔','ریګرېشن د خپلواک متغیر له پېژندل شویو ارزښتونو څخه د تابع متغیر د نامعلومو ارزښتونو د اټکل پروسه ده.'),
('Correlation coefficient is the arithmetic mean between the two regression coefficients.','ارتباطی عددی سر دو ریگریشن عددی سروں کے درمیان حسابی اوسط ہے۔','د همتړاو ضریب د دوو ریګرېشن ضریبونو تر منځ حسابي اوسط دی.'),
('If b_xy = 0.8, b_yx = 0.5 then r_xy = 0.4.','اگر b_xy = 0.8، b_yx = 0.5 ہو تو r_xy = 0.4۔','که b_xy = 0.8، b_yx = 0.5 وي نو r_xy = 0.4.'),
('The coefficient of correlation lies between −1 and 1.','ارتباطی عددی سر −1 اور 1 کے درمیان ہوتا ہے۔','د همتړاو ضریب د −1 او 1 تر منځ پروت دی.'),
('If r_xy = 0, it means x and y variable are independent of each other.','اگر r_xy = 0 ہو تو اس کا مطلب ہے کہ x اور y متغیرات ایک دوسرے سے آزاد ہیں۔','که r_xy = 0 وي نو پدې معنا چې x او y متغیره یو له بل څخه خپلواک دي.'),
('If the two variables move in the opposite direction then correlation between them is said to be positive.','اگر دو متغیرات مخالف سمت میں حرکت کریں تو ان کے درمیان ارتباط کو مثبت کہا جاتا ہے۔','که دوه متغیره په مخالف لوري حرکت وکړي نو د هغوی تر منځ همتړاو مثبت ویل کېږي.'),
('Suppose ŷ = 5 − 2x, the y-intercept is 2.','فرض کریں ŷ = 5 − 2x، y-قطع 2 ہے۔','فرض کړئ ŷ = 5 − 2x، د y-کټ 2 دی.'),
('A simple linear regression contains only one independent variable.','سادہ خطی ریگریشن میں صرف ایک آزاد متغیر ہوتا ہے۔','ساده خطي ریګرېشن یوازې یو خپلواک متغیر لري.'),
('Both the regression coefficients b_y.x and b_x.y should be of same sign.','دونوں ریگریشن عددی سر b_y.x اور b_x.y کی علامت ایک جیسی ہونی چاہیے۔','دواړه ریګرېشن ضریبونه b_y.x او b_x.y باید یو شان نښه ولري.')]
for i,(a,b,d) in enumerate(T1): q(s,f't{i+1}',f'({rom[i]}) {a}',f'({rom[i]}) {b}',f'({rom[i]}) {d}',f'stat11-ex5-1-{rom[i]}')
head(s,'h52','5.2 Fill in the blanks with a suitable word.','5.2 خالی جگہوں کو موزوں لفظ سے پُر کریں۔','5.2 تشې په مناسب کلمه ډکې کړئ.',exerciseId='stat11-ex5-2')
F2=[('If the regression coefficient b_y.x > 1 then b_x.y ____________.','اگر ریگریشن عددی سر b_y.x > 1 ہو تو b_x.y ____________۔','که ریګرېشن ضریب b_y.x > 1 وي نو b_x.y ____________.'),
('If the regression coefficient b_y.x < 1 then b_x.y ____________.','اگر ریگریشن عددی سر b_y.x < 1 ہو تو b_x.y ____________۔','که ریګرېشن ضریب b_y.x < 1 وي نو b_x.y ____________.'),
('If the variables x and y are independent the value of regression coefficient is ____________.','اگر متغیرات x اور y آزاد ہوں تو ریگریشن عددی سر کی قدر ____________ ہے۔','که متغیرونه x او y خپلواک وي نو د ریګرېشن ضریب ارزښت ____________ دی.'),
('The range of the coefficient of correlation is ____________.','ارتباطی عددی سر کی حد ____________ ہے۔','د همتړاو ضریب حد ____________ دی.'),
('A regression equation having two or more independent variables is called ____________.','وہ ریگریشن مساوات جس میں دو یا زیادہ آزاد متغیرات ہوں ____________ کہلاتی ہے۔','هغه ریګرېشن معادله چې دوه یا ډېر خپلواک متغیرونه ولري ____________ بلل کېږي.'),
('If the correlation coefficient is zero, the value of regression coefficient is ____________.','اگر ارتباطی عددی سر صفر ہو تو ریگریشن عددی سر کی قدر ____________ ہے۔','که د همتړاو ضریب صفر وي نو د ریګرېشن ضریب ارزښت ____________ دی.'),
('For the regression equation ŷ = 7 + 2x, then value of slope is ____________.','ریگریشن مساوات ŷ = 7 + 2x کے لیے ڈھلوان کی قدر ____________ ہے۔','د ریګرېشن معادلې ŷ = 7 + 2x لپاره د ډلوان ارزښت ____________ دی.'),
('If x = 2 and ŷ = 7 + 2x, then value of ŷ is ____________.','اگر x = 2 اور ŷ = 7 + 2x ہو تو ŷ کی قدر ____________ ہے۔','که x = 2 او ŷ = 7 + 2x وي نو د ŷ ارزښت ____________ دی.'),
('The error term e is equal to ____________.','غلطی کی اصطلاح e ____________ کے برابر ہے۔','د تېروتنې اصطلاح e له ____________ سره مساوي ده.')]
for i,(a,b,d) in enumerate(F2): q(s,f'f{i+1}',f'({rom[i]}) {a}',f'({rom[i]}) {b}',f'({rom[i]}) {d}',f'stat11-ex5-2-{rom[i]}',**({'sourceGap':dict(note='Q5.2 continues on the next page with item (x).')} if i==8 else {}))
F=Flow(s);F.done()
s['sourceNote']='Printed page 191. In the printed text the symbols b_xy, b_yx, r_xy, b_y.x, b_x.y carry subscripts; they are written with underscores in the plain text here. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 202 (printed 192) ----------
s=page(202,U,'192','Exercise-5: Q5.2 (x) · Q5.3 Choose the correct answer (i)–(ix)','مشق-5: سوال 5.2 (x) · سوال 5.3 صحیح جواب منتخب کریں (i)–(ix)','تمرین-5: پوښتنه 5.2 (x) · پوښتنه 5.3 سم ځواب وټاکئ (i)–(ix)','exercise5-b',layout='exercise')
Flow(s)
q(s,'f10','(x) The signature property in regression means that the signs of b_y.x, b_x.y, and r_xy are ____________.','(x) ریگریشن میں دستخطی خاصیت کا مطلب ہے کہ b_y.x، b_x.y اور r_xy کی علامتیں ____________ ہیں۔','(x) په ریګرېشن کې د لاسلیک ځانګړتیا پدې معنا چې د b_y.x، b_x.y او r_xy نښې ____________ دي.','stat11-ex5-2-x',sourceGap=dict(note='Completes Q5.2 from the previous page.'))
head(s,'h53','5.3 Choose the correct answer.','5.3 صحیح جواب منتخب کریں۔','5.3 سم ځواب وټاکئ.',exerciseId='stat11-ex5-3')
M=[(1,'(i) If x and y are two variables, there can be at most','(i) اگر x اور y دو متغیرات ہوں تو زیادہ سے زیادہ ہو سکتی ہیں','(i) که x او y دوه متغیره وي نو تر ډېره به وي',('one regression line','two regression lines','an infinite number of regression lines','three regression lines'),('ایک ریگریشن لکیر','دو ریگریشن لکیریں','ریگریشن لکیروں کی لامحدود تعداد','تین ریگریشن لکیریں'),('یوه ریګرېشن کرښه','دوه ریګرېشن کرښې','د ریګرېشن کرښو بې‌پایه شمېر','درې ریګرېشن کرښې')),
(2,'(ii) In the regression line of y on x, the variable x is known as','(ii) x پر y کی ریگریشن لکیر میں متغیر x کہلاتا ہے','(ii) د x پر y په ریګرېشن کرښه کې متغیر x بلل کېږي',('independent variable','intercept of the line','both (a) and (b)','all of the above'),('آزاد متغیر','لکیر کا قطع','(الف) اور (ب) دونوں','مندرجہ بالا سب'),('خپلواک متغیر','د کرښې کټ','(a) او (b) دواړه','پورتني ټول')),
(3,'(iii) In the regression line y = α + βx, β is called the','(iii) ریگریشن لکیر y = α + βx میں β کہلاتا ہے','(iii) د ریګرېشن کرښې y = α + βx کې β بلل کېږي',('slope of the line','intercept of the line','neither (a) nor (b)','both (a) and (b)'),('لکیر کا ڈھلوان','لکیر کا قطع','نہ (الف) نہ (ب)','(الف) اور (ب) دونوں'),('د کرښې ډلوان','د کرښې کټ','نه (a) نه (b)','(a) او (b) دواړه')),
(4,'(iv) If b_y.x and b_x.y are two regression coefficients, they have','(iv) اگر b_y.x اور b_x.y دو ریگریشن عددی سر ہوں تو ان کی','(iv) که b_y.x او b_x.y دوه ریګرېشن ضریبونه وي نو دوی لري',('same sign','opposite sign','either same or opposite sign','nothing can be said'),('ایک جیسی علامت ہوتی ہے','مخالف علامت ہوتی ہے','ایک جیسی یا مخالف علامت ہوتی ہے','کچھ نہیں کہا جا سکتا'),('یو شان نښه','مخالفه نښه','یو شان یا مخالفه نښه','هېڅ نشي ویلای')),
(5,'(v) If b_y.x > 1, then b_x.y is','(v) اگر b_y.x > 1 ہو تو b_x.y ہے','(v) که b_y.x > 1 وي نو b_x.y دی',('less than 1','greater than 1','equal to 1','equal to 0'),('1 سے کم','1 سے زیادہ','1 کے برابر','0 کے برابر'),('له 1 څخه کم','له 1 څخه ډېر','له 1 سره مساوي','له 0 سره مساوي')),
(6,'(vi) If x and y are independent then the value of regression coefficient b_x.y is equal to','(vi) اگر x اور y آزاد ہوں تو ریگریشن عددی سر b_x.y کی قدر کے برابر ہے','(vi) که x او y خپلواک وي نو د ریګرېشن ضریب b_x.y ارزښت له … سره مساوي دی',('0','1','∞','any positive value'),('0','1','∞','کوئی بھی مثبت قدر'),('0','1','∞','هر مثبت ارزښت')),
(7,'(vii) The idea of product moment correlation was given by','(vii) حاصلِ ضرب معیارِ اثر ارتباط کا تصور دیا تھا','(vii) د ضرب-مومنټ همتړاو مفکوره ورکړې وه',('Sir Francis Galton','Spearman','Karl Pearson','R.A Fisher'),('سر فرانسس گالٹن نے','سپیئرمین نے','کارل پیئرسن نے','آر اے فشر نے'),('سر فرانسس ګالټن','سپیرمن','کارل پیرسن','آر ای فشر')),
(8,'(viii) The unit of correlation coefficient is','(viii) ارتباطی عددی سر کی اکائی ہے','(viii) د همتړاو د ضریب واحد دی',('kg','percent','non-existing','metre'),('کلوگرام','فیصد','موجود نہیں','میٹر'),('کیلوګرام','سلنه','نشته','متر')),
(9,'(ix) The range of simple correlation coefficient is','(ix) سادہ ارتباطی عددی سر کی حد ہے','(ix) د ساده همتړاو د ضریب حد دی',('−∞ to ∞','0 to ∞','−1 to 1','0 to 1'),('−∞ سے ∞','0 سے ∞','−1 سے 1','0 سے 1'),('−∞ تر ∞','0 تر ∞','−1 تر 1','0 تر 1'))]
seq=['f10','h53']
for i,a,b,d,oe,ou,op in M: seq+=mcq(s,i,a,b,d,oe,ou,op)
build(s,202,seq,[])
s['sourceNote']='Printed page 192. In the printed text the symbols b_y.x, b_x.y, r_xy carry subscripts; they are written with underscores here. Q5.3 continues on the next page (item x). Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
