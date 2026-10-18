"""Shared builder for Chemistry XII glossary spreads: entries are (term_en, def_en, term_ur, def_ur, term_ps, def_ps)."""
from class12_chemistry_opening import pair,section,SOURCE
def glossary_record(sid,pdf,printed,entries,heading=False,lead=None):
    P=[];L=[]
    for q in (lead or []):
        L.append({'type':'paragraph','indices':[len(P)]});P.append(pair(*q))
    if heading:
        L.append({'type':'heading','indices':[len(P)]});P.append(pair('Glossary','فرہنگ','لغتنامه'))
    s0=len(P)
    for te,de,tu,du,tp,dp in entries:
        P.append(pair(f'{te}: {de}',f'{tu}: {du}',f'{tp}: {dp}'))
    L.append({'type':'list','indices':list(range(s0,len(P)))})
    a,b=printed
    r=section(sid,f'Glossary (printed {a}–{b})',f'فرہنگ (صفحات {a}–{b})',f'لغتنامه (مخونه {a}–{b})',P,L,[],f'{a}–{b}')
    r['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':pdf,'printedPages':[a,b]}]
    return r
