import json
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions
from physics_agent2_translations import TRANSLATIONS,TITLES
from physics_agent2_page011 import prepare
from class12_physics_printer_figures import figure
prepare()

if __name__=='__main__':
    old=json.loads((ROOT/'docs/source-verification/physics-agent2-pages.json').read_text(encoding='utf-8'))
    records=[r for r in old if r['pdfPage']==11]
    sections=[]
    for record,number in zip(records,['11.8','11.9','11.10']):
        identity=record['id']
        record.pop('figures',None)
        pairs=list(TRANSLATIONS[identity])
        if number=='11.8':
            layout=[{'type':'paragraph','indices':[0]},{'type':'paragraph','indices':[1]},
                    {'type':'paragraph','indices':[2]},{'type':'visual'},{'type':'paragraph','indices':[3]}]
        elif number=='11.9':
            layout=[{'type':'paragraph','indices':[0]},{'type':'visual'},{'type':'paragraph','indices':[1]}]
        else:
            record['paragraphs'].append('Quiz?')
            pairs.append(('مختصر سوال؟','لنډه پوښتنه؟'))
            layout=[{'type':'paragraph','indices':[0]},{'type':'visual'},{'type':'paragraph','indices':[1]},
                    {'type':'heading','indices':[3]},{'type':'paragraph','indices':[2]}]
        record['diagramHtml']=figure(number,'en')
        revised=section(record,[(p,*pair) for p,pair in zip(record['paragraphs'],pairs)],layout,TITLES[identity])
        revised['kind']='lesson'
        revised['diagramSvg']=figure(number,'en')
        revised['diagramSvgUrdu']=figure(number,'ur')
        revised['diagramSvgPashto']=figure(number,'ps')
        revised['content']+=revised['diagramSvg']
        sections.append(revised)
    upsert(records,sections)
    sync_companions(exercises=records[2]['exercises'])
    checkpoint(11,'corrected_verified',[r['id'] for r in records],
               'Full spread rendered at 3x and inspected. Selenium, xerography, laser and inkjet paragraphs compared and source grammar/inject spelling retained. Source raster Figures 11.8–11.10 replaced with coded optical/electrostatic apparatus: letter A on original paper/drum/printed sheet, lens/light paths and roller; laser fan, charge pattern and scanner; nozzle/charging unit/opposite deflection plates, straight uncharged versus curved negative charged-drop paths, gutter and paper. Every instructional caption and device label paired in Urdu/Pashto versions. Quiz heading retained, quiz source question upserted without authored answer.',printed_pages=[12,13])
