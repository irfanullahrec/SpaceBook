"""Coded SVG figures for Class 12 Computer Science (flat fills; labels per language)."""


def _txt(x, y, s, size=14, anchor='middle', weight='normal', fill='#1e293b'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{fill}" font-family="sans-serif">{s}</text>'


def os_interface(users, apps, os_, hw, user_n, cap):
    """Figure 1.1: Operating System as an interface (users / application programs / OS / hardware)."""
    box = lambda x, y, w, h, s: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#fff7e6" stroke="#e0a83a" stroke-width="2"/>' + _txt(x + w / 2, y + h / 2 + 5, s)
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 330" role="img" aria-label="' + cap + '">',
           '<rect width="460" height="330" fill="#ffffff"/>',
           '<rect x="20" y="10" width="420" height="270" rx="26" fill="#fffdf6" stroke="#f0c040" stroke-width="3"/>',
           box(45, 30, 90, 36, f'{users} 1'), box(150, 30, 90, 36, f'{users} 2'), _txt(275, 54, '- - -', 16), box(310, 30, 110, 36, user_n)]
    for x in (90, 195, 365):
        out.append(f'<line x1="{x}" y1="66" x2="{x}" y2="96" stroke="#94a3b8" stroke-width="2"/>')
    out += [box(60, 96, 340, 44, apps), '<line x1="230" y1="140" x2="230" y2="160" stroke="#94a3b8" stroke-width="2"/>',
            box(60, 160, 340, 44, os_), '<line x1="230" y1="204" x2="230" y2="224" stroke="#94a3b8" stroke-width="2"/>',
            box(60, 224, 340, 44, hw), _txt(230, 312, cap, 14, fill='#475569'), '</svg>']
    return ''.join(out)


def fig_1_1():
    return (os_interface('User', 'Application Programs', 'Operating System', 'Hardwares', 'User n', 'Figure 1.1: Operating System as an Interface'),
            os_interface('صارف', 'ایپلیکیشن پروگرامز', 'آپریٹنگ سسٹم', 'ہارڈویئر', 'صارف n', 'شکل 1.1: آپریٹنگ سسٹم بطور انٹرفیس'),
            os_interface('کاروونکی', 'کاريال پروګرامونه', 'عملیاتي سیسټم', 'هارډویر', 'کاروونکی n', '۱.۱ شکل: عملیاتي سیسټم د منځګړي په توګه'))


def _cap(cap, y):
    return _txt(240, y, cap, 13, fill='#475569')


def win7_desktop(labels, cap):
    """Figure 1.3: Windows 7 desktop mock-up with the printed callouts (icons, task bar, start button, system tray)."""
    icons, taskbar, start, tray, pinned, title = labels
    note = lambda x, y, w, s: f'<rect x="{x}" y="{y}" width="{w}" height="22" fill="#ffffff" stroke="#1e293b"/>' + _txt(x + w / 2, y + 15, s, 10)
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 300" role="img" aria-label="' + cap + '">'
            '<rect width="480" height="300" fill="#ffffff"/><rect x="20" y="10" width="440" height="250" fill="#1f5fae"/>'
            '<rect x="20" y="236" width="440" height="24" fill="#16365f"/><circle cx="36" cy="248" r="9" fill="#5fb0ff"/>'
            '<rect x="420" y="240" width="36" height="16" fill="#26507f"/>'
            '<rect x="200" y="90" width="38" height="38" fill="#f25022"/><rect x="242" y="90" width="38" height="38" fill="#7fba00"/>'
            '<rect x="200" y="132" width="38" height="38" fill="#00a4ef"/><rect x="242" y="132" width="38" height="38" fill="#ffb900"/>'
            '<rect x="30" y="28" width="22" height="22" fill="#d9e6f5"/><rect x="30" y="58" width="22" height="22" fill="#d9e6f5"/>'
            + note(180, 14, 140, title) + note(80, 40, 130, icons) + '<line x1="80" y1="51" x2="56" y2="51" stroke="#e11d48" stroke-width="3"/>'
            + note(120, 205, 230, taskbar) + note(330, 170, 120, tray) + '<line x1="438" y1="192" x2="438" y2="238" stroke="#e11d48" stroke-width="3"/>'
            + note(28, 205, 85, start) + note(70, 264, 220, pinned) + _cap(cap, 296) + '</svg>')


def fig_1_3():
    return (win7_desktop(('Desktop Icons and Shortcuts', 'The entire item below the orange line is the “Task Bar”', 'Start Button', 'System Tray', 'Items “Pinned” to the task bar replace “Quick Launch”', 'Default Windows 7 Desktop'), 'Figure 1.3: Windows 7 Desktop'),
            win7_desktop(('ڈیسک ٹاپ آئیکنز اور شارٹ کٹس', 'نارنجی لکیر کے نیچے پورا حصہ ’’ٹاسک بار‘‘ ہے', 'اسٹارٹ بٹن', 'سسٹم ٹرے', 'ٹاسک بار پر ’’پِن‘‘ کیے گئے آئٹمز ’’کوئیک لانچ‘‘ کی جگہ لیتے ہیں', 'ونڈوز 7 کا معیاری ڈیسک ٹاپ'), 'شکل 1.3: ونڈوز 7 ڈیسک ٹاپ'),
            win7_desktop(('د ډیسکټاپ نښې او لنډلارې', 'د نارنجي کرښې لاندې ټوله برخه "ټاسک بار" ده', 'د پیل تڼۍ', 'د سیسټم پتنوس', 'پر ټاسک بار "پن" شوي توکي د "Quick Launch" ځای نیسي', 'د وینډوز ۷ معیاري ډیسکټاپ'), '۱.۳ شکل: د وینډوز ۷ ډیسکټاپ'))


def unix_prompt(cap):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 170" role="img" aria-label="' + cap + '">'
            '<rect width="480" height="170" fill="#ffffff"/><rect x="20" y="10" width="440" height="130" fill="#ffffff" stroke="#64748b" stroke-width="2"/>'
            '<rect x="20" y="10" width="440" height="24" fill="#6b7a8f"/>' + _txt(240, 27, 'penguin01', 13, weight='bold', fill='#ffffff')
            + '<rect x="400" y="14" width="16" height="16" fill="#cbd5e1"/><rect x="420" y="14" width="16" height="16" fill="#cbd5e1"/><rect x="440" y="14" width="16" height="16" fill="#ef4444"/>'
            + _txt(32, 54, '%', 14, anchor='start', fill='#0f172a') + _cap(cap, 160) + '</svg>')


def fig_1_4():
    return (unix_prompt('Figure 1.4 UNIX Prompt'), unix_prompt('شکل 1.4 یونکس پرامپٹ'), unix_prompt('۱.۴ شکل: د UNIX پرامپټ'))


def mac_desktop(labels, cap):
    menu, about, dock = labels
    folders = ''.join(f'<rect x="{x}" y="{y}" width="26" height="20" fill="#cfe0f5" stroke="#64748b"/>' for x in (360, 395, 430) for y in (70, 110, 150))
    dock_items = ''.join(f'<rect x="{x}" y="232" width="24" height="24" rx="4" fill="{c}"/>' for x, c in zip(range(120, 380, 32), ['#60a5fa', '#334155', '#f59e0b', '#38bdf8', '#e2e8f0', '#94a3b8', '#fbbf24', '#cbd5e1']))
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 290" role="img" aria-label="' + cap + '">'
            '<rect width="480" height="290" fill="#ffffff"/><rect x="20" y="10" width="440" height="255" fill="#7da0c9"/>'
            '<rect x="20" y="10" width="440" height="16" fill="#eef2f7"/>' + _txt(30, 22, menu, 10, anchor='start')
            + '<rect x="40" y="40" width="150" height="80" fill="#f1f5f9" stroke="#64748b"/>' + _txt(115, 85, about, 12)
            + '<rect x="60" y="130" width="200" height="90" fill="#1e3a5f" stroke="#64748b"/>' + _txt(160, 150, 'CNN.com top stories', 11, fill='#ffffff')
            + '<rect x="350" y="55" width="110" height="130" fill="#e8eef6" stroke="#64748b"/>' + folders
            + '<rect x="100" y="228" width="280" height="32" rx="8" fill="#dbe4ef" opacity="0.9"/>' + dock_items
            + _txt(240, 278, dock, 10, fill='#1e293b') + _cap(cap, 288) + '</svg>')


def fig_1_7():
    return (mac_desktop(('File  Edit  View  Go  Special  Help', 'About This Computer — Mac OS', 'Dock'), 'Figure 1.7: Mac OS Desktop'),
            mac_desktop(('فائل  ایڈٹ  ویو  گو  اسپیشل  ہیلپ', 'اس کمپیوٹر کے بارے میں — Mac OS', 'ڈاک'), 'شکل 1.7: میک او ایس ڈیسک ٹاپ'),
            mac_desktop(('فایل  سمون  لید  تګ  ځانګړی  مرسته', 'د دې کمپیوټر په اړه — Mac OS', 'ډاک'), '۱.۷ شکل: د Mac OS ډیسکټاپ'))


def stack(title, cells, cap, w=200, cell_h=34, first_h=48):
    """Vertical memory stack (e.g. Figure 1.6): title above, cells top to bottom, caption below."""
    x0 = 240 - w / 2
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 {H}" role="img" aria-label="' + cap + '">', '<rect width="480" height="{H}" fill="#ffffff"/>']
    y = 10
    for line in title:
        out.append(_txt(240, y + 14, line, 14, weight='bold')); y += 18
    y += 4
    for i, c in enumerate(cells):
        h = first_h if i == 0 and '\n' in c else cell_h
        out.append(f'<rect x="{x0}" y="{y}" width="{w}" height="{h}" fill="#ffffff" stroke="#334155" stroke-width="2"/>')
        parts = c.split('\n')
        for j, s in enumerate(parts):
            out.append(_txt(240, y + h / 2 + 5 + (j - (len(parts) - 1) / 2) * 16, s, 13, weight='bold'))
        y += h
    out.append(_txt(240, y + 26, cap, 13, weight='bold', fill='#1e3a8a'))
    out.append('</svg>')
    H = int(y + 40)
    return ''.join(out).replace('{H}', str(H)), H


def fig_1_6():
    en, h = stack(['Main Memory', '(RAM)'], ['Operating System\n(Kernel)', 'Job 3', 'Job 2', 'Job 1', 'Job 0'], 'Figure 1.6 Main Memory Partitioning in Multiprogramming')
    ur, _ = stack(['مین میموری', '(RAM)'], ['آپریٹنگ سسٹم\n(کرنل)', 'جاب 3', 'جاب 2', 'جاب 1', 'جاب 0'], 'شکل 1.6 ملٹی پروگرامنگ میں مین میموری کی تقسیم')
    ps, _ = stack(['اصلي حافظه', '(RAM)'], ['عملیاتي سیسټم\n(کرنل)', 'دنده ۳', 'دنده ۲', 'دنده ۱', 'دنده ۰'], '۱.۶ شکل: په څو-پروګرامي کار کې د اصلي حافظې وېش')
    return en, ur, ps, 480 / h


def tree(nodes, edges, labels, cap, W=520, H=330, notes=()):
    """Generic node-link diagram. nodes: {id: (x, y, w)}; edges: [(a, b)]; labels: {id: text}; notes: [(x, y, text)]."""
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{cap}">', f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
    for a, b in edges:
        (x1, y1, _), (x2, y2, _) = nodes[a], nodes[b]
        out.append(f'<line x1="{x1}" y1="{y1 + 13}" x2="{x2}" y2="{y2 - 13}" stroke="#475569" stroke-width="1.5"/>')
    for k, (x, y, w) in nodes.items():
        out.append(f'<rect x="{x - w / 2}" y="{y - 13}" width="{w}" height="26" rx="13" fill="#fde9c4" stroke="#d9a441"/>')
        out.append(_txt(x, y + 4, labels[k], 11))
    for x, y, s in notes:
        out.append(_txt(x, y, s, 11, fill='#334155'))
    out.append(_txt(W / 2, H - 8, cap, 13, fill='#475569'))
    out.append('</svg>')
    return ''.join(out)


def fig_1_8():
    nodes = {'root': (260, 50, 70), 'app': (130, 120, 100), 'doc': (390, 120, 100), 'games': (50, 200, 80), 'spread': (150, 200, 100),
             'pres': (255, 200, 100), 'cvs': (360, 200, 70), 'trans': (460, 200, 90), 'cv': (330, 270, 90), 'pr': (430, 270, 90)}
    edges = [('root', 'app'), ('root', 'doc'), ('app', 'games'), ('app', 'spread'), ('doc', 'pres'), ('doc', 'cvs'), ('doc', 'trans'), ('cvs', 'cv'), ('cvs', 'pr')]
    def lab(t): return dict(zip(['root', 'app', 'doc', 'games', 'spread', 'pres', 'cvs', 'trans', 'cv', 'pr'], t))
    en = tree(nodes, edges, lab(['C:\\', 'Applications', 'Documents', 'Games', 'Spreadsheets', 'Presentations', 'CVs', 'Transcripts', 'Curriculum Vitea', 'Person Request']),
              'Figure 1.8: Hierarchical File System', notes=[(260, 22, 'Root Directory'), (260, 115, 'Sub Directories'), (255, 172, 'Sub Directories'), (380, 302, 'Files')])
    ur = tree(nodes, edges, lab(['C:\\', 'ایپلیکیشنز', 'دستاویزات', 'گیمز', 'اسپریڈ شیٹس', 'پریزنٹیشنز', 'سی ویز', 'ٹرانسکرپٹس', 'Curriculum Vitea', 'Person Request']),
              'شکل 1.8: درجہ وار فائل سسٹم', notes=[(260, 22, 'روٹ ڈائریکٹری'), (260, 115, 'ذیلی ڈائریکٹریز'), (255, 172, 'ذیلی ڈائریکٹریز'), (380, 302, 'فائلیں')])
    ps = tree(nodes, edges, lab(['C:\\', 'کاريالونه', 'اسناد', 'لوبې', 'سپرېډشیټونه', 'پرېزنټېشنونه', 'CVs', 'ټرانسکریپټونه', 'Curriculum Vitea', 'Person Request']),
              '۱.۸ شکل: درجه‌ییز فایل سیسټم', notes=[(260, 22, 'ریښه لارښود'), (260, 115, 'فرعي لارښودونه'), (255, 172, 'فرعي لارښودونه'), (380, 302, 'فایلونه')])
    return en, ur, ps, 520 / 330


def layers(top_boxes, rows, cap, W=460):
    """Users row over stacked layer boxes (Figure 1.9 style)."""
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {{H}}" role="img" aria-label="{cap}">', f'<rect width="{W}" height="{{H}}" fill="#ffffff"/>']
    xs = [110, 210, 330]
    for x, s in zip(xs, top_boxes):
        out.append(f'<rect x="{x - 45}" y="14" width="90" height="34" fill="#ffffff" stroke="#f08a24" stroke-width="3"/>' + _txt(x, 37, s, 14, weight='bold'))
        out.append(f'<line x1="{x}" y1="48" x2="{x}" y2="70" stroke="#1e293b" stroke-width="2"/>')
    out.append(_txt(272, 36, '- -', 14, weight='bold'))
    y = 70
    for i, s in enumerate(rows):
        h = 50 if i == 2 else 40
        out.append(f'<rect x="80" y="{y}" width="300" height="{h}" fill="#ffffff" stroke="#1d4ed8" stroke-width="2"/>' + _txt(230, y + h / 2 + 5, s, 14, weight='bold'))
        y += h
        if i < len(rows) - 1:
            if i == 2:
                out.append(f'<rect x="200" y="{y}" width="60" height="22" fill="#f08a24"/>')
            else:
                out.append(f'<line x1="230" y1="{y}" x2="230" y2="{y + 22}" stroke="#1e293b" stroke-width="2"/>')
            y += 22
    out.append(_txt(W / 2, y + 26, cap, 13, weight='bold', fill='#1e3a8a') + '</svg>')
    H = int(y + 40)
    return ''.join(out).replace('{H}', str(H)), H


def fig_1_9():
    en, h = layers(['User 1', 'User 2', 'User n'], ['Application Programs', 'Operating System', 'Drivers', 'Hardwares'], 'Figure 1.9 Device Drivers and Operating System')
    ur, _ = layers(['صارف 1', 'صارف 2', 'صارف n'], ['ایپلیکیشن پروگرامز', 'آپریٹنگ سسٹم', 'ڈرائیورز', 'ہارڈویئر'], 'شکل 1.9 ڈیوائس ڈرائیورز اور آپریٹنگ سسٹم')
    ps, _ = layers(['کاروونکی ۱', 'کاروونکی ۲', 'کاروونکی n'], ['کاريال پروګرامونه', 'عملیاتي سیسټم', 'چلوونکي (Drivers)', 'هارډویر'], '۱.۹ شکل: د وسایلو چلوونکي او عملیاتي سیسټم')
    return en, ur, ps, 460 / h


def state_model(L, cap):
    """Figure 1.10 five-state process model. L: dict of labels."""
    node = lambda x, y, s: f'<ellipse cx="{x}" cy="{y}" rx="44" ry="24" fill="#cfe5f7" stroke="#5a8fc2"/>' + _txt(x, y + 5, s, 12, weight='bold')
    arr = '<marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1e293b"/></marker>'
    line = lambda x1, y1, x2, y2: f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#1e293b" stroke-width="2" marker-end="url(#a)"/>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 300" role="img" aria-label="{cap}"><defs>{arr}</defs><rect width="520" height="300" fill="#ffffff"/>'
            + node(55, 60, L['new']) + node(190, 60, L['ready']) + node(330, 60, L['run']) + node(465, 60, L['exit']) + node(190, 225, L['blocked'])
            + line(99, 60, 144, 60) + _txt(122, 50, L['admit'], 11)
            + line(234, 52, 286, 52) + _txt(260, 42, L['dispatch'], 11)
            + line(286, 70, 234, 70) + _txt(260, 88, L['timeout'], 11)
            + line(374, 60, 419, 60) + _txt(396, 50, L['release'], 11)
            + line(315, 82, 205, 202) + _txt(285, 150, L['wait'], 11)
            + line(190, 201, 190, 86) + _txt(152, 150, L['occurs'], 11)
            + _txt(260, 290, cap, 13, weight='bold', fill='#1e3a8a') + '</svg>')


def fig_1_10():
    en = state_model(dict(new='New', ready='Ready', run='Running', exit='Exit', blocked='Blocked', admit='Admit', dispatch='Dispatch', timeout='Timeout', release='Release', wait='Event Wait', occurs='Event Occurs'), 'Figure 1.10: Five-State Process Model')
    ur = state_model(dict(new='نیا', ready='تیار', run='چل رہا', exit='اختتام', blocked='بلاک', admit='داخلہ', dispatch='روانگی', timeout='وقت ختم', release='رہائی', wait='واقعے کا انتظار', occurs='واقعہ پیش آیا'), 'شکل 1.10: پانچ حالتوں والا پراسیس ماڈل')
    ps = state_model(dict(new='نوی', ready='چمتو', run='روان', exit='وتل', blocked='بند', admit='منل', dispatch='لېږل', timeout='وخت پای', release='خوشې کول', wait='د پېښې انتظار', occurs='پېښه وشوه'), '۱.۱۰ شکل: د پنځو حالتونو د پروسې ماډل')
    return en, ur, ps, 520 / 300


def waterfall(labels, cap):
    """Figure 2.1 cascading SDLC phases with feedback arrows to a left bus."""
    cols = ['#f4f1c9', '#f4f1c9', '#e6d3ef', '#e6d3ef', '#dbe7f3', '#dbe7f3', '#f7d4dc', '#f7d4dc', '#ffffff']
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 470" role="img" aria-label="{cap}">',
           '<defs><marker id="w" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1e293b"/></marker></defs>',
           '<rect width="520" height="470" fill="#ffffff"/>']
    bus = 40
    for i, s in enumerate(labels):
        x, y = 70 + i * 44, 20 + i * 46
        w = 110
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="5" fill="{cols[i]}" stroke="#94a3b8"/>' + _txt(x + w / 2, y + 21, s, 11, weight='bold'))
        if i < len(labels) - 1:
            out.append(f'<polyline points="{x + w},{y + 10} {x + w + 22},{y + 10} {x + w + 22},{y + 46}" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#w)"/>')
        if i > 0:
            out.append(f'<line x1="{x}" y1="{y + 16}" x2="{bus + 2}" y2="{y + 16}" stroke="#1e293b" stroke-width="1.5" marker-end="url(#w)"/>')
    last_y = 20 + (len(labels) - 1) * 46 + 32
    out.append(f'<polyline points="{70 + (len(labels) - 1) * 44 + 55},{last_y} {70 + (len(labels) - 1) * 44 + 55},{last_y + 18} {bus},{last_y + 18} {bus},{36}" fill="none" stroke="#1e293b" stroke-width="1.5"/>')
    out.append(f'<line x1="{bus}" y1="36" x2="68" y2="36" stroke="#1e293b" stroke-width="1.5" marker-end="url(#w)"/>')
    out.append(_txt(260, 462, cap, 13, weight='bold', fill='#1e293b') + '</svg>')
    return ''.join(out)


def fig_2_1():
    return (waterfall(['Planning', 'Feasibility', 'Analysis', 'Requirement Eng.', 'Design', 'Coding', 'Testing', 'Deployment', 'Maintenance'], 'Figure 2.1: Phases of System Development Life Cycle'),
            waterfall(['منصوبہ بندی', 'فیزیبلٹی', 'تجزیہ', 'ریکوائرمنٹ انجینئرنگ', 'ڈیزائن', 'کوڈنگ', 'جانچ', 'تعیناتی', 'دیکھ بھال'], 'شکل 2.1: سسٹم ڈویلپمنٹ لائف سائیکل کے مراحل'),
            waterfall(['پلان جوړونه', 'عملي وړتیا', 'تحلیل', 'د اړتیاوو انجنیري', 'ډیزاین', 'کوډ لیکنه', 'ازموینه', 'ځای پر ځای کول', 'ساتنه'], '۲.۱ شکل: د سیسټم د پراختیا د ژوند دورې پړاوونه'), 520 / 470)


ARROW = '<marker id="fa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1e293b"/></marker>'


def fc_shape(kind, cx, cy, w, h, label, size=12):
    """Flowchart shapes: terminal / io / process / decision (centered at cx, cy)."""
    s = 'fill="#ffffff" stroke="#1e293b" stroke-width="2"'
    if kind == 'terminal':
        g = f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="{h / 2}" {s}/>'
    elif kind == 'io':
        k = 18
        g = f'<polygon points="{cx - w / 2 + k},{cy - h / 2} {cx + w / 2},{cy - h / 2} {cx + w / 2 - k},{cy + h / 2} {cx - w / 2},{cy + h / 2}" {s}/>'
    elif kind == 'decision':
        g = f'<polygon points="{cx},{cy - h / 2} {cx + w / 2},{cy} {cx},{cy + h / 2} {cx - w / 2},{cy}" {s}/>'
    else:
        g = f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" {s}/>'
    lines = label.split('\n')
    for i, ln in enumerate(lines):
        g += _txt(cx, cy + 5 + (i - (len(lines) - 1) / 2) * 15, ln, size, weight='bold')
    return g


def fc_arrow(x1, y1, x2, y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#1e293b" stroke-width="2" marker-end="url(#fa)"/>'


def flow_linear(steps, cap, W=360):
    """Vertical flowchart: steps = [(kind, label)]."""
    y, out = 30, []
    for i, (k, lab) in enumerate(steps):
        h = 46 if '\n' in lab else 36
        out.append(fc_shape(k, W / 2, y + h / 2, 200 if k != 'terminal' else 120, h, lab))
        if i < len(steps) - 1:
            out.append(fc_arrow(W / 2, y + h, W / 2, y + h + 22))
        y += h + 22
    H = y + 20
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{cap}"><defs>{ARROW}</defs><rect width="{W}" height="{H}" fill="#ffffff"/>'
            + ''.join(out) + _txt(W / 2, H - 8, cap, 13, weight='bold', fill='#1e3a8a') + '</svg>'), H


def symbols_table(rows, head, cap):
    """Figure 2.2 flowchart symbols: rows of (name, kind, use)."""
    W, rh = 560, 62
    H = 40 + rh * len(rows) + 30
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{cap}"><defs>{ARROW}</defs><rect width="{W}" height="{H}" fill="#ffffff"/>',
           f'<rect x="10" y="8" width="{W - 20}" height="{rh * len(rows) + 30}" fill="#ffffff" stroke="#e11d48" stroke-width="1.5"/>',
           _txt(60, 28, head[0], 12, weight='bold'), _txt(170, 28, head[1], 12, weight='bold'), _txt(260, 28, head[2], 12, anchor='start', weight='bold')]
    fills = {'terminal': '#2f6fd1', 'io': '#f2a3c6', 'process': '#a5e3dc', 'decision': '#8fa2e8'}
    for i, (name, kind, use) in enumerate(rows):
        cy = 40 + rh * i + rh / 2
        out.append(_txt(60, cy + 5, name, 12))
        if kind == 'line':
            out.append(f'<line x1="120" y1="{cy}" x2="220" y2="{cy}" stroke="#1e293b" stroke-width="2" marker-end="url(#fa)"/>')
        else:
            g = fc_shape(kind, 170, cy, 100, 40, '')
            out.append(g.replace('fill="#ffffff"', f'fill="{fills[kind]}"', 1))
        parts = use.split('\n')
        for j, p in enumerate(parts):
            out.append(_txt(250, cy + 5 + (j - (len(parts) - 1) / 2) * 15, p, 11, anchor='start'))
    out.append(_txt(W / 2, H - 6, cap, 13, weight='bold', fill='#1e3a8a') + '</svg>')
    return ''.join(out), H


def fig_2_2():
    en, h = symbols_table([('Oval', 'terminal', 'Denotes the beginning or end of a program.'), ('Flow line', 'line', 'Denotes the direction of logic flow in a program.'),
                           ('Parallelogram', 'io', 'Denotes either an input operation (e.g. INPUT)\nor an output operation (e.g. PRINT).'), ('Rectangle', 'process', 'Denotes a process to be carried out\n(e.g. an addition).'),
                           ('Diamond', 'decision', 'Denotes a decision (or branch) to be made. The program\nshould continue along one of two routes (e.g. IF/THEN/ELSE).')], ('Name', 'Symbol', 'Use in flowchart'), 'Figure 2.2 Flowchart Symbols')
    ur, _ = symbols_table([('بیضوی', 'terminal', 'پروگرام کے آغاز یا اختتام کو ظاہر کرتا ہے۔'), ('بہاؤ کی لکیر', 'line', 'پروگرام میں منطق کے بہاؤ کی سمت ظاہر کرتی ہے۔'),
                           ('متوازی الاضلاع', 'io', 'ان پٹ عمل (مثلاً INPUT) یا\nآؤٹ پٹ عمل (مثلاً PRINT) ظاہر کرتا ہے۔'), ('مستطیل', 'process', 'انجام دیے جانے والے عمل کو ظاہر کرتا ہے\n(مثلاً جمع)۔'),
                           ('معین', 'decision', 'کیے جانے والے فیصلے (یا شاخ) کو ظاہر کرتا ہے؛ پروگرام\nدو میں سے ایک راستے پر چلتا ہے (مثلاً IF/THEN/ELSE)۔')], ('نام', 'علامت', 'فلو چارٹ میں استعمال'), 'شکل 2.2 فلو چارٹ کی علامات')
    ps, _ = symbols_table([('هګۍ ډوله', 'terminal', 'د پروګرام پیل یا پای ښيي.'), ('د بهیر کرښه', 'line', 'په پروګرام کې د منطق د بهیر لوری ښيي.'),
                           ('متوازي‌الاضلاع', 'io', 'یا د ننوتو عملیه (لکه INPUT) یا\nد وتو عملیه (لکه PRINT) ښيي.'), ('مستطیل', 'process', 'د ترسره کېدونکې عملیې ښودنه\n(لکه جمع).'),
                           ('معین', 'decision', 'د کېدونکې پرېکړې (یا څانګې) ښودنه؛ پروګرام\nله دوو لارو یوه تعقیبوي (لکه IF/THEN/ELSE).')], ('نوم', 'نښه', 'په فلوچارټ کې کارونه'), '۲.۲ شکل: د فلوچارټ نښې')
    return en, ur, ps, 560 / h


def fig_2_3():
    en, h = flow_linear([('terminal', 'START'), ('io', 'READ A,B,C,D,E'), ('process', 'SUM = A+B+C+D+E\nAVERAGE = SUM/5'), ('io', 'PRINT AVERAGE'), ('terminal', 'END')], 'Figure 2.3 Flowchart')
    ur, _ = flow_linear([('terminal', 'START'), ('io', 'READ A,B,C,D,E'), ('process', 'SUM = A+B+C+D+E\nAVERAGE = SUM/5'), ('io', 'PRINT AVERAGE'), ('terminal', 'END')], 'شکل 2.3 فلو چارٹ')
    ps, _ = flow_linear([('terminal', 'START'), ('io', 'READ A,B,C,D,E'), ('process', 'SUM = A+B+C+D+E\nAVERAGE = SUM/5'), ('io', 'PRINT AVERAGE'), ('terminal', 'END')], '۲.۳ شکل: فلوچارټ')
    return en, ur, ps, 360 / h


def _svg(W, H, cap, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{cap}"><defs>{ARROW}</defs>'
            f'<rect width="{W}" height="{H}" fill="#ffffff"/>{body}' + _txt(W / 2, H - 8, cap, 13, fill='#475569') + '</svg>')


def if_flow(L, cap):
    """Flowchart 4.1: if structure. L = (condition, statement, next, T, F)."""
    c, s, n, T, F = L
    b = (fc_arrow(110, 10, 110, 42) + fc_shape('decision', 110, 72, 160, 60, c, 12)
         + fc_arrow(190, 72, 300, 72) + _txt(245, 64, T, 12, weight='bold') + fc_shape('process', 360, 72, 120, 40, s, 12)
         + f'<polyline points="360,92 360,140 116,140" fill="none" stroke="#1e293b" stroke-width="2" marker-end="url(#fa)"/>'
         + fc_arrow(110, 102, 110, 170) + _txt(98, 128, F, 12, weight='bold') + fc_shape('process', 110, 190, 120, 40, n, 12))
    return _svg(440, 245, cap, b)


def fig_4_1():
    return (if_flow(('Condition', 'Statement (s)', 'Next Statement', 'T', 'F'), 'Flowchart 4.1: Working of If Structure'),
            if_flow(('شرط', 'بیان (بیانات)', 'اگلا بیان', 'T', 'F'), 'فلو چارٹ 4.1: if ساخت کا عمل'),
            if_flow(('شرط', 'بیان (بیانونه)', 'راتلونکی بیان', 'T', 'F'), '۴.۱ فلوچارټ: د if جوړښت کار'), 440 / 245)


def ifelse_flow(L, cap):
    """if-else structure: decision with T to one box, F to another, both joining to next statement."""
    c, s1, s2, n, T, F = L
    b = (fc_arrow(220, 8, 220, 34) + fc_shape('decision', 220, 64, 160, 60, c, 12)
         + f'<polyline points="300,64 360,64 360,104" fill="none" stroke="#1e293b" stroke-width="2" marker-end="url(#fa)"/>' + _txt(330, 56, T, 12, weight='bold')
         + f'<polyline points="140,64 80,64 80,104" fill="none" stroke="#1e293b" stroke-width="2" marker-end="url(#fa)"/>' + _txt(110, 56, F, 12, weight='bold')
         + fc_shape('process', 360, 124, 120, 40, s1, 11) + fc_shape('process', 80, 124, 120, 40, s2, 11)
         + f'<polyline points="360,144 360,170 220,170" fill="none" stroke="#1e293b" stroke-width="2"/>'
         + f'<polyline points="80,144 80,170 220,170" fill="none" stroke="#1e293b" stroke-width="2"/>'
         + fc_arrow(220, 170, 220, 194) + fc_shape('process', 220, 214, 130, 40, n, 12))
    return _svg(440, 265, cap, b)


def ifelse2_flow(L, cap):
    """Flowchart 4.2 (book layout): decision; T to right statement box; F down to statement box; both rejoin and exit downward."""
    c, s, T, F = L
    b = (fc_arrow(110, 8, 110, 34) + fc_shape('decision', 110, 64, 160, 60, c, 12)
         + fc_arrow(190, 64, 290, 64) + _txt(240, 56, T, 12, weight='bold') + fc_shape('process', 350, 64, 120, 40, s, 11)
         + fc_arrow(110, 94, 110, 124) + _txt(98, 114, F, 12, weight='bold') + fc_shape('process', 110, 144, 120, 40, s, 11)
         + '<polyline points="350,84 350,200 116,200" fill="none" stroke="#1e293b" stroke-width="2" marker-end="url(#fa)"/>'
         + '<line x1="110" y1="164" x2="110" y2="200" stroke="#1e293b" stroke-width="2"/>' + fc_arrow(110, 200, 110, 228))
    return _svg(440, 260, cap, b)


def fig_4_2():
    return (ifelse2_flow(('Condition', 'Statement (s)', 'T', 'F'), 'Flowchart 4.2: Working of If-else Structure'),
            ifelse2_flow(('شرط', 'بیان (بیانات)', 'T', 'F'), 'فلو چارٹ 4.2: if-else ساخت کا عمل'),
            ifelse2_flow(('شرط', 'بیان (بیانونه)', 'T', 'F'), '۴.۲ فلوچارټ: د if-else جوړښت کار'), 440 / 260)


def switch_flow(L, cap):
    """Flowchart 4.3: chain of case decisions (T → statement box → right bus), F down to next case, last F → Default; bus joins exit."""
    cases, stmt, dflt, T, F = L
    b = fc_arrow(110, 6, 110, 26)
    y = 50
    for i, c in enumerate(cases):
        b += fc_shape('decision', 110, y, 150, 46, c, 12)
        b += fc_arrow(185, y, 290, y) + _txt(238, y - 8, T, 12, weight='bold') + fc_shape('process', 345, y, 110, 34, stmt, 11)
        b += f'<line x1="400" y1="{y}" x2="430" y2="{y}" stroke="#1e293b" stroke-width="2"/>'
        b += fc_arrow(110, y + 23, 110, y + 57) + _txt(98, y + 44, F, 12, weight='bold')
        y += 80
    b += fc_shape('process', 110, y - 4, 110, 34, dflt, 12)
    b += f'<line x1="430" y1="50" x2="430" y2="{y + 34}" stroke="#1e293b" stroke-width="2"/>'
    b += f'<polyline points="430,{y + 34} 110,{y + 34}" fill="none" stroke="#1e293b" stroke-width="2"/>'
    b += f'<line x1="110" y1="{y + 13}" x2="110" y2="{y + 34}" stroke="#1e293b" stroke-width="2"/>' + fc_arrow(110, y + 34, 110, y + 58)
    return _svg(460, y + 90, cap, b), y + 90


def fig_4_3():
    en, h = switch_flow((['Case 1', 'Case 2', 'Case 3', 'Case 4'], 'Statement (s)', 'Default', 'T', 'F'), 'Flowchart 4.3: Working of switch-default Structure')
    ur, _ = switch_flow((['کیس 1', 'کیس 2', 'کیس 3', 'کیس 4'], 'بیان (بیانات)', 'ڈیفالٹ', 'T', 'F'), 'فلو چارٹ 4.3: switch-default ساخت کا عمل')
    ps, _ = switch_flow((['حالت ۱', 'حالت ۲', 'حالت ۳', 'حالت ۴'], 'بیان (بیانونه)', 'ډیفالټ', 'T', 'F'), '۴.۳ فلوچارټ: د switch-default جوړښت کار')
    return en, ur, ps, 460 / h


def for_flow(L, cap):
    """Flowchart 4.4: Initialization → Condition (T → Loop Body → Increment/Decrement → back above condition; F exits down)."""
    ini, cond, body, inc, T, F = L
    b = (fc_arrow(150, 6, 150, 24) + fc_shape('process', 150, 44, 130, 38, ini, 12)
         + fc_arrow(150, 63, 150, 196) + fc_shape('decision', 150, 222, 160, 52, cond, 12)
         + fc_arrow(230, 222, 320, 222) + _txt(275, 214, T, 12, weight='bold') + fc_shape('process', 375, 222, 110, 36, body, 12)
         + fc_arrow(375, 204, 375, 168) + fc_shape('process', 375, 148, 120, 40, inc, 11)
         + '<polyline points="375,128 375,100 156,100" fill="none" stroke="#1e293b" stroke-width="2" marker-end="url(#fa)"/>'
         + fc_arrow(150, 248, 150, 284) + _txt(138, 270, F, 12, weight='bold'))
    return _svg(460, 315, cap, b)


def fig_4_4():
    return (for_flow(('Initialization', 'Condition', 'Loop Body', 'Increment/\nDecrement', 'T', 'F'), 'Flowchart 4.4: Working of for Loop'),
            for_flow(('ابتدائی قدر', 'شرط', 'لوپ کا جسم', 'اضافہ/\nکمی', 'T', 'F'), 'فلو چارٹ 4.4: for لوپ کا عمل'),
            for_flow(('لومړنی ارزښت', 'شرط', 'د حلقې بدنه', 'زیاتول/\nکمول', 'T', 'F'), '۴.۴ فلوچارټ: د for حلقې کار'), 460 / 315)


def while_flow(L, cap):
    """Flowchart 4.5: Condition (T → Loop Body → back to top; F exits down)."""
    cond, body, T, F = L
    b = (fc_arrow(120, 6, 120, 76) + fc_shape('decision', 120, 104, 160, 52, cond, 12)
         + fc_arrow(200, 104, 290, 104) + _txt(245, 96, T, 12, weight='bold') + fc_shape('process', 345, 104, 110, 36, body, 12)
         + '<polyline points="345,86 345,40 126,40" fill="none" stroke="#1e293b" stroke-width="2" marker-end="url(#fa)"/>'
         + fc_arrow(120, 130, 120, 170) + _txt(108, 156, F, 12, weight='bold'))
    return _svg(440, 200, cap, b)


def fig_4_5():
    return (while_flow(('Condition', 'Loop Body', 'T', 'F'), 'Flowchart 4.5: Working of while Loop'),
            while_flow(('شرط', 'لوپ کا جسم', 'T', 'F'), 'فلو چارٹ 4.5: while لوپ کا عمل'),
            while_flow(('شرط', 'د حلقې بدنه', 'T', 'F'), '۴.۵ فلوچارټ: د while حلقې کار'), 440 / 200)


def dowhile_flow(L, cap):
    """Flowchart 4.6: Loop Body then Condition (T back to body; F exits down)."""
    body, cond, T, F = L
    b = (fc_arrow(160, 6, 160, 30) + fc_shape('process', 160, 50, 120, 36, body, 12)
         + fc_arrow(160, 68, 160, 104) + fc_shape('decision', 160, 132, 160, 52, cond, 12)
         + '<polyline points="240,132 320,132 320,50 226,50" fill="none" stroke="#1e293b" stroke-width="2" marker-end="url(#fa)"/>' + _txt(285, 124, T, 12, weight='bold')
         + fc_arrow(160, 158, 160, 196) + _txt(148, 182, F, 12, weight='bold'))
    return _svg(400, 225, cap, b)


def fig_4_6():
    return (dowhile_flow(('Loop Body', 'Condition', 'T', 'F'), 'Flowchart 4.6: Working of do-while Loop'),
            dowhile_flow(('لوپ کا جسم', 'شرط', 'T', 'F'), 'فلو چارٹ 4.6: do-while لوپ کا عمل'),
            dowhile_flow(('د حلقې بدنه', 'شرط', 'T', 'F'), '۴.۶ فلوچارټ: د do-while حلقې کار'), 400 / 225)


def array_1d(name, idx, vals, addrs, cap, notes=None, cw=56):
    """Unit 5 one-dimensional array: indices above, cells, addresses below; notes=(indices, data items, memory address) callouts."""
    n = len(idx)
    x0 = 70
    W = x0 + n * cw + (120 if notes else 30)
    H = 150 if addrs else 120
    b = _txt(x0 - 14, 72, name, 15, anchor='end')
    for i in range(n):
        x = x0 + i * cw
        b += _txt(x + cw / 2, 44, idx[i], 13) + f'<rect x="{x}" y="52" width="{cw}" height="30" fill="#f8fafc" stroke="#1e293b" stroke-width="1.5"/>'
        if vals:
            b += _txt(x + cw / 2, 72, vals[i], 13)
        if addrs:
            b += _txt(x + cw / 2, 102, addrs[i], 12)
    if notes:
        xr = x0 + n * cw
        tag = lambda y, s: f'<rect x="{xr + 16}" y="{y - 13}" width="96" height="20" fill="#ffffff" stroke="#e11d48"/>' + _txt(xr + 64, y + 2, s, 10, weight='bold')
        b += tag(40, notes[0]) + tag(72, notes[1])
        b += f'<rect x="4" y="88" width="60" height="22" fill="#ffffff" stroke="#e11d48"/>' + _txt(34, 103, notes[2], 9, weight='bold')
    return _svg(W, H, cap, b), W / H



def array_2d(rows, cap, cw=60, ch=30):
    """Unit 5 two-dimensional array: column indices on top, row indices at left, values in a grid."""
    nr, nc = len(rows), len(rows[0])
    x0, y0 = 50, 40
    W, H = x0 + nc * cw + 30, y0 + nr * ch + 40
    b = ''
    for j in range(nc):
        b += _txt(x0 + j * cw + cw / 2, y0 - 10, str(j), 13)
    for i, r in enumerate(rows):
        b += _txt(x0 - 16, y0 + i * ch + ch / 2 + 5, str(i), 13)
        for j, v in enumerate(r):
            b += f'<rect x="{x0 + j * cw}" y="{y0 + i * ch}" width="{cw}" height="{ch}" fill="#f8fafc" stroke="#1e293b" stroke-width="1.5"/>' + _txt(x0 + j * cw + cw / 2, y0 + i * ch + ch / 2 + 5, v, 13)
    return _svg(W, H, cap, b), W / H


def pointer_box(cap):
    """Figure 7.1: fPointer box (1000) with arrow to x box (5.5) stored at address 1000."""
    b = (_txt(110, 30, 'fPointer', 14, weight='bold') + '<rect x="30" y="40" width="160" height="44" rx="6" fill="#f8fafc" stroke="#1e293b" stroke-width="1.5"/>' + _txt(110, 68, '1000', 14, weight='bold')
         + fc_arrow(190, 62, 318, 62)
         + _txt(400, 30, 'x', 14, weight='bold') + '<rect x="320" y="40" width="160" height="44" rx="6" fill="#f8fafc" stroke="#1e293b" stroke-width="1.5"/>' + _txt(400, 68, '5.5', 14, weight='bold')
         + _txt(400, 108, '1000', 13, weight='bold'))
    return _svg(510, 140, cap, b)


def fig_7_1():
    return (pointer_box('Figure 7.1: Use of the Pointer Variable'), pointer_box('شکل 7.1: پوائنٹر ویری ایبل کا استعمال'), pointer_box('۷.۱ شکل: د پوائنټر متغیر کارونه'), 510 / 140)


def class_diagram(W, H, nodes, edges, notes, cap):
    """Unit 8 inheritance sketches. nodes: {key: (cx, cy, w, h, label, kind)} kind in box/dashed/triangle;
    edges: (from_key, to_key) drawn as an arrow from the bottom/top edge of one node to the other; notes: (x, y, text, anchor)."""
    b = ''
    for cx, cy, w, h, label, kind in nodes.values():
        if kind == 'triangle':
            b += f'<polygon points="{cx},{cy - h / 2} {cx + w / 2},{cy + h / 2} {cx - w / 2},{cy + h / 2}" fill="#fbfde8" stroke="#a3b62a" stroke-width="3"/>' + _txt(cx, cy + h / 4 + 5, label, 15, weight='bold')
        else:
            dash = ' stroke-dasharray="4 3"' if kind == 'dashed' else ''
            b += f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="5" fill="#fbfde8" stroke="#a3b62a" stroke-width="3"{dash}/>' + _txt(cx, cy + 6, label, 15, weight='bold')
    for a, z in edges:
        ax, ay, aw, ah = nodes[a][:4]
        zx, zy, zw, zh = nodes[z][:4]
        y1 = ay - ah / 2 if zy < ay else ay + ah / 2
        y2 = zy + zh / 2 if zy < ay else zy - zh / 2
        b += fc_arrow(ax, y1, zx, y2 + (6 if zy < ay else -6))
    for x, y, s, anc in notes:
        b += _txt(x, y, s, 12, anchor=anc, weight='bold')
    return _svg(W, H, cap, b)


def _fruit(L, cap):
    return class_diagram(460, 250, {'f': (230, 40, 150, 40, L[0], 'box'), 'b': (150, 170, 110, 40, L[1], 'box'), 'a': (310, 170, 110, 40, L[2], 'box')},
                         [('b', 'f'), ('a', 'f')], [(320, 45, L[3], 'start'), (380, 175, L[4], 'start')], cap)


def fig_8_2a():
    return (_fruit(('FRUIT', 'Banana', 'Apple', 'Base class', 'Child classes'), 'Figure 8.2: Inheritance of Fruit Class'),
            _fruit(('پھل', 'کیلا', 'سیب', 'بیس کلاس', 'چائلڈ کلاسز'), 'شکل 8.2: پھل کلاس کی وراثت'),
            _fruit(('مېوه', 'کېله', 'مڼه', 'اساسي ټولګی', 'ماشوم ټولګي'), '۸.۲ شکل: د مېوې ټولګي میراث'), 460 / 250)


def _shape(L, cap):
    return class_diagram(460, 330, {'s': (180, 40, 120, 40, L[0], 'dashed'), 'r': (110, 150, 130, 44, L[1], 'box'), 't': (270, 150, 160, 80, L[2], 'triangle'),
                                    'q': (110, 260, 90, 44, L[3], 'box')},
                         [('s', 'r'), ('s', 't'), ('q', 'r')], [(270, 45, L[4], 'start'), (360, 125, L[5], 'start')], cap)


def fig_8_2b():
    return (_shape(('Shape', 'Rectangle', 'Triangle', 'Square', 'Base class', 'Derived class'), 'Figure 8.2: Inheritance of Shape Class'),
            _shape(('شکل', 'مستطیل', 'مثلث', 'مربع', 'بیس کلاس', 'ڈیرائیوڈ کلاس'), 'شکل 8.2: شیپ کلاس کی وراثت'),
            _shape(('بڼه', 'مستطیل', 'مثلث', 'مربع', 'اساسي ټولګی', 'مشتق ټولګی'), '۸.۲ شکل: د بڼې ټولګي میراث'), 460 / 330)


def _patient(L, cap):
    return class_diagram(520, 250, {'p': (260, 40, 140, 40, L[0], 'box'), 'i': (200, 170, 110, 40, L[1], 'box'), 'o': (340, 170, 110, 40, L[2], 'box')},
                         [('i', 'p'), ('o', 'p')], [(340, 32, L[3], 'start'), (340, 52, L[4], 'start'), (140, 175, L[5], 'end'), (400, 175, L[6], 'start')], cap)


def fig_8_3():
    return (_patient(('Patient', 'Indoor', 'Outdoor', 'Name, Father name, Age', 'Address, Disease', 'Ward No, Bed No.', 'Next date of visit'), 'Figure 8.3: Inheritance of Patient Class'),
            _patient(('مریض', 'اِن ڈور', 'آؤٹ ڈور', 'نام، والد کا نام، عمر', 'پتہ، بیماری', 'وارڈ نمبر، بیڈ نمبر', 'اگلی ملاقات کی تاریخ'), 'شکل 8.3: مریض کلاس کی وراثت'),
            _patient(('ناروغ', 'داخلي', 'بهرنی', 'نوم، د پلار نوم، عمر', 'پته، ناروغي', 'د وارډ شمېره، د بستر شمېره', 'د راتلونکې کتنې نېټه'), '۸.۳ شکل: د ناروغ ټولګي میراث'), 520 / 250)


def _multi(L, cap):
    return class_diagram(420, 250, {'a': (120, 40, 120, 40, L[0], 'box'), 'b': (300, 40, 120, 40, L[1], 'box'), 'c': (210, 170, 120, 40, L[2], 'box')},
                         [('c', 'a'), ('c', 'b')], [], cap)


def fig_8_4():
    return (_multi(('class A', 'class B', 'class c'), 'Figure 8.4: Multiple Inheritance'),
            _multi(('class A', 'class B', 'class c'), 'شکل 8.4: متعدد وراثت'),
            _multi(('class A', 'class B', 'class c'), '۸.۴ شکل: څو ګونی میراث'), 420 / 250)


def text_window(title, lines, cap, dark=False, W=460, rows=None):
    """Unit 9 Notepad / console window mock-up: title bar, optional menu bar, monospace content lines."""
    n = rows or max(len(lines), 3)
    top = 52 if not dark else 32
    H = top + n * 18 + 50
    bg, fg = ('#111111', '#e5e5e5') if dark else ('#ffffff', '#111111')
    b = (f'<rect x="10" y="8" width="{W - 20}" height="{H - 36}" fill="#f1f5f9" stroke="#475569" stroke-width="1.5"/>'
         f'<rect x="10" y="8" width="{W - 20}" height="20" fill="#3b5998"/>' + _txt(18, 23, title, 11, anchor='start', weight='bold', fill='#ffffff')
         + ''.join(f'<rect x="{W - 66 + i * 18}" y="11" width="14" height="14" fill="{c}"/>' for i, c in enumerate(('#cbd5e1', '#cbd5e1', '#ef4444'))))
    if not dark:
        b += ''.join(_txt(20 + i * 42, 43, m, 11, anchor='start') for i, m in enumerate(('File', 'Edit', 'Format', 'View', 'Help')))
    b += f'<rect x="14" y="{top - 4}" width="{W - 28}" height="{n * 18 + 8}" fill="{bg}" stroke="#94a3b8"/>'
    for i, s in enumerate(lines):
        b += f'<text x="20" y="{top + 12 + i * 18}" font-size="12" font-family="Consolas, monospace" fill="{fg}" xml:space="preserve">{s}</text>'
    return _svg(W, H, cap, b), W / H
