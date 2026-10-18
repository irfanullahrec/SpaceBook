"""Keep unreadable endings explicit instead of displaying a completed reading."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
file=ROOT/'chemistry-page-151.json'
r=json.loads(file.read_text(encoding='utf-8'))
rows={p['id']:p for p in r['paras']}
rows['chem11-p151-question-9'].pop('sourceGap',None)
changes={
'chem11-p151-question-10':('10. At the same temperature and pressure which of the following gases has [scan obscured] greatest density.','10. یکساں درجہ حرارت اور دباؤ پر درج ذیل میں سے کس گیس کی [اسکین میں متن چھپا ہوا ہے] کثافت سب سے زیادہ ہے۔','10. په یوه تودوخه او فشار کې له لاندې ګازونو څخه د کوم یوه [په سکین کې متن پټ دی] کثافت تر ټولو زیات دی.'),
'chem11-p151-question-14':('14. At 50°C a gas has 1atm pressure, and 20dm³ volume, its volume at STP [scan obscured] be','14. 50°C پر ایک گیس کا دباؤ 1atm اور حجم 20dm³ ہے، STP پر اس کا حجم [اسکین میں متن چھپا ہوا ہے]','14. په 50°C کې د یوه ګاز فشار 1atm او حجم 20dm³ دی، په STP کې یې حجم [په سکین کې متن پټ دی]'),
'chem11-p151-short-1':('1. Justify that 1cm³ of hydrogen (H₂) and 1cm³ of methane (CH₄) at STP will [scan obscured] same number of molecules although one molecules of methane (CH₄) is 8 [scan obscured] heavier than that of hydrogen (H₂).','1. جواز دیں کہ STP پر ہائیڈروجن (H₂) کے 1cm³ اور میتھین (CH₄) کے 1cm³ میں سالموں کی تعداد برابر [اسکین میں متن چھپا ہوا ہے]، اگرچہ میتھین (CH₄) کا ایک سالمہ ہائیڈروجن (H₂) کے سالمے سے 8 [اسکین میں متن چھپا ہوا ہے] بھاری ہے۔','1. دلیل وړاندې کړئ چې په STP کې د هایدروجن (H₂) په 1cm³ او د میتان (CH₄) په 1cm³ کې د مالیکولونو شمېر یو شان [په سکین کې متن پټ دی]، که څه هم د میتان (CH₄) یو مالیکول د هایدروجن (H₂) تر مالیکول 8 [په سکین کې متن پټ دی] دروند دی.'),
'chem11-p151-short-2':('2. Do you think that some of the postulates of kinetic molecular theory of ga[scan obscured] are faulty? Write down these postulates.','2. کیا آپ کے خیال میں گیس[اسکین میں متن چھپا ہوا ہے] کے حرکی سالماتی نظریے کے بعض مفروضے ناقص ہیں؟ یہ مفروضے لکھیں۔','2. ایا ستاسو په اند د ګاز[په سکین کې متن پټ دی] د کینټیک مالیکولي تیورۍ ځینې فرضونه ناسم دي؟ دغه فرضونه ولیکئ.'),
'chem11-p151-short-5':('5. Why do you think that lighter gases can diffuse more rapidly than heavier on[scan obscured]','5. آپ کے خیال میں ہلکی گیسیں بھاری [اسکین میں متن چھپا ہوا ہے] سے زیادہ تیزی سے کیوں پھیل سکتی ہیں؟','5. ستاسو په اند سپک ګازونه ولې د درنو [په سکین کې متن پټ دی] په پرتله چټک خپرېدای شي؟')}
for id,triple in changes.items():
    rows[id].update(en=triple[0],ur=triple[1],ps=triple[2])
    rows[id]['sourceGap']={'note':'The right-edge curl obscures the fragment marked in the source text. Full-book and split PDFs have identical scans. No completed wording is substituted for that fragment.'}
r['sourceNote']='Question 9 is legible at enlarged resolution. The remaining curled-edge gaps in questions 10, 14 and short questions 1, 2, 5 are explicitly marked in all languages; earlier completed readings are not treated as verified. The full and split scans are identical.'
file.write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
