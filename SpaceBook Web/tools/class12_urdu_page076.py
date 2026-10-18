"""Urdu XII PDF76 (spread): printed pp.142–143 — Lesson 14 text end (source مردم دیدہ), مشق Q1–Q4 and grammar note محاورہ اور روزمرہ."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
t = Builder()
for x in [
    ("Love of the Prophet had melted his heart. When he took the name of the Holy Prophet (peace and blessings of Allah be upon him and his family), his eyes would fill with tears, and while reciting the Qur’an he would weep involuntarily. In short, his personality was endlessly charming. Those who have only read his verse and not met him are unaware of Iqbal’s higher excellences.",
     'عشقِ رسولؐ نے ان کے دل کو گداز کر رکھا تھا۔ نبی کریم صلی اللہ علیہ وآلہٖ وسلّم کا نام لیتے وقت ان کی آنکھیں پُرنم ہو جاتی تھیں اور قرآن پڑھتے پڑھتے بے اختیار رو پڑتے تھے۔ غرض ان کی شخصیت بے حد دلآویز تھی۔ جن لوگوں نے صرف ان کا کلام پڑھا ہے اور ان سے ملے نہیں، تو وہ اقبالؒ کے اعلیٰ کمالات سے بے خبر ہیں۔',
     'د رسول ﷺ مینې د هغه زړه نرم کړی و. د نبي کریم صلی الله علیه وآله وسلم د نوم اخیستو پر وخت به یې سترګې له اوښکو ډکې شوې او د قرآن د لوستلو پر مهال به بې‌اختیاره وژړل. لنډه دا چې د هغه شخصیت بې‌حده زړه‌راښکونکی و. کومو خلکو چې یوازې د هغه کلام لوستی او ورسره لیدلي یې نه دي، د اقبال له لوړو کمالاتو بې‌خبره دي.'),
    ("About two and a half years before his death he moved into his newly built bungalow on Mayo Road. He had not been there many days when his Begum Sahiba passed away. He was greatly grieved by this event. I saw him in that state: the late lady’s grave was being dug and he sat close by with his hand on his forehead. At that time he looked very old — his back bent and his face pale. After this event his health kept declining steadily. At last he died on 21 April 1938 and was buried outside the Badshahi (Shahi) Mosque.",
     'موت سے کوئی ڈھائی سال پہلے وہ میو روڈ پر اپنی نوتعمیر کوٹھی میں اٹھ گئے۔ وہاں گئے ابھی تھوڑے دن ہوئے تھے کہ ان کی بیگم صاحبہ کا انتقال ہو گیا۔ انھیں اس واقعے کا بہت صدمہ ہوا۔ میں نے اس حالت میں انھیں دیکھا کہ مرحومہ کی قبر کھودی جا رہی ہے اور وہ پیشانی پر ہاتھ رکھے پاس ہی بیٹھے ہیں۔ اس وقت وہ بہت بوڑھے معلوم ہو رہے تھے۔ کمر جھکی ہوئی تھی اور چہرہ زرد۔ اس واقعے کے بعد ان کی صحت برابر بگڑتی چلی گئی۔ آخر ۲۱/اپریل ۱۹۳۸ء کو انتقال کیا اور شاہی مسجد کے باہر دفن ہوئے۔',
     'له مرګ نه شاوخوا دوه نیم کاله مخکې هغه د مېو روډ پر خپله نوې جوړه کوټۍ کې کډه شو. هلته لا څو ورځې تېرې شوې وې چې د هغه بېګم صاحبه وفات شوه. هغه ته د دې پېښې ډېر صدمه ورسېده. ما هغه په داسې حال کې ولید چې د مرحومې قبر کیندل کېده او هغه لاس پر تندي ایښی تر څنګ ناست و. په هغه وخت کې ډېر زوړ ښکارېده — ملا یې کږه وه او مخ یې زېړ. له دې پېښې وروسته یې روغتیا پرله‌پسې خرابېده. په پای کې د ۱۹۳۸ز د اپرېل په ۲۱مه وفات شو او د شاهي جومات بهر خاورو ته وسپارل شو.'),
    ('(Mardum Deeda)', '(مردم دیدہ)', '(مردم دیده)'),
]: t.p(*x)
tx = BOOK.record(t, 'urdu12-u14-text-5', 'Lesson text (5)', 'متنِ سبق (۵)', 'د لوست متن (۵)', 76, [142])

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Write short answers.', '۱۔ مختصر جوابات لکھیں۔', '۱. لنډ ځوابونه ولیکئ.')
e.group('lines', [
    ("(a) Describe the gatherings held at Allama Iqbal's house.", '(الف) علامہ اقبالؒ کے گھر ہونے والی محفلوں کا حال لکھیں۔', '(الف) د علامه اقبال په کور کې د کېدونکو محفلونو حال ولیکئ.'),
    ('(b) What is the attitude of the poets of U.P. in the matter of hearing and reciting verse?', '(ب) شعر سننے اور سنانے کے معاملے میں یو۔پی کے شعرا کا کیا طرزِ عمل ہے؟', '(ب) د شعر اورېدو او اورولو په چاره کې د یو.پي د شاعرانو چلند څه دی؟'),
    ('(c) Who was Sir Shahabuddin?', '(ج) سر شہاب الدین کون تھے؟', '(ج) سر شهاب‌الدین څوک و؟'),
    ("(d) Write the names of Allama Iqbal's friends who are mentioned in this sketch.", '(د) علامہ اقبالؒ کے اُن دوست احباب کے نام لکھیں، جن کا ذکر اس خاکے میں ہے۔', '(د) د علامه اقبال د هغو ملګرو نومونه ولیکئ چې په دې خاکه کې یې یادونه شوې.'),
    ('(e) “I am thinking that the young men of the college too should be seated in purdah.” Why did Allama Iqbal say this sentence?', '(ہ) ’’میں اس فکر میں ہوں کہ کالج کے نوجوانوں کو بھی پردے میں بٹھا دیا جائے‘‘ علامہ اقبالؒ نے یہ جملہ کیوں کہا؟', '(ه) "زه په دې فکر کې یم چې د کالج ځوانان هم په پرده کې کېنول شي" — علامه اقبال دا جمله ولې وویله؟'),
])
e.p("2. Write a detailed note on the aspects of Allama Iqbal's life that have been highlighted in this essay.", '۲۔ اس مضمون میں علامہ اقبالؒ کی زندگی کے جن پہلوؤں پر روشنی ڈالی گئی ہے، اُن پر ایک تفصیلی نوٹ لکھیں۔', '۲. په دې مقاله کې د علامه اقبال د ژوند پر کومو اړخونو رڼا اچول شوې، پر هغو یو مفصل یادښت ولیکئ.')
e.p('3. Fill in the blanks:', '۳۔ خالی جگہ پُر کریں:', '۳. تش ځایونه ډک کړئ:')
e.group('lines', [
    ('(a) In those days the salt ________ was at its height.', '(الف) اُن دنوں نمک کی ________ زوروں پر تھی۔', '(الف) په هغو ورځو کې د مالګې ________ په اوج کې وه.'),
    ('(b) The subject was dry, but now and then ________ also happened.', '(ب) موضوع روکھا پھیکا تھا مگر بیچ بیچ میں ________ بھی ہو جاتے تھے۔', '(ب) موضوع وچ و، خو منځ منځ کې ________ هم کېدې.'),
    ('(c) In winter he had ________ cooked with great relish.', '(ج) وہ جاڑے میں بڑے شوق سے ________ پکواتے تھے۔', '(ج) هغه به په ژمي کې په ډېر شوق ________ پخاوه.'),
    ('(d) Allama Iqbal generally spoke ________ .', '(د) علامہ اقبالؒ عام طور پر ________ بولتے تھے۔', '(د) علامه اقبال به عموماً ________ ویله.'),
    ('(e) According to Allama Iqbal, mushairas ________ poetry.', '(ہ) علامہ اقبالؒ کے مطابق مشاعروں نے شاعری کو ________ کر ڈالا۔', '(ه) د علامه اقبال په وینا مشاعرو شاعري ________ کړه.'),
])
e.p('4. Write an essay of at least five hundred words on the title “My Teachers”. Keep idiomatic usage (rozmarra) in mind and use idioms (muhāwarāt).*', '۴۔ آپ ’’میرے اساتذہ‘‘ کے عنوان پر کم از کم پانچ سو الفاظ کا مضمون تحریر کریں۔ روزمرہ کا خیال رکھیں اور محاورات استعمال کریں۔*', '۴. د "زما استادان" تر سرلیک لاندې لږ تر لږه پنځه سوه کلمې مقاله ولیکئ. روزمره ته پام وکړئ او محاورې وکاروئ.*')
ex = BOOK.record(e, 'urdu12-u14-exercise', 'Exercise', 'مشق', 'تمرین', 76, [142, 143])
ex['sourceCoverIllustrationReview'] = 'Faint background drawing of a chair/desk behind the exercise is decorative; not reproduced.'

g = Builder()
g.h('Idiom (muhāwara) and everyday usage (rozmarra)', '* محاورہ اور روزمرہ', '* محاوره او روزمره')
g.p('When two or more words are used in a figurative rather than literal sense, it is called an idiom (muhāwara) — for example, “āṅkheṅ dikhānā” (to glare at), “āṅkhoṅ se girānā” (to lower in esteem), “nau do gyārah honā” (to vanish, take to one’s heels), “tāre ginnā” (to pass a sleepless night), etc. Rozmarra is the name for the everyday speech of native speakers. In rozmarra words are used in their literal meanings. An idiom comes within the bounds of grammar whereas rozmarra is above grammar. Likewise an idiom does not change, whereas rozmarra keeps changing according to native speakers.',
    'جب دو یا دو سے زیادہ الفاظ حقیقی معنوں کے بجائے مجازی معنوں میں استعمال ہوں تو وہ محاورہ کہلاتا ہے۔ مثلاً آنکھیں دِکھانا، آنکھوں سے گرانا، نو دو گیارہ ہونا، تارے گننا وغیرہ۔ روزمرہ اہلِ زبان کے بول چال کا نام ہے۔ روزمرہ میں الفاظ اپنے حقیقی معنوں میں استعمال ہوتے ہیں۔ محاورہ قواعد کی حدود میں آتا ہے جب کہ روزمرہ قواعد سے بالاتر ہوتا ہے۔ اسی طرح محاورے میں تبدیلی نہیں ہوتی جب کہ روزمرہ اہلِ زبان کے مطابق تبدیل ہوتا رہتا ہے۔',
    'کله چې دوه یا له دوو ډېرې کلمې د حقیقي مانا پر ځای په مجازي مانا وکارول شي، محاوره بلل کېږي — لکه "سترګې ښودل" (ګواښل)، "له سترګو غورځول" (بې‌قدره کول)، "نهه دوه یوولس کېدل" (تښتېدل)، "ستوري شمېرل" (بې‌خوبه شپه تېرول) او نور. روزمره د اهل زبان د ورځنیو خبرو نوم دی. په روزمره کې کلمې په خپلو حقیقي ماناوو کارېږي. محاوره د قواعدو په پوله کې راځي، خو روزمره له قواعدو پورته وي. همداراز په محاوره کې بدلون نه راځي، خو روزمره د اهل زبان سره سم بدلېږي.')
gr = BOOK.record(g, 'urdu12-u14-grammar', 'Grammar note: idiom and everyday usage', 'محاورہ اور روزمرہ', 'محاوره او روزمره', 76, [143])

issues = [{'id': 'urdu12-pdf076', 'unit': 14, 'printedPage': 143, 'description': 'Owner handwriting excluded: pencilled answers in the Q3 blanks (ستیاگرہ، لطیفے، شب دیگ، پنجابی، غارت) and a diagonal handwritten note with signature at the bottom of p.143. Blanks are kept empty as printed.'}]

if __name__ == '__main__':
    BOOK.save(76, [(14, tx), (14, ex), (14, gr)], issues=issues, complete_units=[14])
