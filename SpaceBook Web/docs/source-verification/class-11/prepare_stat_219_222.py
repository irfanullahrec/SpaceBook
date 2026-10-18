from stathelp import *
c=cell
U='time-series'
E68='stat11-ex-6-8'
def q(s,key,en,ur,ps,ex,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,**m)
def o(s,key,en,ur,ps,ex): add(s,key,en,ur,ps,role='option',exerciseId=ex)
def row(a,b,d,vals): return [c(a,b,d)]+[c(str(v)) for v in vals]
rom=['i','ii','iii','iv','v','vi','vii','viii','ix','x']
UL=['(الف)','(ب)','(ج)','(د)']
def mcq(s,i,en,ur,ps,oe,ou,op):
    ex=f'stat11-ex6-2-{i}'; q(s,f'm{i}',en,ur,ps,ex)
    keys=[f'm{i}']
    for k,(a,b,d) in enumerate(zip(oe,ou,op)):
        o(s,f'm{i}{"abcd"[k]}',f'({"abcd"[k]}) {a}',f'{UL[k]} {b}',f'({"abcd"[k]}) {d}',ex); keys.append(f'm{i}{"abcd"[k]}')
    return keys
N1=(r'\sum y=na+b\sum x+c\sum x^2\qquad\text{(i)}','Σy = na + bΣx + cΣx²   (i)')
N2=(r'\sum xy=a\sum x+b\sum x^2+c\sum x^3\qquad\text{(ii)}','Σxy = aΣx + bΣx² + cΣx³   (ii)')
N3=(r'\sum x^2y=a\sum x^2+b\sum x^3+c\sum x^4\qquad\text{(iii)}','Σx²y = aΣx² + bΣx³ + cΣx⁴   (iii)')
# ---------- scan 219 (printed 209) ----------
s=page(219,U,'209','Example 6.8: table and normal equations','مثال 6.8: جدول اور معمول کی مساواتیں','بېلګه 6.8: جدول او نورمال معادلې','ts-quad-3')
Flow(s)
add(s,'a1','Putting values in the above equation','اوپر دی گئی مساوات میں قدریں رکھنے سے','په پورتنۍ معادله کې ارزښتونه ایښودو سره',role='solution',exampleId=E68)
add(s,'a2','Multiply equation (4) by 21 and subtract it from equation (6)','مساوات (4) کو 21 سے ضرب دیں اور اسے مساوات (6) سے منہا کریں','معادله (4) په 21 ضرب کړئ او له معادلې (6) څخه یې تفریق کړئ',role='solution',exampleId=E68)
rows=[(1980,100,-7,49,-700,-343,4900,2401,'93.94'),(1981,87,-5,25,-435,-125,2175,625,'88.36'),(1982,96,-3,9,-288,-27,864,81,'95.90'),(1983,102,-1,1,-102,-1,102,1,'116.56'),(1984,139,1,1,139,1,139,1,'150.34'),(1985,210,3,9,630,27,1890,81,'197.24'),(1986,289,5,25,1445,125,7225,625,'257.26'),(1987,307,7,49,2149,343,15043,2401,'330.40')]
s['tables']=[table('Example 6.8 solution table','مثال 6.8 کا حل: جدول','د بېلګې 6.8 د حل جدول',[c('Year','سال','کال'),c('y'),c('x'),c('x²'),c('xy'),c('x³'),c('x²y'),c('x⁴'),c('ŷ')],[[c(str(v)) for v in r] for r in rows]+[[c('Total','میزان','ټولیز'),c('1330'),c('0'),c('168'),c('2839'),c('0'),c('32338'),c('6216'),c('1330')]],exampleId=E68)]
s['equations']+=[eqn(219,'n2',N2[0],N2[1],exampleId=E68),eqn(219,'n3',N3[0],N3[1],exampleId=E68),
 eqn(219,'e4',r'1330=8a+618c\qquad\text{(4)}','1330 = 8a + 618c   (4)   [the printed coefficient 618 is a misprint of 168]',exampleId=E68),
 eqn(219,'e5',r'2838=168b\qquad\text{(5)}\qquad\Rightarrow\ b=\dfrac{2838}{168}=16.89','2838 = 168b   (5)   ⇒ b = 2838/168 = 16.89',exampleId=E68),
 eqn(219,'e6',r'32338=168a+6216c\qquad\text{(6)}','32338 = 168a + 6216c   (6)',exampleId=E68),
 eqn(219,'e6b',r'32338=168a+6216c\qquad\text{(6)}','32338 = 168a + 6216c   (6)',exampleId=E68),
 eqn(219,'e4b',r'27930=168a+3528c\qquad\text{(4)}','27930 = 168a + 3528c   (4)',exampleId=E68),
 eqn(219,'e7',r'4408=2688c\qquad\Rightarrow\ c=\dfrac{4408}{2688}=1.64','4408 = 2688c   ⇒ c = 4408/2688 = 1.64',exampleId=E68)]
P=lambda *ks:dict(type='paragraphs',ids=[pid(219,k) for k in ks])
s['flow']=[dict(type='equation',index=0),dict(type='equation',index=1),dict(type='table',index=0),P('a1'),dict(type='equation',index=2),dict(type='equation',index=3),dict(type='equation',index=4),P('a2'),dict(type='equation',index=5),dict(type='equation',index=6),dict(type='equation',index=7)]
s['sourceNote']='Printed page 209. The first lines complete the normal equations (ii) and (iii) from the previous page. In the printed equation (4) the coefficient of c reads 618 (a misprint; the working below uses 168 → 168 × 21 = 3528). The subtraction line is printed with minus signs under each term. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 220 (printed 210) ----------
s=page(220,U,'210','Example 6.8 (end) · Advantages and disadvantages of the method of least squares','مثال 6.8 (اختتام) · کم از کم مربعات کے طریقے کے فوائد اور نقصانات','بېلګه 6.8 (پای) · د لږ تر لږه مربعاتو د طریقې ګټې او زیانونه','ts-quad-4')
Flow(s)
add(s,'a1','Put this value of c in equation (4)','c کی یہ قدر مساوات (4) میں رکھیں','د c دا ارزښت په معادله (4) کې کېږدئ',role='solution',exampleId=E68)
add(s,'a2','Hence the fitted second degree parabola is ŷ = 131.81 + 16.89x + 1.64x²','لہٰذا فٹ کیا گیا دوسرے درجے کا قطع مکافی ہے ŷ = 131.81 + 16.89x + 1.64x²','نو برابر شوې دویم درجې پیراپولا ده ŷ = 131.81 + 16.89x + 1.64x²',role='solution',exampleId=E68)
add(s,'a3','Putting values of x in this equation, to find trend values, given in the last column of the table.','x کی قدریں اس مساوات میں رکھنے سے رجحان کی قدریں معلوم کی جاتی ہیں، جو جدول کے آخری کالم میں دی گئی ہیں۔','پدې معادله کې د x ارزښتونه ایښودو سره د تمایل ارزښتونه موندل کېږي، چې د جدول په وروستي کالم کې ورکړل شوي دي.',role='solution',exampleId=E68)
head(s,'h','Advantages and disadvantages of the method of least squares','کم از کم مربعات کے طریقے کے فوائد اور نقصانات','د لږ تر لږه مربعاتو د طریقې ګټې او زیانونه')
add(s,'ah','Advantages:','فوائد:','ګټې:')
L(s,[('v1','(i) This is a definite and an objective method.','(i) یہ ایک قطعی اور معروضی طریقہ ہے۔','(i) دا یوه ټاکلې او معروضي طریقه ده.'),('v2','(ii) The trend is expressed by a mathematical formula.','(ii) رجحان ایک ریاضیاتی فارمولے سے ظاہر کیا جاتا ہے۔','(ii) تمایل په یوه ریاضیاتي فورمول ښودل کېږي.'),('v3','(iii) The fitted trend can easily be extended into future or past.','(iii) فٹ کیا گیا رجحان آسانی سے مستقبل یا ماضی تک بڑھایا جا سکتا ہے۔','(iii) برابر شوی تمایل په اسانۍ سره راتلونکي یا تېر وخت ته غځېدای شي.')],'ls-adv')
add(s,'dh','Disadvantages:','نقصانات:','زیانونه:')
L(s,[('w1','(i) This method is too difficult for some type of curves.','(i) یہ طریقہ بعض اقسام کے منحنیات کے لیے بہت مشکل ہے۔','(i) دا طریقه د ځینو ډولونو منحنیو لپاره ډېره ستونزمنه ده.'),('w2','(ii) It is some time difficult to choose a proper mathematical equation.','(ii) بعض اوقات مناسب ریاضیاتی مساوات کا انتخاب مشکل ہوتا ہے۔','(ii) ځینې وختونه د مناسبې ریاضیاتي معادلې ټاکل ستونزمن وي.')],'ls-dis')
s['equations']+=[eqn(220,'c1',r'\begin{aligned}1330&=8a+168(1.63)\\ &=8a+275.52\\ 1330-275.52&=8a\\ 1054.48&=8a\end{aligned}\qquad\text{or}\qquad a=\dfrac{1054.48}{8}=131.81','1330 = 8a + 168(1.63) = 8a + 275.52; 1330 − 275.52 = 8a; 1054.48 = 8a or a = 1054.48/8 = 131.81   [1.63 is printed here while c = 1.64 above]',exampleId=E68)]
P=lambda *ks:dict(type='paragraphs',ids=[pid(220,k) for k in ks])
s['flow']=[P('a1'),dict(type='equation',index=0),P('a2','a3','h','ah','v1','v2','v3','dh','w1','w2')]
s['sourceNote']='Printed page 210. The lower third of the page is blank. A dark mark at the top-left corner is ignored. Printed spellings kept: "some time difficult" (for sometimes). Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 221 (printed 211) ----------
s=page(221,U,'211','Key points of Unit 6','یونٹ 6 کے اہم نکات','د شپږم واحد مهم ټکي','key-points-unit6')
Flow(s)
head(s,'h','Key points','اہم نکات','مهم ټکي')
L(s,[('k1','A series of observations of the same characteristics arranged according to the time of occurrence is known as time series.','ایک ہی خصوصیات کے مشاہدات کا سلسلہ جو وقوع کے وقت کے مطابق ترتیب دیا گیا ہو وقتی سلسلہ کہلاتا ہے۔','د یو شان ځانګړتیاوو د کتنو لړۍ چې د پېښېدو د وخت له مخې ترتیب شوې وي د وخت لړۍ بلل کېږي.'),
('k2','The description, measurement and isolation of various changes in a time series during a period of time are called analysis of time series.','کسی مدت کے دوران وقتی سلسلے میں مختلف تبدیلیوں کی تفصیل، پیمائش اور علیحدگی وقتی سلسلے کا تجزیہ کہلاتی ہے۔','د یوې مودې په اوږدو کې په وخت لړۍ کې د بېلابېلو بدلونونو بیان، اندازه کول او جلا کول د وخت لړۍ تحلیل بلل کېږي.'),
('k3','The term secular trend means changes occurring in a time series in one direction over a fairly long period of time.','صدیوی رجحان کی اصطلاح کا مطلب وقتی سلسلے میں ایک سمت میں خاصے طویل عرصے میں واقع ہونے والی تبدیلیاں ہیں۔','د عمري تمایل اصطلاح پدې معنا چې په وخت لړۍ کې په یو لوري کې په ښه اوږده مودې کې رامنځته کېدونکي بدلونونه.'),
('k4','A journey from one peak (say prosperity) to another peak (prosperity) is called a cycle.','ایک چوٹی (مثلاً خوشحالی) سے دوسری چوٹی (خوشحالی) تک کا سفر چکر کہلاتا ہے۔','له یوې څوکې (لکه سوکالۍ) څخه بلې څوکې (سوکالۍ) ته سفر یو دوره بلل کېږي.'),
('k5','In a time series only time (t) and values (y) are given. The variable x is obtained by coding the time variable.','وقتی سلسلے میں صرف وقت (t) اور قدریں (y) دی جاتی ہیں۔ متغیر x وقت کے متغیر کی کوڈنگ سے حاصل کیا جاتا ہے۔','په وخت لړۍ کې یوازې وخت (t) او ارزښتونه (y) ورکول کېږي. متغیر x د وخت د متغیر په کوډ کولو سره ترلاسه کېږي.'),
('k6','If the number of years is odd, take x = … −2, −1, 0, 1, 2, … i.e.','اگر سالوں کی تعداد طاق ہو تو x = … −2, −1, 0, 1, 2, … لیں یعنی','که د کلونو شمېر طاق وي نو x = … −2, −1, 0, 1, 2, … واخلئ یعنې')],'unit6-kp-1')
add(s,'k7','If the number of years is even, take x = … −7, −5, −3, −1, 1, 3, 5, 7, … i.e.','اگر سالوں کی تعداد جفت ہو تو x = … −7, −5, −3, −1, 1, 3, 5, 7, … لیں یعنی','که د کلونو شمېر جفت وي نو x = … −7, −5, −3, −1, 1, 3, 5, 7, … واخلئ یعنې',listGroup='unit6-kp-2')
add(s,'k8','The equation of second degree parabola/quadratic trend is given by ŷ = a + bx + cx²','دوسرے درجے کے قطع مکافی/دو درجی رجحان کی مساوات یوں دی جاتی ہے ŷ = a + bx + cx²','د دویم درجې پیراپولا/دوه‌درجي تمایل معادله داسې ورکول کېږي ŷ = a + bx + cx²',listGroup='unit6-kp-3')
add(s,'k9','Three normal equation for a, b and c are;','a, b اور c کے لیے تین معمول کی مساواتیں یہ ہیں؛','د a, b او c لپاره درې نورمال معادلې دا دي؛',listGroup='unit6-kp-3')
s['tables']=[table('Odd number of years: coded time','سالوں کی طاق تعداد: کوڈ شدہ وقت','د کلونو طاق شمېر: کوډ شوی وخت',[c('Years','سال','کلونه')]+[c(str(v)) for v in range(2001,2006)],[row('Coded time (x)','کوڈ شدہ وقت (x)','کوډ شوی وخت (x)',[-2,-1,0,1,2])]),
 table('Even number of years: coded time','سالوں کی جفت تعداد: کوڈ شدہ وقت','د کلونو جفت شمېر: کوډ شوی وخت',[c('Years','سال','کلونه')]+[c(str(v)) for v in range(2010,2016)],[row('Coded time (x)','کوڈ شدہ وقت (x)','کوډ شوی وخت (x)',[-5,-3,-1,1,3,5])])]
s['equations']+=[eqn(221,'n1',N1[0],N1[1]),eqn(221,'n2',N2[0],N2[1]),eqn(221,'n3',N3[0],N3[1])]
P=lambda *ks:dict(type='paragraphs',ids=[pid(221,k) for k in ks])
s['flow']=[P('h','k1','k2','k3','k4','k5','k6'),dict(type='table',index=0),P('k7'),dict(type='table',index=1),P('k8','k9'),dict(type='equation',index=0),dict(type='equation',index=1),dict(type='equation',index=2)]
s['sourceNote']='Printed page 211. Key points of the unit as a bulleted list. A black dot near the first coded-time table is ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 222 (printed 212) ----------
s=page(222,U,'212','Exercise-6: Q6.1 Fill in the blanks · Q6.2 Choose the correct statement (i)–(vi)','مشق-6: سوال 6.1 خالی جگہیں پُر کریں · سوال 6.2 صحیح بیان منتخب کریں (i)–(vi)','تمرین-6: پوښتنه 6.1 تشې ډکې کړئ · پوښتنه 6.2 سم بیان وټاکئ (i)–(vi)','exercise6-a',layout='exercise')
Flow(s)
head(s,'h','Exercise-6','مشق-6','تمرین-6',exerciseId='stat11-ex6')
head(s,'h61','6.1 Fill in the blanks with suitable words.','6.1 خالی جگہوں کو موزوں الفاظ سے پُر کریں۔','6.1 تشې په مناسبو کلمو ډکې کړئ.',exerciseId='stat11-ex6-1')
F1=[('A time series is a set of values arranged in ____________ order.','وقتی سلسلہ قدروں کا وہ مجموعہ ہے جو ____________ ترتیب میں ہو۔','د وخت لړۍ د ارزښتونو هغه ټولګه ده چې په ____________ ترتیب کې وي.'),
('Two or more time series can be compared by ____________ analysis.','دو یا زیادہ وقتی سلسلوں کا موازنہ ____________ تجزیے سے کیا جا سکتا ہے۔','دوه یا ډېرې وخت لړۍ د ____________ تحلیل په واسطه پرتله کېدای شي.'),
('A time series consist of at the most ____________ components.','وقتی سلسلہ زیادہ سے زیادہ ____________ اجزاء پر مشتمل ہوتا ہے۔','د وخت لړۍ تر ډېره ____________ برخې لري.'),
('The component representing the long term fluctuation of a time series is called ____________.','وقتی سلسلے کے طویل مدتی اتار چڑھاؤ کی نمائندگی کرنے والا جزو ____________ کہلاتا ہے۔','هغه برخه چې د وخت لړۍ اوږدمهاله بدلونونه استازیتوب کوي ____________ بلل کېږي.'),
('Periodic changes in a business time series are called ____________.','کاروباری وقتی سلسلے میں دوری تبدیلیاں ____________ کہلاتی ہیں۔','په سوداګریزه وخت لړۍ کې دوري بدلونونه ____________ بلل کېږي.'),
('The moving average method eliminates ____________.','متحرک اوسط کا طریقہ ____________ کو ختم کرتا ہے۔','د خوځېدونکي اوسط طریقه ____________ له منځه وړي.'),
('Cyclic movement in a time series occurs due to ____________.','وقتی سلسلے میں دوری حرکت ____________ کی وجہ سے واقع ہوتی ہے۔','په وخت لړۍ کې دوري حرکت د ____________ له امله رامنځته کېږي.'),
('The conclusions drawn from time series analysis are ____________ true.','وقتی سلسلے کے تجزیے سے اخذ کردہ نتائج ____________ درست ہوتے ہیں۔','د وخت لړۍ له تحلیل څخه ترلاسه شوې پایلې ____________ سمې دي.'),
('Data concerning events over a period of time is called ____________.','ایک مدت کے دوران واقعات سے متعلق اعداد و شمار ____________ کہلاتے ہیں۔','د یوې مودې په اوږدو کې د پېښو په اړه معلومات ____________ بلل کېږي.'),
('The graph constructed for time series data is known as ____________.','وقتی سلسلے کے اعداد و شمار کے لیے بنایا گیا گراف ____________ کہلاتا ہے۔','د وخت لړۍ معلوماتو لپاره جوړ شوی ګراف ____________ بلل کېږي.')]
for i,(a,b,d) in enumerate(F1): q(s,f'f{i+1}',f'({rom[i]}) {a}',f'({rom[i]}) {b}',f'({rom[i]}) {d}',f'stat11-ex6-1-{rom[i]}')
head(s,'h62','6.2 Choose the correct statement.','6.2 صحیح بیان منتخب کریں۔','6.2 سم بیان وټاکئ.',exerciseId='stat11-ex6-2')
M=[(1,'(i) A time series consists of','(i) وقتی سلسلہ پر مشتمل ہوتا ہے','(i) د وخت لړۍ لري',('two components','three components','four components','five components'),('دو اجزاء پر','تین اجزاء پر','چار اجزاء پر','پانچ اجزاء پر'),('دوه برخې','درې برخې','څلور برخې','پنځه برخې')),
(2,'(ii) The forecasts on the basis of a time series is','(ii) وقتی سلسلے کی بنیاد پر پیش گوئیاں ہوتی ہیں','(ii) د وخت لړۍ پر بنسټ وړاندوینې دي',('cent per cent true','true to a great extent','never true','accurate'),('سو فیصد درست','بڑی حد تک درست','کبھی درست نہیں','درست'),('سلو په سلو سمې','ډېره برخه سمې','هېڅکله سمې نه','دقیقې')),
(3,'(iii) The component of a time series attached to long term variations is terms as','(iii) وقتی سلسلے کا وہ جزو جو طویل مدتی تغیرات سے وابستہ ہے کہلاتا ہے','(iii) د وخت لړۍ هغه برخه چې له اوږدمهاله تغیراتو سره تړلې ده بلل کېږي',('cyclic variation','secular trend','irregular variation','all of the above'),('دوری تغیر','صدیوی رجحان','بے قاعدہ تغیر','مندرجہ بالا سب'),('دوري تغیر','عمري تمایل','بې‌قاعده تغیر','پورتني ټول')),
(4,'(iv) Salient factors responsible for seasonal variations are','(iv) موسمی تغیرات کے ذمہ دار نمایاں عوامل ہیں','(iv) د موسمي تغیراتو مسوول مهم عوامل دي',('weather','special customs','festivals','all of the above'),('موسم','خاص رسوم','تہوار','مندرجہ بالا سب'),('هوا','ځانګړي رواجونه','ختمې','پورتني ټول')),
(5,'(v) Trend in a time series means','(v) وقتی سلسلے میں رجحان کا مطلب ہے','(v) په وخت لړۍ کې تمایل پدې معنا',('long term regular movement','short term regular movement','both (a) and (b)','neither (a) or (b)'),('طویل مدتی باقاعدہ حرکت','قلیل مدتی باقاعدہ حرکت','(الف) اور (ب) دونوں','نہ (الف) نہ (ب)'),('اوږدمهاله منظمه حرکت','لنډمهاله منظمه حرکت','(a) او (b) دواړه','نه (a) نه (b)')),
(6,'(vi) Value of b in the trend line ŷ = a + bx is','(vi) رجحان کی لکیر ŷ = a + bx میں b کی قدر ہے','(vi) د تمایل کرښې ŷ = a + bx کې د b ارزښت دی',('always positive','always negative','both positive and negative','zero'),('ہمیشہ مثبت','ہمیشہ منفی','مثبت اور منفی دونوں','صفر'),('تل مثبت','تل منفي','مثبت او منفي دواړه','صفر'))]
seq=['h','h61']+[f'f{i+1}' for i in range(10) if False]
build(s,222,['h','h61']+[f'f{i}' for i in range(1,11)]+['h62'],[])
last=s['flow']
for i,a,b,d,oe,ou,op in M:
    keys=mcq(s,i,a,b,d,oe,ou,op)
    last.append(dict(type='paragraphs',ids=[pid(222,k) for k in keys]))
# merge consecutive paragraph blocks
merged=[]
for blk in last:
    if merged and merged[-1]['type']=='paragraphs' and blk['type']=='paragraphs': merged[-1]['ids']+=blk['ids']
    else: merged.append(blk)
s['flow']=merged
s['sourceNote']='Printed page 212. Printed spellings kept: "terms as" (for termed as), "cent per cent". Q6.1 has ten items (i)–(x); item (viii) is printed over two lines. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
