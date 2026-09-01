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
        "empty": "#161B22",
        "scale": ["#0E4429", "#006D32", "#26A641", "#39D353"],
    },
    "light": {
        "bg": "#FFFFFF",
        "border": "#D0D7DE",
        "title": "#1F2328",
        "text": "#59636E",
        "empty": "#EBEDF0",
        "scale": ["#9BE9A8", "#40C463", "#30A14E", "#216E39"],
    },
}

CELL = 11
GAP = 3
STRIDE = CELL + GAP
PAD = 16
GUTTER = 28          # room for the Mon/Wed/Fri labels
HEADER = 46          # title line
MONTHS = 16          # month labels above the grid
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


def bucket(count, thresholds):
    for i, t in enumerate(thresholds):
        if count <= t:
            return i
    return len(thresholds) - 1


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
    counts = sorted(c for c in (d["contributionCount"] for d in days) if c > 0)
    # Quartiles over the non-empty days, so a handful of huge days cannot
    # flatten every ordinary one into the palest colour.
    if counts:
        q = [counts[min(len(counts) - 1, (len(counts) * n) // 4)] for n in (1, 2, 3)]
        thresholds = [q[0], q[1], q[2], counts[-1]]
    else:
        thresholds = [0, 0, 0, 0]

    grid_w = len(weeks) * STRIDE - GAP
    width = PAD * 2 + GUTTER + grid_w
    height = PAD * 2 + HEADER + MONTHS + 7 * STRIDE - GAP + 26
    gx = PAD + GUTTER
    gy = PAD + HEADER + MONTHS

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" '
        f'aria-label="{total} contributions by {login} in the last year">',
        f'<rect width="{width}" height="{height}" rx="6" fill="{t["bg"]}" '
        f'stroke="{t["border"]}"/>',
        f'<g font-family="{FONT}">',
        f'<text x="{PAD}" y="{PAD + 14}" font-size="14" font-weight="600" '
        f'fill="{t["title"]}">{total} contributions in the last year</text>',
    ]

    current, longest = streaks(days)
    best = max((d["contributionCount"] for d in days), default=0)
    summary = (f"{current} day current streak &#183; {longest} day longest streak "
               f"&#183; {best} in a single day")
    parts.append(f'<text x="{PAD}" y="{PAD + 33}" font-size="11" '
                 f'fill="{t["text"]}">{summary}</text>')

    # Month labels, printed once per month above the first week that starts it.
    seen = set()
    for i, week in enumerate(weeks):
        first = date.fromisoformat(week["contributionDays"][0]["date"])
        if first.month not in seen and first.day <= 7 and i < len(weeks) - 1:
            seen.add(first.month)
            parts.append(f'<text x="{gx + i * STRIDE}" y="{gy - 6}" font-size="10" '
                         f'fill="{t["text"]}">{MONTH_NAMES[first.month - 1]}</text>')

    for row, label in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        parts.append(f'<text x="{PAD}" y="{gy + row * STRIDE + 9}" font-size="9" '
                     f'fill="{t["text"]}">{label}</text>')

    for i, week in enumerate(weeks):
        for day in week["contributionDays"]:
            n = day["contributionCount"]
            fill = t["empty"] if n == 0 else t["scale"][bucket(n, thresholds)]
            x = gx + i * STRIDE
            y = gy + day["weekday"] * STRIDE
            parts.append(
                f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" '
                f'fill="{fill}"><title>{n} on {day["date"]}</title></rect>'
            )

    ly = gy + 7 * STRIDE + 10
    lx = width - PAD - 5 * STRIDE - 62
    parts.append(f'<text x="{lx}" y="{ly + 9}" font-size="10" '
                 f'fill="{t["text"]}">Less</text>')
    for i, fill in enumerate([t["empty"]] + t["scale"]):
        parts.append(f'<rect x="{lx + 27 + i * STRIDE}" y="{ly}" width="{CELL}" '
                     f'height="{CELL}" rx="2" fill="{fill}"/>')
    parts.append(f'<text x="{lx + 27 + 5 * STRIDE}" y="{ly + 9}" font-size="10" '
                 f'fill="{t["text"]}">More</text>')

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
