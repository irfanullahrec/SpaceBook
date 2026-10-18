from stathelp import *
c=cell
U='dispersion-skewness-kurtosis'
E26='stat11-ex-3-26'; E27='stat11-ex-3-27'; E28='stat11-ex-3-28'
SKP=(r"Sk=\dfrac{3(Mean-Median)}{S}","Sk = 3(Mean − Median)/S")
SKB=(r"Sk=\dfrac{Q_1+Q_3-2Q_2}{Q_3-Q_1}","Sk = (Q1 + Q3 − 2Q2)/(Q3 − Q1)")
# ---------- scan 139 (printed 131) ----------
s=page(139,U,'131','Example 3.26 (Bowley end) · Example 3.27: discrete series (Pearson)','مثال 3.26 (باؤلے کا اختتام) · مثال 3.27: منفصل سلسلہ (پیئرسن)','بېلګه 3.26 (د Bowley پای) · بېلګه 3.27: منفصله لړۍ (Pearson)','skewness-4')
Flow(s)
add(s,'a1','It means that given distribution has negative skewness.','اس کا مطلب ہے کہ دی گئی تقسیم منفی کج ہے۔','دا پدې معنا ده چې ورکړل شوی ویش منفي کوړوالی لري.',role='solution',exampleId=E26)
add(s,'a2','Remember that answer of all of the three methods may or may not be same but decision will always be same.','یاد رکھیں کہ تینوں طریقوں کا جواب ایک جیسا ہو بھی سکتا ہے اور نہیں بھی لیکن فیصلہ ہمیشہ ایک ہی ہوگا۔','په یاد ولرئ چې د درېواړو طریقو ځواب کېدای شي یو شان وي یا نه وي خو پرېکړه به تل یو شان وي.')
head(s,'ex27','Example: 3.27','مثال: 3.27','بېلګه: 3.27',exampleId=E27)
add(s,'q27','For the following frequency table, calculate the coefficient of skewness.','درج ذیل تعدد جدول کے لیے کجی کا عددی سر حساب کریں۔','د لاندې فریکونسي جدول لپاره د کوړوالي ضریب محاسبه کړئ.',role='question',exampleId=E27)
head(s,'sol27','Solution:','حل:','حل:',exampleId=E27)
add(s,'a3',"(i) Pearson's coefficient of skewness",'(i) کجی کا پیئرسنی عددی سر','(i) د کوړوالي پیرسني ضریب',role='solution',exampleId=E27)
add(s,'a4','Arranging the given data along with frequencies:','دیے گئے اعداد و شمار کو تعدد کے ساتھ ترتیب دیتے ہوئے:','ورکړل شوي معلومات د فریکونسیو سره ترتیبول:',role='solution',exampleId=E27)
add(s,'a5','As Σf = 109 is odd therefore,','چونکہ Σf = 109 طاق ہے اس لیے،','ځکه چې Σf = 109 طاق دی نو،',role='solution',exampleId=E27,sourceGap=dict(note='The working continues on the next page (Median = …).'))
rows=[('6','6','36','-13.725','188.376','1130.26','6'),('10','10','100','-9.725','94.576','945.76','16'),('14','18','252','-5.725','32.776','589.97','34'),('18','30','540','-1.725','2.976','89.28','64'),('22','15','330','2.275','5.176','77.64','79'),('26','12','312','6.275','39.376','472.52','91'),('30','10','300','10.275','105.576','1055.76','101'),('34','6','204','14.275','20.3776','1222.66','107'),('38','2','76','18.275','333.975','667.952','109')]
s['tables']=[table('Example 3.27: x and f','مثال 3.27: x اور f','بېلګه 3.27: x او f',[c('x:')]+[c(v) for v in ['6','10','14','18','22','26','30','34','38']],[[c('f:')]+[c(v) for v in ['6','10','18','30','15','12','10','6','2']]],exampleId=E27),
 table('Example 3.27 solution table','مثال 3.27 کا حل: جدول','د بېلګې 3.27 د حل جدول',[c('x'),c('f'),c('fx'),c('(x − x̄)'),c('(x − x̄)²'),c('f(x − x̄)²'),c('c.f')],[[c(v) for v in r] for r in rows]+[[c('Total','میزان','ټولیز'),c('109'),c('2150'),c('–'),c('–'),c('6251.794'),c('–')]],exampleId=E27)]
eq=[('b1',r"\text{So }Sk=\dfrac{3+8.5-2(7)}{8.5-3}","So Sk = (3 + 8.5 − 2(7))/(8.5 − 3)",E26),
 ('b2',r"=\dfrac{11.5-14}{5.5}=\dfrac{-2.5}{5.5}=-0.45","= (11.5 − 14)/5.5 = −2.5/5.5 = −0.45",E26),
 ('p0',SKP[0],SKP[1],E27),
 ('p1',r"\bar{x}=\dfrac{\sum fx}{\sum f}=\dfrac{2150}{109}=19.725","x̄ = Σfx/Σf = 2150/109 = 19.725",E27),
 ('p2',r"S=\sqrt{\dfrac{\sum f(x-\bar{x})^2}{\sum f}}=\sqrt{\dfrac{6251.794}{109}}=\sqrt{57.356}=7.57","S = √(Σf(x − x̄)²/Σf) = √(6251.794/109) = √57.356 = 7.57",E27)]
build(s,139,['E:b1','E:b2','a1','a2','ex27','q27','T:0','sol27','a3','E:p0','a4','T:1','E:p1','E:p2','a5'],eq)
s['sourceNote']='Printed page 131. The first lines complete the Bowley working of Example 3.26. The x and f rows of Example 3.27 are shown as a table. A blue ink tick next to "Example: 3.27" is ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 140 (printed 132) ----------
s=page(140,U,'132','Example 3.27 (Pearson end, Bowley) · Example 3.28 (question)','مثال 3.27 (پیئرسن کا اختتام، باؤلے) · مثال 3.28 (سوال)','بېلګه 3.27 (د Pearson پای، Bowley) · بېلګه 3.28 (پوښتنه)','skewness-5')
Flow(s)
add(s,'a1','⇒ The given distribution is positively skewed.','⇒ دی گئی تقسیم مثبت کج ہے۔','⇒ ورکړل شوی ویش مثبت کوړ دی.',role='solution',exampleId=E27)
add(s,'a2',"(ii) Bowley's coefficient of skewness",'(ii) کجی کا باؤلے عددی سر','(ii) د کوړوالي بولي ضریب',role='solution',exampleId=E27)
add(s,'a3','Arranging the data, we have','اعداد و شمار کو ترتیب دیتے ہوئے ہمیں ملتا ہے','معلومات ترتیبول موږ ترلاسه کوو',role='solution',exampleId=E27)
add(s,'a4','Here Σf = 109 is odd','یہاں Σf = 109 طاق ہے','دلته Σf = 109 طاق دی',role='solution',exampleId=E27)
add(s,'a5','⇒ that given distribution has positive skewness.','⇒ کہ دی گئی تقسیم مثبت کجی رکھتی ہے۔','⇒ چې ورکړل شوی ویش مثبت کوړوالی لري.',role='solution',exampleId=E27)
head(s,'ex28','Example: 3.28','مثال: 3.28','بېلګه: 3.28',exampleId=E28)
add(s,'q28','Calculate coefficient of skewness for the following data:','درج ذیل اعداد و شمار کے لیے کجی کا عددی سر حساب کریں:','د لاندې معلوماتو لپاره د کوړوالي ضریب محاسبه کړئ:',role='question',exampleId=E28,sourceGap=dict(note='The solution of Example 3.28 begins on the next page.'))
xs=[('6','6','6'),('10','10','16'),('14','18','34'),('18','30','64'),('22','15','79'),('26','12','91'),('30','10','101'),('34','6','107'),('38','2','109')]
s['tables']=[table('Example 3.27: x, f, c.f','مثال 3.27: x, f, c.f','بېلګه 3.27: x, f, c.f',[c('x'),c('f'),c('c.f')],[[c(v) for v in r] for r in xs]+[[c('Total','میزان','ټولیز'),c('109'),c('–')]],exampleId=E27),
 table('Example 3.28: class and frequency','مثال 3.28: طبقہ اور تعدد','بېلګه 3.28: ټولګی او فریکونسي',[c('class:','طبقہ:','ټولګی:')]+[c(v) for v in ['20 – 24','25 – 29','30 – 34','35 – 39','40 – 44','45 – 49','50 – 54']],[[c('Frequency:','تعدد:','فریکونسي:')]+[c(v) for v in ['22','28','218','227','235','216','54']]],exampleId=E28)]
eq=[('m1',r"\text{Median}=\left(\dfrac{\sum f+1}{2}\right)\text{th item}=\left(\dfrac{109+1}{2}\right)\text{th item}=55\text{th item}=18","Median = ((Σf + 1)/2)th item = ((109 + 1)/2)th item = 55th item = 18",E27),
 ('m2',r"\text{Hence }Sk=\dfrac{3(19.725-18)}{7.57}=\dfrac{5.175}{7.57}=0.68","Hence Sk = 3(19.725 − 18)/7.57 = 5.175/7.57 = 0.68",E27),
 ('b0',SKB[0],SKB[1],E27),
 ('q1',r"\therefore\ Q_1=\left(\dfrac{\sum f+1}{4}\right)\text{th value}=\left(\dfrac{109+1}{4}\right)\text{th value}=27.5\text{th value}\ \Rightarrow\ Q_1=14","∴ Q1 = ((Σf + 1)/4)th value = ((109 + 1)/4)th value = 27.5th value ⇒ Q1 = 14",E27),
 ('q2',r"Q_2=2\left(\dfrac{\sum f+1}{4}\right)\text{th value}=\left(\dfrac{\sum f+1}{2}\right)\text{th value}=\left(\dfrac{109+1}{2}\right)\text{th value}=55\text{th value}\ \Rightarrow\ Q_2=18","Q2 = 2((Σf + 1)/4)th value = ((Σf + 1)/2)th value = ((109 + 1)/2)th value = 55th value ⇒ Q2 = 18",E27),
 ('q3',r"Q_3=3\left(\dfrac{\sum f+1}{4}\right)\text{th value}=3\left(\dfrac{109+1}{2}\right)\text{th value}=82.5\text{th value}\ \Rightarrow\ Q_3=26","Q3 = 3((Σf + 1)/4)th value = 3((109 + 1)/2)th value = 82.5th value ⇒ Q3 = 26   [printed with denominator 2 in the second form]",E27),
 ('sk',r"\therefore\ Sk=\dfrac{Q_1+Q_3-2Q_2}{Q_3-Q_1}=\dfrac{14+26-2(18)}{26-14}=\dfrac{40-36}{12}=\dfrac{4}{12}=0.33","∴ Sk = (Q1 + Q3 − 2Q2)/(Q3 − Q1) = (14 + 26 − 2(18))/(26 − 14) = (40 − 36)/12 = 4/12 = 0.33",E27)]
build(s,140,['E:m1','E:m2','a1','a2','E:b0','a3','T:0','a4','E:q1','E:q2','E:q3','E:sk','a5','ex28','q28','T:1'],eq)
s['sourceNote']='Printed page 132. The first lines complete the Pearson working of Example 3.27. The x, f, c.f table is printed on the left and the working for Q1, Q2, Q3 on its right; the working is shown after the table. Blue ink ticks next to "Example: 3.28" are ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 141 (printed 133) ----------
s=page(141,U,'133','Example 3.28: solution (Pearson, Bowley start)','مثال 3.28: حل (پیئرسن، باؤلے کا آغاز)','بېلګه 3.28: حل (Pearson، د Bowley پیل)','skewness-6')
Flow(s)
head(s,'sol28','Solution:','حل:','حل:',exampleId=E28)
add(s,'a1',"(i) Pearson's coefficient of skewness",'(i) کجی کا پیئرسنی عددی سر','(i) د کوړوالي پیرسني ضریب',role='solution',exampleId=E28)
add(s,'a2','as Σf = 1000 is even ∴ Median = (Σf/2)th value = (1000/2)th value = 500th value ⇒ Median lies in the group (39.5 – 44.5)','چونکہ Σf = 1000 جفت ہے ∴ وسطانیہ = (Σf/2)ویں قدر = (1000/2)ویں قدر = 500ویں قدر ⇒ وسطانیہ گروہ (39.5 – 44.5) میں واقع ہے','ځکه چې Σf = 1000 جفت دی ∴ میانه = (Σf/2) ارزښت = (1000/2) ارزښت = 500م ارزښت ⇒ میانه په ګروپ (39.5 – 44.5) کې پرته ده',role='solution',exampleId=E28)
add(s,'a3','The given distribution is negatively skewed.','دی گئی تقسیم منفی کج ہے۔','ورکړل شوی ویش منفي کوړ دی.',role='solution',exampleId=E28)
add(s,'a4',"(ii) Bowley's coefficient of skewness is",'(ii) کجی کا باؤلے عددی سر یہ ہے','(ii) د کوړوالي بولي ضریب دا دی',role='solution',exampleId=E28)
rows=[('20 – 24','22','22','-3','-66','198','19.5 – 24.5','22'),('25 – 29','28','27','-2','-56','112','24.5 – 29.5','50'),('30 – 34','218','32','-1','-218','218','29.5 – 34.5','268'),('35 – 39','227','37','0','0','0','34.5 – 39.5','495'),('40 – 44','235','42','1','235','235','39.5 – 44.5','730'),('45 – 49','216','47','2','432','864','44.5 – 49.5','946'),('50 – 54','54','52','3','162','486','49.5 – 54.5','1000')]
s['tables']=[table('Example 3.28 solution table','مثال 3.28 کا حل: جدول','د بېلګې 3.28 د حل جدول',[c('Classes:','طبقات:','ټولګي:'),c('f'),c('x'),c('u = (x − 37)/5'),c('fu'),c('fu²'),c('Class boundaries','طبقاتی حدود','د ټولګیو حدود'),c('c.f')],[[c(v) for v in r] for r in rows]+[[c('Total','میزان','ټولیز'),c('1000'),c('–'),c('–'),c('489'),c('2113'),c('–'),c('')]],exampleId=E28)]
eq=[('p0',SKP[0],SKP[1],E28),
 ('p1',r"\bar{x}=A+\dfrac{\sum fu}{\sum f}\times h=37+\dfrac{489}{1000}\times 5=39.45","x̄ = A + (Σfu/Σf) × h = 37 + (489/1000) × 5 = 39.45",E28),
 ('p2',r"\text{So Median}=l_1+\dfrac{h}{f}\left(\dfrac{\sum f}{2}-c\right)","So Median = l1 + (h/f)(Σf/2 − c)",E28),
 ('p3',r"=39.5+\dfrac{5}{235}(500-495)=39.5+\dfrac{25}{235}=39.5+0.11=39.61","= 39.5 + (5/235)(500 − 495) = 39.5 + 25/235 = 39.5 + 0.11 = 39.61",E28),
 ('p4',r"S=\sqrt{\dfrac{\sum fu^2}{\sum f}-\left(\dfrac{\sum fu}{\sum f}\right)^2}\times h=\sqrt{\dfrac{2113}{1000}-\left(\dfrac{489}{1000}\right)^2}\times 5","S = √(Σfu²/Σf − (Σfu/Σf)²) × h = √(2113/1000 − (489/1000)²) × 5",E28),
 ('p5',r"=\sqrt{2.113-0.239}\times 5=\sqrt{1.874}\times 5=(1.368)\times 5=6.845","= √(2.113 − 0.239) × 5 = √1.874 × 5 = (1.368) × 5 = 6.845",E28),
 ('p6',r"\text{Hence }Sk=\dfrac{3(39.45-39.61)}{6.845}=\dfrac{3(-0.16)}{6.845}=\dfrac{-0.48}{6.845}=-0.07","Hence Sk = 3(39.45 − 39.61)/6.845 = 3(−0.16)/6.845 = −0.48/6.845 = −0.07",E28),
 ('b0',SKB[0],SKB[1],E28)]
build(s,141,['sol28','a1','E:p0','T:0','E:p1','a2','E:p2','E:p3','E:p4','E:p5','E:p6','a3','a4','E:b0'],eq)
s['sourceNote']='Printed page 133. In the solution table the last cell of the total row (c.f) is empty and the second-last is a dash. The printed median is 39.61 (39.5 + 0.11). Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 142 (printed 134) ----------
s=page(142,U,'134','Example 3.28: Bowley working (Q1, Q2 start)','مثال 3.28: باؤلے کا حل (Q1، Q2 کا آغاز)','بېلګه 3.28: د Bowley حل (Q1، د Q2 پیل)','skewness-7')
Flow(s)
add(s,'a1','Here n = 1000 is even therefore','یہاں n = 1000 جفت ہے اس لیے','دلته n = 1000 جفت دی نو',role='solution',exampleId=E28)
add(s,'a2','⇒ Q1 lies in the group (29.5 – 34.5)','⇒ Q1 گروہ (29.5 – 34.5) میں واقع ہے','⇒ Q1 په ګروپ (29.5 – 34.5) کې پرته ده',role='solution',exampleId=E28)
add(s,'a3','⇒ Q2 = lies in the group (39.5 – 44.5)','⇒ Q2 = گروہ (39.5 – 44.5) میں واقع ہے','⇒ Q2 = په ګروپ (39.5 – 44.5) کې پرته ده',role='solution',exampleId=E28,sourceGap=dict(note='The working continues on the next page (Q3 and the value of Sk).'))
rows=[('20 – 24','19.5 – 24.5','22','22'),('25 – 29','24.5 – 29.5','28','50'),('30 – 34','29.5 – 34.5','218','268'),('35 – 39','34.5 – 39.5','227','495'),('40 – 44','39.5 – 44.5','235','730'),('45 – 49','44.5 – 49.5','216','946'),('50 – 54','49.5 – 54.5','54','1000')]
s['tables']=[table('Example 3.28: classes, boundaries, f, c.f','مثال 3.28: طبقات، حدود، f، c.f','بېلګه 3.28: ټولګي، حدود، f، c.f',[c('Classes','طبقات','ټولګي'),c('Class boundaries','طبقاتی حدود','د ټولګیو حدود'),c('f'),c('c.f')],[[c(v) for v in r] for r in rows]+[[c('Total','میزان','ټولیز'),c('–'),c('1000'),c('–')]],exampleId=E28)]
eq=[('q1a',r"Q_1=\left(\dfrac{\sum f}{4}\right)\text{th value}=\left(\dfrac{1000}{4}\right)\text{th value}=250\text{th value}","Q1 = (Σf/4)th value = (1000/4)th value = 250th value",E28),
 ('q1b',r"\therefore\ Q_1=l_1+\dfrac{h}{f}\left(\dfrac{\sum f}{4}-c\right)","∴ Q1 = l1 + (h/f)(Σf/4 − c)",E28),
 ('q1c',r"=29.5+\dfrac{5}{218}(250-50)","= 29.5 + (5/218)(250 − 50)",E28),
 ('q1d',r"=29.5+\dfrac{1000}{218}","= 29.5 + 1000/218",E28),
 ('q1e',r"=29.5+4.59","= 29.5 + 4.59",E28),
 ('q1f',r"=34.09","= 34.09",E28),
 ('q2a',r"Q_2=2\left(\dfrac{\sum f}{4}\right)\text{th value}=\left(\dfrac{1000}{2}\right)\text{th value}=500\text{ th value}","Q2 = 2(Σf/4)th value = (1000/2)th value = 500 th value",E28)]
build(s,142,['T:0','a1','E:q1a','a2','E:q1b','E:q1c','E:q1d','E:q1e','E:q1f','E:q2a','a3'],eq)
s['sourceNote']='Printed page 134. The table at the top is the grouped table used for the Bowley method. A dark artefact at the top-left corner is ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
