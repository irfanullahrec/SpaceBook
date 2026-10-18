"""Mutalia-e-Quran XII PDF53: p.50 — Lesson 5 matters of knowledge and action; vocabulary. Run: python class12_quran_page053.py"""
from class12_quran_common import BOOK, Builder, rec, KA, L, VOC

VOCAB = [
    ('ثُمَّ ازْدَادُوا', 'Then they went on increasing', 'پھر وہ بڑھتے چلے گئے', 'بیا وړاندې لاړل'),
    ('يَتَرَبَّصُونَ', 'They are waiting', 'وہ انتظار کر رہے ہیں', 'انتظار کوي'),
    ('نَمْنَعْكُمْ', 'We protected you', 'ہم نے تمھیں بچایا', 'موږ تاسو وژغورلئ'),
    ('الدَّرْكِ', 'Level, depth', 'طبقہ', 'طبقه'),
    ('وَاعْتَصَمُوا', 'And they held fast', 'اور انھوں نے مضبوطی سے تھام لیا', 'او کلکې منګولې یې ولګولې'),
    ('تُخْفُوهُ', 'You conceal it', 'تم اسے چھپاؤ', 'یې پټ کړئ'),
    ('يَسْأَلُكَ', 'They demand of you', 'وہ آپ سے مطالبہ کرتے ہیں', 'له تاسو غوښتنه کوي'),
    ('الْعِجْلَ', 'The calf', 'بچھڑا', 'سخی'),
    ('تَرَكَ', 'He left', 'اس نے چھوڑا', 'هغه پرېښود'),
    ('بَشِّرِ', 'Give glad tidings', 'آپ خوش خبری دے دیجیے', 'زېری ورکړئ'),
    ('أَلَمْ نَسْتَحْوِذْ', 'Did we not encircle', 'کیا ہم نے گھیر نہ لیا تھا', 'ایا موږ نه وئ را ګېر کړي'),
    ('كُسَالَى', 'Lazily', 'سستی', 'سستي'),
    ('الْأَسْفَلِ', 'The lowest', 'سب سے نچلا', 'تر ټولو ښکته'),
    ('إِنْ تُبْدُوا', 'If you disclose', 'اگر تم ظاہر کرو', 'که ښکاره کړئ'),
    ('تَعْفُوا', 'You pardon', 'تم معاف کر دو', 'وبښئ'),
    ('جَهْرَةً', 'Openly', 'علانیہ طور پر', 'په ښکاره'),
    ('اسْتَنْكَفُوا', 'They disdained', 'انھوں نے عار کیا', 'شرم یې وګاڼه'),
    ('يُبَيِّنُ', 'He makes clear', 'وہ بیان کرتا ہے', 'روښانه بیانوي'),
]


def p53():
    b = Builder()
    KA(b)
    L(b, [('Allah Almighty has commanded us to do justice in every situation and every matter, even if the true word is against ourselves or our parents, relatives, the rich or the poor. Justice is commanded not only in judicial matters, but also in domestic life, mutual affairs, transactions, and with everyone whether one\'s own or a stranger.', 'اللہ تعالیٰ نے ہمیں ہر حال اور ہر معاملہ میں عدل کرنے کا حکم دیا ہے خواہ عدل کی بات خود ہمارے خلاف ہو یا والدین، رشتے دار، دولت مند یا غریب کے خلاف ہو صرف عدالتی معاملات ہی نہیں بلکہ خانہ داری، باہمی معاملات، لین دین، اپنے بیگانے ہر ایک کے ساتھ عدل کرنے کا حکم ہے۔', 'الله تعالی موږ ته په هر حال او هره چاره کې د عدل حکم کړی، که څه هم د عدل خبره زموږ یا زموږ د مور و پلار، خپلوانو، شتمن یا بېوزله پر خلاف وي؛ نه یوازې په قضايي چارو، بلکې په کورنۍ، منځنیو چارو، راکړه ورکړه او له خپل او پردي هر چا سره د عدل حکم دی.'),
          ('Sitting in a gathering in which the verses of Allah Almighty are being denied and religion is being mocked amounts to supporting disbelief and mockery. One should always stay away from such evil gatherings.', 'جس مجلس میں اللہ تعالیٰ کی آیات کا انکار اور دین کا مذاق اُڑایا جا رہا ہو اس میں بیٹھنا کفر و استہزاء کا ساتھ دینے کے مترادف ہے ایسی بُری مجالس سے ہمیشہ دور رہنا چاہیے۔', 'په هغه مجلس کې ناسته چې پکې د الله تعالی له آیتونو انکار او پر دین ملنډې کېږي، د کفر او ملنډو له ملاتړ سره برابره ده؛ له داسې بدو مجلسونو باید تل لرې پاتې شو.'),
          ('One purpose of the sending of the Messengers was that they give the believers glad tidings of Paradise and warn those persisting in disbelief of the punishment of Hell, so that the proof is completed upon people in this way and on the Day of Resurrection they cannot present any excuse before Allah Almighty for their disbelief and bad deeds.', 'رسولوں کی بعثت کا ایک مقصد یہ تھا کہ وہ اہلِ ایمان کو جنت کی خوش خبری دیں اور کفر پر جمے رہنے والوں کو عذابِ جہنم سے ڈرائیں تاکہ اس طرح لوگوں پر اتمامِ حجت ہو جائے اور وہ روزِ قیامت اللہ تعالیٰ کے ہاں اپنے کفر اور بد عملی کا کوئی عذر پیش نہ کر سکیں۔', 'د رسولانو د لېږلو یوه موخه دا وه چې مؤمنانو ته د جنت زېری ورکړي او پر کفر ټینګو خلکو ته د دوزخ له عذابه وېره ورکړي، تر څو په دې ډول پر خلکو حجت پوره شي او د قیامت په ورځ د الله تعالی په وړاندې د خپل کفر او بدعملۍ هېڅ عذر وړاندې نه کړای شي.'),
          ('The Christian belief of the Trinity, i.e. three gods (Allah Almighty, Sayyidah Maryam (peace be upon her) and Sayyiduna \'Isa (peace be upon him)), is wrong. Allah Almighty is One; He has no need of any son. He alone is the Owner of everything of the heavens and the earth.', 'نصاریٰ کا عقیدۂ تثلیث یعنی تین خدا (اللہ تعالیٰ، سیدہ مریم علیہا السلام اور سیدنا عیسیٰ علیہ السلام) غلط ہے۔ اللہ تعالیٰ تو یکتا ہے اسے کسی بیٹے کی حاجت نہیں۔ وہ تو آسمانوں اور زمینوں کی ہر شے کا تنِ تنہا مالک ہے۔', 'د نصاراوو د تثلیث عقیده، یعنې درې خدایان (الله تعالی، سیده مریم علیها السلام او سیدنا عیسی علیه السلام)، غلطه ده. الله تعالی یو دی، هېڅ زوی ته اړتیا نه لري؛ هغه یوازې د آسمانونو او ځمکې د هر شي مالک دی.'),
          ('The blessed person of the Noble Prophet (peace and blessings of Allah be upon him) is a proof (burhan) for the believers. His holy person, his noble character, his pure life, his miracles and the revelation of the Qur\'an-e-Hakeem upon him are clear proofs of his Messengership, after seeing which no further proof remains needed for accepting the truth and believing in it.', 'نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی ذاتِ مبارکہ مومنوں کے لیے برہان ہے۔ آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی ذاتِ اقدس، آپ کے اخلاقِ کریمانہ، آپ کی سیرتِ طیبہ، آپ کے معجزات اور آپ پر قرآن حکیم کا نزول آپ کی رسالت کے کھلے دلائل ہیں جن کو دیکھنے کے بعد حق بات قبول کر لینے اور اس پر ایمان لانے کے لیے مزید کسی دلیل کی ضرورت باقی نہیں رہتی۔', 'د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم مبارکه ذات د مؤمنانو لپاره برهان دی. د هغه سپېڅلې ذات، کریمانه اخلاق، پاکه سیرت، معجزې او پر هغه د قرآن حکیم نزول د هغه د رسالت ښکاره دلیلونه دي چې له لیدو وروسته یې د حق خبرې منلو او پرې ایمان راوړلو ته د بل کوم دلیل اړتیا نه پاتې کېږي.')])
    VOC(b, 'mq12-l5-vocab', VOCAB)
    BOOK.save(53, [(5, rec(b, 5, 53, 53))], issues=[{'id': 'mq12-pdf053', 'unit': 5, 'printedPage': 50,
               'description': 'Four-column vocabulary rendered as one two-column table (18 rows).'}])


if __name__ == '__main__':
    p53()
