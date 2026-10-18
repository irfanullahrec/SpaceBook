from physics_agent1_sequential import save, render, crop
quotes=[
 dict(reference='سورہ یٰس - 40',arabic='لَا الشَّمْسُ يَنْبَغِي لَهَا أَنْ تُدْرِكَ الْقَمَرَ وَلَا اللَّيْلُ سَابِقُ النَّهَارِ وَكُلٌّ فِي فَلَكٍ يَسْبَحُونَ',urdu='نہ تو سورج ہی سے ہو سکتا ہے کہ چاند کو جا پکڑے اور نہ رات ہی دن سے پہلے آسکتی ہے اور سب اپنے اپنے دائرے میں تیر رہے ہیں۔',english='The sun is not to overtake the moon, nor is the night to outpace the day. Each floats in an orbit.'),
 dict(reference='سورہ رحمٰن - 33',arabic='يٰمَعْشَرَ الْجِنِّ وَالْإِنْسِ إِنِ اسْتَطَعْتُمْ أَنْ تَنْفُذُوا مِنْ أَقْطَارِ السَّمٰوٰتِ وَالْأَرْضِ فَانْفُذُوا لَا تَنْفُذُونَ إِلَّا بِسُلْطٰنٍ',urdu='اے گروہ جن وانس اگر تمہیں قدرت ہو کہ آسمان اور زمین کے کناروں سے نکل جاؤ تو نکل جاؤ اور زور کے سوا تو تم نکل سکتے ہی نہیں۔',english='O company of Jinn and men, if you can (and want) to cross the limits sky and earth, then cross, you will not cross except by the authority (from Allah).'),
 dict(reference='سورہ ملک - 3',arabic='الَّذِي خَلَقَ سَبْعَ سَمٰوٰتٍ طِبَاقًا مَا تَرٰى فِي خَلْقِ الرَّحْمٰنِ مِنْ تَفٰوُتٍ فَارْجِعِ الْبَصَرَ هَلْ تَرٰى مِنْ فُطُورٍ',urdu='اس نے سات آسمان اوپر تلے بنائے (اے دیکھنے والے) کیا تو (اللہ) رحمٰن کی آفرینش میں کوئی نقص دیکھتا ہے؟ ذرا آنکھ اٹھا کر دیکھ تجھے کو (آسمان میں) کوئی شگاف نظر آتا ہے۔',english='He who created seven heavens in layers. You see no discrepancy in the creation of the compassionate. Look again can you see any fault?')
]
phrases=[dict(arabic='أَفَلَا يَتَفَكَّرُونَ',urdu='بھلا یہ لوگ غور و فکر نہیں کرتے۔',english='Do they not think?'),
 dict(arabic='أَفَلَا يَتَدَبَّرُونَ',urdu='بھلا یہ لوگ غور نہیں کرتے۔',english='Do they not contemplate?'),
 dict(arabic='أَفَلَا يَنْظُرُونَ',urdu='آیا یہ لوگ نہیں دیکھتے۔',english='Do they (people) not look?')]
paras=[item for q in quotes for item in [q['arabic']+' ('+q['reference']+')',q['urdu'],q['english']]]
paras.extend(item for q in phrases for item in [q['arabic'],q['urdu'],q['english']])
paras += ['CONTRIBUTION TO PHYSICAL SCIENCE BY ISLAMIC WORLD',
 'Scientists of the Islamic world contributed in the development of physics. Few of the notable scientists are:',
 'Yaqub Kindi (800 - 873) A.D',
 'He was born in Busra, Iraq. He produced extensive research monographs on metrology, specific gravity and tides. His most important work was done in the field of optics, especially on reflection of light.']
figures=[dict(src=crop(9,'printed004-quran-source.png',(.19,.146,.812,.625)),alt='Original textbook Arabic verses and Urdu and English translations.',caption='Quraan and Physics — original source typography'),
 dict(src=crop(9,'printed004-yaqub-kindi.png',(.623,.668,.816,.854)),alt='Textbook portrait of Yaqub Kindi.',caption='YAQUB KINDI')]
save(dict(pdfPage=9,printedPage=4,status='completed-corrected',chapterNumber=1,chapter='Unit 1: Physical Quantities and Measurement',
 title='Quraan and Physics / Contribution to Physical Science by Islamic World',
 sections=[dict(code='1.1',heading='1.1 Introduction to Physics',paras=paras,figures=figures,blocks=[dict(type='sourceQuotation',**quote) for quote in quotes]+[dict(type='sourcePhrase',**phrase) for phrase in phrases])],
 comparison='Repaired interleaved multilingual quotations and surah reference, preserved original printed typography in source crop and retained scientist portrait'))
render(10)
