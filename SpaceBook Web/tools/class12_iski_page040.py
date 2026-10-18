"""Islamiat (Ikhtiari) XII PDF40: pp.70–71 — Sirah exercise; F. selected verses Al-Baqarah 267. Run: python class12_iski_page040.py"""
from class12_iski_common import BOOK, Builder, rec, P, L, AR


def p40():
    b = Builder()
    b.h('Exercise', 'مشق', 'تمرین')
    b.p('Question 1: Write detailed answers to the following questions.', 'سوال 1: درج ذیل سوالوں کے مفصل جواب لکھیں۔', 'پوښتنه ۱: د لاندې پوښتنو مفصل ځوابونه ولیکئ.')
    L(b, [('i. What was the condition of the society into which the Noble Prophet ﷺ came?', 'i۔ نبی اکرم صلی اللہ علیہ وآلہٖ وسلم جس معاشرے میں تشریف لائے اسکی کیا حالت تھی؟', 'i. نبي اکرم ﷺ چې کومې ټولنې ته راغی، د هغې حالت څه و؟'),
          ('ii. What did he ﷺ say on the occasion of the Farewell Sermon?', 'ii۔ خطبہ حجۃ الوداع کے موقع پر آپ صلی اللہ علیہ وآلہٖ وسلم نے کیا ارشاد فرمایا؟', 'ii. د حجة الوداع د خطبې پر مهال هغه ﷺ څه وفرمایل؟'),
          ('iii. What are the Islamic teachings regarding freedom of thought and opinion?', 'iii۔ آزادیٔ فکر و رائے کے بارے میں اسلامی تعلیمات کیا ہیں؟', 'iii. د فکر او نظر د ازادۍ په اړه اسلامي لارښوونې څه دي؟'),
          ('iv. State the guiding principles of the first Muslim society.', 'iv۔ اولین مسلم معاشرے کے رہنما اصول بیان کریں۔', 'iv. د لومړنۍ مسلمانې ټولنې لارښود اصول بیان کړئ.'),
          ('v. Write a note on the belief in the finality of prophethood.', 'v۔ عقیدہ ختم نبوت پر نوٹ تحریر کریں۔', 'v. د ختم نبوت پر عقیده یادښت ولیکئ.')])
    b.p('Question 2: Fill in the blanks with suitable words according to the lesson.', 'سوال 2: سبق کے مطابق مناسب الفاظ لگا کر خالی جگہ پر کریں۔', 'پوښتنه ۲: د لوست سره سم په مناسبو ټکو تشې ځایونه ډک کړئ.')
    L(b, [('i. For the guidance of people, ______ were sent in every era.', 'i۔ لوگوں کی ہدایت کے لیے ہر دور میں ______ مبعوث کیے گئے۔', 'i. د خلکو د هدایت لپاره په هره دوره کې ______ مبعوث شول.'),
          ('ii. The best creation of Allah the Exalted is ______.', 'ii۔ اللہ تعالیٰ کی بہترین مخلوق ______ ہے۔', 'ii. د الله تعالی غوره مخلوق ______ دی.'),
          ('iii. Before Islam some people used to perform the tawaf of the Kaaba ______.', 'iii۔ اسلام سے قبل بعض لوگ ______ ہو کر کعبے کا طواف کرتے تھے۔', 'iii. له اسلام مخکې ځینو خلکو به ______ د کعبې طواف کاوه.'),
          ('iv. While giving the invitation to tawhid, the Noble Prophet ﷺ took the testimony of his ______.', 'iv۔ توحید کی دعوت دیتے وقت نبی اکرم صلی اللہ علیہ وآلہٖ وسلم نے اپنی ______ کی گواہی لی۔', 'iv. د توحید د بلنې پر مهال نبي اکرم ﷺ د خپل ______ شاهدي واخیسته.'),
          ('v. The Farewell Sermon is the best charter of ______ rights.', 'v۔ خطبہ حجۃ الوداع ______ حقوق کا بہترین منشور ہے۔', 'v. د حجة الوداع خطبه د ______ حقونو غوره منشور دی.'),
          ('vi. In the matter of religion there is no ______ of any kind.', 'vi۔ دین کے معاملے میں کسی قسم کا ______ نہیں ہوتا۔', 'vi. د دین په چاره کې هېڅ ډول ______ نشته.'),
          ('vii. For others one should like what one likes for ______.', 'vii۔ دوسروں کے لیے وہ پسند کرنا چاہیے جو ______ لیے پسند ہو۔', 'vii. د نورو لپاره باید هغه خوښ کړو چې د ______ لپاره خوښ وي.'),
          ('viii. To leave a Muslim brother without help or support is ______.', 'viii۔ مسلمان بھائی کو بے یار و مددگار چھوڑنا ______ ہے۔', 'viii. مسلمان ورور بې‌ملاتړه پرېښودل ______ دي.'),
          ('ix. The foundation of the Islamic social system is on ______.', 'ix۔ اسلامی معاشرتی نظام کی بنیاد ______ پر ہے۔', 'ix. د اسلامي ټولنیز نظام بنسټ پر ______ دی.'),
          ('x. Taqwa is the spirit of all ______.', 'x۔ تقویٰ تمام ______ کی روح ہے۔', 'x. تقوا د ټولو ______ روح ده.')])
    b.p('Question 3: Write short answers to the following questions.', 'سوال 3: درج ذیل سوالوں کے مختصر جوابات لکھیں۔', 'پوښتنه ۳: د لاندې پوښتنو لنډ ځوابونه ولیکئ.')
    L(b, [('i. Give a short definition of justice.', 'i۔ عدل کی مختصر تعریف کریں۔', 'i. د عدل لنډه تعریف وکړئ.'),
          ('ii. Why is faith in the belief of messengership necessary for understanding the belief of tawhid?', 'ii۔ عقیدہ توحید کو سمجھنے کے لیے عقیدہ رسالت پر ایمان لانا کیوں ضروری ہے۔', 'ii. د توحید د عقیدې د پوهېدو لپاره د رسالت پر عقیده ایمان ولې ضروري دی؟'),
          ('iii. Who is a God-fearing (muttaqi) person?', 'iii۔ متقی انسان کون ہے؟', 'iii. متقي انسان څوک دی؟')])
    r1 = rec(b, 1, 70, 40, [70], kind='exercise')
    t = Builder()
    t.h('F. Selected verses of the Quran', 'و۔ منتخب آیاتِ قرآن', 'و. د قرآن غوره آیتونه')
    t.h('Surah al-Baqarah, verses 267 to 286', 'سورۃ البقرہ آیت نمبر 267 تا 286', 'سورة البقره، ۲۶۷ تر ۲۸۶ آیتونه')
    t.p('Verse no. 267', 'آیت نمبر: 267', 'آیت نمبر: ۲۶۷')
    AR(t, 'يٰٓاَيُّهَا الَّذِيْنَ اٰمَنُوْٓا اَنْفِقُوْا مِنْ طَيِّبٰتِ مَا كَسَبْتُمْ وَمِمَّآ اَخْرَجْنَا لَكُمْ مِّنَ الْاَرْضِ ۠ وَلَا تَيَمَّمُوا الْخَبِيْثَ مِنْهُ تُنْفِقُوْنَ وَلَسْتُمْ بِاٰخِذِيْهِ اِلَّآ اَنْ تُغْمِضُوْا فِيْهِ ؕ وَاعْلَمُوْٓا اَنَّ اللّٰهَ غَنِيٌّ حَمِيْدٌ')
    P(t, [('Translation: Believers! Of the pure and good wealth that you earn, and of the things that We bring out of the earth for you, spend in the way of Allah too. And do not intend to give bad and impure things, which, if they were given to you, you would never take except by closing your eyes while taking them. And know that Allah is Self-sufficient, Possessor of all praiseworthy qualities.', 'ترجمہ: مومنو! جو پاکیزہ اور عمدہ مال تم کماتے ہو اور جو چیزیں ہم تمہارے لئے زمین سے نکالتے ہیں ان میں سے اللہ کی راہ میں بھی خرچ کرو۔ اور بری اور ناپاک چیزیں دینے کا قصد نہ کرنا کہ اگر وہ چیزیں تمہیں دی جائیں تو بجز اس کے کہ لیتے وقت آنکھیں بند کر لو ان کو کبھی نہ لو۔ اور جان رکھو کہ اللہ بے نیاز ہے خوبیوں والا ہے۔', 'ژباړه: مؤمنانو! له هغه پاک او غوره مال چې تاسو یې ګټئ، او له هغو شیانو چې موږ یې ستاسو لپاره له ځمکې راباسو، د الله په لاره کې هم ولګوئ. او د بدو او ناپاکو شیانو د ورکولو اراده مه کوئ، چې که هغه تاسو ته درکړل شي، نو هېڅکله به یې وانخلئ مګر دا چې د اخیستو پر مهال سترګې پټې کړئ. او پوه شئ چې الله بې‌نیازه، د ښېګڼو خاوند دی.')])
    t.h('Commentary', 'تفسیر', 'تفسیر')
    P(t, [('In this noble verse the command has been given to spend excellent and pure things in the way of Allah the Exalted. Giving defective and disliked things in the way of Allah the Exalted has also been forbidden.', 'اس آیتِ کریمہ میں اللہ تعالیٰ کی راہ میں عمدہ اور پاک چیزیں خرچ کرنے کا حکم دیا گیا ہے۔ ناقص اور ناپسندیدہ چیزیں اللہ تعالیٰ کی راہ میں دینے کی ممانعت بھی کی گئی ہے۔', 'په دې کریمه آیت کې د الله تعالی په لاره کې د غوره او پاکو شیانو د لګولو حکم شوی. د الله تعالی په لاره کې د نیمګړو او ناخوښو شیانو ورکول هم منع شوي.'),
          ('Allah the Exalted has stressed that the true believers are those who spend the best things in His way. Whatever wealth a person earns, he in fact earns it by virtue of the abilities and powers given by Allah the Exalted. In the same way, whatever the earth produces is only by virtue of the perfect power of Allah the Exalted, because without His will and intention not even a single leaf can move. Therefore believers are being urged that before spending in the way of God they should see well that the wealth is excellent …', 'اللہ تعالیٰ نے تاکید فرمائی ہے کہ اصل مومن وہ ہیں جو اس کی راہ میں بہترین چیزیں خرچ کرتے ہیں۔ انسان جو مال بھی کماتا ہے وہ دراصل اللہ تعالیٰ کی دی ہوئی قابلیتوں اور طاقتوں کے بل بوتے پر ہی کماتا ہے۔ اسی طرح زمین جو کچھ بھی پیدا کرتی ہے وہ محض اللہ تعالیٰ کی قدرتِ کاملہ ہی کی بدولت ہوتا ہے۔ اس لیے کہ اس کی مرضی اور منشا کے بغیر تو ایک پتا بھی نہیں ہل سکتا۔ لہٰذا مومنوں کو تلقین کی جا رہی ہے کہ راہِ خدا میں خرچ کرنے سے پہلے اچھی طرح دیکھ لو کہ مال عمدہ ہو', 'الله تعالی ټینګار کړی چې اصلي مؤمنان هغه دي چې د هغه په لاره کې غوره شیان لګوي. انسان هر مال چې ګټي، په اصل کې یې د الله تعالی د ورکړو وړتیاوو او ځواکونو په زور ګټي. همداسې ځمکه چې هر څه زېږوي، یوازې د الله تعالی د بشپړې قدرت له برکته وي، ځکه د هغه له خوښې او ارادې پرته یوه پاڼه هم نشي خوځېدای. نو مؤمنانو ته سپارښتنه کېږي چې د خدای په لاره کې له لګولو مخکې ښه وګورئ چې مال غوره وي …')])
    BOOK.save(40, [(1, r1), (1, rec(t, 1, 71, 40, [71]))], issues=[{'id': 'iski12-pdf040', 'unit': 1, 'printedPage': 70,
               'description': 'p.70: blanks of Q2 filled in by a student in handwriting, and page numbers written beside questions — all excluded; blanks rendered empty. p.71: student marks beside the commentary excluded.'}])


if __name__ == '__main__':
    p40()
