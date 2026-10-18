"""Coded SVG maps for Pakistan Studies XII (schematic outlines; labels per language)."""
from html import escape as e

# Simplified subcontinent outlines in a 600x520 frame (north up).
PAK = 'M120,150 L170,95 L215,70 L250,85 L262,120 L245,150 L232,175 L215,205 L195,240 L178,262 L150,270 L120,262 L95,245 L60,240 L40,215 L55,180 L90,170 Z'
KASH = 'M250,85 L290,62 L330,75 L345,100 L325,128 L290,132 L262,120 Z'
INDIA = ('M262,120 L290,132 L325,128 L345,140 L380,170 L430,182 L470,170 L520,150 L560,160 L555,200 L520,215 L505,240 '
         'L480,232 L470,255 L440,270 L420,300 L380,345 L345,400 L320,450 L300,470 L285,430 L265,370 L245,320 L215,290 '
         'L190,285 L178,262 L195,240 L215,205 L232,175 L245,150 Z')
NEPAL = 'M330,150 L395,168 L430,182 L425,192 L380,185 L340,170 Z'
BHUTAN = 'M455,180 L478,176 L480,188 L458,190 Z'
BANG = 'M440,205 L470,200 L482,215 L478,250 L465,262 L450,250 L440,225 Z'
LANKA = 'M325,470 L338,478 L340,500 L328,505 L320,490 Z'
HYD = (310, 300, 46, 36)
JUNA = (222, 296, 24, 16)

L = {
 'en': dict(title='Areas that went to India', pak='Pakistan', ind='Bharat (India)', kash='Jammu & Kashmir (disputed area)',
            nepal='Nepal', bhutan='Bhutan', bang='Bangladesh', lanka='Sri Lanka', bal='Balochistan', sindh='Sindh', pun='Punjab',
            kpk='Khyber Pakhtunkhwa', na='Northern Areas', ara='Arabian Sea', bay='Bay of Bengal', hyd='Hyderabad State',
            juna='Junagadh & Manavadar', lah='Lahore', kar='Karachi', que='Quetta', pes='Peshawar', dli='Delhi',
            mur='Murshidabad', cal='Calcutta', gur='Gurdaspur', bat='Batala', pat='Pathankot', amr='Amritsar', fer='Ferozepur', faz='Fazilka',
            key='Key', k1='Areas occupied by India by force', k2='Areas handed to India at partition', k3='Disputed area', k4='City',
            n='N', s='S', ea='E', w='W', scale='Scale (schematic)'),
 'ur': dict(title='وہ علاقے جو ہندوستان کے پاس چلے گئے', pak='پاکستان', ind='بھارت', kash='جموں کشمیر (متنازعہ علاقہ)',
            nepal='نیپال', bhutan='بھوٹان', bang='بنگلہ دیش', lanka='سری لنکا', bal='بلوچستان', sindh='سندھ', pun='پنجاب',
            kpk='خیبر پختونخوا', na='شمالی علاقہ جات', ara='بحیرۂ عرب', bay='خلیج بنگال', hyd='ریاست حیدر آباد',
            juna='جونا گڑھ و مناوادر', lah='لاہور', kar='کراچی', que='کوئٹہ', pes='پشاور', dli='دہلی',
            mur='مرشد آباد', cal='کلکتہ', gur='گورداسپور', bat='بٹالہ', pat='پٹھان کوٹ', amr='امرتسر', fer='فیروز پور', faz='فاضلکا',
            key='علامات', k1='وہ علاقے جن پر ہندوستان نے زبردستی قبضہ کیا', k2='تقسیم کے وقت جو علاقے ہندوستان کے حوالے کیے گئے', k3='متنازعہ علاقے', k4='شہر',
            n='شمال', s='جنوب', ea='مشرق', w='مغرب', scale='سکیل (خاکہ)'),
 'ps': dict(title='هغه سیمې چې هندوستان ته ولاړې', pak='پاکستان', ind='بهارت', kash='جمون کشمیر (شخړه‌ییزه سیمه)',
            nepal='نېپال', bhutan='بوتان', bang='بنګله‌دېش', lanka='سریلانکا', bal='بلوچستان', sindh='سند', pun='پنجاب',
            kpk='خیبر پښتونخوا', na='شمالي سیمې', ara='عربي سمندر', bay='د بنګال خلیج', hyd='د حیدراباد ریاست',
            juna='جوناګړ او مناوادر', lah='لاهور', kar='کراچۍ', que='کوټه', pes='پېښور', dli='ډهلي',
            mur='مرشدآباد', cal='کلکته', gur='ګورداسپور', bat='بټاله', pat='پټهانکوټ', amr='امرتسر', fer='فیروزپور', faz='فاضلکا',
            key='نښې', k1='هغه سیمې چې هندوستان په زور ونیولې', k2='د وېش پر وخت هندوستان ته سپارل شوې سیمې', k3='شخړه‌ییزې سیمې', k4='ښار',
            n='شمال', s='سویل', ea='ختیځ', w='لوېدیځ', scale='پیمانه (خاکه)'),
}


def partition_map(lang):
    t = L[lang]; rtl = lang != 'en'
    anc = 'end' if rtl else 'start'
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 560" role="img" aria-label="{e(t["title"])}" '
         f'font-family="Noto Naskh Arabic, Segoe UI, sans-serif">',
         '<rect x="0" y="0" width="600" height="560" fill="#bfe3f5"/>',
         f'<path d="{INDIA}" fill="#fbf8e6" stroke="#555" stroke-width="1.2"/>',
         f'<path d="{PAK}" fill="#d8ecb5" stroke="#555" stroke-width="1.2"/>',
         f'<path d="{KASH}" fill="#e66fa4" stroke="#555" stroke-width="1.2"/>',
         ''.join(f'<path d="{p}" fill="#d9418f" stroke="#555" stroke-width="1"/>' for p in (NEPAL, BHUTAN, BANG, LANKA))]
    for (x, y, w, h) in (HYD, JUNA):
        o.append(f'<g fill="#f7b9b9" stroke="#c0392b" stroke-width=".8"><rect x="{x}" y="{y}" width="{w}" height="{h}"/>')
        for i in range(1, 4):
            o.append(f'<line x1="{x + w * i / 4}" y1="{y}" x2="{x + w * i / 4}" y2="{y + h}"/><line x1="{x}" y1="{y + h * i / 4}" x2="{x + w}" y2="{y + h * i / 4}"/>')
        o.append('</g>')
    lab = lambda x, y, s, size=12, w='normal', fill='#222': o.append(
        f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="middle">{e(s)}</text>')
    lab(150, 205, t['pak'], 18, 'bold'); lab(340, 250, t['ind'], 20, 'bold'); lab(300, 104, t['kash'], 9, 'bold')
    lab(380, 175, t['nepal'], 10); lab(468, 172, t['bhutan'], 9); lab(462, 232, t['bang'], 9); lab(330, 520, t['lanka'], 10)
    lab(80, 220, t['bal'], 11); lab(135, 250, t['sindh'], 11); lab(165, 150, t['pun'], 11); lab(160, 120, t['kpk'], 9); lab(232, 66, t['na'], 9)
    lab(130, 360, t['ara'], 18, 'bold', '#1b4f72'); lab(500, 370, t['bay'], 18, 'bold', '#1b4f72')
    lab(333, 292, t['hyd'], 10); lab(234, 326, t['juna'], 9)
    cities = [(205, 140, 'lah', 'sq'), (128, 265, 'kar', 'sq'), (98, 185, 'que', 'sq'), (192, 110, 'pes', 'sq'), (285, 205, 'dli', 'sq'),
              (440, 195, 'mur', 'dot'), (440, 245, 'cal', 'dot'), (232, 125, 'gur', 'dot'), (238, 132, 'bat', 'dot'), (240, 118, 'pat', 'dot'),
              (228, 140, 'amr', 'dot'), (222, 152, 'fer', 'dot'), (212, 162, 'faz', 'dot')]
    for x, y, k, kind in cities:
        if kind == 'sq':
            o.append(f'<rect x="{x - 4}" y="{y - 4}" width="8" height="8" fill="#fff" stroke="#333"/>')
        else:
            o.append(f'<circle cx="{x}" cy="{y}" r="4" fill="#c0392b" stroke="#fff" stroke-width=".8"/>')
        dx = -7 if k in ('mur', 'cal', 'lah') else 7
        o.append(f'<text x="{x + dx}" y="{y + 4}" font-size="9" fill="#222" text-anchor="{"end" if dx < 0 else "start"}">{e(t[k])}</text>')
    o.append('<text x="300" y="88" font-size="14" text-anchor="middle" fill="#222">✚</text>')
    # compass
    o.append('<g transform="translate(40,40)"><circle r="20" fill="#c0392b" opacity=".85"/><path d="M0,-18 L4,0 L0,18 L-4,0 Z M-18,0 L0,4 L18,0 L0,-4 Z" fill="#fff"/>'
             f'<text y="-24" font-size="9" text-anchor="middle">{e(t["n"])}</text><text y="33" font-size="9" text-anchor="middle">{e(t["s"])}</text>'
             f'<text x="26" y="3" font-size="9">{e(t["ea"])}</text><text x="-26" y="3" font-size="9" text-anchor="end">{e(t["w"])}</text></g>')
    # title box
    o.append(f'<rect x="330" y="14" width="258" height="30" fill="#fff" stroke="#c0392b" stroke-dasharray="5 3"/>'
             f'<text x="459" y="34" font-size="14" font-weight="bold" text-anchor="middle" fill="#c0392b">{e(t["title"])}</text>')
    # legend
    lx = 10
    o.append(f'<rect x="{lx}" y="430" width="260" height="120" fill="#fff" stroke="#333"/>'
             f'<text x="{lx + 130}" y="448" font-size="13" font-weight="bold" text-anchor="middle">{e(t["key"])}</text>')
    items = [('grid', t['k1']), ('dot', t['k2']), ('plus', t['k3']), ('sq', t['k4'])]
    for i, (kind, s) in enumerate(items):
        y = 468 + i * 20
        sx = lx + 236 if rtl else lx + 12
        if kind == 'grid':
            o.append(f'<rect x="{sx}" y="{y - 9}" width="12" height="12" fill="#f7b9b9" stroke="#c0392b"/>')
        elif kind == 'dot':
            o.append(f'<circle cx="{sx + 6}" cy="{y - 3}" r="5" fill="#c0392b"/>')
        elif kind == 'plus':
            o.append(f'<text x="{sx + 6}" y="{y + 2}" font-size="13" text-anchor="middle">✚</text>')
        else:
            o.append(f'<rect x="{sx}" y="{y - 9}" width="11" height="11" fill="#fff" stroke="#333"/>')
        tx = lx + 228 if rtl else lx + 32
        o.append(f'<text x="{tx}" y="{y + 1}" font-size="10" text-anchor="{anc}">{e(s)}</text>')
    o.append(f'<text x="470" y="545" font-size="9">{e(t["scale"])}</text><line x1="470" y1="530" x2="570" y2="530" stroke="#333" stroke-width="2"/>'
             '<text x="470" y="526" font-size="8">0</text><text x="515" y="526" font-size="8">250</text><text x="550" y="526" font-size="8">500 km</text>')
    o.append('</svg>')
    return ''.join(o)


# ---- Muslim world tile map (p.47) ----
MW_CAT = [('#b9cf6a', '75–100', '۷۵–۱۰۰'), ('#e2658f', '50–80', '۵۰–۸۰'), ('#f2d33c', '15–50', '۱۵–۵۰'), ('#f6ead0', '5–10', '۵–۱۰')]
MW = [  # (region en/ur/ps, [(country en, ur, ps, cat)])
 (('North & West Africa', 'شمالی و مغربی افریقہ', 'شمالي او لوېدیځه افریقا'),
  [('Morocco', 'مراکش', 'مراکش', 0), ('Algeria', 'الجزائر', 'الجزایر', 0), ('Tunisia', 'تیونس', 'تونس', 0), ('Libya', 'لیبیا', 'لیبیا', 0),
   ('Egypt', 'مصر', 'مصر', 0), ('Mauritania', 'موریطانیہ', 'موریتانیا', 0), ('Mali', 'مالی', 'مالي', 0), ('Niger', 'نائجر', 'نایجر', 0),
   ('Senegal', 'سینیگال', 'سنګال', 0), ('Chad', 'چاڈ', 'چاډ', 1), ('Nigeria', 'نائجیریا', 'نایجیریا', 1), ('Guinea', 'گنی', 'ګینه', 1)]),
 (('East Africa', 'مشرقی افریقہ', 'ختیځه افریقا'),
  [('Sudan', 'سوڈان', 'سوډان', 0), ('Somalia', 'صومالیہ', 'سومالیا', 0), ('Djibouti', 'جبوتی', 'جیبوتي', 0), ('Ethiopia', 'ایتھوپیا', 'ایتوپیا', 2),
   ('Eritrea', 'اریٹیریا', 'اریتریا', 1), ('Tanzania', 'تنزانیہ', 'تنزانیا', 2), ('Kenya', 'کینیا', 'کینیا', 3)]),
 (('Middle East', 'مشرقِ وسطیٰ', 'منځنی ختیځ'),
  [('Saudi Arabia', 'سعودی عرب', 'سعودي عربستان', 0), ('Yemen', 'یمن', 'یمن', 0), ('Oman', 'عمان', 'عمان', 0), ('U.A.E.', 'متحدہ عرب امارات', 'متحده عربي امارات', 0),
   ('Kuwait', 'کویت', 'کویت', 0), ('Iraq', 'عراق', 'عراق', 0), ('Syria', 'شام', 'سوریه', 0), ('Jordan', 'اردن', 'اردن', 0),
   ('Lebanon', 'لبنان', 'لبنان', 1), ('Turkey', 'ترکی', 'ترکیه', 0), ('Iran', 'ایران', 'ایران', 0)]),
 (('Central & South Asia', 'وسطی و جنوبی ایشیا', 'منځنۍ او سویلي اسیا'),
  [('Pakistan', 'پاکستان', 'پاکستان', 0), ('Afghanistan', 'افغانستان', 'افغانستان', 0), ('Bangladesh', 'بنگلہ دیش', 'بنګله‌دېش', 0),
   ('Uzbekistan', 'ازبکستان', 'ازبکستان', 0), ('Turkmenistan', 'ترکمانستان', 'ترکمنستان', 0), ('Tajikistan', 'تاجکستان', 'تاجکستان', 0),
   ('Kyrgyzstan', 'کرغزستان', 'قرغزستان', 0), ('Kazakhstan', 'قازقستان', 'قزاقستان', 1), ('Azerbaijan', 'آذربائیجان', 'اذربایجان', 0),
   ('India', 'بھارت', 'بهارت', 2), ('Maldives', 'مالدیپ', 'مالدیپ', 0)]),
 (('South-East Asia', 'جنوب مشرقی ایشیا', 'سویل ختیځه اسیا'),
  [('Indonesia', 'انڈونیشیا', 'اندونیزیا', 0), ('Malaysia', 'ملائیشیا', 'مالیزیا', 1), ('Brunei', 'برونائی', 'برونای', 1), ('Philippines', 'فلپائن', 'فلیپین', 3)]),
]
MW_L = {'en': ('The Muslim World', 'Countries in which {} per cent are Muslims', 'schematic tile map (not to scale)'),
        'ur': ('مسلم دُنیا', 'ممالک جن میں {} فیصد مسلمان ہیں', 'خاکہ نما نقشہ (پیمانے کے بغیر)'),
        'ps': ('اسلامي نړۍ', 'هغه هېوادونه چې {} سلنه مسلمانان لري', 'خاکه‌ییز نقشه (بې پیمانې)')}


def muslim_world(lang):
    i = {'en': 0, 'ur': 1, 'ps': 2}[lang]; rtl = lang != 'en'; T = MW_L[lang]
    W, cw, ch = 760, 140, 30
    rows = max(len(c) for _, c in MW)
    H = 120 + rows * (ch + 6) + 70
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{e(T[0])}" font-family="Noto Naskh Arabic, Segoe UI, sans-serif">',
         f'<rect width="{W}" height="{H}" fill="#cfe9f7"/>',
         f'<text x="{W/2}" y="30" font-size="20" font-weight="bold" text-anchor="middle" fill="#8e1b3a">{e(T[0])}</text>']
    order = list(range(len(MW)))
    if rtl: order = order[::-1]  # Africa on the left in both — keep geographic west→east
    order = list(range(len(MW)))
    for col, k in enumerate(order):
        (reg, ctys) = MW[k]
        x = 15 + col * (cw + 10)
        o.append(f'<text x="{x + cw/2}" y="62" font-size="12" font-weight="bold" text-anchor="middle">{e(reg[i])}</text>')
        for r, c in enumerate(ctys):
            y = 74 + r * (ch + 6)
            o.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="4" fill="{MW_CAT[c[3]][0]}" stroke="#555" stroke-width=".8"/>'
                     f'<text x="{x + cw/2}" y="{y + 20}" font-size="12" text-anchor="middle">{e(c[i])}</text>')
    for k, (col, en, ur) in enumerate(MW_CAT):
        x = 15 + (k % 2) * 370; ly = H - 62 + (k // 2) * 22
        rng = en if lang == 'en' else ur
        o.append(f'<rect x="{x}" y="{ly}" width="18" height="14" fill="{col}" stroke="#555"/>'
                 f'<text x="{x + 24}" y="{ly + 12}" font-size="10">{e(T[1].format(rng))}</text>')
    o.append(f'<text x="{W - 10}" y="{H - 6}" font-size="9" text-anchor="end" fill="#555">{e(T[2])}</text></svg>')
    return ''.join(o)


# ---- Physical map of Pakistan (p.51) — schematic ----
PK = ('M330,40 L380,30 L430,60 L470,70 L500,110 L480,140 L455,150 L430,175 L420,210 L400,240 L390,280 L375,320 '
      'L360,360 L330,400 L310,430 L285,455 L250,470 L215,460 L175,455 L130,450 L80,445 L50,420 L60,380 L90,350 '
      'L120,330 L140,300 L175,290 L210,275 L240,250 L260,215 L290,180 L300,140 L310,100 Z')
PHYS = {
 'en': dict(title='Physical map of Pakistan', china='China', afg='Afghanistan', iran='Iran', ind='Bharat (India)',
            hk='Hindu Kush', ks='Koh-e-Safed', kw='Waziristan hills', kth='Thal desert', pp='Pir Panjal', him='Himalaya',
            kara='Karakoram', jam='Vale of Jammu', siw='Siwalik', pot='Potohar Plateau', uip='Upper Indus Plain', chol='Cholistan desert',
            kir='Kirthar range', thar='Thar desert', lip='Lower Indus Plain', delta='Indus delta', makran='Makran hills', kharan='Kharan desert',
            bal='Balochistan Plateau', sul='Koh-e-Sulaiman', disp='Indian illegally occupied Jammu & Kashmir (disputed territory – final status to be decided in line with relevant UNSC resolutions)',
            fu='Frontier undefined', n='North', km='km', inset='Insets: Junagadh & Manavadar; Sir Creek'),
 'ur': dict(title='پاکستان کا طبعی نقشہ', china='چین', afg='افغانستان', iran='ایران', ind='بھارت',
            hk='کوہِ ہندوکش', ks='کوہِ سفید', kw='کوہِ وزیرستان', kth='صحرائے تھل', pp='پیر پنجال', him='کوہِ ہمالیہ',
            kara='کوہِ قراقرم', jam='وادیٔ جموں', siw='کوہِ شوالک', pot='سطحِ مرتفع پوٹھوہار', uip='دریائے سندھ کا بالائی میدان', chol='صحرائے چولستان',
            kir='کوہِ کیرتھر', thar='صحرائے تھر', lip='دریائے سندھ کا زیریں میدان', delta='سندھ کا ڈیلٹا', makran='مکران کی پہاڑیاں', kharan='صحرائے خاران',
            bal='سطحِ مرتفع بلوچستان', sul='کوہِ سلیمان', disp='Indian illegally occupied Jammu & Kashmir (disputed territory – final status to be decided in line with relevant UNSC resolutions)',
            fu='Frontier undefined', n='شمال', km='کلومیٹر', inset='ذیلی نقشے: جونا گڑھ و مناوادر؛ سر کریک'),
 'ps': dict(title='د پاکستان طبیعي نقشه', china='چین', afg='افغانستان', iran='ایران', ind='بهارت',
            hk='هندوکش', ks='سپین غر', kw='د وزیرستان غرونه', kth='د تهل دښته', pp='پیر پنجال', him='همالیا',
            kara='قراقرم', jam='د جمون دره', siw='شوالک', pot='د پوټوهار لوړه سطحه', uip='د سند پورتنی هوار', chol='د چولستان دښته',
            kir='کیرتهر غر', thar='د تهر دښته', lip='د سند لاندینی هوار', delta='د سند ډیلټا', makran='د مکران غونډۍ', kharan='د خاران دښته',
            bal='د بلوچستان لوړه سطحه', sul='سلیمان غر', disp='Indian illegally occupied Jammu & Kashmir (disputed territory – final status to be decided in line with relevant UNSC resolutions)',
            fu='Frontier undefined', n='شمال', km='کیلومتره', inset='فرعي نقشې: جوناګړ او مناوادر؛ سر کریک'),
}


def physical_map(lang):
    t = PHYS[lang]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 520" role="img" aria-label="{e(t["title"])}" font-family="Noto Naskh Arabic, Segoe UI, sans-serif">',
         '<defs><linearGradient id="relief" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a0f1e"/><stop offset=".35" stop-color="#a0525a"/>'
         '<stop offset=".6" stop-color="#e8d7a0"/><stop offset="1" stop-color="#f3e7a2"/></linearGradient></defs>',
         '<rect width="560" height="520" fill="#fff"/>',
         f'<path d="{PK}" fill="#f1e3a3" stroke="#333" stroke-width="1.5"/>',
         '<path d="M330,40 L380,30 L430,60 L470,70 L500,110 L480,140 L455,150 L430,175 L405,170 L380,140 L350,130 L320,150 L300,200 L280,260 L250,300 L210,330 L190,360 L180,400 L170,455 L130,450 L80,445 L50,420 L60,380 L90,350 L120,330 L140,300 L175,290 L210,275 L240,250 L260,215 L290,180 L300,140 L310,100 Z" fill="#a0525a"/>',
         '<path d="M330,40 L380,30 L430,60 L470,70 L500,110 L480,140 L455,150 L440,140 L420,110 L380,90 L345,85 L320,110 L310,100 Z" fill="#5a0f1e"/>',
         '<path d="M405,170 L430,175 L420,210 L395,230 L370,215 Z" fill="#d6b48a"/>',
         f'<text x="20" y="40" font-size="20" font-weight="bold" fill="#8e1b3a">{e(t["title"])}</text>']
    lab = lambda x, y, s, size=10, fill='#111', w='normal': o.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="middle">{e(s)}</text>')
    lab(470, 40, t['china'], 13, w='bold'); lab(230, 210, t['afg'], 13, w='bold'); lab(40, 380, t['iran'], 13, w='bold'); lab(460, 330, t['ind'], 13, w='bold')
    pts = [(330, 55, 'hk'), (300, 120, 'ks'), (270, 150, 'kw'), (340, 150, 'kth'), (430, 95, 'pp'), (445, 80, 'him'), (400, 50, 'kara'),
           (470, 160, 'jam'), (420, 190, 'siw'), (400, 220, 'pot'), (380, 270, 'uip'), (400, 340, 'chol'), (230, 360, 'kir'),
           (330, 380, 'thar'), (300, 430, 'lip'), (280, 470, 'delta'), (130, 470, 'makran'), (110, 360, 'kharan'), (170, 320, 'bal'), (280, 250, 'sul')]
    for x, y, k in pts:
        o.append(f'<circle cx="{x}" cy="{y}" r="2.5" fill="#1565c0"/>')
        o.append(f'<text x="{x}" y="{y - 5}" font-size="9" text-anchor="middle" fill="#0d2a4a" stroke="#fff" stroke-width="2.5" paint-order="stroke">{e(t[k])}</text>')
    o.append(f'<rect x="300" y="470" width="250" height="40" fill="#fff" stroke="#900"/>'
             f'<text x="425" y="484" font-size="7" text-anchor="middle" fill="#900">{e(t["disp"][:62])}</text>'
             f'<text x="425" y="496" font-size="7" text-anchor="middle" fill="#900">{e(t["disp"][62:])}</text>')
    o.append(f'<text x="540" y="150" font-size="8" fill="#333" transform="rotate(90 540 150)">{e(t["fu"])}</text>')
    o.append(f'<path d="M530,55 L536,40 L542,55 Z" fill="#333"/><text x="536" y="70" font-size="10" text-anchor="middle">{e(t["n"])}</text>')
    o.append('<g transform="translate(20,80)"><rect width="200" height="6" fill="#fff" stroke="#333"/><rect width="40" height="6" fill="#333"/><rect x="80" width="40" height="6" fill="#333"/><rect x="160" width="40" height="6" fill="#333"/>'
             f'<text y="-4" font-size="8">0</text><text x="40" y="-4" font-size="8">150</text><text x="80" y="-4" font-size="8">300</text><text x="120" y="-4" font-size="8">450</text><text x="160" y="-4" font-size="8">600</text><text x="200" y="16" font-size="8" text-anchor="end">{e(t["km"])}</text></g>')
    o.append(f'<text x="20" y="510" font-size="9" fill="#555">{e(t["inset"])}</text></svg>')
    return ''.join(o)


# ---- Climatic regions map (p.53) — schematic ----
CLIM = [  # (colour, en, ur, ps, polygon)
 ('#5a0f1e', 'Highland region', 'بلند پہاڑی خطہ', 'لوړه غرنۍ سیمه', 'M330,40 L380,30 L430,60 L470,70 L500,110 L470,120 L430,100 L380,80 L340,90 Z'),
 ('#6a3d9a', 'Humid mountain region', 'مرطوب پہاڑی خطہ', 'لانده غرنۍ سیمه', 'M340,90 L380,80 L430,100 L470,120 L480,140 L455,150 L420,140 L380,125 L330,120 Z'),
 ('#e8957c', 'Semi-arid mountain region', 'نیم خشک پہاڑی خطہ', 'نیمه وچه غرنۍ سیمه', 'M310,100 L330,120 L380,125 L360,170 L320,200 L290,180 L300,140 Z'),
 ('#f5ef8a', 'Humid plain region', 'مرطوب میدانی خطہ', 'لانده هواره سیمه', 'M420,140 L455,150 L430,175 L420,210 L395,200 L400,170 Z'),
 ('#f2c5d6', 'Semi-arid plain region', 'نیم خشک میدانی خطہ', 'نیمه وچه هواره سیمه', 'M360,170 L400,170 L395,200 L420,210 L400,240 L390,280 L340,270 L320,230 Z'),
 ('#f7dfe8', 'Semi-desert region', 'نیم صحرائی خطہ', 'نیمه صحرايي سیمه', 'M290,180 L320,200 L320,230 L340,270 L300,300 L250,300 L240,250 L260,215 Z'),
 ('#e7a08d', 'Desert region', 'صحرائی خطہ', 'صحرايي سیمه', 'M240,250 L250,300 L300,300 L340,270 L390,280 L375,320 L360,360 L330,400 L300,420 L200,420 L120,420 L60,400 L60,380 L90,350 L120,330 L140,300 L175,290 L210,275 Z'),
 ('#6a8fd8', 'Coastal region', 'ساحلی خطہ', 'ساحلي سیمه', 'M60,400 L120,420 L200,420 L300,420 L330,400 L310,430 L285,455 L250,470 L215,460 L175,455 L130,450 L80,445 L50,420 Z'),
]
CL_CITIES = [(370, 60, 'Chitral', 'چترال', 'چترال'), (430, 70, 'Gilgit-Baltistan', 'گلگت بلتستان', 'ګلګت بلتستان'), (440, 95, 'Skardu', 'سکردو', 'سکردو'),
             (300, 135, 'Parachinar', 'پاڑہ چنار', 'پاړه‌چنار'), (340, 125, 'Peshawar', 'پشاور', 'پېښور'), (395, 140, 'Islamabad', 'اسلام آباد', 'اسلام‌اباد'),
             (330, 165, 'Bannu', 'بنوں', 'بنو'), (420, 170, 'Sialkot', 'سیالکوٹ', 'سیالکوټ'), (380, 190, 'Sargodha', 'سرگودھا', 'سرګودها'),
             (425, 200, 'Lahore', 'لاہور', 'لاهور'), (400, 210, 'Faisalabad', 'فیصل آباد', 'فیصل‌اباد'), (410, 235, 'Sahiwal', 'ساہیوال', 'ساهیوال'),
             (330, 205, 'D.I. Khan', 'ڈیرہ اسماعیل خان', 'ډېره اسماعیل خان'), (290, 215, 'Zhob', 'ژوب', 'ژوب'), (370, 260, 'Multan', 'ملتان', 'ملتان'),
             (220, 270, 'Quetta', 'کوئٹہ', 'کوټه'), (200, 300, 'Nushki', 'نوشکی', 'نوشکي'), (270, 300, 'Sibi', 'سبی', 'سیبي'), (230, 320, 'Kalat', 'قلات', 'قلات'),
             (120, 330, 'Nokkundi', 'نوکنڈی', 'نوکنډي'), (230, 350, 'Khuzdar', 'خضدار', 'خضدار'), (300, 345, 'Jacobabad', 'جیکب آباد', 'جېکب‌اباد'),
             (170, 385, 'Panjgur', 'پنجگور', 'پنجګور'), (100, 410, 'Turbat', 'تربت', 'تربت'), (270, 400, 'Hyderabad', 'حیدر آباد', 'حیدراباد'),
             (320, 395, 'Umerkot', 'عمر کوٹ', 'عمرکوټ'), (70, 440, 'Gwadar', 'گوادر', 'ګوادر'), (240, 440, 'Karachi', 'کراچی', 'کراچۍ'), (300, 440, 'Badin', 'بدین', 'بدین')]
CLT = {'en': ('Regions of Pakistan by climate', 'Key', 'Arabian Sea', 'North'), 'ur': ('آب و ہوا کے لحاظ سے پاکستان کے خطے', 'علامات', 'بحیرۂ عرب', 'شمال'),
       'ps': ('د اقلیم له مخې د پاکستان سیمې', 'نښې', 'عربي سمندر', 'شمال')}


def climate_map(lang):
    i = {'en': 0, 'ur': 1, 'ps': 2}[lang]; T = CLT[lang]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 520" role="img" aria-label="{e(T[0])}" font-family="Noto Naskh Arabic, Segoe UI, sans-serif">',
         '<rect width="560" height="520" fill="#fff"/><path d="M0,430 L50,420 L80,445 L130,450 L175,455 L215,460 L250,470 L285,455 L310,430 L330,420 L330,520 L0,520 Z" fill="#bfe3f5"/>',
         f'<text x="20" y="30" font-size="18" font-weight="bold" fill="#8e1b3a">{e(T[0])}</text>']
    o.append(f'<path d="{PK}" fill="#e8957c"/>')
    for col, en, ur, ps, d in CLIM:
        o.append(f'<path d="{d}" fill="{col}" stroke="#fff" stroke-width=".8"/>')
    o.append(f'<path d="{PK}" fill="none" stroke="#333" stroke-width="1.5"/>')
    for x, y, *nm in CL_CITIES:
        o.append(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#111"/><text x="{x + 4}" y="{y + 3}" font-size="8" fill="#111">{e(nm[i])}</text>')
    o.append(f'<text x="120" y="500" font-size="14" font-weight="bold" fill="#1b4f72">{e(T[2])}</text>')
    o.append(f'<rect x="20" y="60" width="150" height="{28 + 20 * len(CLIM)}" fill="#fff" stroke="#c0392b"/><text x="95" y="78" font-size="12" font-weight="bold" text-anchor="middle" fill="#c0392b">{e(T[1])}</text>')
    for k, (col, *nm, d) in enumerate(CLIM):
        y = 92 + k * 20
        o.append(f'<rect x="28" y="{y - 9}" width="16" height="12" fill="{col}" stroke="#555"/><text x="50" y="{y + 1}" font-size="9">{e(nm[i])}</text>')
    o.append(f'<path d="M530,55 L536,40 L542,55 Z" fill="#333"/><text x="536" y="70" font-size="10" text-anchor="middle">{e(T[3])}</text></svg>')
    return ''.join(o)
