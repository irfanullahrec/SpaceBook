"""Urdu XII PDF108 (spread): p.206 Poem 4 مشق Q1–Q3; p.207 Poem 5 author note (ن۔م۔ راشد, 1910–1975)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Give short answers to the following questions according to the poem.', '۱۔ نظم کے مطابق درج ذیل سوالات کے مختصر جوابات دیں۔', '۱. د نظم سره سم لاندې پوښتنو ته لنډ ځوابونه ورکړئ.')
e.group('lines', [
    ('(a) Write the central idea of this poem.', '(ا) اس نظم کا مرکزی خیال لکھیں۔', '(الف) د دې نظم مرکزي فکر ولیکئ.'),
    ("(b) Which longing of his heart does the poet mention?", '(ب) شاعر اپنے دل کی کس اُمنگ کا ذکر کرتا ہے؟', '(ب) شاعر د خپل زړه د کوم ارمان یادونه کوي؟'),
    ('(c) What is the wish expressed to bring down from the sky?', '(ج) آسمان سے کن کو لانے کی خواہش کا اظہار کیا گیا ہے؟', '(ج) له اسمانه د څه راوړلو هیله څرګنده شوې؟'),
    ('(d) Where is the new world (jahān-e nau) situated?', '(د) جہانِ نو کہاں واقع ہے؟', '(د) نوې نړۍ چېرته پرته ده؟'),
    ('(e) What kind of people are most people in the world?', '(ہ) دنیا میں زیادہ تر لوگ کس قسم کے ہیں؟', '(ه) په نړۍ کې ډېری خلک څه ډول دي؟'),
    ('(f) Why has the wish been expressed that the universe should become a single speck?', '(و) یہ خواہش کیوں کی گئی ہے کہ کائنات ایک ذرہ بن جائے؟', '(و) دا هیله ولې شوې چې کائنات دې یوه ذره شي؟'),
    ('(g) What stands in the way of changing the ways of Nature?', '(ز) قدرت کے طریقے بدلنے میں کیا چیز حائل ہے؟', '(ز) د قدرت د لارو په بدلولو کې کوم شی خنډ دی؟'),
    ('(h) What is meant by “a fakir of the line” (lakīr kā faqīr)?', '(ح) ’’لکیر کا فقیر‘‘ سے کیا مراد ہے؟', '(ح) "د کرښې فقیر" څه مانا لري؟'),
    ("(i) What is the reason for the tangle in the poet's self?", '(ط) شاعر کی ذات میں اُلجھاؤ کی کیا وجہ ہے؟', '(ط) د شاعر په ذات کې د ګډوډۍ لامل څه دی؟'),
    ('(j) Write a summary of this poem in your own words.', '(ی) اس نظم کا خلاصہ اپنے الفاظ میں تحریر کریں۔', '(ی) د دې نظم لنډیز په خپلو کلمو ولیکئ.'),
])
e.p('2. Explain:', '۲۔ تشریح کریں۔', '۲. تشریح کړئ:')
e.group('lines', [
    ('But yes — in spite of this, the blaze that is in my heart:', 'مگر ہاں باوجود اس کے مرے دل میں جو جوالا ہے', 'خو هو — سره له دې، زما په زړه کې چې کومه لمبه ده:'),
    ('longings have cast my being into a tangle.', 'اُمنگوں نے مری ہستی کو اک اُلجھن میں ڈالا ہے', 'ارمانونو زما هستي په یوه ګډوډۍ کې اچولې.'),
])
e.p('3. “Lakīr kā faqīr honā” (to be a fakir of the line — to follow blindly) is an idiom. Define the idiom (muhāwara) and write any five idioms.', '۳۔ ’’لکیر کا فقیر ہونا‘‘ محاورہ ہے۔ محاورہ کی تعریف کریں اور کوئی سے پانچ محاورات لکھیں۔', '۳. "د کرښې فقیر کېدل" (ړوند تقلید کول) محاوره ده. د محاورې تعریف وکړئ او هر پنځه محاورې ولیکئ.')
ex = BOOK.record(e, 'urdu12-u21-exercise', 'Exercise', 'مشق', 'تمرین', 108, [206])

a = Builder()
a.h('N. M. Rashid', 'ن۔م۔ راشدؔ', 'ن.م. راشد')
a.p('Born: 1910 · Died: 1975', 'ولادت: ۱۹۱۰ء · وفات: ۱۹۷۵ء', 'زېږېدنه: ۱۹۱۰ز · مړینه: ۱۹۷۵ز')
for x in [
    ("N. M. Rashid's real name was Raja Nazar Muhammad Janjua. He was born in the village of Kot Bhagan, Alipur Chattha (Gujranwala). After doing an M.A. in Economics from Government College Lahore he passed a long period of economic hardship. At last fate smiled on him and he joined the U.N.O. He worked in several countries; he spent the last part of his life abroad and died there. N. M. Rashid is a unique example of artistic and thematic departure from traditional Urdu poetry. He is a poet of hard and rough emotions. The prevailing traditional moulds of the naẓm were wholly unable to keep pace with his thought and art; so he emerged with a new colour.",
     'ن۔م۔ راشدؔ کا اصل نام راجا نذر محمد جنجوعہ تھا۔ وہ علی پور چٹھہ (گوجرانوالہ) کے گاؤں کوٹ بھاگاں میں پیدا ہوئے۔ گورنمنٹ کالج لاہور سے اقتصادیات میں ایم۔اے کرنے کے بعد اقتصادی بدحالی کا ایک طویل دور گزارا۔ بالآخر تقدیر اُن پر مہربان ہو گئی اور وہ یو۔این۔او سے منسلک ہو گئے۔ اُنھوں نے کئی ممالک میں کام کیا۔ عمر کا آخری حصہ بیرونِ ملک گزارا اور وہیں وفات پائی۔ ن۔م۔ راشدؔ اُردو کی روایتی شاعری سے فنی اور معنوی انحراف کی ایک انوکھی مثال ہیں۔ وہ سخت اور کھردرے جذبات کے شاعر ہیں۔ نظم کے مروّجہ روایتی سانچے اُن کے فکر و فن کا ساتھ دینے سے یکسر قاصر تھے۔ چنانچہ وہ ایک نیا رنگ لے کر اُبھرے۔',
     'د ن.م. راشد اصلي نوم راجا نذر محمد جنجوعه و. هغه د علي‌پور چټه (ګوجرانواله) په کوټ بهاګان کلي کې زېږېدلی. له ګورنمنټ کالج لاهور نه یې په اقتصاد کې ایم.اې وکړ او بیا یې د اقتصادي بدحالۍ اوږده دوره تېره کړه. په پای کې تقدیر ورباندې مهربانه شو او له ملګرو ملتونو سره وتړل شو. په ګڼو هېوادونو کې یې کار وکړ؛ د عمر وروستۍ برخه یې په بهر کې تېره کړه او همالته وفات شو. ن.م. راشد له دودیزې اردو شاعرۍ څخه د فني او معنوي انحراف یوه بې‌ساري بېلګه ده. هغه د سختو او زیږو احساساتو شاعر دی. د نظم دودیزو چوکاټونو د هغه د فکر او هنر ملګرتیا نه شوه کولی؛ نو هغه له یوه نوي رنګ سره راڅرګند شو.'),
    ("Rashid is among the first architects of the modern Urdu naẓm. His creative mind did not accept the prevailing moulds of the naẓm. He made many experiments in form; though the form and technique of his poems are new and strange to the reader of the Urdu naẓm, he also kept in view the classical style of the language. He devised a system of rhymes that appears to be the inner need of the poems. By the time of Iqbal several artistic and intellectual changes had taken place in the Urdu naẓm, but on the whole it was something simple and easily understood. Rashid's poems, by contrast, carry complexity and ambiguity. His naẓm is not simple and narrative; rather his poems have a dramatic and fictional manner. Besides this he made good use of symbolism, so that it often becomes difficult for the reader to reach the depth of meaning of his poems. Several critics hold that he is a poet not of today but of tomorrow.",
     'راشدؔ جدید اُردو نظم کے اوّلین معماروں میں سے ہیں۔ اُن کے تخلیقی ذہن نے نظم کے مروّجہ سانچوں کو قبول نہیں کیا۔ اُنھوں نے نظم میں ہیئت کے متعدد تجربے کیے، اگرچہ اُن کی نظموں کی ہیئت اور تکنیک اُردو نظم کے قاری کے لیے نئی اور انوکھی چیز ہے، لیکن اُنھوں نے زبان کے کلاسیکی اسلوب کو بھی مدِنظر رکھا۔ اُنھوں نے قوافی کا ایک ایسا نظام مرتب کیا جو نظموں کی داخلی ضرورت نظر آتی ہے۔ اقبالؒ کے عہد تک پہنچتے پہنچتے اُردو نظم میں کئی ایک فنی و فکری تبدیلیاں رونما ہو چکی تھیں لیکن بہرحال اُردو نظم سیدھی سادی اور آسانی سے سمجھ میں آنے والی چیز تھی۔ راشدؔ کی نظمیں اس کے برعکس پیچیدگی اور ابہام لیے ہوئے ہیں۔ اُن کی نظم سادہ اور بیانیہ نہیں ہے بلکہ اُن کی نظموں میں ڈرامائی اور افسانوی انداز ہے۔ اس کے علاوہ اُنھوں نے علامت نگاری سے بھی خوب کام لیا، اس لیے اکثر اوقات قاری کے لیے اُن کی نظموں کے معنی اور مفہوم کی تہہ تک پہنچنا مشکل ہو جاتا ہے۔ اُن کے بارے میں کئی ایک نقادوں کا خیال ہے کہ وہ آج کے نہیں بلکہ آنے والے کل کے شاعر ہیں۔',
     'راشد د نوي اردو نظم له لومړنیو معمارانو څخه دی. د هغه پنځګر ذهن د نظم دودیز چوکاټونه ونه منل. هغه په نظم کې د بڼې ګڼې تجربې وکړې؛ که څه هم د هغه د نظمونو بڼه او تخنیک د اردو نظم لوستونکي ته نوی او عجیب شی دی، خو هغه د ژبې کلاسیک سبک هم په پام کې ونیو. هغه د قافیو داسې نظام جوړ کړ چې د نظمونو داخلي اړتیا ښکاري. د اقبال تر وخته په اردو نظم کې ګڼ فني او فکري بدلونونه راغلي وو، خو بیا هم اردو نظم ساده او په اسانۍ د پوهېدو وړ شی و. د راشد نظمونه برعکس پېچلتیا او ابهام لري. د هغه نظم ساده او بیانیه نه دی، بلکې په نظمونو کې یې ډرامايي او کیسه‌ییز انداز دی. سربېره پر دې یې له سمبولیزم څخه هم ښه کار اخیستی، نو ډېری وخت لوستونکي ته د هغه د نظمونو د مانا تل ته رسېدل ګران شي. د ګڼو نقادانو نظر دا دی چې هغه د نن نه، بلکې د راتلونکي سبا شاعر دی.'),
    ('Collections of poetry: Mavra, Iran mein Ajnabi, La=Insaan, Guman ka Mumkin.', 'مجموعہ ہائے کلام: ماورا، ایران میں اجنبی، لا = انسان، گماں کا ممکن۔', 'د کلام ټولګې: ماورا، په ایران کې پردی، لا=انسان، د ګومان ممکن.'),
]: a.p(*x)
UT = ('Stars (Sitare)', 'ستارے', 'ستوري', 'ن۔م۔ راشدؔ')
au = BOOK.record(a, 'urdu12-u22-author', 'About the poet: N. M. Rashid', 'ن۔م۔ راشدؔ (تعارف)', 'ن.م. راشد (پېژندنه)', 108, [207], unit_title=UT)
au['sourceCoverIllustrationReview'] = 'Portrait photograph of N. M. Rashid and floral border are decorative; not reproduced.'
issues = [{'id': 'urdu12-pdf108', 'unit': 22, 'printedPage': 207, 'description': 'N. M. Rashid died 1975; under Pakistani copyright (50 years from the year following death) his work entered the public domain on 1 Jan 2026, so Poem 5 will be transcribed in full. Exercise Q2 on p.206 prints “مرے دل میں جو جوالا ہے” where the poem (p.205) has “مرے دل میں جُوالا ہے” — retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(108, [(21, ex), (22, au)], issues=issues, complete_units=[21])
