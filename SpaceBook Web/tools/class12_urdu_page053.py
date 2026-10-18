"""Urdu XII PDF53 (spread): printed pp.96–97 — Lesson 10 مشق Q1–Q6 and the genre note 'افسانہ'. Completes Lesson 10."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Write answers to the following questions.', '1. درج ذیل سوالات کے جوابات لکھیں۔', '1. لاندې پوښتنو ته ځوابونه ولیکئ.')
e.group('lines', [
    ('a. Write a story with the title “The bad come to a bad end”.', 'ا۔ ’’بُرے کا بُرا انجام‘‘ کے عنوان سے کہانی تحریر کریں۔', 'ا. د "بد د بد پای" تر سرلیک لاندې یوه کیسه ولیکئ.'),
    ("b. What had happened to Sakina Begum's son?", 'ب۔ سکینہ بیگم کے بیٹے کو کیا ہو گیا تھا؟', 'ب. د سکینه بېګم زوی ته څه شوي وو؟'),
    ('c. Whose cry was “Makhan tosh”?', 'ج۔ ’’مکھن ٹوش‘‘ کا نعرہ کس کا تھا؟', 'ج. د "مکهن ټوش" ناره د چا وه؟'),
    ('d. What did Abdullah do when a passer-by fainted with fright?', 'د۔ جب کوئی راہگیر ڈر کر بے ہوش ہو جاتا تو عبداللہ کیا کرتا؟', 'د. کله چې به کوم لاروی له وېرې بې‌هوښه شو، عبدالله به څه کول؟'),
    ('e. When people stopped leaving their homes after dusk, what method did Abdullah adopt to obtain food?', 'ہ۔ جب لوگوں نے شام کے بعد گھروں سے نکلنا چھوڑ دیا تو عبداللہ نے خوراک کے حصول کے لیے کیا طریقہ اختیار کیا؟', 'ه. کله چې خلکو له ماښام وروسته له کورونو وتل پرېښودل، عبدالله د خوړو د ترلاسه کولو لپاره کومه لاره غوره کړه؟'),
    ('f. What did the neighbours do on hearing of the “ghost”?', 'و۔ ’’بھوت‘‘ کا سن کر محلے والوں نے کیا کیا؟', 'و. د "پېري" په اورېدو محلې والو څه وکړل؟'),
    ("g. Where did Abdullah's death take place?", 'ز۔ عبداللہ کی موت کہاں واقع ہوئی؟', 'ز. د عبدالله مرګ چېرته پېښ شو؟'),
])
e.p('2. Fill in the blanks according to correct idiomatic usage (rozmarra).', '2. خالی جگہ درست روز مرہ کے مطابق پُر کریں۔', '2. د سمې ورځنۍ محاورې سره سم تش ځایونه ډک کړئ.')
e.group('lines', [
    ('a. But this man descended like the angel of ________ .', 'ا۔ مگر یہ شخص تو ________ کے فرشتے کی طرح نازل ہوا۔', 'ا. خو دا سړی د ________ د پرښتې په څېر راښکته شو.'),
    ('b. My voice was ________ with fear?', 'ب۔ میری آواز خوف سے ________ رہی تھی؟', 'ب. زما غږ له وېرې ________ ؟'),
    ('c. Both will sleep comfortably, ________ outstretched.', 'ج۔ دونوں مزے سے ________ پھیلا کر سوئیں گے۔', 'ج. دواړه به په خوند ________ غزولي ویده شي.'),
    ('d. Like a cat it ________ and seized my throat.', 'د۔ بلی کی طرح ________ کر میرا گلا دبوچ لیا۔', 'د. د پیشو په څېر یې ________ او ستونی یې راونیو.'),
    ('e. My condition had now become a little ________ .', 'ہ۔ میری طبیعت اب ذرا ________ چکی تھی۔', 'ه. زما حال اوس یو څه ________ و.'),
])
e.p('3. Use the following words and phrases in sentences of your own.', '3. مندرجہ ذیل الفاظ و تراکیب کو اپنے جملوں میں استعمال کریں۔', '3. لاندې کلمې او ترکیبونه په خپلو جملو کې وکاروئ.')
e.p('sunsān (deserted), muṭh-bheṛ (encounter), chauṛā-chaklā (broad), imtidād-e-zamāna (passage of time), sangsār karnā (to stone), hū kā ʿālam (dead silence), bāchhen khilnā (to beam with joy)', 'سنسان، مُڈبھیڑ، چوڑا چکلا، امتدادِ زمانہ، سنگسار کرنا، ہُو کا عالم، باچھیں کھلنا', 'سنسان (شاړ)، مډبهېړ (مخامخ کېدل)، چوړا چکلا (پلن)، امتداد زمانه (د وخت تېرېدل)، سنګسارول، د هو عالم (بشپړه چوپتیا)، باچهېں کهلنا (له خوښۍ ګل کېدل)')
e.p('4. Put diacritics (iʿrāb) on the following words.', '4. درج ذیل الفاظ پر اِعراب لگائیں۔', '4. پر لاندې کلمو اعراب کېږدئ.')
e.p('nauʿiyyat, ghanīm, bar-afrokhta, sannāṭā, muṭh-bheṛ, badro [Urdu words to be vowelled]', 'نوعیت، غنیم، برافروختہ، سناٹا، مڈبھیڑ، بدرو', 'نوعیت، غنیم، برافروخته، سناټا، مډبهېړ، بدرو [د اردو کلمې چې اعراب پرې کېښودل شي]')
e.p('5. Correct the following sentences according to idiomatic usage.', '5. درج ذیل جملے روز مرہ کے مطابق درست کریں۔', '5. لاندې جملې د ورځنۍ محاورې سره سم سمې کړئ.')
e.group('lines', [
    ('a. “The thief was arrested along with (bamaʿ) the stolen goods.”', 'ا۔ چور بمع مالِ مسروقہ گرفتار ہو گیا۔', 'ا. "غل له غلا شوي مال سره ونیول شو."'),
    ('b. “The government flag is flying over the top of the building.”', 'ب۔ عمارت کے اُوپر سرکاری پرچم لہرا رہا ہے۔', 'ب. "د ودانۍ پر سر دولتي بیرغ رپېږي."'),
    ('c. “The scenes of the Kaghan valley are indeed worth seeing.”', 'ج۔ وادیٔ کاغان کے مناظر تو دیکھنے والے ہیں۔', 'ج. "د کاغان د درې منظرې خو د لیدو دي."'),
    ("d. “I don't understand what you are saying.”", 'د۔ مجھ کو سمجھ نہیں آتی کہ تم کیا کہہ رہے ہو۔', 'د. "زه نه پوهېږم چې ته څه وایې."'),
    ('e. “My college will open on dated the first of September.”', 'ہ۔ مورخہ یکم ستمبر کو میرا کالج کھلے گا۔', 'ه. "زما کالج به د سپتمبر په لومړۍ نېټه خلاصېږي."'),
])
e.p('6. Put punctuation marks at the appropriate places in the following passage.', '6. درج ذیل عبارت میں مناسب مقامات پر رموزِ اوقاف لگائیں۔', '6. په لاندې متن کې په مناسبو ځایونو کې رموزِ اوقاف کېږدئ.')
e.p('Listen son the country needs, besides engineers and doctors, people connected with other walks of life too in this country there is no top-ranking historian expert economist unique writer or poet best administrator internationally recognised lawyer or politician or scientist all this belongs to the field of arts [printed without punctuation, to be punctuated]',
    'سنو بیٹا ملک کو انجینئروں اور ڈاکٹروں کے علاوہ دوسرے شعبہ ہائے زندگی سے تعلق رکھنے والے لوگوں کی بھی ضرورت ہے اس ملک میں کوئی چوٹی کا مؤرخ ماہر اقتصادیات یگانۂ روزگار ادیب یا شاعر بہترین منتظم بین الاقوامی معیار کا قانون دان یا سیاست دان سائنس دان نہیں ہے یہ سب کچھ تو آرٹس کے شعبے سے متعلق ہے۔',
    'واوره زویه هېواد ته له انجنیرانو او ډاکټرانو پرته د ژوند د نورو برخو خلکو ته هم اړتیا ده په دې هېواد کې کوم لوړ پوړی مورخ اقتصادپوه بې‌ساری ادیب یا شاعر غوره مدیر نړیوال معیاري قانونپوه یا سیاستوال ساینسپوه نشته دا ټول د هنرونو له څانګې سره تړاو لري [پرته له تکي‌ایښودنې چاپ شوی، باید تکي ورکړل شي]')
e.h('The short story (afsāna):', 'اِفسانہ:', 'لنډه کیسه (افسانه):')
e.p('For “afsāna” the English words Fiction and Short Story are used. It belongs to the kind (type) of the novel and the dāstān. But whereas the novel takes into itself a whole world, the short story presents only one aspect of human life in this world, or only one face of social, economic and political problems. So we define the short story thus:',
    '’’افسانہ‘‘ کے لیے انگریزی زبان کے الفاظ Fiction اور Short Story استعمال ہوتے ہیں۔ یہ ناول اور داستان کی نوعیت (قسم) سے تعلق رکھتا ہے۔ مگر جہاں ناول ایک پورے جہان کو اپنے اندر سمو لیتا ہے۔ وہاں افسانہ اس جہانِ انسانی کی زندگی کا صرف ایک پہلو یا معاشرتی، معاشی اور سیاسی مسائل کا صرف ایک رُخ پیش کرتا ہے۔ پس ہم افسانہ کی تعریف یوں پیش کرتے ہیں:',
    'د "افسانه" لپاره د انګرېزي ژبې کلمې Fiction او Short Story کارېږي. دا د ناول او داستان له ډول سره تړاو لري. خو چېرته چې ناول یوه بشپړه نړۍ په ځان کې ځایوي، هلته افسانه د انساني نړۍ د ژوند یوازې یو اړخ یا د ټولنیزو، اقتصادي او سیاسي ستونزو یوازې یو مخ وړاندې کوي. نو موږ د افسانې تعریف داسې وړاندې کوو:')
e.p('“The short story is that genre of literature which presents some one aspect of life, a character or an event so completely that it can be read in a single sitting.”', '’’افسانہ ادب کی وہ صنف ہے جو زندگی، کردار یا واقعہ کے کسی ایک پہلو کو مکمل طور پر اس طرح پیش کرتا ہے کہ اسے ایک ہی نشست میں پڑھا جا سکے‘‘۔', '"افسانه د ادب هغه ژانر دی چې د ژوند، کرکټر یا پېښې یو اړخ په بشپړه توګه داسې وړاندې کوي چې په یوه ناسته کې ولوستل شي."')
e.p('That is, a short story is a brief tale that can be read in from half an hour to one or two hours. It presents an important and interesting event in someone’s life in an artistic form. The narration of this event includes a beginning, a climax and an ending.', 'یعنی افسانہ وہ مختصر کہانی ہے جسے آدھے گھنٹے سے لے کر ایک یا دو گھنٹے میں پڑھا جا سکتا ہے۔ یہ کسی شخص کی زندگی کے اہم اور دلچسپ واقعے کو فنی شکل میں پیش کرتا ہے۔ اس واقعے کے بیان میں ابتدا، عروج اور خاتمہ شامل ہے۔', 'یعنې افسانه هغه لنډه کیسه ده چې له نیم ساعت څخه تر یو یا دوه ساعته پورې ولوستل شي. د یو کس د ژوند یوه مهمه او په زړه پورې پېښه په هنري بڼه وړاندې کوي. د دې پېښې په بیان کې پیل، اوج او پای شامل دي.')
ex = BOOK.record(e, 'urdu12-u10-exercise', 'Exercise; the short story (afsāna)', 'مشق؛ افسانہ', 'تمرین؛ افسانه', 53, [96, 97])
issues = [{'id': 'urdu12-pdf053', 'unit': 10, 'printedPage': 96, 'description': 'Q2 sentences are not from this story (they are general idiom drills). Q5 sentences deliberately contain errors to be corrected; Q6 passage printed without punctuation. Handwritten answers in Q2 blanks are owner notes, excluded. Q2(b) ends with “؟” as printed.'}]

if __name__ == '__main__':
    BOOK.save(53, [(10, ex)], issues=issues, complete_units=[10])
