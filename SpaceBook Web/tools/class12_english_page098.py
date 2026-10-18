"""PDF98 (printed 183–184): Unit 18 'Reported speech Exercise: Future Tense' 21–30 (unit end); Unit 19 'Lord of the Flies' (William Golding, abridged) outcomes."""
from class12_book_common import Book, Builder

BOOK = Book('english')
v = Builder()
D = ['21. She said, "I will perform better in next competition"', '22. He said to his teacher, "I will bring good results in exams"', '23. She said to mother, "I will bring good name to you"', '24. Alex said to Mark, "I will be waiting for you at the main gate"', '25. I said to him, "I will have to convince my parents for this"',
     '26. They said, "we will have to stay more active"', '27. She said, "I will be looking for your response"', '28. He said to me, "I will have to think twice before taking such action"', '29. I said to him, "You will have wait for me for two hours"', '30. She said, "We will be signing an agreement on next Sunday"']
R = [[d, ''] for d in D]
v.table('eng12-u18-reported-3', ['Direct Speech', 'Indirect Speech'], R, ['براہِ راست کلام', 'بالواسطہ کلام'], ['مستقیمه وینا', 'غیرمستقیمه وینا'],
        caption='Reported speech Exercise: Future Tense', captionUrdu='بالواسطہ کلام کی مشق: زمانۂ مستقبل', captionPashto='د غیرمستقیمې وینا تمرین: راتلونکی زمان')
a = BOOK.record(v, 'eng12-u18-vocab-c', 'Reported speech — future tense table', 'بالواسطہ کلام — زمانۂ مستقبل کا جدول', 'غیرمستقیمه وینا — د راتلونکي زمان جدول', 98, [183])

UT = ('Lord of the Flies', 'لارڈ آف دی فلائیز', 'لارډ آف دي فلایز')
o = Builder()
o.h('Unit 19 — Lord of the Flies (William Golding)', 'یونٹ 19 — لارڈ آف دی فلائیز (ولیم گولڈنگ)', 'واحد 19 — لارډ آف دي فلایز (ویلیم ګولډینګ)')
o.p('[Abridged] (with some adaptations to make it palatable to the taste of students and to make it agreeable to their social and cultural sensibilities).', '[مختصر شدہ] (کچھ ترامیم کے ساتھ تاکہ یہ طلبہ کے ذوق کے مطابق ہو اور ان کی سماجی و ثقافتی حساسیت سے ہم آہنگ ہو)۔', '[لنډ شوی] (د ځینو بدلونونو سره ترڅو د زده کوونکو له ذوق سره سم وي او د هغوی له ټولنیزو او کلتوري حساسیتونو سره برابر وي).')
o.p('By the end of the unit, the students will be able to:', 'اس یونٹ کے اختتام تک طلبہ اس قابل ہوں گے کہ:', 'د دې واحد په پای کې به زده کوونکي وکولای شي چې:')
o.group('list', [
    ('Read a text to make connections between characters, events, motives and causes of conflicts in texts across cultures.', 'متن پڑھ کر مختلف ثقافتوں کے متون میں کرداروں، واقعات، محرکات اور تنازعات کے اسباب کے درمیان ربط قائم کریں۔', 'متن ولولي ترڅو د بېلابېلو کلتورونو په متنونو کې د کرکټرونو، پېښو، انګېزو او د شخړو د لاملونو ترمنځ اړیکې جوړې کړي.'),
    ('Analyze story elements: characters, events, setting, plot, theme, tone, point of view.', 'کہانی کے عناصر کا تجزیہ کریں: کردار، واقعات، ماحول، پلاٹ، موضوع، لہجہ، نقطۂ نظر۔', 'د کیسې عناصر تحلیل کړي: کرکټرونه، پېښې، چاپېریال، پلاټ، موضوع، لهجه، لیدلوری.'),
    ("Recognize the author's purpose and point of view and their effects on the text.", 'مصنف کے مقصد اور نقطۂ نظر اور متن پر ان کے اثرات کو پہچانیں۔', 'د لیکوال موخه او لیدلوری او په متن یې اغېزې وپېژني.'),
    ('Analyze the conflict in a story or literary selection. Explore options to resolve the conflict. Propose another resolution.', 'کسی کہانی یا ادبی انتخاب میں تنازع کا تجزیہ کریں۔ تنازع حل کرنے کے امکانات تلاش کریں۔ کوئی دوسرا حل تجویز کریں۔', 'په یوه کیسه یا ادبي ټاکنه کې شخړه تحلیل کړي. د شخړې د حل لارې وسپړي. بل حل وړاندیز کړي.'),
    ('Identify universal themes present in literature across all cultures.', 'تمام ثقافتوں کے ادب میں موجود آفاقی موضوعات کی نشاندہی کریں۔', 'په ټولو کلتورونو کې په ادب کې شته نړیوالې موضوعګانې وپېژني.'),
    ("Demonstrate heightened awareness of conventions and dynamic of group discussion and interaction to: present and explain ones point of view clearly; support or modify one's opinion with reasons; acknowledge other's contribution; share information and ideas; clarify, rephrase, explain expand and restate information and ideas.", 'گروہی بحث اور تعامل کے آداب اور حرکیات کا بڑھا ہوا شعور ظاہر کریں تاکہ: اپنا نقطۂ نظر واضح طور پر پیش اور بیان کریں؛ دلائل کے ساتھ اپنی رائے کی تائید یا ترمیم کریں؛ دوسروں کے حصے کا اعتراف کریں؛ معلومات اور خیالات کا تبادلہ کریں؛ معلومات اور خیالات کی وضاحت، نئے الفاظ میں بیان، تشریح، توسیع اور دوبارہ بیان کریں۔', 'د ډله‌ییز بحث او تعامل د دودونو او خوځښت لوړ پوهاوی وښيي ترڅو: خپل لیدلوری په روښانه ډول وړاندې او تشریح کړي؛ د دلیلونو سره خپل نظر ملاتړ یا بدل کړي؛ د نورو ونډه ومني؛ معلومات او نظرونه شریک کړي؛ معلومات او نظرونه روښانه، بیا وویل، تشریح، پراخ او بیا بیان کړي.'),
    ('Illustrate appropriate vocabulary and spelling in their own writing.', 'اپنی تحریر میں موزوں ذخیرۂ الفاظ اور املا کا مظاہرہ کریں۔', 'په خپله لیکنه کې مناسبې لغات او املا وښيي.'),
    ('Use direct and indirect speech appropriately in speech and writing according to the required communicative function.', 'مطلوبہ ابلاغی مقصد کے مطابق گفتگو اور تحریر میں براہِ راست اور بالواسطہ کلام کو موزوں طور پر استعمال کریں۔', 'د اړین اړیکه‌ییز موخې سره سم په خبرو او لیکنه کې مستقیمه او غیرمستقیمه وینا په مناسب ډول وکاروي.'),
])
op = BOOK.record(o, 'eng12-u19-outcomes', 'Unit 19 — learning outcomes', 'یونٹ 19 — تعلیمی نتائج', 'واحد 19 — د زده کړې پایلې', 98, [184], unit_title=UT)
issues = [{'id': 'eng12-p183-184', 'unit': 18, 'printedPage': 183, 'description': 'Printed text retained: “You will have wait for me” (item 29), “on next Sunday”, “ones point of view”, “explain expand”.'}]

if __name__ == '__main__':
    BOOK.save(98, [(18, a), (19, op)], issues=issues, complete_units=[18])
