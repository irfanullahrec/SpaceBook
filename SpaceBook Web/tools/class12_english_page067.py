"""PDF67 (printed 121–122): 'Technical Education' (Frank F. Islam, Daily Times 2018 — modern copyrighted) continued: paragraph-wise summary."""
from class12_book_common import Book, Builder

BOOK = Book('english')
r = Builder()
P = [
    ('TVET helps fight unemployment and poverty and has even been called a remedy for terrorism and crime. Pakistan needs policies that are not only relevant but implementable, since good policies often fail at the stage of implementation.',
     'ٹی ویٹ بے روزگاری اور غربت سے نمٹنے میں مدد دیتی ہے اور اسے دہشت گردی اور جرائم کا علاج بھی کہا گیا ہے۔ پاکستان کو ایسی پالیسیاں درکار ہیں جو نہ صرف متعلقہ بلکہ قابلِ عمل بھی ہوں، کیونکہ اچھی پالیسیاں اکثر عمل درآمد کے مرحلے پر ناکام ہو جاتی ہیں۔',
     'TVET د بې‌کارۍ او بېوزلۍ پر وړاندې مرسته کوي او حتی د ترهګرۍ او جرمونو درمل هم بلل شوی. پاکستان داسې پالیسیو ته اړتیا لري چې نه یوازې اړوندې بلکې د پلي کېدو وړ هم وي، ځکه ښې پالیسۍ اکثرا د پلي کولو په پړاو کې پاتې راځي.'),
    ('Pakistan should learn from Japan and Germany, which rebuilt their economies after World War II by focusing on technical and vocational education; in Germany about a third of secondary-school graduates enter vocational training and about half of the workforce is trained in the VET system.',
     'پاکستان کو جاپان اور جرمنی سے سیکھنا چاہیے جنہوں نے دوسری جنگِ عظیم کے بعد فنی اور پیشہ ورانہ تعلیم پر توجہ دے کر اپنی معیشتیں دوبارہ تعمیر کیں؛ جرمنی میں ثانوی اسکول کے تقریباً ایک تہائی فارغ التحصیل پیشہ ورانہ تربیت میں جاتے ہیں اور تقریباً آدھی افرادی قوت وی ای ٹی نظام میں تربیت یافتہ ہے۔',
     'پاکستان باید له جاپان او جرمني زده کړه وکړي چې له دویمې نړیوالې جګړې وروسته یې پر تخنیکي او مسلکي زده کړه د تمرکز له لارې خپل اقتصادونه بیا جوړ کړل؛ په جرمني کې د ثانوي ښوونځي شاوخوا درېیمه برخه فارغان مسلکي روزنې ته ځي او نږدې نیمایي کاري ځواک په VET سیسټم کې روزل شوی.'),
    ('Quaid-e-Azam Muhammad Ali Jinnah, in his speech at the Dhaka University Convocation (24 March 1948), urged students to turn to technical fields, saying there is no shame in manual work and that the country badly needs technically qualified people.',
     'قائدِ اعظم محمد علی جناح نے ڈھاکہ یونیورسٹی کے جلسۂ تقسیمِ اسناد (24 مارچ 1948) میں اپنی تقریر میں طلبہ پر زور دیا کہ وہ فنی شعبوں کی طرف آئیں، اور کہا کہ ہاتھ سے کام کرنے میں کوئی شرم نہیں اور ملک کو تکنیکی طور پر اہل لوگوں کی شدید ضرورت ہے۔',
     'قائد اعظم محمد علي جناح د ډاکې پوهنتون د فراغت په غونډه (د 1948 د مارچ 24) کې په خپله وینا کې زده کوونکي وهڅول چې تخنیکي برخو ته مخه کړي، ویې ویل چې په لاسي کار کې هېڅ شرم نشته او هېواد تخنیکي وړ خلکو ته سخته اړتیا لري.'),
    ('The present situation is discouraging: Pakistan needs about a million skilled workers a year but has only about 300,000; only about 16 per cent of young people complete secondary education, so most of the labour force has little education or skill.',
     'موجودہ صورتِ حال حوصلہ شکن ہے: پاکستان کو سالانہ تقریباً دس لاکھ ہنرمند کارکن درکار ہیں لیکن صرف تقریباً تین لاکھ ہیں؛ صرف تقریباً 16 فیصد نوجوان ثانوی تعلیم مکمل کرتے ہیں، اس لیے زیادہ تر افرادی قوت کے پاس بہت کم تعلیم یا ہنر ہے۔',
     'اوسنی حالت مایوسوونکی دی: پاکستان په کال کې شاوخوا یو میلیون ماهرو کارګرانو ته اړتیا لري خو یوازې شاوخوا 300,000 لري؛ یوازې شاوخوا 16 سلنه ځوانان ثانوي زده کړې بشپړوي، نو ډېری کاري ځواک لږه زده کړه یا مهارت لري.'),
    ('Other problems include a mismatch between the skills needed and those available, courses that do not respond to the market, weak links with industry, outdated facilities, a shortage of trained teachers, low financial returns that make vocational education unattractive, few scholarships, and a social bias towards university degrees.',
     'دیگر مسائل میں درکار اور دستیاب مہارتوں کے درمیان عدم مطابقت، منڈی کے مطابق نہ ہونے والے کورسز، صنعت سے کمزور روابط، فرسودہ سہولیات، تربیت یافتہ اساتذہ کی کمی، کم مالی فوائد جو پیشہ ورانہ تعلیم کو غیر پرکشش بناتے ہیں، کم وظائف اور یونیورسٹی کی ڈگریوں کی طرف سماجی رجحان شامل ہیں۔',
     'نورې ستونزې د اړینو او شته مهارتونو ترمنځ ناسمون، له بازار سره نابرابر کورسونه، له صنعت سره کمزورې اړیکې، زړې اسانتیاوې، د روزل شویو ښوونکو کمښت، ټیټې مالي ګټې چې مسلکي زده کړه نا زړه‌راښکونکې کوي، لږ بورسونه او د پوهنتون سندونو ته ټولنیز تمایل دي.'),
    ('The writer recommends expanding and upgrading the TVET system, linking it clearly with general education, introducing vocational subjects at school level with subsidies and stipends, and steadily improving the quality of vocational education and training.',
     'مصنف ٹی ویٹ نظام کو وسعت دینے اور بہتر بنانے، اسے عمومی تعلیم سے واضح طور پر جوڑنے، اسکول کی سطح پر سبسڈی اور وظائف کے ساتھ پیشہ ورانہ مضامین متعارف کرانے اور پیشہ ورانہ تعلیم و تربیت کے معیار کو مسلسل بہتر بنانے کی سفارش کرتا ہے۔',
     'لیکوال وړاندیز کوي چې د TVET سیسټم پراخ او لوړ شي، له عمومي زده کړې سره په روښانه ډول وتړل شي، د ښوونځي په کچه د سبسایډي او معاشونو سره مسلکي مضامین معرفي شي، او د مسلکي زده کړې او روزنې کیفیت په دوامداره توګه ښه شي.'),
]
for x in P: r.p(*x)
rd = BOOK.record(r, 'eng12-u13-text-b', 'Reading text — summary (2)', 'متن — خلاصہ (2)', 'متن — لنډیز (2)', 67, [121, 122])
rd['sourceGap'] = 'Modern copyrighted newspaper article (Frank F. Islam, Daily Times, 8 Dec 2018); paragraph-wise summary, not verbatim.'
rd['sourceCoverIllustrationReview'] = 'Workshop photograph is decorative; not reproduced.'

if __name__ == '__main__':
    BOOK.save(67, [(13, rd)], issues=[{'id': 'eng12-u13-copyright', 'unit': 13, 'printedPage': 123, 'description': 'Reading text “Technical Education” is credited (p123) to Frank F. Islam, Daily Times, 8 December 2018 — a modern copyrighted article; the app carries a paragraph-wise summary with a sourceGap note instead of the verbatim text. Glossary, questions and exercises are reproduced in full.'}])
