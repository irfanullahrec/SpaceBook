"""PDF32 (printed 51–52): Unit 5 root-word table; D parts of speech (a) 1–15, (b) underlined words 1–15 (unit end)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
w = Builder()
w.p('Identify the root word for the following words.', 'درج ذیل الفاظ کا مادّہ (روٹ ورڈ) پہچانیں۔', 'د لاندې کلمو رېښه‌ییزه کلمه وپېژنئ.')
W = ['mountain', 'rescued', 'naturalist', 'stormy', 'loaner', 'kindness', 'answered', 'respectful', 'completed', 'misspell', 'migration', 'actor', 'champion', 'nervous', 'servant']
R = [[str(i), x, ''] for i, x in enumerate(W, 1)]
w.table('eng12-u05-roots', ['No.', 'Word', 'Root Word'], R, ['نمبر', 'لفظ', 'مادّہ'], ['شمېره', 'کلمه', 'رېښه'], R, R)
w.h('D. Parts of Speech: Activities on Parsing:', 'D. اجزائے کلام: تجزیۂ نحوی کی سرگرمیاں:', 'D. د وینا برخې: د نحوي تجزیې فعالیتونه:')
w.p('(a). Pick out nouns, verbs, adverbs, adjectives and prepositions in the following sentences:', '(a). درج ذیل جملوں میں اسماء، افعال، متعلقاتِ فعل، صفات اور حروفِ جار چن کر الگ کریں:', '(a). په لاندې جملو کې نومونه، فعلونه، قیدونه، صفتونه او اضافې وټاکئ:')
A = ['In that house lived two men.', 'look, an aged woman came by.', 'The colour of this cap is quite different from that one.', 'Now I saw in my dream that he spoke many good words.', 'The most cruel dog was thereabout.',
     'We must clear up this misunderstanding between us.', 'It was a fine jacket, green and clean.', 'Nowadays, people usually talk about the dearness when they meet in the streets.', 'I saw in my dream that my father spoke many good words.',
     'In the current circumstances, I think it is very kind of you to help me with the problem.', 'Jack covered his small nose in sunblock.', 'I threw the round frisbee as far as I could.', 'My family rented a beach house for our summer vacation.',
     'The beautiful sunset added the perfect touch to our summer afternoon.', 'Beach volleyball is very popular during the summer.']
AU = ['اس گھر میں دو آدمی رہتے تھے۔', 'دیکھو، ایک بوڑھی عورت پاس سے گزری۔', 'اس ٹوپی کا رنگ اُس والی سے بالکل مختلف ہے۔', 'اب میں نے خواب میں دیکھا کہ اس نے بہت سی اچھی باتیں کہیں۔', 'سب سے ظالم کتا آس پاس ہی تھا۔',
      'ہمیں اپنے درمیان یہ غلط فہمی دور کرنی چاہیے۔', 'یہ ایک عمدہ جیکٹ تھی، سبز اور صاف۔', 'آج کل لوگ گلیوں میں ملتے ہیں تو عموماً مہنگائی کی بات کرتے ہیں۔', 'میں نے خواب میں دیکھا کہ میرے والد نے بہت سی اچھی باتیں کہیں۔',
      'موجودہ حالات میں میرے خیال میں یہ آپ کی بڑی مہربانی ہے کہ آپ مسئلے میں میری مدد کر رہے ہیں۔', 'جیک نے اپنی چھوٹی ناک کو سن بلاک سے ڈھانپ لیا۔', 'میں نے گول فریزبی جتنی دور پھینک سکا پھینکی۔', 'میرے گھرانے نے گرمیوں کی چھٹیوں کے لیے ساحلی گھر کرائے پر لیا۔',
      'خوبصورت غروبِ آفتاب نے ہماری گرمیوں کی سہ پہر کو مکمل کر دیا۔', 'ساحلی والی بال گرمیوں میں بہت مقبول ہے۔']
AP = ['په هغه کور کې دوه سړي اوسېدل.', 'وګوره، یوه زړه ښځه تېره شوه.', 'د دې خولۍ رنګ له هغې بالکل بېل دی.', 'اوس ما په خوب کې ولیدل چې هغه ډېرې ښې خبرې وکړې.', 'تر ټولو ظالم سپی همدلته شاوخوا و.',
      'موږ باید زموږ ترمنځ دا ناپوهي لرې کړو.', 'دا یو ښه جاکټ و، شین او پاک.', 'نن سبا خلک کله چې په کوڅو کې سره ګوري، معمولاً د ګرانۍ خبرې کوي.', 'ما په خوب کې ولیدل چې پلار مې ډېرې ښې خبرې وکړې.',
      'په اوسنیو شرایطو کې زما په اند ستاسو ډېره مهرباني ده چې په ستونزه کې مې مرسته کوئ.', 'جېک خپله کوچنۍ پوزه په لمر‌ساتونکي کرېم پوښلې.', 'ما ګرده فریزبي څومره چې لرې مې کولی شوه، وغورځوله.', 'زموږ کورنۍ د اوړني رخصتۍ لپاره د سمندر غاړې کور په کرایه ونیو.',
      'ښکلي لمرپرېوتو زموږ د اوړي ماسپښین ته بشپړه ښکلا ورکړه.', 'د سمندر غاړې والیبال په اوړي کې ډېر مشهور دی.']
w.group('lines', [(f'{i}. {e}', f'{i}. {e} — ({u})', f'{i}. {e} — ({p})') for i, (e, u, p) in enumerate(zip(A, AU, AP), 1)])
w.p('(b). Which part of speech are the underlined words in the following sentences', '(b). درج ذیل جملوں میں خط کشیدہ الفاظ کون سا جزوِ کلام ہیں', '(b). په لاندې جملو کې لاندې کرښه لرونکې کلمې د وینا کومه برخه دي')
Bs = [('She thought of a wise plan.', 'thought'), ('I want to go now.', 'now'), ('Where are you going?', 'you'), ('The sun gives us heat and light.', 'gives'), ('Aleena is my best friend.', 'best'),
      ('The pen was expensive; still I bought it.', 'bought'), ('That was a lovely evening.', 'lovely'), ('Wy father works in a factory.', 'factory'), ('She must be a stupid.', 'stupid'), ('The cat is under the bed.', 'under'),
      ('Jasmines are white in colour.', 'white'), ('Do it quickly.', 'quickly'), ('He went to the market to buy some vegetables.', 'to'), ('I helped him because he is poor.', 'because'), ('It is my handkerchief.', 'It')]
w.group('lines', [(f'{i}. {s} [underlined: {u}]', f'{i}. {s} [خط کشیدہ لفظ: {u}]', f'{i}. {s} [لاندې کرښه: {u}]') for i, (s, u) in enumerate(Bs, 1)])
ex = BOOK.record(w, 'eng12-u05-vocab-b', 'Root words; Parts of speech (parsing) (a) and (b)', 'مادّہ الفاظ؛ اجزائے کلام (تجزیہ) (a) اور (b)', 'رېښه‌ییزې کلمې؛ د وینا برخې (تجزیه) (a) او (b)', 32, [51, 52])
issues = [{'id': 'eng12-p51-52', 'unit': 5, 'printedPage': 52, 'description': 'Printed text retained: (a)2 “look, an aged woman” (lower-case), (b)8 “Wy father”, (b)9 “She must be a stupid.” Underlining is shown as “[underlined: …]” because the app does not reproduce underline formatting inside paired text.'}]

if __name__ == '__main__':
    BOOK.save(32, [(5, ex)], issues=issues, complete_units=[5])
