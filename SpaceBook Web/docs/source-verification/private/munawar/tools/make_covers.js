/* Draws the cover of every Munawar (Kanz) book: our own flat vector artwork, in the proportions of the Government covers (about 380 x 520).
 *
 *   node docs/source-verification/private/munawar/tools/make_covers.js            writes PNGs to the folder given by COVER_TMP (default: os temp)
 *   python docs/source-verification/private/munawar/tools/make_covers.py           runs this, then turns the PNGs into covers/Munawar/<subject id>.webp
 *
 * Needs Playwright (SpaceBook Web/node_modules) and Chrome or Edge. Nothing of the publisher's artwork or logo is used: the cover says
 * the book's name, its class and "Munawar - Kanz Series".
 */
'use strict';
const fs = require('fs');
const os = require('os');
const path = require('path');

const HERE = __dirname;
const books = JSON.parse(fs.readFileSync(path.join(HERE, '..', 'books.json'), 'utf8')).books;
const OUT = process.env.COVER_TMP || path.join(os.tmpdir(), 'munawar_covers');
fs.mkdirSync(OUT, { recursive: true });

// theme -> [top colour, bottom colour, accent, title colour]
const THEMES = {
  math: ['#fb7185', '#f97316', '#fde047', '#be123c'],
  english: ['#38bdf8', '#2563eb', '#fde047', '#1d4ed8'],
  grammar: ['#a78bfa', '#7c3aed', '#fcd34d', '#6d28d9'],
  urdu: ['#4ade80', '#16a34a', '#fde047', '#166534'],
  urdugrammar: ['#2dd4bf', '#0d9488', '#fde047', '#115e59'],
  islamiyat: ['#34d399', '#047857', '#fcd34d', '#065f46'],
  gk: ['#fdba74', '#ea580c', '#fef08a', '#9a3412'],
  prelim: ['#7dd3fc', '#0284c7', '#fef08a', '#075985'],
  waqf: ['#fcd34d', '#d97706', '#ffffff', '#92400e'],
  computer: ['#818cf8', '#4338ca', '#67e8f9', '#3730a3'],
  science: ['#67e8f9', '#0891b2', '#bef264', '#155e75'],
  sst: ['#fda4af', '#be185d', '#fde68a', '#9d174d'],
};
const TITLE = {
  math: 'Mathematics', english: 'English', grammar: 'English Grammar', urdu: 'Urdu', urdugrammar: 'Urdu Grammar', islamiyat: 'Islamiyat',
  gk: 'General Knowledge', prelim: 'Preliminary Knowledge', waqf: 'Waqfiyat-e-Aama', computer: 'Computer', science: 'Science', sst: 'Social Studies',
};

const star = (cx, cy, r, fill) => {
  const pts = [];
  for (let i = 0; i < 10; i++) { const a = -Math.PI / 2 + i * Math.PI / 5; const rr = i % 2 ? r * 0.45 : r; pts.push((cx + rr * Math.cos(a)).toFixed(1) + ',' + (cy + rr * Math.sin(a)).toFixed(1)); }
  return `<polygon points="${pts.join(' ')}" fill="${fill}"/>`;
};
const tile = (x, y, w, fill, text, tc, fs, rot) =>
  `<g transform="rotate(${rot || 0} ${x + w / 2} ${y + w / 2})"><rect x="${x}" y="${y}" width="${w}" height="${w}" rx="14" fill="${fill}" stroke="#fff" stroke-width="4"/><text x="${x + w / 2}" y="${y + w * 0.7}" text-anchor="middle" font-size="${fs}" font-weight="800" fill="${tc}" font-family="Arial Rounded MT Bold,Segoe UI,Arial,sans-serif">${text}</text></g>`;
const pencil = (x, y, rot, c) =>
  `<g transform="translate(${x} ${y}) rotate(${rot})"><rect x="0" y="0" width="16" height="96" rx="3" fill="${c}"/><rect x="0" y="0" width="16" height="14" rx="3" fill="#fda4af"/><polygon points="0,96 16,96 8,118" fill="#fde68a"/><polygon points="5,108 11,108 8,118" fill="#334155"/></g>`;

const ART = {
  math: () => tile(34, 78, 76, '#ef4444', '1', '#fff', 56, -8) + tile(120, 56, 84, '#facc15', '2', '#92400e', 62, 4) + tile(216, 80, 80, '#8b5cf6', '3', '#fff', 58, 8) +
    ['+', '−', '×', '÷'].map((s, i) => `<circle cx="${62 + i * 82}" cy="198" r="28" fill="#fff" stroke="#fde047" stroke-width="5"/><text x="${62 + i * 82}" y="209" text-anchor="middle" font-size="34" font-weight="800" fill="#be123c" font-family="Arial,sans-serif">${s}</text>`).join('') +
    star(330, 60, 18, '#fde047'),
  english: () => tile(40, 100, 78, '#f59e0b', 'A', '#fff', 56, -10) + tile(130, 80, 84, '#22c55e', 'B', '#fff', 60, 3) + tile(226, 104, 78, '#ef4444', 'C', '#fff', 56, 9) +
    pencil(318, 70, 18, '#facc15') + `<path d="M40 214 q150 -40 300 0" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round" stroke-dasharray="2 14"/>`,
  grammar: () => `<rect x="38" y="52" width="196" height="118" rx="26" fill="#fff"/><polygon points="80,168 70,206 112,170" fill="#fff"/>` +
    `<text x="136" y="132" text-anchor="middle" font-size="76" font-weight="800" fill="#6d28d9" font-family="Georgia,serif">Aa</text>` +
    `<rect x="240" y="90" width="110" height="82" rx="20" fill="#fde047"/><text x="295" y="150" text-anchor="middle" font-size="52" font-weight="800" fill="#7c2d12" font-family="Georgia,serif">?!</text>` +
    pencil(300, 126, 28, '#34d399') + `<rect x="56" y="200" width="150" height="9" rx="4" fill="#fff" opacity=".85"/><rect x="56" y="222" width="110" height="9" rx="4" fill="#fff" opacity=".6"/>`,
  urdu: () => ['ا', 'ب', 'پ'].map((c, i) => `<g transform="rotate(${[-8, 3, 9][i]} ${86 + i * 100} 130)"><rect x="${46 + i * 100}" y="${[86, 66, 90][i]}" width="82" height="92" rx="16" fill="${['#f59e0b', '#fff', '#ef4444'][i]}" stroke="#fff" stroke-width="4"/><text x="${87 + i * 100}" y="${[152, 132, 156][i]}" text-anchor="middle" font-size="70" font-weight="700" fill="${['#fff', '#166534', '#fff'][i]}" font-family="Noto Nastaliq Urdu,Jameel Noori Nastaleeq,Urdu Typesetting,Segoe UI,serif">${c}</text></g>`).join('') +
    `<path d="M40 214 q70 -30 140 0 t140 0" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round"/>` + star(336, 56, 16, '#fde047'),
  urdugrammar: () => `<rect x="40" y="56" width="300" height="142" rx="24" fill="#fff"/>` +
    `<text x="190" y="140" text-anchor="middle" font-size="62" font-weight="700" fill="#115e59" font-family="Noto Nastaliq Urdu,Jameel Noori Nastaleeq,Urdu Typesetting,Segoe UI,serif">اسم · فعل</text>` +
    `<rect x="70" y="162" width="240" height="8" rx="4" fill="#99f6e4"/>` + pencil(320, 110, 24, '#fb923c') + star(52, 218, 14, '#fde047'),
  islamiyat: () => `<circle cx="190" cy="112" r="92" fill="#fff" opacity=".2"/>` +
    `<rect x="104" y="136" width="172" height="86" rx="6" fill="#fff"/><path d="M118 136 a72 72 0 0 1 144 0z" fill="#fde68a"/><rect x="186" y="62" width="8" height="30" fill="#fde047"/><path d="M200 60 a14 14 0 1 1 -10 -15 a11 11 0 1 0 10 15z" fill="#fde047"/>` +
    `<rect x="64" y="104" width="30" height="118" rx="6" fill="#fff"/><polygon points="64,104 94,104 79,64" fill="#fde68a"/><rect x="286" y="104" width="30" height="118" rx="6" fill="#fff"/><polygon points="286,104 316,104 301,64" fill="#fde68a"/>` +
    `<path d="M174 222 v-40 a16 16 0 0 1 32 0 v40z" fill="#047857"/>` + star(70, 50, 12, '#fde047') + star(318, 44, 10, '#fde047'),
  gk: () => `<circle cx="170" cy="128" r="88" fill="#38bdf8" stroke="#fff" stroke-width="6"/>` +
    `<path d="M120 80 q30 -16 52 4 q-6 24 -30 26 q-14 18 -26 4z M178 130 q36 -6 50 18 q-10 34 -38 40 q-16 -18 -12 -58z M96 150 q18 6 20 28 q-18 4 -26 -12z" fill="#4ade80"/>` +
    `<circle cx="270" cy="184" r="42" fill="#fff" fill-opacity=".25" stroke="#fff" stroke-width="9"/><line x1="300" y1="214" x2="342" y2="256" stroke="#7c2d12" stroke-width="14" stroke-linecap="round"/>` + star(324, 62, 16, '#fde047'),
  prelim: () => `<circle cx="300" cy="64" r="34" fill="#fde047"/>` + Array.from({ length: 8 }, (_, i) => `<line x1="300" y1="64" x2="${300 + 50 * Math.cos(i * Math.PI / 4)}" y2="${64 + 50 * Math.sin(i * Math.PI / 4)}" stroke="#fde047" stroke-width="6" stroke-linecap="round"/>`).join('') +
    `<circle cx="300" cy="64" r="34" fill="#fde047"/><circle cx="150" cy="132" r="72" fill="#22c55e" stroke="#fff" stroke-width="6"/><path d="M100 118 q24 -14 42 4 q-4 22 -26 24z M158 150 q30 -4 40 16 q-8 26 -32 30z" fill="#bbf7d0"/>` +
    `<rect x="236" y="168" width="14" height="52" fill="#16a34a"/><circle cx="243" cy="158" r="22" fill="#ef4444"/><circle cx="243" cy="158" r="9" fill="#fde047"/>`,
  waqf: () => `<circle cx="150" cy="130" r="74" fill="#38bdf8" stroke="#fff" stroke-width="6"/><path d="M104 108 q26 -14 44 4 q-6 22 -26 24z M158 140 q30 -4 40 16 q-8 26 -32 30z" fill="#4ade80"/>` +
    `<path d="M290 70 a46 46 0 1 1 -2 0 q-16 18 -4 52 h-24 q8 -34 -6 -50 a46 46 0 0 1 36 -2z" fill="#fde047" stroke="#fff" stroke-width="5"/><rect x="262" y="146" width="40" height="10" rx="4" fill="#fff"/><rect x="268" y="160" width="28" height="10" rx="4" fill="#fff"/>` +
    star(60, 60, 14, '#fff') + star(334, 210, 12, '#fff'),
  computer: () => `<rect x="76" y="44" width="228" height="140" rx="16" fill="#fff"/><rect x="90" y="58" width="200" height="112" rx="8" fill="#22d3ee"/>` +
    `<rect x="104" y="74" width="72" height="14" rx="4" fill="#fff" opacity=".8"/><rect x="104" y="96" width="120" height="10" rx="4" fill="#fff" opacity=".6"/><circle cx="252" cy="130" r="22" fill="#fde047"/>` +
    `<rect x="170" y="184" width="40" height="22" fill="#e2e8f0"/><rect x="132" y="204" width="116" height="12" rx="6" fill="#fff"/>` +
    `<rect x="64" y="226" width="200" height="30" rx="8" fill="#e0e7ff"/>` + Array.from({ length: 10 }, (_, i) => `<rect x="${72 + i * 19}" y="232" width="14" height="8" rx="2" fill="#6366f1"/>`).join('') +
    `<ellipse cx="312" cy="240" rx="22" ry="16" fill="#fff"/><line x1="312" y1="224" x2="312" y2="240" stroke="#6366f1" stroke-width="3"/>`,
  science: () => `<path d="M150 54 h40 v52 l50 92 a20 20 0 0 1 -18 30 h-104 a20 20 0 0 1 -18 -30 l50 -92z" fill="#fff" fill-opacity=".92" stroke="#fff" stroke-width="5"/>` +
    `<path d="M126 176 h88 l30 52 h-148z" fill="#a3e635"/><circle cx="170" cy="190" r="7" fill="#fff"/><circle cx="192" cy="204" r="5" fill="#fff"/><circle cx="160" cy="212" r="4" fill="#fff"/>` +
    `<rect x="144" y="46" width="52" height="12" rx="5" fill="#0e7490"/>` +
    `<g transform="translate(300 90)"><ellipse rx="52" ry="18" fill="none" stroke="#fde047" stroke-width="5"/><ellipse rx="52" ry="18" fill="none" stroke="#fde047" stroke-width="5" transform="rotate(60)"/><ellipse rx="52" ry="18" fill="none" stroke="#fde047" stroke-width="5" transform="rotate(-60)"/><circle r="10" fill="#fff"/></g>` +
    `<path d="M70 120 q-30 -40 10 -66 q40 30 -10 66z" fill="#4ade80"/>`,
  sst: () => `<rect x="50" y="108" width="82" height="118" rx="6" fill="#fff"/><rect x="146" y="76" width="90" height="150" rx="6" fill="#fde68a"/><rect x="250" y="120" width="80" height="106" rx="6" fill="#fff"/>` +
    [66, 94].map(x => [124, 152, 180].map(y => `<rect x="${x}" y="${y}" width="16" height="16" rx="3" fill="#fb7185"/>`).join('')).join('') +
    [162, 192].map(x => [92, 122, 152, 182].map(y => `<rect x="${x}" y="${y}" width="18" height="18" rx="3" fill="#be185d" opacity=".8"/>`).join('')).join('') +
    `<rect x="268" y="136" width="44" height="40" rx="4" fill="#fb7185"/><line x1="190" y1="76" x2="190" y2="36" stroke="#fff" stroke-width="5"/><path d="M190 38 h42 l-12 14 l12 14 h-42z" fill="#16a34a"/>` +
    `<path d="M300 64 a22 22 0 0 1 22 22 c0 22 -22 40 -22 40 s-22 -18 -22 -40 a22 22 0 0 1 22 -22z" fill="#ef4444" stroke="#fff" stroke-width="4"/><circle cx="300" cy="86" r="8" fill="#fff"/>`,
};

function cover(b) {
  const [c1, c2, acc, ink] = THEMES[b.theme];
  const title = TITLE[b.theme] + (b.code === 'compbl' ? ' (Bilingual)' : '');
  const long = title.length > 11;          // two lines of 44px; shorter titles are one line of 50-56px
  const urdu = b.nameUrdu;
  return `<!doctype html><meta charset="utf-8"><style>
  *{box-sizing:border-box;margin:0;padding:0}
  body{width:380px;height:520px;overflow:hidden;font-family:"Arial Rounded MT Bold","Segoe UI",Arial,sans-serif}
  .c{position:relative;width:380px;height:520px;background:linear-gradient(180deg,${c1} 0%,${c2} 100%);overflow:hidden}
  .c:before{content:"";position:absolute;left:-60px;right:-60px;bottom:-130px;height:330px;border-radius:50%;background:rgba(255,255,255,.18)}
  .c:after{content:"";position:absolute;left:-30px;top:-70px;width:200px;height:200px;border-radius:50%;background:rgba(255,255,255,.12)}
  .top{position:absolute;top:16px;left:0;right:0;text-align:center;z-index:2}
  .kanz{display:inline-block;padding:5px 18px;border-radius:999px;background:#fff;color:${ink};font-size:15px;font-weight:800;letter-spacing:.14em;text-transform:uppercase}
  .title{position:absolute;top:56px;left:18px;right:18px;text-align:center;color:#fff;font-weight:900;line-height:1.02;font-size:${long ? 44 : (title.length >= 10 ? 50 : 56)}px;text-shadow:0 3px 0 ${ink},0 5px 12px rgba(0,0,0,.25);z-index:2}
  .ur{position:absolute;top:${long ? 170 : 130}px;left:0;right:0;text-align:center;font-size:30px;color:${acc};direction:rtl;font-family:"Noto Nastaliq Urdu","Jameel Noori Nastaleeq","Urdu Typesetting","Segoe UI",serif;text-shadow:0 2px 0 ${ink};z-index:2}
  .art{position:absolute;left:0;top:${long ? 190 : 150}px;width:380px;height:260px;z-index:1}
  .badge{position:absolute;right:16px;top:${long ? 176 : 118}px;width:74px;height:74px;border-radius:50%;background:#fff;border:6px solid ${acc};display:flex;flex-direction:column;align-items:center;justify-content:center;color:${ink};box-shadow:0 6px 14px rgba(0,0,0,.25);z-index:3;line-height:1}
  .badge span{font-size:10px;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
  .badge b{font-size:38px;font-weight:900;margin-top:1px}
  .foot{position:absolute;left:0;right:0;bottom:0;height:62px;background:#fff;display:flex;align-items:center;justify-content:center;gap:12px;color:${ink};z-index:2;border-top:5px solid ${acc}}
  .m{width:36px;height:36px;border-radius:11px;background:${ink};display:grid;place-items:center}
  .foot b{font-size:20px;letter-spacing:.04em}
  .foot small{display:block;font-size:11px;font-weight:700;opacity:.75;letter-spacing:.1em;text-transform:uppercase}
  </style><div class="c">
  <div class="top"><span class="kanz">Kanz</span></div>
  <div class="title">${title}</div>
  <div class="ur" lang="ur">${urdu}</div>
  <svg class="art" viewBox="0 0 380 260" xmlns="http://www.w3.org/2000/svg">${ART[b.theme]()}</svg>
  <div class="badge"><span>Class</span><b>${b.cls}</b></div>
  <div class="foot"><div class="m"><svg viewBox="0 0 48 48" width="26" height="26"><path d="M12 35V14l12 13 12-13v21" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg></div><div><b>Munawar</b><small>Kanz Series</small></div></div>
  </div>`;
}

(async () => {
  const { chromium } = require(path.join(HERE, '..', '..', '..', '..', '..', 'node_modules', 'playwright'));
  let browser;
  try { browser = await chromium.launch({ channel: 'msedge' }); } catch (e) { browser = await chromium.launch(); }
  const page = await browser.newPage({ viewport: { width: 380, height: 520 }, deviceScaleFactor: 2 });
  for (const b of books) {
    await page.setContent(cover(b), { waitUntil: 'load' });
    await page.screenshot({ path: path.join(OUT, b.subjectId + '.png') });
  }
  await browser.close();
  console.log('wrote', books.length, 'covers to', OUT);
})().catch(e => { console.error(e); process.exit(1); });
