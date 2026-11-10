#!/usr/bin/env python3
"""Render a bseoa report as a GitHub job summary.

    summarize.py <report.json> <issues|diff> <url>

Reads either `bseoa issues --json` (a list of issues) or `bseoa diff --json`
(new, fixed and persisting counts) and writes Markdown to stdout.
"""

import html
import json
import sys
from collections import Counter

# The summary uses emoji for severity. A Windows runner's console defaults to
# cp1252, where encoding one raises and takes the whole step down with it.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Most severe first, so the table reads top-down in the order you would fix.
SEVERITY_ORDER = ["critical", "high", "medium", "low"]
SEVERITY_ICON = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "⚪"}

# A job summary is capped at 1 MiB and nobody reads a thousand rows anyway.
MAX_ROWS = 25


def severity_rank(issue):
    try:
        return SEVERITY_ORDER.index(issue.get("severity", "low"))
    except ValueError:
        return len(SEVERITY_ORDER)


def cell(text, limit=90):
    """One table cell: escaped, pipe-safe and short enough to read."""
    text = " ".join(str(text or "").split())
    if len(text) > limit:
        text = text[: limit - 1] + "…"
    return html.escape(text, quote=False).replace("|", "\\|")


def counts_line(issues):
    counts = Counter(i.get("severity", "low") for i in issues)
    parts = [
        f"{SEVERITY_ICON.get(s, '')} {counts[s]} {s}"
        for s in SEVERITY_ORDER
        if counts[s]
    ]
    return " · ".join(parts) if parts else "none"


def issue_table(issues, out):
    ranked = sorted(issues, key=severity_rank)
    out.append("| | Issue | Page |")
    out.append("|---|---|---|")
    for issue in ranked[:MAX_ROWS]:
        severity = issue.get("severity", "low")
        message = issue.get("message") or issue.get("key", "")
        docs = issue.get("docs_url")
        label = f"[{cell(message)}]({docs})" if docs else cell(message)
        out.append(f"| {SEVERITY_ICON.get(severity, '')} | {label} | {cell(issue.get('url', ''), 60)} |")
    if len(ranked) > MAX_ROWS:
        out.append(f"| | _and {len(ranked) - MAX_ROWS} more_ | |")


def render_issues(report, url, out):
    out.append(f"## Black SEO Analyzer — {cell(url, 120)}")
    out.append("")
    if not report:
        out.append("No issues found.")
        return
    out.append(f"**{len(report)} issues:** {counts_line(report)}")
    out.append("")
    issue_table(report, out)


def render_diff(report, url, out):
    new = report.get("new_issues", [])
    fixed = report.get("fixed_issues", [])
    persisting = report.get("persisting", 0)

    out.append(f"## Black SEO Analyzer — {cell(url, 120)}")
    out.append("")
    out.append("| | Count |")
    out.append("|---|---|")
    out.append(f"| 🆕 New | {len(new)} |")
    out.append(f"| ✅ Fixed | {len(fixed)} |")
    out.append(f"| ➖ Unchanged | {persisting} |")
    out.append("")

    if new:
        out.append(f"### New issues — {counts_line(new)}")
        out.append("")
        issue_table(new, out)
    else:
        out.append("### No new issues")
        out.append("")
        out.append("This change introduced nothing new.")

    if fixed:
        out.append("")
        plural = "issue" if len(fixed) == 1 else "issues"
        out.append(f"<details><summary>{len(fixed)} {plural} fixed</summary>")
        out.append("")
        issue_table(fixed, out)
        out.append("")
        out.append("</details>")


def main():
    if len(sys.argv) < 4:
        print("usage: summarize.py <report.json> <issues|diff> <url>", file=sys.stderr)
        return 2

    path, mode, url = sys.argv[1], sys.argv[2], sys.argv[3]
    try:
        with open(path, encoding="utf-8") as handle:
            report = json.load(handle)
    except (OSError, json.JSONDecodeError) as error:
        # A summary is a convenience. Never fail the job over one.
        print(f"Could not read the Black SEO Analyzer report: {error}")
        return 0

    out = []
    if mode == "diff" and isinstance(report, dict):
        render_diff(report, url, out)
    elif isinstance(report, list):
        render_issues(report, url, out)
    else:
        print("The report was not in a shape this summary understands.")
        return 0

    out.append("")
    out.append(
        "<sub>Reported by "
        "[Black SEO Analyzer](https://www.blackseoanalyzer.com/)</sub>"
    )
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
