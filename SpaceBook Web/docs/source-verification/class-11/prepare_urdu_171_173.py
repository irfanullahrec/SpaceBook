from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,u,**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'urdu11-{u}-q',tab='exercise',**k)
def V(s,u1,u2,e1,e2,p1,p2): add(s,f'v{len(s["paras"])+1}',e1+'\n'+e2,u1+'\n'+u2,p1+'\n'+p2,listType='poem',kind='verse')
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded.'
# scan 171 = printed 164
s=page(171,'g01','164','Exercise (Mashq) on the ghazals of Mir: questions 2–4; definition of ghazal','مشق: غزلیاتِ میر پر سوالات: سوال 2 تا 4؛ غزل کی تعریف','تمرین: د میر غزلونو پوښتنې: ۲ تر ۴ پوښتنې؛ د غزل تعریف','ex2')
F=Flow(s)
Q(s,'2۔ «کہیں کیا جو پوچھے کوئی ہم سے میرؔ / جہاں میں تم آئے تھے، کیا کر چلے» میرؔ کی غزل کے اس مقطع کی تشریح کریں نیز یہ بھی واضح کریں، کہ اس میں علمِ بیان کی کون سی خوبی پائی جاتی ہے؟','2. “What shall we say if someone asks us, Mir, / ‘You came into the world; what did you do and depart?’” Explain this maqta of Mir’s ghazal and also make clear what merit of the science of expression (ilm-e-bayan) is found in it.','۲. «څه ووایو که څوک له موږ نه وپوښتي میر / په نړۍ کې راغلئ، څه مو وکړل او ولاړئ» د میر د غزل دا مقطع تشریح کړئ او همدارنګه څرګنده کړئ چې پدې کې د علم بیان کومه ښېګڼه موندل کېږي؟',u='g01')
Q(s,'3۔ مندرجہ ذیل مصرعوں کے ساتھ دوسرا مصرع لگا کر شعر مکمل کریں۔','3. Complete the couplet by adding the second line to the following lines.','۳. له لاندې مصرعو سره دویمه مصرعه ورزیاتولو سره شعر بشپړ کړئ.',u='g01')
for t in [('الف) فقیرانہ آئے صدا کر چلے','(a) Faqeerana aaye sada kar chale','(الف) فقیرانه راغلو غږ کولو سره ولاړو'),
('ب) وہ کیا چیز ہے آہ! جس کے لیے','(b) Woh kya cheez hai aah! jis ke liye','(ب) هغه څه شی دی افسوس چې د هغه لپاره'),
('ج) دکھائی دیے یوں کہ بے خود کیا','(c) Dikhai diye yun ke be-khud kiya','(ج) ښکاره شوې داسې چې بې خوده مو کړ'),
('د) پرستش کی یاں تک کہ اے بت تجھے','(d) Parastish ki yaan tak ke ae but tujhe','(د) ستاسو پرستش مو دومره وکړه ای بته'),
('ہ) کہیں کیا، جو پوچھے کوئی ہم سے میرؔ','(e) Kahen kya, jo poochhe koi hum se Mir','(ه) څه ووایو که څوک له موږ وپوښتي میر')]:
    add(s,f'i{len(s["paras"])+1}',t[1],t[0],t[2],listGroup='ex-3')
Q(s,'4۔ میرؔ کی شاعرانہ خصوصیات پر نوٹ لکھیں۔','4. Write a note on the poetic characteristics of Mir.','۴. د میر په شاعرانه ځانګړتیاوو یادداشت ولیکئ.',u='g01')
H(s,'غزل کی تعریف:','Definition of ghazal:','د غزل تعریف:')
P(s,'غزل کا لفظ عربی زبان کا ایک مصدر ہے، جس کے معنی «کا تنا» (چرخے پر روئی سے سُوت) «وہ ما گر» بنانا ہے۔','The word ghazal is a verbal noun of the Arabic language, whose meaning is “spinning” (making thread from cotton on the spinning wheel). (the Urdu gloss in the scan is printed in a small blurred hand; read approximately)','د غزل کلمه د عربي ژبې یو مصدر دی چې معنا یې «ګنډل» (په چرخه کې له پنبې نه تار جوړول) ده. (د سکین په اردو تفسیر کې لیکنه کوچنۍ او تیاره ده؛ تقریباً لوستل شوې)',boxed=True)
P(s,'ادب کی رو سے غزل کے معنی ہیں عورتوں سے باتیں کرنا، عورتوں کے حُسن و جمال کی تعریف کرنا۔','In literature the meaning of ghazal is to talk with women, to praise the beauty and charm of women.','د ادب له مخې د غزل معنا له ښځو سره خبرې کول، د ښځو د حسن او جمال ستاینه کول ده.',boxed=True)
P(s,'غزل نظم کی ایک صنف ہے جس میں عشق و محبّت (حقیقی و مجازی) کا ذکر ہوتا ہے۔','The ghazal is a genre of nazm in which love and affection (real and metaphorical) is mentioned.','غزل د نظم یو ډول دی چې په هغه کې د عشق او مینې (حقیقي او مجازي) یادونه کېږي.',boxed=True)
P(s,'غزل کے کم از کم اشعار کی تعداد پانچ اور زیادہ کی کوئی حد مقرر نہیں ہے۔','The minimum number of couplets in a ghazal is five and no limit is fixed for the maximum.','د غزل لږترلږه د شعرونو شمېر پنځه دی او د زیاتو کومه حد نه دی ټاکل شوی.',boxed=True)
F.done()
s['sourceNote']='Printed page 164 (scan 171): questions 2–4 (question 2 quotes the maqta; question 3 gives five half-lines in blue), and the blue box “غزل کی تعریف” (four sentences). The scan is slightly out of focus and a finger covers the top-left corner; the first sentence of the box is read approximately.'+NOTE
s['vocabulary']={}
save(s)
# scan 172 = printed 165
s=page(172,'g02','165','Khwaja Mir Dard (poet profile)','خواجہ میر درد (شاعر کا تعارف)','خواجه میر درد (د شاعر پېژندنه)','author')
F=Flow(s)
H(s,'خواجہ میر درد','Khwaja Mir Dard','خواجه میر درد')
P(s,'پیدایش: ۱۷۲۰ء — وفات: ۱۷۸۵ء','Born: 1720 — Died: 1785','زېږېدنه: ۱۷۲۰ز — وفات: ۱۷۸۵ز')
P(s,'خواجہ میر دردؔ دِلّی میں پیدا ہوئے۔ گو تصوّف کے مضامین اُردو کے بیشتر شعرا نے باندھے ہیں لیکن ان میں جو تکمیلی شان دردؔ نے پیدا کی ہے، وہ انھی کا حصّہ ہے۔ اس کی بڑی وجہ یہ بھی ہے کہ وہ صوفی تھے۔ دردؔ قلبی واردات کے اظہار کے لیے جن الفاظ کا چناؤ کرتے ہیں، یوں محسوس ہوتا ہے جیسے وہ الفاظ بنے ہی اس مقصد کے لیے ہوں۔ دردؔ کی صوفیانہ شاعری وحدت الوجود اور وحدت الشہود کے فلسفوں کا خوب صورت امتزاج پیش کرتی ہے۔ خواجہ میر دردؔ تصوّف کے فلسفیانہ مضامین کو جس بے ساختگی اور سادگی سے بیان کرتے ہیں، وہ انھی کے ساتھ مخصوص ہے۔ اُن کی غزل میں تغزّل صرف تصوّف کی بدولت پیدا ہوتی ہے۔ دردؔ کے ہاں عشق اور تصوّف ایک دوسرے سے الگ نہیں بل کہ باہم مربوط ہیں۔ انھوں نے محاورہ اور روز مرّہ کثرت سے استعمال کیا اور نہ صرف غزل کی تہذیبی روایت پیدا کی بل کہ اسے ارتقا کے اگلے زینے پر چڑھنے کا راستہ بھی دکھایا۔ اُردو شاعری کو دردؔ نے ایک ہی مجموعۂ کلام (دیوانِ درد) دیا ہے، لیکن معیار کے اعتبار سے وہ اتنا بلند پایہ ہے کہ اسے کسی صورت نظر انداز نہیں کیا جا سکتا اور جس نے دردؔ کو غزل گو شعرا کے صفِ اوّل میں کھڑا کر دیا ہے۔','Khwaja Mir Dard was born in Delhi. Although the themes of Sufism have been composed by most Urdu poets, the culminating splendour that Dard created in them is his own portion. A big reason for this is also that he was a Sufi. The words that Dard chooses to express experiences of the heart seem as if those words had been made for this very purpose. Dard’s Sufi poetry presents a beautiful blend of the philosophies of wahdat-ul-wujood and wahdat-ush-shuhood. The spontaneity and simplicity with which Khwaja Mir Dard expresses the philosophical themes of Sufism is peculiar to him alone. In his ghazal the lyric quality arises only by virtue of Sufism. In Dard love and Sufism are not separate from each other but interlinked. He used idiom and everyday speech abundantly and not only created the cultural tradition of the ghazal but also showed it the way to climb to the next stair of evolution. Dard gave Urdu poetry only one collection (Diwan-e-Dard), but in terms of standard it is of such high rank that it cannot in any way be ignored, and it has made Dard stand in the first row of ghazal poets.','خواجه میر درد په دهلي کې زېږېدلی دی. که څه هم د تصوف مضامین د اردو ډېرو شاعرانو جوړ کړي دي خو پدې کې چې کومه بشپړونکې شان درد پیدا کړی دی هغه د هغه ځانګړې برخه ده. د دې لوی لامل دا هم دی چې هغه صوفي و. درد د زړه د واردات د څرګندولو لپاره چې کوم الفاظ ټاکي داسې احساسېږي لکه دغه الفاظ د همدې موخې لپاره جوړ شوي وي. د درد صوفیانه شاعري د وحدت الوجود او وحدت الشهود د فلسفو ښکلی ګډوالی وړاندې کوي. خواجه میر درد د تصوف فلسفي مضامین چې په کومې بې ساختګۍ او سادګۍ بیانوي هغه د هغه سره ځانګړی دی. د هغه په غزل کې تغزل یوازې د تصوف په برکت پیدا کېږي. د درد سره عشق او تصوف یو له بل نه جلا نه بلکې یو له بل سره تړلي دي. هغه محاوره او روزمره ډېره کارولې او نه یوازې یې د غزل تهذیبي روایت پیدا کړ بلکې هغې ته یې د ارتقا په راتلونکي زینه د خېژېدو لاره هم وښوده. اردو شاعرۍ ته درد یوازې یوه شعري ټولګه (دیوان درد) ورکړې ده خو د معیار له مخې هغه دومره لوړ دی چې په هېڅ ډول نشي نظرانداز کېدای او چې درد یې د غزل ګو شاعرانو په لومړۍ کتار کې ودرولی دی.')
P(s,'تصانیف: شمعِ محفل، آہِ سرد، نالۂ دردؔ، واردات، دردِ دل اور علم الکتاب۔','Works: Shama-e-Mehfil, Aah-e-Sard, Naala-e-Dard, Waaridaat, Dard-e-Dil and Ilm-ul-Kitab.','تصنیفات: شمع محفل، آه سرد، ناله درد، واردات، درد دل او علم الکتاب.')
F.done()
s['sourceNote']='Printed page 165 (scan 172): ornamental title “خواجہ میر درد”, portrait (not reproduced), birth/death boxes (1720 and 1785), biography and list of works.'+NOTE
s['vocabulary']={}
save(s)
# scan 173 = printed 166
s=page(173,'g02','166','Ghazal (Khwaja Mir Dard): “Qatl-e-aashiq kisi mashooq se kuchh door na tha”','غزل (خواجہ میر درد): «قتلِ عاشق کسی معشوق سے کچھ دور نہ تھا»','غزل (خواجه میر درد): «د عاشق وژل له کوم معشوق نه لرې نه و»','poem1')
F=Flow(s)
H(s,'غزل','Ghazal','غزل')
for r in [
('قتلِ عاشق کسی معشوق سے کچھ دور نہ تھا','پر ترے عہد کے آگے تو یہ دستور نہ تھا','The killing of a lover was not far from any beloved,','but before your age this was not the custom.','د عاشق وژل له کوم معشوق نه څه لرې نه و','خو ستا د دور په وړاندې دا دستور نه و'),
('رات مجلس میں ترے حسن کے شعلے کے حضور','شمع کے منہ پہ جو دیکھا، تو کہیں نور نہ تھا','Last night in the assembly, in the presence of the flame of your beauty,','when I looked at the face of the candle there was no light anywhere.','د تیرې شپې په مجلس کې ستا د حسن د شعلې په حضور کې','د شمعې پر مخ مې چې وکتل نو هېڅ رڼا نه وه'),
('ذکر میرا ہی وہ کرتا تھا صریحاً لیکن','میں نے پوچھا تو کہا، خیر یہ مذکور نہ تھا','He used to mention me explicitly, yet','when I asked he said, “Never mind, this was not mentioned.”','هغه زما یادونه په څرګنده کوله خو','چې ما وپوښتل نو وې ویل، خیر دا ذکر نه و'),
('باوجودے کہ پر و بال نہ تھے آدم کے','وہاں پہنچا کہ فرشتے کا بھی مقدور نہ تھا','Although Adam had neither wings nor feathers,','he reached where even the angel had no power to reach.','که څه هم د آدم وزرونه نه وو','هلته ورسېد چېرته چې د فرښتې هم وس نه و'),
('پرورشِ غم کی ترے یاں تئیں تو کی، دیکھا','کوئی بھی داغ تھا سینے میں کہ ناسور نہ تھا','Here in your care I have nurtured grief; see,','there was no scar in the breast that was not an ulcer.','د ستا د غم روزنه مې دلته وکړه، وګوره','په سینه کې کوم داغ نه و چې ناسور نه و'),
('مُحتسِب آج تو مے خانے میں تیرے ہاتھوں','دل نہ تھا کوئی، کہ شیشے کی طرح چُور نہ تھا','Muhtasib, today in the tavern because of you','there was no heart that was not shattered like a glass.','محتسبه نن په میخانه کې ستا په لاس','کوم زړه نه و چې د شیشې په څېر ماتې نه و'),
('دردؔ کے ملنے سے اے یار! بُرا کیوں مانا','اس کو کچھ اور سوا دید کے منظور نہ تھا','Friend! Why did you take offence at meeting Dard?','He desired nothing else besides the sight.','ای ملګریه! د درد له ملاقات نه ولې بد ګڼې','هغه ته له لیدو پرته بل څه منظور نه و')]:
    V(s,*r)
P(s,'(دیوانِ درد، مرتبہ: خلیل الرحمن داؤدی)','(Diwan-e-Dard, compiled by Khalil-ur-Rahman Dawoodi)','(دیوان درد، ترتیب کوونکی: خلیل الرحمن داودي)')
F.done()
s['sourceNote']='Printed page 166 (scan 173): title “غزل”, running head “خواجہ میر درد”, the ghazal (six couplets in two-line form plus the closing couplet with the pen-name “درد”) and the source line “(دیوانِ درد مرتبہ خلیل الرحمن داؤدی)”; the printed page number at the foot is cropped.'+NOTE
s['vocabulary']={}
save(s)
