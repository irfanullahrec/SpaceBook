// Tab-structure audit (run inside the app page: fetch + eval). For each Class 9-12 subject and a sample of chapters
// it records the main tabs, the lesson sub-tabs, exercise-like headings shown in each tab, and how much of the
// Exercise tab's text is repeated in the other tabs. Results land in window.__audit (array) and window.__auditDone.
(async function () {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const norm = s => String(s || '').replace(/\s+/g, ' ').trim();
  const EXRX = /\b(exercise|review exercise|review questions?|questions?|mcqs?|multiple choice|short questions?|long questions?|numerical problems?|assignments?|activity|activities)\b|مشق|سوالات|سوال|تمرین|مشغولتیا|پوښتن/i;
  const area = () => document.getElementById('subjTabContent') || document.querySelector('.math-tab-content-scroll') || document.getElementById('subjectTopicArea');
  function snapshot() {
    const a = area(); if (!a) return {heads: [], sents: new Set(), len: 0};
    const heads = [...a.querySelectorAll('h1,h2,h3,h4,h5,.math-acc-header,.slo-accordion-header,summary,.math-book-subheading,.c1-banner,.m6-h3,.m6-exercise-t')]
      .map(e => norm(e.textContent).slice(0, 90)).filter(Boolean);
    const sents = new Set();
    norm(a.textContent).split(/(?<=[.?!۔؟])\s+/).map(s => s.toLowerCase().replace(/[^a-z0-9؀-ۿ ]/g, '').trim()).filter(s => s.length > 35).forEach(s => sents.add(s.slice(0, 120)));
    return {heads, sents, len: norm(a.textContent).length};
  }
  const tabBtns = () => [...document.querySelectorAll('.math-nav-tabs button, .math-nav-tabs .math-tab-btn')];
  const subBtns = () => [...document.querySelectorAll('#subjSubTabsBar button, .math-sub-tabs button, .topic-sub-tabs-bar button')].map(b => norm(b.textContent));
  const out = window.__audit = []; window.__auditDone = false;
  const classes = (window.__auditClasses || ['cls9', 'cls10', 'cls11', 'cls12']);
  const D = typeof subjects !== 'undefined' ? subjects : (window.subjects || {});
  for (const cls of classes) {
    const list = (window.__auditSubjects && window.__auditSubjects[cls]) || ((typeof DATA !== 'undefined' && DATA.subjects && DATA.subjects[cls]) || []).map(s => s.id);
    for (const sid of list) {
      const rec = {cls, sid, tabs: [], chapters: []};
      try {
        openSubject(cls, sid); await sleep(1300);
        const chBtns = [...document.querySelectorAll('.math-ch-sidebar .math-ch-btn, .math-ch-sidebar .bio-ch-btn, .math-ch-sidebar .math-ch-item')];
        rec.nChapters = chBtns.length;
        const pick = [...new Set([0, Math.floor(chBtns.length / 2), chBtns.length - 1])].filter(i => i >= 0 && chBtns[i]);
        for (const ci of pick) {
          const btns0 = [...document.querySelectorAll('.math-ch-sidebar .math-ch-btn, .math-ch-sidebar .bio-ch-btn, .math-ch-sidebar .math-ch-item')];
          btns0[ci].click(); await sleep(1100);
          const chRec = {ci, title: norm(btns0[ci].textContent).slice(0, 70), tabs: {}};
          const labels = tabBtns().map(b => norm(b.textContent)).filter(l => !/Word Stats/.test(l));
          if (!rec.tabs.length) rec.tabs = labels;
          const snaps = {};
          for (let ti = 0; ti < labels.length; ti++) {
            const b = tabBtns()[ti]; if (!b) continue;
            b.click(); await sleep(650);
            const s = snapshot();
            snaps[labels[ti]] = s;
            chRec.tabs[labels[ti]] = {len: s.len, sub: subBtns(), exHeads: s.heads.filter(h => EXRX.test(h)).slice(0, 12), heads: s.heads.slice(0, 25)};
          }
          // repetition: share of each tab's sentences that also appear in another tab
          const names = Object.keys(snaps);
          chRec.repeat = {};
          for (const a of names) for (const b of names) if (a < b) {
            const A = snaps[a].sents, B = snaps[b].sents; if (!A.size || !B.size) continue;
            let n = 0; A.forEach(x => { if (B.has(x)) n++; });
            if (n >= 3) chRec.repeat[a + ' ⟷ ' + b] = n + ' shared (' + Math.round(100 * n / Math.min(A.size, B.size)) + '% of smaller)';
          }
          rec.chapters.push(chRec);
        }
      } catch (e) { rec.error = String(e && e.message || e); }
      out.push(rec);
    }
  }
  window.__auditDone = true;
})();
