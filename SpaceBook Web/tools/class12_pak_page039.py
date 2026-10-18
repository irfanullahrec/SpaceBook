"""Pak Studies XII PDF39 (spread): printed pp.67–68 — Ch.4 Objectives Resolution: salient points 1–7; importance begins."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
def P(*v): t.p(*v)
def H(*v): t.h(*v)
P('… remembered by the name “Objectives Resolution”. Through this resolution the Constituent Assembly, as the representative of the Pakistani people, affirmed that the future constitution of Pakistan would be in harmony with the teachings of the Qur’an and Sunnah. The people of Pakistan and their representatives will use their governmental powers within the limits fixed by Allah the Exalted.',
  '… نام سے یاد کیا جاتا ہے۔ اس قرارداد کے ذریعے دستور ساز اسمبلی نے پاکستانی عوام کے نمائندہ کی حیثیت سے یہ اقرار کیا کہ پاکستان کا آئندہ دستور قرآن و سنت کی تعلیمات سے ہم آہنگ ہوگا۔ پاکستان کے عوام اور ان کے نمائندے اپنے حکومتی اختیارات اللہ تعالیٰ کی مقرر کردہ حدود کے اندر رہ کر استعمال کریں گے۔',
  '… نوم یادېږي. د دې پرېکړه‌لیک له لارې اساسي قانون جوړوونکې اسمبلۍ د پاکستاني خلکو د استازي په توګه اقرار وکړ چې د پاکستان راتلونکی اساسي قانون به د قرآن او سنت له لارښوونو سره همغږی وي. د پاکستان خلک او د هغوی استازي به خپل حکومتي واکونه د الله تعالیٰ په ټاکلو پولو کې دننه کاروي.')
H('Salient points of the Objectives Resolution', 'قراردادِ مقاصد کے اہم نکات', 'د موخو پرېکړه‌لیک مهم ټکي')
P('The Objectives Resolution apparently looks like a formal constitutional declaration, but this resolution, by providing a solid foundation for constitution-making in Pakistan, became the cause of clear progress in this respect. The special points of the resolution are as follows.',
  'قراردادِ مقاصد بظاہر ایک رسمی آئینی اعلان نظر آتی ہے مگر یہ قرارداد پاکستان میں دستور سازی کو ایک ٹھوس بنیاد فراہم کر کے اس ضمن میں واضح پیش رفت کا باعث بنی۔ قرارداد کے خاص خاص نکات مندرجہ ذیل ہیں۔',
  'د موخو پرېکړه‌لیک په ښکاره یو رسمي اساسي اعلان ښکاري، خو دې پرېکړه‌لیک په پاکستان کې اساسي قانون جوړونې ته ټینګ بنسټ ورکړ او په دې برخه کې د ښکاره پرمختګ لامل شو. د پرېکړه‌لیک ځانګړي ټکي دا دي:')
for h, p in [
 (('1. The concept of sovereignty', '1۔ حاکمیتِ اعلیٰ کا تصور', '۱. د لوړ حاکمیت تصور'),
  ('Sovereignty over the whole universe belongs to Allah the Exalted alone. He has no partner in sovereignty. The authority of sovereignty with the inhabitants of Pakistan has the status of a sacred trust, and they are bound to exercise these powers while remaining within the limits of the Qur’an and Sunnah.',
   'پوری کائنات میں حاکمیتِ اعلیٰ صرف اللہ تعالیٰ کو حاصل ہے۔ حاکمیت میں اس کا کوئی شریک نہیں۔ پاکستان کے باشندوں کے پاس حاکمیت کا اختیار ایک مقدس امانت کی حیثیت رکھتا ہے اور وہ اس بات کے پابند ہیں کہ قرآن و سنت کی حدود میں رہتے ہوئے ان اختیارات کو بروئے کار لائیں۔',
   'په ټوله کائنات کې لوړ حاکمیت یوازې الله تعالیٰ ته حاصل دی. په حاکمیت کې یې هېڅ شریک نشته. د پاکستان اوسېدونکو سره د حاکمیت واک د یوې سپېڅلې امانت حیثیت لري، او هغوی پابند دي چې د قرآن او سنت په پولو کې دا واکونه وکاروي.')),
 (('2. Following the basic principles of Islam', '2۔ اسلام کے بنیادی اصولوں کی پیروی', '۲. د اسلام د بنسټیزو اصولو پیروي'),
  ('The state will exercise its power and authority through the elected representatives of the people, in which democracy, freedom, equality, tolerance and the principles of social justice will be acted upon according to Islamic teachings.',
   'ریاست اپنے اقتدار اور اختیارات کا استعمال عوام کے منتخب نمائندوں کے ذریعے کرے گی جس میں جمہوریت، آزادی، مساوات، رواداری اور معاشرتی انصاف کے اصولوں پر اسلامی تعلیمات کے مطابق عمل کیا جائے گا۔',
   'دولت به خپل واک او اختیارات د خلکو د ټاکل شویو استازو له لارې کاروي، چې پکې به د ډیموکراسۍ، ازادۍ، برابرۍ، زغم او ټولنیز انصاف پر اصولو د اسلامي لارښوونو سره سم عمل کېږي.')),
 (('3. Promotion of Islamic teachings in individual and collective life', '3۔ انفرادی اور اجتماعی زندگی میں اسلامی تعلیمات کا فروغ', '۳. په فردي او ټولنیز ژوند کې د اسلامي لارښوونو وده'),
  ('The state will enable Muslims to lead their individual and collective lives according to Islamic teachings.',
   'ریاست مسلمانوں کو اس قابل بنائے گی کہ وہ اپنی انفرادی اور اجتماعی زندگی اسلامی تعلیمات کے مطابق بسر کر سکیں۔',
   'دولت به مسلمانان دې وړ کړي چې خپل فردي او ټولنیز ژوند د اسلامي لارښوونو سره سم تېر کړي.')),
 (('4. Protection of the rights of minorities', '4۔ اقلیتوں کے حقوق کا تحفظ', '۴. د لږکیو د حقونو ساتنه'),
  ('Minorities will have complete freedom to practise their religion and to preach it. Moreover they will also be free to develop their culture and protect their legitimate interests.',
   'اقلیتوں کو اپنے مذہب پر عمل کرنے اور اس کی تبلیغ کرنے کی مکمل آزادی حاصل ہوگی۔ نیز وہ اپنے تمدن کی نشو و نما اور جائز مفادات کے تحفظ میں بھی آزاد ہوں گے۔',
   'لږکیو ته به په خپل دین د عمل او تبلیغ بشپړه ازادي وي. همداراز د خپل تمدن په وده او د مشروعو ګټو په ساتنه کې به هم ازاد وي.')),
 (('5. Protection of fundamental rights', '5۔ بنیادی حقوق کا تحفظ', '۵. د بنسټیزو حقونو ساتنه'),
  ('Citizens will have protection of all fundamental rights, e.g. freedom, equality, property, expression of opinion, belief, worship and association, and they will not be deprived of these rights.',
   'شہریوں کو تمام بنیادی حقوق مثلاً آزادی، مساوات، ملکیت، اظہارِ رائے، عقیدہ، عبادت اور انجمن سازی کے حقوق کا تحفظ حاصل ہوگا اور اُن کو ان حقوق سے محروم نہیں کیا جائے گا۔',
   'وګړو ته به د ټولو بنسټیزو حقونو لکه ازادۍ، برابرۍ، ملکیت، د بیان، عقیدې، عبادت او ټولنو جوړولو د حقونو ساتنه وي او له دې حقونو به بې‌برخې نه کېږي.')),
 (('6. Federal form of government and provincial autonomy', '6۔ وفاقی طرزِ حکومت اور صوبائی خود مختاری', '۶. فدرالي حکومت او ولایتي خپلواکي'),
  ('The units included in Pakistan will form a federation in which the units (provinces) will have autonomy.',
   'پاکستان میں شامل ادارے ایک وفاق کی تشکیل کریں گے جس میں وحدتوں (صوبوں) کو خود مختاری حاصل ہوگی۔',
   'په پاکستان کې شامل واحدونه به یو فدراسیون جوړوي، چې پکې به واحدونو (ولایتونو) ته خپلواکي وي.')),
 (('7. Independence of the judiciary', '7۔ عدلیہ کی آزادی', '۷. د قضا خپلواکي'),
  ('In the constitution the independence of the judiciary will have complete protection, i.e. no governmental or non-governmental pressure of any kind will be put on it in making decisions.',
   'دستور میں عدلیہ کی آزادی کو مکمل تحفظ حاصل ہوگا یعنی فیصلے کرنے میں اس پر کسی قسم کا حکومتی یا غیر حکومتی دباؤ نہیں ڈالا جائے گا۔',
   'په اساسي قانون کې به د قضا خپلواکۍ ته بشپړه ساتنه وي، یعنې د پرېکړو په کولو کې به پرې هېڅ ډول حکومتي یا غیر حکومتي فشار نه اچول کېږي.')),
]:
    H(*h); P(*p)
P('After the approval of this resolution, a Basic Principles Committee for framing the country’s constitution was also formed on the same day, and to advise this committee on Islamic teachings a Board of Islamic Teachings was also formed. Maulana Syed Sulaiman Nadvi was appointed chairman of this board.',
  'اس قرارداد کی منظوری کے بعد ملکی آئین بنانے کے لیے بنیادی اصولوں کی کمیٹی بھی اسی دن تشکیل دی گئی اور اس کمیٹی کو مشورہ دینے کے لیے تعلیماتِ اسلامی بورڈ کی بھی تشکیل کی گئی۔ مولانا سید سلیمان ندوی کو اس بورڈ کا چیئرمین مقرر کیا گیا۔',
  'د دې پرېکړه‌لیک له تصویب وروسته د هېواد د اساسي قانون د جوړولو لپاره د بنسټیزو اصولو کمېټه هم په همدې ورځ جوړه شوه، او دې کمېټې ته د مشورې لپاره د اسلامي لارښوونو بورډ هم جوړ شو. مولانا سید سلیمان ندوي د دې بورډ رئیس وټاکل شو.')
H('Importance of the Objectives Resolution', 'قراردادِ مقاصد کی اہمیت', 'د موخو پرېکړه‌لیک اهمیت')
P('The Objectives Resolution has special importance in the history of constitution-making in Pakistan. This resolution ended the ongoing controversial debate in the country regarding the form and character of the constitution and made it clear that Pakistan’s …',
  'قراردادِ مقاصد پاکستان کی دستور سازی کی تاریخ میں خاص اہمیت کی حامل ہے۔ اس قرارداد نے ملک میں دستور کی شکل اور کردار کے حوالے سے جاری اختلافی بحث کو ختم کر دیا اور یہ واضح کر دیا کہ پاکستان کا …',
  'د موخو پرېکړه‌لیک د پاکستان د اساسي قانون جوړونې په تاریخ کې ځانګړی اهمیت لري. دې پرېکړه‌لیک په هېواد کې د اساسي قانون د بڼې او رول په اړه روان اختلافي بحث پای ته ورساوه او روښانه یې کړه چې د پاکستان …')
rec = BOOK.record(t, 'pak12-ch4-text-2', 'Chapter 4 text (2)', 'بابِ چہارم — متن (۲)', 'څلورم څپرکی — متن (۲)', 39, [67, 68])

if __name__ == '__main__':
    BOOK.save(39, [(4, rec)])
