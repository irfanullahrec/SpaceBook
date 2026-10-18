from itertools import product,combinations
from math11_answer_authoring import Author,step,S
A=Author(6)
def put(q,p,favorable,total,work,method):
    probability=S.Rational(favorable,total)
    assert 0<=probability<=1
    A.put('6.4',str(q),p,'$'+S.latex(probability)+'$',[method,step('Count the favorable outcomes and divide by the total number of equally likely outcomes.','موافق نتائج گن کر یکساں ممکن نتائج کی کل تعداد پر تقسیم کریں۔','مساعدې پایلې وشمېرئ او د مساوي احتمال لرونکو پایلو پر ټول شمېر یې ووېشئ.',work+r',\quad P(E)=\frac{'+str(favorable)+'}{'+str(total)+'}='+S.latex(probability))])
fair=step('Use the six equally likely faces of a fair die.','غیر جانب دار پانسے کے چھ یکساں ممکن رخ استعمال کریں۔','د عادلانه ځار شپږ مساوي احتمال لرونکي مخونه وکاروئ.',r'S=\{1,2,3,4,5,6\},\quad n(S)=6')
for part,event in [('(i)',[5]),('(ii)',[]),('(iii)',[1,2,3,4,5,6]),('(iv)',[3,6]),('(v)',[4,5,6])]:
    put(1,part,len(event),6,r'E=\{'+','.join(map(str,event))+r'\}',fair)
balls=step('Draw three distinct balls together, without replacement. All unordered selections are equally likely, so use combinations.','تین مختلف گیندیں ایک ساتھ، واپس رکھے بغیر نکالیں۔ تمام بے ترتیب انتخاب یکساں ممکن ہیں، اس لیے جوڑ استعمال کریں۔','درې بېل توپونه یوځای، له بېرته ایښودلو پرته وباسئ. ټول بې ترتیبه انتخابونه مساوي احتمال لري، نو ترکیبونه وکاروئ.',r'n(S)=\binom{15}{3}=455')
all_balls=list(combinations(range(15),3));assert len(all_balls)==455
for part,count,indices in [('(i)',6,set(range(9,15))),('(ii)',4,set(range(4)))]:
    fav=sum(set(x)<=indices for x in all_balls);assert fav==S.binomial(count,3)
    put(2,part,fav,455,r'n(E)=\binom{'+str(count)+r'}{3}='+str(fav),balls)
guess=step('Assume independent random guesses, with correct and incorrect equally likely. There are 2⁸ equally likely answer patterns.','آزاد بے ترتیب اندازے فرض کریں، جن میں درست اور غلط یکساں ممکن ہوں۔ 2⁸ یکساں ممکن جوابی ترتیبیں ہیں۔','خپلواک تصادفي اټکلونه فرض کړئ، چې سم او ناسم مساوي احتمال ولري. 2⁸ مساوي احتمال لرونکې ځوابي بڼې شته.',r'n(S)=2^8=256,\quad n(E_k)=\binom8k')
patterns=list(product((0,1),repeat=8))
for part,ks in [('(i)',[8]),('(ii)',[7]),('(iii)',[6]),('(iv)',[6,7,8])]:
    fav=sum(sum(x) in ks for x in patterns);assert fav==sum(S.binomial(8,k) for k in ks)
    work='n(E)='+('+'.join(r'\binom8{'+str(k)+'}' for k in ks))+'='+str(fav)
    put(3,part,fav,256,work,guess)
coins=step('The three unbiased coins are independent. List all eight equally likely head-tail sequences.','تین غیر جانب دار سکے آزاد ہیں۔ چت پٹ کی آٹھ یکساں ممکن ترتیبیں لکھیں۔','درې بې طرفه سکې خپلواکې دي. د مخ او شا اته مساوي احتمال لرونکې لړۍ ولیکئ.',r'S=\{HHH,HHT,HTH,HTT,THH,THT,TTH,TTT\}')
patterns=[''.join(p) for p in product('HT',repeat=3)]
for part,ks in [('(i)',[3]),('(ii)',[2]),('(iii)',[1]),('(iv)',[1,2,3]),('(v)',[2,3]),('(vi)',[0])]:
    event=[p for p in patterns if p.count('H') in ks]
    put(4,part,len(event),8,r'E=\{'+','.join(event)+r'\}',coins)
committee=step('Choose an unordered five-person committee. Multiply the choices of men and women for a fixed composition.','پانچ افراد کی بے ترتیب کمیٹی منتخب کریں۔ مقررہ ترکیب کے لیے مردوں اور عورتوں کے انتخابوں کو ضرب دیں۔','د پنځو کسانو بې ترتیبه کمیټه وټاکئ. د ټاکلي ترکیب لپاره د نارینه وو او ښځو انتخابونه سره ضرب کړئ.',r'n(S)=\binom{10}{5}=252')
committees=list(combinations(range(10),5))
for part,men,women in [('(i)',3,2),('(ii)',2,3)]:
    fav=sum(sum(i<6 for i in c)==men for c in committees);assert fav==S.binomial(6,men)*S.binomial(4,women)
    put(5,part,fav,252,r'n(E)=\binom6{'+str(men)+r'}\binom4{'+str(women)+'}='+str(fav),committee)
cards=step('A standard 52-card pack has four suits of 13 cards, four aces, and three face cards (J,Q,K) in each suit. Each card is equally likely.','معیاری 52 پتوں کی گڈی میں چار رنگ، ہر رنگ کے 13 پتے، چار اِکے، اور ہر رنگ میں تین تصویری پتے (J,Q,K) ہوتے ہیں۔ ہر پتہ یکساں ممکن ہے۔','د 52 کارتونو معیاري دسته څلور رنګونه لري، د هر رنګ 13 کارتونه، څلور اېسونه، او په هر رنګ کې درې د څېرې کارتونه (J,Q,K). هر کارت مساوي احتمال لري.')
deck=list(product('SHDC',range(1,14)))
events=[
('(i)',[(s,r) for s,r in deck if r==1],r'n(E)=4'),
('(ii)',[(s,r) for s,r in deck if s in 'SH'],r'n(E)=13+13=26'),
('(iii)',[(s,r) for s,r in deck if s=='D'],r'n(E)=13'),
('(iv)',[(s,r) for s,r in deck if r in [11,12,13]],r'n(E)=4\cdot3=12'),
('(v)',[(s,r) for s,r in deck if (s,r)!=('H',1)],r'n(E)=52-1=51')]
for part,event,work in events:put(6,part,len(event),52,work,cards)
dice=step('Assume fair independent dice. Count ordered pairs, so (1,2) and (2,1) are different outcomes. An even doublet means the same even number on both dice.','پانسے غیر جانب دار اور آزاد فرض کریں۔ ترتیب دار جوڑے گنیں، اس لیے (1,2) اور (2,1) مختلف نتائج ہیں۔ جفت دوہرے جوڑے میں دونوں پانسوں پر ایک ہی جفت عدد آتا ہے۔','عادلانه او خپلواک ځارونه فرض کړئ. ترتیب لرونکې جوړې وشمېرئ، نو (1,2) او (2,1) بېلې پایلې دي. جفت دوه ګونی د دواړو ځارونو پر مخ د یوه جفت عدد راتلل دي.',r'n(S)=6\cdot6=36')
predicates=[
('(i)',lambda a,b:a==b and a%2==0),
('(ii)',lambda a,b:a+b<6),
('(iii)',lambda a,b:a+b>7),
('(iv)',lambda a,b:a+b>10),
('(v)',lambda a,b:a+b>=10),
('(vi)',lambda a,b:a*b==6),
('(vii)',lambda a,b:(a+b)%2==0),
('(viii)',lambda a,b:(a+b)%2==1),
('(ix)',lambda a,b:(a+b)%3==0),
('(x)',lambda a,b:a+b in [2,3,5,7,11])]
expected=[3,10,15,3,6,4,18,18,12,15]
for (part,pred),count in zip(predicates,expected):
    event=[(a,b) for a,b in product(range(1,7),repeat=2) if pred(a,b)];assert len(event)==count
    work=r'E=\{'+','.join(f'({a},{b})' for a,b in event)+r'\}'
    put(7,part,count,36,work,dice)
A.save(['6.4'],[195,196])
