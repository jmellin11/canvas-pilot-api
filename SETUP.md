# Canvas Pilot API Setup Guide

## Prerequisites

- Python 3.11+
- pip
- A valid Anthropic API key
- Access to your Canvas school login

## 1. Clone the repo

```bash
git clone https://github.com/jmellin11/canvas-pilot-api.git
cd canvas-pilot-api
```

## 2. Create your local environment file

```bash
cp .env.example .env
```

Open `.env` and add your credentials:

```dotenv
CLAUDE_API_KEY=sk-ant-...
CLAUDE_MODEL=claude-3-5-sonnet-20241022
CANVAS_AUTH=cookie
CANVAS_BASE=
CANVAS_WEB_BASE=
```

## 3. Install dependencies

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## 4. Run the API smoke test

```bash
python test_api.py
```

The smoke test verifies:
- the `.env` file loads correctly
- your Anthropic API key is present
- the model endpoint responds successfully

## 5. Begin the Canvas workflow

The repo is structured to mirror the original project. Start by exploring the following modules:

- `src/llm_bridge.py` — API access layer
- `src/canvas_client.py` — Canvas communication
- `src/canvas_credentials.py` — local credential handling
- `src/skills/` — workflow modules

## 6. Security notes

- Keep `.env` local
- Never commit private credentials or cookies
- Keep course-specific details local and in gitignored files

## 7. Recommended next steps

1. Validate Anthropic key connectivity
2. Add Canvas auth handling
3. Implement `canvas_setup.py`
4. Implement `canvas_scan.py`
5. Implement `canvas_execute.py`
6. Add run-result and approval gating logic
