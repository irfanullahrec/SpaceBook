"""Mutalia-e-Quran XII PDF178: p.175 — Lesson 18 matters of knowledge and action (2–5); vocabulary. Run: python class12_quran_page178.py"""
from class12_quran_common import BOOK, Builder, rec, L, VOC

VOCAB = [
    ('سِتَّةِ أَيَّامٍ', 'Six days', 'چھے دن', 'شپږ ورځې'),
    ('اسْتَوَىٰ', 'He established Himself (in a manner befitting Him)', 'وہ جلوہ افروز ہوا', 'مستوي شو'),
    ('يَلِجُ', 'It enters', 'وہ داخل ہوتا ہے', 'ننوځي'),
    ('يَعْرُجُ', 'It ascends', 'وہ چڑھتا ہے', 'ختي'),
    ('هُوَ مَعَكُمْ', 'He is with you', 'وہ تمھارے ساتھ ہے', 'هغه له تاسو سره دی'),
    ('أَنْفَقَ', 'He spent', 'اس نے خرچ کیا', 'ویې لګول'),
    ('تَرَى', 'You will see', 'آپ دیکھیں گے', 'وبه وینئ'),
    ('يَسْعَىٰ', 'It will be running', 'وہ دوڑ رہا ہوگا', 'منډې به وهي'),
    ('بِأَيْمَانِهِمْ', 'On their right', 'اُن کے دائیں طرف', 'د هغوی ښي لوري ته'),
    ('سُورٍ', 'A wall', 'دیوار', 'دېوال'),
    ('الْغَرُورُ', 'The deceiver', 'دھوکے باز', 'غولوونکی'),
    ('سَابِقُوا', 'Race one another', 'تم ایک دوسرے پر سبقت لے جاؤ', 'پر یو بل مخکې شئ'),
    ('أَنْ نَبْرَأَهَا', 'That We bring it into being', 'کہ ہم اس کو پیدا کریں', 'چې موږ یې پیدا کړو'),
    ('يَسِيرٌ', 'Easy', 'آسان', 'اسان'),
    ('تَأْسَوْا', 'You grieve', 'تم غم کرو', 'غم وکړئ'),
    ('فَاتَكُمْ', 'It slipped from you', 'وہ تمھارے (ہاتھ سے) جاتی رہی', 'ستاسو (له لاسه) ووتله'),
    ('لَا تَفْرَحُوا', 'Do not exult', 'تم نہ اتراؤ', 'مه ویاړئ'),
    ('الْحَدِيدَ', 'Iron', 'لوہا', 'اوسپنه'),
    ('بَأْسٌ', '(Military) strength', '(جنگی) طاقت', '(جنګي) ځواک'),
    ('أَلَّا يَقْدِرُونَ', 'That they have no power', 'کہ انھیں کوئی اختیار نہیں', 'چې هېڅ اختیار نه لري'),
]


def p178():
    b = Builder()
    L(b, [('Those people who, even after hearing the truth, do not take advantage of the respite for action and reform their deeds, Allah Almighty hardens their hearts, and such people are sinful. We should establish a strong connection with the Qur\'an Karim and fulfil its demands.', 'حق بات سن کر بھی جو لوگ عمل کی مہلت سے فائدہ اٹھا کر اپنے عمل کی اصلاح نہیں کرتے تو اللہ تعالیٰ ان کے دل سخت کر دیتا ہے اور ایسے لوگ فاسق ہیں۔ ہمیں قرآنِ کریم سے مضبوط تعلق قائم کر کے اس کے تقاضوں کو پورا کرنا چاہیے۔', 'هغه خلک چې حقه خبره له اورېدو وروسته هم د عمل له مهلت ګټه نه اخلي او خپل عمل نه سموي، الله تعالی یې زړونه سخت کړي، او داسې خلک فاسقان دي. موږ باید له قرآن کریم سره ټینګه اړیکه جوړه کړو او د هغه غوښتنې پوره کړو.'),
          ('If a person feels that he has fallen behind in good deeds, he should not despair; he should hope that Allah Almighty, who can bring dead land to life by sending rain, can also grant the ability to do good deeds so as to irrigate the land of our hearts with the light of faith.', 'اگر انسان محسوس کرے کہ وہ نیک اعمال میں پیچھے رہ گیا ہے تو اسے مایوس نہیں ہونا چاہیے اور یہ امید رکھنی چاہیے کہ جو اللہ تعالیٰ بارش برسا کر مردہ زمین کو آباد کر سکتا ہے وہ ہمارے دلوں کی زمین کو ایمان کے نور سے سیراب کرنے کے لیے نیک اعمال کی توفیق عطا فرما سکتا ہے۔', 'که انسان احساس وکړي چې په نېکو عملونو کې شاته پاتې شوی، باید مایوسه نه شي او دا هیله ولري چې هغه الله تعالی چې په باران وورولو مړه ځمکه ژوندۍ کولی شي، زموږ د زړونو ځمکه د ایمان په نور د خړوبولو لپاره د نېکو عملونو توفیق راکولی شي.'),
          ('Most people, at different stages of their lives, become occupied in such interests as make them heedless of fulfilling the demands of faith and religion — for example play and amusement in childhood, adornment and finery in youth, boasting of getting ahead of others in early adulthood, and in old age greed for an abundance of accumulated wealth and children. We should not forget the Hereafter by falling into this deception of the life of the world.', 'اکثر انسان اپنی زندگی کے مختلف مراحل میں ایسی دلچسپیوں میں مشغول ہو جاتے ہیں جو انھیں ایمان اور دین کے تقاضوں کی ادائیگی سے غافل کر دیتی ہیں مثلاً بچپن میں کھیل کود، نوجوانی میں زیب و زینت، جوانی میں دوسروں سے آگے بڑھ جانے کا فخر اور بڑھاپے میں جمع کیے ہوئے مال و اولاد پر کثرت کی ہوس۔ ہمیں دنیا کی زندگی کے اس دھوکا میں پڑ کر آخرت کو نہیں بھولنا چاہیے۔', 'ډېر انسانان د خپل ژوند په بېلابېلو پړاوونو کې په داسې لېوالتیاوو بوخت شي چې د ایمان او دین د غوښتنو له ادا کولو یې غافلوي، لکه په ماشومتوب کې لوبې، په تنکي ځوانۍ کې سینګار، په ځوانۍ کې له نورو د مخکې کېدو وياړ، او په زړښت کې پر راټول شوي مال او اولاد د زیاتوالي حرص. موږ باید د دنیا د ژوند په دې دوکه کې ونه لوېږو او آخرت هېر نه کړو.'),
          ('We should not grieve too much over any loss; rather we should be patient, because the loss that was destined has happened and that loss could not have been averted; and the blessings that Allah Almighty grants us, we should not exult over them but should give thanks, because every blessing is received from the bounty of Allah Almighty and is decreed from Him.', 'ہمیں کسی نقصان پر بہت زیادہ غم نہیں بلکہ صبر کرنا چاہیے کیوں کہ جس نقصان کا ہونا مقدر ہو چکا ہوا اس نقصان سے بچا نہیں جا سکتا اور جو نعمتیں اللہ تعالیٰ ہمیں عطا فرمائے ان پر اترانا نہیں بلکہ شکر ادا کرنا چاہیے کیونکہ ہر نعمت اللہ تعالیٰ کے فضل سے ملتی ہے اور وہ اس کی طرف سے مقرر ہوتی ہے۔', 'موږ باید پر کوم زیان ډېر غم ونه کړو بلکې صبر وکړو، ځکه چې کوم زیان مقدر شوی و، له هغه ځان نه شو ژغورلی؛ او کوم نعمتونه چې الله تعالی موږ ته راکړي، پرې ونه ویاړو بلکې شکر یې ادا کړو، ځکه چې هر نعمت د الله تعالی په فضل ترلاسه کېږي او د هغه له لوري ټاکل شوی وي.')])
    VOC(b, 'mq12-l18-vocab', VOCAB)
    BOOK.save(178, [(18, rec(b, 18, 178, 178))], issues=[{'id': 'mq12-pdf178', 'unit': 18, 'printedPage': 175,
               'description': 'Knowledge points continued from p.174. Last point prints "جس نقصان کا ہونا مقدر ہو چکا ہوا اس نقصان" (kept). Four-column vocabulary rendered as one two-column table (20 rows). Orange highlighter marks by a reader excluded.'}])


if __name__ == '__main__':
    p178()
