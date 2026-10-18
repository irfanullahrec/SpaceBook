"""Urdu XII PDF20 (spread): printed pp.30–31 — Lesson 4 text end (Iqbal couplet; source تصوراتِ اقبالؒ) and مشق Q1–Q4."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
t = Builder()
t.p('Now that we are free, our love of the homeland will neither overpower our ties with the millat nor harm them. As far as we are concerned, we shall always remain ready to fulfil this desire of the Poet of Islam:',
    'اب کہ ہم آزاد ہیں، ہماری وطن دوستی ہمارے ملی روابط پر غالب نہ آئے گی اور نہ انھیں نقصان پہنچائے گی۔ جہاں تک ہمارا تعلق ہے، ہم شاعرِ اسلام کی اس آرزو کو بر لانے کے لیے ہمیشہ سربکف رہیں گے۔',
    'اوس چې موږ ازاد یو، زموږ وطن‌دوستي به زموږ پر ملي اړیکو برلاسې نه شي او نه به ورته زیان ورسوي. تر هغه ځایه چې زموږ خبره ده، موږ به د اسلام د شاعر د دې هیلې د پوره کولو لپاره تل سر په لاس یو:')
t.group('lines', [('“Let the Muslims be one for the guarding of the Haram (the Kaʿba),', 'ایک ہوں مسلم، حرم کی پاسبانی کے لیے', 'مسلمانان دې د حرم د ساتنې لپاره یو شي'),
                  ('from the shore of the Nile to the soil of Kashghar.”', 'نیل کے ساحل سے لے کر تابہ خاکِ کاشغر', 'د نیل له غاړې نیولې تر کاشغر خاورې پورې')])
t.p('(Tasawwurat-e-Iqbal)', '(تصوراتِ اقبالؒ)', '(تصورات اقبال)')
tx = BOOK.record(t, 'urdu12-u4-text-3', 'Lesson text (3)', 'متنِ سبق (۳)', 'د لوست متن (۳)', 20, [30])

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Give short answers to the following:', '۱۔ درج ذیل کے مختصر جوابات دیں:', '۱. لاندې ته لنډ ځوابونه ورکړئ:')
e.group('lines', [
    ('(a) With what feeling were the hearts of the Muslims of India filled before the creation of Pakistan?', '(الف) پاکستان کے قیام سے پہلے اسلامیانِ ہند کے دل کس جذبے سے سرشار تھے؟', '(الف) د پاکستان له جوړېدو مخکې د هند د مسلمانانو زړونه په کوم احساس ډک وو؟'),
    ('(b) What is our national ideal?', '(ب) ہمارا قومی نصب العین کیا ہے؟', '(ب) زموږ ملي موخه څه ده؟'),
    ('(c) What is the straight path to achieving the national ideal?', '(ج) قومی نصب العین کے حصول کا سیدھا راستہ کون سا ہے؟', '(ج) د ملي موخې د ترلاسه کولو سمه لار کومه ده؟'),
    ('(d) Who gave us the concept of “Pakistan”?', '(د) ہمیں ’’پاکستان‘‘ کا تصور کس نے دیا؟', '(د) موږ ته د "پاکستان" تصور چا راکړ؟'),
    ('(e) Why did Iqbal turn his attention to the practical politics of the Muslims of India?', '(ہ) اقبالؒ نے مسلمانانِ ہند کی عملی سیاسیات کی طرف اپنی توجہ کیوں مبذول کی؟', '(ه) اقبال ولې د هند د مسلمانانو عملي سیاست ته پام واړاوه؟'),
    ("(f) Why did Iqbal's concept of Pakistan bear no relation to his world-embracing concept of the millat?", '(و) اقبالؒ کا تصورِ پاکستان اس کے آفاق گیر تصورِ ملت سے کیوں نسبت نہیں رکھتا تھا؟', '(و) د اقبال د پاکستان تصور ولې د هغه د نړۍ‌ګېر ملت له تصور سره تړاو نه درلود؟'),
    ('(g) Now that we have obtained the free homeland of Pakistan, according to the author what is logically incumbent upon us?', '(ز) جب ہم نے آزاد وطن پاکستان حاصل کر لیا تو بقولِ مصنف اب منطقی طور پر ہمارے لیے کیا لازم ہے؟', '(ز) کله چې موږ د پاکستان ازاد وطن ترلاسه کړ، د لیکوال په وینا اوس په منطقي ډول موږ ته څه لازم دي؟'),
    ('(h) Tipu Sultan, Sultan Abdul Hamid II, Syed Jamaluddin Afghani and Allama Iqbal were preachers of which common concept?', '(ح) ٹیپو سلطانؒ، سلطان عبدالحمید ثانیؒ، سید جمال الدین افغانیؒ اور علامہ اقبالؒ کس مشترک تصوّر کے مبلّغ تھے؟', '(ح) ټیپو سلطان، سلطان عبدالحمید دویم، سید جمال الدین افغاني او علامه اقبال د کوم ګډ تصور مبلغان وو؟'),
])
e.p('2. Write detailed answers to the following questions:', '۲۔ درج ذیل سوالات کے مفصل جواب تحریر کریں:', '۲. لاندې پوښتنو ته مفصل ځوابونه ولیکئ:')
e.group('lines', [
    ('(a) On which important points has the author thrown light in the essay?', '(الف) مضمون میں مصنف نے کن اہم نکات پر روشنی ڈالی ہے؟', '(الف) لیکوال په مقاله کې پر کومو مهمو ټکو رڼا اچولې؟'),
    ('(b) Why was the creation of Pakistan necessary for the Muslims of the subcontinent?', '(ب) پاکستان کا قیام برصغیر کے مسلمانوں کے لیے کیوں ضروری تھا؟', '(ب) د نیمې وچې د مسلمانانو لپاره د پاکستان جوړېدل ولې اړین وو؟'),
    ('(c) What role can Pakistan play with regard to the unity of the Islamic millat?', '(ج) ملتِ اسلامیہ کے اتحاد کے ضمن میں پاکستان کیا کردار ادا کر سکتا ہے؟', '(ج) د اسلامي ملت د یووالي په برخه کې پاکستان کوم رول لوبولی شي؟'),
    ('(d) According to the author, how shall we be able to raise high the word of Allah?', '(د) بقولِ مصنف ہم کیوں کر اعلائے کلمتہ اللہ کر سکیں گے؟', '(د) د لیکوال په وینا موږ به څنګه د الله کلمه لوړه کړای شو؟'),
    ('(e) “Let the Muslims be one for the guarding of the Haram / from the shore of the Nile to the soil of Kashghar” — whose couplet is this? Explain its meaning in the context of this essay.', '(ہ) ایک ہوں مسلم حرم کی پاسبانی کے لیے — نیل کے ساحل سے لے کر تابہ خاکِ کاشغر — یہ شعر کس شاعر کا ہے؟ اس مضمون کے تناظر میں شعر کا مفہوم واضح کریں۔', '(ه) "مسلمانان دې د حرم د ساتنې لپاره یو شي — د نیل له غاړې تر کاشغر خاورې" — دا بیت د کوم شاعر دی؟ د دې مقالې په چوکاټ کې یې مانا روښانه کړئ.'),
])
e.p('3. Identify the auxiliary verbs (imdādī afʿāl) in the following sentences:', '۳۔ درج ذیل جملوں میں امدادی افعال کی نشاندہی کریں:', '۳. په لاندې جملو کې مرستندوي فعلونه وپېژنئ:')
S = [('(a) I threw Saleem down on the ground.', '(الف) میں نے سلیم کو زمین پر پٹخ دیا۔', '(الف) ما سلیم په ځمکه وغورځاوه.'), ('(b) Let him make his point clear.', '(ب) اُسے اپنی بات واضح کرنے دو۔', '(ب) پرېږده چې خپله خبره روښانه کړي.'),
     ('(c) The blind man suddenly fell into a pit.', '(ج) اندھا اچانک گڑھے میں گر پڑا۔', '(ج) ړوند ناڅاپه کندې ته ولوېد.'), ('(d) The whole homeland has woken up, comrades!', '(د) جاگ اُٹھا ہے سارا وطن ساتھیو!', '(د) ټول وطن راویښ شوی، ملګرو!'),
     ('(e) What I have heard cannot be told by me.', '(ہ) جو میں نے سنا ہے وہ مجھ سے بیان نہیں ہو سکتا۔', '(ه) څه چې ما اورېدلي، له ما نه شي بیانېدای.')]
e.group('lines', S)
e.p('4. Put diacritics (iʿrāb) on the following words.', '۴۔ درج ذیل الفاظ پر اِعراب لگائیں۔', '۴. پر لاندې کلمو اعراب کېږدئ.')
e.p('waṭaniyyat, mufakkir-e-islām, mutaṣarrif, taṣawwur-e-millat, taḥaffuẓ, barr-e-ʿaẓīm [Urdu words to be vowelled]', 'وطنیت، مفکرِ اسلام، متصرف، تصورِ ملت، تحفظ، برعظیم۔', 'وطنیت، مفکر اسلام، متصرف، تصور ملت، تحفظ، برعظیم [د اردو کلمې چې اعراب پرې کېښودل شي]')
for p in e.paras:
    pass
ex = BOOK.record(e, 'urdu12-u4-exercise', 'Exercise', 'مشق', 'تمرین', 20, [30, 31])
issues = [{'id': 'urdu12-pdf020', 'unit': 4, 'printedPage': 30, 'description': 'The Iqbal couplet is printed in a shaded box with a pen-and-inkpot ornament (not reproduced). Q2(e) prints the couplet on one line. Q3 sentences are Urdu grammar items; English/Pashto give their meaning for reference.'}]

if __name__ == '__main__':
    BOOK.save(20, [(4, tx), (4, ex)], issues=issues, complete_units=[4])
