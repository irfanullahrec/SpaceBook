import os

css_path = os.path.join(os.path.dirname(__file__), '..', 'css', 'style.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update #top-header
old_header = """#top-header {
  position: fixed; top: 0; left: 0; right: 0;
  height: var(--header-h);
  background: #ffffff;"""

new_header = """#top-header {
  position: fixed; top: 0; left: 0; right: 0;
  height: var(--header-h);
  background: #ffffff url("../banner_kpk_academic.png") no-repeat center center;
  background-size: cover;"""

if old_header in css:
    css = css.replace(old_header, new_header, 1)
    print("Updated #top-header background")
else:
    print("Warning: old_header not found")

# 2. Add brand/hamburger enhancements for contrast
old_brand = """.header-brand {
  display: flex; align-items: center; gap: 0.55rem;
  cursor: pointer; user-select: none;
}"""

new_brand = """.header-brand {
  display: flex; align-items: center; gap: 0.55rem;
  cursor: pointer; user-select: none;
  background: rgba(255, 255, 255, 0.92);
  padding: 0.2rem 0.65rem;
  border-radius: 10px;
  border: 1px solid rgba(186, 224, 253, 0.85);
  box-shadow: 0 1px 4px rgba(2, 132, 199, 0.08);
  backdrop-filter: blur(4px);
}"""

if old_brand in css:
    css = css.replace(old_brand, new_brand, 1)
    print("Updated .header-brand contrast")
else:
    print("Warning: old_brand not found")

old_burger = """.hamburger-btn {
  width: 36px; height: 36px;
  background: transparent;
  border: none;
  border-radius: 8px;"""

new_burger = """.hamburger-btn {
  width: 36px; height: 36px;
  background: rgba(255, 255, 255, 0.92);
  border: 1px solid rgba(186, 224, 253, 0.85);
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(2, 132, 199, 0.08);
  backdrop-filter: blur(4px);"""

if old_burger in css:
    css = css.replace(old_burger, new_burger, 1)
    print("Updated .hamburger-btn contrast")
else:
    print("Warning: old_burger not found")

# 3. Update classes view positioning to shift classes up near header
old_cw = """body:has(.classes-universe-wrapper) #main-wrapper {
  margin-top: calc(var(--top-total-h) + 6px);
  min-height: calc(100vh - var(--top-total-h) - 6px);
}
body:has(.classes-universe-wrapper) #page-content {
  width: 100%;
  max-width: none;
  padding: .35rem 1.15rem .75rem;"""

new_cw = """body:has(.classes-universe-wrapper) #main-wrapper {
  margin-top: calc(var(--header-h) + 2px);
  min-height: calc(100vh - var(--header-h) - 2px);
}
body:has(.classes-universe-wrapper) #page-content {
  width: 100%;
  max-width: none;
  padding: .15rem 1.15rem .5rem;"""

if old_cw in css:
    css = css.replace(old_cw, new_cw, 1)
    print("Updated classes view margin-top and padding to shift up near header")
else:
    print("Warning: old_cw not found")

# 4. Update subjects-compact-grid for Class 1 (and all classes) to fit both rows without scroll down
old_grid = """.subjects-compact-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.5rem;
  height: calc(100vh - 110px);
  overflow-y: auto;
  align-content: start;
  padding-bottom: 1rem;
}

.subjects-compact-grid.cols-3 { grid-template-columns: repeat(3, 1fr); }
.subjects-compact-grid.cols-4 { grid-template-columns: repeat(4, 1fr); }
.subjects-compact-grid.cols-5 { grid-template-columns: repeat(5, 1fr); }
.subjects-compact-grid.cols-6 { grid-template-columns: repeat(6, 1fr); }
.subjects-compact-grid.cols-7 { grid-template-columns: repeat(7, 1fr); }
.subjects-compact-grid.cols-8 { grid-template-columns: repeat(8, 1fr); }"""

new_grid = """body:has(.subjects-compact-grid) #main-wrapper {
  margin-top: calc(var(--header-h) + 4px);
  min-height: calc(100vh - var(--header-h) - 4px);
}
body:has(.subjects-compact-grid) #page-content {
  padding: 0.15rem 1.15rem 0.4rem;
  max-width: 1480px;
}
body:has(.subjects-compact-grid) #footer {
  display: none !important;
}

.subjects-compact-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.4rem 0.65rem;
  max-height: calc(100vh - var(--header-h) - 14px);
  overflow-y: auto;
  align-content: start;
  justify-content: center;
  padding-bottom: 0.25rem;
}

.subjects-compact-grid.cols-3 { grid-template-columns: repeat(3, minmax(0, 250px)); justify-content: center; }
.subjects-compact-grid.cols-4 { grid-template-columns: repeat(4, minmax(0, 230px)); justify-content: center; }
.subjects-compact-grid.cols-5 { grid-template-columns: repeat(5, minmax(0, 220px)); justify-content: center; }
.subjects-compact-grid.cols-6 { grid-template-columns: repeat(6, minmax(0, 200px)); justify-content: center; }
.subjects-compact-grid.cols-7 { grid-template-columns: repeat(7, minmax(0, 185px)); justify-content: center; }
.subjects-compact-grid.cols-8 { grid-template-columns: repeat(8, minmax(0, 175px)); justify-content: center; }"""

if old_grid in css:
    css = css.replace(old_grid, new_grid, 1)
    print("Updated subjects-compact-grid columns and spacing")
else:
    print("Warning: old_grid not found")

# 5. Update .subject-card-compact and .scc-title-row
old_card = """.subject-card-compact {
  background: #ffffff;
  border: 1.5px solid #e2e8f0;
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
  width: 100%;
  aspect-ratio: 3/4;
  position: relative;
  display: block;
}"""

new_card = """.subject-card-compact {
  background: #ffffff;
  border: 1.5px solid #e2e8f0;
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
  width: 100%;
  max-height: clamp(160px, 34vh, 245px);
  aspect-ratio: 3/4;
  position: relative;
  display: block;
}"""

if old_card in css:
    css = css.replace(old_card, new_card, 1)
    print("Updated .subject-card-compact max-height clamp")
else:
    print("Warning: old_card not found")

old_title = """.scc-title-row {
  padding: 0.35rem 0.2rem 0.15rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  gap: 0.1rem;
  flex-shrink: 0;
  width: 100%;
  min-height: 2.85rem;
  max-height: 2.85rem;
  box-sizing: border-box;
}"""

new_title = """.scc-title-row {
  padding: 0.2rem 0.2rem 0.1rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  gap: 0.05rem;
  flex-shrink: 0;
  width: 100%;
  min-height: 2.35rem;
  max-height: 2.45rem;
  box-sizing: border-box;
}"""

if old_title in css:
    css = css.replace(old_title, new_title, 1)
    print("Updated .scc-title-row padding and height")
else:
    print("Warning: old_title not found")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS updates written successfully!")
