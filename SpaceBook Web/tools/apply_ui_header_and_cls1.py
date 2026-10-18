import os

# 1. Update SpaceBook Web/css/style.css
css_path = r'D:\SpaceBook\SpaceBook Web\css\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Revert #top-header background to clean white #ffffff
old_top_header = """#top-header {
  position: fixed; top: 0; left: 0; right: 0;
  height: var(--header-h);
  background: #ffffff url("../banner_kpk_academic.png") no-repeat center center;
  background-size: cover;
  color: #0f172a;
  z-index: 950;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 1.15rem;
  gap: 0.75rem;
  border-bottom: 1px solid #e2e8f0;
  box-shadow: 0 1px 4px rgba(0,0,0,0.03);
}"""

clean_top_header = """#top-header {
  position: fixed; top: 0; left: 0; right: 0;
  height: var(--header-h);
  background: #ffffff;
  color: #0f172a;
  z-index: 950;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 1.15rem;
  gap: 0.75rem;
  border-bottom: 1px solid #e2e8f0;
  box-shadow: 0 1px 4px rgba(0,0,0,0.03);
}"""

if old_top_header in css:
    css = css.replace(old_top_header, clean_top_header, 1)
    print("Reverted #top-header background to #ffffff")
else:
    # check if partial match
    import re
    css = re.sub(
        r'#top-header\s*\{[^}]*background:[^;]*banner_kpk_academic\.png[^}]*\}',
        clean_top_header,
        css
    )
    print("Reverted #top-header via regex")

# Revert .hamburger-btn and .header-brand
old_burger = """.hamburger-btn {
  width: 36px; height: 36px;
  background: rgba(255, 255, 255, 0.92);
  border: 1px solid rgba(186, 224, 253, 0.85);
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(2, 132, 199, 0.08);
  backdrop-filter: blur(4px);"""

clean_burger = """.hamburger-btn {
  width: 36px; height: 36px;
  background: transparent;
  border: none;
  border-radius: 8px;"""

if old_burger in css:
    css = css.replace(old_burger, clean_burger, 1)
    print("Reverted .hamburger-btn")

old_brand = """.header-brand {
  display: flex; align-items: center; gap: 0.55rem;
  cursor: pointer; user-select: none;
  background: rgba(255, 255, 255, 0.92);
  padding: 0.2rem 0.65rem;
  border-radius: 10px;
  border: 1px solid rgba(186, 224, 253, 0.85);
  box-shadow: 0 1px 4px rgba(2, 132, 199, 0.08);
  backdrop-filter: blur(4px);
}"""

clean_brand = """.header-brand {
  display: flex; align-items: center; gap: 0.55rem;
  cursor: pointer; user-select: none;
}"""

if old_brand in css:
    css = css.replace(old_brand, clean_brand, 1)
    print("Reverted .header-brand")

# Add Class 1 full cover stage grid styles
cls1_css = """
/* ── CLASS 1 FULL COVER STAGE GRID (NO BLANK SPACE, FULL PAGE, UNHIDDEN COVERS) ── */
body:has(.cls1-cover-stage-grid) #main-wrapper {
  margin-top: var(--header-h) !important;
  min-height: calc(100vh - var(--header-h)) !important;
}
body:has(.cls1-cover-stage-grid) #page-content {
  padding: 8px 12px 10px !important;
  max-width: 100% !important;
  width: 100% !important;
  height: calc(100vh - var(--header-h)) !important;
  box-sizing: border-box !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: stretch !important;
  background: #ffffff !important;
}
body:has(.cls1-cover-stage-grid) #footer {
  display: none !important;
}

.cls1-cover-stage-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(2, 1fr);
  gap: 10px;
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cls1-cover-card {
  appearance: none;
  border: 1.5px solid #cbd5e1;
  border-radius: 12px;
  padding: 0;
  margin: 0;
  background: #ffffff;
  cursor: pointer;
  overflow: hidden;
  position: relative;
  width: 100%;
  height: 100%;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.08);
  transition: transform 0.18s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.18s ease, border-color 0.18s ease;
  display: flex;
}
.cls1-cover-card:hover {
  transform: translateY(-2px) scale(1.01);
  border-color: #0284c7;
  box-shadow: 0 8px 20px rgba(2, 132, 199, 0.22);
  z-index: 2;
}

.cls1-cover-img {
  width: 100%;
  height: 100%;
  object-fit: fill;
  display: block;
  border-radius: 10px;
}
"""

if '.cls1-cover-stage-grid' not in css:
    css += '\n' + cls1_css
    print("Added .cls1-cover-stage-grid styles to style.css")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("style.css updated successfully!")

# 2. Update SpaceBook Web/js/app.js for Class 1 rendering
app_path = r'D:\SpaceBook\SpaceBook Web\js\app.js'
with open(app_path, 'r', encoding='utf-8') as f:
    app = f.read()

old_render = """pageContent().innerHTML = `
    <div class="subjects-compact-grid ${gridColsClass}">"""

new_render = """if (classId === 'cls1') {
    pageContent().innerHTML = `
      <div class="cls1-cover-stage-grid">
        ${displaySubs.map(s => {
          const coverSrc = getCoverPage(s.id);
          const imgHtml = coverSrc ? `<img class="cls1-cover-img" src="${coverSrc}" alt="${s.name} cover" loading="lazy">` : `<div class="scc-placeholder">${s.emoji}</div>`;
          return `
          <button type="button" class="cls1-cover-card" onclick="openSubject('${classId}','${s.id}')" title="Explore ${s.name} units & solved notes" aria-label="${s.name}">
            ${imgHtml}
          </button>`;
        }).join("")}
      </div>`;
    return;
  }

pageContent().innerHTML = `
    <div class="subjects-compact-grid ${gridColsClass}">"""

if "if (classId === 'cls1')" not in app:
    if old_render in app:
        app = app.replace(old_render, new_render, 1)
        print("Updated app.js goToSubjects to render cls1-cover-stage-grid for Class 1")
    else:
        print("Warning: old_render target not found in app.js")
else:
    print("Class 1 custom rendering already in app.js")

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(app)

print("app.js updated successfully!")
