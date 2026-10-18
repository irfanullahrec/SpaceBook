"""PDF95 (printed 177–178): 'Lines from the Deserted Village' (Oliver Goldsmith, 1770 — public domain) full poem line by line; About the poet; Glossary a breath–bowers."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
s = Builder()
s.h('Lines From The Deserted Village — BY OLIVER GOLDSMITH', 'اجڑے گاؤں سے اشعار — اولیور گولڈ اسمتھ', 'له وران کلي څخه بیتونه — اولیور ګولډسمیټ')
ST = [
    [("Sweet Auburn ! loveliest village of the plain,", 'پیارے آبرن! میدان کے سب سے دلکش گاؤں،', 'خوږه اوبرنه! د میدان تر ټولو ښکلی کلیه،'),
     ("Where health and plenty chear'd the labouring swain,", 'جہاں صحت اور فراوانی محنتی دہقان کو شاد رکھتی تھی،', 'چېرته چې روغتیا او پرېمانۍ زیارکښ بزګر خوشحاله ساته،'),
     ("Where smiling spring its earliest visit paid,", 'جہاں مسکراتی بہار سب سے پہلے آتی تھی،', 'چېرته چې موسکا کوونکی پسرلی تر ټولو وړاندې راتلو،'),
     ("And parting summer's ling'ring blooms delay'd:", 'اور رخصت ہوتی گرمی کے دیر تک ٹھہرنے والے پھول دیر سے مرجھاتے تھے:', 'او د تلونکي اوړي ځنډېدونکي ګلونه وروسته رژېدل:')],
    [("Dear lovely bowers of innocence and ease,", 'معصومیت اور سکون کے پیارے، دلکش کنج،', 'د بې‌ګناهۍ او ارامۍ ګرانو، ښکلو سیوریو،'),
     ("Seats of my youth, when every sport could please,", 'میری جوانی کے ٹھکانے، جب ہر کھیل خوش کرتا تھا،', 'زما د ځوانۍ ځایونو، کله چې هره لوبه خوښوله،'),
     ("How often have I loiter'd o'er thy green,", 'کتنی بار میں تیرے سبزہ زار پر بے مقصد گھوما ہوں،', 'څو ځله زه ستا په شنه ډګر بې‌موخې ګرځېدلی یم،'),
     ("Where humble happiness endear'd each scene;", 'جہاں سادہ سی خوشی ہر منظر کو عزیز بنا دیتی تھی؛', 'چېرته چې ساده خوښۍ هره منظره ګرانه کوله؛'),
     ("How often have I paus'd on every charm,", 'کتنی بار میں ہر دلکشی پر ٹھہرا ہوں،', 'څو ځله زه په هره ښکلا ودرېدلی یم،')],
    [("The shelter'd cot, the cultivated farm,", 'محفوظ جھونپڑا، کاشت شدہ کھیت،', 'خوندي کوډله، کرل شوی پټی،'),
     ("The never-failing brook, the busy mill,", 'کبھی نہ سوکھنے والی ندی، مصروف چکی،', 'هېڅکله نه وچېدونکې ویاله، بوخت ژرنده،'),
     ("The decent church that topp'd the neighbouring hill,", 'باوقار گرجا جو پڑوسی پہاڑی کی چوٹی پر تھا،', 'باوقاره کلیسا چې د ګاونډي غونډۍ پر سر وه،'),
     ("The hawthorn bush, with seats beneath the shade,", 'شہتوت نما کانٹے دار جھاڑی، جس کے سائے تلے نشستیں تھیں،', 'د ازغي بوټی، چې سیوري لاندې یې ناستې وې،'),
     ("For talking age and whisp'ring lovers made;", 'جو باتیں کرتے بوڑھوں اور سرگوشی کرتے عاشقوں کے لیے بنی تھیں؛', 'چې د خبرې کوونکو زړو او پسپس کوونکو مینانو لپاره جوړې وې؛')],
    [("How often have I bless'd the coming day,", 'کتنی بار میں نے آنے والے دن کو دعا دی،', 'څو ځله ما راتلونکې ورځ ته دعا کړې،'),
     ("When toil remitting lent its turn to play,", 'جب محنت نے ڈھیل دے کر کھیل کو اپنی باری دی،', 'کله چې زیار سست شو او خپله نوبت یې لوبې ته ورکړ،'),
     ("And all the village train, from labour free,", 'اور گاؤں کا سارا قافلہ، محنت سے آزاد ہو کر،', 'او د کلي ټوله ډله، له کاره ازاده،'),
     ("Led up their sports beneath the spreading tree;", 'پھیلے ہوئے درخت کے نیچے اپنے کھیل شروع کرتا؛', 'د غځېدلې ونې لاندې یې خپلې لوبې پیلولې؛'),
     ("While many a pastime circled in the shade,", 'جبکہ سائے میں کئی مشغلے گھومتے رہتے،', 'په داسې حال کې چې په سیوري کې ډېرې ساتېرۍ ګرځېدې،')],
    [("The young contending as the old survey'd;", 'جوان مقابلہ کرتے اور بوڑھے دیکھتے؛', 'ځوانانو سیالي کوله او زړو کتل؛'),
     ("And many a gambol frolicked o'er the ground,", 'اور کئی اچھل کود میدان پر مستی کرتی،', 'او ډېرو ټوپونو په ډګر کې ساتېري کوله،'),
     ("And slights of art and feats of strength went round;", 'اور فن کے کرتب اور طاقت کے کارنامے چلتے رہتے؛', 'او د هنر چلونه او د ځواک کارنامې روانې وې؛'),
     ("And still as each repeated pleasure tir'd,", 'اور جب بھی کوئی بار بار کی خوشی تھکا دیتی،', 'او هر کله چې یوه تکرارېدونکې خوښي ستړې کړه،'),
     ("Succeeding sports the mirthful band inspir'd;", 'تو اگلے کھیل اس خوش باش ٹولی کو نیا جوش دیتے؛', 'نو راتلونکو لوبو خوشحاله ډلې ته نوی جوش ورکاوه؛')],
    [("The dancing pair that simply sought renown,", 'ناچتا جوڑا جو بس شہرت چاہتا تھا،', 'نڅاکوونکې جوړه چې یوازې یې شهرت غوښت،'),
     ("By holding out to tire each other down;", 'ایک دوسرے کو تھکا دینے تک ڈٹے رہ کر؛', 'د یو بل تر ستړي کولو پورې په ټینګ پاتې کېدو؛'),
     ("The swain mistrustless of his smutted face,", 'دہقان جو اپنے کالک لگے چہرے سے بے خبر تھا،', 'بزګر چې د خپل تور شوي مخ څخه ناخبره و،'),
     ("While secret laughter titter'd round the place;", 'جبکہ چپکے چپکے ہنسی ہر طرف کھلکھلاتی؛', 'په داسې حال کې چې پټې خندا شاوخوا کړسهار کاوه؛'),
     ("The bashful virgin's side-long looks of love,", 'شرمیلی دوشیزہ کی محبت بھری ترچھی نظریں،', 'د شرمنې پېغلې مینه‌ناکې کږې کتنې،')],
    [("The matron's glance that would those looks reprove;", 'بزرگ خاتون کی نگاہ جو ان نظروں پر ٹوکتی؛', 'د مشرې مېرمنې نظر چې پر هغو کتنو به یې ملامتي کوله؛'),
     ("These were thy charms, sweet village; sports like these,", 'یہی تیری دلکشیاں تھیں، پیارے گاؤں؛ ایسے کھیل،', 'دا ستا ښکلاوې وې، خوږه کلیه؛ دا ډول لوبې،'),
     ("With sweet succession, taught even toil to please;", 'خوشگوار تسلسل کے ساتھ، محنت کو بھی دلپذیر بنا دیتے؛', 'په خوږ تسلسل، حتی زیار ته یې د خوښولو درس ورکاوه؛'),
     ("These round thy bowers their chearful influence shed,", 'یہ تیرے کنجوں کے گرد اپنا خوشگوار اثر بکھیرتے،', 'دوی ستا د سیوریو شاوخوا خپل خوشحاله اغېز خپراوه،'),
     ("These were thy charms—But all these charms are fled.", 'یہی تیری دلکشیاں تھیں — مگر یہ سب دلکشیاں رخصت ہو چکیں۔', 'دا ستا ښکلاوې وې — خو دا ټولې ښکلاوې تښتېدلې دي.')],
    [("Ill fares the land, to hast'ning ills a prey,", 'برا حال ہے اس سرزمین کا، جو تیزی سے بڑھتی برائیوں کا شکار ہے،', 'بد حال دی د هغې ځمکې، چې د ګړندیو بدیو ښکار ده،'),
     ("Where wealth accumulates and men decay;", 'جہاں دولت جمع ہوتی ہے اور انسان زوال پذیر ہوتے ہیں؛', 'چېرته چې شتمني راټولېږي او انسانان زوال مومي؛'),
     ("Princes and lords may flourish, or may fade;", 'شہزادے اور امرا پھل پھول سکتے ہیں، یا مٹ سکتے ہیں؛', 'شهزادګان او اربابان کېدای شي وده وکړي، یا ورک شي؛'),
     ("A breath can make them as a breath has made;", 'ایک لفظ انہیں بنا سکتا ہے جیسے ایک لفظ نے بنایا ہے؛', 'یوه کلمه یې جوړولی شي لکه څنګه چې یوې کلمې جوړ کړي؛'),
     ("But a bold peasantry, their country's pride,", 'لیکن ایک دلیر کسان طبقہ، جو اپنے ملک کا فخر ہے،', 'خو یو زړور بزګر طبقه، چې د خپل هېواد ویاړ دی،'),
     ("When once destroy'd can never be supplied.", 'ایک بار تباہ ہو جائے تو کبھی پورا نہیں کیا جا سکتا۔', 'یو ځل چې ویجاړ شي هېڅکله بیا نه شي پوره کېدای.')],
]
for st in ST: s.group('lines', st)
rec = BOOK.record(s, 'eng12-u18-poem', 'Lines from the Deserted Village — poem', 'اجڑے گاؤں سے اشعار — نظم', 'له وران کلي څخه بیتونه — شعر', 95, [177, 178])
rec['sourceCoverIllustrationReview'] = 'Faded title watermark at the top of p.177 is decorative.'

a = Builder()
a.h('About the poet:', 'شاعر کے بارے میں:', 'د شاعر په اړه:')
a.p("Oliver Goldsmith was born on November 10, 1730 in Kilkenny West, Ireland and died on April 4, 1774 in London. He is best known for his novel The Vicar of Wakefield, his poem The Deserted Village (1770) and his plays The Good Natur'd Man and She Stoops to Conquer etc. He received his BA degree in February 1749 from Trinity College, Dublin. He was the son of an Anglo- Irish Clergyman, Charles Goldsmith.",
    'اولیور گولڈ اسمتھ 10 نومبر 1730 کو کلکینی ویسٹ، آئرلینڈ میں پیدا ہوئے اور 4 اپریل 1774 کو لندن میں وفات پائی۔ وہ اپنے ناول The Vicar of Wakefield، اپنی نظم The Deserted Village (1770) اور اپنے ڈراموں The Good Natur\'d Man اور She Stoops to Conquer وغیرہ کے لیے سب سے زیادہ مشہور ہیں۔ انہوں نے فروری 1749 میں ٹرنٹی کالج، ڈبلن سے بی اے کی ڈگری حاصل کی۔ وہ ایک اینگلو آئرش پادری چارلس گولڈ اسمتھ کے بیٹے تھے۔',
    'اولیور ګولډسمیټ د 1730 د نومبر په 10 په کیلکېني ویسټ، ایرلینډ کې زېږېدلی او د 1774 د اپرېل په 4 په لندن کې مړ شو. هغه د خپل ناول The Vicar of Wakefield، د خپل شعر The Deserted Village (1770) او د خپلو ډرامو The Good Natur\'d Man او She Stoops to Conquer او نورو له امله تر ټولو ډېر مشهور دی. هغه د 1749 په فبرورۍ کې د ډبلن له ټرینیټي کالج څخه د بي اې سند واخیست. هغه د یوه انګلو-ایرلینډي پادري چارلس ګولډسمیټ زوی و.')
a.h('Glossary', 'فرہنگ', 'وییپانګه')
gloss(a, 'eng12-u18-gloss-a', [
    ('a breath', 'a word', 'ایک لفظ', 'یوه کلمه'),
    ('bashful (adj.)', 'shy; timid', 'شرمیلا؛ جھجکنے والا', 'شرمن؛ وېرېدونکی'),
    ('bless (v)', 'give prayers to', 'دعا دینا', 'دعا ورکول'),
    ('bowers (n)', 'shaddy place surrounded by trees', 'درختوں سے گھری سایہ دار جگہ', 'په ونو راګیر سیوري لرونکی ځای'),
])
ab = BOOK.record(a, 'eng12-u18-about-glossary-a', 'About the poet; Glossary (a breath – bowers)', 'شاعر کے بارے میں؛ فرہنگ (a breath – bowers)', 'د شاعر په اړه؛ وییپانګه (a breath – bowers)', 95, [178])
ab['sourceCoverIllustrationReview'] = 'Portrait engraving of Oliver Goldsmith is decorative; not reproduced.'
issues = [{'id': 'eng12-p177-178', 'unit': 18, 'printedPage': 177, 'description': 'Goldsmith’s poem (1770) is public domain and given in full as printed, line by line, with stanza breaks as in the book (the book breaks stanzas mid-sentence). Printed spellings retained: “chear\'d”, “chearful”, “slights of art” (sleights), “Sweet Auburn !”. The “About the poet” heading is faint in the scan. Glossary retained: “shaddy”.'}]

if __name__ == '__main__':
    BOOK.save(95, [(18, rec), (18, ab)], issues=issues)
