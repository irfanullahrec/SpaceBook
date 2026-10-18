"""PDF119 (printed 225–226): Lord of the Flies glossary savage–whoop; Reading Comprehension 1–21; Writing Suggestions 1–2."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
g = Builder()
gloss(g, 'eng12-u19-gloss-c', [
    ('savage(n)', 'an uncivilized person.', 'غیر مہذب شخص۔', 'نامتمدن کس.'),
    ('sneak(v)', 'move stealthily', 'چپکے سے حرکت کرنا', 'په پټه حرکت کول'),
    ("summon one's wits", 'make efforts to become calm and think more clearly', 'پرسکون ہونے اور زیادہ واضح سوچنے کی کوشش کرنا', 'د ارامېدو او روښانه فکر کولو هڅه کول'),
    ('sick(n)', 'vomiting', 'قے', 'کانګې'),
    ('scrabbling(n)', 'an aimless drawing', 'بے مقصد لکیریں', 'بې‌موخې انځور'),
    ('squeak(n)', 'a short high pitched noise', 'ایک مختصر باریک آواز', 'لنډ نری غږ'),
    ('shudder(v)', 'shake', 'کانپنا', 'لړزېدل'),
    ('speck(n)', 'a very small spot', 'بہت چھوٹا دھبہ', 'ډېر کوچنی ټکی'),
    ('smothering((v)', 'suffocating; causing difficulty in breathing', 'دم گھونٹنے والا؛ سانس لینے میں دشواری پیدا کرنے والا', 'ساه بندوونکی؛ د ساه اخیستو ستونزه پیدا کوونکی'),
    ('succulent(adj.)', 'full of juice', 'رس سے بھرا', 'له شیرې ډک'),
    ('stinking(adj.)', 'very bad.', 'بہت برا۔', 'ډېر بد.'),
    ('swerve(v)', 'change direction abruptly.', 'اچانک سمت بدلنا۔', 'ناڅاپه لوری بدلول.'),
    ('sniggering(adj.)', 'a disrespectful laugh.', 'بے ادبی کی ہنسی۔', 'بې‌ادبانه خندا.'),
    ('squirming(v)', 'to move in a twisting motion.', 'بل کھاتے ہوئے حرکت کرنا۔', 'په تاوېدونکي حرکت ښورېدل.'),
    ('strangled(adj.)', 'suppressed', 'دبایا ہوا', 'زبېښل شوی'),
    ('tusks(n)', 'a long pointed tooth specialized for fighting in a hog or elephant', 'سؤر یا ہاتھی کا لمبا نوکیلا دانت جو لڑائی کے لیے مخصوص ہو', 'د خنزیر یا فیل اوږد تېره غاښ چې د جګړې لپاره ځانګړی وي'),
    ('unaccustomed(adj.)', 'unfamiliar with', 'ناواقف', 'ناآشنا'),
    ('tropical(adj.)', 'of hot and humid weather or climate.', 'گرم اور مرطوب موسم یا آب و ہوا کا۔', 'د تود او لوند موسم یا اقلیم.'),
    ('timidity(n)', 'coward. Lack of self-confidence.', 'بزدل۔ خود اعتمادی کی کمی۔', 'بزدل. د ځان باور کمښت.'),
    ('ungainly(adj.)', 'awkward', 'بھدا', 'ناوړه، بې‌ډوله'),
    ('vicious(adj.)', 'marked by deep ill will.', 'گہری بدنیتی والا۔', 'له ژورې بدنیتۍ ډک.'),
    ('wary(adj)', 'suspicious', 'محتاط، شکی', 'محتاط، شکمن'),
    ('wrench(n)', 'wring; twist.', 'مروڑنا؛ بل دینا۔', 'تاوول؛ مروړل.'),
    ('weariness(n)', 'tiredness', 'تھکن', 'ستړیا'),
    ('whine(n)', 'complain in a sorrowful manner.', 'دکھی انداز میں شکایت کرنا۔', 'په غمجن ډول شکایت کول.'),
    ('whoop(n)', 'a loud hooting cry', 'زور دار نعرہ', 'لوړه چیغه'),
])
a = BOOK.record(g, 'eng12-u19-glossary-c', 'Glossary (savage – whoop)', 'فرہنگ (savage – whoop)', 'وییپانګه (savage – whoop)', 119, [225])

q = Builder()
q.h('Reading Comprehension', 'مطالعہ اور فہم', 'لوستل او پوهه')
q.p('Answer the Questions', 'سوالات کے جواب دیں', 'پوښتنو ته ځواب ووایئ')
Q = [
    ('How did the boys come to the jungle island?', 'لڑکے جنگلی جزیرے پر کیسے پہنچے؟', 'هلکان ځنګلي ټاپو ته څنګه راغلل؟'),
    ('What did Ralph do to attract the other boys on the island?', 'رالف نے جزیرے پر دوسرے لڑکوں کو متوجہ کرنے کے لیے کیا کیا؟', 'رالف په ټاپو کې د نورو هلکانو د راجلبولو لپاره څه وکړل؟'),
    ('Describe the scene of the arrival of Jack and his band at the place where the boys were assembled?', 'لڑکوں کے جمع ہونے کی جگہ پر جیک اور اس کی ٹولی کی آمد کا منظر بیان کریں؟', 'هغه ځای ته چې هلکان راټول وو، د جیک او د هغه د ډلې د راتګ صحنه بیان کړئ؟'),
    ('What was the first issue to that arose before the boys and how was it tackled?', 'لڑکوں کے سامنے پہلا مسئلہ کیا آیا اور اسے کیسے حل کیا گیا؟', 'د هلکانو مخې ته لومړۍ ستونزه کومه وه او څنګه حل شوه؟'),
    ('How did Ralph think they would be rescued?', 'رالف کے خیال میں انہیں کیسے بچایا جائے گا؟', 'رالف فکر کاوه چې څنګه به وژغورل شي؟'),
    ('What rule regarding the conch was made and why?', 'سیپی کے بارے میں کیا قاعدہ بنایا گیا اور کیوں؟', 'د سیپۍ په اړه کومه قاعده جوړه شوه او ولې؟'),
    ("Briefly describe the role of hallucinations scene from 'Loard of the Flies'.", '’’لارڈ آف دی فلائیز‘‘ سے فریبِ نظر (hallucinations) کے منظر کا کردار مختصراً بیان کریں۔', 'د "لارډ آف دي فلایز" څخه د خیالي لید (hallucinations) د صحنې رول په لنډه توګه بیان کړئ.'),
    ("What is the significance of the title 'Loard of the Flies'?", 'عنوان ’’لارڈ آف دی فلائیز‘‘ کی کیا اہمیت ہے؟', 'د "لارډ آف دي فلایز" سرلیک اهمیت څه دی؟'),
    ('What happenes to the conch and Piggy and what does its suggest?', 'سیپی اور پگی کے ساتھ کیا ہوتا ہے اور اس سے کیا ظاہر ہوتا ہے؟', 'په سیپۍ او پګي څه کېږي او دا څه ښيي؟'),
    ('How are the boys rescued at the end?', 'آخر میں لڑکوں کو کیسے بچایا جاتا ہے؟', 'په پای کې هلکان څنګه ژغورل کېږي؟'),
    ("How were Ralph's priorities different from Jack's?", 'رالف کی ترجیحات جیک سے کیسے مختلف تھیں؟', 'د رالف لومړیتوبونه د جیک څخه څنګه توپیر درلود؟'),
    ('What does Simon represent in the novel?', 'ناول میں سائمن کس چیز کی نمائندگی کرتا ہے؟', 'په ناول کې سایمن د څه استازیتوب کوي؟'),
    ('Compare and contrast the characters of Ralph and Piggy.', 'رالف اور پگی کے کرداروں کا موازنہ اور تقابل کریں۔', 'د رالف او پګي کرکټرونه پرتله کړئ.'),
    ('What is the purpose of the introduction of the mock-hunts in the novel?', 'ناول میں فرضی شکار (mock-hunts) کو شامل کرنے کا مقصد کیا ہے؟', 'په ناول کې د جعلي ښکارونو (mock-hunts) د راوستلو موخه څه ده؟'),
    ("[Quotation from Jack’s speech inviting the boys to join his tribe — abridged text p. 208, beginning “Listen all of you…”] Whose words are these and what's the occasion?", '[جیک کی تقریر سے اقتباس جس میں وہ لڑکوں کو اپنے قبیلے میں شامل ہونے کی دعوت دیتا ہے — مختصر متن صفحہ 208، جو “Listen all of you…” سے شروع ہوتا ہے] یہ کس کے الفاظ ہیں اور موقع کیا ہے؟', '[د جیک له وینا څخه اقتباس چې هلکانو ته د خپلې قبیلې د ګډون بلنه ورکوي — لنډ شوی متن 208 مخ، چې په “Listen all of you…” پیلېږي] دا د چا خبرې دي او موقع څه ده؟'),
    ("[Quotation describing Jack’s authority at the feast — abridged text p. 210, beginning “Authority set on his shoulder…”] Explain this statement of William Golding with reference to the context.", '[جیک کے اختیار کو بیان کرنے والا اقتباس — مختصر متن صفحہ 210، جو “Authority set on his shoulder…” سے شروع ہوتا ہے] ولیم گولڈنگ کے اس بیان کی سیاق و سباق کے حوالے سے وضاحت کریں۔', '[د مېلمستیا پر مهال د جیک د واک تشریح کوونکی اقتباس — لنډ شوی متن 210 مخ، چې په “Authority set on his shoulder…” پیلېږي] د ویلیم ګولډینګ دا وینا د شرایطو په حواله تشریح کړئ.'),
    ('"The fire is the most important thing. Without the fire we can\'t be rescued." Whose words are these? What do you say about this statement?', '"The fire is the most important thing. Without the fire we can\'t be rescued." یہ کس کے الفاظ ہیں؟ اس بیان کے بارے میں آپ کیا کہتے ہیں؟', '"The fire is the most important thing. Without the fire we can\'t be rescued." دا د چا خبرې دي؟ د دې وینا په اړه څه وایئ؟'),
    ('What is the dominant theme of the novel " Lord of the flies"?', 'ناول ’’لارڈ آف دی فلائیز‘‘ کا غالب موضوع کیا ہے؟', 'د "لارډ آف دي فلایز" ناول غالبه موضوع څه ده؟'),
    ('What general idea about the psychology of small children do you derive from this novel\' Lord of the flies"?', 'اس ناول ’’لارڈ آف دی فلائیز‘‘ سے آپ چھوٹے بچوں کی نفسیات کے بارے میں کیا عمومی خیال اخذ کرتے ہیں؟', 'له دې ناول "لارډ آف دي فلایز" څخه د کوچنیو ماشومانو د ارواپوهنې په اړه کوم عمومي نظر اخلئ؟'),
    ('Explain the following symbols used in the novel:', 'ناول میں استعمال ہونے والی درج ذیل علامتوں کی وضاحت کریں:', 'په ناول کې کارول شوي لاندې سمبولونه تشریح کړئ:'),
    ("The conch shell, Piggy's glasses, the signal fire, the beast.", 'سیپی، پگی کی عینک، اشارے کی آگ، درندہ۔', 'سیپۍ، د پګي عینکې، د نښې اور، ځناور.'),
]
q.group('lines', [(f'{i}. {e}', f'{i}. {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(Q, 1)])
q.h('Writing Suggestions', 'تحریری تجاویز', 'د لیکلو وړاندیزونه')
q.group('lines', [
    ('1. Write the character sketch of the following characters: A) Ralph B) jack C) Piggy D) Simon', '1. درج ذیل کرداروں کا کرداری خاکہ لکھیں: A) رالف B) جیک C) پگی D) سائمن', '1. د لاندې کرکټرونو کرکټري انځور ولیکئ: A) رالف B) جیک C) پګي D) سایمن'),
    ('2. Compare and contrast the characters of Ralph and Jack.', '2. رالف اور جیک کے کرداروں کا موازنہ اور تقابل کریں۔', '2. د رالف او جیک کرکټرونه پرتله کړئ.'),
])
b = BOOK.record(q, 'eng12-u19-comprehension', 'Reading Comprehension; Writing Suggestions', 'مطالعہ اور فہم؛ تحریری تجاویز', 'لوستل او پوهه؛ د لیکلو وړاندیزونه', 119, [226])
issues = [{'id': 'eng12-p225-226', 'unit': 19, 'printedPage': 226, 'description': 'Questions 15–16 quote the copyrighted abridgement at length; the app gives page references instead. Printed text retained: “Loard of the Flies” (Q7–8), “first issue to that arose”, “What happenes … what does its suggest”, “this novel\' Lord of the flies\"”; Q20/21 split one question across two numbers. Glossary retained: “smothering((v)”, “timidity(n) — coward”, “whine(n)” defined as a verb.'}]

if __name__ == '__main__':
    BOOK.save(119, [(19, a), (19, b)], issues=issues)
