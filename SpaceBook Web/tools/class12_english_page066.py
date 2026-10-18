"""PDF66 (printed 119–120): Unit 13 opener 'Technical Education' outcomes; reading text (board-authored essay) start."""
from class12_book_common import Book, Builder

BOOK = Book('english')
UT = ('Technical Education', 'فنی تعلیم', 'تخنیکي زده کړه')
o = Builder()
o.h('Unit 13 — Technical Education', 'یونٹ 13 — فنی تعلیم', 'واحد 13 — تخنیکي زده کړه')
o.p('By the end of the unit, the students will be able to:', 'اس یونٹ کے اختتام تک طلبہ اس قابل ہوں گے کہ:', 'د دې واحد په پای کې به زده کوونکي وکولای شي چې:')
o.group('list', [
    ('Use pre-reading strategies to predict the content of a text from topic / picture, title / headings, key words and visuals etc. by using prior knowledge, asking questions and contextual clues.', 'سابقہ علم، سوالات اور سیاقی اشاروں کو استعمال کرتے ہوئے موضوع / تصویر، عنوان / سرخیوں، کلیدی الفاظ اور بصری مواد وغیرہ سے متن کے مواد کی پیش گوئی کے لیے مطالعے سے پہلے کی حکمتِ عملیاں استعمال کریں۔', 'د مخکینۍ پوهې، پوښتنو او شرایطي نښو په کارولو د موضوع / انځور، سرلیک / سرټکو، کلیدي کلمو او لیدنیزو موادو څخه د متن د منځپانګې د وړاندوینې لپاره د لوستلو مخکې ستراتیژۍ وکاروي.'),
    ('Skim text to: have general idea of the text; infer theme/ main idea.', 'متن پر سرسری نظر ڈالیں تاکہ: متن کا عمومی اندازہ ہو؛ موضوع/ مرکزی خیال اخذ کریں۔', 'په متن سرسري نظر واچوي ترڅو: د متن عمومي مفکوره ولري؛ موضوع/ اصلي مفکوره استنباط کړي.'),
    ('Apply critical thinking to interact with text, use intensive reading strategies (while-reading) to scan to answer short questions.', 'متن سے تعامل کے لیے تنقیدی سوچ کا اطلاق کریں، گہرے مطالعے کی حکمتِ عملیاں (دورانِ مطالعہ) استعمال کریں تاکہ مختصر سوالات کے جواب کے لیے متن میں تلاش کریں۔', 'له متن سره د تعامل لپاره انتقادي فکر پلي کړي، د ژورو لوستلو ستراتیژۍ (د لوستلو پر مهال) وکاروي ترڅو د لنډو پوښتنو د ځوابولو لپاره متن ولټوي.'),
    ('Write a persuasive/argumentative essay on a given topic to: state an opinion on the topic; list ideas and arguments that support opinion.', 'دیے گئے موضوع پر ترغیبی/استدلالی مضمون لکھیں تاکہ: موضوع پر رائے بیان کریں؛ رائے کی تائید کرنے والے خیالات اور دلائل کی فہرست بنائیں۔', 'په ورکړل شوې موضوع یوه هڅوونکې/استدلالي مقاله ولیکي ترڅو: په موضوع نظر بیان کړي؛ د نظر د ملاتړ نظرونه او دلیلونه لست کړي.'),
    ('Analyze passages in the text to identify the theme/ general subject, key idea/ central thought (a statement about the general subject) and supporting details.', 'متن کے اقتباسات کا تجزیہ کر کے موضوع/ عمومی مضمون، کلیدی خیال/ مرکزی سوچ (عمومی مضمون کے بارے میں ایک بیان) اور معاون تفصیلات کی نشاندہی کریں۔', 'د متن برخې تحلیل کړي ترڅو موضوع/ عمومي مضمون، کلیدي نظر/ مرکزي فکر (د عمومي مضمون په اړه یو بیان) او ملاتړي جزییات وپېژني.'),
    ('Recognize that the theme of a text is carried in a thesis statement.', 'پہچانیں کہ متن کا موضوع مرکزی دعوے میں بیان ہوتا ہے۔', 'وپېژني چې د متن موضوع د تیسس په بیان کې راځي.'),
    ('Use various reference sources for interpersonal, academic and workplace situation including figurative, idiomatic and technical vocabulary.', 'باہمی، تعلیمی اور کام کی جگہ کے حالات کے لیے مجازی، محاوراتی اور تکنیکی ذخیرۂ الفاظ سمیت مختلف حوالہ جاتی ذرائع استعمال کریں۔', 'د متقابلو، تعلیمي او د کار ځای حالاتو لپاره د مجازي، محاوره‌ییزو او تخنیکي لغاتو په ګډون بېلابېلې مرجع سرچینې وکاروي.'),
    ('Identify, analyze and construct conditional sentences.', 'شرطیہ جملوں کی نشاندہی، تجزیہ اور تشکیل کریں۔', 'شرطي جملې وپېژني، تحلیل او جوړې کړي.'),
    ('Analyze and construct simple, compound and complex sentences.', 'سادہ، مرکب اور پیچیدہ جملوں کا تجزیہ اور تشکیل کریں۔', 'ساده، مرکبې او پېچلې جملې تحلیل او جوړې کړي.'),
])
op = BOOK.record(o, 'eng12-u13-outcomes', 'Unit 13 — learning outcomes', 'یونٹ 13 — تعلیمی نتائج', 'واحد 13 — د زده کړې پایلې', 66, [119], unit_title=UT)

r = Builder()
r.h('Technical Education', 'فنی تعلیم', 'تخنیکي زده کړه')
r.p('[Summary — the reading text is a 2018 newspaper article by Frank F. Islam (Daily Times, 8 December 2018), a modern copyrighted text; read it in the printed textbook, pp. 120–123.]', '[خلاصہ — یہ متن فرینک ایف اسلام کا 2018 کا اخباری مضمون (ڈیلی ٹائمز، 8 دسمبر 2018) ہے جو جدید کاپی رائٹ شدہ متن ہے؛ اسے درسی کتاب کے صفحات 120–123 میں پڑھیں۔]', '[لنډیز — دا متن د فرانک ایف اسلام د 2018 کال ورځپاڼې مقاله (ډیلي ټایمز، د 2018 د ډسمبر 8) ده چې نوی د کاپي رایټ لاندې متن دی؛ په چاپي درسي کتاب کې یې په 120–123 مخونو کې ولولئ.]')
P = [
    ('A skilled, well-trained workforce is the key to economic growth. Pakistan is passing through a demographic transition, and investing in the education and training of its young people would let it reap the “demographic dividend”; this needs political commitment and adequate funding for human-resource development.',
     'ہنرمند اور اچھی تربیت یافتہ افرادی قوت معاشی ترقی کی کلید ہے۔ پاکستان آبادیاتی تبدیلی کے دور سے گزر رہا ہے اور اپنے نوجوانوں کی تعلیم و تربیت پر سرمایہ کاری سے ’’آبادیاتی فائدہ‘‘ حاصل کر سکتا ہے؛ اس کے لیے سیاسی عزم اور انسانی وسائل کی ترقی کے لیے مناسب فنڈز درکار ہیں۔',
     'ماهر او ښه روزل شوی کاري ځواک د اقتصادي ودې کیلي ده. پاکستان د نفوسي بدلون له پړاو تېرېږي، او د خپلو ځوانانو په زده کړه او روزنه کې پانګونه یې کولی شي "نفوسي ګټه" ترلاسه کړي؛ دا سیاسي ژمنې او د بشري سرچینو د پراختیا لپاره کافي بودیجې ته اړتیا لري.'),
    ('Pakistan has the largest young generation in its history — about 64 per cent of its people are under thirty — which brings both challenges and opportunities; the country’s future depends on a strategy to educate this “youth bulge” and use its potential.',
     'پاکستان میں اپنی تاریخ کی سب سے بڑی نوجوان نسل ہے — تقریباً 64 فیصد لوگ تیس سال سے کم عمر ہیں — جو چیلنج بھی ہے اور موقع بھی؛ ملک کا مستقبل اس ’’نوجوانوں کی بہتات‘‘ کو تعلیم دینے اور اس کی صلاحیت سے فائدہ اٹھانے کی حکمتِ عملی پر منحصر ہے۔',
     'پاکستان په خپل تاریخ کې تر ټولو لوی ځوان نسل لري — شاوخوا 64 سلنه خلک له دېرشو کلونو کم عمر لري — چې ننګونې او فرصتونه دواړه راوړي؛ د هېواد راتلونکی د دې "د ځوانانو ډېروالي" د زده کړې او د هغوی له وړتیا د ګټې اخیستو په ستراتیژۍ پورې اړه لري.'),
    ('The technical and vocational education and training (TVET) system faces problems of access, quality, equity and relevance: about three million young people enter the job market each year, but its 3,500-plus institutes train fewer than half a million, and many graduates still lack the skills the market wants.',
     'فنی و پیشہ ورانہ تعلیم و تربیت (ٹی ویٹ) کا نظام رسائی، معیار، مساوات اور مطابقت کے مسائل کا شکار ہے: ہر سال تقریباً تیس لاکھ نوجوان روزگار کی منڈی میں آتے ہیں، لیکن اس کے 3500 سے زیادہ ادارے پانچ لاکھ سے کم کو تربیت دیتے ہیں، اور بہت سے فارغ التحصیل افراد کے پاس اب بھی منڈی کی مطلوبہ مہارتیں نہیں ہوتیں۔',
     'د تخنیکي او مسلکي زده کړې او روزنې (TVET) سیسټم د لاسرسي، کیفیت، عدالت او سمون له ستونزو سره مخ دی: هر کال شاوخوا درې میلیونه ځوانان د دندو بازار ته راځي، خو د هغه له 3500 زیات بنسټونه له نیم میلیون کم روزي، او ډېری فارغان لا هم هغه مهارتونه نه لري چې بازار یې غواړي.'),
]
for x in P: r.p(*x)
rd = BOOK.record(r, 'eng12-u13-text-a', 'Reading text — summary (1)', 'متن — خلاصہ (1)', 'متن — لنډیز (1)', 66, [120])
rd['sourceCoverIllustrationReview'] = 'Hexagon icon graphic (technical trades) is decorative; not reproduced.'
rd['sourceGap'] = 'Modern copyrighted newspaper article (Frank F. Islam, Daily Times, 8 Dec 2018); paragraph-wise summary, not verbatim. Printed pp. 120–123.'
issues = [{'id': 'eng12-p120', 'unit': 13, 'printedPage': 120, 'description': 'Printed text retained: “at the crossroads of the history”, “let them go wasted”, “investment with the purpose of education”, “capitalize the demographic dividends”.'}]

if __name__ == '__main__':
    BOOK.save(66, [(13, op), (13, rd)], issues=issues)
