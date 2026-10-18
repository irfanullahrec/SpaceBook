from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,u='n13',**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId=f'urdu11-{u}-q',tab='exercise',**k)
def V(s,u1,u2,e1,e2,p1,p2): add(s,f'v{len(s["paras"])+1}',e1+'\n'+e2,u1+'\n'+u2,p1+'\n'+p2,listType='poem',kind='verse')
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded.'
# scan 165 = printed 158
s=page(165,'n13','158','Ikhlas, end; Exercise (Mashq) on Ikhlas','اخلاص (اختتام)؛ مشق: «اخلاص» پر سوالات','اخلاص (پای)؛ تمرین: «اخلاص» پوښتنې','poem2')
F=Flow(s)
V(s,'حاجت نہیں اخلاص کی کچھ بعد نِ …','قائم کرو ہستی میں نظامِ اخلاص','There is no need for anything of ikhlas after … (the end of the line is cropped in the scan);','establish in existence the order of ikhlas.','د اخلاص څه حاجت نشته وروسته ن …','په هستۍ کې د اخلاص نظام قایم کړئ')
V(s,'شیریں گفتار پہ حیرت کیسی','ہے گفتۂ رحمنؒ کلامِ اخلاص','Why astonishment at the sweet speech?','the saying of Rahman is the word of ikhlas.','په خوږ ګفتار څه حیرانتیا','د رحمن ویلي کلام د اخلاص کلام دی')
P(s,'(ستارِ فقیر)','(Sitar-e-Faqeer, printed faintly; read approximately)','(ستار فقیر؛ په ضعیف ډول چاپ شوی، تقریباً لوستل شوی)')
H(s,'مشق','Exercise (Mashq)','تمرین')
Q(s,'1۔ اس نظم میں «اخلاص» کی جو تعریفیں بیان کی گئی ہیں، انھیں مختصراً لکھیں۔','1. Write briefly the definitions of “ikhlas” stated in this poem.','۱. پدې نظم کې د «اخلاص» چې کومې تعریفونه بیان شوي دي هغه په لنډه توګه ولیکئ.')
Q(s,'2۔ «ہما» پرندے کی کیا خصوصیت بیان کی جاتی ہے؟','2. What speciality of the bird “Huma” is stated?','۲. د «هما» مرغۍ کومه ځانګړتیا بیانېږي؟')
Q(s,'3۔ اخلاص کی وجہ سے کون سا سفر آسان ہو جاتا ہے؟','3. Which journey becomes easy because of ikhlas?','۳. د اخلاص له امله کوم سفر اسانه کېږي؟')
Q(s,'4۔ اس نظم کا مرکزی خیال بیان کریں۔','4. State the central idea of this poem.','۴. د دې نظم مرکزي خیال بیان کړئ.')
Q(s,'5۔ «فانی ہے ہر اک چیز، ہر اک رسم و رواج / باقی ہے، مگر ایک دوامِ اخلاص» کلام میں دو ایسے الفاظ استعمال کرنا جو ایک دوسرے کی ضد ہوں «صنعتِ تضاد» کہلاتا ہے۔ جیسے مندرجہ بالا شعر میں «فانی» اور «باقی» ایک دوسرے کی ضد ہیں۔ صنعتِ تضاد کی تعریف کریں اور تین مثالیں لکھیں۔','5. “Everything is perishable, every custom and tradition; / only one thing remains: the perpetuity of ikhlas.” To use in verse two words that are opposites of one another is called “sanat-e-tazaad”. As in the above couplet “faani” and “baaqi” are opposites of each other. Define sanat-e-tazaad and write three examples.','۵. «هر شی فاني دی، هر دود او رواج / پاتې دی خو یو دوام اخلاص». په کلام کې دوه داسې الفاظ کارول چې یو د بل ضد وي «صنعت تضاد» بلل کېږي. لکه په پورتني شعر کې «فاني» او «باقي» یو د بل ضد دي. د صنعت تضاد تعریف وکړئ او درې بېلګې ولیکئ.')
P(s,'طلبہ کو عبدالرحمن باباؒ کے چند ضرب المثل اشعار سنائیں۔','Recite to the students some proverb-like couplets of Abdur Rahman Baba.','زده‌کوونکو ته د عبدالرحمن بابا څو ضرب المثل شعرونه واورئ.',boxed=True)
F.done()
s['sourceNote']='Printed page 158 (scan 165): the end of the poem “Ikhlas” (the left parts of the first line are cropped; the faint source line may be read “(ستارِ فقیر)”), the “Mashq” title and questions 1–5 (question 5 quotes the couplet in blue and defines tazaad), and a boxed instruction whose blue label is too faint to read (the instruction reads “طلبہ کو عبدالرحمن باباؒ کے چند ضرب المثل اشعار سنائیں”).'+NOTE
s['vocabulary']={}
save(s)
# scan 166 = printed 159
s=page(166,'g01','159','Section title: Hissa-e-Ghazal (Ghazal part)','سیکشن عنوان: حصۂ غزل','د برخې سرلیک: د غزل برخه','divider')
F=Flow(s)
H(s,'حصۂ غزل','Hissa-e-Ghazal (Ghazal part)','د غزل برخه')
F.done()
s['sourceNote']='Printed page 159 (scan 166): section-divider page with the calligraphic title “حصۂ غزل” in a decorative emblem (not reproduced); no other text.'+NOTE
s['vocabulary']={}
save(s)
# scan 167 = printed 160
s=page(167,'g01','160','Mir Taqi Mir (poet profile)','میر تقی میر (شاعر کا تعارف)','میر تقي میر (د شاعر پېژندنه)','author')
F=Flow(s)
H(s,'میر تقی میر','Mir Taqi Mir','میر تقي میر')
P(s,'پیدایش: ۱۷۲۱ء — وفات: ۱۸۱۰ء','Born: 1721 — Died: 1810','زېږېدنه: ۱۷۲۱ز — وفات: ۱۸۱۰ز')
P(s,'میر تقی میرؔ کی شاعری زندگی کے انقلابات کی ترجمان رہی ہے۔ اگرچہ بعض ناقدین نے میرؔ کو قنوطیّت کا حامل شاعر بھی کہا ہے۔ میرؔ زندگی کی مایوسیوں کی طرف اشارہ ضرور کرتا ہے لیکن ان کی شاعری قاری کو زندگی سے بیزاری پر مجبور نہیں کرتی بل کہ کسی حد تک ایک نشاطیہ احساس بھی جگاتی ہے۔ یہی سبب ہے کہ میرؔ کی شاعرانہ عظمت کا اعتراف نہ صرف ان کے معاصرین نے کیا ہے، بل کہ اب تک کے تمام مستند ناقدین اور غزل کے معتبر شعرا نے میرؔ کے کلام کی ہمہ گیریت، نشتریّت اور افادیّت کو کھلے دل سے تسلیم کیا ہے۔ غالبؔ جیسے یگانۂ روزگار شاعر نے برملا یہ کہا:','Mir Taqi Mir’s poetry has been the voice of the revolutions of life. Although some critics have also called Mir a poet of pessimism. Mir does indicate the disappointments of life but his poetry does not compel the reader to be disgusted with life; rather to some extent it also awakens a cheerful feeling. This is why the poetic greatness of Mir has been acknowledged not only by his contemporaries but all authoritative critics and reliable poets of the ghazal up to now have openly acknowledged the all-encompassing nature, the piercing quality and the usefulness of Mir’s verse. A unique poet of the age like Ghalib said openly:','د میر تقي میر شاعري د ژوند د انقلابونو ترجمانه پاتې شوې ده. که څه هم ځینو ناقدینو میر ته قنوطي شاعر هم ویلی دی. میر د ژوند د نهیلیو لور ته اشاره ضرور کوي خو د هغه شاعري لوستونکی د ژوند له بیزارۍ نه نه مجبوروي بلکې یو څه حده یو نشاطیه احساس هم راویښوي. همدا لامل دی چې د میر شاعرانه عظمت نه یوازې د هغه معاصرینو اعتراف کړی دی بلکې تر اوسه ټول معتبر ناقدینو او د غزل معتبرو شاعرانو د میر د کلام ټول ګیرتیا، نشتریت او ګټه په پرانیستي زړه منلې ده. غالب غوندې د زمانې یګانه شاعر په ښکاره وویل:')
V(s,'ریختے کے تمھیں استاد نہیں ہو غالبؔ','کہتے ہیں، اگلے زمانے میں کوئی میرؔ بھی تھا','You are not the only master of Rekhta, Ghalib;','they say that in former times there was a Mir too.','ای غالبه ته د ریختې یوازینی استاد نه یې','وايي چې په پخوانۍ زمانه کې یو میر هم و')
P(s,'میرؔ کو خدائے سخن کے نام سے بھی یاد کیا جاتا ہے۔ میرؔ کا اُسلوبِ بیان سادہ اور سلیس ہونے کے باوجود نُدرت اور انفرادیت کا حامل ہے۔ ان کے کلام میں روز مرّہ اور محاورے کا التزام بخوبی موجود ہے۔ اُن کے عہد کو اُردو شاعری کے زریں عہد سے تعبیر کیا جاتا ہے۔ اُنھوں نے اُردو ادب کو چھے ضخیم مجموعہ ہائے کلام دیے، جن کی قدر و قیمت وقت گزرنے کے ساتھ ساتھ بڑھتی چلی جا رہی ہے۔ گویا میر تقی میرؔ کا یہ دعویٰ بالکل دُرست ثابت ہوا ہے:','Mir is also remembered by the name “Khuda-e-Sukhan” (God of Poetry). Although Mir’s style of expression is simple and fluent, it has novelty and individuality. In his verse the observance of everyday speech and idiom is well present. His period is described as the golden age of Urdu poetry. He gave Urdu literature six voluminous collections of verse, whose worth and value keep rising with the passing of time. It is as though Mir Taqi Mir’s claim has proved quite correct:','میر ته د خدای سخن په نوم هم یادېږي. د میر د بیان سټایل د ساده او روان کېدو سره سره نوښت او انفرادیت لري. د هغه په کلام کې روزمره او محاورې التزام ښه موجود دی. د هغه دور ته د اردو شاعرۍ زرین دور ویل کېږي. هغه اردو ادب ته شپږ ضخیم شعري ټولګې ورکړې دي چې قدر او بیه یې د وخت تېرېدو سره سره زیاتېږي. ګواکې د میر تقي میر دا دعوی بالکل سمه ثابته شوې ده:')
V(s,'سارے عالم پر ہوں میں چھایا ہوا','مستند ہے میرا فرمایا ہوا','I am spread over the whole world;','what I have said is authentic.','زه په ټوله نړۍ خپور یم','زما ویل شوی معتبر دی')
P(s,'تصانیف: چھے دواوین (اُردو)، دیوانِ میرؔ (فارسی)، ذکرِ میرؔ (خود نوشت) اور نکات الشعرا (تذکرہ)۔','Works: six divans (Urdu), the Divan of Mir (Persian), Zikr-e-Mir (autobiography) and Nikaat-ush-Shuara (biographical dictionary).','تصنیفات: شپږ دیوانونه (اردو)، دیوان میر (فارسي)، ذکر میر (خود نوشت) او نکات الشعرا (تذکره).')
F.done()
s['sourceNote']='Printed page 160 (scan 167): ornamental title “میر تقی میر”, portrait (not reproduced), birth/death boxes (1721 and 1810), biography with two quoted couplets in blue (Ghalib’s and Mir’s) and the list of works.'+NOTE
s['vocabulary']={}
save(s)
