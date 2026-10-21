"""Numbers and Latin words of a scan vs the data (for Urdu-source books where the Urdu text cannot be OCR'd here).

    python tools/qa/digits_check.py <page_text.json> <ocr dir> [--urdu-data <urdu page_text.json>]

RapidOCR reads digits and Latin letters on an Urdu page reliably. Numbers (>= 2 digits, decimals kept; Arabic-Indic and Persian digits are
converted) that the scan shows on page N but that occur in no data string of pages N-2..N+2 are listed ("scan-only"), and the numbers of the
data that occur in no OCR page N-2..N+2 ("data-only"). Each line is then opened next to its scan."""
import sys, os, re, json

TR = str.maketrans('٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹', '01234567890123456789')


def nums(s):
    s = s.translate(TR)
    return set(re.findall(r'\d+(?:[.,]\d+)?', s.replace(',', '.') if False else s))


pt, od = sys.argv[1], sys.argv[2]
pages = json.load(open(pt, encoding='utf8'))
if '--urdu-data' in sys.argv:
    for k, v in json.load(open(sys.argv[sys.argv.index('--urdu-data') + 1], encoding='utf8')).items(): pages.setdefault(k, []).extend(v)
dn = {int(k): set().union(*[nums(s) for s in v]) if v else set() for k, v in pages.items()}
on = {}
for f in os.listdir(od):
    m = re.match(r'p(\d+)\.txt$', f)
    if m: on[int(m.group(1))] = nums(open(os.path.join(od, f), encoding='utf8').read())
tot_s = tot_d = 0
for n in sorted(on):
    near_d = set().union(*[dn.get(k, set()) for k in range(n - 2, n + 3)])
    near_o = set().union(*[on.get(k, set()) for k in range(n - 2, n + 3)])
    so = sorted(x for x in on[n] if len(x) >= 2 and x not in near_d)
    do = sorted(x for x in dn.get(n, set()) if len(x) >= 2 and x not in near_o)
    tot_s += len(so); tot_d += len(do)
    if so or do: print('p%d scan-only: %s | data-only: %s' % (n, ' '.join(so[:12]), ' '.join(do[:12])))
print('totals scan-only', tot_s, 'data-only', tot_d)
