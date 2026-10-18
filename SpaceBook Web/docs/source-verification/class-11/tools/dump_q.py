import sys,json
sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from math11_answer_authoring import load_unit
u=load_unit(int(sys.argv[1]))
for ex in u['exercises']:
    print('==',ex['id'])
    def walk(bs):
        for b in bs:
            if b['t']=='q':
                print(f"Q{b['no']}: {b['en']}")
                for p in b.get('parts',[]):print(f"   {p['no']} {p['en']}")
            if b.get('blocks'):walk(b['blocks'])
    walk(ex['blocks'])
