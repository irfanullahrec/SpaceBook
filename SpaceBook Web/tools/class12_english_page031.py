"""PDF31 (printed 49–50): Unit 5 Vocabulary A (dictionary transcription); B three levels of syllable stress + examples + activity; C root words (start)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
B = '________'
w = Builder()
w.h('Vocabulary and Grammar', 'ذخیرۂ الفاظ اور قواعد', 'لغات او ګرامر')
w.p('A. Consult a dictionary and write the phonetic transcription of the following words.', 'A. لغت سے رجوع کریں اور درج ذیل الفاظ کی صوتی نقل لکھیں۔', 'A. قاموس ته مراجعه وکړئ او د لاندې کلمو غږیز لیکدود ولیکئ.')
W = ['Bike', 'Bus', 'Car', 'Tire', 'Ticket', 'Truck', 'Speed', 'Patrol', 'Road', 'Garage']
R = [[x, ''] for x in W]
w.table('eng12-u05-dict', ['Word', 'Phonetic Transcription'], R, ['لفظ', 'صوتی نقل'], ['کلمه', 'غږیز لیکدود'], R, R)
w.h('B. Three Levels of Syllable Stress in English', 'B. انگریزی میں ہجائی زور کی تین سطحیں', 'B. په انګلیسي کې د سیلاب د فشار درې کچې')
w.p("Syllables in English words don't all have the same level of loudness. Some are loud, some are short and quiet, some are in between.", 'انگریزی الفاظ کے تمام ہجوں کی بلندی کی سطح ایک جیسی نہیں ہوتی۔ کچھ بلند ہوتے ہیں، کچھ مختصر اور دھیمے، اور کچھ درمیانے۔', 'د انګلیسي کلمو ټول سیلابونه یو شان لوړوالی نه لري. ځینې لوړ دي، ځینې لنډ او ارام، او ځینې یې ترمنځ.')
w.h('English has three levels of stress:', 'انگریزی میں زور کی تین سطحیں ہیں:', 'انګلیسي د فشار درې کچې لري:')
for head, en, ur, ps in [
    (('1. Primary Stress', '1. بنیادی زور', '1. لومړنی فشار'), "The loudest syllable in the word. In one-syllable words, that one syllable has the primary stress (except for a handful of short function words like the, which might not have any stress at all). Primary stress is marked in IPA by putting a raised vertical line [ˈ] at the beginning of the syllable.",
     'لفظ کا سب سے بلند ہجا۔ یک ہجائی الفاظ میں وہی ایک ہجا بنیادی زور رکھتا ہے (سوائے چند مختصر نحوی الفاظ کے جیسے the، جن پر شاید کوئی زور نہ ہو)۔ IPA میں بنیادی زور ہجے کے شروع میں ایک اوپر اٹھی ہوئی عمودی لکیر [ˈ] لگا کر ظاہر کیا جاتا ہے۔',
     'په کلمه کې تر ټولو لوړ سیلاب. په یو‌سیلابه کلمو کې همدا یو سیلاب لومړنی فشار لري (پرته له یو شمېر لنډو دندیزو کلمو لکه the، چې کېدای شي هېڅ فشار ونه لري). په IPA کې لومړنی فشار د سیلاب په پیل کې د یوې پورته عمودي کرښې [ˈ] په ایښودو ښودل کېږي.'),
    (('2. Secondary Stress', '2. ثانوی زور', '2. دویمی فشار'), "Syllables which aren't completely unstressed, but aren't as loud as the primary stress. Secondary stress is marked with a lowered vertical line [ˌ] at the beginning of the syllable.",
     'وہ ہجے جو مکمل طور پر بے زور نہیں ہوتے، لیکن بنیادی زور جتنے بلند بھی نہیں ہوتے۔ ثانوی زور ہجے کے شروع میں ایک نیچی عمودی لکیر [ˌ] سے ظاہر کیا جاتا ہے۔',
     'هغه سیلابونه چې بشپړ بې‌فشاره نه دي، خو د لومړني فشار هومره لوړ هم نه دي. دویمی فشار د سیلاب په پیل کې د یوې ټیټې عمودي کرښې [ˌ] په واسطه ښودل کېږي.'),
    (('3. Unstressed Syllables', '3. بے زور ہجے', '3. بې‌فشاره سیلابونه'), 'Syllables that have no stress at all. In English, almost all of these have schwa [ə] for their vowel, though [i] will also often be unstressed, like the [i] in happy [ˈhæpi]. (Very rarely, another non-schwa vowel might be unstressed, like the [o] of potato [pəˈteto] for most speakers.)',
     'وہ ہجے جن پر بالکل زور نہیں ہوتا۔ انگریزی میں ان میں سے تقریباً سب کا مصوتہ شوا [ə] ہوتا ہے، اگرچہ [i] بھی اکثر بے زور ہوتا ہے، جیسے happy [ˈhæpi] میں [i]۔ (بہت ہی کم کوئی اور غیر شوا مصوتہ بے زور ہو سکتا ہے، جیسے زیادہ تر بولنے والوں کے لیے potato [pəˈteto] کا [o]۔)',
     'هغه سیلابونه چې هېڅ فشار نه لري. په انګلیسي کې نږدې ټول یې د خپل غږلرونکي په توګه شوا [ə] لري، که څه هم [i] هم اکثرا بې‌فشاره وي، لکه په happy [ˈhæpi] کې [i]. (ډېر کم کېدای شي بل غیرشوا غږلرونکی بې‌فشاره وي، لکه د ډېرو ویونکو لپاره د potato [pəˈteto] [o].)'),
]:
    w.h(*head); w.p(en, ur, ps)
w.h('Examples:', 'مثالیں:', 'بېلګې:')
EX = [["[əˈnʌf]", 'enough'], ["[ˌmænəˈtobə]", 'Manitoba'], ["[ˈfotəˌgræf]", 'photograph']]
w.table('eng12-u05-stress-ex', ['IPA', 'Word'], EX, ['IPA', 'لفظ'], ['IPA', 'کلمه'], EX, EX)
w.p('A good example of the difference between secondary stress and the complete absence of stress is the final syllable of delegate, used as a verb and used as a noun.', 'ثانوی زور اور زور کی مکمل غیر موجودگی کے فرق کی ایک اچھی مثال لفظ delegate کا آخری ہجا ہے، جب اسے فعل اور اسم کے طور پر استعمال کیا جائے۔', 'د دویمي فشار او د فشار د بشپړ نشتوالي ترمنځ د توپیر یوه ښه بېلګه د delegate کلمې وروستی سیلاب دی، کله چې د فعل او نوم په توګه وکارول شي.')
DL = [["[ˈdɛləˌget]", 'verb: You have to delegate your responsibilities'], ["[ˈdɛləgət]", 'noun: We elected a delegate to the national committee']]
DLU = [["[ˈdɛləˌget]", 'فعل: آپ کو اپنی ذمہ داریاں سونپنی ہوں گی (delegate)'], ["[ˈdɛləgət]", 'اسم: ہم نے قومی کمیٹی کے لیے ایک نمائندہ (delegate) منتخب کیا']]
DLP = [["[ˈdɛləˌget]", 'فعل: تاسو باید خپل مسؤلیتونه وسپارئ (delegate)'], ["[ˈdɛləgət]", 'نوم: موږ ملي کمیټې ته یو استازی (delegate) وټاکه']]
w.table('eng12-u05-delegate', ['IPA', 'Use'], DL, ['IPA', 'استعمال'], ['IPA', 'کارونه'], DLU, DLP)
w.h('Activity', 'سرگرمی', 'فعالیت')
w.p('Consult Dictionary and mark which syllable is to stress in the following words.', 'لغت سے رجوع کریں اور نشان لگائیں کہ درج ذیل الفاظ میں کس ہجے پر زور ہے۔', 'قاموس ته مراجعه وکړئ او په نښه کړئ چې په لاندې کلمو کې پر کوم سیلاب فشار دی.')
ST = [['1', 'beautiful', '1st / 2nd / 3rd'], ['2', 'between', '1st / 2nd'], ['3', 'management', '1st / 2nd / 3rd'], ['4', 'campaign', '1st / 2nd'], ['5', 'financial', '1st / 2nd / 3rd'],
      ['6', 'candidate', '1st / 2nd / 3rd'], ['7', 'certainly', '1st / 2nd / 3rd'], ['8', 'material', '1st / 2nd / 3rd / 4th'], ['9', 'newspaper', '1st / 2nd / 3rd'], ['10', 'character', '1st / 2nd / 3rd']]
w.table('eng12-u05-stress-activity', ['No.', 'Word', 'Syllable options'], ST, ['نمبر', 'لفظ', 'ہجے کے اختیارات'], ['شمېره', 'کلمه', 'د سیلاب اختیارونه'], ST, ST)
w.p('C. Root words are words from which many other words are formed. Root words can be used with a combination of roots and affixes.', 'C. مادّہ الفاظ وہ الفاظ ہیں جن سے بہت سے دوسرے الفاظ بنتے ہیں۔ مادّہ الفاظ کو مادوں اور زوائد کے امتزاج کے ساتھ استعمال کیا جا سکتا ہے۔', 'C. رېښه‌ییزې کلمې هغه کلمې دي چې ډېرې نورې کلمې ترې جوړېږي. رېښه‌ییزې کلمې د رېښو او زوایدو له ترکیب سره کارول کېدای شي.')
w.h('Example:', 'مثال:', 'بېلګه:')
w.p('Word: preview — Root Word: view — Prefix: pre-; removable — Root Word: move — Prefix: re- — Suffix: -able', 'لفظ: preview — مادّہ: view — سابقہ: pre-؛ removable — مادّہ: move — سابقہ: re- — لاحقہ: -able', 'کلمه: preview — رېښه: view — مختاړی: pre-؛ removable — رېښه: move — مختاړی: re- — وروستاړی: -able')
rec = BOOK.record(w, 'eng12-u05-vocab-a', 'Vocabulary and Grammar — A, B (syllable stress), C (root words, start)', 'ذخیرۂ الفاظ اور قواعد — A، B (ہجائی زور)، C (مادّہ الفاظ، آغاز)', 'لغات او ګرامر — A، B (د سیلاب فشار)، C (رېښه‌ییزې کلمې، پیل)', 31, [49, 50])
issues = [{'id': 'eng12-p49-50', 'unit': 5, 'printedPage': 50, 'description': 'Printed transcriptions kept with their American vowels ([ˈfotəˌgræf], [pəˈteto]); the example line prints “Prefix: pre-removable” run together (preview / removable). Activity prints “which syllable is to stress”.'}]

if __name__ == '__main__':
    BOOK.save(31, [(5, rec)], issues=issues)
