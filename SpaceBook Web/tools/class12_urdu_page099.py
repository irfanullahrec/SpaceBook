"""Urdu XII PDF99 (spread): p.188 Iqbal author note end + works; p.189 Poem 1 'جوابِ شکوہ' — headnote and stanzas 1–3 (public domain)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
a = Builder()
for x in [
    ("Iqbal is a figure of whom not only Asia but the whole world is proud. He began writing poetry in his school days, but it was after his tour of Europe that his themes were truly settled. He had studied world history, so he was aware of the causes of the Muslims' decline. Through his poetry he gave the message of movement and action. His philosophy of selfhood (khudī) and his concept of the true believer (mard-e momin) became a guiding light for Muslims. Unlike the traditional Urdu poets, Iqbal introduced Urdu poetry to new subjects, ideas, style and philosophical thought. His observation was extremely powerful, and he had mastery of scene-painting. In short, Iqbal's poetry is the best blend of tradition and innovation. Because of his immense poetic qualities he is called the Poet of the East (Shāʿir-e Mashriq), the Sage of the Ummah (Ḥakīm-ul-Ummat) and the Pulse-reader of Nature (Nabbāẓ-e Fiṭrat). Iqbal also had mastery of Arabic and Persian; he has used Qur'anic verses very beautifully in his poetry. Besides this, a large part of his poetry is in Persian; Iqbal's universal ideas are found mostly in his Persian verse.",
     'اقبالؒ وہ ہستی ہیں، جن پر نہ صرف ایشیا بلکہ پوری دُنیا فخر کرتی ہے۔ اُنھوں نے شاعری کا آغاز سکول کے زمانے سے کیا تھا، لیکن دورۂ یورپ کے بعد صحیح معنوں میں اُن کے موضوعات کا تعین ہوا۔ اُنھوں نے تاریخِ عالم کا مطالعہ کیا تھا، اِس لیے وہ مسلمانوں کے زوال کے اسباب سے آگاہ تھے۔ اُنھوں نے اپنی شاعری کے ذریعے حرکت و عمل کا پیغام دیا۔ اُن کا فلسفۂ خودی اور تصوّرِ مردِ مومن مسلمانوں کے لیے مشعلِ راہ بن گیا۔ اُردو کے روایتی شعرا کے برعکس اقبالؒ نے اُردو شاعری کو نئے موضوع، خیالات، اسلوب اور فلسفیانہ خیالات سے روشناس کرایا۔ اُن کا مشاہدہ بے حد قوی تھا۔ منظرنگاری پر اُنھیں عبور حاصل تھا۔ غرض اقبالؒ کی شاعری روایت اور جدت کا بہترین امتزاج ہے۔ اپنی بے پناہ شاعرانہ خصوصیات کے باعث اُنھیں شاعرِ مشرق، حکیم الامت، اور نباضِ فطرت کہا جاتا ہے۔ اقبالؒ کو عربی اور فارسی زبانوں پر بھی عبور حاصل تھا اُنھوں نے اپنے کلام میں قرآنی آیات کا استعمال بڑی خوب صورتی سے کیا ہے۔ اس کے علاوہ اُن کے کلام کا ایک بڑا حصہ فارسی زبان پر مشتمل ہے۔ اقبالؒ کے آفاقی نظریات زیادہ تر اُن کے فارسی کلام میں موجود ہیں۔',
     'اقبال هغه شخصیت دی چې نه یوازې اسیا بلکې ټوله نړۍ پرې ویاړي. هغه د ښوونځي له وخته شاعري پیل کړې وه، خو د اروپا له سفر وروسته یې په رښتینې مانا موضوعګانې وټاکل شوې. هغه د نړۍ تاریخ لوستی و، نو د مسلمانانو د زوال له لاملونو خبر و. د خپلې شاعرۍ له لارې یې د حرکت او عمل پیغام ورکړ. د هغه د "خودۍ" فلسفه او د "مرد مومن" تصور مسلمانانو ته د لارې مشال شو. د اردو د دودیزو شاعرانو پر خلاف اقبال اردو شاعري له نویو موضوعګانو، فکرونو، سبک او فلسفي اندونو سره اشنا کړه. د هغه لید ډېر پیاوړی و؛ پر منظرکښنې یې واک درلود. لنډه دا چې د اقبال شاعري د دود او نوښت غوره ګډون دی. د خپلو بې‌ساري شاعرانه ځانګړنو له امله هغه ته "د ختیځ شاعر"، "حکیم الامت" او "د طبیعت نبض‌پېژندونکی" ویل کېږي. اقبال پر عربي او فارسي ژبو هم واک درلود؛ په خپل کلام کې یې قرآني ایتونه ډېر په ښکلا کارولي. سربېره پر دې د هغه د کلام لویه برخه په فارسي ده؛ د اقبال نړیوال نظریات ډېری د هغه په فارسي کلام کې دي.'),
    ("Works: Bang-e-Dara, Bal-e-Jibreel, Zarb-e-Kaleem, Armaghan-e-Hijaz, Zaboor-e-Ajam, Javed Nama, Asrar-e-Khudi, Rumooz-e-Bekhudi, Pas Che Bayad Kard Ae Aqwam-e-Sharq, Musafir, Payam-e-Mashriq, Ilm-ul-Iqtisad (prose), etc.",
     'تصانیف: بانگِ درا، بالِ جبریل، ضربِ کلیم، ارمغانِ حجاز، زبورِ عجم، جاوید نامہ، اسرارِ خودی، رموزِ بے خودی، پس چہ باید کرد اے اقوامِ شرق، مسافر، پیامِ مشرق، علم الاقتصاد (نثر) وغیرہ',
     'تصنیفات: بانګ درا، بال جبریل، ضرب کلیم، ارمغان حجاز، زبور عجم، جاوید نامه، اسرار خودي، رموز بې‌خودي، پس چه باید کرد ای اقوام شرق، مسافر، پیام مشرق، علم الاقتصاد (نثر) او نور.'),
]: a.p(*x)
au = BOOK.record(a, 'urdu12-u18-author-2', 'About the poet: Allama Iqbal (2)', 'علّامہ اقبالؒ (تعارف ۲)', 'علامه اقبال (پېژندنه ۲)', 99, [187, 188])
au['sourceNote'] = 'The first paragraph begins on p.187 and continues on p.188; it is recorded here whole.'
au['sourceCoverIllustrationReview'] = 'Book-cover image on p.188: “Kulliyat-e-Iqbal (Urdu) — Bang-e-Dara, Bal-e-Jibreel, Zarb-e-Kaleem, Armaghan-e-Hijaz” with Iqbal’s pensive portrait; decorative, not reproduced.'

t = Builder()
t.h('The Answer to the Complaint — Allama Muhammad Iqbal', 'جوابِ شکوہ — علامہ محمد اقبالؒ', 'د شکوې ځواب — علامه محمد اقبال')
t.p("In 1911 Allama Iqbal wrote his world-famous poem “Shikwa” (The Complaint), in which he mentions the decline of the Muslims after their glory and splendour. In this poem Iqbal, on the Muslims' behalf, complained to Allah Almighty about their decline. He wrote “Jawab-e-Shikwa” in 1913, in which “Shikwa” is answered and the real causes of the Muslims' decline are set out in order in the light of the Qur'an and Sunnah. This is the merit of this poem. Therefore, before teaching this poem, a few stanzas of “Shikwa” should be read out in class so that students find it easier to understand “Jawab-e-Shikwa”.",
    '۱۹۱۱ء میں علامہ اقبالؒ نے اپنی شہرۂ آفاق نظم ’’شکوہ‘‘ لکھی جس میں مسلمانوں کی شان و شوکت کے بعد اُن کے زوال کا ذکر کیا ہے۔ اس نظم میں اقبالؒ نے مسلمانوں کے زوال پر اُن کی زبانی اللہ تعالیٰ سے شکوہ کیا ہے۔ ’’جوابِ شکوہ‘‘ اُنھوں نے ۱۹۱۳ء میں لکھی، جس میں ’’شکوہ‘‘ کا جواب دیا گیا ہے اور مسلمانوں کے زوال کے اصل اسباب کو قرآن و سنت کی روشنی میں ترتیب وار بیان کیا گیا ہے۔ یہی اس نظم کی خوبی ہے۔ لہٰذا یہ نظم پڑھانے سے پہلے ’’شکوہ‘‘ کے چند بند جماعت میں پڑھ کر سنائے جائیں تا کہ طلبہ کو ’’جوابِ شکوہ‘‘ سمجھنے میں آسانی رہے۔',
    'په ۱۹۱۱ز کې علامه اقبال خپل نړیوال شهرت لرونکی نظم "شکوه" ولیکه، چې پکې د مسلمانانو له شان او شوکت وروسته د هغوی د زوال یادونه شوې. په دې نظم کې اقبال د مسلمانانو له خولې د هغوی پر زوال الله تعالیٰ ته ګیله کړې. "د شکوې ځواب" یې په ۱۹۱۳ز کې ولیکه، چې پکې "شکوې" ته ځواب ورکړل شوی او د مسلمانانو د زوال اصلي لاملونه د قرآن او سنت په رڼا کې په ترتیب بیان شوي. همدا د دې نظم ښېګڼه ده. نو د دې نظم له تدریس مخکې دې په ټولګي کې د "شکوې" یو څو بندونه ولوستل شي، څو زده‌کوونکو ته د "د شکوې ځواب" پوهېدل اسانه شي.')
S = [
 [('The word that comes from the heart has effect;', 'دل سے جو بات نکلتی ہے اثر رکھتی ہے', 'هغه خبره چې له زړه راوځي اغېز لري؛'),
  ('it has no wings, yet it has the power of flight.', 'پر نہیں، طاقتِ پرواز مگر رکھتی ہے', 'وزر نه لري، خو د الوتو ځواک لري.'),
  ('Its origin is holy; it keeps its gaze on the heights;', 'قدسی الاصل ہے، رفعت پہ نظر رکھتی ہے', 'اصل یې قدسي دی، لوړتیا ته ګوري؛'),
  ('it rises from the dust and passes over the heavens.', 'خاک سے اٹھتی ہے، گردوں پہ گزر رکھتی ہے', 'له خاورې پورته کېږي او له اسمانونو تېرېږي.'),
  ('My love was mischievous, rebellious and clever;', 'عشق تھا فتنہ گر و سرکش و چالاک مرا', 'زما مینه فتنه‌ګره، سرکښه او چالاکه وه؛'),
  ('my bold lament tore through the sky.', 'آسماں چیر گیا نالۂ بیباک مرا', 'زما بې‌باکه فریاد اسمان وڅیره.')],
 [('The old man of the heavens heard it and said, “There is someone somewhere!”', 'پیرِ گردوں نے کہا سن کے، کہیں ہے کوئی!', 'د اسمان زاړه واورېدل او ویې ویل: "چېرته څوک شته!"'),
  ('The planets said, “There is someone on the highest Throne!”', 'بولے سیّارے، سرِ عرشِ بریں ہے کوئی!', 'سیارو وویل: "د لوړ عرش پر سر څوک شته!"'),
  ('The moon said, “No, it is someone of the earth!”', 'چاند کہتا تھا، نہیں، اہلِ زمیں ہے کوئی!', 'سپوږمۍ ویل: "نه، د ځمکې څوک دی!"'),
  ('The Milky Way said, “Someone is hidden right here.”', 'کہکشاں کہتی تھی، پوشیدہ یہیں ہے کوئی', 'کهکشان ویل: "څوک همدلته پټ دی."'),
  ('If anyone understood my complaint at all, it was Riḍwān (the keeper of Paradise):', 'کچھ جو سمجھا مرے شکوے کو تو رضواں سمجھا', 'که چا زما شکوه یو څه وپوهېده، نو رضوان (د جنت ساتونکی) وپوهېد:'),
  ('he took me for the man expelled from Paradise.', 'مجھے جنت سے نکالا ہوا انساں سمجھا', 'هغه زه له جنته ایستل شوی انسان وګڼلم.')],
 [('Even the angels were astonished: what is this voice?', 'تھی فرشتوں کو بھی حیرت کہ یہ آواز ہے کیا!', 'پرښتې هم حیرانې وې چې دا څه غږ دی!'),
  ('Even to those of the Throne this secret is not revealed — what is it?', 'عرش والوں پہ بھی کھلتا نہیں یہ راز ہے کیا!', 'د عرش خلکو ته هم دا راز نه پرانیستل کېږي چې څه دی!'),
  ('Does man’s striving reach even to the top of the Throne?', 'تا سرِ عرش بھی انساں کی تگ و تاز ہے کیا؟', 'ایا د انسان منډه ترړه تر عرش پورې هم رسېږي؟'),
  ('Has even a pinch of dust learned to fly?', 'آ گئی خاک کی چٹکی کو بھی پرواز ہے کیا؟', 'ایا د خاورې یوې چونډۍ ته هم الوتنه راغلې؟'),
  ('How heedless of manners are the dwellers of the earth!', 'غافل آداب سے سُکّانِ زمیں کیسے ہیں!', 'د ځمکې اوسېدونکي له ادبه څومره غافل دي!'),
  ('How pert and insolent are these residents of the lowly world!', 'شوخ و گستاخ یہ پستی کے مکیں کیسے ہیں!', 'د ټیټې نړۍ دا اوسېدونکي څومره شوخ او ګستاخ دي!')],
]
for i, st in enumerate(S, 1):
    t.p(f'Stanza {i}', f'بند {"۰۱۲۳۴۵۶۷۸۹"[i]}', f'بند {i}')
    t.group('lines', st)
po = BOOK.record(t, 'urdu12-u18-poem-1', 'Poem text (1): stanzas 1–3', 'متنِ نظم (۱): بند ۱–۳', 'د نظم متن (۱): بندونه ۱–۳', 99, [189])
issues = [{'id': 'urdu12-pdf099', 'unit': 18, 'printedPage': 189, 'description': 'Jawab-e-Shikwa (Iqbal, d.1938) is public domain and transcribed in full; English and Pashto renderings are line-by-line prose translations. A pen underline under “1911” and “1913” in the headnote is an owner mark, excluded.'}]

if __name__ == '__main__':
    BOOK.save(99, [(18, au), (18, po)], issues=issues)
