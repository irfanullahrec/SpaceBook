"""PDF41 (printed 69–70): Unit 7 Glossary (drift over … visceral); Reading Comprehension Q1–7; Writing Suggestions — comparison/contrast essays, block structure."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
g = Builder()
gloss(g, 'eng12-u07-gloss-b', [
    ('drift over(v)', 'A continuous slow movement from one place to another', 'ایک جگہ سے دوسری جگہ مسلسل آہستہ حرکت', 'له یوه ځایه بل ځای ته دوامداره ورو حرکت'),
    ('exoplanet(n)', 'a planet located outside our solar system', 'ہمارے نظامِ شمسی سے باہر واقع سیارہ', 'زموږ له لمریز نظام بهر پرته سیاره'),
    ('extrasolar(adj.)', '(of a planet, etc.) outside our solar system', '(سیارہ وغیرہ) ہمارے نظامِ شمسی سے باہر', '(سیاره او نور) زموږ له لمریز نظام بهر'),
    ('foreboding(n)', 'a strong feeling that something unpleasant or dangerous is going to happen', 'یہ شدید احساس کہ کچھ ناخوشگوار یا خطرناک ہونے والا ہے', 'دا قوي احساس چې یو ناخوښ یا خطرناک شی پېښېدونکی دی'),
    ('galactic(adj.)', 'relating to a galaxy', 'کہکشاں سے متعلق', 'له کهکشان سره تړلی'),
    ('habitable(adj.)', 'suitable for people to live in', 'لوگوں کے رہنے کے قابل', 'د خلکو د اوسېدو وړ'),
    ('ignite(v)', 'to set afire, to cause (a fuel) to burn', 'آگ لگانا، (ایندھن کو) جلانا', 'اور لګول، (سون توکي) سوځول'),
    ('intricate(adj.)', 'having a lot of different parts and small details that fit together', 'بہت سے مختلف حصوں اور چھوٹی تفصیلات والا جو آپس میں جڑتے ہوں', 'د ډېرو بېلابېلو برخو او کوچنیو جزییاتو لرونکی چې سره برابرېږي'),
    ('jaw-droppingly(adv.)', 'in a way that is so large or good that it surprises you very much', 'اس طرح جو اتنا بڑا یا اچھا ہو کہ بہت حیران کر دے', 'په داسې ډول چې دومره لوی یا ښه وي چې ډېر حیران مو کړي'),
    ('longevity(n)', 'long life; the fact of lasting a long time', 'طویل عمر؛ دیر تک قائم رہنا', 'اوږد عمر؛ د اوږد وخت لپاره دوام'),
    ('manifestations(n)', 'an event, action or thing that is a sign that something exists or is happening;', 'کوئی واقعہ، عمل یا چیز جو کسی چیز کے وجود یا ہونے کی علامت ہو؛', 'یوه پېښه، کړنه یا شی چې د یو شي د شتون یا پېښېدو نښه وي؛'),
    ('pinpoint(v)', 'to find and show the exact position of somebody/something', 'کسی کا/کسی چیز کا درست مقام معلوم کرنا اور دکھانا', 'د یو چا/یو شي دقیق ځای موندل او ښودل'),
    ('pristine(adj.)', 'fresh and clean, as if new', 'تازہ اور صاف، گویا نیا ہو', 'تازه او پاک، لکه نوی'),
    ('probe(n)', 'a complete and careful investigation of something', 'کسی چیز کی مکمل اور محتاط تحقیقات', 'د یو شي بشپړه او محتاطه څېړنه'),
    ('protostar(n)', 'a cloud of gas and dust in space believed to develop into a star', 'خلا میں گیس اور گرد کا بادل جس کے بارے میں خیال ہے کہ وہ ستارہ بنے گا', 'په فضا کې د ګاز او دوړو ورېځ چې باور کېږي ستوری به شي'),
    ('spectroscopic(adj.)', 'connected with the process of forming and looking at spectrum with a spectroscope', 'طیف بین (اسپیکٹروسکوپ) سے طیف بنانے اور دیکھنے کے عمل سے متعلق', 'د طیف‌بین (سپکټروسکوپ) په واسطه د طیف د جوړولو او کتلو له بهیر سره تړلی'),
    ('spectroscopy(n)', 'The study of forming and looking at spectra using spectroscopes (a piece of equipment for forming and looking at spectrum)', 'طیف بینوں (طیف بنانے اور دیکھنے کا آلہ) کے ذریعے طیف بنانے اور دیکھنے کا مطالعہ', 'د طیف‌بینونو (د طیف د جوړولو او کتلو وسیله) په کارولو د طیفونو د جوړولو او کتلو مطالعه'),
    ('tenuous(adj.)', 'so weak or uncertain that it hardly exists', 'اتنا کمزور یا غیر یقینی کہ مشکل سے موجود ہو', 'دومره کمزوری یا ناڅرګند چې په سختۍ شتون ولري'),
    ('transit(n)', 'the process of being moved or carried from one place to another', 'ایک جگہ سے دوسری جگہ منتقل یا لے جائے جانے کا عمل', 'له یوه ځایه بل ځای ته د لېږدول کېدو یا وړل کېدو بهیر'),
    ('turbulent(adj.)', 'in which there is a lot of sudden change, trouble, argument and sometimes violence', 'جس میں بہت سی اچانک تبدیلی، پریشانی، بحث اور کبھی تشدد ہو', 'چې پکې ډېر ناڅاپي بدلون، ستونزه، شخړه او کله کله تاوتریخوالی وي'),
    ('visceral(adj.)', 'resulting from strong feelings rather than careful thought', 'سوچے سمجھے خیال کے بجائے شدید جذبات کا نتیجہ', 'د پام وړ فکر پر ځای د قوي احساساتو پایله'),
])
gl = BOOK.record(g, 'eng12-u07-glossary-b', 'Glossary (2)', 'فرہنگ (2)', 'وییپانګه (2)', 41, [69])

q = Builder()
q.h('Reading Comprehension', 'مطالعہ اور فہم', 'لوستل او پوهه')
q.group('lines', [
    ("1. Why did the cosmologists need a telescope in space well above the Earth's atmosphere?", '1. ماہرینِ کونیات کو زمین کے کرۂ ہوائی سے بہت اوپر خلا میں دوربین کی ضرورت کیوں تھی؟', '1. کیهان‌پوهانو ولې د ځمکې له اتموسفیر ډېر پورته په فضا کې دوربین ته اړتیا درلوده؟'),
    ('2. What does the author mean by the sentence "when we look at stars we look at history"?', '2. مصنف کا جملے ’’جب ہم ستاروں کو دیکھتے ہیں تو تاریخ کو دیکھتے ہیں‘‘ سے کیا مطلب ہے؟', '2. د لیکوال مطلب له دې جملې "کله چې ستورو ته ګورو، تاریخ ته ګورو" څه دی؟'),
    ('3. Why will the life on,Earth not disturb even if our galaxy Milkyway colloids with its neighbouring Andromeda?', '3. اگر ہماری کہکشاں ملکی وے اپنی پڑوسی اینڈرومیڈا سے ٹکرا بھی جائے تو زمین پر زندگی کیوں متاثر نہیں ہو گی؟', '3. که زموږ کهکشان شیدې لار له خپل ګاونډي انډرومیډا سره ټکر هم وکړي، په ځمکه ژوند به ولې ګډوډ نه شي؟'),
    ('4. What is the Hubble Deep Field?', '4. ہبل ڈیپ فیلڈ کیا ہے؟', '4. د هبل ژور ډګر (Hubble Deep Field) څه دی؟'),
    ('5. How does the formation of stars take place in star nurseries?', '5. ستاروں کی نرسریوں میں ستارے کیسے بنتے ہیں؟', '5. د ستورو په روزنځیو کې ستوري څنګه جوړېږي؟'),
    ('6. How do scientists study the atmosphere of an exoplanet through "fingerprint" technique?', '6. سائنس دان ’’فنگر پرنٹ‘‘ تکنیک کے ذریعے کسی بیرونی سیارے کے کرۂ ہوائی کا مطالعہ کیسے کرتے ہیں؟', '6. ساینس‌پوهان د "ګوتو نښې" تخنیک له لارې د یوې بهرنۍ سیارې اتموسفیر څنګه څېړي؟'),
    ('7. How will you explain in astronomical terms the statement, "what you see is not always what you get"?', '7. آپ فلکیاتی اصطلاحات میں اس بیان کی وضاحت کیسے کریں گے کہ ’’جو آپ دیکھتے ہیں وہ ہمیشہ وہ نہیں ہوتا جو آپ پاتے ہیں‘‘؟', '7. تاسو به په ستورپوهنیزو اصطلاحاتو کې دا بیان څنګه تشریح کړئ: "هغه څه چې ګورئ تل هغه نه وي چې ترلاسه کوئ"؟'),
])
q.h('Writing Suggestions', 'تحریری تجاویز', 'د لیکلو وړاندیزونه')
q.h('A. Comparison and Contrast Essays', 'A. موازنہ اور تقابل کے مضامین', 'A. د پرتلې او توپیر مقالې')
q.p('A compare and contrast essay looks at the similarities and differences between two or more objects.', 'موازنے اور تقابل کا مضمون دو یا زیادہ اشیاء کے درمیان مماثلتوں اور فرق کا جائزہ لیتا ہے۔', 'د پرتلې او توپیر مقاله د دوو یا ډېرو شیانو ترمنځ ورته‌والي او توپیرونه څېړي.')
q.p('Methods for Organization: Compare and contrast essays are structured in two main ways.', 'ترتیب کے طریقے: موازنے اور تقابل کے مضامین دو بنیادی طریقوں سے ترتیب دیے جاتے ہیں۔', 'د تنظیم طریقې: د پرتلې او توپیر مقالې په دوو اصلي لارو جوړېږي.')
q.h('1. Block Structure', '1. بلاک ساخت', '1. بلاک جوړښت')
q.p('For the block structure, all information about one object being compared/contrasted is given first, and information about the other object is listed afterwards.', 'بلاک ساخت میں موازنہ/تقابل کی جانے والی ایک چیز کے بارے میں تمام معلومات پہلے دی جاتی ہیں اور دوسری چیز کے بارے میں معلومات بعد میں درج کی جاتی ہیں۔', 'په بلاک جوړښت کې د پرتله/توپیر کېدونکي یوه شي په اړه ټول معلومات لومړی ورکول کېږي، او د بل شي په اړه معلومات وروسته لیکل کېږي.')
BS = ['Introduction', 'Object 1 - Point 1', 'Object 1 - Point 2', 'Object 1 - Point 3', 'Transition sentence/paragraph', 'Object 2 - Point 1', 'Object 2 - Point 2', 'Object 2 - Point 3', 'Conclusion']
BU = ['تعارف', 'شے 1 — نکتہ 1', 'شے 1 — نکتہ 2', 'شے 1 — نکتہ 3', 'عبوری جملہ/پیراگراف', 'شے 2 — نکتہ 1', 'شے 2 — نکتہ 2', 'شے 2 — نکتہ 3', 'اختتامیہ']
BP = ['پېژندنه', 'شی 1 — ټکی 1', 'شی 1 — ټکی 2', 'شی 1 — ټکی 3', 'انتقالي جمله/پراګراف', 'شی 2 — ټکی 1', 'شی 2 — ټکی 2', 'شی 2 — ټکی 3', 'پایله']
q.table('eng12-u07-block', ['Block Structure'], [[x] for x in BS], ['بلاک ساخت'], ['بلاک جوړښت'], [[x] for x in BU], [[x] for x in BP])
qs = BOOK.record(q, 'eng12-u07-comprehension', 'Reading Comprehension; Writing — comparison and contrast (1)', 'مطالعہ اور فہم؛ تحریر — موازنہ اور تقابل (1)', 'لوستل او پوهه؛ لیکنه — پرتله او توپیر (1)', 41, [70])
issues = [{'id': 'eng12-p69-70', 'unit': 7, 'printedPage': 70, 'description': 'Printed text retained: Q3 “life on,Earth not disturb … Milkyway colloids” (collides), glossary “spectrum” for spectra; the block-structure diagram is reproduced as a one-column structured table.'}]

if __name__ == '__main__':
    BOOK.save(41, [(7, gl), (7, qs)], issues=issues)
