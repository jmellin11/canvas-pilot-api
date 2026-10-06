"""Core Canvas client utilities.

This module keeps the original Canvas Pilot architecture shape while making the
model/backend integration explicit and API-driven instead of agent-driven.
"""

from __future__ import annotations

import os
from typing import Any, Dict, Optional


class CanvasClient:
    """Thin canvas client shell. Replace with real Canvas API logic as needed."""

    def __init__(self, base_url: Optional[str] = None):
        self.base_url = (base_url or os.getenv("CANVAS_BASE") or "").rstrip("/")

    def get_courses(self) -> list[dict[str, Any]]:
        """Return a list of Canvas courses. Placeholder for actual implementation."""
        return []

    def get_assignments(self, course_id: str) -> list[dict[str, Any]]:
        """Return assignments for a course. Placeholder for actual implementation."""
        return []
