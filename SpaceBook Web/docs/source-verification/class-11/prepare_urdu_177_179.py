from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,u='g03',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'urdu11-{u}-q',tab='exercise',**k)
def V(s,u1,u2,e1,e2,p1,p2): add(s,f'v{len(s["paras"])+1}',e1+'\n'+e2,u1+'\n'+u2,p1+'\n'+p2,listType='poem',kind='verse')
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded.'
# scan 177 = printed 170
s=page(177,'g03','170','Exercise (Mashq) on the ghazal of Mushafi; box on Sher','مشق: غزلِ مصحفی پر سوالات؛ شعر','تمرین: د مصحفي د غزل پوښتنې؛ شعر','ex')
F=Flow(s)
H(s,'مشق','Exercise (Mashq)','تمرین')
Q(s,'1۔ مصحفیؔ کی شاملِ نصاب غزل میں جو ترا کیب استعمال ہوئی ہیں اُنھیں تحریر کریں۔','1. Write the compound phrases (tarakeeb) used in Mushafi’s ghazal included in the syllabus.','۱. د مصحفي په نصابي غزل کې چې کوم ترکیبونه کارول شوي دي هغه ولیکئ.')
Q(s,'2۔ مصحفیؔ کی غزل میں ردیف اور قافیوں کی نشان دہی کریں۔','2. Point out the radif and the rhymes in Mushafi’s ghazal.','۲. د مصحفي په غزل کې ردیف او قافیې په نښه کړئ.')
Q(s,'3۔ اس غزل میں سے چند مرکباتِ اضافی لکھیں۔','3. Write some izafi compounds from this ghazal.','۳. له دې غزل نه څو مرکبات اضافي ولیکئ.')
Q(s,'4۔ ان مصرعوں کا مفہوم واضح کریں۔','4. Make clear the meaning of these lines.','۴. د دغو مصرعو مفهوم څرګند کړئ.')
for t in [('• گل کو شکستِ رنگ کا پیغام آ گیا','• The message of the defeat of colour came to the rose.','• ګل ته د رنګ د ماتې پیغام راغی'),
('• خورشید کف کے بیچ لیے جام آ گیا','• The sun came holding a goblet in his palm.','• لمر په لاس کې جام نیولی راغی'),
('• جو گرتے ہی ہوا سے تہِ دام آ گیا','• who, falling from the air, at once came under the net.','• چې له هوا د لوېدو سره سم د جال لاندې راغی')]:
    add(s,f'i{len(s["paras"])+1}',t[1],t[0],t[2],listGroup='ex-4')
Q(s,'5۔ درج ذیل الفاظ و تراکیب کو جملوں میں استعمال کریں۔ گل اندام، پُر خمار، کف، تہِ دام، اسیر، آفتابِ عمر۔','5. Use the following words and phrases in sentences: gul-andaam, pur-khumaar, kaf, teh-e-daam, aseer, aaftaab-e-umr.','۵. لاندې الفاظ او ترکیبونه په جملو کې وکاروئ. ګل اندام، پر خمار، کف، ته دام، اسیر، آفتاب عمر.')
Q(s,'6۔ مصحفیؔ کی غزل کے دوسرے شعر میں جس صنعت کا استعمال ہوا ہے، اس کی تعریف کریں اور دو مثالیں دیں۔','6. Define the figure used in the second couplet of Mushafi’s ghazal and give two examples.','۶. د مصحفي د غزل په دویم شعر کې چې کوم صنعت کارول شوی دی هغه تعریف کړئ او دوه بېلګې ورکړئ.')
H(s,'شعر:','Sher (couplet):','شعر:')
P(s,'وہ کلامِ موزوں جو با مقصد ہو، ایک خیال کو ظاہر کرے اور جس کے دونوں مصرعے ایک ہی وزن میں ہوں «شعر» کہلاتا ہے۔','Metrical speech that has a purpose, expresses one idea and whose two lines are in one and the same metre is called “sher”.','هغه موزون کلام چې با مقصده وي، یو خیال څرګند کړي او چې دواړه مصرعې یې په یو وزن وي «شعر» بلل کېږي.',boxed=True)
F.done()
s['sourceNote']='Printed page 170 (scan 177): “Mashq” title, questions 1–6 (question 4 quotes three lines with blue bullets; question 5 lists words in blue) and the blue box “شعر”. The scan is slightly crinkled at the left.'+NOTE
s['vocabulary']={}
save(s)
# scan 178 = printed 171
s=page(178,'g04','171','Mirza Asadullah Khan Ghalib (poet profile)','مرزا اسد اللہ خان غالب (شاعر کا تعارف)','مرزا اسد الله خان غالب (د شاعر پېژندنه)','author')
F=Flow(s)
H(s,'مرزا اسد اللہ خان غالب','Mirza Asadullah Khan Ghalib','مرزا اسد الله خان غالب')
P(s,'پیدایش: ۲۷؍ دسمبر ۱۷۹۷ء — وفات: ۱۵؍ فروری ۱۸۶۹ء','Born: 27 December 1797 — Died: 15 February 1869','زېږېدنه: ۲۷ دسمبر ۱۷۹۷ز — وفات: ۱۵ فبروري ۱۸۶۹ز')
P(s,'مرزا اسد اللہ خان غالبؔ آگرہ میں پیدا ہوئے۔ ابتدا میں اسدؔ اور بعد میں غالبؔ تخلص اختیار کیا۔ شاہی دربار سے نجم الدولہ اور دبیر الملک کے خطاب پائے۔ غالبؔ کے آبا و اجداد ترک سلجوقی تھے جو مغلیہ عہد میں ماوراء النہر سے ہندوستان آئے اور اچھے سرکاری عہدوں پر فائز رہے۔ ان کے چچا نصر اللہ بیگ شاہی فوج میں رسال دار تھے۔ نوابانِ لوہارو سے مرزا غالبؔ کا سسرالی رشتہ تھا۔ اپنی خاندانی وجاہت پر اُنھیں ناز تھا:','Mirza Asadullah Khan Ghalib was born in Agra. At first he adopted the pen-name Asad and later Ghalib. From the royal court he received the titles Najm-ud-Daula and Dabeer-ul-Mulk. Ghalib’s ancestors were Seljuk Turks who came to India from Transoxiana during the Mughal period and held good government posts. His uncle Nasrullah Beg was a risaldar in the royal army. Mirza Ghalib was related by marriage to the nawabs of Loharu. He took pride in his family’s distinction:','مرزا اسد الله خان غالب په اګره کې زېږېدلی دی. په پیل کې یې اسد او وروسته غالب تخلص غوره کړ. له شاهي دربار نه یې نجم الدوله او دبیر الملک لقبونه ترلاسه کړل. د غالب نیکه ګان ترک سلجوقي وو چې د مغلیه دورې په وخت له ماوراء النهره هندوستان ته راغلل او په ښو دولتي دندو پاتې شول. د هغه تره نصر الله بیګ په شاهي پوځ کې رسالدار و. د لوهارو له نوابانو سره د مرزا غالب خسري خپلوي وه. په خپلې کورنۍ وجاهت یې ویاړ و:')
V(s,'سو پشت سے ہے پیشۂ آبا سپہ گری','کچھ شاعری ذریعۂ عزّت نہیں مجھے','For a hundred generations the profession of my forefathers has been soldiering;','poetry is no source of honour for me.','سل پېړۍ راهیسې د نیکه ګانو پېشه سپاهي ګري ده','شاعري ماته د عزت وسیله نه ده')
P(s,'اپنی شعر گوئی کے پہلے دور میں غالبؔ نے مشکل پسندی اِختیار کی لیکن پھر سادہ طرز اپنایا۔ خیال کی لطافت، بلندی، روز مرّہ اور محاورات کا لُطف، طرزِ ادا کی شوخی اور موضوعات کی رنگارنگی نے ان کے کلام کو منفرد اور دل کش بنا دیا۔ زندگی کے غموں اور دکھوں کے باوجود وہ خوش طبعی کا دامن ہاتھ سے نہیں چھوڑتے۔ ان کی شاعری کی ایک اہم خوبی مُحاکات ہے۔ وہ لفظوں سے تصویر کھینچ کر رکھ دیتے ہیں۔ اُنھوں نے اپنی شاعری کا انتخاب «دیوانِ غالب» کی شکل میں کیا اور ان کی شاعرانہ عظمت میں اس انتخاب کو بڑا دخل ہے۔ اُردو کا یہ عظیم شاعر دِلّی میں انتقال کر گیا۔','In the first period of his poetry Ghalib adopted difficulty, but then adopted a simple style. The delicacy and loftiness of thought, the delight of everyday speech and idioms, the playfulness of manner of expression and the variety of subjects made his verse unique and attractive. Despite the griefs and sorrows of life he does not let go the hem of good humour. One important virtue of his poetry is mimesis (muhakaat): he draws a picture with words. He made a selection of his poetry in the form of “Diwan-e-Ghalib” and this selection has a large part in his poetic greatness. This great poet of Urdu died in Delhi.','د خپل شعر ګویۍ په لومړۍ دوره کې غالب مشکل پسندي غوره کړه خو بیا یې ساده طرز غوره کړ. د خیال نرمي، لوړتیا، روزمره او محاورو خوند، د بیان طرز ښوخي او د موضوعاتو رنګارنګي د هغه کلام ځانګړی او زړه راکښونکی کړ. د ژوند د غمونو او دردونو سره سره هغه د خوش طبعۍ لمن له لاسه نه پرېږدي. د هغه د شاعرۍ یوه مهمه ښه والی محاکات دی. هغه په الفاظو انځور راکاږي. هغه د خپلې شاعرۍ انتخاب د «دیوان غالب» په بڼه وکړ او د هغه د شاعرانه عظمت په کې دې انتخاب لوی لاسوهنه ده. د اردو دا لوی شاعر په دهلي کې وفات شو.')
P(s,'تصانیف: دیوانِ غالب، اُردوئے معلیٰ، عُودِ ہندی، لطائفِ غیبی، کلیاتِ غالب (فارسی)، قاطعِ برہان، دستنبو وغیرہ۔','Works: Diwan-e-Ghalib, Urdu-e-Mualla, Ud-e-Hindi, Lataif-e-Ghaibi, Kulliyat-e-Ghalib (Persian), Qate-e-Burhan, Dastanbu, etc.','تصنیفات: دیوان غالب، اردوی معلی، عود هندي، لطایف غیبي، کلیات غالب (فارسي)، قاطع برهان، دستنبو او نور.')
F.done()
s['sourceNote']='Printed page 171 (scan 178): ornamental title “مرزا اسد اللہ خان غالب”, portrait (not reproduced), birth/death boxes (27 December 1797 and 15 February 1869), biography with a quoted couplet in blue, and the list of works.'+NOTE
s['vocabulary']={}
save(s)
# scan 179 = printed 172
s=page(179,'g04','172','Ghazal (Ghalib): “Daaim pada hua tere dar par nahin hoon main”','غزل (غالب): «دائم پڑا ہوا ترے در پر نہیں ہوں میں»','غزل (غالب): «تل ستا پر دروازه پروت نه یم زه»','poem1')
F=Flow(s)
H(s,'غزل','Ghazal','غزل')
for r in [
('دائم پڑا ہوا ترے در پر نہیں ہوں میں','خاک ایسی زندگی پہ کہ پتھر نہیں ہوں میں','I am not constantly lying at your door;','dust on such a life — I am not a stone.','تل ستا په دروازه پروت نه یم زه','خاورې دې شي پر داسې ژوند چې ډبره نه یم زه'),
('کیوں گردشِ مدام سے گھبرا نہ جائے دل','انسان ہوں، پیالہ و ساغر نہیں ہوں میں','Why should the heart not be dismayed by the constant turning?','I am a human being, not a cup or goblet.','ولې دې د همېشنۍ ګردش نه زړه ونه ډارېږي','انسان یم، پیاله او ساغر نه یم زه'),
('یارب! زمانہ مجھ کو مٹاتا ہے کس لیے','لوحِ جہاں پہ حرفِ مکرر نہیں ہوں میں','O Lord! Why does time wipe me out?','I am not a repeated letter on the tablet of the world.','ای ربه! زمانه ماته ولې له منځه وړي','د نړۍ په لوح باندې تکرار شوی توری نه یم زه'),
('حد چاہیے سزا میں، عقوبت کے واسطے','آخر گنہگار ہوں، کافر نہیں ہوں میں','There should be a limit in punishment, in penalty;','after all I am a sinner, I am not an unbeliever.','په سزا کې حد پکار دی، د عقوبت لپاره','په پای کې ګناهګار یم، کافر نه یم زه'),
('کس واسطے عزیز نہیں جانتے مجھے','لعل و زمرّد و زر و گوہر نہیں ہوں میں','Why do they not hold me dear?','I am not ruby, emerald, gold and pearl.','ولې ماته ګران نه ګڼي','لعل او زمرد او زر او ګوهر نه یم زه'),
('رکھتے ہو تم قدم مری آنکھوں سے کیوں دریغ','رتبے میں مہر و ماہ سے کمتر نہیں ہوں میں','Why do you withhold your footstep from my eyes?','in rank I am not less than the sun and moon.','ولې ستاسو قدم زما له سترګو دریغ ساتئ','په رتبه کې له لمر او سپوږمۍ نه کم نه یم زه'),
('کرتے ہو مجھ کو منعِ قدم بوس کس لیے','کیا آسمان کے بھی برابر نہیں ہوں میں','Why do you forbid me to kiss your feet?','am I not even equal to the sky?','ولې ما ته د قدم بوسې منع کوئ','آیا زه د اسمان هم برابر نه یم'),
('غالبؔ وظیفہ خوار ہو، دو شاہ کو دُعا','وہ دن گئے، جو کہتے تھے: «نوکر نہیں ہوں میں»','Ghalib, be a pensioner; give a prayer for the king;','those days have gone when you used to say: “I am not a servant.”','غالبه وظیفه خور اوسه، پاچا ته دعا ورکړه','هغه ورځې تېرې شوې چې ویل دې: «نوکر نه یم زه»')]:
    V(s,*r)
F.done()
s['sourceNote']='Printed page 172 (scan 179): title “غزل”, running head “مرزا اسد اللہ خان غالب”, and the ghazal “دائم پڑا ہوا ترے در پر نہیں ہوں میں” (seven couplets and the closing couplet with the pen-name “غالب” centred). The scan is slightly torn at the right edge.'+NOTE
s['vocabulary']={}
save(s)
