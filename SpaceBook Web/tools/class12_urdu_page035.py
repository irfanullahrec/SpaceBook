"""Urdu XII PDF35 (spread): printed pp.60–61 — Lesson 7 'منظور' text part 4."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
t = Builder()
for x in [
    ('(continuing) …mind had itself invented this method so that his sorrow would be suppressed.', '(جاری) …دماغ نے یہ طریقہ خود ایجاد کیا تھا کہ اس کا دکھ دب جائے۔', '(دوام) …ذهن دا لاره پخپله ایجاد کړې وه چې د هغه درد پټ شي.'),
    ('Akhtar had another attack. It was far more painful and dangerous than the first, but he showed patience and endurance and, keeping Manzoor’s example before him, tried to remain heedless of his pain, in which he succeeded. This time the doctors were a hundred per cent certain that no power in the world could save him, but a miracle happened, and when the nurse on night duty handed him over to the other nurses early in the morning, his falling pulse had steadied… he was alive.',
     'اختر پر پھر ایک دورہ پڑا۔ یہ پہلے دورے سے کہیں زیادہ تکلیف دہ اور خطرناک تھا مگر اس نے صبر اور تحمل سے کام لیا اور منظور کی مثال سامنے رکھ کر اپنے درد سے غافل رہنے کی کوشش کی جس میں اسے کامیابی ہوئی۔ ڈاکٹروں کو اس مرتبہ تو سو فیصد یقین تھا کہ دنیا کی کوئی طاقت اسے نہیں بچا سکتی، مگر معجزہ رونما ہوا اور رات کی ڈیوٹی پر مُعین نرس نے صبح سویرے اسے دوسری نرسوں کے سپرد کیا تو اس کی گرتی ہوئی نبض سنبھل چکی تھی……… وہ زندہ تھا۔',
     'پر اختر بیا یو دوره راغله. دا له لومړۍ دورې ډېره دردناکه او خطرناکه وه، خو هغه صبر او زغم وکړ او د منظور بېلګه یې مخې ته کېښوده او هڅه یې وکړه چې له خپل درد ناخبره پاتې شي، او بریالی شو. دا ځل ډاکټرانو ته سل په سلو کې باور و چې د نړۍ هیڅ ځواک یې نه شي ژغورلی، خو معجزه وشوه، او کله چې د شپې په دنده ټاکلې نرسې سهار وختي هغه نورو نرسانو ته وسپاره، د هغه لوېدونکی نبض ټینګ شوی و…… ژوندی و.'),
    ('When, exhausted from wrestling with death, he began to fall asleep, he looked with half-closed eyes towards Manzoor, who was lost in sleep. His face was glowing. In his weak and feeble heart Akhtar kissed his forehead and fell asleep.',
     'موت سے کشتی لڑتے لڑتے نڈھال ہو کر جب وہ سونے لگا تو اس نے نیم مُندی ہوئی آنکھوں سے منظور کی طرف دیکھا جو محوِ خواب تھا۔ اس کا چہرہ دمک رہا تھا۔ اختر نے اپنے کمزور و نحیف دل میں اس کی پیشانی کو چوما اور سو گیا۔',
     'له مرګ سره د غېږ وهلو له امله ستړی ستومانه چې ویده کېده، په نیم پټو سترګو یې منظور ته وکتل چې په خوب ورک و. مخ یې ځلېده. اختر په خپل کمزوري او ناتوانه زړه کې د هغه تندی ښکل کړ او ویده شو.'),
    ('When he woke, Manzoor was chirping. He was saying to a nurse about him: “Apa, wake Akhtar bhai jan. It is time for his medicine.”', 'جب اٹھا تو منظور چہک رہا تھا۔ اس کے متعلق ایک نرس سے کہہ رہا تھا۔ ’’آپا اختر بھائی جان کو جگاؤ۔ دوا کا وقت ہو گیا ہے‘‘۔', 'کله چې راویښ شو، منظور چغېده. د هغه په اړه یې یوې نرسې ته ویل: "اپا، اختر ورورجان راویښ کړه. د درملو وخت شوی."'),
]: t.p(*x)
t.group('lines', [
    ('“Let him sleep……… he needs rest.”', '’’سونے دو……… اسے آرام کی ضرورت ہے‘‘۔', '"پرېږده چې ویده وي…… ارام ته اړتیا لري."'),
    ('“No……… he is perfectly fine. You give him his medicine.”', '’’نہیں……… وہ بالکل ٹھیک ہے۔ آپ انھیں دوا دیجیے‘‘۔', '"نه…… هغه بېخي ښه دی. تاسو یې درمل ورکړئ."'),
    ('“All right, I’ll give it.”', '’’اچھا دے دوں گی‘‘۔', '"ښه، ورکوم یې."'),
])
for x in [
    ('When Manzoor looked towards Akhtar, his eyes were open. He said very happily, in a loud voice:', 'منظور نے جب اختر کی طرف دیکھا تو اس کی آنکھیں کھلی ہوئی تھیں۔ اس نے بہت خوش ہو کر باآوازِ بلند کہا:', 'کله چې منظور اختر ته وکتل، سترګې یې پرانیستې وې. په ډېره خوښۍ یې په لوړ غږ وویل:'),
]: t.p(*x)
t.group('lines', [
    ('“Assalamu alaikum.”', '’’السلام علیکم‘‘۔', '"السلام علیکم."'),
    ('Akhtar answered in a voice full of weakness: “Wa alaikum assalam.”', 'اختر نے نقاہت بھرے لہجے میں جواب دیا: ’’وعلیکم السلام‘‘۔', 'اختر په کمزوره لهجه ځواب ورکړ: "وعلیکم السلام."'),
    ('“Bhai jan! You slept a lot.”', '’’بھائی جان! آپ بہت سوئے‘‘۔', '"ورورجانه! ډېر ویده وئ."'),
    ('“Yes……… perhaps.”', '’’ہاں……… شاید‘‘۔', '"هو…… ښايي."'),
    ('“The nurse is bringing medicine for you.”', '’’نرس آپ کے لیے دوا لا رہی ہے‘‘۔', '"نرسه ستاسو لپاره درمل راوړي."'),
])
for x in [
    ('Akhtar felt that Manzoor’s words were strengthening his feeble heart. After a little while he himself began to chirp and chatter like him. He asked Manzoor: “Did you pray for me this time too?”',
     'اختر نے محسوس کیا کہ منظور کی باتیں اس کے نحیف دل کو تقویت پہنچا رہی ہیں۔ تھوڑی دیر کے بعد ہی وہ خود اسی کی طرح چہکنے چہکارنے لگا۔ اس نے منظور سے پوچھا: ’’اس مرتبہ بھی تم نے میرے لیے دعا مانگی تھی‘‘؟',
     'اختر احساس کړ چې د منظور خبرې د هغه کمزوري زړه ته ځواک ورکوي. لږ وروسته پخپله د هغه په څېر چغېدل او خبرې کول پیل کړل. له منظور یې وپوښتل: "دا ځل دې هم زما لپاره دعا کړې وه؟"'),
]: t.p(*x)
t.group('lines', [
    ('Manzoor answered: “No.”', 'منظور نے جواب دیا۔ ’’نہیں‘‘۔', 'منظور ځواب ورکړ: "نه."'),
    ('“Why?”', '’’کیوں؟‘‘', '"ولې؟"'),
    ('“I don’t pray every day……… I prayed once; that was enough. I knew you would get well.” There was certainty in his tone.', '’’میں روز روز دعائیں نہیں مانگا کرتا……… ایک دفعہ مانگ لی، کافی تھی۔ مجھے معلوم تھا آپ ٹھیک ہو جائیں گے‘‘۔ اس کے لہجے میں یقین تھا۔', '"زه هره ورځ دعا نه کوم…… یو ځل مې وکړه، بس وه. پوهېدم چې تاسو به روغ شئ." په لهجه کې یې باور و.'),
])
for x in [
    ('Akhtar, to tease him a little, said: “You keep telling others that they will get well; why don’t you get well yourself and go home?”', 'اختر نے اسے ذرا سا چھیڑنے کے لیے کہا: ’’تم دوسروں سے کہتے رہتے ہو کہ ٹھیک ہو جاؤ گے، خود کیوں نہیں ٹھیک ہو کر گھر چلے جاتے‘‘۔', 'اختر د هغه د لږ ټوکولو لپاره وویل: "ته نورو ته وایې چې روغ به شئ، پخپله ولې نه روغېږې او کور ته نه ځې؟"'),
    ('Manzoor thought for a little while: “I will get well too. The big doctor ji said that within a month you will start walking about……… look, now I can slide down and up.”', 'منظور نے تھوڑی دیر سوچا: ’’میں بھی ٹھیک ہو جاؤں گا۔ بڑے ڈاکٹر جی کہتے تھے کہ تم ایک مہینے تک چلنے پھرنے لگو گے……… دیکھیں نا اب میں نیچے اور اوپر کھسک سکتا ہوں‘‘۔', 'منظور یو څه وخت فکر وکړ: "زه به هم روغ شم. لوی ډاکټر جي ویل چې په یوه میاشت کې به ګرځېدل پیل کړې…… وګورئ، اوس زه ښکته او پورته ښوییدلی شم."'),
    ('He made an unsuccessful attempt to slide up and down in the blanket. Akhtar at once said: “Well done, Manzoor mian……… what is a month?……… it will pass like this.”', 'اس نے کمبل میں اوپر نیچے کھسکنے کی ناکام کوشش کی۔ اختر نے فوراً کہا: واہ منظور میاں واہ……… ایک مہینا کیا ہے……… یوں گزر جائے گا۔', 'هغه په کمبل کې د پورته او ښکته ښوییدو ناکامه هڅه وکړه. اختر سمدستي وویل: "واه منظور میاں، واه…… یوه میاشت څه ده…… داسې به تېره شي."'),
    ('Manzoor snapped his fingers and began to laugh happily.', 'منظور نے چٹکی بجائی اور خوش ہو کر ہنسنے لگا۔', 'منظور ګوتې وشړنګولې او په خوښۍ یې خندل پیل کړل.'),
    ('More than a month passed. During this time Akhtar had two or three heart attacks which were not very severe. Now his condition was better and his weakness was going away. There was not the former tension in his nerves either. The rhythm of his heart was right. The doctors thought he was now out of danger, but their wonder remained as before at how he had survived.',
     'ایک مہینے سے زیادہ عرصہ گزر گیا۔ اس دوران اختر پر دل کے دو تین دورے پڑے جو زیادہ شدید نہیں تھے۔ اب اس کی حالت بہتر تھی، نقاہت دور ہو رہی تھی۔ اعصاب میں پہلا سا تناؤ بھی نہیں تھا۔ دل کی رفتار ٹھیک تھی۔ ڈاکٹروں کا خیال تھا کہ اب وہ خطرے سے باہر ہے۔ لیکن ان کا تعجب بدستور قائم تھا کہ وہ بچ کیسے گیا۔',
     'له یوې میاشتې زیات وخت تېر شو. په دې موده کې پر اختر د زړه دوه درې دورې راغلې چې ډېرې سختې نه وې. اوس یې حالت ښه و، کمزوري یې لرې کېده. په عصابو کې یې پخوانی فشار هم نه و. د زړه ټکان یې سم و. ډاکټرانو فکر کاوه چې اوس له خطره وتلی؛ خو حیرانتیا یې لا پاتې وه چې څنګه ژوندی پاتې شو.'),
    ('Akhtar laughed to himself. He knew who had saved him. It was no injection.', 'اختر دل ہی دل میں ہنستا تھا۔ اسے معلوم تھا کہ اسے بچانے والا کون ہے۔ وہ کوئی انجکشن نہیں تھا۔', 'اختر په زړه کې خندل. پوهېده چې څوک یې ژغورونکی دی. هغه کومه پېچکاري نه وه.'),
]: t.p(*x)
rec = BOOK.record(t, 'urdu12-u7-text-4', 'Lesson text (4)', 'متنِ سبق (۴)', 'د لوست متن (۴)', 35, [60, 61])
issues = [{'id': 'urdu12-pdf035', 'unit': 7, 'printedPage': 60, 'description': 'First word of p.60 is cut at the gutter (“[دم]اغ نے”), restored from context. Printed punctuation retained: question mark outside the closing quote in “…دعا مانگی تھی‘‘؟”; Akhtar’s reply “واہ منظور میاں واہ…” printed without quotation marks.'}]

if __name__ == '__main__':
    BOOK.save(35, [(7, rec)], issues=issues)
