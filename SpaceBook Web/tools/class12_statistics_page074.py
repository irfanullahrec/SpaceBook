"""PDF74 printed 139–140: Table 4.2 ordinates of the standard Normal curve (z = 0 … 3.99); use of the ordinates table.
Entries are transcribed from the scan; every cell was compared against the computed ordinate and the printed
deviations (misprints) are reproduced exactly as listed in OVERRIDES and logged as a source issue."""
from math import exp, pi, sqrt
from class12_statistics_common import Builder, save

OVERRIDES = {(0.3, 8): '0.3812', (0.5, 3): '0.34674', (0.5, 8): '0.33742', (1.0, 9): '0.22203', (1.6, 4): '0.10401',
             (1.7, 8): '0.0373', (2.0, 4): '0.0489', (2.7, 6): '0.0083', (2.8, 9): '0.00614', (3.6, 3): '0.0006'}


def printed_rows():
    rows = []
    for i in range(40):
        z = round(i / 10, 1)
        cells = []
        for j in range(10):
            v = exp(-((z + j / 100) ** 2) / 2) / sqrt(2 * pi)
            cells.append(OVERRIDES.get((z, j), f'{v:.4f}'))
        rows.append([('0' if z == 0 else f'{z:.1f}')] + cells)
    return rows


b = Builder()
b.h('TABLE 4.2: Ordinates y or f(z) of the standard Normal curve at z', 'جدول 4.2: z پر معیاری نارمل منحنی کے ordinates y یا f(z)', 'جدول 4.2: په z کې د معیاري نورمال منحني اورډیناټونه y یا f(z)')
b.grid('stat12-table4-2', ['Z', '0.00', '0.01', '0.02', '0.03', '0.04', '0.05', '0.06', '0.07', '0.08', '0.09'], printed_rows())
b.h('• Use of ordinates table', '• ordinates کے جدول کا استعمال', '• د اورډیناټونو د جدول کارول')
b.p('Ordinates of the standard normal curve given in table 4.2, as usual require Z-value $Z=\\frac{X-\\mu}{\\sigma}$ rounded up to two decimal points.', 'جدول 4.2 میں دیے گئے معیاری نارمل منحنی کے ordinates کے لیے حسبِ معمول Z کی قیمت $Z=\\frac{X-\\mu}{\\sigma}$ دو اعشاری مقامات تک گول درکار ہوتی ہے۔', 'په 4.2 جدول کې ورکړل شوي د معیاري نورمال منحني اورډیناټونه د معمول سره سم د Z قیمت $Z=\\frac{X-\\mu}{\\sigma}$ ته اړتیا لري چې تر دوو اعشاري ځایونو ګرد شوی وي.')
rec = b.build('stat12-p074-table-4-2', 'Table 4.2 Ordinates of the standard normal curve', 'جدول 4.2 معیاری نارمل منحنی کے ordinates', 'جدول 4.2 د معیاري نورمال منحني اورډیناټونه', 74, [139, 140])
issues = [{'id': 'stat12-p139-table42-misprints', 'unit': 4, 'printedPage': 139, 'description': 'Table 4.2 kept as printed; misprints vs exact ordinates: z=0.38→0.3812 (0.3712), 0.53→0.34674, 0.58→0.33742, 1.09→0.22203, 1.64→0.10401, 1.78→0.0373 (0.0973), 2.04→0.0489 (0.0498), 2.76→0.0083 (0.0088), 2.89→0.00614, 3.63→0.0006 (0.0005).'}]

if __name__ == '__main__':
    save(74, [(4, rec)], issues=issues)
