# Glitch Assistant

A small command-line assistant powered by Groq.

## Install

Python 3.10+ is required.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configure

Create a `.env` file in the project root:

```dotenv
GROQ_API_KEY=your-groq-api-key
```

Optional settings:

- `GROQ_MODEL` — defaults to `openai/gpt-oss-20b`
- `GROQ_BASE_URL` — defaults to Groq's OpenAI-compatible API URL
- `GROQ_TIMEOUT` — request timeout in seconds; defaults to `60`

## Run

Pass a prompt directly:

```bash
python main.py "Explain dependency injection simply"
```

Or start interactive mode:

```bash
python main.py
```

Enter `exit`, `quit`, or press `Ctrl-D` to leave interactive mode.
```
