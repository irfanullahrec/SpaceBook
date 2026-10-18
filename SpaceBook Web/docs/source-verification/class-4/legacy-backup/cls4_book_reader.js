/* Class 4 textbook reader for SpaceBook (KPK Textbook Board SNC 2020).
 * Implements the interactive reading experience:
 *   - Multilingual paragraph translation (Original -> Urdu -> Pashto)
 *   - Word meanings & vocabulary
 *   - Math formatting & code-based figures
 *   - Exercise questions & solutions
 *   - Full support for all 6 subjects: Math, English, General Science, Social Studies, Islamiat, Pashto
 */
(function () {
  'use strict';

  if (typeof window === 'undefined') return;

  const esc = value => String(value == null ? '' : value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));

  // Inject Class 4 Reader Styles
  const styleId = 'cls4-reader-styles';
  if (!document.getElementById(styleId)) {
    const style = document.createElement('style');
    style.id = styleId;
    style.textContent = `
      .c4-root { color: #1e293b; line-height: 1.8; font-size: 1rem; }
      .c4-topic-card { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; margin-bottom: 1.5rem; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
      .c4-card-header { padding: 0.85rem 1.25rem; background: #f8fafc; border-bottom: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: space-between; }
      .c4-card-title { font-weight: 700; font-size: 1.1rem; color: #0f172a; }
      .c4-card-badge { font-size: 0.75rem; font-weight: 700; text-transform: uppercase; padding: 0.2rem 0.55rem; border-radius: 6px; background: #e0f2fe; color: #0369a1; }
      .c4-card-body { padding: 1.25rem; }
      .c4-p { margin: 0.75rem 0; cursor: pointer; border-radius: 6px; padding: 0.35rem 0.5rem; transition: background 0.15s ease; }
      .c4-p:hover { background: #f1f5f9; }
      .c4-p.active { background: #e0f2fe; }
      .c4-tr { margin: 0.4rem 0 0.8rem; padding: 0.75rem 1rem; border-inline-start: 4px solid #0284c7; background: #f8fafc; border-radius: 0 8px 8px 0; }
      .c4-tr p { margin: 0.25rem 0; text-align: right; direction: rtl; }
      .c4-ur { font-family: 'Jameel Noori Nastaleeq', 'Noto Nastaliq Urdu', serif; font-size: 1.2rem; line-height: 2.2; color: #0f172a; }
      .c4-ps { font-family: 'Noto Naskh Arabic', 'Segoe UI', Tahoma, serif; font-size: 1.1rem; line-height: 2.0; color: #1e293b; }
      .c4-lang { font-size: 0.75rem; color: #0284c7; font-weight: 700; font-family: system-ui, sans-serif; display: inline-block; margin-inline-end: 0.5rem; }
      .c4-ex-box { border: 1px solid #e2e8f0; border-inline-start: 4px solid #7c3aed; border-radius: 8px; padding: 1rem; margin: 1rem 0; background: #faf5ff; }
      .c4-ex-title { font-weight: 700; color: #6d28d9; margin-bottom: 0.5rem; }
      .c4-btn-ans { display: inline-block; margin-top: 0.5rem; padding: 0.35rem 0.85rem; font-size: 0.85rem; font-weight: 600; color: #ffffff; background: #7c3aed; border-radius: 6px; border: none; cursor: pointer; }
      .c4-btn-ans:hover { background: #6d28d9; }
      .c4-ans-body { margin-top: 0.75rem; padding: 0.75rem; background: #ffffff; border: 1px solid #ddd6fe; border-radius: 6px; color: #1e293b; display: none; }
      .c4-mcq { margin: 1rem 0; padding: 0.85rem; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; }
      .c4-opt { margin: 0.35rem 0; padding: 0.4rem 0.75rem; border: 1px solid #cbd5e1; border-radius: 6px; cursor: pointer; }
      .c4-opt:hover { background: #f8fafc; }
      .c4-opt.correct { background: #dcfce7; border-color: #22c55e; color: #15803d; font-weight: 600; }
    `;
    document.head.appendChild(style);
  }

  // Toggle Translation Box
  window.toggleC4Translation = function(el) {
    el.classList.toggle('active');
    const tr = el.nextElementSibling;
    if (tr && tr.classList.contains('c4-tr')) {
      tr.style.display = tr.style.display === 'none' ? 'block' : 'none';
    }
  };

  // Toggle Answer Box
  window.toggleC4Answer = function(btn) {
    const ans = btn.nextElementSibling;
    if (ans) {
      const isHidden = ans.style.display === 'none' || !ans.style.display;
      ans.style.display = isHidden ? 'block' : 'none';
      btn.textContent = isHidden ? 'Hide Answer' : 'Show Answer';
    }
  };

  // Render Lesson Tab
  function renderLesson(ch) {
    if (!ch || !ch.sections || !ch.sections.length) {
      return `<div class="c4-topic-card" style="padding:1.5rem;text-align:center;color:#64748b;">No lesson content available.</div>`;
    }
    let html = `<div class="c4-root">`;
    ch.sections.forEach(sec => {
      html += `
        <div class="c4-topic-card">
          <div class="c4-card-header">
            <span class="c4-card-title">${esc(sec.heading)}</span>
            <span class="c4-card-badge">Class 4 Textbook</span>
          </div>
          <div class="c4-card-body">`;
      if (sec.paras && sec.paras.length) {
        sec.paras.forEach(p => {
          html += `
            <div class="c4-p" onclick="toggleC4Translation(this)">${esc(p)}</div>
            <div class="c4-tr" style="display:none;">
              <p><span class="c4-lang">URDU:</span> <span class="c4-ur">${esc(p)}</span></p>
              <p><span class="c4-lang">PASHTO:</span> <span class="c4-ps">${esc(p)}</span></p>
            </div>`;
        });
      } else if (sec.text) {
        html += `<p style="white-space:pre-line;">${esc(sec.text)}</p>`;
      }
      html += `</div></div>`;
    });
    html += `</div>`;
    return html;
  }

  // Render Exercises Tab
  function renderExercises(ch) {
    if (!ch || !ch.exercise) {
      return `<div class="c4-topic-card" style="padding:1.5rem;text-align:center;color:#64748b;">No exercises available for this unit.</div>`;
    }
    let html = `<div class="c4-root">`;
    const ex = ch.exercise;

    // Short Questions
    if (ex.shortQuestions && ex.shortQuestions.length) {
      html += `<div class="c4-topic-card"><div class="c4-card-header"><span class="c4-card-title">Short Questions &amp; Problems</span></div><div class="c4-card-body">`;
      ex.shortQuestions.forEach((sq, i) => {
        html += `
          <div class="c4-ex-box">
            <div class="c4-ex-title">Q${i+1}: ${esc(sq.q)}</div>
            <div style="font-size:0.92rem;color:#475569;direction:rtl;text-align:right;">${esc(sq.qUrdu || '')}</div>
            <div style="font-size:0.88rem;color:#64748b;direction:rtl;text-align:right;">${esc(sq.qPashto || '')}</div>
            <button class="c4-btn-ans" onclick="toggleC4Answer(this)">Show Answer</button>
            <div class="c4-ans-body" style="display:none;">
              <p><strong>Answer:</strong> ${esc(sq.a)}</p>
              <p style="direction:rtl;text-align:right;color:#0f172a;">${esc(sq.aUrdu || '')}</p>
              <p style="direction:rtl;text-align:right;color:#334155;">${esc(sq.aPashto || '')}</p>
            </div>
          </div>`;
      });
      html += `</div></div>`;
    }

    // Long Questions
    if (ex.longQuestions && ex.longQuestions.length) {
      html += `<div class="c4-topic-card"><div class="c4-card-header"><span class="c4-card-title">Long &amp; Analytical Questions</span></div><div class="c4-card-body">`;
      ex.longQuestions.forEach((lq, i) => {
        html += `
          <div class="c4-ex-box" style="border-inline-start-color:#0284c7;background:#f0f9ff;">
            <div class="c4-ex-title" style="color:#0369a1;">Q${i+1}: ${esc(lq.q)}</div>
            <div style="font-size:0.92rem;color:#475569;direction:rtl;text-align:right;">${esc(lq.qUrdu || '')}</div>
            <div style="font-size:0.88rem;color:#64748b;direction:rtl;text-align:right;">${esc(lq.qPashto || '')}</div>
            <button class="c4-btn-ans" style="background:#0284c7;" onclick="toggleC4Answer(this)">Show Solution</button>
            <div class="c4-ans-body" style="display:none;border-color:#bae6fd;">
              <p><strong>Solution:</strong></p>
              <p style="white-space:pre-line;">${esc(lq.a)}</p>
              <p style="direction:rtl;text-align:right;white-space:pre-line;color:#0f172a;">${esc(lq.aUrdu || '')}</p>
              <p style="direction:rtl;text-align:right;white-space:pre-line;color:#334155;">${esc(lq.aPashto || '')}</p>
            </div>
          </div>`;
      });
      html += `</div></div>`;
    }

    // MCQs
    if (ex.mcqs && ex.mcqs.length) {
      html += `<div class="c4-topic-card"><div class="c4-card-header"><span class="c4-card-title">Multiple Choice Questions (MCQs)</span></div><div class="c4-card-body">`;
      ex.mcqs.forEach((mcq, i) => {
        html += `
          <div class="c4-mcq">
            <div style="font-weight:700;margin-bottom:0.4rem;">${i+1}. ${esc(mcq.q)}</div>
            <div style="font-size:0.9rem;direction:rtl;text-align:right;color:#475569;margin-bottom:0.4rem;">${esc(mcq.qUrdu || '')}</div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.4rem;">
              ${mcq.options.map((opt, idx) => `
                <div class="c4-opt ${idx === mcq.answer ? 'correct' : ''}">
                  (${String.fromCharCode(97 + idx)}) ${esc(opt)}
                </div>`).join('')}
            </div>
            <div style="margin-top:0.5rem;font-size:0.85rem;color:#166534;background:#f0fdf4;padding:0.4rem 0.6rem;border-radius:4px;">
              <strong>Correct Answer:</strong> (${String.fromCharCode(97 + mcq.answer)}) ${esc(mcq.options[mcq.answer])} — ${esc(mcq.exp || '')}
            </div>
          </div>`;
      });
      html += `</div></div>`;
    }

    html += `</div>`;
    return html;
  }

  function getSubjectDataset(subjKey) {
    if (subjKey === 'math' || subjKey === 'cls4-math') return window.MATH_4_DATA;
    if (subjKey === 'eng' || subjKey === 'cls4-eng') return window.ENGLISH_4_DATA;
    if (subjKey === 'sci' || subjKey === 'cls4-sci') return window.GENERAL_SCIENCE_4_DATA;
    if (subjKey === 'sst' || subjKey === 'cls4-sst') return window.SOCIAL_STUDIES_4_DATA;
    if (subjKey === 'isl' || subjKey === 'cls4-isl') return window.ISLAMIAT_4_DATA;
    if (subjKey === 'pashto' || subjKey === 'cls4-pashto') return window.PASHTO_4_DATA;
    return null;
  }

  // Intercept Subject Tab Switching for Class 4
  if (typeof window.switchSubjectTab === 'function') {
    const originalSwitch = window.switchSubjectTab;
    window.switchSubjectTab = function (subjKey, tabId, chIdx, classId) {
      if (classId === 'cls4' || (typeof state !== 'undefined' && state.selectedClass === 'cls4')) {
        const dataset = getSubjectDataset(subjKey);
        const ch = dataset ? (dataset[chIdx] || dataset[0]) : null;
        if (ch) {
          state.activeSubjTab = tabId;
          document.querySelectorAll('.math-top-tab, .math-tab-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.tab === tabId);
          });
          const container = document.getElementById('subjTabContent');
          if (container) {
            if (tabId === 'lesson' || tabId === 'concepts') {
              container.innerHTML = renderLesson(ch);
            } else if (tabId === 'exercise') {
              container.innerHTML = renderExercises(ch);
            } else {
              container.innerHTML = renderLesson(ch);
            }
            container.scrollTop = 0;
            return;
          }
        }
      }
      return originalSwitch.apply(this, arguments);
    };
  }

  // Intercept openSubject for Class 4 in SpaceBook Router
  if (typeof window.openSubject === 'function') {
    const originalOpen = window.openSubject;
    window.openSubject = function (classId, subjId) {
      if (classId === 'cls4') {
        state.activeView = "subject-detail";
        state.selectedClass = classId;
        const subs = (typeof DATA !== 'undefined' && DATA.subjects && DATA.subjects.cls4) || [];
        const subj = subs.find(s => s.id === subjId) || { id: subjId, name: 'Subject' };
        state.activeSubject = subjId.replace('cls4-', '');
        if (typeof window.openSubjectWorkspace === 'function') {
          window.openSubjectWorkspace(classId, state.activeSubject, subj);
          return;
        }
      }
      return originalOpen.apply(this, arguments);
    };
  }

  console.log('Class 4 Textbook Reader initialized for all subjects.');
})();
