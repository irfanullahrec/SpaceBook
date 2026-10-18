"""PDF80 (printed 147–148): future perfect (examples, deadline note, activities); D Future Perfect Continuous Tense (definition, timeline figure, identity/form, examples, learning activity)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
v = Builder()
EX = ['I will have had my lunch by 1 p.m.', 'I will have finished when you arrive.']
v.group('list', [(x,) * 3 for x in EX])
for p in v.paras[-2:]: p['untranslatedByDesign'] = True
v.p("It is important to remember that in future perfect tense, the action you are talking about, must have a deadline. If you don't mention a deadline then it is better to use the simple future tense instead of the future perfect tense.",
    'یہ یاد رکھنا ضروری ہے کہ مستقبل مکمل میں جس کام کی آپ بات کر رہے ہیں اس کی ایک آخری حد (وقت) ہونی چاہیے۔ اگر آپ آخری حد ذکر نہ کریں تو مستقبل مکمل کے بجائے سادہ مستقبل استعمال کرنا بہتر ہے۔',
    'دا په یاد ساتل مهم دي چې په راتلونکي بشپړ زمان کې، هغه کار چې تاسو یې په اړه خبرې کوئ باید یوه وروستۍ نېټه ولري. که وروستۍ نېټه یاده نه کړئ، نو د راتلونکي بشپړ پر ځای د ساده راتلونکي زمان کارول غوره دي.')
v.p('For example,', 'مثلاً،', 'د بېلګې په توګه،')
v.group('list', [('"Hoorain will leave."(correct) instead of "Hoorain will have left".(incorrect), but', '"Hoorain will leave." (درست) بجائے "Hoorain will have left" کے (غلط)، لیکن', '"Hoorain will leave." (سم) د "Hoorain will have left" پر ځای (ناسم)، خو'),
                 ('Hoorainwillhaveleftbeforeevening.(Correct)', 'Hoorainwillhaveleftbeforeevening. (درست)', 'Hoorainwillhaveleftbeforeevening. (سم)')])
v.h('Activity', 'سرگرمی', 'فعالیت')
v.p('Divide the class into several groups of five students each. Ask them to write five sentences on the topic "what will our country be like in the next 50 years ? What will have happened by then?" They should be advised to use the future perfect in their sentences.',
    'جماعت کو پانچ پانچ طلبہ کے کئی گروہوں میں تقسیم کریں۔ ان سے ’’اگلے 50 برسوں میں ہمارا ملک کیسا ہو گا؟ تب تک کیا ہو چکا ہو گا؟‘‘ کے موضوع پر پانچ جملے لکھوائیں۔ انہیں اپنے جملوں میں مستقبل مکمل استعمال کرنے کا مشورہ دیا جائے۔',
    'ټولګی په پنځه پنځه کسیزو څو ډلو ووېشئ. ترې وغواړئ چې د "زموږ هېواد به په راتلونکو 50 کلونو کې څنګه وي؟ تر هغه وخته به څه شوي وي؟" په موضوع پنځه جملې ولیکي. ورته مشوره ورکړئ چې په خپلو جملو کې راتلونکی بشپړ زمان وکاروي.')
v.p("For example,' people will have got more artificial by then.'", "مثلاً، ' people will have got more artificial by then.'", "د بېلګې په توګه، ' people will have got more artificial by then.'")
v.h('Activity', 'سرگرمی', 'فعالیت')
v.p('Use the correct form of the verbs in the brackets to make it future perfect tense:', 'قوسین میں دیے گئے افعال کی درست شکل استعمال کر کے جملوں کو مستقبل مکمل میں بنائیں:', 'په قوسونو کې د فعلونو سمه بڼه وکاروئ ترڅو جمله راتلونکی بشپړ زمان شي:')
A = [(1, 'Umair____his bike next week. (To repair)'), (2, "They____the washing by by 9 o'clock. ( To do)"), (3, 'He____Malaysia by the end of this year. ( To visit )'), (4, "I____by 9 o'clock.( To finish)"),
     (5, 'The police_ the thief. (To arrest)'), (6, 'She____in the concert tomorrow evening.( To play)'), (7, 'By this time nextyear, Abrar_his University degree. (To take)'), (9, 'When I get home my dog____at the door watching for me. ( To sit)'),
     (10, 'The train____before we reach the station. (To leave)'), (11, 'She____this issue with her father tonight. ( To discuss)')]
v.group('lines', [(f'{n}. {s}',) * 3 for n, s in A])
for p in v.paras[-len(A):]: p['untranslatedByDesign'] = True
v.h('D. Future Perfect Continuous Tense', 'D. مستقبل مکمل جاری', 'D. راتلونکی بشپړ روان زمان')
v.p('Definition: Future Perfect Continuous tense, also known as Future Perfect Progressive tense is used to talk about an action that will have begun in past , present or future and that will continue up for some indefinite time in future.',
    'تعریف: مستقبل مکمل جاری، جسے مستقبل مکمل استمراری بھی کہا جاتا ہے، ایسے کام کے بارے میں بات کرنے کے لیے استعمال ہوتا ہے جو ماضی، حال یا مستقبل میں شروع ہو چکا ہو گا اور مستقبل میں کسی غیر معین وقت تک جاری رہے گا۔',
    'تعریف: راتلونکی بشپړ روان زمان، چې د راتلونکي بشپړ دوامداره زمان په نوم هم پېژندل کېږي، د داسې کار په اړه د خبرو لپاره کارول کېږي چې په تېر، اوسني یا راتلونکي وخت کې به پیل شوی وي او په راتلونکي کې به تر یو نامعلوم وخته دوام ومومي.')
a = BOOK.record(v, 'eng12-u15-vocab-c', 'Future Perfect (2), activities; D Future Perfect Continuous (1)', 'مستقبل مکمل (2)، سرگرمیاں؛ D مستقبل مکمل جاری (1)', 'راتلونکی بشپړ (2)، فعالیتونه؛ D راتلونکی بشپړ روان (1)', 80, [147])

L = {'en': ('Will have been', 'Teaching', '(2016)', 'Started', 'Teaching', '(2020)', 'Now', '(2021)'),
     'ur': ('Will have been', 'Teaching', '(2016)', 'پڑھانا', 'شروع کیا', '(2020)', 'اب', '(2021)'),
     'ps': ('Will have been', 'Teaching', '(2016)', 'تدریس', 'پیل شوه', '(2020)', 'اوس', '(2021)')}


def timeline(lang):
    t = L[lang]
    return ('<svg viewBox="0 0 260 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Timeline 2016–2021" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="currentColor">'
            '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="currentColor"/></marker></defs>'
            f'<text x="150" y="14" text-anchor="middle">{t[0]}</text><text x="150" y="28" text-anchor="middle">{t[1]}</text>'
            '<line x1="160" y1="36" x2="160" y2="56" stroke="currentColor" stroke-width="2"/>'
            '<line x1="160" y1="56" x2="20" y2="56" stroke="currentColor" stroke-width="2" marker-end="url(#ah)"/>'
            '<line x1="20" y1="90" x2="240" y2="90" stroke="currentColor" stroke-width="2" marker-end="url(#ah)"/>'
            '<line x1="20" y1="82" x2="20" y2="98" stroke="currentColor" stroke-width="2"/>'
            '<line x1="125" y1="82" x2="125" y2="98" stroke="currentColor" stroke-width="2"/>'
            '<line x1="160" y1="56" x2="160" y2="98" stroke="currentColor" stroke-width="2"/>'
            f'<text x="20" y="114" text-anchor="middle">{t[2]}</text><text x="20" y="127" text-anchor="middle">{t[3]}</text><text x="20" y="140" text-anchor="middle">{t[4]}</text>'
            f'<text x="122" y="114" text-anchor="middle">{t[5]}</text><text x="122" y="127" text-anchor="middle">{t[6]}</text>'
            f'<text x="166" y="114" text-anchor="middle">{t[7]}</text></svg>')


c = Builder()
c.p('Actually, in Future Perfect Continuous tense, we go in our imagination to a future point and from there, we talk about an ongoing action that for how long it has been continuing with reference to a particular point of time/activity and that particular point/activity might be now or even before now.',
    'دراصل مستقبل مکمل جاری میں ہم تصور میں مستقبل کے کسی مقام پر جاتے ہیں اور وہاں سے کسی جاری کام کے بارے میں بات کرتے ہیں کہ وہ کسی خاص وقت/سرگرمی کے حوالے سے کتنی دیر سے جاری ہے، اور وہ خاص وقت/سرگرمی اب یا اب سے پہلے بھی ہو سکتی ہے۔',
    'په حقیقت کې په راتلونکي بشپړ روان زمان کې، موږ په خپل تصور کې د راتلونکي یوه ټکي ته ځو او له هغه ځایه د یو روان کار په اړه خبرې کوو چې د یو ټاکلي وخت/فعالیت په تړاو څومره موده یې دوام کړی، او هغه ټاکلی وخت/فعالیت کېدای شي اوس یا له اوس مخکې وي.')
c.p('Consider the following timeline:', 'درج ذیل ٹائم لائن پر غور کریں:', 'لاندې مهال‌کرښه په پام کې ونیسئ:')
c.blocks.append({'id': 'eng12-u15-fpc-timeline', 'svg': timeline('en'), 'svgUrdu': timeline('ur'), 'svgPashto': timeline('ps'), 'sourceWidthRatio': .42})
c.layout.append({'type': 'visualParagraph', 'blockId': 'eng12-u15-fpc-timeline', 'indices': [len(c.paras)], 'visualFirst': True})
c.paras.append({'text': 'Suppose you are now in 2020; and let\'s say you started teaching English right this year; you are thinking about the next year 2021(future) ; so you would say, " Next year I will have been teaching English for one year." But if suppose you started the job back in 2016 then thinking about the next year (2021) you would say,',
                'urdu': 'فرض کریں آپ اب 2020 میں ہیں؛ اور مان لیں آپ نے اسی سال انگریزی پڑھانا شروع کیا؛ آپ اگلے سال 2021 (مستقبل) کے بارے میں سوچ رہے ہیں؛ تو آپ کہیں گے: " Next year I will have been teaching English for one year." لیکن اگر فرض کریں آپ نے یہ ملازمت 2016 میں شروع کی تھی تو اگلے سال (2021) کے بارے میں سوچتے ہوئے آپ کہیں گے،',
                'pashto': 'فرض کړئ اوس په 2020 کې یاست؛ او ووایو چې همدا کال مو د انګرېزي تدریس پیل کړ؛ د راتلونکي کال 2021 (راتلونکی) په اړه فکر کوئ؛ نو به ووایئ: " Next year I will have been teaching English for one year." خو که فرض کړو دنده مو په 2016 کې پیل کړې وه، نو د راتلونکي کال (2021) په اړه په فکر کولو به ووایئ،'})
c.p('" Next year I will have been teaching English for five years."', '" Next year I will have been teaching English for five years."', '" Next year I will have been teaching English for five years."'); c.paras[-1]['untranslatedByDesign'] = True
c.p('Here, " will have been teaching" indicates that the action of teaching will be continuing up to the next year (2021) and might go even further.', 'یہاں " will have been teaching" ظاہر کرتا ہے کہ پڑھانے کا عمل اگلے سال (2021) تک جاری رہے گا اور شاید اس سے بھی آگے جائے۔', 'دلته " will have been teaching" ښيي چې د تدریس کار به تر راتلونکي کال (2021) پورې دوام ولري او کېدای شي له هغه هم وړاندې لاړ شي.')
c.p('Unlike Future Perfect tense, the action here has no end date or completion point.', 'مستقبل مکمل کے برعکس، یہاں کام کی کوئی اختتامی تاریخ یا تکمیل کا مقام نہیں۔', 'د راتلونکي بشپړ زمان برعکس، دلته کار د پای نېټه یا د بشپړېدو ټکی نه لري.')
c.h('Identity:', 'شناخت:', 'پېژندنه:')
c.p('To Identify the Future Perfect Continuous tense, it is to remember that this tense has the following form or structure.', 'مستقبل مکمل جاری کو پہچاننے کے لیے یاد رکھیں کہ اس زمانے کی ساخت یہ ہے۔', 'د راتلونکي بشپړ روان زمان د پېژندلو لپاره په یاد ولرئ چې دا زمان لاندې بڼه یا جوړښت لري.')
c.p('Subject + will + have+ been+ present participle of the main verb', 'فاعل + will + have + been + اصل فعل کا حال کا اسمِ فاعل', 'فاعل + will + have + been + د اصلي فعل اوسنی صفت فاعلي')
c.p('Fe example,', 'مثلاً،', 'د بېلګې په توګه،')
EX2 = ['He will have been playing hockey for three years by the next week.', 'They will have been sleeping for two hours when their father gets home.', 'Shama will have been doing her job for two years the next month.', 'They will have been playing football for hours before you reach.', 'I will have been helping him for a few hours at night.']
c.group('list', [(x,) * 3 for x in EX2])
for p in c.paras[-len(EX2):]: p['untranslatedByDesign'] = True
c.h('Learning activity:', 'تعلیمی سرگرمی:', 'د زده کړې فعالیت:')
c.p('Ask your students to imagine themselves 20 years in future from now (2040). Have each one write 5 sentences about what he or she will have been doing at that time; and for how long between now and then.', 'اپنے طلبہ سے کہیں کہ وہ خود کو اب سے 20 سال بعد (2040) میں تصور کریں۔ ہر ایک سے 5 جملے لکھوائیں کہ وہ اس وقت کیا کر رہا/رہی ہو گا اور اب سے تب تک کتنی دیر سے۔', 'خپلو زده کوونکو ته ووایئ چې ځانونه له اوس 20 کاله وروسته (2040) کې تصور کړي. هر یو دې 5 جملې ولیکي چې په هغه وخت کې به څه کوي؛ او له اوس تر هغه وخته به څومره موده.')
c.p('For example, " I will have been working on a good position for 15 years."', 'مثلاً، " I will have been working on a good position for 15 years."', 'د بېلګې په توګه، " I will have been working on a good position for 15 years."')
b = BOOK.record(c, 'eng12-u15-vocab-d', 'Future Perfect Continuous (2): timeline, form, examples', 'مستقبل مکمل جاری (2): ٹائم لائن، ساخت، مثالیں', 'راتلونکی بشپړ روان (2): مهال‌کرښه، جوړښت، بېلګې', 80, [148])
issues = [{'id': 'eng12-p147-148', 'unit': 15, 'printedPage': 147, 'description': 'Printed numbering retained: the future-perfect activity skips item 8 (1–7, 9–11). Also retained: “by by 9 o\'clock”, “Hoorainwillhaveleftbeforeevening”, “nextyear”, “Fe example”, “continue up for”. The timeline figure is redrawn as coded SVG.'}]

if __name__ == '__main__':
    BOOK.save(80, [(15, a), (15, b)], issues=issues)
