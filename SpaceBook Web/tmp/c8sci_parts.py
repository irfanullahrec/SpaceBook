import re
D='D:/SpaceBook/SpaceBook Web/docs/source-verification/class-8/sci/pages/'
def put(pg,start,lab,text):
    f=D+f'p{pg}.txt'; L=open(f,encoding='utf8').read().split('\n')
    s=next(k for k,l in enumerate(L) if l.startswith(start))
    i=next(k for k in range(s,len(L)) if L[k].startswith(f'qp {lab} '))
    if L[i+1].startswith('sol'): return
    L.insert(i+1,'sol '+text); open(f,'w',encoding='utf8',newline='\n').write('\n'.join(L))
V='## From the activity list: '
put('028','box teach','a','Voluntary: walking, running, riding a bicycle, eating, reading, swimming. '+V+'we do these willingly. || رضاکارانہ: چلنا، دوڑنا، سائیکل چلانا، کھانا، پڑھنا، تیراکی۔')
put('028','box teach','b','Involuntary: sneezing, breathing, heartbeat, blinking of eyes, salivation. '+V+'they happen without our conscious control. || غیر ارادی: چھینکنا، سانس لینا، دل کی دھڑکن، پلکیں جھپکنا، لعاب کا نکلنا۔')
put('028','box teach','c','Other voluntary: writing, talking, playing, kicking a ball. Other involuntary: yawning, goose bumps, pulling the hand away from something hot, shivering, digestion. ## Examples; your own experience may add more.')
put('031','p ','a','The reading is the distance in centimetres at the ruler mark where the thumb catches it; for example 15 cm gives a reaction time t = sqrt(2d/g) = sqrt(2 x 0.15 / 9.8) = about 0.17 s. ## Example value; the reading depends on the figure/your own trial (Not verified).')
put('031','p ','b','The student whose catch distance is the smallest has the shortest reaction time. ## Depends on your class data (Not verified).')
put('031','p ','c','Add the ten reflex times and divide by 10: average = (t1 + t2 + ... + t10) / 10, typically about 0.15 to 0.25 s. ## Depends on your class data (Not verified).')
put('031','p ','d','The student who catches the ruler after the longest distance has the slowest reflex (longest reaction time). ## Depends on your class data (Not verified).')
put('045','qp a','a','Height, weight, arm span or foot length usually show the greatest variability in a class because every student has a slightly different value. ## Depends on your class data (Not verified).')
put('045','qp a','b','Continuous variations: height, weight, foot length, arm span, hand span. Discontinuous variations: blood group, eye colour, ability to roll the tongue, attached or free ear lobes. ## Continuous traits show a range of values; discontinuous traits fall in distinct groups (Derived from the standard traits).')
