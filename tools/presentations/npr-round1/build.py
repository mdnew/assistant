#!/usr/bin/env python3
"""Generate review.html (the shareable scrolling page) from index.html.

index.html is the only source of truth. Run this after editing it:

    python3 build.py
"""
import re, html, pathlib

src = pathlib.Path("index.html").read_text(encoding="utf-8")
style = re.search(r"<style>(.*?)</style>", src, re.S).group(1)

slides = []
for m in re.finditer(r'<section class="slide[^"]*"([^>]*)>(.*?)</section>', src, re.S):
    attrs, inner = m.group(1), m.group(2)
    def a(k):
        g = re.search(k + r'="([^"]*)"', attrs)
        return g.group(1) if g else ""
    frame = re.search(r'(<div class="frame.*?)\s*<div class="slide-notes">', inner, re.S)
    notes = re.search(r'<div class="slide-notes">(.*?)</div>\s*$', inner, re.S)
    slides.append({
        "who": a("data-who"), "sec": a("data-sec"), "time": a("data-time"),
        "frame": frame.group(1).strip() if frame else inner.strip(),
        "notes": notes.group(1).strip() if notes else "",
    })

def mmss(t):
    m, s = t.split(":"); return int(m) * 60 + int(s)
run, rows = 0, []
for i, sl in enumerate(slides, 1):
    run += mmss(sl["time"])
    rows.append(f'<tr><td>{i}</td><td class="who">{sl["who"]}</td><td class="sec">{sl["sec"]}</td>'
                f'<td class="t">{sl["time"]}</td><td class="t">{run//60}:{run%60:02d}</td></tr>')
rows.append(f'<tr class="tot"><td></td><td class="who">&nbsp;</td>'
            f'<td class="sec">Content total, leaving {(900-run)//60}:{(900-run)%60:02d} buffer</td>'
            f'<td class="t">{run//60}:{run%60:02d}</td><td class="t">15:00</td></tr>')

blocks = "\n".join(
    f'''  <section class="block">
    <div class="bar"><span class="num">{i:02d}</span><span class="who-tag">{sl["who"]}</span>
      <span class="sec-tag">{sl["sec"]}</span><span class="time-tag">{sl["time"]}</span></div>
    {sl["frame"]}
    <div class="notes"><span class="lab">Talk track</span>
{sl["notes"]}
    </div>
  </section>''' for i, sl in enumerate(slides, 1))

OVERRIDE = """
  /* ---- review page: same slides, laid out to scroll ---- */
  html, body { height:auto; overflow:auto; background:#F4F3F8; }
  @media (prefers-color-scheme: dark) { html, body { background:#121218; } }
  .stage, .hud, .notes-panel, .grid-ov { display:none !important; }
  .wrap { max-width:1180px; margin:0 auto; padding:56px 28px 100px;
    display:flex; flex-direction:column; gap:40px; }
  .slide, .slide.is-active { display:block; }
  .frame { width:100% !important; border-radius:3px;
    box-shadow:0 0 0 1px rgba(26,26,34,.10), 0 1px 2px rgba(26,26,34,.05), 0 12px 32px -8px rgba(26,26,34,.16); }
  .masthead { display:flex; flex-direction:column; gap:13px; }
  .kicker { font-size:11.5px; letter-spacing:.16em; text-transform:uppercase; color:#6D4DF2; font-weight:500; }
  h1.pg { margin:0; font-size:clamp(32px,5.2vw,50px); font-weight:300; letter-spacing:-.015em;
    line-height:1.05; color:#1A1A22; }
  .standfirst { margin:0; max-width:64ch; font-size:16px; line-height:1.62; color:#62626E; }
  .ros { background:#FFF; border:1px solid #DDDBE6; border-radius:5px; overflow:hidden; }
  .ros h2 { margin:0; padding:18px 22px 14px; font-size:15px; font-weight:600; color:#1A1A22; }
  table.ros-t { width:100%; border-collapse:collapse; font-variant-numeric:tabular-nums; }
  table.ros-t th { text-align:left; font-size:10.5px; letter-spacing:.1em; text-transform:uppercase;
    color:#62626E; font-weight:500; padding:8px 14px; border-top:1px solid #DDDBE6;
    border-bottom:1px solid #DDDBE6; background:#EFEBFE; }
  table.ros-t td { padding:9px 14px; font-size:13.5px; border-bottom:1px solid #DDDBE6; color:#62626E; }
  table.ros-t td.who { font-weight:600; color:#1A1A22; width:15%; }
  table.ros-t td.sec { color:#1A1A22; width:38%; }
  table.ros-t td.t { font-family:ui-monospace,monospace; font-size:12.5px; width:12%; white-space:nowrap; }
  table.ros-t tr.tot td { font-weight:600; color:#1A1A22; border-bottom:none; background:rgba(109,77,242,.05); }
  .block { display:flex; flex-direction:column; gap:14px; }
  .bar { display:flex; flex-wrap:wrap; align-items:baseline; gap:10px; }
  .num { font-family:ui-monospace,monospace; font-size:12px; color:#62626E; }
  .who-tag { font-size:11px; letter-spacing:.09em; text-transform:uppercase; font-weight:600;
    padding:4px 9px; border-radius:3px; background:#EFEBFE; color:#6D4DF2; }
  .sec-tag { font-size:15px; font-weight:500; color:#1A1A22; }
  .time-tag { font-family:ui-monospace,monospace; font-size:12px; color:#62626E; margin-left:auto; }
  .notes { background:#FFF; border:1px solid #DDDBE6; border-left:3px solid #6D4DF2; border-radius:4px;
    padding:16px 20px; display:flex; flex-direction:column; gap:9px; }
  .notes .lab { font-size:10.5px; letter-spacing:.13em; text-transform:uppercase; font-weight:600; color:#6D4DF2; }
  .notes p { margin:0; font-size:14px; line-height:1.62; color:#62626E; max-width:76ch; }
  .notes p b { color:#1A1A22; font-weight:500; }
  @media (prefers-color-scheme: dark) {
    h1.pg, .sec-tag, table.ros-t td.who, table.ros-t td.sec, .notes p b { color:#ECEBF2; }
    .standfirst, .num, .time-tag, table.ros-t td, .notes p { color:#9895A4; }
    .ros, .notes { background:#1B1B24; border-color:#2C2B37; }
    table.ros-t th { background:#221E3A; color:#9895A4; border-color:#2C2B37; }
    table.ros-t td { border-color:#2C2B37; }
    .who-tag { background:#221E3A; color:#A28FFF; }
  }
  @media (max-width:820px) { .frame { aspect-ratio:auto; } }
"""

out = f"""<title>NPR Pitch Deck</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500;600&display=swap">
<style>{style}{OVERRIDE}</style>

<div class="wrap">
  <header class="masthead">
    <span class="kicker">Uptech Studio &middot; NPR Round 1</span>
    <h1 class="pg">Fifteen-minute pitch deck</h1>
    <p class="standfirst">
      {len(slides)} slides across four speaking blocks. Presentation density, not proposal density: the
      written response carries the detail, so these exist to be talked over. Generated from the
      presentable deck, so this page and the live deck never drift.
    </p>
  </header>

  <section class="ros">
    <h2>Run of show</h2>
    <table class="ros-t">
      <thead><tr><th>Slide</th><th>Speaker</th><th>Section</th><th>Target</th><th>Running</th></tr></thead>
      <tbody>
{chr(10).join("        " + r for r in rows)}
      </tbody>
    </table>
  </section>

{blocks}
</div>
"""
pathlib.Path("review.html").write_text(out, encoding="utf-8")
print(f"review.html written: {len(slides)} slides, {run//60}:{run%60:02d} of content")
