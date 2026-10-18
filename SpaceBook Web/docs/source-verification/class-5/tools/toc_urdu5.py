"""Generate the Class 5 Urdu contents pages (urdu/pages/p004-p007.txt) from compact data.

    python tools/toc_urdu5.py      (run from docs/source-verification/class-5)
Each lesson card on the printed contents lists seven skill rows; the row labels repeat, so their
translations are defined once in L. Slot order is Urdu || English || Pashto (Urdu is the source language).
"""
from pathlib import Path

L = {
    'a': ('آپ نے کیا سمجھا؟', 'What did you understand?', 'څه مو پوه شول؟'),
    'b': ('مل کر کریں بات', "Let's talk together", 'راځئ یو ځای خبرې وکړو'),
    'c': ('لفظوں کا کھیل', 'Word game', 'د ټکو لوبه'),
    'd': ('قواعد سیکھیں', 'Learn grammar', 'ګرامر زده کړئ'),
    'e': ('پڑھیں', 'Read', 'ولولئ'),
    'f': ('کچھ نیا لکھیں', 'Write something new', 'یو څه نوی ولیکئ'),
    'g': ('آؤ کریں کام', "Come, let's work", 'راځئ کار وکړو'),
    's': ('سمجھیں اور بتائیں', 'Understand and tell', 'پوه شئ او ووایئ'),
}
READ = ('پڑھ کر سوالات کے زبانی جواب دینا۔', 'Reading and answering the questions orally.', 'لوستل او پوښتنو ته خولې ځوابونه ورکول.')
TALK = ('دیے ہوئے موضوع پر بات چیت کرنا', 'Talking about a given topic', 'پر ورکړل شوي موضوع خبرې کول')
QA = ('کالم مِلانا، درست جواب کی نشان دہی کرنا، سوال جواب', 'Matching columns, marking the correct answer, question-answer', 'ستنې سره سمول، سم ځواب نښه کول، پوښتنه ځواب')


def t3(x):
    return ' || '.join(x)


def lesson(n, title, page, rows):
    out = [f'table سبق {n}: {title[0]} (صفحہ {page}) || Lesson {n}: {title[1]} (page {page}) || {n} لوست: {title[2]} (مخ {page})',
           'th | مہارت || Skill || مهارت | تفصیل || Details || تفصیل']
    out += [f'tr | {t3(L[k])} | {t3(d)}' for k, d in rows]
    out.append('endtable')
    return out


P = {}
P[4] = ['@status front-matter',
        '@deco Coloured lesson cards with a lesson-number tab and a page-number oval; a term divider "دوسری سہ ماہی" and a review bar "جائزہ ۔ ۲" at the foot.',
        '# فہرست || Contents || فهرست']
P[4] += lesson(5, ('جو وعدہ کرو سو پورا کرو', 'Keep Your Promise', 'چې ژمنه کوې، پوره یې کړه'), 32, [
    ('a', ('حروف کی ترتیب درست کر کے خالی جگہ پُر کرنا، کردار شناخت کرنا، سوال جواب', 'Arranging letters correctly to fill blanks, identifying characters, question-answer', 'د توریو سم ترتیب سره تش ځایونه ډکول، کرکټرونه پېژندل، پوښتنه ځواب')),
    ('b', ('برقی میڈیا سے کہانی سُن کر ساتھیوں کو سنانا', 'Listening to a story on electronic media and telling it to classmates', 'له برېښنايي رسنیو کیسه اورېدل او ملګرو ته ویل')),
    ('c', ('حُروف الگ الگ کر کے ان حروف سے مزید الفاظ بنانا', 'Separating the letters and making more words from them', 'توري جلا کول او ترې نور ټکي جوړول')),
    ('d', ('واوین کا تصوّر، اسمِ معرفہ، اسمِ نکرہ کی شناخت', 'Concept of inverted commas; identifying proper and common nouns', 'د واوینو مفهوم؛ د خاص او عام نوم پېژندنه')),
    ('e', ('عبارت پڑھ کر سوالوں کے جواب دینا', 'Reading a passage and answering questions', 'متن لوستل او پوښتنو ته ځوابونه')),
    ('f', ('اَخلاقی کہانی لکھنا', 'Writing a moral story', 'اخلاقي کیسه لیکل')),
    ('g', ('پسندیدہ عادات، ناپسندیدہ عادات پر مبنی چارٹ بنانا', 'Making a chart of good and bad habits', 'د ښو او بدو عادتونو چارټ جوړول'))])
P[4] += lesson(6, ('قومی تہوار (برائے مطالعہ)', 'National Festivals (for reading)', 'ملي جشنونه (د لوستلو لپاره)'), 40, [('s', READ)])
P[4] += ['p دوسری سہ ماہی || Second term || دویمه درې میاشتنۍ']
P[4] += lesson(7, ('ہوا چلی (نظم)', 'The Wind Blew (poem)', 'باد ولګېد (نظم)'), 42, [
    ('a', ('مصرعوں کی تکمیل، حروف جوڑ کر الفاظ بنانا، ان سے متعلقہ مصرعے تلاش کرنا، سوال جواب', 'Completing lines, joining letters into words, finding the related lines, question-answer', 'د مصرعو بشپړول، توري یو ځای کول او ټکي جوړول، اړوندې مصرعې موندل، پوښتنه ځواب')),
    ('b', TALK),
    ('c', ('گروہی الفاظ کا تصوّر', 'Concept of group words', 'د ډله ییزو ټکو مفهوم')),
    ('d', ('سابقے، لاحقے کا تصوّر', 'Concept of prefixes and suffixes', 'د مختاړو او وروستاړو مفهوم')),
    ('e', ('اشعار پڑھ کر اُن کا مرکزی خیال بتانا', 'Reading verses and telling their central idea', 'بیتونه لوستل او مرکزي فکر یې ویل')),
    ('f', ('دیے ہوئے موضوع پر پیراگراف لکھنا', 'Writing a paragraph on a given topic', 'پر ورکړل شوي موضوع پراګراف لیکل')),
    ('g', ('انٹرنیٹ کا استعمال کرتے ہوئے معلومات اکٹھی کرنا، ساتھیوں کو بتانا', 'Collecting information using the internet and telling classmates', 'د انټرنېټ په کارولو معلومات راټولول او ملګرو ته ویل'))])
P[4] += lesson(8, ('میری پہچان ہے تُو', 'You Are My Identity', 'ته زما پېژندنه یې'), 49, [
    ('a', ('الفاظ سے متعلقہ معلومات لکھنا، درست جواب کی نشان دہی کرنا، سوال جواب', 'Writing information about words, marking the correct answer, question-answer', 'د ټکو اړوند معلومات لیکل، سم ځواب نښه کول، پوښتنه ځواب')),
    ('b', ('قومی ترانے کا مفہوم سنانا', 'Telling the meaning of the national anthem', 'د ملي ترانې مفهوم ویل')),
    ('c', ('لفظ سازی، لُغت کا استعمال', 'Word building, using a dictionary', 'ټکي جوړول، د قاموس کارول')),
    ('d', ('اِعراب کا استعمال، علامتِ فاعل اور علامتِ مفعول کا تصوّر', 'Using diacritics; concept of subject and object markers', 'د اعرابو کارول؛ د فاعل او مفعول د نښو مفهوم')),
    ('e', ('پہیلیاں پڑھنا، بُوجھنا', 'Reading and solving riddles', 'معماګانې لوستل او حلول')),
    ('f', ('درخواست لکھنا', 'Writing an application', 'غوښتنلیک لیکل')),
    ('g', ('قومی ترانے سے متعلق چارٹ تیار کرنا', 'Preparing a chart about the national anthem', 'د ملي ترانې په اړه چارټ جوړول'))])
P[4] += lesson(9, ('ہمارے پیشے', 'Our Professions', 'زموږ مسلکونه'), 58, [
    ('a', QA),
    ('b', ('تصویروں کے متعلق بات چیت کرنا', 'Talking about pictures', 'د انځورونو په اړه خبرې کول')),
    ('c', ('الفاظ سازی، الف بائی ترتیب', 'Word building, alphabetical order', 'ټکي جوړول، الفبايي ترتیب')),
    ('d', ('فعل سے فاعل بنانا، تذکیر و تانیث کو مدِنظر رکھتے ہوئے فعل کا استعمال کرنا', 'Making the doer from the verb; using verbs according to masculine and feminine', 'له فعل څخه فاعل جوړول؛ د نارینه او ښځینه له مخې د فعل کارول')),
    ('e', ('پیراگراف پڑھ کر اس کے بارے میں سوالوں کے جواب دینا', 'Reading a paragraph and answering questions about it', 'پراګراف لوستل او د هغه په اړه پوښتنو ته ځوابونه')),
    ('f', ('تصویریں دیکھ کر کہانی لکھنا', 'Writing a story by looking at pictures', 'انځورونه کتل او کیسه لیکل')),
    ('g', ('مختلف پیشوں سے وابستہ افراد کے بارے میں بات چیت کرنا', 'Talking about people in different professions', 'د بېلابېلو مسلکونو د خلکو په اړه خبرې کول'))])
P[4] += ['p جائزہ ۔ ۲ || Review 2 || ارزونه ۲',
         '@issue The contents for lessons 1–4 (and review 1) are missing from the scans: JPG 003 is the title page and JPG 004 begins with lesson 5. Lesson 6 is marked "for reading" and has only one skill line.']

P[5] = ['@status front-matter', '@deco Coloured lesson cards; a review bar "جائزہ ۔ ۳" at the foot.']
P[5] += lesson(10, ('ایک گائے اور بکری (نظم)', 'A Cow and a Goat (poem)', 'یوه غوا او یوه وزه (نظم)'), 69, [
    ('a', QA),
    ('b', ('کرداروں کے بارے میں بات چیت کرنا', 'Talking about the characters', 'د کرکټرونو په اړه خبرې کول')),
    ('c', ('حُروف کی ترتیب درست کر کے الفاظ بنانا اور ان کے بارے میں لکھنا', 'Arranging letters into words and writing about them', 'د توریو سم ترتیب سره ټکي جوړول او د هغو په اړه لیکل')),
    ('d', ('واحد جمع کا استعمال کرنا، خالی جگہ پُر کرنا، غلط فقرات کی درستی کرنا', 'Using singular and plural, filling blanks, correcting wrong sentences', 'د مفرد او جمع کارول، تش ځایونه ډکول، ناسمې جملې سمول')),
    ('e', ('اشعار پڑھ کر اُن کے بارے میں بتانا', 'Reading verses and telling about them', 'بیتونه لوستل او د هغو په اړه ویل')),
    ('f', ('شعر کا مفہوم لکھنا', 'Writing the meaning of a verse', 'د بیت مفهوم لیکل')),
    ('g', ('نظم کو کرداری مکالمے کی صورت میں پیش کرنا', 'Presenting the poem as a dialogue of characters', 'نظم د کرکټرونو د مکالمې په بڼه وړاندې کول'))])
P[5] += lesson(11, ('حضرت عثمان غنی رضی اللہ تعالیٰ عنہ', 'Hazrat Usman Ghani (RA)', 'حضرت عثمان غني رضي الله تعالی عنه'), 76, [
    ('a', ('خالی جگہ پُر کرنا، درست جواب کا انتخاب کرنا، سوال جواب', 'Filling blanks, choosing the correct answer, question-answer', 'تش ځایونه ډکول، سم ځواب ټاکل، پوښتنه ځواب')),
    ('b', ('واقعہ سنانا، اظہارِ خیال کرنا', 'Narrating an incident, expressing views', 'پېښه ویل، نظر څرګندول')),
    ('c', ('اِعراب لگانا، لُغت کا استعمال، جملے بنانا', 'Adding diacritics, using a dictionary, making sentences', 'اعراب لګول، قاموس کارول، جملې جوړول')),
    ('d', ('فعل ماضی، حال اور مستقبل کے جملوں کی شناخت اور تبدیلی؛ الفاظ متضاد کا تصوّر، خالی جگہ پُر کرنا', 'Identifying and changing past, present and future sentences; concept of opposites, filling blanks', 'د تېر، اوسني او راتلونکي جملو پېژندل او بدلول؛ د متضادو ټکو مفهوم، تش ځایونه ډکول')),
    ('e', ('عبارت پڑھ کر خلاصہ سنانا', 'Reading a passage and telling its summary', 'متن لوستل او لنډیز یې ویل')),
    ('f', ('خط لکھنا، عددی ترتیب کا تصوّر', 'Writing a letter; concept of numerical order', 'لیک لیکل؛ د شمېري ترتیب مفهوم')),
    ('g', ('معاشرتی مسئلے کی نشان دہی کرنا، اس کا حل تجویز کرنا، گتے کے ڈبے سے غلّک بنانا', 'Identifying a social problem and suggesting a solution; making a money box from a cardboard box', 'ټولنیزه ستونزه پېژندل او حل یې وړاندیز کول؛ له کارتني بکس څخه غلک جوړول'))])
P[5] += lesson(12, ('دنیا آپ کی مٹھی میں', 'The World in Your Fist', 'نړۍ ستاسو په موټي کې'), 84, [
    ('a', ('خالی جگہ پُر کرنا، غلط درست جواب کی نشان دہی کرنا، سوال جواب', 'Filling blanks, marking right and wrong answers, question-answer', 'تش ځایونه ډکول، سم او ناسم ځواب نښه کول، پوښتنه ځواب')),
    ('b', ('انٹرنیٹ کے فائدے اور نقصانات پر بات چیت کرنا', 'Talking about the benefits and harms of the internet', 'د انټرنېټ د ګټو او زیانونو په اړه خبرې کول')),
    ('c', ('الفاظ کے حروف الگ کرنا اور آخری حرف سے کوئی خوبی لکھنا', 'Separating the letters of words and writing a good quality from the last letter', 'د ټکو توري جلا کول او له وروستي توري یوه ښېګڼه لیکل')),
    ('d', ('ماضی شکیہ، تمنّائی اور شرطیہ کا تصوّر', 'Concept of the doubtful, wishing and conditional past tenses', 'د شکي، تمنايي او شرطي تېر مهال مفهوم')),
    ('e', ('عبارت پڑھ کر سوالوں کے جواب دینا', 'Reading a passage and answering questions', 'متن لوستل او پوښتنو ته ځوابونه')),
    ('f', ('کسی ذریعۂ ابلاغ کے بارے میں معلومات لکھنا، اُردو زبان میں ای میل لکھنا', 'Writing information about a means of communication; writing an e-mail in Urdu', 'د یوې رسنۍ په اړه معلومات لیکل؛ په اردو ژبه برېښنالیک لیکل')),
    ('g', ('اُردو کی بورڈ کا چارٹ بنانا', 'Making a chart of the Urdu keyboard', 'د اردو کیبورډ چارټ جوړول'))])
P[5] += lesson(13, ('ہم پھول اک چمن کے (نظم)', 'We Are Flowers of One Garden (poem)', 'موږ د یوه چمن ګلان یو (نظم)'), 91, [
    ('a', ('مصرعوں کی تکمیل کرنا، الفاظ کی ترتیب درست کر کے مصرعے لکھنا، سوال جواب', 'Completing lines, writing lines by arranging the words correctly, question-answer', 'مصرعې بشپړول، د ټکو سم ترتیب سره مصرعې لیکل، پوښتنه ځواب')),
    ('b', ('اپنا پسندیدہ شعر سنانا، دیے ہوئے موضوع پر تجاویز دینا', 'Reciting a favourite verse, giving suggestions on a given topic', 'خپل غوره بیت ویل، پر ورکړل شوي موضوع وړاندیزونه ورکول')),
    ('c', ('حروف کی ترتیب درست کر کے الفاظ بنانا، ہم آواز الفاظ کا تصوّر', 'Making words by arranging letters; concept of words that sound alike', 'د توریو سم ترتیب سره ټکي جوړول؛ د ورته غږیزو ټکو مفهوم')),
    ('d', ('قوسین کا تصوّر', 'Concept of brackets', 'د قوسونو مفهوم')),
    ('e', ('اشعار پڑھ کر سوالوں کے جواب دینا', 'Reading verses and answering questions', 'بیتونه لوستل او پوښتنو ته ځوابونه')),
    ('f', ('محاورات کا جملوں میں استعمال کرنا، ہندسی گنتی کو عددی ترتیب میں بدل کر خالی جگہ پُر کرنا', 'Using idioms in sentences; filling blanks by changing figures into number words', 'په جملو کې اصطلاحات کارول؛ هندسي شمېرنه په شمېري ترتیب بدلول او تش ځایونه ډکول')),
    ('g', ('دعوت نامہ تیار کرنا', 'Preparing an invitation card', 'بلنلیک جوړول'))])
P[5] += lesson(14, ('آؤ بچو! سنو کہانی (برائے مطالعہ)', 'Come Children, Hear a Story (for reading)', 'راشئ ماشومانو! کیسه واورئ (د لوستلو لپاره)'), 98, [('s', READ)])
P[5] += ['p جائزہ ۔ ۳ || Review 3 || ارزونه ۳']

P[6] = ['@status front-matter', '@deco Coloured lesson cards; a term divider "تیسری سہ ماہی" and a review bar "جائزہ ۔ ۴" with a flower border at the foot.']
P[6] += lesson(15, ('آئیں! مدد کریں', 'Come! Let Us Help', 'راځئ! مرسته وکړو'), 102, [
    ('a', ('خالی جگہ پُر کرنا، غلط اور درست بیان کی نشان دہی کرنا، سوال جواب', 'Filling blanks, marking true and false statements, question-answer', 'تش ځایونه ډکول، سمې او ناسمې وینا نښه کول، پوښتنه ځواب')),
    ('b', TALK),
    ('c', ('متشابہ الفاظ کا تصوّر', 'Concept of similar-looking words', 'د ورته ښکارېدونکو ټکو مفهوم')),
    ('d', ('حروفِ ندا، تاسّف اور استعجاب کا تصوّر اور استعمال', 'Concept and use of words of calling, regret and surprise', 'د ندا، افسوس او حیرانتیا د توریو مفهوم او کارونه')),
    ('e', ('پیراگراف پڑھ کر سوالوں کے جواب دینا', 'Reading a paragraph and answering questions', 'پراګراف لوستل او پوښتنو ته ځوابونه')),
    ('f', ('خط لکھنا، مضمون لکھنا', 'Writing a letter, writing an essay', 'لیک لیکل، مقاله لیکل')),
    ('g', ('چارٹ بنانا', 'Making a chart', 'چارټ جوړول'))])
P[6] += lesson(16, ('رکھیں میرا خیال', 'Take Care of Me', 'زما خیال وساتئ'), 109, [
    ('a', ('دُرست، کالم مِلانا، سوال جواب', 'Correct answers, matching columns, question-answer', 'سم ځوابونه، ستنې سره سمول، پوښتنه ځواب')),
    ('b', TALK),
    ('c', ('مختلف الفاظ اور ان کا استعمال', 'Different words and their use', 'بېلابېل ټکي او کارونه یې')),
    ('d', ('اِستفہامیہ کا تصوّر اور جملوں میں استعمال، حُروفِ عطف کا تصوّر اور استعمال', 'Concept of question words and their use in sentences; concept and use of conjunctions', 'د پوښتنیزو ټکو مفهوم او په جملو کې کارونه؛ د عطف توریو مفهوم او کارونه')),
    ('e', ('عبارت پڑھ کر اس کا مفہوم بتانا', 'Reading a passage and telling its meaning', 'متن لوستل او مفهوم یې ویل')),
    ('f', ('تصویروں کی مدد سے کہانی لکھنا', 'Writing a story with the help of pictures', 'د انځورونو په مرسته کیسه لیکل')),
    ('g', ('کُوڑے دان، گُل دان بنانا، تقریر کرنا، چارٹ بنانا', 'Making a dustbin and a flower vase, giving a speech, making a chart', 'د کثافاتو لوښی او ګلدان جوړول، وینا کول، چارټ جوړول'))])
P[6] += lesson(17, ('نیک بنو، نیکی پھیلاؤ (نظم)', 'Be Good, Spread Goodness (poem)', 'نېک شئ، نېکي خپره کړئ (نظم)'), 116, [
    ('a', ('حروف کی ترتیب درست کر کے الفاظ بنانا اور اُن سے متعلقہ مصرعے لکھنا، کالم مِلانا، سوال جواب', 'Making words by arranging letters and writing the related lines, matching columns, question-answer', 'د توریو سم ترتیب سره ټکي جوړول او اړوندې مصرعې لیکل، ستنې سره سمول، پوښتنه ځواب')),
    ('b', TALK),
    ('c', ('مرکّب الفاظ کا تصوّر', 'Concept of compound words', 'د مرکبو ټکو مفهوم')),
    ('d', ('جملوں کی زمانے کے لحاظ سے تبدیلی، علامتِ فاعل اور علامتِ مفعول کا استعمال', 'Changing sentences by tense; using subject and object markers', 'د مهال له مخې د جملو بدلول؛ د فاعل او مفعول د نښو کارونه')),
    ('e', ('نظم پڑھ کر مرکزی خیال سنانا', 'Reading the poem and telling its central idea', 'نظم لوستل او مرکزي فکر یې ویل')),
    ('f', ('نثر بنانا، دیے ہوئے موضوع پر دس جملے لکھنا', 'Turning verse into prose, writing ten sentences on a given topic', 'نظم په نثر اړول، پر ورکړل شوي موضوع لس جملې لیکل')),
    ('g', ('فہرست بنانا، داخلہ فارم پُر کرنا', 'Making a list, filling in an admission form', 'لېست جوړول، د داخلې فورمه ډکول'))])
P[6] += ['p تیسری سہ ماہی || Third term || درېیمه درې میاشتنۍ']
P[6] += lesson(18, ('ایک قدیم شہر', 'An Ancient City', 'یو لرغونی ښار'), 122, [
    ('a', ('خالی جگہ پُر کرنا، غلط درست بیان کی نشان دہی کرنا، سوال جواب', 'Filling blanks, marking true and false statements, question-answer', 'تش ځایونه ډکول، سمې او ناسمې وینا نښه کول، پوښتنه ځواب')),
    ('b', TALK),
    ('c', ('لُغت کا استعمال کرنا، الف بائی ترتیب سے الفاظ لکھنا', 'Using a dictionary, writing words in alphabetical order', 'قاموس کارول، په الفبايي ترتیب ټکي لیکل')),
    ('d', ('غلط جملوں کی درستی کرنا، الفاظ متضاد کا تصوّر', 'Correcting wrong sentences; concept of opposites', 'ناسمې جملې سمول؛ د متضادو ټکو مفهوم')),
    ('e', ('عبارت پڑھ کر اس کے بارے میں سوالوں کے جواب دینا', 'Reading a passage and answering questions about it', 'متن لوستل او د هغه په اړه پوښتنو ته ځوابونه')),
    ('f', ('محاورات کا جملوں میں استعمال کرنا، مضمون لکھنا', 'Using idioms in sentences, writing an essay', 'په جملو کې اصطلاحات کارول، مقاله لیکل')),
    ('g', ('مختلف صوبائی عمارات سے متعلق کتابچہ تیار کرنا', 'Preparing a booklet about different provincial buildings', 'د بېلابېلو ولایتي ودانیو په اړه کتابګوټی جوړول'))])
P[6] += lesson(19, ('حُسنِ سلوک', 'Good Conduct', 'ښه چلند'), 129, [
    ('a', ('معمّے میں سے الفاظ تلاش کر کے متعلقہ جملے لکھنا، درست جواب کی نشان دہی کرنا، سوال جواب', 'Finding words in a puzzle and writing related sentences, marking the correct answer, question-answer', 'له معما څخه ټکي موندل او اړوندې جملې لیکل، سم ځواب نښه کول، پوښتنه ځواب')),
    ('b', ('سبق پر اظہارِ خیال کرنا، کرداروں کے متعلق رائے دینا', 'Expressing views on the lesson, giving opinions about the characters', 'پر لوست نظر څرګندول، د کرکټرونو په اړه رایه ورکول')),
    ('c', ('مرکّب الفاظ کا تصوّر، جملہ سازی', 'Concept of compound words, making sentences', 'د مرکبو ټکو مفهوم، جملې جوړول')),
    ('d', ('اِعراب کو مدِنظر رکھتے ہوئے درست معانی کی شناخت کرنا، کالم مِلانا، حروفِ شرط و جزا کا تصوّر اور استعمال', 'Identifying correct meanings by the diacritics, matching columns; concept and use of if-then words', 'د اعرابو له مخې سمې ماناوې پېژندل، ستنې سره سمول؛ د شرط او جزا د توریو مفهوم او کارونه')),
    ('e', ('عبارت پڑھ کر اپنے الفاظ میں بتانا', 'Reading a passage and telling it in your own words', 'متن لوستل او په خپلو ټکو یې ویل')),
    ('f', ('مختصر کہانی لکھنا، دیے ہوئے موضوع پر پیراگراف لکھنا', 'Writing a short story, writing a paragraph on a given topic', 'لنډه کیسه لیکل، پر ورکړل شوي موضوع پراګراف لیکل')),
    ('g', ('تہنیتی کارڈ بنانا', 'Making a greeting card', 'د مبارکۍ کارت جوړول'))])
P[6] += ['p جائزہ ۔ ۴ || Review 4 || ارزونه ۴']

P[7] = ['@status front-matter', '@deco Coloured lesson cards; a review bar "جائزہ ۔ ۵" and a flower border at the foot.']
P[7] += lesson(20, ('کہا اقبال رحمۃ اللہ علیہ نے (نظم)', 'Iqbal Said (poem)', 'اقبال رحمة الله علیه وویل (نظم)'), 138, [
    ('a', ('مصرعوں کی تکمیل، حروف کی ترتیب درست کر کے لفظ بنانا اور اس سے متعلقہ مصرع لکھنا، سوال جواب', 'Completing lines, making a word by arranging letters and writing the related line, question-answer', 'مصرعې بشپړول، د توریو سم ترتیب سره ټکی جوړول او اړونده مصرعه لیکل، پوښتنه ځواب')),
    ('b', ('نظم پر بات چیت کرنا', 'Talking about the poem', 'د نظم په اړه خبرې کول')),
    ('c', ('اشاروں کی مدد سے شخصیت کا نام بُوجھنا', 'Guessing a personality from clues', 'د نښو په مرسته د شخصیت نوم موندل')),
    ('d', ('الفاظ مترادف کا تصوّر، الف بائی ترتیب، لُغت کا استعمال کرنا', 'Concept of synonyms, alphabetical order, using a dictionary', 'د مترادفو ټکو مفهوم، الفبايي ترتیب، د قاموس کارول')),
    ('e', ('اشعار پڑھ کر ان میں پوشیدہ پیغام بتانا', 'Reading verses and telling the hidden message in them', 'بیتونه لوستل او پټ پیغام یې ویل')),
    ('f', ('دیے ہوئے موضوع پر دس جملے لکھنا', 'Writing ten sentences on a given topic', 'پر ورکړل شوي موضوع لس جملې لیکل')),
    ('g', ('تقریر تیار کرنا، انٹرنیٹ کی مدد سے معلومات اکٹھی کرنا، گنتی یاد کرنا (۶۱ تا ۱۰۰)', 'Preparing a speech, collecting information with the internet, learning number words (61 to 100)', 'وینا چمتو کول، د انټرنېټ په مرسته معلومات راټولول، شمېرنه یادول (۶۱ تر ۱۰۰)'))])
P[7] += lesson(21, ('بے مثل ہے نظام تیرا', 'Your System Is Matchless', 'بې ساری دی ستا نظام'), 144, [
    ('a', ('حروف کو ترتیب دے کر الفاظ بنانا، خالی جگہ پُر کرنا، درست جواب کی نشان دہی کرنا، سوال جواب', 'Making words by arranging letters, filling blanks, marking the correct answer, question-answer', 'د توریو په ترتیب ټکي جوړول، تش ځایونه ډکول، سم ځواب نښه کول، پوښتنه ځواب')),
    ('b', TALK),
    ('c', ('الفاظ کے حروف الگ الگ کر کے درمیان والے حرف سے مزید الفاظ بنانا', 'Separating the letters of words and making more words from the middle letter', 'د ټکو توري جلا کول او له منځني توري نور ټکي جوړول')),
    ('d', ('واحد کی جمع اور جمع کی واحد بنانا، فاعل اور مفعول کو مدِنظر رکھتے ہوئے فعل کا استعمال کرنا', 'Making plurals of singulars and singulars of plurals; using verbs according to subject and object', 'له مفرد جمع او له جمع مفرد جوړول؛ د فاعل او مفعول له مخې د فعل کارول')),
    ('e', ('عبارت پڑھ کر مرکزی خیال بتانا', 'Reading a passage and telling its central idea', 'متن لوستل او مرکزي فکر یې ویل')),
    ('f', ('دیے ہوئے موضوع پر دو پیراگراف لکھنا', 'Writing two paragraphs on a given topic', 'پر ورکړل شوي موضوع دوه پراګرافونه لیکل')),
    ('g', ('نظامِ شمسی سے متعلق کتابچہ تیار کرنا', 'Preparing a booklet about the solar system', 'د لمریز نظام په اړه کتابګوټی جوړول'))])
P[7] += lesson(22, ('اقوالِ زریں (برائے مطالعہ)', 'Golden Sayings (for reading)', 'زرین اقوال (د لوستلو لپاره)'), 151, [('s', READ)])
P[7] += lesson(23, ('ٹوٹ بٹوٹ کے مُرغے (نظم)', "Toot Batoot's Roosters (poem)", 'د ټوټ بټوټ چرګان (نظم)'), 152, [
    ('a', ('مصرعوں کو درست ترتیب سے لکھنا، معمّے میں سے الفاظ تلاش کر کے ان سے متعلقہ مصرعے لکھنا، سوال جواب', 'Writing lines in the correct order, finding words in a puzzle and writing the related lines, question-answer', 'مصرعې په سم ترتیب لیکل، له معما ټکي موندل او اړوندې مصرعې لیکل، پوښتنه ځواب')),
    ('b', TALK),
    ('c', ('مختلف طریقوں سے الفاظ سازی کرنا', 'Making words in different ways', 'په بېلابېلو لارو ټکي جوړول')),
    ('d', ('حروفِ ندا، حروفِ استعجاب، حُروفِ افسوس، حروفِ جار کا استعمال کرتے ہوئے خالی جگہ پُر کرنا', 'Filling blanks using words of calling, surprise and regret, and prepositions', 'د ندا، حیرانتیا، افسوس او جر د توریو په کارولو تش ځایونه ډکول')),
    ('e', ('عبارت درست تلفّظ اور روانی سے پڑھنا', 'Reading a passage with correct pronunciation and fluency', 'متن په سم تلفظ او روانۍ لوستل')),
    ('f', ('مضمون لکھنا', 'Writing an essay', 'مقاله لیکل')),
    ('g', ('انٹرنیٹ کا استعمال کرنا، یومِ مزاح منانے کا اہتمام کرنا', 'Using the internet, arranging to celebrate a day of humour', 'انټرنېټ کارول، د ټوکو ورځې د لمانځلو انتظام کول'))])
P[7] += ['p جائزہ ۔ ۵ || Review 5 || ارزونه ۵']

if __name__ == '__main__':
    base = Path(__file__).resolve().parents[1] / 'urdu' / 'pages'
    for k, lines in P.items():
        (base / f'p{k:03}.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
        print(f'p{k:03}.txt', len(lines), 'lines')
