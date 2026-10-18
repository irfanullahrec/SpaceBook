"""Urdu XII PDF125 (spread): p.240 Ghazal 15 (Zafar Iqbal — copyrighted) couplets 6–9 summary; p.241 مشق Q1–Q5."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
s = Builder()
for x in [
    ('6. Our capacity (of heart) is not so very large either, yet even when a grievance arose, we did not complain.',
     '۶۔ اپنا ظرف بھی اتنا کشادہ نہیں، لیکن شکایت پیدا بھی ہوئی تو ہم نے شکایت نہیں کی۔',
     '۶. زموږ ظرف هم دومره پراخ نه دی، خو که ګیله پیدا هم شوه، موږ ګیله ونه کړه.'),
    ('7. It is also true that we never became your supplicants — and you, too, never showed any favour.',
     '۷۔ یہ بھی سچ ہے کہ ہم تیرے سوالی نہ ہوئے، اور تُو نے بھی کبھی کوئی عنایت نہیں کی۔',
     '۷. دا هم رښتیا ده چې موږ ستا سوالګر نه شوو، او تا هم کله کومه مهرباني ونه کړه.'),
    ('8. Whatever is happening here was bound to happen this way; that is why we have not been surprised at anything.',
     '۸۔ جو یہاں ہو رہا ہے وہ اسی طرح ہونا تھا، اس لیے ہم نے کسی بات پر حیرت نہیں کی۔',
     '۸. څه چې دلته کېږي، باید همداسې شوي وای؛ ځکه موږ پر هېڅ خبره حیرانتیا ونه کړه.'),
    ('9. (Maqṭaʿ) O Zafar, what we were granted was itself more than enough; for what we never got, we never felt any longing.',
     '۹۔ (مقطع) اے ظفرؔ! جو میسر ہوا وہ بھی زیادہ تھا؛ جو ملا ہی نہیں، اس کی کبھی حسرت نہیں کی۔',
     '۹. (مقطع) اې ظفره! څه چې په برخه شول، هغه هم زیات وو؛ څه چې ونه موندل، د هغو ارمان مو هېڅکله ونه کړ.'),
    ('(Tashkeel)', '(تشکیل)', '(تشکیل)'),
]: s.p(*x)
po = BOOK.record(s, 'urdu12-u32-ghazal-2', 'Ghazal — couplet-wise summary (2)', 'غزل — شعر وار خلاصہ (۲)', 'غزل — بیت په بیت لنډیز (۲)', 125, [240])
po['sourceGap'] = 'Zafar Iqbal (living) — in copyright; couplet-wise summary in the app, not verbatim. Printed p. 240 (couplets 6–9).'

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.group('lines', [
    ('1. Explain the opening (maṭlaʿ) and closing (maqṭaʿ) couplets of this ghazal.', '۱۔ اس غزل کے مطلع اور مقطع کی تشریح کریں۔', '۱. د دې غزل مطلع او مقطع تشریح کړئ.'),
    ('2. In which couplet of this ghazal has the figure murāʿāt-un-naẓīr been used?', '۲۔ اس غزل کے کس شعر میں صنعتِ مراعاۃ النظیر کا استعمال کیا گیا ہے؟', '۲. د دې غزل په کوم بیت کې د مراعات النظیر صنعت کارول شوی؟'),
    ('3. Put diacritics on the following words: shirākat, dasht, sulūk, muyassar.', '۳۔ درج ذیل الفاظ پر اعراب لگائیں: شراکت، دشت، سلوک، میسر۔', '۳. پر لاندې کلمو اعراب کېږدئ: شراکت، دښت، سلوک، میسر.'),
    ('4. Explain the following couplets (couplets 6 and 8 of the ghazal, beginning “Ẓarf itnā bhī kushāda nahīṉ apnā…” and “Ho rahā hai jo, isī ṭaraḥ se honā thā yahāṉ…”).', '۴۔ درج ذیل اشعار کی تشریح کریں: ’’ظرف اتنا بھی کشادہ نہیں اپنا، لیکن / ہم نے پیدا بھی ہوئی ہے تو شکایت نہیں کی‘‘ ’’ہو رہا ہے جو، اسی طرح سے ہونا تھا یہاں / اس لیے ہم نے کسی بات پہ حیرت نہیں کی‘‘', '۴. لاندې بیتونه تشریح کړئ (د غزل ۶م او ۸م بیت).'),
    ('5. According to the given ghazal, put (✓) against the correct sentence and (✗) against the wrong one.', '۵۔ دی گئی غزل کے مطابق درست جملے کے سامنے (✓) کا نشان اور غلط کے سامنے (✗) کا نشان لگائیں۔', '۵. د ورکړل شوي غزل سره سم سمې جملې ته (✓) او ناسمې ته (✗) نښه کېږدئ.'),
    ("(a) The poet does not share in the beloved's dreams.", '(ا) شاعر محبوب کے خوابوں میں حصے دار نہیں ہوتا۔', '(الف) شاعر د محبوب په خوبونو کې شریک نه دی.'),
    ("(b) The poet has gone wild because of the beloved's cruelties.", '(ب) محبوب کی جفاؤں سے شاعر وحشت زدہ ہو گیا۔', '(ب) د محبوب له ظلمونو شاعر لېونی شو.'),
    ('(c) The poet took revenge for the faithlessness.', '(ج) شاعر نے بے وفائی کا بدلہ لیا۔', '(ج) شاعر د بې‌وفايۍ غچ واخیست.'),
    ('(d) The poet deliberately did not side with the beloved.', '(د) شاعر نے جان بوجھ کر محبوب کا ساتھ نہیں دیا۔', '(د) شاعر قصداً د محبوب ملاتړ ونه کړ.'),
    ('(e) The poet does not like asking (begging).', '(ہ) سوال کرنا شاعر کو اچھا نہیں لگتا۔', '(ه) شاعر ته سوال کول ښه نه ښکاري.'),
    ("(f) The poet is extremely surprised at the beloved's behaviour.", '(و) شاعر کو محبوب کے رویے پر بے حد حیرت ہے۔', '(و) شاعر د محبوب پر چلند ډېر حیران دی.'),
    ("(g) The poet's capacity is immensely vast.", '(ز) شاعر کا ظرف بے پناہ وسیع ہے۔', '(ز) د شاعر ظرف بې‌حده پراخ دی.'),
    ('(h) The poet does not ask in order to fulfil his wish.', '(ح) شاعر اپنی خواہش کی تکمیل کے لیے سوال نہیں کرتا۔', '(ح) شاعر د خپلې هیلې د پوره کولو لپاره سوال نه کوي.'),
    ('(i) “Union with the beloved” is the poet’s longing.', '(ط) ’’وصالِ یار‘‘ شاعر کی حسرت ہے۔', '(ط) "د یار وصال" د شاعر ارمان دی.'),
    ('(j) Despite wishing, the poet could not muster courage.', '(ی) چاہت کے باوجود شاعر ہمت نہ کر سکا۔', '(ی) سره له غوښتنې شاعر همت ونه کړای شو.'),
])
ex = BOOK.record(e, 'urdu12-u32-exercise', 'Exercise', 'مشق', 'تمرین', 125, [241])
issues = [{'id': 'urdu12-pdf125', 'unit': 32, 'printedPage': 241, 'description': 'Exercise Q4 quotes two couplets of the (copyrighted) ghazal as part of the board-written exercise; reproduced as short quotations only.'}]

if __name__ == '__main__':
    BOOK.save(125, [(32, po), (32, ex)], issues=issues, complete_units=[32])
