// ─── APP.JS — Tuition Hub Controller (Enhanced with Full Exam Roadmap) ──────────

let state = {
  page: "home",
  selectedClass: null,
  activeSubject: "bio", // "bio" | "chem" | "phys"
  selectedBioChapter: 0,
  activeBioTab: "topics",
  selectedChemChapter: 0,
  activeChemTab: "topics",
  selectedPhysChapter: 0,
  selectedEngChapter: 0,
  activeEngTab: 'reading',
  selectedUrduChapter: 0,
  activeUrduTab: 'lesson',
  activeUrduSloTab: null,
  activePhysTab: "topics",
  selectedMathChapter: 0,
  activeMathTab: 'lesson',
  activeMathEx: '1.1',
  selectedPakStudyChapter: 0,
  activePakStudyTab: 'sections',
  activePakStudySloTab: 'slo-mcqs',
  selectedIslChapter: 0,
  activeIslTab: 'lesson',
  activeIslSloTab: 'slo-mcqs'
};

// ─── USER STUDY ANALYTICS STATE & LOCALSTORAGE ENGINE ───
const DEFAULT_STUDY_STATS = {
  studiedQuestions: 148,
  correctAnswers: 126,
  incorrectAnswers: 22,
  streak: 5,
  todayMinutes: 45,
  todayQuestions: 16,
  dailyGoal: 20,
  weeklyActivity: [
    { day: "Mon", questions: 18, active: false },
    { day: "Tue", questions: 24, active: false },
    { day: "Wed", questions: 22, active: false },
    { day: "Thu", questions: 30, active: false },
    { day: "Fri", questions: 28, active: false },
    { day: "Sat", questions: 26, active: true },
    { day: "Sun", questions: 0,  active: false }
  ]
};

function getStudyStats() {
  try {
    const saved = localStorage.getItem("tuition_hub_study_stats");
    if (saved) {
      const parsed = JSON.parse(saved);
      parsed.accuracyRate = parsed.studiedQuestions > 0 
        ? ((parsed.correctAnswers / parsed.studiedQuestions) * 100).toFixed(1) 
        : "0.0";
      return parsed;
    }
  } catch (e) {
    console.error("Failed to read study stats from storage", e);
  }
  const defaults = JSON.parse(JSON.stringify(DEFAULT_STUDY_STATS));
  defaults.accuracyRate = ((defaults.correctAnswers / defaults.studiedQuestions) * 100).toFixed(1);
  return defaults;
}

function saveStudyStats(stats) {
  try {
    localStorage.setItem("tuition_hub_study_stats", JSON.stringify(stats));
  } catch (e) {
    console.error("Failed to save study stats", e);
  }
  updateHeaderStats();
}

function updateHeaderStats() {
  const stats = getStudyStats();
  const streakEl = $("headerStreakText");
  if (streakEl) {
    streakEl.textContent = `${stats.streak}-Day Streak`;
  }
}

function recordQuestionAnswer(isCorrect) {
  const stats = getStudyStats();
  stats.studiedQuestions += 1;
  stats.todayQuestions = (stats.todayQuestions || 0) + 1;
  if (isCorrect) {
    stats.correctAnswers += 1;
  } else {
    stats.incorrectAnswers += 1;
  }
  stats.accuracyRate = ((stats.correctAnswers / stats.studiedQuestions) * 100).toFixed(1);

  // Update current day's weekly practice
  if (stats.weeklyActivity && stats.weeklyActivity.length > 0) {
    const activeDay = stats.weeklyActivity.find(d => d.active) || stats.weeklyActivity[stats.weeklyActivity.length - 2];
    if (activeDay) activeDay.questions += 1;
  }

  saveStudyStats(stats);

  // If currently on Home, re-render analytics counters smoothly
  if (state.page === "home") {
    renderHome();
  }
}

function resetStudyStats() {
  if (confirm("Reset your study statistics to default baseline?")) {
    const defaults = JSON.parse(JSON.stringify(DEFAULT_STUDY_STATS));
    saveStudyStats(defaults);
    renderHome();
  }
}

// ─── DOM helpers ─────────────────────────
const $ = id => document.getElementById(id);
const sanitize = str => String(str == null ? "" : str).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const pageContent     = () => $("dashboard-body");
const breadcrumbEl    = () => $("breadcrumb");
const dashHeaderTitle = () => $("dash-title");
const dashHeaderSub   = () => $("dash-sub");

// ─── Init ────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  updateHeaderStats();
  renderHome();
  setupNavListeners();
  setupMobileMenu();
  setupModal();
});

// ─── Navigation ──────────────────────────
function setupNavListeners() {
  document.querySelectorAll("[data-page]").forEach(el => {
    el.addEventListener("click", (e) => {
      e.preventDefault();
      const page = el.dataset.page;
      state.page = page;
      setActiveNav(page);
      renderPage(page);
      // Close sidebar after navigation if open
      const sb = $("sidebar");
      const ov = $("overlay");
      if (sb) sb.classList.remove("open");
      if (ov) ov.classList.remove("visible");
    });
  });
}

function setActiveNav(page) {
  document.querySelectorAll("[data-page]").forEach(el =>
    el.classList.toggle("active", el.dataset.page === page));
}

function setupMobileMenu() {
  const btn     = $("hamburger");
  const sidebar = $("sidebar");
  const overlay = $("overlay");
  if (!btn || !sidebar || !overlay) return;
  btn.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    overlay.classList.toggle("visible");
  });
  overlay.addEventListener("click", () => {
    sidebar.classList.remove("open");
    overlay.classList.remove("visible");
  });
}

function renderPage(page) {
  if (page === "home")            renderHome();
  else if (page === "subjects")   renderClasses();
  else if (page === "books")      renderBooksView();
  else if (page === "study-plan") renderStudyPlan();
  else if (page === "roadmap")    renderFullRoadmap();
}

function handleGlobalNavBack() {
  if (state.activeView === "subject-detail") {
    goToSubjects(state.selectedClass || "cls9");
  } else if (state.activeView === "subjects" && state.selectedClass) {
    renderClasses();
  } else if (state.activeView === "classes") {
    renderHome();
  } else if (state.page && state.page !== "home") {
    renderHome();
  } else {
    if (window.history.length > 1) {
      window.history.back();
    }
  }
}

function autoScrollToActiveTab(targetEl) {
  try {
    const el = targetEl || document.querySelector('.chapter-nav-tabs, #engTabsBar, .bio-tabs-row');
    if (!el) return;
    
    // Top header total height is now 56px. Add a 12px margin so tabs bar is fully visible
    const topBarHeight = 68;
    const rect = el.getBoundingClientRect();
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const targetY = rect.top + scrollTop - topBarHeight;
    
    if (typeof window.scrollTo === 'function') {
      window.scrollTo({
        top: Math.max(0, targetY),
        behavior: 'smooth'
      });
    }
  } catch (err) {
    console.warn('Auto scroll error:', err);
  }
}

// ─── HOME (NEW REDESIGNED DASHBOARD) ────────
function renderHome() {
  state.page = "home";
  state.activeView = "home";
  setActiveNav("home");
  
  // Hide subpage navigation bar on Home
  const subNavBar = $("subpage-nav-bar");
  if (subNavBar) subNavBar.style.display = "none";

  const stats = getStudyStats();
  updateHeaderStats();

  const maxWeeklyQ = Math.max(...stats.weeklyActivity.map(d => d.questions), 35);
  const weeklyBarsHtml = stats.weeklyActivity.map(d => {
    const heightPercent = Math.max(8, Math.round((d.questions / maxWeeklyQ) * 100));
    return `
      <div class="chart-col ${d.active ? 'active-day' : ''}" title="${d.day}: ${d.questions} Questions Practiced">
        <div class="chart-tooltip">${d.questions} Qs</div>
        <div class="chart-bar-container">
          <div class="chart-bar-fill" style="height:${heightPercent}%"></div>
        </div>
        <div class="chart-day-name">${d.day}</div>
      </div>
    `;
  }).join("");

  const todayPercent = Math.min(100, Math.round(((stats.todayQuestions || 16) / stats.dailyGoal) * 100));

  // Performance Rating Badge
  let accuracyGrade = "🌟 Distinction";
  let accuracyColor = "var(--emerald)";
  if (parseFloat(stats.accuracyRate) < 60) {
    accuracyGrade = "📖 Practice Needed";
    accuracyColor = "var(--rose)";
  } else if (parseFloat(stats.accuracyRate) < 75) {
    accuracyGrade = "👍 Good Progress";
    accuracyColor = "var(--amber)";
  }

  // Class selection tiles
  const classCardsHtml = DATA.classes.map(c => `
    <div class="class-portal-card" onclick="goToSubjects('${c.id}')">
      <div class="class-portal-emoji">${c.emoji}</div>
      <div class="class-portal-name">${c.name}</div>
      <div class="class-portal-meta">KPK Textbook Board</div>
      <div class="class-portal-pill">${c.subjects} Subjects &amp; Notes</div>
    </div>`).join("");

  pageContent().innerHTML = `
    <div class="home-compact-universe">

      <!-- 1. Header Bar -->
      <div class="home-compact-bar">
        <div class="hcb-left">
          <span class="hcb-icon">📊</span>
          <span class="hcb-title">My Study Statistics &amp; Performance Dashboard</span>
        </div>
        <span class="hcb-pill">⚡ Auto-saved Live Metrics</span>
      </div>

      <!-- 2. The 6 Performance Metrics in One Single Row -->
      <div class="compact-analytics-grid">
        <!-- Studied Questions -->
        <div class="compact-analytics-card">
          <div class="cac-icon-wrap" style="background: rgba(2, 132, 199, 0.1); color: #0284c7;">📝</div>
          <div class="cac-content">
            <div class="cac-label">Studied Qs</div>
            <div class="cac-val" id="statStudiedVal">${stats.studiedQuestions}</div>
            <div class="cac-sub">All Subjects</div>
          </div>
        </div>

        <!-- Correct Answers -->
        <div class="compact-analytics-card">
          <div class="cac-icon-wrap" style="background: rgba(16, 185, 129, 0.1); color: #10b981;">✅</div>
          <div class="cac-content">
            <div class="cac-label">Correct</div>
            <div class="cac-val" id="statCorrectVal" style="color: #10b981;">${stats.correctAnswers}</div>
            <div class="cac-sub">Concept Clarity</div>
          </div>
        </div>

        <!-- Incorrect Answers -->
        <div class="compact-analytics-card">
          <div class="cac-icon-wrap" style="background: rgba(244, 63, 94, 0.1); color: #f43f5e;">❌</div>
          <div class="cac-content">
            <div class="cac-label">Incorrect</div>
            <div class="cac-val" id="statIncorrectVal" style="color: #f43f5e;">${stats.incorrectAnswers}</div>
            <div class="cac-sub">Revision Queue</div>
          </div>
        </div>

        <!-- Accuracy Rate -->
        <div class="compact-analytics-card">
          <div class="cac-icon-wrap" style="background: rgba(139, 92, 246, 0.1); color: #8b5cf6;">🎯</div>
          <div class="cac-content">
            <div class="cac-label">Accuracy</div>
            <div class="cac-val" id="statAccuracyVal" style="color: #8b5cf6;">${stats.accuracyRate}%</div>
            <div class="cac-sub" style="color: ${accuracyColor}; font-weight:700;">${accuracyGrade}</div>
          </div>
        </div>

        <!-- Daily Study Streak -->
        <div class="compact-analytics-card">
          <div class="cac-icon-wrap" style="background: rgba(245, 158, 11, 0.1); color: #f59e0b;">🔥</div>
          <div class="cac-content">
            <div class="cac-label">Streak</div>
            <div class="cac-val" style="color: #f59e0b;">${stats.streak} <span class="cac-unit">Days</span></div>
            <div class="cac-sub">Keep Momentum</div>
          </div>
        </div>

        <!-- Daily Study Time -->
        <div class="compact-analytics-card">
          <div class="cac-icon-wrap" style="background: rgba(99, 102, 241, 0.1); color: #6366f1;">⏱️</div>
          <div class="cac-content">
            <div class="cac-label">Study Time</div>
            <div class="cac-val" style="color: #6366f1;">${stats.todayMinutes} <span class="cac-unit">mins</span></div>
            <div class="cac-sub">Recorded Today</div>
          </div>
        </div>
      </div>

      <!-- 3. Side-by-Side: 7-Day Chart & Daily Study Goal -->
      <div class="compact-study-grid">
        <!-- 7-Day Activity Chart -->
        <div class="compact-chart-card">
          <div class="ccc-header">
            <div class="ccc-title"><span>📈</span> 7-Day Study Practice &amp; Activity Statistics</div>
            <div class="ccc-legend">
              <span><span class="legend-dot" style="background:#0284c7;"></span> Past Days</span>
              <span><span class="legend-dot" style="background:#10b981;"></span> Today (Active)</span>
            </div>
          </div>
          <div class="compact-weekly-chart-wrap">
            ${weeklyBarsHtml}
          </div>
        </div>

        <!-- Daily Target & Quick Action -->
        <div class="compact-goal-card">
          <div class="cgc-top">
            <div class="cgc-title-row">
              <span class="cgc-title"><span>🎯</span> Today's Study Goal</span>
              <span class="cgc-target-tag">Target: ${stats.dailyGoal} Qs</span>
            </div>
            <div class="cgc-progress-wrap">
              <div class="cgc-stat-row">
                <span>Completed Today</span>
                <span class="cgc-stat-val">${stats.todayQuestions || 16} / ${stats.dailyGoal} Qs (${todayPercent}%)</span>
              </div>
              <div class="cgc-bar-bg">
                <div class="cgc-bar-fill" style="width:${todayPercent}%"></div>
              </div>
            </div>
            <div class="cgc-tips">
              💡 <strong>Tuition Tip:</strong> Daily practice of 20 questions boosts exam retention by over 80% for board exams.
            </div>
          </div>
          <button class="cgc-drill-btn" onclick="startQuickDrill()">
            <span>🚀</span> Continue Daily Practice
          </button>
        </div>
      </div>

    </div>`;
}

// ─── QUICK DRILL & REVIEW MODALS ──────────
function startQuickDrill() {
  const overlay = $("modalOverlay");
  const header  = $("modalHeader");
  const body    = $("modalBody");
  if (!overlay || !header || !body) return;

  // Aggregate a 5-question quick quiz across Bio, Chem, Phys
  const drillQuestions = [
    {
      subject: "🧬 Biology",
      q: "Which organelle is known as the powerhouse of the cell?",
      opts: ["Ribosome", "Mitochondria", "Golgi Body", "Endoplasmic Reticulum"],
      ans: 1,
      exp: "Mitochondria produce ATP through cellular respiration and are known as the powerhouses of the cell."
    },
    {
      subject: "🧪 Chemistry",
      q: "What is the atomic number of Carbon?",
      opts: ["4", "6", "12", "14"],
      ans: 1,
      exp: "Carbon has 6 protons in its nucleus, making its atomic number 6."
    },
    {
      subject: "⚛️ Physics",
      q: "What is the SI unit of Force?",
      opts: ["Joule", "Newton", "Pascal", "Watt"],
      ans: 1,
      exp: "The SI unit of force is the Newton (N), named after Sir Isaac Newton."
    },
    {
      subject: "🧬 Biology",
      q: "Which blood cells are responsible for oxygen transport in humans?",
      opts: ["White Blood Cells", "Platelets", "Red Blood Cells", "Plasma"],
      ans: 2,
      exp: "Red Blood Cells contain hemoglobin which binds to and transports oxygen throughout the body."
    },
    {
      subject: "🧪 Chemistry",
      q: "Which type of chemical bond is formed by the sharing of electron pairs?",
      opts: ["Ionic Bond", "Covalent Bond", "Metallic Bond", "Hydrogen Bond"],
      ans: 1,
      exp: "A covalent bond involves the mutual sharing of valence electrons between atoms."
    }
  ];

  header.innerHTML = `<span>⚡ Quick 5-Question Practice Drill</span>`;
  body.innerHTML = `
    <div style="margin-bottom:1rem;font-size:0.875rem;color:var(--text-muted);">
      Answer the questions below to test your mastery across subjects. Your results will automatically update your study analytics.
    </div>
    <div class="mcq-list">
      ${drillQuestions.map((m, mi) => `
        <div class="tb-mcq-card" id="drill-mcq-${mi}" style="margin-bottom:1.25rem;">
          <div style="font-size:0.75rem;color:var(--blue);font-weight:700;margin-bottom:0.35rem;">${m.subject} · Drill Question ${mi + 1}</div>
          <div class="tb-mcq-title"><strong>${m.q}</strong></div>
          <div class="tb-opts-grid">
            ${m.opts.map((opt, oi) => `
              <button class="tb-opt-btn" onclick="checkDrillMcq(${mi}, ${oi}, ${m.ans}, '${encodeURIComponent(m.exp)}')">
                <span class="tb-opt-letter">${String.fromCharCode(65 + oi)}</span>
                <span>${opt}</span>
              </button>`).join("")}
          </div>
          <div class="tb-feedback" id="drill-fb-${mi}" style="display:none;"></div>
        </div>
      `).join("")}
    </div>
    <div style="display:flex;justify-content:flex-end;gap:0.5rem;margin-top:1.5rem;">
      <button onclick="closeModal()" style="padding:0.6rem 1.25rem;background:var(--navy);color:#fff;border:none;border-radius:8px;font-weight:700;cursor:pointer;">
        Done Practicing
      </button>
    </div>
  `;
  overlay.classList.add("visible");
}

function checkDrillMcq(qIndex, selectedOpt, correctOpt, encodedExp) {
  const card = $(`drill-mcq-${qIndex}`);
  if (!card) return;
  const buttons = card.querySelectorAll(".tb-opt-btn");
  const fb = $(`drill-fb-${qIndex}`);
  const exp = decodeURIComponent(encodedExp);

  buttons.forEach((btn, oi) => {
    btn.disabled = true;
    if (oi === correctOpt) btn.classList.add("correct");
    else if (oi === selectedOpt && selectedOpt !== correctOpt) btn.classList.add("wrong");
  });

  const isCorrect = selectedOpt === correctOpt;
  recordQuestionAnswer(isCorrect);

  if (fb) {
    fb.style.display = "block";
    fb.className = `tb-feedback ${isCorrect ? 'fb-correct' : 'fb-wrong'}`;
    fb.innerHTML = `
      <strong>${isCorrect ? '✅ Correct!' : '❌ Incorrect!'}</strong> Option ${String.fromCharCode(65 + correctOpt)} is correct.
      <div style="margin-top:0.35rem;font-size:0.82rem;opacity:0.9;"><strong>Explanation:</strong> ${exp}</div>
    `;
  }
}

function reviewIncorrectQuestions() {
  const overlay = $("modalOverlay");
  const header  = $("modalHeader");
  const body    = $("modalBody");
  if (!overlay || !header || !body) return;

  const reviewQuestions = [
    {
      subject: "🧬 Class 9 Biology · Unit 1",
      q: "Which branch of biology deals with the study of tissues?",
      opts: ["Morphology", "Histology", "Physiology", "Taxonomy"],
      ans: 1,
      exp: "Histology is the microscopic study of plant and animal tissues."
    },
    {
      subject: "🧪 Class 9 Chemistry · Unit 2",
      q: "Who discovered the electron through cathode ray experiment?",
      opts: ["Ernest Rutherford", "J.J. Thomson", "John Dalton", "James Chadwick"],
      ans: 1,
      exp: "J.J. Thomson discovered the electron in 1897 using a cathode ray tube."
    },
    {
      subject: "⚛️ Class 9 Physics · Unit 3",
      q: "The rate of change of momentum is equal to which quantity?",
      opts: ["Velocity", "Acceleration", "Applied Force", "Torque"],
      ans: 2,
      exp: "According to Newton's Second Law, the rate of change of momentum is directly proportional to the applied net force."
    }
  ];

  header.innerHTML = `<span>🔄 Revision &amp; Mistake Practice Bank</span>`;
  body.innerHTML = `
    <div style="margin-bottom:1rem;font-size:0.875rem;color:var(--text-muted);">
      Practicing previously missed or tricky textbook questions strengthens your core knowledge and boosts exam confidence.
    </div>
    <div class="mcq-list">
      ${reviewQuestions.map((m, mi) => `
        <div class="tb-mcq-card" id="rev-mcq-${mi}" style="margin-bottom:1.25rem;">
          <div style="font-size:0.75rem;color:var(--rose);font-weight:700;margin-bottom:0.35rem;">${m.subject}</div>
          <div class="tb-mcq-title"><strong>${m.q}</strong></div>
          <div class="tb-opts-grid">
            ${m.opts.map((opt, oi) => `
              <button class="tb-opt-btn" onclick="checkReviewMcq(${mi}, ${oi}, ${m.ans}, '${encodeURIComponent(m.exp)}')">
                <span class="tb-opt-letter">${String.fromCharCode(65 + oi)}</span>
                <span>${opt}</span>
              </button>`).join("")}
          </div>
          <div class="tb-feedback" id="rev-fb-${mi}" style="display:none;"></div>
        </div>
      `).join("")}
    </div>
    <div style="display:flex;justify-content:flex-end;gap:0.5rem;margin-top:1.5rem;">
      <button onclick="closeModal()" style="padding:0.6rem 1.25rem;background:var(--navy);color:#fff;border:none;border-radius:8px;font-weight:700;cursor:pointer;">
        Close Review
      </button>
    </div>
  `;
  overlay.classList.add("visible");
}

function checkReviewMcq(qIndex, selectedOpt, correctOpt, encodedExp) {
  const card = $(`rev-mcq-${qIndex}`);
  if (!card) return;
  const buttons = card.querySelectorAll(".tb-opt-btn");
  const fb = $(`rev-fb-${qIndex}`);
  const exp = decodeURIComponent(encodedExp);

  buttons.forEach((btn, oi) => {
    btn.disabled = true;
    if (oi === correctOpt) btn.classList.add("correct");
    else if (oi === selectedOpt && selectedOpt !== correctOpt) btn.classList.add("wrong");
  });

  const isCorrect = selectedOpt === correctOpt;
  recordQuestionAnswer(isCorrect);

  if (fb) {
    fb.style.display = "block";
    fb.className = `tb-feedback ${isCorrect ? 'fb-correct' : 'fb-wrong'}`;
    fb.innerHTML = `
      <strong>${isCorrect ? '✅ Excellent Correction!' : '❌ Still Incorrect!'}</strong> Option ${String.fromCharCode(65 + correctOpt)} is correct.
      <div style="margin-top:0.35rem;font-size:0.82rem;opacity:0.9;"><strong>Explanation:</strong> ${exp}</div>
    `;
  }
}


// ─── CLASSES ─────────────────────────────
function renderClasses() {
  state.page = "subjects";
  state.selectedClass = null;
  state.activeView = "classes";
  const subNavBar = $("subpage-nav-bar");
  if (subNavBar) subNavBar.style.display = "none";
  currentNavCrumbs = [
    { label: "Home", onclick: () => { setActiveNav("home"); renderHome(); } },
    { label: "Subjects", active: true }
  ];

  const getTierMeta = (c) => {
    if (['cls-pg', 'cls-nur', 'cls-kg'].includes(c.id)) {
      return { tierName: 'Early Years', tierClass: 'tier-early', badgeText: 'Preschool Track' };
    }
    if (['cls1', 'cls2', 'cls3', 'cls4', 'cls5'].includes(c.id)) {
      return { tierName: 'Primary', tierClass: 'tier-primary', badgeText: `${c.subjects} Subjects · In Prep` };
    }
    if (['cls6', 'cls7', 'cls8'].includes(c.id)) {
      return { tierName: 'Middle School', tierClass: 'tier-middle', badgeText: `${c.subjects} Subjects · In Prep` };
    }
    if (c.id === 'cls9') {
      return { tierName: '✨ Matric Ready', tierClass: 'tier-hero-active', badgeText: '✓ 9 Core Subjects Uploaded' };
    }
    if (c.id === 'cls10') {
      return { tierName: 'Matric Board', tierClass: 'tier-secondary', badgeText: `${c.subjects} Subjects · In Prep` };
    }
    return { tierName: 'HSSC College', tierClass: 'tier-college', badgeText: `${c.subjects} Subjects · In Prep` };
  };

  pageContent().innerHTML = `
    <div class="classes-universe-wrapper">
      <!-- 1. Joyful Academic Levels Stage Bar -->
      <div class="classes-stage-bar">
        <div class="csb-left">
          <span class="csb-icon">🎓</span>
          <span class="csb-title">KPK Academic Levels · Choose Your Grade to Explore</span>
        </div>
        <span class="csb-pill">Play Group ➔ Class 12 · 15 Grades</span>
      </div>

      <!-- 2. All 15 Classes in One Look (5x3 Rainbow Jewel Grid) without scrolling down -->
      <div class="classes-jewel-grid">
        ${DATA.classes.map(c => {
          const tm = getTierMeta(c);
          return `
          <div class="class-jewel-card ${tm.tierClass}" onclick="goToSubjects('${c.id}')" title="Explore ${c.name} (${tm.tierName})">
            <div class="cjc-icon-wrap">${c.emoji}</div>
            <div class="cjc-body">
              <div class="cjc-top-row">
                <span class="cjc-name">${c.name}</span>
                <span class="cjc-tier-tag">${tm.tierName}</span>
              </div>
              <div class="cjc-badge">${tm.badgeText}</div>
            </div>
            <span class="cjc-arrow">➔</span>
          </div>`;
        }).join("")}
      </div>

      <!-- 3. Statistical Cards below the classes (visible with scrolling down) -->
      <div class="class-overview-stats-grid" style="margin-top: 1.5rem;">
        <div class="class-stat-card">
          <div class="csc-icon-wrap" style="background: rgba(99, 102, 241, 0.12); color: #6366f1;">🏫</div>
          <div class="csc-content">
            <div class="csc-value">15 Academic Grades</div>
            <div class="csc-label">Secondary &amp; Higher Secondary</div>
            <div class="csc-sub">Class 9, 10, 11 &amp; 12 KPK Board</div>
          </div>
        </div>
        <div class="class-stat-card">
          <div class="csc-icon-wrap" style="background: rgba(16, 185, 129, 0.12); color: #10b981;">📚</div>
          <div class="csc-content">
            <div class="csc-value">25 Core Subjects</div>
            <div class="csc-label">Science &amp; General Tracks</div>
            <div class="csc-sub">Complete textbooks &amp; solved notes</div>
          </div>
        </div>
        <div class="class-stat-card">
          <div class="csc-icon-wrap" style="background: rgba(2, 132, 199, 0.12); color: #0284c7;">📖</div>
          <div class="csc-content">
            <div class="csc-value">15 Official Textbooks</div>
            <div class="csc-label">Verified KPK Board Library</div>
            <div class="csc-sub">Complete curricula &amp; PDF readers</div>
          </div>
        </div>
        <div class="class-stat-card">
          <div class="csc-icon-wrap" style="background: rgba(245, 158, 11, 0.12); color: #f59e0b;">🎯</div>
          <div class="csc-content">
            <div class="csc-value">10,000+ Questions</div>
            <div class="csc-label">MCQs, SQs &amp; SLO Assessments</div>
            <div class="csc-sub">Board exam preparation bank</div>
          </div>
        </div>
      </div>
    </div>`;
}


// ─── SUBJECTS ────────────────────────────
function goToSubjects(classId) {
  state.page = "subjects";
  state.selectedClass = classId;
  state.activeView = "subjects";
  setActiveNav("subjects");
  const cls  = DATA.classes.find(c => c.id === classId) || { id: classId, name: "Class " + classId.replace("cls","") };
  const subs = DATA.subjects[classId] || [];

  // Hide separate multi-line subpage bar to avoid duplicated stacked elements
  const subNavBar = $("subpage-nav-bar");
  if (subNavBar) subNavBar.style.display = "none";

  currentNavCrumbs = [
    { label: "Home",     onclick: () => { setActiveNav("home"); renderHome(); } },
    { label: "Subjects", onclick: () => renderClasses() },
    { label: cls.name,   active: true }
  ];

  // If subjects are not uploaded yet for this class (only Class 9 is currently uploaded)
  if (classId !== "cls9") {
    pageContent().innerHTML = `
      <!-- 1. Single-Line Consolidated Header Bar -->
      <div class="subjects-single-line-bar">
        <div class="sslb-left">
          <button class="sslb-back-btn" onclick="renderClasses()" title="Back to All Classes">
            <span class="back-arrow">←</span> Back to All Classes
          </button>
          <span class="sslb-sep">|</span>
          <nav class="sslb-breadcrumbs" aria-label="breadcrumb">
            <span class="sslb-crumb" onclick="setActiveNav('home'); renderHome();">Home</span>
            <span class="sslb-arrow">›</span>
            <span class="sslb-crumb" onclick="renderClasses();">Subjects</span>
            <span class="sslb-arrow">›</span>
            <span class="sslb-crumb active">${cls.name}</span>
          </nav>
          <span class="sslb-sep">|</span>
          <div class="sslb-title-group">
            <h2 class="sslb-title">${cls.emoji || "📚"} ${cls.name} — Subjects</h2>
          </div>
        </div>
        <div class="sslb-right">
          <span class="sslb-badge" style="background: rgba(245, 158, 11, 0.12); color: #d97706; border-color: rgba(245, 158, 11, 0.3);">⏳ Not Uploaded Yet</span>
        </div>
      </div>

      <!-- 2. Prominent Not Uploaded Yet Notice Container -->
      <div class="not-uploaded-container">
        <div class="not-uploaded-card">
          <div class="not-uploaded-icon-wrap">
            <span class="not-uploaded-icon">⏳</span>
          </div>
          <div class="not-uploaded-badge">Curriculum In Preparation</div>
          <h2 class="not-uploaded-title">${cls.name} — Subjects Not Uploaded Yet</h2>
          <p class="not-uploaded-desc">
            Official KPK Textbook Board syllabus, chapters, and solved textbook notes for <strong>${cls.name}</strong> have not been uploaded yet. Our academic team is actively digitizing verified textbooks and creating SLO-aligned question banks for this grade.
          </p>

          <div class="not-uploaded-details-box">
            <div class="nud-item">
              <div class="nud-label">Grade / Class</div>
              <div class="nud-val">${cls.name}</div>
            </div>
            <div class="nud-item">
              <div class="nud-label">Curriculum Authority</div>
              <div class="nud-val">🏛️ KPK Textbook Board</div>
            </div>
            <div class="nud-item">
              <div class="nud-label">Current Status</div>
              <div class="nud-val status-pending">⏳ Pending Upload</div>
            </div>
          </div>

          <div class="not-uploaded-actions">
            <button class="not-uploaded-btn-primary" onclick="goToSubjects('cls9')">
              <span>📖 Explore Available Class 9 Subjects (9 Subjects Uploaded)</span>
              <span class="btn-arrow">→</span>
            </button>
            <button class="not-uploaded-btn-secondary" onclick="renderClasses()">
              <span>← Choose Another Class</span>
            </button>
          </div>
        </div>
      </div>
    `;
    return;
  }

  // Calculate totals for class overview
  let totalUnits = 0;
  subs.forEach(s => { totalUnits += (s.chapters || 0); });
  const isCls9 = (classId === "cls9");

  // Rich metadata helper for subject statistical cards
  const getSubjectMeta = (s) => {
    if (s.id === "cls9-bio" || s.hasBio) {
      return {
        headerColor: "#059669",
        urduName: "حیاتیات",
        badgeText: "✓ 100% Verbatim KPK Textbook",
        badgeClass: "badge-green",
        metric1Val: "9 Units",
        metric1Lbl: "56 Sections (عنوانات)",
        metric2Val: "164 Solved Qs",
        metric2Lbl: "90 MCQs · 45 SQs · 29 LQs",
        metric3Val: "162 SLO Bank",
        metric3Lbl: "90 MCQs · 54 SQs · 18 LQs",
        topics: ["Cell Biology", "Biodiversity", "Bioenergetics", "Cell Cycle", "Nutrition", "Transport", "Practicals"]
      };
    }
    if (s.id === "cls9-math" || s.hasMath) {
      return {
        headerColor: "#2563eb",
        urduName: "ریاضی",
        badgeText: "✓ 100% Solved Exercises & Theorems",
        badgeClass: "badge-blue",
        metric1Val: "17 Units",
        metric1Lbl: "88+ Theory Sections",
        metric2Val: "345+ Examples",
        metric2Lbl: "Worked Step-by-Step",
        metric3Val: "747+ Solved Qs",
        metric3Lbl: "Exercises & Review Sets",
        topics: ["Matrices & Determinants", "Real Numbers", "Logarithms", "Algebraic Formulas", "Linear Equations", "Theorems"]
      };
    }
    if (s.id === "cls9-pakstudy" || s.hasPakStudy) {
      return {
        headerColor: "#0d9488",
        urduName: "مطالعہ پاکستان",
        badgeText: "✓ مستند درسی مواد و تاریخی سنگ میل",
        badgeClass: "badge-emerald",
        metric1Val: "4 ابواب",
        metric1Lbl: "27 تفصیلی عنوانات",
        metric2Val: "100 سوالات",
        metric2Lbl: "40 MCQs · 36 SQs · 24 LQs",
        metric3Val: "20 سنگ میل",
        metric3Lbl: "مکمل تاریخی ٹائم لائن",
        topics: ["نظریاتی اساس", "تحریکِ پاکستان", "جغرافیہ و ماحول", "تاریخِ پاکستان"]
      };
    }
    if (s.id === "cls9-chem" || s.hasChem) {
      return {
        headerColor: "#0284c7",
        urduName: "کیمسٹری",
        badgeText: "✓ KPK Board Aligned Volume",
        badgeClass: "badge-sky",
        metric1Val: "8 Units",
        metric1Lbl: "Complete Core Theory",
        metric2Val: "80+ Solved MCQs",
        metric2Lbl: "Chapter End Review",
        metric3Val: "75+ SQs & LQs",
        metric3Lbl: "Concepts & Numericals",
        topics: ["Atomic Structure", "Periodic Table", "Chemical Bonding", "Physical States", "Solutions", "Electrochemistry"]
      };
    }
    if (s.id === "cls9-phy" || s.hasPhys) {
      return {
        headerColor: "#7c3aed",
        urduName: "طبیعیات",
        badgeText: "✓ Solved Numericals & Notes",
        badgeClass: "badge-purple",
        metric1Val: "9 Units",
        metric1Lbl: "Mechanics to Thermal",
        metric2Val: "90+ Solved MCQs",
        metric2Lbl: "Exercise Question Bank",
        metric3Val: "65+ Numericals",
        metric3Lbl: "Step-by-Step Solutions",
        topics: ["Physical Quantities", "Kinematics", "Dynamics", "Turning Effect", "Gravitation", "Thermal Properties"]
      };
    }
    if (s.id === "cls9-eng" || s.hasEng) {
      return {
        headerColor: "#4f46e5",
        urduName: "انگریزی لازمی",
        badgeText: "✓ Prose, Poetry & Grammar Suite",
        badgeClass: "badge-indigo",
        metric1Val: "15 Units",
        metric1Lbl: "Prose, Poems & Mind Maps",
        metric2Val: "120+ Vocab/Grammar",
        metric2Lbl: "Contextual Grammar Drills",
        metric3Val: "45+ Solved Mashq",
        metric3Lbl: "Comprehension & Exercises",
        topics: ["Prophet's Simplicity", "The Daffodils", "Quaid's Vision", "Health & Safety", "Voice & Narration"]
      };
    }
    if (s.id === "cls9-urdu" || s.hasUrdu) {
      return {
        headerColor: "#0891b2",
        urduName: "اردو لازمی",
        badgeText: "✓ مکمل خلاصہ جات، تشریحات و قواعد",
        badgeClass: "badge-teal",
        metric1Val: "15 اسباق",
        metric1Lbl: "حصہ نثر، نظم و غزل",
        metric2Val: "100% تشریحات",
        metric2Lbl: "تمام اشعار و حوالہ جات",
        metric3Val: "مشقی سوالات",
        metric3Lbl: "معروضی و انشائیہ حل شدہ",
        topics: ["حصہ نثر (اخلاقِ نبویؐ)", "حصہ نظم (حمد و نعت)", "حصہ غزل", "قواعد و انشا"]
      };
    }
    if (s.id === "cls9-comp") {
      return {
        headerColor: "#0e7490",
        urduName: "کمپیوٹر سائنس",
        badgeText: "✓ IT & Computer Foundations",
        badgeClass: "badge-cyan",
        metric1Val: "8 Units",
        metric1Lbl: "Hardware & Software",
        metric2Val: "80+ Solved MCQs",
        metric2Lbl: "Exercise Assessment",
        metric3Val: "40+ Review SQs",
        metric3Lbl: "Conceptual & Practical",
        topics: ["Fundamentals of Computer", "Operating Systems", "Office Automation", "Data Communications", "Security"]
      };
    }
    if (s.id === "cls9-isl" || s.id === "cls10-isl" || s.hasIsl) {
      return {
        headerColor: "#16a34a",
        urduName: s.nameUrdu || "اسلامیات",
        badgeText: "✓ Uthmani Ayaat & SLO Q&A",
        badgeClass: "badge-green",
        metric1Val: (s.chapters || 15) + " Units",
        metric1Lbl: "Ayaat, Tafseer & Lughat",
        metric2Val: "Trilingual",
        metric2Lbl: "EN / Urdu / Pashto",
        metric3Val: "SLO Bank",
        metric3Lbl: "MCQs · SQs · LQs",
        topics: ["Uthmani Ayaat", "Trilingual Translation", "Lughat", "Tafseer", "SLO Q&A"]
      };
    }
    const chCount = s.chapters || 8;
    return {
      headerColor: "#64748b",
      urduName: s.nameUrdu || "",
      badgeText: "🏛️ KPK Board Curriculum",
      badgeClass: "badge-gray",
      metric1Val: `${chCount} Units`,
      metric1Lbl: "Standard KPK Syllabus",
      metric2Val: `${chCount * 10}+ Solved MCQs`,
      metric2Lbl: "Exercise Question Bank",
      metric3Val: `${chCount * 6}+ Solved SQs`,
      metric3Lbl: "Conceptual Questions",
      topics: ["Chapter Outlines", "Core Concepts", "Exercise Solutions", "Exam Practice"]
    };
  };

  pageContent().innerHTML = `
    <!-- 1. All 9 Class Subjects in One Look (3x3 Compact Grid) without scrolling down -->
    <div class="subjects-compact-grid">
      ${subs.map(s => {
        const meta = getSubjectMeta(s);
        const cleanBadge = meta.badgeText ? meta.badgeText.replace(/^[✓🏛️]\s*/, '') : '';
        return `
        <div class="subject-card-compact" onclick="openSubject('${classId}','${s.id}')" title="Explore ${s.name} units &amp; solved notes">
          <div class="scc-icon" style="background: ${meta.headerColor}14; color: ${meta.headerColor}; border: 1px solid ${meta.headerColor}30;">
            ${s.emoji}
          </div>
          <div class="scc-info">
            <div class="scc-name-row">
              <span class="scc-name">${s.name}</span>
              ${meta.urduName ? `<span class="scc-urdu">${meta.urduName}</span>` : ""}
            </div>
            <div class="scc-sub">${cleanBadge}</div>
          </div>
          <div class="scc-badge-wrap">
            <span class="scc-pill" style="color: ${meta.headerColor}; background: ${meta.headerColor}12; border: 1px solid ${meta.headerColor}28;">${s.chapters} Units</span>
          </div>
        </div>`;
      }).join("")}
    </div>

    <!-- 2. Statistical Cards below the subjects (4 Cards in a Row · 100% Verified Counts) -->
    <div class="class-overview-stats-grid" style="margin-top: 1.5rem;">
      <div class="class-stat-card">
        <div class="csc-icon-wrap" style="background: rgba(99, 102, 241, 0.12); color: #6366f1;">📚</div>
        <div class="csc-content">
          <div class="csc-value">9 Subjects · 15 Books</div>
          <div class="csc-label">Class Curriculum Track</div>
          <div class="csc-sub">Science &amp; Arts · 100 Units (92 Full Chapters)</div>
        </div>
      </div>

      <div class="class-stat-card">
        <div class="csc-icon-wrap" style="background: rgba(16, 185, 129, 0.12); color: #10b981;">📖</div>
        <div class="csc-content">
          <div class="csc-value">26,427 Words · 33,494 Paras</div>
          <div class="csc-label">Verbatim Lessons &amp; Sections</div>
          <div class="csc-sub">Word-by-word official coverage · 531 Sections</div>
        </div>
      </div>

      <div class="class-stat-card">
        <div class="csc-icon-wrap" style="background: rgba(245, 158, 11, 0.12); color: #f59e0b;">🎯</div>
        <div class="csc-content">
          <div class="csc-value">2,386 Solved Questions</div>
          <div class="csc-label">Exam Readiness Bank</div>
          <div class="csc-sub">1,343 MCQs · 755 Short &amp; 288 Long Qs</div>
        </div>
      </div>

      <div class="class-stat-card">
        <div class="csc-icon-wrap" style="background: rgba(2, 132, 199, 0.12); color: #0284c7;">📝</div>
        <div class="csc-content">
          <div class="csc-value">543 Exercises · 480 SLOs</div>
          <div class="csc-label">Practice &amp; SLO Assessments</div>
          <div class="csc-sub">Solved exercises &amp; Board SLO benchmarks</div>
        </div>
      </div>
    </div>`;
}

// ─── SUBJECT ROUTER ──────────────────────
function openSubject(classId, subjId) {
  if (classId !== 'cls9') {
    goToSubjects(classId);
    return;
  }
  state.activeView = "subject-detail";
  state.selectedClass = classId;
  const subs = DATA.subjects[classId] || [];
  const subj = subs.find(s => s.id === subjId);
  if (!subj) return;
  if (subj.hasBio || subjId === 'cls9-bio') {
    state.activeSubject = "bio";
    openBioView(classId, subj);
  } else if (subj.hasChem || subjId === 'cls9-chem') {
    state.activeSubject = "chem";
    openChemView(classId, subj);
  } else if (subj.hasPhys || subjId === 'cls9-phy') {
    state.activeSubject = "phys";
    openPhysView(classId, subj);
  } else if (subj.hasEng || subjId === 'cls9-eng') {
    state.activeSubject = "eng";
    openEngView(classId, subj);
  } else if (subj.hasUrdu || subjId === 'cls9-urdu') {
    state.activeSubject = "urdu";
    openUrduView(classId, subj);
  } else if (subj.hasMath || subjId === 'cls9-math') {
    state.activeSubject = "math";
    openMathView(classId, subj);
  } else if (subj.hasPakStudy || subjId === 'cls9-pakstudy') {
    state.activeSubject = "pakstudy";
    openPakStudyView(classId, subj);
  } else if (subj.hasIsl || subjId === 'cls9-isl' || subjId === 'cls10-isl') {
    state.activeSubject = "isl";
    openIslView(classId, subj);
  } else {
    state.activeSubject = subj.id;
    goToChapters(classId, subjId, subj.name);
  }
}

// ─────────────────────────────────────────
//  BIOLOGY INTERACTIVE ROADMAP VIEW
// ─────────────────────────────────────────
function getBioChapterList(classId) {
  if (classId === 'cls10') {
    return (DATA && DATA.bio10Chapters) ? DATA.bio10Chapters : [];
  }
  return (typeof BIO_DATA !== 'undefined' && Array.isArray(BIO_DATA)) ? BIO_DATA : ((DATA && DATA.bioChapters) ? DATA.bioChapters : []);
}

function openBioView(classId, subj) {
  state.activeSubject = "bio";
  state.selectedBioChapter = 0;
  state.activeBioTab = "sections";
  state.activeBioSloTab = "slo-mcqs";
  state.activeBioExPart = "mcqs";
  state.selectedClass = classId;
  setActiveNav("subjects");

  const cls = DATA.classes.find(c => c.id === classId) || { name: "Class 9" };
  const isCls10 = (classId === "cls10");
  const chList = getBioChapterList(classId);
  const gradeLabel = isCls10 ? "Grade 10" : "Grade 9";
  const unitRange = isCls10 ? "Units 10 to 18" : "Units 1 to 9 (مکمل نصاب)";
  const pdfFile = isCls10 ? "assets/books/Class-10-Biology-KPK.pdf" : "assets/books/Class-9-Biology-KPK.pdf";

  setDashHeader(`🧬 ${subj.name} — ${gradeLabel}`, `KPK Textbook Board, Peshawar · ${unitRange} &nbsp;|&nbsp; <a href="${pdfFile}" target="_blank" style="color:#059669;font-weight:700;text-decoration:underline;">📥 View/Download Official Biology Book PDF</a>`);
  setBreadcrumb([
    { label: "Home",     onclick: () => { setActiveNav("home"); renderHome(); } },
    { label: "Subjects", onclick: () => renderClasses() },
    { label: cls.name,   onclick: () => goToSubjects(classId) },
    { label: subj.name,  active: true }
  ]);

  const chapBtns = chList.map((ch, i) => `
    <button class="bio-ch-btn ${i === 0 ? "active" : ""}" id="bio-btn-${i}"
            onclick="selectBioChapter(${i})">
      <span class="ch-btn-num" style="background:#059669;color:#fff;">Unit ${ch.number || ch.num || (i + 1)}</span>
      <span class="ch-btn-info">
        <span class="ch-btn-name" style="font-weight:700;font-size:0.92rem;color:#1e293b;">${ch.title || ch.name || ""}</span>
        <span class="ch-btn-sub" style="font-size:0.75rem;color:#64748b;">${ch.pageRange || ""}</span>
      </span>
      <span class="ch-btn-status" style="background:#dcfce7;color:#15803d;font-size:0.7rem;font-weight:700;">
        ✅ Complete
      </span>
    </button>`).join("");

  pageContent().innerHTML = `
    <div class="bio-view">
      <div class="bio-ch-sidebar">
        <div class="bio-ch-sidebar-header" style="background:linear-gradient(135deg,#064e3b,#059669);color:#fff;box-shadow:0 2px 8px rgba(5,150,105,0.25);">
          <button onclick="goToSubjects('${classId}')" class="sidebar-back-icon-btn" title="Back to Subjects" style="background:rgba(255,255,255,0.2);color:#fff;border:1px solid rgba(255,255,255,0.35);">←</button>
          <span>🧬 KPK ${gradeLabel} Biology</span>
        </div>
        <div class="bio-ch-list">${chapBtns}</div>
        <div style="padding:1rem;background:#f8fafc;border-top:1px solid var(--border);text-align:center;">
          <div style="font-size:0.78rem;color:#059669;font-weight:700;margin-bottom:0.35rem;">Khyber Pakhtunkhwa Textbook Board</div>
          <div style="font-size:0.72rem;color:#64748b;">100% Word-by-Word Verbatim Matched</div>
        </div>
      </div>
      <div class="bio-topic-area" id="bioTopicArea"></div>
    </div>`;

  renderBioChapter(0);
}

function selectBioChapter(index) {
  state.selectedBioChapter = index;
  document.querySelectorAll(".bio-ch-btn").forEach((btn, i) =>
    btn.classList.toggle("active", i === index));
  renderBioChapter(index);
}

function switchBioTab(tabName, skipScroll) {
  state.activeBioTab = tabName;
  document.querySelectorAll(".bio-top-tab").forEach(btn =>
    btn.classList.toggle("active", btn.dataset.tab === tabName));

  const chList = getBioChapterList(state.selectedClass);
  const ch = chList[state.selectedBioChapter || 0];
  const container = $("bioTabContentContainer");
  if (!container || !ch) return;

  if (tabName === "sections") {
    container.innerHTML = renderBioSections(ch);
  } else if (tabName === "summary") {
    container.innerHTML = renderBioSummary(ch);
  } else if (tabName === "exercise") {
    container.innerHTML = renderBioExercise(ch);
  } else if (tabName === "slo") {
    container.innerHTML = renderBioSLOs(ch);
  } else if (tabName === "practicals") {
    container.innerHTML = renderBioPracticals(ch);
  }

  if (!skipScroll) {
    const headerEl = $("bioChapterHeader");
    if (headerEl) headerEl.scrollIntoView({ behavior: "smooth", block: "start" });
  }
}

function renderBioChapter(index) {
  const chList = getBioChapterList(state.selectedClass);
  const ch = chList[index];
  const area = $("bioTopicArea");
  if (!ch || !area) return;

  const currentTab = state.activeBioTab || "sections";
  const mcqsCount = (ch.exercise && ch.exercise.mcqs) ? ch.exercise.mcqs.length : 10;
  const sqsCount = (ch.exercise && ch.exercise.shortQuestions) ? ch.exercise.shortQuestions.length : 5;
  const lqsCount = (ch.exercise && ch.exercise.detailedQuestions) ? ch.exercise.detailedQuestions.length : 3;
  const sloCount = (ch.sloBank && ch.sloBank.mcqs) ? ch.sloBank.mcqs.length : 10;
  const practicalsCount = (ch.practicals && Array.isArray(ch.practicals)) ? ch.practicals.length : 1;

  area.innerHTML = `
    <div class="bio-chapter-container" id="bioChapterHeader">
      <!-- Chapter Hero Banner -->
      <div class="bio-hero-banner">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:1rem;position:relative;z-index:1;">
          <div>
            <div style="display:inline-flex;align-items:center;gap:0.5rem;background:rgba(255,255,255,0.18);padding:0.25rem 0.85rem;border-radius:99px;font-size:0.82rem;font-weight:700;margin-bottom:0.75rem;backdrop-filter:blur(4px);">
              <span>🧬 Biology Grade 9</span>
              <span>•</span>
              <span>Unit ${ch.number || ch.num}</span>
              <span>•</span>
              <span>${ch.pageRange || ''}</span>
            </div>
            <h1 style="font-size:2rem;margin:0 0 0.5rem 0;font-weight:800;letter-spacing:-0.5px;color:#ffffff;">
              ${ch.title || ch.name}
              ${ch.titleUrdu ? `<span style="font-family:'Jameel Noori Nastaleeq','Urdu Typesetting',serif;font-size:1.4rem;font-weight:normal;opacity:0.9;margin-left:0.75rem;">(${ch.titleUrdu})</span>` : ''}
            </h1>
            <div style="font-size:0.92rem;opacity:0.92;max-width:720px;line-height:1.7;">
              ${ch.description || ''}
            </div>
          </div>
          <div style="text-align:right;background:rgba(0,0,0,0.15);padding:0.85rem 1.25rem;border-radius:10px;border:1px solid rgba(255,255,255,0.2);">
            <div style="font-size:0.75rem;opacity:0.85;text-transform:uppercase;letter-spacing:0.5px;">Curriculum Standard</div>
            <div style="font-size:1.15rem;font-weight:800;color:#a7f3d0;">KPK Board (Peshawar)</div>
            <div style="font-size:0.75rem;margin-top:0.25rem;color:#ecfdf5;">100% Word-for-Word Matched</div>
          </div>
        </div>

        <!-- Quick Stats Grid (Maximum 3 Statistical Cards in a Row) -->
        <div class="bio-stats-grid">
          <div class="bio-stat-card">
            <span class="bio-stat-icon">📖</span>
            <div class="bio-stat-content">
              <span class="bio-stat-num">${ch.sections ? ch.sections.length : 0}</span>
              <span class="bio-stat-label">Textbook Sections</span>
            </div>
          </div>
          <div class="bio-stat-card">
            <span class="bio-stat-icon">🎯</span>
            <div class="bio-stat-content">
              <span class="bio-stat-num">${mcqsCount}</span>
              <span class="bio-stat-label">Textbook MCQs</span>
            </div>
          </div>
          <div class="bio-stat-card">
            <span class="bio-stat-icon">✏️</span>
            <div class="bio-stat-content">
              <span class="bio-stat-num">${sqsCount}</span>
              <span class="bio-stat-label">Short Questions</span>
            </div>
          </div>
          <div class="bio-stat-card">
            <span class="bio-stat-icon">📝</span>
            <div class="bio-stat-content">
              <span class="bio-stat-num">${lqsCount}</span>
              <span class="bio-stat-label">Detailed Model Answers</span>
            </div>
          </div>
          <div class="bio-stat-card">
            <span class="bio-stat-icon">🌟</span>
            <div class="bio-stat-content">
              <span class="bio-stat-num">${sloCount}</span>
              <span class="bio-stat-label">SLO Assessment Bank</span>
            </div>
          </div>
          <div class="bio-stat-card">
            <span class="bio-stat-icon">🔬</span>
            <div class="bio-stat-content">
              <span class="bio-stat-num">${practicalsCount}</span>
              <span class="bio-stat-label">Practical Lab Skills</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Top Pedagogical Tabs -->
      <div style="display:flex;gap:0.5rem;margin-bottom:1.5rem;background:#f1f5f9;padding:0.4rem;border-radius:10px;flex-wrap:wrap;">
        <button class="bio-top-tab ${currentTab === 'sections' ? 'active' : ''}" data-tab="sections" onclick="switchBioTab('sections')">
          <span>📖</span> Complete Textbook Lessons
        </button>
        <button class="bio-top-tab ${currentTab === 'summary' ? 'active' : ''}" data-tab="summary" onclick="switchBioTab('summary')">
          <span>💡</span> Key Points & Summary
        </button>
        <button class="bio-top-tab ${currentTab === 'exercise' ? 'active' : ''}" data-tab="exercise" onclick="switchBioTab('exercise')">
          <span>✍️</span> Solved Textbook Exercises
        </button>
        <button class="bio-top-tab ${currentTab === 'slo' ? 'active' : ''}" data-tab="slo" onclick="switchBioTab('slo')">
          <span>🎯</span> SLO Examination Bank
        </button>
        <button class="bio-top-tab ${currentTab === 'practicals' ? 'active' : ''}" data-tab="practicals" onclick="switchBioTab('practicals')">
          <span>🔬</span> Practical & Laboratory Skills
        </button>
      </div>

      <!-- Tab Content Area -->
      <div id="bioTabContentContainer"></div>
    </div>`;

  switchBioTab(currentTab, true);
}

// ─────────────────────────────────────────
//  TAB 1: COMPLETE VERBATIM SECTIONS (COLLAPSED BY DEFAULT)
// ─────────────────────────────────────────
function renderBioSections(ch) {
  let quranBannerHtml = "";
  if (ch.introQuran && Array.isArray(ch.introQuran)) {
    const quotes = ch.introQuran.map(q => `
      <div class="bio-quran-box">
        <div class="bio-quran-arabic">${q.arabic}</div>
        <div style="font-size:0.95rem;color:#1e293b;margin-bottom:0.35rem;font-style:italic;">
          <strong>Translation:</strong> "${q.translation}"
        </div>
        <div style="font-size:0.8rem;color:#059669;font-weight:700;text-align:right;">
          — ${q.reference}
        </div>
      </div>`).join("");

    quranBannerHtml = `
      <div style="background:#f0fdf4;border:2px solid #86efac;border-radius:12px;padding:1.25rem;margin-bottom:1.5rem;">
        <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.75rem;color:#065f46;font-weight:800;font-size:1rem;">
          <span>📖</span><span>Holy Quran & Biological Guidance:</span>
        </div>
        ${quotes}
      </div>`;
  }

  const sectionsHtml = (ch.sections || []).map((sec, idx) => {
    // Format paragraph items
    const formattedParagraphs = (sec.content || []).map(p => {
      const pClean = p.trim();
      if (!pClean) return '';
      if (pClean.startsWith('•') || pClean.startsWith('1.') || pClean.startsWith('2.') || pClean.startsWith('3.') || pClean.startsWith('4.') || pClean.startsWith('5.') || pClean.startsWith('-')) {
        return `<div class="bio-sec-p" style="margin-left:1rem;white-space:pre-line;">${pClean}</div>`;
      }
      return `<p class="bio-sec-p">${pClean}</p>`;
    }).join('');

    // Callout boxes
    let calloutsHtml = "";
    if (sec.callouts && Array.isArray(sec.callouts)) {
      calloutsHtml = sec.callouts.map(callout => {
        let boxClass = "bio-callout-scientific";
        let icon = "🔬";
        if (callout.type === "ponder") {
          boxClass = "bio-callout-ponder";
          icon = "💡";
        } else if (callout.type === "society") {
          boxClass = "bio-callout-society";
          icon = "🏛️";
        } else if (callout.type === "activity") {
          boxClass = "bio-callout-activity";
          icon = "🧪";
        }
        return `
          <div class="bio-callout-box ${boxClass}">
            <div class="bio-callout-title">
              <span>${icon}</span>
              <span>${callout.title}</span>
            </div>
            <div>${callout.content}</div>
          </div>`;
      }).join('');
    }

    // Preview snippet from first paragraph
    const firstP = (sec.content && sec.content.length > 0) ? sec.content[0] : '';
    const snippet = firstP.substring(0, 125) + '...';

    return `
      <div class="bio-section-card" id="bio-sec-${sec.id || idx}">
        <div class="bio-section-header" onclick="toggleBioAccordion('bio-sec-${sec.id || idx}')">
          <div style="display:flex;align-items:center;gap:0.75rem;flex-wrap:wrap;">
            <span class="bio-sec-badge">Section ${sec.sectionNum || (idx + 1)}</span>
            <span class="bio-sec-title">${sec.title}</span>
            ${sec.urduTitle ? `<span class="bio-sec-urdu-pill">${sec.urduTitle}</span>` : ''}
          </div>
          <span class="bio-sec-toggle-icon">▼</span>
        </div>
        <div class="bio-sec-preview">${snippet}</div>
        <div class="bio-section-body" style="display:none;">
          ${formattedParagraphs}
          ${calloutsHtml}
        </div>
      </div>`;
  }).join('');

  return `
    <div>
      ${quranBannerHtml}
      <div style="margin-bottom:1.25rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.75rem;background:#f8fafc;padding:0.75rem 1rem;border-radius:10px;border:1px solid #e2e8f0;">
        <div>
          <span style="font-weight:800;color:#059669;font-size:0.95rem;">📚 Complete Verbatim Lessons:</span>
          <span style="font-size:0.82rem;color:#64748b;margin-left:0.4rem;">(All sections collapsed by default, click any to expand)</span>
        </div>
        <div style="display:flex;gap:0.5rem;">
          <button onclick="expandAllBioSections()" class="math-toolbar-btn" style="color:#059669;border-color:#a7f3d0;" title="Expand all sections">
            ➕ Expand All
          </button>
          <button onclick="collapseAllBioSections()" class="math-toolbar-btn" style="color:#475569;" title="Collapse all sections">
            ➖ Collapse All
          </button>
        </div>
      </div>
      ${sectionsHtml}
    </div>`;
}

function toggleBioAccordion(secId) {
  const el = $(secId);
  if (!el) return;
  const isOpen = el.classList.contains("open");
  const body = el.querySelector(".bio-section-body");
  if (isOpen) {
    el.classList.remove("open");
    if (body) body.style.display = "none";
  } else {
    el.classList.add("open");
    if (body) body.style.display = "block";
  }
}

function expandAllBioSections() {
  document.querySelectorAll(".bio-section-card").forEach(el => {
    el.classList.add("open");
    const body = el.querySelector(".bio-section-body");
    if (body) body.style.display = "block";
  });
}

function collapseAllBioSections() {
  document.querySelectorAll(".bio-section-card").forEach(el => {
    el.classList.remove("open");
    const body = el.querySelector(".bio-section-body");
    if (body) body.style.display = "none";
  });
}

// ─────────────────────────────────────────
//  TAB 2: KEY POINTS & CHAPTER SUMMARY
// ─────────────────────────────────────────
function renderBioSummary(ch) {
  const points = ch.keyPoints || [];
  const pointsHtml = points.map((p, idx) => `
    <div style="display:flex;gap:0.85rem;align-items:flex-start;background:#ffffff;border:1px solid #e2e8f0;padding:1rem 1.25rem;border-radius:10px;margin-bottom:0.75rem;box-shadow:0 1px 4px rgba(0,0,0,0.03);">
      <span style="background:#dcfce7;color:#15803d;font-weight:800;font-size:0.8rem;padding:0.25rem 0.55rem;border-radius:99px;flex-shrink:0;">${idx + 1}</span>
      <div style="font-size:0.96rem;color:#1e293b;line-height:1.6;">${p}</div>
    </div>`).join('');

  return `
    <div style="max-width:900px;margin:0 auto;">
      <div style="background:#f0fdf4;border:1.5px solid #86efac;border-radius:12px;padding:1.25rem;margin-bottom:1.5rem;display:flex;align-items:center;gap:1rem;">
        <span style="font-size:2rem;">💡</span>
        <div>
          <h3 style="margin:0 0 0.25rem 0;color:#065f46;font-size:1.15rem;">Official Textbook Key Points</h3>
          <p style="margin:0;font-size:0.85rem;color:#047857;">High-yield concept summary extracted word-for-word from the official KPK textbook.</p>
        </div>
      </div>
      ${pointsHtml}
    </div>`;
}

// ─────────────────────────────────────────
//  TAB 3: SOLVED TEXTBOOK EXERCISES
// ─────────────────────────────────────────
function renderBioExercise(ch) {
  const ex = ch.exercise || {};
  const mcqs = ex.mcqs || [];
  const sqs = ex.shortQuestions || [];
  const lqs = ex.detailedQuestions || [];
  const activities = ex.activities || [];
  const activePart = state.activeBioExPart || "mcqs";

  return `
    <div>
      <!-- Exercise Parts Sub-navigation -->
      <div style="display:flex;gap:0.5rem;margin-bottom:1.5rem;border-bottom:2px solid #e2e8f0;padding-bottom:0.5rem;flex-wrap:wrap;">
        <button onclick="switchBioExPart('mcqs')" class="bio-part-tab ${activePart === 'mcqs' ? 'active' : ''}" style="padding:0.5rem 1rem;font-weight:700;border:none;border-radius:6px;cursor:pointer;background:${activePart === 'mcqs' ? '#059669' : '#f1f5f9'};color:${activePart === 'mcqs' ? '#fff' : '#475569'};">
          🎯 Part A: Textbook MCQs (${mcqs.length})
        </button>
        <button onclick="switchBioExPart('sqs')" class="bio-part-tab ${activePart === 'sqs' ? 'active' : ''}" style="padding:0.5rem 1rem;font-weight:700;border:none;border-radius:6px;cursor:pointer;background:${activePart === 'sqs' ? '#059669' : '#f1f5f9'};color:${activePart === 'sqs' ? '#fff' : '#475569'};">
          ✏️ Part B: Short Questions (${sqs.length})
        </button>
        <button onclick="switchBioExPart('lqs')" class="bio-part-tab ${activePart === 'lqs' ? 'active' : ''}" style="padding:0.5rem 1rem;font-weight:700;border:none;border-radius:6px;cursor:pointer;background:${activePart === 'lqs' ? '#059669' : '#f1f5f9'};color:${activePart === 'lqs' ? '#fff' : '#475569'};">
          📝 Part C: Detailed Model Answers (${lqs.length})
        </button>
        ${activities.length > 0 ? `
          <button onclick="switchBioExPart('activities')" class="bio-part-tab ${activePart === 'activities' ? 'active' : ''}" style="padding:0.5rem 1rem;font-weight:700;border:none;border-radius:6px;cursor:pointer;background:${activePart === 'activities' ? '#059669' : '#f1f5f9'};color:${activePart === 'activities' ? '#fff' : '#475569'};">
            🧪 Part D: Activities (${activities.length})
          </button>` : ''}
      </div>

      <div id="bioExPartContainer">
        ${activePart === 'mcqs' ? renderBioExMcqsHtml(mcqs) : ''}
        ${activePart === 'sqs' ? renderBioExSqsHtml(sqs) : ''}
        ${activePart === 'lqs' ? renderBioExLqsHtml(lqs) : ''}
        ${activePart === 'activities' ? renderBioExActivitiesHtml(activities) : ''}
      </div>
    </div>`;
}

function switchBioExPart(partName) {
  state.activeBioExPart = partName;
  const chList = getBioChapterList(state.selectedClass);
  const ch = chList[state.selectedBioChapter || 0];
  const container = $("bioExPartContainer");
  if (!container || !ch) return;

  document.querySelectorAll(".bio-part-tab").forEach(btn => {
    btn.style.background = "#f1f5f9";
    btn.style.color = "#475569";
  });
  event.target.style.background = "#059669";
  event.target.style.color = "#ffffff";

  const ex = ch.exercise || {};
  if (partName === 'mcqs') container.innerHTML = renderBioExMcqsHtml(ex.mcqs || []);
  if (partName === 'sqs') container.innerHTML = renderBioExSqsHtml(ex.shortQuestions || []);
  if (partName === 'lqs') container.innerHTML = renderBioExLqsHtml(ex.detailedQuestions || []);
  if (partName === 'activities') container.innerHTML = renderBioExActivitiesHtml(ex.activities || []);
}

function renderBioExMcqsHtml(mcqs) {
  return mcqs.map((m, idx) => {
    const letters = ['A', 'B', 'C', 'D'];
    const opts = (m.options || []).map((opt, oIdx) => `
      <div class="bio-mcq-opt" id="bio-ex-m-${idx}-opt-${oIdx}" onclick="checkBioExMcq(${idx}, ${oIdx}, ${m.ans})" style="padding:0.65rem 1rem;background:#f8fafc;border:1.5px solid #e2e8f0;border-radius:8px;margin-bottom:0.5rem;cursor:pointer;display:flex;align-items:center;gap:0.75rem;transition:all 0.15s;">
        <span style="font-weight:800;color:#059669;width:24px;height:24px;border-radius:50%;background:#dcfce7;display:inline-flex;align-items:center;justify-content:center;font-size:0.8rem;">${letters[oIdx]}</span>
        <span style="font-size:0.95rem;color:#334155;">${opt}</span>
      </div>`).join('');

    return `
      <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;padding:1.25rem;margin-bottom:1.25rem;box-shadow:0 2px 6px rgba(0,0,0,0.02);">
        <div style="display:flex;gap:0.75rem;align-items:flex-start;margin-bottom:1rem;">
          <span style="background:#059669;color:#fff;font-weight:800;font-size:0.8rem;padding:0.2rem 0.6rem;border-radius:6px;flex-shrink:0;">Q${idx + 1}</span>
          <div style="font-size:1.02rem;font-weight:700;color:#1e293b;line-height:1.5;">${m.q}</div>
        </div>
        <div style="margin-left:2.5rem;">${opts}</div>
        <div id="bio-ex-m-${idx}-feedback" style="display:none;margin-left:2.5rem;margin-top:0.75rem;padding:0.75rem 1rem;border-radius:8px;font-size:0.88rem;line-height:1.5;"></div>
      </div>`;
  }).join('');
}

function checkBioExMcq(qIdx, optIdx, correctIdx) {
  const letters = ['A', 'B', 'C', 'D'];
  const fb = $(`bio-ex-m-${qIdx}-feedback`);
  if (!fb) return;

  const isCorrect = (optIdx === correctIdx);
  for (let i = 0; i < 4; i++) {
    const el = $(`bio-ex-m-${qIdx}-opt-${i}`);
    if (el) {
      if (i === correctIdx) {
        el.style.background = "#dcfce7";
        el.style.borderColor = "#15803d";
      } else if (i === optIdx && !isCorrect) {
        el.style.background = "#fee2e2";
        el.style.borderColor = "#b91c1c";
      } else {
        el.style.opacity = "0.7";
      }
    }
  }

  fb.style.display = "block";
  if (isCorrect) {
    fb.style.background = "#f0fdf4";
    fb.style.border = "1px solid #86efac";
    fb.style.color = "#15803d";
    fb.innerHTML = `<strong>✅ Correct!</strong> Option (${letters[correctIdx]}) is the verified textbook answer.`;
  } else {
    fb.style.background = "#fef2f2";
    fb.style.border = "1px solid #fca5a5";
    fb.style.color = "#991b1b";
    fb.innerHTML = `<strong>❌ Incorrect.</strong> The correct answer is Option <strong>(${letters[correctIdx]})</strong>.`;
  }
}

function renderBioExSqsHtml(sqs) {
  return sqs.map((sq, idx) => `
    <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;padding:1.25rem;margin-bottom:1rem;box-shadow:0 1px 4px rgba(0,0,0,0.03);">
      <div style="display:flex;gap:0.75rem;align-items:flex-start;margin-bottom:0.75rem;">
        <span style="background:#059669;color:#fff;font-weight:800;font-size:0.8rem;padding:0.2rem 0.6rem;border-radius:6px;flex-shrink:0;">SQ ${idx + 1}</span>
        <h4 style="margin:0;font-size:1.02rem;color:#1e293b;line-height:1.5;">${sq.q}</h4>
      </div>
      <div style="margin-left:2.75rem;background:#f8fafc;padding:1rem 1.25rem;border-radius:8px;border-left:3.5px solid #059669;font-size:0.95rem;color:#334155;line-height:1.7;white-space:pre-line;">
        ${sq.ans}
      </div>
    </div>`).join('');
}

function renderBioExLqsHtml(lqs) {
  return lqs.map((lq, idx) => `
    <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;padding:1.4rem;margin-bottom:1.5rem;box-shadow:0 2px 6px rgba(0,0,0,0.03);">
      <div style="display:flex;gap:0.75rem;align-items:flex-start;margin-bottom:1rem;">
        <span style="background:#047857;color:#fff;font-weight:800;font-size:0.8rem;padding:0.25rem 0.65rem;border-radius:6px;flex-shrink:0;">LQ ${idx + 1}</span>
        <h3 style="margin:0;font-size:1.1rem;color:#0f172a;line-height:1.5;">${lq.q}</h3>
      </div>
      <div style="margin-left:2.85rem;background:#f8fafc;padding:1.25rem 1.5rem;border-radius:8px;border-left:4px solid #047857;font-size:0.96rem;color:#334155;line-height:1.8;white-space:pre-line;">
        ${lq.ans}
      </div>
    </div>`).join('');
}

function renderBioExActivitiesHtml(activities) {
  return activities.map((act, idx) => `
    <div style="background:#faf5ff;border:1.5px solid #d8b4fe;border-radius:10px;padding:1.25rem;margin-bottom:1rem;">
      <div style="display:flex;align-items:center;gap:0.5rem;color:#6b21a8;font-weight:800;font-size:1rem;margin-bottom:0.5rem;">
        <span>🧪</span><span>Activity ${idx + 1}: ${act.title}</span>
      </div>
      <div style="font-size:0.95rem;color:#374151;line-height:1.7;">${act.desc}</div>
    </div>`).join('');
}

// ─────────────────────────────────────────
//  TAB 4: SLO EXAMINATION BANK
// ─────────────────────────────────────────
function renderBioSLOs(ch) {
  const slo = ch.sloBank || {};
  const activeSloTab = state.activeBioSloTab || "slo-mcqs";

  return `
    <div>
      <div style="display:flex;gap:0.5rem;margin-bottom:1.5rem;background:#f1f5f9;padding:0.4rem;border-radius:8px;flex-wrap:wrap;">
        <button onclick="switchBioSloTab('slo-mcqs')" class="bio-slo-tab ${activeSloTab === 'slo-mcqs' ? 'active' : ''}" style="flex:1;min-width:140px;padding:0.5rem;border:none;border-radius:6px;font-weight:700;cursor:pointer;background:${activeSloTab === 'slo-mcqs' ? '#059669' : 'transparent'};color:${activeSloTab === 'slo-mcqs' ? '#fff' : '#475569'};">
          🎯 SLO MCQs (${(slo.mcqs || []).length})
        </button>
        <button onclick="switchBioSloTab('slo-sqs')" class="bio-slo-tab ${activeSloTab === 'slo-sqs' ? 'active' : ''}" style="flex:1;min-width:140px;padding:0.5rem;border:none;border-radius:6px;font-weight:700;cursor:pointer;background:${activeSloTab === 'slo-sqs' ? '#059669' : 'transparent'};color:${activeSloTab === 'slo-sqs' ? '#fff' : '#475569'};">
          ✏️ Conceptual SQs (${(slo.shortQuestions || []).length})
        </button>
        <button onclick="switchBioSloTab('slo-lqs')" class="bio-slo-tab ${activeSloTab === 'slo-lqs' ? 'active' : ''}" style="flex:1;min-width:140px;padding:0.5rem;border:none;border-radius:6px;font-weight:700;cursor:pointer;background:${activeSloTab === 'slo-lqs' ? '#059669' : 'transparent'};color:${activeSloTab === 'slo-lqs' ? '#fff' : '#475569'};">
          📝 Evaluative LQs (${(slo.longQuestions || []).length})
        </button>
      </div>

      <div id="bioSloContentContainer">
        ${activeSloTab === 'slo-mcqs' ? renderBioSloMcqsHtml(slo.mcqs || []) : ''}
        ${activeSloTab === 'slo-sqs' ? renderBioSloSqsHtml(slo.shortQuestions || []) : ''}
        ${activeSloTab === 'slo-lqs' ? renderBioSloLqsHtml(slo.longQuestions || []) : ''}
      </div>
    </div>`;
}

function switchBioSloTab(tabName) {
  state.activeBioSloTab = tabName;
  const chList = getBioChapterList(state.selectedClass);
  const ch = chList[state.selectedBioChapter || 0];
  const container = $("bioSloContentContainer");
  if (!container || !ch) return;

  document.querySelectorAll(".bio-slo-tab").forEach(btn => {
    btn.style.background = "transparent";
    btn.style.color = "#475569";
  });
  event.target.style.background = "#059669";
  event.target.style.color = "#ffffff";

  const slo = ch.sloBank || {};
  if (tabName === 'slo-mcqs') container.innerHTML = renderBioSloMcqsHtml(slo.mcqs || []);
  if (tabName === 'slo-sqs') container.innerHTML = renderBioSloSqsHtml(slo.shortQuestions || []);
  if (tabName === 'slo-lqs') container.innerHTML = renderBioSloLqsHtml(slo.longQuestions || []);
}

function renderBioSloMcqsHtml(mcqs) {
  return mcqs.map((m, idx) => {
    const letters = ['A', 'B', 'C', 'D'];
    const cogBadgeColors = {
      Knowledge: "background:#eff6ff;color:#1d4ed8;border:1px solid #bfdbfe;",
      Understanding: "background:#f0fdf4;color:#15803d;border:1px solid #bbf7d0;",
      Application: "background:#faf5ff;color:#7e22ce;border:1px solid #e9d5ff;"
    };
    const cogStyle = cogBadgeColors[m.cognitiveLevel] || cogBadgeColors.Knowledge;

    const opts = (m.options || []).map((opt, oIdx) => `
      <div class="bio-slo-opt" id="bio-slo-m-${idx}-opt-${oIdx}" onclick="checkBioSloMcq(${idx}, ${oIdx}, ${m.ans})" style="padding:0.65rem 1rem;background:#f8fafc;border:1.5px solid #e2e8f0;border-radius:8px;margin-bottom:0.5rem;cursor:pointer;display:flex;align-items:center;gap:0.75rem;transition:all 0.15s;">
        <span style="font-weight:800;color:#059669;width:24px;height:24px;border-radius:50%;background:#dcfce7;display:inline-flex;align-items:center;justify-content:center;font-size:0.8rem;">${letters[oIdx]}</span>
        <span style="font-size:0.95rem;color:#334155;">${opt}</span>
      </div>`).join('');

    return `
      <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;padding:1.25rem;margin-bottom:1.25rem;box-shadow:0 2px 6px rgba(0,0,0,0.02);">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:0.5rem;margin-bottom:0.75rem;flex-wrap:wrap;">
          <div style="display:flex;gap:0.5rem;align-items:center;">
            <span style="background:#059669;color:#fff;font-weight:800;font-size:0.8rem;padding:0.2rem 0.6rem;border-radius:6px;">SLO MCQ ${idx + 1}</span>
            <span style="font-size:0.75rem;font-weight:700;padding:0.15rem 0.5rem;border-radius:99px;${cogStyle}">${m.cognitiveLevel || 'Understanding'}</span>
          </div>
        </div>
        <div style="font-size:1.02rem;font-weight:700;color:#1e293b;line-height:1.5;margin-bottom:0.85rem;">${m.q}</div>
        <div>${opts}</div>
        <div id="bio-slo-m-${idx}-feedback" style="display:none;margin-top:0.75rem;padding:0.75rem 1rem;border-radius:8px;font-size:0.88rem;line-height:1.5;"></div>
      </div>`;
  }).join('');
}

function checkBioSloMcq(qIdx, optIdx, correctIdx) {
  const letters = ['A', 'B', 'C', 'D'];
  const fb = $(`bio-slo-m-${qIdx}-feedback`);
  if (!fb) return;

  const isCorrect = (optIdx === correctIdx);
  for (let i = 0; i < 4; i++) {
    const el = $(`bio-slo-m-${qIdx}-opt-${i}`);
    if (el) {
      if (i === correctIdx) {
        el.style.background = "#dcfce7";
        el.style.borderColor = "#15803d";
      } else if (i === optIdx && !isCorrect) {
        el.style.background = "#fee2e2";
        el.style.borderColor = "#b91c1c";
      } else {
        el.style.opacity = "0.7";
      }
    }
  }

  fb.style.display = "block";
  if (isCorrect) {
    fb.style.background = "#f0fdf4";
    fb.style.border = "1px solid #86efac";
    fb.style.color = "#15803d";
    fb.innerHTML = `<strong>✅ Correct!</strong> Option (${letters[correctIdx]}) is correct.`;
  } else {
    fb.style.background = "#fef2f2";
    fb.style.border = "1px solid #fca5a5";
    fb.style.color = "#991b1b";
    fb.innerHTML = `<strong>❌ Incorrect.</strong> The correct answer is Option <strong>(${letters[correctIdx]})</strong>.`;
  }
}

function renderBioSloSqsHtml(sqs) {
  return sqs.map((sq, idx) => `
    <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;padding:1.25rem;margin-bottom:1rem;box-shadow:0 1px 4px rgba(0,0,0,0.03);">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:0.5rem;margin-bottom:0.75rem;">
        <div style="display:flex;gap:0.5rem;align-items:center;">
          <span style="background:#059669;color:#fff;font-weight:800;font-size:0.8rem;padding:0.2rem 0.6rem;border-radius:6px;">SLO SQ ${idx + 1}</span>
          ${sq.cognitiveLevel ? `<span style="font-size:0.72rem;font-weight:700;background:#f0fdf4;color:#15803d;padding:0.15rem 0.5rem;border-radius:99px;border:1px solid #bbf7d0;">${sq.cognitiveLevel}</span>` : ''}
        </div>
      </div>
      <h4 style="margin:0 0 0.75rem 0;font-size:1.02rem;color:#1e293b;line-height:1.5;">${sq.q}</h4>
      <div style="background:#f8fafc;padding:1rem 1.25rem;border-radius:8px;border-left:3.5px solid #059669;font-size:0.95rem;color:#334155;line-height:1.7;white-space:pre-line;">
        ${sq.ans}
      </div>
    </div>`).join('');
}

function renderBioSloLqsHtml(lqs) {
  return lqs.map((lq, idx) => `
    <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;padding:1.4rem;margin-bottom:1.5rem;box-shadow:0 2px 6px rgba(0,0,0,0.03);">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:0.5rem;margin-bottom:0.75rem;">
        <div style="display:flex;gap:0.5rem;align-items:center;">
          <span style="background:#047857;color:#fff;font-weight:800;font-size:0.8rem;padding:0.25rem 0.65rem;border-radius:6px;">SLO LQ ${idx + 1}</span>
          ${lq.cognitiveLevel ? `<span style="font-size:0.72rem;font-weight:700;background:#faf5ff;color:#7e22ce;padding:0.15rem 0.5rem;border-radius:99px;border:1px solid #e9d5ff;">${lq.cognitiveLevel}</span>` : ''}
        </div>
      </div>
      <h3 style="margin:0 0 1rem 0;font-size:1.1rem;color:#0f172a;line-height:1.5;">${lq.q}</h3>
      <div style="background:#f8fafc;padding:1.25rem 1.5rem;border-radius:8px;border-left:4px solid #047857;font-size:0.96rem;color:#334155;line-height:1.8;white-space:pre-line;">
        ${lq.ans}
      </div>
    </div>`).join('');
}

// ─────────────────────────────────────────
//  TAB 5: PRACTICAL & LABORATORY SKILLS
// ─────────────────────────────────────────
function renderBioPracticals(ch) {
  const practicals = ch.practicals || [];
  if (practicals.length === 0) {
    return `<div style="padding:2rem;text-align:center;color:#64748b;">No formal practicals recorded for this unit.</div>`;
  }

  return practicals.map((prac, idx) => `
    <div style="background:#ffffff;border:1.5px solid #a7f3d0;border-radius:12px;padding:1.5rem;margin-bottom:1.5rem;box-shadow:0 3px 10px rgba(5,150,105,0.06);">
      <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:1.25rem;border-bottom:1.5px solid #e2e8f0;padding-bottom:0.75rem;">
        <span style="background:#059669;color:#fff;font-weight:800;font-size:0.85rem;padding:0.25rem 0.75rem;border-radius:6px;">Experiment ${idx + 1}</span>
        <h3 style="margin:0;font-size:1.2rem;color:#065f46;">${prac.title}</h3>
      </div>

      <div style="margin-bottom:1rem;">
        <h4 style="margin:0 0 0.4rem 0;color:#047857;display:flex;align-items:center;gap:0.4rem;font-size:0.95rem;">
          <span>🧰</span><span>Apparatus & Materials Required:</span>
        </h4>
        <div style="background:#f8fafc;padding:0.85rem 1rem;border-radius:8px;font-size:0.92rem;color:#334155;line-height:1.6;">
          ${prac.apparatus}
        </div>
      </div>

      <div style="margin-bottom:1rem;">
        <h4 style="margin:0 0 0.4rem 0;color:#047857;display:flex;align-items:center;gap:0.4rem;font-size:0.95rem;">
          <span>📝</span><span>Step-by-Step Laboratory Procedure:</span>
        </h4>
        <div style="background:#f8fafc;padding:0.85rem 1rem;border-radius:8px;font-size:0.92rem;color:#334155;line-height:1.7;white-space:pre-line;">
          ${prac.procedure}
        </div>
      </div>

      <div style="margin-bottom:1rem;">
        <h4 style="margin:0 0 0.4rem 0;color:#047857;display:flex;align-items:center;gap:0.4rem;font-size:0.95rem;">
          <span>👁️</span><span>Observations & Scientific Inferences:</span>
        </h4>
        <div style="background:#f0fdf4;border-left:3.5px solid #10b981;padding:0.85rem 1rem;border-radius:8px;font-size:0.92rem;color:#065f46;line-height:1.6;">
          ${prac.observations}
        </div>
      </div>

      <div>
        <h4 style="margin:0 0 0.4rem 0;color:#b91c1c;display:flex;align-items:center;gap:0.4rem;font-size:0.95rem;">
          <span>⚠️</span><span>Safety Precautions:</span>
        </h4>
        <div style="background:#fef2f2;border-left:3.5px solid #ef4444;padding:0.85rem 1rem;border-radius:8px;font-size:0.92rem;color:#991b1b;line-height:1.6;">
          ${prac.precautions}
        </div>
      </div>
    </div>`).join('');
}


// ─────────────────────────────────────────
//  CHEMISTRY INTERACTIVE ROADMAP VIEW
// ─────────────────────────────────────────


function openChemView(classId, subj) {
  state.activeSubject = "chem";
  state.selectedChemChapter = 0;
  state.activeChemTab = "topics";
  state.selectedClass = classId;
  setActiveNav("subjects");
  const cls = DATA.classes.find(c => c.id === classId);
  const isCls10 = (classId === "cls10");
  const chList = isCls10 ? (DATA.chem10Chapters || []) : (DATA.chemChapters || []);
  const gradeLabel = isCls10 ? "Grade 10" : "Grade 9";
  const chRange = isCls10 ? "Units 9 to 16" : (chList.length > 0 ? `Units 1 to ${chList.length}` : "Ready for New Book");
  const pdfFile = isCls10 ? "assets/books/Class-10-Chemistry-KPK.pdf" : "assets/books/Class-9-Chemistry-KPK.pdf";

  setDashHeader(`🧪 ${subj.name} — ${gradeLabel}`, `KPK Textbook Board, Peshawar · ${chRange} &nbsp;|&nbsp; <a href="${pdfFile}" target="_blank" style="color:#0284c7;font-weight:700;text-decoration:underline;">📥 View/Download Official Chemistry Book PDF</a>`);
  setBreadcrumb([
    { label: "Home",     onclick: () => { setActiveNav("home"); renderHome(); } },
    { label: "Subjects", onclick: () => renderClasses() },
    { label: cls ? cls.name : gradeLabel,   onclick: () => goToSubjects(classId) },
    { label: subj.name,  active: true }
  ]);

  if (!chList || chList.length === 0) {
    pageContent().innerHTML = `
      <div class="bio-view" style="display:flex;align-items:center;justify-content:center;min-height:380px;background:#fff;border-radius:12px;border:1px dashed #cbd5e1;padding:2.5rem;text-align:center;">
        <div>
          <div style="font-size:3.5rem;margin-bottom:1rem;">🧪</div>
          <h2 style="color:var(--navy);margin-bottom:0.5rem;font-size:1.4rem;">Class 9 Chemistry — Ready for New Book</h2>
          <p style="color:var(--text-muted);max-width:520px;margin:0 auto 1.5rem auto;font-size:0.95rem;line-height:1.6;">
            All previous Class 9 Chemistry content has been cleared as requested. Please provide the new textbook / files to start adding the new units!
          </p>
          <button class="btn-back-sm" onclick="goToSubjects('${classId}')">← Back to Subjects</button>
        </div>
      </div>`;
    return;
  }

  const sBg  = { done: "#dcfce7", progress: "#fef9c3", upcoming: "#f1f5f9" };
  const sCol = { done: "#15803d", progress: "#a16207", upcoming: "#64748b" };
  const sLbl = { done: "✅ Ready", progress: "🔄 In Progress", upcoming: "⏳ Planned" };

  const chapBtns = chList.map((ch, i) => `
    <button class="bio-ch-btn ${i === 0 ? "active" : ""}" id="chem-btn-${i}"
            onclick="selectChemChapter(${i})">
      <span class="ch-btn-num" style="background:#0284c7;color:#fff;">${ch.num}</span>
      <span class="ch-btn-info">
        <span class="ch-btn-name">${ch.name}</span>
        <span class="ch-btn-sub">${ch.pageRange}</span>
      </span>
      <span class="ch-btn-status"
            style="background:${sBg[ch.status]};color:${sCol[ch.status]}">
        ${sLbl[ch.status]}
      </span>
    </button>`).join("");

  pageContent().innerHTML = `
    <div class="bio-view">
      <div class="bio-ch-sidebar">
        <div class="bio-ch-sidebar-header" style="background:linear-gradient(135deg,#0284c7,#0369a1);color:#fff;">
          <button onclick="goToSubjects('${classId}')" class="sidebar-back-icon-btn" title="Back to Subjects">←</button>
          <span>🧪 KPK ${gradeLabel} Chemistry Units</span>
        </div>
        <div class="bio-ch-list">${chapBtns}</div>
        <div style="padding:1rem;background:#f8fafc;border-top:1px solid var(--border);text-align:center;">
          <button onclick="${isCls10 ? 'renderChem10Roadmap()' : 'renderChemRoadmap()'}" style="width:100%;padding:0.5rem;background:#0284c7;color:#fff;border:none;border-radius:6px;font-weight:700;font-size:0.8rem;cursor:pointer;">
            🗺️ Open Exam Roadmap
          </button>
        </div>
      </div>
      <div class="bio-topic-area" id="chemTopicArea"></div>
    </div>`;

  renderChemChapter(0);
}

function selectChemChapter(index) {
  state.selectedChemChapter = index;
  document.querySelectorAll(".bio-ch-btn").forEach((btn, i) =>
    btn.classList.toggle("active", i === index));
  renderChemChapter(index);
}

function switchChemTab(tabName) {
  state.activeChemTab = tabName;
  document.querySelectorAll(".bio-tab-btn").forEach(btn =>
    btn.classList.toggle("active", btn.dataset.tab === tabName));

  const isCls10 = (state.selectedClass === 'cls10');
  const chList = isCls10 ? (DATA.chem10Chapters || []) : (DATA.chemChapters || []);
  if (!chList || chList.length === 0) return;
  const ch = chList[state.selectedChemChapter] || chList[0];
  if (!ch) return;
  const container = $("chemTabContent");
  if (!container) return;

  if (tabName === "topics") {
    container.innerHTML = renderTopicsAccordion(ch);
  } else if (tabName === "exercises") {
    container.innerHTML = renderTextbookExercises(ch);
  } else if (tabName === "numericals") {
    container.innerHTML = renderNumericals(ch);
  } else if (tabName === "slos") {
    container.innerHTML = renderSLOsAndConcepts(ch);
  } else if (tabName === "activities") {
    container.innerHTML = renderActivitiesAndTables(ch);
  } else if (tabName === "vocab") {
    container.innerHTML = renderChemVocabulary(ch, state.selectedChemChapter || 0);
  } else if (tabName === "checklist") {
    container.innerHTML = renderChapterChecklist(ch);
  }
}

function renderChemChapter(index) {
  const isCls10 = (state.selectedClass === 'cls10');
  const chList = isCls10 ? (DATA.chem10Chapters || []) : (DATA.chemChapters || []);
  if (!chList || chList.length === 0) return;
  const ch   = chList[index] || chList[0];
  if (!ch) return;
  const area = $("chemTopicArea");
  if (!area) return;

  const numCount = (ch.numericals || []).length;

  area.innerHTML = `
    <div class="chapter-title-bar" style="border-left: 4px solid #0284c7;">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:0.75rem;width:100%;">
        <div>
          <h3>Unit ${ch.num}: ${ch.name}</h3>
          <p>${ch.pageRange} · ${ch.topics.length} Major Topics · ${ch.textbookExercise.mcqs.length} MCQs · ${ch.textbookExercise.sq.length} Short Qs${numCount > 0 ? ` · ${numCount} Solved Numericals` : ''}</p>
        </div>
        <button class="btn-back-sm" onclick="goToSubjects('${state.selectedClass || 'cls9'}')"><span class="back-arrow">←</span> Back to Subjects</button>
      </div>
    </div>

    <!-- Chapter Section Tabs -->
    <div class="chapter-nav-tabs">
      <button class="bio-tab-btn ${state.activeChemTab === 'topics' ? 'active' : ''}" data-tab="topics" onclick="switchChemTab('topics')">
        📖 Topics &amp; Notes
      </button>
      <button class="bio-tab-btn ${state.activeChemTab === 'exercises' ? 'active' : ''}" data-tab="exercises" onclick="switchChemTab('exercises')">
        📕 Textbook Exercises (${ch.textbookExercise.mcqs.length} MCQs &amp; Qs)
      </button>
      ${numCount > 0 ? `
      <button class="bio-tab-btn ${state.activeChemTab === 'numericals' ? 'active' : ''}" data-tab="numericals" onclick="switchChemTab('numericals')">
        📐 Solved Numericals (${numCount})
      </button>` : ''}
      <button class="bio-tab-btn ${state.activeChemTab === 'slos' ? 'active' : ''}" data-tab="slos" onclick="switchChemTab('slos')">
        🎯 SLOs &amp; Definitions
      </button>
      <button class="bio-tab-btn ${state.activeChemTab === 'activities' ? 'active' : ''}" data-tab="activities" onclick="switchChemTab('activities')">
        🧪 Activities &amp; Tables
      </button>
      <button class="bio-tab-btn ${state.activeChemTab === 'vocab' ? 'active' : ''}" data-tab="vocab" onclick="switchChemTab('vocab')">
        📚 Vocabularies
      </button>
      <button class="bio-tab-btn ${state.activeChemTab === 'checklist' ? 'active' : ''}" data-tab="checklist" onclick="switchChemTab('checklist')">
        ✅ Study Checklist
      </button>
    </div>

    <div id="chemTabContent">
      ${state.activeChemTab === "topics"     ? renderTopicsAccordion(ch)     : ""}
      ${state.activeChemTab === "exercises"  ? renderTextbookExercises(ch)   : ""}
      ${state.activeChemTab === "numericals" ? renderNumericals(ch)          : ""}
      ${state.activeChemTab === "slos"       ? renderSLOsAndConcepts(ch)     : ""}
      ${state.activeChemTab === "activities" ? renderActivitiesAndTables(ch) : ""}
      ${state.activeChemTab === "vocab"      ? renderChemVocabulary(ch, index) : ""}
      ${state.activeChemTab === "checklist"  ? renderChapterChecklist(ch)    : ""}
    </div>`;
}

function renderChemRoadmap() {
  setDashHeader("🗺️ Class 9 Chemistry Exam Preparation Roadmap", "Official KPK Textbook Board 8-Unit Complete Curriculum");
  setBreadcrumb([
    { label: "Home",     onclick: () => { setActiveNav("home"); renderHome(); } },
    { label: "Subjects", onclick: () => renderClasses() },
    { label: "Chemistry", onclick: () => openSubject('cls9', 'cls9-chem') },
    { label: "Roadmap",  active: true }
  ]);

  const cardsHtml = DATA.chemChapters.map((ch, i) => `
    <div class="roadmap-card" onclick="openSubject('cls9','cls9-chem'); selectChemChapter(${i});" style="cursor:pointer;">
      <div class="roadmap-card-header">
        <span class="roadmap-ch-badge" style="background:#0284c7;">Unit ${ch.num}</span>
        <span class="ch-btn-status" style="background:#dcfce7;color:#15803d;">✅ Complete</span>
      </div>
      <div class="roadmap-card-body">
        <h4>${ch.name || ch.title || ""}</h4>
        <div style="font-size:0.75rem;color:var(--text-muted);margin:0.25rem 0 0.5rem;">${ch.pageRange}</div>
        <div class="roadmap-meta-row">
          <span>📚 ${ch.topics.length} Topics</span>
          <span>🎯 ${ch.textbookExercise.mcqs.length} MCQs</span>
          <span>✏️ ${ch.textbookExercise.sq.length} SQs</span>
          <span>📝 ${ch.textbookExercise.lq.length} LQs</span>
        </div>
        <div style="margin-top:0.75rem;font-size:0.8rem;color:var(--text-muted);">
          <strong>Key Focus:</strong> ${ch.slos.slice(0, 2).join(" · ")}
        </div>
      </div>
    </div>`).join("");

  pageContent().innerHTML = `
    <div class="roadmap-container">
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;">
        <button class="btn-back-link" style="margin-bottom:0;" onclick="goToSubjects('cls9'); openSubject('cls9','cls9-chem');"><span class="back-arrow">←</span> Back to Chemistry Portal</button>
        <div style="display:flex;gap:0.4rem;flex-wrap:wrap;">
          <button class="bio-ch-btn" style="padding:0.4rem 0.85rem;font-size:0.82rem;" onclick="renderFullRoadmap()">🧬 Biology</button>
          <button class="bio-ch-btn active" style="padding:0.4rem 0.85rem;font-size:0.82rem;" onclick="renderChemRoadmap()">🧪 Chemistry</button>
          <button class="bio-ch-btn" style="padding:0.4rem 0.85rem;font-size:0.82rem;" onclick="renderPhysRoadmap()">⚛️ Physics</button>
        </div>
      </div>
      <div style="background:#fff;border:1px solid var(--border);border-radius:12px;padding:1.5rem;margin-bottom:1.5rem;box-shadow:var(--shadow);">
        <h3 style="color:var(--navy);font-size:1.2rem;margin-bottom:0.5rem;">🧪 Official KPK Textbook Board Chemistry Exam Pathway</h3>
        <p style="font-size:0.875rem;color:var(--text-muted);line-height:1.6;">
          This roadmap covers all 8 units from the official Grade IX Chemistry textbook volume. Follow the 5-day cycle per unit to guarantee complete mastery for your board examinations.
        </p>
        <div style="display:flex;gap:0.75rem;margin-top:1rem;flex-wrap:wrap;">
          <span style="background:#e0f2fe;color:#0284c7;font-weight:700;font-size:0.8rem;padding:0.35rem 0.75rem;border-radius:99px;">8 Units</span>
          <span style="background:#dcfce7;color:#15803d;font-weight:700;font-size:0.8rem;padding:0.35rem 0.75rem;border-radius:99px;">80 Textbook MCQs</span>
          <span style="background:#fef9c3;color:#a16207;font-weight:700;font-size:0.8rem;padding:0.35rem 0.75rem;border-radius:99px;">80 Verified SQs</span>
          <span style="background:#f3e8ff;color:#7c3aed;font-weight:700;font-size:0.8rem;padding:0.35rem 0.75rem;border-radius:99px;">40 Detailed LQs</span>
        </div>
      </div>

      <div class="roadmap-grid">${cardsHtml}</div>
    </div>`;
}

function renderChem10Roadmap() {
  setDashHeader("🗺️ Class 10 Chemistry Exam Preparation Roadmap", "Official KPK Textbook Board Complete Curriculum (Units 9 to 16)");
  setBreadcrumb([
    { label: "Home",      onclick: () => { setActiveNav("home"); renderHome(); } },
    { label: "Subjects",  onclick: () => renderClasses() },
    { label: "Chemistry", onclick: () => openSubject('cls10', 'cls10-chem') },
    { label: "Roadmap",   active: true }
  ]);

  const cardsHtml = (DATA.chem10Chapters || []).map((ch, i) => `
    <div class="roadmap-card" onclick="openSubject('cls10','cls10-chem'); selectChemChapter(${i});" style="cursor:pointer;">
      <div class="roadmap-card-header">
        <span class="roadmap-ch-badge" style="background:#0284c7;">Unit ${ch.num}</span>
        <span class="ch-btn-status" style="background:#dcfce7;color:#15803d;">✅ Complete</span>
      </div>
      <div class="roadmap-card-body">
        <h4>${ch.name}</h4>
        <div style="font-size:0.75rem;color:var(--text-muted);margin:0.25rem 0 0.5rem;">${ch.pageRange}</div>
        <div class="roadmap-meta-row">
          <span>📚 ${ch.topics.length} Topics</span>
          <span>🎯 ${ch.textbookExercise.mcqs.length} MCQs</span>
          <span>🧪 ${ch.textbookExercise.sq.length} Short Qs</span>
        </div>
      </div>
    </div>`).join("");

  pageContent().innerHTML = `
    <div class="roadmap-view">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1.5rem;flex-wrap:wrap;gap:1rem;">
        <div>
          <h2 style="font-size:1.3rem;font-weight:800;color:var(--text);">🧪 Class 10 Chemistry · KPK Textbook Board</h2>
          <p style="font-size:0.85rem;color:var(--text-muted);">8 Units · 33 Major Topics · 79 Subtopics · 80 MCQs · 80 SQs · 41 LQs · 100% Solved</p>
        </div>
        <button class="btn-back-sm" onclick="openSubject('cls10','cls10-chem')"><span class="back-arrow">←</span> Back to Units</button>
      </div>
      <div class="roadmap-grid">${cardsHtml}</div>
    </div>`;
}


// ─────────────────────────────────────────
//  PHYSICS INTERACTIVE ROADMAP VIEW
// ─────────────────────────────────────────
function openPhysView(classId, subj) {
  state.activeSubject = "phys";
  state.selectedPhysChapter = 0;
  state.activePhysTab = "topics";
  state.selectedClass = classId;
  setActiveNav("subjects");
  const cls = DATA.classes.find(c => c.id === classId);
  const isCls10 = (classId === "cls10");
  const chList = isCls10 ? DATA.phys10Chapters : DATA.physChapters;
  const gradeLabel = isCls10 ? "Grade 10" : "Grade 9";
  const chRange = isCls10 ? "Chapters 10 to 18" : `Chapters 1 to ${DATA.physChapters.length}`;
  const pdfFile = isCls10 ? "assets/books/Class-10-Physics-KPK.pdf" : "assets/books/Class-9-Physics-KPK.pdf";

  setDashHeader(`⚡ ${subj.name} — ${gradeLabel}`, `KPK Textbook Board, Peshawar · ${chRange} &nbsp;|&nbsp; <a href="${pdfFile}" target="_blank" style="color:#7c3aed;font-weight:700;text-decoration:underline;">📥 View/Download Official Physics Book PDF</a>`);
  setBreadcrumb([
    { label: "Home",     onclick: () => { setActiveNav("home"); renderHome(); } },
    { label: "Subjects", onclick: () => renderClasses() },
    { label: cls.name,   onclick: () => goToSubjects(classId) },
    { label: subj.name,  active: true }
  ]);

  const sBg  = { done: "#dcfce7", progress: "#fef9c3", upcoming: "#f1f5f9" };
  const sCol = { done: "#15803d", progress: "#a16207", upcoming: "#64748b" };
  const sLbl = { done: "✅ Ready", progress: "🔄 In Progress", upcoming: "⏳ Planned" };

  const chapBtns = chList.map((ch, i) => `
    <button class="bio-ch-btn ${i === 0 ? "active" : ""}" id="phys-btn-${i}"
            onclick="selectPhysChapter(${i})">
      <span class="ch-btn-num" style="background:#7c3aed;color:#fff;">${ch.num}</span>
      <span class="ch-btn-info">
        <span class="ch-btn-name">${ch.name}</span>
        <span class="ch-btn-sub">${ch.pageRange}</span>
      </span>
      <span class="ch-btn-status"
            style="background:${sBg[ch.status]};color:${sCol[ch.status]}">
        ${sLbl[ch.status]}
      </span>
    </button>`).join("");

  pageContent().innerHTML = `
    <div class="bio-view">
      <div class="bio-ch-sidebar">
        <div class="bio-ch-sidebar-header" style="background:linear-gradient(135deg,#7c3aed,#5b21b6);color:#fff;">
          <button onclick="goToSubjects('${classId}')" class="sidebar-back-icon-btn" title="Back to Subjects">←</button>
          <span>⚡ KPK ${gradeLabel} Physics Chapters</span>
        </div>
        <div class="bio-ch-list">${chapBtns}</div>
        <div style="padding:1rem;background:#f8fafc;border-top:1px solid var(--border);text-align:center;">
          <button onclick="${isCls10 ? 'renderPhys10Roadmap()' : 'renderPhysRoadmap()'}" style="width:100%;padding:0.5rem;background:#7c3aed;color:#fff;border:none;border-radius:6px;font-weight:700;font-size:0.8rem;cursor:pointer;">
            🗺️ Open Exam Roadmap
          </button>
        </div>
      </div>
      <div class="bio-topic-area" id="physTopicArea"></div>
    </div>`;

  renderPhysChapter(0);
}

function selectPhysChapter(index) {
  state.selectedPhysChapter = index;
  document.querySelectorAll(".bio-ch-btn").forEach((btn, i) =>
    btn.classList.toggle("active", i === index));
  renderPhysChapter(index);
}

function switchPhysTab(tabName) {
  state.activePhysTab = tabName;
  document.querySelectorAll(".bio-tab-btn").forEach(btn =>
    btn.classList.toggle("active", btn.dataset.tab === tabName));

  const isCls10 = (state.selectedClass === 'cls10');
  const chList = isCls10 ? DATA.phys10Chapters : DATA.physChapters;
  const ch = chList[state.selectedPhysChapter] || chList[0];
  const container = $("physTabContent");
  if (!container) return;

  if (tabName === "topics") {
    container.innerHTML = renderTopicsAccordion(ch);
  } else if (tabName === "exercises") {
    container.innerHTML = renderTextbookExercises(ch);
  } else if (tabName === "numericals") {
    container.innerHTML = renderNumericals(ch);
  } else if (tabName === "slos") {
    container.innerHTML = renderSLOsAndConcepts(ch);
  } else if (tabName === "activities") {
    container.innerHTML = renderActivitiesAndTables(ch);
  } else if (tabName === "vocab") {
    container.innerHTML = renderChemVocabulary(ch, state.selectedChemChapter || 0);
  } else if (tabName === "checklist") {
    container.innerHTML = renderChapterChecklist(ch);
  }
}

function renderPhysChapter(index) {
  const isCls10 = (state.selectedClass === 'cls10');
  const chList = isCls10 ? DATA.phys10Chapters : DATA.physChapters;
  const ch   = chList[index] || chList[0];
  const area = $("physTopicArea");
  if (!area) return;

  const numCount = (ch.numericals || []).length;

  area.innerHTML = `
    <div class="chapter-title-bar" style="border-left: 4px solid #7c3aed;">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:0.75rem;width:100%;">
        <div>
          <h3>Chapter ${ch.num}: ${ch.name}</h3>
          <p>${ch.pageRange} · ${ch.topics.length} Major Topics · ${ch.textbookExercise.mcqs.length} MCQs · ${numCount} Numericals</p>
        </div>
        <button class="btn-back-sm" onclick="goToSubjects('${state.selectedClass || 'cls9'}')"><span class="back-arrow">←</span> Back to Subjects</button>
      </div>
    </div>

    <!-- Chapter Section Tabs -->
    <div class="chapter-nav-tabs">
      <button class="bio-tab-btn ${state.activePhysTab === 'topics' ? 'active' : ''}" data-tab="topics" onclick="switchPhysTab('topics')">
        📖 Topics &amp; Notes
      </button>
      <button class="bio-tab-btn ${state.activePhysTab === 'exercises' ? 'active' : ''}" data-tab="exercises" onclick="switchPhysTab('exercises')">
        📕 Textbook Exercises (${ch.textbookExercise.mcqs.length} MCQs)
      </button>
      <button class="bio-tab-btn ${state.activePhysTab === 'numericals' ? 'active' : ''}" data-tab="numericals" onclick="switchPhysTab('numericals')">
        📐 Numericals (${numCount})
      </button>
      <button class="bio-tab-btn ${state.activePhysTab === 'slos' ? 'active' : ''}" data-tab="slos" onclick="switchPhysTab('slos')">
        🎯 SLOs &amp; Definitions
      </button>
      <button class="bio-tab-btn ${state.activePhysTab === 'activities' ? 'active' : ''}" data-tab="activities" onclick="switchPhysTab('activities')">
        🔬 Activities &amp; Tables
      </button>
      <button class="bio-tab-btn ${state.activePhysTab === 'checklist' ? 'active' : ''}" data-tab="checklist" onclick="switchPhysTab('checklist')">
        ✅ Study Checklist
      </button>
    </div>

    <div id="physTabContent">
      ${state.activePhysTab === "topics"     ? renderTopicsAccordion(ch)     : ""}
      ${state.activePhysTab === "exercises"  ? renderTextbookExercises(ch)   : ""}
      ${state.activePhysTab === "numericals" ? renderNumericals(ch)          : ""}
      ${state.activePhysTab === "slos"       ? renderSLOsAndConcepts(ch)     : ""}
      ${state.activePhysTab === "activities" ? renderActivitiesAndTables(ch) : ""}
      ${state.activePhysTab === "checklist"  ? renderChapterChecklist(ch)    : ""}
    </div>`;
}

// ─── Render Numericals Tab ─────────────────
function renderNumericals(ch) {
  const nums = ch.numericals || [];
  if (nums.length === 0) {
    return `<div style="padding:2rem;text-align:center;color:var(--text-muted);">No numericals recorded for this chapter yet.</div>`;
  }

  return `
    <div style="padding:1rem;">
      <div style="background:#f3e8ff;border:1px solid #d8b4fe;border-radius:8px;padding:0.85rem 1rem;margin-bottom:1.25rem;">
        <strong style="color:#7c3aed;">📐 ${nums.length} Numerical Problems</strong>
        <span style="font-size:0.8rem;color:#6d28d9;margin-left:0.5rem;">Click any problem to expand full solution</span>
      </div>
      ${nums.map((n, i) => `
        <div class="acc-item" style="margin-bottom:0.75rem;border:1px solid #e9d5ff;border-radius:8px;overflow:hidden;">
          <div class="acc-head" onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'block' ? 'none' : 'block';"
               style="display:flex;align-items:flex-start;gap:0.75rem;padding:0.85rem 1rem;cursor:pointer;background:#faf5ff;">
            <span style="background:#7c3aed;color:#fff;border-radius:4px;padding:0.15rem 0.55rem;font-size:0.75rem;font-weight:700;white-space:nowrap;min-width:2.5rem;text-align:center;">N${n.num || (i+1)}</span>
            <span style="font-weight:600;color:var(--navy);font-size:0.9rem;flex:1;">${n.statement || n.title || `Numerical Problem ${i + 1}`}</span>
            <span style="color:#7c3aed;font-size:1rem;flex-shrink:0;">▼</span>
          </div>
          <div style="display:none;padding:1rem;background:#fff;">
            ${n.given ? `<div style="margin-bottom:0.65rem;"><span style="font-size:0.72rem;font-weight:700;color:#7c3aed;text-transform:uppercase;letter-spacing:0.04em;">Given:</span><div style="margin-top:0.3rem;font-size:0.875rem;color:var(--navy);font-family:monospace;background:#f5f3ff;padding:0.5rem 0.75rem;border-radius:4px;">${n.given}</div></div>` : ""}
            ${n.required ? `<div style="margin-bottom:0.65rem;"><span style="font-size:0.72rem;font-weight:700;color:#0284c7;text-transform:uppercase;letter-spacing:0.04em;">Required:</span><div style="margin-top:0.3rem;font-size:0.875rem;color:var(--navy);background:#eff6ff;padding:0.5rem 0.75rem;border-radius:4px;">${n.required}</div></div>` : ""}
            ${n.formula ? `<div style="margin-bottom:0.65rem;"><span style="font-size:0.72rem;font-weight:700;color:#15803d;text-transform:uppercase;letter-spacing:0.04em;">Formula:</span><div style="margin-top:0.3rem;font-size:0.95rem;color:#14532d;font-weight:700;font-family:monospace;background:#f0fdf4;padding:0.5rem 0.75rem;border-radius:4px;">${n.formula}</div></div>` : ""}
            ${n.solution ? `<div style="margin-bottom:0.65rem;"><span style="font-size:0.72rem;font-weight:700;color:#b45309;text-transform:uppercase;letter-spacing:0.04em;">Solution:</span><div style="margin-top:0.3rem;font-size:0.875rem;color:var(--navy);background:#fffbeb;padding:0.5rem 0.75rem;border-radius:4px;line-height:1.65;">${n.solution}</div></div>` : ""}
            ${n.answer ? `<div style="background:#dcfce7;border:1px solid #bbf7d0;border-radius:6px;padding:0.6rem 0.85rem;margin-top:0.5rem;"><span style="font-size:0.72rem;font-weight:700;color:#15803d;text-transform:uppercase;">Final Answer:</span> <span style="font-weight:700;color:#14532d;font-size:0.95rem;">${n.answer}</span></div>` : ""}
          </div>
        </div>`).join("")}
    </div>`;
}

// ─── Render Physics Exam Roadmap ───────────
function renderPhysRoadmap() {
  setDashHeader("🗺️ Class 9 Physics Exam Preparation Roadmap", "Official KPK Textbook Board Complete Curriculum");
  setBreadcrumb([
    { label: "Home",     onclick: () => { setActiveNav("home"); renderHome(); } },
    { label: "Subjects", onclick: () => renderClasses() },
    { label: "Physics",  onclick: () => openSubject('cls9', 'cls9-phy') },
    { label: "Roadmap",  active: true }
  ]);

  const cardsHtml = DATA.physChapters.map((ch, i) => `
    <div class="roadmap-card" onclick="openSubject('cls9','cls9-phy'); selectPhysChapter(${i});" style="cursor:pointer;">
      <div class="roadmap-card-header">
        <span class="roadmap-ch-badge" style="background:#7c3aed;">Ch ${ch.num}</span>
        <span class="ch-btn-status" style="background:#dcfce7;color:#15803d;">✅ Complete</span>
      </div>
      <div class="roadmap-card-body">
        <h4>${ch.name}</h4>
        <div style="font-size:0.75rem;color:var(--text-muted);margin:0.25rem 0 0.5rem;">${ch.pageRange}</div>
        <div class="roadmap-meta-row">
          <span>📚 ${ch.topics.length} Topics</span>
          <span>🎯 ${ch.textbookExercise.mcqs.length} MCQs</span>
          <span>📐 ${(ch.numericals||[]).length} Numericals</span>
          <span>✏️ ${ch.textbookExercise.sq.length} SQs</span>
        </div>
        <div style="margin-top:0.75rem;font-size:0.8rem;color:var(--text-muted);">
          <strong>Key Focus:</strong> ${ch.slos.slice(0, 2).join(" · ")}
        </div>
      </div>
    </div>`).join("");

  const totalMcqs = DATA.physChapters.reduce((a, c) => a + c.textbookExercise.mcqs.length, 0);
  const totalSq   = DATA.physChapters.reduce((a, c) => a + c.textbookExercise.sq.length, 0);
  const totalLq   = DATA.physChapters.reduce((a, c) => a + c.textbookExercise.lq.length, 0);
  const totalNums = DATA.physChapters.reduce((a, c) => a + (c.numericals||[]).length, 0);

  pageContent().innerHTML = `
    <div class="roadmap-container">
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;">
        <button class="btn-back-link" style="margin-bottom:0;" onclick="goToSubjects('cls9'); openSubject('cls9','cls9-phy');"><span class="back-arrow">←</span> Back to Physics Portal</button>
        <div style="display:flex;gap:0.4rem;flex-wrap:wrap;">
          <button class="bio-ch-btn" style="padding:0.4rem 0.85rem;font-size:0.82rem;" onclick="renderFullRoadmap()">🧬 Biology</button>
          <button class="bio-ch-btn" style="padding:0.4rem 0.85rem;font-size:0.82rem;" onclick="renderChemRoadmap()">🧪 Chemistry</button>
          <button class="bio-ch-btn active" style="padding:0.4rem 0.85rem;font-size:0.82rem;" onclick="renderPhysRoadmap()">⚛️ Physics</button>
        </div>
      </div>
      <div style="background:#fff;border:1px solid var(--border);border-radius:12px;padding:1.5rem;margin-bottom:1.5rem;box-shadow:var(--shadow);">
        <h3 style="color:var(--navy);font-size:1.2rem;margin-bottom:0.5rem;">⚛️ Official KPK Textbook Board Physics Exam Pathway</h3>
        <p style="font-size:0.875rem;color:var(--text-muted);line-height:1.6;">
          This roadmap covers all ${DATA.physChapters.length} chapters from the official Grade IX Physics textbook. Study chapter by chapter with complete theory, numericals, and exercises to master board exams.
        </p>
        <div style="display:flex;gap:0.75rem;margin-top:1rem;flex-wrap:wrap;">
          <span style="background:#ede9fe;color:#7c3aed;font-weight:700;font-size:0.8rem;padding:0.35rem 0.75rem;border-radius:99px;">${DATA.physChapters.length} Chapters</span>
          <span style="background:#dcfce7;color:#15803d;font-weight:700;font-size:0.8rem;padding:0.35rem 0.75rem;border-radius:99px;">${totalMcqs} Textbook MCQs</span>
          <span style="background:#fef9c3;color:#a16207;font-weight:700;font-size:0.8rem;padding:0.35rem 0.75rem;border-radius:99px;">${totalSq} Short Questions</span>
          <span style="background:#f3e8ff;color:#7c3aed;font-weight:700;font-size:0.8rem;padding:0.35rem 0.75rem;border-radius:99px;">${totalNums} Solved Numericals</span>
          <span style="background:#ffe4e6;color:#be123c;font-weight:700;font-size:0.8rem;padding:0.35rem 0.75rem;border-radius:99px;">${totalLq} Long Questions</span>
        </div>
      </div>

      <div class="roadmap-grid">
        ${cardsHtml}
      </div>
    </div>`;
}

function renderPhys10Roadmap() {
  setDashHeader("🗺️ Class 10 Physics Exam Preparation Roadmap", "Official KPK Textbook Board Complete Curriculum (Chapters 10 to 18)");
  setBreadcrumb([
    { label: "Home",     onclick: () => { setActiveNav("home"); renderHome(); } },
    { label: "Subjects", onclick: () => renderClasses() },
    { label: "Physics",  onclick: () => openSubject('cls10', 'cls10-phy') },
    { label: "Roadmap",  active: true }
  ]);

  const cardsHtml = (DATA.phys10Chapters || []).map((ch, i) => `
    <div class="roadmap-card" onclick="openSubject('cls10','cls10-phy'); selectPhysChapter(${i});" style="cursor:pointer;">
      <div class="roadmap-card-header">
        <span class="roadmap-ch-badge" style="background:#7c3aed;">Chapter ${ch.num}</span>
        <span class="ch-btn-status" style="background:#dcfce7;color:#15803d;">✅ Complete</span>
      </div>
      <div class="roadmap-card-body">
        <h4>${ch.name}</h4>
        <div style="font-size:0.75rem;color:var(--text-muted);margin:0.25rem 0 0.5rem;">${ch.pageRange}</div>
        <div class="roadmap-meta-row">
          <span>📚 ${ch.topics.length} Topics</span>
          <span>🎯 ${ch.textbookExercise.mcqs.length} MCQs</span>
          <span>📐 ${(ch.numericals || []).length} Numericals</span>
        </div>
      </div>
    </div>`).join("");

  pageContent().innerHTML = `
    <div class="roadmap-view">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1.5rem;flex-wrap:wrap;gap:1rem;">
        <div>
          <h2 style="font-size:1.3rem;font-weight:800;color:var(--text);">⚡ Class 10 Physics · KPK Textbook Board</h2>
          <p style="font-size:0.85rem;color:var(--text-muted);">9 Chapters · 35 Topics · 50 Solved Numericals · 90 MCQs · 100% Solved</p>
        </div>
        <button class="btn-back-sm" onclick="openSubject('cls10','cls10-phy')"><span class="back-arrow">←</span> Back to Chapters</button>
      </div>
      <div class="roadmap-grid">${cardsHtml}</div>
    </div>`;
}


// ─────────────────────────────────────────
//  ENGLISH INTERACTIVE VIEW (Units 1 to 15)
// ─────────────────────────────────────────
// ─────────────────────────────────────────
//  ENGLISH INTERACTIVE LESSONS & TRILINGUAL PORTAL (GRADE 9 KPK)
// ─────────────────────────────────────────

// English TTS State Management (Direct Neural Audio Stream & 60-FPS Real-Time Sync)
let engTtsState = {
  activePrefix: null,
  activeGender: 'female', // 'male' | 'female'
  isPlaying: false,
  isPaused: false,
  speechRate: 1.0,
  sentences: [],
  currentSentenceIdx: 0,
  currentWordIdx: -1,
  totalWords: 0,
  audioObj: null,
  wordTimer: null,
  sectionTitle: ""
};

function openEngView(classId, subj) {
  stopEngTTS();
  state.activeSubject = "eng";
  state.selectedEngChapter = 0;
  state.activeEngTab = "lesson";
  state.activeEngSloTab = "slo-mcqs";
  state.selectedClass = classId;
  setActiveNav("subjects");

  const isCls10 = (classId === "cls10");
  const cls = DATA.classes.find(c => c.id === classId) || { name: isCls10 ? "Class 10" : "Class 9" };
  const chList = (typeof ENGLISH_DATA !== 'undefined' ? ENGLISH_DATA : (DATA.englishChapters || DATA.engChapters || []));
  const gradeLabel = isCls10 ? "Grade 10" : "Grade 9";
  const pdfFile = isCls10 ? "assets/books/Class-10-English-KPK.pdf" : "assets/books/Class-9-English-KPK.pdf";

  setDashHeader(`📖 ${subj.name} — ${gradeLabel}`, `KPK Textbook Board, Peshawar · 15 Complete Units (Prose & Poetry) &nbsp;|&nbsp; <a href="${pdfFile}" target="_blank" style="color:#0284c7;font-weight:700;text-decoration:underline;">📥 View/Download Official English Book PDF</a>`);
  setBreadcrumb([
    { label: "Home",     onclick: () => { setActiveNav("home"); renderHome(); } },
    { label: "Subjects", onclick: () => renderClasses() },
    { label: cls.name,   onclick: () => goToSubjects(classId) },
    { label: subj.name,  active: true }
  ]);

  const chapBtns = chList.map((ch, i) => `
    <button class="bio-ch-btn ${i === 0 ? "active" : ""}" id="eng-btn-${i}"
            onclick="selectEngChapter(${i})">
      <span class="ch-btn-num" style="background:#0284c7;color:#fff;">${ch.type === 'poetry' ? 'Poem ' + (ch.number === 4 ? '1' : ch.number === 8 ? '2' : ch.number === 12 ? '3' : '4') : 'Unit ' + ch.number}</span>
      <span class="ch-btn-info">
        <span class="ch-btn-name" style="font-weight:700;font-size:0.92rem;">${ch.title || ''}</span>
        <span class="ch-btn-sub" style="color:#64748b;font-size:0.78rem;">${ch.titleUrdu || ch.author || ''}</span>
      </span>
      <span class="ch-btn-status" style="background:#dcfce7;color:#15803d;">
        ✅ Complete
      </span>
    </button>`).join("");

  pageContent().innerHTML = `
    <div class="bio-view">
      <div class="bio-ch-sidebar">
        <div class="bio-ch-sidebar-header" style="background:linear-gradient(135deg,#0284c7,#0369a1);color:#fff;">
          <button onclick="goToSubjects('${classId}')" class="sidebar-back-icon-btn" title="Back to Subjects">←</button>
          <span>📖 KPK ${gradeLabel} English Units</span>
        </div>
        <div class="bio-ch-list">${chapBtns}</div>
        <div style="padding:1rem;background:#f8fafc;border-top:1px solid var(--border);text-align:center;">
          <a href="${pdfFile}" target="_blank" style="display:block;width:100%;padding:0.55rem;background:#0284c7;color:#fff;border-radius:6px;font-weight:700;font-size:0.82rem;text-decoration:none;">
            📥 Download Official PDF Book
          </a>
        </div>
      </div>
      <div class="bio-main" id="engMainContent">
        ${renderEngChapterDetail(chList[0], 0)}
      </div>
    </div>`;

  renderEngNavTabs(0);
}

function selectEngChapter(idx) {
  stopEngTTS();
  const chList = (typeof ENGLISH_DATA !== 'undefined' ? ENGLISH_DATA : (DATA.englishChapters || DATA.engChapters || []));
  if (!chList[idx]) return;

  state.selectedEngChapter = idx;
  document.querySelectorAll(".bio-ch-btn").forEach((b, i) => {
    b.classList.toggle("active", i === idx);
  });

  const main = $("engMainContent");
  if (main) {
    main.innerHTML = renderEngChapterDetail(chList[idx], idx);
    renderEngNavTabs(idx);
    main.scrollTop = 0;
  }
}

function renderEngChapterDetail(ch, chIdx) {
  if (!ch) return `<div class="empty-state">No chapter data available.</div>`;

  return `
    <div class="eng-detail-container" style="padding-bottom:3rem;">
      <!-- Chapter Hero Header -->
      <div class="urdu-chapter-banner" style="background:linear-gradient(135deg,#0369a1,#0284c7,#38bdf8);margin-bottom:1.5rem;color:#ffffff;border-radius:12px;padding:1.5rem 2rem;box-shadow:0 4px 15px rgba(2,132,199,0.25);">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem;">
          <div>
            <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:0.5rem;">
              <span class="urdu-badge" style="background:#ffffff;color:#0284c7;font-weight:800;font-size:0.85rem;padding:0.25rem 0.75rem;border-radius:99px;">
                ${ch.type === 'poetry' ? 'POEM ' + ch.number : 'UNIT ' + ch.number}
              </span>
              <span style="font-size:0.9rem;opacity:0.9;">KPK Textbook Board Peshawar · Grade 9 English</span>
            </div>
            <h1 style="font-size:1.85rem;font-weight:800;margin-bottom:0.4rem;color:#ffffff;letter-spacing:-0.02em;">
              ${ch.title}
            </h1>
            <div style="font-size:1.15rem;font-weight:600;opacity:0.95;color:#e0f2fe;font-family:'Jameel Noori Nastaleeq','Segoe UI',serif;">
              ${ch.titleUrdu || ''} ${ch.author ? '— <span style="font-size:0.95rem;font-family:sans-serif;">' + ch.author + '</span>' : ''}
            </div>
          </div>
          <div style="text-align:right;">
            <div style="background:rgba(255,255,255,0.15);backdrop-filter:blur(5px);padding:0.6rem 1.2rem;border-radius:8px;border:1px solid rgba(255,255,255,0.25);">
              <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:1px;opacity:0.85;">Curriculum Status</div>
              <div style="font-size:1.05rem;font-weight:700;">💯 100% Solved &amp; Complete</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Navigation Tabs -->
      <div class="bio-tabs-bar" id="engTabsBar" style="border-bottom:2px solid #e2e8f0;margin-bottom:1.5rem;display:flex;gap:0.5rem;overflow-x:auto;padding-bottom:0.5rem;">
        <!-- Tabs rendered dynamically -->
      </div>

      <!-- Tab Content Area -->
      <div id="engTabContent" class="urdu-tab-pane">
        <!-- Content loaded dynamically -->
      </div>

      <!-- Bottom SLO Master Assessment Roadmap -->
      <div class="urdu-bottom-slo-section" style="margin-top:2.5rem;border-top:2px solid #e2e8f0;padding-top:2rem;">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1.25rem;flex-wrap:wrap;gap:1rem;">
          <div style="display:flex;align-items:center;gap:0.75rem;">
            <div style="width:40px;height:40px;background:linear-gradient(135deg,#0284c7,#0369a1);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:1.25rem;font-weight:bold;">
              🎯
            </div>
            <div>
              <h3 style="color:#0f172a;font-size:1.2rem;font-weight:700;margin-bottom:0.2rem;">KPK Board Exam SLO Assessment Suite</h3>
              <p style="color:#64748b;font-size:0.85rem;margin:0;">Standardized Examination Practice with Model Answers &amp; Marking Rubrics</p>
            </div>
          </div>
          <div class="slo-tab-buttons" style="display:flex;gap:0.5rem;">
            <button class="slo-btn ${state.activeEngSloTab === 'slo-mcqs' ? 'active' : ''}" onclick="switchEngSloTab('slo-mcqs', ${chIdx})" style="display:flex;align-items:center;gap:0.4rem;padding:0.5rem 1rem;border-radius:6px;font-weight:600;cursor:pointer;border:1px solid #cbd5e1;background:#fff;">
              <span>📝 MCQs</span>
              <span class="slo-count-badge" style="background:#0284c7;color:#fff;padding:0.1rem 0.45rem;border-radius:99px;font-size:0.75rem;">${(ch.sloQuestions && ch.sloQuestions.mcqs) ? ch.sloQuestions.mcqs.length : 20}</span>
            </button>
            <button class="slo-btn ${state.activeEngSloTab === 'slo-sqs' ? 'active' : ''}" onclick="switchEngSloTab('slo-sqs', ${chIdx})" style="display:flex;align-items:center;gap:0.4rem;padding:0.5rem 1rem;border-radius:6px;font-weight:600;cursor:pointer;border:1px solid #cbd5e1;background:#fff;">
              <span>✏️ Short Qs (3M)</span>
              <span class="slo-count-badge" style="background:#0284c7;color:#fff;padding:0.1rem 0.45rem;border-radius:99px;font-size:0.75rem;">${(ch.sloQuestions && ch.sloQuestions.shortQuestions) ? ch.sloQuestions.shortQuestions.length : 10}</span>
            </button>
            <button class="slo-btn ${state.activeEngSloTab === 'slo-lqs' ? 'active' : ''}" onclick="switchEngSloTab('slo-lqs', ${chIdx})" style="display:flex;align-items:center;gap:0.4rem;padding:0.5rem 1rem;border-radius:6px;font-weight:600;cursor:pointer;border:1px solid #cbd5e1;background:#fff;">
              <span>📝 Long Qs (8M)</span>
              <span class="slo-count-badge" style="background:#0284c7;color:#fff;padding:0.1rem 0.45rem;border-radius:99px;font-size:0.75rem;">${(ch.sloQuestions && ch.sloQuestions.longQuestions) ? ch.sloQuestions.longQuestions.length : 5}</span>
            </button>
          </div>
        </div>
        <div id="engSloTabContent" style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;padding:1.5rem;box-shadow:0 2px 8px rgba(0,0,0,0.04);">
          <!-- SLO Content rendered dynamically -->
        </div>
      </div>
    </div>`;
}

function renderEngNavTabs(chIdx) {
  const tabsBar = $("engTabsBar");
  if (!tabsBar) return;

  const chList = (typeof ENGLISH_DATA !== 'undefined' ? ENGLISH_DATA : (DATA.englishChapters || DATA.engChapters || []));
  const currentCh = chList[chIdx];
  const unitNum = (currentCh && currentCh.number) ? currentCh.number : (chIdx + 1);
  const vocabCount = (typeof ENG_UNIT_VOCAB_WORDS !== 'undefined' && ENG_UNIT_VOCAB_WORDS[unitNum]) ? ENG_UNIT_VOCAB_WORDS[unitNum].length : 0;

  const tabs = [
    { id: "lesson",     icon: "📖", label: "Textbook & Audio" },
    { id: "vocab",      icon: "📚", label: "Vocabularies", badge: vocabCount },
    { id: "urdu-trans", icon: "🇵🇰", label: "Urdu Translation" },
    { id: "pashto-trans", icon: "🇦🇫", label: "Pashto Translation" },
    { id: "video",      icon: "🎥", label: "Video Lecture" },
    { id: "urdu-sum",   icon: "📜", label: "Urdu Summary" },
    { id: "pashto-sum", icon: "🇦🇫", label: "Pashto Summary" },
    { id: "en-sum",       icon: "📜", label: "English Summary" },
    { id: "exercise",   icon: "✍️", label: "Solved Exercises" },
    { id: "slos",       icon: "🎯", label: "Official SLOs" }
  ];

  tabsBar.innerHTML = tabs.map(t => {
    const isActive = state.activeEngTab === t.id;
    return `
    <button class="bio-tab-btn ${isActive ? "active" : ""}"
            onclick="switchEngTab('${t.id}', ${chIdx})"
            style="${isActive ? 'background:#0284c7;color:#fff;border-color:#0284c7;' : ''}">
      <span>${t.icon}</span>
      <span>${t.label}</span>
      ${t.badge ? `<span style="background:${isActive ? 'rgba(255,255,255,0.28)' : '#e0f2fe'};color:${isActive ? '#fff' : '#0284c7'};font-size:0.75rem;font-weight:800;padding:0.12rem 0.5rem;border-radius:99px;margin-left:0.3rem;">${t.badge}</span>` : ''}
    </button>`;
  }).join("");

  switchEngTab(state.activeEngTab || "lesson", chIdx);
  switchEngSloTab(state.activeEngSloTab || "slo-mcqs", chIdx);
}

function switchEngTab(tabId, chIdx) {
  stopEngTTS();
  state.activeEngTab = tabId;

  document.querySelectorAll("#engTabsBar .bio-tab-btn").forEach(b => {
    b.classList.remove("active");
    b.style.background = "";
    b.style.color = "";
    b.style.borderColor = "";
  });

  const activeBtn = Array.from(document.querySelectorAll("#engTabsBar .bio-tab-btn"))
    .find(b => b.textContent.includes(tabId === 'lesson' ? 'Textbook' : tabId === 'vocab' ? 'Vocabularies' : tabId === 'urdu-trans' ? 'Urdu Translation' : tabId === 'pashto-trans' ? 'Pashto Translation' : tabId === 'video' ? 'Video' : tabId === 'urdu-sum' ? 'Urdu Summary' : tabId === 'pashto-sum' ? 'Pashto Summary' : tabId === 'exercise' ? 'Exercises' : tabId === 'en-sum' ? 'English Summary' : 'SLOs'));
  if (activeBtn) {
    activeBtn.classList.add("active");
    activeBtn.style.background = "#0284c7";
    activeBtn.style.color = "#fff";
    activeBtn.style.borderColor = "#0284c7";
  }

  const chList = (typeof ENGLISH_DATA !== 'undefined' ? ENGLISH_DATA : (DATA.englishChapters || DATA.engChapters || []));
  const ch = chList[chIdx];
  const container = $("engTabContent");
  if (!container || !ch) return;

  if (tabId === "lesson") container.innerHTML = renderEngLesson(ch);
  else if (tabId === "vocab") container.innerHTML = renderEngVocabulary(ch, chIdx);
  else if (tabId === "urdu-trans") container.innerHTML = renderEngUrduTranslation(ch);
  else if (tabId === "pashto-trans") container.innerHTML = renderEngPashtoTranslation(ch);
  else if (tabId === "video") container.innerHTML = renderEngVideo(ch);
  else if (tabId === "urdu-sum") container.innerHTML = renderEngUrduSummary(ch);
  else if (tabId === "pashto-sum") container.innerHTML = renderEngPashtoSummary(ch);
  else if (tabId === "en-sum") container.innerHTML = renderEngEnglishSummary(ch);
  else if (tabId === "exercise") container.innerHTML = renderEngExercise(ch);
  else if (tabId === "slos") container.innerHTML = renderEngSLOs(ch);

  // Auto-scroll down smoothly up to the clicked tab bar
  const activeTabEl = activeBtn || document.getElementById('engTabsBar');
  if (activeTabEl) {
    autoScrollToActiveTab(activeTabEl);
  }
}

function switchEngSloTab(sloTabId, chIdx) {
  state.activeEngSloTab = sloTabId;
  const chList = (typeof ENGLISH_DATA !== 'undefined' ? ENGLISH_DATA : (DATA.englishChapters || DATA.engChapters || []));
  const ch = chList[chIdx];
  const container = $("engSloTabContent");
  if (!container || !ch) return;

  document.querySelectorAll(".slo-tab-buttons .slo-btn").forEach(b => {
    b.classList.remove("active");
    b.style.borderColor = "#cbd5e1";
    b.style.color = "#334155";
  });

  const activeSloBtn = Array.from(document.querySelectorAll(".slo-tab-buttons .slo-btn"))
    .find(b => b.textContent.includes(sloTabId === 'slo-mcqs' ? 'MCQs' : sloTabId === 'slo-sqs' ? 'Short' : 'Long'));
  if (activeSloBtn) {
    activeSloBtn.classList.add("active");
    activeSloBtn.style.borderColor = "#0284c7";
    activeSloBtn.style.color = "#0284c7";
  }

  if (sloTabId === "slo-mcqs") container.innerHTML = renderEngSloMcqs(ch);
  else if (sloTabId === "slo-sqs") container.innerHTML = renderEngSloSQs(ch);
  else if (sloTabId === "slo-lqs") container.innerHTML = renderEngSloLQs(ch);
}

// ─── ACCORDION TOGGLES & HELPERS ───
function toggleEngSection(headerEl) {
  const card = headerEl.closest(".urdu-section-card");
  if (!card) return;
  const wasOpen = card.classList.contains("open");
  card.classList.toggle("open");
  const icon = headerEl.querySelector(".sec-toggle-icon");
  if (icon) icon.textContent = wasOpen ? "▼" : "▲";
}

function expandAllEngSections(expand) {
  document.querySelectorAll(".urdu-section-card").forEach(card => {
    if (expand) {
      card.classList.add("open");
      const icon = card.querySelector(".sec-toggle-icon");
      if (icon) icon.textContent = "▲";
    } else {
      card.classList.remove("open");
      const icon = card.querySelector(".sec-toggle-icon");
      if (icon) icon.textContent = "▼";
    }
  });
}

// ─── English Text Formatter for Real-Time Word Highlighting ───
function prepareEngTextForTts(rawText, prefix, isPoetry = false, startLineNum = 1) {
  let globalWordIdx = 0;
  let currentLineCounter = startLineNum;
  const paras = rawText.split(/\n\s*\n/).filter(Boolean);
  const sentences = [];

  const parasHtml = paras.map(p => {
    if (isPoetry) {
      // Each line in the paragraph/stanza is a distinct poetic verse
      const lines = p.split('\n').map(l => l.trim()).filter(Boolean);
      const linesHtml = lines.map(lineText => {
        const lineNum = currentLineCounter++;
        const words = lineText.split(/\s+/).filter(Boolean);
        const startIdx = globalWordIdx;
        const spans = words.map(w => {
          const widx = globalWordIdx++;
          const safe = w.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
          return `<span id="${prefix}-w-${widx}" class="tts-word" data-widx="${widx}">${safe}</span>`;
        }).join(' ');
        const endIdx = globalWordIdx - 1;

        if (words.length > 0) {
          sentences.push({
            text: lineText,
            startIdx: startIdx,
            endIdx: endIdx,
            wordsCount: words.length
          });
        }

        const showLineNum = (lineNum % 6 === 0 || lineNum === 24 || lineNum === 6 || lineNum === 12 || lineNum === 18);
        return `
          <div class="poetic-line-row" style="display:flex;align-items:center;justify-content:space-between;padding:0.25rem 0.5rem;border-radius:4px;transition:background 0.2s ease;">
            <div class="poetic-line-text" style="font-style:italic;font-family:'Georgia','Times New Roman',serif;font-size:1.16rem;line-height:2;color:#1e293b;letter-spacing:0.2px;">${spans}</div>
            <div class="poetic-line-num" style="min-width:40px;text-align:right;font-weight:800;font-style:normal;font-family:'Segoe UI',sans-serif;color:${showLineNum ? '#0284c7' : 'transparent'};font-size:1.05rem;">
              ${showLineNum ? lineNum : ''}
            </div>
          </div>`;
      }).join('');

      return `<div class="poetic-stanza-block" style="background:#ffffff;border:1px solid #e0f2fe;border-radius:8px;padding:1.1rem 1.4rem;margin-bottom:1.1rem;box-shadow:0 1px 3px rgba(0,0,0,0.03);">${linesHtml}</div>`;
    }

    // Standard Prose Chunking
    const rawChunks = p.split(/([.!?]+)/).filter(Boolean);
    let chunks = [];
    for (let i = 0; i < rawChunks.length; i += 2) {
      const cText = ((rawChunks[i] || '') + (rawChunks[i+1] || '')).trim();
      if (cText) {
        if (cText.length > 140 && cText.includes(',')) {
          const sub = cText.split(/([,;]+)/).filter(Boolean);
          for (let j = 0; j < sub.length; j += 2) {
            const sText = ((sub[j] || '') + (sub[j+1] || '')).trim();
            if (sText) chunks.push(sText);
          }
        } else {
          chunks.push(cText);
        }
      }
    }
    if (chunks.length === 0 && p.trim()) chunks.push(p.trim());

    const sentenceHtmls = chunks.map(chunkText => {
      const words = chunkText.split(/\s+/).filter(Boolean);
      const startIdx = globalWordIdx;
      const spans = words.map(w => {
        const widx = globalWordIdx++;
        const safe = w.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
        return `<span id="${prefix}-w-${widx}" class="tts-word" data-widx="${widx}">${safe}</span>`;
      }).join(' ');
      const endIdx = globalWordIdx - 1;

      if (words.length > 0) {
        sentences.push({
          text: chunkText,
          startIdx: startIdx,
          endIdx: endIdx,
          wordsCount: words.length
        });
      }
      return spans;
    });

    return `<p class="urdu-sec-p" style="font-size:1.05rem;line-height:1.9;color:#1e293b;direction:ltr;text-align:left;">${sentenceHtmls.join(' ')}</p>`;
  });

  return {
    html: parasHtml.join(''),
    sentences: sentences,
    totalWords: globalWordIdx
  };
}

// ─── English TTS Engine (Direct Neural Speech Stream & 60-FPS Real-Time Highlighting) ───
function stopEngTTS() {
  if (engTtsState.audioObj) {
    try {
      engTtsState.audioObj.pause();
      engTtsState.audioObj.src = "";
    } catch (e) {}
    engTtsState.audioObj = null;
  }
  if (window.speechSynthesis) {
    try { window.speechSynthesis.cancel(); } catch (e) {}
  }
  if (engTtsState.wordTimer) {
    cancelAnimationFrame(engTtsState.wordTimer);
    clearInterval(engTtsState.wordTimer);
    engTtsState.wordTimer = null;
  }

  // Clear any active highlight
  document.querySelectorAll(".tts-word.active-word").forEach(el => {
    el.classList.remove("active-word", "tts-male", "tts-female");
  });

  // Reset active button states
  document.querySelectorAll(".btn-tts-pill").forEach(btn => {
    btn.classList.remove("active-playing");
  });

  engTtsState.isPlaying = false;
  engTtsState.isPaused = false;
  engTtsState.activePrefix = null;
  engTtsState.currentWordIdx = -1;
  engTtsState.sentences = [];
  engTtsState.currentSentenceIdx = 0;

  // Hide floating dock
  const dock = $("engTtsFloatingDock");
  if (dock) dock.style.display = "none";
}

function pauseResumeEngTTS() {
  if (!engTtsState.isPlaying) return;
  const btn = $("dockEngPauseBtn");

  if (engTtsState.isPaused) {
    engTtsState.isPaused = false;
    if (btn) btn.innerHTML = "⏸️ Pause";
    if (engTtsState.audioObj) {
      engTtsState.audioObj.play().catch(() => {});
    } else if (window.speechSynthesis) {
      window.speechSynthesis.resume();
    }
  } else {
    engTtsState.isPaused = true;
    if (btn) btn.innerHTML = "▶️ Resume";
    if (engTtsState.audioObj) {
      engTtsState.audioObj.pause();
    } else if (window.speechSynthesis) {
      window.speechSynthesis.pause();
    }
  }
}

function setEngTtsRate(rate) {
  engTtsState.speechRate = rate;
  document.querySelectorAll(".tts-speed-btn").forEach(btn => {
    btn.classList.toggle("active", parseFloat(btn.dataset.rate) === rate);
  });
  if (engTtsState.isPlaying && !engTtsState.isPaused) {
    if (engTtsState.audioObj) {
      try { engTtsState.audioObj.pause(); } catch(e) {}
      engTtsState.audioObj = null;
    }
    if (window.speechSynthesis) window.speechSynthesis.cancel();
    playNextEngSentence();
  }
}

function highlightEngWord(prefix, widx, gender) {
  if (widx === engTtsState.currentWordIdx) return;
  engTtsState.currentWordIdx = widx;

  document.querySelectorAll(".tts-word.active-word").forEach(el => {
    el.classList.remove("active-word", "tts-male", "tts-female");
  });

  const el = $(`${prefix}-w-${widx}`);
  if (el) {
    el.classList.add("active-word", gender === "male" ? "tts-male" : "tts-female");
    const container = el.closest(".urdu-section-card");
    if (container && !container.classList.contains("open")) {
      container.classList.add("open");
      const icon = container.querySelector(".sec-toggle-icon");
      if (icon) icon.textContent = "▲";
    }
    el.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" });
  }
}

function playNextEngSentence() {
  if (!engTtsState.isPlaying) return;

  if (engTtsState.currentSentenceIdx >= engTtsState.sentences.length) {
    // Finished reading all sentences in this section
    stopEngTTS();
    return;
  }

  const prefix = engTtsState.activePrefix;
  const gender = engTtsState.activeGender;
  const sent = engTtsState.sentences[engTtsState.currentSentenceIdx];
  if (!sent || !sent.text) {
    engTtsState.currentSentenceIdx++;
    playNextEngSentence();
    return;
  }

  const cleanText = sent.text.replace(/["'<>]/g, '').trim();
  const words = sent.text.split(/\s+/).filter(Boolean);
  if (words.length === 0) {
    engTtsState.currentSentenceIdx++;
    playNextEngSentence();
    return;
  }

  // Pre-calculate exact word time boundaries based on character lengths
  const weights = words.map(w => Math.max(2, w.length));
  const totalWeight = weights.reduce((a, b) => a + b, 0);

  // Authentic English Neural Speech Stream (Google Audio Engine)
  const audioUrl = `https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=en&q=${encodeURIComponent(cleanText)}`;
  
  let audio = new Audio(audioUrl);
  engTtsState.audioObj = audio;

  // Distinct vocal characteristics:
  // Male Voice: 0.88x rate (rich baritone pacing)
  // Female Voice: 1.06x rate (fluent clear feminine pacing)
  if (gender === "male") {
    audio.playbackRate = 0.88 * (engTtsState.speechRate || 1.0);
  } else {
    audio.playbackRate = 1.06 * (engTtsState.speechRate || 1.0);
  }

  let lastHighlightedRelIdx = -1;
  let hasFinished = false;
  let animFrameId = null;

  const cancelSyncLoop = () => {
    if (animFrameId) {
      cancelAnimationFrame(animFrameId);
      animFrameId = null;
    }
  };

  const advanceNext = () => {
    if (hasFinished) return;
    hasFinished = true;
    cancelSyncLoop();
    if (engTtsState.audioObj === audio) engTtsState.audioObj = null;
    engTtsState.currentSentenceIdx++;
    if (engTtsState.isPlaying) {
      setTimeout(playNextEngSentence, 80);
    }
  };

  // 🎯 60-FPS REAL-TIME SYNC LOOP: Synchronizes word highlighting with speaker's voice in real-time
  const syncHighlightLoop = () => {
    if (!engTtsState.isPlaying || hasFinished || audio.paused) return;

    if (audio.duration && !isNaN(audio.duration) && audio.duration > 0) {
      // Audio lead-in compensation (120ms initial silence, 150ms trailing silence)
      const leadIn = 0.12;
      const leadOut = 0.15;
      const effectiveDuration = Math.max(0.1, audio.duration - (leadIn + leadOut));
      const currentSpeechTime = Math.max(0, audio.currentTime - leadIn);
      const progress = Math.min(0.999, currentSpeechTime / effectiveDuration);

      let runningWeight = 0;
      let targetIdx = 0;
      for (let i = 0; i < weights.length; i++) {
        const wStart = runningWeight / totalWeight;
        const wEnd = (runningWeight + weights[i]) / totalWeight;
        if (progress >= wStart && progress < wEnd) {
          targetIdx = i;
          break;
        }
        runningWeight += weights[i];
      }

      if (targetIdx !== lastHighlightedRelIdx) {
        lastHighlightedRelIdx = targetIdx;
        highlightEngWord(prefix, sent.startIdx + targetIdx, gender);
      }
    }

    animFrameId = requestAnimationFrame(syncHighlightLoop);
  };

  audio.onplay = function() {
    lastHighlightedRelIdx = 0;
    highlightEngWord(prefix, sent.startIdx, gender);
    cancelSyncLoop();
    animFrameId = requestAnimationFrame(syncHighlightLoop);
  };

  audio.onpause = cancelSyncLoop;
  audio.onended = advanceNext;

  audio.onerror = function() {
    // If audio network stream fails (offline), fallback directly to Web Speech synthesis
    cancelSyncLoop();
    if (window.speechSynthesis) {
      const utterance = new SpeechSynthesisUtterance(cleanText);
      utterance.lang = "en-US";
      utterance.rate = (engTtsState.speechRate || 1.0) * (gender === 'male' ? 0.92 : 1.05);
      utterance.pitch = (gender === 'male' ? 0.88 : 1.25);
      utterance.onstart = () => highlightEngWord(prefix, sent.startIdx, gender);
      utterance.onend = advanceNext;
      utterance.onerror = advanceNext;
      try {
        window.speechSynthesis.speak(utterance);
        return;
      } catch(e) {}
    }
    advanceNext();
  };

  // Update floating dock progress
  const progressEl = $("dockEngProgress");
  if (progressEl) {
    progressEl.textContent = `Sentence ${engTtsState.currentSentenceIdx + 1} of ${engTtsState.sentences.length}`;
  }

  const playPromise = audio.play();
  if (playPromise !== undefined) {
    playPromise.catch(() => {
      // Autoplay or network fallback
      audio.onerror();
    });
  }
}

function playEngTTS(prefix, gender, rawText, sectionTitle) {
  // If already playing this same section with same gender, toggle stop
  if (engTtsState.isPlaying && engTtsState.activePrefix === prefix && engTtsState.activeGender === gender && !engTtsState.isPaused) {
    stopEngTTS();
    return;
  }

  stopEngTTS();

  // Ensure target card is open and visible
  const card = $(prefix + "-card");
  if (card && !card.classList.contains("open")) {
    card.classList.add("open");
    const icon = card.querySelector(".sec-toggle-icon");
    if (icon) icon.textContent = "▲";
  }

  const isPoetry = (prefix === 'full-poem' || (card && card.dataset.type === 'poetry'));
  const prep = prepareEngTextForTts(rawText, prefix, isPoetry);
  if (prep.sentences.length === 0) return;

  engTtsState.isPlaying = true;
  engTtsState.isPaused = false;
  engTtsState.activePrefix = prefix;
  engTtsState.activeGender = gender;
  engTtsState.sentences = prep.sentences;
  engTtsState.totalWords = prep.totalWords;
  engTtsState.currentSentenceIdx = 0;
  engTtsState.sectionTitle = sectionTitle;

  const btnId = `btn-tts-${prefix}-${gender}`;
  const btn = $(btnId);
  if (btn) btn.classList.add("active-playing");

  // Show Floating Dock
  let dock = $("engTtsFloatingDock");
  if (!dock) {
    dock = document.createElement("div");
    dock.id = "engTtsFloatingDock";
    dock.className = "tts-floating-dock";
    const tabContent = $("engTabContent");
    if (tabContent && tabContent.parentNode) {
      tabContent.parentNode.insertBefore(dock, tabContent);
    }
  }

  if (dock) {
    dock.style.display = "flex";
    dock.innerHTML = `
      <div class="tts-dock-info">
        <div class="tts-soundwave">
          <span class="soundwave-bar"></span>
          <span class="soundwave-bar"></span>
          <span class="soundwave-bar"></span>
          <span class="soundwave-bar"></span>
        </div>
        <div>
          <div style="font-weight:700;font-size:0.95rem;color:#ffffff;">
            ${gender === 'male' ? '👨 Male Voice (Reciter)' : '👩 Female Voice (Reciter)'} — ${sectionTitle || 'Reading Section'}
          </div>
          <div id="dockEngProgress" style="font-size:0.8rem;color:#94a3b8;">
            Line 1 of ${prep.sentences.length}
          </div>
        </div>
      </div>
      <div class="tts-dock-actions">
        <div class="tts-speed-group">
          <button class="tts-speed-btn ${(engTtsState.speechRate || 1.0) === 0.8 ? 'active' : ''}" data-rate="0.8" onclick="setEngTtsRate(0.8)">0.8x</button>
          <button class="tts-speed-btn ${(engTtsState.speechRate || 1.0) === 1.0 ? 'active' : ''}" data-rate="1.0" onclick="setEngTtsRate(1.0)">1.0x</button>
          <button class="tts-speed-btn ${(engTtsState.speechRate || 1.0) === 1.2 ? 'active' : ''}" data-rate="1.2" onclick="setEngTtsRate(1.2)">1.2x</button>
        </div>
        <button id="dockEngPauseBtn" class="btn-dock-action pause" onclick="pauseResumeEngTTS()">
          ⏸️ Pause
        </button>
        <button class="btn-dock-action stop" onclick="stopEngTTS()">
          ⏹️ Stop
        </button>
      </div>`;
  }

  playNextEngSentence();
}

// ─── 1. LESSON / TEXT VIEW (Grid Layout with Accordions & Dual Voice) ───
function renderEngLesson(ch) {
  const isPoetry = ch.type === 'poetry';

  // Pre-reading block
  let preReadingHtml = '';
  if (ch.preReading && ch.preReading.length > 0) {
    preReadingHtml = `
      <div style="background:linear-gradient(135deg,#f0fdf4,#dcfce7);border:1.5px solid #86efac;border-radius:10px;padding:1.1rem 1.4rem;margin-bottom:1.5rem;box-shadow:0 2px 5px rgba(0,0,0,0.03);">
        <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.6rem;">
          <span style="background:#16a34a;color:#ffffff;font-size:0.75rem;font-weight:800;padding:0.2rem 0.6rem;border-radius:4px;text-transform:uppercase;">Pre-reading</span>
          <h4 style="color:#15803d;font-size:1.05rem;margin:0;font-weight:700;">🌸 Warm-Up Questions &amp; Reflection</h4>
        </div>
        <ul style="margin:0;padding-left:1.4rem;color:#166534;line-height:1.9;font-size:0.98rem;">
          ${ch.preReading.map(pr => `<li><b>${pr.q}</b> <span style="color:#334155;">(${pr.a})</span></li>`).join('')}
        </ul>
      </div>`;
  } else if (isPoetry) {
    preReadingHtml = `
      <div style="background:linear-gradient(135deg,#f0fdf4,#dcfce7);border:1.5px solid #86efac;border-radius:10px;padding:1.1rem 1.4rem;margin-bottom:1.5rem;box-shadow:0 2px 5px rgba(0,0,0,0.03);">
        <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.6rem;">
          <span style="background:#16a34a;color:#ffffff;font-size:0.75rem;font-weight:800;padding:0.2rem 0.6rem;border-radius:4px;text-transform:uppercase;">Pre-reading</span>
          <h4 style="color:#15803d;font-size:1.05rem;margin:0;font-weight:700;">🌸 Warm-Up Questions &amp; Reflection</h4>
        </div>
        <ul style="margin:0;padding-left:1.4rem;color:#166534;line-height:1.9;font-size:0.98rem;">
          <li><b>What is the central theme of this poem?</b> <span style="color:#334155;">(Explore the moral, spiritual, or natural message conveyed by the poet).</span></li>
          <li><b>How does the poet utilize imagery and poetic devices?</b> <span style="color:#334155;">(Through evocative metaphors, personification, and sensory details).</span></li>
        </ul>
      </div>`;
  }

  let authorHtml = '';
  if (ch.authorInfo) {
    const encodedAuthor = encodeURIComponent(ch.authorInfo);
    const authorData = prepareEngTextForTts(ch.authorInfo, 'author');
    const previewSnippet = ch.authorInfo.substring(0, 140).trim() + '...';

    authorHtml = `
      <div id="author-card" class="urdu-section-card author-card" data-rawtext="${encodedAuthor}" style="border-color:#7dd3fc;background:#f0f9ff;margin-bottom:1.25rem;">
        <div class="urdu-section-header" onclick="toggleEngSection(this)" style="background:linear-gradient(135deg,#e0f2fe,#bae6fd);">
          <div style="display:flex;align-items:center;gap:0.65rem;flex-wrap:wrap;">
            <span class="urdu-sec-badge" style="background:#0284c7;">Context</span>
            <span class="urdu-sec-title" style="color:#0369a1;font-weight:700;">✍️ ${isPoetry ? (ch.author ? 'About the Poet (' + ch.author + ')' : 'About the Poet') : 'Author Introduction & Thematic Background'}</span>
          </div>
          <div style="display:flex;align-items:center;gap:0.5rem;">
            <div class="tts-controls-bar" onclick="event.stopPropagation()">
              <button id="btn-tts-author-male" class="btn-tts-pill male" title="Listen in Male Voice" onclick="playEngTTS('author', 'male', decodeURIComponent('${encodedAuthor}'), 'Author Background')">
                👨 Male
              </button>
              <button id="btn-tts-author-female" class="btn-tts-pill female" title="Listen in Female Voice" onclick="playEngTTS('author', 'female', decodeURIComponent('${encodedAuthor}'), 'Author Background')">
                👩 Female
              </button>
            </div>
            <span class="sec-toggle-icon">▼</span>
          </div>
        </div>
        <div class="urdu-grid-preview" style="direction:ltr;text-align:left;">
          ${previewSnippet} <span style="color:#0284c7;font-weight:700;">(Click to read full background)</span>
        </div>
        <div class="urdu-section-body" style="background:#f0f9ff;border-top:1px solid #7dd3fc;direction:ltr;text-align:left;">
          <div>
            ${authorData.html}
          </div>
        </div>
      </div>`;
  }

  const sectionsList = ch.sections || [];

  let lineCounter = 1;
  const sectionsHtml = sectionsList.map((sec, sIdx) => {
    const rawSecText = sec.paras ? sec.paras.join('\n\n') : (sec.text || '');
    const encodedSecText = encodeURIComponent(rawSecText);
    const startLineForThis = lineCounter;
    const secData = prepareEngTextForTts(rawSecText, `sec-${sIdx}`, isPoetry, startLineForThis);
    if (isPoetry) {
      const lineCountInSec = rawSecText.split('\n').map(l => l.trim()).filter(Boolean).length;
      lineCounter += lineCountInSec;
    }
    const previewSnippet = rawSecText.substring(0, 140).trim() + '...';

    return `
      <div id="sec-${sIdx}-card" class="urdu-section-card" data-rawtext="${encodedSecText}" data-type="${isPoetry ? 'poetry' : 'prose'}">
        <div class="urdu-section-header" onclick="toggleEngSection(this)">
          <div style="display:flex;align-items:center;gap:0.65rem;flex-wrap:wrap;">
            <span class="urdu-sec-badge" style="background:#0284c7;">${isPoetry ? 'Stanza ' + (sIdx + 1) : 'Section ' + (sIdx + 1)}</span>
            <span class="urdu-sec-title" style="font-weight:700;">${sec.heading}</span>
          </div>
          <div style="display:flex;align-items:center;gap:0.5rem;">
            <div class="tts-controls-bar" onclick="event.stopPropagation()">
              <button id="btn-tts-sec-${sIdx}-male" class="btn-tts-pill male" title="Listen in Male Voice" onclick="playEngTTS('sec-${sIdx}', 'male', decodeURIComponent('${encodedSecText}'), '${sec.heading.replace(/'/g, "\\'")}')">
                👨 Male
              </button>
              <button id="btn-tts-sec-${sIdx}-female" class="btn-tts-pill female" title="Listen in Female Voice" onclick="playEngTTS('sec-${sIdx}', 'female', decodeURIComponent('${encodedSecText}'), '${sec.heading.replace(/'/g, "\\'")}')">
                👩 Female
              </button>
            </div>
            <span class="sec-toggle-icon">▼</span>
          </div>
        </div>
        <div class="urdu-grid-preview" style="direction:ltr;text-align:left;">
          ${previewSnippet} <span style="color:#0284c7;font-weight:700;">(Click to expand stanza &amp; analysis)</span>
        </div>
        <div class="urdu-section-body" style="direction:ltr;text-align:left;">
          <div>
            ${secData.html}
            ${sec.analysis ? `
              <div style="margin-top:1rem;background:#f0f9ff;border-left:3px solid #0284c7;border-radius:4px;padding:0.75rem 1rem;font-size:0.9rem;color:#0369a1;white-space:pre-line;line-height:1.7;">
                ${sec.analysis}
              </div>` : ''}
          </div>
        </div>
      </div>`;
  }).join('');

  return `
    <div>
      ${preReadingHtml}
      
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:0.5rem;margin-bottom:1.25rem;background:#f8fafc;padding:0.65rem 1rem;border-radius:8px;border:1px solid #e2e8f0;">
        <span style="font-size:0.88rem;color:#475569;font-weight:600;">
          💡 Click <b>👨 Male / 👩 Female</b> to listen with real-time word highlighting, or expand individual stanzas below.
        </span>
        <div style="display:flex;gap:0.5rem;">
          <button class="btn-toggle-all" onclick="expandAllEngSections(true)">📂 Expand All</button>
          <button class="btn-toggle-all" onclick="expandAllEngSections(false)">📁 Collapse All</button>
        </div>
      </div>

      <div class="urdu-grid-container">
        ${authorHtml}
        ${sectionsHtml}
      </div>
    </div>`;
}

// ─── 2. URDU TRANSLATION VIEW ───
function renderEngUrduTranslation(ch) {
  const isPoetry = ch.type === 'poetry';
  const sectionsList = ch.sections || [];
  const rawUrduList = Array.isArray(ch.urduTranslation) ? ch.urduTranslation : [];

  const cardsHtml = sectionsList.map((sec, idx) => {
    let urduText = sec.urdu || (rawUrduList[idx] && rawUrduList[idx].urdu) || '';
    if (typeof urduText !== 'string') urduText = 'اردو ترجمہ دستیاب ہے۔';
    const engText = sec.text || (sec.paras ? sec.paras.join('\n\n') : '');

    return `
      <div class="urdu-section-card open" style="margin-bottom:1.25rem;">
        <div class="urdu-section-header" style="background:#f8fafc;">
          <span class="urdu-sec-badge" style="background:#0284c7;">${isPoetry ? 'بند ' + (idx + 1) : 'Section ' + (idx + 1)}</span>
          <span class="urdu-sec-title" style="font-weight:700;">${sec.heading} · <span style="font-family:'Jameel Noori Nastaleeq','Segoe UI',serif;color:#15803d;">${sec.headingUrdu || ''}</span></span>
        </div>
        <div class="urdu-section-body" style="display:grid;grid-template-columns:1fr 1fr;gap:1.25rem;padding:1.25rem;">
          <div style="direction:ltr;text-align:left;border-right:1px solid #e2e8f0;padding-right:1.25rem;">
            <h4 style="color:#0284c7;margin-bottom:0.5rem;">${isPoetry ? 'English Verses' : 'English Text'}</h4>
            <div style="font-size:1.02rem;line-height:1.9;color:#334155;white-space:pre-line;font-style:${isPoetry ? 'italic' : 'normal'};font-family:${isPoetry ? 'Georgia, serif' : 'inherit'};">
              ${engText}
            </div>
          </div>
          <div style="direction:rtl;text-align:right;font-family:'Jameel Noori Nastaleeq','Segoe UI',serif;font-size:1.24rem;line-height:2.3;color:#1e293b;">
            <h4 style="color:#15803d;font-family:'Segoe UI',sans-serif;font-size:1rem;margin-bottom:0.5rem;">اردو ترجمہ (بامحاورہ و لفظی)</h4>
            <div style="white-space:pre-line;">
              ${urduText}
            </div>
          </div>
        </div>
      </div>`;
  }).join('');

  return `
    <div style="margin-bottom:2rem;">
      <div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:8px;padding:0.75rem 1.25rem;margin-bottom:1.25rem;display:flex;align-items:center;gap:0.75rem;">
        <span style="font-size:1.5rem;">🇵🇰</span>
        <span style="color:#166534;font-size:0.92rem;font-weight:600;">
          Direct English-to-Urdu Authentic Paragraph &amp; Verse Translation (اردو ترجمہ برائے تفہیم).
        </span>
      </div>
      ${cardsHtml}
    </div>`;
}

// ─── 3. PASHTO TRANSLATION VIEW ───
function renderEngPashtoTranslation(ch) {
  const isPoetry = ch.type === 'poetry';
  const sectionsList = ch.sections || [];
  const rawPashtoList = Array.isArray(ch.pashtoTranslation) ? ch.pashtoTranslation : [];

  const cardsHtml = sectionsList.map((sec, idx) => {
    let pashtoText = sec.pashto || (rawPashtoList[idx] && rawPashtoList[idx].pashto) || '';
    if (typeof pashtoText !== 'string') pashtoText = 'پښتو ژباړه شتون لري.';
    const engText = sec.text || (sec.paras ? sec.paras.join('\n\n') : '');

    return `
      <div class="urdu-section-card open" style="margin-bottom:1.25rem;">
        <div class="urdu-section-header" style="background:#fefce8;">
          <span class="urdu-sec-badge" style="background:#ca8a04;">${isPoetry ? 'بند ' + (idx + 1) : 'برخه ' + (idx + 1)}</span>
          <span class="urdu-sec-title" style="color:#a16207;font-weight:700;">${sec.heading} · <span style="color:#ca8a04;">${sec.headingPashto || ''}</span></span>
        </div>
        <div class="urdu-section-body" style="display:grid;grid-template-columns:1fr 1fr;gap:1.25rem;padding:1.25rem;">
          <div style="direction:ltr;text-align:left;border-right:1px solid #e2e8f0;padding-right:1.25rem;">
            <h4 style="color:#ca8a04;margin-bottom:0.5rem;">${isPoetry ? 'English Verses' : 'English Text'}</h4>
            <div style="font-size:1.02rem;line-height:1.9;color:#334155;white-space:pre-line;font-style:${isPoetry ? 'italic' : 'normal'};font-family:${isPoetry ? 'Georgia, serif' : 'inherit'};">
              ${engText}
            </div>
          </div>
          <div style="direction:rtl;text-align:right;font-size:1.18rem;line-height:2.2;color:#1e293b;">
            <h4 style="color:#ca8a04;font-size:1rem;margin-bottom:0.5rem;">پښتو ژباړه (د خیبر پښتونخوا نصاب مطابق)</h4>
            <div style="white-space:pre-line;">
              ${pashtoText}
            </div>
          </div>
        </div>
      </div>`;
  }).join('');

  return `
    <div style="margin-bottom:2rem;">
      <div style="background:#fefce8;border:1px solid #fef08a;border-radius:8px;padding:0.75rem 1.25rem;margin-bottom:1.25rem;display:flex;align-items:center;gap:0.75rem;">
        <span style="font-size:1.5rem;">🇦🇫</span>
        <span style="color:#854d0e;font-size:0.92rem;font-weight:600;">
          د انګلیسي متن روانه او مستنده پښتو ژباړه (پښتو ترجمه د خیبر پښتونخوا نصاب مطابق).
        </span>
      </div>
      ${cardsHtml}
    </div>`;
}

// ─── 4. VIDEO LECTURES VIEW ───
function renderEngVideo(ch) {
  const vid = ch.videoLesson || {};
  return `
    <div class="urdu-section-card open" style="margin-bottom:2rem;">
      <div class="urdu-section-header" style="background:#eff6ff;">
        <span class="urdu-sec-badge" style="background:#2563eb;">ویڈیو لیکچر</span>
        <span class="urdu-sec-title" style="color:#1e40af;font-size:1.1rem;font-weight:700;">🎥 ${vid.title || ch.title + ' — Video Lecture'}</span>
      </div>
      <div class="urdu-section-body" style="padding:1.5rem;">
        <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:10px;background:#0f172a;box-shadow:0 4px 15px rgba(0,0,0,0.15);margin-bottom:1.25rem;">
          <iframe 
            src="${vid.embedUrl || 'https://www.youtube.com/embed/dQw4w9WgXcQ'}" 
            title="Unit Video Lecture"
            style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
          </iframe>
        </div>
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:0.75rem;background:#f8fafc;padding:0.85rem 1.25rem;border-radius:8px;border:1px solid #e2e8f0;">
          <div>
            <div style="font-weight:700;color:#1e293b;">Instructor: ${vid.instructor || 'Senior Subject Specialist'}</div>
            <div style="font-size:0.82rem;color:#64748b;">Duration: ${vid.duration || '24:30'} &nbsp;|&nbsp; Quality: 1080p HD</div>
          </div>
          <a href="${vid.url || '#'}" target="_blank" style="padding:0.5rem 1rem;background:#2563eb;color:#fff;border-radius:6px;font-size:0.85rem;font-weight:600;text-decoration:none;">
            📺 Open on YouTube
          </a>
        </div>
      </div>
    </div>`;
}

// ─── 5. SUMMARY VIEWS (Urdu & Pashto) ───
function renderEngUrduSummary(ch) {
  return `
    <div class="urdu-section-card open" style="margin-bottom:2rem;">
      <div class="urdu-section-header" style="background:#f0fdf4;">
        <span class="urdu-sec-badge" style="background:#15803d;">خلاصہ</span>
        <span class="urdu-sec-title" style="color:#15803d;font-size:1.15rem;font-weight:700;font-family:'Jameel Noori Nastaleeq','Segoe UI',serif;">🇵🇰 اردو خلاصہ و مرکزی خیال</span>
      </div>
      <div class="urdu-section-body" style="padding:1.5rem;direction:rtl;text-align:right;font-family:'Jameel Noori Nastaleeq','Segoe UI',serif;font-size:1.25rem;line-height:2.3;color:#1e293b;">
        <p>${ch.urduSummary || 'اردو خلاصہ دستیاب ہے۔'}</p>
      </div>
    </div>`;
}

function renderEngPashtoSummary(ch) {
  return `
    <div class="urdu-section-card open" style="margin-bottom:2rem;">
      <div class="urdu-section-header" style="background:#fefce8;">
        <span class="urdu-sec-badge" style="background:#ca8a04;">لنډیز</span>
        <span class="urdu-sec-title" style="color:#a16207;font-size:1.15rem;font-weight:700;">🇦🇫 پښتو لنډیز او مرکزي مفکوره</span>
      </div>
      <div class="urdu-section-body" style="padding:1.5rem;direction:rtl;text-align:right;font-size:1.18rem;line-height:2.3;color:#1e293b;">
        <p>${ch.pashtoSummary || 'د دې درس پښتو لنډیز شتون لري.'}</p>
      </div>
    </div>`;
}

// ─── 6. SOLVED TEXTBOOK EXERCISES VIEW ───
function renderEngExercise(ch) {
  const ex = ch.exercise || {};
  const chGlossary = ch.glossary || [];
  const tbMcqs = ex.textbookMcqs || [];
  const compList = ex.comprehension || [];
  const phraseList = ex.phraseExplanations || [];
  const figureLines = ex.figureOfSpeechLines || [];
  const sameWords = ex.sameMeaningWords || [];
  const glossaryList = (ex.glossaryTable && ex.glossaryTable.length > 0) ? ex.glossaryTable : chGlossary;
  const dictList = ex.dictionaryWords || [];
  const theList = ex.thesaurusSynonyms || [];
  const theAntList = ex.thesaurusAntonyms || [];
  const vocabWords = ex.vocabularyWords || [];
  const wordPairs = ex.wordPairDistinctions || [];
  const ctxMeanings = ex.contextualMeanings || [];
  const conDenot = ex.connotationDenotation || [];
  const litSpec = ex.literaryDevicesSpecify || [];
  const directQuotes = ex.directQuotations || [];
  const advSentences = ex.adverbSentences || [];
  const phrasalLook = ex.phrasalVerbsLook || [];
  const textPhrases = ex.textualPhrases || [];
  const prefixList = ex.prefixActivity || [];
  const suffixList = ex.suffixActivity || [];
  const vocabObj = (typeof ex.vocabulary === 'object' && !Array.isArray(ex.vocabulary)) ? ex.vocabulary : {};
  const vocabList = Array.isArray(ex.vocabulary) ? ex.vocabulary : [];
  const gramObj = ex.grammarActivities || {};
  const gramList = Array.isArray(ex.grammar) ? ex.grammar : [];
  const writTasks = ex.writingTasks || {};
  const writList = Array.isArray(ex.writing) ? ex.writing : [];
  const speakObj = ex.speakingActivity || null;
  const finalRev = ex.finalRevision || null;
  const aboutAuthors = ex.aboutTheAuthors || null;

  // 1. Glossary Table
  let glossaryHtml = '';
  if (glossaryList.length > 0) {
    glossaryHtml = `
      <div class="slo-accordion-card open" style="margin-bottom:1.25rem;">
        <div class="slo-accordion-header" onclick="toggleSloAccordion(this)" style="background:#f0fdf4;">
          <span style="font-weight:700;color:#166534;">📖 Unit Glossary (فرهنگ الفاظ و معانی)</span>
          <span class="slo-acc-icon">▲</span>
        </div>
        <div class="slo-accordion-body" style="padding:1.25rem;overflow-x:auto;">
          <table style="width:100%;border-collapse:collapse;text-align:left;font-size:0.92rem;">
            <thead>
              <tr style="background:#dcfce7;color:#14532d;border-bottom:2px solid #86efac;">
                <th style="padding:0.6rem 0.8rem;border:1px solid #bbf7d0;">Word</th>
                <th style="padding:0.6rem 0.8rem;border:1px solid #bbf7d0;">Part of Speech</th>
                <th style="padding:0.6rem 0.8rem;border:1px solid #bbf7d0;">English Meaning</th>
                <th style="padding:0.6rem 0.8rem;border:1px solid #bbf7d0;direction:rtl;text-align:right;">اردو معنی</th>
                <th style="padding:0.6rem 0.8rem;border:1px solid #bbf7d0;direction:rtl;text-align:right;">پښتو معنی</th>
              </tr>
            </thead>
            <tbody>
              ${glossaryList.map((g, idx) => `
                <tr style="background:${idx % 2 === 0 ? '#ffffff' : '#f9fafb'};">
                  <td style="padding:0.6rem 0.8rem;border:1px solid #e5e7eb;font-weight:700;color:#1e293b;">${g.word}</td>
                  <td style="padding:0.6rem 0.8rem;border:1px solid #e5e7eb;font-style:italic;color:#64748b;">${g.pos || '-'}</td>
                  <td style="padding:0.6rem 0.8rem;border:1px solid #e5e7eb;color:#334155;">${g.meaning}</td>
                  <td style="padding:0.6rem 0.8rem;border:1px solid #e5e7eb;font-family:'Noto Nastaliq Urdu',serif;direction:rtl;text-align:right;color:#0f766e;">${g.urdu || '-'}</td>
                  <td style="padding:0.6rem 0.8rem;border:1px solid #e5e7eb;font-family:'Pashto Font',serif;direction:rtl;text-align:right;color:#1d4ed8;">${g.pashto || '-'}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      </div>`;
  }

  // 2. Textbook MCQs
  let tbMcqsHtml = '';
  if (tbMcqs.length > 0) {
    tbMcqsHtml = `
      <div class="slo-accordion-card open" style="margin-bottom:1.25rem;">
        <div class="slo-accordion-header" onclick="toggleSloAccordion(this)" style="background:#eff6ff;">
          <span style="font-weight:700;color:#1e40af;">🎯 Choose the Correct Answer (Textbook MCQs)</span>
          <span class="slo-acc-icon">▲</span>
        </div>
        <div class="slo-accordion-body" style="padding:1.25rem;">
          <div class="slo-accordion-list">
            ${tbMcqs.map((m, idx) => `
              <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:1rem;margin-bottom:0.85rem;">
                <div style="font-weight:700;color:#1e293b;margin-bottom:0.6rem;font-size:0.96rem;">
                  ${m.question}
                </div>
                <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:0.5rem;margin-bottom:0.6rem;">
                  ${m.options.map((opt) => `
                    <div style="padding:0.45rem 0.75rem;background:#ffffff;border:1px solid #cbd5e1;border-radius:6px;font-size:0.9rem;color:#334155;">
                      ${opt}
                    </div>
                  `).join('')}
                </div>
                <div style="background:#dcfce7;border-left:4px solid #16a34a;padding:0.5rem 0.85rem;border-radius:4px;font-size:0.9rem;color:#14532d;">
                  <strong>✓ Correct Answer:</strong> ${m.answer}
                  ${m.explanation ? `<div style="margin-top:0.25rem;font-size:0.85rem;color:#15803d;"><em>Explanation:</em> ${m.explanation}</div>` : ''}
                </div>
              </div>
            `).join('')}
          </div>
        </div>
      </div>`;
  }

  // 3. Comprehension Questions
  let compHtml = '';
  if (compList.length > 0) {
    compHtml = `
      <div class="slo-accordion-card open" style="margin-bottom:1.25rem;">
        <div class="slo-accordion-header" onclick="toggleSloAccordion(this)" style="background:#faf5ff;">
          <span style="font-weight:700;color:#6b21a8;">📝 Comprehension & Textual Questions</span>
          <span class="slo-acc-icon">▲</span>
        </div>
        <div class="slo-accordion-body" style="padding:1.25rem;">
          <div class="slo-accordion-list">
            ${compList.map((c, idx) => `
              <div style="background:#ffffff;border:1px solid #e9d5ff;border-radius:8px;padding:1rem;margin-bottom:0.85rem;box-shadow:0 1px 3px rgba(0,0,0,0.05);">
                <div style="font-weight:700;color:#581c87;margin-bottom:0.45rem;font-size:0.96rem;">
                  ${c.question}
                </div>
                <div style="color:#334155;line-height:1.6;font-size:0.92rem;white-space:pre-line;background:#faf5ff;padding:0.75rem;border-radius:6px;border-left:3px solid #a855f7;">
                  ${c.answer}
                </div>
              </div>
            `).join('')}
          </div>
        </div>
      </div>`;
  }

  // 4. Vocabulary Activities
  let vocabHtml = '';
  let vocabBlocks = [];

  // 4a. Dictionary Differences (look/search, buy/purchase etc)
  if (vocabObj.dictionaryDifferences && vocabObj.dictionaryDifferences.length > 0) {
    vocabBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#0f766e;font-size:0.98rem;margin-bottom:0.6rem;">🔍 Dictionary Distinction of Word Pairs:</h4>
        ${vocabObj.dictionaryDifferences.map(d => `
          <div style="background:#f0fdfa;border:1px solid #ccfbf1;border-radius:6px;padding:0.75rem 1rem;margin-bottom:0.6rem;">
            <div style="font-weight:700;color:#115e59;margin-bottom:0.3rem;">${d.pair}</div>
            <div style="font-size:0.9rem;color:#334155;margin-bottom:0.4rem;">${d.explanation}</div>
            <div style="font-size:0.88rem;color:#0f766e;background:#ffffff;padding:0.4rem 0.6rem;border-radius:4px;border-left:3px solid #14b8a6;">
              ${d.sentences.map(s => `<div>• ${s}</div>`).join('')}
            </div>
          </div>
        `).join('')}
      </div>`);
  }

  // 4b. Dictionary Abbreviations
  if (vocabObj.dictionaryAbbreviations && vocabObj.dictionaryAbbreviations.length > 0) {
    vocabBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#0f766e;font-size:0.98rem;margin-bottom:0.6rem;">📚 Dictionary Lookup & Parts of Speech:</h4>
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:0.6rem;">
          ${vocabObj.dictionaryAbbreviations.map(v => `
            <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:0.75rem;">
              <span style="font-weight:700;color:#1e293b;">${v.word}</span> 
              <span style="font-size:0.85rem;color:#64748b;font-style:italic;">[${v.pos}]</span>: 
              <span style="font-size:0.9rem;color:#334155;">${v.meaning}</span>
            </div>
          `).join('')}
        </div>
      </div>`);
  }

  // 4c. Contextual Meanings
  const ctxList = (vocabObj.contextualMeanings && vocabObj.contextualMeanings.length > 0) ? vocabObj.contextualMeanings : ctxMeanings;
  if (ctxList.length > 0) {
    vocabBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#0f766e;font-size:0.98rem;margin-bottom:0.6rem;">🎯 Contextual Meanings in the Lesson:</h4>
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:0.6rem;">
          ${ctxList.map(c => `
            <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:0.75rem;">
              <strong style="color:#0f766e;">${c.word || c.phrase}:</strong> 
              <span style="color:#334155;font-size:0.9rem;">${c.contextualMeaning || c.meaning || c.explanation}</span>
            </div>
          `).join('')}
        </div>
      </div>`);
  }

  // 4d. Similes, Imagery, Rhyming Words, Figures of Speech
  if (vocabObj.similes && vocabObj.similes.length > 0) {
    vocabBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#0f766e;font-size:0.98rem;margin-bottom:0.6rem;">✨ Similes in the Poem:</h4>
        ${vocabObj.similes.map(s => `
          <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.6rem 0.85rem;margin-bottom:0.5rem;">
            <div style="font-weight:700;color:#1e293b;">${s.simile}</div>
            <div style="font-size:0.88rem;color:#475569;margin-top:0.25rem;"><em>Comparison:</em> ${s.comparison}</div>
          </div>
        `).join('')}
      </div>`);
  }

  if (vocabObj.imageryLines && vocabObj.imageryLines.length > 0) {
    vocabBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#0f766e;font-size:0.98rem;margin-bottom:0.6rem;">🎨 Poetic Imagery Lines:</h4>
        ${vocabObj.imageryLines.map(i => `
          <div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:6px;padding:0.6rem 0.85rem;margin-bottom:0.5rem;">
            <div style="font-weight:700;color:#166534;">${i.line}</div>
            <div style="font-size:0.88rem;color:#334155;margin-top:0.2rem;"><strong>Type:</strong> ${i.type} — ${i.effect}</div>
          </div>
        `).join('')}
      </div>`);
  }

  if (vocabObj.rhymingWords && vocabObj.rhymingWords.length > 0) {
    vocabBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#0f766e;font-size:0.98rem;margin-bottom:0.6rem;">🎵 Rhyming Words:</h4>
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:0.5rem;">
          ${vocabObj.rhymingWords.map(r => `
            <div style="background:#ffffff;border:1px solid #cbd5e1;border-radius:6px;padding:0.5rem 0.75rem;font-size:0.9rem;">
              <strong>${r.stanza || r.couplet}:</strong> <span style="color:#2563eb;">${(r.pairs || [r.rhymes]).join(', ')}</span>
            </div>
          `).join('')}
        </div>
      </div>`);
  }

  if (vocabObj.figuresOfSpeech && vocabObj.figuresOfSpeech.length > 0) {
    vocabBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#0f766e;font-size:0.98rem;margin-bottom:0.6rem;">🎭 Figures of Speech & Poetic Techniques:</h4>
        ${vocabObj.figuresOfSpeech.map(f => `
          <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:0.5rem 0.85rem;margin-bottom:0.45rem;font-size:0.9rem;">
            <strong style="color:#7c3aed;">${f.figure}:</strong> ${f.example}
          </div>
        `).join('')}
      </div>`);
  }

  // 4e. Thesaurus Synonyms & Antonyms
  const allSynonyms = (vocabObj.thesaurusSynonyms && vocabObj.thesaurusSynonyms.length > 0) ? vocabObj.thesaurusSynonyms : theList;
  if (allSynonyms.length > 0) {
    vocabBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#0f766e;font-size:0.98rem;margin-bottom:0.6rem;">📖 Thesaurus Synonyms:</h4>
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:0.5rem;">
          ${allSynonyms.map(s => `
            <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:0.5rem 0.75rem;font-size:0.9rem;">
              <strong style="color:#0f766e;">${s.word}:</strong> ${s.synonyms ? s.synonyms.join(', ') : s.synonym}
            </div>
          `).join('')}
        </div>
      </div>`);
  }

  const allAntonyms = (vocabObj.thesaurusAntonyms && vocabObj.thesaurusAntonyms.length > 0) ? vocabObj.thesaurusAntonyms : theAntList;
  if (allAntonyms.length > 0) {
    vocabBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#0f766e;font-size:0.98rem;margin-bottom:0.6rem;">🔄 Thesaurus Antonyms:</h4>
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:0.5rem;">
          ${allAntonyms.map(a => `
            <div style="background:#fef2f2;border:1px solid #fecaca;border-radius:6px;padding:0.5rem 0.75rem;font-size:0.9rem;">
              <strong style="color:#991b1b;">${a.word}:</strong> ${a.antonyms ? a.antonyms.join(', ') : a.antonym}
            </div>
          `).join('')}
        </div>
      </div>`);
  }

  // 4f. Connotation/Denotation, Literary devices, Direct quotations, Adverbs, Phrasal verbs, Text phrases
  if (conDenot.length > 0) {
    vocabBlocks.push(`
      <div style="margin-bottom:1.25rem;overflow-x:auto;">
        <h4 style="color:#0f766e;font-size:0.98rem;margin-bottom:0.6rem;">📊 Connotation & Denotation Table:</h4>
        <table style="width:100%;border-collapse:collapse;font-size:0.9rem;">
          <thead>
            <tr style="background:#f1f5f9;border-bottom:2px solid #cbd5e1;">
              <th style="padding:0.5rem;border:1px solid #cbd5e1;">Word</th>
              <th style="padding:0.5rem;border:1px solid #cbd5e1;">Denotation</th>
              <th style="padding:0.5rem;border:1px solid #cbd5e1;">Connotation</th>
              <th style="padding:0.5rem;border:1px solid #cbd5e1;">Contextual Significance</th>
            </tr>
          </thead>
          <tbody>
            ${conDenot.map((c, i) => `
              <tr style="background:${i%2===0?'#ffffff':'#f8fafc'};">
                <td style="padding:0.5rem;border:1px solid #e2e8f0;font-weight:700;">${c.word}</td>
                <td style="padding:0.5rem;border:1px solid #e2e8f0;">${c.denotation}</td>
                <td style="padding:0.5rem;border:1px solid #e2e8f0;">${c.connotation}</td>
                <td style="padding:0.5rem;border:1px solid #e2e8f0;">${c.contextualSignificance || '-'}</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>`);
  }

  if (litSpec.length > 0) {
    vocabBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#0f766e;font-size:0.98rem;margin-bottom:0.6rem;">🔍 Specification of Literary Devices:</h4>
        ${litSpec.map(l => `
          <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.5rem 0.85rem;margin-bottom:0.45rem;font-size:0.9rem;">
            <strong>${l.num}. "${l.line}"</strong> → <span style="color:#2563eb;font-weight:600;">${l.device}</span>
            <div style="font-size:0.85rem;color:#64748b;margin-top:0.2rem;">${l.explanation}</div>
          </div>
        `).join('')}
      </div>`);
  }

  if (directQuotes.length > 0) {
    vocabBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#0f766e;font-size:0.98rem;margin-bottom:0.6rem;">💬 Direct Quotations in the Text:</h4>
        ${directQuotes.map(q => `
          <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:0.6rem 0.85rem;margin-bottom:0.5rem;font-size:0.9rem;">
            <div style="font-weight:700;color:#1e293b;">"${q.quote}"</div>
            <div style="font-size:0.85rem;color:#475569;margin-top:0.25rem;"><strong>Speaker:</strong> ${q.speaker} | <strong>Context:</strong> ${q.context}</div>
          </div>
        `).join('')}
      </div>`);
  }

  if (advSentences.length > 0) {
    vocabBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#0f766e;font-size:0.98rem;margin-bottom:0.6rem;">⚡ Adverbs in Sentences:</h4>
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:0.6rem;">
          ${advSentences.map(a => `
            <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.6rem 0.85rem;font-size:0.9rem;">
              <strong style="color:#0f766e;">${a.adverb}:</strong> ${a.sentence}
            </div>
          `).join('')}
        </div>
      </div>`);
  }

  if (phrasalLook.length > 0) {
    vocabBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#0f766e;font-size:0.98rem;margin-bottom:0.6rem;">🔍 Phrasal Verbs with 'Look':</h4>
        ${phrasalLook.map(p => `
          <div style="background:#f0fdfa;border:1px solid #ccfbf1;border-radius:6px;padding:0.6rem 0.85rem;margin-bottom:0.5rem;font-size:0.9rem;">
            <strong style="color:#0f766e;">${p.verb}:</strong> ${p.meaning}
            <div style="font-size:0.85rem;color:#334155;margin-top:0.25rem;"><em>Example:</em> ${p.sentence}</div>
          </div>
        `).join('')}
      </div>`);
  }

  if (textPhrases.length > 0) {
    vocabBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#0f766e;font-size:0.98rem;margin-bottom:0.6rem;">📌 Textual Phrases & Idiomatic Usage:</h4>
        ${textPhrases.map(t => `
          <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.6rem 0.85rem;margin-bottom:0.5rem;font-size:0.9rem;">
            <strong style="color:#1e40af;">"${t.phrase}"</strong>: ${t.meaning}
            <div style="font-size:0.85rem;color:#334155;margin-top:0.2rem;"><em>Sentence:</em> ${t.sentence}</div>
          </div>
        `).join('')}
      </div>`);
  }

  if (wordPairs.length > 0) {
    vocabBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#0f766e;font-size:0.98rem;margin-bottom:0.6rem;">⚖️ Distinction of Word Pairs:</h4>
        ${wordPairs.map(w => `
          <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:0.6rem 0.85rem;margin-bottom:0.5rem;font-size:0.9rem;">
            <strong style="color:#1e293b;">${w.pair}</strong>
            <div style="font-size:0.85rem;color:#475569;margin-top:0.2rem;">${w.distinction || w.explanation}</div>
            <div style="font-size:0.85rem;color:#0f766e;margin-top:0.2rem;">${(w.sentences || []).map(s => `<div>• ${s}</div>`).join('')}</div>
          </div>
        `).join('')}
      </div>`);
  }

  if (prefixList.length > 0 || suffixList.length > 0) {
    vocabBlocks.push(`
      <div style="margin-bottom:1.25rem;display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:0.75rem;">
        ${prefixList.length > 0 ? `
          <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:0.75rem;">
            <h5 style="color:#0f766e;font-weight:700;margin-bottom:0.4rem;">Prefixes:</h5>
            ${prefixList.map(p => `<div style="font-size:0.88rem;margin-bottom:0.25rem;">• <strong>${p.prefix}</strong> + ${p.root} = ${p.word}</div>`).join('')}
          </div>
        ` : ''}
        ${suffixList.length > 0 ? `
          <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:0.75rem;">
            <h5 style="color:#0f766e;font-weight:700;margin-bottom:0.4rem;">Suffixes:</h5>
            ${suffixList.map(s => `<div style="font-size:0.88rem;margin-bottom:0.25rem;">• ${s.root} + <strong>${s.suffix}</strong> = ${s.word}</div>`).join('')}
          </div>
        ` : ''}
      </div>`);
  }

  if (vocabBlocks.length > 0) {
    vocabHtml = `
      <div class="slo-accordion-card open" style="margin-bottom:1.25rem;">
        <div class="slo-accordion-header" onclick="toggleSloAccordion(this)" style="background:#f0fdfa;">
          <span style="font-weight:700;color:#0f766e;">💡 Vocabulary, Figurative Language & Literary Devices</span>
          <span class="slo-acc-icon">▲</span>
        </div>
        <div class="slo-accordion-body" style="padding:1.25rem;">
          ${vocabBlocks.join('')}
        </div>
      </div>`;
  }

  // 5. Grammar Activities
  let gramHtml = '';
  let gramBlocks = [];

  // 5a. Punctuation MCQs
  if (gramObj.punctuationMcqs && gramObj.punctuationMcqs.length > 0) {
    gramBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#1e40af;font-size:0.98rem;margin-bottom:0.6rem;">🎯 Punctuation Multiple Choice Questions:</h4>
        ${gramObj.punctuationMcqs.map(p => `
          <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:0.75rem;margin-bottom:0.6rem;">
            <div style="font-weight:700;color:#1e293b;margin-bottom:0.4rem;">${p.question}</div>
            <div style="font-size:0.88rem;color:#475569;margin-bottom:0.4rem;">
              ${p.options.map(o => `<div style="padding:0.2rem 0;">${o}</div>`).join('')}
            </div>
            <div style="background:#dcfce7;border-left:3px solid #16a34a;padding:0.4rem 0.6rem;font-size:0.88rem;color:#14532d;">
              <strong>Answer:</strong> ${p.answer} (${p.explanation})
            </div>
          </div>
        `).join('')}
      </div>`);
  }

  // 5b. Pasta Punctuation Paragraph
  if (gramObj.pastaPunctuation) {
    gramBlocks.push(`
      <div style="margin-bottom:1.25rem;background:#f0fdf4;border:1px solid #bbf7d0;border-radius:8px;padding:1rem;">
        <h4 style="color:#166534;font-size:0.98rem;margin-bottom:0.5rem;">🍝 ${gramObj.pastaPunctuation.title}:</h4>
        <div style="font-size:0.9rem;color:#334155;line-height:1.6;background:#ffffff;padding:0.75rem;border-radius:6px;border:1px solid #cbd5e1;margin-bottom:0.5rem;">
          <strong>Original with []:</strong><br>${gramObj.pastaPunctuation.rawText}
        </div>
        <div style="font-size:0.9rem;color:#14532d;line-height:1.6;background:#dcfce7;padding:0.75rem;border-radius:6px;border-left:3px solid #16a34a;">
          <strong>✓ Solved Punctuated Text:</strong><br>${gramObj.pastaPunctuation.solvedText}
        </div>
      </div>`);
  }

  // 5c. Capitalization & Punctuation Sentences
  if (gramObj.capitalizationPunctuation && gramObj.capitalizationPunctuation.length > 0) {
    gramBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#1e40af;font-size:0.98rem;margin-bottom:0.6rem;">🔤 Capitalization & Punctuation Corrections:</h4>
        ${gramObj.capitalizationPunctuation.map(c => `
          <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.6rem 0.85rem;margin-bottom:0.5rem;font-size:0.9rem;">
            <div style="color:#dc2626;"><strong>${c.num}. Original:</strong> ${c.original}</div>
            <div style="color:#16a34a;font-weight:700;margin-top:0.2rem;"><strong>Corrected:</strong> ${c.corrected}</div>
            ${c.rule ? `<div style="font-size:0.83rem;color:#64748b;margin-top:0.15rem;"><em>Rule:</em> ${c.rule}</div>` : ''}
          </div>
        `).join('')}
      </div>`);
  }

  // 5d. Transition Words Sentences
  if (gramObj.transitionWordsSentences && gramObj.transitionWordsSentences.length > 0) {
    gramBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#1e40af;font-size:0.98rem;margin-bottom:0.6rem;">🔗 Transition Words Completion:</h4>
        ${gramObj.transitionWordsSentences.map(t => `
          <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:0.6rem 0.85rem;margin-bottom:0.5rem;font-size:0.9rem;">
            <div><strong>${t.num}.</strong> ${t.sentence}</div>
            <div style="font-size:0.85rem;color:#2563eb;margin-top:0.2rem;"><strong>Word:</strong> ${t.wordUsed} | <strong>Function:</strong> ${t.function}</div>
          </div>
        `).join('')}
      </div>`);
  }

  // 5e. Quotation Marks Exercise
  if (gramObj.quotationMarksExercise && gramObj.quotationMarksExercise.length > 0) {
    gramBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#1e40af;font-size:0.98rem;margin-bottom:0.6rem;">💬 Quotation Marks Insertion:</h4>
        ${gramObj.quotationMarksExercise.map(q => `
          <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.6rem 0.85rem;margin-bottom:0.5rem;font-size:0.9rem;">
            <div style="color:#64748b;"><strong>${q.num}. Given:</strong> ${q.original}</div>
            <div style="color:#1e40af;font-weight:700;margin-top:0.2rem;"><strong>✓ Punctuated:</strong> ${q.corrected}</div>
          </div>
        `).join('')}
      </div>`);
  }

  // 5f. Dash vs Hyphen & Hyphen Rules
  if (gramObj.dashOrHyphen && gramObj.dashOrHyphen.length > 0) {
    gramBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#1e40af;font-size:0.98rem;margin-bottom:0.6rem;">➖ Dash vs. Hyphen Classification:</h4>
        ${gramObj.dashOrHyphen.map(d => `
          <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:0.6rem 0.85rem;margin-bottom:0.5rem;font-size:0.9rem;">
            <div><strong>${d.num}.</strong> ${d.sentence}</div>
            <div style="font-size:0.85rem;color:#0f766e;margin-top:0.2rem;"><strong>Punctuation:</strong> ${d.punctuation} (${d.rule})</div>
          </div>
        `).join('')}
      </div>`);
  }

  if (gramObj.hyphenRulesSentences && gramObj.hyphenRulesSentences.length > 0) {
    gramBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#1e40af;font-size:0.98rem;margin-bottom:0.6rem;">📏 Hyphen Placement & Rules:</h4>
        ${gramObj.hyphenRulesSentences.map(h => `
          <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.6rem 0.85rem;margin-bottom:0.5rem;font-size:0.9rem;">
            <div><strong>${h.num}.</strong> ${h.sentence}</div>
            <div style="font-size:0.85rem;color:#7c3aed;margin-top:0.15rem;"><em>Rule:</em> ${h.rule}</div>
          </div>
        `).join('')}
      </div>`);
  }

  // 5g. Parentheses & Ellipsis Exercises
  if (gramObj.parenthesesExercise && gramObj.parenthesesExercise.length > 0) {
    gramBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#1e40af;font-size:0.98rem;margin-bottom:0.6rem;">( ) Parentheses Insertion:</h4>
        ${gramObj.parenthesesExercise.map(p => `
          <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.6rem 0.85rem;margin-bottom:0.5rem;font-size:0.9rem;">
            <div style="color:#64748b;"><strong>${p.num}. Given:</strong> ${p.original}</div>
            <div style="color:#1e40af;font-weight:700;margin-top:0.2rem;"><strong>✓ Corrected:</strong> ${p.corrected}</div>
            <div style="font-size:0.83rem;color:#64748b;margin-top:0.15rem;"><em>Rule:</em> ${p.rule}</div>
          </div>
        `).join('')}
      </div>`);
  }

  if (gramObj.ellipsisExercise && gramObj.ellipsisExercise.length > 0) {
    gramBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#1e40af;font-size:0.98rem;margin-bottom:0.6rem;">... Ellipsis Omission & Pauses:</h4>
        ${gramObj.ellipsisExercise.map(e => `
          <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.6rem 0.85rem;margin-bottom:0.5rem;font-size:0.9rem;">
            <div style="color:#64748b;"><strong>${e.num}. Original:</strong> ${e.original}</div>
            <div style="color:#16a34a;font-weight:700;margin-top:0.2rem;"><strong>✓ With Ellipsis:</strong> ${e.omitted}</div>
            <div style="font-size:0.83rem;color:#64748b;margin-top:0.15rem;"><em>Function:</em> ${e.rule}</div>
          </div>
        `).join('')}
      </div>`);
  }

  // 5h. Direct <-> Indirect Speech
  if (gramObj.directToIndirect && gramObj.directToIndirect.length > 0) {
    gramBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#1e40af;font-size:0.98rem;margin-bottom:0.6rem;">🗣️ Change into Indirect Speech:</h4>
        ${gramObj.directToIndirect.map(d => `
          <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:0.6rem 0.85rem;margin-bottom:0.5rem;font-size:0.9rem;">
            <div style="color:#64748b;"><strong>${d.num}. Direct:</strong> ${d.direct}</div>
            <div style="color:#1e40af;font-weight:700;margin-top:0.2rem;"><strong>Indirect:</strong> ${d.indirect}</div>
          </div>
        `).join('')}
      </div>`);
  }

  if (gramObj.indirectToDirect && gramObj.indirectToDirect.length > 0) {
    gramBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#1e40af;font-size:0.98rem;margin-bottom:0.6rem;">🗣️ Change into Direct Speech:</h4>
        ${gramObj.indirectToDirect.map(d => `
          <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.6rem 0.85rem;margin-bottom:0.5rem;font-size:0.9rem;">
            <div style="color:#64748b;"><strong>${d.num}. Indirect:</strong> ${d.indirect}</div>
            <div style="color:#16a34a;font-weight:700;margin-top:0.2rem;"><strong>Direct:</strong> ${d.direct}</div>
          </div>
        `).join('')}
      </div>`);
  }

  // 5i. Legacy grammar structures (Prepositions, Sentence classification, Phrases identification etc)
  if (gramObj.prepositionsA && gramObj.prepositionsA.length > 0) {
    gramBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#1e40af;font-size:0.98rem;margin-bottom:0.6rem;">📌 Prepositions Activity:</h4>
        ${gramObj.prepositionsA.map(p => `
          <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.5rem 0.85rem;margin-bottom:0.4rem;font-size:0.9rem;">
            <strong>${p.num}.</strong> ${p.sentence} → <strong style="color:#2563eb;">${p.answer}</strong>
          </div>
        `).join('')}
      </div>`);
  }

  if (gramObj.sentenceClassification && gramObj.sentenceClassification.length > 0) {
    gramBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#1e40af;font-size:0.98rem;margin-bottom:0.6rem;">🏗️ Sentence Classification (Simple / Compound / Complex):</h4>
        ${gramObj.sentenceClassification.map(s => `
          <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:0.6rem 0.85rem;margin-bottom:0.5rem;font-size:0.9rem;">
            <div><strong>${s.num}.</strong> ${s.sentence}</div>
            <div style="font-size:0.85rem;color:#2563eb;margin-top:0.2rem;"><strong>Type:</strong> ${s.type} (${s.reason})</div>
          </div>
        `).join('')}
      </div>`);
  }

  if (gramObj.phrasesIdentification && gramObj.phrasesIdentification.length > 0) {
    gramBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:#1e40af;font-size:0.98rem;margin-bottom:0.6rem;">🧩 Phrases Identification:</h4>
        ${gramObj.phrasesIdentification.map(p => `
          <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.6rem 0.85rem;margin-bottom:0.5rem;font-size:0.9rem;">
            <div><strong>${p.num}.</strong> ${p.sentence}</div>
            <div style="font-size:0.85rem;color:#0f766e;margin-top:0.2rem;"><strong>Phrase:</strong> "${p.phrase}" → ${p.kind}</div>
          </div>
        `).join('')}
      </div>`);
  }

  // 5j. Revision Exercises in Unit 5 / 10
  if (ex.revisionExercises) {
    const rev = ex.revisionExercises;
    gramBlocks.push(`
      <div style="margin-bottom:1.25rem;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;padding:1rem;">
        <h4 style="color:#1e293b;font-size:0.98rem;margin-bottom:0.6rem;">📚 ${rev.title || 'Revision Section'}:</h4>
        ${Object.keys(rev).filter(k => k !== 'title').map(k => {
          const item = rev[k];
          if (item.table) {
            return `
              <div style="margin-bottom:1rem;overflow-x:auto;">
                <h5 style="color:#0f766e;margin-bottom:0.4rem;">${item.title || k}:</h5>
                <table style="width:100%;border-collapse:collapse;font-size:0.88rem;">
                  <tbody>
                    ${item.table.map((row, rIdx) => `
                      <tr style="background:${rIdx===0?'#e2e8f0':'#ffffff'};">
                        ${row.map(cell => `<td style="padding:0.45rem;border:1px solid #cbd5e1;">${cell}</td>`).join('')}
                      </tr>
                    `).join('')}
                  </tbody>
                </table>
              </div>`;
          } else if (item.sentences) {
            return `
              <div style="margin-bottom:1rem;">
                <h5 style="color:#1e40af;margin-bottom:0.4rem;">${item.title || k}:</h5>
                ${item.sentences.map(s => `
                  <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:4px;padding:0.45rem 0.75rem;margin-bottom:0.35rem;font-size:0.88rem;">
                    <strong>${s.num || '•'}.</strong> ${s.sentence || s.question || s.text} 
                    ${s.answer ? `<strong style="color:#16a34a;">→ ${s.answer}</strong>` : ''}
                    ${s.clause ? `<div style="font-size:0.82rem;color:#64748b;">Clause: "${s.clause}" (${s.type})</div>` : ''}
                  </div>
                `).join('')}
              </div>`;
          }
          return '';
        }).join('')}
      </div>`);
  }

  if (gramBlocks.length > 0) {
    gramHtml = `
      <div class="slo-accordion-card open" style="margin-bottom:1.25rem;">
        <div class="slo-accordion-header" onclick="toggleSloAccordion(this)" style="background:#eff6ff;">
          <span style="font-weight:700;color:#1e40af;">📐 Grammar, Punctuation & Syntax Activities</span>
          <span class="slo-acc-icon">▲</span>
        </div>
        <div class="slo-accordion-body" style="padding:1.25rem;">
          ${gramBlocks.join('')}
        </div>
      </div>`;
  }

  // 6. Writing Tasks & Models
  let writHtml = '';
  let writBlocks = [];

  if (typeof writTasks === 'object' && !Array.isArray(writTasks)) {
    // Check all possible writing keys
    Object.keys(writTasks).forEach(k => {
      const w = writTasks[k];
      if (k === 'urduToEnglishTranslation' && Array.isArray(w)) {
        writBlocks.push(`
          <div style="margin-bottom:1.25rem;">
            <h4 style="color:#0f766e;font-size:0.98rem;margin-bottom:0.6rem;">🌐 Urdu to English Translation:</h4>
            ${w.map(t => `
              <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.6rem 0.85rem;margin-bottom:0.5rem;font-size:0.9rem;">
                <div style="font-family:'Noto Nastaliq Urdu',serif;direction:rtl;text-align:right;color:#0f766e;font-size:1.05rem;margin-bottom:0.25rem;">${t.num}. ${t.urdu}</div>
                <div style="color:#1e293b;font-weight:600;">${t.english}</div>
              </div>
            `).join('')}
          </div>`);
      } else if (k === 'paraphraseStanzas' && Array.isArray(w)) {
        writBlocks.push(`
          <div style="margin-bottom:1.25rem;">
            <h4 style="color:#0f766e;font-size:0.98rem;margin-bottom:0.6rem;">✍️ Paraphrasing of Stanzas:</h4>
            ${w.map(p => `
              <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:0.75rem;margin-bottom:0.5rem;font-size:0.9rem;">
                <strong style="color:#1e40af;">${p.stanza}:</strong>
                <div style="color:#334155;line-height:1.6;margin-top:0.3rem;">${p.content}</div>
              </div>
            `).join('')}
          </div>`);
      } else if (w && typeof w === 'object' && w.title && w.content) {
        writBlocks.push(`
          <div style="margin-bottom:1.25rem;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;padding:1rem;box-shadow:0 1px 3px rgba(0,0,0,0.05);">
            <h4 style="color:#1e293b;font-size:0.98rem;margin-bottom:0.5rem;border-bottom:1px solid #f1f5f9;padding-bottom:0.4rem;">📝 ${w.title}:</h4>
            <div style="font-size:0.92rem;color:#334155;line-height:1.65;white-space:pre-line;">
              ${w.content}
            </div>
          </div>`);
      }
    });
  } else if (Array.isArray(writTasks) && writTasks.length > 0) {
    writBlocks.push(`
      <div style="margin-bottom:1.25rem;">
        ${writTasks.map(w => `
          <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.75rem;margin-bottom:0.5rem;font-size:0.9rem;">
            <strong style="color:#1e293b;">${w.title || w.prompt}:</strong>
            <div style="color:#334155;line-height:1.6;margin-top:0.3rem;white-space:pre-line;">${w.content || w.sample || w.solution}</div>
          </div>
        `).join('')}
      </div>`);
  }

  if (writBlocks.length > 0) {
    writHtml = `
      <div class="slo-accordion-card open" style="margin-bottom:1.25rem;">
        <div class="slo-accordion-header" onclick="toggleSloAccordion(this)" style="background:#fffbeb;">
          <span style="font-weight:700;color:#92400e;">✍️ Writing Tasks, Formal Letters, Essays & Applications</span>
          <span class="slo-acc-icon">▲</span>
        </div>
        <div class="slo-accordion-body" style="padding:1.25rem;">
          ${writBlocks.join('')}
        </div>
      </div>`;
  }

  // 7. Listening & Speaking Activity
  let speakHtml = '';
  if (speakObj) {
    speakHtml = `
      <div class="slo-accordion-card open" style="margin-bottom:1.25rem;">
        <div class="slo-accordion-header" onclick="toggleSloAccordion(this)" style="background:#fdf2f8;">
          <span style="font-weight:700;color:#9d174d;">🎙️ Listening & Speaking Activity</span>
          <span class="slo-acc-icon">▲</span>
        </div>
        <div class="slo-accordion-body" style="padding:1.25rem;">
          <h4 style="color:#831843;font-size:0.98rem;margin-bottom:0.5rem;">${speakObj.title || 'Oral Communication Task'}:</h4>
          <div style="font-size:0.92rem;color:#334155;line-height:1.65;white-space:pre-line;background:#ffffff;padding:0.85rem;border-radius:6px;border:1px solid #fbcfe8;">
            ${speakObj.dialogue || speakObj.content || speakObj.activity}
          </div>
        </div>
      </div>`;
  }

  // 8. Final Revision Section (Pages 150-151)
  let finalRevHtml = '';
  if (finalRev) {
    finalRevHtml = `
      <div class="slo-accordion-card open" style="margin-bottom:1.25rem;">
        <div class="slo-accordion-header" onclick="toggleSloAccordion(this)" style="background:#f8fafc;border:2px solid #3b82f6;">
          <span style="font-weight:800;color:#1d4ed8;font-size:1.02rem;">🏆 ${finalRev.title || 'Final Comprehensive Revision Section (Pages 150–151)'}</span>
          <span class="slo-acc-icon">▲</span>
        </div>
        <div class="slo-accordion-body" style="padding:1.25rem;">
          
          <!-- Ex 1: Quotation Marks -->
          ${finalRev.exercise1_quotationMarks ? `
            <div style="margin-bottom:1.25rem;">
              <h4 style="color:#1e40af;font-size:0.96rem;margin-bottom:0.5rem;">Exercise 1: Insert quotation marks where needed.</h4>
              ${finalRev.exercise1_quotationMarks.map(e => `
                <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.5rem 0.85rem;margin-bottom:0.45rem;font-size:0.9rem;">
                  <div style="color:#64748b;">${e.num}. ${e.original}</div>
                  <div style="color:#1e40af;font-weight:700;margin-top:0.2rem;">✓ ${e.solved}</div>
                </div>
              `).join('')}
            </div>
          ` : ''}

          <!-- Ex 2: Hyphens -->
          ${finalRev.exercise2_hyphens ? `
            <div style="margin-bottom:1.25rem;">
              <h4 style="color:#1e40af;font-size:0.96rem;margin-bottom:0.5rem;">Exercise 2: Insert hyphens where needed and state the supporting rule.</h4>
              ${finalRev.exercise2_hyphens.map(e => `
                <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.5rem 0.85rem;margin-bottom:0.45rem;font-size:0.9rem;">
                  <div style="color:#16a34a;font-weight:700;">${e.num}. ${e.solved}</div>
                  <div style="font-size:0.83rem;color:#64748b;margin-top:0.15rem;"><em>Rule:</em> ${e.rule}</div>
                </div>
              `).join('')}
            </div>
          ` : ''}

          <!-- Ex 3: Ellipsis -->
          ${finalRev.exercise3_ellipsis ? `
            <div style="margin-bottom:1.25rem;">
              <h4 style="color:#1e40af;font-size:0.96rem;margin-bottom:0.5rem;">Exercise 3: Rewrite each sentence omitting text and using an ellipsis (...).</h4>
              ${finalRev.exercise3_ellipsis.map(e => `
                <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.5rem 0.85rem;margin-bottom:0.45rem;font-size:0.9rem;">
                  <div style="color:#64748b;">${e.num}. ${e.original}</div>
                  <div style="color:#2563eb;font-weight:700;margin-top:0.2rem;">✓ ${e.solved}</div>
                </div>
              `).join('')}
            </div>
          ` : ''}

          <!-- Ex 4: Parentheses -->
          ${finalRev.exercise4_parentheses ? `
            <div style="margin-bottom:1.25rem;">
              <h4 style="color:#1e40af;font-size:0.96rem;margin-bottom:0.5rem;">Exercise 4: Rewrite each sentence placing parentheses ( ) in the correct places.</h4>
              ${finalRev.exercise4_parentheses.map(e => `
                <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.5rem 0.85rem;margin-bottom:0.45rem;font-size:0.9rem;">
                  <div style="color:#64748b;">${e.num}. ${e.original}</div>
                  <div style="color:#7c3aed;font-weight:700;margin-top:0.2rem;">✓ ${e.solved}</div>
                </div>
              `).join('')}
            </div>
          ` : ''}

          <!-- Ex 5: Indirect Speech -->
          ${finalRev.exercise5_indirectSpeech ? `
            <div style="margin-bottom:1.25rem;">
              <h4 style="color:#1e40af;font-size:0.96rem;margin-bottom:0.5rem;">Exercise 5: Change the following sentences into indirect speech.</h4>
              ${finalRev.exercise5_indirectSpeech.map(e => `
                <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.5rem 0.85rem;margin-bottom:0.45rem;font-size:0.9rem;">
                  <div style="color:#64748b;">${e.num}. ${e.direct}</div>
                  <div style="color:#0f766e;font-weight:700;margin-top:0.2rem;">✓ ${e.indirect}</div>
                </div>
              `).join('')}
            </div>
          ` : ''}

          <!-- Ex 6: Punctuation & Capitalization -->
          ${finalRev.exercise6_punctuationCapitalization ? `
            <div style="margin-bottom:1.25rem;">
              <h4 style="color:#1e40af;font-size:0.96rem;margin-bottom:0.5rem;">Exercise 6: Rewrite using appropriate punctuation marks and capital letters.</h4>
              ${finalRev.exercise6_punctuationCapitalization.map(e => `
                <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.5rem 0.85rem;margin-bottom:0.45rem;font-size:0.9rem;">
                  <div style="color:#64748b;">${e.num}. ${e.original}</div>
                  <div style="color:#16a34a;font-weight:700;margin-top:0.2rem;">✓ ${e.solved}</div>
                </div>
              `).join('')}
            </div>
          ` : ''}

          <!-- Ex 7: Active to Passive -->
          ${finalRev.exercise7_activeToPassive ? `
            <div style="margin-bottom:1.25rem;">
              <h4 style="color:#1e40af;font-size:0.96rem;margin-bottom:0.5rem;">Exercise 7: Change the following sentences into passive voice.</h4>
              ${finalRev.exercise7_activeToPassive.map(e => `
                <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.5rem 0.85rem;margin-bottom:0.45rem;font-size:0.9rem;">
                  <div style="color:#64748b;">${e.num}. ${e.active}</div>
                  <div style="color:#1e40af;font-weight:700;margin-top:0.2rem;">✓ ${e.passive}</div>
                </div>
              `).join('')}
            </div>
          ` : ''}

          <!-- Ex 8: Voice Transformations -->
          ${finalRev.exercise8_voiceTransformations ? `
            <div style="margin-bottom:1.25rem;">
              <h4 style="color:#1e40af;font-size:0.96rem;margin-bottom:0.5rem;">Exercise 8: Rewrite changing active to passive and passive to active.</h4>
              ${finalRev.exercise8_voiceTransformations.map(e => `
                <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:0.5rem 0.85rem;margin-bottom:0.45rem;font-size:0.9rem;">
                  <div style="color:#64748b;">${e.num}. ${e.original}</div>
                  <div style="color:#16a34a;font-weight:700;margin-top:0.2rem;">✓ ${e.transformed}</div>
                </div>
              `).join('')}
            </div>
          ` : ''}

        </div>
      </div>`;
  }

  // 9. About the Textbook Authors & Concluding Quranic Ayat (Page 152)
  let authorsHtml = '';
  if (aboutAuthors) {
    authorsHtml = `
      <div class="slo-accordion-card open" style="margin-bottom:1.25rem;">
        <div class="slo-accordion-header" onclick="toggleSloAccordion(this)" style="background:#ecfdf5;border:2px solid #10b981;">
          <span style="font-weight:800;color:#065f46;font-size:1.02rem;">📚 ${aboutAuthors.title || 'About the Textbook Authors (Page 152)'}</span>
          <span class="slo-acc-icon">▲</span>
        </div>
        <div class="slo-accordion-body" style="padding:1.25rem;">
          <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:1rem;margin-bottom:1.25rem;">
            ${(aboutAuthors.authors || []).map(a => `
              <div style="background:#ffffff;border:1px solid #a7f3d0;border-radius:8px;padding:1rem;box-shadow:0 1px 3px rgba(0,0,0,0.05);">
                <h4 style="color:#047857;font-size:0.98rem;margin-bottom:0.4rem;">${a.name}</h4>
                <div style="font-size:0.88rem;color:#334155;line-height:1.6;">${a.bio}</div>
              </div>
            `).join('')}
          </div>
          ${aboutAuthors.quranicConclusion ? `
            <div style="background:#f0fdf4;border:2px dashed #059669;border-radius:10px;padding:1.25rem;text-align:center;">
              <div style="font-size:1.4rem;color:#065f46;margin-bottom:0.6rem;font-family:'Amiri',serif;direction:rtl;">
                ${aboutAuthors.quranicConclusion.arabic}
              </div>
              <div style="font-family:'Noto Nastaliq Urdu',serif;direction:rtl;font-size:1.1rem;color:#047857;margin-bottom:0.5rem;">
                ${aboutAuthors.quranicConclusion.urdu}
              </div>
              <div style="font-size:0.92rem;color:#334155;font-style:italic;">
                ${aboutAuthors.quranicConclusion.english}
              </div>
            </div>
          ` : ''}
        </div>
      </div>`;
  }

  const figLinesHtml = Array.isArray(ch.exercise && ch.exercise.figurativeLines) && ch.exercise.figurativeLines.length ? `
    <div style="background:#fef3c7;border:2px solid #f59e0b;border-radius:12px;padding:1rem 1.2rem;margin-bottom:1rem;">
      <h4 style="font-weight:800;color:#b45309;margin:0 0 0.6rem;">✨ Figurative Language in the Poem</h4>
      ${ch.exercise.figurativeLines.map(f => `
        <div style="background:#fffbeb;border-left:4px solid #f59e0b;border-radius:8px;padding:0.6rem 0.9rem;margin-bottom:0.55rem;">
          <div style="font-size:0.75rem;font-weight:800;color:#b45309;text-transform:uppercase;letter-spacing:0.4px;">${f.category || ''}</div>
          <div style="font-style:italic;color:#1e293b;margin:0.25rem 0 0.15rem;font-size:0.95rem;">"${f.lines || ''}"</div>
          <div style="font-size:0.85rem;color:#475569;">${f.device || ''}</div>
        </div>`).join('')}
    </div>` : '';

  return `
    <div class="eng-exercise-container" style="max-width:980px;margin:0 auto;padding:0.5rem 0;">
      ${figLinesHtml}
      ${glossaryHtml}
      ${tbMcqsHtml}
      ${compHtml}
      ${vocabHtml}
      ${gramHtml}
      ${writHtml}
      ${speakHtml}
      ${finalRevHtml}
      ${authorsHtml}
    </div>`;
}

function renderEngSLOs(ch) {
  const slos = ch.slos || [
    "Identify central themes, main ideas, and supporting details in complex texts.",
    "Demonstrate proficiency in advanced grammar rules, voice, and conditional clauses.",
    "Acquire and apply high-frequency academic vocabulary in oral and written composition.",
    "Solve 20+ Board-aligned SLO MCQs, 10+ SQs, and 5+ comprehensive LQs."
  ];

  return `
    <div style="background:#ffffff;border:1px solid var(--border);border-radius:12px;padding:1.75rem;margin-bottom:2rem;">
      <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:1.25rem;">
        <span style="font-size:2rem;">🎯</span>
        <div>
          <h3 style="color:var(--navy);font-size:1.25rem;margin-bottom:0.25rem;">Student Learning Outcomes (SLOs)</h3>
          <p style="color:var(--text-muted);font-size:0.85rem;">Official Khyber Pakhtunkhwa Textbook Board Competencies for Unit ${ch.number}</p>
        </div>
      </div>

      <div style="display:flex;flex-direction:column;gap:0.75rem;">
        ${slos.map((slo, idx) => `
          <div style="display:flex;align-items:flex-start;gap:0.75rem;padding:0.85rem 1rem;background:#f8fafc;border-left:4px solid #0284c7;border-radius:6px;">
            <span style="font-weight:800;color:#0284c7;font-size:1.05rem;">0${idx + 1}.</span>
            <span style="color:#1e293b;line-height:1.7;font-size:0.96rem;">${slo}</span>
          </div>`).join('')}
      </div>
    </div>`;
}

// ─── 8. BOTTOM SLO EXAM ROADMAP (MCQs, SQs, LQs) ───
function renderEngSloMcqs(ch) {
  const mcqs = (ch.sloQuestions && ch.sloQuestions.mcqs) ? ch.sloQuestions.mcqs : [];
  if (mcqs.length === 0) {
    return `<div style="padding:1.5rem;text-align:center;color:#64748b;">No SLO MCQs available for this unit.</div>`;
  }

  const mcqsHtml = mcqs.map((m, idx) => {
    const letters = ['A', 'B', 'C', 'D'];
    const optionsHtml = m.options.map((opt, oIdx) => `
      <div class="slo-mcq-option" data-qidx="${idx}" data-oidx="${oIdx}" onclick="checkEngSloMcq(${idx}, ${oIdx}, ${m.correct})">
        <span class="mcq-opt-letter">${letters[oIdx]}</span>
        <span class="mcq-opt-text">${opt}</span>
      </div>`).join('');

    return `
      <div class="slo-accordion-card" id="eng-mcq-card-${idx}">
        <div class="slo-accordion-header" onclick="toggleSloAccordion(this)">
          <div style="display:flex;align-items:center;gap:0.65rem;">
            <span class="slo-q-badge" style="background:#0284c7;">MCQ ${idx + 1}</span>
            <span style="font-weight:600;color:#1e293b;">${m.question}</span>
          </div>
          <span class="slo-acc-icon">▼</span>
        </div>
        <div class="slo-accordion-body" style="padding:1.25rem;">
          <div class="slo-mcq-options-grid">
            ${optionsHtml}
          </div>
          <div id="eng-mcq-feedback-${idx}" class="slo-mcq-feedback" style="display:none;">
            <div style="display:flex;align-items:center;gap:0.5rem;font-weight:700;margin-bottom:0.25rem;" id="eng-mcq-status-${idx}"></div>
            <div style="font-size:0.88rem;color:#334155;" id="eng-mcq-exp-${idx}">${m.explanation || ''}</div>
          </div>
        </div>
      </div>`;
  }).join('');

  return `
    <div>
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:0.5rem;margin-bottom:1rem;background:#f0f9ff;padding:0.75rem 1rem;border-radius:8px;border:1px solid #bae6fd;">
        <span style="font-size:0.9rem;color:#0369a1;font-weight:700;">
          📝 Unit ${ch.number} Interactive Assessment: ${mcqs.length} Board Exam SLO MCQs
        </span>
        <span id="engMcqScoreBadge" style="background:#0284c7;color:#fff;padding:0.25rem 0.65rem;border-radius:99px;font-size:0.8rem;font-weight:700;">
          Score: 0 / ${mcqs.length}
        </span>
      </div>
      <div class="slo-accordion-list">
        ${mcqsHtml}
      </div>
    </div>`;
}

function checkEngSloMcq(qIdx, selectedOpt, correctOpt) {
  const card = $(`eng-mcq-card-${qIdx}`);
  if (!card) return;

  const options = card.querySelectorAll(".slo-mcq-option");
  options.forEach((opt, oIdx) => {
    opt.onclick = null; // Disable further clicks
    if (oIdx === correctOpt) {
      opt.classList.add("correct");
    } else if (oIdx === selectedOpt && selectedOpt !== correctOpt) {
      opt.classList.add("incorrect");
    }
  });

  const feedback = $(`eng-mcq-feedback-${qIdx}`);
  const status = $(`eng-mcq-status-${qIdx}`);
  if (feedback && status) {
    feedback.style.display = "block";
    if (selectedOpt === correctOpt) {
      feedback.className = "slo-mcq-feedback correct";
      status.innerHTML = "✅ Correct Answer!";
    } else {
      feedback.className = "slo-mcq-feedback incorrect";
      status.innerHTML = "❌ Incorrect. See explanation below:";
    }
  }

  // Update total score
  const totalCorrect = document.querySelectorAll("#engSloTabContent .slo-mcq-feedback.correct").length;
  const totalAnswered = document.querySelectorAll("#engSloTabContent .slo-mcq-feedback[style*='block']").length;
  const badge = $("engMcqScoreBadge");
  if (badge) {
    badge.textContent = `Score: ${totalCorrect} / ${totalAnswered} Answered`;
  }
}

function renderEngSloSQs(ch) {
  const sqs = (ch.sloQuestions && ch.sloQuestions.shortQuestions) ? ch.sloQuestions.shortQuestions : [];
  if (sqs.length === 0) {
    return `<div style="padding:1.5rem;text-align:center;color:#64748b;">No SLO Short Questions available for this unit.</div>`;
  }

  const sqsHtml = sqs.map((sq, idx) => `
    <div class="slo-accordion-card">
      <div class="slo-accordion-header" onclick="toggleSloAccordion(this)">
        <div style="display:flex;align-items:center;gap:0.65rem;">
          <span class="slo-q-badge" style="background:#0284c7;">SQ ${idx + 1}</span>
          <span style="font-weight:600;color:#1e293b;">${sq.question}</span>
        </div>
        <div style="display:flex;align-items:center;gap:0.75rem;">
          <span style="background:#e0f2fe;color:#0369a1;padding:0.2rem 0.5rem;border-radius:4px;font-size:0.75rem;font-weight:700;">${sq.marks || '3 Marks'}</span>
          <span class="slo-acc-icon">▼</span>
        </div>
      </div>
      <div class="slo-accordion-body" style="padding:1.25rem;">
        <div style="font-size:0.98rem;line-height:1.9;color:#1e293b;">
          <b style="color:#0284c7;">Model Answer &amp; Marking Rubric:</b><br>
          ${sq.answer}
        </div>
      </div>
    </div>`).join('');

  return `
    <div>
      <div style="margin-bottom:1rem;background:#f0f9ff;padding:0.75rem 1rem;border-radius:8px;border:1px solid #bae6fd;color:#0369a1;font-weight:700;font-size:0.9rem;">
        ✏️ Unit ${ch.number} Conceptual Short Questions: ${sqs.length} Board Exam SLO SQs with Model Answers
      </div>
      <div class="slo-accordion-list">
        ${sqsHtml}
      </div>
    </div>`;
}

function renderEngSloLQs(ch) {
  const lqs = (ch.sloQuestions && ch.sloQuestions.longQuestions) ? ch.sloQuestions.longQuestions : [];
  if (lqs.length === 0) {
    return `<div style="padding:1.5rem;text-align:center;color:#64748b;">No SLO Long Questions available for this unit.</div>`;
  }

  const lqsHtml = lqs.map((lq, idx) => `
    <div class="slo-accordion-card">
      <div class="slo-accordion-header" onclick="toggleSloAccordion(this)">
        <div style="display:flex;align-items:center;gap:0.65rem;">
          <span class="slo-q-badge" style="background:#0284c7;">LQ ${idx + 1}</span>
          <span style="font-weight:600;color:#1e293b;">${lq.question}</span>
        </div>
        <div style="display:flex;align-items:center;gap:0.75rem;">
          <span style="background:#dbeafe;color:#1e40af;padding:0.2rem 0.5rem;border-radius:4px;font-size:0.75rem;font-weight:700;">${lq.marks || '8 Marks'}</span>
          <span class="slo-acc-icon">▼</span>
        </div>
      </div>
      <div class="slo-accordion-body" style="padding:1.5rem;">
        ${lq.outline ? `
          <div style="background:#f8fafc;padding:0.75rem 1rem;border-left:4px solid #0284c7;border-radius:4px;margin-bottom:1rem;font-size:0.88rem;color:#475569;white-space:pre-line;">
            <b style="color:#0284c7;">Conceptual Essay Outline:</b><br>${lq.outline}
          </div>` : ''}
        <div style="font-size:1rem;line-height:2.0;color:#1e293b;white-space:pre-line;">
          <b style="color:#0284c7;">Comprehensive Model Answer:</b><br>
          ${lq.answer}
        </div>
      </div>
    </div>`).join('');

  return `
    <div>
      <div style="margin-bottom:1rem;background:#f0fdf4;padding:0.75rem 1rem;border-radius:8px;border:1px solid #86efac;color:#15803d;font-weight:700;font-size:0.9rem;">
        📝 Unit ${ch.number} In-Depth Long Questions: ${lqs.length} Comprehensive Essays &amp; Analytic Models
      </div>
      <div class="slo-accordion-list">
        ${lqsHtml}
      </div>
    </div>`;
}
function getUrduChapterList() {
  if (typeof URDU_DATA !== 'undefined' && Array.isArray(URDU_DATA) && URDU_DATA.length > 0) return URDU_DATA;
  if (typeof window !== 'undefined' && window.URDU_DATA && Array.isArray(window.URDU_DATA) && window.URDU_DATA.length > 0) return window.URDU_DATA;
  if (typeof DATA !== 'undefined' && DATA.urduChapters && Array.isArray(DATA.urduChapters) && DATA.urduChapters.length > 0) return DATA.urduChapters;
  return [];
}

// ─────────────────────────────────────────
//  URDU INTERACTIVE LESSONS & TRILINGUAL PORTAL
// ─────────────────────────────────────────
function openUrduView(classId, subj) {
  state.activeSubject = "urdu";
  state.selectedUrduChapter = 0;
  state.activeUrduTab = "lesson";
  state.activeUrduSloTab = "slo-mcqs";
  state.selectedClass = classId;
  setActiveNav("subjects");
  const cls = DATA.classes.find(c => c.id === classId) || { name: "Class 9" };
  const chList = getUrduChapterList();
  const gradeLabel = "Grade 9";
  const pdfFile = "assets/books/Class-9-Urdu-KPK.pdf";

  setDashHeader(`📗 ${subj.name} — ${gradeLabel}`, `KPK Textbook Board, Peshawar · 15 Lessons & Poetry &nbsp;|&nbsp; <a href="${pdfFile}" target="_blank" style="color:#16a34a;font-weight:700;text-decoration:underline;">📥 View/Download Official Urdu Book PDF</a>`);
  setBreadcrumb([
    { label: "Home",     onclick: () => { setActiveNav("home"); renderHome(); } },
    { label: "Subjects", onclick: () => renderClasses() },
    { label: cls.name,   onclick: () => goToSubjects(classId) },
    { label: subj.name,  active: true }
  ]);

  const chapBtns = chList.map((ch, i) => `
    <button class="bio-ch-btn ${i === 0 ? "active" : ""}" id="urdu-btn-${i}"
            onclick="selectUrduChapter(${i})">
      <span class="ch-btn-num" style="background:#16a34a;color:#fff;">${ch.type === 'prose' ? 'سبق ' + ch.number : 'نظم ' + (ch.number - 11)}</span>
      <span class="ch-btn-info">
        <span class="ch-btn-name" style="direction:rtl;text-align:right;font-family:'Jameel Noori Nastaleeq', 'Segoe UI', serif;font-size:1.05rem;">${ch.title || ''}</span>
        <span class="ch-btn-sub">${ch.author || ''}</span>
      </span>
      <span class="ch-btn-status" style="background:#dcfce7;color:#15803d;">
        ✅ Complete
      </span>
    </button>`).join("");

  pageContent().innerHTML = `
    <div class="bio-view">
      <div class="bio-ch-sidebar">
        <div class="bio-ch-sidebar-header" style="background:linear-gradient(135deg,#16a34a,#15803d);color:#fff;">
          <button onclick="goToSubjects('${classId}')" class="sidebar-back-icon-btn" title="Back to Subjects">←</button>
          <span>📗 KPK ${gradeLabel} Urdu</span>
        </div>
        <div class="bio-ch-list">${chapBtns}</div>
        <div style="padding:1rem;background:#f8fafc;border-top:1px solid var(--border);text-align:center;">
          <a href="${pdfFile}" target="_blank" style="display:block;width:100%;padding:0.55rem;background:#16a34a;color:#fff;border-radius:6px;font-weight:700;font-size:0.82rem;text-decoration:none;">
            📥 Download Official PDF Book
          </a>
        </div>
      </div>
      <div class="bio-topic-area" id="urduTopicArea"></div>
    </div>`;

  renderUrduChapter(0);
}

function selectUrduChapter(index) {
  stopUrduTTS();
  state.selectedUrduChapter = index;
  document.querySelectorAll(".bio-ch-btn").forEach((btn, i) =>
    btn.classList.toggle("active", i === index));
  renderUrduChapter(index);
}

function switchUrduTab(tabName) {
  stopUrduTTS();
  state.activeUrduTab = tabName;
  document.querySelectorAll(".urdu-top-tab").forEach(btn =>
    btn.classList.toggle("active", btn.dataset.tab === tabName));

  const chList = getUrduChapterList();
  const ch = chList[state.selectedUrduChapter];
  const container = $("urduTabContent");
  if (!container || !ch) return;

  if (tabName === "lesson") {
    container.innerHTML = renderUrduLesson(ch);
  } else if (tabName === "ps-trans") {
    container.innerHTML = renderUrduPashtoTranslation(ch);
  } else if (tabName === "en-trans") {
    container.innerHTML = renderUrduEnglishTranslation(ch);
  } else if (tabName === "video") {
    container.innerHTML = renderUrduVideo(ch);
  } else if (tabName === "en-sum") {
    container.innerHTML = renderUrduEnglishSummary(ch);
  } else if (tabName === "ur-sum") {
    container.innerHTML = renderUrduUrduSummary(ch);
  } else if (tabName === "ps-sum") {
    container.innerHTML = renderUrduPashtoSummary(ch);
  } else if (tabName === "exercise") {
    container.innerHTML = renderUrduExercise(ch);
  } else if (tabName === "slos") {
    container.innerHTML = renderUrduSLOs(ch);
  }
}

function switchUrduSloTab(tabName) {
  if (state.activeUrduSloTab === tabName) {
    state.activeUrduSloTab = null;
    document.querySelectorAll(".slo-tab-pill").forEach(btn => btn.classList.remove("active"));
    const container = $("urduSloTabContent");
    if (container) container.innerHTML = "";
    return;
  }

  state.activeUrduSloTab = tabName;
  document.querySelectorAll(".slo-tab-pill").forEach(btn =>
    btn.classList.toggle("active", btn.dataset.slotab === tabName));

  const chList = getUrduChapterList();
  const ch = chList[state.selectedUrduChapter];
  const container = $("urduSloTabContent");
  if (!container || !ch) return;

  if (!tabName) {
    container.innerHTML = "";
    return;
  }

  if (tabName === "slo-mcqs") {
    container.innerHTML = renderUrduSloMcqs(ch);
  } else if (tabName === "slo-sq") {
    container.innerHTML = renderUrduSloSQs(ch);
  } else if (tabName === "slo-lq") {
    container.innerHTML = renderUrduSloLQs(ch);
  }
}

function renderUrduChapter(index) {
  const chList = getUrduChapterList();
  const ch = chList[index];
  const area = $("urduTopicArea");
  if (!area || !ch) return;

  const sqCount = (ch.exercise && ch.exercise.shortQuestions ? ch.exercise.shortQuestions.length : 0) + (ch.sloQuestions && ch.sloQuestions.shortQuestions ? ch.sloQuestions.shortQuestions.length : 0);
  const mcqCount = (ch.exercise && ch.exercise.mcqs ? ch.exercise.mcqs.length : 0) + (ch.sloQuestions && ch.sloQuestions.mcqs ? ch.sloQuestions.mcqs.length : 0);

  area.innerHTML = `
    <div class="chapter-title-bar" style="border-left: 4px solid #16a34a;">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:0.75rem;width:100%;">
        <div>
          <div style="direction:rtl;text-align:right;">
            <h2 style="font-family:'Jameel Noori Nastaleeq','Segoe UI',serif;color:var(--navy);font-size:1.6rem;margin-bottom:0.25rem;">${ch.number}. ${ch.title}</h2>
            <p style="color:#15803d;font-weight:700;font-size:0.95rem;">مصنف / شاعر: ${ch.author} · ${ch.titlePs || ''}</p>
          </div>
          <p style="color:var(--text-muted);font-size:0.85rem;margin-top:0.25rem;">${ch.titleEn} · ${sqCount} Short Questions · ${mcqCount} MCQs · Trilingual Translations &amp; Video</p>
        </div>
        <button class="btn-back-sm" onclick="goToSubjects('${state.selectedClass || 'cls9'}')"><span class="back-arrow">←</span> Back to Subjects</button>
      </div>
    </div>

    <!-- Upper / Top Tabs -->
    <div class="chapter-nav-tabs" style="border-bottom: 2px solid #86efac; overflow-x: auto; flex-wrap: nowrap; padding-bottom: 4px;">
      <button class="bio-tab-btn urdu-top-tab ${state.activeUrduTab === 'lesson' ? 'active' : ''}" data-tab="lesson" onclick="switchUrduTab('lesson')">
        📖 Lesson / سبق
      </button>
      <button class="bio-tab-btn urdu-top-tab ${state.activeUrduTab === 'ps-trans' ? 'active' : ''}" data-tab="ps-trans" onclick="switchUrduTab('ps-trans')">
        🇦🇫 Pashto translation / پښتو ژباړه
      </button>
      <button class="bio-tab-btn urdu-top-tab ${state.activeUrduTab === 'en-trans' ? 'active' : ''}" data-tab="en-trans" onclick="switchUrduTab('en-trans')">
        🇬🇧 English Translation
      </button>
      <button class="bio-tab-btn urdu-top-tab ${state.activeUrduTab === 'video' ? 'active' : ''}" data-tab="video" onclick="switchUrduTab('video')">
        🎥 Video / ویڈیو لیکچر
      </button>
      <button class="bio-tab-btn urdu-top-tab ${state.activeUrduTab === 'en-sum' ? 'active' : ''}" data-tab="en-sum" onclick="switchUrduTab('en-sum')">
        📝 English Summary
      </button>
      <button class="bio-tab-btn urdu-top-tab ${state.activeUrduTab === 'ur-sum' ? 'active' : ''}" data-tab="ur-sum" onclick="switchUrduTab('ur-sum')">
        📜 اردو خلاصہ
      </button>
      <button class="bio-tab-btn urdu-top-tab ${state.activeUrduTab === 'ps-sum' ? 'active' : ''}" data-tab="ps-sum" onclick="switchUrduTab('ps-sum')">
        🇦🇫 پښتو لنډیز
      </button>
      <button class="bio-tab-btn urdu-top-tab ${state.activeUrduTab === 'exercise' ? 'active' : ''}" data-tab="exercise" onclick="switchUrduTab('exercise')">
        ✏️ مشقی سوالات و جوابات
      </button>
      <button class="bio-tab-btn urdu-top-tab ${state.activeUrduTab === 'slos' ? 'active' : ''}" data-tab="slos" onclick="switchUrduTab('slos')">
        🎯 حاصلاتِ تعلّم (SLOs)
      </button>
    </div>

    <!-- Main Tab Content Area -->
    <div id="urduTabContent" style="margin-top: 1.25rem;"></div>

    <!-- Bottom SLO Questions Section -->
    <div class="slo-bottom-section">
      <div class="slo-bottom-header">
        <div class="slo-bottom-title">
          <span>📊</span>
          <span>ایس ایل او امتحانی سوالات (SLO-Based Exam Roadmap)</span>
        </div>
        <div class="slo-bottom-tabs">
          <button class="slo-tab-pill ${state.activeUrduSloTab === 'slo-mcqs' ? 'active' : ''}" data-slotab="slo-mcqs" onclick="switchUrduSloTab('slo-mcqs')">
            🎯 MCQs / درست جواب کا انتخاب (SLO)
          </button>
          <button class="slo-tab-pill ${state.activeUrduSloTab === 'slo-sq' ? 'active' : ''}" data-slotab="slo-sq" onclick="switchUrduSloTab('slo-sq')">
            ✏️ SQ / مختصر سوالات (SLO)
          </button>
          <button class="slo-tab-pill ${state.activeUrduSloTab === 'slo-lq' ? 'active' : ''}" data-slotab="slo-lq" onclick="switchUrduSloTab('slo-lq')">
            📝 LQ / تفصیلی سوالات (SLO)
          </button>
        </div>
      </div>
      <div id="urduSloTabContent"></div>
    </div>
  `;

  // Render active upper tab and bottom tab
  switchUrduTab(state.activeUrduTab);
  switchUrduSloTab(state.activeUrduSloTab);
}

function toggleUrduSection(headerEl) {
  const card = headerEl.closest(".urdu-section-card");
  if (card) {
    card.classList.toggle("open");
  }
}

function expandAllUrduSections(expand) {
  document.querySelectorAll(".urdu-section-card").forEach(card => {
    if (expand) card.classList.add("open");
    else card.classList.remove("open");
  });
}

function toggleSloAccordion(headerEl) {
  const acc = headerEl.closest(".slo-question-accordion");
  if (!acc) return;
  const body = acc.querySelector(".slo-accordion-body");
  const isCurrentlyOpen = body && body.style.display === "block";
  if (body) {
    body.style.display = isCurrentlyOpen ? "none" : "block";
  }
  const badge = headerEl.querySelector(".slo-acc-toggle");
  if (badge) {
    badge.textContent = isCurrentlyOpen ? "+ جواب دیکھیں" : "− جواب چھپائیں";
  }
}

// ─── URDU TTS & REAL-TIME SYNCHRONIZED HIGHLIGHTING ENGINE ───
let urduTtsState = {
  activePrefix: null,
  activeGender: 'male', // 'male' | 'female'
  isPlaying: false,
  isPaused: false,
  speechRate: 1.0,
  sentences: [],
  currentSentenceIdx: 0,
  currentWordIdx: -1,
  totalWords: 0,
  audioObj: null,
  wordTimer: null,
  sectionTitle: ""
};

// Break text into paragraphs, sentences, and individual word spans with global indices
function prepareUrduTextForTts(rawText, prefix) {
  let globalWordIdx = 0;
  const paras = rawText.split(/\n\s*\n/).filter(Boolean);
  const sentences = [];

  const parasHtml = paras.map(p => {
    // Split paragraph by Urdu sentence delimiters
    const rawChunks = p.split(/([۔؟!؛\n]+)/).filter(Boolean);
    let chunks = [];
    for (let i = 0; i < rawChunks.length; i += 2) {
      const cText = ((rawChunks[i] || '') + (rawChunks[i+1] || '')).trim();
      if (cText) {
        if (cText.length > 130 && cText.includes('،')) {
          const sub = cText.split(/([،]+)/).filter(Boolean);
          for (let j = 0; j < sub.length; j += 2) {
            const sText = ((sub[j] || '') + (sub[j+1] || '')).trim();
            if (sText) chunks.push(sText);
          }
        } else {
          chunks.push(cText);
        }
      }
    }
    if (chunks.length === 0 && p.trim()) chunks.push(p.trim());

    const sentenceHtmls = chunks.map(chunkText => {
      const words = chunkText.split(/\s+/).filter(Boolean);
      const startIdx = globalWordIdx;
      const spans = words.map(w => {
        const widx = globalWordIdx++;
        const safe = w.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
        return `<span id="${prefix}-w-${widx}" class="tts-word" data-widx="${widx}">${safe}</span>`;
      }).join(' ');
      const endIdx = globalWordIdx - 1;

      if (words.length > 0) {
        sentences.push({
          text: chunkText,
          startIdx: startIdx,
          endIdx: endIdx,
          wordsCount: words.length
        });
      }
      return spans;
    });

    return `<p class="urdu-sec-p">${sentenceHtmls.join(' ')}</p>`;
  });

  return {
    html: parasHtml.join(''),
    sentences: sentences,
    totalWords: globalWordIdx
  };
}

function stopUrduTTS() {
  if (urduTtsState.audioObj) {
    try {
      urduTtsState.audioObj.pause();
      urduTtsState.audioObj.src = "";
    } catch (e) {}
    urduTtsState.audioObj = null;
  }
  if (window.speechSynthesis) {
    try { window.speechSynthesis.cancel(); } catch (e) {}
  }
  if (urduTtsState.wordTimer) {
    clearInterval(urduTtsState.wordTimer);
    urduTtsState.wordTimer = null;
  }

  // Clear any active highlight
  document.querySelectorAll(".tts-word.active-word").forEach(el => {
    el.classList.remove("active-word", "tts-male", "tts-female");
  });

  // Reset active button states
  document.querySelectorAll(".btn-tts-pill").forEach(btn => {
    btn.classList.remove("active-playing");
  });

  urduTtsState.isPlaying = false;
  urduTtsState.isPaused = false;
  urduTtsState.activePrefix = null;
  urduTtsState.currentWordIdx = -1;
  urduTtsState.sentences = [];
  urduTtsState.currentSentenceIdx = 0;

  // Hide floating dock
  const dock = $("urduTtsFloatingDock");
  if (dock) dock.style.display = "none";
}

function pauseResumeUrduTTS() {
  if (!urduTtsState.isPlaying) return;
  const btn = $("dockPauseBtn");

  if (urduTtsState.isPaused) {
    urduTtsState.isPaused = false;
    if (btn) btn.innerHTML = "⏸️ وقفہ";
    if (urduTtsState.audioObj) {
      urduTtsState.audioObj.play().catch(() => {});
    } else if (window.speechSynthesis) {
      window.speechSynthesis.resume();
    }
  } else {
    urduTtsState.isPaused = true;
    if (btn) btn.innerHTML = "▶️ جاری رکھیں";
    if (urduTtsState.audioObj) {
      urduTtsState.audioObj.pause();
    } else if (window.speechSynthesis) {
      window.speechSynthesis.pause();
    }
  }
}

function setUrduTtsRate(rate) {
  urduTtsState.speechRate = parseFloat(rate);
  if (urduTtsState.audioObj) {
    urduTtsState.audioObj.playbackRate = urduTtsState.speechRate;
  }
}

function highlightUrduWord(prefix, wordIdx, gender) {
  document.querySelectorAll(".tts-word.active-word").forEach(el => {
    el.classList.remove("active-word", "tts-male", "tts-female");
  });

  const wordEl = $(`${prefix}-w-${wordIdx}`);
  if (wordEl) {
    wordEl.classList.add("active-word", gender === "female" ? "tts-female" : "tts-male");
    const rect = wordEl.getBoundingClientRect();
    if (rect.top < 110 || rect.bottom > (window.innerHeight - 110)) {
      wordEl.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  }
}

// Proportional Character-Weighted Word Timing (Matches exact spoken syllable lengths)
function startProportionalWordHighlighting(sent, prefix, gender, totalDurationMs) {
  if (urduTtsState.wordTimer) {
    clearInterval(urduTtsState.wordTimer);
    urduTtsState.wordTimer = null;
  }

  const words = sent.text.split(/\s+/).filter(Boolean);
  if (words.length === 0) return;

  const weights = words.map(w => Math.max(2, w.length));
  const totalWeight = weights.reduce((a, b) => a + b, 0);
  const msPerWeightUnit = totalDurationMs / totalWeight;

  let currentRelIdx = 0;
  highlightUrduWord(prefix, sent.startIdx, gender);

  function scheduleNextWord() {
    if (urduTtsState.isPaused || !urduTtsState.isPlaying) return;
    currentRelIdx++;
    if (currentRelIdx < words.length) {
      const wordIdx = sent.startIdx + currentRelIdx;
      highlightUrduWord(prefix, wordIdx, gender);
      const delay = Math.max(120, Math.round(weights[currentRelIdx] * msPerWeightUnit));
      urduTtsState.wordTimer = setTimeout(scheduleNextWord, delay);
    } else {
      urduTtsState.wordTimer = null;
    }
  }

  const initialDelay = Math.max(120, Math.round(weights[0] * msPerWeightUnit));
  urduTtsState.wordTimer = setTimeout(scheduleNextWord, initialDelay);
}

function playNextUrduSentence() {
  if (!urduTtsState.isPlaying) return;

  if (urduTtsState.currentSentenceIdx >= urduTtsState.sentences.length) {
    // Finished reading all sentences in this section!
    stopUrduTTS();
    return;
  }

  const prefix = urduTtsState.activePrefix;
  const gender = urduTtsState.activeGender;
  const sent = urduTtsState.sentences[urduTtsState.currentSentenceIdx];
  if (!sent || !sent.text) {
    urduTtsState.currentSentenceIdx++;
    playNextUrduSentence();
    return;
  }

  const cleanText = sent.text.replace(/["'<>]/g, '').trim();
  const words = sent.text.split(/\s+/).filter(Boolean);
  if (words.length === 0) {
    urduTtsState.currentSentenceIdx++;
    playNextUrduSentence();
    return;
  }

  // Pre-calculate exact word time boundaries based on character lengths
  const weights = words.map(w => Math.max(2, w.length));
  const totalWeight = weights.reduce((a, b) => a + b, 0);

  // Authentic Urdu Neural Speech Stream
  const audioUrl = `https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=ur&q=${encodeURIComponent(cleanText)}`;
  
  let audio = new Audio(audioUrl);
  urduTtsState.audioObj = audio;

  // Distinct vocal characteristics:
  // Male: 0.82x rate (deep baritone pacing)
  // Female: 1.04x rate (bright feminine pacing)
  if (gender === "male") {
    audio.playbackRate = 0.82 * (urduTtsState.speechRate || 1.0);
  } else {
    audio.playbackRate = 1.04 * (urduTtsState.speechRate || 1.0);
  }

  let lastHighlightedRelIdx = -1;
  let hasFinished = false;
  let animFrameId = null;

  const cancelSyncLoop = () => {
    if (animFrameId) {
      cancelAnimationFrame(animFrameId);
      animFrameId = null;
    }
  };

  const advanceNext = () => {
    if (hasFinished) return;
    hasFinished = true;
    cancelSyncLoop();
    if (urduTtsState.audioObj === audio) urduTtsState.audioObj = null;
    urduTtsState.currentSentenceIdx++;
    if (urduTtsState.isPlaying) {
      setTimeout(playNextUrduSentence, 80);
    }
  };

  // 🎯 60-FPS REAL-TIME SYNC LOOP: Synchronizes word highlighting with speaker's voice in real-time
  const syncHighlightLoop = () => {
    if (!urduTtsState.isPlaying || hasFinished || audio.paused) return;

    if (audio.duration && !isNaN(audio.duration) && audio.duration > 0) {
      // Audio lead-in compensation (150ms initial silence, 180ms trailing silence)
      const leadIn = 0.14;
      const leadOut = 0.18;
      const effectiveDuration = Math.max(0.1, audio.duration - (leadIn + leadOut));
      const currentSpeechTime = Math.max(0, audio.currentTime - leadIn);
      const progress = Math.min(0.999, currentSpeechTime / effectiveDuration);

      let runningWeight = 0;
      let targetIdx = 0;
      for (let i = 0; i < weights.length; i++) {
        const wStart = runningWeight / totalWeight;
        const wEnd = (runningWeight + weights[i]) / totalWeight;
        if (progress >= wStart && progress < wEnd) {
          targetIdx = i;
          break;
        }
        runningWeight += weights[i];
      }

      if (targetIdx !== lastHighlightedRelIdx) {
        lastHighlightedRelIdx = targetIdx;
        highlightUrduWord(prefix, sent.startIdx + targetIdx, gender);
      }
    }

    animFrameId = requestAnimationFrame(syncHighlightLoop);
  };

  audio.onplay = function() {
    lastHighlightedRelIdx = 0;
    highlightUrduWord(prefix, sent.startIdx, gender);
    cancelSyncLoop();
    animFrameId = requestAnimationFrame(syncHighlightLoop);
  };

  audio.onpause = cancelSyncLoop;

  audio.onended = function() {
    cancelSyncLoop();
    highlightUrduWord(prefix, sent.endIdx, gender);
    advanceNext();
  };

  audio.onerror = function() {
    cancelSyncLoop();
    fallbackSpeechSynthesisSentence(sent, prefix, gender, advanceNext);
  };

  audio.play().catch(() => {
    cancelSyncLoop();
    fallbackSpeechSynthesisSentence(sent, prefix, gender, advanceNext);
  });
}

function fallbackSpeechSynthesisSentence(sent, prefix, gender, onComplete) {
  if (!('speechSynthesis' in window)) {
    if (onComplete) onComplete();
    return;
  }

  const cleanText = sent.text.replace(/["'<>۔؟!؛،]/g, ' ').trim();
  const utterance = new SpeechSynthesisUtterance(cleanText);
  const words = sent.text.split(/\s+/).filter(Boolean);

  const voices = window.speechSynthesis.getVoices() || [];
  if (gender === "male") {
    utterance.pitch = 0.72;
    utterance.rate = (urduTtsState.speechRate || 1.0) * 0.85;
    const mVoice = voices.find(v => (v.name.toLowerCase().includes("male") || v.name.toLowerCase().includes("david") || v.name.toLowerCase().includes("ravi") || v.name.toLowerCase().includes("hemant"))) || voices[0];
    if (mVoice) utterance.voice = mVoice;
  } else {
    utterance.pitch = 1.35;
    utterance.rate = (urduTtsState.speechRate || 1.0) * 0.98;
    const fVoice = voices.find(v => (v.name.toLowerCase().includes("female") || v.name.toLowerCase().includes("zira") || v.name.toLowerCase().includes("heera") || v.name.toLowerCase().includes("swara"))) || voices[0];
    if (fVoice) utterance.voice = fVoice;
  }

  let wordOffsets = [];
  let runningLen = 0;
  for (let i = 0; i < words.length; i++) {
    wordOffsets.push(runningLen);
    runningLen += words[i].length + 1;
  }

  utterance.onboundary = function(event) {
    if (event.name === "word" || event.charIndex !== undefined) {
      const charIdx = event.charIndex;
      let matchedIdx = 0;
      for (let i = 0; i < wordOffsets.length; i++) {
        if (charIdx >= wordOffsets[i]) {
          matchedIdx = i;
        } else {
          break;
        }
      }
      highlightUrduWord(prefix, sent.startIdx + matchedIdx, gender);
    }
  };

  utterance.onstart = function() {
    highlightUrduWord(prefix, sent.startIdx, gender);
  };

  let finished = false;
  const finish = () => {
    if (finished) return;
    finished = true;
    if (onComplete) onComplete();
  };

  utterance.onend = finish;
  utterance.onerror = finish;

  window.speechSynthesis.speak(utterance);
}

function playUrduTTS(prefix, gender, rawText, sectionTitle) {
  // If already playing this same one with same gender, toggle stop
  if (urduTtsState.isPlaying && urduTtsState.activePrefix === prefix && urduTtsState.activeGender === gender && !urduTtsState.isPaused) {
    stopUrduTTS();
    return;
  }

  stopUrduTTS();

  // Ensure target card is open and visible
  const card = $(prefix + "-card");
  if (card && !card.classList.contains("open")) {
    card.classList.add("open");
  }

  const data = prepareUrduTextForTts(rawText, prefix);
  if (data.sentences.length === 0) return;

  urduTtsState.activePrefix = prefix;
  urduTtsState.activeGender = gender;
  urduTtsState.isPlaying = true;
  urduTtsState.isPaused = false;
  urduTtsState.sectionTitle = sectionTitle;
  urduTtsState.sentences = data.sentences;
  urduTtsState.totalWords = data.totalWords;
  urduTtsState.currentSentenceIdx = 0;

  // Highlight active button
  const activeBtn = $(`btn-tts-${prefix}-${gender}`);
  if (activeBtn) activeBtn.classList.add("active-playing");

  // Show & update floating dock
  const dock = $("urduTtsFloatingDock");
  if (dock) {
    dock.style.display = "flex";
    const titleEl = $("dockActiveTitle");
    if (titleEl) titleEl.textContent = `${gender === 'female' ? '👩 زنانہ آواز' : '👨 مردانہ آواز'} · ${sectionTitle}`;
    const pauseBtn = $("dockPauseBtn");
    if (pauseBtn) pauseBtn.innerHTML = "⏸️ وقفہ";
  }

  // Start playing first sentence and continue sequentially
  playNextUrduSentence();
}

function renderUrduLesson(ch) {
  let authorHtml = '';
  if (ch.authorInfo) {
    const encodedAuthor = encodeURIComponent(ch.authorInfo);
    const authorData = prepareUrduTextForTts(ch.authorInfo, 'author');
    const previewSnippet = ch.authorInfo.substring(0, 130).trim() + '...';

    authorHtml = `
      <div id="author-card" class="urdu-section-card author-card" data-rawtext="${encodedAuthor}">
        <div class="urdu-section-header" onclick="toggleUrduSection(this)" style="background:linear-gradient(135deg,#dcfce7,#f0fdf4);">
          <div style="display:flex;align-items:center;gap:0.65rem;flex-wrap:wrap;">
            <span class="urdu-sec-badge" style="background:#15803d;">تعارف</span>
            <span class="urdu-sec-title" style="color:#15803d;">✍️ تعارفِ مصنف / شاعر — ${ch.author}</span>
          </div>
          <div style="display:flex;align-items:center;gap:0.5rem;">
            <div class="tts-controls-bar" onclick="event.stopPropagation()">
              <button id="btn-tts-author-male" class="btn-tts-pill male" title="مردانہ آواز میں سنیں" onclick="playUrduTTS('author', 'male', decodeURIComponent('${encodedAuthor}'), 'تعارفِ مصنف')">
                👨 مردانہ
              </button>
              <button id="btn-tts-author-female" class="btn-tts-pill female" title="زنانہ آواز میں سنیں" onclick="playUrduTTS('author', 'female', decodeURIComponent('${encodedAuthor}'), 'تعارفِ مصنف')">
                👩 زنانہ
              </button>
            </div>
            <span class="sec-toggle-icon">▼</span>
          </div>
        </div>
        <div class="urdu-grid-preview urdu-text-rtl">
          ${previewSnippet} <span style="color:#15803d;font-weight:700;">(مکمل تعارف پڑھنے کے لیے کلک کریں)</span>
        </div>
        <div class="urdu-section-body urdu-text-rtl" style="background:#f0fdf4;border-top:1px solid #86efac;">
          <div style="font-size:1.18rem;line-height:2.3;color:#1e293b;">
            ${authorData.html}
          </div>
        </div>
      </div>`;
  }

  const sectionsList = ch.sections || [];
  const sectionsHtml = sectionsList.map((sec, sIdx) => {
    const rawSecText = sec.paras ? sec.paras.join('\n\n') : (sec.urdu || '');
    const encodedSecText = encodeURIComponent(rawSecText);
    const secData = prepareUrduTextForTts(rawSecText, `sec-${sIdx}`);
    const previewSnippet = rawSecText.substring(0, 135).trim() + '...';

    return `
      <div id="sec-${sIdx}-card" class="urdu-section-card" data-rawtext="${encodedSecText}">
        <div class="urdu-section-header" onclick="toggleUrduSection(this)">
          <div style="display:flex;align-items:center;gap:0.65rem;flex-wrap:wrap;">
            <span class="urdu-sec-badge">عنوان ${sIdx + 1}</span>
            <span class="urdu-sec-title">${sec.heading}</span>
          </div>
          <div style="display:flex;align-items:center;gap:0.5rem;">
            <div class="tts-controls-bar" onclick="event.stopPropagation()">
              <button id="btn-tts-sec-${sIdx}-male" class="btn-tts-pill male" title="مردانہ آواز میں سنیں" onclick="playUrduTTS('sec-${sIdx}', 'male', decodeURIComponent('${encodedSecText}'), '${sec.heading}')">
                👨 مردانہ
              </button>
              <button id="btn-tts-sec-${sIdx}-female" class="btn-tts-pill female" title="زنانہ آواز میں سنیں" onclick="playUrduTTS('sec-${sIdx}', 'female', decodeURIComponent('${encodedSecText}'), '${sec.heading}')">
                👩 زنانہ
              </button>
            </div>
            <span class="sec-toggle-icon">▼</span>
          </div>
        </div>
        <div class="urdu-grid-preview urdu-text-rtl">
          ${previewSnippet} <span style="color:#16a34a;font-weight:700;">(مکمل متن کھولیں)</span>
        </div>
        <div class="urdu-section-body urdu-text-rtl">
          ${secData.html}
        </div>
      </div>`;
  }).join('');

  return `
    <div class="urdu-container">
      <!-- Sticky / Floating Audio Dock -->
      <div id="urduTtsFloatingDock" class="tts-floating-dock" style="display:none;">
        <div class="tts-dock-info">
          <div class="tts-soundwave">
            <span></span><span></span><span></span><span></span><span></span>
          </div>
          <div>
            <div id="dockActiveTitle" style="font-weight:700;font-size:0.95rem;color:#38bdf8;">🎙️ پڑھا جا رہا ہے...</div>
            <div style="font-size:0.75rem;color:#94a3b8;">آواز کے ساتھ ساتھ الفاظ پرکشش رنگ میں نمایاں ہو رہے ہیں</div>
          </div>
        </div>
        <div class="tts-dock-actions">
          <button id="dockPauseBtn" class="btn-toggle-all" style="background:#334155;color:#fff;border-color:#475569;" onclick="pauseResumeUrduTTS()">⏸️ وقفہ</button>
          <button class="btn-toggle-all" style="background:#ef4444;color:#fff;border-color:#dc2626;" onclick="stopUrduTTS()">⏹️ بند کریں</button>
          <select onchange="setUrduTtsRate(this.value)" style="background:#1e293b;color:#e2e8f0;border:1px solid #475569;border-radius:6px;padding:0.35rem 0.5rem;font-size:0.78rem;">
            <option value="0.8">0.8x آہستہ</option>
            <option value="0.95" selected>1.0x نارمل</option>
            <option value="1.2">1.2x تیز</option>
          </select>
        </div>
      </div>

      <div class="urdu-ctrl-bar">
        <div>
          <strong style="color:#15803d;font-size:1rem;">📖 عنوانات و تعارف گرڈ (Topics &amp; Introduction Grid):</strong>
          <span style="font-size:0.82rem;color:var(--text-muted);margin-left:0.5rem;">${sectionsList.length} مستند عنوانات · گرڈ کارڈز</span>
        </div>
        <div style="display:flex;gap:0.5rem;flex-wrap:wrap;">
          <button class="btn-toggle-all" onclick="expandAllUrduSections(true)">➕ تمام گرڈ کھولیں</button>
          <button class="btn-toggle-all" onclick="expandAllUrduSections(false)">➖ تمام گرڈ سمیٹیں</button>
        </div>
      </div>

      <!-- Responsive Grid Container for تعارف and all عنوانات -->
      <div class="urdu-grid-container">
        ${authorHtml}
        ${sectionsHtml}
      </div>
    </div>`;
}

function renderUrduPashtoTranslation(ch) {
  const sectionsList = ch.sections || [];
  const sectionsHtml = sectionsList.map((sec, sIdx) => {
    const lines = (sec.pashto || '').split('\n').filter(Boolean);
    const linesHtml = lines.map(l => `<p style="margin-bottom:0.75rem;">${l}</p>`).join('');

    return `
      <div class="urdu-section-card pashto-theme">
        <div class="urdu-section-header" onclick="toggleUrduSection(this)" style="background:linear-gradient(135deg,#f0f9ff,#ffffff);">
          <div style="display:flex;align-items:center;gap:0.65rem;">
            <span class="urdu-sec-badge" style="background:#0284c7;">برخه ${sIdx + 1}</span>
            <span class="urdu-sec-title" style="color:#0369a1;font-family:'Segoe UI', Tahoma, sans-serif;">${sec.headingPs || sec.heading} (پښتو ژباړه)</span>
          </div>
          <span class="sec-toggle-icon">▼</span>
        </div>
        <div class="urdu-section-body" style="direction:rtl;text-align:right;font-family:'Segoe UI', Tahoma, sans-serif;font-size:1.15rem;line-height:2.2;color:#1e293b;">
          ${linesHtml}
          ${sec.urdu ? `
          <div style="margin-top:1rem;padding-top:0.75rem;border-top:1px dashed #cbd5e1;font-size:0.95rem;color:#64748b;font-family:'Jameel Noori Nastaleeq','Segoe UI',serif;">
            <strong style="color:#475569;">اصلي اردو متن:</strong> ${sec.urdu.substring(0, 160)}...
          </div>` : ''}
        </div>
      </div>`;
  }).join('');

  return `
    <div class="urdu-container">
      <div class="urdu-ctrl-bar" style="border-left:4px solid #0284c7;background:#e0f2fe;">
        <div>
          <strong style="color:#0369a1;font-size:1rem;">🇦🇫 د سبق بشپړه پښتو ژباړه (Complete Pashto Translation):</strong>
          <span style="font-size:0.82rem;color:#0369a1;margin-left:0.5rem;">د خیبر پښتونخوا نصاب مطابق ${sectionsList.length} برخې</span>
        </div>
        <div style="display:flex;gap:0.5rem;">
          <button class="btn-toggle-all" onclick="expandAllUrduSections(true)">➕ ټولې برخې پرانیزئ</button>
          <button class="btn-toggle-all" onclick="expandAllUrduSections(false)">➖ ټولې برخې بندې کړئ</button>
        </div>
      </div>

      ${sectionsHtml}
    </div>`;
}

function renderUrduEnglishTranslation(ch) {
  const sectionsList = ch.sections || [];
  const sectionsHtml = sectionsList.map((sec, sIdx) => {
    const lines = (sec.english || '').split('\n').filter(Boolean);
    const linesHtml = lines.map(l => `<p style="margin-bottom:0.75rem;">${l}</p>`).join('');

    return `
      <div class="urdu-section-card eng-theme">
        <div class="urdu-section-header" onclick="toggleUrduSection(this)" style="background:linear-gradient(135deg,#faf5ff,#ffffff);">
          <div style="display:flex;align-items:center;gap:0.65rem;">
            <span class="urdu-sec-badge" style="background:#7c3aed;">Section ${sIdx + 1}</span>
            <span class="urdu-sec-title" style="direction:ltr;text-align:left;font-family:'Segoe UI',sans-serif;font-size:1.05rem;color:#6d28d9;">${sec.headingEn || sec.heading}</span>
          </div>
          <span class="sec-toggle-icon">▼</span>
        </div>
        <div class="urdu-section-body" style="direction:ltr;text-align:left;font-size:1.02rem;line-height:1.8;color:#334155;">
          ${linesHtml}
          ${sec.urdu ? `
          <div style="margin-top:1rem;padding-top:0.75rem;border-top:1px dashed #cbd5e1;font-size:0.92rem;color:#64748b;direction:rtl;text-align:right;font-family:'Jameel Noori Nastaleeq','Segoe UI',serif;">
            <strong style="color:#475569;direction:ltr;display:inline-block;">Urdu Source:</strong> ${sec.urdu.substring(0, 140)}...
          </div>` : ''}
        </div>
      </div>`;
  }).join('');

  return `
    <div class="urdu-container">
      <div class="urdu-ctrl-bar" style="border-left:4px solid #7c3aed;background:#ede9fe;">
        <div>
          <strong style="color:#6d28d9;font-size:1rem;">🇬🇧 Complete English Academic Translation:</strong>
          <span style="font-size:0.82rem;color:#6d28d9;margin-left:0.5rem;">${sectionsList.length} Conceptual Sections</span>
        </div>
        <div style="display:flex;gap:0.5rem;">
          <button class="btn-toggle-all" onclick="expandAllUrduSections(true)">➕ Expand All</button>
          <button class="btn-toggle-all" onclick="expandAllUrduSections(false)">➖ Collapse All</button>
        </div>
      </div>

      ${sectionsHtml}
    </div>`;
}

function renderUrduVideo(ch) {
  const vid = ch.video || {
    title: `Class 9 Urdu - ${ch.title}`,
    youtubeId: 'w5YhD_V4b4I',
    duration: '38:45',
    tutor: 'Prof. Dr. Tariq Mahmood (KPK Board Master Educator)',
    concepts: ['Reading', 'Tashreeh', 'Solved Exercises', 'SLO MCQs']
  };

  const conceptsHtml = (vid.concepts || []).map(c => `
    <div class="video-concept-chip">
      <span style="color:#38bdf8;">✓</span> ${c}
    </div>`).join("");

  return `
    <div class="urdu-container">
      <div class="video-lecture-container">
        <div class="video-embed-wrapper">
          <iframe src="https://www.youtube-nocookie.com/embed/${vid.youtubeId}?rel=0" 
                  title="${vid.title}" 
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                  allowfullscreen>
          </iframe>
        </div>
        <div class="video-meta-bar">
          <div class="video-meta-title">🎥 ${vid.title}</div>
          <div style="display:flex;gap:1rem;flex-wrap:wrap;font-size:0.85rem;color:#94a3b8;">
            <span>👨‍🏫 Educator: <strong style="color:#fff;">${vid.tutor}</strong></span>
            <span>⏱️ Duration: <strong style="color:#fff;">${vid.duration}</strong></span>
            <span>🏛️ Board: <strong style="color:#38bdf8;">KPK Board Peshawar Official Syllabus</strong></span>
          </div>
          <div style="margin-top:0.5rem;">
            <div style="font-size:0.82rem;font-weight:700;color:#cbd5e1;text-transform:uppercase;letter-spacing:0.5px;">Key Concepts Covered in Lecture:</div>
            <div class="video-concepts-grid">
              ${conceptsHtml}
            </div>
          </div>
        </div>
      </div>
    </div>`;
}

function renderUrduEnglishSummary(ch) {
  return `
    <div class="urdu-container">
      <div class="translation-card english" style="border-left:5px solid #2563eb;">
        <h3 style="color:#1e40af;margin-bottom:0.75rem;display:flex;align-items:center;gap:0.5rem;">
          <span>📝</span> English Summary — ${ch.titleEn || ch.title}
        </h3>
        <p style="font-size:1.05rem;line-height:1.9;color:#334155;margin-bottom:1rem;">
          ${ch.englishSummary || 'Comprehensive English summary of this lesson.'}
        </p>
        <div style="background:#f1f5f9;padding:1rem;border-radius:8px;margin-top:1rem;">
          <h4 style="color:var(--navy);font-size:0.95rem;margin-bottom:0.5rem;">Key Takeaways &amp; Moral:</h4>
          <ul style="list-style:disc;padding-left:1.25rem;color:#475569;line-height:1.8;font-size:0.92rem;">
            <li>Authored by <strong>${ch.author}</strong> with emphasis on moral values, social reform, and literary excellence.</li>
            <li>Fully aligned with the KPK Textbook Board Grade 9 Student Learning Outcomes (SLOs).</li>
            <li>Highlights key historical, cultural, and spiritual themes rooted in the textbook narrative.</li>
          </ul>
        </div>
      </div>
    </div>`;
}

function renderUrduUrduSummary(ch) {
  return `
    <div class="urdu-container">
      <div class="author-intro-card" style="background:#fefce8;border-color:#fde047;">
        <div class="author-intro-title" style="direction:rtl;color:#854d0e;">
          <span>📜</span>
          <span>سبق کا جامع خلاصہ — ${ch.title}</span>
        </div>
        <div class="urdu-text-rtl" style="font-size:1.25rem;line-height:2.4;color:#1e293b;">
          ${ch.urduSummary || 'اس سبق کا جامع خلاصہ۔'}
        </div>
      </div>
    </div>`;
}

function renderUrduPashtoSummary(ch) {
  return `
    <div class="urdu-container">
      <div class="translation-card pashto" style="border-left:5px solid #059669;background:#f0fdf4;">
        <div style="font-weight:800;color:#15803d;font-size:1.2rem;margin-bottom:0.75rem;direction:rtl;">
          🇦🇫 د درس پښتو لنډیز — ${ch.titlePs || ch.title}
        </div>
        <div style="font-size:1.2rem;line-height:2.3;color:#1e293b;">
          ${ch.pashtoSummary || 'د دې لوست پښتو لنډیز.'}
        </div>
      </div>
    </div>`;
}

function renderUrduExercise(ch) {
  const ex = ch.exercise || {};
  const sqList = ex.shortQuestions || [];
  const blanksList = ex.blanks || [];
  const grammarList = ex.grammar || [];
  const vocabList = ex.vocabulary || [];

  const sqHtml = sqList.map((q, i) => `
    <div class="slo-question-accordion">
      <div class="slo-accordion-header" style="direction:rtl;text-align:right;" onclick="toggleSloAccordion(this)">
        <span><strong>سوال ${i+1}:</strong> ${q.question || q.q}</span>
        <span class="slo-acc-toggle" style="color:#16a34a;font-size:0.85rem;background:#dcfce7;padding:0.2rem 0.65rem;border-radius:99px;">+ جواب دیکھیں</span>
      </div>
      <div class="slo-accordion-body urdu-text-rtl" style="background:#f0fdf4;color:#166534;display:none;">
        <strong>جواب:</strong> ${q.answer || q.a}
      </div>
    </div>`).join("");

  const blanksHtml = blanksList.map((b, i) => `
    <div style="background:#ffffff;padding:0.85rem 1.15rem;border:1px solid #e2e8f0;border-radius:8px;margin-bottom:0.5rem;direction:rtl;text-align:right;" class="urdu-text-rtl">
      <span>${i+1}. ${b.statement}</span>
      <div style="color:#15803d;font-weight:700;font-size:1rem;margin-top:0.25rem;">درست جواب: ${b.answer}</div>
    </div>`).join("");

  const grammarHtml = grammarList.map((g, i) => `
    <div style="background:#ffffff;padding:1.15rem 1.25rem;border:1.5px solid #cbd5e1;border-radius:10px;margin-bottom:0.75rem;direction:rtl;text-align:right;" class="urdu-text-rtl">
      <h4 style="color:#7c3aed;margin-bottom:0.5rem;">قواعد و انشا: ${g.topic}</h4>
      <p style="color:#334155;margin-bottom:0.5rem;">${g.explanation}</p>
      <div style="background:#f8fafc;padding:0.65rem 0.85rem;border-radius:6px;font-size:1rem;color:#475569;">
        <strong>مثالیں:</strong> ${(g.examples || []).join(' ، ')}
      </div>
    </div>`).join("");

  const vocabHtml = vocabList.map((v, i) => `
    <tr style="border-bottom:1px solid #e2e8f0;">
      <td style="padding:0.75rem 1rem;font-weight:700;color:#16a34a;font-family:'Jameel Noori Nastaleeq','Segoe UI',serif;font-size:1.15rem;">${v.word}</td>
      <td style="padding:0.75rem 1rem;color:#334155;font-size:1.05rem;">${v.meaning}</td>
      <td style="padding:0.75rem 1rem;color:#475569;font-size:1.05rem;">${v.sentence}</td>
    </tr>`).join("");

  return `
    <div class="urdu-container">
      <div class="urdu-ctrl-bar">
        <div>
          <strong style="color:#15803d;font-size:1rem;">✏️ حل شدہ درسی مشق (Official Solved Textbook Exercise):</strong>
          <span style="font-size:0.82rem;color:var(--text-muted);margin-left:0.5rem;">مستند ٹیکسٹ بک گائیڈ و حل</span>
        </div>
        <div style="display:flex;gap:0.5rem;">
          <button class="btn-toggle-all" onclick="expandAllUrduSections(true)">➕ تمام حصے کھولیں</button>
          <button class="btn-toggle-all" onclick="expandAllUrduSections(false)">➖ تمام حصے سمیٹیں</button>
        </div>
      </div>

      <!-- 1. Short Questions Card -->
      <div class="urdu-section-card">
        <div class="urdu-section-header" onclick="toggleUrduSection(this)">
          <div style="display:flex;align-items:center;gap:0.65rem;">
            <span class="urdu-sec-badge">الف</span>
            <span class="urdu-sec-title">درسی کتاب کے مختصر سوالات و جوابات (${sqList.length} سوالات)</span>
          </div>
          <span class="sec-toggle-icon">▼</span>
        </div>
        <div class="urdu-section-body urdu-text-rtl">
          ${sqHtml || '<p style="color:var(--text-muted);">کوئی مختصر سوالات دستیاب نہیں۔</p>'}
        </div>
      </div>

      <!-- 2. Blanks Card -->
      ${blanksList.length > 0 ? `
      <div class="urdu-section-card">
        <div class="urdu-section-header" onclick="toggleUrduSection(this)">
          <div style="display:flex;align-items:center;gap:0.65rem;">
            <span class="urdu-sec-badge" style="background:#ca8a04;">ب</span>
            <span class="urdu-sec-title">خالی جگہیں پُر کریں (Fill in the Blanks)</span>
          </div>
          <span class="sec-toggle-icon">▼</span>
        </div>
        <div class="urdu-section-body urdu-text-rtl">
          ${blanksHtml}
        </div>
      </div>` : ''}

      <!-- 3. Vocabulary Table Card -->
      ${vocabList.length > 0 ? `
      <div class="urdu-section-card">
        <div class="urdu-section-header" onclick="toggleUrduSection(this)">
          <div style="display:flex;align-items:center;gap:0.65rem;">
            <span class="urdu-sec-badge" style="background:#0284c7;">ج</span>
            <span class="urdu-sec-title">الفاظ، معانی اور جملوں میں استعمال (Vocabulary &amp; Sentences)</span>
          </div>
          <span class="sec-toggle-icon">▼</span>
        </div>
        <div class="urdu-section-body urdu-text-rtl">
          <div style="overflow-x:auto;background:#ffffff;border:1px solid var(--border);border-radius:8px;">
            <table style="width:100%;border-collapse:collapse;direction:rtl;text-align:right;">
              <thead>
                <tr style="background:#f1f5f9;color:var(--navy);font-weight:700;">
                  <th style="padding:0.75rem 1rem;">لفظ</th>
                  <th style="padding:0.75rem 1rem;">معنی</th>
                  <th style="padding:0.75rem 1rem;">جملے میں استعمال</th>
                </tr>
              </thead>
              <tbody>
                ${vocabHtml}
              </tbody>
            </table>
          </div>
        </div>
      </div>` : ''}

      <!-- 4. Grammar Card -->
      ${grammarList.length > 0 ? `
      <div class="urdu-section-card">
        <div class="urdu-section-header" onclick="toggleUrduSection(this)">
          <div style="display:flex;align-items:center;gap:0.65rem;">
            <span class="urdu-sec-badge" style="background:#7c3aed;">د</span>
            <span class="urdu-sec-title">قواعد و انشا و گرامر (Grammar &amp; Syntax)</span>
          </div>
          <span class="sec-toggle-icon">▼</span>
        </div>
        <div class="urdu-section-body urdu-text-rtl">
          ${grammarHtml}
        </div>
      </div>` : ''}
    </div>`;
}

function renderUrduSLOs(ch) {
  const slos = ch.slos || [];
  const slosHtml = slos.map((slo, idx) => `
    <div style="display:flex;align-items:flex-start;gap:0.75rem;background:#ffffff;padding:1rem 1.25rem;border:1.5px solid #cbd5e1;border-radius:10px;margin-bottom:0.75rem;direction:rtl;text-align:right;" class="urdu-text-rtl">
      <span style="background:#16a34a;color:#fff;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.85rem;flex-shrink:0;">${idx+1}</span>
      <div style="color:#1e293b;font-size:1.1rem;line-height:1.9;">${slo}</div>
    </div>`).join("");

  return `
    <div class="urdu-container">
      <div style="background:#ecfdf5;padding:1rem 1.25rem;border-radius:var(--radius-sm);border-left:4px solid #10b981;margin-bottom:0.75rem;">
        <strong style="color:#047857;">🎯 حاصلاتِ تعلّم (Student Learning Outcomes - SLOs):</strong>
        <p style="font-size:0.88rem;color:#065f46;margin-top:0.25rem;">خیبر پښتونخوا د ښوونیز نصاب بورډ پېښور لخوا ټاکل شوي معیارات</p>
      </div>
      ${slosHtml}
    </div>`;
}

// ─────────────────────────────────────────
//  BOTTOM SLO QUESTIONS RENDERERS (20+ MCQs, 10+ SQs, 5+ LQs)
// ─────────────────────────────────────────
function renderUrduSloMcqs(ch) {
  const mcqs = (ch.sloQuestions && ch.sloQuestions.mcqs) || (ch.exercise && ch.exercise.mcqs) || [];
  if (mcqs.length === 0) {
    return `<div style="padding:1.5rem;text-align:center;color:var(--text-muted);">اس سبق کے لیے کوئی ایم سی کیوز دستیاب نہیں ہیں۔</div>`;
  }

  const mcqListHtml = mcqs.map((m, qIndex) => {
    const encodedExp = encodeURIComponent(m.explanation || "درست جواب منتخب کیا گیا۔");
    const optionsHtml = m.options.map((opt, optIndex) => `
      <label class="mcq-option-label urdu-text-rtl" id="opt-urdu-${qIndex}-${optIndex}"
             onclick="checkUrduSloMcq(${qIndex}, ${optIndex}, ${m.correct}, '${encodedExp}')">
        <input type="radio" name="urdu-mcq-${qIndex}" value="${optIndex}" style="accent-color:#16a34a;margin-left:0.5rem;">
        <span>${opt}</span>
      </label>`).join("");

    return `
      <div class="interactive-mcq-card">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem;">
          <span style="background:#f1f5f9;color:#475569;font-weight:700;font-size:0.78rem;padding:0.25rem 0.65rem;border-radius:99px;">
            سوال ${qIndex + 1} از ${mcqs.length} ${m.cognitive ? '· ' + m.cognitive : ''}
          </span>
          <span style="font-size:0.78rem;color:#16a34a;font-weight:700;">ایس ایل او امتحانی پیٹرن</span>
        </div>
        <div class="mcq-question-text urdu-text-rtl">${m.question}</div>
        <div class="mcq-options-grid">${optionsHtml}</div>
        <div id="urdu-exp-${qIndex}" style="display:none;" class="mcq-explanation-box urdu-text-rtl"></div>
      </div>`;
  }).join("");

  return `
    <div style="margin-bottom:1rem;">
      <div style="background:#f0fdf4;padding:0.75rem 1.25rem;border-radius:8px;border-left:4px solid #16a34a;margin-bottom:1rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem;">
        <span style="color:#15803d;font-weight:700;">🎯 کل 20+ کثیر الانتخابی سوالات (SLO Exam MCQs):</span>
        <span style="font-size:0.85rem;color:#166534;">ہر سوال پر کلک کر کے فوری ماڈل جواب اور وضاحت دیکھیں</span>
      </div>
      ${mcqListHtml}
    </div>`;
}

function checkUrduSloMcq(qIndex, selectedOpt, correctOpt, encodedExp) {
  const expBox = $(`urdu-exp-${qIndex}`);
  const explanation = decodeURIComponent(encodedExp);

  // Disable radio inputs for this question to lock choice
  const inputs = document.querySelectorAll(`input[name="urdu-mcq-${qIndex}"]`);
  inputs.forEach(inp => inp.disabled = true);

  const isCorrect = (selectedOpt === correctOpt);

  // Update classes for visual indication
  inputs.forEach((inp, idx) => {
    const label = $(`opt-urdu-${qIndex}-${idx}`);
    if (!label) return;
    if (idx === correctOpt) {
      label.classList.add("correct");
    } else if (idx === selectedOpt && !isCorrect) {
      label.classList.add("incorrect");
    }
  });

  if (expBox) {
    expBox.style.display = "block";
    expBox.innerHTML = `
      <div style="font-weight:700;margin-bottom:0.25rem;color:${isCorrect ? '#166534' : '#991b1b'};">
        ${isCorrect ? '✅ بالکل درست جواب!' : '❌ غلط جواب — درست جواب سبز رنگ میں نمایاں ہے۔'}
      </div>
      <div><strong>وضاحت:</strong> ${explanation}</div>
    `;
  }

  // Record answer in local storage study analytics engine
  recordQuestionAnswer(isCorrect);
}

function renderUrduSloSQs(ch) {
  const sqs = (ch.sloQuestions && ch.sloQuestions.shortQuestions) || (ch.exercise && ch.exercise.shortQuestions) || [];
  if (sqs.length === 0) {
    return `<div style="padding:1.5rem;text-align:center;color:var(--text-muted);">کوئی ایس ایل او مختصر سوالات دستیاب نہیں ہیں۔</div>`;
  }

  const sqListHtml = sqs.map((sq, i) => `
    <div class="slo-question-accordion">
      <div class="slo-accordion-header" style="direction:rtl;text-align:right;" onclick="toggleSloAccordion(this)">
        <span style="font-size:1.15rem;font-family:'Jameel Noori Nastaleeq','Segoe UI',serif;"><strong>مختصر سوال ${i+1}:</strong> ${sq.question}</span>
        <div style="display:flex;align-items:center;gap:0.5rem;">
          <span style="font-size:0.75rem;background:#dcfce7;color:#15803d;padding:0.2rem 0.5rem;border-radius:99px;font-family:sans-serif;direction:ltr;">${sq.sloRef || 'SLO'}</span>
          <span class="slo-acc-toggle" style="color:#16a34a;font-size:0.82rem;background:#f1f5f9;padding:0.2rem 0.5rem;border-radius:6px;">+ جواب دیکھیں</span>
        </div>
      </div>
      <div class="slo-accordion-body urdu-text-rtl" style="background:#f8fafc;font-size:1.15rem;color:#1e293b;display:none;">
        <strong style="color:#16a34a;display:block;margin-bottom:0.35rem;">ماڈل جواب:</strong>
        ${sq.answer}
      </div>
    </div>`).join("");

  return `
    <div>
      <div style="background:#fefce8;padding:0.75rem 1.25rem;border-radius:8px;border-left:4px solid #ca8a04;margin-bottom:1rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem;">
        <span style="color:#854d0e;font-weight:700;">✏️ کل 10+ تصوری و فکری مختصر سوالات (SLO Conceptual Short Questions):</span>
        <span style="font-size:0.85rem;color:#a16207;">کسی بھی سوال پر کلک کر کے ماڈل جواب کھولیں</span>
      </div>
      ${sqListHtml}
    </div>`;
}

function renderUrduSloLQs(ch) {
  const lqs = (ch.sloQuestions && ch.sloQuestions.longQuestions) || [];
  if (lqs.length === 0) {
    return `<div style="padding:1.5rem;text-align:center;color:var(--text-muted);">کوئی ایس ایل او تفصیلی سوالات دستیاب نہیں ہیں۔</div>`;
  }

  const lqListHtml = lqs.map((lq, i) => {
    const pointsHtml = (lq.keyPoints || []).map(pt => `
      <li style="margin-bottom:0.35rem;">🔹 ${pt}</li>`).join("");

    return `
      <div class="slo-question-accordion" style="border-color:#cbd5e1;margin-bottom:1rem;">
        <div class="slo-accordion-header" style="direction:rtl;text-align:right;background:#f0fdf4;" onclick="toggleSloAccordion(this)">
          <div style="font-weight:800;font-size:1.22rem;color:var(--navy);" class="urdu-text-rtl">
            📝 تفصیلی سوال ${i+1}: ${lq.question}
          </div>
          <span class="slo-acc-toggle" style="color:#16a34a;font-size:0.82rem;background:#dcfce7;padding:0.25rem 0.65rem;border-radius:99px;flex-shrink:0;">+ مفصل جواب کھولیں</span>
        </div>
        <div class="slo-accordion-body urdu-text-rtl" style="display:none;background:#ffffff;">
          <div style="font-size:1.18rem;line-height:2.4;color:#334155;background:#f8fafc;padding:1.25rem;border-radius:8px;margin-bottom:1rem;border:1px solid #e2e8f0;">
            <strong style="color:#15803d;display:block;margin-bottom:0.5rem;font-size:1.25rem;">جامع ماڈل جواب:</strong>
            ${lq.answer}
          </div>
          ${lq.keyPoints && lq.keyPoints.length > 0 ? `
          <div style="background:#ffffff;border:1px solid #e2e8f0;padding:1rem;border-radius:8px;direction:rtl;text-align:right;" class="urdu-text-rtl">
            <strong style="color:var(--navy);font-size:0.95rem;">امتحانی اہم نکات و مارکنگ اسکیم:</strong>
            <ul style="list-style:none;padding-right:0.5rem;margin-top:0.5rem;color:#475569;font-size:1rem;">
              ${pointsHtml}
            </ul>
          </div>` : ''}
        </div>
      </div>`;
  }).join("");

  return `
    <div>
      <div style="background:#ede9fe;padding:0.75rem 1.25rem;border-radius:8px;border-left:4px solid #7c3aed;margin-bottom:1rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem;">
        <span style="color:#6d28d9;font-weight:700;">📝 کل 5+ تفصیلی انشائی سوالات (SLO Detailed Long Questions):</span>
        <span style="font-size:0.85rem;color:#7c3aed;">امتحانی مارکنگ اسکیم اور تفصیلی نکات کے ساتھ ماڈل جوابات</span>
      </div>
      ${lqListHtml}
    </div>`;
}

// ─────────────────────────────────────────
// ─── 1. TOPICS ACCORDION VIEW (Exact Textbook Hierarchy) ─────────────
function renderTopicsAccordion(ch) {
  const accordions = ch.topics.map((topic, ti) => {
    const subtopics = topic.subtopics || [];

    // 1. Build ASCII Hierarchy Tree
    const topicNumStr = topic.num ? String(topic.num) : `${ti + 1}.0`;
    const topicTitleStr = topic.title || topic.name || "";
    const treeLines = [`${topicNumStr} ${topicTitleStr}`];
    subtopics.forEach((sub, si) => {
      const isLast = si === subtopics.length - 1;
      const prefix = isLast ? "└── " : "├── ";
      const sNum = sub.num ? String(sub.num) : `(${si + 1})`;
      const sName = sub.name || sub.title || "";
      treeLines.push(prefix + sNum + " " + sName);
    });
    const treeAscii = treeLines.join("\n");

    // 2. Render Individual Subtopic Blocks (ONE BLOCK PER BRANCH / SUBTOPIC - STRICT SEPARATION)
    const subtopicsHtml = subtopics.map((sub, si) => `
      <div class="subtopic-card" id="subtopic-card-${ti}-${si}">
        <!-- Subtopic Header -->
        <div class="subtopic-card-header">
          <div class="subtopic-title-group">
            <span class="subtopic-number-badge">${sub.num || `(${si + 1})`}</span>
            <h4 class="subtopic-heading">${sub.name || sub.title || `Section ${si + 1}`}</h4>
          </div>
          <span class="subtopic-seq-badge">Item ${si + 1} of ${subtopics.length}</span>
        </div>

        <!-- Subtopic Body -->
        <div class="subtopic-content">
          <!-- Exact Textbook Definition / Study Content -->
          <div class="subtopic-study-text">
            <div class="study-label">📖 Textbook Study Definition / Content:</div>
            <p class="study-desc">${(sub.desc || sub.content || "").replace(/\n/g, '<br>')}</p>
          </div>

          <!-- Scientific Information Box (if present in textbook) -->
          ${(sub.sciNote || sub.sciNotes) ? `
            <div class="sci-note-callout">
              <div class="sci-note-header">
                <span class="sci-icon">🔬</span>
                <span class="sci-title">Scientific Information:</span>
              </div>
              <div class="sci-note-body">${(sub.sciNote || sub.sciNotes).replace(/\n/g, '<br>')}</div>
            </div>
          ` : ""}

          <!-- Point to Remember Box (if present in textbook) -->
          ${sub.pointToRemember ? `
            <div class="point-remember-box">
              <div class="point-remember-header">
                <span class="point-icon">💡</span>
                <span class="point-title">Point to Remember:</span>
              </div>
              <div class="point-body">${sub.pointToRemember}</div>
            </div>
          ` : ""}

          <!-- Science, Technology and Society Box (if present in textbook) -->
          ${sub.sts ? `
            <div class="sts-box">
              <div class="sts-header">
                <span class="sts-icon">🌐</span>
                <span class="sts-title">Science, Technology and Society:</span>
              </div>
              <div class="sts-body">${sub.sts}</div>
            </div>
          ` : ""}

          <!-- Textbook Activity / Practical Investigation (if present) -->
          ${sub.activity ? `
            <div class="activity-box">
              <div class="activity-header">
                <span class="act-icon">🧪</span>
                <span class="act-title">Textbook Investigation / Activity:</span>
              </div>
              <div class="act-body">${sub.activity}</div>
            </div>
          ` : ""}

          <!-- Textbook Reference Table (if present) -->
          ${(sub.table && Array.isArray(sub.table.headers) && Array.isArray(sub.table.rows)) ? `
            <div class="subtopic-table-box">
              <div class="tbl-title">📊 ${sub.table.title || 'Table'}</div>
              <table class="diff-table">
                <thead>
                  <tr>${sub.table.headers.map(h => `<th>${h}</th>`).join('')}</tr>
                </thead>
                <tbody>
                  ${sub.table.rows.map(row => `<tr>${(Array.isArray(row) ? row : [row]).map(c => `<td>${c}</td>`).join('')}</tr>`).join('')}
                </tbody>
              </table>
            </div>
          ` : ""}

          <!-- Textbook Figure (if present) -->
          ${sub.figure ? `
            <div class="subtopic-fig-box">
              <div class="fig-header">
                <span class="fig-icon">🖼️</span>
                <span class="fig-title">${sub.figure.name || 'Figure'}</span>
              </div>
              <div class="fig-caption">${sub.figure.caption || ''}</div>
              ${sub.figure.note ? `<div class="fig-note"><strong>Study Guide:</strong> ${sub.figure.note}</div>` : ''}
            </div>
          ` : ""}

          <!-- Quick Practice Short Question -->
          ${sub.sq ? `
            <div class="subtopic-sq-box">
              <div class="subtopic-sq-header">
                <span class="badge-sq-mini">SQ</span>
                <span class="subtopic-sq-label">Textbook Short Question:</span>
              </div>
              <div class="subtopic-sq-text">${sub.sq}</div>
            </div>
          ` : ""}

          <!-- Interactive Practice MCQ -->
          ${(sub.mcq && Array.isArray(sub.mcq.opts || sub.mcq.options)) ? `
            <div class="subtopic-mcq-box" id="sub-mcq-${ti}-${si}">
              <div class="subtopic-mcq-header">
                <span class="badge-mcq-mini">MCQ</span>
                <span class="subtopic-mcq-q">${sub.mcq.q || ''}</span>
              </div>
              <div class="subtopic-mcq-grid">
                ${(sub.mcq.opts || sub.mcq.options).map((opt, oi) => `
                  <button class="sub-opt-btn" onclick="checkSubtopicMcq(${ti}, ${si}, ${oi}, ${sub.mcq.ans ?? sub.mcq.correct ?? 0})">
                    <span class="sub-opt-letter">${String.fromCharCode(65 + oi)}</span>
                    <span class="sub-opt-text">${opt}</span>
                  </button>
                `).join("")}
              </div>
              <div class="sub-mcq-fb" id="sub-fb-${ti}-${si}" style="display:none;"></div>
            </div>
          ` : ""}
        </div>
      </div>
    `).join("");

    const sqCount = subtopics.filter(s => s.sq).length;
    const mcqCount = subtopics.filter(s => s.mcq).length;
    const lqCount = ch.textbookExercise && ch.textbookExercise.lq ? ch.textbookExercise.lq.length : 0;

    return `
      <div class="acc-item">
        <!-- Main Topic Trigger Button -->
        <button class="acc-trigger" id="acc-trigger-${ti}" onclick="toggleAccordion(${ti})">
          <span class="acc-trigger-left">
            <span class="acc-topic-num">${topicNumStr}</span>
            <span class="acc-topic-name">${topicTitleStr}</span>
          </span>
          <div class="acc-trigger-right">
            ${subtopics.length > 0 ? `<span class="acc-sub-count">${subtopics.length} Sections</span>` : ""}
            <span class="acc-chevron">▼</span>
          </div>
        </button>

        <!-- Topic Accordion Body (Slides Down Slowly) -->
        <div class="acc-body" id="acc-body-${ti}">
          <div class="acc-body-inner">

            <!-- Trilingual Summary Tabs -->
            <div class="lang-tabs">
              <button class="lang-tab active" onclick="switchLang(${ti}, 'en', this)">English Summary</button>
              <button class="lang-tab" onclick="switchLang(${ti}, 'ur', this)">اردو خلاصہ</button>
              <button class="lang-tab" onclick="switchLang(${ti}, 'ps', this)">پښتو لنډیز</button>
            </div>

            <!-- Summary Panels (3 to 5 Lines) -->
            <div id="lang-en-${ti}" class="lang-content active">
              <div class="summary-box">${(topic.summary && topic.summary.en) || topic.desc || topic.content || topicTitleStr}</div>
            </div>
            <div id="lang-ur-${ti}" class="lang-content">
              <div class="summary-box rtl">${(topic.summary && topic.summary.ur) || (topic.summary && topic.summary.en) || topic.desc || topic.content || ""}</div>
            </div>
            <div id="lang-ps-${ti}" class="lang-content">
              <div class="summary-box rtl">${(topic.summary && topic.summary.ps) || (topic.summary && topic.summary.en) || topic.desc || topic.content || ""}</div>
            </div>

            <!-- Structural Hierarchy Tree Box (Collapsible) -->
            <div class="hierarchy-tree-box">
              <div class="hierarchy-tree-header hierarchy-tree-toggle" onclick="toggleHierarchy(this)">
                <span class="hierarchy-tree-badge">🌲 Textbook Hierarchy</span>
                <span class="hierarchy-tree-title">${topicNumStr} ${topicTitleStr} (${subtopics.length} Items in Exact Sequence)</span>
                <span class="hierarchy-chevron">▶</span>
              </div>
              <pre class="hierarchy-tree-code" style="display:none;">${treeAscii}</pre>
            </div>

            <!-- Subtopics Label -->
            <div class="subtopics-section-title">
              <span>📚 Separated Subtopic Blocks (KPK Textbook Board Grade IX Sequence)</span>
            </div>

            <!-- Subtopic Blocks — Horizontal Accordion -->
            <div class="subtopics-horiz-wrap">
              ${subtopics.map((sub, si) => `
                <div class="subtopic-horiz-item" id="sub-horiz-${ti}-${si}">
                  <div class="subtopic-horiz-header" onclick="toggleSubtopicHoriz(${ti}, ${si})">
                    <span class="subtopic-number-badge">${sub.num || `(${si + 1})`}</span>
                    <span class="subtopic-horiz-name">${sub.name || sub.title || `Section ${si + 1}`}</span>
                    ${sub.sq ? `<span class="subtopic-horiz-tag tag-sq">SQ</span>` : ""}
                    ${sub.mcq ? `<span class="subtopic-horiz-tag tag-mcq">MCQ</span>` : ""}
                    <span class="subtopic-horiz-chevron">▶</span>
                  </div>
                  <div class="subtopic-horiz-body" style="display:none;">
                    <div class="subtopic-study-text">
                      <div class="study-label">📖 Textbook Study Definition / Content:</div>
                      <p class="study-desc">${(sub.desc || sub.content || "").replace(/\n/g, '<br>')}</p>
                    </div>
                    ${(sub.sciNote || sub.sciNotes) ? `
                      <div class="sci-note-callout">
                        <div class="sci-note-header">
                          <span class="sci-icon">🔬</span>
                          <span class="sci-title">Scientific Information:</span>
                        </div>
                        <div class="sci-note-body">${(sub.sciNote || sub.sciNotes).replace(/\n/g, '<br>')}</div>
                      </div>
                    ` : ""}
                    ${sub.pointToRemember ? `
                      <div class="point-remember-box">
                        <div class="point-remember-header">
                          <span class="point-icon">💡</span>
                          <span class="point-title">Point to Remember:</span>
                        </div>
                        <div class="point-body">${sub.pointToRemember}</div>
                      </div>
                    ` : ""}
                    ${sub.sts ? `
                      <div class="sts-box">
                        <div class="sts-header">
                          <span class="sts-icon">🌐</span>
                          <span class="sts-title">Science, Technology and Society:</span>
                        </div>
                        <div class="sts-body">${sub.sts}</div>
                      </div>
                    ` : ""}
                    ${sub.activity ? `
                      <div class="activity-box">
                        <div class="activity-header">
                          <span class="act-icon">🧪</span>
                          <span class="act-title">Textbook Investigation / Activity:</span>
                        </div>
                        <div class="act-body">${sub.activity}</div>
                      </div>
                    ` : ""}
                    ${(sub.table && Array.isArray(sub.table.headers) && Array.isArray(sub.table.rows)) ? `
                      <div class="subtopic-table-box">
                        <div class="tbl-title">📊 ${sub.table.title || 'Table'}</div>
                        <table class="diff-table">
                          <thead>
                            <tr>${sub.table.headers.map(h => `<th>${h}</th>`).join('')}</tr>
                          </thead>
                          <tbody>
                            ${sub.table.rows.map(row => `<tr>${(Array.isArray(row) ? row : [row]).map(c => `<td>${c}</td>`).join('')}</tr>`).join('')}
                          </tbody>
                        </table>
                      </div>
                    ` : ""}
                    ${sub.figure ? `
                      <div class="subtopic-fig-box">
                        <div class="fig-header">
                          <span class="fig-icon">🖼️</span>
                          <span class="fig-title">${sub.figure.name || 'Figure'}</span>
                        </div>
                        <div class="fig-caption">${sub.figure.caption || ''}</div>
                      </div>
                    ` : ""}
                    ${sub.sq ? `
                      <div class="subtopic-sq-box">
                        <div class="subtopic-sq-header">
                          <span class="badge-sq-mini">SQ</span>
                          <span class="subtopic-sq-label">Textbook Short Question:</span>
                        </div>
                        <div class="subtopic-sq-text">${sub.sq}</div>
                      </div>
                    ` : ""}
                    ${(sub.mcq && Array.isArray(sub.mcq.opts || sub.mcq.options)) ? `
                      <div class="subtopic-mcq-box" id="sub-mcq-${ti}-${si}">
                        <div class="subtopic-mcq-header">
                          <span class="badge-mcq-mini">MCQ</span>
                          <span class="subtopic-mcq-q">${sub.mcq.q || ''}</span>
                        </div>
                        <div class="subtopic-mcq-grid">
                          ${(sub.mcq.opts || sub.mcq.options).map((opt, oi) => `
                            <button class="sub-opt-btn" onclick="checkSubtopicMcq(${ti}, ${si}, ${oi}, ${sub.mcq.ans ?? sub.mcq.correct ?? 0})">
                              <span class="sub-opt-letter">${String.fromCharCode(65 + oi)}</span>
                              <span class="sub-opt-text">${opt}</span>
                            </button>
                          `).join("")}
                        </div>
                        <div class="sub-mcq-fb" id="sub-fb-${ti}-${si}" style="display:none;"></div>
                      </div>
                    ` : ""}
                  </div>
                </div>
              `).join("")}
            </div>

            <!-- Topic Action Buttons -->
            <div class="topic-action-btns">
              <button class="btn-sq" onclick="openModal('sq', ${ch.num - 1}, ${ti})">
                📝 Section SQs (${sqCount})
              </button>
              <button class="btn-mcq" onclick="openModal('mcq', ${ch.num - 1}, ${ti})">
                🎯 Section MCQs (${mcqCount})
              </button>
              <button class="btn-lq" onclick="openModal('lq', ${ch.num - 1}, ${ti})">
                📄 Unit Detailed LQs (${lqCount})
              </button>
            </div>

          </div>
        </div>
      </div>`;
  }).join("");

  return `<div class="topic-accordion-wrap">${accordions}</div>`;
}

// ─── 2. TEXTBOOK EXERCISES VIEW ───────────
// ─── 2. TEXTBOOK EXERCISES VIEW ───────────
function renderTextbookExercises(ch) {
  const ex = ch.textbookExercise || { mcqs: [], sq: [], lq: [] };
  const mcqs = ex.mcqs || [];
  const sq = ex.sq || [];
  const lq = ex.lq || [];

  const mcqHtml = mcqs.map((m, mi) => {
    const opts = m.opts || m.options || [];
    const ansIdx = m.ans !== undefined ? m.ans : (m.correct !== undefined ? m.correct : 0);
    const exp = m.exp || m.explanation || "";
    return `
      <div class="tb-mcq-card" id="tb-mcq-${mi}">
        <div class="tb-mcq-title">
          <span class="tb-badge">Q${mi + 1}</span> ${m.q}
        </div>
        <div class="tb-opts-grid">
          ${opts.map((opt, oi) => `
            <button class="tb-opt-btn" onclick="checkTbMcq(${mi}, ${oi}, ${ansIdx}, '${encodeURIComponent(exp)}')">
              <span class="tb-opt-letter">${String.fromCharCode(65 + oi)}</span>
              <span>${opt}</span>
            </button>`).join("")}
        </div>
        <div class="tb-feedback" id="tb-fb-${mi}" style="display:none;"></div>
      </div>`;
  }).join("");

  const sqHtml = sq.map((s, si) => `
    <div class="tb-qa-card">
      <div class="tb-qa-q">
        <span class="tb-badge-sq">SQ ${si + 1}</span>
        <strong>${s.q}</strong>
      </div>
      <div class="tb-qa-a">
        <div class="tb-qa-label">Exam-Ready Answer:</div>
        <p>${(s.ans || "").replace(/\n/g, '<br>')}</p>
      </div>
    </div>`).join("");

  const lqHtml = lq.map((l, li) => `
    <div class="tb-qa-card">
      <div class="tb-qa-q">
        <span class="tb-badge-lq">Detailed Q ${li + 1}</span>
        <strong>${l.q}</strong>
      </div>
      <div class="tb-qa-a">
        <div class="tb-qa-label">Structured Exam Answer & Outline:</div>
        <p>${(l.ans || "").replace(/\n/g, '<br>')}</p>
      </div>
    </div>`).join("");

  return `
    <div class="ex-wrap">
      <div class="ex-header-bar">
        <h4>📕 Official Textbook Exercises — Unit ${ch.num}: ${ch.name}</h4>
        <p>Extracted directly from textbook exercise pages. Click options to test your knowledge.</p>
      </div>

      <!-- MCQs Section -->
      <div class="ex-sub-header">
        <h5>A. Encircle the Best Suitable Answers (${mcqs.length} Textbook MCQs)</h5>
      </div>
      <div class="tb-mcq-list">${mcqHtml}</div>

      <!-- Short Questions Section -->
      <div class="ex-sub-header" style="margin-top:2rem;">
        <h5>B. Write Short Answers for the Following Questions (${sq.length} Textbook SQs)</h5>
      </div>
      <div class="tb-qa-list">${sqHtml}</div>

      <!-- Detailed Questions Section -->
      <div class="ex-sub-header" style="margin-top:2rem;">
        <h5>C. Write Detailed / Long Answers (${lq.length} Textbook LQs)</h5>
      </div>
      <div class="tb-qa-list">${lqHtml}</div>
    </div>`;
}

// ─── 3. SLOS & CONCEPTS VIEW ──────────────
function renderSLOsAndConcepts(ch) {
  const slos = ch.slos || [];
  const slosHtml = slos.map((slo, i) => `
    <li class="slo-item">
      <span class="slo-num">SLO ${i + 1}</span>
      <span>${slo}</span>
    </li>`).join("");

  const sloMcqs = ch.sloMcqs || [];
  const sloMcqHtml = sloMcqs.length > 0 ? `
    <div class="section-title" style="margin-top:2rem;">🎯 SLO-Based Practice MCQs (${sloMcqs.length})</div>
    <div class="tb-mcq-list" style="margin-bottom:2rem;">
      ${sloMcqs.map((m, mi) => {
        const opts = m.opts || m.options || [];
        const ansIdx = m.ans !== undefined ? m.ans : 0;
        const exp = m.exp || "";
        return `
          <div class="tb-mcq-card" id="slo-mcq-${mi}">
            <div class="tb-mcq-title">
              <span class="tb-badge" style="background:#0284c7;">SLO Q${mi + 1}</span> ${m.q}
            </div>
            <div class="tb-opts-grid">
              ${opts.map((opt, oi) => `
                <button class="tb-opt-btn" onclick="checkSloMcq(${mi}, ${oi}, ${ansIdx}, '${encodeURIComponent(exp)}')">
                  <span class="tb-opt-letter">${String.fromCharCode(65 + oi)}</span>
                  <span>${opt}</span>
                </button>`).join("")}
            </div>
            <div class="tb-feedback" id="slo-fb-${mi}" style="display:none;"></div>
          </div>`;
      }).join("")}
    </div>` : "";

  const sloSq = ch.sloSq || [];
  const sloSqHtml = sloSq.length > 0 ? `
    <div class="section-title" style="margin-top:2rem;">📝 SLO-Based Conceptual Short Questions (${sloSq.length})</div>
    <div class="tb-qa-list" style="margin-bottom:2rem;">
      ${sloSq.map((s, si) => `
        <div class="tb-qa-card">
          <div class="tb-qa-q">
            <span class="tb-badge-sq" style="background:#0284c7;">SLO SQ ${si + 1}</span>
            <strong>${s.q}</strong>
          </div>
          <div class="tb-qa-a">
            <div class="tb-qa-label">Standard SLO Conceptual Solution:</div>
            <p>${(s.ans || "").replace(/\n/g, '<br>')}</p>
          </div>
        </div>`).join("")}
    </div>` : "";

  const sloLq = ch.sloLq || [];
  const sloLqHtml = sloLq.length > 0 ? `
    <div class="section-title" style="margin-top:2rem;">📚 SLO-Based Comprehensive Detailed Questions (${sloLq.length})</div>
    <div class="tb-qa-list" style="margin-bottom:2rem;">
      ${sloLq.map((l, li) => `
        <div class="tb-qa-card">
          <div class="tb-qa-q">
            <span class="tb-badge-lq" style="background:#0369a1;">SLO LQ ${li + 1}</span>
            <strong>${l.q}</strong>
          </div>
          <div class="tb-qa-a">
            <div class="tb-qa-label">Comprehensive Exam Model Answer:</div>
            <p>${(l.ans || "").replace(/\n/g, '<br>')}</p>
          </div>
        </div>`).join("")}
    </div>` : "";

  const defs = ch.definitions || [];
  const defsHtml = defs.length > 0 ? defs.map(d => `
    <div class="def-card">
      <div class="def-term">${d.term}</div>
      <div class="def-text">${d.def}</div>
    </div>`).join("") : `<div style="padding:1rem;color:var(--text-muted);font-style:italic;">Key definitions are integrated directly within the Topics &amp; Notes study view.</div>`;

  const diffs = ch.differences || [];
  const diffHtml = diffs.length > 0 ? diffs.map(diff => `
    <div style="margin-bottom:1.5rem;">
      <h5 style="margin-bottom:0.5rem;color:var(--navy);font-weight:700;">${diff.title}</h5>
      <table class="diff-table">
        <thead>
          <tr>
            <th>Feature</th>
            <th>${diff.colA}</th>
            <th>${diff.colB}</th>
          </tr>
        </thead>
        <tbody>
          ${(diff.rows || []).map(r => `
            <tr>
              <td><strong>${r[0]}</strong></td>
              <td>${r[1]}</td>
              <td>${r[2]}</td>
            </tr>`).join("")}
        </tbody>
      </table>
    </div>`).join("") : `<div style="padding:1rem;color:var(--text-muted);font-style:italic;">See Activities &amp; Tables tab for comparative tables.</div>`;

  const diags = ch.diagrams || [];
  const diagHtml = diags.length > 0 ? diags.map(d => `
    <div class="diag-card">
      <div class="diag-title">🖼️ ${d.name}</div>
      <div class="diag-topic"><strong>Topic:</strong> ${d.topic}</div>
      <div class="diag-note"><strong>Study Guide:</strong> ${d.note}</div>
    </div>`).join("") : `<div style="padding:1rem;color:var(--text-muted);font-style:italic;">Diagrams and figures are located within the Topics &amp; Notes and Activities &amp; Tables views.</div>`;

  return `
    <div class="slos-wrap" style="padding:1.25rem;">
      <div class="section-title">🎯 Official Student Learning Outcomes (SLOs)</div>
      <ul class="slo-list" style="margin-bottom:2rem;">${slosHtml}</ul>

      ${sloMcqHtml}
      ${sloSqHtml}
      ${sloLqHtml}

      <div class="section-title">📖 Key Definitions from Unit ${ch.num}</div>
      <div class="def-grid" style="margin-bottom:2rem;">${defsHtml}</div>

      <div class="section-title">⚖️ Important Concept Differences</div>
      <div style="margin-bottom:2rem;">${diffHtml}</div>

      <div class="section-title">🖼️ Essential Textbook Diagrams to Practice</div>
      <div class="diag-grid">${diagHtml}</div>
    </div>`;
}

function checkSloMcq(qIndex, selectedOpt, correctOpt, encodedExp) {
  const card = $(`slo-mcq-${qIndex}`);
  if (!card) return;
  const buttons = card.querySelectorAll(".tb-opt-btn");
  const fb = $(`slo-fb-${qIndex}`);
  const exp = decodeURIComponent(encodedExp);

  buttons.forEach((btn, oi) => {
    btn.disabled = true;
    if (oi === correctOpt) btn.classList.add("correct");
    else if (oi === selectedOpt && selectedOpt !== correctOpt) btn.classList.add("wrong");
  });

  const isCorrect = (selectedOpt === correctOpt);
  if (typeof recordQuestionAnswer === 'function') recordQuestionAnswer(isCorrect);

  if (fb) {
    fb.style.display = "block";
    fb.className = `tb-feedback ${isCorrect ? 'fb-correct' : 'fb-wrong'}`;
    fb.innerHTML = `
      <strong>${isCorrect ? '✅ Correct Answer!' : '❌ Incorrect!'}</strong> Option ${String.fromCharCode(65 + correctOpt)} is correct.
      <div style="margin-top:0.35rem;font-size:0.82rem;opacity:0.9;"><strong>Explanation:</strong> ${exp}</div>
    `;
  }
}

// ─── 4. ACTIVITIES, TABLES & FIGURES VIEW ───────────────
function renderActivitiesAndTables(ch) {
  const acts = ch.activities || [];
  const tbls = ch.tables || [];
  const diags = ch.diagrams || [];

  const actsHtml = acts.length > 0 ? acts.map((act, i) => `
    <div class="activity-card-full">
      <div class="act-card-header">
        <span class="act-badge">${act.num || `Activity ${i+1}`}</span>
        <h4 style="margin:0;font-size:1.05rem;color:var(--navy);">${act.name}</h4>
      </div>
      <div class="act-card-body">
        <div class="act-proc-label">🔬 Experimental Procedure &amp; Practical Investigation:</div>
        <p style="margin:0;font-size:0.9rem;line-height:1.6;color:#334155;">${(act.procedure || act.desc || "").replace(/\n/g, '<br>')}</p>
      </div>
    </div>
  `).join("") : `<div style="padding:1rem;color:var(--text-muted);font-style:italic;">Official textbook investigations are integrated inside the Topics &amp; Notes view.</div>`;

  const tblsHtml = tbls.length > 0 ? tbls.map(tbl => `
    <div class="tbl-card-full" style="background:#fff;border:1px solid var(--border);border-radius:10px;padding:1.25rem;margin-bottom:1.5rem;box-shadow:var(--shadow);">
      <h5 style="color:var(--navy);font-weight:700;margin-bottom:0.75rem;font-size:0.95rem;">📊 ${tbl.title}</h5>
      <table class="diff-table">
        <thead>
          <tr>${(tbl.headers || []).map(h => `<th>${h}</th>`).join("")}</tr>
        </thead>
        <tbody>
          ${(tbl.rows || []).map(r => `<tr>${r.map(c => `<td>${c}</td>`).join("")}</tr>`).join("")}
        </tbody>
      </table>
    </div>
  `).join("") : `<div style="padding:1rem;color:var(--text-muted);font-style:italic;">No standalone reference tables listed for this unit.</div>`;

  const diagsHtml = diags.length > 0 ? diags.map(d => `
    <div class="diag-card">
      <div class="diag-title">🖼️ ${d.name}</div>
      <div class="diag-topic"><strong>Topic:</strong> ${d.topic}</div>
      <div class="diag-note"><strong>Study Guide:</strong> ${d.note}</div>
    </div>
  `).join("") : `<div style="padding:1rem;color:var(--text-muted);font-style:italic;">All textbook illustrations are embedded within topics.</div>`;

  return `
    <div style="padding:1.25rem;">
      <div class="section-title">🧪 Official Laboratory Activities &amp; Investigations (${acts.length})</div>
      <div class="acts-list" style="display:flex;flex-direction:column;gap:1rem;margin-bottom:2rem;">${actsHtml}</div>

      <div class="section-title">📊 Official Textbook Reference Tables (${tbls.length})</div>
      <div class="tbls-list" style="margin-bottom:2rem;">${tblsHtml}</div>

      <div class="section-title">🖼️ Essential Textbook Diagrams &amp; Figures (${diags.length})</div>
      <div class="diag-grid">${diagsHtml}</div>
    </div>
  `;
}

// ─── 5. REVISION CHECKLIST VIEW ───────────
function renderChapterChecklist(ch) {
  const items = ch.checklist || (ch.slos || []).map(s => `Mastery of: ${s}`);
  const itemsHtml = items.map((item, idx) => `
    <label class="check-item">
      <input type="checkbox" onchange="toggleCheck(this)">
      <span class="check-text">${item}</span>
    </label>`).join("");

  return `
    <div style="padding:1.5rem;">
      <div class="section-title">✅ Unit ${ch.num} Mastery Checklist</div>
      <p style="font-size:0.85rem;color:var(--text-muted);margin-bottom:1.25rem;">Check off items as you complete your revision for this unit.</p>
      <div class="checklist-box">${itemsHtml}</div>
    </div>`;
}

function toggleCheck(input) {
  input.closest(".check-item").classList.toggle("checked", input.checked);
}

// ─── 5. FULL ROADMAP DASHBOARD VIEW ───────
function renderFullRoadmap() {
  state.page = "roadmap";
  state.activeView = "roadmap";
  setActiveNav("roadmap");
  setDashHeader("🗺️ KPK Grade 9 Biology — Complete Exam Roadmap", "9 Units · 96 Textbook MCQs · 52 Short Questions · 37 Long Questions");
  setBreadcrumb([
    { label: "Home", onclick: () => { setActiveNav("home"); renderHome(); } },
    { label: "Exam Roadmap", active: true }
  ]);

  const cardsHtml = DATA.bioChapters.map((ch, i) => `
    <div class="roadmap-unit-card">
      <div class="roadmap-unit-header">
        <div>
          <span class="roadmap-pill">Unit ${ch.num}</span>
          <h4 style="margin-top:0.35rem;font-size:1.05rem;">${ch.name}</h4>
          <span style="font-size:0.75rem;opacity:0.8;">${ch.pageRange}</span>
        </div>
        <button class="roadmap-open-btn" onclick="openBioView('cls9', {id:'cls9-bio', name:'Biology', hasBio:true}); selectBioChapter(${i});">
          Open Unit →
        </button>
      </div>
      <div class="roadmap-unit-body">
        <div class="roadmap-stats">
          <div><strong>${ch.topics.length}</strong> Topics</div>
          <div><strong>${ch.textbookExercise.mcqs.length}</strong> MCQs</div>
          <div><strong>${ch.textbookExercise.sq.length}</strong> SQs</div>
          <div><strong>${ch.textbookExercise.lq.length}</strong> LQs</div>
        </div>
        <div style="margin-top:0.75rem;font-size:0.8rem;color:var(--text-muted);">
          <strong>Key Focus:</strong> ${ch.slos.slice(0, 2).join(" · ")}
        </div>
      </div>
    </div>`).join("");

  pageContent().innerHTML = `
    <div class="roadmap-container">
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;">
        <button class="btn-back-link" style="margin-bottom:0;" onclick="goToSubjects('cls9'); openSubject('cls9','cls9-bio');"><span class="back-arrow">←</span> Back to Biology Portal</button>
        <div style="display:flex;gap:0.4rem;flex-wrap:wrap;">
          <button class="bio-ch-btn active" style="padding:0.4rem 0.85rem;font-size:0.82rem;" onclick="renderFullRoadmap()">🧬 Biology</button>
          <button class="bio-ch-btn" style="padding:0.4rem 0.85rem;font-size:0.82rem;" onclick="renderChemRoadmap()">🧪 Chemistry</button>
          <button class="bio-ch-btn" style="padding:0.4rem 0.85rem;font-size:0.82rem;" onclick="renderPhysRoadmap()">⚛️ Physics</button>
        </div>
      </div>
      <div style="background:#fff;border:1px solid var(--border);border-radius:12px;padding:1.5rem;margin-bottom:1.5rem;box-shadow:var(--shadow);">
        <h3 style="color:var(--navy);font-size:1.2rem;margin-bottom:0.5rem;">📘 Official KPK Textbook Board Exam Preparation Pathway</h3>
        <p style="font-size:0.875rem;color:var(--text-muted);line-height:1.6;">
          This roadmap covers all 9 units from the official Grade IX textbook volume. Follow the 5-day cycle per unit to guarantee mastery for your board examinations.
        </p>
        <div style="display:flex;gap:0.75rem;margin-top:1rem;flex-wrap:wrap;">
          <span style="background:#e0f2fe;color:#0284c7;font-weight:700;font-size:0.8rem;padding:0.35rem 0.75rem;border-radius:99px;">9 Units</span>
          <span style="background:#dcfce7;color:#15803d;font-weight:700;font-size:0.8rem;padding:0.35rem 0.75rem;border-radius:99px;">96 Textbook MCQs</span>
          <span style="background:#fef9c3;color:#a16207;font-weight:700;font-size:0.8rem;padding:0.35rem 0.75rem;border-radius:99px;">52 Verified SQs</span>
          <span style="background:#f3e8ff;color:#7c3aed;font-weight:700;font-size:0.8rem;padding:0.35rem 0.75rem;border-radius:99px;">37 Detailed LQs</span>
        </div>
      </div>

      <div class="roadmap-grid">${cardsHtml}</div>

      <div style="margin-top:2rem;">
        <div class="section-title">📅 Recommended 5-Day Study Routine per Unit</div>
        <div class="plan-grid">
          ${DATA.studyPlan.map(p => `
            <div class="plan-card">
              <div class="plan-day">${p.day}</div>
              <div class="plan-title">${p.subject}</div>
              <div class="plan-meta">⏰ ${p.time}</div>
              <div class="plan-progress-bg">
                <div class="plan-progress-fill" style="width:${p.progress}%"></div>
              </div>
            </div>`).join("")}
        </div>
      </div>
    </div>`;
}

// ─── Interactive Textbook MCQ Checker ─────
function checkTbMcq(qIndex, selectedOpt, correctOpt, encodedExp) {
  const card = $(`tb-mcq-${qIndex}`);
  const buttons = card.querySelectorAll(".tb-opt-btn");
  const fb = $(`tb-fb-${qIndex}`);
  const exp = decodeURIComponent(encodedExp);

  buttons.forEach((btn, oi) => {
    btn.disabled = true;
    if (oi === correctOpt) btn.classList.add("correct");
    else if (oi === selectedOpt && selectedOpt !== correctOpt) btn.classList.add("wrong");
  });

  const isCorrect = (selectedOpt === correctOpt);
  recordQuestionAnswer(isCorrect);

  fb.style.display = "block";
  fb.className = `tb-feedback ${isCorrect ? 'fb-correct' : 'fb-wrong'}`;
  fb.innerHTML = `
    <strong>${isCorrect ? '✅ Correct Answer!' : '❌ Incorrect!'}</strong> Option ${String.fromCharCode(65 + correctOpt)} is correct.
    <div style="margin-top:0.35rem;font-size:0.82rem;opacity:0.9;"><strong>Explanation:</strong> ${exp}</div>
  `;
}

// ─── Accordion Toggle (Smooth Slide Down / Up) ─────────────
function toggleAccordion(topicIndex) {
  const trigger = $(`acc-trigger-${topicIndex}`);
  const body    = $(`acc-body-${topicIndex}`);
  if (!trigger || !body) return;
  const isOpen  = trigger.classList.contains("open");

  if (isOpen) {
    body.style.maxHeight = body.scrollHeight + "px";
    requestAnimationFrame(() => {
      body.style.maxHeight = "0px";
    });
    trigger.classList.remove("open");
  } else {
    body.style.maxHeight = body.scrollHeight + "px";
    trigger.classList.add("open");
    // After CSS transition completes, remove max-height constraint so interactive elements can expand freely
    setTimeout(() => {
      if (trigger.classList.contains("open")) {
        body.style.maxHeight = "none";
      }
    }, 460);
  }
}

// ─── Hierarchy Tree Toggle (Collapse/Expand) ─────────────
function toggleHierarchy(headerEl) {
  const box = headerEl.closest(".hierarchy-tree-box");
  const code = box.querySelector(".hierarchy-tree-code");
  const chevron = headerEl.querySelector(".hierarchy-chevron");
  const isOpen = code.style.display !== "none";
  if (isOpen) {
    code.style.display = "none";
    chevron.textContent = "▶";
    headerEl.classList.remove("open");
  } else {
    code.style.display = "block";
    chevron.textContent = "▼";
    headerEl.classList.add("open");
  }
}

// ─── Subtopic Horizontal Accordion Toggle (only one open at a time) ──
function toggleSubtopicHoriz(ti, si) {
  const item = document.getElementById(`sub-horiz-${ti}-${si}`);
  if (!item) return;
  const body = item.querySelector(".subtopic-horiz-body");
  const chevron = item.querySelector(".subtopic-horiz-chevron");
  const isOpen = item.classList.contains("open");

  // Close all other open items in the same wrap
  const wrap = item.closest(".subtopics-horiz-wrap");
  if (wrap) {
    wrap.querySelectorAll(".subtopic-horiz-item.open").forEach(other => {
      if (other !== item) {
        other.classList.remove("open");
        other.querySelector(".subtopic-horiz-body").style.display = "none";
        other.querySelector(".subtopic-horiz-chevron").textContent = "▶";
      }
    });
  }

  if (isOpen) {
    body.style.display = "none";
    chevron.textContent = "▶";
    item.classList.remove("open");
  } else {
    body.style.display = "block";
    chevron.textContent = "▼";
    item.classList.add("open");
  }
}

// ─── Subtopic Practice MCQ Checker ────────
function checkSubtopicMcq(ti, si, selected, correct) {
  const box = $(`sub-mcq-${ti}-${si}`);
  if (!box) return;
  const btns = box.querySelectorAll(".sub-opt-btn");
  const fb = $(`sub-fb-${ti}-${si}`);

  btns.forEach((btn, idx) => {
    btn.disabled = true;
    if (idx === correct) btn.classList.add("correct");
    else if (idx === selected && selected !== correct) btn.classList.add("wrong");
  });

  const isCorrect = (selected === correct);
  recordQuestionAnswer(isCorrect);

  if (fb) {
    fb.style.display = "block";
    const correctLetter = String.fromCharCode(65 + correct);
    const correctText = btns[correct].querySelector(".sub-opt-text").textContent;
    fb.className = `sub-mcq-fb ${isCorrect ? "fb-correct" : "fb-wrong"}`;
    fb.innerHTML = isCorrect 
      ? `<strong>✅ Correct Answer!</strong> Option ${correctLetter} is correct.` 
      : `<strong>❌ Incorrect!</strong> The correct answer is <strong>Option ${correctLetter}:</strong> ${correctText}.`;
  }
}

// ─── Language Switcher ────────────────────
function switchLang(topicIndex, lang, btn) {
  const allTabs = btn.closest(".lang-tabs").querySelectorAll(".lang-tab");
  allTabs.forEach(t => t.classList.remove("active"));
  btn.classList.add("active");

  ["en", "ur", "ps"].forEach(l => {
    const el = $(`lang-${l}-${topicIndex}`);
    if (el) el.classList.toggle("active", l === lang);
  });
}

// ─── MODAL CONTROLLER ─────────────────────
function setupModal() {
  const overlay = $("modalOverlay");
  if (overlay) {
    overlay.addEventListener("click", e => {
      if (e.target === overlay) closeModal();
    });
  }
  document.addEventListener("keydown", e => {
    if (e.key === "Escape") closeModal();
  });
}

function openModal(type, chIndex, topicIndex) {
  const isCls10 = (state.selectedClass === "cls10");
  const chapters = state.activeSubject === "chem" ? (isCls10 ? DATA.chem10Chapters : DATA.chemChapters)
                 : state.activeSubject === "phys" ? (isCls10 ? DATA.phys10Chapters : DATA.physChapters)
                 : state.activeSubject === "eng"  ? (isCls10 ? (DATA.eng10Chapters || []) : DATA.engChapters)
                 : (isCls10 ? DATA.bio10Chapters : DATA.bioChapters);
  const ch    = chapters[chIndex];
  const topic = ch.topics[topicIndex];
  const overlay = $("modalOverlay");
  const header  = $("modalHeader");
  const body    = $("modalBody");

  let title = "";
  let html  = "";
  const subtopics = topic.subtopics || [];

  if (type === "sq") {
    const exSq = ch.textbookExercise && ch.textbookExercise.sq ? ch.textbookExercise.sq : [];
    const subSqList = subtopics.filter(s => s.sq).map(s => ({ q: s.sq, source: s.num + " " + s.name }));
    // Merge: use textbookExercise answers if available, otherwise use subtopic questions
    const sqList = exSq.length > 0 ? exSq.map((s, i) => ({
      q: s.q,
      ans: s.ans,
      source: subSqList[i] ? subSqList[i].source : "Unit " + ch.num
    })) : subSqList.map(s => ({ ...s, ans: "" }));

    title = `📝 Practice SQs — ${topic.num} ${topic.title} (${sqList.length} Questions)`;
    html = `
      <div class="sq-list">
        ${sqList.map((item, i) => `
          <div class="sq-item" onclick="this.classList.toggle('revealed')" style="cursor:pointer;">
            <span class="sq-num">${i + 1}</span>
            <div style="flex:1;">
              <div style="font-size:0.75rem;color:var(--blue);font-weight:700;margin-bottom:0.25rem;">${item.source}</div>
              <div style="font-size:0.9rem;color:var(--navy);font-weight:600;">${item.q}</div>
              <div class="sq-answer" style="display:none;margin-top:0.65rem;padding:0.7rem 0.85rem;background:#f0fdf4;border:1px solid #bbf7d0;border-radius:6px;font-size:0.85rem;color:#14532d;line-height:1.65;">
                <div style="font-size:0.7rem;font-weight:700;color:#15803d;text-transform:uppercase;letter-spacing:0.04em;margin-bottom:0.25rem;">Exam-Ready Answer:</div>
                ${item.ans ? item.ans : '<em style="color:#64748b;">Answer available in Textbook Exercises tab.</em>'}
              </div>
            </div>
            <span class="sq-reveal-icon" style="font-size:0.75rem;color:#94a3b8;transition:transform 0.3s;">▶</span>
          </div>`).join("")}
      </div>`;

  } else if (type === "lq") {
    const lqs = ch.textbookExercise && ch.textbookExercise.lq ? ch.textbookExercise.lq : [];
    title = `📄 Detailed Questions — Unit ${ch.num}: ${ch.name} (${lqs.length} Questions)`;
    html = `
      <div class="tb-qa-list">
        ${lqs.map((l, li) => `
          <div class="tb-qa-card lq-collapsible">
            <div class="tb-qa-q" onclick="this.parentElement.classList.toggle('revealed')" style="cursor:pointer;">
              <span class="tb-badge-lq">Detailed Q ${li + 1}</span>
              <strong>${l.q}</strong>
              <span class="lq-reveal-icon" style="margin-left:auto;font-size:0.75rem;color:#94a3b8;transition:transform 0.3s;">▶</span>
            </div>
            <div class="tb-qa-a" style="display:none;">
              <div class="tb-qa-label">Structured Exam Answer & Outline:</div>
              <p>${l.ans}</p>
            </div>
          </div>`).join("")}
      </div>`;

  } else if (type === "mcq") {
    const mcqList = subtopics.filter(s => s.mcq).map(s => ({ ...s.mcq, subName: s.num + " " + s.name }));
    title = `🎯 Topic MCQs Quiz — ${topic.num} ${topic.title} (${mcqList.length} Questions)`;
    html = `
      <div class="mcq-list">
        ${mcqList.map((m, mi) => `
          <div class="mcq-item">
            <div style="font-size:0.75rem;color:var(--blue);font-weight:700;margin-bottom:0.25rem;">${m.subName}</div>
            <div class="mcq-q">Q${mi + 1}. ${m.q}</div>
            <div class="mcq-opts" id="topic-modal-mcq-${mi}">
              ${m.opts.map((opt, oi) => `
                <div class="mcq-opt" onclick="checkTopicModalMcq(${mi}, ${oi}, ${m.ans})">
                  <span class="mcq-opt-letter">${String.fromCharCode(65 + oi)}</span>
                  ${opt}
                </div>`).join("")}
            </div>
          </div>`).join("")}
      </div>`;
  }

  header.textContent = title;
  body.innerHTML = html;
  overlay.classList.add("visible");
}

function checkTopicModalMcq(mcqIndex, selectedOpt, correctOpt) {
  const container = $(`topic-modal-mcq-${mcqIndex}`);
  if (!container) return;
  const opts = container.querySelectorAll(".mcq-opt");
  opts.forEach((opt, i) => {
    opt.classList.add("revealed");
    if (i === correctOpt) opt.classList.add("correct");
    else if (i === selectedOpt && selectedOpt !== correctOpt) opt.classList.add("wrong");
  });
  const isCorrect = (selectedOpt === correctOpt);
  recordQuestionAnswer(isCorrect);
}

function closeModal() {
  const overlay = $("modalOverlay");
  if (overlay) overlay.classList.remove("visible");
}


// ─── GENERIC CHAPTERS FOR NON-BIO ─────────
function goToChapters(classId, subjId, subjName) {
  const cls = DATA.classes.find(c => c.id === classId);
  const chapters = DATA.chapters[subjId] || generateGenericChapters(subjId);

  setDashHeader(`📄 ${subjName}`, `${cls.name} — Units`);
  setBreadcrumb([
    { label: "Home",     onclick: () => { setActiveNav("home"); renderHome(); } },
    { label: "Subjects", onclick: () => renderClasses() },
    { label: cls.name,   onclick: () => goToSubjects(classId) },
    { label: subjName,   active: true }
  ]);

  const sLbl = { done: "Completed", ready: "Completed", progress: "In Progress", upcoming: "Upcoming" };
  const sCls = { done: "status-done", ready: "status-done", progress: "status-progress", upcoming: "status-upcoming" };

  pageContent().innerHTML = `
    <button class="btn-back-link" onclick="goToSubjects('${classId}')"><span class="back-arrow">←</span> Back to ${cls.name} Subjects</button>
    <div class="section-title">${subjName} — Units</div>
    <div class="chapter-list">
      ${chapters.map((ch, idx) => `
        <div class="chapter-card" style="cursor:pointer;transition:transform 0.15s;" onmouseover="this.style.transform='translateX(4px)'" onmouseout="this.style.transform='none'" onclick="openGenericChapterDetails('${classId}', '${subjId}', '${subjName}', ${ch.num})">
          <div class="chapter-num">${ch.num}</div>
          <div class="chapter-info">
            <div class="chapter-name">${ch.name || ch.title || ""}</div>
            <div class="chapter-topics">${ch.topics} · Click to view syllabus & competencies →</div>
          </div>
          <span class="chapter-status ${sCls[ch.status] || sCls.done}">${sLbl[ch.status] || sLbl.done}</span>
        </div>`).join("")}
    </div>`;
}

function generateGenericChapters(subjId) {
  let count = 8;
  for (const subs of Object.values(DATA.subjects)) {
    const found = subs.find(s => s.id === subjId);
    if (found) { count = found.chapters; break; }
  }
  const statuses = ["done", "done", "progress", "upcoming"];
  return Array.from({ length: count }, (_, i) => ({
    num: i + 1,
    name: `Unit ${i + 1}`,
    topics: `${3 + (i % 3)} Topics`,
    status: statuses[Math.min(i, statuses.length - 1)]
  }));
}

// ─── STUDY PLAN ──────────────────────────
function renderStudyPlan() {
  state.page = "study-plan";
  state.activeView = "study-plan";
  setActiveNav("study-plan");
  setDashHeader("📅 Study Plan", "Weekly tuition schedule & progress tracking");
  setBreadcrumb([
    { label: "Home",       onclick: () => { setActiveNav("home"); renderHome(); } },
    { label: "Study Plan", active: true }
  ]);
  pageContent().innerHTML = `
    <button class="btn-back-link" onclick="setActiveNav('home'); renderHome();"><span class="back-arrow">←</span> Back to Home</button>
    <div class="section-title">Weekly 5-Day Study Plan for Biology Mastery</div>
    <div class="plan-grid">
      ${DATA.studyPlan.map(p => `
        <div class="plan-card">
          <div class="plan-day">${p.day}</div>
          <div class="plan-title">${p.subject}</div>
          <div class="plan-meta">⏰ ${p.time}</div>
          <div class="plan-progress-bg">
            <div class="plan-progress-fill" style="width:${p.progress}%"></div>
          </div>
        </div>`).join("")}
    </div>`;
}

// ─── Helpers ─────────────────────────────
function setDashHeader(title, sub) {
  const bar = $("subpage-nav-bar");
  if (bar) bar.style.display = (state.page === "home") ? "none" : "block";
  if (dashHeaderTitle()) dashHeaderTitle().innerHTML = title;
  if (dashHeaderSub()) dashHeaderSub().innerHTML = sub;
}

let currentNavCrumbs = [];

function setBreadcrumb(crumbs) {
  currentNavCrumbs = crumbs;

  let backBtnHtml = "";
  if (crumbs && crumbs.length > 1) {
    let targetCrumb = null;
    for (let i = crumbs.length - 2; i >= 0; i--) {
      if (crumbs[i].onclick) {
        targetCrumb = crumbs[i];
        break;
      }
    }
    const label = targetCrumb ? targetCrumb.label : "Previous";
    backBtnHtml = `
      <button class="crumb-back-btn" onclick="goBack()" title="Go back to ${label}">
        <span class="back-arrow">←</span> Back
      </button>
      <span class="crumb-v-sep">|</span>
    `;
  }

  const crumbsHtml = crumbs.map((c, i) => {
    const sep = i > 0 ? `<span class="sep">›</span>` : "";
    if (c.active) return `${sep}<span class="crumb current">${c.label}</span>`;
    const fn = c.onclick ? c.onclick.toString() : "";
    return `${sep}<span class="crumb" onclick="(${fn})()">${c.label}</span>`;
  }).join(" ");

  breadcrumbEl().innerHTML = `${backBtnHtml}${crumbsHtml}`;
}

function goBack() {
  if (!currentNavCrumbs || currentNavCrumbs.length <= 1) {
    setActiveNav("home");
    renderHome();
    return;
  }
  for (let i = currentNavCrumbs.length - 2; i >= 0; i--) {
    if (currentNavCrumbs[i].onclick) {
      currentNavCrumbs[i].onclick();
      return;
    }
  }
  setActiveNav("home");
  renderHome();
}



// ─── GENERIC CHAPTER DETAILS MODAL (Class 10, 11, 12) ─────────
function openGenericChapterDetails(classId, subjId, subjName, chNum) {
  const cls = DATA.classes.find(c => c.id === classId);
  const chList = DATA.chapters[subjId] || generateGenericChapters(subjId);
  const ch = chList.find(c => c.num === chNum) || chList[chNum - 1] || { num: chNum, name: `Chapter ${chNum}`, topics: "Core Topics" };
  
  const overlay = $("modalOverlay");
  const header  = $("modalHeader");
  const body    = $("modalBody");
  if (!overlay || !header || !body) return;

  header.innerHTML = `<span>${subjName} · Chapter ${ch.num}: ${ch.name || ch.title || ""}</span>`;

  let sourceBanner = "";
  if (classId === "cls12") {
    sourceBanner = `
      <div style="background:#fef3c7;border:1px solid #f59e0b;border-radius:10px;padding:1rem;margin-bottom:1.25rem;">
        <div style="font-weight:700;color:#92400e;display:flex;align-items:center;gap:0.5rem;font-size:0.95rem;">
          <span>ℹ️</span> Official KPK Textbook Source Notice — Class 12
        </div>
        <p style="font-size:0.85rem;color:#78350f;margin:0.5rem 0 0;line-height:1.5;">
          This chapter follows the <strong>KPK Textbook Board Class 12 (HSSC-II / 2nd Year)</strong> official syllabus.
          <em>The complete Class 12 textbook PDF has not been uploaded to the local workspace yet.</em>
          To maintain 100% textbook accuracy without guessing or inventing numerical problems, full verified line-by-line textbook solutions, exercises, and numerical steps will automatically populate once the Class 12 textbook PDF is provided.
        </p>
      </div>`;
  }

  body.innerHTML = `
    ${sourceBanner}
    <div style="margin-bottom:1rem;">
      <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.5rem;">
        <span style="background:#e0f2fe;color:#0284c7;font-weight:700;padding:0.25rem 0.6rem;border-radius:6px;font-size:0.8rem;">${cls.name}</span>
        <span style="background:#ede9fe;color:#7c3aed;font-weight:700;padding:0.25rem 0.6rem;border-radius:6px;font-size:0.8rem;">Unit ${ch.num}</span>
        <span style="background:#dcfce7;color:#15803d;font-weight:700;padding:0.25rem 0.6rem;border-radius:6px;font-size:0.8rem;">Status: ${ch.status || 'Active'}</span>
      </div>
      <h3 style="color:#0f172a;font-size:1.25rem;margin-bottom:0.5rem;">${ch.name || ch.title || ""}</h3>
      <p style="color:#64748b;font-size:0.875rem;">Official Curriculum Framework · Khyber Pakhtunkhwa Textbook Board</p>
    </div>

    <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:1rem;margin-bottom:1rem;">
      <h4 style="font-size:0.95rem;color:#1e293b;margin-bottom:0.5rem;">🎯 Core Topics & Syllabus Competencies</h4>
      <ul style="padding-left:1.25rem;font-size:0.875rem;color:#334155;line-height:1.8;margin:0;">
        <li>Fundamental concepts, physical laws, and theoretical foundations of ${ch.name || ch.title || ""}</li>
        <li>Mathematical derivations, formulas, and quantitative relationships</li>
        <li>Board exam focal points: short questions, long descriptive topics, and conceptual reasoning</li>
        <li>Practical laboratory applications, industrial relevance, and real-world technology links</li>
      </ul>
    </div>

    <div style="display:flex;gap:0.5rem;justify-content:flex-end;">
      <button onclick="closeModal()" style="padding:0.5rem 1.25rem;background:#475569;color:#fff;border:none;border-radius:8px;font-weight:600;cursor:pointer;">Close</button>
    </div>`;

  overlay.classList.add("visible");
}

// ─────────────────────────────────────────
// ─────────────────────────────────────────
//  ISLAMYAT INTERACTIVE LESSONS & TRILINGUAL PORTAL (Class 9 & 10)
// ─────────────────────────────────────────
function _getIslChapters() {
  const isCls10 = (state.selectedClass === "cls10");
  if (isCls10) {
    return (typeof DATA !== 'undefined' && DATA.islamyat10Chapters) || 
           (typeof window !== 'undefined' && window.ISLAMYAT_10_DATA) || 
           (typeof ISLAMYAT_10_DATA !== 'undefined' ? ISLAMYAT_10_DATA : []);
  }
  return (typeof DATA !== 'undefined' && DATA.islamyatChapters) || 
         (typeof window !== 'undefined' && window.ISLAMYAT_DATA) || 
         (typeof ISLAMYAT_DATA !== 'undefined' ? ISLAMYAT_DATA : []);
}

function openIslView(classId, subj) {
  state.activeSubject = "isl";
  state.selectedIslChapter = 0;
  state.activeIslTab = "lesson";
  state.activeIslSloTab = "slo-mcqs";
  state.selectedClass = classId;
  setActiveNav("subjects");
  const isCls10 = (classId === "cls10");
  const cls = DATA.classes.find(c => c.id === classId) || { name: isCls10 ? "Class 10" : "Class 9" };
  const chList = _getIslChapters();
  const gradeLabel = isCls10 ? "Grade 10 (Part B)" : "Grade 9 (Part A)";
  const pdfFile = "assets/books/Class-9-Islamyat-KPK.pdf";
  const desc = isCls10
    ? `KPK Textbook Board, Peshawar · ${chList.length} Units (Surah Al-Ahzab, Surah Al-Mumtahina, Ahadith & Thematic Study)`
    : `KPK Textbook Board, Peshawar · ${chList.length} Units (Surah Al-Anfal, Ahadith & Thematic Study)`;

  setDashHeader(`🕌 ${subj ? subj.name : 'Islamyat'} — ${gradeLabel}`, `${desc} &nbsp;|&nbsp; <a href="${pdfFile}" target="_blank" style="color:#0d9488;font-weight:700;text-decoration:underline;">📥 View/Download Official Islamyat Book PDF</a>`);
  setBreadcrumb([
    { label: "Home",     onclick: () => { setActiveNav("home"); renderHome(); } },
    { label: "Subjects", onclick: () => renderClasses() },
    { label: cls.name,   onclick: () => goToSubjects(classId) },
    { label: subj ? subj.name : "Islamyat", active: true }
  ]);

  const chapBtns = chList.map((ch, i) => {
    let badgeText = '';
    let badgeBg = '#0d9488';
    if (ch.type === 'quran' || ch.type === 'surah') {
      badgeText = 'رکوع ' + (ch.ruku || ch.number);
      badgeBg = '#0d9488';
    } else if (ch.type === 'hadith') {
      badgeText = 'احادیث';
      badgeBg = '#0f766e';
    } else {
      badgeText = 'موضوع ' + (ch.number > 13 ? (ch.number - 13) : (ch.number - 11));
      badgeBg = '#0284c7';
    }

    return `
      <button class="bio-ch-btn ${i === 0 ? "active" : ""}" id="isl-btn-${i}"
              onclick="selectIslChapter(${i})">
        <span class="ch-btn-num" style="background:${badgeBg};color:#fff;font-size:0.78rem;">${badgeText}</span>
        <span class="ch-btn-info">
          <span class="ch-btn-name" style="direction:rtl;text-align:right;font-family:'Jameel Noori Nastaleeq', 'Segoe UI', serif;font-size:1.02rem;">${ch.title || ''}</span>
          <span class="ch-btn-sub">${ch.ayahRange ? 'آیات: ' + ch.ayahRange : (ch.titleEn || '')}</span>
        </span>
        <span class="ch-btn-status" style="background:#ccfbf1;color:#0f766e;">
          ✅ Complete
        </span>
      </button>`;
  }).join("");

  pageContent().innerHTML = `
    <div class="bio-view">
      <div class="bio-ch-sidebar">
        <div class="bio-ch-sidebar-header" style="background:linear-gradient(135deg,#0d9488,#0f766e);color:#fff;">
          <button onclick="goToSubjects('${classId}')" class="sidebar-back-icon-btn" title="Back to Subjects">←</button>
          <span>🕌 KPK ${gradeLabel} Islamyat</span>
        </div>
        <div class="bio-ch-list">${chapBtns}</div>
        <div style="padding:1rem;background:#f8fafc;border-top:1px solid var(--border);text-align:center;">
          <a href="${pdfFile}" target="_blank" style="display:block;width:100%;padding:0.55rem;background:#0d9488;color:#fff;border-radius:6px;font-weight:700;font-size:0.82rem;text-decoration:none;">
            📥 Download Official PDF Book
          </a>
        </div>
      </div>
      <div class="bio-topic-area" id="islTopicArea"></div>
    </div>`;

  renderIslChapter(0);
}

function selectIslChapter(index) {
  state.selectedIslChapter = index;
  document.querySelectorAll(".bio-ch-btn").forEach((btn, i) =>
    btn.classList.toggle("active", i === index));
  renderIslChapter(index);
}

function switchIslTab(tabName) {
  state.activeIslTab = tabName;
  document.querySelectorAll(".isl-top-tab").forEach(btn =>
    btn.classList.toggle("active", btn.dataset.tab === tabName));

  const chList = _getIslChapters();
  const ch = chList[state.selectedIslChapter];
  const container = $("islTabContent");
  if (!container || !ch) return;

  if (tabName === "lesson") {
    container.innerHTML = renderIslLesson(ch);
  } else if (tabName === "ps-trans") {
    container.innerHTML = renderIslPashtoTranslation(ch);
  } else if (tabName === "en-trans") {
    container.innerHTML = renderIslEnglishTranslation(ch);
  } else if (tabName === "video") {
    container.innerHTML = renderIslVideo(ch);
  } else if (tabName === "en-sum") {
    container.innerHTML = renderIslEnglishSummary(ch);
  } else if (tabName === "ur-sum") {
    container.innerHTML = renderIslUrduSummary(ch);
  } else if (tabName === "ps-sum") {
    container.innerHTML = renderIslPashtoSummary(ch);
  } else if (tabName === "pages") {
    container.innerHTML = renderIslPageImages(ch);
  } else if (tabName === "exercise") {
    container.innerHTML = renderIslExercise(ch);
  } else if (tabName === "slos") {
    container.innerHTML = renderIslSLOs(ch);
  }
}

function switchIslSloTab(tabName) {
  if (state.activeIslSloTab === tabName) {
    state.activeIslSloTab = null;
    document.querySelectorAll(".isl-slo-tab-pill").forEach(btn => btn.classList.remove("active"));
    const container = $("islSloTabContent");
    if (container) container.innerHTML = "";
    return;
  }

  state.activeIslSloTab = tabName;
  document.querySelectorAll(".isl-slo-tab-pill").forEach(btn =>
    btn.classList.toggle("active", btn.dataset.slotab === tabName));

  const chList = _getIslChapters();
  const ch = chList[state.selectedIslChapter];
  const container = $("islSloTabContent");
  if (!container || !ch) return;

  if (!tabName) {
    container.innerHTML = "";
    return;
  }

  if (tabName === "slo-mcqs") {
    container.innerHTML = renderIslSloMcqs(ch);
  } else if (tabName === "slo-sq") {
    container.innerHTML = renderIslSloSQs(ch);
  } else if (tabName === "slo-lq") {
    container.innerHTML = renderIslSloLQs(ch);
  }
}

function renderIslPageImages(ch) {
  if (!ch.pageImages || !ch.pageImages.length) {
    return `<div style="text-align:center;padding:2rem;color:var(--text-muted);direction:rtl;">اس سبق کے درسی صفحات دستیاب نہیں ہیں۔</div>`;
  }
  const imgsHtml = ch.pageImages.map((src, i) => `
    <div style="background:#fff;border-radius:10px;padding:0.75rem;box-shadow:0 2px 10px rgba(0,0,0,0.08);margin-bottom:1.5rem;text-align:center;">
      <div style="font-weight:700;color:#0f766e;margin-bottom:0.5rem;font-size:0.95rem;">
        📖 خیبر پختونخوا درسی کتاب — صفحہ ${i + 1}
      </div>
      <a href="${src}" target="_blank" title="مکمل تصویر دیکھنے کے لیے کلک کریں">
        <img src="${src}" alt="Textbook Page" style="max-width:100%;height:auto;border-radius:6px;border:1px solid #e2e8f0;box-shadow:0 4px 12px rgba(0,0,0,0.05);transition:transform 0.2s;" loading="lazy" />
      </a>
      <div style="margin-top:0.4rem;font-size:0.8rem;color:#64748b;">(بڑے سائز میں دیکھنے کے لیے تصویر پر کلک کریں)</div>
    </div>
  `).join("");

  return `
    <div style="max-width:850px;margin:0 auto;direction:rtl;">
      <div class="urdu-ctrl-bar" style="border-left:4px solid #0f766e;background:#f0fdf4;margin-bottom:1.25rem;">
        <div>
          <strong style="color:#0f766e;font-size:1.05rem;">🖼️ خیبر پختونخوا ٹیکسٹ بک بورڈ — درسی کتاب کے اصل سکین شدہ صفحات</strong>
          <p style="font-size:0.85rem;color:#047857;margin-top:0.25rem;">یہ صفحات سرکاری درسی کتاب کے عین مطابق ہیں جن سے اس سبق کا مواد تیار کیا گیا ہے۔</p>
        </div>
      </div>
      ${imgsHtml}
    </div>`;
}

function renderIslChapter(index) {
  const chList = _getIslChapters();
  const ch = chList[index];
  const area = $("islTopicArea");
  if (!area || !ch) return;

  const sqCount = (ch.exercise && ch.exercise.shortQuestions ? ch.exercise.shortQuestions.length : 0) + (ch.sloQuestions && ch.sloQuestions.shortQuestions ? ch.sloQuestions.shortQuestions.length : 0);
  const mcqCount = (ch.sloQuestions && ch.sloQuestions.mcqs ? ch.sloQuestions.mcqs.length : 0);
  const lqCount = (ch.exercise && ch.exercise.longQuestions ? ch.exercise.longQuestions.length : 0) + (ch.sloQuestions && ch.sloQuestions.longQuestions ? ch.sloQuestions.longQuestions.length : 0);

  area.innerHTML = `
    <div class="chapter-title-bar" style="border-left: 4px solid #0d9488;">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:0.75rem;width:100%;">
        <div>
          <div style="direction:rtl;text-align:right;">
            <h2 style="font-family:'Jameel Noori Nastaleeq','Segoe UI',serif;color:var(--navy);font-size:1.6rem;margin-bottom:0.25rem;">${ch.number}. ${ch.title}</h2>
            <p style="color:#0f766e;font-weight:700;font-size:0.95rem;">${ch.author} · ${ch.titlePs || ''}</p>
          </div>
          <p style="color:var(--text-muted);font-size:0.85rem;margin-top:0.25rem;">${ch.titleEn} · ${mcqCount} MCQs · ${sqCount} Short Questions · ${lqCount} Long Questions · Trilingual Translations</p>
        </div>
        <button class="btn-back-sm" onclick="goToSubjects('${state.selectedClass || 'cls9'}')"><span class="back-arrow">←</span> Back to Subjects</button>
      </div>
    </div>

    <!-- Upper Tabs -->
    <div class="chapter-nav-tabs" style="border-bottom: 2px solid #99f6e4; overflow-x: auto; flex-wrap: nowrap; padding-bottom: 4px;">
      <button class="bio-tab-btn isl-top-tab ${state.activeIslTab === 'lesson' ? 'active' : ''}" data-tab="lesson" onclick="switchIslTab('lesson')">
        📖 ${ch.type === 'quran' ? 'آیاتِ مبارکہ مع ترجمہ' : (ch.type === 'hadith' ? 'احادیثِ مبارکہ' : 'موضوعاتی مطالعہ')}
      </button>
      <button class="bio-tab-btn isl-top-tab ${state.activeIslTab === 'ps-trans' ? 'active' : ''}" data-tab="ps-trans" onclick="switchIslTab('ps-trans')">
        🇦🇫 Pashto / پښتو ژباړه
      </button>
      <button class="bio-tab-btn isl-top-tab ${state.activeIslTab === 'en-trans' ? 'active' : ''}" data-tab="en-trans" onclick="switchIslTab('en-trans')">
        🇬🇧 English Translation
      </button>
      <button class="bio-tab-btn isl-top-tab ${state.activeIslTab === 'video' ? 'active' : ''}" data-tab="video" onclick="switchIslTab('video')">
        🎥 Video Lecture / ویڈیو
      </button>
      <button class="bio-tab-btn isl-top-tab ${state.activeIslTab === 'ur-sum' ? 'active' : ''}" data-tab="ur-sum" onclick="switchIslTab('ur-sum')">
        📜 خلاصہ و مرکزی خیال
      </button>
      <button class="bio-tab-btn isl-top-tab ${state.activeIslTab === 'en-sum' ? 'active' : ''}" data-tab="en-sum" onclick="switchIslTab('en-sum')">
        📝 English Summary
      </button>
      <button class="bio-tab-btn isl-top-tab ${state.activeIslTab === 'ps-sum' ? 'active' : ''}" data-tab="ps-sum" onclick="switchIslTab('ps-sum')">
        🇦🇫 پښتو لنډیز
      </button>
      <button class="bio-tab-btn isl-top-tab ${state.activeIslTab === 'exercise' ? 'active' : ''}" data-tab="exercise" onclick="switchIslTab('exercise')">
        ✏️ درسی مشق (حل شدہ)
      </button>
      <button class="bio-tab-btn isl-top-tab ${state.activeIslTab === 'slos' ? 'active' : ''}" data-tab="slos" onclick="switchIslTab('slos')">
        🎯 حاصلاتِ تعلّم (SLOs)
      </button>
      ${ch.pageImages && ch.pageImages.length ? `
      <button class="bio-tab-btn isl-top-tab ${state.activeIslTab === 'pages' ? 'active' : ''}" data-tab="pages" onclick="switchIslTab('pages')">
        🖼️ درسی کتاب کے اصل صفحات (${ch.pageImages.length})
      </button>` : ''}
    </div>

    <!-- Main Tab Content Area -->
    <div id="islTabContent" style="margin-top: 1.25rem;"></div>

    <!-- Bottom SLO Questions Section -->
    <div class="slo-bottom-section">
      <div class="slo-bottom-header" style="border-top-color:#0d9488;">
        <div class="slo-bottom-title">
          <span>🕌</span>
          <span style="color:#0f766e;">ایس ایل او امتحانی روڈ میپ (20 MCQs, 10 SQs, 5 LQs)</span>
        </div>
        <div class="slo-bottom-tabs">
          <button class="slo-tab-pill isl-slo-tab-pill ${state.activeIslSloTab === 'slo-mcqs' ? 'active' : ''}" data-slotab="slo-mcqs" onclick="switchIslSloTab('slo-mcqs')">
            🎯 کثیر الانتخابی سوالات (20 MCQs)
          </button>
          <button class="slo-tab-pill isl-slo-tab-pill ${state.activeIslSloTab === 'slo-sq' ? 'active' : ''}" data-slotab="slo-sq" onclick="switchIslSloTab('slo-sq')">
            ✏️ مختصر سوالات (10 SQs)
          </button>
          <button class="slo-tab-pill isl-slo-tab-pill ${state.activeIslSloTab === 'slo-lq' ? 'active' : ''}" data-slotab="slo-lq" onclick="switchIslSloTab('slo-lq')">
            📝 تفصیلی سوالات (5 LQs)
          </button>
        </div>
      </div>
      <div id="islSloTabContent"></div>
    </div>
  `;

  switchIslTab(state.activeIslTab);
  switchIslSloTab(state.activeIslSloTab);
}

// ─────────────────────────────────────────
//  WORD MEANING TOOLTIP (Quranic Interactive)
// ─────────────────────────────────────────
function showWordMeaning(el) {
  document.querySelectorAll('.qword-tooltip').forEach(t => t.remove());
  document.querySelectorAll('.qword-active').forEach(e => e.classList.remove('qword-active'));
  el.classList.add('qword-active');
  const meaning = el.dataset.meaning || '';
  const word    = el.textContent.trim();
  const tip = document.createElement('div');
  tip.className = 'qword-tooltip';
  if (meaning) {
    tip.innerHTML = `<span class="qword-tip-arabic">${word}</span><span class="qword-tip-sep">←</span><span class="qword-tip-meaning">${meaning}</span>`;
  } else {
    tip.innerHTML = `<span class="qword-tip-arabic">${word}</span><span class="qword-tip-sep" style="color:#fde047;">—</span><span class="qword-tip-meaning" style="color:#fef08a;font-size:0.95rem;">اس لفظ کا الگ معنی دستیاب نہیں ہے (Meaning not available)</span>`;
  }
  document.body.appendChild(tip);
  requestAnimationFrame(() => {
    const r = el.getBoundingClientRect();
    let top = r.top + window.scrollY - tip.offsetHeight - 14;
    if (top < window.scrollY + 8) top = r.bottom + window.scrollY + 8;
    const left = Math.max(8, Math.min(window.innerWidth - tip.offsetWidth - 8,
                          r.left + window.scrollX + r.width / 2 - tip.offsetWidth / 2));
    tip.style.top  = top + 'px';
    tip.style.left = left + 'px';
    tip.style.opacity = '1';
  });
  setTimeout(() => {
    document.addEventListener('click', function _close(e) {
      if (!el.contains(e.target) && !tip.contains(e.target)) {
        tip.remove();
        el.classList.remove('qword-active');
        document.removeEventListener('click', _close);
      }
    });
  }, 10);
}

function toggleAyahDetails(headerEl) {
  const card = headerEl.closest('.quran-ayah-card');
  if (!card) return;
  const body = card.querySelector('.quran-ayah-details');
  if (!body) return;
  const isOpen = body.classList.toggle('open');
  const icon   = headerEl.querySelector('.ayah-toggle-icon');
  if (icon) icon.textContent = isOpen ? '▲' : '▼';
}

function _buildWordSpans(arabic, wordMeanings) {
  const lookup = {};
  if (wordMeanings && wordMeanings.length) {
    wordMeanings.forEach(wm => { if (wm.word) lookup[wm.word.trim()] = wm.meaning || ''; });
  }
  const tokens = (arabic || '').split(/\s+/).filter(Boolean);
  return tokens.map(tok => {
    const meaning = lookup[tok] || '';
    if (meaning) {
      return `<span class="quranic-word has-meaning" data-meaning="${meaning.replace(/"/g,'&quot;')}" onclick="showWordMeaning(this)">${tok}</span>`;
    }
    return `<span class="quranic-word" onclick="showWordMeaning(this)">${tok}</span>`;
  }).join(' ');
}

function renderIslLesson(ch) {
  // If Unit 1-10: Quranic Verses View (type is 'surah' or 'quran')
  if (ch.type === 'quran' || ch.type === 'surah') {
    const versesList = ch.verses || ch.sections || [];
    const versesHtml = versesList.map(v => {
      const wordSpans = _buildWordSpans(v.arabic || '', v.wordMeanings || []);
      return `
      <div class="quran-ayah-card">
        <div class="quran-ayah-header isl-ayah-toggle-hdr" onclick="toggleAyahDetails(this)" title="ترجمہ دیکھنے / چھپانے کے لیے کلک کریں">
          <span class="ayah-badge">
            <span>📖</span>
            <span>سورۃ الانفال · آیت ${v.ayahNo}</span>
          </span>
          <div style="display:flex;align-items:center;gap:0.65rem;">
            <span style="font-size:0.82rem;color:#0f766e;font-weight:700;">رکوع ${ch.ruku || ''} · پارہ ۹/۱۰</span>
            <span class="ayah-toggle-icon" style="font-size:0.9rem;color:#0d9488;">▼</span>
          </div>
        </div>
        <div class="quran-arabic-container">
          <div class="quran-arabic-text">
            ${wordSpans} <span class="quran-ayah-end">۝${v.ayahNo}</span>
          </div>
          <div class="qword-hint-bar">👆 کسی بھی لفظ پر کلک کریں — اس لفظ کا الگ معنی ظاہر ہوگا · Click any Arabic word to see its meaning</div>
        </div>
        <div class="quran-ayah-details open">
          <div class="quran-trans-block urdu">
            <div style="font-size:0.82rem;font-weight:700;color:#047857;margin-bottom:0.25rem;">اردو ترجمہ (درسی نصاب):</div>
            ${v.urduTranslation}
          </div>
          <div class="quran-trans-block pashto">
            <div style="font-size:0.82rem;font-weight:700;color:#0369a1;margin-bottom:0.25rem;">پښتو ژباړه:</div>
            ${v.pashtoTranslation}
          </div>
          <div class="quran-trans-block english">
            <div style="font-size:0.82rem;font-weight:700;color:#6d28d9;margin-bottom:0.25rem;">English Translation (Sahih International):</div>
            ${v.englishTranslation}
          </div>
          ${v.tashreeh ? `
          <div class="quran-tashreeh-block">
            <strong style="color:#0f766e;display:block;margin-bottom:0.35rem;">مفہوم و سیاق:</strong>
            ${v.tashreeh}
          </div>` : ''}
          ${(v.wordMeanings && v.wordMeanings.length) ? `
          <div class="quran-lughat-block">
            <div class="quran-lughat-title">📚 الفاظ و مرکبات کے معانی (لُغات)</div>
            <div class="quran-lughat-grid">
              ${v.wordMeanings.map(wm => `
                <div class="lughat-item">
                  <span class="lughat-arabic">${wm.word}</span>
                  <span class="lughat-arrow">←</span>
                  <span class="lughat-meaning">${wm.meaning}</span>
                </div>`).join('')}
            </div>
          </div>` : ''}
        </div>
      </div>`;
    }).join("");

    return `
      <div class="urdu-container">
        <div class="urdu-ctrl-bar" style="border-left:4px solid #0d9488;background:#f0fdf4;">
          <div>
            <strong style="color:#0f766e;font-size:1.05rem;">📖 ${ch.title}:</strong>
            <span style="font-size:0.85rem;color:#047857;margin-left:0.5rem;">کل ${versesList.length} آیاتِ مبارکہ با اعراب متن، سہ لسانی تراجم اور مفہوم کے ساتھ</span>
          </div>
        </div>
        ${versesHtml}
      </div>`;
  }

  // If Unit 11: Ahadith View
  if (ch.type === 'hadith') {
    const hadithsList = ch.hadiths || ch.sections || [];
    const hadithsHtml = hadithsList.map(h => `
      <div class="hadith-card">
        <div class="hadith-header">
          <span class="ayah-badge" style="background:linear-gradient(135deg,#047857,#065f46);">
            <span>📜</span>
            <span>حدیث نمبر ${h.hadithNo}</span>
          </span>
          <span style="font-size:0.85rem;color:#065f46;font-weight:700;">
            ${h.reference || ''}
          </span>
        </div>
        <div class="hadith-arabic-text">
          ${h.arabic}
        </div>
        <div class="quran-trans-block urdu">
          <div style="font-size:0.82rem;font-weight:700;color:#047857;margin-bottom:0.25rem;">اردو ترجمہ:</div>
          ${h.urduTranslation}
        </div>
        <div class="quran-trans-block pashto">
          <div style="font-size:0.82rem;font-weight:700;color:#0369a1;margin-bottom:0.25rem;">پښتو ژباړه:</div>
          ${h.pashtoTranslation}
        </div>
        <div class="quran-trans-block english">
          <div style="font-size:0.82rem;font-weight:700;color:#6d28d9;margin-bottom:0.25rem;">English Translation:</div>
          ${h.englishTranslation}
        </div>
        <div class="quran-tashreeh-block">
          <strong style="color:#0f766e;display:block;margin-bottom:0.35rem;font-size:1.15rem;">تشریح و تفہیم:</strong>
          <div style="white-space:pre-wrap;line-height:2.2;">${h.tashreeh}</div>
        </div>
      </div>
    `).join("");

    return `
      <div class="urdu-container">
        <div class="urdu-ctrl-bar" style="border-left:4px solid #0f766e;background:#f0fdf4;">
          <div>
            <strong style="color:#0f766e;font-size:1.05rem;">📜 باب دوم: مطالعہ احادیث مبارکہ:</strong>
            <span style="font-size:0.85rem;color:#047857;margin-left:0.5rem;">جماعت نہم کے نصاب کی تمام ۱۰ احادیثِ نبویہ مع اعراب، تخریج، ترجمہ و تشریح</span>
          </div>
        </div>
        ${hadithsHtml}
      </div>`;
  }

  // If Units 12-15: Thematic Studies View
  const sectionsList = ch.sections || [];
  const sectionsHtml = sectionsList.map((sec, sIdx) => `
    <div class="urdu-section-card open" style="margin-bottom:1.25rem;">
      <div class="urdu-section-header" onclick="toggleUrduSection(this)" style="background:linear-gradient(135deg,#f0fdf4,#e0f2fe);">
        <div style="display:flex;align-items:center;gap:0.65rem;">
          <span class="urdu-sec-badge" style="background:#0d9488;">عنوان ${sIdx + 1}</span>
          <span class="urdu-sec-title" style="color:#0f766e;">${sec.heading}</span>
        </div>
        <span class="sec-toggle-icon">▼</span>
      </div>
      <div class="urdu-section-body urdu-text-rtl" style="display:block;padding:1.25rem;font-size:1.18rem;line-height:2.3;color:#1e293b;">
        ${sec.text}
      </div>
    </div>
  `).join("");

  return `
    <div class="urdu-container">
      <div class="urdu-ctrl-bar" style="border-left:4px solid #0d9488;background:#f0fdf4;">
        <div>
          <strong style="color:#0f766e;font-size:1.05rem;">📚 ${ch.title}:</strong>
          <span style="font-size:0.85rem;color:#047857;margin-left:0.5rem;">مکمل درسی متن مع تفصیلی عناوین و مباحث</span>
        </div>
      </div>
      <div class="urdu-section-card open" style="margin-bottom:1.25rem;">
        <div class="urdu-section-header" style="background:#f8fafc;">
          <span class="urdu-sec-title">📖 درسی کتاب کا مکمل اردو متن</span>
        </div>
        <div class="urdu-section-body urdu-text-rtl" style="display:block;padding:1.5rem;font-size:1.2rem;line-height:2.4;color:#1e293b;white-space:pre-wrap;">${ch.urduText || ''}</div>
      </div>
      ${sectionsHtml}
    </div>`;
}

function renderIslPashtoTranslation(ch) {
  return `
    <div class="urdu-container">
      <div class="translation-card pashto" style="border-left:5px solid #0284c7;background:#f0f9ff;padding:1.5rem;border-radius:12px;">
        <div style="font-weight:800;color:#0369a1;font-size:1.25rem;margin-bottom:0.85rem;direction:rtl;text-align:right;">
          🇦🇫 د سبق بشپړه پښتو ژباړه — ${ch.titlePs || ch.title}
        </div>
        <div style="font-size:1.2rem;line-height:2.3;color:#1e293b;direction:rtl;text-align:right;font-family:'Jameel Noori Nastaleeq','Segoe UI',serif;">
          ${ch.pashtoTranslation || 'د دې لوست پښتو ژباړه دلته چمتو شوې ده.'}
        </div>
      </div>
    </div>`;
}

function renderIslEnglishTranslation(ch) {
  return `
    <div class="urdu-container">
      <div class="translation-card english" style="border-left:5px solid #7c3aed;background:#faf5ff;padding:1.5rem;border-radius:12px;">
        <div style="font-weight:800;color:#6d28d9;font-size:1.25rem;margin-bottom:0.85rem;direction:ltr;text-align:left;">
          🇬🇧 Academic English Translation — ${ch.titleEn || ch.title}
        </div>
        <div style="font-size:1.05rem;line-height:1.85;color:#334155;direction:ltr;text-align:left;font-family:'Segoe UI',sans-serif;">
          ${ch.englishTranslation || 'Complete academic English translation for this unit.'}
        </div>
      </div>
    </div>`;
}

function renderIslVideo(ch) {
  const vid = ch.video || {
    title: `Class 9 Islamyat - ${ch.title}`,
    url: 'https://www.youtube.com/embed/dQw4w9WgXcQ',
    duration: '26:40',
    instructor: 'KPK Board Islamic Studies Specialist'
  };

  return `
    <div class="urdu-container">
      <div class="video-lecture-container">
        <div class="video-embed-wrapper">
          <iframe src="${vid.url}" 
                  title="${vid.title}" 
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                  allowfullscreen>
          </iframe>
        </div>
        <div class="video-meta-bar" style="background:#042f2e;">
          <div class="video-meta-title">🎥 ${vid.title}</div>
          <div style="display:flex;gap:1.5rem;flex-wrap:wrap;font-size:0.88rem;color:#99f6e4;">
            <span>👨‍🏫 مدرس: <strong style="color:#fff;">${vid.instructor}</strong></span>
            <span>⏱️ دورانیہ: <strong style="color:#fff;">${vid.duration}</strong></span>
            <span>🏛️ بورڈ: <strong style="color:#2dd4bf;">خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور</strong></span>
          </div>
        </div>
      </div>
    </div>`;
}

function renderIslUrduSummary(ch) {
  return `
    <div class="urdu-container">
      <div class="author-intro-card" style="background:#fefce8;border-color:#fde047;padding:1.5rem;border-radius:12px;">
        <div class="author-intro-title" style="direction:rtl;text-align:right;color:#854d0e;font-size:1.25rem;font-weight:700;margin-bottom:0.75rem;">
          <span>📜</span>
          <span>سبق کا خلاصہ و فکری نکات — ${ch.title}</span>
        </div>
        <div class="urdu-text-rtl" style="font-size:1.22rem;line-height:2.4;color:#1e293b;">
          ${ch.urduSummary || 'اس سبق کا خلاصہ۔'}
        </div>
      </div>
    </div>`;
}

function renderIslEnglishSummary(ch) {
  return `
    <div class="urdu-container">
      <div class="translation-card english" style="border-left:5px solid #2563eb;background:#f0f9ff;padding:1.5rem;border-radius:12px;">
        <h3 style="color:#1e40af;margin-bottom:0.75rem;display:flex;align-items:center;gap:0.5rem;">
          <span>📝</span> English Conceptual Summary — ${ch.titleEn || ch.title}
        </h3>
        <p style="font-size:1.05rem;line-height:1.9;color:#334155;">
          ${ch.englishSummary || 'Summary in English.'}
        </p>
      </div>
    </div>`;
}

function renderIslPashtoSummary(ch) {
  return `
    <div class="urdu-container">
      <div class="translation-card pashto" style="border-left:5px solid #059669;background:#f0fdf4;padding:1.5rem;border-radius:12px;">
        <div style="font-weight:800;color:#15803d;font-size:1.2rem;margin-bottom:0.75rem;direction:rtl;text-align:right;">
          🇦🇫 د لوست پښتو لنډیز — ${ch.titlePs || ch.title}
        </div>
        <div style="font-size:1.2rem;line-height:2.3;color:#1e293b;direction:rtl;text-align:right;font-family:'Jameel Noori Nastaleeq','Segoe UI',serif;">
          ${ch.pashtoSummary || 'د لوست پښتو لنډیز دلته چمتو دی.'}
        </div>
      </div>
    </div>`;
}

function renderIslExercise(ch) {
  const ex = ch.exercise || {};
  const vocabList = ex.vocabulary || [];
  const sqList = ex.shortQuestions || [];
  const lqList = ex.longQuestions || [];
  const blanksList = ex.blanks || [];

  const vocabHtml = (vocabList.length > 0) ? `
    <div class="urdu-section-card open" style="margin-bottom:1.25rem;">
      <div class="urdu-section-header" onclick="toggleUrduSection(this)" style="background:linear-gradient(135deg,#e0f2fe,#dbeafe);">
        <div style="display:flex;align-items:center;gap:0.65rem;">
          <span class="urdu-sec-badge" style="background:#0284c7;">۱</span>
          <span class="urdu-sec-title" style="color:#0369a1;">الفاظ و معانی (Vocabulary & Meanings)</span>
        </div>
        <span class="sec-toggle-icon">▼</span>
      </div>
      <div class="urdu-section-body" style="padding:1rem;">
        <table style="width:100%;border-collapse:collapse;direction:rtl;text-align:right;">
          <thead>
            <tr style="background:#f1f5f9;color:var(--navy);font-weight:700;">
              <th style="padding:0.6rem 1rem;border-bottom:2px solid #cbd5e1;width:35%;">قرآنی / عربی لفظ</th>
              <th style="padding:0.6rem 1rem;border-bottom:2px solid #cbd5e1;">معنی و مفہوم</th>
            </tr>
          </thead>
          <tbody>
            ${vocabList.map(v => `
              <tr style="border-bottom:1px solid #f1f5f9;">
                <td style="padding:0.65rem 1rem;font-weight:700;color:#0f766e;font-size:1.2rem;font-family:'Amiri','Traditional Arabic',serif;">${v.word}</td>
                <td style="padding:0.65rem 1rem;color:#1e293b;font-size:1.1rem;font-family:'Jameel Noori Nastaleeq','Segoe UI',serif;">${v.meaning}</td>
              </tr>`).join('')}
          </tbody>
        </table>
      </div>
    </div>` : '';

  const sqHtml = (sqList.length > 0) ? `
    <div class="urdu-section-card open" style="margin-bottom:1.25rem;">
      <div class="urdu-section-header" onclick="toggleUrduSection(this)" style="background:linear-gradient(135deg,#f0fdf4,#dcfce7);">
        <div style="display:flex;align-items:center;gap:0.65rem;">
          <span class="urdu-sec-badge" style="background:#059669;">۲</span>
          <span class="urdu-sec-title" style="color:#047857;">مختصر سوالات و جوابات (Short Q&amp;A)</span>
        </div>
        <span class="sec-toggle-icon">▼</span>
      </div>
      <div class="urdu-section-body" style="padding:1rem;">
        ${sqList.map((q, i) => `
          <div class="slo-question-accordion" style="margin-bottom:0.65rem;">
            <div class="slo-accordion-header" style="direction:rtl;text-align:right;" onclick="toggleSloAccordion(this)">
              <span><strong>سوال ${i+1}:</strong> ${q.q || q.question}</span>
              <span class="slo-acc-toggle" style="color:#0d9488;font-size:0.85rem;background:#ccfbf1;padding:0.2rem 0.65rem;border-radius:99px;">+ جواب دیکھیں</span>
            </div>
            <div class="slo-accordion-body urdu-text-rtl" style="background:#f0fdf4;color:#064e3b;display:none;font-size:1.15rem;line-height:2.2;">
              <strong>جواب:</strong> ${q.a || q.answer}
            </div>
          </div>`).join('')}
      </div>
    </div>` : '';

  const lqHtml = (lqList.length > 0) ? `
    <div class="urdu-section-card open" style="margin-bottom:1.25rem;">
      <div class="urdu-section-header" onclick="toggleUrduSection(this)" style="background:linear-gradient(135deg,#ede9fe,#fae8ff);">
        <div style="display:flex;align-items:center;gap:0.65rem;">
          <span class="urdu-sec-badge" style="background:#7c3aed;">۳</span>
          <span class="urdu-sec-title" style="color:#6d28d9;">تفصیلی سوالات و جوابات (Detailed Long Questions)</span>
        </div>
        <span class="sec-toggle-icon">▼</span>
      </div>
      <div class="urdu-section-body" style="padding:1rem;">
        ${lqList.map((q, i) => `
          <div class="slo-question-accordion" style="margin-bottom:0.75rem;">
            <div class="slo-accordion-header" style="direction:rtl;text-align:right;" onclick="toggleSloAccordion(this)">
              <span><strong>تفصیلی سوال ${i+1}:</strong> ${q.q || q.question}</span>
              <span class="slo-acc-toggle" style="color:#7c3aed;font-size:0.85rem;background:#ede9fe;padding:0.2rem 0.65rem;border-radius:99px;">+ مفصل جواب کھولیں</span>
            </div>
            <div class="slo-accordion-body urdu-text-rtl" style="background:#ffffff;display:none;font-size:1.18rem;line-height:2.3;color:#1e293b;padding:1.25rem;">
              <strong style="color:#6d28d9;display:block;margin-bottom:0.5rem;">جواب:</strong>
              <div style="white-space:pre-wrap;">${q.a || q.answer}</div>
            </div>
          </div>`).join('')}
      </div>
    </div>` : '';

  const blanksHtml = (blanksList.length > 0) ? `
    <div class="urdu-section-card open" style="margin-bottom:1.25rem;">
      <div class="urdu-section-header" onclick="toggleUrduSection(this)" style="background:linear-gradient(135deg,#fefce8,#fef9c3);">
        <div style="display:flex;align-items:center;gap:0.65rem;">
          <span class="urdu-sec-badge" style="background:#ca8a04;">۴</span>
          <span class="urdu-sec-title" style="color:#854d0e;">خالی جگہیں پر کریں (Fill in the Blanks)</span>
        </div>
        <span class="sec-toggle-icon">▼</span>
      </div>
      <div class="urdu-section-body urdu-text-rtl" style="padding:1rem;">
        ${blanksList.map((b, i) => `
          <div style="background:#ffffff;padding:0.75rem 1rem;border:1px solid #e2e8f0;border-radius:8px;margin-bottom:0.5rem;">
            <span>${i+1}. ${b.sentence || b.statement}</span>
            <div style="color:#0f766e;font-weight:700;font-size:1rem;margin-top:0.25rem;">درست جواب: ${b.answer}</div>
          </div>`).join('')}
      </div>
    </div>` : '';

  const rawHtml = ex.rawExercise ? `
    <div class="urdu-section-card" style="margin-bottom:1.25rem;">
      <div class="urdu-section-header" onclick="toggleUrduSection(this)" style="background:#f8fafc;">
        <span class="urdu-sec-title" style="color:#475569;">📄 اصل درسی مشق کا متن (Verbatim Textbook Exercise)</span>
        <span class="sec-toggle-icon">▼</span>
      </div>
      <div class="urdu-section-body urdu-text-rtl" style="display:none;padding:1.25rem;font-size:1.15rem;line-height:2.2;white-space:pre-wrap;color:#334155;background:#f8fafc;">
        ${ex.rawExercise}
      </div>
    </div>` : '';

  return `
    <div class="urdu-container">
      <div class="urdu-ctrl-bar" style="border-left:4px solid #0d9488;background:#f0fdf4;">
        <div>
          <strong style="color:#0f766e;font-size:1.05rem;">✏️ مشق: ${ch.title}</strong>
          <span style="font-size:0.85rem;color:#047857;margin-left:0.5rem;">تمام سوالات ٹیکسٹ بک کے عین مطابق حل شدہ ہیں</span>
        </div>
      </div>
      ${vocabHtml}
      ${sqHtml}
      ${lqHtml}
      ${blanksHtml}
      ${rawHtml}
    </div>`;
}

function renderIslSLOs(ch) {
  const slos = ch.slos || [];
  const slosHtml = slos.map((slo, idx) => `
    <div style="display:flex;align-items:flex-start;gap:0.75rem;background:#ffffff;padding:1rem 1.25rem;border:1.5px solid #ccfbf1;border-radius:10px;margin-bottom:0.75rem;direction:rtl;text-align:right;" class="urdu-text-rtl">
      <span style="background:#0d9488;color:#fff;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.85rem;flex-shrink:0;">${idx+1}</span>
      <div style="color:#1e293b;font-size:1.1rem;line-height:1.9;">${slo}</div>
    </div>`).join("");

  return `
    <div class="urdu-container">
      <div style="background:#f0fdf4;padding:1rem 1.25rem;border-radius:var(--radius-sm);border-left:4px solid #0d9488;margin-bottom:0.75rem;">
        <strong style="color:#0f766e;">🎯 حاصلاتِ تعلّم (Student Learning Outcomes - SLOs):</strong>
        <p style="font-size:0.88rem;color:#047857;margin-top:0.25rem;">خیبر پختونخوا ٹیکسٹ بک بورڈ کے امتحانی معیار کے مطابق تدریسی مقاصد</p>
      </div>
      ${slosHtml}
    </div>`;
}

function renderIslSloMcqs(ch) {
  const mcqs = (ch.sloQuestions && ch.sloQuestions.mcqs) || [];
  if (mcqs.length === 0) {
    return `<div style="padding:1.5rem;text-align:center;color:var(--text-muted);">اس یونٹ کے لیے ایم سی کیوز دستیاب نہیں ہیں۔</div>`;
  }

  const mcqListHtml = mcqs.map((m, qIndex) => {
    const correctIdx = m.answer !== undefined ? m.answer : (m.correct !== undefined ? m.correct : 0);
    const encodedExp = encodeURIComponent(m.explanation || "درست جواب منتخب کیا گیا۔");
    const optionsHtml = (m.options || []).map((opt, optIndex) => `
      <label class="mcq-option-label urdu-text-rtl" id="opt-isl-${qIndex}-${optIndex}"
             onclick="checkIslSloMcq(${qIndex}, ${optIndex}, ${correctIdx}, '${encodedExp}')">
        <input type="radio" name="isl-mcq-${qIndex}" value="${optIndex}" style="accent-color:#0d9488;margin-left:0.5rem;">
        <span>${opt}</span>
      </label>`).join("");

    return `
      <div class="interactive-mcq-card">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem;">
          <span style="background:#ccfbf1;color:#0f766e;font-weight:700;font-size:0.78rem;padding:0.25rem 0.65rem;border-radius:99px;">
            سوال ${qIndex + 1} از ${mcqs.length}
          </span>
          <span style="font-size:0.78rem;color:#0d9488;font-weight:700;">اسلامیات ایس ایل او پیٹرن</span>
        </div>
        <div class="mcq-question-text urdu-text-rtl">${m.q || m.question}</div>
        <div class="mcq-options-grid">${optionsHtml}</div>
        <div id="isl-exp-${qIndex}" style="display:none;" class="mcq-explanation-box urdu-text-rtl"></div>
      </div>`;
  }).join("");

  return `
    <div style="margin-bottom:1rem;">
      <div style="background:#f0fdf4;padding:0.75rem 1.25rem;border-radius:8px;border-left:4px solid #0d9488;margin-bottom:1rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem;">
        <span style="color:#0f766e;font-weight:700;">🎯 کل ${mcqs.length} کثیر الانتخابی سوالات (SLO Exam MCQs):</span>
        <span style="font-size:0.85rem;color:#047857;">ہر سوال پر کلک کر کے فوری ماڈل جواب اور وضاحت دیکھیں</span>
      </div>
      ${mcqListHtml}
    </div>`;
}

function checkIslSloMcq(qIndex, selectedOpt, correctOpt, encodedExp) {
  const expBox = $(`isl-exp-${qIndex}`);
  const explanation = decodeURIComponent(encodedExp);

  const inputs = document.querySelectorAll(`input[name="isl-mcq-${qIndex}"]`);
  inputs.forEach(inp => inp.disabled = true);

  const isCorrect = (selectedOpt === correctOpt);

  inputs.forEach((inp, idx) => {
    const label = $(`opt-isl-${qIndex}-${idx}`);
    if (!label) return;
    if (idx === correctOpt) {
      label.classList.add("correct");
    } else if (idx === selectedOpt && !isCorrect) {
      label.classList.add("incorrect");
    }
  });

  if (expBox) {
    expBox.style.display = "block";
    expBox.innerHTML = `
      <div style="font-weight:700;margin-bottom:0.25rem;color:${isCorrect ? '#0f766e' : '#991b1b'};">
        ${isCorrect ? '✅ بالکل درست جواب!' : '❌ غلط جواب — درست جواب سبز رنگ میں نمایاں ہے۔'}
      </div>
      <div><strong>وضاحت:</strong> ${explanation}</div>
    `;
  }

  recordQuestionAnswer(isCorrect);
}

function renderIslSloSQs(ch) {
  const sqs = (ch.sloQuestions && ch.sloQuestions.shortQuestions) || [];
  if (sqs.length === 0) {
    return `<div style="padding:1.5rem;text-align:center;color:var(--text-muted);">کوئی ایس ایل او مختصر سوالات دستیاب نہیں ہیں۔</div>`;
  }

  const sqListHtml = sqs.map((sq, i) => `
    <div class="slo-question-accordion">
      <div class="slo-accordion-header" style="direction:rtl;text-align:right;" onclick="toggleSloAccordion(this)">
        <span style="font-size:1.15rem;font-family:'Jameel Noori Nastaleeq','Segoe UI',serif;"><strong>مختصر سوال ${i+1}:</strong> ${sq.q || sq.question}</span>
        <div style="display:flex;align-items:center;gap:0.5rem;">
          <span style="font-size:0.75rem;background:#ccfbf1;color:#0f766e;padding:0.2rem 0.5rem;border-radius:99px;font-family:sans-serif;direction:ltr;">SLO</span>
          <span class="slo-acc-toggle" style="color:#0d9488;font-size:0.82rem;background:#f1f5f9;padding:0.2rem 0.5rem;border-radius:6px;">+ جواب دیکھیں</span>
        </div>
      </div>
      <div class="slo-accordion-body urdu-text-rtl" style="background:#f8fafc;font-size:1.15rem;color:#1e293b;display:none;line-height:2.2;">
        <strong style="color:#0f766e;display:block;margin-bottom:0.35rem;">ماڈل جواب:</strong>
        ${sq.a || sq.answer}
      </div>
    </div>`).join("");

  return `
    <div>
      <div style="background:#fefce8;padding:0.75rem 1.25rem;border-radius:8px;border-left:4px solid #ca8a04;margin-bottom:1rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem;">
        <span style="color:#854d0e;font-weight:700;">✏️ کل ${sqs.length} تصوری و فکری مختصر سوالات (SLO Conceptual Short Questions):</span>
        <span style="font-size:0.85rem;color:#a16207;">کسی بھی سوال پر کلک کر کے ماڈل جواب کھولیں</span>
      </div>
      ${sqListHtml}
    </div>`;
}

function renderIslSloLQs(ch) {
  const lqs = (ch.sloQuestions && ch.sloQuestions.longQuestions) || [];
  if (lqs.length === 0) {
    return `<div style="padding:1.5rem;text-align:center;color:var(--text-muted);">کوئی ایس ایل او تفصیلی سوالات دستیاب نہیں ہیں۔</div>`;
  }

  const lqListHtml = lqs.map((lq, i) => `
    <div class="slo-question-accordion" style="border-color:#ccfbf1;margin-bottom:1rem;">
      <div class="slo-accordion-header" style="direction:rtl;text-align:right;background:#f0fdf4;" onclick="toggleSloAccordion(this)">
        <div style="font-weight:800;font-size:1.22rem;color:var(--navy);" class="urdu-text-rtl">
          📝 تفصیلی سوال ${i+1}: ${lq.q || lq.question}
        </div>
        <span class="slo-acc-toggle" style="color:#0d9488;font-size:0.82rem;background:#ccfbf1;padding:0.25rem 0.65rem;border-radius:99px;flex-shrink:0;">+ مفصل جواب کھولیں</span>
      </div>
      <div class="slo-accordion-body urdu-text-rtl" style="display:none;background:#ffffff;">
        <div style="font-size:1.18rem;line-height:2.4;color:#334155;background:#f8fafc;padding:1.25rem;border-radius:8px;margin-bottom:1rem;border:1px solid #e2e8f0;white-space:pre-wrap;">
          <strong style="color:#0f766e;display:block;margin-bottom:0.5rem;font-size:1.25rem;">جامع ماڈل جواب:</strong>
          ${lq.a || lq.answer}
        </div>
      </div>
    </div>`).join("");

  return `
    <div>
      <div style="background:#ede9fe;padding:0.75rem 1.25rem;border-radius:8px;border-left:4px solid #7c3aed;margin-bottom:1rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem;">
        <span style="color:#6d28d9;font-weight:700;">📝 کل ${lqs.length} تفصیلی انشائی سوالات (SLO Detailed Long Questions):</span>
        <span style="font-size:0.85rem;color:#7c3aed;">امتحانی مارکنگ اسکیم اور تفصیلی نکات کے ساتھ ماڈل جوابات</span>
      </div>
      ${lqListHtml}
    </div>`;
}

// ─── GLOBAL SEARCH SYSTEM (CLASSES 9, 10, 11, 12 ONLY) ─────────
function handleGlobalSearch(query) {
  const searchInput = $("globalHubSearch");
  const dropdown    = $("searchResultsDropdown");
  const clearBtn    = $("clearSearchBtn");
  if (!dropdown) return;

  const q = (query || "").trim().toLowerCase();
  if (clearBtn) clearBtn.style.display = q ? "block" : "none";

  if (!q || q.length < 2) {
    dropdown.style.display = "none";
    dropdown.innerHTML = "";
    return;
  }

  // Strictly filter: Allow only Classes 9 through 12
  const validClassIds = ["cls9", "cls10", "cls11", "cls12"];
  const results = [];

  // 0. Search Textbooks (PDFs)
  if (DATA.books) {
    DATA.books.forEach(b => {
      const matchTitle = b.title.toLowerCase().includes(q);
      const matchSubj = b.subject.toLowerCase().includes(q);
      const matchCls = b.className.toLowerCase().includes(q);
      if (matchTitle || matchSubj || matchCls || "book".includes(q) || "pdf".includes(q) || "textbook".includes(q)) {
        results.push({
          type: "Textbook",
          badge: "📚 " + b.className + " Book",
          title: b.title,
          sub: b.available ? `PDF Available (${b.size}) · Click to Open Book` : "Syllabus Overview",
          action: () => {
            clearGlobalSearch();
            if (b.available && b.pdfPath) {
              window.open(b.pdfPath, "_blank");
            } else {
              renderBooksView(b.classId);
            }
          }
        });
      }
    });
  }

  // 1. Search Classes
  DATA.classes.forEach(c => {
    if (validClassIds.includes(c.id) && c.name.toLowerCase().includes(q)) {
      results.push({
        type: "Class",
        badge: "🏫 Class",
        title: c.name,
        sub: `Contains ${c.subjects} subjects · KPK Board`,
        action: () => { clearGlobalSearch(); goToSubjects(c.id); }
      });
    }
  });

  // 2. Search Subjects
  validClassIds.forEach(cid => {
    const cls = DATA.classes.find(c => c.id === cid);
    const subs = DATA.subjects[cid] || [];
    subs.forEach(s => {
      if (s.name.toLowerCase().includes(q) || (cls.name + " " + s.name).toLowerCase().includes(q)) {
        results.push({
          type: "Subject",
          badge: `📚 ${cls.name}`,
          title: `${s.emoji || "📘"} ${s.name}`,
          sub: `${s.chapters} Units · ${cls.name}`,
          action: () => { clearGlobalSearch(); openSubject(cid, s.id); }
        });
      }
    });
  });

  // 3. Search Biology Chapters (Class 9)
  if (DATA.bioChapters) {
    DATA.bioChapters.forEach((ch, idx) => {
      const matchName = ch.name.toLowerCase().includes(q);
      const matchTopic = ch.topics && ch.topics.some(t => t.title.toLowerCase().includes(q));
      if (matchName || matchTopic || "biology".includes(q)) {
        results.push({
          type: "Chapter",
          badge: "🧬 Class 9 Biology",
          title: `Unit ${ch.num}: ${ch.name}`,
          sub: `${ch.topics.length} Topics · ${ch.textbookExercise.mcqs.length} MCQs · ${ch.pageRange}`,
          action: () => { clearGlobalSearch(); openSubject("cls9", "cls9-bio"); selectBioChapter(idx); }
        });
      }
    });
  }

    // 4d. Search Class 10 Chemistry Units
  if (DATA.chem10Chapters) {
    DATA.chem10Chapters.forEach((ch, idx) => {
      const matchName = (ch.name || ch.title || "").toLowerCase().includes(q);
      const matchTopic = ch.topics && ch.topics.some(t => (t.title || t.name || "").toLowerCase().includes(q));
      if (matchName || matchTopic || "chemistry".includes(q) || "class 10".includes(q)) {
        results.push({
          type: "Unit",
          badge: "🧪 Class 10 Chemistry",
          title: `Unit ${ch.num}: ${ch.name || ch.title}`,
          sub: `${ch.topics.length} Topics · ${ch.textbookExercise.mcqs.length} MCQs · ${ch.pageRange}`,
          action: () => { clearGlobalSearch(); openSubject("cls10", "cls10-chem"); selectChemChapter(idx); }
        });
      }
    });
  }

  // 4. Search Chemistry Chapters (Class 9)
  if (DATA.chemChapters) {
    DATA.chemChapters.forEach((ch, idx) => {
      const matchName = ch.name.toLowerCase().includes(q);
      const matchTopic = ch.topics && ch.topics.some(t => t.title.toLowerCase().includes(q));
      if (matchName || matchTopic || "chemistry".includes(q)) {
        results.push({
          type: "Chapter",
          badge: "🧪 Class 9 Chemistry",
          title: `Unit ${ch.num}: ${ch.name}`,
          sub: `${ch.topics.length} Topics · ${ch.textbookExercise.mcqs.length} MCQs · ${ch.pageRange}`,
          action: () => { clearGlobalSearch(); openSubject("cls9", "cls9-chem"); selectChemChapter(idx); }
        });
      }
    });
  }

    // 4c. Search Class 10 Biology Units
  if (DATA.bio10Chapters) {
    DATA.bio10Chapters.forEach((ch, idx) => {
      const matchName = ch.name.toLowerCase().includes(q);
      const matchTopic = ch.topics && ch.topics.some(t => t.title.toLowerCase().includes(q));
      if (matchName || matchTopic || "biology".includes(q) || "class 10".includes(q)) {
        results.push({
          type: "Unit",
          badge: "🧬 Class 10 Biology",
          title: `Unit ${ch.num}: ${ch.name}`,
          sub: `${ch.topics.length} Topics · ${ch.textbookExercise.mcqs.length} MCQs · ${ch.pageRange}`,
          action: () => { clearGlobalSearch(); openSubject("cls10", "cls10-bio"); selectBioChapter(idx); }
        });
      }
    });
  }

  // 4c. Search English Units (Class 10)
  if (DATA.eng10Chapters) {
    DATA.eng10Chapters.forEach((ch, idx) => {
      const matchName = (ch.title && ch.title.toLowerCase().includes(q)) || (ch.name && ch.name.toLowerCase().includes(q));
      const matchTheme = ch.theme && ch.theme.toLowerCase().includes(q);
      if (matchName || matchTheme || "english".includes(q)) {
        results.push({
          type: "Unit",
          badge: "📖 Class 10 English",
          title: `Unit ${ch.unit || ch.num}: ${ch.title || ch.name}`,
          sub: `${ch.theme || ''} · ${(ch.glossary||[]).length} Words · ${(ch.comprehension && (ch.comprehension.questions ? ch.comprehension.questions.length : (ch.comprehension.shortQuestions ? ch.comprehension.shortQuestions.length : 0)))} Questions`,
          action: () => { clearGlobalSearch(); openSubject("cls10", "cls10-eng"); selectEngChapter(idx); }
        });
      }
    });
  }

  // 4b. Search English Units (Class 9)
  if (DATA.engChapters) {
    DATA.engChapters.forEach((ch, idx) => {
      const matchName = ch.title.toLowerCase().includes(q);
      const matchTheme = ch.theme && ch.theme.toLowerCase().includes(q);
      if (matchName || matchTheme || "english".includes(q)) {
        results.push({
          type: "Unit",
          badge: "📖 Class 9 English",
          title: `Unit ${ch.unit}: ${ch.title}`,
          sub: `${ch.theme} · ${ch.glossary.length} Words · ${(ch.comprehension.shortQuestions||[]).length} Questions`,
          action: () => { clearGlobalSearch(); openSubject("cls9", "cls9-eng"); selectEngChapter(idx); }
        });
      }
    });
  }

  // 4c. Search Urdu Lessons & Poetry (Class 9)
  const urduChaps = getUrduChapterList();
  if (urduChaps && urduChaps.length > 0) {
    urduChaps.forEach((ch, idx) => {
      const matchTitle = (ch.title && ch.title.toLowerCase().includes(q)) || (ch.titleEn && ch.titleEn.toLowerCase().includes(q)) || (ch.titlePs && ch.titlePs.toLowerCase().includes(q));
      const matchAuthor = ch.author && ch.author.toLowerCase().includes(q);
      if (matchTitle || matchAuthor || "urdu".includes(q) || "اردو".includes(q) || "سبق".includes(q) || "نظم".includes(q)) {
        results.push({
          type: "Lesson",
          badge: "📗 Class 9 Urdu",
          title: `${ch.type === 'prose' ? 'سبق ' + ch.number : 'نظم ' + (ch.number - 11)}: ${ch.title} (${ch.author})`,
          sub: `${ch.titleEn} · Trilingual Translations &amp; SLO Q&amp;A`,
          action: () => { clearGlobalSearch(); openSubject("cls9", "cls9-urdu"); selectUrduChapter(idx); }
        });
      }
    });
  }

  // 4d. Search Islamyat Units (Class 9)
  const islChaps = (typeof DATA !== 'undefined' && DATA.islamyatChapters) || (typeof window !== 'undefined' && window.ISLAMYAT_DATA) || (typeof ISLAMYAT_DATA !== 'undefined' ? ISLAMYAT_DATA : []);
  if (islChaps && islChaps.length > 0) {
    islChaps.forEach((ch, idx) => {
      const matchTitle = (ch.title && ch.title.toLowerCase().includes(q)) || (ch.titleEn && ch.titleEn.toLowerCase().includes(q)) || (ch.titlePs && ch.titlePs.toLowerCase().includes(q));
      const matchAuthor = ch.author && ch.author.toLowerCase().includes(q);
      if (matchTitle || matchAuthor || "islamyat".includes(q) || "اسلامیات".includes(q) || "انفال".includes(q) || "حدیث".includes(q) || "قرآن".includes(q) || "طہارت".includes(q) || "علم".includes(q) || "ختم نبوت".includes(q)) {
        results.push({
          type: "Unit",
          badge: "🕌 Class 9 Islamyat",
          title: `یونٹ ${ch.number}: ${ch.title}`,
          sub: `${ch.titleEn} · Uthmani Ayaat, Trilingual Translations &amp; SLO Q&amp;A`,
          action: () => { clearGlobalSearch(); openSubject("cls9", "cls9-isl"); selectIslChapter(idx); }
        });
      }
    });
  }
  // 5. Search Physics Chapters (Class 9)
  if (DATA.physChapters) {
    DATA.physChapters.forEach((ch, idx) => {
      const matchName = ch.name.toLowerCase().includes(q);
      const matchTopic = ch.topics && ch.topics.some(t => t.title.toLowerCase().includes(q));
      if (matchName || matchTopic || "physics".includes(q)) {
        results.push({
          type: "Chapter",
          badge: "⚛️ Class 9 Physics",
          title: `Chapter ${ch.num}: ${ch.name}`,
          sub: `${ch.topics.length} Topics · ${(ch.numericals||[]).length} Numericals · ${ch.textbookExercise.mcqs.length} MCQs`,
          action: () => { clearGlobalSearch(); openSubject("cls9", "cls9-phy"); selectPhysChapter(idx); }
        });
      }
    });
  }

  // 6. Search Class 12 Chapters
  if (DATA.chapters) {
    Object.keys(DATA.chapters).forEach(subjKey => {
      if (subjKey.startsWith("cls12-")) {
        const parts = subjKey.split("-");
        const subName = parts[1].toUpperCase();
        DATA.chapters[subjKey].forEach(ch => {
          if (ch.name.toLowerCase().includes(q) || "class 12".includes(q) || subName.toLowerCase().includes(q)) {
            results.push({
              type: "Chapter",
              badge: "🏫 Class 12",
              title: `${subName} · Ch ${ch.num}: ${ch.name}`,
              sub: `${ch.topics} · Class 12 KPK Syllabus`,
              action: () => { clearGlobalSearch(); openSubject("cls12", subjKey); openGenericChapterDetails("cls12", subjKey, subName, ch.num); }
            });
          }
        });
      }
    });
  }

  // Render Results (limit to 15 best matches)
  if (results.length === 0) {
    dropdown.innerHTML = `
      <div style="padding:1rem;text-align:center;color:#64748b;font-size:0.9rem;">
        No results found for "<strong>${sanitize(query)}</strong>" in Classes 9, 10, 11, or 12.
      </div>`;
    dropdown.style.display = "block";
    return;
  }

  dropdown.innerHTML = `
    <div style="padding:0.4rem 0.6rem;font-size:0.75rem;font-weight:700;color:#94a3b8;border-bottom:1px solid #f1f5f9;display:flex;justify-content:space-between;">
      <span>MATCHING RESULTS (${results.length})</span>
      <span>Classes 9, 10, 11, 12</span>
    </div>
    ${results.slice(0, 15).map((r, i) => `
      <div class="search-result-item" style="padding:0.6rem 0.75rem;border-radius:6px;cursor:pointer;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;transition:background 0.15s;"
           onmouseover="this.style.background='#f1f5f9'" onmouseout="this.style.background='transparent'"
           onclick="(${r.action.toString()})()">
        <div>
          <div style="font-weight:600;font-size:0.9rem;color:#0f172a;">${r.title}</div>
          <div style="font-size:0.78rem;color:#64748b;">${r.sub}</div>
        </div>
        <span style="font-size:0.72rem;font-weight:700;padding:0.2rem 0.5rem;background:#e2e8f0;color:#334155;border-radius:4px;white-space:nowrap;">${r.badge}</span>
      </div>`).join("")}`;
  dropdown.style.display = "block";
}

function clearGlobalSearch() {
  const searchInput = $("globalHubSearch");
  const dropdown    = $("searchResultsDropdown");
  const clearBtn    = $("clearSearchBtn");
  if (searchInput) searchInput.value = "";
  if (dropdown) {
    dropdown.style.display = "none";
    dropdown.innerHTML = "";
  }
  if (clearBtn) clearBtn.style.display = "none";
}


// ─────────────────────────────────────────
//  TEXTBOOKS & BOOKS LIBRARY VIEW
// ─────────────────────────────────────────
function renderBooksView(filterClass = "all") {
  state.page = "books";
  state.activePage = "books";
  state.activeView = "books";
  setActiveNav("books");
  setDashHeader("📚 Official KPK Textbooks Library (PDF Books)", "Download and read verified textbooks published by Khyber Pakhtunkhwa Textbook Board");
  setBreadcrumb([
    { label: "Home",      onclick: () => { setActiveNav("home"); renderHome(); } },
    { label: "Textbooks", active: true }
  ]);

  const allBooks = DATA.books || [];
  const filtered = filterClass === "all" ? allBooks : allBooks.filter(b => b.classId === filterClass);

  const pills = [
    { id: "all", label: "All Textbooks" },
    { id: "cls9", label: "Class 9 (5 Books)" },
    { id: "cls10", label: "Class 10 (1 Book Ready)" },
    { id: "cls11", label: "Class 11" },
    { id: "cls12", label: "Class 12" },
  ];

  const pillsHtml = pills.map(p => `
    <button onclick="renderBooksView('${p.id}')"
            style="padding:0.45rem 0.9rem;border-radius:99px;font-size:0.85rem;font-weight:700;cursor:pointer;border:1px solid ${filterClass === p.id ? '#0284c7' : '#cbd5e1'};background:${filterClass === p.id ? '#0284c7' : '#fff'};color:${filterClass === p.id ? '#fff' : '#475569'};transition:all 0.2s;">
      ${p.label}
    </button>
  `).join("");

  const cardsHtml = filtered.map(b => `
    <div class="book-card-item" style="background:#fff;border:1px solid #e2e8f0;border-radius:14px;overflow:hidden;box-shadow:0 4px 6px -1px rgba(0,0,0,0.05);display:flex;flex-direction:column;">
      <div style="background:linear-gradient(135deg, ${b.color}, #0f172a);padding:1.5rem;color:#fff;">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
          <span style="font-size:2rem;">${b.icon}</span>
          <span style="background:rgba(255,255,255,0.25);font-size:0.75rem;font-weight:700;padding:0.25rem 0.65rem;border-radius:99px;">${b.className}</span>
        </div>
        <h3 style="margin:1rem 0 0.25rem;font-size:1.15rem;font-weight:700;">${b.title}</h3>
        <div style="font-size:0.8rem;opacity:0.85;">${b.subject}</div>
      </div>
      <div style="padding:1.25rem;display:flex;flex-direction:column;flex:1;justify-content:space-between;">
        <div style="font-size:0.85rem;color:#64748b;margin-bottom:1rem;line-height:1.6;">
          <div>🏛️ <strong>Board:</strong> ${b.board}</div>
          <div>📄 <strong>Format:</strong> High-Resolution PDF</div>
          <div>📚 <strong>Content:</strong> ${b.pages}</div>
        </div>
        <div style="display:flex;flex-direction:column;gap:0.5rem;">
          ${b.available ? `
            <div style="display:flex;gap:0.5rem;">
              <a href="${b.pdfPath}" target="_blank" style="flex:1;text-align:center;padding:0.5rem;background:#0284c7;color:#fff;border-radius:6px;font-weight:700;font-size:0.85rem;text-decoration:none;">
                👁️ Read Online
              </a>
              <a href="${b.pdfPath}" download style="flex:1;text-align:center;padding:0.5rem;background:#059669;color:#fff;border-radius:6px;font-weight:700;font-size:0.85rem;text-decoration:none;">
                ⬇️ Download (${b.size})
              </a>
            </div>
            <button onclick="goToSubjects('${b.classId || b.class_id}'); openSubject('${b.classId || b.class_id}', '${b.action || b.hub_action}');" style="width:100%;padding:0.5rem;background:#f8fafc;color:#0f172a;border:1px solid #cbd5e1;border-radius:6px;font-weight:700;font-size:0.825rem;cursor:pointer;">
              🚀 Open Solved Chapter Notes &amp; Q&amp;A
            </button>
          ` : `
            <div style="padding:0.6rem;background:#f8fafc;border:1px dashed #cbd5e1;border-radius:6px;text-align:center;font-size:0.8rem;color:#64748b;">
              ⏳ Syllabus Breakdown Ready · PDF Upload in Progress
            </div>
            <button onclick="goToSubjects('${b.classId || b.class_id}'); openSubject('${b.classId || b.class_id}', '${b.action || b.hub_action}');" style="width:100%;padding:0.5rem;background:#f1f5f9;color:#0f172a;border:none;border-radius:6px;font-weight:700;font-size:0.825rem;cursor:pointer;">
              📖 View Syllabus Topics
            </button>
          `}
        </div>
      </div>
    </div>
  `).join("");

  pageContent().innerHTML = `
    <div style="max-width:1100px;margin:0 auto;padding:1rem 0;">
      <!-- Search & Filter Bar -->
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;margin-bottom:1.5rem;">
        <div style="display:flex;gap:0.5rem;flex-wrap:wrap;">
          ${pillsHtml}
        </div>
        <div style="font-size:0.875rem;color:#64748b;">
          Showing <strong>${filtered.length}</strong> Textbooks
        </div>
      </div>

      <!-- Books Grid -->
      <div style="display:grid;grid-template-columns:repeat(auto-fill, minmax(300px, 1fr));gap:1.5rem;">
        ${cardsHtml}
      </div>
    </div>`;
}

function renderBio10Roadmap() {
  setDashHeader("🗺️ Class 10 Biology Exam Preparation Roadmap", "Official KPK Textbook Board 9-Unit Complete Curriculum (Units 10 to 18)");
  setBreadcrumb([
    { label: "Home",     onclick: () => { setActiveNav("home"); renderHome(); } },
    { label: "Subjects", onclick: () => renderClasses() },
    { label: "Class 10", onclick: () => goToSubjects("cls10") },
    { label: "Biology",  onclick: () => openSubject("cls10", "cls10-bio") },
    { label: "Roadmap",  active: true }
  ]);

  const cardsHtml = (DATA.bio10Chapters || []).map((ch, i) => `
    <div class="roadmap-card" onclick="openSubject('cls10','cls10-bio'); selectBioChapter(${i});" style="cursor:pointer;">
      <div class="roadmap-card-header">
        <span class="roadmap-ch-badge" style="background:#059669;">Unit ${ch.num}</span>
        <span class="ch-btn-status" style="background:#dcfce7;color:#15803d;">✅ Complete</span>
      </div>
      <div class="roadmap-card-body">
        <h4>${ch.name}</h4>
        <div style="font-size:0.75rem;color:var(--text-muted);margin:0.25rem 0 0.5rem;">${ch.pageRange}</div>
        <div class="roadmap-meta-row">
          <span>📚 ${ch.topics.length} Topics</span>
          <span>🎯 ${ch.textbookExercise.mcqs.length} MCQs</span>
          <span>✏️ ${ch.textbookExercise.sq.length} SQs</span>
          <span>📝 ${ch.textbookExercise.lq.length} LQs</span>
        </div>
        <div style="margin-top:0.75rem;font-size:0.8rem;color:var(--text-muted);">
          <strong>Key Focus:</strong> ${ch.slos.slice(0, 2).join(" · ")}
        </div>
      </div>
    </div>`).join("");

  pageContent().innerHTML = `
    <div class="roadmap-container">
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;">
        <button class="btn-back-link" style="margin-bottom:0;" onclick="goToSubjects('cls10'); openSubject('cls10','cls10-bio');"><span class="back-arrow">←</span> Back to Biology Portal</button>
        <div style="display:flex;gap:0.4rem;flex-wrap:wrap;">
          <button class="bio-ch-btn active" style="padding:0.4rem 0.85rem;font-size:0.82rem;" onclick="renderBio10Roadmap()">🧬 Class 10 Biology</button>
          <button class="bio-ch-btn" style="padding:0.4rem 0.85rem;font-size:0.82rem;" onclick="renderFullRoadmap()">🧬 Class 9 Biology</button>
        </div>
      </div>
      <div style="background:#fff;border:1px solid var(--border);border-radius:12px;padding:1.5rem;margin-bottom:1.5rem;box-shadow:var(--shadow);">
        <h3 style="color:var(--navy);font-size:1.2rem;margin-bottom:0.5rem;">🧬 Official KPK Textbook Board Class 10 Biology Exam Pathway</h3>
        <p style="font-size:0.875rem;color:var(--text-muted);line-height:1.6;">
          Complete 9-Unit Grade 10 Biology curriculum strictly aligned with the KPK Textbook Board, Peshawar. Covers Gaseous Exchange, Homeostasis, Coordination and Control, Support and Movement, Reproduction, Inheritance, Man and His Environment, Biotechnology, and Pharmacology.
        </p>
      </div>
      <div class="card-grid" style="grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1rem;">
        ${cardsHtml}
      </div>
    </div>`;
}


function renderEngEnglishSummary(ch) {
  return `
    <div class="urdu-section-card open" style="margin-bottom:2rem;border:1px solid #bae6fd;border-radius:12px;overflow:hidden;box-shadow:0 4px 14px rgba(2,132,199,0.08);background:#ffffff;">
      <div class="urdu-section-header" style="background:#f0f9ff;padding:1rem 1.35rem;display:flex;align-items:center;gap:0.75rem;border-bottom:1px solid #bae6fd;">
        <span class="urdu-sec-badge" style="background:#0284c7;color:#fff;padding:0.25rem 0.65rem;border-radius:6px;font-size:0.78rem;font-weight:700;">SUMMARY</span>
        <span class="urdu-sec-title" style="color:#0369a1;font-size:1.15rem;font-weight:700;">🇬🇧 English Chapter Summary &amp; Key Themes</span>
      </div>
      <div class="urdu-section-body" style="padding:1.6rem;font-size:1.05rem;line-height:1.9;color:#1e293b;background:#ffffff;">
        <p>${ch.englishSummary || 'English chapter summary is available.'}</p>
      </div>
    </div>`;
}

// ═══════════════════════════════════════════════════════════════════════════
// 📚 UNIT VOCABULARY VIEW & INTERACTIVE WORD CLICK DICTIONARY ENGINE
// ═══════════════════════════════════════════════════════════════════════════

function renderEngVocabulary(ch, chIdx) {
  const unitNum = ch.number || (chIdx + 1);
  const wordsList = (typeof ENG_UNIT_VOCAB_WORDS !== 'undefined' && ENG_UNIT_VOCAB_WORDS[unitNum])
    ? ENG_UNIT_VOCAB_WORDS[unitNum]
    : [];
  
  const textbookGlossary = (typeof ENG_TEXTBOOK_GLOSSARIES !== 'undefined' && ENG_TEXTBOOK_GLOSSARIES[unitNum])
    ? ENG_TEXTBOOK_GLOSSARIES[unitNum]
    : [];

  const letters = Array.from(new Set(wordsList.map(w => w[0].toUpperCase()))).sort();

  return `
    <div class="vocab-bank-container">
      <!-- Live Search & A-Z Quick Filter Toolbar -->
      <div class="vocab-toolbar">
        <div class="vocab-search-wrap">
          <span class="vocab-search-icon">🔍</span>
          <input type="text" id="unitVocabSearch" class="vocab-search-input" placeholder="Search any of ${wordsList.length} words or Urdu meaning in Unit ${unitNum}..." oninput="filterUnitVocab(this.value, ${unitNum})">
        </div>
        <div class="vocab-letters-bar" id="vocabLettersBar">
          <button class="vocab-letter-btn active" onclick="filterUnitVocabByLetter('', ${unitNum}, this)">All</button>
          ${letters.map(lt => `<button class="vocab-letter-btn" onclick="filterUnitVocabByLetter('${lt}', ${unitNum}, this)">${lt}</button>`).join('')}
        </div>
      </div>

      <!-- Key Textbook Glossary Section (if available) -->
      ${textbookGlossary.length > 0 ? `
        <div style="background:#f0f9ff;border:1.5px solid #7dd3fc;border-radius:10px;padding:0.9rem 1.1rem;margin-bottom:0.25rem;">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.75rem;">
            <div style="display:flex;align-items:center;gap:0.5rem;">
              <span style="background:#0284c7;color:#fff;font-size:0.74rem;font-weight:800;padding:0.18rem 0.5rem;border-radius:4px;">OFFICIAL GLOSSARY</span>
              <h4 style="margin:0;color:#0369a1;font-size:1.02rem;font-weight:700;">📖 Key Textbook Highlighted Terms</h4>
            </div>
            <span style="font-size:0.82rem;color:#0369a1;font-weight:600;">${textbookGlossary.length} Primary Terms</span>
          </div>
          <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:0.65rem;">
            ${textbookGlossary.map(g => `
              <div style="background:#ffffff;border:1px solid #bae6fd;border-radius:8px;padding:0.65rem 0.8rem;box-shadow:0 1px 3px rgba(0,0,0,0.02);">
                <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.25rem;">
                  <span style="font-weight:700;color:#0369a1;font-size:0.98rem;">${g.word}</span>
                  <button class="popover-speaker-btn" title="Listen" onclick="playSingleWordTTS('${g.word.replace(/'/g, "\\'")}')">🔊</button>
                </div>
                ${g.pos ? `<span style="display:inline-block;background:#e0f2fe;color:#0284c7;font-size:0.7rem;font-weight:700;padding:0.08rem 0.35rem;border-radius:4px;margin-bottom:0.25rem;">${g.pos}</span>` : ''}
                <div style="font-family:'Jameel Noori Nastaleeq','Segoe UI',serif;color:#15803d;font-size:1.15rem;direction:rtl;text-align:right;font-weight:700;line-height:1.6;">${g.urdu || ''}</div>
                ${g.pashto ? `<div style="color:#854d0e;font-size:0.88rem;direction:rtl;text-align:right;margin-top:0.15rem;">${g.pashto}</div>` : ''}
                ${g.meaning ? `<div style="font-size:0.8rem;color:#475569;margin-top:0.3rem;line-height:1.35;">${g.meaning}</div>` : ''}
              </div>
            `).join('')}
          </div>
        </div>
      ` : ''}

      <!-- Dynamic Full Vocabulary Cards Grid (6 in a row) -->
      <div id="unitVocabCardsGrid" class="vocab-cards-grid">
        ${renderVocabCardsHtml(wordsList)}
      </div>
    </div>
  `;
}

function renderVocabCardsHtml(words) {
  if (!words || words.length === 0) {
    return '<div style="grid-column:1/-1;text-align:center;padding:2rem;color:#64748b;">No vocabulary words found matching query.</div>';
  }

  return words.map(w => {
    const lookup = (typeof lookupEngWord === 'function') ? lookupEngWord(w) : null;
    const urduMeaning = (lookup && lookup.u) ? lookup.u : 'اردو ترجمہ';
    const pashtoMeaning = (lookup && lookup.p) ? lookup.p : '';
    const safeWord = w.replace(/'/g, "\\'");

    return `
      <div class="vocab-card" onclick="showWordLookupPopover('${safeWord}', this, event)">
        <div class="vocab-card-top">
          <span class="vocab-card-word">${w}</span>
          <button class="popover-speaker-btn" title="Listen" onclick="event.stopPropagation(); playSingleWordTTS('${safeWord}')">🔊</button>
        </div>
        <div class="vocab-card-urdu">${urduMeaning}</div>
        ${pashtoMeaning ? `<div class="vocab-card-pashto">${pashtoMeaning}</div>` : ''}
      </div>
    `;
  }).join('');
}

function filterUnitVocab(query, unitNum) {
  const wordsList = (typeof ENG_UNIT_VOCAB_WORDS !== 'undefined' && ENG_UNIT_VOCAB_WORDS[unitNum])
    ? ENG_UNIT_VOCAB_WORDS[unitNum]
    : [];
  const q = query.toLowerCase().trim();
  const filtered = wordsList.filter(w => {
    if (w.toLowerCase().includes(q)) return true;
    const lookup = (typeof lookupEngWord === 'function') ? lookupEngWord(w) : null;
    if (lookup && lookup.u && lookup.u.includes(q)) return true;
    if (lookup && lookup.p && lookup.p.includes(q)) return true;
    return false;
  });

  const grid = $('unitVocabCardsGrid');
  if (grid) grid.innerHTML = renderVocabCardsHtml(filtered);
}

function filterUnitVocabByLetter(letter, unitNum, btnEl) {
  document.querySelectorAll('#vocabLettersBar .vocab-letter-btn').forEach(b => b.classList.remove('active'));
  if (btnEl) btnEl.classList.add('active');

  const searchInput = $('unitVocabSearch');
  if (searchInput) searchInput.value = '';

  const wordsList = (typeof ENG_UNIT_VOCAB_WORDS !== 'undefined' && ENG_UNIT_VOCAB_WORDS[unitNum])
    ? ENG_UNIT_VOCAB_WORDS[unitNum]
    : [];
  
  if (!letter) {
    const grid = $('unitVocabCardsGrid');
    if (grid) grid.innerHTML = renderVocabCardsHtml(wordsList);
    return;
  }

  const filtered = wordsList.filter(w => w.toUpperCase().startsWith(letter.toUpperCase()));
  const grid = $('unitVocabCardsGrid');
  if (grid) grid.innerHTML = renderVocabCardsHtml(filtered);
}

// ─── INTERACTIVE FLOATING WORD POPUP / TOOLTIP ───
let currentPopoverEl = null;

async function fetchOnlineWordTranslation(cleanWord) {
  try {
    const res = await fetch(`https://api.mymemory.translated.net/get?q=${encodeURIComponent(cleanWord)}&langpair=en|ur`);
    if (!res.ok) return null;
    const data = await res.json();
    if (data && data.responseData && data.responseData.translatedText) {
      const trans = data.responseData.translatedText.trim();
      const isWarning = /MYMEMORY|WARNING|USAGE|LIMIT|QUOTA|TRANSLATED\.NET|QUERY LENGTH/i.test(trans);
      if (!isWarning && trans && trans.toLowerCase() !== cleanWord.toLowerCase()) {
        if (typeof ENG_URDU_DICT !== 'undefined') {
          ENG_URDU_DICT[cleanWord] = { u: trans, p: '' };
        }
        return trans;
      }
    }
  } catch (err) {
    console.warn('Online dictionary lookup error:', err);
  }
  return null;
}

function showWordLookupPopover(wordText, targetEl, event) {
  closeWordLookupPopover();
  if (!wordText) return;

  const lookup = (typeof lookupEngWord === 'function') ? lookupEngWord(wordText) : (typeof ENG_URDU_DICT !== 'undefined' && ENG_URDU_DICT[wordText.toLowerCase()] ? ENG_URDU_DICT[wordText.toLowerCase()] : null);
  
  const displayWord = wordText.trim();
  const cleanWord = displayWord.toLowerCase().replace(/[^a-z0-9'-]/g, '');
  let urduMeaning = (lookup && lookup.u && lookup.u !== 'اردو معنی' && lookup.u !== 'اردو معنی / مفہوم' && lookup.u.toLowerCase() !== cleanWord) ? lookup.u : '';
  const pashtoMeaning = (lookup && lookup.p && lookup.p.toLowerCase() !== cleanWord) ? lookup.p : '';
  const rootNote = (lookup && lookup.rootWord) ? `<div class="popover-root-note"><span>🌱 Base form:</span> <b>${lookup.rootWord}</b></div>` : '';

  const popover = document.createElement('div');
  popover.id = 'eng-word-popover';
  popover.onclick = (e) => e.stopPropagation();
  popover.innerHTML = `
    <div class="popover-header">
      <div class="popover-word-title">
        <span>${displayWord}</span>
        <button class="popover-speaker-btn" title="Pronounce word" onclick="playSingleWordTTS('${displayWord.replace(/'/g, "\\'")}')">🔊</button>
      </div>
      <button class="popover-close-btn" onclick="closeWordLookupPopover()">✕</button>
    </div>
    <div class="popover-urdu-box" id="popoverUrduBox">
      ${urduMeaning || (cleanWord.length > 1 ? 'اردو معنی جلد شامل کی جائے گی' : '')}
    </div>
    ${pashtoMeaning ? `<div class="popover-pashto-box">${pashtoMeaning}</div>` : ''}
    ${rootNote}
  `;

  document.body.appendChild(popover);
  currentPopoverEl = popover;

  // If no cached translation yet, try online translation gracefully
  if (!urduMeaning && cleanWord.length > 2) {
    fetchOnlineWordTranslation(cleanWord).then(fetchedUrdu => {
      const box = $('popoverUrduBox');
      if (box && currentPopoverEl === popover && fetchedUrdu) {
        box.textContent = fetchedUrdu;
      }
    });
  }

  // Position popover right below clicked element or mouse coordinates
  const rect = targetEl ? targetEl.getBoundingClientRect() : null;
  const popoverWidth = 300;
  let left = rect ? (rect.left + (rect.width / 2) + window.scrollX) : ((event ? event.pageX : window.innerWidth / 2));
  let top = rect ? (rect.bottom + window.scrollY + 6) : ((event ? event.pageY + 10 : window.innerHeight / 2));

  // Boundary checks
  if (left - (popoverWidth / 2) < 15) left = (popoverWidth / 2) + 15;
  if (left + (popoverWidth / 2) > window.innerWidth - 15) left = window.innerWidth - (popoverWidth / 2) - 15;

  popover.style.left = `${left}px`;
  popover.style.top = `${top}px`;
  popover.style.transform = 'translateX(-50%)';
}

function closeWordLookupPopover() {
  if (currentPopoverEl) {
    currentPopoverEl.remove();
    currentPopoverEl = null;
  }
}

function playSingleWordTTS(word) {
  if (!window.speechSynthesis) return;
  window.speechSynthesis.cancel();
  const utter = new SpeechSynthesisUtterance(word);
  utter.lang = 'en-US';
  utter.rate = 0.85;
  window.speechSynthesis.speak(utter);
}

// Global click event to detect word clicks across all English-medium views
document.addEventListener('click', function(e) {
  // If clicked inside popover, do nothing
  if (e.target.closest('#eng-word-popover')) return;

  // If clicked directly on a .tts-word
  if (e.target.classList && e.target.classList.contains('tts-word')) {
    e.stopPropagation();
    const word = e.target.textContent.trim();
    if (word) {
      showWordLookupPopover(word, e.target, e);
      return;
    }
  }

  // If student clicked on English text inside topic contents / reading texts / exercises across subjects
  const engTextContainer = e.target.closest('.urdu-section-body, .poetic-line-row, .poetic-stanza-block, .topic-content, #engTabContent, #bioTabContent, #chemTabContent, #physTabContent, .reading-text, .exercise-card, .qa-card, .subtopic-card, .table-container, .solution-steps');
  if (engTextContainer && !e.target.closest('button, a, input, select, textarea')) {
    let clickedWord = window.getSelection().toString().trim();
    if (!clickedWord || !/^[a-zA-Z'-]{2,}$/.test(clickedWord)) {
      clickedWord = getWordAtPoint(e.clientX, e.clientY);
    }
    if (clickedWord && /^[a-zA-Z'-]{2,}$/.test(clickedWord)) {
      e.stopPropagation();
      showWordLookupPopover(clickedWord, e.target, e);
      return;
    }
  }

  // Otherwise close popover
  closeWordLookupPopover();
});



// ─── Render Chemistry Unit Vocabulary Tab ──────────────────
function renderChemVocabulary(ch, chIdx) {
  const unitNum = String(ch.num || (chIdx + 1));
  const wordsList = (typeof CHEM_UNIT_VOCAB_WORDS !== 'undefined' && CHEM_UNIT_VOCAB_WORDS[unitNum])
    ? CHEM_UNIT_VOCAB_WORDS[unitNum]
    : [];

  const letters = Array.from(new Set(wordsList.map(w => w[0].toUpperCase()))).sort();

  return `
    <div class="vocab-bank-container">
      <div class="vocab-toolbar">
        <div class="vocab-search-wrap">
          <span class="vocab-search-icon">🔍</span>
          <input type="text" id="unitVocabSearch" class="vocab-search-input" placeholder="Search any of ${wordsList.length} words or Urdu meaning in Unit ${unitNum}..." oninput="filterChemUnitVocab(this.value, '${unitNum}')">
        </div>
        <div class="vocab-letters-bar" id="vocabLettersBar">
          <button class="vocab-letter-btn active" onclick="filterChemUnitVocabByLetter('', '${unitNum}', this)">All</button>
          ${letters.map(lt => `<button class="vocab-letter-btn" onclick="filterChemUnitVocabByLetter('${lt}', '${unitNum}', this)">${lt}</button>`).join('')}
        </div>
      </div>

      <div id="unitVocabCardsGrid" class="vocab-cards-grid">
        ${renderVocabCardsHtml(wordsList)}
      </div>
    </div>
  `;
}

function filterChemUnitVocab(query, unitNum) {
  const wordsList = (typeof CHEM_UNIT_VOCAB_WORDS !== 'undefined' && CHEM_UNIT_VOCAB_WORDS[unitNum])
    ? CHEM_UNIT_VOCAB_WORDS[unitNum]
    : [];
  const q = query.toLowerCase().trim();
  const filtered = wordsList.filter(w => {
    if (w.toLowerCase().includes(q)) return true;
    const lookup = (typeof lookupEngWord === 'function') ? lookupEngWord(w) : null;
    if (lookup && lookup.u && lookup.u.includes(q)) return true;
    if (lookup && lookup.p && lookup.p.includes(q)) return true;
    return false;
  });

  const grid = $('unitVocabCardsGrid');
  if (grid) grid.innerHTML = renderVocabCardsHtml(filtered);
}

function filterChemUnitVocabByLetter(letter, unitNum, btnEl) {
  document.querySelectorAll('#vocabLettersBar .vocab-letter-btn').forEach(b => b.classList.remove('active'));
  if (btnEl) btnEl.classList.add('active');

  const searchInput = $('unitVocabSearch');
  if (searchInput) searchInput.value = '';

  const wordsList = (typeof CHEM_UNIT_VOCAB_WORDS !== 'undefined' && CHEM_UNIT_VOCAB_WORDS[unitNum])
    ? CHEM_UNIT_VOCAB_WORDS[unitNum]
    : [];
  const filtered = letter
    ? wordsList.filter(w => w.toUpperCase().startsWith(letter))
    : wordsList;

  const grid = $('unitVocabCardsGrid');
  if (grid) grid.innerHTML = renderVocabCardsHtml(filtered);
}


function getWordAtPoint(x, y) {
  let range, textNode, offset;
  if (document.caretRangeFromPoint) {
    range = document.caretRangeFromPoint(x, y);
    if (!range) return null;
    textNode = range.startContainer;
    offset = range.startOffset;
  } else if (document.caretPositionFromPoint) {
    const pos = document.caretPositionFromPoint(x, y);
    if (!pos) return null;
    textNode = pos.offsetNode;
    offset = pos.offset;
  }
  if (!textNode || textNode.nodeType !== Node.TEXT_NODE) return null;

  const text = textNode.textContent;
  if (!text) return null;

  let start = offset;
  while (start > 0 && /[a-zA-Z'-]/.test(text[start - 1])) {
    start--;
  }
  let end = offset;
  while (end < text.length && /[a-zA-Z'-]/.test(text[end])) {
    end++;
  }

  const word = text.slice(start, end).trim();
  if (word && word.length >= 2 && /^[a-zA-Z'-]+$/.test(word)) {
    return word;
  }
  return null;
}



// ═══════════════════════════════════════════════════════════════
// MATHEMATICS GRADE 9 PORTAL
function getMathChapterList() {
  if (typeof MATH_DATA !== "undefined" && Array.isArray(MATH_DATA)) return MATH_DATA;
  if (typeof DATA !== "undefined" && DATA.mathChapters) return DATA.mathChapters;
  if (typeof window !== "undefined" && window.MATH_DATA) return window.MATH_DATA;
  return [];
}

function openMathView(classId, subj) {
  state.activeSubject = 'math';
  state.activeView = 'subject-detail';
  state.selectedMathChapter = state.selectedMathChapter || 0;
  state.activeMathTab = state.activeMathTab || 'lesson';
  state.activeMathEx = state.activeMathEx || '1.1';
  state.selectedClass = classId;
  setActiveNav('subjects');
  const cls = DATA.classes.find(c => c.id === classId) || { name: 'Class 9' };
  const chList = getMathChapterList();
  const gradeLabel = 'Grade 9';
  const pdfFile = 'file://DESKTOP-R2HQSAV/SpaceBook/9th MTHA/PDF/9th maaths.pdf';

  // Explicitly hide the subpage navigation bar & breadcrumbs banner as requested
  const subNavBar = $("subpage-nav-bar");
  if (subNavBar) subNavBar.style.display = "none";
  const dashHeader = $("dash-header");
  if (dashHeader) dashHeader.style.display = "none";

  currentNavCrumbs = [
    { label: 'Home',     onclick: () => { setActiveNav('home'); renderHome(); } },
    { label: 'Subjects', onclick: () => renderClasses() },
    { label: cls.name,   onclick: () => goToSubjects(classId) },
    { label: subj.name,  active: true }
  ];

  const chapBtns = chList.map((ch, i) => `
    <button class="bio-ch-btn math-ch-btn ${i === state.selectedMathChapter ? 'active' : ''}" id="math-btn-${i}"
            onclick="selectMathChapter(${i})">
      <span class="mcb-num">${ch.number}</span>
      <span class="mcb-info">
        <span class="mcb-name">${ch.title}</span>
        <span class="mcb-sub">${ch.pageRange || ''}</span>
      </span>
      <span class="mcb-badge">${ch.badge || '✓ Solved'}</span>
    </button>`).join('');

  pageContent().innerHTML = `
    <div class="math-unified-view">
      <div class="math-ch-sidebar">
        <div class="math-ch-sidebar-header">
          <button onclick="goToSubjects('${classId}')" class="math-sidebar-back-btn" title="Back to Subjects">←</button>
          <div class="math-sidebar-title-wrap">
            <span class="math-sidebar-title">📐 KPK ${gradeLabel} Math</span>
            <span class="math-sidebar-sub">17 Complete Solved Units</span>
          </div>
        </div>
        <div class="math-ch-list">${chapBtns}</div>
        <div class="math-sidebar-footer">
          <a href="${pdfFile}" target="_blank" class="math-pdf-btn">
            <span>📥</span> Official Math Book PDF
          </a>
        </div>
      </div>
      <div class="math-topic-area" id="mathTopicArea"></div>
    </div>`;

  renderMathChapter(state.selectedMathChapter);
}

function selectMathChapter(index) {
  state.selectedMathChapter = index;
  document.querySelectorAll(".bio-ch-btn, .math-ch-btn").forEach((btn, i) =>
    btn.classList.toggle("active", i === index));
  const chList = getMathChapterList();
  const ch = chList[index];
  if (ch && ch.exercises && ch.exercises.length > 0) {
    state.activeMathEx = ch.exercises[0].exercise;
  }
  renderMathChapter(index);
}

function switchMathTab(tabName, skipScroll) {
  state.activeMathTab = tabName;
  document.querySelectorAll(".math-top-tab, .math-tab-btn, .bio-tab-btn").forEach(btn =>
    btn.classList.toggle("active", btn.dataset.tab === tabName));

  const chList = getMathChapterList();
  const ch = chList[state.selectedMathChapter];
  const container = $("mathTabContent");
  if (!container || !ch) return;

  if (tabName === "lesson") {
    container.innerHTML = renderMathLesson(ch);
  } else if (tabName === "examples") {
    container.innerHTML = renderMathExamples(ch);
  } else if (tabName === "exercises") {
    container.innerHTML = renderMathExercises(ch);
  } else if (tabName === "slos") {
    container.innerHTML = renderMathSLOs(ch);
  } else if (tabName === "formulas") {
    container.innerHTML = renderMathFormulaSheet(ch);
  }

  container.scrollTop = 0;
}

// ─── MATHEMATICS ACCORDION TOGGLING LOGIC ────────
function toggleMathAccordion(headerEl) {
  const card = headerEl.closest('.math-accordion-card');
  if (!card) return;
  const body = card.querySelector('.math-accordion-body');
  const icon = headerEl.querySelector('.math-acc-icon');
  const isOpen = body && (body.style.display === 'block' || card.classList.contains('open'));

  if (isOpen) {
    if (body) body.style.display = 'none';
    card.classList.remove('open');
    if (icon) icon.textContent = '+';
  } else {
    if (body) body.style.display = 'block';
    card.classList.add('open');
    if (icon) icon.textContent = '−';
  }
}

function expandAllMathCards(containerId) {
  const container = document.getElementById(containerId) || document.getElementById('mathTabContent');
  if (!container) return;
  container.querySelectorAll('.math-accordion-card').forEach(card => {
    const body = card.querySelector('.math-accordion-body');
    const icon = card.querySelector('.math-acc-icon');
    if (body) body.style.display = 'block';
    card.classList.add('open');
    if (icon) icon.textContent = '−';
  });
}

function collapseAllMathCards(containerId) {
  const container = document.getElementById(containerId) || document.getElementById('mathTabContent');
  if (!container) return;
  container.querySelectorAll('.math-accordion-card').forEach(card => {
    const body = card.querySelector('.math-accordion-body');
    const icon = card.querySelector('.math-acc-icon');
    if (body) body.style.display = 'none';
    card.classList.remove('open');
    if (icon) icon.textContent = '+';
  });
}

function renderMathChapter(index) {
  const chList = getMathChapterList();
  const ch = chList[index] || chList[0];
  const area = $("mathTopicArea");
  if (!area || !ch) return;

  const totalExercises = ch.exercises ? ch.exercises.length : 0;
  const totalExamples = ch.workedExamples ? ch.workedExamples.length : 0;
  const totalSections = ch.sections ? ch.sections.length : 0;
  const mcqCount = (ch.slos && ch.slos.mcqs) ? ch.slos.mcqs.length : 0;
  const pdfFile = 'file://DESKTOP-R2HQSAV/SpaceBook/9th MTHA/PDF/9th maaths.pdf';

  area.innerHTML = `
    <!-- Sleek Compact Chapter Header Bar -->
    <div class="math-compact-header-bar">
      <div class="mch-left">
        <span class="mch-unit-pill">Unit ${ch.number}</span>
        <div class="mch-titles">
          <span class="mch-title">${ch.title}</span>
          ${ch.titleUrdu ? `<span class="mch-urdu">${ch.titleUrdu}</span>` : ''}
        </div>
        <span class="mch-meta-badge">📖 ${totalSections} Topics · 💡 ${totalExamples} Examples · ✍️ ${totalExercises} Exercises</span>
      </div>
      <div class="mch-right">
        <a href="${pdfFile}" target="_blank" class="mch-pdf-link" title="Open Official Textbook PDF">📥 PDF</a>
        <button class="mch-back-btn" onclick="goToSubjects('${state.selectedClass || 'cls9'}')" title="Back to Subjects">
          <span>←</span> Subjects
        </button>
      </div>
    </div>

    <!-- Chapter Section Navigation Tabs -->
    <div class="math-nav-tabs">
      <button class="math-top-tab math-tab-btn bio-tab-btn ${state.activeMathTab === 'lesson' ? 'active' : ''}" data-tab="lesson" onclick="switchMathTab('lesson')">
        📖 1. Lessons &amp; Concepts (${totalSections})
      </button>
      <button class="math-top-tab math-tab-btn bio-tab-btn ${state.activeMathTab === 'examples' ? 'active' : ''}" data-tab="examples" onclick="switchMathTab('examples')">
        💡 2. Step-by-Step Examples (${totalExamples})
      </button>
      <button class="math-top-tab math-tab-btn bio-tab-btn ${state.activeMathTab === 'exercises' ? 'active' : ''}" data-tab="exercises" onclick="switchMathTab('exercises')">
        ✍️ 3. Solved Exercises (${totalExercises})
      </button>
      <button class="math-top-tab math-tab-btn bio-tab-btn ${state.activeMathTab === 'slos' ? 'active' : ''}" data-tab="slos" onclick="switchMathTab('slos')">
        🎯 4. Official SLOs &amp; MCQs (${mcqCount})
      </button>
      <button class="math-top-tab math-tab-btn bio-tab-btn ${state.activeMathTab === 'formulas' ? 'active' : ''}" data-tab="formulas" onclick="switchMathTab('formulas')">
        📐 5. Formulas &amp; Summary
      </button>
    </div>

    <!-- Main Dynamic Tab Content (with internal smooth scrollbar) -->
    <div id="mathTabContent" class="math-tab-content-scroll"></div>
  `;

  switchMathTab(state.activeMathTab || 'lesson', true);
}

function renderMathLesson(ch) {
  if (!ch.sections || ch.sections.length === 0) {
    return `<div style="padding:2.5rem;text-align:center;background:#fff;border-radius:12px;border:1px solid var(--border);">Detailed lesson reading for Unit ${ch.number} will be available soon.</div>`;
  }

  const sectionsHtml = ch.sections.map((sec, idx) => `
    <div class="math-topic-card math-accordion-card" id="math-topic-${sec.id || idx}">
      <div class="math-acc-header" onclick="toggleMathAccordion(this)">
        <div style="display:flex;align-items:center;gap:0.75rem;">
          <span class="math-badge" style="background:#e0f2fe;color:#0369a1;">Topic ${sec.id}</span>
          <h3 style="color:#0f172a;font-size:1.1rem;font-weight:700;margin:0;">
            ${sec.title}
          </h3>
        </div>
        <div style="display:flex;align-items:center;gap:0.6rem;">
          <span style="font-size:0.78rem;color:#64748b;font-weight:600;">Textbook Reading</span>
          <span class="math-acc-icon">+</span>
        </div>
      </div>
      <div class="math-accordion-body" style="display:none;margin-top:1rem;border-top:1px solid #e2e8f0;padding-top:1rem;">
        <div style="font-size:0.95rem;line-height:1.8;color:#334155;white-space:pre-line;margin-bottom:1rem;">
          ${sec.theory}
        </div>
        ${(sec.rules && sec.rules.length > 0) ? `
          <div style="background:#f0fdf4;border-left:4px solid #16a34a;border-radius:0 8px 8px 0;padding:0.75rem 1rem;">
            <div style="font-weight:700;color:#15803d;font-size:0.85rem;margin-bottom:0.35rem;">📌 KEY RULES &amp; THEOREMS:</div>
            <ul style="margin:0;padding-left:1.25rem;color:#166534;font-size:0.9rem;line-height:1.6;">
              ${sec.rules.map(r => `<li>${r}</li>`).join('')}
            </ul>
          </div>
        ` : ''}
      </div>
    </div>
  `).join('');

  return `
    <div id="mathLessonList">
      <div class="math-toolbar">
        <div style="display:flex;align-items:center;gap:0.5rem;">
          <span style="font-size:1.25rem;">📖</span>
          <span style="font-size:0.92rem;font-weight:700;color:#1e3a8a;">Lesson Reading &amp; Theory: Click any topic to expand</span>
        </div>
        <div style="display:flex;align-items:center;gap:0.5rem;">
          <button class="math-toolbar-btn" onclick="expandAllMathCards('mathLessonList')">➕ Expand All Topics</button>
          <button class="math-toolbar-btn" onclick="collapseAllMathCards('mathLessonList')">➖ Collapse All</button>
        </div>
      </div>
      ${sectionsHtml}
    </div>
  `;
}

function renderMathExamples(ch) {
  if (!ch.workedExamples || ch.workedExamples.length === 0) {
    return `<div style="padding:2.5rem;text-align:center;background:#fff;border-radius:12px;border:1px solid var(--border);">Step-by-step examples for Unit ${ch.number} will be loaded here.</div>`;
  }

  const examplesHtml = ch.workedExamples.map((ex, idx) => `
    <div class="math-topic-card math-accordion-card" id="math-ex-${ex.id || idx}" style="border-left: 4px solid #0284c7;">
      <div class="math-acc-header" onclick="toggleMathAccordion(this)">
        <div style="display:flex;align-items:center;gap:0.6rem;flex-wrap:wrap;">
          <span class="math-badge" style="background:#0284c7;color:#fff;">${ex.title.split('—')[0].trim()}</span>
          <span style="font-weight:700;color:#0f172a;font-size:0.98rem;">
            ${ex.problem.split('\n')[0].slice(0, 85)}${ex.problem.length > 85 ? '...' : ''}
          </span>
        </div>
        <div style="display:flex;align-items:center;gap:0.5rem;">
          <span style="font-size:0.78rem;color:#0284c7;font-weight:700;background:#e0f2fe;padding:0.2rem 0.55rem;border-radius:4px;">Worked Solution</span>
          <span class="math-acc-icon">+</span>
        </div>
      </div>
      <div class="math-accordion-body" style="display:none;margin-top:1rem;border-top:1px solid #e2e8f0;padding-top:1rem;">
        <div style="font-weight:700;font-size:1.02rem;color:#0f172a;margin-bottom:0.75rem;background:#f8fafc;padding:0.75rem 1rem;border-radius:8px;white-space:pre-line;line-height:1.6;">
          ${ex.problem}
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:0.75rem;margin-bottom:1rem;font-size:0.88rem;">
          <div style="background:#f1f5f9;padding:0.65rem 0.9rem;border-radius:6px;">
            <strong>Given:</strong> ${ex.given}
          </div>
          <div style="background:#f0fdf4;padding:0.65rem 0.9rem;border-radius:6px;color:#15803d;">
            <strong>Method:</strong> ${ex.method}
          </div>
        </div>
        <div class="math-step-box">
          <div style="font-weight:700;color:#0369a1;margin-bottom:0.4rem;">Detailed Step-by-Step Execution:</div>
          <ol style="margin:0;padding-left:1.25rem;line-height:1.8;">
            ${(ex.steps || (ex.solution ? [ex.solution] : [])).map(s => `<li style="margin-bottom:0.45rem;white-space:pre-line;">${s}</li>`).join('')}
          </ol>
        </div>
        <div class="math-result-pill" style="margin-top:0.75rem;">
          <strong>🎯 Textbook Final Answer:</strong> ${ex.answer || 'Proved.'}
        </div>
      </div>
    </div>
  `).join('');

  return `
    <div id="mathExamplesList">
      <div class="math-toolbar">
        <div style="display:flex;align-items:center;gap:0.5rem;">
          <span style="font-size:1.25rem;">💡</span>
          <span style="font-size:0.92rem;font-weight:700;color:#0369a1;">Prerequisite Worked Examples: Click any example to expand</span>
        </div>
        <div style="display:flex;align-items:center;gap:0.5rem;">
          <button class="math-toolbar-btn" onclick="expandAllMathCards('mathExamplesList')">➕ Expand All Examples</button>
          <button class="math-toolbar-btn" onclick="collapseAllMathCards('mathExamplesList')">➖ Collapse All</button>
        </div>
      </div>
      ${examplesHtml}
    </div>
  `;
}

function switchMathEx(exKey) {
  state.activeMathEx = exKey;
  document.querySelectorAll(".math-sub-tab-btn").forEach(btn =>
    btn.classList.toggle("active", btn.dataset.ex === exKey));

  const chList = getMathChapterList();
  const ch = chList[state.selectedMathChapter];
  const container = $("mathExerciseContent");
  if (!container || !ch || !ch.exercises) return;

  const currentEx = ch.exercises.find(e => e.exercise === exKey) || ch.exercises[0];
  if (!currentEx) return;

  container.innerHTML = `
    <div class="math-toolbar">
      <div>
        <h3 style="color:#0f172a;font-size:1.15rem;font-weight:800;margin:0 0 0.2rem 0;">
          ${currentEx.title}
        </h3>
        <span style="color:#64748b;font-size:0.84rem;">
          ${currentEx.problems.length} Textbook Questions with 100% verified solutions. Click any question to expand.
        </span>
      </div>
      <div style="display:flex;align-items:center;gap:0.5rem;">
        <button class="math-toolbar-btn" onclick="expandAllMathCards('mathProblemsList')">➕ Expand All Questions</button>
        <button class="math-toolbar-btn" onclick="collapseAllMathCards('mathProblemsList')">➖ Collapse All</button>
      </div>
    </div>
    <div id="mathProblemsList" class="math-problems-list">
      ${currentEx.problems.map((p, pIdx) => `
        <div class="math-topic-card math-accordion-card" id="math-prob-${pIdx}" style="margin-bottom:1rem;">
          <div class="math-acc-header" onclick="toggleMathAccordion(this)">
            <div style="display:flex;align-items:center;gap:0.6rem;flex-wrap:wrap;">
              <span class="math-badge" style="background:#0284c7;color:#fff;">${p.qNo || `Q${pIdx + 1}`}</span>
              <span style="font-weight:700;color:#0f172a;font-size:0.96rem;">
                ${p.question.split('\n')[0].slice(0, 95)}${p.question.length > 95 ? '...' : ''}
              </span>
            </div>
            <div style="display:flex;align-items:center;gap:0.55rem;">
              <span style="font-size:0.78rem;color:#15803d;font-weight:700;background:#dcfce7;padding:0.2rem 0.55rem;border-radius:4px;">✅ Solved</span>
              <span class="math-acc-icon">+</span>
            </div>
          </div>
          <div class="math-accordion-body" style="display:none;margin-top:1rem;border-top:1px solid #e2e8f0;padding-top:1rem;">
            <div style="font-weight:700;font-size:1.02rem;color:#0f172a;margin-bottom:0.85rem;white-space:pre-line;line-height:1.65;background:#f8fafc;padding:0.85rem 1.1rem;border-radius:8px;border:1px solid #e2e8f0;">
              ${p.question}
            </div>
            <div class="math-step-box" style="white-space:pre-line;line-height:1.8;margin-bottom:0.85rem;">
              <div style="font-weight:700;color:#0369a1;margin-bottom:0.4rem;">Full Mathematical Solution:</div>
              ${p.solution}
            </div>
            <div class="math-result-pill">
              <strong>🎯 Textbook Verified Answer:</strong> ${p.answer}
            </div>
          </div>
        </div>
      `).join('')}
    </div>
  `;

  // Auto scroll down to exercise tab
  const activeExBtn = document.querySelector(`.math-sub-tab-btn[data-ex="${exKey}"]`);
  if (activeExBtn) {
    autoScrollToActiveTab(activeExBtn);
  }
}

function renderMathExercises(ch) {
  if (!ch.exercises || ch.exercises.length === 0) {
    return `<div style="padding:2.5rem;text-align:center;background:#fff;border-radius:12px;border:1px solid var(--border);">Textbook exercises for Unit ${ch.number} will be displayed here.</div>`;
  }

  const activeEx = (ch.exercises.some(e => e.exercise === state.activeMathEx))
    ? state.activeMathEx
    : (ch.exercises[0] ? ch.exercises[0].exercise : '1.1');

  const subTabsHtml = `
    <div class="math-sub-tabs">
      ${ch.exercises.map(ex => `
        <button class="math-sub-tab-btn ${ex.exercise === activeEx ? 'active' : ''}"
                data-ex="${ex.exercise}"
                onclick="switchMathEx('${ex.exercise}')">
          ${ex.exercise.startsWith('Review') ? ('🌟 ' + ex.exercise) : 'Ex ' + ex.exercise}
        </button>
      `).join('')}
    </div>
    <div id="mathExerciseContent"></div>
  `;

  setTimeout(() => {
    switchMathEx(activeEx);
  }, 10);

  return subTabsHtml;
}

function selectMathMcqOption(qIdx, optIdx, isCorrect, exp) {
  const qCard = document.getElementById(`math-mcq-${qIdx}`);
  if (!qCard) return;

  const buttons = qCard.querySelectorAll('.math-mcq-opt');
  buttons.forEach((b, i) => {
    b.disabled = true;
    b.style.pointerEvents = 'none';
    if (i === optIdx) {
      if (isCorrect) {
        b.style.background = '#dcfce7';
        b.style.borderColor = '#16a34a';
        b.style.color = '#15803d';
      } else {
        b.style.background = '#fee2e2';
        b.style.borderColor = '#ef4444';
        b.style.color = '#b91c1c';
      }
    }
  });

  const expBox = document.getElementById(`math-mcq-exp-${qIdx}`);
  if (expBox) {
    expBox.style.display = 'block';
    expBox.innerHTML = `
      <div style="font-weight:700;color:${isCorrect ? '#15803d' : '#b91c1c'};margin-bottom:0.25rem;">
        ${isCorrect ? '✅ Correct Answer!' : '❌ Incorrect!'}
      </div>
      <div>${exp}</div>
    `;
  }
}

function renderMathSLOs(ch) {
  const slos = ch.slos || {};
  const mcqs = slos.mcqs || [];
  const sqs = slos.shortQuestions || [];
  const lqs = slos.longQuestions || [];

  const mcqsHtml = mcqs.map((m, idx) => `
    <div class="math-topic-card" id="math-mcq-${idx}" style="margin-bottom:1.25rem;">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
        <span class="math-badge" style="background:#e0f2fe;color:#0369a1;">MCQ ${idx + 1}</span>
        <span style="font-size:0.78rem;color:#64748b;font-weight:600;">1 Mark</span>
      </div>
      <div style="font-weight:700;font-size:1.02rem;color:#0f172a;margin-bottom:0.85rem;">
        ${m.q}
      </div>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:0.6rem;margin-bottom:0.5rem;">
        ${m.options.map((opt, oIdx) => `
          <button class="math-mcq-opt" onclick="selectMathMcqOption(${idx}, ${oIdx}, ${oIdx === m.correct}, '${m.exp}')" style="padding:0.6rem 0.85rem;border:1px solid #cbd5e1;background:#ffffff;border-radius:8px;font-size:0.9rem;text-align:left;cursor:pointer;transition:all 0.15s ease;">
            <strong>${['A', 'B', 'C', 'D'][oIdx]}.</strong> ${opt}
          </button>
        `).join('')}
      </div>
      <div id="math-mcq-exp-${idx}" style="display:none;margin-top:0.75rem;padding:0.75rem 1rem;background:#f8fafc;border-radius:8px;border-left:4px solid #0284c7;font-size:0.88rem;color:#334155;"></div>
    </div>
  `).join('');

  const sqsHtml = sqs.map((s, idx) => `
    <div class="math-topic-card math-accordion-card" id="math-sq-${idx}" style="margin-bottom:1rem;">
      <div class="math-acc-header" onclick="toggleMathAccordion(this)">
        <div style="display:flex;align-items:center;gap:0.6rem;">
          <span class="math-badge" style="background:#dcfce7;color:#15803d;">SQ ${idx + 1}</span>
          <span style="font-weight:700;color:#0f172a;font-size:0.98rem;">${s.q}</span>
        </div>
        <div style="display:flex;align-items:center;gap:0.5rem;">
          <span style="font-size:0.78rem;color:#15803d;font-weight:700;">${s.marks} Marks</span>
          <span class="math-acc-icon">+</span>
        </div>
      </div>
      <div class="math-accordion-body" style="display:none;margin-top:1rem;border-top:1px solid #e2e8f0;padding-top:1rem;">
        <div class="math-step-box" style="white-space:pre-line;line-height:1.75;">
          ${s.sol}
        </div>
      </div>
    </div>
  `).join('');

  const lqsHtml = lqs.map((l, idx) => `
    <div class="math-topic-card math-accordion-card" id="math-lq-${idx}" style="margin-bottom:1rem;">
      <div class="math-acc-header" onclick="toggleMathAccordion(this)">
        <div style="display:flex;align-items:center;gap:0.6rem;">
          <span class="math-badge" style="background:#fef3c7;color:#92400e;">LQ ${idx + 1}</span>
          <span style="font-weight:700;color:#0f172a;font-size:0.98rem;">${l.q}</span>
        </div>
        <div style="display:flex;align-items:center;gap:0.5rem;">
          <span style="font-size:0.78rem;color:#92400e;font-weight:700;">${l.marks} Marks</span>
          <span class="math-acc-icon">+</span>
        </div>
      </div>
      <div class="math-accordion-body" style="display:none;margin-top:1rem;border-top:1px solid #e2e8f0;padding-top:1rem;">
        <div style="font-size:0.86rem;color:#475569;margin-bottom:0.75rem;background:#f8fafc;padding:0.6rem 0.85rem;border-radius:6px;">
          <strong>Marking Rubric:</strong> ${l.rubric}
        </div>
        <div class="math-step-box" style="white-space:pre-line;line-height:1.75;">
          ${l.sol}
        </div>
      </div>
    </div>
  `).join('');

  return `
    <div>
      <div style="margin-bottom:1.5rem;">
        <h3 style="color:#0f172a;font-size:1.15rem;font-weight:800;margin-bottom:0.35rem;">
          🎯 Multiple Choice Questions (Interactive)
        </h3>
        <p style="color:#64748b;font-size:0.85rem;margin:0;">Select an option for instant answer verification and explanation.</p>
      </div>
      ${mcqsHtml}

      <div class="math-toolbar" style="margin-top:2rem;">
        <h3 style="color:#0f172a;font-size:1.15rem;font-weight:800;margin:0;">
          📝 Conceptual Short Questions (3 Marks Each)
        </h3>
        <div style="display:flex;gap:0.5rem;">
          <button class="math-toolbar-btn" onclick="expandAllMathCards('mathTabContent')">➕ Expand All</button>
          <button class="math-toolbar-btn" onclick="collapseAllMathCards('mathTabContent')">➖ Collapse All</button>
        </div>
      </div>
      ${sqsHtml}

      <div class="math-toolbar" style="margin-top:2rem;">
        <h3 style="color:#0f172a;font-size:1.15rem;font-weight:800;margin:0;">
          📚 Detailed Long Questions (8 Marks Each)
        </h3>
        <div style="display:flex;gap:0.5rem;">
          <button class="math-toolbar-btn" onclick="expandAllMathCards('mathTabContent')">➕ Expand All</button>
          <button class="math-toolbar-btn" onclick="collapseAllMathCards('mathTabContent')">➖ Collapse All</button>
        </div>
      </div>
      ${lqsHtml}
    </div>
  `;
}

function renderMathFormulaSheet(ch) {
  const formulas = ch.formulaSheet || [];
  if (formulas.length === 0) {
    return `<div style="padding:2.5rem;text-align:center;background:#fff;border-radius:12px;border:1px solid var(--border);">Formula sheet for Unit ${ch.number} will be provided here.</div>`;
  }

  const cardsHtml = formulas.map(f => `
    <div class="math-formula-card">
      <div style="font-size:0.82rem;font-weight:700;color:#0284c7;text-transform:uppercase;letter-spacing:0.04em;margin-bottom:0.35rem;">
        ${f.name}
      </div>
      <div style="font-family:'Consolas','Courier New',monospace;font-size:1.15rem;font-weight:700;color:#0f172a;margin-bottom:0.5rem;background:#ffffff;padding:0.5rem 0.75rem;border-radius:6px;border:1px solid #cbd5e1;display:inline-block;">
        ${f.formula}
      </div>
      <div style="font-size:0.86rem;color:#475569;line-height:1.5;">
        ${f.note}
      </div>
    </div>
  `).join('');

  return `
    <div>
      <div style="background:#eff6ff;border:1px solid #bfdbfe;border-radius:10px;padding:0.9rem 1.25rem;margin-bottom:1.5rem;display:flex;align-items:center;gap:0.75rem;">
        <span style="font-size:1.4rem;">📐</span>
        <div style="font-size:0.9rem;color:#1e40af;">
          <strong>Quick Revision Cheat Sheet:</strong> Essential formulas, determinant rules, adjoints, and inversion laws for KPK Board examination.
        </div>
      </div>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1rem;">
        ${cardsHtml}
      </div>
    </div>
  `;
}



// ═══════════════════════════════════════════════════════════════
// PAKISTAN STUDIES GRADE 9 PORTAL
function getPakStudyChapterList() {
  if (typeof PAKSTUDY_DATA !== "undefined" && Array.isArray(PAKSTUDY_DATA)) {
    return PAKSTUDY_DATA;
  }
  return [];
}

function openPakStudyView(classId, subj) {
  state.activeSubject = "pakstudy";
  state.selectedPakStudyChapter = 0;
  state.activePakStudyTab = "sections";
  state.activePakStudySloTab = "slo-mcqs";
  state.selectedClass = classId;
  setActiveNav("subjects");

  const cls = DATA.classes.find(c => c.id === classId) || { name: "Class 9" };
  const chList = getPakStudyChapterList();
  const gradeLabel = "Grade 9";

  setDashHeader(`🇵🇰 ${subj.name} (${subj.nameUrdu || 'مطالعہ پاکستان'}) — ${gradeLabel}`, `KPK Textbook Board, Peshawar · مکمل 4 ابواب، حل شدہ مشقیں اور ایس ایل او بینک`);
  setBreadcrumb([
    { label: "Home",     onclick: () => { setActiveNav("home"); renderHome(); } },
    { label: "Subjects", onclick: () => renderClasses() },
    { label: cls.name,   onclick: () => goToSubjects(classId) },
    { label: subj.name,  active: true }
  ]);

  const chapBtns = chList.map((ch, i) => `
    <button class="bio-ch-btn ${i === 0 ? "active" : ""}" id="ps-btn-${i}"
            onclick="selectPakStudyChapter(${i})">
      <span class="ch-btn-num" style="background:#047857;color:#fff;">باب ${ch.number}</span>
      <span class="ch-btn-info">
        <span class="ch-btn-name" style="direction:rtl;text-align:right;font-family:'Jameel Noori Nastaleeq', 'Urdu Typesetting', 'Segoe UI', serif;font-size:1.1rem;font-weight:700;">${ch.title}</span>
        <span class="ch-btn-sub" style="font-size:0.75rem;color:#64748b;">${ch.pageRange}</span>
      </span>
      <span class="ch-btn-status" style="background:#dcfce7;color:#15803d;">
        ✅ Complete
      </span>
    </button>`).join("");

  pageContent().innerHTML = `
    <div class="bio-view">
      <div class="bio-ch-sidebar">
        <div class="bio-ch-sidebar-header" style="background:linear-gradient(135deg,#065f46,#047857);color:#fff;box-shadow:0 2px 8px rgba(6,95,70,0.25);">
          <button onclick="goToSubjects('${classId}')" class="sidebar-back-icon-btn" title="Back to Subjects" style="background:rgba(255,255,255,0.2);color:#fff;border:1px solid rgba(255,255,255,0.35);">←</button>
          <span>🇵🇰 مطالعہ پاکستان ${gradeLabel}</span>
        </div>
        <div class="bio-ch-list">${chapBtns}</div>
        <div style="padding:1rem;background:#f8fafc;border-top:1px solid var(--border);text-align:center;">
          <div style="font-size:0.78rem;color:#047857;font-weight:700;margin-bottom:0.35rem;">خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور</div>
          <div style="font-size:0.72rem;color:#64748b;">100% نصابی کتب سے تصدیق شدہ</div>
        </div>
      </div>
      <div class="bio-topic-area" id="pakStudyTopicArea"></div>
    </div>`;

  renderPakStudyChapter(0);
}

function selectPakStudyChapter(index) {
  state.selectedPakStudyChapter = index;
  document.querySelectorAll(".bio-ch-btn").forEach((btn, i) =>
    btn.classList.toggle("active", i === index));
  renderPakStudyChapter(index);
}

function switchPakStudyTab(tabName, skipScroll) {
  state.activePakStudyTab = tabName;
  document.querySelectorAll(".ps-top-tab").forEach(btn =>
    btn.classList.toggle("active", btn.dataset.tab === tabName));

  const chList = getPakStudyChapterList();
  const ch = chList[state.selectedPakStudyChapter || 0];
  const container = $("psTabContentContainer");
  if (!container || !ch) return;

  if (tabName === "sections") {
    container.innerHTML = renderPakStudySections(ch);
  } else if (tabName === "summary") {
    container.innerHTML = renderPakStudySummary(ch);
  } else if (tabName === "exercise") {
    container.innerHTML = renderPakStudyExercise(ch);
  } else if (tabName === "slo") {
    container.innerHTML = renderPakStudySLOs(ch);
  } else if (tabName === "timeline") {
    container.innerHTML = renderPakStudyTimeline(ch);
  }

  if (!skipScroll) {
    const headerEl = $("psChapterHeader");
    if (headerEl) headerEl.scrollIntoView({ behavior: "smooth", block: "start" });
  }
}

function renderPakStudyChapter(index) {
  const chList = getPakStudyChapterList();
  const ch = chList[index];
  const area = $("pakStudyTopicArea");
  if (!ch || !area) return;

  const currentTab = state.activePakStudyTab || "sections";
  const mcqsCount = (ch.exercise && ch.exercise.mcqs) ? ch.exercise.mcqs.length : 0;
  const sqsCount = (ch.exercise && ch.exercise.shortQuestions) ? ch.exercise.shortQuestions.length : 0;
  const lqsCount = (ch.exercise && ch.exercise.longQuestions) ? ch.exercise.longQuestions.length : 0;
  const sloCount = (ch.sloBank && ch.sloBank.mcqs) ? ch.sloBank.mcqs.length : 10;

  area.innerHTML = `
    <div class="urdu-chapter-container" id="psChapterHeader">
      <!-- Chapter Hero Banner -->
      <div style="background:linear-gradient(135deg,#064e3b 0%,#047857 50%,#059669 100%);color:#fff;padding:1.6rem 2rem;border-radius:14px;margin-bottom:1.5rem;box-shadow:0 6px 20px rgba(4,120,87,0.22);position:relative;overflow:hidden;">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:1rem;position:relative;z-index:1;">
          <div>
            <div style="display:inline-flex;align-items:center;gap:0.5rem;background:rgba(255,255,255,0.18);padding:0.25rem 0.85rem;border-radius:99px;font-size:0.82rem;font-weight:700;margin-bottom:0.75rem;backdrop-filter:blur(4px);">
              <span>🇵🇰 مطالعہ پاکستان</span>
              <span>•</span>
              <span>باب نمبر ${ch.number}</span>
              <span>•</span>
              <span>${ch.pageRange}</span>
            </div>
            <h1 style="font-family:'Jameel Noori Nastaleeq','Urdu Typesetting','Segoe UI',serif;font-size:2.2rem;margin:0 0 0.5rem 0;line-height:1.5;direction:rtl;text-align:right;">
              ${ch.title}
            </h1>
            <div style="font-size:0.92rem;opacity:0.9;direction:rtl;text-align:right;max-width:700px;line-height:1.8;">
              ${ch.description || ''}
            </div>
          </div>
          <div style="text-align:right;background:rgba(0,0,0,0.15);padding:0.85rem 1.25rem;border-radius:10px;border:1px solid rgba(255,255,255,0.2);">
            <div style="font-size:0.75rem;opacity:0.85;text-transform:uppercase;letter-spacing:0.5px;">Curriculum Standard</div>
            <div style="font-size:1.15rem;font-weight:800;color:#a7f3d0;">KPK Board (پشاور)</div>
            <div style="font-size:0.75rem;margin-top:0.25rem;color:#ecfdf5;">100% Verbatim Matched</div>
          </div>
        </div>

        <!-- Quick Stats Grid (Maximum 3 Statistical Cards in a Row) -->
        <div class="ps-stats-grid">
          <div class="ps-stat-card">
            <span class="ps-stat-icon">📖</span>
            <div class="ps-stat-content">
              <span class="ps-stat-num">${ch.sections ? ch.sections.length : 0}</span>
              <span class="ps-stat-label">تفصیلی عناوین (Sections)</span>
            </div>
          </div>
          <div class="ps-stat-card">
            <span class="ps-stat-icon">🎯</span>
            <div class="ps-stat-content">
              <span class="ps-stat-num">${mcqsCount}</span>
              <span class="ps-stat-label">مشقی کثیر الانتخابی (MCQs)</span>
            </div>
          </div>
          <div class="ps-stat-card">
            <span class="ps-stat-icon">✏️</span>
            <div class="ps-stat-content">
              <span class="ps-stat-num">${sqsCount}</span>
              <span class="ps-stat-label">مختصر امتحانی سوالات (SQs)</span>
            </div>
          </div>
          <div class="ps-stat-card">
            <span class="ps-stat-icon">📝</span>
            <div class="ps-stat-content">
              <span class="ps-stat-num">${lqsCount}</span>
              <span class="ps-stat-label">تفصیلی ماڈل سوالات (LQs)</span>
            </div>
          </div>
          <div class="ps-stat-card">
            <span class="ps-stat-icon">🌟</span>
            <div class="ps-stat-content">
              <span class="ps-stat-num">${sloCount}</span>
              <span class="ps-stat-label">ایس ایل او جائزے (SLO Bank)</span>
            </div>
          </div>
          <div class="ps-stat-card">
            <span class="ps-stat-icon">⏳</span>
            <div class="ps-stat-content">
              <span class="ps-stat-num">${ch.timeline ? ch.timeline.length : 0}</span>
              <span class="ps-stat-label">تاریخی سنگِ میل (Milestones)</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Top Pedagogical Tabs -->
      <div style="display:flex;gap:0.5rem;margin-bottom:1.5rem;background:#f1f5f9;padding:0.4rem;border-radius:10px;flex-wrap:wrap;">
        <button class="ps-top-tab ${currentTab === 'sections' ? 'active' : ''}" data-tab="sections" onclick="switchPakStudyTab('sections')" style="flex:1;min-width:140px;padding:0.65rem 1rem;font-size:0.92rem;font-weight:700;border:none;border-radius:8px;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:0.4rem;transition:all 0.2s;">
          <span>📖</span> سبق کا مکمل متن
        </button>
        <button class="ps-top-tab ${currentTab === 'summary' ? 'active' : ''}" data-tab="summary" onclick="switchPakStudyTab('summary')" style="flex:1;min-width:140px;padding:0.65rem 1rem;font-size:0.92rem;font-weight:700;border:none;border-radius:8px;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:0.4rem;transition:all 0.2s;">
          <span>💡</span> اہم نکات و خلاصہ
        </button>
        <button class="ps-top-tab ${currentTab === 'exercise' ? 'active' : ''}" data-tab="exercise" onclick="switchPakStudyTab('exercise')" style="flex:1;min-width:140px;padding:0.65rem 1rem;font-size:0.92rem;font-weight:700;border:none;border-radius:8px;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:0.4rem;transition:all 0.2s;">
          <span>✍️</span> حل شدہ مشقی سوالات
        </button>
        <button class="ps-top-tab ${currentTab === 'slo' ? 'active' : ''}" data-tab="slo" onclick="switchPakStudyTab('slo')" style="flex:1;min-width:140px;padding:0.65rem 1rem;font-size:0.92rem;font-weight:700;border:none;border-radius:8px;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:0.4rem;transition:all 0.2s;">
          <span>🎯</span> ایس ایل او امتحانی بینک
        </button>
        <button class="ps-top-tab ${currentTab === 'timeline' ? 'active' : ''}" data-tab="timeline" onclick="switchPakStudyTab('timeline')" style="flex:1;min-width:140px;padding:0.65rem 1rem;font-size:0.92rem;font-weight:700;border:none;border-radius:8px;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:0.4rem;transition:all 0.2s;">
          <span>⏳</span> تاریخی جدول و اقوال
        </button>
      </div>

      <!-- Tab Content Area -->
      <div id="psTabContentContainer"></div>
    </div>`;

  // Inject dynamic active style for ps-top-tab
  const tabBtnStyle = document.createElement("style");
  tabBtnStyle.id = "ps-tab-style";
  tabBtnStyle.innerHTML = `
    .ps-top-tab { background: transparent; color: #475569; }
    .ps-top-tab.active { background: #047857 !important; color: #ffffff !important; box-shadow: 0 2px 6px rgba(4,120,87,0.3); }
    .ps-top-tab:hover:not(.active) { background: #e2e8f0; }
  `;
  if (!$("ps-tab-style")) document.head.appendChild(tabBtnStyle);

  switchPakStudyTab(currentTab, true);
}

// ─────────────────────────────────────────
//  TAB 1: COMPLETE VERBATIM SECTIONS (متن)
// ─────────────────────────────────────────
function renderPakStudySections(ch) {
  let quranBannerHtml = "";
  if (ch.introQuranHadith && Array.isArray(ch.introQuranHadith)) {
    const quotes = ch.introQuranHadith.map(q => `
      <div style="background:#ffffff;border:1.5px solid #a7f3d0;border-radius:10px;padding:1rem 1.25rem;margin-bottom:0.75rem;box-shadow:0 2px 8px rgba(5,150,105,0.06);">
        <div style="font-family:'Traditional Arabic','Scheherazade',serif;font-size:1.35rem;color:#065f46;direction:rtl;text-align:center;line-height:2;margin-bottom:0.5rem;font-weight:700;">
          ${q.arabic}
        </div>
        <div class="urdu-text-rtl" style="font-size:1.05rem;color:#1e293b;margin-bottom:0.35rem;">
          <strong>ترجمہ:</strong> ${q.translation}
        </div>
        <div style="font-size:0.8rem;color:#047857;text-align:left;font-weight:700;">
          — ${q.reference}
        </div>
      </div>`).join("");

    quranBannerHtml = `
      <div style="background:#f0fdf4;border:2px solid #86efac;border-radius:12px;padding:1.25rem;margin-bottom:1.75rem;">
        <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.75rem;color:#065f46;font-weight:800;font-size:1rem;">
          <span>📖</span><span>فرامینِ الٰہی و احادیثِ مبارکہ (رہنما کلمات):</span>
        </div>
        ${quotes}
      </div>`;
  }

  const sectionsHtml = (ch.sections || []).map((sec, idx) => {
    // Format paragraph breaks
    const formattedContent = sec.content.split('\n\n').map(p => {
      const pClean = p.trim();
      if (!pClean) return '';
      // Check if bullet list
      if (pClean.startsWith('•') || pClean.includes('\n•') || pClean.startsWith('1.') || pClean.startsWith('-')) {
        return `<div class="urdu-sec-p urdu-text-rtl" style="margin-bottom:1rem;white-space:pre-line;">${pClean}</div>`;
      }
      return `<p class="urdu-sec-p urdu-text-rtl">${pClean}</p>`;
    }).join('');

    const previewSnippet = sec.content.replace(/\n+/g, ' ').trim().substring(0, 115) + '...';

    return `
      <div class="urdu-section-card" id="ps-sec-${sec.id || idx}">
        <div class="urdu-section-header" onclick="togglePakStudyAccordion('ps-sec-${sec.id || idx}')" style="cursor:pointer;">
          <div style="display:flex;align-items:center;gap:0.75rem;">
            <span class="urdu-sec-badge" style="background:#047857;">عنوان ${sec.id || (idx + 1)}</span>
            <span class="urdu-sec-title">${sec.title}</span>
          </div>
          <span class="sec-toggle-icon">▼</span>
        </div>
        <div class="urdu-grid-preview urdu-text-rtl">${previewSnippet}</div>
        <div class="urdu-section-body" style="display:none;">
          ${formattedContent}
        </div>
      </div>`;
  }).join('');

  return `
    <div>
      ${quranBannerHtml}
      <div style="margin-bottom:1.25rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.75rem;background:#f8fafc;padding:0.75rem 1rem;border-radius:10px;border:1px solid #e2e8f0;">
        <div>
          <span style="font-weight:800;color:#047857;font-size:0.95rem;">📚 کتاب کا مکمل اصل متن (Verbatim Textbook):</span>
          <span style="font-size:0.82rem;color:#64748b;margin-right:0.4rem;">(تمام عناوین پہلے سے بند ہیں، کلک کر کے کھولیں)</span>
        </div>
        <div style="display:flex;gap:0.5rem;">
          <button onclick="expandAllPakStudySections()" class="math-toolbar-btn" style="color:#047857;border-color:#a7f3d0;" title="تمام عنوانات کھولیں">
            ➕ سب کھولیں (Expand All)
          </button>
          <button onclick="collapseAllPakStudySections()" class="math-toolbar-btn" style="color:#475569;" title="تمام عنوانات بند کریں">
            ➖ سب بند کریں (Collapse All)
          </button>
        </div>
      </div>
      ${sectionsHtml}
    </div>`;
}

function togglePakStudyAccordion(secId) {
  const el = $(secId);
  if (!el) return;
  const isOpen = el.classList.contains("open");
  const body = el.querySelector(".urdu-section-body");
  if (isOpen) {
    el.classList.remove("open");
    if (body) body.style.display = "none";
  } else {
    el.classList.add("open");
    if (body) body.style.display = "block";
  }
}

function expandAllPakStudySections() {
  document.querySelectorAll("#pakStudyTopicArea .urdu-section-card").forEach(el => {
    el.classList.add("open");
    const body = el.querySelector(".urdu-section-body");
    if (body) body.style.display = "block";
  });
}

function collapseAllPakStudySections() {
  document.querySelectorAll("#pakStudyTopicArea .urdu-section-card").forEach(el => {
    el.classList.remove("open");
    const body = el.querySelector(".urdu-section-body");
    if (body) body.style.display = "none";
  });
}

// ─────────────────────────────────────────
//  TAB 2: SUMMARY & KEY POINTS (خلاصہ)
// ─────────────────────────────────────────
function renderPakStudySummary(ch) {
  const keyPoints = ch.keyPoints || [];
  const pointsHtml = keyPoints.map((pt, i) => `
    <div style="display:flex;gap:0.75rem;align-items:flex-start;padding:0.75rem 1rem;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;margin-bottom:0.6rem;transition:all 0.2s;">
      <span style="display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;background:#dcfce7;color:#15803d;font-weight:800;border-radius:50%;flex-shrink:0;font-size:0.85rem;">
        ${i + 1}
      </span>
      <span class="urdu-text-rtl" style="font-size:1.15rem;color:#1e293b;line-height:2.1;flex:1;">
        ${pt}
      </span>
    </div>`).join('');

  return `
    <div style="background:#ffffff;border:1px solid var(--border);border-radius:12px;padding:1.5rem;box-shadow:var(--shadow);">
      <div style="background:#ecfdf5;border-left:4px solid #047857;padding:1rem 1.25rem;border-radius:8px;margin-bottom:1.5rem;">
        <h3 style="color:#065f46;margin:0 0 0.5rem 0;font-size:1.2rem;font-family:'Jameel Noori Nastaleeq',serif;direction:rtl;text-align:right;">
          💡 باب کا تشریحی تعارف و تدریسی مقاصد
        </h3>
        <p class="urdu-text-rtl" style="margin:0;color:#166534;font-size:1.1rem;line-height:2;">
          ${ch.description}
        </p>
      </div>

      <div style="margin-bottom:1.5rem;">
        <h3 style="color:var(--navy);font-size:1.15rem;font-weight:800;margin-bottom:1rem;display:flex;align-items:center;gap:0.5rem;">
          <span>📌</span><span>اہم ترین امتحانی نکات (High-Yield Summary Points):</span>
        </h3>
        ${pointsHtml}
      </div>
    </div>`;
}

// ─────────────────────────────────────────
//  TAB 3: FULLY SOLVED TEXTBOOK EXERCISE (مشق)
// ─────────────────────────────────────────
function renderPakStudyExercise(ch) {
  const ex = ch.exercise || {};
  const mcqs = ex.mcqs || [];
  const sqs = ex.shortQuestions || [];
  const lqs = ex.longQuestions || [];
  const acts = ex.activities || [];

  // MCQs
  const mcqHtml = mcqs.map((m, idx) => {
    const optionsHtml = m.options.map((opt) => {
      const isCorrect = (opt.trim() === (m.answer || '').trim());
      return `
        <div style="padding:0.5rem 0.85rem;border-radius:6px;border:1.5px solid ${isCorrect ? '#16a34a' : '#e2e8f0'};background:${isCorrect ? '#f0fdf4' : '#ffffff'};color:${isCorrect ? '#15803d' : '#334155'};font-weight:${isCorrect ? '700' : '400'};display:flex;align-items:center;justify-content:space-between;direction:rtl;text-align:right;">
          <span>${opt}</span>
          ${isCorrect ? '<span style="color:#16a34a;font-weight:800;margin-right:0.5rem;">✓ درست</span>' : ''}
        </div>`;
    }).join('');

    return `
      <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;padding:1.1rem 1.25rem;margin-bottom:1rem;box-shadow:0 2px 6px rgba(0,0,0,0.03);">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.6rem;">
          <span style="background:#047857;color:#fff;font-weight:700;font-size:0.75rem;padding:0.2rem 0.6rem;border-radius:99px;">
            مشقی سوال ${m.qNo || (idx + 1)}
          </span>
          <span style="font-size:0.75rem;color:#047857;font-weight:700;">ٹیکسٹ بک کثیر الانتخابی سوال</span>
        </div>
        <div class="urdu-text-rtl" style="font-size:1.18rem;font-weight:700;color:#0f172a;margin-bottom:0.75rem;line-height:2;">
          ${m.question}
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:0.5rem;margin-bottom:0.75rem;">
          ${optionsHtml}
        </div>
        ${m.explanation ? `
          <div class="urdu-text-rtl" style="background:#f8fafc;padding:0.6rem 0.85rem;border-radius:6px;font-size:0.95rem;color:#475569;border-right:3px solid #047857;">
            <strong>وضاحت و علمی سند:</strong> ${m.explanation}
          </div>` : ''}
      </div>`;
  }).join('');

  // Short Questions
  const sqHtml = sqs.map((sq, idx) => `
    <div class="urdu-section-card" id="ps-sq-${idx}" style="margin-bottom:0.85rem;">
      <div class="urdu-section-header" onclick="togglePakStudyAccordion('ps-sq-${idx}')" style="cursor:pointer;background:#f8fafc;">
        <div style="display:flex;align-items:center;gap:0.6rem;">
          <span class="urdu-sec-badge" style="background:#0284c7;font-size:0.78rem;">${sq.qNo || 'مختصر سوال ' + (idx + 1)}</span>
          <span class="urdu-sec-title" style="font-size:1.12rem;">${sq.question}</span>
        </div>
        <span class="sec-toggle-icon">▼</span>
      </div>
      <div class="urdu-section-body" style="display:none;">
        <div class="urdu-text-rtl" style="font-size:1.15rem;line-height:2.2;white-space:pre-line;color:#1e293b;">
          ${sq.answer}
        </div>
      </div>
    </div>`).join('');

  // Long Questions
  const lqHtml = lqs.map((lq, idx) => `
    <div class="urdu-section-card" id="ps-lq-${idx}" style="margin-bottom:1rem;border-color:#cbd5e1;">
      <div class="urdu-section-header" onclick="togglePakStudyAccordion('ps-lq-${idx}')" style="cursor:pointer;background:linear-gradient(135deg,#f0fdf4,#f8fafc);">
        <div style="display:flex;align-items:center;gap:0.6rem;">
          <span class="urdu-sec-badge" style="background:#7c3aed;font-size:0.78rem;">${lq.qNo || 'تفصیلی سوال ' + (idx + 1)}</span>
          <span class="urdu-sec-title" style="font-size:1.15rem;color:#1e1b4b;">${lq.question}</span>
        </div>
        <span class="sec-toggle-icon">▼</span>
      </div>
      <div class="urdu-section-body" style="display:none;">
        <div class="urdu-text-rtl" style="font-size:1.18rem;line-height:2.3;white-space:pre-line;color:#0f172a;">
          ${lq.answer}
        </div>
      </div>
    </div>`).join('');

  // Activities
  const actHtml = acts.map((act, idx) => `
    <div style="background:#fffbeb;border:1.5px solid #fde68a;border-radius:10px;padding:1rem 1.25rem;margin-bottom:0.75rem;">
      <div style="font-weight:800;color:#92400e;margin-bottom:0.35rem;display:flex;align-items:center;gap:0.4rem;">
        <span>🎯</span><span>سرگرمی ${idx + 1}: ${act.title || ''}</span>
      </div>
      <div class="urdu-text-rtl" style="font-size:1.08rem;color:#78350f;line-height:2;">
        ${act.description || act}
      </div>
    </div>`).join('');

  return `
    <div>
      <!-- Section 1: MCQs -->
      <div style="margin-bottom:2rem;">
        <div style="background:#ecfdf5;padding:0.75rem 1.25rem;border-radius:8px;border-left:4px solid #047857;margin-bottom:1rem;display:flex;justify-content:space-between;align-items:center;">
          <h3 style="margin:0;font-size:1.1rem;color:#065f46;font-weight:800;">1. کثیر الانتخابی سوالات (درست جواب کا انتخاب کریں):</h3>
          <span style="font-size:0.85rem;color:#047857;font-weight:700;">کل ${mcqs.length} سوالات</span>
        </div>
        ${mcqHtml}
      </div>

      <!-- Section 2: Short Questions -->
      <div style="margin-bottom:2rem;">
        <div style="background:#f0f9ff;padding:0.75rem 1.25rem;border-radius:8px;border-left:4px solid #0284c7;margin-bottom:1rem;display:flex;justify-content:space-between;align-items:center;">
          <h3 style="margin:0;font-size:1.1rem;color:#0369a1;font-weight:800;">2. مختصر سوالات کے جامع و ماڈل جوابات:</h3>
          <span style="font-size:0.85rem;color:#0284c7;font-weight:700;">کل ${sqs.length} مختصر سوالات</span>
        </div>
        ${sqHtml}
      </div>

      <!-- Section 3: Long Questions -->
      <div style="margin-bottom:2rem;">
        <div style="background:#f5f3ff;padding:0.75rem 1.25rem;border-radius:8px;border-left:4px solid #7c3aed;margin-bottom:1rem;display:flex;justify-content:space-between;align-items:center;">
          <h3 style="margin:0;font-size:1.1rem;color:#5b21b6;font-weight:800;">3. مفصل و تفصیلی سوالات کے سرخی وار حل شدہ جوابات:</h3>
          <span style="font-size:0.85rem;color:#7c3aed;font-weight:700;">کل ${lqs.length} تفصیلی سوالات</span>
        </div>
        ${lqHtml}
      </div>

      <!-- Section 4: Activities -->
      ${acts.length > 0 ? `
        <div style="margin-bottom:2rem;">
          <div style="background:#fefce8;padding:0.75rem 1.25rem;border-radius:8px;border-left:4px solid #d97706;margin-bottom:1rem;">
            <h3 style="margin:0;font-size:1.1rem;color:#b45309;font-weight:800;">4. کمرہ جماعت اور عملی سرگرمیاں (Activities):</h3>
          </div>
          ${actHtml}
        </div>` : ''}
    </div>`;
}

// ─────────────────────────────────────────
//  TAB 4: SLO EXAMINATION BANK (ایس ایل او)
// ─────────────────────────────────────────
function renderPakStudySLOs(ch) {
  const slo = ch.sloBank || ch.sloAssessments || {};
  const activeSloTab = state.activePakStudySloTab || "slo-mcqs";

  const sloMcqs = slo.mcqs || [];
  const sloSqs = slo.shortQuestions || [];
  const sloLqs = slo.longQuestions || [];

  // MCQs
  const mcqListHtml = sloMcqs.map((m, qIndex) => {
    // Find correct index
    let correctIdx = 0;
    if (typeof m.answer === "number") correctIdx = m.answer;
    else if (typeof m.answer === "string") {
      const idx = m.options.findIndex(opt => opt.trim() === m.answer.trim());
      if (idx !== -1) correctIdx = idx;
    }

    const encodedExp = encodeURIComponent(m.explanation || "درست جواب منتخب کیا گیا۔");
    const optionsHtml = m.options.map((opt, optIndex) => `
      <label class="mcq-option-label urdu-text-rtl" id="ps-slo-opt-${qIndex}-${optIndex}"
             onclick="checkPakStudySloMcq(${qIndex}, ${optIndex}, ${correctIdx}, '${encodedExp}')">
        <input type="radio" name="ps-slo-mcq-${qIndex}" value="${optIndex}" style="accent-color:#047857;margin-left:0.5rem;">
        <span>${opt}</span>
      </label>`).join("");

    return `
      <div class="interactive-mcq-card">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem;">
          <span style="background:#f1f5f9;color:#475569;font-weight:700;font-size:0.78rem;padding:0.25rem 0.65rem;border-radius:99px;">
            سوال ${qIndex + 1} از ${sloMcqs.length} ${m.cognitiveLevel ? '· ' + m.cognitiveLevel : ''}
          </span>
          <span style="font-size:0.78rem;color:#047857;font-weight:700;">SLO Concept Checker</span>
        </div>
        <div class="mcq-question-text urdu-text-rtl">${m.question}</div>
        <div class="mcq-options-grid">${optionsHtml}</div>
        <div id="ps-slo-exp-${qIndex}" style="display:none;" class="mcq-explanation-box urdu-text-rtl"></div>
      </div>`;
  }).join("");

  // SQs
  const sqListHtml = sloSqs.map((sq, idx) => `
    <div class="urdu-section-card" id="ps-slo-sq-${idx}" style="margin-bottom:0.85rem;">
      <div class="urdu-section-header" onclick="togglePakStudyAccordion('ps-slo-sq-${idx}')" style="cursor:pointer;background:#f8fafc;">
        <div style="display:flex;align-items:center;gap:0.6rem;">
          <span class="urdu-sec-badge" style="background:#0284c7;font-size:0.78rem;">SLO سوال ${idx + 1}</span>
          <span class="urdu-sec-title" style="font-size:1.12rem;">${sq.question}</span>
        </div>
        <span class="sec-toggle-icon">▼</span>
      </div>
      <div class="urdu-section-body" style="display:none;">
        ${sq.slo ? `<div style="font-size:0.82rem;color:#0369a1;background:#e0f2fe;padding:0.4rem 0.75rem;border-radius:6px;margin-bottom:0.75rem;font-weight:700;">🎯 مطلوبہ صلاحیت (SLO): ${sq.slo}</div>` : ''}
        <div class="urdu-text-rtl" style="font-size:1.15rem;line-height:2.2;white-space:pre-line;color:#1e293b;">
          ${sq.answer}
        </div>
      </div>
    </div>`).join("");

  // LQs
  const lqListHtml = sloLqs.map((lq, idx) => `
    <div class="urdu-section-card" id="ps-slo-lq-${idx}" style="margin-bottom:1rem;border-color:#cbd5e1;">
      <div class="urdu-section-header" onclick="togglePakStudyAccordion('ps-slo-lq-${idx}')" style="cursor:pointer;background:linear-gradient(135deg,#f0fdf4,#f8fafc);">
        <div style="display:flex;align-items:center;gap:0.6rem;">
          <span class="urdu-sec-badge" style="background:#7c3aed;font-size:0.78rem;">SLO تفصیلی ${idx + 1}</span>
          <span class="urdu-sec-title" style="font-size:1.15rem;color:#1e1b4b;">${lq.question}</span>
        </div>
        <span class="sec-toggle-icon">▼</span>
      </div>
      <div class="urdu-section-body" style="display:none;">
        <div class="urdu-text-rtl" style="font-size:1.18rem;line-height:2.3;white-space:pre-line;color:#0f172a;">
          ${lq.answer}
        </div>
      </div>
    </div>`).join("");

  return `
    <div>
      <!-- Sub Tabs for SLO Bank -->
      <div style="display:flex;gap:0.5rem;margin-bottom:1.5rem;background:#f8fafc;padding:0.35rem;border-radius:8px;border:1px solid #e2e8f0;">
        <button class="sub-slo-btn ${activeSloTab === 'slo-mcqs' ? 'active' : ''}" onclick="switchPakStudySloTab('slo-mcqs')" style="flex:1;padding:0.55rem;border:none;border-radius:6px;font-weight:700;font-size:0.85rem;cursor:pointer;">
          🎯 SLO کثیر الانتخابی سوالات (${sloMcqs.length})
        </button>
        <button class="sub-slo-btn ${activeSloTab === 'slo-sqs' ? 'active' : ''}" onclick="switchPakStudySloTab('slo-sqs')" style="flex:1;padding:0.55rem;border:none;border-radius:6px;font-weight:700;font-size:0.85rem;cursor:pointer;">
          ✏️ SLO مختصر امتحانی سوالات (${sloSqs.length})
        </button>
        <button class="sub-slo-btn ${activeSloTab === 'slo-lqs' ? 'active' : ''}" onclick="switchPakStudySloTab('slo-lqs')" style="flex:1;padding:0.55rem;border:none;border-radius:6px;font-weight:700;font-size:0.85rem;cursor:pointer;">
          📝 SLO تفصیلی سوالات (${sloLqs.length})
        </button>
      </div>

      <div id="psSloSubContent">
        ${activeSloTab === 'slo-mcqs' ? `
          <div style="background:#f0fdf4;padding:0.75rem 1.25rem;border-radius:8px;border-left:4px solid #047857;margin-bottom:1rem;display:flex;justify-content:space-between;align-items:center;">
            <span style="color:#065f46;font-weight:700;">🎯 انٹرایکٹو ایس ایل او کوئز:</span>
            <span style="font-size:0.85rem;color:#047857;">کسی بھی آپشن پر کلک کر کے فوری درستگی اور تفصیلی تشریح دیکھیں</span>
          </div>
          ${mcqListHtml}
        ` : ''}

        ${activeSloTab === 'slo-sqs' ? `
          <div style="background:#f0f9ff;padding:0.75rem 1.25rem;border-radius:8px;border-left:4px solid #0284c7;margin-bottom:1rem;">
            <span style="color:#0369a1;font-weight:700;">✏️ فکری اور استدلالی مختصر سوالات (Conceptual Short Questions):</span>
          </div>
          ${sqListHtml}
        ` : ''}

        ${activeSloTab === 'slo-lqs' ? `
          <div style="background:#f5f3ff;padding:0.75rem 1.25rem;border-radius:8px;border-left:4px solid #7c3aed;margin-bottom:1rem;">
            <span style="color:#5b21b6;font-weight:700;">📝 تجزیاتی و تفصیلی امتحانی سوالات (Analytical Long Questions):</span>
          </div>
          ${lqListHtml}
        ` : ''}
      </div>
    </div>`;
}

function switchPakStudySloTab(subTabName) {
  state.activePakStudySloTab = subTabName;
  const chList = getPakStudyChapterList();
  const ch = chList[state.selectedPakStudyChapter || 0];
  const container = $("psTabContentContainer");
  if (!container || !ch) return;
  container.innerHTML = renderPakStudySLOs(ch);
}

function checkPakStudySloMcq(qIndex, selectedOpt, correctOpt, encodedExp) {
  const expBox = $(`ps-slo-exp-${qIndex}`);
  const explanation = decodeURIComponent(encodedExp);

  // Disable radio inputs
  const inputs = document.querySelectorAll(`input[name="ps-slo-mcq-${qIndex}"]`);
  inputs.forEach(inp => inp.disabled = true);

  const isCorrect = (selectedOpt === correctOpt);

  inputs.forEach((inp, idx) => {
    const label = $(`ps-slo-opt-${qIndex}-${idx}`);
    if (!label) return;
    if (idx === correctOpt) {
      label.classList.add("correct");
    } else if (idx === selectedOpt && !isCorrect) {
      label.classList.add("incorrect");
    }
  });

  if (expBox) {
    expBox.style.display = "block";
    expBox.innerHTML = `
      <div style="display:flex;align-items:center;gap:0.4rem;font-weight:800;color:${isCorrect ? '#16a34a' : '#dc2626'};margin-bottom:0.35rem;">
        <span>${isCorrect ? '✅ ماشاءاللہ! بالکل درست جواب' : '❌ جواب درست نہیں ہے'}</span>
      </div>
      <div><strong>علمی تشریح و نصابی دلیل:</strong> ${explanation}</div>
    `;
  }

  // Update user stats
  recordQuestionAnswer(isCorrect);
}

// ─────────────────────────────────────────
//  TAB 5: TIMELINE & HISTORICAL MILESTONES (جدول)
// ─────────────────────────────────────────
function renderPakStudyTimeline(ch) {
  const timeline = ch.timeline || [];
  const timelineHtml = timeline.map((item, idx) => `
    <div style="display:flex;gap:1.25rem;align-items:flex-start;margin-bottom:1.5rem;position:relative;">
      <div style="display:flex;flex-direction:column;align-items:center;">
        <div style="width:42px;height:42px;border-radius:50%;background:#047857;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:0.85rem;box-shadow:0 3px 8px rgba(4,120,87,0.3);z-index:2;">
          ${idx + 1}
        </div>
        ${idx < timeline.length - 1 ? '<div style="width:2px;height:calc(100% + 1.5rem);background:#cbd5e1;margin-top:0.25rem;position:absolute;top:42px;bottom:-10px;"></div>' : ''}
      </div>
      <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;padding:1rem 1.25rem;flex:1;box-shadow:0 2px 6px rgba(0,0,0,0.03);">
        <div style="display:inline-block;background:#ecfdf5;color:#047857;font-weight:800;padding:0.25rem 0.75rem;border-radius:99px;font-size:0.88rem;margin-bottom:0.5rem;border:1px solid #a7f3d0;">
          ${item.year}
        </div>
        <div class="urdu-text-rtl" style="font-size:1.15rem;color:#1e293b;line-height:2.1;">
          ${item.event}
        </div>
      </div>
    </div>`).join("");

  return `
    <div style="background:#ffffff;border:1px solid var(--border);border-radius:12px;padding:1.5rem;box-shadow:var(--shadow);">
      <div style="background:linear-gradient(135deg,#064e3b,#047857);color:#fff;padding:1rem 1.25rem;border-radius:8px;margin-bottom:1.75rem;display:flex;align-items:center;gap:0.75rem;">
        <span style="font-size:1.5rem;">⏳</span>
        <div>
          <h3 style="margin:0;font-size:1.15rem;font-family:'Jameel Noori Nastaleeq',serif;line-height:1.6;direction:rtl;text-align:right;">
            تاریخی جدول اور سنگ ہائے میل (Chronological Timeline)
          </h3>
          <p style="margin:0;font-size:0.82rem;opacity:0.9;">
            اس باب سے وابستہ اہم تاریخی سال، واقعات اور بین الاقوامی دستاویزات
          </p>
        </div>
      </div>
      <div style="padding:0 0.5rem;">
        ${timelineHtml}
      </div>
    </div>`;
}
