"""PDF92 (printed 171–172): Unit 17 vocab A 2–6; word-form cloze; B Direct-Indirect speech (introduction, person of pronouns, pronoun tables)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
v = Builder()
MC = [('2. That he is very ........ should be evident from the number of friends he has.', 'a) sociable   b) social   c) societal   d) society'),
      ('3. The gangsters made a ........ attack on the hapless refugees.', 'a) timid   b) bold   c) valiant   d) cowardly'),
      ('4. People from villages are migrating to ........ areas.', 'a) urban   b) urbane   c) rural   d) rustic'),
      ('5. This drug is not to be taken ........', 'a) verbally   b) physically   c) orally   d) generally'),
      ('6. The terrorists could not ........ the army advance.', 'a) withstand   b) withheld   c) withdraw')]
for q, o in MC:
    v.p(q, q, q); v.paras[-1]['untranslatedByDesign'] = True
    v.p(o, o, o); v.paras[-1]['untranslatedByDesign'] = True
v.p('Fill in the blanks with the correct form of the words in brackets.', 'قوسین میں دیے گئے الفاظ کی درست شکل سے خالی جگہیں پُر کریں۔', 'تش ځایونه په قوسونو کې د کلمو په سمه بڼه ډک کړئ.')
c = 'It has been ____ (observation) that drivers have become more careless and rash these days. The traffic police committee has ____ (decision) to take this disregard for traffic rules very seriously. CCTV cameras will be monitored at all times, and the traffic offenders will be ____ (catch) immediately by the police at the next junction. It has ____ (be) decided to ____ (penalty) the first instance of law break with a fine and the second with the ____ (cancel) of the driving license.'
v.p(c, c, c); v.paras[-1]['untranslatedByDesign'] = True
v.h('B. Direct-Indirect speech.', 'B. براہِ راست اور بالواسطہ کلام', 'B. مستقیمه او غیرمستقیمه وینا')
v.p('Look at the following two sentences:', 'درج ذیل دو جملوں کو دیکھیں:', 'لاندې دوو جملو ته وګورئ:')
v.group('list', [('John said, “I am unwell now”. - Sentence [1].', 'John said, “I am unwell now”. - جملہ [1]۔', 'John said, “I am unwell now”. - جمله [1].'),
                 ('John said that he was unwell then. - Sentence [2].', 'John said that he was unwell then. - جملہ [2]۔', 'John said that he was unwell then. - جمله [2].')])
for x in [
    ('Sentence [1] is said to be in Direct speech and sentence [2] in Indirect speech. We can see that there is no change in meaning, but there is a change in form.', 'جملہ [1] براہِ راست کلام میں اور جملہ [2] بالواسطہ کلام میں کہلاتا ہے۔ ہم دیکھ سکتے ہیں کہ مطلب میں کوئی تبدیلی نہیں، لیکن شکل میں تبدیلی ہے۔', 'جمله [1] په مستقیمه وینا او جمله [2] په غیرمستقیمه وینا کې بلل کېږي. لیدلی شو چې په مانا کې بدلون نشته، خو په بڼه کې بدلون شته.'),
    ('First, the inverted commas have been removed.', 'اول، واوین (inverted commas) ہٹا دیے گئے ہیں۔', 'لومړی، اقتباس نښې (inverted commas) لرې شوې دي.'),
    ("Second, the pronoun `I' in sentence [1] has been changed from I st person to 3 rd person.", "دوم، جملہ [1] میں ضمیر `I' کو متکلم (پہلے شخص) سے غائب (تیسرے شخص) میں بدل دیا گیا ہے۔", "دویم، په جمله [1] کې ضمیر `I' له لومړي شخص څخه درېیم شخص ته بدل شوی."),
    ("Third, the auxiliary verb `am` which is in the simple present tense, in sentence [1] has been changed to `was` which is in the simple past tense.", 'سوم، جملہ [1] میں امدادی فعل `am` جو سادہ حال میں ہے، `was` میں بدل دیا گیا ہے جو سادہ ماضی میں ہے۔', 'درېیم، په جمله [1] کې مرستندوی فعل `am` چې په ساده حال کې دی، `was` ته بدل شوی چې په ساده تېر کې دی.'),
    ("Fourth, the adverb `now` has been changed to `then`, i.e.; a word showing closeness in time is changed to a word showing distance.", 'چہارم، متعلق فعل `now` کو `then` میں بدل دیا گیا ہے، یعنی وقت میں قربت ظاہر کرنے والا لفظ دوری ظاہر کرنے والے لفظ میں بدل گیا ہے۔', 'څلورم، قید `now` په `then` بدل شوی، یعنې هغه کلمه چې په وخت کې نږدېوالی ښيي په هغې کلمې بدله شوې چې لرېوالی ښيي.'),
    ("The word `that` has been added after the reporting verb `said`.", 'لفظ `that` کو بیانیہ فعل `said` کے بعد شامل کیا گیا ہے۔', 'کلمه `that` د راپور ورکوونکي فعل `said` وروسته زیاته شوې.'),
    ('So, we change the person of the pronoun and the tense of the verb and the adverb when we change from Direct to Indirect.', 'چنانچہ جب ہم براہِ راست سے بالواسطہ میں بدلتے ہیں تو ضمیر کا شخص، فعل کا زمانہ اور متعلق فعل بدلتے ہیں۔', 'نو کله چې له مستقیمې څخه غیرمستقیمې ته بدلوو، د ضمیر شخص، د فعل زمان او قید بدلوو.'),
]: v.p(*x)
a = BOOK.record(v, 'eng12-u17-vocab-b', 'Vocabulary A (2–6), word-form cloze; B Direct–Indirect speech (1)', 'ذخیرۂ الفاظ A (2–6)، الفاظ کی شکل؛ B براہِ راست/بالواسطہ کلام (1)', 'لغات A (2–6)، د کلمو بڼه؛ B مستقیمه/غیرمستقیمه وینا (1)', 92, [171])

w = Builder()
w.h('What do we mean by “Person” of a pronoun?', 'ضمیر کے ’’شخص‘‘ سے ہماری کیا مراد ہے؟', 'د ضمیر له "شخص" څخه زموږ مطلب څه دی؟')
w.p('We know that there are three person[s] where a pronoun is concerned. They are the 1st person, the 2nd person and the 3rd person.', 'ہم جانتے ہیں کہ ضمیر کے لحاظ سے تین شخص ہیں۔ یہ پہلا شخص (متکلم)، دوسرا شخص (حاضر) اور تیسرا شخص (غائب) ہیں۔', 'پوهېږو چې د ضمیر په اړه درې شخصونه دي. هغه لومړی شخص (متکلم)، دویم شخص (مخاطب) او درېیم شخص (غایب) دي.')
w.group('list', [("The definition of the 1st person is `Person speaking`.", 'پہلے شخص کی تعریف ہے ’’بولنے والا شخص‘‘۔', 'د لومړي شخص تعریف دی "ویونکی شخص".'),
                 ("The definition of 2nd person is `Person spoken to`.", 'دوسرے شخص کی تعریف ہے ’’جس سے بات کی جائے‘‘۔', 'د دویم شخص تعریف دی "هغه چې ورسره خبرې کېږي".'),
                 ("The definition of 3rd person is `Person spoken of/ about`.", 'تیسرے شخص کی تعریف ہے ’’جس کے بارے میں بات کی جائے‘‘۔', 'د درېیم شخص تعریف دی "هغه چې د هغه په اړه خبرې کېږي".')])
w.h('Why can’t we have a 4th Person?', 'چوتھا شخص کیوں نہیں ہو سکتا؟', 'څلورم شخص ولې نه شو درلودلی؟')
for x in [
    ("It is because in a conversation there can only be a `person speaking`, `a person spoken to' or a `person spoken of`. There cannot be a fourth `person`.", 'اس لیے کہ گفتگو میں صرف ’’بولنے والا شخص‘‘، ’’جس سے بات کی جائے‘‘ یا ’’جس کے بارے میں بات کی جائے‘‘ ہی ہو سکتا ہے۔ چوتھا ’’شخص‘‘ نہیں ہو سکتا۔', 'ځکه چې په خبرو اترو کې یوازې "ویونکی شخص"، "هغه چې ورسره خبرې کېږي" یا "هغه چې د هغه په اړه خبرې کېږي" کېدای شي. څلورم "شخص" نه شي کېدای.'),
    ("Let us suppose that there are two people `A` and `B`. If A says to B “I want to go there”, he is the `person speaking` and he refers to himself as `I', so `I' is the first person.", "فرض کریں دو لوگ `A` اور `B` ہیں۔ اگر A، B سے کہے “I want to go there” تو وہ ’’بولنے والا شخص‘‘ ہے اور اپنے آپ کو `I' کہتا ہے، اس لیے `I' پہلا شخص ہے۔", "فرض کړئ دوه کسان `A` او `B` دي. که A، B ته ووايي “I want to go there”، هغه \"ویونکی شخص\" دی او ځان ته `I' وايي، نو `I' لومړی شخص دی."),
    ("Suppose he asks B “Do you want to come?”, B is the `person spoken to` and he is being addressed as `you`, so `you` is the second person.", 'فرض کریں وہ B سے پوچھے “Do you want to come?” تو B ’’جس سے بات کی جائے‘‘ ہے اور اسے `you` کہہ کر مخاطب کیا جا رہا ہے، اس لیے `you` دوسرا شخص ہے۔', 'فرض کړئ هغه له B وپوښتي “Do you want to come?”، B "هغه چې ورسره خبرې کېږي" دی او د `you` په نوم مخاطب کېږي، نو `you` دویم شخص دی.'),
    ("Suppose `A` leaves and `C` comes along and B tells C what A told him, saying, `He wanted to go there`. `A` is the `person spoken of` and so `He` is the third person.", 'فرض کریں `A` چلا جائے اور `C` آ جائے اور B، C کو بتائے کہ A نے اس سے کیا کہا، یوں کہتے ہوئے `He wanted to go there`۔ `A` ’’جس کے بارے میں بات کی جائے‘‘ ہے اس لیے `He` تیسرا شخص ہے۔', 'فرض کړئ `A` لاړ شي او `C` راشي او B، C ته ووايي چې A ورته څه ویلي وو، داسې: `He wanted to go there`. `A` "هغه چې د هغه په اړه خبرې کېږي" دی نو `He` درېیم شخص دی.'),
]: w.p(*x)
H = {'en': ['Person', 'Singular', 'Plural'], 'ur': ['شخص', 'واحد', 'جمع'], 'ps': ['شخص', 'مفرد', 'جمع']}
R1 = [['1st', 'I', 'We'], ['2nd', 'You', 'You'], ['3rd', 'He, She, It', 'They.']]
w.table('eng12-u17-person-1', H['en'], R1, H['ur'], H['ps'])
w.p('We will list the remaining pronouns according to their person:', 'ہم باقی ضمائر کو ان کے شخص کے مطابق درج کریں گے:', 'پاتې ضمیرونه به د هغوی د شخص له مخې لیست کړو:')
R2 = [['1st', 'me', 'us', ''], ['2nd', 'you', 'you', ''], ['3rd', 'him, her,', 'them', 'it.']]
w.table('eng12-u17-person-2', H['en'] + ['Accusative case'], R2, H['ur'] + ['حالتِ مفعولی'], H['ps'] + ['مفعولي حالت'])
R3 = [['1st', 'my, mine', 'our, ours', ''], ['2nd', 'your, yours', 'your, yours', 'their, theirs'], ['3rd', 'his, his, her, hers', 'Its, its', '']]
w.table('eng12-u17-person-3', H['en'] + ['Possessive case [nominative and accusative]'], R3, H['ur'] + ['حالتِ اضافی [فاعلی اور مفعولی]'], H['ps'] + ['ملکي حالت [فاعلي او مفعولي]'])
b = BOOK.record(w, 'eng12-u17-vocab-c', 'B Direct–Indirect speech (2): person of pronouns', 'B براہِ راست/بالواسطہ کلام (2): ضمائر کا شخص', 'B مستقیمه/غیرمستقیمه وینا (2): د ضمیرونو شخص', 92, [172])
issues = [{'id': 'eng12-p171-172', 'unit': 17, 'printedPage': 172, 'description': 'Pronoun tables retained exactly as printed, including misplaced cells: “it.” under Accusative case; “their, theirs” in the 2nd-person row under Possessive case; 3rd-person plural possessive printed as “Its, its”; “his, his, her, hers”. Item 6 of A has only three options. Printed “I st person to 3 rd person”, “i.e.;” retained.'}]

if __name__ == '__main__':
    BOOK.save(92, [(17, a), (17, b)], issues=issues)
