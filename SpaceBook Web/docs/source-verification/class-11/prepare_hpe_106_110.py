from hpehelp import *
def P(s,rows,pre='p'):
    for (ur,en,ps,*m) in rows: add(s,f'{pre}{len(s["paras"])+1}',en,ur,ps,**(m[0] if m else {}))
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def Q(s,ur,en,ps,u='u07',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'hpe11-{u}-q',tab='exercise',**k)
def O(s,ur,en,ps,u='u07'): add(s,f'o{len(s["paras"])+1}',en,ur,ps,role='option',exerciseId=f'hpe11-{u}-q',tab='exercise')
GAP=lambda t:dict(sourceGap=dict(note=t))
NOTE=' English and Pashto are our translations (need native review); watermark and footer strip excluded.'
def L(items,g):
    return [(a,b,c_,dict(listGroup=g)) for a,b,c_ in items]
def MC(s,q,opts):
    Q(s,*q)
    for o in opts: O(s,*o)
# scan 106 = printed 104 (figures)
s=page(106,'u07','104','Volleyball skills: blocking, smashing','والی بال کی مہارتیں: بلاکنگ، سمیش کرنا','د والیبال مهارتونه: بلاکنګ، سمېش کول','volleyball-12')
F=Flow(s)
H(s,'4۔ بلاکنگ (Blocking)','4. Blocking (Blocking)','۴. بلاکنګ (Blocking)')
P(s,[('نیٹ کے نزدیک بال کو اوپر جمپ کرتے ہوئے روکنے کے عمل کو بلاکنگ کہتے ہیں۔ اس میں اگلی لائن کے کھلاڑی حصہ لیتے ہیں۔ ایک یا زیادہ کھلاڑی بیک وقت بال کو چھو سکتے ہیں۔ جب مخالف سمیش کرنے کی کوشش کرتا ہے تو اس لمحے دفاعی ٹیم کے اگلے کھلاڑی جمپ کر کے بال کو نیٹ عبور کرنے سے روکتے ہیں۔','The act of stopping the ball near the net, jumping up, is called blocking. Players of the front line take part in it. One or more players can touch the ball at the same time. When the opponent tries to smash, at that moment the front players of the defending team jump and stop the ball from crossing the net.','د جال سره نږدې توپ پورته ټوپ وهلو سره درولو عمل ته بلاکنګ وايي. پدې کې د مخکینۍ کرښې لوبغاړي برخه اخلي. یو یا ډېر لوبغاړي په یو وخت توپ لمسولای شي. کله چې مخالف سمېش کولو هڅه کوي نو پدې شېبه د دفاعي ټیم مخکینۍ لوبغاړي ټوپ وهلو سره توپ د جال له تېرېدو نه ساتي.',GAP('A colour photograph of players blocking at the net is not reproduced.'))])
H(s,'5۔ سمیش کرنا (Smashing)','5. Smashing (Smashing)','۵. سمېش کول (Smashing)')
P(s,[('جب بوسٹر بال ہوا میں اچھالے گا تو ایک کھلاڑی جس کی طرف بال اچھالا گیا ہو ہوا میں جمپ کرتے ہوئے نیٹ کے اوپر سے بال کو مخالف کورٹ میں مارے گا۔ اس عمل کو سمیش یا Spike کہتے ہیں۔ نیٹ کو ٹچ کرنا فاؤل ہے۔ سمیشر خیال رکھے کہ آگے بلاک بھی ہے لہٰذا بال کو اس طرح مارے کہ بلاک نہ ہو سکے یا اس طرح مارے کے بلاک کرنے والوں کے ہاتھ سے ٹچ ہو کر کورٹ سے باہر چلا جائے۔','When the booster tosses the ball in the air, a player towards whom the ball was tossed, jumping in the air, will hit the ball over the net into the opponent’s court. This act is called a smash or Spike. Touching the net is a foul. The smasher should keep in mind that there is also a block in front, so he should hit the ball so that it cannot be blocked, or so that, touching the hands of the blockers, it goes out of the court.','کله چې بوسټر توپ په هوا کې غورځوي نو یو لوبغاړی چې هغه لوري ته توپ غورځول شوی وي په هوا کې ټوپ وهلو سره د جال پورته نه توپ د مخالف په کورټ کې وهي. دې عمل ته سمېش یا Spike وايي. جال لمس کول فاول دی. سمېشر باید پام وساتي چې مخکې بلاک هم دی نو توپ داسې وهي چې بلاک نشي یا داسې وهي چې د بلاک کوونکو له لاسونو سره لګېدو سره له کورټ بهر لاړ شي.')])
F.fg(0)
F.fg(1)
F.done()
fig1=svg(360,200,'Two players at the net: a blocker jumping with raised hands to stop the ball, and an attacker in yellow hitting the ball from above; other players below',
  '<rect x="10" y="90" width="340" height="18" fill="#fff" stroke="#444" stroke-width="2"/>'+''.join(f'<line x1="{x}" y1="90" x2="{x}" y2="108" stroke="#999"/>' for x in range(20,350,12))+
  '<circle cx="110" cy="40" r="16" fill="#6d4c41"/><path d="M110 56 l0 50 M110 66 l-14 -40 M110 66 l28 -30" stroke="#f9a825" stroke-width="12" fill="none" stroke-linecap="round"/><circle cx="130" cy="14" r="12" fill="#fdd835" stroke="#555"/>'+
  '<circle cx="230" cy="70" r="16" fill="#6d4c41"/><path d="M230 86 l0 60 M230 96 l-20 -50 M230 96 l26 -40" stroke="#eee" stroke-width="12" fill="none" stroke-linecap="round"/><path d="M230 146 l-12 40 M230 146 l16 38" stroke="#e53935" stroke-width="12"/>')
fig2=svg(360,260,'A smasher in blue jumping at a net with his right arm raised to hit a volleyball above the net',
  ''.join(f'<line x1="{20+i*8}" y1="20" x2="{20+i*8}" y2="240" stroke="#444"/>' for i in range(12))+''.join(f'<line x1="20" y1="{20+i*16}" x2="110" y2="{20+i*16+10}" stroke="#444"/>' for i in range(14))+
  '<circle cx="150" cy="70" r="24" fill="#fff" stroke="#c2185b" stroke-width="3"/><circle cx="260" cy="150" r="18" fill="#6d4c41"/><path d="M260 166 l-20 70 M258 180 l-70 -100 M262 180 l40 40" stroke="#42a5f5" stroke-width="22" fill="none" stroke-linecap="round"/>')
s['figures']=[dict(id='hpe11-s106-fig1',svg=fig1,caption='Blocking at the net',captionUrdu='نیٹ پر بلاکنگ',captionPashto='په جال بلاکنګ',labels=[],sourceGap=dict(note='Simplified coded redrawing of the colour photograph.')),dict(id='hpe11-s106-fig2',svg=fig2,caption='Smashing: jumping with the arm raised to hit the ball over the net',captionUrdu='سمیش: جمپ کرتے ہوئے بازو اٹھا کر بال کو نیٹ کے اوپر سے مارنا',captionPashto='سمېش: ټوپ وهلو سره لاس پورته کولو سره توپ د جال پورته وهل',labels=[],sourceGap=dict(note='Simplified coded redrawing of the coloured illustration.'))]
s['sourceNote']='Printed page 104: the fourth and fifth volleyball skills (blocking and smashing) with a photograph and an illustration. The footer strip is intact.'+NOTE
s['vocabulary']={}
save(s)
# scan 107 = printed 105 (figure)
s=page(107,'u07','105','Volleyball skills: passing/setting (boosting)','والی بال کی مہارتیں: پاس بنانا (سیٹنگ / بوسٹنگ)','د والیبال مهارتونه: پاس جوړول (سیټنګ / بوسټنګ)','volleyball-13')
F=Flow(s)
H(s,'6۔ پاس بنانا (Setting/Boosting):','6. Making the Pass (Setting/Boosting):','۶. پاس جوړول (Setting/Boosting):')
P(s,[('جب دفاعی کھلاڑی بال کو اوپر اچھالے تو بوسٹر (Booster) دونوں ہاتھوں سے بال کو نیٹ کے اوپر اس طرح اچھالے کہ اس ٹیم کا دوسرا کھلاڑی جمپ کر کے بال کو مخالف کورٹ میں سمیش کر سکے۔ بوسٹر کبھی سامنے والے کبھی پیچھے والے کھلاڑی کی طرف بال اس طرح اچھالے کہ بلاکنگ کا موقع ہی نہ مل سکے۔ بوسٹر بال کو آئیڈیا بھی کر سکتا ہے یعنی خود ہی آہستہ سے بال کو مخالف کی طرف ڈاج دیتے ہوئے پھینک دے۔','When the defensive player tosses the ball up, the booster (Booster) with both hands should toss the ball over the net in such a way that another player of that team can jump and smash the ball into the opponent’s court. The booster should sometimes toss the ball towards the player in front, sometimes towards the one behind, in such a way that there is no opportunity of blocking at all. The booster can also use an idea (“Idea” as printed), that is, himself dodging, gently throw the ball towards the opponent.','کله چې دفاعي لوبغاړی توپ پورته غورځوي نو بوسټر (Booster) په دواړو لاسونو توپ د جال پورته داسې غورځوي چې د هغه ټیم بل لوبغاړی ټوپ وهلو سره توپ د مخالف په کورټ کې سمېش کړای شي. بوسټر کله مخکې والا او کله شاته والا لوبغاړي لوري ته توپ داسې غورځوي چې د بلاکنګ موقع ورته ونه مومي. بوسټر توپ ته آیډیا هم کولای شي یعنې پخپله ورو توپ د مخالف لوري ته ډاج ورکولو سره وغورځوي.',GAP('The scan prints “آئیڈیا” (idea) for the tactic of a gentle drop shot; kept as printed.'))])
F.fg(0)
F.done()
fig=svg(520,260,'Two panels of a volleyball player in a red shirt setting the ball above the head with both hands, with red arrows showing the upward direction of the ball and a forward arrow',
  '<g>'+''.join(f'<circle cx="{x}" cy="{y}" r="22" fill="#6d4c41"/><path d="M{x} {y+22} l0 80 M{x} {y+40} l-40 -50 M{x} {y+40} l50 -50" stroke="#e53935" stroke-width="26" fill="none" stroke-linecap="round"/><circle cx="{x}" cy="{y-80}" r="30" fill="#1a237e"/><path d="M{x-20} {y-84} q20 -10 40 0" stroke="#ffb74d" stroke-width="6" fill="none"/>' for x,y in [(130,130),(390,150)])+
  '<path d="M170 86 l10 -26 M420 40 l-8 20 M500 110 l-22 8" stroke="#e53935" stroke-width="4" fill="none"/></g>')
s['figures']=[dict(id='hpe11-s107-fig1',svg=fig,caption='Setting/boosting: the ball passed above the head with both hands',captionUrdu='پاس بنانا: دونوں ہاتھوں سے بال کو سر کے اوپر پاس کرنا',captionPashto='پاس جوړول: په دواړو لاسونو توپ د سر پورته پاس کول',labels=[lab('Setting/Boosting','پاس بنانا','پاس جوړول')],sourceGap=dict(note='Simplified coded redrawing of the two coloured illustrations of setting.'))]
s['sourceNote']='Printed page 105: the sixth volleyball skill (setting/boosting) with two illustrations. The page number “105” and the footer strip are partly cropped at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 108 = printed 106
s=page(108,'u07','106','Exercise questions: volleyball (1–7)','مشقی سوالات: والی بال (1–7)','تمرین پوښتنې: والیبال (۱–۷)','ex7f')
F=Flow(s)
H(s,'مشقی سوالات','Exercise Questions','تمرین پوښتنې')
H(s,'1۔ موزوں جواب منتخب کر کے لکھیں۔','1. Select the suitable answer and write it.','۱. مناسب ځواب وټاکئ او ولیکئ.')
MC(s,('i۔ والی بال میں سروس ایریا ________ میٹر ہوتا ہے۔','i. In volleyball the service area is ________ metres.','i. په والیبال کې سروس ایریا ________ متره وي.'),[('(الف) 3','(a) 3','(الف) ۳'),('(ب) 6','(b) 6','(ب) ۶'),('(ج) 9','(c) 9','(ج) ۹'),('(د) 1','(d) 1','(د) ۱')])
MC(s,('ii۔ والی بال میں اٹیک ایریا ________ میٹر ہوتا ہے۔','ii. In volleyball the attack area is ________ metres.','ii. په والیبال کې اټیک ایریا ________ متره وي.'),[('(الف) 3','(a) 3','(الف) ۳'),('(ب) 1','(b) 1','(ب) ۱'),('(ج) 2','(c) 2','(ج) ۲'),('(د) 6','(d) 6','(د) ۶')])
MC(s,('iii۔ والی بال کورٹ کی لمبائی ________ میٹر ہوتی ہے۔','iii. The length of a volleyball court is ________ metres.','iii. د والیبال کورټ اوږدوالی ________ متره وي.'),[('(الف) 9','(a) 9','(الف) ۹'),('(ب) 18','(b) 18','(ب) ۱۸'),('(ج) 12','(c) 12','(ج) ۱۲'),('(د) 20','(d) 20','(د) ۲۰')])
MC(s,('iv۔ والی بال میں ٹائم آؤٹ کا دورانیہ ________ سیکنڈ ہوتا ہے۔','iv. In volleyball the duration of a time-out is ________ seconds.','iv. په والیبال کې د ټایم آوټ موده ________ ثانیې وي.'),[('(الف) 5','(a) 5','(الف) ۵'),('(ب) 10','(b) 10','(ب) ۱۰'),('(ج) 20','(c) 20','(ج) ۲۰'),('(د) 30','(d) 30','(د) ۳۰')])
MC(s,('v۔ والی بال میں پانچویں سیٹ میں ________ پوائنٹ ہوتے ہیں۔','v. In volleyball in the fifth set there are ________ points.','v. په والیبال کې په پنځم سیټ کې ________ پوائنټونه وي.'),[('(الف) 21','(a) 21','(الف) ۲۱'),('(ب) 25','(b) 25','(ب) ۲۵'),('(ج) 20','(c) 20','(ج) ۲۰'),('(د) 15','(d) 15','(د) ۱۵')])
MC(s,('vi۔ والی بال کورٹ کی چوڑائی ________ میٹر ہوتی ہے۔','vi. The width of a volleyball court is ________ metres.','vi. د والیبال کورټ پلنوالی ________ متره وي.'),[('(الف) 9','(a) 9','(الف) ۹'),('(ب) 3','(b) 3','(ب) ۳'),('(ج) 18','(c) 18','(ج) ۱۸'),('(د) 6','(d) 6','(د) ۶')])
MC(s,('vii۔ والی بال کے ایک سیٹ میں ________ پوائنٹ ہوتے ہیں۔','vii. In one set of volleyball there are ________ points.','vii. د والیبال په یو سیټ کې ________ پوائنټونه وي.'),[('(الف) 21','(a) 21','(الف) ۲۱'),('(ب) 24','(b) 24','(ب) ۲۴'),('(ج) 15','(c) 15','(ج) ۱۵'),('(د) 25','(d) 25','(د) ۲۵')])
F.done()
s['sourceNote']='Printed page 106: exercise questions on volleyball, multiple-choice items i–vii (continued on the next page).'+NOTE
s['vocabulary']={}
save(s)
# scan 109 = printed 107
s=page(109,'u07','107','Exercise questions: volleyball (8–10) and descriptive questions','مشقی سوالات: والی بال (8–10) اور تفصیلی سوالات','تمرین پوښتنې: والیبال (۸–۱۰) او تشریحي پوښتنې','ex7g')
F=Flow(s)
MC(s,('viii۔ والی بال ٹیم میں ________ کھلاڑی ہوتے ہیں۔','viii. In a volleyball team there are ________ players.','viii. په والیبال ټیم کې ________ لوبغاړي وي.'),[('(الف) 11','(a) 11','(الف) ۱۱'),('(ب) 12','(b) 12','(ب) ۱۲'),('(ج) 9','(c) 9','(ج) ۹'),('(د) 7','(d) 7','(د) ۷')])
MC(s,('ix۔ والی بال میچ کے دوران ایک ٹیم کے ________ کھلاڑی کورٹ میں ہوتے ہیں۔','ix. During a volleyball match ________ players of a team are in the court.','ix. د والیبال لوبې په موده کې د یو ټیم ________ لوبغاړي په کورټ کې وي.'),[('(الف) 9','(a) 9','(الف) ۹'),('(ب) 6','(b) 6','(ب) ۶'),('(ج) 12','(c) 12','(ج) ۱۲'),('(د) 9','(d) 9','(د) ۹')])
MC(s,('x۔ والی بال میچ میں پوائنٹ برابر ہونے کی صورت میں ________ پوائنٹ کی برتری سے سیٹ جیتا جاتا ہے۔','x. In a volleyball match, in case of a tie in points, the set is won by a lead of ________ points.','x. د والیبال په لوبه کې د پوائنټونو د برابرۍ په صورت کې د ________ پوائنټ برتري سره سیټ ګټل کېږي.'),[('(الف) 1','(a) 1','(الف) ۱'),('(ب) 2','(b) 2','(ب) ۲'),('(ج) 3','(c) 3','(ج) ۳'),('(د) 4','(d) 4','(د) ۴')])
H(s,'2۔ درج ذیل سوالوں کے جواب لکھیں۔','2. Write answers to the following questions.','۲. د لاندې پوښتنو ځوابونه ولیکئ.')
for ur,en,ps in [('i۔ والی بال کورٹ بمعہ پیمائش بنائیں اور روٹیشن آرڈر ظاہر کریں۔','i. Draw the volleyball court with measurements and show the rotation order.','i. د والیبال کورټ د اندازو سره جوړ کړئ او روټېشن آرډر وښيئ.'),('ii۔ والی بال میں سروس اور بلاکنگ کے فاؤلز درج کریں۔','ii. List the fouls of service and blocking in volleyball.','ii. په والیبال کې د سروس او بلاکنګ فاولونه ولیکئ.'),('iii۔ والی بال میں پوائنٹ جیتنے کی وضاحت کریں۔','iii. Explain winning a point in volleyball.','iii. په والیبال کې د پوائنټ ګټلو توضیح وکړئ.')]: Q(s,ur,en,ps)
F.done()
s['sourceNote']='Printed page 107: exercise questions on volleyball, multiple-choice items viii–x and three descriptive questions; the lower part of the page is blank. In item ix the scan prints the same value 9 for options (a) and (d).'+NOTE
s['vocabulary']={}
save(s)
# scan 110 = printed 108 (figure)
s=page(110,'u07','108','Table tennis: table, ball and net measurements','ٹیبل ٹینس: میز، گیند اور نیٹ کی پیمائش','ټیبل ټینس: د میز، توپ او جال اندازې','tabletennis-1')
F=Flow(s)
H(s,'ٹیبل ٹینس','Table Tennis','ټیبل ټینس')
P(s,[]+L([('میز کی لمبائی: 9 فٹ یا 2.74 میٹر','Length of the table: 9 feet or 2.74 metres','د میز اوږدوالی: ۹ فوټه یا ۲.۷۴ متره'),('میز کی چوڑائی: 5 فٹ یا 1.52 میٹر','Width of the table: 5 feet or 1.52 metres','د میز پلنوالی: ۵ فوټه یا ۱.۵۲ متره'),('میز کی اونچائی: 2 فٹ 6 انچ یا 0.76 میٹر','Height of the table: 2 feet 6 inches or 0.76 metres','د میز لوړوالی: ۲ فوټه ۶ انچه یا ۰.۷۶ متره'),('گیند: سلولائیڈ (Celloloid) کا سفید یا پیلا گیند جس کا وزن 37 سے 39 گرین یا 2.40 سے 2.53 گرام اور محیط 4.133 انچ یا 10 سینٹی میٹر','Ball: a white or yellow celluloid (“Celloloid” as printed) ball whose weight is 37 to 39 grains or 2.40 to 2.53 grams and circumference 4.133 inches or 10 centimetres','توپ: د سلولایډ (Celloloid) سپین یا ژېړ توپ چې وزن یې ۳۷ نه تر ۳۹ ګرېنو یا ۲.۴۰ نه تر ۲.۵۳ ګرامو او محیط ۴.۱۳۳ انچه یا ۱۰ سانتي متره وي'),('نیٹ: لمبائی = 1.8 میٹر، چوڑائی 15 سینٹی میٹر','Net: length = 1.8 metres, width 15 centimetres','جال: اوږدوالی = ۱.۸ متره، پلنوالی ۱۵ سانتي متره')],'tt'))
F.fg(0)
F.done()
fig=svg(520,360,'A table-tennis table drawn in perspective with the net across the middle, and labels 274 cm for length, 152.5 cm for width, 76 cm for height and net overhang 15.25 cm; below it a net and a ball',
  '<polygon points="80,120 380,70 500,160 200,220" fill="#2e3b2d" stroke="#ccc" stroke-width="3"/>'+'<polygon points="238,80 262,70 340,190 316,200" fill="#222" stroke="#aaa"/>'+
  ''.join(f'<rect x="{x}" y="{y}" width="12" height="90" fill="#444"/>' for x,y in [(110,150),(230,200),(430,150),(330,190)])+
  T(180,70,'274cm',13)+T(470,100,'152.5cm',13,'start')+T(40,200,'76cm',13)+T(250,262,'Net overhang 15.25cm',13)+
  '<path d="M90 300 l140 -30 l0 50 l-140 30 Z" fill="#eee" stroke="#444"/><circle cx="400" cy="310" r="40" fill="#fff" stroke="#999" stroke-width="3"/>')
s['figures']=[dict(id='hpe11-s110-fig1',svg=fig,caption='Table-tennis table: 274 cm × 152.5 cm, height 76 cm, net overhang 15.25 cm; a net and a ball',captionUrdu='ٹیبل ٹینس کی میز: 274 × 152.5 سینٹی میٹر، اونچائی 76 سینٹی میٹر، نیٹ اوور ہینگ 15.25 سینٹی میٹر؛ نیٹ اور گیند',captionPashto='د ټیبل ټینس میز: ۲۷۴ × ۱۵۲.۵ سانتي متره، لوړوالی ۷۶ سانتي متره، د جال اوور هینګ ۱۵.۲۵ سانتي متره؛ جال او توپ',labels=[],sourceGap=dict(note='Simplified coded perspective sketch of the table with the English labels as printed (274cm, 152.5cm, 76cm, Net overhang 15.25cm); the photograph-like net and ball drawings are only indicated.'))]
s['sourceNote']='Printed page 108: table tennis — measurements of the table, ball and net with a perspective diagram. The ball’s brand marking is not reproduced.'+NOTE
s['vocabulary']={}
save(s)
