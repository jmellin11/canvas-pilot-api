"""Anthropic API bridge for the Canvas Pilot workflow.

This module mirrors the original project structure while replacing direct agent
model calls with a clean Python API integration.
"""

from __future__ import annotations

import json
import os
from typing import Optional

from anthropic import Anthropic


class CanvasLLMBridge:
    def __init__(self):
        api_key = os.getenv("CLAUDE_API_KEY")
        if not api_key:
            raise ValueError("CLAUDE_API_KEY not set in .env")

        self.client = Anthropic(api_key=api_key)
        self.model = os.getenv("CLAUDE_MODEL", "claude-3-5-sonnet-20241022")

    def health_check(self) -> bool:
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=32,
                messages=[{"role": "user", "content": "Reply with OK only."}],
            )
            return bool(response.content and response.content[0].text.strip().upper() == "OK")
        except Exception:
            return False

    def analyze_assignment(self, assignment_spec: str, course_context: Optional[str] = None) -> str:
        prompt = f"""Course context:\n{course_context or 'None'}\n\nAssignment:\n{assignment_spec}\n\nReturn a structured analysis with: objective, required artifacts, constraints, and a short implementation plan."""
        system = "You are a careful assignment analysis helper for a local-first Canvas workflow. Be precise, structured, and concise."
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            system=system,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text

    def generate_draft(self, assignment_spec: str, assignment_type: str, course_context: Optional[str] = None) -> str:
        prompt = f"""Assignment type: {assignment_type}\n\nCourse context:\n{course_context or 'None'}\n\nAssignment specification:\n{assignment_spec}\n\nGenerate a review-ready draft that follows the spec closely. Output the draft only."""
        system = "You are a drafting assistant for use inside a local review workflow. Write directly, accurately, and keep the output review-ready."
        response = self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            system=system,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text

    def verify_requirements(self, draft: str, requirements: str) -> dict:
        prompt = f"""Draft:\n{draft}\n\nRequirements:\n{requirements}\n\nReturn JSON with keys: status, missing_items, summary."""
        system = "You are a verification assistant for assignment completeness. Return valid JSON only."
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            system=system,
            messages=[{"role": "user", "content": prompt}],
        )
        try:
            return json.loads(response.content[0].text)
        except Exception:
            return {"status": "error", "missing_items": [], "summary": response.content[0].text}
