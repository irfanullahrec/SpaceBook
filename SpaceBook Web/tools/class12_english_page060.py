"""PDF60 (printed 107–108): Unit 11 transitional devices list (by function); Activity A (fill in, 1–10), B (transition words 1–8)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
B = '________'
w = Builder()
w.p('Here is a list of some common transitional devices that can be used to cue readers in a given way.', 'یہاں کچھ عام عبوری ذرائع کی فہرست ہے جو قارئین کو کسی خاص سمت میں اشارہ دینے کے لیے استعمال کیے جا سکتے ہیں۔', 'دلته د ځینو عامو انتقالي وسایلو لست دی چې لوستونکو ته په یوه ټاکلي ډول د اشارې لپاره کارول کېدای شي.')
TD = [
    (('TO ADD:', 'اضافہ کے لیے:', 'د زیاتولو لپاره:'), "and, again, and then, besides, equally important, finally, further, furthermore, nor, too, next, lastly, what's more, moreover, in addition, first (second, etc.)"),
    (('TO COMPARE:', 'موازنہ کے لیے:', 'د پرتلې لپاره:'), 'whereas, but, yet, on the other hand, however, nevertheless, on the contrary, by comparison, where, compared to, up against, balanced against, vis a vis, but, although, conversely, meanwhile, after all, in contrast, although this may be true, etc.'),
    (('TO PROVE:', 'ثابت کرنے کے لیے:', 'د ثابتولو لپاره:'), 'because, for, since, for the same reason, obviously, evidently, furthermore, moreover, besides, indeed, in fact, in addition, in any case, that is, etc.'),
    (('TO SHOW EXCEPTION:', 'استثنا ظاہر کرنے کے لیے:', 'د استثنا د ښودلو لپاره:'), 'yet, still, however, nevertheless, in spite of, despite, of course, once in a while, sometimes,etc.'),
    (('TO SHOW TIME:', 'وقت ظاہر کرنے کے لیے:', 'د وخت د ښودلو لپاره:'), 'immediately, thereafter, soon, after a few hours, finally, then, later, previously, formerly, first (second, etc.), next, and then, etc.'),
    (('TO REPEAT:', 'دہرانے کے لیے:', 'د تکرار لپاره:'), 'in brief, as I have said, as I have noted, as has been noted, etc.'),
    (('TO EMPHASIZE:', 'تاکید کے لیے:', 'د ټینګار لپاره:'), 'definitely, extremely, obviously, in fact, indeed, in any case, absolutely, positively, naturally, surprisingly, always, forever, perennially, eternally, never, emphatically, unquestionably, without a doubt, certainly, undeniably, without reservation, etc.'),
    (('TO SHOW SEQUENCE:', 'ترتیب ظاہر کرنے کے لیے:', 'د ترتیب د ښودلو لپاره:'), 'first, second, third, and so forth. A, B, C, and so forth. next, then, following this, at this time, now, at this point, after, afterward, subsequently, finally, consequently, previously, before this, simultaneously, concurrently, thus, therefore, hence, next, and then, soon, etc.'),
    (('TO GIVE AN EXAMPLE:', 'مثال دینے کے لیے:', 'د بېلګې د ورکولو لپاره:'), 'for example, for instance, in this case, in another case, on this occasion, in this situation, take the case of, to demonstrate, to illustrate, as an illustration, to illustrate, etc.'),
    (('TO SUMMARIZE OR CONCLUDE:', 'خلاصہ یا نتیجہ کے لیے:', 'د لنډیز یا پایلې لپاره:'), 'in brief, on the whole, summing up, to conclude, in conclusion, as I have shown, as I have said, hence, therefore, accordingly, thus, as a result, consequently, etc.'),
]
for head, words in TD:
    w.h(*head)
    w.p(words, words, words); w.paras[-1]['untranslatedByDesign'] = True
w.h('Activity', 'سرگرمی', 'فعالیت')
w.p('A. Fill in the blanks with appropriate transitional word/phrase of different types given in the box', 'A. خانے میں دیے گئے مختلف اقسام کے موزوں عبوری لفظ/فقرے سے خالی جگہیں پُر کریں', 'A. تش ځایونه په بکس کې د ورکړل شویو بېلابېلو ډولونو د مناسب انتقالي کلمې/عبارت سره ډک کړئ')
BX = 'nearby, similarly, even if, ultimately, in the meantime, consequently, furthermore, in other words'
w.p(BX, BX, BX); w.paras[-1]['untranslatedByDesign'] = True
A = [(f'{B}, the teachers were meeting in a closed-door session. (place and space)', f'{B}، اساتذہ ایک بند کمرے کے اجلاس میں مصروف تھے۔ (جگہ اور مقام)', f'{B}، ښوونکي په یوه تړلې غونډه کې وو. (ځای او فضا)'),
     (f'{B}, the harvest dance was also held on a Friday night. (comparison / contrast)', f'{B}، فصل کی کٹائی کا رقص بھی جمعہ کی رات منعقد ہوا۔ (موازنہ / تقابل)', f'{B}، د حاصل د رېبلو نڅا هم د جمعې په شپه وشوه. (پرتله / توپیر)'),
     (f"{B} the school district pays for half of the students' breakfasts, there still will be those without enough resources to pay for the remaining amount. (cause / purpose)", f'{B} اسکول ڈسٹرکٹ طلبہ کے آدھے ناشتے کی ادائیگی کرتا ہے، پھر بھی ایسے لوگ ہوں گے جن کے پاس باقی رقم ادا کرنے کے لیے کافی وسائل نہیں ہوں گے۔ (سبب / مقصد)', f'{B} د ښوونځي ولسوالي د زده کوونکو د نیمایي ناري پیسې ورکوي، بیا به هم داسې کسان وي چې د پاتې پیسو د ورکولو لپاره کافي سرچینې نه لري. (لامل / موخه)'),
     (f"{B}, no one has more influence on a student 's grades than the student himself. (conclusion / summary)", f'{B}، کسی طالب علم کے نمبروں پر خود طالب علم سے زیادہ کسی کا اثر نہیں ہوتا۔ (نتیجہ / خلاصہ)', f'{B}، د یوه زده کوونکي پر نمرو هېڅوک تر پخپله زده کوونکي ډېر اغېز نه لري. (پایله / لنډیز)'),
     (f'{B}, the library will be closed during lunch. (time / sequence)', f'{B}، دوپہر کے کھانے کے دوران لائبریری بند رہے گی۔ (وقت / ترتیب)', f'{B}، د غرمې ډوډۍ پر مهال کتابتون به تړلی وي. (وخت / ترتیب)'),
     (f'{B}, fewer students are able to take courses in the fine arts: music, art, and drama. (effect / result / qualification)', f'{B}، کم طلبہ فنونِ لطیفہ: موسیقی، مصوری اور ڈراما کے کورسز لے پاتے ہیں۔ (اثر / نتیجہ / شرط)', f'{B}، لږ زده کوونکي وکولای شي په ښکلو هنرونو: موسیقۍ، هنر او ډرامې کې کورسونه واخلي. (اغېز / پایله / شرط)'),
     (f'{B}, the student council has unanimously endorsed the revised calendar for the school. (addition / extension)', f'{B}، طلبہ کونسل نے اسکول کے نظرِ ثانی شدہ کیلنڈر کی متفقہ توثیق کر دی ہے۔ (اضافہ / توسیع)', f'{B}، د زده کوونکو شورا د ښوونځي بیاکتل شوې جنتري په اتفاق تایید کړې. (زیاتوالی / پراختیا)'),
     (f'{B}, a longer school day may provide more opportunities instead of fewer. (example /clarification/ emphasis )', f'{B}، اسکول کا طویل دن کم کے بجائے زیادہ مواقع فراہم کر سکتا ہے۔ (مثال / وضاحت / تاکید)', f'{B}، د ښوونځي اوږده ورځ کېدای شي د لږو پر ځای ډېر فرصتونه برابر کړي. (بېلګه / روښانتیا / ټینګار)')]
w.group('lines', [(f'{i}. {e}', f'{i}. {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(A, 1)])
w.p('B. Use the correct transition words in the blank spaces below from list of transition words in the box.', 'B. خانے میں دی گئی عبوری الفاظ کی فہرست سے نیچے خالی جگہوں میں درست عبوری الفاظ استعمال کریں۔', 'B. په بکس کې د انتقالي کلمو له لست څخه په لاندې تشو ځایونو کې سمې انتقالي کلمې وکاروئ.')
BX2 = 'therefore, for example, consequently, meanwhile, likewise, although'
w.p(BX2, BX2, BX2); w.paras[-1]['untranslatedByDesign'] = True
Bt = [(f'Tim earned an A on the test; {B},Justin also received an A.', f'ٹم نے ٹیسٹ میں A گریڈ لیا؛ {B}، جسٹن نے بھی A گریڈ لیا۔', f'ټیم په ازموینه کې A وګاټه؛ {B}، جسټن هم A ترلاسه کړ.'),
      (f'The book was interesting; {B}, it was hard to read.', f'کتاب دلچسپ تھی؛ {B}، اسے پڑھنا مشکل تھا۔', f'کتاب زړه‌راښکونکی و؛ {B}، لوستل یې سخت وو.'),
      (f'Gordon finished his chores early; {B}, he had time to play football.', f'گورڈن نے اپنے کام جلدی ختم کر لیے؛ {B}، اس کے پاس فٹ بال کھیلنے کا وقت تھا۔', f'ګورډن خپل کارونه ژر بشپړ کړل؛ {B}، د فوټبال لوبې لپاره یې وخت درلود.'),
      (f"Sarah's horse is beautiful; {B}, it is well-bred.", f'سارہ کا گھوڑا خوبصورت ہے؛ {B}، یہ اچھی نسل کا ہے۔', f'د سارې آس ښکلی دی؛ {B}، ښه نسل لري.'),
      (f'The sailors prepared the ship to sail; {B}, the dock workers loaded the cargo.', f'ملاحوں نے جہاز کو روانگی کے لیے تیار کیا؛ {B}، گودی کے مزدوروں نے سامان لادا۔', f'ملاحانو بېړۍ د تګ لپاره چمتو کړه؛ {B}، د بندر کارګرانو بار بار کړ.'),
      (f"Her sister had a cold; {B}, Julie's family canceled the trip.", f'اس کی بہن کو زکام تھا؛ {B}، جولی کے خاندان نے سفر منسوخ کر دیا۔', f'خور یې زکام وه؛ {B}، د جولي کورنۍ سفر لغوه کړ.'),
      (f'Oranges are good for you; {B}, they are full of vitamin C.', f'مالٹے آپ کے لیے مفید ہیں؛ {B}، ان میں وٹامن سی بھرپور ہے۔', f'مالټې ستاسو لپاره ګټورې دي؛ {B}، له ویټامین C ډکې دي.'),
      (f'Two seats were left on the bus; {B}, most of the group had to wait for the next one.', f'بس میں دو نشستیں باقی تھیں؛ {B}، گروہ کے زیادہ تر افراد کو اگلی بس کا انتظار کرنا پڑا۔', f'په بس کې دوه څوکۍ پاتې وې؛ {B}، د ډلې ډېری غړي اړ شول چې د بل انتظار وکړي.')]
w.group('lines', [(f'{i}. {e}', f'{i}. {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(Bt, 1)])
rec = BOOK.record(w, 'eng12-u11-vocab-a', 'Transitional devices list; Activity A–B', 'عبوری ذرائع کی فہرست؛ سرگرمی A–B', 'د انتقالي وسایلو لست؛ فعالیت A–B', 60, [107, 108])
issues = [{'id': 'eng12-p107-108', 'unit': 11, 'printedPage': 108, 'description': 'Printed text retained: activity A numbers the category labels as separate lines (items 2 and 4 are category labels), “a student ’s grades”, “;  ,Justin”. Transitional word lists are kept in English in all views (marked untranslatedByDesign).'}]

if __name__ == '__main__':
    BOOK.save(60, [(11, rec)], issues=issues)
