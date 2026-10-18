from stathelp import *
c=cell
U='time-series'
E62='stat11-ex-6-2'; E63='stat11-ex-6-3'; E64='stat11-ex-6-4'; E65='stat11-ex-6-5'
def row(a,b,d,vals): return [c(a,b,d)]+[c(str(v)) for v in vals]
def semifig_b():
    W,H=620,330
    px=lambda x:80+(x-1976)*60; py=lambda v:270-v*(220/480.0)
    o='<line x1="60" y1="40" x2="60" y2="270" stroke="#111" stroke-width="1.8"/><line x1="60" y1="270" x2="590" y2="270" stroke="#111" stroke-width="1.8"/>'
    for v in (0,150,300,450): o+=T(52,py(v)+4,str(v),12,'end')
    o+=T(60,28,'y-axis',12,'start')+T(596,274,'x-axis',12,'start')+T(300,34,'Graph showing the semi-average trend',13)
    for yv in range(1976,1985): o+=f'<line x1="{px(yv)}" y1="266" x2="{px(yv)}" y2="274" stroke="#111"/>'+T(px(yv),292,str(yv),12)
    o+=f'<line x1="{px(1976.6)}" y1="{py(262):.1f}" x2="{px(1983.8)}" y2="{py(355):.1f}" stroke="#1c7ab8" stroke-width="1.8"/>'
    for xx,vv in ((1977.5,273),(1982.5,341.5)): o+=f'<circle cx="{px(xx):.1f}" cy="{py(vv):.1f}" r="4" fill="#111"/>'
    return svg(W,H,'Semi-average trend: a straight line through the two semi-average points (1977.5, 273) and (1982.5, 341.5) rising to the right',o)
# ---------- scan 211 (printed 201) ----------
s=page(211,U,'201','Example 6.2 (b) · Advantages and disadvantages of semi-average · (iii) Method of moving average (start)','مثال 6.2 (ب) · نیم اوسط کے فوائد اور نقصانات · (iii) متحرک اوسط کا طریقہ (آغاز)','بېلګه 6.2 (b) · د نیمه اوسط ګټې او زیانونه · (iii) د خوځېدونکي اوسط طریقه (پیل)','ts-semi-2')
Flow(s)
add(s,'a1','(b) Here the number of years is odd so we exclude the middle value in order to divide the series in to two equal parts. Then average of each parts is computed. The averages are plotted on the graph paper to obtain the semi-average trend.','(ب) یہاں سالوں کی تعداد طاق ہے اس لیے ہم سلسلے کو دو برابر حصوں میں تقسیم کرنے کے لیے درمیانی قدر کو خارج کرتے ہیں۔ پھر ہر حصے کا اوسط حساب کیا جاتا ہے۔ نیم اوسط رجحان حاصل کرنے کے لیے اوسطوں کو گراف پیپر پر بنایا جاتا ہے۔','(b) دلته د کلونو شمېر طاق دی نو موږ لړۍ ته په دوو مساوي برخو ویشلو لپاره منځنی ارزښت وباسو. بیا د هرې برخې اوسط محاسبه کېږي. د نیمه اوسط تمایل ترلاسه کولو لپاره اوسطونه په ګراف کاغذ رسمېږي.',role='solution',exampleId=E62)
add(s,'ah','Advantages','فوائد','ګټې')
L(s,[('v1','(i) This method is very simple to apply.','(i) یہ طریقہ لاگو کرنے میں بہت آسان ہے۔','(i) دا طریقه د پلي کولو لپاره ډېره ساده ده.'),('v2','(ii) For one series, there is only one trend line.','(ii) ایک سلسلے کے لیے صرف ایک رجحان کی لکیر ہوتی ہے۔','(ii) د یوې لړۍ لپاره یوازې یوه د تمایل کرښه شته.')],'semi-adv')
add(s,'dh','Disadvantages','نقصانات','زیانونه')
L(s,[('w1','(i) It is affected by extreme values.','(i) یہ انتہائی قدروں سے متاثر ہوتا ہے۔','(i) دا د سختو ارزښتونو لخوا اغېزمن کېږي.'),('w2','(ii) It is used only when the trend is linear or nearly linear.','(ii) یہ صرف اس وقت استعمال ہوتا ہے جب رجحان خطی یا تقریباً خطی ہو۔','(ii) دا یوازې هغه وخت کارول کېږي چې تمایل خطي یا نږدې خطي وي.')],'semi-dis')
add(s,'h3','(iii) The method of moving average','(iii) متحرک اوسط کا طریقہ','(iii) د خوځېدونکي اوسط طریقه')
add(s,'t3','In this method, arithmetic mean is calculated successively by taking a specified number of values at a time say 3, 5, 7 etc., then leaving the first value','اس طریقے میں حسابی اوسط یکے بعد دیگرے ایک وقت میں قدروں کی مخصوص تعداد لے کر حساب کیا جاتا ہے مثلاً 3، 5، 7 وغیرہ، پھر پہلی قدر کو چھوڑ کر','پدې طریقه کې حسابي اوسط پرله‌پسې د یو وخت د ارزښتونو ټاکلی شمېر اخیستلو سره محاسبه کېږي لکه 3، 5، 7 او نور، بیا لومړی ارزښت پرېښودو سره',sourceGap=dict(note='The sentence continues on the next page ("and including the next value …").'))
rows=[('1976','286'),('1977','260'),('1978','276'),('1979','270'),('1980','…'),('1981','348'),('1982','351'),('1983','321'),('1984','346')]
av=['','1092 ÷ 4 = 273','','','','','1366 ÷ 4 = 341.5','','']
av=['','1092 ÷ 4 = 273','','','','','','1366 ÷ 4 = 341.5','']
s['tables']=[table('Example 6.2 (b) solution: values and averages','مثال 6.2 (ب) کا حل: قدریں اور اوسط','د بېلګې 6.2 (b) حل: ارزښتونه او اوسطونه',[c('Year','سال','کال'),c('Values','قدریں','ارزښتونه'),c('Averages','اوسط','اوسطونه')],[[c(rows[i][0]),c(rows[i][1]),c(av[i])] for i in range(9)],exampleId=E62)]
s['figures']=[dict(id='stat11-s211-fig1',svg=semifig_b(),caption='Graph showing the semi-average trend (Example 6.2 (b))',captionUrdu='نیم اوسط رجحان دکھانے والا گراف (مثال 6.2 (ب))',captionPashto='د نیمه اوسط د تمایل ښودونکی ګراف (بېلګه 6.2 (b))',labels=[lab('y-axis','y-محور','y-محور'),lab('x-axis','x-محور','x-محور')],sourceGap=dict(note='Redrawn as a coded graph: the semi-average points are at the mid-years of the two groups with values 273 and 341.5.'))]
P=lambda *ks:dict(type='paragraphs',ids=[pid(211,k) for k in ks])
s['flow']=[P('a1'),dict(type='table',index=0),dict(type='figure',index=0),P('ah','v1','v2','dh','w1','w2','h3','t3')]
s['sourceNote']='Printed page 201. In the solution table the middle value (1980) is printed as "…" and excluded from both groups; the averages 273 and 341.5 are printed beside brackets that group the first four and last four years and are placed on the second and eighth rows. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 212 (printed 202) ----------
s=page(212,U,'202','Moving average method (end) · Example 6.3: 3-year and 5-year moving averages','متحرک اوسط کا طریقہ (اختتام) · مثال 6.3: 3 سالہ اور 5 سالہ متحرک اوسط','د خوځېدونکي اوسط طریقه (پای) · بېلګه 6.3: 3 کلن او 5 کلن خوځېدونکي اوسطونه','ts-ma-1')
Flow(s)
add(s,'c1','and including the next value. This process is continued till all the values in the series are finished. The averages so obtained are placed against the centre of each group.','اور اگلی قدر کو شامل کر کے۔ یہ عمل اس وقت تک جاری رہتا ہے جب تک سلسلے کی تمام قدریں ختم نہ ہو جائیں۔ اس طرح حاصل ہونے والے اوسط ہر گروہ کے مرکز کے سامنے رکھے جاتے ہیں۔','او بل ارزښت شاملولو سره. دا پروسه تر هغه دوام کوي څو د لړۍ ټول ارزښتونه پای ته ورسېږي. په دې توګه ترلاسه شوي اوسطونه د هرې ډلې د مرکز په مقابل کې ایښودل کېږي.',sourceGap=dict(note='Completes the sentence from the previous page.'))
add(s,'c2','When we find the moving average taking an even number of values say 2, 4, 6 etc. the middle of the group will lie between two years. In order to make the averages coincide with a particular year, we centre the total by calculating further a 2-year moving total of the even order moving totals. Then moving averages are computed called centred moving averages.','جب ہم قدروں کی جفت تعداد لے کر متحرک اوسط نکالتے ہیں مثلاً 2، 4، 6 وغیرہ تو گروہ کا درمیان دو سالوں کے بیچ میں ہوگا۔ اوسطوں کو کسی خاص سال کے ساتھ منطبق کرنے کے لیے ہم جفت درجے کے متحرک مجموعوں کا مزید 2 سالہ متحرک مجموعہ حساب کر کے مجموعے کو مرکز میں لاتے ہیں۔ پھر متحرک اوسط حساب کیے جاتے ہیں جنہیں مرکزی متحرک اوسط کہتے ہیں۔','کله چې موږ د ارزښتونو جفت شمېر اخیستلو سره خوځېدونکی اوسط موندو لکه 2، 4، 6 او نور نو د ډلې منځ به د دوو کلونو تر منځ وي. د دې لپاره چې اوسطونه له یو ځانګړي کال سره سره برابر شي، موږ د جفت ترتیب خوځېدونکو مجموعو د 2 کلن خوځېدونکي مجموعې په نورې محاسبې سره مجموعه په مرکز کې راولو. بیا خوځېدونکي اوسطونه محاسبه کېږي چې مرکزي خوځېدونکي اوسطونه بلل کېږي.')
head(s,'ex63','Example: 6.3','مثال: 6.3','بېلګه: 6.3',exampleId=E63)
add(s,'q63','Find (i) 3-year and (ii) 5-year moving average for the following time series:','درج ذیل وقتی سلسلے کے لیے (i) 3 سالہ اور (ii) 5 سالہ متحرک اوسط معلوم کریں:','د لاندې وخت لړۍ لپاره (i) 3 کلن او (ii) 5 کلن خوځېدونکی اوسط ومومئ:',role='question',exampleId=E63)
head(s,'sol63','Solution:','حل:','حل:',exampleId=E63)
yrs=list(range(2005,2017)); vals=[20,23,25,28,23,29,32,27,37,35,32,35]
t3=['-',68,76,76,80,84,88,96,99,104,102,'-']; a3=['-',23,25,25,27,28,29,32,33,35,34,'-']
t5=['-','-',119,128,137,139,148,160,163,166,'-','-']; a5=['-','-',24,26,27,28,30,32,33,33,'-','-']
s['tables']=[table('Example 6.3: years and values','مثال 6.3: سال اور قدریں','بېلګه 6.3: کلونه او ارزښتونه',[c('Years:','سال:','کلونه:')]+[c(str(v)) for v in yrs],[row('Values:','قدریں:','ارزښتونه:',vals)],exampleId=E63),
 table('Example 6.3 solution table','مثال 6.3 کا حل: جدول','د بېلګې 6.3 د حل جدول',[c('Years','سال','کلونه'),c('Values (y)','قدریں (y)','ارزښتونه (y)'),c('3-year moving totals','3 سالہ متحرک مجموعے','3 کلن خوځېدونکي مجموعې'),c('3-years moving averages: (ŷ)','3 سالہ متحرک اوسط: (ŷ)','3 کلن خوځېدونکي اوسطونه: (ŷ)'),c('5-year moving totals','5 سالہ متحرک مجموعے','5 کلن خوځېدونکي مجموعې'),c('5-year moving averages: (ŷ)','5 سالہ متحرک اوسط: (ŷ)','5 کلن خوځېدونکي اوسطونه: (ŷ)')],[[c(str(yrs[i])),c(str(vals[i])),c(str(t3[i])),c(str(a3[i])),c(str(t5[i])),c(str(a5[i]))] for i in range(12)],exampleId=E63)]
P=lambda *ks:dict(type='paragraphs',ids=[pid(212,k) for k in ks])
s['flow']=[P('c1','c2','ex63','q63'),dict(type='table',index=0),P('sol63'),dict(type='table',index=1)]
s['sourceNote']='Printed page 202. The years in the question row are printed split over two lines ("200 / 5" for 2005 etc.) and are read as full years. Header graphics and watermark excluded.'
s['vocabulary']={'moving average':dict(ur='متحرک اوسط',ps='خوځېدونکی اوسط')}
save(s)
# ---------- scan 213 (printed 203) ----------
s=page(213,U,'203','Example 6.4: 4-year centred moving averages','مثال 6.4: 4 سالہ مرکزی متحرک اوسط','بېلګه 6.4: 4 کلن مرکزي خوځېدونکي اوسطونه','ts-ma-2')
Flow(s)
head(s,'ex64','Example: 6.4','مثال: 6.4','بېلګه: 6.4',exampleId=E64)
add(s,'q64','Compute the 4-year centered moving averages for the following time series:','درج ذیل وقتی سلسلے کے لیے 4 سالہ مرکزی متحرک اوسط حساب کریں:','د لاندې وخت لړۍ لپاره 4 کلن مرکزي خوځېدونکي اوسطونه محاسبه کړئ:',role='question',exampleId=E64)
head(s,'sol64','Solution:','حل:','حل:',exampleId=E64)
add(s,'n1','In column (3) the 4-year moving totals 290, 292, 293, 294, 306, 300, 303, 313 and 305 are printed between consecutive years (each between the rows 1981–1982, 1982–1983, …, 1989–1990); they are listed separately in the second table.','کالم (3) میں 4 سالہ متحرک مجموعے 290، 292، 293، 294، 306، 300، 303، 313 اور 305 مسلسل سالوں کے بیچ میں چھپے ہیں (ہر ایک سطروں 1981–1982، 1982–1983، …، 1989–1990 کے درمیان)؛ انہیں دوسرے جدول میں الگ سے درج کیا گیا ہے۔','په کالم (3) کې 4 کلن خوځېدونکي مجموعې 290، 292، 293، 294، 306، 300، 303، 313 او 305 د پرله‌پسې کلونو تر منځ چاپ شوې دي (هره یوه د قطارونو 1981–1982، 1982–1983، …، 1989–1990 تر منځ)؛ دوی په دویم جدول کې جلا لیکل شوي دي.',role='solution',exampleId=E64)
yrs=list(range(1980,1992)); vals=[72,68,78,72,74,69,79,84,69,72,89,76]
t2=['-','-',582,585,587,600,606,603,616,618,'-','-']; av=['-','-','72.75','73.125','73.375','75','75.75','75.375','77','77.25','-','-']
mid=[('1981 – 1982',290),('1982 – 1983',292),('1983 – 1984',293),('1984 – 1985',294),('1985 – 1986',306),('1986 – 1987',300),('1987 – 1988',303),('1988 – 1989',313),('1989 – 1990',305)]
s['tables']=[table('Example 6.4: years and prices','مثال 6.4: سال اور قیمتیں','بېلګه 6.4: کلونه او بیې',[c('Years:','سال:','کلونه:')]+[c(str(v)) for v in yrs],[row('Prices:','قیمتیں:','بیې:',vals)],exampleId=E64),
 table('Example 6.4 solution table','مثال 6.4 کا حل: جدول','د بېلګې 6.4 د حل جدول',[c('Years (1)','سال (1)','کلونه (1)'),c('Values (y) (2)','قدریں (y) (2)','ارزښتونه (y) (2)'),c('2-years moving totals (4)','2 سالہ متحرک مجموعے (4)','2 کلن خوځېدونکي مجموعې (4)'),c('4-year centred moving averages: column (4) ÷ 8 (ŷ)','4 سالہ مرکزی متحرک اوسط: کالم (4) ÷ 8 (ŷ)','4 کلن مرکزي خوځېدونکي اوسطونه: کالم (4) ÷ 8 (ŷ)')],[[c(str(yrs[i])),c(str(vals[i])),c(str(t2[i])),c(av[i])] for i in range(12)],exampleId=E64),
 table('Example 6.4: 4-year moving totals, column (3)','مثال 6.4: 4 سالہ متحرک مجموعے، کالم (3)','بېلګه 6.4: 4 کلن خوځېدونکي مجموعې، کالم (3)',[c('Between years','سالوں کے بیچ','د کلونو تر منځ'),c('4-year moving totals (3)','4 سالہ متحرک مجموعے (3)','4 کلن خوځېدونکي مجموعې (3)')],[[c(a),c(str(b))] for a,b in mid],exampleId=E64)]
P=lambda *ks:dict(type='paragraphs',ids=[pid(213,k) for k in ks])
s['flow']=[P('ex64','q64'),dict(type='table',index=0),P('sol64'),dict(type='table',index=1),P('n1'),dict(type='table',index=2)]
s['sourceNote']='Printed page 203. In the printed solution table the 4-year moving totals (column 3) sit halfway between the year rows; they are therefore listed in a separate table keyed by the pair of years. Printed spellings kept: "centered", "centred". Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 214 (printed 204) ----------
s=page(214,U,'204','Moving average merits and demerits · (iv) Method of least squares · Coding time variable · Example 6.5 (start)','متحرک اوسط کے فوائد اور نقصانات · (iv) کم از کم مربعات کا طریقہ · وقت کے متغیر کی کوڈنگ · مثال 6.5 (آغاز)','د خوځېدونکي اوسط ګټې او زیانونه · (iv) د لږ تر لږه مربعاتو طریقه · د وخت د متغیر کوډ کول · بېلګه 6.5 (پیل)','ts-ls-1')
Flow(s)
add(s,'t0','Advantages and disadvantages of moving average Method','متحرک اوسط کے طریقے کے فوائد اور نقصانات','د خوځېدونکي اوسط طریقې ګټې او زیانونه')
L(s,[('v1','(i) This method is simple to apply.','(i) یہ طریقہ لاگو کرنا آسان ہے۔','(i) دا طریقه د پلي کولو لپاره ساده ده.'),('v2','(ii) It eliminates the short term fluctuations.','(ii) یہ قلیل مدتی اتار چڑھاؤ کو ختم کرتا ہے۔','(ii) دا لنډمهاله بدلونونه له منځه وړي.'),('v3','(iii) It reduces the effect of extreme values.','(iii) یہ انتہائی قدروں کے اثر کو کم کرتا ہے۔','(iii) دا د سختو ارزښتونو اغېز کموي.')],'ma-adv')
add(s,'dh','Disadvantages','نقصانات','زیانونه')
L(s,[('w1','(i) Some values at the beginning and at the end of a time series are lost so it is not an appropriate method for projections.','(i) وقتی سلسلے کے آغاز اور اختتام کی کچھ قدریں ضائع ہو جاتی ہیں اس لیے یہ تخمینوں کے لیے موزوں طریقہ نہیں۔','(i) د وخت لړۍ د پیل او پای ځینې ارزښتونه له منځه ځي نو دا د وړاندوینو لپاره مناسبه طریقه نه ده.'),('w2','(ii) This method is preferred for a small number of years.','(ii) یہ طریقہ سالوں کی کم تعداد کے لیے ترجیح دیا جاتا ہے۔','(ii) دا طریقه د کلونو د لږ شمېر لپاره غوره ګڼل کېږي.')],'ma-dis')
add(s,'h4','(iv) The method of least squares:','(iv) کم از کم مربعات کا طریقہ:','(iv) د لږ تر لږه مربعاتو طریقه:')
add(s,'t4','The secular trend can also be measured by fitting a straight line to the given data whereas straight line is best fitted by the method of least squares. According to this method equation for a straight line or linear trend is ŷ = a + bx, where','صدیوی رجحان کو دیے گئے اعداد و شمار پر سیدھی لکیر فٹ کر کے بھی ناپا جا سکتا ہے جبکہ سیدھی لکیر کم از کم مربعات کے طریقے سے بہترین فٹ ہوتی ہے۔ اس طریقے کے مطابق سیدھی لکیر یا خطی رجحان کی مساوات ŷ = a + bx ہے، جہاں','عمري تمایل د ورکړل شویو معلوماتو ته د مستقیمې کرښې په برابرولو سره هم اندازه کېدای شي پداسې حال کې چې مستقیمه کرښه د لږ تر لږه مربعاتو په طریقه ښه برابرېږي. د دې طریقې له مخې د مستقیمې کرښې یا خطي تمایل معادله ŷ = a + bx ده، چېرته چې')
add(s,'t5','After finding the values of a and b, the fitted equation is used to find the trend values ŷ.','a اور b کی قدریں معلوم کرنے کے بعد فٹ کی گئی مساوات رجحان کی قدریں ŷ معلوم کرنے کے لیے استعمال کی جاتی ہے۔','د a او b د ارزښتونو له موندلو وروسته برابره شوې معادله د تمایل ارزښتونو ŷ د موندلو لپاره کارول کېږي.')
add(s,'h6','Coding time variable:','وقت کے متغیر کی کوڈنگ:','د وخت د متغیر کوډ کول:')
add(s,'t6','In a time series only time (t) and values (y) are given. The variable x is obtained by coding the time variable as follows;','وقتی سلسلے میں صرف وقت (t) اور قدریں (y) دی جاتی ہیں۔ متغیر x وقت کے متغیر کی کوڈنگ سے یوں حاصل کیا جاتا ہے؛','په وخت لړۍ کې یوازې وخت (t) او ارزښتونه (y) ورکول کېږي. متغیر x د وخت د متغیر په کوډ کولو سره داسې ترلاسه کېږي؛')
add(s,'c1','Case i: If the number of years is odd, take x = … −2, −1, 0, 1, 2, … i.e.','حالت i: اگر سالوں کی تعداد طاق ہو تو x = … −2, −1, 0, 1, 2, … لیں یعنی','حالت i: که د کلونو شمېر طاق وي نو x = … −2, −1, 0, 1, 2, … واخلئ یعنې')
add(s,'c2','Case ii: If the number of years is even, take x = … −7, −5, −3, −1, 1, 3, 5, 7, … i.e.','حالت ii: اگر سالوں کی تعداد جفت ہو تو x = … −7, −5, −3, −1, 1, 3, 5, 7, … لیں یعنی','حالت ii: که د کلونو شمېر جفت وي نو x = … −7, −5, −3, −1, 1, 3, 5, 7, … واخلئ یعنې')
head(s,'ex65','Example: 6.5','مثال: 6.5','بېلګه: 6.5',exampleId=E65)
add(s,'q65','Find the trend values by fitting a least squares straight line from the following data.','درج ذیل اعداد و شمار سے کم از کم مربعات کی سیدھی لکیر فٹ کر کے رجحان کی قدریں معلوم کریں۔','له لاندې معلوماتو څخه د لږ تر لږه مربعاتو مستقیمه کرښه برابرولو سره د تمایل ارزښتونه ومومئ.',role='question',exampleId=E65,sourceGap=dict(note='The data of Example 6.5 are printed on the next page.'))
s['tables']=[table('Case i: odd number of years, coded time','حالت i: سالوں کی طاق تعداد، کوڈ شدہ وقت','حالت i: د کلونو طاق شمېر، کوډ شوی وخت',[c('Years','سال','کلونه')]+[c(str(v)) for v in range(2001,2006)],[row('Coded time (x)','کوڈ شدہ وقت (x)','کوډ شوی وخت (x)',[-2,-1,0,1,2])]),
 table('Case ii: even number of years, coded time','حالت ii: سالوں کی جفت تعداد، کوڈ شدہ وقت','حالت ii: د کلونو جفت شمېر، کوډ شوی وخت',[c('Years','سال','کلونه')]+[c(str(v)) for v in range(2010,2016)],[row('Coded time (x)','کوڈ شدہ وقت (x)','کوډ شوی وخت (x)',[-5,-3,-1,1,3,5])])]
s['equations']+=[eqn(214,'f',r'b=\dfrac{n\sum xy-\sum x\sum y}{n\sum x^2-\left(\sum x\right)^2}\quad\text{and}\quad a=\dfrac{\sum y}{n}-b\left(\dfrac{\sum x}{n}\right)','b = (nΣxy − ΣxΣy)/(nΣx² − (Σx)²) and a = Σy/n − b(Σx/n)')]
P=lambda *ks:dict(type='paragraphs',ids=[pid(214,k) for k in ks])
s['flow']=[P('t0','v1','v2','v3','dh','w1','w2','h4','t4'),dict(type='equation',index=0),P('t5','h6','t6','c1'),dict(type='table',index=0),P('c2'),dict(type='table',index=1),P('ex65','q65')]
s['sourceNote']='Printed page 204. The formulas for b and a are printed inside the paragraph and are shown as an equation after it. Header graphics and watermark excluded.'
s['vocabulary']={'coding':dict(ur='کوڈنگ',ps='کوډ کول')}
save(s)
