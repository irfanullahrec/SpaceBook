"""PDF48 (printed 83–84): Unit 8 economy words 12–16; B stressed syllables; C prefixes 1–10; C conditional sentences table; zero-conditional matching activity (unit end)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
B = '________'
w = Builder()
EC = [('the price of something: the amount of money that is needed to pay for or buy something', 'کسی چیز کی قیمت: کسی چیز کی ادائیگی یا خریداری کے لیے درکار رقم', 'د یو شي بیه: هغه پیسې چې د یو شي د ورکړې یا اخیستو لپاره اړینې دي'),
      ('the supply of goods available for sale in a store', 'دکان میں فروخت کے لیے دستیاب سامان کا ذخیرہ', 'په پلورنځي کې د پلور لپاره د شته توکو زېرمه'),
      ('the way in which money is used and handled', 'رقم کے استعمال اور انتظام کا طریقہ', 'د پیسو د کارولو او اداره کولو طریقه'),
      ('to put (money) in a bank account', 'بینک کھاتے میں (رقم) جمع کرنا', 'په بانکي حساب کې (پیسې) اچول'),
      ('unable to pay debts', 'قرض ادا کرنے سے قاصر', 'د پورونو د ورکولو توان نه لرونکی')]
w.group('lines', [(f'{i}. {e} {B}', f'{i}. {u} {B}', f'{i}. {p} {B}') for i, (e, u, p) in enumerate(EC, 12)])
w.p("B. The syllable of the words written in capital letters is 'stressed'while that with small letters is 'unstressed'. Practically pronounce thes e words with stressed and unstressed sounds.", 'B. الفاظ کا جو ہجا بڑے حروف میں لکھا ہے وہ ’’زور دار‘‘ ہے جبکہ چھوٹے حروف والا ’’بے زور‘‘ ہے۔ ان الفاظ کو زور دار اور بے زور آوازوں کے ساتھ عملاً ادا کریں۔', 'B. د کلمو هغه سیلاب چې په لویو تورو لیکل شوی "فشار لرونکی" دی او په کوچنیو تورو "بې‌فشاره" دی. دا کلمې د فشار لرونکو او بې‌فشاره غږونو سره عملاً تلفظ کړئ.')
WL = 'cruSADE, arCADE, aGREE, guaranTEE, sightSEER, puppeTEER, SiamESE, JapanESE, chEESE, cassETTE, CorvETTE, towelETTE, unIQUE, physIQUE, baLOON, afterNOON, carTOON, iCONic, GRAPHic, hyperTENsion, teleVIsion, nuTRItion, reveLAtion, deMOcracy, geOGraphy, ALlergy, NAUtical, CLArity, CRItical, SEAfood (sea + food), ICEland (ice + land), TOOTHpaste (tooth + paste), FOOTball (foot + ball), BAsketball (basket + ball), ten-MEter, rock-SOlid, fifteen-MInute, old-FAshioned, AIRplane mechanic, PROject manager, BOARD member, North DAKOTA, Mr. SMITH, Apple INCORPORATED, mySELF, themSELVES, ourSELVES, TEN, FIFty, ONE-hundred'
w.p(WL, WL, WL); w.paras[-1]['untranslatedByDesign'] = True
w.p('C. Add the correct prefix to the word to complete each sentence.', 'C. ہر جملہ مکمل کرنے کے لیے لفظ کے ساتھ درست سابقہ لگائیں۔', 'C. د هرې جملې د بشپړولو لپاره کلمې ته سم مختاړی ورزیات کړئ.')
PR = [
    (f'I wanted to ease my stomach {B}comfort, so I drank some ginger root tea.', f'میں اپنے معدے کی {B}comfort (بے آرامی) دور کرنا چاہتا تھا، اس لیے میں نے ادرک کی چائے پی۔', f'ما غوښتل د خپلې معدې {B}comfort (ناارامي) کمه کړم، نو د زنجبیلو چای مې وڅښه.'),
    (f'Moatasim looked funny in his {B}matched shirt and pants.', f'معتصم اپنی {B}matched (بے میل) قمیض اور پتلون میں عجیب لگ رہا تھا۔', f'معتصم په خپل {B}matched (نابرابر) کمیس او پتلون کې خندونکی ښکارېده.'),
    (f'Penelope felt {B}glamorous at the party because she was the only one not wearing a dress.', f'پینیلپی پارٹی میں خود کو {B}glamorous (بے رونق) محسوس کر رہی تھی کیونکہ وہ اکیلی تھی جس نے فراک نہیں پہنا تھا۔', f'پېنېلوپي په مېلمستیا کې ځان {B}glamorous (بې‌ښکلا) احساس کړ ځکه یوازې هغه وه چې جامې یې نه وې اغوستې.'),
    (f'My mother said those {B}aging creams do not work, so I should not waste my money on them.', f'میری والدہ نے کہا کہ وہ {B}aging (عمر روکنے والی) کریمیں کام نہیں کرتیں، اس لیے مجھے ان پر پیسہ ضائع نہیں کرنا چاہیے۔', f'مور مې وویل چې هغه {B}aging (د عمر ضد) کرېمونه کار نه کوي، نو باید پرې خپلې پیسې ضایع نه کړم.'),
    (f"The child's {B}standard performance on the test alarmed his parents.", f'ٹیسٹ میں بچے کی {B}standard (معیار سے کم) کارکردگی نے اس کے والدین کو پریشان کر دیا۔', f'په ازموینه کې د ماشوم {B}standard (له معیار ټیټ) فعالیت مور او پلار یې اندېښمن کړل.'),
    (f'When my sister first saw the meteor, she thought it was a {B}natural phenomenon.', f'جب میری بہن نے پہلی بار شہابِ ثاقب دیکھا تو اس نے سمجھا کہ یہ کوئی {B}natural (مافوق الفطرت) مظہر ہے۔', f'کله چې زما خور لومړی ځل شهاب ولید، فکر یې وکړ چې یوه {B}natural (له طبیعت پورته) پدیده ده.'),
    (f'Even though she got an excellent job offer, Ayehsa did not want to {B}locate to a different country.', f'اگرچہ اسے ملازمت کی بہترین پیشکش ملی، عائشہ کسی دوسرے ملک میں {B}locate (منتقل) نہیں ہونا چاہتی تھی۔', f'که څه هم د دندې غوره وړاندیز ورته وشو، عایشې نه غوښتل چې بل هېواد ته {B}locate (کډه) شي.'),
    (f'With a small class size, the students get to {B}act with the teacher more frequently.', f'چھوٹی جماعت ہونے کی وجہ سے طلبہ کو استاد کے ساتھ زیادہ کثرت سے {B}act (تعامل) کا موقع ملتا ہے۔', f'د کوچني ټولګي له امله زده کوونکي له ښوونکي سره ډېر ځله {B}act (تعامل) کوي.'),
    (f'I slipped on the ice because I did not heed the {B}cautions about watching my step.', f'میں برف پر پھسل گیا کیونکہ میں نے قدم سنبھال کر چلنے کی {B}cautions (پیشگی احتیاطوں) پر دھیان نہیں دیا۔', f'زه پر یخ وښوییدم ځکه چې د خپلو ګامونو د پام په اړه {B}cautions (مخکینیو خبرداریو) ته مې پام ونه کړ.'),
    (f'A {B}combatant is another word for civilian', f'{B}combatant (غیر جنگجو) شہری کا دوسرا نام ہے', f'{B}combatant (نه جنګیالی) د ملکي وګړي بله کلمه ده'),
]
w.group('lines', [(f'{i}. {e}', f'{i}. {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(PR, 1)])
w.h('C. Conditional sentences', 'C. شرطیہ جملے', 'C. شرطي جملې')
w.p('A conditional sentence is a sentence that gives a condition (e.g., If it rains) and the outcome of the condition occurring (e.g., the game will be cancelled).', 'شرطیہ جملہ وہ جملہ ہے جو ایک شرط (مثلاً اگر بارش ہوئی) اور اس شرط کے پورا ہونے کا نتیجہ (مثلاً کھیل منسوخ ہو جائے گا) بیان کرے۔', 'شرطي جمله هغه جمله ده چې یو شرط (لکه که باران وشو) او د شرط د پوره کېدو پایله (لکه لوبه به لغوه شي) ورکوي.')
w.p('There are four types of conditional sentences:', 'شرطیہ جملوں کی چار اقسام ہیں:', 'د شرطي جملو څلور ډولونه دي:')
CT = [['zero conditional', 'Expresses something as a fact', 'If you sleep, you dream.'], ['first conditional', 'States the result of a possible future event occurring', 'If you get some sleep, you will feel better.'],
      ['second conditional', 'States the result of an unlikely event occurring or an untruth being true', 'If you became an insomniac, you would understand. (unlikely event occurring) If you were an insomniac, you would understand. (untruth being true)'],
      ['third conditional', 'States how the situation would be different with a different past', 'If you had slept last night, you would have beaten your record.']]
CU = [['صفر شرطیہ', 'کسی بات کو حقیقت کے طور پر بیان کرتا ہے', 'If you sleep, you dream. (اگر آپ سوتے ہیں تو خواب دیکھتے ہیں۔)'], ['پہلا شرطیہ', 'مستقبل کے کسی ممکنہ واقعے کے ہونے کا نتیجہ بیان کرتا ہے', 'If you get some sleep, you will feel better. (اگر آپ کچھ سو لیں تو بہتر محسوس کریں گے۔)'],
      ['دوسرا شرطیہ', 'کسی غیر متوقع واقعے کے ہونے یا کسی غیر حقیقی بات کے سچ ہونے کا نتیجہ بیان کرتا ہے', 'If you became an insomniac, you would understand. (غیر متوقع واقعہ) If you were an insomniac, you would understand. (غیر حقیقی بات کا سچ ہونا)'],
      ['تیسرا شرطیہ', 'بیان کرتا ہے کہ مختلف ماضی کی صورت میں حالات کیسے مختلف ہوتے', 'If you had slept last night, you would have beaten your record. (اگر آپ کل رات سو لیتے تو اپنا ریکارڈ توڑ دیتے۔)']]
CP = [['صفر شرطي', 'یو شی د حقیقت په توګه بیانوي', 'If you sleep, you dream. (که ویده شې، خوب وینې.)'], ['لومړی شرطي', 'د راتلونکې یوې ممکنې پېښې د پېښېدو پایله بیانوي', 'If you get some sleep, you will feel better. (که لږ ویده شې، ښه به احساس کړې.)'],
      ['دویم شرطي', 'د یوې نااحتمالي پېښې د پېښېدو یا د یوې ناسمې خبرې د رښتیا کېدو پایله بیانوي', 'If you became an insomniac, you would understand. (نااحتمالي پېښه) If you were an insomniac, you would understand. (ناسمه خبره رښتیا کېدل)'],
      ['درېیم شرطي', 'بیانوي چې د بل ډول تېر سره به حالت څنګه توپیر درلود', 'If you had slept last night, you would have beaten your record. (که تېره شپه ویده شوی وای، خپل ریکارډ به دې مات کړی وای.)']]
w.table('eng12-u08-conditionals', ['Type', 'Function', 'Example'], CT, ['قسم', 'کام', 'مثال'], ['ډول', 'دنده', 'بېلګه'], CU, CP)
w.h('Activity', 'سرگرمی', 'فعالیت')
w.p('Match the clauses of zero conditional sentence in the given columns', 'دیے گئے کالموں میں صفر شرطیہ جملے کے اجزاء کو ملائیں', 'په ورکړل شویو ستونونو کې د صفر شرطي جملې برخې سره برابرې کړئ')
A = ['If I am late for class,', 'When he stays up very late,', 'People get hungry', 'If you study hard,', 'When she watches a movie,', 'When I cross the street,', "I can't do my homework,", 'He always smiles', 'If I miss the bus,', 'When you make lots of noise,', 'Tea tastes sweet', 'You should eat less', 'I always take my umbrella', "When I'm sad,", 'When he cleans the house,']
Bc = ['he is very tired the next morning.', 'he listens to music.', 'I always look left and right.', 'I take a taxi to work.', 'I watch a funny movie.', "if I don't have my glasses.", "if they don't eat.", 'if you add some sugar.', 'if you want to lose weight.', 'my teacher gets angry.', 'she likes to eat popcorn.', 'the librarian gets angry.', 'when he is happy.', 'when it rains.', 'you get good grades in school.']
R = [[f'{i}. {a}', b] for i, (a, b) in enumerate(zip(A, Bc), 1)]
w.table('eng12-u08-zero-cond', ['A', 'B'], R, ['A', 'B'], ['A', 'B'], R, R)
rec = BOOK.record(w, 'eng12-u08-vocab-b', 'Economy words (12–16); stressed syllables; prefixes; Conditional sentences', 'معیشت کے الفاظ (12–16)؛ زور دار ہجے؛ سابقے؛ شرطیہ جملے', 'د اقتصاد کلمې (12–16)؛ فشار لرونکي سیلابونه؛ مختاړي؛ شرطي جملې', 48, [83, 84])
issues = [{'id': 'eng12-p83-84', 'unit': 8, 'printedPage': 84, 'description': "Printed text retained: “'stressed'while”, “thes e words”, “baLOON” (balloon), “Ayehsa”, “ten-MEter”; two sub-sections are both labelled “C.” (prefixes and conditional sentences). Zero-conditional column B is printed in a different order (matching exercise)."}]

if __name__ == '__main__':
    BOOK.save(48, [(8, rec)], issues=issues, complete_units=[8])
