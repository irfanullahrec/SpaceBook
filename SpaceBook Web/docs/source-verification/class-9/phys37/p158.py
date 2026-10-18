# -*- coding: utf-8 -*-
TITLE = 'KE derivation Eq 6.3 / work-energy theorem / information: magnetar / Example 6.2 bullet speed begins'
SECTIONS = [
    ('6.3-deriv', ('6.3 Kinetic energy — derivation', '6.3 حرکی توانائی — اخذ', '6.3 حرکي انرژي — لاسته راوړنه'), [
        ('p', 'By third equation of motion', 'حرکت کی تیسری مساوات سے', 'د حرکت د درېیمې معادلې له مخې'),
        ('eq', None, '2aS = v_f^2 − v_i^2'),
        ('p', 'rearranging', 'ترتیب بدلنے سے', 'په بیا ترتیب'),
        ('eq', None, 'S = [[v_f^2 − v_i^2|2a]]', '3'),
        ('p', 'putting equation 2 and 3 in equation 1', 'مساوات 2 اور 3 کو مساوات 1 میں رکھنے سے', 'د 2 او 3 معادلې په 1 معادله کې ایښودلو سره'),
        ('eq', None, 'E_K = ma × [[v_f^2 − v_i^2|2a]]'),
        ('p', 'or', 'یا', 'یا'),
        ('eq', None, 'E_K = m × [[v_f^2 − v_i^2|2]]'),
        ('p', 'As the object started from rest therefore v_i = 0 and v_f = v', 'چونکہ جسم سکون سے شروع ہوا اس لیے v_i = 0 اور v_f = v', 'څرنګه چې جسم له سکون پیل شو، نو v_i = 0 او v_f = v'),
        ('eq', 'phys9-u6-eq63', 'E_K = [[1|2]] mv^2', '6.3'),
        ('p', 'This equation shows the relation between the kinetic energy of a moving object with its mass and velocity. Equally important, it demonstrate the work kinetic energy theorem which states that the work done on an object is equal to change in energy.', 'یہ مساوات حرکت کرتے جسم کی حرکی توانائی کا اس کی کمیت اور رفتار سے تعلق ظاہر کرتی ہے۔ اتنا ہی اہم یہ کہ یہ کام-حرکی توانائی کے مسئلے کو ظاہر کرتی ہے جو کہتا ہے کہ کسی جسم پر کیا گیا کام توانائی میں تبدیلی کے برابر ہے۔', 'دا معادله د خوځنده جسم د حرکي انرژۍ اړیکه له کتلې او سرعت سره ښيي. همدومره مهم، دا د کار-حرکي انرژۍ قضیه ښيي چې وايي پر جسم ترسره شوی کار د انرژۍ له بدلون سره مساوي دی.'),
        ('h', 'INFORMATION', 'معلومات', 'معلومات'),
        ('p', 'Magnetar: On December 27, 2004, astronomers observed the greatest flash of light ever recorded from outside the solar system. It came from the highly magnetic neutron star SGR 1806-20 (a magnetar). During 0.20 s, this star released as much energy as our sun does in 250,000 years.', 'میگنیٹار: 27 دسمبر 2004 کو ماہرینِ فلکیات نے نظامِ شمسی کے باہر سے اب تک ریکارڈ کی گئی روشنی کی سب سے بڑی چمک دیکھی۔ یہ انتہائی مقناطیسی نیوٹران ستارے SGR 1806-20 (ایک میگنیٹار) سے آئی۔ 0.20 s کے دوران اس ستارے نے اتنی توانائی خارج کی جتنی ہمارا سورج 2,50,000 سال میں کرتا ہے۔', 'مګنېټار: د 2004 کال د ډسمبر په 27 ستوري پوهانو له لمریز نظامه بهر تر اوسه ثبت شوې تر ټولو لویه د رڼا ځلا ولیده. دا د ډېر مقناطیسي نیوټرون ستوري SGR 1806-20 (یو مګنېټار) څخه راغله. په 0.20 s کې دې ستوري دومره انرژي خپره کړه لکه زموږ لمر چې په 250,000 کالو کې یې خپروي.'),
        ('fig', 'Photograph: a bright magnetar flash in space.', 'تصویر: خلا میں میگنیٹار کی تیز چمک۔', 'انځور: په فضا کې د مګنېټار روښانه ځلا.'),
    ]),
    ('ex6.2', ('Example 6.2 BULLET SPEED', 'مثال 6.2 گولی کی رفتار', '6.2 مثال د ګولۍ سرعت'), [
        ('p', 'A 60.0 g bullet is fired from a gun with 3150 J of kinetic energy. Find its velocity.', '60.0 g کی ایک گولی 3150 J حرکی توانائی کے ساتھ بندوق سے چلائی جاتی ہے۔ اس کی رفتار معلوم کریں۔', 'یوه 60.0 g ګولۍ له ټوپکه د 3150 J حرکي انرژۍ سره ویشتل کېږي. سرعت یې معلوم کړئ.'),
        ('h', 'SOLUTION — GIVEN:', 'حل — معلوم:', 'حل — ورکړل شوي:'),
        ('ul', [('mass m = 60 g = 0.06 kg', 'کمیت m = 60 g = 0.06 kg', 'کتله m = 60 g = 0.06 kg'), ('Kinetic energy E_k = 3150 J', 'حرکی توانائی E_k = 3150 J', 'حرکي انرژي E_k = 3150 J')]),
        ('h', 'REQUIRED:', 'مطلوب:', 'غوښتل شوي:'),
        ('p', 'velocity v = ?', 'رفتار v = ?', 'سرعت v = ?'),
        ('p', 'The kinetic energy is given as', 'حرکی توانائی یوں ہے', 'حرکي انرژي داسې ده'),
        ('eq', None, 'E_K = [[1|2]] mv^2'),
        ('p', 'rearranging', 'ترتیب بدلنے سے', 'په بیا ترتیب'),
        ('eq', None, 'v^2 = [[2E_K|m]]'),
        ('h', 'EXTENSION EXERCISE 6.1', 'توسیعی مشق 6.1', '6.1 پراخه تمرین'),
        ('p', 'If a car of mass 800 kg is having same kinetic energy, what will be its speed?', 'اگر 800 kg کمیت کی گاڑی کی حرکی توانائی بھی یہی ہو تو اس کی رفتار کیا ہوگی؟', 'که د 800 kg کتلې موټر هم دا حرکي انرژي ولري، سرعت به یې څومره وي؟'),
    ]),
]
