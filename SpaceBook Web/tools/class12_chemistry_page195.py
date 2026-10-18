"""PDF195 printed384–385: Answers of MCQs (Units 13–24)."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
KEY={13:'a a c c a d b c b b b c c a a',14:'d d a d b d c a c d d b a c c',15:'b a a c d b c a d d d c a d d',16:'b b b d c d d a d c c c c b b',
17:'a b a a a d b b b c a d b d a',18:'b c d a b d c b c b b c a d a',19:'b c d d b b c c a d a b a d b',20:'c c a b d a b d a d',
21:'c a a c d a d b b c b a d c c',22:'a d c c a b c a d c c d b a b',23:'d d a a d d d a c a b a d a d',24:'b c a a b a d c a d a d b b d'}
P=[];L=[];B=[]
L.append({'type':'heading','indices':[0]});P.append(pair('Answers of MCQs','کثیر انتخابی سوالات کے جوابات','د څو انتخابي پوښتنو ځوابونه'))
rows=[[f'Unit-{u}']+[f'{i+1}. {a}' for i,a in enumerate(v.split())]+['']*(15-len(v.split())) for u,v in KEY.items()]
hdr=['Unit']+[str(i) for i in range(1,16)]
tb={'id':'chem12-mcq-answers','headers':hdr,'rows':[[r[0]]+[c.split('. ')[1] if c else '' for c in r[1:]] for r in rows],
 'translations':[{'language':'اردو','headers':['یونٹ']+hdr[1:],'rows':[[f'یونٹ-{r[0][5:]}']+[c.split('. ')[1] if c else '' for c in r[1:]] for r in rows]},
  {'language':'پښتو','headers':['واحد']+hdr[1:],'rows':[[f'واحد-{r[0][5:]}']+[c.split('. ')[1] if c else '' for c in r[1:]] for r in rows]}]}
B.append(tb);L.append({'type':'sourceDataTable','tableId':tb['id']})
r=section('24.14','Answers of MCQs (Units 13–24)','کثیر انتخابی سوالات کے جوابات (یونٹ 13–24)','د څو انتخابي پوښتنو ځوابونه (واحدونه 13–24)',P,L,B,'384–385')
r['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':195,'printedPages':[384,385]}];r['sourceContinuesOnPdfPage']=196
r['sourceNote']='Printed key for Unit 20 lists only MCQs 1–10, matching the ten MCQs printed in Unit 20.'
carry=[{'from':'24.14','to':'24.15','startsAt':'GLOSSARY'}]
if __name__=='__main__':save(195,[r],carry=carry,chapter_number=24)
