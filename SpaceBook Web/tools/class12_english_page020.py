"""PDF20 (printed 27–28): 'The Solitary Reaper' (William Wordsworth, 1807 — public domain) full text; About the poet; Glossary; Reading Comprehension Q1–2."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
p = Builder()
p.h('Solitary Reaper', 'تنہا فصل کاٹنے والی', 'یوازینۍ لوګړه')
ST = [
    [('Behold her, single in the field,', 'اسے دیکھو، کھیت میں اکیلی،', 'هغې ته وګوره، په پټي کې یوازې،'),
     ('Yon solitary Highland Lass!', 'وہ پہاڑی علاقے کی تنہا لڑکی!', 'هغه د غرنۍ سیمې یوازینۍ نجلۍ!'),
     ('Reaping and singing by herself;', 'اکیلی فصل کاٹتی اور گاتی ہوئی؛', 'یوازې لو کوي او سندرې وايي؛'),
     ('Stop here, or gently pass!', 'یہاں رک جاؤ، یا آہستگی سے گزر جاؤ!', 'دلته ودرېږه، یا ورو تېر شه!'),
     ('Alone she cuts and binds the grain,', 'اکیلی وہ اناج کاٹتی اور باندھتی ہے،', 'یوازې غله رېبي او ګېډۍ کوي،'),
     ('And sings a melancholy strain;', 'اور ایک اداس دھن گاتی ہے؛', 'او یوه غمجنه نغمه وايي؛'),
     ('O listen! for the Vale profound', 'اے سنو! کیونکہ گہری وادی', 'ای واوره! ځکه ژوره دره'),
     ('Is overflowing with the sound.', 'اس آواز سے لبریز ہو رہی ہے۔', 'له دې غږه ډکه ده.')],
    [('No Nightingale did ever chaunt', 'کسی بلبل نے کبھی ایسے نغمے نہیں گائے', 'هېڅ بلبل هېڅکله داسې سندرې نه دي ویلي'),
     ('More welcome notes to weary bands', 'جو تھکے ہوئے قافلوں کو زیادہ خوشگوار لگتے', 'چې ستړو کاروانونو ته دې ډېرې خوږې وي'),
     ('Of travellers in some shady haunt,', 'مسافروں کو کسی سایہ دار ٹھکانے میں،', 'د مسافرو، په کوم سیوري لرونکي ځای کې،'),
     ('Among Arabian sands:', 'عرب کے ریگزاروں کے درمیان:', 'د عربو د شګو په منځ کې:'),
     ("A voice so thrilling ne'er was heard", 'ایسی سنسنی خیز آواز کبھی نہیں سنی گئی', 'داسې زړه‌راښکونکی غږ هېڅکله نه دی اورېدل شوی'),
     ('In spring-time from the Cuckoo-bird,', 'موسمِ بہار میں کوئل سے،', 'د پسرلي په موسم کې له کوکو مرغۍ،'),
     ('Breaking the silence of the seas', 'سمندروں کی خاموشی توڑتے ہوئے', 'د سمندرونو چوپتیا ماتوي'),
     ('Among the farthest Hebrides.', 'دور ترین ہیبرائیڈز جزائر کے درمیان۔', 'د تر ټولو لرې هېبرایډز ټاپوګانو په منځ کې.')],
    [('Will no one tell me what she sings?—', 'کیا کوئی مجھے نہیں بتائے گا کہ وہ کیا گا رہی ہے؟—', 'ایا څوک راته نه وايي چې هغه څه وايي؟—'),
     ('Perhaps the plaintive numbers flow', 'شاید یہ درد بھرے اشعار بہہ رہے ہیں', 'ښايي دا دردناک بیتونه بهېږي'),
     ('For old, unhappy, far-off things,', 'پرانی، ناخوشگوار، دور دراز باتوں کے لیے،', 'د زړو، ناخوښو، لرې شیانو لپاره،'),
     ('And battles long ago:', 'اور بہت پہلے کی جنگوں کے لیے:', 'او د ډېر پخوا جګړو لپاره:'),
     ('Or is it some more humble lay,', 'یا یہ کوئی اور سادہ سا گیت ہے،', 'یا دا کومه ډېره ساده سندره ده،'),
     ('Familiar matter of to-day?', 'آج کی کوئی جانی پہچانی بات؟', 'د نن ورځې کومه اشنا خبره؟'),
     ('Some natural sorrow, loss, or pain,', 'کوئی فطری غم، نقصان یا درد،', 'کوم طبیعي غم، زیان یا درد،'),
     ('That has been, and may be again?', 'جو ہو چکا ہے، اور پھر ہو سکتا ہے؟', 'چې شوی دی، او بیا کېدای شي؟')],
    [("Whate'er the theme, the Maiden sang", 'موضوع جو بھی ہو، دوشیزہ ایسے گاتی رہی', 'موضوع هر څه چې وه، پېغلې داسې سندره ویله'),
     ('As if her song could have no ending;', 'گویا اس کے گیت کا کوئی انجام نہ ہو؛', 'لکه د هغې سندره چې پای نه لري؛'),
     ('I saw her singing at her work,', 'میں نے اسے کام کرتے ہوئے گاتے دیکھا،', 'ما هغه د کار پر مهال د سندرو ویلو ولیده،'),
     ("And o'er the sickle bending;—", 'اور درانتی پر جھکی ہوئی؛—', 'او پر لور ټیټه؛—'),
     ('I listened, motionless and still;', 'میں نے سنا، بے حس و حرکت اور ساکت؛', 'ما واورېده، بې‌حرکته او ارام؛'),
     ('And, as I mounted up the hill,', 'اور جب میں پہاڑی پر چڑھا،', 'او کله چې زه غونډۍ ته وختم،'),
     ('The music in my heart I bore,', 'وہ موسیقی میں اپنے دل میں لیے رہا،', 'هغه موسیقي مې په زړه کې یوړه،'),
     ('Long after it was heard no more.', 'بہت دیر بعد تک جب وہ سنائی دینا بند ہو گئی۔', 'ډېر وروسته له دې چې نوره نه اورېدل کېده.')],
]
for st in ST:
    p.group('lines', st)
poem = BOOK.record(p, 'eng12-u03-poem', 'The Solitary Reaper — poem text', 'تنہا فصل کاٹنے والی — نظم', 'یوازینۍ لوګړه — شعر', 20, [27])
poem['sourceCoverIllustrationReview'] = 'Painting of a Highland girl behind the poem is decorative; not reproduced. Urdu/Pashto give a line-by-line prose rendering of the poem.'

a = Builder()
a.h('About the poet', 'شاعر کے بارے میں', 'د شاعر په اړه')
a.p('William Wordsworth (April 7,1770—April 23,1850) was an English poet. He was born in Cockermouth, Cumberland, located in the Lake District of England. He was one of the founders of Romanticism in English poetry. He is best known for his "Lyrical Ballads" — his joint publication with Samuel Taylor Coleridge— and "The Prelude" which is a Romantic epic poem. In 1843, Wordsworth became \'the poet laureate\' upon the insistence of the then prime Minister Robert Peel.',
    'ولیم ورڈزورتھ (7 اپریل 1770 — 23 اپریل 1850) ایک انگریز شاعر تھے۔ وہ انگلستان کے لیک ڈسٹرکٹ میں واقع کمبرلینڈ کے قصبے کاکر ماؤتھ میں پیدا ہوئے۔ وہ انگریزی شاعری میں رومانویت کے بانیوں میں سے تھے۔ وہ اپنی ’’لیریکل بیلڈز‘‘ — سیموئل ٹیلر کولرج کے ساتھ مشترکہ اشاعت — اور ’’دی پریلیوڈ‘‘ کے لیے سب سے زیادہ مشہور ہیں جو ایک رومانوی رزمیہ نظم ہے۔ 1843 میں اس وقت کے وزیرِ اعظم رابرٹ پیل کے اصرار پر ورڈزورتھ ’’ملک الشعراء‘‘ بنے۔',
    'ویلیم ورډزورت (د 1770 د اپرېل 7 — د 1850 د اپرېل 23) یو انګرېز شاعر و. هغه د انګلستان په لېک ډیسټرکټ کې د کمبرلینډ په کاکرماوت کې زېږېدلی. هغه په انګلیسي شاعرۍ کې د رومانتیزم له بنسټګرو څخه و. هغه په تېره د خپلو "لیریکل بالادز" — له سمویل ټېلر کولرېج سره ګډې خپرونې — او "د پریلوډ" له امله مشهور دی چې یو رومانتیک حماسي شعر دی. په 1843 کې ورډزورت د هغه وخت د لومړي وزیر رابرټ پیل په ټینګار "د شاعرانو ملک" شو.')
GL = [
    ('behold (v)', 'See', 'دیکھنا', 'کتل'), ('chaunt (v)', 'Sing', 'گانا', 'سندره ویل'), ('hebrides (n)', 'the islands off the west coast of Scotland.', 'اسکاٹ لینڈ کے مغربی ساحل کے قریب جزائر۔', 'د سکاټلېنډ د لویدیځ ساحل څېرمه ټاپوګان.'),
    ('highland (n)', 'belonging to the mountainous areas of western and northern Scotland', 'مغربی اور شمالی اسکاٹ لینڈ کے پہاڑی علاقوں سے تعلق رکھنے والا', 'د لویدیځ او شمالي سکاټلېنډ غرنیو سیمو پورې اړوند'),
    ('lass (n)', 'Girl', 'لڑکی', 'نجلۍ'), ('lay (n)', 'Song', 'گیت', 'سندره'), ('numbers (n)', 'lines of verse of music. The word is rarely used in this sense today.', 'نظم یا موسیقی کے مصرعے۔ آج یہ لفظ اس معنی میں شاذ و نادر استعمال ہوتا ہے۔', 'د شعر یا موسیقۍ بیتونه. نن دا کلمه په دې مانا ډېره لږ کارېږي.'),
    ('profound (adj.)', 'deep', 'گہرا', 'ژور'), ('single (adg.)', 'alone, by herself:', 'اکیلی، خود ہی:', 'یوازې، پخپله:'), ('strain (n)', 'Melody', 'دھن', 'نغمه'),
    ('the vale (n)', 'valley', 'وادی', 'دره'), ('yon (adv.)', 'That', 'وہ', 'هغه'),
]
a.h('Glossary', 'فرہنگ', 'وییپانګه')
gloss(a, 'eng12-u03-gloss', GL)
a.h('Reading Comprehension', 'مطالعہ اور فہم', 'لوستل او پوهه')
a.group('lines', [
    ('1. What is the theme of the poem "The Solitary Reaper"?', '1. نظم ’’تنہا فصل کاٹنے والی‘‘ کا موضوع کیا ہے؟', '1. د "یوازینۍ لوګړه" شعر موضوع څه ده؟'),
    ('2. How does Wordsworth describe the song of the solitary reaper?', '2. ورڈزورتھ تنہا فصل کاٹنے والی کے گیت کو کیسے بیان کرتا ہے؟', '2. ورډزورت د یوازینۍ لوګړې سندره څنګه بیانوي؟'),
])
ab = BOOK.record(a, 'eng12-u03-about-glossary', 'About the poet; Glossary; Reading Comprehension (1)', 'شاعر کے بارے میں؛ فرہنگ؛ مطالعہ اور فہم (1)', 'د شاعر په اړه؛ وییپانګه؛ لوستل او پوهه (1)', 20, [28])
ab['sourceCoverIllustrationReview'] = 'Portrait of Wordsworth is decorative; not reproduced.'
issues = [{'id': 'eng12-p28-typos', 'unit': 3, 'printedPage': 28, 'description': 'Glossary prints “single (adg.)”, “lines of verse of music” (or music), “hebrides” in lower case; About the poet prints “then prime Minister”. Printed text retained.'}]

if __name__ == '__main__':
    BOOK.save(20, [(3, poem), (3, ab)], issues=issues)
