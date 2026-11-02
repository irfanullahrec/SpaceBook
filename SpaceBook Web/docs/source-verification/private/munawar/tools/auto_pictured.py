"""Turns the "(Pictured words: a, b, c.)" / "(Pictures: ...)" notes of a transcribed question into a `pic row` before it.
usage: python docs/source-verification/private/munawar/tools/auto_pictured.py <book-id>... [--write]   (without --write: only a report)
A note is used only when at least 70 % of its items have a drawing; unmapped items are left out of the row and listed in the report."""
import re, sys, collections
from pathlib import Path
MUN = Path(__file__).resolve().parents[1]          # docs/source-verification/private/munawar
sys.path.insert(0, str(MUN / 'tools'))
import mun_figs as M

OBJ = set(M.OBJECTS)
SYN = {
    'ship': 'boat', 'sailboat': 'boat', 'motorboat': 'boat', 'aeroplane': 'plane', 'airplane': 'plane', 'jet': 'plane', 'seaplane': 'plane', 'bicycle': 'bike',
    'motorbike': 'bike', 'taxi': 'car', 'forklift': 'truck', 'hot air balloon': 'balloon', 'chicken': 'hen', 'watch': 'clockicon', 'clock': 'clockicon',
    'torch': 'lamp', 'mice': 'rat', 'mouse': 'rat', 'home': 'house', 'man': 'boy', 'children': 'boy', 'child': 'boy', 'lamb': 'sheep', 'queen': 'crown',
    'x-box': 'gameconsole', 'rose': 'flower', 'tv': 'tv', 'screen': 'tv', 'school bag': 'schoolbag', 'bag': 'bag', 'icecream': 'icecream', 'ice-cream': 'icecream',
    'eggs': 'egg', 'cows': 'cow', 'pigeon': 'bird', 'crow': 'bird', 'sparrow': 'bird', 'parrot': 'bird', 'jackal': 'dog', 'ape': 'monkey', 'yak': 'cow', 'ox': 'cow',
    'alligator': 'crocodile', 'bus': 'bus', 'cheese': 'cheese', 'pot': 'pot', 'pan': 'pot', 'fan': 'fan', 'sun': 'sun', 'plane': 'plane', 'shoes': 'shoe',
    'peach': 'apricot', 'bee': 'bee', 'kite': 'kite', 'cap': 'cap', 'hat': 'hat', 'frog': 'frog', 'gas': None, 'lion': 'lion', 'train': 'train',
    'bridge': None, 'monitor': 'monitor', 'brush': 'brush', 'bed': 'bed', 'ball': 'ball', 'doll': 'doll', 'teddy': 'teddy', 'jug': 'jug', 'pen': 'pen',
}


def obj_for(w):
    w = w.strip().lower().strip('.').strip()
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
    pairs = [(re.sub(r'^(a|an|the)\s+', '', w.strip().strip('.')), obj_for(w)) for w in items]
    got = [(w, o) for w, o in pairs if o]
    return pairs, got


def process(book, write):
    d = MUN / book / 'pages'
    missing = collections.Counter(); added = 0
    for f in sorted(d.glob('p*.txt')):
        lines = f.read_text(encoding='utf-8').split('\n')
        out = []; changed = False
        for ln in lines:
            m = re.search(r'\((?:Pictured words|Pictures|Pictured sentences)\s*:\s*([^)]*)\)', ln.split('||')[0]) if ln[:2] in ('q ', 'p ') or ln.startswith('qp ') else None
            if m and 'Pictured sentences' not in m.group(0):
                items = [x for x in re.split(r',\s*|\s+and\s+', m.group(1)) if x.strip()]
                pairs, got = rows_for(items)
                if len(items) >= 2 and len(got) >= 0.7 * len(items) and len(got) >= 2:
                    for w, o in pairs:
                        if not o:
                            missing[w] += 1
                    scale = 0.8 if len(got) > 5 else 1.0
                    for k in range(0, len(got), 7):
                        chunk = got[k:k + 7]
                        pic = 'pic row ' + ' | '.join(f'{w}={o}' for w, o in chunk) + (f' s={scale}' if scale != 1.0 else '')
                        if pic not in lines and pic not in out:
                            out.append(pic); changed = True; added += 1
                else:
                    for w, o in pairs:
                        if not o:
                            missing[w] += 1
            out.append(ln)
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
