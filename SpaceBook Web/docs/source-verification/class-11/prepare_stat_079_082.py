from statlib import *
from statcharts import _axes
c=cell
U='central-tendency'
def pid(n,k): return f'stat11-s{n:03}-{k}'
def build(s,seq):
    """seq: list of ('p',[keys]) / ('e',key) / ('t',idx) / ('f',idx); paragraphs referenced by key; equations created from E dict."""
    pass
def qdg():
    W,H=600,360;Lm,R,Tp,B=70,130,40,70
    o,Y,pw,ph=_axes(W,H,Lm,R,Tp,B,0,100,[0,10,20,30,40,50,60,70,80,90,100],False,'Graphic Estimation of Quartiles, D and P')
    xs=[9.5,19.5,29.5,39.5,49.5,59.5,69.5];ys=[0,12,30,57,77,94,100]
    X=lambda v:Lm+pw*(v-4)/(75-4)
    o+='<polyline fill="none" stroke="#111" stroke-width="2" points="'+' '.join(f'{X(a):.1f},{Y(b):.1f}' for a,b in zip(xs,ys))+'"/>'
    for a,b in zip(xs,ys): o+=f'<path d="M{X(a)-4:.1f},{Y(b)-4:.1f} L{X(a)+4:.1f},{Y(b)+4:.1f} M{X(a)-4:.1f},{Y(b)+4:.1f} L{X(a)+4:.1f},{Y(b)-4:.1f}" stroke="#111" stroke-width="1.6"/>'+T(X(a),Tp+ph+16,str(a),11)
    for lvl,xv in [(25,27),(50,38),(75,49.5),(80,52),(70,48)]:
        o+=f'<line x1="{Lm}" y1="{Y(lvl):.1f}" x2="{X(xv):.1f}" y2="{Y(lvl):.1f}" stroke="#111"/><line x1="{X(xv):.1f}" y1="{Y(lvl):.1f}" x2="{X(xv):.1f}" y2="{Tp+ph}" stroke="#111"/>'
    o+=T(Lm+pw/2,H-12,'Class boundaries',12)+f'<text transform="translate(14 {Tp+ph/2}) rotate(-90)" font-size="11" text-anchor="middle" font-family="Arial">Cumulative frequencies</text>'
    o+=T(Lm+pw+20,Tp+30,'Scale',12,'start')+T(Lm+pw+20,Tp+46,'on x-axis 1.S.S=1',11,'start')+T(Lm+pw+20,Tp+60,'on y-axis 1.S.S=1',11,'start')
    return svg(W,H,'Cumulative frequency curve with horizontal guides at 25, 50, 75, 80 and 70 meeting the curve and vertical lines to the x-axis giving Q1 about 27, Q2 about 38, Q3 about 49.5, D8 about 52 and P70 about 48',o)
# ---------- scan 79 (printed 71) ----------
s=page(79,U,'71','Examples 2.17, 2.18 (setup)','مثالیں 2.17، 2.18 (آغاز)','بېلګې 2.17، 2.18 (پیل)','quantile-examples-1')
head(s,'ex17','Example: 2.17','مثال: 2.17','بېلګه: 2.17',exampleId='stat11-ex-2-17')
add(s,'q17','Find third quartile, seventh decile and twentieth percentile for the data 68, 50, 32, 21, 54, 38, 59, 66, and 44.','اعداد و شمار 68, 50, 32, 21, 54, 38, 59, 66 اور 44 کے لیے تیسری چوتھائی، ساتواں دسواں اور بیسواں فی صدکیہ معلوم کریں۔','د معلوماتو 68, 50, 32, 21, 54, 38, 59, 66 او 44 لپاره دریم څلورمه، اووم لسمه او شل‌مه سلمه ومومئ.',role='question',exampleId='stat11-ex-2-17')
head(s,'sol17','Solution:','حل:','حل:',exampleId='stat11-ex-2-17')
add(s,'a1','Rewrite the given data in the ascending order. x = 21, 32, 38, 44, 50, 54, 59, 66, 68. Here n = 9 is odd, therefore','دیے گئے اعداد و شمار کو صعودی ترتیب میں دوبارہ لکھیں۔ x = 21, 32, 38, 44, 50, 54, 59, 66, 68۔ یہاں n = 9 طاق ہے، لہٰذا','ورکړل شوي معلومات په پورته‌والي ترتیب بیا ولیکئ. x = 21, 32, 38, 44, 50, 54, 59, 66, 68. دلته n = 9 طاق دی، نو',role='solution',exampleId='stat11-ex-2-17')
add(s,'a2','Since 7.5 is not showing a serial number. In such cases we proceed as;','چونکہ 7.5 کوئی سلسلہ وار نمبر ظاہر نہیں کرتا۔ ایسی صورتوں میں ہم اس طرح آگے بڑھتے ہیں؛','ځکه چې 7.5 لړ شمېره نه ښيي. په داسې حالتونو کې موږ داسې مخکې ځو؛',role='solution',exampleId='stat11-ex-2-17')
add(s,'c2','Case-ii: Discrete series or grouped data','صورت-ii: منفصل سلسلہ یا گروہی اعداد و شمار','حالت-ii: منفصله لړۍ یا ګروپي معلومات')
head(s,'ex18','Example: 2.18','مثال: 2.18','بېلګه: 2.18',exampleId='stat11-ex-2-18')
add(s,'q18','Calculate Q₂, D₆, and P₂₅ for the distribution of the values of 140 fruits given in the following table.','درج ذیل جدول میں دی گئی 140 پھلوں کی قدروں کی تقسیم کے لیے Q₂، D₆ اور P₂₅ حساب کریں۔','د لاندې جدول کې ورکړل شویو د 140 مېوو د ارزښتونو د ویش لپاره Q₂، D₆ او P₂₅ محاسبه کړئ.',role='question',exampleId='stat11-ex-2-18')
head(s,'sol18','Solution:','حل:','حل:',exampleId='stat11-ex-2-18')
add(s,'a3','List the given data in increasing order along with frequencies;','دیے گئے اعداد و شمار کو تعددات کے ساتھ بڑھتی ترتیب میں فہرست کریں؛','ورکړل شوي معلومات له فریکونسیو سره په زیاتېدونکي ترتیب لیست کړئ؛',role='solution',exampleId='stat11-ex-2-18',sourceGap=dict(note='The table follows at the top of the next page.'))
s['tables']=[table('Example 2.18: values of 140 fruits','مثال 2.18: 140 پھلوں کی قدریں','بېلګه 2.18: د 140 مېوو ارزښتونه',[c('x:')]+[c(str(v)) for v in [30,25,10,36,50,44,40,55,60]],[[c('f:')]+[c(v) for v in ['14','8','03','18','22','23','27','17','08']]],exampleId='stat11-ex-2-18')]
s['equations']=[
 eqn(79,'q3',r'\text{(i)}\ Q_3=3\left(\dfrac{n+1}{4}\right)\text{th observation}=3\left(\dfrac{9+1}{4}\right)\text{th observation}=\dfrac{30}{4}=7.5\text{th observation}','(i) Q3 = 3((n + 1)/4)th observation = 3((9 + 1)/4)th observation = 30/4 = 7.5th observation',exampleId='stat11-ex-2-17'),
 eqn(79,'q3b',r'Q_3=7\text{th value}+0.5\,(8\text{th value}-7\text{th value})=59+0.5(66-59)=59+0.5(7)=59+3.5=62.5','Q3 = 7th value + 0.5 (8th value − 7th value) = 59 + 0.5(66 − 59) = 59 + 0.5(7) = 59 + 3.5 = 62.5',exampleId='stat11-ex-2-17'),
 eqn(79,'d7',r'\text{(ii)}\ D_7=7\left(\dfrac{n+1}{10}\right)\text{th observation}=7\left(\dfrac{9+1}{10}\right)\text{th observation}=7\text{th observation}=59','(ii) D7 = 7((n + 1)/10)th observation = 7((9 + 1)/10)th observation = 7th observation = 59',exampleId='stat11-ex-2-17'),
 eqn(79,'p20',r'\text{(iii)}\ P_{20}=20\left(\dfrac{n+1}{100}\right)\text{th value}=20\left(\dfrac{9+1}{100}\right)\text{th value}=2\text{nd value}=32','(iii) P20 = 20((n + 1)/100)th value = 20((9 + 1)/100)th value = 2nd value = 32',exampleId='stat11-ex-2-17')]
s['flow']=[dict(type='paragraphs',ids=[pid(79,k) for k in ('ex17','q17','sol17','a1')]),dict(type='equation',index=0),dict(type='paragraphs',ids=[pid(79,'a2')]),dict(type='equation',index=1),dict(type='equation',index=2),dict(type='equation',index=3),dict(type='paragraphs',ids=[pid(79,k) for k in ('c2','ex18','q18')]),dict(type='table',index=0),dict(type='paragraphs',ids=[pid(79,'sol18'),pid(79,'a3')])]
s['sourceNote']='Printed page 71. In the printed working "(ii) D7" and "(iii) P20" the bracketed fractions use a small italic n. The data lines (x / f) of Example 2.18 are kept as a one-row table with f values printed "03" and "08". Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 80 (printed 72) ----------
s=page(80,U,'72','Example 2.18 solution · Case-iii continuous series · Example 2.19','مثال 2.18 کا حل · صورت-iii مسلسل سلسلہ · مثال 2.19','د بېلګې 2.18 حل · حالت-iii دوامداره لړۍ · بېلګه 2.19','quantile-examples-2')
s['tables']=[table('Example 2.18: arranged data with cumulative frequency','مثال 2.18: جمعی تعدد کے ساتھ ترتیب شدہ اعداد و شمار','بېلګه 2.18: له مجموعي فریکونسي سره ترتیب شوي معلومات',[c('x'),c('f'),c('c.f')],[[c(a),c(b),c(d)] for a,b,d in [('10','3','3'),('25','8','11'),('30','14','25'),('36','18','43'),('40','27','70'),('44','23','93'),('50','22','115'),('55','17','132'),('60','08','140')]]+[[c('Total','کل','ټول'),c('140'),c('–')]],exampleId='stat11-ex-2-18',role='solution'),
 table('Example 2.19: classes and frequency','مثال 2.19: جماعتیں اور تعدد','بېلګه 2.19: ټولګي او فریکونسي',[c('Classes:','جماعتیں:','ټولګي:')]+[c(v) for v in ['0 – 4','5 – 9','10–14','15–19','20–24','25–29','30–34']],[[c('Frequency:','تعدد:','فریکونسي:')]+[c(str(v)) for v in [4,6,10,16,12,8,4]]],exampleId='stat11-ex-2-19'),
 table('Example 2.19: class boundaries and c.f','مثال 2.19: جماعتی سرحدیں اور c.f','بېلګه 2.19: د ټولګي پولې او c.f',[c('Classes','جماعتیں','ټولګي'),c('f'),c('Class boundaries','جماعتی سرحدیں','د ټولګي پولې'),c('c.f')],[[c(a),c(b),c(d),c(e)] for a,b,d,e in [('0 – 4','4','−0.5 – 4.5','4'),('5 – 9','6','4.5 – 9.5','10'),('10 – 14','10','9.5 – 14.5','20'),('15 – 19','16','14.5 – 19.5','36'),('20 – 24','12','19.5 – 24.5','48'),('25 – 29','8','24.5 – 29.5','56'),('30 – 34','4','29.5 – 34.5','60')]]+[[c('Total','کل','ټول'),c('60'),c('–'),c('–')]],exampleId='stat11-ex-2-19',role='solution')]
add(s,'n1','Since Σf = 140 is even','چونکہ Σf = 140 جفت ہے','ځکه چې Σf = 140 جفت دی',role='solution',exampleId='stat11-ex-2-18')
add(s,'c3','Case-iii: Continuous series or grouped data.','صورت-iii: مسلسل سلسلہ یا گروہی اعداد و شمار۔','حالت-iii: دوامداره لړۍ یا ګروپي معلومات.')
head(s,'ex19','Example: 2.19','مثال: 2.19','بېلګه: 2.19',exampleId='stat11-ex-2-19')
add(s,'q19','Calculate Q₁, D₈, and P₆₀ from the following data:','درج ذیل اعداد و شمار سے Q₁، D₈ اور P₆₀ حساب کریں:','له لاندې معلوماتو څخه Q₁، D₈ او P₆₀ محاسبه کړئ:',role='question',exampleId='stat11-ex-2-19')
head(s,'sol19','Solution:','حل:','حل:',exampleId='stat11-ex-2-19')
add(s,'n2','Here Σf = 60 is even','یہاں Σf = 60 جفت ہے','دلته Σf = 60 جفت دی',role='solution',exampleId='stat11-ex-2-19')
s['equations']=[
 eqn(80,'a1',r'\text{(i)}\ \therefore Q_2=2\left(\dfrac{\sum f}{4}\right)\text{th value}=2\left(\dfrac{140}{4}\right)\text{th value}=70\text{th value.}','(i) ∴ Q2 = 2(Σf/4)th value = 2(140/4)th value = 70th value.',exampleId='stat11-ex-2-18'),
 eqn(80,'a1b',r'\Rightarrow Q_2=40','⇒ Q2 = 40',exampleId='stat11-ex-2-18'),
 eqn(80,'a2',r'\text{(ii)}\ D_6=6\left(\dfrac{\sum f}{10}\right)\text{th value}=6\left(\dfrac{140}{10}\right)\text{th value}=84\text{th value.}','(ii) D6 = 6(Σf/10)th value = 6(140/10)th value = 84th value.',exampleId='stat11-ex-2-18'),
 eqn(80,'a2b',r'\Rightarrow D_6=44','⇒ D6 = 44',exampleId='stat11-ex-2-18'),
 eqn(80,'a3',r'\text{(iii)}\ P_{25}=25\left(\dfrac{\sum f}{100}\right)\text{th value}=25\left(\dfrac{140}{100}\right)\text{th value}=35\text{th value.}','(iii) P25 = 25(Σf/100)th value = 25(140/100)th value = 35th value.',exampleId='stat11-ex-2-18'),
 eqn(80,'a3b',r'\Rightarrow P_{25}=36','⇒ P25 = 36',exampleId='stat11-ex-2-18'),
 eqn(80,'b1',r'\text{(i)}\ Q_1=\left(\dfrac{\sum f}{4}\right)\text{th value}=\left(\dfrac{60}{4}\right)\text{th value}=15\text{th value.}','(i) Q1 = (Σf/4)th value = (60/4)th value = 15th value.',exampleId='stat11-ex-2-19')]
s['flow']=[dict(type='table',index=0),dict(type='paragraphs',ids=[pid(80,'n1')]),dict(type='equation',index=0),dict(type='equation',index=1),dict(type='equation',index=2),dict(type='equation',index=3),dict(type='equation',index=4),dict(type='equation',index=5),dict(type='paragraphs',ids=[pid(80,k) for k in ('c3','ex19','q19')]),dict(type='table',index=1),dict(type='paragraphs',ids=[pid(80,'sol19')]),dict(type='table',index=2),dict(type='paragraphs',ids=[pid(80,'n2')]),dict(type='equation',index=6)]
s['sourceNote']='Printed page 72. The right-hand working of Example 2.18 is printed beside the table and follows it here. Printed "0 – 4" class with boundary "−0.5 – 4.5" and the "08" frequency are as printed. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 81 (printed 73) ----------
s=page(81,U,'73','Example 2.19 (end) · 2.3.10 Graphic calculation of quartiles, deciles, percentiles · Example 2.20','مثال 2.19 (اختتام) · 2.3.10 چوتھائیوں، دسویں اور فی صدکیات کا گرافی حساب · مثال 2.20','بېلګه 2.19 (پای) · 2.3.10 د څلورمو، لسمو او سلمو ګرافي محاسبه · بېلګه 2.20','quantile-graphic-1')
add(s,'i1','It implies that Q₁ lies in the group (9.5 - 14.5).','اس کا مطلب ہے کہ Q₁ گروہ (9.5 - 14.5) میں واقع ہے۔','پدې معنا چې Q₁ په ډله (9.5 - 14.5) کې پرته ده.',role='solution',exampleId='stat11-ex-2-19')
add(s,'i2','It implies that D₈ lies in the group (19.5 - 24.5).','اس کا مطلب ہے کہ D₈ گروہ (19.5 - 24.5) میں واقع ہے۔','پدې معنا چې D₈ په ډله (19.5 - 24.5) کې پرته ده.',role='solution',exampleId='stat11-ex-2-19')
add(s,'i3','It implies that P₆₀ lies in the group (14.5 - 19.5).','اس کا مطلب ہے کہ P₆₀ گروہ (14.5 - 19.5) میں واقع ہے۔','پدې معنا چې P₆₀ په ډله (14.5 - 19.5) کې پرته ده.',role='solution',exampleId='stat11-ex-2-19')
head(s,'h2310','2.3.10 Graphic calculation of quartiles, deciles and percentiles','2.3.10 چوتھائیوں، دسویں اور فی صدکیات کا گرافی حساب','2.3.10 د څلورمو، لسمو او سلمو ګرافي محاسبه')
head(s,'ex20','Example: 2.20','مثال: 2.20','بېلګه: 2.20',exampleId='stat11-ex-2-20')
add(s,'q20','Compute graphically quartiles, D₈ and P₇₀ from the data given below;','نیچے دیے گئے اعداد و شمار سے چوتھائیاں، D₈ اور P₇₀ گرافی طور پر حساب کریں؛','د لاندې ورکړل شویو معلوماتو څخه څلورمې، D₈ او P₇₀ په ګرافي ډول محاسبه کړئ؛',role='question',exampleId='stat11-ex-2-20')
head(s,'sol20','Solution:','حل:','حل:',exampleId='stat11-ex-2-20')
add(s,'n3','Here Σf = n = 100 is even so','یہاں Σf = n = 100 جفت ہے اس لیے','دلته Σf = n = 100 جفت دی نو',role='solution',exampleId='stat11-ex-2-20')
s['tables']=[table('Example 2.20: marks and number of students','مثال 2.20: نمبر اور طلبہ کی تعداد','بېلګه 2.20: نمرې او د زده کوونکو شمېر',[c('Marks:','نمبر:','نمرې:')]+[c(v) for v in ['10–19','20–29','30–39','40–49','50–59','60–69']],[[c('No. of students:','طلبہ کی تعداد:','د زده کوونکو شمېر:')]+[c(v) for v in ['12','18','27','20','17','06']]],exampleId='stat11-ex-2-20'),
 table('Example 2.20: c.f and class boundaries','مثال 2.20: c.f اور جماعتی سرحدیں','بېلګه 2.20: c.f او د ټولګي پولې',[c('Marks','نمبر','نمرې'),c('f'),c('c.f'),c('Class boundaries','جماعتی سرحدیں','د ټولګي پولې')],[[c(a),c(b),c(d),c(e)] for a,b,d,e in [('10 – 19','12','12','9.5 – 19.5'),('20 – 29','18','30','19.5 – 29.5'),('30 – 39','27','57','29.5 – 39.5'),('40 – 49','20','77','39.5 – 49.5'),('50 – 59','17','94','49.5 – 59.5'),('60 – 69','06','100','59.5 – 69.5')]]+[[c('Total','کل','ټول'),c('100'),c('–'),c('–')]],exampleId='stat11-ex-2-20',role='solution')]
s['equations']=[
 eqn(81,'e1',r'\therefore Q_1=l_1+\dfrac{h}{f}\left(\dfrac{\sum f}{4}-c\right)=9.5+\dfrac{5}{10}\left(\dfrac{60}{4}-10\right)=9.5+\dfrac{25}{10}=9.5+2.5=12','∴ Q1 = l1 + (h/f)(Σf/4 − c) = 9.5 + (5/10)(60/4 − 10) = 9.5 + 25/10 = 9.5 + 2.5 = 12',exampleId='stat11-ex-2-19'),
 eqn(81,'e2',r'\text{(ii)}\ D_8=8\left(\dfrac{\sum f}{10}\right)\text{th value}=8\left(\dfrac{60}{10}\right)\text{th value}=48\text{th value}','(ii) D8 = 8(Σf/10)th value = 8(60/10)th value = 48th value',exampleId='stat11-ex-2-19'),
 eqn(81,'e3',r'\therefore D_8=l_1+\dfrac{h}{f}\left(\dfrac{8\sum f}{10}-c\right)=19.5+\dfrac{5}{12}(48-36)=19.5+\dfrac{5}{12}(12)=19.5+5=24.5','∴ D8 = l1 + (h/f)(8Σf/10 − c) = 19.5 + (5/12)(48 − 36) = 19.5 + (5/12)(12) = 19.5 + 5 = 24.5',exampleId='stat11-ex-2-19'),
 eqn(81,'e4',r'\text{(iii)}\ P_{60}=60\left(\dfrac{\sum f}{100}\right)\text{th value}=60\left(\dfrac{60}{100}\right)\text{th value}=36\text{th value.}','(iii) P60 = 60(Σf/100)th value = 60(60/100)th value = 36th value.',exampleId='stat11-ex-2-19'),
 eqn(81,'e5',r'\therefore P_{60}=l_1+\dfrac{h}{f}\left(\dfrac{60\sum f}{100}-c\right)=14.5+\dfrac{5}{16}(36-20)=14.5+\dfrac{5}{16}(16)=14.5+5=19.5','∴ P60 = l1 + (h/f)(60Σf/100 − c) = 14.5 + (5/16)(36 − 20) = 14.5 + (5/16)(16) = 14.5 + 5 = 19.5',exampleId='stat11-ex-2-19'),
 eqn(81,'e6',r'Q_1=\left(\dfrac{\sum f}{4}\right)\text{th value}=\left(\dfrac{100}{4}\right)\text{th value}=25\text{th value.}','Q1 = (Σf/4)th value = (100/4)th value = 25th value.',exampleId='stat11-ex-2-20'),
 eqn(81,'e7',r'Q_2=2\left(\dfrac{\sum f}{4}\right)\text{th value}=2\left(\dfrac{100}{4}\right)\text{th value}=50\text{th value.}','Q2 = 2(Σf/4)th value = 2(100/4)th value = 50th value.',exampleId='stat11-ex-2-20')]
s['flow']=[dict(type='paragraphs',ids=[pid(81,'i1')]),dict(type='equation',index=0),dict(type='equation',index=1),dict(type='paragraphs',ids=[pid(81,'i2')]),dict(type='equation',index=2),dict(type='equation',index=3),dict(type='paragraphs',ids=[pid(81,'i3')]),dict(type='equation',index=4),dict(type='paragraphs',ids=[pid(81,k) for k in ('h2310','ex20','q20')]),dict(type='table',index=0),dict(type='paragraphs',ids=[pid(81,'sol20')]),dict(type='table',index=1),dict(type='paragraphs',ids=[pid(81,'n3')]),dict(type='equation',index=5),dict(type='equation',index=6)]
s['sourceNote']='Printed page 73. The right-hand working of Example 2.20 sits beside the table and follows it here (it continues on the next page). The heading 2.3.10 is printed in plain (non-bold) type. Printed "D₈ = 8(Σf/10)" fractions keep the printed structure. Header graphics and watermark excluded.'
s['vocabulary']={}
save(s)
# ---------- scan 82 (printed 74) ----------
s=page(82,U,'74','Example 2.20 (end) · graph · 2.4 Mode','مثال 2.20 (اختتام) · گراف · 2.4 عادہ','بېلګه 2.20 (پای) · ګراف · 2.4 مود','quantile-graph-mode')
s['equations']=[
 eqn(82,'e1',r'Q_3=3\left(\dfrac{\sum f}{4}\right)\text{th value}=3\left(\dfrac{100}{4}\right)\text{th value}=75\text{th value.}','Q3 = 3(Σf/4)th value = 3(100/4)th value = 75th value.',exampleId='stat11-ex-2-20'),
 eqn(82,'e2',r'D_8=8\left(\dfrac{\sum f}{10}\right)\text{th value}=8\left(\dfrac{100}{10}\right)\text{th value}=80\text{th value.}','D8 = 8(Σf/10)th value = 8(100/10)th value = 80th value.',exampleId='stat11-ex-2-20'),
 eqn(82,'e3',r'P_{70}=70\left(\dfrac{\sum f}{100}\right)\text{th value}=70\left(\dfrac{100}{100}\right)\text{th value}=70\text{th value}','P70 = 70(Σf/100)th value = 70(100/100)th value = 70th value',exampleId='stat11-ex-2-20')]
add(s,'ap','Approximate Answers: Q₁ = 27, Q₂ = 38, Q₃ = 49.5, D₈ = 52, P₇₀ = 48','تخمینی جوابات: Q₁ = 27، Q₂ = 38، Q₃ = 49.5، D₈ = 52، P₇₀ = 48','نږدې ځوابونه: Q₁ = 27، Q₂ = 38، Q₃ = 49.5، D₈ = 52، P₇₀ = 48',role='solution',exampleId='stat11-ex-2-20')
head(s,'h24','2.4 Mode','2.4 عادہ','2.4 مود')
add(s,'t24','A value that appears most often in a data set is called mode. For example, x = 3, 6, 5, 3, 2. As the value 3 appears most number of time i.e. twice and remaining values occur only once so Mode = 3. Sometimes a data set may have no mode or may have more than one mode, whereas, it will have only one mean and only one median. A data set with each value occurring only once has no mode. A data set with only one value occurring with the highest frequency has only one mode. The data set in this case, is called unimodal. A data set with two','وہ قدر جو اعداد و شمار کے مجموعے میں سب سے زیادہ بار آئے عادہ کہلاتی ہے۔ مثال کے طور پر x = 3, 6, 5, 3, 2۔ چونکہ قدر 3 سب سے زیادہ بار یعنی دو بار آتی ہے اور باقی قدریں صرف ایک بار آتی ہیں اس لیے عادہ = 3۔ بعض اوقات اعداد و شمار کے مجموعے کا کوئی عادہ نہیں ہو سکتا یا ایک سے زیادہ عادہ ہو سکتے ہیں، جبکہ اس کا صرف ایک اوسط اور صرف ایک وسطانیہ ہوتا ہے۔ جس مجموعے میں ہر قدر صرف ایک بار آئے اس کا کوئی عادہ نہیں ہوتا۔ جس مجموعے میں صرف ایک قدر سب سے زیادہ تعدد کے ساتھ آئے اس کا صرف ایک عادہ ہوتا ہے۔ اس صورت میں مجموعہ یک عادی کہلاتا ہے۔ دو والا مجموعہ','هغه ارزښت چې په معلوماتو ټولګه کې تر ټولو ډېر ځله راځي مود بلل کېږي. د مثال په توګه x = 3, 6, 5, 3, 2. څرنګه چې ارزښت 3 تر ټولو ډېر ځله یعنې دوه ځله راځي او پاتې ارزښتونه یوازې یو ځل راځي نو مود = 3. ځینې وختونه د معلوماتو ټولګه کېدای شي هېڅ مود ونه لري یا له یو څخه ډېر مودونه ولري، پداسې حال کې چې یوازې یو اوسط او یوازې یوه میانه لري. هغه ټولګه چې هر ارزښت یوازې یو ځل په کې راځي مود نه لري. هغه ټولګه چې یوازې یو ارزښت لوړې فریکونسۍ سره په کې راځي یوازې یو مود لري. په دې حالت کې ټولګه یو‌مودي بلل کېږي. هغه ټولګه چې دوه',sourceGap=dict(note='The sentence continues on the next page ("…A data set with two modes is called bimodal…").'))
s['figures']=[dict(id='stat11-s082-fig1',svg=qdg(),caption='Graphic Estimation of Quartiles, D and P',captionUrdu='چوتھائیوں، D اور P کا گرافی تخمینہ',captionPashto='د څلورمو، D او P ګرافي اټکل',labels=[lab('Cumulative frequencies','جمعی تعددات','مجموعي فریکونسۍ'),lab('Class boundaries','جماعتی سرحدیں','د ټولګي پولې')],sourceGap=dict(note='Redrawn as coded SVG from the c.f values (9.5→0, 19.5→12, 29.5→30, 39.5→57, 49.5→77, 59.5→94, 69.5→100); the guide lines are drawn at the printed approximate answers (27, 38, 49.5, 52, 48).'))]
s['flow']=[dict(type='equation',index=0),dict(type='equation',index=1),dict(type='equation',index=2),dict(type='figure',index=0),dict(type='paragraphs',ids=[pid(82,k) for k in ('ap','h24','t24')])]
s['sourceNote']='Printed page 74. The first three lines continue the Example 2.20 working from the previous page. A colour smudge at the top-left is ignored. Header graphics and watermark excluded.'
s['vocabulary']={'mode':dict(ur='عادہ',ps='مود'),'unimodal':dict(ur='یک عادی',ps='یو‌مودي')}
save(s)
