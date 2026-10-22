import re,sys
def sol(a,why=''):
    return f"sol {a} ## {why or a} || درست جواب: {a} || سم ځواب: {a}"
def ins(page, after_marker, items):
    f=f'p{page}.txt'; L=open(f,encoding='utf8').read().split('\n')
    s=next(i for i,l in enumerate(L) if l.startswith(after_marker))
    out=L[:s+1]; rest=L[s+1:]; done=set(); res=[]
    for l in rest:
        res.append(l)
        m=re.match(r'qp (\S+) \|',l)
        if m and m.group(1) in items and m.group(1) not in done:
            done.add(m.group(1)); res.append(items[m.group(1)])
    assert done==set(items),(page,done)
    open(f,'w',encoding='utf8',newline='\n').write('\n'.join(out+res))
ins('020','q - | Add the correct demonstrative',{
 'a':sol('that','"that" points to something away from the speaker: Take that to your grandmother.'),
 'b':sol('this','"this" refers to the thing just mentioned (speaking fluently): ... this is all I want.'),
 'c':sol('That','"That" introduces the story being talked about.'),
 'd':sol('These','"These" is plural to agree with "are": These are not good translations.')})
ins('021','q - | Read each sentence',{
 '1':sol('ourselves','Sarah and I = we, so the reflexive pronoun is ourselves.'),
 '2':sol('themselves','Ali and his sister = they, so themselves.'),
 '3':sol('herself','"all by herself" refers to Fatima.'),
 '4':sol('themselves','Ahmed and Inam = they, so themselves.'),
 '5':sol('herself','Duaa reminded herself: subject and object are the same person.'),
 '6':sol('itself','The dog wagged itself (its tail), singular non-person: itself.'),
 '7':sol('ourselves','We promised ourselves.'),
 '8':sol('themselves','The team congratulated themselves (the team members).'),
 '9':sol('herself','Afsha hurt herself.'),
 '10':sol('themselves','They challenged themselves.')})
ins('026','q 1 | Fill in the blanks',{
 'a':sol('motives'),'b':sol('unreasonable'),'c':sol('illogical'),'d':sol('jealous'),
 'e':sol('serenity'),'f':sol('frank'),'g':sol('succeed'),'h':sol('self-centered')})
# p019 table words
f='p019.txt'; t=open(f,encoding='utf8').read()
for j,w,mn in [('gvniohtre','overnight','during the night'),('rmacepd','cramped','too small and crowded'),('ptmnetar','apartment','a flat; a set of rooms in a building'),('dgsursrnuoin','surrounding','all around'),('labeyr','barely','only just; hardly'),('rgernfoie','foreigner','a person from another country'),('poinxemocl','complexion','the natural colour of the skin of the face'),('adeterspa','desperate','having a great need; hopeless'),('esisonpred','depression','a state of deep sadness')]:
    t=t.replace(f'tr | {j} |  |',f'tr | {j} | {w} | {mn}')
open(f,'w',encoding='utf8',newline='\n').write(t)
