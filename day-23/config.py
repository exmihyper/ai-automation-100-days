from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    CF_ACCOUNT_ID: str
    CF_API_TOKEN: str
    CF_MODEL: str = "@cf/qwen/qwen3-30b-a3b-fp8"

settings = Settings()