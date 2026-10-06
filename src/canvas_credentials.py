"""Canvas credential utilities.

This is intentionally small and local-first. The original repo stores all student
and course-specific auth in local files and gitignored directories.
"""

from __future__ import annotations

import os
from pathlib import Path


def local_state_dir() -> Path:
    return Path(__file__).resolve().parent.parent / ".cookies"


def load_canvas_base_url() -> str:
    return os.getenv("CANVAS_BASE", "")


def ensure_local_dirs() -> None:
    Path(__file__).resolve().parent.parent.joinpath(".cookies").mkdir(exist_ok=True)
    Path(__file__).resolve().parent.parent.joinpath("runs").mkdir(exist_ok=True)
    Path(__file__).resolve().parent.parent.joinpath("sources").mkdir(exist_ok=True)
