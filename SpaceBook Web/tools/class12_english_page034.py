"""PDF34 (printed 55–56): Unit 6 About the Poet; Glossary; Reading Comprehension Q1–9; Writing; Oral Communication; Vocabulary A (start)."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
a = Builder()
a.h('About the Poet', 'شاعر کے بارے میں', 'د شاعر په اړه')
a.p('Rudyard Kipling (1865-1936) was born in Bombay, India; his father was the curator of the Lahore Museum. He went to school in England and returned to India as a journalist in 1882. He achieved rapid fame as a poet and short-story writer in England. He was the first Englishman to receive the Nobel Prize for Literature in 1907. His two Jungle Books (1894, 1895) are set in Indian. Jungle; and Kim a novel, is set in pre-partition Lahore.',
    'رڈیارڈ کپلنگ (1865-1936) بمبئی، ہندوستان میں پیدا ہوئے؛ ان کے والد لاہور عجائب گھر کے نگران تھے۔ انہوں نے انگلستان میں تعلیم حاصل کی اور 1882 میں صحافی کی حیثیت سے ہندوستان واپس آئے۔ انہوں نے انگلستان میں شاعر اور افسانہ نگار کی حیثیت سے تیزی سے شہرت حاصل کی۔ وہ 1907 میں ادب کا نوبل انعام پانے والے پہلے انگریز تھے۔ ان کی دو ’’جنگل بکس‘‘ (1894، 1895) ہندوستانی جنگل کے پس منظر میں ہیں؛ اور ناول ’’کِم‘‘ تقسیم سے پہلے کے لاہور کے پس منظر میں ہے۔',
    'روډیارډ کیپلینګ (1865-1936) د هند په بمبۍ کې زېږېدلی؛ پلار یې د لاهور د موزیم څارونکی و. په انګلستان کې یې ښوونځی ووایه او په 1882 کې د خبریال په توګه هند ته ستون شو. په انګلستان کې یې د شاعر او لنډې کیسې لیکوال په توګه ژر شهرت وموند. هغه لومړنی انګرېز و چې په 1907 کې یې د ادب نوبل جایزه ترلاسه کړه. د هغه دوه "د ځنګل کتابونه" (1894، 1895) د هند په ځنګل کې پېښېږي؛ او "کیم" ناول له وېش مخکې په لاهور کې پېښېږي.')
GL = [
    ('aim(n)', 'intention; goal', 'ارادہ؛ مقصد', 'اراده؛ موخه'), ('bear(v)', 'to accept', 'قبول کرنا', 'منل'), ('common touch(n)', 'ability to get along with ordinary people', 'عام لوگوں کے ساتھ گھل مل جانے کی صلاحیت', 'له عامو خلکو سره د جوړ جاړي وړتیا'),
    ('foes(n)', 'enemies', 'دشمن', 'دښمنان'), ('give way (v)', 'Allow', 'اجازت دینا', 'اجازه ورکول'), ('heap (n)', 'Pile', 'ڈھیر', 'ډېری'),
    ('imposters (n)', 'people who pretend to be other people;showing a false identity,:', 'وہ لوگ جو دوسرے ہونے کا ڈھونگ رچاتے ہیں؛ جھوٹی شناخت ظاہر کرنے والے', 'هغه خلک چې ځان بل ښيي؛ دروغجنه پېژندنه ښوونکي'),
    ('knaves (n)', 'lying men; rogues', 'جھوٹے آدمی؛ بدمعاش', 'دروغجن سړي؛ بدمعاشان'), ('make allowance', 'permit; allow', 'گنجائش دینا؛ اجازت دینا', 'ځای ورکول؛ اجازه ورکول'),
    ('pitch-and-toss', 'a game of skill and chance breathe a word : tell a secret; talk about something', 'مہارت اور قسمت کا ایک کھیل؛ breathe a word: راز بتانا؛ کسی چیز کے بارے میں بات کرنا', 'د مهارت او بخت یوه لوبه؛ breathe a word: راز ویل؛ د یو شي په اړه خبرې کول'),
    ('serve your turn', 'be useful; helpful', 'کام آنا؛ مددگار ہونا', 'په کار راتلل؛ مرستندوی کېدل'), ('sinew(n)', 'strong tissue that connects muscles to bones', 'مضبوط ریشہ جو پٹھوں کو ہڈیوں سے جوڑتا ہے', 'قوي نسج چې عضلې له هډوکو سره نښلوي'),
    ('stoop(v)', 'bend', 'جھکنا', 'ټیټېدل'), ('triumph (n)', 'victory; success', 'فتح؛ کامیابی', 'بریا؛ کامیابي'), ('will(n)', 'Determination', 'عزم', 'عزم'),
    ('winnings (n)', 'money that is won in a game', 'کھیل میں جیتی ہوئی رقم', 'په لوبه کې ګټلې پیسې'), ('wise (adj.)', 'Smart', 'سمجھدار', 'هوښیار'), ('worn-out(adj.)', 'damaged; used', 'خراب؛ استعمال شدہ', 'زیانمن؛ کارول شوی'),
]
a.h('Glossary', 'فرہنگ', 'وییپانګه')
gloss(a, 'eng12-u06-gloss', GL)
ab = BOOK.record(a, 'eng12-u06-about-glossary', 'About the Poet; Glossary', 'شاعر کے بارے میں؛ فرہنگ', 'د شاعر په اړه؛ وییپانګه', 34, [55])
ab['sourceCoverIllustrationReview'] = 'Portrait of Kipling is decorative; not reproduced.'

q = Builder()
q.h('Reading Comprehension', 'مطالعہ اور فہم', 'لوستل او پوهه')
q.group('lines', [
    ('1. What is the main theme of the poem "If"?', '1. نظم ’’اگر‘‘ کا مرکزی موضوع کیا ہے؟', '1. د "که" شعر اصلي موضوع څه ده؟'),
    ('2. Make a list of all the qualities of a perfect man as mentioned by the poet in stanza two of the poem "If".', '2. نظم ’’اگر‘‘ کے دوسرے بند میں شاعر کی بیان کردہ ایک کامل انسان کی تمام خوبیوں کی فہرست بنائیں۔', '2. د "که" شعر په دویم بند کې د شاعر له خوا یاد شوي د بشپړ انسان ټولې ځانګړنې لست کړئ.'),
    ('3. Explain the line, "Or walk with kings – nor lose thy common touch".', '3. مصرعے ’’یا بادشاہوں کے ساتھ چلو — اور عام لوگوں سے تعلق نہ کھوؤ‘‘ کی وضاحت کریں۔', '3. دا مسرعه تشریح کړئ: "یا له پاچایانو سره ګام پورته کړه — او له عامو خلکو اړیکه له لاسه مه ورکوه".'),
    ('4. Cite an example of the use of personification in the poem "If"?', '4. نظم ’’اگر‘‘ میں تجسیم کے استعمال کی ایک مثال دیں؟', '4. د "که" په شعر کې د تجسیم د کارونې یوه بېلګه راوړئ؟'),
    ('5. What is the significance of the title of the poem?', '5. نظم کے عنوان کی کیا اہمیت ہے؟', '5. د شعر د سرلیک اهمیت څه دی؟'),
    ('6. What does this point say about the value of time?', '6. یہ نکتہ وقت کی قدر کے بارے میں کیا کہتا ہے؟', '6. دا ټکی د وخت د ارزښت په اړه څه وايي؟'),
    ('7. Explain the meaning of this line in your own words, "And – which is more – you\'ll be a man, my son."', '7. اس مصرعے کا مطلب اپنے الفاظ میں بیان کریں: ’’اور — جو اس سے بھی بڑھ کر ہے — تم ایک مرد بنو گے، میرے بیٹے۔‘‘', '7. د دې مسرعې مانا په خپلو ټکو کې تشریح کړئ: "او — چې تر دې هم زیات دی — ته به سړی شې، زما زویه."'),
    ('8. What is the rhyme scheme of this poem?', '8. اس نظم کی قافیہ بندی کیا ہے؟', '8. د دې شعر د قافیې طرحه څه ده؟'),
    ('9. State some qualities other than the ones mentioned in the poem "If" that make a successful man.', '9. نظم ’’اگر‘‘ میں مذکور خوبیوں کے علاوہ کچھ اور خوبیاں بیان کریں جو ایک کامیاب انسان بناتی ہیں۔', '9. د "که" په شعر کې له یادو شویو پرته ځینې نورې ځانګړنې بیان کړئ چې یو بریالی سړی جوړوي.'),
])
q.h('Writing Suggestions', 'تحریری تجاویز', 'د لیکلو وړاندیزونه')
q.p('Ask your students to write a short essay on a person known to them, who possesses all or some of the qualities of a perfect man as mentioned in the poem "If".', 'اپنے طلبہ سے کہیں کہ وہ اپنے کسی جاننے والے شخص پر ایک مختصر مضمون لکھیں جس میں نظم ’’اگر‘‘ میں بیان کردہ کامل انسان کی تمام یا کچھ خوبیاں ہوں۔', 'له خپلو زده کوونکو وغواړئ چې د یوه پېژندل شوي کس په اړه لنډه مقاله ولیکي چې د "که" په شعر کې یاد شوي د بشپړ انسان ټولې یا ځینې ځانګړنې ولري.')
q.h('Oral Communication', 'زبانی ابلاغ', 'د خولې اړیکه')
q.p('Ask two or three students to play the role of a father and give advice to the student who are spouse to be playing the role of sons. The sons (class students) should interact with them (fathers) asking various questions. The questions should be on how to behave as a good citizen of a country.', 'دو تین طلبہ سے کہیں کہ وہ باپ کا کردار ادا کریں اور ان طلبہ کو نصیحت کریں جو بیٹوں کا کردار ادا کر رہے ہوں۔ بیٹے (جماعت کے طلبہ) مختلف سوالات پوچھ کر ان (باپوں) سے تبادلۂ خیال کریں۔ سوالات اس بارے میں ہوں کہ ملک کے اچھے شہری کی طرح کیسے برتاؤ کیا جائے۔', 'له دوو یا درېیو زده کوونکو وغواړئ چې د پلار رول ولوبوي او هغو زده کوونکو ته نصیحت وکړي چې د زامنو رول لوبوي. زامن (د ټولګي زده کوونکي) باید د بېلابېلو پوښتنو په کولو له هغوی (پلرونو) سره تعامل وکړي. پوښتنې باید د دې په اړه وي چې د یوه هېواد د ښه تبعه په توګه څنګه چلند وشي.')
q.h('Vocabulary and Grammar', 'ذخیرۂ الفاظ اور قواعد', 'لغات او ګرامر')
q.p('A. Consult a dictionary and write the phonetic transcription of the following words.', 'A. لغت سے رجوع کریں اور درج ذیل الفاظ کی صوتی نقل لکھیں۔', 'A. قاموس ته مراجعه وکړئ او د لاندې کلمو غږیز لیکدود ولیکئ.')
W = ['Stage', 'Infant', 'Nurse', 'Satchel', 'Snail', 'Lover']
R = [[x, ''] for x in W]
q.table('eng12-u06-dict-a', ['Word', 'Phonetic Transcription'], R, ['لفظ', 'صوتی نقل'], ['کلمه', 'غږیز لیکدود'], R, R)
qs = BOOK.record(q, 'eng12-u06-comprehension', 'Reading Comprehension; Writing; Oral Communication; Vocabulary A (1)', 'مطالعہ اور فہم؛ تحریر؛ زبانی ابلاغ؛ ذخیرۂ الفاظ A (1)', 'لوستل او پوهه؛ لیکنه؛ د خولې اړیکه؛ لغات A (1)', 34, [56])
issues = [{'id': 'eng12-p55-56', 'unit': 6, 'printedPage': 56, 'description': 'Printed text retained: “set in Indian. Jungle”, glossary “imposters” (poem: impostors) and a merged entry “pitch-and-toss … breathe a word”, Q3 quotes “thy common touch” (poem: the common touch), Q6 “this point” (undefined), oral task “who are spouse to be” (supposed to be). The dictionary words (Stage, Infant, Satchel…) belong to Unit 12’s poem.'}]

if __name__ == '__main__':
    BOOK.save(34, [(6, ab), (6, qs)], issues=issues)
