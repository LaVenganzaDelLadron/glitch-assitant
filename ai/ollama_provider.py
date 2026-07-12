#ai/ollama_provider.py
import os
from ai.base import LLMProvider


class OllamaProvider(LLMProvider):

    def __init__(
        self,
        host: str | None = None,
        default_model: str | None = None,
        timeout_seconds: int | None = None
    ):
        try:
            from ollama import Client
        except ImportError:
            raise RuntimeError(
                "Install ollama package to use ollama models"
            )

        timeout = timeout_seconds or int(
            os.environ.get("OLLAMA_TIMEOUT", 120)
        )

        self.client = Client(
            host=host or os.getenv(
                "OLLAMA_HOST",
                "http://127.0.0.1:11434"
            ),
            timeout=timeout
        )

        self.default_model = (
            default_model
            or os.getenv("OLLAMA_MODEL", "llama3.2:3b")
        )

    def generate(
        self,
        prompt: str,
        model: str | None = None
    ) -> str:

        response = self.client.generate(
            model=model or self.default_model,
            prompt=prompt
        )

        return response["response"]