/* In-browser QA harness for Class 9/10 page-view checks (dev only; paste/load in the app page via the Browser pane).
 *   await (await fetch('/tools/qa/browser_harness.js')).text() -> (0,eval)(text)
 *   __qa.bg([[ 'cls10','cls10-math' ], ...], maxChapters, waitMs)   starts a background run (the JS tool stops after 45 s)
 *   __qa.status()   {done, cur, n};   __qa.results   list of {subj, chapters, pageScroll, issues:[{ch, page, bad:[...]}]}
 * A chapter is "bad" when the document scrolls sideways, an element sticks out of the viewport outside any scroll container,
 * or an overflow:hidden box clips its content (text-overflow:ellipsis boxes are only counted in `ell`). */
(function () {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  function over() {
    const W = document.documentElement.clientWidth, bad = [];
    const page = document.documentElement.scrollWidth > W + 1;
    let ell = 0;
    for (const el of document.querySelectorAll('body *')) {
      if (bad.length >= 12) break;
      const cs = getComputedStyle(el);
      if (cs.display === 'none' || cs.visibility === 'hidden' || el.closest('[hidden]')) continue;
      const r = el.getBoundingClientRect();
      if (r.width === 0 || r.height === 0) continue;
      if (r.right > W + 2 || r.left < -2) {
        let p = el.parentElement, sc = false;
        while (p && p !== document.body) {
          const c = getComputedStyle(p);
          if (/(auto|scroll|hidden|clip)/.test(c.overflowX) || c.position === 'fixed') { sc = true; break; }
          p = p.parentElement;
        }
        if (!sc && cs.position !== 'fixed') bad.push({ k: 'out', tag: el.tagName.toLowerCase(), cls: String(el.className).slice(0, 40), w: Math.round(r.width), r: Math.round(r.right), t: (el.innerText || '').slice(0, 30) });
      } else if ((cs.overflowX === 'hidden' || cs.overflowX === 'clip') && el.scrollWidth > el.clientWidth + 3 && el.clientWidth > 40) {
        if (cs.textOverflow === 'ellipsis') { ell++; continue; }
        bad.push({ k: 'clip', tag: el.tagName.toLowerCase(), cls: String(el.className).slice(0, 40), sw: el.scrollWidth, cw: el.clientWidth, t: (el.innerText || '').slice(0, 30) });
      }
    }
    return { page, W, bad, ell };
  }
  async function run(cls, subj, maxCh, wait, tabs) {
    state.selectedClass = cls; openSubject(cls, subj); await sleep(1500);
    const seen = new Set(), calls = [];
    document.querySelectorAll('[onclick]').forEach(e => { const o = e.getAttribute('onclick'); if (/^select\w*Chapter\(/.test(o) && !seen.has(o)) { seen.add(o); calls.push(o); } });
    const out = { subj, chapters: calls.length, pageScroll: 0, ell: 0, issues: [] };
    const lim = Math.min(calls.length, maxCh || 99);
    for (let i = 0; i < lim; i++) {
      try { (0, eval)(calls[i]); } catch (e) { out.issues.push({ ch: i, err: String(e.message).slice(0, 80) }); continue; }
      await sleep(wait || 700);
      const passes = [null];
      if (tabs) {   // also click every tab of the chapter once
        document.querySelectorAll('[onclick]').forEach(e => { const o = e.getAttribute('onclick'); if (/^switch\w*Tab\(/.test(o) && !passes.includes(o)) passes.push(o); });
      }
      for (const tabCall of passes) {
        if (tabCall) { try { (0, eval)(tabCall); } catch (e) { continue; } await sleep(wait || 700); }
        const o = over();
        out.ell += o.ell;
        if (o.page) out.pageScroll++;
        if (o.bad.length || o.page) out.issues.push({ ch: i, tab: tabCall, page: o.page, bad: o.bad.slice(0, 4) });
      }
    }
    return out;
  }
  const qa = window.__qa = { sleep, over, run, results: [], done: true, cur: '' };
  qa.bg = function (subs, maxCh, wait, tabs) {
    qa.results = []; qa.done = false; qa.cur = '';
    (async () => { for (const [c, s] of subs) { qa.cur = s; try { qa.results.push(await run(c, s, maxCh, wait, tabs)); } catch (e) { qa.results.push({ subj: s, err: String(e.message) }); } } qa.done = true; })();
    return 'started';
  };
  qa.status = () => ({ done: qa.done, cur: qa.cur, n: qa.results.length });
})();
