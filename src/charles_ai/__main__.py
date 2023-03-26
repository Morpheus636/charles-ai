from . import discord_interface
from . import ai_engine

import dotenv
from . import config

# Load and validate config
dotenv.load_dotenv()
config.validate_env()

ai_engine.setup()
discord_interface.start()
