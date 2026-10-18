# -*- coding: utf-8 -*-
TITLE = 'Gravitational PE = mgh / Figures 6.6–6.7 / Table 6.2 energy of objects / PE proof'
_R = [['Big Bang', '10^68'], ['Annual world energy use', '4 × 10^20'], ['1 kg uranium', '4 × 10^13'], ['1 ton TNT', '4.2 × 10^9'], ['1000-kg car at 90 km/h', '3.1 × 10^5'], ['Tennis ball at 100 km/h', '22'], ['Single electron in TV Screen', '4 × 10^-15'], ['Energy to break one DNA strand', '10^-19']]
_U = ['بگ بینگ', 'دنیا میں توانائی کا سالانہ استعمال', '1 kg یورینیم', '1 ٹن TNT', '90 km/h پر 1000 kg کی گاڑی', '100 km/h پر ٹینس بال', 'ٹی وی اسکرین میں ایک الیکٹران', 'DNA کی ایک لڑی توڑنے کی توانائی']
_P = ['لوی چاودنه (بګ بنګ)', 'د نړۍ کلنۍ د انرژۍ لګښت', '1 kg یورانیم', '1 ټن TNT', 'په 90 km/h کې 1000 kg موټر', 'په 100 km/h کې د ټېنس توپ', 'د تلویزیون په پرده کې یو الکترون', 'د DNA د یوه تار د ماتولو انرژي']
SECTIONS = [
    ('6.4-gpe', ('6.4 Potential energy (continued)', '6.4 مخفی توانائی (جاری)', '6.4 ذخیروي انرژي (دوام)'), [
        ('p', '(springs, slingshot in figure 6.5 are examples of elastic potential energy). A battery contains both chemical and electrical potential energy.', '(شکل 6.5 میں اسپرنگ اور غلیل لچکدار مخفی توانائی کی مثالیں ہیں)۔ بیٹری میں کیمیائی اور برقی دونوں مخفی توانائیاں ہوتی ہیں۔', '(په 6.5 شکل کې فنرونه او غولیل د ارتجاعي ذخیروي انرژۍ مثالونه دي). بیټرۍ کیمیاوي او برقي دواړه ذخیروي انرژۍ لري.'),
        ('p', 'Mathematically Gravitational potential energy is the product of mass ‘m’, the acceleration due to gravity ‘g’, and the change in height ‘h’.', 'ریاضیاتی طور پر تجاذبی مخفی توانائی کمیت \'m\'، کششِ ثقل کے اسراع \'g\' اور بلندی میں تبدیلی \'h\' کا حاصلِ ضرب ہے۔', 'په ریاضي ډول د جاذبې ذخیروي انرژي د کتلې \'m\'، د جاذبې تعجیل \'g\' او د لوړوالي د بدلون \'h\' حاصل ضرب دی.'),
        ('eq', None, 'E_{GPE} = mgh'),
        ('p', 'Like all energies potential energy is also a scalar quantity. For example if we lift a brick of mass 0.3 kg from the ground to 2 m high the work is done against the force of gravity, this work appears as 5.88 J of energy.', 'تمام توانائیوں کی طرح مخفی توانائی بھی غیر سمتی مقدار ہے۔ مثلاً اگر ہم 0.3 kg کمیت کی اینٹ کو زمین سے 2 m اونچا اٹھائیں تو کششِ ثقل کی قوت کے خلاف کام ہوتا ہے؛ یہ کام 5.88 J توانائی کی صورت میں ظاہر ہوتا ہے۔', 'د ټولو انرژیو په څېر ذخیروي انرژي هم سکالر کمیت دی. د مثال په توګه که د 0.3 kg کتلې خښته له ځمکې 2 m لوړ پورته کړو، د جاذبې د قوت پر وړاندې کار کېږي؛ دا کار د 5.88 J انرژۍ په بڼه ښکاري.'),
        ('fig', 'Figure 6.6: a hand lifting a 0.3 kg brick 2 m above the ground.', 'شکل 6.6: ایک ہاتھ 0.3 kg کی اینٹ کو زمین سے 2 m اوپر اٹھا رہا ہے۔', '6.6 شکل: یو لاس د 0.3 kg خښته له ځمکې 2 m پورته کوي.'),
        ('h', 'Mathematical proof:', 'ریاضیاتی ثبوت:', 'ریاضي ثبوت:'),
        ('p', 'consider an object of mass ‘m’ being lifted vertically by a force ‘F’ to height ‘h’ as shown in figure 6.7. The work done by the force F is given by equation.', 'کمیت \'m\' کے ایک جسم پر غور کریں جسے قوت \'F\' سے عموداً بلندی \'h\' تک اٹھایا جاتا ہے جیسا کہ شکل 6.7 میں ہے۔ قوت F کا کیا گیا کام مساوات سے ملتا ہے۔', 'د \'m\' کتلې یو جسم په پام کې ونیسئ چې د \'F\' قوت په واسطه عمودي \'h\' لوړوالي ته پورته کېږي لکه په 6.7 شکل کې. د F قوت ترسره شوی کار په معادله ورکول کېږي.'),
        ('eq', None, 'W = E_{GPE} = F × S', '1'),
        ('p', 'Since the force in this case is equal to its weight', 'چونکہ اس صورت میں قوت اس کے وزن کے برابر ہے', 'څرنګه چې په دې حالت کې قوت د هغه له وزن سره مساوي دی'),
        ('eq', None, 'F = W = mg', '2'),
        ('fig', 'Figure 6.7: a mass m lifted from the ground to height h; F = W = mg.', 'شکل 6.7: کمیت m کو زمین سے بلندی h تک اٹھایا گیا؛ F = W = mg۔', '6.7 شکل: m کتله له ځمکې h لوړوالي ته پورته شوې؛ F = W = mg.'),
        ('tab', 'phys9-u6-table62', 'TABLE 6.2: Energy of Various Objects and Phenomena', ['Object/phenomenon', 'Energy in joules'], _R,
         (['جسم/مظہر', 'توانائی جول میں'], [[u, r[1]] for r, u in zip(_R, _U)]), (['جسم/پدیده', 'انرژي په ژول'], [[p, r[1]] for r, p in zip(_R, _P)])),
        ('p', 'Here the distance moved is the height ‘h’', 'یہاں طے کیا گیا فاصلہ بلندی \'h\' ہے', 'دلته وهل شوی واټن لوړوالی \'h\' دی'),
        ('eq', None, 'S = h', '3'),
    ]),
]
