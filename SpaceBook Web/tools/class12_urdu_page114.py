"""Urdu XII PDF114 (spread): pp.218–219 — Poem 8 'بڑے ڈرپوک ہو!' (Wazir Agha, d.2010 — copyrighted) summary."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
s = Builder()
s.h('You Are Such Cowards! — Wazir Agha', 'بڑے ڈرپوک ہو! — وزیرؔ آغا', 'ډېر ډارن یئ! — وزیر اغا')
s.p('[Summary — Wazir Agha (d. 2010) is in copyright; read the full free-verse poem in the printed textbook, pp. 218–219.]', '[خلاصہ — وزیرؔ آغا (وفات ۲۰۱۰ء) کا کلام کاپی رائٹ میں ہے؛ مکمل آزاد نظم درسی کتاب کے صفحات ۲۱۸–۲۱۹ میں پڑھیں۔]', '[لنډیز — د وزیر اغا (مړ ۲۰۱۰ز) کلام د کاپي‌رایټ لاندې دی؛ بشپړ ازاد نظم د درسي کتاب په ۲۱۸–۲۱۹ مخونو کې ولولئ.]')
for x in [
    ('The poet addresses the stars and teases them: they are great cowards, for they come out only at night.',
     'شاعر ستاروں سے مخاطب ہو کر انھیں چھیڑتا ہے کہ وہ بڑے ڈرپوک ہیں، کیونکہ صرف رات کو نکلتے ہیں۔',
     'شاعر ستورو ته مخ اړوي او ټوکې ورسره کوي چې ډېر ډارن دي، ځکه یوازې د شپې راوځي.'),
    ('Sometimes they slip in hidden beneath the veil of fragrant moonlight, wet with the motherly tenderness of tears; sometimes, like countless nails of light, they are driven into the body of darkness — neither living nor dying.',
     'کبھی وہ آنسوؤں کی بھیگی ممتا میں مہکتی چاندنی کی اوڑھنی میں چھپ کر آتے ہیں؛ کبھی روشنی کی ان گنت میخوں کی صورت تاریکی کے جسم میں پیوست ہوتے ہیں — نہ جیتے ہیں نہ مرتے ہیں۔',
     'کله د اوښکو په لانده مینه کې د معطرې سپوږمۍ تر څادر لاندې پټ راځي؛ کله د رڼا د بې‌شمېره مېخونو په څېر د تیارې په بدن کې ننوځي — نه ژوندي دي نه مړه.'),
    ('The stars have never seen how bright and how boundless the day is; they have never seen that other star — the sun — which comes out only by day.',
     'ستاروں نے کبھی نہیں دیکھا کہ دن کتنا منوّر اور کس قدر بے انت ہوتا ہے؛ انھوں نے وہ تارا (سورج) کبھی نہیں دیکھا جو فقط دن کو نکلتا ہے۔',
     'ستورو هېڅکله نه دي لیدلي چې ورځ څومره روښانه او بې‌پایه وي؛ هغه ستوری (لمر) یې هېڅکله نه دی لیدلی چې یوازې د ورځې راوځي.'),
    ('Armed with shining spears and holding a golden mace, that brave warrior passes alone across the arc of the horizon, fearlessly crossing the frontiers of grief and joy, until at last, amid the clamour of evening, he reaches his destination. And the poem closes by repeating: “You are such cowards, stars — you come out only at night!!”',
     'چمکتی برچھیوں سے لیس، ہاتھ میں سنہرا گرز لیے وہ بہادر سورما افق کی قوس سے تنہا گزرتا ہے، غم اور خوشی کی سرحدوں سے بے خطر بڑھتا چلا جاتا ہے اور آخر شام کے کہرام میں اپنی منزل پر جا پہنچتا ہے۔ نظم پھر یہی دہرا کر ختم ہوتی ہے کہ ’’بڑے ڈرپوک ہو تارو! فقط شب کو نکلتے ہو!!‘‘',
     'په ځلانده نېزو سمبال، په لاس کې د سرو زرو ګرز، هغه زړور اتل یوازې د افق له کږې تېرېږي، د غم او خوښۍ له پولو بې‌وېرې مخ ته ځي، او په پای کې د ماښام په شور ماشور کې خپل منزل ته رسېږي. نظم بیا همدا تکراروي: "ډېر ډارن یئ ستورو! یوازې د شپې راوځئ!!"'),
    ('(Auraq, August–September 1995)', '(اوراق۔ اگست، ستمبر ۱۹۹۵ء)', '(اوراق، اګست–سپتمبر ۱۹۹۵ز)'),
    ('*After slight alteration for curricular needs.', '*نصابی ضرورتوں کے تحت قدرے ترمیم کے بعد', '*د درسي اړتیاوو له مخې د لږ بدلون وروسته.'),
]: s.p(*x)
po = BOOK.record(s, 'urdu12-u25-poem', 'Poem — summary', 'نظم — خلاصہ', 'نظم — لنډیز', 114, [218, 219])
po['sourceGap'] = 'Wazir Agha (d. 2010) — in copyright; summary in the app, not verbatim. Printed pp. 218–219. Only the title/refrain is quoted. The board footnote (“adapted for curricular needs”) is transcribed.'
po['sourceCoverIllustrationReview'] = 'Portrait photograph of Wazir Agha (p.218) and floral border are decorative; not reproduced.'
UT = ('You Are Such Cowards (Bare Darpok Ho)', 'بڑے ڈرپوک ہو!', 'ډېر ډارن یئ!', 'وزیرؔ آغا')
po['unitTitle'] = UT[0]
issues = [{'id': 'urdu12-pdf114', 'unit': 25, 'printedPage': 218, 'description': 'Poem 8 has no separate author note in the poetry section (Wazir Agha’s note appears earlier with his prose lesson, unit 6); only a portrait is printed beside the title.'}]

if __name__ == '__main__':
    po.pop('unitTitle')
    rec = BOOK.record(s, 'urdu12-u25-poem', 'Poem — summary', 'نظم — خلاصہ', 'نظم — لنډیز', 114, [218, 219], unit_title=UT)
    rec.update({k: po[k] for k in ('sourceGap', 'sourceCoverIllustrationReview')})
    BOOK.save(114, [(25, rec)], issues=issues)
