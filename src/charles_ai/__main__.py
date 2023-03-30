import dotenv

from . import ai_engine, config, discord_interface


# Load and validate config
config.load()

ai_engine.setup()
discord_interface.start()
