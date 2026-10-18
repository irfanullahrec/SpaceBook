import json
from pathlib import Path
OUT = Path(__file__).parent
data = json.loads((OUT/'inventory.json').read_text(encoding='utf-8'))
records = json.loads((OUT/'physics-pages.json').read_text(encoding='utf-8'))
last = int(__import__('sys').argv[1])
for page in range(3, last+1):
    if any(r['pdfPage']==page for r in records):
        continue
    records.append({'pdfPage':page,'printedPage':'1' if page==3 else None,'status':'corrected','kind':{3:'publication credits',4:'Quranic verse in Urdu',5:'contents'}.get(page,'lesson'),'compared':'Visible source text, punctuation, heading hierarchy, reading order and original language; explicit English/Urdu/Pashto paired records. Decorative borders, scan watermark and handwriting excluded.','data':'js/physics_10_source_data.js','evidence':f'tmp/class-10-physics/pdf{page:03d}.png','validation':'node syntax and focused non-browser class-10 validate_physics.cjs passed; no raster lesson content.'})
book = data['subjects'][0]['books'][0]
for record in records:
    if 6 <= record['pdfPage'] <= 9:
        record['printedPage'] = str(record['pdfPage']-5)
    if record['pdfPage'] == 10:
        record['printedPage'] = '6'
        record['comparison'] = 'Example 10.2 question, GIVEN/REQUIRED, full source calculation including cancellations, answer and Figure 10.4 labels; Assignment 10.2 without invented answer; 10.3.1 derivation with equation labels 1 and 2; Angular Frequency TIP. All paired translations and native SVG/KaTeX code.'
    if record['pdfPage'] == 11:
        record['printedPage'] = '5'
        record['comparison'] = 'Spring-motion proof: all original paragraphs, F_res ∝ -x, Hooke/Newton equations numbered 1/2 and 10.4, final a ∝ x as printed; Figure 10.3 stretched/equilibrium/compressed positions, spring lengths, restoring directions, displacement labels, zero-force label. Source Hook/Hooke/Hooks spellings retained; paired translations. Inserted before PDF page 10 content by printed order, without duplicating records.'
    if record['pdfPage'] == 12:
        record['printedPage'] = '7'
        record['comparison'] = 'Square-root continuation, full time-period paragraph, equations 10.5 and 10.6, amplitude independence statement, Example 10.3 original question/GIVEN/REQUIRED/full solution with squaring, isolation, substitution, unit cancellations, 2.02 kg = 2 kg and final 2.0 kg source wording. Uppercase K in isolation retained as printed. All three language fields and real KaTeX checked.'
    if record['pdfPage'] == 13:
        record['printedPage'] = '8'
        record['comparison'] = 'Assignment 10.3 source 0.2 kg and 4 N/m question only; original simple-pendulum definition, weight paragraph, three distinct bullet conditions, full force-component proof, numbered equations 1/2, small-angle arc statement; Figure 10.5 with O/P/Q/R/S, lengths l, displacement x, arc s, tension T and radial/tangential weight components. Original wording retained; paired translations, semantic list, locally inspected native SVG.'
    if record['pdfPage'] == 14:
        record['printedPage'] = '9'
        record['comparison'] = 'Pendulum proof continued: numbered equations 3/4 and 10.7 with cancelled masses, restoring direction and inertia paragraph. Example 10.4 source question, GIVEN/REQUIRED, original solution introduction and negative restoring-force formula; Figure 10.6 coded weight/components and ten-degree labels. Example continues on the next PDF page and is explicitly marked continuationExpected. Source awkward phrasing and F_rest/F_res notation retained; three-language formatted equations checked.'
    if record['pdfPage'] == 15:
        record['printedPage'] = '10'
        record['comparison'] = 'Example 10.4 continued in same stable record: substitution, sin10 rounded 0.17, negative 0.167 N and magnitude answer. Assignment 10.4 without invented answer. Full 10.4.1 source period proof, cancellation, square roots and equation 10.8; source mass/amplitude independence paragraph. Original mass spring wording retained with separate clarification. Three language KaTeX rendering checked.'
        record['sourceDefects'] = [{'location':'10.4.1 parenthetical definition','printed':'the time it takes for the mass spring system to complete one cycle','handling':'Retained exactly and translated; labeled clarification says current section concerns a simple pendulum.'},{'location':'Paragraph after equation 10.8','printed':'depends directly on length and inversely on gravitational acceleration','handling':'Original retained. Clarification states square-root proportionalities and small-angle assumption.'}]
    if record['pdfPage'] == 16:
        record['printedPage'] = '11'
        record['comparison'] = 'Original frequency paragraph and equation 10.9, LAB WORK, Example 10.5 full question/GIVEN/REQUIRED/squaring/isolation/substitution/3.73 m/s² = 3.73 N/kg [down] answer, Gravitational Field TIP, Assignment 10.5 with printed Everest altitude 8954.0 m and no invented solution. Paired translations and all worked formulas rendered through real KaTeX in three languages.'
    if record['pdfPage'] == 17:
        record['printedPage'] = '12'
        record['comparison'] = 'Pendulum LAB WORK on mass/amplitude independence; 10.5 original damping definition, ideal-systems paragraph and complete resistance/energy paragraph. Figure 10.7 native two-panel SVG with constant-length pendulum positions, x01/x02/x03 amplitudes, displacement/time axes, three successively decreasing positive peaks and negative troughs; reusable geometry, translated axis labels. Local SVG preview caught and fixed time-axis arrowhead and label overlap.'
    if record['pdfPage'] == 18:
        record['printedPage'] = '13'
        record['comparison'] = 'SHOCK ABSORBERS note: three original paragraphs, tyre/strut/spring diagram, oil-reservoir/piston/holes/spring cutaway and three labelled damping curves with full caption. Native SVG stores reusable geometry and curve samples; original and Urdu/Pashto labels/captions paired. 10.6 original wave definition replaces active legacy paragraph. Pendulum/damping/wave definitions synchronized to source bank. Native diagrams inspected locally; no raster content.'
    if record['pdfPage'] == 19:
        record['printedPage'] = '14'
        record['comparison'] = 'Two common wave features preserved as ordered list. WATER WAVES AS MEANS OF ENERGY TRANSFER activity: all three original paragraphs, tub/pencil/ripples/cork diagram and five successive water/cork panels with rightward energy arrow and fixed cork horizontal position. Two complete source paragraphs after activity preserved, including ball versus rope and Figure 10.8(a) reference. Paired English/Urdu/Pashto, reusable SVG geometry, source figures inspected locally.'
    if record['pdfPage'] == 20:
        record['printedPage'] = '15'
        record['comparison'] = 'Figure 10.8 original caption retained, with you/friend/energy rope pulse panel and wall/marked point/vertical oscillation wave-train panel. Full wave/rope paragraph and stone/pond paragraph; original 10.6.1, mechanical/electromagnetic definitions and material-medium conditions. Figure 10.9 native projected perpendicular electric/magnetic fields with travel arrow and translated labels; source definitions synchronized. Local SVG checks and three-language reader validation passed.'
    if record['pdfPage'] == 21:
        record['printedPage'] = '16'
        record['comparison'] = 'Electromagnetic field continuation and examples, transverse/longitudinal classification and full definitions, Slinky explanation, crest/trough definitions, AM/FM TIP including 3.00×10⁸ m/s. Figure 10.10 native slinky coils along transverse curve with equilibrium, crest, trough, wavelength λ, upper/lower x0 amplitude arrows, wave/vibration directions and hand. Structured source paragraphs, definitions and three-language coded reader verified.'
    if record['pdfPage'] == 22:
        record['printedPage'] = '17'
        record['comparison'] = 'Figure 10.11 native longitudinal slinky with compression/rarefaction regions, rightward wave and vibration directions, λ and x0 arrows. Full compression/rarefaction explanation; 10.6.2 characteristic wave parameters; exact wavelength and amplitude definitions. Figure 10.12 native sinusoid with λ crest/trough distances, x0 arrows, axes and printed t label retained. Editorial clarification explicitly identifies the source axis inconsistency. Definitions synchronized and all three language renderings checked.'
    if record['pdfPage'] == 23:
        record['printedPage'] = '18'
        record['comparison'] = 'Wave Cycle definition; frequency f, N/t equation 10.10 and three-cycle frequency explanation; Time Period definition and T=1/f equation 10.11; Figure 10.13 coded cycle/P/T graph; earthquake Point to Ponder text with native P/S/surface-wave concept card; Wave Speed definition and v=distance/time=Δs/Δt equation. Paired translations and native figures validated.'
    if record['pdfPage'] == 24:
        record['printedPage'] = '19'
        record['comparison'] = 'Universal wave equation derivation: Δs=λ, Δt=T, equations 2, 3 and 10.12 v=fλ, explanatory paragraph. Full Example 10.6 wave speed with GIVEN/REQUIRED/solution, 2.6 Hz × 0.37 m, 0.962 m s⁻¹ answer and reasonableness sentence. Assignment 10.6 wavelength of sound retained without answer. 10.7 properties opener preserved.'
    if record['pdfPage'] == 25:
        record['printedPage'] = '20'
        record['comparison'] = 'Ripple-tank setup explanation, reflection/refraction/diffraction purpose, shallow tray/transparent base/illumination/shadow projection, reflector explanation, straight and spherical dipper sources and electric motor. Native combined SVG for Figure 10.14 and Figure 10.15(a/b), source labels paired and locally inspected. 10.7 properties text synchronized.'
    if record['pdfPage'] == 26:
        record['printedPage'] = '21'
        record['comparison'] = 'Wavefront definition for two/three-dimensional waves, ray perpendicular relationship, plane-wave explanation and A. Reflection definition. Native multi-panel SVG reconstructs circular fronts/rays, plane fronts/rays, and incident/reflected fronts at a barrier with translated labels. Reflection definition synchronized and local reader validation passed.'
    if record['pdfPage'] == 27:
        record['printedPage'] = '22'
        record['comparison'] = 'Reflection continuation for straight/oblique barriers and ripple tank. B. Refraction definition, shallow/deep water wavelength/speed changes, straight and angled boundary behavior; C. Diffraction definition and two-obstacle ripple-tank method. Native Figure 10.19 shallow/deep boundary with wavefront spacing and ray direction, translated labels; definitions synchronized.'
    if record['pdfPage'] == 28:
        record['printedPage'] = '23'
        record['comparison'] = 'Diffraction continuation: small-opening waves spread circularly when opening ≤ wavelength; wavelength/speed unchanged; large obstacle separation leaves center unaffected. Native Figure 10.20 small/large openings with wavefronts and rays. Full KEY POINTS list preserved as structured records, including all ten source definitions. GROUP A “EARTHQUAKE” research/presentation task preserved without invented answer.'
    if record['pdfPage'] == 29:
        record['printedPage'] = '24'
        record['comparison'] = 'GROUP B two spring-mass systems, GROUP C angle in simple pendulum, GROUP D tsunami, GROUP E defining terms prompts preserved with aligned translations. Exercise questions 1–3 transcribed with all options and no invented answer; source handwriting check marks excluded as scan annotation.'
    if record['pdfPage'] == 30:
        record['printedPage'] = '25'
        record['comparison'] = 'Exercise questions 4–8 transcribed with all options, followed by the complete conceptual-question heading and questions 1–9 on oscillatory motion, pendulum scaling, wave speed and diffraction. Aligned English/Urdu/Pashto records preserved without invented answers; scan watermark excluded.'
    if record['pdfPage'] == 31:
        record['printedPage'] = '26'
        record['comparison'] = 'Complete comprehensive-question prompts 1–7 and numerical-question prompts 1–7 transcribed with units, givens and all source wording. Prompts are paired in English/Urdu/Pashto and kept separate from the existing numerical answer bank; no solutions were invented.'
    if record['pdfPage'] == 32:
        record['printedPage'] = '27'
        record['comparison'] = 'Unit 11 Sound opener: bat detection prompt, unit title and all ten student learning outcomes transcribed and paired across English, Urdu and Pashto; scan watermark and decorative photograph excluded.'
    if record['pdfPage'] == 33:
        record['printedPage'] = '28'
        record['comparison'] = 'Sound unit contents, introductory sound paragraphs, 11.1 Sound Waves definition and longitudinal-medium/vacuum explanation transcribed with source headings and aligned translations.'
    if record['pdfPage'] == 34:
        record['printedPage'] = '29'
        record['comparison'] = 'Figure 11.1 tuning fork and Figure 11.2 vibration examples reconstructed as native SVG; production and transmission paragraphs retained with translated labels and captions.'
    if record['pdfPage'] == 35:
        record['printedPage'] = '30'
        record['comparison'] = 'Bell-in-jar activity, sound-propagation pressure graph and 11.1.3 detection text transcribed; bell, graph and labels reconstructed as coded SVG without scan images.'
    if record['pdfPage'] == 36:
        record['printedPage'] = '31'
        record['comparison'] = 'Physics of hearing text, ear anatomy, 11.2 Characteristics of Sound, pitch explanation and bicycle-wheel activity transcribed with native ear and bicycle SVGs.'
    if record['pdfPage'] == 37:
        record['printedPage'] = '32'
        record['comparison'] = 'Loudness factors, drum example, ruler activity and 11.2.3 quality/timbre paragraphs transcribed with a coded ruler illustration and aligned translations.'
    if record['pdfPage'] == 38:
        record['printedPage'] = '33'
        record['comparison'] = '11.3 Sound Intensity definition, equation 11.1, objective intensity versus subjective loudness, intensity-level introduction and Table 11.1 reconstructed with a native intensity SVG and semantic table.'
    if record['pdfPage'] == 39:
        record['printedPage'] = '34'
        record['comparison'] = 'Intensity-level logarithmic derivation and Point to Ponder note transcribed, including printed equation numbering and the 0 dB clarification.'
    if record['pdfPage'] == 40:
        record['printedPage'] = '35'
        record['comparison'] = 'Table 11.2 source/intensity-level values, decibel equation 11.2, bel-to-decibel reminder and closing paragraph transcribed as structured source content.'
    if record['pdfPage'] == 9:
        record['sourceDefects'] = [{'location':'Equation 10.3','printed':'a ∝ x','handling':'Original retained; separately labeled clarification explains a ∝ −x for signed displacement.'}]
        record['comparison'] = 'Original six main blocks, equations 10.2 and 10.3, ball/bowl Figure 10.2 labels, TIP text and ECG trace. Original printed sign retained. All prose paired in English/Urdu/Pashto; native SVG visuals checked through local renders.'
book['pageReferences'] = [{'pdfPage':r['pdfPage'],'printedPage':r['printedPage']} for r in records]
if last >= 10:
    book['sourceOrderingIssues'] = [{'pdfPages':[10,11],'printedPages':['6','5'],'localJpgs':['010_Page_005.jpg (printed 6)','011_Page_006.jpg (printed 5)'],'handling':'Audit consecutive PDF pages. Display printed page 5 proof before printed page 6 example/derivation. Confirmed visually in both PDF and alternate JPG sources.'}]
book.update(status='in-progress',correctedPages=list(range(1,last+1)),lastFullyVerifiedPage=last,nextPage=last+1,currentChapter='10 — Simple Harmonic Motion and Waves' if last>=6 else 'front matter')
completed_book = last >= book.get('pdfPages', 0)
next_book = None
if completed_book:
    book.update(status='completed', nextPage=None, currentChapter='completed through source page '+str(last))
    for candidate in data['subjects'][0]['books']:
        if candidate is not book and candidate.get('status') == 'not-reviewed':
            next_book = candidate
            break
    if next_book:
        next_book.update(status='in-progress', lastFullyVerifiedPage=0, nextPage=1, currentChapter='unreviewed')
(OUT/'inventory.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(OUT/'physics-pages.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
checkpoint={'assignment':'All Class 10 non-Mathematics textbooks; assignment.txt contains full user instructions','complete':False,'currentSubject':'Physics','sourcePdf':book['path'],'lastFullyVerifiedPdfPage':last,'nextPdfPage':last+1,'nextAction':f'Render and visually inspect PDF page {last+1} of 10thphysics1.pdf. Compare actual active DATA.phys10Chapters and science lesson reader; complete page and save checkpoint before advancing.','remaining':'All later Physics pages and every later subject. PDF split/edition relationships still require visual comparison; no other source pages verified.','rulesRead':['SpaceBook Web/CONTRIBUTING.md','pdf skill'],'rulesSearch':'No applicable AGENTS.md found in workspace source/app trees or D: parent. User overrides branch/push/browser workflow.','sharedFiles':'Use atomic tmp/class-content-shared.lock; re-read under lock; release in finally. No additional agents, browsers or Mathematics inspection.','validation':'node --check app.js and physics_10_source_data.js; validate_physics.cjs non-browser VM checks','progressCounts':{'correctedPages':last,'verifiedUnchangedPages':0,'excludedWholePages':0,'unresolvedItems':0,'unreviewedPdfPages':data['totalPdfPages']-last}}
if completed_book and next_book:
    checkpoint.update(sourcePdf=next_book['path'],lastFullyVerifiedPdfPage=0,nextPdfPage=1,nextAction=f"Render and visually inspect PDF page 1 of {Path(next_book['path']).name}. Compare the active Class 10 Physics reader; complete the page and save checkpoint before advancing.",completedBooks=[book['path']],currentBook=next_book['path'])
checkpoint['sourceOrderingIssues']=book.get('sourceOrderingIssues',[])
checkpoint['sourceDefects']=[item for record in records for item in record.get('sourceDefects',[])]
checkpoint['validation']='node --check app.js and physics_10_source_data.js; validate_physics.cjs and validate_actual_physics.cjs direct non-browser VM checks, including real existing KaTeX; local SVG previews inspected. All checks passed.'
checkpoint['implementation']='js/physics_10_source_data.js loaded after data_phys.js. Active science lesson uses dedicated Class 10 source helpers; worked examples also exposed in numerical and formula/definition views; reviewed prose searchable in English/Urdu/Pashto. Other Physics chapters and existing unreviewed numerical bank preserved.'
(OUT/'checkpoint.json').write_text(json.dumps(checkpoint,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Saved through PDF page {last}; next page {last+1}. Assignment incomplete.')
