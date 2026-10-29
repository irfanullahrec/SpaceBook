'use strict';
/* The pages the build and test tools render (tools/smoke.js, lazy_parity.js, snapshot_html.js, the axe and tab tests ...) show every chapter of every
 * subject. For an anonymous visitor only Chapter 1 is open (js/sb_access.js), so these loaders give the page the access of a person with every plan:
 * all classes, all papers, Test Preparation. Dev-only, never shipped. */
module.exports = `(function () {
  try {
    if (!window.SBAccess || !SBAccess._setState) return;
    var classes = (DATA.classes || []).map(function (c) { return c.id; }), subjects = [];
    Object.keys(DATA.subjects || {}).forEach(function (k) { (DATA.subjects[k] || []).forEach(function (s) { subjects.push(s.id); }); });
    SBAccess._setState({ access: { readClasses: classes, readSubjects: [], planClasses: classes, paperSubjects: subjects, prep: true } }, true);
  } catch (e) { /* the page has no access module: nothing to open */ }
})();`;
