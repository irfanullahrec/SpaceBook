from statlib import *
import math
c=cell
U='collection-presentation'
def pid(n,k): return f'stat11-s{n:03}-{k}'
FILLS=['#cfd8dc','#90a4ae','#b0bec5','#607d8b','#455a64','#eceff1']
def rects():
    fams=[('A',[60,10,10,7.5,5,7.5],60),('B',[50,11.66,13.34,5,8.34,11.66],130),('C',[36,14,16,4.8,16,13.2],230)]
    names=['Food','Clothing','Education','Fuel and lighting','House rent','Misc']
    X0,Y0,H=70,40,300
    Y=lambda v:Y0+H*(1-v/100)
    o=T(230,20,'Sub divided rectangular diagram',13,'middle',600)
    o+=T(40,Y0-8,'y-axis',11,'start')+T(430,Y0+H+4,'x-axis',11,'start')
    for t in range(0,101,10): o+=T(X0-8,Y(t)+4,str(t),11,'end')+f'<line x1="{X0-4}" y1="{Y(t):.1f}" x2="{X0}" y2="{Y(t):.1f}" stroke="#333"/>'
    o+=f'<line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y0+H}" stroke="#333"/><line x1="{X0}" y1="{Y0+H}" x2="420" y2="{Y0+H}" stroke="#333"/>'
    for (nm,vals,w),x in zip(fams,(90,190,290)):
        base=0
        for j,v in enumerate(vals):
            o+=f'<rect x="{x}" y="{Y(base+v):.1f}" width="{w*0.7:.1f}" height="{Y(base)-Y(base+v):.1f}" fill="{FILLS[j]}" stroke="#222"/>';base+=v
        o+=T(x+w*0.35,Y0+H+18,nm,12,'middle',600)
    o+=T(460,70,'Key',12,'start',600)
    for j,nm in enumerate(names): o+=f'<rect x="460" y="{82+j*24}" width="16" height="14" fill="{FILLS[j]}" stroke="#222"/>'+T(482,94+j*24,nm,11,'start')
    return svg(580,380,'Percentage subdivided rectangles for families A, B and C showing food, clothing, education, fuel and lighting, house rent and miscellaneous',o)
def pie():
    data=[('Africa',81.8),('Asia',72.7),('Europe',13.3),('North America',65.7),('Antarctica',23.1),('South America',48.2),('Russia',55.2)]
    cx,cy,r=170,160,120
    o=T(170,16,'Pie chart showing area of continents',13,'middle',600)+f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="#1c5a8a" stroke-width="2"/>'
    a=0;
    for i,(nm,ang) in enumerate(data):
        t=math.radians(a);x=cx+r*math.cos(t);y=cy-r*math.sin(t)
        o+=f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#1c5a8a" stroke-width="1.5"/>'
        m=math.radians(a+ang/2);lx=cx+r*0.62*math.cos(m);ly=cy-r*0.62*math.sin(m)
        sz=12 if ang>30 else 10
        o+=T(lx,ly+4,nm.split()[0] if ang<=30 else nm.replace(' America',''),sz,'middle')
        if nm.endswith('America'): o+=T(lx,ly+18,'America',sz,'middle')
        a+=ang
    return svg(340,300,'Pie chart of continent areas: Africa 81.8, Asia 72.7, Europe 13.3, North America 65.7, Antarctica 23.1, South America 48.2, Russia 55.2 degrees',o)
# ---------- scan 35 (printed 27) ----------
s=page(35,U,'27','1.5.17 The percentage subdivided rectangles · Example 1.10','1.5.17 فیصد ذیلی منقسم مستطیلیں · مثال 1.10','1.5.17 سلنه فرعي ویشل شوي مستطیلونه · بېلګه 1.10','subdivided-rect-1')
head(s,'h17','1.5.17 The percentage subdivided rectangles','1.5.17 فیصد ذیلی منقسم مستطیلیں','1.5.17 سلنه فرعي ویشل شوي مستطیلونه')
add(s,'t1','In the presentation of data by rectangles both length and width of the rectangles are used. Subdivided rectangles are constructed for the data where the quantities along with their components are to be compared. These diagrams are mostly used to compare the budgets of various families.','مستطیلوں کے ذریعے اعداد و شمار کی پیشکش میں مستطیلوں کی لمبائی اور چوڑائی دونوں استعمال ہوتی ہیں۔ ذیلی منقسم مستطیلیں ان اعداد و شمار کے لیے بنائی جاتی ہیں جہاں مقداروں کا ان کے اجزا کے ساتھ موازنہ کرنا ہو۔ یہ خاکے زیادہ تر مختلف خاندانوں کے بجٹ کا موازنہ کرنے کے لیے استعمال ہوتے ہیں۔','د مستطیلونو په واسطه د معلوماتو په وړاندې کولو کې د مستطیلونو اوږدوالی او پلنوالی دواړه کارول کېږي. فرعي ویشل شوي مستطیلونه د هغو معلوماتو لپاره جوړېږي چېرته چې کچې د هغو له اجزاو سره پرتله کول وي. دا ډیاګرامونه ډېر د بېلابېلو کورنیو د بودیجې د پرتلې لپاره کارول کېږي.')
add(s,'t2','To construct subdivided rectangles first fix the length of the rectangles equal to 100% and their widths are kept proportional to the size of the total figures. The rectangles are subdivided according to the length of the various components. To make the partitioning process easy, it is suggested to compute cumulative percentages for the data.','ذیلی منقسم مستطیلیں بنانے کے لیے پہلے مستطیلوں کی لمبائی 100% کے برابر مقرر کریں اور ان کی چوڑائیاں کل اعداد کی مقدار کے متناسب رکھی جاتی ہیں۔ مستطیلوں کو مختلف اجزا کی لمبائی کے مطابق ذیلی تقسیم کیا جاتا ہے۔ تقسیم کے عمل کو آسان بنانے کے لیے تجویز کیا جاتا ہے کہ اعداد و شمار کے جمعی فیصد حساب کیے جائیں۔','د فرعي ویشل شویو مستطیلونو د جوړولو لپاره لومړی د مستطیلونو اوږدوالی له 100% سره مساوي ټاکئ او د هغو پلنوالی د ټولو شمېرو د کچې په تناسب ساتل کېږي. مستطیلونه د بېلابېلو اجزاو د اوږدوالي سره سم فرعي وېشل کېږي. د وېش بهیر د اسانه کولو لپاره وړاندیز کېږي چې د معلوماتو مجموعي سلنې محاسبه شي.')
head(s,'ex','Example: 1.10','مثال: 1.10','بېلګه: 1.10',exampleId='stat11-ex-1-10')
R=[('Food','خوراک','خواړه','24','60','180'),('Clothing','لباس','جامې','4','14','70'),('Education','تعلیم','زده‌کړه','4','16','80'),('Fuel and lighting','ایندھن اور روشنی','سونګ او رڼا','3','6','24'),('House rent','مکان کا کرایہ','د کور کرايه','2','10','80'),('Miscellaneous','متفرق','متفرقه','3','14','66')]
s['tables']=[table('Monthly expenditures (in Rs.) of three families','تین خاندانوں کے ماہانہ اخراجات (روپوں میں)','د دریو کورنیو میاشتني لګښتونه (په روپیو)',[c('Items of expenditure','اخراجات کی مدات','د لګښت توکي'),c('Family A','خاندان A','کورنۍ A'),c('Family B','خاندان B','کورنۍ B'),c('Family C','خاندان C','کورنۍ C')],[[c(a,b,d),c(e),c(f),c(g)] for a,b,d,e,f,g in R],exampleId='stat11-ex-1-10')]
add(s,'q','The following table gives the details of monthly expenditures (in Rs.) of three families.','درج ذیل جدول تین خاندانوں کے ماہانہ اخراجات (روپوں میں) کی تفصیل دیتا ہے۔','لاندې جدول د دریو کورنیو د میاشتنیو لګښتونو (په روپیو) تفصیل ورکوي.',role='question',exampleId='stat11-ex-1-10')
add(s,'q2','Represent the above data by subdivided rectangles.','مندرجہ بالا اعداد و شمار کو ذیلی منقسم مستطیلوں سے ظاہر کریں۔','پورتني معلومات د فرعي ویشل شویو مستطیلونو په واسطه وښیئ.',role='question',exampleId='stat11-ex-1-10')
head(s,'sol','Solution:','حل:','حل:',exampleId='stat11-ex-1-10')
add(s,'s1','To construct subdivided rectangles, the percentages and the cumulative percentages of expenditure in respect of three families are expressed as under;','ذیلی منقسم مستطیلیں بنانے کے لیے تین خاندانوں کے اخراجات کے فیصد اور جمعی فیصد درج ذیل کی طرح ظاہر کیے گئے ہیں؛','د فرعي ویشل شویو مستطیلونو د جوړولو لپاره د دریو کورنیو د لګښتونو سلنې او مجموعي سلنې په لاندې ډول ښودل شوې؛',role='solution',exampleId='stat11-ex-1-10',sourceGap=dict(note='The table announced by this sentence is on the next page.'))
ids=[p['id'] for p in s['paras']];a=ids.index(pid(35,'ex'))+1
s['flow']=[dict(type='paragraphs',ids=ids[:a]),dict(type='table',index=0),dict(type='paragraphs',ids=ids[a:])]
s['sourceNote']='Printed page 27. In the printed table "Families" spans the A, B, C columns (given here as Family A/B/C). Header graphics and watermark excluded.'
s['vocabulary']={'rectangles':dict(ur='مستطیلیں',ps='مستطیلونه')}
save(s)
# ---------- scan 36 (printed 28) ----------
s=page(36,U,'28','Example 1.10 solution table and diagram · 1.5.18 Pie diagram','مثال 1.10 کا حل: جدول اور خاکہ · 1.5.18 پائی خاکہ','د بېلګې 1.10 حل: جدول او ډیاګرام · 1.5.18 پای ډیاګرام','subdivided-rect-2')
H1=[c('Items of expenditure','اخراجات کی مدات','د لګښت توکي')]
for f in 'ABC': H1+=[c(f'{f}: Actual expenditure',f'{f}: اصل اخراجات',f'{f}: واقعي لګښت'),c(f'{f}: % age',f'{f}: فیصد',f'{f}: سلنه'),c(f'{f}: Cumulative % age',f'{f}: جمعی فیصد',f'{f}: مجموعي سلنه')]
R=[('Food','خوراک','خواړه',['24','60','60','60','50','50','180','36','36']),('Clothing','لباس','جامې',['4','10','70','14','11.66','61.66','70','14','50']),('Education','تعلیم','زده‌کړه',['4','10','80','16','13.34','75','80','16','66']),('Fuel & lighting','ایندھن اور روشنی','سونګ او رڼا',['3','7.5','87.5','6','5','80','24','4.8','70.8']),('House rent','مکان کا کرایہ','د کور کرايه',['2','5','92.5','10','8.34','88.34','80','16','86.8']),('Miscellaneous','متفرق','متفرقه',['3','7.5','100','14','11.66','100','66','13.2','100'])]
s['tables']=[table('Percentages and cumulative percentages of expenditure of families A, B and C','خاندانوں A، B اور C کے اخراجات کے فیصد اور جمعی فیصد','د کورنیو A، B او C د لګښتونو سلنې او مجموعي سلنې',H1,[[c(a,b,d)]+[c(x) for x in v] for a,b,d,v in R]+[[c('Total','کل','ټول'),c('40'),c('100'),c('-'),c('120'),c('100'),c('-'),c('500'),c('100'),c('-')]],role='solution')]
s['figures']=[dict(id='stat11-s036-fig1',svg=rects(),caption='Sub divided rectangular diagram',captionUrdu='ذیلی منقسم مستطیلی خاکہ',captionPashto='فرعي ویشل شوی مستطیلي ډیاګرام',labels=[lab('Key','کلید','کلیدي'),lab('Food','خوراک','خواړه'),lab('Clothing','لباس','جامې'),lab('Education','تعلیم','زده‌کړه'),lab('Fuel and lighting','ایندھن اور روشنی','سونګ او رڼا'),lab('House rent','مکان کا کرایہ','د کور کرايه'),lab('Misc','متفرق','متفرقه')],sourceGap=dict(note='Redrawn as coded SVG from the table percentages; the printed hatch patterns are replaced by grey fills, and the printed legend word "Eductain" (Education) is given as Education.'))]
head(s,'h18','1.5.18 Pie diagram','1.5.18 پائی خاکہ','1.5.18 پای ډیاګرام')
add(s,'t18','Pie diagram is a device consisting of a circle divided into sectors. It is also called sector diagram or sub-divided circle. It is an alternative to a component bar diagram. The name pie diagram is given to a circle diagram because in determining the circumference of circle we have to take in to consideration a','پائی خاکہ ایک ایسا آلہ ہے جو دائرے کو قطاعوں میں تقسیم کر کے بنایا جاتا ہے۔ اسے قطاعی خاکہ یا ذیلی منقسم دائرہ بھی کہتے ہیں۔ یہ جزوی بار خاکے کا متبادل ہے۔ دائرے کے خاکے کو پائی خاکہ اس لیے کہا جاتا ہے کہ دائرے کا محیط معلوم کرنے میں ہمیں ایک','پای ډیاګرام یوه وسیله ده چې له یوې دایرې جوړه ده چې په سکتورونو وېشل شوې وي. دې ته سکتور ډیاګرام یا فرعي ویشل شوې دایره هم ویل کېږي. دا د جزوي بار ډیاګرام بدیل دی. د دایرې ډیاګرام ته پای ډیاګرام ځکه ویل کېږي چې د دایرې د محیط په ټاکلو کې موږ باید یو',sourceGap=dict(note='The sentence continues on the next page ("quantity known as pie (written as π)…").'))
ids=[p['id'] for p in s['paras']]
s['flow']=[dict(type='table',index=0),dict(type='figure',index=0),dict(type='paragraphs',ids=ids)]
s['sourceNote']='Printed page 28. The two-level table header (Families → A, B, C → Actual expenditure / % age / Cumulative % age) is flattened to nine labelled columns. Values are as printed (including 11.66, 13.34, 8.34 and the "-" totals). A thumb is visible at the top-left of the scan and a handwritten loop at the foot; both ignored. Header graphics and watermark excluded.'
s['vocabulary']={'pie diagram':dict(ur='پائی خاکہ',ps='پای ډیاګرام')}
save(s)
# ---------- scan 37 (printed 29) ----------
s=page(37,U,'29','Pie diagram (continued) · Example 1.11','پائی خاکہ (جاری) · مثال 1.11','پای ډیاګرام (دوام) · بېلګه 1.11','pie-example')
add(s,'c1','quantity known as pie (written as π) that is area of a circle is known to cover 2π radian or 360°.','مقدار جسے پائی (جو π لکھا جاتا ہے) کہتے ہیں، یعنی دائرے کا رقبہ، جو 2π ریڈین یا 360° کا احاطہ کرتا ہے۔','کچه چې پای بلل کېږي (په π لیکل کېږي) یعنې د دایرې ساحه چې 2π رادیان یا 360° پوښي.',sourceGap=dict(note='Completes the sentence from the previous page: "…we have to take in to consideration a quantity known as pie…".'))
add(s,'c2','To construct a pie chart compute angle for each sector by the formula','پائی چارٹ بنانے کے لیے ہر قطاع کا زاویہ درج ذیل فارمولے سے حساب کریں','د پای چارټ د جوړولو لپاره د هر سکتور زاویه د لاندې فورمول په واسطه محاسبه کړئ')
add(s,'c3','Draw a radius and find different sectors by means of a protractor. The sectors are colored or shaded differently to show the relationship of parts to the whole.','ایک رداس کھینچیں اور چاندے (پروٹریکٹر) کی مدد سے مختلف قطاع معلوم کریں۔ حصوں کے کل سے تعلق کو ظاہر کرنے کے لیے قطاعوں کو مختلف رنگوں یا سایوں سے ظاہر کیا جاتا ہے۔','یو شعاع رسم کړئ او د زاویه‌پیما په مرسته بېلابېل سکتورونه ومومئ. د برخو له ټول سره اړیکه ښودلو لپاره سکتورونه په بېلابېلو رنګونو یا سیوري ښودل کېږي.')
head(s,'ex','Example: 1.11','مثال: 1.11','بېلګه: 1.11',exampleId='stat11-ex-1-11')
add(s,'q','The following table shows the areas of various continents/countries of the world, given in million square miles.','درج ذیل جدول دنیا کے مختلف براعظموں/ممالک کے رقبے دکھاتا ہے، جو ملین مربع میل میں دیے گئے ہیں۔','لاندې جدول د نړۍ د بېلابېلو وچو/هېوادونو ساحې ښيي چې په ملیون مربع مایل کې ورکړل شوې.',role='question',exampleId='stat11-ex-1-11')
add(s,'q2','Prepare a pie chart of the above table.','مندرجہ بالا جدول کا پائی چارٹ تیار کریں۔','د پورتني جدول پای چارټ جوړ کړئ.',role='question',exampleId='stat11-ex-1-11')
head(s,'sol','Solution:','حل:','حل:',exampleId='stat11-ex-1-11')
add(s,'s1','The necessary calculations for construction of a pie diagram are given in the following table.','پائی خاکہ بنانے کے لیے ضروری حسابات درج ذیل جدول میں دیے گئے ہیں۔','د پای ډیاګرام د جوړولو لپاره اړین محاسبې په لاندې جدول کې ورکړل شوې.',role='solution',exampleId='stat11-ex-1-11')
CT=[('Africa','افریقہ','افریقا','11.7'),('Asia','ایشیا','آسیا','10.4'),('Europe','یورپ','اروپا','1.9'),('North America','شمالی امریکہ','شمالي امریکا','9.4'),('Antarctica','انٹارکٹیکا','انټارکتیکا','3.3'),('South America','جنوبی امریکہ','سویلي امریکا','6.9'),('Russia','روس','روسیه','7.9')]
s['tables']=[table('Areas of continents/countries (million square miles)','براعظموں/ممالک کے رقبے (ملین مربع میل)','د وچو/هېوادونو ساحې (ملیون مربع مایل)',[c('Continents/Countries','براعظم/ممالک','وچې/هېوادونه'),c('Area (million square miles)','رقبہ (ملین مربع میل)','ساحه (ملیون مربع مایل)')],[[c(a,b,d),c(e)] for a,b,d,e in CT],exampleId='stat11-ex-1-11'),
 table('Calculations for the pie diagram','پائی خاکے کے حسابات','د پای ډیاګرام محاسبې',[c('Continents/countries','براعظم/ممالک','وچې/هېوادونه'),c('Area (in million sq. miles)','رقبہ (ملین مربع میل)','ساحه (ملیون مربع مایل)'),c('Angle of the sector','قطاع کا زاویہ','د سکتور زاویه'),c('Cumulative angle of the sector','قطاع کا جمعی زاویہ','د سکتور مجموعي زاویه')],[[c('Africa','افریقہ','افریقا'),c('11.7'),c('11.7/51.5×360 = 81.8°'),c('81.8°')],[c('Asia','ایشیا','آسیا'),c('10.4'),c('10.4/51.5×360 =72.7°'),c('154.5°')],[c('Europe','یورپ','اروپا'),c('1.9'),c('= 13.3°'),c('167.8°')],[c('North America','شمالی امریکہ','شمالي امریکا'),c('9.4'),c('= 65.7°'),c('233.5°')],[c('Antarctica','انٹارکٹیکا','انټارکتیکا'),c('3.3'),c('=23.1°'),c('256.6°')],[c('South America','جنوبی امریکہ','سویلي امریکا'),c('6.9'),c('= 48.2°'),c('304.8°')],[c('Russia','روس','روسیه'),c('7.9'),c('= 55.2°'),c('360°')],[c('Total','کل','ټول'),c('51.5'),c('360°'),c('–')]],exampleId='stat11-ex-1-11',role='solution')]
s['equations']=[eqn(37,'ang',r'\text{Angle}=\dfrac{\text{component}}{\text{total}}\times360^\circ','Angle = (component / total) × 360°')]
ids=[p['id'] for p in s['paras']]
s['flow']=[dict(type='paragraphs',ids=ids[:2]),dict(type='equation',index=0),dict(type='paragraphs',ids=ids[2:6]),dict(type='table',index=0),dict(type='paragraphs',ids=ids[6:]),dict(type='table',index=1)]
s['sourceNote']='Printed page 29. Handwritten Urdu words beside the first table, the pencil word above it, small marks under the totals and a stroke below "51.5" are ignored. Pie angles are as printed: the first row prints "81.8°" with a stray pen mark. Header graphics and watermark excluded.'
s['vocabulary']={'protractor':dict(ur='چاندا (پروٹریکٹر)',ps='زاویه‌پیما'),'sector':dict(ur='قطاع',ps='سکتور')}
save(s)
# ---------- scan 38 (printed 30) ----------
s=page(38,U,'30','Pie chart · 1.5.19 Graphs · 1.5.20 Types of graphs','پائی چارٹ · 1.5.19 گراف · 1.5.20 گرافوں کی اقسام','پای چارټ · 1.5.19 ګرافونه · 1.5.20 د ګرافونو ډولونه','pie-graphs')
add(s,'c1','Now draw a circle of any reasonable size and divide it in to sectors according to the cumulative angles as follows;','اب کسی بھی مناسب سائز کا دائرہ بنائیں اور اسے جمعی زاویوں کے مطابق قطاعوں میں تقسیم کریں جیسا کہ درج ذیل ہے؛','اوس د هرې مناسبې کچې دایره رسم کړئ او هغه د مجموعي زاویو سره سم په سکتورونو وېشئ لکه څنګه چې لاندې ده؛')
head(s,'h19','1.5.19 Graphs','1.5.19 گراف','1.5.19 ګرافونه')
add(s,'t19','No doubt that diagrams are fairly good devices to compare two or more quantities but they do not study their relationship. For this purpose graphs come to help. A graph is a pictorial presentation of the relationship between the variables. It gives more accurate and precise results than diagrams.','بلا شبہ خاکے دو یا زیادہ مقداروں کا موازنہ کرنے کے لیے کافی اچھے آلات ہیں لیکن وہ ان کے باہمی تعلق کا مطالعہ نہیں کرتے۔ اس مقصد کے لیے گراف مدد کو آتے ہیں۔ گراف متغیرات کے درمیان تعلق کی تصویری پیشکش ہے۔ یہ خاکوں کے مقابلے میں زیادہ درست اور صحیح نتائج دیتا ہے۔','بې شکه ډیاګرامونه د دوو یا ډېرو کچو د پرتلې لپاره ښه وسایل دي خو دوی د هغو اړیکه نه څېړي. د دې موخې لپاره ګرافونه مرسته کوي. ګراف د متغیرونو ترمنځ د اړیکې انځوریز وړاندې کول دي. دا له ډیاګرامونو څخه ډېر دقیق او سم پایلې ورکوي.')
head(s,'hg','Guidelines for construction of graph','گراف بنانے کے رہنما اصول','د ګراف د جوړولو لارښوونې')
add(s,'tg','The following rules are helpful to make your graph attractive.','درج ذیل قواعد آپ کے گراف کو پرکشش بنانے میں مددگار ہیں۔','لاندې قواعد ستاسو ګراف په زړه پورې کولو کې ګټور دي.')
GL=[('i. A graph must have a title.','i. گراف کا ایک عنوان ہونا ضروری ہے۔','i. ګراف باید یو سرلیک ولري.'),('ii. Arrange the data and compute class boundaries and cumulative frequencies, whenever is needed.','ii. جب بھی ضرورت ہو اعداد و شمار کو ترتیب دیں اور جماعتی سرحدیں اور جمعی تعددات حساب کریں۔','ii. معلومات ترتیب کړئ او هر کله چې اړتیا وي د ټولګي پولې او مجموعي فریکونسۍ محاسبه کړئ.'),('iii. Use a graph paper and draw x-axis and y-axis.','iii. گراف پیپر استعمال کریں اور x-محور اور y-محور کھینچیں۔','iii. ګراف کاغذ وکاروئ او x-محور او y-محور رسم کړئ.'),('iv. Take independent variable that is time, classes etc. on x-axis and dependent variable that is frequencies, cumulative frequencies etc. on y-axis.','iv. آزاد متغیر یعنی وقت، جماعتیں وغیرہ x-محور پر اور تابع متغیر یعنی تعددات، جمعی تعددات وغیرہ y-محور پر لیں۔','iv. خپلواک متغیر یعنې وخت، ټولګي او نور په x-محور او تابع متغیر یعنې فریکونسۍ، مجموعي فریکونسۍ او نور په y-محور واخلئ.'),('v. Select a suitable scale and write it on the top of right hand side corner.','v. مناسب پیمانہ منتخب کریں اور اسے اوپر دائیں ہاتھ کے کونے میں لکھیں۔','v. مناسبه پیمانه وټاکئ او هغه په پورتنۍ ښي لاس کونج کې ولیکئ.'),('vi. Starting point on y-axis should always begin with zero.','vi. y-محور پر نقطۂ آغاز ہمیشہ صفر سے شروع ہونا چاہیے۔','vi. په y-محور د پیل نقطه باید تل له صفر سره پیل شي.'),('vii. Plot the original data and join the plotted points to get the required straight line or curve.','vii. اصل اعداد و شمار کو پلاٹ کریں اور پلاٹ کیے گئے نقاط کو ملا کر مطلوبہ سیدھی لکیر یا منحنی حاصل کریں۔','vii. اصلي معلومات پلاټ کړئ او پلاټ شوې نقطې سره وصل کړئ ترڅو مطلوبه سیده کرښه یا منحني ترلاسه شي.')]
for i,(a,b,d) in enumerate(GL,1): add(s,f'g{i}',a,b,d,listGroup='graph-rules')
head(s,'h20','1.5.20 Types of graphs','1.5.20 گرافوں کی اقسام','1.5.20 د ګرافونو ډولونه')
add(s,'t20','Graphs are generally divided into two main categories; (i) Graphs of time series that is historigram and (ii) Graphs of frequency distributions that is, histogram, frequency polygon, frequency curve and cumulative frequency polygon.','گراف عموماً دو بڑی اقسام میں تقسیم ہوتے ہیں؛ (i) وقتی سلسلے کے گراف یعنی ہسٹوریگرام اور (ii) تعدد تقسیمات کے گراف یعنی ہسٹوگرام، تعدد کثیر الاضلاع، تعدد منحنی اور جمعی تعدد کثیر الاضلاع۔','ګرافونه په عمومي ډول په دوو لویو کټګوریو وېشل کېږي؛ (i) د وخت لړۍ ګرافونه یعنې هیسټوریګرام او (ii) د فریکونسي ویشونو ګرافونه یعنې هیسټوګرام، فریکونسي څو‌ضلعي، فریکونسي منحني او مجموعي فریکونسي څو‌ضلعي.')
s['figures']=[dict(id='stat11-s038-fig1',svg=pie(),caption='Pie chart showing area of continents',captionUrdu='براعظموں کے رقبے کا پائی چارٹ',captionPashto='د وچو د ساحې پای چارټ',labels=[lab('Africa','افریقہ','افریقا'),lab('Asia','ایشیا','آسیا'),lab('Europe','یورپ','اروپا'),lab('North America','شمالی امریکہ','شمالي امریکا'),lab('Antarctica','انٹارکٹیکا','انټارکتیکا'),lab('South America','جنوبی امریکہ','سویلي امریکا'),lab('Russia','روس','روسیه')],sourceGap=dict(note='Redrawn as coded SVG using the printed sector angles (counter-clockwise from the right-hand horizontal radius).'))]
ids=[p['id'] for p in s['paras']]
s['flow']=[dict(type='paragraphs',ids=ids[:1]),dict(type='figure',index=0),dict(type='paragraphs',ids=ids[1:])]
s['sourceNote']='Printed page 30. The printed item "historigram" is retained. Header graphics and watermark excluded.'
s['vocabulary']={'graph':dict(ur='گراف',ps='ګراف')}
save(s)
