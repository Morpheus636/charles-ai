import logging
import os

import dotenv


ai_name = "Charles"
units = "metric"


def load():
    """Loads a dotenv, then ensures that all required environment variables are present, or throws an error if they are not."""
    dotenv.load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        raise KeyError("Missing required environment variable: OPENAI_API_KEY")
    if not os.getenv("DISCORD_BOT_TOKEN"):
        raise KeyError("Missing required environment variable: DISCORD_BOT_TOKEN")
    if not os.getenv("ALLOWED_USER_ID"):
        raise KeyError("Missing required environment variable: ALLOWED_USER_ID")
    if not os.getenv("AI_USER_INFO"):
        raise KeyError("Missing required environment variable: AI_USER_INFO")

    # Optional env var - Set log level
    log_level = int(os.getenv("LOG_LEVEL"))
    if not log_level:
        log_level = 30

    logging.basicConfig(level=log_level)

    # Optional environment variables
    env_ai_name = os.getenv("AI_NAME")
    if env_ai_name:
        global ai_name
        ai_name = env_ai_name

    env_units = os.getenv("UNITS")
    if env_units:
        global units
        units = env_units
