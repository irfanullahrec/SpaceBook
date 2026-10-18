f = r'D:\SpaceBook\SpaceBook Web\docs\source-verification\class-5\tools\figs5.py'
s = open(f, encoding='utf-8').read()
old = """        nx, ny = mx - gx, my - gy
        ln = math.hypot(nx, ny) or 1
        if i < len(sides) and sides[i]:
            out.append(_t(mx + nx / ln * 20, my + ny / ln * 20 + 5, sides[i], 14))"""
new = """        ex_, ey_ = x2 - x1, y2 - y1
        el_ = math.hypot(ex_, ey_) or 1
        nx, ny = -ey_ / el_, ex_ / el_
        if nx * (mx - gx) + ny * (my - gy) < 0:
            nx, ny = -nx, -ny
        if i < len(sides) and sides[i]:
            off = 14 + 3.4 * len(sides[i]) * abs(nx)
            out.append(_t(mx + nx * off, my + ny * 16 + 5, sides[i], 14))"""
if old in s:
    s = s.replace(old, new)
    open(f, 'w', encoding='utf-8').write(s)
    print('patched')
else:
    print('already/absent')
