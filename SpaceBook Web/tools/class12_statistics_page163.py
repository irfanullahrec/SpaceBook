"""PDF163 printed 317–318: Unit 9 Exercise questions 9.17–9.22 (data tables)."""
from class12_statistics_common import Builder, save

b = Builder()


def raw(tid, rows):
    H = [''] * len(rows[0])
    b.table(tid, H, rows, H, H, rows, rows, noHeader=True)


def hdr(tid, heads, rows):
    b.table(tid, [h[0] for h in heads], rows, [h[1] for h in heads], [h[2] for h in heads], rows, rows)


b.p('9.17 The following data gives the figures of production of rice of three varieties A, B, C of rice shown in 12 plots', '9.17 درج ذیل مواد 12 قطعات میں بوئی گئی چاول کی تین اقسام A، B، C کی پیداوار کے اعداد دیتا ہے', '9.17 لاندې معلومات په 12 ټوټو کې کرل شویو د وریجو د درېیو ډولونو A، B، C د تولید شمېرې ورکوي')
raw('stat12-t-q9-17', [['A', '18', '15', '24', '23'], ['B', '19', '23', '24', '18'], ['C', '16', '19', '31', '22']])
b.p('Carry out the analysis of variance and test 5% level of significance that is there a significant difference among varieties?', 'تجزیۂ تغیر کریں اور 5% معنویت کی سطح پر جانچ کریں کہ کیا اقسام کے درمیان معنی خیز فرق ہے؟', 'د واریانس تحلیل ترسره کړئ او د 5% معنی‌داریت په کچه وازموئ چې آیا د ډولونو ترمنځ معنی‌دار توپیر شته؟')
b.p('9.18 The three samples below have been obtained from normal populations with equal variances. Test the hypothesis at 5% level of significance that the population means are equal.', '9.18 نیچے دیے گئے تین نمونے برابر تغیرات والی نارمل آبادیوں سے حاصل کیے گئے ہیں۔ 5% معنویت کی سطح پر اس مفروضے کی جانچ کریں کہ آبادیوں کے اوسط برابر ہیں۔', '9.18 لاندې درې نمونې د برابرو واریانسونو لرونکو نورمالو نفوسونو څخه ترلاسه شوې. د 5% معنی‌داریت په کچه دا فرضیه وازموئ چې د نفوسونو منځني برابر دي.')
X = ('$X_1$',) * 3, ('$X_2$',) * 3, ('$X_3$',) * 3
hdr('stat12-t-q9-18', X, [['10', '5', '9'], ['8', '7', '12'], ['7', '10', '13'], ['14', '9', '12'], ['11', '9', '14']])
b.p('9.19 A test was given to 5 students chosen at random from the first year statistics class each of the three colleges in Peshawar. Their scores were found as follow.', '9.19 پشاور کے تین کالجوں میں سے ہر ایک کی فرسٹ ایئر شماریات کی جماعت سے تصادفی طور پر منتخب 5 طلبہ کا ٹیسٹ لیا گیا۔ ان کے نمبر درج ذیل پائے گئے۔', '9.19 د پېښور د درېیو کالجونو له هر یوه د لومړي کال د احصایې له ټولګي په تصادفي ډول ټاکل شویو 5 زده کوونکو ته ازموینه ورکړل شوه. د دوی نمرې په لاندې ډول وموندل شوې.')
raw('stat12-t-q9-19', [['A', '50', '80', '90', '70', '60'], ['B', '40', '50', '70', '40', '50'], ['C', '70', '60', '60', '50', '60']])
b.p('Perform analysis of variance and show if there is any significant difference among the score of students in the three colleges. Use α = 0.05', 'تجزیۂ تغیر کریں اور دکھائیں کہ کیا تینوں کالجوں کے طلبہ کے نمبروں میں کوئی معنی خیز فرق ہے۔ α = 0.05 استعمال کریں', 'د واریانس تحلیل ترسره کړئ او وښایاست چې آیا د درېیو کالجونو د زده کوونکو په نمرو کې کوم معنی‌دار توپیر شته. α = 0.05 وکاروئ')
b.p('9.20 Test the hypothesis that no differences exist among the four treatments at α = 0.05.', '9.20 α = 0.05 پر اس مفروضے کی جانچ کریں کہ چاروں علاج کے درمیان کوئی فرق نہیں۔', '9.20 په α = 0.05 دا فرضیه وازموئ چې د څلورو درملنو ترمنځ هېڅ توپیر نشته.')
S = lambda k: (f'Sample {k}', f'نمونہ {k}', f'نمونه {k}')
hdr('stat12-t-q9-20', [S(1), S(2), S(3), S(4)], [['5', '3', '4', '8'], ['4', '6', '11', '18'], ['4', '4', '8', '14'], ['11', '6', '6', '27']])
b.p('9.21 Given the following data obtained from a completely randomized design with four treatments;', '9.21 چار علاج والے مکمل تصادفی ڈیزائن سے حاصل کردہ درج ذیل مواد دیا گیا ہے؛', '9.21 د څلورو درملنو لرونکي بشپړ تصادفي ډیزاین څخه ترلاسه شوي لاندې معلومات ورکړل شوي؛')
hdr('stat12-t-q9-21', [('$X_1$',) * 3, ('$X_2$',) * 3, ('$X_3$',) * 3, ('$X_4$',) * 3], [['12.4', '14.4', '10.2', '6.1'], ['20.9', '9.0', '13.2', '5.8'], ['10.1', '23.7', '5.1', '4.8'], ['4.2', '', '', '1.5']])
b.p('Analyse the given data and draw conclusion about the equality of treatment effects. Use α = 0.05', 'دیے گئے مواد کا تجزیہ کریں اور علاج کے اثرات کی برابری کے بارے میں نتیجہ اخذ کریں۔ α = 0.05 استعمال کریں', 'ورکړل شوي معلومات تحلیل کړئ او د درملنو د اغېزو د برابرۍ په اړه پایله واخلئ. α = 0.05 وکاروئ')
b.p('9.22 The following data were obtained by using completely randomized design', '9.22 درج ذیل مواد مکمل تصادفی ڈیزائن استعمال کر کے حاصل کیا گیا', '9.22 لاندې معلومات د بشپړ تصادفي ډیزاین په کارولو ترلاسه شول')
R22 = lambda w: [[f'{w} 1', '6', '8', '10', '8'], [f'{w} 2', '8', '10', '9', ''], [f'{w} 3', '10', '8', '', ''], [f'{w} 4', '9', '10', '7', '8'], [f'{w} 5', '8', '10', '12', '']]
H = [''] * 5
b.table('stat12-t-q9-22', H, R22('Sample'), H, H, R22('نمونہ'), R22('نمونه'), noHeader=True)
ex = b.build('stat12-u9-exercise-c', 'Unit 9 Exercise — 9.17 to 9.22', 'یونٹ 9 مشق — 9.17 تا 9.22', 'واحد 9 تمرین — 9.17 تر 9.22', 163, [317, 318])

if __name__ == '__main__':
    save(163, [(9, ex)])
