"""Urdu XII PDF113 (spread): p.216 Poem 7 'ہمیشہ دیر کر دیتا ہوں' (Munir Niazi, d.2006 — copyrighted) summary; p.217 مشق Q1–Q7."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
s = Builder()
s.h('I Am Always Late — Munir Niazi', 'ہمیشہ دیر کر دیتا ہوں — منیرؔ نیازی', 'زه تل ځنډ کوم — منیر نیازي')
s.p('[Summary — Munir Niazi (d. 2006) is in copyright; read the full poem (a free-verse poem of about sixteen lines in four movements, each closing on the refrain “I am always late”) in the printed textbook, p. 216.]', '[خلاصہ — منیرؔ نیازی (وفات ۲۰۰۶ء) کا کلام کاپی رائٹ میں ہے؛ مکمل نظم (تقریباً سولہ مصرعوں کی آزاد نظم، چار حصوں میں، ہر حصہ ’’ہمیشہ دیر کر دیتا ہوں‘‘ پر ختم) درسی کتاب کے صفحہ ۲۱۶ پر پڑھیں۔]', '[لنډیز — د منیر نیازي (مړ ۲۰۰۶ز) کلام د کاپي‌رایټ لاندې دی؛ بشپړ نظم (شاوخوا شپاړس مصرعې ازاد نظم، په څلورو برخو کې، هره برخه په "زه تل ځنډ کوم" پای ته رسېږي) د درسي کتاب په ۲۱۶ مخ کې ولولئ.]')
for x in [
    ('Movement 1: The speaker confesses that he is always late in doing every task — whether it is saying something important, keeping a promise, or calling someone and bringing them back.',
     'حصہ ۱: شاعر اعتراف کرتا ہے کہ وہ ہر کام کرنے میں ہمیشہ دیر کر دیتا ہے — چاہے کوئی ضروری بات کرنی ہو، کوئی وعدہ نبھانا ہو، یا کسی کو آواز دے کر واپس بلانا ہو۔',
     'برخه ۱: شاعر مني چې هر کار کې تل ځنډ کوي — که ضروري خبره کول وي، که ژمنه پوره کول وي، یا چاته غږ کول او بېرته راوستل وي.'),
    ('Movement 2: He is late in helping a friend and giving him comfort, and in going along long-familiar paths to meet someone.',
     'حصہ ۲: کسی دوست کی مدد کرنے اور اس کی ڈھارس بندھانے میں، اور بہت پرانے راستوں پر کسی سے ملنے جانے میں بھی وہ دیر کر دیتا ہے۔',
     'برخه ۲: د یوه ملګري په مرسته او ډاډ ورکولو کې، او په ډېرو زړو لارو د چا لیدو ته په تلو کې هم ځنډ کوي.'),
    ('Movement 3: He is late in giving his heart to the walks of changing seasons, and in deciding whom to remember and whom to forget.',
     'حصہ ۳: بدلتے موسموں کی سیر میں دل لگانے اور یہ طے کرنے میں کہ کسے یاد رکھنا ہے اور کسے بھول جانا ہے، وہ دیر کر دیتا ہے۔',
     'برخه ۳: د بدلېدونکو موسمونو په ګرځېدو کې د زړه لګولو او د دې پرېکړې کې چې څوک یاد وساتي او څوک هېر کړي، ځنډ کوي.'),
    ('Movement 4: He is late in saving someone from a grief before death comes, and in going to tell a person that the truth was something else — the poem closes on the refrain, showing the regret of a man whose indecision and delay cost him the right moment.',
     'حصہ ۴: کسی کو موت سے پہلے کسی غم سے بچانے اور کسی کے پاس جا کر یہ بتانے میں کہ حقیقت کچھ اور تھی، وہ دیر کر دیتا ہے — نظم اسی ٹیپ پر ختم ہوتی ہے اور اُس انسان کی پشیمانی ظاہر کرتی ہے جس کی تذبذب اور تاخیر نے اس سے صحیح لمحہ چھین لیا۔',
     'برخه ۴: د مرګ له راتګ مخکې د چا له غمه ژغورلو او چاته د دې ویلو کې چې حقیقت بل څه و، ځنډ کوي — نظم په همدې ټیپ پای ته رسېږي او د هغه انسان پښېماني ښيي چې د هغه دوه‌زړیتوب او ځنډ ترې سمه شېبه واخیسته.'),
    ('(Saʿat-e Sayyār)', '(ساعتِ سیّار)', '(ساعت سیار)'),
]: s.p(*x)
po = BOOK.record(s, 'urdu12-u24-poem', 'Poem — summary', 'نظم — خلاصہ', 'نظم — لنډیز', 113, [216])
po['sourceGap'] = 'Munir Niazi (d. 2006) — in copyright; movement-wise summary in the app, not verbatim. Printed p. 216. Only the title/refrain “ہمیشہ دیر کر دیتا ہوں” is quoted.'

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.group('lines', [
    ('1. To which psychological state of man has this poem pointed?', '۱۔ اس نظم میں انسان کی کس نفسیاتی کیفیت کی طرف اشارہ کیا گیا ہے؟', '۱. په دې نظم کې د انسان کوم رواني کیفیت ته اشاره شوې؟'),
    ('2. Describe in detail the tasks in doing which the poet is late.', '۲۔ ان کاموں کی تفصیل بیان کریں جن کے کرنے میں شاعر سے دیر ہو جاتی ہے؟', '۲. د هغو کارونو تفصیل بیان کړئ چې په کولو کې یې شاعر ځنډ کوي.'),
    ('3. What losses are to be expected from delay in ordinary life?', '۳۔ عام زندگی میں دیر کرنے کے کیا نقصانات متوقع ہوتے ہیں؟', '۳. په عادي ژوند کې د ځنډ کوم زیانونه متوقع وي؟'),
    ('4. Explain the following lines:', '۴۔ درج ذیل مصرعوں کی وضاحت کریں۔', '۴. لاندې مصرعې تشریح کړئ:'),
    ('(a) “If I must help him, if I must comfort my friend”', '(ا) مدد کرنی ہو اس کی، یار کی ڈھارس بندھانا ہو', '(الف) "که د هغه مرسته کول وي، که یار ته ډاډ ورکول وي"'),
    ('(b) “If I must go and tell him that the truth was something else”', '(ب) حقیقت اور تھی کچھ، اس کو جا کر یہ بتانا ہو', '(ب) "که ورته تلل او دا ویل وي چې حقیقت بل څه و"'),
    ('(c) “If I must call out to him, if I must call him back”', '(ج) اُسے آواز دینی ہو، اُسے واپس بلانا ہو', '(ج) "که هغه ته غږ کول وي، که هغه بېرته راغوښتل وي"'),
    ('5. Write five words that have two meanings each.', '۵۔ ایسے پانچ الفاظ لکھیں جن کے دو دو معنی ہوں۔', '۵. داسې پنځه کلمې ولیکئ چې هره یوه دوه ماناوې ولري.'),
    ('6. Write a summary of this poem.', '۶۔ اس نظم کا خلاصہ تحریر کریں۔', '۶. د دې نظم لنډیز ولیکئ.'),
    ('7. Use the following words in your own sentences: dērīna (old, long-standing), ḍhāras bandhānā (to console), ḥaqīqat (truth), dil lagānā (to set one’s heart on), waʿda nibhānā (to keep a promise).', '۷۔ درج ذیل الفاظ کو اپنے جملوں میں استعمال کریں: دیرینہ۔ ڈھارس بندھانا۔ حقیقت۔ دل لگانا۔ وعدہ نبھانا۔', '۷. لاندې کلمې په خپلو جملو کې وکاروئ: دېرینه (زوړ)، ډاډ ورکول، حقیقت، زړه لګول، ژمنه پوره کول.'),
])
ex = BOOK.record(e, 'urdu12-u24-exercise', 'Exercise', 'مشق', 'تمرین', 113, [217])
issues = [{'id': 'urdu12-pdf113', 'unit': 24, 'printedPage': 217, 'description': 'Exercise Q4 quotes three single lines of the poem; these are part of the board-written exercise and are reproduced as short quotations. Faint quill-and-inkpot background drawing on p.216 is decorative.'}]

if __name__ == '__main__':
    BOOK.save(113, [(24, po), (24, ex)], issues=issues, complete_units=[24])
