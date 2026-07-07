# Este módulo será el único responsable de leer variables de entorno
# y exponerlas al resto de la aplicación.

import os
from dotenv import load_dotenv


class Settings:
    def __init__(self) -> None:
        load_dotenv()

        self.model: str = self._get_env("OLLAMA_MODEL")
        self.host: str = self._get_env("OLLAMA_HOST")

        self.temperature: float = 0.5
        self.timeout: int = 120

        self.log_level: str = "DEBUG"
        self.embedding_model: str = "bge"
        self.vector_db: str = "VectorDB"

    def _get_env(self, key: str) -> str:
        value = os.getenv(key)
        if value is None:
            raise ValueError(f"Missing required environment variable: {key}")
        return value


settings = Settings()
