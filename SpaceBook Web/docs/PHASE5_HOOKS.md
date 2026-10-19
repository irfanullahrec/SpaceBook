# Phase 5 (first part): hooks instead of patches

**Problem (ARCH-01).** 53 global functions of `app.js` were replaced by 109 hand-made wrappers spread over 35 files (`switchSubjectTab` 14 times, `openSubject` 7, `getSubjectChapterList` 6, `typesetChapterMath` 5, the Maths renderers 6 each, `continue_learning.js` alone 20). Each wrapper did `const original = window.f; window.f = function () { ...original.apply(this, arguments)... }`, so what a call did depended on which scripts loaded in which order, nothing said who had wrapped what, and a new reader had to be added to the chain by hand without being able to see it.

**What was built.** `js/core/hooks.js` (`SBHooks`, loaded before `app.js`):

```js
SBHooks.use('switchSubjectTab', function (next) { return function (subjKey, tabId, chIdx, classId) { ... next.apply(this, arguments) ... }; });
SBHooks.replace('renderStudyPlan', function () { ... });        // an override that never calls the original
SBHooks.list()                                                   // { name: [files in composition order] }
```

The first `use` for a name replaces the global by a stable dispatcher; registration order is composition order (the last registered is outermost), exactly the order the old wrappers were applied in, because it is script order. The wrapper code itself did not change: only the two lines around it, so the behaviour is the same by construction. The same 109 sites are converted (`git diff` of the 35 files is small per file); two cases needed more than the two lines (`sb_structure.js` keeps a reference to the function below it for its own tab planning, and a guard that used the removed variable in `continue_learning.js` and `test_prep.js`).

**Guarded.**
- `node tools/wrappers_audit.js --check` (CI): runs the page's scripts in order and fails when any script replaces a global function itself instead of going through SBHooks. Before: 53 functions / 109 replacements outside any registry; now 0.
- `tests/contract/hooks.json` + `node tests/hooks/hooks.js` (CI): who extends which function, in which order (109 registrations over 53 functions); changing it needs `--update` and a reason.
- The HTML snapshot of every chapter and tab (9,710 renders, `tools/snapshot_html.js`) is identical before and after, on the normal page and on the lazy page; `tests/hooks/hooks.js` also checks that the hooked modules still do their side jobs (continue-learning records a chapter, the Class 5 reader renders through the hook, a subject no reader owns reaches the original).
- Registry unit tests: order, `this`, late registration, `replace`, loud failure when the function does not exist, `reset`.

**Rule from now on** (`CONTRIBUTING.md`): never assign `window.someFunction = ...` for a function another file defined; use `SBHooks.use` (extend) or `SBHooks.replace` (override). `wrappers_audit --check` fails the build otherwise.

## Not done in this part (honest list)

The Phase 5 plan has more: a render pipeline `SB.render(ctx)` with named hooks (`chapter:afterRender`...), **removing the 19 document-wide `MutationObserver`s** (`app.js`, `reader_tools.js`, `sb_four_lang.js`, `sb_global_ui.js`, `sb_mcq.js`, `sb_medium.js`, `sb_rtl.js`, `sb_structure.js` x2, `sb_topic_practice.js`, `sb_trace.js`, `sb_trilingual.js`, `sb_vertical.js`, `structure_harmonizer.js`, `word_stats.js`, `sb_book_skin.js` and four Class 1/2 files), the 22 injected `<style>` blocks, `!important` below 20, replacing `eval` and the 416 inline `onclick`s with delegated handlers, rendering only the active tab, and `<html lang dir>` from the open book. None of that is done. Why the observers were left: they post-process the DOM *after* a render, which the HTML snapshot cannot see (the test sandbox has no MutationObserver that fires), so converting them needs a DOM-level comparison (jsdom with real observers) first; that comparison tool is the next step, then the observers one module at a time. Until then `wrappers_audit` guarantees only the function-wrapping half of ARCH-01.

Not verified in a real browser: nothing here changes what a browser does differently from the test sandbox, but the whole page was only ever run in the Node sandbox.
