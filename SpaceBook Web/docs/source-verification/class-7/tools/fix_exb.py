"""One-off: give the Class 7 ex_b.txt lines a plain final row so the answer shown is the complete answer (the DSL takes the part after the last '=' of the last row)."""
from pathlib import Path
p = Path(__file__).resolve().parents[1] / 'math' / 'dsl' / 'ex_b.txt'
L = p.read_text(encoding='utf-8').split('\n')
FINAL = {
    '7.1|1|a': '19, 22, 25', '7.1|1|b': '100, 10, 1, 0.1', '7.1|1|c': '625, 125, 25', '7.1|1|d': '96, 192, 384', '7.1|1|e': '75, 60, 45',
    '7.1|2|i': '30, 38, 87', '7.1|2|ii': '50, 90, 335', '7.1|2|iii': '165, 285, 1020',
    'R8|5': '121, 123, 125, 127, 129', 'R8|6': 'Printer Rs 1975, photocopy machine Rs 15800', 'R8|7': 'Length 70 m, width 25 m', 'R8|8': '64°, 64°, 52°',
    'R5|2|a': 'Loss Rs 2100, loss 3.12%', 'R5|2|b': 'Profit Rs 150, profit 1.76%',
}
out = []
for ln in L:
    if '~' in ln:
        k = ln.split('~')[0].strip()
        if k in FINAL:
            head, rest = ln.split('=>')[0], ln.split('=>')[1]
            ln = head.rstrip() + ' ;; ' + FINAL[k] + ' =>' + rest
    out.append(ln)
p.write_text('\n'.join(out), encoding='utf-8')
print('ok')
