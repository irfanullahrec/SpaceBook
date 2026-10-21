"""Copy the book's PRINTED answer key (the `ans` lines of the answers pages) onto the questions of Class 4 Mathematics.

    python keyans4.py [--write]      (dry run prints the counts and every key entry that found no question)

Key entries look like `ans Exercise 1 (Page 16) | 2 | a) 103,501 b) 91,190 ...`. A question or part that has no
answer yet gets `sol ANSWER ## Printed answer key.` right after it. Questions that already carry an answer
(sol / solution / qsol / qsolve, e.g. from arith4.py) are never touched, but their computed answer is compared with
the key and any difference is printed.
"""
import re, sys, time
from pathlib import Path

PAGES = Path(__file__).resolve().parents[1] / 'math' / 'pages'
WHY = 'Answer from the book\'s printed answer key. || کتاب کے آخر میں دی گئی جوابات کی فہرست کے مطابق۔ || د کتاب په پای کې د ځوابونو د لیست سره سم.'


def read_key():
    key = {}
    for p in sorted(PAGES.glob('p*.txt')):
        txt = p.read_text(encoding='utf8')
        if '@status answers' not in txt:
            continue
        for line in txt.split('\n'):
            m = re.match(r'^ans (.+?) \| (\S+) \| (.*)$', line)
            if m:
                key[(m.group(1).strip(), m.group(2))] = m.group(3).strip()
    return key


def split_parts(s):
    """'a) 1 b) 2' -> {'a': '1', 'b': '2'} when the letters run a, b, c ... in order; else None"""
    pos = [(m.start(), m.group(1), m.end()) for m in re.finditer(r'(?:^|(?<=[\s;]))([a-z])\)\s*', s)]
    if not pos or [x[1] for x in pos] != [chr(97 + i) for i in range(len(pos))]:
        return None
    out = {}
    for i, (st, letter, en) in enumerate(pos):
        end = pos[i + 1][0] if i + 1 < len(pos) else len(s)
        out[letter] = s[en:end].strip().rstrip(';').strip()
    return out


def clean(a):
    return re.sub(r'\s*\(answer [a-z]\) not printed\)', '', a).strip()


def main():
    write = '--write' in sys.argv
    key = read_key()
    used, added, mismatch = set(), 0, []
    ex, cur_q, parts_seen = None, None, 0
    pages = []
    for p in sorted(PAGES.glob('p*.txt')):
        src = p.read_text(encoding='utf8').split('\n')
        if not any(l.startswith('@status answers') for l in src):
            pages.append((p, src))
    for k, (p, src) in enumerate(pages):
        more = [x for _, s2 in pages[k + 1:k + 3] for x in s2]      # a question's parts may continue on the next page
        out, changed = [], False
        for i, line in enumerate(src):
            out.append(line)
            m = re.match(r'^exercise (.+)$', line)
            if m:
                ex = m.group(1).strip()
                continue
            if line.startswith('endexercise'):
                ex = None
                continue
            m = re.match(r'^(q|qp)\s+(\S+)\s*\|', line)
            if not m or ex is None:
                continue
            if m.group(1) == 'q':
                cur_q, parts_seen = m.group(2), 0
                nxt_is_part = False
                for x in (src[i + 1:] + more):
                    if re.match(r'^(q|exercise|endexercise|page|unit)\b', x):
                        break
                    if x.startswith('qp '):
                        nxt_is_part = True
                        break
                owner = ('q', cur_q)
                if nxt_is_part:
                    continue
            else:
                parts_seen += 1
                owner = ('qp', m.group(2))
            ahead = []
            for x in src[i + 1:]:
                if re.match(r'^(q|qp|exercise|endexercise|h|page|unit)\b', x):
                    break
                ahead.append(x)
            have = [x for x in ahead if re.match(r'^(sol|solution)\b', x)]
            raw = key.get((ex, cur_q))
            if raw is None:
                continue
            used.add((ex, cur_q))
            parts = split_parts(raw)
            if owner[0] == 'q':
                ans = clean(raw)
            elif parts is None:
                continue
            elif owner[1] in parts:
                ans = clean(parts[owner[1]])
            elif len(parts) >= parts_seen:
                ans = clean(list(parts.values())[parts_seen - 1])
            else:
                continue
            if have:
                head = have[0].split('##')[0].split(None, 1)[1].strip() if have[0].startswith('sol ') else have[0][9:].strip()
                if re.sub(r'\D', '', head) != re.sub(r'\D', '', ans) and re.sub(r'\D', '', ans):
                    mismatch.append(f'{p.name} {ex} q{cur_q}{"" if owner[0] == "q" else owner[1]}: computed {head} vs key {ans}')
                continue
            if not ans:
                continue
            out.append(f'sol {ans} ## {WHY}')
            added += 1
            changed = True
        if write and changed:
            for attempt in range(6):          # Windows sometimes refuses the open for a moment (indexer / antivirus)
                try:
                    with open(p, 'w', encoding='utf8', newline='\n') as f:
                        f.write('\n'.join(out))
                    break
                except OSError:
                    time.sleep(1.5)
            else:
                raise
    print(f'answers {"written" if write else "found (dry run)"}: {added}')
    print('computed-vs-key mismatches:', len(mismatch))
    for x in mismatch[:40]:
        print('  ', x)
    miss = [k for k in key if k not in used]
    print('key entries with no question on any page:', len(miss))
    for k in miss[:40]:
        print('  ', k, key[k][:60])


if __name__ == '__main__':
    main()
