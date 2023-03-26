import os

import discord

from . import ai_engine


# Setup discord client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    """Event handler for bot coming online. DMs the allowed user that it is ready."""
    user = await client.fetch_user(os.getenv("ALLOWED_USER_ID"))
    await user.send("Systems are now fully operational.")


@client.event
async def on_message(message):
    # Don't have the bot reply to itself.
    if message.author == client.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        if not message.content.startswith("?"):
            await message.reply(ai_engine.ask(message.content))


def start():
    client.run(os.getenv("DISCORD_BOT_TOKEN"))
