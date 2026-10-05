from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
import json, re, html
ROOT=Path(r'D:\SpaceBook\Books\12th'); OUT=Path(r'D:\SpaceBook\SpaceBook Web\js')
NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
BOOKS={
 'math':('12th Maths',1,12,[
 'Introduction to Symbolic Package, Maple','Functions and Limits','Differentiation','Higher Order Derivatives and Applications','Differentiation of Vector Functions','Integration','Plane Analytic Geometry: Straight Line','Conics I','Conics II','Differential Equations','Partial Differentiation','Introduction to Numerical Methods']),
 'phys':('12th Physics',11,20,['Electrostatics','Current Electricity','Electromagnetism','Electromagnetic Induction','Alternating Current','Physics of Solids','Electronics','Dawn of Modern Physics','Atomic Spectra','Nuclear Physics']),
 'chem':('12th Chemistry',13,24,['s and p-Block Elements','d and f-Block Elements: Transition Elements','Organic Compounds','Hydrocarbons','Alkyl Halides and Amines','Alcohols, Phenols and Ethers','Carbonyl Compounds I: Aldehydes and Ketones','Carbonyl Compounds II: Carboxylic Acids and Functional Derivatives','Biochemistry','Industrial Chemistry','Environmental Chemistry','Analytical Chemistry']),
 'stat':('12th Statistics',1,9,['Probability','Random Variables and Probability Distributions','Special Discrete Probability Distributions','Special Continuous Probability Distributions','Sampling and Sampling Distributions','Estimation','Hypothesis Testing','Association of Attributes','Experimental Design'])}

def read_paras(folder):
    out=[]
    for file in sorted((ROOT/folder/'Word').glob('*.docx')):
        with ZipFile(file) as z:
            root=ET.fromstring(z.read('word/document.xml'))
        for p in root.findall('.//w:p',NS):
            s=''.join(t.text or '' for t in p.findall('.//w:t',NS)).strip()
            if s: out.append(s)
    return out

def chapter_starts(key, paras, lo, hi):
    if key=='chem':
        # Body headings from the source transcription; a later rising section number is used for the carbonyl split.
        starts=[95,1721,3095,3670,6007,7303]
        match=next((i for i,s in enumerate(paras) if i>7303 and i<9660 and re.match(r'^\s*19[.\s]',s)), None)
        starts.append(match if match is not None else 8696)
        starts += [9660,10546,11775,12537,13131]
        starts=[max(0,min(i,len(paras)-1)) for i in starts]
        return starts
    pattern=re.compile(r'^\s*UNIT\s*[-.]?\s*(\d{1,2})\b|^\s*Unit\s*[-.]?\s*(\d{1,2})\b',re.I)
    starts=[]; want=lo
    for i,s in enumerate(paras):
        m=pattern.match(s)
        if not m: continue
        n=int(m.group(1) or m.group(2))
        # Keep only the first source-order occurrence of each next unit to ignore repeating page headers.
        if n==want:
            starts.append(i); want+=1
            if want>hi: break
    if len(starts)!=(hi-lo+1):
        raise RuntimeError(f'{key}: found {len(starts)} unit starts, expected {hi-lo+1}; next={want}')
    return starts

# Compact vector diagrams: page-native SVG markup, not raster images.
def svg_for(key,n,title):
    common='<svg viewBox="0 0 460 210" role="img" aria-label="'+html.escape(title,quote=True)+'" style="width:min(100%,460px);height:auto;background:#fff;border:1px solid #dbeafe;border-radius:10px;margin:12px 0"><path d="M55 170H420M75 185V25" stroke="#334155" stroke-width="2"/><text x="220" y="202" fill="#334155" font-size="13">x / independent variable</text><text x="12" y="22" fill="#334155" font-size="13">y</text>'
    if key=='math':
        if n in (7,8,9):
            shape='<path d="M110 150 Q230 -15 350 150" fill="none" stroke="#2563eb" stroke-width="3"/><path d="M80 75H390" stroke="#dc2626" stroke-width="2" stroke-dasharray="6 5"/><text x="250" y="65" fill="#b91c1c" font-size="14">tangent / directrix</text>'
        elif n in (2,3,4,5,6,10,11,12):
            shape='<path d="M90 155 C145 150 155 55 235 75 S325 130 385 30" fill="none" stroke="#2563eb" stroke-width="3"/><path d="M190 101L280 58" stroke="#dc2626" stroke-width="2"/><circle cx="235" cy="75" r="4" fill="#dc2626"/><text x="290" y="48" fill="#b91c1c" font-size="13">slope / rate</text>'
        else:
            shape='<path d="M90 150 C125 70 175 70 210 150 S295 230 335 85 S385 60 400 120" fill="none" stroke="#2563eb" stroke-width="3"/><text x="210" y="40" fill="#1d4ed8" font-size="14">Maple: symbolic output</text>'
    elif key=='stat':
        shapes={
            1:'<circle cx="205" cy="105" r="48" fill="#dbeafe" stroke="#2563eb" stroke-width="3"/><circle cx="260" cy="105" r="48" fill="#dcfce7" fill-opacity=".8" stroke="#16a34a" stroke-width="3"/><text x="180" y="110" font-size="16">A</text><text x="274" y="110" font-size="16">B</text><text x="222" y="110" font-size="13">A∩B</text>',
            2:'<rect x="125" y="130" width="38" height="40" fill="#93c5fd"/><rect x="180" y="90" width="38" height="80" fill="#60a5fa"/><rect x="235" y="55" width="38" height="115" fill="#3b82f6"/><rect x="290" y="105" width="38" height="65" fill="#60a5fa"/><text x="145" y="190" font-size="13">x</text><text x="246" y="45" font-size="13">P(X=x)</text>',
            3:'<rect x="130" y="145" width="35" height="25" fill="#a78bfa"/><rect x="178" y="110" width="35" height="60" fill="#8b5cf6"/><rect x="226" y="68" width="35" height="102" fill="#7c3aed"/><rect x="274" y="95" width="35" height="75" fill="#8b5cf6"/><rect x="322" y="130" width="35" height="40" fill="#a78bfa"/><text x="200" y="45" font-size="14">Discrete distribution</text>',
            4:'<path d="M100 165 C145 155 165 55 235 45 C305 55 325 155 370 165" fill="none" stroke="#7c3aed" stroke-width="4"/><path d="M235 45V170" stroke="#16a34a" stroke-width="2" stroke-dasharray="5 4"/><text x="245" y="58" fill="#166534" font-size="13">μ</text>',
            5:'<path d="M95 165 C135 150 155 65 230 48 C305 65 325 150 375 165" fill="none" stroke="#0284c7" stroke-width="3"/><path d="M130 165 C160 155 178 105 230 93 C282 105 300 155 340 165" fill="none" stroke="#f97316" stroke-width="3"/><text x="190" y="40" font-size="13">population / sample means</text>',
            6:'<path d="M95 165 C140 155 170 65 235 50 C300 65 330 155 375 165" fill="none" stroke="#2563eb" stroke-width="3"/><path d="M150 162V120M320 162V120M150 145H320" stroke="#dc2626" stroke-width="3"/><text x="220" y="138" font-size="13">confidence interval</text>',
            7:'<path d="M95 165 C140 155 170 65 235 50 C300 65 330 155 375 165" fill="none" stroke="#2563eb" stroke-width="3"/><path d="M320 125 C340 145 350 160 375 165V125Z" fill="#fecaca" stroke="#dc2626"/><text x="321" y="112" font-size="13">rejection region</text>',
            8:'<rect x="112" y="58" width="235" height="110" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/><path d="M225 58V168M112 113H347" stroke="#2563eb" stroke-width="2"/><text x="133" y="91" font-size="14">A</text><text x="255" y="91" font-size="14">B</text><text x="126" y="142" font-size="14">C</text><text x="255" y="142" font-size="14">D</text><text x="148" y="190" font-size="13">attribute contingency table</text>',
            9:'<g fill="#dcfce7" stroke="#059669" stroke-width="2"><rect x="125" y="55" width="70" height="40"/><rect x="215" y="55" width="70" height="40"/><rect x="305" y="55" width="70" height="40"/><rect x="125" y="112" width="70" height="40"/><rect x="215" y="112" width="70" height="40"/><rect x="305" y="112" width="70" height="40"/></g><text x="140" y="81" font-size="13">R₁</text><text x="230" y="81" font-size="13">R₂</text><text x="320" y="81" font-size="13">R₃</text><text x="175" y="184" font-size="13">Randomized treatments / blocks</text>'
        }
        shape=shapes.get(n,'')
    elif key=='phys':
        shapes={11:'<circle cx="230" cy="105" r="34" fill="#fef3c7" stroke="#d97706" stroke-width="3"/><path d="M120 55Q230 -5 340 55M120 155Q230 215 340 155M140 45V165M320 45V165" fill="none" stroke="#2563eb" stroke-width="2"/><text x="216" y="110" font-size="18">+q</text>',12:'<path d="M150 90H225M265 90H340M225 90V145H265V90" fill="none" stroke="#dc2626" stroke-width="4"/><circle cx="245" cy="90" r="24" fill="#fff" stroke="#2563eb" stroke-width="3"/><text x="238" y="96" font-size="13">R</text><text x="185" y="72" font-size="14">I →</text>',13:'<circle cx="230" cy="105" r="5" fill="#dc2626"/><path d="M230 105V35M230 105V175M230 105H155M230 105H305" stroke="#2563eb" stroke-width="3"/><text x="242" y="45" font-size="14">B</text>',14:'<rect x="185" y="63" width="90" height="82" fill="#eff6ff" stroke="#2563eb" stroke-width="3"/><path d="M90 104H180M280 104H370" stroke="#dc2626" stroke-width="3"/><text x="200" y="110" font-size="15">Φ changes</text>',15:'<path d="M75 105 C110 15 150 15 185 105 S260 195 295 105 S370 15 405 105" fill="none" stroke="#2563eb" stroke-width="3"/><text x="330" y="50" font-size="14">AC wave</text>',16:'<g fill="#dbeafe" stroke="#2563eb" stroke-width="2"><circle cx="160" cy="65" r="19"/><circle cx="230" cy="65" r="19"/><circle cx="300" cy="65" r="19"/><circle cx="195" cy="130" r="19"/><circle cx="265" cy="130" r="19"/></g>',17:'<path d="M175 130L230 45L285 130Z" fill="#fef3c7" stroke="#b45309" stroke-width="3"/><text x="204" y="122" font-size="14">p-n</text>',18:'<path d="M100 150H380M130 150V70M220 150V40M310 150V15" stroke="#7c3aed" stroke-width="4"/><text x="132" y="65" font-size="13">E₁</text><text x="224" y="35" font-size="13">E₂</text><path d="M130 70L220 40" stroke="#dc2626" stroke-width="2"/>',19:'<path d="M145 45H300M145 105H300M145 165H300" stroke="#2563eb" stroke-width="3"/><path d="M225 102V50" stroke="#dc2626" stroke-width="3"/><text x="312" y="49" font-size="13">energy levels</text>',20:'<circle cx="230" cy="105" r="48" fill="#fef3c7" stroke="#d97706" stroke-width="3"/><text x="202" y="110" font-size="15">nucleus</text><path d="M285 90Q340 45 375 25M280 120Q335 165 375 185" stroke="#7c3aed" stroke-width="3"/><text x="360" y="32" font-size="13">α / β / γ</text>'}
        shape=shapes.get(n,'')
    else:
        shape='<path d="M90 160 C145 155 170 125 200 95 S270 55 370 45" fill="none" stroke="#059669" stroke-width="3"/><circle cx="200" cy="95" r="5" fill="#dc2626"/><text x="245" y="90" fill="#334155" font-size="14">book relationship</text>'
        if key=='chem':
            chem_shapes={
                13:'<rect x="120" y="55" width="220" height="105" fill="#eff6ff" stroke="#2563eb" stroke-width="3"/><path d="M175 55V160M230 55V160M285 55V160M120 108H340" stroke="#60a5fa"/><text x="152" y="92" font-size="18">s block</text><text x="243" y="92" font-size="18">p block</text><text x="176" y="140" font-size="16">periodic-table regions</text>',
                14:'<circle cx="230" cy="105" r="62" fill="#fef3c7" stroke="#d97706" stroke-width="3"/><path d="M180 105H280M205 62L255 148M255 62L205 148" stroke="#2563eb" stroke-width="3"/><text x="216" y="110" font-size="17">d orbitals</text>',
                15:'<circle cx="230" cy="105" r="12" fill="#fbbf24" stroke="#b45309"/><path d="M230 93L190 55M242 105L282 65M230 117L190 155M218 105L178 145" stroke="#2563eb" stroke-width="3"/><circle cx="185" cy="50" r="10" fill="#dbeafe" stroke="#2563eb"/><circle cx="287" cy="60" r="10" fill="#dbeafe" stroke="#2563eb"/><circle cx="185" cy="160" r="10" fill="#dbeafe" stroke="#2563eb"/><circle cx="173" cy="150" r="10" fill="#dbeafe" stroke="#2563eb"/><text x="215" y="190" font-size="14">organic covalent structure</text>',
                16:'<path d="M120 125L165 90L210 125L255 90L300 125" fill="none" stroke="#2563eb" stroke-width="4"/><circle cx="340" cy="95" r="42" fill="none" stroke="#7c3aed" stroke-width="3"/><path d="M310 65L370 125M370 65L310 125" stroke="#7c3aed" stroke-width="2"/><text x="135" y="155" font-size="13">alkane / alkene chains</text><text x="316" y="157" font-size="13">benzene ring</text>',
                17:'<text x="100" y="115" font-size="21">R—X</text><text x="188" y="115" font-size="21">+</text><text x="218" y="115" font-size="21">NH₃</text><path d="M280 108H330" stroke="#059669" stroke-width="3"/><path d="M319 98L330 108L319 118" fill="none" stroke="#059669" stroke-width="3"/><text x="345" y="115" font-size="20">R—NH₂</text><text x="180" y="155" font-size="14">substitution / amination</text>',
                18:'<text x="105" y="112" font-size="21">R—OH</text><text x="225" y="112" font-size="21">Ar—OH</text><text x="335" y="112" font-size="21">R—O—R′</text><text x="132" y="155" font-size="14">alcohol</text><text x="238" y="155" font-size="14">phenol</text><text x="345" y="155" font-size="14">ether</text>',
                19:'<text x="92" y="115" font-size="20">R—C(=O)—H</text><text x="255" y="115" font-size="20">R—C(=O)—R′</text><text x="123" y="155" font-size="14">aldehyde</text><text x="300" y="155" font-size="14">ketone</text>',
                20:'<text x="85" y="110" font-size="18">R—C(=O)—OH</text><path d="M220 103H260" stroke="#059669" stroke-width="3"/><path d="M250 93L260 103L250 113" fill="none" stroke="#059669" stroke-width="3"/><text x="273" y="110" font-size="17">ester / amide</text><text x="155" y="155" font-size="14">carboxyl derivatives</text>',
                21:'<circle cx="180" cy="105" r="40" fill="#fef3c7" stroke="#d97706" stroke-width="3"/><circle cx="280" cy="105" r="40" fill="#dcfce7" stroke="#16a34a" stroke-width="3"/><path d="M220 105H240" stroke="#334155" stroke-width="3"/><text x="153" y="111" font-size="15">sugar</text><text x="253" y="111" font-size="15">amino acid</text><text x="188" y="170" font-size="14">biomolecules</text>',
                22:'<rect x="95" y="70" width="90" height="55" rx="8" fill="#dbeafe" stroke="#2563eb"/><rect x="225" y="70" width="90" height="55" rx="8" fill="#dcfce7" stroke="#059669"/><path d="M188 98H215" stroke="#334155" stroke-width="3"/><path d="M205 88L215 98L205 108" fill="none" stroke="#334155" stroke-width="3"/><text x="112" y="103" font-size="14">raw feed</text><text x="241" y="103" font-size="14">product</text><text x="155" y="160" font-size="14">industrial process</text>',
                23:'<circle cx="150" cy="90" r="28" fill="#dbeafe" stroke="#2563eb" stroke-width="3"/><circle cx="230" cy="90" r="28" fill="#dcfce7" stroke="#059669" stroke-width="3"/><circle cx="310" cy="90" r="28" fill="#fee2e2" stroke="#dc2626" stroke-width="3"/><path d="M178 90H200M258 90H280" stroke="#334155" stroke-width="3"/><text x="125" y="145" font-size="14">air</text><text x="201" y="145" font-size="14">water</text><text x="287" y="145" font-size="14">soil</text><text x="163" y="175" font-size="14">environmental pathways</text>',
                24:'<path d="M110 145H370M125 145V115M155 145V90M185 145V65M215 145V105M245 145V75M275 145V120M305 145V55M335 145V95" stroke="#7c3aed" stroke-width="7"/><path d="M100 145H390" stroke="#334155" stroke-width="2"/><text x="160" y="180" font-size="14">analytical signal / spectrum</text>'
            }
            shape=chem_shapes.get(n,'')
    if key=='chem' or (key=='stat' and n in (8,9)):
        return common.split('<path d=',1)[0]+shape+'</svg>'
    return common+shape+'</svg>'

def extract_practice_items(body):
    """Keep textbook examples and exercises as source text, in their original order."""
    examples=[]; exercises=[]
    blocks=[]; current=None
    example_re=re.compile(r'^\s*(?:worked\s+)?example\s*(?:\d+|[ivxlcdm]+)?\b',re.I)
    exercise_re=re.compile(r'^\s*(?:review\s+)?exercises?\s*(?:\d+(?:\.\d+)*|[ivxlcdm]+)?\b',re.I)
    for line in body:
        if example_re.match(line):
            if current: blocks.append(current)
            current={'kind':'example','title':line.strip(),'lines':[line.strip()]}
        elif exercise_re.match(line):
            if current: blocks.append(current)
            current={'kind':'exercise','title':line.strip(),'lines':[line.strip()]}
        elif current:
            # Stop a captured item at the next major unit heading only; preserve
            # solution and question paragraphs verbatim between markers.
            current['lines'].append(line)
    if current: blocks.append(current)
    for i,item in enumerate(blocks):
        text='\n'.join(item['lines']).strip()
        if item['kind']=='example':
            examples.append({'id':f'textbook-example-{i+1}','title':item['title'],'problem':text,'given':'','method':'See the source text below.','steps':[],'answer':''})
        else:
            exercises.append({'exercise':item['title'],'title':item['title'],'problems':[{'qNo':str(j+1),'question':line,'solution':'','answer':''} for j,line in enumerate(item['lines'][1:],1) if line.strip()]})
    return examples,exercises

for key,(folder,lo,hi,titles) in BOOKS.items():
    paras=read_paras(folder); starts=chapter_starts(key,paras,lo,hi)
    front=paras[:starts[0]]; chapters=[]
    for idx,start in enumerate(starts):
        end=starts[idx+1] if idx+1<len(starts) else len(paras)
        n=lo+idx; title=titles[idx]; body=paras[start:end]
        # Strip empty values but otherwise preserve the source wording and line order.
        # Split the complete source lesson into readable sections. No source
        # paragraphs are discarded by the lesson view.
        chunks=[body[i:i+80] for i in range(0,len(body),80)]
        sections=[]
        for j, lines in enumerate(chunks):
            if not lines: continue
            content='\n'.join(lines)
            sections.append({'id':f'{n}.{j+1}','title':('Learning outcomes & introduction' if j==0 else 'Textbook lesson extract '+str(j)), 'theory':html.escape(content),'content':html.escape(content).replace(chr(10),'<br>'),'rules':[],'sciNote':content[:1500]})
        # Build study answers from the first explanatory textbook paragraphs,
        # leaving the unit's separately transcribed learning outcomes in the book view.
        objective=re.compile(r'^\s*(?:[•⚫·]\s*)?(?:define|describe|draw|sketch|state|derive|explain|calculate|apply|recognize|recognise|determine|compare|illustrate|understand|know|identify|discuss|elaborate|classify|write|solve|find|construct|analyze|analyse|prove|compute|use|differentiate|show|give|demonstrate|evaluate)\b',re.I)
        core=[line for line in body if len(line)>70 and not re.match(r'^\s*(?:UNIT|Unit)\s*[-.]?\s*\d+\b',line,re.I)
              and not objective.match(line)
              and not any(marker in line.lower() for marker in ('after studying this unit','by the end of this unit','students will be able to','learning outcomes','(remembering)','(understanding)','(applying)','(analyzing)','(evaluating)','(creating)'))]
        if not core: core=body
        source='\n'.join(core[:4])
        long_answer='\n'.join(core[:10])
        others=[t for t in titles if t!=title]
        opts=[title]+others[:3]
        worked_examples, textbook_exercises = extract_practice_items(body)
        chapters.append({'number':n,'num':n,'title':title,'name':title,'pageRange':'KPK Textbook · Unit '+str(n),'sections':sections,'topics':sections,'textbookText':body,'textbookFrontMatter':front if idx==0 else [],'textbookBackMatter':[],'workedExamples':worked_examples,'exercises':textbook_exercises,'formulaSheet':[],'definitions':[{'term':title,'def':html.escape(source[:2200])}],'numericals':[],'sloQuestions':{'mcqs':[{'q':'Which textbook unit does this topic belong to?','options':opts,'correct':0,'explanation':title+' is the subject of this unit.'}],'shortQuestions':[{'q':'State and explain the central idea of '+title+'.','ans':html.escape(source)}],'longQuestions':[{'q':'Explain '+title+' using the definitions, principles, equations and examples presented in this unit.','marks':8,'rubric':'Use the textbook explanation, relevant notation and worked examples.','sol':html.escape(long_answer)}]},'sloBank':{'mcqs':[],'shortQuestions':[],'longQuestions':[]},'diagramSvg':svg_for(key,n,title),'formulas':[]})
    if key!='math':
        for ch in chapters:
            eqs=[line for line in ch['textbookText'] if len(line)<180 and re.search(r'(?:=|≈|∝|→|Δ|∫|√|Σ|σ|π|\\\\frac|\\\\sum)',line) and len(re.findall(r'[A-Za-z0-9]',line))>3][:8]
            ch['formulas']=[{'name':'Textbook equation','formula':html.escape(line),'note':'Transcribed from the supplied textbook Word source.'} for line in eqs]
            if ch['sections']:
                ch['sections'][0]['content'] += ch['diagramSvg']
                ch['sections'][0]['theory'] += html.escape(ch['diagramSvg'])
                ch['sections'][0]['diagramSvg'] = ch['diagramSvg']
    if key=='math':
        # Populate real formula families using textbook notation for calculus and conics.
        forms={
            2:['limₓ→ₐ f(x) = L','Continuity at a: limₓ→ₐ f(x) = f(a)'],
            3:['d(xⁿ)/dx = n xⁿ⁻¹','d(uv)/dx = u·dv/dx + v·du/dx'],
            4:['d²y/dx² = d/dx(dy/dx)','d(eˣ)/dx = eˣ'],
            5:['d r⃗(t)/dt = v⃗(t)','d(a⃗·b⃗)/dt = a⃗′·b⃗ + a⃗·b⃗′'],
            6:['∫xⁿ dx = xⁿ⁺¹/(n + 1) + C, n ≠ −1','∫u dv = uv − ∫v du'],
            7:['y − y₁ = m(x − x₁)','Ax + By + C = 0'],
            8:['(x − h)² + (y − k)² = r²','x²/a² + y²/b² = 1'],
            9:['y² = 4ax','x²/a² − y²/b² = 1'],
            10:['dy/dx = f(x)g(y)','y′ + Py = Q'],
            11:['∂f/∂x','∇f = (fₓ, fᵧ, f_z)'],
            12:['f′(x) ≈ [f(x + h) − f(x)]/h','xₙ₊₁ = xₙ − f(xₙ)/f′(xₙ)']
        }
        for ch in chapters:
            ch['formulaSheet']=forms.get(ch['number'],[])
            ch['formulaSheet']=[{'name':'Key notation','formula':f,'note':'Use the textbook derivation and conditions for this identity.'} for f in ch['formulaSheet']]
            for sec in ch['sections']:
                sec['theory'] += '\n\n'+ch['diagramSvg']
    var={'math':'MATH_12_DATA','phys':'PHYS_12_DATA','chem':'CHEM_12_DATA','stat':'STAT_12_DATA'}[key]
    # math renderer expects textbookText property; other views use the same compatible renderer.
    target=OUT/f'{key}_12_data.js'
    target.write_text('// Class 12 '+key+' textbook data, transcribed from the supplied Word parts.\nconst '+var+' = '+json.dumps(chapters,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
    print(key,'units',len(chapters),'source paragraphs',sum(map(lambda c:len(c['textbookText']),chapters)),'chars',sum(sum(len(x) for x in c['textbookText']) for c in chapters),'file bytes',target.stat().st_size)


