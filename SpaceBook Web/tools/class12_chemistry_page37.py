"""PDF37 printed66–67, chromium equilibria and organic oxidation."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def eq(e):add(e,e,e,'equation')
add('The compounds in which chromium shows +6 oxidation state are chromium trioxide (CrO₃), potassium chromate (K₂CrO₄) and potassium dichromate (K₂Cr₂O₇) etc.',
 'کرومیم کی +6 تکسیدی حالت والے مرکبات کرومیم ٹرائی آکسائیڈ (CrO₃)، پوٹاشیم کرومیٹ (K₂CrO₄) اور پوٹاشیم ڈائی کرومیٹ (K₂Cr₂O₇) وغیرہ ہیں۔',
 'د کرومیم د +6 اکسیدېشن حالت مرکبات کرومیم ټرای اکسایډ (CrO₃)، پوتاشیم کرومېټ (K₂CrO₄) او پوتاشیم ډای کرومېټ (K₂Cr₂O₇) او نور دي.')
add('14.3.2.2 Chromate – Dichromate Equilibrium','14.3.2.2 کرومیٹ — ڈائی کرومیٹ توازن','14.3.2.2 کرومېټ — ډای کرومېټ تعادل','heading')
add('When solid potassium chromate, K₂CrO₄, is dissolved in water it forms a yellow solution. When solid potassium dichromate, K₂Cr₂O₇, is dissolved in water the resulting solution is orange. The colours come from the negative ions CrO₄²⁻(aq) and Cr₂O₇²⁻(aq). However, in solution these ions are actually in equilibrium as indicated by the equation:',
 'ٹھوس پوٹاشیم کرومیٹ K₂CrO₄ پانی میں حل ہو تو پیلا محلول بناتا ہے۔ ٹھوس پوٹاشیم ڈائی کرومیٹ K₂Cr₂O₇ پانی میں حل ہو تو حاصل شدہ محلول نارنجی ہے۔ رنگ منفی آئنوں CrO₄²⁻(aq) اور Cr₂O₇²⁻(aq) سے ہیں۔ تاہم محلول میں یہ آئن حقیقتاً توازن میں ہیں، جیسا مساوات دکھاتی ہے:',
 'جامد پوتاشیم کرومېټ K₂CrO₄ چې په اوبو کې حل شي، ژېړ محلول جوړوي. جامد پوتاشیم ډای کرومېټ K₂Cr₂O₇ چې په اوبو کې حل شي، ترلاسه شوی محلول نارنجي وي. رنګونه له منفي ایونونو CrO₄²⁻(aq) او Cr₂O₇²⁻(aq) څخه دي. خو په محلول کې دا ایونونه په حقیقت کې په تعادل کې دي، لکه معادله چې ښيي:')
svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 250" role="img"><g stroke="#404040" stroke-width="3"><path d="M70 30V205Q130 230 190 205V30" fill="none"/><path d="M230 30V205Q290 230 350 205V30" fill="none"/><path d="M73 80Q130 100 187 80V203Q130 224 73 203Z" fill="#eacb38"/><path d="M233 80Q290 100 347 80V203Q290 224 233 203Z" fill="#d87024"/><ellipse cx="130" cy="30" rx="60" ry="10" fill="none"/><ellipse cx="290" cy="30" rx="60" ry="10" fill="none"/></g></svg>'
blocks.append({'id':'chem12-p66-solution-beakers','svg':svg,'svgUrdu':svg,'svgPashto':svg});layout.append({'type':'visual','blockId':blocks[-1]['id']})
eq('2CrO₄²⁻(aq) + 2H⁺(aq) ⇌ Cr₂O₇²⁻(aq) + H₂O(l)')
add('This is dynamic equilibrium and sensitive to the acidity and basicity of solution. According to Le-Chatelier’s principle, the addition of acid to the reactant shifts the equilibrium towards right and yields more dichromate (orange). On the other hand, the addition of base promotes the conversion of dichromate to chromate.',
 'یہ حرکی توازن ہے اور محلول کی تیزابیت اور اساسیت کے لیے حساس ہے۔ لی شاتلیے کے اصول کے مطابق عامل میں تیزاب کا اضافہ توازن دائیں منتقل کرتا اور زیادہ ڈائی کرومیٹ (نارنجی) پیدا کرتا ہے۔ دوسری طرف اساس کا اضافہ ڈائی کرومیٹ کو کرومیٹ میں بدلنے کو فروغ دیتا ہے۔',
 'دا متحرک تعادل دی او د محلول اسیدیت او قلویت ته حساس دی. د لي شاتلیې د اصل له مخې تعامل کوونکي ته د اسید زیاتول تعادل ښي لوري ته وړي او ډېر ډای کرومېټ (نارنجي) جوړوي. بل لوري ته د قلوي زیاتول د ډای کرومېټ په کرومېټ بدلول زیاتوي.')
eq('2OH⁻ + Cr₂O₇²⁻ ⇌ 2CrO₄²⁻ + H₂O')
add('Orange — Yellow','نارنجی — پیلا','نارنجي — ژېړ')
add('14.3.2.3 Reduction of Chromate (VI) Ions with Zn and an Acid','14.3.2.3 Zn اور تیزاب سے کرومیٹ(VI) آئنوں کی تخفیف','14.3.2.3 په Zn او اسید د کرومېټ(VI) ایونونو احیا','heading')
add('Dichromate (VI) ions (for example, in potassium dichromate (VI) solution) can be reduced to chromium (III) ions and chromium (II) ions using zinc and either dilute sulphuric acid or hydrochloric acid.',
 'ڈائی کرومیٹ(VI) آئن (مثلاً پوٹاشیم ڈائی کرومیٹ(VI) محلول میں) زنک اور پتلا سلفیورک یا ہائیڈروکلورک تیزاب استعمال کرکے کرومیم(III) اور کرومیم(II) آئنوں میں تخفیف پا سکتے ہیں۔',
 'ډای کرومېټ(VI) ایونونه (لکه د پوتاشیم ډای کرومېټ(VI) په محلول کې) د جستو او رقیق سلفوریک یا هایدروکلوریک اسید په کارولو کرومیم(III) او کرومیم(II) ایونونو ته احیا کېدای شي.')
add('Acidic potassium dichromate solution reacts with zinc forming Cr³⁺ ions and colour of the solution changes from orange to green.','تیزابی پوٹاشیم ڈائی کرومیٹ محلول زنک سے تعامل کرکے Cr³⁺ آئن بناتا ہے اور محلول نارنجی سے سبز ہوتا ہے۔','اسیدي پوتاشیم ډای کرومېټ محلول له جستو سره تعامل کوي، Cr³⁺ ایونونه جوړوي او محلول له نارنجي څخه شین کېږي.')
add('For reduction from +6 to +3,','+6 سے +3 تک تخفیف کے لیے،','له +6 څخه +3 ته د احیا لپاره،')
eq('Cr₂O₇²⁻ + 14H⁺ + 3Zn → 2Cr³⁺ + 7H₂O + 3Zn²⁺')
add('and then after further reduction by the zinc, Cr⁺² ions are formed and colour changes from green to blue.','پھر زنک سے مزید تخفیف کے بعد Cr⁺² آئن بنتے ہیں اور رنگ سبز سے نیلا ہوتا ہے۔','بیا د جستو په وسیله له نورې احیا وروسته Cr⁺² ایونونه جوړېږي او رنګ له شین څخه نیلي کېږي.')
add('For reduction from +3 to +2','+3 سے +2 تک تخفیف کے لیے','له +3 څخه +2 ته د احیا لپاره')
eq('2Cr³⁺ + Zn → 2Cr²⁺ + Zn²⁺')
add('14.3.2.4 Potassium Dichromate as an Oxidizing Agent in Organic Chemistry','14.3.2.4 نامیاتی کیمیا میں پوٹاشیم ڈائی کرومیٹ بطور تکسیدی عامل','14.3.2.4 په عضوي کیمیا کې پوتاشیم ډای کرومېټ د اکسیدوونکي په توګه','heading')
add('Potassium dichromate (VI) is used as an oxidizing agent in organic reactions. The solution of potassium dichromate (VI) is acidified with dilute sulphuric acid. When oxidation occurs, the orange solution containing the dichromate (VI) ions is reduced to a green solution containing chromium (III) ions.',
 'پوٹاشیم ڈائی کرومیٹ(VI) نامیاتی تعاملات میں تکسیدی عامل ہے۔ اس کا محلول پتلے سلفیورک تیزاب سے تیزابی بنایا جاتا ہے۔ تکسید ہو تو ڈائی کرومیٹ(VI) آئنوں والا نارنجی محلول تخفیف پاکر کرومیم(III) آئنوں والا سبز محلول بنتا ہے۔',
 'پوتاشیم ډای کرومېټ(VI) په عضوي تعاملونو کې اکسیدوونکی دی. محلول یې په رقیق سلفوریک اسید اسیدي کېږي. چې اکسیدېشن وشي، د ډای کرومېټ(VI) ایونونو نارنجي محلول احیا کېږي او د کرومیم(III) ایونونو شین محلول جوړېږي.')
add('i. Primary Alcohols','i. ابتدائی الکوحل','i. لومړني الکولونه','heading')
add('Primary alcohol are oxidized to either aldehydes or carboxylic acids depending on the reaction conditions.','ابتدائی الکوحل تعامل کی شرائط کے لحاظ سے ایلڈیہائیڈز یا کاربوکسلک تیزابوں میں تکسید پاتے ہیں۔','لومړني الکولونه د تعامل د شرایطو له مخې الدیهایډونو یا کاربوکسیلیک اسیدونو ته اکسیدېږي.')
add('In the case of the formation of carboxylic acids, the alcohol is first oxidized to an aldehyde, which is then oxidized further to the acid.','کاربوکسلک تیزاب بننے کی صورت میں الکوحل پہلے ایلڈیہائیڈ میں تکسید پاتا ہے، جو پھر مزید تکسید سے تیزاب بنتا ہے۔','د کاربوکسیلیک اسیدونو د جوړېدو په حالت کې الکول لومړی الدیهایډ ته اکسیدېږي، چې بیا په نور اکسیدېشن اسید جوړوي.')
add('Partial Oxidation to Aldehydes','ایلڈیہائیڈز میں جزوی تکسید','الدیهایډونو ته جزوي اکسیدېشن','heading')
add('We get an aldehyde if we use an excess of alcohol and remove aldehyde as soon as it is formed in order to avoid further oxidation.','الکوحل کی زائد مقدار استعمال کریں اور ایلڈیہائیڈ بنتے ہی نکال دیں تاکہ مزید تکسید نہ ہو تو ایلڈیہائیڈ حاصل ہوتا ہے۔','که الکول په زیاته اندازه وکاروو او الدیهایډ له جوړېدو سره سم لرې کړو چې نور اکسیدېشن ونه شي، الدیهایډ ترلاسه کوو.')
eq('3CH₃CH₂OH + Cr₂O₇²⁻ + 8H⁺ → 3CH₃CHO + 2Cr³⁺ + 7H₂O')
add('primary alcohol — Acetaldehyde','ابتدائی الکوحل — ایسیٹ ایلڈیہائیڈ','لومړنی الکول — اسیت الدیهایډ')
add('Full Oxidation to Carboxylic Acids','کاربوکسلک تیزابوں میں مکمل تکسید','کاربوکسیلیک اسیدونو ته بشپړ اکسیدېشن','heading')
add('The alcohol is heated with an excess of the oxidizing agent i.e. potassium dichromate (VI), on completion of the reaction, the carboxylic acid is produced.','الکوحل تکسیدی عامل، یعنی پوٹاشیم ڈائی کرومیٹ(VI)، کی زائد مقدار کے ساتھ گرم کیا جاتا ہے؛ تعامل مکمل ہونے پر کاربوکسلک تیزاب بنتا ہے۔','الکول د اکسیدوونکي، یعنې پوتاشیم ډای کرومېټ(VI)، له زیاتې اندازې سره تودېږي؛ د تعامل په بشپړېدو کاربوکسیلیک اسید جوړېږي.')
eq('3CH₃CH₂OH + 2Cr₂O₇²⁻ + 16H⁺ → 3CH₃COOH + 4Cr³⁺ + 11H₂O')
add('primary alcohol — ethanoic acid','ابتدائی الکوحل — ایتھانوئک تیزاب','لومړنی الکول — ایتانویک اسید')
add('ii. Secondary Alcohols','ii. ثانوی الکوحل','ii. ثانوي الکولونه','heading')
add('Secondary alcohols are oxidized to ketones. When the secondary alcohol, 2-propanol is heated with potassium dichromate (VI) solution acidified with dilute sulphuric acid, ketone (propanone) is produced.',
 'ثانوی الکوحل کیٹونز میں تکسید پاتے ہیں۔ ثانوی الکوحل 2-پروپانول کو پتلے سلفیورک تیزاب سے تیزابی بنائے گئے پوٹاشیم ڈائی کرومیٹ(VI) محلول کے ساتھ گرم کریں تو کیٹون (پروپانون) بنتا ہے۔',
 'ثانوي الکولونه کیټونونو ته اکسیدېږي. ثانوي الکول 2-پروپانول چې د پوتاشیم ډای کرومېټ(VI) له هغه محلول سره تود شي چې په رقیق سلفوریک اسید اسیدي شوی وي، کیټون (پروپانون) جوړېږي.')
svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 750 220" role="img"><g font-family="Arial" font-size="22" fill="#222"><text x="25" y="100">CH₃—C—H + [O]</text><text x="94" y="47">OH</text><text x="92" y="153">CH₃</text><path d="M105 55V80M105 105V132M250 95H440" stroke="#222" stroke-width="2"/><path d="M440 95L425 87V103Z"/><text x="300" y="75">K₂Cr₂O₇</text><text x="475" y="100">CH₃—C—CH₃ + H₂O</text><text x="548" y="47">O</text><path d="M554 55V80M560 55V80" stroke="#222" stroke-width="2"/><text x="280" y="122" font-size="18">Conc. H₂SO₄</text><text x="20" y="195" font-size="17">2-propanol(Secondary alcohol)</text><text x="535" y="140" font-size="17">ketone</text></g></svg>'
blocks.append({'id':'chem12-p67-propanol-oxidation','svg':svg,'svgUrdu':svg,'svgPashto':svg});layout.append({'type':'visual','blockId':blocks[-1]['id']})
add('Conc. H₂SO₄; 2-propanol (Secondary alcohol) → ketone','مرتکز H₂SO₄؛ 2-پروپانول (ثانوی الکوحل) → کیٹون','غلیظ H₂SO₄؛ 2-پروپانول (ثانوي الکول) → کیټون')
add('iii. Tertiary Alcohols','iii. ثالثی الکوحل','iii. ثالثي الکولونه','heading')
add('Tertiary alcohols are not oxidized by acidified sodium or potassium dichromate(VI) solution.','ثالثی الکوحل تیزابی سوڈیم یا پوٹاشیم ڈائی کرومیٹ(VI) محلول سے تکسید نہیں پاتے۔','ثالثي الکولونه د اسیدي سوډیم یا پوتاشیم ډای کرومېټ(VI) محلول په وسیله نه اکسیدېږي.')
record=section('14.12','Chromium equilibria and oxidation reactions','کرومیم کے توازن اور تکسیدی تعاملات','د کرومیم تعادلونه او اکسیدېشن تعاملونه',paras,layout,blocks,'66–67');record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':37,'printedPages':[66,67]}]
if __name__=='__main__':save(37,[record],trim=[{'id':'14.13','startsAt':'14.3.2.5 Potassium Dichromate'}],chapter_number=14)
