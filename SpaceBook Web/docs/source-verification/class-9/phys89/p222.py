# -*- coding: utf-8 -*-
TITLE = 'Unit of specific heat / Table 8.3 specific heats / 8.5.3 importance of high specific heat of water'
H = ['Materials', 'Specific heat J kg⁻¹ K⁻¹']
R = [['Aluminum', '910'], ['Copper', '387'], ['Glass', '840'], ['Gold', '129'], ['Iron/ steel', '452'], ['Lead', '128'], ['Silver', '230'], ['Wood', '1700'],
     ['Ethanol', '2450'], ['Glycerin', '2410'], ['Mercury', '139'], ['Water', '4190'], ['Air', '721'], ['Carbon dioxide', '638'], ['Oxygen', '651'], ['Steam (100 °C)', '1520']]
NU = ['ایلومینیم', 'تانبا', 'شیشہ', 'سونا', 'لوہا/فولاد', 'سیسہ', 'چاندی', 'لکڑی', 'ایتھنول', 'گلیسرین', 'پارہ', 'پانی', 'ہوا', 'کاربن ڈائی آکسائیڈ', 'آکسیجن', 'بھاپ (100 °C)']
NP = ['المونیم', 'مس', 'ښیښه', 'سره زر', 'اوسپنه/فولاد', 'سرپ', 'سپین زر', 'لرګی', 'ایتانول', 'ګلیسرین', 'سیماب', 'اوبه', 'هوا', 'کاربن ډای اکسایډ', 'اکسیجن', 'بخار (100 °C)']
SECTIONS = [
    ('8.5.2', ('8.5.2 SPECIFIC HEAT CAPACITY (SPECIFIC HEAT)', '8.5.2 مخصوص حرارتی گنجائش (مخصوص حرارت)', '8.5.2 ځانګړی تودوخیز ظرفیت (ځانګړې تودوخه)'), [
        ('p', 'The S.I. unit of specific heat capacity or specific heat is joule per kilogram per Kelvin which is expressed as J kg^{-1} K^{-1}.', 'مخصوص حرارتی گنجائش کی SI اکائی جول فی کلوگرام فی کیلون ہے جو J kg^{-1} K^{-1} لکھی جاتی ہے۔', 'د ځانګړي تودوخیز ظرفیت SI واحد ژول پر کیلوګرام پر کېلوین دی چې J kg^{-1} K^{-1} لیکل کېږي.'),
        ('p', 'Different substances have different specific heat. The quantity of heat needed also depends on the nature of the material; raising the temperature of 1 kilogram of water by 1 K (1 °C) requires 4190 J of heat, but only 910 J is needed to raise the temperature of 1 kilogram of aluminum by 1 K (1 °C). The specific heat of water at 15 °C is 4190 J kg^{-1} K^{-1}. No other substance has a high specific heat capacity and it has natural benefits in sustaining life on the planet earth.',
         'مختلف مادوں کی مخصوص حرارت مختلف ہے۔ درکار حرارت مادے کی نوعیت پر بھی منحصر ہے؛ 1 کلوگرام پانی کا درجۂ حرارت 1 K (1 °C) بڑھانے کے لیے 4190 J چاہیے جبکہ 1 کلوگرام ایلومینیم کے لیے صرف 910 J۔ 15 °C پر پانی کی مخصوص حرارت 4190 J kg^{-1} K^{-1} ہے۔ کسی اور مادے کی مخصوص حرارتی گنجائش اتنی زیادہ نہیں اور یہ زمین پر زندگی قائم رکھنے میں قدرتی فوائد رکھتی ہے۔',
         'بېلابېل مواد بېلابېله ځانګړې تودوخه لري. اړینه تودوخه د مادې په طبیعت پورې هم اړه لري؛ د 1 کیلوګرام اوبو د تودوخې 1 K (1 °C) لوړولو ته 4190 J او د 1 کیلوګرام المونیم لپاره یوازې 910 J پکار دي. په 15 °C کې د اوبو ځانګړې تودوخه 4190 J kg^{-1} K^{-1} ده. بله هېڅ ماده دومره لوړ ځانګړی تودوخیز ظرفیت نه لري او دا پر ځمکه د ژوند په ساتلو کې طبیعي ګټې لري.'),
        ('tab', 'phys9-u8-table83', 'TABLE 8.3: SPECIFIC HEATS OF VARIOUS SUBSTANCES', H, R,
         (['مادے', 'مخصوص حرارت J kg⁻¹ K⁻¹'], [[NU[i], r[1]] for i, r in enumerate(R)]), (['مواد', 'ځانګړې تودوخه J kg⁻¹ K⁻¹'], [[NP[i], r[1]] for i, r in enumerate(R)])),
    ]),
    ('8.5.3', ('8.5.3 IMPORTANCE OF THE HIGH SPECIFIC HEAT CAPACITY OF WATER', '8.5.3 پانی کی بلند مخصوص حرارتی گنجائش کی اہمیت', '8.5.3 د اوبو د لوړ ځانګړي تودوخیز ظرفیت اهمیت'), [
        ('p', 'The specific heat capacity of water is equal to 4190 J kg^{-1} K^{-1}. It has some important implications.', 'پانی کی مخصوص حرارتی گنجائش 4190 J kg^{-1} K^{-1} ہے۔ اس کے کچھ اہم نتائج ہیں۔', 'د اوبو ځانګړی تودوخیز ظرفیت 4190 J kg^{-1} K^{-1} دی. ځینې مهمې پایلې لري.'),
        ('h', 'A. Moderate climate of sea shore:', 'A. ساحلِ سمندر کی معتدل آب و ہوا:', 'A. د سمندر د غاړې معتدله اقلیم:'),
        ('p', 'The specific heat of sand is about 800 J kg^{-1} K^{-1}. A certain mass of water needs five times more heat than the same mass of soil for its temperature to rise by 1 °C or 1 K. Hence, the land gets heated much more easily then water. Also, it cools down much easily. Hence, a large difference in temperature is formed that gives rise to land breeze and sea breeze. It keeps the climate of the coastal areas moderate. Monsoon in Pakistan is also due to the difference in temperature between the land and the surrounding sea.',
         'ریت کی مخصوص حرارت تقریباً 800 J kg^{-1} K^{-1} ہے۔ پانی کی ایک مقدار کو اتنی ہی کمیت کی مٹی کے مقابلے میں 1 °C یا 1 K درجۂ حرارت بڑھانے کے لیے پانچ گنا زیادہ حرارت چاہیے۔ اس لیے خشکی پانی سے کہیں آسانی سے گرم ہوتی اور آسانی سے ٹھنڈی ہوتی ہے۔ یوں درجۂ حرارت کا بڑا فرق بنتا ہے جس سے خشکی کی ہوا اور سمندری ہوا چلتی ہے۔ یہ ساحلی علاقوں کی آب و ہوا معتدل رکھتا ہے۔ پاکستان میں مون سون بھی خشکی اور گرد کے سمندر کے درجۂ حرارت کے فرق کی وجہ سے ہے۔',
         'د شګو ځانګړې تودوخه شاوخوا 800 J kg^{-1} K^{-1} ده. یوه اندازه اوبه د همغومره کتلې خاورې په پرتله د 1 °C یا 1 K لوړېدو لپاره پنځه چنده ډېره تودوخه غواړي. نو وچه تر اوبو ډېره اسانه تودېږي او اسانه سړېږي. له دې د تودوخې لوی توپیر جوړېږي چې د وچې او سمندر باد رامنځته کوي. دا د ساحلي سیمو اقلیم معتدل ساتي. په پاکستان کې مونسون هم د وچې او شاوخوا سمندر د تودوخې د توپیر له امله دی.'),
        ('h', 'B. As a coolant:', 'B. ٹھنڈا کرنے والے کے طور پر:', 'B. د سړوونکي په توګه:'),
        ('p', 'Water is used as an effective coolant. By allowing water to flow in radiator pipes of the vehicles, heat energy form such parts is removed. Thus, water extracts much heat without much rise in temperature.',
         'پانی مؤثر ٹھنڈک پہنچانے والے کے طور پر استعمال ہوتا ہے۔ گاڑیوں کے ریڈی ایٹر پائپوں میں پانی بہا کر ان حصوں سے حرارتی توانائی نکالی جاتی ہے۔ یوں پانی درجۂ حرارت میں زیادہ اضافے کے بغیر بہت حرارت نکالتا ہے۔',
         'اوبه د اغېزمن سړوونکي په توګه کارېږي. د موټرو د راډیاتور په نلونو کې د اوبو په بهولو له دې برخو تودوخیزه انرژي لرې کېږي. نو اوبه بې له ډېر تودېدو ډېره تودوخه باسي.'),
    ]),
]
EXTRA = dict(tables=[dict(id='phys9-u8-table83', sourceNumber='Table 8.3', title='TABLE 8.3: SPECIFIC HEATS OF VARIOUS SUBSTANCES', headers=H, rows=R)])
