"""PDF42 (printed 71–72): point-by-point structure; connectives of comparison and contrast with examples; B essay task; Oral Communication."""
from class12_book_common import Book, Builder

BOOK = Book('english')
w = Builder()
w.h('2. Point-by-Point Structure', '2. نکتہ بہ نکتہ ساخت', '2. ټکی په ټکی جوړښت')
w.p('For the point-by-point structure, each similarity (or difference) for one object is followed immediately by the similarity (or difference) for the other.', 'نکتہ بہ نکتہ ساخت میں ایک چیز کی ہر مماثلت (یا فرق) کے فوراً بعد دوسری چیز کی مماثلت (یا فرق) بیان کی جاتی ہے۔', 'په ټکي په ټکي جوړښت کې د یوه شي هر ورته‌والی (یا توپیر) سمدستي د بل شي ورته‌والي (یا توپیر) سره تعقیبېږي.')
PS = ['Introduction', 'Point 1: Object 1 ➤ Object 2', 'Point 2: Object 1 ➤ Object 2', 'Point 3: Object 1 ➤ Object 2', 'Conclusion']
PU = ['تعارف', 'نکتہ 1: شے 1 ➤ شے 2', 'نکتہ 2: شے 1 ➤ شے 2', 'نکتہ 3: شے 1 ➤ شے 2', 'اختتامیہ']
PP = ['پېژندنه', 'ټکی 1: شی 1 ➤ شی 2', 'ټکی 2: شی 1 ➤ شی 2', 'ټکی 3: شی 1 ➤ شی 2', 'پایله']
w.table('eng12-u07-point', ['Point-by-Point'], [[x] for x in PS], ['نکتہ بہ نکتہ'], ['ټکی په ټکی'], [[x] for x in PU], [[x] for x in PP])
w.h('Connectives of comparison and contrast', 'موازنے اور تقابل کے ربطی الفاظ', 'د پرتلې او توپیر اړیکه‌ییز توري')
w.p('Connectives of comparison and contrast are transitional devices which show the similarities or differences. So commonly used transitional devices of comparison and contrast are given below.', 'موازنے اور تقابل کے ربطی الفاظ وہ عبوری ذرائع ہیں جو مماثلتیں یا فرق ظاہر کرتے ہیں۔ موازنے اور تقابل کے کچھ عام استعمال ہونے والے عبوری ذرائع نیچے دیے گئے ہیں۔', 'د پرتلې او توپیر اړیکه‌ییز توري هغه انتقالي وسایل دي چې ورته‌والي یا توپیرونه ښيي. د پرتلې او توپیر ځینې عام کارېدونکي انتقالي وسایل لاندې ورکړل شوي.')
w.h('Connectives of Comparison', 'موازنے کے ربطی الفاظ', 'د پرتلې اړیکه‌ییز توري')
CC = ['similarly', 'likewise', 'also', 'both... and...', 'not only... but also...', 'neither... nor...', 'just like (+ noun)', 'similar to (+ noun)', 'to be similar (to)', 'to be the same as', 'to be alike', 'to compare (to/with)']
R = [[x] for x in CC]
w.table('eng12-u07-comparison', ['Connective'], R, ['ربطی لفظ'], ['اړیکه‌ییز توری'], R, R)
w.h('Examples', 'مثالیں', 'بېلګې')
for x in [
    ('Computers can be used to communicate easily, for example via email. Similarly/Likewise, the mobile phone is a convenient tool for communication.', 'کمپیوٹر آسانی سے رابطے کے لیے استعمال کیے جا سکتے ہیں، مثلاً ای میل کے ذریعے۔ اسی طرح موبائل فون بھی رابطے کا ایک آسان ذریعہ ہے۔', 'کمپیوټرونه په اسانۍ د اړیکې لپاره کارول کېدای شي، د بېلګې په توګه د برېښنالیک له لارې. همداسې، ګرځنده تلیفون هم د اړیکې یوه اسانه وسیله ده.'),
    ('Both computers and mobile phones can be used to communicate easily with other people.', 'کمپیوٹر اور موبائل فون دونوں دوسرے لوگوں سے آسانی سے رابطے کے لیے استعمال کیے جا سکتے ہیں۔', 'کمپیوټرونه او ګرځنده تلیفونونه دواړه له نورو خلکو سره د اسانه اړیکې لپاره کارول کېدای شي.'),
    ('Just like the computer, the mobile phone can be used to communicate easily with other people.', 'کمپیوٹر کی طرح موبائل فون بھی دوسرے لوگوں سے آسانی سے رابطے کے لیے استعمال کیا جا سکتا ہے۔', 'د کمپیوټر په څېر، ګرځنده تلیفون هم له نورو خلکو سره د اسانه اړیکې لپاره کارول کېدای شي.'),
    ('The computer is similar to the mobile phone in the way it can be used for easy communication.', 'کمپیوٹر آسان رابطے کے لیے استعمال ہونے کے لحاظ سے موبائل فون سے ملتا جلتا ہے۔', 'کمپیوټر د اسانه اړیکې لپاره د کارېدو له پلوه له ګرځنده تلیفون سره ورته دی.'),
]: w.p(*x)
w.h('Connectives of Contrast', 'تقابل کے ربطی الفاظ', 'د توپیر اړیکه‌ییز توري')
CT = ['however', 'in contrast', 'in comparison', 'by comparison', 'on the other hand', 'while', 'whereas', 'but', 'to differ from', 'to be different (from)', 'to be dissimilar to', 'to be unlike']
R = [[x] for x in CT]
w.table('eng12-u07-contrast', ['Connective'], R, ['ربطی لفظ'], ['اړیکه‌ییز توری'], R, R)
w.h('Examples', 'مثالیں', 'بېلګې')
for x in [
    ('Computers, although increasingly small, are not always easy to carry from one place to another. However, the mobile phone can be carried with ease.', 'کمپیوٹر اگرچہ چھوٹے سے چھوٹے ہوتے جا رہے ہیں، ہمیشہ ایک جگہ سے دوسری جگہ لے جانا آسان نہیں ہوتا۔ تاہم موبائل فون آسانی سے ساتھ لے جایا جا سکتا ہے۔', 'کمپیوټرونه که څه هم مخ پر کوچنیوالي دي، تل له یوه ځایه بل ځای ته وړل اسانه نه دي. خو ګرځنده تلیفون په اسانۍ وړل کېدای شي.'),
    ('Computers are generally not very portable, whereas the mobile phone is.', 'کمپیوٹر عموماً زیادہ قابلِ نقل نہیں ہوتے، جبکہ موبائل فون ہوتا ہے۔', 'کمپیوټرونه عموماً ډېر د وړلو وړ نه دي، په داسې حال کې چې ګرځنده تلیفون دی.'),
    ('Computers differ from mobile phones in their lack of portability.', 'کمپیوٹر قابلِ نقل نہ ہونے میں موبائل فون سے مختلف ہیں۔', 'کمپیوټرونه د وړلو د نه وړتیا له امله له ګرځنده تلیفونونو توپیر لري.'),
    ('Computers are unlike mobile phones in their lack of portability.', 'کمپیوٹر قابلِ نقل نہ ہونے میں موبائل فون کے برعکس ہیں۔', 'کمپیوټرونه د وړلو د نه وړتیا له پلوه د ګرځنده تلیفونونو پر خلاف دي.'),
]: w.p(*x)
w.p('B. Keeping in view the text of \'Truck Art\'and the patte rn of comparison and contrast organization in composition; write an expository essay on "Old Means of Communication vs Modern Means of Communication".', 'B. ’’ٹرک آرٹ‘‘ کے متن اور انشاء میں موازنے اور تقابل کی ترتیب کے انداز کو مدِ نظر رکھتے ہوئے ’’رابطے کے پرانے ذرائع بمقابلہ رابطے کے جدید ذرائع‘‘ پر ایک توضیحی مضمون لکھیں۔', 'B. د "د ټرک هنر" متن او په انشا کې د پرتلې او توپیر د تنظیم بڼه په پام کې ونیسئ؛ د "د اړیکې زړې وسیلې د اړیکې د عصري وسیلو پر وړاندې" په اړه یوه توضیحي مقاله ولیکئ.')
w.h('Oral Communication', 'زبانی ابلاغ', 'د خولې اړیکه')
w.p('Students are separately given a random word like sun, star or moon. The rest of the students must not see the word and thus each student will explain the word. The other students listen carefully to the speech and attempt to guess the secret word.', 'طلبہ کو الگ الگ کوئی تصادفی لفظ دیا جاتا ہے جیسے سورج، ستارہ یا چاند۔ باقی طلبہ وہ لفظ نہ دیکھیں، اور یوں ہر طالب علم لفظ کی وضاحت کرے گا۔ دوسرے طلبہ غور سے بات سنیں اور خفیہ لفظ کا اندازہ لگانے کی کوشش کریں۔', 'زده کوونکو ته په جلا توګه یوه تصادفي کلمه ورکول کېږي لکه لمر، ستوری یا سپوږمۍ. پاتې زده کوونکي باید کلمه ونه ویني او په دې توګه به هر زده کوونکی کلمه تشریح کړي. نور زده کوونکي وینا ته په پام غوږ نیسي او د پټې کلمې د اټکل هڅه کوي.')
rec = BOOK.record(w, 'eng12-u07-writing-b', 'Writing — point-by-point, connectives; essay task; Oral Communication', 'تحریر — نکتہ بہ نکتہ، ربطی الفاظ؛ مضمون؛ زبانی ابلاغ', 'لیکنه — ټکی په ټکی، اړیکه‌ییز توري؛ مقاله؛ د خولې اړیکه', 42, [71, 72])
issues = [{'id': 'eng12-p71-72', 'unit': 7, 'printedPage': 71, 'description': 'Printed text retained: “So commonly used transitional devices” (Some), “‘Truck Art’and the patte rn”, and duplicated heading text (“Point-by-Point / Introduction … Conclusion”) around the diagram. Diagrams reproduced as one-column structured tables.'}]

if __name__ == '__main__':
    BOOK.save(42, [(7, rec)], issues=issues)
