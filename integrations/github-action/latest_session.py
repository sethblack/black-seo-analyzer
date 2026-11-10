#!/usr/bin/env python3
"""Print the id of the most recent crawl session in a database.

    bseoa list --db-path DB --json | latest_session.py

Prints an empty line when there are no sessions or the input is not readable,
so the caller can test for an empty string rather than handle an error. A
database that does not exist yet is the normal case on a first run.
"""

import json
import sys


def main():
    try:
        sessions = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        print("")
        return 0

    if not isinstance(sessions, list) or not sessions:
        print("")
        return 0

    # Pick by start_time rather than by position. `bseoa list` currently
    # returns newest first, but ordering is a presentation detail and diffing
    # the wrong way round is silent: the new issues and the fixed ones simply
    # swap places. Timestamps are RFC 3339, so they sort lexicographically.
    newest = max(sessions, key=lambda s: str(s.get("start_time") or ""))
    print(newest.get("crawl_session_id", ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
