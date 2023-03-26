import dotenv

from . import ai_engine, config, discord_interface


# Load and validate config
dotenv.load_dotenv()
config.validate_env()

ai_engine.setup()
discord_interface.start()
