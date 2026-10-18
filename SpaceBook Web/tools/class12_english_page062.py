"""PDF62 (printed 111–112): "All the World's a Stage" (Shakespeare, As You Like It II.vii — public domain) full text; About the Poet; Glossary (a world too wide … justice)."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
L = [
    ("All the world's a stage,", 'ساری دنیا ایک اسٹیج ہے،', 'ټوله نړۍ یوه سټېج ده،'),
    ('And all the men and women merely players;', 'اور تمام مرد و زن محض اداکار ہیں؛', 'او ټول نارینه او ښځې یوازې لوبغاړي دي؛'),
    ('They have their exits and their entrances,', 'ان کے جانے اور آنے کے مواقع ہیں،', 'هغوی خپل وتل او ننوتل لري،'),
    ('And one man in his time plays many parts,', 'اور ایک آدمی اپنی زندگی میں بہت سے کردار ادا کرتا ہے،', 'او یو سړی په خپل وخت کې ډېر رولونه لوبوي،'),
    ('His acts being seven ages. At first, the infant,', 'اس کے ایکٹ سات ادوار ہیں۔ پہلے شیر خوار بچہ،', 'د هغه پردې اووه عمرونه دي. لومړی، تی‌خور ماشوم،'),
    ("Mewling and puking in the nurse's arms.", 'دایہ کی گود میں روتا اور قے کرتا ہوا۔', 'د دایې په غېږ کې ژاړي او کانګې کوي.'),
    ('Then the whining schoolboy, with his satchel', 'پھر روتا بسورتا اسکول کا لڑکا، اپنے بستے کے ساتھ', 'بیا ګیله‌من ښوونځي هلک، د خپل بستې سره'),
    ('And shining morning face, creeping like snail', 'اور صبح کے چمکتے چہرے کے ساتھ، گھونگے کی طرح رینگتا ہوا', 'او د سهار ځلانده مخ سره، د حلزون په څېر خزي'),
    ('Unwillingly to school. And then the lover,', 'بے دلی سے اسکول کی طرف۔ اور پھر عاشق،', 'په بې‌زړه‌توب ښوونځي ته. او بیا عاشق،'),
    ('Sighing like furnace, with a woeful ballad', 'بھٹی کی طرح آہیں بھرتا ہوا، ایک غمگین گیت کے ساتھ', 'د بټۍ په څېر اسوېلي کاږي، د یوې غمجنې سندرې سره'),
    ("Made to his mistress' eyebrow. Then a soldier,", 'جو اس نے اپنی محبوبہ کی بھنوؤں پر لکھا۔ پھر سپاہی،', 'چې د خپلې معشوقې پر وروځو یې جوړه کړې. بیا یو سرتېری،'),
    ('Full of strange oaths and bearded like the pard,', 'عجیب قسموں سے بھرا اور چیتے کی طرح داڑھی والا،', 'له عجیبو قسمونو ډک او د پړانګ په څېر ږیره لرونکی،'),
    ('Jealous in honor, sudden and quick in quarrel,', 'عزت کے معاملے میں غیرت مند، جھگڑے میں اچانک اور تیز،', 'په عزت کې غیرتي، په شخړه کې ناڅاپي او ګړندی،'),
    ('Seeking the bubble reputation', 'بلبلے جیسی شہرت کی تلاش میں', 'د پوکڼۍ په څېر شهرت لټوي'),
    ("Even in the cannon's mouth. And then the justice,", 'توپ کے دہانے میں بھی۔ اور پھر منصف،', 'حتی د توپ په خوله کې. او بیا قاضي،'),
    ('In fair round belly with good capon lined,', 'اچھے مرغ کھا کھا کر گول مٹول پیٹ والا،', 'د ښو چرګانو په خوړلو ګردې ګېډې سره،'),
    ('With eyes severe and beard of formal cut,', 'سخت آنکھوں اور باقاعدہ تراشی ہوئی داڑھی کے ساتھ،', 'د سختو سترګو او رسمي پرې شوې ږیرې سره،'),
    ('Full of wise saws and modern instances;', 'دانائی کے اقوال اور روزمرہ مثالوں سے بھرا؛', 'له حکیمانه متلونو او عادي بېلګو ډک؛'),
    ('And so he plays his part. The sixth age shifts', 'اور یوں وہ اپنا کردار ادا کرتا ہے۔ چھٹا دور بدل جاتا ہے', 'او همداسې خپل رول لوبوي. شپږم عمر بدلېږي'),
    ('Into the lean and slippered pantaloon,', 'دبلے پتلے، چپل پہنے بوڑھے میں،', 'په ډنګر، څپلۍ اغوستي زوړ سړي،'),
    ('With spectacles on nose and pouch on side;', 'ناک پر عینک اور پہلو میں تھیلی کے ساتھ؛', 'په پوزه عینکې او څنګ ته کڅوړه؛'),
    ('His youthful hose, well saved, a world too wide', 'اس کی جوانی کی سنبھال کر رکھی پتلون، بہت ہی ڈھیلی', 'د ځوانۍ پتلون یې، ښه ساتلی، ډېر پراخ'),
    ('For his shrunk shank, and his big manly voice,', 'اس کی سکڑی ہوئی پنڈلی کے لیے، اور اس کی بھاری مردانہ آواز،', 'د هغه د وچې پنډۍ لپاره، او د هغه لوی نارینه غږ،'),
    ('Turning again toward childish treble, pipes', 'پھر سے بچکانہ باریک آواز کی طرف لوٹتی ہوئی', 'بیا د ماشومانه نري غږ خوا ته اوړي،'),
    ('And whistles in his sound. Last scene of all,', 'اس کی آواز میں سیٹیاں اور باریکی آ جاتی ہے۔ سب سے آخری منظر،', 'او په غږ کې یې شپېلۍ راځي. تر ټولو وروستۍ صحنه،'),
    ('That ends this strange eventful history,', 'جو اس عجیب و غریب واقعات بھری کہانی کو ختم کرتا ہے،', 'چې دا عجیبه پېښو ډکه کیسه پای ته رسوي،'),
    ('Is second childishness and mere oblivion,', 'دوسرا بچپن اور محض فراموشی ہے،', 'دویم ماشومتوب او محض هېرېدنه ده،'),
    ('Sans teeth, sans eyes, sans taste, sans everything.', 'بغیر دانتوں کے، بغیر آنکھوں کے، بغیر ذائقے کے، بغیر ہر چیز کے۔', 'بې غاښونو، بې سترګو، بې خونده، بې هر څه.'),
]
p = Builder()
p.h("All the World's a Stage", 'ساری دنیا ایک اسٹیج ہے', 'ټوله نړۍ یوه سټېج ده')
for st in (L[:8], L[8:16], L[16:24], L[24:]): p.group('lines', st)
poem = BOOK.record(p, 'eng12-u12-poem', "All the World's a Stage — poem text", 'ساری دنیا ایک اسٹیج ہے — نظم', 'ټوله نړۍ یوه سټېج ده — شعر', 62, [111])
poem['sourceCoverIllustrationReview'] = 'Background artwork is decorative; not reproduced. Urdu/Pashto give a line-by-line rendering. (Speech from As You Like It, II.vii; public domain.)'

a = Builder()
a.h('About the Poet', 'شاعر کے بارے میں', 'د شاعر په اړه')
a.p("William Shakespeare was an English poet, playwright, and actor. He was born on 26 April 1564 in Stratford-upon-Avon. Shakespeare is widely regarded as the greatest writer in the English language and the world's pre-eminent dramatist. He is often called England's national poet and nicknamed the Bard of Avon. He wrote about 38 plays, 154 sonnets, two long narrative poems, and a few other verses. His plays have been translated into every major living language and are performed more often than those of any other playwright. Around 1613, at the age of 49, he retired to Stratford, where he died three years later. Few records of Shakespeare's private life survive. He died on 23 April 1616, at the age of 52.",
    'ولیم شیکسپیئر ایک انگریز شاعر، ڈراما نگار اور اداکار تھے۔ وہ 26 اپریل 1564 کو اسٹریٹ فورڈ اپون ایون میں پیدا ہوئے۔ شیکسپیئر کو بڑے پیمانے پر انگریزی زبان کا عظیم ترین ادیب اور دنیا کا ممتاز ترین ڈراما نگار مانا جاتا ہے۔ انہیں اکثر انگلستان کا قومی شاعر کہا جاتا ہے اور ’’بارڈ آف ایون‘‘ کا لقب دیا گیا۔ انہوں نے تقریباً 38 ڈرامے، 154 سانیٹ، دو طویل بیانیہ نظمیں اور چند دوسری نظمیں لکھیں۔ ان کے ڈراموں کا ہر بڑی زندہ زبان میں ترجمہ ہو چکا ہے اور یہ کسی بھی دوسرے ڈراما نگار سے زیادہ پیش کیے جاتے ہیں۔ تقریباً 1613 میں 49 سال کی عمر میں وہ اسٹریٹ فورڈ لوٹ آئے جہاں تین سال بعد ان کا انتقال ہوا۔ شیکسپیئر کی نجی زندگی کے بہت کم ریکارڈ باقی ہیں۔ وہ 23 اپریل 1616 کو 52 سال کی عمر میں فوت ہوئے۔',
    'ویلیم شکسپیر یو انګرېز شاعر، ډرامه‌لیکونکی او لوبغاړی و. هغه د 1564 کال د اپرېل په 26 په سټراټفورډ اپان ایون کې زېږېدلی. شکسپیر په پراخه کچه د انګلیسي ژبې تر ټولو ستر لیکوال او د نړۍ تر ټولو مخکښ ډرامه‌لیکونکی ګڼل کېږي. اکثرا د انګلستان ملي شاعر بلل کېږي او د "د ایون شاعر" لقب یې دی. هغه شاوخوا 38 ډرامې، 154 سانېټونه، دوه اوږده کیسه‌ییز شعرونه او ځینې نور بیتونه ولیکل. د هغه ډرامې په هره لویه ژوندۍ ژبه ژباړل شوې او تر هر بل ډرامه‌لیکونکي ډېرې لوبول کېږي. شاوخوا په 1613 کې، په 49 کلنۍ کې سټراټفورډ ته ستون شو، چېرته چې درې کاله وروسته مړ شو. د شکسپیر د شخصي ژوند ډېر لږ ریکارډونه پاتې دي. هغه د 1616 کال د اپرېل په 23 په 52 کلنۍ کې مړ شو.')
a.h('Glossary', 'فرہنگ', 'وییپانګه')
gloss(a, 'eng12-u12-gloss-a', [
    ('a world too wide', 'much too big', 'بہت ہی بڑا', 'ډېر لوی'),
    ('ages(n)', 'here, periods of time', 'یہاں، زمانے کے ادوار', 'دلته، د وخت دورې'),
    ('ballad (n)', 'a slow love song', 'محبت کا دھیما گیت', 'د مینې ورو سندره'),
    ("even in the cannon's mouth", "a 'cannon' was a large gun, and it's 'mouth' was at the front - so the man seeks his reputation even if it means standing in front of guns, i.e. going to war or getting in fights", "’’توپ‘‘ ایک بڑی بندوق تھی اور اس کا ’’دہانہ‘‘ سامنے ہوتا تھا — یعنی آدمی شہرت کی تلاش میں بندوقوں کے سامنے کھڑا ہونے تک کو تیار ہے، یعنی جنگ میں جانا یا لڑائیوں میں پڑنا", '"توپ" یوه لویه ټوپک وه او "خوله" یې مخې ته وه — یعنې سړی شهرت لټوي حتی که د ټوپکو مخې ته درېدل وي، یعنې جګړې ته تلل یا په شخړو کې ښکېلېدل'),
    ('eventful(adj.)', 'full of activity, containing lots of events', 'سرگرمیوں سے بھرپور، بہت سے واقعات والا', 'له فعالیت ډک، ډېرې پېښې لرونکی'),
    ('furnace (n)', 'an object which contains a fire, used for heating', 'وہ چیز جس میں آگ ہو اور جو گرم کرنے کے لیے استعمال ہو', 'هغه شی چې اور پکې وي او د تودولو لپاره کارېږي'),
    ("good capon lin'd", "'to line' means to fill something at the edges (e.g. 'line a tin for baking a cake') and 'capon' was chicken to eat - so the man was fat from eating good chicken", "’’لائن کرنا‘‘ کا مطلب ہے کسی چیز کو کناروں سے بھرنا (مثلاً کیک بنانے کے لیے سانچے کو لائن کرنا) اور ’’کیپن‘‘ کھانے کا مرغ تھا — یعنی آدمی اچھا مرغ کھا کھا کر موٹا ہو گیا تھا", '"لاین کول" مانا د یو شي څنډې ډکول (لکه د کېک د پخولو لپاره قالب لاین کول) او "کېپن" د خوړلو چرګ و — یعنې سړی د ښو چرګانو په خوړلو چاغ شوی و'),
    ('history(n)', 'here, a kind of play that talks about events in the past', 'یہاں، ڈرامے کی ایک قسم جو ماضی کے واقعات بیان کرے', 'دلته، د ډرامې یو ډول چې د تېرو پېښو په اړه خبرې کوي'),
    ('hose (n)', "tights, thin trousers that men wore in Shakespeare's time", 'تنگ پاجامہ، پتلی پتلون جو شیکسپیئر کے زمانے میں مرد پہنتے تھے', 'تنګ پتلون، نری پتلون چې د شکسپیر په وخت کې نارینه وو اغوسته'),
    ('instances (n)', "examples (as in 'for instance')", "مثالیں (جیسے 'for instance' میں)", "بېلګې (لکه په 'for instance' کې)"),
    ('jealous in honour', 'here, jealous means that someone takes care of something very carefully - so the young man takes great care of his honour, his reputation as a good man', 'یہاں ’’جیلس‘‘ کا مطلب ہے کہ کوئی کسی چیز کا بہت احتیاط سے خیال رکھے — یعنی نوجوان اپنی عزت، ایک اچھے آدمی کی ساکھ کا بہت خیال رکھتا ہے', 'دلته "جیلس" مانا دا ده چې څوک د یو شي ډېره پاملرنه کوي — یعنې ځوان د خپل عزت، د یوه ښه سړي په توګه د خپل شهرت ډېره پاملرنه کوي'),
    ('justice(n)', 'here, a judge or magistrate - so someone very respected', 'یہاں، جج یا مجسٹریٹ — یعنی بہت معزز شخص', 'دلته، قاضي یا مجسټرېټ — یعنې ډېر درناوی لرونکی کس'),
])
ab = BOOK.record(a, 'eng12-u12-about-glossary-a', 'About the Poet; Glossary (1)', 'شاعر کے بارے میں؛ فرہنگ (1)', 'د شاعر په اړه؛ وییپانګه (1)', 62, [112])
ab['sourceCoverIllustrationReview'] = 'Portrait of Shakespeare is decorative; not reproduced.'
issues = [{'id': 'eng12-p111-112', 'unit': 12, 'printedPage': 111, 'description': "Poem lines kept as printed (“Sighing like furnace”, “Jealous in honor”); the printed underlining of “ballad” and “formal” is not reproduced. Glossary retains “it's 'mouth'” and “lin'd” (poem: lined). About the Poet: died aged 52 (born 1564, died 1616)."}]

if __name__ == '__main__':
    BOOK.save(62, [(12, poem), (12, ab)], issues=issues)
