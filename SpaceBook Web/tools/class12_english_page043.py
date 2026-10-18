"""PDF43 (printed 73–74): Unit 7 Vocabulary A weather-idiom matching table; B stressed-syllable activity; C prefixes table + words (start)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
w = Builder()
w.h('Vocabulary and Grammar', 'ذخیرۂ الفاظ اور قواعد', 'لغات او ګرامر')
w.p('A. Find the meanings of the following idioms related to weather in proper reference source and then match them to their exact meanings as given in column B.', 'A. موسم سے متعلق درج ذیل محاوروں کے معنی کسی مناسب حوالہ جاتی ذریعے میں تلاش کریں اور پھر انہیں کالم B میں دیے گئے ان کے درست معنی سے ملائیں۔', 'A. د هوا اړوند د لاندې محاورو ماناوې په یوه مناسبه مرجع سرچینه کې ومومئ او بیا یې د B ستون له دقیقو ماناوو سره برابرې کړئ.')
A = ['To brighten up', 'To take a shine to', 'To make hay when the sun shines', 'Come rain or shine', 'To chase rainbows', 'To save for a rainy day', 'To wait for a raindrop in the drought', 'Right as rain',
     'To take a rain check', 'Into each life some rain must fall', "To rain on someone's parade", 'It never rains but it pours', 'Raining cats and dogs', 'Dry Spell', 'Windfall', 'To shoot the breeze',
     'To get wind of something', 'To know which way the wind blows', 'To sail close to the wind', 'To throw caution to the wind', 'Cloud/storm on the horizon', 'Every dark cloud has a silver lining',
     'Cloud nine', 'To have your head in the clouds', '"I don\'t have the foggiest"']
B = [('"I don\'t have a clue" / "I have no idea', '’’مجھے کوئی اندازہ نہیں‘‘ / ’’مجھے کچھ معلوم نہیں', '"زه هېڅ نه پوهېږم" / "هېڅ نظر نه لرم'),
     ('a large amount of money which is won or unexpectedly received', 'بڑی رقم جو جیتی جائے یا اچانک مل جائے', 'لویه اندازه پیسې چې وګټل شي یا ناڅاپه ترلاسه شي'),
     ('a period in which someone is having less success than usual', 'وہ دور جس میں کسی کو معمول سے کم کامیابی مل رہی ہو', 'هغه دوره چې پکې یو څوک تر معمول لږه بریا لري'),
     ('a state of great happiness', 'بہت زیادہ خوشی کی حالت', 'د ډېرې خوښۍ حالت'), ('approaching problem', 'قریب آتا ہوا مسئلہ', 'نږدې کېدونکې ستونزه'),
     ('every difficult situation has a more comforting and hopeful aspect', 'ہر مشکل صورتِ حال کا ایک زیادہ تسلی بخش اور امید افزا پہلو ہوتا ہے', 'هر سخت حالت یو ډېر ډاډمن او هیله‌ناک اړخ لري'),
     ('everyone must experience difficulties or ill fortune at one time or another', 'ہر کسی کو کبھی نہ کبھی مشکلات یا بدقسمتی کا سامنا کرنا پڑتا ہے', 'هر څوک باید یو وخت یا بل وخت ستونزې یا بدمرغي تجربه کړي'),
     ('fit and healthy', 'تندرست اور صحت مند', 'روغ او سالم'), ('misfortunes seem to either all come in quick succession or all come at once', 'مصیبتیں یا تو یکے بعد دیگرے جلدی آتی ہیں یا سب ایک ساتھ', 'بدمرغۍ یا په چټکۍ یو پسې بل راځي یا ټولې یوځای'),
     ('to become more cheerful', 'زیادہ خوش ہو جانا', 'ډېر خوشاله کېدل'), ('to develop a liking for', 'کسی کو پسند کرنے لگنا', 'خوښول پیل کول'), ('to have a casual conversation', 'غیر رسمی گفتگو کرنا', 'غیررسمي خبرې کول'),
     ('to have unrealistic, impractical, or fanciful ideas', 'غیر حقیقی، ناقابلِ عمل یا خیالی تصورات رکھنا', 'غیرواقعي، ناعملي یا خیالي نظرونه لرل'), ('to hear a rumour about something', 'کسی چیز کے بارے میں افواہ سننا', 'د یو شي په اړه اوازه اورېدل'),
     ('to make the most of an opportunity while it lasts', 'موقع ہونے تک اس سے بھرپور فائدہ اٹھانا', 'تر هغه چې فرصت شته، ترې بشپړه ګټه پورته کول'), ('to pursue something that is impossible/impractical', 'کسی ناممکن/ناقابلِ عمل چیز کے پیچھے بھاگنا', 'د یو ناشوني/ناعملي شي پسې تلل'),
     ('to put something aside for a future time in which it may be needed', 'کسی چیز کو مستقبل کے اس وقت کے لیے بچا رکھنا جب اس کی ضرورت ہو', 'یو شی د راتلونکي هغه وخت لپاره ساتل چې ورته اړتیا وي'),
     ('to refuse an offer, while demonstrating enthusiasm to accept it in the future', 'کسی پیشکش کو ٹھکرانا لیکن مستقبل میں اسے قبول کرنے کا شوق ظاہر کرنا', 'یو وړاندیز ردول، خو په راتلونکي کې یې د منلو لېوالتیا ښودل'),
     ("to spoil someone's plans/to prevent someone from enjoying themselves", 'کسی کے منصوبے خراب کرنا/کسی کو لطف اندوز ہونے سے روکنا', 'د یو چا پلانونه خرابول/یو څوک له خوند اخیستو منع کول'),
     ('to take a great risk/to behave recklessly', 'بڑا خطرہ مول لینا/لاپرواہی سے برتاؤ کرنا', 'لوی خطر منل/بې‌پروا چلند کول'),
     ('to understand what is happening in changing circumstances and be able to anticipate what will happen in the future', 'بدلتے حالات میں جو ہو رہا ہے اسے سمجھنا اور مستقبل میں ہونے والی بات کا اندازہ لگانے کے قابل ہونا', 'په بدلېدونکو حالاتو کې د پېښېدونکو پوهېدل او د راتلونکو پېښو د اټکل وړتیا'),
     ('to verge on the limit of what is acceptable, allowed, or honourable', 'قابلِ قبول، جائز یا باعزت کی حد کے قریب پہنچ جانا', 'د منلو وړ، اجازه لرونکي یا باعزته حد ته نږدې کېدل'),
     ('to wait/hope for something which has little chance of happening', 'کسی ایسی چیز کا انتظار/امید کرنا جس کے ہونے کا امکان کم ہو', 'د داسې شي انتظار/هیله کول چې د پېښېدو چانس یې لږ وي'),
     ('whatever the weather/situation', 'موسم/حالات جو بھی ہوں', 'هوا/حالت هر څه چې وي'), ('raining heavily', 'موسلا دھار بارش ہونا', 'سخت باران ورېدل')]
EN = [[a, b[0]] for a, b in zip(A, B)]
UR = [[a, b[1]] for a, b in zip(A, B)]
PS = [[a, b[2]] for a, b in zip(A, B)]
w.table('eng12-u07-idioms', ['Column A', 'Column B'], EN, ['کالم A', 'کالم B'], ['ستون A', 'ستون B'], UR, PS)
w.h('Activity', 'سرگرمی', 'فعالیت')
w.p("B. The syllable of the words written in capital letters is 'stressed'while that with small letters is 'unstressed'. Practically pronounce thes e words with stressed and unstressed syllable. Also verify them by consulting an authentic dictionary of pronunciation.",
    'B. الفاظ کا جو ہجا بڑے حروف میں لکھا ہے وہ ’’زور دار‘‘ ہے جبکہ چھوٹے حروف والا ’’بے زور‘‘ ہے۔ ان الفاظ کو زور دار اور بے زور ہجوں کے ساتھ عملاً ادا کریں۔ تلفظ کی کسی مستند لغت سے بھی ان کی تصدیق کریں۔',
    'B. د کلمو هغه سیلاب چې په لویو تورو لیکل شوی "فشار لرونکی" دی او په کوچنیو تورو "بې‌فشاره" دی. دا کلمې د فشار لرونکو او بې‌فشاره سیلابونو سره عملاً تلفظ کړئ. د تلفظ د یوه معتبر قاموس په مراجعه یې هم تایید کړئ.')
WL = 'SAMples, CARton, PURple, RAIny, CHIna, HAPpy, reLAX, reCEIVE, diRECT, aMONG, aSIDE, beTWEEN, deCIDE, PREsent (adjective), preSENT(verb), OBject (noun), obJECT (verb), ORderly, SIlently, LOvingly, MAnager, GARdener, EAsier, RARity, OPtimal, GRAdient, GEnorous, ADDable, DURable, LAUGHable, differENTial, SOcial, fiNANcial, muSIcian, physSIcian, cliNIcian, BAkery, SCEnery, coMEdian, ciVILian, techNIcian, reSIstible, imPOSsible, TERRible, arCHAic, plaTOnic, characteRIStic, diaBEtics, paediAtrics, TOpics, classifiCAtion, repoSItion, vegeTAtion, MEdia, bacTERia, vicTORia, inGREdient, PAtient, ANcient, mySTERious, reLIgious, VARious, SELfish, ENglish, PUnish, hypNOsis, diagNOsis, osMOsis'
w.p(WL, WL, WL); w.paras[-1]['untranslatedByDesign'] = True
w.p('C. Read the following prefixes and add them to the relevant word, given below to make a new word. Also write the new meaning in the given space.', 'C. درج ذیل سابقے پڑھیں اور نیا لفظ بنانے کے لیے انہیں نیچے دیے گئے متعلقہ لفظ کے ساتھ لگائیں۔ نیا معنی بھی دی گئی جگہ میں لکھیں۔', 'C. لاندې مختاړي ولولئ او د نوې کلمې د جوړولو لپاره یې لاندې ورکړل شوې اړوندې کلمې ته ورزیات کړئ. نوې مانا هم په ورکړل شوي ځای کې ولیکئ.')
PX = [('dis', 'not, opposite of', 'نہیں، کا الٹ', 'نه، ضد'), ('mis', 'wrongly', 'غلط طریقے سے', 'په غلطه'), ('un', 'not', 'نہیں', 'نه'), ('re', 'again', 'دوبارہ', 'بیا'), ('inter', 'between', 'درمیان', 'ترمنځ'),
      ('pre', 'before', 'پہلے', 'مخکې'), ('non', 'not', 'نہیں', 'نه'), ('super', 'above', 'اوپر', 'پورته'), ('sub', 'under', 'نیچے', 'لاندې'), ('anti', 'against, opposing', 'خلاف، مخالف', 'پر ضد، مخالف')]
w.table('eng12-u07-prefixes', ['Prefix', 'Meaning'], [[p, e] for p, e, _, _ in PX], ['سابقہ', 'معنی'], ['مختاړی', 'مانا'], [[p, u] for p, _, u, _ in PX], [[p, s] for p, _, _, s in PX])
WD = ['satisfied', 'spell', 'acceptable', 'election']
R = [[x, '', ''] for x in WD]
w.table('eng12-u07-prefix-words-a', ['Word', 'New Word', 'Meaning'], R, ['لفظ', 'نیا لفظ', 'معنی'], ['کلمه', 'نوې کلمه', 'مانا'], R, R)
rec = BOOK.record(w, 'eng12-u07-vocab-a', 'Vocabulary — weather idioms; stressed syllables; prefixes (1)', 'ذخیرۂ الفاظ — موسمی محاورے؛ زور دار ہجے؛ سابقے (1)', 'لغات — د هوا محاورې؛ فشار لرونکي سیلابونه؛ مختاړي (1)', 43, [73, 74])
issues = [{'id': 'eng12-p73-74', 'unit': 7, 'printedPage': 74, 'description': "Printed text retained: “'stressed'while”, “thes e words”, word-list spellings “physSIcian”, “GEnorous”, “bacTERia”; idiom column B is printed in a different order from column A (matching exercise)."}]

if __name__ == '__main__':
    BOOK.save(43, [(7, rec)], issues=issues)
