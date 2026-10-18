"""PDF90 (printed 167–168): "Désirée's Baby" full text, part 3 (ending); About the author; Glossary avalanche–menace."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
s = Builder()
P = [
    ('It was an October afternoon; the sun was just sinking. Out in the still fields the negroes were picking cotton.',
     'اکتوبر کی ایک سہ پہر تھی؛ سورج ابھی ڈوب رہا تھا۔ ساکت کھیتوں میں حبشی کپاس چن رہے تھے۔',
     'د اکتوبر یوه غرمه وه؛ لمر لا ډوبېده. په چوپو کروندو کې تورپوستو پنبه ټوله کوله.'),
    ("Desiree had not changed the thin white garment nor the slippers which she wore. Her hair was uncovered and the sun's rays brought a golden gleam from its brown meshes. She did not take the broad, beaten road which led to the far-off plantation of Valmondé. She walked across a deserted field, where the stubble bruised her tender feet, so delicately shod,and tore her thin gown to shreds.",
     'دیزیرے نے نہ تو اپنا پتلا سفید لباس بدلا تھا اور نہ ہی جوتے جو اس نے پہن رکھے تھے۔ اس کے بال کھلے تھے اور سورج کی کرنیں اس کے بھورے گچھوں سے سنہری چمک نکال رہی تھیں۔ اس نے وہ چوڑی، پامال سڑک نہ لی جو دور والمونڈے کے کھیتوں تک جاتی تھی۔ وہ ایک ویران کھیت کے پار چلی، جہاں فصل کے ٹھنٹھوں نے اس کے نازک جوتوں والے نرم پاؤں زخمی کر دیے اور اس کا پتلا گاؤن چیتھڑے چیتھڑے کر دیا۔',
     'دېزیرې نه خپله نرۍ سپینه جامه بدله کړې وه او نه هغه چپلکې چې پښو کې یې وې. وېښتان یې لوڅ وو او د لمر وړانګو یې له نسواري تارونو طلايي ځلا راوېسته. هغې هغه پراخه، تکول شوې لار وانه خیسته چې د والمونډې لرې کښتزار ته تله. هغه د یوې شاړې کروندې له منځه تېره شوه، چېرته چې د رېبل شوي فصل ډډونو د هغې نرمې پښې چې په نازکو بوټانو کې وې ټپي کړې، او نری کالی یې ټوټې ټوټې کړ.'),
    ('She disappeared among the reeds and willows that grew thick along the banks of the deep, sluggish stream; and she did not come back again.',
     'وہ ان سرکنڈوں اور بید کے درختوں میں غائب ہو گئی جو گہری، سست رو ندی کے کناروں پر گھنے اگے ہوئے تھے؛ اور وہ پھر کبھی واپس نہ آئی۔',
     'هغه د هغو نیلونو او ولو ترمنځ ورکه شوه چې د ژورې، سستې ویالې پر غاړو ګڼ شنه شوي وو؛ او بیا بېرته رانغله.'),
    ("Some weeks later there was a curious scene enacted at L'Abri. In the centre of the smoothly swept back yard was a great bonfire. Armand Aubigny sat in the wide hallway that commanded a view of the spectacle; and it was he who dealt out to a half dozen negroes the material which kept this fire ablaze.",
     'کچھ ہفتوں بعد لابری میں ایک عجیب منظر پیش آیا۔ صفائی سے جھاڑو دیے گئے پچھلے صحن کے بیچ ایک بڑا الاؤ تھا۔ آرمانڈ اوبینی کشادہ راہداری میں بیٹھا تھا جہاں سے اس تماشے کا نظارہ ہوتا تھا؛ اور وہی تھا جو آدھ درجن حبشیوں کو وہ سامان دے رہا تھا جو اس آگ کو بھڑکائے رکھتا تھا۔',
     'څو اونۍ وروسته په لابري کې یوه عجیبه صحنه ترسره شوه. د پاک جارو شوي شاتني انګړ په منځ کې یو لوی اور بل و. ارمانډ اوبیني په پراخه دهلیز کې ناست و چې له هغه ځایه دا ننداره لیدل کېده؛ او همدی و چې نیمې درجن تورپوستو ته یې هغه توکي ورکول چې دا اور یې بل ساته.'),
    ('A graceful cradle of willow, with all its dainty furbishings, was laid upon the pyre, which had already been fed with the richness of a priceless layette. Then there were silk gowns, and velvet and satin ones added to these; laces, too, and embroideries; bonnets and gloves; for the basket of flowers had been of rare quality.',
     'بید کا ایک خوبصورت جھولا، اپنی تمام نفیس آرائشوں کے ساتھ، اس چتا پر رکھا گیا جسے پہلے ہی نومولود کے بیش قیمت کپڑوں کے سامان کی دولت سے بھرا جا چکا تھا۔ پھر ریشمی گاؤن، اور مخمل اور ساٹن کے گاؤن ان میں شامل کیے گئے؛ لیس بھی، اور کڑھائیاں؛ ٹوپیاں اور دستانے؛ کیونکہ پھولوں کی ٹوکری (جہیز) نایاب معیار کی تھی۔',
     'د ولې یوه ښکلې زانګو، د خپلو ټولو نازکو سینګارونو سره، پر هغه اور کېښودل شوه چې مخکې د نوي زېږېدلي ماشوم د بې‌بیه جامو په بډاینه تغذیه شوی و. بیا ورېښمین کالي، او د مخمل او ساټن کالي ورسره زیات شول؛ لېسونه هم، او ګلدوزۍ؛ خولۍ او دستکشې؛ ځکه چې د ګلانو ټوکرۍ (جهېز) نادر کیفیت درلود.'),
    ("The last thing to go was a tiny bundle of letters; innocent little scribblings that Désirée had sent to him during the days of their espousal. There was the remnant of one back in the drawer from which he took them. But it was not Désirée's; it was part of an old letter from his mother to his father. He read it. She was thanking God for the blessing of her husband's love: —",
     'آخری چیز جو آگ میں گئی وہ خطوں کا ایک ننھا سا بنڈل تھا؛ معصوم سی تحریریں جو دیزیرے نے منگنی کے دنوں میں اسے بھیجی تھیں۔ جس دراز سے اس نے انہیں نکالا تھا اس میں ایک خط کا بچا ہوا حصہ پیچھے رہ گیا تھا۔ لیکن وہ دیزیرے کا نہیں تھا؛ وہ اس کی ماں کے اس کے باپ کو لکھے ایک پرانے خط کا حصہ تھا۔ اس نے اسے پڑھا۔ وہ اپنے شوہر کی محبت کی نعمت پر خدا کا شکر ادا کر رہی تھی: —',
     'وروستی شی چې اور ته لاړ د لیکونو یوه کوچنۍ بنډل وه؛ معصومې کوچنۍ لیکنې چې دېزیرې د کوژدې په ورځو کې ورته لېږلې وې. په هغه دراز کې چې ترې یې ایستلې وې، د یو لیک پاتې برخه شاته پاتې وه. خو هغه د دېزیرې نه و؛ د هغه د مور د یو زاړه لیک برخه وه چې د هغه پلار ته یې لیکلی و. هغه ولوست. هغې د خپل مېړه د مینې د نعمت لپاره د خدای شکر ادا کاوه: —'),
    ('"But, above all," she wrote, "night and day, I thank the good God for having so arranged our lives that our dear Armand will never know that his mother, who adores him, belongs to the race that is cursed with the brand of slavery."',
     '’’لیکن سب سے بڑھ کر،‘‘ اس نے لکھا، ’’دن رات میں نیک خدا کا شکر ادا کرتی ہوں کہ اس نے ہماری زندگیاں یوں ترتیب دیں کہ ہمارا پیارا آرمانڈ کبھی نہیں جانے گا کہ اس کی ماں، جو اسے دل و جان سے چاہتی ہے، اس نسل سے تعلق رکھتی ہے جس پر غلامی کا داغ لعنت بن کر لگا ہے۔‘‘',
     '"خو تر ټولو زیات،" هغې لیکلي وو، "شپه او ورځ د نېک خدای شکر کوم چې زموږ ژوند یې داسې برابر کړ چې زموږ ګران ارمانډ به هېڅکله پوه نه شي چې مور یې، چې په زړه یې ورسره مینه ده، هغه نژاد ته منسوبه ده چې د غلامۍ په داغ لعنت شوی."'),
]
for x in P: s.p(*x)
s.h('About the author', 'مصنفہ کے بارے میں', 'د لیکوالې په اړه')
s.p('Kate Chopin (February 8, 1850 – August 22, 1904) was an American author of short stories and novels based in Louisiana. She is considered by scholars to have been a forerunner of American 20th-century feminist authors.',
    'کیٹ شوپن (8 فروری 1850 – 22 اگست 1904) لوزیانا میں مقیم ایک امریکی افسانہ نگار اور ناول نگار تھیں۔ محققین انہیں بیسویں صدی کی امریکی نسائی مصنفات کی پیش رو سمجھتے ہیں۔',
    'کېټ شوپن (د 1850 د فبرورۍ 8 – د 1904 د اګسټ 22) په لوزیانا کې مېشته امریکايي د لنډو کیسو او ناولونو لیکواله وه. پوهان هغه د شلمې پېړۍ د امریکايي ښځپالو لیکوالو مخکښه ګڼي.')
rec = BOOK.record(s, 'eng12-u17-text-3', "Désirée's Baby (3); About the author", 'دیزیرے کا بچہ (3)؛ مصنفہ کے بارے میں', 'د دېزیرې ماشوم (3)؛ د لیکوالې په اړه', 90, [167])

g = Builder()
g.h('Glossary', 'فرہنگ', 'وییپانګه')
BL = ('[meaning left blank in the printed book]', '[درسی کتاب میں معنی خالی چھوڑے گئے ہیں]', '[په چاپي کتاب کې مانا تشه پرېښودل شوې]')
gloss(g, 'eng12-u17-gloss-a', [
    ('avalanche(n)', 'a mass of snow, ice and rock that falls down the side of a mountain', 'برف، یخ اور چٹانوں کا تودہ جو پہاڑ کی ڈھلوان سے نیچے گرتا ہے', 'د واورې، یخ او ډبرو یوه کتله چې د غره له اړخه ښکته لوېږي'),
    ('avert(v)', 'to prevent something bad or dangerous from happening', 'کسی بری یا خطرناک چیز کو ہونے سے روکنا', 'د یو بد یا خطرناک شي د پېښېدو مخه نیول'),
    ('Bayou(n)', 'a branch of a river in the southern US that moves very slowly and has many plants growing in it', 'جنوبی امریکہ میں دریا کی ایک شاخ جو بہت آہستہ بہتی ہے اور جس میں بہت سے پودے اگتے ہیں', 'د جنوبي امریکا د سیند یوه څانګه چې ډېره ورو بهېږي او پکې ډېر بوټي شنه کېږي'),
    ('brand(n)', 'a mark made with a piece of hot metal, especially on farm animals to show who owns them', 'گرم دھات کے ٹکڑے سے لگایا گیا نشان، خاص طور پر مویشیوں پر یہ ظاہر کرنے کے لیے کہ وہ کس کی ملکیت ہیں', 'د تودوخې فلز په ټوټه جوړه شوې نښه، په ځانګړي ډول پر کورني څاروي ترڅو وښيي چې د چا دي'),
    ('canopy(n)', 'a cover that is fixed or hangs above a bed, seat, etc. as a shelter or decoration', 'ایک غلاف جو پلنگ، نشست وغیرہ کے اوپر سائبان یا سجاوٹ کے لیے لگایا یا لٹکایا جاتا ہے', 'یو پوښ چې د کټ، څوکۍ او نورو پورته د سیوري یا سینګار لپاره نښلول یا ځړول کېږي'),
    ('clammy(adj.)', 'slightly wet in an unpleasant way', 'ناگوار انداز میں ہلکا سا گیلا', 'په ناخوښه ډول لږ لوند'),
    ('conviction(n)', BL[0], BL[1], BL[2]),
    ('dainty (adj.)', BL[0], BL[1], BL[2]),
    ('despairingly(adv.)', 'in a way that shows a loss of all hope', 'ایسے انداز میں جو ہر امید ختم ہونے کو ظاہر کرے', 'په داسې ډول چې د ټولې هیلې له لاسه ورکول ښيي'),
    ('frowns(n)', 'to make a serious, angry or worried expression by bringing your eyebrows closer together so that lines appear on your forehead', 'بھنویں قریب لا کر سنجیدہ، غصیلا یا پریشان تاثر بنانا تاکہ ماتھے پر لکیریں آ جائیں', 'د وروځو په نږدې کولو جدي، غوسه‌ناک یا اندېښمن څرګندونه جوړول ترڅو پر تندي کرښې راشي'),
    ('headlong(adv.)', 'with the head first and the rest of the body following', 'سر پہلے اور باقی جسم پیچھے', 'سر مخکې او پاتې بدن ورپسې'),
    ('hysterically(adv.)', 'in an extremely excited way and without any control, often with crying or laughter', 'انتہائی جوش میں اور بے قابو ہو کر، اکثر روتے یا ہنستے ہوئے', 'په ډېر جوش او بې‌کنټروله ډول، ډېری وخت د ژړا یا خندا سره'),
    ('imperious(adj.)', 'expecting people to obey you and treating them as if they are not as important as you', 'لوگوں سے اطاعت کی توقع رکھنا اور ان سے ایسا برتاؤ کرنا جیسے وہ آپ جتنے اہم نہ ہوں', 'له خلکو د اطاعت تمه لرل او داسې چلند ورسره کول لکه ستاسو په څېر مهم نه وي'),
    ('indulgent(adj.)', '(usually disapproving) tending to allow somebody to have or do whatever they want', '(عموماً ناپسندیدگی میں) کسی کو جو چاہے رکھنے یا کرنے کی اجازت دینے کا رجحان رکھنے والا', '(معمولاً د ناخوښۍ په مانا) چا ته د هر څه لرلو یا کولو اجازه ورکولو ته تمایل لرونکی'),
    ('layette(n)', 'a set of clothes and other things for a new baby', 'نومولود بچے کے لیے کپڑوں اور دیگر چیزوں کا مجموعہ', 'د نوي زېږېدلي ماشوم لپاره د جامو او نورو شیانو ټولګه'),
    ('listlessly(adv.)', 'without energy or enthusiasm', 'بغیر توانائی یا جوش کے', 'پرته له انرژۍ یا لېوالتیا'),
    ('mahogany(n)', 'the hard red-brown wood of a tropical tree, used for making furniture', 'ایک گرمسیری درخت کی سخت سرخی مائل بھوری لکڑی، جو فرنیچر بنانے میں استعمال ہوتی ہے', 'د یوې تودې سیمې د ونې کلک سور-نسواري لرګی، چې د فرنیچر جوړولو لپاره کارېږي'),
    ('menace(n)', 'to be a possible danger to something/somebody', 'کسی چیز/شخص کے لیے ممکنہ خطرہ ہونا', 'یو شي/چا ته احتمالي خطر کېدل'),
])
gl = BOOK.record(g, 'eng12-u17-glossary-a', 'Glossary (avalanche – menace)', 'فرہنگ (avalanche – menace)', 'وییپانګه (avalanche – menace)', 90, [168])
issues = [{'id': 'eng12-p167-168', 'unit': 17, 'printedPage': 168, 'description': 'Glossary leaves the meanings of “conviction (n)” and “dainty (adj.)” blank; shown as blank-in-book notes. Also retained: “frowns(n)” and “menace(n)” defined with verb phrases; “Bayou” (not in the text); spelling “Desiree” without accents once on p.167; “shod,and”.'}]

if __name__ == '__main__':
    BOOK.save(90, [(17, rec), (17, gl)], issues=issues)
