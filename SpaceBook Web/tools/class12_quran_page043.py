"""Mutalia-e-Quran XII PDF43: p.40 — verses 4:133–134; Lesson 4 knowledge and action; vocabulary (part 1). Run: python class12_quran_page043.py"""
from class12_quran_common import BOOK, Builder, rec, V, KA, L

VOCAB = [
    ('جُنَاحٌ', 'Sin, harm', 'گناہ، حرج', 'ګناه، حرج'),
    ('يَفْتِنَكُمُ', 'He will cause you trouble', 'وہ تمھیں تکلیف پہنچائے گا', 'تاسو ته به ځور درکړي'),
    ('قُعُودًا', 'Sitting', 'بیٹھے ہوئے', 'ناست'),
    ('لَا تَهِنُوا', 'Do not show weakness', 'تم کمزوری نہ دکھاؤ', 'کمزوري مه ښیئ'),
    ('جَادَلْتُمْ', 'You argued', 'تم نے بحث کی', 'تاسو بحث وکړ'),
    ('مَنْ يُشَاقِقِ', 'Whoever opposes', 'جو مخالفت کرے', 'څوک چې مخالفت وکړي'),
    ('نُوَلِّهِ', 'We will turn him', 'ہم اسے پھیر دیں گے', 'موږ به یې واړوو'),
    ('تَقْصُرُوا', 'You shorten (the prayer)', 'تم قصر کرو', 'لنډ یې کړئ'),
    ('فَإِذَا قَضَيْتُمُ', 'Then when you have performed', 'پھر جب تم ادا کر چکو', 'بیا چې مو ادا کړ'),
    ('مَوْقُوتًا', 'At a fixed time', 'مقررہ وقت', 'ټاکلی وخت'),
    ('خَصِيمًا', 'An advocate, a partisan', 'طرف دار', 'پلوی'),
    ('مِنْ نَجْوَاهُمْ', 'Of their secret talks', 'ان کی سرگوشیوں سے', 'له هغوی پټو خبرو'),
    ('يَتَّبِعْ', 'He follows', 'وہ پیروی کرتا ہے', 'هغه پیروي کوي'),
    ('نُصْلِهِ', 'We will scorch him', 'ہم اسے جھلسا دیں گے', 'موږ به یې وسوځوو'),
]


def p43():
    b = Builder()
    V(b, 4, 133, '(لوگو!) اگر وہ چاہے تو تمھیں لے جائے اور دوسروں کو لے آئے اور اللہ ایسا کرنے پر خوب قدرت رکھنے والا ہے۔',
      '(ای خلکو!) که هغه وغواړي، تاسو به یوسي او نور به راولي؛ او الله پر داسې کولو ښه قدرت لري.')
    V(b, 4, 134, 'جو کوئی (فقط) دنیا کے بدلے کا طلب گار ہے تو اللہ کے پاس تو دنیا و آخرت دونوں کا بدلہ ہے اور اللہ خوب سننے والا، خوب دیکھنے والا ہے۔',
      'څوک چې (یوازې) د دنیا د بدلې غوښتونکی وي، نو له الله سره خو د دنیا او آخرت دواړو بدله ده؛ او الله ښه اورېدونکی، ښه لیدونکی دی.')
    KA(b)
    L(b, [('In the state of travel Allah Almighty has commanded that the four-rak\'ah obligatory prayers of Zuhr, \'Asr and \'Isha\' be offered as half. This is called qasr. (There is no qasr in the Maghrib and Fajr prayers; they must be offered in full even on a journey.)', 'اللہ تعالیٰ نے سفر کی حالت میں نماز ظہر، عصر اور عشاء کی چار رکعت والی فرض نماز آدھی ادا کرنے کا حکم دیا ہے۔ اسے قصر کہا جاتا ہے۔ (نماز مغرب اور نماز فجر میں قصر نہیں ہے ان کو سفر میں بھی پورا ہی ادا کرنا فرض ہے)۔', 'الله تعالی د سفر په حال کې د ماسپښین، مازدیګر او ماسخوتن د څلور رکعته فرض لمونځ نیمایي ادا کولو حکم کړی؛ دې ته قصر ویل کېږي. (په ماښام او سهار لمانځه کې قصر نشته؛ هغه په سفر کې هم بشپړ ادا کول فرض دي.)'),
          ('If Muslims fear or apprehend anything from the enemy, then permission has been given for the prayer of fear (salat al-khawf) so that they may remain alert and cautious, so that the enemies may not get any opportunity for mischief. From this the importance and greatness of prayer and the concession given in the commands of the Shari\'ah can be estimated.', 'مسلمانوں کو اگر دشمن کی طرف سے کوئی خوف یا خدشہ ہو تو ان سے ہوشیار اور محتاط رہنے کے لیے صلوٰۃِ خوف کی اجازت دی گئی ہے تاکہ دشمنوں کو کسی شر انگیزی کا موقع نہ مل سکے۔ اس بات سے نماز کی اہمیت و عظمت اور احکامِ شریعت میں دی گئی رعایت کا اندازہ ہوتا ہے۔', 'که مسلمانانو ته د دښمن له لوري کومه وېره یا اندېښنه وي، نو له هغوی د هوښیارتیا او احتیاط لپاره د وېرې د لمانځه اجازه ورکړل شوې، تر څو دښمنانو ته د کومې شرارت موقع ورنه کړل شي. له دې خبرې د لمانځه اهمیت او عظمت او د شریعت په حکمونو کې ورکړل شوې اسانتیا څرګندېږي.'),
          ('Allah Almighty has fixed the times of the obligatory prayers, which must be observed; also, after offering prayer at the fixed times, one should keep remembering Allah Almighty while walking, standing, sitting and lying down.', 'اللہ تعالیٰ نے فرض نمازوں کے اوقات مقرر فرمائے ہیں جن کا خیال رکھنا ضروری ہے نیز مقررہ اوقات میں نماز ادا کرنے کے بعد بھی چلتے پھرتے، اٹھتے بیٹھتے اور لیٹنے کی حالت میں اللہ تعالیٰ کا ذکر کرتے رہنا چاہیے۔', 'الله تعالی د فرضو لمونځونو وختونه ټاکلي چې پاملرنه یې اړینه ده؛ همدارنګه په ټاکلو وختونو کې له لمانځه وروسته هم باید په ګرځېدو، پاڅېدو، ناستې او پرېوتو کې د الله تعالی ذکر روان وساتل شي.'),
          ('Committing a sin oneself and putting its blame on some innocent person is a slander and a very great sin. People can be deceived by this slander and lie, and he will bear the burden of his sin and slander, but before Allah Almighty his deception will not work at all.', 'خود گناہ کر کے اس کا الزام کسی بے قصور پر لگانا بہتان اور بہت بڑا گناہ ہے۔ اس بہتان اور جھوٹ سے لوگوں کو دھوکہ دیا جا سکتا ہے اور وہ اپنے گناہ اور بہتان کا بوجھ اٹھائیں گے مگر اللہ تعالیٰ کے ہاں ان کی دھوکہ دہی نہیں چلے گی۔', 'پخپله ګناه کول او تور یې پر کوم بې‌ګناه لګول بهتان او ډېره لویه ګناه ده. په دې بهتان او درواغو خلک غولول کېدای شي او هغوی به د خپلې ګناه او بهتان بار پورته کوي، خو د الله تعالی په وړاندې به یې دوکه ونه چلېږي.'),
          ('Satan\'s whole business runs only on false promises and hopes. When he wants to take people towards some wrong path, he presents their bad deeds to them as beautiful.', 'شیطان کا سارا کاروبار ہی جھوٹے وعدوں اور امیدوں کے بل پر چلتا ہے۔ وہ لوگوں کو جب کسی غلط راستے کی طرف لے جانا چاہتا ہے تو ان کے بُرے اعمال کو خوش نما بنا کر پیش کرتا ہے۔', 'د شیطان ټول کار یوازې پر درواغجنو ژمنو او هیلو چلېږي؛ کله چې غواړي خلک کومې غلطې لارې ته بوځي، نو د هغوی بد عملونه ښکلي کړي او وړاندې یې کړي.')])
    b.h('Vocabulary', 'ذخیرۂ الفاظ', 'د کلمو زېرمه')
    b.table('mq12-l4-vocab-1', ['Word', 'Meaning'], [[w, e] for w, e, u, p in VOCAB], ['الفاظ', 'معانی'], ['کلمې', 'معناوې'],
            [[w, u] for w, e, u, p in VOCAB], [[w, p] for w, e, u, p in VOCAB])
    BOOK.save(43, [(4, rec(b, 4, 43, 43))], issues=[{'id': 'mq12-pdf043', 'unit': 4, 'printedPage': 40,
               'description': 'Verses of lesson 4 end at 4:134. The vocabulary table continues on p.41 (6 more words, recorded there). Ruku sign after verse 134 not reproduced.'}])


if __name__ == '__main__':
    p43()
