"""PDF27 (printed 41–42): Unit 4 Vocabulary B 17–20, C word–clue matching (unit end); Unit 5 opener 'The Last Leaf' (O. Henry) outcomes."""
from class12_book_common import Book, Builder

BOOK = Book('english')
B = '________'
w = Builder()
w.group('lines', [
    (f'17. Half of the students were present, but the other half were {B}.', f'17. آدھے طلبہ حاضر (present) تھے، لیکن باقی آدھے {B} تھے۔', f'17. نیمایي زده کوونکي حاضر (present) وو، خو نوره نیمایي {B} وو.'),
    (f'18. Attendance at classis compulsory, but the afternoon social programmes are {B}.', f'18. جماعت میں حاضری لازمی (compulsory) ہے، لیکن سہ پہر کے سماجی پروگرام {B} ہیں۔', f'18. په ټولګي کې حاضري لازمي (compulsory) ده، خو د ماسپښین ټولنیز پروګرامونه {B} دي.'),
    (f'19. There have been a few major accidents on this road, but fortunately the injuries have been {B}.', f'19. اس سڑک پر چند بڑے (major) حادثات ہوئے ہیں، لیکن خوش قسمتی سے زخم {B} رہے ہیں۔', f'19. پر دې سړک څو لویې (major) پېښې شوې، خو له نېکه مرغه ټپونه {B} وو.'),
    (f'20. I prefer strong to {B} coffee.', f'20. میں تیز (strong) کافی کو {B} کافی پر ترجیح دیتا ہوں۔', f'20. زه تېز (strong) قهوه تر {B} قهوې غوره ګڼم.'),
])
w.p('C. Read each word below. Match it to its clue, and then write each word on the line next to its clue.', 'C. نیچے دیا گیا ہر لفظ پڑھیں۔ اسے اس کے اشارے سے ملائیں، اور پھر ہر لفظ اس کے اشارے کے ساتھ والی لکیر پر لکھیں۔', 'C. لاندې هره کلمه ولولئ. له خپلې نښې سره یې برابره کړئ، او بیا هره کلمه د هغې د نښې تر څنګ پر کرښه ولیکئ.')
w.p('homonym, novennial, dentist, popular, dual, quadruped, fraternity, union, Neolithic, urbanite decapitate, revive, patriotism, victim', 'homonym, novennial, dentist, popular, dual, quadruped, fraternity, union, Neolithic, urbanite decapitate, revive, patriotism, victim', 'homonym, novennial, dentist, popular, dual, quadruped, fraternity, union, Neolithic, urbanite decapitate, revive, patriotism, victim')
w.paras[-1]['untranslatedByDesign'] = True
CL = [
    ('someone who lives in an urban area', 'وہ شخص جو شہری علاقے میں رہتا ہو', 'هغه کس چې په ښاري سیمه کې اوسېږي'),
    ('to bring back to life', 'دوبارہ زندہ کرنا', 'بېرته ژوندي کول'),
    ('brotherhood', 'بھائی چارہ', 'ورورولي'),
    ('a feeling of friendship and brotherhood', 'دوستی اور بھائی چارے کا احساس', 'د دوستۍ او ورورولۍ احساس'),
    ('to cut off the head', 'سر قلم کرنا', 'سر پرې کول'),
    ('love of country', 'وطن سے محبت', 'له هېواد سره مینه'),
    ('same name', 'ایک ہی نام', 'یو شان نوم'),
    ('a person who codified to treat disease of gums and teeth', 'وہ شخص جو مسوڑھوں اور دانتوں کی بیماری کے علاج کا اہل ہو', 'هغه کس چې د ورو او غاښونو د ناروغیو د درملنې وړ وي'),
    ('consisting of two parts', 'دو حصوں پر مشتمل', 'له دوو برخو جوړ'),
    ('someone who has suffered a misfortune', 'وہ شخص جس پر کوئی مصیبت آئی ہو', 'هغه کس چې پرې ناورین راغلی وي'),
    ('happening every November', 'ہر نومبر میں ہونے والا', 'په هر نومبر کې پېښېدونکی'),
    ('liked or admired by many people', 'بہت سے لوگوں کا پسندیدہ یا ان کی تعریف کا حامل', 'د ډېرو خلکو خوښ یا ستایل شوی'),
    ('having four feet', 'چار پاؤں والا', 'څلور پښې لرونکی'),
    ('joining or being joined', 'جوڑنا یا جڑ جانا', 'یوځای کول یا یوځای کېدل'),
]
w.group('lines', [(f'{i}. {e} {B}', f'{i}. {u} {B}', f'{i}. {p} {B}') for i, (e, u, p) in enumerate(CL, 1)])
ex = BOOK.record(w, 'eng12-u04-exercises-b', 'Vocabulary B (17–20) and C (word clues)', 'ذخیرۂ الفاظ B (17–20) اور C (الفاظ کے اشارے)', 'لغات B (17–20) او C (د کلمو نښې)', 27, [41])

UT = ('The Last Leaf', 'آخری پتا', 'وروستۍ پاڼه')
o = Builder()
o.h('Unit 5 — The Last Leaf (O. Henry)', 'یونٹ 5 — آخری پتا (او۔ ہنری)', 'واحد 5 — وروستۍ پاڼه (او. هنري)')
o.p('By the end of the unit, the students will be able to:', 'اس یونٹ کے اختتام تک طلبہ اس قابل ہوں گے کہ:', 'د دې واحد په پای کې به زده کوونکي وکولای شي چې:')
o.group('list', [
    ('Analyze story elements: characters, events, setting, plot, theme, tone, point of view; identify the speaker or narrator in a selection; recognize the author’s purpose and point of view and their effects on the texts; identify universal themes present in literature across all cultures.', 'کہانی کے عناصر کا تجزیہ کریں: کردار، واقعات، پس منظر، پلاٹ، موضوع، لہجہ، نقطۂ نظر؛ کسی انتخاب میں بولنے والے یا راوی کی نشاندہی کریں؛ مصنف کے مقصد اور نقطۂ نظر اور متون پر ان کے اثرات کو پہچانیں؛ تمام ثقافتوں کے ادب میں موجود آفاقی موضوعات کی نشاندہی کریں۔', 'د کیسې عناصر تحلیل کړي: کرکټرونه، پېښې، ځای او وخت، پلاټ، موضوع، لهجه، لیدلوری؛ په یوه ټاکنه کې ویونکی یا راوي وپېژني؛ د لیکوال موخه او لیدلوری او پر متنونو یې اغېزې وپېژني؛ په ټولو کلتورونو کې په ادب کې موجودې نړیوالې موضوعات وپېژني.'),
    ('Apply critical thinking to interact with text, use intensive reading strategies (while-reading) to scan to answer short questions.', 'متن سے تعامل کے لیے تنقیدی سوچ کا اطلاق کریں، گہرے مطالعے کی حکمتِ عملیاں (دورانِ مطالعہ) استعمال کریں تاکہ مختصر سوالات کے جواب کے لیے متن میں تلاش کریں۔', 'له متن سره د تعامل لپاره انتقادي فکر پلي کړي، د ژورو لوستلو ستراتیژۍ (د لوستلو پر مهال) وکاروي ترڅو د لنډو پوښتنو د ځوابولو لپاره متن ولټوي.'),
    ('Use the knowledge of roots, suffixes and affixes to determine the meaning of unfamiliar words.', 'نامانوس الفاظ کے معنی معلوم کرنے کے لیے مادوں، لاحقوں اور سابقوں کے علم کو استعمال کریں۔', 'د ناپېژندل شویو کلمو د مانا د ټاکلو لپاره د رېښو، وروستاړو او مختاړو له پوهې کار واخلي.'),
    ('Use summary skills to extract salient points and develop a mind map to summarize a text.', 'خلاصہ نویسی کی مہارتیں استعمال کریں تاکہ نمایاں نکات نکالیں اور متن کا خلاصہ کرنے کے لیے ذہنی نقشہ بنائیں۔', 'د لنډیز مهارتونه وکاروي ترڅو برجسته ټکي راوباسي او د متن د لنډیز لپاره ذهني نقشه جوړه کړي.'),
    ('Recognize and pronounce primary and secondary stress in words with help of dictionary.', 'لغت کی مدد سے الفاظ میں بنیادی اور ثانوی زور کو پہچانیں اور ادا کریں۔', 'د قاموس په مرسته په کلمو کې لومړنی او دویمی فشار وپېژني او تلفظ یې کړي.'),
    ('Use knowledge of roots, suffixes and affixes to determine the meaning of unfamiliar words.', 'نامانوس الفاظ کے معنی معلوم کرنے کے لیے مادوں، لاحقوں اور سابقوں کے علم کو استعمال کریں۔', 'د ناپېژندل شویو کلمو د مانا د ټاکلو لپاره د رېښو، وروستاړو او مختاړو له پوهې کار واخلي.'),
    ('Use thesaurus to locate the synonyms closest to the meaning of the given words in the context.', 'سیاق و سباق میں دیے گئے الفاظ کے معنی کے قریب ترین مترادفات تلاش کرنے کے لیے تھیسارس استعمال کریں۔', 'په شرایطو کې د ورکړل شویو کلمو مانا ته تر ټولو نږدې مترادفات د موندلو لپاره تیسارس وکاروي.'),
    ('Parse a sentences into their component parts and describe their syntactic roles.', 'جملوں کو ان کے اجزاء میں تقسیم (تجزیہ) کریں اور ان کے نحوی کردار بیان کریں۔', 'جملې په خپلو برخو ووېشي (تجزیه کړي) او د هغو نحوي رول بیان کړي.'),
    ('Use pronunciation key to pronounce words with developing accuracy.', 'بڑھتی ہوئی درستی کے ساتھ الفاظ ادا کرنے کے لیے تلفظ کی کلید استعمال کریں۔', 'د زیاتېدونکي دقت سره د کلمو د تلفظ لپاره د تلفظ کیلي وکاروي.'),
])
op = BOOK.record(o, 'eng12-u05-outcomes', 'Unit 5 — learning outcomes', 'یونٹ 5 — تعلیمی نتائج', 'واحد 5 — د زده کړې پایلې', 27, [42], unit_title=UT)
op['sourceCoverIllustrationReview'] = 'Photograph of a leaf on water is decorative; not reproduced.'
issues = [{'id': 'eng12-p41-42', 'unit': 4, 'printedPage': 41, 'description': 'Right edge of printed p41 clipped (item 17 “were [absent]”, item 18 “programmes are”, item 19 “injuries”); blanks kept. Printed text retained: “at classis”, “who codified to treat” (qualified), “happening every November” for novennial (every nine years), “urbanite decapitate” (missing comma); Unit 5 outcomes “Parse a sentences”.'}]

if __name__ == '__main__':
    BOOK.save(27, [(4, ex), (5, op)], issues=issues, complete_units=[4])
