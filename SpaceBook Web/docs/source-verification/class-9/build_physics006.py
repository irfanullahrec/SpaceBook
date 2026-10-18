import json
import math
from pathlib import Path
OUT=Path(__file__).resolve().parent
page=json.loads((OUT.parent/'physics9-agent1.json').read_text(encoding='utf-8'))[5]
page.update(id='cls9-physics-page-006',status='inspected-corrected-unresolved',sourcePdf=r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf')
svg=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 320" role="img" aria-labelledby="cls9-physics-dashboard-title cls9-physics-dashboard-desc" style="max-width:100%;height:auto"><title id="cls9-physics-dashboard-title">Car dashboard measurement instruments</title><desc id="cls9-physics-dashboard-desc">Two main dials with needles near zero, with fuel and temperature gauges to either side. The source photograph illustrates measurement for safe driving. Tiny secondary scale and digital display remain unresolved in the scan.</desc><rect x="0" y="0" width="720" height="320" rx="25" fill="#232f38"/>']
def dial(cx,cy,r,maximum,increment):
    svg.extend([f'<circle cx="{cx}" cy="{cy}" r="{r+6}" fill="#182128" stroke="#a5b7c5" stroke-width="3"/>',f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#bfdbfe"/>'])
    for i in range(maximum//increment+1):
        angle=math.radians(150+i*240/(maximum/increment))
        x,y=cx+math.cos(angle)*(r-8),cy+math.sin(angle)*(r-8)
        x2,y2=cx+math.cos(angle)*(r-17),cy+math.sin(angle)*(r-17)
        tx,ty=cx+math.cos(angle)*(r-31),cy+math.sin(angle)*(r-31)
        svg.append(f'<path d="M{x:.1f} {y:.1f}L{x2:.1f} {y2:.1f}" stroke="#172554" stroke-width="2"/><text x="{tx:.1f}" y="{ty+4:.1f}" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#172554">{i*increment}</text>')
    svg.append(f'<path d="M{cx} {cy}l{-r*.85:.1f} {r*.46:.1f}" stroke="#9f1239" stroke-width="4"/><circle cx="{cx}" cy="{cy}" r="10" fill="#334155"/>')
dial(255,150,108,160,20)
dial(475,150,108,7,1)
for cx,label1,label2 in [(108,'E','F'),(626,'C','H')]:
    svg.append(f'<circle cx="{cx}" cy="210" r="58" fill="#bfdbfe" stroke="#a5b7c5" stroke-width="3"/><path d="M{cx-38} 217A40 40 0 1 1 {cx+38} 217" fill="none" stroke="#334155" stroke-width="2"/><text x="{cx-36}" y="220" font-size="14" fill="#172554">{label1}</text><text x="{cx+25}" y="190" font-size="14" fill="#172554">{label2}</text><path d="M{cx} 214l-30 -22" stroke="#9f1239" stroke-width="3"/><circle cx="{cx}" cy="214" r="7" fill="#334155"/>')
svg.append('</svg><p role="note"><strong>Editorial source-review note:</strong> Tiny secondary scale, instrument units and digital readout are unreadable in the source photograph; this illustration remains partially unresolved.<br><span lang="ur" dir="rtl">ادارتی نوٹ: اصل تصویر میں ثانوی پیمانے، آلات کی اکائیوں اور ڈیجیٹل اعداد کی باریک تحریر پڑھی نہیں جا سکی؛ اس خاکے کی تصدیق جزوی طور پر نامکمل ہے۔</span><br><span lang="ps" dir="rtl">ادارتي یادونه: په اصلي انځور کې د فرعي پیمانې، د وسایلو د واحدونو او ډیجیټلي لوستنې وړه لیکنه نه لوستل کېږي؛ د دې شکل بشپړ تایید لا نه دی شوی.</span></p>')
section=page['sections'][0]
section.update(heading=page['title'],headingUrdu='طبیعی مقداریں اور پیمائش',headingPashto='فزیکي کمیتونه او اندازه کول',sourceLayout=[dict(type='paragraph',indices=[0]),dict(type='visual'),dict(type='heading',indices=[1]),dict(type='list',indices=list(range(2,11)))],blocks=[dict(type='dashboard',id='cls9-physics-dashboard-001',svg=''.join(svg),sourcePdfPage=6,printedPage=1,reviewStatus='partial-unresolved-secondary-labels')])
page['unresolvedItems']=[{'location':'Opening dashboard photograph: tiny secondary speed scale, instrument units and digital display','reason':'Original embedded photograph is blurred. Inspected full page at 1.6x and dashboard crop at 4x; the corresponding split contains the same rendered image. Main dial geometry reconstructed, but unreadable labels/readout must not be guessed.','resolutionNeeded':'Clearer local scan of this dashboard image, if one is later found.','affects':'Full figure fidelity; page is not fully verified.'}]
page['comparison']='Fresh visual review confirmed title, caption and all nine source checklist items. Preserved existing aligned translations. Restored checklist as a real list and reconstructed visible dashboard instruments as inline SVG. Unreadable secondary labels/readout are explicitly unresolved; no completion claim.'
(OUT/'physics-page-006.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
