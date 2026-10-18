"""Urdu XII PDF123 (spread): p.236 Ghazal 14 (Ahmad Faraz, d.2008 — copyrighted) couplet-wise summary; p.237 مشق Q1–Q5."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
s = Builder()
s.h('Ghazal — Ahmad Faraz', 'غزل — احمد فرازؔ', 'غزل — احمد فراز')
s.p('[Couplet-wise summary — Ahmad Faraz (d. 2008) is in copyright; read the full ghazal (eight couplets, refrain “… ko kyā bolnā hai”) in the printed textbook, p. 236.]', '[شعر وار خلاصہ — احمد فرازؔ (وفات ۲۰۰۸ء) کا کلام کاپی رائٹ میں ہے؛ مکمل غزل (آٹھ اشعار، ردیف ’’کو کیا بولنا ہے‘‘) درسی کتاب کے صفحہ ۲۳۶ پر پڑھیں۔]', '[بیت په بیت لنډیز — د احمد فراز (مړ ۲۰۰۸ز) کلام د کاپي‌رایټ لاندې دی؛ بشپړ غزل (اته بیتونه، ردیف "… ته څه ویل دي") د درسي کتاب په ۲۳۶ مخ کې ولولئ.]')
for x in [
    ('1. The people have now opened their lips — what is left for the government to say? Now blood will speak; what is left for the sword to say?',
     '۱۔ اب لوگ لب کشا ہیں، سرکار کو کیا کہنا رہ گیا؟ اب لہو بولے گا، تلوار کو کیا کہنا ہے؟',
     '۱. خلکو اوس خوله پرانیستې — سرکار ته څه ویل پاتې دي؟ اوس به وینه خبرې کوي؛ تورې ته څه ویل پاتې دي؟'),
    ('2. In a fair where each seller outdoes the other in selling himself, what has the buyer to say?',
     '۲۔ جس میلے میں بکنے والوں میں ہر ایک دوسرے سے آگے ہو، وہاں خریدار کو کیا کہنا ہے؟',
     '۲. په داسې مېله کې چې د پلورل کېدونکو هر یو له بل نه مخکې وي، پېرودونکي ته څه ویل دي؟'),
    ('3. So the witnesses have come to court — and I already know which friend is to say what.',
     '۳۔ لو، عدالت میں گواہی دینے والے آ گئے؛ مجھے معلوم ہے کس یار نے کیا کہنا ہے۔',
     '۳. ګوره، محکمې ته شاهدان راغلل؛ زه پوهېږم چې کوم یار به څه وايي.'),
    ('4. The wind may listen for a while longer; then what will the lamp on the wall have to say?',
     '۴۔ ہوا کچھ دیر اور کان لگائے رہے، پھر دیوار پر رکھے چراغ کو کیا کہنا ہے؟',
     '۴. باد به یو څه نور غوږ ونیسي، بیا د دیوال پر سر څراغ ته څه ویل دي؟'),
    ('5. Why ask me my last wish? What has a sinner at the gallows to say?',
     '۵۔ مجھ سے آخری خواہش کیا پوچھتے ہو؟ ایک گنہگار سرِ دار کو کیا کہنا ہے؟',
     '۵. له ما وروستۍ هیله ولې پوښتئ؟ د دار پر سر یو ګناهګار ته څه ویل دي؟'),
    ('6. After the king’s decree the people of the city fell silent; now what has the knower of secrets to say?',
     '۶۔ شاہ کے فرمان کے بعد خلقتِ شہر چپ تھی؛ اب کسی واقفِ اسرار کو کیا کہنا ہے؟',
     '۶. د پاچا له فرمان وروسته د ښار خلک چوپ وو؛ اوس د رازونو پوه ته څه ویل دي؟'),
    ('7. Only the showman behind the curtain knows when, where and which character is to say what.',
     '۷۔ صرف پسِ پردہ تماشا گر ہی جانتا ہے کہ کب، کہاں اور کون سے کردار کو کیا کہنا ہے۔',
     '۷. یوازې د پردې شا ننداره‌ګر پوهېږي چې کله، چېرته او کوم کرکټر ته څه ویل دي.'),
    ('8. (Maqṭaʿ) O Faraz, where there are kings’ courts and courtiers, what has a partisan of Ghalib to say there?',
     '۸۔ (مقطع) اے فرازؔ! جہاں شاہوں کے دربار اور مصاحب ہوں، وہاں غالبؔ کے طرف دار کو کیا کہنا ہے؟',
     '۸. (مقطع) اې فرازه! چېرې چې د پاچاهانو دربارونه او درباریان وي، هلته د غالب طرفدار ته څه ویل دي؟'),
    ('(Ae Ishq-e-Junoon Pesha)', '(اے عشقِ جنوں پیشہ)', '(اې عشق جنون‌پېشه)'),
]: s.p(*x)
po = BOOK.record(s, 'urdu12-u31-ghazal', 'Ghazal — couplet-wise summary', 'غزل — شعر وار خلاصہ', 'غزل — بیت په بیت لنډیز', 123, [236])
po['sourceGap'] = 'Ahmad Faraz (d. 2008) — in copyright; couplet-wise summary in the app, not verbatim. Printed p. 236 (8 couplets).'

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.group('lines', [
    ('1. Write answers to the following questions according to the given ghazal:', '۱۔ دی گئی غزل کے مطابق درج ذیل سوالات کے جوابات لکھیں:', '۱. د ورکړل شوي غزل سره سم لاندې پوښتنو ته ځوابونه ولیکئ:'),
    ('(a) What is meant by “now blood will speak”?', '(ا) ’’اَب لہو بولے گا‘‘ سے کیا مراد ہے؟', '(الف) "اوس به وینه خبرې کوي" مطلب څه دی؟'),
    ('(b) What is meant by the wind “listening” (gosh-bar-āwāz)?', '(ب) ہوا کے گوش برآواز سے کیا مراد لی گئی ہے؟', '(ب) د باد د "غوږ نیولو" مطلب څه دی؟'),
    ('(c) Why were the people of the city silent?', '(ج) خلقتِ شہر کیوں چپ تھی؟', '(ج) د ښار خلک ولې چوپ وو؟'),
    ('(d) Why did the poet not tell his last wish?', '(د) شاعر نے آخری خواہش کیوں نہ بتائی؟', '(د) شاعر وروستۍ هیله ولې ونه ښوده؟'),
    ('2. Write the refrain (radīf) of this ghazal.', '۲۔ اس غزل کی ردیف لکھیں۔', '۲. د دې غزل ردیف ولیکئ.'),
    ('3. Write the rhymes of this ghazal.', '۳۔ اس غزل کے قوافی لکھیں۔', '۳. د دې غزل قافیې ولیکئ.'),
    ('4. In the couplet “Bikne wāloṉ meṉ jahāṉ ek se ek āge ho / aise mele meṉ kharīdār ko kyā bolnā hai”: mentioning something in a text and then bringing in other things related to it — provided they are not opposites — is called murāʿāt-un-naẓīr. In the couplet above, a fair and a buyer are mentioned in keeping with selling. Write at least three couplets in which the figure murāʿāt-un-naẓīr is used.', '۴۔ ’’بکنے والوں میں جہاں ایک سے ایک آگے ہو / ایسے میلے میں خریدار کو کیا بولنا ہے‘‘ — کلام میں کسی چیز کا ذکر کرنا اور پھر اُس کی مناسبت سے دوسری چیزیں لانا بشرطیکہ یہ چیزیں متضاد نہ ہوں مراعاۃ النظیر کہلاتا ہے۔ جیسے مندرجہ بالا شعر میں بِکنے کی مناسبت سے میلے اور خریدار کا ذکر کیا گیا ہے۔ کم از کم تین ایسے اشعار لکھیں جن میں صنعتِ مراعاۃ النظیر کا استعمال ہو۔', '۴. په بیت "د پلورل کېدونکو په منځ کې چې هر یو له بل مخکې وي / په داسې مېله کې پېرودونکي ته څه ویل دي" کې: په کلام کې د یوه شي یادونه او بیا د هغه په مناسبت د نورو شیانو راوړل، په دې شرط چې متضاد نه وي، "مراعات النظیر" بلل کېږي. لکه په پورتني بیت کې د پلورلو په مناسبت د مېلې او پېرودونکي یادونه شوې. لږ تر لږه درې داسې بیتونه ولیکئ چې پکې د مراعات النظیر صنعت کارول شوی وي.'),
    ('5. Explain the following couplet (the maqṭaʿ: “Jahāṉ darbār hoṉ shāhoṉ ke muṣāḥib hoṉ Farāz / wahāṉ Ghālib ke ṭaraf-dār ko kyā bolnā hai”).', '۵۔ درج ذیل شعر کی تشریح کریں: ’’جہاں دربار ہوں شاہوں کے مصاحب ہوں فرازؔ / وہاں غالبؔ کے طرف دار کو کیا بولنا ہے‘‘', '۵. لاندې بیت تشریح کړئ (مقطع: "چېرې چې د پاچاهانو دربارونه او درباریان وي، فرازه / هلته د غالب طرفدار ته څه ویل دي").'),
])
ex = BOOK.record(e, 'urdu12-u31-exercise', 'Exercise', 'مشق', 'تمرین', 123, [237])
issues = [{'id': 'urdu12-pdf123', 'unit': 31, 'printedPage': 237, 'description': 'Exercise Q4–Q5 quote two couplets of the (copyrighted) ghazal as part of the board-written exercise; reproduced as short quotations only.'}]

if __name__ == '__main__':
    BOOK.save(123, [(31, po), (31, ex)], issues=issues, complete_units=[31])
