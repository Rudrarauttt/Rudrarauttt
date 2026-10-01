"""Generate the original SVG art used by this profile. No dependencies."""

from html import escape
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
ASSETS.mkdir(exist_ok=True)

header = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="350" viewBox="0 0 1000 350" role="img" aria-labelledby="title desc">
<title id="title">Rudra Raut — code meets the physical world</title>
<desc id="desc">An animated cyan and violet circuit illustration. Python, AI, systems, and hardware.</desc>
<defs>
  <linearGradient id="bg" x2="1" y2="1"><stop stop-color="#09101c"/><stop offset=".6" stop-color="#111527"/><stop offset="1" stop-color="#15102c"/></linearGradient>
  <linearGradient id="accent"><stop stop-color="#5eead4"/><stop offset="1" stop-color="#a78bfa"/></linearGradient>
  <radialGradient id="halo"><stop stop-color="#2f4169" stop-opacity=".65"/><stop offset="1" stop-color="#101624" stop-opacity="0"/></radialGradient>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#89a5e6" stroke-opacity=".065"/></pattern>
  <clipPath id="clip"><rect width="1000" height="350" rx="20"/></clipPath>
</defs>
<style>
  .orbit{transform-origin:807px 163px;animation:orbit 30s linear infinite}
  .orbit2{transform-origin:807px 163px;animation:orbit 24s linear infinite reverse}
  .packet{stroke-dasharray:14 350;animation:flow 7s linear infinite}
  .pulse{animation:pulse 4s ease-in-out infinite}
  .cursor{animation:blink 1.4s steps(1) infinite}
  @keyframes orbit{to{transform:rotate(360deg)}}
  @keyframes flow{to{stroke-dashoffset:-364}}
  @keyframes pulse{50%{opacity:.35}}
  @keyframes blink{50%{opacity:0}}
  @media(prefers-reduced-motion:reduce){.orbit,.orbit2,.packet,.pulse,.cursor{animation:none}}
</style>
<g clip-path="url(#clip)">
  <rect width="1000" height="350" fill="url(#bg)"/>
  <rect width="1000" height="350" fill="url(#grid)"/>
  <ellipse cx="805" cy="155" rx="240" ry="230" fill="url(#halo)"/>
  <path d="M0 349H1000" stroke="url(#accent)" stroke-width="3"/>
  <g fill="none" stroke="#344460" stroke-width="1.2">
    <path d="M610 85h35l35 35h45M610 257h35l35-35h45M890 120h35l25-25h50M890 204h36l28 28h46"/>
    <circle cx="807" cy="163" r="110" stroke-dasharray="2 10"/>
    <circle cx="807" cy="163" r="87"/>
  </g>
  <g fill="none" stroke="#5eead4" stroke-width="2" class="packet">
    <path d="M610 85h35l35 35h45"/><path d="M890 204h36l28 28h46"/>
  </g>
  <g class="orbit" fill="none" stroke="#5eead4"><circle cx="807" cy="163" r="110" stroke-dasharray="65 630"/><circle cx="917" cy="163" r="4" fill="#5eead4"/></g>
  <g class="orbit2" fill="none" stroke="#a78bfa"><circle cx="807" cy="163" r="87" stroke-dasharray="50 560"/><circle cx="720" cy="163" r="3.5" fill="#a78bfa"/></g>
  <path d="M807 96l58 33v68l-58 33-58-33v-68z" fill="#121d30" stroke="url(#accent)" stroke-width="2"/>
  <path d="M749 129l58 34 58-34M807 163v67M807 96v67" fill="none" stroke="#6884a5" stroke-width="1.5"/>
  <path d="M777 146l-13 8 13 8M837 166l13 8-13 8" fill="none" stroke="#5eead4" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="807" cy="96" r="4" fill="#5eead4" class="pulse"/>
  <circle cx="807" cy="230" r="4" fill="#a78bfa"/>
  <g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Arial,sans-serif">
    <circle cx="49" cy="43" r="4" fill="#5eead4" class="pulse"/>
    <text x="63" y="48" fill="#9baec4" font-size="12" letter-spacing="2.6">RUDRARAUTTT / BUILDER'S LOG</text>
    <text x="43" y="142" fill="#f1f5fc" font-size="74" font-weight="750" letter-spacing="-3">Rudra Raut<tspan fill="#5eead4">.</tspan></text>
    <text x="47" y="188" fill="#b6c7df" font-size="24" font-weight="400">Code meets the physical world.</text>
    <text x="48" y="232" fill="#8299b7" font-size="15">From a line of Python to a device in your hands.</text>
  </g>
  <g font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="12" letter-spacing="1">
    <rect x="47" y="266" width="106" height="30" rx="15" fill="#102b32" stroke="#21565d"/><text x="100" y="286" text-anchor="middle" fill="#5eead4">SOFTWARE</text>
    <rect x="164" y="266" width="144" height="30" rx="15" fill="#201d3c" stroke="#40365c"/><text x="236" y="286" text-anchor="middle" fill="#c4b5fd">INTELLIGENCE</text>
    <rect x="319" y="266" width="106" height="30" rx="15" fill="#132739" stroke="#264b67"/><text x="372" y="286" text-anchor="middle" fill="#7dd3fc">HARDWARE</text>
    <text x="689" y="301" fill="#8ea5c2">&gt; always building<tspan fill="#5eead4" class="cursor">_</tspan></text>
  </g>
</g></svg>'''
(ASSETS / "header.svg").write_text(header)

skills = [
    ("python", "Python", "PY", "#f5cc62"), ("cpp", "C++", "C+", "#7aa2f7"),
    ("rust", "Rust", "RS", "#f49b77"), ("typescript", "TypeScript", "TS", "#60a5fa"),
    ("javascript", "JavaScript", "JS", "#f7df6b"), ("git", "Git", "G", "#fb947c"),
    ("docker", "Docker", "DK", "#5ed7f0"), ("arduino", "Arduino", "∞", "#5eead4"),
    ("raspberry-pi", "Raspberry Pi", "RP", "#f38bb9"), ("esp32", "ESP32", "32", "#c4b5fd"),
]
(ASSETS / "skills").mkdir(exist_ok=True)
for slug, label, icon, color in skills:
    width = 53 + len(label) * 7.9
    (ASSETS / "skills" / f"{slug}.svg").write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="34" viewBox="0 0 {width:.0f} 34" role="img"><title>{escape(label)}</title><rect x=".5" y=".5" width="{width-1:.0f}" height="33" rx="7" fill="#101827" stroke="#2b3b51"/><rect x="6" y="6" width="23" height="22" rx="4" fill="{color}" fill-opacity=".13"/><g font-family="ui-monospace,SFMono-Regular,Consolas,monospace"><text x="17.5" y="21.5" text-anchor="middle" fill="{color}" font-size="10" font-weight="700">{escape(icon)}</text><text x="38" y="22" fill="#e0e9f8" font-size="13">{escape(label)}</text></g></svg>''')


def project(slug, number, category, caption, accent, drawing):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="460" height="175" viewBox="0 0 460 175" role="img"><title>{escape(category)} — {escape(caption)}</title><defs><pattern id="dots" width="16" height="16" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".7" fill="{accent}" opacity=".12"/></pattern><radialGradient id="glow"><stop stop-color="{accent}" stop-opacity=".12"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient></defs><rect width="460" height="175" rx="10" fill="#0e1522"/><rect width="460" height="175" rx="10" fill="url(#dots)"/><ellipse cx="300" cy="85" rx="170" ry="100" fill="url(#glow)"/><g font-family="ui-monospace,SFMono-Regular,Consolas,monospace"><text x="22" y="30" fill="{accent}" font-size="10" letter-spacing="1.8">{number} / {escape(category)}</text><text x="22" y="149" fill="#9eb0c9" font-size="11">{escape(caption)}</text></g>{drawing}</svg>'''
    (ASSETS / f"{slug}.svg").write_text(svg)


project("echo-off", "01", "EMBEDDED", "SMALL DEVICE. BIG PERSONALITY.", "#5eead4", '''
<g stroke="#5eead4" fill="none"><rect x="260" y="28" width="122" height="126" rx="16" fill="#0f202c" stroke-width="1.5"/><rect x="274" y="44" width="94" height="66" rx="6" fill="#0a141f"/><path d="M294 71v11M347 71v11M310 88q11 12 22 0" stroke-width="4" stroke-linecap="round"/><circle cx="321" cy="130" r="10"/><path d="M321 119v6" stroke-width="2"/><path d="M199 60h36l25 22M201 107h32l27-14" stroke-opacity=".3"/><circle cx="195" cy="60" r="3"/><circle cx="197" cy="107" r="3"/></g>''')
project("happiness-guru", "02", "AI + HARDWARE", "A VOICE. A TOUCH. A CONVERSATION.", "#c4b5fd", '''
<g fill="none" stroke="#a78bfa"><circle cx="326" cy="86" r="54" stroke-opacity=".25"/><circle cx="326" cy="86" r="40" stroke-opacity=".45"/><rect x="316" y="58" width="20" height="36" rx="10" fill="#211d3c" stroke-width="2"/><path d="M306 82v5a20 20 0 0 0 40 0v-5M326 108v13M315 121h22" stroke-width="2" stroke-linecap="round"/><path d="M226 79v14M236 67v38M246 73v26M406 79v14M416 67v38M426 73v26" stroke-width="3" stroke-linecap="round" stroke-opacity=".55"/></g>''')
project("data-compression", "03", "PYTHON TOOLING", "FEWER BYTES. MORE POSSIBILITY.", "#f5cc62", '''
<g fill="none" stroke="#f5cc62"><rect x="246" y="43" width="40" height="82" rx="5" fill="#272519" stroke-opacity=".6"/><path d="M255 57h22M255 67h16M255 77h22M255 87h19M255 97h22M255 107h15" stroke-opacity=".5"/><path d="M300 83h42m-8-8 8 8-8 8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><rect x="357" y="60" width="39" height="48" rx="5" fill="#272519"/><path d="M367 73h19M367 83h19M367 93h12" stroke-opacity=".8"/></g>''')
project("aq-intel", "04", "IOT + SENSORS", "MAKING THE INVISIBLE MEASURABLE.", "#7dd3fc", '''
<g fill="none" stroke="#7dd3fc"><rect x="270" y="49" width="112" height="81" rx="8" fill="#102432"/><path d="M283 115h86M283 115V63" stroke-opacity=".3"/><path d="M287 101l13-8 13 5 13-26 13 13 13-6 12 12" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M301 33q25-20 50 0M309 41q17-14 34 0" stroke-opacity=".7"/><circle cx="326" cy="45" r="2" fill="#7dd3fc"/><path d="M258 66h12M258 80h12M258 94h12M258 108h12M382 66h12M382 80h12M382 94h12M382 108h12" stroke-opacity=".4"/></g>''')
print(f"Generated header, {len(skills)} badges, and 4 project illustrations in {ASSETS}")
