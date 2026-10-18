"""PDF17 (printed 21–22): Unit 2 Glossary (legislature … vision); Reading Comprehension Q1–10; Oral Communication; Writing Suggestions — introductory paragraph (start)."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
GL = [
    ('legislature (n)', 'A body of persons (the parliament) vested with the power to make, amend and repeal laws for the state;', 'افراد کا وہ ادارہ (پارلیمنٹ) جسے ریاست کے لیے قوانین بنانے، ترمیم کرنے اور منسوخ کرنے کا اختیار ہو؛', 'د کسانو هغه ارګان (پارلمان) چې د دولت لپاره د قوانینو د جوړولو، تعدیلولو او لغوه کولو واک لري؛'),
    ('liberal (ad).)', 'Relating to or having social and political views that favour progress and reform; advocating individual freedom; generous in temperament and behaviour; tolerant of the views of others', 'ترقی اور اصلاح کے حامی سماجی و سیاسی نظریات سے متعلق یا ان کا حامل؛ انفرادی آزادی کا حامی؛ مزاج اور رویے میں فراخ دل؛ دوسروں کی آراء کو برداشت کرنے والا', 'له داسې ټولنیزو او سیاسي نظرونو سره تړلی یا د هغو لرونکی چې د پرمختګ او اصلاح ملاتړ کوي؛ د فردي ازادۍ پلوی؛ په مزاج او چلند کې سخاوتمند؛ د نورو نظرونو زغمونکی'),
    ('nepotism (n)', 'Favouritism shown to relatives or close friends by those with power or influence', 'طاقت یا اثر و رسوخ رکھنے والوں کی طرف سے رشتہ داروں یا قریبی دوستوں کی طرف داری', 'د واک یا نفوذ لرونکو له خوا خپلوانو یا نږدې ملګرو ته طرفداري'),
    ('obligation (n)', 'A moral or legal requirement; duty; agreement, bond, commitment; promise;', 'اخلاقی یا قانونی تقاضا؛ فرض؛ معاہدہ، بندھن، عہد؛ وعدہ؛', 'اخلاقي یا قانوني اړتیا؛ دنده؛ تړون، تړاو، ژمنه؛ وعده؛'),
    ('onerous (adj.)', 'laborious or oppressive; burdensome, demanding, difficult;', 'محنت طلب یا جابرانہ؛ بوجھل، کٹھن، مشکل؛', 'ستړی کوونکی یا ځپونکی؛ دروند، غوښتونکی، سخت؛'),
    ('privileges (n)', 'Fundamental rights guaranteed to the citizens of a country by its constitution; a benefit or immunity granted in certain conditions;', 'کسی ملک کے آئین کی طرف سے اس کے شہریوں کو ضمانت شدہ بنیادی حقوق؛ بعض حالات میں دی گئی سہولت یا استثنا؛', 'هغه بنسټیز حقونه چې د یوه هېواد اساسي قانون یې اتباعو ته تضمینوي؛ په ځینو شرایطو کې ورکړل شوې ګټه یا معافیت؛'),
    ('pronouncement (n)', 'An official or authoritative statement or announcement', 'سرکاری یا مستند بیان یا اعلان', 'رسمي یا باواکه بیان یا اعلان'),
    ('secular (adj.)', 'Of or related to worldly things as opposed to the sacred; not concerned with or related to religion; not within the control of the church/religion', 'مقدس کے برعکس دنیاوی چیزوں سے متعلق؛ مذہب سے غیر متعلق؛ کلیسا/مذہب کے اختیار سے باہر', 'د سپیڅلو پر خلاف له دنیوي شیانو سره تړلی؛ له دین سره نه تړلی؛ د کلیسا/دین له واک بهر'),
    ('sovereign (adj.)', 'Supreme in rank or authority; absolute; chief; dominant;', 'رتبے یا اختیار میں اعلیٰ ترین؛ مطلق؛ اہم ترین؛ غالب؛', 'په رتبه یا واک کې تر ټولو لوړ؛ مطلق؛ مشر؛ غالب؛'),
    ('subjection (n)', 'The act/process of bringing under control or authority;', 'قابو یا اختیار میں لانے کا عمل؛', 'تر کنټرول یا واک لاندې راوستلو کړنه/بهیر؛'),
    ('temple (n)', 'Hindu place of worship; a building or place dedicated to worship of a deity or deities;', 'ہندو عبادت گاہ؛ کسی دیوتا یا دیوتاؤں کی پوجا کے لیے مخصوص عمارت یا جگہ؛', 'د هندوانو عبادتځای؛ هغه ودانۍ یا ځای چې د یوه یا ډېرو خدایانو عبادت ته ځانګړی وي؛'),
    ('titanic (ad),)', 'Huge; colossal; enormous; gigantic; massive', 'بہت بڑا؛ عظیم الجثہ؛ بے پناہ؛ دیو ہیکل؛ بھاری', 'ډېر لوی؛ ستر؛ بې‌اندازې؛ دیو ډوله؛ دروند'),
    ('to advocate (v)', 'To support or recommend publicly; plead for or speak in favour of', 'سرِعام حمایت یا سفارش کرنا؛ کسی کے حق میں دلیل دینا یا بولنا', 'په ښکاره ملاتړ یا سپارښتنه کول؛ د یو څه په ګټه دلیل ویل یا خبرې کول'),
    ('to bury the hatchet', 'To cease hostilities and become reconciled or friends,', 'دشمنی ختم کر کے صلح کر لینا یا دوست بن جانا،', 'دښمني پای ته رسول او روغه کول یا ملګري کېدل،'),
    ('to countenance (v)', 'To support or encourage; to sanction, to tolerate, to endure;', 'حمایت یا حوصلہ افزائی کرنا؛ منظوری دینا، برداشت کرنا، سہنا؛', 'ملاتړ یا هڅونه کول؛ اجازه ورکول، زغمل، تېرول؛'),
    ('to vanish (v)', 'To disappear, esp. suddenly or mysteriously; fade away', 'غائب ہو جانا، خاص طور پر اچانک یا پراسرار طریقے سے؛ مٹ جانا', 'ورکېدل، په ځانګړي ډول ناڅاپه یا په پراسرار ډول؛ له منځه تلل'),
    ('unavoidable (adj.)', 'That which cannot be avoided; inevitable; certain; inescapable', 'جس سے بچا نہ جا سکے؛ ناگزیر؛ یقینی؛ لازمی', 'هغه چې ترې ډډه نه شي کېدای؛ ناګزیر؛ حتمي؛ نه تېښته کېدونکی'),
    ('unprecedented(adj.)', 'Having no precedent; unparalleled; exceptional; extraordinary; unrivalled', 'جس کی کوئی نظیر نہ ہو؛ بے مثال؛ استثنائی؛ غیر معمولی؛ بے مقابلہ', 'چې ساری یې نه وي؛ بې‌مثاله؛ استثنایي؛ غیرعادي؛ بې‌سیاله'),
    ('utmost (adj.)', 'Of the greatest possible degree or amount', 'ممکنہ حد تک سب سے زیادہ درجے یا مقدار کا', 'د امکان تر ټولو لوړې درجې یا اندازې'),
    ('verdict (n)', 'A decision; judgment or conclusion;', 'فیصلہ؛ رائے یا نتیجہ؛', 'پرېکړه؛ قضاوت یا پایله؛'),
    ('vision (n)', 'The act, faculty or an instance of great perception, esp. of future development; farsightedness; foresight; insight intuition', 'گہرے ادراک کا عمل، صلاحیت یا مثال، خاص طور پر مستقبل کی ترقی کا؛ دور اندیشی؛ پیش بینی؛ بصیرت، وجدان', 'د ژور درک کړنه، وړتیا یا بېلګه، په ځانګړي ډول د راتلونکي پرمختګ؛ لرلید؛ وړاندوینه؛ بصیرت، وجدان'),
]
g = Builder()
gloss(g, 'eng12-u02-gloss-b', GL)
gl = BOOK.record(g, 'eng12-u02-glossary-b', 'Glossary (2)', 'فرہنگ (2)', 'وییپانګه (2)', 17, [21])

q = Builder()
q.h('Reading Comprehension', 'مطالعہ اور فہم', 'لوستل او پوهه')
q.group('lines', [
    ('1. What were the two main functions of the first constituent assembly of Pakistan as mentioned by Muhammad Ali Jinnah in his speech?', '1. محمد علی جناح نے اپنی تقریر میں پاکستان کی پہلی دستور ساز اسمبلی کے کون سے دو اہم فرائض بیان کیے؟', '1. محمد علي جناح په خپله وینا کې د پاکستان د لومړۍ اساسي اسمبلۍ کومې دوه مهمې دندې یادې کړې؟'),
    ("2. What is 'the unprecedented cyclonic revolution' which Quaid e Azam has talked about in his speech? Why did he call it as unprecedented?", '2. وہ ’’بے مثال طوفانی انقلاب‘‘ کیا ہے جس کا قائدِ اعظم نے اپنی تقریر میں ذکر کیا؟ انہوں نے اسے بے مثال کیوں کہا؟', '2. هغه "بې‌ساری توپاني انقلاب" څه دی چې قائد اعظم په خپله وینا کې یاد کړ؟ ولې یې بې‌ساری وباله؟'),
    ('3. How did Quaid e Azam Muhammad Ali Jinnah express his feelings about bribery, corruption and nepotism and jobbery ?', '3. قائدِ اعظم محمد علی جناح نے رشوت، بدعنوانی، اقربا پروری اور سفارش بازی کے بارے میں اپنے جذبات کا اظہار کیسے کیا؟', '3. قائد اعظم محمد علي جناح د رشوت، فساد، خپلوي‌پالنې او سپارښتنه‌بازۍ په اړه خپل احساسات څنګه څرګند کړل؟'),
    ("4. What were Muhammad Ali Jinnah's views about the partition of of India? Describe in a few lines.", '4. تقسیمِ ہند کے بارے میں محمد علی جناح کے کیا خیالات تھے؟ چند سطروں میں بیان کریں۔', '4. د هند د وېش په اړه د محمد علي جناح نظرونه څه وو؟ په څو کرښو کې یې بیان کړئ.'),
    ('5. What, in the eyes of the Quaid , was the the biggest hindrance in the way of India to attain freedom of the foreign occupation?', '5. قائد کی نظر میں غیر ملکی قبضے سے آزادی حاصل کرنے کی راہ میں ہندوستان کی سب سے بڑی رکاوٹ کیا تھی؟', '5. د قائد په اند، له بهرني اشغال څخه د ازادۍ د ترلاسه کولو په لار کې د هند تر ټولو لوی خنډ څه و؟'),
    ("6. Describe Quaid e Azam's views about the minorities as expressed in his address to the first constituent assembly.", '6. پہلی دستور ساز اسمبلی سے اپنے خطاب میں اقلیتوں کے بارے میں قائدِ اعظم کے بیان کردہ خیالات بیان کریں۔', '6. لومړۍ اساسي اسمبلۍ ته په خپله وینا کې د اقلیتونو په اړه د قائد اعظم څرګند شوي نظرونه بیان کړئ.'),
    ('7. What kind of freedom did Muhammad Ali Jinnah envision for the people of Pakistan in general?', '7. محمد علی جناح نے عمومی طور پر پاکستان کے لوگوں کے لیے کس قسم کی آزادی کا تصور کیا؟', '7. محمد علي جناح په عمومي ډول د پاکستان د خلکو لپاره څه ډول ازادي په پام کې نیولې وه؟'),
    ('8. What did Muhammad Ali Jinnah mean by "Hindus would cease to be Hindus and Muslims would cease to be Muslims"?', '8. محمد علی جناح کا ’’ہندو، ہندو نہیں رہیں گے اور مسلمان، مسلمان نہیں رہیں گے‘‘ سے کیا مطلب تھا؟', '8. د محمد علي جناح مطلب له "هندوان به هندوان پاتې نه شي او مسلمانان به مسلمانان پاتې نه شي" څخه څه و؟'),
    ('9. After reading this important speech of the Quaid e Azam Muhammad Ali Jinnah, what do you think, was his vision of Pakistan?', '9. قائدِ اعظم محمد علی جناح کی یہ اہم تقریر پڑھنے کے بعد آپ کے خیال میں پاکستان کے بارے میں ان کا تصور کیا تھا؟', '9. د قائد اعظم محمد علي جناح د دې مهمې وینا تر لوستلو وروسته ستاسو په اند د پاکستان په اړه د هغه لید څه و؟'),
    ('10. Read the last paragraph of this speech and state as to what were the guiding principles of the Quaid-e-Azam Muhammad Ali Jinnah. Also, elaborate the significance of these principles.', '10. اس تقریر کا آخری پیراگراف پڑھیں اور بتائیں کہ قائدِ اعظم محمد علی جناح کے رہنما اصول کیا تھے۔ ان اصولوں کی اہمیت کی بھی وضاحت کریں۔', '10. د دې وینا وروستی پراګراف ولولئ او ووایاست چې د قائد اعظم محمد علي جناح لارښود اصول کوم وو. د دې اصولو اهمیت هم تشریح کړئ.'),
])
q.h('Oral Communication', 'زبانی ابلاغ', 'د خولې اړیکه')
q.p('Make two groups of the students and arrange a debate on the topic" What type of Pakistan did Quaid e Azam want?"', 'طلبہ کے دو گروہ بنائیں اور ’’قائدِ اعظم کس قسم کا پاکستان چاہتے تھے؟‘‘ کے موضوع پر مباحثے کا اہتمام کریں۔', 'د زده کوونکو دوه ډلې جوړې کړئ او د "قائد اعظم څه ډول پاکستان غوښته؟" په موضوع یو مباحثه جوړه کړئ.')
q.h('Writing Suggestions', 'تحریری تجاویز', 'د لیکلو وړاندیزونه')
q.h('Writing an introductory paragraph:', 'تعارفی پیراگراف لکھنا:', 'د پیلني پراګراف لیکل:')
q.p('The primary purpose of an introductory paragraph is to grab the interest of the reader and identify the topic and purpose of the essay. It is the beginning of an essay and does the same job for an essay as a topic sentence does for a paragraph. It tells the reader what the subject of the essay will be and how it will be developed.',
    'تعارفی پیراگراف کا بنیادی مقصد قاری کی دلچسپی حاصل کرنا اور مضمون کے موضوع اور مقصد کی نشاندہی کرنا ہے۔ یہ مضمون کا آغاز ہے اور مضمون کے لیے وہی کام کرتا ہے جو پیراگراف کے لیے موضوعی جملہ کرتا ہے۔ یہ قاری کو بتاتا ہے کہ مضمون کا موضوع کیا ہو گا اور اسے کیسے آگے بڑھایا جائے گا۔',
    'د پیلني پراګراف اصلي موخه د لوستونکي پام ځانته اړول او د مقالې د موضوع او موخې پېژندل دي. دا د مقالې پیل دی او مقالې ته هماغه کار کوي چې موضوعي جمله یې پراګراف ته کوي. لوستونکي ته وايي چې د مقالې موضوع به څه وي او څنګه به پراختیا ومومي.')
rc = BOOK.record(q, 'eng12-u02-comprehension', 'Reading Comprehension; Oral Communication; Writing an introductory paragraph', 'مطالعہ اور فہم؛ زبانی ابلاغ؛ تعارفی پیراگراف', 'لوستل او پوهه؛ د خولې اړیکه؛ پیلنی پراګراف', 17, [22])
issues = [{'id': 'eng12-p21-22-typos', 'unit': 2, 'printedPage': 22, 'description': 'Printed text retained: glossary word classes “(ad).)”, “(ad),)”; questions print “partition of of India”, “the the biggest hindrance”, “freedom of the foreign occupation”, “call it as unprecedented”.'}]

if __name__ == '__main__':
    BOOK.save(17, [(2, gl), (2, rc)], issues=issues)
