"""Civics XII PDF91–95: pp.172–181 — glossary of special terms (continued, letters alif … ye) and “about the author” (p.181).
Run: python class12_civics_page091.py N (91–95)."""
import sys
from class12_civics_common import BOOK, Builder
from class12_civics_page088 import gl, BM


def L(b, en, ur, ps):
    b.h(f'({en})', f'({ur})', f'({ps})')


def rec(b, n, pdf, pages):
    return BOOK.record(b, f'civ12-bm-glossary-{n}', f'Glossary ({n})', f'مخصوص اِصطلاحات ({n})', f'ځانګړې اصطلاحګانې ({n})', pdf, pages)


def p91():
    b = Builder()
    gl(b, [
     ('Extremism', 'Intiha-pasandi', 'Adopting extreme and dangerous methods and ways to achieve an objective.', 'اِنتہا پسندی', 'مقصد کے حصول کیلئے اِنتہائی اور خطرناک طریقے اور راستے اِختیار کرنا۔', 'افراطیت', 'د موخې د ترلاسه کولو لپاره افراطي او خطرناکې طریقې او لارې غوره کول.'),
     ('Market Economy', 'Azad ma‘ishat', 'Such an economic system in which the state does not interfere much.', 'آزاد معیشت', 'ایک ایسا معاشی نظام جس میں ریاست زیادہ مداخلت نہ کرے۔', 'ازاد اقتصاد', 'داسې اقتصادي نظام چې دولت پکې ډېره لاسوهنه ونه کړي.'),
     ('Reforms', 'Islahat', 'Positive changes in some thing.', 'اِصلاحات', 'کسی چیز میں مثبت تبدیلیاں۔', 'اصلاحات', 'په یو شي کې مثبت بدلونونه.'),
     ('Socialism', 'Ishtimali nizam', 'Such a system in which the means of production and income are under the control of the state and collective ownership has been established over them.', 'اِشتمالی نظام', 'ایک ایسا نظام جس میں پیداوار اور آمدنی کے ذرائع ریاست کے قابو میں ہوں اور اُن پر اِجتماعی ملکیت قائم کی گئی ہو۔', 'اشتمالي نظام', 'داسې نظام چې د تولید او عاید سرچینې د دولت تر واک لاندې وي او پرې ټولیز ملکیت ټینګ شوی وي.')])
    L(b, 'Be', 'ب', 'ب')
    gl(b, [
     ('Rebellion', 'Baghawat', 'Not to accept any government or state openly and to raise one’s voice against it.', 'بغاوت', 'کسی بھی حکومت یا ریاست کو برملا تسلیم نہ کرنا اور اُسکے خلاف آواز اُٹھانا۔', 'بغاوت', 'یو حکومت یا دولت په ښکاره نه منل او د هغه پر وړاندې غږ پورته کول.'),
     ('Indirect', 'Bil-wasta', 'For which some auxiliary thing is needed, e.g. climbing up by means of a ladder.', 'بالواسطہ', 'جس کے لئے کسی امدادی چیز کی ضرورت ہو مثلاً سیڑھی کے ذریعے اُوپر چڑھنا۔', 'غیر مستقیم', 'چې کوم مرستندوی شي ته اړتیا ولري، لکه د زینې په مرسته پورته ختل.'),
     ('Direct', 'Bila-wasta', 'Straight; without any support, e.g. climbing up by jumping.', 'بلاواسطہ', 'براہِ راست، بغیر کسی سہارے کے۔ مثلاً چھلانگ کے اُوپر چڑھنا۔', 'مستقیم', 'نېغ؛ له کوم ملاتړ پرته، لکه په ټوپ پورته ختل.'),
     ('Budget', 'Budget', 'Mizaniya; the statement of the expenditure and income of a government for one financial year.', 'بجٹ', 'میزانیہ۔ حکومت کے ایک مالی سال کے اخراجات اور آمدن کا بیان۔', 'بودیجه', 'د یوه مالي کال لپاره د حکومت د لګښتونو او عاید بیان.'),
     ('Corruption', 'Bad-unwani', 'Misusing one’s powers and obtaining illegal benefits; bringing national resources into personal use.', 'بدعنوانی', 'اپنے اِختیارات کا غلط اِستعمال اور ناجائز فوائد حاصل کرنا۔ قومی وسائل کو ذاتی اِستعمال میں لانا۔', 'فساد', 'د خپلو واکونو ناسمه کارونه او ناروا ګټې ترلاسه کول؛ ملي سرچینې په شخصي کار راوستل.'),
     ('International', 'Bain-ul-aqwami', 'Between countries; at the world level, world standard.', 'بین الاقوامی', 'ملکوں کے درمیان، دُنیا کی سطح پر، عالمی معیار کا۔', 'نړیوال', 'د هېوادونو ترمنځ؛ په نړیواله کچه، نړیوال معیار.'),
     ('Crisis', 'Bohran', 'Such a problem for the government which is difficult to solve.', 'بحران', 'حکومت کے لئے ایک ایسا مسئلہ جسے حل کرنا مشکل ہو۔', 'بحران', 'حکومت ته داسې ستونزه چې حل یې ستونزمن وي.'),
     ('Exports', 'Baramadat', 'Things going out of the country.', 'برآمدات', 'ملک سے باہر جانے والی چیزیں۔', 'صادرات', 'هغه شیان چې له هېواده بهر ځي.'),
     ('King-making', 'Badshah-gari', 'Such strong world institutions and countries as make governments in weak states.', 'بادشاہ گری', 'ایسے مضبوط عالمی اِدارے اور ممالک جو کمزور ریاستوں میں حکومتیں بناتی ہیں۔', 'پاچا جوړونه', 'هغه پیاوړې نړیوالې ادارې او هېوادونه چې په کمزورو دولتونو کې حکومتونه جوړوي.')])
    L(b, 'Pe', 'پ', 'پ')
    gl(b, [
     ('Patriarchal', 'Pidar-sari', 'That social system in which the head of the family is a man.', 'پدرسری', 'وہ سماجی نظام جس میں خاندان کا سربراہ مرد ہو۔', 'پلارواکي', 'هغه ټولنیز نظام چې پکې د کورنۍ مشر نارینه وي.'),
     ('Parliament', 'Parliament', 'The central law-making institution is generally given the name of parliament. A provincial assembly cannot be called parliament.', 'پارلیمنٹ', 'مرکزی قانون ساز اِدارے کو عموماً پارلیمنٹ کا نام دیا جاتا ہے۔ صوبائی اسمبلی کو پارلیمنٹ نہیں کہا جا سکتا۔', 'پارلمان', 'مرکزي قانون جوړوونکې ادارې ته عموماً پارلمان ویل کېږي. ولایتي اسمبلۍ ته پارلمان نه شي ویل کېدای.'),
     ('Policy', 'Policy', 'Strategy, ways and means, course of action; style of relations.', 'پالیسی', 'حکمتِ عملی، طور طریقے، طرزِ عمل، اندازِ تعلقات۔', 'پالیسي', 'تګلاره، لارې چارې، کړنلاره، د اړیکو طرز.'),
     ('Pope', 'Pope', 'The world spiritual leader of the Christians.', 'پوپ', 'عیسائیوں کا عالمی روحانی پیشوا۔', 'پاپ', 'د مسیحیانو نړیوال روحاني مشر.'),
     ('Pentagon', 'Pentagon', 'The central building of the American Ministry of Defence.', 'پینٹا گان', 'امریکی وزارتِ دفاع کی مرکزی عمارت۔', 'پنټاګون', 'د امریکا د دفاع وزارت مرکزي ودانۍ.'),
     ('Parliamentary Year', 'Parliamani sal', 'The day on which the first session begins after elections is called the first day of the parliamentary year.', 'پارلیمانی سال', 'اِنتخابات کے بعد جس دن سے پہلا اِجلاس شروع ہوتا ہے وہ پارلیمانی سال کا پہلا دن کہا جاتا ہے۔', 'پارلماني کال', 'له ټاکنو وروسته چې په کومه ورځ لومړۍ غونډه پیلېږي، هغې ته د پارلماني کال لومړۍ ورځ ویل کېږي.'),
     ('Plutonium', 'Plutonium', 'A valuable radioactive metal which is obtained from burnt material in a reactor.', 'پلوٹونیم', 'ایک قیمتی تابکار دھات جو ایٹمی ری ایکٹر میں جلے ہوئے مواد سے حاصل کیا جاتا ہے۔', 'پلوټونیم', 'یو قیمتي وړانګه‌ییز فلز چې په اټومي ریاکټر کې له سوځېدلو موادو ترلاسه کېږي.'),
     ('Controlled Economy', 'Paband ma‘ishat', 'Such an economic system which is in the grip of the state.', 'پابند معیشت', 'ایک ایسا معاشی نظام جو ریاست کی گرفت میں ہو۔', 'مقید اقتصاد', 'داسې اقتصادي نظام چې د دولت په منګولو کې وي.')])
    r1 = rec(b, 3, 91, [172])
    t = Builder()
    L(t, 'Te', 'ت', 'ت')
    gl(t, [
     ('Civilization', 'Tahzib', 'Those human activities which are related to the fulfilment of human needs in the best way are given the name of civilisation or culture. Such people or nations as are engaged in these activities are called civilised.', 'تہذیب', 'وہ اِنسانی سرگرمیاں جو اِنسانی ضروریات کی بہترین انداز میں تکمیل سے متعلقہ ہوں اُسے تہذیب یا تمدن کا نام دیا جاتا ہے۔ ایسے لوگ یا اقوام جو اِس سرگرمی میں ملوث ہوں مہذب کہلاتے ہیں۔', 'تمدن', 'هغه انساني فعالیتونه چې د انساني اړتیاوو په غوره ډول پوره کولو پورې اړه ولري، تمدن یا مدنیت بلل کېږي. هغه خلک یا قومونه چې په دې فعالیت بوخت وي، متمدن بلل کېږي.'),
     ('Historical', 'Tarikhi', 'The conditions and events of the past of human life and civilisation; the study of the past which is done through history.', 'تاریخی', 'اِنسانی زندگی و تہذیب کے ماضی کے حالات و واقعات۔ ماضی کا مطالعہ تاریخ کے ذریعے کیا جاتا ہے۔', 'تاریخي', 'د انساني ژوند او تمدن د تېر وخت حالات او پېښې؛ د تېر وخت مطالعه د تاریخ له لارې کېږي.'),
     ('Developing', 'Taraqqi-pazir', 'Those countries which are still progressing are called developing or Third World countries.', 'ترقی پذیر', 'وہ ممالک جو ابھی ترقی کر رہے ہوں انہیں ترقی پذیر یا تیسری دُنیا کے ممالک کہلاتے ہیں۔', 'پرمختیايي', 'هغه هېوادونه چې لا پرمختګ کوي، پرمختیايي یا د درېیمې نړۍ هېوادونه بلل کېږي.'),
     ('Developed', 'Taraqqi-yafta', 'Those states which have attained progress or have reached the height of progress.', 'ترقی یافتہ', 'وہ ریاستیں جو ترقی حاصل کر چکی ہوں یا ترقی کی اِنتہا تک پہنچ چکے ہوں۔', 'پرمختللی', 'هغه دولتونه چې پرمختګ یې ترلاسه کړی یا د پرمختګ اوج ته رسېدلي وي.'),
     ('Check and Balances', 'Nigrani o tawazun', 'Such a system in which the three organs of government can supervise one another.', 'نگرانی و توازن', 'ایسا نظام جس میں حکومت کے تین اعضاء ایک دوسرے کی نگرانی کر سکیں۔', 'څارنه او توازن', 'داسې نظام چې پکې د حکومت درې ارګانونه د یو بل څارنه کولی شي.'),
     ('Analysis', 'Tajziya', 'Opening something to obtain details and information about its internal structure or composition.', 'تجزیہ', 'کسی چیز کو کھول کر اُسکی اندرونی ساخت یا بناوٹ کے بارے میں تفصیلات اور معلومات حاصل کرنا۔', 'شننه', 'د یو شي پرانیستل او د هغه د داخلي جوړښت یا بڼې په اړه تفصیلات او معلومات ترلاسه کول.'),
     ('Written', 'Tahriri', 'A written thing.', 'تحریری', 'لکھی ہوئی چیز۔', 'لیکلی', 'لیکل شوی شی.'),
     ('Bias', 'Ta‘assub', 'Ill intention, malice, envy, rancour.', 'تعصب', 'بدنیتی، بغض، حسد، کینہ۔', 'تعصب', 'بدنیتي، کینه، حسد، کرکه.'),
     ('Amendment', 'Tarmim', 'To make a change in something, especially in the constitution of a country.', 'ترمیم', 'کسی چیز خصوصاً ملک کے آئین میں تبدیلی کرنا۔', 'تعدیل', 'په یو شي، په ځانګړې توګه د هېواد په اساسي قانون کې بدلون راوستل.'),
     ('Criticism', 'Tanqid', 'A detailed review of the positive and negative aspects of something.', 'تنقید', 'کسی چیز کے مثبت اور منفی پہلوؤں کا تفصیلی جائزہ۔', 'نیوکه', 'د یو شي د مثبتو او منفي اړخونو تفصیلي کتنه.'),
     ('Violence', 'Tashaddud', 'By non-peaceful, bloody methods; by means of force.', 'تشدد', 'غیر پُرامن، خونی طریقے، طاقت کے ذریعے۔', 'تاوتریخوالی', 'په ناسوله‌ییزو، وینه‌لړلو لارو؛ د ځواک له لارې.'),
     ('Explanation/Interpretation', 'Tashrih-o-tauzih', 'To give further clarification and explanation of something, a matter, a principle, law etc.', 'تشریح و توضیح', 'کسی چیز، بات، اُصول، قانون وغیرہ کی مزید وضاحت اور تشریح کرنا۔', 'تشریح او توضیح', 'د یو شي، خبرې، اصل، قانون او نورو لا روښانه کول او تشریح.'),
     ('Continuity', 'Tasalsul', 'Succession.', 'تسلسل', 'تواتر۔', 'تسلسل', 'پرلپسې والی.'),
     ('Adjournment Motion', 'Tahrik-e-iltawa', 'On the application of members in the legislature, stopping the routine proceedings so that an immediately important national matter may be debated.', 'تحریکِ اِلتواء', 'مقننہ میں ارکان کی درخواست کہ معمول کی کارروائی روک کر فوری اہمیت کے قومی معاملے پر بحث کی جائے۔', 'د ځنډولو طرح', 'په مقننه کې د غړو غوښتنه چې عادي بهیر ودرول شي او پر بېړني اهمیت لرونکې ملي چارې بحث وشي.'),
     ('To promote, circulation', 'Tarvij', 'To make current.', 'ترویج', 'رواج دینا۔', 'ترویج', 'رواجول.'),
     ('Disarmament', 'Takhfif-e-aslaha', 'Reducing weapons.', 'تخفیفِ اسلحہ', 'اسلحہ میں کمی کرنا۔', 'د وسلو کمول', 'د وسلو کمول.'),
     ('Variations', 'Taghayyurat', 'Changes.', 'تغیرات', 'تبدیلیاں۔', 'بدلونونه', 'بدلونونه.'),
     ('Custody', 'Tahwil', 'Taking into possession.', 'تحویل', 'قبضے میں لینا۔', 'تحویل', 'په قبضه کې اخیستل.'),
     ('Dissolution', 'Tahlil', 'Breaking.', 'تحلیل', 'توڑنا۔', 'منحل کول', 'ماتول.'),
     ('Ratification', 'Tausiq', 'The final and definite approval of the competent institution.', 'توثیق', 'مجاز اِدارے کی آخری اور حتمی منظوری۔', 'تصویب', 'د واکمنې ادارې وروستۍ او قطعي منظوري.'),
     ('Theatre', 'Theatre', 'Such a place where plays, shows and dramas etc. are seen.', 'تھیٹر', 'ایسی جگہ جہاں کھیل تماشے اور ڈرامے وغیرہ دیکھے جاتے ہیں۔', 'تیاتر', 'داسې ځای چې هلته لوبې ننداري او ډرامې او نور لیدل کېږي.')])
    r2 = rec(t, 4, 91, [173])
    BOOK.save(91, [(BM, r1), (BM, r2)], issues=[{'id': 'civ12-pdf091', 'unit': BM, 'printedPage': 172,
               'description': 'p.172 “بلاواسطہ … مثلاً چھلانگ کے اُوپر چڑھنا”, “جو کمزور ریاستوں میں حکومتیں بناتی ہیں”, “ایٹمی ری ایکٹر … مواد سے حاصل کیا جاتا ہے”; p.173 “انہیں ترقی پذیر … کے ممالک کہلاتے ہیں”, “نگرانی و توازن” filed under ت. Retained as printed.'}])


def p92():
    b = Builder()
    L(b, 'Ṭe', 'ٹ', 'ټ')
    gl(b, [('Tax', 'Tax', 'The money which is obtained from citizens with different references for the national treasury is called tax.', 'ٹیکس', 'شہریوں سے قومی خزانے کے لئے مختلف حوالوں سے جو رقم حاصل کی جاتی ہے اُسے ٹیکس کہتے ہیں۔', 'مالیه', 'هغه پیسې چې د ملي خزانې لپاره له اتباعو په بېلابېلو ډولونو اخیستل کېږي، مالیه ورته ویل کېږي.')])
    L(b, 'Se', 'ث', 'ث')
    gl(b, [
     ('Culture', 'Saqafat', 'Those human activities or means which are the cause of human enjoyment and from which the ways and habits etc. of individuals can be estimated. Culture is called, for example, poetry, music, dress, painting etc.', 'ثقافت', 'وہ اِنسانی سرگرمیاں یا وسائل جو اِنسانی لطف کا باعث ہوں اور جن سے افراد کے طور طریقوں و عادات وغیرہ کا اندازہ ہو سکے۔ ثقافت کو (Culture) کہا جاتا ہے مثلاً شعر و شاعری، موسیقی، لباس، مصوری وغیرہ۔', 'کلتور', 'هغه انساني فعالیتونه یا وسایل چې د انساني خوند لامل وي او د وګړو د طرزونو او عادتونو اټکل ترې کېدای شي؛ لکه شعر او شاعري، موسیقي، جامې، انځورګري او نور.'),
     ('Cultural Heritage', 'Saqafati virsa', 'The transfer of cultural values from generation to generation and their protection.', 'ثقافتی ورثہ', 'ثقافتی اقدار کی نسل در نسل منتقلی اور اُسکی حفاظت۔', 'کلتوري میراث', 'د کلتوري ارزښتونو له نسله نسل ته لېږد او ساتنه.')])
    L(b, 'Jim', 'ج', 'ج')
    gl(b, [('GATT', 'General Agreement on Trade and Tariff', 'An institution of world trade which has at this time changed into the world trade institution (W.T.O). Its purpose was to support the economy.', 'جنرل اگریمنٹ آن ٹریڈ اینڈ ٹیرف', 'عالمی تجارت کا اِدارہ جو اِس وقت عالمی تجارتی اِدارے (W.T.O) میں تبدیل ہوا ہے۔ اِس کا مقصد معیشت کو سہارا دینا تھا۔', 'ګاټ', 'د نړیوالې سوداګرۍ اداره چې اوس په نړیوالې سوداګریزې ادارې (W.T.O) اوښتې. موخه یې اقتصاد ته ملاتړ ورکول وو.')])
    L(b, 'He', 'ح', 'ح')
    gl(b, [
     ('Sovereignty', 'Hakimiyat', 'It is also called supreme authority, i.e. that highest authority of the state above which there is no other higher authority.', 'حاکمیت', 'اِسے اقتدارِ اعلیٰ بھی کہتے ہیں۔ یعنی ریاست کے وہ اعلیٰ ترین اِختیار جس کے اُوپر کوئی اور بالا اِختیار نہ ہو۔', 'حاکمیت', 'لوړ واک هم ورته ویل کېږي، یعنې د دولت هغه تر ټولو لوړ واک چې له هغه پورته بل لوړ واک نه وي.'),
     ('Opposition', 'Hizb-e-ikhtilaf', 'That party or parties which supervise the governing party or parties and criticise the negative activities of the government.', 'حزبِ اِختلاف', 'وہ جماعت یا جماعتیں جو حکومتی جماعت یا جماعتوں کی نگرانی کرتی ہیں اور حکومت کی منفی سرگرمیوں پر تنقید کرتی ہیں۔', 'اپوزیسیون', 'هغه ګوند یا ګوندونه چې د حکومتي ګوند یا ګوندونو څارنه کوي او د حکومت پر منفي فعالیتونو نیوکه کوي.'),
     ('Veto', 'Haq-e-istirdad', 'The right to reject.', 'حقِ اِستر داد', 'مسترد یا نامنظور کرنے کا حق۔', 'د ویټو حق', 'د ردولو یا نه منلو حق.'),
     ('Right of Self-determination', 'Haq-e-khud-iradiyat', 'The right of small and subjugated nationalities to decide their political future.', 'حقِ خودارادیت', 'چھوٹی اور محکوم قومیتوں کا اپنے سیاسی مستقبل کے فیصلے کا حق۔', 'د برخلیک ټاکنې حق', 'د کوچنیو او محکومو قومیتونو حق چې د خپل سیاسي راتلونکي پرېکړه وکړي.')])
    L(b, 'Khe', 'خ', 'خ')
    gl(b, [
     ('Family', 'Khandan', 'The first unit of human society or civilisation in which individuals, especially husband and wife, parents and children etc., live together.', 'خاندان', 'اِنسانی معاشرہ یا تہذیب کی پہلی اکائی جس میں افراد خصوصاً میاں، بیوی، والدین اور بچے وغیرہ مل کر رہتے ہوں۔', 'کورنۍ', 'د انساني ټولنې یا تمدن لومړی واحد چې پکې وګړي، په ځانګړې توګه مېړه، ښځه، مور او پلار او ماشومان او نور یوځای اوسېږي.'),
     ('Features/Characteristics/Attribute', 'Khususiyat', 'Features, qualities.', 'خصوصیات', 'خدوخال، کیفیات۔', 'ځانګړنې', 'بڼه، کیفیتونه.'),
     ('Foreign Policy', 'Kharija policy', 'The principles of a country for establishing relations with other countries.', 'خارجہ پالیسی', 'کسی ملک کا دوسرے ممالک سے تعلقات قائم کرنے کے لئے اُصول۔', 'بهرنۍ تګلاره', 'له نورو هېوادونو سره د اړیکو د ټینګولو لپاره د یوه هېواد اصول.')])
    L(b, 'Che', 'چ', 'چ')
    gl(b, [
     ('Charter', 'Charter', 'Manifesto, programme.', 'چارٹر', 'منشور، پروگرام۔', 'منشور', 'منشور، پروګرام.'),
     ('Aggression', 'Jarhiyat', 'One country entering another country forcibly and military interference.', 'جارحیت', 'کسی ملک کا دوسرے ملک میں زبردستی داخل ہونا اور فوجی مداخلت کرنا۔', 'تېری', 'د یوه هېواد په زوره بل هېواد ته ننوتل او پوځي لاسوهنه.')])
    r1 = rec(b, 5, 92, [174])
    t = Builder()
    L(t, 'Dal', 'د', 'د')
    gl(t, [
     ('Constitution', 'Dastur', 'It is also given the name of the constitution or basic law. It is the name of that law which explains the mutual relationship of the state and the public.', 'دستور', 'اِسے آئین یا بنیادی قانون کا نام بھی دیا جاتا ہے۔ یہ اُس قانون کا نام ہے جو ریاست اور عوام کے باہمی تعلق کی وضاحت کرتا ہے۔', 'اساسي قانون', 'آیین یا بنسټیز قانون هم ورته ویل کېږي. د هغه قانون نوم دی چې د دولت او خلکو دوه اړخیزه اړیکه روښانه کوي.'),
     ('Jurisdiction', 'Daira-e-kar', 'The sphere of authority of any individual or institution.', 'دائرہ کار', 'کسی بھی فرد یا اِدارے کا دائرہ اِختیار۔', 'صلاحیت ساحه', 'د یوه فرد یا ادارې د واک ساحه.'),
     ('Testimonials', 'Dastavizat', 'Certificates, papers, documents.', 'دستاویزات', 'اسناد، کاغذات، Documents۔', 'اسناد', 'سندونه، کاغذونه، Documents.'),
     ('Common Wealth', 'Daulat-e-mushtaraka', 'The world organisation of those countries which had once obtained independence from Britain. Its head is the British queen, and these countries give concessions to one another in trade.', 'دولتِ مشترکہ', 'اُن ممالک کی عالمی تنظیم جو کبھی برطانیہ سے آزادی حاصل کر چکے تھے۔ اِس کی سربراہ برطانوی ملکہ ہوتی ہے اور یہ ممالک ایک دوسرے کے ساتھ تجارت میں رعایت کرتے ہیں۔', 'ګډه شتمني (دولت مشترکه)', 'د هغو هېوادونو نړیوال سازمان چې یو وخت یې له برتانیې خپلواکي اخیستې وه. مشره یې د برتانیې ملکه وي او دا هېوادونه په سوداګرۍ کې یو بل ته اسانتیاوې ورکوي.'),
     ('Preface', 'Dibacha', 'The opening words or thoughts from the author in a book.', 'دیباچہ', 'کسی کتاب میں مصنف کی طرف سے اِبتدائی کلمات یا خیالات۔', 'سریزه', 'په یوه کتاب کې د لیکوال له خوا پیلیزې خبرې یا فکرونه.'),
     ('Brain Drain', 'Dimagh ka bahao', 'Shortage of skilled individuals: when the able and intelligent class of some country goes to other countries because of the attractive concessions offered by them, this is the drain of brains. For example, Pakistan’s engineers, doctors, scientists and other professional experts go to the Gulf countries, Europe, America and especially Canada (skilled people going out of the country).', 'دماغ کا بہاؤ', 'ہنرمند افراد کی قلت۔ کسی ملک کا قابل اور ذہین طبقہ جو دیگر ممالک کی دلکش مراعات کی پیشکش کی وجہ سے دوسرے ممالک میں چلا جاتا ہے تو یہ دماغ کا بہاؤ ہے۔ مثلاً پاکستان کے انجینئرز، ڈاکٹرز، سائنسدان اور دیگر پیشہ ور ماہرین خلیجی ممالک، یورپ، امریکہ اور خاص طور پر کینیڈا جاتے ہیں۔ (ہنرمند افراد کا ملک سے باہر جانا)', 'د دماغونو تېښته', 'د مهارت لرونکو کسانو کمښت: د یوه هېواد وړ او هوښیار قشر چې د نورو هېوادونو د زړه‌راښکونکو امتیازاتو له امله نورو هېوادونو ته ځي، دا د دماغونو تېښته ده. لکه د پاکستان انجینران، ډاکټران، ساینس‌پوهان او نور مسلکي متخصصین خلیجي هېوادونو، اروپا، امریکا او په ځانګړې توګه کاناډا ته ځي (د ماهرو کسانو له هېواده وتل).'),
     ('Imports', 'Daramadat', 'Things coming into the country.', 'درآمدات', 'ملک میں آنے والی چیزیں۔', 'واردات', 'هغه شیان چې هېواد ته راځي.'),
     ('Terrorism', 'Dahshat-gardi', 'An attempt to reach an objective through fear and terror, murder and destruction and unrest.', 'دہشت گردی', 'خوف و ہراس، قتل و غارت اور بدامنی کے ذریعے مقصد تک رسائی کی کوشش۔', 'ترهګري', 'د وېرې، وژنو او ویجاړۍ او بدامنۍ له لارې موخې ته د رسېدو هڅه.')])
    L(t, 'Zal', 'ذ', 'ذ')
    gl(t, [('Media', 'Zara‘i-e-iblagh', 'Institutions of broadcasting and publishing; print media, i.e. newspapers, books, magazines, journals etc., and electronic media, i.e. TV, radio, dish, phone, computer, cinema etc.', 'ذرائع ابلاغ', 'نشر و اشاعت کے اِدارے، پرنٹ میڈیا یعنی اخبارات، کتب، میگزین، رسائل وغیرہ اور الیکٹرانک میڈیا یعنی ٹی وی، ریڈیو، ڈش، فون، کمپیوٹر، سینما وغیرہ۔', 'رسنۍ', 'د خپرونو ادارې؛ چاپي رسنۍ، یعنې ورځپاڼې، کتابونه، مجلې او نور، او برېښنايي رسنۍ، یعنې ټلوېزیون، راډیو، ډش، ټیلیفون، کمپیوټر، سینما او نور.')])
    L(t, 'Re', 'ر', 'ر')
    gl(t, [
     ('Customs', 'Rasm-o-riwaj', 'Those social principles which run the system of society, but there is no one who makes them; they arise and vanish by themselves, but courts of the country do not recognise them and do not punish for breaking them.', 'رسم و رواج', 'وہ معاشرتی اُصول جو معاشرے کا نظام چلاتے ہیں لیکن اِس کا بنانے والا کوئی نہیں ہوتا۔ یہ خود بخود پیدا اور فنا ہوتے ہیں لیکن ملک کی عدالتیں اِسے تسلیم نہیں کرتیں اور نہ اِن کے توڑنے پر سزا دیتی ہے۔', 'دودونه', 'هغه ټولنیز اصول چې د ټولنې نظام چلوي، خو جوړوونکی یې نه وي؛ پخپله پیدا او ورکېږي، خو د هېواد محکمې یې نه مني او د ماتولو سزا یې نه ورکوي.'),
     ('Traditions', 'Riwayat', 'Those customs or ways which an individual or nation has received in inheritance from its forefathers are called traditions.', 'روایات', 'وہ رسوم یا طور طریقے جو کسی فرد یا قوم کو آباؤ اجداد سے وراثت میں ملتے ہوں روایات کہلاتے ہیں۔', 'روایات', 'هغه دودونه یا طرزونه چې یوه فرد یا قوم ته له پلرونو نیکونو په میراث رسېدلي وي، روایات بلل کېږي.'),
     ('Voluntarily', 'Raza-karana', 'Such an activity or service for which no remuneration is taken.', 'رضاکارانہ', 'ایسی سرگرمی یا خدمت جس کا کوئی معاوضہ نہ لیا جائے۔', 'رضاکارانه', 'داسې فعالیت یا خدمت چې معاوضه یې وانه خیستل شي.'),
     ('Orientations', 'Rujhanat', 'Towards which an individual’s thinking is more inclined.', 'رُجحانات', 'ایک فرد کی سوچ کس طرف زیادہ مائل ہے۔', 'تمایلات', 'د یوه فرد فکر کومې خوا ته ډېر مایل دی.'),
     ('Welfare', 'Rifahi', 'It is also called falahi. Those state activities which create facility in human life, especially with reference to education, health and employment.', 'رفاہی', 'اِسے فلاحی بھی کہتے ہیں۔ وہ ریاستی سرگرمیاں جو اِنسانی زندگی میں خصوصاً تعلیم، صحت اور روزگار کے حوالے سے سہولت پیدا کریں۔', 'هوساینیز', 'فلاحي هم ورته ویل کېږي؛ هغه دولتي فعالیتونه چې په انساني ژوند کې په ځانګړې توګه د زده‌کړې، روغتیا او روزګار په برخه کې اسانتیا پیدا کړي.')])
    r2 = rec(t, 6, 92, [175])
    BOOK.save(92, [(BM, r1), (BM, r2)], issues=[{'id': 'civ12-pdf092', 'unit': BM, 'printedPage': 174,
               'description': 'p.174 “حقِ اِستر داد”, “ریاست کے وہ اعلیٰ ترین اِختیار”, “چارٹر” and “جارحیت” filed under چ; p.175 “ملک کی عدالتیں … نہ اِن کے توڑنے پر سزا دیتی ہے”. Retained as printed.'}])


def p93():
    b = Builder()
    gl(b, [
     ('Subjects', 'Ri‘aya', 'Those people of a state who for some reason are not regular citizens. The subjects of a king too are called ri‘aya.', 'رعایا', 'کسی ریاست کے وہ لوگ جو کسی وجہ سے باقاعدہ شہری نہ ہوں۔ بادشاہ کے محکوموں کو بھی رعایا کہا جاتا ہے۔', 'رعیت', 'د یوه دولت هغه خلک چې په کوم لامل منظم اتباع نه وي. د پاچا محکومو ته هم رعیت ویل کېږي.'),
     ('Tolerance', 'Rawadari', 'Acceptance; tolerating the weak and minorities and showing broad-mindedness.', 'رواداری', 'قبولیت، کمزور اور اقلیت کو برداشت کرنا اور وسیع القلبی کا مظاہرہ۔', 'رواداري', 'منل؛ کمزوري او لږکۍ زغمل او د پراخ زړه‌توب ښودل.'),
     ('Traditionalism', 'Riwayat-pasandi', 'Giving more importance to customs and traditions.', 'روایت پسندی', 'رسم و رواج اور روایات کو زیادہ اہمیت دینا۔', 'دودپالنه', 'دودونو او روایاتو ته ډېر اهمیت ورکول.'),
     ('Conservative', 'Raj‘at-pasand', 'Returning towards the past.', 'رُجعت پسند', 'ماضی کی طرف رجوع کرنا۔', 'ارتجاعي', 'تېر وخت ته راګرځېدل.')])
    L(b, 'Ze', 'ز', 'ز')
    gl(b, [('Foreign Exchange', 'Zar-e-mubadila', 'That currency through which international trade takes place.', 'زرِ مبادلہ', 'وہ سکہ جس کے ذریعے بین الاقوامی تجارت ہوتی ہے۔', 'بهرنۍ اسعار', 'هغه پیسې چې د هغو له لارې نړیواله سوداګري کېږي.')])
    L(b, 'Sin', 'س', 'س')
    gl(b, [
     ('Political', 'Siyasi', 'Concerned with politics and political parties; concerned with government or civil administration; ideas arising from government and opposition; interest in politics or being active in politics.', 'سیاسی', 'سیاست اور سیاسی جماعتوں سے متعلق۔ حکومت یا سول نظم و نسق سے متعلق۔ حکومت اور حزبِ اِختلاف سے اُبھرنے والے تصورات۔ سیاست میں دلچسپی یا سیاست میں سرگرم ہونا۔', 'سیاسي', 'له سیاست او سیاسي ګوندونو سره تړلی؛ له حکومت یا ملکي ادارې سره تړلی؛ له حکومت او اپوزیسیون راپورته شوي تصورونه؛ په سیاست کې لېوالتیا یا فعالیت.'),
     ('Political Chaos', 'Siyasi abtari', 'Bad political conditions.', 'سیاسی ابتری', 'خراب سیاسی حالات۔', 'سیاسي ګډوډي', 'خراب سیاسي حالات.'),
     ('Socrates', 'Suqrat', 'A Greek philosopher of about the fifth century BC.', 'سقراط', 'تقریباً پانچویں صدی قبل از مسیح کا یونانی فلسفی۔', 'سقراط', 'د میلاد څخه مخکې نږدې د پنځمې پېړۍ یوناني فیلسوف.'),
     ('Union of Soviet Socialist Republics-USSR', 'Soviet Union', 'A country which came into being in 1917 and ended in 1990. Its fifteen provinces which became independent include Russia, Ukraine and the present Muslim countries of Central Asia etc.', 'سوویت یونین', 'ایک ملک جو 1917ء میں وجود پذیر ہوا اور 1990ء میں ختم ہوا۔ اِس کے پندرہ صوبے تھے جو سب آزاد ہوئے اور جس میں روس، یوکرائن اور وسطی ایشیاء کے موجودہ مسلمان ممالک وغیرہ شامل تھے۔', 'شوروي اتحاد', 'یو هېواد چې په ۱۹۱۷ کال رامنځته او په ۱۹۹۰ کال پای ته ورسېد. پنځلس ولایتونه یې وو چې ټول خپلواک شول او روسیه، اوکراین او د منځنۍ آسیا اوسني مسلمان هېوادونه او نور پکې شامل وو.'),
     ('Secular', 'Secular', 'A non-religious political system; such a political system in which religion has no role and the government does not patronise any religion.', 'سیکولر', 'لادینی سیاسی نظام۔ ایسا سیاسی نظام جس میں مذہب کا کوئی کردار نہ ہو اور حکومت کسی مذہب کی سرپرستی نہ کرے۔', 'سېکولر', 'نادیني سیاسي نظام؛ داسې سیاسي نظام چې دین پکې رول ونه لري او حکومت د کوم دین سرپرستي ونه کړي.'),
     ('Public Sector', 'Sarkari shu‘ba', 'The sector of government.', 'سرکاری شعبہ', 'حکومت کا شعبہ۔', 'دولتي سکټور', 'د حکومت برخه.'),
     ('Investment', 'Sarmaya-kari', 'Putting money for income.', 'سرمایہ کاری', 'آمدنی کیلئے پیسہ لگانا۔', 'پانګونه', 'د عاید لپاره پیسې لګول.'),
     ('South Asian Association for Regional Cooperation-SAARC', 'SAARC', 'An organisation for regional cooperation among the countries of South Asia.', 'سارک', 'جنوبی ایشیاء کے ممالک کے درمیان علاقائی تعاون کی تنظیم۔', 'سارک', 'د سوېلي آسیا د هېوادونو ترمنځ د سیمه‌ییزې همکارۍ سازمان.')])
    L(b, 'Shin', 'ش', 'ش')
    gl(b, [('City-States', 'Shahri riyasaten', 'About 500 BC, small states at the city level on the land of Greece, e.g. Athens, Sparta etc.', 'شہری ریاستیں', 'تقریباً ۵۰۰ قبل از مسیح میں یونان کی سرزمین پر پہلی شہری سطح کی چھوٹی ریاستیں مثلاً ایتھنز، سپارٹا وغیرہ۔', 'ښاري دولتونه', 'د میلاد څخه نږدې ۵۰۰ کاله مخکې د یونان پر خاوره د ښار په کچه کوچني دولتونه، لکه اتن، سپارټا او نور.')])
    L(b, 'Sad', 'ص', 'ص')
    gl(b, [('Capability', 'Salahiyat', 'The ability or strength to do some work.', 'صلاحیت', 'کسی کام کرنے کی اہلیت یا طاقت۔', 'وړتیا', 'د کوم کار د کولو اهلیت یا ځواک.')])
    r1 = rec(b, 7, 93, [176])
    t = Builder()
    L(t, 'Ṭo’e', 'ط', 'ط')
    gl(t, [
     ('Physical Conditions', 'Tab‘i halat', 'Physical, geographical conditions, outward situation; conditions related to land, water, natural resources and boundaries.', 'طبعی حالات', 'جسمانی، جغرافیائی حالات، ظاہری صورتِ حال، زمین، پانی، قدرتی وسائل اور حدود اربع کے متعلق حالات۔', 'طبیعي حالات', 'جسمي، جغرافیايي حالات، ښکاره حالت؛ له ځمکې، اوبو، طبیعي سرچینو او پولو سره تړلي حالات.'),
     ('Physical', 'Tibbi', 'Concerned with health.', 'طبی', 'صحت کے متعلق۔', 'طبي', 'له روغتیا سره تړلی.'),
     ('Class System', 'Tabaqati nizam', 'The presence of rich and poor and other discriminatory groups in a country.', 'طبقاتی نظام', 'کسی ملک میں امیر و غریب اور دیگر اِمتیازی گروہوں کی موجودگی۔', 'طبقاتي نظام', 'په یوه هېواد کې د شتمنو او بېوزلو او نورو تبعیضي ډلو شتون.')])
    L(t, 'Ain', 'ع', 'ع')
    gl(t, [
     ('Science', '‘Ilm', 'Those facts which are obtained from observations and experiments.', 'علم', 'وہ حقائق جو مشاہدات و تجربات سے حاصل ہوں۔', 'علم', 'هغه حقایق چې له کتنو او تجربو ترلاسه کېږي.'),
     ('Rational', '‘Aqli', 'Whose basis is not on emotions but on thought and reflection.', 'عقلی', 'جس کی بنیاد جذبات پر نہ ہو بلکہ سوچ و بچار پر ہو۔', 'عقلي', 'چې بنسټ یې پر احساساتو نه، بلکې پر فکر او غور وي.'),
     ('Non existence, default', '‘Adam', 'Not being.', 'عدم', 'نہ ہونا۔', 'نشتوالی', 'نه کېدل.'),
     ('Absence', '‘Adam-e-maujudgi', 'Not being present.', 'عدم موجودگی', 'موجود نہ ہونا۔', 'نه شتون', 'نه موجودېدل.'),
     ('Instability', '‘Adam-e-istihkam', 'Not being stable; in which there is no stability.', 'عدمِ اِستحکام', 'مستحکم نہ ہونا، جس میں ٹھہراؤ نہ ہو۔', 'بې‌ثباتي', 'باثباته نه کېدل؛ چې درېدل پکې نه وي.'),
     ('Global', '‘Alami', 'At the world level; in the whole world.', 'عالمی', 'دُنیا کی سطح پر، ساری دُنیا میں۔', 'نړیوال', 'په نړیواله کچه؛ په ټوله نړۍ کې.'),
     ('No-Confidence', '‘Adam-e-i‘timad', 'Not having confidence.', 'عدمِ اعتماد', 'اِعتماد نہ ہونا۔', 'بې‌باوري', 'باور نه لرل.'),
     ('Multi National Corporations', 'Kasir-ul-aqwami corporations', 'Such business institutions as work in several countries, e.g. Pepsi.', 'کثیر الاقوامی کارپوریشنوں', 'ایسے تجارتی اِدارے جو کئی ممالک میں کام کرتے ہوں۔ مثلاً پیپسی۔', 'څو ملیتي شرکتونه', 'داسې سوداګریزې ادارې چې په څو هېوادونو کې کار کوي، لکه پیپسي.')])
    L(t, 'Fe', 'ف', 'ف')
    gl(t, [
     ('Art', 'Fann', 'Practical demonstration.', 'فن', 'عملی مظاہرہ۔', 'هنر', 'عملي ښودنه.'),
     ('Individuals', 'Fard', 'Man or woman, whose plural is afrad.', 'فرد', 'مرد یا عورت اِسکی جمع افراد ہے۔', 'فرد', 'نارینه یا ښځه؛ جمع یې افراد ده.'),
     ('Leisure', 'Faraghat', 'Free moments, moments of leisure.', 'فراغت', 'فارغ لمحات، فرصت کے لمحے۔', 'فراغت', 'وزګارې شېبې، د فرصت شېبې.'),
     ('Fine Arts', 'Funun-e-latifa', 'Those arts or human activities from which individuals may obtain pleasure.', 'فنونِ لطیفہ', 'وہ فنون یا اِنسانی سرگرمیاں جن سے افراد لطف حاصل کر سکیں۔', 'ښکلي هنرونه', 'هغه هنرونه یا انساني فعالیتونه چې وګړي ترې خوند واخلي.'),
     ('Sectarianism', 'Firqa-wariyat', 'People of a religion being divided into groups on the basis of different styles of thought.', 'فرقہ واریت', 'کسی مذہب کے لوگوں کا مختلف اندازِ فکر کی بنیاد پر گروہوں میں تقسیم ہونا۔', 'فرقه‌پالنه', 'د یوه دین د خلکو د بېلابېلو فکري طرزونو پر بنسټ په ډلو وېشل کېدل.'),
     ('Natural', 'Fitri', 'Natural, i.e. according to the law of nature; those principles and regulations which are not artificial but exist in the universe.', 'فطری', 'قدرتی، یعنی قانونِ فطرت کے مطابق، وہ اُصول و ضوابط جو مصنوعی نہ ہوں بلکہ کائنات میں موجود ہوں۔', 'فطري', 'طبیعي، یعنې د فطرت د قانون سره سم؛ هغه اصول او ضوابط چې مصنوعي نه وي، بلکې په کاینات کې شته وي.'),
     ('State Parties', 'Fariq riyasaten', 'Those states which are parties to some dispute or treaty etc.', 'فریق ریاستیں', 'وہ ریاستیں جو کسی تنازعہ یا معاہدہ وغیرہ میں حصہ دار ہوں۔', 'اړخ دولتونه', 'هغه دولتونه چې په کومه شخړه یا تړون او نورو کې برخه‌وال وي.')])
    L(t, 'Qaf', 'ق', 'ق')
    gl(t, [('Offender', 'Qanun-shikan', 'Those who break the law.', 'قانون شکن', 'قانون توڑنے والے۔', 'قانون ماتوونکی', 'قانون ماتوونکي.')])
    L(t, 'Kaf', 'ک', 'ک')
    gl(t, [
     ('Congress', 'Congress', 'An important political party of India; the name of the American law-making institution.', 'کانگریس', 'بھارت کا ایک اہم سیاسی جماعت۔ امریکی قانون ساز اِدارے کا نام۔', 'کانګرس', 'د هند یو مهم سیاسي ګوند؛ د امریکا د قانون جوړوونکې ادارې نوم.'),
     ('Cabinet', 'Kabina', 'Council of ministers. In Britain the king used to consult a small cabinet of eminent citizens of the country …', 'کابینہ', 'وزراء کی کونسل۔ برطانیہ میں بادشاہ ملک کے نامور شہریوں سے ایک چھوٹے کیبن …', 'کابینه', 'د وزیرانو شورا. په برتانیه کې پاچا د هېواد له نامتو اتباعو سره په یوه کوچني کېبن …')])
    r2 = rec(t, 8, 93, [177])
    BOOK.save(93, [(BM, r1), (BM, r2)], issues=[{'id': 'civ12-pdf093', 'unit': BM, 'printedPage': 177,
               'description': 'p.177 “طبی (Physical)” (term and gloss mismatched in print), “کثیر الاقوامی کارپوریشنوں”, “کانگریس: بھارت کا ایک اہم سیاسی جماعت”; p.176 “سوویت یونین … اِس کے پندرہ صوبے تھے جو سب آزاد ہوئے”. Retained as printed.'}])


def p94():
    b = Builder()
    gl(b, [
     ('Cabinet (continued)', 'Kabina', '… (Cabinet) for advice on state affairs; therefore the council of ministers was given the name of cabinet.', 'کابینہ (جاری)', '(Cabinet) میں ریاستی اُمور کے بارے میں صلاح مشورہ کیا کرتے تھے۔ اِس لئے وزراء کے کونسل کو کابینہ کا نام دیا گیا۔', 'کابینه (دوام)', '… (Cabinet) کې د دولتي چارو په اړه سلا مشوره کوله؛ له همدې امله د وزیرانو شورا ته کابینه نوم ورکړل شو.'),
     ('Ban, null and void', 'Kal-‘adam', 'Non-existent, extinct; as if it does not exist.', 'کالعدم', 'معدوم، ناپید، گویا کہ ہے ہی نہیں۔', 'منحل', 'نابود، ورک، لکه چې شتون نه لري.'),
     ('Convention', 'Convention', 'A joint treaty of several countries.', 'کنونشن', 'کئی ممالک کا مشترکہ معاہدہ۔', 'کنوانسیون', 'د څو هېوادونو ګډ تړون.')])
    L(b, 'Gaf', 'گ', 'ګ')
    gl(b, [('Globalization', 'Globalization', 'The world changing into one village.', 'گلوبلائزیشن', 'دُنیا کا ایک گاؤں میں تبدیل ہونا۔', 'نړیوالتوب', 'د نړۍ پر یوه کلي اوښتل.')])
    L(b, 'Lam', 'ل', 'ل')
    gl(b, [
     ('Latin', 'Latini', 'The ancient Greek language.', 'لاطینی', 'قدیم یونانی زبان۔', 'لاتیني', 'لرغونې یوناني ژبه.'),
     ('Flexible', 'Lachakdar', 'Soft; in which change is possible with ease.', 'لچکدار', 'نرم، جس میں آسانی سے تبدیلی ممکن ہو۔', 'نرم', 'نرم؛ چې په اسانۍ بدلون پکې شونی وي.')])
    L(b, 'Mim', 'م', 'م')
    gl(b, [
     ('Economic', 'Ma‘ashi', 'Economic; concerned with economy; activities of production, trade, income and revenue and finance etc.', 'معاشی', 'اِقتصادی۔ معیشت کے متعلق۔ پیداواری، تجارتی، آمدنی و لاگت اور مالی وغیرہ سرگرمیاں۔', 'اقتصادي', 'اقتصادي؛ له اقتصاد سره تړلی؛ د تولید، سوداګرۍ، عاید او لګښت او مالي او نورو فعالیتونه.'),
     ('Social', 'Mu‘ashrati', 'That aspect of human life which is called social on the basis of mutual relations and way of living.', 'معاشرتی', 'اِنسانی زندگی کا وہ پہلو جو باہمی تعلقات، رہن سہن سے ہو اُسے معاشرتی یا سماجی کہا جاتا ہے۔', 'ټولنیز', 'د انساني ژوند هغه اړخ چې له دوه اړخیزو اړیکو او اوسېدو سره تړلی وي، ټولنیز ویل کېږي.'),
     ('Society', 'Mu‘ashra', 'A group of humans living together on a permanent basis for the fulfilment of mutual needs is called society.', 'معاشرہ', 'اِنسانوں کا گروہ جو مستقل بنیادوں پر باہمی ضروریات کی تکمیل کے لئے مل جل کر رہنا معاشرہ کہلاتا ہے۔', 'ټولنه', 'د انسانانو ډله چې په دایمي بنسټ د دوه اړخیزو اړتیاوو د پوره کولو لپاره یوځای اوسي، ټولنه بلل کېږي.'),
     ('Treaty', 'Mu‘ahida', 'The parties agreeing on some matter or making a pledge.', 'معاہدہ', 'کسی معاملے پر فریقین کے درمیان راضی ہونا یا عہد و پیمان کرنا۔', 'تړون', 'پر کومې چارې د اړخونو ترمنځ رضایت یا ژمنه کول.'),
     ('Sovereign', 'Muqtadir', 'That individual or institution which exercises the highest powers.', 'مقتدر', 'وہ فرد یا اِدارہ جو اعلیٰ ترین اِختیارات کا اِستعمال کرے۔', 'واکمن', 'هغه فرد یا اداره چې تر ټولو لوړ واکونه کاروي.'),
     ('Absolute', 'Mutlaq', 'Possessor of full powers.', 'مطلق', 'کامل اِختیارات کا حامل ہونا۔', 'مطلق', 'د بشپړو واکونو لرونکی.'),
     ('Local Government', 'Maqami hukumat', 'Institutions subordinate to the central government which run affairs at the local level, in cities, villages and rural areas, by using government powers to some extent through elected representatives, e.g. district and tehsil councils etc. It is also given the name of basic democracy.', 'مقامی حکومت', 'مرکزی حکومت کے ماتحت اِدارے جو مقامی سطح پر شہروں، گاؤں اور دیہات کی حد تک سرکاری اِختیارات کا اِستعمال کر کے منتخب نمائندے معاملات چلائیں مثلاً ضلع و تحصیل کونسل وغیرہ۔ اِسے بنیادی جمہوریت کا نام بھی دیا جاتا ہے۔', 'سیمه‌ییز حکومت', 'د مرکزي حکومت لاندې ادارې چې په سیمه‌ییزه کچه، په ښارونو، کلیو او بانډو کې ټاکل شوي استازي د دولتي واکونو په کارولو چارې چلوي، لکه د ولسوالۍ او تحصیل شوراګانې او نور. بنسټیزه ډیموکراسي هم ورته ویل کېږي.'),
     ('Economy', 'Ma‘ishat', 'The economic condition of a country.', 'معیشت', 'کسی ملک کی اِقتصادی حالت۔', 'اقتصاد', 'د یوه هېواد اقتصادي حالت.'),
     ('Matriarchal', 'Madar-sari', 'That social system in which a woman is the head of the family.', 'مادرسری', 'وہ سماجی نظام جس میں عورت خاندان کی سربراہ ہو۔', 'مورواکي', 'هغه ټولنیز نظام چې پکې ښځه د کورنۍ مشره وي.'),
     ('Millat', 'Millat', 'A comprehensive nationhood, e.g. despite the citizenship of different states, all Muslims are one millat.', 'ملت', 'ہمہ گیر قومیت۔ مثلاً مختلف ریاستوں کی شہریت کے باوجود تمام مسلمان ایک ملت ہیں۔', 'ملت', 'هر اړخیز قومیت؛ لکه د بېلابېلو دولتونو د تابعیت سره سره ټول مسلمانان یو ملت دي.'),
     ('Hereditary', 'Mauroosi', 'From generation to generation.', 'موروثی', 'نسل در نسل۔', 'میراثي', 'له نسله تر نسله.'),
     ('Logical', 'Mantiqi', 'With strong and solid arguments.', 'منطقی', 'مضبوط اور ٹھوس دلائل کے ساتھ۔', 'منطقي', 'له پیاوړو او کلکو دلایلو سره.')])
    r1 = rec(b, 9, 94, [178])
    t = Builder()
    gl(t, [
     ('Coordinated', 'Marbut', 'In which there is connection.', 'مربوط', 'جس میں رابطہ ہو۔', 'منسجم', 'چې اړیکه پکې وي.'),
     ('Organized', 'Munazzam', 'The act of working with organisation and in an effective manner.', 'منظم', 'تنظیم کے ساتھ اور مؤثر انداز میں کام کرنے کا عمل۔', 'منظم', 'په تنظیم او اغېزمن ډول د کار کولو عمل.'),
     ('Neutral', 'Mu‘tadil', 'With moderation; impartiality; not taking part in any activity for or against someone, e.g. neither slow nor fast, neither hot nor cold etc.', 'معتدل', 'اِعتدال کے ساتھ۔ غیر جانبداری۔ کسی کے حق یا خلاف سرگرمی میں حصہ نہ لینا۔ مثلاً نہ آہستہ، نہ تیز، نہ گرم، نہ سرد وغیرہ۔', 'معتدل', 'په اعتدال؛ بې‌طرفي؛ د چا په ګټه یا خلاف فعالیت کې برخه نه اخیستل، لکه نه ورو، نه چټک، نه ګرم، نه سوړ او نور.'),
     ('Conditional', 'Mashrut', 'In which there is some condition.', 'مشروط', 'جس میں کوئی شرط ہو۔', 'مشروط', 'چې کوم شرط پکې وي.'),
     ('Impeachment', 'Muwakhaza', 'Removing someone from his office according to a regular judicial method.', 'مواخذہ', 'کسی کو باقاعدہ عدالتی طریقہ کار کے مطابق اپنے عہدے سے برطرف کرنا۔', 'استیضاح (عزل)', 'یو څوک د منظمې قضايي کړنلارې سره سم له خپلې څوکۍ لرې کول.'),
     ('Competent', 'Mujaz', 'That individual or institution which, according to law, has the authority of some work or order.', 'مجاز', 'وہ فرد یا اِدارہ جو قانون کے مطابق کسی کام یا حکم کا اِختیار رکھے۔', 'واکمن', 'هغه فرد یا اداره چې د قانون سره سم د کوم کار یا حکم واک ولري.'),
     ('Joint', 'Makhlut', 'Together.', 'مخلوط', 'مل جل کر۔', 'ګډ', 'یوځای.'),
     ('Guard', 'Muhafiz', 'Those who protect.', 'محافظ', 'حفاظت کرنے والے۔', 'ساتونکی', 'ساتونکي.'),
     ('Advisory', 'Mushawarati', 'The authority to give advice.', 'مشاورتی', 'مشورہ دینے کا اِختیار۔', 'مشورتي', 'د مشورې ورکولو واک.'),
     ('Justified', 'Munsifana', 'According to the requirements of justice.', 'منصفانہ', 'اِنصاف کے تقاضوں کے مطابق۔', 'عادلانه', 'د عدالت د غوښتنو سره سم.'),
     ('Opportunist', 'Mauqa‘-parast', 'Such people as are in search of suitable opportunities to obtain benefits.', 'موقع پرست', 'ایسے لوگ جو فوائد حاصل کرنے کے لئے مناسب مواقع کی تلاش میں ہوں۔', 'فرصت‌طلب', 'داسې خلک چې د ګټو د ترلاسه کولو لپاره د مناسبو فرصتونو په لټه کې وي.'),
     ('Seasonal Politicians', 'Mausami siyasatdan', 'Such politicians as are absent in difficult times and are foremost in national politics in times of ease and comfort.', 'موسمی سیاستدان', 'ایسے سیاستدان جو مشکل اوقات میں غائب ہوں اور سہولت و آرام کے اوقات میں ملکی سیاست میں پیش پیش ہوں۔', 'موسمي سیاستوال', 'داسې سیاستوال چې په ستونزمنو وختونو کې ورک وي او د اسانتیا او ارامۍ په وختونو کې په ملي سیاست کې مخکښ وي.'),
     ('Manifesto', 'Manshur', 'The programme of a political party.', 'منشور', 'کسی سیاسی جماعت کا پروگرام۔', 'منشور', 'د یوه سیاسي ګوند پروګرام.'),
     ('Observation', 'Mushahida', 'To see some event or thing and draw some results from it.', 'مشاہدہ', 'کسی واقعے یا چیز کو دیکھنا اور اُس سے کچھ نتائج اخذ کرنا۔', 'کتنه', 'یوه پېښه یا شی لیدل او ترې ځینې پایلې اخیستل.'),
     ('Budget', 'Mizaniya', 'The annual estimate of expenditure and income.', 'میزانیہ', 'اخراجات اور آمدنی کا سالانہ تخمینہ۔', 'بودیجه', 'د لګښتونو او عاید کلنی اټکل.'),
     ('Ruled', 'Mahkum', 'Those people over whom government is done.', 'محکوم', 'وہ لوگ جن پر حکومت کی جاتی ہے۔', 'محکوم', 'هغه خلک چې پرې حکومت کېږي.'),
     ('Comparative', 'Muwazanati', 'Comparing two things to know the characteristics of both and to distinguish good from bad.', 'موازناتی', 'دو چیزوں کے درمیان مقابلہ کر کے دونوں کی خصوصیات معلوم کرنا اور اچھے بُرے کی تمیز کرنا۔', 'پرتلیز', 'د دوو شیانو ترمنځ پرتله او د دواړو ځانګړنې معلومول او د ښه او بد توپیر.'),
     ('Economy', 'Ma‘ishat', 'The system of livelihood and employment.', 'معیشت', 'روزی اور روزگار کا نظام۔', 'اقتصاد', 'د روزۍ او روزګار نظام.'),
     ('Fiscal', 'Maliyati', 'Concerned with financial affairs or money.', 'مالیاتی', 'مالی اُمور سے یا پیسہ سے متعلق۔', 'مالي', 'له مالي چارو یا پیسو سره تړلی.'),
     ('Accused', 'Mulzim', 'That individual against whom there is an accusation of a crime.', 'ملزم', 'وہ فرد جس پر جرم کا اِلزام ہو۔', 'تورن', 'هغه فرد چې پر هغه د جرم تور وي.'),
     ('Criminal', 'Mujrim', 'That individual on whom the crime is proved.', 'مجرم', 'وہ فرد جس پر جرم ثابت ہو۔', 'مجرم', 'هغه فرد چې پرې جرم ثابت وي.'),
     ('Hatred', 'Munafirat', 'Hatred.', 'منافرت', 'نفرت۔', 'کرکه', 'کرکه.'),
     ('Source', 'Makhaz', 'From where it has been derived or taken.', 'ماخذ', 'جہاں سے اخذ کیا گیا یا لیا گیا ہو۔', 'سرچینه', 'چېرته چې ترې اخیستل شوی وي.'),
     ('Draft, Bill', 'Musawwada', 'A written proposal for making some law in the legislature.', 'مسودہ', 'مقننہ میں کوئی قانون بنانے کی تحریری تجویز۔', 'مسوده', 'په مقننه کې د کوم قانون د جوړولو لیکلی وړاندیز.'),
     ('Financial Institutions', 'Maliyati idare', 'Those institutions which do the transactions of money.', 'مالیاتی اِدارے', 'وہ اِدارے جو رقم کی لین دین کریں۔', 'مالي ادارې', 'هغه ادارې چې د پیسو راکړه ورکړه کوي.')])
    L(t, 'Nun', 'ن', 'ن')
    gl(t, [('Illiteracy', 'Nakhwandagi', 'Not being educated.', 'ناخواندگی', 'تعلیم یافتہ نہ ہونا۔', 'بې‌سوادي', 'لوستی نه کېدل.')])
    r2 = rec(t, 10, 94, [179])
    BOOK.save(94, [(BM, r1), (BM, r2)], issues=[{'id': 'civ12-pdf094', 'unit': BM, 'printedPage': 178,
               'description': 'p.178 “لاطینی: قدیم یونانی زبان” (Latin glossed as ancient Greek), “معاشرہ … مل جل کر رہنا معاشرہ کہلاتا ہے”, “وزراء کے کونسل”; p.179 “جو رقم کی لین دین کریں”. Retained as printed.'}])


def p95():
    b = Builder()
    gl(b, [('Theory/Ideology', 'Nazariya', '1. A collection of rules and regulations, principles and methods which is different from practical activity. 2. Imaginary thinking; that belief about something which is obtained by thinking. 3. A collection of hypothetical principles. 4. A system of social beliefs and values which provides a basis for some social, economic or political activity. 5. A collection of opinions, beliefs and values which guides some individual or group in activities.',
            'نظریہ', '۱۔ قواعد و ضوابط، اُصولوں اور طریقوں کا مجموعہ جو عملی سرگرمی سے مختلف ہو۔ ۲۔ خیالی سوچ۔ کسی چیز کے بارے میں وہ عقیدہ جو سوچنے سے حاصل ہو۔ ۳۔ مفروضاتی اُصولوں کا مجموعہ۔ ۴۔ معاشرتی عقائد اور اقدار کا نظام جو کسی معاشرتی، معاشی یا سیاسی سرگرمی کیلئے بنیاد فراہم کرے۔ ۵۔ رائے، عقائد اور اقدار کا مجموعہ جو کسی فرد یا گروہ کی سرگرمیوں میں راہنمائی کرے۔',
            'نظریه', '۱. د قواعدو، اصولو او طریقو ټولګه چې له عملي فعالیت سره توپیر ولري. ۲. خیالي فکر؛ د یو شي په اړه هغه عقیده چې له فکر کولو ترلاسه شي. ۳. د فرضي اصولو ټولګه. ۴. د ټولنیزو عقایدو او ارزښتونو نظام چې د کوم ټولنیز، اقتصادي یا سیاسي فعالیت لپاره بنسټ برابر کړي. ۵. د رایو، عقایدو او ارزښتونو ټولګه چې په فعالیتونو کې د یوه فرد یا ډلې لارښوونه وکړي.'),
           ('Nomination', 'Namzadgi', 'When some superior power appoints someone to some office according to its own will, it is called nomination.', 'نامزدگی', 'جب کوئی برتر قوت کسی عہدے کے لئے اپنی مرضی سے تقرری کرے اُسے نامزدگی کہا جاتا ہے۔', 'نوماندي', 'کله چې کوم لوړ ځواک د خپلې خوښې سره سم یو څوک کومې څوکۍ ته وګماري، نوماندي ورته ویل کېږي.'),
           ('Management', 'Nazm-o-nasq', 'Administration; running in an organised manner.', 'نظم و نسق', 'اِنتظام، منظم انداز میں چلانا۔', 'اداره', 'انتظام؛ په منظم ډول چلول.'),
           ('North Atlantic Treaty Organization-NATO', 'NATO', 'The North Atlantic Treaty — the military treaty of America and its allies.', 'نیٹو', 'شمالی اوقیانوس کا معاہدہ۔ امریکہ اور اُسکے اِتحادیوں کا فوجی معاہدہ۔', 'ناټو', 'د شمالي اتلانتیک تړون؛ د امریکا او د هغې د متحدینو پوځي تړون.'),
           ('Colonialism', 'Nau-abadiyat', 'Occupying some area in order to use its resources.', 'نوآبادیات', 'کسی علاقے پر اُسکے وسائل اِستعمال کرنے کیلئے قبضہ کرنا۔', 'استعمار', 'د یوې سیمې د سرچینو د کارولو لپاره پرې قبضه کول.'),
           ('House arrest', 'Nazar-band', 'Temporarily confining someone to one place.', 'نظر بند', 'عارضی طور پر کسی کو ایک جگہ میں محدود کرنا۔', 'په کور کې بند', 'په لنډمهاله ډول یو څوک په یوه ځای کې محدودول.'),
           ('Text', 'Nisab', 'Those essays or topics which are taught in educational institutions.', 'نصاب', 'وہ مضامین یا موضوعات جو تعلیمی اِداروں میں پڑھائے جاتے ہیں۔', 'نصاب', 'هغه مضمونونه یا موضوعات چې په تعلیمي ادارو کې تدریسېږي.'),
           ('Colonial System', 'Nau-abadiyati nizam', 'Such a system in which weak countries were made slaves.', 'نوآبادیاتی نظام', 'ایک ایسا نظام جس میں کمزور ممالک کو غلام بنایا جاتا تھا۔', 'استعماري نظام', 'داسې نظام چې پکې کمزوري هېوادونه غلامان کېدل.'),
           ('Private Institutions', 'Niji idare', 'Those institutions which are not governmental.', 'نجی اِدارے', 'وہ اِدارے جو سرکاری نہیں ہوتے۔', 'خصوصي ادارې', 'هغه ادارې چې دولتي نه وي.'),
           ('Private Sector', 'Niji shu‘ba', 'The non-governmental sector.', 'نجی شعبہ', 'غیر سرکاری شعبہ۔', 'خصوصي سکټور', 'نادولتي برخه.')])
    L(b, 'Wao', 'و', 'و')
    gl(b, [('Scope', 'Wus‘at', 'Expansion, i.e. how far a thing is extensive.', 'وسعت', 'پھیلاؤ۔ یعنی کوئی چیز کہاں تک وسیع ہے۔', 'پراخوالی', 'پراختیا، یعنې یو شی تر کومه حده پراخ دی.'),
           ('WTC', 'World Trade Center', 'The world centre of trade in the American city of New York, on which attacks took place in 2001.', 'ورلڈ ٹریڈ سنٹر', 'امریکہ کے شہر نیویارک میں تجارت کا عالمی مرکز جس پر 2001ء میں حملے ہوئے۔', 'نړیوال سوداګریز مرکز', 'د امریکا په نیویارک ښار کې د سوداګرۍ نړیوال مرکز چې په ۲۰۰۱ کال پرې بریدونه وشول.')])
    L(b, 'Ye', 'ی', 'ی')
    gl(b, [('Uranium', 'Uranium', 'A valuable radioactive metal which is used for the atom bomb and other peaceful purposes.', 'یورینیم', 'ایک قیمتی تابکار دھات جو ایٹم بم اور دیگر پرامن مقاصد کیلئے اِستعمال کیا جاتا ہے۔', 'یورانیم', 'یو قیمتي وړانګه‌ییز فلز چې د اټوم بم او نورو سوله‌ییزو موخو لپاره کارول کېږي.')])
    r1 = rec(b, 11, 95, [180])
    t = Builder()
    t.h('About the Author', 'کچھ مصنف کے بارے میں', 'د لیکوال په اړه څه')
    t.h('Professor Bakhtiar', 'پروفیسر بختیار', 'پروفیسر بختیار')
    P = lambda bb, items: [bb.p(*x) for x in items]
    P(t, [('The author of this book, Professor Bakhtiar, belongs to Swabi. He obtained first position in M.A. Political Science from the University of Peshawar. From the same university, as a private candidate, he obtained the degree of M.A. History. Today he is the head of the Department of Political Science at the Government Post Graduate College Swabi.',
           'کتاب ہٰذا کے مصنف پروفیسر بختیار کا تعلق صوابی سے ہے۔ پشاور یونیورسٹی سے ایم اے پولیٹیکل سائنس (سیاسیات) میں پہلی پوزیشن حاصل کی۔ اِسی یونیورسٹی سے بطورِ پرائیویٹ اُمیدوار ایم اے تاریخ کی ڈگری حاصل کی۔ آج کل گورنمنٹ پوسٹ گریجویٹ کالج صوابی میں شعبہ سیاسیات کے سربراہ ہیں۔',
           'د دې کتاب لیکوال پروفیسر بختیار له صوابۍ دی. له پېښور پوهنتون یې د سیاسي علومو په ایم اې کې لومړی مقام ترلاسه کړ. له همدې پوهنتون یې د خصوصي نوماند په توګه د تاریخ د ایم اې سند واخیست. اوس مهال د صوابۍ دولتي پوسټ ګرېجوېټ کالج د سیاسي علومو د څانګې مشر دی.'),
          ('The author has written several books for the Textbook Board. He has also written several books on political science, international relations, civics, ethics and history etc.',
           'مصنف نے ٹیکسٹ بک بورڈ کیلئے متعدد کتب تحریر کیں۔ آپ نے سیاسیات، بین الاقوامی تعلقات، شہریت، اخلاقیات اور تاریخ وغیرہ پر بھی کئی کتب تحریر کیں ہیں۔',
           'لیکوال د درسي کتابونو بورډ لپاره ډېر کتابونه لیکلي. هغه پر سیاسي علومو، نړیوالو اړیکو، تابعیت، اخلاقو او تاریخ او نورو هم ډېر کتابونه لیکلي دي.')])
    r2 = BOOK.record(t, 'civ12-bm-about-author', 'About the author', 'کچھ مصنف کے بارے میں', 'د لیکوال په اړه', 95, [181])
    BOOK.save(95, [(BM, r1), (BM, r2)], complete_units=[BM], issues=[{'id': 'civ12-pdf095', 'unit': BM, 'printedPage': 180,
               'description': 'p.180 “یورینیم … جو … اِستعمال کیا جاتا ہے”; p.181 “کئی کتب تحریر کیں ہیں”. The glossary ends on p.180 with the letter ی; p.181 is the note about the author. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 91
    {91: p91, 92: p92, 93: p93, 94: p94, 95: p95}[n]()
