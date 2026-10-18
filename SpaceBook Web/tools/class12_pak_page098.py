"""Pak Studies XII PDF98 (spread): printed pp.185–186 — Chapter 10 Foreign Policy of Pakistan: definition; basic points 1–10; objectives 1–2."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
P = t.p
H = t.h
P('Chapter Ten', 'بابِ دہم', 'لسم څپرکی')
H('Foreign Policy of the Islamic Republic of Pakistan', 'اسلامی جمہوریہ پاکستان کی خارجہ پالیسی', 'د پاکستان اسلامي جمهوریت بهرنۍ پالیسي')
H('Definition of foreign policy', 'خارجہ پالیسی کی تعریف', 'د بهرنۍ پالیسۍ تعریف')
P('Foreign policy is the name of that part of the policies of any country in which a country establishes relations with other countries. Every country makes these relations keeping its national interests in view; they can change with time, because this is a basic principle of foreign relations that no country has any permanent friend or enemy, but its national interests are permanent and important.',
  'خارجہ پالیسی کسی بھی ملک کی پالیسیوں کے اُس حصے کا نام ہے جس میں کوئی ملک دوسرے ممالک کے ساتھ تعلقات استوار کرتا ہے۔ یہ تعلقات ہر ملک اپنے قومی مفادات کو مدِنظر رکھ کر بناتا ہے، جو وقت کے ساتھ ساتھ تبدیل ہو سکتے ہیں، کیونکہ خارجہ تعلقات کا یہ بنیادی اُصول ہے کہ کسی بھی ملک کا کوئی مستقل دوست یا دشمن نہیں ہوتا بلکہ اُس کے قومی مفادات مستقل اور اہم ہوتے ہیں۔',
  'بهرنۍ پالیسي د یوه هېواد د پالیسیو د هغې برخې نوم دی چې پکې یو هېواد له نورو هېوادونو سره اړیکې ټینګوي. هر هېواد دا اړیکې د خپلو ملي ګټو په پام کې نیولو سره جوړوي، چې د وخت سره بدلېدای شي، ځکه د بهرنیو اړیکو بنسټیز اصل دا دی چې د هېڅ هېواد دایمي دوست یا دښمن نه وي، بلکې ملي ګټې یې دایمي او مهمې وي.')
H('Basic points of Pakistan’s foreign policy', 'پاکستان کی خارجہ پالیسی کے بنیادی نکات', 'د پاکستان د بهرنۍ پالیسۍ بنسټیز ټکي')
P('Pakistan’s foreign policy has been made keeping national interests and priorities in view. Although changes keep coming in Pakistan’s foreign policy with time, the leaders of Pakistan, keeping national interests in front, have laid down a few basic principles of foreign policy. Among these basic principles the following are important:',
  'پاکستان کی خارجہ پالیسی ملکی مفادات اور ترجیحات کو مدِنظر رکھ کر بنائی گئی ہے۔ اگرچہ وقت کے ساتھ ساتھ پاکستان خارجہ پالیسی میں تبدیلیاں لاتا رہتا ہے تاہم پاکستان کے راہنماؤں نے قومی مفادات کو سامنے رکھ کر خارجہ پالیسی کے چند بنیادی اصول وضع کیے ہیں۔ ان بنیادی اصولوں میں درج ذیل اہم ہیں:۔',
  'د پاکستان بهرنۍ پالیسي د هېواد د ګټو او لومړیتوبونو په پام کې نیولو سره جوړه شوې. که څه هم د وخت سره پاکستان په بهرنۍ پالیسۍ کې بدلونونه راولي، خو د پاکستان مشرانو د ملي ګټو په پام کې نیولو سره د بهرنۍ پالیسۍ څو بنسټیز اصول ټاکلي. په دې بنسټیزو اصولو کې دا مهم دي:')
t.group('lines', [
 ('1. Protection of one’s own freedom and autonomy', '1۔ اپنی آزادی اور خود مختاری کا تحفظ', '۱. د خپلې ازادۍ او خپلواکۍ ساتنه'),
 ('2. Respect for the freedom, autonomy and sovereignty of others.', '2۔ دوسروں کی آزادی، خود مختاری اور اقتدارِ اعلیٰ کا احترام۔', '۲. د نورو ازادۍ، خپلواکۍ او لوړ حاکمیت ته درناوی.'),
 ('3. Abstaining from interference in the internal affairs of other countries.', '3۔ دوسرے ممالک کے اندرونی معاملات میں دخل اندازی سے احتراز۔', '۳. د نورو هېوادونو په کورنیو چارو کې له لاسوهنې ډډه.'),
 ('4. Adherence to the principle of non-alignment in international relations.', '4۔ بین الاقوامی تعلقات میں غیر جانبداری کے اُصول کی پابندی۔', '۴. په نړیوالو اړیکو کې د بې‌پلوۍ اصل ته پابندي.'),
 ('5. Strict implementation of the Charter of the United Nations.', '5۔ اقوامِ متحدہ کے منشور پر سختی سے عمل۔', '۵. د ملګرو ملتونو پر منشور په کلکه عمل.'),
 ('6. Promoting basic human rights, peace and reconciliation in the world.', '6۔ دُنیا میں بنیادی انسانی حقوق، امن اور آشتی کو فروغ دینا۔', '۶. په نړۍ کې بنسټیزو بشري حقونو، سولې او روغې ته وده ورکول.'),
 ('7. Opposition to racial discrimination and support for the right of self-determination.', '7۔ نسلی امتیاز کی مخالفت اور حقِ خود ارادیت کی حمایت۔', '۷. د نژادي توپیر مخالفت او د خپل برخلیک ټاکلو د حق ملاتړ.'),
 ('8. Establishment of a just international economic system.', '8۔ منصفانہ بین الاقوامی معاشی نظام کا قیام۔', '۸. د عادلانه نړیوال اقتصادي نظام جوړول.'),
 ('9. Protection of the interests of all Muslims and the unity of the Islamic world', '9۔ تمام مسلمانوں کے مفادات کا تحفظ اور اتحادِ عالمِ اسلام', '۹. د ټولو مسلمانانو د ګټو ساتنه او د اسلامي نړۍ اتحاد'),
 ('10. Establishing better relations in South Asia and promoting peace and security in this region', '10۔ جنوبی ایشیا میں بہتر تعلقات استوار کرنا اور اس خطہ میں امن و سلامتی کا فروغ', '۱۰. په سویلي اسیا کې ښې اړیکې ټینګول او په دې سیمه کې د سولې او امنیت وده')])
H('Objectives of Pakistan’s foreign policy', 'پاکستان کی خارجہ پالیسی کے مقاصد', 'د پاکستان د بهرنۍ پالیسۍ موخې')
P('Pakistan came into existence on 14 August 1947, and from British India it inherited no foreign policy. However, after independence, keeping in view the objectives of the Ideology of Pakistan and the Pakistan Movement, foreign policy was newly formed.',
  'پاکستان 14 اگست 1947ء کو معرضِ وجود میں آیا اور برطانوی ہندوستان سے خارجہ پالیسی کو ورثے میں نہیں پایا۔ البتہ آزادی کے بعد نظریہ پاکستان اور تحریکِ پاکستان کے مقاصد کو پیشِ نظر رکھتے ہوئے خارجہ پالیسی کی تشکیلِ نو کی گئی۔',
  'پاکستان د ۱۹۴۷ز د اګست په ۱۴مه رامنځته شو او له برتانوي هندوستان یې بهرنۍ پالیسي په میراث کې ونه موندله. خو له خپلواکۍ وروسته د پاکستان د نظریې او د پاکستان د غورځنګ د موخو په پام کې نیولو سره بهرنۍ پالیسي له سره جوړه شوه.')
P('The important objectives of Pakistan’s foreign policy are as follows:',
  'پاکستان کی خارجہ پالیسی کے اہم مقاصد مندرجہ ذیل ہیں:۔',
  'د پاکستان د بهرنۍ پالیسۍ مهمې موخې دا دي:')
H('1. National security', '1۔ قومی سلامتی', '۱. ملي امنیت')
P('The most important objective of Pakistan’s foreign policy is national security and protection. Pakistan had emerged new on the map of the world, and there was a need that an appropriate arrangement be made for its security and protection. Therefore Pakistan made national security the basis of its foreign policy and, in its relations with foreign countries, always gave importance to national security. Even today national security is a basic goal in Pakistan’s foreign policy. Pakistan respects the territorial integrity of other countries and expects from other countries too that they respect Pakistan’s national security.',
  'پاکستان کی خارجہ پالیسی کا سب سے اہم مقصد قومی سلامتی و تحفظ ہے۔ پاکستان دُنیا کے نقشے پر نیا نیا اُبھرا تھا اور ضرورت تھی کہ اس کی سلامتی اور تحفظ کا مناسب بندوبست کیا جائے۔ لہٰذا پاکستان نے ملکی سلامتی کو خارجہ پالیسی کی بنیاد بنایا اور بیرونی ممالک کے ساتھ تعلقات میں قومی سلامتی کو ہمیشہ اہمیت دی۔ آج بھی پاکستان کی خارجہ پالیسی میں قومی سلامتی بنیادی نصب العین ہے۔ پاکستان دوسرے ممالک کی علاقائی سالمیت کا احترام کرتا ہے اور دوسرے ممالک سے بھی یہی توقع رکھتا ہے کہ وہ بھی پاکستان کی قومی سلامتی کا احترام کریں۔',
  'د پاکستان د بهرنۍ پالیسۍ تر ټولو مهمه موخه ملي امنیت او ساتنه ده. پاکستان د نړۍ پر نقشه نوی راڅرګند شوی و، او اړتیا وه چې د هغه د امنیت او ساتنې مناسب ترتیب وشي. نو پاکستان د هېواد امنیت د بهرنۍ پالیسۍ بنسټ وګرځاوه او له بهرنیو هېوادونو سره په اړیکو کې یې تل ملي امنیت ته اهمیت ورکړ. نن هم د پاکستان په بهرنۍ پالیسۍ کې ملي امنیت بنسټیز هدف دی. پاکستان د نورو هېوادونو سیمه‌ییزې بشپړتیا ته درناوی کوي او له نورو هېوادونو هم همدا تمه لري چې د پاکستان ملي امنیت ته درناوی وکړي.')
H('2. Economic progress', '2۔ معاشی ترقی', '۲. اقتصادي پرمختګ')
P('Pakistan is a developing country and wants to progress economically. Therefore Pakistan wants to establish good relations with all those countries with which it can trade, or from which it can obtain economic help and progress economically. Keeping new economic tendencies in view, Pakistan has made important changes in its foreign policy. In particular it has adopted free trade, free economics and privatisation.',
  'پاکستان ایک ترقی پذیر ملک ہے اور معاشی طور پر اپنی ترقی چاہتا ہے۔ لہٰذا پاکستان اُن تمام ممالک کے ساتھ اچھے تعلقات قائم کرنا چاہتا ہے جن کے ساتھ تجارت کر کے یا جن سے معاشی مدد حاصل کر کے معاشی طور پر ترقی کر سکے۔ نئے اقتصادی رجحانات کو مدِنظر رکھتے ہوئے پاکستان نے اپنی خارجہ پالیسی میں اہم تبدیلیاں کی ہیں۔ خصوصاً آزاد تجارت، آزاد اقتصادیات اور نجکاری کو اپنایا ہے۔',
  'پاکستان یو پرمختیايي هېواد دی او اقتصادي پلوه خپل پرمختګ غواړي. نو پاکستان له هغو ټولو هېوادونو سره ښې اړیکې ټینګول غواړي چې ورسره سوداګري وکړي یا ترې اقتصادي مرسته ترلاسه کړي او اقتصادي پرمختګ وکړي. د نویو اقتصادي تمایلاتو په پام کې نیولو سره پاکستان په خپله بهرنۍ پالیسۍ کې مهم بدلونونه راوستي، په ځانګړي ډول ازاده سوداګري، ازاد اقتصاد او خصوصي کول یې غوره کړي.')
UT = ('Foreign Policy of the Islamic Republic of Pakistan', 'اسلامی جمہوریہ پاکستان کی خارجہ پالیسی', 'د پاکستان اسلامي جمهوریت بهرنۍ پالیسي')
rec = BOOK.record(t, 'pak12-ch10-text-1', 'Chapter 10 text (1)', 'بابِ دہم — متن (۱)', 'لسم څپرکی — متن (۱)', 98, [185, 186], unit_title=UT)
issues = [{'id': 'pak12-pdf098', 'unit': 10, 'printedPage': 185, 'description': 'The chapter title on p.185 is set in a decorative oval and headings in pink panels within a floral border (ornament, not reproduced). The objective numbers on p.186 use Urdu letters/digits (“ا۔”, “۲۔”); normalised.'}]

if __name__ == '__main__':
    BOOK.save(98, [(10, rec)], issues=issues)
