from stathelp import *
import math
c=cell
U='time-series'
E61='stat11-ex-6-1'; E62='stat11-ex-6-2'
def row(a,b,d,vals): return [c(a,b,d)]+[c(str(v)) for v in vals]
def wave():
    W,H=620,200
    pts=[]
    # smooth wave: peaks at x=105 and x=345 and x=570; troughs at 235 and 445 (schematic)
    def y(x):
        return 100-65*math.sin((x-30)/ (2*math.pi*70) *2*math.pi*0.5*2)  # placeholder replaced below
    # build curve with cosine of period ~ 250 starting at low point near x=20
    import math as m
    ptsL=[]
    for i in range(0,601):
        x=20+i*0.95
        yy=100-60*m.sin((x-20)/115*m.pi - 0.0)
        ptsL.append((x,yy))
    o='<polyline points="'+' '.join(f'{x:.1f},{yv:.1f}' for x,yv in ptsL)+'" fill="none" stroke="#111" stroke-width="1.8"/>'
    o+=T(120,38,'Prosperity',13)+T(335,32,'Prosperity',13)+T(238,178,'Depression',13)
    o+='<text x="165" y="92" font-size="12" font-family="Arial,sans-serif" transform="rotate(48 165 92)">Recession</text>'
    o+='<text x="305" y="80" font-size="12" font-family="Arial,sans-serif" transform="rotate(-55 305 80)">Recovery</text>'
    return svg(W,H,'A wave-shaped cycle curve rising to prosperity, falling through recession to depression and rising again through recovery to the next prosperity peak',o)
def trendfig():
    W,H=620,360
    yrs=list(range(2000,2008)); vals=[12,14,10,16,18,16,20,18]
    px=lambda i:100+i*65; py=lambda v:300-v*(230/22.0)
    o=f'<line x1="70" y1="40" x2="70" y2="300" stroke="#111" stroke-width="1.8"/><line x1="70" y1="300" x2="590" y2="300" stroke="#111" stroke-width="1.8"/>'
    for v in (0,10,20): o+=T(60,py(v)+4,str(v),12,'end')
    o+=T(70,30,'y-axis',12,'start')+T(596,304,'x-axis',12,'start')+T(260,40,'Graph showing the trend',13)+T(440,40,'Scale: on x-axis 6.S.S = 1; on y-axis 1.S.S = 1',11,'start')
    for i,yv in enumerate(yrs):
        o+=f'<line x1="{px(i)}" y1="296" x2="{px(i)}" y2="304" stroke="#111"/>'+T(px(i),322,str(yv),12)
    o+='<polyline points="'+' '.join(f'{px(i)},{py(v):.1f}' for i,v in enumerate(vals))+'" fill="none" stroke="#111" stroke-width="1.8"/>'
    for i,v in enumerate(vals): o+=f'<circle cx="{px(i)}" cy="{py(v):.1f}" r="3.5" fill="#111"/>'
    o+=f'<line x1="{px(0)-20}" y1="{py(11):.1f}" x2="{px(7)+40}" y2="{py(21):.1f}" stroke="#1c7ab8" stroke-width="1.8"/>'
    return svg(W,H,'Freehand trend graph: yearly values 2000 to 2007 joined by a zig-zag line with a rising straight trend line drawn through them',o)
def semifig():
    W,H=620,330
    yrs=list(range(1980,1988))
    px=lambda x:80+(x-1980)*66; py=lambda v:270-v*(220/130.0)
    o='<line x1="60" y1="40" x2="60" y2="270" stroke="#111" stroke-width="1.8"/><line x1="60" y1="270" x2="590" y2="270" stroke="#111" stroke-width="1.8"/>'
    for v in (0,40,80,120): o+=T(52,py(v)+4,str(v),12,'end')
    o+=T(60,28,'y-axis',12,'start')+T(596,274,'x-axis',12,'start')+T(300,34,'Graph showing semi-average trend',13)
    for yv in yrs: o+=f'<line x1="{px(yv)}" y1="266" x2="{px(yv)}" y2="274" stroke="#111"/>'+T(px(yv),292,str(yv),12)
    o+=f'<line x1="{px(1979.6)}" y1="{py(88):.1f}" x2="{px(1987.4)}" y2="{py(122):.1f}" stroke="#1c7ab8" stroke-width="1.8"/>'
    for xx,vv in ((1981.5,93),(1985.5,105)): o+=f'<circle cx="{px(xx):.1f}" cy="{py(vv):.1f}" r="4" fill="#111"/>'
    return svg(W,H,'Semi-average trend: a straight line passing through the two semi-average points (1981.5, 93) and (1985.5, 105) rising slowly to the right',o)
# ---------- scan 207 (printed 197) ----------
s=page(207,U,'197','6.1.1 Components of a time series','6.1.1 وقتی سلسلے کے اجزاء','6.1.1 د وخت لړۍ برخې','ts-components-1')
Flow(s)
add(s,'c1','the future operations.','مستقبل کے عملیات۔','راتلونکي عملیات.',sourceGap=dict(note='Completes the sentence from the previous page ("… (iv) planning").'))
head(s,'h611','6.1.1 Components of a time series','6.1.1 وقتی سلسلے کے اجزاء','6.1.1 د وخت لړۍ برخې')
add(s,'t611','There are four main types of components which cause change in a time series.','وقتی سلسلے میں تبدیلی کا باعث بننے والے اجزاء کی چار بڑی اقسام ہیں۔','د وخت لړۍ د بدلون لامل کېدونکو برخو څلور اصلي ډولونه شته.')
add(s,'h1','(i) Secular trend','(i) صدیوی رجحان','(i) عمري تمایل')
add(s,'t1','The term secular trend means changes occurring in a time series in one direction over a fairly long period of time. It reflects the tendency of either persistent growth or persistent decline and is usually spread over a period not less than ten years e.g. agricultural production, banking business is increasing since 1947.','صدیوی رجحان کی اصطلاح کا مطلب وقتی سلسلے میں ایک سمت میں خاصے طویل عرصے میں واقع ہونے والی تبدیلیاں ہیں۔ یہ مسلسل اضافے یا مسلسل کمی کے رجحان کی عکاسی کرتا ہے اور عموماً دس سال سے کم نہ ہونے والی مدت پر پھیلا ہوتا ہے مثلاً زرعی پیداوار، بینکاری کا کاروبار 1947 سے بڑھ رہا ہے۔','د عمري تمایل اصطلاح پدې معنا چې په وخت لړۍ کې په یو لوري کې په ښه اوږده مودې کې رامنځته کېدونکي بدلونونه. دا د دوامدار ودې یا دوامدار کموالي تمایل ښيي او معمولاً د لسو کلونو څخه نه کمې مودې ته پراخېږي لکه کرنیز تولید، بانکي سوداګري له 1947 راهیسې زیاتېږي.')
add(s,'h2','(ii) Seasonal variations','(ii) موسمی تغیرات','(ii) موسمي تغیرات')
add(s,'t2','As name indicates these changes occur due to a seasonal effect within a year, a month, a week or even a day. That is why called short-term variations. For example, certain items have more sales in a particular season like ice cream in summer, umbrellas in rainy season, and woolen cloths in winter season etc.','جیسا کہ نام سے ظاہر ہے یہ تبدیلیاں ایک سال، ایک مہینے، ایک ہفتے یا حتیٰ کہ ایک دن کے اندر موسمی اثر کی وجہ سے واقع ہوتی ہیں۔ اسی لیے انہیں قلیل مدتی تغیرات کہا جاتا ہے۔ مثال کے طور پر، بعض اشیاء کی کسی خاص موسم میں زیادہ فروخت ہوتی ہے جیسے گرمیوں میں آئس کریم، برسات کے موسم میں چھتریاں اور سردیوں کے موسم میں اونی کپڑے وغیرہ۔','لکه څنګه چې نوم ښيي دا بدلونونه په یو کال، یوې میاشت، یوې اوونۍ یا حتی یوې ورځې کې د موسمي اغېز له امله رامنځته کېږي. همدا لامل دی چې دوی ته لنډمهاله تغیرات ویل کېږي. د مثال په توګه، ځینې توکي په یو ځانګړي موسم کې ډېر پلورل کېږي لکه په اوړي کې آیس کریم، د باران په موسم کې چترۍ او د ژمي په موسم کې وړیني جامې او نور.')
add(s,'h3','(iii) Cyclical variations','(iii) دوری تغیرات','(iii) دوري تغیرات')
add(s,'t3','A journey from one peak (say prosperity) to another peak (prosperity) is called a cycle. A complete cycle has four constituents namely prosperity, recession, depression and recovery.','ایک چوٹی (مثلاً خوشحالی) سے دوسری چوٹی (خوشحالی) تک کا سفر چکر کہلاتا ہے۔ ایک مکمل چکر کے چار اجزاء ہوتے ہیں یعنی خوشحالی، کساد بازاری، ڈپریشن اور بحالی۔','له یوې څوکې (لکه سوکالۍ) څخه بلې څوکې (سوکالۍ) ته سفر یو دوره بلل کېږي. یوه بشپړه دوره څلور برخې لري یعنې سوکالي، کساد، ډپریشن او بیا رغېدنه.')
add(s,'t4','A cycle covers a long span of time ranging from 2 to 10 years or even a longer period. Cycles related to business are called business cycles or trade cycles. The length of business cycles varies from one business to the other.','ایک چکر 2 سے 10 سال یا اس سے بھی طویل مدت پر محیط ہوتا ہے۔ کاروبار سے متعلق چکر کاروباری چکر یا تجارتی چکر کہلاتے ہیں۔ کاروباری چکروں کی طوالت ایک کاروبار سے دوسرے میں مختلف ہوتی ہے۔','یوه دوره له 2 څخه تر 10 کلونو یا حتی لویې مودې پورې اوږده موده پوښي. له سوداګرۍ سره تړلې دورې سوداګریزې دورې یا تجارتي دورې بلل کېږي. د سوداګریزو دورو اوږدوالی له یوې سوداګرۍ څخه بلې ته توپیر لري.')
add(s,'h4','(iv) Irregular variations','(iv) بے قاعدہ تغیرات','(iv) بې‌قاعده تغیرات')
add(s,'t5','These variations are unpredictable, unavoidable, and unsystematic in nature and occur by chance. It occurs due to floods, fires, earthquakes, wars, feminine, accidents, epidemics, labour strikes, elections etc. All these events occur from time to time but there is no regularity in their occurrence. They are also called random variations or residual variations or accidental variations or erratic variations.','یہ تغیرات غیر متوقع، ناگزیر اور غیر منظم نوعیت کے ہوتے ہیں اور اتفاقی طور پر واقع ہوتے ہیں۔ یہ سیلاب، آگ، زلزلوں، جنگوں، قحط، حادثات، وباؤں، مزدوروں کی ہڑتالوں، انتخابات وغیرہ کی وجہ سے واقع ہوتے ہیں۔ یہ تمام واقعات وقتاً فوقتاً واقع ہوتے ہیں لیکن ان کے وقوع میں کوئی باقاعدگی نہیں ہوتی۔ انہیں بے ترتیب تغیرات یا باقی ماندہ تغیرات یا حادثاتی تغیرات یا بے ڈھنگے تغیرات بھی کہا جاتا ہے۔','دا تغیرات ناڅرګند، ناڅاپي او غیر منظم طبیعت لري او په اتفاقي ډول رامنځته کېږي. دا د سېلابونو، اورونو، زلزلو، جګړو، قحط، پېښو، وبا، د کارګرانو اعتصابونو، ټاکنو او نورو له امله رامنځته کېږي. دا ټول پېښې وخت په وخت رامنځته کېږي خو د هغو په رامنځته کېدو کې هېڅ منظمتیا نشته. دوی ته تصادفي تغیرات یا پاتې تغیرات یا اتفاقي تغیرات یا بې‌ځایه تغیرات هم ویل کېږي.')
s['figures']=[dict(id='stat11-s207-fig1',svg=wave(),caption='A business cycle: prosperity, recession, depression and recovery',captionUrdu='کاروباری چکر: خوشحالی، کساد بازاری، ڈپریشن اور بحالی',captionPashto='سوداګریزه دوره: سوکالي، کساد، ډپریشن او بیا رغېدنه',labels=[lab('Prosperity','خوشحالی','سوکالي'),lab('Recession','کساد بازاری','کساد'),lab('Depression','ڈپریشن','ډپریشن'),lab('Recovery','بحالی','بیا رغېدنه')],sourceGap=dict(note='Redrawn as a coded schematic of the printed wave curve with its four labelled phases.'))]
P=lambda *ks:dict(type='paragraphs',ids=[pid(207,k) for k in ks])
s['flow']=[P('c1','h611','t611','h1','t1','h2','t2','h3','t3'),dict(type='figure',index=0),P('t4','h4','t5')]
s['sourceNote']='Printed page 197. The first words complete the sentence from the previous page. The cycle figure shows a wave with the labels Prosperity (twice), Recession, Recovery and Depression. Printed spellings kept: "feminine" (for famine). Header graphics and watermark excluded.'
s['vocabulary']={'secular trend':dict(ur='صدیوی رجحان',ps='عمري تمایل'),'seasonal variations':dict(ur='موسمی تغیرات',ps='موسمي تغیرات')}
save(s)
# ---------- scan 208 (printed 198) ----------
s=page(208,U,'198','6.1.2 Measuring components · 6.1.3 Mathematical models · 6.1.4 Measurement of secular trend · (i) Freehand curve method','6.1.2 اجزاء کی پیمائش · 6.1.3 ریاضیاتی ماڈل · 6.1.4 صدیوی رجحان کی پیمائش · (i) آزاد دستی منحنی کا طریقہ','6.1.2 د برخو اندازه کول · 6.1.3 ریاضیاتي ماډلونه · 6.1.4 د عمري تمایل اندازه کول · (i) د آزاد لاس منحني طریقه','ts-models-1')
Flow(s)
head(s,'h612','6.1.2 Measuring and isolating the components of a time series','6.1.2 وقتی سلسلے کے اجزاء کی پیمائش اور علیحدگی','6.1.2 د وخت لړۍ د برخو اندازه کول او جلا کول')
add(s,'t612','After description of the various components, the next step in the analysis of time series is to measure and remove these changes from the time series. For this purpose every component has its own procedures.','مختلف اجزاء کی تفصیل کے بعد وقتی سلسلے کے تجزیے کا اگلا قدم ان تبدیلیوں کو ناپنا اور وقتی سلسلے سے ہٹانا ہے۔ اس مقصد کے لیے ہر جزو کے اپنے طریقے ہیں۔','د بېلابېلو برخو له بیان وروسته د وخت لړۍ په تحلیل کې بل ګام دا دی چې دا بدلونونه اندازه او د وخت لړۍ څخه لرې شي. د دې موخې لپاره هره برخه خپلې طریقې لري.')
head(s,'h613','6.1.3 Mathematical models for a time series analysis','6.1.3 وقتی سلسلے کے تجزیے کے ریاضیاتی ماڈل','6.1.3 د وخت لړۍ د تحلیل لپاره ریاضیاتي ماډلونه')
add(s,'t613','To apply a mathematical model in a time series analysis we first make assumptions about the relationship existing among the various components. It is commonly assumed that these components have either multiplicative relationship or additive relationship.','وقتی سلسلے کے تجزیے میں ریاضیاتی ماڈل لاگو کرنے کے لیے ہم پہلے مختلف اجزاء کے درمیان موجود تعلق کے بارے میں مفروضے بناتے ہیں۔ عام طور پر فرض کیا جاتا ہے کہ ان اجزاء میں یا تو ضربی تعلق ہے یا جمعی تعلق۔','د وخت لړۍ په تحلیل کې د ریاضیاتي ماډل د پلي کولو لپاره موږ لومړی د بېلابېلو برخو تر منځ د شته اړیکې په اړه انګېرنې کوو. عموماً انګېرل کېږي چې دا برخې یا ضربي اړیکه لري یا جمعي اړیکه.')
add(s,'h1','(i) Multiplicative model','(i) ضربی ماڈل','(i) ضربي ماډل')
add(s,'t1','In case of multiplicative relationship, it is assumed that any particular observation “y” at time “t” is a result of the product of the effect of the four components of a time series namely trend (T), seasonal variations (S), cyclic variations (C) and the irregular variations (I) i.e. y_t = T × S × C × I. This model does not assume the independence of the four components of the time series. It is appropriate for projections.','ضربی تعلق کی صورت میں فرض کیا جاتا ہے کہ وقت “t” پر کوئی خاص مشاہدہ “y” وقتی سلسلے کے چار اجزاء یعنی رجحان (T)، موسمی تغیرات (S)، دوری تغیرات (C) اور بے قاعدہ تغیرات (I) کے اثر کے حاصلِ ضرب کا نتیجہ ہے یعنی y_t = T × S × C × I۔ یہ ماڈل وقتی سلسلے کے چار اجزاء کی آزادی کا مفروضہ نہیں بناتا۔ یہ تخمینوں کے لیے موزوں ہے۔','د ضربي اړیکې په حالت کې انګېرل کېږي چې په وخت “t” کې هره ځانګړې کتنه “y” د وخت لړۍ د څلورو برخو یعنې تمایل (T)، موسمي تغیرات (S)، دوري تغیرات (C) او بې‌قاعده تغیرات (I) د اغېز د ضرب پایله ده یعنې y_t = T × S × C × I. دا ماډل د وخت لړۍ د څلورو برخو خپلواکي نه انګېري. دا د وړاندوینو لپاره مناسب دی.')
add(s,'h2','(ii) Additive model','(ii) جمعی ماڈل','(ii) جمعي ماډل')
add(s,'t2','Some people believe that the observation y is a result of additive effect of the components i.e. y_t = T + S + C + I. This model is based on the assumption that the four components are independent of each other. It is rarely used as it is not appropriate for future events.','بعض لوگ یقین رکھتے ہیں کہ مشاہدہ y اجزاء کے جمعی اثر کا نتیجہ ہے یعنی y_t = T + S + C + I۔ یہ ماڈل اس مفروضے پر مبنی ہے کہ چاروں اجزاء ایک دوسرے سے آزاد ہیں۔ یہ شاذ و نادر استعمال ہوتا ہے کیونکہ یہ مستقبل کے واقعات کے لیے موزوں نہیں۔','ځینې خلک باور لري چې کتنه y د برخو د جمعي اغېز پایله ده یعنې y_t = T + S + C + I. دا ماډل پر دې انګېرنه والړ دی چې څلور برخې یو له بل څخه خپلواکې دي. دا په ندرت کارول کېږي ځکه چې د راتلونکو پېښو لپاره مناسب نه دی.')
head(s,'h614','6.1.4 Measurement of secular trend','6.1.4 صدیوی رجحان کی پیمائش','6.1.4 د عمري تمایل اندازه کول')
add(s,'t614','There are four methods for measurement of secular trend:','صدیوی رجحان کی پیمائش کے چار طریقے ہیں:','د عمري تمایل د اندازه کولو څلور طریقې شته:')
L(s,[('m1','(i) Freehand curve or graphical method.','(i) آزاد دستی منحنی یا تصویری طریقہ۔','(i) د آزاد لاس منحني یا ګرافي طریقه.'),('m2','(ii) Semi-average method.','(ii) نیم اوسط کا طریقہ۔','(ii) د نیمه اوسط طریقه.'),('m3','(iii) Moving average method.','(iii) متحرک اوسط کا طریقہ۔','(iii) د خوځېدونکي اوسط طریقه.'),('m4','(iv) Least squares method.','(iv) کم از کم مربعات کا طریقہ۔','(iv) د لږ تر لږه مربعاتو طریقه.')],'secular-trend-methods')
add(s,'h5','(i) The freehand curve method:','(i) آزاد دستی منحنی کا طریقہ:','(i) د آزاد لاس منحني طریقه:')
add(s,'t6','According to this method, the data are plotted on a graph paper taking the time units (e.g. years, months etc.) on x-axis and observations on the y-axis. The plotted points are joined by a freehand smooth curve or segments of straight line in such a way that it shows a general tendency of the values.','اس طریقے کے مطابق اعداد و شمار کو گراف پیپر پر بنایا جاتا ہے جس میں وقت کی اکائیاں (مثلاً سال، مہینے وغیرہ) x-محور پر اور مشاہدات y-محور پر لیے جاتے ہیں۔ بنائے گئے نقاط کو آزاد دستی ہموار منحنی یا سیدھی لکیر کے حصوں سے اس طرح ملایا جاتا ہے کہ وہ قدروں کا عمومی رجحان ظاہر کرے۔','د دې طریقې له مخې معلومات په ګراف کاغذ رسمېږي چې د وخت واحدونه (لکه کلونه، میاشتې او نور) په x-محور او کتنې په y-محور اخیستل کېږي. رسم شوې نقطې د آزاد لاس هواره منحني یا د مستقیمې کرښې برخو په واسطه داسې سره نښلول کېږي چې د ارزښتونو عمومي تمایل وښيي.')
s['equations']+=[eqn(208,'mm',r'y_t=T\times S\times C\times I','y_t = T × S × C × I'),eqn(208,'am',r'y_t=T+S+C+I','y_t = T + S + C + I')]
P=lambda *ks:dict(type='paragraphs',ids=[pid(208,k) for k in ks])
s['flow']=[P('h612','t612','h613','t613','h1','t1'),dict(type='equation',index=0),P('h2','t2'),dict(type='equation',index=1),P('h614','t614','m1','m2','m3','m4','h5','t6')]
s['sourceNote']='Printed page 198. The two model formulas are printed inline inside their sentences and are repeated as equations after them. Printed spellings kept: "rarely used". Header graphics and watermark excluded.'
s['vocabulary']={'multiplicative model':dict(ur='ضربی ماڈل',ps='ضربي ماډل'),'additive model':dict(ur='جمعی ماڈل',ps='جمعي ماډل')}
save(s)
# ---------- scan 209 (printed 199) ----------
s=page(209,U,'199','Example 6.1: freehand trend · Merits and demerits · (ii) Method of semi-average (start)','مثال 6.1: آزاد دستی رجحان · خوبیاں اور خامیاں · (ii) نیم اوسط کا طریقہ (آغاز)','بېلګه 6.1: آزاد لاس تمایل · ګټې او زیانونه · (ii) د نیمه اوسط طریقه (پیل)','ts-freehand-1')
Flow(s)
head(s,'ex61','Example: 6.1','مثال: 6.1','بېلګه: 6.1',exampleId=E61)
add(s,'q61','Draw a freehand trend for the following data on a graph paper.','درج ذیل اعداد و شمار کا آزاد دستی رجحان گراف پیپر پر بنائیں۔','د لاندې معلوماتو آزاد لاس تمایل په ګراف کاغذ رسم کړئ.',role='question',exampleId=E61)
head(s,'sol61','Solution:','حل:','حل:',exampleId=E61)
add(s,'a1','Draw the axes and plot the data by taking years on the x-axis and values on the y-axis as follows;','محور بنائیں اور اعداد و شمار کو بنائیں جس میں سال x-محور پر اور قدریں y-محور پر لی جائیں جیسا کہ درج ذیل ہے؛','محورونه رسم کړئ او معلومات رسم کړئ چې کلونه په x-محور او ارزښتونه په y-محور اخیستل کېږي لکه لاندې؛',role='solution',exampleId=E61)
add(s,'mh','Merits','خوبیاں','ګټې')
L(s,[('m1','(i) This method is very easy.','(i) یہ طریقہ بہت آسان ہے۔','(i) دا طریقه ډېره اسانه ده.'),('m2','(ii) It saves time because looking at a graph is easier than the complex mathematical calculations.','(ii) یہ وقت بچاتا ہے کیونکہ گراف کو دیکھنا پیچیدہ ریاضیاتی حسابات سے آسان ہے۔','(ii) دا وخت ژغوري ځکه چې ګراف لیدل له پیچلو ریاضیاتي محاسبو څخه اسانه دي.')],'freehand-merits')
add(s,'dh','Demerits','خامیاں','زیانونه')
L(s,[('d1','(i) Different persons will draw different trend lines for the same data.','(i) مختلف لوگ ایک ہی اعداد و شمار کے لیے مختلف رجحان کی لکیریں بنائیں گے۔','(i) بېلابېل کسان به د یو شان معلوماتو لپاره بېلابېلې د تمایل کرښې رسم کړي.'),('d2','(ii) Considerable practice of drawing a curve is required.','(ii) منحنی بنانے کی خاصی مشق درکار ہے۔','(ii) د منحني د رسمولو ښه تمرین اړین دی.'),('d3','(iii) It depends on the judgment of the investigator or the scientist.','(iii) یہ تحقیق کرنے والے یا سائنسدان کے فیصلے پر منحصر ہے۔','(iii) دا د څېړونکي یا ساینس‌پوه په قضاوت پورې اړه لري.')],'freehand-demerits')
add(s,'h2','(ii) The method of semi-average','(ii) نیم اوسط کا طریقہ','(ii) د نیمه اوسط طریقه')
add(s,'t2','In this method, the data is divided into two equal parts. If the number of years in a series is odd, the middle year is excluded at the time of dividing the series in to two equal parts. Then the average of each part is computed and placed against the centre of each part. The average values are plotted on the graph paper against the midpoints. The line joining these two plotted points gives trend line. The direction of line indicates about rising, falling or constant trend of business','اس طریقے میں اعداد و شمار کو دو برابر حصوں میں تقسیم کیا جاتا ہے۔ اگر سلسلے میں سالوں کی تعداد طاق ہو تو سلسلے کو دو برابر حصوں میں تقسیم کرتے وقت درمیانی سال کو خارج کر دیا جاتا ہے۔ پھر ہر حصے کا اوسط حساب کیا جاتا ہے اور ہر حصے کے مرکز کے سامنے رکھا جاتا ہے۔ اوسط قدروں کو گراف پیپر پر وسطی نقطوں کے سامنے بنایا جاتا ہے۔ ان دو بنائے گئے نقاط کو ملانے والی لکیر رجحان کی لکیر دیتی ہے۔ لکیر کی سمت کاروبار کے بڑھتے، گھٹتے یا مستقل رجحان کے بارے میں بتاتی ہے','پدې طریقه کې معلومات په دوو مساوي برخو وېشل کېږي. که په لړۍ کې د کلونو شمېر طاق وي نو لړۍ ته په دوو مساوي برخو د ویشلو پر مهال منځنی کال وځي. بیا د هرې برخې اوسط محاسبه کېږي او د هرې برخې د مرکز په مقابل کې ایښودل کېږي. اوسط ارزښتونه په ګراف کاغذ د منځنیو نقطو په مقابل کې رسمېږي. دا دوه رسم شوې نقطې نښلوونکې کرښه د تمایل کرښه ورکوي. د کرښې لوری د سوداګرۍ د لوړېدونکي، ښکته کېدونکي یا ثابت تمایل په اړه وايي',sourceGap=dict(note='The sentence continues on the next page.'))
s['tables']=[table('Example 6.1: years and values','مثال 6.1: سال اور قدریں','بېلګه 6.1: کلونه او ارزښتونه',[c('Year:','سال:','کال:')]+[c(str(v)) for v in range(2000,2008)],[row('Values:','قدریں:','ارزښتونه:',[12,14,10,16,18,16,20,18])],exampleId=E61)]
s['figures']=[dict(id='stat11-s209-fig1',svg=trendfig(),caption='Graph showing the trend (Example 6.1)',captionUrdu='رجحان دکھانے والا گراف (مثال 6.1)',captionPashto='د تمایل ښودونکی ګراف (بېلګه 6.1)',labels=[lab('y-axis','y-محور','y-محور'),lab('x-axis','x-محور','x-محور')],sourceGap=dict(note='Redrawn as a coded graph from the printed data pairs; the scale note "6.S.S = 1 on x-axis, 1.S.S = 1 on y-axis" is kept in the figure.'))]
P=lambda *ks:dict(type='paragraphs',ids=[pid(209,k) for k in ks])
s['flow']=[P('ex61','q61'),dict(type='table',index=0),P('sol61','a1'),dict(type='figure',index=0),P('mh','m1','m2','dh','d1','d2','d3','h2','t2')]
s['sourceNote']='Printed page 199. The year labels on the x-axis are printed vertically (one digit per line). Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 210 (printed 200) ----------
s=page(210,U,'200','Example 6.2: semi-average trend (a)','مثال 6.2: نیم اوسط رجحان (الف)','بېلګه 6.2: د نیمه اوسط تمایل (a)','ts-semi-1')
Flow(s)
head(s,'ex62','Example: 6.2','مثال: 6.2','بېلګه: 6.2',exampleId=E62)
add(s,'q62','Draw the trend by the method of semi-average from the following data.','درج ذیل اعداد و شمار سے نیم اوسط کے طریقے سے رجحان بنائیں۔','له لاندې معلوماتو څخه د نیمه اوسط په طریقه تمایل رسم کړئ.',role='question',exampleId=E62)
add(s,'qa','(a)','(الف)','(a)',role='question',exampleId=E62)
add(s,'qb','(b)','(ب)','(b)',role='question',exampleId=E62)
head(s,'sol62','Solution:','حل:','حل:',exampleId=E62)
add(s,'a1','(a) Here the number of years is even, the data is divided in to two equal parts, each having four observations. Simple average of each part is computed and is written at the middle of the group. These averages are plotted on the graph paper. Then a line is drawn crossing these two points, which is the required semi-average trend line.','(الف) یہاں سالوں کی تعداد جفت ہے، اعداد و شمار کو دو برابر حصوں میں تقسیم کیا گیا ہے، ہر ایک میں چار مشاہدات ہیں۔ ہر حصے کا سادہ اوسط حساب کیا جاتا ہے اور گروہ کے درمیان لکھا جاتا ہے۔ ان اوسطوں کو گراف پیپر پر بنایا جاتا ہے۔ پھر ان دو نقاط سے گزرتی ہوئی لکیر کھینچی جاتی ہے، جو مطلوبہ نیم اوسط رجحان کی لکیر ہے۔','(a) دلته د کلونو شمېر جفت دی، معلومات په دوو مساوي برخو ویشل شوي، هره یوه څلور کتنې لري. د هرې برخې ساده اوسط محاسبه کېږي او د ډلې په منځ کې لیکل کېږي. دا اوسطونه په ګراف کاغذ رسمېږي. بیا دا دوه نقطې تېروونکې کرښه ایستل کېږي، چې اړینه د نیمه اوسط د تمایل کرښه ده.',role='solution',exampleId=E62)
s['tables']=[table('Example 6.2 (a): year and values','مثال 6.2 (الف): سال اور قدریں','بېلګه 6.2 (a): کال او ارزښتونه',[c('Year','سال','کال')]+[c(str(v)) for v in range(1980,1988)],[row('Values','قدریں','ارزښتونه',[97,85,100,90,105,83,112,120])],exampleId=E62),
 table('Example 6.2 (b): year and values','مثال 6.2 (ب): سال اور قدریں','بېلګه 6.2 (b): کال او ارزښتونه',[c('Year','سال','کال')]+[c(str(v)) for v in range(1976,1985)],[row('Values','قدریں','ارزښتونه',[286,260,276,270,302,348,351,321,346])],exampleId=E62),
 table('Example 6.2 (a) solution: values and averages','مثال 6.2 (الف) کا حل: قدریں اور اوسط','د بېلګې 6.2 (a) حل: ارزښتونه او اوسطونه',[c('Year','سال','کال'),c('Values','قدریں','ارزښتونه'),c('Averages','اوسط','اوسطونه')],[[c('1980'),c('97'),c('')],[c('1981'),c('85'),c('372 ÷ 4 = 93')],[c('1982'),c('100'),c('')],[c('1983'),c('90'),c('')],[c('1984'),c('105'),c('')],[c('1985'),c('83'),c('420 ÷ 4 = 105')],[c('1986'),c('112'),c('')],[c('1987'),c('120'),c('')]],exampleId=E62)]
s['figures']=[dict(id='stat11-s210-fig1',svg=semifig(),caption='Graph showing semi-average trend (Example 6.2 (a))',captionUrdu='نیم اوسط رجحان دکھانے والا گراف (مثال 6.2 (الف))',captionPashto='د نیمه اوسط د تمایل ښودونکی ګراف (بېلګه 6.2 (a))',labels=[lab('y-axis','y-محور','y-محور'),lab('x-axis','x-محور','x-محور')],sourceGap=dict(note='Redrawn as a coded graph: the two semi-average points are at the mid-years 1981.5 and 1985.5 with values 93 and 105.'))]
P=lambda *ks:dict(type='paragraphs',ids=[pid(210,k) for k in ks])
s['flow']=[P('ex62','q62','qa'),dict(type='table',index=0),P('qb'),dict(type='table',index=1),P('sol62','a1'),dict(type='table',index=2),dict(type='figure',index=0)]
s['sourceNote']='Printed page 200. In the solution table the averages 93 and 105 are printed beside brackets that group the first four and last four years; they are placed on the second and sixth rows. Header graphics and watermark excluded.'
s['vocabulary']={'semi-average':dict(ur='نیم اوسط',ps='نیمه اوسط')}
save(s)
