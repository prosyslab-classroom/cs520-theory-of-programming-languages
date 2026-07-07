#!/usr/bin/env python3
"""Regenerate README.eng.md from README.md using the local Codex CLI."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from textwrap import dedent


def build_prompt() -> str:
    return dedent(
        """
        Translate README.md into README.eng.md.
        """
    ).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo",
        type=Path,
        default=Path.cwd(),
        help="Repository root containing README.md",
    )
    args = parser.parse_args()

    repo = args.repo.resolve()
    if not (repo / "README.md").exists():
        print(f"README.md not found under {repo}", file=sys.stderr)
        return 1

    prompt = build_prompt()
    cmd = ["codex", "exec", "-C", str(repo), "-s", "workspace-write", prompt]
    completed = subprocess.run(cmd)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
