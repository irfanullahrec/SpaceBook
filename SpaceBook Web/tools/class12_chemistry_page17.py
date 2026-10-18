"""PDF17 (printed26–27), including the inspected first-line continuation on28."""
from class12_chemistry_opening import pair, section, SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def head(en,ur,ps):add(en,ur,ps,'heading')
def eq(value):add(value,value,value,'equation')
headers=['Elements','Be','Mg','Ca','Sr','Ba'];values=['1.57','1.31','1.00','0.95','0.89']
add('Table 13.21 Trend in Electronegativity in Group IIA Elements','جدول 13.21 گروپ IIA کے عناصر میں برقی منفیت کا رجحان','جدول 13.21 د IIA ګروپ په عناصرو کې د برېښنا منفي توب تمایل')
t={'id':'chem12-table-13-21','headers':headers,'rows':[['Electronegativity']+values],
   'translations':[{'language':'اردو','headers':['عناصر']+headers[1:],'rows':[['برقی منفیت']+values]},
                   {'language':'پښتو','headers':['عناصر']+headers[1:],'rows':[['برېښنا منفي توب']+values]}]}
blocks.append(t);layout.append({'type':'sourceDataTable','tableId':t['id']})
head('13.3.1.4 Trend in Melting and Boiling Points','13.3.1.4 پگھلنے اور ابلنے کے درجوں کا رجحان','13.3.1.4 د وېلې کېدو او اېشېدو د ټکو تمایل')
add('Melting point: If we exclude the magnesium, there is a general decrease in melting point going down Group – IIA. However, if you include magnesium, you will see that its melting point is lower than the melting point of calcium, the next element. If you include magnesium, there is no obvious trend in melting points.',
    'نقطۂ پگھلاؤ: میگنیشیم کو چھوڑ دیں تو گروپ IIA میں نیچے جانے پر نقطۂ پگھلاؤ عموماً کم ہوتا ہے۔ تاہم میگنیشیم کو شامل کریں تو اس کا نقطۂ پگھلاؤ اگلے عنصر کیلشیم سے کم ہے۔ میگنیشیم کو شامل کرنے پر پگھلنے کے درجوں کا کوئی واضح رجحان نہیں رہتا۔',
    'د وېلې کېدو ټکی: که مګنیزیم وباسو، په IIA ګروپ کې ښکته تګ سره د وېلې کېدو ټکی عموماً ټیټېږي. خو که مګنیزیم شامل کړو، د هغه د وېلې کېدو ټکی له راتلونکي عنصر کلسیم څخه ټیټ دی. د مګنیزیم په شاملولو د وېلې کېدو په ټکو کې څرګند تمایل نه شته.')
add('Boiling point: There does not appear to be a trend in boiling points going down the group. Again magnesium is an anomaly.',
    'نقطۂ ابال: گروپ میں نیچے جانے پر ابلنے کے درجوں میں کوئی واضح رجحان نظر نہیں آتا۔ یہاں بھی میگنیشیم استثنا ہے۔',
    'د اېشېدو ټکی: په ګروپ کې ښکته تګ سره د اېشېدو په ټکو کې کوم څرګند تمایل نه ښکاري. دلته هم مګنیزیم استثنا دی.')
add('Table 13.22 Trend in Melting and Boiling points in Group – IIA Elements','جدول 13.22 گروپ IIA کے عناصر میں پگھلنے اور ابلنے کے درجوں کا رجحان','جدول 13.22 د IIA ګروپ په عناصرو کې د وېلې کېدو او اېشېدو د ټکو تمایل')
m=['1278','651','843','769','725'];b=['2477','1110','1487','1380','1640']
t={'id':'chem12-table-13-22','headers':['Element']+headers[1:],'rows':[['Melting point (°C)']+m,['Boiling point (°C)']+b],
   'translations':[{'language':'اردو','headers':['عنصر']+headers[1:],'rows':[['نقطۂ پگھلاؤ (°C)']+m,['نقطۂ ابال (°C)']+b]},
                   {'language':'پښتو','headers':['عنصر']+headers[1:],'rows':[['د وېلې کېدو ټکی (°C)']+m,['د اېشېدو ټکی (°C)']+b]}]}
blocks.append(t);layout.append({'type':'sourceDataTable','tableId':t['id']})
head('13.3.2 Trend in Reactivity with Water','13.3.2 پانی کے ساتھ تعامل پذیری کا رجحان','13.3.2 له اوبو سره د تعامل وړتیا تمایل')
add('Beryllium is the only alkaline earth metal, which does not react with water even at red heat due to much less electropositive character. The other elements of Group – IIA react with water, though slowly.',
    'بیریلیم واحد الکلائن ارتھ دھات ہے جو اپنی بہت کم برقی مثبت خصوصیت کی وجہ سے سرخ تپش پر بھی پانی سے تعامل نہیں کرتی۔ گروپ IIA کے دوسرے عناصر پانی سے تعامل کرتے ہیں، اگرچہ آہستہ۔',
    'بېریلیم یوازینی القلي ځمکنی فلز دی چې د ډېر لږ برېښنا مثبت ځانګړنې له امله ان په سره تودوخه کې له اوبو سره تعامل نه کوي. د IIA ګروپ نور عناصر له اوبو سره تعامل کوي، خو ورو.')
add('Magnesium burns in steam to produce white magnesium oxide and hydrogen gas.',
    'میگنیشیم بھاپ میں جل کر سفید میگنیشیم آکسائیڈ اور ہائیڈروجن گیس بناتا ہے۔',
    'مګنیزیم په بخار کې سوځي او سپین مګنیزیم اکسایډ او هایدروجن ګاز جوړوي.')
eq('Mg(s) + H₂O(g) → MgO(s) + H₂(g)')
add('Calcium, strontium and barium react even with cold water to form the corresponding hydroxides.',
    'کیلشیم، اسٹرونشیم اور بیریم ٹھنڈے پانی سے بھی تعامل کر کے متعلقہ ہائیڈرو آکسائیڈز بناتے ہیں۔',
    'کلسیم، سټرونشیم او بېریم ان له سړو اوبو سره تعامل کوي او اړوند هایدروکسایډونه جوړوي.')
eq('Ca(s) + 2H₂O(l) → Ca(OH)₂(aq) + H₂(g)')
add('Group – IIA elements become more reactive towards water as we go down the group.',
    'گروپ میں نیچے جانے پر گروپ IIA کے عناصر پانی کے ساتھ زیادہ تعامل پذیر ہوتے جاتے ہیں۔',
    'په ګروپ کې ښکته تګ سره د IIA ګروپ عناصر له اوبو سره لا ډېر تعامل کوونکي کېږي.')
head('13.3.3 Reactions with Oxygen and Nitrogen','13.3.3 آکسیجن اور نائٹروجن کے ساتھ تعاملات','13.3.3 له اکسیجن او نایټروجن سره تعاملونه')
add('Group – IIA elements react with oxygen to produce the respective metal oxide.',
    'گروپ IIA کے عناصر آکسیجن سے تعامل کر کے متعلقہ دھاتی آکسائیڈ بناتے ہیں۔',
    'د IIA ګروپ عناصر له اکسیجن سره تعامل کوي او اړوند فلزي اکسایډ جوړوي.')
head('13.3.3.1 Formation of Oxides','13.3.3.1 آکسائیڈز کی تشکیل','13.3.3.1 د اکسایډونو جوړېدل')
add('Ca, Sr and Ba being more electropositive, react with air readily to form a mixture of their respective oxides. The reactivity towards oxygen increases as we go down the group.',
    'Ca، Sr اور Ba زیادہ برقی مثبت ہونے کی وجہ سے ہوا سے آسانی سے تعامل کر کے اپنے متعلقہ آکسائیڈز کا آمیزہ بناتے ہیں۔ گروپ میں نیچے جانے پر آکسیجن کے ساتھ تعامل پذیری بڑھتی ہے۔',
    'Ca، Sr او Ba د ډېر برېښنا مثبت توب له امله له هوا سره په اسانه تعامل کوي او د خپلو اړوندو اکسایډونو مخلوط جوړوي. په ګروپ کې ښکته تګ سره له اکسیجن سره د تعامل وړتیا زیاتېږي.')
eq('2Ca(s) + O₂(g) → 2CaO(s)')
add('Beryllium does not react below 600°C, but in powdered form burns brilliantly. Beryllium has very strong layer of BeO on its surface, which prevents any more oxygen reaching the underlying beryllium to react with it.',
    'بیریلیم 600°C سے نیچے تعامل نہیں کرتا، مگر سفوف کی صورت میں روشن شعلے کے ساتھ جلتا ہے۔ اس کی سطح پر BeO کی بہت مضبوط تہہ مزید آکسیجن کو نیچے کے بیریلیم تک پہنچ کر تعامل کرنے سے روکتی ہے۔',
    'بېریلیم تر 600°C لاندې تعامل نه کوي، خو د پوډر په بڼه په ځلانده لمبه سوځي. پر سطحه یې د BeO ډېره پیاوړې طبقه وي، چې د نورو اکسیجن د لاندې بېریلیم ته رسېدو او ورسره تعامل کولو مخه نیسي.')
add('Thus, Ca, Ba and Sr are stored in paraffin but Be and Mg are not because they form protective oxide layer on their surface.',
    'اس لیے Ca، Ba اور Sr پیرافین میں رکھے جاتے ہیں، مگر Be اور Mg نہیں، کیونکہ ان کی سطح پر آکسائیڈ کی حفاظتی تہہ بنتی ہے۔',
    'نو Ca، Ba او Sr په پارافین کې ساتل کېږي، خو Be او Mg نه، ځکه پر سطحه یې د اکسایډ ساتونکې طبقه جوړېږي.')
head('13.3.3.2 Formation of Peroxides on Heating with Oxygen','13.3.3.2 آکسیجن کے ساتھ گرم کرنے پر پرآکسائیڈز کی تشکیل','13.3.3.2 له اکسیجن سره په تودولو د پراکسایډونو جوړېدل')
add('Be, Mg and Ca do not form peroxide when heated with oxygen. However, Sr and Ba react in oxygen to form peroxide.',
    'Be، Mg اور Ca آکسیجن کے ساتھ گرم کرنے پر پرآکسائیڈ نہیں بناتے، مگر Sr اور Ba آکسیجن سے تعامل کر کے پرآکسائیڈ بناتے ہیں۔',
    'Be، Mg او Ca له اکسیجن سره په تودولو پراکسایډ نه جوړوي، خو Sr او Ba په اکسیجن کې تعامل کوي او پراکسایډ جوړوي.')
add('Barium forms barium peroxide on heating with oxygen, but strontium reacts with oxygen to form strontium peroxide, when it is heated with oxygen under high pressure.',
    'بیریم آکسیجن کے ساتھ گرم کرنے پر بیریم پرآکسائیڈ بناتا ہے، جبکہ اسٹرونشیم بلند دباؤ پر آکسیجن کے ساتھ گرم کرنے پر اسٹرونشیم پرآکسائیڈ بناتا ہے۔',
    'بېریم له اکسیجن سره په تودولو بېریم پراکسایډ جوړوي، خو سټرونشیم له اکسیجن سره تر لوړ فشار لاندې په تودولو سټرونشیم پراکسایډ جوړوي.')
eq('Ba(s) + O₂(g) → BaO₂(s)')
eq('Sr(s) + O₂(g) → SrO₂(s)')
head('13.3.3.3 Formation of Nitrides on Heating in Air','13.3.3.3 ہوا میں گرم کرنے پر نائٹرائیڈز کی تشکیل','13.3.3.3 په هوا کې په تودولو د نایټرایډونو جوړېدل')
add('All the Group – IIA elements burn in nitrogen to form ionic nitrides of the general formula, M₃N₂.',
    'گروپ IIA کے سب عناصر نائٹروجن میں جل کر عمومی فارمولے M₃N₂ والے آئنک نائٹرائیڈز بناتے ہیں۔',
    'د IIA ګروپ ټول عناصر په نایټروجن کې سوځي او د M₃N₂ عمومي فورمول لرونکي ایوني نایټرایډونه جوړوي.')
eq('3M(s) + N₂(g) —Δ→ M₃N₂(s)')
eq('3Mg(s) + N₂(g) —Δ→ Mg₃N₂(s)')
eq('3Be(s) + N₂(g) —Δ→ Be₃N₂(s)')
add('The nitrides of Group – IIA elements are ionic and solid in nature except beryllium nitride (Be₃N₂) which is covalent and volatile.',
    'بیریلیم نائٹرائیڈ (Be₃N₂) کے علاوہ گروپ IIA کے عناصر کے نائٹرائیڈز آئنک اور ٹھوس ہیں؛ بیریلیم نائٹرائیڈ اشتراکی اور فرار پذیر ہے۔',
    'له بېریلیم نایټرایډ (Be₃N₂) پرته د IIA ګروپ د عناصرو نایټرایډونه ایوني او جامد دي؛ بېریلیم نایټرایډ کووالنټ او ژر بخار کېدونکی دی.')
head('13.3.4 Trend in Solubility of the Hydroxides, Sulphates and Carbonates','13.3.4 ہائیڈرو آکسائیڈز، سلفیٹس اور کاربونیٹس کی حل پذیری کا رجحان','13.3.4 د هایدروکسایډونو، سلفېټونو او کاربونېټونو د حل کېدو وړتیا تمایل')
head('i. Solubility of the Hydroxides','i. ہائیڈرو آکسائیڈز کی حل پذیری','i. د هایدروکسایډونو د حل کېدو وړتیا')
add('Group–II metal hydroxides become more soluble in water as we go down the group.',
    'گروپ میں نیچے جانے پر گروپ II کے دھاتی ہائیڈرو آکسائیڈز پانی میں زیادہ حل پذیر ہوتے ہیں۔',
    'په ګروپ کې ښکته تګ سره د II ګروپ فلزي هایدروکسایډونه په اوبو کې ډېر حل کېدونکي کېږي.')
add('Magnesium hydroxide appears to be insoluble in water. However, if it is shaken in water and filtered, the solution is slightly basic (pH = 9.0). This is because some magnesium hydroxide has been dissolved.',
    'میگنیشیم ہائیڈرو آکسائیڈ پانی میں غیر حل پذیر دکھائی دیتا ہے۔ تاہم اسے پانی میں ہلا کر چھانیں تو محلول معمولی اساسی ہوتا ہے (pH = 9.0)، کیونکہ کچھ میگنیشیم ہائیڈرو آکسائیڈ حل ہو چکا ہوتا ہے۔',
    'مګنیزیم هایدروکسایډ په اوبو کې ناحل کېدونکی ښکاري. خو که په اوبو کې وخوځول شي او چاڼ شي، محلول لږ قلوي وي (pH = 9.0)، ځکه یو څه مګنیزیم هایدروکسایډ حل شوی وي.')
add('Calcium hydroxide is partially soluble in water. A suspension of calcium hydroxide in water will appear at more alkaline (pH = 11) than magnesium hydroxide as it is more soluble so there will be more hydroxide ions present in solution of magnesium hydroxide.',
    'کیلشیم ہائیڈرو آکسائیڈ پانی میں جزوی طور پر حل پذیر ہے۔ پانی میں اس کا معلق آمیزہ میگنیشیم ہائیڈرو آکسائیڈ سے زیادہ الکلائن دکھائی دیتا ہے (pH = 11)، کیونکہ یہ زیادہ حل پذیر ہے، اس لیے میگنیشیم ہائیڈرو آکسائیڈ کے محلول میں زیادہ ہائیڈرو آکسائیڈ آئن ہوں گے۔',
    'کلسیم هایدروکسایډ په اوبو کې تر یوه حده حل کېږي. په اوبو کې یې تعلیق د مګنیزیم هایدروکسایډ په پرتله ډېر قلوي ښکاري (pH = 11)، ځکه ډېر حل کېدونکی دی؛ نو د مګنیزیم هایدروکسایډ په محلول کې به ډېر هایدروکسایډ ایونونه وي.')
add('Barium hydroxide is soluble enough to produce a solution with a concentration around 0.1 mol dm⁻³ at room temperature. The hydroxide ions present would make the solution strongly alkaline.',
    'بیریم ہائیڈرو آکسائیڈ اتنا حل پذیر ہے کہ کمرے کے درجۂ حرارت پر تقریباً 0.1 mol dm⁻³ ارتکاز کا محلول بناتا ہے۔ موجود ہائیڈرو آکسائیڈ آئن محلول کو شدید الکلائن بناتے ہیں۔',
    'بېریم هایدروکسایډ دومره حل کېدونکی دی چې د خونې په تودوخه کې شاوخوا 0.1 mol dm⁻³ غلظت لرونکی محلول جوړوي. موجود هایدروکسایډ ایونونه محلول ډېر قلوي کوي.')
paras[-1]['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':17,'printedPage':27},{'sourcePdf':SOURCE,'pdfPage':18,'printedPage':28,'scope':'first-line continuation only'}]
record=section('13.13','Group IIA physical properties and reactivity','گروپ IIA کی طبعی خصوصیات اور تعامل پذیری','د IIA ګروپ فزیکي ځانګړنې او د تعامل وړتیا',paras,layout,blocks,'26–27')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':17,'printedPages':[26,27]}]
record['sourceContinuations']=[{'sourcePdf':SOURCE,'pdfPage':18,'printedPage':28,'sourceParagraphIndices':[len(paras)-1],'scope':'first-line completion of the barium hydroxide paragraph'}]
issues=[{'id':'chem12-p27-hydroxide-solution','printedPage':27,'description':'The calcium hydroxide comparison ends by naming magnesium hydroxide as the solution with more hydroxide ions. Printed wording is retained in all languages.'}]
if __name__=='__main__':save(17,[record],issues=issues,carry=[{'from':'13.13','to':'13.14','startsAt':'Ba2+\nBa(OH)2(8)'}])
