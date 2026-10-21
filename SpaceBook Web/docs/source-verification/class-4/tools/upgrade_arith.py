"""Give existing one-line answers of plain arithmetic questions a worked-equation chain the animated solution can step through.

    CLS=1 python upgrade_arith.py [--write]        (CLS = 1, 2, 3, 4 or 5; default 4)

For a question that is exactly `A + B`, `A - B`, `A x B` or `A ÷ B` and whose single `sol ANSWER ## why` line agrees
with the computed result, the `sol` line is replaced by `solution ANSWER`, the book's own explanation as step 1, then
the question, the working and the result as `sm` rows (same steps arith4.py writes). Disagreeing answers are never
changed; they are printed so a person can look at them.
"""
import re, sys
from pathlib import Path
import arith4

HERE = arith4.HERE


def digits(s):
    return re.sub(r'\D', '', s.translate(str.maketrans('۰۱۲۳۴۵۶۷۸۹', '0123456789')))


def process(path, write):
    src = path.read_text(encoding='utf8').split('\n')
    out, n, bad = [], 0, []
    i = 0
    while i < len(src):
        line = src[i]
        out.append(line)
        m = re.match(r'^(q|qp)\s+(\S+)\s*\|\s*(.*)$', line)
        if m:
            p = arith4.parse(m.group(3).split(' || ')[0])
            # the sol line must come before the next question line, and be the only answer line of this item
            j, sols = i + 1, []
            while j < len(src) and not re.match(r'^(q|qp|exercise|endexercise|h|page|unit)\b', src[j]):
                if re.match(r'^(sol|solution|qsol|qsolve|ss|sm)\b', src[j]):
                    sols.append(j)
                j += 1
            if p and len(sols) == 1 and src[sols[0]].startswith('sol '):
                built = arith4.build(*p)
                head, _, why = src[sols[0]][4:].partition('##')
                if built and digits(built[0][9:]) == digits(head):
                    # copy the lines between the question and its sol unchanged, then the new block
                    out.extend(src[i + 1:sols[0]])
                    ans = built[0]
                    out.append(ans)
                    if why.strip():
                        out.append('ss ' + why.strip())
                    out.extend(built[1:])
                    i = sols[0] + 1
                    n += 1
                    continue
                elif built:
                    bad.append(f'{path.name} {m.group(2)}: key {head.strip()} vs computed {built[0][9:]}')
        i += 1
    if write and n:
        with open(path, 'w', encoding='utf8', newline='\n') as f:
            f.write('\n'.join(out))
    return n, bad


if __name__ == '__main__':
    subj = next((a for a in sys.argv[1:] if not a.startswith('--')), 'math')
    tot, allbad = 0, []
    for p in sorted((HERE / subj / 'pages').glob('p*.txt')):
        n, bad = process(p, '--write' in sys.argv)
        tot += n
        allbad += bad
    print(f'{"upgraded" if "--write" in sys.argv else "can upgrade"}: {tot}; answer disagrees with computed value: {len(allbad)}')
    for b in allbad[:30]:
        print('  ', b)
