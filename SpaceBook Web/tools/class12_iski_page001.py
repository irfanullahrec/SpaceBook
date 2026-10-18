"""Islamiat (Ikhtiari) XII PDF1-5: cover, credits, preface, table of contents, p.1 (chapter 1 opening).
Run: python class12_iski_page001.py N (1,3,4,5)."""
import sys
from class12_iski_common import BOOK, Builder, rec, P, L, AR

TOC = [
 ('Chapter 1: The Holy Quran', 'باب اول: قرآن مجید', '۱ څپرکی: قرآن مجید', '1'),
 ('A. Inimitability of the Quran, eloquence and rhetoric, universality and variety, permanence / everlasting code of life', 'الف۔ اعجاز القرآن، فصاحت و بلاغت، ہمہ گیریت اور تنوع، دوام/دائمی ضابطۂ حیات', 'الف. د قرآن اعجاز، فصاحت او بلاغت، هراړخیزتوب او تنوع، دوام / د ژوند تلپاتې دستور', '1'),
 ('B. Translation and exegesis of the Quran', 'ب۔ ترجمہ و تفسیر قرآن', 'ب. د قرآن ژباړه او تفسیر', '12'),
 ('• Conditions and limits of Quranic exegesis', '• تفسیر قرآن کی شرائط اور حدود', '• د قرآن د تفسیر شرطونه او حدود', '12'),
 ('• Principles of exegesis (selection from al-Fawz al-Kabir)', '• اصولِ تفسیرِ قرآن (الفوز الکبیر سے انتخاب)', '• د تفسیر اصول (له الفوز الکبیر څخه انتخاب)', '14'),
 ('• Exegetical literature and a brief introduction to some famous translations and commentaries', '• تفسیری ادب اور چند مشہور تراجم و تفاسیر کا اجمالی تعارف', '• تفسیري ادب او د ځینو مشهورو ژباړو او تفسیرونو لنډه پېژندنه', '15'),
 ('C. Basic themes of the Holy Quran', 'ج۔ قرآن مجید کی اساسی مباحث', 'ج. د قرآن مجید بنسټیز بحثونه', '20'),
 ('• Economic issues', '• معاشی مسائل', '• اقتصادي مسایل', '20'),
 ('• Stories of the prophets — style and purposes', '• قصص الانبیاء۔ انداز بیان اور مقاصد', '• د پیغمبرانو قصې — د بیان انداز او موخې', '29'),
 ('• Purification of the self, household management and civic politics', '• تزکیہ نفس، تدبیر منزل اور سیاستِ مدنیہ', '• د نفس تزکیه، د کور تدبیر او مدني سیاست', '34'),
 ('D. Worship', 'د۔ عبادات', 'د. عبادتونه', '44'),
 ('• Spending: zakat, charities and alms — basic rules and principles, social importance, economic stability', '• انفاق: زکوٰۃ، صدقات اور خیرات، بنیادی ضابطے اور اصول، معاشرتی اہمیت، معاشی استحکام', '• انفاق: زکات، صدقې او خیرات — بنسټیز مقررات او اصول، ټولنیز اهمیت، اقتصادي ثبات', '44'),
 ('• Responsibilities of the individual and society and duties of the state', '• فرد اور معاشرہ کی ذمہ داریاں اور ریاست کے فرائض', '• د فرد او ټولنې مسؤلیتونه او د دولت دندې', '51'),
 ('E. Study of the Sirah of the Messenger of Allah ﷺ in the light of the Holy Quran', 'ہ۔ سیرۃ رسول اللہ صلی اللہ علیہ وآلہٖ وسلم کا قرآن مجید کی روشنی میں مطالعہ', 'هـ. د قرآن مجید په رڼا کې د رسول الله ﷺ د سیرت مطالعه', '61'),
 ('• Freedom of thought, respect for humanity, basis of mutual relations', '• آزادیٔ فکر، احترامِ آدمیت، تعلقاتِ باہمی کی اساس', '• د فکر ازادي، د انسانیت درناوی، د ګډو اړیکو بنسټ', '61'),
 ('• Guiding principles of the early Muslim society', '• اولین مسلم معاشرہ کے راہنما اصول', '• د لومړنۍ مسلمانې ټولنې لارښود اصول', '66'),
 ('F. Selected verses of the Quran — translation and exegesis', 'و۔ منتخب آیاتِ قرآن۔ ترجمہ و تفسیر', 'و. د قرآن غوره آیتونه — ژباړه او تفسیر', '71'),
 ('• Surah al-Baqarah', '• سورۃ البقرۃ', '• سورة البقره', '71'),
 ('Chapter 2: Hadith', 'باب دوم: حدیث', '۲ څپرکی: حدیث', '97'),
 ('• Hadith as a source of rulings, legislative status of hadith, authority of hadith', '• حدیث بطور ماخذِ احکام، حدیث کی تشریعی حیثیت، حجیتِ حدیث', '• حدیث د احکامو د سرچینې په توګه، د حدیث تشریعي حیثیت، د حدیث حجیت', '97'),
 ('• Principles of hadith — study of selected topics of Nukhbat al-Fikar', '• اصولِ حدیث۔ نخبۃ الفکر کے منتخب مباحث کا مطالعہ', '• د حدیث اصول — د نخبة الفکر د غوره بحثونو مطالعه', '111'),
 ('• Approach and prominent principles of Imam Bukhari and Imam Muslim in selecting hadith', '• امام بخاری اور امام مسلم کا انتخابِ حدیث میں رویہ اور نمایاں اصول', '• د حدیث په انتخاب کې د امام بخاري او امام مسلم چلند او ښکاره اصول', '114'),
 ('• Special study of selected hadiths — translation and explanation', '• منتخب احادیث کا خصوصی مطالعہ ترجمہ و تشریح', '• د غوره احادیثو ځانګړې مطالعه — ژباړه او تشریح', '118'),
 ('Chapter 3: Services of Muslims in academic progress', 'باب سوم: علمی پیش رفت میں مسلمانوں کی خدمات', '۳ څپرکی: په علمي پرمختګ کې د مسلمانانو خدمتونه', '149'),
 ('• Mention of some prominent sciences and services of Muslims', '• چند نمایاں علوم کا تذکرہ اور مسلمانوں کی خدمات', '• د ځینو ښکاره علومو یادونه او د مسلمانانو خدمتونه', '150'),
 ('• Religious sciences', '• دینی علوم', '• دیني علوم', '150'),
 ('• Social sciences', '• معاشرتی علوم', '• ټولنیز علوم', '154'),
 ('• Economic sciences', '• معاشی علوم', '• اقتصادي علوم', '160'),
 ('• Scientific sciences', '• سائنسی علوم', '• ساینسي علوم', '168'),
 ('• Progress of sciences in Andalusia — services and influences', '• اندلس میں علوم کی ترقی۔ خدمات اور اثرات', '• په اندلس کې د علومو پرمختګ — خدمتونه او اغېزې', '171'),
 ('• The state of knowledge in the Muslim world in the period of decline — causes and effects of neglect', '• دورِ انحطاط میں مسلم دنیا میں علم کی حالت، بے توجہی کے اسباب اور اثرات', '• د زوال په دوره کې په اسلامي نړۍ کې د علم حالت، د بې‌پامۍ لاملونه او اغېزې', '176'),
 ('• Responsibilities of the Muslim ummah with reference to academic progress in the present and future', '• عصرِ حاضر اور مستقبل میں علمی پیش رفت کے حوالے سے مسلمان امت کی ذمہ داریاں', '• په اوسني او راتلونکي کې د علمي پرمختګ په حواله د مسلمان امت مسؤلیتونه', '178'),
 ('• Possible efforts of individuals and the collective for spreading knowledge — the plan of the future and the attitude of the ummah', '• اشاعتِ علم کے لیے افراد اور اجتماع کی ممکنہ کاوشیں۔ مستقبل کا نقشہ اور امت کا رویہ', '• د علم د خپرولو لپاره د افرادو او ټولنې ممکنه هڅې — د راتلونکي نقشه او د امت چلند', '183'),
 ('Chapter 4: The Islamic system of government and state', 'باب چہارم: اسلام کا نظامِ حکومت و ریاست', '۴ څپرکی: د اسلام د حکومت او دولت نظام', '186'),
 ('• The concept of the Islamic system of government and possible efforts for it in the modern age', '• اسلامی نظامِ حکومت کا تصور اور دورِ جدید میں اس کی ممکنہ کوششیں', '• د اسلامي حکومت د نظام تصور او په نوي عصر کې د هغه ممکنه هڅې', '186'),
 ('Chapter 5: The present age and Islamic states', 'باب پنجم: عصرِ حاضر اور اسلامی ریاستیں', '۵ څپرکی: اوسنی عصر او اسلامي دولتونه', '200'),
 ('• Religious, social and cultural difficulties of Muslims in non-Muslim states and their solution', '• غیر مسلم ریاستوں میں مسلمانوں کی دینی، سماجی اور ثقافتی مشکلات اور ان کا حل', '• په غیرمسلم دولتونو کې د مسلمانانو دیني، ټولنیزې او کلتوري ستونزې او د هغو حل', '200'),
 ('• Pakistan as a Muslim state', '• پاکستان۔ بطور مسلم ریاست', '• پاکستان د مسلمان دولت په توګه', '203'),
 ('• Movement, formation and political condition', '• تحریک، تشکیل اور سیاسی حالت', '• خوځښت، جوړښت او سیاسي حالت', '204'),
 ('• Pakistan as an Islamic welfare state', '• پاکستان بحیثیت اسلامی فلاحی ریاست', '• پاکستان د اسلامي هوساینیز دولت په توګه', '207'),
 ('Chapter 6: Arabic language and literature', 'باب ششم: عربی زبان و ادب', '۶ څپرکی: عربي ژبه او ادب', '215'),
 ('• Study of Arabic literature', '• عربی ادب کا مطالعہ', '• د عربي ادب مطالعه', '215'),
 ('• Study of some verses with reference to Arabic literature', '• عربی ادب کے حوالے سے چند آیات کا مطالعہ', '• د عربي ادب په حواله د ځینو آیتونو مطالعه', '216'),
 ('• Study with reference to literary greatness: sermons of the Messenger ﷺ', '• ادبی عظمت کے حوالے سے مطالعہ: خطباتِ رسول ﷺ', '• د ادبي عظمت په حواله مطالعه: د رسول ﷺ خطبې', '224'),
 ('• Letters of the rightly-guided caliphs', '• خلفائے راشدین کے خطوط', '• د خلفای راشدینو لیکونه', '227'),
 ('• Jurisprudential texts and literature', '• فقہی عبارات و ادب', '• فقهي متنونه او ادب', '235')]


def toc(b, rows, tid):
    b.table(tid, ['Contents', 'Page'], [[r[0], r[3]] for r in rows], ['عنوانات', 'صفحہ نمبر'], ['سرلیکونه', 'مخ'],
            [[r[1], r[3]] for r in rows], [[r[2], r[3]] for r in rows])


def p1():
    b = Builder()
    b.h('Islamiat (Elective) for class twelve', 'اسلامیات (اختیاری) برائے بارہویں جماعت', 'اسلامیات (اختیاري) د دولسم ټولګي لپاره')
    P(b, [('Front cover: the Holy Kaaba and the Sacred Mosque; Khyber Pakhtunkhwa Textbook Board, Peshawar (emblem). [photograph described, not reproduced]', 'سرورق: خانہ کعبہ اور مسجد الحرام؛ خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور (نشان)۔ [تصویر کی وضاحت]', 'پوښ: کعبه شریفه او مسجد الحرام؛ د خیبر پښتونخوا درسي کتابونو بورډ، پېښور (نښان). [د انځور تشریح]')])
    BOOK.save(1, [('FM', rec(b, 'FM', 1, 1, [None], first=True, kind='cover'))], issues=[{'id': 'iski12-pdf001', 'unit': 'FM', 'printedPage': None,
               'description': 'Cover scan carries handwritten scribbles and a “Free from Government / NOT FOR SALE” stamp — excluded. PDF2 is a third-party website advertisement — marked excluded.'}])


def p3():
    b = Builder()
    P(b, [('All rights reserved with Leading Books Publishers.', 'جملہ حقوق بحق لیڈنگ بکس پبلشر محفوظ ہیں', 'ټول حقونه د لیډنګ بکس خپرندویه سره خوندي دي.'),
          ('Approved by: Directorate of Curriculum and Teacher Education, Khyber Pakhtunkhwa, Abbottabad. According to: National Curriculum 2006. Letter no. 8324-26/F.03/Vol-I/Is.Ele.(Urdu)-XII dated 27.10.2017.', 'منظور کردہ: نظامت نصاب و تعلیم اساتذہ خیبر پختونخوا، ایبٹ آباد۔ بمطابق: قومی نصاب 2006۔ مراسلہ نمبر 8324-26/F.03/Vol-I/Is.Ele.(Urdu)-XII مورخہ 27.10.2017', 'منظور کوونکی: د خیبر پښتونخوا د نصاب او ښوونکو د زده‌کړې ریاست، ایبټ اباد. د ۲۰۰۶ ملي نصاب سره سم. لیک شمېره 8324-26/F.03/Vol-I/Is.Ele.(Urdu)-XII نېټه 27.10.2017.'),
          ('Authors: Dr Shafqat Ali Janjua, Ahmad Saeed, Niaz Muhammad. Supervisor of review: Gohar Ali Khan, Director DCTE, Abbottabad.', 'مصنفین: ڈاکٹر شفقت علی جنجوعہ، احمد سعید، نیاز محمد۔ نگرانِ نظرِ ثانی: گوہر علی خان، ڈائریکٹر ڈی۔سی۔ٹی۔ای، ایبٹ آباد۔', 'لیکوالان: ډاکټر شفقت علي جنجوعه، احمد سعید، نیاز محمد. د بیاکتنې څارونکی: ګوهر علي خان، ډایرکټر DCTE، ایبټ اباد.'),
          ('Review: Dr Mufti Abdul Wahab (Associate Professor, Government Degree College Mandian, Abbottabad); Safdar Rahman (Directorate of Curriculum and Teacher Education, Abbottabad); Professor Abdul Saboor (Government College No. 1, Abbottabad); Professor Ahmad Jan (Assistant Professor, Government Post Graduate College No. 1, Abbottabad); Syed Rifaqat Ali Shah (subject specialist, Textbook Board Peshawar).', 'نظرِ ثانی: ڈاکٹر مفتی عبدالوہاب ایسوسی ایٹ پروفیسر گورنمنٹ ڈگری کالج منڈیاں ایبٹ آباد؛ صفدر رحمان نظامت نصاب و تعلیم اساتذہ ایبٹ آباد؛ پروفیسر عبدالصبور گورنمنٹ کالج نمبر 1 ایبٹ آباد؛ پروفیسر احمد جان اسسٹنٹ پروفیسر گورنمنٹ پوسٹ گریجویٹ کالج نمبر 1 ایبٹ آباد؛ سید رفاقت علی شاہ ماہر مضمون، ٹیکسٹ بک بورڈ پشاور۔', 'بیاکتنه: ډاکټر مفتي عبدالوهاب (اسوسیېټ پروفیسر، د منډیان حکومتي ډګري کالج، ایبټ اباد)؛ صفدر رحمان (د نصاب او ښوونکو د زده‌کړې ریاست، ایبټ اباد)؛ پروفیسر عبدالصبور (حکومتي کالج ۱ شمېره، ایبټ اباد)؛ پروفیسر احمد جان (اسسټنټ پروفیسر، حکومتي پوسټ ګرېجویټ کالج ۱ شمېره، ایبټ اباد)؛ سید رفاقت علي شاه (د مضمون متخصص، درسي کتابونو بورډ پېښور).'),
          ('Second review: Dr Mufti Abdul Wahab (Professor, Vice Principal, Government Post Graduate College No. 1, Abbottabad); Qari Abdul Shakoor (senior teacher of Islamiat, Government High School Jhangi, Abbottabad); Izazullah (subject specialist, Islamiat, Khyber Pakhtunkhwa Textbook Board, Peshawar); Hidayatullah (Additional Director, Directorate of Curriculum and Teacher Education, Khyber Pakhtunkhwa, Abbottabad).', 'دوبارہ نظرِ ثانی: ڈاکٹر مفتی عبدالوہاب پروفیسر۔ وائس پرنسپل گورنمنٹ پوسٹ گریجویٹ کالج نمبر 1 ایبٹ آباد؛ قاری عبدالشکور سینئر معلم اسلامیات گورنمنٹ ہائی سکول جھنگی، ایبٹ آباد؛ اعزاز اللہ، ماہرِ مضمون (اسلامیات)، خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور؛ ہدایت اللہ، ایڈیشنل ڈائریکٹر، نظامت نصاب و تعلیم اساتذہ خیبر پختونخوا ایبٹ آباد۔', 'دوهمه بیاکتنه: ډاکټر مفتي عبدالوهاب (پروفیسر، مرستیال پرنسپل، حکومتي پوسټ ګرېجویټ کالج ۱ شمېره، ایبټ اباد)؛ قاري عبدالشکور (د اسلامیاتو لوړ ښوونکی، جهنګي حکومتي عالي ښوونځی، ایبټ اباد)؛ اعزاز الله (د اسلامیاتو متخصص، د خیبر پښتونخوا درسي کتابونو بورډ، پېښور)؛ هدایت الله (اضافي ډایرکټر، د خیبر پښتونخوا د نصاب او ښوونکو د زده‌کړې ریاست، ایبټ اباد).'),
          ('Editor: Dr Sajid-ur-Rahman Orakzai, subject specialist, Khyber Pakhtunkhwa Textbook Board, Peshawar. Printing supervision: Ismatullah Khan Gandapur, Chairman; Saeed-ur-Rahman (Member Printing), Khyber Pakhtunkhwa Textbook Board, Peshawar. 2020-21. www.kptbb.gov.pk · membertbb@yahoo.com · 091-9217159-60', 'ایڈیٹر: ڈاکٹر ساجد الرحمٰن اورکزئی، ماہرِ مضمون، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔ طباعت زیرِ نگرانی: عصمت اللہ خان گنڈاپور، چیئرمین؛ سعید الرحمٰن (ممبر پرنٹنگ)، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔ 2020-21 · www.kptbb.gov.pk · membertbb@yahoo.com · 091-9217159-60', 'مدیر: ډاکټر ساجد الرحمن اورکزي، د مضمون متخصص، د خیبر پښتونخوا درسي کتابونو بورډ، پېښور. د چاپ څارنه: عصمت الله خان ګنډاپور، رئیس؛ سعید الرحمن (د چاپ غړی)، د خیبر پښتونخوا درسي کتابونو بورډ، پېښور. ۲۰۲۰-۲۱ · www.kptbb.gov.pk · membertbb@yahoo.com · 091-9217159-60')])
    r1 = rec(b, 'FM', 2, 3, ['ii'], kind='credits')
    t = Builder()
    AR(t, 'بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِیْمِ')
    t.h('Preface', 'پیش لفظ', 'سریزه')
    P(t, [('In making the State of Pakistan this great purpose was at work, that in Pakistan Islamic injunctions would be enforced and Muslims would obtain religious freedom. Allah Most High granted success in this purpose and in 1947 Pakistan came into being. Being an Islamic country, whose ideology of life is Islam, and being Muslims, it is our effort that we create love and affection for Islamic values in our male and female students, so that they mould their personality and character into the Islamic pattern. To fulfil this same purpose the Government of Khyber Pakhtunkhwa has tried to make Islamiat (Elective) effective and useful, so that the syllabus is balanced, purposeful and according to the demands of the modern age, and male and female students succeed in achieving the purposes and do not become entangled in unnecessary burden.', 'مملکتِ پاکستان بنانے میں یہ عظیم مقصد کارفرما تھا کہ پاکستان میں اسلامی احکام نافذ کیے جائیں گے اور مسلمانوں کو مذہبی آزادی حاصل ہو گی۔ اللہ تعالیٰ نے اس مقصد میں کامیابی عطا فرمائی اور 1947ء میں پاکستان کا قیام عمل میں لایا گیا۔ اسلامی ملک ہونے کے سبب اس کا نظریۂ حیات اسلام ہے اور مسلمان ہونے کے ناطے ہماری کوشش ہے کہ ہم اپنے طلبہ و طالبات میں اسلامی اقدار سے محبت و الفت پیدا کریں تاکہ وہ اپنی شخصیت و کردار کو اسلامی سانچے میں ڈھالیں۔ اسی مقصد کو پورا کرنے کے لیے حکومتِ خیبر پختونخوا نے اسلامیات (اختیاری) کو موثر اور مفید بنانے کے لیے کوشش کی ہے کہ نصاب متوازن، بامقصد اور جدید دور کے تقاضوں کے مطابق ہو اور طلبہ اور طالبات کو حصولِ مقاصد میں کامیابی ہو اور غیر ضروری بوجھ میں الجھنے نہ پائیں۔', 'د پاکستان د دولت په جوړولو کې دا ستره موخه کارګره وه چې په پاکستان کې به اسلامي احکام پلي کېږي او مسلمانانو ته به دیني ازادي ورکول کېږي. الله تعالی په دې موخه کې بریا ورکړه او په ۱۹۴۷ کې پاکستان جوړ شو. د اسلامي هېواد په توګه یې د ژوند نظریه اسلام ده، او د مسلمانانو په توګه زموږ هڅه ده چې په خپلو زده‌کوونکو هلکانو او نجونو کې له اسلامي ارزښتونو سره مینه او الفت پیدا کړو، تر څو خپل شخصیت او کردار په اسلامي قالب کې واچوي. د همدې موخې د پوره کولو لپاره د خیبر پښتونخوا حکومت هڅه کړې چې اسلامیات (اختیاري) اغېزمن او ګټور کړي، تر څو نصاب متوازن، بامقصده او د نوي عصر د غوښتنو سره سم وي، او زده‌کوونکي د موخو په ترلاسه کولو کې بریالي شي او په غیرضروري بار کې ښکېل نشي.'),
          ('The book under consideration is according to the mental level of the students of class twelve, and effort has been made to remove their religious thirst. In this book, about the first source of Islam, the Quran, its truthfulness, universality and inimitability are told. It has also been tried to make clear that the Quran emphasises not only beliefs and worships but also covers dealings and morals. A brief introduction to important exegeses too has been given. The principles of the early Muslim society too have been told. Selected Quranic verses and hadiths have not only been included in the book, but explanation too has been made for clarity of their concepts. Along with the Sirah of the Messenger of Allah ﷺ, the terminology of hadith, their introduction and the important kinds of hadith have been included briefly.', 'زیرِ نظر کتاب بارہویں جماعت کے طلبہ کے ذہنی سطح کے مطابق ہے اور ان کی دینی تشنگی دور کرنے کی کوشش کی گئی ہے۔ اس کتاب میں اسلام کے ماخذِ اول قرآن کی حقانیت، عالمگیریت اور اعجاز کے بارے میں بتایا گیا ہے۔ یہ بھی واضح کرنے کی کوشش کی گئی ہے کہ قرآن نہ صرف اعتقادات اور عبادات پر زور دیتا ہے بلکہ یہ معاملات اور اخلاقیات کا بھی احاطہ کرتا ہے۔ اجمالی طور پر اہم تفاسیر کا بھی تعارف کرایا گیا ہے۔ اولین مسلم معاشرے کے اصول بھی بتائے گئے ہیں۔ منتخب قرآنی آیات اور احادیث کو نہ صرف شاملِ کتاب کیا گیا ہے بلکہ مفاہیم اور وضاحت کے لیے تشریح بھی کی گئی ہے۔ سیرت رسول صلی اللہ علیہ وآلہٖ وسلم کے ساتھ ساتھ احادیث کی اصطلاحات، ان کا تعارف اور احادیث کی چند اقسام مختصر طور پر شامل کی گئی ہیں۔', 'تر غور لاندې کتاب د دولسم ټولګي د زده‌کوونکو د ذهني کچې سره سم دی او د هغوی د دیني تندې د لرې کولو هڅه شوې. په دې کتاب کې د اسلام د لومړۍ سرچینې قرآن د حقانیت، نړیوالتوب او اعجاز په اړه ویل شوي. دا هم روښانه کولو هڅه شوې چې قرآن نه یوازې پر عقایدو او عباداتو ټینګار کوي، بلکې معاملات او اخلاق هم رانغاړي. په لنډه توګه د مهمو تفسیرونو پېژندنه هم شوې. د لومړنۍ مسلمانې ټولنې اصول هم ښودل شوي. غوره قرآني آیتونه او احادیث نه یوازې په کتاب کې شامل شوي، بلکې د مفهومونو او وضاحت لپاره یې تشریح هم شوې. د رسول الله ﷺ د سیرت ترڅنګ د حدیث اصطلاحات، د هغو پېژندنه او د احادیثو ځینې ډولونه په لنډه توګه شامل شوي.'),
          ('In the scientific sciences, the progress of Muslims and the causes of their decline have not only been stated in easy style, but rather such a highway too has been pointed out, walking on which they can restore their lost past glory. At the end, to acquaint students with Arabic language and literature, sermons of the Messenger of Allah ﷺ and letters of the rightly-guided caliphs too have been included in the book.', 'سائنسی علوم میں مسلمانوں کی ترقی اور ان کے تنزل کے اسباب کو نہ صرف آسان پیرائے میں بیان کیا گیا ہے بلکہ ایک ایسی شاہراہ کی بھی نشاندہی کر دی گئی ہے جس پر چل کر وہ اپنی کھوئی ہوئی عظمتِ رفتہ کو بحال کر سکتے ہیں۔ کتاب کے آخر میں طلبہ کو عربی زبان و ادب سے روشناس کرنے کے لیے خطباتِ رسول صلی اللہ علیہ وآلہٖ وسلم اور خطوطِ خلفائے راشدین کو بھی شامل کیا گیا ہے۔', 'په ساینسي علومو کې د مسلمانانو پرمختګ او د هغوی د زوال لاملونه نه یوازې په اسانه انداز بیان شوي، بلکې داسې لویه لاره هم په ګوته شوې چې پرې په تګ خپل ورک شوی تېر عظمت بېرته راژوندی کولی شي. د کتاب په پای کې د زده‌کوونکو د عربي ژبې او ادب سره د پېژندنې لپاره د رسول الله ﷺ خطبې او د خلفای راشدینو لیکونه هم شامل شوي.')])
    r2 = rec(t, 'FM', 3, 3, ['iii'], kind='preface')
    BOOK.save(3, [('FM', r1), ('FM', r2)], issues=[{'id': 'iski12-pdf003', 'unit': 'FM', 'printedPage': None,
               'description': 'Credits page and preface (one page). Preface printed with a run-on sentence order at its end (“…خطوط خلفائے راشدین کو بھی شامل کیا گیا ہے”) — rendered in reading order.'}])


def p4():
    b = Builder()
    b.h('Table of contents', 'فہرستِ عنوانات', 'د سرلیکونو فهرست')
    toc(b, TOC[:13], 'iski12-toc-1')
    r1 = rec(b, 'FM', 4, 4, ['iv'], kind='contents')
    t = Builder()
    toc(t, TOC[13:31], 'iski12-toc-2')
    BOOK.save(4, [('FM', r1), ('FM', rec(t, 'FM', 5, 4, ['v'], kind='contents'))])


def p5():
    b = Builder()
    toc(b, TOC[31:], 'iski12-toc-3')
    r1 = rec(b, 'FM', 6, 5, ['vi'], kind='contents')
    t = Builder()
    AR(t, 'بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِیْمِ')
    P(t, [('Beginning with the name of Allah, who is most kind, most merciful.', 'شروع اللہ کا نام لے کر جو بڑا مہربان نہایت رحم والا ہے', 'د الله په نوم پیل چې ډېر مهربان او ډېر رحم کوونکی دی.')])
    t.h('Chapter one — The Holy Quran', 'باب اول — قرآنِ مجید', 'لومړی څپرکی — قرآن مجید')
    t.h('Teaching objectives', 'تدریسی مقاصد', 'تدریسي موخې')
    P(t, [('The purpose of this lesson is to make male and female students able that they:', 'اس سبق کا مقصد طلبہ اور طالبات کو اس قابل بنانا ہے کہ وہ:', 'د دې لوست موخه دا ده چې زده‌کوونکي هلکان او نجونې دې ته وړ شي چې:')])
    L(t, [('1. can know the concept of revelation and become acquainted with the revealed books;', '1۔ وحی کا مفہوم جان سکیں اور الہامی کتب سے آشنا ہو سکیں۔', '۱. د وحې مفهوم وپېژني او له الهامي کتابونو سره اشنا شي؛'),
          ('2. can know the writing and script of the Holy Quran, can read the Holy Quran in the correct way through familiarity with the stop-marks in the Holy Quran, and can also observe the etiquette of recitation and the matters related to it;', '2۔ قرآن مجید کی کتابت، رسم الخط کو جان سکیں اور قرآن مجید میں رموزِ اوقاف سے واقفیت کے ذریعے قرآن مجید کو درست طریقے سے پڑھ سکیں نیز وہ آدابِ تلاوت اور اس سے متعلق امور کی پابندی کر سکیں۔', '۲. د قرآن مجید کتابت او رسم الخط وپېژني، او په قرآن مجید کې د وقف نښو په پېژندلو قرآن مجید په سمه توګه ولولي، او همداسې د تلاوت اداب او اړوند چارې مراعات کړي؛'),
          ('3. can study the Holy Quran with the perception of its eloquence and rhetoric and with the understanding of the universality and variety of its subjects in such a way that they come to know that the Holy Quran is a permanent code of life.', '3۔ قرآن مجید کو اس کی فصاحت و بلاغت کے ادراک اور اس کے مضامین کی ہمہ گیریت و تنوع کے فہم کے ساتھ اس طرح مطالعہ کر سکیں کہ انہیں معلوم ہو جائے کہ قرآن مجید دائمی ضابطۂ حیات ہے۔', '۳. قرآن مجید د هغه د فصاحت او بلاغت په درک او د مضامینو د هراړخیزتوب او تنوع په پوهې سره داسې مطالعه کړي چې پوه شي چې قرآن مجید د ژوند تلپاتې دستور دی.')])
    t.h('A. Inimitability of the Quran', 'ا۔ اعجاز القرآن:', 'الف. د قرآن اعجاز')
    P(t, [('In the Holy Quran guidance exists for scientific evolution and for the material, social, economic, moral, political, civilisational and spiritual needs of human beings. Along with scientific evolution these guidances are coming in front ever more brightly. As human thought and reflection is gaining stability and maturity, so the depth of the meaningfulness of this complete code is coming to the fore. In this way the Holy Quran has the status of a miracle in every respect, e.g.: this is the only book which has remained preserved in the breasts of millions of human beings in every age, and will remain preserved. In the same way this is the only book which in every age on the face of the earth has been read the most.', 'قرآن مجید میں سائنسی ارتقاء، انسانوں کی مادی، معاشرتی، معاشی، اخلاقی، سیاسی، تمدنی اور روحانی ضرورتوں کی رہنمائی کے لیے ہدایات موجود ہیں۔ سائنسی ارتقاء کے ساتھ ساتھ یہ ہدایات مزید نکھر کر سامنے آ رہی ہیں۔ جیسے جیسے انسانی سوچ و فکر میں استحکام اور استحسان آ رہا ہے ویسے ویسے اس ضابطۂ کامل کی معنویت کی گہرائی سامنے آ رہی ہے۔ یوں تو قرآن مجید کئی لحاظ سے معجزے کی حیثیت رکھتا ہے، مثلاً: یہ واحد کتاب ہے جو ہر زمانے میں لاکھوں انسانوں کے سینوں میں محفوظ رہی، محفوظ ہے اور محفوظ رہے گی۔ اسی طرح یہ واحد کتاب ہے جو روئے زمین پر ہر زمانے میں سب سے زیادہ پڑھی جاتی رہی ہے۔', 'په قرآن مجید کې د ساینسي ودې او د انسانانو د مادي، ټولنیزو، اقتصادي، اخلاقي، سیاسي، مدني او روحاني اړتیاوو د لارښوونې لپاره هدایتونه شته. د ساینسي ودې ترڅنګ دا هدایتونه لا روښانه مخې ته راځي. څنګه چې د انسان په فکر کې ثبات او پوخوالی راځي، همداسې د دې بشپړ دستور د معنا ژوروالی څرګندېږي. په ډېرو لحاظونو قرآن مجید د معجزې حیثیت لري، لکه: دا یوازینی کتاب دی چې په هر عصر کې د لکونو انسانانو په سینو کې خوندي پاتې شوی، خوندي دی او خوندي به پاتې شي. همداسې دا یوازینی کتاب دی چې د ځمکې پر مخ په هر عصر کې تر ټولو ډېر لوستل شوی.')])
    r2 = rec(t, 1, 1, 5, [1], first=True)
    BOOK.save(5, [('FM', r1), (1, r2)], issues=[{'id': 'iski12-pdf005', 'unit': 1, 'printedPage': 1,
               'description': 'p.1 carries a handwritten date note and a “NOT FOR SALE” stamp — excluded. Contents table transcribed as structured data.'}])


if __name__ == '__main__':
    {1: p1, 3: p3, 4: p4, 5: p5}[int(sys.argv[1]) if len(sys.argv) > 1 else 1]()
