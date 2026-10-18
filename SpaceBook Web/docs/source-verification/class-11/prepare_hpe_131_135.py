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
    return [(a,b,c_,dict(listGroup=g)) for a,b,c_ in items]
def MC(s,q,opts):
    Q(s,*q)
    for o in opts: O(s,*o)
def opts4(vals):
    return [(f'({a}) {v}',f'({e}) {v}',f'({a}) {v}') for a,e,v in zip(['الف','ب','ج','د'],['a','b','c','d'],vals)]
def mc(s,ur,en,ps,vals): MC(s,(ur,en,ps),opts4(vals))
# scan 131 = printed 129
s=page(131,'u07','129','Exercise questions: Kabaddi (1 i–vi)','مشقی سوالات: کبڈی (1 i–vi)','تمرین پوښتنې: کبډي (۱ i–vi)','ex7l')
F=Flow(s)
H(s,'مشقی سوالات','Exercise Questions','تمرین پوښتنې')
H(s,'1۔ موزوں جوابات منتخب کر کے لکھیں۔','1. Select the suitable answers and write them.','۱. مناسب ځوابونه وټاکئ او ولیکئ.')
mc(s,'i۔ کبڈی میچ کا مجموعی وقت ________ منٹ ہوتا ہے۔','i. The total time of a Kabaddi match is ________ minutes.','i. د کبډۍ د لوبې ټوله موده ________ دقیقې وي.',['20','15','30','40'])
mc(s,'ii۔ کبڈی کھیل کے درمیان وقفہ ________ منٹ ہوتا ہے۔','ii. The break in the middle of a Kabaddi game is ________ minutes.','ii. د کبډۍ د لوبې ترمنځ وقفه ________ دقیقې وي.',['5','10','3','15'])
mc(s,'iii۔ کبڈی ٹیم میں ________ کھلاڑی ہوتے ہیں۔','iii. There are ________ players in a Kabaddi team.','iii. د کبډۍ په ټیم کې ________ لوبغاړي وي.',['15','12','10','11'])
mc(s,'iv۔ کبڈی میں حملہ آور کو ________ سیکنڈ کا وقت دیا جاتا ہے۔','iv. In Kabaddi the raider is given ________ seconds.','iv. په کبډۍ کې برید کوونکي ته ________ ثانیې وخت ورکول کېږي.',['10','30','15','20'])
mc(s,'v۔ کبڈی میں دائرہ کا نصف قطر ________ فٹ ہوتا ہے۔','v. In Kabaddi the radius of the circle is ________ feet.','v. په کبډۍ کې د دایرې نیم قطر ________ فټه وي.',['60','40','80','70'])
mc(s,'vi۔ کبڈی کے گراؤنڈ میں پالے کی زیادہ سے زیادہ اونچائی ________ انچ ہوتی ہے۔','vi. In a Kabaddi ground the maximum height of the pale is ________ inches.','vi. د کبډۍ په ګراونډ کې د پالې ډېره ډېره لوړوالی ________ انچه وي.',['6','7','8','9'])
F.done()
s['sourceNote']='Printed page 129: heading Exercise Questions, question 1 items i–vi on Kabaddi (continued). The page number “129” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 132 = printed 130
s=page(132,'u07','130','Exercise questions: Kabaddi (vii–ix) and descriptive questions','مشقی سوالات: کبڈی (vii–ix) اور تفصیلی سوالات','تمرین پوښتنې: کبډي (vii–ix) او تشریحي پوښتنې','ex7m')
F=Flow(s)
mc(s,'vii۔ کبڈی میں پالوں کا درمیانی فاصلہ ________ فٹ ہوتا ہے۔','vii. In Kabaddi the distance between the pales is ________ feet.','vii. په کبډۍ کې د پالو ترمنځ واټن ________ فټه وي.',['20','10','15','18'])
mc(s,'viii۔ کبڈی کے میچ میں برابری کی صورت میں ________ منٹ اضافی وقت دیا جاتا ہے۔','viii. In a Kabaddi match, in case of a tie, ________ minutes of extra time are given.','viii. د کبډۍ په لوبه کې د برابرۍ په صورت کې ________ دقیقې اضافي وخت ورکول کېږي.',['5','15','10','20'])
mc(s,'ix۔ کبڈی کے میچ میں ________ امپائر ہوتے ہیں۔','ix. There are ________ umpires in a Kabaddi match.','ix. د کبډۍ په لوبه کې ________ امپایران وي.',['1','3','2','4'])
H(s,'2۔ درج ذیل سوالات کے جواب لکھیں۔','2. Write answers to the following questions.','۲. لاندې پوښتنو ځوابونه ولیکئ.')
Q(s,'i۔ کبڈی کا دائرہ بنائیں اور فاؤلز درج کریں۔','i. Draw the Kabaddi circle and list the fouls.','i. د کبډۍ دایره جوړه کړئ او فاولونه ولیکئ.')
Q(s,'ii۔ کبڈی کھیل کے قواعد و ضوابط درج کریں۔','ii. List the rules and regulations of the game of Kabaddi.','ii. د کبډۍ د لوبې قواعد او ضوابط ولیکئ.')
F.done()
s['sourceNote']='Printed page 130: Kabaddi exercise items vii–ix (multiple-choice) and question 2 (i–ii); lower part blank. The page number “130” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 133 = printed 131 (hockey field)
s=page(133,'u07','131','Hockey: playing field and goal post dimensions','ہاکی: کھیل کا میدان اور گول پوسٹ کی پیمائش','هاکي: د لوبې میدان او د ګول پوسټ اندازې','hockey-1')
F=Flow(s)
H(s,'ہاکی','Hockey','هاکي')
H(s,'کھیل کا میدان','The Playing Field','د لوبې میدان')
F.tb(0)
H(s,'گول پوسٹ','Goal Post','ګول پوسټ')
F.tb(1)
F.fg(0)
F.done()
rows=[('Length','لمبائی','اوږدوالی','100 yards','100 گز','۱۰۰ ګز','91.4 metres','91.4 میٹر','۹۱.۴ متره'),
('Width','چوڑائی','سور','60 yards','60 گز','۶۰ ګز','55 metres','55 میٹر','۵۵ متره'),
('Shooting circle','شوٹنگ سرکل','شوټنګ سرکل','16 yards','16 گز','۱۶ ګز','14.63 metres','14.63 میٹر','۱۴.۶۳ متره'),
('Penalty stroke','پنلٹی سٹروک','پنلټي سټروک','7 yards','7 گز','۷ ګز','6.45 metres','6.45 میٹر','۶.۴۵ متره'),
('Penalty corner','پنلٹی کارنر','پنلټي کارنر','10 yards','10 گز','۱۰ ګز','9.41 metres','9.41 میٹر','۹.۴۱ متره'),
('Corner','کارنر','کارنر','5 yards','5 گز','۵ ګز','4.55 metres','4.55 میٹر','۴.۵۵ متره')]
rows2=[('Distance between the posts','پولوں کا درمیانی فاصلہ','د پولونو ترمنځ واټن','4 yards','4 گز','۴ ګز','3.66 metres','3.66 میٹر','۳.۶۶ متره'),
('Height','اونچائی','لوړوالی','7 feet','7 فٹ','۷ فټه','2.25 metres','2.25 میٹر','۲.۲۵ متره'),
('Board','تختہ','تخته','18 inches','18 انچ','۱۸ انچه','46 centimetres','46 سینٹی میٹر','۴۶ سانتي متره')]
def trow(r): return [c(r[0],r[1],r[2]),c(r[3],r[4],r[5]),c(r[6],r[7],r[8])]
hdr=[c('Item','پیمائش','اندازه'),c('Yards / feet / inches','گز / فٹ / انچ','ګز / فټ / انچ'),c('Metric','میٹرک','میټریک')]
s['tables']=[table('Hockey playing field dimensions','ہاکی کے میدان کی پیمائشیں','د هاکۍ د میدان اندازې',hdr,[trow(r) for r in rows]),
 table('Hockey goal post dimensions','ہاکی گول پوسٹ کی پیمائشیں','د هاکۍ د ګول پوسټ اندازې',hdr,[trow(r) for r in rows2])]
def tl(x,y,t,a='middle',sz=11): return f'<text x="{x}" y="{y}" font-size="{sz}" text-anchor="{a}" fill="#222" font-family="sans-serif">{t}</text>'
fig=svg(460,260,'Hockey pitch diagram: a green rectangle 91.4 m by 55 m with 23-metre lines, a shooting circle of 14.63 m radius in front of each goal, goals 3.66 m wide, and a penalty spot 6.4 m from the goal line',
 '<rect x="60" y="40" width="340" height="180" fill="#5fa84d" stroke="#222" stroke-width="2"/><line x1="145" y1="40" x2="145" y2="220" stroke="#fff" stroke-width="2"/><line x1="230" y1="40" x2="230" y2="220" stroke="#fff" stroke-width="2"/><line x1="315" y1="40" x2="315" y2="220" stroke="#fff" stroke-width="2"/>'
 '<path d="M60 90 A55 55 0 0 1 60 190" fill="none" stroke="#fff" stroke-width="2"/><path d="M400 90 A55 55 0 0 0 400 190" fill="none" stroke="#fff" stroke-width="2"/>'
 '<rect x="46" y="125" width="14" height="30" fill="none" stroke="#222" stroke-width="2"/><rect x="400" y="125" width="14" height="30" fill="none" stroke="#222" stroke-width="2"/><circle cx="385" cy="140" r="3" fill="#fff"/>'
 '<line x1="60" y1="25" x2="400" y2="25" stroke="#222" marker-start="" /><line x1="415" y1="40" x2="415" y2="220" stroke="#222"/>'
 +tl(230,18,'91.4 m')+tl(440,135,'55 m')+tl(188,70,'22.9 m')+tl(92,142,'14.63 m','start',10)+tl(30,148,'3.66 m','middle',10)+tl(30,118,'2.19 m','middle',10)+tl(372,210,'6.4 m','middle',10))
s['figures']=[dict(id='hpe11-s133-fig1',svg=fig,caption='Hockey pitch (dimensions in metres)',captionUrdu='ہاکی کا میدان (پیمائش میٹر میں)',captionPashto='د هاکۍ میدان (اندازې په مترو)',labels=[],sourceGap=dict(note='Simplified coded redrawing of the green pitch diagram; positions of the dashed D-lines are not reproduced.'))]
s['sourceNote']='Printed page 131: chapter heading Hockey (ہاکی), playing-field dimensions (length, width, shooting circle, penalty stroke, penalty corner, corner), goal post (distance, height, board), and a pitch diagram. Yards are printed as “گز”. The page number “131” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 134 = printed 132
s=page(134,'u07','132','Hockey: flags, team, duration, captain','ہاکی: جھنڈے، ٹیم، کھیل کا دورانیہ، کپتان','هاکي: بیرغونه، ټیم، د لوبې موده، کپتان','hockey-2')
F=Flow(s)
H(s,'جھنڈے','Flags','بیرغونه')
P(s,[('ہر کونے پر اور درمیانی لائن سے تین فٹ کے فاصلے پر۔','At every corner and at a distance of three feet from the middle line.','په هر کونج کې او د منځني لاین له درې فټو واټن.')])
H(s,'ٹیم','Team','ټیم')
P(s,[('گراؤنڈ میں ایک وقت میں ایک ٹیم کے گیارہ کھلاڑیوں سے زیادہ نہیں کھیل سکتے۔ کھیل کے دوران جتنے کھلاڑی تبدیل کرنا چاہیں اجازت ہوگی۔ تبدیل شدہ کھلاڑی اس میچ میں دوبارہ حصہ لے سکتا ہے۔ کھلاڑی کی تبدیلی اجازت کے بغیر نہیں ہوگی۔ ایک وقت میں ایک ٹیم کا ایک ہی گول کیپر کھیل سکتا ہے۔','Not more than eleven players of a team can play on the ground at a time. During the game, as many players as one wants to change will be permitted. A substituted player can take part again in that match. A change of player will not be made without permission. At one time only one goalkeeper of a team can play.','په ګراونډ کې په یو وخت کې د یو ټیم له یوولسو لوبغاړو ډېر نشي لوبېدای. د لوبې په موده کې څومره لوبغاړي چې بدلول غواړي اجازه به وي. بدل شوی لوبغاړی بیا هم په دې لوبه کې برخه اخیستی شي. د لوبغاړي بدلون به له اجازې پرته نه وي. په یو وخت کې د یو ټیم یوازې یو ګول کیپر لوبېدای شي.')])
H(s,'کھیل کا دورانیہ','Duration of the Game','د لوبې موده')
P(s,[('پہلے یہ کھیل 35، 35 منٹ کے دو ہاف پر مشتمل ہوتا تھا۔ وقفہ 5 منٹ ہوتا تھا۔ وقفہ کے بعد ٹیمیں اطراف بدلتی تھیں۔ ستمبر 2014 سے ہاکی کا کھیل 15-15 منٹ کے چار کوارٹر پر مشتمل کر دیا گیا ہے پہلے اور دوسرے، تیسرے اور چوتھے کوارٹر میں 2-2 منٹ جبکہ دوسرے اور تیسرے کوارٹر میں 10 منٹ کی بریک ہوتی ہے۔ جس کو ہاف ٹائم کہتے ہیں۔','Earlier this game consisted of two halves of 35-35 minutes. The break was 5 minutes. After the break the teams used to change sides. From September 2014 the game of hockey has been made to consist of four quarters of 15-15 minutes; between the first and second, and third and fourth quarters there is a 2-2 minute break, while between the second and third quarters there is a 10-minute break, which is called half time.','مخکې دا لوبه د ۳۵–۳۵ دقیقو له دوو نیمایو جوړه وه. وقفه ۵ دقیقې وه. له وقفې وروسته ټیمونو اړخونه بدلول. د ۲۰۱۴ د سپتمبر نه د هاکۍ لوبه د ۱۵–۱۵ دقیقو له څلورو کوارټرونو جوړه شوې ده؛ په لومړي او دویم، دریم او څلورم کوارټر کې ۲–۲ دقیقې او په دویم او دریم کوارټر کې د ۱۰ دقیقو وقفه وي چې هاف ټایم ورته وایي.',GAP('The Urdu text of the break between quarters is internally awkward as printed (“پہلے اور دوسرے، تیسرے اور چوتھے … 2-2 منٹ”); kept as printed.'))])
H(s,'کپتان','Captain','کپتان')
P(s,[]+L([('ا۔ کپتان ٹاس جیت کر سائیڈ یا پاس کا انتخاب کرتا ہے۔','A. The captain, on winning the toss, chooses the side or the pass.','ا. کپتان ټاس ګټلو سره اړخ یا پاس غوره کوي.'),
('ب۔ کھیل کے دوران ہونے والے واقعات کا ذمہ دار ہوتا ہے۔','B. He is responsible for the events that take place during the game.','ب. د لوبې په موده کې د پېښو مسؤل وي.'),
('ج۔ کھلاڑیوں کو قانون پر چلنے کی ہدایت کرتا ہے۔','C. He instructs the players to follow the rules.','ج. لوبغاړو ته د قانون پر پلي کېدو لارښوونه کوي.')],'cap'))
F.fg(0)
F.done()
fig=svg(300,260,'A close view of a hockey stick and ball on the ground, with a group of players in dark green shirts running behind',
 '<rect width="300" height="260" fill="#cfd8dc"/><path d="M20 30 L210 170" stroke="#3e2723" stroke-width="12" stroke-linecap="round"/><path d="M210 170 q30 40 -10 55" stroke="#e53935" stroke-width="12" fill="none" stroke-linecap="round"/><circle cx="80" cy="215" r="28" fill="#fff" stroke="#999" stroke-width="2"/>'
 '<g fill="#1b5e20"><circle cx="190" cy="60" r="10"/><rect x="178" y="72" width="24" height="50" rx="8"/><circle cx="235" cy="85" r="10"/><rect x="223" y="97" width="24" height="50" rx="8"/><circle cx="270" cy="55" r="10"/><rect x="258" y="67" width="24" height="50" rx="8"/></g>')
s['figures']=[dict(id='hpe11-s134-fig1',svg=fig,caption='A hockey stick and ball, with players of a team behind',captionUrdu='ہاکی اسٹک اور گیند، پیچھے ٹیم کے کھلاڑی',captionPashto='د هاکۍ سټک او توپ، شاته د ټیم لوبغاړي',labels=[],sourceGap=dict(note='The original is a coloured photograph; replaced by a simplified coded SVG schematic (no raster image).'))]
s['sourceNote']='Printed page 132: flags, team, duration of the game (older and September-2014 formats) and captain, with a photograph of a hockey stick and players at the lower left. The page number “132” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 135 = printed 133
s=page(135,'u07','133','Hockey: rules; umpires and timekeeper; ball and stick','ہاکی: کھیل کے قواعد و ضوابط؛ امپائرز اور ٹائم کیپر؛ گیند اور سٹک','هاکي: د لوبې قواعد او ضوابط؛ امپایران او ټایم کیپر؛ توپ او سټک','hockey-3')
F=Flow(s)
H(s,'کھیل کے قواعد و ضوابط','Rules and Regulations of the Game','د لوبې قواعد او ضوابط')
H(s,'امپائرز اور ٹائم کیپر','Umpires and Timekeeper','امپایران او ټایم کیپر')
P(s,[]+L([
('1۔ کھیل کی نگرانی اور قوانین کے نفاذ کے ذمہ دار امپائر ہوتے ہیں۔','1. Umpires are responsible for supervising the game and enforcing the rules.','۱. د لوبې څارنې او د قوانینو د پلي کولو مسؤل امپایران وي.'),
('2۔ ہر امپائر اپنے نصف حصہ کا ذمہ دار ہوتا ہے۔','2. Each umpire is responsible for his half.','۲. هر امپایر د خپل نیمایي مسؤل وي.'),
('3۔ امپائر کسی بھی کھلاڑی کو ناشائستہ رویہ یا فاؤلز کی بنا پر عارضی یا مستقل طور پر نکال سکتا ہے۔','3. An umpire can send off any player temporarily or permanently on the basis of improper conduct or fouls.','۳. امپایر کوم هر لوبغاړی د ناوړه چلند یا فاولونو پر بنسټ لنډمهاله یا تلپاتې توګه ایستلی شي.'),
('4۔ کسی بھی ایسے معاملہ پر جہاں شک ہو دونوں امپائر مشورہ کر کے فیصلہ دیتے ہیں۔','4. On any matter where there is doubt, both umpires give a decision after consulting.','۴. په هر داسې معامله چې شک وي دواړه امپایران مشوره کولو سره پرېکړه کوي.'),
('5۔ امپائر کھیل کو شروع کرنے، وقفہ کرنے، ختم کرنے اور کھیل کے دوران ضابطہ شکنی کرنے پر وِسل کرتا ہے۔','5. The umpire whistles to start the game, to take a break, to end it, and on a breach of rules during play.','۵. امپایر د لوبې د پیلولو، وقفې، پای ته رسولو او د لوبې په موده کې د ضابطې ماتولو پر مهال سیټۍ وهي.'),
('6۔ کھلاڑی کو وارننگ کا ریکارڈ رکھتا ہے۔','6. He keeps a record of warnings to a player.','۶. د لوبغاړي د خبرتیا ثبت ساتي.'),
('7۔ امپائر کھیل کی ہار جیت کا فیصلہ دیتا ہے۔','7. The umpire decides the win or loss of the game.','۷. امپایر د لوبې د ګټلو او بایللو پرېکړه کوي.'),
('8۔ امپائر کا فیصلہ حتمی ہوتا ہے۔','8. The umpire’s decision is final.','۸. د امپایر پرېکړه حتمي وي.'),
('9۔ کھیل شروع ہونے کے ساتھ ہی ٹائم کیپر زوقت کا حساب رکھتا ہے۔','9. As soon as the game starts, the timekeeper keeps account of time.','۹. د لوبې له پیلېدو سره سم ټایم کیپر د وخت حساب ساتي.',),
('10۔ 35 منٹ پورے ہونے پر امپائر کو بتاتا ہے۔','10. On completion of 35 minutes he informs the umpire.','۱۰. د ۳۵ دقیقو بشپړېدو پر مهال امپایر ته خبر ورکوي.'),
('11۔ ضائع شدہ وقت کا حساب رکھتا ہے اور اسی حصہ میں شامل کرتا ہے۔','11. He keeps a record of lost time and adds it to the same part.','۱۱. د ضایع شوي وخت حساب ساتي او په همدې برخه کې یې شاملوي.')],'um'))
H(s,'گیند اور سٹک','Ball and Stick','توپ او سټک')
P(s,[]+L([
('(ا) گیند سفید رنگ کے پلاسٹک کا بنا ہوتا ہے جس کے اندر کارک ہوتا ہے۔ اس کا وزن 5.5 اونس سے 5.7 اونس ہوتا ہے۔ محیط تقریباً 9 انچ ہوتا ہے۔','(a) The ball is made of white plastic with cork inside. Its weight is 5.5 ounces to 5.7 ounces. The circumference is about 9 inches.','(الف) توپ د سپین رنګه پلاستیک جوړ وي چې دننه یې کارک وي. وزن یې ۵.۵ اونس نه تر ۵.۷ اونس وي. محیط یې شاوخوا ۹ انچه وي.'),
('(ب) سٹک لکڑی کی بنی ہوتی ہے جس کا ایک سرا مڑا ہوا اور چپٹا ہوتا ہے۔ اس کا وزن 12 اونس سے 28 اونس تک ہوتا ہے۔ سٹک ہر حال میں 2 انچ قطر کے رنگ سے گزرنی چاہیے۔','(b) The stick is made of wood, one end of which is curved and flat. Its weight is from 12 ounces to 28 ounces. The stick should in every case pass through a ring of 2 inches diameter.','(ب) سټک د لرګي جوړ وي چې یو سر یې کږ او پلن وي. وزن یې له ۱۲ اونس نه تر ۲۸ اونس پورې وي. سټک په هر حال کې باید د ۲ انچه قطر له حلقې تېر شي.')],'bs'))
F.fg(0)
F.done()
fig=svg(220,300,'A hockey stick shown diagonally: a long wooden shaft with a black grip near the bottom and a red curved head at the lower left',
 '<line x1="190" y1="20" x2="80" y2="230" stroke="#c9a06a" stroke-width="10" stroke-linecap="round"/><line x1="105" y1="185" x2="85" y2="225" stroke="#111" stroke-width="16" stroke-linecap="round"/><path d="M80 230 q-45 20 -60 45 q10 20 40 5 q25 -15 35 -35" fill="#e53935" stroke="#b71c1c" stroke-width="3"/>')
s['figures']=[dict(id='hpe11-s135-fig1',svg=fig,caption='A hockey stick',captionUrdu='ہاکی سٹک',captionPashto='د هاکۍ سټک',labels=[],sourceGap=dict(note='The original is a coloured picture; replaced by a simplified coded SVG schematic (no raster image).'))]
s['sourceNote']='Printed page 133: Rules and Regulations of the Game: umpires and timekeeper (items 1–11), and the ball and stick, with a picture of a hockey stick at the left. The page number “133” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
