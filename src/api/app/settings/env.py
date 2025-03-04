from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )
    OLLAMA_URL: str = Field(
        title="Ollama URL",
        description="The URL of the Ollama API",
        examples=["https://ollama.com"]
    )
    