from enghelp import *
c=cell
U='u15'
def Qn(s,key,en,ur,ps,ex,tab,**m): add(s,key,en,ur,ps,role='question',exerciseId=ex,tab=tab,**m)
def Op(s,key,en,ur,ps,ex,tab='grammar',**m): add(s,key,en,ur,ps,role='option',exerciseId=ex,tab=tab,**m)
def H(s,key,en,ur,ps,tab=None,**m):
    d=dict(kind='heading',**m)
    if tab: d['tab']=tab
    add(s,key,en,ur,ps,**d)
VEX='eng11-u15-vocab'; GEX='eng11-u15-grammar'
# ---------- scan 151 (printed 142) ----------
s=page(151,U,'142','Vocabulary exercise (end, B, C) · Grammar: order of adjectives','ذخیرۂ الفاظ کی مشق (اختتام، ب، ج) · قواعد: صفات کی ترتیب','د لغت تمرین (پای، ب، ج) · ګرامر: د صفتونو ترتیب','vocab-order-adjective')
F=Flow(s)
VQ=[('Everyone has been so ______ since I lost my job. (SYMPATHY)','جب سے میری نوکری گئی ہے ہر کوئی بہت ______ رہا ہے۔ (SYMPATHY)','له هغه وخته چې ما دنده له لاسه ورکړه هر څوک ډېر ______ دی. (SYMPATHY)'),
('There is a slight ______ that you’ll get the job. (POSSIBLE)','اس بات کا معمولی سا ______ ہے کہ آپ کو نوکری مل جائے۔ (POSSIBLE)','یو لږ ______ شته چې تاسو دنده ومومئ. (POSSIBLE)'),
('The teacher asked the students to write a ______ of the text. (SUMMARISE)','استاد نے طلبہ سے کہا کہ متن کا ______ لکھیں۔ (SUMMARISE)','ښوونکي له زده کوونکو وغوښتل چې د متن یو ______ ولیکي. (SUMMARISE)'),
('Writing speeches for ______ is his specialty. (POLITICS)','______ کے لیے تقریریں لکھنا اس کی خاصیت ہے۔ (POLITICS)','د ______ لپاره وینا لیکل د هغه تخصص دی. (POLITICS)')]
for i,(a,b,d) in enumerate(VQ,9): Qn(s,f'v{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',VEX,'vocabulary')
Qn(s,'vb','B. Read the words in the list below. Use two words from the list to make one compound word and use them in sentences.','ب. نیچے فہرست کے الفاظ پڑھیں۔ فہرست میں سے دو الفاظ ملا کر ایک مرکب لفظ بنائیں اور انہیں جملوں میں استعمال کریں۔','ب. لاندې لیست کلمې ولولئ. له لیست څخه دوه کلمې یوځای کړئ ترڅو یوه مرکبه کلمه جوړه شي او په جملو کې یې وکاروئ.',VEX,'vocabulary')
add(s,'vbw','grand, space, door, shake, room, air, half; broad, father, soft, board, boat, in, walk; out, bell, mother, hand, plane, milk, steam; suit, mate, ball, way','grand، space، door، shake، room، air، half؛ broad، father، soft، board، boat، in، walk؛ out، bell، mother، hand، plane، milk، steam؛ suit، mate، ball، way','grand، space، door، shake، room، air، half؛ broad، father، soft، board، boat، in، walk؛ out، bell، mother، hand، plane، milk، steam؛ suit، mate، ball، way',tab='vocabulary',sourceGap=dict(note='The words are printed in a box of four rows (7 + 7 + 7 + 4 words, read row by row): grand, space, door, shake, room, air, half / broad, father, soft, board, boat, in, walk / out, bell, mother, hand, plane, milk, steam / suit, mate, ball, way.'))
Qn(s,'vc','C. Fill in the blanks with the words below. (one of which may be used twice)','ج. نیچے دیے گئے الفاظ سے خالی جگہیں پُر کریں۔ (ان میں سے ایک دو بار استعمال ہو سکتا ہے)','ج. د لاندې کلمو سره تشې ډکې کړئ. (له هغو یوه کېدای شي دوه ځله وکارول شي)',VEX,'vocabulary')
add(s,'vcw','in case, unless, provided, in the event, whether','in case، unless، provided، in the event، whether','in case، unless، provided، in the event، whether',tab='vocabulary',sourceGap=dict(note='The five words are printed on pink strips: in case, unless, provided, in the event, whether.'))
CQ=[('______ that Jamila sees the broken vase, just tell her the dog ran into it.','______ جمیلہ ٹوٹا ہوا گلدان دیکھ لے، بس اسے بتا دینا کہ کتا اس سے ٹکرا گیا۔','______ جمیله مات ګلدان ووینې، یوازې ورته ووایه چې سپي ورسره ټکر شو.'),
('Take my phone number with you when you travel ______ you need to get in contact with me.','سفر کرتے وقت میرا فون نمبر ساتھ رکھیں ______ آپ کو مجھ سے رابطہ کرنے کی ضرورت پڑے۔','کله چې سفر کوئ زما د تلیفون شمېره له ځان سره ولرئ ______ تاسو ته له ما سره د اړیکې اړتیا شي.'),
('______ that you have filled out the form correctly, you should get your refund within seven working days.','______ آپ نے فارم درست طور پر پُر کیا ہو، آپ کو سات کاری دنوں کے اندر رقم کی واپسی مل جانی چاہیے۔','______ تاسو فورمه په سمه ډکه کړې وي، تاسو باید په اوو کاري ورځو کې خپله بېرته ورکړه ومومئ.'),
('______ you tell me where to go, I’ll get lost.','______ آپ مجھے بتائیں کہ کہاں جانا ہے، میں کھو جاؤں گا۔','______ تاسو ماته ووایئ چې چېرته لاړ شم، زه به ورک شم.'),
('Bring these chips with you ______ you get hungry on the journey.','یہ چپس اپنے ساتھ لے آئیں ______ آپ کو سفر میں بھوک لگے۔','دا چپس له ځان سره راوړئ ______ تاسو په سفر کې وږي شئ.'),
('Jasmine needs to know ______ you still want to buy her old car or not.','جیسمین کو جاننا ہے ______ آپ اب بھی اس کی پرانی کار خریدنا چاہتے ہیں یا نہیں۔','جیسمین باید پوه شي ______ تاسو لا هم د هغې زوړ موټر اخیستل غواړئ که نه.')]
for i,(a,b,d) in enumerate(CQ,1): Qn(s,f'c{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',VEX,'vocabulary')
H(s,'gr','Grammar','قواعد','ګرامر',tab='grammar')
H(s,'go','Order of Adjective','صفات کی ترتیب','د صفتونو ترتیب',tab='grammar')
add(s,'g1','In English, it is common to use more than one adjective to describe a noun. These adjectives must be used in the proper order.','انگریزی میں ایک اسم کو بیان کرنے کے لیے ایک سے زیادہ صفات استعمال کرنا عام ہے۔ یہ صفات درست ترتیب میں استعمال ہونی چاہئیں۔','په انګلیسي کې د یو اسم د تشریح لپاره له یوه ډېر صفتونه کارول عام دي. دا صفتونه باید په سمه ترتیب وکارول شي.',tab='grammar',listGroup='order')
add(s,'g2','Example: Here is a beautiful, red, cloth flag. Why does beautiful come before red? Why does red come before cloth?','مثال: یہ ایک خوبصورت، سرخ، کپڑے کا جھنڈا ہے۔ beautiful، red سے پہلے کیوں آتا ہے؟ red، cloth سے پہلے کیوں آتا ہے؟','بېلګه: دا یوه ښکلې، سره، ټوکر ډوله بیرغ دی. ولې beautiful د red مخکې راځي؟ ولې red د cloth مخکې راځي؟',tab='grammar')
add(s,'g3','Understanding the proper order of adjectives needs practice.','صفات کی درست ترتیب کو سمجھنے کے لیے مشق کی ضرورت ہے۔','د صفتونو د سم ترتیب پوهېدو ته تمرین ته اړتیا ده.',tab='grammar',listGroup='order')
F.done()
s['sourceNote']='Printed page 142. The page begins with items 9–12 of vocabulary Part A (base words in capitals in parentheses), then Part B (a boxed list of 25 words for forming compound words), Part C (five strips and six sentences with blanks), "Grammar" and the sub-heading "Order of Adjective" with two bulleted notes and an example in which "beautiful", "red" and "cloth" are shown in the text (the words "beautiful" and "red" are in italics). Item 5 of Part C reads "Bring these chips with you ___ you get hungry on the journey." Border lines, a pink corner flag, the watermark and the "Whatsapp" strip are excluded. The page number 142 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 152 (printed 143) ----------
s=page(152,U,'143','Grammar: order of adjectives (table, A)','قواعد: صفات کی ترتیب (جدول، الف)','ګرامر: د صفتونو ترتیب (جدول، الف)','order-adjective-table-a')
F=Flow(s)
add(s,'ti','Use the following table to practice using the proper order of adjectives in the following sentences.','درج ذیل جملوں میں صفات کی درست ترتیب استعمال کرنے کی مشق کے لیے درج ذیل جدول استعمال کریں۔','په لاندې جملو کې د صفتونو د سم ترتیب د کارولو د تمرین لپاره لاندې جدول وکاروئ.',tab='grammar')
hdr=[('Number','عدد','شمېر'),('Opinion','رائے','نظر'),('Size','سائز','اندازه'),('Age','عمر','عمر'),('Shape','شکل','شکل'),('Color','رنگ','رنګ'),('Origin','اصل / ملک','اصل'),('Material','مواد','مواد'),('Purpose','مقصد','موخه'),('Noun','اسم','اسم')]
def row(**kw):
    out=[]
    for h,_,_ in hdr:
        v=kw.get(h)
        out.append(c(*v) if v else c('','',''))
    return out
rows=[row(Size=('small','چھوٹا','کوچنی'),Shape=('round','گول','ګردي'),Origin=('Pakistan','پاکستان','پاکستان')),
row(Color=('red','سرخ','سور'),Purpose=('sleeping','سونے کا','د خوب')),
row(Opinion=('generous','فیاض','سخي'),Age=('old','بوڑھا','زوړ'),Noun=('man','آدمی','سړی')),
row(Number=('four','چار','څلور'),Material=('metal','دھات','فلز'))]
s['tables']=[table('Order of adjectives','صفات کی ترتیب','د صفتونو ترتیب',[c(*h) for h in hdr],rows,tab='grammar')]
F.tb(0)
Qn(s,'ga','A. Tell which of the sentences are in the usual correct order of adjective.','الف. بتائیں کہ ان میں سے کون سے جملے صفات کی معمول کی درست ترتیب میں ہیں۔','الف. ووایئ چې له دې جملو څخه کومې د صفتونو په معمولي سمه ترتیب کې دي.',GEX,'grammar')
A=[(['She was wearing red beautiful shoes.','She was wearing beautiful red shoes.'],'وہ جوتے پہنے ہوئے تھی','هغې بوټان اغوستي وو'),
(['He is just an old silly man.','He is just a silly old man.'],'وہ بس ایک بے وقوف بوڑھا آدمی ہے','هغه یوازې یو نادانه زوړ سړی دی'),
(['She bought a new powerful computer.','She bought a powerful new computer.'],'اس نے ایک طاقتور نیا کمپیوٹر خریدا','هغې یو پیاوړی نوی کمپیوټر واخیست'),
(['They have just moved into a modern big house.','They have just moved into a big modern house.'],'وہ ابھی ایک بڑے جدید گھر میں منتقل ہوئے ہیں','هغوی همدا اوس یو لوی عصري کور ته ولېږدېدل'),
(['Last night I watched an interesting German film.','Last night I watched a German interesting film.'],'کل رات میں نے ایک دلچسپ جرمن فلم دیکھی','تېره شپه ما یوه په زړه پورې آلماني فلم ولیده'),
(['I need a new electronic dictionary.','I need an electronic new dictionary.'],'مجھے ایک نیا الیکٹرانک لغت چاہیے','ما ته یو نوی بریښنایي قاموس په کار دی'),
(['My cellar is full of black big spiders.','My cellar is full of big black spiders.'],'میرا تہہ خانہ بڑی کالی مکڑیوں سے بھرا ہے','زما ځمکني تهکاله له لویو تورو غټو لیمو ډک دی'),
(['She was carrying a new beautiful bag.','She was carrying a beautiful new bag.'],'وہ ایک خوبصورت نیا بیگ اٹھائے ہوئے تھی','هغې یو ښکلی نوی کڅوړه پورته کړې وه'),
(['I hate this awful wet weather.','I hate this wet awful weather.'],'مجھے یہ خوفناک گیلا موسم ناپسند ہے','زه دا ناوړه لندې هوا نه خوښوم'),
(['I like that small glass coffee table.','I like that glass small coffee table.','I like that coffee glass small table.'],'مجھے وہ چھوٹی شیشے کی کافی میز پسند ہے','زه هغه کوچنۍ شیشه‌ییزه د کافي مېز خوښوم'),
(['There is a red horrible insect on your back.','There is a horrible red insect on your back.'],'آپ کی پیٹھ پر ایک خوفناک سرخ کیڑا ہے','ستاسو په شا یو ډارونی سور حشره شته'),
(['Sim City is a new exciting computer game.','Sim City is a new computer exciting game.','Sim City is an exciting new computer game.'],'سم سٹی ایک دلچسپ نیا کمپیوٹر گیم ہے','سیم ښار یوه په زړه پورې نوې کمپیوټري لوبه ده')]
for i,(vs,ur,ps) in enumerate(A,1):
    for j,v in enumerate(vs):
        tag=' ('+'ABC'[j]+')'
        Op(s,f'a{i}{"abc"[j]}',f'{i}. {v}' if j==0 else v,(f'{i}. ' if j==0 else '')+ur+tag.replace('A','الف').replace('B','ب').replace('C','ج'),(f'{i}. ' if j==0 else '')+ps+tag,GEX)
F.done()
s['sourceNote']='Printed page 143. The page begins with the sentence "Use the following table to practice…" (the first words are clipped at the left edge) and a table with the columns Number, Opinion, Size, Age, Shape, Color, Origin, Material, Purpose and Noun; its cells hold: small / round / Pakistan; red / sleeping; generous / old / man; four / metal (the row positions follow the print). Part A lists twelve items, each with two or three variants of the same sentence, so the order of adjectives can be compared. The Urdu and Pashto of each variant are translations of the meaning; the variants are marked (A), (B), (C) by us. Border lines, a pink corner flag, the watermark and the phone-number strip are excluded. The page number 143 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 153 (printed 144) ----------
s=page(153,U,'144','Grammar: order of adjectives (A end, B)','قواعد: صفات کی ترتیب (الف کا اختتام، ب)','ګرامر: د صفتونو ترتیب (الف پای، ب)','order-adjective-b')
F=Flow(s)
A=[(['I ate hot delicious soup for lunch.','I ate delicious hot soup for lunch.'],'میں نے دوپہر کے کھانے میں گرم مزیدار سوپ کھایا','ما د غرمې په خواړو کې ګرم خوندور سوپ وخوړ'),
(['They live in a wonderful old wooden house.','They live in an old wonderful wooden house.','They live in a wooden wonderful old house.'],'وہ ایک شاندار پرانے لکڑی کے گھر میں رہتے ہیں','هغوی په یو ښکلي زوړ لرګین کور کې اوسېږي'),
(['They are a heavy loud metal band.','They are a loud heavy metal band.','They are a metal heavy loud band.'],'وہ ایک بھاری اونچی آواز والا میٹل بینڈ ہیں','هغوی یو دروند لوړ غږ لرونکی میټل بانډ دي')]
for n,(vs,ur,ps) in zip((13,14,15),A):
    for j,v in enumerate(vs):
        tag=' ('+'ABC'[j]+')'
        Op(s,f'a{n}{"abc"[j]}',f'{n}. {v}' if j==0 else v,(f'{n}. ' if j==0 else '')+ur+tag.replace('A','الف').replace('B','ب').replace('C','ج'),(f'{n}. ' if j==0 else '')+ps+tag,GEX)
Qn(s,'gb','B. Fill in the blanks with proper order of adjective in the parenthesis.','ب. قوسین میں دیے گئے صفات کی درست ترتیب کے ساتھ خالی جگہیں پُر کریں۔','ب. د قوس په منځ کې د صفتونو په سمه ترتیب تشې ډکې کړئ.',GEX,'grammar')
B=[('We wanted ______ (grey / a / metal) table.','ہم ______ (grey / a / metal) میز چاہتے تھے۔','موږ ______ (grey / a / metal) مېز غوښت.'),
('They bought ______ (red / a / new) car.','انہوں نے ______ (red / a / new) کار خریدی۔','هغوی ______ (red / a / new) موټر واخیست.'),
('She went home and sat on ______ (comfortable/her/ wooden/ old) bed.','وہ گھر گئی اور ______ (comfortable/her/ wooden/ old) بستر پر بیٹھ گئی۔','هغه کور ته ولاړه او پر ______ (comfortable/her/ wooden/ old) بستر کېناسته.'),
('He bought ______ (woollen / a / Bannu / fabulous) suit.','اس نے ______ (woollen / a / Bannu / fabulous) سوٹ خریدا۔','هغه ______ (woollen / a / Bannu / fabulous) سوټ واخیست.'),
('They have ______ (Dutch / black) bicycles.','ان کے پاس ______ (Dutch / black) سائیکلیں ہیں۔','هغوی ______ (Dutch / black) بایسکلونه لري.'),
('He wants ______ (some / French / delicious / really) cheese.','وہ ______ (some / French / delicious / really) پنیر چاہتا ہے۔','هغه ______ (some / French / delicious / really) پنیر غواړي.'),
('______ (young / a / energetic) man walked into the room.','______ (young / a / energetic) آدمی کمرے میں داخل ہوا۔','______ (young / a / energetic) سړی خونې ته ننوتی.'),
('He has ______ (a lot of / old / interesting) books.','اس کے پاس ______ (a lot of / old / interesting) کتابیں ہیں۔','هغه ______ (a lot of / old / interesting) کتابونه لري.'),
('She bought ______ (plastic / red / a / new) lunchbox.','اس نے ______ (plastic / red / a / new) لنچ باکس خریدا۔','هغې ______ (plastic / red / a / new) د غرمې بکس واخیست.'),
('He is looking for ______ (leather / stylish / a /black) bag.','وہ ______ (leather / stylish / a /black) بیگ تلاش کر رہا ہے۔','هغه ______ (leather / stylish / a /black) کڅوړه لټوي.'),
('She dropped ______ (old / beautiful / the) plate and it smashed.','اس نے ______ (old / beautiful / the) پلیٹ گرا دی اور وہ ٹوٹ گئی۔','هغې ______ (old / beautiful / the) پلیټ وغورځوله او ماته شوه.'),
('I want ______ (silk / green / an / amazing) dress.','مجھے ______ (silk / green / an / amazing) لباس چاہیے۔','زه ______ (silk / green / an / amazing) جامه غواړم.'),
('She drank ______ (Italian / black / hot) coffee.','اس نے ______ (Italian / black / hot) کافی پی۔','هغې ______ (Italian / black / hot) کافي وڅښله.'),
('He saw ______ (French / writing / old / an) desk.','اس نے ______ (French / writing / old / an) ڈیسک دیکھا۔','هغه ______ (French / writing / old / an) میز ولید.'),
('They stayed in ______ (little / a / cute) cottage.','وہ ______ (little / a / cute) کاٹیج میں ٹھہرے۔','هغوی په ______ (little / a / cute) کوټۍ کې ودرېدل.'),
('I visited ______ (ancient / a / spooky / German) castle.','میں نے ______ (ancient / a / spooky / German) قلعہ دیکھا۔','ما ______ (ancient / a / spooky / German) کلا وکته.'),
('He has ______ (silver / old / beautiful / a) ring.','اس کے پاس ______ (silver / old / beautiful / a) انگوٹھی ہے۔','هغه ______ (silver / old / beautiful / a) ګوتمۍ لري.'),
('We ate ______ (green / Iranian / round / some) apples.','ہم نے ______ (green / Iranian / round / some) سیب کھائے۔','موږ ______ (green / Iranian / round / some) مڼې وخوړې.'),
('I need ______ (computer / comfortable / a) desk.','مجھے ______ (computer / comfortable / a) ڈیسک چاہیے۔','ما ته ______ (computer / comfortable / a) مېز په کار دی.'),
('They went on holiday to ______ (small / wooden / a / beautiful) cabin.','وہ ______ (small / wooden / a / beautiful) کیبن میں چھٹیاں منانے گئے۔','هغوی ______ (small / wooden / a / beautiful) کیبین ته رخصتۍ ته ولاړل.')]
for i,(a,b,d) in enumerate(B,1): Qn(s,f'b{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',GEX,'grammar')
F.done()
s['sourceNote']='Printed page 144. Items 13–15 of Part A (two or three variants each) and Part B with twenty items, each with the words to arrange in parentheses; the printed parentheses of item 3 read "(comfortable/her/ wooden/ old)", and item 10 uses a slash-like mark ("(leather / stylish / a /black)"), item 14 "(French / writing / old / an)" — read as printed. The Urdu and Pashto of each variant are translations of the meaning; the variants are marked (A), (B), (C) by us. Border lines, a pink corner flag, the watermark and the "Whatsapp" strip are excluded. The page number 144 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
# ---------- scan 154 (printed 145) ----------
s=page(154,U,'145','Grammar: adjective clauses (C) · Teacher\'s Guideline','قواعد: صفتی جملے (ج) · استاد کی رہنمائی','ګرامر: صفتي جملې (ج) · د ښوونکي لارښوونه','adjective-clauses')
F=Flow(s)
Qn(s,'gc','C. Combine two sentences together to make one sentence. Put the adjective clause after the noun that it describes. You can use “who” or “that” to put the clauses together.','ج. دو جملوں کو ملا کر ایک جملہ بنائیں۔ صفتی جملے کو اس اسم کے بعد رکھیں جس کی وہ وضاحت کرتا ہے۔ آپ جملوں کو ملانے کے لیے “who” یا “that” استعمال کر سکتے ہیں۔','ج. دوه جملې یوځای کړئ ترڅو یوه جمله جوړه شي. صفتي جمله د هغه اسم وروسته کېږدئ چې تشریح یې کوي. تاسو کولای شئ جملې سره نښلولو لپاره “who” یا “that” وکاروئ.',GEX,'grammar')
add(s,'ex','Example: The student is a very nice person. / She comes from Lahore. The student who comes from Lahore is a very nice person.','مثال: طالبہ بہت اچھی شخصیت ہے۔ / وہ لاہور سے آتی ہے۔ لاہور سے آنے والی طالبہ بہت اچھی شخصیت ہے۔','بېلګه: زده کوونکې ډېره ښه شخصیت ده. / هغه له لاهور راځي. هغه زده کوونکې چې له لاهور راځي ډېره ښه شخصیت ده.',tab='grammar')
C=[('We sent a package to our relatives. They live in Karachi.','ہم نے اپنے رشتہ داروں کو ایک پیکیج بھیجا۔ وہ کراچی میں رہتے ہیں۔','موږ خپلو خپلوانو ته یو بسته ولېږله. هغوی په کراچۍ کې اوسېږي.'),
('The woman works as a cashier. She sits next to me in class.','عورت کیشیئر کے طور پر کام کرتی ہے۔ وہ کلاس میں میرے ساتھ بیٹھتی ہے۔','ښځه د نغدي سړي په توګه کار کوي. هغه په ټولګي کې زما سره کېني.'),
('That’s the book. Everyone is reading it.','یہ وہ کتاب ہے۔ ہر کوئی اسے پڑھ رہا ہے۔','دا هغه کتاب دی. هر څوک یې لولي.'),
('We bought some trees. Our neighbor told us they were on sale.','ہم نے کچھ درخت خریدے۔ ہمارے پڑوسی نے بتایا کہ وہ سیل پر تھے۔','موږ څو ونې واخیستې. زموږ ګاونډي ویلي چې هغه په پلور وې.'),
('The car has a bad engine. I bought it last month.','کار کا انجن خراب ہے۔ میں نے اسے پچھلے مہینے خریدا۔','د موټر انجن خراب دی. ما دا تېره میاشت واخیست.'),
('I lived in an apartment building. It had a very slow elevator.','میں ایک اپارٹمنٹ بلڈنگ میں رہتا تھا۔ اس میں بہت سست لفٹ تھی۔','زه په یوه اپارتمان ودانۍ کې اوسېدم. هغه ډېر ورو لفټ درلود.'),
('You should see a doctor. He can help you with your back problems.','آپ کو ڈاکٹر کو دکھانا چاہیے۔ وہ آپ کی کمر کے مسائل میں مدد کر سکتا ہے۔','تاسو باید ډاکټر ته ورشئ. هغه کولای شي ستاسو د شا په ستونزو کې مرسته وکړي.'),
('The tornado was extremely powerful. It hit Minnesota.','طوفان انتہائی طاقتور تھا۔ اس نے مینیسوٹا کو نشانہ بنایا۔','طوفان ډېر پیاوړی و. هغه مینیسوټا ته ورسېد.'),
('We saw the woman at the grocery store. She lives next door to us.','ہم نے عورت کو گروسری اسٹور پر دیکھا۔ وہ ہمارے برابر والے گھر میں رہتی ہے۔','موږ ښځه د خوراکي توکو په هټۍ کې ولیده. هغه زموږ د ګاونډ کور کې اوسېږي.'),
('My wife returned the pants. They were too big for me.','میری بیوی نے پتلون واپس کر دی۔ وہ میرے لیے بہت بڑی تھی۔','زما ښځې پتلون بېرته ورکړ. هغه ماته ډېر لوی و.')]
for i,(a,b,d) in enumerate(C,1): Qn(s,f'c{i}',f'{i}. {a}',f'{i}. {b}',f'{i}. {d}',GEX,'grammar')
H(s,'tg','Teacher’s Guideline:','استاد کی رہنمائی:','د ښوونکي لارښوونه:')
add(s,'tgt','Explain and revise with the students the use of adjectives phrases and classes.','طلبہ کو صفتی فقروں اور جملوں (clauses) کے استعمال کی وضاحت کریں اور اس کا اعادہ کریں۔','زده کوونکو ته د صفتي عبارتونو او جملو (clauses) کارول تشریح او تکرار کړئ.')
F.done()
s['sourceNote']='Printed page 145. Part C: the instruction, an example in which the answer ("The student who comes from Lahore is a very nice person.") is underlined, ten pairs of sentences to combine, a large blank space and the pink "Teacher\'s Guideline" banner. The printed text of the guideline reads "adjectives phrases and classes" (for "adjective phrases and clauses"); kept as printed. Border lines, pink corner flags, the watermark and the phone-number strip are excluded. The page number 145 is printed in a diamond at the foot.'
s['vocabulary']={}
save(s)
