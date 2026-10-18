"""Mutalia-e-Quran XII PDF217: p.214 — al-Taghabun knowledge points (2–3); Lesson 23 vocabulary; exercise Q1 item 1. Run: python class12_quran_page217.py"""
from class12_quran_common import BOOK, Builder, rec, L, VOC, EX, MCQ, Q1, words

VOCAB = [
    ('يَشْهَدُ', 'He bears witness', 'وہ گواہی دیتا ہے', 'شاهدي ورکوي'),
    ('أَيْمَانَهُمْ', 'Their oaths', 'ان کی قسمیں', 'د هغوی قسمونه'),
    ('فَطُبِعَ', 'So a seal was set', 'پس مہر لگا دی گئی', 'نو مهر ولګول شو'),
    ('خُشُبٌ مُسَنَّدَةٌ', 'Timbers propped up (hollow)', 'دیوار سے لگائی (کھوکھلی) لکڑیاں', 'دېوال ته تکیه شوي (تش) لرګي'),
    ('الْعَدُوُّ', 'The enemy', 'دشمن', 'دښمن'),
    ('رَجَعْنَا', 'We returned', 'ہم واپس گئے', 'بېرته لاړو'),
    ('الْأَعَزُّ', 'The more honourable', 'زیادہ عزت والا', 'ډېر عزتمن'),
    ('الْأَذَلَّ', 'The more abased', 'زیادہ ذلت والا', 'ډېر ذلیل'),
    ('لَا تُلْهِكُمْ', 'Let it not divert you', 'وہ تمھیں غافل نہ کر دے', 'تاسو دې غافل نه کړي'),
    ('تُسِرُّونَ', 'You conceal', 'تم چھپاتے ہو', 'پټوئ'),
    ('تُعْلِنُونَ', 'You make public', 'تم ظاہر کرتے ہو', 'ښکاره کوئ'),
    ('لَتُبْعَثُنَّ', 'You will surely be raised', 'تم ضرور اٹھائے جاؤ گے', 'خامخا به راپاڅول شئ'),
    ('لَتُنَبَّؤُنَّ', 'You will surely be informed', 'تمھیں ضرور بتایا جائے گا', 'خامخا به درته وویل شي'),
    ('يَوْمُ التَّغَابُنِ', 'The day of loss and gain', 'ہار جیت کا دن', 'د ګټې او بایلنې ورځ'),
    ('الْبَلَاغُ الْمُبِينُ', 'Clear conveyance', 'واضح طور پر پہنچا دینا', 'په ښکاره ډول رسول'),
    ('فَاحْذَرُوهُمْ', 'So beware of them', 'پس تم ان سے ہوشیار رہو', 'نو ترې هوښیار اوسئ'),
    ('إِنْ تَعْفُوا', 'If you pardon', 'اگر تم معاف کر دو', 'که عفو وکړئ'),
    ('وَتَصْفَحُوا', 'And you overlook', 'اور تم درگزر کرو', 'او تېر شئ'),
    ('فِتْنَةٌ', 'A trial', 'آزمائش', 'ازموینه'),
    ('مَا اسْتَطَعْتُمْ', 'As much as you are able', 'جو تم سے ہو سکے', 'څومره چې وس مو رسي'),
    ('إِنْ تُقْرِضُوا', 'If you lend', 'اگر تم قرضِ حسنہ دو گے', 'که ښه پور ورکړئ'),
    ('شَكُورٌ', 'Most appreciative', 'نہایت قدر دان', 'ډېر قدردان'),
]


def p217():
    b = Builder()
    L(b, [('One of the fruits of faith is that the servant becomes content with the pleasure of Allah Almighty in every condition and becomes one who is patient in afflictions instead of complaining. However, this does not negate the immediate and involuntary effect of some shock; rather it negates that lasting effect from which complaints arise on the tongue and a trace of ill-thought about the Lord arises in the heart.', 'ایمان کے ثمرات میں سے ایک یہ ہے کہ بندہ ہر حال میں اللہ تعالیٰ کی رضا پر راضی رہنے والا ہو جائے۔ مصائب پر شکوہ شکایت کے بجائے صبر کرنے والا بن جائے۔ البتہ کسی صدمہ پر فوری اور غیر اختیاری تاثر کی نفی نہیں بلکہ اُس مستقل تاثر کی نفی ہے جس سے زبان پر شکوہ اور دل میں رب سے بدگمانی کا شائبہ پیدا ہوتا ہے۔', 'د ایمان له ګټو یوه دا ده چې بنده په هر حال کې د الله تعالی پر رضا راضي پاتې شي، او پر مصیبتونو د ګیلې پر ځای صابر شي. البته د کوم صدمې پر وړاندې د سمدستي او بې‌اختیاره اغېز نفي نه ده، بلکې د هغه دوامداره اغېز نفي ده چې له هغه په ژبه ګیله او په زړه کې له رب سره د بدګومانۍ نښه پیدا کېږي.'),
          ('The believing servant\'s reliance is not on his own effort, intelligence, planning and the means he has arranged, but on Allah Almighty. Tawakkul is that permissible means be adopted for permissible matters, but reliance concerning the result be placed only on the Causer of causes.', 'بندۂ مومن کا بھروسہ اپنی محنت، ذہانت، منصوبہ بندی اور فراہم کردہ اسباب پر نہیں بلکہ اللہ تعالیٰ پر ہوتا ہے۔ توکل یہ ہے کہ جائز اُمور کے لیے جائز اسباب اختیار کیے جائیں لیکن نتیجہ کے حوالہ سے بھروسہ مُسَبِّبُ الْأَسْبَاب پر ہی کیا جائے۔', 'د مؤمن بنده باور پر خپله هڅه، هوښیارتیا، پلان جوړونه او برابرو شویو اسبابو نه، بلکې پر الله تعالی وي. توکل دا دی چې د روا چارو لپاره روا اسباب غوره شي، خو د پایلې په اړه باور یوازې پر مسبب الاسباب وشي.')])
    VOC(b, 'mq12-l23-vocab', VOCAB)
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, words(63, 1, 14, 18), ('— in this Allah Almighty has borne witness that the hypocrites are:', 'میں اللہ تعالیٰ نے گواہی دی ہے کہ منافقین ہیں:', '— په دې کې الله تعالی شاهدي ورکړې چې منافقان دي:'),
        [('liars', 'جھوٹے', 'دروغجن'), ('cowards', 'بزدل', 'بزدلان'), ('deceivers', 'مکار', 'چل‌بازان'), ('misers', 'بخیل', 'بخیلان')])
    BOOK.save(217, [(23, rec(b, 23, 217, 217, kind='exercise'))], issues=[{'id': 'mq12-pdf217', 'unit': 23, 'printedPage': 214,
               'description': 'Knowledge points 2–3 continued from p.213. Four-column vocabulary (covering both surahs) rendered as one two-column table (22 rows). Q1 continues on p.215. Quoted verses drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p217()
