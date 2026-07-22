"""Minimal interface for generating text with Groq."""

from __future__ import annotations

from app.config import ConfigurationError, get_settings


class LLMError(RuntimeError):
    """Raised when a response cannot be generated."""


def generate(prompt: str) -> str:
    """Generate a response for *prompt* using the configured Groq model."""
    if not prompt.strip():
        raise LLMError("Prompt cannot be empty.")

    try:
        settings = get_settings()
    except ConfigurationError as error:
        raise LLMError(str(error)) from error

    try:
        from openai import APIError, OpenAI
    except ImportError as error:
        raise LLMError("Missing dependency: run 'pip install -r requirements.txt'.") from error

    try:
        client = OpenAI(
            api_key=settings.api_key,
            base_url=settings.base_url,
            timeout=settings.timeout,
        )
        response = client.responses.create(input=prompt, model=settings.model)
    except APIError as error:
        raise LLMError(f"Groq request failed: {error}") from error

    return response.output_text.strip()
