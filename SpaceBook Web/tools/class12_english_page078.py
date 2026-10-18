"""PDF78 (printed 143–144): Unit 15 Reading Comprehension Q1–6; Writing (paraphrase of stanzas 3–4); Oral; Vocabulary A context MCQs 1–8; B Future Continuous Tense (definition, form, examples)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
q = Builder()
q.h('Reading Comprehension', 'مطالعہ اور فہم', 'لوستل او پوهه')
q.group('lines', [
    ('1. Compare and contrast the behaviour of the people in the past and today, in the light of the poem "Once upon a time".', '1. نظم ’’ایک زمانے میں‘‘ کی روشنی میں ماضی اور آج کے لوگوں کے رویے کا موازنہ اور تقابل کریں۔', '1. د "یو وخت و" شعر په رڼا کې د پخوا او نن ورځې د خلکو چلند پرتله کړئ.'),
    ('2. What does the poet want to learn from his son?', '2. شاعر اپنے بیٹے سے کیا سیکھنا چاہتا ہے؟', '2. شاعر له خپل زوی څخه څه زده کول غواړي؟'),
    ('3. What do the expressions "laugh with their teeth" and " teeth like a snake\'s bare fangs" mean?', '3. اظہارات ’’دانتوں سے ہنسنا‘‘ اور ’’سانپ کے ننگے دانتوں جیسے دانت‘‘ کا کیا مطلب ہے؟', '3. د "په غاښونو خندل" او "د مار د لوڅو غاښونو په څېر غاښونه" څرګندونو مانا څه ده؟'),
    ('4. To what does the poet compare the eyes of the modern man in the poem," Once upon a time" and why?', '4. نظم ’’ایک زمانے میں‘‘ میں شاعر جدید انسان کی آنکھوں کو کس چیز سے تشبیہ دیتا ہے اور کیوں؟', '4. شاعر د "یو وخت و" په شعر کې د عصري انسان سترګې له څه سره تشبیه کوي او ولې؟'),
    ('5. Describe the tone of the poem "Once upon a time."', '5. نظم ’’ایک زمانے میں‘‘ کے لہجے کو بیان کریں۔', '5. د "یو وخت و" شعر لهجه بیان کړئ.'),
    ('6. Find out the similes and metaphors used by the poet in the first and fourth stanza of the poem.', '6. نظم کے پہلے اور چوتھے بند میں شاعر کی استعمال کردہ تشبیہات اور استعارات تلاش کریں۔', '6. د شعر په لومړي او څلورم بند کې د شاعر کارول شوې تشبیهات او استعارې ومومئ.'),
])
q.h('Writing Suggestions', 'تحریری تجاویز', 'د لیکلو وړاندیزونه')
q.p('Write the paraphrase of the following stanzas: stanza 3 (beginning ‘Feel at home!’ ‘Come again’) and stanza 4 (beginning “So I have learned many things, son.”) of the poem. [The two stanzas are quoted in full in the printed book, p. 143.]', 'درج ذیل بندوں کی نثری وضاحت لکھیں: نظم کا تیسرا بند (جو ’’اپنا گھر سمجھو! پھر آنا‘‘ سے شروع ہوتا ہے) اور چوتھا بند (جو ’’تو بیٹا، میں نے بہت سی چیزیں سیکھی ہیں‘‘ سے شروع ہوتا ہے)۔ [دونوں بند درسی کتاب کے صفحہ 143 پر مکمل درج ہیں۔]', 'د لاندې بندونو نثري تشریح ولیکئ: د شعر درېیم بند (چې په "ځان په کور کې وګڼه! بیا راشه" پیلېږي) او څلورم بند (چې په "نو زویه، ما ډېر شیان زده کړي" پیلېږي). [دواړه بندونه په چاپي کتاب کې په 143 مخ کې بشپړ راغلي.]')
q.h('Oral Communication', 'زبانی ابلاغ', 'د خولې اړیکه')
q.p('Conduct a group activity in the class, dividing the students into two equal groups. One group will present arguments in favour of the modern time while the other group will give arguments in favour of the past.', 'جماعت میں ایک گروہی سرگرمی کرائیں اور طلبہ کو دو برابر گروہوں میں تقسیم کریں۔ ایک گروہ جدید دور کے حق میں دلائل پیش کرے گا جبکہ دوسرا گروہ ماضی کے حق میں دلائل دے گا۔', 'په ټولګي کې یو ډله‌ییز فعالیت ترسره کړئ او زده کوونکي په دوو برابرو ډلو ووېشئ. یوه ډله به د عصري وخت په ګټه دلیلونه وړاندې کړي او بله به د پخوا په ګټه دلیلونه ورکړي.')
qs = BOOK.record(q, 'eng12-u15-comprehension', 'Reading Comprehension; Writing; Oral Communication', 'مطالعہ اور فہم؛ تحریر؛ زبانی ابلاغ', 'لوستل او پوهه؛ لیکنه؛ د خولې اړیکه', 78, [143])

v = Builder()
v.h('Vocabulary and Grammar', 'ذخیرۂ الفاظ اور قواعد', 'لغات او ګرامر')
v.p('A. Read the sentence and guess the meaning of the underlined word from its context.', 'A. جملہ پڑھیں اور سیاق سے خط کشیدہ لفظ کے معنی کا اندازہ لگائیں۔', 'A. جمله ولولئ او له شرایطو څخه د لاندې کرښه لرونکې کلمې مانا اټکل کړئ.')
MC = [('The child was rushed to the hospital after she had an adverse reaction to the medicine. [underlined: adverse]', ['a. healing', 'b. harmful', 'c. soothing', 'd. helpful']),
      ('The novice teacher was excited about her first teaching job since graduating college. [underlined: novice]', ['a. Experienced', 'b. Beginner', 'c. Knowledgeable', 'd. Stern']),
      ('The alluring aroma of the cookies drew Sandy toward the kitchen for a taste. [underlined: alluring]', ['a. Unpleasant', 'b. Unappetizing', 'c. Desirable', 'd. Obnoxious']),
      ('The man should go to jail for his inhumane treatment of his horses. [underlined: inhumane]', ['a. Loving', 'b. Caring', 'c. Proper', 'd. Cruel']),
      ('The greedy child was snatching candy from the shelf. [underlined: greedy]', ['a. Happy', 'b. Pleasant', 'c. Giving', 'd. Selfish']),
      ('You should not belittle his effort but thank him for trying. [underlined: belittle]', ['a. Make important', 'b. Make unimportant', 'c. Make inviting', 'd. Make appealing']),
      ('The sun suddenly vanished from view as the storm clouds rolled across the sky. [underlined: vanished]', ['a. Appeared', 'b. Danced', 'c. Disappeared', 'd. Floated']),
      ('The soldiers crouched down low behind their vehicle and waited for the enemy to pass. [underlined: crouched]', ['a. Stooped with bent knees', 'b. Stood straight and tall', 'c. Leaned against', 'd. Ran from'])]
for i, (s, opts) in enumerate(MC, 1):
    v.p(f'{i}. {s}', f'{i}. {s}', f'{i}. {s}'); v.paras[-1]['untranslatedByDesign'] = True
    o = '   '.join(opts)
    v.p(o, o, o); v.paras[-1]['untranslatedByDesign'] = True
v.h('B. Future Continuous Tense', 'B. مستقبل جاری', 'B. راتلونکی روان زمان')
v.p('Definition: The future continuous tense , also called as the future progressive tense, is a tense that shows that an action will take place in future and continue for a certain length of time.', 'تعریف: مستقبل جاری، جسے مستقبل استمراری بھی کہتے ہیں، وہ زمانہ ہے جو ظاہر کرتا ہے کہ کوئی کام مستقبل میں ہو گا اور کچھ وقت تک جاری رہے گا۔', 'تعریف: راتلونکی روان زمان، چې راتلونکی دوامداره زمان هم بلل کېږي، هغه زمان دی چې ښيي یو کار به په راتلونکي کې ترسره شي او د یوې ټاکلې مودې لپاره به دوام ولري.')
v.p('Form: It is formed using the structure will + be + the present participle (the root verb + ing). For example,', 'ساخت: یہ will + be + حال کا اسمِ فاعل (بنیادی فعل + ing) کی ساخت سے بنتا ہے۔ مثلاً،', 'جوړښت: دا د will + be + د اوسني زمان صفت فاعلي (رېښه‌ییز فعل + ing) له جوړښت سره جوړېږي. د بېلګې په توګه،')
v.group('list', [
    ("The plane will be leaving for Saudi Arabia at 3 o'clock.", 'جہاز 3 بجے سعودی عرب کے لیے روانہ ہو رہا ہو گا۔', 'الوتکه به په 3 بجو سعودي عربستان ته روانه وي.'),
    ('They will be playing a match in the evening.', 'وہ شام کو ایک میچ کھیل رہے ہوں گے۔', 'دوی به په ماښام کې یوه لوبه کوي.'),
    ('Our teacher will be e arriving the class in a short while.', 'ہمارے استاد تھوڑی دیر میں جماعت میں پہنچ رہے ہوں گے۔', 'زموږ ښوونکی به په لږ وخت کې ټولګي ته رارسېږي.'),
])
vg = BOOK.record(v, 'eng12-u15-vocab-a', 'Vocabulary A (context clues); B Future Continuous Tense (1)', 'ذخیرۂ الفاظ A (سیاقی اشارے)؛ B مستقبل جاری (1)', 'لغات A (شرایطي نښې)؛ B راتلونکی روان (1)', 78, [144])
issues = [{'id': 'eng12-p143-144', 'unit': 15, 'printedPage': 143, 'description': 'The writing task quotes stanzas 3–4 of the copyrighted poem in full; the app refers to the stanzas instead of reproducing them. Printed text retained: “also called as the future progressive tense”, example “will be e arriving the class”. Underlined target words are shown as “[underlined: …]”.'}]

if __name__ == '__main__':
    BOOK.save(78, [(15, qs), (15, vg)], issues=issues)
