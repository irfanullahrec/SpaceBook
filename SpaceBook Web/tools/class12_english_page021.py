"""PDF21 (printed 29–30): Reading Comprehension Q3–8; Writing Suggestions — poetic language and analysis chart; Activity; Oral Communication; Vocabulary A (animals/character phonetic table)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
w = Builder()
w.group('lines', [
    ('3. What are the poet\'s feelings about the song as expressed in the second stanza of the poem "The Solitary Reaper"?', '3. نظم ’’تنہا فصل کاٹنے والی‘‘ کے دوسرے بند میں گیت کے بارے میں شاعر کے کیا جذبات ظاہر ہوئے ہیں؟', '3. د "یوازینۍ لوګړه" شعر په دویم بند کې د سندرې په اړه د شاعر احساسات څه دي؟'),
    ('4. Describe in your own words the visual images depicted in the first stanza of the poem "The Solitary Reaper".', '4. نظم ’’تنہا فصل کاٹنے والی‘‘ کے پہلے بند میں دکھائی گئی بصری تصویروں کو اپنے الفاظ میں بیان کریں۔', '4. د "یوازینۍ لوګړه" شعر په لومړي بند کې انځور شوي لیدنیز انځورونه په خپلو ټکو کې بیان کړئ.'),
    ('5. Give the examples of alliteration from " The Solitary Reaper."', '5. ’’تنہا فصل کاٹنے والی‘‘ سے صنعتِ تکرارِ حرفی (alliteration) کی مثالیں دیں۔', '5. له "یوازینۍ لوګړه" څخه د تورو د تکرار (alliteration) بېلګې راوړئ.'),
    ('6. As you read the third stanza of "The Solitary Reaper" what pictures of the situation do you make in your mind?', '6. ’’تنہا فصل کاٹنے والی‘‘ کا تیسرا بند پڑھتے ہوئے آپ اپنے ذہن میں صورتِ حال کی کیا تصویریں بناتے ہیں؟', '6. کله چې د "یوازینۍ لوګړه" درېیم بند لولئ، په ذهن کې د حالت څه انځورونه جوړوئ؟'),
    ('7. Explain the last stanza of the poem "The Solitary Reaper" in your own words.', '7. نظم ’’تنہا فصل کاٹنے والی‘‘ کے آخری بند کی اپنے الفاظ میں وضاحت کریں۔', '7. د "یوازینۍ لوګړه" شعر وروستی بند په خپلو ټکو کې تشریح کړئ.'),
    ('8. What is the dominant theme of the poem The Solitary Reaper"?', '8. نظم ’’تنہا فصل کاٹنے والی‘‘ کا غالب موضوع کیا ہے؟', '8. د "یوازینۍ لوګړه" شعر غالبه موضوع څه ده؟'),
])
w.h('Writing Suggestions', 'تحریری تجاویز', 'د لیکلو وړاندیزونه')
w.h('Understanding the poem and its language', 'نظم اور اس کی زبان کو سمجھنا', 'شعر او د هغې ژبه پوهېدل')
for x in [
    ('Poetic language (also called poetic devices) are the tools of sound or meaning that a poet can use to make the poem more surprising, vivid, complex, or interesting. Examples of these tools include alliteration, onomatopoeia, imagery, metaphors similes, and allusion.', 'شاعرانہ زبان (جسے شاعرانہ صنائع بھی کہتے ہیں) آواز یا معنی کے وہ اوزار ہیں جنہیں شاعر نظم کو زیادہ حیران کن، واضح، پیچیدہ یا دلچسپ بنانے کے لیے استعمال کر سکتا ہے۔ ان اوزاروں کی مثالیں تکرارِ حرفی، صوتی لفظ (اونوماٹوپیا)، پیکر تراشی، استعارے، تشبیہات اور تلمیح ہیں۔', 'شاعرانه ژبه (چې شاعرانه صنعتونه هم بلل کېږي) د غږ یا مانا هغه وسایل دي چې شاعر یې د شعر د ډېر حیرانوونکي، ژوندي، پېچلي یا زړه‌راښکونکي کولو لپاره کارولی شي. د دې وسایلو بېلګې د تورو تکرار، غږپېښه کلمه (اونوماټوپیا)، انځورګري، استعارې، تشبیهات او تلمیح دي.'),
    ("Poets don't include poetic language because they want to make their poem sound complicated or hard to understand. Instead, they use these tools to help you wake up, pay attention, and look at the world in new ways.", 'شاعر شاعرانہ زبان اس لیے شامل نہیں کرتے کہ وہ اپنی نظم کو پیچیدہ یا مشکل بنانا چاہتے ہیں۔ بلکہ وہ یہ اوزار اس لیے استعمال کرتے ہیں کہ آپ بیدار ہوں، توجہ دیں اور دنیا کو نئے انداز سے دیکھیں۔', 'شاعران شاعرانه ژبه له دې امله نه کاروي چې غواړي خپل شعر پېچلی یا د پوهېدو لپاره سخت کړي. بلکې دا وسایل کاروي ترڅو تاسو ویښ شئ، پام وکړئ او نړۍ ته په نویو لارو وګورئ.'),
    ('Use the following chart to record your statement of the meaning of the poem and your observations about the technique of the poem. Each column in the chart deals with one poetic techniques.', 'نظم کے معنی کے بارے میں اپنا بیان اور نظم کی تکنیک کے بارے میں اپنے مشاہدات درج کرنے کے لیے درج ذیل چارٹ استعمال کریں۔ چارٹ کا ہر کالم ایک شاعرانہ تکنیک سے متعلق ہے۔', 'د شعر د مانا په اړه د خپل بیان او د شعر د تخنیک په اړه د خپلو لیدنو د ثبتولو لپاره لاندې چارټ وکاروئ. د چارټ هر ستون له یوه شاعرانه تخنیک سره تړاو لري.'),
]: w.p(*x)
EN = [['Stanza:', 'Human:', 'Rhyme:', 'Sight (Visual):', 'Similes:'], ['Couplets', 'The Poet', '', '', ''], ['Tercets', 'Man/Woman', 'Rhythm:', 'Hearing (Aural):', ''],
      ['Quatrains', 'Mother/Father', '', '', ''], ['Quintets', 'Young/Old', 'Alliteration:', 'Smell (olfactory):', 'Implied metaphors:'], ['Sestets', 'Boy/Girl', '', '', ''],
      ['Octave', 'Son/Doughter', 'Consonance:', 'Taste: (Gustatory)', 'Other Devices:'], ['Strophes:', 'Nnon-human:', '', '', ''], ['', 'Animal', 'Assonance:', 'Touch (Tactile):', ''],
      ['', 'Wild', '', '', ''], ['', 'Domestic', 'Onomatopoeia:', '', ''], ['', 'Plants', '', '', '']]
UR = [['بند:', 'انسانی:', 'قافیہ:', 'بصری:', 'تشبیہات:'], ['دو مصرعی (Couplets)', 'شاعر', '', '', ''], ['سہ مصرعی (Tercets)', 'مرد/عورت', 'آہنگ:', 'سماعی:', ''],
      ['چہار مصرعی (Quatrains)', 'ماں/باپ', '', '', ''], ['پنج مصرعی (Quintets)', 'جوان/بوڑھا', 'تکرارِ حرفی:', 'شامّہ (سونگھنا):', 'ضمنی استعارے:'], ['شش مصرعی (Sestets)', 'لڑکا/لڑکی', '', '', ''],
      ['ہشت مصرعی (Octave)', 'بیٹا/بیٹی', 'تکرارِ مصمتہ:', 'ذائقہ:', 'دیگر صنائع:'], ['بند (Strophes):', 'غیر انسانی:', '', '', ''], ['', 'جانور', 'تکرارِ مصوتہ:', 'لمس:', ''],
      ['', 'جنگلی', '', '', ''], ['', 'پالتو', 'صوتی لفظ:', '', ''], ['', 'پودے', '', '', '']]
PS = [['بند:', 'انساني:', 'قافیه:', 'لیدنیز:', 'تشبیهات:'], ['دوه‌بیتي (Couplets)', 'شاعر', '', '', ''], ['درې‌مسرعي (Tercets)', 'نر/ښځه', 'اهنګ:', 'اورېدنیز:', ''],
      ['څلورمسرعي (Quatrains)', 'مور/پلار', '', '', ''], ['پنځه‌مسرعي (Quintets)', 'ځوان/زوړ', 'د تورو تکرار:', 'بویول:', 'ضمني استعارې:'], ['شپږمسرعي (Sestets)', 'هلک/نجلۍ', '', '', ''],
      ['اته‌مسرعي (Octave)', 'زوی/لور', 'د بې‌غږو تکرار:', 'خوند:', 'نور صنعتونه:'], ['بندونه (Strophes):', 'غیرانساني:', '', '', ''], ['', 'حیوان', 'د غږلرونکو تکرار:', 'لمس:', ''],
      ['', 'ځنګلي', '', '', ''], ['', 'کورني', 'غږپېښه کلمه:', '', ''], ['', 'بوټي', '', '', '']]
w.table('eng12-u03-poetic-chart', ['Stanza type', 'Speaker', 'Sound', 'Imagery', 'Figurative language'], EN, ['بند کی قسم', 'متکلم', 'آواز', 'پیکر تراشی', 'مجازی زبان'], ['د بند ډول', 'ویونکی', 'غږ', 'انځورګري', 'مجازي ژبه'], UR, PS)
w.h('Activity', 'سرگرمی', 'فعالیت')
w.p("Keeping in view the above chart, write a paragraph on the poet use of language in the poem 'The Solitary Reaper' by highlighting various techniques used by the poet.", 'مندرجہ بالا چارٹ کو مدِ نظر رکھتے ہوئے شاعر کی استعمال کردہ مختلف تکنیکوں کو اجاگر کر کے نظم ’’تنہا فصل کاٹنے والی‘‘ میں شاعر کے زبان کے استعمال پر ایک پیراگراف لکھیں۔', 'پورتنی چارټ په پام کې ونیسئ او د شاعر د کارول شویو بېلابېلو تخنیکونو په روښانه کولو د "یوازینۍ لوګړه" په شعر کې د شاعر د ژبې د کارونې په اړه یو پراګراف ولیکئ.')
w.h('Oral Communication', 'زبانی ابلاغ', 'د خولې اړیکه')
w.p('Divide the class into two groups. One group may be asked to speak in favour of the rural life and the other to speak in favour of the urban life.', 'جماعت کو دو گروہوں میں تقسیم کریں۔ ایک گروہ سے دیہی زندگی کے حق میں اور دوسرے سے شہری زندگی کے حق میں بولنے کو کہا جائے۔', 'ټولګی په دوو ډلو ووېشئ. له یوې ډلې وغوښتل شي چې د کلیوالي ژوند په ګټه او له بلې چې د ښاري ژوند په ګټه خبرې وکړي.')
w.h('Vocabulary and Grammar', 'ذخیرۂ الفاظ اور قواعد', 'لغات او ګرامر')
w.p('A. How are the following phonetic transcription of the words spelled correctly? Write down in the given blanks.', 'A. درج ذیل الفاظ کی صوتی نقل کے درست ہجے کیا ہیں؟ دی گئی خالی جگہوں میں لکھیں۔', 'A. د لاندې کلمو غږیز لیکدود په سمه توګه څنګه لیکل کېږي؟ په ورکړل شویو تشو ځایونو کې یې ولیکئ.')
AN = ["/'taɪgə/", "/'ræbɪ/", "/'hæmstə/", "/'bi:tl/", '/gu:s/', '/kaʊ/', "/'mʌŋki/", '/maʊs/', '/ʃi:p/', "/'spaɪdə/"]
CH = ["/'sɪərɪəs/", "/'keəfʊl/", "/ kən'fju:zd/", "/'dʒenərəs/", "/ dɪ'tɜ:mɪnd/", '/streɪndʒ/', '/breɪv/', "/'dʒentl/", "/'ɒnɪst/", "/'kjʊərɪəs/"]
R = [[a, '', b, ''] for a, b in zip(AN, CH)]
w.table('eng12-u03-ipa', ['Animals — Phonetic Transcription', 'Spelling', 'Character — Phonetic Transcription', 'Spelling'], R,
        ['جانور — صوتی نقل', 'ہجے', 'کردار — صوتی نقل', 'ہجے'], ['حیوانات — غږیز لیکدود', 'املا', 'شخصیت — غږیز لیکدود', 'املا'], R, R)
rec = BOOK.record(w, 'eng12-u03-exercises-a', 'Comprehension Q3–8; poetic language chart; Oral Communication; Vocabulary A', 'فہم سوالات 3–8؛ شاعرانہ زبان کا چارٹ؛ زبانی ابلاغ؛ ذخیرۂ الفاظ A', 'د پوهې پوښتنې 3–8؛ د شاعرانه ژبې چارټ؛ د خولې اړیکه؛ لغات A', 21, [29, 30])
issues = [{'id': 'eng12-p29-30-typos', 'unit': 3, 'printedPage': 30, 'description': 'Printed text retained: chart “Son/Doughter”, “Nnon-human:”, “one poetic techniques”, activity “the poet use of language”, Q8 unbalanced quotation mark, “/ˈræbɪ/” (rabbit, printed without final t).'}]

if __name__ == '__main__':
    BOOK.save(21, [(3, rec)], issues=issues)
