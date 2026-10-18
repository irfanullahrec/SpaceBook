"""Urdu XII PDF33 (spread): printed pp.56–57 — Lesson 7 'منظور' text part 2."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
t = Builder()
for x in [
    ('He spent the whole night in very severe agony. Oxygen was given continuously. When morning came he felt somewhat better and, exhausted, fell asleep.',
     'ساری رات اس نے بڑے شدید کرب میں کاٹی۔ اوکسیجن برابر دی جا رہی تھی، صبح ہوئی تو اسے کسی قدر افاقہ ہوا اور وہ نڈھال ہو کر سو گیا۔',
     'ټوله شپه یې په ډېر سخت درد کې تېره کړه. اکسیجن په دوامداره توګه ورکول کېده. کله چې سهار شو، یو څه ښه شو او ستړی ستومانه ویده شو.'),
    ('Two or three of his relatives came, sat for a while and left. The doctors had told them that the patient had a heart ailment called “coronary thrombosis”. It is very deadly.',
     'اس کے دو تین عزیز آئے۔ کچھ دیر بیٹھے رہے اور چلے گئے۔ ڈاکٹروں نے انھیں بتا دیا تھا کہ مریض کو دل کا عارضہ ہے جسے ’’کورونری تھرومبوسس‘‘ کہتے ہیں۔ یہ بہت مہلک ہوتا ہے۔',
     'د هغه دوه درې خپلوان راغلل، یو څه وخت کېناستل او لاړل. ډاکټرانو ورته ویلي وو چې ناروغ د زړه ناروغي لري چې "کورونري ترومبوسس" ورته وايي. دا ډېره وژونکې وي.'),
    ('When he woke up he was given injections. A dull pain persisted in his heart as before. His shoulder muscles were stiff, as though someone had been pounding them all night. Every fibre of his body ached, but because of weakness he did not feel very much pain. All the same he was sure that his death was not far off; if not today, then tomorrow he would surely die.',
     'جب وہ اٹھا تو اسے ٹیکے لگا دیے گئے۔ اس کے دل میں بدستور میٹھا میٹھا درد ہو رہا تھا۔ شانوں کے پٹھے اکڑے ہوئے تھے۔ جیسے رات بھر انھیں کوئی کوٹتا رہا تھا۔ جسم کی بوٹی بوٹی دکھ رہی تھی مگر نقاہت کے باعث وہ بہت زیادہ تکلیف محسوس نہیں کر رہا تھا۔ ویسے اس کو یقین تھا کہ اس کی موت دور نہیں، آج نہیں تو کل ضرور مر جائے گا۔',
     'کله چې راویښ شو، پېچکارۍ یې ورته ولګولې. په زړه کې یې لکه پخوا خوږ خوږ درد کېده. د اوږو عضلې یې شخې وې، لکه ټوله شپه چې چا کوټلي وي. د بدن هره ټوټه یې خوږېده، خو د کمزورۍ له امله یې ډېر درد نه احساساوه. خو باور یې درلود چې مرګ یې لرې نه دی؛ که نن نه، سبا به خامخا مړ شي.'),
    ('He was nearly thirty-two years old. In these years he had seen no comfort that could come back to him now and add to his hardship. His parents had left him the scar of separation in his very childhood. It is not known who in particular brought him up. He had reached this age simply stumbling here and there, and working in a factory he was living a life of extreme poverty on twenty-five rupees a month.',
     'اس کی عمر بتیس برس کے قریب تھی۔ ان برسوں میں اس نے کوئی راحت نہیں دیکھی تھی جو اس وقت اسے یاد آتی اور اس کی صعوبت میں اضافہ کرتی۔ اس کے ماں باپ اس کو بچپن ہی سے داغِ مفارقت دے گئے تھے۔ معلوم نہیں اس کی پرورش کس خاص شخص نے کی تھی۔ بس وہ ایسے ہی ادھر ادھر کی ٹھوکریں کھاتا، اس عمر تک پہنچ گیا تھا اور ایک کارخانے میں ملازم ہو کر پچیس روپے ماہوار پر انتہا درجے کی افلاس زدہ زندگی گزار رہا تھا۔',
     'عمر یې شاوخوا دوه دېرش کاله و. په دې کلونو کې یې کومه ارامي نه وه لیدلې چې اوس یې ورپه یاد شي او سختي یې زیاته کړي. مور او پلار یې په ماشومتوب کې د بېلتون داغ ورکړی و. معلومه نه ده چې د هغه روزنه کوم ځانګړي کس کړې وه. هسې به یې دلته او هلته ټکرونه خوړل، تر دې عمر ورسېد، او په یوه فابریکه کې ګومارل شوی و او د میاشتې په پنځه ویشت روپیو یې په ډېره بېوزلۍ ژوند تېراوه.'),
    ('Had the pangs not risen in his heart, he would not have felt any marked difference between his health and his illness, because his health had never been good; some ailment or other always clung to him.',
     'دل میں ٹیسیں نہ اٹھتیں تو وہ اپنی تندرستی اور بیماری میں کوئی نمایاں فرق محسوس نہ کرتا کیونکہ صحت اس کی کبھی بھی اچھی نہیں تھی۔ کوئی نہ کوئی عارضہ اسے ضرور لاحق رہتا تھا۔',
     'که په زړه کې یې درد نه وای پورته شوی، د خپلې روغتیا او ناروغۍ ترمنځ به یې کوم ښکاره توپیر نه احساساوه، ځکه چې روغتیا یې هېڅکله ښه نه وه؛ یوه نه یوه ناروغي به خامخا ورسره وه.'),
    ('By evening he had been given four injections. The oxygen had been removed. The heart pain was somewhat less, so he was conscious and could take stock of his surroundings.',
     'شام تک اُسے چار ٹیکے لگ چکے تھے۔ اوکسیجن ہٹا لی گئی تھی۔ دل کا درد کسی قدر کم تھا، اس لیے وہ ہوش میں تھا اور اپنے گرد و پیش کا جائزہ لے سکتا تھا۔',
     'تر ماښامه پورې یې څلور پېچکارۍ لګېدلې وې. اکسیجن لرې شوی و. د زړه درد یو څه کم و، نو په هوښ کې و او د خپل شاوخوا کتنه یې کولی شوه.'),
    ('He was in a very large ward in which many other patients like him lay on iron cots; the nurses were busy with their work. On his right a boy of nine or ten, wrapped in a blanket, was looking towards him; his face was glowing.',
     'وہ بہت بڑے وارڈ میں تھا جس میں اس کی طرح اور کئی مریض لوہے کی چارپائیوں پر لیٹے تھے، نرسیں اپنے کام میں مشغول تھیں۔ اس کے داہنے ہاتھ نو دس برس کا لڑکا کمبل میں لپٹا ہوا اس کی طرف دیکھ رہا تھا، اس کا چہرہ تمتما رہا تھا۔',
     'هغه په یوه ډېر لوی وارډ کې و چې پکې د هغه په څېر نور ډېر ناروغان پر اوسپنیزو کټونو پراته وو؛ نرسانې په خپل کار بوختې وې. ښي لاس ته یې یو نهه لس کلن هلک په کمبل کې تاو، هغه ته کتل؛ مخ یې ځلېده.'),
    ('“Assalamu alaikum,” said the boy very lovingly.', '’’السلام علیکم‘‘۔ لڑکے نے بڑے پیار سے کہا۔', '"السلام علیکم،" هلک په ډېره مینه وویل.'),
    ('The new patient, touched by his loving tone, answered: “Wa alaikum assalam.” The boy turned over in his blanket: “Bhai jan! How are you feeling now?” The new patient said briefly: “Thanks be to Allah.”',
     'نئے مریض نے اس کے پیار بھرے لہجے سے متاثر ہو کر جواب دیا۔ ’’وعلیکم السلام‘‘۔ لڑکے نے کمبل میں کروٹ بدلی: بھائی جان! اب آپ کی طبیعت کیسی ہے‘‘۔ نئے مریض نے اختصار سے کہا: اللہ کا شکر ہے۔',
     'نوي ناروغ د هغه په مینه‌ناکه لهجه اغېزمن شو او ځواب یې ورکړ: "وعلیکم السلام." هلک په کمبل کې اړخ واړاوه: "ورورجانه! اوس مو حال څنګه دی؟" نوي ناروغ په لنډه توګه وویل: "د الله شکر دی."'),
    ('The boy’s face glowed even more. “You will get well very soon. What is your name?”', 'لڑکے کا چہرہ اور زیادہ تمتما اٹھا۔ ’’آپ بہت جلدی ٹھیک ہو جائیں گے۔ آپ کا نام کیا ہے‘‘۔', 'د هلک مخ نور هم وځلېد. "تاسو به ډېر ژر روغ شئ. نوم مو څه دی؟"'),
    ('“My name!” The new patient smiled and looked at the boy with brotherly affection.', '’’میرا نام‘‘! نئے مریض نے مسکرا کر لڑکے کی طرف برادرانہ شفقت سے دیکھا۔', '"زما نوم!" نوي ناروغ وموسکېد او هلک ته یې په ورورولي مینه وکتل.'),
    ('“My name is Akhtar.”', '’’میرا نام اختر ہے‘‘۔', '"زما نوم اختر دی."'),
    ('“My name is Manzoor.” Saying this, he turned over at once and called to the nurse who was passing by.', '’’میرا نام منظور ہے‘‘۔ یہ کہہ کر اس نے یک دم کروٹ بدلی اور اس نرس کو پکارا جو ادھر سے گزر رہی تھی۔', '"زما نوم منظور دی." دا یې وویل، سمدستي یې اړخ واړاوه او هغې نرسې ته یې غږ وکړ چې له هغه ځایه تېرېده.'),
    ('“Apa… Apa jan.”', '’’آپا……… آپا جان‘‘۔', '"اپا… اپا جانې."'),
    ('The nurse stopped. Manzoor put his hand to his forehead and greeted her. The nurse came near, caressed him and went on. A little later the assistant house surgeon came. Manzoor greeted him too: “Doctor ji, assalamu alaikum.”',
     'نرس رک گئی۔ منظور نے ماتھے پر ہاتھ رکھ کر اسے سلام کیا۔ نرس قریب آئی اور اسے پیار کر کے چلی گئی۔ تھوڑی دیر بعد اسسٹنٹ ہاؤس سرجن آیا۔ منظور نے اس کو بھی سلام کیا۔ ’’ڈاکٹر جی، السلام علیکم‘‘۔',
     'نرسه ودرېده. منظور لاس پر تندي کېښود او سلام یې ورته وکړ. نرسه نږدې راغله، مینه یې ورکړه او لاړه. لږ وروسته اسسټنټ هاوس سرجن راغی. منظور هغه ته هم سلام وکړ: "ډاکټر جي، السلام علیکم."'),
    ('The doctor returned the greeting, sat down beside him, and for a long time held his hand in his own and talked with him about the hospital.',
     'ڈاکٹر سلام کا جواب دے کر اس کے پاس بیٹھ گیا اور دیر تک اس کا ہاتھ اپنے ہاتھ میں لے کر اس سے باتیں کرتا رہا جو ہسپتال کے بارے میں تھیں۔',
     'ډاکټر د سلام ځواب ورکړ، د هغه تر څنګ کېناست او ډېر وخت یې د هغه لاس په خپل لاس کې ونیو او د روغتون په اړه یې ورسره خبرې وکړې.'),
    ('Manzoor took an interest in every patient of his ward. He knew whose condition was good and whose was bad, who had gone. All the nurses were his sisters and all the doctors his friends. Among the patients one was an uncle (chacha), one a maternal uncle (mamoon) and one a brother.',
     'منظور کو اپنے وارڈ کے ہر مریض سے دلچسپی تھی۔ اس کو معلوم تھا کس کی حالت اچھی ہے اور کس کی حالت خراب ہے، کون گیا ہے، سب نرسیں اس کی بہنیں تھیں اور سب ڈاکٹر اس کے دوست۔ مریضوں میں کوئی چچا تھا، کوئی ماموں اور کوئی بھائی۔',
     'منظور د خپل وارډ له هر ناروغ سره لېوالتیا درلوده. پوهېده چې د چا حالت ښه دی او د چا خراب، څوک تللی. ټولې نرسانې یې خویندې وې او ټول ډاکټران یې ملګري. په ناروغانو کې یو یې تره و، یو ماما او یو ورور.'),
    ('Everyone loved him. His looks were ordinary, but there was an extraordinary attraction in him. A glow always remained on his face, which served as a halo to his innocence. He was always cheerful and very talkative; but Akhtar, although a heart patient, had become very irritable because of this disease… (continued on p. 58)',
     'سب اس سے پیار کرتے تھے۔ اس کی شکل و صورت معمولی تھی۔ مگر اس میں غیر معمولی کشش تھی۔ ہر وقت اس کے چہرے پر تمتماہٹ رہتی جو اس کی معصومیت پر ہالے کا کام دیتی تھی۔ وہ ہر وقت خوش رہتا تھا۔ بہت زیادہ باتونی تھا، مگر اختر کو، حالانکہ وہ دل کا مریض تھا اور اس مرض کے باعث بہت چڑچڑا ہو گیا… (صفحہ ۵۸ پر جاری)',
     'ټولو ورسره مینه درلوده. بڼه یې عادي وه، خو یوه غیرعادي کشش پکې و. تل به یې پر مخ یوه ځلا وه چې د هغه پر معصومیت یې د هالې کار کاوه. تل خوشحاله و او ډېر خبرې کوونکی و، خو اختر، که څه هم د زړه ناروغ و او د دې ناروغۍ له امله ډېر تریخ‌خویه شوی و… (په ۵۸ مخ کې دوام)'),
]: t.p(*x)
rec = BOOK.record(t, 'urdu12-u7-text-2', 'Lesson text (2)', 'متنِ سبق (۲)', 'د لوست متن (۲)', 33, [56, 57])
rec['sourceCoverIllustrationReview'] = 'Ward drawings in the page margins (nurses, patients, medicine shelves) are decorative; not reproduced.'
issues = [{'id': 'urdu12-pdf033', 'unit': 7, 'printedPage': 56, 'description': 'P.56–57 are tightly bound in the scan; the first letters of two lines are lost at the gutter (“[نر]سیں اپنے کام میں”, “دیکھ [رہ]ا تھا”) and are restored from context and the Word OCR. Printed quotation marks are unbalanced in “بھائی جان! اب آپ کی طبیعت کیسی ہے‘‘” and “’’میرا نام‘‘!” — retained.'}]

if __name__ == '__main__':
    BOOK.save(33, [(7, rec)], issues=issues)
