"""PDF56 (printed 99–100): argumentative essay (body, conclusion, summary); Activity; Oral; Vocabulary A prefix bank/grid; B first conditional 1–13; C circle the correct words 1–6 (unit end)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
w = Builder()
for x in [
    ('Body paragraphs: Body paragraphs is the area where you provide arguments and provide evidence to prove your point and thus to persuade the readers. The best way here ,is to present one point in one paragraph. At least, three body paragraphs would make a good persuasive essay.', 'متن کے پیراگراف: متن کے پیراگراف وہ حصہ ہیں جہاں آپ اپنا نکتہ ثابت کرنے اور یوں قارئین کو قائل کرنے کے لیے دلائل اور شواہد پیش کرتے ہیں۔ یہاں بہترین طریقہ یہ ہے کہ ایک پیراگراف میں ایک نکتہ پیش کیا جائے۔ کم از کم تین متن کے پیراگراف ایک اچھا ترغیبی مضمون بنائیں گے۔', 'د متن پراګرافونه: د متن پراګرافونه هغه برخه ده چې پکې د خپل ټکي د ثابتولو او په دې توګه د لوستونکو د قانع کولو لپاره دلیلونه او شواهد وړاندې کوئ. دلته تر ټولو غوره لاره دا ده چې په یوه پراګراف کې یو ټکی وړاندې کړئ. لږ تر لږه درې د متن پراګرافونه به یوه ښه هڅوونکې مقاله جوړه کړي.'),
    ('Conclusion: It where you would conclude your essay. Here, you have to summarize and close the essay with an impact. You will try to convince the reader claiming that your argument is the most valid one.', 'اختتامیہ: یہ وہ جگہ ہے جہاں آپ اپنا مضمون ختم کریں گے۔ یہاں آپ کو خلاصہ کرنا ہے اور مضمون کو مؤثر انداز میں ختم کرنا ہے۔ آپ یہ دعویٰ کرتے ہوئے قاری کو قائل کرنے کی کوشش کریں گے کہ آپ کی دلیل سب سے زیادہ درست ہے۔', 'پایله: دا هغه ځای دی چې خپله مقاله پکې پای ته رسوئ. دلته باید لنډیز وکړئ او مقاله په اغېزمن ډول پای ته ورسوئ. هڅه به وکړئ چې لوستونکی قانع کړئ او ادعا وکړئ چې ستاسو دلیل تر ټولو سم دی.'),
    ('To sum up, a good argumentative essay should have:', 'خلاصہ یہ کہ ایک اچھے استدلالی مضمون میں یہ ہونا چاہیے:', 'په لنډه توګه، یوه ښه استدلالي مقاله باید ولري:'),
]: w.p(*x)
w.group('lines', [('1- A clear and solid thesis statement in the introduction.', '1- تعارف میں ایک واضح اور مضبوط مرکزی دعویٰ۔', '1- په پېژندنه کې یو روښانه او ټینګ تیسس بیان.'),
                  ('2- Logical reasoning, examples, evidence,facts and figures etc in support of the thesis statement.', '2- مرکزی دعوے کی تائید میں منطقی استدلال، مثالیں، شواہد، حقائق اور اعداد و شمار وغیرہ۔', '2- د تیسس بیان په ملاتړ منطقي استدلال، بېلګې، شواهد، حقایق او شمېرې او نور.'),
                  ('3- An effective conclusion.', '3- ایک مؤثر اختتامیہ۔', '3- یوه اغېزمنه پایله.')])
w.h('Activity', 'سرگرمی', 'فعالیت')
w.p('Keeping in view the structure of an argumentative essay, write your own opinion on the following topic : " The bread earner has always got a stronger social status"', 'استدلالی مضمون کی ساخت کو مدِ نظر رکھتے ہوئے درج ذیل موضوع پر اپنی رائے لکھیں: ’’کمانے والے کی سماجی حیثیت ہمیشہ زیادہ مضبوط رہی ہے‘‘', 'د استدلالي مقالې جوړښت په پام کې ونیسئ او په لاندې موضوع خپل نظر ولیکئ: "ډوډۍ ګټونکی تل قوي ټولنیز حیثیت لري"')
w.h('Oral Communication', 'زبانی ابلاغ', 'د خولې اړیکه')
w.p('Divide the class into two equal groups. The first group will be asked to speak in favour of women equality and the second group will be asked to speak against it.', 'جماعت کو دو برابر گروہوں میں تقسیم کریں۔ پہلے گروہ سے خواتین کی برابری کے حق میں اور دوسرے سے اس کے خلاف بولنے کو کہا جائے گا۔', 'ټولګی په دوو برابرو ډلو ووېشئ. له لومړۍ ډلې به وغوښتل شي چې د ښځو د برابرۍ په ګټه او له دویمې به چې پر ضد یې خبرې وکړي.')
w.h('Vocabulary and Grammar', 'ذخیرۂ الفاظ اور قواعد', 'لغات او ګرامر')
w.p('A. Use the bank of prefixes to complete each word. There may be more than one answer for some words. Use new words in your sentences.', 'A. ہر لفظ مکمل کرنے کے لیے سابقوں کا ذخیرہ استعمال کریں۔ بعض الفاظ کے ایک سے زیادہ جواب ہو سکتے ہیں۔ نئے الفاظ اپنے جملوں میں استعمال کریں۔', 'A. د هرې کلمې د بشپړولو لپاره د مختاړو زېرمه وکاروئ. د ځینو کلمو لپاره کېدای شي له یوه زیات ځوابونه وي. نوې کلمې په خپلو جملو کې وکاروئ.')
PB = [['de-', 'dis-', 'ex-', 'il-', 'im-', 'in-', 'mis-', 'non-', 'pre-', 're-', 'un-', 'with-']]
H = [''] * 12
w.table('eng12-u10-prefix-bank', H, PB, H, H, PB, PB, noHeader=True)
G = [['__ fix', '__ sense', '__ happy', '__ place', '__ usual', '__ portant'], ['__ mind', '__ pert', '__ respect', '__ draw', '__ logical', '__ trieve'],
     ['__ equal', '__ legal', '__ fiction', '__ visible', '__ play', '__ cellent'], ['__ prove', '__ frost', '__ ceed', '__ view', '__ code', '__ flex'], ['__ lucky', '__ lead', '__ fat', '__ fair', '__ gust', '__ hold']]
H6 = [''] * 6
w.table('eng12-u10-prefix-grid', H6, G, H6, H6, G, G, noHeader=True)
w.p('B. Complete the sentences with the verb in brackets. Use the First Conditional.', 'B. قوسین میں دیے گئے فعل سے جملے مکمل کریں۔ پہلا شرطیہ استعمال کریں۔', 'B. جملې په قوسونو کې د ورکړل شوي فعل سره بشپړې کړئ. لومړی شرطي وکاروئ.')
FC = ['If my aunt comes to visit, she ........ (give) us a present.', "If it doesn't rain, we ........ (go) to the beach.", 'If it ........ (snow) tonight, we will make a snowman tomorrow.', "If you don't try, you ........ (not succeed).",
      'If you ........ (bring) the sandwiches for the picnic, I will bring the drinks.', "If he talks too long, his parents ........ (not let) him use the phone.", 'He will turn on the heater if it ........ (get) too cold.',
      "You won't understand the questions unless you ........ (read) the book.", 'If we ........ (go) to Peshawar, we ........ (visit) my friend Salman.', 'If she ........ (do) well in her exams, my sister ........ (go) to university.',
      'Neelam ........ (not eat) supper if she ........ (eat) all that ice cream.', 'My brother ........ (drive) us to the cinema if we ........ (ask) him.', 'Uncle Ismail ........ (phone) us if he ........ (want) to come with us.']
w.group('lines', [(f'{i}. {s}',) * 3 for i, s in enumerate(FC, 1)])
w.p('C. Circle the correct words.', 'C. درست الفاظ کے گرد دائرہ لگائیں۔', 'C. د سمو کلمو شاوخوا کړۍ وکاږئ.')
CW = ['Arif will water the garden if he comes/will come home.', 'We will buy our tickets if we will have/have enough money.', 'We will be late for the show unless you hurry/will hurry.', 'I will take/take an umbrella if it rains.',
      'If it is/will be a nice day tomorrow, we will go for a bike ride.', "He won't cross the road unless he will see/sees the green light."]
w.group('lines', [(f'{i}. {s}',) * 3 for i, s in enumerate(CW, 1)])
for p in w.paras[-(len(FC) + len(CW) + 1):]:
    if p['text'][0].isdigit(): p['untranslatedByDesign'] = True
rec = BOOK.record(w, 'eng12-u10-writing-vocab', 'Argumentative essay (body, conclusion); Activity; Oral; Vocabulary A–C', 'استدلالی مضمون (متن، اختتامیہ)؛ سرگرمی؛ زبانی ابلاغ؛ ذخیرۂ الفاظ A–C', 'استدلالي مقاله (متن، پایله)؛ فعالیت؛ د خولې اړیکه؛ لغات A–C', 56, [99, 100])
issues = [{'id': 'eng12-p99-100', 'unit': 10, 'printedPage': 99, 'description': 'Printed text retained: “Body paragraphs is the area”, “The best way here ,is”, “It where you would conclude”, “evidence,facts”. Prefix grid and grammar drills are shown in English in all views.'}]

if __name__ == '__main__':
    BOOK.save(56, [(10, rec)], issues=issues, complete_units=[10])
