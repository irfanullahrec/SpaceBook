"""PDF19 (printed 25–26): Unit 2 context clues 4–12 and Teacher's Guideline (unit end); Unit 3 opener 'Solitary Reaper' (Wordsworth) outcomes."""
from class12_book_common import Book, Builder

BOOK = Book('english')
w = Builder()
w.group('lines', [
    ('4. [first line cut off in the scan] …ness, is the cause of most of his trouble.', '4. [اسکین میں پہلی سطر کٹی ہوئی ہے] …، اس کی زیادہ تر پریشانیوں کی وجہ ہے۔', '4. [په سکین کې لومړۍ کرښه پرې شوې] …، د هغه د ډېرو ستونزو لامل دی.'),
    ('5. Rather than be involved in clandestine meetings, they did everything quite openly.', '5. خفیہ ملاقاتوں میں شامل ہونے کے بجائے انہوں نے سب کچھ بالکل کھلم کھلا کیا۔', '5. د پټو غونډو په ځای یې هر څه په بشپړ ډول په ښکاره وکړل.'),
    ('6. Ecclesiastics, such as priests, ministers, and pastors, should set models of behavior for their congregants.', '6. مذہبی پیشوا، جیسے پادری، منسٹر اور پاسٹر، اپنے پیروکاروں کے لیے طرزِ عمل کا نمونہ قائم کریں۔', '6. مذهبي مشران، لکه پادریان، منسټران او پاسټران، باید خپلو پیروانو ته د چلند بېلګې وړاندې کړي.'),
    ('7. The girl was churlish – rude, sullen and absolutely ill-mannered.', '7. لڑکی بدمزاج تھی — بدتمیز، ترش رو اور بالکل بد اخلاق۔', '7. نجلۍ بدخویه وه — بې‌ادبه، تریو تندي او بالکل بداخلاقه.'),
    ('8. Because the conflagration was aided by wind, it was so destructive that every building in the area was completely burned to the ground.', '8. چونکہ ہوا نے آتش زدگی کو بڑھا دیا تھا، یہ اتنی تباہ کن تھی کہ علاقے کی ہر عمارت مکمل طور پر جل کر خاک ہو گئی۔', '8. څرنګه چې باد د اور لګېدنې سره مرسته وکړه، دومره ورانوونکې وه چې په سیمه کې هره ودانۍ بشپړه وسوځېده او له ځمکې سره برابره شوه.'),
    ("9. My opponent's argument is fallacious, misleading – plain wrong.", '9. میرے مخالف کی دلیل مغالطہ آمیز ہے، گمراہ کن — صاف غلط۔', '9. زما د مخالف دلیل تېروتونکی دی، ګمراه کوونکی — بالکل ناسم.'),
    ('10. Although some men are loquacious, others hardly talk at all.', '10. اگرچہ کچھ مرد بہت باتونی ہوتے ہیں، دوسرے مشکل سے ہی بات کرتے ہیں۔', '10. که څه هم ځینې سړي ډېر خبرې‌کوونکي وي، نور په سختۍ سره خبرې کوي.'),
    ('11. The patient is so somnolent that she requires medication to help her stay awake for more than a short time.', '11. مریضہ اتنی غنودگی میں رہتی ہے کہ اسے تھوڑی دیر سے زیادہ جاگتے رہنے کے لیے دوا کی ضرورت ہوتی ہے۔', '11. ناروغه دومره خوبجنه ده چې د لنډ وخت څخه زیات د ویښ پاتې کېدو لپاره درملو ته اړتیا لري.'),
    ('12. Celestial bodies, such as the sun, moon, and stars, are governed by predictable laws.', '12. اجرامِ فلکی، جیسے سورج، چاند اور ستارے، قابلِ پیش گوئی قوانین کے تابع ہیں۔', '12. اسماني اجسام، لکه لمر، سپوږمۍ او ستوري، د وړاندوینې وړ قوانینو تابع دي.'),
])
w.h("Teacher's Guideline", 'استاد کے لیے رہنمائی', 'ښوونکي ته لارښوونه')
w.p('Explain to student different types of contextual clues and their application for deducing the meaning of unfamiliar words.', 'طالب علم کو سیاقی اشاروں کی مختلف اقسام اور نامانوس الفاظ کے معنی اخذ کرنے میں ان کے اطلاق کی وضاحت کریں۔', 'زده کوونکي ته د شرایطي نښو بېلابېل ډولونه او د ناپېژندل شویو کلمو د مانا په استنباط کې د هغو کارونه تشریح کړئ.')
ex = BOOK.record(w, 'eng12-u02-vocab-b', "Context clues 4–12; Teacher's Guideline", "سیاقی اشارے 4–12؛ استاد کے لیے رہنمائی", "شرایطي نښې 4–12؛ ښوونکي ته لارښوونه", 19, [25])

UT = ('Solitary Reaper (Poem)', 'تنہا فصل کاٹنے والی (نظم)', 'یوازینۍ لوګړه (شعر)')
o = Builder()
o.h('Unit 3 — Solitary Reaper (Wordsworth)', 'یونٹ 3 — تنہا فصل کاٹنے والی (ورڈزورتھ)', 'واحد 3 — یوازینۍ لوګړه (ورډزورت)')
o.p('By the end of the unit, the students will be able to:', 'اس یونٹ کے اختتام تک طلبہ اس قابل ہوں گے کہ:', 'د دې واحد په پای کې به زده کوونکي وکولای شي چې:')
o.group('list', [
    ('Read a given poem and give orally and in writing: theme and its development; personal response with justification; recognize literary techniques such as personification and alliteration.', 'دی گئی نظم پڑھیں اور زبانی و تحریری طور پر بیان کریں: موضوع اور اس کا ارتقا؛ جواز کے ساتھ ذاتی ردِعمل؛ ادبی تکنیکوں جیسے تجسیم اور صنعتِ تجنیسِ حرفی کو پہچانیں۔', 'ورکړل شوی شعر ولولي او په خوله او لیکلي ډول ووايي: موضوع او د هغې وده؛ د دلیل سره شخصي غبرګون؛ ادبي تخنیکونه لکه تجسیم او د تورو تکرار وپېژني.'),
    ('Analyze how a writer/ poet uses language to appeal to the senses through use of figurative language including similes, metaphors and imagery.', 'تجزیہ کریں کہ ایک مصنف/ شاعر تشبیہات، استعارات اور پیکر تراشی سمیت مجازی زبان کے ذریعے حواس کو متاثر کرنے کے لیے زبان کیسے استعمال کرتا ہے۔', 'تحلیل کړي چې یو لیکوال/ شاعر د تشبیهاتو، استعارو او انځورګرۍ په ګډون د مجازي ژبې له لارې حواسو ته د اپیل لپاره ژبه څنګه کاروي.'),
    ('Set tone. influence reader for various purposes e.g. propaganda, irony, parody and satire. Analyze their effect on communication.', 'لہجہ متعین کریں۔ مختلف مقاصد کے لیے قاری کو متاثر کریں، مثلاً پروپیگنڈا، طنز، پیروڈی اور ہجو۔ ابلاغ پر ان کے اثر کا تجزیہ کریں۔', 'لهجه وټاکي. د بېلابېلو موخو لپاره پر لوستونکي اغېز وکړي، لکه پروپاګنډ، طنز، پاروډي او هجو. پر اړیکه یې اغېز تحلیل کړي.'),
    ('Use pre-reading strategies to predict the content of a text from topic / picture, title / headings, key words and visuals etc. by using prior knowledge, asking questions and contextual clues.', 'سابقہ علم، سوالات اور سیاقی اشاروں کو استعمال کرتے ہوئے موضوع / تصویر، عنوان / سرخیوں، کلیدی الفاظ اور بصری مواد وغیرہ سے متن کے مواد کی پیش گوئی کے لیے مطالعے سے پہلے کی حکمتِ عملیاں استعمال کریں۔', 'د مخکینۍ پوهې، پوښتنو او شرایطي نښو په کارولو د موضوع / انځور، سرلیک / سرټکو، کلیدي کلمو او لیدنیزو موادو څخه د متن د منځپانګې د وړاندوینې لپاره د لوستلو مخکې ستراتیژۍ وکاروي.'),
    ('Skim text to: have general idea of the text; infer theme/ main idea.', 'متن پر سرسری نظر ڈالیں تاکہ: متن کا عمومی اندازہ ہو؛ موضوع/ مرکزی خیال اخذ کریں۔', 'په متن سرسري نظر واچوي ترڅو: د متن عمومي مفکوره ولري؛ موضوع/ اصلي مفکوره استنباط کړي.'),
    ('Apply critical thinking to interact with text, use intensive reading strategies (while-reading) to scan to answer short questions', 'متن سے تعامل کے لیے تنقیدی سوچ کا اطلاق کریں، گہرے مطالعے کی حکمتِ عملیاں (دورانِ مطالعہ) استعمال کریں تاکہ مختصر سوالات کے جواب کے لیے متن میں تلاش کریں', 'له متن سره د تعامل لپاره انتقادي فکر پلي کړي، د ژورو لوستلو ستراتیژۍ (د لوستلو پر مهال) وکاروي ترڅو د لنډو پوښتنو د ځوابولو لپاره متن ولټوي'),
    ('Write an introductory paragraph with a clear central thought.', 'واضح مرکزی خیال کے ساتھ ایک تعارفی پیراگراف لکھیں۔', 'د روښانه مرکزي فکر سره یو پیلنی پراګراف ولیکي.'),
    ('Use pronunciation key to pronounce words with developing accuracy.', 'بڑھتی ہوئی درستی کے ساتھ الفاظ ادا کرنے کے لیے تلفظ کی کلید استعمال کریں۔', 'د زیاتېدونکي دقت سره د کلمو د تلفظ لپاره د تلفظ کیلي وکاروي.'),
    ('Deduce the meaning of unfamiliar words from the context using contextual clues.', 'سیاقی اشاروں کو استعمال کرتے ہوئے سیاق و سباق سے نامانوس الفاظ کے معنی اخذ کریں۔', 'د شرایطي نښو په کارولو له شرایطو څخه د ناپېژندل شویو کلمو مانا استنباط کړي.'),
])
op = BOOK.record(o, 'eng12-u03-outcomes', 'Unit 3 — learning outcomes', 'یونٹ 3 — تعلیمی نتائج', 'واحد 3 — د زده کړې پایلې', 19, [26], unit_title=UT)
issues = [{'id': 'eng12-p25-cut', 'unit': 2, 'printedPage': 25, 'description': 'The top of printed page 25 is cut off in every available copy (PDF, JPG): context-clue item 4 survives only as “…ness, is the cause of most of his trouble.” and item 5 is partly clipped (“…ather than be involved…”, reconstructed as “Rather”). Teacher’s guideline prints “Explain to student”. Needs a clean print to restore item 4.'}]

if __name__ == '__main__':
    BOOK.save(19, [(2, ex), (3, op)], issues=issues, complete_units=[2])
