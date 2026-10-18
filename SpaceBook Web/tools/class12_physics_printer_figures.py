"""Coded optical and electrostatic printer apparatus; no source raster assets."""
LABELS = {
 'paper':('Paper','کاغذ','کاغذ'), 'lens':('Lens','عدسہ','عدسیه'),
 'image':('Image on drum','ڈرم پر عکس','پر ډرم انځور'),
 'printed':('Printed document','چھپی ہوئی دستاویز','چاپ شوی سند'),
 'laser':('Path of laser','لیزر کا راستہ','د لېزر لاره'),
 'remaining':('Remaining charged region','باقی بار دار حصہ','پاتې چارج لرونکې سیمه'),
 'computer':('Computer, laser, and optics','کمپیوٹر، لیزر اور بصری نظام','کمپیوټر، لېزر او نوري سیستم'),
 'nozzle':('Inkjet nozzle','انک جیٹ نوزل','د اېنک جېټ نوزل'),
 'charging':('Electrostatic charging unit','برقِ سکونی سے بار دینے کا آلہ','د ساکنې برېښنا د چارج کولو واحد'),
 'deflection':('Deflection plates','انحرافی تختیاں','د انحراف تختې'),
 'negative':('Negative plate','منفی تختی','منفي تخته'),
 'positive':('Positive plate','مثبت تختی','مثبته تخته'),
 'uncharged':('Path of uncharged drop','غیر بار دار قطرے کا راستہ','د بې چارج څاڅکي لاره'),
 'charged':('Path of charged drop','بار دار قطرے کا راستہ','د چارج لرونکي څاڅکي لاره'),
 'gutter':('Gutter','نالی','ناوه'),
}
CAPTIONS={
 '11.8':('A positive-charge image of the letter “A” is created on xerographic drum.', 'زیروگرافی کے ڈرم پر حرف “A” کا مثبت بار والا عکس بنتا ہے۔', 'د زېروګرافۍ پر ډرم د “A” توري مثبت چارج لرونکی انځور جوړېږي.'),
 '11.9':('Laser printer with a static laser scanning unit.', 'جامد لیزر اسکیننگ یونٹ والا لیزر پرنٹر۔', 'لېزر چاپګر له ثابت لېزر سکېن کوونکي واحد سره.'),
 '11.10':('Charging of ink droplets between two oppositely charged plates.', 'مخالف بار والی دو تختیوں کے درمیان سیاہی کے قطروں کو بار دار کرنا۔', 'د مخالف چارج لرونکو دوو تختو ترمنځ د رنګ څاڅکي چارج کول.'),
}

def label(key,x,y,lang):
    value=LABELS[key][{'en':0,'ur':1,'ps':2}[lang]]
    return f'<text x="{x}" y="{y}" font-size="15" text-anchor="middle">{value}</text>'

def drum():
    return '<g transform="translate(195 265) rotate(-27)"><path d="M-100-45H95A25 45 0 0 1 95 45H-100Z" fill="#93b4d5" stroke="#475569"/><ellipse cx="-100" cy="0" rx="25" ry="45" fill="#b2c9df" stroke="#475569"/><ellipse cx="95" cy="0" rx="25" ry="45" fill="#91aed0" stroke="#475569"/><path d="M-10 28L10-35 48 28M0 9H36" fill="none" stroke="#ef8354" stroke-width="7"/><circle cx="-15" cy="18" r="2"/><circle cx="50" cy="20" r="2"/><circle cx="61" cy="17" r="2"/><circle cx="62" cy="26" r="2"/></g>'

def copier(lang):
    body='<path d="M130 45L340 45 285 110H75Z" fill="#fff" stroke="#334155" stroke-width="2"/><text x="183" y="94" font-size="65" font-style="italic">A</text>'
    body+='<path d="M150 110L205 110 185 163Z M185 163L160 226 220 226Z" fill="#fef08a"/><path d="M177 160H193" stroke="#334155" stroke-width="3"/>'+drum()
    body+='<path d="M165 350L340 328 293 382 113 395Z" fill="#fff" stroke="#64748b"/><text x="212" y="376" font-size="64" font-style="italic">A</text><path d="M316 367L447 323M318 375L449 331" stroke="#db5c83" stroke-width="9"/><circle cx="316" cy="367" r="5" fill="#fff" stroke="#be185d"/><circle cx="318" cy="375" r="5" fill="#fff" stroke="#be185d"/><path d="M82 264Q78 240 88 233" fill="none" stroke="#334155"/><path d="M87 232L83 242 93 240Z" fill="#334155"/>'
    return body+label('paper',94,82,lang)+label('lens',240,168,lang)+label('image',361,224,lang)+label('printed',235,428,lang)

def laser(lang):
    body=''
    for y in range(110,231,20):
        body+=f'<path d="M367 298L{260-(y-110)*.5} {y}" stroke="#b28b59"/>'
    body+='<g transform="translate(195 208) rotate(-30)"><path d="M-110-43H100A23 43 0 0 1 100 43H-110Z" fill="#fff8ed" stroke="#9a7d63"/><ellipse cx="-110" cy="0" rx="25" ry="43" fill="#fff" stroke="#9a7d63"/>'
    for y in range(-36,38,6):
        body+=f'<path d="M-100 {y}H105" stroke="#886d56"/>'
    body+='<path d="M-5 30L14-31 43 30M4 8H32" stroke="#475569" stroke-dasharray="3 3" stroke-width="3" fill="none"/><path d="M-124 8Q-118 41-97 32" fill="none" stroke="#334155"/><path d="M-95 32L-105 27-103 37Z" fill="#334155"/></g>'
    body+='<path d="M350 291L399 268 459 286 410 309Z" fill="#fef08a"/><path d="M350 291L410 309V375L350 353Z" fill="#fde047"/><path d="M410 309L459 286V353L410 375Z" fill="#facc15"/><path d="M195 101L264 125M120 155L190 194" stroke="#334155"/>'
    return body+label('laser',187,89,lang)+label('remaining',125,141,lang)+label('computer',355,254,lang)

def inkjet(lang):
    body='<path d="M135 48H235Q260 48 260 75V121M135 61H232Q247 61 247 81V121" fill="none" stroke="#334155" stroke-width="3"/><path d="M255 131V472" stroke="#334155" stroke-width="1.5"/><rect x="190" y="147" width="48" height="44" fill="#ef4444"/><rect x="276" y="147" width="48" height="44" fill="#ef4444"/><rect x="198" y="224" width="22" height="180" fill="#ef4444"/><rect x="298" y="224" width="22" height="180" fill="#ef4444"/><path d="M255 194V315Q255 382 300 417" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="4 4"/><path d="M300 417Q305 450 346 450H374M308 417Q313 439 350 439H374" stroke="#334155" stroke-width="2" fill="none"/><rect x="198" y="474" width="135" height="50" fill="#fff" stroke="#334155"/><path d="M164 471H370M178 528H368M215 304H116M312 306H416M219 411H39M303 415H478" stroke="#64748b"/>'
    body+=label('nozzle',375,90,lang)+label('charging',420,166,lang)+label('deflection',422,246,lang)
    body+=label('negative',91,277,lang)+label('positive',412,293,lang)
    body+=label('uncharged',112,400,lang)+label('charged',431,403,lang)+label('gutter',412,453,lang)+label('paper',265,503,lang)
    return body

def figure(number,lang):
    drawing={'11.8':copier,'11.9':laser,'11.10':inkjet}[number](lang)
    caption=CAPTIONS[number][{'en':0,'ur':1,'ps':2}[lang]]
    height=550 if number=='11.10' else 460
    title='phys12-printer-'+number.replace('.','-')+'-'+lang
    return f'<figure><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 {height}" role="img" aria-labelledby="{title}" style="width:100%;max-width:600px;height:auto"><title id="{title}">{caption}</title>{drawing}</svg><figcaption>{"FIGURE" if lang=="en" else "شکل"} {number} — {caption}</figcaption></figure>'
