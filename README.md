# Canvas Pilot API

Canvas Pilot API is a local-first Canvas LMS automation tool powered by a direct Claude API backend.

It mirrors the original Canvas Pilot structure while swapping the model layer from an IDE-controlled agent workflow to a Python API-based integration.

## Why this repo exists

The original Canvas Pilot is a strong local-first framework for scanning Canvas, creating approval plans, running per-course skills, and reviewing output before submission. This fork keeps that same structure but replaces the model access pattern with a clean API integration layer so the project can work with a pay-per-use LLM backend.

## Core ideas

- Local-first workflow
- Student approval gate before execution
- Per-course and per-assignment skill routing
- Plan artifacts and run reports
- Direct model calls through an API bridge
- Human review before uploading or submitting

## Quick start

1. Copy `.env.example` to `.env`
2. Add your Anthropic API key
3. Install dependencies:

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
```

4. Run the API smoke test:

```bash
python test_api.py
```

5. Start from the workflow modules in `src/skills/`

## Repository structure

```text
canvas-pilot-api/
├── .agents/
│   └── skills/
│       ├── canvas-setup/
│       ├── canvas-scan/
│       ├── canvas-execute/
│       └── canvas-submit/
├── src/
│   ├── __init__.py
│   ├── llm_bridge.py
│   ├── canvas_client.py
│   ├── canvas_credentials.py
│   └── skills/
│       ├── __init__.py
│       ├── canvas_setup.py
│       ├── canvas_scan.py
│       ├── canvas_execute.py
│       └── canvas_submit.py
├── docs/
├── examples/
├── scripts/
├── sources/
├── tests/
├── .env.example
├── .gitignore
├── README.md
├── SETUP.md
├── requirements.txt
├── LICENSE
└── test_api.py
```

## License

This project is licensed under the GNU Affero General Public License v3.0 or later.
