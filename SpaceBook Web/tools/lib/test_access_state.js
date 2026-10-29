'use strict';
/* The saved access answer (localStorage sb_access_v1, js/sb_access.js) of a person with every plan, made from the app catalog: every class, every
 * subject's papers, Test Preparation. The real-browser test launcher (tests/baseline/lib.js) puts it in each new browser context, so the pages show
 * every chapter; a test of the visitor's view opts out (launch({ anonymous: true })). Dev-only, never shipped. */
const fs = require('fs'), path = require('path');
module.exports = function accessState() {
  const cat = JSON.parse(fs.readFileSync(path.join(__dirname, '..', '..', 'content', 'app_catalog.json'), 'utf8'));
  const classes = cat.classes.map(c => c.id);
  const subjects = cat.classes.flatMap(c => c.subjects.map(s => s.id));
  return JSON.stringify({ ok: true, signedIn: false, plan: 'paid', access: { readClasses: classes, readSubjects: [], planClasses: classes, paperSubjects: subjects, prep: true }, subscriptions: [] });
};
