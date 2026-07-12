# Glitch Assistant

![Glitch Assistant](./glitch.gif)

Glitch Assistant is a voice-driven CLI AI assistant built with Python. It listens to your microphone, transcribes speech, sends the text to an Ollama model, and speaks the response back.

## Supported OS

- **Arch Linux only** (recommended + tested)

## Features

- Speech-to-text (Whisper via `faster-whisper`)
- Text generation via **Ollama**
- Text-to-speech (pyttsx3)

## Requirements

- Python 3.10+ (best on a fresh Arch install)
- A running **Ollama** server on `http://127.0.0.1:11434`
- Working microphone + speakers

## Install

### 1) Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3) Install system dependencies (Arch)

This project uses:
- `sounddevice` (PortAudio)
- `scipy` (required by `sounddevice` WAV helpers used here)

```bash
sudo pacman -S --needed portaudio libffi alsa-utils
```

If you hit build issues with Python packages:

```bash
sudo pacman -S --needed base-devel python-pip
```

## Configure Ollama

Make sure Ollama is running:

```bash
ollama serve
```

Pull a model (example):

```bash
ollama pull llama3.2:3b
```

Optional environment variables:

- `OLLAMA_HOST` (default: `http://127.0.0.1:11434`)
- `OLLAMA_MODEL` (default: `llama3.2:3b`)
- `OLLAMA_TIMEOUT` (default: `120` seconds)

## Run

```bash
python main.py
```

The app will say: **“Glitch Assistant is online.”**

Then it loops:
1. Records audio (5 seconds)
2. Transcribes it
3. Sends prompt to Ollama
4. Speaks the response

### Exit

Say one of:
- `exit`
- `quit`
- `shutdown`

## Notes / Troubleshooting

- Microphone issues (ALSA):

```bash
arecord -l
```

- Verify Ollama is reachable:

```bash
curl http://127.0.0.1:11434/api/tags
```

