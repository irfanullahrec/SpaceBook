"""PDF87 printed 165–166: Example 5.4 solution parts (i)–(iv) — population mean/SD, 16 samples, sampling distribution, calculation table."""
from class12_statistics_common import Builder, save

X = r'\overline{X}'
x = r'\overline{x}'
SOL = ('Solution:', 'حل:', 'حل:')
b = Builder()
b.h(*SOL)
b.p('(i) Population mean is given by', '(i) آبادی کا اوسط یہ ہے', '(i) د نفوس منځنی دا دی')
b.eq(r'\mu=\frac{\Sigma x}{N}=\frac{18}{4}=4.5')
b.p('Population Standard deviation is given by', 'آبادی کا معیاری انحراف یہ ہے', 'د نفوس معیاري انحراف دا دی')
b.eq(r'\sigma=\sqrt{\frac{\Sigma x^2}{N}-\left(\frac{\Sigma x}{N}\right)^2}=\sqrt{\frac{108}{4}-\left(\frac{18}{4}\right)^2}=\sqrt{6.75}=2.598')
b.p('(ii) Possible samples in S.W.R $=N^n=4^2=16$', '(ii) S.W.R میں ممکنہ نمونے $=N^n=4^2=16$', '(ii) په S.W.R کې شونې نمونې $=N^n=4^2=16$')
rows = [['1', '2, 2', '2', '9', '6, 2', '4'], ['2', '2, 2', '2', '10', '6, 2', '4'], ['3', '2, 6', '4', '11', '6, 6', '6'], ['4', '2, 8', '5', '12', '6, 8', '7'],
        ['5', '2, 2', '2', '13', '8, 2', '5'], ['6', '2, 2', '2', '14', '8, 2', '5'], ['7', '2, 6', '4', '15', '8, 6', '7'], ['8', '2, 8', '5', '16', '8, 8', '8']]
b.table('stat12-t-ex5-4-samples', ['S.No.', 'Samples', f'${X}$', 'S.No.', 'Samples', f'${X}$'], rows,
        ['نمبر شمار', 'نمونے', f'${X}$', 'نمبر شمار', 'نمونے', f'${X}$'], ['شمېره', 'نمونې', f'${X}$', 'شمېره', 'نمونې', f'${X}$'])
b.p(f'(iii) Sampling distribution of ${X}$', f'(iii) ${X}$ کی نمونہ جاتی تقسیم', f'(iii) د ${X}$ نمونوي وېش')
tal = [['2', '||||', '4', '4/16'], ['4', '||||', '4', '4/16'], ['5', '||||', '4', '4/16'], ['6', '|', '1', '1/16'], ['7', '||', '2', '2/16'], ['8', '|', '1', '1/16'], ['Total', '', '16', '1']]
b.table('stat12-t-ex5-4-dist', [f'${X}$', 'Tally bar', '$f$', f'$f({x})$'], tal, [f'${X}$', 'ٹیلی بار', '$f$', f'$f({x})$'], [f'${X}$', 'ټلي بار', '$f$', f'$f({x})$'],
        [r if r[0] != 'Total' else ['کل'] + r[1:] for r in tal], [r if r[0] != 'Total' else ['ټول'] + r[1:] for r in tal])
b.p(f'(iv) Calculation for the mean and S.E of the sampling distribution of ${X}$', f'(iv) ${X}$ کی نمونہ جاتی تقسیم کے اوسط اور معیاری غلطی کا حساب', f'(iv) د ${X}$ د نمونوي وېش د منځني او معیاري تېروتنې محاسبه')
b.grid('stat12-t-ex5-4-calc', [f'${X}$', f'$f({x})$', f'${X}f({x})$', f'${X}^2f({x})$'],
       [['2', '4/16', '8/16', '16/16'], ['4', '4/16', '16/16', '64/16'], ['5', '4/16', '20/16', '100/16'], ['6', '1/16', '6/16', '36/16'], ['7', '2/16', '14/16', '98/16'], ['8', '1/16', '8/16', '64/16'], ['Total', '1', '72/16', '378/16']])
rec = b.build('stat12-p087-example-5-4', 'Example 5.4 — population values, samples and sampling distribution of the mean', 'مثال 5.4 — آبادی کی قیمتیں، نمونے اور اوسط کی نمونہ جاتی تقسیم', 'بېلګه 5.4 — د نفوس قیمتونه، نمونې او د منځني نمونوي وېش', 87, [165, 166])
issues = [{'id': 'stat12-p165-ex54-samples', 'unit': 5, 'printedPage': 165, 'description': 'The printed 16-sample table pairs the two children aged 2 as separate units (rows 1, 2, 5, 6 are all “2, 2”); kept as printed.'}]

if __name__ == '__main__':
    save(87, [(5, rec)], issues=issues)
