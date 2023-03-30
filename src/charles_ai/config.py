import os


ai_name = "Charles"


def validate_env():
    """Ensures that all required environment variables are present, or throws an error if they are not."""
    if not os.getenv("OPENAI_API_KEY"):
        raise KeyError("Missing required environment variable: OPENAI_API_KEY")
    if not os.getenv("DISCORD_BOT_TOKEN"):
        raise KeyError("Missing required environment variable: DISCORD_BOT_TOKEN")
    if not os.getenv("ALLOWED_USER_ID"):
        raise KeyError("Missing required environment variable: ALLOWED_USER_ID")
    if not os.getenv("AI_USER_INFO"):
        raise KeyError("Missing required environment variable: AI_USER_INFO")
        
    # Optional environment variables
    env_ai_name = os.getenv("AI_NAME")
    if env_ai_name:
        global ai_name
        ai_name = env_ai_name
