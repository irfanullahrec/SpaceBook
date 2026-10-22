import json,collections,sys
g=json.load(open('docs/source-verification/class-8/math/gen_solutions.json',encoding='utf8'))
L=json.load(open('tmp/m8_leaves.json',encoding='utf8'))
print(len(g),len(L), list(g)[:3])
miss=collections.OrderedDict()
for l in L:
    ex=l['ex']
    parts=[p for p,_ in l['parts']] or ['']
    m=[p for p in parts if f"{ex}|{l['q']}|{p}" not in g]
    if m: miss.setdefault(ex,[]).append((l['q'],m,l['en'][:70],str(l.get('key'))[:60]))
print({k:sum(len(x[1]) for x in v) for k,v in miss.items()})
json.dump(miss,open('tmp/miss8.json','w'))
