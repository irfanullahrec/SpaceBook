/* Runs inside index.html (headless browser) for build_study_index.js.
 * For every class/subject: opens the subject like a student would, reads the chapter list from the sidebar,
 * finds the loaded data array whose titles match those chapters, and counts each chapter's study items.
 * window.__SP_NAMES (injected) = candidate global variable names from the js/ files.
 * Result is written to a pre#sp-out element as JSON. */
(async () => {
  'use strict';
  const wait = ms => new Promise(r => setTimeout(r, ms));
  const SIDEBAR = '.math-ch-list [onclick*="Chapter("], .math-ch-list button, .drawing-page-list button';
  const visible = () => [...document.querySelectorAll(SIDEBAR)].filter(e => e.offsetParent !== null);
  const norm = s => String(s || '').normalize('NFKC').toLowerCase().replace(/[ً-ٰٟۖ-ۭ]/g, '')
    .replace(/[^\p{L}\p{N}]+/gu, ' ').trim();

  // ---------- categories ----------
  const CAT = [
    ['tf', /true\s*(\/|or|and|-)?\s*false|truefalse|\btf\b|درست.{0,8}غلط|صحیح.{0,8}غلط|سم.{0,8}ناسم/i],
    ['blank', /blank|fill in|fill the|خالی/i],
    ['match', /match|column|ملاپ|ملائیں|جوڑ/i],
    ['mcq', /\bmcqs?\b|multiple.?choice|choose the (correct|right|best)|correct (option|answer)|encircle|tick|کثیر الانتخاب|درست جواب|صحیح جواب|څو ځوابه|سم ځواب/i],
    ['lq', /comprehensive|\blong\b|detail|descriptive|essay|extensive|\blqs?\b|تفصیلی|طویل|اوږد/i],
    ['sq', /conceptual|\bshort\b|brief|\bsqs?\b|مختصر|لنډ/i],
    ['num', /numerical|problems?\b|calculat|عددی/i],
    ['slo', /\bslos?\b|learning outcome|objectives?\b|حاصلات|تدریسی مقاصد/i],
  ];
  const classify = s => { s = String(s || ''); for (const [c, rx] of CAT) if (rx.test(s)) return c; return null; };
  const SKIPKEY = /^(source.*|.*translations?|.*Translation|ur|ps|en|ar|urdu|pashto|english|.*Urdu|.*Pashto|figures?|svg|equations?|formula.*|vocab.*|glossary.*|.*Words?|words|dictionary.*|thesaurus.*|rows|headers|cells|columns|points|paths|labels|flow|layout|parts|options|choices|answers?|solution.*|steps|keyPoints.*|summary|tables?|images?|videos?)$/;
  const textOf = b => [b.en, b.text, b.q, b.question, b.title, b.heading, b.ur, b.original].filter(x => typeof x === 'string').join(' ');
  const looksMcq = s => /(^|\s)\(?a[).]\s.+\s\(?b[).]\s.+\s\(?c[).]\s/i.test(s) || /\(الف\).+\(ب\).+\(ج\)/.test(s);

  // page-transcribed books (Classes 11–12): questions live in paragraph text under headings such as
  // "MULTIPLE CHOICE QUESTIONS" / "Conceptual Questions 3–12"; count the numbered items under each heading
  const HDR = /(multiple[- ]choice questions|\bmcqs?\b|short[- ](?:answer )?questions|conceptual questions|comprehensive questions|long[- ](?:answer )?questions|descriptive questions|numerical (?:questions|problems)|true\s*\/?\s*(?:or\s*)?false|fill in the blanks|match(?:ing)? the columns|کثیر الانتخابی سوالات|معروضی سوالات|مختصر (?:جوابات|سوالات)|تفصیلی (?:جوابات|سوالات)|انشائیہ سوالات|خالی جگہ)/gi;
  const NUM = /(?:^|[\s(])([0-9۰-۹]{1,3})[.)\-۔]\s*(?=\S)/g;
  const toInt = s => parseInt(String(s).replace(/[۰-۹]/g, d => '۰۱۲۳۴۵۶۷۸۹'.indexOf(d)), 10);
  function textPass(ch) {
    const c = {};
    let cur = null, last = 0;
    const scan = s => {
      const parts = String(s).split(HDR);
      parts.forEach((seg, i) => {
        if (i % 2 === 1) { const k = classify(seg); if (k !== cur) { cur = k; last = 0; } return; }
        if (!cur) return;
        let m; NUM.lastIndex = 0;
        while ((m = NUM.exec(seg))) { const n = toInt(m[1]); if (n > last && n <= last + 3) { c[cur] = (c[cur] || 0) + (n - last); last = n; } }
      });
    };
    const secs = Array.isArray(ch.sections) ? ch.sections : Array.isArray(ch.pages) ? ch.pages : [ch];
    const seen = new Set();
    const walkT = v => {
      if (!v || typeof v !== 'object' || seen.has(v)) return; seen.add(v);
      if (Array.isArray(v)) { v.forEach(walkT); return; }
      if (typeof v.title === 'string') {
        const r = v.title.match(HDR);
        if (r) { const k = classify(r[0]); const st = v.title.slice(v.title.search(HDR)).match(/^[^0-9]*?(\d+)/); const start = st ? +st[1] - 1 : 0; if (k !== cur) { cur = k; last = start; } else last = Math.max(last, start); }
      }
      const s = typeof v.original === 'string' ? v.original : typeof v.text === 'string' ? v.text : typeof v.en === 'string' ? v.en : null;
      if (s) scan(s);
      for (const k of ['paras', 'blocks', 'items', 'flow', 'subsections']) if (Array.isArray(v[k])) walkT(v[k]);
    };
    walkT(secs);
    return c;
  }

  function count(ch) {
    const c = {};
    const add = (k, n) => { if (n > 0) c[k] = (c[k] || 0) + n; };
    const seen = new Set();
    function blocks(list, ctx) {
      let cur = ctx;
      for (const b of list) {
        if (!b || typeof b !== 'object') continue;
        const t = b.t || b.type || b.kind;
        if (t === 'h' || t === 'heading' || t === 'subheading') { const k = classify(textOf(b)); if (k) cur = k; continue; }
        if (t === 'exercise') { blocks(b.blocks || b.items || [], classify(b.id || b.title) || ctx); continue; }
        if (t === 'q' || t === 'question') {
          const s = textOf(b);
          const k = cur || (looksMcq(s) ? 'mcq' : classify(s) || 'ex');
          add(k, Array.isArray(b.parts) && b.parts.length ? b.parts.length : 1);
          continue;
        }
        if (t === 'parts' && Array.isArray(b.parts)) { add(cur || 'ex', b.parts.length); continue; }
        if (t === 'mcq') { add('mcq', 1); continue; }
        walk(b, cur);
      }
    }
    function walk(v, ctx) {
      if (!v || typeof v !== 'object' || seen.has(v)) return;
      seen.add(v);
      if (Array.isArray(v)) { v.forEach(x => walk(x, ctx)); return; }
      // a stand-alone question with options
      const opts = v.options || v.choices || v.opts;
      if (Array.isArray(opts) && opts.length >= 2 && (v.q || v.question || v.en || v.text || v.stem)) { add(ctx === 'slo' ? 'mcq' : (ctx && ctx !== 'mcq' && ctx !== 'ex' ? ctx : 'mcq'), 1); return; }
      for (const k of Object.keys(v)) {
        if (SKIPKEY.test(k)) continue;
        const x = v[k];
        if (!x || typeof x !== 'object') continue;
        if (k === 'blocks' && Array.isArray(x)) { blocks(x, ctx); continue; }
        const kc = classify(k.replace(/([a-z])([A-Z])/g, '$1 $2'));
        if (kc && Array.isArray(x)) {
          if (kc === 'slo' && x.length && typeof x[0] === 'object' && !Array.isArray(x[0]) && Object.keys(x[0]).some(z => /mcq|short|long|sq|lq/i.test(z))) { walk(x, kc); continue; }
          add(kc, x.filter(i => i != null && i !== '').length);
          continue;
        }
        walk(x, kc || ctx);
      }
    }
    walk(ch, null);
    if (!Object.keys(c).some(k => k !== 'slo')) Object.entries(textPass(ch)).forEach(([k, n]) => add(k, n));
    // lesson parts to read
    const secs = Array.isArray(ch.sections) ? ch.sections : Array.isArray(ch.pages) ? ch.pages : Array.isArray(ch.topics) ? ch.topics : null;
    const read = secs ? secs.filter(s => !classify((s && (s.title || s.heading || s.kind || s.status)) || '') && !/exercise|assessment|review|مشق|تمرین/i.test(String(s && (s.title || s.heading || s.status) || ''))).length : 0;
    c.read = Math.max(1, Math.min(read || 1, 40));
    return c;
  }

  // ---------- candidate chapter arrays from loaded globals ----------
  const TITLE_KEYS = ['title', 'titleEn', 'name', 'titleUrdu', 'unitTitle', 'chapterTitle', 'heading', 'titleUr', 'urduTitle'];
  const cands = [];
  const isChapterArray = a => Array.isArray(a) && a.length >= 1 && a.length <= 120 && a.filter(x => x && typeof x === 'object' && TITLE_KEYS.some(k => typeof x[k] === 'string')).length >= Math.max(1, a.length * 0.6);
  function collect(v, path, depth, seen) {
    if (!v || typeof v !== 'object' || seen.has(v) || depth > 3) return;
    seen.add(v);
    if (isChapterArray(v)) { cands.push({path, arr: v}); if (depth >= 2) return; }
    if (Array.isArray(v)) return;
    for (const k of Object.keys(v)) { let x; try { x = v[k]; } catch (e) { continue; } if (x && typeof x === 'object') collect(x, path + '.' + k, depth + 1, seen); }
  }
  const seen = new Set();
  for (const n of (window.__SP_NAMES || [])) { let v; try { v = (0, eval)(n); } catch (e) { continue; } if (v && typeof v === 'object') collect(v, n, 0, seen); }
  cands.forEach(cd => { cd.titles = cd.arr.map(x => TITLE_KEYS.map(k => x && typeof x[k] === 'string' ? norm(x[k]) : '').filter(t => t.length >= 4 && !/^(unit|chapter|lesson|باب|سبق)\s*\d+$/.test(t))); });

  function bestMatch(side, clsNum) {
    const own = new RegExp('(^|[^0-9])' + clsNum + '([^0-9]|$)');
    const sn = side.map(norm);
    let best = null;
    for (const cd of cands) {
      if (/^DATA\.(chapters|subjects|classes|books|studyPlan)\b/.test(cd.path)) continue;
      const map = sn.map(s => cd.titles.findIndex(ts => ts.some(t => s.includes(t))));
      const score = map.filter(i => i >= 0).length;
      if (!score) continue;
      const pref = (/BOOKS/.test(cd.path) ? 0.5 : 0) + (own.test(cd.path) ? 1.5 : 0) - Math.abs(cd.arr.length - side.length) * 0.01;
      if (!best || score + pref > best.score + best.pref) best = {cd, map, score, pref};
    }
    return best;
  }

  await wait(1500);
  const out = {generated: new Date().toISOString(), classes: []};
  for (const cls of DATA.classes) {
    const C = {id: cls.id, name: cls.name, subjects: []};
    for (const s of (DATA.subjects[cls.id] || [])) {
      let side = [];
      try { openSubject(cls.id, s.id); await wait(200); side = visible().map(e => e.textContent.replace(/\s+/g, ' ').trim()); } catch (e) { /* skipped */ }
      if (!side.length || (side.length === 1 && /not available/i.test(side[0]))) continue;
      const m = bestMatch(side, (cls.id.match(/\d+/) || [''])[0]);
      const chapters = side.map((t, i) => {
        const obj = m && m.map[i] >= 0 ? m.cd.arr[m.map[i]] : null;
        return {t: t.slice(0, 120), c: obj ? count(obj) : {read: 1}};
      });
      C.subjects.push({id: s.id, name: s.name, ur: s.nameUrdu || '', emoji: s.emoji || '📘', src: m ? m.cd.path : '', matched: m ? m.score : 0, chapters});
    }
    if (C.subjects.length) out.classes.push(C);
  }
  const pre = document.createElement('pre'); pre.id = 'sp-out'; pre.textContent = JSON.stringify(out); document.body.appendChild(pre);
})();
