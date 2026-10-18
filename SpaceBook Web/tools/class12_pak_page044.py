"""Pak Studies XII PDF44 (spread): printed pp.77–78 — Ch.4 duties of citizens 1–9."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
def P(*v): t.p(*v)
def H(*v): t.h(*v)
H('Duties of citizens', 'شہریوں کے فرائض', 'د وګړو دندې')
P('Where the citizens of Pakistan have equal rights, some responsibilities are also laid upon them, because rights and duties are closely related to each other, and no society can progress without establishing a balance between them. The duties of a Pakistani citizen are as follows.',
  'پاکستان کے شہریوں کو جہاں مساوی حقوق حاصل ہیں۔ وہاں ان پر کچھ ذمہ داریاں بھی عائد ہوتی ہیں کیونکہ حقوق اور فرائض کا آپس میں گہرا تعلق ہے، اور ان میں توازن قائم کیے بغیر کوئی معاشرہ ترقی نہیں کر سکتا۔ پاکستانی شہری کے فرائض مندرجہ ذیل ہیں۔',
  'د پاکستان وګړو ته چې چېرته برابر حقونه حاصل دي، هلته پرې ځینې مسؤولیتونه هم لازم دي، ځکه حقونه او دندې یو له بل سره ژوره اړیکه لري، او پرته له دې چې ترمنځ یې توازن جوړ شي، هېڅ ټولنه پرمختګ نه شي کولی. د پاکستاني وګړي دندې دا دي:')
for h, p in [
 (('1. Loyalty to the country', '1۔ ملک سے وفاداری', '۱. له هېواد سره وفاداري'),
  ('It is incumbent on a good Pakistani citizen that he remain loyal to the state of Pakistan and not be involved in any activity that falls into the category of treason against the country.',
   'ایک اچھے پاکستانی شہری پر لازم ہے کہ وہ ریاستِ پاکستان کا وفادار رہے اور کسی ایسی سرگرمی میں ملوث نہ ہو جو ملک کے ساتھ غداری کے زمرے میں آتی ہو۔',
   'پر یوه ښه پاکستاني وګړي لازمه ده چې د پاکستان دولت ته وفادار پاتې شي او په داسې هېڅ فعالیت کې ښکېل نه شي چې د هېواد سره د غدارۍ په کټګورۍ کې راځي.')),
 (('2. Respect for the law', '2۔ قانون کا احترام', '۲. د قانون درناوی'),
  ('It is the moral and legal duty of every citizen to respect all national and state laws and not to violate the law in any case.',
   'ہر شہری کا اخلاقی اور قانونی فرض ہے کہ وہ تمام ملکی اور ریاستی قوانین کا احترام کرے اور کسی بھی صورت میں قانون کی خلاف ورزی نہ کرے۔',
   'د هر وګړي اخلاقي او قانوني دنده ده چې د هېواد او دولت د ټولو قوانینو درناوی وکړي او په هېڅ صورت کې د قانون سرغړونه ونه کړي.')),
 (('3. Payment of taxes', '3۔ ٹیکسوں کی ادائیگی', '۳. د مالیو ورکړه'),
  ('It is the responsibility of citizens to pay on time all the taxes imposed by the government, because without their payment it will not be possible to run the government administration and to carry out development work for the welfare of the people.',
   'شہریوں کی ذمہ داری ہے کہ وہ حکومت کی طرف سے عائد کردہ تمام ٹیکس بروقت ادا کریں کیونکہ ان کی ادائیگی کے بغیر حکومتی انتظامات چلانا اور عوام کی فلاح و بہبود کے لیے ترقیاتی کام کرنا ممکن نہیں ہوگا۔',
   'د وګړو مسؤولیت دی چې د حکومت له خوا لګول شوې ټولې مالیې په خپل وخت ورکړي، ځکه پرته له دې د حکومتي ترتیباتو چلول او د خلکو د هوساینې لپاره پراختیايي کارونه ممکن نه دي.')),
 (('4. Proper use of the right to vote', '4۔ ووٹ کے حق کا صحیح استعمال', '۴. د رایې د حق سمه کارونه'),
  ('The proper use of the right to vote is the most important duty among the basic responsibilities of every good citizen. Citizens should vote for honest candidates of good character, so that the political system of the country is strengthened and corruption can be eliminated.',
   'ووٹ کے حق کا صحیح استعمال ہر اچھے شہری کی بنیادی ذمہ داریوں میں اہم ترین فریضہ ہے۔ شہریوں کو چاہیے کہ وہ دیانت دار اور اچھے کردار کے حامل اُمیدواروں کو ووٹ دیں تاکہ ملک کا سیاسی نظام مضبوط ہو اور بدعنوانی کا خاتمہ کیا جا سکے۔',
   'د رایې د حق سمه کارونه د هر ښه وګړي د بنسټیزو مسؤولیتونو تر ټولو مهمه دنده ده. وګړي باید ایماندارو او ښه کرکټر لرونکو نوماندانو ته رایه ورکړي، څو د هېواد سیاسي نظام پیاوړی شي او فساد له منځه یوړل شي.')),
 (('5. Social service', '5۔ سماجی خدمت', '۵. ټولنیز خدمت'),
  ('The citizen of a democratic country is morally bound to take part in social service and in works for the welfare and betterment of society.',
   'ایک جمہوری ملک کا شہری اخلاقی طور پر اس بات کا پابند ہوتا ہے کہ وہ سماجی خدمت اور معاشرے کی فلاح و بہبود کے کاموں میں حصہ لے۔',
   'د یوه دیموکراتیک هېواد وګړی په اخلاقي توګه پابند وي چې په ټولنیز خدمت او د ټولنې د هوساینې او ښېګڼې په کارونو کې ګډون وکړي.')),
 (('6. Supremacy of the national interest', '6۔ قومی مفاد کی بالادستی', '۶. د ملي ګټو لوړوالی'),
  ('As Pakistani citizens it is our duty to give priority to the national and community interest over personal interests and to stay away from all activities that are contrary to the national interest.',
   'پاکستانی شہری ہونے کے ناطے ہمارا فرض بنتا ہے کہ ہم ملکی اور قومی مفاد کو ذاتی مفادات پر ترجیح دیں اور ایسی تمام سرگرمیوں سے دور رہیں جو قومی مفادات کے منافی ہوں۔',
   'د پاکستاني وګړو په توګه زموږ دنده ده چې هېوادني او ملي ګټو ته پر شخصي ګټو لومړیتوب ورکړو او له داسې ټولو فعالیتونو لرې پاتې شو چې د ملي ګټو خلاف وي.')),
 (('7. Acquiring education', '7۔ تعلیم کا حصول', '۷. د زده‌کړې ترلاسه کول'),
  ('Where acquiring education is part of one’s rights, it is also counted among one’s duties. It is every person’s duty to acquire education himself and to get his children educated too, because progress is not possible without education.',
   'تعلیم کا حاصل کرنا جہاں حقوق کا حصہ ہے وہاں اس کا شمار فرائض میں بھی ہوتا ہے۔ ہر شخص کا فرض ہے کہ وہ خود بھی تعلیم حاصل کرے اور اپنے بچوں کو بھی تعلیم دلوائے کیونکہ تعلیم کے بغیر ترقی ممکن نہیں۔',
   'د زده‌کړې ترلاسه کول چې چېرته د حقونو برخه ده، هلته په دندو کې هم شمېرل کېږي. د هر چا دنده ده چې پخپله هم زده‌کړه وکړي او خپلو ماشومانو ته هم زده‌کړه ورکړي، ځکه پرته له زده‌کړې پرمختګ ممکن نه دی.')),
 (('8. Hard work', '8۔ محنت', '۸. زیار'),
  ('It is every citizen’s responsibility to meet his needs and play his full role in the progress of the country.',
   'ہر شہری کی ذمہ داری ہے کہ وہ اپنی ضروریات کو پورا کرنے اور ملک کی ترقی میں اپنا بھرپور کردار ادا کرے۔',
   'د هر وګړي مسؤولیت دی چې خپلې اړتیاوې پوره کړي او د هېواد په پرمختګ کې خپل بشپړ رول ولوبوي.')),
 (('9. Human rights', '9۔ انسانی حقوق', '۹. بشري حقونه'),
  ('The concept of human rights was first given by our beloved Holy Prophet, Hazrat Muhammad, Messenger of Allah, Seal of the Prophets (peace and blessings of Allah be upon him, his family and companions), fourteen hundred years ago. This was the regular charter of human rights, which laid the foundation of basic human rights. In the modern age too human rights have been given considerable importance. Every country moving towards democracy began to adopt constitutions. Following France, a chapter on fundamental rights began to be included in the constitution of every country. Likewise, when Pakistan brought its first constitution in 1956, a chapter on fundamental rights became an essential part of it.',
   'انسانی حقوق کا تصور سب سے پہلے ہمارے پیارے نبی کریم حضرت محمد رسول اللہ خاتم النبیین صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم نے آج سے چودہ سو سال پہلے دے دیا تھا۔ یہ باقاعدہ انسانی حقوق کا چارٹر تھا۔ جس نے انسانی بنیادی حقوق کی بنیاد رکھی۔ جدید دور میں بھی انسانی حقوق کو کافی اہمیت دی گئی ہے۔ ہر ملک جمہوریت کی طرف رواں دواں ہوا اور دساتیر کو اپنانا شروع کر دیا۔ فرانس کی تقلید کرتے ہوئے ہر ملک کے دستور میں بنیادی حقوق کا ایک باب شامل کیا جانے لگا۔ اسی طرح جب پاکستان نے 1956ء میں پہلا دستور لایا گیا تو بنیادی حقوق کا ایک باب اس کا ضروری حصہ بنا۔',
   'د بشري حقونو تصور تر ټولو لومړی زموږ ګران نبي کریم حضرت محمد رسول الله خاتم النبیین صلی الله علیه وعلی آله واصحابه وسلم نن څوارلس سوه کاله مخکې ورکړی و. دا د بشري حقونو منظم منشور و، چې د انسان د بنسټیزو حقونو بنسټ یې کېښود. په نوي عصر کې هم بشري حقونو ته ډېر اهمیت ورکړل شوی. هر هېواد ډیموکراسۍ ته روان شو او اساسي قوانین یې غوره کړل. د فرانسې په پیروۍ د هر هېواد په اساسي قانون کې د بنسټیزو حقونو یو څپرکی شاملېده. همداسې کله چې پاکستان په ۱۹۵۶ز کې لومړی اساسي قانون راوړ، د بنسټیزو حقونو یو څپرکی یې اړینه برخه شو.')),
]:
    H(*h); P(*p)
rec = BOOK.record(t, 'pak12-ch4-text-7', 'Chapter 4 text (7)', 'بابِ چہارم — متن (۷)', 'څلورم څپرکی — متن (۷)', 44, [77, 78])
issues = [{'id': 'pak12-pdf044', 'unit': 4, 'printedPage': 78, 'description': 'p.78 prints “جب پاکستان نے 1956ء میں پہلا دستور لایا گیا” (mixed active/passive construction) — retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(44, [(4, rec)], issues=issues)
