# -*- coding: utf-8 -*-
"""
Patches app.js to add:
1. switchSubjectTab handling for 'glossary', 'vocabulary', 'language', 'writing'
2. renderSubjectExerciseTab category 'agreeDisagree'
3. renderSubjectExProblems rendering for 'agreeDisagree'
4. Complete renderer functions:
   - renderEnglishGlossaryTab(ch)
   - filterEnglishGlossaryTable(val)
   - renderEnglishVocabularyTab(ch)
   - switchEnglishVocabSubTab(subTab)
   - renderEnglishVocabSubContent(ch, subTab)
   - renderEnglishUseOfLanguageTab(ch)
   - renderEnglishWritingTab(ch)
   - switchEnglishWritingSubTab(subTab)
   - renderEnglishWritingSubContent(ch, subTab)
"""

with open(r"D:\SpaceBook\SpaceBook Web\js\app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update switchSubjectTab dispatch
target_switch = """    if (tabId === 'exercise') {
      container.innerHTML = renderSubjectExerciseTab(subjKey, ch);
    } else if (tabId === 'slos') {
      container.innerHTML = renderSubjectSLOsTab(subjKey, ch);
    } else if (tabId === 'grammar') {
      container.innerHTML = renderLanguageGrammarTab(subjKey, ch);"""

replace_switch = """    if (tabId === 'exercise') {
      container.innerHTML = renderSubjectExerciseTab(subjKey, ch);
    } else if (tabId === 'glossary') {
      container.innerHTML = renderEnglishGlossaryTab(ch);
    } else if (tabId === 'vocabulary') {
      container.innerHTML = renderEnglishVocabularyTab(ch);
    } else if (tabId === 'language') {
      container.innerHTML = renderEnglishUseOfLanguageTab(ch);
    } else if (tabId === 'writing') {
      container.innerHTML = renderEnglishWritingTab(ch);
    } else if (tabId === 'slos') {
      container.innerHTML = renderSubjectSLOsTab(subjKey, ch);
    } else if (tabId === 'grammar') {
      container.innerHTML = renderLanguageGrammarTab(subjKey, ch);"""

if target_switch in content:
    content = content.replace(target_switch, replace_switch, 1)
    print("Patched switchSubjectTab dispatch successfully.")
else:
    print("Warning: target_switch not found!")

# 2. Update renderSubjectExerciseTab to include agreeDisagree category
target_cats = """  if (mcqs.length > 0) categories.push({ key: 'mcqs', name: `🎯 MCQs (${mcqs.length})` });
  if (sqs.length > 0) categories.push({ key: 'sqs', name: isUrdu ? `📝 مختصر سوالات (${sqs.length})` : `📝 Short Questions (${sqs.length})` });
  if (lqs.length > 0) categories.push({ key: 'lqs', name: isUrdu ? `📚 تفصیلی سوالات (${lqs.length})` : `📚 Long Questions (${lqs.length})` });"""

replace_cats = """  const agreeDisagree = ex.agreeDisagree || [];
  if (sqs.length > 0) categories.push({ key: 'sqs', name: isUrdu ? `📝 مختصر سوالات (${sqs.length})` : `📝 Part A: Comprehension (${sqs.length})` });
  if (agreeDisagree.length > 0) categories.push({ key: 'agreeDisagree', name: `🤝 Part B: Agree / Disagree (${agreeDisagree.length})` });
  if (mcqs.length > 0) categories.push({ key: 'mcqs', name: `🎯 MCQs (${mcqs.length})` });
  if (lqs.length > 0) categories.push({ key: 'lqs', name: isUrdu ? `📚 تفصیلی سوالات (${lqs.length})` : `📚 Long Questions (${lqs.length})` });"""

if target_cats in content:
    content = content.replace(target_cats, replace_cats, 1)
    print("Patched renderSubjectExerciseTab categories successfully.")
else:
    print("Warning: target_cats not found!")

# 3. Add agreeDisagree handling in renderSubjectExProblems
target_sq_handling = """  if (catKey === 'sqs' || catKey === 'all') {
    const sqs = ex.comprehension || ex.shortQuestions || ex.sqs || ex.crqs || [];"""

replace_sq_handling = """  if (catKey === 'agreeDisagree' || catKey === 'all') {
    const adList = ex.agreeDisagree || [];
    if (adList.length > 0) {
      const adChunk = `
        <div style="margin-bottom:1.5rem;">
          <div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:8px;padding:0.75rem 1rem;margin-bottom:1rem;">
            <strong style="color:#166534;font-size:0.95rem;">🤝 B) Respond to each statement by writing an explanation as to why you agree or disagree:</strong>
            <div style="font-size:0.84rem;color:#374151;margin-top:0.2rem;">KPK Textbook Board Grade 8 English Exercise Part B — Reasoned personal responses and reflections.</div>
          </div>
          ${adList.map((ad, idx) => `
            <div class="math-topic-card" style="margin-bottom:1rem;border-left:4px solid #16a34a;padding:1rem;">
              <div style="display:flex;align-items:center;justify-content:space-between;gap:0.5rem;margin-bottom:0.5rem;flex-wrap:wrap;">
                <span class="math-badge" style="background:#dcfce7;color:#15803d;font-weight:700;">Statement ${ad.statementNo || (idx + 1)}</span>
                <span style="background:${ad.position && ad.position.toLowerCase().includes('disagree') ? '#fee2e2' : '#ecfdf5'};color:${ad.position && ad.position.toLowerCase().includes('disagree') ? '#b91c1c' : '#047857'};font-weight:800;font-size:0.8rem;padding:0.25rem 0.65rem;border-radius:99px;">
                  ${ad.position || 'Reasoned Response'}
                </span>
              </div>
              <div style="font-weight:700;color:#0f172a;font-size:1rem;margin-bottom:0.6rem;">
                ${ad.statement}
              </div>
              <div style="color:#64748b;font-size:0.84rem;font-style:italic;margin-bottom:0.6rem;">
                ${ad.prompt || 'I agree / disagree because:'}
              </div>
              <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:0.85rem;line-height:1.7;color:#1e293b;font-size:0.9rem;margin-bottom:0.6rem;">
                <strong>Explanation:</strong> ${ad.explanation}
              </div>
              ${ad.urduExplanation ? `
                <div style="background:#fffbeb;border:1px solid #fde68a;border-radius:6px;padding:0.75rem;direction:rtl;text-align:right;font-family:'Jameel Noori Nastaleeq',serif;font-size:1.05rem;line-height:2;color:#92400e;margin-bottom:0.4rem;">
                  <strong>اردو تشریح:</strong> ${ad.urduExplanation}
                </div>` : ''}
              ${ad.pashtoExplanation ? `
                <div style="background:#f0fdfa;border:1px solid #ccfbf1;border-radius:6px;padding:0.75rem;direction:rtl;text-align:right;font-family:'Pashto Kror Asmat',serif;font-size:1.02rem;line-height:2;color:#115e59;">
                  <strong>پښتو وضاحت:</strong> ${ad.pashtoExplanation}
                </div>` : ''}
            </div>
          `).join('')}
        </div>`;
      if (catKey === 'agreeDisagree') return adChunk;
      res += adChunk;
    }
  }

  if (catKey === 'sqs' || catKey === 'all') {
    const sqs = ex.comprehension || ex.shortQuestions || ex.sqs || ex.crqs || [];"""

if target_sq_handling in content:
    content = content.replace(target_sq_handling, replace_sq_handling, 1)
    print("Patched renderSubjectExProblems agreeDisagree handling successfully.")
else:
    print("Warning: target_sq_handling not found!")

# 4. Append dedicated English tab renderers
new_functions = """
// ─── DEDICATED ENGLISH TABS RENDERERS (GLOSSARY, VOCABULARY, USE OF LANGUAGE, WRITING) ─────
function renderEnglishGlossaryTab(ch) {
  const glossary = ch.glossary || ch.words || [];
  return `
    <div>
      <div style="background:#eff6ff;border:1px solid #bfdbfe;border-radius:8px;padding:0.9rem 1.1rem;margin-bottom:1.25rem;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:0.75rem;">
        <div>
          <span style="font-weight:800;color:#1e40af;font-size:1.05rem;">📚 Textbook Glossary — ${ch.title}</span>
          <div style="font-size:0.86rem;color:#334155;margin-top:0.25rem;">100% Verbatim Glossary Table directly matched to KPTBB Grade 8 Textbook pages.</div>
        </div>
        <div style="display:flex;align-items:center;gap:0.5rem;">
          <span style="background:#dbeafe;color:#1e40af;font-weight:700;font-size:0.8rem;padding:0.3rem 0.75rem;border-radius:99px;">
            ${glossary.length} Glossary Terms
          </span>
        </div>
      </div>

      <div style="margin-bottom:1rem;">
        <input type="text" class="pcs-input" placeholder="🔍 Search Glossary words, meanings, Urdu, or Pashto..." 
               oninput="filterEnglishGlossaryTable(this.value)" 
               style="width:100%;max-width:420px;padding:0.5rem 0.85rem;font-size:0.88rem;border:1px solid #cbd5e1;border-radius:6px;background:#ffffff;">
      </div>

      <div class="words-table-wrap" style="overflow-x:auto;">
        <table class="words-grid-table" id="englishGlossaryTable" style="width:100%;border-collapse:collapse;">
          <thead>
            <tr style="background:#f1f5f9;">
              <th style="width:16%;padding:0.65rem 0.85rem;text-align:left;border:1px solid #cbd5e1;">Word &amp; POS</th>
              <th style="width:28%;padding:0.65rem 0.85rem;text-align:left;border:1px solid #cbd5e1;">Textbook Meaning</th>
              <th style="width:20%;padding:0.65rem 0.85rem;text-align:right;border:1px solid #cbd5e1;direction:rtl;">اردو معنی</th>
              <th style="width:18%;padding:0.65rem 0.85rem;text-align:right;border:1px solid #cbd5e1;direction:rtl;">پښتو معنی</th>
              <th style="width:18%;padding:0.65rem 0.85rem;text-align:left;border:1px solid #cbd5e1;">Contextual Sentence</th>
            </tr>
          </thead>
          <tbody>
            ${glossary.map((w, idx) => `
              <tr class="glossary-row" style="background:${idx % 2 === 0 ? '#ffffff' : '#f8fafc'};">
                <td style="padding:0.75rem 0.85rem;border:1px solid #e2e8f0;font-weight:700;color:#0f172a;">
                  <div>${w.word}</div>
                  <span style="font-size:0.75rem;color:#64748b;font-weight:600;text-transform:lowercase;">(${w.pos || 'noun'})</span>
                </td>
                <td style="padding:0.75rem 0.85rem;border:1px solid #e2e8f0;color:#334155;line-height:1.5;">${w.meaning}</td>
                <td style="padding:0.75rem 0.85rem;border:1px solid #e2e8f0;direction:rtl;text-align:right;font-family:'Jameel Noori Nastaleeq',serif;font-size:1.05rem;color:#0f766e;">${w.urdu || ''}</td>
                <td style="padding:0.75rem 0.85rem;border:1px solid #e2e8f0;direction:rtl;text-align:right;font-family:'Pashto Kror Asmat',serif;font-size:1.02rem;color:#0369a1;">${w.pashto || ''}</td>
                <td style="padding:0.75rem 0.85rem;border:1px solid #e2e8f0;font-size:0.85rem;color:#475569;font-style:italic;">${w.sentence || ''}</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
    </div>
  `;
}

function filterEnglishGlossaryTable(val) {
  const query = (val || '').toLowerCase().trim();
  const rows = document.querySelectorAll('#englishGlossaryTable tbody tr');
  rows.forEach(r => {
    const text = r.textContent.toLowerCase();
    r.style.display = text.includes(query) ? '' : 'none';
  });
}

function renderEnglishVocabularyTab(ch) {
  const vs = ch.vocabularySection || {};
  const partA = vs.partA_dictionary || [];
  const partB = vs.partB_silentLetters || [];
  const partC = vs.partC_syllabification || [];
  const activeSubTab = state.activeEngVocabSubTab || 'partA';

  return `
    <div>
      <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:0.85rem 1.1rem;margin-bottom:1.25rem;">
        <span style="font-weight:800;color:#0f172a;font-size:1rem;">🔤 Textbook Vocabulary Suite — ${ch.title}</span>
        <div style="font-size:0.85rem;color:#64748b;margin-top:0.2rem;">Parts of Speech Abbreviations, Silent Letters, and Syllable Demarcation directly from KPTBB Grade 8.</div>
      </div>

      <div class="category-sub-tabs-bar" style="margin-bottom:1.25rem;">
        <button class="category-sub-tab-btn ${activeSubTab === 'partA' ? 'active' : ''}" onclick="switchEnglishVocabSubTab('partA')">
          📖 A. Dictionary &amp; Parts of Speech (${partA.length})
        </button>
        <button class="category-sub-tab-btn ${activeSubTab === 'partB' ? 'active' : ''}" onclick="switchEnglishVocabSubTab('partB')">
          🔇 B. Silent Letters (${partB.length})
        </button>
        <button class="category-sub-tab-btn ${activeSubTab === 'partC' ? 'active' : ''}" onclick="switchEnglishVocabSubTab('partC')">
          ✂️ C. Syllable Demarcation (${partC.length})
        </button>
      </div>

      <div id="engVocabContent">
        ${renderEnglishVocabSubContent(ch, activeSubTab)}
      </div>
    </div>
  `;
}

function switchEnglishVocabSubTab(subTab) {
  state.activeEngVocabSubTab = subTab;
  const chList = getSubjectChapterList('eng', state.selectedClass);
  const ch = chList[state.selectedSubjChapter || 0];
  const container = document.getElementById('engVocabContent');
  if (container && ch) {
    document.querySelectorAll('.category-sub-tabs-bar .category-sub-tab-btn').forEach(b => {
      b.classList.toggle('active', b.getAttribute('onclick') && b.getAttribute('onclick').includes("'" + subTab + "'"));
    });
    container.innerHTML = renderEnglishVocabSubContent(ch, subTab);
  }
}

function renderEnglishVocabSubContent(ch, subTab) {
  const vs = ch.vocabularySection || {};
  if (subTab === 'partA') {
    const partA = vs.partA_dictionary || [];
    return `
      <div>
        <div style="background:#eff6ff;border:1px solid #bfdbfe;border-radius:6px;padding:0.75rem 1rem;margin-bottom:1rem;font-size:0.88rem;color:#1e40af;">
          <strong>A. Find the meaning of the following words from the dictionary and identify the parts of speech of the word through abbreviation used:</strong>
        </div>
        <div class="words-table-wrap" style="overflow-x:auto;">
          <table class="words-grid-table" style="width:100%;border-collapse:collapse;">
            <thead>
              <tr style="background:#f1f5f9;">
                <th style="width:18%;padding:0.65rem 0.85rem;border:1px solid #cbd5e1;text-align:left;">Word</th>
                <th style="width:18%;padding:0.65rem 0.85rem;border:1px solid #cbd5e1;text-align:left;">Part of Speech &amp; Abbr.</th>
                <th style="width:34%;padding:0.65rem 0.85rem;border:1px solid #cbd5e1;text-align:left;">Dictionary Definition</th>
                <th style="width:15%;padding:0.65rem 0.85rem;border:1px solid #cbd5e1;direction:rtl;text-align:right;">اردو معنی</th>
                <th style="width:15%;padding:0.65rem 0.85rem;border:1px solid #cbd5e1;text-align:left;">Example Sentence</th>
              </tr>
            </thead>
            <tbody>
              ${partA.map(item => `
                <tr>
                  <td style="padding:0.75rem;border:1px solid #e2e8f0;font-weight:700;color:#0f172a;">${item.word}</td>
                  <td style="padding:0.75rem;border:1px solid #e2e8f0;">
                    <span style="background:#e0f2fe;color:#0369a1;font-weight:700;font-size:0.78rem;padding:0.2rem 0.5rem;border-radius:4px;">${item.abbr || 'n.'}</span>
                    <span style="font-size:0.82rem;color:#64748b;margin-left:0.3rem;">${item.pos}</span>
                  </td>
                  <td style="padding:0.75rem;border:1px solid #e2e8f0;color:#334155;font-size:0.88rem;">${item.meaning}</td>
                  <td style="padding:0.75rem;border:1px solid #e2e8f0;direction:rtl;text-align:right;font-family:'Jameel Noori Nastaleeq',serif;font-size:1.05rem;color:#0f766e;">${item.urdu || ''}</td>
                  <td style="padding:0.75rem;border:1px solid #e2e8f0;font-size:0.84rem;color:#475569;font-style:italic;">${item.sentence || ''}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      </div>`;
  } else if (subTab === 'partB') {
    const partB = vs.partB_silentLetters || [];
    return `
      <div>
        <div style="background:#fff7ed;border:1px solid #fed7aa;border-radius:6px;padding:0.75rem 1rem;margin-bottom:1.25rem;font-size:0.88rem;color:#9a3412;">
          <strong>B. Underline and identify the silent letters in the following words:</strong>
          <div style="font-size:0.82rem;margin-top:0.2rem;color:#7c2d12;">Textbook silent letter identification drills with phonetic rules.</div>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:0.85rem;">
          ${partB.map(item => `
            <div class="math-topic-card" style="padding:0.9rem;border-left:4px solid #ea580c;display:flex;flex-direction:column;justify-content:space-between;">
              <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.4rem;">
                <span style="font-size:1.15rem;font-weight:800;color:#0f172a;letter-spacing:0.02em;">
                  ${item.word.split('').map(ch => ch.toLowerCase() === item.silentLetter.toLowerCase() 
                    ? `<span style=\"color:#dc2626;text-decoration:underline;text-decoration-color:#dc2626;text-underline-offset:4px;font-weight:900;background:#fee2e2;padding:0 2px;border-radius:2px;\">${ch}</span>` 
                    : ch).join('')}
                </span>
                <span style="background:#fee2e2;color:#b91c1c;font-weight:800;font-size:0.75rem;padding:0.2rem 0.5rem;border-radius:99px;">
                  Silent '${item.silentLetter}'
                </span>
              </div>
              <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.4rem;">
                <span style="font-family:monospace;font-size:0.86rem;color:#0284c7;background:#f0f9ff;padding:0.15rem 0.4rem;border-radius:4px;">${item.phonetic || ''}</span>
              </div>
              <div style="font-size:0.82rem;color:#475569;line-height:1.4;">${item.rule || 'Silent in standard pronunciation.'}</div>
            </div>
          `).join('')}
        </div>
      </div>`;
  } else {
    const partC = vs.partC_syllabification || [];
    return `
      <div>
        <div style="background:#f5f3ff;border:1px solid #ddd6fe;border-radius:6px;padding:0.75rem 1rem;margin-bottom:1.25rem;font-size:0.88rem;color:#5b21b6;">
          <strong>C. Use a dictionary to demarcate the following words into syllables:</strong>
          <div style="font-size:0.82rem;margin-top:0.2rem;color:#6d28d9;">Syllable demarcations with dot breaks (·), stress marks, and count metrics.</div>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:0.85rem;">
          ${partC.map(item => `
            <div class="math-topic-card" style="padding:0.9rem;border-left:4px solid #7c3aed;">
              <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.4rem;">
                <span style="font-size:1.05rem;font-weight:800;color:#0f172a;">${item.word}</span>
                <span style="background:#ede9fe;color:#6d28d9;font-weight:800;font-size:0.75rem;padding:0.2rem 0.5rem;border-radius:99px;">
                  ${item.count} Syllables
                </span>
              </div>
              <div style="background:#faf5ff;border:1px solid #e9d5ff;border-radius:4px;padding:0.4rem 0.6rem;font-family:monospace;font-size:0.92rem;color:#5b21b6;font-weight:700;margin-bottom:0.4rem;letter-spacing:0.04em;">
                ${item.demarcation}
              </div>
              <div style="font-size:0.8rem;color:#64748b;font-family:monospace;">${item.phonetic || ''}</div>
            </div>
          `).join('')}
        </div>
      </div>`;
  }
}

function renderEnglishUseOfLanguageTab(ch) {
  const lang = ch.useOfLanguage || {};
  const shorts = lang.shortVowels || [];
  const longs = lang.longVowels || [];
  const drills = lang.practiceDrills || [];

  return `
    <div>
      <div style="background:#eff6ff;border:1px solid #bfdbfe;border-radius:8px;padding:0.9rem 1.1rem;margin-bottom:1.25rem;">
        <span style="font-weight:800;color:#1e40af;font-size:1.05rem;">🗣️ Use of Language: ${lang.title || 'Long and Short Vowel Sounds'}</span>
        <div style="font-size:0.86rem;color:#334155;margin-top:0.35rem;line-height:1.6;">
          ${lang.overview || 'When a vowel sounds like its name, this is called a long sound. A vowel letter can also have short sounds. Whether a vowel has a long sound, a short sound, or remains silent, depends on its position in a word and the letters around it.'}
        </div>
      </div>

      <!-- Short Vowels Table -->
      <div class="math-topic-card" style="margin-bottom:1.25rem;padding:1rem;">
        <h4 style="color:#0284c7;font-size:1rem;font-weight:800;margin-bottom:0.75rem;display:flex;align-items:center;gap:0.4rem;">
          <span>🔊</span> Short Vowels (The most common sound for each vowel)
        </h4>
        <div class="words-table-wrap" style="overflow-x:auto;">
          <table class="words-grid-table" style="width:100%;border-collapse:collapse;">
            <thead>
              <tr style="background:#f1f5f9;">
                <th style="width:12%;padding:0.6rem 0.8rem;border:1px solid #cbd5e1;text-align:center;">Vowel</th>
                <th style="width:18%;padding:0.6rem 0.8rem;border:1px solid #cbd5e1;text-align:center;">Phonetic IPA</th>
                <th style="width:40%;padding:0.6rem 0.8rem;border:1px solid #cbd5e1;text-align:left;">Textbook Example Words</th>
                <th style="width:30%;padding:0.6rem 0.8rem;border:1px solid #cbd5e1;text-align:left;">Pronunciation Guide</th>
              </tr>
            </thead>
            <tbody>
              ${shorts.map(v => `
                <tr>
                  <td style="padding:0.7rem;border:1px solid #e2e8f0;text-align:center;font-weight:900;font-size:1.2rem;color:#0284c7;">${v.vowel}</td>
                  <td style="padding:0.7rem;border:1px solid #e2e8f0;text-align:center;font-family:monospace;font-weight:700;font-size:1.05rem;color:#0f766e;">${v.ipa}</td>
                  <td style="padding:0.7rem;border:1px solid #e2e8f0;">
                    ${(v.examples || []).map(ex => `<span style=\"background:#e0f2fe;color:#0369a1;font-weight:700;font-size:0.85rem;padding:0.2rem 0.55rem;border-radius:4px;margin-right:0.35rem;display:inline-block;margin-bottom:0.2rem;\">${ex}</span>`).join('')}
                  </td>
                  <td style="padding:0.7rem;border:1px solid #e2e8f0;font-size:0.85rem;color:#475569;">${v.note || ''}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      </div>

      <!-- Long Vowels Table -->
      ${longs.length > 0 ? `
        <div class="math-topic-card" style="margin-bottom:1.25rem;padding:1rem;">
          <h4 style="color:#7c3aed;font-size:1rem;font-weight:800;margin-bottom:0.75rem;display:flex;align-items:center;gap:0.4rem;">
            <span>🎵</span> Long Vowels (Vowel sounds like its alphabet name)
          </h4>
          <div class="words-table-wrap" style="overflow-x:auto;">
            <table class="words-grid-table" style="width:100%;border-collapse:collapse;">
              <thead>
                <tr style="background:#f1f5f9;">
                  <th style="width:12%;padding:0.6rem 0.8rem;border:1px solid #cbd5e1;text-align:center;">Vowel</th>
                  <th style="width:18%;padding:0.6rem 0.8rem;border:1px solid #cbd5e1;text-align:center;">Phonetic IPA</th>
                  <th style="width:40%;padding:0.6rem 0.8rem;border:1px solid #cbd5e1;text-align:left;">Example Words</th>
                  <th style="width:30%;padding:0.6rem 0.8rem;border:1px solid #cbd5e1;text-align:left;">Spelling Rule</th>
                </tr>
              </thead>
              <tbody>
                ${longs.map(v => `
                  <tr>
                    <td style="padding:0.7rem;border:1px solid #e2e8f0;text-align:center;font-weight:900;font-size:1.2rem;color:#7c3aed;">${v.vowel}</td>
                    <td style="padding:0.7rem;border:1px solid #e2e8f0;text-align:center;font-family:monospace;font-weight:700;font-size:1.05rem;color:#5b21b6;">${v.ipa}</td>
                    <td style="padding:0.7rem;border:1px solid #e2e8f0;">
                      ${(v.examples || []).map(ex => `<span style=\"background:#ede9fe;color:#5b21b6;font-weight:700;font-size:0.85rem;padding:0.2rem 0.55rem;border-radius:4px;margin-right:0.35rem;display:inline-block;margin-bottom:0.2rem;\">${ex}</span>`).join('')}
                    </td>
                    <td style="padding:0.7rem;border:1px solid #e2e8f0;font-size:0.85rem;color:#475569;">${v.rule || ''}</td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>` : ''}

      <!-- Sound Contrast Drills -->
      ${drills.length > 0 ? `
        <div class="math-topic-card" style="padding:1rem;">
          <h4 style="color:#0f172a;font-size:0.98rem;font-weight:800;margin-bottom:0.65rem;">Contrast Drills:</h4>
          ${drills.map(d => `
            <div>
              <div style="font-weight:700;font-size:0.9rem;color:#0369a1;margin-bottom:0.4rem;">${d.drill}</div>
              <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:0.6rem;">
                ${(d.items || []).map(it => `
                  <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:0.6rem 0.8rem;font-size:0.85rem;">
                    <strong>${it.word}</strong>: <span style="color:#0f766e;font-weight:700;">${it.sound}</span>
                    <div style="font-size:0.78rem;color:#64748b;margin-top:0.2rem;">${it.contrast}</div>
                  </div>
                `).join('')}
              </div>
            </div>
          `).join('')}
        </div>` : ''}
    </div>
  `;
}

function renderEnglishWritingTab(ch) {
  const w = ch.writing || {};
  const activeSubTab = state.activeEngWritingSubTab || 'partA';

  return `
    <div>
      <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:0.85rem 1.1rem;margin-bottom:1.25rem;">
        <span style="font-weight:800;color:#0f172a;font-size:1rem;">📝 Textbook Writing Suite — ${ch.title}</span>
        <div style="font-size:0.85rem;color:#64748b;margin-top:0.2rem;">Mind Mapping, Formal Summaries, Textual Analysis, and Unified Model Paragraphs from KPTBB Grade 8.</div>
      </div>

      <div class="category-sub-tabs-bar" style="margin-bottom:1.25rem;">
        <button class="category-sub-tab-btn ${activeSubTab === 'partA' ? 'active' : ''}" onclick="switchEnglishWritingSubTab('partA')">
          🗺️ A. Mind Map &amp; Summary
        </button>
        <button class="category-sub-tab-btn ${activeSubTab === 'partB' ? 'active' : ''}" onclick="switchEnglishWritingSubTab('partB')">
          🔍 B. Textual Analysis (Verbs &amp; Modifiers)
        </button>
        <button class="category-sub-tab-btn ${activeSubTab === 'partC' ? 'active' : ''}" onclick="switchEnglishWritingSubTab('partC')">
          ✍️ C. Model Paragraph Writing
        </button>
      </div>

      <div id="engWritingContent">
        ${renderEnglishWritingSubContent(ch, activeSubTab)}
      </div>
    </div>
  `;
}

function switchEnglishWritingSubTab(subTab) {
  state.activeEngWritingSubTab = subTab;
  const chList = getSubjectChapterList('eng', state.selectedClass);
  const ch = chList[state.selectedSubjChapter || 0];
  const container = document.getElementById('engWritingContent');
  if (container && ch) {
    document.querySelectorAll('.category-sub-tabs-bar .category-sub-tab-btn').forEach(b => {
      b.classList.toggle('active', b.getAttribute('onclick') && b.getAttribute('onclick').includes("'" + subTab + "'"));
    });
    container.innerHTML = renderEnglishWritingSubContent(ch, subTab);
  }
}

function renderEnglishWritingSubContent(ch, subTab) {
  const w = ch.writing || {};
  if (subTab === 'partA') {
    const mm = w.mindMap || { branches: [] };
    return `
      <div>
        <!-- Interactive Visual Mind Map Diagram -->
        <div class="math-topic-card" style="margin-bottom:1.25rem;padding:1.25rem;background:#faf5ff;border:1.5px solid #e9d5ff;">
          <h4 style="color:#6b21a8;font-size:1.05rem;font-weight:800;margin-bottom:1rem;display:flex;align-items:center;gap:0.4rem;">
            <span>🗺️</span> ${mm.title || 'Mind Map'}
          </h4>
          
          <div style="display:flex;flex-direction:column;align-items:center;gap:1.5rem;margin:1rem 0;">
            <!-- Central Bubble -->
            <div style="background:#7c3aed;color:#ffffff;font-weight:800;font-size:1.05rem;padding:0.9rem 1.75rem;border-radius:99px;box-shadow:0 4px 6px -1px rgba(124,58,237,0.3);text-align:center;max-width:380px;">
              ⭐ ${mm.centralTheme || ch.title}
            </div>

            <!-- Branches Grid -->
            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1rem;width:100%;">
              ${(mm.branches || []).map((br, bIdx) => `
                <div style="background:#ffffff;border:1.5px solid #d8b4fe;border-radius:8px;padding:0.9rem;box-shadow:0 2px 4px rgba(0,0,0,0.03);">
                  <div style="font-weight:800;color:#6b21a8;font-size:0.94rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.35rem;">
                    <span style="background:#f3e8ff;border-radius:50%;width:22px;height:22px;display:inline-flex;align-items:center;justify-content:center;font-size:0.75rem;">${bIdx + 1}</span>
                    <span>${br.branchName}</span>
                  </div>
                  <ul style="margin:0;padding-left:1.1rem;font-size:0.85rem;color:#4b5563;line-height:1.6;">
                    ${(br.subIdeas || []).map(si => `<li style=\"margin-bottom:0.3rem;\">${si}</li>`).join('')}
                  </ul>
                </div>
              `).join('')}
            </div>
          </div>
        </div>

        <!-- Full Model Summary Card -->
        <div class="math-topic-card" style="padding:1.25rem;">
          <h4 style="color:#0f172a;font-size:1rem;font-weight:800;margin-bottom:0.65rem;display:flex;align-items:center;gap:0.4rem;">
            <span>📄</span> Comprehensive Lesson Summary
          </h4>
          <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:1rem 1.25rem;line-height:1.8;color:#1e293b;font-size:0.92rem;text-align:justify;">
            ${w.summary || ch.englishSummary || 'Complete textbook summary.'}
          </div>
        </div>
      </div>`;
  } else if (subTab === 'partB') {
    const ta = w.textAnalysis || {};
    return `
      <div>
        <div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:6px;padding:0.75rem 1rem;margin-bottom:1.25rem;font-size:0.88rem;color:#166534;">
          <strong>B. Read the first paragraph of the lesson carefully. Underline the specific words, vivid verbs and modifiers:</strong>
          <div style="font-size:0.82rem;margin-top:0.2rem;color:#15803d;">Analysis of descriptive linguistic devices used in the opening paragraph.</div>
        </div>

        ${ta.paragraphExcerpt ? `
          <div class="math-topic-card" style="margin-bottom:1.25rem;padding:1rem;">
            <div style="font-weight:700;color:#0f172a;margin-bottom:0.4rem;font-size:0.92rem;">Target Paragraph Excerpt:</div>
            <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:0.9rem;font-style:italic;color:#334155;line-height:1.7;">
              "${ta.paragraphExcerpt}"
            </div>
          </div>` : ''}

        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1rem;">
          <div class="math-topic-card" style="padding:1rem;border-top:4px solid #0284c7;">
            <h5 style="color:#0369a1;font-weight:800;margin-bottom:0.6rem;font-size:0.94rem;">1. Specific Words:</h5>
            <div style="display:flex;flex-wrap:wrap;gap:0.4rem;">
              ${(ta.specificWords || []).map(word => `
                <span style="background:#e0f2fe;color:#0369a1;font-weight:700;font-size:0.84rem;padding:0.25rem 0.6rem;border-radius:4px;">${word}</span>
              `).join('')}
            </div>
          </div>

          <div class="math-topic-card" style="padding:1rem;border-top:4px solid #16a34a;">
            <h5 style="color:#15803d;font-weight:800;margin-bottom:0.6rem;font-size:0.94rem;">2. Vivid Verbs:</h5>
            <div style="display:flex;flex-wrap:wrap;gap:0.4rem;">
              ${(ta.vividVerbs || []).map(verb => `
                <span style="background:#dcfce7;color:#15803d;font-weight:700;font-size:0.84rem;padding:0.25rem 0.6rem;border-radius:4px;">${verb}</span>
              `).join('')}
            </div>
          </div>

          <div class="math-topic-card" style="padding:1rem;border-top:4px solid #9333ea;">
            <h5 style="color:#7e22ce;font-weight:800;margin-bottom:0.6rem;font-size:0.94rem;">3. Modifiers (Adjectives &amp; Adverbs):</h5>
            <div style="display:flex;flex-wrap:wrap;gap:0.4rem;">
              ${(ta.modifiers || []).map(mod => `
                <span style="background:#f3e8ff;color:#7e22ce;font-weight:700;font-size:0.84rem;padding:0.25rem 0.6rem;border-radius:4px;">${mod}</span>
              `).join('')}
            </div>
          </div>
        </div>
      </div>`;
  } else {
    const mp = w.modelParagraph || {};
    return `
      <div>
        <div style="background:#eff6ff;border:1px solid #bfdbfe;border-radius:6px;padding:0.75rem 1rem;margin-bottom:1.25rem;font-size:0.88rem;color:#1e40af;">
          <strong>C. Write a simple and unified paragraph of about 50 to 60 words using a clear topic sentence, specific words, vivid verbs and modifiers:</strong>
        </div>

        <div class="math-topic-card" style="padding:1.25rem;border-left:4px solid #2563eb;">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.65rem;flex-wrap:wrap;gap:0.5rem;">
            <h4 style="color:#0f172a;font-size:1.05rem;font-weight:800;margin:0;">
              ${mp.title || 'Model Unified Paragraph'}
            </h4>
            <span style="background:#dbeafe;color:#1e40af;font-weight:800;font-size:0.8rem;padding:0.25rem 0.65rem;border-radius:99px;">
              ${mp.wordCount || 60} Words (Target: 50–60 words)
            </span>
          </div>

          <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:1rem 1.25rem;line-height:1.9;color:#1e293b;font-size:0.95rem;text-align:justify;margin-bottom:1rem;">
            ${mp.text || 'Paragraph text.'}
          </div>

          <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.75rem 1rem;font-size:0.84rem;color:#475569;line-height:1.6;">
            <strong>Structural Features:</strong> Contains a clear topic sentence introducing the virtue, body sentences loaded with vivid verbs and historical specifics, and a concluding synthesis.
          </div>
        </div>
      </div>`;
  }
}
"""

content += "\n\n" + new_functions

with open(r"D:\SpaceBook\SpaceBook Web\js\app.js", "w", encoding="utf-8") as f:
    f.write(content)

print("app.js updated successfully with dedicated English renderers.")
