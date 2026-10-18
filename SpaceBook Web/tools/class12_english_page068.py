"""PDF68 (printed 123–124): 'Technical Education' (end, summary) + Reference & Source; Unit 13 Glossary (accommodate … mainstream)."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
r = Builder()
r.p('The essay ends by urging more practical, market-oriented and computer-based courses, flexible curricula, private-sector participation, closer links between industry and academia, wide public awareness of TVET programmes, better publicity, skill centres at universities, and distance-learning programmes for rural youth and drop-outs. If sound policies are implemented in letter and spirit, vocational and technical education can carry the country towards high employment and sustainable economic growth.',
    'مضمون آخر میں زیادہ عملی، منڈی کے مطابق اور کمپیوٹر پر مبنی کورسز، لچکدار نصاب، نجی شعبے کی شمولیت، صنعت اور تعلیمی اداروں کے درمیان قریبی روابط، ٹی ویٹ پروگراموں کے بارے میں وسیع عوامی آگاہی، بہتر تشہیر، جامعات میں مہارت کے مراکز اور دیہی نوجوانوں اور تعلیم چھوڑنے والوں کے لیے فاصلاتی تعلیم کے پروگراموں پر زور دیتا ہے۔ اگر درست پالیسیوں پر لفظاً و معناً عمل کیا جائے تو پیشہ ورانہ اور فنی تعلیم ملک کو زیادہ روزگار اور پائیدار معاشی ترقی کی طرف لے جا سکتی ہے۔',
    'مقاله په پای کې پر ډېرو عملي، د بازار سره برابرو او کمپیوټري کورسونو، انعطاف‌منونکي نصاب، د خصوصي سکټور ګډون، د صنعت او پوهنتونونو ترمنځ نږدې اړیکو، د TVET پروګرامونو په اړه پراخ عامه پوهاوي، ښه تبلیغ، په پوهنتونونو کې د مهارت مرکزونو او د کلیوالو ځوانانو او پاتې شویو لپاره د لرې زده کړې پروګرامونو ټینګار کوي. که سمې پالیسۍ په لفظ او روح پلي شي، مسلکي او تخنیکي زده کړه کولی شي هېواد لوړ استخدام او دوامداره اقتصادي ودې ته ورسوي.')
r.h('Reference & Source', 'حوالہ اور ماخذ', 'سرچینه')
REF = 'Technical Education — By Frank F. Islam an Entrepreneur, Civic Leader, and Thought Leader based in Washington, DC. Published in Daily Times, December 8th 2018.'
r.p(REF, REF, REF); r.paras[-1]['untranslatedByDesign'] = True
rd = BOOK.record(r, 'eng12-u13-text-c', 'Reading text — summary (3); Reference & Source', 'متن — خلاصہ (3)؛ حوالہ', 'متن — لنډیز (3)؛ سرچینه', 68, [123])
rd['sourceGap'] = 'Modern copyrighted newspaper article (Frank F. Islam, Daily Times, 8 Dec 2018); paragraph-wise summary, not verbatim.'
g = Builder()
g.h('Glossary', 'فرہنگ', 'وییپانګه')
gloss(g, 'eng12-u13-gloss-a', [
    ('accommodate(v)', 'to provide somebody with a room or place to sleep, live or sit', 'کسی کو سونے، رہنے یا بیٹھنے کے لیے کمرہ یا جگہ فراہم کرنا', 'یو چا ته د خوب، اوسېدو یا کېناستو لپاره کوټه یا ځای ورکول'),
    ('adequate (adj.)', 'enough in quantity, or good enough in quality, for a particular purpose or need', 'کسی خاص مقصد یا ضرورت کے لیے مقدار میں کافی یا معیار میں اچھا', 'د یوې ټاکلې موخې یا اړتیا لپاره په اندازه کې کافي یا په کیفیت کې ښه'),
    ('aggravate(v)', 'to make an illness or a bad or unpleasant situation worse', 'کسی بیماری یا بری یا ناخوشگوار صورتِ حال کو بدتر بنانا', 'یوه ناروغي یا بد یا ناخوښ حالت لا بدتر کول'),
    ('alleviate(v)', 'to make something less severe', 'کسی چیز کی شدت کم کرنا', 'د یو شي سختي کمول'),
    ('autonomy(n)', 'the freedom for a country, a region or an organization to govern itself independently', 'کسی ملک، خطے یا ادارے کی خود مختاری سے اپنا انتظام چلانے کی آزادی', 'د یوه هېواد، سیمې یا سازمان د خپلواک ډول د ځان اداره کولو ازادي'),
    ('bulge(v)', 'to be completely full (of something), to stick out from something in a round shape', 'کسی چیز سے پوری طرح بھرا ہونا، کسی چیز سے گول شکل میں ابھرنا', 'له یو شي بشپړ ډک کېدل، له یو شي په ګرده بڼه راوتل'),
    ('capitalize(v)', 'to sell possessions in order to change them into money', 'اپنی املاک کو رقم میں بدلنے کے لیے بیچنا', 'شتمني د پیسو د بدلولو لپاره پلورل'),
    ('cohort(n)', 'a group of people who share a common feature or aspect of behaviour', 'لوگوں کا گروہ جن میں کوئی مشترک خصوصیت یا رویے کا پہلو ہو', 'د خلکو ډله چې ګډه ځانګړنه یا د چلند اړخ لري'),
    ('convergence(n)', 'the process of moving together from different directions and meeting; the point where this happens', 'مختلف سمتوں سے ایک ساتھ آ کر ملنے کا عمل؛ وہ مقام جہاں یہ ہوتا ہے', 'له بېلابېلو لورو د یوځای راتلو او سره مخ کېدو بهیر؛ هغه ټکی چې دا پکې کېږي'),
    ('demographic (adj.)', 'data relating to the population and different groups within it', 'آبادی اور اس کے اندر مختلف گروہوں سے متعلق مواد', 'له نفوس او په هغه کې له بېلابېلو ډلو سره تړلي معلومات'),
    ('dividend(n)', 'an amount of the profits that a company pays to people who own shares in the company', 'منافع کی وہ رقم جو کمپنی اپنے حصص داروں کو ادا کرتی ہے', 'د ګټې هغه اندازه چې شرکت یې خپلو ونډه‌والو ته ورکوي'),
    ('extensively(adv.)', 'in a way that covers a large area', 'اس طرح جو بڑے رقبے کا احاطہ کرے', 'په داسې ډول چې لویه سیمه پوښي'),
    ('grab(n)', 'to take or hold somebody/something with your hand suddenly or roughly', 'کسی کو/کسی چیز کو ہاتھ سے اچانک یا سختی سے پکڑنا', 'یو څوک/یو شی په لاس ناڅاپه یا په زور نیول'),
    ('immense(adj.)', 'extremely large or great', 'بے حد بڑا یا عظیم', 'ډېر لوی یا ستر'),
    ('integration(n)', 'the act or process of combining two or more things so that they work together', 'دو یا زیادہ چیزوں کو اس طرح یکجا کرنے کا عمل کہ وہ مل کر کام کریں', 'د دوو یا ډېرو شیانو د داسې یوځای کولو کړنه یا بهیر چې یوځای کار وکړي'),
    ('laser-beam (n)', 'a narrow, intense beam of light produced by a laser.', 'لیزر سے پیدا ہونے والی روشنی کی تنگ اور تیز شعاع۔', 'د لېزر له خوا تولید شوې د رڼا نرۍ او تېزه وړانګه.'),
    ('mainstream(adj.)', 'the ideas and opinions that are thought to be normal because they are shared by most people; the people whose ideas and opinions are most accepted', 'وہ خیالات اور آراء جو معمول سمجھی جاتی ہیں کیونکہ زیادہ تر لوگ ان میں شریک ہیں؛ وہ لوگ جن کے خیالات اور آراء سب سے زیادہ قبول کی جاتی ہیں', 'هغه نظرونه او رایې چې عادي ګڼل کېږي ځکه ډېری خلک ورسره شریک دي؛ هغه خلک چې نظرونه او رایې یې تر ټولو ډېر منل کېږي'),
])
gl = BOOK.record(g, 'eng12-u13-glossary-a', 'Glossary (1)', 'فرہنگ (1)', 'وییپانګه (1)', 68, [124])

if __name__ == '__main__':
    BOOK.save(68, [(13, rd), (13, gl)])
