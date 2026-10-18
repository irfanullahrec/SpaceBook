"""Economics XII PDF158: pp.296–297 — summary of the budget for the fiscal year 2018-19 (points 1–11) and the structured table
“Budget at a glance”; examination papers title page. Run: python class12_eco_page158.py"""
from class12_eco_common import BOOK, Builder, P, L

PTS = [
 ('1. The total volume of the budget 2018-19 is 5,932.5 billion rupees. This budget is 16.2 per cent more than the previous fiscal year.', '1۔ بجٹ 2018-19ء کا کل حجم 5932.5 بلین روپیہ ہے۔ یہ بجٹ سابقہ مالی سال سے 16.2 فیصد زیادہ ہے۔', '۱. د ۲۰۱۸-۱۹ بودجې ټول حجم ۵۹۳۲.۵ بلیونه روپۍ دی. دا بودجه له تېر مالي کال ۱۶.۲ سلنه زیاته ده.'),
 ('2. The net revenue has been estimated at 3,070.4 billion rupees, which is 4.9 per cent more than the previous fiscal year.', '2۔ خالص محاصل کا اندازہ 3070.4 بلین روپیہ لگایا گیا ہے، جو کہ پچھلے مالی سال سے 4.9 فیصد زیادہ ہے۔', '۲. خالص عواید ۳۰۷۰.۴ بلیونه روپۍ اټکل شوي، چې له تېر مالي کال ۴.۹ سلنه زیات دي.'),
 ('3. The estimate of the provinces’ share in federal taxes is 2,590.1 billion rupees, which is 8.6 per cent more than last year.', '3۔ وفاقی ٹیکسوں میں صوبوں کے حصے کا تخمینہ 2590.1 بلین روپیہ ہے، جو کہ پچھلے سال سے 8.6 فیصد زیادہ ہے۔', '۳. په فدرالي مالیو کې د ولایتونو د ونډې اټکل ۲۵۹۰.۱ بلیونه روپۍ دی، چې له تېر کال ۸.۶ سلنه زیات دی.'),
 ('4. The estimate of net capital receipts is 443.1 billion rupees, which is 19.8 per cent less than the previous fiscal year.', '4۔ خالص سرمایاتی وصولیوں کا اندازہ 443.1 بلین روپے ہے، جو کہ پچھلے مالی سال سے 19.8 فیصد کم ہے۔', '۴. د خالصو پانګیزو اخیستنو اټکل ۴۴۳.۱ بلیونه روپۍ دی، چې له تېر مالي کال ۱۹.۸ سلنه کم دی.'),
 ('5. The estimate of external receipts is 1,118 billion rupees, which is 33.4 per cent more than the previous fiscal year.', '5۔ بیرونی وصولیوں کا تخمینہ 1118 بلین روپے ہے، جو کہ سابقہ مالی سال سے 33.4 فیصد زیادہ ہے۔', '۵. د بهرنیو اخیستنو اټکل ۱۱۱۸ بلیونه روپۍ دی، چې له تېر مالي کال ۳۳.۴ سلنه زیات دی.'),
 ('6. The estimate of total expenditure is 5,932.5 billion rupees, of which 4,780.4 billion rupees will be non-development and 1,152.1 billion rupees development expenditure.', '6۔ مجموعی اخراجات کا تخمینہ 5932.5 بلین روپے ہے، جس میں سے 4780.4 بلین روپے غیر ترقیاتی جبکہ 1152.1 بلین روپے ترقیاتی اخراجات ہوں گے۔', '۶. د ټولو لګښتونو اټکل ۵۹۳۲.۵ بلیونه روپۍ دی، چې له هغې ۴۷۸۰.۴ بلیونه روپۍ غیرپراختیايي او ۱۱۵۲.۱ بلیونه روپۍ پراختیايي لګښتونه به وي.'),
 ('7. In this way the ratio of non-development and development expenditure will be respectively 80.4 per cent and 19.4 per cent.', '7۔ اس طرح غیر ترقیاتی اور ترقیاتی اخراجات کی شرح بالترتیب 80.4 فیصد اور 19.4 فیصد ہو گی۔', '۷. په دې ډول د غیرپراختیايي او پراختیايي لګښتونو نرخ په ترتیب سره ۸۰.۴ سلنه او ۱۹.۴ سلنه به وي.'),
 ('8. Out of non-development expenditure, 3,340.4 billion rupees will be spent on general public services.', '8۔ غیر ترقیاتی اخراجات میں سے 3340.4 بلین روپے جنرل پبلک سروسز پر خرچ ہوں گے۔', '۸. له غیرپراختیايي لګښتونو ۳۳۴۰.۴ بلیونه روپۍ به پر عمومي عامه خدمتونو ولګېږي.'),
 ('9. Besides the Public Sector Development (PSDP), development expenditure will be 180.2 billion rupees, which is 18.4 per cent more than last year.', '9۔ پبلک سیکٹر ڈویلپمنٹ (PSDP) کے علاوہ ترقیاتی خرچہ 180.2 بلین روپے ہو گا، جو کہ پچھلے سال سے 18.4 فیصد زیادہ ہے۔', '۹. د عامې برخې له پراختیا (PSDP) پرته پراختیايي لګښت به ۱۸۰.۲ بلیونه روپۍ وي، چې له تېر کال ۱۸.۴ سلنه زیات دی.'),
 ('10. The volume of the PSDP is 1,650 billion rupees, of which 850 billion rupees will be distributed among the provinces.', '10۔ PSDP کا حجم 1650 بلین روپے ہے، جس میں سے 850 بلین روپے صوبوں میں تقسیم کیے جائیں گے۔', '۱۰. د PSDP حجم ۱۶۵۰ بلیونه روپۍ دی، چې له هغې ۸۵۰ بلیونه روپۍ به پر ولایتونو ووېشل شي.'),
 ('11. To meet the expenditure 4,917.2 billion rupees will be available, whereas 1,015.3 billion rupees will be borrowed from banks.', '11۔ اخراجات کو پورا کرنے کے لیے 4917.2 بلین روپے دستیاب ہوں گے جبکہ 1015.3 بلین روپے کا بنکوں سے قرض لیا جائے گا۔', '۱۱. د لګښتونو د پوره کولو لپاره ۴۹۱۷.۲ بلیونه روپۍ به شتون ولري، حال دا چې ۱۰۱۵.۳ بلیونه روپۍ به له بانکونو پور اخیستل کېږي.')]

# Budget at a glance (Rs. in billion), printed in English
ROWS = [('TAX REVENUE', '4,888.6', 'A. CURRENT', '4,178.6'),
        ('- FBR Taxes', '4,435.0', 'Interest Payments', '1,620.2'),
        ('- Other Taxes', '453.6', 'Pension', '342.0'),
        ('- NON-TAX REVENUE', '771.9', 'Defence Affairs & Services', '1,100.3'),
        ('(a) Gross Revenue Receipts', '5,660.5', 'Grants and Transfers', '477.9'),
        ('(b) Less Provincial Share', '2,590.1', 'Subsidies', '174.7'),
        ('I. Net Revenue Receipts (a-b)', '3,070.4', 'Running of Civil Govt.', '463.4'),
        ('II. Capital Receipts (Non-Bank)', '532.8', '', ''),
        ('III. External Receipts (net)', '342.1', 'B. DEVELOPMENT', '1,067.6'),
        ('IV. Estimated Provincial Surplus', '285.6', 'Federal PSDP', '800.0'),
        ('V. Bank Borrowing', '1,015.3', 'Net Lending', '87.4'),
        ('VI. Privatization Proceeds', '0.0', 'Other Dev. Expenditure', '180.2'),
        ('TOTAL RESOURCES (I to VI)', '5,246.2', 'TOTAL EXPENDITURE (A+B)', '5,246.2')]
UR = {'TAX REVENUE': 'ٹیکس محاصل', '- FBR Taxes': '- ایف بی آر ٹیکس', '- Other Taxes': '- دیگر ٹیکس', '- NON-TAX REVENUE': '- غیر ٹیکس محاصل',
      '(a) Gross Revenue Receipts': '(a) مجموعی محصولاتی وصولیاں', '(b) Less Provincial Share': '(b) منفی صوبائی حصہ', 'I. Net Revenue Receipts (a-b)': 'I. خالص محصولاتی وصولیاں (a-b)',
      'II. Capital Receipts (Non-Bank)': 'II. سرمایاتی وصولیاں (غیر بنک)', 'III. External Receipts (net)': 'III. بیرونی وصولیاں (خالص)', 'IV. Estimated Provincial Surplus': 'IV. متوقع صوبائی فاضل',
      'V. Bank Borrowing': 'V. بنک قرضہ', 'VI. Privatization Proceeds': 'VI. نجکاری سے آمدنی', 'TOTAL RESOURCES (I to VI)': 'کل وسائل (I تا VI)',
      'A. CURRENT': 'A. رواں', 'Interest Payments': 'سود کی ادائیگیاں', 'Pension': 'پنشن', 'Defence Affairs & Services': 'دفاعی امور و خدمات', 'Grants and Transfers': 'گرانٹس اور منتقلیاں',
      'Subsidies': 'اعانے', 'Running of Civil Govt.': 'سول حکومت کا انتظام', 'B. DEVELOPMENT': 'B. ترقیاتی', 'Federal PSDP': 'وفاقی PSDP', 'Net Lending': 'خالص قرض دہی',
      'Other Dev. Expenditure': 'دیگر ترقیاتی اخراجات', 'TOTAL EXPENDITURE (A+B)': 'کل اخراجات (A+B)', '': ''}
PS = {'TAX REVENUE': 'مالیاتي عواید', '- FBR Taxes': '- د FBR مالیې', '- Other Taxes': '- نورې مالیې', '- NON-TAX REVENUE': '- غیرمالیاتي عواید',
      '(a) Gross Revenue Receipts': '(a) ټول عوایدي اخیستنې', '(b) Less Provincial Share': '(b) منفي ولایتي ونډه', 'I. Net Revenue Receipts (a-b)': 'I. خالص عوایدي اخیستنې (a-b)',
      'II. Capital Receipts (Non-Bank)': 'II. پانګیزې اخیستنې (غیربانکي)', 'III. External Receipts (net)': 'III. بهرنۍ اخیستنې (خالص)', 'IV. Estimated Provincial Surplus': 'IV. اټکل شوی ولایتي اضافه',
      'V. Bank Borrowing': 'V. بانکي پور', 'VI. Privatization Proceeds': 'VI. د خصوصي کولو عاید', 'TOTAL RESOURCES (I to VI)': 'ټولې سرچینې (I تر VI)',
      'A. CURRENT': 'A. روان', 'Interest Payments': 'د سود ورکړې', 'Pension': 'تقاعد', 'Defence Affairs & Services': 'دفاعي چارې او خدمتونه', 'Grants and Transfers': 'مرستې او لېږدونې',
      'Subsidies': 'سبسایډي', 'Running of Civil Govt.': 'د ملکي حکومت چلول', 'B. DEVELOPMENT': 'B. پراختیايي', 'Federal PSDP': 'فدرالي PSDP', 'Net Lending': 'خالص پور ورکول',
      'Other Dev. Expenditure': 'نور پراختیايي لګښتونه', 'TOTAL EXPENDITURE (A+B)': 'ټول لګښتونه (A+B)', '': ''}


def p158():
    b = Builder()
    b.h('Summary of the budget for the fiscal year 2018-19', 'خلاصہ بجٹ برائے مالی سال 2018-19', 'د ۲۰۱۸-۱۹ مالي کال د بودجې لنډیز')
    L(b, PTS)
    b.h('Budget at a glance for the fiscal year 2018-19 (Rs. in billion)', 'BUDGET AT A GLANCE FOR THE FISCAL YEAR 2018-19 (Rs. in Billion)', 'د ۲۰۱۸-۱۹ مالي کال بودجه په یوه نظر (میلیارده روپۍ)')
    b.table('eco12-appx-table1', ['Receipts', 'Rs. bn', 'Expenditure', 'Rs. bn'], [list(r) for r in ROWS],
            ['وصولیاں', 'بلین روپے', 'اخراجات', 'بلین روپے'], ['اخیستنې', 'میلیارده روپۍ', 'لګښتونه', 'میلیارده روپۍ'],
            [[UR[r[0]], r[1], UR[r[2]], r[3]] for r in ROWS], [[PS[r[0]], r[1], PS[r[2]], r[3]] for r in ROWS])
    r1 = BOOK.record(b, 'eco12-appx-2', 'Appendix — budget 2018-19', 'ضمیمہ — بجٹ 2018-19ء', 'ضمیمه — د ۲۰۱۸-۱۹ بودجه', 158, [296])
    t = Builder()
    t.h('Examination papers', 'پرچہ جات', 'د ازموینې پرچې')
    P(t, [('(Title page of the section of past examination papers.)', '(سابقہ امتحانی پرچہ جات کے حصے کا سرورق۔)', '(د تېرو ازموینو د پرچو د برخې سرپاڼه.)')])
    r2 = BOOK.record(t, 'eco12-papers-0', 'Examination papers — title page', 'پرچہ جات — سرورق', 'د ازموینې پرچې — سرپاڼه', 158, [297])
    BOOK.save(158, [(14, r1), (14, r2)], issues=[{'id': 'eco12-pdf158', 'unit': 14, 'printedPage': 296,
               'description': 'Budget summary and table printed as in the source. The summary gives total budget 5,932.5 billion while the table totals 5,246.2 billion (different bases) — both kept as printed. The table is printed in English and transcribed as structured data with translated row labels.'}])


if __name__ == '__main__':
    p158()
