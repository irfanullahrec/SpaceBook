"""PDF20, printed32–33: inert pair continuation and tetrachlorides."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_orbital_diagrams import block
paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def head(en,ur,ps):add(en,ur,ps,'heading')
def visual(identity,kind):
    blocks.append(block(identity,kind));layout.append({'type':'visual','blockId':identity})
add('i. Promotion of one electron of the s-orbital into higher energy p-orbital. Energy must be provided for this process.',
    'i. s آربیٹل کے ایک الیکٹرون کی زیادہ توانائی والے p آربیٹل میں ترقی۔ اس عمل کے لیے توانائی فراہم کرنا ضروری ہے۔',
    'i. د s اوربیټل د یوه الکترون لوړول د لوړې انرژۍ p اوربیټل ته. دې بهیر ته انرژي برابرول اړین دي.')
add('ii. Formation of four covalent bonds by the four hybrid orbitals, energy is released in this process.',
    'ii. چار ہائبرڈ آربیٹلز سے چار اشتراکی بندوں کی تشکیل؛ اس عمل میں توانائی خارج ہوتی ہے۔',
    'ii. د څلورو هایبرډ اوربیټلونو له خوا د څلورو کووالنټ تړونونو جوړېدل؛ په دې بهیر کې انرژي خوشې کېږي.')
add('If energy release in the formation of four bonds is more than energy absorbed in promotion of s-electron then hybridization is feasible. This happens in case of C and Si and also for Ge in most cases. However, Sn and Pb form weak covalent bonds due to their larger atomic radius. So, the energy released in the formation of four covalent bonds may be less than the energy needed to promote s-electrons. So, hybridization will not occur and two s-electrons remain paired. They are called inert pair and effect is called inert pair effect, thus, Sn and Pb show oxidation state of +2 in addition to +4.',
    'اگر چار بند بنانے میں خارج ہونے والی توانائی s الیکٹرون کی ترقی میں جذب ہونے والی توانائی سے زیادہ ہو تو ہائبرڈائزیشن ممکن ہے۔ C اور Si اور اکثر Ge میں ایسا ہوتا ہے۔ تاہم بڑے ایٹمی رداس کی وجہ سے Sn اور Pb کمزور اشتراکی بند بناتے ہیں۔ اس لیے چار اشتراکی بند بنانے میں خارج ہونے والی توانائی، s الیکٹرونوں کی ترقی کے لیے درکار توانائی سے کم ہو سکتی ہے۔ چنانچہ ہائبرڈائزیشن نہیں ہوتی اور دو s الیکٹرون جوڑے میں رہتے ہیں۔ انہیں غیر فعال جوڑا اور اس اثر کو غیر فعال جوڑے کا اثر کہتے ہیں؛ یوں Sn اور Pb، +4 کے علاوہ +2 تکسیدی حالت بھی دکھاتے ہیں۔',
    'که د څلورو تړونونو په جوړولو کې خوشې شوې انرژي د s الکترون د لوړولو له جذب شوې انرژۍ څخه زیاته وي، نو هایبرډایزېشن ممکن دی. دا په C او Si او په ډېرو حالتونو کې په Ge کې پېښېږي. خو Sn او Pb د لویې اټومي شعاع له امله کمزوري کووالنټ تړونونه جوړوي. نو د څلورو کووالنټ تړونونو په جوړولو کې خوشې شوې انرژي ښايي د s الکترونونو د لوړولو له اړینې انرژۍ کمه وي. نو هایبرډایزېشن نه پېښېږي او دوه s الکترونونه جوړه پاتې کېږي. هغوی غیر فعاله جوړه او اغېز یې د غیر فعالې جوړې اغېز بلل کېږي؛ په دې توګه Sn او Pb د +4 ترڅنګ +2 د اکسیدېشن حالت ښيي.')
head('13.4.4.2 Inert Pair Effect and the Formation of Covalent Bonds','13.4.4.2 غیر فعال جوڑے کا اثر اور اشتراکی بندوں کی تشکیل','13.4.4.2 د غیر فعالې جوړې اغېز او د کووالنټ تړونونو جوړېدل')
add('Carbon normally forms four covalent bonds rather than two. The outer electronic structure of carbon is,',
    'کاربن عموماً دو کی بجائے چار اشتراکی بند بناتا ہے۔ کاربن کی بیرونی الیکٹرونی ساخت یہ ہے:',
    'کاربن په عادي ډول د دوو پر ځای څلور کووالنټ تړونونه جوړوي. د کاربن بهرنی الکتروني جوړښت دا دی:')
visual('chem12-carbon-ground-state','ground')
add('There are two unpaired electrons in 2px and 2py orbitals. In order to form bonds, however, carbon promotes one ‘s’ electron to the empty 2pz orbital.',
    '2px اور 2py آربیٹلز میں دو غیر جوڑا الیکٹرون ہیں۔ تاہم بند بنانے کے لیے کاربن ایک s الیکٹرون کو خالی 2pz آربیٹل میں ترقی دیتا ہے۔',
    'په 2px او 2py اوربیټلونو کې دوه بې جوړې الکترونونه شته. خو د تړونونو د جوړولو لپاره کاربن یو s الکترون خالي 2pz اوربیټل ته لوړوي.')
visual('chem12-carbon-excited-state','excited')
add('This produces 4 unpaired electrons which (after hybridization) can form four covalent bonds. To promote the ‘s’ electron to ‘p’ orbital requires energy. During the covalent bond formation each bond releases energy and this energy is enough for the promotion of ‘s’ electron to ‘p’ orbital.',
    'اس سے 4 غیر جوڑا الیکٹرون بنتے ہیں، جو ہائبرڈائزیشن کے بعد چار اشتراکی بند بنا سکتے ہیں۔ s الیکٹرون کو p آربیٹل میں ترقی دینے کے لیے توانائی درکار ہے۔ اشتراکی بند کی تشکیل میں ہر بند توانائی خارج کرتا ہے اور یہ توانائی s الیکٹرون کو p آربیٹل میں ترقی دینے کے لیے کافی ہے۔',
    'دا 4 بې جوړې الکترونونه پیدا کوي، چې له هایبرډایزېشن وروسته څلور کووالنټ تړونونه جوړولای شي. د s الکترون p اوربیټل ته لوړول انرژي غواړي. د کووالنټ تړون د جوړېدو پر مهال هر تړون انرژي خوشې کوي او دا انرژي د s الکترون p اوربیټل ته د لوړولو لپاره بس ده.')
add('The other members of Group – IVA, such as lead show reluctance to do the same; this is due the decrease in bond energies down the group. Bond energies decreases as atomic size increases and the bonding pair move away from the two nuclei and also because of screening effect. For example, the energy released by two extra Pb–Cl bonds may not be enough to cater the extra energy needed to promote a 6s electron into the empty 6p orbital.',
    'گروپ IVA کے دوسرے ارکان، مثلاً سیسہ، ایسا کرنے میں کم آمادگی دکھاتے ہیں؛ اس کی وجہ گروپ میں نیچے بندوں کی توانائی کا کم ہونا ہے۔ ایٹمی جسامت بڑھنے، بند بنانے والے جوڑے کے دونوں مرکزوں سے دور ہونے اور حجاب کے اثر سے بندوں کی توانائی کم ہوتی ہے۔ مثلاً دو اضافی Pb–Cl بندوں سے خارج توانائی، ایک 6s الیکٹرون کو خالی 6p آربیٹل میں ترقی دینے کے لیے درکار اضافی توانائی پوری کرنے کے لیے کافی نہیں ہو سکتی۔',
    'د IVA ګروپ نور غړي، لکه سرب، د همدې کار کولو ته لږه لېوالتیا ښيي؛ دا په ګروپ کې ښکته د تړونونو د انرژیو د کمېدو له امله دی. د اټومي اندازې په زیاتېدو، د تړون جوړوونکې جوړې له دواړو هستو څخه په لیرې کېدو او د پردې د اغېز له امله د تړونونو انرژي کمېږي. د بېلګې په توګه له دوو اضافي Pb–Cl تړونونو خوشې شوې انرژي ښايي د یوه 6s الکترون خالي 6p اوربیټل ته د لوړولو اړینه اضافي انرژي پوره نه کړي.')
paras[-1]['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':20,'printedPages':[32,33]}]
head('13.4.5 Chlorides of Carbon, Silicon and Lead','13.4.5 کاربن، سلیکان اور سیسے کے کلورائیڈز','13.4.5 د کاربن، سیلیکان او سرب کلورایډونه')
add('Carbon, silicon and lead give tetrachlorides, which are simple covalent molecules. They exist in liquid state at room temperature with the general formula of MCl₄. (where M = C, Si, Pb).',
    'کاربن، سلیکان اور سیسہ ٹیٹراکلورائیڈز بناتے ہیں، جو سادہ اشتراکی سالمے ہیں۔ یہ کمرے کے درجہ حرارت پر مائع حالت میں ہوتے ہیں اور ان کا عمومی فارمولا MCl₄ ہے (جہاں M = C، Si، Pb)۔',
    'کاربن، سیلیکان او سرب ټېټراکلورایډونه جوړوي، چې ساده کووالنټ مالیکولونه دي. هغوی د خونې په تودوخه کې په مایع حالت کې وي او عمومي فورمول یې MCl₄ دی (چې M = C، Si، Pb دی).')
head('13.4.5.1 Structures and Stability','13.4.5.1 ساختیں اور استحکام','13.4.5.1 جوړښتونه او ثبات')
head('i. Structure','i. ساخت','i. جوړښت')
add('The MCl₄ have a tetrahedral shape with a bond angle of 109.5°. A typical example is carbon tetrachloride.',
    'MCl₄ کی شکل چہار سطحی ہے، جس میں بند کا زاویہ 109.5° ہے۔ کاربن ٹیٹراکلورائیڈ ایک عام مثال ہے۔',
    'MCl₄ څلورمخیز شکل لري او د تړون زاویه یې 109.5° ده. کاربن ټېټراکلورایډ یې یوه عادي بېلګه ده.')
visual('chem12-figure-13-3','ccl4')
add('Figure 13.3 Structure of CCl₄.','شکل 13.3 CCl₄ کی ساخت۔','شکل 13.3 د CCl₄ جوړښت.')
head('ii. Stability','ii. استحکام','ii. ثبات')
add('When we move down the Group, compounds with a +2 oxidation state in Group – IVA element become more stable.',
    'گروپ میں نیچے جانے پر گروپ IVA کے عنصر کی +2 تکسیدی حالت والے مرکبات زیادہ مستحکم ہوتے ہیں۔',
    'په ګروپ کې ښکته تګ سره د IVA ګروپ د عنصر د +2 د اکسیدېشن حالت لرونکي مرکبات ډېر ثابت کېږي.')
add('This means that the +4 oxidation is less favourable while the +2 oxidation state is more favourable down the Group.',
    'اس کا مطلب ہے کہ گروپ میں نیچے +4 تکسید کم موافق، جبکہ +2 تکسیدی حالت زیادہ موافق ہے۔',
    'دا مانا لري چې په ګروپ کې ښکته +4 اکسیدېشن لږ مساعد دی، خو +2 د اکسیدېشن حالت ډېر مساعد دی.')
add('Thus, stability decreases from CCl₄ to PbCl₄. Lead tetrachloride (PbCl₄) at room temperature, tends to decompose to give lead dichloride (PbCl₂) and chlorine gas.',
    'یوں CCl₄ سے PbCl₄ تک استحکام کم ہوتا ہے۔ سیسہ ٹیٹراکلورائیڈ (PbCl₄) کمرے کے درجہ حرارت پر تحلیل ہو کر سیسہ ڈائی کلورائیڈ (PbCl₂) اور کلورین گیس بنانے کا رجحان رکھتا ہے۔',
    'نو له CCl₄ څخه PbCl₄ ته ثبات کمېږي. سرب ټېټراکلورایډ (PbCl₄) د خونې په تودوخه کې د تجزیې تمایل لري او سرب ډای کلورایډ (PbCl₂) او کلورین ګاز جوړوي.')
add('PbCl₄(s) → PbCl₂(s) + Cl₂(g)','PbCl₄(s) → PbCl₂(s) + Cl₂(g)','PbCl₄(s) → PbCl₂(s) + Cl₂(g)','equation')
head('13.4.5.2 Reactions with Water','13.4.5.2 پانی کے ساتھ تعاملات','13.4.5.2 له اوبو سره تعاملونه')
add('Carbon tetrachloride (CCl₄) does not react with water. This is due to bulky nature of chlorine atoms around small carbon atom. As a result, oxygen of water cannot penetrate to reach carbon atom.',
    'کاربن ٹیٹراکلورائیڈ (CCl₄) پانی سے تعامل نہیں کرتا۔ اس کی وجہ چھوٹے کاربن ایٹم کے گرد کلورین ایٹموں کی بھاری جسامت ہے۔ نتیجتاً پانی کی آکسیجن اندر داخل ہو کر کاربن ایٹم تک نہیں پہنچ سکتی۔',
    'کاربن ټېټراکلورایډ (CCl₄) له اوبو سره تعامل نه کوي. دا د کوچني کاربن اټوم شاوخوا د کلورین د اټومونو د لویې اندازې له امله دی. په پایله کې د اوبو اکسیجن دننه نه شي ننوتلای چې کاربن اټوم ته ورسېږي.')
add('SiCl₄ to PbCl₄ react violently with water to produce their respective oxides and fumes of HCl.',
    'SiCl₄ سے PbCl₄ تک پانی سے شدید تعامل کر کے اپنے متعلقہ آکسائیڈز اور HCl کے بخارات بناتے ہیں۔',
    'له SiCl₄ څخه تر PbCl₄ پورې له اوبو سره په شدت تعامل کوي او خپل اړوند اکسایډونه او د HCl لوګي جوړوي.')
record=section('13.16','Inert pair effect and tetrachlorides','غیر فعال جوڑے کا اثر اور ٹیٹراکلورائیڈز','د غیر فعالې جوړې اغېز او ټېټراکلورایډونه',paras,layout,blocks,'32–33')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':20,'printedPages':[32,33]}]
record['sourceContinuesOnPdfPage']=21
issues=[{'id':'chem12-p33-pbcl4-phase','printedPage':33,'description':'The prose describes tetrachlorides as liquids at room temperature but the printed PbCl4 decomposition equation labels its phase (s). Both retained.'}]
if __name__=='__main__':save(20,[record],carry=[{'from':'13.16','to':'13.17','startsAt':'SiO200+4HCL'}],issues=issues)
