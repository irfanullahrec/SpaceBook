"""Helpers that print DSL lines for routine Class 5 exercise solutions (number words, expanded form, ...).

Usage: gen5.py words 290014 433453 ...      -> 'qp' answer lines (sol) for "write in words"
       gen5.py expand 131441 ...             -> sol lines for "expanded form"
Output lines are pasted after the matching `qp` line; check them against the printed answer key.
"""
import sys

ONES = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def under100(n):
    if n < 20:
        return ONES[n]
    t, o = divmod(n, 10)
    return TENS[t] + ('-' + ONES[o] if o else '')


def under1000(n, glue=True):
    h, r = divmod(n, 100)
    out = []
    if h:
        out.append(ONES[h] + ' hundred')
    if r:
        out.append(('and ' if h and glue else '') + under100(r))
    return ' '.join(out)


def words(n):
    """Book style: 'one million four hundred and fifty-six thousand, nine hundred and seven'."""
    if n == 0:
        return 'zero'
    m, r = divmod(n, 1_000_000)
    th, u = divmod(r, 1000)
    head = ' '.join(x for x in [under1000(m) + ' million' if m else '', under1000(th) + ' thousand' if th else ''] if x)
    if not u:
        return head
    if not head:
        return under1000(u)
    return head + (', ' + under1000(u) if u >= 100 else ' and ' + under1000(u))


def fmt(n):
    return f'{n:,}'


def tex(n):
    return f'{n:,}'.replace(',', '{,}')


def expanded(n):
    s = str(n)
    terms = [int(d) * 10 ** (len(s) - i - 1) for i, d in enumerate(s)]
    return ' + '.join(tex(t) for t in terms if t) or '0'


def coltable(rows, ops, labels=None, notes=None, cap=''):
    """rows: digit strings (commas kept as part of the digit they follow); ops: per-row sign ('', '+', '×', '−', '=')."""
    def cells(r):
        out = []
        for ch in r:
            if ch == ',' and out:
                out[-1] += ','
            else:
                out.append(ch)
        return out
    cs = [cells(r) for r in rows]
    w = max(len(c) for c in cs)
    lines = ['table' + (' ' + cap if cap else '')]
    for i, c in enumerate(cs):
        row = [labels[i] if labels else None, ops[i]] + [''] * (w - len(c)) + c + ([notes[i]] if notes else [])
        row = [x for x in row if x is not None]
        lines.append('tr | ' + ' | '.join(row))
    lines.append('endtable')
    return chr(10).join(lines)


def longmul(a, b, labels=None):
    """Book layout: partial products of a by each digit of b (ones first, shifted with zeros), then the total."""
    sb = str(b)
    parts = [a * int(d) * 10 ** (len(sb) - 1 - i) for i, d in enumerate(sb)][::-1]
    parts = [p for p in parts if p] if len(parts) > 1 else parts
    rows = [str(a), str(b)] + [str(p) for p in parts] + [str(a * b)]
    ops = ['', '×'] + [''] * (len(parts) - 1) + ['+', '=']
    lab = None
    if labels:
        lab = [labels[0], labels[1]] + [''] * len(parts) + [labels[2]]
    return coltable(rows, ops, lab)


def main():
    kind, *nums = sys.argv[1:]
    for x in nums:
        n = int(x.replace(',', ''))
        if kind == 'mul':
            print(longmul(n, int(nums[1]))); return
        if kind == 'words':
            w = words(n)
            w = w[0].upper() + w[1:]
            print(f'sol {w} ## Group the digits in periods from the right ({fmt(n)}) and read each period with its name (million, thousand). || دائیں طرف سے ہندسوں کے گروپ بنائیں ({fmt(n)}) اور ہر گروپ کو اس کے نام (ملین، ہزار) کے ساتھ پڑھیں۔ || له ښي لوري رقمونه په ډلو ووېشئ ({fmt(n)}) او هره ډله د خپل نوم (ملیون، زر) سره ولولئ.')
        elif kind == 'places':
            st = str(n); names = ['ones', 'tens', 'hundreds', 'thousands', 'ten thousands', 'hundred thousands', 'millions']
            vals = '; '.join(f'{d} → {tex(int(d) * 10 ** (len(st) - i - 1))}' for i, d in enumerate(st))
            print(f'sol ${vals}$ ## Place value = digit × value of its place (ones, tens, hundreds, thousands, ...). || مقامی قیمت = ہندسہ × اس کے مقام کی قیمت (اکائی، دہائی، سینکڑہ، ہزار، ...)۔ || مکاني ارزښت = رقم × د هغه د ځای ارزښت (یوونه، لسګونه، سلګونه، زرګونه، ...).')
        elif kind == 'expand':
            print(f'sol ${tex(n)} = {expanded(n)}$ ## Write each non-zero digit times its place value and add them. || ہر غیر صفر ہندسے کو اس کی مقامی قیمت کے ساتھ لکھ کر جمع کریں۔ || هر غیر صفر رقم د هغه د مکاني ارزښت سره ولیکئ او جمع یې کړئ.')


if __name__ == '__main__':
    main()
