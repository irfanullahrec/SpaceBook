f = r'D:\SpaceBook\SpaceBook Web\docs\source-verification\class-5\tools\build_math5.py'
s = open(f, encoding='utf-8').read()
if 'FIG5_OPS' not in s:
    s = s.replace("import figs\n", "import figs\nimport figs5\nFIG5_OPS = [k for k, v in vars(figs5).items() if callable(v) and not k.startswith('_')]\nfor _k in FIG5_OPS:\n    setattr(figs, _k, getattr(figs5, _k))\n", 1)
    old = "'chart', 'pie', 'spinner', 'ptree'):"
    assert old in s
    s = s.replace(old, "'chart', 'pie', 'spinner', 'ptree') or op in FIG5_OPS:")
    open(f, 'w', encoding='utf-8').write(s)
print('ok')
