"""Urdu XII PDF115 (spread): p.220 Poem 8 مشق Q1 + note آزاد نظم; p.221 section title page 'حصۂ غزل'."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Write answers to the following questions according to the poem.', '۱۔ نظم کے مطابق درج ذیل سوالوں کا جواب لکھیں۔', '۱. د نظم سره سم لاندې پوښتنو ته ځواب ولیکئ.')
e.group('lines', [
    ('(a) What is the poet saying to the stars in this poem?', '(ا) اس نظم میں شاعر ستاروں سے کیا کہہ رہا ہے؟', '(الف) په دې نظم کې شاعر ستورو ته څه وايي؟'),
    ('(b) Whom has the poet called brave and a warrior in the poem?', '(ب) شاعر نے نظم میں بہادر اور سورما کس کو کہا ہے؟', '(ب) شاعر په نظم کې چا ته زړور او اتل ویلي؟'),
    ('(c) Why has the poet called the stars cowards?', '(ج) شاعر نے ستاروں کو ڈرپوک کیوں کہا ہے؟', '(ج) شاعر ستوري ولې ډارن بللي؟'),
    ('(d) Define free verse (āzād naẓm) and blank verse (muʿarrā naẓm) and give one example of each.', '(د) آزاد نظم اور معریٰ نظم کی تعریف کریں اور ایک ایک مثال دیں۔', '(د) د ازاد نظم او معرا نظم تعریف وکړئ او د هر یوه یوه بېلګه ورکړئ.'),
    ('(e) What qualities of the star that comes out by day have been described?', '(ہ) دن کو نکلنے والے ستارے کی کون کون سی خوبیاں بیان کی گئی ہیں؟', '(ه) د ورځې د راوتونکي ستوري کومې ښېګڼې بیان شوې؟'),
])
ex = BOOK.record(e, 'urdu12-u25-exercise', 'Exercise', 'مشق', 'تمرین', 115, [220])

n = Builder()
n.h('Free verse (āzād naẓm)', 'آزاد نظم', 'ازاد نظم')
n.p('When Urdu poetry became crowded with subjects and ideas, poets began to feel hampered by the constraint of rhyme and refrain. Under the influence of Western literature the modern naẓm came into fashion here too; notable among its forms are free verse and blank verse. In free verse there is no constraint of rhyme and refrain, nor of metre and baḥr, yet continuity, flow and musicality in the verses are necessary. Free verse is based on one baḥr, but the division of its feet (arkān) is at the poet’s discretion: some lines are long and some short, and sometimes a line is very long. Many experiments in form have been made in free verse; special care is taken of poetic rhythm and sound effect.',
    'اُردو شاعری میں جب موضوعات اور خیالات کی بھرمار ہو گئی تو شاعروں کو قافیہ اور ردیف کی پابندی سے اُلجھن ہونے لگی۔ مغربی ادب کے زیرِ اثر یہاں بھی جدید نظم کا رواج ہوا۔ ان میں آزاد نظم اور نظمِ معریٰ قابلِ ذکر ہیں۔ آزاد نظم میں قافیہ اور ردیف سمیت وزن اور بحر کی پابندی نہیں ہوتی تاہم اشعار میں تسلسل، روانی اور موسیقیت ضروری ہے۔ آزاد نظم کی بنیاد ایک بحر پر ہوتی ہے لیکن اس بحر کے ارکان کی تقسیم شاعر کی صوابدید پر ہوتی ہے۔ کوئی مصرع بڑا اور کوئی چھوٹا ہوتا ہے اور بعض اوقات تو ایک مصرع بہت طویل ہوتا ہے۔ آزاد نظم میں ہیئت کے حوالے سے متعدد تجربات ہوئے ہیں۔ آزاد نظم میں شعری آہنگ اور صوتی تاثر کا خاص خیال رکھا جاتا ہے۔',
    'کله چې په اردو شاعرۍ کې د موضوعګانو او فکرونو ګڼه ګوڼه شوه، شاعرانو ته د قافیې او ردیف له پابندۍ ستونزه پیدا شوه. د لوېدیځ ادب تر اغېز لاندې دلته هم نوی نظم دود شو؛ په دې کې ازاد نظم او معرا نظم د یادونې وړ دي. په ازاد نظم کې د قافیې او ردیف ترڅنګ د وزن او بحر پابندي هم نه وي، خو په بیتونو کې پرله‌پسې‌والی، روانتیا او موسیقیت ضروري دي. د ازاد نظم بنسټ پر یوه بحر وي، خو د هغه بحر د ارکانو وېش د شاعر په خوښه وي: ځینې مصرعې اوږدې او ځینې لنډې وي، او کله کله یوه مصرع ډېره اوږده وي. په ازاد نظم کې د بڼې ګڼې تجربې شوې؛ په ازاد نظم کې شعري اهنګ او غږیز اغېز ته ځانګړې پاملرنه کېږي.')
nt = BOOK.record(n, 'urdu12-u25-note', 'Note: free verse', 'آزاد نظم', 'ازاد نظم', 115, [220])

g = Builder()
g.h('Ghazal section', 'حصۂ غزل', 'د غزل برخه')
g.p('Section title page (p.221): “Ḥiṣṣa-e Ghazal” — the ghazal section of the book (ghazals 9–16).', 'عنوانی صفحہ (ص ۲۲۱): ’’حصۂ غزل‘‘ — کتاب کا غزلوں کا حصہ (غزلیں ۹–۱۶)۔', 'سرلیک مخ (۲۲۱ مخ): "د غزل برخه" — د کتاب د غزلو برخه (غزلې ۹–۱۶).')
UT = ('Ghazal: Those I sought in the heavens and on the earths', 'غزل: جنھیں میں ڈھونڈتا تھا آسمانوں میں زمینوں میں', 'غزل: هغه چې ما په اسمانونو او ځمکو کې لټول', 'علامہ اقبالؒ')
sec = BOOK.record(g, 'urdu12-ghazal-title', 'Ghazal section (title page)', 'حصۂ غزل', 'د غزل برخه', 115, [221], unit_title=UT)
sec['sourceCoverIllustrationReview'] = 'Decorative blue eight-pointed frame and a quill-inkpot-paper drawing; not reproduced.'
issues = [{'id': 'urdu12-pdf115', 'unit': 25, 'printedPage': 220, 'description': 'p.220: last line cut at the gutter (“[ت]اثر کا خاص خیال رکھا جاتا ہے”) — reconstructed. Note: the definition says free verse has no constraint of “metre and baḥr” yet is “based on one baḥr” — retained as printed. Ghazals 9–16 will be units 26–33.'}]

if __name__ == '__main__':
    BOOK.save(115, [(25, ex), (25, nt), (26, sec)], issues=issues, complete_units=[25])
