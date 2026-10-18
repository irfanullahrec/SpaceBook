from urduhelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def I(s,items,g):
    for ur,en,ps in items: add(s,f'i{len(s["paras"])+1}',en,ur,ps,listGroup=g)
NOTE=' English and Pashto are our translations (need native review); watermark and ornamental borders excluded.'
# scan 1
s=page(1,'front-matter','','Front cover','سرورق','پوښ','cover')
F=Flow(s)
P(s,'اُردو (لازمی) — گیارھویں جماعت کے لیے — خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔ (کتاب پر «11» کا چھے کونوں والا نشان)','Urdu (Compulsory) — for the eleventh class — Khyber Pakhtunkhwa Textbook Board, Peshawar. (A hexagonal “11” badge on the cover.)','اردو (لازمي) — د یولسم ټولګي لپاره — د خیبر پښتونخوا ټیکسټ بک بورډ، پېښور. (پر پوښ د «۱۱» شپږ کنجه نښه)')
F.done()
s['sourceNote']='Front cover: title, class badge, board name and crest; the cover illustration (two portraits of poets in front of a mountain and pine tree) is not reproduced and not captioned in print.'+NOTE
s['vocabulary']={}
save(s)
# scan 2
s=page(2,'front-matter','','Quranic verse (Surah al-Ahzab 40)','قرآنی آیت کا ترجمہ (سورۃ الاحزاب: 40)','د قرآني آیت ترجمه (سورة الاحزاب: ۴۰)','verse')
F=Flow(s)
P(s,'اللہ تعالیٰ کا ارشاد ہے:','Allah the Exalted says:','د الله تعالیٰ ارشاد دی:')
P(s,'ترجمہ: «محمد (ﷺ) تمھارے مردوں میں سے کسی کے باپ نہیں ہیں لیکن وہ اللہ کے رسول ہیں اور تمام نبیوں میں سب سے آخری نبی ہیں اور اللہ ہر بات کو خوب جاننے والا ہے۔» (سورۃ الاحزاب، آیت: 40)','Translation: “Muhammad (peace be upon him) is not the father of any of your men, but he is the Messenger of Allah and the last of all the prophets; and Allah is Knowing of all things.” (Surah al-Ahzab, verse 40)','ترجمه: «محمد (ﷺ) ستاسو د نارینه وو له چا نه پلار نه دی خو د الله رسول دی او د ټولو انبیاوو وروستی نبي دی او الله هره خبره ښه پېژني.» (سورة الاحزاب، ۴۰ آیت)')
F.done()
s['sourceNote']='Page with a boxed Urdu translation of Surah al-Ahzab 40 (the Arabic text is not printed); the benediction after the Prophet’s name is printed in small calligraphy.'+NOTE
s['vocabulary']={}
save(s)
# scan 3
s=page(3,'front-matter','','Title page','عنوانی صفحہ','سرلیک پاڼه','title')
F=Flow(s)
P(s,'بِسْمِ اللّٰہِ الرَّحْمٰنِ الرَّحِیْمِ — شروع اللہ کے نام سے جو بڑا مہربان، نہایت رحم والا ہے۔','In the name of Allah, the Entirely Merciful, the Especially Merciful.','د الله په نوم چې ډېر مهربان او ډېر رحم کوونکی دی.')
H(s,'اُردو (لازمی) گیارھویں جماعت کے لیے','Urdu (Compulsory) for Class Eleven','اردو (لازمي) د یولسم ټولګي لپاره')
P(s,'خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور','Khyber Pakhtunkhwa Textbook Board, Peshawar','د خیبر پښتونخوا ټیکسټ بک بورډ، پېښور')
F.done()
s['sourceNote']='Title page with the Bismillah in a decorated cartouche, the title, and the board crest (not reproduced).'+NOTE
s['vocabulary']={}
save(s)
# scan 4
s=page(4,'front-matter','','Copyright and credits','جملہ حقوق اور تفصیلات','د چاپ حقونه او تفصیلات','credits')
F=Flow(s)
P(s,'جملہ حقوق بحق خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور محفوظ ہیں۔','All rights are reserved by the Khyber Pakhtunkhwa Textbook Board, Peshawar.','ټول حقونه د خیبر پښتونخوا ټیکسټ بک بورډ، پېښور سره خوندي دي.')
I(s,[('تیار کردہ: خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور','Prepared by: Khyber Pakhtunkhwa Textbook Board, Peshawar','چمتو کوونکی: د خیبر پښتونخوا ټیکسټ بک بورډ، پېښور'),
('منظور کردہ: نصاب و تعلیمِ اساتذہ خیبر پختونخوا، ایبٹ آباد — مراسلہ نمبر: No. 382-84/u-04/CTR/DCTE/NOC مورخہ 2022-01-31','Approved by: Curriculum and Teacher Education, Khyber Pakhtunkhwa, Abbottabad — letter no. No. 382-84/u-04/CTR/DCTE/NOC dated 31-01-2022 (number read from the scan)','تصویب کوونکی: د نصاب او د ښوونکو زده‌کړې ریاست خیبر پښتونخوا، ابټ اباد — مراسلې شمېره: No. 382-84/u-04/CTR/DCTE/NOC نېټه ۲۰۲۲-۰۱-۳۱'),
('مؤلفین: ڈاکٹر جاوید بادشاہ، پروفیسر خالد اصغر ڈار، ڈاکٹر طارق ہاشمی، پروفیسر محمد جمال، ڈاکٹر اظہار اللہ اظہار','Authors: Dr Javaid Badshah, Prof. Khalid Asghar Dar, Dr Tariq Hashmi, Prof. Muhammad Jamal, Dr Izhar Ullah Izhar','مؤلفین: ډاکټر جاوید بادشاه، پروفیسر خالد اصغر ډار، ډاکټر طارق هاشمي، پروفیسر محمد جمال، ډاکټر اظهار الله اظهار')],'urdu-credits')
H(s,'نظرِ ثانی و ترامیم','Review and amendments','بیاکتنه او ترمیمات')
I(s,[('ڈاکٹر محمد امتیاز، ایسوسی ایٹ پروفیسر (اُردو) گورنمنٹ پوسٹ گریجویٹ کالج، صوابی','Dr Muhammad Imtiaz, Associate Professor (Urdu), Government Postgraduate College, Swabi','ډاکټر محمد امتیاز، ایسوسي ایټ پروفیسر (اردو)، د حکومتي پوسټ ګریجویټ کالج، صوابۍ'),
('ڈاکٹر اشفاق احمد آشفتہ، اسسٹنٹ پروفیسر (اُردو) گورنمنٹ ڈگری کالج بوئی، ایبٹ آباد','Dr Ashfaq Ahmad Aashufta, Assistant Professor (Urdu), Government Degree College Boi, Abbottabad','ډاکټر اشفاق احمد آشفته، اسسټنټ پروفیسر (اردو)، د حکومتي ډګري کالج بوئي، ابټ اباد'),
('عبدالستار، ماہرِ مضمون (اُردو)، گورنمنٹ ہائیر سیکنڈری اسکول گلی بدرال، مانسہرہ','Abdus Sattar, subject specialist (Urdu), Government Higher Secondary School Gali Badral, Mansehra','عبدالستار، د مضمون ماهر (اردو)، د حکومتي لوړو ثانوي ښوونځي ګلي بدرال، مانسهره'),
('تاج ولی خان، ماہرِ مضمون (لسانیات)، نظامتِ نصاب و تعلیمِ اساتذہ خیبر پختونخوا، ایبٹ آباد','Taj Wali Khan, subject specialist (linguistics), Directorate of Curriculum and Teacher Education, Khyber Pakhtunkhwa, Abbottabad','تاج ولي خان، د مضمون ماهر (ژبپوهنه)، د نصاب او د ښوونکو د زده‌کړې ریاست خیبر پښتونخوا، ابټ اباد'),
('سلیم اللہ علوی، ماہرِ مضمون (اُردو)، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور','Saleemullah Alvi, subject specialist (Urdu), Khyber Pakhtunkhwa Textbook Board, Peshawar','سلیم الله علوي، د مضمون ماهر (اردو)، د خیبر پښتونخوا ټیکسټ بک بورډ، پېښور')],'urdu-review')
P(s,'مدیر: ڈاکٹر عظمت علی درانی، ماہرِ مضمون (اُردو)، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور','Editor: Dr Azmat Ali Durrani, subject specialist (Urdu), Khyber Pakhtunkhwa Textbook Board, Peshawar','مدیر: ډاکټر عظمت علي دراني، د مضمون ماهر (اردو)، د خیبر پښتونخوا ټیکسټ بک بورډ، پېښور')
P(s,'زیرِ نگرانی: سید فرالثقلین (چیئرمین)، عبدالولی خان ممبر (ای اینڈ پی)، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور','Under supervision of: Syed Farasaqalain (Chairman), Abdul Wali Khan, Member (E&P), Khyber Pakhtunkhwa Textbook Board, Peshawar (names read from the scan)','تر څارنې لاندې: سید فرالثقلین (رئیس)، عبدالولي خان غړی (E&P)، د خیبر پښتونخوا ټیکسټ بک بورډ، پېښور')
P(s,'تعلیمی سال: 2024-25ء۔ ویب سائٹ: https://tbb.kp.gov.pk۔ ای میل: membertbb@yahoo.com۔ ٹیلی فون: 091-9217159-60۔','Academic year: 2024-25. Website: https://tbb.kp.gov.pk. E-mail: membertbb@yahoo.com. Telephone: 091-9217159-60.','تعلیمي کال: ۲۰۲۴-۲۵. ویب پاڼه: https://tbb.kp.gov.pk. برېښنالیک: membertbb@yahoo.com. تلیفون: 091-9217159-60.')
F.done()
s['sourceNote']='Copyright and credits page with a decorative border; names and the letter number are read from the scan and may contain misreadings.'+NOTE
s['vocabulary']={}
save(s)
# scan 5
s=page(5,'front-matter','','Learning outcomes','حاصلاتِ تعلم','د زده‌کړې السته راوړنې','outcomes')
F=Flow(s)
H(s,'حاصلاتِ تعلم','Student learning outcomes','د زده‌کړې السته راوړنې')
P(s,'تدریسِ اُردو کے ذریعے طلبہ اس قابل ہو سکیں گے کہ:','Through the teaching of Urdu, students will be able to:','د اردو په تدریس سره به زده‌کوونکي دې ته وړ شي چې:')
I(s,[('اُردو زبان شناسی پر عبور حاصل کر سکیں۔','gain mastery of Urdu linguistics.','د اردو ژبپوهنې باندې بشپړ لاسرسی ترلاسه کړي.'),
('اصنافِ سخن کی تعریف کر سکیں اور انھیں پہچان کر استحسان کر سکیں۔','define the genres of literature and recognise and appreciate them.','د ادبي ډولونو تعریف وکړي او هغه وپېژني او ستاينه یې وکړي.'),
('علمِ بیان، علمِ بدیع اور صنعتوں کی تعریف کر سکیں۔','define the science of expression (ilm-e-bayan), the science of embellishment (ilm-e-badee) and figures of speech.','د علم بیان، علم بدیع او صنعتونو تعریف وکړي.'),
('زبان، احساسات، جذبات، خیالات اور تصورات کے حوالے سے کی گئی گفت گو کا مکمل ادراک کر سکیں۔','fully comprehend discussion about language, feelings, emotions, thoughts and concepts.','د ژبې، احساساتو، جذباتو، خیالاتو او تصوراتو په اړه شوې خبرې په بشپړ ډول درک کړي.'),
('اُردو میں اپنا مافی الضمیر پورے سیاق و سباق کے ساتھ بول چال، گفت گو اور تقریر کے ذریعے سمجھا سکیں۔','express their thoughts in Urdu, with full context, through conversation, discussion and speech.','په اردو کې خپل مافي الضمیر د بشپړ شرایطو سره په خبرو اترو، مرکې او وینا کې وړاندې کړي.'),
('عملی زندگی میں سماجی ضرورتوں کے تحت اُردو کو مہارت سے استعمال کر سکیں۔','use Urdu skilfully in practical life for social needs.','په عملي ژوند کې د ټولنیزو اړتیاوو لپاره اردو په مهارت سره وکاروي.'),
('اُردو نظم و نثر کی صورت میں موجود ادب پارے، صحافت، دفتری و عدالتی ضروریات، جدید علمی اور تکنیکی تحریروں کو پڑھ کر ان کا پورا فہم حاصل کر سکیں۔ ان کا استحسان کر سکیں اور ان پر تنقیدی رائے دے سکیں۔','read literary pieces in Urdu verse and prose, journalism, office and court needs and modern academic and technical writing, fully understand them, appreciate them and give a critical opinion on them.','د اردو نظم او نثر په بڼه ادبي ټوټې، ژورنالیزم، دفتري او عدالتي اړتیاوې، نوي علمي او تخنیکي لیکنې ولولي، پوره پوهه ترې ترلاسه کړي، ستاينه یې وکړي او پرې انتقادي نظر ورکړي.'),
('روزمرہ زندگی کے مسائل کے حوالے سے غیر رسمی خطوط لکھ سکیں۔ داخلہ فارم، شناختی کارڈ فارم اور دیگر فارم وغیرہ پُر کر سکیں۔','write informal letters about everyday problems and fill in admission forms, identity card forms and other forms.','د ورځني ژوند د مسایلو په اړه غیر رسمي لیکونه ولیکي او د داخلې فورمې، پېژندپاڼې فورمې او نورې فورمې ډکې کړي.'),
('کسی ادبی، علمی، صحافتی موضوع پر اپنے وسیع تر مطالعہ، تجربے اور مشاہدے کی روشنی میں استدلال، درست تلفظ اور عمدہ لب و لہجے کے ساتھ کم از کم پانچ منٹ تک تقریر کر سکیں۔','speak for at least five minutes on a literary, academic or journalistic topic in the light of their wide study, experience and observation, with reasoning, correct pronunciation and a fine tone.','په کوم ادبي، علمي یا خبري موضوع د خپل پراخ مطالعې، تجربې او مشاهدې په رڼا کې د استدلال، سم تلفظ او ښه لهجې سره لږ تر لږه پنځه دقیقې وینا وکړي.')],'urdu-outcomes')
F.done()
s['sourceNote']='Page “Learning outcomes” with a decorative blue border; nine star-bulleted points.'+NOTE
s['vocabulary']={}
save(s)
# scan 7 (printed ii): contents, poetry part
s=page(7,'front-matter','ii','Contents: Poetry part (Hissa-e-Nazm)','فہرست: حصۂ نظم','فهرست: د نظم برخه','toc-nazm')
F=Flow(s)
H(s,'حصۂ نظم','Poetry part (Hissa-e-Nazm)','د نظم برخه')
F.tb(0)
F.done()
rows=[('1','حمد','Hamd','ماہر القادری','Maher-ul-Qadri','115'),('2','نعت','Naat','محسن کاکوروی','Mohsin Kakorvi','118'),('3','شہر آشوب','Shehr Ashob','نظیر اکبر آبادی','Nazir Akbarabadi','121'),('4','شہزادے کا چھت پر سونا اور……','The Prince Sleeping on the Roof and …','میر حسن','Mir Hasan','125'),('5','ذرِ مراد (مرثیہ)','Durr-e-Murad (marsiya)','میر انیس','Mir Anees','128'),('6','تختِ فرس پہ علی اکبر کا خطاب','Ali Akbar’s Address on the Horse','مرزا دبیر','Mirza Dabeer','132'),('7','امید (مسدس)','Umeed (musaddas)','الطاف حسین حالی','Altaf Hussain Hali','135'),('8','نصیحتِ اخلاقی','Naseehat-e-Akhlaqi','اکبر الہ آبادی','Akbar Allahabadi','140'),('9','جلوۂ سحر','Jalwa-e-Sehar','حفیظ جالندھری','Hafeez Jalandhari','143'),('10','پرانا کوٹ','Purana Coat','سید محمد جعفری','Syed Muhammad Jafri','147'),('11','یہ سڑکیں','Yeh Sarkain','سید ضمیر جعفری','Syed Zameer Jafri','151'),('12','قطعات','Qitaat','مرزا محمود سرحدی','Mirza Mahmood Sarhadi','154'),('13','اخلاص','Ikhlas','عبدالرحمن بابا / مترجم: طٰہٰ خان','Abdur Rahman Baba / translator: Taha Khan','157')]
s['tables']=[table('Contents of the poetry part','حصۂ نظم کی فہرست','د نظم برخې فهرست',[c('No.','شمار','شمېره'),c('Title','عنوان','سرلیک'),c('Poet','شاعر','شاعر'),c('Page','صفحہ','پاڼه')],[[c(n),c(e,u,e),c(pe,pu,pe),c(pg)] for n,u,e,pu,pe,pg in rows],sourceGap=dict(note='Printed with columns in the order: page, poet, title, number (right to left). Title translations to Pashto are shown in English; the Urdu titles are exact.'))]
s['sourceNote']='Printed page ii (scan 7): contents of the poetry part, 13 rows, with a books illustration. The prose-part contents (printed page i, scan 6) is absent from the supplied scans.'+NOTE
s['vocabulary']={}
save(s)
# scan 8
s=page(8,'front-matter','','Contents: Ghazal part (Hissa-e-Ghazal)','فہرست: حصۂ غزل','فهرست: د غزل برخه','toc-ghazal')
F=Flow(s)
H(s,'حصۂ غزل','Ghazal part (Hissa-e-Ghazal)','د غزل برخه')
F.tb(0)
F.done()
rows=[('1','فقیرانہ آئے صدا کر چلے / جس سر کو غرور آج ہے یاں تاج وری کا','Faqeerana aaye sada kar chale / Jis sar ko ghurur aaj hai yaan taaj-wari ka','میر تقی میر','Mir Taqi Mir','161, 162'),('2','قتلِ عاشق کسی معشوق سے کچھ دور نہ تھا','Qatl-e-ashiq kisi mashooq se kuchh door na tha','خواجہ میر درد','Khwaja Mir Dard','166'),('3','ناگہ چمن میں جب وہ گل اندام آ گیا','Nagah chaman mein jab woh gul-andaam aa gaya','غلام ہمدانی مصحفی','Ghulam Hamdani Mushafi','168'),('4','دائم پڑا ہوا ترے در پر نہیں ہوں میں / ہزاروں خواہشیں ایسی کہ ہر خواہش پہ دم نکلے','Daaim pada hua tere dar par nahin hoon main / Hazaron khwahishen aisi ke har khwahish pe dam nikle','مرزا غالب','Mirza Ghalib','172, 173'),('5','آئنہ اپنی نظر سے نہ جدا ہونے دو','Aaina apni nazar se na juda hone do','داغ دہلوی','Dagh Dehlvi','176'),('—','فرہنگ','Farhang (glossary)','—','—','178')]
s['tables']=[table('Contents of the ghazal part','حصۂ غزل کی فہرست','د غزل برخې فهرست',[c('No.','شمار','شمېره'),c('Opening line(s)','مطلع / عنوان','مطلع / سرلیک'),c('Poet','شاعر','شاعر'),c('Page','صفحہ','پاڼه')],[[c(n),c(e,u,e),c(pe,pu,pe),c(pg)] for n,u,e,pu,pe,pg in rows],sourceGap=dict(note='Printed with a star (☆) beside each ghazal title. The Farhang (glossary) row is listed at printed page 178 as printed here; in the scans the glossary starts at scan 185.'))]
s['sourceNote']='Scan 8 (no printed number visible): contents of the ghazal part, five ghazals and the glossary; a faint books illustration is behind the table.'+NOTE
s['vocabulary']={}
save(s)
