'use strict';
/* SBHooks (js/core/hooks.js): the registry that replaced hand-made function wrappers.
 *   node --max-old-space-size=8192 tests/hooks/hooks.js [--update]    --update rewrites tests/contract/hooks.json (who extends what, in order)
 * Part 1 tests the registry on its own. Part 2 loads the whole page and compares who extends what with the locked list: the order is the
 * order the old wrappers were applied in (script order), so a change here changes behaviour and must be intended. Part 3 checks that
 * the modules converted from wrappers still do their side jobs (continue-learning records a chapter, sb_structure hides empty tabs). */
const fs = require('fs'), path = require('path'), vm = require('vm');
const LOCK = path.join(__dirname, '..', 'contract', 'hooks.json');
let passed = 0, failed = 0;
const check = (name, ok, extra) => { if (ok) passed++; else { failed++; console.log('FAIL  ' + name + (extra ? ' : ' + extra : '')); } };

// ---------- 1. the registry itself
function fresh() {
  const g = { console, setTimeout, clearTimeout };
  g.window = g; g.document = undefined;
  vm.createContext(g);
  vm.runInContext(fs.readFileSync(path.join(__dirname, '..', '..', 'js', 'core', 'hooks.js'), 'utf8'), g);
  return g;
}
{
  const g = fresh();
  vm.runInContext("function greet(name) { return 'hello ' + name; }", g);
  const first = g.greet;
  g.SBHooks.use('greet', next => function (name) { return '[' + next.call(this, name) + ']'; }, { id: 'a.js' });
  const dispatcher = g.greet;
  g.SBHooks.use('greet', next => function (name) { return next.call(this, name.toUpperCase()) + '!'; }, { id: 'b.js' });
  check('the global becomes a stable dispatcher on the first use', dispatcher !== first && g.greet === dispatcher);
  check('the last registered wraps outermost (the order of the old wrapper chain)', g.greet('ali') === '[hello ALI]!', g.greet('ali'));
  check('list() says who extends what, in order', JSON.stringify(g.SBHooks.list()) === '{"greet":["a.js","b.js"]}', JSON.stringify(g.SBHooks.list()));
  check('base() is the original function', g.SBHooks.base('greet') === first);
  const obj = { greet: g.greet, tag: 't' };
  g.SBHooks.use('greet', next => function () { return this && this.tag; });
  check('this reaches the wrapper', obj.greet('x') === 't');
  check('a late registration is picked up by the next call', g.greet !== undefined && g.SBHooks.list().greet.length === 3);
  g.SBHooks.replace('greet', function () { return 'replaced'; }, { id: 'c.js' });
  check('replace() overrides everything below it and is itself wrapped by later uses', g.greet('x') === 'replaced');
  let threw = null; try { g.SBHooks.use('nothing', n => n); } catch (e) { threw = e; }
  check('hooking a function that does not exist fails loudly', !!threw && /not a function/.test(threw.message));
  threw = null; try { g.SBHooks.use('greet', 5); } catch (e) { threw = e; }
  check('a factory must be a function', !!threw);
  g.SBHooks.reset();
  check('reset() puts the original back', g.greet === first && g.greet('z') === 'hello z');
}

// ---------- 2. the whole page: who extends what
const { load } = require('../../tools/lib/app_sandbox');
const timers = [];
const app = load({ page: process.env.SB_PAGE || 'lazy.html', quiet: true, before: sb => { sb.setTimeout = fn => { timers.push(fn); return timers.length; }; } });
const flush = () => timers.splice(0).forEach(fn => { try { fn(); } catch (e) { /* a timer of the page */ } });
const list = app.run('JSON.stringify(SBHooks.list())');
const current = JSON.parse(list);
if (process.argv.includes('--update')) {
  fs.mkdirSync(path.dirname(LOCK), { recursive: true });
  fs.writeFileSync(LOCK, JSON.stringify({ note: 'Who extends which global function through SBHooks, in composition order (first = closest to the original). Order = script order in index.html; tests/hooks/hooks.js --update after an intended change.', hooks: current }, null, 1) + '\n');
  console.log('wrote ' + path.relative(process.cwd(), LOCK));
}
const lock = JSON.parse(fs.readFileSync(LOCK, 'utf8')).hooks;
const diff = [...new Set([...Object.keys(lock), ...Object.keys(current)])].filter(n => JSON.stringify(lock[n]) !== JSON.stringify(current[n]));
check('who extends what matches tests/contract/hooks.json (' + Object.keys(current).length + ' functions, ' + Object.values(current).reduce((n, a) => n + a.length, 0) + ' registrations)', diff.length === 0, diff.join(', '));
check('switchSubjectTab has its 18 extensions in script order', current.switchSubjectTab && current.switchSubjectTab.length === 18 && current.switchSubjectTab[0] === 'class11_study_views.js' && current.switchSubjectTab[13] === 'sb_book_spread.js' && current.switchSubjectTab[14] === 'sb_structure.js' && current.switchSubjectTab[15] === 'sb_exercise_tabs.js' && current.switchSubjectTab[16] === 'a11y.js' && current.switchSubjectTab[17] === 'lazycards.js');
check('the dispatcher is what the global holds', app.run("window.switchSubjectTab.__sbHooked === true && typeof SBHooks.base('switchSubjectTab') === 'function'") === true);

// ---------- 3. converted modules still do their side jobs
{
  const run = c => { try { return app.run(c, 120000); } catch (e) { return 'ERR ' + e.message; } };
  run("openSubject('cls9', 'cls9-bio')"); flush();
  run("selectBioChapter(2)"); flush();
  const saved = run("localStorage.getItem('sbContinue:v1')");
  check('continue-learning (a hooked wrapper) records the opened chapter', typeof saved === 'string' && /cls9-bio/.test(saved) && /selectBioChapter/.test(saved), String(saved).slice(0, 120));
  // sb_structure wraps switchSubjectTab: tabs that would be empty are hidden by the plan
  run("openSubject('cls5', 'cls5-math')");
  const body = run("document.getElementById('dashboard-body').innerHTML");
  check('opening a subject through the hooked openSubject still renders the workspace', /math-ch-list|subjectTopicArea|mathTopicArea/.test(String(body)), String(body).slice(0, 80));
  // Class 5 Maths is rendered by the Class 5 reader through the switchSubjectTab hook
  run("selectSubjectChapter && 0");
  const tabHtml = run("(() => { switchSubjectTab('math', 'lesson', 0, 'cls5'); return document.getElementById('subjTabContent').innerHTML; })()");
  check('the Class 5 reader renders its Maths lesson through the hook', /m5-/.test(String(tabHtml)), String(tabHtml).slice(0, 80));
  const other = run("(() => { switchSubjectTab('bio', 'lesson', 0, 'cls9'); return document.getElementById('subjTabContent').innerHTML; })()");
  check('a subject no reader owns still reaches the original renderer', String(other).length > 500 && !/m5-root/.test(String(other)), String(other).length + '');
}

console.log(`hooks tests: ${passed} passed, ${failed} failed`);
process.exit(failed ? 1 : 0);
