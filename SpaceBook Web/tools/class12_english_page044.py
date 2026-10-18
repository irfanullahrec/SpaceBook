"""PDF44 (printed 75–76): Unit 7 prefix words (end); D apposition 1–10; E noun clauses + completion exercise 1–15 (unit end)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
B = '________'
w = Builder()
WD = ['related', 'pay', 'sense', 'script', 'merge', 'bacterial']
R = [[x, '', ''] for x in WD]
w.table('eng12-u07-prefix-words-b', ['Word', 'New Word', 'Meaning'], R, ['لفظ', 'نیا لفظ', 'معنی'], ['کلمه', 'نوې کلمه', 'مانا'], R, R)
w.p('D. Combine the following sentences by placing nouns and noun phrases in apposition.', 'D. اسماء اور اسمی فقروں کو بدل (اپوزیشن) کے طور پر رکھ کر درج ذیل جملوں کو ملائیں۔', 'D. د نومونو او نومي عبارتونو د بدل (اپوزیشن) په توګه په ایښودو لاندې جملې سره یوځای کړئ.')
AP = [
    ('The first prime Minister of Pakistan was assassinated in 1951. He was Liaqat Ali Khan.', 'پاکستان کے پہلے وزیرِ اعظم 1951 میں قتل کیے گئے۔ وہ لیاقت علی خان تھے۔', 'د پاکستان لومړی وزیر په 1951 کې ووژل شو. هغه لیاقت علي خان و.'),
    ("The river Indus' annual flow is about 243 cubic kilometres. It is the longest river of Pakistan.", 'دریائے سندھ کا سالانہ بہاؤ تقریباً 243 مکعب کلومیٹر ہے۔ یہ پاکستان کا سب سے لمبا دریا ہے۔', 'د سند سیند کلنی بهیر شاوخوا 243 مکعب کیلومتره دی. دا د پاکستان تر ټولو اوږد سیند دی.'),
    ('Ustad Ahmad Lahori was the chief architect of Taj Mahal, in Agra, India. He hailed from Lahore.', 'استاد احمد لاہوری آگرہ، بھارت میں تاج محل کے چیف معمار تھے۔ ان کا تعلق لاہور سے تھا۔', 'استاد احمد لاهوري د هند په اګره کې د تاج محل مشر معمار و. هغه د لاهور و.'),
    ('John Kennedy was known for his eloquent and inspirational speeches. He was a popular US President.', 'جان کینیڈی اپنی فصیح اور ولولہ انگیز تقریروں کے لیے مشہور تھے۔ وہ ایک مقبول امریکی صدر تھے۔', 'جان کېنډي د خپلو فصیحو او الهام‌بښونکو ویناوو له امله مشهور و. هغه یو مشهور امریکایي ولسمشر و.'),
    ('The first country to recognise Pakistan is The Islamic republic of Iran. It is our neighbouring country.', 'پاکستان کو تسلیم کرنے والا پہلا ملک اسلامی جمہوریہ ایران ہے۔ یہ ہمارا پڑوسی ملک ہے۔', 'لومړنی هېواد چې پاکستان یې په رسمیت وپېژانده د ایران اسلامي جمهوریت دی. دا زموږ ګاونډی هېواد دی.'),
    ("My uncle's car is the envoy of my friends. It is a sporty red convertible with bucket seats.", 'میرے چچا کی گاڑی میرے دوستوں کی رشک ہے۔ یہ بکٹ سیٹوں والی ایک اسپورٹی سرخ کنورٹیبل ہے۔', 'زما د تره موټر زما د ملګرو د حسد وړ دی. دا د بکټ څوکیو سره یو سپورټي سور کنورټیبل دی.'),
    ('The chief surgeon took his daughter on a hospital tour. He is an expert in in organ transplant procedures.', 'چیف سرجن اپنی بیٹی کو ہسپتال کے دورے پر لے گئے۔ وہ اعضاء کی پیوند کاری کے ماہر ہیں۔', 'مشر جراح خپله لور د روغتون لیدنې ته بوتله. هغه د غړو د پیوند په پروسیجرونو کې متخصص دی.'),
    ('The problem delayed the entire program. It was that you did not come on time.', 'مسئلے نے پورے پروگرام میں تاخیر کر دی۔ وہ یہ تھا کہ تم وقت پر نہیں آئے۔', 'ستونزې ټول پروګرام وځنډاوه. هغه دا وه چې ته پر وخت رانه غلې.'),
    ('The worry troubles me too much. It is who we should invite.', 'فکر مجھے بہت پریشان کرتی ہے۔ وہ یہ ہے کہ ہمیں کسے مدعو کرنا چاہیے۔', 'اندېښنه ما ډېر ځوروي. هغه دا ده چې باید چا ته بلنه ورکړو.'),
    ('Hamad is very dear to me. He is my younger brother.', 'حماد مجھے بہت عزیز ہے۔ وہ میرا چھوٹا بھائی ہے۔', 'حماد ماته ډېر ګران دی. هغه زما کشر ورور دی.'),
]
w.group('lines', [(f'{i}. {e}', f'{i}. {e} — ({u})', f'{i}. {e} — ({p})') for i, (e, u, p) in enumerate(AP, 1)])
w.h('E. Noun Clauses', 'E. اسمیہ جملے (نَون کلازز)', 'E. نومي جملې (نون کلازونه)')
w.p('Noun clauses are dependent clauses that can replace any noun in the sentence: subjects, objects, and/or subject complements. In all, there are five different functions that a noun clause can serve: subjects, direct objects, indirect objects, objects of the preposition and subject complements.', 'اسمیہ جملے تابع جملے ہیں جو جملے میں کسی بھی اسم کی جگہ لے سکتے ہیں: فاعل، مفعول اور/یا فاعل کا تکملہ۔ مجموعی طور پر اسمیہ جملہ پانچ مختلف کام کر سکتا ہے: فاعل، مفعولِ صریح، مفعولِ غیر صریح، حرفِ جار کا مفعول اور فاعل کا تکملہ۔', 'نومي جملې تابع جملې دي چې په جمله کې د هر نوم ځای نیولی شي: فاعل، مفعول او/یا د فاعل بشپړوونکی. په ټوله کې نومي جمله پنځه بېلابېلې دندې ترسره کولی شي: فاعل، مستقیم مفعول، غیرمستقیم مفعول، د اضافې مفعول او د فاعل بشپړوونکی.')
w.p('Using the noun clauses given at the end, complete the following sentences:', 'آخر میں دیے گئے اسمیہ جملوں کو استعمال کرتے ہوئے درج ذیل جملے مکمل کریں:', 'په پای کې د ورکړل شویو نومي جملو په کارولو لاندې جملې بشپړې کړئ:')
NC = [(f'The prize will be given to {B}.', f'انعام {B} کو دیا جائے گا۔', f'جایزه به {B} ته ورکړل شي.'), (f'Do you know {B}?', f'کیا آپ جانتے ہیں {B}؟', f'ایا پوهېږې {B}؟'), (f"I don't understand {B}.", f'میں نہیں سمجھتا {B}۔', f'زه نه پوهېږم {B}.'),
      (f'{B} made his friends angry.', f'{B} نے اس کے دوستوں کو ناراض کر دیا۔', f'{B} د هغه ملګري په غوسه کړل.'), (f'{B} astonished her teachers.', f'{B} نے اس کے اساتذہ کو حیران کر دیا۔', f'{B} د هغې ښوونکي حیران کړل.'),
      (f'{B} was not very agreeable.', f'{B} زیادہ خوشگوار نہیں تھا۔', f'{B} ډېر د خوښې وړ نه و.'), (f'The food inspector checked {B}.', f'فوڈ انسپکٹر نے جانچا {B}۔', f'د خوړو څارونکي وکتل {B}.'),
      (f'She did not know {B}.', f'وہ نہیں جانتی تھی {B}۔', f'هغې نه پوهېده {B}.'), (f'His problem was {B}.', f'اس کا مسئلہ یہ تھا {B}۔', f'د هغه ستونزه دا وه {B}.'),
      (f"Hammad's great achievement at school was {B}.", f'اسکول میں حماد کی بڑی کامیابی یہ تھی {B}۔', f'په ښوونځي کې د حماد لویه لاسته راوړنه دا وه {B}.'), (f'The teacher is not responsible for {B}.', f'استاد {B} کا ذمہ دار نہیں۔', f'ښوونکی د {B} مسؤل نه دی.'),
      (f'The money will go to {B}.', f'پیسہ {B} کو جائے گا۔', f'پیسې به {B} ته ولاړې شي.'), (f"It's very disappointing {B}.", f'یہ بہت مایوس کن ہے {B}۔', f'دا ډېره مایوسوونکې ده {B}.'),
      (f'They are perfectly happy {B}.', f'وہ بالکل خوش ہیں {B}۔', f'دوی بشپړ خوشاله دي {B}.'), (f'Umair runs so fast {B}.', f'عمیر اتنا تیز دوڑتا ہے {B}۔', f'عمیر دومره ګړندی منډه وهي {B}.')]
w.group('lines', [(f'{i}. {e}', f'{i}. {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(NC, 1)])
L = "Noun clauses: ( that he couldn't speak fluently, what Hurain wrote, whichever charity you choose, where they live now, that you were coming with us, what time it is, when he became the class proctor, what you are talking about, whoever stands first in the class, what the students decided to do, that the food was hygienically safe, what Umair said, that you failed in the examination, how the girl behaved, that he can outrun a cat)"
w.p(L, L, L); w.paras[-1]['untranslatedByDesign'] = True
rec = BOOK.record(w, 'eng12-u07-vocab-b', 'Prefix words (end); Apposition; Noun clauses', 'سابقہ دار الفاظ (اختتام)؛ بدل؛ اسمیہ جملے', 'مختاړي کلمې (پای)؛ بدل؛ نومي جملې', 44, [75, 76])
issues = [{'id': 'eng12-p75-76', 'unit': 7, 'printedPage': 75, 'description': 'Printed text retained: “cubic kil ometres”, “the envoy of my friends” (envy), “an expert in in organ transplant”, item 9 “It is who we should invite”; right edge of p75 clipped (“subjects, objects”, “a noun clause”, “objects of the preposition”), completed from context.'}]

if __name__ == '__main__':
    BOOK.save(44, [(7, rec)], issues=issues, complete_units=[7])
