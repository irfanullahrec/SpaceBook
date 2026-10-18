"""Restore the Urdu back matter with explicit original-language paragraph pairs."""
import html
from class12_source_review import upsert, section, shared_class_data_lock, sync_companions
from class12_fidelity_repair import stage_reference
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'

def build(page,identity,title,rows,layout,titles,languages):
    # rows=(original, English meaning, Urdu, Pashto); originals stay visible.
    record={'id':identity,'title':title,'kind':'book_back_matter','pdfPage':page,'printedPage':None,'sourcePdf':SOURCE,'paragraphs':[r[0] for r in rows]}
    sec=section(record,[(r[0],r[2],r[3]) for r in rows],layout,titles,'ur')
    for para,row,language in zip(sec['paras'],rows,languages):
        para.update(english=row[1],sourceLanguage=language,originalLanguage=language)
    sec.update(kind='book_back_matter',sourceClass12Physics=True,sourceBlocks=[],sourceLanguage='mixed' if len(set(languages))>1 else languages[0],sourceLanguages=languages,
               sourceOriginalLabel='Original textbook text (English meaning on selection):',sourceUrduLabel='Urdu original / Urdu translation (اصل اردو / اردو ترجمہ):')
    return record,sec

ur200=[
 'مومن تو آپس میں بھائی بھائی ہیں۔ پس اپنے دو بھائیوں میں صلح کرا دیا کرو اور اللہ سے ڈرتے رہو تاکہ تم پر رحمت کی جائے۔',
 '(سورۃ الحجرات: ۱۰)',
 'اے ایمان والو! اُن پاکیزہ چیزوں میں سے کھاؤ جو ہم نے تم کو دی ہیں۔',
 '(سورۃ البقرہ: آیت ۱۷۲)']
en200=[
 'The believers are brothers to one another. So make peace between your two brothers, and fear Allah so that mercy may be shown to you.',
 '(Surah Al-Hujurat:10)',
 'O believers! Eat of the wholesome things that We have given you.',
 '(Surah Al-Baqarah:verse172)']
ps200=[
 'مؤمنان په خپل منځ کې وروڼه دي. نو د خپلو دوو وروڼو ترمنځ سوله وکړئ او له الله ووېرېږئ، څو پر تاسو رحم وشي.',
 '(سورة الحجرات:۱۰)',
 'اې مؤمنانو! له هغو پاکو شیانو وخورئ چې موږ تاسو ته درکړي دي.',
 '(سورة البقره:آیت۱۷۲)']
r200,s200=build(200,'phys12-back-cover-urdu-verses-380','Back-cover Qur’anic quotations',[(u,e,u,p) for u,e,p in zip(ur200,en200,ps200)],[{'type':'quotation','indices':[0,1]},{'type':'quotation','indices':[2,3]}],('سرورق کے آخر میں قرآنی اقتباسات','د شا پوښ قرآني اقتباسونه'),['ur']*4)

ur201=['قومی ترانہ','پاک سرزمین شاد باد','کشورِ حسین شاد باد','تُو نشانِ عزمِ عالی شان','ارضِ پاکستان','مرکزِ یقین شاد باد','پاک سرزمین کا نظام','قوتِ اُخوتِ عوام','قوم ملک سلطنت','پائندہ تابندہ باد','شاد باد منزلِ مُراد','پرچمِ ستارہ و ہلال','رہبرِ ترقّی و کمال','ترجمانِ ماضی شانِ حال','جانِ اِستقبال','سایۂ خدائے ذوالجلال']
en201=['National Anthem','May the sacred land be blessed','May the beautiful country be blessed','You are the symbol of lofty resolve','Land of Pakistan','May the centre of certainty be blessed','The order of the sacred land','The strength of the people’s brotherhood','Nation, country, state','May they endure and shine','May the cherished destination be blessed','Flag of the star and crescent','Guide to progress and perfection','Voice of the past, glory of the present','Spirit of the future','Under the protection of God, the Lord of Majesty']
ps201=['ملي سرود','سپېڅلې خاوره دې اباده وي','ښکلی هېواد دې اباد وي','ته د لوړ عزم نښه یې','د پاکستان خاوره','د یقین مرکز دې اباد وي','د سپېڅلې خاورې نظام','د ولس د ورورولۍ ځواک','ملت، هېواد، دولت','تلپاتې او ځلانده دې وي','د هیلو منزل دې اباد وي','د ستوري او هلال بیرغ','د پرمختګ او کمال لارښود','د تېر وخت ویاند، د اوسني وخت ویاړ','د راتلونکي روح','د لوی او باجلاله خدای تر سیوري لاندې']
rows201=[(u,e,u,p) for u,e,p in zip(ur201,en201,ps201)]
rows201 += [
 ('Leading Books Publishers','Leading Books Publishers','لیڈنگ بکس پبلشرز','لیډنګ بکس خپرندویان'),
 ('Jamrud Road, Peshawar','Jamrud Road, Peshawar','جمروڈ روڈ، پشاور','د جمرود سړک، پېښور'),
 ('Code No. — Quantity — Printed by','Code No. — Quantity — Printed by','کوڈ نمبر — تعداد — مطبع','د کوډ شمېره — شمېر — چاپوونکی'),
 ('PSP/NBP-57-208-2122(O) — 50285 — Naqvi Brothers Printing Press','PSP/NBP-57-208-2122(O) — 50285 — Naqvi Brothers Printing Press','PSP/NBP-57-208-2122(O) — 50285 — نقوی برادرز پرنٹنگ پریس','PSP/NBP-57-208-2122(O) — 50285 — نقوي برادرز چاپخونه')]
layout201=[{'type':'heading','indices':[0]},{'type':'quotation','indices':[1,2,3,4,5]},{'type':'quotation','indices':[6,7,8,9,10]},{'type':'quotation','indices':[11,12,13,14,15]},{'type':'paragraph','indices':[16]},{'type':'paragraph','indices':[17]},{'type':'table','indices':[18,19]}]
r201,s201=build(201,'phys12-back-cover-national-anthem-publisher-201','National anthem and publisher imprint',rows201,layout201,('قومی ترانہ اور اشاعت کی تفصیل','ملي سرود او د چاپ معلومات'),['ur']*16+['en']*4)
s201['sourceTableRows']={18:rows201[18][0].split(' — '),19:rows201[19][0].split(' — ')}

if __name__=='__main__':
    with shared_class_data_lock():
        upsert([r200],[s200],chapter_index=9)
        sync_companions(chapter_index=9,retire_sections=['20.22'],trim_sections=[{'id':'20.23','startsAt':'Code No.','title':'Publisher imprint — pending source-fidelity replacement','clearSciNote':True}])
    stage_reference(200,r200,'Inspected the whole back-quotation page. Restored both Urdu quotations with their separate surah/verse citations, including “پاکیزہ”; sentence punctuation and original Urdu retained. English/Pashto meanings aligned; explicit original-language metadata enables the Urdu source with English meaning on selection. Decorative floral frames and watermark excluded as decoration. Retired OCR20.22 after glossary/profiles/feedback exclusion/quotations were all accounted for.')
    with shared_class_data_lock():
        upsert([r201],[s201],chapter_index=9)
        sync_companions(chapter_index=9,retire_sections=['20.23'])
    stage_reference(201,r201,'Inspected the back cover and250dpi anthem crop. Restored the Urdu title and15 poem lines in three five-line stanzas, with original-language fields and paired English/Pashto meanings (including the spirit of the future line). Kept the two English publisher/address lines and rebuilt the three-column imprint table with code, quantity50285 and printer. English imprint correctly marked English; Urdu/Pashto imprint translations supplied. Decorative building photograph and publisher emblem excluded; no raster embedded. Superseded OCR20.23 retired.')
    print('PDF200 and201 source back matter staged, with original language preserved.')
