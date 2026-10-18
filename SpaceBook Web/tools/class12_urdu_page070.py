"""Urdu XII PDF70 (spread): printed pp.130–131 — Lesson 13 text end (source مضامینِ فرحت) and مشق Q1–Q3."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
t = Builder()
for x in [
    ('…the result is that college lads write essays that great writers could not even dream of.',
     '…ہیں، اسی کا نتیجہ ہے کہ کالج کے لونڈے وہ مضمون لکھ جاتے ہیں، جو بڑے بڑے اہلِ قلم کے حاشیۂ خیال میں بھی نہیں آتے۔',
     '…دي، د همدې پایله ده چې د کالج هلکان داسې مقالې لیکي چې لوی لوی لیکوالو یې په خیال کې هم نه راځي.'),
    ('With the Maulvi Sahib’s death a pillar of the Urdu language fell, and such a pillar that, far from building another like it, it is hard even to prop up that part. A search is on for another professor to fill his place, but let the authorities of Osmania University note that, though they sift Hindustan from end to end, finding a professor like Maulvi Waheeduddin Saleem is a great thing; if even someone a fraction of his worth is found, count it a blessing, a great blessing.',
     'مولوی صاحب کیا مرے، زبانِ اردو کا ایک ستون گر گیا اور ایسا ستون گرا کہ اس جیسا بننا تو کجا، اس حصے میں اڑ واڑ بھی لگانی مشکل ہے۔ ان کی جگہ بھرنے کے لیے دوسرے پروفیسر کی تلاش ہو رہی ہے، مگر عثمانیہ یونیورسٹی کے اربابِ حل و عقد لکھ رکھیں کہ چاہے اِس سرے سے اُس سرے تک ہندوستان چھان مارو، مولوی وحید الدین سلیم جیسا پروفیسر ملنا تو بڑی بات ہے، ان کا پاسنگ بھی مل جائے، تو غنیمت اور بہت غنیمت سمجھو۔',
     'مولوي صاحب څه مړ شو، د اردو ژبې یوه ستنه ولوېده، او داسې ستنه ولوېده چې د هغې په څېر جوړول خو لا څه، هغه برخې ته ټیکه ورکول هم ګران دي. د هغه د ځای ډکولو لپاره د بل پروفیسر لټون روان دی، خو د عثمانیه پوهنتون واکمن دې ولیکي چې که د هندوستان له یوه سره تر بل سره پورې هم وچاڼئ، د مولوي وحیدالدین سلیم په څېر پروفیسر موندل خو لویه خبره ده؛ که د هغه یوه کوچنۍ برخه هم پیدا شي، غنیمت او ډېر غنیمت یې وګڼئ.'),
    ('(Mazameen-e-Farhat)', '(مضامینِ فرحت)', '(مضامین فرحت)'),
]: t.p(*x)
tx = BOOK.record(t, 'urdu12-u13-text-6', 'Lesson text (6)', 'متنِ سبق (۶)', 'د لوست متن (۶)', 70, [130])

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Write answers to the following questions.', '۱۔ درج ذیل سوالات کے جوابات لکھیں۔', '۱. لاندې پوښتنو ته ځوابونه ولیکئ.')
e.group('lines', [
    ('(a) When and how did the Maulvi Sahib and Farhatullah Baig meet?', '(الف) مولوی صاحب اور فرحت اللہ بیگ کی ملاقات کب اور کیسے ہوئی؟', '(الف) د مولوي صاحب او فرحت الله بیګ لیدنه کله او څنګه وشوه؟'),
    ("(b) Describe the Maulvi Sahib's appearance in your own words.", '(ب) مولوی صاحب کا حلیہ اپنے الفاظ میں بیان کریں؟', '(ب) د مولوي صاحب بڼه په خپلو کلمو بیان کړئ؟'),
    ("(c) What views did Farhat express about the Maulvi Sahib's temperament?", '(ج) فرحت نے مولوی صاحب کے مزاج کے بارے میں کن خیالات کا اظہار کیا؟', '(ج) فرحت د مولوي صاحب د مزاج په اړه کوم نظرونه څرګند کړل؟'),
    ('(d) What misunderstanding arose at the annual function of the Hyderabad college?', '(د) حیدر آباد کالج کے سالانہ جلسے میں کیا غلط فہمی پیدا ہوئی؟', '(د) د حیدراباد کالج په کلنۍ غونډه کې کومه غلط‌فهمي پیدا شوه؟'),
    ('(e) What excuse did the Maulvi Sahib give for his thrift?', '(ہ) مولوی صاحب اپنی کفایت شعاری کے بارے میں کیا عذر پیش کیا کرتے تھے؟', '(ه) مولوي صاحب به د خپلې سپما په اړه کوم عذر وړاندې کاوه؟'),
    ('(f) Explain this sentence: “and the Maulvi Sahib would fall out with someone or other.”', '(و) ’’اور مولوی صاحب کی کسی نہ کسی سے بگڑ جاتی‘‘ اس جملے کی وضاحت کریں؟', '(و) "او د مولوي صاحب به له یو نه یو سره خبره خرابه شوه" — دا جمله تشریح کړئ؟'),
    ('(g) What principles did the Maulvi Sahib rely on to coin technical terms?', '(ز) مولوی صاحب نے اصطلاحات وضع کرنے کے لیے کن اصولوں کا سہارا لیا؟', '(ز) مولوي صاحب د اصطلاحاتو د جوړولو لپاره پر کومو اصولو تکیه وکړه؟'),
])
e.p('2. Explain the following sentences.', '۲۔ درج ذیل جملوں کی وضاحت کریں۔', '۲. لاندې جملې تشریح کړئ.')
e.group('lines', [
    ('(a) Before the oil runs out the lamp flickers and trembles, the flame begins to sink and at last slowly goes cold. Now, in place of the lamp, life has become an electric lamp: here you press the button, there it is pitch dark.', '(الف) تیل ختم ہونے سے پہلے چراغ جھلملاتا، ٹمٹماتا، لو بیٹھنی شروع ہوتی اور آخر رفتہ رفتہ ٹھنڈا ہو جاتا ہے۔ اب چراغ کی جگہ زندگی بجلی کا لیمپ ہو گئی ہے۔ ادھر بٹن دبایا، ادھر گھپ اندھیرا۔', '(الف) د تېلو له خلاصېدو مخکې څراغ رپېږي، ځلېږي، لمبه یې ټیټېږي او په پای کې ورو ورو یخېږي. اوس د څراغ پر ځای ژوند برېښنايي څراغ شوی؛ دلته تڼۍ کېکاږې، هلته سخته تیاره.'),
    ('(b) But when does my tongue stop! I said: “Maulvi Sahib! Why are you worried? In the name of God, go ahead and die; I will write it in an essay.”', '(ب) مگر میری زبان کب رُکتی ہے۔ میں نے کہا: ’’مولوی صاحب! گھبراتے کیوں ہیں، بسم اللہ کیجیے، مر جائیے، مضمون میں لکھ دوں گا‘‘', '(ب) خو زما ژبه کله درېږي! ما وویل: "مولوي صاحب! ولې وارخطا کېږئ؟ بسم الله کړئ، مړ شئ، مقاله به زه ولیکم."'),
    ('(c) The tongue was his own; he did not know how to defer to anyone; he would cool his heart by giving people a piece of his mind.', '(ج) زبان اپنی تھی، کسی کا دینا نہیں آتا تھا، بے نقط سُنا کر دل ٹھنڈا کر لیتے تھے۔', '(ج) ژبه یې خپله وه، د چا پور یې نه ورکاوه، په سختو خبرو به یې زړه یخاوه.'),
    ('(d) Fearing drought, he kept filling his coffers in times of plenty.', '(د) خشک سالی کے اندیشے سے ارزانی کے زمانے میں کھتے بھرنے کی فکر میں رہے۔', '(د) د وچکالۍ له وېرې یې د ارزانۍ په وخت کې د زېرمو د ډکولو فکر کاوه.'),
    ('(e) The wider his vision grew, the narrower his heart became.', '(ہ) جتنی اُن کی نگاہ وسیع ہوئی، اتنا ہی اُن کا دل تنگ ہوا۔', '(ه) څومره چې یې نظر پراخ شو، هومره یې زړه تنګ شو.'),
])
e.p('3. Fill in the blanks with suitable words:', '۳۔ خالی جگہ مناسب الفاظ سے پُر کریں:', '۳. تش ځایونه په مناسبو کلمو ډک کړئ:')
e.group('lines', [
    ('(a) He stepped out of the ranks and became the victim of the arrow of ________ .', '(الف) صف سے آگے بڑھا اور تیر ________ کا شکار ہوا۔', '(الف) له لیکې مخکې شو او د ________ د غشي ښکار شو.'),
    ('(b) An old man is coming towards me taking long ________ .', '(ب) ایک بڑے میاں بڑے بڑے ________ بھرتے میری طرف آ رہے ہیں۔', '(ب) یو زوړ سړی په لویو لویو ________ ماته راځي.'),
    ('(c) Everyone praised his quick ________ .', '(ج) اُن کی زود ________ کی سب تعریف کرتے تھے۔', '(ج) ټولو یې د چټک ________ ستاینه کوله.'),
    ('(d) Men of merit have always remained in ________ circumstances.', '(د) اہلِ کمال ہمیشہ ________ حال رہے ہیں۔', '(د) باکماله خلک تل ________ حال پاتې شوي.'),
    ('(e) I drew a picture of the Delhi of that ________ .', '(ہ) میں نے اُس ________ کی دلّی کا نقشہ کھینچا۔', '(ه) ما د هغه ________ د ډهلي انځور وکېښ.'),
    ('(f) God gives the sugar-eater ________ .', '(و) خُدا شکر خورے کو ________ دیتا ہے۔', '(و) خدای بوره‌خوړونکي ته ________ ورکوي.'),
])
ex = BOOK.record(e, 'urdu12-u13-exercise-1', 'Exercise (1)', 'مشق (۱)', 'تمرین (۱)', 70, [130, 131])
issues = [{'id': 'urdu12-pdf070', 'unit': 13, 'printedPage': 130, 'description': 'Q1(d) says the misunderstanding arose at the “Hyderabad college” function; in the text the function was at Aurangabad — retained as printed. Q2(a) prints “تیل ختم ہونے سے پہلے” (text: “تیل ختم ہونے کے بعد”).'}]

if __name__ == '__main__':
    BOOK.save(70, [(13, tx), (13, ex)], issues=issues)
