"""PDF122 (printed 231 + inside back cover): Authors' Profile; Qur'anic verse; KPTBB Textbook Feedback Form. Completes Unit 19 and the book."""
from class12_book_common import Book, Builder

BOOK = Book('english')
a = Builder()
a.h("Authors' Profile", 'مصنفین کا تعارف', 'د لیکوالانو پېژندنه')
a.h('Ali Akbar Khan', 'علی اکبر خان', 'علي اکبر خان')
a.p('(Asst. Professor of English, Higher Education Department, KPK.) Ali Akbar Khan has been teaching English language and literature at Intermediate, Graduate and Postgraduate levels. He has served in many positions in Higher Education Department, Government of Khyber Pakhtunkhwa and is currently serving as head of the Department of English in Degree College Lakaro District Mohmand. He has also co-authored the textbook of English for Grade X for Khyber Pakhtunkhwa Textbook Board, Peshawar.',
    '(اسسٹنٹ پروفیسر انگریزی، محکمہ اعلیٰ تعلیم، خیبر پختونخوا) علی اکبر خان انٹرمیڈیٹ، گریجویٹ اور پوسٹ گریجویٹ سطح پر انگریزی زبان و ادب پڑھاتے رہے ہیں۔ وہ حکومتِ خیبر پختونخوا کے محکمہ اعلیٰ تعلیم میں کئی عہدوں پر خدمات انجام دے چکے ہیں اور اس وقت ڈگری کالج لکڑو ضلع مہمند میں شعبۂ انگریزی کے سربراہ ہیں۔ انہوں نے خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور کے لیے دسویں جماعت کی انگریزی کی درسی کتاب کی مشترکہ تصنیف بھی کی ہے۔',
    '(د انګرېزي اسسټنټ پروفیسر، د لوړو زده کړو ریاست، خیبر پښتونخوا) علي اکبر خان په انټرمیډیټ، فارغ او له فراغت وروسته کچو کې انګرېزي ژبه او ادب تدریسوي. هغه د خیبر پښتونخوا حکومت د لوړو زده کړو په ریاست کې په ډېرو دندو کار کړی او اوس د مهمند ولسوالۍ د لکړو په ډګري کالج کې د انګرېزي څانګې مشر دی. هغه د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور لپاره د لسم ټولګي د انګرېزي درسي کتاب ګډ لیکوال هم دی.')
a.h('Jaffar Ali khan Nurar', 'جعفر علی خان نورار', 'جعفر علي خان نورار')
a.p('(Senior Subject Specialist in English, E&SE. Department, KPK.) Jaffar Ali Khan is Senior Subject Specialist, serving in Elementary and Secondary Education Department. He is MA English, MA TEFL and Master of Education with speciality in Teacher Education. He has got an ample experience of more than 20 years of teaching English at intermediate and advance levels.He has attended and conducted many workshops as Master Trainer.',
    '(سینئر سبجیکٹ اسپیشلسٹ انگریزی، محکمہ ابتدائی و ثانوی تعلیم، خیبر پختونخوا) جعفر علی خان محکمہ ابتدائی و ثانوی تعلیم میں سینئر سبجیکٹ اسپیشلسٹ ہیں۔ وہ ایم اے انگریزی، ایم اے ٹی ای ایف ایل اور اساتذہ کی تعلیم میں تخصص کے ساتھ ماسٹر آف ایجوکیشن ہیں۔ انہیں انٹرمیڈیٹ اور اعلیٰ سطح پر انگریزی پڑھانے کا 20 سال سے زیادہ کا وسیع تجربہ ہے۔ وہ ماسٹر ٹرینر کے طور پر کئی ورکشاپس میں شرکت اور ان کا انعقاد کر چکے ہیں۔',
    '(د انګرېزي سینیر سبجیکټ سپیشلسټ، د لومړنیو او ثانوي زده کړو ریاست، خیبر پښتونخوا) جعفر علي خان د لومړنیو او ثانوي زده کړو په ریاست کې سینیر سبجیکټ سپیشلسټ دی. هغه د انګرېزي ماسټري، د TEFL ماسټري او د ښوونکو په روزنه کې د تخصص سره د زده کړې ماسټري لري. په انټرمیډیټ او لوړو کچو کې د انګرېزي تدریس له 20 کلونو زیاته پراخه تجربه لري. هغه د ماسټر ټرېنر په توګه په ډېرو ورکشاپونو کې ګډون او د هغو تنظیم کړی.')
au = BOOK.record(a, 'eng12-backmatter-authors', "Authors' Profile", 'مصنفین کا تعارف', 'د لیکوالانو پېژندنه', 122, [231])

f = Builder()
f.p('مومن تو آپس میں بھائی بھائی ہیں۔ پس اپنے دو بھائیوں میں صلح کرا دیا کرو اور اللہ سے ڈرتے رہو تاکہ تم پر رحمت کی جائے۔ (سورۃ الحجرات: 10)',
    'مومن تو آپس میں بھائی بھائی ہیں۔ پس اپنے دو بھائیوں میں صلح کرا دیا کرو اور اللہ سے ڈرتے رہو تاکہ تم پر رحمت کی جائے۔ (سورۃ الحجرات: 10)',
    'مومنان خو سره وروڼه دي. نو د خپلو دوو وروڼو ترمنځ روغه کوئ او له الله ووېرېږئ ترڅو پر تاسو رحم وشي. (سورة الحجرات: 10)')
f.paras[-1]['englishGloss'] = 'The believers are but brothers, so make peace between your brothers and fear Allah that you may receive mercy. (Al-Hujurat 49:10) [printed in Urdu only]'
f.h('Khyber Pakhtunkhwa Textbook Board — TEXTBOOK FEEDBACK FORM', 'خیبر پختونخوا ٹیکسٹ بک بورڈ — درسی کتاب کا فیڈ بیک فارم', 'د خیبر پښتونخوا د درسي کتابونو بورډ — د درسي کتاب د نظر فورمه')
f.p('Phase – V, Hayatabad Peshawar. Phone: 091-9217714-15 Fax: 091-9217163, Website: www.kptbb.gov.pk', 'فیز – V، حیات آباد پشاور۔ فون: 091-9217714-15 فیکس: 091-9217163، ویب سائٹ: www.kptbb.gov.pk', 'فاز – V، حیات‌اباد پېښور. ټیلیفون: 091-9217714-15 فکس: 091-9217163، وېبپاڼه: www.kptbb.gov.pk')
S = [('Overall the book is interesting and user friendly.', 'مجموعی طور پر کتاب دلچسپ اور استعمال میں آسان ہے۔', 'په ټولیز ډول کتاب په زړه پورې او د کارونې لپاره اسانه دی.'),
     ('The language and content of the book is age / grade appropriate and the content is free of grammatical and punctuation errors.', 'کتاب کی زبان اور مواد عمر / جماعت کے مطابق ہے اور مواد قواعد اور رموزِ اوقاف کی غلطیوں سے پاک ہے۔', 'د کتاب ژبه او منځپانګه د عمر / ټولګي سره سمه ده او منځپانګه د ګرامر او د تکي‌ایښودنې له تېروتنو پاکه ده.'),
     ('Content is supported with examples from real life / culture.', 'مواد کی حقیقی زندگی / ثقافت سے مثالوں کے ذریعے تائید کی گئی ہے۔', 'منځپانګه د رښتیني ژوند / کلتور له بېلګو سره ملاتړ شوې.'),
     ('Contents / texts are authentic and updated.', 'مواد / متون مستند اور تازہ ترین ہیں۔', 'منځپانګې / متنونه معتبر او تازه دي.'),
     ('Pictures / diagrams / graphs / illustrations are informative, relevant and clear if not, then identify them.', 'تصاویر / خاکے / گراف / توضیحی اشکال معلوماتی، متعلقہ اور واضح ہیں؛ اگر نہیں تو ان کی نشاندہی کریں۔', 'انځورونه / ډیاګرامونه / ګرافونه / توضیحي شکلونه معلوماتي، اړوند او روښانه دي؛ که نه وي، وې پېژنئ.'),
     ('Activities, projects and additional work is suggested for reinforcement of concepts.', 'تصورات کی پختگی کے لیے سرگرمیاں، منصوبے اور اضافی کام تجویز کیے گئے ہیں۔', 'د مفاهیمو د پیاوړتیا لپاره فعالیتونه، پروژې او اضافي کار وړاندیز شوي.'),
     ('Assessment achievements are thought provoking and comprise cognitive, psychomotor and effective skills.', 'جانچ کے نتائج فکر انگیز ہیں اور ادراکی، نفسی حرکی اور مؤثر (جذباتی) مہارتوں پر مشتمل ہیں۔', 'د ارزونې لاسته راوړنې فکر راپاروونکې دي او ادراکي، رواني-حرکي او اغېزناکې (احساسي) مهارتونه لري.'),
     ('The textbook is easy to be covered within academic year.', 'درسی کتاب تعلیمی سال کے اندر آسانی سے مکمل کیا جا سکتا ہے۔', 'درسي کتاب د تعلیمي کال په اوږدو کې په اسانۍ بشپړېدای شي.')]
f.table('eng12-feedback-statements', ['S#', 'Statement', 'Remarks'], [[f'{i}.', e, ''] for i, (e, u, p) in enumerate(S, 1)],
        ['نمبر', 'بیان', 'تبصرہ'], ['شمېره', 'وینا', 'تبصره'], [[f'{i}.', u, ''] for i, (e, u, p) in enumerate(S, 1)], [[f'{i}.', p, ''] for i, (e, u, p) in enumerate(S, 1)])
blank = [['', '', ''] for _ in range(5)]
f.table('eng12-feedback-pages', ['Page No.', 'Observation/comments', 'Suggested amendment along with rationale'], blank, ['صفحہ نمبر', 'مشاہدہ/تبصرہ', 'مجوزہ ترمیم مع وجہ'], ['مخ شمېره', 'کتنه/تبصره', 'وړاندیز شوې اصلاح د دلیل سره'])
f.group('lines', [('General Remarks: ____________', 'عمومی تبصرہ: ____________', 'عمومي تبصره: ____________'),
                  ('Name & Address: ____________', 'نام اور پتہ: ____________', 'نوم او پته: ____________'),
                  ('Contact No. & Email: ____________', 'رابطہ نمبر اور ای میل: ____________', 'د اړیکې شمېره او برېښنالیک: ____________')])
fb = BOOK.record(f, 'eng12-backmatter-feedback', 'Textbook Feedback Form', 'درسی کتاب کا فیڈ بیک فارم', 'د درسي کتاب د نظر فورمه', 122, [232])
fb['sourceCoverIllustrationReview'] = 'KPTBB logo on the feedback form is decorative; not reproduced.'
issues = [{'id': 'eng12-p231-232', 'unit': 19, 'printedPage': 231, 'description': 'Back matter appended to Unit 19 (as for Statistics). Authors’ Profile retained as printed: “KPK.)” closing brackets without openers, “Jaffar Ali khan Nurar”, “advance levels.He”. Feedback form retained: “effective skills” (affective), “is easy to be covered”. The Qur’anic verse (Al-Hujurat 10) is printed in Urdu only; shown as printed with an English gloss.'}]

if __name__ == '__main__':
    BOOK.save(122, [(19, au), (19, fb)], issues=issues, complete_units=[19])
