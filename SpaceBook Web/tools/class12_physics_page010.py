import json
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions
from physics_agent2_translations import TRANSLATIONS, TITLES
from physics_agent2_page010 import prepare
from class12_physics_field_figures import source_blocks
prepare()

if __name__ == '__main__':
    old = json.loads((ROOT / 'docs/source-verification/physics-agent2-pages.json').read_text(encoding='utf-8'))
    records = [r for r in old if r['pdfPage']==10]
    sections=[]
    for record in records:
        identity=record['id']
        if identity=='phys12-front-example112-solution':
            record['paragraphs'] = ['REQUIRED', r'electric field \(=E=?\)', 'SOLUTION', 'Using electric field intensity formulae']+record['paragraphs'][2:]
            pairs=[('مطلوب','غوښتل شوي'), (r'برقی میدان \(=E=?\)',r'برېښنايي میدان \(=E=?\)'), ('حل','حل'), ('برقی میدان کی شدت کا فارمولا استعمال کرتے ہوئے','د برېښنايي میدان د شدت د فورمول په کارولو سره')]+[(p,p) for p in record['paragraphs'][4:]]
            layout=[{'type':'heading','indices':[0]}, {'type':'paragraph','indices':[1]}, {'type':'heading','indices':[2]}, {'type':'paragraph','indices':[3]}]+[{'type':'equation','indices':[i]} for i in range(4,7)]
            previous=json.loads((ROOT/'docs/source-verification/class-12/physics-corrections.json').read_text(encoding='utf-8'))
            start=next(r for r in previous if r['id']=='phys12-front-example112-start')
            example=record['workedExamples'][0]
            example['problem']=start['paragraphs'][0]
            example['given']=start['paragraphs'][2:4]
            example['required']=[record['paragraphs'][1]]
            example['steps']=record['paragraphs'][3:]
        elif identity=='phys12-front-field-lines':
            record.pop('figures',None)
            blocks=source_blocks()
            record['sourceBlocks']=blocks
            record['paragraphs'].append('[Editorial clarification: the printed reference to Fig. (11.5) is inconsistent; Figure 11.4 shows opposite charges, while Figure 11.5 shows two positive charges. The source reference is retained.]')
            pairs=TRANSLATIONS[identity]+[('[ادارتی وضاحت: کتاب میں شکل (11.5) کا حوالہ متناقض ہے؛ شکل 11.4 میں مخالف بار ہیں جبکہ شکل 11.5 میں دو مثبت بار ہیں۔ اصل حوالہ محفوظ رکھا گیا ہے۔]', '[د سمونوال وضاحت: په کتاب کې د شکل (11.5) حواله ناسمه ده؛ شکل 11.4 مخالف چارجونه ښيي، خو شکل 11.5 دوه مثبت چارجونه ښيي. اصلي حواله ساتل شوې ده.]')]
            layout=[{'type':'paragraph','indices':[0]}, {'type':'paragraph','indices':[1]},
                    {'type':'visual','blockId':blocks[0]['id']}, {'type':'visual','blockId':blocks[1]['id']},
                    {'type':'paragraph','indices':[2]}, {'type':'paragraph','indices':[3]},
                    {'type':'paragraph','indices':[6]}, {'type':'paragraph','indices':[4]},
                    {'type':'visual','blockId':blocks[2]['id']}, {'type':'paragraph','indices':[5]},
                    {'type':'visual','blockId':blocks[3]['id']}]
        else:
            record['paragraphs'].append('APPLICATIONS OF ELECTROSTATICS')
            pairs=TRANSLATIONS[identity]+[('برقِ سکونی کے اطلاقات','د ساکنې برېښنا کارونې')]
            layout=[{'type':'heading','indices':[1]},{'type':'paragraph','indices':[0]}]
        revised=section(record,[(p,*pair) for p,pair in zip(record['paragraphs'],pairs)],layout,TITLES[identity])
        revised['kind']='lesson'
        if identity=='phys12-front-field-lines':
            revised['sourceBlocks']=record['sourceBlocks']
            revised['diagramSvg']=''.join(b['svg'] for b in record['sourceBlocks'])
            revised['diagramSvgUrdu']=''.join(b['svgUrdu'] for b in record['sourceBlocks'])
            revised['diagramSvgPashto']=''.join(b['svgPashto'] for b in record['sourceBlocks'])
            revised['content']+=revised['diagramSvg']
            revised['paras'][6]['isEditorial']=True
            revised['paras'][6]['originalText']=None
        sections.append(revised)
    upsert(records,sections)
    sync_companions(worked_examples=records[0]['workedExamples'])
    checkpoint(10,'corrected_verified',[r['id'] for r in records],
               'Original complete spread inspected at 3x. Example 11.2 required/solution headings separated from prose, all three formula/substitution/result lines and full page-9 given conversions retained in worked-example view. All six field-line paragraphs compared; printed Fig 11.5 mismatch retained and editorial clarification separately paired. Figures 11.4–11.7 reconstructed with native SVG field geometry, charge signs, arrows, tangent-point labels A/B/C/D and E/F, plate signs/fringing, equipotential rings and normal termination at metal surface. Source raster figures removed from active source records and lesson/topic data; captions translated per figure. Applications heading restored, photocopier opening paragraph retained.',printed_pages=[10,11])
