"""Urdu XII PDF100 (spread): printed pp.190–191 — Poem 1 'جوابِ شکوہ' (Iqbal) stanzas 4–11 (end; source بانگِ درا)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
t = Builder()
S = [
 [('So insolent that he is angry even with Allah —', 'اس قدر شوخ کہ اللہ سے بھی برہم ہے', 'دومره شوخ چې له الله سره هم خپه دی —'),
  ('is this the same Adam to whom the angels bowed?', 'تھا جو مسجودِ ملائک یہ وہی آدم ہے؟', 'ایا دا هماغه آدم دی چې پرښتو ورته سجده کړې وه؟'),
  ('He is a knower of the world of states and a sage of the secrets of how much;', 'عالمِ کیف ہے، دانائے رموزِ کم ہے', 'د کیفیت عالِم دی، د کمیت د رازونو پوه دی؛'),
  ('yes, but he is a stranger to the secrets of humility.', 'ہاں، مگر عجز کے اسرار سے نا محرم ہے', 'هو، خو د عاجزۍ له رازونو ناخبره دی.'),
  ('Men are proud of their power of speech,', 'ناز ہے طاقتِ گفتار پہ انسانوں کو', 'انسانان د خبرو پر ځواک ویاړي،'),
  ('yet the ignorant have no manners in speaking.', 'بات کرنے کا سلیقہ نہیں نادانوں کو', 'خو ناپوهانو ته د خبرو سلیقه نشته.')],
 [('A voice came: “Your tale is moving; your cup brims with restless tears.', 'آئی آواز غم انگیز ہے افسانہ ترا ۔ اشکِ بیتاب سے لبریز ہے پیمانہ ترا', 'یو غږ راغی: "ستا کیسه غمجنه ده؛ ستا پیاله له بې‌قرارو اوښکو ډکه ده.'),
  ('Your ecstatic cry has gripped the sky; how bold-tongued is your mad heart!', 'آسماں گیر ہوا نعرۂ مستانہ ترا ۔ کس قدر شوخ زباں ہے دلِ دیوانہ ترا', 'ستا مستانه نعرې اسمان ونیو؛ ستا لېونی زړه څومره شوخ‌ژبی دی!'),
  ('With what grace of manner you turned complaint into thanks;', 'شکر شکوے کو کیا حسنِ ادا سے تو نے', 'تا په څومره ښکلي انداز شکوه په شکر بدله کړه؛'),
  ('you made servants converse with God!', 'ہم سخن کر دیا بندوں کو خدا سے تو نے', 'تا بندګان له خدای سره هم‌خبرې کړل!"')],
 [('We are inclined to generosity, but there is no one who asks; to whom shall We show the way? There is no traveller to the destination.', 'ہم تو مائل بہ کرم ہیں، کوئی سائل ہی نہیں ۔ راہ دکھلائیں کسے؟ رہروِ منزل ہی نہیں', '"موږ خو کرم ته مایل یو، خو سوالګر نشته؛ چا ته لار وښیو؟ د منزل لاروی نشته.'),
  ('Our nurture is for all, but there is no worthy essence; this is not the clay from which Adam is built.', 'تربیت عام تو ہے، جوہرِ قابل ہی نہیں ۔ جس سے تعمیر ہو آدم کی یہ وہ گِل ہی نہیں', 'روزنه خو عامه ده، خو وړ جوهر نشته؛ دا هغه خټه نه ده چې آدم ترې جوړ شي.'),
  ('If anyone were worthy, We would grant him the glory of Kai (Kayānī kings);', 'کوئی قابل ہو تو ہم شانِ کئی دیتے ہیں', 'که څوک وړ وي، موږ ورته د کیاني پاچاهانو شان ورکوو؛'),
  ('to those who seek, We give even a new world.', 'ڈھونڈنے والوں کو دنیا بھی نئی دیتے ہیں', 'لټوونکو ته نوې نړۍ هم ورکوو.')],
 [('Your hands are powerless, your hearts accustomed to unbelief; you are an Ummah that brings disgrace to the Prophet.', 'ہاتھ بے زور ہیں، الحاد سے دل خوگر ہیں ۔ اُمتی باعثِ رسوائیِ پیغمبرؐ ہیں', 'لاسونه مو بې‌زوره دي، زړونه مو له الحاد سره روږدي؛ امتیان د پیغمبر ﷺ د رسوايۍ لامل دي.'),
  ('The idol-breakers have departed; those who remain are idol-makers — the father was Abraham, the sons are Āzar.', 'بت شکن اٹھ گئے، باقی جو رہے بت گر ہیں ۔ تھا براہیمؑ پدر اور پسر آزر ہیں', 'بت‌ماتوونکي لاړل، څوک چې پاتې دي بت‌جوړوونکي دي؛ پلار ابراهیم و او زامن آزر دي.'),
  ('New are the drinkers, new the wine, new even the jars;', 'بادہ آشام نئے، بادہ نیا، خُم بھی نئے', 'څښونکي نوي، شراب نوي، منګي هم نوي؛'),
  ('the sanctuary of the Kaaba is new, the idols new, and you are new too.', 'حرمِ کعبہ نیا، بت بھی نئے، تم بھی نئے', 'د کعبې حرم نوی، بتان هم نوي، تاسو هم نوي.')],
 [('Who erased falsehood from the page of time? Who freed mankind from slavery?', 'صفحۂ دہر سے باطل کو مٹایا کس نے؟ ۔ نوعِ انساں کو غلامی سے چھڑایا کس نے؟', 'د زمانې له پاڼې باطل چا ورک کړ؟ انسانیت چا له غلامۍ خلاص کړ؟'),
  ('Who peopled My Kaaba with foreheads (in prostration)? Who held My Qur’an to the breast?', 'میرے کعبے کو جبینوں سے بسایا کس نے؟ ۔ میرے قرآن کو سینے سے لگایا کس نے؟', 'زما کعبه چا په تندیو (سجدو) اباده کړه؟ زما قرآن چا سینې ته ونیو؟'),
  ('They were indeed your forefathers — but what are you?', 'تھے تو آبا وہ تمھارے ہی، مگر تم کیا ہو؟', 'هغوی خو ستاسو نیکونه وو، خو تاسو څه یاست؟'),
  ('Sitting idle, hand on hand, waiting for tomorrow!', 'ہاتھ پر ہاتھ دھرے منتظرِ فردا ہو!', 'لاس پر لاس ایښي، د سبا انتظار باسئ!')],
 [('What did you say? For the Muslim there is only the promise of houris! Even if one complains unjustly, sense is required!', 'کیا کہا؟ بہرِ مسلماں ہے فقط وعدۂ حور ۔ شکوہ بے جا بھی کرے کوئی تو لازم ہے شعور!', 'څه دې وویل؟ د مسلمان لپاره یوازې د حورو ژمنه ده؟ که څوک بې‌ځایه ګیله هم کوي، پوهه یې لازمه ده!'),
  ('Justice is the Creator’s law from eternity: if the unbeliever adopted the Muslim’s ways, he would receive houris and palaces.', 'عدل ہے فاطرِ ہستی کا ازل سے دستور ۔ مسلم آئیں ہوا کافر تو ملے حور و قصور', 'عدل له ازله د خالق دستور دی؛ که کافر د مسلمان دود غوره کړ، هغه ته به حورې او ماڼۍ ورکړل شي.'),
  ('Among you there is no one who even desires the houris;', 'تم میں حوروں کا کوئی چاہنے والا ہی نہیں', 'په تاسو کې د حورو غوښتونکی هم نشته؛'),
  ('the radiance of Sinai is present, but there is no Moses.', 'جلوۂ طور تو موجود ہے موسیٰ ہی نہیں', 'د طور جلوه خو شته، خو موسیٰ نشته.')],
 [('You will not be wiped out by the wiping out of Iran; the intoxication of wine has no tie to the cup.', 'تو نہ مٹ جائے گا ایران کے مٹ جانے سے ۔ نشۂ مے کو تعلق نہیں پیمانے سے', 'ته به د ایران په ورکېدو نه ورکېږې؛ د شرابو نشه له پیالې سره تړاو نه لري.'),
  ('It is evident from the tale of the Tatar onslaught: the Kaaba found guardians from the idol-house.', 'ہے عیاں یورشِ تاتار کے افسانے سے ۔ پاسباں مل گئے کعبے کو صنم خانے سے', 'د تاتارو د یرغل له کیسې ښکاره ده: کعبې ته له بتخانې ساتونکي ورپیدا شول.'),
  ('You are indeed the support of the ship of Truth in the world;', 'کشتیٔ حق کا زمانے میں سہارا تو ہے', 'په نړۍ کې د حق د کښتۍ ملاتړ ته یې؛'),
  ('the new age is night — a dim star, still, you are.', 'عصرِ نو رات ہے، دھندلا سا ستارا تو ہے', 'نوی عصر شپه ده — یو تت ستوری، خو ته یې.')],
 [('Like fragrance you are imprisoned in the bud — scatter yourself; load your baggage on the shoulders of the garden breeze.', 'مثلِ بو قید ہے غنچے میں، پریشاں ہو جا ۔ رختِ بر دوشِ ہوائے چمنستاں ہو جا', 'د خوشبو په څېر په غوټۍ کې بند یې، خپور شه؛ د باغ د باد پر اوږو خپل سامان بار کړه.'),
  ('You are of little substance — from a speck become a desert; from the song of a wave become the tumult of a storm.', 'ہے تنک مایہ، تو ذرّے سے بیاباں ہو جا ۔ نغمۂ موج سے ہنگامۂ طوفاں ہو جا', 'کم‌پانګې یې، له ذرې دښته شه؛ د څپې له سندرې د طوفان هنګامه شه.'),
  ('With the power of love raise up everything low;', 'قوتِ عشق سے ہر پست کو بالا کر دے', 'د مینې په ځواک هر ټیټ لوړ کړه؛'),
  ('fill the world with light by the name of Muhammad.', 'دہر میں اسمِ محمدؐ سے اجالا کر دے', 'په نړۍ کې د محمد ﷺ په نوم رڼا خوره کړه.')],
 [('Everyone is drunk on the wine of the love of bodily ease; are you Muslims? Is this the way of being Muslim?', 'ہر کوئی مستِ مئے ذوقِ تن آسانی ہے ۔ تم مسلماں ہو؟ یہ اندازِ مسلمانی ہے؟', 'هر څوک د ارام‌غوښتنې په شرابو مست دی؛ تاسو مسلمانان یاست؟ ایا دا د مسلمانۍ انداز دی؟'),
  ('Neither the poverty of Ḥaidar (ʿAlī) nor the wealth of ʿUthmān — what spiritual link do you have with your forebears?', 'حیدریؓ فقر ہے، نے دولتِ عثمانیؓ ہے ۔ تم کو اسلاف سے کیا نسبتِ روحانی ہے', 'نه حیدري (علي) فقر شته، نه عثماني دولت؛ له خپلو مخکېنیو سره مو کومه روحاني اړیکه ده؟'),
  ('They were honoured in their age by being Muslims,', 'وہ زمانے میں معزز تھے مسلماں ہو کر', 'هغوی په زمانه کې د مسلمان په توګه معزز وو،'),
  ('and you have been disgraced by abandoning the Qur’an.', 'اور تم خوار ہوئے تارکِ قرآں ہو کر', 'او تاسو د قرآن په پرېښودو خوار شوئ.')],
 [('Reason is your shield, love your sword; my dervish! your vicegerency is world-conquering.', 'عقل ہے تیری سپر، عشق ہے شمشیر تری ۔ مرے درویش! خلافت ہے جہانگیر تری', 'عقل ستا ډال دی، مینه ستا توره؛ زما درویشه! ستا خلافت نړۍ‌نیوونکی دی.'),
  ('Your takbīr is fire for all besides Allah; if you are a Muslim, your striving is destiny.', 'ماسوای اللہ کے لیے آگ ہے تکبیر تری ۔ تو مسلماں ہو تو تقدیر ہے تدبیر تری', 'ستا تکبیر له الله پرته هر څه ته اور دی؛ که ته مسلمان یې، ستا تدبیر تقدیر دی.'),
  ('If you are faithful to Muhammad, We are yours;', 'کی محمدؐ سے وفا تو نے تو ہم تیرے ہیں', 'که تا له محمد ﷺ سره وفا وکړه، موږ ستا یو؛'),
  ('what is this world? The Tablet and the Pen are yours.', 'یہ جہاں چیز ہے کیا لوح و قلم تیرے ہیں', 'دا نړۍ څه شی ده؟ لوح او قلم ستا دي."')],
]
for i, st in enumerate(S, 4):
    t.p(f'Stanza {i}', f'بند {"".join("۰۱۲۳۴۵۶۷۸۹"[int(c)] for c in str(i))}', f'بند {i}')
    t.group('lines', st)
t.p('(Bang-e-Dara)', '(بانگِ درا)', '(بانګ درا)')
po = BOOK.record(t, 'urdu12-u18-poem-2', 'Poem text (2): stanzas 4–13', 'متنِ نظم (۲): بند ۴–۱۳', 'د نظم متن (۲): بندونه ۴–۱۳', 100, [190, 191])
po['sourceNote'] = 'In the printed layout the first couplet of each six-line stanza is set as two half-lines side by side; here each pair of half-lines from stanza 5 onward is joined with “ ۔ ” on one line, with the closing couplet as two lines.'
issues = [{'id': 'urdu12-pdf100', 'unit': 18, 'printedPage': 190, 'description': 'The textbook prints a 13-stanza selection from Jawab-e-Shikwa (pp.189–191), not the full 36-stanza poem; transcribed as printed. p.190 prints “شانِ کئی” (Kayānī glory) as in Bang-e-Dara.'}]

if __name__ == '__main__':
    BOOK.save(100, [(18, po)], issues=issues)
