"""apply_gen8.py - replace the template stub solutions of Class 8 Mathematics with engine-computed worked solutions.

    python apply_gen8.py [--dry]

Reads  class-8/math/gen_solutions.json   (written by class-7/tools/msol_run.py 8: every entry is computed and checked
                                           against the printed key, or authored in math/dsl/*.txt and chain-checked)
       js/math_8_data.js                 (question -> solId)
Writes js/math_8_solutions.js            (entry replaced only where a generated solution exists)
Run again whenever gen_solutions.json changes; it is idempotent.
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
APP = HERE.parents[2]
DATA = APP / 'js' / 'math_8_data.js'
SOL = APP / 'js' / 'math_8_solutions.js'


def load_json_assign(path, name):
    txt = path.read_text(encoding='utf-8')
    m = re.search(r'(?:const|window\.)\s*' + re.escape(name) + r'\s*=\s*', txt)
    start = m.end()
    dec = json.JSONDecoder()
    obj, end = dec.raw_decode(txt, start)
    return txt, obj, start, end


def main():
    gen = json.loads((HERE / 'math' / 'gen_solutions.json').read_text(encoding='utf-8'))
    _, units, _, _ = load_json_assign(DATA, 'MATH_8_DATA')
    stxt, sols, s0, s1 = load_json_assign(SOL, 'MATH_8_SOLUTIONS')
    replaced = 0
    seen = set()

    def walk(blocks, unit, ex):
        nonlocal replaced
        for x in blocks:
            if x.get('t') == 'exercise':
                ex = x.get('id')
            if x.get('t') == 'q':
                exid = f'R{unit}' if ex == 'Review Exercise' else ex
                leaves = [(p.get('no', ''), p) for p in x['parts']] if x.get('parts') else [('', x)]
                for no, owner in leaves:
                    key = f"{exid}|{x.get('no')}|{no}"
                    sid = owner.get('solId')
                    if key in gen and sid and sid in sols and key not in seen:
                        seen.add(key)
                        g = gen[key]
                        sols[sid] = {'steps': g['steps'], 'answer': g['answer']}
                        replaced += 1
            if x.get('blocks'):
                walk(x['blocks'], unit, ex)

    for u in units:
        for s in u.get('sections', []):
            walk(s.get('blocks', []), u['number'], None)
    print('replaced', replaced, 'of', len(gen), 'generated;', len(sols), 'solution entries in total')
    if '--dry' in sys.argv:
        return
    SOL.write_text(stxt[:s0] + json.dumps(sols, ensure_ascii=False) + stxt[s1:], encoding='utf-8')


if __name__ == '__main__':
    main()
