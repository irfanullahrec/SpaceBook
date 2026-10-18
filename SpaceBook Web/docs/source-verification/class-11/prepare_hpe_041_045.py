from hpehelp import *
def P(s,rows,pre='p'):
    for (ur,en,ps,*m) in rows: add(s,f'{pre}{len(s["paras"])+1}',en,ur,ps,**(m[0] if m else {}))
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
GAP=lambda t:dict(sourceGap=dict(note=t))
NOTE=' English and Pashto are our translations (need native review); watermark and footer strip excluded.'
MISS='The scans (JPG file numbers) skip from printed page 36 directly to printed page 39: printed pages 37 and 38, which hold the Chapter 5 (Biomechanics for Sports) opener and the start of the tennis skill, are not in the local source set.'
# scan 41 = printed 39 (figure)
s=page(41,'u05','39','Tennis: forehand drive (end), exercise and activity','ٹینس: فورہینڈ (اختتام)، ورزش اور سرگرمی','ټینس: فورهینډ (پای)، تمرین او فعالیت','tennis-1')
F=Flow(s)
P(s,[('… کر کے جسم کا توازن برقرار رکھتے ہوئے شٹل کو تیزی کے ساتھ سیدھے ہاتھ سے مخالف کے کورٹ میں گرائیں۔ شٹل کی پوزیشن کو مدنظر رکھتے ہوئے قوت کا اصول استعمال کریں۔','… and, keeping the balance of the body, drop the shuttle quickly with the right hand into the opponent’s court. Use the principle of force keeping in view the position of the shuttle.','… کولو سره د بدن توازن ساتلو سره شټل په ګړندیتوب سره په ښي لاس د مخالف کورټ ته راوغورځوئ. د شټل د موقعیت په پام کې نیولو سره د ځواک اصول وکاروئ.',GAP('The first words of this sentence are on printed page 38, which is missing from the source set. '+MISS))])
F.fg(0)
H(s,'ورزش (Exercise):','Exercise:','تمرین (Exercise):')
P(s,[('اس مہارت میں بہتری لانے کے لیے مندرجہ ذیل ورزشیں ضروری ہیں۔','To bring improvement in this skill the following exercises are necessary.','پدې مهارت کې د ښه والي راوستو لپاره لاندې تمرینونه اړین دي.'),
('i۔ کھڑے کھڑے جمپ کرنا۔','i. Jumping while standing.','i. ولاړ ولاړ ټوپ وهل.',dict(listGroup='ex')),
('ii۔ پہلو کی جانب جھکنا۔','ii. Bending to the side.','ii. څنګ لوري ته کږېدل.',dict(listGroup='ex')),
('iii۔ گھٹنوں پر توازن قائم کرنا۔','iii. Establishing balance on the knees.','iii. په زنګنونو توازن ټینګول.',dict(listGroup='ex')),
('iv۔ فرنٹ رول کرنا۔','iv. Doing a front roll.','iv. فرنټ رول کول.',dict(listGroup='ex')),
('v۔ ہاتھوں کو آگے کی طرف ملا کر جھلانا۔','v. Swinging with the hands joined in front.','v. لاسونه مخکې لوري ته یو ځای کولو سره ورغړول.',dict(listGroup='ex'))])
H(s,'سرگرمی (Activity):','Activity:','فعالیت (Activity):')
P(s,[('20 x 10 فٹ کے مستطیل کورٹ میں ایک ایک کھلاڑی نیٹ کے آر پار کھڑے ہو جائیں۔ ایک نیٹ کے قریب اور دوسرا کورٹ کے بیک لائن پر کھڑا ہو جائے۔ نیٹ کے قریب والا شٹل کو اونچا اور دور پھینکے اور دوسرا اسے زور سے سیدھے ہاتھ کے ریکٹ سے مخالف کو واپس کریں۔ یہ مشق 10 منٹ تک جاری رکھیں۔','In a rectangular court of 20 x 10 feet one player each should stand across the net. One should stand near the net and the other on the back line of the court. The one near the net should throw the shuttle high and far and the other should return it forcefully to the opponent with the racket in the right hand. Continue this practice for 10 minutes.','په ۲۰ x ۱۰ فوټو مستطیل کورټ کې یو یو لوبغاړی د جال دواړو خواوو ته ودرېږي. یو د جال سره نږدې او بل د کورټ د شاتنۍ کرښې پر سر ودرېږي. د جال سره نږدې شټل لوړ او لرې وغورځوي او بل یې په زور په ښي لاس د ریکټ سره مخالف ته بېرته ورکړي. دا تمرین ۱۰ دقیقې دوام ورکړئ.')])
F.done()
fig=svg(520,220,'Five stages of a forehand stroke drawn as stick figures, with arrows showing the racket swinging from low behind to high in front; the word forehand is written at the left',
  T(60,24,'forehand',14,'start',700)+''.join(
  f'<circle cx="{x}" cy="{y}" r="14" fill="#6d4c41"/><line x1="{x}" y1="{y+14}" x2="{x}" y2="{y+70}" stroke="#333" stroke-width="5"/><line x1="{x}" y1="{y+70}" x2="{x-18}" y2="{y+120}" stroke="#333" stroke-width="5"/><line x1="{x}" y1="{y+70}" x2="{x+18}" y2="{y+120}" stroke="#333" stroke-width="5"/><line x1="{x}" y1="{y+30}" x2="{x+rx}" y2="{y+ry}" stroke="#333" stroke-width="4"/><ellipse cx="{x+rx+6}" cy="{y+ry-10}" rx="9" ry="18" fill="none" stroke="#1b5e20" stroke-width="3"/>'
  for x,y,rx,ry in [(60,60,-26,70),(170,60,-24,60),(280,60,26,56),(390,50,30,30),(490,40,16,-20)])+
  '<path d="M80 150 Q250 190 470 70" fill="none" stroke="#c62828" stroke-width="3" stroke-dasharray="6 4"/>')
s['figures']=[dict(id='hpe11-s041-fig1',svg=fig,caption='Forehand stroke in five stages (forehand)',captionUrdu='فورہینڈ ضرب کے پانچ مراحل',captionPashto='د فورهینډ د ګوزار پنځه پړاوونه',labels=[lab('forehand','فورہینڈ','فورهینډ')],sourceGap=dict(note='Simplified coded stick-figure redrawing of the five-stage drawing of a tennis forehand; the original is a coloured line drawing with arrows.'))]
s['sourceNote']='Printed page 39 (the page number “39” is printed in a hexagon at the foot). '+MISS+NOTE
s['vocabulary']={}
save(s)
# scan 42 = printed 40 (figure)
s=page(42,'u05','40','Performance of the smash; backhand stroke skill (badminton)','سمیش کی کارکردگی؛ الٹے ہاتھ کے ریکٹ سے ضرب لگانا','د سمېش کارکردګي؛ په کیڼ لاس د ریکټ ګوزار','badminton-1')
F=Flow(s)
H(s,'کارکردگی (Performance):','Performance:','کارکردګي (Performance):')
P(s,[('مندرجہ بالا سرگرمی کرنے سے کھلاڑی میں جسمانی توازن برقرار رکھنے کی مہارت پیدا ہوگی۔ اس سرگرمی سے سمیش (Smash) مارنے اور اس کو جاندار بنانے کی خوبی ترقی پائے گی۔','By doing the above activity, the skill of maintaining physical balance will arise in the player. By this activity the quality of hitting a smash (Smash) and making it lively will develop.','د پورتني فعالیت کولو سره په لوبغاړي کې د بدني توازن ساتلو مهارت پیدا کېږي. له دې فعالیت نه سمېش (Smash) وهلو او هغه ژوندی کولو ښه والی پرمختګ کوي.')])
H(s,'2۔ الٹے ہاتھ کے ریکٹ سے ضرب لگانا (Backhand Stroke Skill):','2. Hitting with the Racket in the Left (Back) Hand (Backhand Stroke Skill):','۲. په کیڼ لاس د ریکټ سره ګوزار (Backhand Stroke Skill):')
P(s,[('بیڈ منٹن کی تمام مہارتوں میں سے یہ مشکل مہارت ہے کیونکہ اس میں پورے جسم کی قوت کے ساتھ بازو کو دوسری طرف جھلا کر اس طرح سے ضرب لگائی جاتی ہے کہ سر سے پاؤں تک جسم سیدھا اور توازن میں ہو جاتا ہے اور آخر میں کلائی سے ہلکا سا جھٹکا دے کر شٹل کو مخالف کے حصے میں گرایا جاتا ہے۔ اس میں توازن کا اصول اور قوت کے اصول کو استعمال میں لایا جاتا ہے۔','Among all the skills of badminton this is a difficult skill, because in it, with the strength of the whole body, the arm is swung to the other side and the stroke is delivered in such a way that the body from head to foot becomes straight and in balance, and finally, giving a slight jerk with the wrist, the shuttle is dropped into the opponent’s part. In it the principle of balance and the principle of force are used.','په بیډمنټن د ټولو مهارتونو کې دا ستونزمنه مهارت دی ځکه په هغې کې د ټول بدن د ځواک سره لاس بلې خوا ته ورغړولو سره داسې ګوزار کېږي چې له سره تر پښو پورې بدن سیده او په توازن کې شي او په پای کې له مړوند نه یو سپک ټکان ورکولو سره شټل د مخالف په برخه کې غورځول کېږي. په هغې کې د توازن او د ځواک اصول په کار اچول کېږي.')])
F.fg(0)
F.done()
fig=svg(520,260,'Four stages of a badminton backhand stroke drawn as stick figures on a court line, the racket swinging overhead in the later stages',
  ''.join(f'<circle cx="{x}" cy="{y}" r="14" fill="#6d4c41"/><line x1="{x}" y1="{y+14}" x2="{x}" y2="{y+80}" stroke="#2e6bb5" stroke-width="7"/><line x1="{x}" y1="{y+80}" x2="{x-16}" y2="{y+140}" stroke="#333" stroke-width="5"/><line x1="{x}" y1="{y+80}" x2="{x+16}" y2="{y+140}" stroke="#333" stroke-width="5"/><line x1="{x}" y1="{y+30}" x2="{x+rx}" y2="{y+ry}" stroke="#333" stroke-width="4"/><ellipse cx="{x+rx}" cy="{y+ry-14}" rx="8" ry="16" fill="none" stroke="#1b5e20" stroke-width="3"/>'
   for x,y,rx,ry in [(70,50,26,0),(190,50,-20,40),(310,30,12,-30),(430,50,34,-6)])+
  '<line x1="20" y1="214" x2="500" y2="214" stroke="#555" stroke-width="3"/><line x1="40" y1="190" x2="40" y2="240" stroke="#555" stroke-width="3"/><line x1="480" y1="190" x2="480" y2="240" stroke="#555" stroke-width="3"/>')
s['figures']=[dict(id='hpe11-s042-fig1',svg=fig,caption='Backhand stroke in four stages',captionUrdu='الٹے ہاتھ کی ضرب کے چار مراحل',captionPashto='د کیڼ لاس د ګوزار څلور پړاوونه',labels=[],sourceGap=dict(note='Simplified coded stick-figure redrawing of the four-stage badminton drawing.'))]
s['sourceNote']='Printed page 40: performance paragraph of the previous skill and the second skill (backhand stroke in badminton) with the four-stage drawing; the lower third of the page is blank.'+NOTE
s['vocabulary']={}
save(s)
# scan 43 = printed 41
s=page(43,'u05','41','Backhand: exercise, activity, performance; volleyball (start)','الٹے ہاتھ کی ضرب: ورزش، سرگرمی، کارکردگی؛ والی بال','د کیڼ لاس ګوزار: تمرین، فعالیت، کارکردګي؛ والیبال','badminton-2')
F=Flow(s)
H(s,'ورزش (Exercise):','Exercise:','تمرین (Exercise):')
P(s,[('i۔ کمر پر ہاتھ رکھ کر دھڑ کو اطراف میں گھمانا۔','i. Putting the hands on the waist and rotating the trunk to the sides.','i. په ملا لاسونه ایښودلو سره تنه څنګونو ته ګرځول.',dict(listGroup='ex')),
('ii۔ سر کو آگے اور پیچھے جھکانا۔','ii. Bending the head forward and backward.','ii. سر مخکې او شاته ټیټول.',dict(listGroup='ex')),
('iii۔ باری باری ایک پاؤں پر کھڑے ہونا۔','iii. Standing on one foot by turns.','iii. په نوبت په یوه پښه ولاړ کېدل.',dict(listGroup='ex')),
('iv۔ کھڑے کھڑے جمپ لگانا۔','iv. Jumping while standing.','iv. ولاړ ولاړ ټوپ وهل.',dict(listGroup='ex')),
('v۔ گھٹنوں پر توازن قائم رکھنا۔','v. Maintaining balance on the knees.','v. په زنګنونو توازن ساتل.',dict(listGroup='ex'))])
H(s,'سرگرمی (Activity):','Activity:','فعالیت (Activity):')
P(s,[('15 x 10 فٹ کے ایک مستطیل ایریا میں کھلاڑی نیٹ کے آر پار کھڑے ہو جائیں۔ پہلے باری باری بیک ہینڈ سروس کی مشق کریں۔ اس کے بعد ریلی کرانے کی کوشش کریں یہ سرگرمی 10 منٹ تک جاری رکھیں۔ اس سرگرمی سے دونوں میں فٹ ورک، جسمانی توازن اور ہاتھ سے سٹروک مارنے کی مہارت بہتر ہوگی۔','In a rectangular area of 15 x 10 feet the players should stand across the net. First practise backhand service by turns. After that try to have a rally; continue this activity for 10 minutes. Through this activity footwork, bodily balance and the skill of hitting a stroke with the hand will improve in both.','په ۱۵ x ۱۰ فوټو یوه مستطیل سیمه کې لوبغاړي د جال دواړو خواوو ته ودرېږي. لومړی په نوبت د بیک هینډ سروس تمرین وکړئ. له دې وروسته ریلي کولو هڅه وکړئ دا فعالیت ۱۰ دقیقې دوام ورکړئ. له دې فعالیت نه په دواړو کې فټ ورک، بدني توازن او په لاس د سټروک وهلو مهارت ښه کېږي.')])
H(s,'کارکردگی (Performance):','Performance:','کارکردګي (Performance):')
P(s,[('مندرجہ بالا سرگرمی سے کھلاڑیوں کی سٹروک میں بہتری آئے گی۔ اس سے عضلات اور اعصاب میں ہم آہنگی بڑھے گی۔ اس سرگرمی سے شٹل کو صحیح جگہ پر پھینکنے کی خوبی پیدا ہوگی۔','Through the above activity the players’ strokes will improve. By it coordination between muscles and nerves will increase. Through this activity the quality of throwing the shuttle to the right place will arise.','له پورتني فعالیت نه د لوبغاړو په سټروک کې ښه والی راځي. له دې نه په عضلاتو او اعصابو کې همغږي زیاتېږي. له دې فعالیت نه شټل ته په سم ځای غورځولو ښه والی پیدا کېږي.')])
H(s,'والی بال (Volley Ball)','Volleyball (Volley Ball)','والیبال (Volley Ball)')
P(s,[('والی بال میں سمیشنگ کرنے کی مہارت کو بڑھانے اور اس کو بائیو مکینیکل اصولوں کے مطابق جسمانی حرکات کو کنٹرول کرنے کا عملی مظاہرہ کریں۔','In volleyball, demonstrate practically increasing the skill of smashing and controlling bodily movements according to biomechanical principles.','په والیبال کې د سمېشنګ کولو مهارت زیاتولو او د هغه د بایومیکانیکي اصولو سره سم بدني حرکتونه کنټرولولو عملي ښودنه وکړئ.')])
F.done()
s['sourceNote']='Printed page 41: exercise, activity and performance for the backhand stroke, and the volleyball introduction; the lower part of the page is blank.'+NOTE
s['vocabulary']={}
save(s)
# scan 44 = printed 42 (figure)
s=page(44,'u05','42','Volleyball: skill of smashing; exercise','والی بال: سمیشنگ کرنے کی مہارت؛ ورزش','والیبال: د سمېشنګ مهارت؛ تمرین','volley-1')
F=Flow(s)
H(s,'سمیشنگ کرنے کی مہارت (Skill):','Skill of Smashing (Skill):','د سمېشنګ مهارت (Skill):')
P(s,[('والی بال کے میچ کے دوران جو نہی بوسٹر بال کو پاس بنائے تو سمیش کرنے والا کھلاڑی ٹائمنگ کے ساتھ ہوا میں جمپ لگا کر بال کو پوری طاقت کے ساتھ مخالف کے کورٹ میں ایسی جگہ مارے کہ کوئی کھلاڑی نہ اٹھا سکے۔ سمیشنگ کرتے وقت جسم کے توازن کو برقرار رکھیں۔','During a volleyball match, as soon as the booster makes the ball a pass, the player doing the smash, jumping in the air with timing, should hit the ball with full strength into the opponent’s court at such a place that no player can pick it up. Maintain the balance of the body while smashing.','د والیبال د لوبې په موده کې همدا چې بوسټر توپ ته پاس جوړ کړي نو سمېش کوونکی لوبغاړی د ټایمنګ سره په هوا ټوپ وهلو سره توپ په بشپړ ځواک سره د مخالف کورټ ته داسې ځای وهي چې هېڅ لوبغاړی یې پورته نه کړای شي. د سمېشنګ په وخت کې د بدن توازن وساتئ.')])
F.fg(0)
H(s,'ورزش (Exercise):','Exercise:','تمرین (Exercise):')
P(s,[('اس مہارت کی سرگرمی سے پہلے طلبا مندرجہ ذیل جسمانی اعضاء کی ورزش کریں۔','Before the activity of this skill the students should exercise the following parts of the body.','د دې مهارت له فعالیت نه مخکې زده‌کوونکي د لاندې بدني غړو تمرین وکړي.'),
('i۔ دونوں بازوؤں کو ملا کر گھمانا۔','i. Joining both arms and rotating them.','i. دواړه لاسونه یو ځای کولو سره ګرځول.',dict(listGroup='ex')),
('ii۔ ہاتھوں سے کندھوں کو چھونا۔','ii. Touching the shoulders with the hands.','ii. په لاسونو اوږې لمس کول.',dict(listGroup='ex')),
('iii۔ کھڑے کھڑے جمپ لگانا۔','iii. Jumping while standing.','iii. ولاړ ولاړ ټوپ وهل.',dict(listGroup='ex')),
('iv۔ ایک ایک پنجے پر باری باری کھڑے ہونا۔','iv. Standing on one toe at a time by turns.','iv. په یوه یوه ګوته په نوبت ولاړ کېدل.',dict(listGroup='ex')),
('v۔ جھکتے ہوئے پاؤں کو چھونا۔','v. Touching the feet while bending.','v. کږېدو سره پښې لمس کول.',dict(listGroup='ex'))])
F.done()
fig=svg(520,260,'Volleyball smash silhouette: a net, one player jumping above it to hit the ball, a defender with raised hands at the left and two players on the lower side',
  '<rect x="30" y="140" width="460" height="70" fill="#fff" stroke="#444" stroke-width="2"/>'+''.join(f'<line x1="{x}" y1="140" x2="{x}" y2="210" stroke="#999"/>' for x in range(50,490,20))+''.join(f'<line x1="30" y1="{y}" x2="490" y2="{y}" stroke="#999"/>' for y in range(160,210,20))+
  '<circle cx="190" cy="26" r="16" fill="#222"/>'+
  '<circle cx="250" cy="70" r="12" fill="#222"/><line x1="250" y1="82" x2="244" y2="140" stroke="#222" stroke-width="12"/><line x1="250" y1="86" x2="232" y2="52" stroke="#222" stroke-width="7"/><line x1="250" y1="86" x2="276" y2="50" stroke="#222" stroke-width="7"/>'+
  '<circle cx="130" cy="100" r="12" fill="#222"/><line x1="130" y1="112" x2="140" y2="170" stroke="#222" stroke-width="12"/><line x1="130" y1="116" x2="150" y2="80" stroke="#222" stroke-width="7"/>'+
  '<circle cx="330" cy="170" r="14" fill="#222"/><line x1="330" y1="184" x2="330" y2="238" stroke="#222" stroke-width="18"/>'+
  '<circle cx="420" cy="180" r="12" fill="#222"/><line x1="420" y1="192" x2="420" y2="240" stroke="#222" stroke-width="16"/>')
s['figures']=[dict(id='hpe11-s044-fig1',svg=fig,caption='Smashing in volleyball (silhouettes of players at the net)',captionUrdu='والی بال میں سمیشنگ (نیٹ پر کھلاڑیوں کے خاکے)',captionPashto='په والیبال کې سمېشنګ (د جال سره د لوبغاړو سیوری)',labels=[],sourceGap=dict(note='Simplified coded silhouette of the four players at the net; the original is a black silhouette illustration.'))]
s['sourceNote']='Printed page 42: skill of smashing in volleyball with the silhouette illustration, and the warm-up exercises i–v.'+NOTE
s['vocabulary']={}
save(s)
# scan 45 = printed 43
s=page(45,'u05','43','Volleyball: activity “Two vs Three”; performance; boosting skill','والی بال: سرگرمی “دو بمقابلہ تین”؛ کارکردگی؛ بوسٹنگ کی مہارت','والیبال: فعالیت “دوه په مقابل درې”؛ کارکردګي؛ بوسټنګ مهارت','volley-2')
F=Flow(s)
H(s,'سرگرمی (Activity):','Activity:','فعالیت (Activity):')
H(s,'دو بمقابلہ تین (Two VS Three)','Two versus Three (Two VS Three)','دوه په مقابل درې (Two VS Three)')
P(s,[('اس سرگرمی میں 5 طلبا حصہ لیتے ہیں۔ اس سرگرمی میں دو کھلاڑی نیٹ سے ایک طرف اور تین کھلاڑی دوسری طرف کھڑے ہو جائیں۔','Five students take part in this activity. In this activity two players should stand on one side of the net and three players on the other side.','پدې فعالیت کې ۵ زده‌کوونکي برخه اخلي. پدې فعالیت کې دوه لوبغاړي د جال یوې خوا او درې لوبغاړي بلې خوا ته ودرېږي.'),
('اس سرگرمی میں 2 کھلاڑی پہلے سروس کریں گے دوسری طرف تین کھلاڑی بال کو پاس، سیٹ اور سمیش کی کوشش کریں گے۔ یہ سرگرمی 12x6 میٹر کے مستطیل کورٹ میں کریں۔ اس کی مدد سے سروس، پاسنگ، سیٹنگ اور سمیشنگ چاروں چیزوں میں کارکردگی بہتر ہوگی۔ یہ سرگرمی 5-5 منٹ کے وقفے سے دہرائیں۔ اس سرگرمی سے سمیشنگ کی مہارت میں بہتری آئے گی۔','In this activity 2 players will serve first; on the other side three players will try to pass, set and smash the ball. Do this activity in a rectangular court of 12x6 metres. With its help performance will improve in all four things: service, passing, setting and smashing. Repeat this activity at intervals of 5-5 minutes. Through this activity the skill of smashing will improve.','پدې فعالیت کې ۲ لوبغاړي لومړی سروس کوي بلې خوا ته درې لوبغاړي توپ ته پاس، سیټ او سمېش هڅه کوي. دا فعالیت په ۱۲x۶ مترو مستطیل کورټ کې وکړئ. د هغه په مرسته سروس، پاسنګ، سیټنګ او سمېشنګ څلورو شیانو کې کارکردګي ښه کېږي. دا فعالیت په ۵–۵ دقیقو وقفه تکرار کړئ. له دې فعالیت نه په سمېشنګ مهارت کې ښه والی راځي.')])
H(s,'کارکردگی (Performance):','Performance:','کارکردګي (Performance):')
P(s,[('اس سرگرمی کے بعد طلباء میں والی بال کے سمیشنگ، پاسنگ اور سروس کی مہارت میں بہتری آئے گی۔ کھلاڑیوں/طلباء کے درمیان ٹیم ورک (Team work) بھی پیدا ہوگا۔ اس کے ذریعے کھلاڑیوں میں توازن کو برقرار رکھنے اور ہوا میں جسم پر کنٹرول بھی بہتر ہوگا۔ کھلاڑی میچ کے دوران ٹیم ورک کی وجہ سے بہتر کارکردگی دکھائیں گے۔','After this activity improvement will come in the students’ skill in volleyball smashing, passing and service. Team work (Team work) will also arise among the players/students. Through it balance and control over the body in the air will also be better in the players. The players will show better performance during the match because of team work.','له دې فعالیت وروسته په زده‌کوونکو کې د والیبال د سمېشنګ، پاسنګ او سروس په مهارت کې ښه والی راځي. د لوبغاړو/زده‌کوونکو ترمنځ ټیم ورک (Team work) هم پیدا کېږي. د هغه په مټ په لوبغاړو کې توازن ساتل او په هوا کې پر بدن کنټرول هم ښه کېږي. لوبغاړي د لوبې په موده کې د ټیم ورک له امله ښه کارکردګي ښيي.')])
H(s,'مہارت (Skill):','Skill:','مهارت (Skill):')
H(s,'بال کو ایک یا دونوں ہاتھوں سے اٹھانا (Boosting):','Lifting the Ball with One or Both Hands (Boosting):','توپ په یوه یا دواړو لاسونو پورته کول (Boosting):')
P(s,[('والی بال میں نیٹ کے قریب بال کو اوپر اچھالنا بوسٹنگ کہلاتا ہے۔ جب بال پاس ہو کر بوسٹر کے پاس آتا ہے۔ تو بوسٹر انگلیوں کے پوروں سے بال کو نیٹ کے اوپر اس طرح اچھالتا ہے کہ سمیشر اس کو ٹائمنگ کے ساتھ جمپ لگا کر ایک ہاتھ سے زور سے مارے تاکہ بال صحیح جگہ پر جا کر گرے۔ اس میں بال بناتے وقت قوت کے انجذاب کا اصول مدنظر رکھنا ضروری ہے۔','In volleyball, tossing the ball up near the net is called boosting. When the ball comes to the booster after a pass, the booster tosses the ball above the net with the fingertips in such a way that the smasher, jumping with timing, hits it hard with one hand so that the ball goes and falls in the right place. In it, while setting the ball it is necessary to keep in view the principle of the absorption of force.','په والیبال کې د جال سره نږدې توپ پورته غورځول بوسټنګ بلل کېږي. کله چې توپ پاس کېدو سره بوسټر ته راشي. نو بوسټر د ګوتو په څوکو توپ د جال پر سر داسې پورته غورځوي چې سمېشر هغه د ټایمنګ سره ټوپ وهلو سره په یو لاس په زور ووهي ترڅو توپ په سم ځای ولوېږي. په هغې کې د توپ جوړولو په وخت کې د ځواک د جذب اصول په پام کې نیول اړین دي.')])
F.done()
s['sourceNote']='Printed page 43: activity “Two vs Three”, performance, and the start of the skill of boosting (lifting the ball).'+NOTE
s['vocabulary']={}
save(s)
