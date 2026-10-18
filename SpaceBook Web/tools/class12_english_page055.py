"""PDF55 (printed 97–98): Unit 10 Glossary (diminished … WEF); Reading Comprehension Q1–7; Writing — argumentative essay (introduction)."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
g = Builder()
gloss(g, 'eng12-u10-gloss-b', [
    ('diminished(adj.)', 'small : weakened.', 'چھوٹا؛ کمزور کیا ہوا۔', 'کوچنی؛ کمزوری شوی.'),
    ('detrimental(adj.)', 'fatal ; harmful.', 'مہلک؛ نقصان دہ۔', 'وژونکی؛ زیانمن.'),
    ('disparity(n)', 'inequality.', 'عدم مساوات۔', 'نابرابري.'),
    ('eventually (adv.)', 'finally.', 'آخرکار۔', 'په پای کې.'),
    ('impart(v)', 'transmit; translate.', 'منتقل کرنا؛ ترجمانی کرنا۔', 'لېږدول؛ ژباړل.'),
    ('intimate(adj.)', 'having very close relationship.', 'بہت قریبی تعلق رکھنے والا۔', 'ډېره نږدې اړیکه لرونکی.'),
    ('latent(adj.)', 'potentially existing.', 'ممکنہ طور پر موجود۔', 'په احتمالي ډول شته.'),
    ('manifest(v)', 'demonstrate.', 'ظاہر کرنا۔', 'ښکاره کول.'),
    ('mortality(n)', 'death rate.', 'شرحِ اموات۔', 'د مړینې کچه.'),
    ('ongoing(adj.)', 'currently happening.', 'جاری۔', 'روان.'),
    ('offsprings(n)', 'children.', 'اولاد۔', 'اولاد.'),
    ('persistent(adj.)', 'continual; never-ending.', 'مسلسل؛ نہ ختم ہونے والا۔', 'دوامداره؛ نه ختمېدونکی.'),
    ('plague(v)', 'cause to suffer or inflict.', 'تکلیف میں مبتلا کرنا۔', 'ځورول یا ربړول.'),
    ('pinnacle(n)', 'The most successful point, the culmination.', 'سب سے کامیاب مقام، انتہا۔', 'تر ټولو بریالی ټکی، اوج.'),
    ('patriarchal(adj.)', 'Relating to or denoting a system of society control by men.', 'مردوں کے زیرِ کنٹرول معاشرتی نظام سے متعلق یا اسے ظاہر کرنے والا۔', 'د نارینه وو تر کنټرول لاندې ټولنیز نظام پورې اړوند یا ښوونکی.'),
    ('pedestal(n)', 'position ; standing.', 'مقام؛ حیثیت۔', 'ځای؛ حیثیت.'),
    ('potentialities(n)', 'capabilities.', 'صلاحیتیں۔', 'وړتیاوې.'),
    ('parity (n)', 'equality.', 'برابری۔', 'برابري.'),
    ('render(v)', 'provide; cause to become.', 'فراہم کرنا؛ بنا دینا۔', 'برابرول؛ بدلول.'),
    ('swara(n)', 'Swara (سوارہ), is a custom found in parts of county where girls, often minors, are given in marriage or servitude to an aggrieved family as compensation to end disputes, often murder.', 'سوارہ ملک کے بعض حصوں میں پائی جانے والی ایک رسم ہے جس میں لڑکیوں کو، اکثر نابالغ، تنازعات — اکثر قتل — ختم کرنے کے معاوضے کے طور پر متاثرہ خاندان کو نکاح یا غلامی میں دے دیا جاتا ہے۔', 'سوره د هېواد په ځینو برخو کې یو دود دی چې پکې نجونې، اکثرا نابالغې، د شخړو — اکثرا وژنې — د پای ته رسولو د جبران په توګه زیانمنې کورنۍ ته په واده یا غلامۍ کې ورکول کېږي.'),
    ('WEF', 'World Economic Forum', 'عالمی اقتصادی فورم', 'نړیوال اقتصادي فورم'),
])
gl = BOOK.record(g, 'eng12-u10-glossary-b', 'Glossary (2)', 'فرہنگ (2)', 'وییپانګه (2)', 55, [97])

q = Builder()
q.h('Reading Comprehension', 'مطالعہ اور فہم', 'لوستل او پوهه')
q.group('lines', [
    ('1. Do you agree or disagree with the views of the writer as stated in the third paragraph of the text?', '1. کیا آپ متن کے تیسرے پیراگراف میں بیان کردہ مصنف کے خیالات سے متفق ہیں یا نہیں؟', '1. ایا د متن په درېیم پراګراف کې د لیکوال له بیان شویو نظرونو سره موافق یاست که مخالف؟'),
    ('2. Give a brief account of the plight of women in Pakistan with respect to their healthcare issues.', '2. صحت کے مسائل کے حوالے سے پاکستان میں عورتوں کی حالتِ زار کا مختصر احوال دیں۔', '2. د روغتیایي مسایلو په اړه په پاکستان کې د ښځو د بدې ورځې لنډ حال ووایاست.'),
    ('3. What factors are responsible for the economic backwardness of women in Pakistan?', '3. پاکستان میں عورتوں کی معاشی پسماندگی کے کون سے عوامل ذمہ دار ہیں؟', '3. په پاکستان کې د ښځو د اقتصادي وروسته‌پاتې‌والي لپاره کوم عوامل مسؤل دي؟'),
    ("4. What does Islam say about women's rights? Explain your answer in the light of Qur'an and Hadith.", '4. اسلام عورتوں کے حقوق کے بارے میں کیا کہتا ہے؟ اپنے جواب کی قرآن و حدیث کی روشنی میں وضاحت کریں۔', '4. اسلام د ښځو د حقونو په اړه څه وايي؟ خپل ځواب د قرآن او حدیث په رڼا کې تشریح کړئ.'),
    ('5. State any incidence of gender inequality in any sector which you have ever observed in your immediate surrounding.', '5. کسی بھی شعبے میں صنفی عدم مساوات کا کوئی واقعہ بیان کریں جو آپ نے اپنے قریبی ماحول میں کبھی دیکھا ہو۔', '5. په هره برخه کې د جنسیتي نابرابرۍ کومه پېښه بیان کړئ چې تاسو په خپل نږدې چاپېریال کې لیدلې وي.'),
    ('6. What seems to be the motive behind writing this text?', '6. اس متن کو لکھنے کے پیچھے کیا مقصد نظر آتا ہے؟', '6. د دې متن د لیکلو تر شا موخه څه ښکاري؟'),
    ('7. What would you suggest for the eradication of gender inequality?', '7. آپ صنفی عدم مساوات کے خاتمے کے لیے کیا تجویز کریں گے؟', '7. تاسو به د جنسیتي نابرابرۍ د له منځه وړلو لپاره څه وړاندیز کړئ؟'),
])
q.h('Writing Suggestions', 'تحریری تجاویز', 'د لیکلو وړاندیزونه')
q.h('What is an argumentative essay?', 'استدلالی مضمون کیا ہے؟', 'استدلالي مقاله څه ده؟')
q.p("In this type of essay, the writer establishes a stance or position on an issue by providing reasons and supporting evidence. when writing an argumentative (persuasive) essay, you need more than just an opinion to make your point of view accepted by the reader. Even the strongest stance won't be compelling if it is structured improperly and not backed up with solid reason in an evidence.",
    'اس قسم کے مضمون میں مصنف وجوہات اور معاون شواہد فراہم کر کے کسی مسئلے پر اپنا موقف یا مؤقف قائم کرتا ہے۔ استدلالی (ترغیبی) مضمون لکھتے وقت اپنا نقطۂ نظر قاری سے منوانے کے لیے آپ کو محض رائے سے زیادہ کی ضرورت ہوتی ہے۔ مضبوط ترین موقف بھی قائل کرنے والا نہیں ہو گا اگر اسے غلط طریقے سے ترتیب دیا جائے اور ٹھوس دلیل اور شواہد سے اس کی تائید نہ ہو۔',
    'په دې ډول مقاله کې لیکوال د دلیلونو او ملاتړي شواهدو په وړاندې کولو په یوه مسئله خپل دریځ یا موقف ټاکي. د استدلالي (هڅوونکې) مقالې د لیکلو پر مهال، د لوستونکي له خوا د خپل لیدلوري د منلو لپاره له یوازې نظر څخه ډېر څه ته اړتیا لرئ. حتی تر ټولو قوي دریځ به قانع کوونکی نه وي که په سمه توګه جوړ نه شي او په قوي دلیل او شواهدو ملاتړ نه شي.')
q.h('Structure of an argumentative essay:', 'استدلالی مضمون کی ساخت:', 'د استدلالي مقالې جوړښت:')
q.p('Introduction: Give such an opening statement through which you grab the attention or hook the reader. You can start with a surprising statistical figure that is not commonly known within the field. Next, provide a background on your topic to prepare the readers for the rest of your essay. You may engage the reader by answering questions like',
    'تعارف: ایسا ابتدائی بیان دیں جس کے ذریعے آپ قاری کی توجہ حاصل کریں یا اسے اپنی طرف کھینچیں۔ آپ کسی حیران کن شماریاتی عدد سے آغاز کر سکتے ہیں جو اس شعبے میں عام طور پر معلوم نہ ہو۔ اس کے بعد اپنے موضوع کا پس منظر دیں تاکہ قارئین باقی مضمون کے لیے تیار ہوں۔ آپ ایسے سوالات کے جواب دے کر قاری کو مشغول کر سکتے ہیں جیسے',
    'پېژندنه: داسې پیلنی بیان ورکړئ چې د لوستونکي پام راواړوي یا یې ځانته راکاږي. کولی شئ په یوه حیرانوونکې احصاییوي شمېرې پیل وکړئ چې په هغه برخه کې عموماً نه وي پېژندل شوې. وروسته د خپلې موضوع شالید وړاندې کړئ ترڅو لوستونکي د مقالې پاتې برخې ته چمتو شي. تاسو کولی شئ د داسې پوښتنو په ځوابولو لوستونکی بوخت کړئ لکه')
q.group('list', [('Why is the this issue important?', 'یہ مسئلہ کیوں اہم ہے؟', 'دا مسئله ولې مهمه ده؟'), ('What are the root causes of this problem?', 'اس مسئلے کی بنیادی وجوہات کیا ہیں؟', 'د دې ستونزې رېښه‌ییز لاملونه کوم دي؟'),
                 ('What is affected?', 'کیا متاثر ہوتا ہے؟', 'څه اغېزمن کېږي؟'), ('Are there any solutions available?', 'کیا کوئی حل موجود ہیں؟', 'ایا کوم حلونه شته؟')])
q.p('For example, if the topic is gender inequality in the workplace you can share statistics from a research that exemplifies the difference in income of the average men and women who perform the same role.', 'مثال کے طور پر اگر موضوع کام کی جگہ پر صنفی عدم مساوات ہو تو آپ کسی تحقیق کے اعداد و شمار پیش کر سکتے ہیں جو ایک ہی کام کرنے والے اوسط مرد و عورت کی آمدنی کا فرق واضح کرے۔', 'د بېلګې په توګه که موضوع د کار په ځای کې جنسیتي نابرابري وي، کولی شئ د یوې څېړنې احصاییې شریکې کړئ چې د یو شان رول ترسره کوونکو منځنیو نارینه او ښځو د عاید توپیر ښيي.')
qs = BOOK.record(q, 'eng12-u10-comprehension', 'Reading Comprehension; Writing — argumentative essay (1)', 'مطالعہ اور فہم؛ تحریر — استدلالی مضمون (1)', 'لوستل او پوهه؛ لیکنه — استدلالي مقاله (1)', 55, [98])
issues = [{'id': 'eng12-p97-98', 'unit': 10, 'printedPage': 97, 'description': 'Printed text retained: glossary “parts of county” (country), “society control by men”, “impart … translate”; writing “when writing” (lower-case), “solid reason in an evidence”, “Why is the this issue important?”.'}]

if __name__ == '__main__':
    BOOK.save(55, [(10, gl), (10, qs)], issues=issues)
