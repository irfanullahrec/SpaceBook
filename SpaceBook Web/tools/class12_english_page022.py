"""PDF22 (printed 31–32): Unit 3 Vocabulary A (miscellaneous words), B verb forms 1–10 (unit end); Unit 4 opener 'Truck Art' (Rachel Redford) outcomes."""
from class12_book_common import Book, Builder

BOOK = Book('english')
w = Builder()
M1 = ['/ðæt/', "/'dɪfɪkəlt/", '/ju:/', '/wɪtʃ/', '/ðeər/', "/ə'baʊt/", "/'foʊtoʊ/", '/ʃʊd/', "/'pi:pəl/", "/'ɔ:lsoʊ/"]
M2 = ["/'ʌndər/", "/'prɒbləm/", "/'nevər/", "/'sɜ:rvɪs/", "/'sʌmθɪŋ/", '/pleɪs/', '/pɔɪnt/', "/prə'vaɪd/", '/lɑ:rdʒ/', "/'dʒenərəl/"]
R = [[a, '', b, ''] for a, b in zip(M1, M2)]
w.table('eng12-u03-ipa-misc', ['Miscellaneous words — Phonetic Transcription', 'Spelling', 'Miscellaneous words — Phonetic Transcription', 'Spelling'], R,
        ['متفرق الفاظ — صوتی نقل', 'ہجے', 'متفرق الفاظ — صوتی نقل', 'ہجے'], ['متفرقې کلمې — غږیز لیکدود', 'املا', 'متفرقې کلمې — غږیز لیکدود', 'املا'], R, R)
w.p('B. Use the correct form of the verbs given in brackets:', 'B. قوسین میں دیے گئے افعال کی درست شکل استعمال کریں:', 'B. په قوسونو کې د ورکړل شویو فعلونو سمه بڼه وکاروئ:')
B = '________'
w.group('lines', [
    (f'1. Your friends {B} for you for over an hour. (wait)', f'1. آپ کے دوست ایک گھنٹے سے زیادہ دیر سے آپ کا {B}۔ (wait — انتظار کرنا)', f'1. ستاسو ملګري له یو ساعت زیات ستاسو {B}. (wait — انتظار کول)'),
    (f'2. It is not worth {B} so much money for this concert (pay).', f'2. اس کنسرٹ کے لیے اتنی رقم {B} کے قابل نہیں (pay — ادا کرنا)۔', f'2. د دې کنسرټ لپاره دومره پیسې {B} نه ارزي (pay — ورکول).'),
    (f'3. When I reached the station, the train {B} (leave).', f'3. جب میں اسٹیشن پہنچا تو ٹرین {B} (leave — روانہ ہونا)۔', f'3. کله چې سټېشن ته ورسېدم، اورګاډی {B} (leave — تلل).'),
    (f'4. I {B} the Badshahi Mosque last month. (visit).', f'4. میں نے پچھلے مہینے بادشاہی مسجد {B}۔ (visit — دیکھنے جانا)', f'4. ما تېره میاشت بادشاهي جومات {B}. (visit — لیدنه کول)'),
    (f'5. The criminal {B} the victim with a blunt object. (attack).', f'5. مجرم نے کند چیز سے متاثرہ شخص پر {B}۔ (attack — حملہ کرنا)', f'5. مجرم پر قرباني د یوه پڅ شي سره {B}. (attack — برید کول)'),
    (f'6. His company is greatly {B} after. (seek)', f'6. اس کی صحبت کی بہت {B} جاتی ہے۔ (seek — تلاش کرنا)', f'6. د هغه ملګرتیا ډېره {B}. (seek — لټول)'),
    (f'7. His courage {B} him (forsake).', f'7. اس کی ہمت نے اس کا ساتھ {B} (forsake — چھوڑ دینا)۔', f'7. د هغه زړورتیا هغه {B} (forsake — پرېښودل).'),
    (f'8. The terrified people {B} to the mountains. (flee).', f'8. خوفزدہ لوگ پہاڑوں کی طرف {B}۔ (flee — بھاگنا)', f'8. وېرېدلي خلک غرونو ته {B}. (flee — تښتېدل)'),
    (f'9. The police {B} no stone unturned to trace the culprits. (leave)', f'9. پولیس نے مجرموں کا سراغ لگانے کے لیے کوئی کسر نہیں {B}۔ (leave — چھوڑنا)', f'9. پولیسو د مجرمانو د موندلو لپاره هېڅ هڅه پاتې {B}. (leave — پرېښودل)'),
    (f'10. The robber {B} him a blow on the head. (strike).', f'10. ڈاکو نے اس کے سر پر ایک ضرب {B}۔ (strike — مارنا)', f'10. غل د هغه پر سر یو ګوزار {B}. (strike — وهل)'),
])
ex = BOOK.record(w, 'eng12-u03-exercises-b', 'Vocabulary A (miscellaneous words); B verb forms', 'ذخیرۂ الفاظ A (متفرق الفاظ)؛ B افعال کی شکلیں', 'لغات A (متفرقې کلمې)؛ B د فعلونو بڼې', 22, [31])

UT = ('Truck Art', 'ٹرک آرٹ', 'د ټرک هنر')
o = Builder()
o.h('Unit 4 — Truck Art (Rachel Redford)', 'یونٹ 4 — ٹرک آرٹ (ریچل ریڈفورڈ)', 'واحد 4 — د ټرک هنر (ریچل ریډفورډ)')
o.p('By the end of the unit, the students will be able to:', 'اس یونٹ کے اختتام تک طلبہ اس قابل ہوں گے کہ:', 'د دې واحد په پای کې به زده کوونکي وکولای شي چې:')
o.group('list', [
    ('Use pre-reading strategies to predict the content of a text from topic / picture, title / headings, key words and visuals etc. by using prior knowledge, asking questions and contextual clues.', 'سابقہ علم، سوالات اور سیاقی اشاروں کو استعمال کرتے ہوئے موضوع / تصویر، عنوان / سرخیوں، کلیدی الفاظ اور بصری مواد وغیرہ سے متن کے مواد کی پیش گوئی کے لیے مطالعے سے پہلے کی حکمتِ عملیاں استعمال کریں۔', 'د مخکینۍ پوهې، پوښتنو او شرایطي نښو په کارولو د موضوع / انځور، سرلیک / سرټکو، کلیدي کلمو او لیدنیزو موادو څخه د متن د منځپانګې د وړاندوینې لپاره د لوستلو مخکې ستراتیژۍ وکاروي.'),
    ('Skim text to: have general idea of the text; infer theme/ main idea.', 'متن پر سرسری نظر ڈالیں تاکہ: متن کا عمومی اندازہ ہو؛ موضوع/ مرکزی خیال اخذ کریں۔', 'په متن سرسري نظر واچوي ترڅو: د متن عمومي مفکوره ولري؛ موضوع/ اصلي مفکوره استنباط کړي.'),
    ('Analyze passages in the text to identify the theme/ general subject, key idea/ central thought (a statement about the general subject), and supporting details.', 'متن کے اقتباسات کا تجزیہ کر کے موضوع/ عمومی مضمون، کلیدی خیال/ مرکزی سوچ (عمومی مضمون کے بارے میں ایک بیان) اور معاون تفصیلات کی نشاندہی کریں۔', 'د متن برخې تحلیل کړي ترڅو موضوع/ عمومي مضمون، کلیدي نظر/ مرکزي فکر (د عمومي مضمون په اړه یو بیان) او ملاتړي جزییات وپېژني.'),
    ('Recognize that the theme of a text is carried in a thesis statement.', 'پہچانیں کہ متن کا موضوع مرکزی دعوے (تھیسس اسٹیٹمنٹ) میں بیان ہوتا ہے۔', 'وپېژني چې د متن موضوع د تیسس په بیان کې راځي.'),
    ('Analyze paragraphs to identify sentences that support the main idea through definition; example/ illustration; cause and effect; comparison and contrast; facts, analogies, anecdotes and quotations.', 'پیراگرافوں کا تجزیہ کر کے ان جملوں کی نشاندہی کریں جو مرکزی خیال کی تائید کرتے ہیں بذریعہ: تعریف؛ مثال/ توضیح؛ سبب اور نتیجہ؛ موازنہ اور تقابل؛ حقائق، تمثیلات، واقعات اور اقتباسات۔', 'پراګرافونه تحلیل کړي ترڅو هغه جملې وپېژني چې د اصلي نظر ملاتړ کوي د: تعریف؛ بېلګې/ تشریح؛ لامل او پایلې؛ پرتلې او توپیر؛ حقایقو، ورته والیو، کیسو او نقل‌قولونو له لارې.'),
    ('Use appropriate vocabulary in their own writing.', 'اپنی تحریر میں موزوں ذخیرۂ الفاظ استعمال کریں۔', 'په خپله لیکنه کې مناسب لغات وکاروي.'),
    ('Use pronunciation key to pronounce words with developing accuracy.', 'بڑھتی ہوئی درستی کے ساتھ الفاظ ادا کرنے کے لیے تلفظ کی کلید استعمال کریں۔', 'د زیاتېدونکي دقت سره د کلمو د تلفظ لپاره د تلفظ کیلي وکاروي.'),
    ('Recognize pronounce and represent primary and secondary stress in words with the help of a dictionary.', 'لغت کی مدد سے الفاظ میں بنیادی اور ثانوی زور (اسٹریس) کو پہچانیں، ادا کریں اور ظاہر کریں۔', 'د قاموس په مرسته په کلمو کې لومړنی او دویمی فشار وپېژني، تلفظ یې کړي او وښيي.'),
    ('Use knowledge of roots suffixes and affixes to determine the meaning of unfamiliar words.', 'نامانوس الفاظ کے معنی معلوم کرنے کے لیے مادوں، لاحقوں اور سابقوں کے علم کو استعمال کریں۔', 'د ناپېژندل شویو کلمو د مانا د ټاکلو لپاره د رېښو، وروستاړو او مختاړو له پوهې کار واخلي.'),
    ('Use thesaurus to locate the synonyms closest to the meaning of the given words in the context.', 'سیاق و سباق میں دیے گئے الفاظ کے معنی کے قریب ترین مترادفات تلاش کرنے کے لیے تھیسارس استعمال کریں۔', 'په شرایطو کې د ورکړل شویو کلمو مانا ته تر ټولو نږدې مترادفات د موندلو لپاره تیسارس وکاروي.'),
    ('Use pronunciation key to pronounce words with developing accuracy.', 'بڑھتی ہوئی درستی کے ساتھ الفاظ ادا کرنے کے لیے تلفظ کی کلید استعمال کریں۔', 'د زیاتېدونکي دقت سره د کلمو د تلفظ لپاره د تلفظ کیلي وکاروي.'),
])
op = BOOK.record(o, 'eng12-u04-outcomes', 'Unit 4 — learning outcomes', 'یونٹ 4 — تعلیمی نتائج', 'واحد 4 — د زده کړې پایلې', 22, [32], unit_title=UT)
issues = [{'id': 'eng12-p31-ipa', 'unit': 3, 'printedPage': 31, 'description': 'Miscellaneous-words transcriptions use superscript/raised marks in the scan (e.g. /ˈdɪfɪkˀlt/, /ðeəʳ/, /ˈpi:pˀl/); rendered with the nearest standard IPA (/ˈdɪfɪkəlt/, /ðeər/, /ˈpi:pəl/). Item 6 prints “greatly ___ after. (seek)”.'}]

if __name__ == '__main__':
    BOOK.save(22, [(3, ex), (4, op)], issues=issues, complete_units=[3])
