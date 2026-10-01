"""Render profile cards from public repositories. Python standard library only."""

from collections import Counter
from datetime import datetime, timezone
from html import escape
import json
import os
from pathlib import Path
import re
from urllib.request import Request, urlopen


USER = os.environ.get("PROFILE_USER", "Rudrarauttt")
if not re.fullmatch(r"[A-Za-z0-9-]+", USER):
    raise ValueError("Invalid GitHub username")
OUT = Path("dist")
COLORS = {"Python": "#f5cc62", "C++": "#7aa2f7", "C": "#a3acc2", "Rust": "#f49b77", "TypeScript": "#60a5fa", "JavaScript": "#f7df6b", "Dockerfile": "#5ed7f0", "Shell": "#a6da95"}


def api(path):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": f"{USER}-profile", "X-GitHub-Api-Version": "2022-11-28"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urlopen(Request(f"https://api.github.com{path}", headers=headers), timeout=30) as response:
        return json.load(response)


def collect():
    repos = []
    page = 1
    while True:
        batch = api(f"/users/{USER}/repos?type=owner&sort=pushed&direction=desc&per_page=100&page={page}")
        # Explicit visibility guard, even if a developer runs with a personal token.
        repos.extend(r for r in batch if not r["private"] and not r["fork"] and not r["archived"] and r["name"].lower() != USER.lower() and r["size"] > 0)
        if len(batch) < 100:
            break
        page += 1
    repos.sort(key=lambda r: r["pushed_at"], reverse=True)
    languages = Counter()
    for repo in repos:
        languages.update(api(f'/repos/{USER}/{repo["name"]}/languages'))
    return repos, languages


def card(repos, languages, dark):
    bg, surface, border, ink, muted, accent = (
        ("#0d1117", "#101822", "#263445", "#edf4ff", "#9baec4", "#5eead4") if dark else
        ("#f8fafc", "#ffffff", "#dce4ed", "#172537", "#52657c", "#087f72")
    )
    date = datetime.now(timezone.utc).strftime("%d %b %Y")
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="430" viewBox="0 0 960 430" role="img" aria-labelledby="title desc"><title id="title">Public workbench for {escape(USER)}</title><desc id="desc">Recently pushed public repositories and source language distribution. Updated {date} UTC. Language sizes are code bytes, not proficiency.</desc><rect x=".5" y=".5" width="959" height="429" rx="18" fill="{bg}" stroke="{border}"/><g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Arial,sans-serif">']

    def text(x, y, value, size=16, fill=ink, weight=400, extra=""):
        parts.append(f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-weight="{weight}" {extra}>{escape(str(value))}</text>')

    text(30, 37, "PUBLIC BUILD LOG", 13, accent, 650, 'letter-spacing="2"')
    text(930, 37, f"UPDATED {date.upper()} UTC", 11, muted, 500, 'text-anchor="end"')
    text(30, 75, "Latest on the workbench", 26, ink, 650)
    for i, repo in enumerate(repos[:3]):
        x = 30 + i * 308
        parts.append(f'<rect x="{x}" y="96" width="288" height="127" rx="10" fill="{surface}" stroke="{border}"/>')
        name = repo["name"]
        # Two deliberate lines keep repository names readable at profile width.
        lines = [name] if len(name) <= 26 else [name[:26], name[26:49] + ("…" if len(name) > 49 else "")]
        text(x + 16, 123, f"0{i+1} / PUBLIC REPOSITORY", 10, muted, 600, 'letter-spacing="1"')
        for j, line in enumerate(lines):
            text(x + 16, 149 + 19 * j, line, 15, ink, 600)
        pushed = repo["pushed_at"][:10]
        text(x + 16, 202, f'{repo.get("language") or "Project notes"} · pushed {pushed}', 11, accent)
    if not repos:
        text(30, 150, "Public projects will appear here as they are published.", 16, muted)

    text(30, 264, "PUBLIC CODE MIX", 12, accent, 650, 'letter-spacing="1.5"')
    text(930, 264, "Source bytes across public, original repositories", 11, muted, 400, 'text-anchor="end"')
    total = sum(languages.values())
    top = languages.most_common(5)
    if len(languages) > 5:
        top.append(("Other", total - sum(n for _, n in top)))
    x = 30
    for index, (language, count) in enumerate(top):
        width = 900 * count / total
        color = COLORS.get(language, "#b69df5")
        parts.append(f'<rect x="{x:.2f}" y="282" width="{width:.2f}" height="12" fill="{color}"/>')
        x += width
        col, row = index % 3, index // 3
        lx, ly = 30 + col * 308, 321 + row * 24
        parts.append(f'<circle cx="{lx + 4}" cy="{ly - 4}" r="4" fill="{color}"/>')
        text(lx + 16, ly, f"{language}  {count / total:.1%}", 12, muted)
    if not total:
        text(30, 321, "Language data will appear when public code is available.", 13, muted)
    parts.append(f'<path d="M30 372H930" stroke="{border}"/>')
    text(30, 402, "BUILD → TEST → LEARN → REPEAT", 11, muted, 600, 'letter-spacing="1.2"')
    text(930, 402, "Refreshed daily with GitHub Actions", 11, muted, 400, 'text-anchor="end"')
    parts.append("</g></svg>")
    return "".join(parts)


if __name__ == "__main__":
    repos, languages = collect()
    OUT.mkdir(exist_ok=True)
    for dark in (False, True):
        target = OUT / f'activity-{"dark" if dark else "light"}.svg'
        target.write_text(card(repos, languages, dark))
        print(f"Rendered {target} from {len(repos)} public repositories")
