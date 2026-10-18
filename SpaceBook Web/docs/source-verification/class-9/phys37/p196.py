# -*- coding: utf-8 -*-
TITLE = 'Young\'s modulus Eq 7.9 / Table 7.2 / stress-strain curves Figure 7.11 / Lab work'
_R = [['Aluminum', '7.0 × 10^10'], ['Brass', '9.0 × 10^10'], ['Copper', '11 × 10^10'], ['Crown glass', '6.0 × 10^10'], ['Iron', '21 × 10^10'], ['Lead', '1.6 × 10^10'], ['Nickel', '21 × 10^10'], ['Steel', '20 × 10^10']]
_U = ['ایلومینیم', 'پیتل', 'تانبا', 'کراؤن گلاس', 'لوہا', 'سیسہ', 'نکل', 'فولاد']
_P = ['المونیم', 'برنج', 'مس', 'کراون ښیښه', 'اوسپنه', 'سرب', 'نکل', 'فولاد']
SECTIONS = [
    ('7.10-ym', ('Young’s modulus (continued)', 'ینگ کا معیار (جاری)', 'د ینګ ماډولس (دوام)'), [
        ('p', 'the limit of proportionality. Within this limit, the ratio is a constant whose value depends on the material of the wire, and is known as the Young’s modulus of the material. Mathematically', 'تناسب کی حد کے اندر۔ اس حد کے اندر یہ نسبت ایک مستقل ہے جس کی قدر تار کے مادے پر منحصر ہے، اور اسے مادے کا ینگ کا معیار کہتے ہیں۔ ریاضیاتی طور پر', 'د تناسب په حد کې. په دې حد کې نسبت یو ثابت دی چې ارزښت یې د سیم په ماده پورې اړه لري، او د مادې د ینګ ماډولس بلل کېږي. په ریاضي ډول'),
        ('eq', None, 'Stress ∝ Strain'),
        ('eq', None, 'or   Stress = Constant × Strain'),
        ('p', 'Constant of proportionality is called Young’s modulus is denoted by Y', 'تناسب کا مستقل ینگ کا معیار کہلاتا ہے اور Y سے ظاہر کیا جاتا ہے', 'د تناسب ثابت د ینګ ماډولس بلل کېږي او په Y ښودل کېږي'),
        ('eq', None, 'Stress = Young’s Modulus × Strain'),
        ('p', 'rearranging the above equation, we get', 'اوپر والی مساوات کو ترتیب دینے سے', 'د پورتنۍ معادلې په بیا ترتیبولو سره'),
        ('eq', None, 'Young’s Modulus = [[Stress|Strain]]'),
        ('p', 'Young’s modulus is denoted by Y and its unit is Nm^{-2}, putting values of stress and strain, we get', 'ینگ کا معیار Y سے ظاہر کیا جاتا ہے اور اس کی اکائی Nm^{-2} ہے، تناؤ اور اسٹرین کی قدریں رکھنے سے', 'د ینګ ماډولس په Y ښودل کېږي او واحد یې Nm^{-2} دی، د سټرېس او سټرېن د ارزښتونو په ایښودلو'),
        ('eq', None, 'Y = [[F/A|x/l]]'),
        ('eq', 'phys9-u7-eq79', 'rearranging   Y = [[F × l|A × x]]', '7.9'),
        ('p', 'Young Modulus for different materials are given in the table 7.2.', 'مختلف مادوں کے لیے ینگ کا معیار جدول 7.2 میں دیا گیا ہے۔', 'د بېلابېلو موادو لپاره د ینګ ماډولس په 7.2 جدول کې ورکړل شوی.'),
        ('tab', 'phys9-u7-table72', 'Modulus for Selected Materials [Table 7.2]', ['Material', 'Young Modulus, Y, (Pa)'], _R,
         (['مادہ', 'ینگ کا معیار، Y، (Pa)'], [[u, r[1]] for r, u in zip(_R, _U)]), (['ماده', 'د ینګ ماډولس، Y، (Pa)'], [[p, r[1]] for r, p in zip(_R, _P)])),
    ]),
    ('7.10-curve', ('Stress strain curves', 'تناؤ اور اسٹرین کے منحنی خطوط', 'د سټرېس او سټرېن منحنیګانې'), [
        ('p', 'Stress and strain curves are measured by stress tester.', 'تناؤ اور اسٹرین کے منحنی خطوط اسٹریس ٹیسٹر سے ناپے جاتے ہیں۔', 'د سټرېس او سټرېن منحنیګانې د سټرېس ټیسټر په واسطه اندازه کېږي.'),
        ('p', 'The applied stress is increased and the change in length is noted. The values are then printed on graph. A typical graph for metal is shown in the figure 7.11.', 'لگایا گیا تناؤ بڑھایا جاتا ہے اور لمبائی میں تبدیلی نوٹ کی جاتی ہے۔ پھر قدریں گراف پر درج کی جاتی ہیں۔ دھات کا ایک عام گراف شکل 7.11 میں دکھایا گیا ہے۔', 'اچول شوی سټرېس زیاتېږي او په اوږدوالي کې بدلون یادېږي. بیا ارزښتونه پر ګراف لیکل کېږي. د فلز یو عادي ګراف په 7.11 شکل کې ښودل شوی.'),
        ('p', 'Here, Point A, is the limit of proportionality, the limit up to which Hooke’s law is obeyed called proportional limit.', 'یہاں نقطہ A تناسب کی حد ہے، وہ حد جہاں تک ہُک کے قانون کی پابندی ہوتی ہے، اسے تناسبی حد کہتے ہیں۔', 'دلته A ټکی د تناسب حد دی، هغه حد چې تر هغه پورې د هوک قانون پلی کېږي، تناسبي حد بلل کېږي.'),
        ('fig', 'Figure 7.11 Stress strain curve — stress (vertical) against strain (horizontal) from O: rising straight to A, then to B (end of the elastic region), up to the maximum C and down to D in the plastic region.', 'شکل 7.11 تناؤ اسٹرین منحنی — O سے تناؤ (عمودی) بمقابلہ اسٹرین (افقی): سیدھا A تک، پھر B تک (لچکدار علاقے کا اختتام)، زیادہ سے زیادہ C تک اور پلاسٹک علاقے میں D تک نیچے۔', '7.11 شکل د سټرېس سټرېن منحني — له O څخه سټرېس (عمودي) د سټرېن (افقي) په وړاندې: تر A مستقیم، بیا تر B (د ارتجاعي سیمې پای)، تر اعظمي C او په پلاستیکي سیمه کې تر D ښکته.'),
        ('h', 'LAB WORK', 'لیب ورک', 'لابراتواري کار'),
        ('p', 'To study the relation between load and extension (helical spring) by drawing graph.', 'گراف بنا کر بوجھ اور لمبائی میں اضافے (پیچ دار اسپرنگ) کے درمیان تعلق کا مطالعہ کرنا۔', 'د ګراف په رسمولو سره د بار او غځېدنې (مارپېچ فنر) ترمنځ د اړیکې مطالعه.'),
    ]),
]
