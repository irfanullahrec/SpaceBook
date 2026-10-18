"""Faithful water/oxygen/chlorine reactions, printed pages 8–9."""
from class12_chemistry_opening import pair, section, SOURCE
from class12_chemistry_sync import save
paras=[];layout=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def head(en,ur,ps):add(en,ur,ps,'heading')
def eq(value):add(value,value,value,'equation')
add('The strength of the Van der Waal’s forces decreases as the size of the molecule decreases, so the melting and boiling points decreases in the order:',
    'سالمے کی جسامت کم ہونے پر وان ڈر والز قوتوں کی طاقت کم ہوتی ہے، اس لیے پگھلنے اور ابلنے کے درجے درج ذیل ترتیب میں کم ہوتے ہیں:',
    'د مالیکول د اندازې په کمېدو سره د وان در والس قوو پیاوړتیا کمېږي، نو د وېلې کېدو او اېشېدو ټکي په لاندې ترتیب ټیټېږي:')
eq('S₈ > P₄ > Cl₂ > Ar')
head('13.1.2 Reactions of the Period 3ʳᵈ Elements with Water, Oxygen and Chlorine','13.1.2 تیسرے دور کے عناصر کے پانی، آکسیجن اور کلورین کے ساتھ تعاملات','13.1.2 له اوبو، اکسیجن او کلورین سره د درېیمې دورې د عناصرو تعاملونه')
head('i. Reactions of the Period 3ʳᵈ Elements with Water','i. تیسرے دور کے عناصر کے پانی کے ساتھ تعاملات','i. له اوبو سره د درېیمې دورې د عناصرو تعاملونه')
add('Sodium undergoes exothermic reaction with cold water producing hydrogen and a solution of sodium hydroxide.',
    'سوڈیم ٹھنڈے پانی کے ساتھ حرارت خارج کرنے والا تعامل کرتا ہے، جس سے ہائیڈروجن اور سوڈیم ہائیڈرو آکسائیڈ کا محلول بنتا ہے۔',
    'سوډیم له سړو اوبو سره تودوخه خوشې کوونکی تعامل کوي او هایدروجن او د سوډیم هایدروکسایډ محلول جوړوي.')
eq('2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g)')
add('Magnesium reacts slowly with cold water but burns in steam. A clean coil of magnesium dropped into cold water eventually is covered with small bubbles of hydrogen, which floats it to the surface. Magnesium form a very thin layer of magnesium hydroxide on the surface, which tends to stop it from further reaction.',
    'میگنیشیم ٹھنڈے پانی کے ساتھ آہستہ تعامل کرتا ہے، مگر بھاپ میں جلتا ہے۔ ٹھنڈے پانی میں ڈالی گئی میگنیشیم کی صاف کنڈلی آخرکار ہائیڈروجن کے چھوٹے بلبلوں سے ڈھک جاتی ہے، جو اسے سطح پر تیراتے ہیں۔ میگنیشیم کی سطح پر میگنیشیم ہائیڈرو آکسائیڈ کی بہت باریک تہہ بنتی ہے، جو مزید تعامل کو روکنے کا رجحان رکھتی ہے۔',
    'مګنیزیم له سړو اوبو سره ورو تعامل کوي، خو په بخار کې سوځي. په سړو اوبو کې اچول شوې د مګنیزیم پاکه تاو شوې پټه په پای کې د هایدروجن په کوچنیو پوکاڼو پوښل کېږي، چې سطحې ته یې راخېژوي. مګنیزیم پر سطحه د مګنیزیم هایدروکسایډ ډېره نرۍ طبقه جوړوي، چې د نور تعامل د مخنیوي تمایل لري.')
eq('Mg(s) + 2H₂O(l) → Mg(OH)₂(aq) + H₂(g)')
add('Magnesium burns in steam with its typical white flame to produce white magnesium oxide and hydrogen.',
    'میگنیشیم بھاپ میں اپنے مخصوص سفید شعلے کے ساتھ جلتا ہے اور سفید میگنیشیم آکسائیڈ اور ہائیڈروجن بناتا ہے۔',
    'مګنیزیم په بخار کې په خپل ځانګړي سپین لمبه سوځي او سپین مګنیزیم اکسایډ او هایدروجن جوړوي.')
eq('Mg(s) + H₂O(g) → MgO(s) + H₂(g)')
add('Aluminium powder when heated in steam produces hydrogen and aluminium. This reaction is relatively slow with bulk because of the formation of strong aluminium oxide layer on the metal and build-up of even more oxide during reaction.',
    'ایلومینیم کا سفوف بھاپ میں گرم کرنے پر ہائیڈروجن اور ایلومینیم بناتا ہے۔ بڑے ٹکڑے کے ساتھ یہ تعامل نسبتاً آہستہ ہوتا ہے، کیونکہ دھات پر ایلومینیم آکسائیڈ کی مضبوط تہہ بنتی ہے اور تعامل کے دوران مزید آکسائیڈ جمع ہوتی ہے۔',
    'د المونیم پوډر په بخار کې د تودولو پر مهال هایدروجن او المونیم جوړوي. دا تعامل له لویې ټوټې سره نسبتاً ورو وي، ځکه پر فلز د المونیم اکسایډ پیاوړې طبقه جوړېږي او د تعامل پر مهال نور اکسایډ هم راټولېږي.')
eq('2Al(s) + 3H₂O(g) → Al₂O₃(s) + 3H₂(g)')
add('Silicon react with steam at red heat to produce silicon dioxide and hydrogen.',
    'سلیکان سرخ تپش پر بھاپ کے ساتھ تعامل کر کے سلیکان ڈائی آکسائیڈ اور ہائیڈروجن بناتا ہے۔',
    'سیلیکان په سره تودوخه کې له بخار سره تعامل کوي او سیلیکان ډای اکسایډ او هایدروجن جوړوي.')
eq('Si(s) + 2H₂O(g) → SiO₂(s) + 2H₂(g)')
add('Chlorine dissolves in water to some extent to give a pale green solution. A reversible reaction takes place to produce a mixture of hydrochloric acid and chloric (I) acid (hypochlorous acid), which decompose to HCl on exposure to sunlight.',
    'کلورین کسی حد تک پانی میں حل ہو کر ہلکا سبز محلول بناتی ہے۔ ایک قابلِ واپسی تعامل سے ہائیڈروکلورک ایسڈ اور کلورک (I) ایسڈ (ہائپوکلورس ایسڈ) کا آمیزہ بنتا ہے، جو سورج کی روشنی میں HCl میں تحلیل ہوتا ہے۔',
    'کلورین تر یوه حده په اوبو کې حل کېږي او کم رنګه شین محلول جوړوي. یو بېرته ګرځېدونکی تعامل د هایدروکلوریک اسید او کلوریک (I) اسید (هایپوکلورس اسید) مخلوط جوړوي، چې د لمر په رڼا کې په HCl تجزیه کېږي.')
eq('Cl₂(g) + H₂O(l) ⇌ HCl(aq) + HOCl(aq)')
eq('HOCl(aq) → HCl(aq) + ½ O₂(g)')
add('Net reaction:','مجموعی تعامل:','ټولیز تعامل:')
eq('Cl₂(g) + H₂O(l) → 2HCl(aq) + ½ O₂(g)')
add('There is no reaction between argon and water.','آرگن اور پانی کے درمیان کوئی تعامل نہیں ہوتا۔','د ارګون او اوبو ترمنځ تعامل نه کېږي.')
head('ii. Reactions of the Period 3ʳᵈ Elements with Oxygen','ii. تیسرے دور کے عناصر کے آکسیجن کے ساتھ تعاملات','ii. له اکسیجن سره د درېیمې دورې د عناصرو تعاملونه')
add('Sodium burns in a limited supply of air (oxygen) with a pale yellow flame to produce a white solid of sodium oxide. In sodium oxide, the oxidation state of oxygen is −2.',
    'سوڈیم ہوا (آکسیجن) کی محدود فراہمی میں ہلکے زرد شعلے کے ساتھ جل کر سوڈیم آکسائیڈ کا سفید ٹھوس مادہ بناتا ہے۔ سوڈیم آکسائیڈ میں آکسیجن کی تکسیدی حالت −2 ہے۔',
    'سوډیم د هوا (اکسیجن) په محدوده اندازه کې په کم رنګه ژېړه لمبه سوځي او د سوډیم اکسایډ سپین جامد جوړوي. په سوډیم اکسایډ کې د اکسیجن اکسیدېشن حالت −2 دی.')
eq('4Na(s) + O₂(g) → 2Na₂O(s)')
add('Sodium burns in an excess of air (oxygen) with a flame to produce a pale yellow solid of sodium peroxide. In sodium peroxide the oxidation state of oxygen is −1.',
    'سوڈیم ہوا (آکسیجن) کی زیادہ مقدار میں شعلے کے ساتھ جل کر سوڈیم پرآکسائیڈ کا ہلکا زرد ٹھوس مادہ بناتا ہے۔ سوڈیم پرآکسائیڈ میں آکسیجن کی تکسیدی حالت −1 ہے۔',
    'سوډیم د هوا (اکسیجن) په زیاته اندازه کې په لمبه سوځي او د سوډیم پراکسایډ کم رنګه ژېړ جامد جوړوي. په سوډیم پراکسایډ کې د اکسیجن اکسیدېشن حالت −1 دی.')
eq('2Na(s) + O₂(g) → Na₂O₂(s)')
add('When sodium peroxide react with oxygen at high temperature and pressure, it produces a yellow-orange solid of sodium superoxide (NaO₂). In sodium superoxide the oxidation state of oxygen is −½.',
    'سوڈیم پرآکسائیڈ بلند درجۂ حرارت اور دباؤ پر آکسیجن کے ساتھ تعامل کر کے سوڈیم سپرآکسائیڈ (NaO₂) کا زرد نارنجی ٹھوس مادہ بناتا ہے۔ سوڈیم سپرآکسائیڈ میں آکسیجن کی تکسیدی حالت −½ ہے۔',
    'سوډیم پراکسایډ په لوړه تودوخه او فشار کې له اکسیجن سره تعامل کوي او د سوډیم سوپراکسایډ (NaO₂) ژېړ نارنجي جامد جوړوي. په سوډیم سوپراکسایډ کې د اکسیجن اکسیدېشن حالت −½ دی.')
eq('Na₂O₂(s) + O₂(g) → 2NaO₂(s)')
add('Magnesium burns in oxygen with an intense flame to give white solid magnesium oxide.',
    'میگنیشیم آکسیجن میں تیز شعلے کے ساتھ جل کر سفید ٹھوس میگنیشیم آکسائیڈ بناتا ہے۔',
    'مګنیزیم په اکسیجن کې په تېزه لمبه سوځي او سپین جامد مګنیزیم اکسایډ جوړوي.')
eq('2Mg(s) + O₂(g) → 2MgO(s)')
add('Aluminium burns in oxygen, if it is powdered, otherwise, the strong oxide layer on aluminium tends to inhibit the reaction.',
    'ایلومینیم سفوف کی صورت میں آکسیجن میں جلتا ہے؛ ورنہ اس پر آکسائیڈ کی مضبوط تہہ تعامل کو روکنے کا رجحان رکھتی ہے۔',
    'المونیم که د پوډر په بڼه وي په اکسیجن کې سوځي؛ که نه، پر المونیم د اکسایډ پیاوړې طبقه د تعامل د مخنیوي تمایل لري.')
eq('4Al(s) + 3O₂(g) → 2Al₂O₃(s)')
add('Silicon burns in oxygen if heated strongly enough. Silicon dioxide is produced.',
    'سلیکان کو کافی شدت سے گرم کرنے پر وہ آکسیجن میں جلتا ہے اور سلیکان ڈائی آکسائیڈ بنتی ہے۔',
    'سیلیکان که په کافي اندازه ډېر تود شي په اکسیجن کې سوځي او سیلیکان ډای اکسایډ جوړېږي.')
eq('Si(s) + O₂(g) → SiO₂(s)')
add('White phosphorus catches fire spontaneously in air, burning with white flame and produces clouds of white smoke. A mixture of phosphorus trioxide (phosphorus (III) oxide) and phosphorus pentaoxide (phosphorus (V) oxide) is formed.',
    'سفید فاسفورس ہوا میں خود بخود آگ پکڑتا ہے، سفید شعلے کے ساتھ جلتا ہے اور سفید دھوئیں کے بادل بناتا ہے۔ فاسفورس ٹرائی آکسائیڈ (فاسفورس (III) آکسائیڈ) اور فاسفورس پینٹا آکسائیڈ (فاسفورس (V) آکسائیڈ) کا آمیزہ بنتا ہے۔',
    'سپین فاسفورس په هوا کې په خپله اور اخلي، په سپینه لمبه سوځي او د سپین لوګي ورېځې جوړوي. د فاسفورس ټرای اکسایډ (فاسفورس (III) اکسایډ) او فاسفورس پنتا اکسایډ (فاسفورس (V) اکسایډ) مخلوط جوړېږي.')
add('For phosphorus trioxide:','فاسفورس ٹرائی آکسائیڈ کے لیے:','د فاسفورس ټرای اکسایډ لپاره:')
eq('P₄(s) + 3O₂(g) → P₄O₆(g)')
add('For phosphorus pentaoxide:','فاسفورس پینٹا آکسائیڈ کے لیے:','د فاسفورس پنتا اکسایډ لپاره:')
eq('P₄(s) + 5O₂(g) → P₄O₁₀(g)')
add('Sulphur burns in air or oxygen on gentle heating with a pale blue flame. It produces colourless sulphur dioxide gas.',
    'سلفر ہلکا گرم کرنے پر ہوا یا آکسیجن میں ہلکے نیلے شعلے کے ساتھ جلتا ہے اور بے رنگ سلفر ڈائی آکسائیڈ گیس بناتا ہے۔',
    'سلفر په لږ تودولو سره په هوا یا اکسیجن کې په کم رنګه آبي لمبه سوځي او بې رنګه سلفر ډای اکسایډ ګاز جوړوي.')
eq('S(s) + O₂(g) → SO₂(g)')
head('iii. Reactions of the Period 3ʳᵈ Elements with Chlorine','iii. تیسرے دور کے عناصر کے کلورین کے ساتھ تعاملات','iii. له کلورین سره د درېیمې دورې د عناصرو تعاملونه')
add('Sodium burns in chlorine with a bright orange flame. White, solid sodium chloride is produced.',
    'سوڈیم کلورین میں روشن نارنجی شعلے کے ساتھ جلتا ہے اور سفید ٹھوس سوڈیم کلورائیڈ بنتا ہے۔',
    'سوډیم په کلورین کې په روښانه نارنجي لمبه سوځي او سپین جامد سوډیم کلورایډ جوړېږي.')
eq('2Na(s) + Cl₂(g) → 2NaCl(s)')
add('Magnesium burns with its usual intense white flame to give white magnesium chloride.',
    'میگنیشیم اپنے معمول کے تیز سفید شعلے کے ساتھ جل کر سفید میگنیشیم کلورائیڈ بناتا ہے۔',
    'مګنیزیم په خپله عادي تېزه سپینه لمبه سوځي او سپین مګنیزیم کلورایډ جوړوي.')
eq('Mg(s) + Cl₂(g) → MgCl₂(s)')
add('Aluminium reacts with chlorine by passing dry chlorine over aluminium foil heated in a long tube. Aluminium burns in stream of chlorine to produce pale yellow aluminium chloride.',
    'ایک لمبی نلکی میں گرم ایلومینیم کی ورق پر خشک کلورین گزارنے سے ایلومینیم کلورین کے ساتھ تعامل کرتا ہے۔ ایلومینیم کلورین کے بہاؤ میں جل کر ہلکا زرد ایلومینیم کلورائیڈ بناتا ہے۔',
    'په اوږده نل کې پر تود شوي المونیمي ورق د وچ کلورین په تېرولو سره المونیم له کلورین سره تعامل کوي. المونیم د کلورین په جریان کې سوځي او کم رنګه ژېړ المونیم کلورایډ جوړوي.')
eq('2Al(s) + 3Cl₂(g) → 2AlCl₃(s)')
record=section('13.4','13.1.2 Reactions with water, oxygen and chlorine','13.1.2 پانی، آکسیجن اور کلورین کے ساتھ تعاملات','13.1.2 له اوبو، اکسیجن او کلورین سره تعاملونه',paras,layout,[],'8–9')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':8,'printedPages':[8,9]}]
issues=[{'id':'chem12-p8-aluminium-steam','printedPage':8,'description':'The prose says steam produces hydrogen and aluminium, while the printed equation produces aluminium oxide. Both source statements are retained.'}]
if __name__=='__main__':save(8,[record],issues=issues,carry=[{'from':'13.4','to':'13.5','startsAt':'If chlorine is passed over silicon powder'}])
