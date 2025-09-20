import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration class for the Personal Assistant API."""

    # OpenAI Configuration
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "enter-api-key")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o")
    OPENAI_TEMPERATURE: float = float(os.getenv("OPENAI_TEMPERATURE", 1))

    # TAVILY
    TAVILY_SEARCH_KEY: str = os.getenv("TAVILY_SEARCH_KEY", "enter tavily-key")
    MAX_RESULTS: int = int(os.getenv("MAX_RESULTS", 5))

    # Slack Configuration
    SLACK_BOT_TOKEN: str = os.getenv("SLACK_BOT_TOKEN", "xo-bot-token")
    SLACK_SIGNING_SECRET: str = os.getenv("SLACK_SIGNING_SECRET", "signing-secret")

    # Google API Configuration
    GOOGLE_CREDENTIALS_FILE: str = os.getenv("GOOGLE_CREDENTIALS_FILE", "credentials.json")
    GOOGLE_TOKEN_FILE: str = os.getenv("GOOGLE_TOKEN_FILE", "token.json")
    GOOGLE_SCOPES: list = [
        "https://www.googleapis.com/auth/calendar",
        "https://mail.google.com/",
    ]

    # Timezone Configuration
    DEFAULT_TIMEZONE: str = os.getenv("DEFAULT_TIMEZONE", "Asia/Kolkata")

    # Weather API Configuration
    OPEN_METEO_URL: str = os.getenv("OPEN_METEO_URL", "https://api.open-meteo.com/v1/forecast")
    NOMINATIM_URL: str = os.getenv("NOMINATIM_URL", "https://nominatim.openstreetmap.org/search")


# Initialize and validate configuration
config = Config()
