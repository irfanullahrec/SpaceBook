"""PDF160 printed 311–312: Example 9.2 TrSS, ESS, ANOVA table, F = 6.461 < 7.2 (accept H0); Unit 9 key points."""
from class12_statistics_common import Builder, save
from class12_statistics_figs import chi_tail

b = Builder()
b.mlines([r'=\left[\frac{196}{5}+\frac{361}{5}+\frac{25}{4}\right]-C.F', r'=[39.2+72.2+6.25]-103.1429=14.5071', r'ESS=TSS-T_rSS', r'=26.8571-14.5071=12.35'])
b.p('Put all these values in ANOVA table we have', 'ان تمام قیمتوں کو ANOVA جدول میں رکھنے سے ہمیں ملتا ہے', 'دا ټول قیمتونه د ANOVA په جدول کې د ایښودو سره لرو')
b.p('ANOVA table', 'ANOVA جدول', 'د ANOVA جدول')
AH = ['S.O.V', 'df', 'S.S', 'M.S', 'F']
AR = lambda t, e, to: [[t, '2', '14.5071', '7.2536', '6.461'], [e, '11', '12.35', '1.1227', '—'], [to, '13', '26.8571', '—', '—']]
b.table('stat12-t-ex9-2-anova', AH, AR('Treatments', 'Error', 'Total'), AH, AH, AR('علاج', 'خطا', 'میزان'), AR('درملنې', 'تېروتنه', 'ټول'))
b.p('v. Critical region', 'v. فیصلہ کن علاقہ', 'v. بحراني سیمه')
b.vpara('stat12-ex9-2-cr', chi_tail(7.2, df=4, xmax=10, alpha='α=0.01', label='F curve with rejection region beyond 7.2, α = 0.01'),
        'Reject $H_0$ if $F_c\\ge F_{tab}$ whereas, $F_{tab}=F_{\\alpha,(\\nu_1,\\nu_2)}=F_{0.01,(2,11)}=7.2$ (From F-table 9.1)',
        '$H_0$ کو رد کریں اگر $F_c\\ge F_{tab}$ جبکہ $F_{tab}=F_{\\alpha,(\\nu_1,\\nu_2)}=F_{0.01,(2,11)}=7.2$ (F-جدول 9.1 سے)',
        '$H_0$ رد کړئ که $F_c\\ge F_{tab}$ په داسې حال کې چې $F_{tab}=F_{\\alpha,(\\nu_1,\\nu_2)}=F_{0.01,(2,11)}=7.2$ (له 9.1 F-جدول څخه)', ratio=.45)
b.p('vi. Conclusion:', 'vi. نتیجہ:', 'vi. پایله:')
b.p('Since our computed value of $F_c=6.461$ lies in the acceptance region, therefore, we accept $H_0$.', 'چونکہ ہماری معلوم کی گئی قیمت $F_c=6.461$ قبولیت کے علاقے میں ہے، لہٰذا ہم $H_0$ قبول کرتے ہیں۔', 'څرنګه چې زموږ محاسبه شوی قیمت $F_c=6.461$ د منلو په سیمه کې پروت دی، نو $H_0$ منو.')
e92 = b.build('stat12-p160-example-9-2', 'Example 9.2 — ANOVA table and conclusion', 'مثال 9.2 — ANOVA جدول اور نتیجہ', 'بېلګه 9.2 — د ANOVA جدول او پایله', 160, [311])

k = Builder()
k.h('Key points', 'اہم نکات', 'مهم ټکي')
k.group('list', [
    ('A plan of experiment in which all situations except that of treatments are kept under control as much as possible, is known as design of experiment.', 'تجربے کا وہ منصوبہ جس میں علاج کے علاوہ تمام حالات کو جہاں تک ممکن ہو قابو میں رکھا جائے، تجربے کا ڈیزائن کہلاتا ہے۔', 'د تجربې هغه پلان چې پکې د درملنو پرته ټول حالات تر وسه وسه کنټرول کې وساتل شي، د تجربې ډیزاین بلل کېږي.'),
    ('Anything whose effect is measured and is compared with others is called treatment.', 'ہر وہ چیز جس کے اثر کی پیمائش کی جائے اور دوسروں سے موازنہ کیا جائے، علاج کہلاتی ہے۔', 'هر هغه شی چې اغېز یې اندازه او له نورو سره پرتله کېږي، درملنه بلل کېږي.'),
    ('The total material or objects on which the experiment is done is known as experimental material.', 'وہ کل مواد یا اشیاء جن پر تجربہ کیا جائے تجرباتی مواد کہلاتی ہیں۔', 'هغه ټول توکي یا شیان چې تجربه پرې کېږي، تجربوي توکي بلل کېږي.'),
    ('The smallest division of an experimental material to which a treatment is applied is called experimental unit.', 'تجرباتی مواد کی سب سے چھوٹی تقسیم جس پر علاج لاگو کیا جائے تجرباتی اکائی کہلاتی ہے۔', 'د تجربوي توکو تر ټولو کوچنۍ برخه چې درملنه پرې پلي کېږي، تجربوي واحد بلل کېږي.'),
    ('The results obtained from the experimental units are called yield or responses.', 'تجرباتی اکائیوں سے حاصل ہونے والے نتائج پیداوار یا ردِعمل کہلاتے ہیں۔', 'له تجربوي واحدونو ترلاسه شوې پایلې حاصل یا غبرګونونه بلل کېږي.'),
    ('A group of homogenous experimental units e.g. land of same fertility, students of same age, weight, I.Q, etc. to which all treatment are assigned at random is called a block.', 'یکساں تجرباتی اکائیوں کا گروہ، مثلاً ایک جیسی زرخیزی والی زمین، ایک جیسی عمر، وزن، I.Q وغیرہ کے طلبہ، جن پر تمام علاج تصادفی طور پر تفویض ہوں، بلاک کہلاتا ہے۔', 'د همجنسه تجربوي واحدونو ډله، لکه د یو شان حاصلخېزۍ ځمکه، د یو شان عمر، وزن، I.Q او نورو زده کوونکي، چې ټولې درملنې ورته په تصادفي ډول ورکړل شي، بلاک بلل کېږي.'),
    ('Uniformity trial is used only for making blocks.', 'یکسانیت کا تجربہ صرف بلاک بنانے کے لیے استعمال ہوتا ہے۔', 'د یووالي ازمېښت یوازې د بلاکونو د جوړولو لپاره کارول کېږي.'),
    ('All factors which are not in the control of a researcher are called uncontrolled or extraneous factors.', 'وہ تمام عوامل جو محقق کے قابو میں نہ ہوں غیر قابو شدہ یا خارجی عوامل کہلاتے ہیں۔', 'ټول هغه عوامل چې د څېړونکي په کنټرول کې نه وي، ناکنټرول شوي یا بهرني عوامل بلل کېږي.'),
    ('The error which arises due to the extraneous factors is called experimental error.', 'خارجی عوامل کی وجہ سے پیدا ہونے والی خطا تجرباتی خطا کہلاتی ہے۔', 'هغه تېروتنه چې د بهرنیو عواملو له امله رامنځته کېږي، تجربوي تېروتنه بلل کېږي.'),
    ('Design of experiment is actually a strategy for controlling the experimental error in order to bring out the real difference among the treatments.', 'تجربے کا ڈیزائن دراصل تجرباتی خطا کو قابو کرنے کی حکمتِ عملی ہے تاکہ علاج کے درمیان حقیقی فرق سامنے آ سکے۔', 'د تجربې ډیزاین په حقیقت کې د تجربوي تېروتنې د کنټرول ستراتیژي ده ترڅو د درملنو ترمنځ ریښتینی توپیر څرګند شي.'),
    ('The allocation of treatments to experimental units in such a manner that an experimental unit has equal chance of receiving any of the treatments is called randomization.', 'تجرباتی اکائیوں کو علاج اس طرح تفویض کرنا کہ ہر تجرباتی اکائی کو کوئی بھی علاج ملنے کا برابر موقع ہو، تصادفیت کہلاتا ہے۔', 'تجربوي واحدونو ته د درملنو داسې ورکول چې هر تجربوي واحد د هرې درملنې د ترلاسه کولو برابر چانس ولري، تصادفي کول بلل کېږي.'),
    ('Repetition of a treatment on a number of experimental units in an experiment is known as replication of the treatment.', 'کسی تجربے میں متعدد تجرباتی اکائیوں پر ایک علاج کو دہرانا علاج کا تکرار کہلاتا ہے۔', 'په یوه تجربه کې پر ګڼو تجربوي واحدونو د یوې درملنې تکرارول د درملنې تکرار بلل کېږي.'),
    ('Local control also called error control reduces the experimental error.', 'مقامی کنٹرول، جسے خطا کنٹرول بھی کہتے ہیں، تجرباتی خطا کو کم کرتا ہے۔', 'سیمه‌ییز کنټرول چې د تېروتنې کنټرول هم بلل کېږي، تجربوي تېروتنه کموي.'),
    ('Experimental design in which the treatments are allocated randomly to the experimental units is called completely randomized design', 'وہ تجرباتی ڈیزائن جس میں علاج تجرباتی اکائیوں کو تصادفی طور پر تفویض کیے جائیں مکمل تصادفی ڈیزائن کہلاتا ہے', 'هغه تجربوي ډیزاین چې پکې درملنې تجربوي واحدونو ته په تصادفي ډول ورکول کېږي، بشپړ تصادفي ډیزاین بلل کېږي'),
    ('ANOVA is a technique which split the total variance into meaningful component variances; each gives an estimate of the population variance. The ratio of two component variances is distributed as F with corresponding degrees of freedom.', 'ANOVA ایک تکنیک ہے جو کل تغیر کو بامعنی جزوی تغیرات میں تقسیم کرتی ہے؛ ہر ایک آبادی کے تغیر کا تخمینہ دیتا ہے۔ دو جزوی تغیرات کی نسبت متعلقہ درجاتِ آزادی کے ساتھ F کے طور پر تقسیم ہوتی ہے۔', 'ANOVA یوه تخنیک ده چې ټول واریانس په معنی‌دارو برخه‌ییزو واریانسونو وېشي؛ هر یو د نفوس د واریانس اټکل ورکوي. د دوو برخه‌ییزو واریانسونو نسبت د اړوندو د ازادۍ درجو سره د F په توګه وېشل کېږي.'),
])
kp = k.build('stat12-u9-key-points', 'Unit 9 — Key points', 'یونٹ 9 — اہم نکات', 'واحد 9 — مهم ټکي', 160, [312])

if __name__ == '__main__':
    save(160, [(9, e92), (9, kp)])
