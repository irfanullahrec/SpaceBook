"""Repair presentation/translations on reviewed pages without advancing."""
import json
from physics_agent1_sequential import LEDGER, TRANSLATIONS, PROGRESS, ROOT, write_review

pages=json.loads(LEDGER.read_text(encoding='utf-8'))
translations=json.loads(TRANSLATIONS.read_text(encoding='utf-8'))
page9=next(page for page in pages if page['pdfPage']==9)
blocks=page9['sections'][0]['blocks']
quotations=[block for block in blocks if block['type']=='sourceQuotation']
phrases=[block for block in blocks if block['type']=='sourcePhrase']
quote_ps=[
 'لمر نه شي کولای چې سپوږمۍ راونیسي، او شپه له ورځې مخکې کېدای نه شي. هر یو په خپل مدار کې لامبو وهي.',
 'اې د پېریانو او انسانانو ډلې! که کولای شئ چې د اسمانونو او ځمکې له پولو ووځئ، نو ووځئ؛ تاسو به له واک او ځواک پرته ونه وځئ.',
 'هغه ذات چې اووه اسمانونه یې پوړ پر پوړ پیدا کړل. ته د رحمان په پیدایښت کې هېڅ ناانډولي نه وینې. بیا وګوره، آیا کومه چاودنه وینې؟'
]
phrase_ps=['آیا دوی فکر نه کوي؟','آیا دوی غور نه کوي؟','آیا خلک نه ګوري؟']
pairs=[]
for quote,ps in zip(quotations,quote_ps): pairs.extend([[quote['urdu'],ps] for _ in range(3)])
for phrase,ps in zip(phrases,phrase_ps): pairs.extend([[phrase['urdu'],ps] for _ in range(3)])
pairs.extend([
 ['عالمِ اسلام کی جانب سے طبعی سائنس میں خدمات','د اسلامي نړۍ له خوا په فزیکي ساینس کې ونډه'],
 ['عالمِ اسلام کے سائنس دانوں نے طبیعیات کی ترقی میں حصہ لیا۔ چند نمایاں سائنس دان یہ ہیں:', 'د اسلامي نړۍ ساینسپوهانو د فزیک په پرمختګ کې ونډه اخیستې ده. ځینې نامتو ساینسپوهان دا دي:'],
 ['یعقوب کندی (800–873) عیسوی','یعقوب کندي (800–873) میلادي'],
 ['وہ بصرہ، عراق میں پیدا ہوئے۔ انہوں نے علمِ پیمائش، مخصوص کششِ ثقل اور مدوجزر پر وسیع تحقیقی رسائل لکھے۔ ان کا سب سے اہم کام بصریات میں، خصوصاً روشنی کے انعکاس پر تھا۔','هغه د عراق په بصره کې زېږېدلی و. هغه د اندازه پوهنې، ځانګړي ثقل او مد او جزر په اړه پراخې څېړنیزې لیکنې کړې دي. د هغه تر ټولو مهم کار د رڼا پوهنې په برخه کې، په ځانګړي ډول د رڼا پر انعکاس و.']
])
translations['9']={'1.1':pairs}
TRANSLATIONS.write_text(json.dumps(translations,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
write_review(pages)
progress=json.loads(PROGRESS.read_text(encoding='utf-8'))
progress['presentationRules']=['No JPG/PNG images in topics','Person names as text','Arabic quotations as Unicode text','LaTeX metadata and vector formula/diagram rendering','Explicit Urdu and Pashto translations for each reviewed paragraph']
progress['translationCorrection']='All reviewed lesson paragraphs on PDF pages 6–11 now have explicit Urdu and Pashto translations.'
PROGRESS.write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Delete only this agent's unused topic crops, with an exact checked directory.
assets=(ROOT/'assets/physics9-agent1').resolve()
assert assets.parent == (ROOT/'assets').resolve()
if assets.exists():
    for path in assets.iterdir():
        if path.is_file() and path.suffix=='.png' and path.name.startswith('printed'): path.unlink()
print('Corrected reviewed-page translations and removed raster topic references.')
