"""PDF199 printed392–393: Glossary (Substituent group … Williamson Synthesis) and References."""
from class12_chemistry_opening import ROOT,pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_glossary import glossary_record
E=[
('Substituent group','A substituent is an atom or group of atoms which replaces one or more hydrogen or other atom or group of atoms on the parent molecule.','متبادل گروپ','متبادل وہ ایٹم یا ایٹموں کا گروہ ہے جو اصل سالمے پر ایک یا زیادہ ہائیڈروجن یا دوسرے ایٹم یا ایٹموں کے گروہ کی جگہ لیتا ہے۔','بدیل ګروپ','بدیل هغه اټوم یا د اټومونو ډله ده چې پر اصلي مالیکول د یوه یا ډېرو هایدروجن یا نورو اټومونو یا اټومي ډلو ځای نیسي.'),
('Substrate','It is a molecule or a compound that undergoes a chemical reaction, whether under the action of a catalyst, an enzyme or an inhibitor. It can also refer to a surface on which other chemical reactions are performed.','سبسٹریٹ','یہ وہ سالمہ یا مرکب ہے جو کیمیائی تعامل سے گزرتا ہے، خواہ عمل انگیز، خامرے یا روکنے والے کے عمل سے۔ اس سے وہ سطح بھی مراد ہو سکتی ہے جس پر دوسرے کیمیائی تعاملات کیے جاتے ہیں۔','سبسټرېټ','دا هغه مالیکول یا مرکب دی چې کیمیاوي تعامل کوي، که د کتلست، انزایم یا مخنیوونکي د عمل لاندې وي. دا هغې سطحې ته هم ویل کېدای شي چې پرې نور کیمیاوي تعاملونه ترسره کېږي.'),
('Sulphydryl or Marcapto','A mercapto group is a functional group containing a sulfur atom bonded to a hydrogen atom. General formula: –SH.','سلف ہائیڈرائل یا مرکیپٹو','مرکیپٹو گروپ وہ فعلی گروپ ہے جس میں سلفر ایٹم ہائیڈروجن ایٹم سے جڑا ہو۔ عمومی فارمولا: –SH۔','سلفهایدریل یا مرکپټو','مرکپټو ګروپ هغه فعال ګروپ دی چې پکې د سلفر اټوم له هایدروجني اټوم سره تړلی وي. عمومي فورمول: –SH.'),
('Synthetic Organic Compound','The compounds which can be synthesized in laboratory by chemical manipulations (chemical reactions) from living or non-living organisms.','مصنوعی نامیاتی مرکب','وہ مرکبات جو جاندار یا بے جان اجسام سے کیمیائی ترکیبوں (کیمیائی تعاملات) کے ذریعے تجربہ گاہ میں تالیف کیے جا سکیں۔','مصنوعي عضوي مرکب','هغه مرکبات چې له ژوندیو یا غیر ژوندیو موجوداتو څخه د کیمیاوي لاسوهنو (کیمیاوي تعاملونو) په واسطه په لابراتوار کې جوړېدای شي.'),
('Tautomerism','A type of isomerism wherein the isomers interchange into one another very easily to exist together in equilibrium.','ٹاٹومرزم','آئسومرزم کی وہ قسم جس میں آئسومرز ایک دوسرے میں بہت آسانی سے بدل کر توازن میں اکٹھے موجود رہتے ہیں۔','ټاټومېریزم','د ایزومېریزم هغه ډول چې پکې ایزومرونه په ډېره اسانۍ یو بل ته بدلېږي او په توازن کې یو ځای شتون لري.'),
('Electronegativity','Electronegativity is a measure of the tendency of an atom to attract a shared pair of electrons in a covalent bond.','برقی منفیت','برقی منفیت شریک گرفتی بند میں مشترک الیکٹرانی جوڑے کو اپنی طرف کھینچنے کے ایٹم کے رجحان کا پیمانہ ہے۔','الکترونېګاتیویټي','الکترونېګاتیویټي په کوولانټ تړون کې د شریکې الکتروني جوړې د راښکلو لپاره د اټوم د تمایل اندازه ده.'),
('Ultra violet visible spectroscopy','An instrumental scanning method that analyses the absorption of light within UV–Visible region.','بالائے بنفشی مرئی سپیکٹروسکوپی','آلاتی جائزے کا وہ طریقہ جو UV–مرئی خطے میں روشنی کے جذب کا تجزیہ کرتا ہے۔','ماورای بنفش لیدونکې سپکټروسکوپي','یوه وسیلوي سکن طریقه چې په UV–لیدونکې سیمه کې د رڼا جذب تحلیلوي.'),
('Unsaturated Hydrocarbon','Unsaturated hydrocarbons are hydrocarbons that have double or triple covalent bonds between adjacent carbon atoms.','غیر سیر شدہ ہائیڈروکاربن','غیر سیر شدہ ہائیڈروکاربنز وہ ہائیڈروکاربنز ہیں جن کے ملحقہ کاربن ایٹموں کے درمیان دوہرے یا تہرے شریک گرفتی بند ہوں۔','نامشبوع هایدروکاربن','نامشبوع هایدروکاربنونه هغه هایدروکاربنونه دي چې د ګاونډیو کاربني اټومونو ترمنځ دوه ګوني یا درې ګوني کوولانټ تړونونه لري.'),
('Vital force theory','A theory that an organic molecule cannot be produced from inorganic molecules, but can only be produced from a living organism or some part of a living organism.','حیاتی قوت کا نظریہ','وہ نظریہ کہ نامیاتی سالمہ غیر نامیاتی سالمات سے نہیں بن سکتا بلکہ صرف کسی جاندار یا جاندار کے کسی حصے سے بن سکتا ہے۔','د حیاتي ځواک نظریه','هغه نظریه چې عضوي مالیکول له غیر عضوي مالیکولونو نه شي جوړېدای، بلکې یوازې له ژوندي موجود یا د هغه له کومې برخې جوړېدای شي.'),
('Williamson Synthesis','A method of synthesizing ethers by reaction of a sodium alkoxide with a halogen derivative of a hydrocarbon (as an alkyl halide).','ولیمسن تالیف','سوڈیم الکوآکسائیڈ کے ہائیڈروکاربن کے ہیلوجن مشتق (جیسے الکائل ہیلائیڈ) سے تعامل کے ذریعے ایتھرز کی تالیف کا طریقہ۔','د ولیمسن جوړښت','د سوډیم الکوکساید او د هایدروکاربن د هالوجن مشتق (لکه الکایل هالاید) د تعامل په واسطه د ایترونو د جوړولو طریقه.')]
r=glossary_record('24.18',199,(392,392),E)
r['title']='Glossary (printed 392)';r['headingUrdu']='فرہنگ (صفحہ 392)';r['headingPashto']='لغتنامه (مخ 392)'
r['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':199,'printedPages':[392]}];r['insertBefore']='24.exercise.solved'
refs=['Shriver and Atkins’ Inorganic Chemistry, Fifth Edition, by P.W. Atkins, T.L. Overton, J.P. Rourke, M.T. Weller, and F.A. Armstrong, Published by W. H. Freeman and Company New York.',
'General Chemistry: The Essential Concepts, Sixth Edition by R. Chang and J. Overby Published by McGraw-Hill.',
'General chemistry: principles and modern applications, Eleventh edition by Ralph H. Petrucci, F. Geoffrey Herring, Jeffrey D. Madura, Carey Bissonnette. Published by Pearson Canada Inc.',
'Advanced Inorganic chemistry, Third Edition, by F. Albert Cotton and G. Wilkinson Published by John Wiley & Sons, Inc.',
'Fundamentals of Inorganic chemistry, An introductory text for degree course studies, by J. Barrett and M. A. Malati Published by Horwood Publishing Limited International Publishers Coll House, Westergate, Chichester, West Sussex, PO20 6QL England.',
'Inorganic Chemistry, by R. Garg and R. Singh, Published by McGraw Hill Education (India) Private Limited.',
'Organic Chemistry by L. G. Wade, Jr. Eight Edition 2013; Pearson Education, Inc.',
'Organic Chemistry by Francis A. Carey; Tenth Edition 2016; McGraw-Hill Higher Education.',
'Organic Chemistry by David Klein; Third Edition 2017; John Wiley and Sons, Inc.',
'Organic Chemistry, by J. Clayden; Second Edition 2012; Oxford University Press.',
'A Textbook of Organic Chemistry by M. Younas; 2017 Edition; Ilmi Kitab Khana.',
'Spectroscopy by D. L. Pavia; Fifth Edition 2015; Cengage Learning.',
'Organic Spectroscopy and Chromatography by M. Younas: Edition 2007; Ilmi Kitab Khana.']
P=[pair('References','حوالہ جات','ماخذونه')];L=[{'type':'heading','indices':[0]}]
for i,x in enumerate(refs,1):P.append(pair(f'{i}. {x}',f'{i}. {x}',f'{i}. {x}'))
L.append({'type':'lines','indices':list(range(1,len(P)))})
rr=section('24.19','References','حوالہ جات','ماخذونه',P,L,[],'393')
rr['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':199,'printedPages':[393]}];rr['insertBefore']='24.exercise.solved'
rr['translationNote']='Bibliographic entries are kept in their original English form in all three languages.'
if __name__=='__main__':save(199,[r,rr],chapter_number=24)
