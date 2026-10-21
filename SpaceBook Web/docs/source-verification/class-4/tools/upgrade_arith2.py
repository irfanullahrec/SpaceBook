"""Worked chains for blank-style arithmetic: `A op B = __`, `a + b + c = ___` (expanded-form sums), with or without printed options.

    CLS=1 python upgrade_arith2.py [--write]      (CLS = 1..5; default 4)

The expression is cleaned (the trailing `= ___`, `= ☐`, `(a) .. (b) ..` options and `(split ...)` notes are removed), computed
exactly, and only used when it equals the number in the existing one-line answer. Mismatches are printed, never changed.
"""
import re, sys
from pathlib import Path
import arith4

HERE = arith4.HERE
BLANK = re.compile(r'\s*=\s*(?:\$\s*)?(?:_+|\\_+|☐|\?|□)[\s\S]*$')


def clean(t):
    t = t.strip()
    t = BLANK.sub('', t)
    t = re.sub(r'\s*\((?:split|a\)|b\)).*$', '', t)
    t = t.replace('$', '').strip()
    return t


def digits(s):
    return re.sub(r'\D', '', s.translate(str.maketrans('۰۱۲۳۴۵۶۷۸۹', '0123456789')))


def multi_add(t):
    parts = [x.strip() for x in t.split('+')]
    if len(parts) < 3 or any(not re.fullmatch(r'\d[\d,{}]*', x) for x in parts):
        return None
    return [arith4.num(x) for x in parts]


def build_multi(nums):
    total = sum(nums)
    q = ' + '.join(arith4.t(n) for n in nums)
    run, acc, rows = nums[0], [], []
    chain = arith4.t(nums[0])
    steps = []
    for n in nums[1:]:
        run += n
        steps.append(f'{arith4.t(run)}')
    row = q + ' = ' + ' = '.join(steps)
    en = 'Add the numbers one after another from the left.'
    ur = 'بائیں سے شروع کر کے اعداد کو ایک کے بعد ایک جمع کریں۔'
    ps = 'له کیڼ لوري پیل کړئ او عددونه یو په بل پسې سره جمع کړئ.'
    w = arith4.WRITE
    r = arith4.RESULT
    ans = f'{total:,}'
    return ans, [f'ss {w[0]}. || {w[1]}۔ || {w[2]}.', f'sm {q}', f'ss {en} || {ur} || {ps}', f'sm {row}',
                 f'ss {r[0]} {ans}. || {r[1]} {ans}۔ || {r[2]} {ans}.']


def process(path, write):
    src = path.read_text(encoding='utf8').split('\n')
    out, n, bad, i = [], 0, [], 0
    while i < len(src):
        line = src[i]
        out.append(line)
        m = re.match(r'^(q|qp)\s+(\S+)\s*\|\s*(.*)$', line)
        if m:
            raw = m.group(3).split(' || ')[0]
            j, ans = i + 1, []
            while j < len(src) and not re.match(r'^(q|qp|exercise|endexercise|h|page|unit)\b', src[j]):
                if re.match(r'^(sol|solution|qsol|qsolve|ss|sm)\b', src[j]):
                    ans.append(j)
                j += 1
            if len(ans) == 1 and src[ans[0]].startswith('sol ') and BLANK.search(raw):
                t = clean(raw)
                head, _, why = src[ans[0]][4:].partition('##')
                block = None
                p = arith4.parse(t)
                if p:
                    built = arith4.build(*p)
                    if built and digits(built[0][9:]) == digits(head):
                        block = [built[0].replace(built[0][9:], head.strip())] + (['ss ' + why.strip()] if why.strip() else []) + built[1:]
                    elif built:
                        bad.append(f'{path.name} {m.group(2)}: {t[:40]} -> {built[0][9:]} vs {head.strip()}')
                else:
                    mm = multi_add(t)
                    if mm:
                        ans_s, steps = build_multi(mm)
                        if digits(ans_s) == digits(head):
                            block = ['solution ' + head.strip()] + (['ss ' + why.strip()] if why.strip() else []) + steps
                        else:
                            bad.append(f'{path.name} {m.group(2)}: {t[:40]} -> {ans_s} vs {head.strip()}')
                if block:
                    out.extend(src[i + 1:ans[0]])
                    out.extend(block)
                    i = ans[0] + 1
                    n += 1
                    continue
        i += 1
    if write and n:
        with open(path, 'w', encoding='utf8', newline='\n') as f:
            f.write('\n'.join(out))
    return n, bad


if __name__ == '__main__':
    tot, allbad = 0, []
    for p in sorted((HERE / 'math' / 'pages').glob('p*.txt')):
        n, bad = process(p, '--write' in sys.argv)
        tot += n
        allbad += bad
    print(f'{"upgraded" if "--write" in sys.argv else "can upgrade"}: {tot}; disagree: {len(allbad)}')
    for b in allbad[:20]:
        print('  ', b)
