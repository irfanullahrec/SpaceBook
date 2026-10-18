"""Urdu XII PDF138 (spread): pp.266–267 — Glossary: Ghazals 10–16 (end of glossary)."""
from class12_urdu_glossary import page

G10 = [
    ('ہات', 'ہاتھ', 'hāt — hand', 'لاس'),
    ('دھج', 'انداز، طریقہ', 'dhaj — manner, style', 'انداز، طریقه'),
    ('مقتل', 'قتل گاہ، پھانسی گھاٹ', 'maqtal — place of slaughter, gallows', 'وژنځی، د ځړولو ځای'),
]
G11 = [
    ('دَر', 'دروازہ، دہلیز', 'dar — door, threshold', 'دروازه، درشل'),
    ('پہلو', 'قرب، پاس', 'pahlū — side, nearness', 'څنګ، نږدې'),
    ('چارہ ساز', 'علاج کرنے والا، کام بنانے والا', 'chāra-sāz — healer, one who sets things right', 'درملګر، کار جوړوونکی'),
    ('سنور جانا', 'آراستہ ہونا، درست ہونا', 'sanwar jānā — to be adorned, set right', 'سینګارېدل، سمېدل'),
    ('گھِر جانا', 'محصور ہونا', 'ghir jānā — to be surrounded, hemmed in', 'راګېرېدل'),
    ('پیمانِ وفا', 'ساتھ دینے کا وعدہ / اقرار', 'paimān-e wafā — pledge of loyalty', 'د وفا ژمنه'),
    ('معیار', 'پرکھ، کسوٹی', 'miʿyār — standard, touchstone', 'معیار، محک'),
]
G12 = [
    ('احباب', '(حبیب کی جمع) دوست', 'aḥbāb — (plural of ḥabīb) friends', 'ملګري'),
    ('اوّلیں', 'پہلا', 'awwalīṉ — first', 'لومړی'),
    ('سرشاری', 'خوشی، مسرت', 'sarshārī — elation, joy', 'خوښي'),
    ('عارض', 'گال', 'ʿāriẓ — cheek', 'انانګی'),
    ('لب', 'ہونٹ', 'lab — lip', 'شونډه'),
]
G13 = [
    ('در و بام', '(دروازہ اور چھت) مُراد مکان', 'dar-o-bām — door and roof, i.e. the house', 'دروازه او بام، مطلب کور'),
    ('دستار', 'پگڑی (جو بزرگی اور عزت کی علامت ہے)', 'dastār — turban (a sign of eminence and honour)', 'پګړۍ (د مشرتوب او عزت نښه)'),
]
G14 = [
    ('اَسرار', '(سِر کی جمع) راز', 'asrār — (plural of sirr) secrets', 'رازونه'),
    ('دار', 'پھانسی کا مقام', 'dār — the gallows', 'دار'),
    ('لب کُشا', 'لب کھولنا، بولنا', 'lab-kushā — opening one’s lips, speaking out', 'خوله پرانیستل، خبرې کول'),
    ('پسِ پردہ', 'پردے کے پیچھے', 'pas-e parda — behind the curtain', 'تر پردې شا'),
]
G15 = [
    ('شراکت', 'حصہ داری، شریک ہونا', 'shirākat — partnership, sharing', 'شراکت'),
    ('دانستہ', 'جان بوجھ کر، قصداً', 'dānista — deliberately', 'قصداً'),
    ('عنایت', 'مہربانی، توجہ', 'ʿināyat — kindness, favour', 'مهرباني'),
    ('کُشادہ', 'کھلا، وسیع', 'kushāda — open, wide', 'پراخ'),
    ('دشت', 'صحرا، بیابان', 'dasht — desert, wilderness', 'دښته'),
    ('وحشت', 'ڈر، خوف، پاگل پن', 'waḥshat — fear, madness', 'وېره، لېونتوب'),
    ('رعایت', 'طرف داری کرنا، مہربانی کرنا', 'riʿāyat — favour, concession', 'رعایت، مهرباني'),
    ('حسرت', 'آرزو، ارمان', 'ḥasrat — longing, regret', 'ارمان'),
]
G16 = [
    ('اصرار', 'ضد، تاکید', 'iṣrār — insistence', 'ټینګار'),
    ('گردن زدنی', 'واجب القتل، مار ڈالنے کے قابل', 'gardan-zadanī — deserving death', 'د وژلو وړ'),
    ('عظمت', 'بڑائی، بزرگی', 'ʿaẓmat — greatness', 'لویي'),
    ('زخم سینا', 'لفظی معنی زخم کو ٹانکے لگانا، مُراد: دادرسی کرنا، حوصلہ بڑھانا', 'zakhm sīnā — literally stitching a wound; i.e. consoling, encouraging', 'ټپ ګنډل — مطلب ډاډ ورکول، زړه ورکول'),
]

if __name__ == '__main__':
    page(138, [266, 267], [
        ('Ghazal 10: Faiz Ahmad Faiz', 'فیض احمد فیضؔ', 'فیض احمد فیض', G10),
        ('Ghazal 11: Ahmad Nadeem Qasmi', 'احمد ندیمؔ قاسمی', 'احمد ندیم قاسمي', G11),
        ('Ghazal 12: Nasir Kazmi', 'ناصرؔ کاظمی', 'ناصر کاظمي', G12),
        ('Ghazal 13: Shakeeb Jalali', 'شکیبؔ جلالی', 'شکیب جلالي', G13),
        ('Ghazal 14: Ahmad Faraz', 'احمد فرازؔ', 'احمد فراز', G14),
        ('Ghazal 15: Zafar Iqbal', 'ظفرؔ اقبال', 'ظفر اقبال', G15),
        ('Ghazal 16: Shahzad Ahmad', 'شہزادؔ احمد', 'شهزاد احمد', G16),
    ])
