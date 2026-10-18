"""Urdu XII PDF102 (spread): p.194 Poem 2 author note (اختر شیرانی, 1905–1948); p.195 Poem 2 'بڑھے چلو' full text (public domain)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
a = Builder()
a.h('Akhtar Sheerani', 'اخترؔ شیرانی', 'اختر شیراني')
a.p('Born: 1905 · Died: 1948', 'ولادت: ۱۹۰۵ء · وفات: ۱۹۴۸ء', 'زېږېدنه: ۱۹۰۵ز · مړینه: ۱۹۴۸ز')
for x in [
    ("Akhtar Sheerani's real name was Muhammad Dawood Khan and he used the pen-name Akhtar. He was the son of the famous scholar, researcher, educationist and critic Hafiz Mahmood Sheerani. Akhtar Sheerani was born in the state of Tonk. His father moved from Tonk to Lahore. He was educated in Lahore and passed the Munshi Fazil and Adeeb Fazil examinations from Oriental College Lahore. After that he remained associated with various literary journals.",
     'اخترؔ شیرانی کا اصل نام محمد داؤد خاں تھا اور اخترؔ تخلص کرتے تھے۔ وہ مشہور عالم، محقق، ماہرِ تعلیم اور نقاد حافظ محمود شیرانی کے بیٹے تھے۔ اخترؔ شیرانی ریاست ٹونک میں پیدا ہوئے۔ اُن کے والد ٹونک سے لاہور منتقل ہو گئے۔ اُنھوں نے لاہور میں تعلیم حاصل کی۔ اورینٹل کالج لاہور سے منشی فاضل اور ادیب فاضل کا امتحان پاس کیا۔ اس کے بعد مختلف ادبی رسائل سے وابستہ رہے۔',
     'د اختر شیراني اصلي نوم محمد داود خان و او "اختر" یې تخلص کاوه. هغه د مشهور عالم، څېړونکي، د ښوونې پوه او نقاد حافظ محمود شیراني زوی و. اختر شیراني د ټونک په ریاست کې زېږېدلی. پلار یې له ټونک لاهور ته کډه شو. هغه په لاهور کې زده‌کړې وکړې؛ له اورینټل کالج لاهور نه یې د منشي فاضل او ادیب فاضل ازموینې بریالۍ کړې. له هغې وروسته له بېلابېلو ادبي مجلو سره تړلی پاتې شو.'),
    ("Akhtar began writing poetry at an early age. His nature was brimming with playfulness and colour. He had a deep interest in the scenes of nature. He was an important romantic poet of his age, but his romanticism cannot be subtracted from emotion. The kind of layered depth found in good poetry is not seen in his work, yet he is a fortunate poet in that his verses are on everyone's lips. A special feature of his poetry is that for him woman is not something otherworldly but an ordinary human being, with nothing unnatural in her conduct. For him poetry is a passion born of a lover's solitudes. Akhtar is a conscious artist; avoiding the prevailing styles, he made various experiments in form.",
     'اخترؔ نے کم عمری سے ہی شعر کہنے شروع کیے۔ اُن کی طبیعت میں شوخی اور رنگینی کُوٹ کُوٹ کر بھری ہوئی تھی۔ اُنھیں مناظرِ قدرت سے گہری دلچسپی تھی۔ وہ اپنے دور کے ایک اہم رومانی شاعر تھے، لیکن اُن کی رومانیت سے جذبات کو منہا نہیں کیا جا سکتا۔ اچھی شاعری میں جس طرح کی تہہ داری ہوتی ہے، وہ اُن کے ہاں نظر نہیں آتی، لیکن وہ اس لحاظ سے خوش قسمت شاعر ہیں کہ اُن کے اشعار زبان زدِ عام ہیں۔ اُن کی شاعری کی ایک خاص بات یہ ہے کہ اُن کے ہاں عورت کوئی ماورائی چیز نہیں بلکہ عام انسان ہے اور اُس کے رویوں میں کوئی غیر فطری عناصر نہیں ہیں۔ اُن کے نزدیک شاعری ایک ایسا جذبہ ہے جو عاشقانہ تنہائیوں کی پیداوار ہے۔ اخترؔ ایک باشعور فنکار ہیں، اُنھوں نے مروجہ اسالیب سے گریز کرتے ہوئے ہیئت کے مختلف تجربے کیے ہیں۔',
     'اختر په کم عمر کې شعر ویل پیل کړل. په طبیعت کې یې شوخي او رنګیني ډکه وه. د طبیعت له منظرو سره یې ژوره لېوالتیا درلوده. هغه د خپل وخت یو مهم رومانتیک شاعر و، خو د هغه له رومانتیکتوب څخه احساسات نه شي جلا کېدای. هغه ژوروالی چې په ښه شاعرۍ کې وي، د هغه په کلام کې نه ښکاري، خو په دې لحاظ نېکمرغه شاعر دی چې بیتونه یې د خلکو پر ژبو دي. د هغه د شاعرۍ یوه ځانګړې خبره دا ده چې د هغه په نزد ښځه کوم ماورايي شی نه، بلکې عادي انسان دی او په چلند کې یې کوم غیر طبیعي عناصر نشته. د هغه په نظر شاعري داسې جذبه ده چې د عاشقانه یوازېتوب زېږنده ده. اختر یو باشعوره هنرمند دی؛ له دودیزو سبکونو یې ډډه کړې او د بڼې ډول ډول تجربې یې کړې.'),
    ('Collected poetry: Kulliyat-e-Akhtar Sheerani.', 'مجموعۂ کلام: (کلیاتِ اخترؔ شیرانی)', 'د کلام ټولګه: کلیات اختر شیراني.'),
]: a.p(*x)
UT = ('March On (Barhe Chalo)', 'بڑھے چلو', 'مخ ته ولاړ شئ', 'اخترؔ شیرانی')
au = BOOK.record(a, 'urdu12-u19-author', 'About the poet: Akhtar Sheerani', 'اخترؔ شیرانی (تعارف)', 'اختر شیراني (پېژندنه)', 102, [194], unit_title=UT)
au['sourceCoverIllustrationReview'] = 'Portrait photograph of Akhtar Sheerani and floral border are decorative; not reproduced.'

t = Builder()
t.h('March On — Akhtar Sheerani', 'بڑھے چلو — اخترؔ شیرانی', 'مخ ته ولاړ شئ — اختر شیراني')
CH = [('Brave swordsmen, march on, march on;', 'دلاورانِ تیغ زن بڑھے چلو، بڑھے چلو', 'تورې وهونکو زړورو، مخ ته ځئ، مخ ته ځئ؛'),
      ('valiant rank-breakers, march on, march on.', 'بہادرانِ صف شکن بڑھے چلو، بڑھے چلو', 'لیکې ماتوونکو اتلانو، مخ ته ځئ، مخ ته ځئ.')]
ST = [
 [('Do not stop, though desert and sandy wastes lie before you;', 'رُکو نہیں، جو دشت و ریگزار آئیں سامنے', 'مه درېږئ، که دښتې او شګلنې سیمې مخې ته درشي؛'),
  ('do not flinch, though floods and rivers lie before you;', 'بچو نہیں، جو سیل و جوئے بار آئیں سامنے', 'مه ډډه کوئ، که سېلابونه او سیندونه مخې ته درشي؛'),
  ('do not retreat, though sea and mountain lie before you;', 'ہٹو نہیں، جو بحر و کوہسار آئیں سامنے', 'شا ته مه کېږئ، که سمندر او غرونه مخې ته درشي؛'),
  ('however hard the road may be, march on, march on.', 'ہو راہ کتنی ہی کٹھن بڑھے چلو، بڑھے چلو', 'لار که هر څومره سخته وي، مخ ته ځئ، مخ ته ځئ.')],
 [('The homeland takes pride in your sharp sword;', 'تمھاری تیغِ تیز پر وطن کو افتخار ہے', 'وطن ستاسو پر تېره توره ویاړي؛'),
  ('the homeland’s death and life depend on you;', 'وطن کی مرگ و زیست کا تمھیں پہ انحصار ہے', 'د وطن مرګ او ژوند پر تاسو تړلی دی؛'),
  ('it is you in whose hearts its love is restless;', 'تمھیں ہو جن کے دل میں اس کا عشق بے قرار ہے', 'تاسو یاست چې د هغه مینه مو په زړونو کې بې‌قراره ده؛'),
  ('with a passion kindled in your hearts, march on, march on.', 'لگائے دل میں اک لگن بڑھے چلو، بڑھے چلو', 'په زړه کې یوه لېوالتیا بله کړئ، مخ ته ځئ، مخ ته ځئ.')],
 [('Raise the merciless sword in the pure name of the homeland;', 'اٹھاؤ تیغِ بے اماں، وطن کے پاک نام پر', 'د وطن پر پاک نوم بې‌امانه توره پورته کړئ؛'),
  ('spend your youthful lives in the pure name of the homeland;', 'لٹا دو عمرِ نوجواں، وطن کے پاک نام پر', 'د وطن پر پاک نوم خپله ځواني قربان کړئ؛'),
  ('sacrifice your lives in the pure name of the homeland;', 'نثار کر دو اپنی جاں، وطن کے پاک نام پر', 'د وطن پر پاک نوم خپل ځانونه قربان کړئ؛'),
  ('the homeland is calling — march on, march on.', 'صدائیں دیتا ہے وطن، بڑھے چلو، بڑھے چلو', 'وطن غږ کوي — مخ ته ځئ، مخ ته ځئ.')],
]
for i, st in enumerate(ST, 1):
    t.p(f'Stanza {i}', f'بند {"۰۱۲۳"[i]}', f'بند {i}')
    t.group('lines', st)
    t.group('lines', CH)
po = BOOK.record(t, 'urdu12-u19-poem', 'Poem text', 'متنِ نظم', 'د نظم متن', 102, [195])
issues = [{'id': 'urdu12-pdf102', 'unit': 19, 'printedPage': 195, 'description': 'Akhtar Sheerani died 1948; under Pakistani copyright (life + 50 years) the poem is public domain and transcribed in full. The two-line refrain is printed after every stanza and is repeated likewise.'}]

if __name__ == '__main__':
    BOOK.save(102, [(19, au), (19, po)], issues=issues)
