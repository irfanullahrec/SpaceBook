"""Add a scan-led opening section for Class 12 Chemistry Unit 22."""
import json
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'Books/12th/12th Chemistry/JPG'
section={
 'id':'22.source.309-312','title':'Unit 22 source reading — Industrial Chemistry (printed pp.309–312)',
 'theory':'''Printed p.309 lists the Unit 22 learning outcomes: economic importance of chemical industries; Pakistani raw materials; addition and condensation polymerization; petrochemical feedstocks, fractions, building blocks and processes; major petrochemicals; dyes; PVC and nylon; cosmetics; and synthetic adhesives.

Printed pp.310–311 define industrial chemistry as processing raw materials into useful products. Chemical-process industries use chemical reactions, extraction/separation/purification, or formulated mixtures; products include plastics, resins, dyes, medicines, paints, soaps, detergents, petrochemicals, perfumes, inorganics and synthetic organics. The text distinguishes organic chemicals (carbon-based) from inorganic materials and groups outputs as base chemicals, intermediates and finished products. It lists sectors including basic inorganic and organic chemicals, fertilizers and pesticides, polymers and fibres, pharmaceuticals, paints, soaps and detergents, and miscellaneous products.

The source identifies oil, natural gas, metals, minerals, coal and salt as industrial raw materials. Petrochemical feedstocks include methane, ethane, propane and butane from natural-gas processing, and benzene, toluene and xylene from petroleum refining; methane and these aromatic compounds can feed petrochemical production. The Pakistan economy section describes chemical industries’ contribution to farming, textiles, food, medicine, trade and everyday products.

Printed pp.312 introduces safety in process industries: choose suitable construction materials to prevent corrosion; control impurities and reactions and analyze processes to maintain yield and purity; use instrumentation and automatic control; package and transport products safely; protect workers and plants; fund research and development; prevent toxic air and water discharges; and label chemicals for identification and safe handling.''',
 'theoryUrdu':'صفحہ 309 میں صنعتی کیمیا کے تعلیمی مقاصد دیے گئے ہیں: معیشت میں اہمیت، پاکستان کے خام مواد، اضافی و تکاثفی پولیمرائزیشن، پیٹروکیمیکل فیڈ اسٹاک اور عمل، رنگ، PVC و نائلون، کاسمیٹکس اور مصنوعی چپکنے والے مادے۔\n\nصفحہ 310–311 صنعتی کیمیا کو خام مواد سے مفید مصنوعات بنانے کا عمل بتاتے ہیں۔ صنعت میں کیمیائی تعامل، استخراج، علیحدگی، تطہیر اور تیار کردہ آمیزے شامل ہیں۔ مصنوعات میں پلاسٹک، رال، رنگ، ادویات، صابن، ڈیٹرجنٹ، پیٹروکیمیکلز اور دیگر مادے شامل ہیں۔ متن بنیادی کیمیکلز، درمیانی مصنوعات اور تیار شدہ مصنوعات میں فرق کرتا ہے۔ خام مواد میں تیل، قدرتی گیس، دھاتیں، معدنیات، کوئلہ اور نمک شامل ہیں۔ قدرتی گیس سے میتھین، ایتھین، پروپین اور بیوٹین، جبکہ تیل کی صفائی سے بینزین، ٹولوین اور زائلین حاصل کیے جاتے ہیں۔\n\nصفحہ 312 عمل کی صنعتوں میں حفاظتی تدابیر بتاتا ہے: زنگ سے بچانے والے تعمیراتی مواد کا انتخاب، خام مواد کی صفائی، تعاملات کا کنٹرول اور تجزیہ، خودکار آلات، محفوظ پیکنگ و ترسیل، کارکنوں کی حفاظت، تحقیق و ترقی، زہریلے اخراج کی روک تھام اور کیمیکلز پر واضح لیبل۔',
 'theoryPashto':'په 309 مخ کې د صنعتي کیمیا د زده‌کړې موخې دي: په اقتصاد کې اهمیت، د پاکستان خام مواد، اضافي او تراکمي پولیمیرایزېشن، د پېټروکیمیاوي موادو سرچینې او بهیرونه، رنګونه، PVC او نایلون، کاسمیټکس او مصنوعي سریښونه.\n\nپه 310–311 مخونو کې صنعتي کیمیا له خامو موادو څخه د ګټورو محصولاتو جوړولو بهیر ګڼل شوی. په صنعتي بهیرونو کې کیمیاوي تعاملونه، استخراج، بېلول، پاکول او ځانګړي مخلوطونه شامل دي. محصولات پلاستیک، رېزین، رنګونه، درمل، صابون، ډیټرجنټونه او پېټروکیمیاوي توکي رانغاړي. متن بنسټیز کیمیاوي مواد، منځني مواد او بشپړ شوي محصولات بېلوي. خام مواد تېل، طبیعي ګاز، فلزات، منرالونه، سکاره او مالګه دي. له طبیعي ګازه مېتان، ایتان، پروپان او بیوتان، او د تېلو له تصفیې بنزین، تولیون او زایلین ترلاسه کېږي.\n\nپه 312 مخ کې د بهیر د صنعتونو خوندیتوب بیان شوی: د زنګ پر وړاندې مناسب ساختماني مواد، د خامو موادو او تعاملاتو کنټرول او شننه، اتومات وسایل، خوندي بسته‌بندي او لېږد، د کارکوونکو ساتنه، څېړنه او پراختیا، د زهري ککړتیا مخنیوی، او د کیمیاوي موادو روښانه نښه کول.',
 'sourceReferences':[{'printedPage':309,'jpg':'155_page_2.jpg','status':'source transcribed'},{'printedPage':310,'jpg':'156_page_1.jpg','status':'source transcribed'},{'printedPage':311,'jpg':'156_page_2.jpg','status':'source transcribed'},{'printedPage':312,'jpg':'157_page_1.jpg','status':'source transcribed'}],
 'translationStatus':'Urdu/Pashto lesson summaries supplied; manual review pending'
}
asset=ROOT/'assets/chem12/unit22-industrial-chemistry-cover.jpg'
asset.parent.mkdir(parents=True,exist_ok=True)
if not asset.exists():
 Image.open(SOURCE/'155_page_2.jpg').crop((0,0,618,810)).save(asset)
section['diagramSvg']='<figure><img src="assets/chem12/unit22-industrial-chemistry-cover.jpg" alt="Class 12 Chemistry Unit 22, Industrial Chemistry" style="max-width:100%;height:auto"><figcaption>Unit 22: Industrial Chemistry (source page 309)</figcaption></figure>'
target=ROOT/'js/chem_12_data.js'
with target.open('a',encoding='utf-8',newline='\n') as f:
 f.write('\n// Unit 22 scan-led source addition: printed pp.309–312.\n')
 f.write('CHEM_12_DATA[9].sections.push('+json.dumps(section,ensure_ascii=False)+' );\n')
print('Added Unit 22 source reading through printed page 312.')
