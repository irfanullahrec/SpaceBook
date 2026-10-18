"""Mutalia-e-Quran XII PDF227: p.224 — al-Tahrim matters of knowledge and action; Lesson 24 vocabulary. Run: python class12_quran_page227.py"""
from class12_quran_common import BOOK, Builder, rec, KA, L, VOC

VOCAB = [
    ('فَطَلِّقُوهُنَّ', 'Then divorce them', 'پس تم انھیں طلاق دو', 'نو طلاق ورکړئ'),
    ('أَحْصُوا الْعِدَّةَ', 'Count the waiting period', 'تم عدت کو شمار کرو', 'عدت وشمېرئ'),
    ('لَا يَحْتَسِبُ', 'He does not imagine', 'اسے گمان نہیں ہوتا', 'ګومان یې نه کوي'),
    ('بَالِغُ أَمْرِهِ', 'He accomplishes His purpose', 'وہ اپنا کام پورا کر کے رہتا ہے', 'خپل کار پوره کوي'),
    ('قَدْرًا', 'A measure', 'اندازہ', 'اندازه'),
    ('ثَلَاثَةُ أَشْهُرٍ', 'Three months', 'تین مہینے', 'درې میاشتې'),
    ('فَإِنْ أَرْضَعْنَ', 'Then if they suckle', 'پس اگر وہ دودھ پلائیں', 'نو که شیدې ورکړي'),
    ('سَبْعَ سَمَاوَاتٍ', 'Seven heavens', 'سات آسمان', 'اووه آسمانونه'),
    ('نَبَّأَتْ', 'She informed', 'اس نے خبر دی', 'خبر یې ورکړ'),
    ('ظَهِيرٌ', 'Helper', 'مددگار', 'مرستندوی'),
    ('أَنْ يُبْدِلَهُ', 'That He may give him in exchange', 'کہ وہ اس کو بدل دے', 'چې ورته بدل کړي'),
    ('سَائِحَاتٍ', 'Women who fast', 'روزہ دار عورتیں', 'روژه نیوونکې ښځې'),
    ('ثَيِّبَاتٍ', 'Previously married', 'شوہر دیدہ', 'مېړه لیدلې'),
    ('أَبْكَارًا', 'Virgins', 'کنواریاں', 'پېغلې'),
    ('قُوا', 'Save, protect', 'تم بچاؤ', 'وژغورئ'),
    ('وَقُودُهَا', 'Its fuel', 'اس کا ایندھن', 'د هغه خشاک'),
    ('غِلَاظٌ شِدَادٌ', 'Stern and very strong', 'سخت مزاج بہت طاقت ور', 'سخت‌مزاجه، ډېر ځواکمن'),
    ('تَوْبَةً نَصُوحًا', 'Sincere repentance', 'خالص توبہ', 'خالصه توبه'),
    ('وَاغْلُظْ', 'And be stern', 'اور آپ سختی کیجیے', 'او سختي وکړئ'),
    ('أَحْصَنَتْ', 'She guarded', 'اس نے حفاظت کی', 'وساته'),
    ('فَنَفَخْنَا', 'So We breathed', 'تو ہم نے پھونک دیا', 'نو موږ پو وکړ'),
    ('مِنَ الْقَانِتِينَ', 'Of the obedient', 'اطاعت گزاروں میں سے', 'له اطاعت کوونکو'),
]


def p227():
    b = Builder()
    KA(b)
    L(b, [('In family life, in the context of mutual likes and dislikes, if some slip or shortcoming occurs from women, they too should repent in the presence of Allah Almighty and, acknowledging their shortcoming, should also bring improvement in their attitude, so that domestic life remains pleasant and no serious stage arises.', 'عائلی زندگی میں باہمی پسند و ناپسند کے حوالہ سے اگر خواتین سے کوئی لغزش اور کوتاہی ہو جائے تو انھیں اللہ تعالیٰ کے حضور بھی توبہ کرنی چاہیے اور اپنی کوتاہی کا اعتراف کر کے اپنے رویہ میں بھی بہتری لانی چاہیے تاکہ گھریلو زندگی خوشگوار رہے اور کوئی سنگین مرحلہ درپیش نہ ہو۔', 'په کورني ژوند کې د خپل منځي خوښې او ناخوښې په اړه که له ښځو کومه تېروتنه او کمزوري وشي، نو هغوی باید د الله تعالی حضور ته هم توبه وکړي او د خپلې کمزورۍ په منلو سره په خپل چلند کې هم ښه والی راولي، تر څو کورنی ژوند خوشاله پاتې شي او کوم سخت پړاو مخې ته رانه شي.'),
          ('Just as the lofty qualities of the Pure Wives (may Allah be pleased with them) are proof of their high conduct and character, they are also a guiding light for the women of the Ummah. They too should try to create these qualities and this character within themselves.', 'ازواجِ مطہرات رضی اللہ عنہن کی اعلیٰ صفات جہاں ان کی اعلیٰ سیرت و کردار کی دلیل ہیں وہاں اُمت کی خواتین کے لیے مشعلِ راہ بھی ہیں، انھیں چاہیے کہ وہ بھی ان صفات و کردار کو اپنے اندر پیدا کرنے کی کوشش کریں۔', 'د پاکو مېرمنو رضي الله عنهن لوړ صفتونه په داسې حال کې چې د هغوی د لوړ سیرت او کړنو دلیل دي، د امت د ښځو لپاره د لارې څراغ هم دي؛ هغوی باید هم هڅه وکړي چې دا صفتونه او کړنې په ځان کې پیدا کړي.'),
          ('Allah Almighty has instructed the head of the household that he is responsible not only for the upkeep of his family, but it is also his responsibility to try to save his family and dependants along with himself from the punishment of the Hereafter. In this matter he should arrange for their religious and moral guidance and upbringing in a correct manner.', 'اللہ تعالیٰ نے سربراہِ خاندان کے لیے ہدایت فرمائی ہے کہ وہ صرف اپنے خاندان کی کفالت کا ذمہ دار نہیں ہے بلکہ اس کی یہ ذمہ داری بھی ہے کہ وہ اپنے ساتھ اپنے اہل و عیال کو اُخروی عذاب سے بچانے کی کوشش کرے۔ اس معاملہ میں اُن کی درست انداز میں دینی و اخلاقی رہنمائی و تربیت کا اہتمام کرے۔', 'الله تعالی د کورنۍ مشر ته لارښوونه کړې چې هغه یوازې د خپلې کورنۍ د پالنې مسؤل نه دی، بلکې دا یې هم مسؤلیت دی چې له ځان سره خپله کورنۍ او اولاد هم د آخرت له عذابه د ژغورلو هڅه وکړي؛ په دې چاره کې باید په سمه توګه د هغوی د دیني او اخلاقي لارښوونې او روزنې اهتمام وکړي.')])
    VOC(b, 'mq12-l24-vocab', VOCAB)
    BOOK.save(227, [(24, rec(b, 24, 227, 227))], issues=[{'id': 'mq12-pdf227', 'unit': 24, 'printedPage': 224,
               'description': 'Four-column vocabulary (covering both surahs) rendered as one two-column table (22 rows). Lower part of p.224 blank.'}])


if __name__ == '__main__':
    p227()
