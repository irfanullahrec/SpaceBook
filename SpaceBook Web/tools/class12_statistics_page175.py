"""PDF175–176: About the Author; hadith page; back cover (National Anthem, printer/code/quantity). Book complete."""
from class12_statistics_common import Builder, save

a = Builder()
a.h('About the Author', 'مصنف کے بارے میں', 'د لیکوال په اړه')
a.p('Jamal Shah is Professor of Statistics. He was born in 1964 in Mangah, District Mardan. He got his early education from Government higher secondary school Dargai Mangah district Charsadda. He did F.Sc. from Government postgraduate college Mardan, B.Sc. from Government postgraduate Jehanzeb College Saidu Sharif Swat. In 1988, from university of Peshawar, he received his M.Sc. Statistics degree and stood third in his batch.',
    'جمال شاہ شماریات کے پروفیسر ہیں۔ وہ 1964 میں منگاہ، ضلع مردان میں پیدا ہوئے۔ انہوں نے ابتدائی تعلیم گورنمنٹ ہائر سیکنڈری اسکول درگئی منگاہ ضلع چارسدہ سے حاصل کی۔ ایف ایس سی گورنمنٹ پوسٹ گریجویٹ کالج مردان سے اور بی ایس سی گورنمنٹ پوسٹ گریجویٹ جہانزیب کالج سیدو شریف سوات سے کی۔ 1988 میں پشاور یونیورسٹی سے ایم ایس سی شماریات کی ڈگری حاصل کی اور اپنے بیچ میں تیسری پوزیشن حاصل کی۔',
    'جمال شاه د احصایې پروفیسر دی. هغه په 1964 کې د مردان ولسوالۍ په منګاه کې زېږېدلی. لومړنۍ زده کړې یې د چارسدې ولسوالۍ د درګۍ منګاه له دولتي لوړ ثانوي ښوونځي ترلاسه کړې. F.Sc. یې له دولتي پوسټ ګرېجویټ کالج مردان، او B.Sc. یې له دولتي پوسټ ګرېجویټ جهانزېب کالج سیدو شریف سوات څخه وکړ. په 1988 کې یې د پېښور له پوهنتون څخه د احصایې M.Sc. سند ترلاسه کړ او په خپله ډله کې درېیم شو.')
a.p('He started his service in December, 1988 as Lecturer in statistics from Government Khushal Khan Khattak college Akora Khattak district Nowshera. He remained chairman department of Statistics, Government postgraduate college Mansehra and Abbottabad for many years. Presently he is working as Principal, Govt. Degree college, Zaida Swabi. The author has a vast teaching experience of 30 years in the subject statistics at Inter, Bachelor and Master level.',
    'انہوں نے دسمبر 1988 میں گورنمنٹ خوشحال خان خٹک کالج اکوڑہ خٹک ضلع نوشہرہ سے شماریات کے لیکچرر کی حیثیت سے ملازمت شروع کی۔ وہ کئی سال گورنمنٹ پوسٹ گریجویٹ کالج مانسہرہ اور ایبٹ آباد کے شعبۂ شماریات کے چیئرمین رہے۔ اس وقت وہ گورنمنٹ ڈگری کالج زیدہ صوابی کے پرنسپل کے طور پر کام کر رہے ہیں۔ مصنف کو انٹر، بیچلر اور ماسٹر سطح پر شماریات کے مضمون کی تدریس کا 30 سال کا وسیع تجربہ ہے۔',
    'هغه په ډسمبر 1988 کې د نوښار ولسوالۍ د اکوړه خټک له دولتي خوشحال خان خټک کالج څخه د احصایې د لکچرر په توګه خپله دنده پیل کړه. هغه د ډېرو کلونو لپاره د مانسهرې او ایبټ اباد د دولتي پوسټ ګرېجویټ کالج د احصایې د څانګې مشر و. اوس مهال هغه د صوابي زیده دولتي ډګري کالج د پرنسپل په توګه کار کوي. لیکوال د انټر، بیچلر او ماسټر په کچه د احصایې په مضمون کې د 30 کلونو پراخه تدریسي تجربه لري.')
a.p('رشوت لینے والا اور رشوت دینے والا دونوں جہنمی ہیں۔ (حدیث نبوی ﷺ)', 'رشوت لینے والا اور رشوت دینے والا دونوں جہنمی ہیں۔ (حدیث نبوی ﷺ)', 'رشوت لینے والا اور رشوت دینے والا دونوں جہنمی ہیں۔ (حدیث نبوی ﷺ)')
a.p('(Translation: The one who takes a bribe and the one who gives a bribe are both in Hell. — Hadith of the Prophet ﷺ)', '(اصل متن: رشوت لینے والا اور رشوت دینے والا دونوں جہنمی ہیں۔ — حدیث نبوی ﷺ)', '(ژباړه: رشوت اخیستونکی او رشوت ورکوونکی دواړه دوزخیان دي. — نبوي حدیث ﷺ)')
au = a.build('stat12-about-author', 'About the Author', 'مصنف کے بارے میں', 'د لیکوال په اړه', 175, [])

b = Builder()
b.h('Back cover: National Anthem and printing details', 'پچھلا سرورق: قومی ترانہ اور طباعت کی تفصیلات', 'شاتنۍ پوښ: ملي سرود او د چاپ جزییات')
b.h('قومی ترانہ', 'قومی ترانہ', 'قومی ترانہ')
for ln in ['پاک سرزمین شاد باد — کشورِ حسین شاد باد', 'تو نشانِ عزمِ عالی شان — ارضِ پاکستان', 'مرکزِ یقین شاد باد', 'پاک سرزمین کا نظام — قوتِ اخوتِ عوام',
           'قوم، ملک، سلطنت — پائندہ تابندہ باد', 'شاد باد منزلِ مراد', 'پرچمِ ستارہ و ہلال — رہبرِ ترقی و کمال', 'ترجمانِ ماضی شانِ حال — جانِ استقبال', 'سایۂ خدائے ذوالجلال']:
    b.p(ln, ln, ln)
b.p('Printed by: Etihad … | Code No.: PSP/EHD-59…-227-1920(0) | Quabtity: 11397 (bottom line partly cut off in the scan)', 'طابع: Etihad … | کوڈ نمبر: PSP/EHD-59…-227-1920(0) | تعداد: 11397 (اسکین میں نچلی سطر جزوی طور پر کٹی ہوئی ہے)', 'چاپوونکی: Etihad … | کوډ شمېره: PSP/EHD-59…-227-1920(0) | شمېر: 11397 (په سکین کې لاندې کرښه جزوي پرې شوې)')
bc = b.build('stat12-back-cover', 'Back cover: National Anthem and printing details', 'پچھلا سرورق: قومی ترانہ اور طباعت کی تفصیلات', 'شاتنۍ پوښ: ملي سرود او د چاپ جزییات', 176, [])
bc['sourceCoverIllustrationReview'] = 'Fort-gate photograph on the back cover is decorative and not reproduced. The National Anthem is shown in Urdu in all language views.'
issues = [{'id': 'stat12-back-cover-cut', 'unit': 9, 'printedPage': None, 'description': 'Back cover bottom line (printer name, code number, quantity) is partly cut off in the scan; visible parts transcribed, “Quabtity” typo retained. The Urdu hadith page (PDF175 right) is reproduced in Urdu with English/Pashto translations.'}]

if __name__ == '__main__':
    save(175, [(9, au)], issues=issues)
    save(176, [(9, bc)])
