# -*- coding: utf-8 -*-
"""SVG generators for Class 2 Mathematics instructional diagrams.
Pure code generation (no raster images, screenshots, or base64 bitmaps).
"""
import math
from html import escape

FONT = 'font-family="system-ui, -apple-system, Segoe UI, Roboto, sans-serif" font-size="14" fill="#0f172a"'

def number_line(start, end, jumps=None, highlight=None, width=540, height=80):
    """Draws a clean, child-friendly horizontal number line."""
    pad = 40
    step_px = (width - 2 * pad) / max(end - start, 1)
    y_axis = 45
    
    parts = []
    # Main horizontal axis with arrowheads
    parts.append(f'<line x1="{pad-15}" y1="{y_axis}" x2="{width-pad+15}" y2="{y_axis}" stroke="#0284c7" stroke-width="2.5" />')
    parts.append(f'<polygon points="{pad-18},{y_axis} {pad-10},{y_axis-5} {pad-10},{y_axis+5}" fill="#0284c7" />')
    parts.append(f'<polygon points="{width-pad+18},{y_axis} {width-pad+10},{y_axis-5} {width-pad+10},{y_axis+5}" fill="#0284c7" />')
    
    for val in range(start, end + 1):
        x = pad + (val - start) * step_px
        is_hl = (highlight is not None and val == highlight)
        tick_h = 10 if val % 5 == 0 else 6
        color = "#e11d48" if is_hl else "#0284c7"
        
        parts.append(f'<line x1="{x}" y1="{y_axis - tick_h}" x2="{x}" y2="{y_axis + tick_h}" stroke="{color}" stroke-width="{2 if is_hl else 1.5}" />')
        parts.append(f'<text x="{x}" y="{y_axis + 24}" text-anchor="middle" font-size="{13 if is_hl else 11}" font-weight="{"700" if is_hl else "500"}" fill="{color}">{val}</text>')
        
        if is_hl:
            parts.append(f'<circle cx="{x}" cy="{y_axis}" r="5" fill="#e11d48" />')
            
    # Optional jump arcs
    if jumps:
        for j_start, j_end, j_label in jumps:
            x1 = pad + (j_start - start) * step_px
            x2 = pad + (j_end - start) * step_px
            mid_x = (x1 + x2) / 2
            arc_h = 24
            parts.append(f'<path d="M {x1} {y_axis - 6} Q {mid_x} {y_axis - 6 - arc_h} {x2} {y_axis - 6}" fill="none" stroke="#16a34a" stroke-width="2" stroke-dasharray="3,3" />')
            parts.append(f'<polygon points="{x2},{y_axis - 6} {x2-4},{y_axis - 12} {x2+2},{y_axis - 12}" fill="#16a34a" />')
            if j_label:
                parts.append(f'<text x="{mid_x}" y="{y_axis - 6 - arc_h + 8}" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">{escape(j_label)}</text>')
                
    label = f"Number line from {start} to {end}"
    return f'<svg viewBox="0 0 {width} {height}" width="100%" style="max-width:{width}px;" role="img" aria-label="{escape(label)}" {FONT}>{"".join(parts)}</svg>'


def place_value_blocks(hundreds=0, tens=0, ones=0, width=480, height=130):
    """Draws Dienes blocks: Hundreds (10x10 squares), Tens (1x10 rods), and Ones (unit cubes)."""
    parts = []
    # Background card
    parts.append(f'<rect width="{width}" height="{height}" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>')
    
    # Hundreds section
    hx = 20
    parts.append(f'<text x="{hx + 40}" y="24" text-anchor="middle" font-weight="700" fill="#0369a1">Hundreds ({hundreds})</text>')
    for i in range(min(hundreds, 4)):
        ox = hx + i * 16
        oy = 34 + i * 4
        parts.append(f'<rect x="{ox}" y="{oy}" width="70" height="70" fill="#bae6fd" stroke="#0284c7" stroke-width="1.2" rx="3"/>')
        # Grid lines inside
        for g in range(1, 10):
            parts.append(f'<line x1="{ox + g*7}" y1="{oy}" x2="{ox + g*7}" y2="{oy + 70}" stroke="#7dd3fc" stroke-width="0.6"/>')
            parts.append(f'<line x1="{ox}" y1="{oy + g*7}" x2="{ox + 70}" y2="{oy + g*7}" stroke="#7dd3fc" stroke-width="0.6"/>')
            
    # Tens section
    tx = 180
    parts.append(f'<text x="{tx + 45}" y="24" text-anchor="middle" font-weight="700" fill="#047857">Tens ({tens})</text>')
    for i in range(min(tens, 9)):
        ox = tx + i * 11
        oy = 38
        parts.append(f'<rect x="{ox}" y="{oy}" width="8" height="66" fill="#a7f3d0" stroke="#059669" stroke-width="1.2" rx="2"/>')
        for g in range(1, 10):
            parts.append(f'<line x1="{ox}" y1="{oy + g*6.6}" x2="{ox + 8}" y2="{oy + g*6.6}" stroke="#34d399" stroke-width="0.6"/>')
            
    # Ones section
    ox_start = 320
    parts.append(f'<text x="{ox_start + 50}" y="24" text-anchor="middle" font-weight="700" fill="#b91c1c">Ones ({ones})</text>')
    for i in range(min(ones, 15)):
        row = i // 5
        col = i % 5
        bx = ox_start + col * 18 + 10
        by = 40 + row * 18
        parts.append(f'<rect x="{bx}" y="{by}" width="14" height="14" fill="#fecdd3" stroke="#e11d48" stroke-width="1.2" rx="2"/>')
        
    total = hundreds * 100 + tens * 10 + ones
    label = f"Place value blocks: {hundreds} hundreds, {tens} tens, {ones} ones = {total}"
    return f'<svg viewBox="0 0 {width} {height}" width="100%" style="max-width:{width}px;" role="img" aria-label="{escape(label)}" {FONT}>{"".join(parts)}</svg>'


def array_groups(groups, per_group, item_label="items", width=420, height=100):
    """Draws grouped plates of objects for multiplication and repeated addition."""
    parts = []
    plate_w = (width - 30) / groups
    for g in range(groups):
        cx = 15 + g * plate_w + plate_w / 2
        cy = 50
        rx = min(plate_w / 2 - 6, 38)
        ry = 32
        parts.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5"/>')
        parts.append(f'<text x="{cx}" y="92" text-anchor="middle" font-size="11" font-weight="600" fill="#475569">Group {g+1}: {per_group}</text>')
        
        # Dots or stars inside
        for p in range(per_group):
            angle = 2 * math.pi * p / max(per_group, 1)
            dist = min(rx - 12, 16) if per_group > 1 else 0
            dx = cx + dist * math.cos(angle)
            dy = cy + (dist * 0.7) * math.sin(angle)
            parts.append(f'<circle cx="{dx}" cy="{dy}" r="5" fill="#f59e0b" stroke="#d97706" stroke-width="1"/>')
            
    label = f"{groups} groups of {per_group} = {groups * per_group}"
    return f'<svg viewBox="0 0 {width} {height}" width="100%" style="max-width:{width}px;" role="img" aria-label="{escape(label)}" {FONT}>{"".join(parts)}</svg>'


def fraction_circle(total_parts, shaded_parts, size=120):
    """Draws an SVG circle divided into equal sectors with shaded parts."""
    parts = []
    cx = size / 2
    cy = size / 2
    r = size / 2 - 8
    
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#f8fafc" stroke="#334155" stroke-width="2"/>')
    
    if total_parts == 1:
        if shaded_parts >= 1:
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#38bdf8"/>')
    else:
        angle_step = 2 * math.pi / total_parts
        for i in range(total_parts):
            a1 = i * angle_step - math.pi / 2
            a2 = (i + 1) * angle_step - math.pi / 2
            x1 = cx + r * math.cos(a1)
            y1 = cy + r * math.sin(a1)
            x2 = cx + r * math.cos(a2)
            y2 = cy + r * math.sin(a2)
            large_arc = 1 if (a2 - a1) > math.pi else 0
            
            fill = "#38bdf8" if i < shaded_parts else "#f8fafc"
            path_d = f"M {cx} {cy} L {x1} {y1} A {r} {r} 0 {large_arc} 1 {x2} {y2} Z"
            parts.append(f'<path d="{path_d}" fill="{fill}" stroke="#334155" stroke-width="1.5"/>')
            
    label = f"Fraction: {shaded_parts}/{total_parts}"
    return f'<svg viewBox="0 0 {size} {size}" width="{size}" height="{size}" role="img" aria-label="{escape(label)}">{"".join(parts)}</svg>'


def clock_face(hour, minute, size=130):
    """Draws an analogue clock with hour and minute hands."""
    parts = []
    cx = size / 2
    cy = size / 2
    r = size / 2 - 6
    
    # Rim and face
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" stroke="#0284c7" stroke-width="3"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="3.5" fill="#0f172a"/>')
    
    # 12 Hour numbers
    for h in range(1, 13):
        angle = (h * 30 - 90) * math.pi / 180
        nx = cx + (r - 14) * math.cos(angle)
        ny = cy + (r - 14) * math.sin(angle) + 4
        parts.append(f'<text x="{nx}" y="{ny}" text-anchor="middle" font-size="11" font-weight="700" fill="#1e293b">{h}</text>')
        
    # Hour hand (short, thicker)
    h_angle = ((hour % 12 + minute / 60) * 30 - 90) * math.pi / 180
    hx = cx + (r * 0.5) * math.cos(h_angle)
    hy = cy + (r * 0.5) * math.sin(h_angle)
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{hx}" y2="{hy}" stroke="#0f172a" stroke-width="3.5" stroke-linecap="round"/>')
    
    # Minute hand (long, thinner)
    m_angle = (minute * 6 - 90) * math.pi / 180
    mx = cx + (r * 0.75) * math.cos(m_angle)
    my = cy + (r * 0.75) * math.sin(m_angle)
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{mx}" y2="{my}" stroke="#e11d48" stroke-width="2.2" stroke-linecap="round"/>')
    
    label = f"Clock showing {hour}:{minute:02d}"
    return f'<svg viewBox="0 0 {size} {size}" width="{size}" height="{size}" role="img" aria-label="{escape(label)}" {FONT}>{"".join(parts)}</svg>'


def shape_2d(shape_name, size=110):
    """Draws 2-D geometrical shape."""
    parts = []
    pad = 12
    w = size - 2 * pad
    
    name_l = shape_name.lower().replace("-", "").replace(" ", "")
    if "circle" in name_l and "semi" not in name_l and "quarter" not in name_l:
        parts.append(f'<circle cx="{size/2}" cy="{size/2}" r="{w/2}" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>')
    elif "square" in name_l:
        parts.append(f'<rect x="{pad}" y="{pad}" width="{w}" height="{w}" rx="2" fill="#fed7aa" stroke="#ea580c" stroke-width="2"/>')
    elif "rectangle" in name_l:
        parts.append(f'<rect x="{pad}" y="{pad + 15}" width="{w}" height="{w - 30}" rx="2" fill="#bbf7d0" stroke="#16a34a" stroke-width="2"/>')
    elif "triangle" in name_l:
        p1 = f"{size/2},{pad}"
        p2 = f"{pad},{size - pad}"
        p3 = f"{size - pad},{size - pad}"
        parts.append(f'<polygon points="{p1} {p2} {p3}" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>')
    elif "semi" in name_l:
        path_d = f"M {pad} {size/2} A {w/2} {w/2} 0 0 1 {size - pad} {size/2} Z"
        parts.append(f'<path d="{path_d}" fill="#ddd6fe" stroke="#7c3aed" stroke-width="2"/>')
    elif "quarter" in name_l:
        path_d = f"M {pad} {pad} L {size - pad} {pad} A {w} {w} 0 0 1 {pad} {size - pad} Z"
        parts.append(f'<path d="{path_d}" fill="#fbcfe8" stroke="#db2777" stroke-width="2"/>')
    else:
        parts.append(f'<circle cx="{size/2}" cy="{size/2}" r="{w/2}" fill="#e2e8f0" stroke="#64748b" stroke-width="2"/>')
        
    label = f"2D Shape: {shape_name}"
    return f'<svg viewBox="0 0 {size} {size}" width="{size}" height="{size}" role="img" aria-label="{escape(label)}">{"".join(parts)}</svg>'
