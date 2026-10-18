"""Render all figs1 icons (and given figure specs) into one HTML sheet, then a PNG via headless Edge.
   iconsheet.py OUT.png ['op spec' ...]      (used only to eyeball the coded figures, not the website)"""
import sys, subprocess, os, re, inspect
import figs1
src = inspect.getsource(figs1._icon)
names = re.findall(r"^\s+'([a-z0-9]+)': f?'", src, re.M)
extra = ['coin1', 'coin2', 'coin5', 'coin10', 'note10', 'note20', 'note50', 'note100', 'note500', 'note1000', 'note5000', 'hand0', 'hand3', 'hand5']
cells = ''.join(f'<div style="display:inline-block;width:70px;text-align:center;font:10px sans-serif">{figs1.cnt(n + ":1")}<br>{n}</div>' for n in names + extra) if '--noicons' not in sys.argv else ''
specs = [s for s in sys.argv[2:] if s != '--noicons']
figs = ''.join(f'<div style="margin:6px;border:1px solid #ccc;display:inline-block">{getattr(figs1, s.split(" ", 1)[0])(s.split(" ", 1)[1])}</div><div style="font:11px monospace">{s}</div>' for s in specs)
html = f'<html><body style="margin:4px;background:#fff">{cells}<hr>{figs}</body></html>'
hp = os.path.join(os.environ.get('TEMP', '.'), 'c1_iconsheet.html')
open(hp, 'w', encoding='utf-8').write(html)
out = os.path.abspath(sys.argv[1])
edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
subprocess.run([edge, '--headless', '--disable-gpu', f'--screenshot={out}', '--window-size=1200,1400', 'file:///' + hp.replace(os.sep, '/')], capture_output=True, timeout=90)
print(out, os.path.exists(out))
