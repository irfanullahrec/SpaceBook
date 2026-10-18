# -*- coding: utf-8 -*-
TITLE = 'Float or sink: net force / W/F_B ratio derivation Eq 7.5 / Lab work / Example 7.4 crown'
SECTIONS = [
    ('7.8-net', ('7.8 Archimedes principle — float or sink', '7.8 ارشمیدس کا اصول — تیرنا یا ڈوبنا', '7.8 د ارشمیدس اصل — لامبو یا ډوبېدل'), [
        ('p', 'floats. Now when we submerge a coin figure 7.7(b). It is denser than water, so the coin’s weight is greater than the weight of the displaced water. Hence the coin’s weight is greater than the upward buoyant force, and it sinks.', 'تیرتی ہے۔ اب جب ہم ایک سکہ ڈبوتے ہیں، شکل 7.7(b)۔ یہ پانی سے زیادہ کثیف ہے اس لیے سکے کا وزن ہٹائے گئے پانی کے وزن سے زیادہ ہے۔ لہٰذا سکے کا وزن اوپر کی طرف تیرانے والی قوت سے زیادہ ہے اور یہ ڈوب جاتا ہے۔', 'لامبو وهي. اوس کله چې یوه سکه ډوبه کړو، 7.7(b) شکل. دا تر اوبو کثیفه ده، نو د سکې وزن د بې ځایه شوو اوبو تر وزن ډېر دی. نو د سکې وزن د پورته لامبو قوت تر اندازې ډېر دی او ډوبېږي.'),
        ('p', 'Whether an object will float or sink depends on the net force acting on it. This net force can be calculated as follows:', 'کوئی جسم تیرے گا یا ڈوبے گا اس کا انحصار اس پر عمل کرنے والی خالص قوت پر ہے۔ یہ خالص قوت یوں معلوم کی جا سکتی ہے:', 'ایا یو جسم به لامبو وهي که ډوب به شي، پر هغه عمل کوونکي خالص قوت پورې اړه لري. دا خالص قوت داسې محاسبه کېږي:'),
        ('eq', None, 'F_{net} = F_B − W (object)'),
        ('p', 'Now we can apply Archimedes’ principle, using ‘m_o’ to represent the mass of the submerged object and ‘m_f’ as mass of fluid ‘g’ is acceleration due to gravity.', 'اب ہم ارشمیدس کا اصول لاگو کر سکتے ہیں، جہاں \'m_o\' ڈوبے ہوئے جسم کی کمیت، \'m_f\' سیال کی کمیت اور \'g\' ثقلی اسراع ہے۔', 'اوس د ارشمیدس اصل کارولی شو، چې \'m_o\' د ډوب شوي جسم کتله، \'m_f\' د سیال کتله او \'g\' د جاذبې تعجیل دی.'),
        ('eq', None, 'F_{net} = m_f g − m_o g'),
        ('p', 'Remember that ‘m = ρV’, so the expression can be rewritten as follows:', 'یاد رکھیں کہ \'m = ρV\'، اس لیے اظہار کو یوں دوبارہ لکھا جا سکتا ہے:', 'په یاد ولرئ چې \'m = ρV\'، نو افاده داسې بیا لیکل کېدای شي:'),
        ('eq', None, 'F_{net} = ρ_f V_f g − ρ_o V_o g   or   F_{net} = (ρ_f V_f − ρ_o V_o)g'),
        ('p', 'A simple relationship between the weight ‘W’ of a submerged object of mass m_o and density ρ_o and the buoyant force ‘F_B’ on the object by fluid displaced of mass m_f and density ρ_f can be found by considering their ratio as follows:', 'کمیت m_o اور کثافت ρ_o والے ڈوبے ہوئے جسم کے وزن \'W\' اور کمیت m_f اور کثافت ρ_f والے ہٹائے گئے سیال کی طرف سے جسم پر تیرانے والی قوت \'F_B\' کے درمیان ایک سادہ تعلق ان کا نسبت لے کر یوں معلوم کیا جا سکتا ہے:', 'د m_o کتلې او ρ_o کثافت لرونکي ډوب شوي جسم د وزن \'W\' او د m_f کتلې او ρ_f کثافت لرونکي بې ځایه شوي سیال له خوا پر جسم د لامبو قوت \'F_B\' ترمنځ یوه ساده اړیکه د دوی د نسبت په پام کې نیولو داسې موندل کېږي:'),
        ('eq', None, '[[W|F_B]] = [[m_o g|m_f g]]'),
        ('eq', None, 'or   [[W|F_B]] = [[m_o|m_f]]', '1'),
        ('p', 'for submerged object equal volume is displaced therefore', 'ڈوبے ہوئے جسم کے لیے برابر حجم ہٹتا ہے، لہٰذا', 'د ډوب شوي جسم لپاره مساوي حجم بې ځایه کېږي، نو'),
        ('eq', None, 'V_o = V_B = V'),
        ('eq', None, 'therefore   m_o = ρ_o V   and   m_f = ρ_f V'),
        ('p', 'putting these values in equation 1, we get', 'یہ قدریں مساوات 1 میں رکھنے سے', 'دا ارزښتونه په 1 معادله کې ایښودلو سره'),
        ('eq', None, '[[W|F_B]] = [[ρ_o V|ρ_f V]]'),
        ('eq', 'phys9-u7-eq75', 'or   [[W|F_B]] = [[ρ_o|ρ_f]]', '7.5'),
        ('h', 'LAB WORK', 'لیب ورک', 'لابراتواري کار'),
        ('p', 'To find the density of a body heavier than water by Archimedes Principle.', 'ارشمیدس کے اصول سے پانی سے بھاری جسم کی کثافت معلوم کرنا۔', 'د ارشمیدس د اصل په مرسته د اوبو تر درانه جسم کثافت معلومول.'),
    ]),
    ('ex7.4', ('Example 7.4 IS CROWN MADE OF PURE GOLD?', 'مثال 7.4 کیا تاج خالص سونے کا ہے؟', '7.4 مثال ایا تاج له خالص سرو زرو جوړ دی؟'), [
        ('p', 'A girl purchases a “gold” crown at a flea market. After she gets home, she hangs the crown from a scale and finds its weight to be 7.84 N. She then weighs the crown while it is immersed in water and the scale reads 6.86 N. Is the crown made of pure gold?', 'ایک لڑکی کباڑ بازار سے ایک "سونے" کا تاج خریدتی ہے۔ گھر پہنچ کر وہ تاج کو ترازو سے لٹکاتی ہے اور اس کا وزن 7.84 N پاتی ہے۔ پھر وہ تاج کو پانی میں ڈبو کر تولتی ہے اور ترازو 6.86 N پڑھتا ہے۔ کیا تاج خالص سونے کا بنا ہے؟', 'یوه نجلۍ له کباړ بازار څخه یو "زرین" تاج اخلي. کور ته د رسېدو وروسته تاج له ترازو ځړوي او وزن یې 7.84 N مومي. بیا تاج په اوبو کې ډوب تلي او ترازو 6.86 N ښيي. ایا تاج له خالص سرو زرو جوړ دی؟'),
    ]),
]
