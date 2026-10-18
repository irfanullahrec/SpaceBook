from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,u='g04',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'urdu11-{u}-q',tab='exercise',**k)
def V(s,u1,u2,e1,e2,p1,p2): add(s,f'v{len(s["paras"])+1}',e1+'\n'+e2,u1+'\n'+u2,p1+'\n'+p2,listType='poem',kind='verse')
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded.'
# scan 180 = printed 173
s=page(180,'g04','173','Ghazal (Ghalib): “Hazaron khwahishen aisi ke har khwahish pe dam nikle”','غزل (غالب): «ہزاروں خواہشیں ایسی کہ ہر خواہش پہ دم نکلے»','غزل (غالب): «زرګونه هیلې داسې چې هره هیله ساه ووځي»','poem2')
F=Flow(s)
P(s,'(۲)','(2)','(۲)')
for r in [
('ہزاروں خواہشیں ایسی کہ ہر خواہش پہ دم نکلے','بہت نکلے مرے ارمان، لیکن پھر بھی کم نکلے','Thousands of desires such that for every desire the breath departs;','many of my longings were fulfilled, yet still too few.','زرګونه هیلې داسې چې هره هیله ساه ووځي','ډېرې زما هیلې پوره شوې خو بیا هم لږې'),
('ڈرے کیوں میرا قاتل کیا رہے گا اس کی گردن پر','وہ خوں، جو چشمِ تر سے عمر بھر یوں دم بہ دم نکلے؟','Why should my murderer fear? What will remain on his neck?','that blood which flows moment by moment all life long from the wet eye?','ولې دې زما وژونکی ووېریږي څه به د هغه پر غاړه پاتې شي','هغه وینه چې له لندې سترګې ټول عمر دم په دم راوځي'),
('نکلنا خلد سے آدمؑ کا سنتے آئے ہیں، لیکن','بہت بے آبرو ہو کر ترے کوچے سے ہم نکلے','We have heard of Adam’s expulsion from Paradise, but','we left your lane with much greater disgrace.','د آدم له جنت نه وتل موږ اورېدلي دي خو','موږ ستا له کوڅې ډېر بې عزته وتو'),
('بھرم کھل جائے ظالم تیرے قامت کی درازی کا','اگر اس طرۂ پُر پیچ و خم کا پیچ و خم نکلے','Your pride in the tallness of your stature would be exposed, tyrant,','if the twist and curve of that twisted curl were to straighten out.','ظالمه ستا د قد د اوږدوالي بهرم به ورک شي','که د دغې پېچلې زلفې پېچ او خم وغځېږي'),
('ہوئی جن سے توقع خستگی کی داد پانے کی','وہ ہم سے بھی زیادہ خستۂ تیغِ ستم نکلے','Those from whom we expected praise for our weariness','turned out even more worn down by the sword of tyranny than we.','هغوی چې له هغو نه د خستګۍ د ستاینې توقع وه','هغوی له موږ نه هم ډېر د ظلم د توري ټپيان راووتل'),
('محبّت میں نہیں ہے فرق مرنے اور جینے کا','اُسی کو دیکھ کر جیتے ہیں جس کافر پہ دم نکلے','In love there is no difference between dying and living;','we live by seeing that very infidel for whom the breath departs.','په مینه کې د مرګ او ژوند ترمنځ توپیر نشته','په هغه ژوند کوو چې په کوم کافر ساه ووځي'),
('کہاں مے خانے کا دروازہ غالبؔ اور کہاں واعظ','پر اتنا جانتے ہیں، کل وہ جاتا تھا کہ ہم نکلے','Where is the door of the tavern, Ghalib, and where the preacher?','but this much we know: yesterday he was going in as we came out.','چېرته د میخانې دروازه غالبه او چېرته واعظ','خو دومره پوهېږو، پرون هغه ننوتو او موږ ووتو')]:
    V(s,*r)
P(s,'(دیوانِ غالب)','(Diwan-e-Ghalib)','(دیوان غالب)')
F.done()
s['sourceNote']='Printed page 173 (scan 180): the badge “(۲)” and the second ghazal of Ghalib (six couplets and the closing couplet with the pen-name “غالب” centred; the ghazal is printed in two-line form), with source line “(دیوانِ غالب)”. A finger is visible at the left edge.'+NOTE
s['vocabulary']={}
save(s)
# scan 181 = printed 174
s=page(181,'g04','174','Exercise (Mashq) on the ghazals of Ghalib','مشق: غزلیاتِ غالب پر سوالات','تمرین: د غالب د غزلونو پوښتنې','ex')
F=Flow(s)
H(s,'مشق','Exercise (Mashq)','تمرین')
Q(s,'1۔ «کیوں گردشِ مدام سے گھبرا نہ جائے دل / انسان ہوں، پیالہ و ساغر نہیں ہوں میں» غالبؔ کے اس شعر کی تشریح کریں نیز یہ بتائیں کہ اس میں علمِ بیان کی کون سی خوبی پائی جاتی ہے۔','1. “Why should the heart not be dismayed by constant turning? / I am a human being, not a cup or goblet.” Explain this couplet of Ghalib and also state what merit of ilm-e-bayan is found in it.','۱. «ولې دې د همېشنۍ ګردش نه زړه ونه ډارېږي / انسان یم، پیاله او ساغر نه یم زه» د غالب دا شعر تشریح کړئ او همدارنګه ووایئ چې پدې کې د علم بیان کومه ښېګڼه موندل کېږي.')
Q(s,'2۔ مندرجہ ذیل مصرعوں کا مفہوم واضح کریں۔','2. Make clear the meaning of the following lines.','۲. د لاندې مصرعو مفهوم څرګند کړئ.')
for t in [('الف) لوحِ جہاں پہ حرفِ مکرّر نہیں ہوں میں','(a) Louh-e-jahan pe harf-e-mukarrar nahin hoon main','(الف) د نړۍ په لوح تکرار شوی توری نه یم زه'),
('ب) رتبے میں مہر و ماہ سے کمتر نہیں ہوں میں','(b) Rutbe mein mehr-o-maah se kamtar nahin hoon main','(ب) په رتبه کې له لمر او سپوږمۍ نه کم نه یم زه'),
('ج) وہ دن گئے، جو کہتے تھے: نوکر نہیں ہوں میں','(c) Woh din gaye jo kehte the naukar nahin hoon main','(ج) هغه ورځې تېرې شوې چې ویل دې نوکر نه یم زه'),
('د) بہت نکلے مرے ارمان، لیکن پھر بھی کم نکلے','(d) Bahut nikle mere armaan lekin phir bhi kam nikle','(د) ډېرې زما هیلې پوره شوې خو بیا هم لږې'),
('ہ) اُسی کو دیکھ کر جیتے ہیں جس کافر پہ دم نکلے','(e) Usi ko dekh kar jeete hain jis kafir pe dam nikle','(ه) په هغه ژوند کوو چې په کوم کافر ساه ووځي')]:
    add(s,f'i{len(s["paras"])+1}',t[1],t[0],t[2],listGroup='ex-2')
Q(s,'3۔ غالبؔ کی پہلی غزل کی ردیف تحریر کریں۔','3. Write the radif of Ghalib’s first ghazal.','۳. د غالب د لومړي غزل ردیف ولیکئ.')
Q(s,'4۔ غالبؔ کی دوسری غزل کے قافیوں کی نشان دہی کریں۔','4. Point out the rhymes of Ghalib’s second ghazal.','۴. د غالب د دویم غزل قافیې په نښه کړئ.')
Q(s,'5۔ آپ کو غالبؔ کا کون سا شعر زیادہ پسند ہے اور کیوں؟','5. Which couplet of Ghalib do you like most and why?','۵. تاسو ته د غالب کوم شعر ډېر خوښ دی او ولې؟')
Q(s,'6۔ مندرجہ ذیل الفاظ و تراکیب کو جملوں میں استعمال کریں۔ خاک (ڈالنا)، لعل و زمرّد، مہر و ماہ، لوح، عقوبت، گردشِ مدام، بھرم کھلنا، چشمِ تر۔','6. Use the following words and phrases in sentences: khaak (daalna), laal-o-zumurrad, mehr-o-maah, louh, uqoobat, gardish-e-mudaam, bharam khulna, chashm-e-tar.','۶. لاندې الفاظ او ترکیبونه په جملو کې وکاروئ. خاک (اچول)، لعل او زمرد، مهر او ماه، لوح، عقوبت، ګردش مدام، بهرم خلاصېدل، چشم تر.')
Q(s,'7۔ غالبؔ کے کلام کی نمایاں خصوصیات تحریر کریں۔','7. Write the prominent characteristics of Ghalib’s verse.','۷. د غالب د کلام څرګندې ځانګړتیاوې ولیکئ.')
F.done()
s['sourceNote']='Printed page 174 (scan 181): “Mashq” title and questions 1–7 (question 1 quotes the couplet; question 2 has five lines; question 6 lists words in blue). The page is cropped at the left and a finger is visible at the right.'+NOTE
s['vocabulary']={}
save(s)
# scan 182 = printed 175
s=page(182,'g05','175','Dagh Dehlvi (poet profile)','داغ دہلوی (شاعر کا تعارف)','داغ دهلوي (د شاعر پېژندنه)','author')
F=Flow(s)
H(s,'داغؔ دہلوی','Dagh Dehlvi','داغ دهلوي')
P(s,'پیدایش: ۲۵؍ مئی ۱۸۳۱ء — وفات: ۱۹۰۵ء','Born: 25 May 1831 — Died: 1905','زېږېدنه: ۲۵ مۍ ۱۸۳۱ز — وفات: ۱۹۰۵ز')
P(s,'نواب مرزا خان داغؔ دِلّی میں پیدا ہوئے۔ قلعۂ معلّیٰ میں پرورش پائی۔ قلعے میں مشاعروں کی رونق کو داغؔ نے قریب سے دیکھا اور یہیں سے ان کا ذوقِ شاعری اُبھرا اور نکھرا۔ شاعری میں استاد ذوقؔ کے شاگرد تھے۔','Nawab Mirza Khan Dagh was born in Delhi. He was brought up in the Red Fort. Dagh saw at close quarters the splendour of mushairas in the Fort and from here his taste for poetry emerged and was refined. In poetry he was a pupil of Ustad Zauq.','نواب مرزا خان داغ په دهلي کې زېږېدلی دی. په قلعه معلی کې وروزل شو. په قلعه کې د مشاعرو رونق داغ له نژدې ولید او له همدې ځایه د هغه د شاعرۍ ذوق راپورته او ښکلی شو. په شاعرۍ کې د استاد ذوق شاګرد و.')
P(s,'داغؔ کے یہاں جو چیز سب سے نمایاں ہے وہ لطفِ محاورہ اور زبان کا چٹخارہ ہے۔ اُن کا اندازِ بیان بڑا خوب صورت ہے۔ داغؔ کی غزلوں میں عشق کی معاملہ بندی، شوخی اور مسرّت کے جذبات کی فراوانی ہے۔ ان کی شاعری میں میرؔ کا غم یا غالبؔ کا غور و فکر نہیں ہے مگر ان کا اندازِ بیان سہلِ ممتنع کی بہترین مثال پیش کرتا ہے جس کی بدولت ان کی شاعری کو ایک خاص مقام حاصل ہوا ہے۔ ان کی زبان کو سند کا درجہ حاصل ہے۔ ان کا ایک امتیاز یہ بھی ہے کہ علامہ اقبال بھی انھیں اپنا کلام اصلاح کے لیے ارسال کیا کرتے تھے۔ ان کی موت پر اقبال نے ایک پُر تاثیر مرثیہ لکھا جس میں داغؔ کی شاعری کی خوبیاں بیان کی گئی ہیں۔ اُردو غزل کی تاریخ میں داغؔ کو نمایاں مقام حاصل ہے۔ اُردو زبان کے فروغ میں بھی ان کی شاعری کا بڑا حصّہ ہے۔ داغؔ کا کلیات اُردو شاعری کا قابلِ قدر سرمایہ ہے۔ آپ کا حیدر آباد میں انتقال ہوا۔','What is most prominent in Dagh is the delight of idiom and the relish of language. His manner of expression is very beautiful. In Dagh’s ghazals there is abundance of the handling of love affairs, playfulness and feelings of joy. In his poetry there is neither Mir’s grief nor Ghalib’s depth of thought, but his manner of expression presents the best example of “sahl-e-mumtana” (simple yet inimitable), by virtue of which his poetry has gained a special place. His language has the rank of authority. Another distinction of his is that even Allama Iqbal used to send him his verse for correction. On his death Iqbal wrote a moving elegy in which the merits of Dagh’s poetry are described. Dagh holds a prominent place in the history of the Urdu ghazal. His poetry has a large share in the promotion of the Urdu language as well. Dagh’s Kulliyat is a valuable treasure of Urdu poetry. He died in Hyderabad.','د داغ سره چې تر ټولو څرګنده ده هغه د محاورې خوند او د ژبې ټکور دی. د هغه د بیان انداز ډېر ښکلی دی. د داغ په غزلونو کې د عشق معامله بندي، ښوخي او د خوښۍ جذباتو ډېرښت دی. د هغه په شاعرۍ کې د میر غم یا د غالب غور او فکر نشته خو د هغه د بیان انداز د سهل ممتنع ښه نمونه وړاندې کوي چې د هغې په برکت د هغه شاعرۍ ته یو ځانګړی مقام ترلاسه شوی دی. د هغه ژبې ته د سند درجه ترلاسه ده. د هغه یو امتیاز دا هم دی چې علامه اقبال هم هغه ته خپل کلام د اصلاح لپاره لېږلو. د هغه په مړینه اقبال یو اغېزمنه مرثیه ولیکله چې په هغې کې د داغ د شاعرۍ ښېګڼې بیان شوي دي. د اردو غزل په تاریخ کې داغ ته څرګند مقام ترلاسه دی. د اردو ژبې په وده کې هم د هغه د شاعرۍ لویه برخه ده. د داغ کلیات د اردو شاعرۍ د قدر وړ پانګه ده. هغه په حیدرآباد کې وفات شو.')
P(s,'مجموعہ ہائے کلام: ماہتابِ داغؔ، گلزارِ داغؔ، آفتابِ داغؔ اور یادگارِ داغؔ، داغؔ دہلوی کے نمایندہ شعری مجموعے ہیں۔','Collections of verse: Mahtab-e-Dagh, Gulzar-e-Dagh, Aaftab-e-Dagh and Yaadgar-e-Dagh are the representative poetry collections of Dagh Dehlvi.','شعري ټولګې: ماهتاب داغ، ګلزار داغ، آفتاب داغ او یادګار داغ د داغ دهلوي استازې شعري ټولګې دي.')
F.done()
s['sourceNote']='Printed page 175 (scan 182): ornamental title “داغ دہلوی”, portrait (not reproduced), birth/death boxes (25 May 1831 and 1905), biography and the names of the collections.'+NOTE
s['vocabulary']={}
save(s)
