"""PDF9 (printed 5–6): Unit 1 Glossary (embodiment … vibrant); Reading Comprehension questions; Writing Suggestions — pre-writing strategies, listing (start)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
GL = [
    ('embodiment(n)', 'concrete representation ; incarnation.', 'ٹھوس نمائندگی؛ مجسم صورت۔', 'عیني استازیتوب؛ مجسم بڼه.'),
    ('Esteem(n)', 'regard highly', 'بہت قدر کرنا', 'ډېر درناوی کول'),
    ('expedition(n)', 'a military compaign organized to achieve a specific objective.', 'کسی مخصوص مقصد کے حصول کے لیے منظم فوجی مہم۔', 'د یوې ټاکلې موخې د ترلاسه کولو لپاره تنظیم شوې پوځي کمپاین.'),
    ('gains (n)', 'benefits.', 'فوائد۔', 'ګټې.'),
    ('indolent(adj)', 'idle ; work-shy.', 'سست؛ کام چور۔', 'لټ؛ له کار تښتېدونکی.'),
    ('Integral (adj)', 'essential.', 'لازمی۔', 'اړین.'),
    ('lag behind(ph.v)', 'remain backward.', 'پیچھے رہ جانا۔', 'شاته پاتې کېدل.'),
    ('lofty(iest)(adj)', 'exalted ; of high moral value', 'بلند؛ اعلیٰ اخلاقی قدر کا حامل', 'لوړ؛ د لوړ اخلاقي ارزښت لرونکی'),
    ('obscure(adj)', 'not famous ; indistinct.', 'غیر معروف؛ غیر واضح۔', 'نامشهور؛ ناڅرګند.'),
    ('ostentation(n)', 'showy display ; pomposity.', 'نمود و نمائش؛ شان و شوکت کا دکھاوا۔', 'ځان‌ښودنه؛ دبدبه.'),
    ('prosperity(n)', 'the state of being successful and having a lot of money.', 'کامیاب ہونے اور بہت سا پیسہ رکھنے کی حالت۔', 'د بریالیتوب او ډېرو پیسو د لرلو حالت.'),
    ('rectify(adj)', 'Correct', 'درست کرنا', 'سمول'),
    ('rectitude(n)', 'uprightness ; righteousness.', 'راست بازی؛ نیکوکاری۔', 'سموالی؛ نېکي.'),
    ('repose(v)', 'to put something ( trust) in something.', 'کسی چیز پر (بھروسہ) رکھنا۔', 'په یو شي (باور) کول.'),
    ('reverence(n)', 'veneration ; a feeling of profound respect.', 'تعظیم؛ گہرے احترام کا احساس۔', 'تعظیم؛ د ژور درناوي احساس.'),
    ('sagaciously(adv.)', 'wisely.', 'دانشمندی سے۔', 'په هوښیارۍ.'),
    ('scantiness(v)', 'meagerness ; in small quantity.', 'قلت؛ کم مقدار میں۔', 'کمښت؛ په لږ مقدار.'),
    ('stern(adj)', 'strict ; severe.', 'سخت؛ کڑا۔', 'سخت؛ کلک.'),
    ('strife(n)', 'bitter conflict.', 'شدید تنازع۔', 'سخته شخړه.'),
    ('sublime(adj)', 'lofty.', 'بلند و بالا۔', 'لوړ.'),
    ('tender(adj)', 'young and immature.', 'کم عمر اور ناپختہ۔', 'ځوان او ناپوخ.'),
    ('vanity(n)', 'feelings of excessive pride ; boastfulness.', 'حد سے زیادہ غرور کا احساس؛ شیخی۔', 'د ډېر غرور احساس؛ ځان‌ستاینه.'),
    ('vibrant(adj)', 'vigorous.', 'پُرجوش۔', 'پیاوړی.'),
]
g = Builder()
g.table('eng12-u01-gloss-b', ['Word', 'Meaning'], [[w, m] for w, m, _, _ in GL], ['لفظ', 'معنی'], ['کلمه', 'مانا'], [[w, u] for w, _, u, _ in GL], [[w, p] for w, _, _, p in GL])
gl = BOOK.record(g, 'eng12-u01-glossary-b', 'Glossary (2)', 'فرہنگ (2)', 'وییپانګه (2)', 9, [5])

q = Builder()
q.h('Reading Comprehension', 'مطالعہ اور فہم', 'لوستل او پوهه')
q.h('Answer the Questions', 'سوالات کے جواب دیں', 'پوښتنو ته ځواب ورکړئ')
q.group('lines', [
    ('1. How was the youth given a great esteem by the beloved Rasool (ﷺ) in the Battle of Uhud?', '1. غزوۂ احد میں پیارے رسول (ﷺ) نے نوجوانوں کو کس طرح بڑی قدر دی؟', '1. د احد په غزا کې خوږ رسول (ﷺ) ځوانانو ته څنګه لوی درناوی ورکړ؟'),
    ('2. Narrate the hadith in which the beloved Rasool (ﷺ) resembles himself with the last brick of the otherwise complete house of prophethood.', '2. وہ حدیث بیان کریں جس میں پیارے رسول (ﷺ) نے خود کو نبوت کی باقی مکمل عمارت کی آخری اینٹ سے تشبیہ دی ہے۔', '2. هغه حدیث بیان کړئ چې پکې خوږ رسول (ﷺ) ځان د نبوت د پاتې بشپړې ودانۍ له وروستۍ خښتې سره تشبیه کوي.'),
    ('3. How did Hazrat Muhammad (رسول اللہ خاتم النبیین ﷺ) spend his youth ?', '3. حضرت محمد (رسول اللہ خاتم النبیین ﷺ) نے اپنی جوانی کیسے گزاری؟', '3. حضرت محمد (رسول الله خاتم النبیین ﷺ) خپله ځواني څنګه تېره کړه؟'),
    ('4. Evaluate in brief the character of present day youth in the light of the teachings of the beloved Rasool (ﷺ).', '4. پیارے رسول (ﷺ) کی تعلیمات کی روشنی میں آج کے نوجوانوں کے کردار کا مختصر جائزہ لیں۔', '4. د خوږ رسول (ﷺ) د لارښوونو په رڼا کې د نن ورځې د ځوانانو شخصیت په لنډه توګه وارزوئ.'),
    ('5. What social activities did Hazrat Muhammad (رسول اللہ خاتم النبیین ﷺ) participate in his youth?', '5. حضرت محمد (رسول اللہ خاتم النبیین ﷺ) نے اپنی جوانی میں کن سماجی سرگرمیوں میں حصہ لیا؟', '5. حضرت محمد (رسول الله خاتم النبیین ﷺ) په خپله ځوانۍ کې په کومو ټولنیزو فعالیتونو کې برخه واخیسته؟'),
    ('6. What did the Holy Rasool (ﷺ) say about modesty (Haya)? What is the importance of modesty in the life of youth?', '6. رسولِ پاک (ﷺ) نے حیا کے بارے میں کیا فرمایا؟ نوجوانوں کی زندگی میں حیا کی کیا اہمیت ہے؟', '6. سپیڅلي رسول (ﷺ) د حیا په اړه څه وفرمایل؟ د ځوانانو په ژوند کې د حیا اهمیت څه دی؟'),
    ('7. Cite an instance from the text showing that the beloved Rasool (ﷺ) lead simple and austere life.', '7. متن سے کوئی مثال پیش کریں جس سے ظاہر ہو کہ پیارے رسول (ﷺ) سادہ اور کفایت شعار زندگی گزارتے تھے۔', '7. له متن څخه یوه بېلګه راوړئ چې وښيي خوږ رسول (ﷺ) ساده او قناعت‌ناک ژوند درلود.'),
    ('8. What type of youth did the Holy Rasool (ﷺ) want to see?', '8. رسولِ پاک (ﷺ) کس قسم کے نوجوان دیکھنا چاہتے تھے؟', '8. سپیڅلي رسول (ﷺ) څه ډول ځوانان لیدل غوښتل؟'),
])
rc = BOOK.record(q, 'eng12-u01-comprehension', 'Reading Comprehension', 'مطالعہ اور فہم', 'لوستل او پوهه', 9, [6])

w = Builder()
w.h('Writing Suggestions', 'تحریری تجاویز', 'د لیکلو وړاندیزونه')
w.h('Pre-writing Strategies', 'لکھنے سے پہلے کی حکمتِ عملیاں', 'د لیکلو مخکې ستراتیژۍ')
w.p('Pre-writing strategies use writing to generate and clarify ideas. While many writers have traditionally created outlines before beginning writing, there are several other effective prewriting activities. We often call these prewriting strategies "brainstorming techniques." Five useful strategies are listing, clustering, freewriting, looping, and asking the six journalists\' questions. These strategies help you with both your invention and organization of ideas, and can aid you in developing topics for your writing.',
    'لکھنے سے پہلے کی حکمتِ عملیاں خیالات پیدا کرنے اور واضح کرنے کے لیے لکھنے کو استعمال کرتی ہیں۔ اگرچہ بہت سے لکھنے والے روایتی طور پر لکھنا شروع کرنے سے پہلے خاکے بناتے رہے ہیں، تاہم لکھنے سے پہلے کی کئی اور مؤثر سرگرمیاں بھی ہیں۔ ہم اکثر ان حکمتِ عملیوں کو ’’ذہنی آزمائش کی تکنیکیں‘‘ کہتے ہیں۔ پانچ مفید حکمتِ عملیاں یہ ہیں: فہرست سازی، گروہ بندی، آزادانہ لکھنا، دائرہ وار لکھنا، اور صحافیوں کے چھ سوالات پوچھنا۔ یہ حکمتِ عملیاں خیالات کی ایجاد اور ترتیب دونوں میں آپ کی مدد کرتی ہیں اور آپ کی تحریر کے موضوعات کو پروان چڑھانے میں معاون ہو سکتی ہیں۔',
    'د لیکلو مخکې ستراتیژۍ د نظرونو د پیدا کولو او روښانه کولو لپاره له لیکلو کار اخلي. که څه هم ډېرو لیکوالو په دودیز ډول له لیکلو مخکې طرحې جوړولې، خو د لیکلو مخکې نور ګڼ اغېزمن فعالیتونه هم شته. موږ اکثرا دې ستراتیژیو ته "د فکرونو د راټولولو تخنیکونه" وایو. پنځه ګټورې ستراتیژۍ دا دي: لست جوړول، ډله‌بندي، ازاده لیکنه، کړۍ‌ییزه لیکنه، او د خبریالانو د شپږو پوښتنو کول. دا ستراتیژۍ ستاسو سره د نظرونو په ایجاد او تنظیم دواړو کې مرسته کوي او ستاسو د لیکنې د موضوعاتو په پراختیا کې مرسته کولی شي.')
w.h('i. Listing', 'i. فہرست سازی', 'i. لست جوړول')
w.p('Listing is a process of generating a lot of information within a short time by generating some broad ideas and then building on those associations for more detail. Listing is particularly useful if your starting topic is very broad and you need to narrow it down.',
    'فہرست سازی کچھ وسیع خیالات پیدا کر کے اور پھر مزید تفصیل کے لیے ان روابط کو آگے بڑھا کر کم وقت میں بہت سی معلومات پیدا کرنے کا عمل ہے۔ فہرست سازی خاص طور پر اس وقت مفید ہے جب آپ کا ابتدائی موضوع بہت وسیع ہو اور آپ کو اسے محدود کرنا ہو۔',
    'لست جوړول د ځینو پراخو نظرونو د پیدا کولو او بیا د ډېر تفصیل لپاره پر هغو اړیکو د جوړولو له لارې په لنډ وخت کې د ډېرو معلوماتو د پیدا کولو بهیر دی. لست جوړول په ځانګړي ډول هغه وخت ګټور دی چې ستاسو پیلنۍ موضوع ډېره پراخه وي او تاسو یې محدودولو ته اړتیا لرئ.')
w.group('list', [('Jot down all the possible terms that emerge from the general topic you are working on. This procedure works especially well if you work in a team. All team members can generate ideas, with one member acting as scribe. Do not worry about editing or throwing out what might not be a good idea. Simply write down as many possibilities as you can.',
                  'جس عمومی موضوع پر آپ کام کر رہے ہیں اس سے ابھرنے والی تمام ممکنہ اصطلاحات لکھ لیں۔ یہ طریقہ خاص طور پر ٹیم میں کام کرنے کی صورت میں اچھا کام کرتا ہے۔ ٹیم کے تمام ارکان خیالات پیش کر سکتے ہیں اور ایک رکن لکھنے کا کام کرے۔ ترمیم کرنے یا ناموزوں خیال کو نکال پھینکنے کی فکر نہ کریں۔ بس جتنے زیادہ امکانات لکھ سکیں لکھ لیں۔',
                  'هغه ټول ممکن اصطلاحات ولیکئ چې له هغې عمومي موضوع څخه راپورته کېږي چې پرې کار کوئ. دا طریقه په ځانګړي ډول هغه وخت ښه کار کوي چې په ټیم کې کار وکړئ. د ټیم ټول غړي نظرونه وړاندې کولی شي او یو غړی د لیکوال کار وکړي. د سمون یا د هغه څه د لرې کولو اندېښنه مه کوئ چې ښه نظر نه وي. یوازې څومره چې کولی شئ امکانات ولیکئ.')])
ws = BOOK.record(w, 'eng12-u01-writing-a', 'Writing Suggestions — pre-writing strategies (1)', 'تحریری تجاویز — لکھنے سے پہلے کی حکمتِ عملیاں (1)', 'د لیکلو وړاندیزونه — د لیکلو مخکې ستراتیژۍ (1)', 9, [6])
issues = [{'id': 'eng12-p5-6-typos', 'unit': 1, 'printedPage': 5, 'description': 'Glossary prints “compaign”, “rectify(adj)”, “scantiness(v)”; question 7 prints “lead simple and austere life” (led). Printed text retained.'}]

if __name__ == '__main__':
    BOOK.save(9, [(1, gl), (1, rc), (1, ws)], issues=issues)
