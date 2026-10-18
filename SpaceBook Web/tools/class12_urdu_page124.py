"""Urdu XII PDF124 (spread): p.238 Ghazal 15 author note (ظفر اقبال, b.1933); p.239 Ghazal 15 (living poet — copyrighted) couplet-wise summary."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
a = Builder()
a.h('Zafar Iqbal', 'ظفرؔ اقبال', 'ظفر اقبال')
a.p('Born: 1933', 'ولادت: ۱۹۳۳ء', 'زېږېدنه: ۱۹۳۳ز')
for x in [
    ("Zafar Iqbal, born in Okara, has a poetic journey of more than half a century. At first he was sometimes near to and sometimes far from the traditions of the ghazal; at last he became free of the spell of the ghazal's traditions, but on this journey he had to pass through hard stages. The common reader and the creative writer of Urdu literature are such captives of the traditions of the Urdu ghazal that they cannot even think of leaving this enchanted atmosphere. In past centuries Hali and Insha did try to break the ghazal's traditions, but what change came to the ghazal through those efforts? Hali and Insha were deprived of their own place in the Urdu ghazal.",
     'اوکاڑہ میں پیدا ہونے والے ظفرؔ اقبال کی شاعری کا سفر نصف صدی سے زیادہ ہے۔ ابتدا میں وہ غزل کی روایات کے کبھی قریب اور کبھی دُور ہوئے۔ آخر کار غزل کی روایات کے سحر سے آزاد ہو گئے لیکن اس سفر میں اُنھیں کڑے مراحل سے گزرنا پڑا۔ اُردو ادب کا عام قاری اور تخلیق نگار اُردو غزل کی روایات کا ایسا اسیر ہے کہ وہ اس طلسمی فضا سے باہر نکلنے کا سوچ بھی نہیں سکتا۔ گزشتہ صدیوں میں حالیؔ اور انشاؔ نے غزل کی روایات کو توڑنے کی کوشش ضرور کی لیکن اس کوششوں کی بِنا پر غزل میں کیا تبدیلی آتی، اُردو غزل میں حالیؔ اور انشاؔ اپنے مقام سے محروم ہو گئے۔',
     'په اوکاړه کې زېږېدلي ظفر اقبال د شاعرۍ سفر له نیمې پېړۍ زیات دی. په پیل کې هغه کله د غزل دودونو ته نږدې او کله ترې لرې شو؛ په پای کې د غزل د دودونو له جادو ازاد شو، خو په دې سفر کې یې له سختو پړاوونو تېرېدل وو. د اردو ادب عام لوستونکی او پنځګر د اردو غزل د دودونو داسې بندي دی چې له دې جادويي فضا د وتلو فکر هم نه شي کولی. په تېرو پېړیو کې حالي او انشا د غزل د دودونو د ماتولو هڅه خو وکړه، خو د دې هڅو له امله په غزل کې څه بدلون راغی؟ حالي او انشا په اردو غزل کې له خپل مقامه بې‌برخې شول.'),
    ("Zafar Iqbal's important achievement is that he has completely changed the centuries-old traditional atmosphere of the ghazal and the ghazal's inherited aesthetics. That is why Dr. Tabassum Kashmiri has rightly called him the literary apostate of the twentieth century and the first poet to be freed from the slavery of the traditional ghazal.",
     'ظفرؔ اقبال کا اہم کارنامہ یہ ہے کہ انھوں نے غزل کی صدیوں پُرانی روائتی فضا اور غزل کی موروثی جمالیات کو مکمل طور پر تبدیل کر دیا ہے۔ اس لیے ڈاکٹر تبسم کاشمیری نے اُنھیں بجا طور پر بیسویں صدی کا ادبی مرتد اور روایتی غزل کی غلامی سے آزاد ہونے والا پہلا شاعر کہا ہے۔',
     'د ظفر اقبال مهمه کارنامه دا ده چې د غزل پېړیو زوړ دودیز چاپېریال او د غزل میراثي ښکلاپوهنه یې بشپړه بدله کړې. ځکه ډاکټر تبسم کاشمیري هغه په حقه د شلمې پېړۍ ادبي "مرتد" او له دودیز غزل غلامۍ ازادېدونکی لومړی شاعر بللی.'),
    ('Collections of poetry: Tajdeed, Taqweem, Tashkeel, Tajawuz, Tawarud, Tasahul, Aab-e-Rawan, Gulaftab, Hate Hanuman, Ratb-o-Yabis, Ab Tak (Kulliyat).', 'مجموعہ ہائے کلام: تجدید، تقویم، تشکیل، تجاوز، توارد، تساہل، آبِ رواں، گلافتاب، ہٹے ہنومان، رطب و یابس، اب تک (کلیات)', 'د کلام ټولګې: تجدید، تقویم، تشکیل، تجاوز، توارد، تساهل، آب روان، ګلافتاب، هټې هنومان، رطب و یابس، اب تک (کلیات).'),
]: a.p(*x)
UT = ('Ghazal: We did not sit together, did not share our dreams', 'غزل: مل کے بیٹھے نہیں، خوابوں میں شراکت نہیں کی', 'غزل: یوځای کېنا نه ستو، په خوبونو کې مو شراکت ونه کړ', 'ظفرؔ اقبال')
au = BOOK.record(a, 'urdu12-u32-author', 'About the poet: Zafar Iqbal', 'ظفرؔ اقبال (تعارف)', 'ظفر اقبال (پېژندنه)', 124, [238], unit_title=UT)
au['sourceCoverIllustrationReview'] = 'Portrait photograph of Zafar Iqbal is decorative; not reproduced.'

s = Builder()
s.h('Ghazal — Zafar Iqbal', 'غزل — ظفرؔ اقبال', 'غزل — ظفر اقبال')
s.p('[Couplet-wise summary — Zafar Iqbal is a living poet and his work is in copyright; read the full ghazal (nine couplets) in the printed textbook, pp. 239–240.]', '[شعر وار خلاصہ — ظفرؔ اقبال حیات شاعر ہیں اور ان کا کلام کاپی رائٹ میں ہے؛ مکمل غزل (نو اشعار) درسی کتاب کے صفحات ۲۳۹–۲۴۰ پر پڑھیں۔]', '[بیت په بیت لنډیز — ظفر اقبال ژوندی شاعر دی او کلام یې د کاپي‌رایټ لاندې دی؛ بشپړ غزل (نهه بیتونه) د درسي کتاب په ۲۳۹–۲۴۰ مخونو کې ولولئ.]')
for x in [
    ('1. We never sat together, never shared dreams — what other bond could there be with you, if not love we never declared?',
     '۱۔ ہم کبھی مل کر نہیں بیٹھے، خوابوں میں شراکت نہیں کی — تجھ سے اور کیا رشتہ ہو جب محبت ہی نہیں کی؟',
     '۱. موږ هېڅکله یوځای کېنا نه ستو، په خوبونو کې مو شراکت ونه کړ — له تا سره به بله کومه اړیکه وي کله چې مینه مو هم ونه کړه؟'),
    ('2. We wander here looking like decent men; we never threw dust in the wilderness or went mad (as lovers do).',
     '۲۔ ہم یہیں شریف آدمیوں کی صورت پھرتے ہیں؛ کبھی دشت میں خاک نہیں اُڑائی، وحشت نہیں کی۔',
     '۲. موږ همدلته د شریفو خلکو په بڼه ګرځو؛ هېڅکله مو په دښته کې خاورې نه دي الوتې، لېونتوب مو نه دی کړی.'),
    ('3. Your treatment was not special to us alone — and we, too, showed you no special favour.',
     '۳۔ تیرا سلوک صرف ہم سے خاص نہیں تھا، اور ہم نے بھی تیرے ساتھ کوئی رعایت نہیں کی۔',
     '۳. ستا چلند یوازې له موږ سره ځانګړی نه و، او موږ هم له تا سره کومه رعایت ونه کړ.'),
    ('4. We might have asked you your intention some time; we wished to many times, but never had the courage.',
     '۴۔ کبھی تجھ سے تیرا ارادہ بھی پوچھ لیتے؛ ہم نے کئی بار چاہا تھا، مگر ہمت نہیں کی۔',
     '۴. کله به مو له تا ستا اراده هم پوښتلې وای؛ ډېر ځله مو وغوښتل، خو همت مو ونه کړ.'),
    ('5. Though we liked you very much, in that gathering we deliberately did not take your side.',
     '۵۔ تو ہمیں بہت اچھا بھی لگا، مگر اُس محفل میں ہم نے دانستہ تیری حمایت نہیں کی۔',
     '۵. که څه هم ته موږ ته ډېر ښه ښکارېدې، خو په هغه غونډه کې مو قصداً ستا ملاتړ ونه کړ.'),
]: s.p(*x)
po = BOOK.record(s, 'urdu12-u32-ghazal', 'Ghazal — couplet-wise summary (1)', 'غزل — شعر وار خلاصہ (۱)', 'غزل — بیت په بیت لنډیز (۱)', 124, [239])
po['sourceGap'] = 'Zafar Iqbal (living) — in copyright; couplet-wise summary in the app, not verbatim. Printed p. 239 (couplets 1–5 of 9; continues on p.240).'
issues = [{'id': 'urdu12-pdf124', 'unit': 32, 'printedPage': 238, 'description': 'p.238 shows Zafar Iqbal’s birth year with an unclear digit (reads like ۱۹۲۳ء/۱۹۳۳ء); the standard date 27 September 1933 is used. Only a birth year is printed (living poet). “اس کوششوں کی بِنا پر” (number agreement) retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(124, [(32, au), (32, po)], issues=issues)
