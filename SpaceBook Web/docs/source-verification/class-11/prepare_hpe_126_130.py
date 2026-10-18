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
# scan 126 = printed 124
s=page(126,'u07','124','Exercise questions: football (8–10) and descriptive questions','مشقی سوالات: فٹ بال (8–10) اور تفصیلی سوالات','تمرین پوښتنې: فوټبال (۸–۱۰) او تشریحي پوښتنې','ex7k')
F=Flow(s)
MC(s,('viii۔ فٹ بال میں گول پوسٹوں کا درمیانی فاصلہ ________ میٹر ہوتا ہے۔','viii. In football the distance between the goal posts is ________ metres.','viii. په فوټبال کې د ګول پوسټونو ترمنځ واټن ________ متره وي.'),[('(الف) 6.32','(a) 6.32','(الف) ۶.۳۲'),('(ب) 7.32','(b) 7.32','(ب) ۷.۳۲'),('(ج) 8.32','(c) 8.32','(ج) ۸.۳۲'),('(د) 9.32','(d) 9.32','(د) ۹.۳۲')])
MC(s,('ix۔ فٹ بال گراؤنڈ کی کم از کم چوڑائی ________ میٹر ہوتی ہے۔','ix. The minimum width of a football ground is ________ metres.','ix. د فوټبال د ګراونډ لږ تر لږه سور ________ متره وي.'),[('(الف) 60','(a) 60','(الف) ۶۰'),('(ب) 45','(b) 45','(ب) ۴۵'),('(ج) 80','(c) 80','(ج) ۸۰'),('(د) 90','(d) 90','(د) ۹۰')])
MC(s,('x۔ فٹ بال میچ کے دوران گراؤنڈ میں ________ آفیشلز میچ کرواتے ہیں۔','x. During a football match ________ officials conduct the match on the ground.','x. د فوټبال لوبې په موده کې په ګراونډ کې ________ آفیشلان لوبه کوي.'),[('(الف) 1','(a) 1','(الف) ۱'),('(ب) 2','(b) 2','(ب) ۲'),('(ج) 3','(c) 3','(ج) ۳'),('(د) 4','(d) 4','(د) ۴')])
H(s,'2۔ درج ذیل سوالات کے جواب لکھیں۔','2. Write answers to the following questions.','۲. لاندې پوښتنو ځوابونه ولیکئ.')
Q(s,'i۔ فٹ بال گراؤنڈ کا خاکہ بنائیں اور کھلاڑیوں کی پوزیشن ظاہر کریں۔','i. Draw a sketch of a football ground and show the positions of the players.','i. د فوټبال د ګراونډ انځور جوړ کړئ او د لوبغاړو موقعیت وښایاست.')
Q(s,'ii۔ فٹ بال میں ڈائریکٹ فری کک کن فاؤلز پر دی جاتی ہے وضاحت کریں۔','ii. Explain for which fouls a direct free kick is given in football.','ii. په فوټبال کې مستقیم فري کک په کومو فاولونو ورکول کېږي توضیح یې کړئ.')
Q(s,'iii۔ فٹ بال میں آف سائیڈ اور پنلٹی کی وضاحت کریں۔','iii. Explain offside and penalty in football.','iii. په فوټبال کې آف ساید او پنلټي توضیح کړئ.')
F.done()
s['sourceNote']='Printed page 124: football exercise items viii–x (multiple-choice) and question 2 (i–iii); lower half blank. The page number “124” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 127 = printed 125
s=page(127,'u07','125','Kabaddi: ground, poles, outer circle','کبڈی: گراؤنڈ، پالے، بیرونی دائرہ','کبډي: ګراونډ، پالې، بهرنی دایره','kabaddi-1')
F=Flow(s)
H(s,'کبڈی','Kabaddi','کبډي')
H(s,'گراؤنڈ:','Ground:','ګراونډ:')
P(s,[('یہ ایک دائرہ میں کھیلا جاتا ہے جس کا نصف قطر 75 تا 80 فٹ ہوتا ہے۔','It is played in a circle whose radius is 75 to 80 feet.','دا په یوه دایره کې لوبول کېږي چې نیم قطر یې ۷۵ تر ۸۰ فټه وي.')])
H(s,'پالے:','Poles (Lines):','پالې:')
P(s,[('دائرہ کے سنٹر لائن پر دو پالے ہوتے جن کا درمیانی فاصلہ 20 فٹ ہوتا ہے اور پالوں کی اونچائی 6 تا 9 انچ ہوتی ہے۔','On the centre line of the circle there are two pales (marks) whose distance apart is 20 feet, and the height of the pales is 6 to 9 inches.','د دایرې په سنټر لاین دوه پالې وي چې ترمنځ واټن یې ۲۰ فټه وي او د پالو لوړوالی ۶ تر ۹ انچه وي.',GAP('The Urdu “پالے” is kept as printed (a Kabaddi term for the marker/line); the translation is ours.'))])
H(s,'بیرونی دائرہ:','Outer Circle:','بهرنی دایره:')
P(s,[('کھیل کے دائرہ کے باہر 10 تا 20 فٹ جگہ خالی رکھ کر دائرہ لگایا جاتا ہے تاکہ تماشائی میدان میں نہ آ سکیں۔','The circle is drawn leaving 10 to 20 feet of space empty outside the playing circle so that spectators cannot come into the field.','د لوبې له دایرې بهر ۱۰ تر ۲۰ فټه ځای خالي ایښودلو سره دایره ایستل کېږي ترڅو تماشا کوونکي میدان ته رانشي.')])
F.fg(0)
F.done()
def lbl(x,y,t,c='#d81b60',a='middle'): return f'<text x="{x}" y="{y}" font-size="13" text-anchor="{a}" fill="{c}" font-family="sans-serif">{t}</text>'
fig=svg(420,360,'Kabaddi ground: a large circle containing a rounded court, a centre line with Raiders marked at each end and Stoppers at top and bottom, dimensions 20 feet, 25 feet and 75 feet',
 '<circle cx="210" cy="180" r="165" fill="none" stroke="#d81b60" stroke-width="2"/><rect x="95" y="130" width="230" height="100" rx="48" fill="none" stroke="#00695c" stroke-width="3"/><line x1="45" y1="180" x2="375" y2="180" stroke="#000" stroke-width="3"/><line x1="210" y1="180" x2="210" y2="345" stroke="#000" stroke-width="2"/><line x1="95" y1="110" x2="95" y2="250" stroke="#000" stroke-width="2" stroke-dasharray="3 6"/><line x1="325" y1="110" x2="325" y2="250" stroke="#000" stroke-width="2" stroke-dasharray="3 6"/>'
 +lbl(210,40,'Stoppers','#1565c0')+lbl(210,350,'Stoppers','#1565c0')+lbl(70,170,'Raiders')+lbl(350,170,'Raiders')+lbl(210,170,'20FT')+lbl(150,195,'25FT')+lbl(290,195,'35FT')+lbl(250,210,'25FT')+lbl(225,285,'75FT'))
s['figures']=[dict(id='hpe11-s127-fig1',svg=fig,caption='Kabaddi ground (dimensions in feet)',captionUrdu='کبڈی کا گراؤنڈ (پیمائش فٹ میں)',captionPashto='د کبډي ګراونډ (اندازې په فټو)',labels=[],sourceGap=dict(note='Simplified redrawing of the coloured diagram; the right-hand “35FT” figure is hard to read in the scan and may be 25FT.'))]
s['sourceNote']='Printed page 125: chapter heading Kabaddi (کبڈی), ground, poles and outer circle, with a labelled ground diagram (Raiders, Stoppers, 20FT, 25FT, 35FT, 75FT). The page number “125” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 128 = printed 126
s=page(128,'u07','126','Kabaddi: players, time, rules (1)','کبڈی: کھلاڑی، کھیل کا وقت، قواعد و ضوابط','کبډي: لوبغاړي، د لوبې وخت، قواعد او ضوابط','kabaddi-2')
F=Flow(s)
H(s,'کھلاڑی:','Players:','لوبغاړي:')
P(s,[('ایک ٹیم میں 11 کھلاڑی ہوں گے اس کے علاوہ دو متبادل کھلاڑی۔','There will be 11 players in a team, besides two substitute players.','په یوه ټیم کې ۱۱ لوبغاړي وي د دې ترڅنګ دوه بدل لوبغاړي.')])
H(s,'کھیل کا وقت:','Time of the Game:','د لوبې وخت:')
P(s,[('20-20 منٹ کے دو ہاف ہوں گے۔ دونوں ہاف میں 5 منٹ کا وقفہ ہوتا ہے اور کھلاڑی اطراف بدلتے ہیں۔','There will be two halves of 20-20 minutes. There is a 5-minute break between the two halves and the players change sides.','د ۲۰–۲۰ دقیقو دوه نیمایۍ وي. په دواړو نیمایو کې د ۵ دقیقو وقفه وي او لوبغاړي اړخونه بدلوي.')])
H(s,'قواعد و ضوابط:','Rules and Regulations:','قواعد او ضوابط:')
P(s,[]+L([
('کھیل کا آغاز ٹاس سے ہوتا ہے۔ جیتنے والے کو اختیار ہے کہ وہ سائیڈ لے یا پہلے حملہ آور کو بھیجے۔','The game begins with a toss. The winner has the choice to take a side or to send the raider first.','لوبه په ټاس پیلېږي. ګټونکي ته اختیار وي چې اړخ واخلي یا لومړی برید کوونکی ولېږي.'),
('دونوں ٹیمیں باری باری اپنا ایک کھلاڑی کبڈی ڈالنے (حملہ) کے لیے بھیجتی ہیں۔','Both teams in turn send one of their players to raid (attack).','دواړه ټیمونه په بدل بدل خپل یو لوبغاړی د کبډۍ اچولو (برید) لپاره لېږي.'),
('ایک کھلاڑی لگاتار دو مرتبہ کبڈی (حملہ) نہیں ڈال سکتا۔','A player cannot raid (attack) twice in a row.','یو لوبغاړی په پرله پسې ډول دوه ځله کبډۍ (برید) نشي اچولی.'),
('حملہ آور مخالف کے حصے میں 30 سیکنڈ تک ٹھہر سکتا ہے۔ 30 سیکنڈ میں اس نے مخالف کھلاڑی کو چھو کر واپس آنا ہوگا۔ ناکامی کی صورت میں مخالف کو ایک پوائنٹ ملے گا۔','The raider can stay in the opponent’s half for up to 30 seconds. Within 30 seconds he must touch an opposing player and return. In case of failure the opponent gets one point.','برید کوونکی د مخالف په برخه کې تر ۳۰ ثانیو پورې پاتې کېدای شي. په ۳۰ ثانیو کې به یې مخالف لوبغاړی لمس کړی او بېرته راځي. په ناکامۍ کې به مخالف ته یو پوائنټ ورکول کېږي.'),
('اگر کامیابی سے 30 سیکنڈ میں اپنے کورٹ میں واپس داخل ہوا تو حملہ آور کو پوائنٹ ملے گا۔','If he successfully re-enters his own court within 30 seconds, the raider gets a point.','که په بریالیتوب په ۳۰ ثانیو کې خپل کورټ ته بېرته داخل شو نو برید کوونکي ته پوائنټ ورکول کېږي.'),
('دفاعی ٹیم اگر حملہ آور کو 30 سیکنڈ تک اپنے کورٹ میں پکڑے رکھے یا روکے رکھے تو اسے ایک پوائنٹ ملتا ہے۔','If the defending team holds or keeps the raider in its court for 30 seconds, it gets one point.','که دفاعي ټیم برید کوونکی تر ۳۰ ثانیو پورې په خپل کورټ کې ونیسي یا ودرو، نو یو پوائنټ ورکول کېږي.'),
('جس کھلاڑی کا ہاتھ حملہ آور کو ٹچ ہو یا حملہ آور خود جسے ٹچ کرے وہی کھلاڑی اسے پکڑ سکتا ہے۔ اگر دوسرا کوئی چھوٹے تو پوائنٹ حملہ آور کو ملتا ہے۔','The player whose hand touches the raider, or whom the raider himself touches, is the only one who can catch him. If any other touches, the point goes to the raider.','هغه لوبغاړی چې لاس یې برید کوونکي ته ولګي یا برید کوونکی پخپله چې هغه ولمسوي، همدا لوبغاړی یې نیولی شي. که بل څوک ولمسوي نو پوائنټ برید کوونکي ته ورکول کېږي.'),
('اگر ایک سے زیادہ کھلاڑی حملہ آور کو چھو لیں تو پوائنٹ حملہ آور کو دیا جاتا ہے۔','If more than one player touches the raider, the point is given to the raider.','که له یوه ډېر لوبغاړي برید کوونکی ولمسوي نو پوائنټ برید کوونکي ته ورکول کېږي.'),
('اگر کوئی حملہ آور پکڑا جائے تو امپائر اُس وقت تک وِسل نہیں کرے گا جب تک وہ خود ہاتھ نہ اٹھائے یا 30 سیکنڈ گزر نہ جائیں۔','If a raider is caught, the umpire will not whistle until he himself raises his hand or 30 seconds have passed.','که کوم برید کوونکی ونیول شي نو امپایر به تر هغه وخته سیټۍ نه وهي ترڅو چې هغه پخپله لاس پورته نه کړي یا ۳۰ ثانیې تېرې نه شي.'),
('حملہ آور کو گراؤنڈ سے باہر دھکیل دیا جائے تو پوائنٹ دفاعی ٹیم کو ملے گا اور اگر دفاعی ٹیم کا کھلاڑی دائرہ سے باہر نکل جائے تو پوائنٹ حملہ آور ٹیم کو ملے گا۔','If the raider is pushed outside the ground, the point will go to the defending team; and if a player of the defending team goes outside the circle, the point will go to the raiding team.','که برید کوونکی له ګراونډ نه بهر وټیل شي نو پوائنټ دفاعي ټیم ته ورکول کېږي او که د دفاعي ټیم لوبغاړی له دایرې بهر ووځي نو پوائنټ د برید کوونکي ټیم ته ورکول کېږي.'),
('پانچ کھلاڑی بطور جاپھی (دفاعی) موجود نہ ہوں تو پوائنٹ حملہ آور کو دیا جائے گا۔','If five players are not present as stoppers (defenders), the point will be given to the raider.','که پنځه لوبغاړي د جاپهي (دفاعي) په توګه موجود نه وي نو پوائنټ برید کوونکي ته ورکول کېږي.')],'kr1'))
F.done()
s['sourceNote']='Printed page 126: players, duration, and the first part of the rules and regulations of Kabaddi (stars list). The word “جاپھی” (stopper) is kept as printed. The page number “126” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 129 = printed 127
s=page(129,'u07','127','Kabaddi: rules (2), fouls, tie, officials; skills — raider (start)','کبڈی: قواعد (2)، فاؤلز، میچ برابری، عہدیداران؛ مہارتیں — حملہ آور','کبډي: قواعد (۲)، فاولونه، د لوبې برابري، مامورین؛ مهارتونه — برید کوونکی','kabaddi-3')
F=Flow(s)
P(s,[]+L([
('دوران کھیل کوئی کھلاڑی جسم پر تیل یا چکنائی نہیں استعمال کر سکتا۔ نہ انگوٹھی پہن سکتا ہے۔','During the game no player may use oil or grease on the body, nor wear a ring.','د لوبې په موده کې هېڅ لوبغاړی په بدن تېل یا غوړي نشي کارولی. نه ګوتمه اغوستلی شي.'),
('ہر کھلاڑی لنگوٹر استعمال کر سکتا ہے ساتھ ٹیکر بھی جس پر کھلاڑی کا نمبر درج ہوتا ہے۔','Every player may use a loincloth (printed “لنگوٹر”), along with a tag/sticker on which the player’s number is written.','هر لوبغاړی لنګوټه (په متن کې «لنګوټر») کارولی شي سره له سټیکر هم چې پر هغې د لوبغاړي شمېره لیکل شوې وي.')],'kr2'))
H(s,'فاؤلز','Fouls','فاولونه')
P(s,[]+L([
('اگر کوئی دفاعی کھلاڑی حملہ آور کو ٹکر مارے یا بالوں سے پکڑے تو فاؤل ہوگا اور پوائنٹ حملہ آور کو دیا جائے گا۔','If a defender collides with the raider or catches him by the hair, it will be a foul and the point will be given to the raider.','که کوم دفاعي لوبغاړی برید کوونکي ته ټکر ورکړي یا په ویښتو یې ونیسي نو فاول وي او پوائنټ برید کوونکي ته ورکول کېږي.'),
('حملہ آور کو پکڑے بغیر قینچی مارنا فاؤل ہے۔','Applying the scissors hold without catching the raider is a foul.','برید کوونکی نیولو پرته قینچي وهل فاول دی.'),
('بھاگتے ہوئے حملہ آور کو ایڑی مارنا فاؤل ہے۔','Kicking a running raider with the heel is a foul.','منډې وهونکي برید کوونکي ته پاشنه وهل فاول دی.'),
('وِسل کے بعد 5 سیکنڈ تک تاخیر کرنے پر حملہ آور کے خلاف پوائنٹ دیا جاتا ہے۔','For delaying 5 seconds after the whistle a point is given against the raider.','له سیټۍ وروسته تر ۵ ثانیو ځنډ کولو په برید کوونکي پوائنټ ورکول کېږي.'),
('کھیل کے دوران مخالف کی کلائی، گردن یا ٹخنہ کو مروڑنا فاؤل ہے۔','During the game, twisting the opponent’s wrist, neck or ankle is a foul.','د لوبې په موده کې د مخالف د مړوند، غاړې یا ګوتې ټيټول (غوړول) فاول دی.'),
('مخالف کا گلہ گھونٹنا یا آنکھوں کو سختی سے بند کرنا فاؤل ہے۔','Throttling the opponent’s throat or shutting his eyes forcefully is a foul.','د مخالف ستوني نیول یا سترګې په زوره تړل فاول دی.'),
('کھیل کے دوران گالی گلوچ، اشتعال انگیز الفاظ کا استعمال بھی فاؤل ہوگا۔','During the game abusive language and provocative words will also be a foul.','د لوبې په موده کې ګواښ، سپکې ټکي او اشتعال ورکوونکي الفاظ کارول هم فاول وي.')],'kf'))
P(s,[('جو ٹیم مقررہ وقت میں زیادہ پوائنٹ بناتی ہے وہ میچ جیت جاتی ہے۔','The team that scores more points in the fixed time wins the match.','هغه ټیم چې په ټاکلي وخت کې ډېر پوائنټونه جوړ کړي لوبه ګټي.')])
H(s,'میچ برابری کی صورت میں:','In Case of a Tied Match:','د لوبې د برابرۍ په صورت کې:')
P(s,[('مقررہ وقت میں میچ برابری کی صورت میں 10 منٹ کا اضافی وقت دیا جاتا ہے جو 5-5 منٹ کے دو ہاف پر مشتمل ہوتا ہے۔ تمام قوانین کا اطلاق ہوتا ہے۔ جو ٹیم زیادہ پوائنٹ بناتی ہے میچ جیت جاتی ہے۔','If the match is tied in the fixed time, 10 minutes of extra time are given, consisting of two halves of 5-5 minutes. All rules apply. The team that scores more points wins the match.','که په ټاکلي وخت کې لوبه برابره شي نو ۱۰ دقیقې اضافي وخت ورکول کېږي چې د ۵–۵ دقیقو له دوو نیمایو جوړ وي. ټول قوانین پلي کېږي. هغه ټیم چې ډېر پوائنټونه جوړ کړي لوبه ګټي.')])
H(s,'عہدیداران:','Officials:','مامورین:')
P(s,[('ایک میچ میں 2 امپائر، فیلڈ جیوری کے 3 ممبران اور 3 سکورر ہوں گے۔','In one match there will be 2 umpires, 3 members of the field jury and 3 scorers.','په یوه لوبه کې ۲ امپایرانو، د فیلډ جیوري ۳ غړي او ۳ سکورر وي.',GAP('The scan is partly overprinted with bleed-through from the reverse page here; reading is best-effort.'))])
H(s,'مہارتیں (Skills):','Skills:','مهارتونه (Skills):')
H(s,'حملہ آور:','Raider:','برید کوونکی:')
P(s,[('رفتار پر عبور اور جاپھیوں پر نظر رکھتے ہوئے کمزور پر حملہ کرنا۔ اگر دائرہ کی لائن کے قریب ہو تو اسے باہر کی طرف دھکا دینا۔ اپنے آپ کو پکڑنے سے بچانا، بلاوجہ زور آزمائی نہ کرنا، واپسی پر سائیڈ بھاگ جانا، پکڑے جانے پر ٹیکنیکل','Mastery of speed, and, keeping an eye on the stoppers, attacking the weak one. If he is near the line of the circle, pushing him outward. Saving oneself from being caught, not wrestling without reason, running aside on the way back, and on being caught, getting free by a technical …','په چټکتیا واک او جاپهیانو ته پام کولو سره پر کمزوري برید کول. که د دایرې د لاین نږدې وي نو بهر لوري ته یې وټل. ځان له نیول کېدو ژغورل، بې له دلیل زور آزمایي نه کول، بېرته کېدو کې اړخ ته تښتېدل، د نیول کېدو په صورت کې تخنیکي …',GAP('The sentence continues on the next page (printed page 128: “طریقہ سے جان چھڑانا…”). First heading of the skills section is partly illegible in the scan; read as “حملہ آور”.'))])
F.done()
s['sourceNote']='Printed page 127: second half of the Kabaddi rules, fouls, tied match, officials, and the beginning of the skills section (raider). The scan carries heavy bleed-through from the reverse side and parts are best-effort. The page number “127” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 130 = printed 128 (photo)
s=page(130,'u07','128','Kabaddi skills: raider (end), defender (stopper)','کبڈی کی مہارتیں: حملہ آور (اختتام)، دفاع (جاپھی)','د کبډۍ مهارتونه: برید کوونکی (پای)، دفاع (جاپهي)','kabaddi-4')
F=Flow(s)
P(s,[('طریقہ سے جان چھڑانا، مضبوط گرفت میں آنے پر ہاتھ اٹھا لینا۔','… way, and when caught in a firm grip, raising the hand.','… طریقې ځان خلاصول، په پیاوړي ګرفت کې راتلو پر مهال لاس پورته کول.',GAP('Completes the sentence from printed page 127.'))])
H(s,'دفاع (جاپھی):','Defence (Stopper):','دفاع (جاپهي):')
P(s,[('ہاتھوں کو مضبوطی سے پکڑے رکھنا اور ساہی کو دائرہ میں گھمانا اس کو ڈاج کرنا تاکہ ایک جاپھی اس پر حملہ کر کے پکڑ سکے۔ کلائی کو مضبوطی سے پکڑنا، پکڑ کر قینچی لگانا، دائرہ کے اوپر سے گھمانا اور باہر کی طرف دھکیل دینا۔ اگر حملہ آور بھاگے تو پیچھے جاتے ہوئے پالے کے قریب سے باہر کی طرف دھکا دینا۔','Holding the hands firmly and turning the “sahi” (raider) round in the circle and dodging him so that one stopper can attack and catch him. Holding the wrist firmly, applying the scissors after catching, turning him over the circle and pushing him outward. If the raider runs, pushing him outward from near the pale while going back.','لاسونه په کلکه نیول او ساهي په دایره کې ګرځول او هغه ته ډاج ورکول ترڅو یو جاپهي پرې برید وکړي او ونیسي. مړوند په کلکه نیول، نیولو وروسته قینچي وهل، د دایرې له پاسه یې ګرځول او بهر لوري ته یې وټل. که برید کوونکی وتښتي نو شاته تللو پر مهال د پالې له نږدې بهر لوري ته وټل.',GAP('“ساہی” is kept as printed (it appears to mean the raider); the translation is ours.'))])
F.fg(0)
F.done()
fig=svg(400,260,'A kabaddi game outdoors on an orange field with several players: one player in an orange shirt bends forward gripping another, other players run around',
 '<rect width="400" height="260" fill="#e0693a"/><rect width="400" height="70" fill="#9bb8cf"/><path d="M0 70 q40 -30 80 0 t80 0 t80 0 t80 0 t80 0 v-10 h-400z" fill="#3f7d3a"/>'
 +'<circle cx="150" cy="110" r="14" fill="#f5cba7"/><path d="M150 124 l-30 70 M150 124 l40 50 M120 194 l-20 40 M120 194 l30 40" stroke="#ff7043" stroke-width="16" stroke-linecap="round" fill="none"/>'
 +'<circle cx="230" cy="100" r="13" fill="#c68642"/><path d="M230 113 l-15 65 M215 178 l-25 50 M215 178 l30 45" stroke="#222" stroke-width="14" stroke-linecap="round" fill="none"/>'
 +'<circle cx="320" cy="115" r="13" fill="#c68642"/><path d="M320 128 l10 55 M330 183 l-10 45 M330 183 l35 30" stroke="#222" stroke-width="14" stroke-linecap="round" fill="none"/>'
 +'<circle cx="60" cy="110" r="12" fill="#c68642"/><path d="M60 122 l5 55 M65 177 l-10 50 M65 177 l25 40" stroke="#222" stroke-width="13" stroke-linecap="round" fill="none"/>')
s['figures']=[dict(id='hpe11-s130-fig1',svg=fig,caption='A kabaddi match in progress: a stopper gripping the raider',captionUrdu='کبڈی کا میچ: جاپھی حملہ آور کو پکڑتے ہوئے',captionPashto='د کبډۍ لوبه: جاپهي برید کوونکی نیسي',labels=[],sourceGap=dict(note='The original is a coloured photograph; replaced by a simplified coded SVG schematic (no raster image).'))]
s['sourceNote']='Printed page 128: end of the raider skill, defence (stopper) skill, with a photograph of a kabaddi match. The scan carries bleed-through of mirrored text from the reverse side (exercise items i–vi of page 129) which is not part of this page. The page number “128” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
