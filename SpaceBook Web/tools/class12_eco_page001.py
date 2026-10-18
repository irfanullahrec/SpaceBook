"""Economics XII front matter: PDF1 cover; PDF2 download-site advertisement (excluded); PDF3 imprint (R) + prayer (L, p.iii); PDF4 preface (R, p.iv)
+ testimonials (L, p.v); PDF5–7 testimonials (pp.vi–x) + contents (p.xi); PDF8 contents (pp.xii–xiii). PDF9 (contents p.xiv + chapter 1) is in page009.
Run: python class12_eco_page001.py N (1, 3–8)."""
import sys
from class12_eco_common import BOOK, Builder

FM = ('Front matter', 'ابتدائیہ', 'سریزه')
BANNER = 'The download-site banners (“Downloaded from awazeinqilab.com”, WhatsApp number, download notice) above and below every scan and the diagonal watermark are third-party additions and are excluded throughout.'


def p1():
    b = Builder()
    b.h('Kitab-e-Maashiyat (Book of Economics), Part Two — for Intermediate Economics Paper Two', 'کتابِ معاشیات — حصہ دوم — انٹرمیڈیٹ اکنامکس پرچہ دوم کے لئے', 'کتاب معاشیات (د اقتصاد کتاب) — دویمه برخه — د انټرمیډیټ اقتصاد دویم پرچې لپاره')
    for x in [('(Newly revised edition) — Subjective and Objective', '(نیا ترمیم شدہ ایڈیشن) — انشائی (Subjective) و معروضی (Objective)', '(نوې تعدیل شوې نسخه) — انشايي (Subjective) او معروضي (Objective)'),
              ('Professor Muhammad Manzoor Ali Sheikh; revision and additions: Professor Muhammad Jamil', 'پروفیسر محمد منظور علی شیخ — ترمیم و اضافہ: پروفیسر محمد جمیل', 'پروفیسر محمد منظور علي شیخ — تعدیل او زیاتوالی: پروفیسر محمد جمیل'),
              ('Ilmi (publisher’s mark)', 'علمی', 'علمي (د خپروونکي نښه)')]:
        b.p(*x)
    H = (['Head of government', 'Growth rate (%)'], ['سربراہ', 'شرحِ ترقی (%)'], ['مشر', 'د ودې کچه (٪)'])
    rows = [['Ziaul Haq', '5.88'], ['Ayub Khan', '5.82'], ['Pervez Musharraf', '5.14'], ['Benazir Bhautto', '5.08'], ['Zulifikar Ali Bhutto', '4.83'], ['Yahya Khan', '4.38'], ['Nawaz Sharif', '4.06'],
            ['Sikandar Mirza', '3.02'], ['Ghulam Muhammad', '2.95'], ['Asif Ali Zardari', '2.62']]
    b.table('eco12-cover-growth', H[0], rows, H[1], H[2], rows, rows)
    r = BOOK.record(b, 'eco12-fm-cover', 'Front cover', 'سرورق', 'پښتۍ', 1, [None], unit_title=FM)
    r['sourceNote'] = 'The cover bar chart “شرح ترقی” (growth rate by head of government; names printed in English) is reproduced as a structured table with its printed values and spellings.'
    r['sourceCoverIllustrationReview'] = 'Photographs of wheat ears and machine gears and the publisher’s logo are decorative.'
    BOOK.save(1, [('FM', r)], issues=[{'id': 'eco12-pdf001', 'unit': 'FM', 'printedPage': None, 'description': BANNER + ' The cover chart prints “Benazir Bhautto”, “Zulifikar Ali Bhutto”. A small owner pencil mark is excluded.'}])


def p3():
    b = Builder()
    for x in [('Ilmi Maashiyat (Part Two) — Professor Muhammad Manzoor Ali Sheikh', 'علمی معاشیات (حصہ دوم) — پروفیسر محمد منظور علی شیخ', 'علمي معاشیات (دویمه برخه) — پروفیسر محمد منظور علي شیخ'),
              ('Publisher: Ilmi Kitab Khana, Kabeer Street, Urdu Bazar, Lahore (Pakistan); www.ilmikitabkhana.com', 'ناشر: علمی کتاب خانہ، کبیر سٹریٹ، اردو بازار، لاہور (پاکستان)؛ www.ilmikitabkhana.com', 'خپروونکی: علمي کتاب خانه، کبیر سټریټ، اردو بازار، لاهور (پاکستان)؛ www.ilmikitabkhana.com'),
              ('Copyright 2019-20, Ilmi Kitab Khana (Pakistan). All rights reserved. Printing, recording or transmitting any part of this published material by photocopying or any other method without the written permission of the publisher is against the law; legal action will be taken against the offender under civil and criminal procedure, which may involve damages, fine and/or imprisonment, so take care.',
               'حقوقِ اشاعت 2019-20ء علمی کتاب خانہ (پاکستان)۔ جملہ حقوق محفوظ ہیں۔ اس شائع کردہ مواد کا کوئی بھی حصہ عکسی، میکانی، فوٹو کاپی یا کسی دیگر طریقہ سے ناشر کی تحریری اجازت کے بغیر چھاپنا، ریکارڈ کرنا یا ترسیل کرنا خلافِ قانون ہے۔ اس فعل کے مرتکب فرد/افراد کے خلاف ضابطہ دیوانی و فوجداری کے تحت قانونی کارروائی عمل میں لائی جائے گی جو ہرجانہ/جرمانہ و سزا یا دونوں ہو سکتی ہیں لہٰذا احتیاط کریں۔',
               'د خپرولو حقونه 2019-20 علمي کتاب خانه (پاکستان). ټول حقونه خوندي دي. د دې خپاره شوي موادو هره برخه په عکسي، میخانیکي، فوټوکاپي یا بله طریقه د خپروونکي له لیکلې اجازې پرته چاپول، ثبتول یا لېږدول له قانون سره مخالف دي؛ د دې کار د کوونکي پر وړاندې به د مدني او جزايي ضابطې له مخې قانوني اقدام کېږي چې تاوان/جریمه او سزا یا دواړه کېدای شي، نو احتیاط وکړئ.'),
              ('Trade mark: “Ilmi”, Ilmi Kitab Khana and its logo are registered trade marks of Ilmi Kitab Khana, Pakistan; they cannot be used without written permission.', 'ٹریڈ مارک: علمی، علمی کتاب خانہ اور اُس کا لوگو علمی کتاب خانہ، پاکستان کے رجسٹرڈ ٹریڈ مارک ہیں، یہ تحریری اجازت کے بغیر استعمال نہیں ہو سکتے۔', 'سوداګریزه نښه: علمي، علمي کتاب خانه او د هغې نښان د علمي کتاب خانې، پاکستان ثبت شوې سوداګریزې نښې دي؛ له لیکلې اجازې پرته نه شي کارول کېدای.'),
              ('Publisher’s note: before printing, full care was taken that the material be free from every kind of error, yet some error may have remained unintentionally. This institution, the publisher, compiler and author will not be responsible for any such error. If the published material causes or may cause any loss to any person or persons, the publisher, compiler and author will not be responsible for such loss. The author/compiler tried his best that the material be free from every kind of error; even so, being human, error is possible. If any error comes to the reader’s notice, kindly inform this institution so that it can be corrected in the next edition.',
               'عرضِ ناشر: چھپائی سے قبل اس امر کا پورا خیال رکھا گیا کہ مواد ہر قسم کی غلطی سے مبرا ہو تاہم اس بات کا امکان ہو سکتا ہے کہ کوئی غلطی نادانستہ طور پر رہ گئی ہو۔ ادارہ ہٰذا ناشر، مؤلف اور مصنف اس قسم کی غلطی کے ذمہ دار نہ ہوں گے۔ اگر شائع شدہ مواد سے کسی فرد یا افراد کو کسی قسم کا نقصان پہنچے یا پہنچنے کا احتمال ہو تو بھی ناشر، مؤلف اور مصنف اس قسم کے نقصان وغیرہ کے ذمہ دار نہ ہوں گے۔ مصنف/مؤلف کی پوری کوشش رہی کہ مواد ہر طرح کی غلطی سے پاک ہو تاہم اس کے باوجود بھی بتقاضائے بشریت غلطی کا امکان ہو سکتا ہے۔ اگر قاری کی نظر سے کوئی بھی غلطی گزرے تو براہِ کرم ادارہ ہٰذا کو ضرور مطلع کریں تاکہ آئندہ اشاعت میں اس کی تصحیح ہو سکے۔',
               'د خپروونکي وړاندیز: له چاپ مخکې پوره پام شوی چې مواد له هر ډول تېروتنې پاک وي، خو امکان لري چې کومه تېروتنه په ناپوهۍ پاتې شوې وي. دا اداره، خپروونکی، مؤلف او لیکوال به د داسې تېروتنې مسؤل نه وي. که له خپاره شویو موادو کوم کس یا کسانو ته کوم زیان ورسېږي یا د رسېدو احتمال ولري، بیا هم خپروونکی، مؤلف او لیکوال به د داسې زیان مسؤل نه وي. د لیکوال/مؤلف پوره هڅه وه چې مواد له هر ډول تېروتنې پاک وي، خو بیا هم د بشري طبیعت له مخې د تېروتنې امکان شته. که لوستونکي ته کومه تېروتنه وګورئ، مهرباني وکړئ دې ادارې ته خبر ورکړئ ترڅو په راتلونکې چاپ کې سمه شي.'),
              ('For further information contact these numbers — Lahore: (042)37353510-37248129; Islamabad: (051)2656050 or e-mail: contactus@ilmikitabkhana.com. Printed & Bound in Pakistan. Price: Rs. 250/-', 'دیگر معلومات کے لیے ان نمبرز پر رابطہ کریں۔ لاہور: (042)37353510-37248129 اسلام آباد: (051)2656050 یا ای میل: contactus@ilmikitabkhana.com۔ Printed & Bound in Pakistan۔ قیمت: -/250 روپے', 'د نورو معلوماتو لپاره له دې شمېرو اړیکه ونیسئ — لاهور: (042)37353510-37248129؛ اسلام آباد: (051)2656050 یا برېښنالیک: contactus@ilmikitabkhana.com. Printed & Bound in Pakistan. بیه: -/250 روپۍ')]:
        b.p(*x)
    r1 = BOOK.record(b, 'eco12-fm-imprint', 'Imprint', 'طباعتی تفصیلات', 'د چاپ جزییات', 3, [None])
    d = Builder()
    d.h('Prayer', 'دُعا', 'دعا')
    d.p('“Our Lord, so forgive us our sins and remove from us our misdeeds and cause us to die with the righteous.” (Aal-e-Imran 3:193) “You are our Protector, so forgive us and have mercy upon us; and You are the best of those who forgive.” (Al-A‘raf 7:155)',
        'رَبَّنَا فَاغْفِرْ لَنَا ذُنُوْبَنَا وَ كَفِّرْ عَنَّا سَيِّاٰتِنَا وَ تَوَفَّنَا مَعَ الْاَبْرَارِ ۝۱۹۳ اَنْتَ وَلِيُّنَا فَاغْفِرْ لَنَا وَ ارْحَمْنَا وَ اَنْتَ خَيْرُ الْغٰفِرِيْنَ ۝۱۵۵',
        '«زموږ ربه! زموږ ګناهونه وبښه، زموږ بدۍ له موږ لرې کړه او له نېکانو سره مو مړه کړه.» (آل عمران ۳: ۱۹۳) «ته زموږ ساتونکی یې، نو موږ وبښه او پر موږ رحم وکړه، او ته تر ټولو غوره بښونکی یې.» (الاعراف ۷: ۱۵۵)')
    d.p('O our Lord, the faults that have been committed by us, pass over them; remove the evils that are in us and make our end with good people. You alone are our Patron, so forgive us and have mercy on us. You are the most forgiving of all.',
        'اے ہمارے رب، جو قصور ہم سے ہوئے ہیں اُن سے درگزر فرما، جو بُرائیاں ہم میں ہیں انھیں دُور کر دے اور ہمارا خاتمہ نیک لوگوں کے ساتھ کر۔ ہمارے سرپرست تو آپ ہی ہیں، پس ہمیں معاف فرما دیجیے اور ہم پر رحم فرمایئے۔ آپ سب سے بڑھ کر معاف فرمانے والے ہیں۔',
        'ای زموږ ربه، کومې تېروتنې چې له موږ شوې، تېر یې شه؛ کومې بدۍ چې په موږ کې دي، لرې یې کړه او زموږ پای له نېکو خلکو سره کړه. زموږ سرپرست یوازې ته یې، نو موږ وبښه او پر موږ رحم وکړه. ته تر ټولو ډېر بښونکی یې.')
    r2 = BOOK.record(d, 'eco12-fm-prayer', 'Prayer', 'دُعا', 'دعا', 3, ['iii'])
    BOOK.save(3, [('FM', r1), ('FM', r2)], issues=[{'id': 'eco12-pdf003', 'unit': 'FM', 'printedPage': 'iii', 'description': 'The verse numbers 193 and 155 are printed small at the verse ends (Aal-e-Imran 3:193, Al-A‘raf 7:155); the Arabic is retained.'}])


ENDORSE = [
 # (name EN, name UR, institution EN, institution UR, page)
 ('Prof. Muhammad Mansha Tahir', 'پروفیسر محمد منشاء طاہر صاحب', 'Government College, Gujranwala', 'گورنمنٹ کالج، گوجرانوالہ', 'v'),
 ('Prof. Mehr Muhammad Yousaf', 'پروفیسر مہر محمد یوسف صاحب', 'Government College (University), Sargodha', 'گورنمنٹ کالج (یونیورسٹی) سرگودھا', 'v'),
 ('Prof. Sheikh Abdul Ghaffar', 'پروفیسر شیخ عبدالغفار صاحب', 'Government College, Jhang Road, Faisalabad', 'گورنمنٹ کالج جھنگ روڈ، فیصل آباد', 'v'),
 ('Prof. Khalid Pervez Anjum', 'پروفیسر خالد پرویز انجم صاحب', 'Government S.E. College, Bahawalpur', 'گورنمنٹ ایس۔ای کالج، بہاولپور', 'v'),
 ('Prof. Muhammad Saeed Iqbal', 'پروفیسر محمد سعید اقبال صاحب', 'Government College of Science, Lahore', 'گورنمنٹ کالج آف سائنس، لاہور', 'v'),
 ('Prof. Qazi Waqar Alam', 'پروفیسر قاضی وقار عالم صاحب', 'Government College, Satellite Town, Rawalpindi', 'گورنمنٹ کالج، سیٹلائٹ ٹاؤن، راولپنڈی', 'v'),
 ('Prof. Sheikh Sajid Hassan', 'پروفیسر شیخ ساجد حسن صاحب', 'Government Islamia College, Gujranwala', 'گورنمنٹ اسلامیہ کالج، گوجرانوالہ', 'v'),
 ('Prof. Nazir Ahmad Shibli', 'پروفیسر نذیر احمد شبلی صاحب', 'Government College, Bhakkar', 'گورنمنٹ کالج بھکر', 'v'),
 ('Prof. Munir Khalid', 'پروفیسر منیر خالد صاحب', 'Government College of Science, Lahore', 'گورنمنٹ کالج آف سائنس لاہور', 'v'),
 ('Prof. Anwar Ali', 'پروفیسر انور علی صاحب', 'Government Degree College, Alipur', 'گورنمنٹ ڈگری کالج، علی پور', 'v'),
 ('Prof. Muhammad Sarfraz', 'پروفیسر محمد سرفراز صاحب', 'Government College of Science, Multan', 'گورنمنٹ کالج آف سائنس، ملتان', 'v'),
 ('Prof. Dr. Bashir Ahmad Hilmi', 'پروفیسر ڈاکٹر بشیر احمد حلمی صاحب', 'Government College (Samanabad), Faisalabad', 'گورنمنٹ کالج (سمن آباد) فیصل آباد', 'vi'),
 ('Prof. Abdul Salam', 'پروفیسر عبدالسلام صاحب', 'Government College, Multan', 'گورنمنٹ کالج، ملتان', 'vi'),
 ('Prof. Chaudhry Hafeez-ur-Rehman', 'پروفیسر چوہدری حفیظ الرحمٰن صاحب', 'Government College, Sargodha', 'گورنمنٹ کالج سرگودھا', 'vi'),
 ('Prof. Amjad Hussain Malik', 'پروفیسر امجد حسین ملک صاحب', 'Government College, Asghar Mall, Rawalpindi', 'گورنمنٹ کالج، اصغر مال، راولپنڈی', 'vi'),
 ('Prof. Muhammad Tariq Hassan', 'پروفیسر محمد طارق حسن صاحب', 'Government Degree College, Baghdad Road, Bahawalpur', 'گورنمنٹ ڈگری کالج، بغداد روڈ بہاولپور', 'vi'),
 ('Prof. Chaudhry Abdul Wahid', 'پروفیسر چوہدری عبدالواحد صاحب', 'Government College, Jhelum', 'گورنمنٹ کالج جہلم', 'vi'),
 ('Prof. Muhammad Ayub', 'پروفیسر محمد ایوب صاحب', 'Government College, Rahim Yar Khan', 'گورنمنٹ کالج، رحیم یار خاں', 'vi'),
 ('Prof. Muhammad Ishfaq Khan', 'پروفیسر محمد اشفاق خاں صاحب', 'Government College, Dera Ghazi Khan', 'گورنمنٹ کالج ڈیرہ غازی خاں', 'vi'),
 ('Prof. Zahid Sarwar', 'پروفیسر زاہد سرور صاحب', 'Government Degree College, Bochhal Kalan', 'گورنمنٹ ڈگری کالج، بوچھال کلاں', 'vi'),
 ('Prof. Muhammad Zulfiqar', 'پروفیسر محمد ذوالفقار صاحب', 'Government Gordon College, Rawalpindi', 'گورنمنٹ گارڈن کالج، راولپنڈی', 'vi'),
 ('Prof. Arshad Javed', 'پروفیسر ارشد جاوید صاحب', 'Government Inter College, Gujranwala', 'گورنمنٹ انٹر کالج گوجرانوالہ', 'vi'),
 ('Prof. Fayyaz Hussain', 'پروفیسر فیاض حسین صاحب', 'Government Muslim College, Faisalabad', 'گورنمنٹ مسلم کالج، فیصل آباد', 'vi'),
 ('Prof. Muhammad Ikram Ghani', 'پروفیسر محمد اکرام غنی صاحب', 'Government College, Mankera (District Bhakkar)', 'گورنمنٹ کالج منکیرہ (ضلع بھکر)', 'vi'),
 ('Prof. Miss Zahida Shamim', 'پروفیسر مس زاہدہ شمیم صاحبہ', 'Government Model College for Women, Model Town, Lahore', 'گورنمنٹ ماڈل کالج برائے خواتین، ماڈل ٹاؤن، لاہور', 'vii'),
 ('Prof. Mrs. Razia Iqbal', 'پروفیسر مسز رضیہ اقبال صاحبہ', 'Government Islamia College for Women, Tufail Shaheed Road, Lahore Cantt', 'گورنمنٹ اسلامیہ کالج برائے خواتین، طفیل شہید روڈ، لاہور کینٹ', 'vii'),
 ('Prof. Mrs. Munazza Waseem', 'پروفیسر مسز منزہ وسیم صاحبہ', 'Government College for Women, Sadiqabad', 'گورنمنٹ کالج برائے خواتین، صادق آباد', 'vii'),
 ('Prof. Mrs. Nargis Shaheen', 'پروفیسر مسز نرگس شاہین صاحبہ', 'Government College for Women, Bahawalnagar', 'گورنمنٹ کالج برائے خواتین، بہاولنگر', 'vii'),
 ('Prof. Mrs. Rakhshanda Akbar Cheema', 'پروفیسر مسز رخشندہ اکبر چیمہ صاحبہ', 'Government Girls College, Daska', 'گورنمنٹ گرلز کالج، ڈسکہ', 'vii'),
 ('Prof. Mrs. Nuzhat Khurshid', 'پروفیسر مسز نزہت خورشید صاحبہ', 'Government College for Women, Mumtazabad, Multan', 'گورنمنٹ کالج برائے خواتین، ممتاز آباد، ملتان', 'vii'),
 ('Prof. Mrs. Shahida Tahir', 'پروفیسر مسز شاہدہ طاہر صاحبہ', 'Government Degree College for Women, Chiniot', 'گورنمنٹ ڈگری کالج برائے خواتین، چنیوٹ', 'vii'),
 ('Prof. Mrs. Fozia Shaheen', 'پروفیسر مسز فوزیہ شاہین صاحبہ', 'Government Post Graduate College for Women, Bagh (Azad Kashmir)', 'گورنمنٹ پوسٹ گریجوایٹ کالج برائے خواتین، باغ (آزاد کشمیر)', 'vii'),
 ('Prof. Mrs. Razia Gulzar', 'پروفیسر مسز رضیہ گلزار صاحبہ', 'Government College for Women, Attock', 'گورنمنٹ کالج برائے خواتین، اٹک', 'vii'),
 ('Prof. Mrs. Ghulam Zakia', 'پروفیسر مسز غلام زکیہ صاحبہ', 'Government College for Women, Talagang', 'گورنمنٹ کالج برائے خواتین، تلہ گنگ', 'vii'),
 ('Prof. Mrs. Bushra Iqbal', 'پروفیسر مسز بشریٰ اقبال صاحبہ', 'Government College for Women, Marghzar Colony, Gujrat', 'گورنمنٹ کالج برائے خواتین، مرغزار کالونی، گجرات', 'vii'),
 ('Prof. Mrs. Sakina Mustafa', 'پروفیسر مسز سکینہ مصطفیٰ صاحبہ', 'Government Degree College for Women, Haroonabad', 'گورنمنٹ ڈگری کالج برائے خواتین، ہارون آباد', 'vii'),
 ('Prof. Mrs. Batool Gardezi', 'پروفیسر مسز بتول گردیزی صاحبہ', 'Government Degree College for Women, Multan', 'گورنمنٹ ڈگری کالج برائے خواتین، ملتان', 'viii'),
 ('Prof. Miss Talat Hanif', 'پروفیسر مس طلعت حنیف صاحبہ', 'Government College for Women, Okara', 'گورنمنٹ کالج برائے خواتین، اوکاڑہ', 'viii'),
 ('Prof. Mrs. Anwar Shirani', 'پروفیسر مسز انور شیرانی صاحبہ', 'Government College for Women, Taunsa Sharif', 'گورنمنٹ کالج برائے خواتین، تونسہ شریف', 'viii'),
 ('Prof. Miss Farhana Tabassum', 'پروفیسر مس فرحانہ تبسم صاحبہ', 'Government College for Women, Vehari', 'گورنمنٹ کالج برائے خواتین، وہاڑی', 'viii'),
 ('Prof. Mrs. Dilshad Khalida', 'پروفیسر مسز دلشاد خالدہ صاحبہ', 'Government Girls College, Sialkot', 'گورنمنٹ گرلز کالج، سیالکوٹ', 'viii'),
 ('Prof. Mrs. Rashida Kaleem', 'پروفیسر مسز رشیدہ کلیم صاحبہ', 'Government Ayesha College for Women, Timber Market, Lahore', 'گورنمنٹ عائشہ کالج برائے خواتین، ٹمبر مارکیٹ، لاہور', 'viii'),
 ('Prof. Miss Fozia Manzoor', 'پروفیسر مس فوزیہ منظور صاحبہ', 'Government Girls College, Dadyal', 'گورنمنٹ گرلز کالج، ڈڈیال', 'viii'),
 ('Prof. Mrs. Suraya Musarrat Baloch', 'پروفیسر مسز ثریا مسرت بلوچ صاحبہ', 'Government College for Women, Quetta', 'گورنمنٹ کالج برائے خواتین، کوئٹہ', 'viii'),
 ('Prof. Chaudhry Mukhtar Hussain', 'پروفیسر چوہدری مختار حسین صاحب', 'Government Degree College, Dadyal (Azad Kashmir)', 'گورنمنٹ ڈگری کالج ڈڈیال (آزاد کشمیر)', 'viii'),
 ('Prof. Badar Munir Abbasi', 'پروفیسر بدر منیر عباسی صاحب', 'Government Girls College, Hattian Bala, Azad Kashmir', 'گورنمنٹ گرلز کالج، ہٹیاں بالا، آزاد کشمیر', 'viii'),
 ('Prof. Muhammad Ishaq', 'پروفیسر محمد اسحاق صاحب', 'Government College, Tarar Khal', 'گورنمنٹ کالج، تراڑ کھل', 'viii'),
 ('Prof. Dildar Hussain Shad', 'پروفیسر دلدار حسین شاد صاحب', 'Government Inter College, Abbaspur', 'گورنمنٹ انٹر کالج، عباس پور', 'ix'),
 ('Prof. Abdul Rehman Abbasi', 'پروفیسر عبدالرحمٰن عباسی صاحب', 'Government College, Balasar', 'گورنمنٹ کالج، بالسری', 'ix'),
 ('Prof. Muhammad Zubair Sajid', 'پروفیسر محمد زبیر ساجد صاحب', 'Government College, Muzaffarabad', 'گورنمنٹ کالج، مظفر آباد', 'ix'),
 ('Prof. Ashraf Mehmood Khan', 'پروفیسر اشرف محمود خاں صاحب', 'Government Degree College, Mianwali', 'گورنمنٹ ڈگری کالج، میانوالی', 'ix'),
 ('Prof. Chaudhry Muhammad Razzaq', 'پروفیسر چوہدری محمد رزاق صاحب', 'Government Degree College, Dadyal', 'گورنمنٹ ڈگری کالج ڈڈیال', 'ix'),
 ('Prof. Waheed Akhtar', 'پروفیسر وحید اختر صاحب', 'Government College, Mansehra (Khyber PK)', 'گورنمنٹ کالج مانسہرہ (خیبر پی کے)', 'ix'),
 ('Prof. Sardar Muhammad Hameed Tahir', 'پروفیسر سردار محمد حمید طاہر صاحب', 'Government Degree College, Hajeera, Poonch', 'گورنمنٹ ڈگری کالج ہجیرہ، پونچھ', 'ix'),
 ('Prof. Altaf Hussain Awan', 'پروفیسر الطاف حسین اعوان صاحب', 'Government College, Garhi Dupatta', 'گورنمنٹ کالج گڑھی دوپٹہ', 'ix'),
 ('Prof. Muhammad Aslam', 'پروفیسر محمد اسلم صاحب', 'Government Zamindar College, Bhimber Road, Gujrat', 'گورنمنٹ زمیندار کالج، بھمبر روڈ، گجرات', 'ix'),
 ('Prof. Gulyar Khan', 'پروفیسر گلیار خاں صاحب', 'Fatehpur (Swat)', 'فتح پور (سوات)', 'ix'),
 ('Prof. Muhammad Sarfraz Khan', 'پروفیسر محمد سرفراز خاں صاحب', 'Government College, Abbottabad', 'گورنمنٹ کالج، ایبٹ آباد', 'ix'),
 ('Prof. Malik Nasir Dawood', 'پروفیسر ملک ناصر داؤد صاحب', 'Government College, Havelian Cantt', 'گورنمنٹ کالج حویلیاں کینٹ', 'ix–x'),
 ('Prof. Muhammad Asim Iqbal', 'پروفیسر محمد عاصم اقبال صاحب', 'Government College, Khairabad (Mardan)', 'گورنمنٹ کالج خیر آباد (مردان)', 'x'),
 ('Prof. Falak Naz', 'پروفیسر فلک ناز صاحب', 'Government College, Bannu', 'گورنمنٹ کالج بنوں', 'x'),
 ('Prof. Muhammad Nadeem', 'پروفیسر محمد ندیم صاحب', 'Government Post Graduate College, Lakki Marwat', 'گورنمنٹ پوسٹ گریجوایٹ کالج لکی مروت', 'x'),
 ('Prof. Ghulam Hussain Baloch', 'پروفیسر غلام حسین بلوچ صاحب', 'Government Degree College, Sibi (Balochistan)', 'گورنمنٹ ڈگری کالج سبی (بلوچستان)', 'x'),
 ('Prof. Muhammad Akbar Soomro', 'پروفیسر محمد اکبر سومرو صاحب', 'Government College, Usta Muhammad (Balochistan)', 'گورنمنٹ کالج، اوستہ محمد (بلوچستان)', 'x'),
 ('Prof. Ataullah Mengal', 'پروفیسر عطاء اللہ مینگل صاحب', 'Government Degree College, Noshki (Chaghi)', 'گورنمنٹ ڈگری کالج نوشکی (چاغی)', 'x'),
 ('Prof. Zubair Ahmad Buzdar', 'پروفیسر زبیر احمد بزدار صاحب', 'Government College, Kohlu (Balochistan)', 'گورنمنٹ کالج کوہلو (بلوچستان)', 'x'),
 ('Prof. Abdul Wahid Kakar', 'پروفیسر عبدالواحد کاکڑ صاحب', 'Government College, Qila Saifullah, Balochistan', 'گورنمنٹ کالج قلعہ سیف اللہ، بلوچستان', 'x')]


def endorse_block(pdf, pages, part, rows, first=False):
    b = Builder()
    if first:
        b.h('Words of appreciation', 'حرفِ تحسین', 'د ستاینې ټکي')
        b.p('Teachers of economics from colleges across Pakistan commend the author’s books of economics: they say the books are written in easy, fluent and commonly understood language, explain difficult economic terms and theories with simple examples, tables and diagrams, cover the whole syllabus, help students obtain good examination results, and that they therefore recommend these books to their own students; several pray for the author’s health and reward. The endorsers are listed below in the printed order.',
            'پاکستان بھر کے کالجوں کے معاشیات کے اساتذہ مصنف کی معاشیات کی کتب کی تعریف کرتے ہیں: ان کے مطابق یہ کتابیں آسان، سلیس اور عام فہم زبان میں لکھی گئی ہیں، مشکل معاشی اصطلاحات و نظریات کو سادہ مثالوں، گوشواروں اور ڈائیگراموں سے واضح کرتی ہیں، پورے سلیبس پر حاوی ہیں، طلبا کو امتحان میں اچھے نتائج دلاتی ہیں، اس لیے وہ اپنے طلبا کو یہی کتب تجویز کرتے ہیں؛ کئی اساتذہ مصنف کے لیے صحت و اجر کی دعا کرتے ہیں۔ تحسین کرنے والوں کے نام مطبوعہ ترتیب سے ذیل میں درج ہیں۔',
            'د پاکستان په ګوټ ګوټ کې د کالجونو د اقتصاد ښوونکي د لیکوال د اقتصاد کتابونه ستايي: د دوی په وینا دا کتابونه په اسانه، روانه او عام پوهېدونکې ژبه لیکل شوي، سختې اقتصادي اصطلاحګانې او نظریې په ساده بېلګو، جدولونو او ډیاګرامونو روښانه کوي، ټول نصاب رانغاړي، زده‌کوونکو ته په ازموینه کې ښې پایلې ورکوي، له همدې امله دوی خپلو زده‌کوونکو ته همدا کتابونه وړاندیز کوي؛ ډېر ښوونکي د لیکوال لپاره د روغتیا او اجر دعا کوي. د ستاینه کوونکو نومونه په چاپي ترتیب لاندې راغلي دي.')
    H = (['Endorser', 'College', 'Page'], ['نام', 'کالج', 'صفحہ'], ['نوم', 'کالج', 'مخ'])
    b.table(f'eco12-endorse-{part}', H[0], [[e, i, p] for e, u, i, iu, p in rows], H[1], H[2], [[u, iu, p] for e, u, i, iu, p in rows], [[u, iu, p] for e, u, i, iu, p in rows])
    r = BOOK.record(b, f'eco12-fm-endorsements-{part}', f'Words of appreciation ({part})', f'حرفِ تحسین ({part})', f'د ستاینې ټکي ({part})', pdf, pages)
    r['sourceNote'] = ('The “حرفِ تحسین” pages (v–x) are the publisher’s promotional testimonials (66 short recommendations by named teachers). They are given as a structured list of endorsers and '
                       'colleges with a single summary of their common content, rather than as 66 separate blurbs. The Pashto column keeps the Urdu names and college names.')
    return r


PREF = [('This book of economics is a new edition which, in accordance with the new syllabus enforced by the Intermediate Education Boards, has been published for the second year. In it all topics have been presented in the light of modern thought (Modern Thought). For the explanation of economic terms (Terms) the definitions (Definitions) framed by experts of economics have been stated. In the chapter of mathematical economics difficult topics and concepts (Concepts) have been explained in very easy ways with simple examples. Easily understood tables (Tables) and diagrams (Diagram) have been made. To make economic theories (Theories) understood, examples from everyday life have been given so that the meaning may be easily retained. An effort has been made that the language be fluent and easy and the presentation interesting and flowing. According to the new pattern (New Pattern) of the examination paper, at the end of every chapter models (Model) and exercises (Exercise) in the form of subjective and objective questions with answers, and at the end of the book the papers of the 2014 examination of the different Secondary Education Boards, have been included, so that students become well acquainted with their style and standard and prepare accordingly. It is hoped that this new book will prove easy and comprehensive from the point of view of the syllabus and useful and beneficial from the examination point of view, God willing!',
         'یہ کتابِ معاشیات کا نیا ایڈیشن ہے جو انٹرمیڈیٹ ایجوکیشن بورڈوں کے نافذ کردہ نئے سلیبس کے مطابق، سیکنڈ ایئر کے لیے شائع کیا گیا ہے۔ اس میں تمام موضوعات، جدید افکار (Modern Thought) کی روشنی میں پیش کیے گئے ہیں۔ معاشی اصطلاحات (Terms) کی وضاحت کے لیے ماہرینِ معاشیات کی وضع کردہ تعریفات (Definitions) بیان کی گئی ہیں۔ ریاضیاتی معاشیات کے باب میں مشکل عنوانات اور تصورات (Concepts) کو بڑے آسان طریقوں سے، سادہ مثالوں کے ساتھ واضح کیا گیا ہے۔ عام فہم گوشوارے (Tables) اور ڈائیگرام (Diagram) بنائے گئے ہیں۔ معاشی نظریات (Theories) کو سمجھانے کے لیے روزمرہ زندگی سے مثالیں دی گئی ہیں تاکہ مفہوم بہ آسانی ذہن نشین ہو جائے۔ کوشش کی گئی ہے کہ زبان سلیس و آساں ہو اور بیان دلچسپ و رواں۔ پرچۂ امتحان کے نئے اسلوب (New Pattern) کے مطابق ہر باب کے آخر میں، نمونے (Model) اور مشق (Exercise) کے طور پر انشائی اور معروضی طرز کے سوالات مع جوابات، نیز کتاب کے آخر میں مختلف سیکنڈری ایجوکیشن بورڈوں کے امتحان 2014ء کے پرچے شامل کیے گئے ہیں تاکہ طلباء ان کے انداز و معیار سے خوب واقف ہو جائیں اور اس کے مطابق تیاری کریں۔ امید ہے کہ یہ نئے نصاب کے لحاظ سے آسان و جامع کتاب ثابت ہوگی اور امتحانی نقطۂ نگاہ سے مفید و نافع۔ انشاءاللہ!',
         'دا د اقتصاد کتاب نوې نسخه ده چې د انټرمیډیټ ښوونې بورډونو د نافذ کړي نوي نصاب سره سم د دویم کال لپاره خپره شوې. په کې ټول موضوعات د عصري افکارو (Modern Thought) په رڼا کې وړاندې شوي. د اقتصادي اصطلاحګانو (Terms) د روښانه کولو لپاره د اقتصاد پوهانو جوړ کړي تعریفونه (Definitions) بیان شوي. د ریاضیاتي اقتصاد په څپرکي کې سخت سرلیکونه او تصورونه (Concepts) په ډېرو اسانه لارو او ساده بېلګو روښانه شوي. عام پوهېدونکي جدولونه (Tables) او ډیاګرامونه (Diagram) جوړ شوي. د اقتصادي نظریو (Theories) د پوهولو لپاره له ورځني ژوند بېلګې ورکړل شوې ترڅو مفهوم په اسانۍ په ذهن کې کېني. هڅه شوې چې ژبه روانه او اسانه او بیان په زړه پورې او روان وي. د ازموینې د پرچې د نوي طرز (New Pattern) سره سم د هر څپرکي په پای کې د نمونې (Model) او تمرین (Exercise) په توګه انشايي او معروضي پوښتنې له ځوابونو سره، او د کتاب په پای کې د بېلابېلو ثانوي ښوونې بورډونو د ۲۰۱۴ کال د ازموینې پرچې شاملې شوې ترڅو زده‌کوونکي یې له طرز او معیار سره ښه بلد شي او له مخې یې چمتووالی ونیسي. هیله ده چې دا به د نوي نصاب له مخې اسانه او جامع کتاب ثابت شي او د ازموینې له نظره ګټور او مفید. ان‌شاءالله!'),
        ('I am grateful to those experts from whose writings use has been made in compiling this book. May Allah the Exalted reward them and those respected teachers who liked this book and encouraged me with words of appreciation and praise. It is the prayer to the Forgiving, Merciful, Generous Lord that He forgive all our faults and grant us success in this world and the Hereafter. Amen! — Professor Muhammad Manzoor Ali Sheikh (may Allah forgive him); Professor Muhammad Jamil',
         'اس کتاب کی تالیف کے سلسلہ میں جن ماہرین کی نگارشات سے استفادہ کیا گیا ہے میں اُن کا ممنون ہوں۔ اللہ تعالیٰ انھیں جزائے خیر دے اور اُن اساتذۂ کرام کا شکرگزار ہوں جنھوں نے اس کتاب کو پسند فرمایا اور کلماتِ تحسین و توصیف سے میری حوصلہ افزائی کی۔ غفور و رحیم ربِ کریم سے دعا ہے کہ وہ ہماری سب خطائیں معاف فرمائے اور دنیا و آخرت میں فوز و فلاح سے نوازے۔ آمین! — پروفیسر محمد منظور علی شیخ عفا اللہ عنہ؛ پروفیسر محمد جمیل',
         'د دې کتاب د تالیف په لړ کې چې د کومو متخصصینو له لیکنو ګټه اخیستل شوې، د هغوی منندوی یم. الله تعالی دې هغوی ته ښه بدله ورکړي، او د هغو درنو ښوونکو شکر ګزار یم چې دا کتاب یې خوښ کړ او د ستاینې په ټکو یې زما هڅونه وکړه. له بښونکي او مهربان کریم رب څخه دعا ده چې زموږ ټولې تېروتنې وبښي او په دنیا او آخرت کې مو بریالي کړي. آمین! — پروفیسر محمد منظور علي شیخ (الله دې وبښي)؛ پروفیسر محمد جمیل')]


def p4():
    b = Builder()
    b.h('Preface', 'پیش لفظ', 'سریزه')
    for x in PREF:
        b.p(*x)
    r1 = BOOK.record(b, 'eco12-fm-preface', 'Preface', 'پیش لفظ', 'سریزه', 4, ['iv'])
    r2 = endorse_block(4, ['v'], 1, [x for x in ENDORSE if x[4] == 'v'], first=True)
    BOOK.save(4, [('FM', r1), ('FM', r2)], issues=[{'id': 'eco12-pdf004', 'unit': 'FM', 'printedPage': 'iv',
               'description': 'The preface mentions the board papers of the “2014” examination at the end of the book. The right edge of p.iv is cut in the scan (“کے لیے”, “بیان”, “جائے”) and completed from context.'}])


def p5():
    r1 = endorse_block(5, ['vi', 'vii'], 2, [x for x in ENDORSE if x[4] in ('vi', 'vii')])
    BOOK.save(5, [('FM', r1)])


def p6():
    r1 = endorse_block(6, ['viii', 'ix'], 3, [x for x in ENDORSE if x[4] in ('viii', 'ix', 'ix–x')])
    BOOK.save(6, [('FM', r1)])


TOC = [
 ('1', 'Macro Economics — Part A; National Income', 'کلیاتی معاشیات Macro Economics (جزوالف PartA)؛ قومی آمدنی (National Income)', 'Concept of national income; different concepts of national income: gross national product (GNP), net national product (NNP), gross domestic product (GDP); methods of measuring national income: product method, income method, expenditure method; circular flow of income; real income versus money income; equilibrium level of national income; functional relationship of income and consumption (APC), marginal propensity to consume (MPC), average propensity to save (APS), marginal propensity to save (MPS); factors determining national income. Model paper questions.',
  'قومی آمدنی کا مفہوم، قومی آمدنی کے مختلف تصورات: خام قومی پیداوار (GNP)، خالص قومی پیداوار (NNP)، خام ملکی پیداوار (GDP)، قومی آمدنی ماپنے کے طریقے، پیداوار کا طریقہ، آمدنی کا طریقہ، اخراجات کا طریقہ، آمدنی کا دائری بہاؤ، حقیقی آمدنی بمقابلہ زری آمدنی، قومی آمدنی کی متوازن سطح، آمدنی اور صرف کا تفاعلی رشتہ، اوسط میلان صرف (APC)، مختتم میلان صرف (MPC)، اوسط میلان بچت (APC)، مختتم میلان بچت (MPS)، قومی آمدنی کو متعین کرنے والے عوامل۔ ماڈل پرچہ سوالات', '1'),
 ('2', 'Money', 'زر (Money)', 'Barter (Bank) and the difficulties of barter; evolution of money; functions of money; kinds of money; paper money: advantages and disadvantages; instruments of money (credit card), automated teller machine (ATM), travellers’ cheque (TC); supply and demand of money; value of money (Value); quantity theory of money; criticism of the quantity theory; theory of supply and demand of money. Model paper questions.',
  'براہِ راست تبادلہ (Bank)، براہِ راست تبادلہ کی مشکلات، زر کا ارتقاء، زر کے فرائض، زر کی اقسام، کاغذی زر (Paper Money) کے فائدے اور نقصانات، آلاتِ زر (کریڈٹ کارڈ)، آٹو میڈ ٹیلر مشین (ATM)، سفری چیک (TC)، زر کی رسد اور طلب، زر کی قدر (Value)، نظریہ مقدارِ زر، نظریہ مقدارِ زر پر تنقید، زر کی رسد اور طلب کا نظریہ۔ ماڈل پرچہ سوالات', '22'),
 ('3', 'Bank', 'بنک (Bank)', 'Definition of a bank (Definition); kinds of banks; functions of a bank; how money is created; instruments of credit money (details in chapter 2); role of banks in economic development; central bank; principles and functions of the central bank; monetary policy; objectives and methods of controlling credit; concept of interest; Islamic (interest-free) banking; method of banking; practical measures for Islamic banking in Pakistan; Islamic banking at the world level; Islamic banking in Saudi Arabia; Islamic banking in Malaysia; volume of the finances of Islamic banks. Model paper questions.',
  'بنک کی تعریف (Definition)، بنکوں کی اقسام، بنک کے فرائض، زر کس طرح تخلیق کیا جاتا ہے، اعتباری زر کے آلات (تفصیل باب 2 میں)، معاشی ترقی میں بنکوں کا حصہ، مرکزی بنک، مرکزی بنک کے اصول اور فرائض، زری پالیسی، اعتباری زر کنٹرول کرنے کے مقاصد، اعتباری زر کنٹرول کرنے کے طریقے، سود کا مفہوم، اسلامی (یعنی بلاسود) بنکاری کا طریقہ، پاکستان میں اسلامی بنکاری کے لئے عملی اقدامات، عالمی سطح پر اسلامی بنکاری، سعودی عرب میں اسلامی بنکاری، ملائشیا میں اسلامی بنکاری، اسلامی بنکوں کے مالیات کا حجم۔ ماڈل پرچہ سوالات', '46'),
 ('4', 'Public Finance', 'سرکاری مالیات (Pulic Finance)', 'Similarities and differences between public finance and private finance; tax revenue and non-tax revenue; sources of government income; tax culture (Tax Culture); principles of taxation; kinds of taxes; direct taxes; indirect taxes; proposals to improve the tax system of Pakistan; objectives of fiscal policy. Model paper questions.',
  'سرکاری مالیات اور نجی مالیات میں مشابہت اور فرق، سرکاری محصولات اور محصولاتی تمدن، محصولاتی اور غیر محصولاتی آمدنی، حکومت کے ذرائع آمدنی، ٹیکس عائد کرنے کے اصول (Tax Culture)، ٹیکسوں کی اقسام، بلاواسطہ ٹیکس، متراند ٹیکس، پاکستان کے نظام محصولات کا جائزہ، نظام محصولات کو بہتر بنانے کے لیے تجاویز، مالیاتی پالیسی کے مقاصد۔ ماڈل پرچہ سوالات', '63'),
 ('5', 'International Trade', 'بین الاقوامی تجارت (International Trade)', 'Difference between domestic (internal) trade and international trade; benefits and disadvantages of international trade; classical theory of international trade; theory of comparative costs; modern theory of international trade; balance of trade; balance of payments (Balance of Payment); globalisation (Globalization); multinational companies (MNCs); World Trade Organization (WTO). Model paper questions.',
  'ملکی (اندرونی) تجارت اور بین الاقوامی تجارت میں فرق، بین الاقوامی تجارت کے فائدے اور نقصانات، بین الاقوامی تجارت کا کلاسیکی نظریہ، نظریہ تقابلی مصارف، بین الاقوامی تجارت کا جدید نظریہ، توازن تجارت، ادائیگیوں کا توازن (Balance of Payment)، گلوبلائزیشن (عالمگیریت) (Globalization)، کثیر القومی کمپنیاں (MNCs)، عالمی تجارتی تنظیم (WTO)۔ ماڈل پرچہ سوالات', '82'),
 ('6', 'Pakistan Economics — Part B; Introduction to the Economy of Pakistan', 'معاشیات پاکستان (Pakistan Economics) (جزب Part B)؛ معیشت پاکستان کا تعارف', 'Different sectors of the economy of Pakistan; importance of the agricultural sector; solution of agricultural problems; importance of industry in the economy of Pakistan; government measures for industrial development; cottage industries; capital market of Pakistan; stock exchange; education sector; health sector. Model paper questions.',
  'معیشت پاکستان کے مختلف شعبے، زرعی شعبہ کی اہمیت، زرعی مسائل کا حل، معیشت پاکستان میں صنعت کی اہمیت، صنعتی ترقی کے لیے حکومت کے اقدامات، گھریلو صنعتیں، پاکستان کا بازار سرمایہ، اسٹاک ایکسچینج، تعلیم کا شعبہ، صحت کا شعبہ۔ ماڈل پرچہ سوالات', '109'),
 ('7', 'National Income of Pakistan', 'پاکستان کی قومی آمدنی', 'Size of national income and the share of different sectors in it; method of measuring national income in Pakistan; difficulties in measuring national income; per capita income in Pakistan; causes of low per capita income; methods of increasing national income and per capita income in Pakistan; tax culture of Pakistan; government measures to reduce poverty. Model paper questions.',
  'قومی آمدنی کا حجم اور اس میں مختلف شعبوں کا حصہ، پاکستان میں قومی آمدنی ماپنے کا طریقہ، قومی آمدنی ماپنے میں مشکلات، پاکستان میں فی کس آمدنی، فی کس آمدنی کم ہونے کے اسباب، پاکستان میں قومی آمدنی اور فی کس آمدنی بڑھانے کے طریقے، پاکستان کا ٹیکس کلچر، غربت گھٹانے کے لئے حکومتی اقدامات۔ ماڈل پرچہ سوالات', '117'),
 ('8', 'Economic Development and Planning', 'معاشی ترقی اور منصوبہ بندی (Economic Development and Planning)', 'Concept of economic development; measurement of economic development; problems of a developing economy; factors of economic development; economic planning; need and importance of planning in Pakistan; Pakistan Planning Commission; the eighth five-year plan of Pakistan; Medium Term Development Framework (MTDF); problems of the agricultural sector in Pakistan; solution of agricultural problems and government measures; problems of the industrial sector of Pakistan; solution of the problems of the industrial sector; cottage industries of Pakistan. Model paper questions.',
  'معاشی ترقی کا مفہوم، معاشی ترقی کی پیمائش، ترقی پذیر معیشت کے مسائل، معاشی ترقی کے عوامل، معاشی منصوبہ بندی، پاکستان میں منصوبہ بندی کی ضرورت و اہمیت، پاکستان منصوبہ بندی کمیشن، پاکستان کا آٹھواں پنجسالہ منصوبہ، اوسط المیعاد ترقیاتی منصوبہ (MTDF)، پاکستان میں زرعی شعبہ کے مسائل، زرعی مسائل کا حل اور حکومتی اقدامات، پاکستان کے صنعتی شعبہ کے مسائل، صنعتی شعبہ کے مسائل کا حل، پاکستان کی گھریلو صنعتیں۔ ماڈل پرچہ سوالات', '130'),
 ('9', 'Communications, Means of Transport and Development of Human Resources', 'مواصلات، ذرائع نقل و حمل اور انسانی ذرائع کی ترقی', 'Importance of means of communication and transport; network of roads in Pakistan; development work; importance and usefulness of the Pakistan Railway; shipping; airports; seaports; dry ports; means of communication; computer and information technology; role of means of communication in the economic prosperity of Pakistan; importance of human labour; factors of the productivity of labour; mobility of labour; problems of the rapid rate of population growth in Pakistan and the need to educate the population; solution of overpopulation; government measures; manpower planning in Pakistan; problem of unemployment and underemployment in Pakistan; causes and remedies of unemployment; government measures to increase employment. Model paper questions.',
  'ذرائع مواصلات اور حمل و نقل کی اہمیت، پاکستان میں سڑکوں کا جال، ترقیاتی کام، پاکستان ریلوے اور اس کی اہمیت و افادیت، جہاز رانی، ہوائی بندرگاہیں، بحری بندرگاہیں، خشک گودیاں (Dry Ports)، ذرائع مواصلات، کمپیوٹر اور اطلاعی ٹیکنالوجی، پاکستان کی معاشی خوشحالی میں ذرائع مواصلات کا کردار، انسانی محنت کی اہمیت، محنت کی پیداواریت کے عوامل، محنت کی نقل پذیری، پاکستان میں آبادی کی تیز شرحِ افزائش کے مسائل اور آبادی کی تعلیم کی ضرورت، افراطِ آبادی کا حل، حکومت کے اقدامات، پاکستان میں جمعیت محنت کے مسائل، پاکستان میں بے روزگاری اور نیم روزگاری کا مسئلہ، بیروزگاری کی وجوہات اور علاج، روزگار بڑھانے کے لئے سرکاری اقدامات۔ ماڈل پرچہ سوالات', '162'),
 ('10', 'Banking System of Pakistan', 'پاکستان کا بنکاری نظام', 'Commercial banks; National Bank; Zarai Taraqiati Bank Limited (ZTBL); Pakistan Industrial Development Bank; role of banks in the economic development of Pakistan; State Bank of Pakistan; functions of the State Bank; role of the State Bank in economic development; money market; capital market; e-commerce (E-Commerce); inflation; definition of inflation (Definition); causes of inflation; dearness and remedies of inflation; government measures to control inflation. Model paper questions.',
  'کمرشل بنک، نیشنل بنک، زرعی ترقیاتی بنک لمیٹڈ (ZTBL)، پاکستان صنعتی ترقیاتی بنک، پاکستان کی معاشی ترقی میں بنکوں کا کردار، اسٹیٹ بنک آف پاکستان، اسٹیٹ بنک کے فرائض، معاشی ترقی میں اسٹیٹ بنک کا کردار، بازار زر، بازار سرمایہ، ای کامرس (E-Commerce)، افراط زر، افراط زر کی تعریف (Definition)، افراط زر کی وجوہات، مہنگائی اور افراط زر کا علاج، افراط زر کنٹرول کرنے کے لئے حکومتی اقدامات۔ ماڈل پرچہ سوالات', '191'),
 ('11', 'Public Finance of the Government of Pakistan', 'حکومتِ پاکستان کے مالیات', 'Kinds of taxes in Pakistan; sources of income of the Government of Pakistan; internal and external loans; review of the tax system of Pakistan; proposals for improving it; heads of expenditure of the federal government; important objectives of fiscal policy (Fiscal Policy); sources of income and heads of expenditure of the provincial governments in Pakistan; system of zakat; recipients of zakat; zakat, ushr and charity as a means of government income and as a means of social justice; system of zakat and ushr in Pakistan. Model paper questions.',
  'پاکستان میں ٹیکسوں کی اقسام، حکومت پاکستان کے ذرائع آمدنی، اندرونی و بیرونی قرضے، پاکستان کے نظام محصولات کا جائزہ، نظام محصولات بہتر بنانے کے لیے تجاویز، وفاقی حکومت کے اخراجات کی مدیں، مالیاتی پالیسی (Fiscal Policy) کے اہم مقاصد، پاکستان میں صوبائی حکومتوں کے ذرائع آمدنی اور اخراجات کی مدیں، زکوٰۃ کا نظام، زکوٰۃ کے مستحقین، زکوٰۃ، عشر اور خیرات بطور ذریعہ حکومتی آمدن اور بذریعہ معاشرتی انصاف (عدل اجتماعی کا ذریعہ)، پاکستان میں زکوٰۃ و عشر کا نظام۔ ماڈل پرچہ سوالات', '224'),
 ('12', 'Foreign Trade of Pakistan', 'پاکستان کی بیرونی تجارت', 'Importance of foreign trade; important exports of Pakistan; methods of increasing exports; important imports of Pakistan; benefits of foreign trade to Pakistan; balance of payments of Pakistan; causes of imbalance in Pakistan’s balance of payments; government measures to correct the balance of payments; role of regional and international organisations with reference to Pakistan: Economic Cooperation Organization (ECO), SAARC, World Trade Organization (WTO); effects of the WTO on the economy of Pakistan; determination of the rate of foreign exchange; fixed exchange rate; flexible exchange rate. Model paper questions.',
  'بیرونی تجارت کی اہمیت، پاکستان کی اہم برآمدات، برآمدات بڑھانے کے طریقے، پاکستان کی اہم درآمدات، پاکستان کو تجارت خارجہ کے فائدے، پاکستان کی ادائیگیوں کا توازن، پاکستان کی ادائیگیوں کے توازن میں خرابی کے اسباب، ادائیگیوں کے توازن کی اصلاح کے لئے حکومت کے اقدامات، علاقائی و بین الاقوامی تنظیمیں اور پاکستان کے حوالے سے ان کا کردار، معاشی تعاون کی تنظیم (ECO)، سارک (SAARC)، عالمی تجارتی تنظیم (WTO)، عالمی تجارتی تنظیم کے پاکستانی معیشت پر اثرات، مبادلات خارجہ، زرمبادلہ کی شرح کا تعین، معینہ شرح مبادلہ، لچکدار شرح مبادلہ۔ ماڈل پرچہ سوالات', '249'),
 ('13', 'Economic System of Islam', 'اسلام کا معاشی نظام', 'Features and merits of the Islamic economic system; freeing the economy of Pakistan from interest; interest-free banking in Pakistan; basic values of the Islamic economic system; equality, justice and fairness (social and economic); ihsan; prohibition of extravagance; ending the concentration of wealth; sufficiency, moderation and contentment; effects of ostentation and display on expenditure; hoarding; capitalism (Capitalism); socialism (Socialism); comparison of the Islamic economic system and capitalism; comparison of the Islamic economic system and socialism; the economic system of Islam is the best of all. Model paper questions.',
  'اسلامی معاشی نظام کی خصوصیات اور خوبیاں، سود سے پاک معیشت، پاکستان میں بلاسود بنکاری، اسلامی معاشی نظام کی بنیادی اقدار، مساوات، عدل و انصاف (معاشرتی و اقتصادی)، احسان، فضول خرچی کی ممانعت، ارتکاز دولت کا خاتمہ، کفایت شعاری اور قناعت، نمود و نمائش پر اخراجات کے بُرے اثرات، ذخیرہ اندوزی کے بڑے اثرات، سرمایہ داری نظام (Capitalism)، اشتراکی نظام (Socialism)، اسلامی معاشی نظام اور سرمایہ داری کا موازنہ، اسلامی نظام معیشت اور اشتراکیت کا موازنہ، اسلام کا معاشی نظام سب سے بہتر ہے۔ ماڈل پرچہ سوالات', '273'),
 ('', 'Appendix: Current budget for the financial year 2018-19', 'ضمیمہ: حالیہ بجٹ برائے مالی سال 2018-19', '', '', '295'),
 ('', 'Papers', 'پرچہ جات', '', '', '297')]


def toc_table(b, tid, rows):
    H = (['Chapter', 'Details', 'Page No.'], ['باب', 'تفصیل', 'صفحہ نمبر'], ['څپرکی', 'جزییات', 'مخ'])
    b.table(tid, H[0], [[n, (t + ': ' + d) if d else t, p] for n, t, u, d, du, p in rows], H[1], H[2],
            [[n, (u + '؛ ' + du) if du else u, p] for n, t, u, d, du, p in rows], [[n, (u + '؛ ' + du) if du else u, p] for n, t, u, d, du, p in rows])


def p7():
    r1 = endorse_block(7, ['x'], 4, [x for x in ENDORSE if x[4] == 'x'])
    c = Builder()
    c.h('Contents', 'فہرست', 'نیوولیک')
    toc_table(c, 'eco12-toc-1', TOC[:3])
    r2 = BOOK.record(c, 'eco12-fm-contents-1', 'Contents (1)', 'فہرست (۱)', 'نیوولیک (۱)', 7, ['xi'])
    r2['sourceNote'] = 'The contents are reproduced as a structured table; the Pashto column keeps the Urdu topic lists.'
    BOOK.save(7, [('FM', r1), ('FM', r2)], issues=[{'id': 'eco12-pdf007', 'unit': 'FM', 'printedPage': 'xi',
               'description': 'Contents print “براہِ راست تبادلہ (Bank)” (for Barter), “اوسط میلان بچت (APC)” (for APS), and chapter 4 “(Pulic Finance)”. Retained as printed.'}])


def p8():
    c = Builder()
    toc_table(c, 'eco12-toc-2', TOC[3:10])
    r = BOOK.record(c, 'eco12-fm-contents-2', 'Contents (2)', 'فہرست (۲)', 'نیوولیک (۲)', 8, ['xii', 'xiii'])
    BOOK.save(8, [('FM', r)], issues=[{'id': 'eco12-pdf008', 'unit': 'FM', 'printedPage': 'xii', 'description': 'Contents print “(Pulic Finance)” and “متراند ٹیکس” (for بالواسطہ). Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    {1: p1, 3: p3, 4: p4, 5: p5, 6: p6, 7: p7, 8: p8}[n]()
