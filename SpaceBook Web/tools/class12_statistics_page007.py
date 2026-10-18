"""PDF7 printed 5–6: Example 1.4 solution, rules of addition/multiplication, 1.2 introduction to probability,
random experiment, sample space (coin, die, deck-of-cards tree), outcome, event, impossible and simple events."""
from class12_statistics_common import Builder, save
import html

SOL = ('Solution:', 'حل:', 'حل:')


def deck_svg(lang):
    L = {'en': dict(cards='cards', red='Red cards', black='Black cards', s=['Suit-1 Diamond cards', 'Suit-2 Heart cards', 'Suit-3 spade cards', 'Suit-4 Club cards'],
                    ace='Ace', jack='Jack', queen='Queen', king='King', face='(12 picture or face cards)'),
         'ur': dict(cards='پتے', red='سرخ پتے', black='سیاہ پتے', s=['سوٹ-1 اینٹ (ڈائمنڈ)', 'سوٹ-2 پان (ہارٹ)', 'سوٹ-3 حکم (سپیڈ)', 'سوٹ-4 چڑیا (کلب)'],
                    ace='اِکا', jack='غلام', queen='بیگم', king='بادشاہ', face='(12 تصویری پتے)'),
         'ps': dict(cards='پاڼې', red='سرې پاڼې', black='تورې پاڼې', s=['سوټ-1 ډایمنډ', 'سوټ-2 هارټ', 'سوټ-3 سپېډ', 'سوټ-4 کلب'],
                    ace='یکه', jack='غلام', queen='بي‌بي', king='باچا', face='(12 انځوریزې پاڼې)')}[lang]
    e = html.escape
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 470" role="img" aria-label="Deck of 52 playing cards as a tree">',
         '<rect width="620" height="470" rx="6" fill="#dbeafe"/><g font-family="Times New Roman,serif" font-size="15" fill="#111" text-anchor="middle">']

    def box(x, y, v):
        s.append(f'<rect x="{x-14}" y="{y-16}" width="28" height="22" fill="#fff" stroke="#111"/><text x="{x}" y="{y}">{v}</text>')
    box(296, 32, '52'); s.append(f'<text x="345" y="32">{e(L["cards"])}</text>')
    s.append('<path d="M296 40L170 86M296 40L430 86M170 98L110 140M170 98L245 140M430 98L370 140M430 98L505 140" stroke="#111" fill="none"/>')
    box(170, 92, '26'); box(430, 92, '26')
    s.append(f'<text x="118" y="88" font-size="13">{e(L["red"])}</text><text x="490" y="88" font-size="13">{e(L["black"])}</text>')
    cols = [110, 245, 370, 505]
    for i, x in enumerate(cols):
        box(x, 150, '13')
        words = L['s'][i].split(' ', 1)
        s.append(f'<text x="{x}" y="176" font-size="11">{e(words[0])}</text><text x="{x}" y="190" font-size="11">{e(words[1])}</text>')
        for j, v in enumerate([L['ace'], '2', '3', '·', '·', '·', '10', L['jack'], L['queen'], L['king']]):
            s.append(f'<text x="{x}" y="{214+j*22}">{e(v)}</text>')
    s.append('<path d="M70 352h-6v66h6M545 352h6v66h-6" fill="none" stroke="#111"/>')
    s.append(f'<text x="588" y="398" font-size="12">{e(L["face"])}</text></g></svg>')
    return ''.join(s).replace('<text x="588" y="398" font-size="12">', '<text x="310" y="458" font-size="12">')


b = Builder()
b.h(*SOL)
b.p('Here $n=7$, $r=3$, therefore, the total number of combinations is', 'یہاں $n=7$، $r=3$، لہٰذا انتخابات کی کل تعداد یہ ہے', 'دلته $n=7$، $r=3$، نو د ټاکنو ټول شمېر دا دی')
b.eq(r'{}^{7}_{3}C=\frac{7!}{(7-3)!\,3!}=\frac{7\cdot 6\cdot 5\cdot 4!}{4!\,3\cdot 2\cdot 1}=35')
b.h('Rule of addition', 'جمع کا قاعدہ', 'د جمع قاعده')
b.p('If there are two mutually exclusive operations having $m$ and $n$ results respectively, then the two operations combined have $(m+n)$ results.',
    'اگر دو باہم مانع عمل ہوں جن کے بالترتیب $m$ اور $n$ نتائج ہوں، تو دونوں عمل مل کر $(m+n)$ نتائج رکھتے ہیں۔',
    'که دوه یو بل منع کوونکي عملیات وي چې په ترتیب سره $m$ او $n$ پایلې ولري، نو دواړه عملیات یوځای $(m+n)$ پایلې لري.')
b.h('Rule of multiplication', 'ضرب کا قاعدہ', 'د ضرب قاعده')
b.p('If an experiment has $m$ results and another independent experiment has $n$ results, then the compound experiment has exactly $(mn)$ results.',
    'اگر ایک تجربے کے $m$ نتائج ہوں اور دوسرے آزاد تجربے کے $n$ نتائج ہوں، تو مرکب تجربے کے ٹھیک $(mn)$ نتائج ہوں گے۔',
    'که یوه تجربه $m$ پایلې ولري او بله خپلواکه تجربه $n$ پایلې ولري، نو مرکبه تجربه دقیقاً $(mn)$ پایلې لري.')
b.h('1.2 Introduction to probability', '1.2 احتمال کا تعارف', '1.2 د احتمال پېژندنه')
b.p('In everyday life, we face two situations either we may be sure about the occurrence of an event or not sure (uncertain). If sure, then there is no need of probability but if not sure, then probability is used, which is defined as “the numerical evaluation of occurrence of an event is called probability”.',
    'روزمرہ زندگی میں ہمیں دو صورتوں کا سامنا ہوتا ہے: یا تو ہمیں کسی واقعہ کے وقوع کا یقین ہوتا ہے یا یقین نہیں ہوتا (غیر یقینی)۔ اگر یقین ہو تو احتمال کی ضرورت نہیں، لیکن اگر یقین نہ ہو تو احتمال استعمال ہوتا ہے، جس کی تعریف یہ ہے: “کسی واقعہ کے وقوع کی عددی قدر پیمائی کو احتمال کہتے ہیں”۔',
    'په ورځني ژوند کې له دوو حالتونو سره مخ کېږو: یا د یوې پېښې د رامنځته کېدو ډاډ لرو یا یې نه لرو (ناڅرګندتیا). که ډاډ وي، نو احتمال ته اړتیا نشته، خو که ډاډ نه وي، نو احتمال کارول کېږي چې داسې تعریف شوی: “د یوې پېښې د رامنځته کېدو شمېریزې ارزونې ته احتمال وایي”.')
b.p('Originally, it was known as “science of gamblers” because its foundation was laid by two French mathematicians Pascal and Fermat in connection with gambling problems but nowadays probability theory has wider applications in almost all areas of learning. It is a base for inferential statistics.',
    'ابتدا میں اسے “جواریوں کی سائنس” کہا جاتا تھا کیونکہ اس کی بنیاد دو فرانسیسی ریاضی دانوں پاسکل اور فرما نے جوئے کے مسائل کے سلسلے میں رکھی تھی، لیکن آج کل نظریۂ احتمال کا اطلاق علم کے تقریباً ہر شعبے میں ہے۔ یہ استنباطی شماریات کی بنیاد ہے۔',
    'په پیل کې دا د “قمار بازانو علم” په نوم پېژندل کېده، ځکه چې بنسټ یې دوو فرانسوي ریاضي پوهانو پاسکال او فرما د قمار د ستونزو په تړاو کېښود، خو نن ورځ د احتمال نظریه د زده کړې په نږدې ټولو برخو کې پراخه کارونه لري. دا د استنتاجي احصایې بنسټ دی.')
b.p('For learning the probability technique, it is necessary to understand the following key terms.',
    'احتمال کی تکنیک سیکھنے کے لیے درج ذیل بنیادی اصطلاحات کو سمجھنا ضروری ہے۔',
    'د احتمال د تخنیک د زده کړې لپاره د لاندې کلیدي اصطلاحګانو پوهېدل اړین دي.')
b.h('1.2.1 Random experiment', '1.2.1 تصادفی تجربہ', '1.2.1 تصادفي تجربه')
b.p('The dictionary meaning of random is “unexpected” or “unpredictable”, chosen by chance rather than according to a plan.',
    'لفظ random کے لغوی معنی “غیر متوقع” یا “ناقابلِ پیش گوئی” ہیں، یعنی کسی منصوبے کے بجائے اتفاق سے چنا گیا۔',
    'د random کلمې قاموسي مانا “ناڅاپي” یا “نه وړاندوینه کېدونکی” ده، یعنې د پلان پر ځای په تصادف ټاکل شوی.')
b.p('An experiment whose results cannot be predicted in advance is called random experiment. For example; toss of a coin, roll of a die, etc.',
    'ایسا تجربہ جس کے نتائج کی پہلے سے پیش گوئی نہ کی جا سکے، تصادفی تجربہ کہلاتا ہے۔ مثلاً سکہ اچھالنا، پانسہ پھینکنا وغیرہ۔',
    'هغه تجربه چې پایلې یې مخکې له مخکې وړاندوینه نه شي کېدای، تصادفي تجربه بلل کېږي. د بېلګې په توګه د سکې اچول، د ډایس اچول او نور.')
b.h('1.2.2 Sample space', '1.2.2 نمونہ فضا', '1.2.2 نمونوي فضا')
b.p('The collection of all possible results of a random experiment is called sample space and is denoted by S.',
    'کسی تصادفی تجربے کے تمام ممکنہ نتائج کے مجموعے کو نمونہ فضا کہتے ہیں اور اسے S سے ظاہر کرتے ہیں۔',
    'د یوې تصادفي تجربې د ټولو شونو پایلو ټولګې ته نمونوي فضا وایي او په S ښودل کېږي.')
b.p('The sample space for tossing a coin is $S=\\{H,T\\}$.', 'سکہ اچھالنے کی نمونہ فضا $S=\\{H,T\\}$ ہے۔', 'د سکې د اچولو نمونوي فضا $S=\\{H,T\\}$ ده.')
b.p('The sample space for rolling a die is $S=\\{1,2,3,4,5,6\\}$.', 'پانسہ پھینکنے کی نمونہ فضا $S=\\{1,2,3,4,5,6\\}$ ہے۔', 'د ډایس د اچولو نمونوي فضا $S=\\{1,2,3,4,5,6\\}$ ده.')
b.p('The sample space for an ordinary deck of playing cards is', 'تاش کے ایک عام ڈیک کی نمونہ فضا یہ ہے', 'د لوبې د کارتونو د یوې عادي ګډۍ نمونوي فضا دا ده')
b.visual('stat12-deck-tree', deck_svg('en'), deck_svg('ur'), deck_svg('ps'), ratio=.8)
b.h('Definition of outcome', 'نتیجے (outcome) کی تعریف', 'د پایلې (outcome) تعریف')
b.p('Each result of the sample space is called an outcome or sample point.', 'نمونہ فضا کے ہر نتیجے کو outcome یا نمونہ نقطہ کہتے ہیں۔', 'د نمونوي فضا هرې پایلې ته outcome یا نمونوي ټکی وایي.')
b.h('1.2.3 Event', '1.2.3 واقعہ', '1.2.3 پېښه')
b.p('The collection of favourable outcomes to a happening from the sample space is called an event or a subset of the sample space is called an event. It is denoted by $E_1, E_2, E_3\\ldots$ or A, B, C,…',
    'نمونہ فضا میں سے کسی واقعے کے موافق نتائج کے مجموعے کو واقعہ کہتے ہیں، یا نمونہ فضا کے کسی ذیلی سیٹ کو واقعہ کہتے ہیں۔ اسے $E_1, E_2, E_3\\ldots$ یا A، B، C،… سے ظاہر کرتے ہیں۔',
    'له نمونوي فضا څخه د یوې پېښې د موافقو پایلو ټولګې ته پېښه وایي، یا د نمونوي فضا هرې فرعي ټولګې ته پېښه وایي. په $E_1, E_2, E_3\\ldots$ یا A، B، C،… ښودل کېږي.')
b.h('Impossible event', 'ناممکن واقعہ', 'ناشونې پېښه')
b.p('An event which has no favourable outcome is called an impossible or null event and is denoted by $\\phi$. For example, A = observing “7” when a die is rolled once. Surely “A” is impossible event because the number 7 cannot happen when an ordinary die is rolled once.',
    'وہ واقعہ جس کا کوئی موافق نتیجہ نہ ہو، ناممکن یا خالی واقعہ کہلاتا ہے اور اسے $\\phi$ سے ظاہر کرتے ہیں۔ مثلاً A = پانسہ ایک بار پھینکنے پر “7” آنا۔ یقیناً “A” ناممکن واقعہ ہے کیونکہ عام پانسہ ایک بار پھینکنے پر 7 نہیں آ سکتا۔',
    'هغه پېښه چې هېڅ موافقه پایله ونه لري، ناشونې یا تشه پېښه بلل کېږي او په $\\phi$ ښودل کېږي. د بېلګې په توګه A = د ډایس په یو ځل اچولو کې د “7” لیدل. یقیناً “A” ناشونې پېښه ده ځکه چې د عادي ډایس په یو ځل اچولو کې 7 نه شي راتلای.')
b.h('Simple event', 'سادہ واقعہ', 'ساده پېښه')
b.p('An event having exactly one sample point is called simple or elementary event. For example, event $A=\\{5\\}$ when a die is rolled, is a simple event.',
    'وہ واقعہ جس میں ٹھیک ایک نمونہ نقطہ ہو، سادہ یا ابتدائی واقعہ کہلاتا ہے۔ مثلاً پانسہ پھینکنے پر واقعہ $A=\\{5\\}$ ایک سادہ واقعہ ہے۔',
    'هغه پېښه چې دقیقاً یو نمونوي ټکی ولري، ساده یا لومړنۍ پېښه بلل کېږي. د بېلګې په توګه د ډایس په اچولو کې پېښه $A=\\{5\\}$ ساده پېښه ده.')
rec = b.build('stat12-p007-probability-terms', '1.2 Introduction to probability — key terms', '1.2 احتمال کا تعارف — بنیادی اصطلاحات', '1.2 د احتمال پېژندنه — کلیدي اصطلاحګانې', 7, [5, 6])

if __name__ == '__main__':
    save(7, [(1, rec)])
