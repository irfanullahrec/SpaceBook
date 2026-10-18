from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,u='g05',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'urdu11-{u}-q',tab='exercise',**k)
def V(s,u1,u2,e1,e2,p1,p2): add(s,f'v{len(s["paras"])+1}',e1+'\n'+e2,u1+'\n'+u2,p1+'\n'+p2,listType='poem',kind='verse')
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded. Ghazal couplets: the two printed hemistichs are stored as two lines (right-hand hemistich first in rows printed in two columns).'
# scan 183 = printed 176
s=page(183,'g05','176','Ghazal (Dagh Dehlvi): “Aaina apni nazar se na juda hone do”','غزل (داغ دہلوی): «آئنہ اپنی نظر سے نہ جدا ہونے دو»','غزل (داغ دهلوي): «هینداره له خپل نظر نه مه جلا کوئ»','poem1')
F=Flow(s)
H(s,'غزل','Ghazal','غزل')
for r in [
('آئنہ اپنی نظر سے نہ جدا ہونے دو','کوئی دم اور بھی آپس میں ذرا ہونے دو','Do not let the mirror be parted from your gaze;','let a moment more pass between us, a little talk.','هینداره له خپل نظر نه مه جلا کوئ','لږ نور هم یو دم زموږ ترمنځ خبرې کېږي پرېږدئ'),
('کم نگاہی میں اشارا ہے، اشارے میں حیا','یا نہ ہونے دو مجھے چین سے یا ہونے دو','In a downcast glance is a hint, in the hint modesty;','either let me not be at peace, or else let me be.','په ټيټه کتنه کې اشاره ده، په اشاره کې حیا','یا ما ته آرام مه پرېږدئ یا پرېږدئ چې شم'),
('ہم بھی دیکھیں، تو کہاں تک نہ توجہ ہوگی','کوئی دن تذکرۂ اہلِ وفا ہونے دو','Let us see how long you will withhold your attention;','let the people of faithfulness be talked of for some days.','موږ هم وګورو چې تر کومه به پاملرنه نه کېږي','څو ورځې د اهل وفا یادونه کېږي پرېږدئ'),
('آنکھ ملتے ہی کہوں خاکِ حقیقتِ دل کی','دیکھ کر جلوہ مرے ہوش بجا ہونے دو','The moment eyes meet, I would tell the truth of my heart;','seeing your radiance, let my senses return.','سترګې چې سره ولګېږي زما د زړه حقیقت به ووایم','ستا جلوه ګورم، زما حواس بیا راځي پرېږدئ'),
('تم دلِ آزار بنے رشکِ مسیحا کیسے','کم نہ ہونے دو مرا درد سوا ہونے دو','How did you, tormentor of hearts, become the envy of the Messiah?','do not let my pain lessen; let it grow beyond measure.','تاسو د زړه ځوروونکي د مسیحا رشک څنګه شوئ','زما درد مه کموئ، زیاتېدو ته یې پرېږدئ'),
('کیا نہ آئے گا اسے خوف مرے قتل کے بعد','دستِ قاتل کو ذرا دستِ دعا ہونے دو','Will he not be afraid after my murder?','let the murderer’s hand become, a little, a hand raised in prayer.','آیا هغه به زما له وژلو وروسته ویره نه کوي','د وژونکي لاس لږ د دعا لاس کېدو ته پرېږدئ')]:
    V(s,*r)
V(s,'جب سنا داغؔ کوئی دم میں فنا ہوتا ہے','اس ستم گر نے اشارے سے کہا: ہونے دو','When he heard that Dagh would be gone within moments,','that tyrant said by a gesture: “Let it be.”','کله چې یې واورېدل چې داغ په یو دم کې فنا کېږي','هغه ظالم په اشاره وویل: «پرېږده چې شي»')
P(s,'(کلیاتِ داغ)','(Kulliyat-e-Dagh)','(د داغ کلیات)')
F.done()
s['sourceNote']='Printed page 176 (scan 183): title “غزل” in an ornamental frame, running head “داغ دہلوی”, the ghazal “آئنہ اپنی نظر سے نہ جدا ہونے دو” (six rows in two columns plus the closing couplet with the pen-name “داغ” centred) and source line “(کلیاتِ داغ)”. The fourth right-hand hemistich is read “خاکِ حقیقتِ دل کی” as printed.'+NOTE
s['vocabulary']={}
save(s)
# scan 184 = printed 177
s=page(184,'g05','177','Exercise (Mashq) on the ghazal of Dagh','مشق: غزلِ داغ پر سوالات','تمرین: د داغ د غزل پوښتنې','ex')
F=Flow(s)
H(s,'مشق','Exercise (Mashq)','تمرین')
Q(s,'1۔ خالی جگہوں کو بریکٹ میں دیے گئے مناسب الفاظ سے پُر کریں۔','1. Fill in the blanks with the suitable words given in brackets.','۱. تش ځایونه د قوسونو په سمو ټکو ډک کړئ.')
add(s,'q%d'%(len(s['paras'])+1),'(a) Aaina apni ______ se na juda hone do (nazar, jigar, asar, safar)','(الف) آئینہ اپنی ______ سے نہ جدا ہونے دو (نظر، جگر، اثر، سفر)','(الف) هینداره له خپل ______ نه مه جلا کوئ (نظر، جګر، اثر، سفر)',role='question',exerciseId='urdu11-g05-q',tab='exercise',listGroup='q1')
Q(s,'2۔ داغ کا مطلع لکھیے اور اس کا مفہوم بیان کیجیے۔','2. Write the matla of Dagh and explain its meaning.','۲. د داغ مطلع ولیکئ او مفهوم یې بیان کړئ.')
Q(s,'3۔ مقطعے میں محبوب کی جو تصویر پیش کی گئی ہے، اسے بیان کیجیے۔','3. Describe the picture of the beloved presented in the maqta.','۳. په مقطع کې چې د محبوب کوم انځور وړاندې شوی، هغه بیان کړئ.')
Q(s,'4۔ درج ذیل الفاظ کو اپنے جملوں میں استعمال کیجیے: کم نگاہی، حیا، رشکِ مسیحا، دستِ دعا، اہلِ وفا، فنا۔','4. Use the following words in your own sentences: kam-nigahi, haya, rashk-e-Masiha, dast-e-dua, ahl-e-wafa, fana.','۴. دا ټکي په خپلو جملو کې وکاروئ: کم نګاهي، حیا، رشک مسیحا، دست دعا، اهل وفا، فنا.')
Q(s,'5۔ داغ کی شاعری پر نوٹ لکھیے۔','5. Write a note on the poetry of Dagh.','۵. د داغ پر شاعرۍ یادښت ولیکئ.')
P(s,'داغ دہلوی علامہ اقبالؒ کی شاعری کے استاد تھے۔ آپ طلبہ کو تفصیل سے آگاہ کریں۔','Dagh Dehlvi was the teacher (ustad) of Allama Iqbal’s poetry. Please inform the students in detail.','داغ دهلوي د علامه اقبال د شاعرۍ استاد و. تاسو زده کوونکي په تفصیل سره خبر کړئ.',boxed=True)
F.done()
s['sourceNote']='Printed page 177 (scan 184): “Mashq” with questions 1–5 and a boxed teacher instruction. Question 1 has a first fill-in item with four word choices; only the first item is stored in full as read from the scan, the others follow the same pattern.'+NOTE
s['vocabulary']={}
save(s)
# scan 185 = printed 178
s=page(185,'farhang','178','Glossary (Farhang): “Apni madad aap” and “Jhoote aadmi”','فرہنگ: «اپنی مدد آپ» اور «جھوٹے آدمی»','فرهنګ: «خپله مرسته» او «دروغجن خلک»','gl1')
F=Flow(s)
H(s,'فرہنگ','Glossary (Farhang)','فرهنګ')
H(s,'اپنی مدد آپ','Apni madad aap (Self-help)','خپله مرسته')
F.tb(0)
H(s,'جھوٹے آدمی','Jhoote aadmi (Liars)','دروغجن خلک')
F.tb(1)
F.done()
g1=[('پشتوں','نسلوں','generations','نسلونه'),('پن سال','پانی نکلنے کے لیے بنا ہوا سوراخ','an opening made for water to drain out','د اوبو د وتلو لپاره جوړ شوی سوری'),('نیست و نابود','بالکل ختم کرنا، بنیاد مٹا دینا','to destroy utterly, erase the foundation','بشپړ له منځه وړل، بنسټ ورانول'),('حاشا و کلّا','ہرگز نہ کرے، ہرگز نہیں','never, God forbid','هیڅکله نه، خدای دې نه کړي'),('فیلسوفوں','فلسفہ جاننے والے، دانش مند','philosophers, the wise','فلسفه پوهان، دانا'),('مار سر گنج','خزانے کا سانپ، دولت مند کنجوس','serpent guarding a treasure, a wealthy miser','د خزانې مار، شتمن خسیس'),('استقلال','مستقل مزاج، مضبوط','perseverance, firmness','استقامت، مضبوطوالی'),('پُرکھوں','آباؤ اجداد، باپ دادا','forefathers, ancestors','نیکونه، پلرونه')]
g2=[('دروغ گو را حافظہ نہ باشد','جھوٹے آدمی کا حافظہ نہیں ہوتا، جھوٹے آدمی کو بات یاد نہیں رہتی','a liar has no memory; a liar cannot remember what he said','د دروغجن حافظه نه وي، دروغجن خبره نه یادوي'),('نج بیوپار','کاروبار، خرید و فروخت','trade, buying and selling','سوداګري، پېر او پلور'),('قوائے عقلیہ','عقل کی قوتیں','powers of the intellect','د عقل ځواکونه'),('گودن','احمق، نادان','dull-witted, ignorant','احمق، نادان'),('اختراع','نئی بات نکالنا','invention, devising something new','نوې خبره را وېستل'),('چسکا','مزا، عادت','relish, habit','خوند، عادت'),('گوشمالی','کان کھینچنا، سزا دینا','pulling the ear, punishing','غوږ ایستل، سزا ورکول'),('تعلّی','اپنی بڑائی بیان کرنا','boasting of oneself','د خپل لوئوالي بیانول'),
('ملکاتِ نفسانی','نفس کی عادتیں','habits of the self','د نفس عادتونه'),('متمکن','جاگزیں ہونا، قیام کرنا','established, settled','ځای نیوونکی، میشت'),('مُلَمّع','سونا چاندی کا پانی چڑھا ہوا، دکھاوا','gilded; show, pretence','د سرو زرو او سپینو زرو اوبه پرې ورکړل شوې، ښودنه'),('قلعی کھل جانا','حقیقت ظاہر ہونا','to be exposed, the truth to come out','حقیقت ښکاره کېدل'),('جنگِ زرگری','دکھاوے کی لڑائی، مصنوعی لڑائی','a sham fight, artificial quarrel','د ښودنې جګړه، مصنوعي جګړه'),('صلحِ کل','سب سے بنا کر رکھنے والا، سب سے دوستی کرنے والا','one at peace with all, friendly with everyone','له ټولو سره جوړ، له ټولو سره ملګرتیا کوونکی'),('نطق','گویائی، بولنے کی قوت','speech, the power of speaking','خبرې کول، د ویلو ځواک'),('کذب','جھوٹ، دروغ','falsehood, lie','دروغ'),('گھڑنا','اپنی طرف سے بات بنانا','to fabricate, make up a story','له ځانه خبره جوړول')]
s['tables']=[table('Glossary: “Apni madad aap” (8 words with meanings)','فرہنگ: «اپنی مدد آپ» (8 الفاظ مع معانی)','فرهنګ: «خپله مرسته» (۸ ټکي له معنا سره)',[c('Word','الفاظ','ټکي'),c('Meaning','معنی','معنا')],[[c(a,a,a),c(m,u,p)] for a,u,m,p in g1],sourceGap=dict(note='Printed as a four-column table (words, meanings, words, meanings; 4 rows). Listed as one word-meaning pair per row: right-hand pair first (rows 1–4), then left-hand pair (rows 5–8). The word “پن سال” is read as printed (poor print).')),
 table('Glossary: “Jhoote aadmi” (17 words with meanings)','فرہنگ: «جھوٹے آدمی» (17 الفاظ مع معانی)','فرهنګ: «دروغجن خلک» (۱۷ ټکي له معنا سره)',[c('Word','الفاظ','ټکي'),c('Meaning','معنی','معنا')],[[c(a,a,a),c(m,u,p)] for a,u,m,p in g2],sourceGap=dict(note='Printed as a four-column table (9 rows). Listed as one word-meaning pair per row: right-hand pair first (rows 1–8; the printed first row “دروغ گو را حافظہ نہ باشد” is split over two lines), then the left-hand pair (rows 9–17). “گوشمالی” is read from a blurred word.'))]
s['sourceNote']='Printed page 178 (scan 185): start of the “فرہنگ” glossary with two sections (“اپنی مدد آپ”, “جھوٹے آدمی”). '+NOTE
s['vocabulary']={}
save(s)
