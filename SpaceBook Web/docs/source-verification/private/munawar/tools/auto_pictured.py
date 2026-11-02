"""Turns what a transcribed page says about its pictures into `pic row` lines (our own coded drawings, see mun_figs.py):
  1. a question with "(Pictured words: a, b, c.)" / "(Pictures: ...)"           -> a row before the question
  2. a table whose title says "... in the pictures" / "shown" (its first column names the pictures)  -> a row before the table
usage: python docs/source-verification/private/munawar/tools/auto_pictured.py <book-id>... [--write]   (without --write: only a report)
An item list is used only when at least 70 % of its items have a drawing; unmapped items are left out of the row and listed in the report."""
import re, sys, collections
from pathlib import Path
MUN = Path(__file__).resolve().parents[1]          # docs/source-verification/private/munawar
sys.path.insert(0, str(MUN / 'tools'))
import mun_figs as M

OBJ = set(M.OBJECTS)
SYN = {
    'ship': 'boat', 'sailboat': 'boat', 'motorboat': 'boat', 'aeroplane': 'plane', 'airplane': 'plane', 'jet': 'plane', 'seaplane': 'plane', 'bicycle': 'bike',
    'motorbike': 'bike', 'taxi': 'car', 'forklift': 'truck', 'hot air balloon': 'balloon', 'chicken': 'hen', 'cock': 'hen', 'watch': 'clockicon', 'clock': 'clockicon',
    'torch': 'lamp', 'mice': 'rat', 'mouse': 'rat', 'home': 'house', 'man': 'boy', 'children': 'boy', 'child': 'boy', 'lamb': 'sheep', 'queen': 'crown',
    'x-box': 'gameconsole', 'rose': 'flower', 'screen': 'tv', 'school bag': 'schoolbag', 'icecream': 'icecream', 'ice-cream': 'icecream', 'ice cream': 'icecream',
    'eggs': 'egg', 'cows': 'cow', 'pigeon': 'bird', 'crow': 'bird', 'sparrow': 'bird', 'parrot': 'bird', 'robin': 'bird', 'eagle': 'bird', 'jackal': 'dog',
    'ape': 'monkey', 'gorilla': 'monkey', 'orangutan': 'monkey', 'yak': 'cow', 'ox': 'cow', 'bull': 'cow', 'buffalo': 'cow', 'alligator': 'crocodile',
    'coach': 'bus', 'shoes': 'shoe', 'peach': 'apricot', 'tortoise': 'turtle', 'cobra': 'snake', 'armchair': 'sofa', 'sofa': 'sofa', 'tomatoes': 'tomato',
    'teddy bear': 'teddy', 'teddy': 'teddy', 'honeybee': 'bee', 'football': 'football', 'ball': 'ball', 'toy blocks': 'block', 'blocks': 'block',
    'sports car': 'car', 'lantern': 'lamp', 'pocket watch': 'clockicon', 'digital watch': 'clockicon', 'television': 'tv', 'mobile phone': 'phone', 'cell phone': 'phone',
    'ice': 'ice', 'fire': 'fire', 'campfire': 'fire', 'train': 'train', 'rail': 'train', 'gas': None, 'bridge': None, 'plant': 'plant', 'tree': 'tree',
}


def obj_for(w):
    w = w.strip().lower().strip('.').strip()
    w = re.sub(r'\([^)]*\)', '', w).split(' / ')[0].strip()
    w = re.sub(r'^(a|an|the|two|three|four|five|six|seven|eight|nine|ten)\s+', '', w)
    if w in SYN:
        return SYN[w]
    if w in OBJ:
        return w
    for cand in (w[:-1] if w.endswith('s') else None, w[:-2] if w.endswith('es') else None, w[:-3] + 'y' if w.endswith('ies') else None):
        if cand and cand in SYN:
            return SYN[cand]
        if cand and cand in OBJ:
            return cand
    return None


def rows_for(items):
    pairs = [(re.sub(r'\s+', ' ', re.sub(r'^(a|an|the)\s+', '', re.sub(r'\([^)]*\)', '', w).strip().strip('.'))).strip(), obj_for(w)) for w in items]
    got = [(w, o) for w, o in pairs if o]
    return pairs, got


def make_rows(items, missing):
    pairs, got = rows_for(items)
    if len(items) >= 2 and len(got) >= 0.7 * len(items) and len(got) >= 2:
        for w, o in pairs:
            if not o:
                missing[w] += 1
        scale = 0.8 if len(got) > 5 else 1.0
        return [('pic row ' + ' | '.join(f'{w}={o}' for w, o in got[k:k + 7]) + (f' s={scale}' if scale != 1.0 else '')) for k in range(0, len(got), 7)]
    for w, o in pairs:
        if not o:
            missing[w] += 1
    return []


def process(book, write):
    d = MUN / book / 'pages'
    missing = collections.Counter(); added = 0
    for f in sorted(d.glob('p*.txt')):
        lines = f.read_text(encoding='utf-8').split('\n')
        out = []; changed = False
        i = 0
        while i < len(lines):
            ln = lines[i]
            rows = []
            m = re.search(r'\((?:Pictured words|Pictures)\s*:\s*([^)]*)\)', ln.split('||')[0]) if ln[:2] in ('q ', 'p ') or ln.startswith('qp ') else None
            if m:
                rows = make_rows([x for x in re.split(r',\s*|\s+and\s+', m.group(1)) if x.strip()], missing)
            elif ln.startswith('table ') and re.search(r'in the pictures|shown|the pictures', ln.split('||')[0], re.I):
                j = i + 1; items = []
                while j < len(lines) and not lines[j].startswith('endtable'):
                    if lines[j].startswith('tr '):
                        cell = lines[j][3:].replace('||', chr(0)).split('|')[0].split(chr(0))[0].strip()
                        if cell and not re.fullmatch(r'[ivx0-9.]+', cell):
                            items.append(cell)
                    j += 1
                prev = out[-1] if out else ''
                if not prev.startswith('pic row'):
                    rows = make_rows(items, missing)
            for pic in rows:
                if pic not in lines and pic not in out:
                    out.append(pic); changed = True; added += 1
            out.append(ln)
            i += 1
        if changed and write:
            f.write_text('\n'.join(out), encoding='utf-8', newline='')
    return added, missing


if __name__ == '__main__':
    write = '--write' in sys.argv
    allmiss = collections.Counter()
    for b in [a for a in sys.argv[1:] if not a.startswith('--')]:
        n, miss = process(b, write)
        allmiss.update(miss)
        print(b, 'rows', 'written' if write else 'would be added', n)
    print('unmapped:', ', '.join(f'{w}({c})' for w, c in allmiss.most_common(60)))
