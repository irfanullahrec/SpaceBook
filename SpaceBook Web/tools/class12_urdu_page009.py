"""Urdu XII PDF9 (spread): printed pp.8–9 — Lesson 1 مشق Q2–Q5 with رموزِ اوقاف: رابطہ (:) and تفصیلیہ (:-). Completes Lesson 1."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
e = Builder()
e.p('2. Fill in the blanks.', '۲۔ خالی جگہ پُر کریں۔', '۲. تش ځایونه ډک کړئ.')
e.group('lines', [
    ('(a) The sciences were those which were mostly connected with ________ .', '(الف) علوم وہ تھے جن کو ________ سے زیادہ تر تعلق تھا۔', '(الف) علوم هغه وو چې ډېری یې له ________ سره اړه درلوده.'),
    ('(b) Because of religious ________ there was no sympathy with philosophy and logic', '(ب) مذہبی ________ کی وجہ سے فلسفہ اور منطق سے ہمدردی نہ تھی', '(ب) د مذهبي ________ له امله له فلسفې او منطق سره همدردي نه وه'),
    ('(c) ________ was ruling up to the banks of the river Indus.', '(ج) دریائے سندھ کے کنارے تک ________ حکومت کر رہا تھا۔', '(ج) د سند سیند تر غاړې پورې ________ حکومت کاوه.'),
    ('(d) Taking part in assemblies of debate was necessary for ________ .', '(د) مناظرہ کی مجلسوں میں شرکت ________ کے لیے ضروری تھا۔', '(د) د مناظرې په مجلسونو کې ګډون د ________ لپاره اړین و.'),
    ('(e) The third period laid the foundation of ________ education.', '(ہ) تیسرے دور نے ________ تعلیم کی بنیاد ڈالی۔', '(ه) درېیمې دورې د ________ زده کړې بنسټ کېښود.'),
])
e.p('3. Put diacritics (iʿrāb) on the following words and write their meanings.', '۳۔ درج ذیل الفاظ پر اعراب لگائیں اور معنی لکھیں۔', '۳. پر لاندې کلمو اعراب (زېر زبر) کېږدئ او ماناوې یې ولیکئ.')
w = 'معمور، دفعتاً، عجمی، غارت گری، مجتہدین،'
e.p('maʿmūr, dafʿatan, ʿajamī, ghārat-garī, mujtahidīn [Urdu words to be vowelled]', w, 'معمور، دفعتاً، عجمي، غارتګري، مجتهدین [د اردو کلمې چې اعراب پرې کېښودل شي]')
e.p('4. Write a detailed essay on the merits and demerits of the present educational and examination system.', '۴۔ موجودہ تعلیمی اور امتحانی نظام کے حُسن و قبح پر ایک مفصّل مضمون لکھیں۔', '۴. د اوسني تعلیمي او ازموینیز نظام د ښېګڼو او نیمګړتیاوو په اړه یوه مفصله مقاله ولیکئ.')
e.h('Punctuation marks (Rumūz-e-Awqāf):', 'رُموزِ اوقاف:', 'د تکي‌ایښودنې نښې (رموزِ اوقاف):')
e.p('Ramz means a hint or sign; rumūz is its plural, while waqf means a thing set apart. In the terminology of grammar, “rumūz-e-awqāf” are those signs “which separate two words, two phrases or two sentences from each other”. Special signs are placed in writing for a pause or stop so that the meaning becomes clear and no confusion arises in the writing. Using these signs helps the reader to understand and read the passage. If these signs are not present in writing, the whole passage becomes merely a collection of continuous words.',
    'رَمز ایما و اشارہ کو کہتے ہیں، رُموز اس کی جمع ہے جب کہ وقف کے معنی الگ کی ہوئی چیز کے ہیں۔ ’’گرامر / قواعد کی اصطلاح میں اُن علامتوں کو ’’رموزِ اوقاف‘‘ کہتے ہیں جو دو لفظوں، دو فقروں یا جملوں کو ایک دوسرے سے علیحدہ کریں‘‘۔ تحریر میں وقفہ یا ٹھہراؤ کے لیے مخصوص علامات لگائی جاتی ہیں تا کہ مطلب واضح ہو سکے اور تحریر میں اُلجھاؤ پیدا نہ ہو، اِن علامات کے استعمال سے قاری کو عبارت سمجھنے اور پڑھنے میں مدد ملتی ہے۔ تحریر میں یہ علامتیں موجود نہ ہوں تو پوری عبارت صرف مسلسل الفاظ کا مجموعہ بن کر رہ جاتی ہے۔',
    'رمز اشارې او کنایې ته وايي، رموز یې جمع ده، او وقف د جلا شوي شي په مانا دی. "د ګرامر / قواعدو په اصطلاح کې هغو نښو ته "رموزِ اوقاف" وايي چې دوه کلمې، دوه عبارتونه یا جملې له یو بل څخه جلا کوي". په لیکنه کې د وقفې یا درېدو لپاره ځانګړې نښې ایښودل کېږي ترڅو مطلب روښانه شي او په لیکنه کې ګډوډي پیدا نه شي؛ د دې نښو کارول لوستونکي سره د متن په پوهېدو او لوستلو کې مرسته کوي. که دا نښې په لیکنه کې نه وي، ټول متن یوازې د پرلپسې کلمو یوه ټولګه پاتې کېږي.')
e.p('These signs have been included, with definitions, in the various exercises.', 'اِن علامات کو مختلف مشقوں میں مع تعریف شامل کیا گیا ہے۔', 'دا نښې په بېلابېلو تمرینونو کې له تعریف سره شاملې شوې دي.')
e.h('Colon (rābiṭa): ( : )', 'رابطہ: ( : )', 'رابطه (کولن): ( : )')
e.group('list', [
    ('It is used where a previous statement or idea of the sentence needs explanation or confirmation.', 'اس کا استعمال وہاں ہوتا ہے جہاں جملے کی کسی سابق بات یا خیال کی تشریح یا تصدیق کی ضرورت ہو۔', 'دا هلته کارېږي چې د جملې د کومې مخکینۍ خبرې یا فکر تشریح یا تصدیق ته اړتیا وي.'),
])
e.p('As the poet says: ʿ — A man ought to be a man of character.', 'بقولِ شاعر: ع آدمی کو صاحبِ کردار ہونا چاہیے', 'لکه شاعر چې وايي: ع — انسان باید د کردار خاوند وي.')
e.group('list', [('This sign comes after stating a short saying or proverb, or after an introductory sentence.', 'کسی مختصر مقولے یا کہاوت کو بیان کرنا ہو یا تمہیدی جملے کے بعد یہ علامت آتی ہے۔', 'کله چې یو لنډ متل یا قول بیانول وي، یا له سریزه‌ییزې جملې وروسته، دا نښه راځي.')])
e.p('How well Salik Sahib has said: Health is a thousand blessings.', 'سالک صاحب نے کیا خوب کہا ہے: تندرستی ہزار نعمت ہے۔', 'سالک صاحب څومره ښه ویلي: روغتیا زر نعمتونه دي.')
e.group('list', [('Between two such sentences which are opposites of each other but together complete the sentence. For example:-', 'دو ایسے جملوں کے درمیان جو ایک دوسرے کی ضد ہوں لیکن دونوں مل کر جملہ پورا کریں۔ مثلاً:-', 'د داسې دوو جملو ترمنځ چې د یو بل ضد وي خو دواړه یوځای جمله بشپړه کړي. د بېلګې په توګه:-')])
e.p('Man can walk: he cannot fly', 'انسان چل سکتا ہے: اُڑ نہیں سکتا', 'انسان ګرځېدلی شي: الوتلی نه شي')
e.h('Colon-dash (tafṣīliya): ( :- )', 'تفصیلیہ: ( :- )', 'تفصیلیه: ( :- )')
e.p('This word is derived from tafṣīl (detail), which means to explain or to list. This sign is placed where an example, a list or some detail is to be given. For example:-', 'یہ لفظ تفصیل سے نکلا ہے۔ جس کے معنی، تشریح کرنا یا فہرست کے ہیں۔ یہ علامت وہاں لگائی جاتی ہے جہاں مثال، فہرست یا کوئی تفصیل بیان کرنی ہو مثلاً:-', 'دا کلمه له "تفصیل" څخه اخیستل شوې چې مانا یې تشریح کول یا فهرست دی. دا نښه هلته ایښودل کېږي چې بېلګه، فهرست یا کوم تفصیل بیانول وي. د بېلګې په توګه:-')
e.group('list', [('The details of the books bought for the library are as follows:-', 'لائبریری کے لیے خریدی گئی کتابوں کی تفصیل یہ ہے:-', 'د کتابتون لپاره د پېرل شویو کتابونو تفصیل دا دی:-')])
e.p('Diwan-e-Ghalib, Kulliyat-e-Iqbal, Nuskha-ha-e-Wafa, Aab-e-Gum', 'دیوانِ غالب، کلیاتِ اقبال، نسخہ ہائے وفا، آبِ گم', 'دیوانِ غالب، کلیاتِ اقبال، نسخه‌های وفا، آبِ ګم')
e.group('list', [('When an example is to be given in a passage. For example:-', 'کسی عبارت میں مثال پیش کی جائے۔ مثلاً:-', 'کله چې په یوه متن کې بېلګه وړاندې کېږي. د بېلګې په توګه:-')])
e.p('Compounds formed with the genitive particles [blank as printed] are called genitive compounds (murakkabāt-e-iḍāfī). For example:- Khalid’s house, a workshop of vehicles, etc.', 'حروفِ اضافی [ ] سے ملنے والے مرکبات کو مرکباتِ اضافی کہتے ہیں۔ مثلاً:- خالد کا گھر، گاڑیوں کا ورکشاپ وغیرہ', 'هغه مرکبات چې د اضافت له تورو [ ] سره جوړېږي، اضافي مرکبات بلل کېږي. د بېلګې په توګه:- د خالد کور، د موټرو ورکشاپ او نور')
e.group('list', [('When a detail is to be written in a passage, the colon-dash is also used, as:-', 'جب کسی عبارت میں تفصیل لکھنی ہو تو بھی تفصیلیہ لگاتے ہیں جیسے:-', 'کله چې په یوه متن کې تفصیل لیکل کېږي، بیا هم تفصیلیه کارول کېږي، لکه:-')])
e.p('Just listen to my account:- I left home at exactly nine o’clock and stood at the bus stop……', 'ذرا میری روداد سنو:- میں ٹھیک نو بجے گھر سے نکلا، بس سٹاپ پر کھڑا ہوا……', 'زما کیسه واورئ:- زه دقیق نهه بجې له کوره ووتم، د بس په تمځای ودرېدم……')
e.p('5. Using the above signs, give two examples of each sign.', '۵۔ درج بالا علامات کو استعمال کرتے ہوئے ہر علامت کی دو دو مثالیں دیں۔', '۵. د پورته نښو په کارولو د هرې نښې دوه دوه بېلګې ورکړئ.')
ex = BOOK.record(e, 'urdu12-u1-exercise-2', 'Exercise (2): fill in the blanks; punctuation — colon and colon-dash', 'مشق (۲): خالی جگہ، رموزِ اوقاف — رابطہ، تفصیلیہ', 'تمرین (۲): تش ځایونه؛ رموزِ اوقاف — رابطه، تفصیلیه', 9, [8, 9])
issues = [{'id': 'urdu12-pdf009', 'unit': 1, 'printedPage': 9, 'description': 'In the تفصیلیہ example “حروفِ اضافی ___ سے ملنے والے مرکبات …” the particles (کا، کے، کی) are missing/blank in the print; shown as “[ ]”. The رموزِ اوقاف definition is printed in a shaded box. Q2(b) lacks a full stop as printed.'}]

if __name__ == '__main__':
    BOOK.save(9, [(1, ex)], issues=issues, complete_units=[1])
