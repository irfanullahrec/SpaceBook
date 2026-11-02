# Web Updates

1. Trace Again / Count Again button moved below the picture, so it no longer covers the interactive tracing area (js/sb_trace.js).
2. Board SLOs tab now appears only on pages of Class 9 and above; Classes 1-8 pages show Exercise and Games only (js/sb_page_tabs.js).
3. Page bar rules: Lesson pages get Board SLOs (9+), Exercise and Games; Exercise pages and Learning-outcome pages get the Games button only.
4. Pages that show Board SLOs / Exercise tabs always have MCQs, SQs and LQs: none is 0, and longer pages get more questions (made from the page text).
5. Games opened from a page are made only from that page's own content (already so; kept and confirmed).
6. Pressing Space in any game pauses it on the same screen and opens a guide modal (how to win) in English, Urdu and Pashto (js/sb_arcade.js).
7. Header menu: tabs that do not fit (any zoom or window size) move into a "More" menu, so none hides behind Back/search (js/sb_chapter_tools.js).
8. Ans button now also fills empty table cells with the answer (dash/blank filling was already there) (js/sb_solve.js).
9. Download button added beside each chapter's top tabs: Solved Exercise PDF (questions + answers) and SLO-based MCQs/SQs/LQs PDF (js/sb_chapter_tools.js).
10. All Mathematics books (Classes 1-12) now show every answer in the answer modal with the animated and the worked-steps solution (js/sb_solve.js).
11. Word Stats tab shows the open chapter's own words when clicked inside a chapter; subject stats when clicked at subject level (js/word_stats.js).
12. Derived files (lazy page, offline map, service-worker version) regenerated after these changes.

Not done / limits: Solved Exercise PDF uses the answers present in the book data (items without a stored answer say "see the book's answer key"); Word Stats for a chapter counts the words of the tab currently shown; class-level stats unchanged.
