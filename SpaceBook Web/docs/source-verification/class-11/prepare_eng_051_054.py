from enghelp import *
c=cell
U='u04'
V={}
def Qn(s,key,en,ur,ps,ex,tab,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,tab=tab,**m)
def H(s,key,en,ur,ps,tab=None,**m):
    d=dict(kind='heading',**m)
    if tab: d['tab']=tab
    add(s,key,en,ur,ps,**d)
def gl(s,cap,cu,cp,G,hdrs=('Words','Meaning')):
    s['tables']=[table(cap,cu,cp,[c(hdrs[0],'لفظ','کلمه'),c(hdrs[1],'معنی','معنا')],[[c(w,uw,pw),c(m,mu,mp)] for w,m,mu,mp,uw,pw in G],tab='glossary')]
    for w,m,mu,mp,uw,pw in G:
        k=w.split(' (')[0].lower()
        if k: V[k]=dict(ur=uw,ps=pw)
# ---------- scan 51 (printed 42) ----------
s=page(51,U,'42','About the author · Glossary (start)','مصنفہ کے بارے میں · فرہنگ (آغاز)','د لیکوالې په اړه · لغتنامه (پیل)','author-glossary-1')
F=Flow(s)
H(s,'ah','About the author:','مصنفہ کے بارے میں:','د لیکوالې په اړه:')
add(s,'at','Zoa Sherburne (30 September 1912 – 10 October 1995) was an American author, most known for her young adult fiction. Sherburne was born in Seattle, Washington and began writing in elementary school. Sherburne went on to be a very prolific writer, publishing over 300 short stories in magazines. She went on to publish thirteen novels, which together have been translated into over 27 languages. One of her books, Stranger in the House, about a family dealing with the return of their mother from a mental institution, became a movie: Memories Never Die (1982). Her novels often dealt with girls in difficult circumstances: coping with a mother’s alcoholism (Jennifer), with the remarriage of a parent.','زوآ شربرن (30 ستمبر 1912 – 10 اکتوبر 1995) ایک امریکی مصنفہ تھیں، جو اپنے نوجوان قارئین کے لیے افسانوں کے لیے سب سے زیادہ مشہور ہیں۔ شربرن سیئٹل، واشنگٹن میں پیدا ہوئیں اور ابتدائی اسکول میں لکھنا شروع کیا۔ شربرن ایک بہت پُرگو مصنفہ بنیں، رسالوں میں 300 سے زیادہ مختصر کہانیاں شائع کیں۔ انہوں نے تیرہ ناول شائع کیے، جن کا مجموعی طور پر 27 سے زیادہ زبانوں میں ترجمہ ہوا۔ ان کی ایک کتاب Stranger in the House، ایک ایسے خاندان کے بارے میں جو اپنی ماں کی ذہنی ادارے سے واپسی سے نمٹ رہا ہے، فلم بن گئی: Memories Never Die (1982)۔ ان کے ناول اکثر مشکل حالات میں لڑکیوں سے متعلق تھے: ماں کی شراب نوشی (جینیفر) سے نمٹنا، والدین میں سے کسی کی دوسری شادی سے۔','زوا شربرن (د 1912 کال د سپتمبر 30 – د 1995 کال د اکتوبر 10) یوه امریکايي لیکوالې وه، چې د خپلو ځوانو لوستونکو لپاره د افسانو له امله ډېره مشهوره ده. شربرن په سیاټل، واشنګټن کې زېږېدلې وه او په لومړني ښوونځي کې یې لیکل پیل کړل. شربرن یوه ډېره پرګو لیکوالې شوه، په مجلو کې یې له 300 ډېرې لنډې کیسې خپرې کړې. هغې دېرش ناولونه خپاره کړل، چې په ټوله کې له 27 ډېرو ژبو ته ژباړل شوي دي. د هغې یو کتاب Stranger in the House، د یوې کورنۍ په اړه چې د خپلې مور له رواني ادارې څخه د راستنېدو سره معامله کوي، فلم شو: Memories Never Die (1982). د هغې ناولونه ډېر ځله په ستونزمنو شرایطو کې له نجونو سره تړاو لري: د مور د شرابو سره مقابله (جینیفر)، د مور یا پلار له دویم واده سره.',sourceGap=dict(note='The right edge of the photograph clips the last letters of the lines in this paragraph ("an", "Was", "elementary", "300", "which", "books,", "their", "Die", "coping"); the words are read from context. The spacing after full stops is missing in the print ("school.Sherburne", "magazines.She").'))
H(s,'gh','Glossary','فرہنگ','لغتنامه',tab='glossary')
G=[('appendix (n)','a tube-shaped sac attached to and opening into the lower end of the large intestine in humans and some other mammals. In humans the appendix is small and has no known function, but in rabbits, hares, and some other herbivores it is involved in the digestion of cellulose.','ایک نلی نما تھیلی جو انسانوں اور بعض دوسرے ممالیہ میں بڑی آنت کے نچلے سرے سے جڑی ہوئی اور اس میں کھلتی ہے۔ انسانوں میں اپینڈکس چھوٹا ہے اور اس کا کوئی معلوم کام نہیں، لیکن خرگوش، ہرن اور بعض دوسرے سبزی خور جانوروں میں یہ سیلولوز کے ہضم میں شامل ہے۔','یوه نلي‌ډوله کڅوړه چې په انسانانو او ځینو نورو تي لرونکو کې د لویې کولمې له ښکتني پای سره نښتې او په هغې کې خلاصېږي. په انسانانو کې اپنډکس کوچنی دی او هېڅ پېژندل شوې دنده نه لري، خو په ځنګلي خرګوشانو، خرګوشانو او ځینو نورو واښه خورو کې د سیلولوز په هضم کې برخه اخلي.','اپینڈکس','اپنډکس'),
('beagle','a small hound of a breed with a short coat, used for hunting hares.','چھوٹی نسل کا شکاری کتا جس کی کھال چھوٹی ہوتی ہے، خرگوش کے شکار کے لیے استعمال ہوتا ہے۔','د کوچنۍ نسل ښکاري سپی چې لنډه پوستکې لري، د خرګوشانو د ښکار لپاره کارېږي.','بیگل (شکاری کتا)','بیګل'),
('blanked (v)','deliberately ignore (someone).','جان بوجھ کر (کسی کو) نظر انداز کرنا۔','په قصد سره (یو کس) له پامه غورځول.','نظر انداز کیا','له پامه غورځولی'),
('bonfire (n)','a large open-air fire used for burning rubbish or as part of a celebration.','ایک بڑی کھلی فضا کی آگ جو کوڑا جلانے یا جشن کے حصے کے طور پر استعمال ہوتی ہے۔','یو لوی په خلاص هوا کې اور چې د کثافاتو د سوځولو یا د لمانځنې د یوې برخې په توګه کارېږي.','الاؤ','لوی اور'),
('cellophane (n)','a thin transparent wrapping material made from viscose.','ایک پتلا شفاف لپیٹنے کا مواد جو وسکوز سے بنایا جاتا ہے۔','یو نری شفاف نغښتلو توکی چې له ویسکوز څخه جوړېږي.','سیلو فین','سیلوفین'),
('chowder','a rich soup typically containing fish, clams, or corn with potatoes and onions.','ایک گاڑھا شوربہ جس میں عموماً مچھلی، سیپیاں یا مکئی آلو اور پیاز کے ساتھ ہوتی ہے۔','یوه غټه ښوروا چې معمولاً کب، کلامز یا جوار له کچالو او پیازو سره لري.','گاڑھا شوربہ','غټه ښوروا'),
('clams','a marine bivalve mollusc with shells of equal size.','سمندری دو خولی والا نرم جسم جانور جس کے خول برابر سائز کے ہوتے ہیں۔','یو سمندري دوه‌پوښه نرم بدن ژوی چې پوښونه یې مساوي اندازې دي.','سیپیاں','کلامز'),
('closet','a tall cupboard or wardrobe with a door, used for storage.','دروازے والی اونچی الماری یا وارڈروب، جو ذخیرہ کرنے کے لیے استعمال ہوتی ہے۔','د دروازې سره لوړه المارۍ یا جامې ساتونکې، چې د زېرمې لپاره کارېږي.','الماری','المارۍ'),
('davenport (n)','an ornamental writing desk with drawers and a sloping surface for writing; a large heavily upholstered sofa.','درازوں اور لکھنے کے لیے ڈھلوان سطح والی آرائشی لکھنے کی میز؛ ایک بڑا بھاری گدے دار صوفہ۔','د دراز او د لیکلو لپاره ځوړ سطحې سره سینګار شوی د لیکلو مېز؛ یو لوی دروند ګدی لرونکی صوفه.','ڈیون پورٹ (صوفہ)','ډیونپورټ'),
('deftly (adv)','in a way that is neatly skilful and quick in movement.','ایسے انداز میں جو صفائی سے ماہرانہ اور حرکت میں تیز ہو۔','داسې ډول چې په پاکۍ مهارت لرونکی او په حرکت کې ګړندی وي.','مہارت سے','په مهارت'),
('disposition','a person’s inherent qualities of mind and character.','کسی شخص کے ذہن اور کردار کی فطری خصوصیات۔','د یو کس د ذهن او کردار طبیعي ځانګړتیاوې.','مزاج','مزاج'),
('dormitory','a large bedroom for a number of people in a school or institution.','اسکول یا ادارے میں کئی افراد کے لیے بڑا سونے کا کمرہ۔','په ښوونځي یا ادارې کې د څو کسانو لپاره لوی د خوب خونه.','ہاسٹل / خوابگاہ','ډورمېټري')]
gl(s,'Glossary','فرہنگ','لغتنامه',G)
build(s,51,['ah','at','gh','T:0'],[])
s['vocabulary']=V
s['sourceNote']='Printed page 42. "About the author:" is a bold side heading; a pink "Glossary" banner and a two-column table (Words / Meaning) of 12 rows follow. The right edge of the photograph clips the ends of lines in the author paragraph and in the glossary table (for example "lower end o[f]", "In human[s]", "rabbit[s]", "digestion o[f]", "hare[s]", "a[ ]celebration", "potatoe[s]", "surface f[or]", "institution[ ]"); the words are read from context. The page number 42 is printed in a diamond at the foot. Border lines, a pink corner flag and the watermark are excluded; a partial footer at the bottom edge is excluded. The Urdu and Pashto columns are added by us.'
save(s)
# ---------- scan 52 (printed 43) ----------
V={}
s=page(52,U,'43','Glossary (continued)','فرہنگ (جاری)','لغتنامه (دوام)','glossary-2')
F=Flow(s)
G=[('driftwood (n)','pieces of wood which are floating on the sea or have been washed ashore.','لکڑی کے ٹکڑے جو سمندر پر تیر رہے ہیں یا ساحل پر بہہ کر آ گئے ہیں۔','د لرګي ټوټې چې په سمندر باندې لامبي یا ساحل ته ورسېدلې.','بہتی لکڑی','بهېدونکی لرګی'),
('fugitive (n)','a person who has escaped from captivity or is in hiding.','وہ شخص جو قید سے فرار ہو چکا ہو یا چھپا ہوا ہو۔','هغه کس چې له بند څخه تښتېدلی یا په پټه کې وي.','مفرور','تښتېدلی'),
('gaily','in a cheerful or light-hearted way.','خوشی یا ہلکے پھلکے انداز میں۔','په خوشالۍ یا سپک زړه ډول.','خوش دلی سے','په خوشالۍ'),
('Gay (ad)','light-hearted and carefree.','ہلکے پھلکے دل والا اور بے فکر۔','سپک زړی او بې‌غمه.','خوش مزاج','خوشاله'),
('haltingly (adj)','slow and hesitant, especially through lack of confidence; faltering.','سست اور ہچکچاہٹ والا، خاص طور پر اعتماد کی کمی کی وجہ سے؛ لڑکھڑاتا ہوا۔','ورو او ټکنېدونکی، په ځانګړې توګه د باور د نشتوالي له امله؛ لړزېدونکی.','ہکلاتے ہوئے','په ټوخلو سره'),
('hiccupy','have an attack of hiccups or a single hiccup.','ہچکیوں کا دورہ پڑنا یا ایک ہچکی آنا۔','د ټوخلو بریدونو لرل یا یو ټوخل.','ہچکی بھرا','ټوخلي لرونکی'),
('inconsequential','not important or significant.','غیر اہم یا غیر نمایاں۔','مهم یا ښکاره نه.','غیر اہم','بې‌ارزښته'),
('jagged (ad)','with rough, sharp points protruding.','کھردری، نوکیلی چوٹیوں کے ساتھ جو باہر نکلی ہوں۔','له تېرو، تېرو څوکو سره چې بهر ته راوتلې وي.','ناہموار / نوکیلا','څوکه‌ور'),
('nightmarish (n)','Like a frightening or unpleasant dream.','ڈراؤنے یا ناخوشگوار خواب جیسا۔','د وېروونکي یا ناخوښ خوب په څېر.','ڈراؤنا','وېروونکی'),
('Pestered (v)','trouble or annoy (someone) with frequent or persistent requests or interruptions.','بار بار یا مسلسل درخواستوں یا مداخلت سے (کسی کو) تنگ کرنا یا ستانا۔','په مکرر یا دوامداره غوښتنو یا مداخلو سره (یو کس) ځورول یا ځپل.','تنگ کیا','ځورول شوی'),
('poignant','evoking a keen sense of sadness or regret.','اداسی یا پچھتاوے کا گہرا احساس ابھارنے والا۔','د خپګان یا پښېمانۍ ژور احساس راپارونکی.','دردناک','دردوونکی'),
('poked','prod and stir (a fire) with a poker to make it burn more fiercely.','پوکر سے (آگ کو) کریدنا اور ہلانا تاکہ وہ زیادہ تیزی سے جلے۔','په پوکر سره (اور) ټېل وهل او ګډول چې ډېر تېز وسوځي.','کریدا','وهل شوی'),
('pungent','having a sharply strong taste or smell.','تیز اور مضبوط ذائقہ یا بو رکھنے والا۔','تېره او قوي خوند یا بوی لرونکی.','تیز','تېر'),
('quilted','join together (layers of fabric or padding) with lines of stitching to form a bed covering, a warm garment, or for decorative effect.','(کپڑے یا گدی کی تہوں کو) سلائی کی لکیروں سے جوڑنا تاکہ بستر کا کور، گرم لباس بنے یا آرائشی اثر پیدا ہو۔','(د ټوکر یا ګدۍ پرتونه) د ګنډلو په کرښو سره نښلول چې د بستر پوښ، تود جامه یا سینګاري اغېز جوړ شي.','گدے دار','تهول شوی'),
('rake (v)','draw together with a rake or similar implement.','ریک یا اسی طرح کے آلے سے اکٹھا کرنا۔','په ریک یا ورته وسیله سره راټولول.','سمیٹنا','راټولول'),
('scatter-brained (ad)','(of a person) disorganized and lacking in concentration.','(کسی شخص کا) بے ترتیب اور توجہ کی کمی والا۔','(د یو کس) بې‌نظمه او د تمرکز له نشتوالي سره.','لاپروا / بھلکڑ','بې‌پروا'),
('Siamese cat (n)','a cat of a lightly built short-haired breed characterized by slanting blue eyes and typically pale fur with darker points.','ہلکی ساخت کی چھوٹے بالوں والی نسل کی بلی جس کی خصوصیت ترچھی نیلی آنکھیں اور عموماً گہرے نقطوں والی ہلکی کھال ہے۔','د سپکې جوړښت لنډ ویښتو نسل پیشو چې ځانګړتیا یې ټیټې شنې سترګې او معمولاً تیاره نقطو سره روښانه څرمن ده.','سیامی بلی','سیامي پیشو'),
('smoldered','burn slowly with smoke but no flame.','دھوئیں کے ساتھ آہستہ جلنا مگر شعلے کے بغیر۔','په لوګي سره ورو سوځېدل خو پرته له لمبې.','سلگا','ټوخل'),
('smothering (v)','kill (someone) by covering their nose and mouth so that they suffocate; extinguish (a fire) by covering it.','(کسی کو) ناک اور منہ ڈھانپ کر مار دینا تاکہ دم گھٹ جائے؛ (آگ کو) ڈھانپ کر بجھانا۔','(یو کس) د پزې او خولې په پټولو وژل چې ساه یې بنده شي؛ (اور) په پټولو مړول.','دم گھوٹنا','ساه بندول'),
('smudge (n)','a smoky outdoor fire that is lit to keep off insects or protect plants against frost.','دھوئیں والی بیرونی آگ جو کیڑوں کو دور رکھنے یا پودوں کو پالے سے بچانے کے لیے جلائی جاتی ہے۔','لوګی لرونکی بهرنی اور چې د حشراتو د لرې ساتلو یا د بوټو د یخنۍ څخه د ساتنې لپاره بلېږي.','دھواں / دھونی','لوګی'),
('snapping','break suddenly and completely, typically with a sharp cracking sound.','اچانک اور مکمل طور پر ٹوٹنا، عموماً تیز کڑکڑاہٹ کی آواز کے ساتھ۔','ناڅاپي او بشپړ ماتېدل، معمولاً د تېز ټکاس غږ سره.','ٹوٹنا','ماتېدل'),
('snug (ad)','comfortable, warm, and cosy; well protected from the weather or cold.','آرام دہ، گرم اور آرام دہ؛ موسم یا سردی سے اچھی طرح محفوظ۔','آرامه، تود او ښه؛ له هوا یا یخنۍ ښه ساتل شوی.','آرام دہ','آرامه'),
('splinters (n)','a small, thin, sharp piece of wood, glass, or similar material broken','لکڑی، شیشے یا اسی طرح کے مواد کا ایک چھوٹا، پتلا، تیز ٹکڑا جو ٹوٹ گیا ہو','د لرګي، شیشې یا ورته توکي یوه کوچنۍ، نرۍ، تېره ټوټه چې ماته شوې وي','کرچیاں','ټوټې')]
gl(s,'Glossary (continued)','فرہنگ (جاری)','لغتنامه (دوام)',G,hdrs=('Words','Meaning'))
build(s,52,['T:0'],[])
s['vocabulary']=V
s['sourceNote']='Printed page 43: continuation of the Glossary table, 25 rows. Printed headwords are kept with their capitalisation and punctuation ("Gay (ad)", "Pestered (v)", "inconsequen/tial", "scatter-/brained (ad)"). The left edge of the photograph clips the first letters of the headwords in the first column (for example "driftwood", "haltingly", "inconsequen[tial]", "nightmarish"). The last row (splinters) continues on the next page. The page number 43 is printed in a diamond at the foot. Border lines, a pink corner flag and the watermark are excluded.'
save(s)
# ---------- scan 53 (printed 44) ----------
V={}
s=page(53,U,'44','Glossary (end) · Reading Comprehension','فرہنگ (اختتام) · مطالعے کا فہم','لغتنامه (پای) · د لوست پوهه','glossary-rc')
F=Flow(s)
G=[('','off from a larger piece.','ایک بڑے ٹکڑے سے الگ۔','له یوې لویې ټوټې څخه جلا.','',''),
('Spook','a ghost.','بھوت۔','شبح.','بھوت','شبح'),
('squishing','make a soft squelching sound when walked on or in.','اس پر یا اس میں چلنے پر نرم چپ چپ کی آواز پیدا کرنا۔','کله چې پرې یا په هغې کې ګرځېدل کېږي نرم شپشپ غږ جوړول.','چپ چپ کرنا','شپشپ کول'),
('stacks','a large quantity of something.','کسی چیز کی بڑی مقدار۔','د یو شي لویه اندازه.','ڈھیر','ډېرونه'),
('surmount','overcome (a difficulty or obstacle).','(کسی مشکل یا رکاوٹ پر) قابو پانا۔','(یوه ستونزه یا خنډ) برالاسي کول.','قابو پانا','برلاسی کېدل'),
('Tucked (v)','push, fold, or turn (the edges or ends of something, especially garment or bedclothes) so as to hide or secure them.','(کسی چیز کے کناروں یا سروں کو، خاص طور پر لباس یا بستر کے کپڑوں کو) دھکیلنا، موڑنا یا لپیٹنا تاکہ انہیں چھپایا یا محفوظ کیا جا سکے۔','(د یو شي څنډې یا پایونه، په ځانګړې توګه جامې یا د بستر ټوکر) ټېل وهل، نغاړل یا تاوول چې پټ یا خوندي شي.','اڑسا / ٹھونسا','ننه ایښودل'),
('tumbled','rumple; disarrange.','شکن ڈالنا؛ بے ترتیب کرنا۔','ګونځې کول؛ ګډوډول.','بکھرا','ګډوډ'),
('waffles','a small crisp batter cake, baked in a waffle iron and eaten hot with butter or syrup.','ایک چھوٹا خستہ بیٹر کیک، جو وافل آئرن میں پکایا جاتا ہے اور مکھن یا شربت کے ساتھ گرم کھایا جاتا ہے۔','یو کوچنی ټوټه ګډ شوی کیک، چې په وافل اوسپنه کې پخېږي او له مسکې یا شربت سره ګرم خوړل کېږي.','وافلز','وافلز'),
('windowsill (n)','a ledge or sill forming the bottom part of a window.','کھڑکی کے نچلے حصے کی چوکھٹ یا ابھار۔','د کړکۍ د ښکتنۍ برخې څنډه یا ټیټ برخه.','کھڑکی کی چوکھٹ','د کړکۍ څنډه')]
gl(s,'Glossary (end)','فرہنگ (اختتام)','لغتنامه (پای)',G)
H(s,'rc','Reading Comprehension','مطالعے کا فہم','د لوست پوهه')
Qn(s,'ans','Answer the following questions.','درج ذیل سوالات کے جواب دیں۔','لاندې پوښتنو ته ځواب ورکړئ.','eng11-u04-rc','exercise')
RQ=[("How is the theme of ‘From Mother . . . With Love’ a universal theme present in literature across all cultures?",'‘ماں کی طرف سے . . . محبت کے ساتھ’ کا موضوع تمام ثقافتوں کے ادب میں موجود عالمگیر موضوع کیسے ہے؟','د ‘له مور څخه . . . په مینه’ موضوع څنګه په ټولو کلتورونو کې په ادب کې شته نړیوال موضوع دی؟'),
("Comment on the plot of the story ‘From Mother . . . With Love’.",'کہانی ‘ماں کی طرف سے . . . محبت کے ساتھ’ کے پلاٹ پر تبصرہ کریں۔','د کیسې ‘له مور څخه . . . په مینه’ پر پلاټ تبصره وکړئ.'),
("Identify the narrator or speaker of the story ‘From Mother. . . With Love’.",'کہانی ‘ماں کی طرف سے . . . محبت کے ساتھ’ کے راوی یا بولنے والے کی شناخت کریں۔','د کیسې ‘له مور څخه . . . په مینه’ راوي یا خبرې کوونکی وپېژنئ.'),
('Analyze and comment on the character of Minta?','منٹا کے کردار کا تجزیہ اور اس پر تبصرہ کریں؟','د منټا د کردار تحلیل وکړئ او تبصره پرې وکړئ؟'),
('What is the conflict in the story? How is it resolved?','کہانی میں تنازع کیا ہے؟ وہ کیسے حل ہوتا ہے؟','په کیسه کې شخړه څه ده؟ دا څنګه حل کېږي؟'),
('Where does Minta’s father take her to discuss her mother’s illness?','منٹا کے والد اسے اس کی ماں کی بیماری پر بات کرنے کے لیے کہاں لے جاتے ہیں؟','د منټا پلار هغه د هغې د مور د ناروغۍ د خبرو لپاره چېرته وړي؟'),
('Which approach would you have preferred — deception or honesty — if you had to deal with similar circumstances like Minta’s mother ? Give reasons for your choice.','اگر آپ کو منٹا کی ماں جیسے حالات سے نمٹنا پڑتا تو آپ کون سا طریقہ پسند کرتے — فریب یا دیانت؟ اپنے انتخاب کی وجوہات بتائیں۔','که تاسو باید د منټا د مور په څېر شرایطو سره معامله کړې وای نو کوم طریقه به مو خوښه کړې وای — دوکه که صداقت؟ د خپل انتخاب دلایل ورکړئ.'),
('How did the vitamin pills become the symbol of responsibility?','وٹامن کی گولیاں ذمہ داری کی علامت کیسے بن گئیں؟','د ویټامین ګولۍ د مسؤولیت نښه څنګه شوې؟'),
('How did Minta change over the course of the story? Limit your answer to just five sentences.','کہانی کے دوران منٹا کیسے بدلی؟ اپنا جواب صرف پانچ جملوں تک محدود رکھیں۔','د کیسې په اوږدو کې منټا څنګه بدله شوه؟ خپل ځواب یوازې پنځو جملو ته محدود کړئ.'),
('Why was the blue chair significant? Explain.','نیلی کرسی کیوں اہم تھی؟ وضاحت کریں۔','شین چوکۍ ولې مهمه وه؟ تشریح کړئ.'),
('Explain how Minta knows that her mother accepted death. Why is that knowledge comforting to her?','وضاحت کریں کہ منٹا کیسے جانتی ہے کہ اس کی ماں نے موت کو قبول کر لیا تھا۔ وہ علم اس کے لیے تسلی بخش کیوں ہے؟','تشریح کړئ چې منټا څنګه پوهېږي چې د هغې مور مړینه منلې وه. دا پوهه د هغې لپاره ولې تسلي بښونکې ده؟')]
for i,(a,b,d) in enumerate(RQ,1): Qn(s,f'q{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}','eng11-u04-rc','exercise')
build(s,53,['T:0','rc','ans']+[f'q{i}' for i in range(1,12)],[])
s['vocabulary']=V
s['sourceNote']='Printed page 44. The first row of the table is the end of the entry "splinters" from the previous page (the meaning continues "…off from a larger piece."); its headword cell is empty. Headwords "Spook" and "Tucked(v)" are printed with capital letters. The right edge of the photograph clips line ends in the table and in questions 1, 3, 7, 9 and 11 (for example "universal theme[ ]", "With[ ]", "Give[ ]", "your[ ]", "that[ ]"). The page number 44 is printed in a diamond at the foot. Border lines, a pink corner flag and the watermark are excluded; a partial footer at the bottom edge is excluded.'
save(s)
# ---------- scan 54 (printed 45) ----------
V={}
s=page(54,U,'45','Writing Suggestions · Oral Communication · Vocabulary and Grammar','لکھنے کی تجاویز · زبانی رابطہ · ذخیرۂ الفاظ اور قواعد','د لیکلو وړاندیزونه · شفاهي اړیکه · لغت او ګرامر','writing-vocab-grammar')
F=Flow(s)
H(s,'wsh','Writing Suggestions','لکھنے کی تجاویز','د لیکلو وړاندیزونه',tab='writing')
add(s,'ws','Write down the character sketch of Minta.','منٹا کا کردار خاکہ لکھیں۔','د منټا د کردار انځور ولیکئ.',tab='writing',role='question',exerciseId='eng11-u04-writing')
H(s,'oc','Oral Communication','زبانی رابطہ','شفاهي اړیکه',tab='language')
add(s,'wp','Working in pair','جوڑی میں کام','په جوړه کې کار',tab='language',kind='heading')
add(s,'ot','Compare and contrast the characters of Minta’s father and mother. Who do like the most? Justify with reasons.','منٹا کے والد اور والدہ کے کرداروں کا موازنہ اور تضاد کریں۔ آپ کو کون سب سے زیادہ پسند ہے؟ وجوہات کے ساتھ جواز پیش کریں۔','د منټا د پلار او مور کردارونه پرتله کړئ او توپیر یې ښودل. تاسو کوم یو ډېر خوښوئ؟ په دلایلو سره توجیه یې کړئ.',tab='language')
H(s,'vg','Vocabulary and Grammar','ذخیرۂ الفاظ اور قواعد','لغت او ګرامر',tab='vocabulary')
H(s,'v','Vocabulary','ذخیرۂ الفاظ','لغت',tab='vocabulary')
Qn(s,'vi','Look for the meaning of the following emotive words in dictionary. Find their antonyms in an authentic thesaurus. Now write the correct word for the emotions expressed in each statement.','درج ذیل جذباتی الفاظ کے معنی لغت میں دیکھیں۔ ان کے متضاد مستند ترادف نامے میں تلاش کریں۔ اب ہر بیان میں ظاہر ہونے والے جذبات کے لیے درست لفظ لکھیں۔','د لاندې احساساتي کلمو معنا په قاموس کې وګورئ. د هغو ضد معنا په معتبر ترادف‌نامه کې ومومئ. اوس د هر بیان کې څرګند شویو احساساتو لپاره سمه کلمه ولیکئ.','eng11-u04-vocab','vocabulary')
add(s,'vw','lazy, vengeful, vain, snobbish, sympathetic, arrogant, ambitious, proud','lazy، vengeful، vain، snobbish، sympathetic، arrogant، ambitious، proud','lazy، vengeful، vain، snobbish، sympathetic، arrogant، ambitious، proud',tab='vocabulary',sourceGap=dict(note='The eight words are printed in two rows of four on pink strips.'))
VQ=[('1. There’s no house in town better than mine. ____________','1. شہر میں میرے گھر سے بہتر کوئی گھر نہیں۔ ____________','1. په ښار کې له ما د کور ښه کوم کور نشته. ____________'),('2. I can’t stand talking to poor people. ____________','2. میں غریب لوگوں سے بات کرنا برداشت نہیں کر سکتا۔ ____________','2. زه له غریبو خلکو سره خبرې کول نشم زغملای. ____________'),('3. My son did really well in his exam. ____________','3. میرے بیٹے نے اپنے امتحان میں واقعی اچھا کیا۔ ____________','3. زما زوی په خپله ازموینه کې په رښتیا ښه وکړل. ____________'),('4. Oh, my hair looks wonderful today. ____________','4. اوہ، آج میرے بال شاندار لگ رہے ہیں۔ ____________','4. اوه، نن زما ویښتان ډېر ښه ښکاري. ____________'),('5. I just don’t want to get out of bed today. ____________','5. مجھے آج بستر سے اٹھنے کا بالکل دل نہیں چاہتا۔ ____________','5. زه نن یوازې نه غواړم له بستر څخه پاڅېږم. ____________'),('6. I will own my own business within five years. ____________','6. میں پانچ سال کے اندر اپنا کاروبار کروں گا۔ ____________','6. زه به په پنځو کلونو کې خپل سوداګرۍ ولرم. ____________'),('7. Sajida, I understand what you are going through. ____________','7. ساجدہ، میں سمجھتا ہوں کہ تم کس سے گزر رہی ہو۔ ____________','7. ساجده، زه پوهېږم چې ته په څه تېرېږې. ____________'),('8. I’ll never forget what she did to me. ____________','8. میں کبھی نہیں بھولوں گا کہ اس نے میرے ساتھ کیا کیا۔ ____________','8. زه به هېڅکله هېر نه کړم چې هغې ماته څه وکړل. ____________')]
for i,(a,b,d) in enumerate(VQ,1): Qn(s,f'v{i}',a,b,d,'eng11-u04-vocab','vocabulary')
H(s,'gr','GRAMMAR','قواعد','ګرامر',tab='grammar')
Qn(s,'ga','A. Choose one of the relative pronouns who, which or whose to fill in the blanks.','الف. خالی جگہیں پُر کرنے کے لیے موصولی ضمائر who، which یا whose میں سے ایک منتخب کریں۔','a. تشې ډکولو لپاره له نسبتي ضمیرونو who، which یا whose څخه یو وټاکئ.','eng11-u04-grammar','grammar')
GA=[('1. I talked to the girl ____________ car had broken down in front of the shop.','1. میں نے اس لڑکی سے بات کی ____________ کی گاڑی دکان کے سامنے خراب ہو گئی تھی۔','1. ما له هغې نجلۍ سره خبرې وکړې ____________ موټر د هټۍ مخې ته خراب شوی و.'),('2. Mr. Nizam, ____________ is a taxi driver, lives on the corner.','2. جناب نظام، ____________ ٹیکسی ڈرائیور ہیں، کونے پر رہتے ہیں۔','2. ښاغلی نظام، ____________ د ټیکسۍ چلوونکی دی، په کونج کې اوسېږي.'),('3. I live in a house in Hayatabad ____________ is in Peshawar.','3. میں حیات آباد کے ایک گھر میں رہتا ہوں ____________ پشاور میں ہے۔','3. زه په حیات اباد کې په یوه کور کې اوسېږم ____________ په پېښور کې دی.'),('4. This is the girl ____________ comes from Spain.','4. یہ وہ لڑکی ہے ____________ اسپین سے آتی ہے۔','4. دا هغه نجلۍ ده ____________ له هسپانیا څخه راځي.'),('5. That’s Abrar, the boy ____________ has just arrived at the airport.','5. وہ ابرار ہے، وہ لڑکا ____________ ابھی ہوائی اڈے پر پہنچا ہے۔','5. دا ابرار دی، هغه هلک ____________ تازه هوايي ډګر ته رسېدلی دی.')]
for i,(a,b,d) in enumerate(GA,1): Qn(s,f'g{i}',a,b,d,'eng11-u04-grammar','grammar',**({'sourceGap':dict(note='The exercise continues on the next page.')} if i==5 else {}))
F.done()
s['vocabulary']=V
s['sourceNote']='Printed page 45. Pink banners head "Writing Suggestions", "Oral Communication" and "Vocabulary and Grammar". In the vocabulary exercise each statement is followed by a printed blank line at the right. The page number 45 is printed in a diamond at the foot. Border lines, a pink corner flag and the watermark are excluded; a partial footer at the bottom edge is excluded.'
save(s)
