"""Mutalia-e-Quran XII PDF196: p.193 — Lesson 20 exercise Q3 (3b), activities, teachers' guidance. Run: python class12_quran_page196.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, ACT, TCH, words


def p196():
    b = Builder()
    AR(b, f'(3b) {words(59, 21)}', 'What greatness of the Qur\'an-e-Hakim has been stated in the verse?', 'آیت کریمہ میں قرآنِ حکیم کی کیا عظمت بیان کی گئی ہے؟', 'په آیت کې د قرآن حکیم کومه عظمت بیان شوې؟')
    b.h(*ACT)
    L(b, [('Mal-e-fay\' is mentioned in Surah al-Hashr. Find out its details from your teachers.', 'سُوْرَةُ الْحَشْرِ میں مالِ فے کا تذکرہ ہے۔ اساتذہ کرام سے اس کی تفصیل معلوم کریں۔', 'په سورة الحشر کې د مال فیء یادونه ده؛ له ښوونکو یې تفصیل معلوم کړئ.'),
          ('In Surah al-Hashr such people have been praised who, despite being in need themselves, prefer others over themselves. How can you act upon this? Write its possible forms.', 'سُوْرَةُ الْحَشْرِ میں ایسے لوگوں کی تعریف کی گئی ہے جو باوجود محتاج ہونے کے دوسروں کو خود پر ترجیح دیتے ہیں۔ اس پر آپ کیسے عمل کر سکتے ہیں۔ اس کی ممکنہ صورتیں تحریر کریں۔', 'په سورة الحشر کې د داسې خلکو ستاینه شوې چې د اړتیا سره سره نور پر ځان غوره بولي؛ تاسو پرې څنګه عمل کولی شئ؟ د هغه ممکنه بڼې ولیکئ.'),
          ('Memorise orally, with translation, the Asma\' al-Husna mentioned in Surah al-Hashr.', 'سُوْرَةُ الْحَشْرِ میں جن اسماء الحسنیٰ کا تذکرہ ہے ان کو ترجمہ کے ساتھ زبانی یاد کریں۔', 'په سورة الحشر کې چې کوم اسماء الحسنی یاد شوي، هغه له ژباړې سره په یاد کړئ.')])
    b.h(*TCH)
    L(b, [('Tell the students details concerning the exile of the Banu Nadir and have them prepare a list of the breaches of covenant by the Jews.', 'بنو نضیر کی جلاوطنی کے حوالے سے طلبہ کو تفصیلات بتا کر یہود کی بدعہدیوں کی فہرست تیار کرائیں۔', 'زده‌کوونکو ته د بنو نضیر د جلاوطنۍ په اړه تفصیلات ووایئ او د یهودو د ژمنه‌ماتیو لړلیک ترې جوړ کړئ.'),
          ('Have an essay prepared on obedience to the Messenger (peace and blessings of Allah be upon him) and hold a discussion on it.', 'اطاعتِ رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم پر مضمون تیار کرا کر اس پر مذاکرہ کرائیں۔', 'د رسول صلی الله علیه وعلی آله واصحابه وسلم پر اطاعت مقاله جوړه کړئ او پرې بحث وکړئ.'),
          ('Explain the important principle of the distribution of wealth that has been stated in Surah al-Hashr.', 'سُوْرَةُ الْحَشْرِ میں دولت کی تقسیم کا جو اہم اصول بیان کیا گیا ہے اس کی وضاحت کریں۔', 'په سورة الحشر کې د شتمنۍ د وېش کوم مهم اصل چې بیان شوی، هغه روښانه کړئ.')])
    BOOK.save(196, [(20, rec(b, 20, 196, 196, kind='exercise'))], complete_units=[20], issues=[{'id': 'mq12-pdf196', 'unit': 20, 'printedPage': 193,
               'description': 'Lower half of p.193 blank. Quoted verses drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p196()
