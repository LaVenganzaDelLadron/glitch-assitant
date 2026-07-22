import os
from dotenv import load_dotenv

from app.core.provider.groq import GroqProvider
from app.core.base import LLMProvider

load_dotenv()


def get_llm_provider() -> LLMProvider:
    return GroqProvider()

    raise ValueError(
        f"Unsupported LLM_PROVIDER: {provider_name}. "
        "Use 'groq' or 'ollama'."
    )