"""PDF84 (printed 155–156): 'Tourist Attractions in Pakistan' summary part 3 (¶18 cont.–¶22), Reference & Source; Glossary rows alluvial–solace."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
s = Builder()
P = [
    ('¶18 (cont.): The region of modern Pakistan is home to the oldest Asian civilisation — and one of the oldest in the world after Mesopotamia and Egypt — the Indus Valley Civilisation (2,500–1,500 BC).',
     '¶18 (جاری): جدید پاکستان کا خطہ قدیم ترین ایشیائی تہذیب — اور میسوپوٹیمیا اور مصر کے بعد دنیا کی قدیم ترین تہذیبوں میں سے ایک — وادیٔ سندھ کی تہذیب (2,500–1,500 ق م) کا گھر ہے۔',
     '¶18 (دوام): د نني پاکستان سیمه د اسیا تر ټولو زوړ تمدن — او له میسوپوتامیا او مصر وروسته د نړۍ یو له زړو تمدنونو — د سیند د درې تمدن (2,500–1,500 م خ) کور دی.'),
    ('¶19: Pakistan is a land of love, hospitality and spiritual heritage — resting place of Sufi mystics of Islam, Hindu tiraths dating to 3,000 BC, Buddhist sites of Gandhara, and Baba Guru Nanak, founder of Sikhism — and it has worked to preserve churches, gurdwaras, temples, mosques, museums, tombs, forts and shrines.',
     '¶19: پاکستان محبت، مہمان نوازی اور روحانی ورثے کی سرزمین ہے — اسلام کے صوفیائے کرام، 3,000 ق م کے ہندو تیرتھوں، گندھارا کے بدھ مقامات، اور سکھ مذہب کے بانی بابا گرو نانک کی آرام گاہ — اور اس نے گرجا گھروں، گوردواروں، مندروں، مساجد، عجائب گھروں، مقبروں، قلعوں اور مزارات کے تحفظ کے لیے کام کیا ہے۔',
     '¶19: پاکستان د مینې، مېلمه‌پالنې او روحاني میراث ځمکه ده — د اسلام د صوفیانو، د 3,000 م خ د هندو تیرتونو، د ګندهارا د بودايي ځایونو، او د سکه دین د بنسټګر بابا ګرو نانک د ارامځای — او د کلیساګانو، ګوردوارو، معبدونو، جوماتونو، موزیمونو، مقبرو، کلاګانو او زیارتونو د ساتنې لپاره یې کار کړی.'),
    ('¶20: Buddhism found followers and patrons in Gandhara; Pakistan holds sacred relics and fine Buddhist art and architecture, especially the ruins of Taxila, where — the text states — the first ever university was founded in the 10th century BC.',
     '¶20: بدھ مت کو گندھارا میں پیروکار اور سرپرست ملے؛ پاکستان مقدس تبرکات اور عمدہ بدھ فن و تعمیر کا امین ہے، خاص طور پر ٹیکسلا کے کھنڈرات، جہاں — متن کے مطابق — دسویں صدی ق م میں پہلی جامعہ قائم ہوئی۔',
     '¶20: بودايي دین په ګندهارا کې پیروان او ملاتړي وموندل؛ پاکستان سپېڅلي تبرکات او غوره بودايي هنر او معماري ساتي، په ځانګړي ډول د ټیکسلا کنډوالې، چېرته چې — د متن له مخې — په لسمه پېړۍ م خ کې لومړنی پوهنتون جوړ شو.'),
    ('¶21: Punjab was the centre of the Sikh Gurus, so many Sikh sacred sites are in Pakistan, such as Gurdwara Darbar Sahib, Kartarpur; Pakistan opened the visa-free Kartarpur Corridor for Indian Sikh pilgrims as a sign of goodwill and interfaith harmony, and maintains all gurdwaras with care.',
     '¶21: پنجاب سکھ گروؤں کا مرکز تھا، اس لیے سکھوں کے بہت سے مقدس مقامات پاکستان میں ہیں، جیسے گوردوارہ دربار صاحب کرتارپور؛ پاکستان نے خیر سگالی اور بین المذاہب ہم آہنگی کی علامت کے طور پر بھارتی سکھ یاتریوں کے لیے بغیر ویزا کرتارپور راہداری کھولی، اور تمام گوردواروں کی دیکھ بھال کرتا ہے۔',
     '¶21: پنجاب د سکه ګرووانو مرکز و، نو د سکهانو ډېر سپېڅلي ځایونه په پاکستان کې دي، لکه د کرتارپور دربار صاحب ګوردواره؛ پاکستان د ښه نیت او د مذهبونو ترمنځ همغږۍ د نښې په توګه د هندي سکه زایرینو لپاره بې‌ویزې د کرتارپور دهلیز پرانیست، او ټولې ګوردوارې په پاملرنه ساتي.'),
    ('¶22: Pakistan is also a land of saints and Sufis who preached peace and universal love and promoted religious harmony; the shrines of Data Ganj Bakhsh Hajveri, Abdullah Shah Ghazi, Lal Shahbaz Qalandar, Sachal Sarmast and Bahauddin Zakaria are worth visiting for spiritual solace.',
     '¶22: پاکستان اولیا اور صوفیا کی سرزمین بھی ہے جنہوں نے امن اور عالمگیر محبت کا درس دیا اور مذہبی ہم آہنگی کو فروغ دیا؛ داتا گنج بخش ہجویری، عبداللہ شاہ غازی، لعل شہباز قلندر، سچل سرمست اور بہاؤالدین زکریا کے مزارات روحانی سکون کے لیے دیکھنے کے قابل ہیں۔',
     '¶22: پاکستان د اولیاوو او صوفیانو ځمکه هم ده چې د سولې او نړیوالې مینې درس یې ورکړ او مذهبي همغږي یې وده کړه؛ د داتا ګنج بخش هجویري، عبدالله شاه غازي، لعل شهباز قلندر، سچل سرمست او بهاوالدین زکریا زیارتونه د روحاني ارامۍ لپاره د لیدو وړ دي.'),
]
for x in P: s.p(*x)
s.h('Reference & Source', 'حوالہ اور ماخذ', 'حواله او سرچینه')
s.p('Published as article "PAKISTAN\'S TOURIST ATTRACTIONS" in a UK Magazine "Diplomate" in April, 2020.', 'اپریل 2020 میں برطانوی رسالے "Diplomate" میں مضمون "PAKISTAN\'S TOURIST ATTRACTIONS" کے طور پر شائع ہوا۔', 'د 2020 په اپرېل کې د بریتانیا په "Diplomate" مجله کې د "PAKISTAN\'S TOURIST ATTRACTIONS" مقالې په توګه خپره شوه.')
rec = BOOK.record(s, 'eng12-u16-text-3', 'Tourist Attractions in Pakistan — summary (3); source', 'پاکستان میں سیاحتی مقامات — خلاصہ (3)؛ ماخذ', 'په پاکستان کې د ګرځندوی ځایونه — لنډیز (3)؛ سرچینه', 84, [155])
rec['sourceGap'] = 'Modern copyrighted magazine article (Diplomat, UK, April 2020); paragraph-wise summary in the app, not verbatim. Printed p. 155.'

g = Builder()
g.h('Glossary', 'فرہنگ', 'وییپانګه')
gloss(g, 'eng12-u16-gloss-a', [
    ('alluvial (adj)', 'made of sand and earth that is left by rivers or floods', 'دریاؤں یا سیلاب کی چھوڑی ہوئی ریت اور مٹی سے بنا ہوا', 'له هغه شګو او خاورې جوړ چې سیندونه یا سېلابونه یې پرېږدي'),
    ('alpine (adj)', 'relating to high mountains', 'بلند پہاڑوں سے متعلق', 'له لوړو غرونو سره تړلی'),
    ('avifauna (adj)', 'the birds of a particular region, habitat, or geological period', 'کسی خاص خطے، مسکن یا ارضیاتی دور کے پرندے', 'د یوې ځانګړې سیمې، استوګنځي یا ځمکپوهنیز دور مرغان'),
    ('backdrop (n)', 'a painted cloth hung at the back of a theatre stage as part of the scenery.', 'تھیٹر کے اسٹیج کے پیچھے منظر کے حصے کے طور پر لٹکایا جانے والا رنگین کپڑا۔', 'یو رنګ شوی ټوکر چې د تیاتر د سټېج شاته د منظرې د برخې په توګه ځړول کېږي.'),
    ('captivating (adj)', 'taking all your attention; very attractive and interesting', 'پوری توجہ کھینچ لینے والا؛ بہت دلکش اور دلچسپ', 'ټوله پاملرنه ځانته اړوونکی؛ ډېر زړه‌راښکونکی او په زړه پورې'),
    ('coniferous (adj)', 'connected with any tree that produces hard dry fruit called cones', 'ایسے درخت سے متعلق جو کون کہلانے والا سخت خشک پھل دیتا ہے', 'له هغې ونې سره تړلی چې کون نومې سخته وچه مېوه تولیدوي'),
    ('custodian (n)', 'a person who takes responsibility for taking care of or protecting something', 'وہ شخص جو کسی چیز کی دیکھ بھال یا حفاظت کی ذمہ داری لیتا ہے', 'هغه څوک چې د یو شي د پاملرنې یا ساتنې مسؤلیت اخلي'),
    ('endemic (adj)', '(of a plant or animal) native and restricted to a certain place.', '(پودے یا جانور کے لیے) مقامی اور کسی خاص جگہ تک محدود۔', '(د بوټي یا ژوي لپاره) سیمه‌ییز او یوه ټاکلي ځای ته محدود.'),
    ('exponential (adj)', '(of a rate of increase) becoming faster and faster', '(اضافے کی شرح کے لیے) تیز سے تیز تر ہوتا ہوا', '(د زیاتوالي د کچې لپاره) ګړندی او ګړندی کېدونکی'),
    ('fabulous (adj)', 'extremely good', 'نہایت عمدہ', 'ډېر ښه'),
    ('flora and fauna (n)', 'the plants and animals of a particular area', 'کسی خاص علاقے کے پودے اور جانور', 'د یوې ځانګړې سیمې بوټي او ژوي'),
    ('kaleidoscope (n)', 'a toy consisting of a tube that you look through with loose pieces of coloured glass and mirrors at the end. when the tube is turned, the pieces of glass move and form different patterns', 'ایک کھلونا جو ایک نلکی پر مشتمل ہوتا ہے جس میں آپ جھانکتے ہیں اور اس کے سرے پر رنگین شیشے کے ڈھیلے ٹکڑے اور آئینے ہوتے ہیں۔ نلکی گھمانے پر شیشے کے ٹکڑے حرکت کر کے مختلف نقش بناتے ہیں', 'یوه لوبه چې له یو نل جوړه ده چې پکې ګورئ او په پای کې یې د رنګه ښیښې خلاصې ټوټې او هندارې دي. کله چې نل وګرځول شي، د ښیښې ټوټې خوځېږي او بېلابېل نقشونه جوړوي'),
    ('melting pot (n)', 'a place where different peoples, styles, theories, etc. are mixed together', 'ایسی جگہ جہاں مختلف لوگ، انداز، نظریات وغیرہ آپس میں گھل مل جائیں', 'هغه ځای چې پکې بېلابېل خلک، سټایلونه، نظریې او نور سره ګډ شي'),
    ('mesmerise (v)', 'to have such a strong effect on you that you cannot give your attention to anything else', 'آپ پر اتنا گہرا اثر کرنا کہ آپ کسی اور چیز پر توجہ نہ دے سکیں', 'په تاسو داسې قوي اغېز کول چې بل شي ته پاملرنه ونه شئ کړای'),
    ('meticulously (adv)', 'in a way that pays careful attention to every detail', 'ہر تفصیل پر پوری توجہ دیتے ہوئے', 'په داسې ډول چې هر جزئیات ته په دقت پاملرنه کوي'),
    ('mountaineers (n)', 'a person who climbs mountains as a sport', 'وہ شخص جو کھیل کے طور پر پہاڑوں پر چڑھتا ہے', 'هغه څوک چې د لوبې په توګه غرونو ته ختل کوي'),
    ('nirvava', 'the state of perfect happiness and peace', 'کامل خوشی اور سکون کی حالت', 'د بشپړې خوښۍ او سولې حالت'),
    ('picturesque (adj)', '(of a place, building, scene, etc.) pretty, especially in a way that looks old-fashioned', '(جگہ، عمارت، منظر وغیرہ کے لیے) خوبصورت، خاص طور پر پرانے انداز میں', '(د ځای، ودانۍ، منظرې او نورو لپاره) ښکلی، په ځانګړي ډول په زاړه سټایل'),
    ('renovate (v)', 'to repair and paint an old building, a piece of furniture, etc. so that it is in good condition again', 'کسی پرانی عمارت، فرنیچر وغیرہ کی مرمت اور رنگ و روغن کرنا تاکہ وہ پھر سے اچھی حالت میں آ جائے', 'یوه زړه ودانۍ، فرنیچر او نور ترمیم او رنګ کول ترڅو بیا ښه حالت ته راشي'),
    ('snow-clad (adj)', 'covered with snow', 'برف سے ڈھکا ہوا', 'په واورو پوښل شوی'),
    ('solace (n)', 'to make somebody feel better or happier when they are sad or disappointed', 'کسی کو دکھ یا مایوسی میں بہتر یا خوش محسوس کروانا', 'چا ته د خپګان یا نهیلۍ پر مهال ښه یا خوښ احساس ورکول'),
])
gl = BOOK.record(g, 'eng12-u16-glossary-a', 'Glossary (alluvial – solace)', 'فرہنگ (alluvial – solace)', 'وییپانګه (alluvial – solace)', 84, [156])
issues = [{'id': 'eng12-p155-156', 'unit': 16, 'printedPage': 155, 'description': 'Reference prints the magazine name as “Diplomate” (retained). Glossary retained as printed: “nirvava” (nirvana), “avifauna (adj)” (a noun), “mountaineers (n) — a person …”, and “solace (n)” defined with a verb phrase.'}]

if __name__ == '__main__':
    BOOK.save(84, [(16, rec), (16, gl)], issues=issues)
