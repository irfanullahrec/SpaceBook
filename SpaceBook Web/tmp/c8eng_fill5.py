import re
def addq(page, qprefix, text):
    f=f'p{page}.txt'; L=open(f,encoding='utf8').read().split('\n')
    i=next(i for i,l in enumerate(L) if l.startswith(qprefix))
    # insert after last endtable before endexercise, else right after q
    k=i
    while k<len(L) and not L[k].startswith('endexercise') and not (k>i and re.match(r'q(p)? ',L[k])):
        k+=1
    ins=k
    # put sol right after the q line's table end if present
    for m in range(i,k):
        if L[m].startswith('endtable'): ins=m+1
    if ins==k: ins=i+1
    L.insert(ins,text); open(f,'w',encoding='utf8',newline='\n').write('\n'.join(L))
addq('039','q 1 | Read the cause','sol Model answers: b. Effect: the city becomes dirty and diseases spread. Sentence: Because people are dumping trash everywhere, the city becomes dirty and diseases spread. c. Effect: fish and other water animals die. Sentence: Toxic waste dumped in seas, rivers and streams kills fish and other water animals. d. Effect: plastic pollutes the soil and drains and harms animals. Sentence: As more people use polythene bags, plastic pollutes the soil and blocks drains. e. Effect: the air becomes polluted and causes breathing problems. Sentence: Many cars release carbon monoxide, so the air becomes polluted and people suffer breathing problems. ## Each sentence joins the cause and the effect with because, so, as or due to; one possible answer.')
addq('045','q - | Match the type','sol a. ecotourism - to take responsible trips to protect natural environments (e.g. visiting a national park or a conservation project); b. international tourism - visit other countries to visit famous tourist spots (e.g. a trip to Malaysia); c. cultural tourism - to learn about history, lifestyle and culture of a particular place (e.g. visiting Lahore Fort); d. religious tourism - to visit holy places (e.g. Hajj or Umrah); e. recreational tourism - to visit a place just to relax or for fun (e.g. a beach holiday); f. domestic tourism - to explore the beauty of your own country (e.g. a trip to Swat); g. edutourism - to take a trip for higher studies (e.g. a student exchange programme); h. adventure tourism - to explore risky areas and go on for extreme activities (hiking, given) ## Definitions matched by meaning; the examples are suggestions.')
addq('048','q - | Pick the phrasal','sol 1. saw ... off; 2. hurry up; 3. looking forward; 4. got on; 5. get away; 6. take off; 7. speeding up; 8. got in; 9-10. pick ... up (Derived: not in the box); 11-12. dropped ... off; 13. checked in; 14. looked around; 15. checked out; 16. set out; 17. get back ## Phrasal verbs fitted from the box by meaning; 9-10 is Derived because "pick up" is not in the box and the passage blanks are unclear in the scan.')
