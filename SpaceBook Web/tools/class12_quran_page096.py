"""Mutalia-e-Quran XII PDF96: p.93 — Lesson 9 matters of knowledge and action; vocabulary. Run: python class12_quran_page096.py"""
from class12_quran_common import BOOK, Builder, rec, KA, L, VOC

VOCAB = [
    ('فَرَضْنَاهَا', 'We made (its commands) obligatory', 'ہم نے اس (کے احکام) کو فرض کیا', 'موږ یې (حکمونه) فرض کړل'),
    ('مِائَةَ جَلْدَةٍ', 'A hundred lashes', 'سو کوڑے', 'سل دُرې'),
    ('لَا يَنْكِحُهَا', 'He does not marry her', 'وہ اس سے نکاح نہیں کرتا', 'ورسره نکاح نه کوي'),
    ('يَرْمُونَ', 'They accuse', 'وہ تہمت لگاتے ہیں', 'تور لګوي'),
    ('بِأَرْبَعَةِ شُهَدَاءَ', 'With four witnesses', 'چار گواہوں کے ساتھ', 'له څلورو شاهدانو سره'),
    ('يَدْرَؤُا', 'It may avert', 'وہ ٹال سکتا ہے', 'لرې کولی شي'),
    ('إِفْكٌ', 'Slander', 'بہتان', 'بهتان'),
    ('أَفَضْتُمْ', 'You were engaged (in talk)', 'تم پڑ گئے ہو', 'تاسو پکې لوېدلي وئ'),
    ('الْغَافِلَاتِ', 'Innocent (women)', 'بھولی بھالی (عورتیں)', 'ساده‌زړې (ښځې)'),
    ('جُيُوبِهِنَّ', 'Their bosoms (necklines)', 'ان کے گریبان', 'د هغوی ګرېوانونه'),
    ('لَا تُكْرِهُوا', 'Do not compel', 'تم مجبور نہ کرو', 'اړ مه باسئ'),
    ('فَاجْلِدُوا', 'So flog', 'پس تم کوڑے لگاؤ', 'نو دُرې ووهئ'),
    ('رَأْفَةٌ', 'Pity, mercy', 'ترس کھانا، رحم کرنا', 'زړه سوی، رحم'),
    ('حُرِّمَ', 'It has been made unlawful', 'وہ حرام کیا گیا ہے', 'حرام کړای شو'),
    ('الْمُحْصَنَاتِ', 'Chaste (women)', 'پاک دامن (عورتیں)', 'پاکلمنې (ښځې)'),
    ('ثَمَانِينَ', 'Eighty', 'اسی', 'اتیا'),
    ('عُصْبَةٌ', 'A band, group', 'ٹولہ، جماعت، گروہ', 'ډله، ټولګی'),
    ('لَمَسَّكُمْ', 'It would surely have touched you', 'وہ ضرور تمھیں پہنچتا', 'خامخا به درته رسېدلی و'),
    ('خُطُوَاتِ الشَّيْطَانِ', 'The footsteps of Satan', 'شیطان کے نقشِ قدم', 'د شیطان پلونه'),
    ('بِخُمُرِهِنَّ', 'Their head-coverings / veils', 'ان کی اوڑھنیاں / چادریں', 'د هغوی ټکري / څادرونه'),
    ('غَيْرِ أُولِي الْإِرْبَةِ', 'Those without (sexual) desire', 'جو (جنسی) خواہش نہیں رکھتے', 'چې (جنسي) غوښتنه نه لري'),
    ('الْبِغَاءِ', 'Prostitution', 'بدکاری', 'بدکاري'),
]


def p96():
    b = Builder()
    KA(b)
    L(b, [('The crime of zina is intolerable in an Islamic society; in the same way, making a false accusation of zina is also a most serious crime, and its punishment too is very great.', 'زنا کا جرم اسلامی معاشرہ میں ناقابلِ برداشت ہے اسی طرح زنا کا بہتان لگانا بھی سخت ترین جرم ہے اور اس کی سزا بھی بہت بڑی ہے۔', 'د زنا جرم په اسلامي ټولنه کې د زغم وړ نه دی؛ همداسې د زنا تور لګول هم تر ټولو سخت جرم دی او سزا یې هم ډېره لویه ده.'),
          ('Before entering anyone\'s house, one should seek permission from the people of the house and greet the people of the house with salam. Further, it should be remembered that the four walls of a home are the protection of human dignity.', 'کسی کے گھر میں داخل ہونے سے پہلے گھر والوں سے اجازت لینی چاہیے اور گھر والوں کو سلام کرنا چاہیے۔ مزید یہ یاد رکھنا چاہیے کہ گھر کی چار دیواری کا تحفظ احترامِ آدمیت کا تحفظ ہے۔', 'د چا کور ته له ننوتلو مخکې باید د کور له خلکو اجازه واخیستل شي او د کور خلکو ته سلام واچول شي؛ همدارنګه باید په یاد وي چې د کور د څلورو دېوالونو ساتنه د انساني درناوي ساتنه ده.'),
          ('Allah Almighty has commanded the believing men and believing women to guard their gaze and their private parts. In the same way it is not appropriate for a believing woman to display her adornment, beauty and finery before non-mahram men. We should remember that it is easy and effective to stop any evil and corruption at its first stage.', 'اللہ تعالیٰ نے مومن مردوں اور مومن عورتوں کو اپنی نگاہ اور اپنی شرم گاہ کی حفاظت کا حکم دیا ہے۔ اسی طرح کسی مومنہ عورت کے لیے مناسب نہیں کہ وہ اپنی زیب و زینت اور آرائش و زیبائش کا اظہار غیر محرموں کے سامنے کرے۔ ہمیں یاد رکھنا چاہیے کہ کسی بھی بُرائی اور فساد کو اس کے پہلے مرحلہ پر روکنا آسان اور مؤثر ہوتا ہے۔', 'الله تعالی مؤمنو نارینه وو او مؤمنو ښځو ته د خپلې سترګې او شرمګاه د ساتنې حکم کړی؛ همداسې مؤمنې ښځې ته نه ښایي چې خپل سینګار او ښکلا غیر محرمو ته ښکاره کړي. باید په یاد ولرو چې هره بدي او فساد په لومړي پړاو کې منع کول اسانه او اغېزمن وي.')])
    VOC(b, 'mq12-l9-vocab', VOCAB)
    BOOK.save(96, [(9, rec(b, 9, 96, 96))], issues=[{'id': 'mq12-pdf096', 'unit': 9, 'printedPage': 93,
               'description': 'Four-column vocabulary rendered as one two-column table (22 rows).'}])


if __name__ == '__main__':
    p96()
