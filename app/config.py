"""Configuration loaded from environment variables."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


DEFAULT_GROQ_BASE_URL = "https://api.groq.com/openai/v1"
DEFAULT_GROQ_MODEL = "openai/gpt-oss-20b"
DEFAULT_GROQ_TIMEOUT = 60.0


class ConfigurationError(ValueError):
    """Raised when the assistant configuration is invalid."""


@dataclass(frozen=True)
class Settings:
    api_key: str
    model: str
    base_url: str
    timeout: float


def get_settings() -> Settings:
    """Load and validate the Groq settings from the environment."""
    load_dotenv()

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ConfigurationError("GROQ_API_KEY is required. Add it to your environment or .env file.")

    timeout_value = os.getenv("GROQ_TIMEOUT", str(DEFAULT_GROQ_TIMEOUT))
    try:
        timeout = float(timeout_value)
    except ValueError as error:
        raise ConfigurationError("GROQ_TIMEOUT must be a number of seconds.") from error
    if timeout <= 0:
        raise ConfigurationError("GROQ_TIMEOUT must be greater than zero.")

    return Settings(
        api_key=api_key,
        model=os.getenv("GROQ_MODEL", DEFAULT_GROQ_MODEL),
        base_url=os.getenv("GROQ_BASE_URL", DEFAULT_GROQ_BASE_URL),
        timeout=timeout,
    )
