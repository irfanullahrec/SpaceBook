// In-browser layout harness for Class 6-8 books. Load on lazy.html, then:
//   await QA.run('cls7','hpe')  -> {units, tabs, issues:[{u,tab,kind,sel,w,sw}]}
// Reports elements that stick out of the viewport or of their own box without a scroller.
window.QA = (function () {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  function scrollerOK(el) {
    for (let p = el.parentElement; p && p !== document.body; p = p.parentElement) {
      const cs = getComputedStyle(p);
      if (/(auto|scroll)/.test(cs.overflowX)) return p;
    }
    return null;
  }
  function describe(el) {
    let s = el.tagName.toLowerCase();
    if (el.id) s += '#' + el.id;
    if (el.className && typeof el.className === 'string') s += '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.');
    return s;
  }
  function measure(root) {
    const vw = document.documentElement.clientWidth, out = [];
    const docOver = document.documentElement.scrollWidth - vw; const areaOver = root.scrollWidth - root.clientWidth; if (areaOver > 2 && root !== document.body) out.push({ kind: 'area-scroll-x', sel: describe(root), w: areaOver });
    if (docOver > 1) out.push({ kind: 'page-scroll-x', sel: 'html', w: docOver });
    const els = root.querySelectorAll('*');
    let n = 0;
    for (const el of els) {
      if (n > 12) break;
      const r = el.getBoundingClientRect();
      if (!r.width) continue;
      if (r.right > vw + 2) {
        if (getComputedStyle(el).position === 'fixed' || scrollerOK(el)) continue;
        out.push({ kind: 'beyond-viewport', sel: describe(el), w: Math.round(r.right - vw), txt: (el.textContent || '').trim().slice(0, 30) }); n++; continue;
      }
      if (el.scrollWidth - el.clientWidth > 2 && el.clientWidth > 0 && el.children.length && !/^(svg|img|html|body)$/i.test(el.tagName)) {
        const ox = getComputedStyle(el).overflowX;
        if (/(hidden|clip)/.test(ox)) { out.push({ kind: 'clipped-x', sel: describe(el), w: el.scrollWidth - el.clientWidth }); n++; }
      }
    }
    return out;
  }
  async function run(cls, key, opts) {
    opts = opts || {};
    openSubject(cls, cls + '-' + key.split('/')[0]);
    await sleep(opts.wait || 600);
    const nUnits = [...document.querySelectorAll('[onclick*="selectSubjectChapter"]')].length;
    const issues = [], seenTabs = new Set(); let renders = 0;
    for (let u = 0; u < nUnits; u++) {
      selectSubjectChapter(key, u, cls); await sleep(opts.wait || 300);
      const tabs = [...new Set([...document.querySelectorAll('[onclick*="switchSubjectTab"]')].map(e => (/switchSubjectTab\('[^']*',\s*'([^']*)'/.exec(e.getAttribute('onclick')) || [])[1]).filter(Boolean))];
      for (const t of tabs) {
        if (opts.tabs && !opts.tabs.includes(t)) continue;
        seenTabs.add(t);
        switchSubjectTab(key, t, u, cls); await sleep(opts.wait || 300);
        renders++; window.__qaProg = [u, t, renders];
        const root = document.querySelector('#subject-content, #subjectContent, .subject-content, main') || document.body;
        const text = (root.innerText || '').trim();
        if (t === 'lesson' && text.length < 200) issues.push({ u, tab: t, kind: 'thin-content', sel: '', w: text.length });
        const area = document.getElementById('subjectTopicArea') || document.body; const open = [...area.querySelectorAll('.math-accordion-body')]; const prev = open.map(e => e.style.cssText); open.forEach(e => { e.hidden = false; e.style.display = 'block'; e.style.maxHeight = 'none'; }); await sleep(30);
        for (const m of measure(area)) issues.push(Object.assign({ u, tab: t }, m));
        open.forEach((e, i) => { e.style.cssText = prev[i]; });
      }
    }
    return { cls, key, vw: document.documentElement.clientWidth, units: nUnits, tabs: [...seenTabs], renders, issues };
  }
  return { run, measure, sleep };
})();
