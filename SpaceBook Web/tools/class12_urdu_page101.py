"""Urdu XII PDF101 (spread): printed pp.192–193 — Poem 1 مشق Q1–Q6 and notes on نظم / پابند نظم."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Write answers to the following questions according to the poem.', '۱۔ نظم کے مطابق درج ذیل سوالات کے جوابات لکھیں۔', '۱. د نظم سره سم لاندې پوښتنو ته ځوابونه ولیکئ.')
e.group('lines', [
    ("(a) In what form (hai'at) is this poem of Allama Iqbal written?", '(ا) علامہ اقبالؒ کی یہ نظم کس ہیئت میں لکھی گئی ہے؟', '(الف) د علامه اقبال دا نظم په کومه بڼه (هیئت) لیکل شوی؟'),
    ('(b) What thoughts did the angels express on hearing the “Shikwa”?', '(ب) ’’شکوہ‘‘ سُن کر فرشتوں نے کن خیالات کا اظہار کیا؟', '(ب) د "شکوې" په اورېدو پرښتو کوم فکرونه څرګند کړل؟'),
    ("(c) What weaknesses and shortcomings of present-day Muslims are mentioned in this poem?", '(ج) اس نظم میں موجودہ دور کے مسلمانوں کی کن کمزوریوں اور خامیوں کا ذکر ہے؟', '(ج) په دې نظم کې د اوسني دور د مسلمانانو د کومو کمزوریو او نیمګړتیاوو یادونه شوې؟'),
    ('(d) Pick out and write lines (miṣraʿ) from this poem in which the figure of allusion (talmīḥ) is used.', '(د) اس نظم سے ایسے مصرعے چُن کر لکھیں جن میں صنعتِ تلمیح کا استعمال ہو۔', '(د) له دې نظمه داسې مصرعې غوره کړئ او ولیکئ چې پکې د تلمیح صنعت کارول شوی وي.'),
    ('(e) Why has this poem been named “Jawab-e-Shikwa”?', '(ہ) اس نظم کا نام ’’جوابِ شکوہ‘‘ کیوں رکھا گیا ہے؟', '(ه) د دې نظم نوم "جواب شکوه" ولې ایښودل شوی؟'),
    ('(f) Explain “the idols too are new”.', '(و) ’’بُت بھی نئے‘‘ کی تشریح کریں۔', '(و) "بتان هم نوي" تشریح کړئ.'),
    ("(g) In the last stanza, what has been called the Muslim's sword?", '(ز) آخری بند میں کس چیز کو مسلمان کی شمشیر کہا گیا ہے؟', '(ز) په وروستي بند کې کوم شی د مسلمان توره بلل شوی؟'),
    ('(h) How do the members of the Ummah become a cause of disgrace for the Holy Prophet (peace and blessings of Allah be upon him and his family)?', '(ح) امتی نبی کریم صلی اللہ علیہ وآلہٖ وسلم کی رسوائی کا کیسے باعث بنتے ہیں؟', '(ح) امتیان څنګه د نبي کریم صلی الله علیه وآله وسلم د رسوايۍ لامل کېږي؟'),
    ('(i) What is the reward for loving the Holy Prophet (peace and blessings of Allah be upon him and his family)?', '(ط) نبی اکرم صلی اللہ علیہ وآلہٖ وسلم سے محبت کرنے کا کیا انعام ہے؟', '(ط) له نبي اکرم صلی الله علیه وآله وسلم سره د مینې انعام څه دی؟'),
    ("(j) By the blessing of whose name has the poem urged us to bring light to the world?", '(ی) دنیا میں کس کے نام کی برکت سے روشنی کرنے کی تلقین کی گئی ہے؟', '(ی) په نړۍ کې د چا د نوم په برکت د رڼا خورولو تلقین شوی؟'),
])
e.p('2. Put diacritics on the following words: manfaʿat, maṣlaḥat, Ramaḍān, asrār, sipar.', '۲۔ درج ذیل الفاظ پر اعراب لگائیں: منفعت، مصلحت، رمضان، اسرار، سپر۔', '۲. پر لاندې کلمو اعراب کېږدئ: منفعت، مصلحت، رمضان، اسرار، سپر.')
e.p('3. Read this couplet:', '۳۔ یہ شعر پڑھیں:', '۳. دا بیت ولولئ:')
e.group('lines', [
    ('They were honoured in their age by being Muslims,', 'وہ زمانے میں معزز تھے مسلماں ہو کر', 'هغوی په زمانه کې د مسلمان په توګه معزز وو،'),
    ('and you have been disgraced by abandoning the Qur’an.', 'اور تم خوار ہوئے تارکِ قرآں ہو کر', 'او تاسو د قرآن په پرېښودو خوار شوئ.'),
])
e.p('Mentioning two things in a text and stating the difference between them is called the figure of distinction (ṣanʿat-e tafrīq). Find and write at least three couplets in this poem in which the figure of distinction is present.',
    'کلام میں دو چیزوں کا ذکر کر کے دونوں کے درمیان فرق بتانے کو صنعتِ تفریق کہتے ہیں۔ اس نظم میں کم از کم تین ایسے اشعار تلاش کر کے لکھیں جن میں صنعتِ تفریق موجود ہو۔',
    'په کلام کې د دوو شیانو یادونه او د دواړو ترمنځ د توپیر ښودلو ته "د تفریق صنعت" ویل کېږي. په دې نظم کې لږ تر لږه درې داسې بیتونه ومومئ او ولیکئ چې پکې د تفریق صنعت وي.')
e.p('4. Choose the correct word and fill in the blank.', '۴۔ درست لفظ چن کر خالی جگہ پُر کریں۔', '۴. سمه کلمه غوره کړئ او تش ځای ډک کړئ.')
e.group('lines', [
    ("(a) “Jawab-e-Shikwa” is in fact the answer to another poem of Iqbal, ________ . (Saqi Nama, Khizr-e-Rah, Shikwa, Tulu-e-Islam)", '(ا) جوابِ شکوہ‘ دراصل اقبالؒ کی ایک اور نظم ________ کا جواب ہے۔ (ساقی نامہ، خضرِ راہ، شکوہ، طلوعِ اسلام)', '(الف) "جواب شکوه" په اصل کې د اقبال د یو بل نظم ________ ځواب دی. (ساقي نامه، خضر راه، شکوه، طلوع اسلام)'),
    ('(b) A voice came: “Your ________ is moving.” (tale, cup, mad, tavern)', '(ب) آئی آواز غم انگیز ہے ________ تیرا (افسانہ، پیمانہ، دیوانہ، مے خانہ)', '(ب) غږ راغی: ستا ________ غمجن دی. (افسانه، پیمانه، دیوانه، میخانه)'),
    ('(c) Its origin is holy; it keeps its gaze on ________ . (wealth, riches, height, power)', '(ج) قدسی الاصل ہے ________ پہ نظر رکھتی ہے (دولت، ثروت، رفعت، قدرت)', '(ج) اصل یې قدسي دی، پر ________ نظر ساتي. (دولت، ثروت، رفعت، قدرت)'),
    ('(d) ________ have no manners in speaking. (humans, the ignorant, the mad, animals)', '(د) بات کرنے کا سلیقہ نہیں ________ کو (انسانوں، نادانوں، دیوانوں، حیوانوں)', '(د) ________ ته د خبرو سلیقه نشته. (انسانانو، ناپوهانو، لېونیو، حیواناتو)'),
])
e.p('5. Pick out and write at least ten rhyming words from this poem.', '۵۔ اس نظم میں سے کم از کم دس ہم قافیہ الفاظ چن کر لکھیں۔', '۵. له دې نظمه لږ تر لږه لس هم‌قافیه کلمې غوره کړئ او ولیکئ.')
e.p('6. Of the Persian compounds (tarākīb) used in this poem, write at least ten.', '۶۔ اس نظم میں جو فارسی تراکیب استعمال ہوئی ہیں ان میں سے کم از کم دس تراکیب لکھیں۔', '۶. په دې نظم کې کارول شویو فارسي ترکیبونو څخه لږ تر لږه لس ولیکئ.')
ex = BOOK.record(e, 'urdu12-u18-exercise', 'Exercise', 'مشق', 'تمرین', 101, [192, 193])

n = Builder()
n.h('Naẓm (poem)', 'نظم', 'نظم')
n.group('lines', [
    ('1. The literal meaning of naẓm is “to string”, as pearls are strung on a thread. In literature a collection of verses is called a naẓm.', '۱۔ نظم کے لفظی معنی ہیں ’’پرونا‘‘ جیسے موتی لڑی میں پروئے جاتے ہیں۔ ادب کی رُو سے اشعار کے مجموعے کو نظم کہتے ہیں۔', '۱. د نظم لفظي مانا "پېيل" ده، لکه مرغلرې چې په تار کې پېيل کېږي. د ادب له مخې د بیتونو ټولګې ته نظم ویل کېږي.'),
    ('2. “Verses written on a single idea or subject are called a naẓm.”', '۲۔ ’’کسی ایک خیال یا موضوع کے تحت لکھے گئے اشعار کو نظم کہتے ہیں‘‘۔', '۲. "هغو بیتونو ته چې د یوه فکر یا موضوع لاندې لیکل شوي وي، نظم ویل کېږي."'),
])
n.h('Pābaṇd naẓm (bound / regular poem)', 'پابند نظم', 'پابند نظم')
n.p('In this kind of poem, besides metre and baḥr, adherence to rhyme (qāfiya) and often also refrain (radīf) is necessary.', 'اس نظم میں وزن اور بحر کے ساتھ ساتھ قافیہ اور بسا اوقات ردیف کی پابندی بھی ضروری ہوتی ہے۔', 'په دې ډول نظم کې له وزن او بحر سره سره د قافیې او ډېری وخت د ردیف پابندي هم ضروري ده.')
nt = BOOK.record(n, 'urdu12-u18-notes', 'Notes: naẓm and pābaṇd naẓm', 'نظم اور پابند نظم', 'نظم او پابند نظم', 101, [193])
issues = [{'id': 'urdu12-pdf101', 'unit': 18, 'printedPage': 192, 'description': 'Q4(a) opens with an unmatched closing quotation mark (“جوابِ شکوہ‘”) as printed. Faint background drawing behind the exercise is decorative.'}]

if __name__ == '__main__':
    BOOK.save(101, [(18, ex), (18, nt)], issues=issues, complete_units=[18])
