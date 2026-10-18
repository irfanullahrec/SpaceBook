"""Cache reviewed opening-unit vocabulary and connect it to existing word hover."""
from class12_chemistry_opening import ROOT, OUT
import json, os, time

entries=[
 ('chemistry','کیمیا','کیمیا'),('element','عنصر','عنصر'),('elements','عناصر','عناصر'),
 ('periodic','دوری','دوراني'),('period','دور','دوره'),('periods','ادوار','دورې'),
 ('group','گروپ','ګروپ'),('groups','گروپ','ګروپونه'),('demarcation','حد بندی','د برخو بېلول'),
 ('atomic','ایٹمی','اټومي'),('atom','ایٹم','اټوم'),('atoms','ایٹم','اټومونه'),
 ('radius','رداس','شعاع'),('radii','رداس','شعاعوې'),('ionic','آئنک','ایوني'),
 ('ion','آئن','ایون'),('ions','آئن','ایونونه'),('ionization','آئنائزیشن، آئن بننا','ایون کېدل'),
 ('energy','توانائی','انرژي'),('electronegativity','برقی منفیت','برېښنا منفي توب'),
 ('electrical','برقی','برېښنايي'),('conductivity','موصلیت','لېږدونه'),
 ('conductor','موصل','لېږدوونکی'),('conductors','موصل','لېږدوونکي'),
 ('semiconductor','نیم موصل','نیمه هادي'),('melting','پگھلنا','وېلې کېدل'),('boiling','ابلنا','اېشېدل'),
 ('electron','الیکٹران','الکترون'),('electrons','الیکٹران','الکترونونه'),
 ('electronic','الیکٹرانی','الکتروني'),('configuration','ترتیب','ترتیب'),('configurations','ترتیبیں','ترتیبونه'),
 ('nucleus','مرکزہ','هسته'),('nuclei','مرکزے','هستې'),('nuclear','مرکزی','هستوي'),
 ('shell','خول','پوښ'),('shells','خول','پوښونه'),('subshell','ذیلی خول','فرعي پوښ'),
 ('orbital','آربیٹل','اوربیټال'),('orbitals','آربیٹل','اوربیټالونه'),
 ('covalent','اشتراکی','کووالنټ'),('bond','بند','تړون'),('bonds','بند','تړونونه'),
 ('metal','دھات','فلز'),('metals','دھاتیں','فلزونه'),('metallic','دھاتی','فلزي'),
 ('metalloid','نیم دھات','نیمه فلز'),('metalloids','نیم دھاتیں','نیمه فلزونه'),
 ('non-metals','غیر دھاتیں','نافلزونه'),('shielding','حائل ہونا','حایل کېدل'),
 ('screening','کشش میں حائلی کمی','د کشش د پردې اغېز'),('valence','ظرفیت','ظرفیت'),
 ('attraction','کشش','کشش'),('repelled','دور دھکیلے گئے','دفع شوي'),
 ('sodium','سوڈیم','سوډیم'),('magnesium','میگنیشیم','مګنیزیم'),('aluminium','ایلومینیم','المونیم'),
 ('aluminum','ایلومینیم','المونیم'),('silicon','سلیکان','سیلیکان'),('phosphorus','فاسفورس','فاسفورس'),
 ('phosphorous','فاسفورس','فاسفورس'),('sulphur','سلفر','سلفر'),('chlorine','کلورین','کلورین'),
 ('argon','آرگن','ارګون'),('fluorine','فلورین','فلورین'),('caesium','سیزیم','سیزیم'),
 ('hydrogen','ہائیڈروجن','هایدروجن'),('oxygen','آکسیجن','اکسیجن'),('neon','نیون','نیون'),
 ('na','سوڈیم کی علامت','د سوډیم سمبول'),('mg','میگنیشیم کی علامت','د مګنیزیم سمبول'),
 ('al','ایلومینیم کی علامت','د المونیم سمبول'),('si','سلیکان کی علامت','د سیلیکان سمبول'),
 ('cl','کلورین کی علامت','د کلورین سمبول'),('ar','آرگن کی علامت','د ارګون سمبول'),
 ('oxide','آکسائیڈ','اکسایډ'),('oxides','آکسائیڈز','اکسایډونه'),('peroxide','پرآکسائیڈ','پراکسایډ'),
 ('superoxide','سپرآکسائیڈ','سوپراکسایډ'),('chloride','کلورائیڈ','کلورایډ'),('chlorides','کلورائیڈز','کلورایډونه'),
 ('hydroxide','ہائیڈرو آکسائیڈ','هایدروکسایډ'),('hydroxides','ہائیڈرو آکسائیڈز','هایدروکسایډونه'),
 ('acid','تیزاب','تېزاب'),('acids','تیزاب','تېزابونه'),('acidic','تیزابی','تېزابي'),
 ('base','اساس','اساس'),('bases','اساس','اساسونه'),('basic','اساسی','قلوي'),('alkaline','الکلائن','قلوي'),
 ('amphoteric','دو خصوصیتی، تیزابی و اساسی','امفوتېریک، تېزابي او قلوي'),
 ('oxidation','تکسید','اکسیدېشن'),('reducing','اختزالی','ارجاع کوونکی'),('halogens','ہیلوجن','هالوجنونه'),
 ('nitrates','نائٹریٹس','نایټرېټونه'),('carbonates','کاربونیٹس','کاربونېټونه'),
 ('sulphates','سلفیٹس','سلفېټونه'),('sulphite','سلفائٹ','سلفایټ'),('sulphate','سلفیٹ','سلفېټ'),
 ('phosphate','فاسفیٹ','فاسفېټ'),('silicate','سلیکیٹ','سیلیکېټ'),
 ('molecule','سالمہ','مالیکول'),('molecules','سالمے','مالیکولونه'),('molecular','سالماتی','مالیکولي'),
 ('lattice','جالی','جالۍ'),('lattices','جالیاں','جالۍ'),('crystalline','قلمی','بلوري'),
 ('polymeric','کثیر سالماتی','پولیمري'),('dispersion','انتشار','خپرېدنه'),('polarity','قطبیت','قطبیت'),
 ('steam','بھاپ','بخار'),('aqueous','آبی','اوبلن'),('molten','پگھلا ہوا','وېلې شوی'),
 ('exothermic','حرارت خارج کرنے والا','تودوخه خوشې کوونکی'),('reversible','قابلِ واپسی','بېرته ګرځېدونکی'),
 ('concentrated','مرتکز','غلیظ'),('dilute','رقیق','رقیق'),('inert','غیر فعال','غیر فعال'),
 ('iodine','آیوڈین','ایوډین'),('thyroid','تھائرائیڈ','تایرایډ'),('goitre','گلہڑ','جاغور'),
 ('metabolism','تحول','میتابولیزم'),('corundum','کورنڈم','کورنډم'),('diamond','ہیرا','الماس'),
 ('electrodes','الیکٹروڈز','الکټروډونه'),('solubility','حل پذیری','د حل کېدو وړتیا'),
 ('thermal','حرارتی','حرارتي'),('stability','استحکام','ثبات'),('beryllium','بیریلیم','بېریلیم'),
]
entries.extend([
 ('strontium','اسٹرونشیم','سټرونشیم'),('barium','بیریم','بېریم'),('germanium','جرمینیم','جرمانیم'),
 ('tin','ٹن','ټین'),('lead','سیسہ','سرب'),('amphoteric','دو خصوصیتی','امفوتېریک'),
 ('tetrahydroxoberyllate','ٹیٹراہائیڈروکسوبیریلیٹ','ټېټراهایدروکسوبېریلېټ'),
 ('hybridization','ہائبرڈائزیشن','هایبرډایزېشن'),('hybrid','ہائبرڈ','هایبرډ'),
 ('hybridized','ہائبرڈائزڈ','هایبرډ شوی'),('unhybridized','غیر ہائبرڈ','ناهایبرډ'),
 ('promotion','توانائی کی بلند سطح میں ترقی','د انرژۍ لوړې کچې ته لوړول'),
 ('unpaired','غیر جوڑا','بې جوړې'),('paired','جوڑا بنا ہوا','جوړه شوی'),('inert','غیر فعال','غیر فعال'),
 ('tetrachloride','ٹیٹراکلورائیڈ','ټېټراکلورایډ'),('tetrachlorides','ٹیٹراکلورائیڈز','ټېټراکلورایډونه'),
 ('tetrahedral','چہار سطحی','څلورمخیز'),('sigma','سگما','سیګما'),('pi','پائی','پای'),
 ('overlap','تداخل','تداخل'),('lone','تنہا','یوازینی'),('linear','خطی','خطي'),
 ('polarization','قطبی بنانا','قطبي کول'),('lattice','جالی','جالۍ'),('volatile','فرار پذیر','ژر بخار کېدونکی'),
])
entries.extend([
 ('transition','عبوری','انتقالي'),('transitions','انتقالات','انتقالونه'),
 ('lanthanides','لینتھنائیڈز','لانتانایډونه'),('actinides','ایکٹینائیڈز','اکتینایډونه'),
 ('scandium','اسکینڈیم','سکانډیم'),('yttrium','اٹریئم','اېټریوم'),('cadmium','کیڈمیم','کډمیم'),
 ('chromium','کرومیم','کرومیم'),('vanadium','وینیڈیم','وانادیم'),('manganese','مینگنیز','منګنیز'),
 ('copper','تانبا','مس'),('iron','لوہا','اوسپنه'),('cobalt','کوبالٹ','کوبالټ'),('nickel','نکل','نیکل'),
 ('palladium','پیلیڈیم','پالادیم'),('platinum','پلاٹینم','پلاټینم'),('mercury','پارہ','سیماب'),
 ('binding','بندشی','تړل'),('alloy','مخلوط دھات','الیاژ'),('alloys','مخلوط دھاتیں','الیاژونه'),
 ('amalgam','املگم','املګم'),('paramagnetic','پیرا مقناطیسی','پارامقناطیسي'),
 ('diamagnetic','ڈائی مقناطیسی','ډایامقناطیسي'),('ferromagnetic','فیرومقناطیسی','فېرومقناطیسي'),
 ('catalyst','عمل انگیز','کتلیست'),('catalysts','عمل انگیز','کتلیستونه'),('catalytic','عمل انگیزی','کتلیستي'),
 ('coordination','تناسق','کواردینېشن'),('ligand','لیگنڈ','لېګنډ'),('ligands','لیگنڈز','لېګنډونه'),
 ('complex','کمپلیکس','کمپلېکس'),('complexes','کمپلیکس','کمپلېکسونه'),
 ('ferrocyanide','فیروسائنائیڈ','فېروسیانایډ'),('nitroprusside','نائٹروپروسائیڈ','نایټروپروسایډ'),
 ('valency','ظرف','ظرفیت'),('valencies','ظرف','ظرفیتونه'),('aufbau','آفباؤ','اوفباو'),
 ('crystalline','قلمی','بلوري'),('lanthanum','لینتھنم','لانتانم'),('lutetium','لیوٹیشیئم','لوتېشیم'),
])
entries.extend([
 ('organic','نامیاتی','عضوي'),('inorganic','غیر نامیاتی','غیر عضوي'),
 ('hydrocarbon','ہائیڈروکاربن','هایدروکاربن'),('hydrocarbons','ہائیڈروکاربن','هایدروکاربنونه'),
 ('methane','میتھین','میتان'),('ethane','ایتھین (ethane)','ایتان'),('ethene','ایتھین (ethene)','ایتین'),
 ('propane','پروپین','پروپان'),('butane','بیوٹین','بیوټان'),('pentane','پینٹین','پینټان'),
 ('petroleum','پٹرولیم','پټرولیم'),('coal','کوئلہ','د ډبرو سکاره'),('peat','پیٹ','پیټ'),
 ('wood','لکڑی','لرګي'),('fossil','فوسل','فوسیلي'),('fuel','ایندھن','سون'),('fuels','ایندھن','سون توکي'),
 ('natural','قدرتی','طبیعي'),('synthetic','مصنوعی','مصنوعي'),('synthesis','تیاری','ترکیب'),
 ('partial','جزوی','جزوي'),('total','مکمل','بشپړ'),('biotechnology','حیاتی ٹیکنالوجی','بایوټکنالوژي'),
 ('polymer','پولیمر','پولیمر'),('polymers','پولیمرز','پولیمرونه'),('polymerization','پولیمرائزیشن','پولیمریزېشن'),
 ('polyethylene','پولی ایتھیلین','پولي ایتیلین'),('ethylene','ایتھیلین','ایتیلین'),
 ('catenation','خود پیوندی','ځان تړنه'),('isomer','آئسومر','ایزومر'),('isomers','آئسومرز','ایزومرونه'),
 ('isomerism','آئسومرزم','ایزومېریزم'),('homologous','ہم سلسلہ','همولوګ'),('functional','فعلی','فعالي'),
 ('distillation','کشید','تقطیر'),('destructive','تخریبی','تخریبي'),('fractional','جزوی','جزوي'),
 ('coke','کوک','کوک'),('tar','تار','قیر'),('ammoniacal','امونیائی','امونیایي'),
 ('benzene','بینزین','بنزین'),('toluene','ٹولیوئن','تولوین'),('xylene','زائلین','زایلین'),
 ('phenol','فینول','فینول'),('cresol','کریسول','کریسول'),('naphthalene','نیفتھلین','نفتالین'),
 ('anthracene','اینتھراسین','انتراسین'),('alkane','الکین','الکان'),('alkanes','الکینز','الکانونه'),
 ('aliphatic','ایلیفیٹک','الیفاتیک'),('aromatic','ارومیٹک','اروماتیک'),('saturated','سیر شدہ','مشبوع'),
 ('cyanate','سائنیٹ','سیانېټ'),('urea','یوریا','یوریا'),('carbamide','کاربامائیڈ','کاربامایډ'),
 ('fermentation','تخمیر','تخمر'),('pigments','رنگ ساز مواد','رنګیز مواد'),
 ('solvent','محلل','محلل'),('solute','حل شونده','حل کېدونکی'),('non-polar','غیر قطبی','غیر قطبي'),
 ('alcohol','الکوحل','الکول'),('alcohols','الکوحل','الکولونه'),('ketone','کیٹون','کیټون'),
 ('aldehydes','ایلڈیہائیڈز','الدیهایډونه'),('carboxylic','کاربوکسلک','کاربوکسیلیک'),
 ('oxidizing','تکسیدی','اکسیدوونکی'),('reducing','تخفیفی','احیاکوونکی'),
 ('titration','ٹائٹریشن','تیتریشن'),('titrations','ٹائٹریشن','تیتریشنونه'),
 ('adsorbed','جذب سطحی','پر سطح جذب شوی'),('desorbed','سطح سے خارج','له سطحې خوشې شوی'),
 ('precipitate','رسوب','رسوب'),('precipitation','رسوب بننا','رسوب جوړېدل'),
 ('chromate','کرومیٹ','کرومېټ'),('dichromate','ڈائی کرومیٹ','ډای کرومېټ'),
 ('permanganate','پرمینگنیٹ','پرمنګنېټ'),('manganate','مینگنیٹ','منګنېټ'),
 ('ferrous','فیرس','فېرس'),('ferric','فیرک','فېرېک'),('cuprous','کیوپرس','کیوپرس'),('cupric','کیوپرک','کیوپرېک'),
])
vocabulary={word:{'u':urdu,'p':pashto} for word,urdu,pashto in entries}

def main():
    marker='// BEGIN CLASS12 CHEMISTRY REVIEWED VOCABULARY';end='// END CLASS12 CHEMISTRY REVIEWED VOCABULARY'
    block=marker+'\n{ const vocabulary = '+json.dumps(vocabulary,ensure_ascii=False,indent=2)+";\nconst chapter=CHEM_12_DATA.find(item=>item.number===13); chapter.sourceWordMeanings={...(chapter.sourceWordMeanings||{}),...vocabulary};\n}\n"+end+'\n'
    lock=ROOT/'tmp/class-content-shared.lock';fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
    try:
        os.write(fd,f'class12-chemistry pid={os.getpid()}\n'.encode());os.close(fd);fd=None
        for name in ['js/chem_12_data.js','js/app.js']:
            path=ROOT/name;text=path.read_text(encoding='utf-8')
            if name.endswith('chem_12_data.js'):
                if marker in text:
                    start=text.index(marker);stop=text.index(end,start)+len(end);text=text[:start]+block+text[stop:]
                else:text=text.rstrip()+'\n\n'+block
            else:
                old="state.selectedClass === 'cls9' && state.activeSubject === 'chem'\n    ? DATA.chemChapters?.[state.selectedSubjChapter || 0]?.sourceWordMeanings?.[cleanWord] : null;"
                new="state.activeSubject === 'chem'\n    ? (state.selectedClass === 'cls9' ? DATA.chemChapters?.[state.selectedSubjChapter || 0]?.sourceWordMeanings?.[cleanWord]\n      : state.selectedClass === 'cls12' && typeof CHEM_12_DATA !== 'undefined' ? CHEM_12_DATA[state.selectedSubjChapter || 0]?.sourceWordMeanings?.[cleanWord] : null) : null;"
                if old in text:
                    assert text.count(old)==1;text=text.replace(old,new)
                else:assert new in text
            temp=path.with_name(path.name+'.chem12.tmp');temp.write_text(text,encoding='utf-8')
            for attempt in range(6):
                try:os.replace(temp,path);break
                except PermissionError:
                    if attempt==5:raise
                    time.sleep(.15)
    finally:
        if fd is not None:os.close(fd)
        lock.unlink()
    (OUT/'chemistry-vocabulary.json').write_text(json.dumps(vocabulary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'{len(vocabulary)} cached Chemistry word meanings connected to Urdu/Pashto hover.')
if __name__=='__main__':main()
