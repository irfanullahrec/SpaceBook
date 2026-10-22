import re
D='D:/SpaceBook/SpaceBook Web/docs/source-verification/class-8/pashto/pages/'
def add(page, prefix, ps, en, ur):
    f=D+f'p{page}.txt'; L=open(f,encoding='utf8').read().split('\n')
    i=next(k for k,l in enumerate(L) if l.startswith(prefix))
    j=i+1
    while j<len(L) and not (L[j].startswith('endtable') or re.match(r'q |qp |sol|##|@|p ',L[j])): j+=1
    if j<len(L) and L[j].startswith('endtable'): j+=1
    assert not (j<len(L) and L[j].startswith('sol')), page
    L.insert(j,f'sol {ps} || {en} || {ur}')
    open(f,'w',encoding='utf8',newline='\n').write('\n'.join(L))
add('013','q 4 | د لاندینو واحد',
 'عادت = عادتونه؛ سیرت = سیرتونه؛ بنیادم = بنیادمان؛ صحابي = صحابه کرام؛ خوراک = خوراکونه۔',
 'Plurals: عادت = عادتونه (habits); سیرت = سیرتونه (characters); بنیادم = بنیادمان (human beings); صحابي = صحابه کرام (companions); خوراک = خوراکونه (foods).',
 'جمع: عادت = عادتونه؛ سیرت = سیرتونه؛ بنیادم = بنیادمان؛ صحابي = صحابه کرام؛ خوراک = خوراکونه۔')
add('066','q 4 | د دې ټکو مذکر',
 'جینۍ = هلک؛ مور = پلار؛ خور = ورور؛ چیلې = چیلے؛ ګډېنه = ګډ (Derived: د ګډېنې مذکر په کتاب کې نه دے ورکړے شوے)۔',
 'Masculines: جینۍ (girl) = هلک (boy); مور (mother) = پلار (father); خور (sister) = ورور (brother); چیلې (she-kid) = چیلے; ګډېنه (ewe) = ګډ (ram). The last two are Derived: the book gives no key.',
 'مذکر: جینۍ = هلک؛ مور = پلار؛ خور = ورور؛ چیلې = چیلے؛ ګډېنه = ګډ (آخری دو: Derived، کتاب میں کلید نہیں)۔')
add('022','q 6 | د دې روزمرو',
 'په مندہ مندہ تلل = په تلوار تلل؛ په حق رسېدل = مړ کېدل، د دنیا نه تلل؛ خاورو ته سپارل = ښخول، دفنول۔',
 'Idioms: په مندہ مندہ تلل = to go in a hurry; په حق رسېدل = to die, to pass away; خاورو ته سپارل = to bury.',
 'محاورے: په مندہ مندہ تلل = جلدی میں جانا؛ په حق رسېدل = وفات پانا؛ خاورو ته سپارل = دفن کرنا۔')
add('033','q 6 | د دې محاورو معنې',
 'بې وهل = ټکر وهل، ټینګ ټکر کول (Derived)؛ اوازه خوېدل = خبره خپرېدل، شهرت موندل؛ زړۀ ساتل = خاطر ساتل، زړۀ ته پام کول؛ لاس په سر کېدل = ډېر خپه کېدل، حیران پاتې کېدل۔',
 'Idioms: بې وهل = to strike hard (Derived); اوازه خوېدل = for news to spread, to become famous; زړۀ ساتل = to care for someone\'s feelings; لاس په سر کېدل = to be very distressed, to be left helpless. Not verified: no key in the book.',
 'محاورے: بې وهل = زور سے ٹکر مارنا (Derived)؛ اوازه خوېدل = بات پھیلنا، مشہور ہونا؛ زړۀ ساتل = دل کا خیال رکھنا؛ لاس په سر کېدل = بہت غم زدہ ہونا۔ Not verified۔')
add('043','q 6 | د دې محاورو',
 'غلې کښېناستل = چوپ شو، هېڅ نۀ وئیل؛ پېښې ښوئېدل = حالات بدلېدل؛ په شا کېدل = شاته کېدل، پرېښودل (Derived)۔',
 'Idioms: غلې کښېناستل = to sit silent, to say nothing; پېښې ښوئېدل = for events to change; په شا کېدل = to turn back, to give up. Derived: no key in the book.',
 'محاورے: غلې کښېناستل = خاموش بیٹھ جانا؛ پېښې ښوئېدل = حالات بدلنا؛ په شا کېدل = پیچھے ہٹنا (Derived)۔')
