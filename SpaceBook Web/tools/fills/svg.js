'use strict';
/* Small drawings used by the fills (tools/fills/build_fills.js): a Bohr model of an atom and a Lewis dot structure.
 * Dev-only, never shipped: the build writes the finished SVG text into js/fills_data.js. */
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

/* bohr({sym, p, n, shells:[2,8,1]}) -> an atom: the nucleus (protons and neutrons) in the middle, one ring per shell with its electrons on it */
function bohr(a) {
  const shells = a.shells, size = 2 * (30 + 24 * shells.length) + 10, c = size / 2;
  let out = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${size} ${size}" width="${size}" role="img" aria-label="${esc(a.label || `Bohr model of ${a.sym}: ${a.p} protons, ${a.n} neutrons, shells ${shells.join(', ')}`)}">`;
  shells.forEach((n, k) => {
    const r = 30 + 24 * (k + 1);
    out += `<circle cx="${c}" cy="${c}" r="${r}" fill="none" stroke="#64748b" stroke-width="1.5"/>`;
    for (let i = 0; i < n; i++) {
      const ang = (2 * Math.PI * i) / n - Math.PI / 2 + (k % 2 ? Math.PI / n : 0);
      out += `<circle cx="${(c + r * Math.cos(ang)).toFixed(1)}" cy="${(c + r * Math.sin(ang)).toFixed(1)}" r="5" fill="#2563eb"/>`;
    }
  });
  out += `<circle cx="${c}" cy="${c}" r="30" fill="#fde68a" stroke="#b45309" stroke-width="2"/>`;
  out += `<text x="${c}" y="${c - 4}" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" font-weight="700" fill="#451a03">${a.p}p</text>`;
  out += `<text x="${c}" y="${c + 12}" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" font-weight="700" fill="#451a03">${a.n}n</text>`;
  return out + '</svg>';
}

/* lewis({atoms:[{s, x, y, lp:['t','b','l','r']}], bonds:[[i, j, pairs, arrow?]], w, h}) -> the dots of a Lewis structure:
 * a shared pair is two dots across the bond, a lone pair two dots at one side of its atom (t top, b bottom, l left, r right) */
function lewis(m) {
  const w = m.w || 130, h = m.h || 90;
  let out = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" width="${w}" role="img" aria-label="${esc(m.label || 'Lewis structure')}">`;
  const dot = (x, y) => `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="2.3" fill="#0f172a"/>`;
  m.atoms.forEach(a => {
    out += `<text x="${a.x}" y="${a.y + 5.5}" text-anchor="middle" font-family="system-ui,sans-serif" font-size="17" font-weight="800" fill="#1e3a8a">${esc(a.s)}</text>`;
    (a.lp || []).forEach(side => {
      const d = 15;
      if (side === 't') out += dot(a.x - 3.6, a.y - d) + dot(a.x + 3.6, a.y - d);
      if (side === 'b') out += dot(a.x - 3.6, a.y + d) + dot(a.x + 3.6, a.y + d);
      if (side === 'l') out += dot(a.x - d, a.y - 3.6) + dot(a.x - d, a.y + 3.6);
      if (side === 'r') out += dot(a.x + d, a.y - 3.6) + dot(a.x + d, a.y + 3.6);
    });
  });
  (m.bonds || []).forEach(([i, j, pairs, arrow]) => {
    const A = m.atoms[i], B = m.atoms[j], dx = B.x - A.x, dy = B.y - A.y, len = Math.hypot(dx, dy), ux = dx / len, uy = dy / len, px = -uy, py = ux;
    const mx = (A.x + B.x) / 2, my = (A.y + B.y) / 2, step = 7;
    for (let k = 0; k < pairs; k++) {
      const off = (k - (pairs - 1) / 2) * step;
      out += dot(mx + ux * off + px * 3.6, my + uy * off + py * 3.6) + dot(mx + ux * off - px * 3.6, my + uy * off - py * 3.6);
    }
    if (arrow) {      // a coordinate (dative) bond: a small arrow from the atom that gave the pair to the one that took it
      const ax = mx + px * 9, ay = my + py * 9, hx = ux * 5, hy = uy * 5;
      out += `<path d="M${(ax - hx).toFixed(1)} ${(ay - hy).toFixed(1)} L${(ax + hx).toFixed(1)} ${(ay + hy).toFixed(1)} M${(ax + hx - ux * 3 + px * 3).toFixed(1)} ${(ay + hy - uy * 3 + py * 3).toFixed(1)} L${(ax + hx).toFixed(1)} ${(ay + hy).toFixed(1)} L${(ax + hx - ux * 3 - px * 3).toFixed(1)} ${(ay + hy - uy * 3 - py * 3).toFixed(1)}" fill="none" stroke="#b91c1c" stroke-width="1.4"/>`;
    }
  });
  return out + '</svg>';
}
module.exports = { bohr, lewis };
