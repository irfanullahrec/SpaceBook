/* SpaceBook animated tutor: Class 12 Maths, Unit 2, Exercise 2.1, Question 3(a)  f(x)=x^2+1, g(x)=2x, find f(g(x)).
 * Self-contained and scoped (.sbt). Launched from the "Animated explanation" button that app.js renders only for the
 * step group flagged tutor:"comp3a". One authoritative step index (Tutor.i); every change goes through go(). */
(function (root) {
  'use strict';
  const CANCEL = { cancelled: true };
  const SPEEDS = { slow: 2500, normal: 1500, fast: 700 };
  const COLORS = { blue: '#2563eb', orange: '#ea580c', purple: '#7c3aed', green: '#16a34a' };
  const reduced = () => !!(root.matchMedia && root.matchMedia('(prefers-reduced-motion: reduce)').matches);
  const tex = s => root.katex.renderToString(s, { trust: true, throwOnError: false, output: 'html', strict: 'ignore' });
  const C = (cls, t) => `\\htmlClass{${cls}}{${t}}`;
  let uid = 0;

  const css = `
.sbt{position:relative;margin:.35rem 0 .7rem;border:1px solid #cbd5e1;border-radius:12px;background:#fff;color:#0f172a;white-space:normal;overflow-wrap:normal;line-height:1.4;font-size:.95rem;overflow:clip}
.sbt *{box-sizing:border-box}
.sbt-head{display:flex;flex-wrap:wrap;align-items:center;gap:.5rem .75rem;padding:.5rem .8rem;background:#f8fafc;border-bottom:1px solid #e2e8f0}
.sbt-q{background:#027cba;color:#fff;font-weight:700;border-radius:6px;padding:.1rem .5rem;font-size:.8rem}
.sbt-given{font-size:.92rem;flex:1 1 auto}
.sbt-dots{display:flex;align-items:center;gap:.3rem}
.sbt-dot{width:22px;height:22px;border-radius:50%;border:1.5px solid #94a3b8;background:#fff;color:#475569;font-size:.7rem;font-weight:700;cursor:pointer;padding:0}
.sbt-dot.on{background:#027cba;border-color:#027cba;color:#fff}
.sbt-dot.seen{background:#dcfce7;border-color:#16a34a;color:#166534}
.sbt-x{border:0;background:transparent;font-size:1.1rem;cursor:pointer;color:#64748b;padding:0 .25rem}
.sbt-area{position:relative;padding:46px 1rem 10px;min-height:240px;font-size:1.3rem;overflow-x:auto}
.sbt-line{display:block;padding:.18rem .4rem;margin:.08rem 0;border-radius:6px;transition:opacity .35s,transform .35s,background .4s}
.sbt-row{display:grid;grid-template-columns:19rem minmax(0,1fr);column-gap:1.4rem;align-items:center}
.sbt-row.arcs{margin-top:.9rem}
.sbt-note{font-size:.82rem;color:#64748b;white-space:normal}
.sbt-lines.compact .sbt-row{font-size:.78em}
.sbt-line.hid{opacity:0;transform:translateY(8px)}
.sbt-line.muted{opacity:.55;font-size:.85em}
.sbt-cols{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.4rem 1.2rem}
.sbt-col h4{margin:0 0 .2rem;font-size:.78rem;font-weight:700;color:#475569;letter-spacing:.02em}
.sbt-svg{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;overflow:visible}
.sbt-chip{position:absolute;left:0;top:0;z-index:3;padding:.05rem .45rem;border-radius:7px;font-weight:700;font-size:1.05rem;color:#fff;box-shadow:0 3px 10px rgba(0,0,0,.25);pointer-events:none;white-space:nowrap}
.sbt-bubble{position:absolute;z-index:3;transform:translate(-50%,-100%);padding:.1rem .5rem;border-radius:7px;color:#fff;font-size:.85rem;font-weight:700;white-space:nowrap;animation:sbtPop .35s ease-out}
.sbt .katex .hl-blue,.sbt .katex .hl-orange,.sbt .katex .hl-purple,.sbt .katex .hl-green{display:inline-block;border-radius:5px;padding:0 .08em;margin:0 -.04em}
.sbt .katex .hl-blue{background:#dbeafe;box-shadow:0 0 0 2px #60a5fa;color:#1d4ed8}
.sbt .katex .hl-orange{background:#ffedd5;box-shadow:0 0 0 2px #fb923c;color:#c2410c}
.sbt .katex .hl-purple{background:#ede9fe;box-shadow:0 0 0 2px #a78bfa;color:#6d28d9}
.sbt .katex .hl-green{background:#dcfce7;box-shadow:0 0 0 2px #4ade80;color:#15803d}
.sbt .katex .pulse{animation:sbtPulse .8s ease-in-out 2}
.sbt .katex .gone{opacity:.15}
.sbt .katex [class^="k-"],.sbt .katex [class*=" k-"]{display:inline-block}
.sbt .katex [class*="k-slot"]{min-width:2.6em;height:1.05em;border-bottom:2px dashed #94a3b8;vertical-align:-.1em}
.sbt .katex .ul-blue{border-bottom:3px solid #2563eb}.sbt .katex .ul-orange{border-bottom:3px solid #ea580c}
.sbt .katex .zoom{animation:sbtZoom 1s ease-in-out 2;position:relative;z-index:2}
.sbt-line.final{background:#dcfce7;box-shadow:inset 3px 0 0 #16a34a}
.sbt-explain{padding:.55rem .9rem;border-top:1px solid #e2e8f0;background:#fcfdff;min-height:76px}
.sbt-explain h5{margin:0 0 .15rem;font-size:.92rem;color:#0f172a}
.sbt-explain p{margin:0;font-size:.88rem;color:#334155}
.sbt-explain b.b{color:#1d4ed8}.sbt-explain b.o{color:#c2410c}.sbt-explain b.p{color:#6d28d9}.sbt-explain b.g{color:#15803d}
.sbt-nav{position:sticky;bottom:env(safe-area-inset-bottom,0);z-index:5;display:flex;flex-wrap:wrap;align-items:center;gap:.4rem;padding:.5rem .7rem;background:rgba(255,255,255,.97);border-top:1px solid #cbd5e1;box-shadow:0 -4px 10px rgba(15,23,42,.06)}
.sbt-nav button,.sbt-nav select{font:inherit;font-size:.85rem;border:1px solid #cbd5e1;background:#fff;border-radius:999px;padding:.32rem .85rem;cursor:pointer;color:#0f172a}
.sbt-nav button.primary{background:#027cba;border-color:#027cba;color:#fff;font-weight:700}
.sbt-nav button:disabled{opacity:.45;cursor:default}
.sbt-nav .sp{flex:1 1 auto}
.sbt-nav label{font-size:.78rem;color:#475569;display:flex;align-items:center;gap:.3rem}
@keyframes sbtZoom{0%,100%{transform:scale(1)}50%{transform:scale(1.7)}}
@keyframes sbtPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.18)}}
@keyframes sbtPop{from{opacity:0;transform:translate(-50%,-70%) scale(.8)}to{opacity:1;transform:translate(-50%,-100%) scale(1)}}
@media (max-width:640px){.sbt-row{grid-template-columns:1fr;row-gap:0}.sbt-note{padding-left:.4rem}.sbt-area{font-size:1.05rem;padding:30px .5rem 8px}.sbt-cols{grid-template-columns:1fr}.sbt-nav .sp{display:none}}
@media (prefers-reduced-motion:reduce){.sbt .katex .pulse,.sbt-bubble{animation:none}.sbt-line{transition:none}}`;

  // The derivation is written row by row, exactly as a teacher would. A row exists from step `first`; `tex[k]` is its
  // state after step k (-1 = given), `pre` its blank state while it is being written, `view[i]` an override at step i.
  const T3 = `=${C('k-br', `(${C('k-fa', '2')}${C('k-fb', 'x')})`)}^{${C('k-ex', '2')}}+1`;
  const BLANK = n => C('k-slot' + n, '\\ \\ \\ \\ \\ \\ ');
  const ROWS = [
    { id: 'f', first: 0, tex: { '-1': `${C('k-fx', 'f(x)')}=${C('k-fr', 'x^2+1')}` }, note: 'f: the outer function' },
    { id: 'g', first: 0, tex: { '-1': `${C('k-gx', 'g(x)')}=${C('k-g2', '2x')}` }, note: 'g: the inner function' },
    { id: 'c1', first: 0, hideAt: 5, tex: { 0: `f(${C('k-gg', 'g(x)')})=\\,?` }, note: 'g(x) goes inside f' },
    { id: 'c2', first: 1, hideAt: 5, pre: `=f(${BLANK('')})`, tex: { 1: `=f(${C('k-in', '2x')})` }, note: 'the input of f is now 2x' },
    { id: 'c3', first: 2, hideAt: 5, arcsFrom: 4, pre: `=${BLANK('2')}`, tex: { 2: `=${C('k-rb', 'x')}^2+1`, 3: T3 }, note: 'f squares its input, then adds 1' },
    { id: 'c4', first: 4, hideAt: 5, tex: { 4: `=${C('k-p1', '2^2')}\\times ${C('k-p2', 'x^2')}+1` }, note: '(ab)ⁿ = aⁿ · bⁿ' },
    { id: 'c5', first: 4, final: 1, tex: { 4: `=${C('k-four', '4')}x^2+1` }, view: { 5: `f(g(x))=4${C('k-sx', 'x')}^2+1` }, note: '2² = 4' },
    { id: 'x3', first: 5, tex: { 5: `x=${C('k-three', '3')}` }, note: 'now put x = 3' },
    { id: 's1', first: 5, tex: { 5: `=4(${C('k-t1', '3')})^{${C('k-e1', '2')}}+1` }, note: '3 replaces x' },
    { id: 's2', first: 5, tex: { 5: `=${C('k-m1', '4\\times 9')}+1` }, note: '3² = 9' },
    { id: 's3', first: 5, tex: { 5: `=${C('k-m2', '36')}+1` }, note: '4 × 9 = 36' },
    { id: 's4', first: 5, final: 1, tex: { 5: `=${C('k-r', '37')}` }, note: '36 + 1 = 37' },
    { id: 'chk', first: 5, tex: { 5: `f(g(3))=f(6)=6^2+1=37` }, note: 'check: the same value ✓' }
  ];

  const STEPS = [
    { dot: 'Write', title: 'Step 1 · Write what we need',
      html: 'We want <b>f(g(x))</b>. The part inside the bracket, <b class="b">g(x)</b>, is the inner function: it is worked out first and then fed into f.',
      async play(w) {
        const R = w.R;
        await w.t(0.25); w.write(R.c1); await w.t(0.7);
        w.cls(w.q(R.c1, 'k-gg'), 'hl-blue ul-blue zoom');
      } },
    { dot: 'Bring g', title: 'Step 2 · Bring g(x) into f( )',
      html: 'f( ) needs an input. g(x) equals <b class="b">2x</b> (see the given line), so <b class="b">2x</b> travels from g(x) = 2x into the bracket of f, giving <b>f(2x)</b>.',
      async play(w) {
        const R = w.R, gg = w.q(R.c1, 'k-gg'), g2 = w.q(R.g, 'k-g2');
        w.cls(gg, 'hl-blue ul-blue');
        await w.t(0.25); w.write(R.c2); await w.t(0.6);
        const slot = w.q(R.c2, 'k-slot');
        w.arrow(gg, slot, COLORS.orange, { from: 'bottom', to: 'top', side: 'right', bend: 50 });
        await w.t(0.8);
        w.arrow(gg, g2, COLORS.purple, { from: 'top', to: 'bottom', side: 'right', bend: 60 });
        await w.t(0.8);
        w.cls(g2, 'hl-blue ul-blue zoom'); await w.t(0.9);
        const a3 = w.arrow(g2, slot, COLORS.blue, { from: 'bottom', to: 'top', side: 'right', bend: 110 });
        await w.t(0.5);
        await w.fly('2x', a3, COLORS.blue, 1);
        w.clearOverlay(); w.setTex(R.c2, ROWS[3].tex[1]);
        w.cls(w.q(R.c2, 'k-in'), 'hl-blue ul-blue zoom');
      } },
    { dot: 'Bring f', title: 'Step 3 · Bring the rule of f',
      html: 'Next, f( ) must be replaced by its rule. The rule is given by f(x) = <b class="o">x² + 1</b>, so <b class="o">x² + 1</b> travels from the given line into the empty place.',
      async play(w) {
        const R = w.R, fx = w.q(R.f, 'k-fx'), fr = w.q(R.f, 'k-fr'), slot = w.q(R.c3, 'k-slot2');
        await w.t(0.25); w.write(R.c3); await w.t(0.6);
        w.arrow(fx, fr, COLORS.purple, { from: 'top', to: 'top', bend: -60 });
        await w.t(0.8);
        w.cls(fr, 'hl-orange ul-orange zoom'); await w.t(0.9);
        const a = w.arrow(fr, slot, COLORS.orange, { from: 'bottom', to: 'top', side: 'right', bend: 150 });
        await w.t(0.5);
        await w.fly('x²+1', a, COLORS.orange, 1);
        w.clearOverlay(); w.setTex(R.c3, ROWS[4].tex[2]);
        w.cls(w.q(R.c3, 'k-rb'), 'hl-orange zoom');
      } },
    { dot: 'Replace x', title: 'Step 4 · Replace x by 2x',
      html: 'Wherever f has <b class="o">x</b>, put the input <b class="b">2x</b>. Because the x was squared, the whole bracket <b>(2x)</b> is squared: f(2x) = <b>(2x)² + 1</b>.',
      async play(w) {
        const R = w.R, inn = w.q(R.c2, 'k-in'), rb = w.q(R.c3, 'k-rb');
        w.cls(inn, 'hl-blue ul-blue zoom'); w.cls(rb, 'hl-orange pulse'); await w.t(0.9);
        const a = w.arrow(inn, rb, COLORS.blue, { from: 'bottom', to: 'top', side: 'right', bend: 70 });
        await w.t(0.5);
        await w.fly('2x', a, COLORS.blue, 1);
        w.clearOverlay(); w.setTex(R.c3, T3);
        const ex = w.q(R.c3, 'k-ex'); ex.style.opacity = '0';
        w.cls(w.q(R.c3, 'k-br'), 'hl-blue zoom'); await w.t(0.9);
        ex.style.opacity = ''; w.cls(ex, 'hl-purple zoom');
      } },
    { dot: 'Simplify', title: 'Step 5 · Distribute the square, then simplify',
      html: 'The power <b class="p">2</b> belongs to the whole bracket, so it applies to <b>both factors</b>: (ab)<sup>n</sup> = a<sup>n</sup>b<sup>n</sup>. Then <b class="p">2² = 4</b> and x² stays.',
      async play(w) {
        const R = w.R, ex = w.q(R.c3, 'k-ex'), fa = w.q(R.c3, 'k-fa'), fb = w.q(R.c3, 'k-fb');
        await w.t(0.2); w.cls(ex, 'hl-purple pulse'); await w.t(0.4);
        w.arrow(ex, fa, COLORS.purple, { bend: -70, from: 'top', to: 'top' });
        w.arrow(ex, fb, COLORS.purple, { bend: -46, from: 'top', to: 'top' });
        w.cls(fa, 'hl-orange pulse'); w.cls(fb, 'hl-orange pulse');
        await w.t(0.9); w.clearOverlay();
        w.write(R.c4); await w.t(0.7);
        const p1 = w.q(R.c4, 'k-p1'), four = w.q(R.c5, 'k-four');
        w.cls(p1, 'hl-orange ul-orange zoom'); await w.t(0.9);
        const a = w.arrow(p1, four, COLORS.purple, { bend: 60 });
        await w.t(0.4);
        await w.fly('4', a, COLORS.purple, 1);
        w.write(R.c5); w.cls(four, 'hl-green zoom'); w.clearOverlay();
      } },
    { dot: 'x = 3', title: 'Step 6 · Put x = 3 and calculate',
      html: 'Now <b class="b">3</b> replaces x: <b>4(3)² + 1</b>. Square first (3² = 9), then multiply (4 × 9 = 36), then add 1: the value is <b class="g">37</b>. Checking f(g(3)) = f(6) = 6² + 1 gives the same 37.',
      async play(w) {
        const R = w.R, sx = w.q(R.c5, 'k-sx');
        await w.t(0.25); w.write(R.x3); const three = w.q(R.x3, 'k-three');
        w.cls(three, 'hl-blue ul-blue zoom'); w.cls(sx, 'hl-orange pulse'); await w.t(0.9);
        const a = w.arrow(three, sx, COLORS.blue, { from: 'top', to: 'bottom', side: 'right', bend: 60 });
        await w.t(0.5);
        await w.fly('3', a, COLORS.blue, 1);
        w.clearOverlay(); w.write(R.s1); w.cls(w.q(R.s1, 'k-t1'), 'hl-blue zoom'); await w.t(0.9);
        w.cls(w.q(R.s1, 'k-e1'), 'hl-purple zoom'); await w.t(0.8);
        w.write(R.s2); w.cls(w.q(R.s2, 'k-m1'), 'hl-purple zoom'); await w.t(1);
        w.write(R.s3); w.cls(w.q(R.s3, 'k-m2'), 'hl-purple zoom'); await w.t(1);
        w.write(R.s4); w.cls(w.q(R.s4, 'k-r'), 'hl-green zoom'); await w.t(0.8);
        w.write(R.chk);
      } }
  ];

  class Tutor {
    constructor(host) {
      this.host = host; this.i = 0; this.run = 0; this.my = 0; this.seen = new Set(); this.speed = 'normal';
      this.id = 'sbt' + (++uid); this.build(); this.go(0);
    }
    build() {
      if (!document.getElementById('sbt-style')) { const s = document.createElement('style'); s.id = 'sbt-style'; s.textContent = css; document.head.appendChild(s); }
      this.host.innerHTML =
        `<div class="sbt" id="${this.id}"><div class="sbt-head"><span class="sbt-q">Q3 (a)</span>
        <span class="sbt-given">${tex('f(x)=x^2+1,\\ \\ g(x)=2x \\ \\Rightarrow\\ f(g(x))=\\,?')}</span>
        <span class="sbt-dots">${STEPS.map((s, k) => `<button type="button" class="sbt-dot" data-k="${k}" title="${s.dot}" aria-label="${s.title}">${k + 1}</button>`).join('')}</span>
        </div>
        <div class="sbt-area"><svg class="sbt-svg"><defs></defs></svg><div class="sbt-lines"></div></div>
        <div class="sbt-explain" aria-live="polite"><h5></h5><p></p></div>
        <div class="sbt-nav"><button type="button" data-act="prev">◀ Previous</button><button type="button" data-act="replay">↻ Replay Animation</button>
        <button type="button" class="primary" data-act="next">Next Step ▶</button><button type="button" data-act="full" aria-pressed="false">☰ All steps</button><span class="sp"></span>
        <label>Speed <select data-act="speed"><option value="slow">Slow</option><option value="normal" selected>Normal</option><option value="fast">Fast</option></select></label></div></div>`;
      this.el = this.host.firstElementChild;
      this.area = this.el.querySelector('.sbt-area'); this.svg = this.el.querySelector('.sbt-svg'); this.box = this.el.querySelector('.sbt-lines');
      this.el.addEventListener('click', e => {
        const b = e.target.closest('button'); if (!b) return;
        if (b.dataset.k != null) return this.go(+b.dataset.k);
        const a = b.dataset.act;
        if (a === 'prev') this.go(this.i - 1);
        else if (a === 'next') this.go(this.i === STEPS.length - 1 ? 0 : this.i + 1);
        else if (a === 'replay') this.go(this.i);
        else if (a === 'full') { const f = this.host.parentElement.querySelector('[data-sbt-full]'); if (f) { const on = f.style.display === 'none'; f.style.display = on ? 'grid' : 'none'; b.setAttribute('aria-pressed', String(on)); } }
      });
      this.el.querySelector('select').addEventListener('change', e => { this.speed = e.target.value; this.go(this.i); });
    }
    close() { this.run++; this.host.innerHTML = ''; this.host.hidden = true; if (this.btn) this.btn.setAttribute('aria-expanded', 'false'); }
    go(i) {
      this.i = Math.max(0, Math.min(i, STEPS.length - 1));
      const my = ++this.run;
      this.box.innerHTML = ''; this.R = {}; this.clearOverlay();
      ROWS.forEach(L => { if ((L.hideAt != null && this.i >= L.hideAt) || L.first > this.i) return; this.R[L.id] = this.row(L, this.texAt(L, this.i), L.first === this.i); }); this.area.querySelectorAll('.sbt-chip,.sbt-bubble').forEach(n => n.remove());
      const st = STEPS[this.i];
      this.el.querySelector('.sbt-explain h5').textContent = st.title;
      this.el.querySelector('.sbt-explain p').innerHTML = st.html;
      this.el.querySelectorAll('.sbt-dot').forEach((d, k) => { d.classList.toggle('on', k === this.i); d.classList.toggle('seen', k !== this.i && this.seen.has(k)); });
      const last = this.i === STEPS.length - 1, nx = this.el.querySelector('[data-act="next"]');
      nx.textContent = last ? '↻ Replay Solution' : 'Next Step ▶';
      this.el.querySelector('[data-act="prev"]').disabled = this.i === 0;
      this.seen.add(this.i);
      const w = Object.create(this); w.my = my;
      (async () => { try { await st.play(w); } catch (e) { if (e !== CANCEL) console.error('sbt', e); } })();
    }
    // ---- helpers (called on the per-run context w) ----
    chk() { if (this.run !== this.my) throw CANCEL; }
    async t(f) { this.chk(); if (!reduced()) await new Promise(r => setTimeout(r, SPEEDS[this.speed] * f)); this.chk(); }
    texAt(L, i) {
      if (L.view && L.view[i] !== undefined) return L.view[i];
      let best = null;
      Object.keys(L.tex).map(Number).forEach(k => { if (k < i && (best === null || k > best)) best = k; });
      if (best !== null) return L.tex[best];
      return L.pre || L.tex[i];
    }
    row(L, t, hid) {
      const d = document.createElement('div');
      d.className = 'sbt-row sbt-line' + (hid ? ' hid' : '') + (L.final && !hid ? ' final' : '') + (L.arcsFrom != null && this.i >= L.arcsFrom ? ' arcs' : '');
      d.dataset.final = L.final ? '1' : '';
      d.innerHTML = `<div class="sbt-eq">${tex(t)}</div><div class="sbt-note">${L.note || ''}</div>`;
      this.box.appendChild(d); return d;
    }
    setTex(row, t) { row.querySelector('.sbt-eq').innerHTML = tex(t); }
    write(row) {
      this.chk(); row.classList.remove('hid'); if (row.dataset.final) row.classList.add('final');
      if (!reduced() && row.animate) row.animate([{ clipPath: 'inset(0 100% 0 0)' }, { clipPath: 'inset(0 0 0 0)' }], { duration: SPEEDS[this.speed] * 0.4, easing: 'steps(16,end)' });
    }
    lines(spec) {
      return spec.map(s => {
        const d = document.createElement('div');
        d.className = 'sbt-line' + (s.hide ? ' hid' : '') + (s.muted ? ' muted' : '') + (s.final && !s.hide ? ' final' : '');
        d.dataset.final = s.final ? '1' : '';
        d.innerHTML = tex(s.t); this.box.appendChild(d); return d;
      });
    }
    cols(spec) {
      const g = document.createElement('div'); g.className = 'sbt-cols'; this.box.appendChild(g);
      return spec.map(([h, rows]) => {
        const c = document.createElement('div'); c.className = 'sbt-col'; c.innerHTML = `<h4>${h}</h4>`; g.appendChild(c);
        return rows.map(t => { const d = document.createElement('div'); d.className = 'sbt-line hid'; d.innerHTML = tex(t); c.appendChild(d); return d; });
      });
    }
    show(l) { l.classList.remove('hid'); if (l.dataset.final) l.classList.add('final'); }
    q(line, cls) { return line.querySelector('.' + cls); }
    cls(el, c) { if (el) c.split(' ').forEach(k => { el.classList.remove(k); void el.offsetWidth; el.classList.add(k); }); }
    mark(el, c) { this.cls(el, c); }
    rel(el) {
      const r = el.getBoundingClientRect(), a = this.area.getBoundingClientRect();
      return { x: r.left - a.left + this.area.scrollLeft, y: r.top - a.top, w: r.width, h: r.height };
    }
    pt(el, where) { const r = this.rel(el); return { x: r.x + r.w / 2, y: where === 'top' ? r.y : where === 'bottom' ? r.y + r.h : r.y + r.h / 2 }; }
    clearOverlay() { this.svg.querySelectorAll('path,marker').forEach(n => n.remove()); }
    arrow(a, b, color, o = {}) {
      const s = this.pt(a, o.from), d = this.pt(b, o.to);
      const bend = o.bend == null ? 60 : o.bend;
      const c = { x: 0, y: 0 };
      if (o.from === 'top' && !o.side) { c.x = (s.x + d.x) / 2; c.y = Math.min(s.y, d.y) + bend; }
      else { c.x = (s.x + d.x) / 2 + Math.abs(bend); c.y = (s.y + d.y) / 2; }
      const P = t => ({ x: (1 - t) * (1 - t) * s.x + 2 * (1 - t) * t * c.x + t * t * d.x, y: (1 - t) * (1 - t) * s.y + 2 * (1 - t) * t * c.y + t * t * d.y });
      const ns = 'http://www.w3.org/2000/svg', mid = `${this.id}-${color.slice(1)}`;
      if (!this.svg.querySelector('#' + mid)) {
        const m = document.createElementNS(ns, 'marker');
        m.setAttribute('id', mid); m.setAttribute('viewBox', '0 0 10 10'); m.setAttribute('refX', '8'); m.setAttribute('refY', '5');
        m.setAttribute('markerWidth', '7'); m.setAttribute('markerHeight', '7'); m.setAttribute('orient', 'auto-start-reverse');
        m.innerHTML = `<path d="M0 0L10 5L0 10z" fill="${color}"/>`; this.svg.querySelector('defs').appendChild(m);
      }
      const p = document.createElementNS(ns, 'path');
      p.setAttribute('d', `M${s.x} ${s.y} Q${c.x} ${c.y} ${d.x} ${d.y}`); p.setAttribute('fill', 'none');
      p.setAttribute('stroke', color); p.setAttribute('stroke-width', '2.5'); p.setAttribute('stroke-linecap', 'round');
      p.setAttribute('pathLength', '1'); this.svg.appendChild(p);
      const done = () => p.setAttribute('marker-end', `url(#${mid})`);
      if (reduced()) done();
      else {
        p.style.strokeDasharray = '1'; p.style.strokeDashoffset = '1';
        const an = p.animate([{ strokeDashoffset: 1 }, { strokeDashoffset: 0 }], { duration: SPEEDS[this.speed] * 0.5, fill: 'forwards', easing: 'ease-in-out' });
        an.onfinish = done;
      }
      return { P };
    }
    async fly(label, path, color, f) {
      this.chk();
      if (reduced()) return;
      const chip = document.createElement('div'); chip.className = 'sbt-chip'; chip.style.background = color; chip.textContent = label;
      this.area.appendChild(chip);
      const w = chip.offsetWidth, h = chip.offsetHeight, dur = SPEEDS[this.speed] * f;
      await new Promise((res, rej) => {
        const t0 = performance.now();
        const frame = now => {
          if (this.run !== this.my) { chip.remove(); return rej(CANCEL); }
          const u = Math.min(1, (now - t0) / dur), e = u < .5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2, p = path.P(e);
          chip.style.transform = `translate(${p.x - w / 2}px,${p.y - h / 2}px) scale(${1 + .15 * Math.sin(Math.PI * e)})`;
          if (u < 1) setTimeout(() => frame(performance.now()), 16); else res();
        };
        frame(t0);
      });
      chip.remove();
    }
    tip(el, text, color, side) {
      if (!el) return;
      const r = this.rel(el), b = document.createElement('div');
      b.className = 'sbt-bubble'; b.style.background = color; b.textContent = text;
      if (side === 'right') { b.style.transform = 'translate(0,-50%)'; b.style.animation = 'none'; b.style.left = (r.x + r.w + 12) + 'px'; b.style.top = (r.y + r.h / 2) + 'px'; }
      else { b.style.left = (r.x + r.w / 2) + 'px'; b.style.top = (r.y - 4) + 'px'; }
      this.area.appendChild(b);
    }
    underline(line, color) {
      const k = line.querySelector('.katex'); if (!k || reduced()) return;
      const r = this.rel(k), u = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      u.setAttribute('d', `M${r.x} ${r.y + r.h + 2} Q${r.x + r.w / 2} ${r.y + r.h + 7} ${r.x + r.w} ${r.y + r.h + 2}`);
      u.setAttribute('fill', 'none'); u.setAttribute('stroke', color); u.setAttribute('stroke-width', '2.5'); u.setAttribute('stroke-linecap', 'round');
      u.setAttribute('pathLength', '1'); u.style.strokeDasharray = '1'; this.svg.appendChild(u);
      u.animate([{ strokeDashoffset: 1 }, { strokeDashoffset: 0 }], { duration: SPEEDS[this.speed] * 0.4, fill: 'forwards' });
    }
  }

  // Mounted automatically when the host (rendered inside the question's worked answer) first becomes visible.
  function mount(host) {
    if (host._t || !root.katex) return;
    host._t = new Tutor(host);
  }
  // Hosts wait in `pending` until they are on screen (checked on scroll, click and after render); no polling timers.
  const pending = new Set();
  let q = 0;
  function check() {
    pending.forEach(h => {
      if (!h.isConnected) return pending.delete(h);
      const r = h.getBoundingClientRect();
      if (r.width > 0 && r.bottom > 0 && r.top < (root.innerHeight || 800)) { pending.delete(h); mount(h); }
    });
  }
  const later = () => { if (!pending.size) return; clearTimeout(q); q = setTimeout(check, 120); };
  root.addEventListener('scroll', later, { capture: true, passive: true });
  root.addEventListener('click', later, true);
  root.addEventListener('resize', later);
  function scan(n) {
    if (!n || n.nodeType !== 1) return;
    const hosts = n.matches && n.matches('[data-sbt-host]') ? [n] : (n.querySelectorAll ? n.querySelectorAll('[data-sbt-host]') : []);
    hosts.forEach(h => { if (!h._t && !h._w) { h._w = 1; pending.add(h); } });
    later();
  }
  scan(document.body);
  new MutationObserver(ms => ms.forEach(m => m.addedNodes.forEach(scan))).observe(document.documentElement, { childList: true, subtree: true });
})(window);
