'use strict';
/* Do the question cards of the Board SLO tab and of the Solved Exercises tab of Classes 9 to 12 still say "The answer to this saved question still needs to be
 * completed"? (js/class12_study_views.js draws those cards; a Class 11 card takes its answer from the textbook page that holds the same question.)
 *     node --max-old-space-size=6144 tools/launch/study_pending.js [--check] [--classes cls11,cls12] [--list]
 * Runs the page's own renderers in the app sandbox, chapter by chapter, and counts the cards and the "answer pending" notes. --check exits 1 when any card
 * is still pending (it is in the launch gate: a student must never read that sentence); --list prints the questions that are.
 * Why it exists: the exercise coverage tool counts the questions of the books' pages; these cards are a second copy of the same questions (saved
 * records), and 3,242 of the Class 11 ones had no answer until this check was written (2026-10-28). Dev-only, never shipped. */
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
process.chdir(ROOT);
const { load } = require('../lib/app_sandbox');
const args = process.argv.slice(2);
const CHECK = args.includes('--check'), LIST = args.includes('--list');
const CLASSES = (args.includes('--classes') ? args[args.indexOf('--classes') + 1] : 'cls9,cls10,cls11,cls12').split(',');
const catalog = JSON.parse(fs.readFileSync(path.join(ROOT, 'content', 'app_catalog.json'), 'utf8'));

let cards = 0, pending = 0;
const listed = [];
for (const cls of catalog.classes.filter(c => CLASSES.includes(c.id))) {
  const app = load({ page: 'lazy.html', quiet: true });
  for (const subj of cls.subjects) {
    const first = (subj.chapters || []).find(c => /selectSubjectChapter/.test(c.o || ''));
    const m = first && /selectSubjectChapter\('([a-z0-9]+)'/i.exec(first.o);
    if (!m) continue;
    const key = m[1];
    let r;
    try {
      r = JSON.parse(app.run(`(function(){
        state.selectedClass=${JSON.stringify(cls.id)};
        const list=getSubjectChapterList(${JSON.stringify(key)},${JSON.stringify(cls.id)})||[];
        const out={cards:0,pending:0,items:[]};
        list.forEach((ch,i)=>{
          state.selectedSubjChapter=i;
          let h=''; try { h=String(renderSubjectSLOsTab(${JSON.stringify(key)},ch)||''); } catch(e) { return; }
          out.cards+=(h.match(/class12-question/g)||[]).length;
          const re=/<article class="math-topic-card class12-question"[\\s\\S]*?<\\/article>/g; let mm;
          while((mm=re.exec(h))){ if(mm[0].indexOf('data-answer-pending')<0) continue; out.pending++;
            const q=/class12-question-text" dir="auto">([\\s\\S]*?)<\\/div>/.exec(mm[0]); out.items.push((ch.number+': '+(q?q[1].replace(/<[^>]*>/g,' ').replace(/\\s+/g,' ').trim():'')).slice(0,140)); }
        });
        return JSON.stringify(out);
      })()`, 600000));
    } catch (e) { r = { cards: 0, pending: 0, items: [], error: String(e.message).slice(0, 80) }; }
    cards += r.cards; pending += r.pending;
    if (r.pending) { console.log(`${cls.id} ${subj.id}: ${r.pending} of ${r.cards} cards pending`); r.items.forEach(x => listed.push(`${subj.id} ${x}`)); }
  }
}
if (LIST) listed.forEach(x => console.log('  ' + x));
console.log(`study question cards of ${CLASSES.join(', ')}: ${cards} cards, ${pending} say "the answer still needs to be completed"`);
if (CHECK && pending) process.exit(1);
