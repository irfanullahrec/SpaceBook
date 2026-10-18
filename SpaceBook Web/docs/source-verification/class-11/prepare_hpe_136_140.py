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
def photo(s,fid,w,h,aria,body,cap,cu,cp):
    s['figures']=[dict(id=fid,svg=svg(w,h,aria,body),caption=cap,captionUrdu=cu,captionPashto=cp,labels=[],sourceGap=dict(note='The original is a coloured photograph; replaced by a simplified coded SVG schematic (no raster image).'))]
# scan 136 = printed 134
s=page(136,'u07','134','Hockey: dress and equipment; start of play; free hit; corner; penalty corner (start)','ہاکی: لباس اور سامان؛ کھیل کا آغاز؛ فری ہٹ؛ کارنر؛ پنلٹی کارنر','هاکي: جامې او سامان؛ د لوبې پیل؛ فري هټ؛ کارنر؛ پنلټي کارنر','hockey-4')
F=Flow(s)
H(s,'لباس اور سامان','Dress and Equipment','جامې او سامان')
P(s,[('ہر ٹیم اپنے مخصوص رنگ میں ہوتی ہے۔ ایک ٹیم کے تمام کھلاڑیوں کا لباس ایک جیسا ہوتا ہے۔ دونوں ٹیموں کا لباس مختلف ہوتا ہے۔ گول کیپر کے لباس کا رنگ اپنی ٹیم سے مختلف ہوتا ہے۔ صرف گول کیپر، ماسک، گلوز پیڈ وغیرہ پہن سکتا ہے۔','Each team is in its own particular colour. All the players of one team have the same dress. The dress of the two teams is different. The colour of the goalkeeper’s dress is different from his own team. Only the goalkeeper can wear a mask, gloves, pads and so on.','هره ټیم په خپل ځانګړي رنګ کې وي. د یو ټیم د ټولو لوبغاړو جامې یو شان وي. د دواړو ټیمونو جامې توپیر لري. د ګول کیپر د جامو رنګ له خپل ټیم نه توپیر لري. یوازې ګول کیپر ماسک، دستکشې، پیډ او داسې نور اغوستلی شي.')])
H(s,'کھیل کا آغاز','Start of the Game','د لوبې پیل')
P(s,[('جو ٹیم ٹاس جیت جاتی ہے وہ سائیڈ لیتی ہے یا پاس کرتی ہے۔ کھیل شروع کرتے وقت، وقفہ کے بعد اور گول ہونے کے بعد کھیل پاس سے شروع ہوتا ہے۔','The team that wins the toss takes the side or makes the pass. At the start of the game, after the break and after a goal, the game starts with a pass.','هغه ټیم چې ټاس وګټي اړخ اخلي یا پاس کوي. د لوبې د پیل پر مهال، له وقفې وروسته او له ګول وروسته لوبه په پاس پیلېږي.')])
H(s,'فری ہٹ','Free Hit','فري هټ')
P(s,[]+L([('ا۔ جس جگہ فاؤل ہوگا وہاں سے فری ہٹ لی جاتی ہے۔','A. The free hit is taken from the place where the foul occurs.','ا. چېرته چې فاول وي له هماغه ځایه فري هټ اخیستل کېږي.'),
('ب۔ فری ہٹ لگاتے وقت بال ساکن ہو۔','B. The ball should be stationary when taking the free hit.','ب. د فري هټ د وهلو پر مهال توپ ساکن وي.'),
('ج۔ فری ہٹ کے وقت مخالف کھلاڑی 5 گز کے فاصلے پر ہوتے ہیں۔','C. At the time of the free hit the opposing players are at a distance of 5 yards.','ج. د فري هټ پر مهال مخالف لوبغاړي د ۵ ګزو په واټن وي.'),
('د۔ جو کھلاڑی فری ہٹ لگائے گا۔ وہ دوبارہ بال کو اس وقت تک نہیں کھیل سکتا جب تک کوئی دوسرا کھلاڑی بال کو ٹچ نہ کرے۔','D. The player who takes the free hit cannot play the ball again until another player touches the ball.','د. هغه لوبغاړی چې فري هټ وهي بیا توپ نشي لوبولی تر هغه چې بل لوبغاړی توپ ونه لمسوي.')],'fh'))
H(s,'کارنر','Corner','کارنر')
P(s,[('دفاعی ٹیم کے کسی کھلاڑی کی ہاکی سے بال 25 گز کے اندر ٹچ ہو کر گول لائن عبور کر جائے تو حملہ آور ٹیم کو کارنر دیا جائے گا۔ کارنر کے وقت کھلاڑی جہاں چاہیں کھڑے ہو سکتے ہیں۔ کارنر کی ہٹ سے براہ راست گول نہیں ہو سکتا۔','If the ball, touched by the hockey stick of a player of the defending team within 25 yards, crosses the goal line, a corner will be given to the attacking team. At the time of the corner the players can stand wherever they like. A goal cannot be scored directly from the corner hit.','که د دفاعي ټیم د کوم لوبغاړي له هاکۍ سره توپ په ۲۵ ګزو دننه لمس شي او د ګول لاین تېر شي نو برید کوونکي ټیم ته کارنر ورکول کېږي. د کارنر پر مهال لوبغاړي چېرته چې وغواړي ودرېدای شي. د کارنر له هټ نه مستقیم ګول نشي کېدای.')])
H(s,'پنلٹی کارنر','Penalty Corner','پنلټي کارنر')
P(s,[('کسی بھی ٹیم کو پنلٹی کارنر مندرجہ ذیل صورتوں میں دیا جاتا ہے۔','A penalty corner is given to any team in the following cases.','هر ټیم ته پنلټي کارنر په لاندې صورتونو کې ورکول کېږي.',GAP('The list of cases continues on the next page (printed page 135).'))])
F.done()
s['sourceNote']='Printed page 134: dress and equipment, start of the game, free hit (A–D), corner, and the introduction to penalty corner. The page number “134” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 137 = printed 135
s=page(137,'u07','135','Hockey: penalty corner cases (1–8); goalkeeper photograph','ہاکی: پنلٹی کارنر کی صورتیں (1–8)','هاکي: د پنلټي کارنر صورتونه (۱–۸)','hockey-5')
F=Flow(s)
P(s,[]+L([
('1۔ دفاعی ٹیم کا کوئی کھلاڑی 25 گز لائن کے اندر کوئی خطرناک فاؤل کرے۔','1. A player of the defending team commits a dangerous foul within the 25-yard line.','۱. د دفاعي ټیم کوم لوبغاړی د ۲۵ ګز لاین دننه کوم خطرناک فاول وکړي.'),
('2۔ دفاعی ٹیم کے کسی کھلاڑی کے پاؤں پر بال شوٹنگ سرکل کے اندر لگے۔','2. The ball hits the foot of a player of the defending team inside the shooting circle.','۲. د دفاعي ټیم د کوم لوبغاړي په پښه توپ د شوټنګ سرکل دننه ولګېږي.'),
('3۔ دفاعی ٹیم اگر دانستہ طور پر شوٹنگ سرکل کے اندر سے بال گول لائن سے باہر پھینک دے۔','3. The defending team deliberately throws the ball out over the goal line from inside the shooting circle.','۳. دفاعي ټیم که قصدي توګه د شوټنګ سرکل له دننه نه توپ له ګول لاین بهر وغورځوي.'),
('4۔ جب دفاعی ٹیم کے کھلاڑی ڈی سے بال خطرناک طریقے پر کلیئر کریں۔','4. When the players of the defending team clear the ball from the D in a dangerous manner.','۴. کله چې د دفاعي ټیم لوبغاړي له ډي نه توپ په خطرناکه طریقه کلیر کړي.'),
('5۔ فری ہٹ ملنے پر جان بوجھ کر ڈی کے قریب ہٹ لگانے میں تاخیر کرے۔ پنلٹی کارنر کے وقت حملہ آور ٹیم کے کھلاڑی سرکل کے باہر کھڑے ہوں گے اور ایک کھلاڑی بال پھینکنے کے لیے پنلٹی کارنر کے نشان پر کھڑا ہوگا۔','5. On getting a free hit, deliberately delays taking the hit near the D. At the time of the penalty corner the players of the attacking team will stand outside the circle and one player will stand at the penalty-corner mark to push the ball.','۵. د فري هټ په ترلاسه کولو سره قصدي توګه د ډي نږدې په هټ وهلو کې ځنډ وکړي. د پنلټي کارنر پر مهال به د برید کوونکي ټیم لوبغاړي د سرکل بهر ولاړ وي او یو لوبغاړی به د توپ غورځولو لپاره د پنلټي کارنر په نښه ولاړ وي.'),
('6۔ پنلٹی کارنر کے وقت دفاعی ٹیم کے پانچ کھلاڑی گول لائن پر ہوں گے اور باقی تمام کھلاڑی سنٹر لائن پر ہوں گے۔','6. At the time of the penalty corner five players of the defending team will be on the goal line and all the remaining players will be on the centre line.','۶. د پنلټي کارنر پر مهال به د دفاعي ټیم پنځه لوبغاړي په ګول لاین او پاتې ټول لوبغاړي به په سنټر لاین وي.'),
('7۔ پنلٹی کارنر کی ہٹ لگنے سے پہلے کوئی کھلاڑی بھاگ نہیں سکتا۔','7. No player can run before the penalty corner hit is made.','۷. د پنلټي کارنر د هټ له وهلو مخکې هېڅ لوبغاړی نشي منډې وهلی.'),
('8۔ پنلٹی کارنر سے بال اگر براہ راست گول میں جائے اور نیٹ میں لگے تو گول نہیں ہوگا اور اگر تختہ پر لگے تو گول دیا جائے گا۔ یہ قانون گاہے بگاہے بدلتا رہتا ہے۔ آج کل نیٹ پر لگنے سے بھی گول ہو جاتا ہے۔ ان ڈائریکٹ ہٹ کا بال اگر گول میں جائے تو گول دیا جائے گا بشرطیکہ کوئی فاؤل سرزد نہ ہوا ہو اور بال نے مکمل طور پر گول لائن عبور کر لی ہو۔ ڈائریکٹ ہٹ اگر کسی دفاعی کھلاڑی کی ہاکی سے لگ جائے تو تختہ کی قید نہیں ہوتی۔','8. If the ball from the penalty corner goes directly into the goal and hits the net it will not be a goal, and if it hits the board a goal will be given. This rule keeps changing from time to time. Nowadays a goal is scored even on hitting the net. If the ball from an indirect hit goes into the goal, a goal will be given provided no foul has been committed and the ball has crossed the goal line completely. If a direct hit touches the hockey stick of a defending player, the board restriction does not apply.','۸. د پنلټي کارنر نه که توپ مستقیم ګول ته ولاړ شي او جال ته ولګېږي نو ګول نه وي او که تختې ته ولګېږي نو ګول ورکول کېږي. دا قانون وخت په وخت بدلېږي. نن ورځ جال ته په لګېدو هم ګول کېږي. که د نامستقیم هټ توپ ګول ته ولاړ شي نو ګول ورکول کېږي په دې شرط چې کوم فاول نه وي شوی او توپ په بشپړ ډول د ګول لاین تېر کړی وي. که مستقیم هټ د دفاعي لوبغاړي له هاکۍ سره ولګېږي نو د تختې قید نه وي.')],'pc'))
F.fg(0)
F.done()
photo(s,'hpe11-s137-fig1',420,260,'A goal with a green “Rio 2016” banner behind it: a goalkeeper in an orange shirt, pads and mask stands in the goal, with defenders in white shirts and one player in blue in front',
 '<rect width="420" height="260" fill="#6ec04a"/><rect x="40" y="30" width="340" height="190" fill="none" stroke="#fff" stroke-width="6"/><text x="210" y="120" font-size="56" text-anchor="middle" fill="#e8f5e9" font-family="sans-serif" font-weight="bold">Rio 2016</text><circle cx="210" cy="95" r="14" fill="#fff"/><rect x="190" y="110" width="40" height="70" rx="10" fill="#fb8c00"/><rect x="192" y="180" width="36" height="40" fill="#212121"/><g fill="#eceff1"><circle cx="120" cy="140" r="11"/><rect x="108" y="152" width="24" height="55" rx="8"/><circle cx="300" cy="145" r="11"/><rect x="288" y="157" width="24" height="55" rx="8"/><circle cx="345" cy="135" r="11"/><rect x="333" y="147" width="24" height="55" rx="8"/></g><circle cx="65" cy="175" r="11" fill="#1976d2"/><rect x="53" y="187" width="24" height="55" rx="8" fill="#1976d2"/>',
 'Defenders and the goalkeeper in front of the goal at a penalty corner','پنلٹی کارنر کے وقت گول کے سامنے دفاعی کھلاڑی اور گول کیپر','د پنلټي کارنر پر مهال د ګول مخې ته دفاعي لوبغاړي او ګول کیپر')
s['sourceNote']='Printed page 135: eight cases and rules for the penalty corner, with a photograph (goalkeeper and defenders in front of the goal, “Rio 2016” banner) at the foot. Item 8 notes that the rule changes from time to time. The page number “135” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 138 = printed 136
s=page(138,'u07','136','Hockey: penalty (punishment); penalty stroke','ہاکی: سزا؛ پنلٹی سٹروک','هاکي: سزا؛ پنلټي سټروک','hockey-6')
F=Flow(s)
H(s,'سزا','Penalty (Punishment)','سزا')
P(s,[]+L([('ا۔ اگر دفاعی ٹیم بار بار قانون شکنی کرے تو امپائر پنلٹی سٹروک دے سکتا ہے۔','A. If the defending team breaks the rules repeatedly, the umpire can award a penalty stroke.','ا. که دفاعي ټیم په پرله پسې ډول قانون ماتوي نو امپایر پنلټي سټروک ورکولی شي.'),
('ب۔ اگر حملہ آور ٹیم خلاف ورزی کرے تو دفاعی ٹیم کو فری ہٹ دی جائے گی۔','B. If the attacking team commits a violation, a free hit will be given to the defending team.','ب. که برید کوونکی ټیم سرغړونه وکړي نو دفاعي ټیم ته فري هټ ورکول کېږي.')],'pu'))
H(s,'پنلٹی سٹروک','Penalty Stroke','پنلټي سټروک')
P(s,[('پنلٹی سٹروک درج ذیل صورتوں میں دیا جاتا ہے۔','A penalty stroke is given in the following cases.','پنلټي سټروک په لاندې صورتونو کې ورکول کېږي.')]+L([
('ا۔ جب پنلٹی کارنر کے وقت دفاعی ٹیم بار بار قانون شکنی کرے۔','A. When the defending team repeatedly breaks the rules at the time of a penalty corner.','ا. کله چې د پنلټي کارنر پر مهال دفاعي ټیم په پرله پسې ډول قانون ماتوي.'),
('ب۔ گول لائن کے اوپر گول پوسٹوں کے درمیان دفاعی ٹیم کے کھلاڑی کے پاؤں پر لگے۔','B. The ball hits the foot of a player of the defending team on the goal line between the goal posts.','ب. د ګول لاین پر سر د ګول پوسټونو ترمنځ د دفاعي ټیم د لوبغاړي په پښه ولګېږي.'),
('ج۔ بال اگر گول کیپر پکڑے یا دھکیلے۔','C. If the goalkeeper catches or pushes the ball.','ج. که ګول کیپر توپ ونیسي یا وټیلي.'),
('د۔ جب دفاعی ٹیم کا کوئی کھلاڑی حملہ آور ٹیم کے کھلاڑی کو اس وقت خطرناک طریقے سے روکے جب وہ گول کرنے کی پوزیشن میں ہو۔','D. When a player of the defending team stops a player of the attacking team in a dangerous manner while he is in a position to score a goal.','د. کله چې د دفاعي ټیم کوم لوبغاړی د برید کوونکي ټیم لوبغاړی په خطرناکه طریقه هغه مهال ودروي چې هغه د ګول کولو په موقعیت کې وي.'),
('ہ۔ پنلٹی سٹروک کے وقت دونوں ٹیموں کے کھلاڑی 25 گز کے فاصلے پر ہوں گے جبکہ حملہ آور ٹیم کا ایک کھلاڑی پنلٹی سٹروک کی جگہ پر ہوگا اور دفاعی ٹیم کا گول کیپر گول میں ہوگا۔','E. At the time of the penalty stroke the players of both teams will be at a distance of 25 yards, while one player of the attacking team will be at the penalty-stroke spot and the goalkeeper of the defending team will be in the goal.','ه. د پنلټي سټروک پر مهال به د دواړو ټیمونو لوبغاړي د ۲۵ ګزو په واټن وي پداسې حال کې چې د برید کوونکي ټیم یو لوبغاړی به د پنلټي سټروک په ځای او د دفاعي ټیم ګول کیپر به په ګول کې وي.'),
('و۔ پنلٹی سٹروک سے بال اگر گول میں گول لائن عبور کر کے چلا جائے تو گول دیا جائے گا اور اگر گول کیپر بال کو روک لے یا بال پوسٹوں سے لگ کر واپس آ جائے تو پنلٹی سٹروک ضائع ہوگا۔','F. If the ball from the penalty stroke crosses the goal line into the goal, a goal will be given, and if the goalkeeper stops the ball or the ball rebounds from the posts, the penalty stroke is lost.','و. که د پنلټي سټروک نه توپ د ګول لاین تېرولو سره ګول ته ولاړ شي نو ګول ورکول کېږي او که ګول کیپر توپ ودروي یا توپ له پوسټونو سره لګېدو سره بېرته راشي نو پنلټي سټروک ضایع کېږي.')],'ps'))
F.fg(0)
F.done()
photo(s,'hpe11-s138-fig1',420,260,'A penalty stroke being taken: a player at the left about to strike the ball, a goalkeeper in dark kit in the goal at the right, and two officials standing beside the goal',
 '<rect width="420" height="260" fill="#2e9e83"/><rect width="420" height="40" fill="#5c6bc0"/><polygon points="270,40 420,40 420,260 330,260" fill="#e5a46a"/><rect x="340" y="120" width="60" height="90" fill="none" stroke="#eceff1" stroke-width="4"/><circle cx="345" cy="150" r="10" fill="#212121"/><rect x="335" y="160" width="22" height="50" rx="7" fill="#212121"/><circle cx="300" cy="90" r="8" fill="#fdd835"/><rect x="292" y="98" width="16" height="40" rx="5" fill="#fdd835"/><circle cx="90" cy="150" r="10" fill="#f5cba7"/><rect x="80" y="160" width="20" height="45" rx="7" fill="#e53935"/><line x1="70" y1="200" x2="55" y2="225" stroke="#222" stroke-width="4"/><circle cx="150" cy="215" r="5" fill="#fff"/>',
 'A penalty stroke being taken with the goalkeeper in the goal','پنلٹی سٹروک لگاتے ہوئے، گول میں گول کیپر','پنلټي سټروک وهلو سره، په ګول کې ګول کیپر')
s['sourceNote']='Printed page 136: penalty (punishment) cases A–B, penalty stroke cases A–F, with a photograph of a penalty stroke at the foot. The page number “136” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 139 = printed 137
s=page(139,'u07','137','Hockey: when a goal is scored; hit-in; other violations; punishment','ہاکی: گول کب ہوتا ہے؛ ہٹ ان؛ دیگر خلاف ورزیاں؛ سزا','هاکي: ګول کله کېږي؛ هټ ان؛ نورې سرغړونې؛ سزا','hockey-7')
F=Flow(s)
H(s,'گول کب ہوتا ہے','When a Goal Is Scored','ګول کله کېږي')
P(s,[('جب حملہ آور ٹیم کا کوئی کھلاڑی شوٹنگ سرکل کے اندر سے بال کو ہٹ کرے اور بال گول پوسٹوں کے درمیان سے اور کراس بار کے نیچے سے مکمل طور پر گول لائن عبور کرے اور اس دوران کوئی فاؤل سرزد نہ ہوا ہو تو گول دیا جائے گا۔','When a player of the attacking team hits the ball from inside the shooting circle and the ball crosses the goal line completely between the goal posts and under the crossbar, and no foul has been committed during that time, a goal will be given.','کله چې د برید کوونکي ټیم کوم لوبغاړی د شوټنګ سرکل له دننه نه توپ هټ کړي او توپ د ګول پوسټونو ترمنځ او د کراس بار لاندې په بشپړ ډول د ګول لاین تېر کړي او په دې موده کې کوم فاول نه وي شوی نو ګول ورکول کېږي.')])
H(s,'ہٹ ان','Hit-in','هټ ان')
P(s,[('جب بال مکمل طور پر سائیڈ لائن عبور کر جائے تو ہٹ ان دی جاتی ہے۔ جس کھلاڑی سے آخری مرتبہ بال ٹچ ہو کر سائیڈ لائن عبور کرے اس کی مخالف ٹیم کو ہٹ ان دی جائے گی۔ ہٹ ان کے وقت کھلاڑی 5 گز کے فاصلے پر ہوں گے۔ ہٹ ان کرنے والا کھلاڑی بال کو دوبارہ اس وقت تک نہیں کھیل سکتا جب تک دوسرا کھلاڑی اسے ٹچ نہ کرے۔','When the ball crosses the sideline completely, a hit-in is given. The opposing team of the player by whom the ball was last touched before crossing the sideline will be given the hit-in. At the time of the hit-in the players will be at a distance of 5 yards. The player taking the hit-in cannot play the ball again until another player touches it.','کله چې توپ په بشپړ ډول د اړخ لاین تېر کړي نو هټ ان ورکول کېږي. د هغه لوبغاړي مخالف ټیم ته چې له هغه نه وروستی ځل توپ لمس شوی او د اړخ لاین یې تېر کړی هټ ان ورکول کېږي. د هټ ان پر مهال به لوبغاړي د ۵ ګزو په واټن وي. هټ ان کوونکی لوبغاړی بیا توپ نشي لوبولی تر هغه چې بل لوبغاړی هغه ونه لمسوي.')])
H(s,'دیگر خلاف ورزیاں','Other Violations','نورې سرغړونې')
P(s,[]+L([('1۔ کھیل کے دوران پاؤں یا جسم کے کسی حصہ سے بال چھو جانا۔','1. The ball touching the foot or any part of the body during the game.','۱. د لوبې په موده کې توپ ته په پښه یا د بدن کوم برخه لګېدل.'),
('2۔ کھیل میں کسی قسم کی رکاوٹ پیدا کرنا۔','2. Creating any kind of obstruction in the game.','۲. په لوبه کې هر ډول خنډ جوړول.'),
('3۔ وقت ضائع کرنے کی کوشش کرنا۔','3. Trying to waste time.','۳. د وخت ضایع کولو هڅه کول.'),
('4۔ خطرناک طریقے سے بال کو مخالف کی طرف ہٹ کرنا۔','4. Hitting the ball towards the opponent in a dangerous manner.','۴. په خطرناکه طریقه توپ مخالف لوري ته هټ کول.'),
('5۔ الٹی ہاکی سے بال کو روکنا یا ہٹ کرنا۔','5. Stopping or hitting the ball with the reverse side of the stick.','۵. په الټه هاکۍ توپ درول یا هټ کول.'),
('6۔ ناشائستہ رویہ اختیار کرنا۔','6. Adopting improper conduct.','۶. ناوړه چلند خپلول.')],'ov'))
H(s,'سزا','Penalty','سزا')
P(s,[('کھیل کے دوران اگر درج بالا بے ضابطگی ہو تو فری ہٹ دی جاتی ہے اور اگر شوٹنگ سرکل کے اندر ہو تو پنلٹی کارنر یا سٹروک دیا جا سکتا ہے۔ ناشائستہ رویہ پر کسی کھلاڑی کو عارضی یا مستقل طور پر باہر نکالا جا سکتا ہے۔','If the above irregularity occurs during the game a free hit is given, and if it is inside the shooting circle a penalty corner or stroke can be given. For improper conduct a player can be sent off temporarily or permanently.','که د لوبې په موده کې پورتنۍ بې ضابطګي وشي نو فري هټ ورکول کېږي او که د شوټنګ سرکل دننه وي نو پنلټي کارنر یا سټروک ورکول کېدای شي. په ناوړه چلند کوم لوبغاړی لنډمهاله یا تلپاتې توګه بهر ایستل کېدای شي.')])
F.done()
s['sourceNote']='Printed page 137: when a goal is scored, hit-in, other violations (1–6) and the penalty for them. The page number “137” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
# scan 140 = printed 138
s=page(140,'u07','138','Hockey: accidents; Exercise questions: hockey (1 i–iv)','ہاکی: حادثات؛ مشقی سوالات: ہاکی (1 i–iv)','هاکي: پېښې؛ تمرین پوښتنې: هاکي (۱ i–iv)','hockey-8')
F=Flow(s)
H(s,'حادثات','Accidents','پېښې')
P(s,[('کھلاڑی کے زخمی ہونے یا کسی واقعہ کے پیش آ جانے کی صورت میں عارضی طور پر کھیل بند کر دیا جاتا ہے اور ضائع شدہ وقت اس ہاف میں دیا جاتا ہے۔ ایسی صورت میں جیسے کھیل بند کیا گیا تھا اسی حالت میں دوبارہ شروع کیا جائے گا۔','If a player is injured or some incident occurs, the game is stopped temporarily and the lost time is added in that half. In such a case the game will be restarted in the same condition in which it was stopped.','که لوبغاړی ټپي شي یا کومه پېښه رامنځته شي نو لوبه لنډمهاله بنده کېږي او ضایع شوی وخت په هماغه نیمایي کې ورکول کېږي. په داسې صورت کې لوبه په هماغه حالت بیا پیلېږي چې څنګه بنده شوې وه.')])
H(s,'مشقی سوالات','Exercise Questions','تمرین پوښتنې')
H(s,'1۔ موزوں جوابات کا انتخاب کریں۔','1. Choose the suitable answers.','۱. مناسب ځوابونه وټاکئ.')
mc(s,'(i) ہاکی کا گراؤنڈ ________ گز ہوتا ہے۔','(i) A hockey ground is ________ yards.','(i) د هاکۍ ګراونډ ________ ګزه وي.',['90×50','100×60','110×70','120×80'])
mc(s,'(ii) ہاکی میں گول پوسٹوں کا درمیانی فاصلہ ________ گز ہوتا ہے۔','(ii) In hockey the distance between the goal posts is ________ yards.','(ii) په هاکۍ کې د ګول پوسټونو ترمنځ واټن ________ ګزه وي.',['2','3','4','5'])
mc(s,'(iii) ہاکی کھیل کا دورانیہ ________ فٹ کا ہوتا ہے۔','(iii) The duration of a hockey game is ________ feet.','(iii) د هاکۍ لوبې موده ________ فټه وي.',['50','60','70','80'])
MC(s,('(iv) ہاکی سٹک ________ کی بنی ہوتی ہے۔','(iv) A hockey stick is made of ________.','(iv) د هاکۍ سټک د ________ جوړ وي.'),[('(الف) لوہا','(a) Iron','(الف) اوسپنه'),('(ب) پلاسٹک','(b) Plastic','(ب) پلاستیک'),('(ج) ربڑ','(c) Rubber','(ج) ربړ'),('(د) لکڑی','(d) Wood','(د) لرګی')])
F.done()
s['sourceNote']='Printed page 138: accidents, heading Exercise Questions and question 1 items i–iv on hockey (multiple choice). The printed items (iii) “duration … feet” and (iv) option labels are as printed, including the unit “فٹ” for duration, which looks like a printing slip. The page number “138” is shown in a hexagon at the foot.'+NOTE
s['vocabulary']={}
save(s)
