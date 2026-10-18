from statlib import *
from statcharts import _axes
c=cell
U='central-tendency'
def pid(n,k): return f'stat11-s{n:03}-{k}'
def L(s,items,group):
    for k,a,b,d in items: add(s,k,a,b,d,listGroup=group)
def ogive_graph():
    W,H=560,330;Lm,R,Tp,B=60,30,30,60
    o,Y,pw,ph=_axes(W,H,Lm,R,Tp,B,0,70,[0,10,20,30,40,50,60,70],True)
    xs=[4.5,9.5,14.5,19.5,24.5,29.5,34.5];ys=[0,6,16,32,44,52,60]
    X=lambda v:Lm+pw*(v-3.5)/(35.5-3.5)
    for v in xs: o+=f'<line x1="{X(v):.1f}" y1="{Tp}" x2="{X(v):.1f}" y2="{Tp+ph}" stroke="#bbb"/>'+T(X(v),Tp+ph+16,str(v),11)
    o+='<polyline fill="none" stroke="#1c7ab8" stroke-width="2.2" points="'+' '.join(f'{X(a):.1f},{Y(b):.1f}' for a,b in zip(xs,ys))+'"/>'
    for a,b in zip(xs,ys): o+=f'<circle cx="{X(a):.1f}" cy="{Y(b):.1f}" r="3" fill="#1c7ab8"/>'
    mx=14.5+5*(30-16)/16
    o+=f'<line x1="{Lm}" y1="{Y(30):.1f}" x2="{X(mx):.1f}" y2="{Y(30):.1f}" stroke="#111" stroke-width="3"/><line x1="{X(mx):.1f}" y1="{Y(30):.1f}" x2="{X(mx):.1f}" y2="{Tp+ph+4}" stroke="#111" stroke-width="3"/>'
    o+=T(Lm+pw/2,H-8,'Class boundaries',12)+f'<text transform="translate(14 {Tp+ph/2}) rotate(-90)" font-size="11" text-anchor="middle" font-family="Arial">Cumulative frequency</text>'
    return svg(W,H,'Cumulative frequency curve through class boundaries 4.5 to 34.5 with a horizontal line at 30 meeting the curve and a vertical line dropping to about 19 on the x-axis',o)
def sym():
    o='<path d="M30,115 C70,112 100,55 160,22 C220,55 250,112 290,115" fill="none" stroke="#1c6aa8" stroke-width="2"/><line x1="160" y1="22" x2="160" y2="117" stroke="#1c6aa8" stroke-width="2"/><line x1="20" y1="117" x2="320" y2="117" stroke="#222" stroke-width="1.5"/>'+T(10,121,'X',13)
    for x,t in [(110,'Q₁'),(160,'Md'),(215,'Q₃')]: o+=f'<line x1="{x}" y1="113" x2="{x}" y2="121" stroke="#222"/>'+T(x,136,t,12)
    return svg(340,150,'Symmetrical curve with the first quartile, median and third quartile marked on the x-axis',o)
def nl(pts,labs,aria,arrow=False):
    W=60+len(pts)*70
    o=f'<line x1="20" y1="25" x2="{W-10}" y2="25" stroke="#222" stroke-width="2"/>'+T(10,29,'X',12)
    if arrow:o+=f'<path d="M{W-18},20 L{W-8},25 L{W-18},30" fill="none" stroke="#222" stroke-width="2"/>'
    for i,(x,t) in enumerate(zip(pts,labs)): o+=f'<line x1="{x}" y1="20" x2="{x}" y2="30" stroke="#222" stroke-width="1.5"/>'+T(x,48,t,12)
    return svg(W,60,aria,o)
Q=nl([60,130,200],['Q₁','Q₂','Q₃'],'Number line with quartiles Q1, Q2 and Q3 dividing the data into four equal parts')
D=nl([60+i*68 for i in range(9)],[f'D{i}' for i in range(1,10)],'Number line with deciles D1 to D9 dividing the data into ten equal parts',arrow=True)
# ---------- scan 75 (printed 67) ----------
s=page(75,U,'67','2.3.3 Median for continuous series · Example 2.15','2.3.3 مسلسل سلسلے کے لیے وسطانیہ · مثال 2.15','2.3.3 د دوامدارې لړۍ لپاره میانه · بېلګه 2.15','median-continuous')
F=Flow(s)
head(s,'h233','2.3.3 Computation of median in case of continuous series or grouped data','2.3.3 مسلسل سلسلے یا گروہی اعداد و شمار کی صورت میں وسطانیہ کا حساب','2.3.3 د دوامدارې لړۍ یا ګروپي معلوماتو په حالت کې د میانې محاسبه')
add(s,'si','Step-i: Arrange the classes along with frequencies if needed.','مرحلہ-i: ضرورت ہو تو جماعتوں کو تعددات کے ساتھ ترتیب دیں۔','ګام-i: که اړتیا وي ټولګي له فریکونسیو سره ترتیب کړئ.')
add(s,'sii','Step-ii: Compute class boundaries and cumulative frequencies.','مرحلہ-ii: جماعتی سرحدیں اور جمعی تعددات حساب کریں۔','ګام-ii: د ټولګي پولې او مجموعي فریکونسۍ محاسبه کړئ.')
add(s,'siii','Step-iii: Use formula of discrete case to locate the median class.','مرحلہ-iii: وسطانیہ جماعت معلوم کرنے کے لیے منفصل صورت کا فارمولا استعمال کریں۔','ګام-iii: د میانې ټولګی موندلو لپاره د منفصل حالت فورمول وکاروئ.')
add(s,'siv','Step-iv: Calculate the median by formula,','مرحلہ-iv: فارمولے سے وسطانیہ حساب کریں،','ګام-iv: میانه د فورمول په واسطه محاسبه کړئ،')
F.rest()
F.e('f',r'\text{Median}=l_1+\dfrac{h}{f}\left(\dfrac{\sum f}{2}-c\right).','Median = l1 + (h/f)(Σf/2 − c).')
add(s,'wh','Where','جہاں','چېرته چې')
L(s,[('w1','l₁: lower limit of the class boundaries in which median lies.','l₁: جماعتی سرحدوں کی زیریں حد جس میں وسطانیہ واقع ہے۔','l₁: د ټولګي د پولو ښکتنی حد چې په هغه کې میانه پرته ده.'),('w2','h: class interval of the median class.','h: وسطانیہ جماعت کا جماعتی وقفہ۔','h: د میانې ټولګي د ټولګي وقفه.'),('w3','f: median class frequency','f: وسطانیہ جماعت کا تعدد','f: د میانې ټولګي فریکونسي'),('w4','c: cumulative frequency of the preceding class.','c: ماقبل جماعت کا جمعی تعدد۔','c: د مخکیني ټولګي مجموعي فریکونسي.')],'where')
head(s,'ex','Example: 2.15','مثال: 2.15','بېلګه: 2.15',exampleId='stat11-ex-2-15')
add(s,'q','Find out median of the following series:','درج ذیل سلسلے کا وسطانیہ معلوم کریں:','د لاندې لړۍ میانه ومومئ:',role='question',exampleId='stat11-ex-2-15')
head(s,'sol','Solution:','حل:','حل:',exampleId='stat11-ex-2-15')
add(s,'sa','Since n = Σf = 53 is odd, therefore,','چونکہ n = Σf = 53 طاق ہے، لہٰذا،','ځکه چې n = Σf = 53 طاق دی، نو،',role='solution',exampleId='stat11-ex-2-15')
s['tables']=[table('Example 2.15: wages','مثال 2.15: اجرتیں','بېلګه 2.15: مزدورۍ',[c('Wages:','اجرتیں:','مزدورۍ:')]+[c(v) for v in ['20 – 29','30 – 39','40 – 49','50 – 59','60 – 69']],[[c('No. of labour:','مزدوروں کی تعداد:','د کارګرانو شمېر:')]+[c(str(v)) for v in [3,15,20,10,5]]],exampleId='stat11-ex-2-15'),
 table('Example 2.15: class boundaries and c.f','مثال 2.15: جماعتی سرحدیں اور c.f','بېلګه 2.15: د ټولګي پولې او c.f',[c('Wages','اجرتیں','مزدورۍ'),c('f'),c('Class boundaries','جماعتی سرحدیں','د ټولګي پولې'),c('c.f')],[[c(a),c(b),c(d),c(e)] for a,b,d,e in [('20 – 29','3','19.5 – 29.5','3'),('30 – 39','15','29.5 – 39.5','18'),('40 – 49','20','39.5 – 49.5','38'),('50 – 59','10','49.5 – 59.5','48'),('60 – 69','5','59.5 – 69.5','53')]]+[[c('Total','کل','ټول'),c('53'),c('–'),c('–')]],exampleId='stat11-ex-2-15',role='solution')]
ids=[p['id'] for p in s['paras']]
F.rest()
F.done()
s['flow']=[dict(type='paragraphs',ids=[pid(75,k) for k in ('h233','si','sii','siii','siv')]),dict(type='equation',index=0),dict(type='paragraphs',ids=[pid(75,k) for k in ('wh','w1','w2','w3','w4','ex','q')]),dict(type='table',index=0),dict(type='paragraphs',ids=[pid(75,'sol')]),dict(type='table',index=1),dict(type='paragraphs',ids=[pid(75,'sa')])]
s['equations'].append(eqn(75,'m1',r'\text{Median}=\left(\dfrac{\sum f+1}{2}\right)\text{th value}=\left(\dfrac{53+1}{2}\right)\text{th value}=27\text{th value.}','Median = ((Σf + 1)/2)th value = ((53 + 1)/2)th value = 27th value.',exampleId='stat11-ex-2-15'))
add(s,'sb','This implies that median lies in the group (39.5 - 49.5).','اس کا مطلب ہے کہ وسطانیہ گروہ (39.5 - 49.5) میں واقع ہے۔','پدې معنا چې میانه په ډله (39.5 - 49.5) کې پرته ده.',role='solution',exampleId='stat11-ex-2-15')
add(s,'sc','Hence Median = l₁ + (h/f)(Σf/2 − c).','لہٰذا وسطانیہ = l₁ + (h/f)(Σf/2 − c)۔','نو میانه = l₁ + (h/f)(Σf/2 − c).',role='solution',exampleId='stat11-ex-2-15',sourceGap=dict(note='The numerical substitution follows on the next page.'))
s['equations'].append(eqn(75,'m2',r'\text{Hence Median}=l_1+\dfrac{h}{f}\left(\dfrac{\sum f}{2}-c\right).','Hence Median = l1 + (h/f)(Σf/2 − c).',exampleId='stat11-ex-2-15'))
s['paras']=[p for p in s['paras'] if p['id']!=pid(75,'sc')]
s['flow']+=[dict(type='equation',index=1),dict(type='paragraphs',ids=[pid(75,'sb')]),dict(type='equation',index=2)]
s['sourceNote']='Printed page 67. The page-number badge at the foot is partly cut off. The data lines (Wages / No. of labour) are printed as text rows and kept as a one-row table. A white patch at the top-right is a scan artefact. Header graphics and watermark excluded.'
s['vocabulary']={'median class':dict(ur='وسطانیہ جماعت',ps='د میانې ټولګی')}
save(s)
# ---------- scan 76 (printed 68) ----------
s=page(76,U,'68','Example 2.15 (end) · 2.3.4 Graphic method for the median · Example 2.16','مثال 2.15 (اختتام) · 2.3.4 وسطانیہ کا گرافی طریقہ · مثال 2.16','بېلګه 2.15 (پای) · 2.3.4 د میانې ګرافي طریقه · بېلګه 2.16','median-graphic-1')
F=Flow(s)
F.e('c',r'=39.5+\dfrac{10}{20}\left(\dfrac{53}{2}-18\right)=39.5+4.25=43.75','= 39.5 + (10/20)(53/2 − 18) = 39.5 + 4.25 = 43.75',exampleId='stat11-ex-2-15')
head(s,'h234','2.3.4 Graphic method to estimate the median','2.3.4 وسطانیہ کا تخمینہ لگانے کا گرافی طریقہ','2.3.4 د میانې د اټکل ګرافي طریقه')
add(s,'t','Median can also be computed with the help of a graph.','وسطانیہ گراف کی مدد سے بھی حساب کیا جا سکتا ہے۔','میانه د ګراف په مرسته هم محاسبه کېدای شي.')
add(s,'si','Step-i: Compute class boundaries and cumulative frequencies.','مرحلہ-i: جماعتی سرحدیں اور جمعی تعددات حساب کریں۔','ګام-i: د ټولګي پولې او مجموعي فریکونسۍ محاسبه کړئ.')
add(s,'sii','Step-ii: Take a graph paper and draw cumulative frequency curve.','مرحلہ-ii: گراف پیپر لیں اور جمعی تعدد منحنی بنائیں۔','ګام-ii: ګراف کاغذ واخلئ او مجموعي فریکونسي منحني رسم کړئ.')
add(s,'siii','Step-iii: Compute Median =','مرحلہ-iii: وسطانیہ حساب کریں =','ګام-iii: میانه محاسبه کړئ =')
F.rest()
F.e('e1',r'\text{Median}=\left(\dfrac{\sum f}{2}\right)\text{th value if }\sum f\text{ is even}','Median = (Σf/2)th value if Σf is even')
F.e('e2',r'\text{or Median}=\left(\dfrac{\sum f+1}{2}\right)\text{th value if }\sum f\text{ is odd to find the median class.}','or Median = ((Σf + 1)/2)th value if Σf is odd to find the median class.')
add(s,'siv','Step-iv: Locate median on y-axis and draw a horizontal/parallel line to cut the cumulative frequency curve and from this point draw a perpendicular line which cuts the x-axis at a certain point. The value of this point on x-axis is the median.','مرحلہ-iv: y-محور پر وسطانیہ کو تلاش کریں اور جمعی تعدد منحنی کو کاٹنے کے لیے ایک افقی/متوازی لکیر کھینچیں اور اس نقطے سے ایک عمود کھینچیں جو x-محور کو کسی نقطے پر کاٹے۔ x-محور پر اس نقطے کی قدر وسطانیہ ہے۔','ګام-iv: په y-محور میانه ومومئ او د مجموعي فریکونسي منحني پرې کولو لپاره یوه افقي/موازي کرښه رسم کړئ او له دې نقطې څخه یوه عمود کرښه رسم کړئ چې x-محور په یوه نقطه پرې کړي. په x-محور د دې نقطې ارزښت میانه ده.')
head(s,'ex','Example: 2.16','مثال: 2.16','بېلګه: 2.16',exampleId='stat11-ex-2-16')
add(s,'q','Calculate median by graphic method from the data given below:','نیچے دیے گئے اعداد و شمار سے وسطانیہ گرافی طریقے سے حساب کریں:','د لاندې ورکړل شویو معلوماتو څخه میانه د ګرافي طریقې په واسطه محاسبه کړئ:',role='question',exampleId='stat11-ex-2-16')
head(s,'sol','Solution:','حل:','حل:',exampleId='stat11-ex-2-16')
s['tables']=[table('Example 2.16: marks and frequency','مثال 2.16: نمبر اور تعدد','بېلګه 2.16: نمرې او فریکونسي',[c('Marks:','نمبر:','نمرې:')]+[c(v) for v in ['5 – 9','10 – 14','15 – 19','20 – 24','25 – 29','30 – 34']],[[c('Frequency:','تعدد:','فریکونسي:')]+[c(str(v)) for v in [6,10,16,12,8,8]]],exampleId='stat11-ex-2-16'),
 table('Example 2.16: class boundaries and c.f','مثال 2.16: جماعتی سرحدیں اور c.f','بېلګه 2.16: د ټولګي پولې او c.f',[c('Marks','نمبر','نمرې'),c('f'),c('Class boundaries','جماعتی سرحدیں','د ټولګي پولې'),c('c.f')],[[c(a),c(b),c(d),c(e)] for a,b,d,e in [('5 – 9','6','4.5 – 9.5','6'),('10 – 14','10','9.5 – 14.5','16'),('15 – 19','16','14.5 – 19.5','32'),('20 – 24','12','19.5 – 24.5','44'),('25 – 29','8','24.5 – 29.5','52'),('30 – 34','8','29.5 – 34.5','60')]]+[[c('Total','کل','ټول'),c('60'),c('–'),c('–')]],exampleId='stat11-ex-2-16',role='solution')]
s['equations'].append(eqn(76,'n1',r'\text{Since }\sum f=60\text{ is even, Therefore, Median}=\left(\dfrac{\sum f}{2}\right)\text{th value}=\left(\dfrac{60}{2}\right)\text{th value}=30\text{th value.}','Since Σf = 60 is even, Therefore, Median = (Σf/2)th value = (60/2)th value = 30th value.',exampleId='stat11-ex-2-16'))
add(s,'z','This implies that median lies in the group (14.5 – 19.5).','اس کا مطلب ہے کہ وسطانیہ گروہ (14.5 – 19.5) میں واقع ہے۔','پدې معنا چې میانه په ډله (14.5 – 19.5) کې پرته ده.',role='solution',exampleId='stat11-ex-2-16')
ids=[p['id'] for p in s['paras']]
F.rest()
s['flow']=[dict(type='equation',index=0),dict(type='paragraphs',ids=[pid(76,k) for k in ('h234','t','si','sii','siii')]),dict(type='equation',index=1),dict(type='equation',index=2),dict(type='paragraphs',ids=[pid(76,k) for k in ('siv','ex','q')]),dict(type='table',index=0),dict(type='paragraphs',ids=[pid(76,'sol')]),dict(type='table',index=1),dict(type='equation',index=3),dict(type='paragraphs',ids=[pid(76,'z')])]
s['sourceNote']='Printed page 68. The first line completes Example 2.15. The printed working for Example 2.16 sits to the right of the table and is shown after it. The data rows (Marks / Frequency) are kept as a one-row table. A colour smudge at the top-left is ignored. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 77 (printed 69) ----------
s=page(77,U,'69','Example 2.16 graph · 2.3.5 Properties of median · 2.3.6 Advantages of median','مثال 2.16 کا گراف · 2.3.5 وسطانیہ کی خصوصیات · 2.3.6 وسطانیہ کے فوائد','د بېلګې 2.16 ګراف · 2.3.5 د میانې ځانګړتیاوې · 2.3.6 د میانې ګټې','median-properties')
F=Flow(s)
add(s,'g','We can see from the graph that median = 19 (approximately).','ہم گراف سے دیکھ سکتے ہیں کہ وسطانیہ = 19 (تقریباً)۔','موږ له ګراف څخه لیدلای شو چې میانه = 19 (نږدې).')
head(s,'h235','2.3.5 Properties of median','2.3.5 وسطانیہ کی خصوصیات','2.3.5 د میانې ځانګړتیاوې')
add(s,'p1','(i) The sum of the absolute deviations of the observations from their median is less than the sum from any other value of the series, that is, Σ|x − Median| is minimum.','(i) مشاہدات کے ان کے وسطانیہ سے مطلق انحرافات کا مجموعہ سلسلے کی کسی بھی دوسری قدر سے انحرافات کے مجموعے سے کم ہوتا ہے، یعنی Σ|x − Median| کم از کم ہے۔','(i) د کتنو د هغو له میانې څخه د مطلقو انحرافاتو مجموعه د لړۍ له بل هر ارزښت څخه د انحرافاتو له مجموعې څخه کمه وي، یعنې Σ|x − Median| لږ تر لږه دی.',listGroup='median-props')
add(s,'p2','(ii) If values of a variable are changed by adding a constant c then median of the new series will be Median + c.','(ii) اگر متغیر کی قدریں ایک مستقلہ c جمع کر کے بدلی جائیں تو نئے سلسلے کا وسطانیہ Median + c ہوگا۔','(ii) که د متغیر ارزښتونه د یو ثابت c په جمع کولو بدل شي نو د نوې لړۍ میانه به Median + c وي.',listGroup='median-props')
add(s,'p3','(iii) If values of a variable are changed by multiplying a constant c then median of the new series will be c (Median).','(iii) اگر متغیر کی قدریں ایک مستقلہ c سے ضرب دے کر بدلی جائیں تو نئے سلسلے کا وسطانیہ c (Median) ہوگا۔','(iii) که د متغیر ارزښتونه د یو ثابت c په ضرب کولو بدل شي نو د نوې لړۍ میانه به c (Median) وي.',listGroup='median-props')
add(s,'p4','(iv) For a symmetrical distribution median is equidistant from the first and third quartiles i.e. Median − Q₁ = Q₃ − Median.','(iv) متناسب تقسیم کے لیے وسطانیہ پہلی اور تیسری چوتھائی سے یکساں فاصلے پر ہوتا ہے یعنی Median − Q₁ = Q₃ − Median۔','(iv) د متناسب ویش لپاره میانه له لومړي او دریم څلورمي څخه مساوي واټن کې وي یعنې Median − Q₁ = Q₃ − Median.',listGroup='median-props')
head(s,'h236','2.3.6 Advantages of median','2.3.6 وسطانیہ کے فوائد','2.3.6 د میانې ګټې')
L(s,[('a1','(i) It is not affected by extreme values because it is a positional average.','(i) یہ انتہائی قدروں سے متاثر نہیں ہوتا کیونکہ یہ مقامی اوسط ہے۔','(i) دا د سختو ارزښتونو لخوا نه اغېزمنېږي ځکه چې دا موقعیتي اوسط دی.'),('a2','(ii) It can be located even if the data are incomplete.','(ii) یہ اس وقت بھی معلوم کیا جا سکتا ہے جب اعداد و شمار نامکمل ہوں۔','(ii) دا هغه وخت هم موندل کېدای شي چې معلومات نیمګړي وي.'),('a3','(iii) It can be located even for qualitative data (ordinal scale).','(iii) یہ کیفی اعداد و شمار (ترتیبی پیمانے) کے لیے بھی معلوم کیا جا سکتا ہے۔','(iii) دا د کیفي معلوماتو (ترتیبي پیمانې) لپاره هم موندل کېدای شي.'),('a4','(iv) It is an appropriate average for highly skewed distributions.','(iv) یہ بہت زیادہ کج تقسیمات کے لیے موزوں اوسط ہے۔','(iv) دا د ډېر کوړو ویشونو لپاره مناسب اوسط دی.'),('a5','(v) It can be calculated by inspection in some cases.','(v) یہ بعض صورتوں میں معائنے سے حساب کیا جا سکتا ہے۔','(v) دا په ځینو حالتونو کې د معاینې په واسطه محاسبه کېدای شي.')],'median-adv')
s['figures']=[dict(id='stat11-s077-fig1',svg=ogive_graph(),caption='Cumulative frequency curve (ogive) used to estimate the median of Example 2.16',captionUrdu='مثال 2.16 کے وسطانیہ کے تخمینے کے لیے جمعی تعدد منحنی (اوجائیو)',captionPashto='د بېلګې 2.16 د میانې د اټکل لپاره مجموعي فریکونسي منحني (اوجایو)',labels=[lab('Cumulative frequency','جمعی تعدد','مجموعي فریکونسي'),lab('Class boundaries','جماعتی سرحدیں','د ټولګي پولې')],sourceGap=dict(note='The printed axis numbers are washed out in the scan; the graph is redrawn from the Example 2.16 c.f values (4.5→0, 9.5→6, 14.5→16, 19.5→32, 24.5→44, 29.5→52, 34.5→60).')),
 dict(id='stat11-s077-fig2',svg=sym(),caption='Symmetrical distribution: median Md equidistant from Q₁ and Q₃',captionUrdu='متناسب تقسیم: وسطانیہ Md، Q₁ اور Q₃ سے یکساں فاصلے پر',captionPashto='متناسب ویش: میانه Md له Q₁ او Q₃ څخه مساوي واټن کې',labels=[lab('Md','Md','Md'),lab('Q₁','Q₁','Q₁'),lab('Q₃','Q₃','Q₃')],sourceGap=dict(note='Redrawn as a coded schematic curve.'))]
F.rest()
ids=[p['id'] for p in s['paras']]
s['flow']=[dict(type='figure',index=0),dict(type='paragraphs',ids=[pid(77,'g'),pid(77,'h235'),pid(77,'p1'),pid(77,'p2'),pid(77,'p3')]),dict(type='figure',index=1),dict(type='paragraphs',ids=[pid(77,k) for k in ('p4','h236','a1','a2','a3','a4','a5')])]
s['sourceNote']='Printed page 69. A thumb and a fainter title strip at the top of the scan are artefacts. The axis numbers of the printed graph are washed out. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 78 (printed 70) ----------
s=page(78,U,'70','2.3.7 Disadvantages of median · 2.3.8 Quartiles, deciles and percentiles · 2.3.9 Computation','2.3.7 وسطانیہ کی خامیاں · 2.3.8 چوتھائیاں، دسویں اور فی صدکیات · 2.3.9 حساب','2.3.7 د میانې زیانونه · 2.3.8 څلورمې، لسمې او سلمې · 2.3.9 محاسبه','quantiles-1')
F=Flow(s)
head(s,'h237','2.3.7 Disadvantages of median','2.3.7 وسطانیہ کی خامیاں','2.3.7 د میانې زیانونه')
L(s,[('d1','(i) It is not based on all the observations.','(i) یہ تمام مشاہدات پر مبنی نہیں ہے۔','(i) دا پر ټولو کتنو والړ نه دی.'),('d2','(ii) Computation of median need arrangement of data into an array, which is a difficult job, especially for a large body of data.','(ii) وسطانیہ کے حساب کے لیے اعداد و شمار کو ارے میں ترتیب دینا ضروری ہے، جو ایک مشکل کام ہے، خاص طور پر اعداد و شمار کے بڑے مجموعے کے لیے۔','(ii) د میانې محاسبه د معلوماتو په اره کې د ترتیب کولو ته اړتیا لري، چې یو ستونزمن کار دی، په ځانګړي ډول د معلوماتو د لوی مجموعې لپاره.'),('d3','(iii) In case of even number of observations or continuous series median is an estimated value other than any value in the series.','(iii) مشاہدات کی تعداد جفت ہونے یا مسلسل سلسلے کی صورت میں وسطانیہ ایک تخمینی قدر ہوتی ہے جو سلسلے کی کسی بھی قدر کے علاوہ ہوتی ہے۔','(iii) د کتنو د جفت شمېر یا دوامدارې لړۍ په حالت کې میانه یو اټکل شوی ارزښت وي چې د لړۍ له هر ارزښت پرته وي.'),('d4','(iv) It is not useful measure where extreme values receive greater importance.','(iv) یہ ایسی جگہ مفید پیمانہ نہیں جہاں انتہائی قدروں کو زیادہ اہمیت ملتی ہو۔','(iv) دا هغه ځای ګټوره اندازه نه ده چېرته چې سخت ارزښتونه ډېر اهمیت ترلاسه کوي.')],'median-dis')
head(s,'h238','2.3.8 Quartiles, deciles and percentiles','2.3.8 چوتھائیاں، دسویں اور فی صدکیات','2.3.8 څلورمې، لسمې او سلمې')
add(s,'t1','The values which divide a series of ordered data into four equal parts are called quartiles. They are denoted by Q₁, Q₂ and Q₃. That is;','وہ قدریں جو ترتیب دیے گئے اعداد و شمار کے سلسلے کو چار برابر حصوں میں تقسیم کریں چوتھائیاں (کوارٹائلز) کہلاتی ہیں۔ انہیں Q₁، Q₂ اور Q₃ سے ظاہر کیا جاتا ہے۔ یعنی؛','هغه ارزښتونه چې د ترتیب شویو معلوماتو لړۍ په څلورو مساوي برخو وېشي څلورمې (کوارټایلونه) بلل کېږي. دا په Q₁، Q₂ او Q₃ ښودل کېږي. یعنې؛')
add(s,'t2','The values which divide a series into ten equal parts are called deciles. They are denoted by D₁, D₂, D₃, …, D₉. That is;','وہ قدریں جو سلسلے کو دس برابر حصوں میں تقسیم کریں دسویں (ڈیسائلز) کہلاتی ہیں۔ انہیں D₁، D₂، D₃، …، D₉ سے ظاہر کیا جاتا ہے۔ یعنی؛','هغه ارزښتونه چې لړۍ په لسو مساوي برخو وېشي لسمې (ډیسایلونه) بلل کېږي. دا په D₁، D₂، D₃، …، D₉ ښودل کېږي. یعنې؛')
add(s,'t3','The values which divide a series in to hundred equal parts are called percentiles. They are denoted by P₁, P₂, …, P₉₉. These all are positional averages and are used to know the position of an observation relative to the other values in a data set. Note that (i) Median = Q₂ = D₅ = P₅₀ and (ii) Quartiles, deciles and percentiles are collectively called Quantiles','وہ قدریں جو سلسلے کو سو برابر حصوں میں تقسیم کریں فی صدکیات (پرسنٹائلز) کہلاتی ہیں۔ انہیں P₁، P₂، …، P₉₉ سے ظاہر کیا جاتا ہے۔ یہ سب مقامی اوسط ہیں اور اعداد و شمار کے مجموعے میں دوسری قدروں کے مقابلے میں کسی مشاہدے کی پوزیشن جاننے کے لیے استعمال ہوتے ہیں۔ نوٹ کریں کہ (i) وسطانیہ = Q₂ = D₅ = P₅₀ اور (ii) چوتھائیاں، دسویں اور فی صدکیات مجموعی طور پر کوانٹائلز کہلاتی ہیں','هغه ارزښتونه چې لړۍ په سلو مساوي برخو وېشي سلمې (پرسنټایلونه) بلل کېږي. دا په P₁، P₂، …، P₉₉ ښودل کېږي. دا ټول موقعیتي اوسطونه دي او د معلوماتو په ټولګه کې د نورو ارزښتونو په پرتله د یوې کتنې د موقعیت د پېژندلو لپاره کارول کېږي. یادونه وکړئ چې (i) میانه = Q₂ = D₅ = P₅₀ او (ii) څلورمې، لسمې او سلمې په ګډه کوانټایلونه بلل کېږي')
head(s,'h239','2.3.9 Computation of quartiles, deciles and percentiles','2.3.9 چوتھائیوں، دسویں اور فی صدکیات کا حساب','2.3.9 د څلورمو، لسمو او سلمو محاسبه')
add(s,'ci','Case-i: Individual series or ungrouped data','صورت-i: انفرادی سلسلہ یا غیر گروہی اعداد و شمار','حالت-i: انفرادي لړۍ یا نه‌ګروپ شوي معلومات')
add(s,'cn','If n is odd then add 1 with n in the above formulas.','اگر n طاق ہو تو مندرجہ بالا فارمولوں میں n کے ساتھ 1 جمع کریں۔','که n طاق وي نو په پورتنیو فورمولونو کې له n سره 1 جمع کړئ.')
s['figures']=[dict(id='stat11-s078-fig1',svg=Q,caption='Quartiles Q₁, Q₂, Q₃ on the number line',captionUrdu='عدد خط پر چوتھائیاں Q₁، Q₂، Q₃',captionPashto='په شمېر کرښه څلورمې Q₁، Q₂، Q₃',labels=[],sourceGap=dict(note='Redrawn as a coded number line.')),dict(id='stat11-s078-fig2',svg=D,caption='Deciles D₁ to D₉ on the number line',captionUrdu='عدد خط پر دسویں D₁ تا D₉',captionPashto='په شمېر کرښه لسمې D₁ تر D₉',labels=[],sourceGap=dict(note='Redrawn as a coded number line.'))]
s['equations']=[eqn(78,'q',r'Q_i=i\left(\dfrac{n}{4}\right)\text{th item if }n\text{ is even, }i=1,2,3.','Qi = i(n/4)th item if n is even, i = 1, 2, 3.'),eqn(78,'d',r'D_i=i\left(\dfrac{n}{10}\right)\text{th item if }n\text{ is even, }i=1,2,\ldots,9.','Di = i(n/10)th item if n is even, i = 1, 2, …, 9.'),eqn(78,'p',r'P_i=i\left(\dfrac{n}{100}\right)\text{th item if }n\text{ is even, }i=1,2,\ldots,99.','Pi = i(n/100)th item if n is even, i = 1, 2, …, 99.')]
F.rest()
s['flow']=[dict(type='paragraphs',ids=[pid(78,k) for k in ('h237','d1','d2','d3','d4','h238','t1')]),dict(type='figure',index=0),dict(type='paragraphs',ids=[pid(78,'t2')]),dict(type='figure',index=1),dict(type='paragraphs',ids=[pid(78,'t3'),pid(78,'h239'),pid(78,'ci')]),dict(type='equation',index=0),dict(type='equation',index=1),dict(type='equation',index=2),dict(type='paragraphs',ids=[pid(78,'cn')])]
s['sourceNote']='Printed page 70. Handwritten notes near the 2.3.8 heading ("Median = 2, Q = 4, D = 10, P = 100") are ignored. Printed variant "Q₁." in the quartile list punctuation is read as "Q₁, Q₂ and Q₃". Header graphics and watermark excluded.'
s['vocabulary']={'quartiles':dict(ur='چوتھائیاں (کوارٹائلز)',ps='څلورمې (کوارټایلونه)'),'deciles':dict(ur='دسویں (ڈیسائلز)',ps='لسمې (ډیسایلونه)'),'percentiles':dict(ur='فی صدکیات (پرسنٹائلز)',ps='سلمې (پرسنټایلونه)'),'quantiles':dict(ur='کوانٹائلز',ps='کوانټایلونه')}
save(s)
