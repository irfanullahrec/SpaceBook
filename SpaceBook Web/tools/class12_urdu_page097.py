"""Urdu XII PDF97 (spread): p.184 Lesson 17 مشق Q3(b)–Q8 (end); p.185 section title page 'حصۂ نظم' (poetry section)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
e = Builder()
e.group('lines', [
    ('(b) May this illness be ruined — the cup of life is spilling over even before it is full.', '(ب) اس بیماری کا خانہ خراب ہو۔ عمر کا پیمانہ لبریز ہونے سے پہلے ہی چھلکا جا رہا ہے۔', '(ب) د دې ناروغۍ کور دې وران شي — د عمر پیاله له ډکېدو مخکې تويېږي.'),
    ('(c) In the midst of battle, if he merely fell on him, the man would not even ask for water; without moving hand or foot he would suffocate and collapse on the spot.', '(ج) ہنگامِ قتال اگر وہ اس پر صرف گر پڑتے تو وہ پانی بھی نہ مانگتا۔ ہاتھ پاؤں مارے بغیر وہیں دم گھٹ کے ڈھیر ہو جاتا۔', '(ج) د جګړې پر مهال که هغه یوازې پرې پرېوتی، هغه به اوبه هم نه غوښتې؛ بې له لاس او پښو خوځولو به همدلته ساه بند او پرېوتی و.'),
])
e.p("4. Write a detailed note on the Khan Sahib's character.", '۴۔ خان صاحب کے کردار پر ایک مفصّل نوٹ لکھیں۔', '۴. د خان صاحب پر کرکټر یو مفصل یادښت ولیکئ.')
e.p("5. With reference to this essay, write a short note on Mushtaq Ahmad Yousufi's style of writing.", '۵۔ اس مضمون کے حوالے سے مشتاق احمد یوسفی کے طرزِ تحریر پر ایک مختصر نوٹ لکھیں۔', '۵. د دې مقالې په حواله د مشتاق احمد یوسفي د لیکنې پر سبک یو لنډ یادښت ولیکئ.')
e.p('6. Write five sentences containing the “adjectival” (waṣfī) type of subordinate clause.', '۶۔ تابع جملوں کی قسم ’’وصفی‘‘ پر مشتمل پانچ جملے لکھیں۔', '۶. د تابع جملو د "وصفي" ډول لرونکې پنځه جملې ولیکئ.')
e.p('7. Put diacritics on the following words according to the given meanings.', '۷۔ درج ذیل الفاظ پر دیے گئے معنی کے مطابق اعراب لگائیں۔', '۷. پر لاندې کلمو د ورکړل شویو ماناوو سره سم اعراب کېږدئ.')
H = (['Word', 'Meaning (1)', 'Meaning (2)'], ['لفظ', 'معنی (۱)', 'معنی (۲)'], ['کلمه', 'مانا (۱)', 'مانا (۲)'])
ur = [['بکری', 'مویشی', 'فروخت'], ['جلانا', 'آگ میں ڈالنا', 'تازگی دینا، زندہ کرنا'], ['جو', 'نہر', 'غلہ'], ['وتر', 'نماز', 'مثلث کا حصہ']]
en = [['bkry (بکری)', 'bakrī — goat (livestock)', 'bikrī — sale'], ['jlana (جلانا)', 'jalānā — to burn', 'jilānā — to revive, bring to life'], ['jw (جو)', 'jū — stream, canal', 'jau — barley (grain)'], ['wtr (وتر)', 'witr — the witr prayer', 'watar — hypotenuse/chord (part of a triangle)']]
ps = [['بکري', 'وزه (څاروی)', 'پلورنه'], ['جلانا', 'سوځول', 'تازه کول، ژوندي کول'], ['جو', 'ویاله', 'اوربشې (غله)'], ['وتر', 'د وتر لمونځ', 'د مثلث برخه (وتر)']]
e.table('urdu12-u17-iraab', H[0], en, H[1], H[2], ur, ps)
e.p('8. Use the following idioms in your own sentences.', '۸۔ درج ذیل محاورات اپنے جملوں میں استعمال کریں۔', '۸. لاندې محاورې په خپلو جملو کې وکاروئ.')
e.group('lines', [
    ('to sink into the ground (with shame)', 'زمین میں گڑ جانا', 'په ځمکه کې ښخېدل (له شرمه)'),
    ('the sky to fall (calamity to strike)', 'آسمان ٹوٹ پڑنا', 'اسمان راپرېوتل (ناڅاپي مصیبت)'),
    ('to build castles in the air', 'ہوائی قلعے بنانا', 'په هوا کې کلاګانې جوړول'),
    ('to be a lamp at dawn (near death / about to fade)', 'چراغِ سحر ہونا', 'د سهار څراغ کېدل (مرګ ته نږدې)'),
    ('to be faithless like a parrot (ungrateful)', 'طوطا چشمی کرنا', 'طوطا سترګي کول (بې‌وفايي)'),
    ('to knock brick against brick (to destroy utterly)', 'اینٹ سے اینٹ بجانا', 'خښته په خښته وهل (بشپړ ورانول)'),
    ('the intoxication to vanish', 'نشہ ہرن ہو جانا', 'نشه تښتېدل'),
    ('to make someone chew gram through the nose (to harass severely)', 'ناکوں چنے چبوانا', 'په پوزه نخود ژوول (سخت ځورول)'),
    ('a mountain to fall (great calamity)', 'پہاڑ ٹوٹ پڑنا', 'غر راپرېوتل (لویه مصیبت)'),
    ('to send three letters (to curse, scorn)', 'تین حرف بھیجنا', 'درې توري لېږل (لعنت ویل)'),
])
ex = BOOK.record(e, 'urdu12-u17-exercise-2', 'Exercise (2)', 'مشق (۲)', 'تمرین (۲)', 97, [184])

p = Builder()
p.h('Poetry section', 'حصۂ نظم', 'د نظم برخه')
p.p('Section title page (p.185): “Ḥiṣṣa-e Naẓm” — the poetry section of the book (poems 1–8), followed by the ghazal section (9–16).', 'عنوانی صفحہ (ص ۱۸۵): ’’حصۂ نظم‘‘ — کتاب کا نظموں کا حصہ (نظمیں ۱–۸)، جس کے بعد حصۂ غزل (۹–۱۶) ہے۔', 'سرلیک مخ (۱۸۵ مخ): "د نظم برخه" — د کتاب د نظمونو برخه (نظمونه ۱–۸)، چې وروسته یې د غزل برخه (۹–۱۶) راځي.')
UT = ('The Answer to the Complaint (Jawab-e-Shikwa)', 'جوابِ شکوہ', 'د شکوې ځواب', 'علامہ اقبالؒ')
sec = BOOK.record(p, 'urdu12-poetry-title', 'Poetry section (title page)', 'حصۂ نظم', 'د نظم برخه', 97, [185], unit_title=UT)
sec['sourceCoverIllustrationReview'] = 'Decorative blue eight-pointed frame around the calligraphic title “حصۂ نظم”; not reproduced.'
issues = [{'id': 'urdu12-pdf097', 'unit': 17, 'printedPage': 184, 'description': 'Lesson 17 exercise ends at Q8 (p.184). In the app the poems are units 18–25 (poem n = unit 17+n) and the ghazals units 26–33, following the printed contents; legacy poem units 18–22 (with mismatched titles) are superseded by source-authored records.'}]

if __name__ == '__main__':
    BOOK.save(97, [(17, ex), (18, sec)], issues=issues, complete_units=[17])
