from statlib import *
c=cell
U='dispersion-skewness-kurtosis'
def pid(n,k): return f'stat11-s{n:03}-{k}'
def L(s,items,group):
    for k,a,b,d in items: add(s,k,a,b,d,listGroup=group)
def build(s,n,seq,eqs):
    """seq: 'key' paragraph, 'E:key' equation, 'T:i' table."""
    base=len(s['equations'])
    s['equations']+=[eqn(n,k,l,t,**({'exampleId':ex} if ex else {})) for k,l,t,ex in eqs]
    idx={k:base+i for i,(k,_,_,_) in enumerate(eqs)}
    flow=[]
    for it in seq:
        if it.startswith('E:'): flow.append(dict(type='equation',index=idx[it[2:]]))
        elif it.startswith('T:'): flow.append(dict(type='table',index=int(it[2:])))
        else:
            if flow and flow[-1]['type']=='paragraphs': flow[-1]['ids'].append(pid(n,it))
            else: flow.append(dict(type='paragraphs',ids=[pid(n,it)]))
    s['flow']=flow
E7='stat11-ex-3-7'; E8='stat11-ex-3-8'; E9='stat11-ex-3-9'
# ---------- scan 107 (printed 99) ----------
s=page(107,U,'99','Example 3.7 (solution end) · Example 3.8: discrete series (start)','مثال 3.7 (حل کا اختتام) · مثال 3.8: منفصل سلسلہ (آغاز)','بېلګه 3.7 (د حل پای) · بېلګه 3.8: منفصله لړۍ (پیل)','md-2')
Flow(s)
add(s,'a1','(i) Mean deviation from mean is given by','(i) اوسط سے اوسط انحراف یوں دیا جاتا ہے','(i) له اوسط څخه اوسط انحراف داسې ورکول کېږي',role='solution',exampleId=E7)
add(s,'a2','(ii) Mean deviation from median is given by','(ii) وسطانیہ سے اوسط انحراف یوں دیا جاتا ہے','(ii) له میانې څخه اوسط انحراف داسې ورکول کېږي',role='solution',exampleId=E7)
add(s,'a3','For Median first arrange the data in ascending order as 2, 5, 6, 6, 8, 9, 12, 13, 16, 23. Since n = 10 is even','وسطانیہ کے لیے پہلے اعداد و شمار کو صعودی ترتیب میں لکھیں: 2, 5, 6, 6, 8, 9, 12, 13, 16, 23۔ چونکہ n = 10 جفت ہے','د میانې لپاره لومړی معلومات په پورته‌کېدونکې ترتیب ولیکئ: 2, 5, 6, 6, 8, 9, 12, 13, 16, 23. ځکه چې n = 10 جفت دی',role='solution',exampleId=E7)
add(s,'a4','Now compute |x − Median| in the table above we have','اب اوپر دیے گئے جدول میں |x − Median| حساب کریں تو ہمیں ملتا ہے','اوس پورته جدول کې |x − Median| محاسبه کړئ نو موږ لرو',role='solution',exampleId=E7)
add(s,'i2','(ii) Mean deviation in case of discrete series or grouped data.','(ii) منفصل سلسلے یا گروہی اعداد و شمار کی صورت میں اوسط انحراف۔','(ii) د منفصلې لړۍ یا ګروپي معلوماتو په حالت کې اوسط انحراف.')
head(s,'ex8','Example: 3.8','مثال: 3.8','بېلګه: 3.8',exampleId=E8)
add(s,'q8','For the data given below, calculate mean deviation from (i) mean (ii) median also compute coefficient of mean deviation.','نیچے دیے گئے اعداد و شمار کے لیے (i) اوسط (ii) وسطانیہ سے اوسط انحراف حساب کریں اور اوسط انحراف کا عددی سر بھی معلوم کریں۔','د لاندې ورکړل شویو معلوماتو لپاره له (i) اوسط (ii) میانې څخه اوسط انحراف محاسبه کړئ او د اوسط انحراف ضریب هم ومومئ.',role='question',exampleId=E8)
s['tables']=[table('Example 3.8: x and f','مثال 3.8: x اور f','بېلګه 3.8: x او f',[c('x:')]+[c(str(v)) for v in [4,6,8,10,12,14,16]],[[c('f:')]+[c(str(v)) for v in [2,4,5,3,2,1,4]]],exampleId=E8)]
eq=[('a',r'\text{M.D}=\dfrac{\sum|x-\bar{x}|}{n}\quad\text{and}\quad\bar{x}=\dfrac{\sum x}{n}=\dfrac{100}{10}=10','M.D = Σ|x − x̄|/n and x̄ = Σx/n = 100/10 = 10',E7),
 ('b',r'\therefore\ \text{M.D}=\dfrac{48}{10}=4.8\qquad\text{(Absolute dispersion)}','∴ M.D = 48/10 = 4.8   (Absolute dispersion)',E7),
 ('c',r'\text{Coefficient of M.D}=\dfrac{\text{M.D}}{\bar{x}}=\dfrac{4.8}{10}=0.48\qquad\text{(Relative dispersion)}','Coefficient of M.D = M.D/x̄ = 4.8/10 = 0.48   (Relative dispersion)',E7),
 ('d',r'\text{M.D}=\dfrac{\sum|x-\text{Median}|}{n}','M.D = Σ|x − Median|/n',E7),
 ('e',r'\therefore\ \text{Median}=\dfrac12\left[\dfrac{n}{2}\text{th value}+\left(\dfrac{n}{2}+1\right)\text{th value}\right]','∴ Median = ½[(n/2)th value + (n/2 + 1)th value]',E7),
 ('f',r'=\dfrac12\left[\dfrac{10}{2}\text{th value}+\left(\dfrac{10}{2}+1\right)\text{th value}\right]','= ½[(10/2)th value + (10/2 + 1)th value]',E7),
 ('g',r'=\dfrac12[\,5\text{th value}+6\text{th value}\,]=\dfrac12[8+9]=\dfrac{17}{2}=8.5','= ½[5th value + 6th value] = ½[8 + 9] = 17/2 = 8.5',E7),
 ('h',r'\text{M.D}=\dfrac{46}{10}=4.6\qquad\text{(Absolute dispersion)}','M.D = 46/10 = 4.6   (Absolute dispersion)',E7),
 ('i',r'\text{Coefficient of M.D}=\dfrac{\text{M.D}}{\text{Median}}=\dfrac{4.6}{8.5}=0.54\qquad\text{(Relative dispersion)}','Coefficient of M.D = M.D/Median = 4.6/8.5 = 0.54   (Relative dispersion)',E7)]
build(s,107,['a1','E:a','E:b','E:c','a2','E:d','a3','E:e','E:f','E:g','a4','E:h','E:i','i2','ex8','q8','T:0'],eq)
s['sourceNote']='Printed page 99. Continues the solution of Example 3.7 from the previous page. The first lines are labelled (i) and (ii) as printed. The data of Example 3.8 are printed as aligned x and f rows. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 108 (printed 100) ----------
s=page(108,U,'100','Example 3.8: solution','مثال 3.8: حل','بېلګه 3.8: حل','md-3')
Flow(s)
head(s,'sol8','Solution:','حل:','حل:',exampleId=E8)
add(s,'b1','(i) Mean deviation from mean is given by','(i) اوسط سے اوسط انحراف یوں دیا جاتا ہے','(i) له اوسط څخه اوسط انحراف داسې ورکول کېږي',role='solution',exampleId=E8)
add(s,'b2','(ii) Mean deviation from median is given by M.D = Σf|x − Median| / Σf','(ii) وسطانیہ سے اوسط انحراف M.D = Σf|x − Median| / Σf سے دیا جاتا ہے','(ii) له میانې څخه اوسط انحراف د M.D = Σf|x − Median| / Σf په واسطه ورکول کېږي',role='solution',exampleId=E8)
add(s,'b3','Here Σf = 21 is odd ∴ Median = ((Σf + 1)/2)th value = (22/2)th value = 11th value. This implies that [Median] = 8','یہاں Σf = 21 طاق ہے ∴ وسطانیہ = ((Σf + 1)/2)ویں قدر = (22/2)ویں قدر = 11ویں قدر۔ اس کا مطلب ہے کہ [وسطانیہ] = 8','دلته Σf = 21 طاق دی ∴ میانه = ((Σf + 1)/2) ارزښت = (22/2) ارزښت = 11م ارزښت. دا پدې معنا ده چې [میانه] = 8',role='solution',exampleId=E8,sourceGap=dict(note='In the scan the word "Median" before "= 8" in "This implies that … = 8" is missing; it is shown here in square brackets.'))
xs=[4,6,8,10,12,14,16]; fr=[2,4,5,3,2,1,4]; fx=[8,24,40,30,24,14,64]; cf=[2,6,11,14,16,17,21]
dm=['5.7','3.7','1.7','0.3','2.3','4.3','6.3']; fdm=['11.4','14.8','8.5','0.9','4.6','4.3','25.2']; dd=[4,2,0,2,4,6,8]; fdd=[8,8,0,6,8,6,32]
s['tables']=[table('Example 3.8 solution table','مثال 3.8 کا حل: جدول','د بېلګې 3.8 د حل جدول',[c('x'),c('f'),c('fx'),c('c.f'),c('|x − x̄|'),c('f|x − x̄|'),c('|x − Median|'),c('f|x − Median|')],
 [[c(str(xs[i])),c(str(fr[i])),c(str(fx[i])),c(str(cf[i])),c(dm[i]),c(fdm[i]),c(str(dd[i])),c(str(fdd[i]))] for i in range(7)]+[[c('Total','میزان','ټولیز'),c('21'),c('204'),c('–'),c('–'),c('69.7'),c('–'),c('68')]],exampleId=E8)]
eq=[('a',r'\text{M.D}=\dfrac{\sum f|x-\bar{x}|}{\sum f}\quad\text{where }\bar{x}=\dfrac{\sum fx}{\sum f}=\dfrac{204}{21}=9','M.D = Σf|x − x̄|/Σf where x̄ = Σfx/Σf = 204/21 = 9',E8),
 ('b',r'\therefore\ \text{M.D}=\dfrac{69.7}{21}=3.32\qquad\text{(Absolute dispersion)}','∴ M.D = 69.7/21 = 3.32   (Absolute dispersion)',E8),
 ('c',r'\text{Coefficient of M.D}=\dfrac{\text{M.D}}{\bar{x}}=\dfrac{3.32}{9.7}=0.34\qquad\text{(Relative dispersion)}','Coefficient of M.D = M.D/x̄ = 3.32/9.7 = 0.34   (Relative dispersion) [printed 9.7]',E8),
 ('d',r'\therefore\ \text{M.D}=\dfrac{68}{21}=3.24\qquad\text{(Absolute dispersion)}','∴ M.D = 68/21 = 3.24   (Absolute dispersion)',E8),
 ('e',r'\text{Coefficient of M.D}=\dfrac{\text{M.D}}{\text{Median}}=\dfrac{3.24}{8}=0.41\qquad\text{(Relative dispersion)}','Coefficient of M.D = M.D/Median = 3.24/8 = 0.41   (Relative dispersion)',E8)]
build(s,108,['sol8','T:0','b1','E:a','E:b','E:c','b2','b3','E:d','E:e'],eq)
s['sourceNote']='Printed page 100. In the printed coefficient line the denominator is "9.7" although x̄ = 9 (3.32/9 = 0.37; printed result 0.34 matches 3.32/9.7); kept as printed. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 109 (printed 101) ----------
s=page(109,U,'101','Example 3.9: continuous series','مثال 3.9: مسلسل سلسلہ','بېلګه 3.9: دوامداره لړۍ','md-4')
Flow(s)
add(s,'i3','(iii) Mean deviation in case of continuous series or grouped data','(iii) مسلسل سلسلے یا گروہی اعداد و شمار کی صورت میں اوسط انحراف','(iii) د دوامدارې لړۍ یا ګروپي معلوماتو په حالت کې اوسط انحراف')
head(s,'ex9','Example: 3.9','مثال: 3.9','بېلګه: 3.9',exampleId=E9)
add(s,'q9','Evaluate the mean deviation from mean and median; also compute coefficients of mean deviation.','اوسط اور وسطانیہ سے اوسط انحراف کی قدر معلوم کریں؛ اوسط انحراف کے عددی سر بھی حساب کریں۔','له اوسط او میانې څخه اوسط انحراف ارزونه وکړئ؛ د اوسط انحراف ضریبونه هم محاسبه کړئ.',role='question',exampleId=E9)
head(s,'sol9','Solution:','حل:','حل:',exampleId=E9)
add(s,'c1','(i) Mean deviation from mean:','(i) اوسط سے اوسط انحراف:','(i) له اوسط څخه اوسط انحراف:',role='solution',exampleId=E9)
add(s,'c2','(ii) Mean deviation from median:','(ii) وسطانیہ سے اوسط انحراف:','(ii) له میانې څخه اوسط انحراف:',role='solution',exampleId=E9)
add(s,'c3','Here Σf = 40 is even ∴ Median = (Σf/2)th value = (40/2)th value = 20th value. This implies that Median lies in the group (144.5 – 153.5)','یہاں Σf = 40 جفت ہے ∴ وسطانیہ = (Σf/2)ویں قدر = (40/2)ویں قدر = 20ویں قدر۔ اس کا مطلب ہے کہ وسطانیہ گروہ (144.5 – 153.5) میں واقع ہے','دلته Σf = 40 جفت دی ∴ میانه = (Σf/2) ارزښت = (40/2) ارزښت = 20م ارزښت. دا پدې معنا ده چې میانه په ګروپ (144.5 – 153.5) کې پرته ده',role='solution',exampleId=E9)
cl=['118 – 126','127 – 135','136 – 144','145 – 153','154 – 162','163 – 171','172 – 180']; f9=[3,5,9,12,5,4,2]
bd=['117.5 – 126.5','126.5 – 135.5','135.5 – 144.5','144.5 – 153.5','153.5 – 162.5','162.5 – 171.5','171.5 – 180.5']
x9=[122,131,140,149,158,167,176]; fx9=[366,655,1260,1788,790,668,352]; cf9=[3,8,17,29,34,38,40]
a9=['74.925','79.875','62.775','24.300','55.125','80.100','58.050']; b9=['74.25','78.75','60.75','27.00','56.25','81.00','58.50']
s['tables']=[table('Example 3.9: classes and frequency','مثال 3.9: طبقات اور تعدد','بېلګه 3.9: ټولګي او فریکونسي',[c('Classes:','طبقات:','ټولګي:')]+[c(v) for v in cl],[[c('Frequency:','تعدد:','فریکونسي:')]+[c(str(v)) for v in f9]],exampleId=E9),
 table('Example 3.9 solution table','مثال 3.9 کا حل: جدول','د بېلګې 3.9 د حل جدول',[c('Classes','طبقات','ټولګي'),c('f'),c('Class boundaries','طبقاتی حدود','د ټولګیو حدود'),c('x'),c('fx'),c('c.f'),c('f|x − x̄|'),c('f|x − Median|')],
 [[c(cl[i]),c(str(f9[i])),c(bd[i]),c(str(x9[i])),c(str(fx9[i])),c(str(cf9[i])),c(a9[i]),c(b9[i])] for i in range(7)]+[[c('Total','میزان','ټولیز'),c('40'),c('–'),c('–'),c('5879'),c('–'),c('435.350'),c('436.5')]],exampleId=E9)]
eq=[('a',r'\text{M.D}=\dfrac{\sum f|x-\bar{x}|}{\sum f}\ \text{ where, }\ \bar{x}=\dfrac{\sum fx}{\sum f}=\dfrac{5879}{40}=146.975','M.D = Σf|x − x̄|/Σf where, x̄ = Σfx/Σf = 5879/40 = 146.975',E9),
 ('b',r'\therefore\ \text{M.D}=\dfrac{435.35}{40}=10.88\qquad\text{(Absolute dispersion)}','∴ M.D = 435.35/40 = 10.88   (Absolute dispersion)',E9),
 ('c',r'\text{Coefficient of M.D}=\dfrac{\text{M.D}}{\bar{x}}=\dfrac{10.88}{146.975}=0.07\qquad\text{(Relative dispersion)}','Coefficient of M.D = M.D/x̄ = 10.88/146.975 = 0.07   (Relative dispersion)',E9),
 ('d',r'\text{M.D}=\dfrac{\sum f|x-\text{Median}|}{\sum f}','M.D = Σf|x − Median|/Σf',E9),
 ('e',r'\therefore\ \text{Median}=l_1+\dfrac{h}{f}\left(\dfrac{\sum f}{2}-c\right)=144.5+\dfrac{9}{12}\left(\dfrac{40}{2}-17\right)=146.75','∴ Median = l1 + (h/f)(Σf/2 − c) = 144.5 + (9/12)(40/2 − 17) = 146.75',E9)]
build(s,109,['i3','ex9','q9','T:0','sol9','T:1','c1','E:a','E:b','E:c','c2','E:d','c3','E:e'],eq)
s['sourceNote']='Printed page 101. The question data (classes and frequencies) are printed as aligned rows above the "Evaluate…" sentence and are shown in a table before the solution. A handwritten mark and stray dots are ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 110 (printed 102) ----------
s=page(110,U,'102','Example 3.9 (end) · 3.4.2 Advantages and disadvantages · 3.5 Standard deviation and variance · 3.5.1 Standard deviation','مثال 3.9 (اختتام) · 3.4.2 فوائد اور نقصانات · 3.5 معیاری انحراف اور تغیر · 3.5.1 معیاری انحراف','بېلګه 3.9 (پای) · 3.4.2 ګټې او زیانونه · 3.5 معیاري انحراف او وریانس · 3.5.1 معیاري انحراف','sd-1')
Flow(s)
head(s,'h342','3.4.2 Advantages and disadvantages of mean deviation','3.4.2 اوسط انحراف کے فوائد اور نقصانات','3.4.2 د اوسط انحراف ګټې او زیانونه')
add(s,'ah','Advantages:','فوائد:','ګټې:')
L(s,[('v1','(i) It utilizes all the observations of the data set.','(i) یہ اعداد و شمار کے مجموعے کے تمام مشاہدات استعمال کرتا ہے۔','(i) دا د معلوماتو د ټولګې ټولې کتنې کاروي.'),('v2','(ii) It is simple to understand and easy to calculate.','(ii) یہ سمجھنے میں آسان اور حساب کرنے میں سادہ ہے۔','(ii) دا د پوهېدو لپاره ساده او د محاسبې لپاره اسانه دی.'),('v3','(iii) In case of mean deviation from median, it is least affected by extreme values.','(iii) وسطانیہ سے اوسط انحراف کی صورت میں یہ انتہائی قدروں سے سب سے کم متاثر ہوتا ہے۔','(iii) له میانې څخه د اوسط انحراف په حالت کې دا د سختو ارزښتونو لخوا تر ټولو لږ اغېزمن کېږي.')],'md-adv')
add(s,'dh','Disadvantages:','نقصانات:','زیانونه:')
L(s,[('w1','(i) It is not used very often because all the deviations are taken as positive.','(i) یہ اکثر استعمال نہیں ہوتا کیونکہ تمام انحرافات کو مثبت لیا جاتا ہے۔','(i) دا ډېر نه کارول کېږي ځکه چې ټول انحرافات مثبت اخیستل کېږي.'),('w2','(ii) It is not suited for further algebraic treatment.','(ii) یہ مزید الجبری عمل کے لیے موزوں نہیں۔','(ii) دا د نورې الجبري پروسې لپاره مناسب نه دی.')],'md-dis')
head(s,'h35','3.5 Standard deviation and Variance','3.5 معیاری انحراف اور تغیر','3.5 معیاري انحراف او وریانس')
head(s,'h351','3.5.1 Standard deviation','3.5.1 معیاری انحراف','3.5.1 معیاري انحراف')
add(s,'t351','The standard deviation is the most commonly used measure of dispersion. It fulfills all the requisites of a good measure of dispersion except that it is sensitive to extreme values. It is abbreviated as S.D. A small value of the S.D for a data set indicates less spread while a larger value of the S.D indicates more spread around the mean. It is denoted by σ (lower case sigma of the Greek alphabets) in population case and s in sample case. The positive square root of the average of the squared deviations of observations taken from mean is called standard deviation. Mathematically;','معیاری انحراف انتشار کا سب سے زیادہ استعمال ہونے والا پیمانہ ہے۔ یہ انتشار کے اچھے پیمانے کے تمام تقاضے پورے کرتا ہے سوائے اس کے کہ یہ انتہائی قدروں کے لیے حساس ہے۔ اسے S.D کے طور پر مختصر کیا جاتا ہے۔ اعداد و شمار کے مجموعے کے لیے S.D کی چھوٹی قدر کم پھیلاؤ ظاہر کرتی ہے جبکہ S.D کی بڑی قدر اوسط کے گرد زیادہ پھیلاؤ ظاہر کرتی ہے۔ اسے آبادی کی صورت میں σ (یونانی حروفِ تہجی کا چھوٹا سگما) اور نمونے کی صورت میں s سے ظاہر کیا جاتا ہے۔ اوسط سے لیے گئے مشاہدات کے مربع انحرافات کے اوسط کا مثبت جذر معیاری انحراف کہلاتا ہے۔ ریاضیاتی طور پر؛','معیاري انحراف د خپراوي تر ټولو ډېر کارېدونکې اندازه ده. دا د خپراوي د ښې اندازې ټولې اړتیاوې پوره کوي پرته له دې چې دا د سختو ارزښتونو لپاره حساسه ده. دا د S.D په توګه لنډېږي. د معلوماتو د ټولګې لپاره د S.D کوچنی ارزښت لږ خپراوی ښيي پداسې حال کې چې د S.D لوی ارزښت د اوسط شاوخوا ډېر خپراوی ښيي. دا د ټولنې په حالت کې په σ (د یوناني ابجد کوچنی سیګما) او د نمونې په حالت کې په s ښودل کېږي. له اوسط څخه اخیستل شویو کتنو د مربع انحرافاتو د اوسط مثبت جذر معیاري انحراف بلل کېږي. ریاضیاتي ډول؛')
add(s,'pop','Population standard deviation: (Parameter)','آبادی کا معیاری انحراف: (پیرامیٹر)','د ټولنې معیاري انحراف: (پارامېټر)')
add(s,'smp','Sample standard deviation: (Statistic)','نمونے کا معیاری انحراف: (شماریہ)','د نمونې معیاري انحراف: (احصایه)')
add(s,'nt','Note that the sample S.D underestimates the population S.D when the denominator in the sample formula for S.D is n. However, the sample S.D does not underestimate the population S.D if the denominator in the sample formula is','نوٹ کریں کہ جب S.D کے نمونے کے فارمولے میں نسب نما n ہو تو نمونے کا S.D آبادی کے S.D کو کم تخمینہ کرتا ہے۔ تاہم، اگر نمونے کے فارمولے میں نسب نما', 'پام وکړئ چې کله د S.D د نمونې په فورمول کې مخرج n وي نو د نمونې S.D د ټولنې S.D کم اټکل کوي. خو که د نمونې په فورمول کې مخرج',sourceGap=dict(note='The sentence continues on the next page.'))
s['equations']=[]
eq=[('a',r'\dfrac{436.5}{40}','',E9)]
# equations for the page
s['equations']+=[eqn(110,'a',r'\therefore\ \text{M.D}=\dfrac{436.5}{40}=10.91\qquad\text{(Absolute dispersion)}','∴ M.D = 436.5/40 = 10.91   (Absolute dispersion)',exampleId=E9),
 eqn(110,'b',r'\text{Coefficient of M.D}=\dfrac{\text{M.D}}{\text{Median}}=\dfrac{10.91}{146.75}=0.07\qquad\text{(Relative dispersion)}','Coefficient of M.D = M.D/Median = 10.91/146.75 = 0.07   (Relative dispersion)',exampleId=E9),
 eqn(110,'c',r'\sigma=\sqrt{\dfrac{\sum(x-\mu)^2}{N}}\qquad\text{(Parameter)}','σ = √(Σ(x − μ)²/N)   (Parameter)'),
 eqn(110,'d',r's=\sqrt{\dfrac{\sum(x-\bar{x})^2}{n}}\qquad\text{(Statistic)}','s = √(Σ(x − x̄)²/n)   (Statistic)')]
P=lambda *ks:dict(type='paragraphs',ids=[pid(110,k) for k in ks])
s['flow']=[dict(type='equation',index=0),dict(type='equation',index=1),P('h342','ah','v1','v2','v3','dh','w1','w2','h35','h351','t351','pop'),dict(type='equation',index=2),P('smp'),dict(type='equation',index=3),P('nt')]
s['sourceNote']='Printed page 102. The first lines complete Example 3.9. Handwritten Urdu words next to "Advantages" and the 3.5 heading are ignored. "Disadvantages" is printed as given. The formula lines are printed with the labels "Population standard deviation:" and "Sample standard deviation:" on the left and "(Parameter)", "(Statistic)" on the right. Header graphics and watermark excluded.'
s['vocabulary']={'standard deviation':dict(ur='معیاری انحراف',ps='معیاري انحراف'),'variance':dict(ur='تغیر',ps='وریانس')}
save(s)
