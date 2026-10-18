from hpehelp import *
def P(s,rows,pre='p'):
    for (ur,en,ps,*m) in rows: add(s,f'{pre}{len(s["paras"])+1}',en,ur,ps,**(m[0] if m else {}))
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def Q(s,ur,en,ps,u='u07',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'hpe11-{u}-q',tab='exercise',**k)
def O(s,ur,en,ps,u='u07'): add(s,f'o{len(s["paras"])+1}',en,ur,ps,role='option',exerciseId=f'hpe11-{u}-q',tab='exercise')
c=cell
GAP=lambda t:dict(sourceGap=dict(note=t))
NOTE=' English and Pashto are our translations (need native review); watermark and footer strip excluded.'
def L(items,g):
    return [(i[0],i[1],i[2],dict(listGroup=g,**(i[3] if len(i)>3 else {}))) for i in items]
def MC(s,q,opts):
    Q(s,*q)
    for o in opts: O(s,*o)
def tl(x,y,t,a='middle',sz=12,col='#222'): return f'<text x="{x}" y="{y}" font-size="{sz}" text-anchor="{a}" fill="{col}" font-family="sans-serif">{t}</text>'
def box(x,y,w,h,fill='#bbdefb'): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#64b5f6"/>'
# scan 141 = printed 139
s=page(141,'u07','139','Exercise questions: hockey (1 v–vii; 2 i–iv)','مشقی سوالات: ہاکی (1 v–vii؛ 2 i–iv)','تمرین پوښتنې: هاکي (۱ v–vii؛ ۲ i–iv)','ex7n')
F=Flow(s)
MC(s,('(v) ہاکی میں جس جگہ فاؤل ہوگا وہاں سے ________ لی جاتی ہے۔','(v) In hockey, from the place where the foul occurs, a ________ is taken.','(v) په هاکۍ کې چېرته چې فاول وي له هماغه ځایه ________ اخیستل کېږي.'),[('(الف) پنلٹی کارنر','(a) Penalty corner','(الف) پنلټي کارنر'),('(ب) فری ہٹ','(b) Free hit','(ب) فري هټ'),('(ج) کارنر','(c) Corner','(ج) کارنر'),('(د) پنلٹی سٹروک','(d) Penalty stroke','(د) پنلټي سټروک')])
MC(s,('(vi) ہاکی میں جب دفاعی ٹیم کا کوئی کھلاڑی 25 گز لائن کے اندر کوئی خطرناک فاؤل کرے تو مخالف ٹیم ________ کو دی جاتی ہے۔','(vi) In hockey, when a player of the defending team commits a dangerous foul inside the 25-yard line, the opposing team is given a ________.','(vi) په هاکۍ کې کله چې د دفاعي ټیم کوم لوبغاړی د ۲۵ ګز لاین دننه خطرناک فاول وکړي نو مخالف ټیم ته ________ ورکول کېږي.',),[('(الف) پنلٹی کارنر','(a) Penalty corner','(الف) پنلټي کارنر'),('(ب) فری ہٹ','(b) Free hit','(ب) فري هټ'),('(ج) کارنر','(c) Corner','(ج) کارنر'),('(د) پنلٹی سٹروک','(d) Penalty stroke','(د) پنلټي سټروک')])
MC(s,('(vii) ہاکی میں جب دفاعی ٹیم کا کھلاڑی ڈی (D) کے اندر خطرناک طریقے سے بال کو کلیئر کرے تو مخالف ٹیم کو ________ دی جاتی ہے۔','(vii) In hockey, when a player of the defending team clears the ball from inside the D in a dangerous manner, the opposing team is given a ________.','(vii) په هاکۍ کې کله چې د دفاعي ټیم لوبغاړی د ډي (D) دننه په خطرناکه طریقه توپ کلیر کړي نو مخالف ټیم ته ________ ورکول کېږي.'),[('(الف) ہٹ ان','(a) Hit-in','(الف) هټ ان'),('(ب) فری ہٹ','(b) Free hit','(ب) فري هټ'),('(ج) پنلٹی سٹروک','(c) Penalty stroke','(ج) پنلټي سټروک'),('(د) پنلٹی کارنر','(d) Penalty corner','(د) پنلټي کارنر')])
H(s,'2۔ درج ذیل سوالات کے جوابات تحریر کریں۔','2. Write answers to the following questions.','۲. لاندې پوښتنو ځوابونه ولیکئ.')
Q(s,'(i) ہاکی کے گراؤنڈ کا خاکہ پیمائش سمیت بنائیں۔','(i) Draw a sketch of the hockey ground with its measurements.','(i) د هاکۍ د ګراونډ انځور له اندازو سره جوړ کړئ.')
Q(s,'(ii) ہاکی کے کھیل کے قواعد و ضوابط تحریر کریں۔','(ii) Write the rules and regulations of the game of hockey.','(ii) د هاکۍ د لوبې قواعد او ضوابط ولیکئ.')
Q(s,'(iii) ہاکی کے فاؤلز لکھیں۔','(iii) Write the fouls of hockey.','(iii) د هاکۍ فاولونه ولیکئ.')
Q(s,'(iv) درج ذیل پر نوٹ لکھیں۔ (1) پنلٹی کارنر (2) پنلٹی سٹروک (3) فری ہٹ','(iv) Write notes on the following: (1) Penalty corner (2) Penalty stroke (3) Free hit.','(iv) پر لاندې یادښت ولیکئ: (۱) پنلټي کارنر (۲) پنلټي سټروک (۳) فري هټ.')
F.done()
s['sourceNote']='Printed page 139: hockey exercise items v–vii (multiple choice) and question 2 (i–iv, with the list 1–3 under iv). The page number “139” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 142 = printed 140
s=page(142,'u07','140','Tournament systems: knockout system; fixture of 6 teams','ٹورنامنٹ سسٹم: ناک آؤٹ سسٹم؛ 6 ٹیموں کا فکسچر','د ټورنامنټ سیسټمونه: ناک آوټ سیسټم؛ د ۶ ټیمونو فکسچر','tour-1')
F=Flow(s)
H(s,'ٹورنامنٹ سسٹم','Tournament Systems','د ټورنامنټ سیسټمونه')
P(s,[('ٹورنامنٹ سسٹم کی مندرجہ ذیل اقسام ہیں۔','There are the following kinds of tournament system.','د ټورنامنټ سیسټم لاندې ډولونه دي.')]+L([('1۔ ناک آؤٹ سسٹم (Knockout System)','1. Knockout System','۱. ناک آوټ سیسټم (Knockout System)'),('2۔ لیگ سسٹم (League System)','2. League System','۲. لیګ سیسټم (League System)'),('3۔ کومبی نیشن سسٹم (Combination System)','3. Combination System','۳. کمبینیشن سیسټم (Combination System)')],'ts'))
H(s,'1۔ ناک آؤٹ سسٹم (Knockout System)','1. Knockout System','۱. ناک آوټ سیسټم (Knockout System)')
P(s,[]+L([('اس سسٹم میں کوا اگر کوئی ٹیم میچ ہار جائے تو وہ ٹورنامنٹ سے باہر ہو جاتی ہے۔','In this system, if a team loses a match it goes out of the tournament.','په دې سیسټم کې که کوم ټیم لوبه وبایلي نو له ټورنامنټ نه بهر کېږي.',GAP('The printed Urdu has a stray word “کوا” (probably “کوئی”); kept as printed.')),
('اگر ٹیموں کی تعداد 2 کی مکمل طاقت یعنی 2، 4، 8، 16، 32 ہو تو کسی ٹیم کو "بائی" نہیں دی جائے گی۔','If the number of teams is a full power of 2, that is 2, 4, 8, 16, 32, no team will be given a “bye”.','که د ټیمونو شمېر د ۲ بشپړ توان وي یعنې ۲، ۴، ۸، ۱۶، ۳۲ نو هېڅ ټیم ته «بای» نه ورکول کېږي.',GAP('The scan reads “2, 8, 16, 32”; the item 4 is not visible and may be omitted in print.')),
('اگر ٹیموں کی تعداد 2 کی مکمل طاقت نہ ہو تو اگلی طاقت تک جانے کے لیے بائی دی جائے گی۔','If the number of teams is not a full power of 2, byes will be given to reach the next power.','که د ټیمونو شمېر د ۲ بشپړ توان نه وي نو بل توان ته رسېدو لپاره بای ورکول کېږي.'),
('بائیاں قرعہ اندازی کے ذریعے دی جائیں گی۔','Byes will be given by draw of lots.','بایونه به د قرعې په ذریعه ورکول کېږي.'),
('فکسچر میں ڈیٹ اور ٹائم دستیاب سہولیات کے مطابق دیا جائے گا۔','In the fixture the date and time will be given according to the available facilities.','په فکسچر کې نېټه او وخت به د شته اسانتیاوو سره سم ورکول کېږي.'),
('میچوں کی تعداد معلوم کرنے کا فارمولا','The formula for finding the number of matches','د لوبو د شمېر د موندلو فارمول')],'ko'))
P(s,[('6 ٹیموں کا ناک آؤٹ سسٹم کے تحت فکسچر','Fixture of 6 teams under the knockout system','د ۶ ټیمونو فکسچر د ناک آوټ سیسټم لاندې')])
F.fg(0)
F.done()
bx=''
bx+=box(60,30,120,60)+box(60,100,120,60)+box(60,170,120,60)+box(60,240,120,60)
bx+=box(215,60,120,70)+box(215,185,120,70)+'<rect x="370" y="105" width="90" height="105" fill="#fff59d" stroke="#fbc02d"/>'
bx+=tl(40,52,'A (Bye)','end')+tl(40,92,'B','end')+tl(40,122,'C','end')+tl(40,162,'D','end')+tl(40,192,'E','end')+tl(40,232,'F','end')+tl(40,262,'F (Bye)','end')
bx=''
rows=[(30,'A','Bye'),(100,'B','C'),(170,'D','E'),(240,'F','Bye')]
bx+=box(70,25,110,55)+tl(60,55,'A','end')+tl(60,72,'Bye','end',11)+tl(125,45,'',sz=11)
bx+=box(70,90,110,60)+tl(60,115,'B','end')+tl(60,140,'C','end')+tl(125,115,'Date')+tl(125,135,'Time')
bx+=box(70,160,110,60)+tl(60,185,'D','end')+tl(60,210,'E','end')+tl(125,185,'Date')+tl(125,205,'Time')
bx+=box(70,230,110,55)+tl(60,255,'F','end')+tl(60,272,'Bye','end',11)
bx+=tl(195,55,'A',sz=13,col='#e65100')+tl(195,120,'C',sz=13,col='#e65100')+tl(195,185,'B',sz=13,col='#e65100')+tl(195,260,'F',sz=13,col='#e65100')
bx+=box(215,55,110,60)+tl(270,80,'Date')+tl(270,100,'Time')+box(215,175,110,60)+tl(270,200,'Date')+tl(270,220,'Time')
bx+=tl(335,85,'C',sz=13,col='#e65100')+tl(335,205,'F',sz=13,col='#e65100')
bx+='<rect x="355" y="95" width="95" height="105" fill="#fff59d" stroke="#fbc02d"/>'+tl(402,150,'Winner')
s['figures']=[dict(id='hpe11-s142-fig1',svg=svg(470,300,'Knockout fixture of six teams: A and F have byes; B plays C, D plays E; the winners meet the bye teams in the second round and the two winners meet in the final',bx),caption='Knockout fixture for 6 teams (A and F have byes)',captionUrdu='6 ٹیموں کا ناک آؤٹ فکسچر (A اور F کو بائی)',captionPashto='د ۶ ټیمونو ناک آوټ فکسچر (A او F ته بای)',labels=[],sourceGap=dict(note='Simplified coded redrawing of the coloured bracket; the printed bracket labels are reproduced as read.'))]
s['sourceNote']='Printed page 140: chapter heading Tournament System (ٹورنامنٹ سسٹم), the three kinds, and the knockout system rules with a fixture bracket of 6 teams. The page number “140” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 143 = printed 141
s=page(143,'u07','141','Tournament systems: fixture of 8 teams; league system','ٹورنامنٹ سسٹم: 8 ٹیموں کا فکسچر؛ لیگ سسٹم','د ټورنامنټ سیسټمونه: د ۸ ټیمونو فکسچر؛ لیګ سیسټم','tour-2')
F=Flow(s)
P(s,[('ناک آؤٹ سسٹم کے تحت 8 ٹیموں کا فکسچر','Fixture of 8 teams under the knockout system','د ناک آوټ سیسټم لاندې د ۸ ټیمونو فکسچر')])
F.fg(0)
H(s,'2۔ لیگ سسٹم (League System)','2. League System','۲. لیګ سیسټم (League System)')
P(s,[]+L([('اس سسٹم کے تحت ٹورنامنٹ میں شریک ہر ٹیم دوسری ٹیم کے ساتھ کھیلتی ہے۔','Under this system every team taking part in the tournament plays with every other team.','د دې سیسټم لاندې په ټورنامنټ کې ګډون کوونکی هر ټیم له بل ټیم سره لوبېږي.'),
('جفت کی صورت میں کسی بھی ٹیم کو بائی نہیں دی جاتی۔','If the number is even, no team is given a bye.','که شمېر جفت وي نو هېڅ ټیم ته بای نه ورکول کېږي.'),
('طاق کی صورت میں ہر ٹیم کو ایک بار بائی دی جاتی ہے۔','If the number is odd, every team is given a bye once.','که شمېر طاق وي نو هر ټیم ته یو ځل بای ورکول کېږي.'),
('اس سسٹم کے تحت اگر کوئی بھی ٹیم مقابلہ کے دوران ہار جائے تو وہ ٹورنامنٹ سے خارج نہیں ہوگی۔','Under this system, if any team loses during a contest it will not be eliminated from the tournament.','د دې سیسټم لاندې که کوم ټیم د سیالۍ په موده کې وبایلي نو له ټورنامنټ نه به نه ایستل کېږي.'),
('اس سسٹم کے تحت کھیلنے والی ٹیموں کو پوائنٹ اس طرح دیا جاتا ہے کہ جیتنے پر 2 پوائنٹ، برابری کی صورت میں 1، 1 پوائنٹ اور ہارنے والی ٹیم کو کوئی پوائنٹ نہیں ملے گا۔','Under this system points are given to the playing teams in this way: 2 points on winning, 1 point each in case of a draw, and the losing team will get no point.','د دې سیسټم لاندې لوبغاړو ټیمونو ته پوائنټونه داسې ورکول کېږي چې په ګټلو ۲ پوائنټه، د برابرۍ په صورت کې ۱، ۱ پوائنټ او بایلونکي ټیم ته به هېڅ پوائنټ نه ورکول کېږي.'),
('اس سسٹم میں فکسچر بناتے وقت ٹیموں کو Anticlockwise کھیلایا جائے گا۔','In this system, while making the fixture, the teams will be rotated anticlockwise.','په دې سیسټم کې د فکسچر جوړولو پر مهال به ټیمونه Anticlockwise وګرځول شي.'),
('ٹورنامنٹ ہر صورت میں طاق دنوں میں مکمل کرنا ہے۔','The tournament must in every case be completed in an odd number of days.','ټورنامنټ په هر صورت کې په طاق ورځو بشپړول دي.'),
('اس سسٹم میں میچ نکالنے کا فارمولا','The formula for finding the number of matches in this system','په دې سیسټم کې د لوبو د شمېر د موندلو فارمول')],'lg'))
P(s,[('کل میچ = ٹیموں کی تعداد (ٹیموں کی تعداد – 1) ÷ 2','Total matches = (number of teams × (number of teams − 1)) ÷ 2','ټولې لوبې = (د ټیمونو شمېر × (د ټیمونو شمېر − ۱)) ÷ ۲',GAP('The printed formula is a fraction: [number of teams × (1 − number of teams)] over 2 as printed; the standard form n(n−1)/2 is used and is confirmed by the worked examples on the next page.'))])
F.done()
bx=''
for i,(y,a,b,w) in enumerate([(25,'A','B','B'),(80,'C','D','D'),(160,'E','F','F'),(215,'G','H','H')]):
    bx+=box(70,y,110,50)+tl(60,y+20,a,'end')+tl(60,y+36,'Vs','end',10)+tl(60,y+50,b,'end')+tl(125,y+22,'Date')+tl(125,y+40,'Time')+tl(195,y+30,w,sz=14,col='#e65100')
bx+=box(215,50,100,60)+tl(265,75,'Date')+tl(265,95,'Time')+tl(330,85,'D',sz=14,col='#e65100')
bx+=box(215,185,100,60)+tl(265,210,'Date')+tl(265,230,'Time')+tl(330,220,'H',sz=14,col='#e65100')
bx+='<rect x="350" y="110" width="110" height="80" fill="#fff59d" stroke="#fbc02d"/>'+tl(405,155,'Winner')
s['figures']=[dict(id='hpe11-s143-fig1',svg=svg(480,270,'Knockout fixture of eight teams: A v B, C v D, E v F, G v H in round one; winners meet in two semi-finals and the winners play the final',bx),caption='Knockout fixture for 8 teams',captionUrdu='8 ٹیموں کا ناک آؤٹ فکسچر',captionPashto='د ۸ ټیمونو ناک آوټ فکسچر',labels=[],sourceGap=dict(note='Simplified coded redrawing of the coloured bracket; round-winner letters are shown as printed (B, D, F, H, then D and H).'))]
s['sourceNote']='Printed page 141: the fixture of 8 teams under the knockout system, and the league system rules with the formula for the number of matches. The page number “141” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 144 = printed 142 (two fixture tables)
s=page(144,'u07','142','League system: worked example of 5 teams and fixture of 6 teams','لیگ سسٹم: 5 ٹیموں کی مثال اور 6 ٹیموں کا فکسچر','لیګ سیسټم: د ۵ ټیمونو بېلګه او د ۶ ټیمونو فکسچر','tour-3')
F=Flow(s)
P(s,[('مثلاً اگر ٹیموں کی تعداد 5 ہو تو','For example, if the number of teams is 5, then','د بېلګې په توګه که د ټیمونو شمېر ۵ وي نو'),
('کل میچ = (5−1)×5 ÷ 2 = (4×5) ÷ 2 = 20 ÷ 2 = 10','Total matches = ((5−1)×5) ÷ 2 = (4×5) ÷ 2 = 20 ÷ 2 = 10','ټولې لوبې = ((۵−۱)×۵) ÷ ۲ = (۴×۵) ÷ ۲ = ۲۰ ÷ ۲ = ۱۰',GAP('Printed as “5−1×5”; the evaluation 4×5 = 20 and 20/2 = 10 shows the intended product (5−1)×5.')),
('اس سسٹم کے تحت 5 میچوں کا فکسچر','Fixture of 5 teams’ matches under this system','د دې سیسټم لاندې د ۵ ټیمونو د لوبو فکسچر')])
F.tb(0)
P(s,[('کل میچ = (6−1)×6 ÷ 2 = (5×6) ÷ 2 = 30 ÷ 2 = 15۔ لیگ سسٹم کے تحت 6 ٹیموں کا فکسچر مندرجہ ذیل ہے۔','Total matches = ((6−1)×6) ÷ 2 = (5×6) ÷ 2 = 30 ÷ 2 = 15. The fixture of 6 teams under the league system is as follows.','ټولې لوبې = ((۶−۱)×۶) ÷ ۲ = (۵×۶) ÷ ۲ = ۳۰ ÷ ۲ = ۱۵. د لیګ سیسټم لاندې د ۶ ټیمونو فکسچر په لاندې ډول دی.')])
F.tb(1)
F.done()
def m(a,b): return f'{a} vs {b} (Date/Time)'
d5=[['By vs E','A vs D','B vs C'],['By vs D','E vs C','A vs B'],['By vs C','D vs B','E vs A'],['By vs B','C vs A','D vs E'],['By vs A','B vs E','C vs D']]
d6=[['A vs F','B vs E','C vs D'],['A vs E','F vs D','B vs C'],['A vs D','E vs C','F vs B'],['A vs C','D vs B','E vs F'],['A vs B','C vs F','D vs E']]
days=['1st day','2nd day','3rd day','4th day','5th day']
def tt(d):
    hdr=[c(x) for x in days]
    return hdr,[[c(d[j][i]+' (Date, Time)') for j in range(5)] for i in range(3)]
h5,r5=tt(d5);h6,r6=tt(d6)
s['tables']=[table('League fixture of 5 teams (10 matches; “By” = bye)','5 ٹیموں کا لیگ فکسچر (10 میچ؛ By = بائی)','د ۵ ټیمونو لیګ فکسچر (۱۰ لوبې؛ By = بای)',h5,r5),
 table('League fixture of 6 teams (15 matches)','6 ٹیموں کا لیگ فکسچر (15 میچ)','د ۶ ټیمونو لیګ فکسچر (۱۵ لوبې)',h6,r6)]
s['sourceNote']='Printed page 142: worked example of the number of league matches for 5 teams, the 5-team five-day fixture table, the 6-team calculation and its five-day fixture table. Each cell is “X vs Y” with Date and Time lines left blank in the print. The page number “142” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 145 = printed 143
s=page(145,'u07','143','Tournament systems: combination system','ٹورنامنٹ سسٹم: کومبی نیشن سسٹم','د ټورنامنټ سیسټمونه: کمبینیشن سیسټم','tour-4')
F=Flow(s)
H(s,'3۔ کومبی نیشن سسٹم (Combination System)','3. Combination System','۳. کمبینیشن سیسټم (Combination System)')
P(s,[('اس سسٹم کے تحت ابتدائی راؤنڈ لیگ سسٹم کے تحت ہوگا جبکہ سیمی فائنل اور فائنل ناک آؤٹ سسٹم کے تحت ہوں گے۔','Under this system the preliminary round will be under the league system, while the semi-finals and the final will be under the knockout system.','د دې سیسټم لاندې لومړنی راونډ به د لیګ سیسټم لاندې وي پداسې حال کې چې سیمي فاینل او فاینل به د ناک آوټ سیسټم لاندې وي.'),
('میچوں کی تعداد نکالنے کا فارمولا','The formula for finding the number of matches','د لوبو د شمېر د موندلو فارمول'),
('میچوں کی تعداد = ٹیموں کی تعداد (ٹیموں کی تعداد − 1) ÷ 2 + 3','Number of matches = (number of teams × (number of teams − 1)) ÷ 2 + 3','د لوبو شمېر = (د ټیمونو شمېر × (د ټیمونو شمېر − ۱)) ÷ ۲ + ۳'),
('مثلاً اگر ٹیموں کی تعداد 5 ہو تو','For example, if the number of teams is 5, then','د بېلګې په توګه که د ټیمونو شمېر ۵ وي نو'),
('(5−1)×5 ÷ 2 + 3 = (4×5) ÷ 2 + 3 = 20 ÷ 2 + 3 = 10 + 3 = 13','((5−1)×5) ÷ 2 + 3 = (4×5) ÷ 2 + 3 = 20 ÷ 2 + 3 = 10 + 3 = 13','((۵−۱)×۵) ÷ ۲ + ۳ = (۴×۵) ÷ ۲ + ۳ = ۲۰ ÷ ۲ + ۳ = ۱۰ + ۳ = ۱۳',GAP('Printed as “(5−1)/2 + 3 = 4×5/2 + 3 = …”; the product (5−1)×5 is as evaluated in the steps.'))])
F.done()
s['sourceNote']='Printed page 143: combination system and its formula with the 5-team example (13 matches); the rest of the page is blank. The page number “143” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 146 = printed 144 (authors, back matter)
s=page(146,'back-matter','144','Introduction of the authors (1): Malik Asif, Arif Ali Shah, Samiullah Marwat','مصنفین کا تعارف (1): ملک آصف، عارف علی شاہ، سمیع اللہ مروت','د لیکوالانو پېژندنه (۱): ملک آصف، عارف علي شاه، سمیع الله مروت','authors-1')
F=Flow(s)
H(s,'مصنفین کا تعارف','Introduction of the Authors','د لیکوالانو پېژندنه')
H(s,'ملک آصف:','Malik Asif:','ملک آصف:')
P(s,[('ملک آصف نے 1983 میں گومل یونیورسٹی سے صحت و جسمانی تعلیم (HPE) میں ایم ایس سی کی ڈگری حاصل کی اور درس و تدریس کے شعبے سے وابستہ ہو گئے۔ آپ نے مختلف کالجوں میں بطور DPE خدمات سرانجام دیے اور 2015 میں گورنمنٹ پوسٹ گریجویٹ کالج نمبر 1، ایبٹ آباد سے بطور پروفیسر HPE ریٹائرڈ ہوئے۔ آپ کئی کتابوں کے مصنف بھی ہیں۔','Malik Asif received an M.Sc. degree in Health and Physical Education (HPE) from Gomal University in 1983 and joined the field of teaching. He served as DPE in various colleges and retired in 2015 as Professor of HPE from Government Postgraduate College No. 1, Abbottabad. He is also the author of several books.','ملک آصف په ۱۹۸۳ کې د ګومل پوهنتون نه په روغتیا او فزیکي زده کړه (HPE) کې د ایم ایس سي سند ترلاسه کړ او د تدریس په څانګه پورې تړلی شو. هغه په بېلابېلو کالجونو کې د DPE په توګه خدمتونه ترسره کړل او په ۲۰۱۵ کې له ګورنمنټ پوسټ ګریجویټ کالج نمبر ۱، ایبټ آباد نه د HPE د پروفیسر په توګه تقاعد شو. هغه د ډېرو کتابونو لیکوال هم دی.')])
H(s,'عارف علی شاہ:','Arif Ali Shah:','عارف علي شاه:')
P(s,[('عارف علی شاہ نے 2003 میں یونیورسٹی آف کراچی سے صحت و جسمانی تعلیم (HPE) میں ایم ایس سی کی ڈگری حاصل کی اور گولڈ میڈل حاصل کیا۔ آپ 2006 سے درس و تدریس کے شعبے سے وابستہ ہے۔ آج کل گورنمنٹ پوسٹ گریجویٹ کالج نمبر 1، ایبٹ آباد میں بطور چیئرمین HPE ڈیپارٹمنٹ کے خدمات سرانجام دے رہے ہیں۔','Arif Ali Shah received an M.Sc. degree in Health and Physical Education (HPE) from the University of Karachi in 2003 and won a gold medal. He has been associated with teaching since 2006. At present he is serving as Chairman of the HPE Department at Government Postgraduate College No. 1, Abbottabad.','عارف علي شاه په ۲۰۰۳ کې د کراچۍ پوهنتون نه په روغتیا او فزیکي زده کړه (HPE) کې د ایم ایس سي سند ترلاسه کړ او د سرو زرو مډال یې وګاټه. هغه له ۲۰۰۶ راهیسې د تدریس په څانګه پورې تړلی دی. اوس مهال په ګورنمنټ پوسټ ګریجویټ کالج نمبر ۱، ایبټ آباد کې د HPE ډیپارټمنټ د چیرمین په توګه خدمتونه ترسره کوي.')])
H(s,'سمیع اللہ مروت:','Samiullah Marwat:','سمیع الله مروت:')
P(s,[('سمیع اللہ مروت نے 1996 میں گومل یونیورسٹی سے صحت و جسمانی تعلیم (HPE) میں ایم ایس سی کی ڈگری حاصل کی۔ مختلف سکولوں میں بطور DPE کے خدمات سرانجام دیے ہیں۔ آج کل DCTE ایبٹ آباد میں بطور ڈائریکٹر فزیکل ایجوکیشن اینڈ سپورٹس کے خدمات سرانجام دے رہے ہیں۔','Samiullah Marwat received an M.Sc. degree in Health and Physical Education (HPE) from Gomal University in 1996. He has served as DPE in various schools. At present he is serving as Director of Physical Education and Sports at the DCTE, Abbottabad.','سمیع الله مروت په ۱۹۹۶ کې د ګومل پوهنتون نه په روغتیا او فزیکي زده کړه (HPE) کې د ایم ایس سي سند ترلاسه کړ. په بېلابېلو ښوونځیو کې یې د DPE په توګه خدمتونه ترسره کړي دي. اوس مهال په DCTE ایبټ آباد کې د فزیکل ایجوکیشن او سپورټس د ډایرکټر په توګه خدمتونه ترسره کوي.')])
F.done()
s['sourceNote']='Printed page 144: heading Introduction of the Authors (مصنفین کا تعارف) with Malik Asif, Arif Ali Shah and Samiullah Marwat. Printed “Gomal”, “DPE” and “DCTE” kept as in the source. The page number “144” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 147 = printed 145
s=page(147,'back-matter','145','Introduction of the authors (2): Rasheedullah; sports-equipment illustration','مصنفین کا تعارف (2): رشید اللہ','د لیکوالانو پېژندنه (۲): رشید الله','authors-2')
F=Flow(s)
H(s,'رشید اللہ:','Rasheedullah:','رشید الله:')
P(s,[('رشید اللہ نے 1989 میں گومل یونیورسٹی سے صحت و جسمانی تعلیم (HPE) میں ایم ایس سی کی ڈگری حاصل کی۔ 1990 سے مختلف کالجوں میں بطور DPE خدمات سرانجام دے رہے ہیں۔ آج کل گورنمنٹ ڈگری کالج شیروان، ایبٹ آباد میں بطور لیکچرر خدمات سرانجام دے رہے ہیں۔','Rasheedullah received an M.Sc. degree in Health and Physical Education (HPE) from Gomal University in 1989. Since 1990 he has been serving as DPE in various colleges. At present he is serving as Lecturer at Government Degree College Sherwan, Abbottabad.','رشید الله په ۱۹۸۹ کې د ګومل پوهنتون نه په روغتیا او فزیکي زده کړه (HPE) کې د ایم ایس سي سند ترلاسه کړ. له ۱۹۹۰ راهیسې په بېلابېلو کالجونو کې د DPE په توګه خدمتونه ترسره کوي. اوس مهال په ګورنمنټ ډګري کالج شیروان، ایبټ آباد کې د لیکچرر په توګه خدمتونه ترسره کوي.')])
F.fg(0)
F.done()
fig=svg(420,230,'A set of sports equipment standing on a red strip: a basketball, three bowling pins and a bowling ball, a tennis racket, a bat, a table-tennis bat, a baseball, a badminton racket, a golf club and ball, and a rugby ball',
 '<rect width="420" height="230" fill="#ffe9a8"/><rect y="200" width="420" height="30" fill="#e53935"/>'
 '<circle cx="45" cy="170" r="28" fill="#e57346" stroke="#8d3a1a" stroke-width="2"/><g fill="#fff" stroke="#999"><rect x="82" y="130" width="14" height="70" rx="6"/><rect x="104" y="140" width="14" height="60" rx="6"/><rect x="126" y="130" width="14" height="70" rx="6"/></g><circle cx="140" cy="185" r="16" fill="#7cb342"/>'
 '<ellipse cx="190" cy="110" rx="40" ry="55" fill="none" stroke="#e53935" stroke-width="6"/><line x1="190" y1="165" x2="205" y2="200" stroke="#e53935" stroke-width="8"/><rect x="238" y="80" width="16" height="120" rx="7" fill="#37474f"/><circle cx="285" cy="100" r="22" fill="#fff" stroke="#e53935" stroke-width="3"/><circle cx="265" cy="180" r="24" fill="#e53935"/>'
 '<ellipse cx="330" cy="105" rx="30" ry="42" fill="none" stroke="#212121" stroke-width="5"/><line x1="330" y1="150" x2="305" y2="198" stroke="#212121" stroke-width="6"/><circle cx="355" cy="195" r="9" fill="#fff"/><ellipse cx="390" cy="180" rx="28" ry="18" fill="#a1362a"/>')
s['figures']=[dict(id='hpe11-s147-fig1',svg=fig,caption='Decorative picture of sports equipment',captionUrdu='کھیلوں کے سامان کی آرائشی تصویر',captionPashto='د لوبو د سامان ښکلا انځور',labels=[],sourceGap=dict(note='Decorative coloured illustration; replaced by a simplified coded SVG schematic (no raster image).'))]
s['sourceNote']='Printed page 145: the last author, Rasheedullah, followed by a decorative picture of sports equipment; the book ends here in the scans. The page number “145” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
