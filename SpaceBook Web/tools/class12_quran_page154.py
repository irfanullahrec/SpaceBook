"""Mutalia-e-Quran XII PDF154: p.151 — Lesson 15 matters of knowledge and action (3–4); vocabulary. Run: python class12_quran_page154.py"""
from class12_quran_common import BOOK, Builder, rec, L, VOC

VOCAB = [
    ('الرِّقَابِ', 'Necks', 'گردنیں', 'غاړې'),
    ('إِذَا أَثْخَنْتُمُوهُمْ', 'When you have thoroughly subdued them', 'پس جب تم انھیں خوب قتل کر چکو', 'نو کله چې مو ښه ووژل'),
    ('الْوَثَاقَ', 'Binding firmly', 'مضبوط باندھنا', 'ټینګ تړل'),
    ('مَنًّا', 'Favour (release as a favour)', 'احسان', 'احسان'),
    ('الْحَرْبُ', 'War', 'جنگ', 'جګړه'),
    ('أَوْزَارَهَا', 'Its weapons (burdens)', 'اس کے ہتھیار', 'د هغې وسلې'),
    ('بَالَهُمْ', 'Their condition', 'اُن کی حالت', 'د هغوی حالت'),
    ('عَرَّفَهَا', 'He has made it known (well)', 'وہ اسے (خوب) پہچان کرا چکا ہے', '(ښه) یې ورپېژندلی'),
    ('يَتَمَتَّعُونَ', 'They are enjoying', 'وہ لطف اٹھا رہے ہیں', 'خوند اخلي'),
    ('مَثْوًى', 'Abode', 'ٹھکانا', 'ځای'),
    ('نَاصِرَ', 'Helper', 'مددگار', 'مرستندوی'),
    ('مَاءٍ غَيْرِ آسِنٍ', 'Water that will not go stale', 'پانی بدبودار نہ ہوگا', 'اوبه چې بدبویه نه شي'),
    ('لَبَنٍ', 'Milk', 'دودھ', 'شیدې'),
    ('طَعْمُهُ', 'Its taste', 'اس کا ذائقہ', 'د هغه خوند'),
    ('خَمْرٍ', 'Wine', 'شراب', 'شراب'),
    ('لَذَّةٍ لِلشَّارِبِينَ', 'Delicious to those who drink', 'پینے والوں کے لیے لذت بخش ہے', 'څښونکو ته خوندوره'),
    ('عَسَلٍ مُصَفًّى', 'Purified honey', 'صاف کیا ہوا شہد', 'صاف شوي شات'),
    ('سُقُوا', 'They are given to drink', 'انھیں پلایا جائے گا', 'ورته به وڅښول شي'),
    ('أَمْعَاءَهُمْ', 'Their bowels', 'ان کی آنتیں', 'د هغوی کولمې'),
    ('فَأَوْلَىٰ لَهُمْ', 'So woe to them', 'تو اُن کے لیے بربادی ہے', 'نو د هغوی لپاره بربادي ده'),
    ('أَضْغَانَهُمْ', 'Their hidden rancour', 'اُن کے چھپے ہوئے کینے', 'د هغوی پټې کینې'),
    ('يَبْخَلُ', 'He is miserly', 'وہ بخل کرتا ہے', 'بخل کوي'),
]


def p154():
    b = Builder()
    L(b, [('Not considering the words of the Holy Prophet (peace and blessings of Allah be upon him) worthy of attention, mocking them and treating them with carelessness is the conduct of the hypocrites. Allah Almighty sets a seal on their hearts, for such people follow their own desires.', 'نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی باتوں کو قابلِ توجہ نہ سمجھنا، ان کا استہزاء کرنا اور ان سے لاپرواہی برتنا منافقین کا طرزِ عمل ہے۔ اللہ تعالیٰ ان کے دلوں پر مہر لگا دیتا ہے کہ ایسے لوگ اپنی خواہشات کے پیچھے چلتے ہیں۔', 'د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم خبرې د پام وړ نه ګڼل، پرې ټوکې کول او ترې بې‌پروايي کول د منافقانو چلند دی؛ الله تعالی د هغوی پر زړونو مهر لګوي، ځکه چې دا ډول خلک د خپلو غوښتنو پسې ځي.'),
          ('Those who walk on the straight path and adopt the path of guidance, Allah Almighty increases their guidance and grants them further ability for piety. The world is the abode of trial. In it Allah Almighty tests human beings in various ways so that it becomes manifest who is His sincere servant and who is a hypocrite.', 'جو لوگ راہِ راست پر چلتے ہیں اور ہدایت کا راستہ اختیار کرتے ہیں، اللہ تعالیٰ ان کی ہدایت میں اضافہ فرما کر انھیں تقویٰ کی مزید توفیق عطا فرماتا ہے۔ دنیا دار الامتحان ہے۔ اس میں اللہ تعالیٰ انسانوں کو مختلف طریقوں سے آزماتا ہے تاکہ ظاہر ہو جائے کہ کون اس کا مخلص بندہ ہے اور کون منافق۔', 'هغه کسان چې پر سمه لار ځي او د هدایت لار غوره کوي، الله تعالی یې په هدایت کې زیاتوالی کوي او د تقوا نور توفیق ورکوي. دنیا د ازموینې ځای دی؛ په هغه کې الله تعالی انسانان په بېلابېلو طریقو ازمویي تر څو ښکاره شي چې څوک یې مخلص بنده دی او څوک منافق.')])
    VOC(b, 'mq12-l15-vocab', VOCAB)
    BOOK.save(154, [(15, rec(b, 15, 154, 154))], issues=[{'id': 'mq12-pdf154', 'unit': 15, 'printedPage': 151,
               'description': 'Knowledge points continued from p.150. Four-column vocabulary rendered as one two-column table (22 rows). Lower part of p.151 blank.'}])


if __name__ == '__main__':
    p154()
