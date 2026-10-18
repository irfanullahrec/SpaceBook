from statlib import *
from statcharts import _axes
c=cell
U='central-tendency'
def pid(n,k): return f'stat11-s{n:03}-{k}'
def modehist():
    W,H=560,330;Lm,R,Tp,B=70,130,40,70
    o,Y,pw,ph=_axes(W,H,Lm,R,Tp,B,0,20,[0,5,10,15,20],False,'Graphical method of evaluate Mode')
    edges=[9.5,19.5,29.5,39.5,49.5,59.5];hs=[5,10,20,15,3]
    X=lambda v:Lm+pw*0.05+pw*0.9*(v-9.5)/50
    for i,h in enumerate(hs): o+=f'<rect x="{X(edges[i]):.1f}" y="{Y(h):.1f}" width="{X(edges[i+1])-X(edges[i]):.1f}" height="{Y(0)-Y(h):.1f}" fill="#fff" stroke="#1c6aa8" stroke-width="2"/>'
    o+=f'<line x1="{X(29.5):.1f}" y1="{Y(20):.1f}" x2="{X(39.5):.1f}" y2="{Y(15):.1f}" stroke="#1c6aa8" stroke-width="2"/><line x1="{X(39.5):.1f}" y1="{Y(20):.1f}" x2="{X(29.5):.1f}" y2="{Y(10):.1f}" stroke="#1c6aa8" stroke-width="2"/>'
    xm=29.5+10/1.5
    o+=f'<line x1="{X(xm):.1f}" y1="{Y(20-0.5*(xm-29.5)):.1f}" x2="{X(xm):.1f}" y2="{Y(0)-2:.1f}" stroke="#111" stroke-width="2"/><path d="M{X(xm)-5:.1f},{Y(0)-10:.1f} L{X(xm):.1f},{Y(0)-1:.1f} L{X(xm)+5:.1f},{Y(0)-10:.1f}" fill="none" stroke="#111" stroke-width="2"/>'
    for e in edges: o+=T(X(e),Tp+ph+16,str(e),11)
    o+=T(Lm+pw/2,H-10,'Class boundaries',12)+f'<text transform="translate(14 {Tp+ph/2}) rotate(-90)" font-size="11" text-anchor="middle" font-family="Arial">Frequency</text>'
    o+=T(Lm+pw+20,Tp+30,'Scale',12,'start')+T(Lm+pw+20,Tp+46,'on x-axis 1.S.S = 1',11,'start')+T(Lm+pw+20,Tp+60,'on y-axis 1.S.S = 0.5',11,'start')
    return svg(W,H,'Histogram with class boundaries 9.5 to 59.5 and frequencies 5, 10, 20, 15, 3; lines joining the top corners of the tallest bar to its neighbours cross and an arrow drops to about 37.5 on the x-axis',o)
# ---------- scan 83 (printed 75) ----------
s=page(83,U,'75','Mode (end) · 2.4.1 Mode for individual series · Examples 2.21–2.24','عادہ (اختتام) · 2.4.1 انفرادی سلسلے کا عادہ · مثالیں 2.21–2.24','مود (پای) · 2.4.1 د انفرادي لړۍ مود · بېلګې 2.21–2.24','mode-individual')
add(s,'c1','values that occur with the same (highest) frequency has two modes. The distribution in this case is called bimodal. If more than two values in a data set occur with the same (highest) frequency, then it is said to be multimodal.','قدریں جو یکساں (سب سے زیادہ) تعدد کے ساتھ آئیں اس کے دو عادہ ہوتے ہیں۔ اس صورت میں تقسیم دو منوالی کہلاتی ہے۔ اگر اعداد و شمار کے مجموعے میں دو سے زیادہ قدریں یکساں (سب سے زیادہ) تعدد کے ساتھ آئیں تو اسے کثیر منوالی کہا جاتا ہے۔','ارزښتونه چې ورته (تر ټولو لوړې) فریکونسۍ سره راځي دوه مودونه لري. په دې حالت کې ویش دوه‌مودي بلل کېږي. که په معلوماتو ټولګه کې له دوو څخه ډېر ارزښتونه ورته (تر ټولو لوړې) فریکونسۍ سره راشي نو ویل کېږي چې ډېر‌مودي دی.',sourceGap=dict(note='Completes the sentence from the previous page ("A data set with two …").'))
head(s,'h241','2.4.1 Calculation of mode for individual series or ungrouped data','2.4.1 انفرادی سلسلے یا غیر گروہی اعداد و شمار کے لیے عادہ کا حساب','2.4.1 د انفرادي لړۍ یا نه‌ګروپ شویو معلوماتو لپاره د مود محاسبه')
add(s,'t241','Only inspection method is used in this case.','اس صورت میں صرف معائنے کا طریقہ استعمال ہوتا ہے۔','پدې حالت کې یوازې د معاینې طریقه کارول کېږي.')
EX=[('21','The following data give the speeds (in miles per hour) of eight cars that were stopped by police for speeding violation 77, 82, 74, 81, 79, 84, 74 and 78. Find the Mode.','درج ذیل اعداد و شمار آٹھ گاڑیوں کی رفتار (میل فی گھنٹہ میں) دیتے ہیں جنہیں پولیس نے رفتار کی خلاف ورزی پر روکا: 77, 82, 74, 81, 79, 84, 74 اور 78۔ عادہ معلوم کریں۔','لاندې معلومات د اتو موټرو چټکتیا (په مایل په ساعت کې) ورکوي چې پولیسو د چټکتیا د سرغړونې له امله ودرولې: 77, 82, 74, 81, 79, 84, 74 او 78. مود ومومئ.','As 74 occurs twice and remaining values occur only once, so mode = 74 miles per hour.','چونکہ 74 دو بار آتا ہے اور باقی قدریں صرف ایک بار آتی ہیں اس لیے عادہ = 74 میل فی گھنٹہ۔','ځکه چې 74 دوه ځله راځي او پاتې ارزښتونه یوازې یو ځل راځي نو مود = 74 مایل په ساعت.'),
('22','Times spent (in minutes) from home to work place by 12 employees of a small company are: 18, 28, 23, 36, 12, 23, 47, 32, 8, 12, 26, and 31. Find mode for the data.','ایک چھوٹی کمپنی کے 12 ملازمین کے گھر سے کام کی جگہ تک صرف کیے گئے اوقات (منٹوں میں) یہ ہیں: 18, 28, 23, 36, 12, 23, 47, 32, 8, 12, 26 اور 31۔ اعداد و شمار کا عادہ معلوم کریں۔','د یوې کوچنۍ شرکت د 12 کارکوونکو له کور څخه د کار ځای ته تېر شوي وختونه (په دقیقو) دا دي: 18, 28, 23, 36, 12, 23, 47, 32, 8, 12, 26 او 31. د معلوماتو مود ومومئ.','As each of the values 12 and 23 occur twice. Therefore, this data set has two modes, which are 12 and 23 minutes.','چونکہ قدریں 12 اور 23 ہر ایک دو بار آتی ہے۔ لہٰذا اس مجموعے کے دو عادہ ہیں جو 12 اور 23 منٹ ہیں۔','ځکه چې ارزښتونه 12 او 23 هر یو دوه ځله راځي. نو دې ټولګه دوه مودونه لري چې 12 او 23 دقیقې دي.'),
('23','Ten randomly selected degree class students have the ages 27, 19, 22, 21, 29, 19, 25, 21, 30 and 22. Find the Mode.','ڈگری جماعت کے دس بے ترتیب منتخب طلبہ کی عمریں 27, 19, 22, 21, 29, 19, 25, 21, 30 اور 22 ہیں۔ عادہ معلوم کریں۔','د ډګري ټولګي د لسو تصادفي ټاکل شویو زده کوونکو عمرونه 27, 19, 22, 21, 29, 19, 25, 21, 30 او 22 دي. مود ومومئ.','Here 19 occurs twice, 21 occurs twice, 22 occurs twice. So this data set has three modes: 19, 21, and 22.','یہاں 19 دو بار آتا ہے، 21 دو بار آتا ہے، 22 دو بار آتا ہے۔ اس لیے اس مجموعے کے تین عادہ ہیں: 19، 21 اور 22۔','دلته 19 دوه ځله راځي، 21 دوه ځله راځي، 22 دوه ځله راځي. نو دې ټولګه درې مودونه لري: 19، 21 او 22.'),
('24','The blood groups of five students in a statistics class are A⁺, O⁺, AB⁺, O⁺ and A⁻. Find Mode.','احصاء کی جماعت کے پانچ طلبہ کے خون کے گروپ A⁺, O⁺, AB⁺, O⁺ اور A⁻ ہیں۔ عادہ معلوم کریں۔','د احصایې د ټولګي د پنځو زده کوونکو د وینې ډلې A⁺, O⁺, AB⁺, O⁺ او A⁻ دي. مود ومومئ.','As we see that O⁺ occurs most frequently than the other categories of blood group, it is mode for this data set.','جیسا کہ ہم دیکھتے ہیں O⁺ خون کے گروپ کی دوسری اقسام سے زیادہ بار آتا ہے، یہ اس مجموعے کا عادہ ہے۔','لکه څنګه چې موږ ګورو O⁺ د وینې ډلې له نورو کټګوریو څخه ډېر ځله راځي، دا د دې ټولګې مود دی.')]
for n,q,qu,qp,a,au,ap in EX:
    head(s,f'ex{n}',f'Example: 2.{n}',f'مثال: 2.{n}',f'بېلګه: 2.{n}',exampleId=f'stat11-ex-2-{n}')
    add(s,f'q{n}',q,qu,qp,role='question',exampleId=f'stat11-ex-2-{n}')
    head(s,f's{n}','Solution:','حل:','حل:',exampleId=f'stat11-ex-2-{n}')
    add(s,f'a{n}',a,au,ap,role='solution',exampleId=f'stat11-ex-2-{n}')
F=Flow(s);F.done()
s['sourceNote']='Printed page 75. The first lines complete the paragraph begun on the previous page. Printed spacing "violation77,82,74…" and "and78" is normalised; "o⁺" (lowercase o) in the Example 2.24 solution is read as O⁺. A thumb is visible at the top-right of the scan; ignored. Header graphics and watermark excluded.'
s['vocabulary']={'bimodal':dict(ur='دو منوالی',ps='دوه‌مودي'),'multimodal':dict(ur='کثیر منوالی',ps='ډېر‌مودي')}
save(s)
# ---------- scan 84 (printed 76) ----------
s=page(84,U,'76','Example 2.25 · 2.4.2 Mode for discrete series · Example 2.26 · 2.4.3 Mode for continuous series · Example 2.27','مثال 2.25 · 2.4.2 منفصل سلسلے کا عادہ · مثال 2.26 · 2.4.3 مسلسل سلسلے کا عادہ · مثال 2.27','بېلګه 2.25 · 2.4.2 د منفصلې لړۍ مود · بېلګه 2.26 · 2.4.3 د دوامدارې لړۍ مود · بېلګه 2.27','mode-discrete-continuous')
F=Flow(s)
head(s,'ex25','Example: 2.25','مثال: 2.25','بېلګه: 2.25',exampleId='stat11-ex-2-25')
add(s,'q25','Marks obtained by five randomly selected students in a statistics class test are 60, 10, 90, 40 and 30. Find Mode.','احصاء کی جماعتی ٹیسٹ میں پانچ بے ترتیب منتخب طلبہ کے حاصل کردہ نمبر 60, 10, 90, 40 اور 30 ہیں۔ عادہ معلوم کریں۔','د احصایې د ټولګي په ازموینه کې د پنځو تصادفي ټاکل شویو زده کوونکو ترلاسه شوې نمرې 60, 10, 90, 40 او 30 دي. مود ومومئ.',role='question',exampleId='stat11-ex-2-25')
head(s,'s25','Solution:','حل:','حل:',exampleId='stat11-ex-2-25')
add(s,'a25','This data has no mode because each value occurs only once. In such cases average value is obtain through other measures of central tendency.','اس مجموعے کا کوئی عادہ نہیں کیونکہ ہر قدر صرف ایک بار آتی ہے۔ ایسی صورتوں میں اوسط قدر مرکزی رجحان کے دوسرے پیمانوں سے حاصل کی جاتی ہے۔','دې ټولګې مود نه لري ځکه چې هر ارزښت یوازې یو ځل راځي. په داسې حالتونو کې اوسط ارزښت د مرکزي تمایل د نورو اندازو په واسطه ترلاسه کېږي.',role='solution',exampleId='stat11-ex-2-25')
head(s,'h242','2.4.2 Calculation of mode for discrete series or grouped data','2.4.2 منفصل سلسلے یا گروہی اعداد و شمار کے لیے عادہ کا حساب','2.4.2 د منفصلې لړۍ یا ګروپي معلوماتو لپاره د مود محاسبه')
add(s,'t242','Two methods are used in this case;','اس صورت میں دو طریقے استعمال ہوتے ہیں؛','پدې حالت کې دوه طریقې کارول کېږي؛')
add(s,'t242a','(i) Inspection method and','(i) معائنے کا طریقہ اور','(i) د معاینې طریقه او')
add(s,'t242b','(ii) Grouping method.','(ii) گروہ بندی کا طریقہ۔','(ii) د ډله‌بندۍ طریقه.')
head(s,'ex26','Example: 2.26','مثال: 2.26','بېلګه: 2.26',exampleId='stat11-ex-2-26')
add(s,'q26','Calculate mode for the following discrete frequency distribution.','درج ذیل منفصل تعدد تقسیم کے لیے عادہ حساب کریں۔','د لاندې منفصل فریکونسي ویش لپاره مود محاسبه کړئ.',role='question',exampleId='stat11-ex-2-26')
head(s,'s26','Solution:','حل:','حل:',exampleId='stat11-ex-2-26')
add(s,'a26','By looking at the data, the value of the variable 18 has maximum frequency, so Mode = 18.','اعداد و شمار کو دیکھنے سے معلوم ہوتا ہے کہ متغیر کی قدر 18 کا تعدد سب سے زیادہ ہے، اس لیے عادہ = 18۔','معلومات کتلو سره معلومېږي چې د متغیر ارزښت 18 اعظمي فریکونسي لري، نو مود = 18.',role='solution',exampleId='stat11-ex-2-26')
head(s,'h243','2.4.3 Calculating the mode for continuous series or grouped data','2.4.3 مسلسل سلسلے یا گروہی اعداد و شمار کے لیے عادہ کا حساب','2.4.3 د دوامدارې لړۍ یا ګروپي معلوماتو لپاره د مود محاسبه')
add(s,'i','(i) By Formula:','(i) فارمولے سے:','(i) په فورمول:')
add(s,'wh','Where,','جہاں،','چېرته چې،')
for k,a,b,d in [('w1','l₁: lower limit of the model class chosen by inspection method.','l₁: معائنے کے طریقے سے منتخب کردہ عادی جماعت کی زیریں حد۔','l₁: د معاینې طریقې په واسطه ټاکل شوي مودي ټولګي ښکتنی حد.'),('w2','fₘ: frequency of the modal class.','fₘ: عادی جماعت کا تعدد۔','fₘ: د مودي ټولګي فریکونسي.'),('w3','f₀: frequency of the preceding class.','f₀: ماقبل جماعت کا تعدد۔','f₀: د مخکیني ټولګي فریکونسي.'),('w4','f₁: frequency of the following class.','f₁: بعد والی جماعت کا تعدد۔','f₁: د راتلونکي ټولګي فریکونسي.'),('w5','h: class interval of the modal class','h: عادی جماعت کا جماعتی وقفہ','h: د مودي ټولګي د ټولګي وقفه')]: add(s,k,a,b,d,listGroup='where')
add(s,'ii','(ii) By Graph:','(ii) گراف سے:','(ii) په ګراف:')
head(s,'ex27','Example: 2.27','مثال: 2.27','بېلګه: 2.27',exampleId='stat11-ex-2-27')
add(s,'q27','Calculate Mode for the following data:','درج ذیل اعداد و شمار کے لیے عادہ حساب کریں:','د لاندې معلوماتو لپاره مود محاسبه کړئ:',role='question',exampleId='stat11-ex-2-27')
s['tables']=[table('Example 2.26: x and f','مثال 2.26: x اور f','بېلګه 2.26: x او f',[c('x:')]+[c(str(v)) for v in [12,14,16,18,20,22]],[[c('f:')]+[c(str(v)) for v in [1,4,6,10,7,2]]],exampleId='stat11-ex-2-26'),
 table('Example 2.27: marks and frequency','مثال 2.27: نمبر اور تعدد','بېلګه 2.27: نمرې او فریکونسي',[c('Marks:','نمبر:','نمرې:')]+[c(v) for v in ['10 – 24','25 – 39','40 – 54','55 – 69','70 – 84','85 – 99']],[[c('Frequency:','تعدد:','فریکونسي:')]+[c(str(v)) for v in [6,20,44,26,3,1]]],exampleId='stat11-ex-2-27')]
s['equations']=[eqn(84,'mf',r'\text{Mode}=l_1+\dfrac{f_m-f_0}{2f_m-f_0-f_1}\times h','Mode = l1 + ((fm − f0)/(2fm − f0 − f1)) × h')]
F.rest()
s['flow']=[dict(type='paragraphs',ids=[pid(84,k) for k in ('ex25','q25','s25','a25','h242','t242','t242a','t242b','ex26','q26')]),dict(type='table',index=0),dict(type='paragraphs',ids=[pid(84,k) for k in ('s26','a26','h243','i')]),dict(type='equation',index=0),dict(type='paragraphs',ids=[pid(84,k) for k in ('wh','w1','w2','w3','w4','w5','ii','ex27','q27')]),dict(type='table',index=1)]
s['sourceNote']='Printed page 76. The word "model class" in the definition of l₁ is printed so (for "modal class") and is retained. A thumb is visible at the top-left of the scan; ignored. Header graphics and watermark excluded.'
s['vocabulary']={'modal class':dict(ur='عادی جماعت',ps='مودي ټولګی')}
save(s)
# ---------- scan 85 (printed 77) ----------
s=page(85,U,'77','Example 2.27 solution · 2.4.4 Graphical method · Example 2.28','مثال 2.27 کا حل · 2.4.4 گرافی طریقہ · مثال 2.28','د بېلګې 2.27 حل · 2.4.4 ګرافي طریقه · بېلګه 2.28','mode-solution')
F=Flow(s)
head(s,'sol27','Solution:','حل:','حل:',exampleId='stat11-ex-2-27')
s['tables']=[table('Example 2.27: class boundaries','مثال 2.27: جماعتی سرحدیں','بېلګه 2.27: د ټولګي پولې',[c('Marks','نمبر','نمرې'),c('f'),c('Class boundaries','جماعتی سرحدیں','د ټولګي پولې')],[[c(a),c(b),c(d)] for a,b,d in [('10 – 24','6','9.5 – 24.5'),('25 – 39','20','24.5 – 39.5'),('40 – 54','44','39.5 – 54.5'),('55 – 69','26','54.5 – 69.5'),('70 – 84','3','69.5 – 84.5'),('85 – 99','1','84.5 – 99.5')]],exampleId='stat11-ex-2-27',role='solution'),
 table('Example 2.28: groups and frequency','مثال 2.28: گروہ اور تعدد','بېلګه 2.28: ډلې او فریکونسي',[c('Groups:','گروہ:','ډلې:')]+[c(v) for v in ['10 – 19','20 – 29','30 – 39','40 – 49','50 – 59']],[[c('Frequency:','تعدد:','فریکونسي:')]+[c(str(v)) for v in [5,10,20,15,3]]],exampleId='stat11-ex-2-28')]
F.rest();F.tb(0)
add(s,'ins','By inspection method we choose 39.5 – 54.5 as the modal class because it has the maximum frequency, therefore','معائنے کے طریقے سے ہم 39.5 – 54.5 کو عادی جماعت منتخب کرتے ہیں کیونکہ اس کا تعدد سب سے زیادہ ہے، لہٰذا','د معاینې طریقې په واسطه موږ 39.5 – 54.5 د مودي ټولګي په توګه ټاکو ځکه چې فریکونسي یې اعظمي ده، نو',role='solution',exampleId='stat11-ex-2-27')
F.rest()
F.e('m1',r'\text{Mode}=l_1+\dfrac{f_m-f_0}{2f_m-f_0-f_1}\times h','Mode = l1 + ((fm − f0)/(2fm − f0 − f1)) × h',exampleId='stat11-ex-2-27')
F.e('m2',r'=39.5+\dfrac{44-20}{2(44)-20-26}\times15','= 39.5 + ((44 − 20)/(2(44) − 20 − 26)) × 15',exampleId='stat11-ex-2-27')
F.e('m3',r'=39.5+\dfrac{24\times15}{88-46}','= 39.5 + (24 × 15)/(88 − 46)',exampleId='stat11-ex-2-27')
F.e('m4',r'=39.5+8.5=48','= 39.5 + 8.5 = 48',exampleId='stat11-ex-2-27')
head(s,'h244','2.4.4 Calculation of the mode by graphical method','2.4.4 گرافی طریقے سے عادہ کا حساب','2.4.4 د مود د ګرافي طریقې محاسبه')
add(s,'t244','Prepare a histogram, consider a bar having maximum height and join its top corners with the nearest corners of the adjoining bars by straight line. The point of intersection of the joining line is the mode.','ہسٹوگرام تیار کریں، زیادہ سے زیادہ اونچائی والے بار کو لیں اور اس کے اوپری کونوں کو ملحقہ باروں کے قریب ترین کونوں سے سیدھی لکیر سے ملائیں۔ ملانے والی لکیروں کے تقاطع کا نقطہ عادہ ہے۔','هیسټوګرام جوړ کړئ، هغه بار واخلئ چې اعظمي لوړوالی ولري او د هغه پورتني کونجونه د نښتو بارونو له نږدې کونجونو سره په سیده کرښه وصل کړئ. د وصلونکو کرښو د تقاطع نقطه مود ده.')
head(s,'ex28','Example: 2.28','مثال: 2.28','بېلګه: 2.28',exampleId='stat11-ex-2-28')
add(s,'q28','Calculate Mode graphically from the following data.','درج ذیل اعداد و شمار سے عادہ گرافی طور پر حساب کریں۔','له لاندې معلوماتو څخه مود په ګرافي ډول محاسبه کړئ.',role='question',exampleId='stat11-ex-2-28')
F.rest();F.tb(1)
F.done()
s['flow']=[b for b in s['flow']]
# reorder: heading/paragraphs must come after equations; rebuild flow explicitly
s['flow']=[dict(type='paragraphs',ids=[pid(85,'sol27')]),dict(type='table',index=0),dict(type='paragraphs',ids=[pid(85,'ins')]),dict(type='equation',index=0),dict(type='equation',index=1),dict(type='equation',index=2),dict(type='equation',index=3),dict(type='paragraphs',ids=[pid(85,k) for k in ('h244','t244','ex28','q28')]),dict(type='table',index=1)]
s['sourceNote']='Printed page 77. The page-number badge at the foot is partly cut off. Printed expression "2(44)−20−26" and "88−46" are as printed. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 86 (printed 78) ----------
s=page(86,U,'78','Example 2.28 solution graph · 2.4.5 Merits and demerits of mode · 2.4.6 Selection among mean, median and mode','مثال 2.28 کا گراف · 2.4.5 عادہ کی خوبیاں اور خامیاں · 2.4.6 اوسط، وسطانیہ اور عادہ میں انتخاب','د بېلګې 2.28 ګراف · 2.4.5 د مود ګټې او زیانونه · 2.4.6 د اوسط، میانې او مود ترمنځ ټاکنه','mode-graph-merits')
F=Flow(s)
head(s,'sol28','Solution:','حل:','حل:',exampleId='stat11-ex-2-28')
add(s,'m','Mode = 37.5 (approximately)','عادہ = 37.5 (تقریباً)','مود = 37.5 (نږدې)',role='solution',exampleId='stat11-ex-2-28')
head(s,'h245','2.4.5 Merits and demerits of mode','2.4.5 عادہ کی خوبیاں اور خامیاں','2.4.5 د مود ګټې او زیانونه')
add(s,'mh','Merits:','خوبیاں:','ګټې:')
for k,a,b,d in [('m1','(i) It can be determined both for quantitative and qualitative data.','(i) اسے مقداری اور کیفی دونوں اعداد و شمار کے لیے معلوم کیا جا سکتا ہے۔','(i) دا د کمیتي او کیفي دواړو معلوماتو لپاره ټاکل کېدای شي.'),('m2','(ii) It is a value which actually exists within the given data set.','(ii) یہ ایسی قدر ہے جو دیے گئے اعداد و شمار کے مجموعے میں حقیقتاً موجود ہوتی ہے۔','(ii) دا داسې ارزښت دی چې په ورکړل شویو معلوماتو ټولګه کې په حقیقت کې شتون لري.'),('m3','(iii) It can be found out by inspection.','(iii) یہ معائنے سے معلوم کیا جا سکتا ہے۔','(iii) دا د معاینې په واسطه موندل کېدای شي.'),('m4','(iv) It is not affected by extreme values.','(iv) یہ انتہائی قدروں سے متاثر نہیں ہوتا۔','(iv) دا د سختو ارزښتونو لخوا نه اغېزمنېږي.')]: add(s,k,a,b,d,listGroup='merits')
add(s,'dh','Demerits:','خامیاں:','زیانونه:')
for k,a,b,d in [('d1','(i) It does not consider all values of the data.','(i) یہ اعداد و شمار کی تمام قدروں کو مدنظر نہیں رکھتا۔','(i) دا د معلوماتو ټول ارزښتونه په پام کې نه نیسي.'),('d2','(ii) Sometimes a distribution may have no mode or may have more than one mode.','(ii) بعض اوقات کسی تقسیم کا کوئی عادہ نہیں ہو سکتا یا ایک سے زیادہ عادہ ہو سکتے ہیں۔','(ii) ځینې وختونه یو ویش کېدای شي مود ونه لري یا له یو څخه ډېر مودونه ولري.')]: add(s,k,a,b,d,listGroup='demerits')
head(s,'h246','2.4.6 Selection among mean, median and mode','2.4.6 اوسط، وسطانیہ اور عادہ میں انتخاب','2.4.6 د اوسط، میانې او مود ترمنځ ټاکنه')
add(s,'t246','The selection of an appropriate measure among these three for a specific variable depends on the scale of measurement as shown in the following table;','کسی خاص متغیر کے لیے ان تینوں میں سے مناسب پیمانے کا انتخاب پیمائش کے پیمانے پر منحصر ہوتا ہے جیسا کہ درج ذیل جدول میں دکھایا گیا ہے؛','د یوه ځانګړي متغیر لپاره د دې دریو څخه د مناسبې اندازې ټاکنه د اندازې په پیمانه پورې اړه لري لکه څنګه چې په لاندې جدول کې ښودل شوې؛',sourceGap=dict(note='The table follows at the top of the next page.'))
s['figures']=[dict(id='stat11-s086-fig1',svg=modehist(),caption='Graphical method of evaluate Mode',captionUrdu='عادہ معلوم کرنے کا گرافی طریقہ',captionPashto='د مود د ارزونې ګرافي طریقه',labels=[lab('Frequency','تعدد','فریکونسي'),lab('Class boundaries','جماعتی سرحدیں','د ټولګي پولې')],sourceGap=dict(note='Redrawn as coded SVG from the Example 2.28 frequencies; the crossing point of the two joining lines is drawn from the printed construction and the printed answer reads Mode = 37.5 (approximately).'))]
F.rest()
s['flow']=[dict(type='paragraphs',ids=[pid(86,'sol28')]),dict(type='figure',index=0),dict(type='paragraphs',ids=[pid(86,k) for k in ('m','h245','mh','m1','m2','m3','m4','dh','d1','d2','h246','t246')])]
s['sourceNote']='Printed page 78. Handwritten Urdu words next to "Merits" and "Demerits" headings are ignored. A ghost of the page-number bar shows at the foot. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
