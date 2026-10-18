from hpehelp import *
def P(s,rows,pre='p'):
    for (ur,en,ps,*m) in rows: add(s,f'{pre}{len(s["paras"])+1}',en,ur,ps,**(m[0] if m else {}))
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def Q(s,ur,en,ps,u='u07',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'hpe11-{u}-q',tab='exercise',**k)
def O(s,ur,en,ps,u='u07'): add(s,f'o{len(s["paras"])+1}',en,ur,ps,role='option',exerciseId=f'hpe11-{u}-q',tab='exercise')
GAP=lambda t:dict(sourceGap=dict(note=t))
NOTE=' English and Pashto are our translations (need native review); watermark and footer strip excluded.'
c=cell
def L(items,g):
    return [(a,b,c_,dict(listGroup=g)) for a,b,c_ in items]
def MC(s,q,opts):
    Q(s,*q)
    for o in opts: O(s,*o)
# scan 81 = printed 79 (figure)
s=page(81,'u07','79','Shot put: sector and circle diagrams; rules 1–3','شاٹ پٹ: سیکٹر اور دائرے کے خاکے؛ قوانین 1–3','شاټ پټ: د سکتور او دایرې انځورونه؛ قوانین ۱–۳','shotput-2')
F=Flow(s)
F.fg(0)
H(s,'شاٹ پٹ کے قوانین:','Rules of Shot Put:','د شاټ پټ قوانین:')
P(s,[]+L([('1۔ باری کی ترتیب قرعہ اندازی سے دی جائے گی۔','1. The order of turns will be given by draw.','۱. د نوبت ترتیب په قرعه ورکول کېږي.'),('2۔ 8 سے کم کھلاڑی ہوں تو 6-6 کوششیں دی جائیں گی۔','2. If there are fewer than 8 players, 6-6 attempts will be given.','۲. که له ۸ کم لوبغاړي وي نو ۶–۶ هڅې ورکول کېږي.'),('3۔ 8 سے زیادہ کھلاڑی ہوں تو پہلے 3-3 کوششیں دی جائیں گی۔ پھر 8 بہترین کھلاڑی منتخب کر کے 3-3 کوششیں دی جائیں گی۔','3. If there are more than 8 players, 3-3 attempts will first be given. Then 8 best players will be selected and 3-3 attempts will be given.','۳. که له ۸ زیات لوبغاړي وي نو لومړی ۳–۳ هڅې ورکول کېږي. بیا ۸ غوره لوبغاړي ټاکلو سره ۳–۳ هڅې ورکول کېږي.')],'ru'))
F.done()
fig=svg(520,400,'Plan of the shot-put circle with dimensions: sector lines at 34.92 degrees, circle 2.135 m in diameter, 90 degrees, 50 mm and 75 cm lines; and a second perspective drawing with stop board dimensions 1.22 m, 11.2 cm, 10.2 cm and 5 cm',
  '<line x1="260" y1="10" x2="260" y2="210" stroke="#555" stroke-dasharray="3 3"/><line x1="180" y1="30" x2="228" y2="140" stroke="#222" stroke-width="3"/><line x1="340" y1="30" x2="294" y2="140" stroke="#222" stroke-width="3"/><circle cx="260" cy="190" r="56" fill="none" stroke="#222" stroke-width="2"/>'+
  T(260,55,'34.92°',11)+'<line x1="170" y1="190" x2="370" y2="190" stroke="#222" stroke-width="3"/>'+T(222,188,'90°',11)+T(252,215,'2.135m',11)+T(120,180,'50mm',10)+T(130,212,'75cm',10)+
  '<ellipse cx="190" cy="320" rx="120" ry="40" fill="none" stroke="#222" stroke-width="2"/><rect x="290" y="296" width="14" height="20" fill="#555"/>'+T(230,320,'34.92°',11)+T(130,325,'2.135m',11)+T(340,284,'1.22m',11)+T(360,304,'11.2cm',11)+T(360,322,'10.2cm',11)+T(380,340,'5cm',11)+T(210,372,'75cm',11)+T(180,388,'5cm',11))
s['figures']=[dict(id='hpe11-s081-fig1',svg=fig,caption='Shot-put circle and sector: 34.92°, 90°, 2.135 m, 50 mm, 75 cm; stop board 1.22 m, 11.2 cm, 10.2 cm, 5 cm',captionUrdu='شاٹ پٹ کا دائرہ اور سیکٹر: 34.92°، 90°، 2.135 میٹر، 50 ملی میٹر، 75 سینٹی میٹر؛ سٹاپ بورڈ 1.22 میٹر، 11.2، 10.2، 5 سینٹی میٹر',captionPashto='د شاټ پټ دایره او سکتور: ۳۴.۹۲°، ۹۰°، ۲.۱۳۵ متره، ۵۰ ملي متره، ۷۵ سانتي متره؛ سټاپ بورډ ۱.۲۲ متره، ۱۱.۲، ۱۰.۲، ۵ سانتي متره',labels=[],sourceGap=dict(note='Simplified coded schematic of the two printed diagrams; the dimension labels (printed in English) are reproduced but the geometry is only indicative.'))]
s['sourceNote']='Printed page 79: two technical diagrams of the shot-put circle (top view and perspective with stop board) and rules 1–3.'+NOTE
s['vocabulary']={}
save(s)
# scan 82 = printed 80 (figure)
s=page(82,'u07','80','Shot put: rules 4–15; fouls 1–5','شاٹ پٹ: قوانین 4–15؛ فاؤلز 1–5','شاټ پټ: قوانین ۴–۱۵؛ فاولونه ۱–۵','shotput-3')
F=Flow(s)
P(s,[]+L([('4۔ ہر کھلاڑی کو چست نمبر دیا جائے گا۔','4. Every player will be given a bib number.','۴. هر لوبغاړي ته چست نمبر ورکول کېږي.'),('5۔ ہر کھلاڑی کو اس کی بہترین کوشش کا فائدہ دیا جائے گا۔','5. Every player will be given the benefit of his best attempt.','۵. هر لوبغاړي ته د هغه د غوره هڅې ګټه ورکول کېږي.'),('6۔ کھلاڑی اس وقت تک دائرہ میں رہے گا جب تک گولہ زمین پر نہ گرے۔','6. The player will remain in the circle until the shot falls on the ground.','۶. لوبغاړی تر هغه وخت پورې په دایره کې پاتې کېږي تر څو چې ګولۍ په ځمکه ونه لوېږي.'),('7۔ ہر کھلاڑی اپنی باری پر گولہ پھینکے گا۔','7. Every player will throw the shot on his own turn.','۷. هر لوبغاړی په خپل نوبت ګولۍ غورځوي.'),('8۔ نام پکارنے کے 1 منٹ کے اندر باری لینی ہو گی۔','8. The turn must be taken within 1 minute of the name being called.','۸. د نوم اخیستو له ۱ دقیقې دننه نوبت اخیستل پکار دي.'),('9۔ انتظامیہ کا مہیا کردہ گولہ استعمال ہوگا۔','9. The shot provided by the administration will be used.','۹. د ادارې برابره شوې ګولۍ کارول کېږي.'),('10۔ وہی کوشش درست شمار ہوگی جو بغیر فاؤل کیے سیکٹر کے اندر گرے۔','10. Only that attempt will be counted valid which falls inside the sector without a foul.','۱۰. یوازې هغه هڅه سمه شمېرل کېږي چې پرته له فاول د سکتور دننه ولوېږي.'),('11۔ ہر کوشش کی پیمائش درج کی جائے گی۔','11. The measurement of every attempt will be recorded.','۱۱. د هرې هڅې اندازه ثبتېږي.'),('12۔ اگر کوئی کھلاڑی بیک وقت فیلڈ اور ٹریک ایونٹ میں حصہ لے رہا ہو تو ریفری کی اجازت سے پہلے ٹریک ایونٹ مکمل کر سکتا ہے۔','12. If a player is taking part in a field and a track event at the same time, he can complete the track event first with the referee’s permission.','۱۲. که کوم لوبغاړی په یو وخت په فیلډ او ټریک ایونټ کې برخه اخلي نو د ریفري په اجازه لومړی ټریک ایونټ بشپړولای شي.'),('13۔ گولہ پھینکنے کے بعد دائرے کے پچھلے نصف حصہ سے باہر نکلے گا۔','13. After throwing the shot he will leave from the rear half of the circle.','۱۳. ګولۍ غورځولو وروسته د دایرې له شاتنۍ نیمایي برخې نه وځي.'),('14۔ کھلاڑی کوئی ایسی چیز استعمال نہیں کر سکتا جو گولہ پھینکنے میں مدد دے۔','14. A player cannot use anything that helps in throwing the shot.','۱۴. لوبغاړی کومه داسې شی نشي کارولای چې د ګولۍ غورځولو کې مرسته وکړي.'),('15۔ گولہ کندھے کی لائن کے اوپر ایک ہاتھ سے پھینکا جائے گا۔','15. The shot will be thrown above the line of the shoulder with one hand.','۱۵. ګولۍ د اوږې د کرښې پورته په یو لاس غورځول کېږي.')],'ru'))
H(s,'فاؤلز:','Fouls:','فاولونه:')
P(s,[]+L([('1۔ گولہ سیکٹر سے باہر یا سیکٹر کی لائن پر گرے۔','1. The shot falls outside the sector or on the sector line.','۱. ګولۍ د سکتور بهر یا د سکتور په کرښه ولوېږي.'),('2۔ سٹاپ بورڈ پر یا آگے پاؤں چلا جائے۔','2. The foot goes onto or beyond the stop board.','۲. پښه په سټاپ بورډ یا مخکې ولاړه شي.'),('3۔ دائرہ کے باہر زمین کو چھونا۔','3. Touching the ground outside the circle.','۳. د دایرې بهر ځمکې ته لمس کول.'),('4۔ کندھے کی لائن سے نیچے لا کر گولہ پھینکنا۔','4. Throwing the shot by bringing it below the line of the shoulder.','۴. د اوږې له کرښې ښکته راوړلو سره ګولۍ غورځول.'),('5۔ بغیر اپنی باری اور چست نمبر کے پھینکنا۔','5. Throwing without one’s own turn and bib number.','۵. پرته له خپل نوبت او چست نمبر غورځول.')],'fl'))
F.fg(0)
F.done()
fig=svg(300,260,'A shot-putter in a crouched throwing stance in the circle on a pink surface, shot held at the neck, free arm extended forward',
  '<rect x="0" y="180" width="300" height="80" fill="#f48fb1"/><ellipse cx="150" cy="230" rx="110" ry="24" fill="none" stroke="#fff" stroke-width="3"/><circle cx="130" cy="40" r="18" fill="#6d4c41"/><path d="M130 58 l10 60 M132 66 l70 -10 M132 70 l-40 8" stroke="#e64a19" stroke-width="12" fill="none" stroke-linecap="round"/><path d="M138 120 l-30 70 M138 120 l34 66" stroke="#222" stroke-width="12" stroke-linecap="round"/><circle cx="96" cy="76" r="9" fill="#1565c0"/>')
s['figures']=[dict(id='hpe11-s082-fig1',svg=fig,caption='Shot-putter in the throwing stance',captionUrdu='گولہ پھینکنے کی پوزیشن میں کھلاڑی',captionPashto='د ګولۍ غورځولو په موقعیت کې لوبغاړی',labels=[],sourceGap=dict(note='Simplified coded redrawing of the coloured illustration.'))]
s['sourceNote']='Printed page 80: shot-put rules 4–15 and fouls 1–5 with an illustration of the throwing stance.'+NOTE
s['vocabulary']={}
save(s)
# scan 83 = printed 81
s=page(83,'u07','81','Shot put: fouls 6–8; throwing skills (grip, standing throw, gliding, delivery)','شاٹ پٹ: فاؤلز 6–8؛ گولہ پھینکنے کی مہارتیں','شاټ پټ: فاولونه ۶–۸؛ ګولۍ غورځولو مهارتونه','shotput-4')
F=Flow(s)
P(s,[]+L([('6۔ گولہ کے زمین پر گرنے سے پہلے سیکٹر چھوڑ دینا۔','6. Leaving the circle before the shot falls on the ground.','۶. د ګولۍ د ځمکې په لوېدو نه مخکې سکتور پرېښودل.'),('7۔ گولہ پھینکنے کے بعد سیکٹر کو آگے سے کراس کرنا۔','7. Crossing the sector from the front after throwing the shot.','۷. د ګولۍ غورځولو وروسته سکتور له مخې نه تېرول.'),('8۔ ممنوعہ ادویات استعمال کرنا۔','8. Using prohibited drugs.','۸. منع شوي درمل کارول.')],'fl'))
H(s,'گولہ پھینکنے کی مہارتیں:','Skills of Throwing the Shot:','د ګولۍ غورځولو مهارتونه:')
H(s,'گرفت:','Grip:','نیونه:')
P(s,[('گولہ انگلیوں کے پوروں سے پکڑا جائے گولہ کندھے کی لائن پر ہو اور گردن کے ساتھ لگا ہوا ہو۔','The shot should be held with the fingertips; the shot should be on the line of the shoulder and touching the neck.','ګولۍ د ګوتو په څوکو ونیول شي ګولۍ د اوږې په کرښه وي او له غاړې سره لګېدلې وي.')])
H(s,'کھڑے کھڑے پھینکنا:','Throwing While Standing:','ولاړ ولاړ غورځول:')
P(s,[('ابتدائی مشق کے طور پر گولے کو کھڑے کھڑے پھینکیں۔ بازو کو اوپر کی طرف سیدھا کرتے ہوئے آگے کی طرف پھیلائیں۔','As initial practice throw the shot while standing. Extend the arm forward, straightening it upwards.','د لومړنۍ تمرین په توګه ګولۍ ولاړ ولاړ وغورځوئ. لاس پورته لوري ته سیده کولو سره مخکې لوري ته وغځوئ.')])
H(s,'گلائیڈ نگ:','Gliding:','ګلایډنګ:')
P(s,[('گولہ پھینکتے وقت دائرے میں کھڑے اتھلیٹ کی کمر سیکٹر کی طرف، دایاں پاؤں آگے، بایاں پاؤں پیچھے، کمر جھکا کر اور چھاتی اٹھا کر گھڑی کے مخالف سمت (Anticlock wise) گھومتے ہوئے گولے کو سیکٹر کی طرف پھینکنے کو گلائیڈ نگ کہتے ہیں۔','At the time of throwing the shot, the athlete standing in the circle with his back towards the sector, the right foot forward and the left foot behind, bending the back and raising the chest and turning anticlockwise (Anticlock wise), throwing the shot towards the sector is called gliding.','د ګولۍ د غورځولو په وخت کې په دایره ولاړ اتلیټ ملا د سکتور لوري ته، ښي پښه مخکې، کیڼه پښه شاته، ملا کږولو او سینه پورته کولو سره د ګړۍ د مخالف لوري (Anticlock wise) ګرځېدو سره ګولۍ د سکتور لوري ته غورځول ګلایډنګ بلل کېږي.')])
H(s,'گولہ پھینکنا (Delivery):','Throwing the Shot (Delivery):','ګولۍ غورځول (Delivery):')
P(s,[('گلائیڈ کے مرحلے کے اختتام پر دائیں اور بائیں پاؤں کے زمین پر لگنے اور گلائیڈ سے حاصل کردہ قوت کی حرکت سے پھینکنے کا عمل شروع ہوتا ہے۔ دائیں ٹانگ اور بائیں بازو کے باہمی پھیلاؤ سے پھینکنے کا عمل شروع کرنا چاہیے۔ بائیں بازو کو چھاتی سے دور رکھیں اور اوپر اٹھائیں۔ کلائی کہنی سے اوپر اور گولہ پھینکتے وقت جسم پوری طرح اوپر کی جانب پھیلا ہو اور توازن کو قائم رکھا جائے۔','At the end of the glide stage, as the right and left feet touch the ground, the action of throwing begins with the movement of force gained from the glide. The action of throwing should begin with the mutual extension of the right leg and the left arm. Keep the left arm away from the chest and raise it. The wrist should be above the elbow, and at the time of throwing the shot the body should be fully extended upwards and balance should be maintained.','د ګلایډ د پړاو په پای کې د ښي او کیڼې پښې په ځمکه لګېدو او د ګلایډ نه ترلاسه شوي ځواک په حرکت سره د غورځولو بهیر پیلېږي. د ښي ښنګر او کیڼ لاس په متقابل غځېدو سره د غورځولو بهیر پیل کول پکار دي. کیڼ لاس له سینې لرې وساتئ او پورته یې کړئ. مړوند له څنګلې پورته او د ګولۍ د غورځولو په وخت بدن بشپړ پورته لوري ته غځول شوی وي او توازن وساتل شي.')])
F.done()
s['sourceNote']='Printed page 81: shot-put fouls 6–8 and the four skills of throwing (grip, standing throw, gliding, delivery); the lower part of the page is blank.'+NOTE
s['vocabulary']={}
save(s)
# scan 84 = printed 82 (figure and table)
s=page(84,'u07','82','Shot put: the nine stages of the throw; score sheet','شاٹ پٹ: پھینکنے کے نو مراحل؛ سکور شیٹ','شاټ پټ: د غورځولو نهه پړاوونه؛ سکور شیټ','shotput-5')
F=Flow(s)
F.fg(0)
H(s,'سکور شیٹ:','Score Sheet:','سکور شیټ:')
F.tb(0)
P(s,[('نوٹ: x کا نشان ناکامی کو ظاہر کرتا ہے۔','Note: the sign x shows a failure.','یادونه: د x نښه ناکامي ښيي.',GAP('The score table prints heights in mixed feet-and-inches notation and a few cells have printing irregularities; they are kept as printed.'))])
F.done()
def pose(x,y,n,k):
    return (f'<circle cx="{x}" cy="{y}" r="9" fill="#fff" stroke="#333"/><path d="M{x} {y+9} l{k} 34 l-8 30 M{x} {y+16} l22 {10-k}" stroke="#333" stroke-width="3" fill="none"/>'+T(x+4,y-14,str(n),12))
fig=svg(520,340,'Nine stages of the shot put shown as stick figures in two rows: stages 4, 3, 2, 1 in the top row from left to right and stages 5 to 9 in the lower row',
  '<rect x="10" y="10" width="500" height="150" fill="none" stroke="#333"/><rect x="10" y="175" width="500" height="150" fill="none" stroke="#333"/>'+
  ''.join(pose(x,50,n,k) for x,n,k in [(70,4,2),(190,3,-4),(310,2,-8),(430,1,6)])+
  ''.join(pose(x,215,n,k) for x,n,k in [(50,5,-6),(150,6,-2),(250,7,2),(350,8,4),(450,9,-5)]))
s['figures']=[dict(id='hpe11-s084-fig1',svg=fig,caption='Shot put: the nine numbered stages of the throw (1–9)',captionUrdu='شاٹ پٹ: پھینکنے کے نو نمبر والے مراحل (1–9)',captionPashto='شاټ پټ: د غورځولو نهه شمېرلي پړاوونه (۱–۹)',labels=[],sourceGap=dict(note='Simplified coded stick-figure schematic of the two framed rows of line drawings; the original shows the throw in detail with the stages numbered 4,3,2,1 and 5–9.'))]
rows=[('1','ماجد','Majid','','','','35\'.6"','','',''),('2','طارق','Tariq','30\'.30"','29\'.4"','3\'2.4"','','35\'.2','34\'.10"',''),('3','صائم','Saim','29\'.6"','','34\'.2"','33\'.10"','32\'.9"','33\'.10"',''),('4','جاوید','Javed','28\'.10"','30\'.5"','','31\'.9"','34\'.10"','34\'.8"',''),('5','سلطان','Sultan','31\'.3"','30\'.6"','','34\'.7"','33\'.9"','32\'.6"',''),('6','خالد','Khalid','','31\'.6"','35\'.1"','','28\'.7\'','34.2"','')]
pos={'1':'Ist','2':'IInd','6':'IIIrd'}
def cl(v): return c('×') if v=='' else c(v)
s['tables']=[table('Score sheet of a shot-put competition (six players, attempts I–VI)','شاٹ پٹ مقابلے کی سکور شیٹ (چھ کھلاڑی، کوششیں I–VI)','د شاټ پټ د سیالۍ سکور شیټ (شپږ لوبغاړي، هڅې I–VI)',[c('No.','نمبر','شمېره'),c('Name','نام','نوم'),c('I'),c('II'),c('III'),c('IV'),c('V'),c('VI'),c('Position','پوزیشن','موقعیت')],[[c(r[0]),c(r[2],r[1],r[2]),cl(r[3]),cl(r[4]),cl(r[5]),cl(r[6]),cl(r[7]),cl(r[8]),c(pos.get(r[0],''))] for r in rows])]
s['sourceNote']='Printed page 82: nine stick-figure stages of the throw and a score sheet of six players with six attempts each (× marks a failure). The player names are Urdu; their English forms are transliterations of the Urdu names.'+NOTE
s['vocabulary']={}
save(s)
# scan 85 = printed 83
s=page(85,'u07','83','Exercise questions: shot put (1–6)','مشقی سوالات: شاٹ پٹ (1–6)','تمرین پوښتنې: شاټ پټ (۱–۶)','ex7c')
F=Flow(s)
H(s,'مشقی سوالات','Exercise Questions','تمرین پوښتنې')
H(s,'1۔ موزوں جواب منتخب کر کے لکھیں۔','1. Select the suitable answer and write it.','۱. مناسب ځواب وټاکئ او ولیکئ.')
MC(s,('i۔ شاٹ پٹ میں مردوں کے لیے گولے کا وزن ________ کلو گرام ہوتا ہے۔','i. In shot put the weight of the shot for men is ________ kilograms.','i. په شاټ پټ کې د نارینه وو لپاره د ګولۍ وزن ________ کیلوګرامه وي.'),[('(الف) 4.265','(a) 4.265','(الف) ۴.۲۶۵'),('(ب) 5.265','(b) 5.265','(ب) ۵.۲۶۵'),('(ج) 6.265','(c) 6.265','(ج) ۶.۲۶۵'),('(د) 7.265','(d) 7.265','(د) ۷.۲۶۵')])
MC(s,('ii۔ شاٹ پٹ میں عورتوں کے لیے گولہ کا وزن ________ کلو گرام ہوتا ہے۔','ii. In shot put the weight of the shot for women is ________ kilograms.','ii. په شاټ پټ کې د ښځو لپاره د ګولۍ وزن ________ کیلوګرامه وي.'),[('(الف) 4','(a) 4','(الف) ۴'),('(ب) 2','(b) 2','(ب) ۲'),('(ج) 6','(c) 6','(ج) ۶'),('(د) 8','(d) 8','(د) ۸')])
MC(s,('iii۔ شاٹ پٹ میں 8 کھلاڑی ہوں تو ________ کوششیں دی جاتی ہیں۔','iii. In shot put if there are 8 players, ________ attempts are given.','iii. په شاټ پټ کې که ۸ لوبغاړي وي نو ________ هڅې ورکول کېږي.'),[('(الف) 3','(a) 3','(الف) ۳'),('(ب) 4','(b) 4','(ب) ۴'),('(ج) 2','(c) 2','(ج) ۲'),('(د) 6','(d) 6','(د) ۶')])
MC(s,('iv۔ شاٹ پٹ میں دائرے کا قطر ________ میٹر ہوتا ہے۔','iv. In shot put the diameter of the circle is ________ metres.','iv. په شاټ پټ کې د دایرې قطر ________ متره وي.'),[('(الف) 2.135','(a) 2.135','(الف) ۲.۱۳۵'),('(ب) 2.75','(b) 2.75','(ب) ۲.۷۵'),('(ج) 2.99','(c) 2.99','(ج) ۲.۹۹'),('(د) 3.135','(d) 3.135','(د) ۳.۱۳۵')])
MC(s,('v۔ شاٹ پٹ میں سیکٹر کا زاویہ ________ درجہ ہوتا ہے۔','v. In shot put the angle of the sector is ________ degrees.','v. په شاټ پټ کې د سکتور زاویه ________ درجې وي.'),[('(الف) 40°','(a) 40°','(الف) ۴۰°'),('(ب) 35°','(b) 35°','(ب) ۳۵°'),('(ج) 34.92°','(c) 34.92°','(ج) ۳۴.۹۲°'),('(د) 35.92°','(d) 35.92°','(د) ۳۵.۹۲°')])
MC(s,('vi۔ شاٹ پٹ میں سٹاپ بورڈ کی لمبائی ________ میٹر ہوتی ہے۔','vi. In shot put the length of the stop board is ________ metres.','vi. په شاټ پټ کې د سټاپ بورډ اوږدوالی ________ متره وي.'),[('(الف) 1.22','(a) 1.22','(الف) ۱.۲۲'),('(ب) 2.12','(b) 2.12','(ب) ۲.۱۲'),('(ج) 3.22','(c) 3.22','(ج) ۳.۲۲'),('(د) 2.76','(d) 2.76','(د) ۲.۷۶')])
F.done()
s['sourceNote']='Printed page 83: exercise questions of the shot-put section — multiple-choice items i–vi. The footer strip is cropped at the foot of the scan.'+NOTE
s['vocabulary']={}
save(s)
