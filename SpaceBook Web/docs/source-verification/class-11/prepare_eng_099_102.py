from enghelp import *
c=cell
U='u09'
V={}
def Qn(s,key,en,ur,ps,ex,tab,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,tab=tab,**m)
def H(s,key,en,ur,ps,tab=None,**m):
    d=dict(kind='heading',**m)
    if tab: d['tab']=tab
    add(s,key,en,ur,ps,**d)
# ---------- scan 99 (printed 90) ----------
s=page(99,U,'90','Glossary (end) · Reading Comprehension · Writing Suggestions','فرہنگ (اختتام) · مطالعے کا فہم · لکھنے کی تجاویز','لغتنامه (پای) · د لوست پوهه · د لیکلو وړاندیزونه','glossary-rc-writing')
F=Flow(s)
G=[('shed (n) (continued)','animals, or as a workshop. “a bicycle shed”','جانوروں کے لیے، یا ورکشاپ کے طور پر۔ “سائیکل شیڈ”','د څارویو لپاره، یا د کارځای په توګه. “د بایسکل سیېبان”','شیڈ','سیېبان'),
('skewers (n)','a long piece of wood or metal used for holding pieces of food, typically meat, together during cooking.','لکڑی یا دھات کا لمبا ٹکڑا جو پکانے کے دوران کھانے کے ٹکڑوں، عموماً گوشت، کو ایک ساتھ تھامنے کے لیے استعمال ہوتا ہے۔','د لرګي یا فلز اوږد ټوټه چې د پخلي پر مهال د خوړو ټوټې، معمولاً غوښه، سره ساتلو لپاره کارېږي.','سیخیں','سیخونه'),
('stooped (adj)','(of a person) having the head and shoulders habitually bent forwards.','(کسی شخص کا) جس کا سر اور کندھے عادتاً آگے کی طرف جھکے ہوں۔','(د یو کس) چې سر او اوږې یې عادتاً مخکې ته کوږې وي.','جھکا ہوا','کوږ'),
('timid (adj)','showing a lack of courage or confidence; easily frightened.','ہمت یا اعتماد کی کمی ظاہر کرنے والا؛ آسانی سے ڈرنے والا۔','د زړورتیا یا باور نشتوالی ښودونکی؛ په اسانۍ ویرېدونکی.','شرمیلا','ویرجن'),
('untethered (v)','release or free from a tether.','رسی یا بندھن سے چھوڑنا یا آزاد کرنا۔','له ټر یا بند څخه خلاصول یا آزادول.','کھول دیا','خلاص کړ')]
s['tables']=[table('Glossary (continued)','فرہنگ (جاری)','لغتنامه (دوام)',[c('Word','لفظ','کلمه'),c('Meaning','معنی','معنا')],[[c(w,uw,pw),c(m,mu,mp)] for w,m,mu,mp,uw,pw in G],tab='glossary')]
F.tb(0)
for w,m,mu,mp,uw,pw in G: V[w.split(' (')[0]]=dict(ur=uw,ps=pw)
H(s,'rch','Reading Comprehension','مطالعے کا فہم','د لوست پوهه')
Qn(s,'ans','Answer the following questions.','درج ذیل سوالات کے جواب دیں۔','لاندې پوښتنو ته ځواب ورکړئ.','eng11-u09-rc','exercise')
RQ=[('What arrangements were made by Navasard for the coming home Arshak?','نواسرد نے ارشک کے گھر آنے کے لیے کیا انتظامات کیے؟','نواسرد د ارشک د کور ته د راتګ لپاره کوم تدارک وکړ؟'),
('Why was Navasard so excited at the arrival of Arshak?','نواسرد ارشک کی آمد پر اتنا پرجوش کیوں تھا؟','نواسرد د ارشک په راتګ ولې دومره په ولوله کې و؟'),
('Describe the plight of Navasard after the departure of Arshak without meeting him.','ارشک کے اس سے ملے بغیر چلے جانے کے بعد نواسرد کی حالتِ زار بیان کریں۔','د ارشک له هغه سره له لیدلو پرته د تللو وروسته د نواسرد حال بیان کړئ.'),
('What is the central idea of the story ‘The White Lamb’. Is this theme relevant to our culture as well?','کہانی ‘سفید برہ’ کا مرکزی خیال کیا ہے؟ کیا یہ موضوع ہماری ثقافت سے بھی متعلق ہے؟','د کیسې ‘سپینه وری’ مرکزي مفکوره څه ده؟ ایا دا موضوع زموږ له کلتور سره هم تړاو لري؟'),
('Write down the plot of the story ‘The White Lamb’.','کہانی ‘سفید برہ’ کا پلاٹ لکھیں۔','د کیسې ‘سپینه وری’ پلاټ ولیکئ.'),
('Is there any conflict in the story ‘The White Lamb’? If yes, how is it resolved?','کیا کہانی ‘سفید برہ’ میں کوئی تنازع ہے؟ اگر ہاں تو وہ کیسے حل ہوتا ہے؟','ایا په کیسه ‘سپینه وری’ کې کومه شخړه شته؟ که هو، نو څنګه حل کېږي؟'),
('How would you resolve the conflict if you were the author of ‘The White Lamb’.','اگر آپ ‘سفید برہ’ کے مصنف ہوتے تو آپ تنازع کو کیسے حل کرتے؟','که ته د ‘سپینه وری’ لیکوال وای نو دې شخړه به دې څنګه حل کړې وای؟'),
('Compare and contrast the character of Navasard and Arshak.','نواسرد اور ارشک کے کردار کا موازنہ اور تقابل کریں۔','د نواسرد او ارشک کرکټر پرتله او توپیر وکړئ.'),
('‘How sharper than a serpent’s tooth it is to have thankless child.’ (Shakespeare). Critically evaluate this statement in the light of the text of lesson ‘The White Lamb’.','‘ناشکرا اولاد رکھنا سانپ کے دانت سے کتنا زیادہ تیز ہے۔’ (شیکسپیئر)۔ سبق ‘سفید برہ’ کے متن کی روشنی میں اس بیان کا تنقیدی جائزہ لیں۔','‘ناشکره اولاد لرل د مار د غاښ نه څومره تېز دی.’ (شکسپیر). د درس ‘سپینه وری’ د متن په رڼا کې دا بیان په انتقادي ډول وارزوئ.')]
for i,(a,b,d) in enumerate(RQ,1): Qn(s,f'q{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}','eng11-u09-rc','exercise',sourceGap=dict(note='The right edge of the page is clipped by the photograph; the words at the end of lines are read from context.')) if i in (1,3,4,6,7,9) else Qn(s,f'q{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}','eng11-u09-rc','exercise')
H(s,'wsh','Writing Suggestions','لکھنے کی تجاویز','د لیکلو وړاندیزونه',tab='writing')
add(s,'wa','(A) Draw the character of Arshak. Was he justified in leaving village without meeting Navasard?','(الف) ارشک کے کردار کا خاکہ کھینچیں۔ کیا وہ نواسرد سے ملے بغیر گاؤں چھوڑنے میں حق بجانب تھا؟','(الف) د ارشک کرکټر انځور کړئ. ایا هغه له نواسرد سره له لیدلو پرته له کلي نه تګ کې حق ته و؟',tab='writing',sourceGap=dict(note='The right edge is clipped ("withou[t]").'))
add(s,'wb','(B) Imagine Arshak has come along to Navasard’s house. Now, taking cue from the text of the story ‘the White Lamb’, write their most likely conversation as one page dialogue.','(ب) تصور کریں کہ ارشک نواسرد کے گھر آ گیا ہے۔ اب کہانی ‘سفید برہ’ کے متن سے اشارہ لے کر ان کی ممکنہ گفتگو ایک صفحے کے مکالمے کی صورت میں لکھیں۔','(ب) انګېرنه وکړئ چې ارشک د نواسرد کور ته راغلی دی. اوس د کیسې ‘سپینه وری’ د متن نه اشاره اخیستو سره د دوی احتمالي خبرې د یوې پاڼې مکالمې په بڼه ولیکئ.',tab='writing',sourceGap=dict(note='The right edge is clipped ("cu[e]", "lik[ely]").'))
F.done()
s['sourceNote']='Printed page 90. The page begins in the middle of the glossary table: the first row completes the meaning of "shed (n)" from the previous page (the Word cell of the first row is shown here as "shed (n) (continued)" by us). A pink "Reading Comprehension" banner and a pink "Writing Suggestions" banner follow. The right edge of the page is clipped (words at the ends of lines are read from context; "Shakespeare" is printed in brackets). The Urdu and Pashto columns of the glossary are added by us. Border lines, pink corner flags, the "awazeinqilab" watermark and a "Whatsapp" strip at the foot are excluded. The page number 90 is printed in a diamond at the foot.'
s['vocabulary']=V
save(s)
# ---------- scan 100 (printed 91) ----------
V={}
s=page(100,U,'91','Oral Communication · Vocabulary · Grammar: transitive or intransitive','زبانی رابطہ · ذخیرۂ الفاظ · قواعد: متعدی یا لازم','شفاهي اړیکه · لغت · ګرامر: متعدي یا لازمي','oral-vocab-grammar')
F=Flow(s)
H(s,'oc','Oral Communication','زبانی رابطہ','شفاهي اړیکه',tab='language')
add(s,'o1','Ask the students to search the following terms on internet: (a) social mobility (b) social class (c) social hierarchy (d) horizontal social mobility (e) vertical social mobility','طلبہ سے کہیں کہ درج ذیل اصطلاحات انٹرنیٹ پر تلاش کریں: (الف) سماجی نقل و حرکت (ب) سماجی طبقہ (ج) سماجی درجہ بندی (د) افقی سماجی نقل و حرکت (ہ) عمودی سماجی نقل و حرکت','له زده کوونکو وغواړئ چې لاندې اصطلاحات په انټرنیټ وپلټي: (الف) ټولنیز خوځښت (ب) ټولنیز ټولګی (ج) ټولنیز درجه‌بندي (د) افقي ټولنیز خوځښت (ه) عمودي ټولنیز خوځښت',tab='language')
add(s,'o2','Now arrange a group discussion, keeping in view its conventions and dynamics, and share this information with your group members and discuss the character and behaviour of Arshak in the light of these newly learnt terms.','اب گروہی بحث کا اہتمام کریں، اس کے اصولوں اور حرکیات کو مدنظر رکھتے ہوئے، اور یہ معلومات اپنے گروپ کے ارکان کے ساتھ شیئر کریں اور ان نئی سیکھی گئی اصطلاحات کی روشنی میں ارشک کے کردار اور برتاؤ پر بات کریں۔','اوس یوه ډله‌ییزه بحث تنظیم کړئ، د هغې دودونه او حرکیات په نظر کې نیولو سره، او دا معلومات له خپلې ډلې غړو سره شریک کړئ او د دې نوو زده شویو اصطلاحاتو په رڼا کې د ارشک کرکټر او چلند وڅېړئ.',tab='language')
H(s,'vg','Vocabulary and Grammar','ذخیرۂ الفاظ اور قواعد','لغت او ګرامر',tab='vocabulary')
H(s,'v','Vocabulary','ذخیرۂ الفاظ','لغت',tab='vocabulary')
Qn(s,'vi','Use the words in parenthesis to form a new word to fill in the blanks.','قوسین میں دیے گئے الفاظ سے نیا لفظ بنا کر خالی جگہیں پُر کریں۔','د قوس په منځ کې ورکړل شوي کلمې وکاروئ ترڅو نوې کلمه جوړه کړئ او تشې ډکې کړئ.','eng11-u09-vocab','vocabulary')
Qn(s,'vp','According to experts, the way you spend your free time is vital to your general ______ (HAPPY), and ______ (GET) the right balance is very important. It goes without saying that physical ______ (FIT) is the key, so everyone’s leisure time should include some form of exercise, ______ (IDEAL) something that you find ______ (ENJOY). Most people also gain ______ (SATISFY) from doing something ______ (CREATE), such as painting, cooking or gardening. However, not all your free time ______ (ACTIVE) should be solitary or you may end up feeling lonely. ______ (COMPANION) is also important to most people’s sense of well-being. But you must find the right kind of social ______ (INTERACT). ______ (MEMBER) in some groups, such as ______ (POLITICS) parties can simply lead to stress and ______ (FRUSTRATE). Joining a ______ (SOCIETY) group like a blood donation society or yoga classes are likely to be much more ______ (BENEFIT).','ماہرین کے مطابق، آپ اپنا فارغ وقت جس طرح گزارتے ہیں وہ آپ کی عمومی ______ (HAPPY) کے لیے اہم ہے، اور درست توازن ______ (GET) بہت ضروری ہے۔ یہ کہے بغیر ظاہر ہے کہ جسمانی ______ (FIT) کلید ہے، لہٰذا ہر ایک کے فارغ وقت میں کسی نہ کسی شکل کی ورزش شامل ہونی چاہیے، ______ (IDEAL) کوئی ایسی چیز جو آپ کو ______ (ENJOY) لگے۔ زیادہ تر لوگ کوئی ______ (CREATE) کام کرنے سے بھی ______ (SATISFY) پاتے ہیں، جیسے مصوری، کھانا پکانا یا باغبانی۔ تاہم، آپ کا سارا فارغ وقت ______ (ACTIVE) تنہائی میں نہیں گزرنا چاہیے ورنہ آپ تنہائی محسوس کر سکتے ہیں۔ ______ (COMPANION) بھی زیادہ تر لوگوں کے احساسِ بہبود کے لیے اہم ہے۔ لیکن آپ کو درست قسم کا سماجی ______ (INTERACT) تلاش کرنا ہوگا۔ کچھ گروہوں میں ______ (MEMBER) جیسے ______ (POLITICS) جماعتیں محض تناؤ اور ______ (FRUSTRATE) کا باعث بن سکتی ہیں۔ خون عطیہ کرنے والی انجمن یا یوگا کلاسوں جیسے ______ (SOCIETY) گروپ میں شامل ہونا کہیں زیادہ ______ (BENEFIT) ہونے کا امکان ہے۔','د متخصصانو په وینا، هغه ډول چې ته خپل خالي وخت تېروې ستا د عمومي ______ (HAPPY) لپاره مهم دی، او سم انډول ______ (GET) ډېر مهم دی. ویل ضروري نه دي چې بدني ______ (FIT) کلیدي ده، نو د هر چا خالي وخت باید د تمرین یوه بڼه ولري، ______ (IDEAL) یو څه چې تاسو ______ (ENJOY) وګڼئ. ډېر خلک هم د یو ______ (CREATE) کار کولو څخه ______ (SATISFY) ترلاسه کوي، لکه انځورګري، پخلی یا باغوانۍ. خو، ستا ټول خالي وخت ______ (ACTIVE) باید یوازېتوب نه وي که نه ته به یوازېتوب احساس کړې. ______ (COMPANION) هم د ډېرو خلکو د هوساینې لپاره مهم دی. خو تاسو باید سم ډول ټولنیز ______ (INTERACT) ومومئ. په ځینو ډلو کې ______ (MEMBER) لکه ______ (POLITICS) ګوندونه کېدای شي یوازې فشار او ______ (FRUSTRATE) رامنځته کړي. یو ______ (SOCIETY) ډله لکه د وینې ورکولو ټولنه یا د یوګا ټولګي کېدای شي ډېر ______ (BENEFIT) وي.','eng11-u09-vocab','vocabulary')
H(s,'gr','Grammar','قواعد','ګرامر',tab='grammar')
H(s,'gt','Transitive or Intransitive','متعدی یا لازم','متعدي یا لازمي',tab='grammar')
Qn(s,'ga','A. Tell whether the verbs in colour are transitive or intransitive. Put a tick on the correct option.','الف. بتائیں کہ رنگین افعال متعدی ہیں یا لازم۔ درست آپشن پر ٹک لگائیں۔','الف. ووایئ چې رنګین فعلونه متعدي دي که لازمي. په سم انتخاب ټیک ولګوئ.','eng11-u09-grammar','grammar')
GA=[('She was crying all day long.','وہ سارا دن روتی رہی۔','هغې ټوله ورځ ژړل.'),
('We showed her the photo album.','ہم نے اسے فوٹو البم دکھایا۔','موږ هغې ته د انځورونو البم وښود.')]
for i,(a,b,d) in enumerate(GA,1): Qn(s,f'a{i}',f'{i}. {a} (Transitive/ Intransitive)',f'{i}. {b} (متعدی / لازم)',f'{i}. {d} (متعدي / لازمي)','eng11-u09-grammar','grammar')
F.done()
s['sourceNote']='Printed page 91. Pink banners "Oral Communication" and "Vocabulary and Grammar". The vocabulary exercise is one running paragraph with 15 blanks (each followed by a capitalised base word in parentheses); the blanks are shown as underscores. In the grammar exercise the verbs in colour are "crying" and "showed"; each sentence is followed at the right by "(Transitive/ Intransitive)". Handwritten marks, the upside-down header strip and the watermark are excluded. The page number 91 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 101 (printed 92) ----------
s=page(101,U,'92','Grammar: transitive or intransitive (continued) · Teacher\'s Guideline','قواعد: متعدی یا لازم (جاری) · استاد کی رہنمائی','ګرامر: متعدي یا لازمي (دوام) · د ښوونکي لارښوونه','grammar-2')
F=Flow(s)
GA=[('The doctor advised me to exercise regularly.','ڈاکٹر نے مجھے باقاعدگی سے ورزش کرنے کا مشورہ دیا۔','ډاکټر ماته مشوره راکړه چې په منظمه توګه تمرین وکړم.'),
('It was raining at that time.','اس وقت بارش ہو رہی تھی۔','په هغه وخت کې باران وریده.'),
('She laughed at the joke.','وہ لطیفے پر ہنسی۔','هغې په ټوکه وخندل.'),
('She gave a cookie to the child.','اس نے بچے کو ایک بسکٹ دیا۔','هغې ماشوم ته یو بسکټ ورکړ.'),
('They slept in the street.','وہ گلی میں سوئے۔','هغوی په کوڅه کې ویده شول.'),
('I ate the cherries.','میں نے چیریاں کھائیں۔','ما چیرۍ وخوړې.'),
('My father doesn’t drink coffee.','میرے والد کافی نہیں پیتے۔','زما پلار کافي نه څښي.'),
('He always keeps his money in a wallet.','وہ ہمیشہ اپنے پیسے بٹوے میں رکھتا ہے۔','هغه تل خپلې پیسې په بټوه کې ساتي.')]
for i,(a,b,d) in enumerate(GA,3): Qn(s,f'a{i}',f'{i}. {a} (Transitive/ Intransitive)',f'{i}. {b} (متعدی / لازم)',f'{i}. {d} (متعدي / لازمي)','eng11-u09-grammar','grammar')
Qn(s,'gb','B. Tell whether the verbs in the following sentences are transitive or intransitive then use these verbs in your own sentences.','ب. بتائیں کہ درج ذیل جملوں میں افعال متعدی ہیں یا لازم، پھر ان افعال کو اپنے جملوں میں استعمال کریں۔','ب. ووایئ چې په لاندې جملو کې فعلونه متعدي دي که لازمي، بیا دا فعلونه په خپلو جملو کې وکاروئ.','eng11-u09-grammar','grammar')
GB=[('Some ants fight fiercely.','کچھ چیونٹیاں شدت سے لڑتی ہیں۔','ځینې مېږي سخت جګړه کوي.'),
('The explosion sank the ship.','دھماکے نے جہاز کو ڈبو دیا۔','چاودنې بېړۍ ډوبه کړه.'),
('He spoke loudly.','وہ زور سے بولا۔','هغه په لوړ غږ خبرې وکړې.'),
('Boil the water.','پانی ابالیں۔','اوبه وجوشوئ.'),
('The horse kicked the boy.','گھوڑے نے لڑکے کو لات ماری۔','آس هلک ته لغته وکړه.'),
('The watchman blew his whistle.','چوکیدار نے اپنی سیٹی بجائی۔','څارونکي خپل سیټۍ وغږوله.'),
('He took shelter under a tree.','اس نے درخت کے نیچے پناہ لی۔','هغه د ونې لاندې پناه واخیسته.'),
('The birds sang sweetly.','پرندوں نے میٹھا گایا۔','مرغانو په خوږ غږ سندرې ویلې.'),
('The fire burns brightly.','آگ روشن جل رہی ہے۔','اور روښانه سوځي.'),
('Birds fly in the sky.','پرندے آسمان میں اڑتے ہیں۔','مرغان په اسمان کې الوځي.'),
('Time heals all wounds','وقت تمام زخم بھر دیتا ہے','وخت ټول زخمونه ښه کوي'),
('You surprised me.','تم نے مجھے حیران کر دیا۔','تا ما حیران کړم.'),
('Do sit down.','براہِ کرم بیٹھ جائیں۔','مهرباني وکړئ کېنئ.'),
('I usually sleep well.','میں عموماً اچھی نیند سوتا ہوں۔','زه معمولاً ښه ویده کېږم.'),
('Let’s eat something.','آئیں کچھ کھائیں۔','راځئ یو څه وخورو.')]
for i,(a,b,d) in enumerate(GB,1): Qn(s,f'b{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}','eng11-u09-grammar','grammar')
H(s,'tg','Teacher’s Guideline:','استاد کی رہنمائی:','د ښوونکي لارښوونه:')
add(s,'tgt','Explain and revise with the students the use of transitive and intransitive verbs.','طلبہ کو متعدی اور لازم افعال کے استعمال کی وضاحت کریں اور اس کا اعادہ کریں۔','زده کوونکو ته د متعدي او لازمي فعلونو کارول تشریح او تکرار کړئ.')
F.done()
s['sourceNote']='Printed page 92. Part A continues with eight sentences, each with its verb printed in colour (advised, raining, laughed, gave, slept, ate, drink, keeps) and "(Transitive/ Intransitive)" at the right; the right edge of the page clips part of these tags. Part B lists 15 sentences. The page ends with a pink "Teacher\'s Guideline" banner. Border lines, pink corner flags, the watermark and the "Whatsapp" strip are excluded. The page number 92 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 102 (printed 93) ----------
s=page(102,'u10','93','Unit 10: The World is Too Much With Us · Learning outcomes','یونٹ 10: دنیا ہم پر بہت حاوی ہے · سیکھنے کے نتائج','واحد 10: نړۍ پر موږ ډېره غالبه ده · د زده کړې پایلې','unit10-outcomes',layout='outcomes')
F=Flow(s)
H(s,'unit','Unit 10','یونٹ 10','واحد 10')
H(s,'title','The World is Too Much With Us','دنیا ہم پر بہت حاوی ہے','نړۍ پر موږ ډېره غالبه ده')
add(s,'au','William Wordsworth','ولیم ورڈز ورتھ','ولیم ورډزورت')
add(s,'intro','By the end of the unit, the students will be able to:','یونٹ کے اختتام تک طلبہ اس قابل ہوں گے کہ:','د واحد په پای کې به زده کوونکي وکولای شي چې:')
O=[('use critical thinking to respond orally and in writing to the text (post-reading) to:','تنقیدی سوچ استعمال کر کے متن (پڑھنے کے بعد) کا زبانی اور تحریری جواب دیں تاکہ:','انتقادي فکر وکاروي ترڅو متن ته (له لوستلو وروسته) په شفاهي او لیکلي ډول ځواب ورکړي ترڅو:'),
('• give a personal opinion and justify stance related to viewpoints/ideas and issues in the text read.','• پڑھے گئے متن میں موجود نقطہ ہائے نظر/خیالات اور مسائل سے متعلق ذاتی رائے دیں اور اپنے موقف کا جواز پیش کریں۔','• په لوستل شوي متن کې د لیدلورو/نظرونو او مسایلو په اړه شخصي نظر ورکړي او خپل دریځ توجیه کړي.'),
('• relate what is read to his or her own feelings and experiences.','• جو کچھ پڑھا گیا اسے اپنے احساسات اور تجربات سے جوڑیں۔','• هغه څه چې لوستل شوي د خپلو احساساتو او تجربو سره وتړي.'),
('• scan to answer short questions.','• مختصر سوالات کے جواب دینے کے لیے سرسری نظر ڈالیں (اسکین کریں)۔','• د لنډو پوښتنو د ځواب لپاره سکین وکړي (په چټکۍ وګوري).'),
('read a given poem and give orally and in writing:','دی گئی نظم پڑھیں اور زبانی اور تحریری طور پر دیں:','ورکړل شوې نظم ولولي او په شفاهي او لیکلي ډول ورکړي:'),
('• theme and its development.','• موضوع اور اس کی نشوونما۔','• موضوع او د هغې پرمختګ.'),
('• personal response with justification.','• جواز کے ساتھ ذاتی ردِعمل۔','• د توجیه سره شخصي غبرګون.'),
('• recognize literary techniques such as personification and alliteration.','• ادبی تکنیکوں مثلاً تشخیص (جان ڈالنا) اور تکرارِ حروف کو پہچانیں۔','• ادبي تخنیکونه لکه شخصیت‌بخښنه او د توري تکرار وپېژني.'),
('analyse how a writer/ poet uses language to:','تجزیہ کریں کہ ایک مصنف/شاعر زبان کو کیسے استعمال کرتا ہے تاکہ:','تحلیل کړي چې یو لیکوال/شاعر ژبه څنګه کاروي ترڅو:'),
('• appeal to the senses through use of figurative language including similes, metaphors and imagery','• تشبیہات، استعارات اور پیکر تراشی سمیت علامتی زبان کے ذریعے حواس سے اپیل کرے','• د تشبیهاتو، استعارو او انځورګرۍ په ګډون د مجازي ژبې په کارولو سره حواسو ته اپیل وکړي'),
('• set tone.','• لہجہ قائم کرے۔','• لهجه جوړه کړي.'),
('recognize and use varying intonation patterns as aids in spoken and written to highlight focus in meaning.','بولنے اور لکھنے میں معنی کے مرکز کو نمایاں کرنے کے لیے مدد کے طور پر مختلف لہجے کے نمونوں کو پہچانیں اور استعمال کریں۔','په خبرو او لیکنه کې د معنا د تمرکز د روښانه کولو لپاره د مرستې په توګه بېلابېل د غږ لوړ ټیټ بڼې وپېژني او وکاروي.'),
('illustrate use of dictionary for finding the appropriate meaning and correct spelling.','موزوں معنی اور درست املا تلاش کرنے کے لیے لغت کے استعمال کی مثال دیں۔','د مناسب معنا او سمې املا موندلو لپاره د قاموس کارول وښيي.'),
('make and use present and past participles.','حال اور ماضی کے اسمِ فاعل/مفعول (participles) بنائیں اور استعمال کریں۔','د حال او تېر زمان participles جوړ کړي او وکاروي.')]
for i,(a,b,d) in enumerate(O,1): add(s,f'o{i}',a,b,d,listGroup='outcomes')
F.done()
s['sourceNote']='Printed page 93: Unit 10 opening page with the unit number, the title banner "The World is Too Much With Us", the poet tag "William Wordsworth" and the list of learning outcomes with nested bullets (the printed bullets "•" are shown in the text of the sub-items). The page number 93 is printed in a diamond at the foot. Border lines, pink corner flags, the watermark and the upside-down header strip are excluded.'
s['vocabulary']={}
save(s)
