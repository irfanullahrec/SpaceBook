"""Save honest progress from checked outputs, not from task aspirations."""
from pathlib import Path
from datetime import datetime,timezone
import json
ROOT=Path(__file__).resolve().parents[1]
checkpoint=ROOT/'math/continuation-checkpoint.json'
before=checkpoint.read_text(encoding='utf-8');d=json.loads(before)
answers=json.loads((ROOT/'math/authored-solutions.json').read_text(encoding='utf-8'))
reviews=[json.loads((ROOT/f'math/unit{i}-answer-review.json').read_text(encoding='utf-8')) for i in [1,2,3]]
assert [r['answeredLeaves'] for r in reviews]==[85,72,78]
batch_files=sorted((ROOT/'math').glob('probability-*-review.json'))
batches=[json.loads(p.read_text(encoding='utf-8')) for p in batch_files]
assert batches[0]['answeredLeaves']==34
batch=batches[-1]
end=datetime.fromisoformat(batch['checkedAt'].replace('Z','+00:00'));start=datetime(2026,10,18,6,3,11,tzinfo=timezone.utc)
seconds=(end-start).total_seconds()
represented=len(list((ROOT/'math/pages').glob('p[0-9][0-9][0-9].txt')))
d.update(updatedAt=datetime.now(timezone.utc).isoformat(),transcribedScans=represented,nextNewTranscript=f'pages/p{represented:03}.txt',answeredExerciseLeaves=len(answers),answerUnitsChecked=[1,2,3],additionalExercisesChecked=['6.4']+(['6.5','Review 6'] if len(batches)>=3 else []),nextAnswerTask='Unit 4 Sequences and Series: all exercise answers still pending. Unit 5 and earlier Unit 6 exercises also need answers.',verification=['unit1-answer-review.json','unit2-answer-review.json','unit3-answer-review.json']+[p.name for p in batch_files],wordMeanings=batch['wordMeanings'])
for issue in d['sourceIssues']:
    if issue.get('scan')==85:issue.update(status='Repaired and checked',detail='Four instructional exercise figures restored as coded SVG; authored head-to-tail construction also rendered and visually inspected.')
if not any(i.get('scan')==193 for i in d['sourceIssues']):d['sourceIssues'].append(dict(scan=193,status='Preserved and explained',detail='Printed probability upper-bound numerator repeats n(E); separate correction explains n(S)/n(S)=1.'))
for source in batch.get('sourceIssues',[]):
    if not any(i.get('detail')==source['issue'] for i in d['sourceIssues']):
        d['sourceIssues'].append(dict(scan=source['scan'],status='Preserved and explained',detail=source['issue']))
checked_pages=sum(len(b['sourceScans']) for b in batches)
d['benchmark']=dict(startedAt=start.isoformat(),finishedAt=end.isoformat(),verifiedNewPages=checked_pages,elapsedSeconds=round(seconds,2),verifiedNewPagesPerHour=round(checked_pages*3600/seconds,2),targetPagesPerHour=400,includes='Source transcription, Urdu/Pashto translations, worked exercise parts, coded figures, cached OCR, vocabulary additions and focused checks.',note='Actual rate; target not achieved. Earlier answer completion is not counted as new pages.')
d['validationLimitation']='Whole-project tools/validate.js reports unrelated Class 2/3 dataset expectations and a Class 10 English load failure, then stops at Class 3 Mathematics schema. Other classes not modified. Focused Class 11 checks pass.'
d['sourceVerificationLimit']=f'{represented} scans are represented. This turn freshly compared Unit 1–3 exercise question pages and printed pages 192–{max(batch["printedPages"])}; inherited lesson pages are not newly verified wholesale.'
d['nextSourceTask']='Continue the independent-events theorem carried into p202.txt, then proceed sequentially. Never close the carried source container with invented text.' if represented==202 else f'Inspect and transcribe p{represented:03}.txt sequentially.'
assert checkpoint.read_text(encoding='utf-8')==before
checkpoint.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:d[k] for k in ['transcribedScans','answeredExerciseLeaves','wordMeanings','nextNewTranscript','benchmark']}))
