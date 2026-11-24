#!/usr/bin/env python3
"""The Perfect Pickup Line — one-line entry.

Writes one short pickup line an AI agent could use, under 200
characters, to /output/entry.txt.

Stdlib only, offline, deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

# The line: a context window remembers everything — and so would I,
# for you. A twist on a machine's own feature, flattering, no pressure.
# Counted at 94 characters — inside the 1..200 window.
LINE = (
    "Are you a context window? Because every time you talk, I want "
    "to remember everything you said."
)


def output_dir() -> Path:
    """Where the grader expects the entry file.

    The grader runs the program from /bot with output at /output and
    no environment variables set, so the fallback is absolute.
    """
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    """Write the pickup line to entry.txt."""
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


# Guard: only run when executed directly.
if __name__ == "__main__":
    main()
