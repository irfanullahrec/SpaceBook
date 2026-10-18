"""PDF11 (printed 9–10): journalists' questions (end), Activity; Oral Communication; Vocabulary and Grammar — IPA, 44 phonemes, consonants table 1–10."""
from class12_book_common import Book, Builder

BOOK = Book('english')
w = Builder()
w.p('issue and at what point in time will the problem or issue culminate in a crisis? When is action needed to address the issue or problem?', 'معاملے کو شکل دینے میں مدد کی اور کس وقت مسئلہ یا معاملہ بحران کی صورت اختیار کرے گا؟ مسئلے یا معاملے سے نمٹنے کے لیے کب اقدام کی ضرورت ہے؟', 'مسئلې په جوړولو کې مرسته وکړه او په کوم وخت کې به ستونزه یا مسئله په بحران بدله شي؟ د مسئلې یا ستونزې د حل لپاره کله اقدام ته اړتیا ده؟')
for head, en, ur, ps in [
    (('Why?:', 'کیوں؟:', 'ولې؟:'), 'Why did the issue or problem arise? Why is it (your topic) an issue or problem at all? Why did the issue or problem develop in the way that it did?', 'معاملہ یا مسئلہ کیوں پیدا ہوا؟ یہ (آپ کا موضوع) سرے سے معاملہ یا مسئلہ کیوں ہے؟ معاملہ یا مسئلہ اسی طرح کیوں پروان چڑھا جیسے چڑھا؟', 'مسئله یا ستونزه ولې رامنځته شوه؟ دا (ستاسو موضوع) اصلاً ولې مسئله یا ستونزه ده؟ مسئله یا ستونزه ولې په هغه ډول وده وکړه چې وکړه؟'),
    (('How?:', 'کیسے؟:', 'څنګه؟:'), 'How is the issue or problem significant? How can it be addressed? How does it affect the participants? How can the issue or problem be resolved?', 'معاملہ یا مسئلہ کس طرح اہم ہے؟ اس سے کیسے نمٹا جا سکتا ہے؟ یہ شرکاء کو کیسے متاثر کرتا ہے؟ معاملہ یا مسئلہ کیسے حل کیا جا سکتا ہے؟', 'مسئله یا ستونزه څنګه مهمه ده؟ څنګه حل کېدای شي؟ پر ګډونوالو څنګه اغېز کوي؟ مسئله یا ستونزه څنګه هوارېدای شي؟'),
]:
    w.h(*head); w.p(en, ur, ps)
w.p("The journalists' questions are a powerful way to develop a great deal of information about a topic very quickly. Learning to ask the appropriate questions about a topic takes practice, however. At times during writing an assignment, you may wish to go back and ask the journalists' questions again to clarify important points that may be getting lost in your planning and drafting",
    'صحافیوں کے سوالات کسی موضوع کے بارے میں بہت جلد بہت سی معلومات حاصل کرنے کا ایک طاقتور ذریعہ ہیں۔ تاہم کسی موضوع کے بارے میں موزوں سوالات پوچھنا سیکھنے کے لیے مشق درکار ہے۔ کبھی کبھار کوئی تحریری کام لکھتے ہوئے آپ واپس جا کر صحافیوں کے سوالات دوبارہ پوچھنا چاہیں گے تاکہ ان اہم نکات کو واضح کریں جو آپ کی منصوبہ بندی اور مسودہ نویسی میں کھو رہے ہوں',
    'د خبریالانو پوښتنې د یوې موضوع په اړه په ډېر چټک ډول د ډېرو معلوماتو د پیدا کولو پیاوړې لاره ده. خو د یوې موضوع په اړه د مناسبو پوښتنو کول زده کول تمرین ته اړتیا لري. ځینې وخت د یوې دندې د لیکلو پر مهال کېدای شي وغواړئ بېرته لاړ شئ او د خبریالانو پوښتنې بیا وکړئ ترڅو هغه مهم ټکي روښانه کړئ چې ستاسو په پلان جوړونه او مسوده لیکنه کې ورکېږي')
w.h('Activity', 'سرگرمی', 'فعالیت')
w.p("Now keeping in mind the prewriting strategies, develop and outline on the topic 'The Love of Holy Prophet (ﷺ) for the youth of Ummah.'",
    'اب لکھنے سے پہلے کی حکمتِ عملیوں کو ذہن میں رکھتے ہوئے ’’امت کے نوجوانوں کے لیے نبیِ پاک (ﷺ) کی محبت‘‘ کے موضوع پر ایک خاکہ تیار کریں۔',
    'اوس د لیکلو مخکې ستراتیژۍ په پام کې ونیسئ او د "د امت ځوانانو ته د سپیڅلي پیغمبر (ﷺ) مینه" په موضوع یوه طرحه جوړه کړئ.')
w.h('Oral Communication', 'زبانی ابلاغ', 'د خولې اړیکه')
w.p('Students will be divided into small groups of five members each. They will be given the task to discuss and point out the weaknesses in the character of the modern day youth and suggest remedies. Then one member from each group will stand and share the result of the group discussion with the whole class. Each representative will be given 3 to 5 minutes for expression.',
    'طلبہ کو پانچ پانچ ارکان کے چھوٹے گروہوں میں تقسیم کیا جائے گا۔ انہیں یہ کام دیا جائے گا کہ وہ آج کے نوجوانوں کے کردار کی کمزوریوں پر بحث کریں، ان کی نشاندہی کریں اور ان کا علاج تجویز کریں۔ پھر ہر گروہ سے ایک رکن کھڑا ہو کر گروہی بحث کا نتیجہ پوری جماعت کے سامنے پیش کرے گا۔ ہر نمائندے کو اظہار کے لیے 3 سے 5 منٹ دیے جائیں گے۔',
    'زده کوونکي به د پنځو پنځو غړو په کوچنیو ډلو ووېشل شي. دوی ته به دنده ورکړل شي چې د نن ورځې د ځوانانو په شخصیت کې پر کمزوریو بحث وکړي، په ګوته یې کړي او درمل یې وړاندیز کړي. بیا به له هرې ډلې یو غړی ودرېږي او د ډله‌ییز بحث پایله به له ټول ټولګي سره شریکه کړي. هر استازي ته به د څرګندونې لپاره 3 تر 5 دقیقې ورکړل شي.')
ws = BOOK.record(w, 'eng12-u01-writing-c', "Journalists' questions (end); Activity; Oral Communication", 'صحافیوں کے سوالات (اختتام)؛ سرگرمی؛ زبانی ابلاغ', 'د خبریالانو پوښتنې (پای)؛ فعالیت؛ د خولې اړیکه', 11, [9])

v = Builder()
v.h('Vocabulary and Grammar', 'ذخیرۂ الفاظ اور قواعد', 'لغات او ګرامر')
v.h('The International Phonetic Alphabet (IPA)', 'بین الاقوامی صوتی حروفِ تہجی (IPA)', 'نړیوال غږیز الفبا (IPA)')
for x in [
    ("How can you pronounce a word you've never read? It can be a bit tricky. How about a word in a foreign language? Now that must be impossible! Or is it? Imagine a set of symbols that could tell you how to pronounce any word in any language on the planet? Well that is exactly what the International Phonetic Alphabet is. Currently, the IPA consists of 107 sound symbols, 52 diacritics (accents) and 4 prosodic marks (intonations) encompassing virtually every phoneme used in every language on the earth. So for any written word, you can identify the associated phoneme symbols, and with a bit of practice, pronounce the word!",
     'آپ ایسے لفظ کا تلفظ کیسے کر سکتے ہیں جو آپ نے کبھی پڑھا نہ ہو؟ یہ کچھ مشکل ہو سکتا ہے۔ اور کسی غیر ملکی زبان کے لفظ کا کیا؟ یہ تو ناممکن ہو گا! یا نہیں؟ تصور کریں علامات کا ایک ایسا مجموعہ جو آپ کو بتا سکے کہ دنیا کی کسی بھی زبان کے کسی بھی لفظ کا تلفظ کیسے کریں؟ بالکل یہی بین الاقوامی صوتی حروفِ تہجی ہے۔ اس وقت IPA میں 107 صوتی علامات، 52 اعراب (لہجے کی علامات) اور 4 عروضی علامات (آہنگ) ہیں جو زمین کی ہر زبان میں استعمال ہونے والے تقریباً ہر صوتیے کا احاطہ کرتی ہیں۔ لہٰذا کسی بھی لکھے ہوئے لفظ کے لیے آپ متعلقہ صوتی علامات پہچان سکتے ہیں اور تھوڑی سی مشق سے لفظ ادا کر سکتے ہیں!',
     'تاسو هغه کلمه څنګه تلفظ کولی شئ چې مو هېڅکله نه وي لوستې؟ دا یو څه ستونزمن کېدای شي. او د یوې بهرنۍ ژبې کلمه څنګه؟ دا خو باید ناشونې وي! که نه؟ تصور وکړئ د نښو داسې ټولګه چې تاسو ته وښيي چې د ځمکې د هرې ژبې هره کلمه څنګه تلفظ کړئ؟ همدا په دقیق ډول نړیوال غږیز الفبا ده. اوس مهال IPA له 107 غږیزو نښو، 52 اعرابو (د لهجې نښو) او 4 عروضي نښو (اهنګونو) جوړ دی چې د ځمکې په هره ژبه کې د کارېدونکي نږدې هر غږ‌پوړي احاطه کوي. نو د هرې لیکل شوې کلمې لپاره تاسو کولی شئ اړوندې غږیزې نښې وپېژنئ او د لږ تمرین سره کلمه تلفظ کړئ!'),
    ('The IPA was created by the International Phonetic Association. Founded in 1886 in Paris.Their original mission was to help school children pronounce words in foreign languages and to aid in the teaching of reading. Today their mission is to promote the scientific study of phonetics.',
     'IPA بین الاقوامی صوتیاتی انجمن نے بنائی۔ یہ انجمن 1886 میں پیرس میں قائم ہوئی۔ اس کا اصل مقصد اسکول کے بچوں کو غیر ملکی زبانوں کے الفاظ کا تلفظ کرنے میں مدد دینا اور پڑھنا سکھانے میں معاونت کرنا تھا۔ آج اس کا مقصد صوتیات کے سائنسی مطالعے کو فروغ دینا ہے۔',
     'IPA د نړیوالې غږپوهنې ټولنې جوړ کړی. دا ټولنه په 1886 کې په پاریس کې جوړه شوه. د هغې اصلي موخه د ښوونځي ماشومانو سره د بهرنیو ژبو د کلمو په تلفظ کې مرسته او د لوستلو په زده کړه کې ملاتړ و. نن یې موخه د غږپوهنې د علمي مطالعې وده ده.'),
]: v.p(*x)
v.h('The 44 Phonemes in English', 'انگریزی کے 44 صوتیے', 'په انګلیسي کې 44 غږ‌پوړي')
for x in [
    ('Despite there being just 26 letters in the English language there are approximately 44 unique sounds, also known as phonemes. The 44 sounds help distinguish one word or meaning from another. Various letters and letter combinations known as graphemes are used to represent the sounds.',
     'انگریزی زبان میں صرف 26 حروف ہونے کے باوجود تقریباً 44 منفرد آوازیں ہیں جنہیں صوتیے (فونیم) بھی کہتے ہیں۔ یہ 44 آوازیں ایک لفظ یا معنی کو دوسرے سے ممتاز کرنے میں مدد دیتی ہیں۔ ان آوازوں کو ظاہر کرنے کے لیے مختلف حروف اور حروف کے مجموعے استعمال ہوتے ہیں جنہیں گریفیم کہتے ہیں۔',
     'سره له دې چې په انګلیسي ژبه کې یوازې 26 توري دي، نږدې 44 ځانګړي غږونه شته چې غږ‌پوړي (فونیم) هم بلل کېږي. دا 44 غږونه یوه کلمه یا مانا له بلې بېلولو کې مرسته کوي. د دې غږونو د ښودلو لپاره بېلابېل توري او د تورو ترکیبونه کارول کېږي چې ګرافیم بلل کېږي.'),
    ('The 44 English sounds fall into two categories: consonants and vowels. Below is a list of the 44 phonemes along with their International Phonetic Alphabet symbols and some examples of their use. Note that there is no such thing as a definitive list of phonemes because of accents, dialects and the evolution of language itself. Therefore you may discover lists with more or less than these 44 sounds.',
     'انگریزی کی 44 آوازیں دو زمروں میں آتی ہیں: مصمتے اور مصوتے۔ نیچے 44 صوتیوں کی فہرست ان کی بین الاقوامی صوتی حروفِ تہجی کی علامات اور ان کے استعمال کی چند مثالوں کے ساتھ دی گئی ہے۔ نوٹ کریں کہ لہجوں، بولیوں اور خود زبان کے ارتقا کی وجہ سے صوتیوں کی کوئی حتمی فہرست موجود نہیں۔ اس لیے آپ کو ان 44 آوازوں سے کم یا زیادہ والی فہرستیں بھی مل سکتی ہیں۔',
     'د انګلیسي 44 غږونه په دوو کټګوریو وېشل کېږي: بې‌غږه (کانسوننټ) او غږلرونکي (واول). لاندې د 44 غږ‌پوړو لست د هغوی د نړیوال غږیز الفبا نښو او د کارونې ځینو بېلګو سره ورکړل شوی. پام وکړئ چې د لهجو، ګړدودونو او پخپله د ژبې د تکامل له امله د غږ‌پوړو کوم قطعي لست نشته. نو کېدای شي داسې لستونه ومومئ چې له دې 44 غږونو کم یا ډېر ولري.'),
]: v.p(*x)
v.h('Consonants', 'مصمتے', 'بې‌غږه توري (کانسوننټ)')
C = [['1', '/b/', 'b, bb', 'bug, bubble'], ['2', '/d/', 'd, dd, ed', 'dad, add, milled'], ['3', '/f/', 'f, ff, ph, gh, lf, ft', 'fat, cliff, phone, enough, half, often'],
     ['4', '/g/', 'g, gg, gh,gu,gue', 'gun, egg, ghost, guest, prologue'], ['5', '/h/', 'h, wh', 'hop, who'], ['6', '/dʒ/', 'j, ge, g, dge, di, gg', 'jam, wage, giraffe, edge, soldier, exaggerate'],
     ['7', '/k/', 'k, c, ch, cc, lk, qu ,q(u), ck, x', 'kit, cat, chris, accent, folk, bouquet, queen, rack, box'], ['8', '/I/', '1.ll, ll', 'live, well'],
     ['9', '/m/', 'm, mm, mb, mn, lm', 'man, summer, comb, column, palm'], ['10', '/n/', 'n, nn,kn, gn, pn', 'net,funny,know, gnat,pneumonic']]
v.table('eng12-u01-consonants-a', ['Phoneme', 'IPA Symbol', 'Graphemes', 'Examples'], C, ['صوتیہ', 'IPA علامت', 'گریفیم', 'مثالیں'], ['غږ‌پوړی', 'IPA نښه', 'ګرافیمونه', 'بېلګې'], C, C)
vg = BOOK.record(v, 'eng12-u01-ipa-a', 'Vocabulary and Grammar — IPA and the 44 phonemes (1)', 'ذخیرۂ الفاظ اور قواعد — IPA اور 44 صوتیے (1)', 'لغات او ګرامر — IPA او 44 غږ‌پوړي (1)', 11, [9, 10])
issues = [{'id': 'eng12-p9-10-typos', 'unit': 1, 'printedPage': 10, 'description': 'Activity prints “develop and outline” (an outline); consonant row 8 prints IPA “/I/” and graphemes “1.ll, ll” (should be /l/, “l, ll”); “chris”, “pneumonic” printed in lower case/as printed. Printed text retained.'}]

if __name__ == '__main__':
    BOOK.save(11, [(1, ws), (1, vg)], issues=issues)
