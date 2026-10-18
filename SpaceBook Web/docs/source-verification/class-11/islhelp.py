from isllib import *
def pid(n,k): return f'isl11-s{n:03}-{k}'
def L(s,items,group):
    for k,a,b,d in items: add(s,k,a,b,d,listGroup=group)
def build(s,n,seq,eqs):
    """seq: 'key' paragraph, 'E:key' equation, 'T:i' table."""
    base=len(s['equations'])
    s['equations']+=[eqn(n,k,l,t,**({'exampleId':ex} if ex else {})) for k,l,t,ex in eqs]
    idx={k:base+i for i,(k,_,_,_) in enumerate(eqs)}
    flow=[]
    for it in seq:
        if it.startswith('E:'): flow.append(dict(type='equation',index=idx[it[2:]]))
        elif it.startswith('T:'): flow.append(dict(type='table',index=int(it[2:])))
        elif it.startswith('F:'): flow.append(dict(type='figure',index=int(it[2:])))
        else:
            if flow and flow[-1]['type']=='paragraphs': flow[-1]['ids'].append(pid(n,it))
            else: flow.append(dict(type='paragraphs',ids=[pid(n,it)]))
    s['flow']=flow
