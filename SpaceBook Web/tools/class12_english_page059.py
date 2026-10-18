"""PDF59 (printed 105–106): Unit 11 Glossary (fetter … zest); Reading Comprehension Q1–6; Writing; Oral; Vocabulary — transitional devices (intro)."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
g = Builder()
gloss(g, 'eng12-u11-gloss-b', [
    ('fetter(n)', 'hold; restrain; shackle.', 'روکنا؛ قابو کرنا؛ بیڑی ڈالنا۔', 'نیول؛ بندول؛ زولنه اچول.'),
    ('grueling(adj.)', 'toilsome; that requires much physieal effort.', 'مشقت طلب؛ جس میں بہت جسمانی محنت درکار ہو۔', 'ستړی کوونکی؛ چې ډېرې فزیکي هڅې ته اړتیا لري.'),
    ('grab(v)', 'catch; take hold of.', 'پکڑنا؛ تھام لینا۔', 'نیول؛ ټینګ نیول.'),
    ('give in(ph.v.)', "succumb; yield; now; accept one's defeat.", 'ہار ماننا؛ جھک جانا؛ اپنی شکست تسلیم کرنا۔', 'ماتې منل؛ تسلیمېدل؛ خپله ماتې منل.'),
    ('ignite(v)', 'arouse feelings and passions.', 'جذبات اور ولولے ابھارنا۔', 'احساسات او جذبې راپارول.'),
    ('incredible(adj.)', 'unbelievable.', 'ناقابلِ یقین۔', 'د باور وړ نه.'),
    ('in a row', 'in a series; consecutively.', 'سلسلہ وار؛ مسلسل۔', 'په لړۍ کې؛ پرله‌پسې.'),
    ('malady(ies) (n)', 'ailments; diseases', 'امراض؛ بیماریاں', 'ناروغۍ؛ رنځونه'),
    ('moisture(n)', 'wetness', 'نمی', 'لندبل'),
    ('plunge into (v)', 'begin with vigour.', 'جوش سے آغاز کرنا۔', 'په جوش پیل کول.'),
    ('prevail(n)', 'predominate; reign.', 'غالب آنا؛ حاوی ہونا۔', 'برلاسی کېدل؛ واکمن کېدل.'),
    ('phenomenal(adj.)', 'unbelievably great.', 'ناقابلِ یقین حد تک عظیم۔', 'د باور وړ نه تر حده ستر.'),
    ('rival(v)', 'compete with', 'مقابلہ کرنا', 'سیالي کول'),
    ('succumb to(v)', 'give in; now before', 'ہار مان لینا؛ جھک جانا', 'تسلیمېدل؛ ټیټېدل'),
    ('stamina(n)', 'staying power.', 'قوتِ برداشت۔', 'د زغم ځواک.'),
    ('satiate(v)', 'to satisfy.', 'تسکین دینا۔', 'اروا کول.'),
    ('scratch line', 'starting line; beginning.', 'آغاز کی لکیر؛ ابتدا۔', 'د پیل کرښه؛ پیل.'),
    ('streak(n)', 'an unbroken series of events .', 'واقعات کا نہ ٹوٹنے والا سلسلہ۔', 'د پېښو نه ماتېدونکې لړۍ.'),
    ('sprint(n)', 'a quick run.', 'تیز دوڑ۔', 'ګړندۍ منډه.'),
    ('successively(adv.)', 'consecutively.', 'مسلسل۔', 'پرله‌پسې.'),
    ('solemn(adj.)', 'sincere; signifier.', 'سنجیدہ؛ پُر خلوص۔', 'سنجیده؛ له اخلاصه ډک.'),
    ('tremendous(adj)', 'grand; extreme in degree.', 'عظیم؛ انتہائی درجے کا۔', 'ستر؛ په درجه کې ډېر.'),
    ('toe to toe(idiom)', 'be able to compete with someone in a strong, determined way.', 'کسی سے مضبوط اور پُرعزم انداز میں مقابلہ کرنے کے قابل ہونا۔', 'له یو چا سره په قوي او هوډمن ډول د سیالۍ وړتیا.'),
    ('unshakable(adj.)', 'steadfast; marked by firm determination.', 'ثابت قدم؛ پختہ عزم والا۔', 'ثابت قدم؛ د ټینګ هوډ لرونکی.'),
    ('rigorous(adj.)', 'follow rules/procedure in a severe way.', 'قواعد/طریقۂ کار کی سختی سے پابندی کرنا۔', 'قواعدو/طریقې ته په سختۍ پابند.'),
    ("win one's spurs(idiom)", "to prove one's skill in a particular area.", 'کسی خاص شعبے میں اپنی مہارت ثابت کرنا۔', 'په یوه ځانګړې برخه کې خپل مهارت ثابتول.'),
    ('wrap up(v)', 'finish off', 'ختم کرنا', 'پای ته رسول'),
    ('zest(n)', 'enthusiasm', 'جوش', 'لېوالتیا'),
])
gl = BOOK.record(g, 'eng12-u11-glossary-b', 'Glossary (2)', 'فرہنگ (2)', 'وییپانګه (2)', 59, [105])

q = Builder()
q.h('Reading Comprehension', 'مطالعہ اور فہم', 'لوستل او پوهه')
q.group('lines', [
    ("1. Why did Jahangir Khan go against his doctors' advice of refraining from taking part in any physical activity?", '1. جہانگیر خان نے کسی بھی جسمانی سرگرمی میں حصہ نہ لینے کے بارے میں اپنے ڈاکٹروں کے مشورے کے خلاف کیوں کیا؟', '1. جهانګیر خان ولې په هر فزیکي فعالیت کې د ګډون نه کولو د خپلو ډاکټرانو د مشورې پر خلاف عمل وکړ؟'),
    ('2. Read paragraph no 6 of the text and say what did Jahangir Khan do to maintain his physical fitness?', '2. متن کا پیراگراف نمبر 6 پڑھیں اور بتائیں کہ جہانگیر خان اپنی جسمانی فٹنس برقرار رکھنے کے لیے کیا کرتے تھے؟', '2. د متن شپږم پراګراف ولولئ او ووایاست چې جهانګیر خان د خپلې فزیکي روغتیا د ساتلو لپاره څه کول؟'),
    ('3. Give a brief detail of Jahangir Khan\'s achievements in the light of the text, " Jahangir Khan – the conqueror".', '3. متن ’’جہانگیر خان — فاتح‘‘ کی روشنی میں جہانگیر خان کی کامیابیوں کی مختصر تفصیل دیں۔', '3. د "جهانګیر خان — فاتح" متن په رڼا کې د جهانګیر خان د لاسته راوړنو لنډ تفصیل ورکړئ.'),
    ('4. Keeping in view the achievements of Jahangir Khan, compare any other national hero in sports with him.', '4. جہانگیر خان کی کامیابیوں کو مدِ نظر رکھتے ہوئے کھیلوں کے کسی اور قومی ہیرو کا ان سے موازنہ کریں۔', '4. د جهانګیر خان لاسته راوړنې په پام کې ونیسئ او په ورزش کې بل ملي اتل ورسره پرتله کړئ.'),
    ('5. An idiom is the expression whose meaning cannot be inferred from the meanings of the words that make it up. Find out three idiomatic expressions from the text and explain their meanings.', '5. محاورہ وہ اظہار ہے جس کے معنی اسے بنانے والے الفاظ کے معنی سے اخذ نہیں کیے جا سکتے۔ متن سے تین محاوراتی اظہارات تلاش کریں اور ان کے معنی کی وضاحت کریں۔', '5. محاوره هغه څرګندونه ده چې مانا یې د جوړوونکو کلمو له ماناوو نه شي اخیستل کېدای. له متن څخه درې محاوره‌ییز څرګندونې ومومئ او ماناوې یې تشریح کړئ.'),
    ('6. What inspiration do you get from the life of Jahangir Khan?', '6. جہانگیر خان کی زندگی سے آپ کو کیا حوصلہ ملتا ہے؟', '6. د جهانګیر خان له ژوند څخه تاسو څه الهام اخلئ؟'),
])
q.h('Writing Suggestions', 'تحریری تجاویز', 'د لیکلو وړاندیزونه')
q.p('Write an essay on the present state of Squash in Pakistan.', 'پاکستان میں اسکواش کی موجودہ حالت پر ایک مضمون لکھیں۔', 'په پاکستان کې د سکواش د اوسني حالت په اړه یوه مقاله ولیکئ.')
q.h('Oral Communication', 'زبانی ابلاغ', 'د خولې اړیکه')
q.p('Divide the students into groups on the basis of the choice of their favourite game. Ask each member to share his reasons in the group for liking the particular game in the group.', 'طلبہ کو ان کے پسندیدہ کھیل کی بنیاد پر گروہوں میں تقسیم کریں۔ ہر رکن سے کہیں کہ گروہ میں اس خاص کھیل کو پسند کرنے کی اپنی وجوہات بتائے۔', 'زده کوونکي د خپلې خوښې لوبې پر بنسټ په ډلو ووېشئ. له هر غړي وغواړئ چې په ډله کې د هغې ځانګړې لوبې د خوښولو دلیلونه شریک کړي.')
q.h('Vocabulary and Grammar', 'ذخیرۂ الفاظ اور قواعد', 'لغات او ګرامر')
q.h('Transitional Devices', 'عبوری ذرائع', 'انتقالي وسایل')
q.p('Transitional devices are like bridges between parts of your paper. They are cues that help the reader to interpret ideas a paper develops. Transitional devices are words or phrases that help carry a thought from one sentence to another, from one idea to another, or from one paragraph to another. And finally, transitional devices link sentences and paragraphs together smoothly so that there are no abrupt jumps or breaks between ideas. There are several types of transitional devices, and each category leads readers to make certain connections or assumptions. Some lead readers forward and imply the building of an idea or thought, while others make readers compare ideas or draw conclusions from the preceding thoughts.',
    'عبوری ذرائع آپ کی تحریر کے حصوں کے درمیان پلوں کی مانند ہیں۔ یہ ایسے اشارے ہیں جو قاری کو تحریر میں پیش کیے گئے خیالات سمجھنے میں مدد دیتے ہیں۔ عبوری ذرائع وہ الفاظ یا فقرے ہیں جو ایک خیال کو ایک جملے سے دوسرے، ایک خیال سے دوسرے یا ایک پیراگراف سے دوسرے تک لے جانے میں مدد دیتے ہیں۔ اور آخر میں عبوری ذرائع جملوں اور پیراگرافوں کو آسانی سے جوڑتے ہیں تاکہ خیالات کے درمیان اچانک چھلانگ یا خلا نہ ہو۔ عبوری ذرائع کی کئی اقسام ہیں اور ہر زمرہ قارئین کو مخصوص روابط یا قیاس تک لے جاتا ہے۔ کچھ قارئین کو آگے لے جاتے ہیں اور کسی خیال کی تعمیر کا اشارہ دیتے ہیں، جبکہ کچھ قارئین سے خیالات کا موازنہ کرواتے ہیں یا پچھلے خیالات سے نتائج اخذ کرواتے ہیں۔',
    'انتقالي وسایل ستاسو د لیکنې د برخو ترمنځ د پلونو په څېر دي. دا هغه نښې دي چې لوستونکي سره د لیکنې د پراختیا شویو نظرونو په پوهېدو کې مرسته کوي. انتقالي وسایل هغه کلمې یا عبارتونه دي چې یو فکر له یوې جملې بلې ته، له یوه نظر بل ته یا له یوه پراګراف بل ته په وړلو کې مرسته کوي. او په پای کې انتقالي وسایل جملې او پراګرافونه په اسانۍ سره تړي ترڅو د نظرونو ترمنځ ناڅاپي ټوپونه یا تشې نه وي. د انتقالي وسایلو ګڼ ډولونه شته او هره کټګوري لوستونکي ځانګړو اړیکو یا انګېرنو ته رسوي. ځینې لوستونکي وړاندې وړي او د یوه نظر یا فکر جوړېدو ته اشاره کوي، په داسې حال کې چې نور لوستونکي اړ کوي چې نظرونه پرتله کړي یا له مخکینیو فکرونو پایلې واخلي.')
qs = BOOK.record(q, 'eng12-u11-comprehension', 'Reading Comprehension; Writing; Oral; Transitional devices (1)', 'مطالعہ اور فہم؛ تحریر؛ زبانی ابلاغ؛ عبوری ذرائع (1)', 'لوستل او پوهه؛ لیکنه؛ د خولې اړیکه؛ انتقالي وسایل (1)', 59, [106])
issues = [{'id': 'eng12-p105-106', 'unit': 11, 'printedPage': 105, 'description': "Printed text retained: glossary “physieal”, “give in … now; accept” and “succumb to … now before” (bow), “prevail(n)”, “solemn … signifier”."}]

if __name__ == '__main__':
    BOOK.save(59, [(11, gl), (11, qs)], issues=issues)
