"""Urdu XII PDF5 (spread): right = فہرست (حصۂ نظم 1–8، حصۂ غزل 9–16، فرہنگ); left = printed p.1, Lesson 1 author note (مولانا شبلی نعمانی)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
U = '۰۱۲۳۴۵۶۷۸۹'
urn = lambda n: ''.join(U[int(d)] for d in str(n))
c = Builder()
c.h('Contents — Poetry section', 'فہرست — حصۂ نظم', 'فهرست — د نظم برخه')
P = [(1, 'جوابِ شکوہ', 'The Answer to the Complaint (Jawab-e-Shikwa)', 'د شکوې ځواب', 'علامہ اقبالؒ', 'Allama Iqbal', 'علامه اقبال', 187),
     (2, 'بڑھے چلو', 'March On', 'مخ ته ولاړ شئ', 'اخترؔ شیرانی', 'Akhtar Sheerani', 'اختر شیراني', 194),
     (3, 'مناظرِ سحر', 'Scenes of Dawn', 'د سهار منظرې', 'جوشؔ ملیح آبادی', 'Josh Malihabadi', 'جوش ملیح ابادي', 198),
     (4, 'شکست کی آواز', 'The Sound of Defeat', 'د ماتې غږ', 'میراجیؔ', 'Meeraji', 'میراجي', 203),
     (5, 'ستارے', 'Stars', 'ستوري', 'ن۔م۔ راشدؔ', 'N. M. Rashid', 'ن م راشد', 207),
     (6, 'نفیرِ عمل', 'The Trumpet of Action', 'د عمل شپېلۍ', 'مجید امجدؔ', 'Majeed Amjad', 'مجید امجد', 211),
     (7, 'ہمیشہ دیر کر دیتا ہوں', 'I Am Always Late', 'زه تل ځنډ کوم', 'منیرؔ نیازی', 'Munir Niazi', 'منیر نیازي', 215),
     (8, 'بڑے ڈرپوک ہو', 'You Are Such a Coward', 'ډېر ډارن یې', 'وزیرؔ آغا', 'Wazir Agha', 'وزیر اغا', 218)]
H = (['No.', 'Title', 'Poet', 'Page'], ['شمار', 'عنوان', 'شاعر', 'صفحہ'], ['شمېره', 'سرلیک', 'شاعر', 'مخ'])
def tab(tid, rows):
    c.table(tid, H[0], [[str(n), e, ae, str(p)] for n, u, e, ps, au, ae, aps, p in rows], H[1], H[2],
            [[urn(n) + '۔', u, au, urn(p)] for n, u, e, ps, au, ae, aps, p in rows], [[str(n), ps, aps, str(p)] for n, u, e, ps, au, ae, aps, p in rows])
tab('urdu12-contents-poems', P)
c.h('Contents — Ghazal section', 'فہرست — حصۂ غزل', 'فهرست — د غزل برخه')
G = [(9, 'جنھیں میں ڈھونڈتا تھا آسمانوں میں زمینوں میں', 'Those I sought in the heavens and on the earths', 'هغه چې ما په اسمانونو او ځمکو کې لټول', 'علامہ اقبالؒ', 'Allama Iqbal', 'علامه اقبال', 222),
     (10, 'کب یاد میں تیرا ساتھ نہیں، کب ہات میں تیرا ہات نہیں', 'When is your company not in my memory, when is your hand not in my hand', 'کله ستا ملګرتیا زما په یاد کې نه ده، کله ستا لاس زما په لاس کې نه دی', 'فیض احمد فیضؔ', 'Faiz Ahmad Faiz', 'فیض احمد فیض', 225),
     (11, 'کون کہتا ہے کہ موت آئی تو مر جاؤں گا', 'Who says that when death comes I shall die', 'څوک وايي چې کله مرګ راشي زه به مړ شم', 'احمد ندیم قاسمی', 'Ahmad Nadeem Qasmi', 'احمد ندیم قاسمي', 228),
     (12, 'سفرِ منزلِ شب یاد نہیں', 'I do not remember the journey to the night’s destination', 'د شپې د منزل سفر مې په یاد نه دی', 'ناصرؔ کاظمی', 'Nasir Kazmi', 'ناصر کاظمي', 230),
     (13, 'آ کے پتھر تو مرے صحن میں دو چار گرے', 'Two or four stones did come and fall into my courtyard', 'دوه څلور ډبرې خو زما انګړ ته راغلې او ولوېدې', 'شکیبؔ جلالی', 'Shakeeb Jalali', 'شکیب جلالي', 232),
     (14, 'لب کشا لوگ ہیں، سرکار کو کیا بولنا ہے', 'The people are speaking out; what has the government to say', 'خلک خوله پرانیزي، سرکار ته څه ویل دي', 'احمد فرازؔ', 'Ahmad Faraz', 'احمد فراز', 235),
     (15, 'مل کے بیٹھے نہیں، خوابوں میں شراکت نہیں کی', 'We did not sit together, did not share our dreams', 'یوځای کېنا نه ستو، په خوبونو کې مو شراکت ونه کړ', 'ظفرؔ اقبال', 'Zafar Iqbal', 'ظفر اقبال', 238),
     (16, 'نہ سہی کچھ مگر اتنا تو کیا کرتے تھے', 'If nothing else, this much at least we used to do', 'که بل څه نه، دومره خو به مو کول', 'شہزادؔ احمد', 'Shahzad Ahmad', 'شهزاد احمد', 242)]
tab('urdu12-contents-ghazals', G)
c.p('Glossary (Farhang) — page 246', 'فرہنگ — ۲۴۶', 'وییپانګه (فرهنګ) — ۲۴۶ مخ')
con = BOOK.record(c, 'urdu12-fm-contents-2', 'Contents — poems, ghazals, glossary', 'فہرست — حصۂ نظم، حصۂ غزل، فرہنگ', 'فهرست — نظم، غزل، وییپانګه', 5, [None])

b = Builder()
b.h('Maulana Shibli Nomani', 'مولانا شبلی نعمانی', 'مولانا شبلي نعماني')
b.p('Born: 1857 · Died: 1914', 'ولادت: ۱۸۵۷ء · وفات: ۱۹۱۴ء', 'زېږېدنه: ۱۸۵۷ز · مړینه: ۱۹۱۴ز')
b.p("Maulana Shibli Nomani was born in Bandol, a village of Azamgarh. His father's name was Shaikh Habibullah. After receiving his early education at Azamgarh he went to Ghazipur to study Arabic and Persian literature and became a pupil of Maulvi Muhammad Farooq. He travelled to distant places in pursuit of learning. After completing his education he began practising law and for some time worked as an Amin of the civil court, but he soon lost interest. After meeting Sir Syed he was appointed a professor at Aligarh College. Shibli Nomani also travelled to various countries. After leaving Aligarh College he founded Dar-ul-Musannifin. This institution was distinguished for Islam and Islamic studies.",
    'مولانا شبلی نعمانی اعظم گڑھ کے ایک گاؤں بندول میں پیدا ہوئے۔ والد کا نام شیخ حبیب اللہ تھا۔ ابتدائی تعلیم اعظم گڑھ سے حاصل کرنے کے بعد عربی و فارسی ادب کی تحصیل کے لیے غازی پور جا کر مولوی محمد فاروق کے شاگرد ہو گئے۔ اُنھوں نے حصولِ تعلیم کے لیے دُور دراز کے سفر کیے۔ تعلیم کی تکمیل کے بعد اُنھوں نے وکالت شروع کی اور کچھ عرصہ امین دیوانی کی حیثیت سے کام کیا، لیکن جلد ہی طبیعت اُچاٹ ہو گئی۔ سرسید سے ملاقات کے بعد وہ علی گڑھ کالج میں پروفیسر مقرر ہو گئے۔ شبلی نعمانی نے مختلف ممالک کے سفر بھی کیے۔ علی گڑھ کالج سے علیحدگی کے بعد اُنھوں نے دارالمصنفین کی بنیاد رکھی۔ یہ ادارہ اسلام اور اسلامیات کے لیے ممتاز تھا۔',
    'مولانا شبلي نعماني د اعظم ګړه په بندول کلي کې زېږېدلی. د پلار نوم یې شیخ حبیب الله و. له اعظم ګړه څخه یې لومړنۍ زده کړې وکړې، بیا د عربي او فارسي ادب د زده کړې لپاره غازي پور ته لاړ او د مولوي محمد فاروق شاګرد شو. د زده کړې لپاره یې لرې لرې سفرونه وکړل. د زده کړې له بشپړېدو وروسته یې وکالت پیل کړ او یو څه موده یې د مدني محکمې د امین په توګه کار وکړ، خو ژر یې زړه ترې ماړه شو. له سرسید سره له لیدنې وروسته د علي ګړه کالج پروفیسر وټاکل شو. شبلي نعماني بېلابېلو هېوادونو ته سفرونه هم وکړل. له علي ګړه کالج څخه له جلا کېدو وروسته یې د دارالمصنفین بنسټ کېښود. دا اداره د اسلام او اسلامي علومو لپاره ممتازه وه.')
b.p('Shibli Nomani was a genius of his age. He was at once a poet, historian, biographer, prose stylist, thinker and reformer. He was associated with the school of Sir Syed, but his style and manner of expression are unique. He makes fine use of similes and metaphors in his writing. His prose is concise and spirited; his writing has fluency and charm. He proves his point with logical reasoning and rational arguments. He also has the honour of being the first historian of Urdu. His historiography is based on research and authority. His greatest achievement is “Seerat-un-Nabi ﷺ”, although he could not complete this work in his lifetime, and after his death his gifted pupil Syed Sulaiman Nadvi completed it.',
    'شبلی نعمانی ایک نابغۂ روزگار ہستی تھے۔ وہ بیک وقت شاعر، مؤرخ، سوانح نگار، انشا پرداز، مفکّر اور مصلح تھے۔ وہ سرسید کے دبستان سے وابستہ تھے لیکن اُن کا اسلوب اور طرزِ بیان منفرد ہے۔ وہ اپنی تحریر میں تشبیہات اور استعارات کا بخوبی استعمال کرتے ہیں۔ اُن کی عبارت مختصر اور پُرجوش ہے۔ تحریر میں روانی اور دلکشی ہے۔ وہ اپنی بات کو منطقی استدلال اور عقلی دلائل سے ثابت کرتے ہیں۔ اُن کو اُردو کا پہلا مؤرخ ہونے کا اعزاز بھی حاصل ہے۔ اُن کی تاریخ نگاری کی بنیاد تحقیق اور سند پر ہے۔ اُن کا سب سے بڑا کارنامہ ’’سیرت النبی ﷺ‘‘ ہے۔ اگرچہ وہ اس تصنیف کو اپنی زندگی میں مکمل نہ کر سکے اور اُن کی وفات کے بعد اُن کے ہونہار شاگرد سید سلیمان ندوی نے اس کی تکمیل کی۔',
    'شبلي نعماني د خپل وخت نابغه شخصیت و. هغه په یو وخت کې شاعر، مورخ، ژوندلیک لیکونکی، انشاپرداز، مفکر او اصلاح‌غوښتونکی و. د سرسید له مکتب سره تړلی و خو سبک او د بیان طرز یې ځانګړی دی. په خپله لیکنه کې تشبیهات او استعارې په ښه توګه کاروي. عبارت یې لنډ او له جوش ډک دی؛ لیکنه یې روانه او زړه‌راښکونکې ده. خپله خبره په منطقي استدلال او عقلي دلیلونو ثابتوي. د اردو د لومړي مورخ ویاړ هم ورته حاصل دی. د هغه تاریخ‌لیکنه پر څېړنه او سند ولاړه ده. تر ټولو لویه کارنامه یې "سیرت النبي ﷺ" ده. که څه هم دا اثر یې په خپل ژوند کې بشپړ نه کړای شو او له مړینې وروسته یې د هغه هوښیار شاګرد سید سلیمان ندوي بشپړ کړ.')
b.p('Works: Seerat-un-Nabi ﷺ, Al-Farooq, Al-Mamoon, Al-Ghazali, Seerat-un-Nauman, Shir-ul-Ajam, etc.', 'تصانیف: سیرت النبی ﷺ، الفاروقؓ، المامون، الغزالی، سیرت النعمانؒ، شعرالعجم وغیرہ', 'تصنیفات: سیرت النبي ﷺ، الفاروق، المامون، الغزالي، سیرت النعمان، شعرالعجم او نور')
UT = ('The Ancient Educational System of the Muslims', 'مسلمانوں کا قدیم طرزِ تعلیم', 'د مسلمانانو د زده کړې زوړ طرز', 'مولانا شبلی نعمانی')
bio = BOOK.record(b, 'urdu12-u1-author', 'About the author: Maulana Shibli Nomani', 'مولانا شبلی نعمانی (تعارف)', 'مولانا شبلي نعماني (پېژندنه)', 5, [1], unit_title=UT)
bio['sourceCoverIllustrationReview'] = 'Portrait of Shibli Nomani and decorative border are not reproduced.'
issues = [{'id': 'urdu12-pdf005', 'unit': 'FM', 'printedPage': None, 'description': 'Contents (poetry/ghazal) on the right half; the poem list numbers 1–8 and the ghazals continue 9–16. In the app, lessons are numbered 1–17 (prose), 18–25 (poems), 26–33 (ghazals) and 34 (glossary). The glossary page number is faint (۲۴۶).'}]

if __name__ == '__main__':
    BOOK.save(5, [('FM', con), (1, bio)], issues=issues, complete_units=["FM"])
