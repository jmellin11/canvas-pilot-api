#!/usr/bin/env python3
"""Smoke test for the Claude API bridge."""

import os
import sys

from dotenv import load_dotenv

load_dotenv()

from src.llm_bridge import CanvasLLMBridge


def main() -> int:
    api_key = os.getenv("CLAUDE_API_KEY")
    if not api_key or api_key.startswith("sk-ant-YOUR"):
        print("Missing or placeholder CLAUDE_API_KEY in .env")
        return 1

    bridge = CanvasLLMBridge()
    print(f"Model: {bridge.model}")

    ok = bridge.health_check()
    if not ok:
        print("Health check failed. Verify your API key and network access.")
        return 1

    sample = "Write a 1-paragraph answer explaining why local-first review gates are useful in a Canvas workflow."
    result = bridge.analyze_assignment(sample, course_context="CS101")
    print("\nSample analysis:\n")
    print(result[:300])
    print("\nAPI smoke test passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
