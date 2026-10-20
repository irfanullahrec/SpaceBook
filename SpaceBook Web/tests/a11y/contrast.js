'use strict';
/* The contrast tool (tools/a11y_contrast.js): ratios, what counts as failing, what the automatic fix does. node tests/a11y/contrast.js */
const c = require('../../tools/a11y_contrast');
let passed = 0, failed = 0;
const check = (name, ok, extra) => { if (ok) passed++; else { failed++; console.log('FAIL  ' + name + (extra ? ' : ' + extra : '')); } };
const near = (a, b) => Math.abs(a - b) < 0.02;

check('black on white is 21:1', near(c.ratio([0, 0, 0], [255, 255, 255]), 21));
check('white on white is 1:1', near(c.ratio([255, 255, 255], [255, 255, 255]), 1));
check('#767676 on white is the well-known 4.54:1', near(c.ratio(c.parseColor('#767676'), [255, 255, 255]), 4.54));
check('colours are read as #rgb, #rrggbb, rgb() and names', JSON.stringify([c.parseColor('#fff'), c.parseColor('#0284c7'), c.parseColor('rgb(2, 132, 199)'), c.parseColor('white')]) === JSON.stringify([[255, 255, 255], [2, 132, 199], [2, 132, 199], [255, 255, 255]]));
check('a translucent colour, var() and gradients are not judged (unknown background)', c.parseColor('rgba(0,0,0,.5)') === null && c.judge('color: var(--x); background: #fff') === null && c.judge('color:#fff;background:linear-gradient(#000,#111)') === null);
check('white on #16a34a fails (3.3:1)', (() => { const f = c.judge('color:#fff;background:#16a34a'); return f && f.ratio === 3.3 && f.need === 4.5; })());
check('white on #15803d passes', c.judge('color:#fff;background:#15803d') === null);
check('large text needs only 3:1', c.judge('color:#fff;background:#16a34a;font-size:1.6rem') === null && c.judge('color:#fff;background:#16a34a;font-size:1.2rem;font-weight:700') === null);
check('large text below 3:1 still fails', c.judge('color:#fff;background:#10b981;font-size:2rem') !== null);
check('a block without both colours is not judged', c.judge('color:#777') === null && c.judge('background:#fff') === null);

const f = c.judge('background: #16a34a; color: #fff; padding: 2px');
const x = c.fixDecl(f);
check('the fix darkens the pill and keeps white text', x && x.target === 'bg' && c.ratio(c.parseColor('#fff'), c.parseColor(x.to)) >= 4.5 && /color: #fff/.test(x.decl), JSON.stringify(x));
check('the fix touches the colour only', x && x.decl.replace(/#[0-9a-f]{3,6}/g, '#') === 'background: #; color: #; padding: 2px');
const g = c.judge('color:#dc2626 !important;background:#fee2e2');
const y = c.fixDecl(g);
check('dark text on a light background: the text is darkened, "!important" stays', y && y.target === 'fg' && /color:#[0-9a-f]{6} !important/.test(y.decl) && c.ratio(c.parseColor(y.to), c.parseColor('#fee2e2')) >= 4.5, JSON.stringify(y));
check('the fixed hue stays the same (a green stays green)', (() => { const p = c.parseColor(x.to); return p[1] > p[0] && p[1] > p[2]; })());

console.log(`contrast tool tests: ${passed} passed, ${failed} failed`);
process.exit(failed ? 1 : 0);
