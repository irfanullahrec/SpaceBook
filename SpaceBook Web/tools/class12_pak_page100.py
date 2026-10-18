"""Pak Studies XII PDF100 (spread): printed pp.189–190 — Ch.10 relations with other countries: 1 Pakistan–China (Khunjerab Pass and JF-17 photos coded as SVG); 2 Pakistan–India."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
P = t.p
H = t.h


def pass_svg(cap):
    """Coded flat illustration standing in for the photograph of the Khunjerab Pass road between snow peaks."""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 300" role="img" aria-label="{cap}">'
            '<rect width="480" height="300" fill="#7fb0d9"/>'
            '<polygon points="0,170 70,80 130,140 200,55 260,120 330,60 400,130 480,90 480,300 0,300" fill="#8a7a74"/>'
            '<polygon points="200,55 225,85 210,82 195,95 180,80" fill="#ffffff"/><polygon points="330,60 355,92 338,88 322,100 310,84" fill="#ffffff"/>'
            '<polygon points="70,80 92,108 76,104 60,112 52,100" fill="#ffffff"/>'
            '<polygon points="0,200 120,150 210,190 300,160 480,210 480,300 0,300" fill="#9c6b4e"/>'
            '<path d="M150 300 C200 240 250 220 300 200" stroke="#4a4a4a" stroke-width="26" fill="none"/>'
            '<path d="M150 300 C200 240 250 220 300 200" stroke="#f2f2f2" stroke-width="2" stroke-dasharray="10 8" fill="none"/>'
            f'<rect x="300" y="262" width="170" height="30" rx="4" fill="#ffffff" opacity="0.85"/><text x="385" y="283" text-anchor="middle" font-size="16" fill="#1d2a38" font-family="sans-serif">{cap}</text></svg>')


def jet_svg(cap):
    """Coded flat illustration standing in for the photograph of a JF-17 Thunder aircraft taking off."""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 280" role="img" aria-label="{cap}">'
            '<rect width="480" height="280" fill="#cfe2ef"/><rect y="220" width="480" height="60" fill="#7aa35c"/>'
            '<path d="M60 170 L330 150 L420 160 L330 172 L60 182 Z" fill="#8c9aa6" stroke="#4d5964" stroke-width="2"/>'
            '<path d="M180 160 L250 105 L275 108 L240 162 Z" fill="#7c8a96" stroke="#4d5964" stroke-width="2"/>'
            '<path d="M180 178 L245 215 L268 212 L238 176 Z" fill="#7c8a96" stroke="#4d5964" stroke-width="2"/>'
            '<path d="M80 168 L95 110 L120 112 L112 166 Z" fill="#7c8a96" stroke="#4d5964" stroke-width="2"/>'
            '<ellipse cx="350" cy="155" rx="28" ry="8" fill="#2f4a5e"/><path d="M60 176 L30 176" stroke="#e8a33a" stroke-width="8"/>'
            '<text x="104" y="150" font-size="13" font-weight="bold" fill="#ffffff" font-family="sans-serif">JF-17</text>'
            '<line x1="300" y1="182" x2="300" y2="205" stroke="#333" stroke-width="3"/><circle cx="300" cy="208" r="5" fill="#222"/>'
            f'<text x="240" y="268" text-anchor="middle" font-size="15" fill="#1d2a38" font-family="sans-serif">{cap}</text></svg>')


H('Relations of Pakistan with other countries', 'پاکستان کے دوسرے ممالک کے ساتھ تعلقات', 'له نورو هېوادونو سره د پاکستان اړیکې')
H('1. Pakistan–China relations', '1۔ پاکستان چین تعلقات', '۱. د پاکستان او چین اړیکې')
P('The relations of Pakistan and China have been friendly from the very beginning. After the communist revolution China had to face considerable diplomatic difficulties at the international level in its early days, but Pakistan always gave China diplomatic support, and Pakistan also played an important role in making China a member of the United Nations.',
  'پاکستان اور چین کے تعلقات ابتداء ہی سے دوستانہ رہے۔ کیمونسٹ انقلاب کے بعد چین کو ابتدائی دنوں میں بین الاقوامی سطح پر کافی سفارتی مشکلات کا سامنا کرنا پڑا لیکن پاکستان نے ہمیشہ چین کی سفارتی تائید کی اور پاکستان نے چین کو اقوامِ متحدہ کا رکن بنانے میں بھی اہم کردار ادا کیا۔',
  'د پاکستان او چین اړیکې له پیله دوستانه وې. له کمونیستي انقلاب وروسته چین په لومړیو ورځو کې په نړیواله کچه له ډېرو ډیپلوماتیکو ستونزو سره مخ شو، خو پاکستان تل د چین ډیپلوماتیک ملاتړ وکړ، او پاکستان چین د ملګرو ملتونو غړی کولو کې هم مهم رول ولوباوه.')
t.visual('pak12-khunjerab', pass_svg('Khunjerab Pass'), pass_svg('خنجراب پاس'), pass_svg('د خنجراب درّه'), 480 / 300)
P('Although in the decade of 1950 a border dispute emerged between Pakistan and China, both countries amicably resolved this dispute through the “Pakistan–China Border Agreement”.',
  'اگرچہ 1950ء کی دہائی میں پاکستان اور چین کے درمیان سرحدی تنازعہ ابھر کر سامنے آیا مگر دونوں ممالک نے خوش اسلوبی کے ساتھ اس تنازعے کو ’’پاکستان چین سرحدی معاہدے‘‘ کے ذریعے حل کر لیا۔',
  'که څه هم د ۱۹۵۰ز په لسیزه کې د پاکستان او چین ترمنځ سرحدي شخړه راپورته شوه، خو دواړو هېوادونو دا شخړه د "پاکستان-چین سرحدي تړون" له لارې په ښه توګه حل کړه.')
t.visual('pak12-jf17', jet_svg('JF-17 Thunder fighter aircraft'), jet_svg('جے ایف 17 تھنڈر لڑاکا طیارہ'), jet_svg('JF-17 تندر جنګي الوتکه'), 480 / 280)
P('China and Pakistan are co-operating with each other in various kinds of defence, agricultural, development and industrial projects. In the defence sector they are also jointly preparing a fighter aircraft (JF-Thunder-17), while with the co-operation of China itself Pakistan’s second big port, Gwadar, has reached completion. To further strengthen these relations, the Prime Minister of China, Wen Jiabao (Wen Jiabao), came on a visit to Pakistan in April 2005. During this visit the two countries signed 22 different kinds of agreements.',
  'چین اور پاکستان مختلف قسم کے دفاعی، زرعی، ترقیاتی اور صنعتی منصوبوں میں ایک دوسرے کے ساتھ تعاون کر رہے ہیں۔ دفاعی شعبے میں مشترکہ لڑاکا ہوائی جہاز (JF-Thunder-17) بھی تیار کر رہے ہیں جب کہ چین ہی کے تعاون سے پاکستان کی دوسری بڑی بندرگاہ گوادر پایہ تکمیل کو پہنچی ہے۔ ان تعلقات کو مزید تقویت دینے کی غرض سے چین کے وزیرِ اعظم وین جیاباؤ (Wen Jiabao) اپریل 2005ء میں پاکستان کے دورے پر آئے۔ اس دورے کے دوران دونوں ممالک نے 22 مختلف قسم کے معاہدوں پر دستخط کیے۔',
  'چین او پاکستان په بېلابېلو دفاعي، کرنیزو، پراختیايي او صنعتي پروژو کې له یو بل سره همکاري کوي. په دفاعي برخه کې ګډه جنګي الوتکه (JF-Thunder-17) هم جوړوي، او د چین په همکارۍ د پاکستان دویم لوی بندر ګوادر بشپړ شوی. د دې اړیکو د لا پیاوړتیا لپاره د چین لومړی وزیر وین جیاباو (Wen Jiabao) د ۲۰۰۵ز په اپرېل کې پاکستان ته راغی. د دې سفر په ترڅ کې دواړو هېوادونو پر ۲۲ بېلابېلو تړونونو لاسلیک وکړ.')
H('2. Relations of Pakistan and India', '2۔ پاکستان اور بھارت کے تعلقات', '۲. د پاکستان او هند اړیکې')
P('From the establishment of Pakistan until today, the relations of Pakistan and India could not be established on pleasant lines. The Kashmir issue is the cause of dispute between the two countries. On it three wars have so far taken place, in 1948, 1965 and 1971. At the time of the establishment of Pakistan, India created many problems for Pakistan.',
  'قیامِ پاکستان سے لے کر آج تک پاکستان اور بھارت کے تعلقات خوشگوار خطوط پر استوار نہیں ہو سکے۔ دونوں ممالک کے درمیان مسئلہ کشمیر وجہ تنازعہ ہے۔ اس پر اب تک تین جنگیں 1948ء، 1965ء اور 1971ء میں ہو چکی ہیں۔ قیامِ پاکستان کے وقت بھارت نے پاکستان کے لیے کئی مسائل پیدا کیے۔',
  'د پاکستان له جوړېدو تر نن پورې د پاکستان او هند اړیکې پر ښو کرښو ټینګې نه شوې. د دواړو هېوادونو ترمنځ د کشمیر مسئله د شخړې لامل ده. پرې تر اوسه درې جګړې په ۱۹۴۸، ۱۹۶۵ او ۱۹۷۱ز کې شوې. د پاکستان د جوړېدو پر وخت هند د پاکستان لپاره ډېرې ستونزې پیدا کړې.')
P('In 1960 the Indus Waters Treaty was signed between Pakistan and India for the solution of the problem of water. With the help of the World Bank and other countries the scheme reached completion, but India refused to pay the sum of its share.',
  '1960ء میں پاکستان اور بھارت کے درمیان پانی کے مسئلے کے حل کے لیے سندھ طاس معاہدے پر دستخط ہوئے۔ عالمی بینک اور دیگر ممالک کی مدد سے منصوبہ پایہ تکمیل تک پہنچا، لیکن بھارت نے اپنے حصے کی رقم دینے سے انکار کر دیا۔',
  'په ۱۹۶۰ز کې د پاکستان او هند ترمنځ د اوبو د ستونزې د حل لپاره د سند د حوزې پر تړون لاسلیک وشو. د نړیوال بانک او نورو هېوادونو په مرسته پروژه بشپړه شوه، خو هند د خپلې برخې د پیسو له ورکولو انکار وکړ.')
P('In 1971 India helped the separatist elements in East Pakistan, because of which Bangladesh came into existence. After this an agreement took place between Pakistan and India at Simla, which is called the Simla Agreement. According to this agreement Pakistan and India announced that they would resolve their differences through negotiations.',
  '1971ء میں بھارت نے مشرقی پاکستان میں علیحدگی پسند عناصر کی مدد کی جس کی وجہ سے بنگلہ دیش وجود میں آیا۔ اس کے بعد پاکستان اور بھارت کے درمیان شملہ کے مقام پر ایک معاہدہ ہوا جسے شملہ معاہدہ کہتے ہیں۔ اس معاہدے کی رُو سے پاکستان اور بھارت نے اپنے اختلافات کو مذاکرات کے ذریعے حل کرنے کا اعلان کیا۔',
  'په ۱۹۷۱ز کې هند په ختیځ پاکستان کې د بېلتون غوښتونکو عناصرو مرسته وکړه، چې له امله یې بنګله دېش رامنځته شو. له دې وروسته د پاکستان او هند ترمنځ په شمله کې یو تړون وشو چې د شملې تړون ورته وایي. د دې تړون له مخې پاکستان او هند اعلان وکړ چې خپل اختلافات به د خبرو اترو له لارې حل کوي.')
P('Through the Simla Agreement some improvement came in the relations of Pakistan and India, and trade and the movement of travellers began on a limited scale. Besides this, in 1980 within the framework of the South Asian Association for Regional Cooperation “SAARC” (SAARC) an effort was made to increase co-operation between the two countries, from which no satisfactory result could come out. Pakistan has always emphasised the invitation to negotiations to India to resolve disputed matters, but India has always resorted to evasion.',
  'شملہ معاہدہ سے پاکستان اور بھارت کے تعلقات میں کچھ بہتری آئی اور محدود پیمانے پر تجارت اور مسافروں کی آمد و رفت شروع ہو گئی۔ اس کے علاوہ 1980ء میں جنوبی ایشیا کی علاقائی تعاون کی تنظیم ’’سارک‘‘ (SAARC) کے دائرہ میں دونوں ملکوں میں تعاون بڑھانے کی کوشش کی گئی، جس کا خاطر خواہ نتیجہ نہ نکل سکا۔ پاکستان ہمیشہ سے اختلافی اُمور کو حل کرنے کے لیے بھارت کو مذاکرات کی دعوت پر زور دیتا رہا ہے لیکن بھارت نے ہمیشہ ٹال مٹول سے کام لیا ہے۔',
  'د شملې له تړون سره د پاکستان او هند په اړیکو کې یو څه ښه والی راغی او په محدوده کچه سوداګري او د مسافرو تګ راتګ پیل شو. سربېره پر دې په ۱۹۸۰ز کې د سویلي اسیا د سیمه‌ییزې همکارۍ سازمان "سارک" (SAARC) په چوکاټ کې د دواړو هېوادونو ترمنځ د همکارۍ د زیاتولو هڅه وشوه، چې د قناعت وړ پایله یې ونه لرله. پاکستان تل د اختلافي چارو د حل لپاره هند ته د خبرو د بلنې ټینګار کړی، خو هند تل له ځنډ او بهانو کار اخیستی.')
P('In 1988, on the occasion of the “SAARC” conference, the Prime Ministers of Pakistan and India got the opportunity to meet, in which an agreement was signed. According to this agreement both countries became bound not to attack each other’s nuclear centres.',
  '1988ء میں ’’سارک‘‘ کانفرنس کے موقع پر پاکستان اور بھارت کے وزرائے اعظم کو ملنے کا موقع ملا جس میں ایک معاہدے پر دستخط ہوئے۔ اس معاہدے کے مطابق دونوں ممالک ایک دوسرے کے جوہری مراکز پر حملہ نہ کرنے کے پابند ہوئے۔',
  'په ۱۹۸۸ز کې د "سارک" کنفرانس پر وخت د پاکستان او هند لومړیو وزیرانو ته د لیدو فرصت پیدا شو، چې پکې پر یوه تړون لاسلیک وشو. د دې تړون له مخې دواړه هېوادونه پابند شول چې د یو بل پر اټومي مرکزونو برید ونه کړي.')
rec = BOOK.record(t, 'pak12-ch10-text-3', 'Chapter 10 text (3)', 'بابِ دہم — متن (۳)', 'لسم څپرکی — متن (۳)', 100, [189, 190])
rec['sourceNote'] = 'The photographs on p.189 (Khunjerab Pass, captioned in print; a JF-17 aircraft, uncaptioned) are replaced by coded illustrations. The China paragraph runs across the page turn to p.190.'
issues = [{'id': 'pak12-pdf100', 'unit': 10, 'printedPage': 189,
           'description': 'The JF-17 photograph on p.189 has no printed caption; the label is supplied editorially. The text calls the aircraft “JF-Thunder-17” and dates SAARC to 1980 (founded 1985) — retained as printed. Decorative pink/green borders are not reproduced.'}]

if __name__ == '__main__':
    BOOK.save(100, [(10, rec)], issues=issues)
