/* Class 10 Biology, Unit 10 "Gaseous Exchange": source-aligned overlay verified page by page
 * against D:\SpaceBook\Books\10th\10th Bio\PDF\Biology Class 10 kpk book.pdf (printed page = PDF page - 3).
 * Original English text is kept verbatim (including printed spellings); Urdu and Pashto are aligned
 * paragraph translations. Figures are redrawn as inline SVG with the printed labels. */
(function () {
  const chapter = typeof DATA !== 'undefined' && Array.isArray(DATA.bio10Chapters) ? DATA.bio10Chapters.find(ch => ch.num === 10) : null;
  if (!chapter || chapter.__bio10Source) return;
  chapter.__bio10Source = true;
  const PDF = 'Biology Class 10 kpk book.pdf';
  const ref = (pdfPage, printedPage) => ({pdf: PDF, pdfPage, printedPage: String(printedPage)});
  const P = (text, urdu, pashto, extra) => Object.assign({text, urdu, pashto}, extra || {});
  const L = (text, urdu, pashto) => ({text, urdu, pashto});

  
  chapter.name = 'Gaseous Exchange';
  chapter.nameUrdu = 'گیسوں کا تبادلہ';
  chapter.namePashto = 'د ګازونو تبادله';
  chapter.pageRange = 'Pages 1 – 15';

  /* ---------------- Unit opening page (PDF 4, printed 1) ---------------- */
  chapter.sloPairs = [
    P('Differentiate among respiration, gas exchange and breathing.', 'تنفس، گیسوں کے تبادلے اور سانس لینے میں فرق بیان کر سکیں۔', 'د تنفس، د ګازونو تبادلې او ساه اخیستلو ترمنځ توپیر وکړای شي.'),
    P('Describe the process of gaseous exchange in plants by comparing photosynthesis and respiration.', 'ضیائی تالیف اور تنفس کا موازنہ کرتے ہوئے پودوں میں گیسوں کے تبادلے کا عمل بیان کر سکیں۔', 'د فوتوسنتیز او تنفس په پرتله کولو سره په بوټو کې د ګازونو د تبادلې بهیر بیان کړای شي.'),
    P('Describe the role of the parts of the air passageway and of the lungs.', 'ہوا کی گزرگاہ کے حصوں اور پھیپھڑوں کا کردار بیان کر سکیں۔', 'د هوا د لارې د برخو او د سږو رول بیان کړای شي.'),
    P('Describe the mechanism of breathing in term of movements of ribs and diaphragm.', 'پسلیوں اور ڈایافرام کی حرکات کے حوالے سے سانس لینے کا طریقۂ کار بیان کر سکیں۔', 'د پښتیو او ډیافرام د حرکتونو له مخې د ساه اخیستلو میکانیزم بیان کړای شي.'),
    P('State the rate of breathing at rest and after exercise.', 'آرام کی حالت میں اور ورزش کے بعد سانس لینے کی شرح بیان کر سکیں۔', 'د آرام په حالت کې او له تمرین وروسته د ساه اخیستلو کچه وښيي.'),
    P('Differentiate between the composition of inspired and expired air.', 'اندر لی جانے والی اور باہر نکالی جانے والی ہوا کی ترکیب میں فرق بیان کر سکیں۔', 'د دننه کېدونکې او بهر وتونکې هوا د جوړښت ترمنځ توپیر وکړای شي.'),
    P('Describe briefly diseases related to the respiratory system like bronchitis, emphysema, pneumonia, asthma, and lung cancer.', 'نظامِ تنفس سے متعلق بیماریوں جیسے برونکائٹس، ایمفیسیما، نمونیا، دمہ اور پھیپھڑوں کے سرطان کو مختصراً بیان کر سکیں۔', 'د تنفسي سیسټم پورې اړوند ناروغۍ لکه برونکایټس، ایمفیزیما، نمونیا، ساه لنډي او د سږو سرطان په لنډ ډول بیان کړای شي.'),
    P('Describe the biological consequences of smoking in relation to the lungs and circulatory system.', 'پھیپھڑوں اور نظامِ دورانِ خون کے حوالے سے تمباکو نوشی کے حیاتیاتی نتائج بیان کر سکیں۔', 'د سږو او د وینې د ګردش سیسټم په تړاو د سګرټ څکولو بیولوژیکي پایلې بیان کړای شي.')
  ];
  chapter.slos = chapter.sloPairs.map(p => p.text);
  chapter.sourceOpening = {
    id: 'bio10-u10-opening', kind: 'unit opening page', pdfPage: 4, printedPage: '1', summary: 'Unit 10 opening page and Students Learning Outcomes', open: true,
    title: L('Unit 10 — GASEOUS EXCHANGE', 'یونٹ 10 — گیسوں کا تبادلہ', 'یونټ 10 — د ګازونو تبادله'),
    sloHeading: L('Students Learning Outcomes', 'طلبہ کے سیکھنے کے نتائج', 'د زده کوونکو د زده کړې پایلې'),
    sloIntro: L('The students will be able to:', 'طلبہ اس قابل ہو جائیں گے کہ:', 'زده کوونکي به وکولای شي چې:'),
    paras: [
      P('Unit 10', 'یونٹ 10', 'یونټ 10'),
      P('GASEOUS EXCHANGE', 'گیسوں کا تبادلہ', 'د ګازونو تبادله'),
      P('Students Learning Outcomes', 'طلبہ کے سیکھنے کے نتائج', 'د زده کوونکو د زده کړې پایلې'),
      P('The students will be able to:', 'طلبہ اس قابل ہو جائیں گے کہ:', 'زده کوونکي به وکولای شي چې:'),
      ...chapter.sloPairs,
      P('NOT FOR SALE', 'فروخت کے لیے نہیں', 'د پلور لپاره نه دی')
    ],
    layout: [{t: 'h', i: 0}, {t: 'h', i: 1}, {t: 'h', i: 2}, 3, {t: 'list', items: [4, 5, 6, 7, 8, 9, 10, 11]}, 12],
    exclusions: ['Decorative unit-opener illustration (blood vessel with red blood cells, heart and vascular tree) has no labels and no instructional caption.', 'Running footer "Biology X · 1" is page furniture.']
  };

  /* ---------------- Figures (inline SVG; printed labels preserved) ---------------- */
  const figures = {};
  figures['fig10-1'] = {
    id: 'fig10-1', widthRatio: 0.62,
    caption: L('Fig.10.1 Relationship between respiration, gaseous exchange and breathing.', 'شکل 10.1 تنفس، گیسوں کے تبادلے اور سانس لینے کے درمیان تعلق۔', 'شکل 10.1 د تنفس، د ګازونو تبادلې او ساه اخیستلو ترمنځ اړیکه.'),
    labels: [
      L('Air moves to lungs', 'ہوا پھیپھڑوں میں جاتی ہے', 'هوا سږو ته ځي'), L('Breathing', 'سانس لینا', 'ساه اخیستل'), L('Air moves out of lungs', 'ہوا پھیپھڑوں سے باہر نکلتی ہے', 'هوا له سږو بهر وځي'),
      L('Oxygen is taken from air', 'آکسیجن ہوا سے لی جاتی ہے', 'اکسیجن له هوا اخیستل کېږي'), L('Gaseous Exchange', 'گیسوں کا تبادلہ', 'د ګازونو تبادله'), L('Carbon dioxide is released in air', 'کاربن ڈائی آکسائیڈ ہوا میں خارج ہوتی ہے', 'کاربن ډای اکسایډ هوا ته خوشې کېږي'),
      L('Oxygen is transported to cells', 'آکسیجن خلیوں تک پہنچائی جاتی ہے', 'اکسیجن حجرو ته لېږدول کېږي'), L('Carbon dioxide is transported to lungs', 'کاربن ڈائی آکسائیڈ پھیپھڑوں تک پہنچائی جاتی ہے', 'کاربن ډای اکسایډ سږو ته لېږدول کېږي'),
      L('Oxygen is used to oxidize food', 'آکسیجن خوراک کی تکسید کے لیے استعمال ہوتی ہے', 'اکسیجن د خوراک د اکسیډیشن لپاره کارول کېږي'), L('Cellular Respiration', 'خلوی تنفس', 'حجروي تنفس'), L('Carbon dioxide is produced', 'کاربن ڈائی آکسائیڈ پیدا ہوتی ہے', 'کاربن ډای اکسایډ تولیدېږي')
    ],
    svg: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 330" role="img" aria-label="Fig.10.1 Relationship between respiration, gaseous exchange and breathing" font-family="Segoe UI, Arial, sans-serif" font-size="11">
      <defs><marker id="b10f1-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#334155"/></marker></defs>
      <g><rect x="10" y="8" width="500" height="86" rx="12" fill="#fef9c3" stroke="#eab308" stroke-width="1.5"/>
        <ellipse cx="95" cy="51" rx="72" ry="30" fill="#e2e8f0"/><text x="95" y="47" text-anchor="middle">Air moves to lungs</text>
        <text x="260" y="56" text-anchor="middle" font-size="14" font-weight="700" fill="#be123c">Breathing</text>
        <ellipse cx="425" cy="51" rx="72" ry="30" fill="#e2e8f0"/><text x="425" y="47" text-anchor="middle">Air moves out of lungs</text></g>
      <path d="M160 94 L140 118" stroke="#334155" stroke-width="1.5" marker-end="url(#b10f1-arrow)"/><path d="M380 118 L360 94" stroke="#334155" stroke-width="1.5" marker-end="url(#b10f1-arrow)"/>
      <path d="M248 94 L260 112 L272 94 z" fill="#7e22ce"/>
      <g><rect x="10" y="118" width="500" height="86" rx="12" fill="#cffafe" stroke="#0891b2" stroke-width="1.5"/>
        <ellipse cx="95" cy="161" rx="72" ry="30" fill="#fef3c7"/><text x="95" y="157" text-anchor="middle">Oxygen is taken from air</text>
        <text x="260" y="166" text-anchor="middle" font-size="14" font-weight="700" fill="#15803d">Gaseous Exchange</text>
        <ellipse cx="425" cy="161" rx="72" ry="30" fill="#fef3c7"/><text x="425" y="157" text-anchor="middle">Carbon dioxide is released in air</text></g>
      <path d="M150 204 L130 232" stroke="#334155" stroke-width="1.5" marker-end="url(#b10f1-arrow)"/><text x="150" y="222" text-anchor="middle" font-size="9" font-weight="700">Oxygen is transported to cells</text>
      <path d="M390 232 L370 204" stroke="#334155" stroke-width="1.5" marker-end="url(#b10f1-arrow)"/><text x="375" y="222" text-anchor="middle" font-size="9" font-weight="700">Carbon dioxide is transported to lungs</text>
      <path d="M248 204 L260 222 L272 204 z" fill="#15803d"/>
      <g><rect x="10" y="236" width="500" height="86" rx="12" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
        <ellipse cx="95" cy="279" rx="72" ry="30" fill="#f1f5f9"/><text x="95" y="275" text-anchor="middle">Oxygen is used to oxidize food</text>
        <text x="260" y="284" text-anchor="middle" font-size="14" font-weight="700" fill="#ea580c" text-decoration="underline">Cellular Respiration</text>
        <ellipse cx="425" cy="279" rx="72" ry="30" fill="#f1f5f9"/><text x="425" y="275" text-anchor="middle">Carbon dioxide is produced</text></g>
    </svg>`
  };
  figures['fig10-2'] = {
    id: 'fig10-2', widthRatio: 0.95,
    caption: L('Fig.10.2 (a). Gaseous exchange in plants; (b). Gaseous exchange in a leaf.', 'شکل 10.2 (a) پودوں میں گیسوں کا تبادلہ؛ (b) پتے میں گیسوں کا تبادلہ۔', 'شکل 10.2 (a) په بوټو کې د ګازونو تبادله؛ (b) په پاڼه کې د ګازونو تبادله.'),
    labels: [L('Night', 'رات', 'شپه'), L('Day', 'دن', 'ورځ'), L('Cutcile', 'کیوٹیکل', 'کیوټیکل'), L('Mesophyll', 'میزوفل', 'میزوفیل'), L('Air enters', 'ہوا داخل ہوتی ہے', 'هوا ننوځي'), L('Stoma', 'سٹوما', 'سټوما'), L('Air leaves', 'ہوا خارج ہوتی ہے', 'هوا وځي')],
    note: 'Printed label spelling "Cutcile" (for cuticle) is kept as printed.',
    svg: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 300" role="img" aria-label="Fig.10.2 Gaseous exchange in plants and in a leaf" font-family="Segoe UI, Arial, sans-serif" font-size="11">
      <defs><marker id="b10f2-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#db2777"/></marker><marker id="b10f2-ab" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#1e3a8a"/></marker></defs>
      <!-- (a) tree: night (left) / day (right) -->
      <rect x="10" y="20" width="120" height="230" fill="#94a3b8"/><rect x="130" y="20" width="120" height="230" fill="#fefce8"/>
      <rect x="118" y="150" width="24" height="100" fill="#92400e"/><path d="M130 150 L105 190 M130 150 L155 192" stroke="#92400e" stroke-width="6" fill="none"/>
      <ellipse cx="130" cy="120" rx="95" ry="60" fill="#4d7c0f"/><ellipse cx="100" cy="95" rx="55" ry="40" fill="#65a30d"/><ellipse cx="165" cy="95" rx="55" ry="40" fill="#84cc16"/>
      <rect x="10" y="20" width="120" height="230" fill="#1e293b" opacity="0.35"/>
      <text x="55" y="38" text-anchor="middle" font-size="13" font-weight="700" fill="#f43f5e">Night</text><text x="195" y="38" text-anchor="middle" font-size="13" font-weight="700" fill="#f97316">Day</text>
      <text x="30" y="60" font-size="12" font-weight="700" fill="#fff">O₂</text><path d="M48 58 L70 82" stroke="#db2777" stroke-width="2.5" marker-end="url(#b10f2-ar)"/>
      <text x="22" y="240" font-size="12" font-weight="700" fill="#fff">CO₂</text><path d="M68 196 L44 222" stroke="#db2777" stroke-width="2.5" marker-end="url(#b10f2-ar)"/>
      <text x="222" y="60" font-size="12" font-weight="700">O₂</text><path d="M192 82 L215 58" stroke="#db2777" stroke-width="2.5" marker-end="url(#b10f2-ar)"/>
      <text x="212" y="240" font-size="12" font-weight="700">CO₂</text><path d="M218 222 L194 196" stroke="#db2777" stroke-width="2.5" marker-end="url(#b10f2-ar)"/>
      <text x="130" y="272" text-anchor="middle" font-weight="700">(a)</text>
      <!-- leaf and arrow to section -->
      <path d="M262 100 C290 60 330 55 350 70 C340 95 300 120 262 100 z" fill="#22c55e" stroke="#15803d"/><path d="M262 100 L348 70" stroke="#15803d" stroke-width="1"/>
      <path d="M300 112 C330 130 350 140 372 150" stroke="#1e3a8a" stroke-width="3" fill="none" marker-end="url(#b10f2-ab)"/>
      <!-- (b) leaf block section -->
      <g transform="translate(372,90)">
        <polygon points="0,30 40,10 170,10 130,30" fill="#86efac" stroke="#166534"/>
        <rect x="0" y="30" width="130" height="12" fill="#d9f99d" stroke="#166534"/>
        <rect x="0" y="42" width="130" height="60" fill="#4ade80" stroke="#166534"/>
        <g stroke="#166534" fill="#86efac"><rect x="4" y="46" width="18" height="24"/><rect x="26" y="46" width="18" height="24"/><rect x="48" y="46" width="18" height="24"/><rect x="70" y="46" width="18" height="24"/><rect x="92" y="46" width="18" height="24"/><rect x="112" y="46" width="14" height="24"/>
        <circle cx="14" cy="86" r="7"/><circle cx="36" cy="86" r="7"/><circle cx="58" cy="86" r="7"/><circle cx="92" cy="86" r="7"/><circle cx="114" cy="86" r="7"/></g>
        <rect x="0" y="102" width="130" height="10" fill="#d9f99d" stroke="#166534"/>
        <polygon points="130,30 170,10 170,92 130,112" fill="#15803d" stroke="#166534"/>
        <ellipse cx="75" cy="107" rx="9" ry="4" fill="#fff" stroke="#166534"/>
        <path d="M60 140 L70 112" stroke="#1e3a8a" stroke-width="1.6" marker-end="url(#b10f2-ab)"/><path d="M80 112 L96 138" stroke="#1e3a8a" stroke-width="1.6" marker-end="url(#b10f2-ab)"/>
        <line x1="60" y1="20" x2="110" y2="-10" stroke="#111"/><text x="112" y="-12">Cutcile</text>
        <line x1="-10" y1="80" x2="8" y2="70" stroke="#111"/><text x="-50" y="88">Mesophyll</text>
        <text x="48" y="156" text-anchor="middle">Air enters</text><text x="112" y="156" text-anchor="middle">Air leaves</text>
        <line x1="84" y1="107" x2="112" y2="128" stroke="#111"/><text x="118" y="132">Stoma</text>
      </g>
      <text x="455" y="272" text-anchor="middle" font-weight="700">(b)</text>
    </svg>`
  };
  figures['fig10-3'] = {
    id: 'fig10-3', widthRatio: 0.5,
    caption: L('Fig.10.3 Lenticels in a bark', 'شکل 10.3 چھال میں لینٹیسلز', 'شکل 10.3 په پوستکي (بارک) کې لینټیسلز'),
    labels: [L('Bark', 'چھال', 'بارک (پوستکی)'), L('Lenticel', 'لینٹیسل', 'لینټیسل')],
    note: 'The textbook shows a photograph of a tree trunk with a magnified cross-section; it is redrawn here as a labelled schematic.',
    svg: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 230" role="img" aria-label="Fig.10.3 Lenticels in a bark" font-family="Segoe UI, Arial, sans-serif" font-size="11">
      <defs><marker id="b10f3-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#dc2626"/></marker></defs>
      <rect x="20" y="10" width="110" height="210" rx="18" fill="#b45309"/><rect x="34" y="10" width="20" height="210" fill="#d97706" opacity="0.5"/>
      <g fill="#fde68a" stroke="#78350f" stroke-width="0.8"><ellipse cx="60" cy="40" rx="9" ry="3"/><ellipse cx="95" cy="62" rx="9" ry="3"/><ellipse cx="50" cy="90" rx="9" ry="3"/><ellipse cx="100" cy="112" rx="9" ry="3"/><ellipse cx="70" cy="140" rx="9" ry="3"/><ellipse cx="105" cy="168" rx="9" ry="3"/><ellipse cx="55" cy="195" rx="9" ry="3"/></g>
      <text x="75" y="226" text-anchor="middle" font-weight="700">Bark</text>
      <path d="M112 112 C160 90 190 90 215 110" stroke="#dc2626" stroke-width="2.5" fill="none" marker-end="url(#b10f3-a)"/>
      <circle cx="245" cy="140" r="62" fill="#0e7490" stroke="#111" stroke-width="1.2"/>
      <path d="M190 120 L210 118 L228 96 L262 96 L280 118 L300 120" stroke="#b91c1c" stroke-width="5" fill="none"/>
      <g fill="#fff" opacity="0.85"><circle cx="236" cy="108" r="3"/><circle cx="246" cy="104" r="3"/><circle cx="256" cy="108" r="3"/><circle cx="242" cy="114" r="3"/><circle cx="252" cy="115" r="3"/><circle cx="228" cy="150" r="2"/><circle cx="262" cy="160" r="2"/><circle cx="240" cy="175" r="2"/><circle cx="275" cy="140" r="2"/><circle cx="214" cy="140" r="2"/></g>
      <line x1="246" y1="100" x2="268" y2="70" stroke="#111"/><text x="270" y="68">Lenticel</text>
    </svg>`
  };
  figures['fig10-4'] = {
    id: 'fig10-4', widthRatio: 0.72,
    caption: L('Fig.10.4 General Outline of the Air Passageway and Lungs', 'شکل 10.4 ہوا کی گزرگاہ اور پھیپھڑوں کا عمومی خاکہ', 'شکل 10.4 د هوا د لارې او سږو عمومي انځور'),
    labels: [L('Nasal cavity', 'ناک کا خلا', 'د پوزې خالیګاه'), L('Nostril', 'نتھنا', 'سوری د پوزې'), L('Epiglottis', 'ایپی گلوٹس', 'اپیګلوټس'), L('Larynx', 'لیرنکس', 'لارینکس'), L('Pleural cavity', 'پلورل کیویٹی', 'پلورل خالیګاه'), L('Right lung', 'دایاں پھیپھڑا', 'ښی سږی'), L('Diaphragm', 'ڈایافرام', 'ډیافرام'), L('Left lung', 'بایاں پھیپھڑا', 'کیڼ سږی'), L('Pharynx', 'فیرنکس', 'فارینکس'), L('Trachea', 'ٹریکیا', 'ټراکیا'), L('Bronchus', 'برونکس', 'برونکس')],
    svg: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 330" role="img" aria-label="Fig.10.4 General Outline of the Air Passageway and Lungs" font-family="Segoe UI, Arial, sans-serif" font-size="11">
      <path d="M150 20 C215 5 260 40 255 95 C250 125 230 140 215 150 L215 175 C290 180 350 215 350 325 L90 325 C90 215 150 180 185 175 L185 150 C160 135 130 100 150 20 z" fill="#fdba74" opacity="0.8"/>
      <path d="M185 66 C175 70 170 82 176 90 L198 92" fill="#fb7185" stroke="#be123c"/>
      <path d="M198 92 C200 110 202 130 198 150 L198 188" stroke="#7f1d1d" stroke-width="8" fill="none"/>
      <rect x="192" y="118" width="12" height="12" fill="#9f1239"/>
      <path d="M190 100 L204 112" stroke="#be123c" stroke-width="3"/>
      <path d="M198 150 L198 190" stroke="#94a3b8" stroke-width="10" stroke-dasharray="3 3"/>
      <path d="M198 190 L160 215 M198 190 L236 215" stroke="#94a3b8" stroke-width="7" fill="none"/>
      <path d="M160 200 C105 200 95 260 110 310 L185 310 C195 280 190 230 160 200 z" fill="#e11d48" opacity="0.75" stroke="#881337" stroke-width="2" stroke-dasharray="5 3"/>
      <path d="M238 200 C290 200 300 260 288 310 L215 310 C205 280 212 230 238 200 z" fill="#e11d48" opacity="0.75" stroke="#881337" stroke-width="2" stroke-dasharray="5 3"/>
      <path d="M160 215 C150 240 140 270 150 300 M236 215 C246 240 254 270 246 300" stroke="#fda4af" stroke-width="2" fill="none"/>
      <path d="M100 312 C150 300 250 300 300 312" stroke="#7f1d1d" stroke-width="3" fill="none"/>
      <line x1="60" y1="60" x2="178" y2="75" stroke="#111"/><text x="2" y="58">Nasal cavity</text>
      <line x1="60" y1="92" x2="172" y2="92" stroke="#111"/><text x="18" y="96">Nostril</text>
      <line x1="60" y1="118" x2="192" y2="120" stroke="#111"/><text x="2" y="122">Epiglottis</text>
      <line x1="60" y1="140" x2="190" y2="140" stroke="#111"/><text x="14" y="144">Larynx</text>
      <line x1="60" y1="235" x2="120" y2="235" stroke="#111"/><text x="2" y="238">Pleural cavity</text>
      <line x1="140" y1="320" x2="150" y2="300" stroke="#111"/><text x="86" y="326">Right lung</text>
      <line x1="200" y1="326" x2="200" y2="312" stroke="#111"/><text x="172" y="328" font-size="10">Diaphragm</text>
      <line x1="300" y1="320" x2="250" y2="300" stroke="#111"/><text x="300" y="326">Left lung</text>
      <line x1="300" y1="112" x2="204" y2="116" stroke="#111"/><text x="304" y="116">Pharynx</text>
      <line x1="320" y1="175" x2="205" y2="170" stroke="#111"/><text x="324" y="179">Trachea</text>
      <line x1="320" y1="214" x2="236" y2="212" stroke="#111"/><text x="324" y="218">Bronchus</text>
    </svg>`
  };
  figures['fig10-5'] = {
    id: 'fig10-5', widthRatio: 0.9,
    caption: L('Fig.10.5 General Outline of Respiratory System in the Human Body.', 'شکل 10.5 انسانی جسم میں نظامِ تنفس کا عمومی خاکہ۔', 'شکل 10.5 د انسان په بدن کې د تنفسي سیسټم عمومي انځور.'),
    labels: [L('Ethmoid sinuses', 'ایتھمائیڈ سائنس', 'ایتموید ساینوسونه'), L('Nose', 'ناک', 'پوزه'), L('Pharynx', 'فیرنکس', 'فارینکس'), L('Tongue', 'زبان', 'ژبه'), L('Lung', 'پھیپھڑا', 'سږی'), L('Trachea', 'ٹریکیا', 'ټراکیا'), L('Bronchus', 'برونکس', 'برونکس'), L('Bronchioles', 'برونکیولز', 'برونکیولونه'), L('Alveoli', 'الویولائی', 'الویولي')],
    svg: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 320" role="img" aria-label="Fig.10.5 General Outline of Respiratory System in the Human Body" font-family="Segoe UI, Arial, sans-serif" font-size="11">
      <path d="M150 30 C210 15 245 50 240 100 C236 125 220 140 205 150 L205 170 C270 175 320 210 320 315 L80 315 C80 210 130 175 170 170 L170 150 C145 135 120 100 150 30 z" fill="#fde68a" opacity="0.75"/>
      <path d="M160 45 C185 40 205 55 208 75 L206 95 L178 92 C170 80 160 70 160 45 z" fill="#ef4444" opacity="0.85"/>
      <path d="M185 92 C195 95 200 110 200 125 L200 185" stroke="#f87171" stroke-width="7" fill="none"/>
      <path d="M200 135 L200 185" stroke="#94a3b8" stroke-width="9" stroke-dasharray="3 3"/>
      <path d="M200 185 L168 205 M200 185 L232 205" stroke="#94a3b8" stroke-width="6" fill="none"/>
      <path d="M168 195 C115 195 100 250 118 300 L190 300 C198 270 190 225 168 195 z" fill="#f97316" opacity="0.8" stroke="#c2410c"/>
      <path d="M232 195 C285 195 300 250 282 300 L210 300 C202 270 210 225 232 195 z" fill="#f97316" opacity="0.8" stroke="#c2410c"/>
      <g stroke="#fff" stroke-width="1.5" fill="none"><path d="M168 205 L150 240 L138 270 M150 240 L160 275 M232 205 L250 240 L262 270 M250 240 L240 275"/></g>
      <circle cx="258" cy="262" r="5" fill="none" stroke="#111"/><path d="M263 262 L330 230" stroke="#111"/>
      <circle cx="430" cy="190" r="110" fill="#fff" stroke="#111" stroke-width="1.5"/>
      <path d="M470 90 C480 110 470 130 450 150 C440 160 436 170 432 182" stroke="#7c2d12" stroke-width="10" fill="none" stroke-linecap="round"/>
      <g stroke="#1d4ed8" stroke-width="3" fill="none"><path d="M460 100 l12 6 M452 118 l13 5 M446 136 l12 7 M440 156 l12 6"/></g>
      <path d="M432 182 C420 192 400 196 388 206 M432 182 C440 195 452 200 462 210" stroke="#9a3412" stroke-width="5" fill="none"/>
      <g fill="#dc2626" stroke="#7f1d1d" stroke-width="0.6"><circle cx="372" cy="208" r="7"/><circle cx="384" cy="218" r="7"/><circle cx="366" cy="222" r="7"/><circle cx="378" cy="232" r="7"/><circle cx="360" cy="236" r="7"/><circle cx="392" cy="232" r="7"/><circle cx="372" cy="246" r="7"/>
        <circle cx="470" cy="216" r="7"/><circle cx="484" cy="226" r="7"/><circle cx="462" cy="230" r="7"/><circle cx="476" cy="240" r="7"/><circle cx="492" cy="240" r="7"/><circle cx="468" cy="254" r="7"/><circle cx="484" cy="256" r="7"/></g>
      <circle cx="496" cy="160" r="14" fill="#fbbf24" stroke="#78350f" stroke-width="2"/><circle cx="496" cy="160" r="5" fill="#451a03"/>
      <line x1="378" y1="246" x2="400" y2="280" stroke="#111"/><text x="392" y="292" text-anchor="middle">Alveoli</text>
      <line x1="496" y1="174" x2="478" y2="296" stroke="#111"/><line x1="462" y1="210" x2="470" y2="296" stroke="#111"/><text x="470" y="308" text-anchor="middle">Bronchioles</text>
      <line x1="120" y1="40" x2="170" y2="60" stroke="#111"/><text x="14" y="40">Ethmoid sinuses</text>
      <line x1="236" y1="70" x2="206" y2="75" stroke="#111"/><text x="240" y="74">Nose</text>
      <line x1="120" y1="86" x2="186" y2="92" stroke="#111"/><text x="74" y="90">Pharynx</text>
      <line x1="238" y1="95" x2="208" y2="88" stroke="#111"/><text x="242" y="99">Tongue</text>
      <line x1="130" y1="110" x2="150" y2="220" stroke="#111"/><text x="100" y="112">Lung</text>
      <line x1="238" y1="122" x2="202" y2="130" stroke="#111"/><text x="242" y="126">Trachea</text>
      <line x1="130" y1="130" x2="175" y2="198" stroke="#111"/><text x="88" y="134">Bronchus</text>
      <line x1="120" y1="236" x2="150" y2="245" stroke="#111"/><text x="60" y="240">Bronchioles</text>
    </svg>`
  };

  /* ---------------- Topics (source sections) ---------------- */
  const keep = Object.fromEntries((chapter.topics || []).map(t => [t.num, t]));
  const practice = num => ({subtopics: (keep[num] && keep[num].subtopics) || []});

  const intro = {
    id: 'bio10-u10-intro', num: 'intro', title: 'Introduction', urduTitle: 'تعارف', pashtoTitle: 'سریزه',
    sourceReferences: [ref(5, 2)], translationStatus: 'authored_aligned_paragraphs',
    paras: [
      P('All living organisms need energy to perform their life sustaining activities. We already know that the ultimate source of energy for life is sunlight. Photosynthetic organisms capture sunlight (recall photosynthesis from Unit 7) and prepare energy rich organic molecules (food) by utilising carbon dioxide and water. Oxygen is released as a bye product of photosynthesis. Respiration takes place in all organisms. During respiration they utilise oxygen to break down organic molecules into carbon dioxide and water to release energy (recall respiration from Unit 7). In this unit we will study how organism give and take the gases (carbon dioxide and oxygen) which are needed for photosynthesis and respiration. We will also study the human respiratory system and its common diseases in detail.',
        'تمام جاندار اپنی زندگی برقرار رکھنے والی سرگرمیاں انجام دینے کے لیے توانائی کے محتاج ہیں۔ ہم پہلے سے جانتے ہیں کہ زندگی کے لیے توانائی کا حتمی ذریعہ سورج کی روشنی ہے۔ ضیائی تالیف کرنے والے جاندار سورج کی روشنی حاصل کرتے ہیں (یونٹ 7 سے ضیائی تالیف یاد کیجیے) اور کاربن ڈائی آکسائیڈ اور پانی استعمال کر کے توانائی سے بھرپور نامیاتی سالمات (خوراک) تیار کرتے ہیں۔ آکسیجن ضیائی تالیف کی ضمنی پیداوار کے طور پر خارج ہوتی ہے۔ تنفس تمام جانداروں میں ہوتا ہے۔ تنفس کے دوران وہ آکسیجن استعمال کر کے نامیاتی سالمات کو کاربن ڈائی آکسائیڈ اور پانی میں توڑتے ہیں تاکہ توانائی خارج ہو (یونٹ 7 سے تنفس یاد کیجیے)۔ اس یونٹ میں ہم مطالعہ کریں گے کہ جاندار وہ گیسیں (کاربن ڈائی آکسائیڈ اور آکسیجن) کیسے دیتے اور لیتے ہیں جو ضیائی تالیف اور تنفس کے لیے درکار ہیں۔ ہم انسانی نظامِ تنفس اور اس کی عام بیماریوں کا بھی تفصیل سے مطالعہ کریں گے۔',
        'ټول ژوندي موجودات د خپل ژوند د ساتلو فعالیتونو د ترسره کولو لپاره انرژۍ ته اړتیا لري. موږ له مخکې پوهېږو چې د ژوند لپاره د انرژۍ وروستۍ سرچینه د لمر رڼا ده. فوتوسنتیز کوونکي موجودات د لمر رڼا نیسي (له اووم یونټ څخه فوتوسنتیز رایاد کړئ) او د کاربن ډای اکسایډ او اوبو په کارولو سره له انرژۍ ډک عضوي مالیکولونه (خوراک) جوړوي. اکسیجن د فوتوسنتیز د ضمني محصول په توګه خوشې کېږي. تنفس په ټولو ژوندیو موجوداتو کې ترسره کېږي. د تنفس پر مهال دوی اکسیجن کاروي ترڅو عضوي مالیکولونه په کاربن ډای اکسایډ او اوبو مات کړي او انرژي خوشې کړي (له اووم یونټ څخه تنفس رایاد کړئ). په دې یونټ کې به موږ مطالعه وکړو چې ژوندي موجودات هغه ګازونه (کاربن ډای اکسایډ او اکسیجن) څنګه ورکوي او اخلي چې د فوتوسنتیز او تنفس لپاره اړین دي. موږ به د انسان تنفسي سیسټم او د هغه عامې ناروغۍ هم په تفصیل سره مطالعه کړو.')
    ],
    layout: [0]
  };

  const t101 = {
    id: 'bio10-u10-t1', num: '10.1', title: 'Respiration, Gaseous Exchange and Breathing', urduTitle: 'تنفس، گیسوں کا تبادلہ اور سانس لینا', pashtoTitle: 'تنفس، د ګازونو تبادله او ساه اخیستل',
    sourceReferences: [ref(5, 2)], translationStatus: 'authored_aligned_paragraphs', subtopics: [],
    figures: {'fig10-1': figures['fig10-1']},
    paras: [
      P('Respiration is an energy releasing process at the cellular level. In this process, food molecules (e.g. glucose) are broken down into simpler compounds like carbon dioxide and water with the release of energy. We know that for aerobic respiration, oxygen is required for the complete oxidation of food molecules while CO₂ is released as a by product. It means that all organisms need to take O₂ from the environment (air or water) for respiration. They also need to release CO₂ into the environment.',
        'تنفس خلوی سطح پر توانائی خارج کرنے والا عمل ہے۔ اس عمل میں خوراک کے سالمات (مثلاً گلوکوز) توانائی کے اخراج کے ساتھ کاربن ڈائی آکسائیڈ اور پانی جیسے سادہ مرکبات میں ٹوٹ جاتے ہیں۔ ہم جانتے ہیں کہ ہوائی تنفس کے لیے خوراک کے سالمات کی مکمل تکسید کے لیے آکسیجن درکار ہوتی ہے جبکہ CO₂ ضمنی پیداوار کے طور پر خارج ہوتی ہے۔ اس کا مطلب ہے کہ تمام جانداروں کو تنفس کے لیے ماحول (ہوا یا پانی) سے O₂ لینے کی ضرورت ہوتی ہے۔ انہیں CO₂ ماحول میں خارج کرنے کی بھی ضرورت ہوتی ہے۔',
        'تنفس په حجروي کچه د انرژۍ د خوشې کولو بهیر دی. په دې بهیر کې د خوراک مالیکولونه (لکه ګلوکوز) د انرژۍ له خوشې کېدو سره په ساده مرکباتو لکه کاربن ډای اکسایډ او اوبو ماتېږي. موږ پوهېږو چې د هوايي تنفس لپاره د خوراک د مالیکولونو بشپړ اکسیډیشن ته اکسیجن اړین دی، په داسې حال کې چې CO₂ د ضمني محصول په توګه خوشې کېږي. دا پدې مانا ده چې ټول ژوندي موجودات د تنفس لپاره له چاپېریال (هوا یا اوبو) څخه O₂ اخیستلو ته اړتیا لري. دوی باید CO₂ هم چاپېریال ته خوشې کړي.', {bold: ['Respiration']}),
      P('Diffusion is a process in which molecules move from a region of higher concentration to a region of lower concentration.',
        'انتشار (ڈفیوژن) ایک ایسا عمل ہے جس میں سالمات زیادہ ارتکاز والے علاقے سے کم ارتکاز والے علاقے کی طرف حرکت کرتے ہیں۔',
        'ډیفیوژن (خپرېدل) هغه بهیر دی چې په هغه کې مالیکولونه د لوړ غلظت له سیمې څخه د ټیټ غلظت سیمې ته حرکت کوي.'),
      P('Gaseous exchange means the exchange of oxygen and carbon dioxide between an organism and its environment. Gaseous exchange occurs by diffusion.',
        'گیسوں کے تبادلے سے مراد کسی جاندار اور اس کے ماحول کے درمیان آکسیجن اور کاربن ڈائی آکسائیڈ کا تبادلہ ہے۔ گیسوں کا تبادلہ انتشار کے ذریعے ہوتا ہے۔',
        'د ګازونو تبادله د یو ژوندي موجود او د هغه د چاپېریال ترمنځ د اکسیجن او کاربن ډای اکسایډ تبادلې ته ویل کېږي. د ګازونو تبادله د ډیفیوژن له لارې ترسره کېږي.', {bold: ['Gaseous exchange']}),
      P('Breathing is the physical process in which animals move air into and out of their body. It is done to get oxygen from air and to release carbon dioxide in it. In higher animals, lungs are the organs of breathing. In breathing, fresh air is made available to the respiratory surface of the lung for gaseous exchange. As fresh air has a higher concentration of oxygen than is present in the blood, therefore, it diffuses into the blood. At the same time, the concentration of carbon dioxide is higher in the blood, so it is diffuses into the lungs and is expelled out by the process of breathing.',
        'سانس لینا وہ طبعی عمل ہے جس میں جانور ہوا کو اپنے جسم کے اندر اور باہر لے جاتے ہیں۔ یہ ہوا سے آکسیجن حاصل کرنے اور اس میں کاربن ڈائی آکسائیڈ خارج کرنے کے لیے کیا جاتا ہے۔ اعلیٰ جانوروں میں پھیپھڑے سانس لینے کے اعضا ہیں۔ سانس لینے میں تازہ ہوا پھیپھڑے کی تنفسی سطح پر گیسوں کے تبادلے کے لیے مہیا کی جاتی ہے۔ چونکہ تازہ ہوا میں آکسیجن کا ارتکاز خون میں موجود ارتکاز سے زیادہ ہوتا ہے، اس لیے یہ خون میں منتشر ہو جاتی ہے۔ اسی وقت خون میں کاربن ڈائی آکسائیڈ کا ارتکاز زیادہ ہوتا ہے، اس لیے یہ پھیپھڑوں میں منتشر ہو جاتی ہے اور سانس لینے کے عمل سے باہر نکال دی جاتی ہے۔',
        'ساه اخیستل هغه فزیکي بهیر دی چې په هغه کې ځناور هوا خپل بدن ته دننه او بهر وړي. دا د هوا څخه د اکسیجن د اخیستلو او هغې ته د کاربن ډای اکسایډ د خوشې کولو لپاره ترسره کېږي. په لوړو ځناورو کې سږي د ساه اخیستلو غړي دي. په ساه اخیستلو کې تازه هوا د ګازونو د تبادلې لپاره د سږي تنفسي سطحې ته رسول کېږي. څرنګه چې تازه هوا کې د اکسیجن غلظت له هغه څخه لوړ وي چې په وینه کې موجود دی، نو ځکه هغه وینې ته خپرېږي. په همدې وخت کې په وینه کې د کاربن ډای اکسایډ غلظت لوړ وي، نو هغه سږو ته خپرېږي او د ساه اخیستلو د بهیر له لارې بهر ایستل کېږي.', {bold: ['Breathing']})
    ],
    layout: [0, {t: 'side', blocks: [{t: 'box', kind: 'recalling', paras: [1]}]}, 2, {t: 'side', blocks: [{t: 'fig', id: 'fig10-1'}]}, 3, {t: 'clear'}]
  };

  const t102 = {
    id: 'bio10-u10-t2', num: '10.2', title: 'Gaseous Exchange in Plants', urduTitle: 'پودوں میں گیسوں کا تبادلہ', pashtoTitle: 'په بوټو کې د ګازونو تبادله',
    sourceReferences: [ref(5, 2), ref(6, 3)], translationStatus: 'authored_aligned_paragraphs', ...practice('10.1'),
    figures: {'fig10-2': figures['fig10-2'], 'fig10-3': figures['fig10-3']},
    paras: [
      P('During the daytime, all plant cells are carrying out respiration. The green parts (leaves) of plants are also carrying out photosynthesis. For photosynthesis, the leaves use carbon dioxide which is produced during respiration. They also take carbon dioxide from the environment. For respiration, leaves use oxygen which is produced during photosynthesis. During respiration, they release carbon dioxide which is used in photosynthesis. So, during daytime leaves are taking carbon dioxide from the environment and releasing oxygen in it.',
        'دن کے وقت پودوں کے تمام خلیے تنفس کر رہے ہوتے ہیں۔ پودوں کے سبز حصے (پتے) ضیائی تالیف بھی کر رہے ہوتے ہیں۔ ضیائی تالیف کے لیے پتے وہ کاربن ڈائی آکسائیڈ استعمال کرتے ہیں جو تنفس کے دوران پیدا ہوتی ہے۔ وہ ماحول سے بھی کاربن ڈائی آکسائیڈ لیتے ہیں۔ تنفس کے لیے پتے وہ آکسیجن استعمال کرتے ہیں جو ضیائی تالیف کے دوران پیدا ہوتی ہے۔ تنفس کے دوران وہ کاربن ڈائی آکسائیڈ خارج کرتے ہیں جو ضیائی تالیف میں استعمال ہوتی ہے۔ چنانچہ دن کے وقت پتے ماحول سے کاربن ڈائی آکسائیڈ لے رہے ہوتے ہیں اور اس میں آکسیجن خارج کر رہے ہوتے ہیں۔',
        'د ورځې پر مهال د بوټي ټولې حجرې تنفس کوي. د بوټو شنې برخې (پاڼې) فوتوسنتیز هم کوي. د فوتوسنتیز لپاره پاڼې هغه کاربن ډای اکسایډ کاروي چې د تنفس پر مهال تولیدېږي. دوی له چاپېریال څخه هم کاربن ډای اکسایډ اخلي. د تنفس لپاره پاڼې هغه اکسیجن کاروي چې د فوتوسنتیز پر مهال تولیدېږي. د تنفس پر مهال دوی هغه کاربن ډای اکسایډ خوشې کوي چې په فوتوسنتیز کې کارول کېږي. نو د ورځې پر مهال پاڼې له چاپېریال څخه کاربن ډای اکسایډ اخلي او هغه ته اکسیجن خوشې کوي.'),
      P('During the night, all cells are carrying out respiration while there is no photosynthesis. So, the cells get oxygen from the environment and release carbon dioxide.',
        'رات کے وقت تمام خلیے تنفس کر رہے ہوتے ہیں جبکہ ضیائی تالیف نہیں ہوتی۔ چنانچہ خلیے ماحول سے آکسیجن حاصل کرتے ہیں اور کاربن ڈائی آکسائیڈ خارج کرتے ہیں۔',
        'د شپې پر مهال ټولې حجرې تنفس کوي، په داسې حال کې چې فوتوسنتیز نه ترسره کېږي. نو حجرې له چاپېریال څخه اکسیجن اخلي او کاربن ډای اکسایډ خوشې کوي.'),
      P('In plants, the gaseous exchange between the body and the environment occurs through the surface. The outer surface of the root, stem and leaves is called the epidermis. This layer allows the exchange of gases between the inner cells and the environment. At some parts a thick cuticle is present over the epidermis. It also allows the exchange of gases.',
        'پودوں میں جسم اور ماحول کے درمیان گیسوں کا تبادلہ سطح کے ذریعے ہوتا ہے۔ جڑ، تنے اور پتوں کی بیرونی سطح کو ایپی ڈرمس کہتے ہیں۔ یہ تہہ اندرونی خلیوں اور ماحول کے درمیان گیسوں کے تبادلے کی اجازت دیتی ہے۔ بعض حصوں پر ایپی ڈرمس کے اوپر ایک موٹی کیوٹیکل موجود ہوتی ہے۔ یہ بھی گیسوں کے تبادلے کی اجازت دیتی ہے۔',
        'په بوټو کې د بدن او چاپېریال ترمنځ د ګازونو تبادله د سطحې له لارې ترسره کېږي. د ریښې، ډډ او پاڼو بهرنۍ سطحې ته اپیډرمس ویل کېږي. دا طبقه د دنننیو حجرو او چاپېریال ترمنځ د ګازونو تبادلې ته اجازه ورکوي. په ځینو برخو کې د اپیډرمس له پاسه یوه پنډه کیوټیکل موجوده وي. هغه هم د ګازونو تبادلې ته اجازه ورکوي.', {bold: ['epidermis']}),
      P('In leaves and young stems, the epidermis has small pores called stomata. In these parts, the air moves in and out through the stomata. Inside the body, gaseous exchange occurs between the cells and air. In woody stems, the entire surface is covered by bark. Gaseous exchange cannot occur through bark. The bark contains special pores called lenticels, which allow the gaseous exchange with the environment.',
        'پتوں اور کم عمر تنوں میں ایپی ڈرمس میں چھوٹے مسام ہوتے ہیں جنہیں سٹومیٹا کہتے ہیں۔ ان حصوں میں ہوا سٹومیٹا کے ذریعے اندر اور باہر جاتی ہے۔ جسم کے اندر گیسوں کا تبادلہ خلیوں اور ہوا کے درمیان ہوتا ہے۔ لکڑی والے تنوں میں پوری سطح چھال سے ڈھکی ہوتی ہے۔ چھال کے ذریعے گیسوں کا تبادلہ نہیں ہو سکتا۔ چھال میں خاص مسام ہوتے ہیں جنہیں لینٹیسلز کہتے ہیں، جو ماحول کے ساتھ گیسوں کے تبادلے کی اجازت دیتے ہیں۔',
        'په پاڼو او ځوانو ډډونو کې اپیډرمس کوچني سوري لري چې سټوماټا ورته ویل کېږي. په دې برخو کې هوا د سټوماټا له لارې دننه او بهر ځي. د بدن په دننه کې د ګازونو تبادله د حجرو او هوا ترمنځ ترسره کېږي. په لرګینو ډډونو کې ټوله سطحه په پوستکي (بارک) پوښل شوې وي. د بارک له لارې د ګازونو تبادله نه شي ترسره کېدای. بارک ځانګړي سوري لري چې لینټیسلز ورته ویل کېږي او له چاپېریال سره د ګازونو تبادلې ته اجازه ورکوي.', {bold: ['stomata', 'lenticels']}),
      P('Effects of Tilling', 'ہل چلانے کے اثرات', 'د ځمکې د قلبې اغېزې'),
      P('You might have seen the farmers and gardeners tilling the soil. Tilling helps soil drainage and aeration. It creates air spaces between soil particles. These spaces in turn allow better exchange of gases between roots and the air.',
        'آپ نے کسانوں اور باغبانوں کو مٹی میں ہل چلاتے دیکھا ہوگا۔ ہل چلانا مٹی کی نکاسی اور ہوا داری میں مدد دیتا ہے۔ یہ مٹی کے ذرات کے درمیان ہوا کی جگہیں پیدا کرتا ہے۔ یہ جگہیں پھر جڑوں اور ہوا کے درمیان گیسوں کے بہتر تبادلے کی اجازت دیتی ہیں۔',
        'تاسو به بزګران او باغوانان لیدلي وي چې ځمکه قلبه کوي. قلبه کول د خاورې د اوبو د وتلو او هوا رسېدلو سره مرسته کوي. دا د خاورې د ذرو ترمنځ د هوا تشې جوړوي. دا تشې بیا د ریښو او هوا ترمنځ د ګازونو ښې تبادلې ته اجازه ورکوي.')
    ],
    layout: [0, 1, 2, 3, {t: 'fig', id: 'fig10-2'}, {t: 'columns', sideWidth: 260, main: [{t: 'box', kind: 'sts', title: 4, paras: [5]}], side: [{t: 'fig', id: 'fig10-3'}]}]
  };

  const t103 = {
    id: 'bio10-u10-t3', num: '10.3', title: 'Gaseous Exchange in Humans', urduTitle: 'انسانوں میں گیسوں کا تبادلہ', pashtoTitle: 'په انسانانو کې د ګازونو تبادله',
    sourceReferences: [ref(7, 4), ref(8, 5)], translationStatus: 'authored_aligned_paragraphs', ...practice('10.2'),
    figures: {'fig10-4': figures['fig10-4'], 'fig10-5': figures['fig10-5']},
    paras: [
      P('Humans have an efficient respiratory system adopted well for the terrestrial mode of life. This system ensures a smooth exchange of gases between the environment and the human body. This system can be divided into two main components which are: air passageway and lungs.',
        'انسانوں کا نظامِ تنفس مؤثر ہے جو خشکی کے طرزِ زندگی کے لیے خوب ڈھلا ہوا ہے۔ یہ نظام ماحول اور انسانی جسم کے درمیان گیسوں کے ہموار تبادلے کو یقینی بناتا ہے۔ اس نظام کو دو بنیادی حصوں میں تقسیم کیا جا سکتا ہے جو یہ ہیں: ہوا کی گزرگاہ اور پھیپھڑے۔',
        'انسانان یو اغېزمن تنفسي سیسټم لري چې د وچې د ژوند له ډول سره ښه برابر شوی دی. دا سیسټم د چاپېریال او د انسان د بدن ترمنځ د ګازونو اسانه تبادله ډاډمنه کوي. دا سیسټم په دوو اصلي برخو وېشل کېدای شي چې دا دي: د هوا لاره او سږي.'),
      P('a). Air Passageway', 'a) ہوا کی گزرگاہ', 'a) د هوا لاره'),
      P('When air enters the body, it passes through connected tubes to reach the lungs. After gaseous exchange, air moves from the lungs to the outside through the same connected tubes. These connected tubes are collectively called the air passageway. It consists of nostrils and nasal cavities, pharynx, larynx, trachea, bronchi and bronchioles.',
        'جب ہوا جسم میں داخل ہوتی ہے تو یہ پھیپھڑوں تک پہنچنے کے لیے آپس میں جڑی ہوئی نالیوں سے گزرتی ہے۔ گیسوں کے تبادلے کے بعد ہوا پھیپھڑوں سے انہی جڑی ہوئی نالیوں کے ذریعے باہر جاتی ہے۔ ان جڑی ہوئی نالیوں کو مجموعی طور پر ہوا کی گزرگاہ کہتے ہیں۔ یہ نتھنوں اور ناک کے خلاؤں، فیرنکس، لیرنکس، ٹریکیا، برونکائی اور برونکیولز پر مشتمل ہے۔',
        'کله چې هوا بدن ته ننوځي، نو سږو ته د رسېدو لپاره له سره تړلو نلونو تېرېږي. د ګازونو له تبادلې وروسته هوا له سږو څخه د همدغو تړلو نلونو له لارې بهر ځي. دغه تړلي نلونه په ټولیز ډول د هوا لاره بلل کېږي. دا د پوزې له سوریو او د پوزې له خالیګاوو، فارینکس، لارینکس، ټراکیا، برونکای او برونکیولونو څخه جوړه ده.'),
      P('Two openings or external nostrils lie on the ventral side of the head. They allow the air from the outside into two nasal cavities. Here the air is warmed, moistened and dust freed by the hairs and the mucous membrane of the nasal cavity.',
        'دو سوراخ یا بیرونی نتھنے سر کی بطنی (وینٹرل) جانب واقع ہوتے ہیں۔ یہ باہر کی ہوا کو ناک کے دو خلاؤں میں داخل ہونے دیتے ہیں۔ یہاں ہوا کو ناک کے خلا کے بالوں اور مخاطی جھلی کے ذریعے گرم، نم اور گرد سے پاک کیا جاتا ہے۔',
        'دوه سوري یا بهرني د پوزې سوري د سر په وینټرل (ګېډې اړخ) خوا کې پراته دي. دوی بهرنۍ هوا د پوزې دوو خالیګاوو ته ننوتلو ته پرېږدي. دلته هوا د پوزې د خالیګاه د وېښتانو او مخاطي پردې په واسطه تودېږي، لمدېږي او له دوړو پاکېږي.', {bold: ['external nostrils', 'nasal cavities']}),
      P('We should breathe through the nose and not through the mouth to keep ourselves healthy.',
        'ہمیں خود کو صحت مند رکھنے کے لیے ناک سے سانس لینا چاہیے، منہ سے نہیں۔',
        'موږ باید د خپل روغتیا د ساتلو لپاره له پوزې څخه ساه واخلو، نه له خولې څخه.'),
      P('The nasal cavities lead into the pharynx which is about a 4.5 inches long muscular passage. It is also lined by the mucous membrane.',
        'ناک کے خلا فیرنکس میں کھلتے ہیں جو تقریباً 4.5 انچ لمبا عضلاتی راستہ ہے۔ یہ بھی مخاطی جھلی سے مستور ہوتا ہے۔',
        'د پوزې خالیګاوې فارینکس ته لاره پیدا کوي چې شاوخوا 4.5 انچه اوږده عضلاتي لاره ده. دا هم په مخاطي پرده پوښل شوې ده.', {bold: ['pharynx']}),
      P('The pharynx contains tonsils and adenoids, which are organs of lymphatic tissue used to trap and filter microorganisms.',
        'فیرنکس میں ٹانسلز اور ایڈینائیڈز ہوتے ہیں، جو لمفاوی بافت کے اعضا ہیں اور خرد جانداروں کو پھنسانے اور چھاننے کے لیے استعمال ہوتے ہیں۔',
        'فارینکس ټانسلونه او اډینایډونه لري، چې د لمفاوي نسج غړي دي او د مایکرو ارګانیزمونو د نیولو او فلټر کولو لپاره کارول کېږي.'),
      P('The air moves from the pharynx into the larynx or voice box. It surrounds the upper part of the trachea. The cavity of the larynx is also lined by the mucous membrane. At the back of the pharynx are two passages, one opens into the esophagus on the dorsal side and the other opens through the glottis into the trachea on the ventral side. The glottis is guarded by a lid like structure called the epiglottis.',
        'ہوا فیرنکس سے لیرنکس یا صوتی خانے (وائس باکس) میں جاتی ہے۔ یہ ٹریکیا کے بالائی حصے کو گھیرے رکھتا ہے۔ لیرنکس کا خلا بھی مخاطی جھلی سے مستور ہوتا ہے۔ فیرنکس کے پچھلے حصے میں دو راستے ہوتے ہیں، ایک پشتی (ڈورسل) جانب غذائی نالی (ایسوفیگس) میں کھلتا ہے اور دوسرا بطنی جانب گلوٹس کے ذریعے ٹریکیا میں کھلتا ہے۔ گلوٹس کی حفاظت ایک ڈھکن نما ساخت کرتی ہے جسے ایپی گلوٹس کہتے ہیں۔',
        'هوا له فارینکس څخه لارینکس یا د غږ صندوق ته ځي. دا د ټراکیا پورتنۍ برخه چاپېره کوي. د لارینکس خالیګاه هم په مخاطي پرده پوښل شوې ده. د فارینکس په شا کې دوې لارې دي، یوه یې په ډورسل (شا) اړخ کې مرۍ (ایزوفیګس) ته خلاصېږي او بله یې په وینټرل اړخ کې د ګلوټس له لارې ټراکیا ته خلاصېږي. ګلوټس د یوه سرپوښ ډوله جوړښت په واسطه ساتل کېږي چې اپیګلوټس ورته ویل کېږي.', {bold: ['larynx', 'glottis']}),
      P('Why is it advised to breathe through the nose and not through the mouth?',
        'ناک سے سانس لینے اور منہ سے سانس نہ لینے کا مشورہ کیوں دیا جاتا ہے؟',
        'ولې سپارښتنه کېږي چې له پوزې څخه ساه واخیستل شي، نه له خولې څخه؟'),
      P('The larynx opens into the trachea or wind pipe. It is a tubular structure. It lies ventral to the esophagus and extends to the chest cavity or thorax. The inner surface of the trachea is ciliated and secretes mucus. This helps to filter, moisten and warm the incoming air. The trachea has 16 to 20 C-shaped cartilaginous rings which prevent it from collapsing and keep the passage of air open.',
        'لیرنکس ٹریکیا یا ہوا کی نالی (ونڈ پائپ) میں کھلتا ہے۔ یہ ایک نالی نما ساخت ہے۔ یہ غذائی نالی کی بطنی جانب واقع ہے اور سینے کے خلا یا تھوریکس تک پھیلی ہوئی ہے۔ ٹریکیا کی اندرونی سطح پر سیلیا ہوتے ہیں اور یہ بلغم (میوکس) خارج کرتی ہے۔ یہ اندر آنے والی ہوا کو چھاننے، نم کرنے اور گرم کرنے میں مدد دیتا ہے۔ ٹریکیا میں 16 سے 20 C کی شکل کے غضروفی (کارٹیلیجینس) حلقے ہوتے ہیں جو اسے پچکنے سے بچاتے ہیں اور ہوا کے راستے کو کھلا رکھتے ہیں۔',
        'لارینکس ټراکیا یا د هوا نل (وینډ پایپ) ته خلاصېږي. دا یو نل ډوله جوړښت دی. دا د مرۍ په وینټرل اړخ پروت دی او د سینې خالیګاه یا تورکس ته غځېږي. د ټراکیا دننۍ سطحه سیلیا لري او مخاط (میوکس) ترشح کوي. دا د ننوتونکې هوا په فلټر کولو، لمدولو او تودولو کې مرسته کوي. ټراکیا 16 تر 20 د C په شکل غضروفي حلقې لري چې هغه له ډوبېدو (پاشل کېدو) ساتي او د هوا لاره خلاصه ساتي.', {bold: ['trachea', 'cartilaginous rings']}),
      P('Transpiration is the loss of water from a plant surface in the form of vapours.',
        'ٹرانسپریشن پودے کی سطح سے بخارات کی شکل میں پانی کا ضیاع ہے۔',
        'ټرانسپیریشن د بوټي له سطحې څخه د بخار په بڼه د اوبو ضایع کېدل دي.'),
      P('Inside the thorax, the trachea divides into two branches called bronchi. Each bronchus enters the lung on its own side. The bronchi also possess the cartilaginous rings but smaller than those of the trachea. Each bronchus, on entering the lungs, divides and sub-divides progressively into smaller bronchi. When the smaller bronchi attain the diameter of one millimeter or less, then they are called bronchioles. Bronchioles have no cartilage.',
        'تھوریکس کے اندر ٹریکیا دو شاخوں میں تقسیم ہو جاتی ہے جنہیں برونکائی کہتے ہیں۔ ہر برونکس اپنی جانب کے پھیپھڑے میں داخل ہوتا ہے۔ برونکائی میں بھی غضروفی حلقے ہوتے ہیں لیکن ٹریکیا کے حلقوں سے چھوٹے۔ ہر برونکس پھیپھڑوں میں داخل ہونے پر بتدریج تقسیم اور ذیلی تقسیم ہو کر چھوٹی برونکائی بناتا ہے۔ جب چھوٹی برونکائی کا قطر ایک ملی میٹر یا اس سے کم ہو جاتا ہے تو انہیں برونکیولز کہتے ہیں۔ برونکیولز میں غضروف نہیں ہوتا۔',
        'د تورکس په دننه کې ټراکیا په دوو څانګو وېشل کېږي چې برونکای ورته ویل کېږي. هر برونکس د خپل اړخ سږي ته ننوځي. برونکای هم غضروفي حلقې لري خو د ټراکیا له حلقو څخه کوچنۍ. هر برونکس سږو ته له ننوتلو سره په تدریجي ډول وېشل او فرعي وېشل کېږي او کوچني برونکای جوړوي. کله چې کوچني برونکای یو ملي متر یا له هغه کم قطر ته ورسېږي، نو بیا برونکیولونه ورته ویل کېږي. برونکیولونه غضروف نه لري.', {bold: ['bronchi', 'bronchioles']}),
      P('Each bronchiole ends in a duct. The duct opens in a cluster of pouches, which resemble bunches of grapes. Each pouch is microscopic structure and is called alveolus (plural: Alveoli). The alveoli are thin-walled and provide the surface for gaseous exchange. Their walls are covered with a network of blood capillaries where gaseous exchange occurs.',
        'ہر برونکیول ایک نالی (ڈکٹ) پر ختم ہوتا ہے۔ یہ نالی تھیلیوں کے ایک گچھے میں کھلتی ہے جو انگور کے گچھوں سے مشابہ ہوتا ہے۔ ہر تھیلی خردبینی ساخت ہے اور اسے الویولس (جمع: الویولائی) کہتے ہیں۔ الویولائی پتلی دیوار والے ہوتے ہیں اور گیسوں کے تبادلے کے لیے سطح مہیا کرتے ہیں۔ ان کی دیواریں خون کی شعریات (کیپلریز) کے جال سے ڈھکی ہوتی ہیں جہاں گیسوں کا تبادلہ ہوتا ہے۔',
        'هر برونکیول په یوه نالۍ (ډکټ) پای ته رسېږي. دا نالۍ د کڅوړو په یوه ټولګي کې خلاصېږي چې د انګورو له وږو سره ورته والی لري. هره کڅوړه مایکروسکوپي جوړښت دی او الویولس (جمع: الویولي) ورته ویل کېږي. الویولي نرۍ دېوالونه لري او د ګازونو د تبادلې لپاره سطحه برابروي. د دوی دېوالونه د وینې د شعریه رګونو (کپیلریو) په جال پوښل شوي دي چې هلته د ګازونو تبادله ترسره کېږي.', {bold: ['alveolus']}),
      P('b). Lungs', 'b) پھیپھڑے', 'b) سږي'),
      P('The lungs are placed in the chest cavity. From above and sides, lungs are enclosed by the chest wall, while there is a thick muscular structure called the diaphragm below the lungs.',
        'پھیپھڑے سینے کے خلا میں واقع ہیں۔ اوپر اور اطراف سے پھیپھڑے سینے کی دیوار سے گھرے ہوئے ہیں، جبکہ پھیپھڑوں کے نیچے ایک موٹی عضلاتی ساخت ہوتی ہے جسے ڈایافرام کہتے ہیں۔',
        'سږي د سینې په خالیګاه کې ځای لري. له پاسه او اړخونو څخه سږي د سینې په دېوال پوښل شوي دي، په داسې حال کې چې د سږو لاندې یو پنډ عضلاتي جوړښت دی چې ډیافرام ورته ویل کېږي.', {bold: ['diaphragm']})
    ],
    layout: [0, {t: 'h', i: 1}, 2, {t: 'side', blocks: [{t: 'box', kind: 'fyi', paras: [4]}]}, 3, 5, {t: 'clear'}, {t: 'columns', sideWidth: 230, main: [{t: 'fig', id: 'fig10-4'}], side: [{t: 'box', kind: 'fyi', paras: [6]}]}, {t: 'side', blocks: [{t: 'box', kind: 'tidbit', paras: [8]}]}, 7, {t: 'side', blocks: [{t: 'box', kind: 'recalling', paras: [10]}]}, 9, {t: 'clear'}, 11, 12, {t: 'fig', id: 'fig10-5'}, {t: 'h', i: 13}, 14]
  };

  /* ---------- 10.3 continued: printed pages 6-7 (PDF 9-10) ---------- */
  figures['fig10-6'] = {
    id: 'fig10-6', widthRatio: 0.95,
    caption: L('Fig.10.6 Mechanism of Breathing in Humans', 'شکل 10.6 انسانوں میں سانس لینے کا طریقۂ کار', 'شکل 10.6 په انسانانو کې د ساه اخیستلو میکانیزم'),
    labels: [
      L('Rib cage expands as', 'پسلیوں کا پنجرہ پھیلتا ہے', 'د پښتیو قفس پراخېږي'), L('rib muscles contract', 'جب پسلیوں کے عضلات سکڑتے ہیں', 'کله چې د پښتیو عضلې تنګېږي'),
      L('Air inhaled', 'ہوا اندر لی گئی', 'هوا دننه واخیستل شوه'), L('Lung', 'پھیپھڑا', 'سږی'), L('Diaphragm', 'ڈایافرام', 'ډیافرام'),
      L('INHALATION', 'سانس اندر لینا', 'ساه اخیستل'), L('Diaphragm contracts', 'ڈایافرام سکڑتا ہے', 'ډیافرام تنګېږي'), L('(moves down)', '(نیچے جاتا ہے)', '(ښکته ځي)'),
      L('Rib cage gets smaller as', 'پسلیوں کا پنجرہ چھوٹا ہوتا ہے', 'د پښتیو قفس کوچنی کېږي'), L('rib muscles relax', 'جب پسلیوں کے عضلات ڈھیلے ہوتے ہیں', 'کله چې د پښتیو عضلې سستېږي'),
      L('Air exhaled', 'ہوا باہر نکالی گئی', 'هوا بهر وایستل شوه'), L('EXHALATION', 'سانس باہر نکالنا', 'ساه ایستل'), L('Diaphragm relaxes', 'ڈایافرام ڈھیلا ہوتا ہے', 'ډیافرام سستېږي'), L('(moves up)', '(اوپر جاتا ہے)', '(پورته ځي)'),
      L('A. Inhalation of Air', 'A. ہوا کا اندر جانا', 'A. د هوا دننه کېدل'), L('B. Exhalation of Air', 'B. ہوا کا باہر نکلنا', 'B. د هوا بهر وتل')
    ],
    svg: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 330" role="img" aria-label="Fig.10.6 Mechanism of Breathing in Humans" font-family="Segoe UI, Arial, sans-serif" font-size="11">
      <defs><marker id="b10f6-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#e11d48"/></marker></defs>
      <g id="b10f6-in">
        <path d="M60 300 C55 190 85 120 150 110 L170 60 C175 40 205 40 210 60 L230 110 C295 120 325 190 320 300 z" fill="#fed7aa"/>
        <path d="M190 40 C200 20 230 20 238 40 L232 70 L200 76 z" fill="#bae6fd"/><path d="M200 76 L200 150" stroke="#7dd3fc" stroke-width="9"/>
        <path d="M200 150 C140 140 105 190 110 265 L195 255 C200 220 200 180 200 150 z" fill="#f9a8d4" stroke="#be185d"/>
        <path d="M200 150 C260 140 295 190 290 265 L205 255 C200 220 200 180 200 150 z" fill="#f9a8d4" stroke="#be185d"/>
        <g stroke="#fef3c7" stroke-width="4" fill="none" opacity="0.9"><path d="M108 175 C150 165 250 165 292 175"/><path d="M104 200 C150 190 250 190 296 200"/><path d="M104 225 C150 215 250 215 296 225"/></g>
        <path d="M110 262 C150 250 250 250 290 262" stroke="#9a3412" stroke-width="4" fill="none"/>
        <g stroke="#e11d48" stroke-width="2.5" marker-end="url(#b10f6-a)"><path d="M100 190 L84 190"/><path d="M100 230 L84 232"/><path d="M300 190 L316 190"/><path d="M300 230 L316 232"/><path d="M200 252 L200 270"/></g>
        <path d="M262 40 L236 40" stroke="#2563eb" stroke-width="5" marker-end="url(#b10f6-a)"/>
        <text x="20" y="22">Rib cage expands as</text><text x="20" y="36">rib muscles contract</text><line x1="90" y1="40" x2="125" y2="170" stroke="#111"/>
        <text x="250" y="62">Air inhaled</text>
        <line x1="270" y1="205" x2="300" y2="205" stroke="#111"/><text x="303" y="209">Lung</text>
        <line x1="245" y1="258" x2="300" y2="268" stroke="#111"/><text x="248" y="284">Diaphragm</text>
        <rect x="120" y="272" width="150" height="44" rx="6" fill="#a7f3d0" stroke="#065f46"/>
        <text x="195" y="285" text-anchor="middle" font-weight="700">INHALATION</text><text x="195" y="298" text-anchor="middle">Diaphragm contracts</text><text x="195" y="310" text-anchor="middle">(moves down)</text>
        <text x="195" y="328" text-anchor="middle" font-weight="700">A. Inhalation of Air</text>
      </g>
      <g id="b10f6-ex" transform="translate(280,0)">
        <path d="M70 300 C65 190 90 125 150 115 L170 60 C175 40 205 40 210 60 L230 115 C290 125 315 190 310 300 z" fill="#fed7aa"/>
        <path d="M190 40 C200 20 230 20 238 40 L232 70 L200 76 z" fill="#bae6fd"/><path d="M200 76 L200 150" stroke="#7dd3fc" stroke-width="9"/>
        <path d="M200 150 C150 145 120 185 125 240 L195 235 C200 205 200 175 200 150 z" fill="#f9a8d4" stroke="#be185d"/>
        <path d="M200 150 C250 145 280 185 275 240 L205 235 C200 205 200 175 200 150 z" fill="#f9a8d4" stroke="#be185d"/>
        <g stroke="#fef3c7" stroke-width="4" fill="none" opacity="0.9"><path d="M122 180 C160 172 240 172 278 180"/><path d="M120 205 C160 197 240 197 280 205"/></g>
        <path d="M125 240 C150 215 250 215 275 240" stroke="#9a3412" stroke-width="4" fill="none"/>
        <g stroke="#e11d48" stroke-width="2.5" marker-end="url(#b10f6-a)"><path d="M112 190 L128 190"/><path d="M112 222 L128 222"/><path d="M288 190 L272 190"/><path d="M288 222 L272 222"/><path d="M200 236 L200 220"/></g>
        <path d="M236 40 L262 40" stroke="#2563eb" stroke-width="5" marker-end="url(#b10f6-a)"/>
        <text x="20" y="22">Rib cage gets smaller as</text><text x="20" y="36">rib muscles relax</text><line x1="90" y1="40" x2="135" y2="175" stroke="#111"/>
        <text x="245" y="62">Air exhaled</text>
        <rect x="140" y="272" width="150" height="44" rx="6" fill="#a7f3d0" stroke="#065f46"/>
        <text x="215" y="285" text-anchor="middle" font-weight="700">EXHALATION</text><text x="215" y="298" text-anchor="middle">Diaphragm relaxes</text><text x="215" y="310" text-anchor="middle">(moves up)</text>
        <text x="195" y="328" text-anchor="middle" font-weight="700">B. Exhalation of Air</text>
      </g>
    </svg>`
  };
  figures['fig10-7'] = {
    id: 'fig10-7', widthRatio: 0.62,
    caption: L('Fig.10.7 Blood circulation in the lungs (around an alveolus)', 'شکل 10.7 پھیپھڑوں میں خون کی گردش (ایک الویولس کے گرد)', 'شکل 10.7 په سږو کې د وینې ګردش (د یوه الویولس شاوخوا)'),
    labels: [L('Arteriole', 'آرٹیریول', 'شریانچه (آرټیریول)'), L('Alveolus', 'الویولس', 'الویولس'), L('Deoxygenated', 'آکسیجن سے خالی', 'بې اکسیجنه'), L('blood comes', 'خون آتا ہے', 'وینه راځي'), L('Capillaries', 'شعریات', 'شعریه رګونه'), L('Oxygenated', 'آکسیجن والا', 'اکسیجن لرونکې'), L('blood returns', 'خون واپس جاتا ہے', 'وینه بېرته ځي'), L('Venule', 'وینیول', 'وریدچه (وینیول)')],
    svg: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 260" role="img" aria-label="Fig.10.7 Blood circulation in the lungs around an alveolus" font-family="Segoe UI, Arial, sans-serif" font-size="11">
      <circle cx="215" cy="140" r="95" fill="#fb923c" stroke="#c2410c" stroke-width="2"/>
      <path d="M150 15 C175 25 185 45 170 70" stroke="#38bdf8" stroke-width="10" fill="none" stroke-linecap="round"/>
      <g stroke="#38bdf8" stroke-width="4" fill="none"><path d="M170 70 C200 60 240 55 270 75"/><path d="M170 70 C160 100 150 130 160 160"/><path d="M200 62 C210 90 205 120 215 140"/><path d="M240 60 C250 90 260 110 290 120"/><path d="M270 75 C290 95 300 110 305 130"/></g>
      <g stroke="#dc2626" stroke-width="4" fill="none"><path d="M160 160 C175 190 190 210 210 225"/><path d="M215 140 C220 170 215 200 210 225"/><path d="M305 130 C300 170 280 200 250 222"/><path d="M180 120 C230 130 260 150 290 170"/><path d="M160 200 C200 190 240 200 270 210"/></g>
      <path d="M210 225 C180 238 150 240 120 236" stroke="#dc2626" stroke-width="10" fill="none" stroke-linecap="round"/>
      <path d="M122 120 L98 112" stroke="#f97316" stroke-width="12"/>
      <line x1="160" y1="22" x2="230" y2="22" stroke="#111"/><text x="234" y="26">Arteriole</text>
      <line x1="245" y1="110" x2="300" y2="40" stroke="#111"/><text x="290" y="36">Alveolus</text>
      <line x1="300" y1="95" x2="330" y2="90" stroke="#111"/><line x1="300" y1="170" x2="330" y2="90" stroke="#111"/><text x="334" y="94">Capillaries</text>
      <text x="10" y="56">Deoxygenated</text><text x="14" y="70">blood comes</text><line x1="50" y1="78" x2="96" y2="110" stroke="#111"/>
      <text x="10" y="168">Oxygenated</text><text x="14" y="182">blood returns</text><line x1="50" y1="190" x2="120" y2="232" stroke="#111"/>
      <line x1="100" y1="250" x2="130" y2="238" stroke="#111"/><text x="60" y="256">Venule</text>
    </svg>`
  };
  t103.figures['fig10-6'] = figures['fig10-6'];
  t103.figures['fig10-7'] = figures['fig10-7'];
  t103.sourceReferences.push(ref(9, 6), ref(10, 7));
  const n3 = t103.paras.length;
  t103.paras.push(
    P('Each lung is enclosed in a double membrane called pleura. It contains a pleural fluid. This fluid makes the movements of the lungs (expansion and contraction) easy.',
      'ہر پھیپھڑا ایک دوہری جھلی میں بند ہوتا ہے جسے پلورا کہتے ہیں۔ اس میں پلورل سیال ہوتا ہے۔ یہ سیال پھیپھڑوں کی حرکات (پھیلنا اور سکڑنا) آسان بناتا ہے۔',
      'هر سږی په یوه دوه ګونې پرده کې ایسار دی چې پلورا ورته ویل کېږي. دا پلورل مایع لري. دا مایع د سږو حرکتونه (پراخېدل او تنګېدل) اسانه کوي.', {bold: ['pleura', 'pleural fluid']}),
    P('10.3.1 Mechanism of Breathing', '10.3.1 سانس لینے کا طریقۂ کار', '10.3.1 د ساه اخیستلو میکانیزم'),
    P('Breathing consists of two phases, the taking in of air called inspiration and letting out of air called expiration. These two phases take place continuously one after the other. Air moves in when the air pressure in the lungs is lower than the pressure outside the body and it moves out when the pressure in the lungs is greater than the atmospheric pressure.',
      'سانس لینا دو مراحل پر مشتمل ہے، ہوا اندر لینا جسے انسپریشن (شہیق) کہتے ہیں اور ہوا باہر نکالنا جسے ایکسپریشن (زفیر) کہتے ہیں۔ یہ دونوں مراحل مسلسل ایک کے بعد دوسرا واقع ہوتے ہیں۔ ہوا اس وقت اندر جاتی ہے جب پھیپھڑوں میں ہوا کا دباؤ جسم کے باہر کے دباؤ سے کم ہو اور اس وقت باہر نکلتی ہے جب پھیپھڑوں میں دباؤ کرۂ ہوائی کے دباؤ سے زیادہ ہو۔',
      'ساه اخیستل دوه پړاوونه لري، د هوا دننه اخیستل چې انسپیریشن ورته ویل کېږي او د هوا بهر ایستل چې ایکسپیریشن ورته ویل کېږي. دا دواړه پړاوونه په پرله پسې ډول یو له بل وروسته ترسره کېږي. هوا هغه وخت دننه ځي چې په سږو کې د هوا فشار د بدن له بهرني فشار څخه ټیټ وي او هغه وخت بهر ځي چې په سږو کې فشار د اتموسفیر له فشار څخه زیات وي.'),
    P('The thorax or chest-cavity is bound by the ribs and muscles at the sides, by the sternum (or chest bone) on the ventral side, by the backbone on the dorsal side and by the diaphragm at the posterior end. The diaphragm is a dome-shaped sheet of skeletal muscles. The muscles in between the ribs are called intercostal muscles.',
      'تھوریکس یا سینے کا خلا اطراف میں پسلیوں اور عضلات سے، بطنی جانب سٹرنم (یا سینے کی ہڈی) سے، پشتی جانب ریڑھ کی ہڈی سے اور پچھلے سرے پر ڈایافرام سے گھرا ہوتا ہے۔ ڈایافرام ڈھانچوی عضلات کی گنبد نما چادر ہے۔ پسلیوں کے درمیان موجود عضلات کو انٹرکوسٹل عضلات کہتے ہیں۔',
      'تورکس یا د سینې خالیګاه په اړخونو کې د پښتیو او عضلو، په وینټرل اړخ کې د سټرنم (یا د سینې هډوکي)، په ډورسل اړخ کې د ملا د تیر او په شاتني سر کې د ډیافرام په واسطه محدوده ده. ډیافرام د اسکلېټي عضلو ګنبد ډوله پاڼه ده. د پښتیو ترمنځ عضلو ته انټرکوسټل عضلې ویل کېږي.'),
    P('a) Inspiration: During inspiration, the volume of the chest cavity increases and the pressure in the lungs decreases. It happens due to two reasons.',
      'a) انسپریشن (شہیق): انسپریشن کے دوران سینے کے خلا کا حجم بڑھ جاتا ہے اور پھیپھڑوں میں دباؤ کم ہو جاتا ہے۔ یہ دو وجوہات کی بنا پر ہوتا ہے۔',
      'a) انسپیریشن: د انسپیریشن پر مهال د سینې د خالیګاه حجم زیاتېږي او په سږو کې فشار کمېږي. دا د دوو لاملونو له امله کېږي.', {bold: ['a) Inspiration:']}),
    P('The muscles of the diaphragm contract, so it becomes flat instead of its domed position.',
      'ڈایافرام کے عضلات سکڑتے ہیں، اس لیے یہ اپنی گنبد نما حالت کے بجائے چپٹا ہو جاتا ہے۔',
      'د ډیافرام عضلې تنګېږي، نو هغه د خپل ګنبدي حالت پر ځای هوار کېږي.'),
    P('The intercostal muscles present between the ribs, contract. Due to their contraction, the ribcage expands.',
      'پسلیوں کے درمیان موجود انٹرکوسٹل عضلات سکڑتے ہیں۔ ان کے سکڑنے کی وجہ سے پسلیوں کا پنجرہ پھیل جاتا ہے۔',
      'د پښتیو ترمنځ موجودې انټرکوسټل عضلې تنګېږي. د دوی د تنګېدو له امله د پښتیو قفس پراخېږي.'),
    P('Due to these movements the volume of the chest cavity increases and so pressure on the lungs decreases. As a result, the atmospheric air rushes in to the lungs through the air passageway.',
      'ان حرکات کی وجہ سے سینے کے خلا کا حجم بڑھ جاتا ہے اور یوں پھیپھڑوں پر دباؤ کم ہو جاتا ہے۔ نتیجتاً کرۂ ہوائی کی ہوا ہوا کی گزرگاہ کے ذریعے تیزی سے پھیپھڑوں میں داخل ہو جاتی ہے۔',
      'د دې حرکتونو له امله د سینې د خالیګاه حجم زیاتېږي او په دې توګه پر سږو فشار کمېږي. په پایله کې د اتموسفیر هوا د هوا د لارې له لارې په چټکۍ سره سږو ته ننوځي.'),
    P('b) Expiration: During this process, the muscles of the ribs and the diaphragm relax. The ribcage goes down to its original position whereas the diaphragm becomes dome-shaped. The volume of the chest cavity is decreased. It increases the pressure on the lungs to expel the air out.',
      'b) ایکسپریشن (زفیر): اس عمل کے دوران پسلیوں اور ڈایافرام کے عضلات ڈھیلے ہو جاتے ہیں۔ پسلیوں کا پنجرہ نیچے اپنی اصل حالت پر آ جاتا ہے جبکہ ڈایافرام گنبد نما ہو جاتا ہے۔ سینے کے خلا کا حجم کم ہو جاتا ہے۔ یہ پھیپھڑوں پر دباؤ بڑھاتا ہے تاکہ ہوا باہر نکل جائے۔',
      'b) ایکسپیریشن: د دې بهیر پر مهال د پښتیو او ډیافرام عضلې سستېږي. د پښتیو قفس خپل اصلي حالت ته ښکته کېږي په داسې حال کې چې ډیافرام ګنبد ډوله کېږي. د سینې د خالیګاه حجم کمېږي. دا پر سږو فشار زیاتوي ترڅو هوا بهر وباسي.', {bold: ['b) Expiration:']}),
    P('10.3.2 Gaseous exchange in Lungs', '10.3.2 پھیپھڑوں میں گیسوں کا تبادلہ', '10.3.2 په سږو کې د ګازونو تبادله'),
    P('We know that the alveoli are very thin-walled and have a network of blood capillaries. So they are an excellent site for gaseous exchange. The blood which enters these capillaries has a low oxygen concentration whereas the inhaled air present in the alveoli has a higher oxygen concentration. Therefore, oxygen from the alveoli diffuses into the capillaries. Similarly, the carbon dioxide concentration in the blood present in the capillaries is more than that of the alveoli. Therefore carbon dioxide diffuses out of the blood and into the alveoli.',
      'ہم جانتے ہیں کہ الویولائی بہت پتلی دیوار والے ہیں اور ان پر خون کی شعریات کا جال ہوتا ہے۔ اس لیے یہ گیسوں کے تبادلے کے لیے بہترین جگہ ہیں۔ ان شعریات میں داخل ہونے والے خون میں آکسیجن کا ارتکاز کم ہوتا ہے جبکہ الویولائی میں موجود اندر لی گئی ہوا میں آکسیجن کا ارتکاز زیادہ ہوتا ہے۔ اس لیے آکسیجن الویولائی سے شعریات میں منتشر ہو جاتی ہے۔ اسی طرح شعریات میں موجود خون میں کاربن ڈائی آکسائیڈ کا ارتکاز الویولائی سے زیادہ ہوتا ہے۔ اس لیے کاربن ڈائی آکسائیڈ خون سے نکل کر الویولائی میں منتشر ہو جاتی ہے۔',
      'موږ پوهېږو چې الویولي ډېر نري دېوالونه لري او د وینې د شعریه رګونو جال لري. نو دوی د ګازونو د تبادلې لپاره غوره ځای دی. هغه وینه چې دې شعریه رګونو ته ننوځي د اکسیجن ټیټ غلظت لري په داسې حال کې چې په الویولي کې دننه اخیستل شوې هوا د اکسیجن لوړ غلظت لري. له همدې امله اکسیجن له الویولي څخه شعریه رګونو ته خپرېږي. همدارنګه په شعریه رګونو کې د موجودې وینې د کاربن ډای اکسایډ غلظت د الویولي تر غلظت زیات وي. له همدې امله کاربن ډای اکسایډ له وینې څخه وځي او الویولي ته خپرېږي.'),
    P('The size of the lungs of any organism is related to the activities and body form of that organism. Cheetah and elephant have large lungs. What do you think why they have large lung sizes?',
      'کسی بھی جاندار کے پھیپھڑوں کا سائز اس جاندار کی سرگرمیوں اور جسمانی ساخت سے تعلق رکھتا ہے۔ چیتے اور ہاتھی کے پھیپھڑے بڑے ہوتے ہیں۔ آپ کے خیال میں ان کے پھیپھڑوں کا سائز بڑا کیوں ہوتا ہے؟',
      'د هر ژوندي موجود د سږو اندازه د هغه موجود له فعالیتونو او د بدن له جوړښت سره تړاو لري. چیتا او فیل لوی سږي لري. ستاسو په اند ولې د دوی سږي لوی دي؟')
  );
  t103.layout.push(n3, {t: 'h', i: n3 + 1}, {t: 'columns', sideWidth: 300, main: [n3 + 2], side: [{t: 'box', kind: 'fyi', paras: [n3 + 3]}]}, n3 + 4, {t: 'list', items: [n3 + 5, n3 + 6]}, n3 + 7, n3 + 8, {t: 'fig', id: 'fig10-6'}, {t: 'h', i: n3 + 9}, n3 + 10, {t: 'columns', sideWidth: 260, main: [{t: 'fig', id: 'fig10-7'}], side: [{t: 'box', kind: 'tidbit', paras: [n3 + 11]}]});

  /* ---------- 10.4 Biological Consequences of Smoking: printed pages 7-9 (PDF 10-12) ---------- */
  const cig = [['Butane', 'lighter fluid'], ['Cadmium', 'batteries'], ['Arsenic', 'poison'], ['Acetic acid', 'vinegar'], ['Nicotine', 'insecticide'], ['Paint'], ['Methane', 'sewer gas'], ['Ammonia'], ['Toilet cleaner'], ['Toluene', 'industrial solvent'], ['Stearic acid', 'candle wax'], ['Methanol', 'rocket fuel'], ['Carbon', 'monoxide', 'pollution'], ['Hexamine', 'barbeque', 'lighter'], ['Formaldehyde']];
  const cigUr = {'Butane':'بیوٹین','lighter fluid':'لائٹر کا سیال','Cadmium':'کیڈمیم','batteries':'بیٹریاں','Arsenic':'آرسینک','poison':'زہر','Acetic acid':'ایسیٹک ایسڈ','vinegar':'سرکہ','Nicotine':'نکوٹین','insecticide':'کیڑے مار دوا','Paint':'رنگ (پینٹ)','Methane':'میتھین','sewer gas':'گٹر کی گیس','Ammonia':'امونیا','Toilet cleaner':'ٹوائلٹ کلینر','Toluene':'ٹولوین','industrial solvent':'صنعتی محلل','Stearic acid':'سٹیرک ایسڈ','candle wax':'موم بتی کا موم','Methanol':'میتھانول','rocket fuel':'راکٹ کا ایندھن','Carbon':'کاربن','monoxide':'مونو آکسائیڈ','pollution':'آلودگی','Hexamine':'ہیکسامین','barbeque':'باربی کیو','lighter':'لائٹر','Formaldehyde':'فارملڈی ہائیڈ'};
  const cigPs = {'Butane':'بیوټین','lighter fluid':'د لایټر مایع','Cadmium':'کاډمیم','batteries':'بیټرۍ','Arsenic':'ارسنیک','poison':'زهر','Acetic acid':'اسیټیک اسید','vinegar':'سرکه','Nicotine':'نیکوټین','insecticide':'حشره وژونکی','Paint':'رنګ (پېنټ)','Methane':'میتان','sewer gas':'د ناوې ګاز','Ammonia':'امونیا','Toilet cleaner':'د تشناب پاکوونکی','Toluene':'ټولوین','industrial solvent':'صنعتي محلل','Stearic acid':'سټیریک اسید','candle wax':'د شمعې موم','Methanol':'میتانول','rocket fuel':'د راکټ تېل','Carbon':'کاربن','monoxide':'مونو اکسایډ','pollution':'ککړتیا','Hexamine':'هیکسامین','barbeque':'باربیکیو','lighter':'لایټر','Formaldehyde':'فارمالډیهایډ'};
  const pos = [[95, 70], [175, 40], [255, 30], [335, 30], [415, 40], [480, 70], [530, 115], [520, 170], [520, 200], [500, 240], [400, 275], [310, 280], [220, 265], [100, 225], [80, 160]];
  const cigLabels = [];
  const cigText = cig.map((lines, i) => {
    const [x, y] = pos[i];
    lines.forEach(t => { if (!cigLabels.some(l => l.text === t)) cigLabels.push(L(t, cigUr[t], cigPs[t])); });
    return `<circle cx="${x}" cy="${y + 22}" r="13" fill="#f59e0b"/><line x1="${x}" y1="${y + 35}" x2="300" y2="150" stroke="#f59e0b" stroke-width="2" stroke-dasharray="2 4"/>` + lines.map((t, k) => `<text x="${x}" y="${y - 2 + k * 12 - (lines.length - 1) * 12}" text-anchor="middle" fill="#e11d48">${t}</text>`).join('');
  }).join('');
  figures['fig10-8'] = {
    id: 'fig10-8', widthRatio: 0.95,
    caption: L('Fig. 10.8 Some of the Contents of a Cigarette', 'شکل 10.8 سگریٹ کے کچھ اجزا', 'شکل 10.8 د سګرټ ځینې اجزا'),
    labels: cigLabels,
    note: 'Printed pictograms (lighter, battery, skull, bottles, etc.) are shown as markers; each chemical is labelled as printed.',
    svg: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 310" role="img" aria-label="Fig. 10.8 Some of the Contents of a Cigarette" font-family="Segoe UI, Arial, sans-serif" font-size="11">${cigText}<rect x="250" y="142" width="110" height="16" rx="3" fill="#fef3c7" stroke="#92400e"/><rect x="330" y="142" width="30" height="16" rx="3" fill="#d97706"/></svg>`
  };
  const table101 = {
    caption: L('Table 10.1 Composition of Inspired and Expired Air', 'جدول 10.1 اندر لی جانے والی اور باہر نکالی جانے والی ہوا کی ترکیب', 'جدول 10.1 د دننه کېدونکې او بهر وتونکې هوا جوړښت'),
    headers: [L('Air components', 'ہوا کے اجزا', 'د هوا اجزا'), L('Inspired Air', 'اندر لی جانے والی ہوا', 'دننه کېدونکې هوا'), L('Expired Air', 'باہر نکالی جانے والی ہوا', 'بهر وتونکې هوا')],
    rowHeaders: true,
    rows: [
      [L('Oxygen', 'آکسیجن', 'اکسیجن'), '21%', '16%'],
      [L('Carbon dioxide', 'کاربن ڈائی آکسائیڈ', 'کاربن ډای اکسایډ'), '0.04%', '4%'],
      [L('Water vapours', 'آبی بخارات', 'د اوبو بخار'), L('Variable', 'متغیر', 'بدلېدونکی'), L('Saturated', 'سیر شدہ', 'مشبوع')],
      [L('Temperature', 'درجۂ حرارت', 'د تودوخې درجه'), L('Variable', 'متغیر', 'بدلېدونکی'), '38 °C']
    ]
  };
  const t104 = {
    id: 'bio10-u10-t4', num: '10.4', title: 'Biological Consequences of Smoking', urduTitle: 'تمباکو نوشی کے حیاتیاتی نتائج', pashtoTitle: 'د سګرټ څکولو بیولوژیکي پایلې',
    sourceReferences: [ref(10, 7), ref(11, 8), ref(12, 9)], translationStatus: 'authored_aligned_paragraphs', ...practice('10.5'),
    figures: {'fig10-8': figures['fig10-8']}, tables: {'table10-1': table101},
    paras: [
      P('Smokers have a much higher risk of developing life threatening diseases. The most crucial risk of smoking is cancer in the lungs, kidneys, oral cavity, larynx, breast, bladder, oesophagus, pancreas and stomach.',
        'تمباکو نوشی کرنے والوں میں جان لیوا بیماریاں لاحق ہونے کا خطرہ بہت زیادہ ہوتا ہے۔ تمباکو نوشی کا سب سے سنگین خطرہ پھیپھڑوں، گردوں، منہ کے خلا، لیرنکس، چھاتی، مثانے، غذائی نالی، لبلبے اور معدے کا سرطان ہے۔',
        'سګرټ څکوونکي د ژوند ګواښونکو ناروغیو د اخته کېدو ډېر لوړ خطر لري. د سګرټ څکولو تر ټولو جدي خطر د سږو، پښتورګو، د خولې د خالیګاه، لارینکس، تیو، مثانې، مرۍ، پانقراس او معدې سرطان دی.'),
      P('Tobacco smoke contains over 4,000 different chemicals. Out of these, there are more than 69 known carcinogens (cancer causing chemicals). The effects of some chemicals found in cigarettes are given below.',
        'تمباکو کے دھوئیں میں 4,000 سے زیادہ مختلف کیمیکلز ہوتے ہیں۔ ان میں سے 69 سے زیادہ معلوم کارسینوجنز (سرطان پیدا کرنے والے کیمیکلز) ہیں۔ سگریٹ میں پائے جانے والے کچھ کیمیکلز کے اثرات ذیل میں دیے گئے ہیں۔',
        'د تنباکو په لوګي کې له 4,000 څخه زیات بېلابېل کیمیاوي مواد شته. له دې جملې څخه له 69 څخه زیات پېژندل شوي کارسینوجنونه (سرطان پیدا کوونکي کیمیاوي مواد) دي. په سګرټو کې د موندل شویو ځینو کیمیاوي موادو اغېزې لاندې ورکړل شوې دي.', {bold: ['carcinogens']}),
      P('The majority of the particulate matter inhaled by a smoker is composed of tar. Within tar, there are many carcinogens. Tar in its solid form also stains the teeth and fingers of smokers. It can also stain and damage the lung tissue. Tar also increases the production of mucous and phlegm.',
        'تمباکو نوش جو ذراتی مادہ سانس کے ساتھ اندر لیتا ہے اس کا زیادہ تر حصہ ٹار پر مشتمل ہوتا ہے۔ ٹار میں بہت سے کارسینوجنز ہوتے ہیں۔ ٹار اپنی ٹھوس شکل میں تمباکو نوشوں کے دانتوں اور انگلیوں پر بھی داغ ڈالتا ہے۔ یہ پھیپھڑوں کی بافت پر بھی داغ ڈال سکتا ہے اور اسے نقصان پہنچا سکتا ہے۔ ٹار بلغم اور کف کی پیداوار بھی بڑھاتا ہے۔',
        'هغه ذروي مواد چې یو سګرټ څکوونکی یې په ساه کې اخلي ډېری برخه یې له تار څخه جوړه ده. په تار کې ډېر کارسینوجنونه شته. تار په خپل جامد حالت کې د سګرټ څکوونکو غاښونه او ګوتې هم داغي کوي. دا کولای شي د سږو نسج هم داغي او زیانمن کړي. تار د مخاط او بلغم تولید هم زیاتوي.', {bold: ['tar']}),
      P('Bad Social Effects of Smoking', 'تمباکو نوشی کے برے سماجی اثرات', 'د سګرټ څکولو بدې ټولنیزې اغېزې'),
      P('Breathing of smoke-laden air by nonsmokers is known as passive smoking. The majority of the nonsmokers are allergic to cigarette smoke as it produces irritation in their eyes and throats. They can also develop cancer by continuously living in an environment polluted with cigarette smoke. Moreover, people tend do not like the company of cigarette smokers due to the bad smell that comes from their mouth. For this reason there are separate zones in public places such as offices, hotels and restaurants for smokers. The Government has banned smoking at public places and on public transport.',
        'تمباکو نوشی نہ کرنے والوں کا دھوئیں سے بھری ہوا میں سانس لینا غیر فعال تمباکو نوشی (پیسو سموکنگ) کہلاتا ہے۔ تمباکو نوشی نہ کرنے والوں کی اکثریت کو سگریٹ کے دھوئیں سے الرجی ہوتی ہے کیونکہ یہ ان کی آنکھوں اور گلے میں جلن پیدا کرتا ہے۔ سگریٹ کے دھوئیں سے آلودہ ماحول میں مسلسل رہنے سے انہیں سرطان بھی ہو سکتا ہے۔ مزید یہ کہ لوگ تمباکو نوشوں کے منہ سے آنے والی بدبو کی وجہ سے ان کی صحبت پسند نہیں کرتے۔ اسی وجہ سے دفاتر، ہوٹلوں اور ریستورانوں جیسی عوامی جگہوں پر تمباکو نوشوں کے لیے الگ حصے ہوتے ہیں۔ حکومت نے عوامی مقامات اور پبلک ٹرانسپورٹ پر تمباکو نوشی پر پابندی لگا دی ہے۔',
        'د هغو کسانو له خوا چې سګرټ نه څکوي د لوګي ډکې هوا تنفس ته غیر فعال سګرټ څکول (پیسیو سموکنګ) ویل کېږي. د سګرټ نه څکوونکو ډېری کسان د سګرټو له لوګي سره حساسیت لري ځکه چې دا د دوی په سترګو او ستوني کې خارښت او سوزش پیدا کوي. دوی کولای شي د سګرټو په لوګي ککړ چاپېریال کې د دوامداره اوسېدو له امله سرطان ته هم اخته شي. سربېره پر دې، خلک د سګرټ څکوونکو د خولې د بد بوی له امله د هغوی ملګرتیا نه خوښوي. له همدې امله په عامه ځایونو لکه دفترونو، هوټلونو او رسټورانتونو کې د سګرټ څکوونکو لپاره جلا برخې شته. حکومت په عامه ځایونو او عامه ټرانسپورټ کې سګرټ څکول منع کړي دي.', {bold: ['passive smoking']}),
      P('Nicotine has many harmful effects such as increased heart rate and blood pressure, constriction in the blood vessels, damage to the muscles, and disturbance in hormonal systems and metabolism. Nicotine can also increase platelet stickiness in the blood which can cause blockage and cause coronary diseases.',
        'نکوٹین کے بہت سے نقصان دہ اثرات ہیں جیسے دل کی دھڑکن اور بلڈ پریشر میں اضافہ، خون کی نالیوں کا تنگ ہونا، عضلات کو نقصان، اور ہارمونی نظاموں اور میٹابولزم میں خلل۔ نکوٹین خون میں پلیٹ لیٹس کی چپچپاہٹ بھی بڑھا سکتی ہے جس سے رکاوٹ پیدا ہو سکتی ہے اور دل کی شریانوں (کورونری) کی بیماریاں ہو سکتی ہیں۔',
        'نیکوټین ډېرې زیانمنې اغېزې لري لکه د زړه د ضربان او د وینې د فشار زیاتوالی، د وینې د رګونو تنګېدل، عضلو ته زیان، او د هورموني سیسټمونو او میټابولیزم ګډوډي. نیکوټین کولای شي په وینه کې د پلېټلېټونو نښتونکی والی هم زیات کړي چې کېدای شي بندښت رامنځته کړي او د زړه د کرونري رګونو ناروغۍ پیدا کړي.', {bold: ['Nicotine']}),
      P('The World Health Organization has called the governments to stop tobacco advertisements to prevent young people to start smoking.',
        'عالمی ادارۂ صحت نے حکومتوں سے مطالبہ کیا ہے کہ نوجوانوں کو تمباکو نوشی شروع کرنے سے روکنے کے لیے تمباکو کے اشتہارات بند کیے جائیں۔',
        'د روغتیا نړیوال سازمان له حکومتونو غوښتي چې د تنباکو اعلانونه ودروي ترڅو ځوانان د سګرټ څکولو له پیل څخه وساتل شي.'),
      P('(Reference: Document number: WHO/NMH/PND/13.1)', '(حوالہ: دستاویز نمبر: WHO/NMH/PND/13.1)', '(مرجع: د سند شمېره: WHO/NMH/PND/13.1)', {bold: ['(Reference: Document number: WHO/NMH/PND/13.1)']}),
      P('Carbon monoxide is formed when a cigarette is lit. It combines with red blood cells and prevents oxygen transportation. When carbon monoxide enters the air ways, it stays along with other toxic chemicals contained in cigarette smoke. These toxins cause inflammation, impair lung functions, and increase the risk of lung diseases.',
        'کاربن مونو آکسائیڈ اس وقت بنتی ہے جب سگریٹ سلگایا جاتا ہے۔ یہ خون کے سرخ خلیوں کے ساتھ مل جاتی ہے اور آکسیجن کی ترسیل کو روکتی ہے۔ جب کاربن مونو آکسائیڈ ہوا کی نالیوں میں داخل ہوتی ہے تو یہ سگریٹ کے دھوئیں میں موجود دیگر زہریلے کیمیکلز کے ساتھ وہاں ٹھہر جاتی ہے۔ یہ زہریلے مادے سوزش پیدا کرتے ہیں، پھیپھڑوں کے افعال کو متاثر کرتے ہیں اور پھیپھڑوں کی بیماریوں کا خطرہ بڑھاتے ہیں۔',
        'کاربن مونو اکسایډ هغه وخت جوړېږي چې سګرټ بل شي. دا د وینې له سرو حجرو سره یوځای کېږي او د اکسیجن لېږد مخه نیسي. کله چې کاربن مونو اکسایډ د هوا لارو ته ننوځي، نو د سګرټ په لوګي کې د نورو زهرجنو کیمیاوي موادو سره هلته پاتې کېږي. دا زهرجن مواد التهاب پیدا کوي، د سږو دندې کمزورې کوي او د سږو د ناروغیو خطر زیاتوي.', {bold: ['Carbon monoxide']}),
      P('Benzene is a major component of cigarettes. It is a carcinogen and causes blood cancer (leukaemia). Similarly, formaldehyde present in cigarettes causes cancers and respiratory, skin and gastrointestinal problems.',
        'بینزین سگریٹ کا ایک بڑا جزو ہے۔ یہ کارسینوجن ہے اور خون کا سرطان (لیوکیمیا) پیدا کرتی ہے۔ اسی طرح سگریٹ میں موجود فارملڈی ہائیڈ سرطان اور سانس، جلد اور معدے و آنتوں کے مسائل پیدا کرتی ہے۔',
        'بنزین د سګرټو یوه لویه برخه ده. دا کارسینوجن دی او د وینې سرطان (لوکیمیا) پیدا کوي. همدارنګه په سګرټو کې موجود فارمالډیهایډ سرطانونه او تنفسي، پوستکي او هضمي ستونزې پیدا کوي.', {bold: ['Benzene', 'formaldehyde']}),
      P('Thirty different metals are also found in cigarette smoke, many of which have been linked to cancer. A few of the metals found are; Arsenic, Nickel, Cadmium, Chromium, and Lead. Radioactive compounds are also found in cigarettes, all of them are carcinogens.',
        'سگریٹ کے دھوئیں میں تیس مختلف دھاتیں بھی پائی جاتی ہیں، جن میں سے بہت سی کا تعلق سرطان سے پایا گیا ہے۔ پائی جانے والی چند دھاتیں یہ ہیں؛ آرسینک، نکل، کیڈمیم، کرومیم اور سیسہ۔ سگریٹ میں تابکار مرکبات بھی پائے جاتے ہیں، جو سب کے سب کارسینوجنز ہیں۔',
        'د سګرټو په لوګي کې دېرش بېلابېل فلزات هم موندل کېږي چې ډېری یې له سرطان سره تړلي ښودل شوي دي. ځینې موندل شوي فلزات دا دي؛ ارسنیک، نکل، کاډمیم، کرومیم او سرب. په سګرټو کې راډیواکتیف مرکبات هم موندل کېږي، چې ټول یې کارسینوجنونه دي.', {bold: ['metals', 'Radioactive compounds']}),
      P('10.4.1 Effect of Exercise on the Rate of Breathing', '10.4.1 ورزش کا سانس لینے کی شرح پر اثر', '10.4.1 د ساه اخیستلو پر کچه د تمرین اغېزه'),
      P('Under resting condition the rate of breathing is 15-20 times per minute. During exercise this rate increases instantly. This is due to the fact that more oxygen is required for the oxidation of glucose molecules to get more energy. As a result of this, more CO₂ is produced which thus accumulates in the blood.',
        'آرام کی حالت میں سانس لینے کی شرح 15-20 بار فی منٹ ہوتی ہے۔ ورزش کے دوران یہ شرح فوراً بڑھ جاتی ہے۔ اس کی وجہ یہ ہے کہ زیادہ توانائی حاصل کرنے کے لیے گلوکوز کے سالمات کی تکسید کے لیے زیادہ آکسیجن درکار ہوتی ہے۔ اس کے نتیجے میں زیادہ CO₂ پیدا ہوتی ہے جو یوں خون میں جمع ہو جاتی ہے۔',
        'د آرام په حالت کې د ساه اخیستلو کچه په یوه دقیقه کې 15-20 ځله ده. د تمرین پر مهال دا کچه سمدستي زیاتېږي. دا ځکه چې د زیاتې انرژۍ د ترلاسه کولو لپاره د ګلوکوز د مالیکولونو اکسیډیشن ته زیات اکسیجن اړین دی. د دې په پایله کې زیات CO₂ تولیدېږي چې په دې توګه په وینه کې راټولېږي.', {bold: ['15-20 times per minute']}),
      P('When this blood reaches the brain, the medulla (breathing centre) detects more carbon dioxide in the blood and sends nerve impulses to the diaphragm and rib muscles at greater speed. So the speed of contraction and relaxation of these muscles increases. It increases the rate and depth of breathing. During exercise, the breathing rate increases up to 30-40 times per minute.',
        'جب یہ خون دماغ تک پہنچتا ہے تو میڈولا (سانس کا مرکز) خون میں زیادہ کاربن ڈائی آکسائیڈ محسوس کرتا ہے اور ڈایافرام اور پسلیوں کے عضلات کو زیادہ رفتار سے عصبی پیغامات بھیجتا ہے۔ چنانچہ ان عضلات کے سکڑنے اور ڈھیلے ہونے کی رفتار بڑھ جاتی ہے۔ اس سے سانس لینے کی شرح اور گہرائی بڑھ جاتی ہے۔ ورزش کے دوران سانس لینے کی شرح 30-40 بار فی منٹ تک بڑھ جاتی ہے۔',
        'کله چې دا وینه دماغ ته ورسېږي، نو میډولا (د ساه اخیستلو مرکز) په وینه کې زیات کاربن ډای اکسایډ احساسوي او ډیافرام او د پښتیو عضلو ته په ډېره چټکۍ سره عصبي پیغامونه لېږي. نو د دې عضلو د تنګېدو او سستېدو چټکتیا زیاتېږي. دا د ساه اخیستلو کچه او ژوروالی زیاتوي. د تمرین پر مهال د ساه اخیستلو کچه په یوه دقیقه کې تر 30-40 ځله پورې زیاتېږي.', {bold: ['(breathing centre)', '30-40 times per minute']}),
      P('Proper Ventilation for Healthy Living', 'صحت مند زندگی کے لیے مناسب ہوا داری', 'د روغ ژوند لپاره مناسب هوا رسونه'),
      P('A home ventilation system is used to maintain a healthy living environment by supplying fresh air inside the home while at the same time removing stale and polluted air. Home ventilation also helps to maintain proper humidity levels. With insufficient home ventilation, pollutants can build up and become very concentrated. Proper home ventilation can help reduce allergy and asthma symptoms and help ease other respiratory disorders.',
        'گھر کا ہوا داری کا نظام گھر کے اندر تازہ ہوا مہیا کر کے اور ساتھ ہی باسی اور آلودہ ہوا کو نکال کر صحت مند رہائشی ماحول برقرار رکھنے کے لیے استعمال ہوتا ہے۔ گھر کی ہوا داری نمی کی مناسب سطح برقرار رکھنے میں بھی مدد دیتی ہے۔ گھر میں ناکافی ہوا داری سے آلودہ مادے جمع ہو کر بہت مرتکز ہو سکتے ہیں۔ گھر کی مناسب ہوا داری الرجی اور دمے کی علامات کم کرنے اور سانس کی دیگر بیماریوں میں آرام دینے میں مدد دے سکتی ہے۔',
        'د کور د هوا رسونې سیسټم د کور دننه د تازه هوا په رسولو او په ورته وخت کې د زړې او ککړې هوا په ایستلو سره د روغ ژوند چاپېریال د ساتلو لپاره کارول کېږي. د کور هوا رسونه د لندبل د مناسبې کچې په ساتلو کې هم مرسته کوي. د کور د ناکافي هوا رسونې په صورت کې ککړونکي مواد راټولېدای او ډېر غلیظ کېدای شي. د کور مناسبه هوا رسونه کولای شي د الرجۍ او ساه لنډۍ نښې کمې کړي او د نورو تنفسي ناروغیو په اسانولو کې مرسته وکړي.'),
      P('Activities', 'سرگرمیاں', 'فعالیتونه'),
      P('Morning walk is traditionally considered beneficial for health. Analyse this sentence in the context of better gaseous exchange.',
        'صبح کی سیر کو روایتی طور پر صحت کے لیے مفید سمجھا جاتا ہے۔ بہتر گیسی تبادلے کے تناظر میں اس جملے کا تجزیہ کیجیے۔',
        'د سهار ګرځېدل په دودیز ډول روغتیا ته ګټور ګڼل کېږي. د ګازونو د ښې تبادلې په تړاو د دې جملې شننه وکړئ.')
    ],
    layout: [{t: 'columns', sideWidth: 320, main: [0, 1, 2], side: [{t: 'box', kind: 'sts', headingIndex: 3, paras: [4]}]},
      {t: 'columns', sideWidth: 300, main: [5], side: [{t: 'box', kind: 'fyi', paras: [6, 7]}]}, 8, 9, 10, {t: 'fig', id: 'fig10-8'},
      {t: 'h', i: 11}, 12, 13, {t: 'box', kind: 'sts', headingIndex: 14, paras: [15]}, {t: 'table', id: 'table10-1'},
      {t: 'box', kind: 'activity', headingIndex: 16, paras: [17]}]
  };

  /* ---------- 10.5 Respiratory Disorders: printed pages 9-10 (PDF 12-13); printed 11-12 absent ---------- */
  figures['fig10-9'] = {
    id: 'fig10-9', widthRatio: 0.8,
    caption: L('Fig.10.9 Mucous in air ways accumulates and causes bronchitis', 'شکل 10.9 ہوا کی نالیوں میں بلغم جمع ہو کر برونکائٹس کا سبب بنتا ہے', 'شکل 10.9 د هوا په لارو کې مخاط راټولېږي او برونکایټس پیدا کوي'),
    labels: [L('Normal lung', 'نارمل پھیپھڑا', 'نورمال سږی'), L('and airway', 'اور ہوا کی نالی', 'او د هوا لاره'), L('Inflamed lung', 'سوجا ہوا پھیپھڑا', 'التهابي سږی'), L('Mucous', 'بلغم', 'مخاط')],
    svg: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 260" role="img" aria-label="Fig.10.9 Mucous in air ways accumulates and causes bronchitis" font-family="Segoe UI, Arial, sans-serif" font-size="11">
      <path d="M200 30 L200 110 M200 110 L170 140 M200 110 L230 140" stroke="#94a3b8" stroke-width="8" fill="none"/>
      <path d="M170 120 C130 120 120 190 135 230 L195 225 C200 190 195 150 170 120 z" fill="#fbcfe8"/><path d="M230 120 C275 120 285 190 270 230 L208 225 C202 190 205 150 230 120 z" fill="#f87171"/>
      <circle cx="90" cy="90" r="70" fill="#fff" stroke="#111" stroke-width="2"/><ellipse cx="90" cy="90" rx="38" ry="48" fill="#f9a8d4" stroke="#be185d" stroke-width="3"/><ellipse cx="90" cy="90" rx="26" ry="34" fill="#831843"/>
      <line x1="140" y1="140" x2="165" y2="190" stroke="#111"/>
      <circle cx="380" cy="90" r="70" fill="#fff" stroke="#111" stroke-width="2"/><ellipse cx="380" cy="90" rx="42" ry="50" fill="#f472b6" stroke="#9d174d" stroke-width="6"/><ellipse cx="380" cy="90" rx="16" ry="20" fill="#facc15" stroke="#a16207" stroke-width="4"/><ellipse cx="380" cy="90" rx="8" ry="10" fill="#451a03"/>
      <line x1="330" y1="140" x2="240" y2="190" stroke="#111"/>
      <line x1="388" y1="100" x2="430" y2="180" stroke="#111"/><text x="420" y="194">Mucous</text>
      <text x="70" y="226" fill="#e11d48">Normal lung</text><text x="70" y="240" fill="#e11d48">and airway</text>
      <text x="300" y="226" fill="#e11d48">Inflamed lung</text><text x="300" y="240" fill="#e11d48">and airway</text>
    </svg>`
  };
  figures['fig10-10'] = {
    id: 'fig10-10', widthRatio: 0.8,
    caption: L('Fig.10.10 Emphysema', 'شکل 10.10 ایمفیسیما', 'شکل 10.10 ایمفیزیما'),
    labels: [L('Normal bronchiole', 'نارمل برونکیول', 'نورمال برونکیول'), L('and alveoli', 'اور الویولائی', 'او الویولي'), L('Emphysema', 'ایمفیسیما', 'ایمفیزیما'), L('with dilation of the alveoli', 'الویولائی کے پھیلاؤ کے ساتھ', 'د الویولي له پراخېدو سره')],
    svg: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 250" role="img" aria-label="Fig.10.10 Emphysema" font-family="Segoe UI, Arial, sans-serif" font-size="11">
      <path d="M60 40 L60 90 M60 90 L40 110 M60 90 L80 110" stroke="#fca5a5" stroke-width="5" fill="none"/>
      <path d="M40 100 C15 100 15 160 25 180 L55 178 C58 150 55 120 40 100 z M80 100 C105 100 105 160 95 180 L65 178 C62 150 65 120 80 100 z" fill="#fbcfe8" stroke="#be185d"/>
      <circle cx="85" cy="150" r="4" fill="none" stroke="#111"/><line x1="85" y1="150" x2="70" y2="190" stroke="#111"/><ellipse cx="65" cy="210" rx="16" ry="22" fill="#fbcfe8" stroke="#9d174d"/>
      <ellipse cx="230" cy="110" rx="85" ry="100" fill="#fff" stroke="#111"/>
      <path d="M175 30 L230 90" stroke="#9f1239" stroke-width="10"/>
      <g fill="#dc2626" stroke="#7f1d1d"><circle cx="215" cy="115" r="14"/><circle cx="242" cy="110" r="14"/><circle cx="228" cy="138" r="14"/><circle cx="256" cy="135" r="14"/><circle cx="210" cy="145" r="14"/><circle cx="240" cy="162" r="14"/><circle cx="262" cy="160" r="12"/></g>
      <ellipse cx="410" cy="110" rx="85" ry="100" fill="#fff" stroke="#111"/>
      <path d="M355 30 L410 90" stroke="#9f1239" stroke-width="10"/>
      <g fill="#db2777" stroke="#831843"><path d="M380 110 C380 90 440 90 445 115 C450 150 430 175 405 172 C380 170 375 140 380 110 z"/></g>
      <g stroke="#831843" fill="none"><path d="M395 115 C410 130 420 120 432 140"/><path d="M392 145 C405 150 418 160 430 152"/></g>
      <line x1="232" y1="150" x2="232" y2="212" stroke="#111"/><text x="232" y="226" text-anchor="middle">Normal bronchiole</text><text x="232" y="240" text-anchor="middle">and alveoli</text>
      <line x1="412" y1="160" x2="420" y2="212" stroke="#111"/><text x="420" y="226" text-anchor="middle">Emphysema</text><text x="420" y="240" text-anchor="middle">with dilation of the alveoli</text>
    </svg>`
  };
  const t105 = {
    id: 'bio10-u10-t5', num: '10.5', title: 'Respiratory Disorders', urduTitle: 'نظامِ تنفس کی بیماریاں', pashtoTitle: 'تنفسي ناروغۍ',
    sourceReferences: [ref(12, 9), ref(13, 10)], translationStatus: 'authored_aligned_paragraphs', ...practice('10.4'),
    sourceGap: 'Printed pages 11 and 12 are missing from the local PDF and from every JPG scan (PDF page 13 is printed page 10; PDF page 14 is printed page 13). The rest of the pneumonia text, and any later disorders on those pages (the unit SLOs name asthma and lung cancer), cannot be verified and are not reconstructed.',
    figures: {'fig10-9': figures['fig10-9'], 'fig10-10': figures['fig10-10']},
    paras: [
      P('Sometime the normal functioning of the respiratory system is disrupted due to certain factors which can lead to serious respiratory disorders. Some of these disorders are discussed below.',
        'کبھی کبھی بعض عوامل کی وجہ سے نظامِ تنفس کا معمول کا کام متاثر ہو جاتا ہے جو سانس کی سنگین بیماریوں کا باعث بن سکتا ہے۔ ان میں سے کچھ بیماریوں پر ذیل میں بحث کی گئی ہے۔',
        'کله کله د ځینو عواملو له امله د تنفسي سیسټم عادي فعالیت ګډوډېږي چې کولای شي جدي تنفسي ناروغیو ته لاره هواره کړي. له دې ناروغیو څخه ځینې لاندې بیان شوې دي.'),
      P('1. Bronchitis', '1. برونکائٹس', '1. برونکایټس'),
      P('When the lining of the bronchi or bronchioles becomes inflamed or infected, this condition is called bronchitis. Bronchitis reduces the amount of air that can flow and causes formation of mucus in the airways. Bronchitis is caused by viruses, bacteria, and their particles that irritate the bronchial tubes.',
        'جب برونکائی یا برونکیولز کی اندرونی تہہ سوج جاتی ہے یا اس میں انفیکشن ہو جاتا ہے تو اس حالت کو برونکائٹس کہتے ہیں۔ برونکائٹس بہنے والی ہوا کی مقدار کم کر دیتا ہے اور ہوا کی نالیوں میں بلغم بننے کا سبب بنتا ہے۔ برونکائٹس وائرسوں، بیکٹیریا اور ان کے ذرات سے ہوتا ہے جو برونکیل نالیوں میں جلن پیدا کرتے ہیں۔',
        'کله چې د برونکای یا برونکیولونو دننۍ طبقه التهابي یا انتاني شي، نو دې حالت ته برونکایټس ویل کېږي. برونکایټس د بهېدونکې هوا اندازه کموي او د هوا په لارو کې د مخاط د جوړېدو لامل کېږي. برونکایټس د ویروسونو، باکتریاوو او د هغوی د ذرو له امله پیدا کېږي چې برونکیل نلونه خاروي.'),
      P('Short-term bronchitis resolves without treatment in two weeks. If conditions do not improve, the patient is given medicines. Antibiotics are used when bronchitis is due to bacterial infection. When bronchitis is due to viral infection, anti-viral medicines are used. Coughing helps to remove irritants from the bronchi.',
        'قلیل مدتی برونکائٹس دو ہفتوں میں علاج کے بغیر ٹھیک ہو جاتا ہے۔ اگر حالت بہتر نہ ہو تو مریض کو دوائیں دی جاتی ہیں۔ جب برونکائٹس بیکٹیریائی انفیکشن کی وجہ سے ہو تو اینٹی بائیوٹکس استعمال کی جاتی ہیں۔ جب برونکائٹس وائرل انفیکشن کی وجہ سے ہو تو اینٹی وائرل دوائیں استعمال کی جاتی ہیں۔ کھانسی برونکائی سے جلن پیدا کرنے والے مادوں کو نکالنے میں مدد دیتی ہے۔',
        'لنډمهاله برونکایټس پرته له درملنې په دوو اوونیو کې جوړېږي. که حالت ښه نه شي، ناروغ ته درمل ورکول کېږي. کله چې برونکایټس د باکتریايي انتان له امله وي انټي بیوټیک کارول کېږي. کله چې برونکایټس د ویروسي انتان له امله وي، ضد ویروس درمل کارول کېږي. ټوخی له برونکای څخه د خارښت پیدا کوونکو موادو په ایستلو کې مرسته کوي.'),
      P('2. Emphysema', '2. ایمفیسیما', '2. ایمفیزیما'),
      P('This is a severe type of lung disease in which due to extensive cough walls of the alveoli are damaged. Environmental pollution can cause emphysema. Cigarette smoke is the most common cause. The effects of emphysema are permanent and irreversible, however if smoking is stopped, further damage might be reduced.',
        'یہ پھیپھڑوں کی ایک شدید قسم کی بیماری ہے جس میں زیادہ کھانسی کی وجہ سے الویولائی کی دیواریں خراب ہو جاتی ہیں۔ ماحولیاتی آلودگی ایمفیسیما کا سبب بن سکتی ہے۔ سگریٹ کا دھواں اس کی سب سے عام وجہ ہے۔ ایمفیسیما کے اثرات مستقل اور ناقابلِ واپسی ہیں، تاہم اگر تمباکو نوشی ترک کر دی جائے تو مزید نقصان کم ہو سکتا ہے۔',
        'دا د سږو یو سخت ډول ناروغي ده چې په هغې کې د ډېر ټوخي له امله د الویولي دېوالونه زیانمن کېږي. چاپېریالي ککړتیا کولای شي ایمفیزیما پیدا کړي. د سګرټو لوګی یې تر ټولو عام لامل دی. د ایمفیزیما اغېزې دایمي او نه بېرته راګرځېدونکې دي، خو که سګرټ څکول ودرول شي، نور زیان کمېدای شي.'),
      P('3. Pneumonia', '3. نمونیا', '3. نمونیا'),
      P('Pneumonia is an inflammation in the lungs, due to infection in the alveoli. Due to pneumonia, the alveoli are filled with pus. It is caused by bacteria, viruses or fungi. General symptoms of pneumonia are cold (upper respiratory infection, for example, sneezing sore throat, cough), which […]',
        'نمونیا پھیپھڑوں میں سوزش ہے جو الویولائی میں انفیکشن کی وجہ سے ہوتی ہے۔ نمونیا کی وجہ سے الویولائی پیپ سے بھر جاتے ہیں۔ یہ بیکٹیریا، وائرسوں یا فنجائی سے ہوتا ہے۔ نمونیا کی عمومی علامات زکام (سانس کی بالائی نالی کا انفیکشن، مثلاً چھینکیں، گلے کی خراش، کھانسی) ہیں، جو […]',
        'نمونیا په سږو کې التهاب دی چې په الویولي کې د انتان له امله کېږي. د نمونیا له امله الویولي له زوو ډکېږي. دا د باکتریاوو، ویروسونو یا فنګسونو له امله پیدا کېږي. د نمونیا عمومي نښې ریزش (د تنفسي سیسټم د پورتنۍ برخې انتان، د بېلګې په توګه پرنجی، د ستوني درد، ټوخی) دي، چې […]'),
      P('Pneumonia can be transmitted by breathing in air with small droplets. These droplets get into the air when an infected person (having these germs) coughs or sneezes.',
        'نمونیا چھوٹے قطروں والی ہوا میں سانس لینے سے منتقل ہو سکتا ہے۔ یہ قطرے اس وقت ہوا میں شامل ہوتے ہیں جب کوئی متاثرہ شخص (جس میں یہ جراثیم ہوں) کھانستا یا چھینکتا ہے۔',
        'نمونیا د وړو څاڅکو لرونکې هوا په تنفس سره لېږدول کېدای شي. دا څاڅکي هغه وخت هوا ته ننوځي چې یو اخته کس (چې دا میکروبونه لري) ټوخی یا پرنجی وکړي.'),
      P('Source note: printed pages 11 and 12 of this unit are missing from the available scans, so the rest of this paragraph and the following disorders are not shown.',
        'ماخذ نوٹ: اس یونٹ کے مطبوعہ صفحات 11 اور 12 دستیاب اسکینز میں موجود نہیں، اس لیے اس پیراگراف کا باقی حصہ اور اس کے بعد کی بیماریاں نہیں دکھائی گئیں۔',
        'د سرچینې یادښت: د دې یونټ چاپي مخونه 11 او 12 په موجودو سکینونو کې نشته، نو د دې پراګراف پاتې برخه او ورپسې ناروغۍ نه دي ښودل شوې.')
    ],
    layout: [0, {t: 'h', i: 1}, 2, 3, {t: 'fig', id: 'fig10-9'}, {t: 'h', i: 4}, 5, {t: 'fig', id: 'fig10-10'}, {t: 'h', i: 6}, {t: 'columns', sideWidth: 280, main: [7], side: [{t: 'box', kind: 'fyi', paras: [8]}]}, {t: 'box', kind: 'note', heading: L('Source note (editorial)', 'ماخذ نوٹ (ادارتی)', 'د سرچینې یادښت (سمونیز)'), paras: [9]}]
  };

  /* ---------- Key Points: printed page 13 (PDF 14) ---------- */
  const kp = [
    ['For aerobic respiration, oxygen is required for the complete oxidation of food molecules while carbon dioxide is released as a by product.', 'ہوائی تنفس کے لیے خوراک کے سالمات کی مکمل تکسید کے لیے آکسیجن درکار ہوتی ہے جبکہ کاربن ڈائی آکسائیڈ ضمنی پیداوار کے طور پر خارج ہوتی ہے۔', 'د هوايي تنفس لپاره د خوراک د مالیکولونو بشپړ اکسیډیشن ته اکسیجن اړین دی په داسې حال کې چې کاربن ډای اکسایډ د ضمني محصول په توګه خوشې کېږي.'],
    ['Gaseous exchange means the exchange of oxygen and carbon dioxide between an organism and its environment.', 'گیسوں کے تبادلے سے مراد کسی جاندار اور اس کے ماحول کے درمیان آکسیجن اور کاربن ڈائی آکسائیڈ کا تبادلہ ہے۔', 'د ګازونو تبادله د یو ژوندي موجود او د هغه د چاپېریال ترمنځ د اکسیجن او کاربن ډای اکسایډ تبادلې ته ویل کېږي.'],
    ['Breathing is the physical process in which animals take air in and out of their body, to get oxygen from this air and to release carbon dioxide in it.', 'سانس لینا وہ طبعی عمل ہے جس میں جانور اپنے جسم میں ہوا اندر اور باہر لے جاتے ہیں، تاکہ اس ہوا سے آکسیجن حاصل کریں اور اس میں کاربن ڈائی آکسائیڈ خارج کریں۔', 'ساه اخیستل هغه فزیکي بهیر دی چې ځناور پکې هوا خپل بدن ته دننه او بهر وړي، ترڅو له دې هوا څخه اکسیجن واخلي او هغې ته کاربن ډای اکسایډ خوشې کړي.'],
    ['In plants, the gaseous exchange between the body and the environment occurs through the general surface, stomata and lenticels.', 'پودوں میں جسم اور ماحول کے درمیان گیسوں کا تبادلہ عمومی سطح، سٹومیٹا اور لینٹیسلز کے ذریعے ہوتا ہے۔', 'په بوټو کې د بدن او چاپېریال ترمنځ د ګازونو تبادله د عمومي سطحې، سټوماټا او لینټیسلونو له لارې ترسره کېږي.'],
    ['The air passageway consists of nostrils, nasal cavities, pharynx, larynx, trachea, bronchi and bronchioles.', 'ہوا کی گزرگاہ نتھنوں، ناک کے خلاؤں، فیرنکس، لیرنکس، ٹریکیا، برونکائی اور برونکیولز پر مشتمل ہے۔', 'د هوا لاره د پوزې له سوریو، د پوزې له خالیګاوو، فارینکس، لارینکس، ټراکیا، برونکای او برونکیولونو څخه جوړه ده.'],
    ['Through external nostrils, air enters into two nasal cavities, from where it goes into the pharynx and then into larynx or voice box.', 'بیرونی نتھنوں کے ذریعے ہوا ناک کے دو خلاؤں میں داخل ہوتی ہے، جہاں سے یہ فیرنکس اور پھر لیرنکس یا صوتی خانے میں جاتی ہے۔', 'د پوزې د بهرنیو سوریو له لارې هوا د پوزې دوو خالیګاوو ته ننوځي، له هغه ځایه فارینکس او بیا لارینکس یا د غږ صندوق ته ځي.'],
    ['The larynx opens into the trachea or wind pipe which divides into two bronchi. Each bronchus enters the lungs on its own side and divides and sub-divides into smaller bronchi and finally into bronchioles. Each bronchiole end at a duct which opens in a cluster of alveoli.', 'لیرنکس ٹریکیا یا ہوا کی نالی میں کھلتا ہے جو دو برونکائی میں تقسیم ہو جاتی ہے۔ ہر برونکس اپنی جانب کے پھیپھڑے میں داخل ہو کر تقسیم اور ذیلی تقسیم ہو کر چھوٹی برونکائی اور آخرکار برونکیولز بناتا ہے۔ ہر برونکیول ایک نالی پر ختم ہوتا ہے جو الویولائی کے ایک گچھے میں کھلتی ہے۔', 'لارینکس ټراکیا یا د هوا نل ته خلاصېږي چې په دوو برونکای وېشل کېږي. هر برونکس د خپل اړخ سږي ته ننوځي او په کوچنیو برونکای او په پای کې په برونکیولونو وېشل او فرعي وېشل کېږي. هر برونکیول په یوه نالۍ پای ته رسېږي چې د الویولي په یوه ټولګي کې خلاصېږي.'],
    ['The alveoli are very thin-walled and provide the surface for gaseous exchange. Their walls are covered with a network of blood capillaries where gaseous exchange occurs.', 'الویولائی بہت پتلی دیوار والے ہیں اور گیسوں کے تبادلے کے لیے سطح مہیا کرتے ہیں۔ ان کی دیواریں خون کی شعریات کے جال سے ڈھکی ہوتی ہیں جہاں گیسوں کا تبادلہ ہوتا ہے۔', 'الویولي ډېر نري دېوالونه لري او د ګازونو د تبادلې لپاره سطحه برابروي. د دوی دېوالونه د وینې د شعریه رګونو په جال پوښل شوي دي چې هلته د ګازونو تبادله کېږي.'],
    ['Each lung is enclosed in a double membrane called pleura which contains a pleural fluid.', 'ہر پھیپھڑا ایک دوہری جھلی میں بند ہوتا ہے جسے پلورا کہتے ہیں جس میں پلورل سیال ہوتا ہے۔', 'هر سږی په یوه دوه ګونې پرده کې ایسار دی چې پلورا ورته ویل کېږي او پلورل مایع لري.'],
    ['During inspiration, the muscles of the diaphragm contract, so it becomes flat. The intercostal muscles also contract, so the ribcage expands. In this way the volume of chest cavity increases, pressure on the lungs decreases and so the atmospheric air rushes in to the lungs.', 'انسپریشن کے دوران ڈایافرام کے عضلات سکڑتے ہیں، اس لیے یہ چپٹا ہو جاتا ہے۔ انٹرکوسٹل عضلات بھی سکڑتے ہیں، اس لیے پسلیوں کا پنجرہ پھیل جاتا ہے۔ اس طرح سینے کے خلا کا حجم بڑھتا ہے، پھیپھڑوں پر دباؤ کم ہوتا ہے اور یوں کرۂ ہوائی کی ہوا تیزی سے پھیپھڑوں میں داخل ہوتی ہے۔', 'د انسپیریشن پر مهال د ډیافرام عضلې تنګېږي، نو هوار کېږي. انټرکوسټل عضلې هم تنګېږي، نو د پښتیو قفس پراخېږي. په دې توګه د سینې د خالیګاه حجم زیاتېږي، پر سږو فشار کمېږي او د اتموسفیر هوا په چټکۍ سره سږو ته ننوځي.'],
    ['During expiration, the muscles of the ribs and the diaphragm relax. In this way, the volume of the chest cavity is decreased, pressure on lungs is increased and so the air is expelled out. Smokers have a much higher risk of developing life threatening diseases.', 'ایکسپریشن کے دوران پسلیوں اور ڈایافرام کے عضلات ڈھیلے ہو جاتے ہیں۔ اس طرح سینے کے خلا کا حجم کم ہو جاتا ہے، پھیپھڑوں پر دباؤ بڑھ جاتا ہے اور یوں ہوا باہر نکل جاتی ہے۔ تمباکو نوشوں میں جان لیوا بیماریاں لاحق ہونے کا خطرہ بہت زیادہ ہوتا ہے۔', 'د ایکسپیریشن پر مهال د پښتیو او ډیافرام عضلې سستېږي. په دې توګه د سینې د خالیګاه حجم کمېږي، پر سږو فشار زیاتېږي او هوا بهر ایستل کېږي. سګرټ څکوونکي د ژوند ګواښونکو ناروغیو ډېر لوړ خطر لري.'],
    ['Tobacco smoke contains more than 69 known carcinogens.', 'تمباکو کے دھوئیں میں 69 سے زیادہ معلوم کارسینوجنز ہوتے ہیں۔', 'د تنباکو په لوګي کې له 69 څخه زیات پېژندل شوي کارسینوجنونه شته.'],
    ['Tobacco contains tar which has many carcinogens. It also stains and damages the lung tissue.', 'تمباکو میں ٹار ہوتا ہے جس میں بہت سے کارسینوجنز ہوتے ہیں۔ یہ پھیپھڑوں کی بافت پر داغ بھی ڈالتا ہے اور اسے نقصان پہنچاتا ہے۔', 'تنباکو تار لري چې ډېر کارسینوجنونه لري. دا د سږو نسج هم داغي او زیانمن کوي.'],
    ['Nicotine has many harmful effects such as increased heart rate and blood pressure, constriction in the blood vessels, damage to the muscles, disturbance in hormonal system and metabolism.', 'نکوٹین کے بہت سے نقصان دہ اثرات ہیں جیسے دل کی دھڑکن اور بلڈ پریشر میں اضافہ، خون کی نالیوں کا تنگ ہونا، عضلات کو نقصان، ہارمونی نظام اور میٹابولزم میں خلل۔', 'نیکوټین ډېرې زیانمنې اغېزې لري لکه د زړه د ضربان او د وینې د فشار زیاتوالی، د وینې د رګونو تنګېدل، عضلو ته زیان، د هورموني سیسټم او میټابولیزم ګډوډي.'],
    ['Carbon monoxide is formed when a cigarette is lit. It combines with red blood cells and prevents oxygen transportation.', 'کاربن مونو آکسائیڈ اس وقت بنتی ہے جب سگریٹ سلگایا جاتا ہے۔ یہ خون کے سرخ خلیوں کے ساتھ مل کر آکسیجن کی ترسیل کو روکتی ہے۔', 'کاربن مونو اکسایډ هغه وخت جوړېږي چې سګرټ بل شي. دا د وینې له سرو حجرو سره یوځای کېږي او د اکسیجن لېږد مخه نیسي.'],
    ['Benzene (major component of cigarettes) is a carcinogen and causes blood cancer (leukaemia).', 'بینزین (سگریٹ کا بڑا جزو) کارسینوجن ہے اور خون کا سرطان (لیوکیمیا) پیدا کرتی ہے۔', 'بنزین (د سګرټو لویه برخه) کارسینوجن دی او د وینې سرطان (لوکیمیا) پیدا کوي.'],
    ['Under resting condition the rate of breathing is 15-20 times per minute. During exercise this rate increases up to 30-40 times per minute.', 'آرام کی حالت میں سانس لینے کی شرح 15-20 بار فی منٹ ہوتی ہے۔ ورزش کے دوران یہ شرح 30-40 بار فی منٹ تک بڑھ جاتی ہے۔', 'د آرام په حالت کې د ساه اخیستلو کچه په یوه دقیقه کې 15-20 ځله ده. د تمرین پر مهال دا کچه په یوه دقیقه کې تر 30-40 ځله زیاتېږي.'],
    ['When the lining of bronchi or bronchioles becomes inflamed or infected, the condition is called bronchitis.', 'جب برونکائی یا برونکیولز کی اندرونی تہہ سوج جاتی ہے یا اس میں انفیکشن ہو جاتا ہے تو اس حالت کو برونکائٹس کہتے ہیں۔', 'کله چې د برونکای یا برونکیولونو دننۍ طبقه التهابي یا انتاني شي، دې حالت ته برونکایټس ویل کېږي.'],
    ['In emphysema, the walls of the alveoli are damaged and the patient feels difficulty in breathing (shortness of breath). Pneumonia is an inflammation in the lungs, due to infection in the alveoli.', 'ایمفیسیما میں الویولائی کی دیواریں خراب ہو جاتی ہیں اور مریض کو سانس لینے میں دشواری (سانس پھولنا) محسوس ہوتی ہے۔ نمونیا پھیپھڑوں میں سوزش ہے جو الویولائی میں انفیکشن کی وجہ سے ہوتی ہے۔', 'په ایمفیزیما کې د الویولي دېوالونه زیانمن کېږي او ناروغ د ساه اخیستلو ستونزه (ساه لنډي) احساسوي. نمونیا په سږو کې التهاب دی چې په الویولي کې د انتان له امله کېږي.']
  ];
  const keyPoints = {
    id: 'bio10-u10-keypoints', num: 'Key Points', title: 'Key Points', urduTitle: 'اہم نکات', pashtoTitle: 'مهم ټکي',
    sourceReferences: [ref(14, 13)], translationStatus: 'authored_aligned_paragraphs', subtopics: [],
    paras: kp.map(([e, u, p]) => P(e, u, p)),
    layout: [{t: 'list', items: kp.map((_, i) => i)}]
  };

  /* ---------- Exercise: printed pages 14-15 (PDF 15-16). The book prints no answer key. ---------- */
  const opt = arr => arr.map(([e, u, p]) => P(e, u, p));
  const mcq = (q, options, ans) => Object.assign(P(...q), {options: opt(options), answer: P(`${'abcd'[ans]}. ${options[ans][0]}`, `${'abcd'[ans]}. ${options[ans][1]}`, `${'abcd'[ans]}. ${options[ans][2]}`), answerType: 'suggested'});
  chapter.sourceExercise = {
    title: L('Exercise', 'مشق', 'تمرین'),
    sourceReferences: [ref(15, 14), ref(16, 15)],
    groups: [
      {heading: L('A. Select the correct answer.', 'A. درست جواب منتخب کیجیے۔', 'A. سم ځواب وټاکئ.'), note: 'The textbook does not print an answer key; the answers shown are SpaceBook suggestions checked against the unit text.', questions: [
        mcq(['The correct order of the structures involved in the flow of air in the human body is:', 'انسانی جسم میں ہوا کے بہاؤ میں شامل ساختوں کی درست ترتیب ہے:', 'د انسان په بدن کې د هوا په بهیر کې د ښکېلو جوړښتونو سم ترتیب دا دی:'], [
          ['Pharynx — Trachea — Larynx — Bronchi — Bronchioles', 'فیرنکس — ٹریکیا — لیرنکس — برونکائی — برونکیولز', 'فارینکس — ټراکیا — لارینکس — برونکای — برونکیولونه'],
          ['Larynx — Pharynx — Trachea — Bronchioles — Bronchi', 'لیرنکس — فیرنکس — ٹریکیا — برونکیولز — برونکائی', 'لارینکس — فارینکس — ټراکیا — برونکیولونه — برونکای'],
          ['Trachea — Pharynx — Larynx — Bronchi — Bronchioles', 'ٹریکیا — فیرنکس — لیرنکس — برونکائی — برونکیولز', 'ټراکیا — فارینکس — لارینکس — برونکای — برونکیولونه'],
          ['Pharynx — Larynx — Trachea — Bronchi — Bronchioles', 'فیرنکس — لیرنکس — ٹریکیا — برونکائی — برونکیولز', 'فارینکس — لارینکس — ټراکیا — برونکای — برونکیولونه']], 3),
        mcq(['Food is prevented from entering into the Larynx by:', 'خوراک کو لیرنکس میں داخل ہونے سے روکا جاتا ہے:', 'خوراک لارینکس ته له ننوتلو څخه منع کېږي د:'], [['Glottis', 'گلوٹس', 'ګلوټس'], ['Epiglottis', 'ایپی گلوٹس', 'اپیګلوټس'], ['Vocal cards', 'صوتی تار (ووکل کارڈز)', 'غږیز تارونه (ووکل کارډز)'], ['Internal nostrils', 'اندرونی نتھنے', 'دنني د پوزې سوري']], 1),
        mcq(['Oxygen from the lungs enter into the blood due to:', 'پھیپھڑوں سے آکسیجن خون میں داخل ہوتی ہے:', 'له سږو څخه اکسیجن وینې ته ننوځي د دې له امله:'], [['Diffusion', 'انتشار (ڈفیوژن)', 'ډیفیوژن'], ['Less affinity of O₂ for air', 'ہوا کے لیے O₂ کی کم کشش', 'هوا ته د O₂ لږ میلان'], ['Higher affinity of CO₂ for air', 'ہوا کے لیے CO₂ کی زیادہ کشش', 'هوا ته د CO₂ زیات میلان'], ['Osmosis', 'اوسموسس', 'اوسموسس']], 0),
        mcq(['Which part of the air passageway is also called the windpipe?', 'ہوا کی گزرگاہ کا کون سا حصہ ہوا کی نالی (ونڈ پائپ) بھی کہلاتا ہے؟', 'د هوا د لارې کومه برخه د هوا نل (وینډ پایپ) هم بلل کېږي؟'], [['Bronchus', 'برونکس', 'برونکس'], ['Alveolus', 'الویولس', 'الویولس'], ['Larynx', 'لیرنکس', 'لارینکس'], ['Trachea', 'ٹریکیا', 'ټراکیا']], 3),
        mcq(['In which disease are the walls of the alveoli are broken?', 'کس بیماری میں الویولائی کی دیواریں ٹوٹ جاتی ہیں؟', 'په کومه ناروغۍ کې د الویولي دېوالونه ماتېږي؟'], [['Pneumonia', 'نمونیا', 'نمونیا'], ['Bronchitis', 'برونکائٹس', 'برونکایټس'], ['Emphysema', 'ایمفیسیما', 'ایمفیزیما'], ['Asthma', 'دمہ', 'ساه لنډي (استما)']], 2),
        mcq(['The diaphragm is flat, the ribs move out; this occurs during:', 'ڈایافرام چپٹا ہوتا ہے، پسلیاں باہر کی طرف حرکت کرتی ہیں؛ یہ ہوتا ہے:', 'ډیافرام هوار وي، پښتۍ بهر خوا حرکت کوي؛ دا پېښېږي د:'], [['Expiration', 'ایکسپریشن کے دوران', 'ایکسپیریشن پر مهال'], ['Inspiration', 'انسپریشن کے دوران', 'انسپیریشن پر مهال'], ['Lungs expansion', 'پھیپھڑوں کے پھیلاؤ کے دوران', 'د سږو د پراخېدو پر مهال'], ['Breathing', 'سانس لینے کے دوران', 'د ساه اخیستلو پر مهال']], 1),
        mcq(['The chest cavity is separated from the abdominal cavity by a muscle called:', 'سینے کا خلا پیٹ کے خلا سے ایک عضلے کے ذریعے الگ ہوتا ہے جسے کہتے ہیں:', 'د سینې خالیګاه د ګېډې له خالیګاه څخه د یوې عضلې په واسطه جلا کېږي چې نوم یې دی:'], [['Larynx', 'لیرنکس', 'لارینکس'], ['Trachea', 'ٹریکیا', 'ټراکیا'], ['Bronchus', 'برونکس', 'برونکس'], ['Diaphragm', 'ڈایافرام', 'ډیافرام']], 3),
        mcq(['Respiration at cellular level is known as:', 'خلوی سطح پر تنفس کہلاتا ہے:', 'په حجروي کچه تنفس بلل کېږي:'], [['Breathing', 'سانس لینا', 'ساه اخیستل'], ['Ventilation', 'ہوا داری (وینٹیلیشن)', 'هوا رسونه (وینټیلیشن)'], ['Oxidation', 'تکسید', 'اکسیډیشن'], ['Inhalation', 'سانس اندر لینا', 'ساه دننه اخیستل']], 2),
        mcq(['High fever, cold and cough with sputum production are symptoms of:', 'تیز بخار، زکام اور بلغم کے ساتھ کھانسی علامات ہیں:', 'لوړه تبه، ریزش او له بلغم سره ټوخی نښې دي د:'], [['Emphysema', 'ایمفیسیما', 'ایمفیزیما'], ['Asthma', 'دمہ', 'ساه لنډي (استما)'], ['Pneumonia', 'نمونیا', 'نمونیا'], ['Bronchitis', 'برونکائٹس', 'برونکایټس']], 2),
        mcq(['Chemotherapy is a treatment of:', 'کیموتھراپی علاج ہے:', 'کیموتراپي درملنه ده د:'], [['Emphysema', 'ایمفیسیما کا', 'ایمفیزیما'], ['Bronchitis', 'برونکائٹس کا', 'برونکایټس'], ['Asthma', 'دمے کا', 'ساه لنډۍ'], ['Lung cancer', 'پھیپھڑوں کے سرطان کا', 'د سږو سرطان']], 3)
      ]},
      {heading: L('B. Write short answers to the following questions.', 'B. درج ذیل سوالات کے مختصر جوابات لکھیے۔', 'B. لاندې پوښتنو ته لنډ ځوابونه ولیکئ.'), questions: [
        P('Why do plants not need a specialised respiratory system?', 'پودوں کو مخصوص نظامِ تنفس کی ضرورت کیوں نہیں ہوتی؟', 'ولې بوټي ځانګړي تنفسي سیسټم ته اړتیا نه لري؟'),
        P('Differentiate between the terms “respiration” and “breathing”.', '“تنفس” اور “سانس لینا” کی اصطلاحات میں فرق بیان کیجیے۔', 'د “تنفس” او “ساه اخیستلو” اصطلاحاتو ترمنځ توپیر وکړئ.'),
        P('How are the surface area of leaves and lungs important for gaseous exchange?', 'پتوں اور پھیپھڑوں کا سطحی رقبہ گیسوں کے تبادلے کے لیے کیسے اہم ہے؟', 'د پاڼو او سږو سطحي مساحت د ګازونو د تبادلې لپاره څنګه مهم دی؟'),
        P('What is the function of the cartilage present in the walls of the trachea and bronchi?', 'ٹریکیا اور برونکائی کی دیواروں میں موجود غضروف کا کیا کام ہے؟', 'د ټراکیا او برونکای په دېوالونو کې د موجود غضروف دنده څه ده؟'),
        P('What is a diaphragm and what is its role in breathing?', 'ڈایافرام کیا ہے اور سانس لینے میں اس کا کیا کردار ہے؟', 'ډیافرام څه شی دی او په ساه اخیستلو کې یې رول څه دی؟'),
        P('What are carcinogens? Name any two carcinogens present in tobacco.', 'کارسینوجنز کیا ہیں؟ تمباکو میں موجود کوئی سے دو کارسینوجنز کے نام لکھیے۔', 'کارسینوجنونه څه دي؟ په تنباکو کې د موجودو هر دوو کارسینوجنونو نومونه واخلئ.'),
        P('Compare the composition of inhaled and exhaled air.', 'اندر لی گئی اور باہر نکالی گئی ہوا کی ترکیب کا موازنہ کیجیے۔', 'د دننه اخیستل شوې او بهر ایستل شوې هوا جوړښت پرتله کړئ.')
      ]},
      {heading: L('C. Write detailed answers to the following questions:', 'C. درج ذیل سوالات کے تفصیلی جوابات لکھیے:', 'C. لاندې پوښتنو ته مفصل ځوابونه ولیکئ:'), questions: [
        P('The gaseous exchange in plants is important for photosynthesis and respiration. Explain the types of gases exchanged and its mechanism.', 'پودوں میں گیسوں کا تبادلہ ضیائی تالیف اور تنفس کے لیے اہم ہے۔ تبادلہ ہونے والی گیسوں کی اقسام اور اس کا طریقۂ کار بیان کیجیے۔', 'په بوټو کې د ګازونو تبادله د فوتوسنتیز او تنفس لپاره مهمه ده. د تبادله کېدونکو ګازونو ډولونه او د هغې میکانیزم تشریح کړئ.'),
        P('Describe the mechanism of breathing in human beings.', 'انسانوں میں سانس لینے کا طریقۂ کار بیان کیجیے۔', 'په انسانانو کې د ساه اخیستلو میکانیزم بیان کړئ.'),
        P('Draw a diagram of the air passage in the human body and describe the role of different parts in the flow of air through it.', 'انسانی جسم میں ہوا کی گزرگاہ کی شکل بنائیے اور اس میں ہوا کے بہاؤ میں مختلف حصوں کا کردار بیان کیجیے۔', 'د انسان په بدن کې د هوا د لارې انځور جوړ کړئ او د هغې له لارې د هوا په بهیر کې د بېلابېلو برخو رول بیان کړئ.'),
        P('What are the causes of respiratory disorders such as bronchitis, pneumonia and lung cancer?', 'سانس کی بیماریوں جیسے برونکائٹس، نمونیا اور پھیپھڑوں کے سرطان کی وجوہات کیا ہیں؟', 'د تنفسي ناروغیو لکه برونکایټس، نمونیا او د سږو سرطان لاملونه کوم دي؟')
      ]},
      {heading: L('Activities', 'سرگرمیاں', 'فعالیتونه'), questions: [
        P('Investigate the effect of light on the net gaseous exchange from a leaf, by using bicarbonate as the indicator.', 'بائی کاربونیٹ کو انڈیکیٹر کے طور پر استعمال کرتے ہوئے پتے سے خالص گیسی تبادلے پر روشنی کے اثر کی تحقیق کیجیے۔', 'د بای کاربونیټ د شاخص په توګه په کارولو سره د پاڼې له خالص ګازي تبادلې باندې د رڼا اغېزه وڅېړئ.'),
        P('Investigate the breathing rate at rest and after exercise.', 'آرام کی حالت میں اور ورزش کے بعد سانس لینے کی شرح کی تحقیق کیجیے۔', 'د آرام په حالت کې او له تمرین وروسته د ساه اخیستلو کچه وڅېړئ.'),
        P('Find out how much air a person can take into his lungs.', 'معلوم کیجیے کہ ایک شخص اپنے پھیپھڑوں میں کتنی ہوا لے سکتا ہے۔', 'معلوم کړئ چې یو کس خپلو سږو ته څومره هوا اخیستلای شي.'),
        P('Demonstrate through experiment, that carbon dioxide is exhaled during respiration.', 'تجربے کے ذریعے ثابت کیجیے کہ تنفس کے دوران کاربن ڈائی آکسائیڈ باہر نکالی جاتی ہے۔', 'د تجربې له لارې وښایاست چې د تنفس پر مهال کاربن ډای اکسایډ بهر ایستل کېږي.')
      ]}
    ]
  };

  chapter.topics = [intro, t101, t102, t103, t104, t105, keyPoints];
  chapter.sourceReview = {status: 'reviewed-with-unresolved', sourcePdf: PDF, lastFullyVerifiedPdfPage: 16, nextPdfPage: 17, complete: false, note: 'printed pages 11-12 are missing from the available scans'};
  chapter.topics.forEach(t => {
    if (!t.paras) return;
    t.text = t.paras.map(p => p.text).join('\n\n');
    t.summary = {en: t.text, ur: t.paras.map(p => p.urdu).join('\n\n'), ps: t.paras.map(p => p.pashto).join('\n\n')};
  });
})();
