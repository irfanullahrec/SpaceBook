"""PDF82 (printed 151–152): 'Tourist Attractions in Pakistan' (Diplomat magazine, UK, April 2020 — copyrighted) paragraph-wise summary, part 1."""
from class12_book_common import Book, Builder

BOOK = Book('english')
s = Builder()
s.h('Tourist Attractions in Pakistan', 'پاکستان میں سیاحتی مقامات', 'په پاکستان کې د ګرځندوی ځایونه')
s.p('[Paragraph-wise summary — the article was published in the UK magazine “Diplomat” in April 2020 and is a modern copyrighted text; read it in the printed textbook, pp. 151–155.]', '[پیراگراف وار خلاصہ — یہ مضمون اپریل 2020 میں برطانوی رسالے ’’ڈپلومیٹ‘‘ میں شائع ہوا اور جدید کاپی رائٹ شدہ متن ہے؛ اسے درسی کتاب کے صفحات 151–155 میں پڑھیں۔]', '[پراګراف په پراګراف لنډیز — دا مقاله د 2020 په اپرېل کې د بریتانیا په "ډیپلومېټ" مجله کې خپره شوې او نوی د کاپي رایټ لاندې متن دی؛ په چاپي درسي کتاب کې یې په 151–155 مخونو کې ولولئ.]')
P = [
    ('¶1: Pakistan has some of the most varied natural beauty in the world, is a cradle of ancient civilizations and a meeting place of religions and cultures; the World Economic Forum placed it in the top 25 per cent of global destinations for its UNESCO World Heritage Sites.',
     '¶1: پاکستان دنیا کے متنوع ترین قدرتی حسن کا حامل ہے، قدیم تہذیبوں کا گہوارہ اور مذاہب و ثقافتوں کا سنگم ہے؛ ورلڈ اکنامک فورم نے اسے یونیسکو کے عالمی ورثہ مقامات کی بنا پر دنیا کے سرفہرست 25 فیصد مقامات میں شامل کیا۔',
     '¶1: پاکستان د نړۍ تر ټولو رنګارنګ طبیعي ښکلا لري، د لرغونو تمدنونو زانګو او د مذهبونو او کلتورونو د یوځای کېدو ځای دی؛ د نړیوال اقتصادي فورم د یونسکو د نړیوال میراث د ځایونو له امله دا د نړۍ په غوره 25 سلنه ځایونو کې شمېرلی.'),
    ('¶2: From the great northern mountain ranges to the Indus delta in the south, with deserts and some of the highest peaks, Pakistan offers sightseeing, skiing, trekking and mountaineering, white-water rafting, trout fishing, jeep, camel and yak safaris, and remarkable plants and wildlife.',
     '¶2: شمال کے عظیم پہاڑی سلسلوں سے جنوب میں سندھ کے ڈیلٹا تک، صحراؤں اور بلند ترین چوٹیوں کے ساتھ، پاکستان سیر و تفریح، اسکیئنگ، ٹریکنگ اور کوہ پیمائی، دریائی رافٹنگ، ٹراؤٹ ماہی گیری، جیپ، اونٹ اور یاک سفاری، اور شاندار نباتات و حیوانات پیش کرتا ہے۔',
     '¶2: په شمال کې له لویو غرنیو لړیو څخه په سویل کې د سیند تر ډیلټا پورې، د دښتو او تر ټولو لوړو څوکو سره، پاکستان د لیدنې، سکي، پیاده ګرځېدو او غرختلو، د سیند په څپو کې کښتۍ چلولو، د ټراوټ کب نیولو، د جیپ، اوښ او یاک سفرونو او په زړه پورې نباتاتو او ژویو بلنه ورکوي.'),
    ('¶3: Its archaeological, historical and religious heritage attracts scholars and pilgrims; foreign tourist arrivals rose from under half a million in 2015 to over two million in 2019, and domestic tourism passed 40 million.',
     '¶3: اس کا آثارِ قدیمہ، تاریخی اور مذہبی ورثہ محققین اور زائرین کو کھینچتا ہے؛ غیر ملکی سیاحوں کی آمد 2015 میں نصف ملین سے کم سے بڑھ کر 2019 میں بیس لاکھ سے زیادہ ہو گئی، اور ملکی سیاحت 4 کروڑ سے تجاوز کر گئی۔',
     '¶3: د هغه لرغونپوهنیز، تاریخي او مذهبي میراث څېړونکي او زیارت کوونکي راکاږي؛ د بهرنیو ګرځندویانو راتګ له 2015 کې له نیم ملیون څخه کم څخه په 2019 کې له دوه ملیونو زیات شو، او کورنی ګرځندوی له 40 ملیونو واوښت.'),
    ("¶4: International rankings praised Pakistan: Condé Nast Traveller listed it first among 20 best holiday destinations for 2020, Lonely Planet called it tourism's next big thing, and Forbes named it one of the ten coolest places to visit in 2019.",
     '¶4: بین الاقوامی درجہ بندیوں نے پاکستان کی تعریف کی: کونڈے ناسٹ ٹریولر نے اسے 2020 کی 20 بہترین تعطیلاتی منزلوں میں پہلے نمبر پر رکھا، لونلی پلانیٹ نے اسے سیاحت کی اگلی بڑی چیز کہا، اور فوربز نے اسے 2019 میں جانے کی دس بہترین جگہوں میں شمار کیا۔',
     '¶4: نړیوالو درجه‌بندیو د پاکستان ستاینه وکړه: کونډې نیسټ ټراولر دا د 2020 د 20 غوره رخصتي ځایونو په سر کې کېښود، لونلي پلانېټ دا د ګرځندوی راتلونکی لوی شی وباله، او فوربز دا په 2019 کې د لیدو لپاره د لسو غوره ځایونو په ډله کې وشمېره.'),
    ("¶5: The British Backpacker Society ranked Pakistan the world's third-best adventure destination for 2020 and earlier called it one of the friendliest countries on earth; its landscape runs from northern mountains to central plains and deserts and the Arabian Sea, and its people are hospitable to foreigners.",
     '¶5: برٹش بیک پیکر سوسائٹی نے پاکستان کو 2020 کے لیے دنیا کی تیسری بہترین مہم جوئی کی منزل قرار دیا اور اس سے پہلے اسے دنیا کے دوستانہ ترین ممالک میں سے ایک کہا؛ اس کا منظر شمالی پہاڑوں سے وسطی میدانوں اور صحراؤں اور بحیرۂ عرب تک پھیلا ہے، اور اس کے لوگ غیر ملکیوں کے لیے مہمان نواز ہیں۔',
     '¶5: د بریتانیا بیک‌پیکر ټولنې پاکستان د 2020 لپاره د نړۍ درېیم غوره ماجراجویانه ځای وباله او مخکې یې د ځمکې تر ټولو دوستانه هېوادونو کې وشمېره؛ منظره یې له شمالي غرونو د منځنیو میدانونو او دښتو او عربي سمندر پورې غځېږي، او خلک یې له بهرنیانو سره مېلمه‌پال دي.'),
    ('¶6: Its ranges include the Himalayas, Karakoram and Hindukush; K2 (8,611 m), the second-highest peak on earth, is one of five of the world’s 14 highest peaks found here, drawing climbers from April to September.',
     '¶6: اس کے پہاڑی سلسلوں میں ہمالیہ، قراقرم اور ہندوکش شامل ہیں؛ کے ٹو (8,611 میٹر)، دنیا کی دوسری بلند ترین چوٹی، دنیا کی 14 بلند ترین چوٹیوں میں سے یہاں موجود پانچ میں سے ایک ہے، جو اپریل سے ستمبر تک کوہ پیماؤں کو کھینچتی ہیں۔',
     '¶6: د هغه غرنۍ لړۍ همالیه، قراقرم او هندوکش لري؛ کې ټو (8,611 متره)، د ځمکې دویمه لوړه څوکه، د نړۍ له 14 لوړو څوکو څخه د هغو پنځو یوه ده چې دلته دي، او له اپرېل تر سپتمبر پورې غرختونکي راکاږي.'),
    ('¶7: The 806 km Karakoram Highway along the old Silk Road to China is the highest trade route in the world; the nearby Mintaka Pass was crossed by famous travellers such as Fa Hien (4th century), Al-Beruni (11th century) and Marco Polo (13th century).',
     '¶7: پرانی شاہراہِ ریشم کے ساتھ چین تک 806 کلومیٹر طویل شاہراہِ قراقرم دنیا کا بلند ترین تجارتی راستہ ہے؛ قریبی درہ منتکا سے مشہور سیاح جیسے فاہیان (چوتھی صدی)، البیرونی (گیارہویں صدی) اور مارکو پولو (تیرہویں صدی) گزرے۔',
     '¶7: د زاړه ورېښمو لارې په اوږدو کې چین ته 806 کیلومتره قراقرم لویه لار د نړۍ تر ټولو لوړه سوداګریزه لاره ده؛ نږدې منتکا درې څخه نامتو سیلانیان لکه فاهیان (څلورمه پېړۍ)، البیروني (یوولسمه پېړۍ) او مارکو پولو (دیارلسمه پېړۍ) تېر شوي.'),
    ('¶8: The Baltoro Glacier in the eastern Karakoram, one of the largest valley glaciers, is visited for K2, Broad Peak and the Gasherbrum peaks, and its meltwater is a lifeline for much of northern Pakistan.',
     '¶8: مشرقی قراقرم میں بلتورو گلیشیئر، جو سب سے بڑے وادی گلیشیئرز میں سے ہے، کے ٹو، براڈ پیک اور گاشربرم چوٹیوں کی وجہ سے دیکھا جاتا ہے، اور اس کا پگھلا پانی شمالی پاکستان کے بڑے حصے کے لیے زندگی کا سہارا ہے۔',
     '¶8: په ختیځ قراقرم کې د بلتورو ګلېشیر، چې یو له لویو درې‌ییزو ګلېشیرونو دی، د کې ټو، براډ پیک او ګاشربروم څوکو له امله لیدل کېږي، او د ویلې شوې اوبه یې د شمالي پاکستان د زیاتې برخې لپاره د ژوند سرچینه ده.'),
    ('¶9: Khyber Pakhtunkhwa is known for the Kaghan and Swat valleys and the Khyber Pass; the northern areas (72,496 sq km) have magnificent valleys — Gilgit, Hunza and Skardu — among peaks over 8,000 metres.',
     '¶9: خیبر پختونخوا وادیٔ کاغان اور سوات اور درۂ خیبر کے لیے مشہور ہے؛ شمالی علاقہ جات (72,496 مربع کلومیٹر) میں 8,000 میٹر سے بلند چوٹیوں کے درمیان شاندار وادیاں — گلگت، ہنزہ اور سکردو — ہیں۔',
     '¶9: خیبر پښتونخوا د کاغان او سوات درو او د خیبر درې له امله مشهور دی؛ شمالي سیمې (72,496 مربع کیلومتره) د 8,000 مترو څخه د لوړو څوکو ترمنځ ښکلې درې — ګلګت، هنزه او سکردو — لري.'),
    ('¶10: In Gilgit-Baltistan, Hunza on the Hunza River was a traditional resting place for travellers; the valley is home to snow leopards, markhors, ibexes and red foxes, and Attabad Lake’s turquoise waters have a violent origin (continued on p. 153).',
     '¶10: گلگت بلتستان میں دریائے ہنزہ کے کنارے ہنزہ مسافروں کا روایتی پڑاؤ تھا؛ وادی برفانی چیتوں، مارخوروں، آئبیکس اور سرخ لومڑیوں کا مسکن ہے، اور عطا آباد جھیل کے فیروزی پانی کی ابتدا ایک تباہ کن واقعے سے ہوئی (صفحہ 153 پر جاری)۔',
     '¶10: په ګلګت بلتستان کې د هنزې سیند پر غاړه هنزه د مسافرو دودیز تمځای و؛ دره د واورینو پړانګانو، مارخورانو، غرنیو وزو او سرو ګیدړو کور دی، او د عطاآباد جهیل فیروزي اوبه یو ویجاړونکی پیل لري (په 153 مخ کې دوام).'),
]
for x in P: s.p(*x)
rec = BOOK.record(s, 'eng12-u16-text-1', 'Tourist Attractions in Pakistan — summary (1)', 'پاکستان میں سیاحتی مقامات — خلاصہ (1)', 'په پاکستان کې د ګرځندوی ځایونه — لنډیز (1)', 82, [151, 152])
rec['sourceGap'] = 'Modern copyrighted magazine article (Diplomat, UK, April 2020); paragraph-wise summary in the app, not verbatim. Printed pp. 151–152.'
rec['sourceCoverIllustrationReview'] = 'Two photographs (yaks on a plateau; a mountain lake) are decorative; not reproduced.'
issues = [{'id': 'eng12-u16-copyright', 'unit': 16, 'printedPage': 151, 'description': 'The reading text is credited (p.155) to the article “Pakistan\'s Tourist Attractions” in the UK magazine Diplomat, April 2020 — modern and copyrighted; the app carries a paragraph-wise summary with a sourceGap note. Printed spellings noted: “Fe Hien” (Fa Hien), “a large portion northern Pakistan\'s population”.'}]

if __name__ == '__main__':
    BOOK.save(82, [(16, rec)], issues=issues)
