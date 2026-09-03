#!/usr/bin/env python3
"""Render a GitHub contribution heatmap to a self-hosted SVG.

The public card services this README used to point at keep going offline
(the last one started answering 402), so the graph is generated here and
committed as a static file instead.
"""

import json
import os
import subprocess
import sys
from datetime import date, timedelta

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays { date contributionCount weekday }
        }
      }
    }
  }
}
"""

THEMES = {
    "dark": {
        "bg": "#0D1117",
        "border": "#30363D",
        "title": "#E6EDF3",
        "text": "#7D8590",
        "grid": "#21262D",
        "line": "#39D353",
        "fill": "#39D353",
    },
    "light": {
        "bg": "#FFFFFF",
        "border": "#D0D7DE",
        "title": "#1F2328",
        "text": "#59636E",
        "grid": "#D8DEE4",
        "line": "#2DA44E",
        "fill": "#2DA44E",
    },
}

PAD = 18
HEADER = 48          # title and summary lines
AXIS = 26            # room for the month labels under the plot
GUTTER = 34          # room for the y axis labels
PLOT_H = 132
PLOT_W = 726
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def fetch(login):
    out = subprocess.run(
        ["gh", "api", "graphql", "-f", "query=" + QUERY, "-F", "login=" + login],
        capture_output=True, text=True, check=True,
    ).stdout
    cal = json.loads(out)["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    return cal["totalContributions"], cal["weeks"]


def smooth_path(pts, y_top, y_bottom):
    """Catmull-Rom through the points, emitted as cubic beziers.

    Control points are clamped to the plot band. Weekly totals swing hard
    enough that an unclamped curve dips under the axis, which would draw a
    week of negative contributions.
    """
    if len(pts) < 2:
        return ""
    clamp = lambda y: min(max(y, y_top), y_bottom)
    d = f"M {pts[0][0]:.1f} {pts[0][1]:.1f}"
    for i in range(len(pts) - 1):
        p0 = pts[i - 1] if i else pts[0]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < len(pts) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, clamp(p1[1] + (p2[1] - p0[1]) / 6))
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, clamp(p2[1] - (p3[1] - p1[1]) / 6))
        d += (f" C {c1[0]:.1f} {c1[1]:.1f}, {c2[0]:.1f} {c2[1]:.1f},"
              f" {p2[0]:.1f} {p2[1]:.1f}")
    return d


def nice_max(value):
    """Round the axis top up to something a person would label."""
    if value <= 5:
        return 5
    for step in (5, 10, 25, 50, 100, 250, 500):
        if value <= step * 4:
            return -(-value // step) * step
    return -(-value // 1000) * 1000


def streaks(days):
    """Longest and current run of consecutive days with at least one contribution.

    The final day is skipped when it is empty: a day still in progress is not
    a broken streak.
    """
    longest = run = 0
    for d in days:
        run = run + 1 if d["contributionCount"] > 0 else 0
        longest = max(longest, run)
    tail = days[:-1] if days and days[-1]["contributionCount"] == 0 else days
    current = 0
    for d in reversed(tail):
        if d["contributionCount"] == 0:
            break
        current += 1
    return current, longest


def render(login, total, weeks, theme_name):
    t = THEMES[theme_name]
    days = [d for w in weeks for d in w["contributionDays"]]
    series = [(date.fromisoformat(w["contributionDays"][0]["date"]),
               sum(d["contributionCount"] for d in w["contributionDays"]))
              for w in weeks]

    width = PAD * 2 + GUTTER + PLOT_W
    height = PAD * 2 + HEADER + PLOT_H + AXIS
    px, py = PAD + GUTTER, PAD + HEADER
    top = nice_max(max((v for _, v in series), default=0))
    step = PLOT_W / max(1, len(series) - 1)
    pts = [(px + i * step, py + PLOT_H - (v / top) * PLOT_H)
           for i, (_, v) in enumerate(series)]

    uid = theme_name
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" '
        f'aria-label="{total} contributions by {login} over the last year">',
        f'<defs><linearGradient id="g-{uid}" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{t["fill"]}" stop-opacity="0.45"/>'
        f'<stop offset="1" stop-color="{t["fill"]}" stop-opacity="0"/>'
        f'</linearGradient></defs>',
        f'<rect width="{width}" height="{height}" rx="6" fill="{t["bg"]}" '
        f'stroke="{t["border"]}"/>',
        f'<g font-family="{FONT}">',
        f'<text x="{PAD}" y="{PAD + 14}" font-size="14" font-weight="600" '
        f'fill="{t["title"]}">{total} contributions in the last year</text>',
    ]

    current, longest = streaks(days)
    best = max((v for _, v in series), default=0)
    parts.append(
        f'<text x="{PAD}" y="{PAD + 33}" font-size="11" fill="{t["text"]}">'
        f'{current} day current streak &#183; {longest} day longest streak '
        f'&#183; {best} in the busiest week</text>')

    for n in range(5):
        y = py + PLOT_H - (n / 4) * PLOT_H
        parts.append(f'<line x1="{px}" y1="{y:.1f}" x2="{px + PLOT_W}" '
                     f'y2="{y:.1f}" stroke="{t["grid"]}" stroke-width="1"/>')
        parts.append(f'<text x="{px - 8}" y="{y + 3.5:.1f}" font-size="9" '
                     f'text-anchor="end" fill="{t["text"]}">{top * n // 4}</text>')

    line = smooth_path(pts, py, py + PLOT_H)
    parts.append(f'<path d="{line} L {pts[-1][0]:.1f} {py + PLOT_H} '
                 f'L {pts[0][0]:.1f} {py + PLOT_H} Z" fill="url(#g-{uid})"/>')
    parts.append(f'<path d="{line}" fill="none" stroke="{t["line"]}" '
                 f'stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')

    peak = max(range(len(series)), key=lambda i: series[i][1])
    parts.append(f'<circle cx="{pts[peak][0]:.1f}" cy="{pts[peak][1]:.1f}" r="3.5" '
                 f'fill="{t["line"]}" stroke="{t["bg"]}" stroke-width="2"/>')

    seen = set()
    for i, (first, _) in enumerate(series):
        if first.month not in seen and first.day <= 7 and i < len(series) - 1:
            seen.add(first.month)
            parts.append(f'<text x="{px + i * step:.1f}" y="{py + PLOT_H + 17}" '
                         f'font-size="10" text-anchor="middle" '
                         f'fill="{t["text"]}">{MONTH_NAMES[first.month - 1]}</text>')

    parts.append("</g></svg>")
    return "\n".join(parts) + "\n"


def main():
    login = sys.argv[1] if len(sys.argv) > 1 else "giaBaoJS"
    out_dir = sys.argv[2] if len(sys.argv) > 2 else "assets"
    total, weeks = fetch(login)
    os.makedirs(out_dir, exist_ok=True)
    for name in THEMES:
        path = os.path.join(out_dir, f"activity-graph-{name}.svg")
        with open(path, "w") as f:
            f.write(render(login, total, weeks, name))
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
