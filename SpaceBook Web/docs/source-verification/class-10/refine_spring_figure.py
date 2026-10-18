from pathlib import Path
p=Path(r'D:\SpaceBook\SpaceBook Web\js\physics_10_source_data.js')
t=p.read_text(encoding='utf-8')
force='stroke="#991b1b" stroke-width="3" marker-end="url(#phys10-spring-arrow)"'
axis='stroke="#1e3a8a" stroke-width="2" marker-start="url(#phys10-axis-arrow)" marker-end="url(#phys10-axis-arrow)"'
replacements={
    f'<path d="M275 94H172M307 94H400" {force}/>':f'<path d="M275 94H172" {force}/><path d="M307 94H400" {force}/>',
    f'<path d="M207 179H279M85 48H170" {axis}/>':f'<path d="M207 179H279" {axis}/><path d="M85 48H170" {axis}/>'
}
for old,new in replacements.items():
    if old in t:
        assert t.count(old)==1
        t=t.replace(old,new,1)
    else:
        assert new in t
p.write_text(t,encoding='utf-8',newline='\n')
print('Separated force and dimension paths so every arrowhead renders.')
