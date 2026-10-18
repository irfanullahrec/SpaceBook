"""PDF99 (printed 185–186): 'Lord of the Flies' (William Golding, 1954 — copyrighted; textbook abridgement) Chapter 1 — paragraph-wise summary, part 1."""
from class12_book_common import Book, Builder

BOOK = Book('english')
s = Builder()
s.h('Lord of the Flies — CHAPTER 1', 'لارڈ آف دی فلائیز — باب 1', 'لارډ آف دي فلایز — لومړی څپرکی')
s.p('[Summary — the textbook prints an abridged adaptation of William Golding’s novel (1954), a modern copyrighted work; read the full abridged text in the printed textbook, pp. 185–221. The app gives a paragraph-wise summary.]',
    '[خلاصہ — درسی کتاب میں ولیم گولڈنگ کے ناول (1954) کی مختصر شدہ صورت دی گئی ہے، جو جدید کاپی رائٹ شدہ تخلیق ہے؛ مکمل مختصر متن درسی کتاب کے صفحات 185–221 میں پڑھیں۔ ایپ پیراگراف وار خلاصہ دیتی ہے۔]',
    '[لنډیز — درسي کتاب د ویلیم ګولډینګ د ناول (1954) لنډه شوې بڼه چاپ کړې، چې نوی د کاپي رایټ لاندې اثر دی؛ بشپړ لنډ شوی متن په چاپي درسي کتاب کې په 185–221 مخونو کې ولولئ. اپلیکېشن پراګراف په پراګراف لنډیز وړاندې کوي.]')
P = [
    ('On a tropical island, a fair-haired twelve-year-old boy climbs out of the scar left by a plane wreck towards a lagoon and meets a fat boy with glasses; the fair boy says his name is Ralph.',
     'ایک گرمسیری جزیرے پر سنہرے بالوں والا بارہ سالہ لڑکا ہوائی جہاز کے ملبے سے بنے نشان (scar) سے نکل کر ایک جھیل کی طرف آتا ہے اور عینک والے ایک موٹے لڑکے سے ملتا ہے؛ سنہرے بالوں والا لڑکا اپنا نام رالف بتاتا ہے۔',
     'په یوه تودې سیمې ټاپو کې، یو د زرینو وېښتانو دولس کلن هلک د الوتکې د ملبې له پرېښودل شوي نښان (scar) څخه د یو جهیل پر لور راوځي او له عینکې لرونکي یو چاغ هلک سره ګوري؛ زرین وېښتانو هلک وايي چې نوم یې رالف دی.'),
    ('Their talk shows that the boys survived a plane crash in the Pacific with no adults left alive; they had apparently been evacuated from an atomic war in England. Ralph believes his father, a Navy commander, will rescue them, but Piggy says the adults were probably all killed by the atom bomb.',
     'ان کی گفتگو سے معلوم ہوتا ہے کہ لڑکے بحرالکاہل میں طیارے کے حادثے میں بچ گئے اور کوئی بالغ زندہ نہیں بچا؛ بظاہر انہیں انگلستان میں ایٹمی جنگ سے نکالا جا رہا تھا۔ رالف کو یقین ہے کہ اس کا باپ، جو بحریہ میں کمانڈر ہے، انہیں بچا لے گا، لیکن پگی کہتا ہے کہ بالغ شاید سب ایٹم بم سے مارے گئے۔',
     'د هغوی له خبرو څرګندېږي چې هلکان په ارام سمندر کې د الوتکې له پېښې ژوندي پاتې شوي او هیڅ لوی سړی ژوندی نه دی پاتې؛ ښکاري چې له انګلستان څخه د اټومي جګړې له امله ایستل کېدل. رالف باور لري چې پلار یې، چې په بحري ځواک کې قوماندان دی، هغوی ژغوري، خو پګي وايي چې لوی خلک به ښايي ټول په اټوم بم وژل شوي وي.'),
    ('Ralph is thrilled to be free of adults; he explores the beach, finds a natural pool in the lagoon and plunges in. The fat boy suggests making a list of names and holding a meeting, and admits he used to be called “Piggy” — which Ralph at once uses to tease him.',
     'رالف بالغوں سے آزادی پر خوش ہے؛ وہ ساحل کی سیر کرتا ہے، جھیل میں ایک قدرتی تالاب پاتا ہے اور اس میں کود جاتا ہے۔ موٹا لڑکا ناموں کی فہرست بنانے اور اجلاس کرنے کی تجویز دیتا ہے، اور اعتراف کرتا ہے کہ اسے ’’پگی‘‘ کہا جاتا تھا — جسے رالف فوراً اسے چھیڑنے کے لیے استعمال کرتا ہے۔',
     'رالف له لویانو د ازادۍ له امله ډېر خوشحاله دی؛ ساحل لټوي، په جهیل کې یو طبیعي حوض مومي او ورټوپ وهي. چاغ هلک وړاندیز کوي چې د نومونو لیست جوړ او غونډه وشي، او مني چې "پګي" ورته ویل کېده — چې رالف یې سمدستي د ټوکو لپاره کاروي.'),
    ('Piggy cannot swim because of his asthma; Ralph boasts that his Navy father taught him at five and will come to rescue them. Piggy says his own father is dead and he lived with his auntie, and insists they must find the others.',
     'پگی دمے کی وجہ سے تیر نہیں سکتا؛ رالف شیخی بگھارتا ہے کہ اس کے بحریہ والے باپ نے اسے پانچ سال کی عمر میں سکھایا تھا اور وہ انہیں بچانے آئے گا۔ پگی بتاتا ہے کہ اس کا باپ مر چکا ہے اور وہ اپنی خالہ کے ساتھ رہتا تھا، اور اصرار کرتا ہے کہ انہیں دوسروں کو تلاش کرنا چاہیے۔',
     'پګي د ساه لنډۍ له امله لامبو نه شي وهلی؛ رالف ویاړ کوي چې بحري پلار یې په پنځه کلنۍ کې ورته زده کړې او هغوی به ژغوري. پګي وايي چې پلار یې مړ دی او له خپلې ترور سره اوسېده، او ټینګار کوي چې باید نور ومومي.'),
    ('Ralph spots something creamy in the weeds — a conch shell, which Piggy recognises as valuable. They retrieve it, and on Piggy’s suggestion Ralph blows it with all his breath to call the others to a meeting.',
     'رالف جھاڑیوں میں کوئی کریمی سی چیز دیکھتا ہے — ایک سیپی (conch)، جسے پگی قیمتی پہچانتا ہے۔ وہ اسے نکال لاتے ہیں، اور پگی کی تجویز پر رالف پوری سانس سے اسے پھونکتا ہے تاکہ دوسروں کو اجلاس کے لیے بلایا جائے۔',
     'رالف په بوټو کې یو کریمي شی ویني — یوه لویه سمندري سیپۍ (conch)، چې پګي یې قیمتي پېژني. هغوی یې راباسي، او د پګي په وړاندیز رالف په ټوله ساه پکې پوکي ترڅو نور غونډې ته راوبلي.'),
    ('A small boy of about six, Johnny, comes out of the palms first; more boys follow, obeying Ralph as they had obeyed “the man with the megaphone”. (continued on p. 187)',
     'تقریباً چھ سال کا ایک چھوٹا لڑکا، جانی، سب سے پہلے کھجوروں سے نکلتا ہے؛ پھر اور لڑکے آتے ہیں، جو رالف کی ویسے ہی اطاعت کرتے ہیں جیسے ’’میگافون والے آدمی‘‘ کی کرتے تھے۔ (صفحہ 187 پر جاری)',
     'شاوخوا شپږ کلن یو کوچنی هلک، جاني، لومړی له کجورو راوځي؛ نور هلکان ورپسې راځي، او د رالف اطاعت داسې کوي لکه د "میګافون والا سړي" یې چې کاوه. (په 187 مخ کې دوام)'),
]
for x in P: s.p(*x)
rec = BOOK.record(s, 'eng12-u19-ch1-a', 'Lord of the Flies — Chapter 1 (summary, 1)', 'لارڈ آف دی فلائیز — باب 1 (خلاصہ، 1)', 'لارډ آف دي فلایز — څپرکی 1 (لنډیز، 1)', 99, [185, 186])
rec['sourceGap'] = 'Modern copyrighted novel (William Golding, 1954), printed as a textbook abridgement; paragraph-wise summary in the app, not verbatim. Printed pp. 185–186.'
rec['sourceCoverIllustrationReview'] = 'Film still (a boy with a sling and a group of boys on a beach) is decorative; not reproduced.'
issues = [{'id': 'eng12-u19-copyright', 'unit': 19, 'printedPage': 185, 'description': 'Unit 19 prints an abridged, adapted version of “Lord of the Flies” (William Golding, 1954 — copyrighted); the app carries a paragraph-wise summary with sourceGap notes for pp.185–221. Exercise items that quote the novel are given as references.'}]

if __name__ == '__main__':
    BOOK.save(99, [(19, rec)], issues=issues)
